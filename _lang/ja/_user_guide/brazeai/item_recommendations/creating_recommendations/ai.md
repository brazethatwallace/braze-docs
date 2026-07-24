---
nav_title: AIレコメンデーション
article_title: AI項目レコメンデーションの作成
description: "このリファレンス記事では、カタログ内の項目に対してAI項目レコメンデーションを作成する方法を説明します。"
page_order: 1
---

# AI項目レコメンデーションを作成する {#create-ai-item-recommendations}

> カタログ内の項目からAIレコメンデーションエンジンを作成する方法について説明します。

## AIアイテムレコメンデーションについて {#about-ai-item-recommendations}

AIアイテムレコメンデーションを使用して、最も人気のある商品を計算したり、特定の[カタログ]({{site.baseurl}}/user_guide/brazeai/item_recommendations)に対してパーソナライズされたAIレコメンデーションを作成したりできます。レコメンデーションを作成した後、パーソナライゼーションを使用してそれらの商品をメッセージに挿入できます。

{% alert tip %}
[AIパーソナライズドレコメンデーション](#recommendation-types)は、少なくとも数百のカタログアイテム、最大100,000のカタログアイテム、そして通常少なくとも30,000人の購入またはインタラクションデータを持つユーザーがいる場合に最も効果的に機能します。これはあくまで大まかな目安であり、状況によって異なる場合があります。その他のレコメンデーションタイプはより少ないデータでも機能します。これには、フォールバックとして**最も人気**を使用する場合も含まれます。
{% endalert %}

{% multi_lang_include brazeai/recommendations/ai.md section="Plan-specific features" %}

## AIアイテムレコメンデーションの作成 {#creating-an-ai-item-recommendation}

### 前提条件 {#prerequisites}

開始する前に、以下が必要です。

- いずれかの[レコメンデーションタイプ]({{site.baseurl}}/user_guide/data/activation/catalogs)を使用するための[カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs)が少なくとも1つ。
- カタログアイテムIDと一致するアイテムへの参照を含む、Braze上の購入またはイベントデータ（カスタムイベント、注文確定イベント、または購入オブジェクト）。

### ステップ1:新しいレコメンデーションを作成する {#step-1-create-a-new-recommendation}

AIアイテムレコメンデーションは、ダッシュボードの以下のいずれかの場所から作成できます。

{% tabs local %}
{% tab ナビゲーションメニューから %}
1. **分析** > **AIアイテムレコメンデーション**に移動します。
2. **予測を作成** > **AIアイテムレコメンデーション**を選択します。
{% endtab %}

{% tab カタログから %}
個別のカタログから直接レコメンデーションを作成することもできます。**カタログ**ページからカタログを選択し、**レコメンデーションを作成**を選択します。
{% endtab %}
{% endtabs %}

### ステップ2:レコメンデーションの詳細を追加する {#step-2-add-recommendation-details}

レコメンデーションに名前と任意の説明を入力します。

![名前と説明のフィールドがある「レコメンデーションの詳細」ステップ。]({% image_buster /assets/img/item_recs_1.png %})

### ステップ3:レコメンデーションを定義する {#recommendation-type}

レコメンデーションタイプを選択します。各タイプは、購入、注文確定、またはカスタムイベントデータなど、過去6か月間のアイテムインタラクションデータを使用します。各タイプの詳細情報とユースケースについては、[タイプとユースケース]({{site.baseurl}}/user_guide/brazeai/item_recommendations)を参照してください。

{% alert tip %}
**最新**または**AIパーソナライズド**を使用する場合、個別のレコメンデーションを作成するのに十分なデータがないユーザーには、フォールバックとして**最も人気**のアイテムが表示されます。**最も人気**のフォールバックは、リンクされたカタログに存在するアイテムのみを返します。<br><br>**AIパーソナライズド**レコメンデーションの場合、**分析**ページの**パーソナライゼーション率**を確認すると、過去24か月間に設定されたイベントを実行したユーザーのうち、パーソナライズされたレコメンデーションがプロファイルに保存されているユーザーの割合を確認できます。**最新**レコメンデーションの場合、**分析**ページには、**最新**レコメンデーションを受け取っているユーザーと**最も人気**フォールバックを受け取っているユーザーの割合が表示されます。
{% endalert %}

#### ステップ3.1:過去の購入またはインタラクションを除外する（任意） {#step-31-exclude-prior-purchases-or-interactions-optional}

ユーザーがすでに購入またはインタラクションしたアイテムの提案を避けるには、**ユーザーが以前にインタラクションしたアイテムをレコメンドしない**を選択します。このオプションは、レコメンデーションの**タイプ**が**AIパーソナライズド**に設定されている場合にのみ利用できます。

![「AIパーソナライズド」がタイプとして選択され、「ユーザーが以前にインタラクションしたアイテムをレコメンドしない」オプションが選択された「レコメンデーションを定義する」ステップ。]({% image_buster /assets/img/item_recs_2-3.png %})

この設定により、レコメンデーションが最近更新されている場合、ユーザーがすでに購入またはインタラクションしたアイテムがメッセージで再利用されることを防ぎます。レコメンデーションの更新間に購入またはインタラクションされたアイテムは、引き続き表示される場合があります。アイテムレコメンデーションの無料版では、更新は毎週行われます。AIアイテムレコメンデーションのPro版では、更新は24時間ごとに行われます。

たとえば、AIアイテムレコメンデーションのPro版を使用している場合、ユーザーが何かを購入してから30分以内にマーケティングメールを受信すると、購入したばかりのアイテムがメールから除外されない場合があります。ただし、24時間後に送信されるメッセージにはそのアイテムは含まれません。

#### ステップ3.2:カタログを選択する {#step-32-select-a-catalog}

まだ入力されていない場合は、このレコメンデーションがアイテムを取得する[カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs)を選択します。

#### ステップ3.3:セレクションを追加する（任意） {#step-33-add-a-selection-optional}

レコメンデーションをより細かくコントロールしたい場合は、[セレクション]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)を選択してカスタムフィルターを適用します。セレクションは、ブランド、サイズ、場所など、カタログ内の特定の列でレコメンデーションをフィルタリングします。Liquidを含むセレクションはレコメンデーションでは使用できません。

![レコメンデーションに「在庫あり」セレクションが選択された例。]({% image_buster /assets/img/item_recs_2-2.png %})

{% alert tip %}
セレクションが見つからない場合は、まずカタログで設定されていることを確認してください。
{% endalert %}

### ステップ4:レコメンデーションを駆動するインタラクションを選択する {#step-4-select-the-interaction-to-drive-recommendations}

このレコメンデーションが最適化するイベントを選択します。このイベントは通常購入ですが、アイテムとの任意のインタラクションにすることもできます。

{% alert tip %}
AIアイテムレコメンデーションを設定する際、イベントの選択は重要です。トリガーイベントによって、AI生成レコメンデーションを受け取るユーザーが決まります。AIアイテムレコメンデーションは、設定したイベントを完了したユーザーに対して生成されるため、この選択がレコメンデーションを受け取るユーザーを直接決定します。リーチしたいオーディエンスセグメント全体をカバーするイベントを選択してください。<br><br>同時に、カバレッジと関連性のバランスを取ってください。ファネル上部のイベント（商品閲覧など）はより広いオーディエンスを捕捉する傾向がありますが、ビジネス成果との関連性は低くなります。一方、ファネル下部のイベント（購入など）はより的を絞った、ビジネスに関連性の高いレコメンデーションを生成する傾向があります。最適なイベントは、カバレッジと収益への影響のバランスが取れたものです。
{% endalert %}

以下に対して最適化できます。

- [購入オブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object)を使用した購入イベント
- 購入を表すカスタムイベント
- その他のアイテムインタラクション（商品閲覧、クリック、メディア再生など）を表すカスタムイベント
- [注文確定イベント]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events?tab=ecommerce.order_placed)を使用した注文確定

**カスタムイベント**を選択した場合は、リストからイベントを選択します。

![イベントの現在のトラッキング方法として「purchase」カスタムイベントが選択されている画面。]({% image_buster /assets/img/item_recs_3.png %})

{% alert note %}
カスタムイベントは、イベントリストに表示される前に十分なデータが必要です。カスタムイベントが表示されない場合は、Brazeバックエンドがまだ処理していないか、モデルのトレーニングに十分なデータがない可能性があります。AIレコメンデーションはインサイトを生成するために履歴データに依存しているため、新しく作成されたイベントやめったにトリガーされないイベントは、より多くのデータが収集されるまで利用できません。
{% endalert %}

### ステップ5:対応するプロパティ名を選択する {#property-name}

レコメンデーションを作成するには、インタラクションイベント（注文確定イベント、購入オブジェクト、またはカスタムイベント）のどのフィールドが、カタログ内のアイテムの`id`フィールドと一致する一意の識別子を持っているかをBrazeに伝える必要があります。不明な場合は、[要件](#requirements)を参照してください。

**プロパティ名**でこのフィールドを選択します。

**プロパティ名**フィールドには、SDKを通じてBrazeに送信されたフィールドのリストが事前に入力されます。十分なデータが提供されている場合、これらのプロパティは正しいプロパティである確率の順にランク付けされます。カタログの`id`フィールドに対応するものを選択してください。

![カタログ内のアイテムIDに対応するプロパティ名「purchase_item」が選択されている画面。]({% image_buster /assets/img/item_recs_4.png %})

#### 要件 {#requirements}

プロパティの選択にはいくつかの要件があります。

- 選択したカタログの`id`フィールドにマッピングされる必要があります。
- **注文確定イベントを選択した場合、または[eコマースイベント]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events)を使用してアイテムレコメンデーションをトレーニングする場合：**商品IDには`products.product_id`を入力します。
  - フィールドは商品の配列内にあるか、IDの配列で終わることができます。いずれの場合も、各商品IDは同じタイムスタンプを持つ個別の連続イベントとして扱われます。
- **購入オブジェクトを選択した場合：**`product_id`またはインタラクションイベントの`properties`のフィールドである必要があります。
- **カスタムイベントを選択した場合：**カスタムイベントの`properties`のフィールドである必要があります。
- ネストされたフィールドは、`event_property.nested_property`の形式でドット記法を使用して**プロパティ名**ドロップダウンに入力する必要があります。たとえば、イベントプロパティ`location`内のネストされたプロパティ`district_name`を選択する場合は、`location.district_name`と入力します。

#### マッピング例 {#example-mappings}

以下のマッピング例は、どちらもこのサンプルカタログを参照しています。

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table aria-label="マッピング例" class="tg">
  <caption>マッピング例</caption>
<thead>
  <tr>
    <th class="tg-0pky">id</th>
    <th class="tg-0pky">title</th>
    <th class="tg-0pky">price</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">ADI-BL-7</td>
    <td class="tg-0pky">Adidas Black Size 7</td>
    <td class="tg-0pky">100.00 USD</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADI-RD-8</td>
    <td class="tg-0pky">Adidas Red Size 8</td>
    <td class="tg-0pky">100.00 USD</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADI-WH-9</td>
    <td class="tg-0pky">Adidas White Size 9</td>
    <td class="tg-0pky">100.00 USD</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADI-PP-10</td>
    <td class="tg-0pky">Adidas Purple Size 10</td>
    <td class="tg-0pky">75.00 USD</td>
  </tr>
</tbody>
</table>

{% tabs %}
{% tab カスタムイベント %}

カスタムイベント`added_to_cart`を使用して、顧客がチェックアウトする前に類似商品をレコメンドしたいとします。イベント`added_to_cart`には、イベントプロパティ`product_sku`があります。

この場合、`product_sku`プロパティには、サンプルカタログの`id`列の値のうち少なくとも1つが含まれている必要があります：「ADI-BL-7」、「ADI-RD-8」、「ADI-WH-9」、または「ADI-PP-10」。すべてのカタログアイテムに対するイベントは必要ありませんが、レコメンデーションエンジンが十分なコンテンツで動作できるように、いくつかは必要です。

##### カスタムイベントオブジェクトの例 {#example-custom-event-object}

このイベントには`"product_sku": "ADI-BL-7"`があり、サンプルカタログの最初のアイテムと一致します。

```json
{
  "events": [
    {
      "external_id": "user1",
      "app_id": "your-app-id",
      "name": "added_to_cart",
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "product_sku": "ADI-BL-7"
      }
    }
  ]
}
```

##### 商品配列を含むカスタムイベントオブジェクトの例 {#example-custom-event-object-with-an-array-of-products}

イベントプロパティに配列内の複数の商品が含まれている場合、各商品IDは個別の連続イベントとして扱われます。このイベントでは、プロパティ`products.sku`を使用してサンプルカタログの1番目と3番目のアイテムと一致させることができます。

```json
{
  "events": [
    {
      "external_id": "user1",
      "app_id": "your-app-id",
      "name": "added_to_cart",
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "transaction_id": "2ff3f9a9-8803-4c3a-91da-14adbf93dc99",
        "products": [
          { "sku": "ADI-BL-7" },
          { "sku": "ADI-WH-9" }
        ]
      }
    }
  ]
}
```

##### 商品ID配列を含むネストされたオブジェクトのカスタムイベントオブジェクトの例 {#example-custom-event-object-with-a-nested-object-containing-a-product-id-array}

商品IDがオブジェクトではなく配列内の値である場合、同じ記法を使用でき、各商品IDは個別の連続イベントとして扱われます。これは、以下のイベントでネストされたオブジェクトと柔軟に組み合わせることができ、プロパティを`purchase.product_skus`として設定することで、サンプルカタログの1番目と3番目のアイテムと一致させることができます。

```json
{
  "events": [
    {
      "external_id": "user1",
      "app_id": "your-app-id",
      "name": "added_to_cart",
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "transaction_id": "13791e08-7c22-4f6c-8cc6-832c76af3743",
        "purchase": {
          "product_skus": ["ADI-BL-7", "ADI-WH-9"]
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab 購入オブジェクト %}

購入オブジェクトは、購入が行われたときにAPIを通じて渡されます。

マッピングに関しては、購入オブジェクトにもカスタムイベントと同様のロジックが適用されますが、購入オブジェクトの`product_id`または`properties`オブジェクト内のフィールドのいずれかを選択できます。

すべてのカタログアイテムに対するイベントは必要ありませんが、レコメンデーションエンジンが十分なコンテンツで動作できるように、いくつかは必要です。

##### 商品IDにマッピングされた購入オブジェクトの例 {#example-purchase-object-mapped-to-product-id}

このイベントには`"product_id": "ADI-BL-7"`があり、カタログの最初のアイテムにマッピングされます。

```json
{
  "purchases": [
    {
      "external_id": "user1",
      "app_id": "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id": "ADI-BL-7",
      "currency": "USD",
      "price": 100.00,
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "color": "black",
        "checkout_duration": 180,
        "size": "7",
        "brand": "Adidas"
      }
    }
  ]
}
```

##### プロパティフィールドにマッピングされた購入オブジェクトの例 {#example-purchase-object-mapped-to-a-properties-field}

このイベントにはプロパティ`"sku": "ADI-RD-8"`があり、カタログの2番目のアイテムにマッピングされます。

```json
{
  "purchases": [
    {
      "external_id": "user1",
      "app_id": "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id": "shoes",
      "currency": "USD",
      "price": 100.00,
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "sku": "ADI-RD-8",
        "color": "red",
        "checkout_duration": 180,
        "size": "8",
        "brand": "Adidas"
      }
    }
  ]
}
```

{% endtab %}
{% tab 注文確定イベント %}

##### 商品IDにマッピングされた注文確定オブジェクトの例 {#example-order-placed-object-mapped-to-product-id}

```json
{
  "name": "ecommerce.order_placed",
  "properties": {
    "order_id": "order_123",
    "total_value": 200.0,
    "currency": "USD",
    "products": [
      {
        "product_id": "ADI-BL-7",
        "product_name": "Adidas Black Size 7",
        "variant_id": "ADI-BL-7-default",
        "quantity": 1,
        "price": 100.0
      }
    ],
    "source": "storefront"
  }
}
```

{% endtab %}
{% endtabs %}

### ステップ6:レコメンデーションをトレーニングする {#step-6-train-the-recommendation}

準備ができたら、**レコメンデーションを作成**を選択します。このプロセスは完了までに10分から36時間かかる場合があります。レコメンデーションのトレーニングが正常に完了した場合、または作成が失敗した理由の説明がメールで届きます。

レコメンデーションは**予測**ページで確認でき、必要に応じて編集またはアーカイブできます。レコメンデーションは毎週（有料版）または毎月（無料版）自動的に再トレーニングされます。