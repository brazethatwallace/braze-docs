---
hidden: true
article_title: Cloud Data Ingestion: SQL Editor (beta)
description: "Learn how to create and validate Cloud Data Ingestion syncs with SQL queries."
page_type: reference
toc_headers: h2
---

# Cloud Data Ingestion: SQL Editor (beta)

Cloud Data Ingestion's SQL Editor lets you create syncs by writing SQL queries directly against your data warehouse.

This removes the need to create or maintain a dedicated CDI table, which was previously required in [Step 1.1 of Data Warehouse Integrations]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=snowflake#step-1-set-up-tables-or-views).

Use the SQL Editor when you want to:

- Sync data without modifying upstream tables
- Work with raw data in your warehouse
- Avoid constructing a `PAYLOAD` column
- Handle more complex data use cases with SQL

{% alert important %}
Cloud Data Ingestion SQL Editor is in beta. Contact your customer success manager or account manager for access.
{% endalert %}

## Prerequisites and limitations

During beta, the SQL Editor has the following limitations:

- Available for **User Attributes** syncs only
- Supports one warehouse source: **Snowflake**

{% alert note %}
Braze runs read-only queries against your data and does not modify your underlying tables. Braze may create temporary objects during query execution, but it does not persist them.
{% endalert %}

## Create a new SQL Editor sync

Follow these steps to create a sync with SQL Editor. If you've already set up a Snowflake source for CDI, skip to Step 3.

### Step 1: Set up your Snowflake role, permissions, warehouse, and user

Before creating your Snowflake source in CDI, make sure the Snowflake user Braze uses has access to the data you want to query and a warehouse to run queries.

#### (Optional) Create a database and schema

If needed, create a dedicated database and schema for your CDI data:

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```

#### Set up role and database permissions

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

#### Set up the warehouse and grant access to the Braze role

Create a warehouse for Braze to run queries:

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
The warehouse must have auto-resume enabled. If it doesn't, grant Braze additional `OPERATE` privileges on the warehouse so Braze can turn it on when the query runs.
{% endalert %}

#### Create a Snowflake user

Create a user for Braze and assign the role:

```sql
CREATE USER BRAZE_INGESTION_USER;
GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

You use this user when you configure your Snowflake source in Braze.

### Step 2: Create a new source in the Braze dashboard

#### Add a Snowflake source

In the Braze dashboard, go to **Data Settings** > **Cloud Data Ingestion** > **Sources**, select **Add data source**, and then select **Snowflake**.

#### Enter connection details

Choose a name for your source and enter your Snowflake credentials and configuration.

{% alert note %}
For the **Snowflake Account Locator** field, enter your Snowflake [account identifier](https://docs.snowflake.com/en/user-guide/admin-account-identifier), which typically follows a format like `xy12345.us-east-1.aws`. This is not the same as a database name or warehouse name.
{% endalert %}

#### Complete RSA key setup

After entering your credentials and configuration, select **Save credentials** and generate an RSA key. Then go back to Snowflake to complete setup. Add the public key shown in the dashboard to the user you created for Braze to connect to Snowflake.

For additional information, see [Snowflake key-pair authentication](https://docs.snowflake.com/en/user-guide/key-pair-auth). If you want to rotate keys at any point, Braze can generate a new key pair and provide the new public key.

```sql
ALTER USER BRAZE_INGESTION_USER SET RSA_PUBLIC_KEY='MIIBIjANBgkqhkiG9w0BA...';
```

Back in Braze, select **Test connection** to verify source access, and then create the source.

### Step 3: Create a new sync and write your SQL query

Go to **Data Settings** > **Cloud Data Ingestion** > **Syncs**, and select **Create data sync**. Choose **User Attributes** under **Data Type**, then reference the Snowflake source from Step 2.

Select **SQL** and write a SQL query that returns user data from your warehouse. Your SQL query defines the data that syncs to Braze. The query result becomes the schema for your sync.

![The Create data sync flow showing SQL selected with a sample query in the SQL editor.]({% image_buster /assets/img/cloud_ingestion/sql-editor-image.png %}){: style="max-width:80%;"}

Your SQL query must return:

- A user identifier (`external_id`, `braze_id`, `alias_name` and `alias_label`, `email`, or `phone`)
- An `UPDATED_AT` column
- At least one additional column (attribute)

{% alert note %}
Only read-only queries are supported, including `JOIN` clauses. For more details, see [SQL constraints](#sql-constraints).
{% endalert %}

### Step 4: Preview and validate your query

Select **Preview and validate** to run your query.

The preview:

- Displays results in a table format
- Shows up to 100 rows
- Shows up to 250 columns

You must successfully preview and validate your query before continuing. For details about errors and fixes, see [Validation behavior](#validation-behavior) and [Troubleshooting](#troubleshooting).

### Step 5: Review attribute mapping and create sync

After validation:

- The identifier column matches users
- The `UPDATED_AT` column drives incremental syncing
- Braze syncs all other columns as attributes

When validation succeeds, continue to **Next: Notifications** and create your sync.

## SQL constraints {#sql-constraints}

Your query must meet the following requirements.

### Include a user identifier

Your query must include at least one of the following:

- `external_id`
- `braze_id`
- `email`
- `phone`
- `alias_name` and `alias_label`

If no valid identifier is detected, validation fails.

### Include `UPDATED_AT`

Your query must include an `UPDATED_AT` column (case-insensitive).

If it's missing, validation fails.

### Include at least one attribute column

Your query must include at least one column in addition to:

- The identifier
- `UPDATED_AT`

If not, validation fails.

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

### Missing required columns

If your query compiles, validation may still fail if:

- No identifier column is found
- `UPDATED_AT` is missing
- No attribute columns are present

In this case, the preview still appears to help you move toward a successful validation.

### Zero-row results

If your query returns zero rows:

- Validation **passes**
- You can still create the sync
- No users are updated until rows are returned

## PAYLOAD support (legacy)

SQL Editor supports [legacy CDI tables]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=snowflake#step-1-set-up-tables-or-views) where a `PAYLOAD` column is present.

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

### "No preview available"

- Read the error banner for hints
- "Unable to connect to the source"
  - Check the configured username, account locator, and RSA key-pair authentication setup
  - Verify the warehouse is running
  - Confirm network access
- "SQL syntax error"
  - Check your SQL syntax
- "Object does not exist or not authorized"
  - Make sure the role has `SELECT` access to the table
  - Confirm database and schema permissions
  - Check table name typos

### "Identity column required"

Make sure your query includes a valid identifier, such as `external_id`.

### "`UPDATED_AT` column is missing"

Add a timestamp column for incremental syncing.

### "No attributes to sync"

Add at least one additional column beyond the identifier and `UPDATED_AT`.

### "Query execution timed out"

Optimize your query or use a larger warehouse.
