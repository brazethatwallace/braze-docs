---
nav_title: "GET: カスタムオブジェクトタイプの一覧"
article_title: "GET: カスタムオブジェクトタイプの一覧"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "この記事では、カスタムオブジェクトタイプの一覧エンドポイントについて詳しく説明します。"
---
{% api %}
# カスタムオブジェクトタイプの一覧 {#list-custom-object-types}
{% apimethod get %}
/custom_objects/types
{% endapimethod %}

> このエンドポイントを使用して、ワークスペース内のカスタムオブジェクトタイプを一覧表示します。

{% alert important %}
カスタムオブジェクトは現在早期アクセス中です。カスタムオブジェクトのAPIキー権限が**設定** > **APIキー**に表示されるには、ワークスペースが有効化されている必要があります。
{% endalert %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`custom_objects.read` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

このエンドポイントはカスタムオブジェクト読み取りバケットに含まれており、デフォルトの制限は1分あたり50リクエストです。

## クエリパラメーター {#query-parameters}

以下の表は、`/custom_objects/types` エンドポイントのクエリパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `search_term` | 任意 | String | タイプ名に対する大文字小文字を区別しないプレフィックスフィルター |
| `limit` | 任意 | Integer | ページサイズ。デフォルトは `100`。`1` から `250` の範囲に制限されます |
| `offset` | 任意 | Integer | オフセット。デフォルトは `0`。負の値は `0` に切り捨てられます |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="カスタムオブジェクトタイプ一覧のクエリパラメーター" }

## リクエスト例 {#example-request}

このセクションには、サンプルのクエリパラメーターペイロードとサンプルのcURLリクエストが含まれます。

### サンプルリクエストペイロード {#sample-request-payload}

このリクエストのクエリパラメーターの参考として、以下のJSONオブジェクトを使用してください。

```json
{
  "search_term": "acc",
  "limit": 2,
  "offset": 0
}
```

### サンプルcURLリクエスト {#sample-curl-request}

この例では、検索語 `acc` に一致するカスタムオブジェクトタイプを一覧表示し、1ページあたり2件の結果を返します。

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/custom_objects/types?search_term=acc&limit=2&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## レスポンス {#response}

このセクションには、成功レスポンスのサンプルとレスポンスフィールドが含まれます。

### 成功レスポンスの例 {#example-success-response}

ステータスコード `200` は、以下のレスポンスボディを返す可能性があります。

```json
{
  "items": [
    {
      "type_name": "account",
      "metadata": { "display_name_source": "name" }
    },
    {
      "type_name": "contact",
      "metadata": {}
    }
  ],
  "total_count": 2,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 100
}
```

`metadata.display_name_source` は、そのタイプに表示名フィールドが設定されている場合に存在します。

### レスポンスパラメーター {#response-parameters}

以下の表は、成功レスポンスに含まれるフィールドの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `items` | 必須 | Array | カスタムオブジェクトタイプレコードのリスト |
| `items[].type_name` | 必須 | String | カスタムオブジェクトタイプのマシン名 |
| `items[].metadata` | 必須 | Object | タイプメタデータオブジェクト |
| `total_count` | 必須 | Integer | 一致するレコードの合計数 |
| `has_more` | 必須 | Boolean | 結果の次のページが利用可能かどうか |
| `next_offset` | 任意 | Integer | `has_more` が `true` の場合の次のページのオフセット |
| `offset` | 必須 | Integer | 現在のページオフセット |
| `limit` | 必須 | Integer | リクエストで使用されたページサイズ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="カスタムオブジェクトタイプ一覧のレスポンスパラメーター" }

## エラー {#errors}

以下の表は、このエンドポイントで発生する一般的なエラーとその解決方法です。

| ステータス | 原因 | ガイダンス |
|---|---|---|
| `400` | クエリパラメーターの型または値が無効 | `limit` と `offset` が整数であること、およびすべてのパラメーター値が有効であることを確認してください。 |
| `401` | REST APIキーが見つからないか無効 | `Authorization` ヘッダーで `Bearer YOUR_REST_API_KEY` が使用されていること、およびキーが有効であることを確認してください。 |
| `403` | APIキーに権限がない、またはリクエストが許可リストによってブロックされている | キーに `custom_objects.read` 権限があること、および許可リストが設定されている場合はソースIPがキーの許可リストに含まれていることを確認してください。 |
| `429` | レート制限を超過 | `X-RateLimit-Reset` の後にリトライし、リクエスト頻度を下げてください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="カスタムオブジェクトタイプ一覧のエラー" }
{% endapi %}