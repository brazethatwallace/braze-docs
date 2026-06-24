---
name: salesforce-migration
description: >
  Salesforce KB → Braze docs (Epic BD-6308): Phase 1 script-driven triage, Phase 2 PRs + Jira,
  Phase 3 CSV write-back. `kb_articles.csv` / optional `sf_kb_articles.csv`. Invoke with @salesforce-migration.
---

# Salesforce Knowledge → Braze Docs (Epic BD-6308)

**Invoke:** `@salesforce-migration` · **Verify:** [`reference-repos`](../reference-repos/SKILL.md) · **Prose:** [`docs/contributing/style_guide/`](../../../docs/contributing/style_guide.md)

---

## Data files

| File | Role |
|------|------|
| [`_data/kb_articles.csv`](_data/kb_articles.csv) | Backlog — pass raw to Cursor; do not pre-process or strip columns. **`suggested_change`** = strong draft user docs, not shorthand-only triage (Phase 1) |
| [`_data/kb_articles_actioned.md`](_data/kb_articles_actioned.md) | **Generated** — Phase 2 queue by `doc_path` |
| [`_data/kb_articles_skipped.md`](_data/kb_articles_skipped.md) | **Generated** — skipped rows + reasons |
| [`_data/sf_kb_articles.csv`](_data/sf_kb_articles.csv) | Optional — full SF `Resolution` (`encoding='latin-1'`) |

> **CSV note:** `kb_articles.csv` may have many columns and long cell content. Pass it to Cursor raw — the script handles all column parsing and triage logic. Do not strip columns or summarize content before running Phase 1.

---

## Scripts

Phase 1 **writes** the two markdown files and may edit the CSV. Phase 2 **reads** them. `sf_kb_sync_tracker.py` trims the CSV when run explicitly.

```bash
python3 scripts/salesforce-analyzer/generate_kb_phase1_outputs.py --infer-doc-paths --no-prune
python3 scripts/salesforce-analyzer/generate_kb_phase1_outputs.py --no-prune

python3 scripts/salesforce-analyzer/sf_kb_sync_tracker.py [--dry-run]

python3 scripts/salesforce-analyzer/sf_kb_phase2_run_batches.py [--limit N] [--doc-path '_docs/...']

python3 scripts/salesforce-analyzer/sf_kb_jira_ticket.py --pr-url '...' --pr-title '[BD-####](SF) ...' --doc-path '_docs/...'   # needs JIRA_USER_EMAIL + JIRA_API_TOKEN

python3 scripts/salesforce-analyzer/sf_kb_sync_epic_pr_titles.py [--dry-run]
```

| Script | Purpose |
|--------|---------|
| `generate_kb_phase1_outputs.py` | Phase 1 gates, path inference, actioned/skipped markdown; `--infer-doc-paths` / prune flags |
| `sf_kb_sync_tracker.py` | PR-labeled `article_id`s → drop from CSV → rerun Phase 1 markdown |
| `sf_kb_phase2_run_batches.py` | `gh` (+ optional Jira): pastes full `suggested_change` into `_docs/` (expects strong draft); polish to ship-ready before merge |
| `sf_kb_jira_ticket.py` | BD Task under epic BD-6308 |
| `sf_kb_sync_epic_pr_titles.py` | PR titles → `[BD-####](SF) …` |

---

## Phase 1: Script-driven triage

> **The script is the sole triage authority.** `generate_kb_phase1_outputs.py` applies all classification gates. Your job is to run the script and fix `doc_path` values — not to re-evaluate whether individual rows should be actionable or skipped.

### Skip gates (script decides — do not override)

If the script marks something actionable, accept it and proceed to Phase 2 without second-guessing.

| Gate | Skip condition |
|------|----------------|
| `implementation_status` | First line is `archived` or `actioned`, or any unlisted value |
| `target` | Value is `inconclusive` |
| `conflict_resolution` | Contains `human review`, `no source`, `codebase inconclusive`, or `inconclusive —` |
| `suggested_change` | Empty, whitespace, or first line starts with: `might`, `may`, `consider reviewing`, `review`, `tbd`, `unclear`, `needs investigation`, `needs sme`, `flag for` |
| `_docs/` paths | All extracted paths are under `_docs/_help/help_articles/` |
| `target` + paths | `target` is `knowledge_article` and no `_docs/` path found in any field |
| Path resolution | No on-disk `_docs/...` target found after path extraction, IA remaps, scripted inference, and best-fit placement |

### What you fix (only this)

- `doc_path` is blank or stale but you can identify the correct current path → update the CSV field, then re-run.
- A path failed because it's under an old IA layout (e.g. `engagement_tools/`, `message_building_by_channel/`) → extend `PATH_INFERENCE_EXACT` or `PATH_INFERENCE_PREFIXES` in `generate_kb_phase1_outputs.py` after confirming the mapping.
- A row landed in skipped with reason "no locatable on-disk target" but has a clear `suggested_change` and a valid topic → search `_docs/` for the best-fit page, set `doc_path`, re-run.

**Never manually move rows between the actioned and skipped files.**

### Steps

1. Edit [`_data/kb_articles.csv`](_data/kb_articles.csv) only to fix `doc_path` values.
2. Run `--infer-doc-paths --no-prune` when `doc_path` is missing or wrong, then `--no-prune` to refresh markdown. Omit `--no-prune` to also prune `archived`/`actioned` rows from the CSV. Extend path maps in `generate_kb_phase1_outputs.py` only after you confirm targets; otherwise search `_docs/` (FAQ/troubleshooting first).
3. Inspect `kb_articles_skipped.md` — address only rows where fixing `doc_path` would recover them. Do not override the skip on any other gate.
4. Inspect `kb_articles_actioned.md` section 1 — one PR per primary `_docs` file.

**`inconclusive`:** still actionable with a `doc_path` — **verify in reference repos** before Phase 2.

**Paths:** not `_docs/_help/help_articles/` — use `_user_guide/`, `_developer_guide/`, or `_api/`.

**`suggested_change`:** Write as **strong draft material** for public docs — full sentences, concrete facts, limits, and steps a customer could follow; say which section to extend when useful. Avoid shorthand-only reminders (use `notes` for author-only context). `sf_kb_phase2_run_batches.py` inserts this field into the target page.

---

## Phase 2: Draft + PR

**Scope:** section 1 of `kb_articles_actioned.md` — same `doc_path` → one PR, one primary `_docs` file (`_includes/` only if needed).

1. Read backlog; optional `sf_kb_articles.csv`; redact PII.
2. **Verify** in reference repos (`inconclusive` especially). Prefer platform/source over SF copy.
3. **Polish** bulk inserts and any remaining CSV prose to **ship-ready** user docs (tone, Liquid, heading levels, redundancy). Phase 1 should already have supplied strong draft material in `suggested_change`; this step finishes integration.
4. Branch: `sf-cursor-<slug>-<YYYYMMDD>` (slug in actioned file).
5. PR → `develop`, label **`salesforce migration`**, title **`[BD-####](SF) …`**. Jira: `sf_kb_jira_ticket.py`.
6. Assignee: [`.github/support_analyzer_doc_assignees.csv`](.github/support_analyzer_doc_assignees.csv) (longest path). Bulk runner sets `--assignee` only when it resolves to a GitHub user.
7. Commits: `_docs/` / `_includes/` only — **no** `_data/kb_articles*` in migration PRs.

**PR body:** product vertical · summary · changes (files + verification paths) · `article_id` sources — use `build_sf_kb_github_pr_body()` in `sf_kb_jira_ticket.py`.

**Jira:** one Task per PR under [**BD-6308**](https://jira.atl.braze.com/browse/BD-6308) — PR link, articles, vertical. Summary: `Salesforce KB batch - <theme>`.

---

## Phase 3: CSV write-back (after all PRs)

After Phase 2 is complete for a batch, write the PR and Jira ticket IDs back to `kb_articles.csv`. This lets you export the updated spreadsheet to Google Sheets so stakeholders can locate both actioned and unactionable articles in one place.

### Steps

1. Add columns `jira_ticket_id` and `pr_url` to `kb_articles.csv` if they don't exist yet.
2. For each row that received a PR in this batch, populate:
   - `jira_ticket_id` — the BD ticket key (e.g. `BD-1234`) from `sf_kb_jira_ticket.py` output
   - `pr_url` — the full GitHub PR URL (e.g. `https://github.com/braze-inc/braze-docs/pull/1234`)
3. Set `implementation_status` = `actioned` on those rows.
4. Save the updated `kb_articles.csv`.

**After saving:** Export `kb_articles.csv` to a new sheet in the source Google Spreadsheet. Rows with `jira_ticket_id` and `pr_url` are the actioned articles; rows without are unactionable or pending.

> **Do not run Phase 1 prune** until after write-back is complete and the CSV has been exported — the prune step drops `actioned` rows, removing the write-back data before it can be shared.

---

## Example prompts

```
@salesforce-migration Run Phase 1 (--infer-doc-paths) and summarize the backlog.
```

```
@salesforce-migration Run Phase 2 for `_docs/_user_guide/channels/push/troubleshooting.md`.
```

```
@salesforce-migration Run Phase 2 for the next batch in kb_articles_actioned.md section 1.
```

```
@salesforce-migration Phase 2 is complete. Write back PR URLs and Jira ticket IDs to kb_articles.csv.
```
