# Indexability + exact-phrase sweep — the nine absent core keywords

**Run 2026-10-26 by the daily builder, as the ordering override named in the
2026-10-26 strategist read (`scripts/outrank_backlog.md`, Phase 1 item 1).**
Scope: the nine CORE keywords with **no MJC URL in the top 50** on the 2026-10-22
board. Read-only by design. Fix authority: hard defects only (noindex, 404, a
canonical pointing elsewhere, a missing sitemap entry). Nothing else was touched.

Nominated owner URLs are taken from `scripts/core_keyword_ownership_audit.md`,
with keyword 6 (`deck builder advertising`) updated from **none** to the page
shipped 2026-10-19, and keyword 10 (`leads for deck builders`) kept on the
lead-generation page per note B of that audit.
The two frozen agency-intent pages were **not** in scope and were **not** edited;
keyword 5's owner is read here only because the sweep is read-only.

## VERDICT IN ONE LINE

**All nine are clean. Not one hard defect: nine of nine return HTTP 200, carry no
`noindex` in meta or in any response header, self-canonicalise, sit in
`sitemap.xml` with a `lastmod` inside the last 18 days, and appear in `llms.txt`.
The indexation question is closed. The constraint is authority.**

## The table

| # | core keyword | nominated owner | HTTP | robots meta / `X-Robots-Tag` | canonical | in sitemap (lastmod) | kw in `<title>` | in H1 | in first 100w | H2s with kw | contextual inbound body links | in `llms.txt` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | marketing for deck builders | `/trades/deck-builder-marketing/` | 200 | none / none | self ✓ | 2026-10-13 ✓ | no | no | **yes** | 1 ✓ | 51 | yes |
| 4 | deck contractor marketing | `/trades/deck-builder-marketing/` | 200 | none / none | self ✓ | 2026-10-13 ✓ | no | no | no | 1 ✓ | 51 | yes |
| 5 | best marketing agency for deck builders | `/learn/best-marketing-agency-for-deck-builders/` | 200 | none / none | self ✓ | 2026-10-15 ✓ | yes | yes | yes | 1 ✓ | 10 | yes |
| 6 | deck builder advertising | `/learn/deck-builder-advertising/` | 200 | none / none | self ✓ | 2026-10-19 ✓ | yes | yes | yes | 1 ✓ | 4 | yes |
| 7 | deck builder seo | `/learn/deck-builder-seo/` | 200 | none / none | self ✓ | 2026-10-15 ✓ | yes | yes | yes | **5** | 8 | yes |
| 8 | deck builder leads | `/learn/deck-builder-leads/` | 200 | none / none | self ✓ | 2026-10-21 ✓ | yes | yes | yes | 2 | 9 | yes |
| 9 | deck builder lead generation | `/learn/deck-builder-lead-generation/` | 200 | none / none | self ✓ | 2026-10-20 ✓ | yes | yes | yes | 2 | 20 | yes |
| 10 | leads for deck builders | `/learn/deck-builder-lead-generation/` | 200 | none / none | self ✓ | 2026-10-20 ✓ | no | no | no | 0 | 20 | yes |
| 11 | facebook ads for deck builders | `/learn/facebook-ads-for-deck-builders/` | 200 | none / none | self ✓ | 2026-10-08 ✓ | yes | yes | yes | 2 | 12 | yes |

Columns 1–4 and 7 (status, robots, canonical, sitemap, `llms.txt`) are the
indexability half. **Every cell in that half passes on every row.** Columns 5 and 6
(exact phrase placement, inbound links) are the relevance half and are recorded
for the strategist; they are not defects and nothing in them was fixed.

Method: live `curl -sS -D - -L` per unique URL for status, final URL and response
headers; the committed HTML for robots meta, canonical, title, H1, first 100 words
of body prose with the H1 removed, and H2s; `sitemap.xml` and `llms.txt` parsed
directly. "Contextual inbound body links" counts `<a href="…">` to the owner from
every other page in `trades/`, `learn/` and the root service pages **after**
stripping `<nav class="site-nav">`, `<footer class="site-footer">`, the
`related-grid` block and every `related-card` — so nav chrome and card decks are
excluded and only in-prose links are counted.

## What else was checked, because a clean page can still be blocked upstream

- **`robots.txt`** — `User-agent: * / Allow: /`. The only `Disallow` lines are
  `/index-v1-backup.html`, `/index-v2.html`, `/brand-guidelines.html`,
  `/temporary screenshots/`, `/node_modules/`, `/scripts/` and `/.github/`. **No
  owner URL is inside a disallowed path.** All eleven named AI crawlers are
  explicitly allowed.
- **Response headers** — GitHub Pages returns `server: GitHub.com` with HTTP 200
  and **no `X-Robots-Tag` on any of the seven unique URLs.** Nothing is being
  suppressed at the edge.
- **`sitemap.xml`** — HTTP 200 live, and declared in `robots.txt`.
- **Redirects** — every `-L` final URL equals the requested URL. No owner is
  redirecting, and nothing in this set is a stub.

## Why this closes the indexation question

The 2026-10-12 audit caught a real defect of exactly the class this sweep was
built to find: `/learn/how-to-get-more-deck-jobs/` had been a 597-byte `noindex`
meta-refresh stub since 09-28 while the 10-06 scoreboard recorded the stub itself
as the ranking URL. That was the case for running this. **It does not reproduce
anywhere in the current set.** The GSC reading behind "indexation is not it"
(36 indexed) was from 09-28 and four weeks stale; this sweep replaces it with a
first-party check of the nine URLs that actually matter, taken today.

So the remaining explanation for a page that exists, returns 200, is indexable,
self-canonicalises, carries the exact phrase in its title and H1, is linked in
prose from eight to twenty sibling pages, and **still cannot place in a top 50
where no rival ranks either** is trust, not crawlability. `facebook ads for deck
builders` is the sharpest instance: an empty top 50 for all three domains, and
MJC has a dedicated page with the phrase at the front of the title, in the H1, in
the first 100 words, in two H2s, and twelve contextual inbound links. There is no
on-page lever left to pull on that URL. The same reading holds for the two
extended open fields (`outdoor living contractor marketing`,
`fence company marketing`).

This is the fourth independent line pointing at authority, and the first one that
rules out the cheap alternative by measurement rather than by inference.

## Two relevance gaps recorded, deliberately NOT fixed

Both are title/H1 relevance questions, not hard defects, so the ordering override
forbids touching them. Raising them for the strategist instead:

1. **Keyword 10, `leads for deck builders`, has zero exact-phrase presence on its
   nominated owner** — not in the title, not in the H1, not in the first 100
   words, not in any of that page's fifteen H2s. Note B of the ownership audit
   recorded the same 0 and left it alone on purpose, because the page was then
   ranking #8 and beating both rivals on the keyword. **That position is gone on
   the 10-22 board.** The reason for the do-not-touch order has therefore expired,
   and the audit's own instruction was "if the next run wants the phrase on the
   page, confirm the do-not-touch order has expired first." It has. This is a
   strategist call: either put the phrase on the lead-generation page, or
   re-nominate the keyword back to `/learn/deck-builder-leads/`, which already
   carries it. **Not the builder's call and not done here.**
2. **Keywords 2 and 4 both sit on the pillar, and neither phrase is in its title
   or H1** (`marketing for deck builders` does make the first 100 words;
   `deck contractor marketing` does not). This is the same title-relevance
   question Note A of the ownership audit flagged for keyword 1 and routed to the
   strategist. Three core keywords now hang on one pillar title. Still the
   strategist's decision, still not an anchor problem.

Nothing in this file argues for a page edit. Column 5 is evidence for the next
strategist read, not a work queue.

## Reproducing it

The sweep script is not committed (it is a one-shot diagnostic, and
`scripts/rank_tracker.py` and the audit files are the durable artefacts). The
method section above is complete enough to rebuild it in about forty lines: nine
`(keyword, owner URL)` pairs, one `curl` per unique URL, and the committed HTML
for everything else.
