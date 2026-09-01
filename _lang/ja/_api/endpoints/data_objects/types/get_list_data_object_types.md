---
nav_title: "GET: データオブジェクトタイプの一覧"
article_title: "GET: データオブジェクトタイプの一覧"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "この記事では、データオブジェクトタイプの一覧エンドポイントについて詳しく説明します。"
---
{% api %}
# データオブジェクトタイプの一覧 {#list-data-object-types}
{% apimethod get %}
/data_objects/types
{% endapimethod %}

> このエンドポイントを使用して、ワークスペース内のデータオブジェクトタイプを一覧表示します。

{% alert important %}
データオブジェクトは現在早期アクセス中です。データオブジェクトのAPIキー権限が**設定** > **APIキー**に表示されるには、ワークスペースが有効になっている必要があります。
{% endalert %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`data_objects.read` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

このエンドポイントはデータオブジェクト読み取りバケットに属しており、デフォルトの制限は1分あたり50リクエストです。

## クエリパラメーター {#query-parameters}

次の表は、`/data_objects/types` エンドポイントのクエリパラメーターの一覧と説明です。

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `search_term` | 任意 | String | タイプ名に対する大文字小文字を区別しないプレフィックスフィルター |
| `limit` | 任意 | Integer | ページサイズ。デフォルトは `100`。`1` から `250` の範囲に制限されます |
| `offset` | 任意 | Integer | オフセット。デフォルトは `0`。負の値は `0` に切り下げられます |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="データオブジェクトタイプ一覧のクエリパラメーター" }

## リクエスト例 {#example-request}

このセクションには、クエリパラメーターのサンプルペイロードとサンプルcURLリクエストが含まれています。

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

この例では、検索語 `acc` に一致するデータオブジェクトタイプを一覧表示し、1ページあたり2件の結果を返します。

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/data_objects/types?search_term=acc&limit=2&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## レスポンス {#response}

このセクションには、成功時のサンプルレスポンスとレスポンスフィールドが含まれています。

### 成功レスポンスの例 {#example-success-response}

ステータスコード `200` は、以下のレスポンスボディを返す場合があります。

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

`metadata.display_name_source` は、そのタイプに表示名フィールドが設定されている場合に含まれます。

### レスポンスパラメーター {#response-parameters}

次の表は、成功レスポンスに含まれるフィールドの一覧と説明です。

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `items` | 必須 | Array | データオブジェクトタイプレコードのリスト |
| `items[].type_name` | 必須 | String | データオブジェクトタイプのマシン名 |
| `items[].metadata` | 必須 | Object | タイプメタデータオブジェクト |
| `total_count` | 必須 | Integer | 一致するレコードの合計数 |
| `has_more` | 必須 | Boolean | 結果の次のページが利用可能かどうか |
| `next_offset` | 任意 | Integer | `has_more` が `true` の場合の次のページのオフセット |
| `offset` | 必須 | Integer | 現在のページオフセット |
| `limit` | 必須 | Integer | リクエストで使用されたページサイズ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="データオブジェクトタイプ一覧のレスポンスパラメーター" }

## エラー {#errors}

次の表は、このエンドポイントで一般的なエラーとその解決方法の一覧です。

| ステータス | 原因 | ガイダンス |
|---|---|---|
| `400` | 無効なクエリパラメーターのタイプまたは値 | `limit` と `offset` が整数であること、およびすべてのパラメーター値が有効であることを確認してください。 |
| `401` | REST APIキーが欠落しているか無効 | `Authorization` ヘッダーが `Bearer YOUR_REST_API_KEY` を使用しており、キーが有効であることを確認してください。 |
| `403` | APIキーに権限がないか、許可リストによりリクエストがブロックされている | キーに `data_objects.read` 権限があること、および設定されている場合はソースIPがキーの許可リストに含まれていることを確認してください。 |
| `429` | レート制限を超過 | `X-RateLimit-Reset` の後にリトライし、リクエスト頻度を減らしてください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="データオブジェクトタイプ一覧のエラー" }
{% endapi %}