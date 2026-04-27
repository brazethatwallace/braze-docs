---
nav_title: eCommerce 추천 이벤트
article_title: 전자상거래 추천 이벤트
page_type: reference
alias: /ecommerce_events/
toc_headers: h2
description: "이 참조 문서에서는 전자상거래 추천 이벤트 및 등록정보, 사용법, 세분화, 관련 분석을 확인할 수 있는 위치 등을 설명합니다."
---

# eCommerce 추천 이벤트 {#ecommerce-recommended-events}

> 이 페이지에서는 전자상거래 추천 이벤트 및 등록정보를 다룹니다. 이 이벤트는 마케터가 효과적인 메시징을 트리거하는 데 필요한 주요 쇼핑 동작을 포착하기 위해 만들어졌습니다. 예를 들어, 유기한 장바구니를 타겟팅하는 것이 있습니다.

{% alert important %}
eCommerce 추천 이벤트는 현재 얼리 액세스 중입니다. 이 얼리 액세스에 참여하고 싶다면 Braze 고객 성공 매니저에게 문의하세요. <br><br>새로운 [Shopify 커넥터]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector)를 사용하고 있다면, 이 추천 이벤트는 통합을 통해 자동으로 사용할 수 있습니다.
{% endalert %}

Braze는 데이터 계획에 시간이 걸린다는 것을 잘 알고 있습니다. 개발 팀과 협력하여 지금부터 이러한 이벤트를 전송하기 시작하는 것을 권장합니다. 전자상거래 추천 이벤트와 함께 즉시 사용할 수 없는 기능이 있을 수 있지만, 2025년 동안 전자상거래 기능을 향상시킬 새로운 제품이 도입될 예정입니다.

## 전자상거래 추천 이벤트의 유형 {#types-of-ecommerce-recommended-events}

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

보고된 모든 비 USD 통화는 보고된 날짜의 환율에 따라 Braze에서 USD로 표시됩니다. 통화 변환을 방지하려면 통화를 USD로 하드코딩하세요.

{% tabs %}
{% tab ecommerce.product_viewed %}

고객이 제품 상세 페이지를 조회할 때 트리거하기 위해 제품 조회 이벤트를 사용할 수 있습니다.

#### 등록정보 {#properties}

| 등록정보 이름 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `product_id` | 예 | 문자열 | 조회된 제품의 고유 식별자입니다. <br> 비-Shopify 고객의 경우, SKU와 같은 카탈로그 항목 ID에 대해 설정한 값이 됩니다. |
| `product_name` | 예 | 문자열 | 조회된 제품의 이름입니다. |
| `variant_id` | 예 | 문자열 | 제품 배리언트의 고유 식별자입니다. 예시: `shirt_medium_blue` |
| `image_url` | 아니요 | 문자열 | 제품 이미지의 URL입니다. |
| `product_url` | 아니요 | 문자열 | 제품 페이지의 URL입니다. |
| `price` | 예 | 플로트 | 조회 시점의 제품 배리언트 단가입니다. |
| `currency` | 예 | 문자열 | 제품 가격이 표시되는 통화(예: "USD" 또는 "EUR")이며, [ISO 4217 형식](https://www.iso.org/iso-4217-currency-codes.html)을 사용합니다. |
| `source` | 예 | 문자열 | 이벤트가 발생한 소스입니다. (Shopify의 경우 storefront입니다.) |
| `type` | 아니요 | 오브젝트 | [재입고 알림]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/) 및 [가격 인하 알림]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications/)과 함께 작동합니다. |
| `metadata` | 아니요 | 오브젝트 | |
| `sku` | 아니요 | 문자열 | (Shopify 전용) Shopify SKU입니다. 카탈로그 ID 필드로 구성할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### 예시 오브젝트 {#example-objects}

{% subtabs %}
{% subtab Web SDK %}

{% sdk_min_versions web:6.8.0 %}

최신 SDK 버전에서는 `logEcommerceEvent()`를 호출합니다:

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

레거시 SDK 버전에서는 `logCustomEvent()`를 호출합니다:

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

**장바구니 업데이트 이벤트 수행** 트리거를 사용하여 장바구니에서 제품이 추가, 제거 또는 업데이트될 때를 추적할 수 있습니다. 이 이벤트는 트리거하기 전에 다음 정보를 확인합니다:

- 이벤트 시간이 사용자의 특정 장바구니에 대한 `updated_at` 시간보다 큽니다.
- 장바구니가 결제 프로세스로 진행되지 않았습니다.
- `products` 배열이 비어 있지 않습니다.

#### 장바구니 매핑 오브젝트 {#carts-mapping-object}

`ecommerce.cart_updated` 이벤트에는 장바구니 매핑 오브젝트가 있습니다. 이 오브젝트는 쇼핑객의 장바구니에 있는 모든 제품을 포함하는 장바구니 매핑을 담고 있는 고객 프로필에 생성됩니다. Liquid 태그를 통해 장바구니에 있는 제품에 접근할 수 있습니다:

{%raw%}
```liquid
{% shopping_cart {{context_properties.${cart_id}}} %}
{% for item in shopping_cart.products %}
{% catalog_items <add_your_catalog> {{item.variant_id}} %}
```
{%endraw%}

장바구니가 업데이트되지 않고 30일 이내에 주문 완료 이벤트로 진행되지 않으면, Braze는 해당 장바구니와 관련 제품을 삭제합니다.

{% alert note %}
장바구니당 제품 수는 Braze에서 제한되지 않습니다. 그러나 Shopify의 제한은 500개입니다.
{% endalert %}

#### 사용자 프로필 병합 시 장바구니 동작 {#cart-behavior-when-merging-user-profiles}

두 개의 장바구니가 있는 경우, 병합된 사용자에 두 장바구니를 모두 추가합니다. 동일하거나 다른 장바구니인 경우 Canvas를 다시 대기줄에 넣어 가장 최근 장바구니 정보가 포함된 메시지를 발송합니다. `ecommerce.cart_updated` 이벤트에는 최신 장바구니 ID와 장바구니에 있는 최신 제품이 포함됩니다.

#### 등록정보 {#properties}

| 등록정보 이름 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `cart_id` | 예 | 문자열 | `cart_id`를 제공하는 서드파티 플랫폼을 사용하지 않는 경우, [Braze 세션 ID]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/)를 사용할 수 있습니다. |
| `total_value` | 예 | 플로트 | 장바구니의 총 금액입니다. |
| `subtotal_value` | 아니요 | 플로트 | 할인 적용 후, 세금 및 배송비 적용 전 장바구니의 소계 금액입니다. |
| `tax` | 아니요 | 플로트 | 장바구니에 적용된 총 세금입니다. |
| `shipping` | 아니요 | 플로트 | 장바구니의 총 배송비입니다. |
| `currency` | 예 | 문자열 | 제품 가격이 표시되는 통화(예: "USD" 또는 "EUR")이며, [ISO 4217 형식](https://www.iso.org/iso-4217-currency-codes.html)을 사용합니다. |
| `products` | 예 | 배열 |  |
| `product_id` | 예 | 문자열 | 조회된 제품의 고유 식별자입니다. <br> 이 값은 제품 ID 또는 SKU일 수 있습니다. |
| `product_name` | 예 | 문자열 | 조회된 제품의 이름입니다. |
| `variant_id` | 예 | 문자열 | 제품 배리언트의 고유 식별자입니다. 예시: `shirt_medium_blue` |
| `image_url` | 아니요 | 문자열 | 제품 이미지의 URL입니다. |
| `product_url` | 아니요 | 문자열 | 제품 페이지의 URL입니다. |
| `quantity` | 예 | 정수 | 장바구니에 있는 제품의 수량입니다. |
| `price` | 예 | 플로트 | 조회 시점의 제품 배리언트 단가입니다. |
| `metadata` | 아니요 | 오브젝트 | 고객이 사용 사례에 맞게 추가하려는 제품에 대한 추가 메타데이터 필드입니다. Shopify의 경우 SKU가 추가됩니다. <br> 일반 이벤트 등록정보 제한인 50kb를 기준으로 제한이 있습니다. |
| `sku` | 아니요 | 문자열 | (Shopify 전용) Shopify SKU입니다. 카탈로그 ID 필드로 구성할 수 있습니다. |
| `source` | 예 | 문자열 | 이벤트가 발생한 소스입니다. (Shopify의 경우 storefront입니다.) |
| `metadata` | 아니요 | 오브젝트 | 고객이 사용 사례에 맞게 추가하려는 제품에 대한 추가 메타데이터 필드입니다. Shopify의 경우 SKU가 추가됩니다. <br> 일반 이벤트 등록정보 제한인 50kb를 기준으로 제한이 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### 예시 오브젝트 {#example-objects}

{% subtabs %}
{% subtab Web SDK %}

{% sdk_min_versions web:6.8.0 %}

최신 SDK 버전에서는 `logEcommerceEvent()`를 호출합니다:

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

레거시 SDK 버전에서는 `logCustomEvent()`를 호출합니다:

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

결제 시작 이벤트를 사용하여 결제 프로세스를 시작했지만 주문을 완료하지 않은 고객을 리타겟할 수 있습니다.

`ecommerce.cart_updated` 이벤트와 마찬가지로, 이 이벤트를 통해 장바구니 Liquid 태그를 활용하여 결제 포기 메시지에서 장바구니 내 모든 제품에 접근할 수 있습니다:

{%raw%}
```liquid
{% shopping_cart {{context_properties.${cart_id}}} :abort_if_not_abandoned false %}
{% for item in shopping_cart.products %}
{% catalog_items <add_your_catalog> {{item.variant_id}} %}
```
{%endraw%}

#### 등록정보 {#properties}

| 등록정보 이름 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `checkout_id` | 예 | 문자열 | 결제의 고유 식별자입니다. |
| `cart_id` | 아니요 | 문자열 | `cart_id`를 제공하는 서드파티 플랫폼을 사용하지 않는 경우, [Braze 세션 ID]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/)를 사용할 수 있습니다. |
| `total_value` | 예 | 플로트 | 장바구니의 총 금액입니다. |
| `subtotal_value` | 아니요 | 플로트 | 할인 적용 후, 세금 및 배송비 적용 전 장바구니의 소계 금액입니다. |
| `tax` | 아니요 | 플로트 | 장바구니에 적용된 총 세금입니다. |
| `shipping` | 아니요 | 플로트 | 장바구니의 총 배송비입니다. |
| `currency` | 예 | 문자열 | 장바구니의 통화입니다. |
| `products` | 예 | 오브젝트 배열 |  |
| `product_id` | 예 | 문자열 | 조회된 제품의 고유 식별자입니다. 예를 들어 이 값은 제품 ID 또는 SKU일 수 있습니다. |
| `product_name` | 예 | 문자열 | 조회된 제품의 이름입니다.  |
| `variant_id` | 예 | 문자열 | 제품 배리언트의 고유 식별자입니다. 예시: `shirt_medium_blue` |
| `image_url` | 아니요 | 문자열 | 제품 이미지의 URL입니다. |
| `product_url` | 아니요 | 문자열 | 제품 페이지의 URL입니다. |
| `quantity` | 예 | 정수 | 장바구니에 있는 제품의 수량입니다. |
| `price` | 예 | 플로트 | 조회 시점의 제품 배리언트 단가입니다. |
| `metadata` | 아니요 | 오브젝트 | 고객이 사용 사례에 맞게 추가하려는 제품에 대한 추가 메타데이터 필드입니다. Shopify의 경우 SKU가 추가됩니다. <br> 일반 이벤트 등록정보 제한인 50kb를 기준으로 제한이 있습니다. |
| `sku` | 아니요 | 문자열 | (Shopify 전용) Shopify SKU입니다. 카탈로그 ID 필드로 구성할 수 있습니다. |
| `source` | 예 | 문자열 | 이벤트가 발생한 소스입니다. (Shopify의 경우 storefront입니다.) |
| `metadata` | 아니요 | 오브젝트 |  |
| `checkout_url` | 아니요 | 문자열 | 결제 페이지의 URL입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### 예시 오브젝트 {#example-objects}

{% subtabs %}
{% subtab Web SDK %}

{% sdk_min_versions web:6.8.0 %}

최신 SDK 버전에서는 `logEcommerceEvent()`를 호출합니다:

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

레거시 SDK 버전에서는 `logCustomEvent()`를 호출합니다:

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

주문 완료 이벤트를 사용하여 고객이 결제 프로세스를 성공적으로 완료하고 주문을 완료했을 때 트리거할 수 있습니다.

#### 등록정보 {#properties}

| 등록정보 이름 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `order_id` | 예 | 문자열 | 완료된 주문의 고유 식별자입니다. |
| `cart_id` | 아니요 | 문자열 | `cart_id`를 제공하는 서드파티 플랫폼을 사용하지 않는 경우, [Braze 세션 ID]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/)를 사용할 수 있습니다. |
| `total_value` | 예 | 플로트 | 장바구니의 총 금액입니다. |
| `subtotal_value` | 아니요 | 플로트 | 할인 적용 후, 세금 및 배송비 적용 전 주문의 소계 금액입니다. |
| `tax` | 아니요 | 플로트 | 주문에 적용된 총 세금입니다. |
| `shipping` | 아니요 | 플로트 | 주문의 총 배송비입니다. |
| `currency` | 예 | 문자열 | 장바구니의 통화입니다. |
| `total_discounts` | 아니요 | 플로트 | 주문에 적용된 총 할인 금액입니다. |
| `discounts`| 아니요 | 오브젝트 배열 | 주문에 적용된 할인의 상세 목록입니다. |
| `products` | 예 | 오브젝트 배열 |  |
| `product_id` | 예 | 문자열 | 조회된 제품의 고유 식별자입니다. 이 값은 제품 ID 또는 SKU일 수 있습니다. |
| `product_name` | 예 | 문자열 | 조회된 제품의 이름입니다. |
| `variant_id` | 예 | 문자열 | 제품 배리언트의 고유 식별자입니다. 예시: `shirt_medium_blue` |
| `image_url` | 아니요 | 문자열 | 제품 이미지의 URL입니다. |
| `product_url` | 아니요 | 문자열 | 제품 페이지의 URL입니다. |
| `quantity` | 예 | 정수 | 장바구니에 있는 제품의 수량입니다. |
| `price` | 예 | 플로트 | 조회 시점의 제품 배리언트 단가입니다. |
| `metadata` | 아니요 | 오브젝트 | 고객이 사용 사례에 맞게 추가하려는 제품에 대한 추가 메타데이터 필드입니다. Shopify의 경우 SKU가 추가됩니다. <br> 일반 이벤트 등록정보 제한인 50kb를 기준으로 제한이 있습니다. |
| `sku` | 아니요 | 문자열 | (Shopify 전용) Shopify SKU입니다. 카탈로그 ID 필드로 구성할 수 있습니다. |
| `source` | 예 | 문자열 | 이벤트가 발생한 소스입니다. (Shopify의 경우 storefront입니다.) |
| `order_status_url` | 아니요 | 문자열 | 주문 상태를 확인할 수 있는 URL입니다. |
| `order_number` | 아니요 | 문자열 | (Shopify 전용) 완료된 주문의 고유 주문 번호입니다. |
| `tags` | 아니요 | 배열 | (Shopify 전용) 주문 태그입니다.
| `referring_site` | 아니요 | 문자열 | (Shopify 전용) 주문이 발생한 사이트입니다(예: Meta). |
| `payment_gateway_names` | 아니요 | 배열 | (Shopify 전용) 결제 시스템 소스입니다(예: POS 또는 모바일). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### 예시 오브젝트 {#example-objects}

{% subtabs %}
{% subtab Web SDK %}

{% sdk_min_versions web:6.8.0 %}

최신 SDK 버전에서는 `logEcommerceEvent()`를 호출합니다:

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

레거시 SDK 버전에서는 `logCustomEvent()`를 호출합니다:

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

주문 환불 이벤트를 사용하여 주문이 부분적으로 또는 전체적으로 환불될 때 트리거할 수 있습니다.

#### 등록정보 {#properties}

| 등록정보 이름       | 필수 | 데이터 유형 | 설명   |
|---------------|---------|-----------|-------------------------|
| `order_id`            | 예      | 문자열    | 완료된 주문의 고유 식별자입니다.        |
| `total_value`         | 예      | 플로트     | 장바구니의 총 금액입니다.    |
| `currency`            | 예      | 문자열    | 장바구니의 통화입니다.    |
| `total_discounts`     | 아니요       | 플로트     | 주문에 적용된 총 할인 금액입니다.   |
| `discounts`           | 아니요       | 오브젝트 배열     | 주문에 적용된 할인의 상세 목록입니다. |
| `products`            | 예      | 오브젝트 배열     |  |
| `product_id`       | 예      | 문자열    | 조회된 제품의 고유 식별자입니다. 이 값은 제품 ID, SKU 또는 유사한 값일 수 있습니다. <br>부분 환불이 발생하고 환불에 `product_id`가 할당되지 않은 경우(예: 주문 수준 환불), 일반화된 `product_id`를 제공하세요.             |
| `product_name`     | 예      | 문자열    | 조회된 제품의 이름입니다.                                                                      |
| `variant_id`       | 예      | 문자열    | 제품 배리언트의 고유 식별자입니다(예: `shirt_medium_blue`).                                         |
| `image_url`        | 아니요       | 문자열    | 제품 이미지의 URL입니다.     |
| `product_url`      | 아니요       | 문자열    | 제품 페이지의 URL입니다.  |
| `quantity`         | 예      | 정수   | 장바구니에 있는 제품의 수량입니다.   |
| `price`            | 예      | 플로트     | 조회 시점의 제품 배리언트 단가입니다.  |
| `metadata`         | 아니요       | 오브젝트    | 고객이 사용 사례에 맞게 추가하려는 제품에 대한 추가 메타데이터 필드입니다. Shopify의 경우 SKU가 추가됩니다. 일반 이벤트 등록정보 제한인 50kb를 기준으로 제한이 있습니다. |
| `sku`            | 아니요       | 문자열    | (Shopify 전용) Shopify SKU입니다. 카탈로그 ID 필드로 구성할 수 있습니다.  |
| `source`              | 예      | 문자열    | 이벤트가 발생한 소스입니다. (Shopify의 경우 storefront입니다.)    |
| `metadata`            | 아니요       | 오브젝트    |                |
| `order_status_url`  | 아니요       | 문자열    | 주문 상태를 확인할 수 있는 URL입니다.     |
| `order_note`       | 아니요       | 문자열    | (Shopify 전용) 판매자가 주문에 추가한 메모입니다.    |
| `order_number`     | 아니요       | 문자열    | (Shopify 전용) 완료된 주문의 고유 주문 번호입니다.   |
| `tags`             | 아니요       | 배열     | (Shopify 전용) 주문 태그입니다.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### 예시 오브젝트 {#example-objects}

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

주문 취소 이벤트를 사용하여 고객이 주문을 취소할 때 트리거할 수 있습니다.

#### 등록정보 {#properties}

| 등록정보 이름      | 필수 | 데이터 유형 | 설명       |
|---------------------|----------|-----------|-------------------|
| `order_id`            | 예      | 문자열    | 완료된 주문의 고유 식별자입니다.              |
| `cancel_reason`       | 예      | 문자열    | 주문이 취소된 이유입니다.           |
| `total_value`         | 예      | 플로트     | 장바구니의 총 금액입니다.         |
| `subtotal_value`      | 아니요       | 플로트     | 할인 적용 후, 세금 및 배송비 적용 전 주문의 소계 금액입니다. |
| `tax`                 | 아니요       | 플로트     | 주문에 적용된 총 세금입니다. |
| `shipping`            | 아니요       | 플로트     | 주문의 총 배송비입니다. |
| `currency`            | 예      | 문자열    | 장바구니의 통화입니다.           |
| `total_discounts`     | 아니요       | 플로트     | 주문에 적용된 총 할인 금액입니다.     |
| `discounts`           | 아니요       | 오브젝트 배열     | 주문에 적용된 할인의 상세 목록입니다.             |
| `products`            | 예      | 오브젝트 배열     |         |
| `product_id`          | 예      | 문자열    | 조회된 제품의 고유 식별자입니다. 이 값은 제품 ID, SKU 또는 유사한 값일 수 있습니다.             |
| `product_name`        | 예      | 문자열    | 조회된 제품의 이름입니다.          |
| `variant_id`          | 예      | 문자열    | 제품 배리언트의 고유 식별자입니다(예: `shirt_medium_blue`).        |
| `image_url`           | 아니요       | 문자열    | 제품 이미지의 URL입니다.           |
| `product_url`         | 아니요       | 문자열    | 제품 페이지의 URL입니다.                                                                     |
| `quantity`            | 예      | 정수   | 장바구니에 있는 제품의 수량입니다.        |
| `price`               | 예      | 플로트     | 조회 시점의 제품 배리언트 단가입니다.     |
| `metadata`            | 아니요       | 오브젝트    | 고객이 사용 사례에 맞게 추가하려는 제품에 대한 추가 메타데이터 필드입니다. Shopify의 경우 SKU가 추가됩니다. 일반 이벤트 등록정보 제한인 50kb를 기준으로 제한이 있습니다. |
| `sku`                 | 아니요       | 문자열    | (Shopify 전용) Shopify SKU입니다. 카탈로그 ID 필드로 구성할 수 있습니다.        |
| `source`              | 예      | 문자열    | 이벤트가 발생한 소스입니다. (Shopify의 경우 storefront입니다.)    |
| `metadata`            | 아니요       | 오브젝트    |       |
| `order_status_url`    | 아니요       | 문자열    | 주문 상태를 확인할 수 있는 URL입니다.                                                                          |
| `order_number`        | 아니요       | 문자열    | (Shopify 전용) 완료된 주문의 고유 주문 번호입니다.  |
| `tags`                | 아니요       | 배열     | (Shopify 전용) 주문 태그입니다.            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### 예시 오브젝트 {#example-objects}

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

## eCommerce 캔버스 템플릿 {#ecommerce-canvas-templates}

Braze는 eCommerce 추천 이벤트를 기반으로 하는 사전 구축된 캔버스 템플릿을 제공합니다. 예를 들어 결제 프로세스를 시작했지만 주문을 완료하기 전에 이탈한 고객을 타겟팅할 수 있습니다. 이러한 이벤트를 사용하여 메시징을 개인화하고 특정 오디언스를 타겟팅함으로써 사용자 여정을 향상시키는 데 도움이 되는 정보에 기반한 결정을 내릴 수 있습니다.

캔버스 템플릿과 함께 이러한 이벤트를 활용하는 더 많은 방법은 전용 [eCommerce 활용 사례]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases/)를 확인하세요.

## 사용자 계산 필드 {#user-calculated-fields}

다음 필드에 대해 표준화된 사용자 필드 계산을 사용합니다:

- **총 매출** = 총 주문 완료 금액의 합계 - 총 주문 환불 금액의 합계
- **총 주문 수** = 고유 주문 완료 이벤트 수 - 고유 주문 취소 수
- **총 환불 금액** = 총 주문 환불 금액의 합계

이러한 사용자 필드 계산은 고객 프로필의 **트랜잭션** 탭에도 포함되어 있습니다.

![사용자 계산 필드가 있는 "트랜잭션" 탭]({% image_buster /assets/img/Shopify/transactions_tab.png %}){: style="max-width:70%;"}

## 자주 묻는 질문 {#frequently-asked-questions}

### 제품 수준의 구매 데이터는 어디에서 볼 수 있나요? {#where-can-i-view-product-level-purchase-data}

고객 프로필의 **트랜잭션** 탭에는 총 매출 및 총 주문 수와 같은 상위 수준의 계산 필드가 표시됩니다. 특정 사용자의 제품 수준 세부 정보를 보려면 [쿼리 빌더]({{site.baseurl}}/user_guide/analytics/reports/query_builder/)를 사용하여 eCommerce 이벤트 데이터를 쿼리하거나, [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)를 통해 이벤트 데이터를 내보내세요.

레거시 구매 이벤트와 달리, eCommerce 추천 이벤트는 제품 세부 정보를 `products` 배열 내의 중첩된 이벤트 속성정보로 저장합니다. 이러한 등록정보는 Liquid를 통한 메시징과 [세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/)을 통한 세분화에서 사용할 수 있습니다.

### 특정 제품별로 사용자를 세분화하려면 어떻게 하나요? {#how-do-i-segment-users-by-a-specific-product}

세그먼터를 사용하면 사용자가 eCommerce 이벤트를 수행한 횟수로 필터링할 수 있습니다. 특정 제품 등록정보(예: `product_id` 또는 `product_name`)로 필터링하려면 중첩된 이벤트 속성정보 필터링을 지원하는 [세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/)을 사용하세요. 예를 들어 지난 90일 동안 제품 "SKU-123"을 구매한 모든 사용자를 찾을 수 있습니다.

### 레거시 구매 이벤트와 eCommerce 추천 이벤트의 차이점은 무엇인가요? {#whats-the-difference-between-legacy-purchase-events-and-ecommerce-recommended-events}

레거시 구매 이벤트는 Braze [구매 오브젝트]({{site.baseurl}}/api/objects_filters/purchase_object/)를 사용하며 `product_id`와 `price`로 개별 제품 구매를 기록합니다. eCommerce 추천 이벤트(예: `ecommerce.order_placed`)는 커스텀 이벤트 등록정보를 사용하며 여러 제품, 할인 및 메타데이터를 포함한 전체 주문 컨텍스트를 단일 이벤트로 캡처합니다.

eCommerce 추천 이벤트의 출시와 함께, Braze는 향후 레거시 구매 이벤트를 단계적으로 폐지할 예정입니다. 현재 구매 이벤트를 사용하고 있다면 사전에 공지를 받게 됩니다. 그때까지는 공식 폐지 날짜까지 구매 이벤트를 계속 사용할 수 있습니다. 자세한 내용은 [추천 이벤트 개요]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/)를 참조하세요.

### eCommerce 추천 이벤트에 커스텀 등록정보를 추가할 수 있나요? {#can-i-add-custom-properties-to-ecommerce-recommended-events}

eCommerce 추천 이벤트에는 필수 및 선택 필드가 포함된 정의된 스키마가 있습니다. 각 이벤트의 `metadata` 오브젝트 내에 추가 커스텀 데이터를 포함할 수 있습니다. 그러나 커스텀 주문 수준 태그나 독점 필드(예: 구매 채널 또는 소매점 정보)는 최상위 등록정보로 지원되지 않습니다. 세분화에 이러한 필드가 필요한 경우, eCommerce 이벤트와 함께 별도의 커스텀 이벤트로 계속 전송하세요.

### eCommerce 이벤트를 전송할 때 external_id를 포함해야 하나요? {#do-i-need-to-include-externalid-when-sending-ecommerce-events}

이벤트를 전송하는 방법에 따라 다릅니다:

- **SDK를 통해**: 아니요. Braze SDK를 사용하면 이벤트가 SDK의 현재 사용자 컨텍스트(익명 또는 식별됨)에 자동으로 연결됩니다. 각 이벤트 호출에 사용자 식별자를 전달할 필요가 없으며, 대신 `changeUser`와 같은 메서드를 사용하여 해당 컨텍스트의 사용자를 식별할 수 있습니다.
- **REST API(`/users/track`)를 통해**: 예. 각 API 요청에는 `external_id`, `braze_id`, `user_alias`, `email` 또는 `phone`과 같은 사용자 식별자가 포함되어야 합니다. API에는 "현재 사용자" 컨텍스트가 없기 때문입니다.

### 인공지능 항목 추천 설정 드롭다운에 중첩된 제품 등록정보가 표시되지 않는 이유는 무엇인가요? {#why-dont-nested-product-properties-appear-in-the-ai-recommendations-setup-dropdown}

[인공지능 항목 추천]({{site.baseurl}}/user_guide/brazeai/item_recommendations/)을 구성할 때, **등록정보 이름** 드롭다운에는 최상위 이벤트 등록정보(예: `order_id`, `total_value`, `currency`)만 나열됩니다. `products` 배열 내의 중첩된 등록정보(예: `products.product_id` 또는 `products.variant_id`)는 이 목록에 표시되지 않을 수 있지만, 필드에 점 표기법을 사용하여 수동으로 입력할 수 있습니다. 대부분의 eCommerce 구현에서 Braze는 `products.product_id`를 항목 식별자로 사용하고, `product_id` 또는 `variant_id` 값과 일치하는 항목 ID를 가진 [카탈로그]({{site.baseurl}}/user_guide/data/activation/catalogs/)와 함께 사용하는 것을 권장합니다.

### 일부 eCommerce 이벤트가 Braze에 표시되지 않는 이유는 무엇인가요? {#why-are-some-of-my-ecommerce-events-not-appearing-in-braze}

이벤트가 고객 프로필이나 로그에 표시되지 않는 경우, 다음을 확인하세요:

- **SDK 데이터 플러시 타이밍**: Braze SDK는 데이터를 로컬에 캐시하고 주기적으로 업로드합니다(일반적으로 10~60초 이내). `logCustomEvent()` 후에 `requestImmediateDataFlush()`를 호출하여 즉시 업로드를 강제할 수 있습니다.
- **필수 등록정보**: eCommerce 이벤트에는 필수 등록정보가 있습니다. 필수 등록정보가 누락되었거나 데이터 유형이 잘못된 경우 이벤트가 거부될 수 있습니다. 이벤트 페이로드가 [필수 스키마](#types-of-ecommerce-recommended-events)와 일치하는지 확인하세요.
- **이벤트 이름 정확성**: eCommerce 이벤트 이름은 대소문자를 구분하며 정확히 일치해야 합니다(예: `ecommerce.checkout_started`이지 `ecommerce.checkoutStarted`가 아닙니다).