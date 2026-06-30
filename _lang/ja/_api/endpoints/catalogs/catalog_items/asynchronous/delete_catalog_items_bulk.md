---
nav_title: "DELETE: 複数のカタログ項目を削除する"
article_title: "DELETE: 複数のカタログ項目を削除する"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "この記事では、複数のカタログ項目を削除するBrazeエンドポイントの詳細について説明します。"

---
{% api %}
# 複数のカタログ項目を削除する {#delete-multiple-catalog-items}
{% apimethod delete %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> このエンドポイントを使用して、カタログ内の複数の項目を削除します。

各リクエストは最大50個の項目をサポートできます。このエンドポイントは非同期です。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#647c82e8-8b38-4df2-bde2-b1d8e19fd332 {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`catalogs.delete_items` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog item' %}

## パスパラメーター {#path-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `catalog_name` | 必須 | 文字列 | カタログ名。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="パスパラメーター" }

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `items` | 必須 | 配列 | 項目オブジェクトを含む配列。項目オブジェクトには、Brazeが削除すべき項目を参照する `id` が含まれている必要があります。リクエストごとに最大50個の項目オブジェクトが許可されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="リクエストパラメーター" }

## リクエスト例 {#example-request}

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {"id": "restaurant1"},
    {"id": "restaurant2"},
    {"id": "restaurant3"}
  ]
}'
```

## 応答 {#response}

このエンドポイントには、`202`、`400`、`404` の3つのステータスコード応答があります。

### 成功応答の例 {#example-success-response}

ステータスコード `202` は、次の応答本文を返す可能性があります。

```json
{
  "message": "success"
}
```

### エラー応答の例 {#example-error-response}

ステータスコード `400` は、次の応答本文を返す可能性があります。発生する可能性のあるエラーの詳細については、[トラブルシューティング](#troubleshooting)を参照してください。

```json
{
  "errors": [
    {
      "id": "items-missing-ids",
      "message": "There are 1 item(s) that do not have ids",
      "parameters": [],
      "parameter_values": []
    }
  ],
  "message": "Invalid Request"
}
```

## トラブルシューティング {#troubleshooting}

次のテーブルに、返される可能性のあるエラーと、関連するトラブルシューティングステップを示します。

| エラー | トラブルシューティング |
| --- | --- |
| `catalog-not-found` | カタログ名が有効であることを確認してください。 |
| `ids-too-large` | 項目IDは250文字以内にする必要があります。 |
| `ids-not-unique` | リクエスト内の項目IDが一意であることを確認してください。 |
| `ids-not-strings` | 項目IDは文字列型でなければなりません。 |
| `items-missing-ids` | 項目IDを持たない項目があります。各項目に項目IDがあることを確認してください。 |
| `invalid-ids` | 項目IDには、英字、数字、ハイフン、アンダースコアのみを使用できます。 |
| `request-includes-too-many-items` | リクエストに含まれる項目が多すぎます。リクエストごとの項目の上限は50個です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="トラブルシューティング" }

{% endapi %}