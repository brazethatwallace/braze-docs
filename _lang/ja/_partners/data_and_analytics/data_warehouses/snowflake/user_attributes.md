---
nav_title: "ユーザープロファイル属性"
article_title: Snowflakeのユーザー属性ビュー
page_order: 10
page_type: partner
search_tag: Partner
toc_headers: h2
---

# ユーザープロファイル属性 {#user-profile-attributes}

> このページは、Snowflakeのデフォルトおよびカスタム属性ビューのリファレンスです。デフォルト属性用に3つのビュー、カスタム属性用に3つのビューがあり、それぞれ固有のパフォーマンス上の考慮事項を持つ特定のユースケース向けに設計されています。

## ダッシュボードとのデータ整合性 {#data-parity-with-the-dashboard}

まれに、このページのSnowflakeビューにおけるデフォルトおよびカスタム属性の値が、Brazeダッシュボードのユーザープロファイルに表示される内容と一致しない場合があります。

たとえば、ダッシュボードではそのユーザーに値が表示されているにもかかわらず、Snowflakeでは属性が`NULL`と表示される場合があります。

広範な不一致が見られる場合は、カスタマーサクセスマネージャーまたはBrazeサポートにお問い合わせください。

## 利用可能なビュー {#available-views}

<table aria-label="利用可能なビュー">
  <caption>利用可能なビュー</caption>
  <thead>
    <tr>
      <th>タイプ</th>
      <th>ビュー</th>
      <th>説明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">デフォルト属性</td>
      <td><code>USER_DEFAULT_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>ユーザープロファイルスナップショット</td>
    </tr>
    <tr>
      <td><code>USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>リアルタイムユーザープロファイル</td>
    </tr>
    <tr>
      <td><code>USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED</code></td>
      <td>変更履歴ログ</td>
    </tr>
    <tr>
      <td rowspan="3">カスタム属性</td>
      <td><code>USER_CUSTOM_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>ユーザープロファイルスナップショット</td>
    </tr>
    <tr>
      <td><code>USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED</code></td>
      <td>リアルタイムユーザープロファイル</td>
    </tr>
    <tr>
      <td><code>USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED</code></td>
      <td>変更履歴ログ</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Available views" }

## ユーザープロファイルスナップショット {#user-profile-snapshots}

これらのビューは、ユーザープロファイル属性の定期的なスナップショットを提供します。データは最大12時間遅延するため、リアルタイムの更新を必要としないクエリに適しています。

 - `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`
 - `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`

### 使用方法 {#usage}

* 最大**12時間の遅延**を伴うユーザー属性のスナップショットを提供します。
* リアルタイムの正確性を必要としないクエリに適しています。
* 特に`USER_ID`以外の属性でフィルタリングする場合、クエリの実行が高速です。
* **制限事項:** データはリアルタイムで更新されません。

{% include partners/snowflake_user_attributes_date_fields_note.md %}

### `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`スキーマ {#user_default_attributes_view_shared-schema}

| 列名     | データタイプ     | 説明 |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Brazeワークスペースの識別子 |
| `APP_ID` | VARCHAR | ワークスペース内の特定のアプリ |
| `USER_ID` | VARCHAR | Brazeの一意のユーザー識別子 |
| `TIME` | NUMBER | プロファイル更新のUnixタイムスタンプ（秒） |
| `TIME_MS` | NUMBER | プロファイル更新のUnixタイムスタンプ（ミリ秒） |
| `UPDATE_SOURCE` | VARCHAR | 属性更新のソース（API、SDK、ダッシュボードなど） |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Snowflakeでデータが最後に更新された日時 |
| `EXTERNAL_USER_ID` | VARCHAR | 独自のユーザー識別子（設定されている場合） |
| `FIRST_NAME` | VARCHAR | ユーザーの名 |
| `LAST_NAME` | VARCHAR | ユーザーの姓 |
| `EMAIL_ADDRESS` | VARCHAR | ユーザーのメールアドレス |
| `GENDER` | VARCHAR | ユーザーの性別 |
| `PHONE_NUMBER` | VARCHAR | ユーザーの電話番号 |
| `DOB` | VARCHAR | ユーザーの生年月日 |
| `TIME_ZONE` | VARCHAR | ユーザーのタイムゾーン |
| `HOME_CITY` | VARCHAR | ユーザーの居住都市 |
| `COUNTRY` | VARCHAR | ユーザーの国 |
| `LANGUAGE` | VARCHAR | ユーザーの言語設定 |
| `ARCHIVED` | BOOLEAN | ユーザープロファイルがアーカイブされているかどうか |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERDEFAULTATTRIBUTESVIEWSHARED schema" }


### `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`スキーマ {#user_custom_attributes_view_shared-schema}

| 列名     | データタイプ     | 説明 |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Brazeワークスペースの識別子 |
| `APP_ID` | VARCHAR | ワークスペース内の特定のアプリ |
| `USER_ID` | VARCHAR | Brazeの一意のユーザー識別子 |
| `EXTERNAL_USER_ID` | VARCHAR | 独自のユーザー識別子（設定されている場合） |
| `TIME` | NUMBER | プロファイル更新のUnixタイムスタンプ（秒） |
| `TIME_MS` | NUMBER | プロファイル更新のUnixタイムスタンプ（ミリ秒） |
| `UPDATE_SOURCE` | VARCHAR | 属性更新のソース（API、SDK、ダッシュボードなど） |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Snowflakeでデータが最後に更新された日時 |
| `CUSTOM_ATTRIBUTES` | VARIANT | すべてのカスタム属性を含むJSONオブジェクト（キーと値のペア） |
| `ARCHIVED` | BOOLEAN | ユーザープロファイルがアーカイブされているかどうか |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERCUSTOMATTRIBUTESVIEWSHARED schema" }

#### CUSTOM_ATTRIBUTESの操作 {#working-with-custom_attributes}

`CUSTOM_ATTRIBUTES`列は、すべてのカスタム属性をJSONオブジェクトとして格納します。SnowflakeのJSON関数を使用して個々の属性にアクセスできます。

**例: 特定のカスタム属性のクエリ**

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

**例: カスタム属性データの分析**

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

## リアルタイムユーザープロファイルビュー {#real-time-user-profile-views}

これらのビューは、ユーザープロファイル属性のほぼリアルタイムの更新を提供します。データはBrazeで更新が行われてから最大10分遅延します。

  - `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`
  - `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED`

### 使用方法

* 最小限の遅延（約10分）で最新のユーザー属性を提供します。
* リアルタイム分析や最新のデータが必要なシナリオに適しています。
* **パフォーマンスに関する考慮事項:**
    * 個々のユーザーに対するクエリは高速です（大規模なウェアハウスを使用して1分以内）。
    * USER_IDフィルターを使用しないクエリは全ユーザーの集計が必要となるため、実行時間が大幅に長くなります。
    * 大規模なデータセット（1億人以上のユーザーなど）に対するクエリは数分かかる場合があります。

{% include partners/snowflake_user_attributes_date_fields_note.md %}

### `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`スキーマ {#user_latest_state_default_attributes_view_shared-schema}

| 列名     | データタイプ     | 説明 |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Brazeワークスペースの識別子 |
| `APP_ID` | VARCHAR | ワークスペース内の特定のアプリ |
| `USER_ID` | VARCHAR | Brazeの一意のユーザー識別子 |
| `TIME` | NUMBER | プロファイル更新のUnixタイムスタンプ（秒） |
| `TIME_MS` | NUMBER | プロファイル更新のUnixタイムスタンプ（ミリ秒） |
| `UPDATE_SOURCE` | VARCHAR | 属性更新のソース（API、SDK、ダッシュボードなど） |
| `ARCHIVED` | BOOLEAN | ユーザープロファイルがアーカイブされているかどうか |
| `SF_UPDATED_AT` | TIMESTAMP_LTZ | Snowflakeでデータが最後に更新された日時 |
| `EXTERNAL_USER_ID` | VARCHAR | 独自のユーザー識別子（設定されている場合） |
| `FIRST_NAME` | VARCHAR | ユーザーの名 |
| `LAST_NAME` | VARCHAR | ユーザーの姓 |
| `EMAIL_ADDRESS` | VARCHAR | ユーザーのメールアドレス |
| `GENDER` | VARCHAR | ユーザーの性別 |
| `PHONE_NUMBER` | VARCHAR | ユーザーの電話番号 |
| `DOB` | VARCHAR | ユーザーの生年月日 |
| `HOME_CITY` | VARCHAR | ユーザーの居住都市 |
| `COUNTRY` | VARCHAR | ユーザーの国 |
| `LANGUAGE` | VARCHAR | ユーザーの言語設定 |
| `TIME_ZONE` | VARCHAR | ユーザーのタイムゾーン |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERLATESTSTATEDEFAULTATTRIBUTESVIEWSHARED schema" }

### `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED`スキーマ {#user_latest_state_custom_attribute_view_shared-schema}

| 列名     | データタイプ     | 説明 |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Brazeワークスペースの識別子 |
| `USER_ID` | VARCHAR | Brazeの一意のユーザー識別子 |
| `EXTERNAL_USER_ID` | VARCHAR | 独自のユーザー識別子（設定されている場合） |
| `TIME` | NUMBER | プロファイル更新のUnixタイムスタンプ（秒） |
| `TIME_MS` | NUMBER | プロファイル更新のUnixタイムスタンプ（ミリ秒） |
| `UPDATE_SOURCE` | VARCHAR | 属性更新のソース（API、SDK、ダッシュボードなど） |
| `ARCHIVED` | BOOLEAN | ユーザープロファイルがアーカイブされているかどうか |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Snowflakeでデータが最後に更新された日時 |
| `APP_ID` | VARCHAR | ワークスペース内の特定のアプリ |
| `CUSTOM_ATTRIBUTES` | OBJECT | すべてのカスタム属性を含むJSONオブジェクト（キーと値のペア） |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERLATESTSTATECUSTOMATTRIBUTEVIEWSHARED schema" }

{% alert note %}
このビューでは、`CUSTOM_ATTRIBUTES`に`VARIANT`ではなく`OBJECT`タイプを使用します。個々の属性をクエリするには、同じJSONアクセサー構文（`:attribute_name::TYPE`）を使用してください。
{% endalert %}

## 変更履歴ログ {#historical-change-logs}

これらのビューは、ユーザー属性の変更履歴ログを保存し、12時間の粒度で変更をキャプチャします。

- `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`
- `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`

### 使用方法

* 6か月間のローリング期間にわたるユーザー属性の変更履歴の記録を提供します。
* データは12時間ごとにスナップショットされます。つまり、この時間枠内の複数の更新は1つのレコードに統合されます。この期間内の個々の変更は個別に保持されません。
* `EFF_DT`と`END_DT`は、ユーザーの属性状態の開始と終了を示します。

{% include partners/snowflake_user_attributes_date_fields_note.md %}

### `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`スキーマ {#user_default_attributes_history_view_shared-schema}

| 列名     | データタイプ     | 説明 |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Brazeワークスペースの識別子 |
| `USER_ID` | VARCHAR | Brazeの一意のユーザー識別子 |
| `APP_ID` | VARCHAR | ワークスペース内の特定のアプリ |
| `TIME` | NUMBER | プロファイル更新のUnixタイムスタンプ（秒） |
| `TIME_MS` | NUMBER | プロファイル更新のUnixタイムスタンプ（ミリ秒） |
| `UPDATE_SOURCE` | VARCHAR | 属性更新のソース（API、SDK、ダッシュボードなど） |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Snowflakeでデータが最後に更新された日時 |
| `EXTERNAL_USER_ID` | VARCHAR | 独自のユーザー識別子（設定されている場合） |
| `FIRST_NAME` | VARCHAR | ユーザーの名 |
| `LAST_NAME` | VARCHAR | ユーザーの姓 |
| `EMAIL_ADDRESS` | VARCHAR | ユーザーのメールアドレス |
| `GENDER` | VARCHAR | ユーザーの性別 |
| `PHONE_NUMBER` | VARCHAR | ユーザーの電話番号 |
| `DOB` | VARCHAR | ユーザーの生年月日 |
| `TIME_ZONE` | VARCHAR | ユーザーのタイムゾーン |
| `HOME_CITY` | VARCHAR | ユーザーの居住都市 |
| `COUNTRY` | VARCHAR | ユーザーの国 |
| `LANGUAGE` | VARCHAR | ユーザーの言語設定 |
| `EFF_DT` | TIMESTAMP_NTZ | 有効日: この属性状態が開始された日時 |
| `END_DT` | TIMESTAMP_NTZ | 終了日: この属性状態が終了した日時（現在の状態の場合はNULL） |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERDEFAULTATTRIBUTESHISTORYVIEWSHARED schema" }

### `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`スキーマ {#user_custom_attributes_history_view_shared-schema}

| 列名     | データタイプ     | 説明 |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Brazeワークスペースの識別子 |
| `USER_ID` | VARCHAR | Brazeの一意のユーザー識別子 |
| `APP_ID` | VARCHAR | ワークスペース内の特定のアプリ |
| `EXTERNAL_USER_ID` | VARCHAR | 独自のユーザー識別子（設定されている場合） |
| `TIME` | NUMBER | プロファイル更新のUnixタイムスタンプ（秒） |
| `TIME_MS` | NUMBER | プロファイル更新のUnixタイムスタンプ（ミリ秒） |
| `UPDATE_SOURCE` | VARCHAR | 属性更新のソース（API、SDK、ダッシュボードなど） |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Snowflakeでデータが最後に更新された日時 |
| `CUSTOM_ATTRIBUTES` | VARIANT | すべてのカスタム属性を含むJSONオブジェクト（キーと値のペア） |
| `ARCHIVED` | BOOLEAN | ユーザープロファイルがアーカイブされているかどうか |
| `EFF_DT` | TIMESTAMP_NTZ | 有効日: この属性状態が開始された日時 |
| `END_DT` | TIMESTAMP_NTZ | 終了日: この属性状態が終了した日時（現在の状態の場合はNULL） |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERCUSTOMATTRIBUTESHISTORYVIEWSHARED schema" }

## 一般的なユースケース {#common-use-cases}

### ユーザーセグメントの構築 {#building-user-segments}

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

### 経時的なユーザー行動の分析 {#analyzing-user-behavior-over-time}

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

### デフォルト属性とカスタム属性の結合 {#combining-default-and-custom-attributes}

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

### 高価値顧客の特定 {#finding-high-value-customers}

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

## ベストプラクティス {#best-practices}

### 推奨されるクエリの使用方法 {#recommended-query-usage}

| ユースケース                                               | 推奨ビュー                                   | 備考                                                                 |
|--------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------------------------|
| 最近の更新を必要としない**一般的なクエリ** | `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`と`USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`               | 高速な実行。データは最大12時間前のものです。                          |
| **最新のユーザー属性**を必要とするクエリ       | `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`と`USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` | ほぼリアルタイムの更新を提供しますが、大規模なデータセットでは低速になる場合があります。 |
| 属性変更の**履歴トラッキング**           | `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`と`USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`      | 属性の変更を12時間の粒度で保存します。                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Recommended query usage" }

### パフォーマンスに関する考慮事項 {#performance-considerations}

* `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`または`USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`に対するクエリは、大規模なウェアハウスの大規模なデータセット（約10億ユーザー）で10秒以内に返されます。
* 単一ユーザーに対する`USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`または`USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED`のクエリは1分以内に返されますが、`USER_ID`フィルタリングなしではスケーリングが不十分です。
* `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`または`USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED`で1億人を超えるユーザーに対するクエリは、ユーザーごとの集計のため数分かかる場合があります。