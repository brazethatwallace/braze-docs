---
nav_title: 推奨イベント
article_title: 推奨イベント
alias: /recommended_events/
page_order: 2
page_type: reference
description: "このリファレンス記事では、Brazeがeコマースイベント向けに提供する推奨イベントについて説明します。"
---

# 推奨イベント {#recommended-events}

> 推奨イベントは、定義済みのJSONスキーマを持つ標準化されたカスタムイベントを送信するフレームワーク上に構築されています。推奨イベントを送信すると、Brazeは取り込み時にスキーマに対してバリデーションを行い、自動フィールド計算やカート管理など、汎用カスタムイベントでは適用されない特別な後処理を実行します。特定の業界向けイベントセットについては、キャンペーンやキャンバスの専用アクションベーストリガーなど、Brazeが特別な処理をサポートする場合があります。

## eコマース推奨イベント {#ecommerce-recommended-events}

[eコマース推奨イベント]({{site.baseurl}}/ecommerce_events)は、購入ジャーニーの6つのステップをカバーします：`product_viewed`、`cart_updated`、`checkout_started`、`order_placed`、`order_cancelled`、`order_refunded`。これらのイベントを正常に送信すると、Brazeはデータをバリデーションし、拡大し続けるプラットフォーム機能のセットで利用できるようにします。

これらの機能には、閲覧放棄、カート放棄、チェックアウト放棄、注文確認フローのキャンバステンプレート、eコマースレポート、*合計収益*、*合計注文数*、*合計返金額*の計算済みユーザープロファイルフィールドが含まれます。また、[セグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension)を使用してネストされた製品プロパティフィルタリングでセグメントを構築したり、{% raw %}`{% shopping_cart %}`{% endraw %} Liquidタグでカート放棄メッセージをパーソナライズしたり、[予測イベント]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events)、[解約予測]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn)、[アイテムレコメンデーション]({{site.baseurl}}/user_guide/brazeai/item_recommendations)などのBrazeAI<sup>TM</sup>機能にデータを供給したりすることもできます。

これらのイベントは定義済みのスキーマに従っているため、サポートされている各機能は、カスタムプロパティマッピングや機能ごとの設定を行うことなく、構造化データを読み取ることができます。

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

### eコマースイベントの仕組み {#how-ecommerce-events-work}

eコマースイベントは、事前定義された名前とプロパティスキーマを持つカスタムイベントです。[Braze SDK]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events)、[`/users/track` REST APIエンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)、または[Cloud Data Ingestion（CDI）]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)を使用して送信すると、Brazeは取り込み時に各イベントをそのスキーマに対してバリデーションします。バリデーションに合格すると、Brazeは収益フィールドの計算やユーザープロファイルのカート状態の管理など、そのイベントタイプに固有の後処理を自動的に適用します。

{% alert note %}
CSVアップロードはeコマースイベントをサポートしていません。これらのイベントを送信するには、SDK、`/users/track`、またはCDIを使用してください。
{% endalert %}

eコマースイベントは、他のカスタムイベントと同じ場所で機能します：実行されたカスタムイベントのトリガーとフィルター、カスタムイベントレポートなどです。ただし、スキーマバリデーションにより、以下のような追加機能が利用可能になります：

- キャンペーン、キャンバス、アクションパス、アプリ内メッセージトリガー、Content Cardsの削除における「注文する」トリガーアクション
- 計算済みeコマースユーザープロファイルフィールド（**合計収益**、**合計注文数**、**合計返金額**）
- カート放棄フローのためのカート状態管理
- 予測イベント、解約予測、アイテムレコメンデーションなどのBrazeAI<sup>TM</sup>機能のためのより豊富なデータ

また、プラットフォームがカスタムイベントをサポートしている場所であれば、eコマースイベントを名前で参照することもできます。たとえば、`ecommerce.product_viewed`イベントでアクションベースのキャンペーンをトリガーしたり、`ecommerce.checkout_started`イベントでフィルタリングするセグメントを構築したり、Currentsを通じて`ecommerce.order_placed`イベントをエクスポートしたりできます。

#### イベントの命名 {#event-naming}

イベント名は正確で、大文字と小文字が区別され、ドット区切りです。常に正規のフォーマットを使用してください。イベント名が6つの正規名のいずれかと正確に一致しない場合、Brazeはそれを標準のカスタムイベントとして扱い、eコマースの後処理は行われません。

イベントのカスタマイズや名前の変更はできません。

- **正しい例：** `ecommerce.order_placed`
- **誤った例：** `order.placed`、`eCommerce_order_placed`、`Order_Placed`

#### イベントスキーマ {#event-schemas}

6つのeコマース推奨イベントは、購入ジャーニーのステージにマッピングされます。ユーザーが対応するアクションを完了した時点で各イベントを発火してください。

![6つのeコマース推奨イベント（product_viewed、cart_updated、checkout_started、order_placed、order_cancelled、order_refunded）を通じたユーザージャーニーの図]({% image_buster /assets/img/shopify/event_schemas.png %})

{% alert tip %}
以下の例は、各イベントのREST APIペイロードを示しています。
クライアントサイドのロギングでは、`ecommerce.product_viewed`、`ecommerce.cart_updated`、`ecommerce.checkout_started`、`ecommerce.order_placed`は利用可能な場合にSDKのeコマースイベントAPIを使用し、`ecommerce.order_cancelled`と`ecommerce.order_refunded`は`logCustomEvent`を使用します。プラットフォーム固有の実装例については、[Braze SDKを通じたeコマースイベントのロギング]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events)を参照してください。
{% endalert %}

{% tabs %}
{% tab ecommerce.product_viewed %}

ユーザーが製品詳細ページを閲覧したときにトリガーします。このイベントは、Brazeカタログの[再入荷通知]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications)および[値下げ通知]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications)と互換性があります。

#### クライアントサイドの実装 {#client-side-implementation}

利用可能な場合はSDKのeコマースイベントAPIを使用してください。プラットフォーム固有の実装例については、[Braze SDKを通じたeコマースイベントのロギング]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events)を参照してください。

#### イベントプロパティ {#event-properties}

| プロパティ名 | データタイプ | 必須 | 説明 |
| -------------- | ---------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `product_id`   | String           | はい      | 一意の製品識別子（例：SKUまたはアイテムID）。 |
| `product_name` | String           | はい      | 製品の表示名。 |
| `variant_id`   | String           | はい      | 製品バリアント識別子（例：`shirt_medium_blue`）。 |
| `image_url`    | String           | いいえ       | 製品画像のURL。 |
| `product_url`  | String           | いいえ       | 製品ページへのURL。 |
| `price`        | Float            | はい      | 閲覧時のバリアント単価。 |
| `currency`     | String           | はい      | 3文字のISO 4217コード（例：`USD`または`EUR`）。 |
| `source`       | String           | はい      | イベントの発生元（例：`web`、`ios`、`android`）。 |
| `type`         | Array of strings | いいえ       | Brazeのカタログトリガー機能（再入荷および値下げアラート）を使用するために必要です。許可される値：`"price_drop"`、`"back_in_stock"` |
| `metadata`     | Object           | いいえ       | 柔軟なキーと値のペア（例：`category`や`brand`）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="イベントプロパティ" }

#### REST APIの例 {#rest-api-example}

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.product_viewed",
      "time": "2026-04-28T14:22:11Z",
      "properties": {
        "product_id": "SKU-RUN-4821",
        "product_name": "Ultraboost Running Shoe",
        "variant_id": "UB-BLK-11",
        "image_url": "https://cdn.example.com/shoes/ub-blk-11.jpg",
        "product_url": "https://www.example.com/products/ultraboost-running-shoe?variant=UB-BLK-11",
        "price": 189.99,
        "currency": "USD",
        "source": "web",
        "type": ["price_drop", "back_in_stock"],
        "metadata": {
          "category": "Running Shoes",
          "brand": "Shoe Brand"
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab ecommerce.cart_updated %}

ユーザーのカートの内容が変更されるたびにトリガーします。

#### クライアントサイドの実装

利用可能な場合はSDKのeコマースイベントAPIを使用してください。プラットフォーム固有の実装例については、[Braze SDKを通じたeコマースイベントのロギング]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events)を参照してください。

このイベントは2つの方法のいずれかで送信できます：

- **カート全体の置換：** `action`を省略するか、`action`を`replace`に設定します。`products`に絶対数量（カート内のバリアントごとの合計ユニット数）を含む完全なラインアイテムのセットを含めます。`total_value`を含める必要があります。
- **増分カート更新：** `action`を`add`または`remove`に設定します。変更されたラインアイテムのみを含めます。各`quantity`は、カート内の合計数量ではなく、追加または削除するユニット数です。`add`の場合、Brazeはライン数量を増やすか、新しいラインを追加します。`remove`の場合、Brazeはライン数量を減らし、数量が`0`に達するとラインを削除します。`total_value`は`add`と`remove`ではオプションです。

{% alert warning %}
特定の`cart_id`に対して、増分カート更新（`add`または`remove`）またはカート全体の置換（`action`なしまたは`replace`）のいずれかを使用してください。同じ`cart_id`に対して両方のアプローチを混在させることは推奨されず、Brazeでカート状態が不整合になる可能性があります。
{% endalert %}

このイベントからメッセージングをトリガーするには、キャンバスとキャンペーンで**カート更新イベントを実行**トリガーを使用します。このトリガーには、カートがショッピングファネルを進行するのを停止する特別な処理が含まれています。

{% alert tip %}
カートは、{% raw %}`{% shopping_cart %}`{% endraw %} Liquidタグを動作させるユーザープロファイル上のカートマッピングオブジェクトを作成します。カートは更新なしで30日後に期限切れになります。2つのユーザープロファイルがマージされた場合、Brazeは両方のカートを保持します。
{% endalert %}

#### イベントプロパティ

| プロパティ | データタイプ | 必須 | 説明 |
|-----------------|-----------|----------|-------------------------------------------------------------------------------------------------------------------------------|
| `cart_id`       | String    | はい      | カートの一意の識別子。ユーザーのカートマッピングのために、カート、チェックアウト、注文イベント間で共有されます。 |
| `action`        | String    | いいえ       | `add`（数量を増やすか新しいラインを追加）、`remove`（数量を減らし、`0`でラインを削除）、または`replace`（カート全体の置換、`action`を省略した場合と同じ）。 |
| `total_value`   | Float     | 条件付き | `action`が省略されているか`replace`の場合は必須。`action`が`add`または`remove`の場合はオプション。 |
| `subtotal_value`| Float     | いいえ       | カートの小計値（割引後、税/送料前）。 |
| `tax`           | Float     | いいえ       | カートに適用された合計税額。 |
| `shipping`      | Float     | いいえ       | カートの合計送料。 |
| `currency`      | String    | はい      | 3文字のISO 4217コード。 |
| `products`      | Array     | はい      | この更新のラインアイテム。カート全体の置換（`action`なしまたは`replace`）の場合、絶対数量を含む完全なカートを含めます。`add`または`remove`の場合、変更されたラインのみを含めます。製品プロパティを参照してください。 |
| `source`        | String    | はい      | イベントの発生元。 |
| `metadata`      | Object    | いいえ       | 追加のイベントレベルデータのための柔軟なキーと値のペア。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="イベントプロパティ" }

#### 製品プロパティ（`products[]`） {#product-properties-products}

| プロパティ | データタイプ | 必須 | 説明 |
|-----------------|-----------|----------|-------------------------------------------------|
| `product_id`    | String    | はい      | 一意の製品識別子。 |
| `product_name`  | String    | はい      | 製品の表示名。 |
| `variant_id`    | String    | はい      | バリアント識別子。 |
| `image_url`     | String    | いいえ       | 製品画像のURL。 |
| `product_url`   | String    | いいえ       | 製品ページへのURL。 |
| `quantity`      | Integer   | はい      | カート全体の置換（`action`なしまたは`replace`）の場合、このラインのカート内のユニット数。`add`または`remove`の場合、追加または削除するユニット数。 |
| `price`         | Float     | はい      | バリアント単価。 |
| `metadata`      | Object    | いいえ       | 柔軟なキーと値のペア（例：`color`や`size`）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="製品プロパティ（products[]）" }

{% comment %}

{% subtabs local %}
{% subtab Web %}

##### `add`

`add`は数量を増やすか、新しいラインを追加します。`quantity`プロパティは追加するユニット数です。

```javascript
braze.logCustomEvent("ecommerce.cart_updated", {
  cart_id: "cart_abc123",
  action: "add",
  currency: "USD",
  source: "web",
  products: [
    {
      product_id: "SKU-RUN-4821",
      product_name: "Ultraboost Running Shoe",
      variant_id: "UB-BLK-11",
      quantity: 1,
      price: 189.99,
    },
  ],
});
```
##### `remove`

`remove`は`quantity`の量だけ数量を減らします。数量が`0`に達するとラインが削除されます。

```javascript
braze.logCustomEvent("ecommerce.cart_updated", {
  cart_id: "cart_abc123",
  action: "remove",
  currency: "USD",
  source: "web",
  products: [
    {
      product_id: "SKU-SOC-1102",
      product_name: "Performance Running Socks",
      variant_id: "SOC-WHT-L",
      quantity: 1,
      price: 14.99,
    },
  ],
});
```

##### `replace`

`replace`（または`action`を省略）はカート全体を送信します。`total_value`は必須です。

```javascript
braze.logCustomEvent("ecommerce.cart_updated", {
  cart_id: "cart_abc123",
  action: "replace",
  total_value: 234.96,
  currency: "USD",
  source: "web",
  products: [
    {
      product_id: "SKU-RUN-4821",
      product_name: "Ultraboost Running Shoe",
      variant_id: "UB-BLK-11",
      image_url: "https://cdn.example.com/shoes/ub-blk-11.jpg",
      product_url: "https://www.example.com/products/ultraboost-running-shoe?variant=UB-BLK-11",
      quantity: 1,
      price: 189.99,
    },
    {
      product_id: "SKU-SOC-1102",
      product_name: "Performance Running Socks",
      variant_id: "SOC-WHT-L",
      image_url: "https://cdn.example.com/socks/soc-wht-l.jpg",
      product_url: "https://www.example.com/products/performance-running-socks?variant=SOC-WHT-L",
      quantity: 2,
      price: 14.99,
    },
  ],
});
```

{% endsubtab %}
{% subtab Android %}

##### Add

`add`は数量を増やすか、新しいラインを追加します。`quantity`プロパティは追加するユニット数です。

```text
Kotlin

// add — units to add
Braze.getInstance(context).logCustomEvent(
  "ecommerce.cart_updated",
  BrazeProperties(
    JSONObject()
      .put("cart_id", "cart_abc123")
      .put("action", "add")
      .put("currency", "USD")
      .put("source", "android")
      .put(
        "products",
        JSONArray().put(
          JSONObject()
            .put("product_id", "SKU-RUN-4821")
            .put("product_name", "Ultraboost Running Shoe")
            .put("variant_id", "UB-BLK-11")
            .put("quantity", 1)
            .put("price", 189.99),
        ),
      ),
  ),
)

JavaScript

// add — units to add
Braze.getInstance(context).logCustomEvent(
    "ecommerce.cart_updated",
    new BrazeProperties(new JSONObject()
        .put("cart_id", "cart_abc123")
        .put("action", "add")
        .put("currency", "USD")
        .put("source", "android")
        .put("products", new JSONArray()
            .put(new JSONObject()
                .put("product_id", "SKU-RUN-4821")
                .put("product_name", "Ultraboost Running Shoe")
                .put("variant_id", "UB-BLK-11")
                .put("quantity", 1)
                .put("price", 189.99)))));
```

##### Remove

`remove`は`quantity`の量だけ数量を減らします。数量が`0`に達するとラインが削除されます。

```text
Kotlin

// remove — units to remove
Braze.getInstance(context).logCustomEvent(
  "ecommerce.cart_updated",
  BrazeProperties(
    JSONObject()
      .put("cart_id", "cart_abc123")
      .put("action", "remove")
      .put("currency", "USD")
      .put("source", "android")
      .put(
        "products",
        JSONArray().put(
          JSONObject()
            .put("product_id", "SKU-SOC-1102")
            .put("product_name", "Performance Running Socks")
            .put("variant_id", "SOC-WHT-L")
            .put("quantity", 1)
            .put("price", 14.99),
        ),
      ),
  ),
)

JavaScript

// remove — units to remove
Braze.getInstance(context).logCustomEvent(
    "ecommerce.cart_updated",
    new BrazeProperties(new JSONObject()
        .put("cart_id", "cart_abc123")
        .put("action", "remove")
        .put("currency", "USD")
        .put("source", "android")
        .put("products", new JSONArray()
            .put(new JSONObject()
                .put("product_id", "SKU-SOC-1102")
                .put("product_name", "Performance Running Socks")
                .put("variant_id", "SOC-WHT-L")
                .put("quantity", 1)
                .put("price", 14.99)))));
```

##### Replace

`replace`（または`action`を省略）はカート全体を送信します。`total_value`は必須です。

```text
Kotlin

// replace — full cart; total_value required
Braze.getInstance(context).logCustomEvent(
  "ecommerce.cart_updated",
  BrazeProperties(
    JSONObject()
      .put("cart_id", "cart_abc123")
      .put("action", "replace")
      .put("total_value", 234.96)
      .put("currency", "USD")
      .put("source", "android")
      .put(
        "products",
        JSONArray()
          .put(
            JSONObject()
              .put("product_id", "SKU-RUN-4821")
              .put("product_name", "Ultraboost Running Shoe")
              .put("variant_id", "UB-BLK-11")
              .put("quantity", 1)
              .put("price", 189.99),
          )
          .put(
            JSONObject()
              .put("product_id", "SKU-SOC-1102")
              .put("product_name", "Performance Running Socks")
              .put("variant_id", "SOC-WHT-L")
              .put("quantity", 2)
              .put("price", 14.99),
          ),
      ),
  ),
)

JavaScript

// replace — full cart; total_value required
Braze.getInstance(context).logCustomEvent(
    "ecommerce.cart_updated",
    new BrazeProperties(new JSONObject()
        .put("cart_id", "cart_abc123")
        .put("action", "replace")
        .put("total_value", 234.96)
        .put("currency", "USD")
        .put("source", "android")
        .put("products", new JSONArray()
            .put(new JSONObject()
                .put("product_id", "SKU-RUN-4821")
                .put("product_name", "Ultraboost Running Shoe")
                .put("variant_id", "UB-BLK-11")
                .put("quantity", 1)
                .put("price", 189.99))
            .put(new JSONObject()
                .put("product_id", "SKU-SOC-1102")
                .put("product_name", "Performance Running Socks")
                .put("variant_id", "SOC-WHT-L")
                .put("quantity", 2)
                .put("price", 14.99)))));
```

{% endsubtab %}
{% subtab Swift %}

##### Add

`add`は数量を増やすか、新しいラインを追加します。`quantity`プロパティは追加するユニット数です。

```text
Swift

// add — units to add
AppDelegate.braze?.logCustomEvent(
  name: "ecommerce.cart_updated",
  properties: [
    "cart_id": "cart_abc123",
    "action": "add",
    "currency": "USD",
    "source": "ios",
    "products": [
      [
        "product_id": "SKU-RUN-4821",
        "product_name": "Ultraboost Running Shoe",
        "variant_id": "UB-BLK-11",
        "quantity": 1,
        "price": 189.99,
      ],
    ],
  ]
)

Objective-C

// add — units to add
[AppDelegate.braze logCustomEvent:@"ecommerce.cart_updated"
                       properties:@{
  @"cart_id": @"cart_abc123",
  @"action": @"add",
  @"currency": @"USD",
  @"source": @"ios",
  @"products": @[@{
    @"product_id": @"SKU-RUN-4821",
    @"product_name": @"Ultraboost Running Shoe",
    @"variant_id": @"UB-BLK-11",
    @"quantity": @1,
    @"price": @189.99,
  }],
}];
```

##### Remove

`remove`は`quantity`の量だけ数量を減らします。数量が`0`に達するとラインが削除されます。

```text
Swift

// remove — units to remove
AppDelegate.braze?.logCustomEvent(
  name: "ecommerce.cart_updated",
  properties: [
    "cart_id": "cart_abc123",
    "action": "remove",
    "currency": "USD",
    "source": "ios",
    "products": [
      [
        "product_id": "SKU-SOC-1102",
        "product_name": "Performance Running Socks",
        "variant_id": "SOC-WHT-L",
        "quantity": 1,
        "price": 14.99,
      ],
    ],
  ]
)

Objective-C

// remove — units to remove
[AppDelegate.braze logCustomEvent:@"ecommerce.cart_updated"
                       properties:@{
  @"cart_id": @"cart_abc123",
  @"action": @"remove",
  @"currency": @"USD",
  @"source": @"ios",
  @"products": @[@{
    @"product_id": @"SKU-SOC-1102",
    @"product_name": @"Performance Running Socks",
    @"variant_id": @"SOC-WHT-L",
    @"quantity": @1,
    @"price": @14.99,
  }],
}];
```

##### Replace

`replace`（または`action`を省略）はカート全体を送信します。`total_value`は必須です。

```text
Swift

// replace — full cart; total_value required
AppDelegate.braze?.logCustomEvent(
  name: "ecommerce.cart_updated",
  properties: [
    "cart_id": "cart_abc123",
    "action": "replace",
    "total_value": 234.96,
    "currency": "USD",
    "source": "ios",
    "products": [
      [
        "product_id": "SKU-RUN-4821",
        "product_name": "Ultraboost Running Shoe",
        "variant_id": "UB-BLK-11",
        "quantity": 1,
        "price": 189.99,
      ],
      [
        "product_id": "SKU-SOC-1102",
        "product_name": "Performance Running Socks",
        "variant_id": "SOC-WHT-L",
        "quantity": 2,
        "price": 14.99,
      ],
    ],
  ]
)

Objective-C

// replace — full cart; total_value required
[AppDelegate.braze logCustomEvent:@"ecommerce.cart_updated"
                       properties:@{
  @"cart_id": @"cart_abc123",
  @"action": @"replace",
  @"total_value": @234.96,
  @"currency": @"USD",
  @"source": @"ios",
  @"products": @[
    @{
      @"product_id": @"SKU-RUN-4821",
      @"product_name": @"Ultraboost Running Shoe",
      @"variant_id": @"UB-BLK-11",
      @"quantity": @1,
      @"price": @189.99,
    },
    @{
      @"product_id": @"SKU-SOC-1102",
      @"product_name": @"Performance Running Socks",
      @"variant_id": @"SOC-WHT-L",
      @"quantity": @2,
      @"price": @14.99,
    },
  ],
}];
```

{% endsubtab %}
{% subtab REST API %}

##### `add`

`add`は数量を増やすか、新しいラインを追加します。`quantity`プロパティは追加するユニット数です。

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.cart_updated",
      "time": "2026-04-28T14:25:33Z",
      "properties": {
        "cart_id": "cart_abc123",
        "action": "add",
        "currency": "USD",
        "source": "web",
        "products": [
          {
            "product_id": "SKU-RUN-4821",
            "product_name": "Ultraboost Running Shoe",
            "variant_id": "UB-BLK-11",
            "quantity": 1,
            "price": 189.99
          }
        ]
      }
    }
  ]
}
```

##### `remove`

`remove`は`quantity`の量だけ数量を減らします。数量が`0`に達するとラインが削除されます。

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.cart_updated",
      "time": "2026-04-28T14:26:10Z",
      "properties": {
        "cart_id": "cart_abc123",
        "action": "remove",
        "currency": "USD",
        "source": "web",
        "products": [
          {
            "product_id": "SKU-SOC-1102",
            "product_name": "Performance Running Socks",
            "variant_id": "SOC-WHT-L",
            "quantity": 1,
            "price": 14.99
          }
        ]
      }
    }
  ]
}
```

##### `replace`

`replace`（または`action`を省略）はカート全体を送信します。`total_value`は必須です。

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.cart_updated",
      "time": "2026-04-28T14:27:00Z",
      "properties": {
        "cart_id": "cart_abc123",
        "action": "replace",
        "total_value": 234.96,
        "subtotal_value": 219.97,
        "tax": 9.0,
        "shipping": 5.99,
        "currency": "USD",
        "products": [
          {
            "product_id": "SKU-RUN-4821",
            "product_name": "Ultraboost Running Shoe",
            "variant_id": "UB-BLK-11",
            "image_url": "https://cdn.example.com/shoes/ub-blk-11.jpg",
            "product_url": "https://www.example.com/products/ultraboost-running-shoe?variant=UB-BLK-11",
            "quantity": 1,
            "price": 189.99,
            "metadata": {
              "color": "Core Black",
              "size": "11"
            }
          },
          {
            "product_id": "SKU-SOC-1102",
            "product_name": "Performance Running Socks",
            "variant_id": "SOC-WHT-L",
            "image_url": "https://cdn.example.com/socks/soc-wht-l.jpg",
            "product_url": "https://www.example.com/products/performance-running-socks?variant=SOC-WHT-L",
            "quantity": 2,
            "price": 14.99,
            "metadata": {
              "color": "White",
              "size": "L"
            }
          }
        ],
        "source": "web",
        "metadata": {
          "cart_source": "product_page_atc_button"
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endcomment %}

{% endtab %}
{% tab ecommerce.checkout_started %}

ユーザーがチェックアウトフローを開始したとき（例：「チェックアウト」を選択した場合やチェックアウトページに到達した場合）にトリガーします。

#### クライアントサイドの実装

利用可能な場合はSDKのeコマースイベントAPIを使用してください。プラットフォーム固有の実装例については、[Braze SDKを通じたeコマースイベントのロギング]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events)を参照してください。

#### イベントプロパティ

| プロパティ | タイプ | 必須 | 説明 |
|----------------|---------|----------|------------------------------------------------------------------------------------------------------------------|
| checkout_id    | String  | はい      | チェックアウトセッションの一意の識別子。 |
| cart_id        | String  | いいえ       | カート識別子。ユーザーのカートマッピングのために、カート、チェックアウト、注文イベント間で共有されます。 |
| total_value    | Float   | はい      | チェックアウトの合計金額。 |
| subtotal_value | Float   | いいえ       | 小計値（割引後、税/送料前）。 |
| tax            | Float   | いいえ       | チェックアウトに適用された合計税額。 |
| shipping       | Float   | いいえ       | 合計送料。 |
| currency       | String  | はい      | 3文字のISO 4217コード。 |
| products       | Array   | はい      | チェックアウトされるアイテム。製品プロパティのサブテーブルを参照してください。 |
| source         | String  | はい      | イベントの発生元。 |
| metadata       | Object  | いいえ       | 柔軟なキーと値のペア。認識されるサブプロパティ：`checkout_url`（String） |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="イベントプロパティ" }

#### 製品プロパティ（`products[]`）

| プロパティ | データタイプ | 必須 | 説明 |
|----------------|-----------|----------|----------------------------------------------------------|
| `product_id`   | String    | はい      | 一意の製品識別子。 |
| `product_name` | String    | はい      | 製品の表示名。 |
| `variant_id`   | String    | はい      | バリアント識別子。 |
| `image_url`    | String    | いいえ       | 製品画像のURL。 |
| `product_url`  | String    | いいえ       | 製品ページへのURL。 |
| `quantity`     | Integer   | はい      | カート内のユニット数。 |
| `price`        | Float     | はい      | バリアント単価。 |
| `metadata`     | Object    | いいえ       | 柔軟なキーと値のペア（例：color、size）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="製品プロパティ（products[]）" }

#### REST APIの例

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.checkout_started",
      "time": "2026-04-28T14:30:05Z",
      "properties": {
        "checkout_id": "chk_88291",
        "cart_id": "cart_abc123",
        "total_value": 234.96,
        "subtotal_value": 219.97,
        "tax": 9.0,
        "shipping": 5.99,
        "currency": "USD",
        "products": [
          {
            "product_id": "SKU-RUN-4821",
            "product_name": "Ultraboost Running Shoe",
            "variant_id": "UB-BLK-11",
            "image_url": "https://cdn.example.com/shoes/ub-blk-11.jpg",
            "product_url": "https://www.example.com/products/ultraboost-running-shoe?variant=UB-BLK-11",
            "quantity": 1,
            "price": 189.99,
            "metadata": {
              "color": "Core Black",
              "size": "11"
            }
          },
          {
            "product_id": "SKU-SOC-1102",
            "product_name": "Performance Running Socks",
            "variant_id": "SOC-WHT-L",
            "image_url": "https://cdn.example.com/socks/soc-wht-l.jpg",
            "product_url": "https://www.example.com/products/performance-running-socks?variant=SOC-WHT-L",
            "quantity": 2,
            "price": 14.99,
            "metadata": {
              "color": "White",
              "size": "L"
            }
          }
        ],
        "source": "web",
        "metadata": {
          "checkout_url": "https://www.example.com/checkout/chk_88291",
          "checkout_type": "express"
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab ecommerce.order_placed %}

注文が正常に完了した場合、または支払いが確認されたときにトリガーします。

#### クライアントサイドの実装

利用可能な場合はSDKのeコマースイベントAPIを使用してください。プラットフォーム固有の実装例については、[Braze SDKを通じたeコマースイベントのロギング]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events)を参照してください。

{% alert important %}
このイベントは主要な収益ドライバーです。ユーザープロファイル上で`total_revenue`を`total_value`の値だけ増加させ、`total_orders`を1増加させます。
{% endalert %}

#### イベントプロパティ

| プロパティ | データタイプ | 必須 | 説明 |
|-----------------|-----------|----------|-----------------------------------------------------------------------------------------------|
| `order_id`      | String    | はい      | 注文の一意の識別子。 |
| `cart_id`       | String    | いいえ       | カート識別子。ユーザーのカートマッピングのために、カート、チェックアウト、注文イベント間で共有されます。 |
| `total_value`   | Float     | はい      | 注文の合計金額。 |
| `subtotal_value`| Float     | いいえ       | 小計値（割引後、税/送料前）。 |
| `tax`           | Float     | いいえ       | 注文に適用された合計税額。 |
| `shipping`      | Float     | いいえ       | 合計送料。 |
| `currency`      | String    | はい      | 3文字のISO 4217コード。 |
| `total_discounts`| Float    | いいえ       | 注文に適用された割引の合計額。 |
| `discounts`     | Array     | いいえ       | 適用された割引の詳細リスト。 |
| `products`      | Array     | はい      | 注文内のアイテム。製品プロパティのサブテーブルを参照してください。 |
| `source`        | String    | はい      | イベントの発生元。 |
| `metadata`      | Object    | いいえ       | 柔軟なキーと値のペア。認識されるサブプロパティ：`order_status_url`（String） |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="イベントプロパティ" }

#### 製品プロパティ（`products[]`）

| プロパティ | データタイプ | 必須 | 説明 |
|-----------------|-----------|----------|---------------------------------------------|
| `product_id`    | String    | はい      | 一意の製品識別子。 |
| `product_name`  | String    | はい      | 製品の表示名。 |
| `variant_id`    | String    | はい      | バリアント識別子。 |
| `image_url`     | String    | いいえ       | 製品画像のURL。 |
| `product_url`   | String    | いいえ       | 製品ページへのURL。 |
| `quantity`      | Integer   | はい      | カート内のユニット数。 |
| `price`         | Float     | はい      | バリアント単価。 |
| `metadata`      | Object    | いいえ       | 柔軟なキーと値のペア（例：`color`や`size`）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="製品プロパティ（products[]）" }

#### REST APIの例

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.order_placed",
      "time": "2026-04-28T14:35:42Z",
      "properties": {
        "order_id": "ord_77821",
        "cart_id": "cart_abc123",
        "total_value": 224.96,
        "subtotal_value": 209.97,
        "tax": 9.0,
        "shipping": 5.99,
        "currency": "USD",
        "total_discounts": 10.0,
        "discounts": [
          {
            "code": "SPRING10",
            "amount": 10.0,
            "type": "percentage"
          }
        ],
        "products": [
          {
            "product_id": "SKU-RUN-4821",
            "product_name": "Ultraboost Running Shoe",
            "variant_id": "UB-BLK-11",
            "image_url": "https://cdn.example.com/shoes/ub-blk-11.jpg",
            "product_url": "https://www.example.com/products/ultraboost-running-shoe?variant=UB-BLK-11",
            "quantity": 1,
            "price": 189.99,
            "metadata": {
              "color": "Core Black",
              "size": "11"
            }
          },
          {
            "product_id": "SKU-SOC-1102",
            "product_name": "Performance Running Socks",
            "variant_id": "SOC-WHT-L",
            "image_url": "https://cdn.example.com/socks/soc-wht-l.jpg",
            "product_url": "https://www.example.com/products/performance-running-socks?variant=SOC-WHT-L",
            "quantity": 2,
            "price": 14.99,
            "metadata": {
              "color": "White",
              "size": "L"
            }
          }
        ],
        "source": "web",
        "metadata": {
          "order_status_url": "https://www.example.com/orders/ord_77821/status"
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab ecommerce.order_cancelled %}

注文がキャンセルされたときにトリガーします。

#### クライアントサイドの実装

`logCustomEvent`を使用してください。プラットフォーム固有の実装例については、[Braze SDKを通じたeコマースイベントのロギング]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events)を参照してください。

{% alert important %}
このイベントはユーザープロファイル上の`total_orders`を1減少させます。`total_revenue`には影響しません。収益を調整するには`order_refunded`を使用してください。
{% endalert %}

#### イベントプロパティ

| プロパティ | タイプ | 必須 | 説明 |
|------------------|---------|----------|--------------------------------------------------------------------------------------------------|
| `order_id`       | String  | はい      | 注文の一意の識別子。 |
| `total_value`    | Float   | はい      | キャンセルされる注文の合計金額。0以上である必要があります。絶対値を送信してください。Brazeが減少を処理します。 |
| `subtotal_value` | Float   | いいえ       | 小計値（割引後、税/送料前）。 |
| `tax`            | Float   | いいえ       | 注文に適用された合計税額。 |
| `shipping`       | Float   | いいえ       | 合計送料。 |
| `currency`       | String  | はい      | 3文字のISO 4217コード。 |
| `total_discounts`| Float   | いいえ       | 注文に適用された割引の合計額。 |
| `discounts`      | Array   | いいえ       | 適用された割引の詳細リスト。 |
| `cancel_reason`  | String  | はい      | 注文がキャンセルされた理由。 |
| `products`       | Array   | はい      | キャンセルされた注文内のアイテム。製品プロパティのサブテーブルを参照してください。 |
| `source`         | String  | はい      | イベントの発生元。 |
| `metadata`       | Object  | いいえ       | 柔軟なキーと値のペア。認識されるサブプロパティ：`order_status_url`（String） |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="イベントプロパティ" }

#### 製品プロパティ（`products[]`）

| プロパティ | データタイプ | 必須 | 説明 |
|----------------|-----------|----------|-----------------------------------------------|
| `product_id`   | String    | はい      | 一意の製品識別子。 |
| `product_name` | String    | はい      | 製品の表示名。 |
| `variant_id`   | String    | はい      | バリアント識別子。 |
| `image_url`    | String    | いいえ       | 製品画像のURL。 |
| `product_url`  | String    | いいえ       | 製品ページへのURL。 |
| `quantity`     | Integer   | はい      | カート内のユニット数。 |
| `price`        | Float     | はい      | バリアント単価。 |
| `metadata`     | Object    | いいえ       | 柔軟なキーと値のペア（例：`color`や`size`）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="製品プロパティ（products[]）" }

#### REST APIの例

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.order_cancelled",
      "time": "2026-04-28T16:10:00Z",
      "properties": {
        "order_id": "ord_77821",
        "total_value": 224.96,
        "subtotal_value": 209.97,
        "tax": 9.0,
        "shipping": 5.99,
        "currency": "USD",
        "total_discounts": 10.0,
        "cancel_reason": "customer_request",
        "products": [
          {
            "product_id": "SKU-RUN-4821",
            "product_name": "Ultraboost Running Shoe",
            "variant_id": "UB-BLK-11",
            "quantity": 1,
            "price": 189.99,
            "metadata": {
              "color": "Core Black",
              "size": "11"
            }
          },
          {
            "product_id": "SKU-SOC-1102",
            "product_name": "Performance Running Socks",
            "variant_id": "SOC-WHT-L",
            "quantity": 2,
            "price": 14.99,
            "metadata": {
              "color": "White",
              "size": "L"
            }
          }
        ],
        "source": "web",
        "metadata": {
          "order_status_url": "https://www.example.com/orders/ord_77821/status"
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab ecommerce.order_refunded %}

全額または一部の返金が発行されたときにトリガーします。

#### クライアントサイドの実装

`logCustomEvent`を使用してください。プラットフォーム固有の実装例については、[Braze SDKを通じたeコマースイベントのロギング]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events)を参照してください。

{% alert important %}
このイベントはユーザープロファイル上の`total_revenue`を`total_value`の値だけ減少させ、`total_refunds`を増加させます。一部返金の場合、`total_value`を元の注文合計ではなく、返金額のみに設定してください。
{% endalert %}

#### イベントプロパティ

| プロパティ | データタイプ | 必須 | 説明 |
|-------------------|-----------|----------|------------------------------------------------------------------------------------------------------|
| `order_id`        | String    | はい      | 元の注文の一意の識別子。 |
| `total_value`     | Float     | はい      | 返金の合計金額。0以上である必要があります。絶対値を送信してください。Brazeがtotal_refundsへの増加を処理します。 |
| `currency`        | String    | はい      | 3文字のISO 4217コード。 |
| `total_discounts` | Float     | いいえ       | 元々適用されていた割引の合計額。 |
| `discounts`       | Array     | いいえ       | 割引の詳細リスト。 |
| `products`        | Array     | はい      | 返金されるアイテム。製品プロパティのサブテーブルを参照してください。 |
| `source`          | String    | はい      | イベントの発生元。 |
| `metadata`        | Object    | いいえ       | 柔軟なキーと値のペア。認識されるサブプロパティ：`order_status_url`（String）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="イベントプロパティ" }

#### 製品プロパティ（`products[]`）

| プロパティ | データタイプ | 必須 | 説明 |
|-----------------|-----------|----------|-------------------------------------------------------|
| `product_id`    | String    | はい      | 一意の製品識別子。 |
| `product_name`  | String    | はい      | 製品の表示名。 |
| `variant_id`    | String    | はい      | バリアント識別子。 |
| `image_url`     | String    | いいえ       | 製品画像のURL。 |
| `product_url`   | String    | いいえ       | 製品ページへのURL。 |
| `quantity`      | Integer   | はい      | カート内のユニット数。 |
| `price`         | Float     | はい      | バリアント単価。 |
| `metadata`      | Object    | いいえ       | 柔軟なキーと値のペア（例：`color`や`size`）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="製品プロパティ（products[]）" }

#### REST APIの例 {#rest-api-examples}

{% subtabs %}
{% subtab 全額返金 %}

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.order_refunded",
      "time": "2026-04-29T10:05:00Z",
      "properties": {
        "order_id": "ord_77821",
        "total_value": 189.99,
        "currency": "USD",
        "total_discounts": 0,
        "products": [
          {
            "product_id": "SKU-RUN-4821",
            "product_name": "Ultraboost Running Shoe",
            "variant_id": "UB-BLK-11",
            "quantity": 1,
            "price": 189.99,
            "metadata": {
              "color": "Core Black",
              "size": "11",
              "refund_reason": "size_mismatch"
            }
          }
        ],
        "source": "web",
        "metadata": {
          "order_status_url": "https://www.example.com/orders/ord_77821/status"
        }
      }
    }
  ]
}
```
{% endsubtab %}
{% subtab 一部返金 %}

```json
{
  "events": [
    {
      "external_id": "user_98765",
      "name": "ecommerce.order_refunded",
      "time": "2026-05-02T11:08:30Z",
      "properties": {
        "order_id": "ORD-20260428-7891",
        "total_value": 29.98,
        "currency": "USD",
        "products": [
          {
            "product_id": "SKU-SOC-1102",
            "product_name": "Performance Running Socks",
            "variant_id": "SOC-WHT-L",
            "image_url": "https://cdn.example.com/socks/soc-wht-l.jpg",
            "product_url": "https://www.example.com/products/performance-running-socks?variant=SOC-WHT-L",
            "quantity": 2,
            "price": 14.99,
            "metadata": {
              "color": "White",
              "size": "L"
            }
          }
        ],
        "source": "web",
        "metadata": {
          "refund_method": "store_credit",
          "initiated_by": "customer"
        }
      }
    }
  ]
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### eコマースイベントの後処理 {#ecommerce-event-post-processing}

eコマースイベントを送信すると、Brazeはそのイベント名に対して期待されるスキーマに対してバリデーションを行います。

以下の表は、バリデーションに合格した場合にBrazeが各イベントに対して自動的に行う処理をまとめたものです。バリデーションに失敗した場合の動作については、[イベントのバリデーションとトラブルシューティング](#event-validation-and-troubleshooting)を参照してください。

| イベント | Brazeが自動的に行う処理 |
|------------------------------|-------------------------------------------------------------------------------------------------------------------|
| `ecommerce.order_placed`     | ユーザープロファイル上の**合計収益**を`total_value`だけ増加させ、**合計注文数**を1増加させます。 |
| `ecommerce.order_cancelled`  | **合計注文数**を1減少させます。 |
| `ecommerce.order_refunded`   | **合計収益**を`total_value`だけ減少させ、**合計返金額**を増加させます。 |
| `ecommerce.cart_updated`     | ユーザープロファイル上のカートマッピングオブジェクトを作成または更新します（カート全体のペイロード、またはオプションの`action`：`add`、`remove`、`replace`による増分カート更新）。カートは更新なしで30日後に期限切れになります。 |
| `ecommerce.product_viewed`   | ユーザープロファイルの変更はありません。セグメンテーション、トリガー、およびBrazeAI<sup>TM</sup>機能（アイテムレコメンデーションなど）で利用可能です。 |
| `ecommerce.checkout_started` | ユーザープロファイルの変更はありません。セグメンテーションとトリガー（例：チェックアウト放棄フロー）で利用可能です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="eコマースイベントの後処理" }

{% alert important %}
USD以外の通貨値は、イベントが報告された日の為替レートを使用して自動的にUSDに変換されます。すでにUSDで報告している場合は、意図しない変換を避けるために通貨として`USD`をハードコードしてください。
{% endalert %}

## 実装の詳細 {#implementation-details}

### データポイントと課金 {#data-points-and-billing}

eコマースイベントは[データポイント]({{site.baseurl}}/user_guide/data/infrastructure/data_points)を消費しません。データポイント使用量に影響を与えることなくログに記録できます。

### イベントサイズの制限 {#event-size-limit}

`/users/track`に送信されるイベントプロパティは、イベントあたり102,400バイト（100 KB）が上限です。トリガーされたキャンペーンおよびキャンバスメッセージの場合、[`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)および[`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)に送信される`trigger_properties`には、デフォルトで51,200バイト（50 KB）というより厳しい制限があります。

ベストプラクティスとして、トリガー、パーソナライゼーション、またはイベントのアトリビューションに必要な製品情報のみを送信してください。説明文、完全なバリアントリスト、在庫、代替画像などのより詳細な製品情報は、Brazeカタログに保存してください。メッセージ送信時には`product_id`または`variant_id`でこれらの詳細を参照します。`metadata`オブジェクトは、メッセージングで使用する注文または製品固有のコンテキストに対して選択的に使用してください。

### 通貨の処理 {#currency-handling}

Brazeは、USD以外の通貨値を、イベントが報告された日の為替レートを使用して自動的にUSDに変換します。この変換された値が収益指標に表示されます。

{% alert tip %}
USDのみで運用している場合は、不要な変換を避けるために、すべてのイベントで`"currency": "USD"`をハードコードしてください。
{% endalert %}

### sourceフィールド {#source-field}

sourceプロパティは、イベントの発生元を識別する必須の文字列です。例えば、`shopify`、`in-store POS`、`custom_api`などです。これにより、Currentsエクスポートでデータを分析したり、バリデーションの問題をデバッグしたりする際に、統合ソースを区別できます。

### メタデータの柔軟性 {#metadata-flexibility}

イベントレベルと製品レベルの両方のメタデータオブジェクトは任意のキーと値のペアを受け入れるため、コアスキーマを変更せずにカスタムディメンションを付加できます。一般的な例としては、`order_status_url`、`gift_wrapped`、`loyalty_points_earned`、`warehouse_id`などがあります。これらのプロパティは、Liquidパーソナライゼーション、Currentsエクスポート、および[セグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension)を通じたセグメンテーションで利用できます。

{% alert important %}
推奨イベントは厳密なスキーマを使用します。そのため、プロパティのトップレベルにカスタムプロパティを追加するとバリデーションに失敗します。すべてのカスタムプロパティは、イベントレベルの`metadata`オブジェクトまたは`products[]`内の製品レベルの`metadata`オブジェクトに配置してください。これらはトップレベルのフィールドと同様に、Liquid、Currents、セグメンテーションで利用できます。
{% endalert %}

## イベントのバリデーションとトラブルシューティング {#event-validation-and-troubleshooting}

`/users/track`またはBraze SDKを通じて推奨eコマースイベントを送信すると、Brazeは推奨イベントの処理中にペイロードをイベントのJSONスキーマに対してバリデーションします。バリデーションは、推奨イベントと名前が完全に一致するすべてのイベント（例：`ecommerce.order_placed`や`ecommerce.cart_updated`）に対して自動的に実行されます。

### バリデーション内容 {#what-we-validate}

eコマース推奨イベントと名前が一致する各イベントについて、Brazeは以下をチェックします。

| チェック項目                | 例                                                                                                                           |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------|
| イベント名                 | 正確に一致する必要があります。例えば、`ecommerce.cart_updated`が正しく、`ecommerce.Cart_Updated`、`cartupdated`、`cart_updated`は不正です。 |
| 必須プロパティの存在        | `order_placed`には`order_id`、`total_value`、`currency`、`products`、`source`が必要です。                                   |
| 正しいデータ型              | `total_value`は数値、`currency`は文字列、`products`は配列である必要があります。                                               |
| トップレベルの余分なプロパティがないこと | プロパティ配下のカスタムフィールドは失敗の原因になります。代わりに`metadata`オブジェクトを使用してください。                         |
| 値の制約                   | 金額フィールドは`0`以上である必要があります。`currency`は有効なISO 4217文字列である必要があります。                                |
| 製品ごとのフィールド        | `products[]`の各アイテムには`product_id`、`product_name`、`variant_id`、`quantity`、`price`が含まれている必要があります。         |
{: .reset-td-br-1 .reset-td-br-2 aria-label="バリデーション内容" }

### バリデーションを行う理由 {#why-we-validate}

eコマースイベントは、収益トラッキング、{% raw %}`{% shopping_cart %}`{% endraw %} Liquidタグ、放棄カートトリガー、レポートなど、一貫性のある予測可能なデータに依存する機能を支えています。ペイロードがスキーマから逸脱すると、これらの機能はサイレントな不正確さ（誤った収益合計、カートの欠落、壊れたトリガー）を生み出します。バリデーションは、下流の機能が予測どおりに動作するよう、事前に契約を強制します。

### バリデーション成功時 {#when-validation-passes}

イベントは、関連するすべての後処理を伴うeコマース推奨イベントとして処理されます。各イベントタイプによってトリガーされる動作の完全なリストについては、[eコマース推奨イベント](#event-schemas)を参照してください。

#### 成功したイベントの確認 {#verify-a-successful-event}

イベントを送信した後、以下のいずれかを使用して、イベントが受け入れられ正しく処理されたことを確認できます。

- [イベントユーザーログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log)：ダッシュボードでユーザーのプロファイルを開き、アクティビティを確認します。推奨イベントは完全なプロパティペイロードとともに表示されるため、イベントが到着し、送信した値と一致していることを確認できます。
- [カスタムイベントレポート]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report)：**Analytics** > **Custom Events Report**に移動して、各推奨イベントの経時的な集計カウントを確認します。これは、インテグレーションがライブになった際に本番トラフィックが期待どおりに流れていることを確認するのに役立ちます。
- [テストユーザー]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups?utm_source=operator_user&utm_medium=dashboard#adding-test-users)：開発ワークスペースでユーザーをテストユーザーとしてマークし、そのユーザーに対してインテグレーションからイベントをトリガーします。テストユーザーはダッシュボードでフラグが付けられるため、エンドツーエンドの動作を分離して検査しやすくなります。

### バリデーション失敗時 {#when-validation-fails}

イベントは推奨イベントとして処理されません。具体的には以下のとおりです。

- **イベントは完全にドロップされます。**無効な推奨eコマースイベントはユーザープロファイルに記録されず、Currentsに表示されず、セグメンテーションにも使用できません。
- 以下を含む下流の推奨イベント機能は実行されません。
  - 収益トラッキング（収益レポート、`total_revenue`などのユーザー計算フィールド）
  - ユーザープロファイル上のカートオブジェクトの更新
  - キャンバスやキャンペーンにおける「カート更新イベントの実行」または「注文完了」トリガー

エラーの報告方法は取り込みパスによって異なります。

- **REST API（`/users/track`）：**各無効なイベントはレスポンスのエラー配列で報告されます。各エントリには、どのイベントが失敗したか（インデックス）と理由（タイプ）が記載されます。トップレベルのメッセージフィールドは`"success"`と表示されますが、これはリクエストがBrazeに到達したことを意味するだけで、すべてのイベントが有効であったことを意味するわけではありません。レスポンスのエラー配列を必ず確認してください。
- **Braze SDK：**SDK呼び出しは即座に返され、バリデーションはバックグラウンドで実行されるため、エラーはアプリに返されません。eコマースイベントのバリデーション失敗を確認するには、失敗サマリーメールを監視してください（[失敗の確認](#find-failures)を参照）。

#### APIエラーレスポンスの例 {#example-api-error-response}

`/users/track`エンドポイントは、どのプロパティが失敗したか、およびその理由を示すフィールドレベルのエラーを返します。トップレベルの`message`はイベントがパイプラインに受け入れられたため`"success"`を返す場合がありますが、`errors`配列がスキーマバリデーションに失敗したフィールドを示します。以下のエラーレスポンスの例を参照してください。

```json
{
 "message": "success",
 "errors": [{ "index": 0, "input_array": "purchases", "type": "'currency' must be an ISO 4217 currency" }]
}
```

失敗は内部的にも分類され、失敗サマリーメール用に集計されます。

| 失敗タイプ                | 意味                                              | 例                                                             |
|------------------------|---------------------------------------------------|----------------------------------------------------------------|
| `missing_property`     | 必須フィールドが存在しません。                       | `order_placed`が`order_id`なしで送信された場合。                  |
| `extra_property`       | スキーマで定義されていないフィールドが追加されました。 | カスタムの`gift_wrapped`フィールドが`metadata`内ではなく`properties`のトップに配置された場合。 |
| `unexpected_data_type` | フィールドの型が正しくありません。                    | `total_value: "29.99"`（文字列）が`29.99`（数値）の代わりに送信された場合。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="APIエラーレスポンスの例" }

{% alert note %}
推奨イベントと名前が完全に一致しないイベント名（例：`ecommerce.OrderPlaced`）はバリデーションを完全にスキップし、通常のカスタムイベントとして記録されます。これらはCurrentsやセグメンテーションに送信した名前で表示されますが、推奨イベントの処理は行われず、レスポンスに`errors`エントリも含まれません。
{% endalert %}

#### 失敗の確認 {#find-failures}

Brazeは、手動ですべてのイベントを監視することなくインテグレーションの問題を特定して修正できるよう、推奨イベントのバリデーション失敗のサマリーをワークスペース管理者にメールで送信します。

サマリーメールには以下が含まれます。

- **合計エラー数：**レポート期間のエラーカウント。
- **イベント別エラー：**各推奨イベントタイプ（例：`ecommerce.cart_updated`や`ecommerce.order_placed`）で失敗したイベント数の内訳。これを使用して、インテグレーションのどのイベントに最初に対応すべきかを特定できます。
- **ソース別エラー：**APIとSDKの分割。これにより、どのインテグレーションが失敗を生成しているかを特定できます。

これらのメールを受信していない場合や受信者リストを確認したい場合は、Brazeアカウントチームにお問い合わせください。

#### 失敗の診断と修正 {#diagnose-and-fix-failures}

失敗サマリーメールを受信した場合：

1. **失敗しているイベントとソースを特定します。**メールはイベント名とインテグレーションソース（`sdk`対`rest_api`）ごとに失敗を分けているため、どのインテグレーションに修正が必要かを特定できます。同じイベントを送信する複数のソースがある場合（例：ストアフロントSDKとバックエンドWebhookの両方が`cart_updated`を送信している場合）、それぞれ独立して対処してください。
2. **ペイロードを[イベントスキーマ](#event-schemas)のスキーマと比較します。**ほとんどの失敗は以下の3つのパターンのいずれかに該当します。
   - `missing_property`：必須フィールドが存在しません。解決するには、必須フィールドを追加してください。
   - `extra_property`：カスタムフィールドが`properties`のトップレベルにあります。解決するには、カスタムフィールドを`metadata`（イベントレベル）または`products[].metadata`（製品ごと）内に移動してください。
   - `unexpected_data_type`：値の型が正しくありません（例：`total_value`が文字列として送信された場合）。解決するには、送信前に値を変換してください。
3. **修正したペイロードを本番環境にロールアウトする前に、開発ワークスペースでテストします。**テストユーザーに対して既知のテストイベントを送信し、そのユーザーのプロファイルで期待される推奨イベントの動作を確認します（例：カートオブジェクトの更新、収益の増加、放棄カートトリガーの発火）。
4. **次の失敗メールを監視して**、そのイベント、ソース、タイプの失敗カウントがゼロに減少したことを確認します。

イベントごとの完全なプロパティ要件については、[イベントスキーマ](#event-schemas)を参照してください。