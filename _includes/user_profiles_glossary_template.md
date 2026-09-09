---
nav_title: User Profiles
layout: user_profiles_event_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "This glossary lists the user profile updates that Braze can track and send to chosen Data Warehouses using Currents."
tool: Currents
search_rank: 7
---

<div class="api-glossary-preamble" markdown="1">

{% alert tip %}
These events are also available as SQL tables in the [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder), [SQL Segment Extensions]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments), and [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake). For SQL table schemas and column details, refer to the [SQL table reference]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables). For Snowflake Data Sharing schemas for user profile attribute views, refer to [User profile attributes]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes).
{% endalert %}

Contact your Braze representative or open a [support ticket]({{site.baseurl}}/user_guide/administer/personal/braze_support) if you need access to additional event entitlements. If you can't find what you need on this page, see the [Customer Behavior Events Library]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events), [Message Engagement Events Library]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events), or [Currents sample data examples](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explanation of user profile update event structure %}

### Event structure

This customer behavior and user events breakdown shows what type of information is generally included in a user profile update event. With a solid understanding of its components, your developers and business intelligence strategy team can use the incoming Currents event data to make data-driven reports and charts, and take advantage of other valuable data metrics.

{% alert important %}
Storage schemas apply to flat file event data sent to data warehouse storage partners, such as Google Cloud Storage, Amazon S3, and Microsoft Azure Blob Storage. Some event and destination combinations listed here are not yet generally available. For information about supported events by partner, see [available partners]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) and the related partner pages.

Currents drops events with payloads larger than 900 KB.
{% endalert %}

{% enddetails %}

</div>

<!--overview-end-->
