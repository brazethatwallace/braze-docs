---
nav_title: カタログアイテムを属性配列にマッチさせる
article_title: カタログアイテムをカスタム属性配列にマッチさせる
page_order: 2
page_type: reference
description: "カタログセレクションとLiquidを使用して、ウィッシュリストなどのカスタム属性配列に名前やIDが含まれるカタログ行を表示します。"
---

# カタログアイテムをカスタム属性配列にマッチさせる {#match-catalog-items-to-a-custom-attribute-array}

> 各ユーザーがプロファイルに保存した商品名のリストを持っている場合、カタログセレクションとLiquidを使用して、そのリストに含まれるカタログ行のみを表示できます（例：ウィッシュリストメール）。

## この例について {#about-this-example}

Flash & Threadは、各顧客の保存済み商品名を文字列配列カスタム属性（`saved_product_names`）に格納しています。カタログには商品の詳細情報（カテゴリ、価格、画像URL、在庫）が保持されています。

カタログセレクションは、静的な値やLiquidの値（カタログ行の配列フィールドを含む）に対してカタログ列をフィルタリングできます。ただし、ユーザープロファイル配列に格納された値に対してカタログ行をフィルタリングすることはできません。ユーザーのリストからパーソナライズするには、セレクションで広範なカタログアイテムのセットを返し、Liquidを使用してプロファイル配列にマッチする行のみを保持します。

このパターンでは以下を行います：

1. ユーザーの配列カスタム属性をLiquid変数に割り当てます。
2. 事前にフィルタリングされたカタログセレクション（最大50アイテム）に対して`catalog_selection_items`を呼び出します。
3. `items`をループし、`contains`を使用して各カタログフィールド（例：`name`や`id`）を配列と照合します。

{% alert important %}
このパターンは、セレクションの結果セット（最大50カタログ行）に各ユーザーの保存済みアイテムが含まれる可能性がある場合にのみ機能します。例えば、小規模なカタログや、フィルターによってセレクションが十分に絞り込まれ、一般的なリストをカバーできる場合です。ユーザーの保存済みアイテムが返される50行の範囲外にある場合、ループはマッチを見つけられず、メッセージにはそれらのアイテムが何も表示されません。セレクションはユーザーのプロファイル配列に対してマッチングできないため、一般的なケースではこれを解決するフィルターはありません。
{% endalert %}

## 考慮事項 {#considerations}

- 顧客に送信する前に、ステージングワークスペースでLiquidとカタログデータをテストしてください。
- セレクションは最大50カタログ行を返すため、各ユーザーの保存済みアイテムがその結果セット内に収まるようにフィルター（例：在庫あり、アクティブなカテゴリ、価格帯）を追加してください。
- この例では、ユーザープロファイル上の文字列配列を使用しています。
- オブジェクトの配列の場合は、各オブジェクト内のプロパティ（例：`product_id`）でマッチングし、`contains`チェックを調整するか、オブジェクトに対して`for`ループを使用してください。[オブジェクトの配列]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects)を参照してください。
- `contains`の動作は属性タイプによって異なります。配列の場合は`==`ではなく`contains`を使用してください。[条件付きロジック]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic)を参照してください。
- 商品名が変更されたり重複したりする可能性がある場合は、安定した識別子（例：カタログの`id`）でマッチングしてください。
- この記事のLiquidスニペットは例です。チャネル（メールHTML、プッシュなど）でレンダリングを検証してください。

## 設定 {#setup}

この例では以下を前提としています：

| アセット | 詳細 |
| --- | --- |
| カスタム属性 | `saved_product_names` — 文字列配列（例：`["linen_shirt", "trail_jacket", "canvas_tote"]`） |
| カタログ | `apparel_products`（列：`id`、`category`、`name`、`price`、`inventory`、`image_url`） |
| セレクション | `apparel_products`上の`in_stock_apparel`、結果上限50、不要な行を除外するフィルター付き（例：`inventory`が`0`より大きい） |
{: .reset-td-br-1 .reset-td-br-2 aria-label="設定" }

### ステップ1：カタログとセレクションを作成する {#step-1-create-the-catalog-and-selection}

1. `apparel_products`という名前のカタログに商品行をインポートまたは同期します。
2. 必要な数の関連行を返すセレクション（例：`in_stock_apparel`）を作成します（50アイテムの上限まで）。
3. メッセージに含めたくない行（在庫切れ、対象外カテゴリなど）を除外するセレクションフィルターを追加します。

セレクションの設定については、[セレクション]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)を参照してください。

### ステップ2：メッセージにLiquidを追加する {#step-2-add-liquid-in-your-message}

プロファイル配列を割り当て、セレクションを読み込み、`contains`でループします：

{% raw %}
```liquid
{% assign saved_product_names = custom_attribute.${saved_product_names} %}
{% catalog_selection_items apparel_products in_stock_apparel %}
{% for item in items %}
{% if saved_product_names contains item.name %}
Product: {{ item.name }}
Category: {{ item.category }}
Price: ${{ item.price }}
Image: {{ item.image_url }}
{% endif %}
{% endfor %}
```
{% endraw %}

配列がディスプレイ名ではなくIDを格納している場合は、`item.name`を`item.id`（または別の列）に置き換えてください。チャネルに合わせてフィールド間にスペースやHTMLを追加してください。{% raw %}`${{ item.price }}`{% endraw %}の`$`はLiquid出力の前に表示されるリテラルの通貨記号であり、Brazeの{% raw %}`${}`{% endraw %}パーソナライゼーション構文の一部ではありません。

このLiquidを自動生成するには、**パーソナライゼーションを追加**モーダル（**カタログアイテム** > **セレクションを使用**）を開いてください。[カタログの使用]({{site.baseurl}}/user_guide/data/activation/catalogs/use)を参照してください。

### ステップ3：プレビューとテスト {#step-3-preview-and-test}

異なる`saved_product_names`値を持つプロファイルにテストメッセージを送信します。マッチするカタログ行のみが表示されること、および空の配列では商品行が表示されないことを確認してください。

## 関連記事 {#related-articles}

- [カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs)
- [セレクション]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)
- [カタログの使用]({{site.baseurl}}/user_guide/data/activation/catalogs/use)
- [カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)
- [条件付きロジック]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic)
- [Liquidユースケースライブラリー — 配列内の文字列を検索する]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases#misc-string-in-array)