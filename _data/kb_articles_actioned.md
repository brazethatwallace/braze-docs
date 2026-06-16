# KB articles — Phase 1 actionable backlog

Generated from `_data/kb_articles.csv` on **2026-06-16 19:22 UTC**.

These rows passed Phase 1 and resolve to an on-disk `_docs/...` file. Work queue for Phase 2 — not CSV `actioned` status.

**Totals:** **106** actionable rows (of 108).
**Reference-repo verification:** **75** row(s) have `conflict_resolution` = `inconclusive` — confirm behavior in reference repos (see `.github/skills/salesforce-migration/SKILL.md` Phase 2) before drafting; do not copy Salesforce Knowledge text without source verification.

## 1. Phase 2 PR batches (one primary `_docs` file per PR)

Open **one PR per row** in the table below. Each PR edits **only** that file; multiple Salesforce Knowledge articles may land in the same PR when they share the same `doc_path`.

Do **not** batch PRs by product vertical — mixed verticals under one path are expected (for example, mis-routed paths). Use **Suggested reviewer vertical** and `.github/support_analyzer_doc_assignees.csv` from the file path for `--assignee` only.

**Open PRs:** **54** (one per primary doc).

| Primary `_docs` target | Articles | Suggested reviewer vertical | Suggested branch slug | Product owner |
| --- | ---: | --- | --- | --- |
| `_docs/_user_guide/messaging/design_and_edit/personalize/liquid/faq.md` | 12 | Messaging (Liquid personalization) | `sf-cursor-liquid-faq-<YYYYMMDD>` |  |
| `_docs/_user_guide/messaging/canvas/faqs.md` | 11 | Canvas | `sf-cursor-canvas-faqs-<YYYYMMDD>` |  |
| `_docs/_user_guide/data/distribution/braze_currents/faq.md` | 7 | Currents | `sf-cursor-braze-currents-faq-<YYYYMMDD>` |  |
| `_docs/_api/endpoints/subscription_groups.md` | 4 | API / platform engineering | `sf-cursor-endpoints-subscription-groups-<YYYYMMDD>` |  |
| `_docs/_user_guide/channels/content_cards/create_a_content_card.md` | 4 | Content Cards | `sf-cursor-content-cards-create-a-content-card-<YYYYMMDD>` |  |
| `_docs/_user_guide/channels/push/troubleshooting.md` | 4 | Push | `sf-cursor-push-troubleshooting-<YYYYMMDD>` |  |
| `_docs/_developer_guide/sdk_integration/reading_verbose_logs.md` | 3 | SDK & developer integrations | `sf-cursor-sdk-integration-reading-verbose-logs-<YYYYMMDD>` |  |
| `_docs/_user_guide/administer/global/user_management/permissions.md` | 3 | Dashboard & administration | `sf-cursor-user-management-permissions-<YYYYMMDD>` |  |
| `_docs/_user_guide/channels/email/drag_and_drop/faq.md` | 3 | Email | `sf-cursor-drag-and-drop-faq-<YYYYMMDD>` |  |
| `_docs/_user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery.md` | 3 | Messaging & automation (Campaigns / Canvas-adjacent) | `sf-cursor-schedule-your-campaign-scheduled-delivery-<YYYYMMDD>` |  |
| `_docs/_user_guide/messaging/campaigns/test_campaigns/campaign_analytics.md` | 3 | Messaging & automation (Campaigns / Canvas-adjacent) | `sf-cursor-test-campaigns-campaign-analytics-<YYYYMMDD>` |  |
| `_docs/_user_guide/administer/global/user_management/manage_company_users.md` | 2 | Dashboard & administration | `sf-cursor-user-management-manage-company-users-<YYYYMMDD>` |  |
| `_docs/_user_guide/channels/content_cards/reporting.md` | 2 | Content Cards | `sf-cursor-content-cards-reporting-<YYYYMMDD>` |  |
| `_docs/_user_guide/channels/email/drag_and_drop/dnd_editor_blocks.md` | 2 | Email | `sf-cursor-drag-and-drop-dnd-editor-blocks-<YYYYMMDD>` |  |
| `_docs/_user_guide/channels/email/subscriptions.md` | 2 | Email | `sf-cursor-email-subscriptions-<YYYYMMDD>` |  |
| `_docs/_user_guide/messaging/design_and_edit/media_library.md` | 2 | Messaging & automation (Campaigns / Canvas-adjacent) | `sf-cursor-design-and-edit-media-library-<YYYYMMDD>` |  |
| `_docs/_user_guide/messaging/design_and_edit/personalize/liquid/using_liquid.md` | 2 | Messaging (Liquid personalization) | `sf-cursor-liquid-using-liquid-<YYYYMMDD>` |  |
| `_docs/_api/api_limits.md` | 1 | API / platform engineering | `sf-cursor--api-api-limits-<YYYYMMDD>` |  |
| `_docs/_api/endpoints/export/campaigns/get_campaign_analytics.md` | 1 | API / platform engineering | `sf-cursor-campaigns-get-campaign-analytics-<YYYYMMDD>` |  |
| `_docs/_developer_guide/platforms/web/content_security_policy.md` | 1 | SDK & developer integrations | `sf-cursor-web-content-security-policy-<YYYYMMDD>` |  |
| `_docs/_developer_guide/sdk_integration.md` | 1 | SDK & developer integrations | `sf-cursor--developer-guide-sdk-integration-<YYYYMMDD>` |  |
| `_docs/_partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents.md` | 1 | Partners & integrations | `sf-cursor-cloud-storage-microsoft-azure-blob-storage-for-currents-<YYYYMMDD>` |  |
| `_docs/_user_guide/administer/global/saml_single_sign_on/saml_sso_setup.md` | 1 | Dashboard & administration | `sf-cursor-saml-single-sign-on-saml-sso-setup-<YYYYMMDD>` |  |
| `_docs/_user_guide/administer/global/workspace_settings/email_preferences.md` | 1 | Dashboard & administration | `sf-cursor-workspace-settings-email-preferences-<YYYYMMDD>` |  |
| `_docs/_user_guide/administer/personal/braze_support.md` | 1 | Dashboard & administration | `sf-cursor-personal-braze-support-<YYYYMMDD>` |  |
| `_docs/_user_guide/analytics/dashboards/home.md` | 1 | Analytics | `sf-cursor-dashboards-home-<YYYYMMDD>` |  |
| `_docs/_user_guide/analytics/reports/custom_events_report.md` | 1 | Analytics | `sf-cursor-reports-custom-events-report-<YYYYMMDD>` |  |
| `_docs/_user_guide/analytics/reports/engagement_reports.md` | 1 | Analytics | `sf-cursor-reports-engagement-reports-<YYYYMMDD>` |  |
| `_docs/_user_guide/analytics/reports/report_builder.md` | 1 | Analytics | `sf-cursor-reports-report-builder-<YYYYMMDD>` |  |
| `_docs/_user_guide/audience/manage_audience/import_users/csv_import.md` | 1 | Audience & segments | `sf-cursor-import-users-csv-import-<YYYYMMDD>` |  |
| `_docs/_user_guide/audience/manage_audience/merge_duplicate_users.md` | 1 | Audience & segments | `sf-cursor-manage-audience-merge-duplicate-users-<YYYYMMDD>` |  |
| `_docs/_user_guide/audience/segments/regex.md` | 1 | Audience & segments | `sf-cursor-segments-regex-<YYYYMMDD>` |  |
| `_docs/_user_guide/audience/segments/segmentation_filters.md` | 1 | Audience & segments | `sf-cursor-segments-segmentation-filters-<YYYYMMDD>` |  |
| `_docs/_user_guide/audience/subscription_preferences/preference_center/dnd_preference_center.md` | 1 | Audience & segments | `sf-cursor-preference-center-dnd-preference-center-<YYYYMMDD>` |  |
| `_docs/_user_guide/channels/email/email_setup/authentication.md` | 1 | Email | `sf-cursor-email-setup-authentication-<YYYYMMDD>` |  |
| `_docs/_user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps.md` | 1 | Email | `sf-cursor-email-setup-deliverability-pitfalls-and-spam-traps-<YYYYMMDD>` |  |
| `_docs/_user_guide/channels/email/email_setup/open_pixel_and_click_tracking.md` | 1 | Email | `sf-cursor-email-setup-open-pixel-and-click-tracking-<YYYYMMDD>` |  |
| `_docs/_user_guide/channels/email/reporting.md` | 1 | Email | `sf-cursor-email-reporting-<YYYYMMDD>` |  |
| `_docs/_user_guide/channels/email/reporting/analytics_glossary.md` | 1 | Email | `sf-cursor-reporting-analytics-glossary-<YYYYMMDD>` |  |
| `_docs/_user_guide/channels/sms_mms_and_rcs/faqs.md` | 1 | SMS / MMS / RCS | `sf-cursor-sms-mms-and-rcs-faqs-<YYYYMMDD>` |  |
| `_docs/_user_guide/channels/whatsapp/faq.md` | 1 | WhatsApp | `sf-cursor-whatsapp-faq-<YYYYMMDD>` |  |
| `_docs/_user_guide/data/activation/attributes/custom_attributes.md` | 1 | Data platform | `sf-cursor-attributes-custom-attributes-<YYYYMMDD>` |  |
| `_docs/_user_guide/data/activation/attributes/nested_custom_attribute_support.md` | 1 | Data platform | `sf-cursor-attributes-nested-custom-attribute-support-<YYYYMMDD>` |  |
| `_docs/_user_guide/data/distribution/export_braze_data.md` | 1 | Data platform | `sf-cursor-distribution-export-braze-data-<YYYYMMDD>` |  |
| `_docs/_user_guide/data/distribution/export_braze_data/segment_data_to_csv.md` | 1 | Data platform | `sf-cursor-export-braze-data-segment-data-to-csv-<YYYYMMDD>` |  |
| `_docs/_user_guide/data/infrastructure/data_points.md` | 1 | Data platform | `sf-cursor-infrastructure-data-points-<YYYYMMDD>` |  |
| `_docs/_user_guide/messaging/canvas/canvas_components/delay_step.md` | 1 | Canvas | `sf-cursor-canvas-components-delay-step-<YYYYMMDD>` |  |
| `_docs/_user_guide/messaging/canvas/create_a_canvas.md` | 1 | Canvas | `sf-cursor-canvas-create-a-canvas-<YYYYMMDD>` |  |
| `_docs/_user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics.md` | 1 | Canvas | `sf-cursor-testing-canvases-measuring-and-testing-with-canvas-analytics-<YYYYMMDD>` |  |
| `_docs/_user_guide/messaging/design_and_edit/personalize/connected_content.md` | 1 | Messaging (Connected Content) | `sf-cursor-personalize-connected-content-<YYYYMMDD>` |  |
| `_docs/_user_guide/messaging/design_and_edit/personalize/sources/promotion_codes.md` | 1 | Messaging & automation (Campaigns / Canvas-adjacent) | `sf-cursor-sources-promotion-codes-<YYYYMMDD>` |  |
| `_docs/_user_guide/messaging/messaging_fundamentals/conversion_events.md` | 1 | Messaging & automation (Campaigns / Canvas-adjacent) | `sf-cursor-messaging-fundamentals-conversion-events-<YYYYMMDD>` |  |
| `_docs/_user_guide/messaging/messaging_fundamentals/frequency_capping.md` | 1 | Messaging & automation (Campaigns / Canvas-adjacent) | `sf-cursor-messaging-fundamentals-frequency-capping-<YYYYMMDD>` |  |
| `_docs/_user_guide/messaging/messaging_fundamentals/sending_test_messages.md` | 1 | Messaging & automation (Campaigns / Canvas-adjacent) | `sf-cursor-messaging-fundamentals-sending-test-messages-<YYYYMMDD>` |  |

### PR batch: `_docs/_user_guide/messaging/design_and_edit/personalize/liquid/faq.md` — **12** article(s)

- **Branch example:** `sf-cursor-liquid-faq-<YYYYMMDD>`
- **Reviewer hint:** Messaging (Liquid personalization)

- **`ka0VP000000L5ntYAC`** — Aborted Message Error "Invalid from email address for recipient:" (tier , score ; team ``)
- **`ka0VP000000Tt4LYAS`** — Are There Size Limits of Canvas Entry Properties Object? (tier , score ; team ``)
- **`ka0VP000000FvpBYAS`** — Can I supply liquid inside the abort_message tag? (tier , score ; team ``)
- **`ka0VP000000TfNxYAK`** — DnD content block preview different from compose view (tier , score ; team ``)
- **`ka0VP000000Pal3YAC`** — Do we support an array of arrays in Liquid? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000S3hJYAS`** — How Do I Create A Dynamic 'Reply-To' Email Address? (tier , score ; team ``)
- **`ka0VP000000LhrZYAS`** — IAM Campaign Error: Warning: Use of the {% connected_content %} tag with retry is not available for this message type. (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000JENRYA4`** — Liquid Error Occurs On The Dashboard When Previewing Some Data Types (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000P5nhYAC`** — Liquid: Event Property Values in Message Composer Preview Mode (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000HoEvYAK`** — Why am I facing an error Unexpected end token when working with Liquid? (tier , score ; team ``)
- **`ka0VP000000Mh4jYAC`** — Why is my content block not appearing under 'Row' in the DnD search tool? (tier , score ; team ``)
- **`ka0VP000000Eiu1YAC`** — Why is my Liquid snippet containing Catalog items returning an abort message? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

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

### PR batch: `_docs/_api/endpoints/subscription_groups.md` — **4** article(s)

- **Branch example:** `sf-cursor-endpoints-subscription-groups-<YYYYMMDD>`
- **Reviewer hint:** API / platform engineering

- **`ka0VP000000RiUnYAK`** — Does a user need to be part of the selected SMS Subscription Group to receive SMS test messages? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000RXRJYA4`** — How to Avoid Duplicate User Creation via Email Capture Forms (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000RgnxYAC`** — Snowflake Log for USERS_MESSAGES_EMAIL_UNSUBSCRIBE (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000RGALYA4`** — Understanding the Subscription Group Timeseries (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/channels/content_cards/create_a_content_card.md` — **4** article(s)

- **Branch example:** `sf-cursor-content-cards-create-a-content-card-<YYYYMMDD>`
- **Reviewer hint:** Content Cards

- **`ka0VP000000MpiDYAS`** — Content Cards not Refreshing at openSession() (Web SDK) (tier , score ; team ``)
- **`ka0VP000000MOtJYAW`** — Content Cards Pinning/Unpinning Behavior (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000MTeTYAW`** — What is the Difference Between a Full Sync and a Partial Sync for Content Cards? (tier , score ; team ``)
- **`ka0VP000000P8TpYAK`** — What is the Impact of Stopping Content Cards Campaigns? (tier , score ; team ``)

### PR batch: `_docs/_user_guide/channels/push/troubleshooting.md` — **4** article(s)

- **Branch example:** `sf-cursor-push-troubleshooting-<YYYYMMDD>`
- **Reviewer hint:** Push

- **`ka0VP000000OyHZYA0`** — Can Data be Migrated Between App Groups and Braze Dashboards Environments (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000D19ZYAS`** — Max Devices Rule (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000QlrJYAS`** — What FCM Responses are treated as uninstall push? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000OndtYAC`** — When does Braze Log Push Open for a User? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_developer_guide/sdk_integration/reading_verbose_logs.md` — **3** article(s)

- **Branch example:** `sf-cursor-sdk-integration-reading-verbose-logs-<YYYYMMDD>`
- **Reviewer hint:** SDK & developer integrations

- **`ka0VP00000087sLYAQ`** — Data Not Getting to Braze (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP0000005gD7YAI`** — User Data Discrepancies when performing tasks via SDK/REST API simultaneously or in close succession. (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000Q6szYAC`** — When might a user have 0 sessions recorded against their profile? (tier , score ; team ``)

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

### PR batch: `_docs/_user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery.md` — **3** article(s)

- **Branch example:** `sf-cursor-schedule-your-campaign-scheduled-delivery-<YYYYMMDD>`
- **Reviewer hint:** Messaging & automation (Campaigns / Canvas-adjacent)

- **`ka0VP000000S1h7YAC`** — Schedule Campaign Sent A Day Before The Schedule Time (tier , score ; team ``)
- **`ka0VP000000GD2vYAG`** — Scheduled Delay For Campaign Delivery (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000Rt21YAC`** — Scheduled Email Campaign Did Not Send to the Entire Estimated Audience (tier , score ; team ``)

### PR batch: `_docs/_user_guide/messaging/campaigns/test_campaigns/campaign_analytics.md` — **3** article(s)

- **Branch example:** `sf-cursor-test-campaigns-campaign-analytics-<YYYYMMDD>`
- **Reviewer hint:** Messaging & automation (Campaigns / Canvas-adjacent)

- **`ka0VP000000MPSnYAO`** — Campaign Last Sent Metric Does Not Match Last Message Send Timestamp (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000P5kTYAS`** — Email and SMS - unique recipients greater than sends (tier , score ; team ``)
- **`ka0VP000000MwgTYAS`** — Why does my historical campaign no longer show any metrics on the Analytics page? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/administer/global/user_management/manage_company_users.md` — **2** article(s)

- **Branch example:** `sf-cursor-user-management-manage-company-users-<YYYYMMDD>`
- **Reviewer hint:** Dashboard & administration

- **`ka0VP000000RvTdYAK`** — Error When Adding New Dashboard User: "Email is already taken" (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000QPnZYAW`** — What if Dashboard Users need to Register with Multiple Companies in Braze? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/channels/content_cards/reporting.md` — **2** article(s)

- **Branch example:** `sf-cursor-content-cards-reporting-<YYYYMMDD>`
- **Reviewer hint:** Content Cards

- **`ka0VP000000QgejYAC`** — Does the content card ID change or remain the same when sent to a recipient more than once in a campaign? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000GCbVYAW`** — How to Configure a Web Content Card to Open a Link in a New Tab? (tier , score ; team ``)

### PR batch: `_docs/_user_guide/channels/email/drag_and_drop/dnd_editor_blocks.md` — **2** article(s)

- **Branch example:** `sf-cursor-drag-and-drop-dnd-editor-blocks-<YYYYMMDD>`
- **Reviewer hint:** Email

- **`ka0VP000000RIldYAG`** — Content Block Does Not Render in Email Preview (tier , score ; team ``)
- **`ka0VP000000RL8PYAW`** — Why is Drag And Drop Editor Ignoring The Alignment Settings of Some Elements? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/channels/email/subscriptions.md` — **2** article(s)

- **Branch example:** `sf-cursor-email-subscriptions-<YYYYMMDD>`
- **Reviewer hint:** Email

- **`ka0VP000000ANubYAG`** — Timestamp of Email Subscription (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))
- **`ka0VP000000TkInYAK`** — What are the possible sources for subscription state updates? (tier , score ; team ``)

### PR batch: `_docs/_user_guide/messaging/design_and_edit/media_library.md` — **2** article(s)

- **Branch example:** `sf-cursor-design-and-edit-media-library-<YYYYMMDD>`
- **Reviewer hint:** Messaging & automation (Campaigns / Canvas-adjacent)

- **`ka0VP000000GHmTYAW`** — Generate An Image Using AI (tier , score ; team ``)
- **`ka0VP000000NMZJYA4`** — Is it possible to create vanity URLs for Media Library image assets, and if so, how? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/messaging/design_and_edit/personalize/liquid/using_liquid.md` — **2** article(s)

- **Branch example:** `sf-cursor-liquid-using-liquid-<YYYYMMDD>`
- **Reviewer hint:** Messaging (Liquid personalization)

- **`ka0VP000000RNOjYAO`** — *INTERNAL* Liquid Parse Error Aborts Message (tier , score ; team ``)
- **`ka0VP000000RanNYAS`** — Liquid / Content Block changes position when switching from HTML > Classic Editor (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_api/api_limits.md` — **1** article(s)

- **Branch example:** `sf-cursor--api-api-limits-<YYYYMMDD>`
- **Reviewer hint:** API / platform engineering

- **`ka0VP000000MIW9YAO`** — What is the API Payload Limit for Braze APIs? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_api/endpoints/export/campaigns/get_campaign_analytics.md` — **1** article(s)

- **Branch example:** `sf-cursor-campaigns-get-campaign-analytics-<YYYYMMDD>`
- **Reviewer hint:** API / platform engineering

- **`ka0VP000000RY5dYAG`** — Can we see delivery failures from API campaigns or API triggered campaigns? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_developer_guide/platforms/web/content_security_policy.md` — **1** article(s)

- **Branch example:** `sf-cursor-web-content-security-policy-<YYYYMMDD>`
- **Reviewer hint:** SDK & developer integrations

- **`ka0VP000000OgZBYA0`** — 3rd Party Web cookie tracking (tier , score ; team ``)

### PR batch: `_docs/_developer_guide/sdk_integration.md` — **1** article(s)

- **Branch example:** `sf-cursor--developer-guide-sdk-integration-<YYYYMMDD>`
- **Reviewer hint:** SDK & developer integrations

- **`ka0VP000000NlavYAC`** — Are there known React and React Native versions needed to work with Braze's React SDK? (tier , score ; team ``)

### PR batch: `_docs/_partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents.md` — **1** article(s)

- **Branch example:** `sf-cursor-cloud-storage-microsoft-azure-blob-storage-for-currents-<YYYYMMDD>`
- **Reviewer hint:** Partners & integrations

- **`ka0VP000000EX7NYAW`** — Is there a set of IPs specifically for storage that can be provided to customers for whitelisting for Azure? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/administer/global/saml_single_sign_on/saml_sso_setup.md` — **1** article(s)

- **Branch example:** `sf-cursor-saml-single-sign-on-saml-sso-setup-<YYYYMMDD>`
- **Reviewer hint:** Dashboard & administration

- **`ka0VP000000NgHtYAK`** — Enabling Google SSO in Braze (tier , score ; team ``)

### PR batch: `_docs/_user_guide/administer/global/workspace_settings/email_preferences.md` — **1** article(s)

- **Branch example:** `sf-cursor-workspace-settings-email-preferences-<YYYYMMDD>`
- **Reviewer hint:** Dashboard & administration

- **`ka0VP000000RdTVYA0`** — 550 5.7.1 relaying denied email Error (tier , score ; team ``)

### PR batch: `_docs/_user_guide/administer/personal/braze_support.md` — **1** article(s)

- **Branch example:** `sf-cursor-personal-braze-support-<YYYYMMDD>`
- **Reviewer hint:** Dashboard & administration

- **`ka0VP000000TtCPYA0`** — Dashboard Doesn't Load Correctly (tier , score ; team ``)

### PR batch: `_docs/_user_guide/analytics/dashboards/home.md` — **1** article(s)

- **Branch example:** `sf-cursor-dashboards-home-<YYYYMMDD>`
- **Reviewer hint:** Analytics

- **`ka0VP000000LJfZYAW`** — Onboarding Campaigns -  1st Session Based on "Session Start" (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/analytics/reports/custom_events_report.md` — **1** article(s)

- **Branch example:** `sf-cursor-reports-custom-events-report-<YYYYMMDD>`
- **Reviewer hint:** Analytics

- **`ka0VP0000004hG5YAI`** — Custom Attribute methods for an Array value (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/analytics/reports/engagement_reports.md` — **1** article(s)

- **Branch example:** `sf-cursor-reports-engagement-reports-<YYYYMMDD>`
- **Reviewer hint:** Analytics

- **`ka0VP0000002K13YAE`** — Engagement Report - Broken Link Solution (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/analytics/reports/report_builder.md` — **1** article(s)

- **Branch example:** `sf-cursor-reports-report-builder-<YYYYMMDD>`
- **Reviewer hint:** Analytics

- **`ka0VP000000S9I5YAK`** — My Engagement Report/Report Builder Download link has expired. (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/audience/manage_audience/import_users/csv_import.md` — **1** article(s)

- **Branch example:** `sf-cursor-import-users-csv-import-<YYYYMMDD>`
- **Reviewer hint:** Audience & segments

- **`ka0VP000000RWTdYAO`** — Successful Response From /users/delete or users/merge Endpoint But The User Is Not Deleted In Braze (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/audience/manage_audience/merge_duplicate_users.md` — **1** article(s)

- **Branch example:** `sf-cursor-manage-audience-merge-duplicate-users-<YYYYMMDD>`
- **Reviewer hint:** Audience & segments

- **`ka0VP000000RaLxYAK`** — Why are multiple User Profiles associated with the Same Email Address? (tier , score ; team ``)

### PR batch: `_docs/_user_guide/audience/segments/regex.md` — **1** article(s)

- **Branch example:** `sf-cursor-segments-regex-<YYYYMMDD>`
- **Reviewer hint:** Audience & segments

- **`ka0VP000000OmgDYAS`** — Custom Event Properties Regex (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/audience/segments/segmentation_filters.md` — **1** article(s)

- **Branch example:** `sf-cursor-segments-segmentation-filters-<YYYYMMDD>`
- **Reviewer hint:** Audience & segments

- **`ka0VP000000942nYAA`** — I can't find a purchase value in a segmentation filter (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/audience/subscription_preferences/preference_center/dnd_preference_center.md` — **1** article(s)

- **Branch example:** `sf-cursor-preference-center-dnd-preference-center-<YYYYMMDD>`
- **Reviewer hint:** Audience & segments

- **`ka0VP0000003WeTYAU`** — Email Preference Center: "We are unable to process this request at this time, please try again later."  (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/channels/email/email_setup/authentication.md` — **1** article(s)

- **Branch example:** `sf-cursor-email-setup-authentication-<YYYYMMDD>`
- **Reviewer hint:** Email

- **`ka0VP000000TiQfYAK`** — How to check SPF, DKIM and DMARC records (tier , score ; team ``)

### PR batch: `_docs/_user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps.md` — **1** article(s)

- **Branch example:** `sf-cursor-email-setup-deliverability-pitfalls-and-spam-traps-<YYYYMMDD>`
- **Reviewer hint:** Email

- **`ka0VP000000TCnNYAW`** — What does Braze need to do to help set up BIMI(Brand Indicators for Messaging Identification)? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/channels/email/email_setup/open_pixel_and_click_tracking.md` — **1** article(s)

- **Branch example:** `sf-cursor-email-setup-open-pixel-and-click-tracking-<YYYYMMDD>`
- **Reviewer hint:** Email

- **`ka0VP000000RQb7YAG`** — Click Tracking Only Available for Links Directed to a HTTP or HTTPS Site (Can you click track phone numbers? etc.) (tier , score ; team ``)

### PR batch: `_docs/_user_guide/channels/email/reporting.md` — **1** article(s)

- **Branch example:** `sf-cursor-email-reporting-<YYYYMMDD>`
- **Reviewer hint:** Email

- **`ka0VP000000RdzlYAC`** — Metric counts are different in Email Performance Dashboard vs Engagement Report (tier , score ; team ``)

### PR batch: `_docs/_user_guide/channels/email/reporting/analytics_glossary.md` — **1** article(s)

- **Branch example:** `sf-cursor-reporting-analytics-glossary-<YYYYMMDD>`
- **Reviewer hint:** Email

- **`ka0VP000000Pzl3YAC`** — "Campaign is already in delay window, so not enqueueing another" outcome with no delay on campaign (tier , score ; team ``)

### PR batch: `_docs/_user_guide/channels/sms_mms_and_rcs/faqs.md` — **1** article(s)

- **Branch example:** `sf-cursor-sms-mms-and-rcs-faqs-<YYYYMMDD>`
- **Reviewer hint:** SMS / MMS / RCS

- **`ka0VP000000SGUrYAO`** — SMS Subscribes are not accurately reflected in SMS/MMS/RCS Channel Engagement (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/channels/whatsapp/faq.md` — **1** article(s)

- **Branch example:** `sf-cursor-whatsapp-faq-<YYYYMMDD>`
- **Reviewer hint:** WhatsApp

- **`ka0VP000000QZBpYAO`** — Whatsapp template has been falsely flagged - content against Whatsapp's Commerce Policy (tier , score ; team ``)

### PR batch: `_docs/_user_guide/data/activation/attributes/custom_attributes.md` — **1** article(s)

- **Branch example:** `sf-cursor-attributes-custom-attributes-<YYYYMMDD>`
- **Reviewer hint:** Data platform

- **`ka0VP000000TlYDYA0`** — Setting Custom Attribute as "" (blank) vs. null (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/data/activation/attributes/nested_custom_attribute_support.md` — **1** article(s)

- **Branch example:** `sf-cursor-attributes-nested-custom-attribute-support-<YYYYMMDD>`
- **Reviewer hint:** Data platform

- **`ka0VP000000Q6D3YAK`** — Testing Nested Custom Attributes and Nested Objects for Custom Event Properties (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/data/distribution/export_braze_data.md` — **1** article(s)

- **Branch example:** `sf-cursor-distribution-export-braze-data-<YYYYMMDD>`
- **Reviewer hint:** Data platform

- **`ka0VP000000FquLYAS`** — Missing Fields_To_Export In /Users/Export/Segment Export File (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/data/distribution/export_braze_data/segment_data_to_csv.md` — **1** article(s)

- **Branch example:** `sf-cursor-export-braze-data-segment-data-to-csv-<YYYYMMDD>`
- **Reviewer hint:** Data platform

- **`ka0VP000000Lt9ZYAS`** — How to Identify and Export Users Who Performed a Specific Custom Event? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/data/infrastructure/data_points.md` — **1** article(s)

- **Branch example:** `sf-cursor-infrastructure-data-points-<YYYYMMDD>`
- **Reviewer hint:** Data platform

- **`ka0VP0000009TFhYAM`** — Subscriptions & Usage - How Often is the Data Refreshed for Data Points? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/messaging/canvas/canvas_components/delay_step.md` — **1** article(s)

- **Branch example:** `sf-cursor-canvas-components-delay-step-<YYYYMMDD>`
- **Reviewer hint:** Canvas

- **`ka0VP000000RIAXYA4`** — Delay Step Auto Advancement Behavior When a Canvas is Stopped (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/messaging/canvas/create_a_canvas.md` — **1** article(s)

- **Branch example:** `sf-cursor-canvas-create-a-canvas-<YYYYMMDD>`
- **Reviewer hint:** Canvas

- **`ka0VP000000GxqXYAS`** — Is Random Variant Assignment Based on a User's Random Bucket number? (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics.md` — **1** article(s)

- **Branch example:** `sf-cursor-testing-canvases-measuring-and-testing-with-canvas-analytics-<YYYYMMDD>`
- **Reviewer hint:** Canvas

- **`ka0VP000000RL3ZYAW`** — Why Is Segment Size Smaller Than Canvas Analytics (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

### PR batch: `_docs/_user_guide/messaging/design_and_edit/personalize/connected_content.md` — **1** article(s)

- **Branch example:** `sf-cursor-personalize-connected-content-<YYYYMMDD>`
- **Reviewer hint:** Messaging (Connected Content)

- **`ka0VP0000003XAjYAM`** — Connected Content Call is not returning a response (tier , score ; team ``; **verify in reference repos** (`conflict_resolution`: inconclusive))

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
