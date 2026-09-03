---
nav_title: "GET: データオブジェクトの取得"
article_title: "GET: データオブジェクトの取得"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "この記事では、データオブジェクトの取得エンドポイントについて詳しく説明します。"
---
{% api %}
# データオブジェクトの取得 {#get-data-object}
{% apimethod get %}
/data_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> このエンドポイントを使用して、1つのデータオブジェクトを返します。

{% alert important %}
データオブジェクトは現在、早期アクセス段階です。データオブジェクトのAPIキー権限が**設定** > **APIキー**に表示されるようにするには、ワークスペースを有効にする必要があります。
{% endalert %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`data_objects.read` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

このエンドポイントはデータオブジェクト読み取りバケットに属し、デフォルトの制限は1分あたり50リクエストです。

## パスパラメーター {#path-parameters}

以下の表は、`/data_objects/objects/{type_name}/{external_id}` エンドポイントのパスパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `type_name` | 必須 | 文字列 | データオブジェクトタイプのマシン名 |
| `external_id` | 必須 | 文字列 | オブジェクト識別子 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="データオブジェクト取得のパスパラメーター" }

## リクエスト例 {#example-request}

このセクションには、サンプルのパスパラメーターペイロードとサンプルのcURLリクエストが含まれています。

### サンプルリクエストペイロード {#sample-request-payload}

このリクエストのパスパラメーターのリファレンスとして、以下のJSONオブジェクトを使用してください。

```json
{
  "type_name": "account",
  "external_id": "acct-123"
}
```

### サンプルcURLリクエスト {#sample-curl-request}

この例では、`acct-123` のアカウントレコードとその保存済み属性を取得します。

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## レスポンス {#response}

このセクションには、成功レスポンスのサンプルとレスポンスフィールドが含まれています。

### 成功レスポンスの例 {#example-success-response}

ステータスコード `200` は、以下のレスポンスボディを返す可能性があります。

```json
{
  "data_object": {
    "type_name": "account",
    "external_id": "acct-123",
    "attributes": { "name": "Acme", "industry": "software" }
  }
}
```

### レスポンスパラメーター {#response-parameters}

以下の表は、成功レスポンスに含まれるフィールドの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `data_object` | 必須 | オブジェクト | 返されたデータオブジェクトレコード |
| `data_object.type_name` | 必須 | 文字列 | データオブジェクトタイプのマシン名 |
| `data_object.external_id` | 必須 | 文字列 | データオブジェクト識別子 |
| `data_object.attributes` | 必須 | オブジェクト | フィールド名をキーとしたオブジェクト属性 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="データオブジェクト取得のレスポンスパラメーター" }

## エラー {#errors}

以下の表は、このエンドポイントで発生する一般的なエラーとその解決方法の一覧です。

| ステータス | 原因 | ガイダンス |
|---|---|---|
| `404` | タイプが見つからない (`data-object-type-not-found`) またはオブジェクトが見つからない (`data-object-not-found`) | `type_name` と `external_id` の両方がワークスペースに存在することを確認してください。 |
| `401` | REST APIキーが不足または無効 | `Authorization` ヘッダーが `Bearer YOUR_REST_API_KEY` を使用しており、キーがアクティブであることを確認してください。 |
| `403` | APIキーに権限がないか、許可リストによってリクエストがブロックされている | キーに `data_objects.read` 権限があること、および設定されている場合はソースIPがキーの許可リストに含まれていることを確認してください。 |
| `429` | レート制限超過 | `X-RateLimit-Reset` の後にリトライし、リクエスト頻度を減らしてください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="データオブジェクト取得のエラー" }
{% endapi %}