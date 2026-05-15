# KB articles — Phase 1 actionable backlog

Generated from `_data/kb_articles.csv` on **2026-05-15 17:45 UTC**.

These rows passed automated Phase 1 gates and resolve to an on-disk `_docs/...` file. They are **not** marked `actioned` in the CSV — this file is a **work queue** for Phase 2.

**Totals:** **44** actionable rows (of 521).
**Epic BD-6308:** **34** additional rows would have appeared here but are listed in `_data/kb_epic_bd6308_tracked_article_ids.txt` (Jira child issues under the epic); see `_data/kb_articles_skipped.md` for those rows.

## 1. Multi-article batches (same primary doc)

Use when several articles should land in **one PR** touching the same file.

### Product vertical ownership (multi-article batches)

When opening a **batched** PR (several KAs, one primary doc), route review to the right **product vertical** (Email, Push, SMS, Canvas, API, Partners, SDK, Analytics, Currents, etc.). The **Suggested product vertical** column is path-based only — **fill in Product owner** when you know the owning team (or correct the suggestion). Agents and scripts should copy the suggested vertical into PR descriptions; use **TBD** rows to realign batching after owners are assigned.

| Primary `_docs` target | Articles | Suggested product vertical | Product owner (your team — **fill in**) |
| --- | ---: | --- | --- |
| `_docs/_partners/canvas_audience_sync/facebook_audience_sync.md` | 4 | Partners (Audience Sync / Facebook) |  |
| `_docs/_api/endpoints/user_data/post_user_track.md` | 2 | API / platform engineering |  |
| `_docs/_developer_guide/sdk_integration/google_tag_manager.md` | 2 | SDK & developer integrations |  |
| `_docs/_partners/home.md` | 2 | Partners & integrations |  |
| `_docs/_user_guide/analytics/tracking/segment_analytics_tracking.md` | 2 | Analytics |  |
| `_docs/_user_guide/messaging/canvas/canvas_components/action_paths.md` | 2 | Canvas (Email channel triggers — confirm Email vs Canvas PM if needed) |  |
| `_docs/_user_guide/messaging/canvas/canvas_components/experiment_step.md` | 2 | Canvas |  |
| `_docs/_user_guide/messaging/canvas/troubleshooting.md` | 2 | Canvas |  |

### `_docs/_partners/canvas_audience_sync/facebook_audience_sync.md` — **4** articles

- **`ka0VP000000NBfVYAW`** — How does Braze connect to Facebook? (tier 1, score 7.5; team `docs`)
- **`ka0VP000000F1i9YAC`** — Facebook Audience Sync Step Fails to Display the Ad Account in Dropdown (tier 1, score 5; team `docs`)
- **`ka0VP000000RA3JYAW`** — Facebook Export/Audience Error: Error Validating Access Token (tier 1, score 5; team `docs`)
- **`ka0VP000000Asf3YAC`** — I receive an error when exporting a Facebook Audience (tier 1, score 5; team `docs`)

### `_docs/_api/endpoints/user_data/post_user_track.md` — **2** articles

- **`ka0VP000000KNWjYAO`** — /users/track Endpoint Response Time (tier 1, score 7.5; team `docs`)
- **`ka0VP000000FsUjYAK`** — 400 error - Bad Syntax (tier 1, score 7.5; team `docs`)

### `_docs/_developer_guide/sdk_integration/google_tag_manager.md` — **2** articles

- **`ka0VP000000O4iPYAS`** — Google Tag Manager (GTM) Braze Initialisation Failed (tier 1, score 7.5; team `docs`)
- **`ka0VP000000OmhpYAC`** — How to Enable Verbose Logging in Google Tag Manager (GTM) (tier 1, score 7.5; team `docs`)

### `_docs/_partners/home.md` — **2** articles

- **`ka0VP000000HmxtYAC`** — Why is it showing Invalid credentials from mParticle Current integration? (tier 1, score 7.5; team `docs`)
- **`ka0VP000000QhvlYAC`** — Deliverability Dashboard shows Google Postmaster as "Connected", Technology Partners records it as "Pending" (tier 1, score 5; team `docs`)

### `_docs/_user_guide/analytics/tracking/segment_analytics_tracking.md` — **2** articles

- **`ka0VP000000BT0HYAW`** — Does Segment Analytics Tracking Display Historical Data on Revenue Dashboard? (tier 1, score 5; team `docs`)
- **`ka0VP000000JUQbYAO`** — Segment Analytics Tracking Not Working (tier 1, score 5; team `kb`)

### `_docs/_user_guide/messaging/canvas/canvas_components/action_paths.md` — **2** articles

- **`ka0VP000000JVo5YAG`** — Action Paths when Ranking is off - what is the expected behaviour? (tier 1, score 7.5; team `docs`)
- **`ka0VP000000JtonYAC`** — How does the "Add an Email Address" trigger work? (tier 1, score 5; team `docs`)

### `_docs/_user_guide/messaging/canvas/canvas_components/experiment_step.md` — **2** articles

- **`ka0VP000000HF7VYAW`** — My Experiment Path is entering users into Content Card steps equally, why is there a discrepancy in Sends? (tier 1, score 7.5; team `docs`)
- **`ka0VP000000TG1NYAW`** — Experiment Path Canvas Step Window (tier 1, score 5; team `docs`)

### `_docs/_user_guide/messaging/canvas/troubleshooting.md` — **2** articles

- **`ka0VP000000So3VYAS`** — Action Based Campaigns/Canvases Using Custom Event Properties as Trigger Not Sending (tier 1, score 7.5; team `docs`)
- **`ka0VP000000TYzBYAW`** — Action-Based Delivery Campaign Not Sending (Check Custom Event Timestamp) (tier 1, score 7.5; team `docs`)

## 2. Batches by vertical (IA bucket) and team

Within each vertical, rows are sorted by **tier ascending**, **score descending**, then title.

### Vertical: `analytics` — **3** articles

#### Team: `docs` — 2 articles

| Tier | Score | article_id | Title | Primary `_docs` target |
| --- | --- | --- | --- | --- |
| 1 | 7.5 | `ka0VP000000TZiLYAW` | Silent Push & Uninstall Tracking | `_docs/_user_guide/analytics/tracking/uninstall_tracking.md` |
| 1 | 5 | `ka0VP000000BT0HYAW` | Does Segment Analytics Tracking Display Historical Data on Revenue Dashboard? | `_docs/_user_guide/analytics/tracking/segment_analytics_tracking.md` |

#### Team: `kb` — 1 articles

| Tier | Score | article_id | Title | Primary `_docs` target |
| --- | --- | --- | --- | --- |
| 1 | 5 | `ka0VP000000JUQbYAO` | Segment Analytics Tracking Not Working | `_docs/_user_guide/analytics/tracking/segment_analytics_tracking.md` |

### Vertical: `api` — **8** articles

#### Team: `docs` — 8 articles

| Tier | Score | article_id | Title | Primary `_docs` target |
| --- | --- | --- | --- | --- |
| 1 | 7.5 | `ka0VP000000KNWjYAO` | /users/track Endpoint Response Time | `_docs/_api/endpoints/user_data/post_user_track.md` |
| 1 | 7.5 | `ka0VP000000FsUjYAK` | 400 error - Bad Syntax | `_docs/_api/endpoints/user_data/post_user_track.md` |
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

### Vertical: `developer_guide` — **5** articles

#### Team: `docs` — 5 articles

| Tier | Score | article_id | Title | Primary `_docs` target |
| --- | --- | --- | --- | --- |
| 1 | 7.5 | `ka03o000001R1LLAA0` | An App Version has sessions logged even though it is not released yet | `_docs/_developer_guide/analytics/setting_user_ids.md` |
| 1 | 7.5 | `ka0VP000000O4iPYAS` | Google Tag Manager (GTM) Braze Initialisation Failed | `_docs/_developer_guide/sdk_integration/google_tag_manager.md` |
| 1 | 7.5 | `ka0VP000000R7YTYA0` | How are Currency Exchange Rates Calculated for the Braze Dashboard | `_docs/_developer_guide/analytics/logging_purchases.md` |
| 1 | 7.5 | `ka0VP000000OmhpYAC` | How to Enable Verbose Logging in Google Tag Manager (GTM) | `_docs/_developer_guide/sdk_integration/google_tag_manager.md` |
| 1 | 7.5 | `ka0VP000000RK7VYAW` | Links in an Email campaign are opening the App | `_docs/_developer_guide/push_notifications/ios_deep_linking_guide.md` |

### Vertical: `messaging` — **11** articles

#### Team: `docs` — 11 articles

| Tier | Score | article_id | Title | Primary `_docs` target |
| --- | --- | --- | --- | --- |
| 1 | 7.5 | `ka0VP000000So3VYAS` | Action Based Campaigns/Canvases Using Custom Event Properties as Trigger Not Sending | `_docs/_user_guide/messaging/canvas/troubleshooting.md` |
| 1 | 7.5 | `ka0VP000000JVo5YAG` | Action Paths when Ranking is off - what is the expected behaviour? | `_docs/_user_guide/messaging/canvas/canvas_components/action_paths.md` |
| 1 | 7.5 | `ka0VP000000TYzBYAW` | Action-Based Delivery Campaign Not Sending (Check Custom Event Timestamp) | `_docs/_user_guide/messaging/canvas/troubleshooting.md` |
| 1 | 7.5 | `ka0VP000000HrRJYA0` | How Conversions are calculated in the Conversions Dashboard | `_docs/_user_guide/messaging/canvas/faqs.md` |
| 1 | 7.5 | `ka0VP000000HF7VYAW` | My Experiment Path is entering users into Content Card steps equally, why is there a discrepancy in Sends? | `_docs/_user_guide/messaging/canvas/canvas_components/experiment_step.md` |
| 1 | 5 | `ka0VP000000TYRJYA4` | Canvas Delay Step "At a specific time" Option | `_docs/_user_guide/messaging/canvas/canvas_components/delay_step.md` |
| 1 | 5 | `ka0VP000000TG1NYAW` | Experiment Path Canvas Step Window | `_docs/_user_guide/messaging/canvas/canvas_components/experiment_step.md` |
| 1 | 5 | `ka0VP0000001b3xYAA` | Facebook Audience Sync - New Audience within Canvas step | `_docs/_user_guide/messaging/canvas/canvas_components/audience_sync.md` |
| 1 | 5 | `ka0VP000000JtonYAC` | How does the "Add an Email Address" trigger work? | `_docs/_user_guide/messaging/canvas/canvas_components/action_paths.md` |
| 1 | 5 | `ka0VP000000Tu3dYAC` | Is it possible to create an action-triggered in-app message within a canvas? | `_docs/_user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas.md` |
| 1 | 5 | `ka0VP000000S1HJYA0` | Unreachable Event Properties in Canvas | `_docs/_user_guide/messaging/canvas/canvas_components/message_step.md` |

### Vertical: `onboarding_faq.md` — **1** articles

#### Team: `kb` — 1 articles

| Tier | Score | article_id | Title | Primary `_docs` target |
| --- | --- | --- | --- | --- |
| 1 | 7.5 | `ka0VP000000NmyPYAS` | Attributes not updated via API after updating user alias | `_docs/_user_guide/onboarding_faq.md` |

### Vertical: `partners` — **9** articles

#### Team: `docs` — 9 articles

| Tier | Score | article_id | Title | Primary `_docs` target |
| --- | --- | --- | --- | --- |
| 1 | 7.5 | `ka0VP000000NvqPYAS` | Appsflyer Install Attribution Source Data is not Being Passed to Braze for iOS Devices | `_docs/_partners/data_and_analytics.md` |
| 1 | 7.5 | `ka0VP000000NBfVYAW` | How does Braze connect to Facebook? | `_docs/_partners/canvas_audience_sync/facebook_audience_sync.md` |
| 1 | 7.5 | `ka0VP000000NFXpYAO` | Troubleshooting Missing mParticle Events In Braze | `_docs/_partners/data_and_analytics/customer_data_platform/mParticle/mparticle.md` |
| 1 | 7.5 | `ka0VP000000HmxtYAC` | Why is it showing Invalid credentials from mParticle Current integration? | `_docs/_partners/home.md` |
| 1 | 5 | `ka0VP000000QhvlYAC` | Deliverability Dashboard shows Google Postmaster as "Connected", Technology Partners records it as "Pending" | `_docs/_partners/home.md` |
| 1 | 5 | `ka0VP000000F1i9YAC` | Facebook Audience Sync Step Fails to Display the Ad Account in Dropdown | `_docs/_partners/canvas_audience_sync/facebook_audience_sync.md` |
| 1 | 5 | `ka0VP000000RA3JYAW` | Facebook Export/Audience Error: Error Validating Access Token | `_docs/_partners/canvas_audience_sync/facebook_audience_sync.md` |
| 1 | 5 | `ka0VP000000Asf3YAC` | I receive an error when exporting a Facebook Audience | `_docs/_partners/canvas_audience_sync/facebook_audience_sync.md` |
| 1 | 5 | `ka0VP000000MpOrYAK` | Using Zapier to Hit Braze's /users/track Endpoint | `_docs/_partners/data_and_analytics/workflow_automation/zapier.md` |

### Vertical: `releases` — **1** articles

#### Team: `docs` — 1 articles

| Tier | Score | article_id | Title | Primary `_docs` target |
| --- | --- | --- | --- | --- |
| 1 | 7.5 | `ka0VP000000TK09YAG` | Understanding "Machine Opens" from Email Campaign Analytics | `_docs/_releases/home.md` |
