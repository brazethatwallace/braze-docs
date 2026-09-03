---
nav_title: "DELETE: オブジェクトリレーションシップの削除"
article_title: "DELETE: オブジェクトリレーションシップの削除"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "この記事では、オブジェクトリレーションシップの削除エンドポイントについて詳しく説明します。"
---
{% api %}
# オブジェクトリレーションシップの削除 {#delete-object-relationship}
{% apimethod delete %}
/data_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> このエンドポイントを使用して、オブジェクト間のリレーションシップエッジを1つ削除します。

{% alert important %}
データオブジェクトは現在早期アクセス段階です。データオブジェクトのAPIキー権限が**設定** > **APIキー**に表示されるには、ワークスペースが有効化されている必要があります。
{% endalert %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`data_objects.object_relationships.delete` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

このエンドポイントはデータオブジェクト書き込みバケットに属しており、デフォルトの制限は1分あたり50リクエストです。

## パスパラメーター {#path-parameters}

以下の表は、`/data_objects/objects/{type_name}/{external_id}/object_relationships` エンドポイントのパスパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `type_name` | 必須 | String | URLオブジェクトタイプ |
| `external_id` | 必須 | String | URLオブジェクト識別子 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="オブジェクトリレーションシップ削除のパスパラメーター" }

## リクエストパラメーター {#request-parameters}

以下の表は、`/data_objects/objects/{type_name}/{external_id}/object_relationships` エンドポイントのJSONリクエストボディパラメーターの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `rel_kind` | 必須 | String | リレーションシップの種類 |
| `related_type_name` | 必須 | String | 関連オブジェクトタイプ |
| `related_external_id` | 必須 | String | 関連オブジェクト識別子 |
| `anchor` | オプション | String | `source`（デフォルト）または `target` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="オブジェクトリレーションシップ削除のリクエストパラメーター" }

{% alert note %}
この `DELETE` エンドポイントはJSONリクエストボディを必要とします。お使いのHTTPクライアントが `DELETE` 呼び出しでリクエストボディを送信することを確認してください。
{% endalert %}

## リクエスト例 {#example-request}

このセクションには、サンプルJSONペイロードとサンプルcURLリクエストが含まれています。

### サンプルリクエストペイロード {#sample-request-payload}

```json
{
  "rel_kind": "subaccount",
  "related_type_name": "account",
  "related_external_id": "acct-456",
  "anchor": "source"
}
```

### サンプルcURLリクエスト {#sample-curl-request}

この例では、`acct-123` と `acct-456` 間の `subaccount` リレーションシップを削除します。両方のアカウントレコードはそのまま残ります。

```bash
curl --location --request DELETE 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/object_relationships' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "rel_kind": "subaccount",
  "related_type_name": "account",
  "related_external_id": "acct-456",
  "anchor": "source"
}'
```

## レスポンス {#response}

このセクションには、成功時のレスポンス例とレスポンスフィールドが含まれています。

### 成功レスポンス例 {#example-success-response}

ステータスコード `200` は以下のレスポンスボディを返す可能性があります。

```json
{ "deleted": true }
```

### レスポンスパラメーター {#response-parameters}

以下の表は、成功レスポンスに含まれるフィールドの一覧と説明です。

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `deleted` | 必須 | Boolean | リレーションシップの削除が成功したかどうか |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="オブジェクトリレーションシップ削除のレスポンスパラメーター" }

## エラー {#errors}

以下の表は、このエンドポイントの一般的なエラーとその解決方法の一覧です。

| ステータス | 原因 | ガイダンス |
|---|---|---|
| `400` | バリデーションエラー | リクエストボディに有効な `rel_kind`、`related_type_name`、`related_external_id`、`anchor` の値が含まれていることを確認してください。 |
| `404` | リレーションシップまたはエンドポイントオブジェクトが見つかりません | 両方のオブジェクトが存在し、リレーションシップのキー値が既存のエッジと一致することを確認してください。 |
| `401` | REST APIキーが不足しているか無効です | `Authorization` ヘッダーが `Bearer YOUR_REST_API_KEY` を使用しており、キーが有効であることを確認してください。 |
| `403` | APIキーに権限がないか、許可リストによりリクエストがブロックされています | キーに `data_objects.object_relationships.delete` 権限があること、および設定されている場合はソースIPがキーの許可リストに含まれていることを確認してください。 |
| `429` | レート制限を超過しました | `X-RateLimit-Reset` の後にリトライし、リクエスト頻度を減らしてください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="オブジェクトリレーションシップ削除のエラー" }
{% endapi %}