---
nav_title: "DELETE: カスタムオブジェクトの削除"
article_title: "DELETE: カスタムオブジェクトの削除"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "この記事では、カスタムオブジェクトの削除エンドポイントについて説明します。"
---
{% api %}
# カスタムオブジェクトの削除 {#delete-custom-object}
{% apimethod delete %}
/custom_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> このエンドポイントを使用して、1つのカスタムオブジェクトを削除します。

{% alert important %}
カスタムオブジェクトは現在早期アクセス中です。カスタムオブジェクトのAPIキー権限が**設定** > **APIキー**に表示されるようにするには、ワークスペースを有効にする必要があります。
{% endalert %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`custom_objects.delete` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

このエンドポイントはカスタムオブジェクト書き込みバケットに含まれ、デフォルトの制限は1分あたり50リクエストです。

## パスパラメーター {#path-parameters}

次の表は、`/custom_objects/objects/{type_name}/{external_id}` エンドポイントのパスパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `type_name` | 必須 | String | カスタムオブジェクトタイプのマシン名 |
| `external_id` | 必須 | String | オブジェクト識別子 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="カスタムオブジェクト削除のパスパラメーター" }

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

この例では、`acct-123` のアカウントレコードを削除します。

```bash
curl --location --request DELETE 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## レスポンス {#response}

このセクションには、成功レスポンスのサンプルとレスポンスフィールドが含まれています。

### 成功レスポンスの例 {#example-success-response}

ステータスコード `200` は、以下のレスポンスボディを返す可能性があります。

```json
{ "deleted": true }
```

削除は同期的に行われます。1つのオブジェクトを削除しても、関連するオブジェクトは削除されません。

### レスポンスパラメーター {#response-parameters}

次の表は、成功レスポンスに含まれるフィールドの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `deleted` | 必須 | Boolean | オブジェクトの削除が成功したかどうか |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="カスタムオブジェクト削除のレスポンスパラメーター" }

## エラー {#errors}

次の表は、このエンドポイントで発生する一般的なエラーとその解決方法の一覧です。

| ステータス | 原因 | ガイダンス |
|---|---|---|
| `404` | タイプが見つからない、またはオブジェクトが見つからない | `type_name` と `external_id` の両方がワークスペースに存在することを確認してください。 |
| `401` | REST APIキーが見つからない、または無効 | `Authorization` ヘッダーが `Bearer YOUR_REST_API_KEY` を使用していること、およびキーが有効であることを確認してください。 |
| `403` | APIキーに権限がない、またはリクエストが許可リストによってブロックされている | キーに `custom_objects.delete` 権限があること、および設定されている場合はソースIPがキーの許可リストに含まれていることを確認してください。 |
| `429` | レート制限の超過 | `X-RateLimit-Reset` の後にリトライし、リクエスト頻度を減らしてください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="カスタムオブジェクト削除のエラー" }
{% endapi %}