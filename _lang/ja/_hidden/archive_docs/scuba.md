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

BrazeでScuba Analyticsを使用するには、以下が必要です。

| 必要条件 | 説明 |
|---|---|
| Scuba APIトークン | `https://{scuba_hostname}/api/create_token` エンドポイントから取得できるScuba APIトークン。 |
| Braze REST APIキー | `users.track` 権限を持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | RESTエンドポイントのURL。エンドポイントはインスタンスの[Braze URL](https://scuba.io)に応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## BrazeへのScubaデータのアップロード {#uploading-your-scuba-data-to-braze}

{% alert important %}
以下のリクエストはcurlを使用します。APIリクエストの管理を改善するには、PostmanなどのAPIクライアントを使用することをお勧めします。
{% endalert %}

BrazeにScubaデータをアップロードするには、`https://scuba.pliant.io/a/scuba-connectors/prod/braze-activation` に対して `application/json` content-typeを使用してPOSTリクエストを行います。

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

次のように置き換えます。

| プレースホルダー | 説明 |
|---|---|
| `BRAZE_API_ENDPOINT` | 現在のBrazeインスタンスのBraze RESTエンドポイントURL。詳細については、[REST APIキー]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys)を参照してください。 |
| `BRAZE_API_KEY` | `users.track` 権限を持つBraze REST APIキー。 |
| `HOSTNAME` | 現在のScubaインスタンスのホスト名。 |
| `SCUBA_API_TOKEN` | Scuba APIトークン。 |
| `TABLE_NAME` | データセットが属するテーブル。詳細については、[用語集: データセットテーブル](https://docs.scuba.io/glossary/dataset-table)を参照してください。 |
| `ACTOR_PROPERTY_NAME` | データセットが属するアクタープロパティ。この名前に一致するデータのみが返されます。詳細については、[用語集: アクタープロパティ](https://docs.scuba.io/glossary/actor-property)を参照してください。 |
| `ACTOR_PROPERTY_FILTER` | アクタープロパティのオーディエンス検索フィルター。 |
| `ACTOR_ID` | データセットが属するアクタープロパティのID。このIDは、Brazeの `external_id` に一致します。詳細については、[用語集: アクター](https://docs.scuba.io/glossary/actor)を参照してください。 |
| `PERIOD_START` | BQL互換の日付としての期間開始日。詳細については、[BQL構文および使用法](https://docs.scuba.io/guides/bql-syntax-and-usage)を参照してください。 |
| `PERIOD_END` | BQL互換の日付としての期間終了日。詳細については、[BQL構文および使用法](https://docs.scuba.io/guides/bql-syntax-and-usage)を参照してください。 |
| `RECORD_LIMIT` | **オプション**: 返されるレコードの最大数。`scuba_record_limit` が省略された場合、Scubaは最大100件のレコードを返します。これを変更するには、負でない数値を `scuba_record_limit` に割り当てます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Uploading your Scuba data to Braze" }

### デフォルト動作 {#default-behavior}

デフォルトでは、`update_existing_only` は `false` に設定されています。これにより、Braze内の既存のレコードが更新され、存在しないレコードの新規レコードが作成されます。Scubaが新しいレコードを作成しないようにするには、`update_existing_only` を `true` に設定します。

### レート制限 {#rate-limit}

Scubaは、このエンドポイントに対して1分あたり50,000件のリクエストのレート制限を適用します。

## Scubaの行動データを使用したセグメントの作成 {#creating-segments-using-scubas-behavioral-data}

[データをアップロード](#uploading-your-scuba-data-to-braze)したら、Scubaの行動データを使用してBrazeでユーザーセグメントを作成できます。

### ステップ1: 新しいセグメントを作成する {#step-1-create-a-new-segment}

Brazeで、**Audience** > **セグメント** に移動し、**Create セグメント** を選択して、セグメントの名前を入力します。

![Brazeでの新しいセグメントの作成。]({% image_buster /assets/img/scuba/analytics/segment_name.png %})

### ステップ2: Scuba属性を探して選択する {#step-2-find-and-select-the-scuba-attribute}

**セグメント Details** > **Filters** で、**Custom Attributes** を選択します。

![「セグメント Details」での「Custom Attributes」フィルターの選択。]({% image_buster /assets/img/scuba/analytics/filter_attribute.png %})

**Search custom attributes** を選択し、前回のPOSTリクエストで使用したアクタープロパティの名前を選択します。

![アクタープロパティをカスタム属性として選択する。]({% image_buster /assets/img/scuba/analytics/select_property.png %})

### ステップ3: 属性を設定する {#step-3-configure-the-attribute}

アクタープロパティ名の横で、Operatorと値を選択します（該当する場合）。これらの値は、Scubaで定義したアクタープロパティによって決定されます。完了したら、**Save** を選択します。

![選択されたプロパティ名に対するOperatorと値の選択。]({% image_buster /assets/img/scuba/analytics/operator_end.png %})