---
name: salesforce-migration
description: >
  Salesforce KB → Braze docs (Epic BD-6308): Phase 1 triage, Phase 2 PRs, `kb_articles.csv` /
  optional `sf_kb_articles.csv`. Invoke with @salesforce-migration.
---

# Salesforce Knowledge → Braze Docs (Epic BD-6308)

**Invoke:** `@salesforce-migration` · **Verify:** [`reference-repos`](../reference-repos/SKILL.md) · **Prose:** [`docs/contributing/style_guide/`](../../../docs/contributing/style_guide.md)

---

## Data files

| File | Role |
|------|------|
| [`_data/kb_articles.csv`](_data/kb_articles.csv) | Backlog; **`suggested_change`** = strong draft user docs, not shorthand-only triage (Phase 1) |
| [`_data/kb_articles_actioned.md`](_data/kb_articles_actioned.md) | **Generated** — Phase 2 queue by `doc_path` |
| [`_data/kb_articles_skipped.md`](_data/kb_articles_skipped.md) | **Generated** — skipped rows + reasons |
| [`_data/sf_kb_articles.csv`](_data/sf_kb_articles.csv) | Optional — full SF `Resolution` (`encoding='latin-1'`) |

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

## Phase 1: Triage

**`suggested_change`:** Write as **strong draft material** for public docs—full sentences, concrete facts, limits, and steps a customer could follow; say which section to extend when useful. Avoid shorthand-only reminders (use `notes` for author-only context). `sf_kb_phase2_run_batches.py` inserts this field into the target page.

1. Edit [`_data/kb_articles.csv`](_data/kb_articles.csv) as needed.
2. Run `--infer-doc-paths --no-prune` when `doc_path` is missing or wrong, then `--no-prune` to refresh markdown. Prune runs when you omit `--no-prune`. Extend path maps in `generate_kb_phase1_outputs.py` only after you confirm targets; otherwise search `_docs/` (FAQ/troubleshooting first).
3. Work from **`kb_articles_actioned.md` section 1** — one PR per primary `_docs` file.
4. Skipped rows with overlap / “codebase confirms” but no path: fix `doc_path` (or infer), re-run.

**Skip:** workarounds/bugs, `*INTERNAL*` titles, support-only or sensitive content.

**`inconclusive`:** still actionable with a `doc_path` — **verify in reference repos** before Phase 2.

**Paths:** not `_docs/_help/help_articles/` — use `_user_guide/`, `_developer_guide/`, or `_api/`.

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
