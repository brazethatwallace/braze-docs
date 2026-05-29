# KB articles — Phase 1 skipped rows

Generated from `_data/kb_articles.csv` on **2026-05-29 16:28 UTC**.

**Do not hand-edit this file** — it is overwritten by `python3 scripts/salesforce-analyzer/generate_kb_phase1_outputs.py` (repo root). Update the CSV (or epic ID list), then re-run that script; the companion `_data/kb_articles_actioned.md` file is refreshed in the same run.

Rows listed here **did not** pass automated Phase 1 gates in `.github/skills/salesforce-migration/SKILL.md`. The **actionable** queue (rows that *did* pass) lives in `_data/kb_articles_actioned.md`. Rows skipped only because they appear in `_data/kb_epic_bd6308.txt` would otherwise be actionable — they are excluded so this list does not duplicate Jira Epic **BD-6308** in-flight work. Redundant-with-live-docs, bug-workaround-only, and other **manual** Phase 1 checks are **not** applied here.

**Totals:** 128 CSV rows — **126 actionable**, **2 skipped**.

**Largest skip buckets** (each bullet matches a `##` section below):

- **1** — conflict_resolution signals manual skip (`human review`).
- **1** — conflict_resolution signals manual skip (`no source`).

## conflict_resolution signals manual skip (`human review`).

**Count:** 1

- **`ka0VP000000OgMHYA0`** — When is a user's account flagged as having uninstalled the app? When are they considered to have installed the app?
  - *Explanation:* `conflict_resolution` (raw): codebase inconclusive. flag for human review.

## conflict_resolution signals manual skip (`no source`).

**Count:** 1

- **`ka0VP000000RElFYAW`** — "Connection reset by peer" Error when making calls via API
  - *Explanation:* `conflict_resolution` (raw): no source found
