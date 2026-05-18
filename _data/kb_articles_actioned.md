# KB articles — Phase 1 actionable backlog

Generated from `_data/kb_articles.csv` on **2026-05-18 16:14 UTC**.

These rows passed automated Phase 1 gates and resolve to an on-disk `_docs/...` file. They are **not** marked `actioned` in the CSV — this file is a **work queue** for Phase 2.

**Totals:** **25** actionable rows (of 246).

## 1. Multi-article batches (same primary doc)

Use when several articles should land in **one PR** touching the same file.

### Product vertical ownership (multi-article batches)

When opening a **batched** PR (several KAs, one primary doc), route review to the right **product vertical** (Email, Push, SMS, Canvas, API, Partners, SDK, Analytics, Currents, etc.). The **Suggested product vertical** column is path-based only — **fill in Product owner** when you know the owning team (or correct the suggestion). Agents and scripts should copy the suggested vertical into PR descriptions; use **TBD** rows to realign batching after owners are assigned.

_No groups of 2+ articles share the same resolved primary file._

## 2. Batches by vertical (IA bucket) and team

Within each vertical, rows are sorted by **tier ascending**, **score descending**, then title.

### Vertical: `analytics` — **1** articles

#### Team: `docs` — 1 articles

| Tier | Score | article_id | Title | Primary `_docs` target |
| --- | --- | --- | --- | --- |
| 1 | 7.5 | `ka0VP000000TZiLYAW` | Silent Push & Uninstall Tracking | `_docs/_user_guide/analytics/tracking/uninstall_tracking.md` |

### Vertical: `api` — **6** articles

#### Team: `docs` — 6 articles

| Tier | Score | article_id | Title | Primary `_docs` target |
| --- | --- | --- | --- | --- |
| 1 | 7.5 | `ka0VP000000HLEXYA4` | API Success Message Received But No Message Delivered | `_docs/_api/errors.md` |
| 1 | 7.5 | `ka0VP000000RQeLYAW` | Campaigns Targeting New Users Surfaced Race Conditions | `_docs/_api/endpoints/user_data/post_user_track_synchronous.md` |
| 1 | 7.5 | `ka0VP000000KuCXYA0` | How to view Spam List of Users | `_docs/_api/objects_filters/user_attributes_object.md` |
| 1 | 7.5 | `ka0VP000000H37xYAC` | Identify Endpoint: User Alias not associated successfully with external ID after 201 response | `_docs/_api/endpoints/user_data/post_user_identify.md` |
| 1 | 5 | `ka0VP000000RVMHYA4` | Can't Update Phone Number Using /Subscription/Status/Set Endpoint | `_docs/_api/endpoints/subscription_groups/post_update_user_subscription_group_status.md` |
| 3 | 4.5 | `ka0VP000000U1RhYAK` | Liquid does not render when included directly in requests made to the `/campaigns/trigger/send` endpoint. | `_docs/_api/endpoints/messaging/send_messages/post_send_triggered_campaigns.md` |

### Vertical: `brazeai` — **1** articles

#### Team: `docs` — 1 articles

| Tier | Score | article_id | Title | Primary `_docs` target |
| --- | --- | --- | --- | --- |
| 1 | 5 | `ka0VP000000DesTYAS` | How To Enable Intelligent Timing In A Canvas | `_docs/_user_guide/brazeai/intelligence_suite/intelligent_timing.md` |

### Vertical: `channels` — **4** articles

#### Team: `docs` — 3 articles

| Tier | Score | article_id | Title | Primary `_docs` target |
| --- | --- | --- | --- | --- |
| 1 | 7.5 | `ka0VP000000QSlRYAW` | When Does Braze Log A Successful "Send" For Push Deliveries? | `_docs/_user_guide/channels/push.md` |
| 1 | 5 | `ka0VP000000SBADYA4` | Firebase SenderID Mismatch | `_docs/_user_guide/channels/push/push_error_codes.md` |
| 1 | 5 | `ka0VP000000TFTVYA4` | How can I see the behaviour of multiple users logged into a single device? | `_docs/_user_guide/channels/push/troubleshooting.md` |

#### Team: `kb` — 1 articles

| Tier | Score | article_id | Title | Primary `_docs` target |
| --- | --- | --- | --- | --- |
| 1 | 5 | `ka0VP000000QZwbYAG` | More or Less Unsubscribes than Clicks on Unsubscribe Link | `_docs/_user_guide/channels/email/reporting/analytics_glossary.md` |

### Vertical: `data` — **1** articles

#### Team: `docs` — 1 articles

| Tier | Score | article_id | Title | Primary `_docs` target |
| --- | --- | --- | --- | --- |
| 1 | 10 | `ka0VP000000TBePYAW` | Braze Currents Data Clients Questions | `_docs/_user_guide/data/distribution/braze_currents/faq.md` |

### Vertical: `developer_guide` — **3** articles

#### Team: `docs` — 3 articles

| Tier | Score | article_id | Title | Primary `_docs` target |
| --- | --- | --- | --- | --- |
| 1 | 7.5 | `ka03o000001R1LLAA0` | An App Version has sessions logged even though it is not released yet | `_docs/_developer_guide/analytics/setting_user_ids.md` |
| 1 | 7.5 | `ka0VP000000R7YTYA0` | How are Currency Exchange Rates Calculated for the Braze Dashboard | `_docs/_developer_guide/analytics/logging_purchases.md` |
| 1 | 7.5 | `ka0VP000000RK7VYAW` | Links in an Email campaign are opening the App | `_docs/_developer_guide/push_notifications/ios_deep_linking_guide.md` |

### Vertical: `messaging` — **5** articles

#### Team: `docs` — 5 articles

| Tier | Score | article_id | Title | Primary `_docs` target |
| --- | --- | --- | --- | --- |
| 1 | 7.5 | `ka0VP000000HrRJYA0` | How Conversions are calculated in the Conversions Dashboard | `_docs/_user_guide/messaging/canvas/faqs.md` |
| 1 | 5 | `ka0VP000000TYRJYA4` | Canvas Delay Step "At a specific time" Option | `_docs/_user_guide/messaging/canvas/canvas_components/delay_step.md` |
| 1 | 5 | `ka0VP0000001b3xYAA` | Facebook Audience Sync - New Audience within Canvas step | `_docs/_user_guide/messaging/canvas/canvas_components/audience_sync.md` |
| 1 | 5 | `ka0VP000000Tu3dYAC` | Is it possible to create an action-triggered in-app message within a canvas? | `_docs/_user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas.md` |
| 1 | 5 | `ka0VP000000S1HJYA0` | Unreachable Event Properties in Canvas | `_docs/_user_guide/messaging/canvas/canvas_components/message_step.md` |

### Vertical: `onboarding_faq.md` — **1** articles

#### Team: `kb` — 1 articles

| Tier | Score | article_id | Title | Primary `_docs` target |
| --- | --- | --- | --- | --- |
| 1 | 7.5 | `ka0VP000000NmyPYAS` | Attributes not updated via API after updating user alias | `_docs/_user_guide/onboarding_faq.md` |

### Vertical: `partners` — **3** articles

#### Team: `docs` — 3 articles

| Tier | Score | article_id | Title | Primary `_docs` target |
| --- | --- | --- | --- | --- |
| 1 | 7.5 | `ka0VP000000NvqPYAS` | Appsflyer Install Attribution Source Data is not Being Passed to Braze for iOS Devices | `_docs/_partners/data_and_analytics.md` |
| 1 | 7.5 | `ka0VP000000NFXpYAO` | Troubleshooting Missing mParticle Events In Braze | `_docs/_partners/data_and_analytics/customer_data_platform/mParticle/mparticle.md` |
| 1 | 5 | `ka0VP000000MpOrYAK` | Using Zapier to Hit Braze's /users/track Endpoint | `_docs/_partners/data_and_analytics/workflow_automation/zapier.md` |
