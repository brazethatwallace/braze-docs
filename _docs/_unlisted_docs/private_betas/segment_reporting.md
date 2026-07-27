---
nav_title: Segment reporting
article_title: Segment reporting in Report Builder
permalink: /segment_reporting_report_builder/
description: "This reference article covers segment as a reporting dimension in Report Builder, including how to report on segments, break down by segment, and which combinations are supported."
hidden: true
noindex: true
page_type: reference
---

# Segment reporting in Report Builder

> This article discusses how to use segments as a reporting dimension in Report Builder, including how to report on segments, break down by segment, and which combinations are supported.

{% multi_lang_include alerts/early_access_beta_alert.md feature='Segment reporting' contact='customer success manager' %}

Report Builder supports **Segments** in rows and as a drilldown option, so you can see how your segments are performing and break down campaign or Canvas performance by segment membership. If **Segments** doesn't appear in your **Rows** or **Drilldown** dropdowns, this feature hasn't been enabled for your account.

You can answer questions like:

- How is a specific segment performing over time?  
- Which campaigns and Canvases are targeting a given segment, and how did each perform?  
- How does engagement compare across segments for a single campaign or Canvas?

{% alert note %}
Segment reporting is only available for segments with [analytics tracking]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking) enabled. To select **Segments** in the **Rows** dropdown, you need the workspace-level ["View Dashboard Reports" permission]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).
{% endalert %}

## Report on segments

To report on segments directly:

1. Go to **Analytics** > **Report Builder (New)**.  
2. Select **Create New Report**.  
3. In the **Rows** dropdown, select **Segments**.  
4. (Optional) Select **Add drilldown** to break the segment data down further:  
   - **Campaigns and Canvases:** See which campaigns and Canvases targeted the segment, and how each performed.  
   - **Date:** See how a segment's size or performance trends over time. Pair with a line chart to visualize the trend.  
5. In **Report content**, open the **Segments** dropdown and select segments to add to your report.   
6. Select metrics in **Columns** > **Customize Metrics**, then set your date range in **Report content**.
7. If you added a **Campaigns and Canvases** drilldown, add the campaigns and Canvases to include in the report.
8. Select **Save and run**.

For the full Report Builder workflow, see [Creating a report]({{site.baseurl}}/user_guide/analytics/reports/report_builder#creating-a-report).

## Drill down by segment

To drill down campaign, Canvas, or channel reports by segment:

1. In the **Rows** dropdown, select **Campaigns**, **Canvases**, or **Campaigns and Canvases**.  
2. Select **Add drilldown**, and choose **Segment**.  
3. In **Report content**, open the **Segments** dropdown and select segments to add to your report.
4. Select metrics in **Columns** > **Customize Metrics**, then set your date range in **Report content**.   
5. Add the campaigns or Canvases to include in the report.
6. Select **Save and run** to see performance broken out by each segment your campaigns or Canvases targeted.

This is especially useful for accounts that send the same campaign or Canvas to multiple segments. You can see how each segment responded without manually cross-referencing segment membership and campaign performance.

## Supported combinations

The following **Rows** and **Drilldown** combinations are supported for segment reporting:

| Rows | Drilldown |
| ----- | ----- |
| Segment | Campaigns and Canvases |
| Segment | Date |
| Campaign | Segment |
| Campaign | Variant |
| Canvas | Segment |
| Campaigns and Canvases | Segment |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Supported rows and drilldown combinations"}

{% alert note %}
Report Builder supports one drilldown at a time. If you select **Campaigns** in the **Rows** dropdown, you can drill down by **Variant** or **Segment**, but not both on the same report.
{% endalert %}

## Metrics availability

Not all Report Builder metrics are available when you report on segments. Which metrics you can select also depends on whether **Segments** is in **Rows** or **Drilldown**, and whether the report includes a campaign or Canvas dimension.

| Metric | Availability |
| ----- | ----- |
| Channel and general messaging metrics | Available for supported rows and drilldown combinations. |
| Conversion counts (Conversions A–D) and conversion event names | Available when segment and campaign or Canvas dimensions appear together. Use **Segments** in rows with a **Campaigns and Canvases** drilldown; or use **Campaigns**, **Canvases**, or **Campaigns and Canvases** in rows with a **Segment** drilldown. |
| Revenue and conversion rate | Not available for segment-dimensioned reports. |
| Segment purchase revenue and count | Available only when **Segments** is in rows. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Segment reporting metrics availability"}

For more on how your rows and drilldown selections affect metrics, see [Metrics availability]({{site.baseurl}}/user_guide/analytics/reports/report_builder#metrics-availability) in Report Builder.