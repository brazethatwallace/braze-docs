---
nav_title: "PUT: データオブジェクトの置換"
article_title: "PUT: データオブジェクトの置換"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、データオブジェクトの置換エンドポイントについて詳しく説明します。"
---
{% api %}
# データオブジェクトの置換 {#replace-data-object}
{% apimethod put %}
/data_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> このエンドポイントを使用して、全属性置換セマンティクスでデータオブジェクトを作成または置換します。

{% alert important %}
データオブジェクトは現在早期アクセス段階です。Data Objects APIキーの権限が**設定** > **APIキー**に表示されるには、ワークスペースが有効になっている必要があります。
{% endalert %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`data_objects.update` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

このエンドポイントはデータオブジェクト書き込みバケットに属しており、デフォルトの制限は1分あたり50リクエストです。

## パスパラメーター {#path-parameters}

以下の表は、`/data_objects/objects/{type_name}/{external_id}` エンドポイントのパスパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `type_name` | 必須 | String | データオブジェクトタイプのマシン名 |
| `external_id` | 必須 | String | オブジェクト識別子 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="データオブジェクト置換のパスパラメーター" }

## リクエストパラメーター {#request-parameters}

以下の表は、`/data_objects/objects/{type_name}/{external_id}` エンドポイントのJSONリクエストボディパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `attributes` | 必須 | Object | オブジェクトの全属性。省略されたフィールドはクリアされます |
| `display_name` | オプション | String | オブジェクトの表示ラベル。タイプに表示名ソースフィールドがある場合、そのフィールドの値が優先されます。デフォルトは `external_id` です |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="データオブジェクト置換のリクエストパラメーター" }

## リクエスト例 {#example-request}

このセクションには、サンプルJSONペイロードとサンプルcURLリクエストが含まれています。

### サンプルリクエストペイロード {#sample-request-payload}

```json
{
  "attributes": {
    "name": "Updated Account"
  }
}
```

### サンプルcURLリクエスト {#sample-curl-request}

この例では、`acct-123` に保存されている属性をペイロード内の属性に置換します。その識別子を持つレコードが存在しない場合、このリクエストによって新規作成されます。

```bash
curl --location --request PUT 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "attributes": {
    "name": "Updated Account"
  }
}'
```

## レスポンス {#response}

このセクションには、成功レスポンスのサンプルとレスポンスフィールドが含まれています。

### 成功レスポンスの例 {#example-success-response}

ステータスコード `200` は以下のレスポンスボディを返す可能性があります。このエンドポイントは、リクエストがオブジェクトを作成した場合でも置換した場合でも `200` を返します。

```json
{
  "data_object": {
    "type_name": "account",
    "external_id": "acct-123",
    "attributes": { "name": "Updated Account" }
  }
}
```

### レスポンスパラメーター {#response-parameters}

以下の表は、成功レスポンスに含まれるフィールドの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `data_object` | 必須 | Object | 作成または置換されたデータオブジェクトレコード |
| `data_object.type_name` | 必須 | String | データオブジェクトタイプのマシン名 |
| `data_object.external_id` | 必須 | String | データオブジェクト識別子 |
| `data_object.attributes` | 必須 | Object | フィールド名をキーとした保存済みオブジェクト属性 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="データオブジェクト置換のレスポンスパラメーター" }

## エラー {#errors}

以下の表は、このエンドポイントで発生する一般的なエラーとその解決方法の一覧です。

| ステータス | 原因 | ガイダンス |
|---|---|---|
| `400` | バリデーションエラー | `attributes` 内のすべてのフィールドがタイプスキーマに存在し、正しいデータ型を使用していることを確認してください。 |
| `404` | タイプが見つからない（`data-object-type-not-found`） | `type_name` がワークスペースに存在し、マシン名と完全に一致していることを確認してください。 |
| `422` | このリクエストが新規オブジェクトを作成する場合にレコード制限に到達（`data-object-record-limit-exceeded`） | そのタイプのオブジェクト数を削減するか、ワークスペースの制限についてBrazeサポートにお問い合わせください。 |
| `401` | REST APIキーが不足または無効 | `Authorization` ヘッダーが `Bearer YOUR_REST_API_KEY` を使用しており、キーがアクティブであることを確認してください。 |
| `403` | APIキーに権限がない、またはリクエストが許可リストによってブロックされている | キーに `data_objects.update` 権限があること、およびソースIPがキーの許可リストに含まれていること（設定されている場合）を確認してください。 |
| `429` | レート制限超過 | `X-RateLimit-Reset` の後にリトライし、リクエスト頻度を下げてください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="データオブジェクト置換のエラー" }
{% endapi %}