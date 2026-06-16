# KB articles — Phase 1 actionable backlog

Generated from `_data/kb_articles.csv` on **2026-06-16 21:55 UTC**.

These rows passed Phase 1 and resolve to an on-disk `_docs/...` file. Work queue for Phase 2 — not CSV `actioned` status.

**Totals:** **13** actionable rows (of 14).
**Reference-repo verification:** **13** row(s) have `conflict_resolution` = `inconclusive` — confirm behavior in reference repos (see `.github/skills/salesforce-migration/SKILL.md` Phase 2) before drafting; do not copy Salesforce Knowledge text without source verification.

## 1. Phase 2 PR batches (one primary `_docs` file per PR)

Open **one PR per row** in the table below. Each PR edits **only** that file; multiple Salesforce Knowledge articles may land in the same PR when they share the same `doc_path`.

Do **not** batch PRs by product vertical — mixed verticals under one path are expected (for example, mis-routed paths). Use **Suggested reviewer vertical** and `.github/support_analyzer_doc_assignees.csv` from the file path for `--assignee` only.

**Open PRs:** **13** (one per primary doc).

| Primary `_docs` target | Articles | Suggested reviewer vertical | Suggested branch slug | Product owner |
| --- | ---: | --- | --- | --- |
| `_docs/_user_guide/analytics/dashboards/home.md` | 1 | Analytics | `sf-cursor-dashboards-home-<YYYYMMDD>` |  |
| `_docs/_user_guide/analytics/reports/report_builder.md` | 1 | Analytics | `sf-cursor-reports-report-builder-<YYYYMMDD>` |  |
| `_docs/_user_guide/audience/manage_audience/import_users/csv_import.md` | 1 | Audience & segments | `sf-cursor-import-users-csv-import-<YYYYMMDD>` |  |
| `_docs/_user_guide/audience/segments/regex.md` | 1 | Audience & segments | `sf-cursor-segments-regex-<YYYYMMDD>` |  |
| `_docs/_user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps.md` | 1 | Email | `sf-cursor-email-setup-deliverability-pitfalls-and-spam-traps-<YYYYMMDD>` |  |
| `_docs/_user_guide/data/activation/attributes/custom_attributes.md` | 1 | Data platform | `sf-cursor-attributes-custom-attributes-<YYYYMMDD>` |  |
| `_docs/_user_guide/data/activation/attributes/nested_custom_attribute_support.md` | 1 | Data platform | `sf-cursor-attributes-nested-custom-attribute-support-<YYYYMMDD>` |  |
| `_docs/_user_guide/data/distribution/export_braze_data/segment_data_to_csv.md` | 1 | Data platform | `sf-cursor-export-braze-data-segment-data-to-csv-<YYYYMMDD>` |  |
| `_docs/_user_guide/messaging/canvas/create_a_canvas.md` | 1 | Canvas | `sf-cursor-canvas-create-a-canvas-<YYYYMMDD>` |  |
| `_docs/_user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics.md` | 1 | Canvas | `sf-cursor-testing-canvases-measuring-and-testing-with-canvas-analytics-<YYYYMMDD>` |  |
| `_docs/_user_guide/messaging/design_and_edit/personalize/sources/promotion_codes.md` | 1 | Messaging & automation (Campaigns / Canvas-adjacent) | `sf-cursor-sources-promotion-codes-<YYYYMMDD>` |  |
| `_docs/_user_guide/messaging/messaging_fundamentals/conversion_events.md` | 1 | Messaging & automation (Campaigns / Canvas-adjacent) | `sf-cursor-messaging-fundamentals-conversion-events-<YYYYMMDD>` |  |
| `_docs/_user_guide/messaging/messaging_fundamentals/frequency_capping.md` | 1 | Messaging & automation (Campaigns / Canvas-adjacent) | `sf-cursor-messaging-fundamentals-frequency-capping-<YYYYMMDD>` |  |

### PR batch: `_docs/_user_guide/analytics/dashboards/home.md` — **1** article(s)

- **Branch example:** `sf-cursor-dashboards-home-<YYYYMMDD>`
- **Reviewer hint:** Analytics

- **`ka0VP000000LJfZYAW`** — Onboarding Campaigns -  1st Session Based on "Session Start" (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/analytics/reports/report_builder.md` — **1** article(s)

- **Branch example:** `sf-cursor-reports-report-builder-<YYYYMMDD>`
- **Reviewer hint:** Analytics

- **`ka0VP000000S9I5YAK`** — My Engagement Report/Report Builder Download link has expired. (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/audience/manage_audience/import_users/csv_import.md` — **1** article(s)

- **Branch example:** `sf-cursor-import-users-csv-import-<YYYYMMDD>`
- **Reviewer hint:** Audience & segments

- **`ka0VP000000RWTdYAO`** — Successful Response From /users/delete or users/merge Endpoint But The User Is Not Deleted In Braze (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/audience/segments/regex.md` — **1** article(s)

- **Branch example:** `sf-cursor-segments-regex-<YYYYMMDD>`
- **Reviewer hint:** Audience & segments

- **`ka0VP000000OmgDYAS`** — Custom Event Properties Regex (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps.md` — **1** article(s)

- **Branch example:** `sf-cursor-email-setup-deliverability-pitfalls-and-spam-traps-<YYYYMMDD>`
- **Reviewer hint:** Email

- **`ka0VP000000TCnNYAW`** — What does Braze need to do to help set up BIMI(Brand Indicators for Messaging Identification)? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/data/activation/attributes/custom_attributes.md` — **1** article(s)

- **Branch example:** `sf-cursor-attributes-custom-attributes-<YYYYMMDD>`
- **Reviewer hint:** Data platform

- **`ka0VP000000TlYDYA0`** — Setting Custom Attribute as "" (blank) vs. null (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/data/activation/attributes/nested_custom_attribute_support.md` — **1** article(s)

- **Branch example:** `sf-cursor-attributes-nested-custom-attribute-support-<YYYYMMDD>`
- **Reviewer hint:** Data platform

- **`ka0VP000000Q6D3YAK`** — Testing Nested Custom Attributes and Nested Objects for Custom Event Properties (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/data/distribution/export_braze_data/segment_data_to_csv.md` — **1** article(s)

- **Branch example:** `sf-cursor-export-braze-data-segment-data-to-csv-<YYYYMMDD>`
- **Reviewer hint:** Data platform

- **`ka0VP000000Lt9ZYAS`** — How to Identify and Export Users Who Performed a Specific Custom Event? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/messaging/canvas/create_a_canvas.md` — **1** article(s)

- **Branch example:** `sf-cursor-canvas-create-a-canvas-<YYYYMMDD>`
- **Reviewer hint:** Canvas

- **`ka0VP000000GxqXYAS`** — Is Random Variant Assignment Based on a User's Random Bucket number? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics.md` — **1** article(s)

- **Branch example:** `sf-cursor-testing-canvases-measuring-and-testing-with-canvas-analytics-<YYYYMMDD>`
- **Reviewer hint:** Canvas

- **`ka0VP000000RL3ZYAW`** — Why Is Segment Size Smaller Than Canvas Analytics (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/messaging/design_and_edit/personalize/sources/promotion_codes.md` — **1** article(s)

- **Branch example:** `sf-cursor-sources-promotion-codes-<YYYYMMDD>`
- **Reviewer hint:** Messaging & automation (Campaigns / Canvas-adjacent)

- **`ka0VP000000TJX7YAO`** — Help! I accidentally uploaded the wrong CSV to import some promo codes, and I clicked "Save List" (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/messaging/messaging_fundamentals/conversion_events.md` — **1** article(s)

- **Branch example:** `sf-cursor-messaging-fundamentals-conversion-events-<YYYYMMDD>`
- **Reviewer hint:** Messaging & automation (Campaigns / Canvas-adjacent)

- **`ka0VP000000OOE5YAO`** — Why the Canvas Steps Conversion Rate does not equal the Canvas Variant Total Conversion Rate? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/messaging/messaging_fundamentals/frequency_capping.md` — **1** article(s)

- **Branch example:** `sf-cursor-messaging-fundamentals-frequency-capping-<YYYYMMDD>`
- **Reviewer hint:** Messaging & automation (Campaigns / Canvas-adjacent)

- **`ka0VP000000JYHJYA4`** — Would User Exit Canvas If Message is Aborted? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
