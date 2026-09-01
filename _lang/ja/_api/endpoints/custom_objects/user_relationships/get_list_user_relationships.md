---
nav_title: "GET: ユーザーリレーションシップの一覧"
article_title: "GET: ユーザーリレーションシップの一覧"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "この記事では、ユーザーリレーションシップの一覧エンドポイントについて説明します。"
---
{% api %}
# ユーザーリレーションシップの一覧 {#list-user-relationships}
{% apimethod get %}
/custom_objects/objects/{type_name}/{external_id}/user_relationships
{% endapimethod %}

> このエンドポイントを使用して、1つのカスタムオブジェクトにリンクされたユーザーを一覧表示します。

{% alert important %}
カスタムオブジェクトは現在、早期アクセス段階です。カスタムオブジェクトのAPIキー権限が**設定** > **APIキー**に表示されるには、ワークスペースが有効になっている必要があります。
{% endalert %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`custom_objects.user_relationships.read` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

このエンドポイントはカスタムオブジェクトの読み取りバケットに含まれ、デフォルトの制限は1分あたり50リクエストです。

## パスパラメーター {#path-parameters}

以下の表は、`/custom_objects/objects/{type_name}/{external_id}/user_relationships` エンドポイントのパスパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `type_name` | 必須 | String | オブジェクトタイプ |
| `external_id` | 必須 | String | オブジェクト識別子 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="ユーザーリレーションシップの一覧パスパラメーター" }

## クエリパラメーター {#query-parameters}

以下の表は、`/custom_objects/objects/{type_name}/{external_id}/user_relationships` エンドポイントのクエリパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `rel_kind` | オプション | String | リレーションシップの種類でフィルター |
| `limit` | オプション | Integer | ページサイズ。デフォルトは `100`。`1` から `250` の範囲に制限されます |
| `offset` | オプション | Integer | オフセット。デフォルトは `0`。負の値は `0` に切り上げられます |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="ユーザーリレーションシップの一覧クエリパラメーター" }

## リクエスト例 {#example-request}

このセクションでは、サンプルパラメーターペイロードとサンプルcURLリクエストを紹介します。

### サンプルリクエストペイロード {#sample-request-payload}

リクエストパラメーターの参考として、以下のJSONオブジェクトを使用してください。

```json
{
  "type_name": "account",
  "external_id": "acct-123",
  "rel_kind": "account_user",
  "limit": 100,
  "offset": 0
}
```

### サンプルcURLリクエスト {#sample-curl-request}

この例では、`account_user` リレーションシップを通じて `acct-123` にリンクされたユーザーを一覧表示します。

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123/user_relationships?rel_kind=account_user&limit=100&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## レスポンス {#response}

このセクションでは、成功レスポンスの例とレスポンスフィールドを紹介します。

### 成功レスポンスの例 {#example-success-response}

ステータスコード `200` は以下のレスポンスボディを返す場合があります。

```json
{
  "items": [
    {
      "type_name": "account",
      "external_id": "acct-123",
      "rel_kind": "account_user",
      "user": { "braze_id": "507f1f77bcf86cd799439011" },
      "attributes": { "role": "admin" }
    }
  ],
  "total_count": 1,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 100
}
```

`user` ペイロードには `braze_id` のみが含まれます。

### レスポンスパラメーター {#response-parameters}

以下の表は、成功レスポンスのフィールドの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `items` | 必須 | Array | ユーザーリレーションシップレコードのリスト |
| `items[].type_name` | 必須 | String | カスタムオブジェクトタイプのマシン名 |
| `items[].external_id` | 必須 | String | カスタムオブジェクト識別子 |
| `items[].rel_kind` | 必須 | String | リレーションシップの種類の値 |
| `items[].user` | 必須 | Object | リンクされたユーザーオブジェクト |
| `items[].user.braze_id` | 必須 | String | Brazeユーザー識別子 |
| `items[].attributes` | 必須 | Object | リレーションシップ属性 |
| `total_count` | 必須 | Integer | 一致するレコードの合計数 |
| `has_more` | 必須 | Boolean | 結果の次のページがあるかどうか |
| `next_offset` | オプション | Integer | `has_more` が `true` の場合の次のページのオフセット |
| `offset` | 必須 | Integer | 現在のページオフセット |
| `limit` | 必須 | Integer | リクエストで使用されたページサイズ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="ユーザーリレーションシップの一覧レスポンスパラメーター" }

## エラー {#errors}

以下の表は、このエンドポイントの一般的なエラーとその解決方法の一覧です。

| ステータス | 原因 | ガイダンス |
|---|---|---|
| `404` | タイプまたはオブジェクトが見つかりません | `type_name` と `external_id` の両方がワークスペースに存在することを確認してください。 |
| `401` | REST APIキーが不足または無効です | `Authorization` ヘッダーが `Bearer YOUR_REST_API_KEY` を使用しており、キーが有効であることを確認してください。 |
| `403` | APIキーに権限がないか、許可リストによってリクエストがブロックされています | キーに `custom_objects.user_relationships.read` 権限があること、および設定済みの場合はソースIPがキーの許可リストに含まれていることを確認してください。 |
| `429` | レート制限を超えました | `X-RateLimit-Reset` の後に再試行し、リクエスト頻度を下げてください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ユーザーリレーションシップの一覧エラー" }
{% endapi %}