---
nav_title: "User profile attributes"
article_title: User attribute views in Snowflake
page_order: 10
page_type: partner
search_tag: Partner
toc_headers: h2
---

# User profile attributes

> This page serves as a reference for the default and custom attribute views in Snowflake. There are three views for default attributes and three views for custom attributes, each designed for a specific use case with its own performance considerations.

## Data parity with the dashboard

In rare circumstances, default and custom attribute values in the Snowflake views on this page may not match what you see on a user's profile in the Braze dashboard.

For example, an attribute may appear as `NULL` in Snowflake while the dashboard shows a value for that user.

If you see widespread mismatches, contact your customer success manager or Braze Support.

## Available views

<table aria-label="Available views">
  <caption>Available views</caption>
  <thead>
    <tr>
      <th>Type</th>
      <th>View</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">Default attribute</td>
      <td><code>USER_DEFAULT_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>User profile snapshots</td>
    </tr>
    <tr>
      <td><code>USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>Real time user profiles</td>
    </tr>
    <tr>
      <td><code>USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED</code></td>
      <td>Historical change logs</td>
    </tr>
    <tr>
      <td rowspan="3">Custom attribute</td>
      <td><code>USER_CUSTOM_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>User profile snapshots</td>
    </tr>
    <tr>
      <td><code>USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED</code></td>
      <td>Real time user profiles</td>
    </tr>
    <tr>
      <td><code>USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED</code></td>
      <td>Historical change logs</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Available views" }

## User profile snapshots

These views provide periodic snapshots of user profile attributes. The data is delayed by up to 12 hours, making it useful for queries that don't require real-time updates.

 - `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`
 - `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`

### Usage

* Provides a snapshot of user attributes with up to a **12-hour delay**.
* Performs well for queries that don't require real-time accuracy.
* Faster query execution, particularly when filtering on attributes other than `USER_ID`.
* **Limitation:** Data is not up to date in real time.

{% include partners/snowflake_user_attributes_date_fields_note.md %}

### `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` schema

| Column name     | Data type     | Description |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Your Braze workspace identifier |
| `APP_ID` | VARCHAR | The specific app within your workspace |
| `USER_ID` | VARCHAR | The unique Braze user identifier |
| `TIME` | NUMBER | Unix timestamp (seconds) of the profile update |
| `TIME_MS` | NUMBER | Unix timestamp (milliseconds) of the profile update |
| `UPDATE_SOURCE` | VARCHAR | The source of the attribute update (API, SDK, dashboard, etc.) |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | When the data was last updated in Snowflake |
| `EXTERNAL_USER_ID` | VARCHAR | Your own user identifier (if set) |
| `FIRST_NAME` | VARCHAR | User's first name |
| `LAST_NAME` | VARCHAR | User's last name |
| `EMAIL_ADDRESS` | VARCHAR | User's email address |
| `GENDER` | VARCHAR | User's gender |
| `PHONE_NUMBER` | VARCHAR | User's phone number |
| `DOB` | VARCHAR | User's date of birth |
| `TIME_ZONE` | VARCHAR | User's timezone |
| `HOME_CITY` | VARCHAR | User's home city |
| `COUNTRY` | VARCHAR | User's country |
| `LANGUAGE` | VARCHAR | User's language preference |
| `ARCHIVED` | BOOLEAN | Whether the user profile is archived |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERDEFAULTATTRIBUTESVIEWSHARED schema" }


### `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED` schema

| Column name     | Data type     | Description |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Your Braze workspace identifier |
| `APP_ID` | VARCHAR | The specific app within your workspace |
| `USER_ID` | VARCHAR | The unique Braze user identifier |
| `EXTERNAL_USER_ID` | VARCHAR | Your own user identifier (if set) |
| `TIME` | NUMBER | Unix timestamp (seconds) of the profile update |
| `TIME_MS` | NUMBER | Unix timestamp (milliseconds) of the profile update |
| `UPDATE_SOURCE` | VARCHAR | The source of the attribute update (API, SDK, dashboard, etc.) |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | When the data was last updated in Snowflake |
| `CUSTOM_ATTRIBUTES` | VARIANT | JSON object containing all custom attributes (key-value pairs) |
| `ARCHIVED` | BOOLEAN | Whether the user profile is archived |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERCUSTOMATTRIBUTESVIEWSHARED schema" }

#### Working with CUSTOM_ATTRIBUTES

The `CUSTOM_ATTRIBUTES` column stores all your custom attributes as a JSON object. You can access individual attributes using Snowflake's JSON functions.

**Example: Querying specific custom attributes**

```sql
-- Get users with a specific loyalty tier
SELECT 
  USER_ID,
  EXTERNAL_USER_ID,
  CUSTOM_ATTRIBUTES:loyalty_tier::STRING as loyalty_tier,
  CUSTOM_ATTRIBUTES:points::NUMBER as points
FROM USER_CUSTOM_ATTRIBUTES_VIEW_SHARED
WHERE CUSTOM_ATTRIBUTES:loyalty_tier::STRING = 'gold';

-- Get users who made a purchase above a certain amount
SELECT 
  USER_ID,
  CUSTOM_ATTRIBUTES:last_purchase_amount::NUMBER as last_purchase_amount
FROM USER_CUSTOM_ATTRIBUTES_VIEW_SHARED
WHERE CUSTOM_ATTRIBUTES:last_purchase_amount::NUMBER > 100;
```

**Example: Analyzing custom attribute data**

```sql
-- Count users by subscription status
SELECT 
  CUSTOM_ATTRIBUTES:subscription_status::STRING as subscription_status,
  COUNT(*) as user_count
FROM USER_CUSTOM_ATTRIBUTES_VIEW_SHARED
GROUP BY CUSTOM_ATTRIBUTES:subscription_status::STRING;

-- Find average order value by customer segment
SELECT 
  CUSTOM_ATTRIBUTES:customer_segment::STRING as segment,
  AVG(CUSTOM_ATTRIBUTES:lifetime_value::NUMBER) as avg_lifetime_value
FROM USER_CUSTOM_ATTRIBUTES_VIEW_SHARED
WHERE CUSTOM_ATTRIBUTES:customer_segment IS NOT NULL
GROUP BY CUSTOM_ATTRIBUTES:customer_segment::STRING;
```

## Real time user profile views

These views provide near real-time updates on user profile attributes, with data delayed by up to 10 minutes after an update occurs in Braze.

  - `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`
  - `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED`

### Usage

* Provides up-to-date user attributes with minimal delay (~10 minutes).
* Useful for real-time analysis and scenarios where recent data is required.
* **Performance considerations:**
    * Queries on individual users are faster (under a minute using a large warehouse).
    * Queries without USER_ID filters require aggregation across all users, leading to significantly longer execution times.
    * Queries on a large dataset (such as over 100 million users) may take many minutes.

{% include partners/snowflake_user_attributes_date_fields_note.md %}

### `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` schema

| Column name     | Data type     | Description |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Your Braze workspace identifier |
| `APP_ID` | VARCHAR | The specific app within your workspace |
| `USER_ID` | VARCHAR | The unique Braze user identifier |
| `TIME` | NUMBER | Unix timestamp (seconds) of the profile update |
| `TIME_MS` | NUMBER | Unix timestamp (milliseconds) of the profile update |
| `UPDATE_SOURCE` | VARCHAR | The source of the attribute update (API, SDK, dashboard, etc.) |
| `ARCHIVED` | BOOLEAN | Whether the user profile is archived |
| `SF_UPDATED_AT` | TIMESTAMP_LTZ | When the data was last updated in Snowflake |
| `EXTERNAL_USER_ID` | VARCHAR | Your own user identifier (if set) |
| `FIRST_NAME` | VARCHAR | User's first name |
| `LAST_NAME` | VARCHAR | User's last name |
| `EMAIL_ADDRESS` | VARCHAR | User's email address |
| `GENDER` | VARCHAR | User's gender |
| `PHONE_NUMBER` | VARCHAR | User's phone number |
| `DOB` | VARCHAR | User's date of birth |
| `HOME_CITY` | VARCHAR | User's home city |
| `COUNTRY` | VARCHAR | User's country |
| `LANGUAGE` | VARCHAR | User's language preference |
| `TIME_ZONE` | VARCHAR | User's timezone |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERLATESTSTATEDEFAULTATTRIBUTESVIEWSHARED schema" }

### `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` schema

| Column name     | Data type     | Description |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Your Braze workspace identifier |
| `USER_ID` | VARCHAR | The unique Braze user identifier |
| `EXTERNAL_USER_ID` | VARCHAR | Your own user identifier (if set) |
| `TIME` | NUMBER | Unix timestamp (seconds) of the profile update |
| `TIME_MS` | NUMBER | Unix timestamp (milliseconds) of the profile update |
| `UPDATE_SOURCE` | VARCHAR | The source of the attribute update (API, SDK, dashboard, etc.) |
| `ARCHIVED` | BOOLEAN | Whether the user profile is archived |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | When the data was last updated in Snowflake |
| `APP_ID` | VARCHAR | The specific app within your workspace |
| `CUSTOM_ATTRIBUTES` | OBJECT | JSON object containing all custom attributes (key-value pairs) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERLATESTSTATECUSTOMATTRIBUTEVIEWSHARED schema" }

{% alert note %}
This view uses `OBJECT` type for `CUSTOM_ATTRIBUTES` instead of `VARIANT`. Use the same JSON accessor syntax (`:attribute_name::TYPE`) to query individual attributes.
{% endalert %}

## Historical change logs

These views store historical change logs of user attributes, capturing changes with a 12-hour granularity.

- `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`
- `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`

### Usage

* Provides a record of historical changes to user attributes for a rolling 6 month period.
* Data is snapshotted every 12 hours, meaning multiple updates in this window are combined into a single record. Individual changes within this period are not separately retained.
* `EFF_DT` and `END_DT` mark the start and end of a user’s attribute state.

{% include partners/snowflake_user_attributes_date_fields_note.md %}

### `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` schema

| Column name     | Data type     | Description |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Your Braze workspace identifier |
| `USER_ID` | VARCHAR | The unique Braze user identifier |
| `APP_ID` | VARCHAR | The specific app within your workspace |
| `TIME` | NUMBER | Unix timestamp (seconds) of the profile update |
| `TIME_MS` | NUMBER | Unix timestamp (milliseconds) of the profile update |
| `UPDATE_SOURCE` | VARCHAR | The source of the attribute update (API, SDK, dashboard, etc.) |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | When the data was last updated in Snowflake |
| `EXTERNAL_USER_ID` | VARCHAR | Your own user identifier (if set) |
| `FIRST_NAME` | VARCHAR | User's first name |
| `LAST_NAME` | VARCHAR | User's last name |
| `EMAIL_ADDRESS` | VARCHAR | User's email address |
| `GENDER` | VARCHAR | User's gender |
| `PHONE_NUMBER` | VARCHAR | User's phone number |
| `DOB` | VARCHAR | User's date of birth |
| `TIME_ZONE` | VARCHAR | User's timezone |
| `HOME_CITY` | VARCHAR | User's home city |
| `COUNTRY` | VARCHAR | User's country |
| `LANGUAGE` | VARCHAR | User's language preference |
| `EFF_DT` | TIMESTAMP_NTZ | Effective date: when this attribute state began |
| `END_DT` | TIMESTAMP_NTZ | End date: when this attribute state ended (NULL for current state) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERDEFAULTATTRIBUTESHISTORYVIEWSHARED schema" }

### `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED` schema

| Column name     | Data type     | Description |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Your Braze workspace identifier |
| `USER_ID` | VARCHAR | The unique Braze user identifier |
| `APP_ID` | VARCHAR | The specific app within your workspace |
| `EXTERNAL_USER_ID` | VARCHAR | Your own user identifier (if set) |
| `TIME` | NUMBER | Unix timestamp (seconds) of the profile update |
| `TIME_MS` | NUMBER | Unix timestamp (milliseconds) of the profile update |
| `UPDATE_SOURCE` | VARCHAR | The source of the attribute update (API, SDK, dashboard, etc.) |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | When the data was last updated in Snowflake |
| `CUSTOM_ATTRIBUTES` | VARIANT | JSON object containing all custom attributes (key-value pairs) |
| `ARCHIVED` | BOOLEAN | Whether the user profile is archived |
| `EFF_DT` | TIMESTAMP_NTZ | Effective date: when this attribute state began |
| `END_DT` | TIMESTAMP_NTZ | End date: when this attribute state ended (NULL for current state) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERCUSTOMATTRIBUTESHISTORYVIEWSHARED schema" }

## Common use cases

### Building user segments

```sql
-- Find active users in a specific city who haven't received an email recently
SELECT 
  d.EXTERNAL_USER_ID,
  d.EMAIL_ADDRESS,
  d.HOME_CITY,
  c.CUSTOM_ATTRIBUTES:last_email_sent::TIMESTAMP as last_email_sent
FROM USER_DEFAULT_ATTRIBUTES_VIEW_SHARED d
JOIN USER_CUSTOM_ATTRIBUTES_VIEW_SHARED c 
  ON d.USER_ID = c.USER_ID
WHERE d.HOME_CITY = 'New York'
  AND d.EMAIL_ADDRESS IS NOT NULL
  AND (c.CUSTOM_ATTRIBUTES:last_email_sent::TIMESTAMP < DATEADD(day, -30, CURRENT_TIMESTAMP())
       OR c.CUSTOM_ATTRIBUTES:last_email_sent IS NULL);
```

### Analyzing user behavior over time

```sql
-- Track how a user's loyalty tier changed over the past 6 months
SELECT 
  USER_ID,
  CUSTOM_ATTRIBUTES:loyalty_tier::STRING as loyalty_tier,
  EFF_DT,
  END_DT
FROM USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED
WHERE USER_ID = 'user_123'
  AND EFF_DT >= DATEADD(month, -6, CURRENT_TIMESTAMP())
ORDER BY EFF_DT DESC;
```

### Combining default and custom attributes

```sql
-- Get a complete user profile with both default and custom attributes
SELECT 
  d.EXTERNAL_USER_ID,
  d.FIRST_NAME,
  d.LAST_NAME,
  d.EMAIL_ADDRESS,
  d.COUNTRY,
  c.CUSTOM_ATTRIBUTES:subscription_status::STRING as subscription_status,
  c.CUSTOM_ATTRIBUTES:lifetime_value::NUMBER as lifetime_value,
  c.CUSTOM_ATTRIBUTES:last_purchase_date::DATE as last_purchase_date
FROM USER_DEFAULT_ATTRIBUTES_VIEW_SHARED d
LEFT JOIN USER_CUSTOM_ATTRIBUTES_VIEW_SHARED c 
  ON d.USER_ID = c.USER_ID
WHERE d.EXTERNAL_USER_ID = 'customer_456';
```

### Finding high-value customers

```sql
-- Identify users with high lifetime value who are at risk of churning
SELECT 
  d.EXTERNAL_USER_ID,
  d.EMAIL_ADDRESS,
  c.CUSTOM_ATTRIBUTES:lifetime_value::NUMBER as lifetime_value,
  c.CUSTOM_ATTRIBUTES:days_since_last_purchase::NUMBER as days_since_last_purchase
FROM USER_DEFAULT_ATTRIBUTES_VIEW_SHARED d
JOIN USER_CUSTOM_ATTRIBUTES_VIEW_SHARED c 
  ON d.USER_ID = c.USER_ID
WHERE c.CUSTOM_ATTRIBUTES:lifetime_value::NUMBER > 1000
  AND c.CUSTOM_ATTRIBUTES:days_since_last_purchase::NUMBER > 90
ORDER BY c.CUSTOM_ATTRIBUTES:lifetime_value::NUMBER DESC;
```

## Best practices

### Recommended query usage

| Use case                                               | Recommended views                                   | Notes                                                                 |
|--------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------------------------|
| **General queries** that do not require recent updates | `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` and `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`               | Fast execution, with data up to 12 hours old.                          |
| Queries requiring the **latest user attributes**       | `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` and `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` | Provides near real-time updates but can be slower for large datasets. |
| **Historical tracking** of attribute changes           | `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` and `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`      | Stores attribute changes with 12-hour granularity.                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Recommended query usage" }

### Performance considerations

* Queries on `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` or `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED` should return in under 10 seconds for large datasets (~1 billion users) on a large warehouse.
* Queries on `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` or `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED ` for a single user return in under a minute but scale poorly without `USER_ID` filtering.
* Queries on over 100 million users in `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` or `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` may take several minutes due to per-user aggregation.
