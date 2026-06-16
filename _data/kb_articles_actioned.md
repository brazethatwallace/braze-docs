# KB articles — Phase 1 actionable backlog

Generated from `_data/kb_articles.csv` on **2026-06-16 19:42 UTC**.

These rows passed Phase 1 and resolve to an on-disk `_docs/...` file. Work queue for Phase 2 — not CSV `actioned` status.

**Totals:** **49** actionable rows (of 50).
**Reference-repo verification:** **43** row(s) have `conflict_resolution` = `inconclusive` — confirm behavior in reference repos (see `.github/skills/salesforce-migration/SKILL.md` Phase 2) before drafting; do not copy Salesforce Knowledge text without source verification.

## 1. Phase 2 PR batches (one primary `_docs` file per PR)

Open **one PR per row** in the table below. Each PR edits **only** that file; multiple Salesforce Knowledge articles may land in the same PR when they share the same `doc_path`.

Do **not** batch PRs by product vertical — mixed verticals under one path are expected (for example, mis-routed paths). Use **Suggested reviewer vertical** and `.github/support_analyzer_doc_assignees.csv` from the file path for `--assignee` only.

**Open PRs:** **25** (one per primary doc).

| Primary `_docs` target | Articles | Suggested reviewer vertical | Suggested branch slug | Product owner |
| --- | ---: | --- | --- | --- |
| `_docs/_user_guide/messaging/canvas/faqs.md` | 11 | Canvas | `sf-cursor-canvas-faqs-<YYYYMMDD>` |  |
| `_docs/_user_guide/data/distribution/braze_currents/faq.md` | 7 | Currents | `sf-cursor-braze-currents-faq-<YYYYMMDD>` |  |
| `_docs/_user_guide/channels/push/troubleshooting.md` | 4 | Push | `sf-cursor-push-troubleshooting-<YYYYMMDD>` |  |
| `_docs/_user_guide/administer/global/user_management/permissions.md` | 3 | Dashboard & administration | `sf-cursor-user-management-permissions-<YYYYMMDD>` |  |
| `_docs/_user_guide/channels/email/drag_and_drop/faq.md` | 3 | Email | `sf-cursor-drag-and-drop-faq-<YYYYMMDD>` |  |
| `_docs/_user_guide/channels/email/subscriptions.md` | 2 | Email | `sf-cursor-email-subscriptions-<YYYYMMDD>` |  |
| `_docs/_developer_guide/platforms/web/content_security_policy.md` | 1 | SDK & developer integrations | `sf-cursor-web-content-security-policy-<YYYYMMDD>` |  |
| `_docs/_user_guide/administer/global/workspace_settings/email_preferences.md` | 1 | Dashboard & administration | `sf-cursor-workspace-settings-email-preferences-<YYYYMMDD>` |  |
| `_docs/_user_guide/analytics/dashboards/home.md` | 1 | Analytics | `sf-cursor-dashboards-home-<YYYYMMDD>` |  |
| `_docs/_user_guide/analytics/reports/report_builder.md` | 1 | Analytics | `sf-cursor-reports-report-builder-<YYYYMMDD>` |  |
| `_docs/_user_guide/audience/manage_audience/import_users/csv_import.md` | 1 | Audience & segments | `sf-cursor-import-users-csv-import-<YYYYMMDD>` |  |
| `_docs/_user_guide/audience/segments/regex.md` | 1 | Audience & segments | `sf-cursor-segments-regex-<YYYYMMDD>` |  |
| `_docs/_user_guide/channels/email/email_setup/authentication.md` | 1 | Email | `sf-cursor-email-setup-authentication-<YYYYMMDD>` |  |
| `_docs/_user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps.md` | 1 | Email | `sf-cursor-email-setup-deliverability-pitfalls-and-spam-traps-<YYYYMMDD>` |  |
| `_docs/_user_guide/channels/email/reporting.md` | 1 | Email | `sf-cursor-email-reporting-<YYYYMMDD>` |  |
| `_docs/_user_guide/data/activation/attributes/custom_attributes.md` | 1 | Data platform | `sf-cursor-attributes-custom-attributes-<YYYYMMDD>` |  |
| `_docs/_user_guide/data/activation/attributes/nested_custom_attribute_support.md` | 1 | Data platform | `sf-cursor-attributes-nested-custom-attribute-support-<YYYYMMDD>` |  |
| `_docs/_user_guide/data/distribution/export_braze_data/segment_data_to_csv.md` | 1 | Data platform | `sf-cursor-export-braze-data-segment-data-to-csv-<YYYYMMDD>` |  |
| `_docs/_user_guide/data/infrastructure/data_points.md` | 1 | Data platform | `sf-cursor-infrastructure-data-points-<YYYYMMDD>` |  |
| `_docs/_user_guide/messaging/canvas/create_a_canvas.md` | 1 | Canvas | `sf-cursor-canvas-create-a-canvas-<YYYYMMDD>` |  |
| `_docs/_user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics.md` | 1 | Canvas | `sf-cursor-testing-canvases-measuring-and-testing-with-canvas-analytics-<YYYYMMDD>` |  |
| `_docs/_user_guide/messaging/design_and_edit/personalize/sources/promotion_codes.md` | 1 | Messaging & automation (Campaigns / Canvas-adjacent) | `sf-cursor-sources-promotion-codes-<YYYYMMDD>` |  |
| `_docs/_user_guide/messaging/messaging_fundamentals/conversion_events.md` | 1 | Messaging & automation (Campaigns / Canvas-adjacent) | `sf-cursor-messaging-fundamentals-conversion-events-<YYYYMMDD>` |  |
| `_docs/_user_guide/messaging/messaging_fundamentals/frequency_capping.md` | 1 | Messaging & automation (Campaigns / Canvas-adjacent) | `sf-cursor-messaging-fundamentals-frequency-capping-<YYYYMMDD>` |  |
| `_docs/_user_guide/messaging/messaging_fundamentals/sending_test_messages.md` | 1 | Messaging & automation (Campaigns / Canvas-adjacent) | `sf-cursor-messaging-fundamentals-sending-test-messages-<YYYYMMDD>` |  |

### PR batch: `_docs/_user_guide/messaging/canvas/faqs.md` — **11** article(s)

- **Branch example:** `sf-cursor-canvas-faqs-<YYYYMMDD>`
- **Reviewer hint:** Canvas

- **`ka0VP000000RgHhYAK`** — Action Path error when selecting link alias. (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000RKFZYA4`** — Button Click Analytics Not Showing For Drag-and-Drop IAMs (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000JWDtYAO`** — Canvas won't save after making changes (No error message displayed) (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka03o000001dVxBAAU`** — Delayed Delivery Behavior in Branching IAM Canvas Step's (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP00000070o5YAA`** — I received the error: "Canvas Entry Properties may not be used in In-App Messages." (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000HPoPYAW`** — Re-Launching an Archived Campaign or Canvas (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000SFovYAG`** — Triggering Action-Based Campaign/Canvas Custom Event Dated in the Past (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000Ji3lYAC`** — Users in the Canvas are bigger than the Estimated Audience (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP0000008BhRYAU`** — When are Users "Kicked" Out of a Canvas via Exception Event? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000GmwjYAC`** — When is a Canvas Step Logged to a User's Profile? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000N7yTYAS`** — Why is a Tag No Longer Appended to a Campaign or Canvas? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/data/distribution/braze_currents/faq.md` — **7** article(s)

- **Branch example:** `sf-cursor-braze-currents-faq-<YYYYMMDD>`
- **Reviewer hint:** Currents

- **`ka0VP000000LtntYAC`** — Can I pull tag information of campaigns and canvases from Currents? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka03o000000tU17AAE`** — Currents Timestamps / Epoch Time (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000EtkbYAC`** — Does the Amplitude Destination Support the Send of Anonymous User Data via Braze Currents? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000Pc6vYAC`** — How Are Content Card/In-App message Control Group Impressions Being Logged in Currents? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000RFuDYAW`** — Targeting a Non-Existent User via API (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP0000007YD3YAM`** — What to expect when using Engagement Reports in S3 (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP0000006bcnYAA`** — Why Conversionbehaviours event from Currents has a different time than the canvas? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/channels/push/troubleshooting.md` — **4** article(s)

- **Branch example:** `sf-cursor-push-troubleshooting-<YYYYMMDD>`
- **Reviewer hint:** Push

- **`ka0VP000000OyHZYA0`** — Can Data be Migrated Between App Groups and Braze Dashboards Environments (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000D19ZYAS`** — Max Devices Rule (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000QlrJYAS`** — What FCM Responses are treated as uninstall push? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000OndtYAC`** — When does Braze Log Push Open for a User? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/administer/global/user_management/permissions.md` — **3** article(s)

- **Branch example:** `sf-cursor-user-management-permissions-<YYYYMMDD>`
- **Reviewer hint:** Dashboard & administration

- **`ka0VP0000003O7RYAU`** — Dashboard error when previewing email campaigns (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000Qh1JYAS`** — How to Get the View PII Limited Role User Permission Enabled? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000S9zdYAC`** — Why can't I fully Access my Braze Dashboard as a user. (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/channels/email/drag_and_drop/faq.md` — **3** article(s)

- **Branch example:** `sf-cursor-drag-and-drop-faq-<YYYYMMDD>`
- **Reviewer hint:** Email

- **`ka0VP000000ThO9YAK`** — Drag and drop content block loses set mobile styling and alignment (tier , score ; team ``)
- **`ka0VP000000NjIzYAK`** — Email text is not displaying in Dark Mode (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000N4AzYAK`** — Why is the custom font not displaying when previewing in email DND Templates? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/channels/email/subscriptions.md` — **2** article(s)

- **Branch example:** `sf-cursor-email-subscriptions-<YYYYMMDD>`
- **Reviewer hint:** Email

- **`ka0VP000000ANubYAG`** — Timestamp of Email Subscription (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000TkInYAK`** — What are the possible sources for subscription state updates? (tier , score ; team ``)

### PR batch: `_docs/_developer_guide/platforms/web/content_security_policy.md` — **1** article(s)

- **Branch example:** `sf-cursor-web-content-security-policy-<YYYYMMDD>`
- **Reviewer hint:** SDK & developer integrations

- **`ka0VP000000OgZBYA0`** — 3rd Party Web cookie tracking (tier , score ; team ``)

### PR batch: `_docs/_user_guide/administer/global/workspace_settings/email_preferences.md` — **1** article(s)

- **Branch example:** `sf-cursor-workspace-settings-email-preferences-<YYYYMMDD>`
- **Reviewer hint:** Dashboard & administration

- **`ka0VP000000RdTVYA0`** — 550 5.7.1 relaying denied email Error (tier , score ; team ``)

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

### PR batch: `_docs/_user_guide/channels/email/email_setup/authentication.md` — **1** article(s)

- **Branch example:** `sf-cursor-email-setup-authentication-<YYYYMMDD>`
- **Reviewer hint:** Email

- **`ka0VP000000TiQfYAK`** — How to check SPF, DKIM and DMARC records (tier , score ; team ``)

### PR batch: `_docs/_user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps.md` — **1** article(s)

- **Branch example:** `sf-cursor-email-setup-deliverability-pitfalls-and-spam-traps-<YYYYMMDD>`
- **Reviewer hint:** Email

- **`ka0VP000000TCnNYAW`** — What does Braze need to do to help set up BIMI(Brand Indicators for Messaging Identification)? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/channels/email/reporting.md` — **1** article(s)

- **Branch example:** `sf-cursor-email-reporting-<YYYYMMDD>`
- **Reviewer hint:** Email

- **`ka0VP000000RdzlYAC`** — Metric counts are different in Email Performance Dashboard vs Engagement Report (tier , score ; team ``)

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

### PR batch: `_docs/_user_guide/data/infrastructure/data_points.md` — **1** article(s)

- **Branch example:** `sf-cursor-infrastructure-data-points-<YYYYMMDD>`
- **Reviewer hint:** Data platform

- **`ka0VP0000009TFhYAM`** — Subscriptions & Usage - How Often is the Data Refreshed for Data Points? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

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

### PR batch: `_docs/_user_guide/messaging/messaging_fundamentals/sending_test_messages.md` — **1** article(s)

- **Branch example:** `sf-cursor-messaging-fundamentals-sending-test-messages-<YYYYMMDD>`
- **Reviewer hint:** Messaging & automation (Campaigns / Canvas-adjacent)

- **`ka0VP0000007fJNYAY`** — Will Receiving a Seed Email Update My User Profile / Analytics? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
