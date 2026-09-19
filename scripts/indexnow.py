#!/usr/bin/env python3
"""
IndexNow submitter — tells Bing (and every IndexNow participant) about new or
changed morejobcalls.com URLs the moment they are pushed.

Why this exists: ChatGPT search and Microsoft Copilot retrieve from Bing's index.
A page Bing has not crawled cannot be cited in a ChatGPT answer, however well it
does on Google. IndexNow is the fastest legitimate way to get Bing to fetch a URL.
(Google does not support IndexNow; Google indexing is Search Console, sitemap +
"Request indexing", which is a Spencer task.)

The key file already lives at the site root (<key>.txt, 32 hex chars, contents =
the key). This script finds it, reads the sitemap, and POSTs the URL list.

    python3 scripts/indexnow.py             # submit every sitemap URL
    python3 scripts/indexnow.py --changed   # only URLs whose files changed in the
                                            # last commit (falls back to all when
                                            # nothing page-shaped changed)
    python3 scripts/indexnow.py --dry       # print what would be sent, send nothing

Exit code is non-zero on an HTTP error so the Action fails loudly.
"""
import argparse
import json
import pathlib
import re
import subprocess
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
HOST = "morejobcalls.com"
ENDPOINT = "https://api.indexnow.org/IndexNow"


def find_key():
    for p in ROOT.glob("*.txt"):
        if re.fullmatch(r"[0-9a-f]{32}\.txt", p.name):
            key = p.read_text().strip()
            if key == p.stem:
                return key
            sys.exit(f"key file {p.name} does not contain its own name")
    sys.exit("no IndexNow key file (<32-hex>.txt) at the site root")


def sitemap_urls():
    xml = (ROOT / "sitemap.xml").read_text()
    return re.findall(r"<loc>\s*(https://[^<\s]+)\s*</loc>", xml)


def changed_urls(all_urls):
    """Map files changed in the last commit to sitemap URLs."""
    try:
        out = subprocess.check_output(
            ["git", "diff", "--name-only", "HEAD~1", "HEAD"], cwd=ROOT, text=True)
    except subprocess.CalledProcessError:
        return []
    files = [f for f in out.split() if f.endswith(".html")]
    hit = set()
    for f in files:
        path = "/" + f[:-len("index.html")] if f.endswith("index.html") else "/" + f
        if path == "/index.html":
            path = "/"
        url = f"https://{HOST}{path}"
        if url in all_urls:
            hit.add(url)
    # keep sitemap order
    return [u for u in all_urls if u in hit]


def submit(urls, key, dry=False):
    body = {"host": HOST, "key": key,
            "keyLocation": f"https://{HOST}/{key}.txt",
            "urlList": urls}
    print(f"IndexNow: {len(urls)} URL(s) -> {ENDPOINT}")
    for u in urls:
        print("  " + u)
    if dry:
        print("(dry run, nothing sent)")
        return
    req = urllib.request.Request(
        ENDPOINT, data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            print(f"response: HTTP {r.status}")
    except urllib.error.HTTPError as e:
        # 200 OK, 202 Accepted (key validation pending). Anything else is a real error.
        sys.exit(f"IndexNow rejected the submission: HTTP {e.code} {e.read().decode()[:300]}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--changed", action="store_true")
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()
    key = find_key()
    urls = sitemap_urls()
    if a.changed:
        sub = changed_urls(urls)
        if sub:
            urls = sub
        else:
            print("no page-shaped changes in the last commit; submitting the full sitemap")
    submit(urls, key, dry=a.dry)
