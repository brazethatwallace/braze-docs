---
nav_title: Canvas alerts
article_title: Canvas threshold alerts
page_order: 4
page_type: reference
description: "This reference article covers how to set up threshold alerts for a Canvas so you're proactively notified when user entries or messages sent fall outside your expected range."
tool: Canvas
channel:
- email
- webhooks
---

# Canvas threshold alerts

> Canvas threshold alerts let you know when something in a Canvas isn't going as planned, so you can catch a stalled journey or an unexpected drop-off before it affects your customers.

{% multi_lang_include alerts/early_access_beta_alert.md feature='Canvas threshold alerts' %}

Set a volume threshold for user entries or messages sent, and Braze notifies you by email or webhook if that threshold is crossed. You can also create multiple alerts for the same Canvas—for example, one alert for user entries and another for messages sent.

Not sure where to start? [Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities) can walk you through how to set up a Canvas threshold alert.

## Step 1: Create an alert

Alerts are set at the Canvas level, and you can configure them for both active and draft Canvases. To open the **Manage Alerts** page for a Canvas, either:

- Go to **Messaging** > **Canvas**, and select **Manage alerts** from the context menu for an individual Canvas
- For active Canvases, open **Canvas Analytics** and select **Manage alerts**.

From the **Manage Alerts** page, select **Configure alert** to create a new alert.

## Step 2: Name your alert and select a Canvas

Give your alert a name and confirm the Canvas it applies to.

![The Configure Alert panel showing the alert name and Canvas name fields, an empty rule group, and a summary sidebar for alert rules, schedule, and notifications.]({% image_buster /assets/img/canvas_threshold_alerts/configure_alert.png %})

## Step 3: Set alert rules

Alert rules define the threshold that triggers a notification. You can build rules using two metrics:

- **User entries:** Number of users who entered the Canvas
- **Messages sent:** Number of messages sent from the Canvas

For each rule, choose a comparison (less than, greater than, less than or equal to, greater than or equal to, or equal to) and a volume threshold. For example, a rule for "User entries less than 3,000" flags a Canvas that's normally reaching thousands of users but has suddenly stalled—a sign of an upstream audience or entry issue worth investigating.

You can group multiple rules together and combine rule groups with AND or OR logic to build more specific alert conditions.

## Step 4: Set the alert schedule

Define how often your alert rules are checked. You can set the check frequency anywhere from 3 to 12 hours (in 1-hour increments), or every 24 hours. Once activated, an alert continues checking on this schedule for as long as the alert and its associated Canvas is active.

## Step 5: Set up notifications

Choose who should be notified when an alert rule is met, and how they're notified:

- **Email:** Add one or more recipient email addresses
- **Webhook:** Enter the webhook URL to notify, and optionally add custom request headers required by your webhook destination

You can enable one or both notification methods for a single alert.

![The Notifications section of the Configure Alert panel, showing Email and Webhook toggles, an email recipients field, a webhook URL field, a note about payload contents, and optional request header fields.]({% image_buster /assets/img/canvas_threshold_alerts/notifications.png %})

Webhook alerts are useful for routing notifications to external platforms, such as a Slack channel—for more, see Slack's documentation for [sending messages using incoming webhooks](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/). Each webhook notification sends a JSON payload with the alert name, evaluation window, and the conditions that triggered the alert.

### Example webhook payload

The following is an example of the JSON payload sent in a POST request to your webhook endpoint when an alert is triggered:

```json
{
  "alert": {
    "name": "Canvas Alert - August 6, 2026",
    "target_type": "CANVAS"
  },
  "evaluation_window_start": "2026-08-06T10:28:01Z",
  "evaluation_window_end": "2026-08-06T13:28:01Z",
  "conditions": [
    {
      "subject": "user_entries",
      "operator": "lt",
      "threshold_value": 500,
      "metric_value": 0.0,
      "group_index": 0
    },
    {
      "subject": "messages_sent",
      "operator": "lt",
      "threshold_value": 500,
      "metric_value": 0.0,
      "group_index": 0
    }
  ]
}
```

## Step 6: Save your alert

Review your alert rules, schedule, and notification settings in the summary panel, then select **Save alert**.

## Step 7: Activate the alert

Saving an alert doesn't activate it. To turn it on, go to the **Manage Alerts** page and use the **Status** toggle for your alert. An alert stays active until you deactivate it or until its associated Canvas is no longer active. The **Alerts Configured** column on the **Canvas** page shows a bell icon for any Canvas with at least one saved alert.

## Considerations

- **Draft Canvases:** You can set up a threshold alert for a Canvas that's still in draft, but the alert won't start checking against your rules until the Canvas launches.
