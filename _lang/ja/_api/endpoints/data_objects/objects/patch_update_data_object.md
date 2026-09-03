---
nav_title: "PATCH: データオブジェクトの更新"
article_title: "PATCH: データオブジェクトの更新"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "この記事では、データオブジェクトの更新エンドポイントの詳細について説明します。"
---
{% api %}
# データオブジェクトの更新 {#update-data-object}
{% apimethod patch %}
/data_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> このエンドポイントを使用して、既存のデータオブジェクトに属性をマージします。

{% alert important %}
データオブジェクトは現在早期アクセス段階です。データオブジェクトのAPIキー権限が**設定** > **APIキー**に表示されるには、ワークスペースが有効になっている必要があります。
{% endalert %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`data_objects.update` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

このエンドポイントはデータオブジェクト書き込みバケットに含まれ、デフォルトの制限は1分あたり50リクエストです。

## パスパラメーター {#path-parameters}

以下の表は、`/data_objects/objects/{type_name}/{external_id}` エンドポイントのパスパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `type_name` | 必須 | String | データオブジェクトタイプのマシン名 |
| `external_id` | 必須 | String | オブジェクト識別子 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="データオブジェクトの更新パスパラメーター" }

## リクエストパラメーター {#request-parameters}

以下の表は、`/data_objects/objects/{type_name}/{external_id}` エンドポイントのJSONリクエストボディパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `attributes` | 必須 | Object | マージするトップレベルフィールド |
| `display_name` | オプション | String | オブジェクトの表示ラベル。タイプに表示名のソースフィールドがある場合、そのフィールドの値が優先されます。省略した場合、既存の表示名が保持されます |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="データオブジェクトの更新リクエストパラメーター" }

## リクエスト例 {#example-request}

このセクションでは、サンプルのJSONペイロードとサンプルのcURLリクエストを示します。

### サンプルリクエストペイロード {#sample-request-payload}

```json
{
  "attributes": {
    "credits": 750
  }
}
```

### サンプルcURLリクエスト {#sample-curl-request}

この例では、`acct-123` の `credits` 属性を更新し、レコードの他の属性は変更しません。

```bash
curl --location --request PATCH 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{ "attributes": { "credits": 750 } }'
```

## レスポンス {#response}

このセクションでは、成功レスポンスのサンプルとレスポンスフィールドについて説明します。

### 成功レスポンス例 {#example-success-response}

ステータスコード `200` は、以下のレスポンスボディを返す可能性があります。`attributes` オブジェクトはマージの結果を反映しています。

```json
{
  "data_object": {
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
| `data_object` | 必須 | Object | 更新されたデータオブジェクトレコード |
| `data_object.type_name` | 必須 | String | データオブジェクトタイプのマシン名 |
| `data_object.external_id` | 必須 | String | データオブジェクト識別子 |
| `data_object.attributes` | 必須 | Object | マージ後のオブジェクト属性 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="データオブジェクトの更新レスポンスパラメーター" }

## エラー {#errors}

以下の表は、このエンドポイントの一般的なエラーとその解決方法の一覧です。

| ステータス | 原因 | ガイダンス |
|---|---|---|
| `400` | バリデーションエラー | `attributes` 内のすべてのフィールドがタイプスキーマに存在し、正しいデータ型を使用していることを確認してください。 |
| `404` | タイプが見つからない、またはオブジェクトが見つからない | `type_name` と `external_id` の両方がワークスペースに存在することを確認してください。 |
| `401` | REST APIキーが見つからない、または無効 | `Authorization` ヘッダーが `Bearer YOUR_REST_API_KEY` を使用しており、キーが有効であることを確認してください。 |
| `403` | APIキーに権限がない、またはリクエストが許可リストによってブロックされている | キーに `data_objects.update` 権限があり、許可リストが設定されている場合は、送信元IPが許可リストに含まれていることを確認してください。 |
| `429` | レート制限超過 | `X-RateLimit-Reset` の後にリトライし、リクエスト頻度を減らしてください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="データオブジェクトの更新エラー" }
{% endapi %}