---
nav_title: Order Placed SQLダッシュボード
article_title: ダッシュボードビルダーでeコマースのOrder Placedイベントをレポートする
page_order: 1
page_type: reference
description: "クエリビルダーのSQLをecommerce.order_placedイベントに使用して、eコマースレポート用のダッシュボードビルダーで売上と注文のタイルを作成します。"
tool: Reports
---

# ダッシュボードビルダーでeコマースのOrder Placedイベントをレポートする {#report-on-ecommerce-order-placed-events-in-dashboard-builder}

> `ecommerce.order_placed` 推奨イベントからカスタムの売上チャートや注文チャートを作成するには、クエリビルダーでSQLクエリを保存し、ダッシュボードビルダーで結果を可視化します。

## この例について {#about-this-example}

架空の衣料小売ブランドFlash and Threadは、[eコマース推奨イベント]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events)を使用して注文を記録しています。マーケティングチームは、プリビルトのラストタッチアトリビューションビューだけでなく、日次売上、平均注文額（AOV）、注文件数を1つのダッシュボードにまとめたいと考えています。

このパターンでは、クエリビルダーを使用してSnowflakeの共有イベントテーブルから `ecommerce.order_placed` をクエリし、保存したクエリをダッシュボードビルダーの**カスタムクエリ**タイルとして追加します。追加の指標（新規購入者とリピート購入者、商品カテゴリ、セグメント別売上など）についても同じワークフローを繰り返すことができます。

組み込みのeコマースダッシュボードが必要な指標の組み合わせをカバーしていない場合に使用してください。ラストタッチアトリビューション売上については、[Revenue - Last Touch Attribution]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder#revenue---last-touch-attribution)ダッシュボードを参照してください。

## 考慮事項 {#considerations}

- **イベントの実装:** クエリがデータを返すには、`ecommerce.order_placed` が実装され、`total_value`（および必要に応じて商品データ）を送信している必要があります。[Shopifyコネクター]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector)を使用している場合、推奨イベントはすでに利用可能な場合があります。
- **クエリビルダーへのアクセス:** クエリビルダーを使用するには、「View PII」[ユーザー権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)が必要です。
- **データ保持:** クエリビルダーはデフォルトで過去60日間のデータを返します。[Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)を使用すると、最大2年間の保持データをクエリできます。[クエリビルダー]({{site.baseurl}}/user_guide/analytics/reports/query_builder)を参照してください。
- **タイムアウト:** 6分以上実行されるクエリはタイムアウトします。レポートが失敗した場合は、日付範囲を狭めるか、`TIME` でフィルターするか、オーディエンスサイズを縮小してください。イベントテーブルは `TIME` でクラスタリングされているため、イベント発生時刻でのフィルタリングが推奨されます。
- **売上フィールド:** サンプルクエリはイベントの `properties` から `total_value` を合計します。Brazeの標準化されたeコマース売上は、プロダクトレポートでは各商品の `price` と `quantity` から算出されることが多いです。`total_value` を商品の明細と一致させるか、スキーマに合わせてSQLを調整してください。
- **列ラベル:** 表示列名はダブルクォーテーションで囲んでください（例: `"Date"`、`"Total Revenue"`）。これにより、ダッシュボードビルダーで読みやすい軸やテーブルヘッダーが表示されます。
- **テスト:** この記事のSQLは例として提供されています。ダッシュボードを広く共有する前に、ワークスペースでクエリを検証してください。

## 設定 {#setup}

### ステップ1:日次売上のSQLクエリを作成する {#step-1-create-a-sql-query-for-daily-revenue}

1. **Analytics** > **クエリビルダー**に移動します。
2. **SQLクエリを作成**を選択し、次に**SQLエディター**を選択します。
3. クエリに名前を付けます（例: `Flash Thread — daily eCommerce revenue`）。
4. 過去60日間の暦日ごとの合計売上について、以下のクエリを貼り付けて調整します。

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
5. **クエリを実行**を選択し、次に**保存**を選択します。

クエリビルダーの設定の詳細については、[クエリビルダーでレポートを実行する]({{site.baseurl}}/user_guide/analytics/reports/query_builder#running-reports-in-the-query-builder)を参照してください。

### ステップ2:クエリをダッシュボードビルダーのタイルに追加する {#step-2-add-the-query-to-a-dashboard-builder-tile}

1. **Analytics** > **ダッシュボードビルダー**に移動します。
2. **ダッシュボードを作成**を選択します（または既存のダッシュボードを開きます）。
3. データソースとして**カスタムクエリ**を選択します。
4. **+ タイルを追加**を選択し、ステップ1で保存したクエリを選択します。
5. 鉛筆アイコンを選択してタイルを編集します。
   - チャートタイプを**折れ線グラフ**に設定します。
   - **X軸**を `Date` に設定します。
   - **Y軸**を `Total Revenue` に設定します。
6. 必要に応じてタイルのサイズを変更し、**保存**を選択します。
7. **ダッシュボードを表示** > **ダッシュボードを実行**を選択します。

ダッシュボードの生成には数分かかる場合があります。[カスタムダッシュボードの作成]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder#creating-a-custom-dashboard)を参照してください。

### ステップ3:追加のOrder Placed指標を追加する（オプション） {#step-3-add-additional-_order-placed_-metrics-optional}

保存済みクエリを個別に作成し、それぞれを独自のタイルとして追加します（ダッシュボードあたり最大10タイル）。

#### 日次の平均注文額と注文件数 {#average-order-value-and-order-count-per-day}

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

X軸に `Date`、Y軸に両方の指標を設定した折れ線グラフまたは棒グラフを使用します（表示したくない列は選択を解除してください）。

#### 日次の新規購入者とリピート購入者 {#new-versus-returning-purchasers-per-day}

このパターンは、各ユーザーの最初の `ecommerce.order_placed` 日とそれ以降の購入日を比較します。クエリビルダーのウィンドウがレポート期間全体をカバーしている場合（例: デフォルトの60日間ウィンドウ）に最も正確です。

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

#### 注文明細からの商品カテゴリ {#product-category-from-order-line-items}

`products` 配列をフラット化し、カテゴリフィールドでフィルターします。異なる商品メタデータキーを使用している場合は、`metadata.category` を置き換えてください。

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

#### セグメント別の購入数と売上（セグメント分析） {#purchases-and-revenue-by-segment-segment-analytics}

これには、レポート対象のセグメントで[セグメント分析トラッキング]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking)が有効になっている必要があります。日付ピッカーには[SQL変数]({{site.baseurl}}/user_guide/analytics/reports/query_builder/sql_variables)を使用してください。

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

### その他の組み込みeコマースレポート {#other-built-in-ecommerce-reporting}

| レポート | 使用するタイミング |
| --- | --- |
| [Revenue - Last Touch Attribution]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder#revenue---last-touch-attribution) | キャンペーンまたはキャンバス別のラストタッチアトリビューション売上 |
| [カスタムイベントレポート]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report) | 推奨イベントのイベント件数と頻度 |
| キャンペーンまたはキャンバスのコンバージョン | `ecommerce.order_placed` が1次コンバージョンイベントの場合 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="その他の組み込みeコマースレポート" }

## 関連記事 {#related-articles}

- [eコマース推奨イベント]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events)
- [クエリビルダー]({{site.baseurl}}/user_guide/analytics/reports/query_builder)
- [クエリビルダーのSQL変数]({{site.baseurl}}/user_guide/analytics/reports/query_builder/sql_variables)
- [ダッシュボードビルダー]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder)
- [Revenue - Last Touch Attribution]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder#revenue---last-touch-attribution)
- [SQLテーブルリファレンス]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#USERS_BEHAVIORS_CUSTOMEVENT_SHARED)
- [セグメント分析トラッキング]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking)