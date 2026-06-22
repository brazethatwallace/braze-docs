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

## 追跡対象のShopifyイベント {#tracked-shopify-events}

Shopifyインテグレーションでは、[eコマース推奨イベント]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events/)を使用して、主要な買い物行動をキャプチャします。これらのイベントを使用した実装例やマーケティング戦略については、[eコマースユースケース]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases/)を参照してください。

{% multi_lang_include alerts/important_alerts.md alert='Shopify customer create' %}

{% tabs %}
{% tab ペイロード例 %}
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
{% subtabs global %}
{% subtab Product viewed %}
**イベント**: `ecommerce.product_viewed`<br>
**タイプ**: 推奨イベント<br>
**トリガー**: 顧客が製品ページを閲覧したとき<br>
**データソース**: Braze SDK<br>
**ユースケース**: ブラウズ放棄

{% raw %}
| 変数 | Liquidテンプレート |
| --- | --- |
|------------------|-----------------------------------------------------|
| `product_id`       | `{{event_properties.${product_id}}}`                |
| `product_name `    | `{{event_properties.${product_name}}}`              |
| `variant_id`       | `{{event_properties.${variant_id}}}`                |
| `image_url `       | `{{event_properties.${image_url}}}`                 |
| `product_url`      | `<your-store.myshopify.com>{{event_properties.${product_url}}}` <br><br>URLの前にShopifyサイトドメインを追加してください。 |
| `price`            | `{{event_properties.${price}}}`                     |
| `currency`         | `{{event_properties.${currency}}}`                  |
| `source`           | `{{event_properties.${source}}}`                    |
| `sku`              | `{{event_properties.${metadata}[0].sku}}`          |
| `type`             | `event_properties.${type}`          |
{: .reset-br-td-1 .reset-br-td-2 aria-label="追跡対象のShopifyイベント" }
{% endraw %}

{% endsubtab %}
{% subtab Cart updated %}
**イベント**: `ecommerce.cart_updated`<br>
**タイプ**: 推奨イベント<br>
**トリガー**: 顧客がショッピングカートに商品を追加、削除、または更新したとき<br>
**データソース**: Braze SDK<br>
**ユースケース**: カート放棄

放棄カートCanvasでは、まず最初のショッピングカートのLiquidタグを追加して、メッセージ内のショッピングカートのコンテキストを取得する必要があります。

{% raw %}
```liquid
{% shopping_cart {{context.${cart_id}}} %}
```
{% endraw %}

次に、以下のショッピングカートのLiquidタグをメッセージに追加できます。

{% raw %}
| 変数         | Liquidテンプレート                                   |
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
{: .reset-br-td-1 .reset-br-td-2 aria-label="追跡対象のShopifyイベント" }
{% endraw %}

{% alert tip %}
Liquidの`for`ループを構築してすべての製品をメールにダイナミックに追加する方法の詳細については、[メール用の放棄カート商品パーソナライゼーション]({{site.baseurl}}/ecommerce_use_cases/#abandoned-cart)を参照してください。
{% endalert %}

{% endsubtab %}
{% subtab Checkout started %}
**イベント**: `ecommerce.checkout_started`<br>
**タイプ**: 推奨イベント<br>
**トリガー**: ユーザーがチェックアウトページに移動したとき<br>
**データソース**: Braze REST API<br>
**ユースケース**: チェックアウト放棄

{% alert important %}
顧客がShop Payを高速チェックアウトオプションとして使用した場合、Shopifyは特定の標準チェックアウトイベント（Shopifyチェックアウト開始Webhookなど）をスキップすることがあります。これにより、Brazeがチェックアウトトークンエイリアスの追加に必要なデータを受信できず、チェックアウト放棄のトラッキングやユーザープロファイルの照合に影響を与える可能性があります。
{% endalert %}

放棄チェックアウトCanvasでは、まず次のLiquidタグを使用する必要があります。

{% raw %}
```liquid
{% shopping_cart {{context.${cart_id}}} :abort_if_not_abandoned false %}
{{context.${cart_id}}}
```
{% endraw %}

次に、以下のLiquidタグをメッセージに追加して、チェックアウト時のカート内の商品を参照できます。

{% raw %}
| 変数         | Liquidテンプレート                                   |
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
{: .reset-br-td-1 .reset-br-td-2 aria-label="追跡対象のShopifyイベント" }
{% endraw %}

{% endsubtab %}
{% subtab Order placed %}
**イベント**: `ecommerce.order_placed`<br>
**タイプ**: 推奨イベント<br>
**トリガー**: ユーザーがチェックアウトプロセスを正常に完了し、注文を確定したとき<br>
**データソース**: Braze REST API<br>
**ユースケース**: 注文確認、購入後リターゲティング、アップセルまたはクロスセル

{% raw %}
| 変数                | Liquidテンプレート                                   |
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
{: .reset-br-td-1 .reset-br-td-2 aria-label="追跡対象のShopifyイベント" }
{% endraw %}

{% alert tip %}
Shopifyのチェックアウト完了Webhookには、商品URLや画像URLが含まれていません。そのため、[メール用の注文確認とフィードバック調査]({{site.baseurl}}/ecommerce_use_cases/#order-confirmation-and-feedback-survey)で説明されているように、カタログLiquidパーソナライゼーションを使用する必要があります。
{% endalert %}

{% endsubtab %}
{% subtab Fulfilled order %}
**イベント**: `shopify_fulfilled_order`<br>
**タイプ**: [カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events/)<br>
**トリガー**: ユーザーの注文がフルフィルメントされ、発送の準備ができたとき<br>
**データソース**: Braze REST API<br>
**ユースケース**: （トランザクション）フルフィルメントの更新

{% raw %}
| 変数 | Liquidテンプレート |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Total Discounts | `{{event_properties.${total_discounts}}}` |
| Confirmed Status | `{{event_properties.${confirmed}}}` |
| Order Status URL | `{{event_properties.${order_status_url}}}` |
| Order Number | `{{event_properties.${order_number}}}` |
| Cancelled Timestamp | `{{event_properties.${cancelled_at}}}` |
| Closed Timestamp | `{{event_properties.${closed_at}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Name | `{{event_properties.${line_items}[0].name}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
| Shipping Title | `{{event_properties.${shipping}[0].title}}` |
| Shipping Price | `{{event_properties.${shipping}[0].price}}` |
| Fulfillment Status | `{{event_properties.${fulfillment_status}}}` |
| Fulfillment Shipment Status | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| Status | `{{event_properties.${fulfillments}[0].status}}` |
| Fulfillment Tracking Company | `{{event_properties.${fulfillments}[0].Fulfillment tracking_company}}` |
| Fulfillment Tracking Number | `{{event_properties.${fulfillments}[0].Fulfillment tracking_number}}` |
| Fulfillment Tracking Numbers | `{{event_properties.${fulfillments}[0].Fulfillment tracking_numbers}}` |
| Fulfillment Tracking URL | `{{event_properties.${fulfillments}[0].Fulfillment tracking_url}}` |
| Fulfillment Tracking URLs | `{{event_properties.${fulfillments}[0].Fulfillment tracking_urls}}` |
| Fulfillment Status | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| Fulfillment Name | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| Fulfillment Price | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| Fulfillment Product ID | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| Fulfillment Quantity | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| Fulfillment Shipping | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| Fulfillment SKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| Fulfillment Title | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| Fulfillment Vendor | `{{event_properties.${fulfillments}[0].line_items[0].vendor}}` |
| Variant ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variant Title | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="追跡対象のShopifyイベント" }
{% endraw %}

{% endsubtab %}
{% subtab Partially fulfilled order %}
**イベント**: `shopify_partially_fulfilled_order`<br>
**タイプ**: [カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events/)<br>
**トリガー**: ユーザーの注文の一部がフルフィルメントされ、発送の準備ができたとき<br>
**データソース**: Braze REST API<br>
**ユースケース**: （トランザクション）フルフィルメントの更新

{% raw %}
| 変数 | Liquidテンプレート |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Total Discounts | `{{event_properties.${total_discounts}}}` |
| Confirmed Status | `{{event_properties.${confirmed}}}` |
| Order Status URL | `{{event_properties.${order_status_url}}}` |
| Order Number | `{{event_properties.${order_number}}}` |
| Cancelled Timestamp | `{{event_properties.${cancelled_at}}}` |
| Closed Timestamp | `{{event_properties.${closed_at}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Name | `{{event_properties.${line_items}[0].name}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
| Shipping Title | `{{event_properties.${shipping}[0].title}}` |
| Shipping Price | `{{event_properties.${shipping}[0].price}}` |
| Fulfillment Status | `{{event_properties.${fulfillment_status}}}` |
| Fulfillment Shipment Status | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| Fulfillment Status | `{{event_properties.${fulfillments}[0].status}}` |
| Fulfillment Tracking Company | `{{event_properties.${fulfillments}[0].tracking_company}}` |
| Fulfillment Tracking Number | `{{event_properties.${fulfillments}[0].tracking_number}}` |
| Fulfillment Tracking Numbers | `{{event_properties.${fulfillments}[0].tracking_numbers}}` |
| Fulfillment Tracking URL | `{{event_properties.${fulfillments}[0].tracking_url}}` |
| Fulfillment Tracking URLs | `{{event_properties.${fulfillments}[0].tracking_urls}}` |
| Fulfillment Status | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| Fulfillment Name | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| Fulfillment Price | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| Fulfillment Product ID | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| Fulfillment Quantity | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| Fulfillment Shipping | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| Fulfillment SKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| Fulfillment Title | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| Fulfillment Vendor | `{{event_properties.${fulfillments}[0].line_items[0].vendor}}` |
| Variant ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variant Title | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="追跡対象のShopifyイベント" }
{% endraw %}

{% endsubtab %}
{% subtab Paid order %}
**イベント**: `shopify_paid_order`<br>
**タイプ**: [カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events/)<br>
**トリガー**: ユーザーの注文がShopify内で支払い済みとマークされたとき<br>
**データソース**: Braze REST API<br>
**ユースケース**: （トランザクション）支払い確認

{% raw %}
| 変数 | Liquidテンプレート |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Confirmed Status | `{{event_properties.${confirmed}}}` |
| Order Status URL | `{{event_properties.${order_status_url}}}` |
| Order Number | `{{event_properties.${order_number}}}` |
| Cancelled Timestamp | `{{event_properties.${cancelled_at}}}` |
| Total Discounts | `{{event_properties.${total_discounts}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Tags | `{{event_properties.${tags}}}` |
| Discount Codes | `{{event_properties.${discount_codes}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
| Shipping Title | `{{event_properties.${shipping}[0].title}}` |
| Shipping Price | `{{event_properties.${shipping}[0].price}}` |
| Variant ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variant Title | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="追跡対象のShopifyイベント" }
{% endraw %}

{% endsubtab %}
{% subtab Order cancelled %}
**イベント**: `ecommerce.order_cancelled`<br>
**タイプ**: 推奨イベント<br>
**トリガー**: ユーザーの注文がキャンセルされたとき<br>
**データソース**: Braze REST API<br>
**ユースケース**: （トランザクション）注文キャンセル確認

{% raw %}
| 変数 | Liquidテンプレート |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Total Price | `{{event_properties.${total_price}}}` |
| Total Discounts | `{{event_properties.${total_discounts}}}` |
| Confirmed | `{{event_properties.${confirmed}}}` |
| Order Status URL | `{{event_properties.${order_status_url}}}` |
| Order Number | `{{event_properties.${order_number}}}` |
| Cancelled Timestamp | `{{event_properties.${cancelled_at}}}` |
| Tags | `{{event_properties.${tags}}}` |
| Discount Codes | `{{event_properties.${discount_codes}}}` |
| Fulfillment Status | `{{event_properties.${fulfillment_status}}}` |
| Fulfillments | `{{event_properties.${fulfillments}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Name | `{{event_properties.${line_items}[0].name}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Fulfillment Status | `{{event_properties.${line_items}[0].fulfillment_status}}` |
| Shipping Title | `{{event_properties.${shipping}[0].title}}` |
| Shipping Price | `{{event_properties.${shipping}[0].price}}` |
| Variant ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variant Title | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="追跡対象のShopifyイベント" }
{% endraw %}
{% endsubtab %}
{% subtab Order refunded %}
**イベント**: `ecommerce.order_refunded`<br>
**タイプ**: 推奨イベント<br>
**トリガー**: ユーザーの注文が返金されたとき<br>
**データソース**: Braze REST API<br>
**ユースケース**: （トランザクション）返金確認

{% raw %}
| 変数 | Liquidテンプレート |
| --- | --- |
| Order ID | `{{event_properties.${order_id}}}` |
| Order Note | `{event_properties.${note}}}` |
| Item ID | `{{event_properties.${line_items}[0].product_id}}` |
| Item Quantity | `{{event_properties.${line_items}[0].quantity}}` |
| Item SKU | `{{event_properties.${line_items}[0].sku}}` |
| Item Title | `{{event_properties.${line_items}[0].title}}` |
| Item Vendor | `{{event_properties.${line_items}[0].vendor}}` |
| Item Name | `{{event_properties.${line_items}[0].name}}` |
| Item Properties | `{{event_properties.${line_items}[0].properties}}` |
| Item Price | `{{event_properties.${line_items}[0].price}}` |
| Variant ID | `{{event_properties.${line_items}[0].variant_id}}` |
| Variant Title | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="追跡対象のShopifyイベント" }
{% endraw %}

{% endsubtab %}
{% subtab Account login %}

**イベント**: `shopify_account_login`<br>
**タイプ**: [カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events/)<br>
**トリガー**: ユーザーがアカウントにログインしたとき<br>
**データソース**: Braze REST API<br>
**ユースケース**: ウェルカムシリーズ

{% raw %}
| 変数 | Liquidテンプレート |
| --- | --- |
| `source` | {{event_properties.${source}}} |
{: .reset-br-td-1 .reset-br-td-2 aria-label="追跡対象のShopifyイベント" }
{% endraw %}

{% alert note %}
現在、Shopifyインテグレーションでは、Brazeの[購入イベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#purchase-events)への入力はサポートされていません。そのため、購入フィルター、Liquidタグ、アクションベースのトリガー、および分析には`ecommerce.order_placed`イベントを使用してください。
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## サポートされているShopifyカスタム属性 {#supported-shopify-custom-attributes}

{% multi_lang_include alerts/note_alerts.md alert='Shopify attributes REST API' %}

{% tabs local %}
{% tab ペイロード例 %}
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
| `shopify_total_spent` | 注文履歴全体で顧客が支払った総額です。 |
| `shopify_order_count` | この顧客に関連する注文数です。テストオーダーとアーカイブオーダーはカウントされません。 |
| `shopify_last_order_id` | 顧客の最後の注文のIDです。 |
| `shopify_last_order_name` | 顧客の最後の注文の名前です。これは、注文リソースの`name`フィールドに直接関係しています。 |
| `shopify_zipcode` | 顧客のデフォルト住所の郵便番号です。 |
| `shopify_province` | 顧客のデフォルト住所の都道府県です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="サポートされているShopifyカスタム属性" }

{% alert important %}
現行のShopify APIバージョンに既知の問題があり、`shopify_last_order_name`ユーザー属性が正しく入力されません。ユーザーへの影響は以下のとおりです。<br><br>

- **既存ユーザー:** すでに`shopify_last_order_name`の値を持っているユーザーの場合、その値は保持されますが、後続の注文では更新されません。
- **新規ユーザー:** 新規ユーザーの場合、フィールドは入力されず、空またはnullのままになります。

このページは、Shopifyがこの問題を解決した後に更新されます。
{% endalert %}

### Liquidパーソナライゼーション {#liquid-personalization}

Shopifyカスタム属性にLiquidパーソナライゼーションを追加するには、**+ パーソナライゼーション**を選択します。次に、パーソナライゼーションタイプとして**カスタム属性**を選択します。

![「パーソナライゼーションの追加」セクションで「属性」ドロップダウンが展開されている画面]({% image_buster /assets/img/shopify/add_personalization_2.png %}){: style="max-width:40%;"}

カスタム属性を選択したら、デフォルト値を入力してLiquidスニペットをメッセージにコピーします。

![Liquidスニペットをメッセージに貼り付ける画面]({% image_buster /assets/img/shopify/copy_liquid_snippet.png %})
{% endtab %}
{% endtabs %}

## サポートされているShopify標準属性 {#supported-shopify-standard-attributes}

{% multi_lang_include alerts/note_alerts.md alert='Shopify attributes REST API' %}

- メール
- 名
- 姓
- 電話
- 市区町村
- 国

{% alert note %}
BrazeがサポートされているShopifyカスタム属性とBraze標準属性を更新するのは、既存のユーザープロファイルとデータに違いがある場合のみです。たとえば、インバウンドShopifyデータにBobという名前が含まれており、BobがBrazeのユーザープロファイルに名前としてすでに存在している場合、Brazeは更新をトリガーせず、データポイントは課金されません。
{% endalert %}

## SDKによるデータ収集 {#sdk-data-collection}

Braze SDKが収集するデータの詳細については、[SDKデータ収集]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection/)を参照してください。

## 履歴バックフィル {#historical-backfill}

> 履歴Shopifyデータは、Brazeを接続する前にインポートされます。過去90日間の注文イベントと過去1年間の顧客データが対象です。どちらの期間も、インテグレーションを完了した日から遡って計算されます。

[Shopify標準インテグレーション設定]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/)または[Shopifyカスタムインテグレーション設定]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration/)を通じて、履歴バックフィルをオンにし、過去の顧客をターゲットにできます。これにより、過去90日間のShopify注文（注文関連イベント）と過去1年間のユーザープロファイルがインポートされます。どちらの期間も、インテグレーションを完了した日から遡って計算されます。

BrazeがShopifyの顧客をインポートする際、設定で選択した`external_id`タイプを割り当てます。

{% alert note %}
アクティブなCampaignsやCanvasesを持つ既存のBrazeユーザーの場合、履歴バックフィルを有効にする前に、インポートされた顧客と注文イベントがSegmentsやジャーニーにどのように影響するかを確認してください。
{% endalert %}

{% multi_lang_include shopify.md section='Custom external ID historical backfill' %}

### Shopify履歴バックフィルの設定 {#setting-up-shopify-historical-backfill}

1. **Shopifyデータの追跡**ステップで、履歴バックフィルをオンにします。

![履歴バックフィルが選択されたShopifyインテグレーションの「Shopifyデータの追跡」ステップ]({% image_buster /assets/img/shopify/historical_data_backfill_sync.png %})

{: start="2"}

2. インテグレーション設定が完了すると、Brazeは初期データ同期を開始します。進捗状況は、インテグレーション設定の**Shopifyデータ**タブで確認できます。

![イベントがアクティブに同期中であることを示すスピナーが表示されたShopifyインテグレーション設定ページ]({% image_buster /assets/img/shopify/historical_data_backfill_syncing.png %})

### 同期データ {#synced-data}

初期データ同期では、Brazeは過去90日間の注文イベントと過去1年間のユーザープロファイルをインポートします。それぞれ、インテグレーションを完了した日から遡って計算されます。BrazeがShopifyの顧客をインポートする際、設定で選択した`external_id`タイプを割り当てます。

以下の表は、初期ロードに含まれるデータをまとめたものです。

| Braze推奨イベント | Shopifyカスタムイベント | Braze標準属性 | Brazeサブスクリプションステータス |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li>注文確定</li><li>注文キャンセル</li><li>注文返金</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li><li>shopify_province</li></ul>{:/} | {::nomarkdown}<ul><li>メール</li><li>名</li><li>姓</li><li>電話</li><li>市区町村</li><li>国</li><li>合計収益</li><li>合計返金</li><li>合計注文数</li></ul>{:/} | {::nomarkdown}<ul><li>このShopifyストアに関連するメールマーケティングサブスクリプション</li><li>このShopifyストアに関連するSMSマーケティングサブスクリプション</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="同期データ" }