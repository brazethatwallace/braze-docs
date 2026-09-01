---
nav_title: "PATCH: オブジェクトリレーションシップの更新"
article_title: "PATCH: オブジェクトリレーションシップの更新"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、オブジェクトリレーションシップの更新エンドポイントについて説明します。"
---
{% api %}
# オブジェクトリレーションシップの更新 {#update-object-relationship}
{% apimethod patch %}
/custom_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> このエンドポイントを使用して、既存のオブジェクトリレーションシップに属性をマージします。

{% alert important %}
カスタムオブジェクトは現在、早期アクセス段階です。カスタムオブジェクトのAPIキー権限が**設定** > **APIキー**に表示されるには、ワークスペースが有効化されている必要があります。
{% endalert %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`custom_objects.object_relationships.update` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

このエンドポイントはカスタムオブジェクト書き込みバケットに含まれ、デフォルトの制限は1分あたり50リクエストです。

## パスパラメーター {#path-parameters}

以下の表は、`/custom_objects/objects/{type_name}/{external_id}/object_relationships` エンドポイントのパスパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `type_name` | 必須 | String | URLオブジェクトタイプ |
| `external_id` | 必須 | String | URLオブジェクト識別子 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="オブジェクトリレーションシップ更新のパスパラメーター" }

## リクエストパラメーター {#request-parameters}

以下の表は、`/custom_objects/objects/{type_name}/{external_id}/object_relationships` エンドポイントのJSONリクエストボディパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `rel_kind` | 必須 | String | リレーションシップの種類 |
| `related_type_name` | 必須 | String | 関連オブジェクトタイプ |
| `related_external_id` | 必須 | String | 関連オブジェクト識別子 |
| `anchor` | オプション | String | `source`（デフォルト）または `target` |
| `attributes` | オプション | Object | マージするリレーションシップ属性 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="オブジェクトリレーションシップ更新のリクエストパラメーター" }

## リクエスト例 {#example-request}

このセクションには、サンプルJSONペイロードとサンプルcURLリクエストが含まれています。

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

この例では、`acct-123` と `acct-456` の間の既存の `subaccount` リレーションシップに属性をマージします。省略した属性は変更されません。

```bash
curl --location --request PATCH 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123/object_relationships' \
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

### 成功レスポンスの例 {#example-success-response}

ステータスコード `200` は、以下のレスポンスボディを返す可能性があります。

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

以下の表は、成功レスポンスに含まれるフィールドの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `object_relationship` | 必須 | Object | 更新されたリレーションシップレコード |
| `object_relationship.rel_kind` | 必須 | String | リレーションシップの種類の値 |
| `object_relationship.to_custom_object` | 条件付き | Object | `anchor=source` の場合の関連オブジェクト |
| `object_relationship.from_custom_object` | 条件付き | Object | `anchor=target` の場合の関連オブジェクト |
| `object_relationship.attributes` | 必須 | Object | マージ後のリレーションシップ属性 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="オブジェクトリレーションシップ更新のレスポンスパラメーター" }

## エラー {#errors}

以下の表は、このエンドポイントの一般的なエラーとその解決方法の一覧です。

| ステータス | 原因 | ガイダンス |
|---|---|---|
| `400` | バリデーションエラー | `rel_kind`、`anchor`、`attributes` がリレーションシップタイプに対して有効であることを確認してください。 |
| `404` | リレーションシップが見つかりません（`custom-object-relationship-not-found`） | ソースオブジェクト、関連オブジェクト、リレーションシップキーの値がすべて存在することを確認してください。 |
| `401` | REST APIキーが欠落しているか無効です | `Authorization` ヘッダーが `Bearer YOUR_REST_API_KEY` を使用しており、キーが有効であることを確認してください。 |
| `403` | APIキーに権限がないか、リクエストが許可リストによってブロックされています | キーに `custom_objects.object_relationships.update` 権限があること、および設定されている場合はソースIPがキーの許可リストに含まれていることを確認してください。 |
| `429` | レート制限を超過しました | `X-RateLimit-Reset` 後にリトライし、リクエスト頻度を下げてください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="オブジェクトリレーションシップ更新のエラー" }
{% endapi %}