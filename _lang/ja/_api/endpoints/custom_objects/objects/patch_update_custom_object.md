---
nav_title: "PATCH: カスタムオブジェクトの更新"
article_title: "PATCH: カスタムオブジェクトの更新"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "この記事では、カスタムオブジェクトの更新エンドポイントについて詳しく説明します。"
---
{% api %}
# カスタムオブジェクトの更新 {#update-custom-object}
{% apimethod patch %}
/custom_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> このエンドポイントを使用して、既存のカスタムオブジェクトに属性をマージします。

{% alert important %}
カスタムオブジェクトは現在、早期アクセス段階です。カスタムオブジェクトのAPIキー権限が**設定** > **APIキー**に表示されるようにするには、ワークスペースを有効にする必要があります。
{% endalert %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`custom_objects.update` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

このエンドポイントは、カスタムオブジェクト書き込みバケットに属し、デフォルトでは1分あたり50リクエストの制限があります。

## パスパラメーター {#path-parameters}

以下の表は、`/custom_objects/objects/{type_name}/{external_id}` エンドポイントのパスパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `type_name` | 必須 | String | カスタムオブジェクトタイプのマシン名 |
| `external_id` | 必須 | String | オブジェクト識別子 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="カスタムオブジェクト更新のパスパラメーター" }

## リクエストパラメーター {#request-parameters}

以下の表は、`/custom_objects/objects/{type_name}/{external_id}` エンドポイントのJSONリクエストボディパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `attributes` | 必須 | Object | マージするトップレベルのフィールド |
| `display_name` | オプション | String | オブジェクトの表示ラベル。タイプに表示名ソースフィールドがある場合、そのフィールドの値が優先されます。省略した場合、既存の表示名が保持されます |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="カスタムオブジェクト更新のリクエストパラメーター" }

## リクエスト例 {#example-request}

このセクションには、サンプルのJSONペイロードとサンプルのcURLリクエストが含まれています。

### サンプルリクエストペイロード {#sample-request-payload}

```json
{
  "attributes": {
    "credits": 750
  }
}
```

### サンプルcURLリクエスト {#sample-curl-request}

この例では、`acct-123` の `credits` 属性を更新し、レコードの他の属性はそのまま保持します。

```bash
curl --location --request PATCH 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{ "attributes": { "credits": 750 } }'
```

## レスポンス {#response}

このセクションには、成功レスポンスのサンプルとレスポンスフィールドが含まれています。

### 成功レスポンスの例 {#example-success-response}

ステータスコード `200` は以下のレスポンスボディを返す場合があります。`attributes` オブジェクトはマージの結果を反映しています。

```json
{
  "custom_object": {
    "type_name": "account",
    "external_id": "acct-123",
    "attributes": { "name": "Acme", "credits": 750 }
  }
}
```

### レスポンスパラメーター {#response-parameters}

以下の表は、成功レスポンスに含まれるフィールドの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `custom_object` | 必須 | Object | 更新されたカスタムオブジェクトレコード |
| `custom_object.type_name` | 必須 | String | カスタムオブジェクトタイプのマシン名 |
| `custom_object.external_id` | 必須 | String | カスタムオブジェクト識別子 |
| `custom_object.attributes` | 必須 | Object | マージ後のオブジェクト属性 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="カスタムオブジェクト更新のレスポンスパラメーター" }

## エラー {#errors}

以下の表は、このエンドポイントで発生する一般的なエラーとその解決方法の一覧です。

| ステータス | 原因 | 対処方法 |
|---|---|---|
| `400` | バリデーションエラー | `attributes` 内のすべてのフィールドがタイプスキーマに存在し、正しいデータ型を使用していることを確認してください。 |
| `404` | タイプまたはオブジェクトが見つかりません | `type_name` と `external_id` の両方がワークスペースに存在することを確認してください。 |
| `401` | REST APIキーが不足しているか無効です | `Authorization` ヘッダーが `Bearer YOUR_REST_API_KEY` を使用しており、キーが有効であることを確認してください。 |
| `403` | APIキーに権限がないか、リクエストが許可リストによってブロックされています | キーに `custom_objects.update` 権限があること、およびソースIPがキーの許可リストに含まれていること（設定されている場合）を確認してください。 |
| `429` | レート制限超過 | `X-RateLimit-Reset` の後にリトライし、リクエスト頻度を下げてください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="カスタムオブジェクト更新のエラー" }
{% endapi %}