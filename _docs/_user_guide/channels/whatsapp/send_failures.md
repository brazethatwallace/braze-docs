---
nav_title: Send failures
article_title: Investigate WhatsApp send failures
page_order: 22
page_type: reference
description: "Use campaign analytics, the Message Activity Log, and Currents to investigate WhatsApp send failures and common Meta error codes."
tool:
  - Reports
channel:
  - WhatsApp
---

# Investigate WhatsApp send failures

> Use this page when WhatsApp deliveries or reads are lower than expected, or when **Failures** in campaign analytics look elevated.

## Investigation workflow

Work through the following steps in order.

1. **Confirm failures in campaign or Canvas analytics.** Open the message step and review the **Failures** count and failure rate. If failures look elevated compared to sends or deliveries, continue to the next step.
2. **Find the error code in the Message Activity Log.** Open the [Message Activity Log]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) for the same send, filter to failed messages, and note the provider error code (for example, `131049` for per-user marketing limits). Use [Common failure codes](#common-failure-codes) to interpret the code and decide next steps.
3. **Export failures with Currents for analysis or retargeting.** After you know the error code, export WhatsApp send failure events through Currents. Use that data to analyze failure trends in your warehouse or to build segments and retarget users on another channel.

## Common failure codes

| Error code | Typical cause | Next step |
|---|---|---|
| `131049` | Meta per-user marketing frequency limit or US marketing pause | See [Meta resources]({{site.baseurl}}/user_guide/channels/whatsapp/meta_resources) and [Retargeting users on other Braze channels]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/optimized_delivery#retargeting-users-on-other-braze-channels) |
| `130472` | Meta marketing experiment holdout | See [Meta resources FAQ]({{site.baseurl}}/user_guide/channels/whatsapp/meta_resources#faq) |
| `131026` | Various non-delivery reasons (Meta doesn't disclose specifics) | Avoid immediate retries; review [Meta Cloud API troubleshooting](https://developers.facebook.com/docs/whatsapp/cloud-api/support#troubleshooting) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Common WhatsApp failure codes" }
