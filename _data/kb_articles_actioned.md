# KB articles — Phase 1 actionable backlog

Generated from `_data/kb_articles.csv` on **2026-06-16 23:46 UTC**.

These rows passed Phase 1 and resolve to an on-disk `_docs/...` file. Work queue for Phase 2 — not CSV `actioned` status.

**Totals:** **2** actionable rows (of 3).
**Reference-repo verification:** **2** row(s) have `conflict_resolution` = `inconclusive` — confirm behavior in reference repos (see `.github/skills/salesforce-migration/SKILL.md` Phase 2) before drafting; do not copy Salesforce Knowledge text without source verification.

## 1. Phase 2 PR batches (one primary `_docs` file per PR)

Open **one PR per row** in the table below. Each PR edits **only** that file; multiple Salesforce Knowledge articles may land in the same PR when they share the same `doc_path`.

Do **not** batch PRs by product vertical — mixed verticals under one path are expected (for example, mis-routed paths). Use **Suggested reviewer vertical** and `.github/support_analyzer_doc_assignees.csv` from the file path for `--assignee` only.

**Open PRs:** **2** (one per primary doc).

| Primary `_docs` target | Articles | Suggested reviewer vertical | Suggested branch slug | Product owner |
| --- | ---: | --- | --- | --- |
| `_docs/_user_guide/audience/segments/regex.md` | 1 | Audience & segments | `sf-cursor-segments-regex-<YYYYMMDD>` |  |
| `_docs/_user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps.md` | 1 | Email | `sf-cursor-email-setup-deliverability-pitfalls-and-spam-traps-<YYYYMMDD>` |  |

### PR batch: `_docs/_user_guide/audience/segments/regex.md` — **1** article(s)

- **Branch example:** `sf-cursor-segments-regex-<YYYYMMDD>`
- **Reviewer hint:** Audience & segments

- **`ka0VP000000OmgDYAS`** — Custom Event Properties Regex (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps.md` — **1** article(s)

- **Branch example:** `sf-cursor-email-setup-deliverability-pitfalls-and-spam-traps-<YYYYMMDD>`
- **Reviewer hint:** Email

- **`ka0VP000000TCnNYAW`** — What does Braze need to do to help set up BIMI(Brand Indicators for Messaging Identification)? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
