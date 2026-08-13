---
nav_title: "POST:カタログセレクションを作成する"
article_title: "POST:カタログセレクションを作成する"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "この記事では、「カタログセレクションの作成」Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# カタログセレクションを作成する {#create-catalog-selection}
{% apimethod post %}
/catalogs/{catalog_name}/selections
{% endapimethod %}

> このエンドポイントを使用して、カタログにセレクションを作成します。

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`catalogs.create_selection` 権限を持つ[APIキー]({{site.baseurl}}/api/basics#rest-api-key-permissions)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog selections' %}

## パスパラメーター {#path-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| -------------- | -------- | --------- | -------------------- |
| `catalog_name` | 必須 | 文字列 | カタログ名。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| ----------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `selection` | 必須 | オブジェクト | セレクション条件を含むオブジェクト。オブジェクトとそのフィールドの詳細については、[カタログセレクションオブジェクト]({{site.baseurl}}/api/objects_filters/catalog_selection_object)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### セレクションオブジェクトのパラメーター {#selection-object-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| ---------------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `name` | 必須 | 文字列 | カタログセレクションの名前。 |
| `description` | オプション | 文字列 | カタログセレクションの説明。 |
| `external_id` | 必須 | 文字列 | セレクションの一意の識別子。 |
| `source` | 必須 | 文字列 | カタログデータのソース。Shopifyカタログの場合は `"Shopify"` を使用します。カスタムカタログの場合は `"custom"` を使用します。 |
| `filters` | オプション | 配列 | カタログアイテムに適用するフィルターオブジェクトの配列。リクエストごとに最大4つのフィルターを指定できます。フィルターが指定されていない場合、カタログ内のすべてのアイテムが含まれます。 |
| `results_limit` | オプション | 整数 | 返す結果の最大数。1から50までの数値を指定する必要があります。 |
| `sort_field` | オプション | 文字列 | 結果をソートするフィールド。`sort_order`と組み合わせて使用する必要があります。`sort_field`と`sort_order`の両方が指定されていない場合、結果はランダムな順序で返されます。 |
| `sort_order` | オプション | 文字列 | 結果のソート順。有効な値は `"asc"`（昇順）または `"desc"`（降順）です。`sort_field`と組み合わせて使用する必要があります。`sort_field`と`sort_order`の両方が指定されていない場合、結果はランダムな順序で返されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
`sort_field`と`sort_order`パラメーターは必ず一緒に使用する必要があります。一方のみを指定した場合、または両方を省略した場合、セレクション結果はランダムな順序で返されます。
{% endalert %}

## リクエスト例 {#example-request}

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/selections' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "selection": {
    "name": "favorite-restaurants",
    "description": "Favorite restaurants in NYC",
    "external_id": "favorite-nyc-restaurants",
    "source": "custom",
    "filters": [
      {
        "field": "City",
        "operator": "equals",
        "value": "NYC"
      },
      {
        "field": "Rating",
        "operator": "greater than",
        "value": 7
      }
    ],
    "results_limit": 10,
    "sort_field": "Rating",
    "sort_order": "desc"
  }
}'
```

### フィルターオペレーター {#filter-operators}

| フィールドタイプ | サポートされているオペレーター |
| ---------- | ------------------------------------------------------- |
| `string` | `equals`, `does not equal` |
| `number` | `equals`, `does not equal`, `greater than`, `less than` |
| `boolean` | `is` |
| `time` | `before`, `after` |
| `array` | `includes value`, `does not include value` |
| `geo` | `geo within`, `geo outside` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
APIは、1回のセレクションリクエストにつき最大4つのフィルターをサポートしています。Brazeダッシュボードでは、セレクションごとに最大10個のフィルターを追加できます。フィルターは配列に記載された順序で適用されます。
{% endalert %}

{% alert note %}
`geo`フィルターを適用すると、`sort_field`および`sort_order`パラメーターに関係なく、システムは自動的に距離順（最も近いアイテムが先頭）で結果をソートします。
{% endalert %}

## 応答 {#response}

このエンドポイントには、`202`、`400`、`404`の3つのステータスコード応答があります。

### 成功応答の例 {#example-success-response}

ステータスコード `202` は、次の応答本文を返す可能性があります。

```json
{
  "message": "success"
}
```

### エラー応答の例 {#example-error-response}

ステータスコード `400` は、次の応答本文を返す可能性があります。発生する可能性のあるエラーの詳細については、「[トラブルシューティング](#troubleshooting)」を参照してください。

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
|--------------------------------------|-----------------------------------------------------------------------------------------------|
| `catalog-not-found` | カタログ名が有効であることを確認してください。 |
| `company-size-limit-already-reached` | カタログのストレージサイズの上限に達しています。 |
| `selection-limit-reached` | カタログのセレクション数が上限に達しています。 |
| `invalid-selection` | セレクションが有効であることを確認してください。 |
| `too-many-filters` | セレクションのフィルター数が多すぎないか確認してください。 |
| `selection-name-already-exists` | セレクション名がカタログ内にすでに存在していないか確認してください。 |
| `selection-has-invalid-filter` | セレクションフィルターが有効かどうか確認してください。 |
| `selection-invalid-results-limit` | セレクションの結果制限が有効かどうか確認してください。 |
| `invalid-sorting` | セレクションのソートが有効かどうか確認してください。 |
| `invalid-sort-field` | セレクションのソートフィールドが有効かどうか確認してください。 |
| `invalid-sort-order` | セレクションのソート順が有効かどうか確認してください。 |
| `selection-contains-too-many-arrays` | セレクションに `array` 型のフィールドが複数含まれていないか確認してください。サポートされているのは1つのみです。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}