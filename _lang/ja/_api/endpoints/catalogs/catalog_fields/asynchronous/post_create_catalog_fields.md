---
nav_title: "POST:カタログフィールドの作成"
article_title: "POST:カタログフィールドの作成"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "この記事では、「カタログフィールドの作成」Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# カタログフィールドの作成 {#create-catalog-fields}
{% apimethod post %}
/catalogs/{catalog_name}/fields
{% endapimethod %}

> このエンドポイントを使用して、カタログに複数のフィールドを作成します。

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`catalogs.create_fields` 権限を持つ [APIキー]({{site.baseurl}}/api/basics#rest-api-key)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog fields' %}

## パスパラメーター {#path-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| -------------- | -------- | --------- | -------------------- |
| `catalog_name` | 必須 | 文字列 | カタログ名。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="パスパラメーター" }

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------ |
| `fields` | 必須 | 配列 | フィールドオブジェクトを含む配列。フィールドオブジェクトには、新しいフィールドの名前とタイプが含まれている必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="リクエストパラメーター" }

## リクエスト例 {#example-request}

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/fields' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "fields": [
    {
      "name": "Name",
      "type": "string"
    },
    {
      "name": "Ratings",
      "type": "number"
    },
    {
      "name": "Loyalty_Program",
      "type": "boolean"
    },
    {
      "name": "Created_At",
      "type": "time"
    },
    {
      "name": "Location",
      "type": "geo"
    }
  ]
}'
```

{% alert note %}
位置情報フィールドの値は `[longitude, latitude]` 配列として指定する必要があります（例: `[-73.988103, 40.779109]`）。緯度は -90 から 90 の範囲、経度は -180 から 180 の範囲でなければなりません。
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
      "id": "catalog-not-found",
      "message": "Could not find catalog",
      "parameters": [
        "catalog_name"
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

次のテーブルに、返される可能性のあるエラーと、関連するトラブルシューティングステップを示します。

| エラー | トラブルシューティング |
|--------------------------------------|--------------------------------------------------------------------------------------------------------|
| `arbitrary-error` | 任意のエラーが発生しました。もう一度試すか、[サポート]({{site.baseurl}}/support_contact)に連絡してください。 |
| `catalog-not-found` | カタログ名が有効であることを確認してください。 |
| `company-size-limit-already-reached` | カタログのストレージサイズの上限に達しています。 |
| `request-includes-too-many-fields` | 各リクエストは最大50の新規フィールドをサポートできます。 |
| `catalog-exceeds-fields-limit` | カタログは500を超えるフィールドを持つことはできません。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="トラブルシューティング" }

{% endapi %}