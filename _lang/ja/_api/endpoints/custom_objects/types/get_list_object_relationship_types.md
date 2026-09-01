---
nav_title: "GET: オブジェクトリレーションシップタイプの一覧取得"
article_title: "GET: オブジェクトリレーションシップタイプの一覧取得"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、オブジェクトリレーションシップタイプの一覧取得エンドポイントについて説明します。"
---
{% api %}
# オブジェクトリレーションシップタイプの一覧取得 {#list-object-relationship-types}
{% apimethod get %}
/custom_objects/types/{type_name}/object_relationship_types
{% endapimethod %}

> このエンドポイントを使用して、指定されたアンカー方向に対するオブジェクト間リンクで利用可能なリレーションシップの種類を一覧取得します。

{% alert important %}
カスタムオブジェクトは現在、早期アクセス段階です。カスタムオブジェクトのAPIキー権限が**設定** > **APIキー**に表示されるには、ワークスペースが有効化されている必要があります。
{% endalert %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`custom_objects.read` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

このエンドポイントはカスタムオブジェクト読み取りバケットに属しており、デフォルトの制限は1分あたり50リクエストです。

## パスパラメーター {#path-parameters}

以下の表は、`/custom_objects/types/{type_name}/object_relationship_types` エンドポイントのパスパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `type_name` | 必須 | String | カスタムオブジェクトタイプのマシン名 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="オブジェクトリレーションシップタイプの一覧取得パスパラメーター" }

## クエリパラメーター {#query-parameters}

以下の表は、`/custom_objects/types/{type_name}/object_relationship_types` エンドポイントのクエリパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `anchor` | オプション | String | `source`（デフォルト）または `target` |
| `limit` | オプション | Integer | ページサイズ。デフォルトは `100`。`1` から `250` の範囲に制限されます |
| `offset` | オプション | Integer | オフセット。デフォルトは `0`。負の値は `0` に切り上げられます |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="オブジェクトリレーションシップタイプの一覧取得クエリパラメーター" }

## リクエスト例 {#example-request}

このセクションには、サンプルパラメーターペイロードとサンプルcURLリクエストが含まれます。

### サンプルリクエストペイロード {#sample-request-payload}

リクエストパラメーターの参考として、以下のJSONオブジェクトを使用してください。

```json
{
  "type_name": "account",
  "anchor": "source",
  "limit": 10,
  "offset": 0
}
```

### サンプルcURLリクエスト {#sample-curl-request}

この例では、`account` タイプがリレーションシップのソースである場合に、`account` タイプで利用可能なオブジェクトリレーションシップの種類を一覧取得します。

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/custom_objects/types/account/object_relationship_types?anchor=source&limit=10&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## レスポンス {#response}

このセクションには、成功レスポンスのサンプルとレスポンスフィールドが含まれます。

### 成功レスポンスの例 {#example-success-response}

ステータスコード `200` は以下のレスポンスボディを返す可能性があります。

```json
{
  "items": [
    {
      "from_type_name": "account",
      "to_type_name": "account",
      "rel_kind": "subaccount",
      "display_name": "subaccount",
      "related_type_name": "account"
    }
  ],
  "total_count": 1,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 10
}
```

`related_type_name` は、選択した `anchor` に対するリレーションシップの反対側のタイプです。

### レスポンスパラメーター {#response-parameters}

以下の表は、成功レスポンスに含まれるフィールドの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `items` | 必須 | Array | 利用可能なオブジェクトリレーションシップタイプの一覧 |
| `items[].from_type_name` | 必須 | String | ソースのカスタムオブジェクトタイプ名 |
| `items[].to_type_name` | 必須 | String | ターゲットのカスタムオブジェクトタイプ名 |
| `items[].rel_kind` | 必須 | String | リレーションシップの種類の値 |
| `items[].display_name` | 必須 | String | リレーションシップの種類の表示ラベル |
| `items[].related_type_name` | 必須 | String | リクエストされた `anchor` に対する反対側のタイプ |
| `total_count` | 必須 | Integer | 一致するレコードの合計数 |
| `has_more` | 必須 | Boolean | 次のページの結果が利用可能かどうか |
| `next_offset` | オプション | Integer | `has_more` が `true` の場合の次のページのオフセット |
| `offset` | 必須 | Integer | 現在のページオフセット |
| `limit` | 必須 | Integer | リクエストで使用されたページサイズ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="オブジェクトリレーションシップタイプの一覧取得レスポンスパラメーター" }

## エラー {#errors}

以下の表は、このエンドポイントの一般的なエラーとその解決方法の一覧です。

| ステータス | 原因 | ガイダンス |
|---|---|---|
| `400` | 無効な `anchor` | `anchor` には `source` または `target` を使用してください。 |
| `404` | タイプが見つかりません（`custom-object-type-not-found`） | `type_name` がワークスペースに存在し、マシン名と完全に一致していることを確認してください。 |
| `401` | REST APIキーが欠落しているか無効です | `Authorization` ヘッダーで `Bearer YOUR_REST_API_KEY` を使用していること、およびキーがアクティブであることを確認してください。 |
| `403` | APIキーに権限がないか、許可リストによってリクエストがブロックされています | キーに `custom_objects.read` 権限があること、および設定されている場合はソースIPがキーの許可リストに含まれていることを確認してください。 |
| `429` | レート制限を超過しました | `X-RateLimit-Reset` の後に再試行し、リクエスト頻度を下げてください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="オブジェクトリレーションシップタイプの一覧取得エラー" }
{% endapi %}