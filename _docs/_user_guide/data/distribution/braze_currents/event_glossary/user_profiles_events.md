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

{% alert important %}
User profile events are in beta. Contact your customer success manager or account manager for access.
{% endalert %}

{% alert tip %}
These events are also available as SQL tables in the [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder), [SQL Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments), and [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake). For SQL table schemas and column details, refer to the [SQL table reference]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/sql_segments/sql_segments_tables). For Snowflake Data Sharing schemas for user profile attribute views, refer to [User profile attributes]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes).
{% endalert %}

Contact your Braze representative or open a [support ticket]({{site.baseurl}}/braze_support) if you need access to additional event entitlements. If you can't find what you need on this page, see the [Customer Behavior Events Library]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events), [Message Engagement Events Library]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events), or [Currents sample data examples](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explanation of user profile update event structure %}

### Event structure

This customer behavior and user events breakdown shows what type of information is generally included in a user profile update event. With a solid understanding of its components, your developers and business intelligence strategy team can use the incoming Currents event data to make data-driven reports and charts, and take advantage of other valuable data metrics.

{% alert important %}
Storage schemas apply to flat file event data sent to data warehouse storage partners, such as Google Cloud Storage, Amazon S3, and Microsoft Azure Blob Storage. Some event and destination combinations listed here are not yet generally available. For information about supported events by partner, see [available partners]({{site.baseurl}}/user_guide/data/braze_currents/available_partners) and the related partner pages.

Currents drops events with payloads larger than 900 KB.
{% endalert %}

{% enddetails %}

</div>

<!--overview-end-->

{% api %}
## User Profile Update events {#user-profile-update-events}

{% apitags %}
Profile
{% endapitags %}

This represents the profile updates for a user.

{% tabs %}
{% tab Cloud Storage %}
```json
// users.profile.Update

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "archived" : "(optional, boolean) When set to True, indicates that this user was archived within Braze",
  "country" : "(optional, string) [PII] Country of the user",
  "custom_attributes" : "(optional, string) Valid JSON string of the updated custom attributes",
  "dob" : "(optional, string) [PII] Date of birth of the user in format \"YYYY-MM-DD\"",
  "email_address" : "(optional, string) [PII] Email address of the user",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "first_name" : "(optional, string) [PII] First name of the user",
  "gender" : "(optional, string) [PII] Gender of the user, one of ['M', 'F', 'O', 'N', 'P']",
  "home_city" : "(optional, string) [PII] Home city of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "language" : "(optional, string) [PII] Language of the user",
  "last_name" : "(optional, string) [PII] Last name of the user",
  "phone_number" : "(optional, string) [PII] Phone number of the user in e.164 format",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "time_ms" : "(required, long) Time in milliseconds when the update happened",
  "timezone" : "(optional, string) Time zone of the user",
  "update_source" : "(required, string) The source of this update",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}
