---
nav_title: "Delta Sharing"
article_title: Databricks Delta Sharing
page_order: 0
description: "This reference article covers Databricks Delta Sharing with Braze (closed beta), which allows you to access Braze engagement and campaign data in your Databricks account."
page_type: partner
search_tag: Partner
permalink: /delta_sharing/
hidden: true
---

# Databricks Delta Sharing

> Databricks [Delta Sharing](https://docs.databricks.com/en/delta-sharing/index.html) allows you to securely share live Braze engagement and campaign data into your Databricks environment. This article describes how sharing works from Braze as the data provider to your Databricks account as the recipient, and how to query shared tables.

{% alert important %}
Databricks Delta Sharing with Braze is in **closed beta**. Availability, supported regions, and product behavior can change. Contact your Braze customer success manager to participate or to confirm whether this feature is enabled for your workspace.
{% endalert %}

Databricks Delta Sharing is part of Braze Data Distribution. For a full overview of Data Distribution options, see [Data Distribution]({{site.baseurl}}/user_guide/data/distribution/).

## Set up Delta Sharing

For Databricks, data sharing happens between a data provider and a data recipient. Your Braze account is the **data provider** because it creates and sends the share, and your Databricks account is the **data recipient** because it consumes the share to create a catalog you can query. For more details, see Databricks documentation on [reading data shared using Databricks-to-Databricks Delta Sharing (for recipients)](https://docs.databricks.com/en/delta-sharing/read-data-databricks.html).

### Step 1: Configure sharing from Braze

1. In Braze, go to **Partner Integrations** > **Data Sharing** > **Databricks Delta Sharing**.
2. Enter your Databricks sharing identifier.
3. When you're finished, select **Create Datashare**. Braze sends the share to your Databricks account.

### Step 2: Create a catalog in Databricks

1. After a few minutes, you should receive the inbound share in your Databricks account.
2. Using the inbound share, create a catalog to view and query the tables. For example:
    {% raw %}
    ```sql
    CREATE CATALOG [IF NOT EXISTS] <catalog-name> USING SHARE braze.<share-name>;
    ```
    {% endraw %}
3. Grant privileges so the right users and groups can query the new catalog.

{% alert warning %}
Shared data is read-only in your Databricks workspace. You can query it like other data, but you can't modify or delete rows in the shared tables through the share.
{% endalert %}

## Usage and visualization

After the data share is provisioned, create a catalog from the incoming share so shared tables appear in your Databricks workspace and are queryable like other data you store there. The shared data remains read-only.

Similar to Currents, you can use Databricks Delta Sharing to:

{% multi_lang_include partners/data_sharing_use_cases.md %}

For a full list of tables and columns available in Databricks, [download the Databricks raw table schemas](/docs/assets/download_file/databricks-data-sharing-raw-table-schemas.txt) as a text file. This file reflects the Databricks Delta Sharing schema (for example, `DB_CREATED_AT` for ingestion time). It is not interchangeable with the [Snowflake raw table schemas](/docs/assets/download_file/data-sharing-raw-table-schemas.txt) or the [SQL table reference]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables/), which describe Snowflake naming and fields.

{% alert note %}
During the closed beta, not every table listed in the Databricks schema file may be available in your share. Column names and types can also differ from Snowflake Data Sharing (for example, `DB_CREATED_AT` instead of `SF_CREATED_AT`). Contact your Braze customer success manager if you need the current table list for your workspace.
{% endalert %}

### User ID schema

Note the following differences between Braze and Databricks naming conventions for user IDs.

| Braze schema | Databricks schema | Description |
| ----------- | ----------- | ----------- |
| `braze_id` | `USER_ID` | The unique identifier that Braze assigns automatically. |
| `external_id` | `EXTERNAL_USER_ID` | The unique identifier of a user's profile that you set in Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="User ID schema" }

## Important information and limitations

### Closed beta availability

During the closed beta, your share may not include every table in the [Databricks raw table schemas](/docs/assets/download_file/databricks-data-sharing-raw-table-schemas.txt) file. Shared data can also differ from Snowflake Data Sharing in column names and types. For example, Databricks shares use `DB_CREATED_AT` for ingestion time, while Snowflake shares use `SF_CREATED_AT`.

### Breaking versus non-breaking changes

#### Non-breaking changes

Non-breaking changes can happen at any time and generally provide additional functionality. Examples of non-breaking changes:

- Adding a new table or view
- Adding a column to an existing table or view

{% alert important %}
Because new columns are considered non-breaking, Braze strongly recommends explicitly listing the columns of interest in each query instead of using `SELECT *` queries. Alternatively, create views that explicitly name columns and query those views instead of querying the shared tables directly.
{% endalert %}

#### Breaking changes

When possible, breaking changes are preceded by an announcement and a migration period. Examples of breaking changes include:

- Removing a table or view
- Removing a column from an existing table or view
- Changing the type or nullability of an existing column

### Databricks regions

During the closed beta, supported cloud providers and regions can differ by workspace and rollout. Contact your Braze customer success manager for the options that apply to your account.

### Retention policy

During the closed beta, historical backfill beyond the standard retention window may be limited.

You can query against the most recent two years of data for each event in the corresponding `USERS_*_SHARED` view.

### General Data Protection Regulation (GDPR) compliance

{% multi_lang_include partners/snowflake_pii_gdpr.md %}

### Querying shared data: `TIME` and query performance

Event data in the data sharing views (for example, `USERS_BEHAVIORS_CUSTOMEVENT_SHARED`) is clustered on the `TIME` field. When you filter by when the event occurred, use `TIME` as the preferred filter. Queries that restrict rows using `TIME` are generally more performant than queries that filter on `DB_CREATED_AT`, because clustering aligns with event time.

| Field | Meaning |
| ----- | ------- |
| `TIME` | Unix timestamp at which the event happened. Prefer this when filtering by occurrence time. |
| `DB_CREATED_AT` | Timestamp when the row was loaded into Databricks (ingestion time). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Querying shared data: TIME and query performance" }

### Speed, performance, and cost of queries

The speed, performance, and cost of any query you run on top of the data depend on the SQL warehouse size you use. Depending on how much data you access, you may need a larger warehouse for the query to complete successfully. For more information, see Databricks documentation on [creating and configuring a SQL warehouse](https://docs.databricks.com/en/compute/sql-warehouse/create.html) (including cluster size and scaling).
