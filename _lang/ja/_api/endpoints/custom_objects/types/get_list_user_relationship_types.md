---
nav_title: "GET: ユーザーリレーションシップタイプの一覧"
article_title: "GET: ユーザーリレーションシップタイプの一覧"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "この記事では、ユーザーリレーションシップタイプの一覧エンドポイントの詳細について説明します。"
---
{% api %}
# ユーザーリレーションシップタイプの一覧 {#list-user-relationship-types}
{% apimethod get %}
/custom_objects/types/{type_name}/user_relationship_types
{% endapimethod %}

> このエンドポイントを使用して、カスタムオブジェクトタイプのユーザーリレーションシップに対する有効な `rel_kind` 値を一覧表示します。

{% alert important %}
カスタムオブジェクトは現在、早期アクセス段階です。カスタムオブジェクトのAPIキー権限が**設定** > **APIキー**に表示されるには、ワークスペースが有効になっている必要があります。
{% endalert %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`custom_objects.read` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

このエンドポイントは、カスタムオブジェクト読み取りバケットに含まれ、デフォルトで1分あたり50リクエストの制限があります。

## パスパラメーター {#path-parameters}

以下の表は、`/custom_objects/types/{type_name}/user_relationship_types` エンドポイントのパスパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `type_name` | 必須 | 文字列 | カスタムオブジェクトタイプのマシン名 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="ユーザーリレーションシップタイプの一覧パスパラメーター" }

## クエリパラメーター {#query-parameters}

以下の表は、`/custom_objects/types/{type_name}/user_relationship_types` エンドポイントのクエリパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `limit` | オプション | 整数 | ページサイズ。デフォルトは `100`。`1` ～ `250` の範囲に制限されます |
| `offset` | オプション | 整数 | オフセット。デフォルトは `0`。負の値は `0` に切り捨てられます |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="ユーザーリレーションシップタイプの一覧クエリパラメーター" }

## リクエスト例 {#example-request}

このセクションには、サンプルパラメーターペイロードとサンプルcURLリクエストが含まれています。

### サンプルリクエストペイロード {#sample-request-payload}

リクエストパラメーターのリファレンスとして、以下のJSONオブジェクトを使用してください。

```json
{
  "type_name": "account",
  "limit": 100,
  "offset": 0
}
```

### サンプルcURLリクエスト {#sample-curl-request}

この例では、ユーザーを `account` レコードにリンクするために使用できるユーザーリレーションシップの種類を一覧表示します。

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/custom_objects/types/account/user_relationship_types?limit=100&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## レスポンス {#response}

このセクションには、成功レスポンスのサンプルとレスポンスフィールドが含まれています。

### 成功レスポンスの例 {#example-success-response}

ステータスコード `200` は以下のレスポンスボディを返す可能性があります。

```json
{
  "items": [
    { "rel_kind": "account_user", "display_name": "account_user" }
  ],
  "total_count": 1,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 100
}
```

`display_name` は現在 `rel_kind` と一致します。

### レスポンスパラメーター {#response-parameters}

以下の表は、成功レスポンスに含まれるフィールドの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `items` | 必須 | 配列 | 利用可能なユーザーリレーションシップタイプの一覧 |
| `items[].rel_kind` | 必須 | 文字列 | ユーザーリレーションシップの種類の値 |
| `items[].display_name` | 必須 | 文字列 | リレーションシップの種類の表示ラベル |
| `total_count` | 必須 | 整数 | 一致するレコードの総数 |
| `has_more` | 必須 | ブール値 | 次のページの結果が利用可能かどうか |
| `next_offset` | オプション | 整数 | `has_more` が `true` の場合の次のページのオフセット |
| `offset` | 必須 | 整数 | 現在のページオフセット |
| `limit` | 必須 | 整数 | リクエストで使用されたページサイズ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="ユーザーリレーションシップタイプの一覧レスポンスパラメーター" }

## エラー {#errors}

以下の表は、このエンドポイントで発生する一般的なエラーとその解決方法の一覧です。

| ステータス | 原因 | ガイダンス |
|---|---|---|
| `404` | タイプが見つかりません (`custom-object-type-not-found`) | `type_name` がワークスペースに存在し、マシン名と完全に一致していることを確認してください。 |
| `401` | REST APIキーが不足しているか無効です | `Authorization` ヘッダーが `Bearer YOUR_REST_API_KEY` を使用しており、キーがアクティブであることを確認してください。 |
| `403` | APIキーに権限がないか、許可リストによりリクエストがブロックされています | キーに `custom_objects.read` 権限があること、および設定されている場合はソースIPがキーの許可リストに含まれていることを確認してください。 |
| `429` | レート制限を超過しました | `X-RateLimit-Reset` 後にリトライし、リクエスト頻度を減らしてください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ユーザーリレーションシップタイプの一覧エラー" }
{% endapi %}