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

---

## 2026-09-21 — Google scoreboard DARK (Apify 403). AI panel 0/108, retrieval 0%. Constraint: INDEXATION/RETRIEVAL.

### Google scoreboard — NO DATA, the Action is failing
`scripts/rank_history.jsonl` still ends at **2026-09-14**, 7 days stale. I dispatched the
tracker manually this run to get a definitive cause: run
[35598221456](https://github.com/morejobcalls/morejobcalls-website/actions/runs/35598221456)
died in 6 seconds with `urllib.error.HTTPError: HTTP Error 403: Forbidden` from Apify.
Same cause as 2026-09-17, unchanged: **Apify monthly usage hard limit**, not a missing
secret. The `set -o pipefail` fix added after 09-17 worked exactly as intended — the 09-17
run reported green with no data, this one is correctly red.

Two scheduled runs (09-17, 09-21) have now produced nothing. **Spencer must raise the Apify
monthly limit or plan; nothing else in the Google half of this program can move until he
does.** Last known positions (2026-09-12/14, unchanged across all three snapshots):

| metric | value |
|---|---|
| beats both (core 12) | 0/12 |
| beats DBM / beats Slamdot | 0 / 0 |
| MJC in top 50 / top 10 | 0 / 0 |

**Movers: none measurable.** **Striking distance (#11–30): none measurable** — not "none
exist", none visible. No keyword-driven re-ordering of the backlog was possible this week,
so the queue was re-planned from the AI scoreboard instead.

### AI-answer (LLMO) scoreboard — fresh, and much better instrumented
The probe Action has been upgraded since last run. Monday now runs `llmo_panel.py`: 18
questions x 2 phrasings x 3 runs = **108 grounded answers**, reported as a mention *rate*
with a confidence interval rather than a single X/18 (AI brand lists are non-deterministic;
one run is noise).

| metric (2026-09-21 panel, Claude/Brave, 108 answers) | value |
|---|---|
| MJC mention rate | **0.0%** (95% CI 0.0–3.4%) |
| hire-intent mention rate | 0.0% |
| **retrieval rate** | **0.0%** |
| cited rate | 0.0% |
| most-cited domains | deckbuildermarketers 23.1%, clicksgeek 19.4%, constructionleadpro 19.4%, deckfencemarketers 18.5%, hardscapemarketingcrew 15.7% |
| most-named brands | Angi 46.3%, HomeAdvisor 38.9%, Thumbtack 35.2%, Deck Builder Marketers 20.4% |

Legacy 18-question grounded probe (2026-09-18, Thursday cadence, kept for trend continuity):
named **0/18**, hire-intent **0/13**, MJC URLs cited **0** — flat on the 09-18 baseline.
Change is not real at 2+ runs either way; both scoreboards are still at zero.

The number that matters is **retrieval 0.0%**. Across every web search those 108 answers
triggered, morejobcalls.com never came back as a result even once. That is not a ranking
problem or a persuasion problem — the engine never saw the pages.

### Binding constraint: INDEXATION / RETRIEVAL (unchanged from 2026-09-14, now confirmed twice over)
Last week's read was Google-only and could have been an Apify artifact. It is not. The
grounding index behind the panel is Brave/Bing, a completely separate crawl from Google's,
and it returns MJC on nothing. Two independent indexes agree.

Re-checked this run, all still clean: `/`, `/trades/deck-builder-marketing/`,
`/learn/deck-builder-marketing-companies-compared/`, `/sitemap.xml` and `/robots.txt` all
200 to a browser UA; robots allows everything including named AI crawlers; the sitemap is
now **43 URLs** (up from 36 — the builder's new pages are all in it). A literal
`"morejobcalls.com"` phrase search still returns competitors and not the domain.

So nothing on the site is wrong, and nothing on the site is the fix. The levers are all
submission and discovery: GSC sitemap + request-indexing, **Bing Webmaster Tools + IndexNow
(new this week — the panel proves Bing/Brave matters as much as Google for the AI half)**,
and real inbound links. The 30 undeployed footer credits are the largest uncashed discovery
asset in the program: 30 contractor domains already owned, worth more right now as crawl
paths than as link equity.

### Rival watch: quiet
Zero new and zero removed URLs vs the 2026-09-14 baseline — 280 DBM (post/page/learn/
case-study) and 9 Slamdot deck|decking|contractor URLs, byte-identical lists. DBM and
Slamdot published nothing in 7 days. `rival_urls.json` refreshed with the 09-21 diff note.

Live top 10 on the two headline keywords (MJC absent from both):
- **hardscapemarketingcrew.com/best-deck-builder-marketing-agencies/** is back in the top 10
  on `deck builder marketing` and takes 15.7% of all AI citations — while still serving a
  **404 "Article not found" body**. It is ranking and being cited on a stale title alone.
  Kept `dead` in the pipeline (nothing to pitch), flagged to recheck monthly.
- **growthdeckmarketing.com** holds its top-10 slot a second week running. Closest
  positioning to MJC of any rival ("qualified booked estimates for deck builders", paid ads
  + CRM + in-house qualification). It belongs in the tracked rival set — but `rank_tracker.py`
  is off-limits to this routine, so this is a request for Spencer/the builder.
- **deckfencemarketers.com** is new in the top 10 on `marketing for deck builders` *and*
  takes 18.5% of AI citations — the 4th-most-cited domain overall, ahead of Slamdot. Also
  worth tracking.
- townsquareinteractive.com and contractorsassociation.org still appear. The latter was
  checked and rejected as an authority target (InterNACHI eBook page, no vendor directory).

### Footer credits: 7 of 37 live (flat)
All seven re-verified live 2026-09-21 with correct target and `rel=nofollow`: apdecks.com,
bivianomodularbuilders.com, oasiscustomdecks.com, paynterconstruction.com,
thewindowprofessor.pro, bivianocontracting.com, mrpatiocover.com. **No regressions, no
missing credits.** (Registry holds 37 sites, not the ~35 in the routine prompt.)

All 30 GHL funnels remain `pending-va` — unchanged for a second week, and now the single
highest-value unblocked item given the retrieval constraint.

### AI-cited pages added to the authority pipeline (4)
Classified all 85 URLs in `llmo_citations.json`. Four new rows, all WebFetch-verified live:
- Silverback Strategies — "Best Digital Marketing Agencies for Roofing" (10 agencies,
  **states it updates quarterly** — the clearest standing re-pitch window in the file)
- Marketing LTB — "10 Best Roofing Digital Marketing Agencies in 2026" (publisher is not on
  its own list, so inclusion is not a competitive ask)
- Owl Roofing — "10 Best Roofing Marketing Companies (2026)" (written by a roofing
  *contractor* about vendors he actually uses — the most credible format an engine can cite)
- Capterra Services agency profile (DBM's profile was AI-cited but now 404s; low effort if a
  free provider profile can still be created)

Four were verified and **rejected** so nobody re-pitches them — Housecall Pro, Abstrakt,
InsideAdvisorPro and BuildFolio are all lists of lead *marketplaces*, not agencies. That
finding drove the week's top backlog item: the broadest hire-intent AI answers are built
from marketplace comparisons MJC can never be added to, so the only way into that cluster is
to rank our own page for it.

### Backlog changes
- Replaced the stale 09-14 strategist read with the 09-21 one (scoreboard dark + retrieval 0%).
- **New page rule:** never publish a self-ranked "best agencies" list with MJC at #1.
  Alphabetical, externally-sourced comparison pages are fine; rankings we top are not.
- Three new Phase 0 items, in order: `/learn/lead-generation-companies-for-contractors/`
  (most-cited cluster, written as a category guide not a ranking), then the
  `/trades/fence-company-marketing/` refresh (vertical #2, weakest rival field we track),
  then the `/trades/patio-cover-marketing/` refresh (open field — first page that will show
  us the day retrieval clears).
- Split the old combined patio+fence Phase 2 item, which targeted two keywords in one item
  against the page rules, and promoted both halves to Phase 0.
- Added a Phase 2 `/trades/roofing-leads/` refresh for **roofing marketing company**:
  vertical #3 is the one cluster where both an inclusion pitch and our own page have a path.
- 13 unchecked items queued in Phase 0/1/2. Phase 3 untouched.

---

## 2026-09-28 — Weekly strategist

### Google scoreboard: DARK for a third week (Apify hard limit, 4 consecutive failures)
`rank_history.jsonl` newest row is still **2026-09-14** — 14 days stale. The `rank-tracker.yml`
Action has failed on **every run since 09-17**: runs 7, 8 and 9 (09-21 dispatch, 09-21 schedule,
09-24 schedule) all ended `urllib.error.HTTPError: HTTP Error 403: Forbidden` from the Apify actor
call in `rank_tracker.py:105`. This is the **monthly usage hard limit**, not a missing secret —
the same cause diagnosed 2026-09-17, now unresolved for 11 days. **Spencer must raise the Apify
monthly limit or plan; nothing else restores position data.**

Last known scoreboard (2026-09-14, unchanged): beats both **0/12** · beats DBM 0 · beats Slamdot 0 ·
MJC top-50 **0** · top-10 **0**. Trend 09-10: 0/0 → 09-12: 0/0 → 09-14: 0/0. No movers can be
reported and **no striking-distance (#11-30) items can be promoted** — not because none exist, but
because nobody can see them.

### AI-answer (LLMO) scoreboard: 0/18, flat, and now precisely explained
Grounded probe `llmo_grounded_history.jsonl` latest **2026-09-24** (4 days old, Action healthy —
all 4 llmo-probe runs succeeded): **named 0/18**, hire-intent **0/13**, **MJC URLs cited 0**.
Identical to 09-18 and 09-21. Change vs ~7 days earlier: **none**, and flat across 3+ runs, so this
is real and not answer noise. The 108-answer panel (`llmo_panel_history.jsonl`, 09-21) agrees:
mention rate 0.0%, hire mention rate 0.0%, **retrieval rate 0.0%**, cited rate 0.0%.
Most-cited domains: deckbuildermarketers.com 23.1%, deckfencemarketers.com 19.4%,
contractorgorilla.com 17.6%, clicksgeek.com 17.6%, sociusmarketing.com 15.7%,
hardscapemarketingcrew.com 14.8%.

### BINDING CONSTRAINT: indexation — and this week it got a sharper diagnosis
Still indexation, third consecutive week, but the previous read ("nothing is retrievable") was
imprecise. This run's tests:
- A **domain-restricted** search returns `https://morejobcalls.com/` with a correct title and an
  accurate content summary → **the homepage IS in the index.**
- Three queries that exactly match deep pages — `patio cover marketing contractors`,
  `angi alternatives for deck builders exclusive appointments`, and the brand query — **all returned
  the homepage and nothing else**, although `/trades/patio-cover-marketing/` and
  `/learn/angi-alternatives-for-deck-builders/` both serve 200.
- An **unrestricted** `morejobcalls.com` search returns Bizapedia, The Manifest and a YouTube channel
  — third-party pages about MJC outrank MJC on its own brand name.
- Serving is fine: homepage, sitemap, robots and a deep trade page all 200; robots explicitly allows
  GPTBot/OAI-SearchBot. Crawl paths are fine: the homepage links all 10 trade pages, the /learn/ hub
  and 3 articles.

**Conclusion: only the homepage is indexed. Not one of the ~20 shipped /learn/ and /trades/ pages is.**
That single fact accounts for 0/18 by itself — the engine can only ever find the generic contractor
homepage, never the page written for the question. This is **crawl budget and trust on a DR-0 domain
with no real inbound links**, not architecture and not on-page. The lever is unchanged and still
unpulled: GSC sitemap + request indexing, Bing Webmaster + IndexNow, and real inbound links. The
**30 pending footer credits are now the highest-leverage unblocked item on the board** — 30 already-
indexed contractor domains linking *directly at deep /trades/ pages*, which is exactly the crawl
signal the deep pages lack.

### Rival watch: one new DBM URL, and it is not a content threat
DBM **281** URLs (was 280), zero removed. Slamdot unchanged at **9**. The one new page is
`/your-journey-with-deck-builder-marketers/` — a 3-step sales/onboarding funnel (H1 "Your Journey
with Deck Builder Marketers", exit-intent popup, strategy-call CTA), **not editorial and not a topic
gap**, so no backlog item was added. DBM has now published **no new editorial content in 14 days**.

Live top 10, both headline keywords (MJC absent from both):
- **footbridgemedia.com/who-we-help/deck-builder-marketing-seo** is **new in the top 10 on BOTH**
  `deck builder marketing` and `marketing for deck builders` — the only new domain this week.
- `linkedin.com/company/deckbuildermarketers` is the **#1 result for "deck builder marketing"**,
  above DBM's own homepage — and it is AI-cited. MJC has no LinkedIn company page.
- growthdeckmarketing.com, deckfencemarketers.com, hardscapemarketingcrew.com (still serving a 404
  body while holding a top-10 slot and 14.8% of AI citations), townsquareinteractive.com and
  contractorsassociation.org all persist. The tracked-rival-set request for growthdeckmarketing and
  deckfencemarketers stands — `rank_tracker.py` is off-limits to this routine.

### Footer credits: 7 of 37 live (flat, no regressions)
All seven re-verified live 2026-09-28 with correct target and anchor text: apdecks.com,
bivianomodularbuilders.com, oasiscustomdecks.com, paynterconstruction.com, thewindowprofessor.pro,
www.bivianocontracting.com, www.mrpatiocover.com. **No missing credits.** All 30 GHL funnels remain
`pending-va` — unchanged for a **third** week. Two of the 30 (alldeckedoutbuilds.com,
deckoutyourhomebuilds.com) returned an empty body to curl and may not be serving at all; worth a
check before the VA works the list.

### AI-cited pages: 94 URLs classified, zero new pitchable listicles
Up from 85. Six roundup/comparison candidates not already in the pipeline were WebFetch-verified live
and **all six rejected** — every one is publisher-authored content that ranks the publisher itself and
lists marketplaces rather than agencies: zioadvertising, pipelineon, regie.ai, homeshowoff, webfx
(fence guide) and contractingempire. Details in `authority_pipeline.md`.

**Cumulative finding worth acting on: across 09-21, 09-24 and 09-28, all 14 AI-cited roundups checked
have been marketplace rosters or vendor self-rankings.** "Pitch the top AI-cited listicle" is a
largely exhausted lane in this niche. The third-party surfaces AI answers *do* cite and that MJC can
actually occupy are **profile directories**: DesignRush (DBM's profile was cited 2x this run — tagged
AI-cited in the pipeline), Clutch, The Manifest (live), Semrush, GoodFirms — plus **LinkedIn**, added
as a new pipeline row this week on the strength of DBM's LinkedIn page holding Google #1.

### Backlog changes
- Replaced the 09-21 strategist read with the 09-28 one (scoreboard dark 4th run + homepage-only indexation).
- Two new Phase 0 items, now the top two unchecked items on the board:
  `/learn/google-ads-for-deck-builders/` (kw **google ads for deck builders**; five thin cited agency
  pages, two of them anytimedigitalmarketing's) and `/trades/hardscape-marketing/` (kw **hardscape
  contractor marketing**; new trade page, open field, and hardscapemarketingcrew's 14.8% citation share
  proves engines are hunting for a hardscape answer).
- **Un-checkboxed `/learn/angi-vs-homeadvisor-vs-thumbtack-for-deck-builders/` as SUPERSEDED.** The
  shipped Phase 0 `/learn/angi-alternatives-for-deck-builders/` already owns that cluster; the Phase 0
  item said it superseded this one but left the checkbox open, which would have produced a duplicate-
  keyword page against the one-keyword-per-page rule.
- 10 unchecked items queued in Phase 0/1/2. Phase 3 untouched. Page rules header intact.
