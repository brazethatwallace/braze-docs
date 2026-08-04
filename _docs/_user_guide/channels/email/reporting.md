---
nav_title: Reporting
article_title: Email Reporting
page_order: 21
description: "This reference article covers the different components of email reporting and where it can be found in the dashboard."
tool:
  - Reports
channel:
  - email

---

# Email reporting

> This article covers the different components of your email reporting and where it can be found in the dashboard.

{% multi_lang_include analytics/campaign_analytics.md channel="email" %}

## Troubleshooting

### Bounced emails

- **554 5.7.1 [internal] recipient address was suppressed due to customer policy:** Try another address, re-engage on another channel, or remove the address from the suppression list for your own test addresses only. Avoid removing real user suppressions as that can hurt reputation.
- **Mailbox full / invalid account:** Often a list-quality signal. Prioritize users who recently opened or clicked (for example, the last 30–60 days) while you clean inactive or bad addresses.

#### Soft bounce retry behavior

When an email soft bounces due to temporary issues (such as mailbox full, server temporarily unavailable, or other transient deliverability failures), Braze automatically retries delivery for up to 72 hours. The number of retry attempts varies by receiver.

If the email is not successfully delivered after the retry period, Braze logs one soft bounce event for that campaign send. These soft bounces don't appear in campaign analytics, but you can:
- Monitor them in the [Message Activity Log]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) to see bounce reasons
- Use the [Soft Bounced segment filter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#soft-bounced) to exclude these users from future sends

Because of this retry period, email delivery metrics (deliveries, bounces, and spam rate) may not add up to 100% for campaigns where soft-bounced emails ultimately fail to deliver.

For more information on soft bounces, see the [Email analytics glossary]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary#soft-bounce).

### Invalid domains

Errors like `unable to get mx info` often mean many targets use bad domains (for example, typos). Segment, export, correct, and re-import those profiles.

### Throttled IPs

You may see the message `Email was deferred due to the following reason(s): [IPs were throttled by recipient server]` in the [Message Activity Log]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) if a mailbox provider temporarily slows or blocks delivery from your IP because of volume, reputation, or both. Braze retries deferred messages; if deferrals cluster from this, you often see elevated soft bounces alongside them.

This pattern usually means you're sending faster than the mailbox provider accepts for your current reputation. In addition to improving engagement and list quality, use [delivery speed rate limiting]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) to cap how quickly messages leave Braze for a campaign or Canvas. That helps reduce throttling while you work with your deliverability team on longer-term fixes.

If throttling persists for specific domains, reduce volume to those domains and contact Braze deliverability support for guidance.

### Unknown IP reputation status

If your email performance report shows an "unknown" value for IP reputation, this may be related to a Google Postmaster Tools outage. Google Postmaster Tools provides reputation data for Gmail deliverability, and temporary service disruptions can result in missing or unknown reputation values.

If you see an unknown reputation status and have questions about your email deliverability, contact [Braze Support]({{site.baseurl}}/support_contact/).
