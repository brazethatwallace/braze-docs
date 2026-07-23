# Braze Docs — agent guidance

English canonical documentation lives under `_docs/` and root `_includes/`. Do not edit `_lang/` unless the user explicitly requests locale work.

## Canonical style guide

Human source of truth: [`docs/contributing/style_guide/`](docs/contributing/style_guide/) (start at [`style_guide.md`](docs/contributing/style_guide.md)).

## Skills (`.github/skills/`)

For the full reference — descriptions, when-to-use guidance, and invocation syntax for both Cursor and Claude Code — see **[CAPABILITIES.md](CAPABILITIES.md)**.

| Skill | When to use |
|-------|-------------|
| [`braze-docs`](.github/skills/braze-docs/SKILL.md) | Drafting, editing, reviewing docs; broken links; merge conflicts |
| [`check-accessibility`](.github/skills/check-accessibility/SKILL.md) | Pre-PR WCAG 2.2 AA gate for docs and site files |
| [`create-pr`](.github/skills/create-pr/SKILL.md) | Opening draft pull requests with repo-aligned descriptions and pre-PR gates |
| [`currents-glossary`](.github/skills/currents-glossary/SKILL.md) | Editing the generated Currents event glossary pages, the Currents changelog, or `currents_events.yml` |
| [`redirect-management`](.github/skills/redirect-management/SKILL.md) | Adding, updating, and validating redirects in `broken_redirect_list.js` |
| [`reference-repos`](.github/skills/reference-repos/SKILL.md) | Verifying product, API, or SDK behavior against source repos |
| [`docs-discrepancies`](.github/skills/docs-discrepancies/SKILL.md) | Page-by-page doc vs platform audits and discrepancy PRs |
| [`support-analyzer`](.github/skills/support-analyzer/SKILL.md) | Manual triage of support case CSVs (after CI digest / Phase 2) |
| [`salesforce-migration`](.github/skills/salesforce-migration/SKILL.md) | Jira SF KB migration tickets and `_data/sf_*.xml` / CSV workflows |
| [`image-pruner`](.github/skills/image-pruner/SKILL.md) | Finding and removing unreferenced `assets/img/` files (all locales) |
| [`image-curator`](.github/skills/image-curator/SKILL.md) | Redundant reference removal from English docs (delete-image-only by default); optional manual prose edits via alt merge gate; dereferenced binary cleanup |
| [`screenshot-pii-audit`](.github/skills/screenshot-pii-audit/SKILL.md) | OCR audit of screenshots for PII before PRs; CI blocking check |
| [`spell-check`](.github/skills/spell-check/SKILL.md) | Pre-PR cspell gate for changed `_docs/` and `_includes/` markdown |
| [`snippet-pii`](scripts/check_snippet_pii.py) | Advisory fenced-code-block PII scan for `_docs/` and `_includes/` (see `check-snippet-pii.yml`) |
| [`tam-solutions`](.github/skills/tam-solutions/SKILL.md) | Converting TAM solution assets into public User Guide example articles |

## How to invoke (Cursor)

- **Routine `_docs/` edits:** Describe the task; no tag required. The repo bootstrap rule points agents at `braze-docs`.
- **Verification:** Invoke **`/reference-repos`** from chat, or ask to “verify against source.” Open [`braze-workspace.code-workspace`](braze-workspace.code-workspace) so `platform` and SDK repos are sibling folders.
- **Heavy workflows:** Invoke from chat once (for example `/redirect-management`, `/support-analyzer`, `/salesforce-migration`, `/docs-discrepancies`, `image-curator`, `/image-pruner`, `/screenshot-pii-audit`, `/spell-check`, `/create-pr`).

Inside `SKILL.md` files and agent rules, cross-reference other skills with `braze-docs:skill-name` or relative links — not `@` or `/`. See [CAPABILITIES.md](CAPABILITIES.md#cross-referencing-skills-in-instructions).

## Privacy

Do not include customer names, company names, email addresses, or other PII from support tickets or Slack in public output.

## Support analyzer (CI)

Twice-weekly GitHub Actions exports Looker cases, publishes a digest, and may open Phase 2 draft PRs via [`.github/support_analyzer_phase2_rules.yml`](.github/support_analyzer_phase2_rules.yml). CSV on branch `support-analyzer-data`: `_data/support_cases_latest.csv`. Manual triage uses the **support-analyzer** skill; CI does not run skills directly.

## Image pruner (CI)

Twice-yearly GitHub Actions (June 1 and December 1) scans `develop` for unreferenced `assets/img/` files via [`.github/workflows/image-pruner-maintenance.yml`](.github/workflows/image-pruner-maintenance.yml). Each run deletes up to 100 candidates (secondary verify, open-PR exclusions) and opens a **draft** `[IP]` pull request when at least one file is removed. Extra batches use the [image-pruner](.github/skills/image-pruner/SKILL.md) skill (`/image-pruner` from chat).

## Image curator (CI)

Twice-yearly GitHub Actions (June 1 and December 1, 14:00 ET) scans English docs for redundant image references via [`.github/workflows/image-curator-maintenance.yml`](.github/workflows/image-curator-maintenance.yml). Each run removes up to 15 high-confidence references (delete-image-only, dereferenced binary delete) and opens a **draft** `[IC]` pull request labeled `image pruning`. Manual vision review and medium-confidence batches use the [image-curator](.github/skills/image-curator/SKILL.md) skill (`/image-curator` from chat).

## Translation glossaries (Phrase)

`scripts/glossaries/*.json` are synced from Phrase TMS term bases (`scripts/sync_glossaries_from_phrase.py`). See [`scripts/glossaries/README.md`](scripts/glossaries/README.md). CI: [`.github/workflows/sync-glossaries-from-phrase.yml`](.github/workflows/sync-glossaries-from-phrase.yml) (requires `PHRASE_TMS_TOKEN` secret). Weekly drift vs platform/SDK repos: [`.github/workflows/audit-glossaries.yml`](.github/workflows/audit-glossaries.yml) (report only).

## Cursor rules (always on)

- [`.cursor/rules/privacy-and-security.mdc`](.cursor/rules/privacy-and-security.mdc)
- [`.cursor/rules/braze-docs-bootstrap.mdc`](.cursor/rules/braze-docs-bootstrap.mdc)
