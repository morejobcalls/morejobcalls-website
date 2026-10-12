# Core-keyword URL ownership audit

Baseline established **2026-10-12** by the daily builder. Measured against the
**2026-10-08** scoreboard (`scripts/rank_history.jsonl`, status OK).

This file exists so the audit is a **diff next time, not a re-derivation**. The backlog
item that commissioned it is still open (`scripts/outrank_backlog.md`, Phase 0) because
remediation is blocked, not because the diagnosis is missing. Re-run the two scripts in
`Method` below and compare.

> **Status: DIAGNOSIS COMPLETE, REMEDIATION BLOCKED.** See `Blocker` at the bottom.
> Nothing was shipped to the site on 2026-10-12.

## Nomination table

One owner URL per core keyword. "On page" = exact-phrase occurrences in that page's HTML.
"Anchors" = internal `<a>` elements site-wide whose anchor text is *exactly* the keyword.
Target state is **exactly 1** anchor per keyword, pointing at the owner.

| # | core keyword | nominated owner | on page | anchors | 10-08 MJC | verdict |
|---|---|---|---|---|---|---|
| 1 | deck builder marketing | `/trades/deck-builder-marketing/` | 26 | **6** | — | anchors diluted, 5 too many |
| 2 | marketing for deck builders | `/trades/deck-builder-marketing/` | **0** | 1 | — | phrase absent from owner |
| 3 | deck builder marketing agency | `/trades/deck-builder-marketing/` | 4 | **0** | #8 wrong URL | **primary defect** |
| 4 | deck contractor marketing | `/trades/deck-builder-marketing/` | **0** | 0 | — | phrase absent from owner |
| 5 | best marketing agency for deck builders | `/learn/best-marketing-agency-for-deck-builders/` | 12 | **0** | — | needs 1 anchor |
| 6 | deck builder advertising | **none** | **0 site-wide** | 0 | — | **no page targets it** |
| 7 | deck builder seo | `/learn/deck-builder-seo/` | 21 | **0** | — | needs 1 anchor |
| 8 | deck builder leads | `/learn/deck-builder-leads/` | 14 | **0** | — | needs 1 anchor |
| 9 | deck builder lead generation | `/learn/deck-builder-lead-generation/` | 16 | **0** | #20 ✓ | correct URL ranking |
| 10 | leads for deck builders | `/learn/deck-builder-leads/` (secondary) | **0** | 0 | — | phrase absent from owner |
| 11 | facebook ads for deck builders | `/learn/facebook-ads-for-deck-builders/` | 12 | 1 ✓ | — | **at target state** |
| 12 | how to get more deck jobs | `/learn/deck-builder-lead-generation/` | **0** | 0 | #40 wrong URL | see correction below |

Nominations 1–4 are fixed by the page rules in `outrank_backlog.md` (the pillar owns
those five commercial phrases, incl. ext `deck company marketing`). 10 is a secondary on
the same page as 8 because the intent is identical and a third leads page would deepen
the cannibalisation this audit exists to fix.

## Findings

**1. The anchor thesis is confirmed and quantified.** 9 of 12 core keywords have **zero**
exact-match internal anchors anywhere on the site. Exactly one keyword
(`facebook ads for deck builders`) is at the intended target state, and it is the one the
2026-10-08 run fixed by hand. Nothing tells Google which URL owns which core query, so it
picks, which is how `/learn/deck-builder-marketing-companies-compared/` came to rank #8
for `deck builder marketing agency` instead of the pillar.

**2. But anchors are only half of it. 5 of 12 core keywords have no exact-phrase presence
on any indexable MJC page at all:** 2, 4, 6, 10 and 12. You cannot rank for a phrase that
is not on the page, so for these five no amount of anchor work can succeed. The
commissioning backlog item diagnosed this as anchor text only; that is incomplete.

**3. `deck builder advertising` has no page and no mention.** The phrase appears nowhere
on morejobcalls.com. Four rivals rank in the top 15 on it (DBM #5, the DR 56 rival #14,
plus two others at #2 and #3). This is a missing-page gap, not a layer gap, and it needs a
strategist decision, so it is out of a mechanical pass's scope.

**4. `leads for deck builders` is the most winnable core keyword on the board and we have
nothing on it.** DBM's best position is only #16 and the DR 56 rival is #28 — the weakest
rival pair of all 12. The phrase occurs 0 times on its nominated owner.

**5. Correction to the 2026-10-12 strategist note.** That note reads the
`how to get more deck jobs` fall (#3 on 10-06 to gone on 10-08) as SERP noise. It is not.
`/learn/how-to-get-more-deck-jobs/` has been a `noindex` + meta-refresh stub since commit
`bef23a5` on **2026-09-28**, when it was merged into `/learn/deck-builder-lead-generation/`
as a 90-95% duplicate. The 10-06 row records the ranking URL as the stub itself, i.e.
Google was still serving a stale index entry; by 10-08 it had re-crawled and dropped it,
exactly as the `noindex` instructed. **We de-indexed our own best core-keyword position.**
The merge itself was sound and should not be reverted (the content was ported and the
overlap was real), but the merge **did not carry the phrase `how to get more deck jobs`
into the destination page** — it occurs 0 times there. So the keyword's owner is now a
page that never says it. That is the whole defect for #12, and it is a layer fix on the
destination page, not a revert.

## Blocker

Every page this audit needs to edit carries the **superseded three-part guarantee remedy**
(fee-back plus a cash sum plus continued work at no charge), which current hard rules
prohibit publishing. Occurrences in the files involved: pillar 6,
`/learn/deck-builder-leads/` 3, `/learn/deck-builder-seo/` 1, and all five source pages
holding the surplus `deck builder marketing` anchors (7, 3, 3, 2, 1). Site-wide the old
remedy is live on **52 files, ~140 instances**, including the homepage and `/terms/`.

The two most recently built pages (`/learn/deck-builder-lead-generation/`,
`/learn/best-marketing-agency-for-fence-companies/`) already use the safe formulation —
the 100-appointments-in-100-days promise, "guaranteed in writing", and a link to the
published terms, with no remedy restated in body copy — so recent runs have been migrating
pages off the old remedy one at a time without a sweep.

This was **not** swept unilaterally for two reasons: the current remedy wording is
Spencer's to confirm (the SOP named as the single source of truth,
`Fulfillment/Operations/SOPs/public-copy-guardrails.md`, is not in this repo), and on
`/learn/contractor-appointment-guarantees-explained/` the three-part remedy is the
substance of the argument ("that's three remedies stacked"), so it is a copy rewrite, not
a find-and-replace. Spencer was asked on 2026-10-12.

## Next run

1. **Wait for Spencer's guarantee wording.** Then do the guarantee sweep and this audit in
   **one pass**, because they touch the same files and a second pass re-crawls them again
   for nothing.
2. Layer fixes, no new sections: put phrase 2 and 4 into pillar H2s and intro copy; put 10
   into `/learn/deck-builder-leads/` meta and one H2; put 12 into
   `/learn/deck-builder-lead-generation/` as an H2 and one sentence.
3. Anchors: create exactly one exact-match anchor per keyword at its owner, and cut
   `deck builder marketing` from 6 to 1. Vary every other inbound anchor that contains a
   core phrase but points at a sibling — specifically the two anchors carrying
   "deck builder marketing agency" that point at `/learn/best-marketing-agency-for-deck-builders/`
   and `/learn/deck-builder-marketing-companies-compared/` rather than the pillar.
4. Raise `deck builder advertising` (#6) with the strategist as a new-page item.
5. Re-run the method below and update this table.

## Method

Reproduce with the two scripts the 2026-10-12 run used (kept out of the repo deliberately;
they are ~40 lines each and re-derivable from this spec):

- **anchor inventory** — walk every `*.html` outside `_archive/` and `v2/`, extract every
  `<a>` with an internal `href`, strip tags from the inner HTML, normalise whitespace and
  punctuation, lowercase, then count anchors whose normalised text equals a core keyword
  exactly, grouped by target. 2026-10-12: 2,103 internal anchors across 78 files.
- **owner check** — for each nominated owner, test the exact phrase against `<title>`,
  `<meta name="description">`, `<h1>`, every `<h2>`, and the page's raw HTML.

`CORE` is the authoritative list in `scripts/rank_tracker.py` (do not edit that file).
