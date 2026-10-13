# Core-keyword URL ownership audit

Baseline established **2026-10-12** by the daily builder. **Remediated 2026-10-13** against
the **2026-10-12** scoreboard (`scripts/rank_history.jsonl`, status OK).

This file exists so the audit is a **diff next time, not a re-derivation**. Re-run the two
scripts in `Method` below and compare against the table.

> **Status: ANCHOR LAYER COMPLETE. PHRASE LAYER COMPLETE except where blocked.**
> Shipped 2026-10-13: 11 of 12 core keywords now have **exactly one** exact-match internal
> anchor pointing at their nominated owner (was 1 of 12), and the three missing owner
> phrases that were in scope are on their owner pages. Two items remain, both out of a
> mechanical pass's scope: `deck builder advertising` (no page exists) and the site-wide
> guarantee sweep (10 of 51 files done, see `Blocker`).

## Nomination table

One owner URL per core keyword. "On page" = exact-phrase occurrences in that page's HTML.
"Anchors" = internal `<a>` elements site-wide whose anchor text is *exactly* the keyword.
Target state is **exactly 1** anchor per keyword, pointing at the owner.

| # | core keyword | nominated owner | on page | anchors | 10-12 MJC | verdict |
|---|---|---|---|---|---|---|
| 1 | deck builder marketing | `/trades/deck-builder-marketing/` | 24 | 1 ✓ | #8 (companies-compared) | at target; see note A |
| 2 | marketing for deck builders | `/trades/deck-builder-marketing/` | 2 ✓ | 1 ✓ | — | **fixed 10-13** |
| 3 | deck builder marketing agency | `/trades/deck-builder-marketing/` | 4 | 1 ✓ | — | **fixed 10-13** |
| 4 | deck contractor marketing | `/trades/deck-builder-marketing/` | 2 ✓ | 1 ✓ | — | **fixed 10-13** |
| 5 | best marketing agency for deck builders | `/learn/best-marketing-agency-for-deck-builders/` | 12 | 1 ✓ | — | **fixed 10-13** |
| 6 | deck builder advertising | **none** | **0 site-wide** | 0 | — | **no page targets it** |
| 7 | deck builder seo | `/learn/deck-builder-seo/` | 21 | 1 ✓ | — | **fixed 10-13** |
| 8 | deck builder leads | `/learn/deck-builder-leads/` | 14 | 1 ✓ | — | **fixed 10-13** |
| 9 | deck builder lead generation | `/learn/deck-builder-lead-generation/` | 16 | 1 ✓ | — | **fixed 10-13** |
| 10 | leads for deck builders | `/learn/deck-builder-lead-generation/` | **0** | 1 ✓ | **#8, beats both** | re-nominated; see note B |
| 11 | facebook ads for deck builders | `/learn/facebook-ads-for-deck-builders/` | 12 | 1 ✓ | — | at target since 10-08 |
| 12 | how to get more deck jobs | `/learn/deck-builder-one-crew-to-five/` | 2 ✓ | 1 ✓ | #34 | re-nominated; see note C |

**Note A — keyword 1 is an anchor-complete miss, so anchors were not the cause.** All six
exact-match anchors already pointed at the pillar on 10-12 and Google still ranked
`/learn/deck-builder-marketing-companies-compared/` at #8 instead. That page carries the
exact phrase in its title and slug, so it out-matches the pillar on title relevance no
matter how the internal anchors are arranged. Surplus anchors were cut 6 → 1 as specified,
but **do not expect keyword 1 to move from anchor work.** If the pillar is still not the
ranking URL on the next two scoreboards, the question is a title/H1 decision on the pillar
and belongs with the strategist, not another anchor pass.

**Note B — keyword 10 was re-nominated from `/learn/deck-builder-leads/` to
`/learn/deck-builder-lead-generation/`.** The 10-12 scoreboard shows the lead-generation
page at **#8 and beating both rivals** on this keyword, which is the site's only win on the
board. The phrase still occurs 0 times on that page, so it is ranking on intent alone. It
was **deliberately not edited**: the commissioning backlog item puts it under a do-not-touch
order while it is re-crawled, and nothing should be risked on the one keyword we are
winning. The exact-match anchor now points at it from `/learn/deck-builder-leads/`.
**If the next run wants the phrase on the page, confirm the do-not-touch order has expired first.**

**Note C — keyword 12 was re-nominated to `/learn/deck-builder-one-crew-to-five/`.** The
10-12 scoreboard ranks that URL at #34 for the keyword, so it is the page Google already
picked. The 10-12 audit nominated `/learn/deck-builder-lead-generation/` (the merge
destination), but that page is under the same do-not-touch order, and the dedicated
`/learn/how-to-get-more-deck-jobs/` is still a 597-byte `noindex` + meta-refresh stub and
should stay that way: reviving it would re-create the duplicate the 09-28 merge removed.
The phrase is now in an H2 and the answer box on the ranking page.

## Findings

**1. The anchor layer is now at target state and should not be re-derived.** 1,864 internal
anchors across 78 files. 11 of 12 core keywords have exactly one exact-match anchor at their
owner; keyword 6 has none because no page targets it. The 10-12 finding that 9 of 12 had
**zero** anchors is resolved. Next audit should be a one-line confirmation, not a project.

**2. The 10-12 finding that 5 of 12 keywords had no exact-phrase presence anywhere is
resolved for 3 of them** (2, 4, 12). Keyword 10 is deliberately left (note B) and keyword 6
has no page. So the live gap is **one missing page**, not a layer defect.

**3. `deck builder advertising` (#6) remains the only true content gap on the core board.**
The phrase still appears nowhere on morejobcalls.com. This needs a strategist decision on
whether it gets its own page or a pillar section, and it is the last core keyword with no
MJC surface at all.

**4. Anchor work alone will not win this board, and the table above now proves it.** Keyword
1 had a full set of correct anchors on 10-12 and still ranked the wrong URL; keyword 10 has
no phrase presence at all and ranks #8 beating both rivals. Internal linking disambiguates
which URL Google picks. It does not decide whether MJC outranks a DR 28 domain. The
strategist's 10-12 read that the binding constraint is **authority** is consistent with
everything in this file.

## Blocker

The site-wide guarantee sweep is **still open and still Spencer's call.** The superseded
three-part remedy (fee back plus a cash sum plus continued work at no charge) is prohibited
by the builder's hard rules, so every file this audit touched was migrated as it was edited:
**10 files and 17 instances done 2026-10-13**, leaving **41 files and ~141 instances** live,
including the homepage, all ten `/trades/` pages and `/terms/`.

Two reasons it was not swept unilaterally, both unchanged from 10-12:

1. **The replacement remedy is not confirmed.** The routine prompt states a single-remedy
   wording (a cash figure), but `scripts/outrank_backlog.md` explicitly warns not to trust
   guarantee wording restated in a routine prompt, the SOP named as the single source of
   truth (`Fulfillment/Operations/SOPs/public-copy-guardrails.md`) is **not in this repo**,
   and the local `/terms/` page documents a *different* remedy structure. So the 10-13 pass
   asserted **no remedy at all**: every migrated instance now reads "100 exclusive sales
   appointment opportunities in 100 days or less, guaranteed in writing" with the remedy
   pointed to the published terms. That matches the formulation already live on the two
   most recently built pages and introduces no new dollar figure. **Do not broadcast a cash
   figure across 41 files until Spencer confirms it against the SOP.**
2. **Two files are a copy rewrite, not a find-and-replace.**
   `/learn/contractor-appointment-guarantees-explained/` argues the three-part remedy as its
   substance, and `/terms/` is legal copy. Neither was touched.
   `/learn/deck-builder-marketing-companies-compared/` is a third exclusion for a different
   reason: it uses the words "refund" and "money-back" to describe **rivals'** published
   guarantees and rival price points, which is accurate comparison content, but it means the
   builder's banned-term grep fires on the file and it cannot be edited under the current
   verification rule. **The kw3 anchor was hosted on `/learn/best-marketing-agency-for-deck-builders/`
   instead for exactly this reason.** If that page ever needs an edit, the grep rule needs a
   rival-quotation carve-out first.

## Next run

1. **Do not re-run this as a project.** Confirm the table with the two scripts below; it
   should come back 11/12 at one anchor each. If it does, the audit is closed.
2. Raise `deck builder advertising` (#6) with the strategist as a new-page item. It is the
   last core keyword with no MJC surface.
3. Leave keywords 10 and 12's owners alone until the do-not-touch order on
   `/learn/deck-builder-lead-generation/` has expired, then decide whether to add phrase 10.
4. The guarantee sweep stays blocked on Spencer. When he confirms the wording, sweep the
   remaining 41 files in **one pass**, and handle the two rewrite files by hand.
5. Watch keyword 1: if the pillar is still not the ranking URL on the next two scoreboards,
   it is a title decision, not an anchor decision (note A).

## Method

Reproduce with the two scripts the 2026-10-12 and 2026-10-13 runs used (kept out of the repo
deliberately; they are ~40 lines each and re-derivable from this spec):

- **anchor inventory** — walk every `*.html` outside `_archive/`, `v2/`, `scripts/` and
  `assets/`, extract every `<a>` with an internal `href`, strip tags from the inner HTML,
  unescape entities, normalise whitespace and punctuation, lowercase, then count anchors
  whose normalised text equals a core keyword exactly, grouped by target.
  2026-10-13: 1,864 internal anchors across 78 files.
- **owner check** — for each nominated owner, test the exact phrase against `<title>`,
  `<meta name="description">`, `<h1>`, every `<h2>`, and the page's raw HTML.

`CORE` is the authoritative list in `scripts/rank_tracker.py` (do not edit that file).
