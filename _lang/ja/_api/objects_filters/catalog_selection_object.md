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

## オブジェクト本文 {#object-body}

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

| キー | 必須 | データ型 | 説明 |
| --- | -------- | --------- | ----------- |
| `name` | 必須 | String | カタログセレクションの名前。 |
| `description` | オプション | String | カタログセレクションの説明。 |
| `external_id` | オプション | String | セレクションの一意の識別子。 |
| `source` | オプション | String | カタログデータのソース。Shopifyカタログの場合、これを`"Shopify"`に設定します。指定可能な値は`"Shopify"`と`"Braze"`です。 |
| `filters` | 必須 | オブジェクトの配列 | カタログアイテムに適用するフィルターオブジェクトの配列。リクエストごとに最大10個のフィルターを指定できます。空のフィルター配列が指定された場合、カタログのすべてのアイテムが含まれます。 |
| `results_limit` | 必須 | Integer | 返す結果の最大数。1〜50の間の数値である必要があります。 |
| `sort_field` | オプション | String | 結果のソートに使用するフィールド。`sort_order`とペアで指定する必要があります。`sort_field`と`sort_order`の両方が指定されていない場合、結果はランダムな順序で返されます。 |
| `sort_order` | オプション | String | 結果のソート順。指定可能な値は`"asc"`（昇順）または`"desc"`（降順）です。`sort_field`とペアで指定する必要があります。`sort_field`と`sort_order`の両方が指定されていない場合、結果はランダムな順序で返されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="オブジェクトの詳細" }

### フィルターオブジェクト {#filter-object}

`filters`配列内の各フィルターオブジェクトには、以下の表に記載されているフィールドが含まれます。

| キー | 必須 | データ型                                   | 説明 |
| --- | -------- | ------------------------------------------- | ----------- |
| `field`    | 必須 | String                                      | フィルタリングするカタログフィールド。 |
| `operator` | 必須 | String                                      | フィルタリングに使用する比較演算子。例として`"includes value"`や`"does not include value"`があります。 |
| `value`    | 必須 | 可変（string、number、boolean、time）     | 比較する値。基礎となるカタログフィールドのデータ型（例：string、number、boolean、time）と一致する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="フィルターオブジェクト" }

{% alert note %}
APIはセレクションリクエストごとに最大10個のフィルターをサポートしています。フィルターは配列内に記載された順序で適用されます。
{% endalert %}