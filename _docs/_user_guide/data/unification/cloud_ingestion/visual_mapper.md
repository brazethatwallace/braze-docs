---
nav_title: Visual mapper
article_title: "Cloud Data Ingestion: Visual mapper"
description: "Learn how to sync a table or view from your data warehouse with Cloud Data Ingestion's visual mapper, without writing SQL."
page_order: 12
page_type: reference
toc_headers: h2
---

# Cloud Data Ingestion: Visual mapper

> This page covers how to use the visual mapper to sync a table or view from your data warehouse to Braze without writing SQL or restructuring your data.

{% alert important %}
The visual mapper is currently in beta. The visual mapper is available for user attribute syncs from all Cloud Data Ingestion data warehouse sources, and additional sync types become available throughout the beta. Contact your customer success manager or account manager for access.
{% endalert %}

With the visual mapper, you can sync an existing table or view from your data warehouse without writing SQL or restructuring your data. Instead of creating a Braze-specific table with `EXTERNAL_ID`, `UPDATED_AT`, and `PAYLOAD` columns, you map your existing table's columns to Braze fields directly in the dashboard.

## Prerequisites

Before you create a sync with the visual mapper, you'll need:

- An active Cloud Data Ingestion data warehouse source. If you haven't set one up, see [Data warehouse integrations]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations).
- The name of the table or view you want to sync, as it appears in your data warehouse.
- A column in your table that contains a supported user identifier, and a column with a timestamp Braze can use for incremental syncing.

{% alert note %}
Braze runs only read-only queries against your data and does not modify your underlying tables. Temporary objects may be created during query execution but are not persisted.
{% endalert %}

## Creating a sync with the visual mapper

### Step 1: Configure the sync

1. Go to **Data Settings** > **Cloud Data Ingestion** > **Syncs**, then select **Create data sync**.
2. Choose a name for your sync and select an active data source. Only active sources can be used.
3. For **Data destination**, select **Braze Data Platform**.
4. For **Data Type**, select **User Attributes**.
5. Select **Next: Data definition**.

### Step 2: Map your source schema

1. On the **Data definition** step, select **Visual mapper**.
2. In the **Table** field, enter the table or view name as it appears in your data warehouse.
3. Select **Map source schema**. Braze reads the schema of your table or view and lists every column with its detected data type.

### Step 3: Review your mappings

The **Review mapping** section tracks two required mappings. Your sync can't be created until both are complete:

- Map one column to a supported user identifier: `external_id`, `braze_id`, `email`, `phone`, or a user alias. Identifier options appear under **Identifiers** in the destination field dropdown.
- Map one column to `updated_at`. Braze uses this timestamp for incremental syncing on recurring syncs, where each sync run imports rows where `updated_at` is later than the last synced value.

For each remaining column, you can:

- **Keep the default mapping.** Each column maps to a Braze field of the same name. If the field doesn't exist in your workspace yet, it's marked **New attribute** and is created during the sync's first run.
- **Map to an existing field.** Search the destination field dropdown to map a column to an existing default or custom attribute in your workspace.
- **Map to a new field.** Type directly in the destination field dropdown to map a column to a new custom attribute.
- **Exclude the column.** Clear the **Import** checkbox to leave a column out of the sync.

{% alert tip %}
Before creating a new attribute, search the destination dropdown for an existing one. For example, if your table has a `fav_color` column but your workspace already tracks `favorite_color`, consider mapping `fav_color` to `favorite_color` instead of creating another attribute.
{% endalert %}

{% alert note %}
Fields whose data type doesn't match your column's detected type show a **Type mismatch** warning. You can still proceed, but mismatched values may fail to sync as row errors. You can view row errors in a sync's run details.
{% endalert %}

### Step 4: Preview and validate

Select **Preview and validate** to run a read-only check against your table or view. The preview shows the first 10 rows using your mapped field names, and only includes columns you're importing.

### Step 5: Finish creating the sync

1. On the **Notifications** step, enter at least one contact email for sync error notifications. You can optionally turn on **Row Error** alerts (sent when a percentage of rows fail to update) and **Sync success** notifications.
2. On the **Schedule** step, turn on **Recurring sync** to run the sync on a schedule, or leave it off for a one-time sync.
3. Review the **Summary** step. It lists your configuration, which attributes are new versus existing, and any columns excluded from the import due to data type issues or your selections.
4. Select **Create sync**. You can also select **Save as draft** at any step to finish later.

## Handling schema changes

The visual mapper checks the schema of your table or view on every sync run and responds based on the type of change:

| Change in your source table | Sync behavior |
|---|---|
| A new column is added | The sync continues but new columns are not synced automatically. To include one, edit the sync and map it. |
| A mapped column is removed | The sync run fails and the sync is paused. The schema change is shown in the sync's run details, and your notification contacts receive an email alert. |
| A mapped column is renamed | Treated as a removed column plus a new column. |
| A column's data type changes | Not detected as a schema change. Incompatible values are reported as row errors in the sync logs. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Handling schema changes" }

To resume a paused sync after a column is removed, select **Edit sync** and review your mappings. The removed column is flagged and no longer appears in the mapper. Saving your mappings confirms the sync should continue without that column. Alternatively, if the data moved to a different column, map the new column before saving.

## Frequently asked questions

### Can I edit my mappings after a sync is created?

Yes. Edit the sync and select **View and edit mapping**. The current schema of the source table loads, with your previous mappings from creating the sync saved. You can edit your mappings from there.

### Can I transform my data in the visual mapper?

No. The visual mapper syncs column values exactly as they appear in your source. It doesn't support transformations, conditional logic, or joins across tables. For those use cases, use the SQL option on the Data definition step to shape your data with a query instead. For more information, see [Cloud Data Ingestion: SQL Editor]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sql_editor).

### Do my existing CDI syncs change?

No. Syncs using the existing table format with `EXTERNAL_ID`, `UPDATED_AT`, and `PAYLOAD` columns continue to work, and you can still create them by selecting **Table** on the **Data definition** step. No migration is required.

### How is my Braze usage affected?

Each column you import writes as an attribute update, and data point billing works the same as other CDI user data syncs. Excluding columns you don't need keeps your syncs efficient. For more information, see [Cloud Data Ingestion best practices]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices).
