---
nav_title: "GET: カスタムオブジェクトの取得"
article_title: "GET: カスタムオブジェクトの取得"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "この記事では、カスタムオブジェクトの取得エンドポイントについて詳しく説明します。"
---
{% api %}
# カスタムオブジェクトの取得 {#get-custom-object}
{% apimethod get %}
/custom_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> このエンドポイントを使用して、1つのカスタムオブジェクトを返します。

{% alert important %}
カスタムオブジェクトは現在早期アクセス段階です。カスタムオブジェクトのAPIキー権限が**設定** > **APIキー**に表示されるには、ワークスペースが有効化されている必要があります。
{% endalert %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`custom_objects.read` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

このエンドポイントはカスタムオブジェクト読み取りバケットに含まれ、デフォルトの制限は1分あたり50リクエストです。

## パスパラメーター {#path-parameters}

以下の表は、`/custom_objects/objects/{type_name}/{external_id}` エンドポイントのパスパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `type_name` | 必須 | String | カスタムオブジェクトタイプのマシン名 |
| `external_id` | 必須 | String | オブジェクト識別子 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="カスタムオブジェクト取得のパスパラメーター" }

## リクエスト例 {#example-request}

このセクションには、サンプルのパスパラメーターペイロードとサンプルのcURLリクエストが含まれています。

### サンプルリクエストペイロード {#sample-request-payload}

このリクエストのパスパラメーターの参考として、以下のJSONオブジェクトを使用してください。

```json
{
  "type_name": "account",
  "external_id": "acct-123"
}
```

### サンプルcURLリクエスト {#sample-curl-request}

この例では、`acct-123` のアカウントレコードとその保存済み属性を取得します。

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## レスポンス {#response}

このセクションには、成功レスポンスのサンプルとレスポンスフィールドが含まれています。

### 成功レスポンスの例 {#example-success-response}

ステータスコード `200` は、以下のレスポンスボディを返す可能性があります。

```json
{
  "custom_object": {
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
| `custom_object` | 必須 | Object | 返されたカスタムオブジェクトレコード |
| `custom_object.type_name` | 必須 | String | カスタムオブジェクトタイプのマシン名 |
| `custom_object.external_id` | 必須 | String | カスタムオブジェクト識別子 |
| `custom_object.attributes` | 必須 | Object | フィールド名をキーとするオブジェクト属性 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="カスタムオブジェクト取得のレスポンスパラメーター" }

## エラー {#errors}

以下の表は、このエンドポイントで発生する一般的なエラーとその解決方法の一覧です。

| ステータス | 原因 | ガイダンス |
|---|---|---|
| `404` | タイプが見つかりません（`custom-object-type-not-found`）またはオブジェクトが見つかりません（`custom-object-not-found`） | `type_name` と `external_id` の両方がワークスペースに存在することを確認してください。 |
| `401` | REST APIキーがないか無効です | `Authorization` ヘッダーが `Bearer YOUR_REST_API_KEY` を使用しており、キーが有効であることを確認してください。 |
| `403` | APIキーに権限がないか、許可リストによってリクエストがブロックされています | キーに `custom_objects.read` 権限があること、および設定されている場合はソースIPがキーの許可リストに含まれていることを確認してください。 |
| `429` | レート制限を超えました | `X-RateLimit-Reset` 後に再試行し、リクエスト頻度を減らしてください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="カスタムオブジェクト取得のエラー" }
{% endapi %}