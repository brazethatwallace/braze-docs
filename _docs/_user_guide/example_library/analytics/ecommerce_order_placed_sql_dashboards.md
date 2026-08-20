---
nav_title: Order Placed SQL dashboards
article_title: Report on eCommerce Order Placed events in Dashboard Builder
page_order: 1
page_type: reference
description: "Use Query Builder SQL on ecommerce.order_placed events to build revenue and order tiles in Dashboard Builder for eCommerce reporting."
tool: Reports
---

# Report on eCommerce Order Placed events in Dashboard Builder

> Build custom revenue and order charts from `ecommerce.order_placed` recommended events by saving SQL queries in Query Builder and visualizing the results in Dashboard Builder.

## About this example

Flash & Thread, a fictional clothing retail brand, logs orders with [eCommerce recommended events]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events/). Its marketing team wants daily revenue, average order value (AOV), and order volume in a single dashboard—not only the prebuilt last-touch attribution view.

This pattern uses Query Builder to query `ecommerce.order_placed` from Snowflake shared event tables, then adds the saved query as a **Custom Queries** tile in Dashboard Builder. You can repeat the workflow for additional metrics (new versus returning purchasers, product categories, or segment-level revenue).

Use this when built-in eCommerce dashboards do not cover your metric mix. For last-touch attributed revenue, see the [Revenue - Last Touch Attribution]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/#revenue---last-touch-attribution) dashboard instead.

## Considerations

- **Event implementation:** `ecommerce.order_placed` must be implemented and sending `total_value` (and product data when needed) before queries return data. If you use the [Shopify connector]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector), recommended events may already be available.
- **Query Builder access:** You need the "View PII" [user permission]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/) to use Query Builder.
- **Data retention:** Query Builder returns data from the past 60 days by default. With [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/), you may query up to two years of retained data. See [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder/).
- **Timeouts:** Queries that run longer than six minutes time out. Narrow the date range, filter on `TIME`, or reduce the audience size if a report fails. Event tables are clustered on `TIME`; prefer filtering on when the event occurred.
- **Revenue field:** Sample queries sum `total_value` from event `properties`. Braze's standardized eCommerce revenue in product reports often derives from each product's `price` and `quantity`. Align `total_value` with your product line items, or adjust SQL to match your schema.
- **Column labels:** Wrap display column names in double quotation marks (for example `"Date"`, `"Total Revenue"`) so Dashboard Builder shows readable axis and table headers.
- **Testing:** The SQL in this article is provided as an example. Validate queries in your workspace before you share dashboards broadly.

## Setup

### Step 1: Create a SQL query for daily revenue

1. Go to **Analytics** > **Query Builder**.
2. Select **Create SQL Query**, then **SQL Editor**.
3. Name the query (for example, `Flash Thread — daily eCommerce revenue`).
4. Paste and adapt the following query for total revenue per calendar day over the last 60 days:

{% raw %}
```sql
SELECT
  DATE_TRUNC('day', TO_TIMESTAMP_NTZ(TIME))::DATE AS "Date",
  SUM(PARSE_JSON(PROPERTIES):total_value::NUMBER(18, 2)) AS "Total Revenue"
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED
WHERE NAME = 'ecommerce.order_placed'
  AND TO_TIMESTAMP_NTZ(TIME) >= DATEADD(day, -60, CURRENT_TIMESTAMP())
  AND TO_TIMESTAMP_NTZ(TIME) <= CURRENT_TIMESTAMP()
GROUP BY 1
ORDER BY 1;
```
{% endraw %}

{:start="5"}
5. Select **Run Query**, then select **Save**.

For Query Builder setup details, see [Running reports in the Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder/#running-reports-in-the-query-builder).

### Step 2: Add the query to a Dashboard Builder tile

1. Go to **Analytics** > **Dashboard Builder**.
2. Select **Create Dashboard** (or open an existing dashboard).
3. For the data source, select **Custom Queries**.
4. Select **+ Add Tile**, then choose the query you saved in Step 1.
5. Select the pencil icon to edit the tile:
   - Set the chart type to **Line graph**.
   - Set **X-axis** to `Date`.
   - Set **Y-axis** to `Total Revenue`.
6. Resize the tile as needed, then select **Save**.
7. Select **View Dashboard** > **Run Dashboard**.

Dashboard generation can take a few minutes. See [Creating a custom dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/#creating-a-custom-dashboard).

### Step 3: Add additional _Order Placed_ metrics (optional)

Create separate saved queries, then add each as its own tile (up to 10 tiles per dashboard).

#### Average order value and order count per day

{% raw %}
```sql
SELECT
  DATE_TRUNC('day', TO_TIMESTAMP_NTZ(TIME))::DATE AS "Date",
  AVG(PARSE_JSON(PROPERTIES):total_value::NUMBER(18, 2)) AS "Average Order Value",
  COUNT(*) AS "No. of Orders"
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED
WHERE NAME = 'ecommerce.order_placed'
  AND TO_TIMESTAMP_NTZ(TIME) >= DATEADD(day, -60, CURRENT_TIMESTAMP())
  AND TO_TIMESTAMP_NTZ(TIME) <= CURRENT_TIMESTAMP()
GROUP BY 1
ORDER BY 1;
```
{% endraw %}

Use a line or bar chart with `Date` on the X-axis and both metrics on the Y-axis (deselect columns you do not want to display).

#### New versus returning purchasers per day

This pattern compares each user's first `ecommerce.order_placed` day to later purchase days. It is most accurate when your Query Builder window covers the full reporting period (for example, the default 60-day window).

{% raw %}
```sql
WITH order_days AS (
  SELECT DISTINCT
    USER_ID,
    DATE_TRUNC('day', TO_TIMESTAMP_NTZ(TIME))::DATE AS purchase_day
  FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED
  WHERE NAME = 'ecommerce.order_placed'
),
first_purchase AS (
  SELECT
    USER_ID,
    MIN(purchase_day) AS first_day
  FROM order_days
  GROUP BY USER_ID
),
per_day_purchasers AS (
  SELECT DISTINCT
    USER_ID,
    purchase_day
  FROM order_days
)
SELECT
  p.purchase_day AS "Date",
  COUNT(DISTINCT CASE
    WHEN f.first_day = p.purchase_day THEN p.USER_ID
  END) AS "New Purchasers",
  COUNT(DISTINCT CASE
    WHEN f.first_day < p.purchase_day THEN p.USER_ID
  END) AS "Returning Purchasers"
FROM per_day_purchasers AS p
INNER JOIN first_purchase AS f
  ON p.USER_ID = f.USER_ID
GROUP BY 1
ORDER BY 1;
```
{% endraw %}

#### Product category from order line items

Flatten the `products` array and filter on your category field. Replace `metadata.category` if you use a different product metadata key.

{% raw %}
```sql
SELECT
  f.value:metadata:category::STRING AS "Product Category",
  COUNT(*) AS "Line Items"
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED,
  LATERAL FLATTEN(INPUT => PARSE_JSON(PROPERTIES):products) f
WHERE NAME = 'ecommerce.order_placed'
  AND f.value:metadata:category::STRING IS NOT NULL
  AND TRIM(f.value:metadata:category::STRING) != ''
  AND LOWER(TRIM(f.value:metadata:category::STRING)) != 'undefined'
GROUP BY 1
ORDER BY 2 DESC;
```
{% endraw %}

#### Purchases and revenue by segment (segment analytics)

This requires [segment analytics tracking]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/) on the segments you report on. Use [SQL variables]({{site.baseurl}}/user_guide/analytics/reports/query_builder/sql_variables/) for date pickers.

{% raw %}
```sql
WITH event_conversions AS (
  SELECT
    user_id,
    time,
    TRY_CAST(GET_PATH(PARSE_JSON(PROPERTIES), 'total_value')::string AS FLOAT) AS price,
    id AS purchase_event_id,
    f.value::string AS user_segment_membership_id
  FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED,
    LATERAL FLATTEN(input => user_segment_membership_ids) AS f
  WHERE NAME = 'ecommerce.order_placed'
    AND time > {{start_date.${Start Date}}}
    AND time < {{end_date.${End Date}}}
)
SELECT
  user_segment_membership_id AS "Segment Analytics Id",
  COUNT(DISTINCT purchase_event_id) AS "Total Purchases",
  ROUND(SUM(price), 2) AS "Total Revenue"
FROM event_conversions
GROUP BY 1
ORDER BY 3 DESC;
```
{% endraw %}

### Other built-in eCommerce reporting

| Report | Use when |
| --- | --- |
| [Revenue - Last Touch Attribution]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/#revenue---last-touch-attribution) | Last-touch attributed revenue by campaign or Canvas |
| [Custom events report]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report/) | Event volume and frequency for recommended events |
| Campaign or Canvas conversions | `ecommerce.order_placed` is the primary conversion event |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Other built-in eCommerce reporting" }

## Related articles

- [eCommerce recommended events]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events/)
- [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder/)
- [SQL variables in Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder/sql_variables/)
- [Dashboard Builder]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/)
- [Revenue - Last Touch Attribution]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/#revenue---last-touch-attribution)
- [SQL table reference]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables/#USERS_BEHAVIORS_CUSTOMEVENT_SHARED)
- [Segment analytics tracking]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/)
