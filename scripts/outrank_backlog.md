# Outrank backlog — morejobcalls.com vs deckbuildermarketers.com + slamdot.com/industries/decking/

The daily builder routine takes the TOP unchecked item, ships it finished, and ticks it
(`[x] YYYY-MM-DD <live url>`). The Monday strategist re-orders this file from the
scoreboard (`scripts/rank_history.jsonl`). Only the strategist adds or re-orders items;
the builder only ticks.

Win condition: MJC above BOTH rivals on >=7 of the 12 CORE keywords in
`scripts/rank_tracker.py`, two scoreboard runs in a row.
Baseline 2026-09-10: 0/12. MJC not in the top 50 on any core keyword.

**When this backlog has no open item, work `scripts/topical_map.md` instead** — the
category-ownership map (~70 open targets across 9 clusters, ranked by leverage). Take
the top open `[ ]` item in the highest-priority open cluster and build it with the
`/cluster-page` conventions. This backlog is depth against two named rivals; the map is
breadth across the whole semantic neighbourhood. Both matter; the backlog wins ties.

**Guarantee, ad spend, client identity, client claims, authority stats:
`Fulfillment/Operations/SOPs/public-copy-guardrails.md` is the single source of truth.**
Read it at the start of every run. Do not trust guarantee wording restated in a routine
prompt or a skill — the paused weekly publisher sat for months with a superseded
guarantee in its prompt, and on 2026-09-27 ten skills were found carrying the
superseded v3.0 remedy six days after v3.1 replaced it.

## Reading the scoreboard (strategist, every run)

`scripts/rank_history.jsonl` rows now carry a `status`. **Before drawing any conclusion,
check the newest row.**

- `status: "NO_DATA"` → the scoreboard was **not measured**. Report "not measured, N days
  stale", name the reason, and **change nothing**. Do not re-order the backlog, do not
  call rankings flat, do not conclude anything about indexation, and never rewrite a page
  on the strength of it. An outage is not a finding.
- `status: "OK"` → a real measurement; read it normally.

**For indexation truth, read Google Search Console — first-party — not a scraper.** When
a scraper and GSC disagree about what Google has indexed, GSC wins.

This rule exists because on 2026-09-28 four consecutive Apify quota 403s produced silence,
and that silence was read as "only the homepage is in the index" — a confident, wrong
conclusion that steered this backlog until GSC (36 indexed) contradicted it. The tool was
broken for $0.13 of overage on a $5/mo free plan. `rank_tracker.py` now records the outage
instead of failing quietly, and the GH Action commits the NO_DATA row and then fails loudly.

## Page rules (every item)
- One primary keyword per page, exact phrase in title (<=60 chars), H1, first 100 words, one H2.
  Never target a keyword another MJC page already owns (check this file first). The pillar
  `/trades/deck-builder-marketing/` owns: deck builder marketing, marketing for deck builders,
  deck builder marketing agency, deck contractor marketing, deck company marketing.
- Answer-first: Key Takeaway box, then at least one comparison table, then an FAQ (FAQPage schema
  matching the visible text word for word).
- 1,500–2,500 words of real substance. Beat the current top 3 results on depth and specificity.
  Read them first (WebFetch) and cover what they cover, plus what only we can say: named client
  numbers from the repo, ad-spend-to-jobs math, the appointment/show-rate layer.
- Link INTO the pillar with a natural contextual anchor, and add links FROM at least 3 relevant
  sibling pages INTO the new page. A page nothing links to does not rank.
- Our deliverable = exclusive sales appointments / deck jobs, never "leads". The keyword may say
  "leads" (title/H1/meta/URL); the sentences describing what WE deliver may not.
- No internal pricing. No invented client numbers. Guarantee wording per
  `public-copy-guardrails.md`, never from the routine prompt (prompts go stale).
- After shipping: IndexNow ping, then **request indexing in Search Console**. IndexNow
  reaches Bing and ChatGPT only; Google is not told by publishing and will leave a new
  page in "Discovered, currently not indexed" for days. Quota ~10-11/day on a rolling
  24h window. Never poll a pending URL - inspections have their own quota.
- No recommended, required or minimum ad budgets and no "all-in" monthly figures (budget is set on the strategy call). Named clients' ACTUAL spend in case studies is fine.
- Never publish a self-ranked "best agencies" list with MJC at #1. Google demotes them and answer
  engines skip the brand that authored the list. A comparison page is fine when it is alphabetical
  and every cell is sourced from the other company's own site (see
  `/learn/deck-builder-marketing-companies-compared/`); a ranking we top is not.
- Exclusive appointments are universal; exclusive territory ("one contractor per market") is VIP tier only. Never state it as universal.
- **Client identity (Spencer, 2026-09-26):** never a client BUSINESS name anywhere on the site (copy, titles, meta/og, alt text, JSON-LD, filenames, captions) — business names are searchable in the Meta Ads Library — and no client logos, @tags or links to client websites. Clients appear as first name + last initial + trade + town ("Chip P., a deck builder in Loomis, CA"); never the owner's surname or full name. Blocklist: `~/.claude/skills/fb-page-legit/identity_blocklist.txt`. The footer-credit program (`scripts/footer_credits.json`) is separate and unchanged.

## Queue (top = next)

> **Strategist read 2026-09-28 — the Google scoreboard is still DARK, and the constraint is now PRECISELY LOCATED.**
> `scripts/rank_history.jsonl` has had no new row since 2026-09-14 (14 days). The Apify actor has now
> returned **HTTP 403 on four consecutive runs** (09-17, 09-21 x2, 09-24) — monthly usage hard limit,
> confirmed again this run from the Action logs. Spencer must raise the Apify plan before any position
> data comes back. There are still **no striking-distance (#11-30) items to promote** — not because none
> exist, but because nobody can see them. Do not infer anything from "flat" rankings.
>
> **What changed this week: the retrieval problem has a sharper diagnosis, and it is not "nothing is indexed".**
> Domain-restricted searches this run returned `https://morejobcalls.com/` with a correct title and an
> accurate content summary — so the **homepage IS in the index**. But three separate queries that exactly
> match deep pages (`patio cover marketing contractors`, `angi alternatives for deck builders exclusive
> appointments`, and the brand query itself) **all returned the homepage and nothing else**, even though
> `/trades/patio-cover-marketing/` and `/learn/angi-alternatives-for-deck-builders/` both serve 200. The
> 2026-09-21 panel's 0.0% retrieval rate was therefore not a serving fault and not a robots fault:
>
> ~~**Only the homepage is in the index. Not one of the ~20 shipped /learn/ and /trades/ pages is.**~~
>
> ⛔ **CORRECTED 2026-09-28 (late) — this conclusion was WRONG, and the reasoning that produced it
> was running on a broken instrument. Do not act on it.** First-party Google Search Console says:
> **36 pages indexed, 14 not indexed.** Two deep pages were inspected live that night and both
> returned "URL is on Google": `/trades/deck-builder-marketing/` and `/trades/siding-leads/`. The
> Performance report shows **48 pages with impression data over 90 days**, including
> `/trades/roofing-leads/` at **707 impressions / 6 clicks** and `/about/` at **212 / 17** —
> impossible for unindexed URLs.
>
> **Why the strategist got it wrong:** the "only the homepage" finding came from Apify
> domain-restricted searches, and Apify had returned **HTTP 403 on four consecutive runs** (the
> same monthly-limit failure noted three paragraphs up). A scraper over its quota returns thin or
> empty results, which look exactly like "nothing else is indexed." The note treated an
> instrument failure as a finding about the site.
>
> **Rule this cost us:** when the measuring tool is known-broken, the correct output is "no data",
> never an inference. And GSC is first-party — when a scraper and GSC disagree about what Google
> has indexed, GSC wins. Check GSC before concluding anything about indexation.
>
> **What is actually true:** indexation is NOT the binding constraint — it went 20 → 36 in a week
> once pages were submitted and indexing was requested. The remaining 14 include 6 that are
> correct by design (a merged page's redirect stub, 2 canonicalised duplicates, 2 fossil 404s).
> Off-site authority is still the real lever, so the 30 pending footer credits remain the top
> unblocked item — that part of the read stands.
>
> That single fact explains the 0/18 grounded score by itself. An answer engine looking for a deck-builder
> answer can only find our generic contractor homepage, never the page actually written for the question.
> Crawl paths are fine — the homepage links all 10 trade pages, the /learn/ hub and 3 articles — so this is
> **crawl budget and trust on a domain with no real inbound links**, not site architecture. An unsubmitted,
> DR-0 domain gets its homepage indexed off third-party brand mentions (Bizapedia, The Manifest and Clutch
> all outrank us on our own brand name) and then gets no crawl spent on its deep pages.
>
> **So the lever is submission and inbound links, and it has not moved in three weeks:** GSC sitemap +
> request indexing, Bing Webmaster + IndexNow, and the **30 pending footer credits**. Those 30 are now the
> highest-leverage unblocked item on the whole board — they are 30 already-indexed contractor domains
> linking *directly at deep /trades/ pages*, which is exactly the crawl signal the deep pages are missing.
> Keep shipping pages — the content compounds the day indexation clears — but **do not rewrite a shipped
> page because it "isn't ranking". It has not been looked at yet.**

### Phase 0 — LLMO: pages for the questions AI answers already cite (added 2026-09-18, work these FIRST)
Source: `scripts/llmo_citations.json` + `scripts/llmo_grounded_history.jsonl` (grounded probe, MJC named 0/18 on 2026-09-18).
AI answers are built from small agency pages and comparison posts, not big brands. Each item below targets a question cluster
where the cited pages are thin and MJC has better evidence. Extra rule for these pages: the first paragraph must state, in
one plain sentence, what MoreJobCalls is ("MoreJobCalls.com is a marketing company for deck builders and other home-service
contractors that ...") so an answer engine can lift it verbatim. Put a dated "Updated <Month YYYY>" line near the top.
- [x] 2026-09-18 Pillar tune `/trades/deck-builder-marketing/` https://morejobcalls.com/trades/deck-builder-marketing/ — shipped as "Deck Builder Marketing Agency That Books Jobs | MoreJobCalls" (60 chars exactly; the string specified below was 65 and the page rule caps titles at 60, so "Deck" was dropped from "Deck Jobs" — it is still in "Deck Builder"). Entity sentence added to the first 50 words, visible "Updated September 2026" line under the H1, dateModified bumped. Original item: title → "Deck Builder Marketing Agency That Books Deck Jobs | MoreJobCalls" (the AI prompt is "best marketing agency for deck builders" and every cited page says "agency"); add the one-sentence entity statement to the first 50 words; add a visible "Updated September 2026" line. Keep the URL.
- [x] 2026-09-18 `/learn/angi-alternatives-for-deck-builders/` https://morejobcalls.com/learn/angi-alternatives-for-deck-builders/ — kw **angi alternatives for deck builders** (+ homeadvisor alternatives, thumbtack alternatives). Most-cited cluster in the panel (7+ comparison pages cited, none deck-specific). Honest table: Angi, HomeAdvisor, Thumbtack, Houzz Pro, Porch, Google LSA, own Meta ads, done-for-you appointments; shared vs exclusive, what you pay for, what a booked appointment really costs. Link to `/learn/angi-homeadvisor-alternatives-for-contractors/` (contractor-general) and differentiate. Supersedes the Phase 2 "angi-vs-homeadvisor-vs-thumbtack" item.
- [x] 2026-09-20 `/learn/contractor-cost-per-lead-by-trade/` https://morejobcalls.com/learn/contractor-cost-per-lead-by-trade/ — kw **how much should a contractor pay per lead** (+ cost per lead for contractors 2026). 7 thin blogs cited. Use ONLY numbers already published on MJC case-study pages (e.g. $400 to $30 per lead, $100/day → $320K), plus the cost-per-booked-appointment reframe. No internal pricing.
- [x] 2026-09-20 Refresh `/learn/contractor-appointment-guarantees-explained/` https://morejobcalls.com/learn/contractor-appointment-guarantees-explained/ (named-competitor list pulled pre-publish, held in morejobcalls-seo/ for Spencer) for **who guarantees appointments for contractors**: cited answers are 5 thin homepages (allforcontractor, contractorai, homebuddy, contractorleadpartners, contractorappointments). Add a comparison table of guarantee TYPES (credit-back, lead replacement, fee refund, fixed cash remedy), what to demand in writing; MJC's own guarantee in canonical Take A wording only.
- [x] 2026-09-20 `/learn/outdoor-living-contractor-marketing/` https://morejobcalls.com/learn/outdoor-living-contractor-marketing/ — promote from Phase 2. Cited answers for outdoor living / patio cover lead gen are all small single-purpose sites (yardreach, dirt2dollars, seoforoutdoorliving). Open field.

- [x] 2026-09-20 Site-wide LLMO entity pass: the one-sentence entity statement + "Updated September 2026" + dateModified on every /learn/ page, trade-specific entity sentence on all 8 trade pages, full Organization node (name MoreJobCalls, legalName MoreJobCalls.com LLC) embedded on every page, About page + homepage schema aligned, llms.txt rewritten (entity header, question map; removed pricing and universal one-per-market claim).

**New this week (2026-09-21), from the 108-answer panel + the citation classification pass:**
- [x] 2026-09-21 `/learn/lead-generation-companies-for-contractors/` https://morejobcalls.com/learn/lead-generation-companies-for-contractors/ — kw **lead generation companies for contractors** (+ best lead generation companies for contractors). The single most-cited cluster in the panel: constructionleadpro, ClicksGeek (3 pages), Abstrakt, InsideAdvisorPro, BuildFolio, Handoff, Hook Agency, Housecall Pro, WebFX, 99calls. The 2026-09-21 authority pass checked them all: **every one is a list of lead *marketplaces*, not agencies**, so MJC can never be pitched onto them — the only way into this answer is to rank our own page. Write it as a category guide, not a ranking: the five ways a contractor can buy lead generation (shared marketplaces, pay-per-lead networks, hourly/retainer agencies, in-house, done-for-you appointments), what each actually costs per *booked* appointment, and how to tell which one a company is when its website won't say. Comparison table by category. Link to `/learn/deck-builder-marketing-companies-compared/` for named companies and to `/learn/angi-homeadvisor-alternatives-for-contractors/`. **Not a "best agencies" ranking and MJC is not #1 on it** — see the page rule below.
- [x] 2026-09-22 Refresh `/trades/fence-company-marketing/` https://morejobcalls.com/trades/fence-company-marketing/ — shipped: title/meta rule-4 fix ("Exclusive Leads" -> books estimates, meta 246->136 chars), visible "Updated September 2026", WebPage node with datePublished/dateModified, second mjc-table (cost per lead vs cost per booked estimate, sourced to Chris Walters/E&C and Chip Paynter), new speed-to-quote section, FAQ 6->8 with schema realigned word-for-word (3 of 6 visible questions did not match their schema), 3 contextual sibling links in. Original item: kw **fence company marketing** (Slamdot #20, DBM absent — the weakest rival field of any keyword we track where a rival ranks at all). Vertical #2 and its own hire-intent AI question ("best marketing agency for fence companies"), where the cited pages are four thin single-purpose sites (fencemarketingpros, fencemarketingxperts, superpath/fencing, hookagency/fence-company-marketing). Give it the full Phase 0 treatment: entity sentence in the first 50 words, visible "Updated September 2026", comparison table, FAQ + FAQPage schema, real fence-client numbers from the repo. Split out of the old combined patio+fence Phase 2 item, which broke the one-keyword-per-item rule.
- [x] 2026-09-23 Refresh `/trades/patio-cover-marketing/` https://morejobcalls.com/trades/patio-cover-marketing/ — shipped: title 62->60 chars with the keyword in front, meta 300->146, rule-4 fix on the Service schema name ("Exclusive Lead Generation" -> "Exclusive Appointment Booking"), visible "Updated September 2026", WebPage node, Key Takeaway answer box, second mjc-table (cost per lead vs cost per completed appointment vs ad spend per signed job, sourced to Chris Walters/E&C and Chip Paynter), new off-season and speed-to-contact sections, two more rows on the channel table covering what the SERP's top pages push (home shows, local SEO), FAQ 6->8 with schema generated from the visible text, 4 contextual sibling links in. Original item: kw **patio cover marketing**. **Open field: no rival ranks in the top 50, and neither do we.** That makes this page the cleanest possible test of the retrieval constraint — the day it appears anywhere in a top 50, indexation has cleared. Same Phase 0 treatment as the fence page. Other half of the split item above.


**New this week (2026-09-28), from the 94-URL citation pass — these are the only two question clusters left where cited pages are thin and MJC has no page:**
- [x] 2026-09-28 `/learn/google-ads-for-deck-builders/` https://morejobcalls.com/learn/google-ads-for-deck-builders/ — kw **google ads for deck builders** (+ deck builder ppc). Cited field is five thin agency service pages (anytimedigitalmarketing has TWO cited pages here — `/deck-building-digital-marketing-agency/` and `/deck-builder-ppc-agency/` — plus semstandard, techtitanva, stratedia), none with real numbers. MJC's `/learn/google-ads-vs-meta-ads-for-contractors/` is contractor-general and keeps that keyword — **this page is deck-specific and must not restate the channel-vs-channel comparison**; link to it instead. Angle only we can write: what a deck builder actually pays per *booked* appointment on search intent vs. paid social, when Google Ads is the right first channel for a deck company and when it is not, LSA vs Search vs PMax for a one-to-five-crew builder. Full Phase 0 treatment (entity sentence in the first 50 words, visible "Updated <Month YYYY>", comparison table, FAQ + word-for-word FAQPage schema).
- [ ] `/trades/hardscape-marketing/` — kw **hardscape contractor marketing**. New trade page; MJC has deck, patio cover, pergola, pool, landscaping but **no hardscape page**, while `hardscapemarketingcrew.com` takes **14.8% of all AI citations** in the panel (the 6th-most-cited domain) off a page that has been serving a 404 body for three weeks. Cited field otherwise is one blog (renderyards). Open field, adjacent to three trade pages we already own, and the citation share proves answer engines are actively looking for a hardscape answer. Same Phase 0 treatment; link into the deck pillar and the patio-cover and pergola trade pages, and add links FROM those three into this one.

### Phase 1 — money keywords with a rival in the top 10
- [x] 2026-09-10 `/trades/deck-builder-marketing/` pillar rebuild (3.8K words, 12 FAQs, 10 inbound case-study links)
- [x] 2026-09-11 `/learn/deck-builder-leads/` https://morejobcalls.com/learn/deck-builder-leads/ — kw **deck builder leads** (+ leads for deck builders, decking leads). Angle: shared vs exclusive, what a deck lead really costs once you count no-shows, and what to buy instead. Rivals: DBM #25, Slamdot #19. Top 3 are marketplaces (serviceallies, minyona, builderprime): out-depth them on honest math.
- [x] 2026-09-14 `/learn/facebook-ads-for-deck-builders/` https://morejobcalls.com/learn/facebook-ads-for-deck-builders/ — kw **facebook ads for deck builders** (+ deck builder advertising). Real campaign structure, creative that works (owner on camera), budget math from the $320K/$100-a-day case. **Weakest field on any money keyword: DBM only #37, Slamdot absent entirely.** Ranking pages are thin agency pages, and this is the one topic where MJC has more real evidence than anyone in the SERP. Ship it well.
- [x] 2026-09-15 `/learn/how-to-get-more-deck-jobs/` https://morejobcalls.com/learn/how-to-get-more-deck-jobs/ — kw **how to get more deck jobs** (+ how to get deck leads). Practical owner playbook: referrals, reviews, speed to lead, ads, follow-up. DBM #22 (and #15 on "how to get deck leads"), Slamdot #24 on the variant. Reddit and Facebook groups rank here, so write it like a builder talking, not an agency.
- [x] 2026-09-16 `/learn/deck-builder-lead-generation/` https://morejobcalls.com/learn/deck-builder-lead-generation/ — kw **deck builder lead generation**. Channel-by-channel ranking by cost per booked appointment, with a table. DBM #18, Slamdot #60.
- [x] 2026-09-17 Optimize `/learn/best-marketing-agency-for-deck-builders/` https://morejobcalls.com/learn/best-marketing-agency-for-deck-builders/ — kw **best marketing agency for deck builders** (DBM #6, Slamdot #20). Added 9-point scorecard table, 8-question call table with weak/real answers, 7 red flags, "what to demand in writing", 8-question visible FAQ + FAQPage schema. Also removed a monthly fee figure and a banned remedy word that were live in the old FAQ JSON-LD (rule 5 / rule 2 violations), and gave the page its first visible FAQ (the old FAQPage schema had no visible counterpart at all). 4 contextual sibling links added in.
- [x] 2026-09-24 `/learn/deck-builder-seo/` https://morejobcalls.com/learn/deck-builder-seo/ — kw **deck builder seo**. Honest take: what SEO does for a deck company, how long it takes, when paid social beats it. Slamdot #1, DBM #2 — the hardest field we track, and we don't sell SEO. Deliberately last in Phase 1. Be useful and fair, and route to the pillar.

### Phase 2 — topical depth (extended keywords + questions rivals own)
- [x] 2026-09-25 `/learn/deck-builder-marketing-ideas/` https://morejobcalls.com/learn/deck-builder-marketing-ideas/ — kw **deck builder marketing ideas**. 18 ideas in three tiers ranked by effort vs sat appointments, 2 mjc-tables (the 18-idea ranking, and the inquiry-to-sat-appointment loss table the rival lists stop short of), off-season section, small-market objection section, 8-question FAQ + matching FAQPage schema, 5 sibling links in. NOTE: CTA band states the 100-in-100 promise and links the terms but omits the remedy wording — the routine's canonical "$10,000 check" phrasing is contradicted by the live Guarantee Terms at apply.morejobcalls.com/terms (fee refund + $2,000 + continued service), so no remedy was published either way. Flagged to Spencer 2026-09-25.
- [ ] `/learn/how-much-should-a-deck-builder-spend-on-marketing/` — marketing budget as a % of revenue, ad spend to jobs math from named cases. No MJC pricing.
~~`/learn/angi-vs-homeadvisor-vs-thumbtack-for-deck-builders/`~~ — **SUPERSEDED 2026-09-28, do not build.** The shipped Phase 0 page `/learn/angi-alternatives-for-deck-builders/` (2026-09-18) already owns this keyword cluster with the full marketplace comparison table (Angi, HomeAdvisor, Thumbtack, Houzz Pro, Porch, Google LSA). The Phase 0 item said it superseded this one but the checkbox was left open, which would have produced a duplicate-keyword page against the one-primary-keyword-per-page rule. Un-checkboxed rather than deleted so the history stays readable.
- [ ] `/learn/deck-builder-winter-marketing/` — slow-season plan (link to the million-dollar slow-season case study).
- [ ] `/learn/deck-builder-speed-to-lead/` — why deck leads go cold, response-time math, follow-up sequence. Link to why-contractor-leads-dont-answer.
- [ ] `/learn/questions-to-ask-a-deck-marketing-agency/` — interview script + what good answers sound like.
- [x] 2026-09-20 (shipped via Phase 0) `/learn/outdoor-living-contractor-marketing/` — kw **outdoor living contractor marketing** (no rival in the top 50; open field). Link to patio/pergola/pool trade pages.
- [ ] Refresh `/trades/roofing-leads/` for kw **roofing marketing company** (keep *roofing leads* as the secondary; do not drop it from the title). Vertical #3 has its own hire-intent AI question and **seven** cited agency listicles (Thrive, Service Direct, Silverback, Marketing LTB, Owl Roofing, ProLine, Contractor Marketing Pros) — the only cluster where inclusion pitches and our own page both have a path. Full Phase 0 treatment. (The patio-cover and fence halves of the old combined item moved to Phase 0.)
- [ ] `/learn/lead-magnet-ideas-for-deck-builders/` — kw **lead magnet ideas for deck builders**. Rival gap: Slamdot owns `/blog/5-lead-magnet-ideas-for-deck-builders-that-attract-real-clients/`, MJC has no page. Go further than a list: which magnet actually produces a booked appointment vs. an email address, with the design-and-estimate offer as the worked example.
- [ ] `/learn/deck-builder-referrals/` — kw **how to get more deck referrals**. Rival gap: Slamdot owns `/blog/3-proven-ways-to-boost-referrals-for-your-decking-business/`, MJC has no page. Angle only we can write: why referral volume is capped by job volume, and what to run while you wait. Do NOT overlap `/learn/how-to-get-more-deck-jobs/` — that page owns the broad playbook; this one is referrals only.

### Phase 3 — needs Spencer (strategist raises it; builder never starts these)
- [ ] Deck Builder Marketing Benchmarks 2026: original anonymized data across ~20 builders (CPL, appointment rate, show rate, close rate). Link bait for Deck Specialist, NADRA, supplier blogs. NEEDS Spencer to approve which numbers go public.
- [x] 2026-09-21 Named-competitor comparison page (Spencer approved 9/21) https://morejobcalls.com/learn/deck-builder-marketing-companies-compared/: 15 companies, alphabetical, every cell sourced from each company's own site. Refresh quarterly (re-verify every cell).
