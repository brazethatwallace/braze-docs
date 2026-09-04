---
nav_title: SQL editor
article_title: "Cloud Data Ingestion: SQL editor"
description: "Learn how to create and validate Cloud Data Ingestion syncs with SQL queries."
page_order: 11
page_type: reference
toc_headers: h2
---

# Cloud Data Ingestion: SQL Editor

> This page covers how to use Braze Cloud Data Ingestion (CDI) SQL Editor to create and validate syncs with SQL queries.

Cloud Data Ingestion's SQL Editor lets you create syncs by writing SQL queries directly against your data warehouse. This removes the need to create or maintain a dedicated CDI table, which was previously required in [Step 1.1 of Data Warehouse Integrations]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views).

Use the SQL Editor when you want to:

- Sync data without modifying upstream tables
- Work with raw data in your warehouse
- Avoid constructing a `PAYLOAD` column
- Handle more complex data use cases with SQL

## Prerequisites and limitations

The SQL Editor has the following limitations:

- Available for data warehouse sources only: Snowflake, Redshift, BigQuery, Databricks, and Fabric.
- Only single statement, read-only queries are supported.

{% alert note %}
Braze runs only read-only queries against your data and does not modify your underlying tables. Temporary objects may be created during query execution but are not persisted.
{% endalert %}

## Create a new SQL Editor sync

Follow these steps to create source first, then a sync with SQL Editor. If you've already set up a source for CDI, you can skip to Step 3.

{% alert note %}
Note that these steps use a Snowflake source as an example. The setup process for other data warehouse sources is similar and can be found in [Step 2: Create a new source in Braze dashboard]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-2-create-a-new-source-in-the-braze-dashboard) of the [Setting up data warehouse integrations]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#setting-up-data-warehouse-integrations) documentation.
{% endalert %}

### Step 1: Set up your Snowflake role, permissions, warehouse, and user

Before creating your Snowflake source in CDI, make sure the Snowflake user Braze uses has access to the data you want to query and a warehouse to run queries.

#### Step 1.1: (Optional) Create a database and schema

If needed, create a dedicated database and schema for your CDI data:

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```

#### Step 1.2: Set up role and database permissions

Grant access to the tables you want to sync:

```sql
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.MY_USER_TABLE TO ROLE BRAZE_INGESTION_ROLE;
```

You can also grant access to multiple or future tables, depending on your use case. For example, to grant access to all future tables in a schema:

```sql
GRANT SELECT ON FUTURE TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
```

#### Step 1.3: Set up the warehouse and grant access to the Braze role

Create a warehouse for Braze to run queries:

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
The warehouse needs to have the auto-resume flag on. If not, grant Braze additional `OPERATE` privileges on the warehouse so Braze can turn it on when the query runs.
{% endalert %}

#### Step 1.4: Create a Snowflake user

Create a user for Braze and assign the role:

```sql
CREATE USER BRAZE_INGESTION_USER;
GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

You use this user when you configure your Snowflake source in Braze.

### Step 2: Create a new source in the Braze dashboard

In this step, create your Snowflake source in Braze and validate the connection.

#### Step 2.1: Add a Snowflake source

1. In the Braze dashboard, go to **Data Settings** > **Cloud Data Ingestion** > **Sources**.
2. Select **Add data source**.
3. Select **Snowflake**.

#### Step 2.2: Enter connection details

Choose a name for your source and enter your Snowflake credentials and configuration.

{% alert note %}
For the **Snowflake Account Locator** field, enter your Snowflake [account identifier](https://docs.snowflake.com/en/user-guide/admin-account-identifier), which typically follows a format like `xy12345.us-east-1.aws`. This is not the same as a database name or warehouse name.
{% endalert %}

#### Step 2.3: Complete RSA key setup

After entering your credentials and configuration, select **Save credentials** and generate an RSA key. Then go back to Snowflake to complete setup. Add the public key shown in the dashboard to the user you created for Braze to connect to Snowflake.

For additional information, see [Snowflake key-pair authentication](https://docs.snowflake.com/en/user-guide/key-pair-auth). If you want to rotate keys at any point, Braze can generate a new key pair and provide the new public key.

```sql
ALTER USER BRAZE_INGESTION_USER SET RSA_PUBLIC_KEY='MIIBIjANBgkqhkiG9w0BA...';
```

Back in Braze, select **Test connection** to verify source access, and then create the source.

### Step 3: Create a new sync and write your SQL query

1. Go to **Data Settings** > **Cloud Data Ingestion** > **Syncs**.
2. Select **Create data sync**.
3. Choose any sync under **Data Type**.
4. Reference the source from Step 2.
5. Select **SQL** and write a SQL query that returns user data from your warehouse. Your SQL query defines the data that syncs to Braze. The query result becomes the schema for your sync.

You can use the Source Explorer to browse for available tables and views to sync from, or the AI SQL generator to get Braze Operator's help on your SQL query.

{% alert note %}
Only read-only queries are supported, including `JOIN` clauses. For more details, see [SQL constraints](#sql-constraints).
{% endalert %}

### Step 4: Preview and validate your query

Select **Preview and validate** to run your query.

The preview:

- Displays results in a table format
- Shows up to 100 rows
- Shows up to 250 columns

To successfully validate, your SQL query must return various required columns:

| Sync data type | Required columns |
|---|---|
| Attributes | - A user identifier, one of `external_id`, `braze_id`, `alias_name` and `alias_label`, email or phone number.<br>- `UPDATED_AT`.<br>- At least one additional column (attribute) to sync. |
| Delete Users | - A user identifier, one of `external_id`, `braze_id`, `alias_name` and `alias_label`, email or phone number.<br>- `UPDATED_AT`. |
| Canvas Triggers | - A user identifier, one of `external_id`, `braze_id`, `alias_name` and `alias_label`, email or phone number.<br>- `UPDATED_AT`. |
| Custom Events | - A user identifier, one of `external_id`, `braze_id`, `alias_name` and `alias_label`, email or phone number.<br>- `UPDATED_AT`.<br>- `NAME` to represent the event name.<br>- `TIME` to represent the event time. If unavailable, CDI uses `UPDATED_AT` as a substitute. |
| Purchase Events | - A user identifier, one of `external_id`, `braze_id`, `alias_name` and `alias_label`, email or phone number.<br>- `UPDATED_AT`.<br>- `PRODUCT_ID`.<br>- `CURRENCY`.<br>- `PRICE`.<br>- `TIME` to represent the purchase event time. If unavailable, CDI uses `UPDATED_AT` as a substitute. |
| Catalog | - `ID` to represent the catalog item identifier.<br>- `UPDATED_AT`.<br>- At least one additional column (catalog field) to sync. |
| Accounts | - `ID` to represent the account identifier.<br>- `NAME` to represent the account name.<br>- `UPDATED_AT`.<br>- At least one additional column (account field) to sync. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 4: Preview and validate your query" }

Additional columns outside of required columns are synced as attributes, Canvas context properties, event properties, catalog fields, and account fields, respectively. See [Validation behavior](#validation-behavior) and [Troubleshooting](#troubleshooting) for helpful tips about preview and validate errors and how to fix them.

### Step 5: Review attribute mapping and create sync

When the validation succeeds, continue to **Next: Notifications** and create your sync.

{% alert important %}
Inaccurate SQL configuration can lead to unintended results, including the overconsumption of data points and broader operational risks. You are responsible for ensuring your query logic is correct and should carefully preview all results before activating a sync.
{% endalert %}

## SQL constraints {#sql-constraints}

### Use `SELECT` queries only

Only read-only queries are supported.

You can use:

- `SELECT`
- `WITH` (CTEs)
- `JOIN`

You can't use:

- `INSERT`, `UPDATE`, or `DELETE`
- `CREATE` or `DROP`
- Multiple statements separated by `;`

### Use a single statement

Your query must be a single executable statement.

## Validation behavior {#validation-behavior}

The SQL Editor validates your query before allowing you to proceed.

### SQL errors

If your query contains syntax errors:

- Validation fails
- No preview appears
- Your warehouse returns an error message

### Compilation errors

If your query references invalid tables, columns, or unauthorized objects:

- Validation fails
- No preview appears
- Your warehouse returns an error message

### Connection errors

If Braze can't connect to your warehouse:

- Validation fails
- No preview appears
- A connection error message appears

### Query timeout

If your query runs too long:

- Braze terminates the query
- Validation fails
- A timeout error appears

### Table schema errors

If your query compiles, validation may still fail if:

- No identifier column is found
- `UPDATED_AT` is missing
- Other required columns are missing

In this case, the preview still appears to help you move toward a successful validation. See [Step 4 in the previous section](#step-4-preview-and-validate-your-query) for details on required columns for each sync data type.

### Zero-row results

If your query returns zero rows:

- Validation **passes**
- You can still create the sync
- No users are updated until rows are returned

## PAYLOAD support (legacy)

SQL Editor supports [legacy CDI tables]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations?tab=snowflake#step-1-set-up-tables-or-views) where a `PAYLOAD` column is present.

If your query includes:

- A valid identifier
- `UPDATED_AT`
- A `PAYLOAD` column
- Additional columns

Then:

- Braze syncs only the `PAYLOAD` column
- Braze ignores additional columns

## Edit a SQL sync

When editing an existing sync:

- Any SQL change requires revalidation
- You can't save invalid changes
- Valid changes take effect after you save

If a sync run is already in progress, your changes take effect on the next run.

## Troubleshooting {#troubleshooting}

This section includes common errors and guidance on how to troubleshoot them.

### "No preview available"

When you see "No preview available", one of the following underlying error types may be causing it.

| Error type | Steps to resolve |
|---|---|
| "No preview available" | Read the error banner for hints. |
| "Unable to connect to the source" | Check the configured username, account locator, and RSA key-pair authentication setup.<br>Verify the warehouse is running.<br>Confirm network access. |
| "SQL syntax error" | Check your SQL syntax. |
| "Object does not exist or not authorized" | Make sure the role has `SELECT` access to the table.<br>Confirm database and schema permissions.<br>Check table name typos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="&quot;No preview available&quot;" }

### "Identity column required"

Make sure your query includes a valid identifier, such as `external_id`.

### "`UPDATED_AT` column is missing"

Add a timestamp column for incremental syncing.

### "Add more columns... There are no attributes/catalog fields/account fields to sync"

Add at least one additional column beyond the identifier and `UPDATED_AT`.

### "Query execution timed out"

Optimize your query or use a larger warehouse.
