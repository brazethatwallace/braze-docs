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

{% alert note %}
`TIME`フィールドは、ユーザープロファイルが更新された時刻を秒単位で表します。`TIME_MS`フィールドは、ミリ秒精度で同じ時刻を示します。バックフィルされたデータの場合、`TIME`と`TIME_MS`の値はバックフィルの実行時刻です。
{% endalert %}

### `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`スキーマ {#user_default_attributes_view_shared-schema}

| 列名     | データタイプ     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `TIME` | NUMBER |
| `TIME_MS` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_USER_ID` | VARCHAR |
| `FIRST_NAME` | VARCHAR |
| `LAST_NAME` | VARCHAR |
| `EMAIL_ADDRESS` | VARCHAR |
| `GENDER` | VARCHAR |
| `PHONE_NUMBER` | VARCHAR |
| `DOB` | VARCHAR |
| `TIMEZONE` | VARCHAR |
| `HOME_CITY` | VARCHAR |
| `COUNTRY` | VARCHAR |
| `LANGUAGE` | VARCHAR |
| `ARCHIVED` | BOOLEAN |
{: .reset-td-br-1 .reset-td-br-2 aria-label="USERDEFAULTATTRIBUTESVIEWSHARED schema" }


### `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`スキーマ {#user_custom_attributes_view_shared-schema}

| 列名     | データタイプ     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `EXTERNAL_USER_ID` | VARCHAR |
| `TIME` | NUMBER |
| `TIME_MS` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `CUSTOM_ATTRIBUTES` | VARIANT |
| `ARCHIVED` | BOOLEAN |
{: .reset-td-br-1 .reset-td-br-2 aria-label="USERCUSTOMATTRIBUTESVIEWSHARED schema" }

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

{% alert note %}
`TIME`フィールドは、ユーザープロファイルが更新された時刻を秒単位で表します。`TIME_MS`フィールドは、ミリ秒精度で同じ時刻を示します。バックフィルされたデータの場合、`TIME`と`TIME_MS`の値はバックフィルの実行時刻です。
{% endalert %}

### `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`スキーマ {#user_latest_state_default_attributes_view_shared-schema}

| 列名     | データタイプ     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `TIME` | NUMBER |
| `TIME_MS` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `ARCHIVED` | BOOLEAN |
| `SF_UPDATED_AT` | TIMESTAMP_LTZ |
| `EXTERNAL_USER_ID` | VARCHAR |
| `FIRST_NAME` | VARCHAR |
| `LAST_NAME` | VARCHAR |
| `EMAIL_ADDRESS` | VARCHAR |
| `GENDER` | VARCHAR |
| `PHONE_NUMBER` | VARCHAR |
| `DOB` | VARCHAR |
| `HOME_CITY` | VARCHAR |
| `COUNTRY` | VARCHAR |
| `LANGUAGE` | VARCHAR |
| `TIMEZONE` | VARCHAR |
{: .reset-td-br-1 .reset-td-br-2 aria-label="USERLATESTSTATEDEFAULTATTRIBUTESVIEWSHARED schema" }

### `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED`スキーマ {#user_latest_state_custom_attribute_view_shared-schema}

| 列名     | データタイプ     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `EXTERNAL_USER_ID` | VARCHAR |
| `TIME` | NUMBER |
| `TIME_MS` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `ARCHIVED` | BOOLEAN |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `APP_ID` | VARCHAR |
| `CUSTOM_ATTRIBUTES` | OBJECT |
{: .reset-td-br-1 .reset-td-br-2 aria-label="USERLATESTSTATECUSTOMATTRIBUTEVIEWSHARED schema" }

## 変更履歴ログ {#historical-change-logs}

これらのビューは、ユーザー属性の変更履歴ログを保存し、12時間の粒度で変更をキャプチャします。

- `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`
- `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`

### 使用方法

* 6か月間のローリング期間にわたるユーザー属性の変更履歴の記録を提供します。
* データは12時間ごとにスナップショットされます。つまり、この時間枠内の複数の更新は1つのレコードに統合されます。この期間内の個々の変更は個別に保持されません。
* `EFF_DT`と`END_DT`は、ユーザーの属性状態の開始と終了を示します。

{% alert note %}
`TIME`フィールドは、ユーザープロファイルが更新された時刻を秒単位で表します。`TIME_MS`フィールドは、ミリ秒精度で同じ時刻を示します。バックフィルされたデータの場合、`TIME`と`TIME_MS`の値はバックフィルの実行時刻です。
{% endalert %}

### `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`スキーマ {#user_default_attributes_history_view_shared-schema}

| 列名     | データタイプ     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `TIME` | NUMBER |
| `TIME_MS` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_USER_ID` | VARCHAR |
| `FIRST_NAME` | VARCHAR |
| `LAST_NAME` | VARCHAR |
| `EMAIL_ADDRESS` | VARCHAR |
| `GENDER` | VARCHAR |
| `PHONE_NUMBER` | VARCHAR |
| `DOB` | VARCHAR |
| `TIMEZONE` | VARCHAR |
| `HOME_CITY` | VARCHAR |
| `COUNTRY` | VARCHAR |
| `LANGUAGE` | VARCHAR |
| `EFF_DT` | TIMESTAMP_NTZ |
| `END_DT` | TIMESTAMP_NTZ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="USERDEFAULTATTRIBUTESHISTORYVIEWSHARED schema" }

### `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`スキーマ {#user_custom_attributes_history_view_shared-schema}

| 列名     | データタイプ     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `EXTERNAL_USER_ID` | VARCHAR |
| `TIME` | NUMBER |
| `TIME_MS` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `CUSTOM_ATTRIBUTES` | VARIANT |
| `ARCHIVED` | BOOLEAN |
| `EFF_DT` | TIMESTAMP_NTZ |
| `END_DT` | TIMESTAMP_NTZ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="USERCUSTOMATTRIBUTESHISTORYVIEWSHARED schema" }

## ベストプラクティス {#best-practices}

### 推奨されるクエリの使用方法 {#recommended-query-usage}

| ユースケース                                               | 推奨ビュー                                   | 備考                                                                 |
|--------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------------------------|
| 最近の更新を必要としない**一般的なクエリ** | `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`と`USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`               | 高速な実行。データは最大12時間前のものです。                          |
| **最新のユーザー属性**を必要とするクエリ       | `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`と`USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` | ほぼリアルタイムの更新を提供しますが、大規模なデータセットでは低速になる場合があります。 |
| 属性変更の**履歴追跡**           | `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`と`USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`      | 属性の変更を12時間の粒度で保存します。                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Recommended query usage" }

### パフォーマンスに関する考慮事項 {#performance-considerations}

* `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`または`USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`に対するクエリは、大規模なウェアハウスの大規模なデータセット（約10億ユーザー）で10秒以内に返されます。
* 単一ユーザーに対する`USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`または`USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED`のクエリは1分以内に返されますが、`USER_ID`フィルタリングなしではスケーリングが不十分です。
* `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`または`USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED`で1億人を超えるユーザーに対するクエリは、ユーザーごとの集計のため数分かかる場合があります。