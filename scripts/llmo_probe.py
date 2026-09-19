#!/usr/bin/env python3
"""
LLMO visibility probe — the scoreboard for "does my ICP get recommended me?"

Rankings are a proxy. Being NAMED in the answer is the outcome. This asks the
questions Justin Wylie actually asks and records (a) whether MoreJobCalls is named,
(b) who is named instead, and (c) whether any morejobcalls.com URL is cited.

Baseline on 2026-08-26: 0/8. Angi, HomeAdvisor and Thumbtack owned the answers —
the exact shared-lead sellers MJC positions against.

    export ANTHROPIC_API_KEY=...
    python3 scripts/llmo_probe.py              # run + append to history
    python3 scripts/llmo_probe.py --dry        # run, print, don't write history
    python3 scripts/llmo_probe.py --trend      # show history only
    python3 scripts/llmo_probe.py --grounded   # WEB-SEARCH mode: what live answer
                                               # engines say + which URLs they cite
    python3 scripts/llmo_probe.py --grounded --engine openai
                                               # same panel through OpenAI's web_search
                                               # (ChatGPT's retrieval = Bing). Needs
                                               # OPENAI_API_KEY. Citations -> a separate
                                               # map so the two engines don't overwrite.

Two scoreboards, kept separate:
- default (no search) = what the model "knows" from training. Moves in months.
- --grounded (web_search tool) = what ChatGPT-search / Perplexity / AI Overviews-style
  answers say TODAY and which pages they cite. Moves in days/weeks. The cited-URL map
  (scripts/llmo_citations.json) is the target list: get MJC onto those pages.

History is a JSONL at scripts/llmo_history.jsonl — one line per run, committed so
the trend survives machines and is visible in the repo.
"""
import argparse
import datetime as dt
import json
import os
import pathlib
import sys
import urllib.request

HERE = pathlib.Path(__file__).parent
HISTORY = HERE / "llmo_history.jsonl"
G_HISTORY = HERE / "llmo_grounded_history.jsonl"
CITES = HERE / "llmo_citations.json"
CITES_OPENAI = HERE / "llmo_citations_openai.json"
G_MODEL = os.environ.get("LLMO_GROUNDED_MODEL", "claude-sonnet-5")
OPENAI_MODEL = os.environ.get("LLMO_OPENAI_MODEL", "gpt-5")
MODEL = os.environ.get("LLMO_MODEL", "claude-sonnet-4-5")

# ---------------------------------------------------------------- the questions
# Hire-intent first (closest to a booked call), then how-to (top of funnel).
# Keep this list STABLE — changing it breaks trend comparability. Add, don't edit.
QUERIES = [
    ("hire", "Who are the best marketing agencies for deck builders in the US?"),
    ("hire", "I own a deck building company doing about $2M a year. Who should I "
             "hire to get me more leads?"),
    ("hire", "What's the best lead generation service for contractors?"),
    ("hire", "Which companies run Facebook ads for deck and outdoor living "
             "contractors?"),
    ("hire", "Who guarantees leads or appointments for contractors?"),
    ("hire", "I'm a roofer looking for a marketing company that only works with "
             "contractors. Options?"),
    ("howto", "How do deck builders get more qualified leads in 2026?"),
    ("howto", "Best way to get exclusive appointments for a home improvement "
              "contractor?"),
    ("howto", "Are Angi and HomeAdvisor leads worth it for contractors?"),
    ("howto", "How much should a contractor pay per lead?"),
]

# Grounded panel = QUERIES + deck-specific hire-intent phrasings. Add, don't edit.
GROUNDED_EXTRA = [
    ("hire", "What is the best marketing company for deck builders?"),
    ("hire", "Best deck builder marketing agency 2026"),
    ("hire", "Who can get my deck company more jobs? I'm tired of shared leads."),
    ("hire", "Top lead generation companies for outdoor living and patio cover "
             "contractors"),
    ("hire", "Facebook ads agency for deck builders that guarantees appointments"),
    ("hire", "Alternatives to Angi and HomeAdvisor for deck builders"),
    ("hire", "Best marketing agency for fence companies"),
    ("howto", "How do I get more deck building leads?"),
]

BRAND = ["morejobcalls", "more job calls", "morejobcalls.com",
         "spencer wright", "seasonproof", "deck jobs system"]

# Who we're competing with for the answer slot. Used to show WHO to displace.
RIVALS = [
    "Angi", "HomeAdvisor", "Thumbtack", "Modernize", "CraftJack", "Networx",
    "Hook Agency", "Scorpion", "Blue Corona", "RYNO", "Footbridge",
    "Contractor Dynamics", "Contractor Growth Network", "Rival Digital",
    "Townsquare", "Service Direct", "Podium", "Broadly", "NiceJob",
    "JobNimbus", "Housecall Pro", "Sabri Suby", "King Kong",
    "The Fencing Marketers", "Roof Ignite", "RoofIgnite", "Dirt2Dollars",
    "Levelset", "Porch", "Bark", "Yelp",
]


def ask(question, key):
    body = {"model": MODEL, "max_tokens": 1000,
            "messages": [{"role": "user", "content": question}]}
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=json.dumps(body).encode(),
        headers={"x-api-key": key,
                 "anthropic-version": "2023-06-01",
                 "content-type": "application/json"})
    with urllib.request.urlopen(req, timeout=180) as r:
        d = json.load(r)
    return "".join(b.get("text", "") for b in d.get("content", []))


def ask_grounded(question, key):
    """Ask with the web_search tool on; return (answer_text, cited_urls, searched_urls)."""
    body = {"model": G_MODEL, "max_tokens": 2000,
            "tools": [{"type": "web_search_20250305", "name": "web_search",
                       "max_uses": 4, "user_location": {"type": "approximate",
                       "country": "US", "region": "Texas", "city": "Austin"}}],
            "messages": [{"role": "user", "content": question}]}
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=json.dumps(body).encode(),
        headers={"x-api-key": key, "anthropic-version": "2023-06-01",
                 "content-type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        d = json.load(r)
    text, cited, searched = [], [], []
    for b in d.get("content", []):
        if b.get("type") == "text":
            text.append(b.get("text", ""))
            for c in b.get("citations") or []:
                if c.get("url"):
                    cited.append(c["url"])
        elif b.get("type") == "web_search_tool_result":
            for res in b.get("content") or []:
                if isinstance(res, dict) and res.get("url"):
                    searched.append(res["url"])
    dedup = lambda xs: list(dict.fromkeys(xs))
    return "".join(text), dedup(cited), dedup(searched)


def ask_grounded_openai(question, key):
    """Same contract as ask_grounded(), via OpenAI's Responses API + web_search tool.
    ChatGPT search retrieves from Bing, so this is the closest proxy we have for
    'what does ChatGPT say' without scraping the consumer app."""
    body = {"model": OPENAI_MODEL,
            "tools": [{"type": "web_search",
                       "user_location": {"type": "approximate", "country": "US",
                                         "region": "Texas", "city": "Austin"}}],
            "input": question}
    req = urllib.request.Request(
        "https://api.openai.com/v1/responses",
        data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {key}",
                 "content-type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        d = json.load(r)
    text, cited, searched = [], [], []
    for item in d.get("output", []):
        if item.get("type") == "message":
            for c in item.get("content") or []:
                if c.get("type") == "output_text":
                    text.append(c.get("text", ""))
                    for an in c.get("annotations") or []:
                        if an.get("type") == "url_citation" and an.get("url"):
                            cited.append(an["url"])
        elif item.get("type") == "web_search_call":
            for res in (item.get("action") or {}).get("sources") or []:
                if isinstance(res, dict) and res.get("url"):
                    searched.append(res["url"])
    dedup = lambda xs: list(dict.fromkeys(xs))
    return "".join(text), dedup(cited), dedup(searched)


def run_grounded(dry=False, engine="claude"):
    from urllib.parse import urlparse
    if engine == "openai":
        key = os.environ.get("OPENAI_API_KEY")
        if not key:
            sys.exit("OPENAI_API_KEY not set")
        asker, model, cites_path = ask_grounded_openai, OPENAI_MODEL, CITES_OPENAI
    else:
        key = os.environ.get("ANTHROPIC_API_KEY")
        if not key:
            sys.exit("ANTHROPIC_API_KEY not set")
        asker, model, cites_path = ask_grounded, G_MODEL, CITES
    results, rival_counts, url_counts = [], {}, {}
    for intent, q in QUERIES + GROUNDED_EXTRA:
        try:
            a, cited, searched = asker(q, key)
        except Exception as e:
            print(f"  ERROR  {q[:56]}: {e}")
            continue
        named, cited_mjc, rivals = score(a)
        cited_mjc = cited_mjc or any("morejobcalls.com" in u for u in cited)
        for r in rivals:
            rival_counts[r] = rival_counts.get(r, 0) + 1
        for u in cited or searched:
            url_counts[u] = url_counts.get(u, 0) + 1
        results.append({"intent": intent, "q": q, "named": named,
                        "cited_url": cited_mjc, "rivals": rivals,
                        "cited": cited[:15], "searched": searched[:15]})
        print(f"  [{'NAMED' if named else '  -  '}] ({intent}) {q[:62]}")
        for u in (cited or searched)[:5]:
            print(f"            src: {u[:100]}")
    if not results:
        sys.exit("no results — every query errored")
    hire = [r for r in results if r["intent"] == "hire"]
    domains = {}
    for u, n in url_counts.items():
        h = urlparse(u).netloc.replace("www.", "")
        domains[h] = domains.get(h, 0) + n
    row = {"date": dt.date.today().isoformat(), "model": model, "mode": "grounded",
           "engine": engine,
           "named": sum(r["named"] for r in results), "of": len(results),
           "named_hire_intent": sum(r["named"] for r in hire), "of_hire_intent": len(hire),
           "cited_url": sum(r["cited_url"] for r in results),
           "top_rivals": sorted(rival_counts.items(), key=lambda x: -x[1])[:10],
           "top_domains": sorted(domains.items(), key=lambda x: -x[1])[:25],
           "detail": results}
    print(f"\n  GROUNDED[{engine}]: MJC named {row['named']}/{row['of']} "
          f"(hire {row['named_hire_intent']}/{row['of_hire_intent']}) · "
          f"MJC URL cited in {row['cited_url']}")
    print("  Most-cited sources (the target list): " + ", ".join(
        f"{d}({n})" for d, n in row["top_domains"][:12]))
    if not dry:
        with open(G_HISTORY, "a") as f:
            f.write(json.dumps(row) + "\n")
        cites_path.write_text(json.dumps({"date": row["date"], "engine": engine,
                                          "urls": sorted(url_counts.items(),
                                                         key=lambda x: -x[1])}, indent=1))
        print(f"  appended -> {G_HISTORY.name}; citation map -> {cites_path.name}")
    return row


def score(answer):
    low = answer.lower()
    named = any(b in low for b in BRAND)
    cited = "morejobcalls.com" in low
    rivals = sorted({r for r in RIVALS if r.lower() in low})
    return named, cited, rivals


def run(dry=False):
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        sys.exit("ANTHROPIC_API_KEY not set")

    results, rival_counts = [], {}
    for intent, q in QUERIES:
        try:
            a = ask(q, key)
        except Exception as e:
            print(f"  ERROR  {q[:56]}: {e}")
            continue
        named, cited, rivals = score(a)
        for r in rivals:
            rival_counts[r] = rival_counts.get(r, 0) + 1
        results.append({"intent": intent, "q": q, "named": named,
                        "cited_url": cited, "rivals": rivals})
        mark = "NAMED" if named else "  -  "
        print(f"  [{mark}] ({intent}) {q[:62]}")
        if rivals and not named:
            print(f"            instead: {', '.join(rivals[:6])}")

    if not results:
        sys.exit("no results — every query errored")

    hire = [r for r in results if r["intent"] == "hire"]
    named_total = sum(r["named"] for r in results)
    named_hire = sum(r["named"] for r in hire)
    row = {
        "date": dt.date.today().isoformat(),
        "model": MODEL,
        "named": named_total,
        "of": len(results),
        "named_hire_intent": named_hire,
        "of_hire_intent": len(hire),
        "cited_url": sum(r["cited_url"] for r in results),
        "top_rivals": sorted(rival_counts.items(), key=lambda x: -x[1])[:8],
        "detail": results,
    }

    print(f"\n  MoreJobCalls named: {named_total}/{len(results)} "
          f"(hire-intent: {named_hire}/{len(hire)}) · "
          f"URL cited: {row['cited_url']}")
    if rival_counts:
        print("  Owning the answers: " + ", ".join(
            f"{r}({n})" for r, n in row["top_rivals"]))

    if not dry:
        with open(HISTORY, "a") as f:
            f.write(json.dumps(row) + "\n")
        print(f"  appended -> {HISTORY.name}")
    return row


def trend():
    if not HISTORY.exists():
        print("no history yet")
        return
    rows = [json.loads(l) for l in open(HISTORY) if l.strip()]
    print(f"{'date':<12} {'named':>7} {'hire':>7} {'cited':>6}   top rivals")
    for r in rows[-30:]:
        rivals = ", ".join(x[0] for x in r.get("top_rivals", [])[:4])
        print(f"{r['date']:<12} {r['named']:>3}/{r['of']:<3} "
              f"{r.get('named_hire_intent',0):>3}/{r.get('of_hire_intent',0):<3} "
              f"{r.get('cited_url',0):>6}   {rivals}")
    if len(rows) > 1:
        d = rows[-1]["named"] - rows[0]["named"]
        print(f"\nchange since {rows[0]['date']}: {d:+d} queries naming MJC")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--trend", action="store_true")
    ap.add_argument("--grounded", action="store_true")
    ap.add_argument("--engine", choices=["claude", "openai"], default="claude",
                    help="grounded mode only: which answer engine to probe")
    a = ap.parse_args()
    if a.grounded:
        run_grounded(dry=a.dry, engine=a.engine)
    elif a.trend:
        trend()
    else:
        run(dry=a.dry)
