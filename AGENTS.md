# Braze Docs — agent guidance

English canonical documentation lives under `_docs/` and root `_includes/`. Do not edit `_lang/` unless the user explicitly requests locale work.

## Canonical style guide

Human source of truth: [`docs/contributing/style_guide/`](docs/contributing/style_guide/) (start at [`style_guide.md`](docs/contributing/style_guide.md)).

## Skills (`.github/skills/`)

| Skill | When to use |
|-------|-------------|
| [`braze-docs`](.github/skills/braze-docs/SKILL.md) | Drafting, editing, reviewing docs; broken links; merge conflicts |
| [`reference-repos`](.github/skills/reference-repos/SKILL.md) | Verifying product, API, or SDK behavior against source repos |
| [`docs-discrepancies`](.github/skills/docs-discrepancies/SKILL.md) | Page-by-page doc vs platform audits and discrepancy PRs |
| [`support-analyzer`](.github/skills/support-analyzer/SKILL.md) | Manual triage of support case CSVs (after CI digest / Phase 2) |
| [`salesforce-migration`](.github/skills/salesforce-migration/SKILL.md) | Jira SF KB migration tickets and `_data/sf_*.xml` / CSV workflows |
| [`image-pruner`](.github/skills/image-pruner/SKILL.md) | Finding and removing unreferenced `assets/img/` files (all locales) |
| [`image-curator`](.github/skills/image-curator/SKILL.md) | Removing redundant referenced images from English docs; prose absorption; dereferenced binary cleanup |
| [`screenshot-pii-audit`](.github/skills/screenshot-pii-audit/SKILL.md) | OCR audit of screenshots for PII before PRs; CI blocking check |

## How to invoke (Cursor)

- **Routine `_docs/` edits:** Describe the task; no tag required. The repo bootstrap rule points agents at `braze-docs`.
- **Verification:** Use **`@reference-repos`** or ask to “verify against source.” Open [`braze-workspace.code-workspace`](braze-workspace.code-workspace) so `platform` and SDK repos are sibling folders.
- **Heavy workflows:** Name the skill once (for example `@support-analyzer`, `@salesforce-migration`, `@docs-discrepancies`, `@image-pruner`, `@image-curator`, `@screenshot-pii-audit`).

## Privacy

Do not include customer names, company names, email addresses, or other PII from support tickets or Slack in public output.

## Support analyzer (CI)

Twice-weekly GitHub Actions exports Looker cases, publishes a digest, and may open Phase 2 draft PRs via [`.github/support_analyzer_phase2_rules.yml`](.github/support_analyzer_phase2_rules.yml). CSV on branch `support-analyzer-data`: `_data/support_cases_latest.csv`. Manual triage uses the **support-analyzer** skill; CI does not run skills directly.

## Image pruner (CI)

Twice-yearly GitHub Actions (June 1 and December 1) scans `develop` for unreferenced `assets/img/` files via [`.github/workflows/image-pruner-maintenance.yml`](.github/workflows/image-pruner-maintenance.yml). Each run deletes up to 100 candidates (secondary verify, open-PR exclusions) and opens a **draft** `[IP]` pull request when at least one file is removed. Extra batches use the **image-pruner** skill or `@image-pruner`.

## Image curator (CI)

Twice-yearly GitHub Actions (June 1 and December 1, 14:00 ET) scans English docs for redundant image references via [`.github/workflows/image-curator-maintenance.yml`](.github/workflows/image-curator-maintenance.yml). Each run removes up to 25 high-confidence references (prose merge, dereferenced binary delete) and opens a **draft** `[IC]` pull request labeled `image pruning`. Manual vision review and medium-confidence batches use the **image-curator** skill or `@image-curator`.

## Cursor rules (always on)

- [`.cursor/rules/privacy-and-security.mdc`](.cursor/rules/privacy-and-security.mdc)
- [`.cursor/rules/braze-docs-bootstrap.mdc`](.cursor/rules/braze-docs-bootstrap.mdc)
