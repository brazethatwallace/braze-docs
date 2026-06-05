---
nav_title: Campaign analytics
noindex: true
layout: redirect
redirect_to: /docs/user_guide/analytics/reports/campaign_analytics
page_order: 3
---

<!-- sf-kb-phase2-batch -->

## Salesforce Knowledge updates

### Email and SMS - unique recipients greater than sends

For email and SMS, Braze increments **Unique recipients** before the ESP send attempt and increments **Sends** after a successful ESP response. Permanent errors (such as invalid email addresses) or duplicate addresses can cause unique recipients to exceed sends.

### Campaign Last Sent Metric Does Not Match Last Message Send Timestamp

For a campaign with a single scheduled send, **Last sent** typically matches the launch time. For repeating campaigns with **Send in local time zone** enabled, **Last sent** can appear earlier than the scheduled time because sends to users in earlier time zones (for example, GMT vs. PST) can complete before your workspace schedule time.

### Why does my historical campaign no longer show any metrics on the Analytics page?

If a campaign was stopped more than 90 days ago, interaction data may have expired and metrics may no longer appear on the **Analytics** page. You can restore interaction data in the dashboard to view metrics again.
