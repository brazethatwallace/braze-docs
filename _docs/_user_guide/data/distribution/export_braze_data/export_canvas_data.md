---
nav_title: Canvas data
article_title: Export Canvas Data
page_order: 3
page_type: reference
description: "This reference article covers how to export Canvas analytics."
tool: 
  - Canvas
  - Reports

---

# Export Canvas data

> User data can be exported to a CSV. This page covers how to export data for your entire Canvas or a specific Canvas component.

## Exporting data for a Canvas

To export data for a Canvas, do the following:

1. Go to **Messaging** > **Canvas** and select your Canvas.
2. Select the **User Data** dropdown in the **Canvas Details** section. 
3. Select one of the following export options:
  - **CSV Export User Data** or
  - **CSV Export Email Address**.

You can also export user data for all the entrants of a Canvas as a CSV file.

## Export users who entered or re-entered a Canvas

When [re-eligibility]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) is enabled, users can enter the same Canvas more than once. The **CSV Export User Data** option on the Canvas details page exports users who entered the Canvas, but it doesn't include how many times each user entered or each entry timestamp.

To analyze when users entered or re-entered a Canvas, use one of the following options:

- **Most recent entry per user:** Export a segment with the [`canvases_received`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) field using the [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) endpoint. For each Canvas, the export includes `last_entered` and `last_exited` timestamps for that user. The `canvases_received` field contains data from the last 90 days.
- **Every entry, including re-entries:** Use [Canvas Entry events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#canvas-entry-events) in Braze Currents or Snowflake Data Sharing. Each `users.canvas.Entry` event represents one Canvas entry and includes a `time` timestamp. Count events per user to determine how many times they entered.
- **Build a user list in the dashboard:** Create a segment with an **Entered Canvas Variation** filter, then export the segment to CSV. See [Canvas troubleshooting]({{site.baseurl}}/user_guide/messaging/canvas/troubleshooting#user-didnt-enter-the-canvas).

{% alert note %}
If you don't have Currents integrated and need every historical entry timestamp, contact your Braze customer success manager.
{% endalert %}

For a specific Canvas step in the original workflow, use **CSV Export User Data** on the step's details page.

## Exporting data for a component (original workflow only)

Canvas results can be exported on an individual component basis for the original Canvas workflow. To do this, select the specific component, then select the **User Data** dropdown in the **Canvas Step Details** page. 

![User Data dropdown on the Canvas Details page.]({% image_buster /assets/img/canvas_csv_export.png %})

{% alert tip %}
For help with CSV and API exports, visit our [export troubleshooting]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting) article.
{% endalert %}

