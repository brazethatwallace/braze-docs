---
nav_title: "PUT: オブジェクトリレーションシップの置換"
article_title: "PUT: オブジェクトリレーションシップの置換"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "この記事では、オブジェクトリレーションシップの置換エンドポイントについて詳しく説明します。"
---
{% api %}
# オブジェクトリレーションシップの置換 {#replace-object-relationship}
{% apimethod put %}
/custom_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> このエンドポイントを使用して、オブジェクトリレーションシップを作成または置換します。

{% alert important %}
カスタムオブジェクトは現在早期アクセス段階です。カスタムオブジェクトのAPIキー権限が**設定** > **APIキー**に表示されるには、ワークスペースを有効にする必要があります。
{% endalert %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`custom_objects.object_relationships.update` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

このエンドポイントはカスタムオブジェクト書き込みバケットに含まれており、デフォルトの制限は1分あたり50リクエストです。

## パスパラメーター {#path-parameters}

次の表は、`/custom_objects/objects/{type_name}/{external_id}/object_relationships` エンドポイントのパスパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `type_name` | 必須 | String | URLオブジェクトタイプ |
| `external_id` | 必須 | String | URLオブジェクト識別子 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Replace object relationship path parameters" }

## リクエストパラメーター {#request-parameters}

次の表は、`/custom_objects/objects/{type_name}/{external_id}/object_relationships` エンドポイントのJSONリクエストボディパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `rel_kind` | 必須 | String | リレーションシップの種類 |
| `related_type_name` | 必須 | String | 関連オブジェクトタイプ |
| `related_external_id` | 必須 | String | 関連オブジェクト識別子 |
| `anchor` | オプション | String | `source`（デフォルト）または `target` |
| `attributes` | オプション | Object | リレーションシップ属性 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Replace object relationship request parameters" }

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

この例では、`acct-123` と `acct-456` の間の `subaccount` リレーションシップを置換し、以前保存されていた属性をすべて上書きします。

```bash
curl --location --request PUT 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123/object_relationships' \
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

このセクションには、成功レスポンスの例とレスポンスフィールドが含まれています。

### 成功レスポンスの例 {#example-success-response}

ステータスコード `200` は、次のレスポンスボディを返す可能性があります。

```json
{
  "object_relationship": {
    "rel_kind": "subaccount",
    "to_custom_object": {
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
| `object_relationship` | 必須 | Object | 作成または置換されたリレーションシップレコード |
| `object_relationship.rel_kind` | 必須 | String | リレーションシップの種類の値 |
| `object_relationship.to_custom_object` | 条件付き | Object | `anchor=source` の場合の関連オブジェクト |
| `object_relationship.from_custom_object` | 条件付き | Object | `anchor=target` の場合の関連オブジェクト |
| `object_relationship.attributes` | 必須 | Object | リレーションシップ属性 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Replace object relationship response parameters" }

## エラー {#errors}

次の表は、このエンドポイントで発生する一般的なエラーとその解決方法の一覧です。

| ステータス | 原因 | ガイダンス |
|---|---|---|
| `400` | バリデーションエラー | `rel_kind`、`anchor`、`attributes` がリレーションシップタイプに対して有効であることを確認してください。 |
| `404` | リレーションシップまたはエンドポイントオブジェクトが見つかりません（`custom-object-relationship-not-found`） | 両方のオブジェクトと関連タイプ名がワークスペースに存在することを確認してください。 |
| `422` | オブジェクトごとのリレーションシップ上限に達しました（`custom-object-relationship-limit-exceeded`） | オブジェクトのリレーションシップ数を減らすか、ワークスペースの制限についてBrazeサポートにお問い合わせください。 |
| `401` | REST APIキーが見つからないか無効です | `Authorization` ヘッダーで `Bearer YOUR_REST_API_KEY` を使用しており、キーが有効であることを確認してください。 |
| `403` | APIキーに権限がないか、リクエストが許可リストによってブロックされています | キーに `custom_objects.object_relationships.update` 権限があること、および設定されている場合はソースIPがキーの許可リストに含まれていることを確認してください。 |
| `429` | レート制限を超過しました | `X-RateLimit-Reset` 以降にリトライし、リクエスト頻度を減らしてください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Replace object relationship errors" }
{% endapi %}