---
nav_title: "PUT: 複数のカタログ項目を置き換える"
article_title: "PUT: 複数のカタログ項目を置き換える"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "この記事では、「複数のカタログ項目を置き換える」Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# カタログ項目を置き換える {#replace-catalog-items}
{% apimethod put %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> このエンドポイントを使用して、カタログ内の複数の項目を置き換えます。

カタログ項目が存在しない場合、このエンドポイントはカタログ内にその項目を作成します。1回のリクエストにつき、最大50個のカタログ項目に対応できます。このエンドポイントは非同期です。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#ab30a4fc-60bc-4460-885c-1b92af8bc061 {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`catalogs.replace_items` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

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
| `items` | 必須 | 配列 | 項目オブジェクトを含む配列。各オブジェクトにはIDが必要です。項目オブジェクトには、カタログに存在するフィールドが含まれている必要があります。リクエストごとに最大50個の項目オブジェクトが許可されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="リクエストパラメーター" }

## リクエスト例 {#example-request}

```
curl --location --request PUT 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "id": "restaurant1",
      "Name": "Restaurant",
      "Loyalty_Program": false,
      "Location": [-73.988103, 40.779109],
      "Preferences": {
        "favorite_brand": "Nike",
        "shirt_size": "L"
      },
      "Top_Dishes": [
        "Hamburger",
        "Deluxe Cheeseburger"
      ],
      "Open_Time": "2021-09-03T09:03:19.967+00:00"
    },
    {
      "id": "restaurant3",
      "City": "San Francisco",
      "Rating": 2,
      "Top_Dishes": [
        "Hot Dog",
        "French Fries"
      ]
    }
  ]
}'
```

{% alert note %}
`Location` フィールドは `geo` データタイプを使用しており、`[経度, 緯度]` の形式の配列を期待します。
{% endalert %}

## レスポンス {#response}

このエンドポイントには、`202`、`400`、`404` の3つのステータスコードレスポンスがあります。

{% alert note %}
カタログのストレージ上限に達した場合にも、`400` レスポンスが返されることがあります。カタログの無料版は500&nbsp;MBが上限です。ストレージ階層とアップグレード方法の詳細については、[データストレージの制限]({{site.baseurl}}/user_guide/data/activation/catalogs#data-storage-limitations)を参照してください。
{% endalert %}

### 成功レスポンスの例 {#example-success-response}

ステータスコード `202` は、次のレスポンスボディを返す可能性があります。

```json
{
  "message": "success"
}
```

### エラーレスポンスの例 {#example-error-response}

ステータスコード `400` は、次のレスポンスボディを返す可能性があります。発生する可能性のあるエラーの詳細については、[トラブルシューティング](#troubleshooting)を参照してください。

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
| `catalog-not-found` | カタログ名が有効であることを確認してください。 |
| `company-size-limit-already-reached` | カタログのストレージサイズ上限に達しています。ストレージ階層の詳細については、[データストレージの制限]({{site.baseurl}}/user_guide/data/activation/catalogs#data-storage-limitations)を参照してください。 |
| `company-size-limit-surge` | リクエストが会社の残りのカタログストレージを超えています。より小さい更新で再試行してください。ストレージ階層の詳細については、[データストレージの制限]({{site.baseurl}}/user_guide/data/activation/catalogs#data-storage-limitations)を参照してください。 |
| `ids-not-string` | 各項目IDが文字列であることを確認してください。 |
| `ids-not-unique` | 各項目IDが一意であることを確認してください。 |
| `ids-too-large` | 各項目IDの文字数制限は250文字です。 |
| `item-array-invalid` | `items` はオブジェクトの配列でなければなりません。 |
| `items-missing-ids` | 項目IDがない項目があります。各項目にIDがあることを確認してください。 |
| `items-too-large` | 項目の値は5,000文字を超えることはできません。 |
| `invalid-ids` | 項目ID名に使用できる文字は、アルファベット、数字、ハイフン、アンダースコアです。 |
| `invalid-fields` | APIリクエストで送信するすべてのフィールドが、すでにカタログに存在していることを確認してください。これはエラーに記載されているIDフィールドとは関係ありません。 |
| `invalid-keys-in-value-object` | 項目オブジェクトのキーに `.` または `$` を含めることはできません。 |
| `too-deep-nesting-in-value-object` | 項目オブジェクトは50レベルを超えるネストを持つことはできません。 |
| `request-includes-too-many-items` | リクエストの項目数が多すぎます。リクエストごとの項目の上限は50個です。 |
| `unable-to-coerce-value` | 項目タイプは変換できません。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="トラブルシューティング" }

{% endapi %}