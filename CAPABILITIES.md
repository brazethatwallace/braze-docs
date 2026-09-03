# Agent capabilities

This file is the authoritative reference for every agent skill in this repo. Skills are reusable, documented workflows that tell an AI agent (Cursor or Claude Code) how to handle a specific documentation task.

Skill source files: [`.github/skills/`](.github/skills/)

Cursor and Claude Code also discover skills through symlinks in [`.cursor/skills/`](.cursor/skills/) and [`.claude/skills/`](.claude/skills/) (each points at the matching folder under `.github/skills/`). When you add a new skill, update those symlink directories alongside the registry tables below.

---

## How to invoke

| Tool | Method |
|------|--------|
| **Cursor** | Type `/skill-name` in the chat (for example, `/image-pruner`). For routine `_docs/` edits, describe the task — no tag needed; the bootstrap rule routes to `braze-docs` automatically. |
| **Claude Code** | Use the `Skill` tool and pass the skill name: `Skill("anthropic-skills:skill-name")`. For routine `_docs/` edits, describing the task is enough — `braze-docs` loads automatically. |

### Cross-referencing skills in instructions

| Context | Syntax |
|---------|--------|
| **Contributor chat (Cursor)** | `/skill-name` — UI command for humans only |
| **Inside `SKILL.md` or agent rules** | `braze-docs:skill-name` with **REQUIRED SUB-SKILL:** markers, or a relative link to a sibling [`SKILL.md`](.github/skills/braze-docs/SKILL.md) |
| **Do not use in skill instructions** | `@skill-name` (force-loads context) or `/skill-name` (chat UI syntax) |

---

## Skills

| Skill | Description | When to use | Cursor | Claude Code |
|-------|-------------|-------------|--------|-------------|
| [`braze-docs`](.github/skills/braze-docs/SKILL.md) | Applies Braze writing style, site conventions, link rules, and Liquid formatting to documentation edits | Drafting or editing articles under `_docs/`; fixing broken links; resolving merge conflicts; reviewing for style | Describe the task (no tag needed), or `/braze-docs` | `Skill("anthropic-skills:braze-docs")` |
| [`check-accessibility`](.github/skills/check-accessibility/SKILL.md) | Pre-PR WCAG 2.2 AA gate that audits changed markdown and site files for accessibility issues | Before opening any PR that touches docs or site files; when asked to run an a11y or WCAG check | `/check-accessibility` | `Skill("anthropic-skills:check-accessibility")` |
| [`create-pr`](.github/skills/create-pr/SKILL.md) | Draft pull request workflow with repo-aligned descriptions, pre-PR gates (accessibility, spell-check, Style QA, PII), and manual verification checklists | Opening any PR to `develop`; submitting a branch for review after docs or site edits | `/create-pr` | `Skill("anthropic-skills:create-pr")` |
| [`currents-glossary`](.github/skills/currents-glossary/SKILL.md) | Guides edits to the generated Currents event glossary pages and changelog: which layer owns each part, `currents_events.yml` syntax, and the dual write that survives regeneration | Editing any `event_glossary/` page or `scripts/resources/currents_events.yml`; adding property details, callouts, or API tags to a Currents event; reporting a wrong event field or schema | `/currents-glossary` | `Skill("anthropic-skills:currents-glossary")` |
| [`docs-discrepancies`](.github/skills/docs-discrepancies/SKILL.md) | Audits a documentation page against platform source code, surfaces gaps, and opens a corrective PR | Verifying a page's accuracy against product behavior; cross-referencing docs with source code | `/docs-discrepancies` | `Skill("anthropic-skills:docs-discrepancies")` |
| [`image-curator`](.github/skills/image-curator/SKILL.md) | Finds redundant image references still in English docs (`_docs/`, `_includes/`), removes references (delete-image-only by default), and deletes dereferenced binaries when safe | Removing low-value screenshots (Save buttons, home pages, full dashboards); processing CI image-curator draft PRs; vision review of medium-confidence candidates | `/image-curator` | `Skill("anthropic-skills:image-curator")` |
| [`image-pruner`](.github/skills/image-pruner/SKILL.md) | Finds image files under `assets/img/` that are not referenced in docs, includes, or site chrome, then removes them | Cleaning up stale screenshots; reducing repo size; processing CI image-pruner draft PRs | `/image-pruner` | `Skill("anthropic-skills:image-pruner")` |
| [`find-ux-debt`](.github/skills/find-ux-debt/SKILL.md) | Scans Braze platform UI files for 8 detectable copy problem types, grouped into Tier 1 (factual issues — file as UX Debt) and Tier 2 (style/judgment — routed to UXW). Offers to log a consolidated UXW story for Tier 2 findings. Two checks require the braze-ux-writing plugin. | After `reference-repos` surfaces a UI component file; any time you want to audit platform copy before filing UX Debt tickets | `/find-ux-debt` | `Skill("anthropic-skills:find-ux-debt")` |
| [`log-ux-debt`](.github/skills/log-ux-debt/SKILL.md) | Logs a UX Debt Jira ticket when a UI label, tooltip, or permission name in platform source does not match the documented copy — handles CODEOWNERS lookup, duplicate detection, and ticket creation with acceptance criteria | When `reference-repos`, `find-ux-debt`, or `docs-discrepancies` surfaces a factual copy inconsistency and you want to file it with the owning team | `/log-ux-debt` | `Skill("anthropic-skills:log-ux-debt")` |
| [`redirect-management`](.github/skills/redirect-management/SKILL.md) | Adds, updates, and validates URL redirects in `broken_redirect_list.js` when pages are renamed, moved, or deleted | Adding redirects for renamed pages; collapsing stale redirect chains; verifying redirects before a PR | `/redirect-management` | `Skill("anthropic-skills:redirect-management")` |
| [`reference-repos`](.github/skills/reference-repos/SKILL.md) | Looks up product, SDK, and API behavior in sibling source repos as a ground-truth source for docs verification | Confirming product or SDK behavior; documenting API limits; cross-referencing a doc claim with code | `/reference-repos` | `Skill("anthropic-skills:reference-repos")` |
| [`release-deploy`](.github/skills/release-deploy/SKILL.md) | Generates the deploy-PR list for monthly release notes via `scripts/generate_releases_deploy.py`: merged `deploy` PRs since the last `v.*` tag, with contributor PRs nested underneath | Drafting monthly release notes; generating the deploy text | `/release-deploy` | `Skill("anthropic-skills:release-deploy")` |
| [`salesforce-migration`](.github/skills/salesforce-migration/SKILL.md) | Migrates Salesforce Knowledge Base articles into public Braze docs (Epic BD-7051), handling triage, drafting, and PRs | Working a Salesforce KB migration Jira ticket; processing `_data/sf_*.xml` or `kb_articles.csv` | `/salesforce-migration` | `Skill("anthropic-skills:salesforce-migration")` |
| [`screenshot-pii-audit`](.github/skills/screenshot-pii-audit/SKILL.md) | OCR-scans changed screenshots for PII (emails, IDs, names, production data) before a PR is opened | Before opening a PR with new or updated screenshots under `assets/img/`; after a CI PII failure | `/screenshot-pii-audit` | `Skill("anthropic-skills:screenshot-pii-audit")` |
| [`sdk-sync`](.github/skills/sdk-sync/SKILL.md) | Syncs SDK repository guide pages by running `scripts/sync_sdk_repository_guides.py`, then validates idempotent output and generated-page changes | Running or reviewing SDK repository guide syncs; reproducing CI sync output locally; verifying completion criteria after sync | `/sdk-sync` | `Skill("anthropic-skills:sdk-sync")` |
| [`slack-to-docs`](.github/skills/slack-to-docs/SKILL.md) | Mines SME or support Slack channels for doc gaps, verifies each theme with `reference-repos` (proof in the overview **Verified?** column), deduplicates against open and pending PRs, and opens manageable draft PRs with thread citations | Pointed at a Slack channel to turn recurring SME threads into docs updates; reproducing the WhatsApp pilot workflow | `/slack-to-docs` | `Skill("anthropic-skills:slack-to-docs")` |
| [`spell-check`](.github/skills/spell-check/SKILL.md) | Runs cspell on changed `_docs/` and `_includes/` markdown; auto-fixes very high-confidence typos; flags ambiguous terms for review | Before opening a PR that changes English docs prose; when CI Spellcheck fails; `/spell-check` | `/spell-check` | `Skill("anthropic-skills:spell-check")` |
| [`support-analyzer`](.github/skills/support-analyzer/SKILL.md) | Triages Braze support case CSVs to find documentation gaps and drafts targeted `_docs` updates | Analyzing support tickets; processing Looker exports on `support-analyzer-data`; drafting docs from support themes | `/support-analyzer` | `Skill("anthropic-skills:support-analyzer")` |
| [`tam-solutions`](.github/skills/tam-solutions/SKILL.md) | Converts internal TAM solution assets into generalized, PII-free example library articles under `_docs/_user_guide/example_library/` | Publishing an internal TAM solution as a public User Guide example; building the Operator Example library | `/tam-solutions` | `Skill("anthropic-skills:tam-solutions")` |
| [`audit-page-seo`](.github/skills/audit-page-seo/SKILL.md) | Ranks `_docs/` pages by SEO/AEO headroom, generates verified link fix tables with section context, and produces per-page recommendation packets (no-approval vs approval-needed tiers) | Running the in-house SEO pilot; page-level title/meta/FAQ/link recommendations | `/audit-page-seo` | `Skill("anthropic-skills:audit-page-seo")` |

---

## Choosing a skill

| Task | Skill |
|------|-------|
| Writing or editing a `_docs/` article | `braze-docs` |
| Fixing broken links in prose or cross-references | `braze-docs` |
| Adding, updating, or validating redirects in `broken_redirect_list.js` | `redirect-management` |
| Resolving merge conflicts in a docs branch | `braze-docs` |
| Editing a Currents event glossary page, the Currents changelog, or `currents_events.yml` | `currents-glossary` |
| Checking for WCAG 2.2 accessibility issues before a PR | `check-accessibility` |
| Opening a draft pull request after finishing a branch | `create-pr` |
| Verifying a page's claims against platform source code | `docs-discrepancies` |
| Scanning a platform UI file for copy problems before filing tickets | `find-ux-debt` |
| Filing a UX Debt Jira ticket for a factual copy inconsistency found in platform source | `log-ux-debt` |
| Confirming SDK, API, or product behavior from source | `reference-repos` |
| Generating the deploy-PR text for monthly release notes | `release-deploy` |
| Removing redundant referenced images from English docs | `image-curator` |
| Removing unused images from `assets/img/` | `image-pruner` |
| Working a Salesforce KB → public docs migration ticket | `salesforce-migration` |
| Auditing screenshots for PII before opening a PR | `screenshot-pii-audit` |
| Running or validating SDK repository guide sync | `sdk-sync` |
| Mining SME Slack channels for source-verified doc PRs | `slack-to-docs` |
| Running spell-check on changed docs before a PR | `spell-check` |
| Turning support ticket themes into doc improvements | `support-analyzer` |
| Publishing an internal TAM solution as a public example | `tam-solutions` |
| SEO/AEO page scoring, link fix tables, or pilot recommendations | `audit-page-seo` |
