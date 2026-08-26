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
    a = ap.parse_args()
    if a.trend:
        trend()
    else:
        run(dry=a.dry)
