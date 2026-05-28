---
nav_title: "POST:複数のカタログアイテムを作成"
article_title: "POST:複数のカタログアイテムを作成"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "この記事では、複数のカタログアイテムを作成するBrazeエンドポイントの詳細について説明します。"

---
{% api %}
# 複数のカタログアイテムを作成する {#create-multiple-catalog-items}
{% apimethod post %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> このエンドポイントを使用して、カタログに複数のアイテムを作成します。

各リクエストは最大50個のアイテムに対応できます。このエンドポイントは非同期です。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cea18bb3-b83a-4160-81fe-8cd42aa6e7cc {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`catalogs.add_items` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog item' %}

## パスパラメーター {#path-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `catalog_name` | 必須 | 文字列 | カタログ名。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Path parameters" }

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `items` | 必須 | 配列 | アイテムオブジェクトを含む配列。アイテムオブジェクトには、カタログのすべてのフィールドが含まれている必要があります。リクエストごとに最大50個のアイテムオブジェクトが許可されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Request parameters" }

## リクエスト例 {#example-request}

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "id": "restaurant1",
      "Name": "Restaurant1",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": true,
      "Location": [-73.988103, 40.779109],
      "Preferences": {
        "favorite_brand": "Nike",
        "shirt_size": "L"
      },
      "Top_Dishes": [
        "Hamburger",
        "Deluxe Cheeseburger"
      ],
      "Created_At": "2022-11-01T09:03:19.967+00:00"
    },
    {
      "id": "restaurant2",
      "Name": "Restaurant2",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 10,
      "Loyalty_Program": true,
      "Location": [-73.988103, 40.779109],
      "Preferences": {
        "favorite_brand": "Nike",
        "shirt_size": "L"
      },
      "Top_Dishes": [
        "Hot Dog",
        "French Fries"
      ],
      "Created_At": "2022-11-02T09:03:19.967+00:00"
    },
    {
      "id": "restaurant3",
      "Name": "Restaurant3",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 3,
      "Loyalty_Program": false,
      "Location": [-73.988103, 40.779109],
      "Preferences": {
        "favorite_brand": "Nike",
        "shirt_size": "L"
      },
      "Top_Dishes": [
        "Buffalo Wings",
        "Philly Cheesesteak"
      ],
      "Created_At": "2022-11-03T09:03:19.967+00:00"
    }
  ]
}'
```

{% alert note %}
`Location` フィールドは `geo` データタイプを使用しており、`[経度, 緯度]` の形式の配列を期待します。
{% endalert %}

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
      "id": "invalid-fields",
      "message": "Some of the fields given do not exist in the catalog",
      "parameters": [
        "id"
      ],
      "parameter_values": [
        "restaurant1"
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
| `ids-not-strings` | アイテムIDは文字列型でなければなりません。 |
| `ids-not-unique` | アイテムIDはリクエスト内で一意でなければなりません。 |
| `ids-too-large` | アイテムIDは250文字以内にする必要があります。 |
| `invalid-ids` | アイテムIDには、英字、数字、ハイフン、アンダースコアのみを使用できます。 |
| `invalid-fields` | APIリクエストで送信するすべてのフィールドが、すでにカタログに存在していることを確認してください。これは、エラーに記載されているIDフィールドとは関係ありません。 |
| `invalid-keys-in-value-object` | アイテムオブジェクトのキーに `.` または `$` を含めることはできません。 |
| `item-array-invalid` | `items` はオブジェクトの配列でなければなりません。 |
| `items-missing-ids` | アイテムIDがないアイテムがあります。各アイテムにアイテムIDがあることを確認してください。 |
| `items-too-large` | アイテムの値は5,000文字を超えることはできません。 |
| `request-includes-too-many-items` | リクエストに含まれるアイテムが多すぎます。リクエストごとのアイテムの上限は50個です。 |
| `too-deep-nesting-in-value-object` | アイテムオブジェクトのネストは50レベルを超えることはできません。 |
| `unable-to-coerce-value` | アイテムタイプは変換できません。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting" }

{% endapi %}