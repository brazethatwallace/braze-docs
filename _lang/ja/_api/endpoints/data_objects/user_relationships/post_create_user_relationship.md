---
nav_title: "POST: ユーザーリレーションシップの作成"
article_title: "POST: ユーザーリレーションシップの作成"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "この記事では、ユーザーリレーションシップの作成エンドポイントについて説明します。"
---
{% api %}
# ユーザーリレーションシップの作成 {#create-user-relationship}
{% apimethod post %}
/data_objects/objects/{type_name}/{external_id}/users
{% endapimethod %}

> このエンドポイントを使用して、1人のBrazeユーザーを1つのデータオブジェクトにリンクします。

{% alert important %}
データオブジェクトは現在早期アクセス中です。データオブジェクトのAPIキー権限が**設定** > **APIキー**に表示されるには、ワークスペースが有効化されている必要があります。
{% endalert %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`data_objects.user_relationships.create` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

このエンドポイントはデータオブジェクト書き込みバケットに含まれ、デフォルトの制限は1分あたり50リクエストです。

## パスパラメーター {#path-parameters}

以下の表は、`/data_objects/objects/{type_name}/{external_id}/users` エンドポイントのパスパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `type_name` | 必須 | 文字列 | オブジェクトタイプ |
| `external_id` | 必須 | 文字列 | オブジェクト識別子 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="ユーザーリレーションシップ作成のパスパラメーター" }

## リクエストパラメーター {#request-parameters}

以下の表は、`/data_objects/objects/{type_name}/{external_id}/users` エンドポイントのJSONリクエストボディパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `braze_id` | 必須 | 文字列 | BrazeユーザーID |
| `rel_kind` | 必須 | 文字列 | リレーションシップの種類 |
| `attributes` | 任意 | オブジェクト | リレーションシップ属性 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="ユーザーリレーションシップ作成のリクエストパラメーター" }

## リクエスト例 {#example-request}

このセクションには、サンプルJSONペイロードとサンプルcURLリクエストが含まれています。

### サンプルリクエストペイロード {#sample-request-payload}

```json
{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user",
  "attributes": {
    "role": "owner"
  }
}
```

### サンプルcURLリクエスト {#sample-curl-request}

この例では、ユーザーを `acct-123` に `account_user` としてリンクし、`role` を `owner` として記録します。

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/users' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user",
  "attributes": {
    "role": "owner"
  }
}'
```

## レスポンス {#response}

このセクションには、成功レスポンスのサンプルとレスポンスフィールドが含まれています。

### 成功レスポンスの例 {#example-success-response}

ステータスコード `201` は、以下のレスポンスボディを返す場合があります。

```json
{
  "user_relationship": {
    "type_name": "account",
    "external_id": "acct-123",
    "rel_kind": "account_user",
    "user": { "braze_id": "507f1f77bcf86cd799439011" },
    "attributes": { "role": "owner" }
  }
}
```

### レスポンスパラメーター {#response-parameters}

以下の表は、成功レスポンスに含まれるフィールドの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `user_relationship` | 必須 | オブジェクト | 作成されたユーザーリレーションシップレコード |
| `user_relationship.type_name` | 必須 | 文字列 | データオブジェクトタイプのマシン名 |
| `user_relationship.external_id` | 必須 | 文字列 | データオブジェクト識別子 |
| `user_relationship.rel_kind` | 必須 | 文字列 | リレーションシップの種類の値 |
| `user_relationship.user` | 必須 | オブジェクト | リンクされたユーザーオブジェクト |
| `user_relationship.user.braze_id` | 必須 | 文字列 | Brazeユーザー識別子 |
| `user_relationship.attributes` | 必須 | オブジェクト | リレーションシップ属性 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="ユーザーリレーションシップ作成のレスポンスパラメーター" }

## エラー {#errors}

以下の表は、このエンドポイントの一般的なエラーとその解決方法の一覧です。

| ステータス | 原因 | ガイダンス |
|---|---|---|
| `400` | タイプに対する不明な `rel_kind` またはスキーマバリデーションエラー | `rel_kind` がオブジェクトタイプに対して有効であること、および `attributes` がリレーションシップスキーマに一致していることを確認してください。 |
| `404` | タイプまたはオブジェクトが見つからない | `type_name` と `external_id` の両方がワークスペースに存在することを確認してください。 |
| `409` | リレーションシップの重複（`duplicate-user-relationship`） | `PUT` を使用して既存のリレーションシップを置き換えるか、再作成する前に削除してください。 |
| `422` | ユーザーあたりのオブジェクト数制限に到達（`data-objects-per-user-limit-exceeded`）またはオブジェクトあたりのユーザー数制限に到達（`users-per-data-object-limit-exceeded`） | ユーザーまたはオブジェクトのリレーションシップ数を減らすか、ワークスペースの制限についてBrazeサポートに問い合わせてください。 |
| `401` | REST APIキーが見つからないか無効 | `Authorization` ヘッダーが `Bearer YOUR_REST_API_KEY` を使用していること、およびキーが有効であることを確認してください。 |
| `403` | APIキーに権限がないか、リクエストが許可リストによってブロックされている | キーに `data_objects.user_relationships.create` 権限があること、また設定されている場合はソースIPがキーの許可リストに含まれていることを確認してください。 |
| `429` | レート制限を超過 | `X-RateLimit-Reset` の後にリトライし、リクエスト頻度を減らしてください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ユーザーリレーションシップ作成のエラー" }
{% endapi %}