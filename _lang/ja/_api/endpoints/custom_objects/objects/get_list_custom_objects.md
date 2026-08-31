---
nav_title: "GET: カスタムオブジェクト一覧"
article_title: "GET: カスタムオブジェクト一覧"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "この記事では、カスタムオブジェクト一覧エンドポイントの詳細について説明します。"
---
{% api %}
# カスタムオブジェクト一覧 {#list-custom-objects}
{% apimethod get %}
/custom_objects/objects/{type_name}
{% endapimethod %}

> このエンドポイントを使用して、特定のカスタムオブジェクトタイプのオブジェクトを一覧表示します。

{% alert important %}
カスタムオブジェクトは現在、早期アクセスの段階です。カスタムオブジェクトのAPIキー権限が**設定** > **APIキー**に表示されるには、ワークスペースが有効化されている必要があります。
{% endalert %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`custom_objects.read` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

このエンドポイントはカスタムオブジェクト読み取りバケットに属し、デフォルトの制限は1分あたり50リクエストです。

## パスパラメーター {#path-parameters}

次の表は、`/custom_objects/objects/{type_name}` エンドポイントのパスパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `type_name` | 必須 | String | カスタムオブジェクトタイプのマシン名 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="カスタムオブジェクト一覧のパスパラメーター" }

## クエリパラメーター {#query-parameters}

次の表は、`/custom_objects/objects/{type_name}` エンドポイントのクエリパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `search_term` | オプション | String | オブジェクト識別子に対する部分一致フィルター |
| `limit` | オプション | Integer | ページサイズ。デフォルトは `100`。`1` から `250` の範囲に制限されます |
| `offset` | オプション | Integer | オフセット。デフォルトは `0`。負の値は `0` に切り下げられます |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="カスタムオブジェクト一覧のクエリパラメーター" }

## リクエスト例 {#example-request}

このセクションには、サンプルパラメーターペイロードとサンプルcURLリクエストが含まれています。

### サンプルリクエストペイロード {#sample-request-payload}

リクエストパラメーターのリファレンスとして、以下のJSONオブジェクトを使用してください。

```json
{
  "type_name": "account",
  "search_term": "acct",
  "limit": 100,
  "offset": 0
}
```

### サンプルcURLリクエスト {#sample-curl-request}

この例では、検索語 `acct` に一致する `account` レコードを一覧表示し、結果の最初のページを返します。

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/custom_objects/objects/account?search_term=acct&limit=100&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## レスポンス {#response}

このセクションには、成功レスポンスのサンプルとレスポンスフィールドが含まれています。

### 成功レスポンスの例 {#example-success-response}

ステータスコード `200` は、以下のレスポンスボディを返す場合があります。

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

次の表は、成功レスポンスに含まれるフィールドの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `items` | 必須 | Array | カスタムオブジェクトレコードのリスト |
| `items[].type_name` | 必須 | String | カスタムオブジェクトタイプのマシン名 |
| `items[].external_id` | 必須 | String | カスタムオブジェクト識別子 |
| `items[].attributes` | 必須 | Object | フィールド名をキーとするオブジェクト属性 |
| `total_count` | 必須 | Integer | 一致するレコードの合計数 |
| `has_more` | 必須 | Boolean | 結果の次のページが利用可能かどうか |
| `next_offset` | オプション | Integer | `has_more` が `true` の場合の次のページのオフセット |
| `offset` | 必須 | Integer | 現在のページオフセット |
| `limit` | 必須 | Integer | リクエストで使用されたページサイズ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="カスタムオブジェクト一覧のレスポンスパラメーター" }

## エラー {#errors}

次の表は、このエンドポイントの一般的なエラーとその解決方法の一覧です。

| ステータス | 原因 | ガイダンス |
|---|---|---|
| `404` | タイプが見つかりません（`custom-object-type-not-found`） | `type_name` がワークスペースに存在し、マシン名と完全に一致していることを確認してください。 |
| `401` | REST APIキーが未設定または無効です | `Authorization` ヘッダーで `Bearer YOUR_REST_API_KEY` が使用されていること、およびキーが有効であることを確認してください。 |
| `403` | APIキーに権限がない、または許可リストによってリクエストがブロックされています | キーに `custom_objects.read` 権限があること、および設定されている場合はソースIPがキーの許可リストに含まれていることを確認してください。 |
| `429` | レート制限を超過しました | `X-RateLimit-Reset` の後にリトライし、リクエスト頻度を下げてください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="カスタムオブジェクト一覧のエラー" }
{% endapi %}