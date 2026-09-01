---
nav_title: Segment analytics tracking
article_title: Segment analytics tracking
page_order: 3
page_type: reference
description: "This reference article covers segment analytics tracking and how to view revenue and purchases over time, sessions over time, and custom events over time."
tool: 
  - Segments
  - Reports
---

# Segment analytics tracking

> When analytics tracking is turned on for a segment, you can view sessions, custom events, and revenue over time for that segment.

If you don't turn analytics tracking on for a segment, you can still access [real-time statistics]({{site.baseurl}}/user_guide/audience/segments/segment_data#segment-statistics) for that segment and target its users with campaigns. The only difference is whether you can access the specific analysis tools mentioned on this page.

## Turning on segment analytics

In a segment's page **Segment Details** section, turn on **Analytics Tracking**.

![Analytics tracking toggle for a segment]({% image_buster /assets/img_archive/A_Tracking_2.png %})

A workspace can have tracking turned on for up to 25 segments. Braze recommends tracking segments that are important for you to analyze when understanding your campaigns' effects on sessions, revenue, and purchases.

{% alert note %}
After enabling analytics tracking, expect a delay before the segment data populates in your reports. If the data doesn't populate within 24 hours, [contact Support]({{site.baseurl}}/user_guide/administer/personal/braze_support).
{% endalert %}

## Viewing revenue and purchases over time

Go to **Analytics** > **Revenue Report** to view data on [revenue and purchases over time for this segment]({{site.baseurl}}/user_guide/analytics/reports/revenue_report).

Revenue and purchase charts reflect activity recorded after analytics tracking is turned on for that segment. Turning tracking on does not backfill earlier purchases into those reports. When you compare segments, use only time ranges where tracking was enabled for each segment you select.

![Revenue data by segment]({% image_buster /assets/img_archive/Revenue.png %})

To visually compare segment data for any custom time range, add or remove segments from the graph. Select **By Segment** in the **Breakdown** dropdown, and then select your segments in **Breakdown values**.

Select any segment name in the graph legend to turn on or off visibility for that segment's metrics.

![Revenue for multiple segments]({% image_buster /assets/img_archive/segment_revenue_multiple.png %})

## Sessions over time

Similarly, you can find data on [sessions over time for this particular segment]({{site.baseurl}}/user_guide/analytics/dashboards/home) on the **Home** page.

![Session data by segment]({% image_buster /assets/img_archive/events_over_time2.png %})

## View custom events over time

View data on [Custom events over time for segments]({{site.baseurl}}/user_guide/data/activation/events/custom_events#analytics) by going to **Analytics** > **Custom events report**.

## Using Query Builder templates

When analytics tracking is turned on, you can use Query Builder report templates to break down performance metrics for campaigns, Canvas, variants, and steps by segments. To learn more, check out [Segment data]({{site.baseurl}}/user_guide/audience/segments/segment_data#viewing-performance-data-by-segment).

## Frequently asked questions

### What should I check if analytics tracking looks wrong or empty?

Confirm **Analytics Tracking** is still enabled in **Segment Details**, you have not exceeded the per-workspace limit (25 segments with tracking), and wait up to 24 hours for data to populate after you first enable tracking. If issues continue, verify the segment definition and report date range, then [contact Support]({{site.baseurl}}/user_guide/administer/personal/braze_support).

