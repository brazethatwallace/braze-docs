---
nav_title: eコマース推奨イベント
article_title: e コマースの推奨イベント
page_type: reference
alias: /ecommerce_events/
toc_headers: h2
description: "この参照記事では、e コマース推奨のイベントとプロパティ、その使用方法、セグメンテーション、関連する分析の表示場所などについて説明します。"
---

# e コマースの推奨イベント {#ecommerce-recommended-events}

> このページでは、e コマース推奨のイベントとプロパティについて説明します。これらのイベントは、マーケターが効果的なメッセージング (カート放棄のターゲット設定など) をトリガーするために必要な主要な購買行動をキャプチャするために作成されています。

{% alert important %}
e コマースの推奨イベントは現在、早期アクセス段階です。早期アクセスにご興味のある方は、Braze カスタマーサクセスマネージャーまでお問い合わせください。<br><br>新しい [Shopify コネクタ]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector)を使用している場合、これらの推奨イベントは統合を通じて自動的に利用可能になります。
{% endalert %}

Braze は、データプランニングには時間がかかることを認識しています。お客様の開発チームに周知し、これらのイベントの送信を今すぐ開始することをお勧めします。e コマース推奨イベントですぐに利用できない機能もあるかもしれませんが、e コマース機能を強化する新製品が2025年中に順次リリースされる予定です。

## e コマースの推奨イベントのタイプ {#types-of-ecommerce-recommended-events}

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

レポートされた米ドル以外の通貨は、レポート日の為替レートに基づき、Braze では米ドルで表示されます。通貨換算を防ぐには、通貨を米ドルにハードコードしてください。

{% tabs %}
{% tab ecommerce.product_viewed %}

顧客が商品詳細ページを閲覧した時点でトリガーされる製品閲覧イベントを使用できます。

#### プロパティ {#properties}

| プロパティ名 | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `product_id` | はい | 文字列 | 閲覧された製品の一意の識別子。<br> Shopify 以外の顧客の場合、これは SKU のようなカタログアイテム ID に設定した値になります。 |
| `product_name` | はい | 文字列 | 閲覧された商品名。 |
| `variant_id` | はい | 文字列 | 製品バリアントの一意の識別子。例: `shirt_medium_blue` |
| `image_url` | いいえ | 文字列 | 商品画像の URL。 |
| `product_url` | いいえ | 文字列 | 詳細情報がある製品ページの URL。 |
| `price` | はい | フロート | 閲覧時の製品のバリアント単価。 |
| `currency` | はい | 文字列 | 製品価格の表示通貨 (「USD」や「EUR」など)。[ISO 4217 フォーマット](https://www.iso.org/iso-4217-currency-codes.html)です。 |
| `source` | はい | 文字列 | イベントの派生元ソース (Shopify の場合はストアフロント)。 |
| `type` | いいえ | オブジェクト | [再入荷通知]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/)および[値下げ通知]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications/)と連携します。 |
| `metadata` | いいえ | オブジェクト | |
| `sku` | いいえ | 文字列 | (Shopify のみ) Shopify SKU。カタログ ID フィールドとして設定できます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### オブジェクトの例 {#example-objects}

{% subtabs %}
{% subtab Web SDK %}

{% sdk_min_versions web:6.8.0 %}

新しい SDK バージョンでは、`logEcommerceEvent()` を呼び出します:

```javascript
braze.logEcommerceEvent({
    "name": "ecommerce.product_viewed",
    "properties": {
        "product_id": "4111176",
        "product_name": "Torchie runners",
        "variant_id": "4111176700",
        "image_url": "https://braze-apparel.com/images/products/large/torchie-runners.jpg",
        "product_url": "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/",
        "price": 85,
        "currency": "GBP",
        "source": "https://braze-apparel.com/",
        "metadata": {
            "sku": "",
            "color": "ORANGE",
            "size": "6",
            "brand": "Braze"
        }
    }
});
```

レガシー SDK バージョンでは、`logCustomEvent()` を呼び出します:

```javascript
braze.logCustomEvent("ecommerce.product_viewed", {
    "product_id": "4111176",
    "product_name": "Torchie runners",
    "variant_id": "4111176700",
    "image_url": "https://braze-apparel.com/images/products/large/torchie-runners.jpg",
    "product_url": "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/",
    "price": 85,
    "currency": "GBP",
    "source": "https://braze-apparel.com/",
    "metadata": {
        "sku": "",
        "color": "ORANGE",
        "size": "6",
        "brand": "Braze"
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
BrazeProperties properties = new BrazeProperties()
    .addProperty("product_id", "4111176")
    .addProperty("product_name", "Torchie runners")
    .addProperty("variant_id", "4111176700")
    .addProperty("image_url", "https://braze-apparel.com/images/products/large/torchie-runners.jpg")
    .addProperty("product_url", "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/")
    .addProperty("price", 85)
    .addProperty("currency", "GBP")
    .addProperty("source", "https://braze-apparel.com/")
    .addProperty("metadata", new JSONObject()
        .put("sku", "")
        .put("color", "ORANGE")
        .put("size", "6")
        .put("brand", "Braze"));

Braze.getInstance(context).logCustomEvent("ecommerce.product_viewed", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let properties: [String: Any] = [
    "product_id": "4111176",
    "product_name": "Torchie runners",
    "variant_id": "4111176700",
    "image_url": "https://braze-apparel.com/images/products/large/torchie-runners.jpg",
    "product_url": "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/",
    "price": 85,
    "currency": "GBP",
    "source": "https://braze-apparel.com/",
    "metadata": [
        "sku": "",
        "color": "ORANGE",
        "size": "6",
        "brand": "Braze"
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.product_viewed", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.product_viewed",
      "time": "2024-01-15T09:03:45Z",
      "properties": {
        "product_id": "4111176",
        "product_name": "Torchie runners",
        "variant_id": "4111176700",
        "image_url": "https://braze-apparel.com/images/products/large/torchie-runners.jpg",
        "product_url": "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/",
        "price": 85,
        "currency": "GBP",
        "source": "https://braze-apparel.com/",
        "metadata": {
          "sku": "",
          "color": "ORANGE",
          "size": "6",
          "brand": "Braze"
        },
        "type": [
          "price_drop",
          "back_in_stock"
        ]
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.cart_updated %}

**カート更新イベントの実行**トリガーを使用して、カートに製品が追加、削除、または更新されたときを追跡できます。このイベントは、トリガーする前に以下の情報を検証します:

- イベント時刻がユーザーの特定のカートの `updated_at` 時刻より後であること。
- カートがチェックアウトプロセスに進んでいないこと。
- `products` 配列が空でないこと。

#### カートマッピングオブジェクト {#carts-mapping-object}

`ecommerce.cart_updated` イベントにはカートマッピングオブジェクトがあります。このオブジェクトは、買い物客のカート内のすべての製品を含むカートのマッピングを持つユーザープロファイルに作成されます。ショッピングカート内の製品には、以下の Liquid タグを通じてアクセスできます:

{%raw%}
```liquid
{% shopping_cart {{context_properties.${cart_id}}} %}
{% for item in shopping_cart.products %}
{% catalog_items <add_your_catalog> {{item.variant_id}} %}
```
{%endraw%}

カートが更新されず、30日以内に注文確定イベントに進まない場合、Braze はカートと関連する製品を削除します。

{% alert note %}
カートあたりの製品数は Braze では制限されていません。ただし、Shopify の制限は500です。
{% endalert %}

#### ユーザープロファイルのマージ時のカートの動作 {#cart-behavior-when-merging-user-profiles}

2つのカートがある場合、両方をマージされたユーザーに追加します。同じカートまたは異なるカートの場合、最新のカート情報を含むメッセージを送信するためにCanvasを再キューイングします。`ecommerce.cart_updated` イベントには、最新のカート ID とカート内の最新の製品が含まれます。

#### プロパティ {#properties}

| プロパティ名 | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `cart_id` | はい | 文字列 | `cart_id` を提供するサードパーティプラットフォームを使用していない場合は、[Braze セッション ID]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/) を使用できます。 |
| `total_value` | はい | フロート | カートの合計金額。 |
| `subtotal_value` | いいえ | フロート | 割引適用後、税金・送料適用前のカートの小計。 |
| `tax` | いいえ | フロート | カートに適用された税金の合計。 |
| `shipping` | いいえ | フロート | カートの送料合計。 |
| `currency` | はい | 文字列 | 製品価格の表示通貨 (「USD」や「EUR」など)。[ISO 4217 フォーマット](https://www.iso.org/iso-4217-currency-codes.html)です。 |
| `products` | はい | 配列 |  |
| `product_id` | はい | 文字列 | 閲覧された製品の一意の識別子。<br> この値は製品 ID または SKU にできます。 |
| `product_name` | はい | 文字列 | 閲覧された製品の名前。 |
| `variant_id` | はい | 文字列 | 製品バリアントの一意の識別子。例: `shirt_medium_blue` |
| `image_url` | いいえ | 文字列 | 商品画像の URL。 |
| `product_url` | いいえ | 文字列 | 詳細情報がある製品ページの URL。 |
| `quantity` | はい | 整数 | カート内の製品の数量。 |
| `price` | はい | フロート | 閲覧時の製品のバリアント単価。 |
| `metadata` | いいえ | オブジェクト | 顧客がユースケースに応じて追加したい製品に関する追加メタデータフィールド。Shopify の場合、SKU が追加されます。<br> 一般的なイベントプロパティの上限である50kbに基づく制限があります。 |
| `sku` | いいえ | 文字列 | (Shopify のみ) Shopify SKU。カタログ ID フィールドとして設定できます。 |
| `source` | はい | 文字列 | イベントの派生元ソース (Shopify の場合はストアフロント)。 |
| `metadata` | いいえ | オブジェクト | 顧客がユースケースに応じて追加したい製品に関する追加メタデータフィールド。Shopify の場合、SKU が追加されます。<br> 一般的なイベントプロパティの上限である50kbに基づく制限があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### オブジェクトの例 {#example-objects}

{% subtabs %}
{% subtab Web SDK %}

{% sdk_min_versions web:6.8.0 %}

新しい SDK バージョンでは、`logEcommerceEvent()` を呼び出します:

```javascript
braze.logEcommerceEvent({
    "name": "ecommerce.cart_updated",
    "properties": {
        "cart_id": "cart_12345",
        "currency": "USD",
        "total_value": 199.98,
        "products": [
            {
                "product_id": "8266836345064",
                "product_name": "Classic T-Shirt",
                "variant_id": "44610569208040",
                "image_url": "https://braze-apparel.com/images/tshirt-blue-medium.jpg",
                "product_url": "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040",
                "quantity": 2,
                "price": 99.99,
                "metadata": {
                    "sku": "TSH-BLU-M",
                    "color": "BLUE",
                    "size": "Medium",
                    "brand": "Braze"
                }
            }
        ],
        "source": "https://braze-apparel.com",
        "metadata": {}
    }
});
```

レガシー SDK バージョンでは、`logCustomEvent()` を呼び出します:

```javascript
braze.logCustomEvent("ecommerce.cart_updated", {
    "cart_id": "cart_12345",
    "currency": "USD",
    "total_value": 199.98,
    "subtotal_value": 179.98,
    "tax": 15.00,
    "shipping": 5.00,
    "products": [
        {
            "product_id": "8266836345064",
            "product_name": "Classic T-Shirt",
            "variant_id": "44610569208040",
            "image_url": "https://braze-apparel.com/images/tshirt-blue-medium.jpg",
            "product_url": "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040",
            "quantity": 2,
            "price": 99.99,
            "metadata": {
                "sku": "TSH-BLU-M",
                "color": "BLUE",
                "size": "Medium",
                "brand": "Braze"
            }
        }
    ],
    "source": "https://braze-apparel.com",
    "metadata": {}
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "8266836345064")
    .put("product_name", "Classic T-Shirt")
    .put("variant_id", "44610569208040")
    .put("image_url", "https://braze-apparel.com/images/tshirt-blue-medium.jpg")
    .put("product_url", "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040")
    .put("quantity", 2)
    .put("price", 99.99)
    .put("metadata", new JSONObject()
        .put("sku", "TSH-BLU-M")
        .put("color", "BLUE")
        .put("size", "Medium")
        .put("brand", "Braze"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("cart_id", "cart_12345")
    .addProperty("currency", "USD")
    .addProperty("total_value", 199.98)
    .addProperty("subtotal_value", 179.98)
    .addProperty("tax", 15.00)
    .addProperty("shipping", 5.00)
    .addProperty("products", products)
    .addProperty("source", "https://braze-apparel.com")
    .addProperty("metadata", new JSONObject());

Braze.getInstance(context).logCustomEvent("ecommerce.cart_updated", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let products: [[String: Any]] = [
    [
        "product_id": "8266836345064",
        "product_name": "Classic T-Shirt",
        "variant_id": "44610569208040",
        "image_url": "https://braze-apparel.com/images/tshirt-blue-medium.jpg",
        "product_url": "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040",
        "quantity": 2,
        "price": 99.99,
        "metadata": [
            "sku": "TSH-BLU-M",
            "color": "BLUE",
            "size": "Medium",
            "brand": "Braze"
        ]
    ]
]

let properties: [String: Any] = [
    "cart_id": "cart_12345",
    "currency": "USD",
    "total_value": 199.98,
    "subtotal_value": 179.98,
    "tax": 15.00,
    "shipping": 5.00,
    "products": products,
    "source": "https://braze-apparel.com",
    "metadata": [:]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.cart_updated", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.cart_updated",
      "time": "2024-01-15T09:15:30Z",
      "properties": {
        "cart_id": "cart_12345",
        "currency": "USD",
        "total_value": 199.98,
        "subtotal_value": 179.98,
        "tax": 15.00,
        "shipping": 5.00,
        "products": [
          {
            "product_id": "8266836345064",
            "product_name": "Classic T-Shirt",
            "variant_id": "44610569208040",
            "image_url": "https://braze-apparel.com/images/tshirt-blue-medium.jpg",
            "product_url": "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040",
            "quantity": 2,
            "price": 99.99,
            "metadata": {
              "sku": "TSH-BLU-M",
              "color": "BLUE",
              "size": "Medium",
              "brand": "Braze"
            }
          }
        ],
        "source": "https://braze-apparel.com",
        "metadata": {}
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.checkout_started %}

チェックアウト開始イベントを使用して、チェックアウトプロセスを開始したが注文を確定していない顧客をリターゲティングできます。

`ecommerce.cart_updated` イベントと同様に、このイベントではショッピングカート Liquid タグを活用して、放棄チェックアウトメッセージ用にカート内のすべての製品にアクセスできます:

{%raw%}
```liquid
{% shopping_cart {{context_properties.${cart_id}}} :abort_if_not_abandoned false %}
{% for item in shopping_cart.products %}
{% catalog_items <add_your_catalog> {{item.variant_id}} %}
```
{%endraw%}

#### プロパティ {#properties}

| プロパティ名 | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `checkout_id` | はい | 文字列 | チェックアウトの一意の識別子。 |
| `cart_id` | いいえ | 文字列 | `cart_id` を提供するサードパーティプラットフォームを使用していない場合は、[Braze セッション ID]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/) を使用できます。 |
| `total_value` | はい | フロート | カートの合計金額。 |
| `subtotal_value` | いいえ | フロート | 割引適用後、税金・送料適用前のカートの小計。 |
| `tax` | いいえ | フロート | カートに適用された税金の合計。 |
| `shipping` | いいえ | フロート | カートの送料合計。 |
| `currency` | はい | 文字列 | カートの通貨。 |
| `products` | はい | オブジェクトの配列 |  |
| `product_id` | はい | 文字列 | 閲覧された製品の一意の識別子。例えば、この値は製品 ID または SKU にできます。 |
| `product_name` | はい | 文字列 | 閲覧された製品の名前。 |
| `variant_id` | はい | 文字列 | 製品バリアントの一意の識別子。例: `shirt_medium_blue` |
| `image_url` | いいえ | 文字列 | 商品画像の URL。 |
| `product_url` | いいえ | 文字列 | 詳細情報がある製品ページの URL。 |
| `quantity` | はい | 整数 | カート内の製品の数量。 |
| `price` | はい | フロート | 閲覧時の製品のバリアント単価。 |
| `metadata` | いいえ | オブジェクト | 顧客がユースケースに応じて追加したい製品に関する追加メタデータフィールド。Shopify の場合、SKU が追加されます。<br> 一般的なイベントプロパティの上限である50kbに基づく制限があります。 |
| `sku` | いいえ | 文字列 | (Shopify のみ) Shopify SKU。カタログ ID フィールドとして設定できます。 |
| `source` | はい | 文字列 | イベントの派生元ソース (Shopify の場合はストアフロント)。 |
| `metadata` | いいえ | オブジェクト |  |
| `checkout_url` | いいえ | 文字列 | チェックアウトページの URL。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### オブジェクトの例 {#example-objects}

{% subtabs %}
{% subtab Web SDK %}

{% sdk_min_versions web:6.8.0 %}

新しい SDK バージョンでは、`logEcommerceEvent()` を呼び出します:

```javascript
braze.logEcommerceEvent({
    "name": "ecommerce.checkout_started",
    "properties": {
        "checkout_id": "checkout_abc123",
        "cart_id": "cart_12345",
        "total_value": 199.98,
        "currency": "USD",
        "products": [
            {
                "product_id": "632910392",
                "product_name": "Wireless Headphones",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199.98,
                "metadata": {
                    "sku": "WH-BLK-PRO",
                    "color": "Black",
                    "brand": "BrazeAudio"
                }
            }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
            "checkout_url": "https://checkout.braze-audio.com/abc123"
        }
    }
});
```

レガシー SDK バージョンでは、`logCustomEvent()` を呼び出します:

```javascript
braze.logCustomEvent("ecommerce.checkout_started", {
    "checkout_id": "checkout_abc123",
    "cart_id": "cart_12345",
    "total_value": 199.98,
    "subtotal_value": 179.98,
    "tax": 15.00,
    "shipping": 5.00,
    "currency": "USD",
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "checkout_url": "https://checkout.braze-audio.com/abc123"
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "632910392")
    .put("product_name", "Wireless Headphones")
    .put("variant_id", "808950810")
    .put("quantity", 1)
    .put("price", 199.98)
    .put("metadata", new JSONObject()
        .put("sku", "WH-BLK-PRO")
        .put("color", "Black")
        .put("brand", "AudioTech"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("checkout_id", "checkout_abc123")
    .addProperty("cart_id", "cart_12345")
    .addProperty("total_value", 199.98)
    .addProperty("subtotal_value", 179.98)
    .addProperty("tax", 15.00)
    .addProperty("shipping", 5.00)
    .addProperty("currency", "USD")
    .addProperty("products", products)
    .addProperty("source", "https://braze-audio.com")
    .addProperty("metadata", new JSONObject()
        .put("checkout_url", "https://checkout.braze-audio.com/abc123"));

Braze.getInstance(context).logCustomEvent("ecommerce.checkout_started", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 199.98,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "checkout_id": "checkout_abc123",
    "cart_id": "cart_12345",
    "total_value": 199.98,
    "subtotal_value": 179.98,
    "tax": 15.00,
    "shipping": 5.00,
    "currency": "USD",
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "checkout_url": "https://checkout.braze-audio.com/abc123"
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.checkout_started", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.checkout_started",
      "time": "2024-01-15T09:25:45Z",
      "properties": {
        "checkout_id": "checkout_abc123",
        "cart_id": "cart_12345",
        "total_value": 199.98,
        "subtotal_value": 179.98,
        "tax": 15.00,
        "shipping": 5.00,
        "currency": "USD",
        "products": [
          {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
              "sku": "WH-BLK-PRO",
              "color": "Black",
              "brand": "BrazeAudio"
            }
          }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
          "checkout_url": "https://checkout.braze-audio.com/abc123"
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.order_placed %}

注文確定イベントを使用して、顧客がチェックアウトプロセスを正常に完了し、注文を確定したときにトリガーできます。

#### プロパティ {#properties}

| プロパティ名 | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `order_id` | はい | 文字列 | 確定された注文の一意の識別子。 |
| `cart_id` | いいえ | 文字列 | `cart_id` を提供するサードパーティプラットフォームを使用していない場合は、[Braze セッション ID]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/) を使用できます。 |
| `total_value` | はい | フロート | カートの合計金額。 |
| `subtotal_value` | いいえ | フロート | 割引適用後、税金・送料適用前の注文の小計。 |
| `tax` | いいえ | フロート | 注文に適用された税金の合計。 |
| `shipping` | いいえ | フロート | 注文の送料合計。 |
| `currency` | はい | 文字列 | カートの通貨。 |
| `total_discounts` | いいえ | フロート | 注文に適用された割引の合計額。 |
| `discounts`| いいえ | オブジェクトの配列 | 注文に適用された割引の詳細リスト。 |
| `products` | はい | オブジェクトの配列 |  |
| `product_id` | はい | 文字列 | 閲覧された製品の一意の識別子。この値は製品 ID または SKU にできます。 |
| `product_name` | はい | 文字列 | 閲覧された製品の名前。 |
| `variant_id` | はい | 文字列 | 製品バリアントの一意の識別子。例: `shirt_medium_blue` |
| `image_url` | いいえ | 文字列 | 商品画像の URL。 |
| `product_url` | いいえ | 文字列 | 詳細情報がある製品ページの URL。 |
| `quantity` | はい | 整数 | カート内の製品の数量。 |
| `price` | はい | フロート | 閲覧時の製品のバリアント単価。 |
| `metadata` | いいえ | オブジェクト | 顧客がユースケースに応じて追加したい製品に関する追加メタデータフィールド。Shopify の場合、SKU が追加されます。<br> 一般的なイベントプロパティの上限である50kbに基づく制限があります。 |
| `sku` | いいえ | 文字列 | (Shopify のみ) Shopify SKU。カタログ ID フィールドとして設定できます。 |
| `source` | はい | 文字列 | イベントの派生元ソース (Shopify の場合はストアフロント)。 |
| `order_status_url` | いいえ | 文字列 | 注文ステータスを確認するための URL。 |
| `order_number` | いいえ | 文字列 | (Shopify のみ) 確定された注文の一意の注文番号。 |
| `tags` | いいえ | 配列 | (Shopify のみ) 注文タグ |
| `referring_site` | いいえ | 文字列 | (Shopify のみ) 注文の発生元サイト (Meta など)。 |
| `payment_gateway_names` | いいえ | 配列 | (Shopify のみ) 決済システムのソース (POS やモバイルなど)。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### オブジェクトの例 {#example-objects}

{% subtabs %}
{% subtab Web SDK %}

{% sdk_min_versions web:6.8.0 %}

新しい SDK バージョンでは、`logEcommerceEvent()` を呼び出します:

```javascript
braze.logEcommerceEvent({
    "name": "ecommerce.order_placed",
    "properties": {
        "order_id": "order_67890",
        "cart_id": "cart_12345",
        "total_value": 189.98,
        "currency": "USD",
        "total_discounts": 10.00,
        "discounts": [
            {
                "code": "SAVE10",
                "amount": 10.00
            }
        ],
        "products": [
            {
                "product_id": "632910392",
                "product_name": "Wireless Headphones",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199.98,
                "metadata": {
                    "sku": "WH-BLK-PRO",
                    "color": "Black",
                    "brand": "BrazeAudio"
                }
            }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
            "order_status_url": "https://braze-audio.com/orders/67890/status",
            "order_number": "ORD-2024-001234",
            "tags": ["electronics", "audio"],
            "referring_site": "https://www.e-referrals.com",
            "payment_gateway_names": ["tap2pay", "dotcash"]
        }
    }
});
```

レガシー SDK バージョンでは、`logCustomEvent()` を呼び出します:

```javascript
braze.logCustomEvent("ecommerce.order_placed", {
    "order_id": "order_67890",
    "cart_id": "cart_12345",
    "total_value": 189.98,
    "subtotal_value": 169.98,
    "tax": 14.40,
    "shipping": 5.60,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": [
        {
            "code": "SAVE10",
            "amount": 10.00
        }
    ],
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["electronics", "audio"],
        "referring_site": "https://www.e-referrals.com",
        "payment_gateway_names": ["tap2pay", "dotcash"]
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray discounts = new JSONArray();
discounts.put(new JSONObject()
    .put("code", "SAVE10")
    .put("amount", 10.00));

JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "632910392")
    .put("product_name", "Wireless Headphones")
    .put("variant_id", "808950810")
    .put("quantity", 1)
    .put("price", 199.98)
    .put("metadata", new JSONObject()
        .put("sku", "WH-BLK-PRO")
        .put("color", "Black")
        .put("brand", "AudioTech"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("order_id", "order_67890")
    .addProperty("cart_id", "cart_12345")
    .addProperty("total_value", 189.98)
    .addProperty("subtotal_value", 169.98)
    .addProperty("tax", 14.40)
    .addProperty("shipping", 5.60)
    .addProperty("currency", "USD")
    .addProperty("total_discounts", 10.00)
    .addProperty("discounts", discounts)
    .addProperty("products", products)
    .addProperty("source", "https://braze-audio.com")
    .addProperty("metadata", new JSONObject()
        .put("order_status_url", "https://braze-audio.com/orders/67890/status")
        .put("order_number", "ORD-2024-001234")
        .put("tags", new JSONArray().put("electronics").put("audio"))
        .put("referring_site", "https://www.e-referrals.com")
        .put("payment_gateway_names", new JSONArray().put("tap2pay").put("dotcash")));

Braze.getInstance(context).logCustomEvent("ecommerce.order_placed", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let discounts: [[String: Any]] = [
    [
        "code": "SAVE10",
        "amount": 10.00
    ]
]

let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 199.98,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "order_id": "order_67890",
    "cart_id": "cart_12345",
    "total_value": 189.98,
    "subtotal_value": 169.98,
    "tax": 14.40,
    "shipping": 5.60,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": discounts,
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["electronics", "audio"],
        "referring_site": "https://www.e-referrals.com",
        "payment_gateway_names": ["tap2pay", "dotcash"]
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.order_placed", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.order_placed",
      "time": "2024-01-15T09:35:20Z",
      "properties": {
        "order_id": "order_67890",
        "cart_id": "cart_12345",
        "total_value": 189.98,
        "subtotal_value": 169.98,
        "tax": 14.40,
        "shipping": 5.60,
        "currency": "USD",
        "total_discounts": 10.00,
        "discounts": [
          {
            "code": "SAVE10",
            "amount": 10.00
          }
        ],
        "products": [
          {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
              "sku": "WH-BLK-PRO",
              "color": "Black",
              "brand": "BrazeAudio"
            }
          }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
          "order_status_url": "https://braze-audio.com/orders/67890/status",
          "order_number": "ORD-2024-001234",
          "tags": ["electronics", "audio"],
          "referring_site": "https://www.e-referrals.com",
          "payment_gateway_names": ["tap2pay", "dotcash"]
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.order_refunded %}

注文返金イベントを使用して、注文が部分的または全額返金されたときにトリガーできます。

#### プロパティ {#properties}

| プロパティ名       | 必須 | データタイプ | 説明   |
|---------------|---------|-----------|-------------------------|
| `order_id`            | はい      | 文字列    | 確定された注文の一意の識別子。        |
| `total_value`         | はい      | フロート     | カートの合計金額。    |
| `currency`            | はい      | 文字列    | カートの通貨。    |
| `total_discounts`     | いいえ       | フロート     | 注文に適用された割引の合計額。   |
| `discounts`           | いいえ       | オブジェクトの配列     | 注文に適用された割引の詳細リスト。 |
| `products`            | はい      | オブジェクトの配列     |  |
| `product_id`       | はい      | 文字列    | 閲覧された製品の一意の識別子。この値は製品 ID、SKU、または類似のものにできます。<br>部分返金が発行され、返金に `product_id` が割り当てられていない場合 (例: 注文レベルの返金)、汎用的な `product_id` を指定してください。             |
| `product_name`     | はい      | 文字列    | 閲覧された製品の名前。                                                                      |
| `variant_id`       | はい      | 文字列    | 製品バリアントの一意の識別子 (`shirt_medium_blue` など)。                                         |
| `image_url`        | いいえ       | 文字列    | 商品画像の URL。     |
| `product_url`      | いいえ       | 文字列    | 詳細情報がある製品ページの URL。  |
| `quantity`         | はい      | 整数   | カート内の製品の数量。   |
| `price`            | はい      | フロート     | 閲覧時の製品のバリアント単価。  |
| `metadata`         | いいえ       | オブジェクト    | 顧客がユースケースに応じて追加したい製品に関する追加メタデータフィールド。Shopify の場合、SKU が追加されます。一般的なイベントプロパティの上限である50kbに基づく制限があります。 |
| `sku`            | いいえ       | 文字列    | (Shopify のみ) Shopify SKU。カタログ ID フィールドとして設定できます。  |
| `source`              | はい      | 文字列    | イベントの派生元ソース (Shopify の場合はストアフロント)。    |
| `metadata`            | いいえ       | オブジェクト    |                |
| `order_status_url`  | いいえ       | 文字列    | 注文ステータスを確認するための URL。     |
| `order_note`       | いいえ       | 文字列    | (Shopify のみ) 販売者が注文に追加したメモ。    |
| `order_number`     | いいえ       | 文字列    | (Shopify のみ) 確定された注文の一意の注文番号。   |
| `tags`             | いいえ       | 配列     | (Shopify のみ) 注文タグ。  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### オブジェクトの例 {#example-objects}

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.order_refunded", {
    "order_id": "order_67890",
    "total_value": 99.99,
    "currency": "USD",
    "total_discounts": 5.00,
    "discounts": [
        {
            "code": "SAVE5",
            "amount": 5.00
        }
    ],
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 99.99,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_note": "Customer requested refund due to defective item",
        "order_number": "ORD-2024-001234",
        "tags": ["refund", "defective"]
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray discounts = new JSONArray();
discounts.put(new JSONObject()
    .put("code", "SAVE5")
    .put("amount", 5.00));

JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "632910392")
    .put("product_name", "Wireless Headphones")
    .put("variant_id", "808950810")
    .put("quantity", 1)
    .put("price", 99.99)
    .put("metadata", new JSONObject()
        .put("sku", "WH-BLK-PRO")
        .put("color", "Black")
        .put("brand", "AudioTech"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("order_id", "order_67890")
    .addProperty("total_value", 99.99)
    .addProperty("currency", "USD")
    .addProperty("total_discounts", 5.00)
    .addProperty("discounts", discounts)
    .addProperty("products", products)
    .addProperty("source", "https://braze-audio.com")
    .addProperty("metadata", new JSONObject()
        .put("order_status_url", "https://braze-audio.com/orders/67890/status")
        .put("order_note", "Customer requested refund due to defective item")
        .put("order_number", "ORD-2024-001234")
        .put("tags", new JSONArray().put("refund").put("defective")));

Braze.getInstance(context).logCustomEvent("ecommerce.order_refunded", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let discounts: [[String: Any]] = [
    [
        "code": "SAVE5",
        "amount": 5.00
    ]
]

let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 99.99,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "order_id": "order_67890",
    "total_value": 99.99,
    "currency": "USD",
    "total_discounts": 5.00,
    "discounts": discounts,
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_note": "Customer requested refund due to defective item",
        "order_number": "ORD-2024-001234",
        "tags": ["refund", "defective"]
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.order_refunded", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.order_refunded",
      "time": "2024-01-15T10:15:30Z",
      "properties": {
        "order_id": "order_67890",
        "total_value": 99.99,
        "currency": "USD",
        "total_discounts": 5.00,
        "discounts": [
          {
            "code": "SAVE5",
            "amount": 5.00
          }
        ],
        "products": [
          {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 99.99,
            "metadata": {
              "sku": "WH-BLK-PRO",
              "color": "Black",
              "brand": "BrazeAudio"
            }
          }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
          "order_status_url": "https://braze-audio.com/orders/67890/status",
          "order_note": "Customer requested refund due to defective item",
          "order_number": "ORD-2024-001234",
          "tags": ["refund", "defective"]
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.order_cancelled %}

注文キャンセルイベントを使用して、顧客が注文をキャンセルしたときにトリガーできます。

#### プロパティ {#properties}

| プロパティ名      | 必須 | データタイプ | 説明       |
|---------------------|----------|-----------|-------------------|
| `order_id`            | はい      | 文字列    | 確定された注文の一意の識別子。              |
| `cancel_reason`       | はい      | 文字列    | 注文がキャンセルされた理由。           |
| `total_value`         | はい      | フロート     | カートの合計金額。         |
| `subtotal_value`      | いいえ       | フロート     | 割引適用後、税金・送料適用前の注文の小計。 |
| `tax`                 | いいえ       | フロート     | 注文に適用された税金の合計。 |
| `shipping`            | いいえ       | フロート     | 注文の送料合計。 |
| `currency`            | はい      | 文字列    | カートの通貨。           |
| `total_discounts`     | いいえ       | フロート     | 注文に適用された割引の合計額。     |
| `discounts`           | いいえ       | オブジェクトの配列     | 注文に適用された割引の詳細リスト。             |
| `products`            | はい      | オブジェクトの配列     |         |
| `product_id`          | はい      | 文字列    | 閲覧された製品の一意の識別子。この値は製品 ID、SKU、または類似のものにできます。             |
| `product_name`        | はい      | 文字列    | 閲覧された製品の名前。          |
| `variant_id`          | はい      | 文字列    | 製品バリアントの一意の識別子 (`shirt_medium_blue` など)。        |
| `image_url`           | いいえ       | 文字列    | 商品画像の URL。           |
| `product_url`         | いいえ       | 文字列    | 詳細情報がある製品ページの URL。                                                                     |
| `quantity`            | はい      | 整数   | カート内の製品の数量。        |
| `price`               | はい      | フロート     | 閲覧時の製品のバリアント単価。     |
| `metadata`            | いいえ       | オブジェクト    | 顧客がユースケースに応じて追加したい製品に関する追加メタデータフィールド。Shopify の場合、SKU が追加されます。一般的なイベントプロパティの上限である50kbに基づく制限があります。 |
| `sku`                 | いいえ       | 文字列    | (Shopify のみ) Shopify SKU。カタログ ID フィールドとして設定できます。        |
| `source`              | はい      | 文字列    | イベントの派生元ソース (Shopify の場合はストアフロント)。    |
| `metadata`            | いいえ       | オブジェクト    |       |
| `order_status_url`    | いいえ       | 文字列    | 注文ステータスを確認するための URL。                                                                          |
| `order_number`        | いいえ       | 文字列    | (Shopify のみ) 確定された注文の一意の注文番号。  |
| `tags`                | いいえ       | 配列     | (Shopify のみ) 注文タグ。            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### オブジェクトの例 {#example-objects}

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.order_cancelled", {
    "order_id": "order_67890",
    "cancel_reason": "customer changed mind",
    "total_value": 189.98,
    "subtotal_value": 169.98,
    "tax": 14.40,
    "shipping": 5.60,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": [
        {
            "code": "SAVE10",
            "amount": 10.00
        }
    ],
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["cancelled", "customer_request"]
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray discounts = new JSONArray();
discounts.put(new JSONObject()
    .put("code", "SAVE10")
    .put("amount", 10.00));

JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "632910392")
    .put("product_name", "Wireless Headphones")
    .put("variant_id", "808950810")
    .put("quantity", 1)
    .put("price", 199.98)
    .put("metadata", new JSONObject()
        .put("sku", "WH-BLK-PRO")
        .put("color", "Black")
        .put("brand", "AudioTech"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("order_id", "order_67890")
    .addProperty("cancel_reason", "customer changed mind")
    .addProperty("total_value", 189.98)
    .addProperty("subtotal_value", 169.98)
    .addProperty("tax", 14.40)
    .addProperty("shipping", 5.60)
    .addProperty("currency", "USD")
    .addProperty("total_discounts", 10.00)
    .addProperty("discounts", discounts)
    .addProperty("products", products)
    .addProperty("source", "https://braze-audio.com")
    .addProperty("metadata", new JSONObject()
        .put("order_status_url", "https://braze-audio.com/orders/67890/status")
        .put("order_number", "ORD-2024-001234")
        .put("tags", new JSONArray().put("cancelled").put("customer_request")));

Braze.getInstance(context).logCustomEvent("ecommerce.order_cancelled", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let discounts: [[String: Any]] = [
    [
        "code": "SAVE10",
        "amount": 10.00
    ]
]

let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 199.98,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "order_id": "order_67890",
    "cancel_reason": "customer changed mind",
    "total_value": 189.98,
    "subtotal_value": 169.98,
    "tax": 14.40,
    "shipping": 5.60,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": discounts,
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["cancelled", "customer_request"]
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.order_cancelled", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.order_cancelled",
      "time": "2024-01-15T10:45:15Z",
      "properties": {
        "order_id": "order_67890",
        "cancel_reason": "customer changed mind",
        "total_value": 189.98,
        "subtotal_value": 169.98,
        "tax": 14.40,
        "shipping": 5.60,
        "currency": "USD",
        "total_discounts": 10.00,
        "discounts": [
          {
            "code": "SAVE10",
            "amount": 10.00
          }
        ],
        "products": [
          {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
              "sku": "WH-BLK-PRO",
              "color": "Black",
              "brand": "BrazeAudio"
            }
          }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
          "order_status_url": "https://braze-audio.com/orders/67890/status",
          "order_number": "ORD-2024-001234",
          "tags": ["cancelled", "customer_request"]
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

## e コマースのキャンバステンプレート {#ecommerce-canvas-templates}

Braze は、e コマース推奨イベントを活用した構築済みのキャンバステンプレートを用意しています。例えば、チェックアウトプロセスを開始したが注文を確定する前に離脱した顧客をターゲティングするテンプレートなどがあります。これらのイベントを使用して、メッセージングのパーソナライズや特定のオーディエンスのターゲティングにより、ユーザージャーニーを強化するための情報に基づいた意思決定を行うことができます。

これらのイベントをキャンバステンプレートで活用するその他の方法については、専用の [e コマースユースケース]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases/)をご覧ください。

## ユーザー計算フィールド {#user-calculated-fields}

以下のフィールドについて、標準化されたユーザーフィールド計算を使用しています:

- **合計収益** = 注文確定の合計値の合計 - 注文返金の合計値の合計
- **合計注文数** = 個別の注文確定イベントの数 - 個別の注文キャンセルの数
- **合計返金額** = 注文返金の合計値の合計

これらのユーザーフィールド計算は、ユーザープロファイルの**トランザクション**タブにも表示されます。

![ユーザー計算フィールドを含む「トランザクション」タブ。]({% image_buster /assets/img/Shopify/transactions_tab.png %}){: style="max-width:70%;"}

## よくある質問 {#frequently-asked-questions}

### 製品レベルの購入データはどこで確認できますか？ {#where-can-i-view-product-level-purchase-data}

ユーザープロファイルの**トランザクション**タブには、高レベルの計算フィールド (合計収益や合計注文数など) が表示されます。特定のユーザーの製品レベルの詳細を確認するには、[クエリビルダー]({{site.baseurl}}/user_guide/analytics/reports/query_builder/)を使用して e コマースイベントデータをクエリするか、[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) を通じてイベントデータをエクスポートしてください。

レガシー購入イベントとは異なり、e コマース推奨イベントは製品の詳細を `products` 配列内のネストされたイベントプロパティとして保存します。これらのプロパティは、Liquid を通じたメッセージングや、[セグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension/)を通じたセグメンテーションで利用できます。

### 特定の製品でユーザーをセグメント化するにはどうすればよいですか？ {#how-do-i-segment-users-by-a-specific-product}

セグメンターでは、ユーザーが e コマースイベントを実行した回数でフィルタリングできます。特定の製品プロパティ (`product_id` や `product_name` など) でフィルタリングするには、ネストされたイベントプロパティのフィルタリングをサポートする[セグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension/)を使用してください。例えば、過去90日間に製品「SKU-123」を購入したすべてのユーザーを見つけることができます。

### レガシー購入イベントと e コマース推奨イベントの違いは何ですか？ {#whats-the-difference-between-legacy-purchase-events-and-ecommerce-recommended-events}

レガシー購入イベントは Braze の[購入オブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object/)を使用し、`product_id` と `price` を持つ個別の製品購入を記録します。e コマース推奨イベント (`ecommerce.order_placed` など) はカスタムイベントプロパティを使用し、複数の製品、割引、メタデータを含む注文全体のコンテキストを単一のイベントでキャプチャします。

e コマース推奨イベントの導入に伴い、Braze は将来的にレガシー購入イベントを段階的に廃止する予定です。現在購入イベントを使用している場合は、事前に通知されます。それまでの間、公式の廃止日まで購入イベントを引き続き使用できます。詳細については、[推奨イベントの概要]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/)を参照してください。

### e コマース推奨イベントにカスタムプロパティを追加できますか？ {#can-i-add-custom-properties-to-ecommerce-recommended-events}

e コマース推奨イベントには、必須フィールドとオプションフィールドを含む定義済みのスキーマがあります。各イベントの `metadata` オブジェクト内に追加のカスタムデータを含めることができます。ただし、カスタムの注文レベルタグや独自のフィールド (購入チャネルや小売店情報など) は、トップレベルのプロパティとしてはサポートされていません。これらのフィールドがセグメンテーションに必要な場合は、e コマースイベントと並行して別のカスタムイベントとして送信し続けてください。

### e コマースイベントを送信する際に external_id を含める必要がありますか？ {#do-i-need-to-include-externalid-when-sending-ecommerce-events}

イベントの送信方法によって異なります:

- **SDK 経由の場合**: いいえ。Braze SDKを使用する場合、イベントはSDKの現在のユーザーコンテキスト (匿名または識別済み) に自動的に関連付けられます。各イベント呼び出しでユーザー識別子を渡す必要はありません。代わりに、`changeUser` などのメソッドを使用してそのコンテキストのユーザーを識別できます。
- **REST API (`/users/track`) 経由の場合**: はい。各 API リクエストには、`external_id`、`braze_id`、`user_alias`、`email`、`phone` などのユーザー識別子を含める必要があります。APIには「現在のユーザー」コンテキストがないためです。

### AI 項目のレコメンデーション設定のドロップダウンにネストされた製品プロパティが表示されないのはなぜですか？ {#why-dont-nested-product-properties-appear-in-the-ai-recommendations-setup-dropdown}

[AI 項目のレコメンデーション]({{site.baseurl}}/user_guide/brazeai/item_recommendations/)を設定する際、**プロパティ名**ドロップダウンにはトップレベルのイベントプロパティ (`order_id`、`total_value`、`currency` など) のみが表示されます。`products` 配列内のネストされたプロパティ (例: `products.product_id` や `products.variant_id`) はこのリストに表示されない場合がありますが、フィールドにドット記法を使用して手動で入力できます。ほとんどの e コマース実装では、Braze はアイテム識別子として `products.product_id` を使用し、`product_id` または `variant_id` の値と一致するアイテム ID を持つ[カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs/)と組み合わせることを推奨しています。

### e コマースイベントの一部が Braze に表示されないのはなぜですか？ {#why-are-some-of-my-ecommerce-events-not-appearing-in-braze}

イベントがユーザープロファイルやログに表示されない場合は、以下を確認してください:

- **SDK データフラッシュのタイミング**: Braze SDKはデータをローカルにキャッシュし、定期的にアップロードします (通常10〜60秒以内)。即時アップロードを強制するには、`logCustomEvent()` の後に `requestImmediateDataFlush()` を呼び出してください。
- **必須プロパティ**: e コマースイベントには必須プロパティがあります。必須プロパティが欠落しているか、データタイプが無効な場合、イベントが拒否される可能性があります。イベントペイロードが[必須スキーマ](#types-of-ecommerce-recommended-events)と一致していることを確認してください。
- **イベント名の正確性**: e コマースイベント名は大文字と小文字が区別され、正確に一致する必要があります (例: `ecommerce.checkout_started` であり、`ecommerce.checkoutStarted` ではありません)。