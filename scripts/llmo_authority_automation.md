# The Authority Engine: automating LLMO authority for MoreJobCalls

Written 2026-11-10. Supersedes the September plan (`llmo_strategy.md` on the retired September branch).
Owner: Spencer. Operators: the Routines named in §6. Public repo: outlet names and statuses only, never
contact details or pitch text.

## 1. What changed since September, and what it proves

| Signal | 2026-09-19 | 2026-11-09 | Read |
|---|---|---|---|
| Google index | nothing | indexed; 4–8 of 12 core keywords in the top 50, 0–1 in the top 10 | indexation solved |
| AI panel (108 grounded runs, Claude engine) | 0% | 4.6% mention rate (CI 2.0–10.4%), 9.3% of answers cite a morejobcalls.com URL | MJC is in the retrieval pool; it is not yet *named* |
| MJC in the probe's most-cited domains | absent | 5th to 13th, week to week | pages are good enough to be fetched |
| Learn pages | 29 | 72 | content is not the constraint |
| Authority pipeline | 35 rows, 1 live | 118 rows, 1 live, 46 tagged AI-cited, ~5 ever pitched | **nothing leaves the pipeline** |
| Footer credits live | 7 / 37 | 7 / 37 | unchanged in 52 days |
| Clutch reviews | 0 | 0 | unchanged |

The machine built in September and October works: three pages a week, every page dated, FAQ-mirrored,
entity-sentenced, merge-gated. The Strategist has named the same binding constraint four weeks running:
**authority / mentions**. And the one part of the system that depends on a human doing the next step
(pitch, list, review, deploy) has produced one live mention in two months.

So the strategy is not "more content" or "better pages". It is: **remove the human from the loop between
"prospect found" and "mention live", everywhere that is safe, and reduce what's left to one tap.**

## 2. Why mentions, and why automation of outreach is the highest-leverage move

How an answer engine decides to *name* a company (as opposed to cite one of its pages):

1. It retrieves 4–8 pages for the rewritten query. For "best deck builder marketing agency" those are
   listicles, directories and competitor service pages (`llmo_panel_citations.json`).
2. It names the companies that appear on **several** of those pages. A company that appears only on its
   own site is a candidate, not an answer. This is why MJC gets *cited* 9% of the time and *named* 4.6%:
   the model reads our page, finds no corroboration, and hedges.
3. Review platforms (Clutch, DesignRush) and "best of" lists are weighted because they look like
   third-party judgement. Reddit and forum threads are weighted as real-world opinion.

Every unit of authority is therefore a *third-party page that says MoreJobCalls is a deck builder
marketing company*. The cheapest unit is an email to a page that already ranks. The pipeline already
holds 118 of them, 46 of which are literally the pages the AI answers are built from. At a realistic
5–10% inclusion rate, working that list produces 6–12 live mentions, which on this panel is the
difference between 4.6% and a double-digit mention rate.

Alternatives considered and why they lose:

- **Paid PR or link agency** ($3–8K/mo): slow, generic, and AI engines weight mentions over links.
  The pitching itself is the automatable part.
- **Buying listicle placement**: many of the cited lists sell slots. Google demotes paid lists, and the
  Prospector's rule (never pay, never link swap) stands. Earned inclusion with proof is what holds.
- **More pages**: 72 pages, flat mention rate. Content is the floor, not the lever.
- **Social-only**: slow for a B2B contractor niche; keep YouTube (it is crawled and trained on), skip
  the rest as an authority play.

## 3. The engine: six loops, ranked by leverage per hour of Spencer's time

| # | Loop | Cadence | What the agent does end to end | Spencer's part | Lead time to a live mention |
|---|---|---|---|---|---|
| 1 | **Outreach** (listicles, directories, comparison posts, podcasts) | weekdays | finds the contact, writes the pitch in Spencer's voice, drafts it in Gmail, sends on approval, follows up twice, triages replies, fulfils asset requests, verifies the mention went live, updates the pipeline | hits Send on a draft (or turns on auto-send for a category) | days to weeks |
| 2 | **Review requests** (Clutch, Google) | weekly check | watches client milestones in the data brain, drafts the ask with that client's published numbers, follows up once, verifies on Clutch | hits Send | days |
| 3 | **Original data** (Deck Builder Marketing Benchmarks) | monthly | aggregates spend, inquiries, cost per booked appointment, show rate across 40+ client ad accounts via the Meta connector and the data-brain workers; publishes/refreshes one dated page; pushes the new numbers to past outreach contacts and trade press | approves the metric list once; approves each monthly draft | one build, then compounding |
| 4 | **Expert quotes and threads** (Featured.com, Qwoted, HARO-style requests; Reddit r/Decks, r/Contractor, FB groups) | daily scan | drafts quotable answers with numbers in Spencer's voice | sends the quote email / posts the Reddit reply himself | days |
| 5 | **Owned-surface sync** (YouTube via vidIQ, learn-page embeds) | weekly | rewrites titles/descriptions with the entity sentence and a link to the matching learn page; embeds the matching video on the page | none, after a one-time vidIQ YouTube verification | immediate |
| 6 | **Entity anchors** (DesignRush, UpCity, GoodFirms, Sortlist, Agency Spotter, LinkedIn company, Crunchbase, Google Business Profile, NADRA directory, Clutch verification) and the **30 footer credits** | once | prepares every field; drives the browser with Spencer present (Claude in Chrome) or hands the VA the paste sheet | one 90-minute co-pilot session; one VA afternoon | days |

Loops 1 and 3 are the plan. Loop 1 is the volume (one email at a time, at scale). Loop 3 is the thing
third parties *want* to link to without being asked, and the page the models will cite for every "how
much / what's normal" question. Everything else is cheap and keeps the entity consistent.

## 4. The approval model (how it stays safe and still runs without Spencer)

Three modes, set per category at the top of the Operator's prompt:

- **draft-only**: the agent drafts, Spencer sends from Gmail. Zero outward action without him.
- **approve-to-send** (default for everything): same as draft-only; the agent additionally recognises
  that a draft was sent and takes over follow-ups, reply triage and verification.
- **auto-send**: for an allowlisted category only (recommended after two weeks: directory "suggest a
  company" forms and listicle inclusion requests), the agent sends without a tap.

The Gmail mailbox is the CRM. Labels: `MJC Outreach/1 Pending` (drafted, waiting on Spencer),
`2 Sent`, `3 Replied` (needs a human read), `4 Live` (mention verified). Contact details stay in Gmail;
the public repo only ever holds outlet name, URL, type and status.

Guardrails the Operator cannot cross: never pay for placement, never offer a link swap, never contact
one outlet more than three times, never send more than 10 emails a day, never quote a number that is not
on a live morejobcalls.com page, guarantee only in the locked wording, never "leads" for our deliverable,
never name or disparage a competitor, never store a contact's email in the repo, honour any
"stop"/"unsubscribe" instantly and permanently.

## 5. Targets (measured by the Monday/Thursday panel and a weekly mentions count)

| Metric | Now (2026-11-09) | 30 days | 60 days | 90 days |
|---|---|---|---|---|
| Live third-party pages naming MJC (pipeline `live`) | 1 | 8 | 18 | 30 |
| Pitches sent (cumulative) | ~5 | 60 | 130 | 200 |
| Clutch reviews | 0 | 3 | 5 | 8 |
| Entity-anchor profiles live | 2 (Clutch, Manifest) | 8 | 10 | 10 |
| Footer credits live | 7 / 37 | 37 / 37 | 37 | 37 |
| AI panel mention rate (Claude engine) | 4.6% | 8% | 15% | 25% |
| AI panel hire-intent mention rate | 6.4% | 12% | 20% | 33% |
| Benchmarks page | none | v1 live | first external citation | monthly refresh habit |

The panel is noisy (CI ±5 points); call a move real only when it holds two runs.

## 6. The agents

### 6.1 MJC Authority Operator (created 2026-11-10; weekdays 14:05 UTC; Slack + Gmail)

Prompt: `scripts/routines/authority_operator.md` (no secrets; safe in the public repo). One run:
inbox pass (replies, follow-ups due) → recognise drafts Spencer sent → send any auto-send-category
drafts → up to five new personalised pitches as Gmail drafts → verify live for anything pitched 7+
days ago → update the Status column of `authority_pipeline.md` → one Slack digest with: drafts waiting
on him, replies needing him, form-only pitches to paste, mentions that went live.

It runs *before* the Authority Prospector (Tue/Thu 15:13) and touches only the Status column, so the two
never collide. The Prospector keeps filling the top of the funnel; the Operator empties it.

### 6.2 MJC Benchmarks Publisher (spec ready; create after Spencer approves the metric list)

Monthly, Meta + Slack connectors. Pulls account-level spend, leads and cost per lead for the last 30 and
90 days across every queryable client account except MJC's own, drops accounts with under $500 spend or
under 10 inquiries, computes **medians, quartiles and n** (never a client-identifiable figure), joins
booked-appointment and show-rate medians from the data-brain workers where available, and drafts
`/learn/deck-builder-marketing-benchmarks/` as an Improver-style branch with a dated "Updated" line, a
"how we counted" box, and a one-paragraph plain-text summary journalists can quote. First run: Slack the
numbers only; Spencer approves which rows go public; thereafter publish via the merge gate and email the
refreshed figures to every outlet in `MJC Outreach/2 Sent` and `4 Live`.

### 6.3 MJC YouTube Entity Sync (spec ready; create after Spencer completes vidIQ YouTube verification)

Weekly, vidIQ + Slack. For each of the 149 videos: title ≤ 100 chars keeps the hook and adds the
category phrase where it fits; description gets the entity sentence, the locked guarantee, the
matching learn-page URL and the booking link; tags carry "deck builder marketing agency",
"MoreJobCalls". Reports changes in one Slack line. Never changes privacy or publish times.

### 6.4 One-time co-pilot session (Spencer, ~90 min, Claude in Chrome)

Directory profiles with the identical entity sentence and the locked guarantee; LinkedIn company page;
Crunchbase; Google Business Profile; Clutch verification; NADRA directory check. The Operator's digest
lists the copy for each field.

## 7. Build order (what happens this week)

1. **Done 2026-11-10**: Gmail labels created; Operator prompt written and Routine created
   (approve-to-send mode); this document; the VA footer-credit sheet restored at
   `scripts/footer_credits_va_batch.md`.
2. **Spencer, 10 minutes**: open Gmail → `MJC Outreach/1 Pending` after the first run, read the five
   drafts, hit Send on the ones he likes. That is the whole daily job in approve-to-send mode.
3. **Spencer, 5 minutes**: complete vidIQ's YouTube verification once (the Operator will prompt when
   it needs it); add the Perplexity and Gemini keys as Action secrets if not already present so the
   panel reports all four engines.
4. **Spencer, one decision**: reply "benchmarks: go" in Slack with any metric he wants excluded; the
   Benchmarks Publisher is created from the spec in §6.2 the same day.
5. **Spencer, one session**: the 90-minute co-pilot block for §6.4, and the VA afternoon for the
   30 footer credits.
6. **After two clean weeks**: flip listicles and directories to auto-send in the Operator prompt.

## 8. What stays human, on purpose

Posting as Spencer on Reddit and in Facebook groups (platform rules and trust), speaking on podcasts,
signing directory terms of service, approving any public claim about a competitor, and deciding which
client numbers become public. Everything else in this plan is a machine's job.
