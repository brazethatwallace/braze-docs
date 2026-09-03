---
# This file is a template consumed by the external `braze-currents-generate-docs` tool
# (braze-agent-plugins / braze-currents plugin) to generate the Currents event glossary
# docs. It is not referenced from within braze-docs, so do not delete it as "unused".
nav_title: Customer behavior and user events
article_title: Customer behavior and user events
layout: customer_behavior_events_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "This glossary lists the various Customer Behavior and User Events that Braze can track and send to chosen Data Warehouses using Currents."
tool: Currents
search_rank: 7
---

<div class="api-glossary-preamble" markdown="1">

{% details Schema scope and related resources %}

Storage schemas apply to the flat file event data we send to data warehouse storage partners (Google Cloud Storage, Amazon S3, and Microsoft Azure Blob Storage). Some event and destination combinations listed here are not yet generally available. For information on which events are supported by various partners, refer to our list of [available partners]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) and check their respective pages.

{% alert tip %}
These events are also available as SQL tables in the [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder), [SQL Segment Extensions]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments), and [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake). For SQL table schemas and column details, refer to the [SQL table reference]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables).
{% endalert %}

Contact your Braze representative or open a [support ticket]({{site.baseurl}}/user_guide/administer/personal/braze_support) if you need access to additional event entitlements. If you can't find what you need on this page, check out our [Message Engagement Events Library]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) or our [Currents sample data examples](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% enddetails %}

{% details Explanation of customer behavior and user event structure and platform values %}

## Event structure

This customer behavior and user events breakdown shows what type of information is generally included in a customer behavior or user event. With a solid understanding of its components, your developers and business intelligence strategy team can use the incoming Currents event data to make data-driven reports and charts, and take advantage of other valuable data metrics.

![Breakdown of a user event showing a purchase event with the listed properties grouped by user-specific properties, behavior-specific properties, and device-specific properties]({% image_buster /assets/img/customer_engagement_event.png %})

Customer behavior and user events are comprised of **user-specific** properties, **behavior-specific** properties, and **device-specific** properties.

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

{% details Considerations for customer behavior and user events %}

- Currents drops events with excessively large payloads of greater than 900&nbsp;KB.
- Many of the events in this glossary are SDK-initiated. Some events, such as `token_state_change`, can be initiated by either the SDK or the backend (for example, in response to a push bounce). The `sdk_version`, `gender`, `language`, and `country` fields are only set for SDK-initiated events; for backend-initiated events, or when that information is not available or not set for the user, these fields may be `null`.

{% enddetails %}

</div>

<!--overview-end-->
