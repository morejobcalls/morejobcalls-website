# Outrank backlog — morejobcalls.com vs deckbuildermarketers.com + slamdot.com/industries/decking/

The daily builder routine takes the TOP unchecked item, ships it finished, and ticks it
(`[x] YYYY-MM-DD <live url>`). The Monday strategist re-orders this file from the
scoreboard (`scripts/rank_history.jsonl`). Only the strategist adds or re-orders items;
the builder only ticks.

Win condition: MJC above BOTH rivals on >=7 of the 12 CORE keywords in
`scripts/rank_tracker.py`, two scoreboard runs in a row.
Baseline 2026-09-10: 0/12. MJC not in the top 50 on any core keyword.

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
- No internal pricing. No invented client numbers. Guarantee wording exactly per the routine prompt.

## Queue (top = next)

> **Strategist read 2026-09-14 — the queue is not the bottleneck, indexation is.**
> MJC is absent from the top 50 on all 20 tracked keywords, including
> `outdoor living contractor marketing` and `patio cover marketing` where NO rival ranks
> either. An indexed page on an open-field keyword lands *somewhere* in a top 50. Absent
> everywhere, plus absent on a branded `morejobcalls.com` search, reads as not-indexed
> rather than out-ranked. Robots, canonicals, 200s and the 36-URL sitemap all check out,
> so this is a crawl/discovery problem for Google to solve, not an on-page one
> (Spencer: GSC sitemap submit + request-indexing — see the weekly Slack).
> Keep shipping: the content compounds the day indexation clears. But do not read
> "no movement" as "the pages are wrong" until MJC appears in a top 50 at all.
> No striking-distance (#11–30) items exist to promote this week for the same reason.

### Phase 0 — LLMO: pages for the questions AI answers already cite (added 2026-09-18, work these FIRST)
Source: `scripts/llmo_citations.json` + `scripts/llmo_grounded_history.jsonl` (grounded probe, MJC named 0/18 on 2026-09-18).
AI answers are built from small agency pages and comparison posts, not big brands. Each item below targets a question cluster
where the cited pages are thin and MJC has better evidence. Extra rule for these pages: the first paragraph must state, in
one plain sentence, what MoreJobCalls is ("MoreJobCalls is a marketing company for deck builders and other home-service
contractors that ...") so an answer engine can lift it verbatim. Put a dated "Updated <Month YYYY>" line near the top.
- [x] 2026-09-18 Pillar tune `/trades/deck-builder-marketing/` https://morejobcalls.com/trades/deck-builder-marketing/ — shipped as "Deck Builder Marketing Agency That Books Jobs | MoreJobCalls" (60 chars exactly; the string specified below was 65 and the page rule caps titles at 60, so "Deck" was dropped from "Deck Jobs" — it is still in "Deck Builder"). Entity sentence added to the first 50 words, visible "Updated September 2026" line under the H1, dateModified bumped. Original item: title → "Deck Builder Marketing Agency That Books Deck Jobs | MoreJobCalls" (the AI prompt is "best marketing agency for deck builders" and every cited page says "agency"); add the one-sentence entity statement to the first 50 words; add a visible "Updated September 2026" line. Keep the URL.
- [x] 2026-09-18 `/learn/angi-alternatives-for-deck-builders/` https://morejobcalls.com/learn/angi-alternatives-for-deck-builders/ — kw **angi alternatives for deck builders** (+ homeadvisor alternatives, thumbtack alternatives). Most-cited cluster in the panel (7+ comparison pages cited, none deck-specific). Honest table: Angi, HomeAdvisor, Thumbtack, Houzz Pro, Porch, Google LSA, own Meta ads, done-for-you appointments; shared vs exclusive, what you pay for, what a booked appointment really costs. Link to `/learn/angi-homeadvisor-alternatives-for-contractors/` (contractor-general) and differentiate. Supersedes the Phase 2 "angi-vs-homeadvisor-vs-thumbtack" item.
- [x] 2026-09-20 `/learn/contractor-cost-per-lead-by-trade/` https://morejobcalls.com/learn/contractor-cost-per-lead-by-trade/ — kw **how much should a contractor pay per lead** (+ cost per lead for contractors 2026). 7 thin blogs cited. Use ONLY numbers already published on MJC case-study pages (e.g. $400 to $30 per lead, $100/day → $320K), plus the cost-per-booked-appointment reframe. No internal pricing.
- [x] 2026-09-20 Refresh `/learn/contractor-appointment-guarantees-explained/` https://morejobcalls.com/learn/contractor-appointment-guarantees-explained/ (named-competitor list pulled pre-publish, held in morejobcalls-seo/ for Spencer) for **who guarantees appointments for contractors**: cited answers are 5 thin homepages (allforcontractor, contractorai, homebuddy, contractorleadpartners, contractorappointments). Add a comparison table of guarantee TYPES (credit-back, lead replacement, fee refund, fixed cash remedy), what to demand in writing; MJC's own guarantee in canonical Take A wording only.
- [x] 2026-09-20 `/learn/outdoor-living-contractor-marketing/` https://morejobcalls.com/learn/outdoor-living-contractor-marketing/ — promote from Phase 2. Cited answers for outdoor living / patio cover lead gen are all small single-purpose sites (yardreach, dirt2dollars, seoforoutdoorliving). Open field.

- [x] 2026-09-20 Site-wide LLMO entity pass: the one-sentence entity statement + "Updated September 2026" + dateModified on every /learn/ page, trade-specific entity sentence on all 8 trade pages, full Organization node (name MoreJobCalls, legalName MoreJobCalls.com LLC) embedded on every page, About page + homepage schema aligned, llms.txt rewritten (entity header, question map; removed pricing and universal one-per-market claim).

### Phase 1 — money keywords with a rival in the top 10
- [x] 2026-09-10 `/trades/deck-builder-marketing/` pillar rebuild (3.8K words, 12 FAQs, 10 inbound case-study links)
- [x] 2026-09-11 `/learn/deck-builder-leads/` https://morejobcalls.com/learn/deck-builder-leads/ — kw **deck builder leads** (+ leads for deck builders, decking leads). Angle: shared vs exclusive, what a deck lead really costs once you count no-shows, and what to buy instead. Rivals: DBM #25, Slamdot #19. Top 3 are marketplaces (serviceallies, minyona, builderprime): out-depth them on honest math.
- [x] 2026-09-14 `/learn/facebook-ads-for-deck-builders/` https://morejobcalls.com/learn/facebook-ads-for-deck-builders/ — kw **facebook ads for deck builders** (+ deck builder advertising). Real campaign structure, creative that works (owner on camera), budget math from the $320K/$100-a-day case. **Weakest field on any money keyword: DBM only #37, Slamdot absent entirely.** Ranking pages are thin agency pages, and this is the one topic where MJC has more real evidence than anyone in the SERP. Ship it well.
- [x] 2026-09-15 `/learn/how-to-get-more-deck-jobs/` https://morejobcalls.com/learn/how-to-get-more-deck-jobs/ — kw **how to get more deck jobs** (+ how to get deck leads). Practical owner playbook: referrals, reviews, speed to lead, ads, follow-up. DBM #22 (and #15 on "how to get deck leads"), Slamdot #24 on the variant. Reddit and Facebook groups rank here, so write it like a builder talking, not an agency.
- [x] 2026-09-16 `/learn/deck-builder-lead-generation/` https://morejobcalls.com/learn/deck-builder-lead-generation/ — kw **deck builder lead generation**. Channel-by-channel ranking by cost per booked appointment, with a table. DBM #18, Slamdot #60.
- [x] 2026-09-17 Optimize `/learn/best-marketing-agency-for-deck-builders/` https://morejobcalls.com/learn/best-marketing-agency-for-deck-builders/ — kw **best marketing agency for deck builders** (DBM #6, Slamdot #20). Added 9-point scorecard table, 8-question call table with weak/real answers, 7 red flags, "what to demand in writing", 8-question visible FAQ + FAQPage schema. Also removed a monthly fee figure and a banned remedy word that were live in the old FAQ JSON-LD (rule 5 / rule 2 violations), and gave the page its first visible FAQ (the old FAQPage schema had no visible counterpart at all). 4 contextual sibling links added in.
- [ ] `/learn/deck-builder-seo/` — kw **deck builder seo**. Honest take: what SEO does for a deck company, how long it takes, when paid social beats it. Slamdot #1, DBM #2 — the hardest field we track, and we don't sell SEO. Deliberately last in Phase 1. Be useful and fair, and route to the pillar.

### Phase 2 — topical depth (extended keywords + questions rivals own)
- [ ] `/learn/deck-builder-marketing-ideas/` — kw **deck builder marketing ideas** (DBM #2, Slamdot #7). 15–20 ideas ranked by effort vs appointments, each with a real example.
- [ ] `/learn/how-much-should-a-deck-builder-spend-on-marketing/` — marketing budget as a % of revenue, ad spend to jobs math from named cases. No MJC pricing.
- [ ] `/learn/angi-vs-homeadvisor-vs-thumbtack-for-deck-builders/` — deck-specific marketplace comparison table. DBM's thumbtack-vs-angi post ranks #8 for lead-gen terms.
- [ ] `/learn/deck-builder-winter-marketing/` — slow-season plan (link to the million-dollar slow-season case study).
- [ ] `/learn/deck-builder-speed-to-lead/` — why deck leads go cold, response-time math, follow-up sequence. Link to why-contractor-leads-dont-answer.
- [ ] `/learn/questions-to-ask-a-deck-marketing-agency/` — interview script + what good answers sound like.
- [x] 2026-09-20 (shipped via Phase 0) `/learn/outdoor-living-contractor-marketing/` — kw **outdoor living contractor marketing** (no rival in the top 50; open field). Link to patio/pergola/pool trade pages.
- [ ] Refresh `/trades/patio-cover-marketing/` for kw **patio cover marketing** (open field, no rival in the top 50) and `/trades/fence-company-marketing/` for kw **fence company marketing** (Slamdot #14, DBM absent).
- [ ] `/learn/lead-magnet-ideas-for-deck-builders/` — kw **lead magnet ideas for deck builders**. Rival gap: Slamdot owns `/blog/5-lead-magnet-ideas-for-deck-builders-that-attract-real-clients/`, MJC has no page. Go further than a list: which magnet actually produces a booked appointment vs. an email address, with the design-and-estimate offer as the worked example.
- [ ] `/learn/deck-builder-referrals/` — kw **how to get more deck referrals**. Rival gap: Slamdot owns `/blog/3-proven-ways-to-boost-referrals-for-your-decking-business/`, MJC has no page. Angle only we can write: why referral volume is capped by job volume, and what to run while you wait. Do NOT overlap `/learn/how-to-get-more-deck-jobs/` — that page owns the broad playbook; this one is referrals only.

### Phase 3 — needs Spencer (strategist raises it; builder never starts these)
- [ ] Deck Builder Marketing Benchmarks 2026: original anonymized data across ~20 builders (CPL, appointment rate, show rate, close rate). Link bait for Deck Specialist, NADRA, supplier blogs. NEEDS Spencer to approve which numbers go public.
- [ ] Named-competitor comparison page. NEEDS Spencer approval: outward claims about a named company.
