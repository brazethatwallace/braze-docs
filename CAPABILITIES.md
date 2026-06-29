# Agent capabilities

This file is the authoritative reference for every agent skill in this repo. Skills are reusable, documented workflows that tell an AI agent (Cursor or Claude Code) how to handle a specific documentation task.

Skill source files: [`.github/skills/`](.github/skills/)

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
| [`create-pr`](.github/skills/create-pr/SKILL.md) | Draft pull request workflow with repo-aligned descriptions, pre-PR gates, and manual verification checklists | Opening any PR to `develop`; submitting a branch for review after docs or site edits | `/create-pr` | `Skill("anthropic-skills:create-pr")` |
| [`docs-discrepancies`](.github/skills/docs-discrepancies/SKILL.md) | Audits a documentation page against platform source code, surfaces gaps, and opens a corrective PR | Verifying a page's accuracy against product behavior; cross-referencing docs with source code | `/docs-discrepancies` | `Skill("anthropic-skills:docs-discrepancies")` |
| [`image-pruner`](.github/skills/image-pruner/SKILL.md) | Finds image files under `assets/img/` that are not referenced in docs, includes, or site chrome, then removes them | Cleaning up stale screenshots; reducing repo size; processing CI image-pruner draft PRs | `/image-pruner` | `Skill("anthropic-skills:image-pruner")` |
| [`redirect-management`](.github/skills/redirect-management/SKILL.md) | Adds, updates, and validates URL redirects in `broken_redirect_list.js` when pages are renamed, moved, or deleted | Adding redirects for renamed pages; collapsing stale redirect chains; verifying redirects before a PR | `/redirect-management` | `Skill("anthropic-skills:redirect-management")` |
| [`reference-repos`](.github/skills/reference-repos/SKILL.md) | Looks up product, SDK, and API behavior in sibling source repos as a ground-truth source for docs verification | Confirming product or SDK behavior; documenting API limits; cross-referencing a doc claim with code | `/reference-repos` | `Skill("anthropic-skills:reference-repos")` |
| [`salesforce-migration`](.github/skills/salesforce-migration/SKILL.md) | Migrates Salesforce Knowledge Base articles into public Braze docs (Epic BD-6308), handling triage, drafting, and PRs | Working a Salesforce KB migration Jira ticket; processing `_data/sf_*.xml` or `kb_articles.csv` | `/salesforce-migration` | `Skill("anthropic-skills:salesforce-migration")` |
| [`screenshot-pii-audit`](.github/skills/screenshot-pii-audit/SKILL.md) | OCR-scans changed screenshots for PII (emails, IDs, names, production data) before a PR is opened | Before opening a PR with new or updated screenshots under `assets/img/`; after a CI PII failure | `/screenshot-pii-audit` | `Skill("anthropic-skills:screenshot-pii-audit")` |
| [`support-analyzer`](.github/skills/support-analyzer/SKILL.md) | Triages Braze support case CSVs to find documentation gaps and drafts targeted `_docs` updates | Analyzing support tickets; processing Looker exports on `support-analyzer-data`; drafting docs from support themes | `/support-analyzer` | `Skill("anthropic-skills:support-analyzer")` |
| [`tam-solutions`](.github/skills/tam-solutions/SKILL.md) | Converts internal TAM solution assets into generalized, PII-free example library articles under `_docs/_user_guide/example_library/` | Publishing an internal TAM solution as a public User Guide example; building the Operator Example library | `/tam-solutions` | `Skill("anthropic-skills:tam-solutions")` |

---

## Choosing a skill

| Task | Skill |
|------|-------|
| Writing or editing a `_docs/` article | `braze-docs` |
| Fixing broken links in prose or cross-references | `braze-docs` |
| Adding, updating, or validating redirects in `broken_redirect_list.js` | `redirect-management` |
| Resolving merge conflicts in a docs branch | `braze-docs` |
| Checking for WCAG 2.2 accessibility issues before a PR | `check-accessibility` |
| Opening a draft pull request after finishing a branch | `create-pr` |
| Verifying a page's claims against platform source code | `docs-discrepancies` |
| Confirming SDK, API, or product behavior from source | `reference-repos` |
| Removing unused images from `assets/img/` | `image-pruner` |
| Working a Salesforce KB → public docs migration ticket | `salesforce-migration` |
| Auditing screenshots for PII before opening a PR | `screenshot-pii-audit` |
| Turning support ticket themes into doc improvements | `support-analyzer` |
| Publishing an internal TAM solution as a public example | `tam-solutions` |
