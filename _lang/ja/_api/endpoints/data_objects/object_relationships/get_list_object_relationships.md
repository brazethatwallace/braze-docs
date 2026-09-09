---
nav_title: "GET: オブジェクトリレーションシップの一覧取得"
article_title: "GET: オブジェクトリレーションシップの一覧取得"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "この記事では、オブジェクトリレーションシップの一覧取得エンドポイントについて詳しく説明します。"
---
{% api %}
# オブジェクトリレーションシップの一覧取得 {#list-object-relationships}
{% apimethod get %}
/data_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> このエンドポイントを使用して、1つのオブジェクトアンカーから関連するデータオブジェクトを一覧取得します。

{% alert important %}
データオブジェクトは現在、早期アクセス段階です。データオブジェクトのAPIキー権限が**設定** > **APIキー**に表示されるようにするには、ワークスペースを有効にする必要があります。
{% endalert %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`data_objects.read` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

このエンドポイントはデータオブジェクト読み取りバケットに属しており、デフォルトのリミットは1分あたり50リクエストです。

## パスパラメーター {#path-parameters}

以下の表は、`/data_objects/objects/{type_name}/{external_id}/object_relationships` エンドポイントのパスパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `type_name` | 必須 | String | ソースオブジェクトタイプ |
| `external_id` | 必須 | String | ソースオブジェクト識別子 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="オブジェクトリレーションシップ一覧取得のパスパラメーター" }

## クエリパラメーター {#query-parameters}

以下の表は、`/data_objects/objects/{type_name}/{external_id}/object_relationships` エンドポイントのクエリパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `anchor` | オプション | String | `source`（デフォルト）または `target` |
| `rel_kind` | オプション | String | 1つのリレーションシップ種別でフィルターします |
| `limit` | オプション | Integer | ページサイズ。デフォルトは `100`。`1` から `250` の範囲に制限されます |
| `offset` | オプション | Integer | オフセット。デフォルトは `0`。負の値は `0` に切り下げられます |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="オブジェクトリレーションシップ一覧取得のクエリパラメーター" }

## リクエスト例 {#example-request}

このセクションには、サンプルパラメーターペイロードとサンプルcURLリクエストが含まれています。

### サンプルリクエストペイロード {#sample-request-payload}

リクエストパラメーターの参考として、以下のJSONオブジェクトを使用してください。

```json
{
  "type_name": "account",
  "external_id": "acct-123",
  "anchor": "source",
  "rel_kind": "subaccount",
  "limit": 100,
  "offset": 0
}
```

### サンプルcURLリクエスト {#sample-curl-request}

この例では、`acct-123` がリンクしている `subaccount` レコードを一覧取得し、最初のページの結果を返します。

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/object_relationships?anchor=source&rel_kind=subaccount&limit=100&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## レスポンス {#response}

このセクションには、成功レスポンスのサンプルとレスポンスフィールドが含まれています。

### 成功レスポンス例 {#example-success-response}

ステータスコード `200` は、以下のレスポンスボディを返す可能性があります。

```json
{
  "items": [
    {
      "rel_kind": "subaccount",
      "to_data_object": {
        "type_name": "account",
        "external_id": "acct-456",
        "attributes": { "name": "Child Account" }
      },
      "attributes": {}
    }
  ],
  "total_count": 1,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 100
}
```

`anchor=target` の場合、関連オブジェクトは `from_data_object` として返されます。

### レスポンスパラメーター {#response-parameters}

以下の表は、成功レスポンスに含まれるフィールドの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `items` | 必須 | Array | オブジェクトリレーションシップレコードのリスト |
| `items[].rel_kind` | 必須 | String | リレーションシップ種別の値 |
| `items[].to_data_object` | 条件付き | Object | `anchor=source` の場合の関連オブジェクト |
| `items[].from_data_object` | 条件付き | Object | `anchor=target` の場合の関連オブジェクト |
| `items[].to_data_object.type_name` | 条件付き | String | 関連オブジェクトのタイプ名 |
| `items[].to_data_object.external_id` | 条件付き | String | 関連オブジェクトのexternal ID |
| `items[].to_data_object.attributes` | 条件付き | Object | 関連オブジェクトの属性 |
| `items[].from_data_object.type_name` | 条件付き | String | 関連オブジェクトのタイプ名 |
| `items[].from_data_object.external_id` | 条件付き | String | 関連オブジェクトのexternal ID |
| `items[].from_data_object.attributes` | 条件付き | Object | 関連オブジェクトの属性 |
| `items[].attributes` | 必須 | Object | リレーションシップの属性 |
| `total_count` | 必須 | Integer | 一致するレコードの合計数 |
| `has_more` | 必須 | Boolean | 次のページの結果が利用可能かどうか |
| `next_offset` | オプション | Integer | `has_more` が `true` の場合の次のページのオフセット |
| `offset` | 必須 | Integer | 現在のページオフセット |
| `limit` | 必須 | Integer | リクエストで使用されたページサイズ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="オブジェクトリレーションシップ一覧取得のレスポンスパラメーター" }

## エラー {#errors}

以下の表は、このエンドポイントで発生する一般的なエラーとその解決方法の一覧です。

| ステータス | 原因 | ガイダンス |
|---|---|---|
| `400` | 無効な `anchor` | `anchor` には `source` または `target` を使用してください。 |
| `404` | タイプまたはオブジェクトが見つかりません | `type_name` と `external_id` がどちらもワークスペースに存在することを確認してください。 |
| `401` | REST APIキーがないか無効です | `Authorization` ヘッダーが `Bearer YOUR_REST_API_KEY` を使用していること、およびキーが有効であることを確認してください。 |
| `403` | APIキーに権限がないか、許可リストによりリクエストがブロックされています | キーが `data_objects.read` 権限を持っていること、および設定されている場合はソースIPがキーの許可リストに含まれていることを確認してください。 |
| `429` | レート制限を超過しました | `X-RateLimit-Reset` の後にリトライし、リクエスト頻度を減らしてください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="オブジェクトリレーションシップ一覧取得のエラー" }
{% endapi %}