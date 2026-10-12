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

---

## 2026-10-05 — Google still DARK (21 days). **First MJC page ever cited by an AI answer.** Constraint: ON-PAGE / BRAND-NAMING LIFTABILITY.

### 1. Google scoreboard — NOT MEASURED. The Action is failing, and it will not fix itself.

`scripts/rank_history.jsonl` newest row is the `NO_DATA` outage of 2026-09-28; the last **real**
measurement is **2026-09-14, 21 days ago**.

| metric | value | vs ~7 days earlier |
|---|---|---|
| beats both (core 12) | **not measured** | n/a — no data since 09-14 (0/12) |
| beats DBM | not measured | n/a |
| beats Slamdot | not measured | n/a |
| MJC in top 50 | not measured | n/a |
| MJC in top 10 | not measured | n/a |
| keywords at #11–30 | **unknown — nobody can see them** | n/a |

Cause, read from the Action logs this run (run 11, job 110492329570): Apify
`HTTP 403 {"type":"platform-feature-disabled","message":"Monthly usage hard limit exceeded"}`.
**Six consecutive failed runs** (09-17, 09-21 ×2, 09-24, 09-28, 10-01). `APIFY_TOKEN` is present
and valid in the environment — this is not a missing secret.

**New and decisive this week: the 2026-10-01 run failed too, i.e. after the month boundary.** A
spend cap that resets monthly would have cleared on 10-01. It did not. So this is an **account-level
hard limit** that only Spencer can lift at https://console.apify.com/billing. Nothing in the repo
can route around it. No movers, no striking-distance promotions, and no ranking inference of any
kind is available until he does.

### 2. AI-answer (LLMO) scoreboard — the number that matters moved off zero

Source `scripts/llmo_grounded_history.jsonl`, run 2026-10-01 (newest; 4 days old, Action healthy —
runs land ~17:00–18:45 UTC, not the nominal 11:40, so today's Monday run had not fired at pass time).

| metric | 2026-10-01 | 2026-09-24 | 2026-09-18 |
|---|---|---|---|
| MJC **named** | 0/18 | 0/18 | 0/18 |
| named, hire-intent | 0/13 | 0/13 | 0/13 |
| **MJC URL cited** | **1** | 0 | 0 |

**The first MJC citation in four grounded runs (~140 citations).**
`https://morejobcalls.com/learn/best-marketing-agency-for-deck-builders/` was both *searched* and
*cited* for the hire-intent question **"Facebook ads agency for deck builders that guarantees
appointments"** — alongside serviceallies ×2, clicksgeek, footbridgemedia and deckbuildermarketers.com.
It still scored `named: false`.

Single-run, so by the 2+ run rule it is **not yet a trend**. But it is a first-ever event, not noise
in a moving average, and it isolates the failure precisely: **retrieval succeeded and naming failed.**

**Why.** The first 50 words of that page are *"Disclosure up front: I run one of these agencies. My
company builds Meta ad systems for home service contractors, deck builders first."* The brand is never
the grammatical subject — "I" and "my company" are. The 2026-09-20 site-wide entity pass did add a
"MoreJobCalls.com is …" sentence to the /learn/ pages, but on this page it sits *behind* the
first-person opening, and the opening is the passage an engine lifts. A page that cannot be quoted as
a sentence whose subject is MoreJobCalls.com cannot put the brand in an answer, however well it ranks.

**Also measured:** 3 of the 18 questions returned **zero citations and zero searches** — the model
answered from parametric knowledge with no retrieval at all ("I own a deck building company doing
about $2M a year. Who should I hire…", "Best way to get exclusive appointments for a home improvement
contractor", "How do I get more deck building leads?"). Those three are unreachable by ranking or by
inclusion; only broad brand prevalence touches them. **The addressable denominator is 15, not 18** —
worth saying out loud before anyone treats 18/18 as the target.

Most-cited domains this run: clicksgeek.com (10), footbridgemedia.com (6), comradeweb.com (5),
webfx.com (5), serviceallies.com (5). Rival-brand mentions are still dominated by the marketplaces
(Angi 9, HomeAdvisor 9, Thumbtack 9) — DBM's own domain slipped to 3 citations from 6 a week earlier.

### 1b. AI-cited classification (94 URLs)

Full classification is written up in `scripts/authority_pipeline.md` (2026-10-05 pass). Summary:
**2 rows added**, 6 (b) candidates verified live and rejected, the rest (a) competitor service pages
or (c) marketplaces/software/PR.

- **Fervor Studio — "Best Contractor Marketing Agencies 2026"** — ranks 10 real named agencies, not
  marketplaces. Only the second genuine agency-inclusion precedent found in 22 cited roundups. The
  same site publishes a deck-builder variant; that is the one to ask for.
- **Deckorators pro editorial blog** — the **first manufacturer/supplier page ever to appear in this
  citation data**, cited for "How do deck builders get more qualified leads in 2026?". New category
  for this pipeline, and MJC's ad-spend numbers are the one thing a decking manufacturer cannot source
  elsewhere. No guest-post route; the realistic ask is an expert-source or data quote.

Rejected (so nobody re-pitches them): beseencontractors (own guide, cites nothing external),
comradeweb/home-services-lead-generation (10 entries, all marketplaces), servicebuddy (2023, flooring,
channels only), leadtruffle (alternatives are *channels*, not providers), and two myquoteiq posts (deck
estimating software, wrong category). **20 of 22 AI-cited roundups checked to date are marketplace
rosters or vendors ranking themselves** — fourth consecutive pass with that result. Profile directories
and our own pages remain the LLMO lane.

### 2. Rival watch — quiet for a third straight week

- **DBM:** 282 URLs, up 1. The single new URL is `/your-journey-with-deck-builder-marketers-v2/` — a
  *second version* of the sales-funnel page added last week (v1 still live). Conversion page, not
  editorial, no topic gap, **no backlog item.** DBM has published **no new editorial content in 21
  days** — three consecutive diffs of nothing but funnel iterations.
- **Slamdot:** 9 deck/decking/contractor URLs, unchanged.
- **SERP top 10** ("deck builder marketing", "marketing for deck builders"): the familiar field
  (footbridgemedia, clicksgeek, sociusmarketing). New faces: **emulent.com** (two ranking posts) and a
  **Townsquare Media radio-station network** serving one syndicated "deck builder digital marketing"
  landing page across kpel965.com, kfyo.com, talkradio960.com and tuscaloosathread.com — the same page
  on four local-radio domains. Worth knowing as a SERP-dilution pattern; not an authority target and
  not a content gap. **MJC is absent from both top 10s**, consistent with the last real 0/12.

### 3. Footer credits — 7 of 37 live, zero regressions

All 37 domains curled live (follow redirects, 20s, browser UA, looking for an
`<a href="https://morejobcalls.com…">` with anchor text `MoreJobCalls.com`).

- **live: 7** — apdecks.com, bivianomodularbuilders.com, oasiscustomdecks.com, paynterconstruction.com,
  thewindowprofessor.pro, www.bivianocontracting.com, www.mrpatiocover.com. Every one still carries
  `rel="nofollow noopener"` intact. **No "missing" flips** — nothing that was live has gone away.
- **pending: 30**, unchanged for three weeks. This is still the largest unblocked authority item on the board.
- **Two pending domains cannot be deployed as-is:** `deckoutyourhomebuilds.com` returns **404** and
  `sidingatlantadecks.com` **does not resolve at all**. The VA cannot add a footer to a site that
  isn't serving; these two need Spencer to check whether the client sites still exist before they
  count toward the 35.

### 4. Backlog changes

Phase 0 had been emptied by the Builder (every item shipped), leaving only 4 unchecked items on the
whole board. Added three new Phase 0 items and promoted one, in order:

1. **Optimize `/learn/best-marketing-agency-for-deck-builders/` for brand-naming liftability** — the
   one page with proof of retrieval. Surgical: brand as the subject of the first sentence, keep the
   first-person voice behind it, plus one quotable answer-first line naming brand + trade + channel +
   appointment promise. No keyword change, no new sections.
2. **First-50-words naming audit of the 8 hire-intent /learn/ pages** — same gate, applied where it
   pays next. Opening-paragraph edits only.
3. **`/learn/best-marketing-agency-for-fence-companies/`** — kw *best marketing agency for fence
   companies*. Replicates the only page shape an engine has cited us for, into vertical #2, against a
   cited field of five thin agency pages. Does not touch `/trades/fence-company-marketing/`'s keyword.
4. **Promoted `/trades/roofing-leads/` refresh from Phase 2 to Phase 0** — kw *roofing marketing
   company*. Its hire-intent question drew 10 citations (joint-largest field we track), it is the one
   cluster where inclusion pitches and our own page both have a path, and the page already has the best
   GSC demand of any MJC page (707 impressions / 6 clicks / 90 days) — being looked at and
   under-converting, not undiscovered.

Phase 2 keeps 3 items; Phase 3 untouched (needs Spencer). **7 unchecked Phase 0/1/2 items queued.**
No ticked items removed, no keyword collisions, page rules header intact.

### Binding constraint this week: **ON-PAGE / TOPICAL — brand-naming liftability.**

For three weeks this log has named authority/mentions, correctly: DR 0, 7 of 37 footer credits, Clutch
at 1 review. That work is still the volume lever and still belongs to Spencer. But this week produced
first-party evidence that a harder gate sits in front of it. An answer engine retrieved an MJC page and
came away without the brand, because the passage it read says "my company" instead of "MoreJobCalls.com".
At 0/18 named, more citations cannot score while that is true — authority buys retrieval, and retrieval
is now demonstrably reachable, but naming converts it. The gate is cheap to fix, it is entirely inside
the Builder's remit, and the top two Phase 0 items are that fix. Expect authority to return to the top
of this line once naming is closed.

---

## 2026-10-12 — Both boards measured. Both flat. Constraint: AUTHORITY / MENTIONS.

First run in five weeks where **both** scoreboards carried real data. Neither moved. The useful
finding this week is not in either number — it is in what the two of them, plus a fourth
consecutive quiet rival diff, now jointly rule out.

### 1. Google scoreboard — measured, Action healthy

Newest row **2026-10-08** (4 days old). The Apify monthly-limit outage that blacked out 09-17
through 10-01 is over: runs 14 and 15 both returned `status: OK` with all 20 keywords. Scheduled
runs land ~17:50 UTC rather than the nominal 11:17, so **today's Monday run had not fired at pass
time** — that is normal GitHub scheduler lag on this repo, not a failure.

| metric | 2026-10-08 | 2026-10-06 | 2026-09-14 |
|---|---|---|---|
| **beats both** (core 12) | **0/12** | 1/12 | 0/12 |
| beats DBM | 0 | 1 | 0 |
| beats Slamdot | 3 | 3 | 0 |
| MJC in top 50 | 3 | 4 | 0 |
| MJC in top 10 | 1 | 1 | 0 |

MJC's three ranked core keywords on 10-08: `deck builder marketing agency` **#8**
(`/learn/deck-builder-marketing-companies-compared/`), `deck builder lead generation` **#20**
(`/learn/deck-builder-lead-generation/`), `how to get more deck jobs` **#40**
(`/trades/deck-builder-marketing/`). Extended: `how to get deck leads` **#16**.

**No 7-day comparison is available.** The only two real snapshots since the outage are 48 hours
apart (10-06, 10-08), so the "vs ~7 days earlier" column above is against 2026-09-14 — before the
outage, and before ~15 pages shipped.

**Movers, and why they are being discounted.** MJC lost four positions between the two runs
(`how to get more deck jobs` #3 → #40, `decking leads` #8 → gone, `facebook ads for deck builders`
#12 → gone, `deck company marketing` #17 → gone) and the single beats-both win was given back.
Taken alone that reads as a collapse. It is not, and the reason is in the rivals' columns of the
same diff: DBM's **homepage replaced its blog posts** at or near the top of nine keywords
simultaneously (`deck builder seo` #20 → #1, `marketing for deck builders` #14 → #2,
`deck builder leads` #28 → #4, `best marketing agency for deck builders` #6 → #2), and Slamdot's
`/industries/decking/` replaced its blog posts on six (`marketing for deck contractors` #4 → #25,
`deck builder advertising` #4 → #14, `deck contractor marketing` #40 → #22). Twelve keywords do not
independently reshuffle the ranking URL for three unrelated domains inside 48 hours. One of the two
scrapes saw a different SERP — different data centre, different personalisation, or a live Google
update mid-flight. **Standing rule reaffirmed: two runs in a row, or it did not happen.** Nothing
was re-planned on the strength of this diff and no page was rewritten over it.

**Striking distance (#11–30): two keywords, zero promotable.** `deck builder lead generation` (#20)
and `how to get deck leads` (#16) both rank the same URL, `/learn/deck-builder-lead-generation/`,
which the builder fully rewrote on **2026-10-09** — three days ago, 4,219 → 5,840 words. Google has
not re-crawled it. Re-touching it would destroy the only clean measurement we are going to get of
whether a striking-distance pass actually works. Left alone deliberately; the builder has been told
so in the backlog read block.

### 2. AI-answer (LLMO) scoreboard — identical to last run, which makes the one gain real

Source `scripts/llmo_grounded_history.jsonl`, run **2026-10-08** (4 days old, Action healthy, run 9
`success`).

| metric | 2026-10-08 | 2026-10-01 | 2026-09-24 | 2026-09-18 |
|---|---|---|---|---|
| MJC **named** | 0/18 | 0/18 | 0/18 | 0/18 |
| named, hire-intent | 0/13 | 0/13 | 0/13 | 0/13 |
| **MJC URL cited** | **1** | **1** | 0 | 0 |

Every figure identical to 10-01. Under the 2+ runs rule that is the first LLMO result this project
can actually bank: `/learn/best-marketing-agency-for-deck-builders/` cited for **"Facebook ads agency
for deck builders that guarantees appointments"** — same page, same question, two consecutive runs.
Retrieval of that one page is now a stable property of the index, not a fluke.

Most-cited domains: clicksgeek.com (11), footbridgemedia.com (6), minyona.com (5), designrush.com (4),
deckbuildermarketers.com (4), sociusmarketing.com (4), comradeweb.com (4), serviceallies.com (4),
homeservicedirect.net (4). Most-named rivals: Angi (8), HomeAdvisor (6), Thumbtack (6),
Footbridge (5), CraftJack (4).

**The naming fix landed and changed nothing — which is the finding, not a failure.** Last week's
constraint was brand-naming liftability, and it was fully worked: 10-05 on the reference page, 10-06
across the other seven hire-intent `/learn/` pages, 10-07 on the new fence page. The 10-08 run moved
by **zero on every metric, citations included**. The explanation is not that naming did not matter —
it is that naming can only pay off on a page that gets retrieved, and **we are retrieved once in ~94
citations**. A perfectly quotable page that is never fetched cannot put the brand in an answer.
Naming was a real gate; it was not the one metering the volume. That gate is now shut behind us.

Footnote: the legacy no-search probe (`llmo_history.jsonl`) and the 108-answer panel
(`llmo_panel_history.jsonl`, 1.9% named, 95% CI 0.5–6.5% on 2026-10-06) are consistent with the
grounded 0/18 and add nothing this week.

### 3. Citation classification (step 1b) — first pass over the new 2026-10-08 snapshot

`llmo_citations.json` refreshed to the 10-08 run, 94 URLs. The 10-05, 10-06 and 10-08 passes all
worked the stale 10-01 snapshot, so this is the first classification of the current one. Full
breakdown written into `authority_pipeline.md`. Summary: **(a)** ~57 competitor agency service pages
(not actionable); **(b)** 8 third-party roundups not already pipelined, all 8 fetched and confirmed
live; **(c)** 1 MJC URL and the marketplace rosters.

**Three added** to `authority_pipeline.md`, tagged `listicle inclusion (AI-cited 2026-10-08)`:

| page | cited for | why it is addable |
|---|---|---|
| `regie.ai/blog/compare-the-top-contractor-lead-generation-companies-for-2026` | "What's the best lead generation service for contractors?" | SaaS publisher competing with nothing we sell; already lists two real agencies (Clicks Geek, Contractor Growth); general editorial email |
| `phonexa.com/blog/lead-generation-companies-for-contractors/` | "Who guarantees leads or appointments for contractors?" — the exact MJC offer | Lead-management software; page states it "doesn't sell contractor leads per se", that listees are unaffiliated, and that the ranking is the team's opinion; six real agencies listed; named author |
| `labtorio.com/blog/best-websites-for-contractor-leads/` (cited ×2) | outdoor-living lead gen; Angi/HomeAdvisor alternatives | marketplace-only roster, so a weak ask — but it has a bylined author, which the other rosters do not |

**Five rejected, with reasons:** `abstraktmg.com` (written by Abstrakt's own CEO, Abstrakt ranked
"Best Overall" — self-ranked); `insideadvisorpro.com` (page discloses Inside Advisor shares an owner
with EverConnect, one of its eight entries — a house list); `marketerhire.com` (MarketerHire at #1 of
8, rest are enterprise agencies — wrong tier plus self-ranking); `handoff.ai` (five marketplace slots
under an "11 best" title, no author, no editorial contact); `usehatchapp.com` (titled "in 2023",
published May 2023 — stale, marketplace-only).

**Fourth consecutive pass confirming the same structural fact, now 22 roundups checked:** the broad
hire-intent AI answers are assembled almost entirely from marketplace rosters and vendor
self-ranked lists, and MJC can be added to neither. The two real adds this week are the first
exceptions, and they share a trait worth prospecting on purpose from here: **both publishers are
software companies, not agencies or marketplaces.** A SaaS or martech blog that lists agencies has
no commercial reason to keep MJC off its list. That is a lane, and it has been handed to the
Prospector in the pipeline note.

No new Phase 0 page item came out of the classification: every question cluster with a thin cited
field now has an MJC page. The one gap found — "Are Angi and HomeAdvisor leads worth it?", cited
field of five thin review posts — was deliberately filed as an **optimization of an existing page**
rather than a new one, because MJC already owns two pages in the Angi cluster and a third would
deepen the cannibalisation that §5 below exists to fix.

### 4. Rival watch — DBM's content engine has now been off for 28 days

| | live | stored | change |
|---|---|---|---|
| deckbuildermarketers.com | 281 | 282 | +1 new, −2 removed |
| slamdot.com (deck/decking/contractor) | 9 | 9 | unchanged, sixth consecutive week |

The one new DBM URL is `/senior-marketing-specialist-remote-marketing-agency-jobs/` — a job posting.
The two removed are `/your-journey-with-deck-builder-marketers/` and its `-v2/`, the funnel pages
tracked as "new" the last two weeks; they have been unpublished. So DBM's fourth consecutive weekly
diff shows **zero new editorial content** and, for the first time, net page loss. `rival_urls.json`
re-baselined.

Live top-10 check (WebSearch, Bing/Brave-flavoured index — *not* Google, and therefore closer to what
the AI probe draws on): **neither MJC nor DBM appears** on "deck builder marketing" or "marketing for
deck builders". The top 10 is Footbridge Media (×2), Socius Marketing (×2), ClicksGeek, plus two new
domains worth noting: **emulent.com** (×2, a syndicated "lead growth playbook" post) and a
**Townsquare Media radio-station syndication cluster** — kfyo.com, tuscaloosathread.com, kpel965.com,
talkradio960.com all carrying the identical "deck builder digital marketing" advertorial. The second
is a paid placement network rather than an editorial target; logged here, not pipelined.

### 5. Backlog re-plan

- **No striking-distance promotions** (see §1 — both #11–30 keywords point at a page rewritten 3 days ago).
- **Added, top of Phase 0: core-keyword URL ownership audit.** Mechanical, no new page. On 10-08 two of
  MJC's three ranked core keywords ranked the **wrong URL**: `deck builder marketing agency` → the
  comparison page (#8) when the page rules name the pillar as owner, and `how to get more deck jobs` →
  the pillar (#40) when the dedicated page exists and held #3 with it on 10-06. This is the third
  occurrence of one defect — the builder found and fixed the same shape on 10-08 for
  `facebook ads for deck builders`, where the Google Ads page was ranking at #12 and the dedicated
  Facebook page was absent entirely, and the fix was anchor text, not content. Three is a pattern: the
  site's deliberate anchor-text variation means nothing tells Google which URL owns which core query,
  so Google picks, and it keeps picking wrong. The item asks for one nomination table across all 12
  core keywords, written back into the file so the next audit is a diff.
- **Added, Phase 0 #2:** optimize `/learn/angi-homeadvisor-alternatives-for-contractors/` for
  **are angi leads worth it** (see §3).
- **Added, Phase 2:** `/learn/google-business-profile-for-deck-builders/`. The largest untouched rival
  gap in the baseline, open since 09-14 and simply never worked: Slamdot owns **three** pages in the
  GBP/local lane — more than on any other topic — and Slamdot is the rival beating us at #2 on
  `deck builder seo`. MJC has no GBP page at all. Scoped tightly away from `/learn/deck-builder-seo/`
  and `/learn/seo-for-contractors/`.
- **No rival-gap item from new rival content**, because there was none (§4).
- Queue state: **7 open Phase 0/1/2 items** (target ≥5), 1 Phase 3 untouched, all 29 ticked items
  preserved, page-rules header intact.

### 6. Footer credits — 7/37, unchanged for a second week, and the base is shrinking

Swept all 37 domains (curl, follow redirects, 20s, browser UA, looking for an `<a>` to
`https://morejobcalls.com` with anchor text exactly `MoreJobCalls.com`).

**7 live, 30 not carrying it, 0 regressions.** Live: apdecks.com, bivianomodularbuilders.com,
oasiscustomdecks.com, paynterconstruction.com, thewindowprofessor.pro, www.bivianocontracting.com,
www.mrpatiocover.com — every one still carrying the credit with the anchor intact. **Nothing has been
deployed in 7 days.**

Three pending domains cannot be deployed as-is, one more than last week:
`deckoutyourhomebuilds.com` 404s, `sidingatlantadecks.com` fails the TLS handshake, and
**`mrpatiocoverdecks.com` newly stopped resolving this week** — it served a 200 page on 10-05 and now
fails to connect. (Its live-credit sibling `mrpatiocover.com` is unaffected.) Effective deployable
base is **34 of 37**, so the honest denominator is shrinking while the numerator holds still.

### 7. Binding constraint: AUTHORITY / MENTIONS

Changed from last week's on-page/brand-naming. Three independent lines of evidence, and the first is
close to decisive:

1. **DBM has published nothing editorial for 28 days** — four consecutive weekly sitemap diffs, and
   this week it removed two pages — and still holds **#1 or #2 on all 12 core keywords**. A rival
   whose content engine has been switched off for a month, and which is shedding pages, is not being
   held at the top by content. It is being held there by DR 28 and ~494 referring domains.
2. **Three extended keywords have no rival in the top 50 at all** — `outdoor living contractor
   marketing`, `fence company marketing`, `patio cover marketing` — and MJC has a dedicated,
   deliberately refreshed page for each (09-20, 09-22, 09-23) and ranks on **none** of them. An
   uncontested field we still cannot enter is not an on-page problem.
3. **The two other candidates are ruled out.** Indexation: GSC 36 indexed (09-28), and MJC pages
   demonstrably do rank — #8 and #20 on core keywords. On-page/topical: last week's naming gate was
   fully closed across all 8 hire-intent pages and the AI board moved by exactly zero, because at 1
   citation in ~94 we are almost never retrieved in the first place.

Meanwhile **every authority asset is still at `new`**: 7/37 footer credits (flat for a second week),
Clutch at 1 review against a bar of 3, and DesignRush, UpCity, GoodFirms, Sortlist and the LinkedIn
company page all unstarted. `authority_pipeline.md` is now 88 rows deep and has converted essentially
none of them.

The uncomfortable part, stated plainly because it is the actionable part: **the content engine is a
month ahead of the authority engine, and every item that would close the gap is Spencer-gated.**
Neither the builder nor the prospector can create a referring domain, file a Clutch review, or deploy
a footer credit. Two robot routines shipping ~15 pages a month cannot substitute for the three or four
hours of account creation and review-asking that would move DR off 0. Until that happens the
scoreboards will keep reading flat, and the pages will keep being good and unranked.

The URL-ownership audit at the top of Phase 0 is the exception worth shipping anyway: it is the one
place where on-page work still has unclaimed upside, it is mechanical, and it is cheap.
