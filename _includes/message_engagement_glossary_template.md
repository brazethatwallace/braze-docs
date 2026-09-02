---
# This file is a template consumed by the external `braze-currents-generate-docs` tool
# (braze-agent-plugins / braze-currents plugin) to generate the Currents event glossary
# docs. It is not referenced from within braze-docs, so do not delete it as "unused".
nav_title: Message engagement events
layout: message_engagement_events_glossary
alias: /message_events_glossary/
page_order: 5
excerpt_separator: ""
page_type: glossary
description: "This glossary lists the various Message Engagement Events that Braze can track and send to chosen Data Warehouses using Currents."
tool: Currents
search_rank: 6
lazy_partner_tabs: true
---

<div class="api-glossary-preamble" markdown="1">

{% details Schema scope and related resources %}

Storage schemas apply to the flat file event data we send to Data Warehouse Storage partners (Google Cloud Storage, Amazon S3, and Microsoft Azure Blob Storage). For schemas that apply to the other partners, refer to our list of [available partners]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) and check their respective pages.

{% alert tip %}
These events are also available as SQL tables in the [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder), [SQL Segment Extensions]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments), and [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake). For SQL table schemas and column details, refer to the [SQL table reference]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables).
{% endalert %}

Contact your account manager or open a [support ticket]({{site.baseurl}}/user_guide/administer/personal/braze_support) if you need access to additional event entitlements. If you can't find what you need in this article, check out our [Customer Behavior Events Library]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) or our [Currents sample data examples](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% enddetails %}

{% details Explanation of message engagement event structure and platform values %}

## Event structure

This event breakdown shows what type of information is generally included in a message engagement event. With a solid understanding of its components, your developers and business intelligence strategy team can use the incoming Currents event data to make data-driven reports and charts, and take advantage of other valuable data metrics.

![Breakdown of a message engagement event showing an email unsubscribe event with the listed properties grouped by user-specific properties, campaign or Canvas tracking properties, and event-specific properties]({% image_buster /assets/img/message_engagement_event.png %}){: width="2300" height="770" style="max-width:100%;height:auto;"}

Message engagement events are comprised of **user-specific** properties, **campaign/canvas tracking** properties, and **event-specific** properties.

### User ID schema

Note the naming conventions for user IDs.

| Braze schema | Currents schema | Description |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | The unique identifier that is automatically assigned by Braze. |
| `external_id` | `"EXTERNAL_USER_ID"` | The unique identifier of a user's profile that is set by the customer. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="User ID schema" }

### Platform values

Certain events return a `platform` value that specifies the platform of the user's device.
<br>The following table details the possible returned values:

| User device | Platform value |
| --- | --- |
| iOS | `ios` |
| Android | `android` |
| FireTV | `kindle` |
| Kindle | `kindle` |
| Web | `web` |
| tvOS | `tvos` |
| Roku | `roku` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Platform values" }

{% enddetails %}

{% details Considerations for message engagement events %}

- Currents drops events with payloads greater than 900&nbsp;KB.
- Objects related to Canvas Flow have IDs you can use for grouping and translate to human-readable names through the [Export Canvas details endpoint]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details).
- Certain fields might not show their most recent state immediately after you update a campaign or Canvas:
  - `campaign_name`
  - `canvas_name`
  - `canvas_step_name`
  - `conversion_behavior`
  - `canvas_variation_name`
  - `experiment_split_name`
  - `message_variation_name`
- If you need complete consistency for these fields, wait one hour after the last update before you send messages to your users.

{% enddetails %}

</div>

<!--overview-end-->
