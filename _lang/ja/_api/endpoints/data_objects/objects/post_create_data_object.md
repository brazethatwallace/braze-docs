---
nav_title: "POST: データオブジェクトを作成"
article_title: "POST: データオブジェクトを作成"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "この記事では、データオブジェクト作成エンドポイントの詳細について説明します。"
---
{% api %}
# データオブジェクトを作成 {#create-data-object}
{% apimethod post %}
/data_objects/objects/{type_name}
{% endapimethod %}

> このエンドポイントを使用して、特定のタイプのデータオブジェクトを1つ作成します。

{% alert important %}
データオブジェクトは現在早期アクセス段階です。データオブジェクトのAPIキー権限が**設定** > **APIキー**に表示されるには、ワークスペースが有効化されている必要があります。
{% endalert %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`data_objects.create` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

このエンドポイントはデータオブジェクト書き込みバケットに含まれており、デフォルトの制限は1分あたり50リクエストです。

## パスパラメーター {#path-parameters}

以下の表は、`/data_objects/objects/{type_name}` エンドポイントのパスパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `type_name` | 必須 | String | データオブジェクトタイプのマシン名 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="データオブジェクト作成のパスパラメーター" }

## リクエストパラメーター {#request-parameters}

以下の表は、`/data_objects/objects/{type_name}` エンドポイントのJSONリクエストボディパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `external_id` | 必須 | String | タイプ内で一意のオブジェクト識別子 |
| `attributes` | 必須 | Object | タイプスキーマに対してバリデーションされるフィールド名をキーとした値 |
| `display_name` | オプション | String | オブジェクトの表示ラベル。タイプに表示名ソースフィールドがある場合、そのフィールドの値が優先されます。デフォルトは `external_id` です |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="データオブジェクト作成のリクエストパラメーター" }

## リクエスト例 {#example-request}

このセクションには、サンプルJSONペイロードとサンプルcURLリクエストが含まれています。

### サンプルリクエストペイロード {#sample-request-payload}

```json
{
  "external_id": "acct-new",
  "attributes": {
    "name": "New Account",
    "industry": "software"
  }
}
```

### サンプルcURLリクエスト {#sample-curl-request}

この例では、識別子 `acct-new` の `account` レコードを作成し、`name` と `industry` 属性を設定します。

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/data_objects/objects/account' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "external_id": "acct-new",
  "attributes": {
    "name": "New Account",
    "industry": "software"
  }
}'
```

## レスポンス {#response}

このセクションには、成功レスポンスのサンプルとレスポンスフィールドが含まれています。

### 成功レスポンス例 {#example-success-response}

ステータスコード `201` は、以下のレスポンスボディを返す可能性があります。

```json
{
  "data_object": {
    "type_name": "account",
    "external_id": "acct-new",
    "attributes": { "name": "New Account", "industry": "software" }
  }
}
```

### レスポンスパラメーター {#response-parameters}

以下の表は、成功レスポンスに含まれるフィールドの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `data_object` | 必須 | Object | 作成されたデータオブジェクトレコード |
| `data_object.type_name` | 必須 | String | データオブジェクトタイプのマシン名 |
| `data_object.external_id` | 必須 | String | データオブジェクト識別子 |
| `data_object.attributes` | 必須 | Object | フィールド名をキーとした格納済みオブジェクト属性 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="データオブジェクト作成のレスポンスパラメーター" }

## エラー {#errors}

以下の表は、このエンドポイントで発生する一般的なエラーとその解決方法の一覧です。

| ステータス | 原因 | ガイダンス |
|---|---|---|
| `400` | 不明な属性フィールドまたは無効な属性タイプ | `attributes` 内のすべてのフィールドがタイプスキーマに存在し、正しいデータ型を使用していることを確認してください。 |
| `404` | タイプが見つかりません (`data-object-type-not-found`) | `type_name` がワークスペースに存在し、マシン名と完全に一致していることを確認してください。 |
| `409` | 重複オブジェクト (`duplicate-data-object`) | 別の `external_id` を使用するか、`PUT` を使用して既存のオブジェクトを置き換えてください。 |
| `422` | レコード制限に到達 (`data-object-record-limit-exceeded`) | タイプのオブジェクト数を削減するか、ワークスペースの制限についてBrazeサポートにお問い合わせください。 |
| `401` | REST APIキーが不足または無効 | `Authorization` ヘッダーで `Bearer YOUR_REST_API_KEY` を使用しており、キーがアクティブであることを確認してください。 |
| `403` | APIキーに権限がないか、許可リストによってリクエストがブロックされています | キーに `data_objects.create` 権限があり、設定されている場合はソースIPがキーの許可リストに含まれていることを確認してください。 |
| `429` | レート制限を超過 | `X-RateLimit-Reset` の後にリトライし、リクエスト頻度を下げてください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="データオブジェクト作成のエラー" }
{% endapi %}