---
nav_title: 추천 이벤트
article_title: 추천 이벤트
alias: /recommended_events/
page_order: 2
page_type: reference
description: "이 참조 문서에서는 Braze가 eCommerce 이벤트에 대해 제공하는 추천 이벤트에 대해 설명합니다."
---

# 추천 이벤트 {#recommended-events}

> 추천 이벤트는 정의된 JSON 스키마를 가진 표준화된 커스텀 이벤트를 전송하는 프레임워크를 기반으로 구축됩니다. 추천 이벤트를 전송하면 Braze는 수집 시 해당 스키마에 대해 유효성을 검사하고, 일반 커스텀 이벤트에서는 제공되지 않는 자동 필드 계산이나 장바구니 관리와 같은 특수 처리를 적용합니다. 특정 산업 이벤트 세트의 경우, Braze는 Campaigns 및 Canvases에 대한 전용 액션 기반 트리거와 같은 특별한 처리도 지원합니다.

## eCommerce 추천 이벤트 {#ecommerce-recommended-events}

[eCommerce 추천 이벤트]({{site.baseurl}}/ecommerce_events)는 구매 여정의 6단계를 다룹니다: `product_viewed`, `cart_updated`, `checkout_started`, `order_placed`, `order_cancelled`, `order_refunded`. 이러한 이벤트를 성공적으로 전송하면 Braze가 데이터를 유효성 검사하고 점점 늘어나는 플랫폼 기능 세트에서 사용할 수 있도록 합니다.

이러한 기능에는 유기한 탐색, 유기한 장바구니, 유기한 결제, 주문 확인 플로우를 위한 Canvas 템플릿, eCommerce 리포팅, 그리고 _총 매출_, _총 주문 수_, _총 환불 금액_에 대한 계산된 사용자 프로필 필드가 포함됩니다. 또한 [세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension)을 통해 중첩된 제품 속성정보 필터링을 사용하여 세그먼트를 구축하고, {% raw %}`{% shopping_cart %}`{% endraw %} Liquid 태그로 유기한 장바구니 메시지를 개인화하며, [Predictive Events]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events), [예측 이탈]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn), [아이템 추천]({{site.baseurl}}/user_guide/brazeai/item_recommendations) 등의 BrazeAI<sup>TM</sup> 기능과 기타 기능을 활용할 수 있습니다.

이러한 이벤트는 정의된 스키마를 따르기 때문에, 지원되는 각 기능이 커스텀 속성정보 매핑이나 기능별 구성 없이도 구조화된 데이터를 읽을 수 있습니다.

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

### eCommerce 이벤트 작동 방식 {#how-ecommerce-events-work}

eCommerce 이벤트는 사전 정의된 이름과 속성정보 스키마를 가진 커스텀 이벤트입니다. [Braze SDK]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events), [`/users/track` REST API 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track), 또는 [클라우드 데이터 수집(CDI)]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)을 사용하여 전송하며, Braze는 수집 시 각 이벤트를 해당 스키마에 대해 유효성 검사합니다. 유효성 검사를 통과하면 Braze는 해당 이벤트 유형에 특화된 후처리를 자동으로 적용합니다(예: 매출 필드 계산 및 사용자 프로필의 장바구니 상태 관리).

{% alert note %}
CSV 업로드는 eCommerce 이벤트를 지원하지 않습니다. 이러한 이벤트를 전송하려면 SDK, `/users/track`, 또는 CDI를 사용하세요.
{% endalert %}

eCommerce 이벤트는 다른 커스텀 이벤트가 작동하는 모든 곳에서 작동합니다: 수행된 커스텀 이벤트에 대한 트리거 및 필터, 커스텀 이벤트 리포팅 등. 그러나 스키마 유효성 검사를 통해 다음과 같은 추가 기능이 활성화됩니다:

- Campaigns, Canvases, 행동 경로, 인앱 메시지 트리거, 콘텐츠 카드 제거에서의 "주문 완료" 트리거 동작
- 계산된 eCommerce 사용자 프로필 필드(**총 매출**, **총 주문 수**, **총 환불 금액**)
- 유기한 장바구니 플로우를 위한 장바구니 상태 관리
- Predictive Events, 예측 이탈, 아이템 추천과 같은 BrazeAI<sup>TM</sup> 기능을 위한 더 풍부한 데이터

플랫폼에서 커스텀 이벤트를 지원하는 모든 곳에서 이름으로 eCommerce 이벤트를 참조할 수도 있습니다. 예를 들어, `ecommerce.product_viewed` 이벤트로 액션 기반 Campaign을 트리거하거나, `ecommerce.checkout_started` 이벤트를 필터링하여 세그먼트를 구축하거나, Currents를 통해 `ecommerce.order_placed` 이벤트를 내보낼 수 있습니다.

#### 이벤트 이름 지정 {#event-naming}

이벤트 이름은 정확하고, 대소문자를 구분하며, 점(.)으로 구분됩니다. 항상 정규 형식을 사용하세요. 이벤트 이름이 6개의 정규 이름 중 하나와 정확히 일치하지 않으면 Braze는 이를 표준 커스텀 이벤트로 처리하며 eCommerce 후처리가 수행되지 않습니다.

이벤트를 커스터마이즈하거나 이름을 변경할 수 없습니다.

- **올바른 예:** `ecommerce.order_placed`
- **잘못된 예:** `order.placed`, `eCommerce_order_placed`, `Order_Placed`

#### 이벤트 스키마 {#event-schemas}

6개의 eCommerce 추천 이벤트는 구매 여정의 단계에 매핑됩니다. 사용자가 해당 동작을 완료하는 시점에 각 이벤트를 발생시키세요.

![6개의 eCommerce 추천 이벤트(product_viewed, cart_updated, checkout_started, order_placed, order_cancelled, order_refunded)를 거치는 사용자 여정 다이어그램]({% image_buster /assets/img/shopify/event_schemas.png %})

{% alert tip %}
다음 예시는 각 이벤트의 REST API 페이로드를 보여줍니다.
클라이언트 측 로깅의 경우, `ecommerce.product_viewed`, `ecommerce.cart_updated`, `ecommerce.checkout_started`, `ecommerce.order_placed`는 사용 가능한 SDK eCommerce 이벤트 API를 사용하고, `ecommerce.order_cancelled`와 `ecommerce.order_refunded`는 `logCustomEvent`를 사용합니다. 플랫폼별 구현 예시는 [Braze SDK를 통한 eCommerce 이벤트 로깅]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events)을 참조하세요.
{% endalert %}

{% tabs %}
{% tab ecommerce.product_viewed %}

사용자가 제품 상세 페이지를 조회할 때 트리거합니다. 이 이벤트는 Braze 카탈로그의 [재입고 알림]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications) 및 [가격 인하 알림]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications)과 호환됩니다.

#### 클라이언트 측 구현 {#client-side-implementation}

사용 가능한 SDK eCommerce 이벤트 API를 사용하세요. 플랫폼별 구현 예시는 [Braze SDK를 통한 eCommerce 이벤트 로깅]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events)을 참조하세요.

#### 이벤트 속성정보 {#event-properties}

| 속성정보 이름 | 데이터 유형 | 필수 | 설명 |
| -------------- | ---------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `product_id`   | 문자열           | 예      | 고유 제품 식별자(예: SKU 또는 항목 ID).                                                                                                   |
| `product_name` | 문자열           | 예      | 제품 표시 이름.                                                                                                                               |
| `variant_id`   | 문자열           | 예      | 제품 배리언트 식별자(예: `shirt_medium_blue`).                                                                                            |
| `image_url`    | 문자열           | 아니요       | 제품 이미지 URL.                                                                                                                                  |
| `product_url`  | 문자열           | 아니요       | 제품 페이지의 URL.                                                                                                           |
| `price`        | 플로트            | 예      | 조회 시점의 배리언트 단가.                                                                                                          |
| `currency`     | 문자열           | 예      | 3자리 ISO 4217 코드(예: `USD` 또는 `EUR`).                                                                                               |
| `source`       | 문자열           | 예      | 이벤트가 발생한 소스(예: `web`, `ios`, `android`).                                                                               |
| `type`         | 문자열 배열 | 아니요       | 재입고 및 가격 인하 알림을 위한 Braze 카탈로그 트리거 기능을 사용하려면 필수입니다. 허용 값: `"price_drop"`, `"back_in_stock"`     |
| `metadata`     | 오브젝트           | 아니요       | 유연한 키-값 페어(예: `category` 또는 `brand`).                                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Event properties" }

#### REST API 예시 {#rest-api-example}

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

사용자의 장바구니 내용이 변경될 때마다 트리거합니다.

#### 클라이언트 측 구현

사용 가능한 SDK eCommerce 이벤트 API를 사용하세요. 플랫폼별 구현 예시는 [Braze SDK를 통한 eCommerce 이벤트 로깅]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events)을 참조하세요.

이 이벤트는 다음 두 가지 방법 중 하나로 전송할 수 있습니다:

- **전체 장바구니 교체:** `action`을 생략하거나 `action`을 `replace`로 설정합니다. `products`에 절대 수량(장바구니에 있는 배리언트별 총 수량)으로 전체 라인 항목 세트를 포함합니다. `total_value`를 반드시 포함해야 합니다.
- **증분 장바구니 업데이트:** `action`을 `add` 또는 `remove`로 설정합니다. 변경된 라인 항목만 포함합니다. 각 `quantity`는 장바구니의 총 수량이 아니라 추가하거나 제거할 단위 수입니다. `add`의 경우 Braze가 라인 수량을 증가시키거나 새 라인을 추가합니다. `remove`의 경우 Braze가 라인 수량을 감소시키고 수량이 `0`에 도달하면 라인을 제거합니다. `total_value`는 `add` 및 `remove`에서 선택 사항입니다.

{% alert warning %}
주어진 장바구니에 대해 증분 장바구니 업데이트(`add` 또는 `remove`)와 전체 교체(`action` 없음 또는 `replace`) 중 하나만 사용하세요. 동일한 `cart_id`에 대해 두 접근 방식을 혼합하면 Braze에서 일관되지 않은 장바구니 상태가 발생할 수 있으므로 권장하지 않습니다.
{% endalert %}

이 이벤트에서 메시징을 트리거하려면 Canvas 및 Campaigns에서 **장바구니 업데이트 이벤트 수행** 트리거를 사용하세요. 이 트리거에는 장바구니가 쇼핑 퍼널을 통해 진행되는 것을 중지하는 특별한 처리가 포함되어 있습니다.

{% alert tip %}
장바구니는 사용자 프로필에 {% raw %}`{% shopping_cart %}`{% endraw %} Liquid 태그를 구동하는 장바구니 매핑 오브젝트를 생성합니다. 장바구니는 업데이트 없이 30일이 지나면 만료됩니다. 두 사용자 프로필이 병합되면 Braze는 두 장바구니를 모두 보존합니다.
{% endalert %}

#### 이벤트 속성정보

| 속성정보        | 데이터 유형 | 필수 | 설명                                                                                                                   |
|-----------------|-----------|----------|-------------------------------------------------------------------------------------------------------------------------------|
| `cart_id`       | 문자열    | 예      | 장바구니의 고유 식별자. 사용자의 장바구니 매핑을 위해 장바구니, 결제, 주문 이벤트 간에 공유됩니다.                   |
| `action`        | 문자열    | 아니요       | `add`(수량 증가 또는 새 라인 추가), `remove`(수량 감소, `0`에서 라인 제거), `replace`(전체 장바구니 교체, `action` 생략과 동일). |
| `total_value`   | 플로트     | 조건부 | `action`이 생략되거나 `replace`일 때 필수. `action`이 `add` 또는 `remove`일 때 선택 사항.                             |
| `subtotal_value`| 플로트     | 아니요       | 장바구니의 소계 금액(할인 후, 세금/배송비 전).                                                                 |
| `tax`           | 플로트     | 아니요       | 장바구니에 적용된 총 세금.                                                                                                |
| `shipping`      | 플로트     | 아니요       | 장바구니의 총 배송비.                                                                                             |
| `currency`      | 문자열    | 예      | 3자리 ISO 4217 코드.                                                                                                   |
| `products`      | 배열     | 예      | 이 업데이트의 라인 항목. 전체 교체(`action` 없음 또는 `replace`)의 경우 절대 수량으로 전체 장바구니를 포함합니다. `add` 또는 `remove`의 경우 변경된 라인만 포함합니다. 제품 속성정보를 참조하세요. |
| `source`        | 문자열    | 예      | 이벤트가 발생한 소스.                                                                                             |
| `metadata`      | 오브젝트    | 아니요       | 추가 이벤트 수준 데이터를 위한 유연한 키-값 페어.                                                                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Event properties" }

#### 제품 속성정보 (`products[]`) {#product-properties-products}

| 속성정보        | 데이터 유형 | 필수 | 설명                                     |
|-----------------|-----------|----------|-------------------------------------------------|
| `product_id`    | 문자열    | 예      | 고유 제품 식별자.                      |
| `product_name`  | 문자열    | 예      | 제품 표시 이름.                           |
| `variant_id`    | 문자열    | 예      | 배리언트 식별자.                             |
| `image_url`     | 문자열    | 아니요       | 제품 이미지 URL.                              |
| `product_url`   | 문자열    | 아니요       | 제품 페이지의 URL.                        |
| `quantity`      | 정수   | 예      | 전체 교체(`action` 없음 또는 `replace`)의 경우 이 라인의 장바구니 내 수량. `add` 또는 `remove`의 경우 추가하거나 제거할 수량. |
| `price`         | 플로트     | 예      | 배리언트 단가.                             |
| `metadata`      | 오브젝트    | 아니요       | 유연한 키-값 페어(예: `color` 또는 `size`).   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Product properties (products[])" }

{% comment %}

{% subtabs local %}
{% subtab Web %}

##### `add`

`add` increases quantity or adds a new line. The `quantity` property is how many units to add.

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

`remove` decreases quantity by the amount in `quantity`. The line is removed when quantity reaches `0`.

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

`replace` (or omit `action`) sends the full cart. `total_value` is required.

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

`add` increases quantity or adds a new line. The `quantity` property is how many units to add.

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

`remove` decreases quantity by the amount in `quantity`. The line is removed when quantity reaches `0`.

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

`replace` (or omit `action`) sends the full cart. `total_value` is required.

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

`add` increases quantity or adds a new line. The `quantity` property is how many units to add.

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

`remove` decreases quantity by the amount in `quantity`. The line is removed when quantity reaches `0`.

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

`replace` (or omit `action`) sends the full cart. `total_value` is required.

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

`add` increases quantity or adds a new line. The `quantity` property is how many units to add.

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

`remove` decreases quantity by the amount in `quantity`. The line is removed when quantity reaches `0`.

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

`replace` (or omit `action`) sends the full cart. `total_value` is required.

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

사용자가 결제 플로우를 시작할 때 트리거합니다(예: "결제"를 선택하거나 결제 페이지에 도착한 경우).

#### 클라이언트 측 구현

사용 가능한 SDK eCommerce 이벤트 API를 사용하세요. 플랫폼별 구현 예시는 [Braze SDK를 통한 eCommerce 이벤트 로깅]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events)을 참조하세요.

#### 이벤트 속성정보

| 속성정보       | 유형    | 필수 | 설명                                                                                                      |
|----------------|---------|----------|------------------------------------------------------------------------------------------------------------------|
| checkout_id    | 문자열  | 예      | 결제 세션의 고유 식별자.                                                                      |
| cart_id        | 문자열  | 아니요       | 장바구니 식별자. 사용자의 장바구니 매핑을 위해 장바구니, 결제, 주문 이벤트 간에 공유됩니다.                     |
| total_value    | 플로트   | 예      | 결제의 총 금액.                                                                            |
| subtotal_value | 플로트   | 아니요       | 소계 금액(할인 후, 세금/배송비 전).                                                                |
| tax            | 플로트   | 아니요       | 결제에 적용된 총 세금.                                                                               |
| shipping       | 플로트   | 아니요       | 총 배송비.                                                                                             |
| currency       | 문자열  | 예      | 3자리 ISO 4217 코드.                                                                                      |
| products       | 배열   | 예      | 결제 중인 항목. 제품 속성정보 하위 테이블을 참조하세요.                                                       |
| source         | 문자열  | 예      | 이벤트가 발생한 소스.                                                                                |
| metadata       | 오브젝트  | 아니요       | 유연한 키-값 페어. 인식되는 하위 속성정보: `checkout_url` (문자열)                                       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Event properties" }

#### 제품 속성정보 (`products[]`)

| 속성정보       | 데이터 유형 | 필수 | 설명                                              |
|----------------|-----------|----------|----------------------------------------------------------|
| `product_id`   | 문자열    | 예      | 고유 제품 식별자.                               |
| `product_name` | 문자열    | 예      | 제품 표시 이름.                                    |
| `variant_id`   | 문자열    | 예      | 배리언트 식별자.                                      |
| `image_url`    | 문자열    | 아니요       | 제품 이미지 URL.                                       |
| `product_url`  | 문자열    | 아니요       | 제품 페이지의 URL.                                 |
| `quantity`     | 정수   | 예      | 장바구니에 있는 수량.                             |
| `price`        | 플로트     | 예      | 배리언트 단가.                                      |
| `metadata`     | 오브젝트    | 아니요       | 유연한 키-값 페어(예: color, size).            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Product properties (products[])" }

#### REST API 예시

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

주문이 성공적으로 완료되거나 결제가 확인되었을 때 트리거합니다.

#### 클라이언트 측 구현

사용 가능한 SDK eCommerce 이벤트 API를 사용하세요. 플랫폼별 구현 예시는 [Braze SDK를 통한 eCommerce 이벤트 로깅]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events)을 참조하세요.

{% alert important %}
이 이벤트는 주요 매출 동인입니다. 사용자 프로필에서 `total_value` 값만큼 `total_revenue`를 증가시키고 `total_orders`를 1 증가시킵니다.
{% endalert %}

#### 이벤트 속성정보

| 속성정보        | 데이터 유형 | 필수 | 설명                                                                                   |
|-----------------|-----------|----------|-----------------------------------------------------------------------------------------------|
| `order_id`      | 문자열    | 예      | 주문의 고유 식별자.                                                              |
| `cart_id`       | 문자열    | 아니요       | 장바구니 식별자. 사용자의 장바구니 매핑을 위해 장바구니, 결제, 주문 이벤트 간에 공유됩니다.  |
| `total_value`   | 플로트     | 예      | 주문의 총 금액.                                                            |
| `subtotal_value`| 플로트     | 아니요       | 소계 금액(할인 후, 세금/배송비 전).                                             |
| `tax`           | 플로트     | 아니요       | 주문에 적용된 총 세금.                                                               |
| `shipping`      | 플로트     | 아니요       | 총 배송비.                                                                          |
| `currency`      | 문자열    | 예      | 3자리 ISO 4217 코드.                                                                   |
| `total_discounts`| 플로트    | 아니요       | 주문에 적용된 총 할인 금액.                                               |
| `discounts`     | 배열     | 아니요       | 적용된 할인의 상세 목록.                                                           |
| `products`      | 배열     | 예      | 주문에 포함된 항목. 제품 속성정보 하위 테이블을 참조하세요.                                         |
| `source`        | 문자열    | 예      | 이벤트가 발생한 소스.                                                             |
| `metadata`      | 오브젝트    | 아니요       | 유연한 키-값 페어. 인식되는 하위 속성정보: `order_status_url` (문자열)                |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Event properties" }

#### 제품 속성정보 (`products[]`)

| 속성정보        | 데이터 유형 | 필수 | 설명                                 |
|-----------------|-----------|----------|---------------------------------------------|
| `product_id`    | 문자열    | 예      | 고유 제품 식별자.                  |
| `product_name`  | 문자열    | 예      | 제품 표시 이름.                       |
| `variant_id`    | 문자열    | 예      | 배리언트 식별자.                         |
| `image_url`     | 문자열    | 아니요       | 제품 이미지 URL.                          |
| `product_url`   | 문자열    | 아니요       | 제품 페이지의 URL.                    |
| `quantity`      | 정수   | 예      | 장바구니에 있는 수량.                |
| `price`         | 플로트     | 예      | 배리언트 단가.                         |
| `metadata`      | 오브젝트    | 아니요       | 유연한 키-값 페어(예: `color` 또는 `size`).|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Product properties (products[])" }

#### REST API 예시

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

주문이 취소되었을 때 트리거합니다.

#### 클라이언트 측 구현

`logCustomEvent`를 사용합니다. 플랫폼별 구현 예시는 [Braze SDK를 통한 eCommerce 이벤트 로깅]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events)을 참조하세요.

{% alert important %}
이 이벤트는 사용자 프로필에서 `total_orders`를 1 감소시킵니다. `total_revenue`에는 영향을 미치지 않습니다. 매출을 조정하려면 `order_refunded`를 사용하세요.
{% endalert %}

#### 이벤트 속성정보

| 속성정보         | 유형    | 필수 | 설명                                                                                      |
|------------------|---------|----------|--------------------------------------------------------------------------------------------------|
| `order_id`       | 문자열  | 예      | 주문의 고유 식별자.                                                                 |
| `total_value`    | 플로트   | 예      | 취소되는 주문의 총 금액. 0 이상이어야 합니다. 절대값을 전송하면 Braze가 감소를 처리합니다. |
| `subtotal_value` | 플로트   | 아니요       | 소계 금액(할인 후, 세금/배송비 전).                                                |
| `tax`            | 플로트   | 아니요       | 주문에 적용된 총 세금.                                                                  |
| `shipping`       | 플로트   | 아니요       | 총 배송비.                                                                             |
| `currency`       | 문자열  | 예      | 3자리 ISO 4217 코드.                                                                      |
| `total_discounts`| 플로트   | 아니요       | 주문에 적용된 총 할인 금액.                                                  |
| `discounts`      | 배열   | 아니요       | 적용된 할인의 상세 목록.                                                              |
| `cancel_reason`  | 문자열  | 예      | 주문이 취소된 이유.                                                                  |
| `products`       | 배열   | 예      | 취소된 주문의 항목. 제품 속성정보 하위 테이블을 참조하세요.                                  |
| `source`         | 문자열  | 예      | 이벤트가 발생한 소스.                                                                |
| `metadata`       | 오브젝트  | 아니요       | 유연한 키-값 페어. 인식되는 하위 속성정보: `order_status_url` (문자열)                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Event properties" }

#### 제품 속성정보 (`products[]`)

| 속성정보       | 데이터 유형 | 필수 | 설명                                   |
|----------------|-----------|----------|-----------------------------------------------|
| `product_id`   | 문자열    | 예      | 고유 제품 식별자.                    |
| `product_name` | 문자열    | 예      | 제품 표시 이름.                         |
| `variant_id`   | 문자열    | 예      | 배리언트 식별자.                           |
| `image_url`    | 문자열    | 아니요       | 제품 이미지 URL.                            |
| `product_url`  | 문자열    | 아니요       | 제품 페이지의 URL.                      |
| `quantity`     | 정수   | 예      | 장바구니에 있는 수량.                  |
| `price`        | 플로트     | 예      | 배리언트 단가.                           |
| `metadata`     | 오브젝트    | 아니요       | 유연한 키-값 페어(예: `color` 또는 `size`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Product properties (products[])" }

#### REST API 예시

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

전체 또는 부분 환불이 발생했을 때 트리거합니다.

#### 클라이언트 측 구현

`logCustomEvent`를 사용합니다. 플랫폼별 구현 예시는 [Braze SDK를 통한 eCommerce 이벤트 로깅]({{site.baseurl}}/developer_guide/analytics/logging_ecommerce_events)을 참조하세요.

{% alert important %}
이 이벤트는 사용자 프로필에서 `total_value` 값만큼 `total_revenue`를 감소시키고 `total_refunds`를 증가시킵니다. 부분 환불의 경우, `total_value`를 원래 주문 총액이 아닌 환불 금액만으로 설정하세요.
{% endalert %}

#### 이벤트 속성정보

| 속성정보          | 데이터 유형 | 필수 | 설명                                                                                          |
|-------------------|-----------|----------|------------------------------------------------------------------------------------------------------|
| `order_id`        | 문자열    | 예      | 원래 주문의 고유 식별자.                                                            |
| `total_value`     | 플로트     | 예      | 환불의 총 금액. 0 이상이어야 합니다. 절대값을 전송하면 Braze가 total_refunds 증가를 처리합니다. |
| `currency`        | 문자열    | 예      | 3자리 ISO 4217 코드.                                                                          |
| `total_discounts` | 플로트     | 아니요       | 원래 적용된 총 할인 금액.                                                        |
| `discounts`       | 배열     | 아니요       | 할인의 상세 목록.                                                                          |
| `products`        | 배열     | 예      | 환불되는 항목. 제품 속성정보 하위 테이블을 참조하세요.                                              |
| `source`          | 문자열    | 예      | 이벤트가 발생한 소스.                                                                    |
| `metadata`        | 오브젝트    | 아니요       | 유연한 키-값 페어. 인식되는 하위 속성정보: `order_status_url` (문자열).                      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Event properties" }

#### 제품 속성정보 (`products[]`)

| 속성정보        | 데이터 유형 | 필수 | 설명                                           |
|-----------------|-----------|----------|-------------------------------------------------------|
| `product_id`    | 문자열    | 예      | 고유 제품 식별자.                            |
| `product_name`  | 문자열    | 예      | 제품 표시 이름.                                 |
| `variant_id`    | 문자열    | 예      | 배리언트 식별자.                                   |
| `image_url`     | 문자열    | 아니요       | 제품 이미지 URL.                                    |
| `product_url`   | 문자열    | 아니요       | 제품 페이지의 URL.                              |
| `quantity`      | 정수   | 예      | 장바구니에 있는 수량.                          |
| `price`         | 플로트     | 예      | 배리언트 단가.                                   |
| `metadata`      | 오브젝트    | 아니요       | 유연한 키-값 페어(예: `color` 또는 `size`).         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Product properties (products[])" }

#### REST API 예시 {#rest-api-examples}

{% subtabs %}
{% subtab 전체 환불 %}

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
{% subtab 부분 환불 %}

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

### eCommerce 이벤트 후처리 {#ecommerce-event-post-processing}

eCommerce 이벤트를 전송하면 Braze는 해당 이벤트 이름에 대한 예상 스키마에 대해 유효성을 검사합니다.

다음 테이블은 유효성 검사를 통과했을 때 Braze가 각 이벤트에 대해 자동으로 수행하는 작업을 요약합니다. 유효성 검사가 실패했을 때의 동작은 [이벤트 유효성 검사 및 문제 해결](#event-validation-and-troubleshooting)을 참조하세요.

| 이벤트                        | Braze가 자동으로 수행하는 작업                                                                                     |
|------------------------------|-------------------------------------------------------------------------------------------------------------------|
| `ecommerce.order_placed`     | 사용자 프로필에서 `total_value`만큼 **총 매출**을 증가시키고 **총 주문 수**를 1 증가시킵니다.                     |
| `ecommerce.order_cancelled`  | **총 주문 수**를 1 감소시킵니다.                                                                                 |
| `ecommerce.order_refunded`   | `total_value`만큼 **총 매출**을 감소시키고 **총 환불 금액**을 증가시킵니다.                              |
| `ecommerce.cart_updated`     | 사용자 프로필에 장바구니 매핑 오브젝트를 생성하거나 업데이트합니다(전체 장바구니 페이로드 또는 선택적 `action`: `add`, `remove`, `replace`를 사용한 증분 장바구니 업데이트). 장바구니는 업데이트 없이 30일이 지나면 만료됩니다.|
| `ecommerce.product_viewed`   | 사용자 프로필 변경 없음. 세분화, 트리거, 아이템 추천과 같은 BrazeAI<sup>TM</sup> 기능에 사용할 수 있습니다.|
| `ecommerce.checkout_started` | 사용자 프로필 변경 없음. 세분화 및 트리거(예: 유기한 결제 플로우)에 사용할 수 있습니다.        |
{: .reset-td-br-1 .reset-td-br-2 aria-label="eCommerce 이벤트 후처리" }

{% alert important %}
비 USD 통화 값은 이벤트가 보고된 날짜의 환율을 사용하여 자동으로 USD로 변환됩니다. 이미 USD로 보고하고 있다면 의도하지 않은 변환을 방지하기 위해 통화를 `USD`로 하드코딩하세요.
{% endalert %}

## 구현 세부 사항 {#implementation-details}

### 데이터 포인트 및 과금 {#data-points-and-billing}

eCommerce 이벤트는 [데이터 포인트]({{site.baseurl}}/user_guide/data/infrastructure/data_points)를 소비하지 않습니다. 데이터 포인트 사용량에 영향을 주지 않고 기록할 수 있습니다.

### 이벤트 크기 제한 {#event-size-limit}

`/users/track`으로 전송되는 이벤트 속성정보는 이벤트당 102,400바이트(100KB)로 제한됩니다. 트리거된 Campaign 및 Canvas 메시지의 경우, [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) 및 [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)로 전송되는 `trigger_properties`는 기본 제한이 51,200바이트(50KB)로 더 엄격합니다.

모범 사례로, 이벤트를 트리거하거나 개인화하거나 귀속시키는 데 필요한 제품 정보만 전송하세요. 설명, 전체 배리언트 목록, 재고, 대체 이미지 등 더 풍부한 제품 세부 정보는 Braze 카탈로그에 저장하세요. 메시지를 전송할 때 `product_id` 또는 `variant_id`로 이러한 세부 정보를 참조하세요. `metadata` 오브젝트는 메시징에서 사용할 주문 또는 제품별 컨텍스트에 선택적으로 사용하세요.

### 통화 처리 {#currency-handling}

Braze는 이벤트가 보고된 날짜의 환율을 사용하여 비 USD 통화 값을 자동으로 USD로 변환합니다. 이 변환된 값이 매출 측정기준에 표시됩니다.

{% alert tip %}
USD로만 운영하는 경우, 불필요한 변환을 방지하기 위해 모든 이벤트에서 `"currency": "USD"`를 하드코딩하세요.
{% endalert %}

### 소스 필드 {#source-field}

소스 속성정보는 이벤트가 발생한 위치를 식별하는 필수 문자열입니다. 예를 들어, `shopify`, `in-store POS`, `custom_api` 등이 있습니다. 이를 통해 Currents 내보내기에서 데이터를 분석하거나 유효성 검사 문제를 디버깅할 때 통합 소스를 구분할 수 있습니다.

### 메타데이터 유연성 {#metadata-flexibility}

이벤트 수준 및 제품 수준 메타데이터 오브젝트 모두 임의의 키-값 페어를 허용하므로, 핵심 스키마를 수정하지 않고도 커스텀 차원을 첨부할 수 있습니다. 일반적인 예로는 `order_status_url`, `gift_wrapped`, `loyalty_points_earned`, `warehouse_id` 등이 있습니다. 이러한 속성정보는 Liquid 개인화, Currents 내보내기, [세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension)을 통한 세분화에서 사용할 수 있습니다.

{% alert important %}
추천 이벤트는 엄격한 스키마를 사용합니다. 따라서 속성정보의 최상위 수준에 커스텀 속성정보를 추가하면 유효성 검사에 실패합니다. 모든 커스텀 속성정보는 이벤트 수준 `metadata` 오브젝트 또는 `products[]` 내부의 제품 수준 `metadata` 오브젝트에 넣으세요. 이러한 속성정보는 최상위 필드와 마찬가지로 Liquid, Currents, 세분화에서 사용할 수 있습니다.
{% endalert %}

## 이벤트 유효성 검사 및 문제 해결 {#event-validation-and-troubleshooting}

`/users/track` 또는 Braze SDK를 통해 추천 eCommerce 이벤트를 전송하면, Braze는 추천 이벤트 처리 중에 이벤트의 JSON 스키마에 대해 페이로드의 유효성을 검사합니다. 유효성 검사는 이름이 추천 이벤트와 정확히 일치하는 모든 이벤트(예: `ecommerce.order_placed` 또는 `ecommerce.cart_updated`)에 대해 자동으로 실행됩니다.

### 유효성 검사 항목 {#what-we-validate}

이름이 eCommerce 추천 이벤트와 일치하는 각 이벤트에 대해 Braze는 다음을 확인합니다:

| 확인 항목                     | 예시                                                                                                                      |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------|
| 이벤트 이름                | 정확해야 합니다. 예를 들어, `ecommerce.cart_updated`가 올바르며 `ecommerce.Cart_Updated`, `cartupdated`, `cart_updated`는 올바르지 않습니다. |
| 필수 속성정보 존재 여부 | `order_placed`에는 `order_id`, `total_value`, `currency`, `products`, `source`가 필요합니다.                                   |
| 올바른 데이터 유형        | `total_value`는 숫자여야 하고, `currency`는 문자열이어야 하며, `products`는 배열이어야 합니다.                                   |
| 최상위 수준에 추가 속성정보 없음 | 속성정보 아래의 커스텀 필드는 실패를 유발합니다. 대신 `metadata` 오브젝트를 사용하세요.                                         |
| 값 제약 조건         | 금액 필드는 `0` 이상이어야 합니다. `currency`는 유효한 ISO 4217 문자열이어야 합니다.                                                  |
| 제품별 필드        | `products[]`의 각 항목에는 `product_id`, `product_name`, `variant_id`, `quantity`, `price`가 포함되어야 합니다.                 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="What we validate" }

### 유효성 검사를 하는 이유 {#why-we-validate}

eCommerce 이벤트는 매출 추적, {% raw %}`{% shopping_cart %}`{% endraw %} Liquid 태그, 유기한 장바구니 트리거, 리포팅 등 일관되고 예측 가능한 데이터에 의존하는 기능을 구동합니다. 페이로드가 스키마에서 벗어나면 이러한 기능이 잘못된 매출 합계, 누락된 장바구니, 깨진 트리거 등 조용한 부정확성을 생성합니다. 유효성 검사는 다운스트림 기능이 예측 가능하게 동작하도록 계약을 사전에 적용합니다.

### 유효성 검사 통과 시 {#when-validation-passes}

이벤트는 모든 관련 후처리와 함께 eCommerce 추천 이벤트로 처리됩니다. 각 이벤트 유형에 의해 트리거되는 동작의 전체 목록은 [이벤트 스키마](#event-schemas)를 참조하세요.

#### 성공적인 이벤트 확인 {#verify-a-successful-event}

이벤트를 전송한 후 다음 방법 중 하나를 사용하여 이벤트가 수락되고 올바르게 처리되었는지 확인할 수 있습니다:

- [이벤트 사용자 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log): 대시보드에서 사용자의 프로필을 열고 활동을 검토합니다. 추천 이벤트는 전체 속성정보 페이로드와 함께 표시되므로, 이벤트가 도착했는지와 값이 전송한 것과 일치하는지 확인할 수 있습니다.
- [커스텀 이벤트 보고서]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report): **Analytics** > **Custom Events**로 이동하여 시간에 따른 각 추천 이벤트의 집계 수를 확인합니다. 이는 통합이 라이브 상태일 때 프로덕션 트래픽이 예상대로 흐르고 있는지 확인하는 데 유용합니다.
- [테스트 사용자]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups?utm_source=operator_user&utm_medium=dashboard#adding-test-users): 개발 워크스페이스에서 사용자를 테스트 사용자로 표시한 다음, 해당 사용자에 대해 통합에서 이벤트를 트리거합니다. 테스트 사용자는 대시보드에서 플래그가 지정되어 엔드투엔드 동작을 쉽게 격리하고 검사할 수 있습니다.

### 유효성 검사 실패 시 {#when-validation-fails}

이벤트는 추천 이벤트로 처리되지 않습니다. 구체적으로:

- **이벤트가 완전히 삭제됩니다.** 유효하지 않은 추천 eCommerce 이벤트는 사용자 프로필에 기록되지 않고, Currents에 표시되지 않으며, 세분화에 사용할 수 없습니다.
- 다음을 포함한 다운스트림 추천 이벤트 기능이 실행되지 않습니다:
  - 매출 추적(매출 리포팅, `total_revenue`와 같은 사용자 계산 필드)
  - 사용자 프로필의 장바구니 오브젝트 업데이트
  - Canvas 및 Campaigns의 "장바구니 업데이트 이벤트 수행" 또는 "주문 완료" 트리거

오류 보고 방식은 수집 경로에 따라 다릅니다:

- **REST API (`/users/track`):** 각 유효하지 않은 이벤트는 응답의 errors 배열에 보고됩니다. 각 항목은 어떤 이벤트가 실패했는지(인덱스)와 이유(유형)를 알려줍니다. 최상위 message 필드는 여전히 "success"라고 표시되는데, 이는 요청이 Braze에 도달했다는 의미일 뿐 모든 이벤트가 유효하다는 의미가 아닙니다. 항상 응답에서 errors 배열을 확인하세요.
- **Braze SDK:** SDK 호출은 즉시 반환되고 유효성 검사는 백그라운드에서 실행되므로, 오류가 앱으로 다시 전송되지 않습니다. eCommerce 이벤트 유효성 검사 실패에 대해 알아보려면 실패 요약 이메일을 확인하세요([실패 찾기](#find-failures) 참조).

#### API 오류 응답 예시 {#example-api-error-response}

`/users/track` 엔드포인트는 어떤 속성정보가 실패했는지와 이유를 나타내는 필드 수준 오류를 반환합니다. 최상위 `message`는 이벤트가 파이프라인에 수락되었기 때문에 `"success"`를 반환할 수 있습니다. `errors` 배열이 스키마 유효성 검사에 실패한 필드를 알려줍니다. 다음 오류 응답 예시를 참조하세요.

```json
{
 "message": "success",
 "errors": [{ "index": 0, "input_array": "purchases", "type": "'currency' must be an ISO 4217 currency" }]
}
```

실패는 내부적으로 분류되고 실패 요약 이메일을 위해 집계됩니다:

| 실패 유형           | 의미                                           | 예시                                                        |
|------------------------|---------------------------------------------------|----------------------------------------------------------------|
| `missing_property`     | 필수 필드가 없습니다.                       | `order_placed`가 `order_id` 없이 전송됨.                        |
| `extra_property`       | 스키마에 정의되지 않은 필드가 추가되었습니다. | `metadata` 내부가 아닌 `properties` 최상위에 커스텀 `gift_wrapped` 필드가 있음. |
| `unexpected_data_type` | 필드의 유형이 잘못되었습니다.                        | `total_value: "29.99"` (문자열) 대신 `29.99` (숫자)여야 함.   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="API 오류 응답 예시" }

{% alert note %}
추천 이벤트와 정확히 일치하지 않는 이벤트 이름(예: `ecommerce.OrderPlaced`)은 유효성 검사를 완전히 건너뛰고 일반 커스텀 이벤트로 기록됩니다. 전송한 이름으로 Currents 및 세분화에 표시되지만, 추천 이벤트 처리를 받지 않으며 응답에 `errors` 항목이 포함되지 않습니다.
{% endalert %}

#### 실패 찾기 {#find-failures}

Braze는 워크스페이스 관리자에게 추천 이벤트 유효성 검사 실패 요약을 이메일로 전송하여, 모든 이벤트를 수동으로 모니터링하지 않고도 통합 문제를 식별하고 수정할 수 있도록 합니다.

요약 이메일에는 다음이 포함됩니다:

- **총 오류 수:** 보고 기간의 오류 수.
- **이벤트별 오류:** 각 추천 이벤트 유형(예: `ecommerce.cart_updated` 및 `ecommerce.order_placed`)에 대해 실패한 이벤트 수의 분석. 이를 통해 통합에서 먼저 주의가 필요한 이벤트를 식별할 수 있습니다.
- **소스별 오류:** API와 SDK 간의 분할로, 어떤 통합이 실패를 생성하고 있는지 정확히 파악할 수 있습니다.

이러한 이메일을 받지 못하거나 수신자 목록을 확인하려면 Braze 계정 팀에 문의하세요.

#### 실패 진단 및 수정 {#diagnose-and-fix-failures}

실패 요약 이메일을 받으면:

1. **실패한 이벤트와 소스를 식별합니다.** 이메일은 이벤트 이름과 통합 소스(`sdk` 대 `rest_api`)별로 실패를 구분하므로, 수정이 필요한 통합을 정확히 파악할 수 있습니다. 동일한 이벤트를 전송하는 여러 소스가 있는 경우(예: 스토어프론트 SDK와 백엔드 웹훅 모두 `cart_updated`를 전송), 각각 독립적으로 처리하세요.
2. **페이로드를 [이벤트 스키마](#event-schemas)의 스키마와 비교합니다.** 대부분의 실패는 다음 세 가지 패턴 중 하나에 해당합니다:
   - `missing_property`: 필수 필드가 없습니다. 해결하려면 필수 필드를 추가하세요.
   - `extra_property`: 커스텀 필드가 `properties`의 최상위 수준에 있습니다. 해결하려면 커스텀 필드를 `metadata`(이벤트 수준) 또는 `products[].metadata`(제품별)로 이동하세요.
   - `unexpected_data_type`: 값의 유형이 잘못되었습니다(예: `total_value`가 문자열로 전송됨). 해결하려면 전송 전에 값을 변환하세요.
3. **프로덕션에 배포하기 전에 개발 워크스페이스에서 수정된 페이로드를 테스트합니다.** 테스트 사용자에 대해 알려진 테스트 이벤트를 전송한 다음, 해당 사용자의 프로필에서 예상되는 추천 이벤트 동작을 확인합니다(예: 장바구니 오브젝트 업데이트, 매출 증가, 유기한 장바구니 트리거 발동).
4. **다음 실패 이메일을 모니터링하여** 해당 이벤트, 소스, 유형에 대한 실패 수가 0으로 떨어지는지 확인합니다.

이벤트별 전체 속성정보 요구 사항은 [이벤트 스키마](#event-schemas)를 참조하세요.