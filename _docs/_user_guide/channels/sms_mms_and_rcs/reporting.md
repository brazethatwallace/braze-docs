---
nav_title: "Reporting"
article_title: "Reporting"
page_order: 21
description: "This reference article covers SMS, MMS, and RCS metrics used at Braze, as well as how to view them in your SMS, MMS, and RCS campaigns."
alias: /sms_mms_rcs_reporting/
page_type: reference
tool:
  - Reports
channel:
  - SMS
  - MMS
  - RCS
  
---

# Reporting for SMS, MMS, and RCS

> This reference article covers SMS, MMS, and RCS metrics used at Braze, as well as how to view them in your SMS, MMS, and RCS campaigns.

{% multi_lang_include analytics/campaign_analytics.md channel="SMS" %}

{% alert note %}
Dashboard click metrics such as *Total Clicks* exclude suspected bot activity, but Currents still exports all click events with `is_suspected_bot_click` and `suspected_bot_click_reason` for warehouse reconciliation. For affected dashboard metrics, segmentation, and orchestration, see [Bot click filtering for SMS/RCS links]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/bot_click_filtering).
{% endalert %}

## Track SMS opt-ins and opt-outs

You can track SMS opt-ins and opt-outs with the following methods:

| Method | Description |
|--------|-------------|
| Segmenter | The segmenter displays the number of users in a specific [Subscription Group]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#subscription-group). It does not deduplicate by phone number—if multiple users share the same phone number, each instance is counted separately. |
| Subscription group timeseries | Provides a daily snapshot of subscriptions for email and phone numbers. The timeseries counts subscriptions, unsubscribes, and resubscribes. For example, if a user subscribes, unsubscribes, and then resubscribes, they are counted as one subscribed user. |
| Currents | Use Currents to export [subscription and engagement events]({{site.baseurl}}/message_events_glossary) for your own reporting. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Track SMS opt-ins and opt-outs" }

{% alert note %}
The _Opt-In_ and _Opt-Out_ statistics in the **SMS/MMS/RCS Performance** panel reflect users opting in or out through inbound keywords (for example, texting "START" for opt-in or "STOP" for opt-out). These numbers are typically lower than what is shown in the segmenter, as they count the number of times these keywords were texted, not the total number of users subscribed to SMS.
{% endalert %}

### Track SMS campaign opt-outs

Track SMS opt-outs at the campaign level by using the inbound receive table instead of the subscription group state change table. For example, in [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder) or your data warehouse, you can run a query that references the `USERS_MESSAGES_SMS_INBOUNDRECEIVE` or [`USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED`]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED) table.

This example query references the `USERS_MESSAGES_SMS_INBOUNDRECEIVE` table:

```sql
SELECT *
FROM USERS_MESSAGES_SMS_INBOUNDRECEIVE
WHERE app_group_id = 'app-group-id'
AND subscription_group_api_id = 'subscription_group_api_id'
AND action = 'Unsubscribed'
AND (campaign_id IS NOT NULL OR canvas_id IS NOT NULL);
```

This returns users who opted out of SMS communications for the given workspace and subscription group, filtered to those associated with campaigns or Canvases.

### Opt-out timing

Keyword and inbound-message events in Currents or your data warehouse, such as timestamps on [`users.messages.sms.InboundReceive`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-inbound-received-events) or subscription group state change events, are the authoritative source for when Braze recorded the opt-out.

{% alert note %}
Event timestamps reflect when Braze received or processed the inbound message, not necessarily when the user sent the SMS or when a carrier or SMS provider received it. If your analysis treats opt-outs as when Braze processed the inbound opt-out path, these timestamps match that definition.
{% endalert %}

The user profile shows current subscription state but may not surface a single "SMS unsubscribed at" field unless you set a [custom attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) or similar when processing opt-outs.

## Charges applied to SMS sending outcomes

This table reflects Braze billing, not your provider's billing. Outcomes that are not charged by Braze may be charged by your provider.

| Outcome | Definition | Charged by Braze |
|--------|------------|--------|
| Sent | A campaign or Canvas step has launched or triggered, and an SMS payload has been sent to the SMS provider. | No charge |
| Delivery Failed | The SMS payload couldn't be sent to the SMS provider. This can occur due to overflowing queues, suspended accounts, or media errors (in the case of MMS). | No charge |
| Delivered | The SMS provider received confirmation of message delivery from the upstream carrier (and, where available, from the destination device). | Charge |
| Rejected | The SMS provider received a rejected receipt indicating that the message wasn't delivered. This can happen for several reasons, including carrier content filtering or availability of the destination device. | Charge |
| **Sends to Carrier** | {% multi_lang_include analytics/metrics.md metric='Sends to Carrier' %} Deprecated for new dashboards. Some dashboards may still label this metric as **Sent to Carrier**. | Charges may apply based on individual message sending outcomes |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Charges applied to SMS sending outcomes" }

{% alert note %}
**Sends to Carrier** is deprecated for new dashboards. Use **Sent**, **Confirmed Delivery**, **Delivery Failed**, and **Rejections** for current reporting. See the [Report Metrics Glossary]({{site.baseurl}}/user_guide/analytics/metrics_glossary) for definitions.
{% endalert %}

## RCS and SMS fallback reporting

For RCS SMS fallback event behavior (including `IS_SMS_FALLBACK=TRUE`), see [How SMS fallback works with events and segmentation]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup#how-sms-fallback-works-with-events-and-segmentation).

{% alert note %}
Dashboard campaign analytics and Snowflake exports can differ slightly in timing and aggregation. For warehouse reconciliation, treat Snowflake or Currents event streams as the more granular source when metrics do not match the dashboard exactly.
{% endalert %}

## Reconcile *Rejections* with Snowflake or Currents

The *Rejections* metric in the dashboard is an aggregate workspace count. It isn't a row-level export, so you can't always match each rejection to a single row in Snowflake or a single `users.messages.sms.Rejection` event in Currents. For example, if the user profile was deleted before Braze finished processing the rejection for warehouse export, that rejection doesn't appear in your `USERS_MESSAGES_SMS_REJECTION_SHARED` table or Currents payload, while aggregate SMS reporting can still reflect the outcome. For more information, see the [SQL table reference]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#sms-message-events-and-deleted-user-profiles) and [SMS Rejection events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-rejection-events) in the Currents event glossary.