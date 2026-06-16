# KB articles — Phase 1 skipped rows

Generated from `_data/kb_articles.csv` on **2026-06-16 21:55 UTC**.

**Do not hand-edit this file** — it is overwritten by `python3 scripts/salesforce-analyzer/generate_kb_phase1_outputs.py` (repo root). Update the CSV (or epic ID list), then re-run that script; the companion `_data/kb_articles_actioned.md` file is refreshed in the same run.

Rows listed here **did not** pass Phase 1 gates (see `.github/skills/salesforce-migration/SKILL.md`). Actionable queue: `_data/kb_articles_actioned.md`. IDs in `_data/kb_epic_bd6308.txt` are excluded as in-flight BD-6308 work.

**Totals:** 14 CSV rows — **13 actionable**, **1 skipped**.

**Largest skip buckets** (each bullet matches a `##` section below):

- **1** — conflict_resolution signals manual skip (`human review`).

## conflict_resolution signals manual skip (`human review`).

**Count:** 1

- **`ka0VP000000OgMHYA0`** — When is a user's account flagged as having uninstalled the app? When are they considered to have installed the app?
  - *Explanation:* `conflict_resolution` (raw): codebase inconclusive. flag for human review.
