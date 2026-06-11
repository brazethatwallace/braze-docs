---
nav_title: "POST:カタログを作成"
article_title: "POST:カタログを作成"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "この記事では、「カタログを作成」Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# カタログを作成する {#create-catalog}
{% apimethod post %}
/catalogs
{% endapimethod %}

> このエンドポイントを使用してカタログを作成します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#af9f3e2d-b7e7-49e7-aa64-f4652892be6e {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`catalogs.create` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key/)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='synchronous catalog' %}

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `catalogs` | 必須 | 配列 | カタログオブジェクトを含む配列。このリクエストでは、カタログオブジェクトは1つのみ許可されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Request parameters" }

### カタログオブジェクトのパラメーター {#catalog-object-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `name` | 必須 | 文字列 | 作成するカタログの名前。 |
| `description` | 必須 | 文字列 | 作成するカタログの説明。 |
| `fields` | 必須 | 配列 | キー `name` と `type` を含むオブジェクトの配列。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Catalog object parameters" }

## リクエスト例 {#example-request}
```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "catalogs": [
    {
      "name": "restaurants",
      "description": "My Restaurants",
      "fields": [
        {
          "name": "id",
          "type": "string"
        },
        {
          "name": "Name",
          "type": "string"
        },
        {
          "name": "City",
          "type": "string"
        },
        {
          "name": "Cuisine",
          "type": "string"
        },
        {
          "name": "Rating",
          "type": "number"
        },
        {
          "name": "Loyalty_Program",
          "type": "boolean"
        },
        {
          "name": "Location",
          "type": "geo"
        },
        {
          "name": "Preferences",
          "type": "object"
        },
        {
          "name": "Top_Dishes",
          "type": "array"
        },
        {
          "name": "Created_At",
          "type": "time"
        }
      ]
    }
  ]
}'
```

{% alert note %}
`geo` データタイプは、地理座標を `[longitude, latitude]` の形式の配列として格納します。例: `[-73.988103, 40.779109]`。
{% endalert %}

## 応答 {#response}

このエンドポイントには `201` と `400` の2つのステータスコード応答があります。

### 成功応答の例 {#example-success-response}

ステータスコード `201` は、次の応答本文を返す可能性があります。

```json
{
  "catalogs": [
    {
      "description": "My Restaurants",
      "fields": [
        {
          "name": "id",
          "type": "string"
        },
        {
          "name": "Name",
          "type": "string"
        },
        {
          "name": "City",
          "type": "string"
        },
        {
          "name": "Cuisine",
          "type": "string"
        },
        {
          "name": "Rating",
          "type": "number"
        },
        {
          "name": "Loyalty_Program",
          "type": "boolean"
        },
        {
          "name": "Location",
          "type": "geo"
        },
        {
          "name": "Preferences",
          "type": "object"
        },
        {
          "name": "Top_Dishes",
          "type": "array"
        },
        {
          "name": "Created_At",
          "type": "time"
        }
      ],
      "name": "restaurants",
      "num_items": 0,
      "updated_at": "2022-11-02T20:04:06.879+00:00"
    }
  ],
  "message": "success"
}
```

### エラー応答の例 {#example-error-response}

ステータスコード `400` は、次の応答本文を返す可能性があります。遭遇する可能性のあるエラーの詳細については、「[トラブルシューティング](#troubleshooting)」を参照してください。

```json
{
  "errors": [
    {
      "id": "catalog-name-already-exists",
      "message": "A catalog with that name already exists",
      "parameters": [
        "name"
      ],
      "parameter_values": [
        "restaurants"
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
| `catalog-array-invalid` | `catalogs` はオブジェクトの配列でなければなりません。 |
| `catalog-name-already-exists` | その名前のカタログはすでに存在しています。 |
| `catalog-name-too-large` | カタログ名の文字数制限は250文字です。 |
| `description-too-long` | 説明の文字数制限は250文字です。 |
| `field-names-not-unique` | 同じフィールド名が2回参照されています。 |
| `field-names-too-large` | フィールド名の文字数制限は250文字です。 |
| `id-not-first-column` | `id` は配列の最初のフィールドでなければなりません。型が文字列であることを確認してください。 |
| `invalid-catalog-name` | カタログ名にはアルファベット、数字、ハイフン、アンダースコアのみを含めることができます。 |
| `invalid-field-names` | フィールドに含めることができるのは、アルファベット、数字、ハイフン、アンダースコアのみです。 |
| `invalid-field-types` | フィールドタイプが有効であることを確認してください。 |
| `invalid-fields` | `fields` が正しくフォーマットされていません。 |
| `too-many-catalog-atoms` | 1つのリクエストにつき1つのカタログしか作成できません。 |
| `too-many-fields` | フィールド数の上限は500です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting" }

{% endapi %}