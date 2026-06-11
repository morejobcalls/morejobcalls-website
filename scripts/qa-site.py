#!/usr/bin/env python3
"""QA check for morejobcalls.com pages: banned offer language, JSON-LD validity, internal links.
Used by /seo-publish and any manual site edit. Run from anywhere."""
import json, re, os, glob, sys

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

files = sorted(set(
    glob.glob("trades/*/index.html") + ["trades/index.html"]
    + glob.glob("learn/*/index.html") + ["learn/index.html", "about/index.html", "index.html", "wins.html"]
))
BANNED = ["work for free", "free until", "working for free"]
errs = []
for f in files:
    html = open(f).read()
    for bad in BANNED:
        if bad.lower() in html.lower():
            errs.append(f"{f}: banned phrase '{bad}' (retired guarantee prong)")
    for i, m in enumerate(re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)):
        try:
            json.loads(m)
        except Exception as e:
            errs.append(f"{f}: JSON-LD block {i+1} invalid: {e}")
    for link in re.findall(r'href="(/[^"#?]*)"', html):
        p = link.lstrip("/")
        if p.endswith("/"):
            p += "index.html"
        if p and not os.path.exists(p):
            errs.append(f"{f}: broken internal link {link}")

print(f"checked {len(files)} files")
if errs:
    print("\n".join(sorted(set(errs))))
    sys.exit(1)
print("ALL CLEAN")
