---
nav_title: "カタログセレクションオブジェクト"
article_title: APIカタログセレクションオブジェクト
page_order: 12
page_type: reference
description: "このリファレンス記事では、カタログセレクションオブジェクトのさまざまなコンポーネントについて説明します。"
tool: Catalogs

---

# カタログセレクションオブジェクト {#catalog-selection-object}

> カタログセレクションを作成する際に、セレクションオブジェクトを提供することで、カタログから返されるアイテムのフィルタリング、ソート、および制限の基準を定義できます。

`selection`オブジェクトを使用すると、フィルターに基づいてカタログからセレクションに含めるアイテムを指定し、それらの並べ替え方法や返す結果の数を設定できます。このオブジェクトは、APIを通じてカタログセレクションを作成する際に使用します。

## オブジェクト本体 {#object-body}

```json
{
  "selection": {
    "name": "Sale",
    "description": "Sales Collection",
    "external_id": "12345678",
    "source": "Shopify",
    "filters": [
      {
        "field": "collection",
        "operator": "includes value",
        "value": "Best Seller"
      },
      {
        "field": "collection",
        "operator": "does not include value",
        "value": "Sale"
      }
    ],
    "results_limit": 5,
    "sort_field": "id",
    "sort_order": "asc"
  }
}
```

## オブジェクトの詳細 {#object-details}

| キー | 必須 | データタイプ | 説明 |
| --- | -------- | --------- | ----------- |
| `name` | 必須 | 文字列 | カタログセレクションの名前。 |
| `description` | オプション | 文字列 | カタログセレクションの説明。 |
| `external_id` | 必須 | 文字列 | セレクションのユニークな識別子。 |
| `source` | オプション | 文字列 | カタログデータのソース。Shopifyカタログの場合は`"Shopify"`に設定します。使用可能な値は`"Shopify"`と`"Braze"`です。 |
| `filters` | オプション | オブジェクト配列 | カタログアイテムに適用するフィルターオブジェクトの配列。リクエストごとに最大4つのフィルターを指定できます。フィルターが指定されていない場合、カタログ内のすべてのアイテムが含まれます。 |
| `results_limit` | オプション | 整数 | 返す結果の最大数。1から50までの数値である必要があります。 |
| `sort_field` | オプション | 文字列 | 結果を並べ替えるフィールド。`sort_order`と組み合わせて使用する必要があります。`sort_field`と`sort_order`の両方が指定されていない場合、結果はランダムな順序で返されます。 |
| `sort_order` | オプション | 文字列 | 結果を並べ替える順序。使用可能な値は`"asc"`（昇順）または`"desc"`（降順）です。`sort_field`と組み合わせて使用する必要があります。`sort_field`と`sort_order`の両方が指定されていない場合、結果はランダムな順序で返されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Object details" }

### フィルターオブジェクト {#filter-object}

`filters`配列内の各フィルターオブジェクトには、以下の表で説明するフィールドが含まれます。

| キー | 必須 | データタイプ                                   | 説明 |
| --- | -------- | ------------------------------------------- | ----------- |
| `field`    | 必須 | 文字列                                      | フィルタリング対象のカタログフィールド。 |
| `operator` | 必須 | 文字列                                      | フィルタリングに使用する比較演算子。例として`"includes value"`や`"does not include value"`があります。 |
| `value`    | 必須 | 可変（文字列、数値、ブール値、時刻）     | 比較対象となる値。基となるカタログフィールドのデータタイプ（例：文字列、数値、ブール値、時刻）と一致する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Filter object" }

{% alert note %}
APIは、1回のセレクションリクエストにつき最大4つのフィルターをサポートしています。Brazeダッシュボードでは、各セレクションにつき最大10個のフィルターを追加できます。フィルターは配列内に記述された順序で適用されます。
{% endalert %}