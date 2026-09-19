# LLMO strategy: get MoreJobCalls named when a contractor asks an AI for a deck marketing agency

Written 2026-09-19. Owner: Spencer. The Builder and Strategist routines edit `scripts/` and site
pages; the items marked **Spencer** below cannot be done from this repo.

The goal in one sentence: when a deck builder (or any outdoor-living contractor) asks ChatGPT,
Google AI Mode, Perplexity, Claude or Copilot "who can get me more deck jobs / appointments", the
answer names MoreJobCalls and cites a morejobcalls.com page.

---

## 1. Where we are today

| Signal | 2026-09-19 | Source |
|---|---|---|
| AI answers naming MJC (grounded, Claude + web search, 18 buyer questions) | **0 / 18** (0 / 13 hire-intent) | `llmo_grounded_history.jsonl` 09-18 |
| morejobcalls.com URL cited in any answer | 0 | same |
| AI answers naming MJC (no search, model memory, 10 questions) | 0 / 10 | `llmo_history.jsonl` |
| Google: `site:morejobcalls.com` | **nothing indexed** | checked 09-14 and again 09-19 |
| Google top 50 on 20 tracked deck keywords | 0 / 20 | `rank_history.jsonl` 09-14 |
| Real referring domains | ~0 (the 449 "referring domains" are a spam redirect network) | `authority_pipeline.md` |
| Client footer credits live | 7 of 37 (30 GHL funnels waiting on the VA) | `footer_credits.json` |
| Clutch reviews | 0 (profile live) | pipeline |

Who owns the answers instead (from the 09-18 grounded probe):

- **How-to questions** ("how do deck builders get more leads", "are Angi leads worth it"): Angi,
  HomeAdvisor and Thumbtack are named in 8–10 of 18 answers. The exact shared-lead sellers MJC
  positions against are the default recommendation.
- **Hire-intent questions** ("best marketing agency for deck builders"): small niche agencies
  whose homepages say the category in the first sentence: deckbuildermarketers.com (cited 5x),
  footbridgemedia.com (4x), contractorgorilla.com, sociusmarketing.com, deckfencemarketers.com,
  superpath.com, buildauthority.com, techtitanva.com. Plus listicles: clicksgeek.com (7x),
  constructionleadpro.com (5x), hardscapemarketingcrew.com (3x, and back in Google's top 10 today).
- Nobody in any answer has a written cash guarantee or named client numbers. That is the opening.

What is already built (so nobody rebuilds it):

- `llms.txt` (kept in sync), `robots.txt` explicitly allowing GPTBot, OAI-SearchBot, ClaudeBot,
  PerplexityBot, Google-Extended, Applebot-Extended, meta-externalagent.
- Organization + Person + Service + FAQPage + BlogPosting + Breadcrumb JSON-LD, `sameAs` to
  YouTube, Instagram, Clutch, The Manifest.
- 29 learn pages and 9 trade pages, each with an answer-first box, tables, FAQ mirrored in schema,
  named client numbers, and (on the newest ones) a one-sentence entity statement in the first
  100 words plus a visible "Updated Month YYYY" line.
- `llmo_probe.py` (Mon/Thu Action) scoring 18 buyer questions through Claude with web search and
  mapping every cited URL into `llmo_citations.json`; `rank_tracker.py`; the authority pipeline
  with 35 targets, 12 of them tagged AI-cited.
- As of today: IndexNow automation (`indexnow.py` + Action), an optional OpenAI engine for the
  probe (ChatGPT's retrieval pool is Bing, which Claude's probe does not see), and three new/
  refreshed Phase 0 pages (see §7).

---

## 2. How an AI answer is made, and why that dictates the plan

There are two ways a brand ends up in an AI answer, and they need different work.

**Path A: retrieval (this is ~80% of the job).** ChatGPT search, Copilot, Perplexity, Google AI
Overviews / AI Mode, Gemini and Claude-with-search all run the same loop: rewrite the question into
1–4 search queries, take the top results from an index, fetch those pages, write an answer, cite
4–6 of them. The index differs by engine, and that matters:

| Engine | Retrieval index | How to get in |
|---|---|---|
| ChatGPT search, Microsoft Copilot | **Bing** | Bing Webmaster Tools + sitemap + IndexNow |
| Google AI Overviews, AI Mode, Gemini | **Google** | Search Console + sitemap + request indexing |
| Claude (claude.ai and API web search) | **Brave Search** | No submit path; Brave crawls what is linked and what is in the big indexes |
| Perplexity | Own crawler (PerplexityBot) + partner indexes | Be linked; PerplexityBot is already allowed |

So being "in the answer" means: (1) the page is in that engine's index at all, (2) it ranks in the
top ~10 for the *rewritten* queries (which are usually plainer than the user's question: "deck
builder marketing agency", "angi alternatives contractors", "cost per lead contractors"), and (3)
the page has a sentence the model can lift verbatim that says who MoreJobCalls is and what it does.

The 09-18 probe shows answers are built from small, specific pages, not big brands. That is good
news: the bar is "clear, specific, indexed, and corroborated", not "DR 70".

**Path B: model memory (~20%, slow).** With search off, a model names what co-occurred with the
category in its training data: directories, listicles, reviews, YouTube transcripts, Reddit
threads, press. This moves in months and is driven by the same third-party work as Path A, so it
comes for free if Path A is done properly. Do not spend separate effort on it.

---

## 3. The three constraints, in the order they bind

### Constraint 1 — Indexation (blocking everything; Spencer, ~1 hour)

The site is not in Google at all, and we have no evidence either way on Bing. No content, schema
or link work can show up in an answer until this clears. Nothing technical is wrong (200s, self
canonicals, sitemap, robots all verified 09-14); the site simply has no discovery path because it
has no real inbound links yet.

1. **Google Search Console**: verify the domain (the DNS TXT method is fastest for a GitHub Pages
   site), submit `https://morejobcalls.com/sitemap.xml`, then use *URL inspection → Request
   indexing* on these eight URLs, in this order: `/`, `/trades/deck-builder-marketing/`,
   `/learn/best-marketing-agency-for-deck-builders/`, `/learn/angi-alternatives-for-deck-builders/`,
   `/learn/deck-builder-lead-generation/`, `/learn/contractor-cost-per-lead-by-trade/`,
   `/learn/outdoor-living-contractor-marketing/`, `/about/`.
2. **Bing Webmaster Tools**: sign in, *Import from Google Search Console* (one click once GSC is
   verified), confirm the sitemap, and check that the IndexNow key
   `https://morejobcalls.com/d986069f56f3407fa4903b98c31babaa.txt` shows as valid. The IndexNow
   Action now pings Bing on every push; that only works once Bing knows the site.
3. **Check weekly** until both show pages: `site:morejobcalls.com` on Google and on Bing. The
   strategist routine should stop treating "flat rankings" as a content signal until this returns
   results.

### Constraint 2 — Corroboration (the actual LLMO work; Spencer + VA, ongoing)

For "best agency" questions the models synthesize from *third-party* pages: listicles,
directories, reviews. A brand with a great site and zero external mentions does not get named,
because the model has nothing to triangulate against. Every item here is a page somewhere else on
the web that says, in effect, "MoreJobCalls is a deck builder marketing agency that books
exclusive appointments and guarantees it".

Priority order (highest signal per hour first):

1. **Clutch reviews — 3 to 5, this month.** Clutch profiles feed the "top agency" lists the models
   cite and are themselves cited. Ask Justin Wylie, Jacob Weaver, Brian Wallace, Chris Walters and
   Derek Lopez; their numbers are already public on the site so the reviews can be specific.
   Specific review text ("booked $320K in deck jobs in 60 days on Meta ads") is what the model
   reads, not the star count.
2. **The AI-cited listicles** (already in `authority_pipeline.md`, tagged AI-cited): 7ten.marketing,
   constructionleadpro.com (two pages), hardscapemarketingcrew.com (back live and in Google's top
   10 for the exact target query as of today), clicksgeek.com, hookagency.com, adaptdigitalsolutions,
   leadgenjay. One pitch, adapted per site: "the only deck-specific agency on your list with a
   written $10,000 cash guarantee and named client numbers; here are five you can verify". Offer
   a real client as a reference. Being added to two of these pages would, on its own, likely put
   MJC in the "best deck builder marketing agency" answer, because those pages are already in it.
3. **Directory profiles with an identical entity sentence**: DesignRush, UpCity, GoodFirms,
   Sortlist, Agency Spotter (all self-serve, all in the pipeline). Use exactly this sentence on
   every one of them and on Clutch/Manifest: *"MoreJobCalls is a marketing company for deck
   builders and other home-service contractors that books exclusive sales appointments onto the
   owner's calendar instead of selling shared leads. 100 exclusive sales appointment
   opportunities in 100 days or less, or we write you a check for $10,000."* Consistency across
   sources is what lets a model resolve "MoreJobCalls", "More Job Calls" and "MoreJobCalls.com LLC"
   into one entity.
4. **The 30 pending footer credits.** Thirty contractor domains MJC already controls, each a real
   crawl path and a real link with a relevant anchor. This is the single largest uncashed item and
   it is a VA task. Ship all 30 in one batch.
5. **Category-adjacent authority**: NADRA membership directory, Deck Specialist / Hardscape
   Magazine contributed article, the two contractor-marketing podcasts, Deck Expo listing. Slower,
   but these are the pages that make model memory (Path B) move.
6. **YouTube and social, cheap and compounding**: every video title/description should carry
   "MoreJobCalls" and a category phrase ("deck builder marketing", "exclusive deck appointments")
   because transcripts and descriptions are crawled and trained on. Spencer answering deck-builder
   questions in Reddit (r/Decks, r/Contractor) and Facebook groups *as himself, with numbers, no
   links* creates co-occurrence in exactly the threads the models weight for "real contractor
   advice".

### Constraint 3 — Content coverage of the rewritten queries (Builder routine; mostly done)

Coverage of the deck cluster is strong. What was missing and is now shipped: cost per lead
(the "how much should a contractor pay per lead" cluster had 7 thin blogs cited and no MJC page),
guarantee types (the "who guarantees appointments" cluster was 5 thin homepages), outdoor living
(open field, no rival in Google's top 50, cited pages are single-purpose sites).

Remaining gaps, in order:

- `/learn/deck-builder-seo/` (Phase 1, hardest field; we do not sell SEO, be fair and route to
  paid social where honest).
- `/learn/deck-builder-marketing-ideas/`, `/learn/how-much-should-a-deck-builder-spend-on-marketing/`,
  `/learn/questions-to-ask-a-deck-marketing-agency/` (Phase 2; each is a query the models rewrite
  hire-intent questions into).
- Roofer and fence variants of the hire-intent pages: the probe asks "roofer looking for a
  marketing company that only works with contractors" and "best marketing agency for fence
  companies" and the trade pages are not written to be lifted for those.
- **Needs Spencer:** the Deck Builder Marketing Benchmarks report (original anonymized data across
  ~20 builders: CPL, appointment rate, show rate, close rate). Original data is the one thing
  listicle authors and trade press link to without being asked, and it is the page the models
  would cite for every "how much / what's normal" question. Decide which numbers can go public.
- **Needs Spencer:** a named-competitor comparison ("MoreJobCalls vs Deck Builder Marketers vs
  Footbridge: exclusivity, ownership, guarantee, what's measured"). These pages get cited for
  "X vs Y" and "alternatives to X" queries and DBM already has one. Requires sign-off on outward
  claims about named companies.

---

## 4. The plan, by week

**Week 1 (Spencer, ~3 hours total)**

- [ ] GSC verify + sitemap + request indexing on the 8 URLs (§3.1)
- [ ] Bing Webmaster Tools import from GSC + confirm IndexNow key (§3.1)
- [ ] Ask 5 clients for Clutch reviews; send each the 2–3 numbers from their own case page
- [ ] Add `OPENAI_API_KEY` as a repo secret so the probe also scores ChatGPT's retrieval pool
- [ ] Green-light the VA on the 30 footer credits; done in one batch
- [ ] Decide the canonical brand rendering for third-party profiles (recommendation: "MoreJobCalls";
  keep "More Job Calls" and "SeasonProof Growth LLC" as alternateName, which the schema already does)

**Weeks 2–4**

- [ ] Self-serve profiles: DesignRush, UpCity, GoodFirms, Sortlist, Agency Spotter, identical
  entity sentence, link to `/trades/deck-builder-marketing/` where the profile allows a URL
- [ ] Pitch the 8 AI-cited listicles (pipeline rows tagged AI-cited); track in `authority_pipeline.md`
- [ ] NADRA membership + directory listing
- [ ] Builder routine ships `/learn/deck-builder-seo/` then Phase 2 in order
- [ ] YouTube: retitle/redescribe the 8 proof videos with brand + category phrase

**Weeks 5–8**

- [ ] Benchmarks report (Spencer approves numbers; Builder writes it)
- [ ] Named-competitor comparison page (Spencer approves claims)
- [ ] Contributed article pitch to Deck Specialist and Hardscape Magazine; two podcast pitches
- [ ] Silverback / Web Tonic / Unified / UFO home-services listicles (broader, easier bar)

**Weeks 9–12**

- [ ] Read the probe every Monday. The first time MJC is named, record *which page was cited and
  for which question* in `strategist_log.md` and have the Builder replicate that page's format on
  the nearest uncovered question. Repeat.
- [ ] Deck Expo exhibitor listing decision (paid; Spencer)

---

## 5. On-page rules every page must pass (LLMO checklist)

Already the Builder's rules, restated as the LLMO version so nobody drops one:

1. **Entity sentence in the first 100 words**, word-for-word the same across the site and the
   directory profiles: "MoreJobCalls is a marketing company for deck builders and other
   home-service contractors that books exclusive sales appointments onto the owner's calendar
   instead of selling shared leads."
2. **Visible "Updated Month YYYY"** near the top and `dateModified` in schema; models prefer
   recent, dated pages for "2026" questions.
3. **Answer first**: a Key Takeaway box that answers the title question in two sentences, so the
   lift is trivial.
4. **At least one comparison table**, because tables are what the models turn into "here are your
   options" lists.
5. **FAQ mirrored word-for-word in FAQPage schema.** Each FAQ answer is a self-contained,
   citable paragraph that names MJC where honest.
6. **Named, checkable numbers.** "$5,109.15 → 106 inquiries → 42 appointments → 12 jobs" gets
   cited; "great results" does not. No invented numbers, no internal pricing.
7. **One primary query per page**, exact phrase in title (≤60 chars), H1 and an H2; never two MJC
   pages on one query.
8. **Inbound links from ≥3 sibling pages** and a link into the pillar; the page in `learn/index`,
   `sitemap.xml` and `llms.txt` on the same commit.
9. **Guarantee wording only in the canonical form.** Deliverable is "exclusive sales
   appointments", never "leads", in sentences that describe what MJC delivers.

---

## 6. Scoreboard: what "ranking" means for this goal

The rank tracker is a proxy. The outcome metric is *being named*. Targets, measured by the Mon/Thu
probe (`llmo_grounded_history.jsonl`; both engines once the OpenAI key exists):

| Milestone | Target date | Metric |
|---|---|---|
| Indexed | by 2026-10-03 | `site:morejobcalls.com` returns pages on Google and Bing |
| First citation | by 2026-10-17 | any morejobcalls.com URL cited in any of the 18 answers |
| First named, hire-intent | by 2026-10-31 | MJC named in ≥1 of 13 hire-intent questions |
| In the deck answer | by 2026-11-30 | named in ≥4 of 13 hire-intent, including "best marketing agency for deck builders" |
| Default recommendation | by 2026-12-31 | named in ≥7 of 13 hire-intent on both engines, two runs in a row |

Leading indicators to read alongside: Bing/Google indexed page counts, GSC impressions on brand +
"deck builder marketing" queries, Clutch review count, live footer credits, live listicle
inclusions, and the rank tracker's top-50 count (it should go from 0 to something the week
indexation clears, which is the confirmation the content is fine).

---

## 7. Shipped on this branch (2026-09-19)

- `scripts/indexnow.py` + `.github/workflows/indexnow.yml`: on every push that touches a page or
  the sitemap, submits the changed URLs (or the whole sitemap) to IndexNow using the existing root
  key file. Bing, and through Bing ChatGPT search and Copilot, learn about new pages in minutes.
- `scripts/llmo_probe.py --grounded --engine openai`: the same 18-question panel through OpenAI's
  Responses API with web search, writing to the same history with an `engine` field and to
  `llmo_citations_openai.json`. The Action runs it automatically once `OPENAI_API_KEY` exists.
- `/learn/contractor-cost-per-lead-by-trade/` (new): "How much should a contractor pay per lead",
  the most-asked how-to question in the panel, with only published MJC numbers.
- `/learn/contractor-appointment-guarantees-explained/` (refreshed): four guarantee types compared,
  what to demand in writing, entity sentence, visible FAQ.
- `/learn/outdoor-living-contractor-marketing/` (new): open-field query, links all four
  outdoor-living trade pages.
- Sibling links, learn index, sitemap and `llms.txt` updated; backlog ticked; the
  hardscapemarketingcrew listicle restored to active in the pipeline (it is live and in Google's
  top 10 for the exact target query again).

---

## 8. What only Spencer can do (the short list)

| Item | Why it can't be automated | Time |
|---|---|---|
| GSC + Bing WMT verification and sitemap submit | Account ownership | 30 min |
| Request indexing on 8 URLs | GSC UI | 15 min |
| Ask 5 clients for Clutch reviews | Relationship | 30 min |
| Approve the VA batch of 30 footer credits | Client sites | 10 min |
| Add `OPENAI_API_KEY` repo secret | Repo admin | 5 min |
| Send the 8 listicle pitches (drafts arrive in Slack from the Prospector) | Outward email | 1 hour |
| Decide which benchmark numbers go public | Business call | 30 min |
| Approve named-competitor comparison claims | Legal/business call | 30 min |

---

## 9. Execution log

**2026-09-19, same day as the plan.** Everything on this list that could be done from the repo or
from Spencer's tools without his sign-in was done:

- Constraint 3 (content) is closed for the deck cluster: all eight remaining Phase 1/2 pages shipped
  (deck-builder-seo, marketing-ideas, marketing budget, questions-to-ask, winter marketing,
  speed-to-lead, lead-magnet ideas, referrals), each with the entity sentence, dated, FAQ mirrored
  in schema, three inbound links, and listed in sitemap, learn index and llms.txt. The site now has
  37 learn pages.
- Entity consistency: the one canonical sentence is in the first 100 words of the homepage, About,
  and all nine trade pages; Organization schema name is MoreJobCalls with the other renderings as
  alternateName.
- `youtube-descriptions.md` carries the entity statement and brand + category keywords on every
  block. `scripts/footer_credits_va_batch.md` is the per-domain paste sheet for the VA.
- In Spencer's Gmail Drafts (unaddressed, ready to send): five Clutch review requests (Wylie,
  Weaver, Wallace, Walters, Lopez) and one listicle pitch template. Directory profile copy, the
  contact-form pitch, and the GSC/Bing click-path are in the private outreach-kit page.

**Still Spencer's** (nothing here can be done from the repo): merge the branch; GSC + Bing WMT
verification, sitemap submit, request indexing; send the six drafts; create the five directory
profiles; approve the VA batch; add `OPENAI_API_KEY`; paste the YouTube descriptions; decide the
benchmark numbers and the competitor-comparison claims; answer forum threads as himself.
