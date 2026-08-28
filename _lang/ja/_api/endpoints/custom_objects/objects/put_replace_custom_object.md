---
nav_title: "PUT: カスタムオブジェクトの置換"
article_title: "PUT: カスタムオブジェクトの置換"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、カスタムオブジェクトの置換エンドポイントについて詳しく説明します。"
---
{% api %}
# カスタムオブジェクトの置換 {#replace-custom-object}
{% apimethod put %}
/custom_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> このエンドポイントを使用して、全属性置換セマンティクスでカスタムオブジェクトを作成または置換します。

{% alert important %}
カスタムオブジェクトは現在、早期アクセス段階です。カスタムオブジェクトのAPIキー権限が**設定** > **APIキー**に表示されるには、ワークスペースが有効になっている必要があります。
{% endalert %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`custom_objects.update` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

このエンドポイントはカスタムオブジェクト書き込みバケットに含まれ、デフォルトの制限は1分あたり50リクエストです。

## パスパラメーター {#path-parameters}

以下の表は、`/custom_objects/objects/{type_name}/{external_id}` エンドポイントのパスパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `type_name` | 必須 | String | カスタムオブジェクトタイプのマシン名 |
| `external_id` | 必須 | String | オブジェクト識別子 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="カスタムオブジェクトの置換パスパラメーター" }

## リクエストパラメーター {#request-parameters}

以下の表は、`/custom_objects/objects/{type_name}/{external_id}` エンドポイントのJSONリクエストボディパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `attributes` | 必須 | Object | オブジェクトの全属性。省略されたフィールドはクリアされます |
| `display_name` | 任意 | String | オブジェクトの表示ラベル。タイプに表示名のソースフィールドがある場合、そのフィールドの値が優先されます。デフォルトは `external_id` です |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="カスタムオブジェクトの置換リクエストパラメーター" }

## リクエスト例 {#example-request}

このセクションには、サンプルJSONペイロードとサンプルcURLリクエストが含まれます。

### サンプルリクエストペイロード {#sample-request-payload}

```json
{
  "attributes": {
    "name": "Updated Account"
  }
}
```

### サンプルcURLリクエスト {#sample-curl-request}

この例では、`acct-123` に保存されている属性をペイロードの内容で置換します。その識別子のレコードが存在しない場合、このリクエストによって新規作成されます。

```bash
curl --location --request PUT 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "attributes": {
    "name": "Updated Account"
  }
}'
```

## レスポンス {#response}

このセクションには、成功レスポンスのサンプルとレスポンスフィールドが含まれます。

### 成功レスポンス例 {#example-success-response}

ステータスコード `200` は、以下のレスポンスボディを返す可能性があります。このエンドポイントは、リクエストがオブジェクトを作成した場合も置換した場合も `200` を返します。

```json
{
  "custom_object": {
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
| `custom_object` | 必須 | Object | 作成または置換されたカスタムオブジェクトレコード |
| `custom_object.type_name` | 必須 | String | カスタムオブジェクトタイプのマシン名 |
| `custom_object.external_id` | 必須 | String | カスタムオブジェクト識別子 |
| `custom_object.attributes` | 必須 | Object | フィールド名をキーとして保存されたオブジェクト属性 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="カスタムオブジェクトの置換レスポンスパラメーター" }

## エラー {#errors}

以下の表は、このエンドポイントで発生する一般的なエラーとその解決方法の一覧です。

| ステータス | 原因 | ガイダンス |
|---|---|---|
| `400` | バリデーションエラー | `attributes` のすべてのフィールドがタイプスキーマに存在し、正しいデータ型を使用していることを確認してください。 |
| `404` | タイプが見つかりません（`custom-object-type-not-found`） | `type_name` がワークスペースに存在し、マシン名と完全に一致していることを確認してください。 |
| `422` | このリクエストが新しいオブジェクトを作成しようとした際にレコード制限に達しました（`custom-object-record-limit-exceeded`） | そのタイプのオブジェクト数を減らすか、ワークスペースの制限についてBrazeサポートにお問い合わせください。 |
| `401` | REST APIキーが見つからないか無効です | `Authorization` ヘッダーが `Bearer YOUR_REST_API_KEY` を使用していること、およびキーがアクティブであることを確認してください。 |
| `403` | APIキーに権限がないか、リクエストが許可リストによってブロックされています | キーに `custom_objects.update` 権限があること、および（設定されている場合）ソースIPがキーの許可リストに含まれていることを確認してください。 |
| `429` | レート制限を超過しました | `X-RateLimit-Reset` の後にリトライし、リクエスト頻度を減らしてください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="カスタムオブジェクトの置換エラー" }
{% endapi %}