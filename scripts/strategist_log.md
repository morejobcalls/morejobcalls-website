# MJC Outrank — weekly strategist log

Maintained by the "MJC Outrank — Weekly Strategist" routine. One dated entry per run:
scoreboard numbers, movers, rival changes, backlog changes, and the binding constraint.
The strategist edits only `scripts/`. Site pages belong to the daily Builder routine.

---

## 2026-09-14 — first strategist run. Baseline established. Constraint: INDEXATION.

### Scoreboard (snapshot 2026-09-12, 2 days old — the Action is healthy)
| metric | value | vs 2026-09-10 |
|---|---|---|
| beats both (core 12) | 0/12 | 0/12 — flat |
| beats DBM | 0 | flat |
| beats Slamdot | 0 | flat |
| MJC in top 50 | 0 | flat |
| MJC in top 10 | 0 | flat |

Only two snapshots exist (09-10, 09-12), so there is no 7-day-earlier comparison yet.
The 7-day window opens on the 2026-09-17 run.

**Movers: none, up or down.** MJC does not appear in the top 50 on any of the 20 tracked
keywords, in either snapshot. Scrape depth was 40–50 results per keyword, so the crawl is
working; there is simply nothing of ours in it.

**Striking distance (#11–30): none.** Nothing to promote to the top of the backlog this
week, because nothing is ranking at all.

Rival positions are unchanged across both snapshots. DBM holds #1 on `deck builder
marketing`, `marketing for deck builders`, `deck builder marketing agency` and `best
marketing agency for deck builders`. Slamdot holds #1 on `deck builder seo`.

### Binding constraint: INDEXATION
Not on-page, and not (yet) authority. The evidence:

1. **Two tracked keywords are open field** — `outdoor living contractor marketing` and
   `patio cover marketing` have no rival in the top 50 either. MJC has a page targeting
   each. An indexed page on an uncontested commercial phrase lands *somewhere* in a top
   50. Ours lands nowhere.
2. **A branded search does not surface the domain.** Searching the brand plus the literal
   string `morejobcalls.com` returns the Manifest profile for MoreJobCalls.com LLC and a
   pile of competitors — but not morejobcalls.com itself. A site Google has indexed always
   wins its own brand.
3. **Nothing technical is blocking it.** Checked this run: homepage, pillar, newest learn
   page, sitemap and robots all return 200 to a browser UA; canonicals are self-referential
   and correct; `robots.txt` allows everything (AI crawlers explicitly); the only `noindex`
   on the site is `/start/`, which is the funnel page and is meant to be excluded. The
   36-URL sitemap covers every content page on disk — the four that are missing
   (brand-guidelines, /start/, /privacy/, /terms/) are all deliberate.
4. **There is no discovery path.** Per `authority_pipeline.md`, MJC's ~449 "referring
   domains" are a third-party spam redirect network, not real links. Only 4 of 35 footer
   credits are live, and those are correctly `rel=nofollow`. So Google has almost no
   legitimate route to crawl the site, and no reason to prioritize it.

That combination is a crawl/discovery problem, and the lever is Google Search Console:
submit the sitemap, then request indexing on the pillar and the newest pages. Until MJC
appears in *a* top 50, "no movement" is not evidence that the pages are wrong — so do not
let it trigger an on-page rewrite of work that has never been seen.

Authority is the constraint *after* this one, and the footer-credit program plus the
directory listings are the right answer to it. But links cannot lift a page Google has not
indexed, so sequencing matters: indexation first, then authority.

### Rival watch
First run, so `scripts/rival_urls.json` is a **baseline, not a diff**: 280 DBM URLs
(post + page + learn + case-study sitemaps) and 9 Slamdot URLs matching deck|decking|
contractor. Next week's run reports genuine new pages against this.

Two rival-gap topics found on Slamdot with no MJC equivalent — both added to Phase 2:
- `/blog/5-lead-magnet-ideas-for-deck-builders-that-attract-real-clients/`
- `/blog/3-proven-ways-to-boost-referrals-for-your-decking-business/`

Slamdot's `/blog/the-local-seo-blueprint-for-deck-builders-...` is deliberately **not**
queued: `/learn/deck-builder-seo/` already owns that keyword space and a second page would
cannibalize it.

New domains in the live top 10 that the tracker does not follow:
- **growthdeckmarketing.com** — closest positioning to MJC yet ("predictable, qualified
  booked estimates for deck builders", paid ads + CRM + in-house qualification). Worth
  adding to the tracker if it holds a top-10 spot next week.
- **hardscapemarketingcrew.com** — "5 Best Deck Builder Marketing Agencies in 2026",
  ranking on core terms. Already in `authority_pipeline.md` as a listicle-inclusion pitch;
  this run confirms it is live in the SERP and worth Spencer's time.
- townsquareinteractive.com and contractorsassociation.org also appear on
  `marketing for deck builders`.

### Footer credits: 4 of 35 live (up 1)
All three previously-live credits re-verified, no regressions:
bivianocontracting.com, oasiscustomdecks.com, mrpatiocover.com.

**bivianomodularbuilders.com flipped candidate → live** (verified, correct target and rel).
`thewindowprofessor.pro` remains a candidate, no anchor found.

All 30 GHL funnels remain `pending-va` — none has the credit yet. That is the single
largest uncashed item in the program: 30 contractor domains, already owned, already
carrying the client relationship, worth more as crawl paths right now than as link equity.

### Backlog changes
- Added the indexation read as a standing note at the top of the queue, so the Builder
  does not misread flat rankings as bad pages.
- Re-ordered Phase 1 by field weakness now that the scoreboard has real rival positions
  (the previous annotations were stale): `facebook-ads-for-deck-builders` stays first and
  is now clearly the best bet — DBM sits at only #37 and Slamdot is absent, and it is the
  one topic where MJC has more real evidence than anything in the SERP.
  `how-to-get-more-deck-jobs` (DBM #22) moves ahead of `deck-builder-lead-generation`
  (DBM #8). `deck-builder-seo` moves to the end of Phase 1: Slamdot #1 and DBM #2 make it
  the hardest field we track, and we do not sell SEO.
- Refreshed every rival position annotation to the 2026-09-12 numbers.
- Added two Phase 2 rival-gap items (lead magnets, referrals).
- 15 unchecked Phase 1/2 items queued. Phase 3 untouched.
