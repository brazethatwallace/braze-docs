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

Unique recipient count is incremented before ESP send; sent count after successful ESP response. Permanent errors (invalid email) or duplicate addresses can cause unique recipients to exceed sends.

### Campaign Last Sent Metric Does Not Match Last Message Send Timestamp

Add a note to campaign analytics docs: For campaigns with single scheduled send, Last Sent typically matches launch time. For repeating campaigns with Send in Local Time Zone enabled, Last Sent may appear earlier than the scheduled time because users in different time zones (e.g. GMT vs PST) can cause sends to occur out of order.

### Why does my historical campaign no longer show any metrics on the Analytics page?

Add 90-day default reporting window to analytics/reporting docs if not documented.
