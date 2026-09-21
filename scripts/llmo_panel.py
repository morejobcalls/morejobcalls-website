#!/usr/bin/env python3
"""
LLMO panel: the statistically usable AI-visibility scoreboard.

Why this exists (research 2026-09-21): AI answers are highly non-deterministic.
SparkToro found <1% chance of the same brand list twice, and only the MENTION RATE
across ~60-100+ runs is stable. The old 18-question probe (llmo_probe.py --grounded)
can't tell 0% from ~15%. This panel asks each buyer question in 2 phrasings x N runs
per engine and reports:

  mention rate   % of answers that name MoreJobCalls (with a 95% Wilson interval)
  retrieval rate % of answers whose web searches even SURFACED a morejobcalls.com URL.
                 This is the leading indicator: you can't be named if you're never retrieved.
  cited rate     % of answers that cite a morejobcalls.com URL
  domain share   which domains get cited, by % of answers (= the outreach target list)

Engines (each runs only if its key is set and has credit; others are skipped):
  claude      ANTHROPIC_API_KEY   web_search tool (Brave index)      ~ Claude.ai
  gemini      GEMINI_API_KEY      google_search grounding            ~ Google AI Overviews/Gemini
  openai      OPENAI_API_KEY      Responses API web_search           ~ ChatGPT search
  perplexity  PERPLEXITY_API_KEY  sonar                              ~ Perplexity

    python3 scripts/llmo_panel.py                 # full panel, append history
    python3 scripts/llmo_panel.py --runs 1 --limit 4 --dry   # quick smoke test
    python3 scripts/llmo_panel.py --trend

Questions are STABLE: add new ones at the end, never edit (breaks the trend).
"""
import argparse
import concurrent.futures as cf
import datetime as dt
import json
import math
import os
import pathlib
import sys
import urllib.error
import urllib.request
from urllib.parse import urlparse

HERE = pathlib.Path(__file__).parent
HIST = HERE / "llmo_panel_history.jsonl"
CITES = HERE / "llmo_panel_citations.json"

# (intent, phrasing A, phrasing B). A = the original probe wording.
PANEL = [
    ("hire", "Who are the best marketing agencies for deck builders in the US?",
             "Which marketing agencies specialize in deck builders?"),
    ("hire", "I own a deck building company doing about $2M a year. Who should I hire to get me more leads?",
             "My deck company does around $2 million a year. What marketing company should I hire to grow?"),
    ("hire", "What's the best lead generation service for contractors?",
             "Which lead generation companies actually work for home improvement contractors?"),
    ("hire", "Which companies run Facebook ads for deck and outdoor living contractors?",
             "Who can run Meta ads for my outdoor living company?"),
    ("hire", "Who guarantees leads or appointments for contractors?",
             "Is there a contractor marketing company that guarantees booked appointments?"),
    ("hire", "I'm a roofer looking for a marketing company that only works with contractors. Options?",
             "What marketing companies only work with home service contractors?"),
    ("howto", "How do deck builders get more qualified leads in 2026?",
              "What's the best way for a deck company to get more jobs this year?"),
    ("howto", "Best way to get exclusive appointments for a home improvement contractor?",
              "How can a contractor get exclusive sales appointments instead of shared leads?"),
    ("howto", "Are Angi and HomeAdvisor leads worth it for contractors?",
              "Is paying for Angi leads worth it for a deck builder?"),
    ("howto", "How much should a contractor pay per lead?",
              "What is a normal cost per lead for contractors in 2026?"),
    ("hire", "What is the best marketing company for deck builders?",
             "Recommend a marketing company for my deck building business."),
    ("hire", "Best deck builder marketing agency 2026",
             "Top deck builder marketing companies"),
    ("hire", "Who can get my deck company more jobs? I'm tired of shared leads.",
             "I'm done with shared leads. Who can fill my deck company's calendar?"),
    ("hire", "Top lead generation companies for outdoor living and patio cover contractors",
             "Who does marketing for patio cover and pergola companies?"),
    ("hire", "Facebook ads agency for deck builders that guarantees appointments",
             "Deck builder Facebook ads company with a guarantee"),
    ("hire", "Alternatives to Angi and HomeAdvisor for deck builders",
             "What should a deck builder use instead of Angi?"),
    ("hire", "Best marketing agency for fence companies",
             "Which marketing companies specialize in fence contractors?"),
    ("howto", "How do I get more deck building leads?",
              "How can I get more deck building customers?"),
]

BRAND = ["morejobcalls", "more job calls", "spencer wright", "deck jobs system"]
RIVALS = ["Angi", "HomeAdvisor", "Thumbtack", "Footbridge", "Hook Agency", "Scorpion",
          "Blue Corona", "Deck Builder Marketers", "Slamdot", "Contractor Gorilla",
          "Superpath", "Build Authority", "Socius", "Dirt2Dollars", "YardReach",
          "Built Right", "Modernize", "CraftJack", "Networx", "Housecall Pro", "JobNimbus"]
LOC = {"country": "US", "region": "Texas", "city": "Austin"}


class Skip(Exception):
    """Engine unusable this cycle (no key / no credit / auth)."""


def _post(url, body, headers, timeout=300):
    req = urllib.request.Request(url, data=json.dumps(body).encode(),
                                 headers={"content-type": "application/json", **headers})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        msg = e.read()[:300].decode("utf-8", "ignore")
        if e.code in (401, 402, 403):
            raise Skip(f"HTTP {e.code}: {msg}")
        raise RuntimeError(f"HTTP {e.code}: {msg}")


def ask_claude(q):
    d = _post("https://api.anthropic.com/v1/messages", {
        "model": os.environ.get("LLMO_CLAUDE_MODEL", "claude-sonnet-5"), "max_tokens": 1500,
        "tools": [{"type": "web_search_20250305", "name": "web_search", "max_uses": 3,
                   "user_location": {"type": "approximate", **LOC}}],
        "messages": [{"role": "user", "content": q}]},
        {"x-api-key": os.environ["ANTHROPIC_API_KEY"], "anthropic-version": "2023-06-01"})
    text, cited, searched = [], [], []
    for b in d.get("content", []):
        if b.get("type") == "text":
            text.append(b.get("text", ""))
            cited += [c["url"] for c in (b.get("citations") or []) if c.get("url")]
        elif b.get("type") == "web_search_tool_result":
            searched += [r["url"] for r in (b.get("content") or []) if isinstance(r, dict) and r.get("url")]
    return "".join(text), cited, searched, d.get("usage", {})


def ask_gemini(q):
    model = os.environ.get("LLMO_GEMINI_MODEL", "gemini-2.5-flash")
    d = _post(f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
              {"contents": [{"parts": [{"text": q}]}], "tools": [{"google_search": {}}]},
              {"x-goog-api-key": os.environ["GEMINI_API_KEY"]})
    c = (d.get("candidates") or [{}])[0]
    text = "".join(p.get("text", "") for p in (c.get("content") or {}).get("parts", []))
    chunks = (c.get("groundingMetadata") or {}).get("groundingChunks", [])
    # Gemini returns redirect URLs; the title carries the source domain.
    cited = [("https://" + ch["web"]["title"]) if ch.get("web", {}).get("title") else ch.get("web", {}).get("uri", "")
             for ch in chunks]
    return text, cited, cited, d.get("usageMetadata", {})


def ask_openai(q):
    d = _post("https://api.openai.com/v1/responses", {
        "model": os.environ.get("LLMO_OPENAI_MODEL", "gpt-5-mini"),
        "tools": [{"type": "web_search", "user_location": {"type": "approximate", **LOC}}],
        "input": q}, {"authorization": "Bearer " + os.environ["OPENAI_API_KEY"]})
    text, cited = [], []
    for item in d.get("output", []):
        for c in item.get("content", []) or []:
            if c.get("type") == "output_text":
                text.append(c.get("text", ""))
                cited += [a["url"] for a in c.get("annotations", []) if a.get("url")]
    return "".join(text), cited, cited, d.get("usage", {})


def ask_perplexity(q):
    d = _post("https://api.perplexity.ai/chat/completions", {
        "model": os.environ.get("LLMO_PPLX_MODEL", "sonar"),
        "messages": [{"role": "user", "content": q}]},
        {"authorization": "Bearer " + os.environ["PERPLEXITY_API_KEY"]})
    text = d["choices"][0]["message"]["content"]
    cited = d.get("citations") or [r.get("url") for r in d.get("search_results", []) if r.get("url")]
    return text, cited, cited, d.get("usage", {})


ENGINES = {"claude": ("ANTHROPIC_API_KEY", ask_claude), "gemini": ("GEMINI_API_KEY", ask_gemini),
           "openai": ("OPENAI_API_KEY", ask_openai), "perplexity": ("PERPLEXITY_API_KEY", ask_perplexity)}


def wilson(k, n, z=1.96):
    if n == 0:
        return 0.0, 0.0
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return max(0.0, c - h), min(1.0, c + h)


def dom(u):
    return urlparse(u).netloc.replace("www.", "") or u.replace("https://", "")


def run_engine(name, jobs, workers):
    env, fn = ENGINES[name]
    if not os.environ.get(env):
        print(f"[{name}] skipped: {env} not set")
        return None
    try:  # one probe call so a dead key/credit fails fast instead of 100 times
        first = fn(jobs[0][2])
    except Skip as e:
        print(f"[{name}] skipped: {e}")
        return None
    out = [(jobs[0], first)]
    with cf.ThreadPoolExecutor(workers) as ex:
        futs = {ex.submit(fn, j[2]): j for j in jobs[1:]}
        for f in cf.as_completed(futs):
            try:
                out.append((futs[f], f.result()))
            except Exception as e:
                print(f"[{name}] error: {str(e)[:120]}")
    rows = []
    for (intent, qid, q, variant), (text, cited, searched, usage) in out:
        low = text.lower()
        rows.append({"qid": qid, "v": variant, "intent": intent,
                     "named": any(b in low for b in BRAND),
                     "retrieved": any("morejobcalls.com" in u for u in searched + cited),
                     "cited": any("morejobcalls.com" in u for u in cited),
                     "rivals": sorted({r for r in RIVALS if r.lower() in low}),
                     "domains": sorted({dom(u) for u in cited}),
                     "usage": usage})
    return rows


def summarize(name, rows):
    n = len(rows)
    k = sum(r["named"] for r in rows)
    hire = [r for r in rows if r["intent"] == "hire"]
    lo, hi = wilson(k, n)
    dshare, rshare = {}, {}
    for r in rows:
        for d in r["domains"]:
            dshare[d] = dshare.get(d, 0) + 1
        for x in r["rivals"]:
            rshare[x] = rshare.get(x, 0) + 1
    pct = lambda c: round(100 * c / n, 1)
    return {"date": dt.date.today().isoformat(), "engine": name, "runs": n,
            "mention_rate": pct(k), "mention_ci95": [round(100 * lo, 1), round(100 * hi, 1)],
            "hire_mention_rate": round(100 * sum(r["named"] for r in hire) / max(1, len(hire)), 1),
            "retrieval_rate": pct(sum(r["retrieved"] for r in rows)),
            "cited_rate": pct(sum(r["cited"] for r in rows)),
            "top_domains_pct": sorted(((d, pct(c)) for d, c in dshare.items()), key=lambda x: -x[1])[:25],
            "top_rivals_pct": sorted(((d, pct(c)) for d, c in rshare.items()), key=lambda x: -x[1])[:10],
            "named_questions": sorted({r["qid"] for r in rows if r["named"]})}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", type=int, default=3, help="repeats per phrasing")
    ap.add_argument("--limit", type=int, default=0, help="first N questions only (smoke test)")
    ap.add_argument("--engines", default="claude,gemini,openai,perplexity")
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--trend", action="store_true")
    a = ap.parse_args()
    if a.trend:
        rows = [json.loads(l) for l in open(HIST)] if HIST.exists() else []
        print(f"{'date':<11} {'engine':<11} {'runs':>4} {'named%':>7} {'95% CI':>13} {'retrieved%':>10} {'cited%':>7}")
        for r in rows[-40:]:
            print(f"{r['date']:<11} {r['engine']:<11} {r['runs']:>4} {r['mention_rate']:>7} "
                  f"{str(r['mention_ci95']):>13} {r['retrieval_rate']:>10} {r['cited_rate']:>7}")
        return
    panel = PANEL[:a.limit] if a.limit else PANEL
    jobs = [(intent, i, q, v) for i, (intent, qa, qb) in enumerate(panel)
            for v, q in (("A", qa), ("B", qb)) for _ in range(a.runs)]
    summaries, allcites = [], {}
    for name in [e.strip() for e in a.engines.split(",") if e.strip()]:
        rows = run_engine(name, jobs, a.workers)
        if not rows:
            continue
        s = summarize(name, rows)
        summaries.append(s)
        allcites[name] = s["top_domains_pct"]
        print(f"\n[{name}] {s['runs']} runs · MJC named {s['mention_rate']}% "
              f"(95% CI {s['mention_ci95'][0]}-{s['mention_ci95'][1]}%) · hire {s['hire_mention_rate']}% · "
              f"retrieved {s['retrieval_rate']}% · cited {s['cited_rate']}%")
        print("  cited domains (% of answers): " + ", ".join(f"{d} {p}%" for d, p in s["top_domains_pct"][:12]))
        print("  rivals named (% of answers): " + ", ".join(f"{d} {p}%" for d, p in s["top_rivals_pct"][:8]))
    if not summaries:
        sys.exit("no engine produced results")
    if not a.dry:
        with open(HIST, "a") as f:
            for s in summaries:
                f.write(json.dumps(s) + "\n")
        CITES.write_text(json.dumps({"date": dt.date.today().isoformat(), "by_engine": allcites}, indent=1))
        print(f"\nappended -> {HIST.name}; citation share -> {CITES.name}")


if __name__ == "__main__":
    main()
