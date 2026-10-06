#!/usr/bin/env python3
"""Outrank scoreboard: real Google positions for morejobcalls.com vs the sites we are
trying to beat, on a fixed deck-builder keyword basket.

Rivals:
  - deckbuildermarketing.com  -> 301 -> deckmarketing.com -> 301 -> slamdot.com/industries/decking/
    (the literal domain Spencer named; its equity now lives on Slamdot's decking page)
  - deckbuildermarketers.com  (Deck Builder Marketers / April Edwards, #1 on most of the basket)

Data: Apify `apify/google-search-scraper`, US/en, desktop, 5 pages deep (top ~50).
Needs APIFY_TOKEN in the environment (GitHub Actions secret, or Claude Code/.env locally).

Usage:
  python3 scripts/rank_tracker.py            # run, append to rank_history.jsonl, print scorecard
  python3 scripts/rank_tracker.py --report   # print scorecard + trend from history only
  python3 scripts/rank_tracker.py --from-serp serp.json --date 2026-09-10   # import raw Apify output

The keyword basket is deliberately stable. ADD keywords if you must; never edit or remove,
or the trend stops being comparable.
"""
import json, os, sys, time, urllib.request, urllib.error, datetime


class NoData(Exception):
    """The scoreboard could not be measured. This is NOT a finding about the site."""
from urllib.parse import urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
HISTORY = os.path.join(HERE, "rank_history.jsonl")
RUN_TIMEOUT_SECS = 600  # actor budget (the 10/05 run needed ~5 min); the GitHub job allows 15 min total

# CORE = the win condition. EXTENDED = tracked for opportunity, not scored.
CORE = [
    "deck builder marketing",
    "marketing for deck builders",
    "deck builder marketing agency",
    "deck contractor marketing",
    "best marketing agency for deck builders",
    "deck builder advertising",
    "deck builder seo",
    "deck builder leads",
    "deck builder lead generation",
    "leads for deck builders",
    "facebook ads for deck builders",
    "how to get more deck jobs",
]
EXTENDED = [
    "deck company marketing",
    "marketing for deck contractors",
    "decking leads",
    "how to get deck leads",
    "deck builder marketing ideas",
    "outdoor living contractor marketing",
    "fence company marketing",
    "patio cover marketing",
]

TRACKED = {
    "mjc": ["morejobcalls.com"],
    "slamdot": ["slamdot.com", "deckmarketing.com", "deckbuildermarketing.com"],
    "dbm": ["deckbuildermarketers.com"],
    "footbridge": ["footbridgemedia.com"],
    "deckfence": ["deckfencemarketers.com"],
}
DEPTH_PAGES = 5


def host(u):
    return urlparse(u).netloc.lower().removeprefix("www.")


def parse(items):
    """Apify dataset items (one per keyword per page) -> {kw: {site: [pos, url] | None}}"""
    rows = {}
    for q in items:
        kw = q["searchQuery"]["term"]
        page = q["searchQuery"].get("page", 1) or 1
        for i, r in enumerate(q.get("organicResults", [])):
            pos = r.get("position") or i + 1
            # Apify positions restart per page on some runs; normalise to absolute.
            absolute = pos if pos > (page - 1) * 10 else (page - 1) * 10 + pos
            rows.setdefault(kw, []).append((absolute, host(r["url"]), r["url"]))
    out = {}
    for kw, lst in rows.items():
        lst.sort()
        best = {}
        for site, domains in TRACKED.items():
            hit = next(((p, u) for p, h, u in lst if any(h == d or h.endswith("." + d) for d in domains)), None)
            best[site] = list(hit) if hit else None
        best["_depth"] = len(lst)
        out[kw] = best
    return out


def fetch(keywords):
    tok = os.environ.get("APIFY_TOKEN") or os.environ.get("APIFY_API_TOKEN")
    if not tok:
        sys.exit("APIFY_TOKEN not set")
    body = {
        "queries": "\n".join(keywords),
        "resultsPerPage": 10,
        "maxPagesPerQuery": DEPTH_PAGES,
        "countryCode": "us",
        "languageCode": "en",
        "mobileResults": False,
        "saveHtml": False,
    }
    # 2026-10-06: the run-sync endpoint hard-caps at 300 s, and 20 keywords x DEPTH_PAGES pages takes ~5 min,
    # so runs TIMED-OUT one page short (run uzexbTmKaEmJvLeFU: 99/100 pages). Start the run, poll it, then read the dataset.
    base = "https://api.apify.com/v2"
    hdr = {"Content-Type": "application/json", "Authorization": f"Bearer {tok}"}
    try:
        req = urllib.request.Request(f"{base}/acts/apify~google-search-scraper/runs?timeout={RUN_TIMEOUT_SECS}&memory=2048",
                                     data=json.dumps(body).encode(), headers=hdr)
        run = json.loads(urllib.request.urlopen(req, timeout=60).read())["data"]
        run_id, ds = run["id"], run["defaultDatasetId"]
        deadline = time.time() + RUN_TIMEOUT_SECS + 60
        status = run.get("status")
        while status in ("READY", "RUNNING", "TIMING-OUT", "ABORTING") and time.time() < deadline:
            time.sleep(15)
            r = urllib.request.Request(f"{base}/actor-runs/{run_id}", headers=hdr)
            status = json.loads(urllib.request.urlopen(r, timeout=60).read())["data"]["status"]
        if status != "SUCCEEDED":
            raise NoData(f"apify run {run_id} ended {status} after {RUN_TIMEOUT_SECS}s budget "
                         f"(https://console.apify.com/view/runs/{run_id})")
        r = urllib.request.Request(f"{base}/datasets/{ds}/items?clean=true&limit=5000", headers=hdr)
        return json.loads(urllib.request.urlopen(r, timeout=120).read())
    except urllib.error.HTTPError as e:
        # A broken instrument must SAY it is broken. Returning nothing here is what
        # let the 2026-09-28 strategist read four straight quota 403s as "only the
        # homepage is indexed" -- an inference drawn from silence. See NO_DATA below.
        detail = ""
        try:
            detail = e.read().decode()[:300]
        except Exception:
            pass
        if e.code in (401, 402, 403):
            raise NoData(
                f"apify HTTP {e.code} - almost always the monthly usage cap on the "
                f"free plan ($5/mo). Check https://console.apify.com/billing. {detail}"
            )
        raise NoData(f"apify HTTP {e.code}. {detail}")
    except NoData:
        raise
    except Exception as e:
        raise NoData(f"apify request failed: {e.__class__.__name__}: {e}")


def beats(a, b):
    """True if position a outranks b (None = not in top ~50)."""
    if a is None:
        return False
    return b is None or a[0] < b[0]


def score(snapshot):
    core = {k: v for k, v in snapshot["results"].items() if k in CORE}
    return {
        "core_keywords": len(core),
        "mjc_ranked_top50": sum(1 for v in core.values() if v["mjc"]),
        "mjc_top10": sum(1 for v in core.values() if v["mjc"] and v["mjc"][0] <= 10),
        "mjc_beats_dbm": sum(1 for v in core.values() if beats(v["mjc"], v["dbm"])),
        "mjc_beats_slamdot": sum(1 for v in core.values() if beats(v["mjc"], v["slamdot"])),
        "mjc_beats_both": sum(1 for v in core.values() if beats(v["mjc"], v["dbm"]) and beats(v["mjc"], v["slamdot"])),
    }


def fmt(p):
    return f"#{p[0]}" if p else "—"


def report(history):
    if not history:
        print("no history yet")
        return
    snap = history[-1]
    if snap.get("status") == "NO_DATA" or snap.get("score") is None:
        print("=" * 72)
        print(f"OUTRANK SCOREBOARD {snap['date']}: NO_DATA - not measured.")
        print(f"  reason: {snap.get('reason', 'unknown')}")
        print("  The newest row is an outage, not a result. Do not draw conclusions")
        print("  about rankings or indexation from it, and do not rewrite pages on")
        print("  the strength of it. For indexation truth, read Google Search")
        print("  Console (first-party) - not a scraper.")
        ok = [h for h in history if h.get("score")]
        if ok:
            last = ok[-1]
            print(f"  last real measurement: {last['date']} "
                  f"(beats_both {last['score']['mjc_beats_both']}/{last['score']['core_keywords']}), "
                  f"{(datetime.date.fromisoformat(snap['date']) - datetime.date.fromisoformat(last['date'])).days} days stale")
        print("=" * 72)
        return
    s = snap["score"]
    print(f"OUTRANK SCOREBOARD {snap['date']}  (win = MJC above BOTH rivals on >=7/{s['core_keywords']} core keywords, 2 checks in a row)")
    print(f"  MJC beats both: {s['mjc_beats_both']}/{s['core_keywords']} | beats DBM {s['mjc_beats_dbm']} | beats Slamdot {s['mjc_beats_slamdot']} | MJC in top50 {s['mjc_ranked_top50']} | top10 {s['mjc_top10']}")
    print(f"  {'keyword':42s} {'MJC':>5s} {'DBM':>5s} {'SLAM':>5s}  MJC url")
    for kw in CORE + EXTENDED:
        v = snap["results"].get(kw)
        if not v:
            continue
        tag = "" if kw in CORE else " (ext)"
        print(f"  {(kw + tag):42s} {fmt(v['mjc']):>5s} {fmt(v['dbm']):>5s} {fmt(v['slamdot']):>5s}  {urlparse(v['mjc'][1]).path if v['mjc'] else ''}")
    if len(history) > 1:
        print("  trend (beats_both / top50):", " → ".join(
            f"{h['date']}:{h['score']['mjc_beats_both']}/{h['score']['mjc_ranked_top50']}"
            if h.get("score") else f"{h['date']}:NO_DATA"
            for h in history[-8:]))


def load():
    if not os.path.exists(HISTORY):
        return []
    return [json.loads(l) for l in open(HISTORY) if l.strip()]


def main():
    args = sys.argv[1:]
    if "--report" in args:
        report(load())
        return
    date = datetime.date.today().isoformat()
    if "--date" in args:
        date = args[args.index("--date") + 1]
    if "--from-serp" in args:
        items = json.load(open(args[args.index("--from-serp") + 1]))
    else:
        try:
            items = fetch(CORE + EXTENDED)
        except NoData as e:
            # Record the outage AS DATA so downstream readers see "not measured"
            # rather than an absence they might mistake for a flat result.
            snap = {"date": date, "status": "NO_DATA", "reason": str(e),
                    "depth_pages": DEPTH_PAGES, "results": {}, "score": None}
            history = [h for h in load() if h["date"] != date] + [snap]
            history.sort(key=lambda h: h["date"])
            with open(HISTORY, "w") as f:
                for h in history:
                    f.write(json.dumps(h, separators=(",", ":")) + "\n")
            print("=" * 72)
            print("NO_DATA - the scoreboard was NOT measured this run.")
            print(f"  reason: {e}")
            print("  Do NOT infer anything about rankings or indexation from this.")
            print("  Nothing changed about the site; the measuring tool is down.")
            print("=" * 72)
            sys.exit(3)
    snap = {"date": date, "status": "OK", "depth_pages": DEPTH_PAGES, "results": parse(items)}
    snap["score"] = score(snap)
    history = [h for h in load() if h["date"] != date] + [snap]
    history.sort(key=lambda h: h["date"])
    with open(HISTORY, "w") as f:
        for h in history:
            f.write(json.dumps(h, separators=(",", ":")) + "\n")
    report(history)


if __name__ == "__main__":
    main()
