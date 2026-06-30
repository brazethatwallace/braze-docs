---
nav_title: "POST:カタログアイテムを作成"
article_title: "POST:カタログアイテムを作成"
search_tag: Endpoint
page_order: 5

layout: api_page
page_type: reference
description: "この記事では、「カタログアイテムを作成」Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# カタログアイテムを作成する {#create-catalog-item}
{% apimethod post %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> このエンドポイントを使用して、カタログにアイテムを作成します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#820c305b-ea6a-4b71-811a-55003a212a40 {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`catalogs.create_item` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## パスパラメーター {#path-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `catalog_name` | 必須 | 文字列 | カタログの名前。 |
| `item_id` | 必須 | 文字列 | カタログアイテムのID。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Path parameters" }

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `items` | 必須 | 配列 | アイテムオブジェクトを含む配列。アイテムオブジェクトには、`id` フィールドを除くカタログのすべてのフィールドを含める必要があります。1つのリクエストにつき、1つのアイテムオブジェクトのみが許可されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Request parameters" }

## リクエスト例 {#example-request}

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
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
    }
  ]
}'
```

{% alert note %}
`Location` フィールドは `geo` データタイプを使用しており、`[経度, 緯度]` の形式の配列を期待します。
{% endalert %}

## 応答 {#response}

このエンドポイントには、`201`、`400`、`404` の3つのステータスコード応答があります。

### 成功応答の例 {#example-success-response}

ステータスコード `201` は、次の応答本文を返す可能性があります。

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

次のテーブルに、返される可能性のあるエラーと、関連するトラブルシューティングステップを示します。

| エラー | トラブルシューティング |
| --- | --- |
| `arbitrary-error` | 任意のエラーが発生しました。もう一度試すか、[サポート]({{site.baseurl}}/support_contact)に連絡してください。 |
| `catalog-not-found` | カタログ名が有効であることを確認してください。 |
| `filtered-set-field-too-long` | フィールド値が、アイテムの文字数制限を超えるフィルターセットで使用されています。 |
| `id-in-body` | リクエスト本文のアイテムIDを削除してください。 |
| `ids-too-large` | 各アイテムIDの文字数制限は250文字です。 |
| `invalid-ids` | アイテムID名に使用できる文字は、アルファベット、数字、ハイフン、アンダースコアです。 |
| `invalid-fields` | APIリクエストで送信するすべてのフィールドが、すでにカタログに存在していることを確認してください。これは、エラーに記載されているIDフィールドとは関係ありません。 |
| `invalid-keys-in-value-object` | アイテムオブジェクトのキーに `.` または `$` を含めることはできません。 |
| `item-already-exists` | そのアイテムはすでにカタログに存在しています。 |
| `item-array-invalid` | `items` はオブジェクトの配列でなければなりません。 |
| `items-too-large` | 各アイテムの文字数制限は5,000文字です。 |
| `request-includes-too-many-items` | 1つのリクエストにつき1つのカタログアイテムしか作成できません。 |
| `too-deep-nesting-in-value-object` | アイテムオブジェクトは50レベルを超えるネストを持つことはできません。 |
| `unable-to-coerce-value` | アイテムタイプは変換できません。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting" }

{% endapi %}