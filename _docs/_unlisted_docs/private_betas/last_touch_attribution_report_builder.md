---
nav_title: "Last-touch attribution"
permalink: /last-touch_attribution_metrics/
hidden: true
---

# Last-touch attribution metrics

> Add last-touch attribution metrics to your reports in the Report Builder.

{% alert note %}
Last-touch attribution metrics are in early access. If you're interested in participating in the early access, contact your customer success manager.
{% endalert %}

Last-touch attribution (LTA) is a conversion attribution model that gives full credit for a conversion to the last message a user interacted with before converting. Unlike campaign-level conversion windows, LTA uses industry-standard attribution windows for each channel:

| Channel | Attribution window |
| --- | --- |
| Email | 30 days |
| SMS | 7 days |
| WhatsApp | 7 days |
| Push | 7 days |
| In-app message | 3 days |
| Content Cards | 3 days |
| Webhook | excluded from this model |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
If a conversion occurs outside of a channel's attribution window, it is not counted under this model. 
{% endalert %}

## Benefits

Last-touch attribution offers key advantages over standard conversion tracking: 

* It allows you to attribute conversions to specific touchpoints, unlocking the ability to understand which channels (not just campaigns or Canvases) are driving results.   
* Credit is given exclusively to the last-touched message, so each conversion is counted only once, eliminating overlapping conversions across campaigns or Canvases with shared conversion events and audiences.

## Add last-touch attribution metrics to your report

1. Go to **Report Builder**, under **Analytics**.
2. Select **Create report** > **Create custom report**. 
3. Within the **Rows** dropdown, select what you want to create a report on.
4. (Optional) Select **Add drilldown**, then choose an area to dive deeper into your reporting.
5. Under **Columns**, select **Customize metrics**   
6. Under **Conversions**, select **Last Touch Attribution**, and then select **Select All**. 

{% alert note %}
Revenue and purchase metrics are not available.
{% endalert %}

![The Customize metrics panel with last-touch attribution metrics.]({% image_buster /assets/unlisted_docs/img/report_builder_2/lta_report_builder.png %})

{: start="7" }
7. Follow steps 7-9 on the [Report Builder](https://www.braze.com/docs/user_guide/analytics/reporting/report_builder) page.

{% alert note %}
Send feedback to your customer success manager or provide it after selecting the **Send Feedback** button.
{% endalert %}