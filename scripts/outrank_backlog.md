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

### Phase 1 — money keywords with a rival in the top 10
- [x] 2026-09-10 `/trades/deck-builder-marketing/` pillar rebuild (3.8K words, 12 FAQs, 10 inbound case-study links)
- [x] 2026-09-11 `/learn/deck-builder-leads/` https://morejobcalls.com/learn/deck-builder-leads/ — kw **deck builder leads** (+ leads for deck builders, decking leads). Angle: shared vs exclusive, what a deck lead really costs once you count no-shows, and what to buy instead. Rivals: DBM #25, Slamdot #19. Top 3 are marketplaces (serviceallies, minyona, builderprime): out-depth them on honest math.
- [x] 2026-09-14 `/learn/facebook-ads-for-deck-builders/` https://morejobcalls.com/learn/facebook-ads-for-deck-builders/ — kw **facebook ads for deck builders** (+ deck builder advertising). Real campaign structure, creative that works (owner on camera), budget math from the $320K/$100-a-day case. **Weakest field on any money keyword: DBM only #37, Slamdot absent entirely.** Ranking pages are thin agency pages, and this is the one topic where MJC has more real evidence than anyone in the SERP. Ship it well.
- [ ] `/learn/how-to-get-more-deck-jobs/` — kw **how to get more deck jobs** (+ how to get deck leads). Practical owner playbook: referrals, reviews, speed to lead, ads, follow-up. DBM #22 (and #15 on "how to get deck leads"), Slamdot #24 on the variant. Reddit and Facebook groups rank here, so write it like a builder talking, not an agency.
- [ ] `/learn/deck-builder-lead-generation/` — kw **deck builder lead generation**. Channel-by-channel ranking by cost per booked appointment, with a table. DBM #8, Slamdot absent.
- [ ] Optimize `/learn/best-marketing-agency-for-deck-builders/` — kw **best marketing agency for deck builders** (DBM #1, Slamdot #6). Add: evaluation scorecard table, questions to ask on the call, red flags, "what to demand in writing", FAQ schema. Keep it a checklist, never a self-ranking listicle.
- [ ] `/learn/deck-builder-seo/` — kw **deck builder seo**. Honest take: what SEO does for a deck company, how long it takes, when paid social beats it. Slamdot #1, DBM #2 — the hardest field we track, and we don't sell SEO. Deliberately last in Phase 1. Be useful and fair, and route to the pillar.

### Phase 2 — topical depth (extended keywords + questions rivals own)
- [ ] `/learn/deck-builder-marketing-ideas/` — kw **deck builder marketing ideas** (DBM #2, Slamdot #7). 15–20 ideas ranked by effort vs appointments, each with a real example.
- [ ] `/learn/how-much-should-a-deck-builder-spend-on-marketing/` — marketing budget as a % of revenue, ad spend to jobs math from named cases. No MJC pricing.
- [ ] `/learn/angi-vs-homeadvisor-vs-thumbtack-for-deck-builders/` — deck-specific marketplace comparison table. DBM's thumbtack-vs-angi post ranks #8 for lead-gen terms.
- [ ] `/learn/deck-builder-winter-marketing/` — slow-season plan (link to the million-dollar slow-season case study).
- [ ] `/learn/deck-builder-speed-to-lead/` — why deck leads go cold, response-time math, follow-up sequence. Link to why-contractor-leads-dont-answer.
- [ ] `/learn/questions-to-ask-a-deck-marketing-agency/` — interview script + what good answers sound like.
- [ ] `/learn/outdoor-living-contractor-marketing/` — kw **outdoor living contractor marketing** (no rival in the top 50; open field). Link to patio/pergola/pool trade pages.
- [ ] Refresh `/trades/patio-cover-marketing/` for kw **patio cover marketing** (open field, no rival in the top 50) and `/trades/fence-company-marketing/` for kw **fence company marketing** (Slamdot #14, DBM absent).
- [ ] `/learn/lead-magnet-ideas-for-deck-builders/` — kw **lead magnet ideas for deck builders**. Rival gap: Slamdot owns `/blog/5-lead-magnet-ideas-for-deck-builders-that-attract-real-clients/`, MJC has no page. Go further than a list: which magnet actually produces a booked appointment vs. an email address, with the design-and-estimate offer as the worked example.
- [ ] `/learn/deck-builder-referrals/` — kw **how to get more deck referrals**. Rival gap: Slamdot owns `/blog/3-proven-ways-to-boost-referrals-for-your-decking-business/`, MJC has no page. Angle only we can write: why referral volume is capped by job volume, and what to run while you wait. Do NOT overlap `/learn/how-to-get-more-deck-jobs/` — that page owns the broad playbook; this one is referrals only.

### Phase 3 — needs Spencer (strategist raises it; builder never starts these)
- [ ] Deck Builder Marketing Benchmarks 2026: original anonymized data across ~20 builders (CPL, appointment rate, show rate, close rate). Link bait for Deck Specialist, NADRA, supplier blogs. NEEDS Spencer to approve which numbers go public.
- [ ] Named-competitor comparison page. NEEDS Spencer approval: outward claims about a named company.
