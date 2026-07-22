---
nav_title: Canvas threshold alerts
article_title: Canvas Threshold Alerts
page_order: 4
page_type: reference
description: "This reference article covers how to set up threshold alerts for a Canvas so you're proactively notified when user entries or messages sent fall outside your expected range."
tool: Canvas
channel:
- email
- webhooks
---

# Canvas threshold alerts

> Catch a stalled journey or an unexpected drop-off before it affects your customers. Canvas threshold alerts let you know when something in a Canvas isn't going as planned. Set a volume threshold for user entries or messages sent, and Braze notifies you by email or webhook if that threshold is crossed.

{% multi_lang_include alerts/early_access_beta_alert.md feature='Canvas threshold alerts' %}

<!-- TODO: add a screenshot of the Configure Alert panel before publishing (PM-provided reference is internal-only) -->

## Configure an alert

Alerts are set at the Canvas level, and you can configure them for both active and draft Canvases. From your **Canvas** or **Canvas Analytics** page, select **Configure alert** to get started, then give your alert a name and confirm the Canvas it applies to.

You can create multiple alerts for the same Canvas. For example, you might add one alert for user entries and another for messages sent.

{% alert tip %}
Not sure where to start? [Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities) can walk you through how to set up a Canvas threshold alert.
{% endalert %}

### Set alert rules

Alert rules define the threshold that triggers a notification. You can build rules using two metrics:

- **User entries:** Number of users who entered the Canvas
- **Messages sent:** Number of messages sent from the Canvas

For each rule, choose a comparison (**less than** or **more than**) and a volume threshold. For example, a rule for **User entries less than 3,000** flags a Canvas that's normally reaching thousands of users but has suddenly stalled—a sign of an upstream audience or entry issue worth investigating.

You can group multiple rules together and combine rule groups with **AND** or **OR** logic to build more specific alert conditions.

### Set the alert schedule

Define how often your alert rules are checked. You can choose a check frequency of every 3, 6, 9, or 12 hours, or once every 24 hours. Once activated, an alert continues checking on this schedule for as long as its associated Canvas is active.

### Set up notifications

Choose who should be notified when an alert rule is met, and how they're notified:

- **Email:** Enter the email address of each recipient
- **Webhook:** Enter the webhook URL to notify

You can enable one or both notification methods for a single alert. Enter a valid email address or webhook URL.

Webhook alerts are useful for routing notifications to external platforms. For more, see Slack's documentation for [sending messages using incoming webhooks](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/).

## Save and activate an alert

Before saving, review your alert rules, schedule, and notification settings in the summary panel, then select **Save alert**.

Saving an alert doesn't activate it. To turn it on, go to the **Manage Alerts** page and use the **Status** toggle for your alert. An alert stays active until you deactivate it or until its associated Canvas is no longer active.

### Draft Canvases

You can set up a threshold alert for a Canvas that's still in draft, but the alert won't start checking against your rules until the Canvas launches.
