---
nav_title: "PATCH: カタログアイテムを編集"
article_title: "PATCH: カタログアイテムの編集"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "この記事では、カタログアイテムの編集Brazeエンドポイントについての詳細を説明します。"

---
{% api %}
# カタログアイテムを編集する {#edit-catalog-item}
{% apimethod patch %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> このエンドポイントを使用して、カタログの既存のアイテムを編集します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e35976ae-ff77-42b7-b691-a883c980d8c0 {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`catalogs.update_item` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

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
| `items` | 必須 | 配列 | アイテムオブジェクトを含む配列。アイテムオブジェクトには、`id` フィールドを除き、カタログに存在するフィールドを含める必要があります。1つのリクエストにつき、1つのアイテムオブジェクトのみが許可されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Request parameters" }

## リクエスト例 {#example-request}

```
curl --location --request PATCH 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "Name": "Restaurant",
      "Loyalty_Program": false,
      "Location": [-73.988103, 40.779109],
      "Preferences": {
        "favorite_brand": "Nike",
        "shirt_size": "L"
      },
      "Top_Dishes": {
        "$add": [
          "Biscuits",
          "Coleslaw"
        ],
        "$remove": [
          "French Fries"
        ]
      },
      "Open_Time": "2021-09-03T09:03:19.967+00:00"
    }
  ]
}'
```

{% alert note %}
- `Location` フィールドは `geo` データタイプを使用しており、`[経度, 緯度]` の形式の配列を想定しています。
- `$add` および `$remove` 演算子は配列型フィールドにのみ適用可能であり、PATCHエンドポイントでのみサポートされています。
{% endalert %}

## 応答 {#response}

このエンドポイントには、`200`、`400`、`404` の3つのステータスコード応答があります。

### 成功応答の例 {#example-success-response}

ステータスコード `200` は、次の応答本文を返す可能性があります。

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
| `arbitrary-error` | 任意のエラーが発生しました。もう一度試すか、[サポート]({{site.baseurl}}/support_contact/)に連絡してください。 |
| `catalog-not-found` | カタログ名が有効であることを確認してください。 |
| `filtered-set-field-too-long` | フィールド値が、アイテムの文字数制限を超えるフィルターセットで使用されています。 |
| `id-in-body` | アイテムIDがすでにカタログに存在しています。 |
| `ids-too-large` | 各アイテムIDの文字数制限は250文字です。 |
| `invalid-ids` | アイテムID名に使用できる文字は、アルファベット、数字、ハイフン、アンダースコアです。 |
| `invalid-fields` | リクエストのフィールドがカタログに存在することを確認してください。 |
| `invalid-keys-in-value-object` | アイテムオブジェクトのキーに `.` または `$` を含めることはできません。 |
| `item-not-found` | そのアイテムがカタログに存在するか確認してください。 |
| `item-array-invalid` | `items` はオブジェクトの配列でなければなりません。 |
| `items-too-large` | 各アイテムの文字数制限は5,000文字です。 |
| `request-includes-too-many-items` | 1つのリクエストにつき1つのカタログアイテムのみ編集できます。 |
| `too-deep-nesting-in-value-object` | アイテムオブジェクトは50レベル以上のネストを持つことはできません。 |
| `unable-to-coerce-value` | アイテムタイプは変換できません。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting" }

{% endapi %}