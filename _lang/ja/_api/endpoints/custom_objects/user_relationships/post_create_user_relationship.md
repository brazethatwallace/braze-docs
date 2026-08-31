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
/custom_objects/objects/{type_name}/{external_id}/users
{% endapimethod %}

> このエンドポイントを使用して、1人のBrazeユーザーを1つのカスタムオブジェクトにリンクします。

{% alert important %}
カスタムオブジェクトは現在早期アクセス中です。カスタムオブジェクトのAPIキー権限が**設定** > **APIキー**に表示されるには、ワークスペースが有効化されている必要があります。
{% endalert %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`custom_objects.user_relationships.create` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

このエンドポイントはカスタムオブジェクト書き込みバケットに含まれ、デフォルトの制限は1分あたり50リクエストです。

## パスパラメーター {#path-parameters}

以下の表は、`/custom_objects/objects/{type_name}/{external_id}/users` エンドポイントのパスパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `type_name` | 必須 | 文字列 | オブジェクトタイプ |
| `external_id` | 必須 | 文字列 | オブジェクト識別子 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="ユーザーリレーションシップ作成のパスパラメーター" }

## リクエストパラメーター {#request-parameters}

以下の表は、`/custom_objects/objects/{type_name}/{external_id}/users` エンドポイントのJSONリクエストボディパラメーターの一覧と説明です。

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
curl --location --request POST 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123/users' \
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

このセクションには、成功レスポンスの例とレスポンスフィールドが含まれています。

### 成功レスポンス例 {#example-success-response}

ステータスコード `201` は以下のレスポンスボディを返す可能性があります。

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

以下の表は、成功レスポンスのフィールドの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `user_relationship` | 必須 | オブジェクト | 作成されたユーザーリレーションシップレコード |
| `user_relationship.type_name` | 必須 | 文字列 | カスタムオブジェクトタイプのマシン名 |
| `user_relationship.external_id` | 必須 | 文字列 | カスタムオブジェクト識別子 |
| `user_relationship.rel_kind` | 必須 | 文字列 | リレーションシップの種類の値 |
| `user_relationship.user` | 必須 | オブジェクト | リンクされたユーザーオブジェクト |
| `user_relationship.user.braze_id` | 必須 | 文字列 | Brazeユーザー識別子 |
| `user_relationship.attributes` | 必須 | オブジェクト | リレーションシップ属性 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="ユーザーリレーションシップ作成のレスポンスパラメーター" }

## エラー {#errors}

以下の表は、このエンドポイントの一般的なエラーとその解決方法の一覧です。

| ステータス | 原因 | ガイダンス |
|---|---|---|
| `400` | そのタイプに対する不明な `rel_kind` またはスキーマバリデーションエラー | `rel_kind` がオブジェクトタイプに対して有効であること、および `attributes` がリレーションシップスキーマに一致していることを確認してください。 |
| `404` | タイプまたはオブジェクトが見つかりません | `type_name` と `external_id` の両方がワークスペースに存在することを確認してください。 |
| `409` | リレーションシップの重複（`duplicate-user-relationship`） | 既存のリレーションシップを置き換えるには `PUT` を使用するか、再作成する前に削除してください。 |
| `422` | ユーザーあたりのオブジェクト数制限に到達（`custom-objects-per-user-limit-exceeded`）またはオブジェクトあたりのユーザー数制限に到達（`users-per-custom-object-limit-exceeded`） | ユーザーまたはオブジェクトのリレーションシップ数を削減するか、ワークスペースの制限についてBrazeサポートにお問い合わせください。 |
| `401` | REST APIキーが不足または無効 | `Authorization` ヘッダーが `Bearer YOUR_REST_API_KEY` を使用していること、およびキーがアクティブであることを確認してください。 |
| `403` | APIキーに権限がないか、リクエストが許可リストによってブロックされています | キーが `custom_objects.user_relationships.create` 権限を持っていること、および設定されている場合はソースIPがキーの許可リストに含まれていることを確認してください。 |
| `429` | レート制限超過 | `X-RateLimit-Reset` の後にリトライし、リクエスト頻度を下げてください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ユーザーリレーションシップ作成のエラー" }
{% endapi %}