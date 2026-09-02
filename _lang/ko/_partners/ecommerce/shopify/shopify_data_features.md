---
nav_title: Shopify 데이터 기능
article_title: Shopify 데이터 기능
description: "이 참조 문서에서는 Shopify 데이터 기능을 다룹니다."
page_type: partner
search_tag: Partner
alias: /shopify_data_features/
page_order: 4
---

# Shopify 데이터 기능 {#shopify-data-features}

> 이 문서에서는 추적되는 Shopify 데이터와 예시 페이로드, 과거 데이터 백필, 제품 동기화를 포함한 Shopify 기능에 대한 개요를 제공합니다.

## 추적되는 Shopify 이벤트 {#tracked-shopify-events}

Shopify 통합은 [이커머스 추천 이벤트]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events)를 사용하여 주요 쇼핑 행동을 캡처합니다. 이러한 이벤트를 활용한 구현 예시 및 마케팅 전략에 대해서는 [이커머스 사용 사례]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases)를 참조하세요.

{% multi_lang_include alerts/important_alerts.md alert='Shopify customer create' %}

{% tabs %}
{% tab 예시 페이로드 %}
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
{% tab Shopify 이벤트 %}

{% alert note %}
Braze는 이커머스 이벤트에 필요한 이벤트 속성정보(예: `cart_id` 또는 `cart_token`)를 Shopify에서 제공받습니다. 드물게 Shopify의 일시적인 문제로 인해 이러한 속성정보가 누락될 수 있으며, 이 경우 해당 이벤트가 삭제될 수 있습니다.
{% endalert %}

{% subtabs global %}
{% subtab Product viewed %}
**이벤트**: `ecommerce.product_viewed`<br>
**유형**: 추천 이벤트<br>
**트리거 조건**: 고객이 제품 페이지를 조회할 때<br>
**데이터 소스**: Braze SDK<br>
**사용 사례**: 브라우즈 유기

{% raw %}
| 변수 | Liquid 템플릿 |
| --- | --- |
|------------------|-----------------------------------------------------|
| `product_id`       | `{{event_properties.${product_id}}}`                |
| `product_name `    | `{{event_properties.${product_name}}}`              |
| `variant_id`       | `{{event_properties.${variant_id}}}`                |
| `image_url `       | `{{event_properties.${image_url}}}`                 |
| `product_url`      | `<your-store.myshopify.com>{{event_properties.${product_url}}}` <br><br>URL 앞에 Shopify 사이트 도메인을 추가하세요. |
| `price`            | `{{event_properties.${price}}}`                     |
| `currency`         | `{{event_properties.${currency}}}`                  |
| `source`           | `{{event_properties.${source}}}`                    |
| `sku`              | `{{event_properties.${metadata}[0].sku}}`          |
| `type`             | `event_properties.${type}`          |
{: .reset-br-td-1 .reset-br-td-2 aria-label="추적되는 Shopify 이벤트" }
{% endraw %}

{% endsubtab %}
{% subtab Cart updated %}
**이벤트**: `ecommerce.cart_updated`<br>
**유형**: 추천 이벤트<br>
**트리거 조건**: 고객이 장바구니에 항목을 추가, 제거 또는 업데이트할 때<br>
**데이터 소스**: Braze SDK<br>
**사용 사례**: 장바구니 유기

유기한 장바구니 Canvases의 경우 먼저 초기 장바구니 Liquid 태그를 추가하여 메시지에서 장바구니 컨텍스트를 확인해야 합니다.

{% raw %}
```liquid
{% shopping_cart {{context.${cart_id}}} %}
```
{% endraw %}

그런 다음 메시지에 다음 장바구니 Liquid 태그를 추가할 수 있습니다.

{% raw %}
| 변수         | Liquid 템플릿                                   |
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
{: .reset-br-td-1 .reset-br-td-2 aria-label="추적되는 Shopify 이벤트" }
{% endraw %}

{% alert tip %}
Liquid `for` 루프를 사용하여 이메일에 모든 제품을 동적으로 추가하는 방법에 대한 자세한 내용은 [이메일용 유기한 장바구니 제품 개인화]({{site.baseurl}}/ecommerce_use_cases#abandoned-cart)를 참조하세요.
{% endalert %}

{% endsubtab %}
{% subtab Checkout started %}
**이벤트**: `ecommerce.checkout_started`<br>
**유형**: 추천 이벤트<br>
**트리거 조건**: 사용자가 결제 페이지로 이동할 때<br>
**데이터 소스**: Braze REST API<br>
**사용 사례**: 결제 유기

{% alert important %}
고객이 Shop Pay를 빠른 결제 옵션으로 사용하는 경우, Shopify가 특정 표준 결제 이벤트(예: Shopify 결제 시작 웹훅)를 건너뛸 수 있습니다. 이 경우 Braze가 결제 토큰 별칭을 추가하는 데 필요한 데이터를 수신하지 못할 수 있으며, 결제 유기 추적 및 사용자 프로필 조정에 영향을 줄 수 있습니다.
{% endalert %}

유기한 결제 Canvases의 경우 먼저 다음 Liquid 태그를 사용해야 합니다:

{% raw %}
```liquid
{% shopping_cart {{context.${cart_id}}} :abort_if_not_abandoned false %}
{{context.${cart_id}}}
```
{% endraw %}

그런 다음 메시지에 다음 Liquid 태그를 추가하여 결제 시점의 장바구니 제품을 참조할 수 있습니다.

{% raw %}
| 변수         | Liquid 템플릿                                   |
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
{: .reset-br-td-1 .reset-br-td-2 aria-label="추적되는 Shopify 이벤트" }
{% endraw %}

{% endsubtab %}
{% subtab Order placed %}
**이벤트**: `ecommerce.order_placed`<br>
**유형**: 추천 이벤트<br>
**트리거 조건**: 사용자가 결제 프로세스를 성공적으로 완료하고 주문을 제출할 때<br>
**데이터 소스**: Braze REST API<br>
**사용 사례**: 주문 확인, 구매 후 리타겟팅, 업셀 또는 크로스셀

{% raw %}
| 변수                | Liquid 템플릿                                   |
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
{: .reset-br-td-1 .reset-br-td-2 aria-label="추적되는 Shopify 이벤트" }
{% endraw %}

{% alert tip %}
Shopify의 결제 완료 웹훅에는 제품 URL이나 이미지 URL이 포함되어 있지 않습니다. 따라서 [이메일용 유기한 장바구니 제품 개인화]({{site.baseurl}}/ecommerce_use_cases#order-confirmation-and-feedback-survey)에 설명된 대로 카탈로그 Liquid 개인화를 사용해야 합니다.
{% endalert %}

{% endsubtab %}
{% subtab Fulfilled order %}
**이벤트**: `shopify_fulfilled_order`<br>
**유형**: [커스텀 이벤트]({{site.baseurl}}/user_guide/data/activation/events/custom_events)<br>
**트리거 조건**: 사용자의 주문이 처리 완료되어 배송 준비가 되었을 때<br>
**데이터 소스**: Braze REST API<br>
**사용 사례**: (트랜잭션) 처리 상태 업데이트

{% raw %}
| 변수 | Liquid 템플릿 |
| --- | --- |
| 주문 ID | `{{event_properties.${order_id}}}` |
| 총 금액 | `{{event_properties.${total_price}}}` |
| 총 할인 | `{{event_properties.${total_discounts}}}` |
| 확인 상태 | `{{event_properties.${confirmed}}}` |
| 주문 상태 URL | `{{event_properties.${order_status_url}}}` |
| 주문 번호 | `{{event_properties.${order_number}}}` |
| 취소 타임스탬프 | `{{event_properties.${cancelled_at}}}` |
| 종료 타임스탬프 | `{{event_properties.${closed_at}}}` |
| 항목 ID | `{{event_properties.${line_items}[0].product_id}}` |
| 항목 수량 | `{{event_properties.${line_items}[0].quantity}}` |
| 항목 SKU | `{{event_properties.${line_items}[0].sku}}` |
| 항목 제목 | `{{event_properties.${line_items}[0].title}}` |
| 항목 판매자 | `{{event_properties.${line_items}[0].vendor}}` |
| 항목 이름 | `{{event_properties.${line_items}[0].name}}` |
| 항목 속성정보 | `{{event_properties.${line_items}[0].properties}}` |
| 항목 가격 | `{{event_properties.${line_items}[0].price}}` |
| 배송 제목 | `{{event_properties.${shipping}[0].title}}` |
| 배송 가격 | `{{event_properties.${shipping}[0].price}}` |
| 처리 상태 | `{{event_properties.${fulfillment_status}}}` |
| 처리 배송 상태 | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| 상태 | `{{event_properties.${fulfillments}[0].status}}` |
| 처리 배송 회사 | `{{event_properties.${fulfillments}[0].Fulfillment tracking_company}}` |
| 처리 운송장 번호 | `{{event_properties.${fulfillments}[0].Fulfillment tracking_number}}` |
| 처리 운송장 번호 목록 | `{{event_properties.${fulfillments}[0].Fulfillment tracking_numbers}}` |
| 처리 추적 URL | `{{event_properties.${fulfillments}[0].Fulfillment tracking_url}}` |
| 처리 추적 URL 목록 | `{{event_properties.${fulfillments}[0].Fulfillment tracking_urls}}` |
| 처리 상태 | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| 처리 이름 | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| 처리 가격 | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| 처리 제품 ID | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| 처리 수량 | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| 처리 배송 여부 | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| 처리 SKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| 처리 제목 | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| 처리 판매자 | `{{event_properties.${fulfillments}[0].line_items[0].vendor}}` |
| 배리언트 ID | `{{event_properties.${line_items}[0].variant_id}}` |
| 배리언트 제목 | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="추적되는 Shopify 이벤트" }
{% endraw %}

{% endsubtab %}
{% subtab Partially fulfilled order %}
**이벤트**: `shopify_partially_fulfilled_order`<br>
**유형**: [커스텀 이벤트]({{site.baseurl}}/user_guide/data/activation/events/custom_events)<br>
**트리거 조건**: 사용자 주문의 일부가 처리 완료되어 배송 준비가 되었을 때<br>
**데이터 소스**: Braze REST API<br>
**사용 사례**: (트랜잭션) 처리 상태 업데이트

{% raw %}
| 변수 | Liquid 템플릿 |
| --- | --- |
| 주문 ID | `{{event_properties.${order_id}}}` |
| 총 금액 | `{{event_properties.${total_price}}}` |
| 총 할인 | `{{event_properties.${total_discounts}}}` |
| 확인 상태 | `{{event_properties.${confirmed}}}` |
| 주문 상태 URL | `{{event_properties.${order_status_url}}}` |
| 주문 번호 | `{{event_properties.${order_number}}}` |
| 취소 타임스탬프 | `{{event_properties.${cancelled_at}}}` |
| 종료 타임스탬프 | `{{event_properties.${closed_at}}}` |
| 항목 ID | `{{event_properties.${line_items}[0].product_id}}` |
| 항목 수량 | `{{event_properties.${line_items}[0].quantity}}` |
| 항목 SKU | `{{event_properties.${line_items}[0].sku}}` |
| 항목 제목 | `{{event_properties.${line_items}[0].title}}` |
| 항목 판매자 | `{{event_properties.${line_items}[0].vendor}}` |
| 항목 이름 | `{{event_properties.${line_items}[0].name}}` |
| 항목 속성정보 | `{{event_properties.${line_items}[0].properties}}` |
| 항목 가격 | `{{event_properties.${line_items}[0].price}}` |
| 배송 제목 | `{{event_properties.${shipping}[0].title}}` |
| 배송 가격 | `{{event_properties.${shipping}[0].price}}` |
| 처리 상태 | `{{event_properties.${fulfillment_status}}}` |
| 처리 배송 상태 | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| 처리 상태 | `{{event_properties.${fulfillments}[0].status}}` |
| 처리 배송 회사 | `{{event_properties.${fulfillments}[0].tracking_company}}` |
| 처리 운송장 번호 | `{{event_properties.${fulfillments}[0].tracking_number}}` |
| 처리 운송장 번호 목록 | `{{event_properties.${fulfillments}[0].tracking_numbers}}` |
| 처리 추적 URL | `{{event_properties.${fulfillments}[0].tracking_url}}` |
| 처리 추적 URL 목록 | `{{event_properties.${fulfillments}[0].tracking_urls}}` |
| 처리 상태 | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| 처리 이름 | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| 처리 가격 | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| 처리 제품 ID | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| 처리 수량 | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| 처리 배송 여부 | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| 처리 SKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| 처리 제목 | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| 처리 판매자 | `{{event_properties.${fulfillments}[0].line_items[0].vendor}}` |
| 배리언트 ID | `{{event_properties.${line_items}[0].variant_id}}` |
| 배리언트 제목 | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="추적되는 Shopify 이벤트" }
{% endraw %}

{% endsubtab %}
{% subtab Paid order %}
**이벤트**: `shopify_paid_order`<br>
**유형**: [커스텀 이벤트]({{site.baseurl}}/user_guide/data/activation/events/custom_events)<br>
**트리거 조건**: Shopify에서 사용자의 주문이 결제 완료로 표시될 때<br>
**데이터 소스**: Braze REST API<br>
**사용 사례**: (트랜잭션) 결제 확인

{% raw %}
| 변수 | Liquid 템플릿 |
| --- | --- |
| 주문 ID | `{{event_properties.${order_id}}}` |
| 확인 상태 | `{{event_properties.${confirmed}}}` |
| 주문 상태 URL | `{{event_properties.${order_status_url}}}` |
| 주문 번호 | `{{event_properties.${order_number}}}` |
| 취소 타임스탬프 | `{{event_properties.${cancelled_at}}}` |
| 총 할인 | `{{event_properties.${total_discounts}}}` |
| 총 금액 | `{{event_properties.${total_price}}}` |
| 태그 | `{{event_properties.${tags}}}` |
| 할인 코드 | `{{event_properties.${discount_codes}}}` |
| 항목 ID | `{{event_properties.${line_items}[0].product_id}}` |
| 항목 수량 | `{{event_properties.${line_items}[0].quantity}}` |
| 항목 SKU | `{{event_properties.${line_items}[0].sku}}` |
| 항목 제목 | `{{event_properties.${line_items}[0].title}}` |
| 항목 판매자 | `{{event_properties.${line_items}[0].vendor}}` |
| 항목 속성정보 | `{{event_properties.${line_items}[0].properties}}` |
| 항목 가격 | `{{event_properties.${line_items}[0].price}}` |
| 배송 제목 | `{{event_properties.${shipping}[0].title}}` |
| 배송 가격 | `{{event_properties.${shipping}[0].price}}` |
| 배리언트 ID | `{{event_properties.${line_items}[0].variant_id}}` |
| 배리언트 제목 | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="추적되는 Shopify 이벤트" }
{% endraw %}

{% endsubtab %}
{% subtab Order cancelled %}
**이벤트**: `ecommerce.order_cancelled`<br>
**유형**: 추천 이벤트<br>
**트리거 조건**: 사용자의 주문이 취소될 때<br>
**데이터 소스**: Braze REST API<br>
**사용 사례**: (트랜잭션) 주문 취소 확인

{% raw %}
| 변수 | Liquid 템플릿 |
| --- | --- |
| 주문 ID | `{{event_properties.${order_id}}}` |
| 총 금액 | `{{event_properties.${total_price}}}` |
| 총 할인 | `{{event_properties.${total_discounts}}}` |
| 확인 여부 | `{{event_properties.${confirmed}}}` |
| 주문 상태 URL | `{{event_properties.${order_status_url}}}` |
| 주문 번호 | `{{event_properties.${order_number}}}` |
| 취소 타임스탬프 | `{{event_properties.${cancelled_at}}}` |
| 태그 | `{{event_properties.${tags}}}` |
| 할인 코드 | `{{event_properties.${discount_codes}}}` |
| 처리 상태 | `{{event_properties.${fulfillment_status}}}` |
| 처리 내역 | `{{event_properties.${fulfillments}}}` |
| 항목 ID | `{{event_properties.${line_items}[0].product_id}}` |
| 항목 수량 | `{{event_properties.${line_items}[0].quantity}}` |
| 항목 SKU | `{{event_properties.${line_items}[0].sku}}` |
| 항목 제목 | `{{event_properties.${line_items}[0].title}}` |
| 항목 판매자 | `{{event_properties.${line_items}[0].vendor}}` |
| 항목 이름 | `{{event_properties.${line_items}[0].name}}` |
| 항목 속성정보 | `{{event_properties.${line_items}[0].properties}}` |
| 처리 상태 | `{{event_properties.${line_items}[0].fulfillment_status}}` |
| 배송 제목 | `{{event_properties.${shipping}[0].title}}` |
| 배송 가격 | `{{event_properties.${shipping}[0].price}}` |
| 배리언트 ID | `{{event_properties.${line_items}[0].variant_id}}` |
| 배리언트 제목 | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="추적되는 Shopify 이벤트" }
{% endraw %}
{% endsubtab %}
{% subtab Order refunded %}
**이벤트**: `ecommerce.order_refunded`<br>
**유형**: 추천 이벤트<br>
**트리거 조건**: 사용자의 주문이 환불될 때<br>
**데이터 소스**: Braze REST API<br>
**사용 사례**: (트랜잭션) 환불 확인

{% raw %}
| 변수 | Liquid 템플릿 |
| --- | --- |
| 주문 ID | `{{event_properties.${order_id}}}` |
| 주문 메모 | `{event_properties.${note}}}` |
| 항목 ID | `{{event_properties.${line_items}[0].product_id}}` |
| 항목 수량 | `{{event_properties.${line_items}[0].quantity}}` |
| 항목 SKU | `{{event_properties.${line_items}[0].sku}}` |
| 항목 제목 | `{{event_properties.${line_items}[0].title}}` |
| 항목 판매자 | `{{event_properties.${line_items}[0].vendor}}` |
| 항목 이름 | `{{event_properties.${line_items}[0].name}}` |
| 항목 속성정보 | `{{event_properties.${line_items}[0].properties}}` |
| 항목 가격 | `{{event_properties.${line_items}[0].price}}` |
| 배리언트 ID | `{{event_properties.${line_items}[0].variant_id}}` |
| 배리언트 제목 | `{{event_properties.${line_items}[0].variant_title}}` |
{: .reset-br-td-1 .reset-br-td-2 aria-label="추적되는 Shopify 이벤트" }
{% endraw %}

{% endsubtab %}
{% subtab Account login %}

**이벤트**: `shopify_account_login`<br>
**유형**: [커스텀 이벤트]({{site.baseurl}}/user_guide/data/activation/events/custom_events)<br>
**트리거 조건**: 사용자가 자신의 계정에 로그인할 때<br>
**데이터 소스**: Braze REST API<br>
**사용 사례**: 환영 시리즈

{% raw %}
| 변수 | Liquid 템플릿 |
| --- | --- |
| `source` | {{event_properties.${source}}} |
{: .reset-br-td-1 .reset-br-td-2 aria-label="추적되는 Shopify 이벤트" }
{% endraw %}

{% alert note %}
현재 Shopify 통합은 Braze [구매 이벤트]({{site.baseurl}}/user_guide/data/activation/events/purchase_events) 채우기를 지원하지 않습니다. 따라서 구매 필터, Liquid 태그, 액션 기반 트리거 및 분석에는 `ecommerce.order_placed` 이벤트를 사용해야 합니다.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 지원되는 Shopify 커스텀 속성 {#supported-shopify-custom-attributes}

{% multi_lang_include alerts/note_alerts.md alert='Shopify attributes REST API' %}

{% tabs local %}
{% tab Example Payload %}
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
{% tab Shopify 커스텀 속성 %}
| 속성 이름 | 설명 |
| --- | --- |
| `shopify_total_spent` | 고객이 주문 내역 전체에서 지출한 총 금액입니다. |
| `shopify_order_count` | 해당 고객과 연결된 주문 수입니다. 테스트 및 보관된 주문은 포함되지 않습니다. |
| `shopify_last_order_id` | 고객의 마지막 주문 ID입니다. |
| `shopify_last_order_name` | 고객의 마지막 주문 이름입니다. 이는 주문 리소스의 `name` 필드와 직접 관련됩니다. |
| `shopify_zipcode` | 고객 기본 주소의 우편번호입니다. |
| `shopify_province` | 고객 기본 주소의 시/도입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="지원되는 Shopify 커스텀 속성" }

{% alert important %}
현재 Shopify API 버전의 알려진 문제로 인해 `shopify_last_order_name` 사용자 속성이 올바르게 채워지지 않습니다. 사용자에게 미치는 영향은 다음과 같습니다.<br><br>

- **기존 사용자:** `shopify_last_order_name`에 이미 값이 있는 사용자의 경우, 해당 값은 유지되지만 이후 주문에 의해 업데이트되지 않습니다.
- **신규 사용자:** 신규 사용자의 경우 해당 필드가 채워지지 않으며 비어 있거나 null로 남습니다.

Shopify에서 이 문제를 해결한 후 이 페이지가 업데이트될 예정입니다.
{% endalert %}

### Liquid 개인화 {#liquid-personalization}

Shopify 커스텀 속성에 대한 Liquid 개인화를 추가하려면 **+ Personalization**을 선택합니다. 그런 다음 개인화 유형으로 **커스텀 속성**를 선택합니다.

![속성 드롭다운이 펼쳐진 개인화 추가 섹션.]({% image_buster /assets/img/shopify/add_personalization_2.png %}){: style="max-width:40%;"}

커스텀 속성을 선택한 후 기본값을 입력하고 Liquid 스니펫을 메시지에 복사합니다.

![Liquid 스니펫을 메시지에 붙여넣기.]({% image_buster /assets/img/shopify/copy_liquid_snippet.png %})
{% endtab %}
{% endtabs %}

## 지원되는 Shopify 표준 속성 {#supported-shopify-standard-attributes}

{% multi_lang_include alerts/note_alerts.md alert='Shopify attributes REST API' %}

- 이메일
- 이름
- 성
- 전화번호
- 구/군/시
- 국가

{% alert note %}
Braze는 기존 고객 프로필의 데이터와 차이가 있는 경우에만 지원되는 Shopify 커스텀 속성 및 Braze 표준 속성을 업데이트합니다. 예를 들어, 수신된 Shopify 데이터에 이름이 Bob으로 포함되어 있고 Braze 고객 프로필에도 이미 이름이 Bob으로 존재하는 경우, Braze는 업데이트를 트리거하지 않으며 데이터 포인트가 차감되지 않습니다.
{% endalert %}

## SDK 데이터 수집 {#sdk-data-collection}

Braze SDK에서 수집하는 데이터에 대한 자세한 내용은 [SDK 데이터 수집]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection)을 참조하세요.

## 과거 데이터 백필 {#historical-backfill}

> 과거 Shopify 데이터는 Braze를 연결하기 전의 데이터를 가져옵니다. 지난 90일간의 주문 이벤트와 지난 1년간의 고객 데이터가 포함됩니다. 두 기간 모두 통합을 완료한 날짜를 기준으로 역산됩니다.

[Shopify 표준 통합 설정]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration) 또는 [Shopify 커스텀 통합 설정]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration)을 통해 과거 데이터 백필을 활성화하여 기존 고객을 타겟팅할 수 있습니다. 이 기능은 지난 90일간의 Shopify 주문(주문 관련 이벤트)과 지난 1년간의 고객 프로필을 가져옵니다. 두 기간 모두 통합을 완료한 날짜를 기준으로 역산됩니다.

Braze가 Shopify 고객을 가져올 때, 구성 설정에서 선택한 `external_id` 유형을 할당합니다.

{% alert note %}
이미 활성 Campaigns 또는 Canvases가 있는 기존 Braze 사용자라면, 과거 데이터 백필을 활성화하기 전에 가져온 고객과 주문 이벤트가 Segments 및 여정에 미치는 영향을 검토하세요.
{% endalert %}

{% multi_lang_include partners/shopify.md section='Custom external ID historical backfill' %}

### Shopify 과거 데이터 백필 설정 {#setting-up-shopify-historical-backfill}

1. **Track Shopify data** 단계에서 과거 데이터 백필을 활성화합니다.

![과거 데이터 백필이 선택된 Shopify 통합의 "Track Shopify data" 단계]({% image_buster /assets/img/shopify/historical_data_backfill_sync.png %})

{: start="2"}

2. 통합 설정을 완료하면 Braze가 초기 데이터 동기화를 시작합니다. 통합 설정의 **Shopify Data** 탭에서 진행 상황을 모니터링할 수 있습니다.

![이벤트가 활발하게 동기화 중임을 나타내는 스피너가 표시된 Shopify 통합 설정 페이지]({% image_buster /assets/img/shopify/historical_data_backfill_syncing.png %})

### 동기화되는 데이터 {#synced-data}

초기 데이터 동기화 시, Braze는 통합 완료일 기준으로 지난 90일간의 주문 이벤트와 지난 1년간의 고객 프로필을 가져옵니다. Braze가 Shopify 고객을 가져올 때, 구성 설정에서 선택한 `external_id` 유형을 할당합니다.

다음 표는 초기 로드에 포함되는 데이터를 요약합니다.

| Braze 권장 이벤트 | Shopify 커스텀 이벤트 | Braze 표준 속성 | Braze 가입 상태 |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li>Order placed</li><li>Order cancelled</li><li>Order refunded</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li><li>shopify_province</li></ul>{:/} | {::nomarkdown}<ul><li>이메일</li><li>이름</li><li>성</li><li>전화번호</li><li>구/군/시</li><li>국가</li><li>총 매출</li><li>총 환불</li><li>총 주문</li></ul>{:/} | {::nomarkdown}<ul><li>이 Shopify 스토어에 연결된 이메일 마케팅 가입</li><li>이 Shopify 스토어에 연결된 단문 메시지 서비스 마케팅 가입</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="동기화되는 데이터" }