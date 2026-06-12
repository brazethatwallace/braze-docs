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

## How to invoke (Cursor)

- **Routine `_docs/` edits:** Describe the task; no tag required. The repo bootstrap rule points agents at `braze-docs`.
- **Verification:** Use **`@reference-repos`** or ask to “verify against source.” Open [`braze-workspace.code-workspace`](braze-workspace.code-workspace) so `platform` and SDK repos are sibling folders.
- **Heavy workflows:** Name the skill once (for example `@support-analyzer`, `@salesforce-migration`, `@docs-discrepancies`, `@image-pruner`).

## Privacy

Do not include customer names, company names, email addresses, or other PII from support tickets or Slack in public output.

## Support analyzer (CI)

Twice-weekly GitHub Actions exports Looker cases, publishes a digest, and may open Phase 2 draft PRs via [`.github/support_analyzer_phase2_rules.yml`](.github/support_analyzer_phase2_rules.yml). CSV on branch `support-analyzer-data`: `_data/support_cases_latest.csv`. Manual triage uses the **support-analyzer** skill; CI does not run skills directly.

## Cursor rules (always on)

- [`.cursor/rules/privacy-and-security.mdc`](.cursor/rules/privacy-and-security.mdc)
- [`.cursor/rules/braze-docs-bootstrap.mdc`](.cursor/rules/braze-docs-bootstrap.mdc)
