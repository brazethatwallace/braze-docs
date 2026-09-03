---
nav_title: "GET: データオブジェクトの一覧取得"
article_title: "GET: データオブジェクトの一覧取得"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "この記事では、データオブジェクトの一覧取得エンドポイントの詳細について説明します。"
---
{% api %}
# データオブジェクトの一覧取得 {#list-data-objects}
{% apimethod get %}
/data_objects/objects/{type_name}
{% endapimethod %}

> このエンドポイントを使用して、特定のデータオブジェクトタイプのオブジェクトを一覧取得します。

{% alert important %}
データオブジェクトは現在早期アクセス段階です。データオブジェクトAPIキーの権限が**設定** > **APIキー**に表示されるには、ワークスペースが有効化されている必要があります。
{% endalert %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`data_objects.read` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

このエンドポイントはデータオブジェクト読み取りバケットに属しており、デフォルトの制限は1分あたり50リクエストです。

## パスパラメーター {#path-parameters}

以下の表は、`/data_objects/objects/{type_name}` エンドポイントのパスパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `type_name` | 必須 | String | データオブジェクトタイプのマシン名 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="データオブジェクトの一覧取得パスパラメーター" }

## クエリパラメーター {#query-parameters}

以下の表は、`/data_objects/objects/{type_name}` エンドポイントのクエリパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `search_term` | オプション | String | オブジェクト識別子に対する部分文字列フィルター |
| `limit` | オプション | Integer | ページサイズ。デフォルトは `100`。`1` から `250` の範囲に制限されます |
| `offset` | オプション | Integer | オフセット。デフォルトは `0`。負の値は `0` に切り上げられます |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="データオブジェクトの一覧取得クエリパラメーター" }

## リクエスト例 {#example-request}

このセクションでは、サンプルのパラメーターペイロードとサンプルのcURLリクエストを示します。

### サンプルリクエストペイロード {#sample-request-payload}

リクエストパラメーターの参考として、以下のJSONオブジェクトを使用してください。

```json
{
  "type_name": "account",
  "search_term": "acct",
  "limit": 100,
  "offset": 0
}
```

### サンプルcURLリクエスト {#sample-curl-request}

この例では、検索語 `acct` に一致する `account` レコードを一覧取得し、結果の最初のページを返します。

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/data_objects/objects/account?search_term=acct&limit=100&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## レスポンス {#response}

このセクションでは、成功時のレスポンス例とレスポンスフィールドを示します。

### 成功レスポンス例 {#example-success-response}

ステータスコード `200` は、以下のレスポンスボディを返す可能性があります。

```json
{
  "items": [
    {
      "type_name": "account",
      "external_id": "acct-123",
      "attributes": { "name": "Acme", "industry": "software" }
    }
  ],
  "total_count": 1,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 100
}
```

### レスポンスパラメーター {#response-parameters}

以下の表は、成功時のレスポンスに含まれるフィールドの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `items` | 必須 | Array | データオブジェクトレコードのリスト |
| `items[].type_name` | 必須 | String | データオブジェクトタイプのマシン名 |
| `items[].external_id` | 必須 | String | データオブジェクト識別子 |
| `items[].attributes` | 必須 | Object | フィールド名をキーとするオブジェクト属性 |
| `total_count` | 必須 | Integer | 一致するレコードの合計数 |
| `has_more` | 必須 | Boolean | 結果の次のページが存在するかどうか |
| `next_offset` | オプション | Integer | `has_more` が `true` の場合の次のページのオフセット |
| `offset` | 必須 | Integer | 現在のページオフセット |
| `limit` | 必須 | Integer | リクエストで使用されたページサイズ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="データオブジェクトの一覧取得レスポンスパラメーター" }

## エラー {#errors}

以下の表は、このエンドポイントで発生する一般的なエラーとその解決方法の一覧です。

| ステータス | 原因 | 対応方法 |
|---|---|---|
| `404` | タイプが見つからない (`data-object-type-not-found`) | `type_name` がワークスペースに存在し、マシン名と完全に一致していることを確認してください。 |
| `401` | REST APIキーが未指定または無効 | `Authorization` ヘッダーで `Bearer YOUR_REST_API_KEY` が使用されていること、およびキーが有効であることを確認してください。 |
| `403` | APIキーに権限がない、またはリクエストが許可リストでブロックされている | キーに `data_objects.read` 権限があること、また許可リストが設定されている場合はソースIPが許可リストに含まれていることを確認してください。 |
| `429` | レート制限超過 | `X-RateLimit-Reset` の後にリトライし、リクエスト頻度を下げてください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="データオブジェクトの一覧取得エラー" }
{% endapi %}