---
nav_title: Scuba
article_title: Scuba Analytics
description: "このScubaとBrazeのテクニカルリファレンスでは、Braze セグメントを使用してScubaのリアルタイムデータインサイトをアクティブにする方法を説明します。"
page_type: partner
search_tag: Partner
noindex: true
hidden: true
---

# Scuba Analytics

>[Scuba Analytics](https://scuba.io) は、高速時系列データ向けに設計された、機械学習を採用したフルスタックのデータコラボレーションプラットフォームです。Scubaでは、ユーザー（アクターとも呼ばれます）を選択的にエクスポートし、Brazeプラットフォームに読み込むことができます。Scubaでは、カスタムアクタープロパティを使用して行動トレンドを分析し、さまざまなプラットフォーム間でデータを有効化し、機械学習を使用して予測モデリングを実行します。

_この統合はScuba Analyticsによって管理されています。_

## 前提条件 {#prerequisites}

Scuba AnalyticsをBrazeで使用するには、以下が必要です。

| 要件 | 説明 |
|---|---|
| Scuba APIトークン | `https://{scuba_hostname}/api/create_token` エンドポイントから取得できるScuba APIトークン。 |
| Braze REST APIキー | `users.track` 権限を持つBraze REST APIキー。<br><br> これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | RESTエンドポイントURL。エンドポイントは、[お使いのインスタンスのBraze URL](https://scuba.io)によって異なります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ScubaデータをBrazeにアップロードする {#uploading-your-scuba-data-to-braze}

{% alert important %}
以下のリクエストはcurlを使用しています。APIリクエストをより適切に管理するために、Postmanなどの APIクライアントの使用をお勧めします。
{% endalert %}

ScubaデータをBrazeにアップロードするには、`application/json`コンテンツタイプを使用して`https://scuba.pliant.io/a/scuba-connectors/prod/braze-activation`にPOSTリクエストを送信します。

```bash
curl -X POST "https://scuba.pliant.io/a/scuba-connectors/prod/braze-activation" \
-H "content-type: application/json" \
-d '{"braze_host":"BRAZE_API_ENDPOINT", \
"braze_api_key":"BRAZE_API_KEY", \
"scuba_host":"HOSTNAME", \
"scuba_token":"SCUBA_API_TOKEN", \
"scuba_table_name":"TABLE_NAME", \
"scuba_actor_property_name":"ACTOR_PROPERTY_NAME", \
"scuba_actor_property_value_filter":"ACTOR_PROPERTY_FILTER" \
"scuba_actor_id":"ACTOR_ID", \
"scuba_period_start":"PERIOD_START", \
"scuba_period_end":"PERIOD_END", \
"scuba_record_limit":"RECORD_LIMIT"}'
```

以下を置き換えてください。

| プレースホルダー             | 説明                                                                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BRAZE_API_ENDPOINT`    | 現在のBrazeインスタンスのBraze RESTエンドポイントURL。詳細については、[REST APIキー]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers)を参照してください。 |
| `BRAZE_API_KEY`         | `users.track`権限を持つBraze REST APIキー。                                                                                                                                      |
| `HOSTNAME`              | 現在のScubaインスタンスのホスト名。                                                                                                                                                    |
| `SCUBA_API_TOKEN`       | Scuba APIトークン。                                                                                                                                                           |
| `TABLE_NAME`            | データセットが属するテーブル。詳細については、[用語集: データセットテーブル](https://docs.scuba.io/glossary/dataset-table)を参照してください。                                                                                                      |
| `ACTOR_PROPERTY_NAME`   | データセットが属するアクタープロパティ。この名前に一致するデータのみが返されます。詳細については、[用語集: アクタープロパティ](https://docs.scuba.io/glossary/actor-property)を参照してください。                                             |
| `ACTOR_PROPERTY_FILTER` | アクタープロパティのオーディエンス検索フィルター。                                                                                                                                             |
| `ACTOR_ID`              | データセットが属するアクタープロパティのID。このIDはBrazeの`external_id`と一致します。詳細については、[用語集: アクター](https://docs.scuba.io/glossary/actor)を参照してください。                                              |
| `PERIOD_START`          | BQL互換の日付形式の開始期間。詳細については、[BQL構文と使用方法](https://docs.scuba.io/guides/bql-syntax-and-usage)を参照してください。                                                                                                 |
| `PERIOD_END`            | BQL互換の日付形式の終了期間。詳細については、[BQL構文と使用方法](https://docs.scuba.io/guides/bql-syntax-and-usage)を参照してください。                                                                                                   |
| `RECORD_LIMIT`          | **オプション**: 返されるレコードの最大数。`scuba_record_limit`を省略した場合、Scubaは最大100件のレコードを返します。これを変更するには、`scuba_record_limit`に任意の非負の数値を設定してください。    |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ScubaデータをBrazeにアップロードする" }

### デフォルトの動作 {#default-behavior}

デフォルトでは、`update_existing_only`は`false`に設定されており、Braze内の既存レコードを更新するとともに、存在しないレコードについては新規作成します。Scubaによる新規レコードの作成を防ぐには、`update_existing_only`を`true`に設定してください。

### レート制限 {#rate-limit}

Scubaは、このエンドポイントに対して1分あたり50,000リクエストのレート制限を適用します。

## Scubaの行動データを使用したセグメントの作成 {#creating-segments-using-scubas-behavioral-data}

[データをアップロード](#uploading-your-scuba-data-to-braze)した後、Scubaの行動データを使用してBrazeでユーザーセグメントを作成できます。

### ステップ1：新しいセグメントを作成する {#step-1-create-a-new-segment}

Brazeで**オーディエンス** > **セグメント**に移動し、**セグメントを作成**を選択してセグメントの名前を入力します。

![Brazeで新しいセグメントを作成する画面。]({% image_buster /assets/img/scuba/analytics/segment_name.png %})

### ステップ2：Scubaの属性を見つけて選択する {#step-2-find-and-select-the-scuba-attribute}

**セグメントの詳細** > **フィルター**で、**カスタム属性**を選択します。

![「セグメントの詳細」の「カスタム属性」フィルターを選択する画面。]({% image_buster /assets/img/scuba/analytics/filter_attribute.png %})

**カスタム属性を検索**を選択し、前のPOSTリクエストで使用したアクタープロパティ名を選択します。

![アクタープロパティをカスタム属性として選択する画面。]({% image_buster /assets/img/scuba/analytics/select_property.png %})

### ステップ3：属性を設定する {#step-3-configure-the-attribute}

アクタープロパティ名の横で、演算子と値（該当する場合）を選択します。これらの値は、Scubaで定義したアクタープロパティによって決まります。完了したら、**保存**を選択します。

![選択した属性の演算子と値を選択する画面。]({% image_buster /assets/img/scuba/analytics/operator_end.png %})