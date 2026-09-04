---
nav_title: "POST: オブジェクトリレーションシップの作成"
article_title: "POST: オブジェクトリレーションシップの作成"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "この記事では、オブジェクトリレーションシップの作成エンドポイントについて説明します。"
---
{% api %}
# オブジェクトリレーションシップの作成 {#create-object-relationship}
{% apimethod post %}
/data_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> このエンドポイントを使用して、2つのデータオブジェクト間に一方向のリレーションシップエッジを作成します。

{% alert important %}
データオブジェクトは現在、早期アクセス段階です。データオブジェクトのAPIキー権限が**設定** > **APIキー**に表示されるには、ワークスペースが有効化されている必要があります。
{% endalert %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`data_objects.object_relationships.create` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

このエンドポイントはデータオブジェクト書き込みバケットに含まれ、デフォルトでは1分あたり50リクエストの制限があります。

## パスパラメーター {#path-parameters}

次の表は、`/data_objects/objects/{type_name}/{external_id}/object_relationships` エンドポイントのパスパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `type_name` | 必須 | String | URLオブジェクトタイプ |
| `external_id` | 必須 | String | URLオブジェクト識別子 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="オブジェクトリレーションシップ作成のパスパラメーター" }

## リクエストパラメーター {#request-parameters}

次の表は、`/data_objects/objects/{type_name}/{external_id}/object_relationships` エンドポイントのJSONリクエストボディパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `rel_kind` | 必須 | String | リレーションシップの種類 |
| `related_type_name` | 必須 | String | 関連オブジェクトタイプ |
| `related_external_id` | 必須 | String | 関連オブジェクト識別子 |
| `anchor` | 任意 | String | `source`（デフォルト）または `target` |
| `attributes` | 任意 | Object | リレーションシップ属性 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="オブジェクトリレーションシップ作成のリクエストパラメーター" }

## リクエスト例 {#example-request}

このセクションには、サンプルのJSONペイロードとサンプルのcURLリクエストが含まれています。

### サンプルリクエストペイロード {#sample-request-payload}

```json
{
  "rel_kind": "subaccount",
  "related_type_name": "account",
  "related_external_id": "acct-456",
  "anchor": "source",
  "attributes": {}
}
```

### サンプルcURLリクエスト {#sample-curl-request}

この例では、`acct-123`を`subaccount`として`acct-456`にリンクし、`acct-123`をリレーションシップのソースとして設定します。

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/object_relationships' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "rel_kind": "subaccount",
  "related_type_name": "account",
  "related_external_id": "acct-456",
  "anchor": "source",
  "attributes": {}
}'
```

## レスポンス {#response}

このセクションには、成功レスポンスのサンプルとレスポンスフィールドが含まれています。

### 成功レスポンス例 {#example-success-response}

ステータスコード `201` は、次のレスポンスボディを返す可能性があります。

```json
{
  "object_relationship": {
    "rel_kind": "subaccount",
    "to_data_object": {
      "type_name": "account",
      "external_id": "acct-456",
      "attributes": { "name": "Child Account" }
    },
    "attributes": {}
  }
}
```

### レスポンスパラメーター {#response-parameters}

次の表は、成功レスポンスに含まれるフィールドの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `object_relationship` | 必須 | Object | 作成されたリレーションシップレコード |
| `object_relationship.rel_kind` | 必須 | String | リレーションシップの種類の値 |
| `object_relationship.to_data_object` | 条件付き | Object | `anchor=source` の場合の関連オブジェクト |
| `object_relationship.from_data_object` | 条件付き | Object | `anchor=target` の場合の関連オブジェクト |
| `object_relationship.to_data_object.type_name` | 条件付き | String | 関連オブジェクトのタイプ名 |
| `object_relationship.to_data_object.external_id` | 条件付き | String | 関連オブジェクトのexternal ID |
| `object_relationship.to_data_object.attributes` | 条件付き | Object | 関連オブジェクトの属性 |
| `object_relationship.from_data_object.type_name` | 条件付き | String | 関連オブジェクトのタイプ名 |
| `object_relationship.from_data_object.external_id` | 条件付き | String | 関連オブジェクトのexternal ID |
| `object_relationship.from_data_object.attributes` | 条件付き | Object | 関連オブジェクトの属性 |
| `object_relationship.attributes` | 必須 | Object | リレーションシップ属性 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="オブジェクトリレーションシップ作成のレスポンスパラメーター" }

## エラー {#errors}

次の表は、このエンドポイントの一般的なエラーとその解決方法の一覧です。

| ステータス | 原因 | ガイダンス |
|---|---|---|
| `400` | 不明な `rel_kind`、無効な `anchor`、リレーションシップの種類に対する無効な関連タイプ、またはスキーマ違反 | `rel_kind` がタイプペアに対して有効であることを確認し、有効な `anchor` を使用し、`attributes` がリレーションシップスキーマに一致することを確認してください。 |
| `404` | URLオブジェクト、関連オブジェクト、URLタイプ、または関連タイプが見つかりません | 両方のオブジェクトと両方のタイプ名がワークスペースに存在することを確認してください。 |
| `409` | エッジの重複（`duplicate-object-relationship`） | `PUT` を使用して既存のリレーションシップを置き換えるか、再作成する前に削除してください。 |
| `422` | オブジェクトごとのリレーションシップ制限に到達（`data-object-relationship-limit-exceeded`） | オブジェクトのリレーションシップ数を減らすか、ワークスペースの制限についてBrazeサポートにお問い合わせください。 |
| `401` | REST APIキーが不足または無効 | `Authorization` ヘッダーが `Bearer YOUR_REST_API_KEY` を使用しており、キーがアクティブであることを確認してください。 |
| `403` | APIキーに権限がないか、許可リストによってリクエストがブロックされています | キーに `data_objects.object_relationships.create` 権限があること、および設定されている場合はソースIPがキーの許可リストに含まれていることを確認してください。 |
| `429` | レート制限超過 | `X-RateLimit-Reset` 後にリトライし、リクエスト頻度を減らしてください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="オブジェクトリレーションシップ作成のエラー" }
{% endapi %}