---
nav_title: "GET: 複数のカタログ項目の詳細をリストする"
article_title: "GET: 複数のカタログ項目の詳細をリストする"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "この記事では、「複数のカタログ項目の詳細をリストする」Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# 複数のカタログ項目の詳細をリストする {#list-multiple-catalog-item-details}
{% apimethod get %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> このエンドポイントを使用して、複数のカタログ項目とその内容を返します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#63a19dd5-10e0-4649-bdf0-097216748bbb {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`catalogs.get_items` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## パスパラメーター {#path-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `catalog_name` | 必須 | 文字列 | カタログ名。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="パスパラメーター" }

## クエリパラメーター {#query-parameters}

このエンドポイントへの各呼び出しでは、50件の項目が返されます。50件を超える項目があるカタログの場合は、以下の応答例に示すように、`Link` ヘッダーを使用して次のページのデータを取得します。

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `cursor` | オプション | 文字列 | カタログ項目のページネーションを決定します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="クエリパラメーター" }

## リクエストパラメーター {#request-parameters}

このエンドポイントにはリクエストボディがありません。

## リクエスト例 {#example-requests}

### カーソルなし {#without-cursor}

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### カーソル付き {#with-cursor}

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答 {#response}

このエンドポイントには、`200`、`400`、`404` の3つのステータスコード応答があります。

### 成功応答の例 {#example-success-response}

ステータスコード `200` は、次の応答ヘッダーと本文を返す可能性があります。

{% alert note %}
カタログの項目数が50以下の場合、`Link` ヘッダーは存在しません。カーソルのない呼び出しでは、`prev` は表示されません。項目の最後のページを表示している場合、`next` は表示されません。
{% endalert %}

```
Link: </catalogs/all_restaurants/items?cursor=c2tpcDow>; rel="prev",</catalogs/all_restaurants/items?cursor=c2tpcDoxMDA=>; rel="next"
```

```json
{
  "items": [
    {
      "id": "restaurant1",
      "Name": "Restaurant1",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": true,
      "Open_Time": "2022-11-02T09:03:19.967Z"
    },
    {
      "id": "restaurant2",
      "Name": "Restaurant2",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 10,
      "Loyalty_Program": true,
      "Open_Time": "2022-11-02T09:03:19.967Z"
    },
    {
      "id": "restaurant3",
      "Name": "Restaurant3",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": false,
      "Open_Time": "2022-11-02T09:03:19.967Z"
    }
  ],
  "message": "success"
}
```

### エラー応答例 {#example-error-response}

ステータスコード `400` は、次の応答本文を返す可能性があります。発生する可能性のあるエラーの詳細については、「[トラブルシューティング](#troubleshooting)」を参照してください。

```json
{
  "errors": [
    {
      "id": "invalid-cursor",
      "message": "'cursor' is not valid",
      "parameters": [
        "cursor"
      ],
      "parameter_values": [
        "bad-cursor"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## トラブルシューティング {#troubleshooting}

次の表に、返される可能性のあるエラーと、関連するトラブルシューティングステップを示します。

| エラー | トラブルシューティング |
| --- | --- |
| `catalog-not-found` | カタログ名が有効であることを確認してください。 |
| `invalid-cursor` | `cursor` が有効であることを確認してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="トラブルシューティング" }

{% endapi %}