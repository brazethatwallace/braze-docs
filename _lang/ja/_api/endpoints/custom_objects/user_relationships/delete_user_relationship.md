---
nav_title: "DELETE: ユーザーリレーションシップの削除"
article_title: "DELETE: ユーザーリレーションシップの削除"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "この記事では、ユーザーリレーションシップの削除エンドポイントについて詳しく説明します。"
---
{% api %}
# ユーザーリレーションシップの削除 {#delete-user-relationship}
{% apimethod delete %}
/custom_objects/objects/{type_name}/{external_id}/users
{% endapimethod %}

> このエンドポイントを使用して、ユーザーとオブジェクト間のリレーションシップを1つ削除します。

{% alert important %}
カスタムオブジェクトは現在、早期アクセス段階です。カスタムオブジェクトのAPIキー権限が**設定** > **APIキー**に表示されるには、ワークスペースが有効化されている必要があります。
{% endalert %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`custom_objects.user_relationships.delete` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

このエンドポイントはカスタムオブジェクト書き込みバケットに属しており、デフォルトの制限は1分あたり50リクエストです。

## パスパラメーター {#path-parameters}

以下の表は、`/custom_objects/objects/{type_name}/{external_id}/users` エンドポイントのパスパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `type_name` | 必須 | 文字列 | オブジェクトタイプ |
| `external_id` | 必須 | 文字列 | オブジェクト識別子 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="ユーザーリレーションシップ削除のパスパラメーター" }

## リクエストパラメーター {#request-parameters}

以下の表は、`/custom_objects/objects/{type_name}/{external_id}/users` エンドポイントのJSONリクエストボディパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `braze_id` | 必須 | 文字列 | BrazeユーザーID |
| `rel_kind` | 必須 | 文字列 | リレーションシップの種類 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="ユーザーリレーションシップ削除のリクエストパラメーター" }

{% alert note %}
この `DELETE` エンドポイントはJSONリクエストボディを必要とします。HTTPクライアントが `DELETE` 呼び出し時にリクエストボディを送信することを確認してください。
{% endalert %}

## リクエスト例 {#example-request}

このセクションには、JSONペイロードのサンプルとcURLリクエストのサンプルが含まれています。

### リクエストペイロードのサンプル {#sample-request-payload}

```json
{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user"
}
```

### cURLリクエストのサンプル {#sample-curl-request}

この例では、指定されたユーザーと `acct-123` の間の `account_user` リレーションシップを削除します。ユーザープロファイルとアカウントレコードはどちらも残ります。

```bash
curl --location --request DELETE 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123/users' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user"
}'
```

## レスポンス {#response}

このセクションには、成功レスポンスのサンプルとレスポンスフィールドが含まれています。

### 成功レスポンスの例 {#example-success-response}

ステータスコード `200` では、以下のレスポンスボディが返される可能性があります。

```json
{ "deleted": true }
```

### レスポンスパラメーター {#response-parameters}

以下の表は、成功レスポンスのフィールドの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `deleted` | 必須 | ブール値 | リレーションシップの削除が成功したかどうか |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="ユーザーリレーションシップ削除のレスポンスパラメーター" }

## エラー {#errors}

以下の表は、このエンドポイントの一般的なエラーとその解決方法の一覧です。

| ステータス | 原因 | ガイダンス |
|---|---|---|
| `400` | バリデーションエラー | リクエストボディに有効な `braze_id` と `rel_kind` の値が含まれていることを確認してください。 |
| `404` | リレーションシップまたはオブジェクトが見つかりません | オブジェクト、ユーザー、およびリレーションシップキーの値がすべて存在することを確認してください。 |
| `401` | REST APIキーが不足しているか無効です | `Authorization` ヘッダーが `Bearer YOUR_REST_API_KEY` を使用しており、キーがアクティブであることを確認してください。 |
| `403` | APIキーに権限がないか、許可リストによってリクエストがブロックされています | キーに `custom_objects.user_relationships.delete` 権限があること、および設定されている場合はソースIPがキーの許可リストに含まれていることを確認してください。 |
| `429` | レート制限を超過しました | `X-RateLimit-Reset` の後にリトライし、リクエスト頻度を減らしてください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ユーザーリレーションシップ削除のエラー" }
{% endapi %}