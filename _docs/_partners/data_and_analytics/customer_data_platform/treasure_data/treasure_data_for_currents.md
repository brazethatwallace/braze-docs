---
nav_title: Treasure Data for Currents
article_title: Treasure Data for Currents
description: "This reference article outlines the partnership between Braze Currents and Treasure Data, an enterprise customer data platform that streams Braze event data into Treasure Data for analysis and activation."
page_type: partner
tool: Currents
alias: /partners/treasure_data_for_currents/
search_tag: Partner
---


# Treasure Data for Currents

> [Treasure Data](https://www.treasuredata.com/) is a customer data platform (CDP) that collects and routes information from multiple sources to a variety of other locations in your marketing stack.

The Braze and Treasure Data integration lets you control the flow of information between the two systems. With Currents, you can stream Braze event data into Treasure Data and make it actionable across your growth stack.

The recommended method is the **Braze Currents Streaming** connector in Treasure Data, paired with a **Custom Currents Export** in Braze. This approach provides:

- Real-time event streaming from Braze into Treasure Data
- Optional automatic table routing by event type
- A flat, SQL-queryable schema that doesn't require JSON parsing

{% alert important %}
The Braze Currents Streaming connector is in beta. Contact Treasure Data support to enable it on your Treasure Data account. For partner-side setup details, see Treasure Data's [Braze Currents Import Integration](https://docs.treasuredata.com/int/braze-currents-import-integration).
{% endalert %}

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Treasure Data account | An active [Treasure Data account](https://console.treasuredata.com) is required to take advantage of this partnership. |
| Currents | To export data to Treasure Data, you need [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/#how-to-access-currents) set up for your account. |
| Braze Currents Streaming connector | Contact Treasure Data support to enable the Braze Currents Streaming connector (beta) on your Treasure Data account. |
| Treasure Data Write API key | A Treasure Data Write API key authenticates the inbound stream from Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integration

### Step 1: Configure the connector in Treasure Data

1. In the Treasure Data console, go to **Connections** > **New Connection**.
2. Select **Braze Currents Streaming**.
3. Under **Authentication**, enter your Treasure Data Write API key.
4. Under **Source Settings**, configure the following:

| Field | Description |
| ----- | ----------- |
| Source Name | A descriptive name for this connection |
| Datastore | Select **Plazma** |
| Database | The Treasure Data database where events are stored |
| Table | The default destination table |
| Multiple Tables | Select to route each Braze event type to its own table |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Source settings" }

5. After you've saved, copy the **Unique ID** (`task_id`). You need this value in the next step.

### Step 2: Create a Custom Currents Export in Braze

The **Treasure Data Export** option in the Braze Currents UI uses the legacy Postback API method and is no longer recommended. Use **Custom Currents Export** instead.

1. In Braze, go to **Partner Integrations** > **Data Export**.
2. Select **Create New Current** > **Custom Currents Export**.
3. Enter an integration name and a contact email for error notifications.
4. Under **Credentials**, enter the endpoint URL for your Treasure Data region. Enter your Treasure Data Write API key as the **Bearer Token**.

| Region | Endpoint URL |
| ------ | ------------ |
| US | `https://braze-in-streaming.treasuredata.com/v1/task/{TASK_ID}` |
| EU | `https://braze-in-streaming.eu01.treasuredata.com/v1/task/{TASK_ID}` |
| AP02 | `https://braze-in-streaming.ap02.treasuredata.com/v1/task/{TASK_ID}` |
| Tokyo | `https://braze-in-streaming.treasuredata.co.jp/task/v1/{TASK_ID}` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Endpoint URLs by region" }

Replace `{TASK_ID}` with the Unique ID you copied in [Step 1](#step-1-configure-the-connector-in-treasure-data).

5. Select the event types you want to export. Custom Currents connections can send events for identified users and for users without an `external_user_id`. Treasure Data ingests both.
6. Select **Launch Current**.

{% alert warning %}
Keep your Treasure Data Write API key and endpoint URL up to date. If the endpoint is unreachable for more than **5&nbsp;days**, Braze drops the connector's events and the data is permanently lost.
{% endalert %}

## Query your data

After events are flowing, query them with SQL. Treasure Data flattens the payload, so you don't need to parse JSON.

```sql
SELECT
  id AS event_id,
  event_type,
  user_external_user_id,
  properties_campaign_name,
  properties_email_address,
  time
FROM your_database.your_table
WHERE TD_INTERVAL(time, '-1d', 'JST')
```

{% alert note %}
The `time` field in Treasure Data is the timestamp when Treasure Data received and processed the event, not the original event occurrence time in Braze.
{% endalert %}

If you selected **Multiple Tables**, each event type lands in its own table (for example, `users_message_email_open` or `users_behaviors_purchase`).

To confirm data is arriving, run a count query a few minutes after you launch the Current:

```sql
SELECT COUNT(*)
FROM your_table
WHERE TD_INTERVAL(time, '-1h')
```

## Data schema

Treasure Data flattens nested JSON up to two levels deep:

| JSON type | Treasure Data column type |
| --------- | ------------------------- |
| string | string |
| number | long |
| boolean | string |
| array | JSON string |
| object (level 1) | `field_name` |
| object (level 2) | `parent_field_name_field_name` |
| null | omitted |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Data type mapping" }

Column names use lowercase letters and underscores only.

## Limits

| Item | Limit |
| ---- | ----- |
| Maximum payload size | 1&nbsp;MB per request |
| Batch size | 100 events per batch (default) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Limits" }

## Integration details

Braze supports exporting all data listed in the [Currents event glossaries]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) to Treasure Data. That includes all properties in both [message engagement]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) and [customer behavior]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) events.

The payload structure for exported data matches the payload structure for custom HTTP connectors. You can review sample payloads in the [examples repository for custom HTTP connectors](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors).

## Migrate from the legacy Postback method

If you previously used **Treasure Data Export** (Postback) in Braze:

1. Complete the Custom Currents Export setup in this article.
2. Confirm events are flowing to the new table.
3. Disable the old Postback-based Current in Braze.

Legacy data stored as raw JSON arrays can still be queried with `JSON_PARSE` and `UNNEST`. New data ingested through the streaming connector uses the flat schema described in [Data schema](#data-schema).
