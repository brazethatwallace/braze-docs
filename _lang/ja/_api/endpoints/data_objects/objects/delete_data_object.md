---
nav_title: "DELETE: データオブジェクトの削除"
article_title: "DELETE: データオブジェクトの削除"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "この記事では、データオブジェクトの削除エンドポイントについて詳しく説明します。"
---
{% api %}
# データオブジェクトの削除 {#delete-data-object}
{% apimethod delete %}
/data_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> このエンドポイントを使用して、1つのデータオブジェクトを削除します。

{% alert important %}
データオブジェクトは現在、早期アクセス段階です。Data Objects APIキーのアクセス許可が**設定** > **APIキー**に表示されるようにするには、ワークスペースを有効にする必要があります。
{% endalert %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`data_objects.delete` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

このエンドポイントはデータオブジェクト書き込みバケットに含まれ、デフォルトの制限は1分あたり50リクエストです。

## パスパラメーター {#path-parameters}

以下の表は、`/data_objects/objects/{type_name}/{external_id}` エンドポイントのパスパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `type_name` | 必須 | String | データオブジェクトタイプのマシン名 |
| `external_id` | 必須 | String | オブジェクト識別子 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="データオブジェクト削除のパスパラメーター" }

## リクエスト例 {#example-request}

このセクションでは、パスパラメーターのサンプルペイロードとサンプルcURLリクエストを紹介します。

### サンプルリクエストペイロード {#sample-request-payload}

このリクエストのパスパラメーターのリファレンスとして、以下のJSONオブジェクトを使用してください。

```json
{
  "type_name": "account",
  "external_id": "acct-123"
}
```

### サンプルcURLリクエスト {#sample-curl-request}

この例では、`acct-123` のアカウントレコードを削除します。

```bash
curl --location --request DELETE 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## レスポンス {#response}

このセクションでは、成功レスポンスのサンプルとレスポンスフィールドを紹介します。

### 成功レスポンスの例 {#example-success-response}

ステータスコード `200` は、以下のレスポンスボディを返す可能性があります。

```json
{ "deleted": true }
```

削除は同期的に処理されます。1つのオブジェクトを削除しても、関連するオブジェクトは削除されません。

### レスポンスパラメーター {#response-parameters}

以下の表は、成功レスポンスに含まれるフィールドの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `deleted` | 必須 | Boolean | オブジェクトの削除が成功したかどうか |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="データオブジェクト削除のレスポンスパラメーター" }

## エラー {#errors}

以下の表は、このエンドポイントで発生する一般的なエラーとその解決方法の一覧です。

| ステータス | 原因 | ガイダンス |
|---|---|---|
| `404` | タイプが見つからない、またはオブジェクトが見つからない | `type_name` と `external_id` がワークスペースに存在することを確認してください。 |
| `401` | REST APIキーが見つからない、または無効 | `Authorization` ヘッダーに `Bearer YOUR_REST_API_KEY` が使用されていること、およびキーが有効であることを確認してください。 |
| `403` | APIキーに権限がない、またはリクエストが許可リストによってブロックされている | キーに `data_objects.delete` 権限があること、および設定されている場合はソースIPがキーの許可リストに含まれていることを確認してください。 |
| `429` | レート制限超過 | `X-RateLimit-Reset` 後にリトライし、リクエスト頻度を減らしてください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="データオブジェクト削除のエラー" }
{% endapi %}