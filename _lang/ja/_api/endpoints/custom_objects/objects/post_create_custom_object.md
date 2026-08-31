---
nav_title: "POST: カスタムオブジェクトの作成"
article_title: "POST: カスタムオブジェクトの作成"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "この記事では、カスタムオブジェクトの作成エンドポイントについて詳しく説明します。"
---
{% api %}
# カスタムオブジェクトの作成 {#create-custom-object}
{% apimethod post %}
/custom_objects/objects/{type_name}
{% endapimethod %}

> このエンドポイントを使用して、あるタイプに対して1つのカスタムオブジェクトを作成します。

{% alert important %}
カスタムオブジェクトは現在早期アクセス段階です。カスタムオブジェクトのAPIキー権限が**設定** > **APIキー**に表示されるには、ワークスペースを有効にする必要があります。
{% endalert %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`custom_objects.create` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

このエンドポイントはカスタムオブジェクト書き込みバケットに含まれ、デフォルトの制限は1分あたり50リクエストです。

## パスパラメーター {#path-parameters}

以下の表は、`/custom_objects/objects/{type_name}` エンドポイントのパスパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `type_name` | 必須 | 文字列 | カスタムオブジェクトタイプのマシン名 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="カスタムオブジェクト作成のパスパラメーター" }

## リクエストパラメーター {#request-parameters}

以下の表は、`/custom_objects/objects/{type_name}` エンドポイントのJSONリクエストボディパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `external_id` | 必須 | 文字列 | タイプ内で一意のオブジェクト識別子 |
| `attributes` | 必須 | オブジェクト | タイプスキーマに対して検証されるフィールド名キーの値 |
| `display_name` | 任意 | 文字列 | オブジェクトの表示ラベル。タイプに表示名ソースフィールドがある場合、そのフィールドの値が優先されます。デフォルトは `external_id` です |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="カスタムオブジェクト作成のリクエストパラメーター" }

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

この例では、識別子 `acct-new` を持つ `account` レコードを作成し、`name` および `industry` 属性を設定します。

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/custom_objects/objects/account' \
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

このセクションには、成功レスポンスの例とレスポンスフィールドが含まれています。

### 成功レスポンスの例 {#example-success-response}

ステータスコード `201` は以下のレスポンスボディを返す可能性があります。

```json
{
  "custom_object": {
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
| `custom_object` | 必須 | オブジェクト | 作成されたカスタムオブジェクトレコード |
| `custom_object.type_name` | 必須 | 文字列 | カスタムオブジェクトタイプのマシン名 |
| `custom_object.external_id` | 必須 | 文字列 | カスタムオブジェクト識別子 |
| `custom_object.attributes` | 必須 | オブジェクト | フィールド名をキーとする保存済みオブジェクト属性 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="カスタムオブジェクト作成のレスポンスパラメーター" }

## エラー {#errors}

以下の表は、このエンドポイントの一般的なエラーとその解決方法の一覧です。

| ステータス | 原因 | ガイダンス |
|---|---|---|
| `400` | 不明な属性フィールドまたは無効な属性タイプ | `attributes` 内のすべてのフィールドがタイプスキーマに存在し、正しいデータ型を使用していることを確認してください。 |
| `404` | タイプが見つかりません (`custom-object-type-not-found`) | `type_name` がワークスペースに存在し、マシン名と完全に一致していることを確認してください。 |
| `409` | 重複オブジェクト (`duplicate-custom-object`) | 別の `external_id` を使用するか、`PUT` を使用して既存のオブジェクトを置き換えてください。 |
| `422` | レコード数の上限に達しました (`custom-object-record-limit-exceeded`) | そのタイプのオブジェクト数を減らすか、ワークスペースの制限についてBrazeサポートにお問い合わせください。 |
| `401` | REST APIキーが見つからないか無効です | `Authorization` ヘッダーが `Bearer YOUR_REST_API_KEY` を使用しており、キーがアクティブであることを確認してください。 |
| `403` | APIキーに権限がないか、許可リストによってリクエストがブロックされています | キーに `custom_objects.create` 権限があり、設定されている場合はソースIPがキーの許可リストに含まれていることを確認してください。 |
| `429` | レート制限を超過しました | `X-RateLimit-Reset` の後に再試行し、リクエスト頻度を下げてください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="カスタムオブジェクト作成のエラー" }
{% endapi %}