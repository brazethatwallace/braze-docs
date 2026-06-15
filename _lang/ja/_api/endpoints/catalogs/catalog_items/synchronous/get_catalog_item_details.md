---
nav_title: "GET: カタログ項目の詳細をリストアップする"
article_title: "GET: カタログ項目の詳細をリストアップする"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "この記事では、「カタログ項目の詳細をリストアップする」Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# カタログ項目の詳細をリストアップする {#list-catalog-item-details}
{% apimethod get %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> このエンドポイントを使用して、カタログ項目とそのコンテンツを返します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#52c6631c-7366-48e5-9e0e-16de7b6285cc {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`catalogs.get_item` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## パスパラメーター {#path-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `catalog_name` | 必須 | 文字列 | カタログの名前。 |
| `item_id` | 必須 | 文字列 | カタログ項目のID。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Path parameters" }

## リクエストパラメーター {#request-parameters}

このエンドポイントにはリクエストボディはありません。

## リクエスト例 {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答 {#response}

このエンドポイントには `200` と `404` の2つのステータスコード応答があります。

### 成功応答の例 {#example-success-response}

ステータスコード `200` は、次の応答本文を返す可能性があります。

```json
{
  "items": [
    {
      "id": "restaurant3",
      "Name": "Restaurant1",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": true,
      "Open_Time": "2022-11-01T09:03:19.967Z"
    }
  ],
  "message": "success"
}
```

### エラー応答の例 {#example-error-response}

ステータスコード `404` は、次の応答を返す可能性があります。発生する可能性のあるエラーの詳細については、[トラブルシューティング](#troubleshooting)を参照してください。

```json
{
  "errors": [
    {
      "id": "item-not-found",
      "message": "Could not find item",
      "parameters": [
        "item_id"
      ],
      "parameter_values": [
        "restaurant34"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## トラブルシューティング {#troubleshooting}

以下の表は、返される可能性のあるエラーと、該当する場合の関連するトラブルシューティング手順を示しています。

| エラー | トラブルシューティング |
| --- | --- |
| `catalog-not-found` | カタログ名が有効であることを確認してください。 |
| `item-not-found` | その項目がカタログに存在することを確認してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting" }

{% endapi %}