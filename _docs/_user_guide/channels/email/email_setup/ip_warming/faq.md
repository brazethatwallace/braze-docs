---
nav_title: FAQ
article_title: Automated IP warming FAQ
channel: email
page_order: 3
description: "Answers to frequently asked questions about automated IP warming in Braze."
---

# Automated IP warming FAQ

> Answers to common questions about [automated IP warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming). For IP warming concepts and manual schedules, see [IP warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming).

## When should I use automated IP warming?

Use automated IP warming when you need to:

- Warm new IP addresses for the first time
- Warm new business units or brands with new subdomains
- Rewarm existing IPs to improve deliverability
- Rewarm for specific mailbox providers to improve deliverability

For setup steps and prerequisites, see [Automated IP warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming).

## How far in advance must the start date be?

The start date must be tomorrow or later in your workspace time zone (or company time zone if the workspace has no override).

Braze creates campaigns at midnight in that time zone for the current day and the next day (0 to 1 days before send). Launching a plan also creates upcoming campaigns immediately.

## How many templates are required?

Braze calculates the minimum from your planned send volumes and the emailable users in the selected segments (not the full segment size). Provide more templates than the minimum so the system can adjust for deliverability issues without stopping. For details, see [Step 3: Select the messages to send]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#step-3-select-the-messages-to-send).

## Can I use the same segment for multiple warmup attempts?

Within a single active plan, Braze automatically excludes users who already received prior IP warming sends for the same template. If you stop a plan and start a new one that reuses the same segments, add a filter to exclude users who received campaigns from the previous plan.

## Can I start IP warming mid-schedule?

Automated IP warming always builds the schedule from the start of the ramp. To approximate a mid-schedule start, set **Current daily send volume** greater than 0 to match your current volume. When current volume is greater than 0, Braze does not apply IP-count scaling to day 1.

## What time zone is used for sending?

Sends use the workspace time zone when one is set; otherwise they use the company time zone. Campaigns are not created in each user's local time zone. To send in local time, update the campaigns created by the plan manually.

## How many IP warming plans can run at the same time?

More than one plan can run concurrently. For details, see [Multiple IP warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#multiple-ip-warming).

## How does volume scale for IP pools with multiple IPs?

When **Current daily send volume** is 0, day 1 starts at the lower of 50 sends per IP or 500 total. Volume then grows by about 1.75 times per send day, subject to ramp guardrails. For example, with 10 IPs: 500 → 875 → 1,532 → 2,681.

If you set a custom current volume greater than 0, IP-count scaling is not applied to day 1. For more on multi-IP plans, see [Warm multiple IPs in one pool]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#warm-multiple-ips-in-one-pool).

## Does automated IP warming support rate limiting per campaign?

No. Each campaign sends at the configured time without a per-campaign rate limit.

## When does Braze hold volume during IP warming?

Braze evaluates deliverability for campaigns that sent between 12 and 20 hours ago. If delivered, open, bounce, or spam complaint rates cross the benchmarks in [During active IP warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#during-active-ip-warming), Braze holds volume for the next send day instead of increasing it.

## What happens when volume is held?

Hold volume is the automatic adjustment Braze applies when those thresholds are crossed. The next scheduled send keeps the same volume instead of advancing. Braze replans future schedule entries, archives existing future campaigns from the plan, and creates new campaigns for the updated schedule immediately. The plan may take longer to reach target volume.

## Why don't campaign edits appear on the IP warming tracker?

Changes you make to campaigns created by automated IP warming (such as schedule, segment, or volume) are not synced back to the IP warming tracker. For related setup notes, see [Step 3: Select the messages to send]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#step-3-select-the-messages-to-send).

## Can I stop an IP warming plan?

Yes. Stopping permanently ends the plan: Braze disables linked campaigns and does not create future ones. You can't resume a stopped plan—create a new plan to continue. For steps to pick up after a stop, see [Stop an IP warmup plan]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#stop-an-ip-warmup-plan).

## When is an IP warming plan marked as complete?

The plan is marked complete after the last scheduled send day ends, at midnight in the effective time zone (workspace or company). For example, if the last campaign sends at 8 pm, the plan is marked complete at midnight four hours later.

## What data can I download?

CSV export includes per-campaign rows with day-level metrics: *Sent*, *Delivered*, *Bounces*, *Spam Reports*, *Total opens*, *Unique opens*, *Clicked*, and *Unsubscribed*. The tracker table aggregates multiple same-day campaigns into a daily view. For more, see [When an IP warming completes]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming#when-an-ip-warming-completes).
