---
nav_title: "구매 오브젝트"
article_title: API 구매 오브젝트
page_order: 8
page_type: reference
description: "이 참조 문서에서는 구매 오브젝트의 다양한 구성요소, 올바른 사용 방법 및 참고할 수 있는 예시를 설명합니다."

---

# 구매 오브젝트 {#purchase-object}

> 이 문서에서는 구매 오브젝트의 다양한 구성요소, 올바른 사용 방법, 모범 사례 및 참고할 수 있는 예시를 설명합니다.

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

## 구매 오브젝트란 무엇인가요? {#what-is-a-purchase-object}

구매 오브젝트는 구매가 이루어졌을 때 API를 통해 전달되는 오브젝트입니다. 각 구매 오브젝트는 구매 배열 내에 위치하며, 각 오브젝트는 특정 사용자가 특정 시점에 수행한 단일 구매를 나타냅니다. 구매 오브젝트에는 Braze 백엔드가 커스터마이징, 데이터 수집, 개인화를 위해 이 정보를 저장하고 사용할 수 있도록 하는 다양한 필드가 있습니다.

### 오브젝트 본문 {#object-body}

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required.
  "external_id" : (optional, string) External user ID,
  "user_alias" : (optional, User Alias Object) User alias object,
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  "app_id" : (optional, string) see App Identifier,
  // See the following product_id naming conventions for clarification.
  "product_id" : (required, string) identifier for the purchase, for example, Product Name or Product Category,
  "currency" : (required, string) ISO 4217 Alphabetic Currency Code,
  //Revenue from a purchase object is calculated as the product of quantity and price.
  "price" : (required, float) value in the base currency unit (for example, Dollars for USD, Yen for JPY),
  "quantity" : (optional, integer) the quantity purchased (defaults to 1, must be <= 100 -- currently, Braze treats a quantity _X_ as _X_ separate purchases with quantity 1),
  "time" : (required, datetime as string in ISO 8601) Time of purchase,
  // See the following purchase object explanation for clarification.
  "properties" : (optional, Properties Object) properties of the event,
  // Setting this flag to true puts the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean)
}
```

{% alert note %}
미래 타임스탬프가 포함된 구매는 기본적으로 현재 시간으로 설정됩니다. 이를 통해 구매 이벤트가 정확한 타이밍으로 기록됩니다.
{% endalert %}

- [외부 사용자 ID]({{site.baseurl}}/api/basics#user-ids)
- [앱 식별자]({{site.baseurl}}/api/identifier_types)
- [ISO 4217 통화 코드 위키](http://en.wikipedia.org/wiki/ISO_4217)
- [ISO 8601 시간 코드 위키](https://en.wikipedia.org/wiki/ISO_8601)

{% alert note %}
일부 식별자 쌍은 함께 사용할 수 없으며, 두 가지가 모두 제공된 경우 `email`이 `phone`보다 우선합니다. 자세한 내용은 [식별자 확인]({{site.baseurl}}/api/objects_filters/user_attributes_object#identifier-resolution)을 참조하세요.
{% endalert %}

## 구매 제품 ID {#purchase-product-id}

구매 오브젝트 내에서 `product_id`는 구매에 대한 식별자입니다(예: `Product Name` 또는 `Product Category`).

- Braze에서는 대시보드에 최대 5,000개의 `product_id`를 저장할 수 있습니다.
- `product_id`는 최대 255자까지 가능합니다.

### 명명 규칙 {#naming-conventions}

Braze에서는 구매 오브젝트 `product_id`에 대한 몇 가지 일반적인 명명 규칙을 제공합니다. `product_id`를 선택할 때, Braze는 이 `product_id`로 기록된 모든 항목을 그룹화할 수 있도록 SKU 대신 제품 이름이나 제품 카테고리와 같은 간단한 이름을 사용할 것을 권장합니다.

이렇게 하면 세분화 및 트리거에 사용할 제품을 더 쉽게 식별할 수 있습니다.

### 주문 수준에서 구매 기록하기 {#log-purchases-at-the-order-level}

제품 수준이 아닌 주문 수준에서 구매를 기록하려면 주문 이름이나 주문 카테고리를 `product_id`로 사용할 수 있습니다(예: `Online Order` 또는 `Completed Order`).

예를 들어, 웹 SDK에서 주문 수준으로 구매를 기록하려면 다음과 같이 합니다:

```html
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "purchases" : [
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "Completed Order",
      "currency" : "USD",
      "price" : 219.98,
      "time" : "2013-07-16T19:20:30+01:00",
      "properties" : {
        "products" : [ { "name": "Monitor", "category": "Gaming", "product_amount": 19.99, },
        { "name": "Gaming Keyboard", "category": "Gaming ", "product_amount": 199.99, }
        ]
      }
    }
  ]
}
```

## 구매 등록정보 오브젝트 {#purchase-properties-object}

{% include data_activation/purchase_event_property_data_types.md %}

커스텀 속성, 이벤트 등록정보 및 카탈로그 전반에 걸친 데이터 유형에 대한 통합 참조는 [데이터 유형]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#purchase-event-property-data-types)을 참조하세요.

### 구매 등록정보 {#purchase-properties}

[구매 등록정보]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events#purchase-properties)를 사용하여 메시지를 트리거하고 Liquid를 사용하여 개인화할 수 있으며, 이러한 등록정보를 기반으로 세분화할 수도 있습니다.

{% include data_activation/segmentable_purchase_properties_keys_note.md %}

#### 명명 규칙

이 기능은 구매 단위가 아닌 **제품 단위로** 설정된다는 점에 유의하세요. 예를 들어, 고유한 제품 수가 많지만 각각의 등록정보가 동일한 경우 세분화가 불필요할 수 있습니다.

이 경우 데이터 구조를 설정할 때 트랜잭션 수준 식별자 대신 "그룹 수준"에서 제품 이름을 사용하는 것이 좋습니다. 예를 들어, 기차표 회사는 "거래 123" 또는 "거래 046"과 같은 특정 거래가 아닌 "편도 여행", "왕복 여행", "다구간 여행"에 대한 제품을 보유해야 합니다. 또 다른 예로, "음식" 구매 이벤트의 경우 등록정보를 "케이크"와 "샌드위치"로 설정하는 것이 가장 좋습니다.

{% alert important %}
Braze REST API를 통해 제품을 추가할 수 있습니다. 예를 들어, `/users/track` 엔드포인트에 호출을 보내고 새로운 구매 ID를 포함하면, Braze는 대시보드의 **데이터 설정** > **제품** 섹션에 자동으로 제품을 생성합니다.
{% endalert %}

### 구매 오브젝트 예시 {#example-purchase-object}

```html
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "purchases" : [
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "backpack",
      "currency" : "USD",
      "price" : 40.00,
      "time" : "2013-07-16T19:20:30+01:00",
      "properties" : {
        "color" : "red",
        "monogram" : "ABC",
        "checkout_duration" : 180,
        "size" : "Large",
        "brand" : "Backpack Locker"
      }
    },
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "pencil",
      "currency" : "USD",
      "price" : 2.00,
      "time" : "2013-07-17T19:20:20+01:00",
      "properties" : {
        "number" : 2,
        "sharpened" : true
      }
    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "pen",
      "currency" : "USD",
      "price" : 2.50,
      "time" : "2013-07-17T19:20:20+01:00",
      "properties" : {
        "color" : "blue",
      }
    }
  ]
}
```

### 구매 오브젝트, 이벤트 오브젝트 및 웹훅 {#purchase-objects-event-objects-and-webhooks}

위의 예시를 통해 누군가 색상, 모노그램, 결제 소요 시간, 사이즈, 브랜드 등의 등록정보를 가진 배낭을 구매했음을 알 수 있습니다. 그런 다음 [구매 이벤트 등록정보]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events#purchase-properties)를 사용하여 이러한 등록정보로 세그먼트를 만들거나 Liquid를 사용하여 채널을 통해 커스텀 메시지를 보낼 수 있습니다. 예를 들어, "안녕하세요 **Ann F.** 님, **빨간색 중형 배낭**을 **$40.00**에 구매해 주셔서 감사합니다! **Backpack Locker**에서 쇼핑해 주셔서 감사합니다!"

세분화에 사용할 등록정보를 저장하고 추적하려면 해당 등록정보를 커스텀 속성으로 설정해야 합니다. 이는 [세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension)을 사용하여 수행할 수 있으며, 해당 고객 프로필의 수명 기간 동안 저장된 커스텀 이벤트 또는 구매 동작을 기반으로 사용자를 타겟팅할 수 있습니다.