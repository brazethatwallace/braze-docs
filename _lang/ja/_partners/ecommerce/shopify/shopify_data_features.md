---
nav_title: Shopifyのデータ機能
article_title: Shopifyのデータ機能
description: "このリファレンス記事では、Shopifyのデータ機能について説明します。"
page_type: partner
search_tag: Partner
alias: /shopify_data_features/
page_order: 4
---

# Shopifyのデータ機能 {#shopify-data-features}

> この記事では、Shopifyの機能の概要を説明します。追跡対象のShopifyデータ、ペイロード例、履歴バックフィル、および製品の同期が含まれます。

## トラッキングされるShopifyイベント {#tracked-shopify-events}

Shopify連携では、[eコマース推奨イベント]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events)を使用して、主要なショッピング行動を取得します。これらのイベントを使用した実装例やマーケティング戦略については、[eコマースユースケース]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases)を参照してください。

{% multi_lang_include alerts/important_alerts.md alert='Shopify customer create' %}

{% tabs %}
{% tab ペイロードの例 %}
{% subtabs global %}
{% subtab Product viewed %}
```json
{
    "name": "ecommerce.product_viewed",
    "properties": {
        "product_id": "12345",
        "product_name": "product",
        "variant_id": "123",
        "image_url": "www.image-url.com",
        "product_url": "mystorefront.myshopify.com/product",
        "price": 10,
        "currency": "USD",
        "source": "mystorefront.myshopify.com",
        "metadata": {
          "sku": "sku"
        },
        "type": [
          "price_drop",
          "back_in_stock"
        ]
    }
}
```
{% endsubtab %}
{% subtab Cart updated %}
```json
{
    "name": "ecommerce.cart_updated",
    "properties": {
        "cart_id": "Z2NwLXVzLWVhc3QxOjAxSjk3UFg4RlFZMjVTVkRHRlc1RlI3SlRY",
        "currency": "USD",
        "total_value": 2000000,
        "products": [
            {
                "product_id": "8266836345064",
                "product_name": "PANTS!!!",
                "variant_id": "44610569208040",
                "image_url": "https://cdn.shopify.com/s/files/1/0604/4211/6328/files/1200px-Trousers-colourisolated.jpg?v=1689256168",
                "product_url": "https://test-store.myshopify.com/products/pants?variant=44610569208040",
                "quantity": 2,
                "price": 1000000,
                "metadata": {
                    "sku": "007"
                }
            }
        ],
        "source": "https://test-store.myshopify.com",
        "metadata": {}
    }
}
```
{% endsubtab %}
{% subtab Checkout started %}
```json
{
    "name": "ecommerce.checkout_started",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "cart_id": "eeafa272cebfd4b22385bc4b645e762c",
        "total_value": 421.88,
        "subtotal_value": 396.88,
        "tax": 15.00,
        "shipping": 10.00,
        "currency": "USD",
        "products": [
            {
                "product_id": "632910392",
                "product_name": "IPod Nano - 8GB",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199,
                "metadata": {
                    "sku": "IPOD2008PINK"
                }
            }
        ],
        "source": "braze-mock-storefront.myshopify.com",
        "checkout_id": "123123123",
        "metadata": {
            "checkout_url": "https://checkout.local/548380009/checkouts/123123123/recover?key=example-secret-token"
        }
    }
}
```
{% endsubtab %}
{% subtab Order placed %}
{% raw %}
```json
{
    "name": "ecommerce.order_placed",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "order_id": "820982911946154508",
        "cart_id": "eeafa272cebfd4b22385bc4b645e762c",
        "total_value": 421.88,
        "subtotal_value": 396.88,
        "tax": 15.00,
        "shipping": 10.00,
        "currency": "USD",
        "total_discounts": 5,
        "discounts": [],
        "products": [
            {
                "product_id": "632910392",
                "product_name": "IPod Nano - 8GB",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199,
                "metadata": {
                    "sku": "IPOD2008PINK"
                }
            }
        ],
        "source": "braze-mock-storefront.myshopify.com",
        "metadata": {
            "order_status_url": "https://apple.myshopify.com/690933842/orders/123456abcd/authenticate?key=abcdefg",
            "order_number": "1234",
            "tags": [
                "heavy",
                "heavy2"
            ],
            "referring_site": "https://www.google.com",
            "payment_gateway_names": [
                "visa",
                "bogus"
            ]
        }
    }
}
```
{% endraw %}
{% endsubtab %}
{% subtab Fulfilled order %}
```json
{
 "name": "shopify_fulfilled_order",
 "time": "2022-05-23T14:44:34-04:00",
 "properties": {
   "order_id": 4444668657855,
   "line_items": [
     {
       "quantity": 1,
       "product_id": 6143032066239,
       "sku": null,
       "title": "Dark Denim Top",
  "variant_id": 40094740549876,
       "variant_title": "Small Dark Denim Top",


       "vendor": "partners-demo",
       "name": "Dark Denim Top",
       "properties": [],
       "price": "60.00",
       "fulfillment_status": "fulfilled"
     }
   ],
   "shipping": [
     {
       "title": "Standard",
       "price": "0.00"
     }
   ],
   "total_price": "130.66",
   "confirmed": true,
   "total_discounts": "0.00",
   "discount_codes": [],
   "order_number": 1093,
   "order_status_url": "https://test-store.myshopify.com/",
   "cancelled_at": null,
   "tags": "",
   "closed_at": "2022-05-23T14:44:34-04:00",
   "fulfillment_status": "fulfilled",
   "fulfillments": [
     {
       "shipment_status": null,
       "status": "success",
       "tracking_company": "Other",
       "tracking_number": "456",
       "tracking_numbers": [
         "456"
       ],
       "tracking_url": "https://braze.com",
       "tracking_urls": [
         "https://braze.com"
       ],
       "line_items": [
         {
           "fulfillment_status": "fulfilled",
           "name": "Dark Denim Top",
           "price": "60.00",
           "product_id": 6143032066239,
           "quantity": 1,
           "requires_shipping": true,
           "sku": null,
           "title": "Dark Denim Top",
           "variant_id": 40094740549876,
           "variant_title": "Small Dark Denim Top",
           "vendor": "partners-demo"
         }
       ]
     }
   ]
 },
 "braze_id": "123abc123abc"
}
```
{% endsubtab %}
{% subtab Partially fulfilled order %}
```json
{
 "name": "shopify_partially_fulfilled_order",
 "time": "2022-05-23T14:43:34-04:00",
 "properties": {
   "order_id": 4444668657855,
   "line_items": [
     {
       "quantity": 1,
       "product_id": 6143032066239,
       "sku": null,
       "title": "Dark Denim Top",
       "variant_id": 40094740549876,
       "variant_title": "",
       "vendor": "partners-demo",
       "name": "Dark Denim Top",
       "properties": [],
       "price": "60.00",
       "fulfillment_status": "fulfilled"
     }
   ],
   "shipping": [
     {
       "title": "Standard",
       "price": "0.00"
     }
   ],
   "total_price": "130.66",
   "confirmed": true,
   "total_discounts": "0.00",
   "discount_codes": [],
   "order_number": 1093,
   "order_status_url": "https://test-store.myshopify.com/",
   "cancelled_at": null,
   "tags": "",
   "closed_at": null,
   "fulfillment_status": "partial",
   "fulfillments": [
     {
       "shipment_status": null,
       "status": "success",
       "tracking_company": "Other",
       "tracking_number": "123",
       "tracking_numbers": [
         "123"
       ],
       "tracking_url": "https://braze.com",
       "tracking_urls": [
         "https://braze.com"
       ],
       "line_items": [
         {
           "fulfillment_status": "fulfilled",
           "name": "Dark Denim Top",
           "price": "60.00",
           "product_id": 6143032066239,
           "properties": [],
           "quantity": 1,
           "requires_shipping": true,
           "sku": null,
           "title": "Dark Denim Top",
           "variant_id": 40094740549876,
           "variant_title": "",
           "vendor": "partners-demo"
         }
       ]
     }
   ]
 },
 "braze_id": "abc123abc123"
}
```
{% endsubtab %}
{% subtab Paid order %}
```json
{
 "name": "shopify_paid_order",
 "time": "2022-05-23T13:52:38-04:00",
 "properties": {
   "order_id": 4444596371647,
   "line_items": [
     {
       "quantity": 1,
       "product_id": 6143033344191,
       "sku": null,
       "title": "LED High Tops",
       "variant_id": 40094740549876,
       "variant_title": null,
       "vendor": "partners-demo",
       "name": "LED High Tops",
       "properties": [],
       "price": "80.00",
       "fulfillment_status": null
     }
   ]
 }
}
```
{% endsubtab %}
{% subtab Order cancelled %}
```json
{
    "name": "ecommerce.order_cancelled",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "order_id": "820982911946154508",
        "cancel_reason": "no longer necessary",
        "total_value": 421.88,
        "subtotal_value": 396.88,
        "tax": 15.00,
        "shipping": 10.00,
        "currency": "USD",
        "total_discounts": 5,
        "discounts": [],
        "products": [
            {
                "product_id": "632910392",
                "product_name": "IPod Nano - 8GB",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199,
                "metadata": {
                    "sku": "IPOD2008PINK"
                }
            }
        ],
        "source": "braze-mock-storefront.myshopify.com",
        "metadata": {
            "order_status_url": "https://apple.myshopify.com/690933842/orders/123456abcd/authenticate?key=abcdefg",
            "order_number": "1234",
            "tags": [
                "heavy",
                "heavy2"
            ]
        }
    }
}
```
{% endsubtab %}
{% subtab Order refunded %}
```json
{
    "name": "ecommerce.order_refunded",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "order_id": "820982911946154508",
        "total_value": 421.88,
        "currency": "USD",
        "products": [
            {
                "product_id": "632910392",
                "product_name": "IPod Nano - 8GB",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199,
                "metadata": {
                    "sku": "IPOD2008PINK"
                }
            }
        ],
        "source": "braze-mock-storefront.myshopify.com",
        "metadata": {
		"order_note": "item was broken"
        }
    }
}
```
{% endsubtab %}
{% subtab Account login %}
```json
{
	"name": "shopify_account_login",
	"properties": {
	"source": "braze-mock-storefront.myshopify.com"
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Shopifyイベント %}

{% alert note %}
Brazeは、eコマースイベントに必要なイベントプロパティ（`cart_id`や`cart_token`など）の提供をShopifyに依存しています。まれに、Shopifyの一時的な問題によりこれらのプロパティが欠落し、影響を受けたイベントがドロップされることがあります。
{% endalert %}

{% subtabs global %}
{% subtab Product viewed %}
**イベント**: `ecommerce.product_viewed`<br>
**タイプ**: 推奨イベント<br>
**トリガー**: 顧客が商品ページを閲覧したとき<br>
**データソース**: Braze SDK<br>
**ユースケース**: 閲覧放棄

{% raw %}
| 変数 | Liquidテンプレーティング |
| --- | --- |
|------------------|-----------------------------------------------------|
| `product_id`       | `{{event_properties.${product_id}}}`                |
| `product_name `    | `{{event_properties.${product_name}}}`              |
| `variant_id`       | `{{event_properties.${variant_id}}}`                |
| `image_url `       | `{{event_properties.${image_url}}}`                 |
| `product_url`      | `<your-store.myshopify.com>{{event_properties.${product_url}}}` <br><br>URLの前にShopifyサイトのドメインを追加してください。 |
| `price`            | `{{event_properties.${price}}}`                     |
| `currency`         | `{{event_properties.${currency}}}`                  |
| `source`           | `{{event_properties.${source}}}`                    |
| `sku`              | `{{event_properties.${metadata}[0].sku}}`          |
| `type`             | `event_properties.${type}`          |
{: .reset-br-td-1 .reset-br-td-2 aria-label="トラッキングされるShopifyイベント" }
{% endraw %}

{% endsubtab %}
{% subtab Cart updated %}
**イベント**: `ecommerce.cart_updated`<br>
**タイプ**: 推奨イベント<br>
**トリガー**: 顧客がショッピングカートに商品を追加、削除、または更新したとき<br>
**データソース**: Braze SDK<br>
**ユースケース**: カート放棄

カート放棄キャンバスでは、まずメッセージ内でショッピングカートのコンテキストを取得するために、初期のショッピングカートLiquidタグを追加する必要があります。

{% raw %}
```liquid
{% shopping_cart {{context.${cart_id}}} %}
```
{% endraw %}

次に、以下のショッピングカートLiquidタグをメッセージに追加できます。

{% raw %}
| 変数         | Liquidテンプレーティング                                   |
|------------------|-----------------------------------------------------|
| `cart_id`          | `{{ shopping_cart.cart_id }}`                       |
| `currency`         | `{{ shopping_cart.currency }}`                      |
| `total_value`      | `{{ shopping_cart.total_value }}`                   |
| `product_id`       | `{{ shopping_cart.products[0].product_id }}`       |
| `product_name`     | `{{ shopping_cart.products[0].product_name }}`     |
| `variant_id`       | `{{ shopping_cart.products[0].variant_id }}`       |
| `image_url`        | `{{ shopping_cart.products[0].image_url }}`        |
| `product_url`      | `{{ shopping_cart.products[0].product_url }}`      |
| `quantity`         | `{{ shopping_cart.products[0].quantity }}`         |
| `price`            | `{{ shopping_cart.products[0].price }}`            |
| `sku`              | `{{ shopping_cart.products[0].metadata[0].sku }}`  |
| `source`           | `{{ shopping_cart.source }}`                        |
| `metadata (value)` | `{{ shopping_cart.metadata[0].<add_value_here> }}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="トラッキングされるShopifyイベント" }
{% endraw %}

{% alert tip %}
Liquidの`for`ループを使用してすべての商品をメールに動的に追加する方法の詳細については、[メール向けカート放棄商品パーソナライゼーション]({{site.baseurl}}/ecommerce_use_cases#abandoned-cart)を参照してください。
{% endalert %}

{% endsubtab %}
{% subtab Checkout started %}
**イベント**: `ecommerce.checkout_started`<br>
**タイプ**: 推奨イベント<br>
**トリガー**: ユーザーがチェックアウトページに移動したとき<br>
**データソース**: Braze REST API<br>
**ユースケース**: チェックアウト放棄

{% alert important %}
顧客が高速チェックアウトオプションとしてShop Payを使用した場合、Shopifyは標準的なチェックアウトイベント（Shopifyのチェックアウト開始Webhookなど）をバイパスすることがあります。これにより、Brazeがチェックアウトトークンエイリアスの追加に必要なデータを受信できない場合があり、チェックアウト放棄トラッキングやユーザープロファイルの照合に影響を与える可能性があります。
{% endalert %}

チェックアウト放棄キャンバスでは、まず以下のLiquidタグを使用する必要があります。

{% raw %}
```liquid
{% shopping_cart {{context.${cart_id}}} :abort_if_not_abandoned false %}
{{context.${cart_id}}}
```
{% endraw %}

次に、以下のLiquidタグをメッセージに追加して、チェックアウト時点のカート内の商品を参照できます。

{% raw %}
| 変数         | Liquidテンプレーティング                                   |
|------------------|-----------------------------------------------------|
| `cart_id`          | `{{ shopping_cart.cart_id }}`                       |
| `currency`         | `{{ shopping_cart.currency }}`                      |
| `total_value`      | `{{ shopping_cart.total_value }}`                   |
| `product_id`       | `{{ shopping_cart.products[0].product_id }}`       |
| `product_name`     | `{{ shopping_cart.products[0].product_name }}`     |
| `variant_id`       | `{{ shopping_cart.products[0].variant_id }}`       |
| `image_url`        | `{{ shopping_cart.products[0].image_url }}`        |
| `product_url`      | `{{ shopping_cart.products[0].product_url }}`      |
| `quantity`         | `{{ shopping_cart.products[0].quantity }}`         |
| `price`            | `{{ shopping_cart.products[0].price }}`            |
| `sku`              | `{{ shopping_cart.products[0].metadata.sku }}`     |
| `source`           | `{{ shopping_cart.source }}`                        |
| `checkout_url`     | `{{ shopping_cart.metadata[0].checkout_url }}`     |
{: .reset-br-td-1 .reset-br-td-2 aria-label="トラッキングされるShopifyイベント" }
{% endraw %}

{% endsubtab %}
{% subtab Order placed %}
**イベント**: `ecommerce.order_placed`<br>
**タイプ**: 推奨イベント<br>
**トリガー**: ユーザーがチェックアウトプロセスを正常に完了し、注文を確定したとき<br>
**データソース**: Braze REST API<br>
**ユースケース**: 注文確認、購入後リターゲティング、アップセルまたはクロスセル

{% raw %}
| 変数                | Liquidテンプレーティング                                   |
|-------------------------|-----------------------------------------------------|
| cart_id                 | `{{event_properties.${cart_id}}}`                   |
| currency                | `{{event_properties.${currency}}}`                  |
| discounts               | `{{event_properties.${discounts}}}`                 |
| order_id                | `{{event_properties.${order_id}}}`                  |
| product_id              | `{{event_properties.${products}[0].product_id}}`   |
| product_name            | `{{event_properties.${products}[0].product_name}}` |
| variant_id              | `{{event_properties.${products}[0].variant_id}}`   |
| quantity                | `{{event_properties.${products}[0].quantity}}`     |
| sku                     | `{{event_properties.${products}[0].metadata.sku}}` |
| total_discounts         | `{{event_properties.${total_discounts}}}`           |
| order_status_url        | `{{event_properties.${metadata}.order_status_url}}` |
| order_number            | `{{event_properties.${metadata}.order_number}}`     |
| tags                    | `{{event_properties.${metadata}.tags}}`             |
| referring_site          | `{{event_properties.${metadata}.referring_site}}`   |
| payment_gateway_names    | `{{event_properties.${metadata}.payment_gateway_names}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="トラッキングされるShopifyイベント" }
{% endraw %}

{% alert tip %}
Shopifyのチェックアウト完了Webhookには、商品URLや画像URLが含まれていません。そのため、[メール向けカート放棄商品パーソナライゼーション]({{site.baseurl}}/ecommerce_use_cases#order-confirmation-and-feedback-survey)で説明されているように、カタログLiquidパーソナライゼーションを使用する必要があります。
{% endalert %}

{% endsubtab %}
{% subtab Fulfilled order %}
**イベント**: `shopify_fulfilled_order`<br>
**タイプ**: [カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events)<br>
**トリガー**: ユーザーの注文がフルフィルメントされ、出荷準備が完了したとき<br>
**データソース**: Braze REST API<br>
**ユースケース**: （トランザクション）フルフィルメント更新

{% raw %}
| 変数 | Liquidテンプレーティング |
| --- | --- |
| 注文ID | `{{event_properties.${order_id}}}` |
| 合計金額 | `{{event_properties.${total_price}}}` |
| 合計割引 | `{{event_properties.${total_discounts}}}` |
| 確認ステータス | `{{event_properties.${confirmed}}}` |
| 注文ステータスURL | `{{event_properties.${order_status_url}}}` |
| 注文番号 | `{{event_properties.${order_number}}}` |
| キャンセルタイムスタンプ | `{{event_properties.${cancelled_at}}}` |
| クローズタイムスタンプ | `{{event_properties.${closed_at}}}` |
| アイテムID | `{{event_properties.${line_items}[0].product_id}}` |
| アイテム数量 | `{{event_properties.${line_items}[0].quantity}}` |
| アイテムSKU | `{{event_properties.${line_items}[0].sku}}` |
| アイテムタイトル | `{{event_properties.${line_items}[0].title}}` |
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
| アイテム名 | `{{event_properties.${line_items}[0].name}}` |
| アイテムプロパティ | `{{event_properties.${line_items}[0].properties}}` |
| アイテム価格 | `{{event_properties.${line_items}[0].price}}` |
| 配送タイトル | `{{event_properties.${shipping}[0].title}}` |
| 配送料 | `{{event_properties.${shipping}[0].price}}` |
| フルフィルメントステータス | `{{event_properties.${fulfillment_status}}}` |
| フルフィルメント出荷ステータス | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| ステータス | `{{event_properties.${fulfillments}[0].status}}` |
| フルフィルメント配送会社 | `{{event_properties.${fulfillments}[0].Fulfillment tracking_company}}` |
| フルフィルメント追跡番号 | `{{event_properties.${fulfillments}[0].Fulfillment tracking_number}}` |
| フルフィルメント追跡番号（複数） | `{{event_properties.${fulfillments}[0].Fulfillment tracking_numbers}}` |
| フルフィルメント追跡URL | `{{event_properties.${fulfillments}[0].Fulfillment tracking_url}}` |
| フルフィルメント追跡URL（複数） | `{{event_properties.${fulfillments}[0].Fulfillment tracking_urls}}` |
| フルフィルメントステータス | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| フルフィルメント名 | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| フルフィルメント価格 | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| フルフィルメント商品ID | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| フルフィルメント数量 | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| フルフィルメント配送 | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| フルフィルメントSKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| フルフィルメントタイトル | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| フルフィルメントベンダー | `{{event_properties.${fulfillments}[0].line_items[0].vendor}}` |
| バリアントID | `{{event_properties.${line_items}[0].variant_id}}` |
| バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="トラッキングされるShopifyイベント" }
{% endraw %}

{% endsubtab %}
{% subtab Partially fulfilled order %}
**イベント**: `shopify_partially_fulfilled_order`<br>
**タイプ**: [カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events)<br>
**トリガー**: ユーザーの注文の一部がフルフィルメントされ、出荷準備が完了したとき<br>
**データソース**: Braze REST API<br>
**ユースケース**: （トランザクション）フルフィルメント更新

{% raw %}
| 変数 | Liquidテンプレーティング |
| --- | --- |
| 注文ID | `{{event_properties.${order_id}}}` |
| 合計金額 | `{{event_properties.${total_price}}}` |
| 合計割引 | `{{event_properties.${total_discounts}}}` |
| 確認ステータス | `{{event_properties.${confirmed}}}` |
| 注文ステータスURL | `{{event_properties.${order_status_url}}}` |
| 注文番号 | `{{event_properties.${order_number}}}` |
| キャンセルタイムスタンプ | `{{event_properties.${cancelled_at}}}` |
| クローズタイムスタンプ | `{{event_properties.${closed_at}}}` |
| アイテムID | `{{event_properties.${line_items}[0].product_id}}` |
| アイテム数量 | `{{event_properties.${line_items}[0].quantity}}` |
| アイテムSKU | `{{event_properties.${line_items}[0].sku}}` |
| アイテムタイトル | `{{event_properties.${line_items}[0].title}}` |
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
| アイテム名 | `{{event_properties.${line_items}[0].name}}` |
| アイテムプロパティ | `{{event_properties.${line_items}[0].properties}}` |
| アイテム価格 | `{{event_properties.${line_items}[0].price}}` |
| 配送タイトル | `{{event_properties.${shipping}[0].title}}` |
| 配送料 | `{{event_properties.${shipping}[0].price}}` |
| フルフィルメントステータス | `{{event_properties.${fulfillment_status}}}` |
| フルフィルメント出荷ステータス | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| フルフィルメントステータス | `{{event_properties.${fulfillments}[0].status}}` |
| フルフィルメント配送会社 | `{{event_properties.${fulfillments}[0].tracking_company}}` |
| フルフィルメント追跡番号 | `{{event_properties.${fulfillments}[0].tracking_number}}` |
| フルフィルメント追跡番号（複数） | `{{event_properties.${fulfillments}[0].tracking_numbers}}` |
| フルフィルメント追跡URL | `{{event_properties.${fulfillments}[0].tracking_url}}` |
| フルフィルメント追跡URL（複数） | `{{event_properties.${fulfillments}[0].tracking_urls}}` |
| フルフィルメントステータス | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| フルフィルメント名 | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| フルフィルメント価格 | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| フルフィルメント商品ID | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| フルフィルメント数量 | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| フルフィルメント配送 | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| フルフィルメントSKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| フルフィルメントタイトル | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| フルフィルメントベンダー | `{{event_properties.${fulfillments}[0].line_items[0].vendor}}` |
| バリアントID | `{{event_properties.${line_items}[0].variant_id}}` |
| バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="トラッキングされるShopifyイベント" }
{% endraw %}

{% endsubtab %}
{% subtab Paid order %}
**イベント**: `shopify_paid_order`<br>
**タイプ**: [カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events)<br>
**トリガー**: ユーザーの注文がShopify内で支払い済みとしてマークされたとき<br>
**データソース**: Braze REST API<br>
**ユースケース**: （トランザクション）支払い確認

{% raw %}
| 変数 | Liquidテンプレーティング |
| --- | --- |
| 注文ID | `{{event_properties.${order_id}}}` |
| 確認ステータス | `{{event_properties.${confirmed}}}` |
| 注文ステータスURL | `{{event_properties.${order_status_url}}}` |
| 注文番号 | `{{event_properties.${order_number}}}` |
| キャンセルタイムスタンプ | `{{event_properties.${cancelled_at}}}` |
| 合計割引 | `{{event_properties.${total_discounts}}}` |
| 合計金額 | `{{event_properties.${total_price}}}` |
| タグ | `{{event_properties.${tags}}}` |
| ディスカウントコード | `{{event_properties.${discount_codes}}}` |
| アイテムID | `{{event_properties.${line_items}[0].product_id}}` |
| アイテム数量 | `{{event_properties.${line_items}[0].quantity}}` |
| アイテムSKU | `{{event_properties.${line_items}[0].sku}}` |
| アイテムタイトル | `{{event_properties.${line_items}[0].title}}` |
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
| アイテムプロパティ | `{{event_properties.${line_items}[0].properties}}` |
| アイテム価格 | `{{event_properties.${line_items}[0].price}}` |
| 配送タイトル | `{{event_properties.${shipping}[0].title}}` |
| 配送料 | `{{event_properties.${shipping}[0].price}}` |
| バリアントID | `{{event_properties.${line_items}[0].variant_id}}` |
| バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="トラッキングされるShopifyイベント" }
{% endraw %}

{% endsubtab %}
{% subtab Order cancelled %}
**イベント**: `ecommerce.order_cancelled`<br>
**タイプ**: 推奨イベント<br>
**トリガー**: ユーザーの注文がキャンセルされたとき<br>
**データソース**: Braze REST API<br>
**ユースケース**: （トランザクション）注文キャンセル確認

{% raw %}
| 変数 | Liquidテンプレーティング |
| --- | --- |
| 注文ID | `{{event_properties.${order_id}}}` |
| 合計金額 | `{{event_properties.${total_price}}}` |
| 合計割引 | `{{event_properties.${total_discounts}}}` |
| 確認済み | `{{event_properties.${confirmed}}}` |
| 注文ステータスURL | `{{event_properties.${order_status_url}}}` |
| 注文番号 | `{{event_properties.${order_number}}}` |
| キャンセルタイムスタンプ | `{{event_properties.${cancelled_at}}}` |
| タグ | `{{event_properties.${tags}}}` |
| ディスカウントコード | `{{event_properties.${discount_codes}}}` |
| フルフィルメントステータス | `{{event_properties.${fulfillment_status}}}` |
| フルフィルメント | `{{event_properties.${fulfillments}}}` |
| アイテムID | `{{event_properties.${line_items}[0].product_id}}` |
| アイテム数量 | `{{event_properties.${line_items}[0].quantity}}` |
| アイテムSKU | `{{event_properties.${line_items}[0].sku}}` |
| アイテムタイトル | `{{event_properties.${line_items}[0].title}}` |
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
| アイテム名 | `{{event_properties.${line_items}[0].name}}` |
| アイテムプロパティ | `{{event_properties.${line_items}[0].properties}}` |
| フルフィルメントステータス | `{{event_properties.${line_items}[0].fulfillment_status}}` |
| 配送タイトル | `{{event_properties.${shipping}[0].title}}` |
| 配送料 | `{{event_properties.${shipping}[0].price}}` |
| バリアントID | `{{event_properties.${line_items}[0].variant_id}}` |
| バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="トラッキングされるShopifyイベント" }
{% endraw %}
{% endsubtab %}
{% subtab Order refunded %}
**イベント**: `ecommerce.order_refunded`<br>
**タイプ**: 推奨イベント<br>
**トリガー**: ユーザーの注文が返金されたとき<br>
**データソース**: Braze REST API<br>
**ユースケース**: （トランザクション）返金確認

{% raw %}
| 変数 | Liquidテンプレーティング |
| --- | --- |
| 注文ID | `{{event_properties.${order_id}}}` |
| 注文メモ | `{event_properties.${note}}}` |
| アイテムID | `{{event_properties.${line_items}[0].product_id}}` |
| アイテム数量 | `{{event_properties.${line_items}[0].quantity}}` |
| アイテムSKU | `{{event_properties.${line_items}[0].sku}}` |
| アイテムタイトル | `{{event_properties.${line_items}[0].title}}` |
| アイテムベンダー | `{{event_properties.${line_items}[0].vendor}}` |
| アイテム名 | `{{event_properties.${line_items}[0].name}}` |
| アイテムプロパティ | `{{event_properties.${line_items}[0].properties}}` |
| アイテム価格 | `{{event_properties.${line_items}[0].price}}` |
| バリアントID | `{{event_properties.${line_items}[0].variant_id}}` |
| バリアントタイトル | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="トラッキングされるShopifyイベント" }
{% endraw %}

{% endsubtab %}
{% subtab Account login %}

**イベント**: `shopify_account_login`<br>
**タイプ**: [カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events)<br>
**トリガー**: ユーザーがアカウントにログインしたとき<br>
**データソース**: Braze REST API<br>
**ユースケース**: ウェルカムシリーズ

{% raw %}
| 変数 | Liquidテンプレーティング |
| --- | --- |
| `source` | {{event_properties.${source}}} |
{: .reset-br-td-1 .reset-br-td-2 aria-label="トラッキングされるShopifyイベント" }
{% endraw %}

{% alert note %}
Shopify連携は現在、Brazeの[購入イベント]({{site.baseurl}}/user_guide/data/activation/events/purchase_events)への入力をサポートしていません。そのため、購入フィルター、Liquidタグ、アクションベースのトリガー、および分析には`ecommerce.order_placed`イベントを使用してください。
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## サポートされているShopifyカスタム属性 {#supported-shopify-custom-attributes}

{% multi_lang_include alerts/note_alerts.md alert='Shopify attributes REST API' %}

{% tabs local %}
{% tab ペイロードの例 %}
{% subtabs %}
{% subtab Shopify Tags %}
```json
{
  "attributes": [
    {
      "shopify_tags": "VIP_customer",
      "shopify_total_spent": "60.00",
      "shopify_order_count": "3",
      "shopify_last_order_id": "1234567",
      "shopify_last_order_name": "test_order",
      "shopify_zipcode": "10001",
      "shopify_province": "null"
    }
  ]
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Shopifyカスタム属性 %}
| 属性名 | 説明 |
| --- | --- |
| `shopify_total_spent` | 顧客が注文履歴全体を通じて費やした合計金額です。 |
| `shopify_order_count` | この顧客に関連付けられている注文の数です。テスト注文やアーカイブ済みの注文はカウントされません。 |
| `shopify_last_order_id` | 顧客の最新の注文のIDです。 |
| `shopify_last_order_name` | 顧客の最新の注文の名前です。これは注文リソースの`name`フィールドに直接関連しています。 |
| `shopify_zipcode` | 顧客のデフォルト住所の郵便番号です。 |
| `shopify_province` | 顧客のデフォルト住所の都道府県です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="サポートされているShopifyカスタム属性" }

{% alert important %}
現在のShopify APIバージョンには既知の問題があり、`shopify_last_order_name`ユーザー属性が正しく入力されません。ユーザーへの影響は以下のとおりです。<br><br>

- **既存ユーザー：** `shopify_last_order_name`にすでに値が設定されているユーザーの場合、その値は保持されますが、その後の注文によって更新されません。
- **新規ユーザー：** 新規ユーザーの場合、このフィールドは入力されず、空またはnullのままになります。

Shopifyがこの問題を解決した後、このページは更新されます。
{% endalert %}

### Liquidパーソナライゼーション {#liquid-personalization}

Shopifyカスタム属性のLiquidパーソナライゼーションを追加するには、**+ パーソナライゼーション**を選択します。次に、パーソナライゼーションタイプとして**カスタム属性**を選択します。

![「属性」ドロップダウンが展開された「パーソナライゼーションを追加」セクション。]({% image_buster /assets/img/shopify/add_personalization_2.png %}){: style="max-width:40%;"}

カスタム属性を選択したら、デフォルト値を入力し、Liquidスニペットをメッセージにコピーします。

![メッセージにLiquidスニペットを貼り付ける。]({% image_buster /assets/img/shopify/copy_liquid_snippet.png %})
{% endtab %}
{% endtabs %}

## サポートされているShopify標準属性 {#supported-shopify-standard-attributes}

{% multi_lang_include alerts/note_alerts.md alert='Shopify attributes REST API' %}

- メール
- 名
- 姓
- 電話番号
- 市区町村
- 国

{% alert note %}
Brazeは、既存のユーザープロファイルのデータと差異がある場合にのみ、サポートされているShopifyカスタム属性およびBraze標準属性を更新します。例えば、受信したShopifyデータに名が「Bob」と含まれており、Brazeユーザープロファイルにすでに名として「Bob」が存在している場合、Brazeは更新をトリガーせず、データポイントも消費されません。
{% endalert %}

## SDKデータ収集 {#sdk-data-collection}

BrazeのSDKによって収集されるデータの詳細については、[SDKデータ収集]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection)を参照してください。

## 過去データのバックフィル {#historical-backfill}

> 過去のShopifyデータは、Brazeを接続する前からインポートされます。過去90日間の注文イベントと、過去1年間の顧客データが対象です。どちらの期間も、インテグレーションを完了した日から遡って計算されます。

[Shopify標準インテグレーション設定]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration)または[Shopifyカスタムインテグレーション設定]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration)を通じて、過去データのバックフィルを有効にすることで、過去の顧客をターゲットにできます。これにより、過去90日間のShopify注文（注文関連イベント）と過去1年間のユーザープロファイルがインポートされます。どちらの期間も、インテグレーションを完了した日から遡って計算されます。

BrazeがShopifyの顧客をインポートする際、設定で選択した`external_id`タイプが割り当てられます。

{% alert note %}
既存のBrazeユーザーでアクティブなキャンペーンやキャンバスがある場合は、過去データのバックフィルを有効にする前に、インポートされた顧客と注文イベントがセグメントやジャーニーにどのような影響を与えるかを確認してください。
{% endalert %}

{% multi_lang_include partners/shopify.md section='Custom external ID historical backfill' %}

### Shopify過去データバックフィルの設定 {#setting-up-shopify-historical-backfill}

1. **Track Shopify data**ステップで過去データのバックフィルを有効にします。

![過去データのバックフィルが選択されたShopifyインテグレーションの「Track Shopify data」ステップ。]({% image_buster /assets/img/shopify/historical_data_backfill_sync.png %})

{: start="2"}

2. インテグレーションの設定が完了すると、Brazeが初回データ同期を開始します。進捗状況はインテグレーション設定の**Shopify Data**タブで確認できます。

![イベントが同期中であることを示すスピナーが表示されたShopifyインテグレーション設定ページ。]({% image_buster /assets/img/shopify/historical_data_backfill_syncing.png %})

### 同期されるデータ {#synced-data}

初回データ同期では、Brazeはインテグレーション完了日から遡って過去90日間の注文イベントと過去1年間のユーザープロファイルをインポートします。BrazeがShopifyの顧客をインポートする際、設定で選択した`external_id`タイプが割り当てられます。

以下の表は、初回読み込みに含まれるデータをまとめたものです。

| Braze推奨イベント | Shopifyカスタムイベント | Braze標準属性項目 | Braze購読ステータス |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li>Order placed</li><li>Order cancelled</li><li>Order refunded</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li><li>shopify_province</li></ul>{:/} | {::nomarkdown}<ul><li>Email</li><li>First Name</li><li>Last Name</li><li>Phone</li><li>City</li><li>Country</li><li>Total Revenue</li><li>Total Refunds</li><li>Total Orders</li></ul>{:/} | {::nomarkdown}<ul><li>このShopifyストアに関連付けられたメールマーケティングの購読</li><li>このShopifyストアに関連付けられたSMSマーケティングの購読</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="同期されるデータ" }