---
nav_title: "PUT: ユーザーリレーションシップの置換"
article_title: "PUT: ユーザーリレーションシップの置換"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "この記事では、ユーザーリレーションシップの置換エンドポイントについて詳しく説明します。"
---
{% api %}
# ユーザーリレーションシップの置換 {#replace-user-relationship}
{% apimethod put %}
/custom_objects/objects/{type_name}/{external_id}/users
{% endapimethod %}

> このエンドポイントを使用して、1つのユーザーリレーションシップを作成または置換します。

{% alert important %}
カスタムオブジェクトは現在早期アクセス中です。カスタムオブジェクトのAPIキー権限が**設定** > **APIキー**に表示されるには、ワークスペースが有効化されている必要があります。
{% endalert %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`custom_objects.user_relationships.update` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

このエンドポイントはカスタムオブジェクトの書き込みバケットに含まれ、デフォルトの制限は1分あたり50リクエストです。

## パスパラメーター {#path-parameters}

以下の表は、`/custom_objects/objects/{type_name}/{external_id}/users` エンドポイントのパスパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `type_name` | 必須 | String | オブジェクトタイプ |
| `external_id` | 必須 | String | オブジェクト識別子 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="ユーザーリレーションシップの置換パスパラメーター" }

## リクエストパラメーター {#request-parameters}

以下の表は、`/custom_objects/objects/{type_name}/{external_id}/users` エンドポイントのJSONリクエストボディパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `braze_id` | 必須 | String | BrazeユーザーID |
| `rel_kind` | 必須 | String | リレーションシップの種類 |
| `attributes` | オプション | Object | リレーションシップ属性 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="ユーザーリレーションシップの置換リクエストパラメーター" }

## リクエスト例 {#example-request}

このセクションには、サンプルのJSONペイロードとサンプルのcURLリクエストが含まれています。

### サンプルリクエストペイロード {#sample-request-payload}

```json
{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user",
  "attributes": {
    "role": "admin"
  }
}
```

### サンプルcURLリクエスト {#sample-curl-request}

この例では、ユーザーと `acct-123` の間の `account_user` リレーションシップの属性を置換し、以前保存されていた属性をすべて上書きします。

```bash
curl --location --request PUT 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123/users' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user",
  "attributes": {
    "role": "admin"
  }
}'
```

## レスポンス {#response}

このセクションには、成功レスポンスの例とレスポンスフィールドが含まれています。

### 成功レスポンスの例 {#example-success-response}

ステータスコード `200` は以下のレスポンスボディを返す可能性があります。

```json
{
  "user_relationship": {
    "type_name": "account",
    "external_id": "acct-123",
    "rel_kind": "account_user",
    "user": { "braze_id": "507f1f77bcf86cd799439011" },
    "attributes": { "role": "admin" }
  }
}
```

### レスポンスパラメーター {#response-parameters}

以下の表は、成功レスポンスに含まれるフィールドの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `user_relationship` | 必須 | Object | 作成または置換されたユーザーリレーションシップレコード |
| `user_relationship.type_name` | 必須 | String | カスタムオブジェクトタイプのマシン名 |
| `user_relationship.external_id` | 必須 | String | カスタムオブジェクト識別子 |
| `user_relationship.rel_kind` | 必須 | String | リレーションシップの種類の値 |
| `user_relationship.user` | 必須 | Object | リンクされたユーザーオブジェクト |
| `user_relationship.user.braze_id` | 必須 | String | Brazeユーザー識別子 |
| `user_relationship.attributes` | 必須 | Object | リレーションシップ属性 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="ユーザーリレーションシップの置換レスポンスパラメーター" }

## エラー {#errors}

以下の表は、このエンドポイントで発生する一般的なエラーとその解決方法の一覧です。

| ステータス | 原因 | ガイダンス |
|---|---|---|
| `400` | バリデーションエラー | `rel_kind` がオブジェクトタイプに対して有効であること、および `attributes` がリレーションシップスキーマと一致していることを確認してください。 |
| `404` | リレーションシップまたはオブジェクトが見つかりません（`custom-object-relationship-not-found`） | オブジェクト、ユーザー、およびリレーションシップキーの値がすべて存在することを確認してください。 |
| `422` | ユーザーあたりのオブジェクト数の上限に達しました（`custom-objects-per-user-limit-exceeded`）、またはオブジェクトあたりのユーザー数の上限に達しました（`users-per-custom-object-limit-exceeded`） | ユーザーまたはオブジェクトのリレーションシップ数を減らすか、ワークスペースの上限についてBrazeサポートにお問い合わせください。 |
| `401` | REST APIキーが不足しているか無効です | `Authorization` ヘッダーで `Bearer YOUR_REST_API_KEY` を使用していること、およびキーがアクティブであることを確認してください。 |
| `403` | APIキーに権限がないか、許可リストによってリクエストがブロックされています | キーに `custom_objects.user_relationships.update` 権限があること、および設定されている場合はソースIPがキーの許可リストに含まれていることを確認してください。 |
| `429` | レート制限超過 | `X-RateLimit-Reset` 後に再試行し、リクエスト頻度を減らしてください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ユーザーリレーションシップの置換エラー" }
{% endapi %}