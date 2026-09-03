---
nav_title: AI 추천
article_title: AI 항목 추천 만들기
description: "이 참조 문서에서는 카탈로그에 있는 항목에 대한 AI 항목 추천을 생성하는 방법을 다룹니다."
page_order: 1
---

# AI 항목 추천 만들기 {#create-ai-item-recommendations}

> 카탈로그에 있는 항목으로 AI 추천 엔진을 만드는 방법을 알아보세요.

## AI 항목 추천 정보 {#about-ai-item-recommendations}

AI 항목 추천을 사용하여 가장 인기 있는 제품을 계산하거나 특정 [카탈로그]({{site.baseurl}}/user_guide/brazeai/item_recommendations)에 대한 개인화된 AI 추천을 만들 수 있습니다. 추천을 만든 후 개인화를 사용하여 해당 제품을 메시지에 삽입할 수 있습니다.

{% alert tip %}
[AI Personalized 추천](#recommendation-types)은 최소 수백 개의 카탈로그 항목, 최대 100,000개의 카탈로그 항목, 그리고 일반적으로 최소 30,000명의 구매 또는 상호작용 데이터가 있는 사용자와 함께 사용할 때 가장 효과적입니다. 이것은 대략적인 가이드일 뿐이며 상황에 따라 달라질 수 있습니다. 다른 추천 유형은 **Most popular**를 대체로 사용하는 경우를 포함하여 더 적은 데이터로도 작동할 수 있습니다.
{% endalert %}

{% multi_lang_include brazeai/recommendations/ai.md section="Plan-specific features" %}

## AI 항목 추천 만들기 {#creating-an-ai-item-recommendation}

### 사전 준비 사항 {#prerequisites}

시작하기 전에 다음 사항이 필요합니다:

- [추천 유형]({{site.baseurl}}/user_guide/data/activation/catalogs) 중 하나를 사용하려면 최소 하나의 [카탈로그]({{site.baseurl}}/user_guide/data/activation/catalogs)가 필요합니다.
- 항목에 대한 참조를 포함하고 카탈로그 항목 ID와 일치해야 하는 Braze의 구매 또는 이벤트 데이터(커스텀 이벤트, 주문 완료 이벤트 또는 구매 객체)가 필요합니다.

### 1단계: 새 추천 만들기 {#step-1-create-a-new-recommendation}

대시보드의 다음 두 곳에서 AI 항목 추천을 만들 수 있습니다:

{% tabs local %}
{% tab 내비게이션 메뉴에서 %}
1. **Analytics** > **AI Item Recommendation**으로 이동합니다.
2. **Create Prediction** > **AI Item Recommendation**을 선택합니다.
{% endtab %}

{% tab 카탈로그에서 %}
개별 카탈로그에서 직접 추천을 만들 수도 있습니다. **Catalogs** 페이지에서 카탈로그를 선택한 다음 **Create Recommendation**을 선택합니다.
{% endtab %}
{% endtabs %}

### 2단계: 추천 세부 정보 추가하기 {#step-2-add-recommendation-details}

추천에 이름과 선택적 설명을 입력합니다.

!["추천 세부 정보" 단계에서 이름과 설명 필드가 표시됩니다.]({% image_buster /assets/img/item_recs_1.png %})

### 3단계: 추천 정의하기 {#recommendation-type}

추천 유형을 선택합니다. 각 유형은 구매, 주문 완료 또는 커스텀 이벤트 데이터와 같은 최근 6개월간의 항목 상호작용 데이터를 사용합니다. 각 유형에 대한 자세한 정보와 사용 사례는 [유형 및 사용 사례]({{site.baseurl}}/user_guide/brazeai/item_recommendations)를 참조하세요.

{% alert tip %}
**Most Recent** 또는 **AI Personalized**를 사용할 때, 개인화된 추천을 생성할 데이터가 부족한 사용자에게는 대체로 **Most Popular** 항목이 제공됩니다. **Most Popular** 대체 항목은 연결된 카탈로그에 존재하는 항목만 반환합니다.<br><br>**AI Personalized** 추천의 경우, **Analytics** 페이지에서 **Personalization rate**를 확인하여 지난 24개월 동안 구성된 이벤트를 수행한 사용자 중 프로필에 개인화된 추천이 저장된 비율을 볼 수 있습니다. **Most Recent** 추천의 경우, **Analytics** 페이지에서 **Most Recent** 추천을 받는 사용자와 **Most Popular** 대체 항목을 받는 사용자의 비율을 확인할 수 있습니다.
{% endalert %}

#### 3.1단계: 이전 구매 또는 상호작용 제외하기 (선택 사항) {#step-31-exclude-prior-purchases-or-interactions-optional}

사용자가 이미 구매하거나 상호작용한 항목을 추천하지 않으려면, **Do not recommend items users have previously interacted with**를 선택합니다. 이 옵션은 추천 **Type**이 **AI Personalized**로 설정된 경우에만 사용할 수 있습니다.

!["추천 정의하기" 단계에서 "AI Personalized" 유형과 "Do not recommend items users have previously interacted with" 옵션이 선택된 모습입니다.]({% image_buster /assets/img/item_recs_2-3.png %})

이 설정은 추천이 최근에 업데이트된 경우, 사용자가 이미 구매하거나 상호작용한 항목을 메시지에서 재사용하지 않도록 합니다. 추천 업데이트 사이에 구매하거나 상호작용한 항목은 여전히 표시될 수 있습니다. 항목 추천의 무료 버전은 주별로, AI 항목 추천의 프로 버전은 24시간마다 업데이트됩니다.

예를 들어, AI 항목 추천 프로 버전을 사용할 때, 사용자가 무언가를 구매한 후 30분 이내에 마케팅 이메일을 받으면, 방금 구매한 항목이 이메일에서 제외되지 않을 수 있습니다. 그러나 24시간 이후에 전송되는 모든 메시지에는 해당 항목이 포함되지 않습니다.

#### 3.2단계: 카탈로그 선택하기 {#step-32-select-a-catalog}

아직 채워지지 않은 경우, 이 추천이 항목을 가져올 [카탈로그]({{site.baseurl}}/user_guide/data/activation/catalogs)를 선택합니다.

#### 3.3단계: 셀렉션 추가하기 (선택 사항) {#step-33-add-a-selection-optional}

추천을 더 세밀하게 제어하려면, [셀렉션]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)을 선택하여 커스텀 필터를 적용합니다. 셀렉션은 브랜드, 사이즈 또는 위치와 같은 카탈로그의 특정 열을 기준으로 추천을 필터링합니다. Liquid를 포함하는 셀렉션은 추천에 사용할 수 없습니다.

![추천에 "in-stock" 셀렉션이 선택된 예시입니다.]({% image_buster /assets/img/item_recs_2-2.png %})

{% alert tip %}
셀렉션을 찾을 수 없는 경우, 먼저 카탈로그에서 셀렉션이 설정되어 있는지 확인하세요.
{% endalert %}

### 4단계: 추천을 주도할 상호작용 선택하기 {#step-4-select-the-interaction-to-drive-recommendations}

이 추천이 최적화할 이벤트를 선택합니다. 이 이벤트는 일반적으로 구매이지만, 항목과의 모든 상호작용이 될 수도 있습니다.

{% alert tip %}
AI 항목 추천을 구성할 때 이벤트 선택이 중요합니다. 트리거 이벤트에 따라 AI 생성 추천을 받을 대상이 결정됩니다. AI 항목 추천은 구성한 이벤트를 완료한 사용자에게 생성되므로, 이 선택이 추천을 받는 대상을 직접 결정합니다. 도달하려는 전체 오디언스를 포괄하는 이벤트를 선택하세요.<br><br>동시에 도달 범위와 관련성 간의 균형을 맞추세요. 퍼널 상단 이벤트(예: Product Viewed)는 더 넓은 오디언스를 포착하는 경향이 있지만 비즈니스 성과와의 연관성이 낮을 수 있고, 퍼널 하단 이벤트(예: Purchased)는 더 타겟팅되고 비즈니스와 관련성 높은 추천을 생성하는 경향이 있습니다. 최적의 이벤트는 도달 범위와 비즈니스 성과에 대한 영향력의 균형을 맞추는 이벤트입니다.
{% endalert %}

최적화할 수 있는 항목:

- [구매 객체]({{site.baseurl}}/api/objects_filters/purchase_object)를 사용한 구매 이벤트
- 구매를 나타내는 커스텀 이벤트
- 기타 항목 상호작용을 나타내는 커스텀 이벤트(예: 제품 조회, 클릭 또는 미디어 재생)
- [주문 완료 이벤트]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events?tab=ecommerce.order_placed)를 사용한 주문 완료

**Custom Event**를 선택한 경우, 목록에서 이벤트를 선택합니다.

!["purchase" 커스텀 이벤트가 현재 이벤트 추적 방법으로 선택된 모습입니다.]({% image_buster /assets/img/item_recs_3.png %})

{% alert note %}
커스텀 이벤트는 이벤트 목록에 표시되기 전에 충분한 데이터가 있어야 합니다. 커스텀 이벤트가 표시되지 않는 경우, Braze 백엔드에서 아직 처리하지 않았거나 모델 교육을 위한 충분한 데이터가 없기 때문일 수 있습니다. AI 추천은 인사이트를 생성하기 위해 과거 데이터에 의존하므로, 새로 생성되었거나 드물게 트리거되는 이벤트는 더 많은 데이터가 수집될 때까지 사용할 수 없습니다.
{% endalert %}

### 5단계: 해당하는 속성정보 이름 선택하기 {#property-name}

추천을 만들려면, 상호작용 이벤트(주문 완료 이벤트, 구매 객체 또는 커스텀 이벤트)의 어떤 필드가 카탈로그에서 항목의 `id` 필드와 일치하는 고유 식별자를 포함하는지 Braze에 알려야 합니다. 잘 모르시겠다면 [요구 사항](#requirements)을 확인하세요.

**Property Name**에서 이 필드를 선택합니다.

**Property Name** 필드에는 SDK를 통해 Braze로 전송된 필드 목록이 미리 채워집니다. 충분한 데이터가 제공되면, 이러한 속성정보는 올바른 속성정보일 확률 순으로 정렬됩니다. 카탈로그의 `id` 필드에 해당하는 것을 선택합니다.

![카탈로그의 항목 ID에 해당하는 속성정보 이름 "purchase_item"이 선택된 모습입니다.]({% image_buster /assets/img/item_recs_4.png %})

#### 요구 사항 {#requirements}

속성정보를 선택할 때 몇 가지 요구 사항이 있습니다:

- 선택한 카탈로그의 `id` 필드에 매핑되어야 합니다.
- **주문 완료 이벤트를 선택했거나 [이커머스 이벤트]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events)를 사용하여 항목 추천을 교육하는 경우:** 제품 ID로 `products.product_id`를 입력합니다.
  - 필드는 제품 배열 안에 있거나 ID 배열로 끝날 수 있습니다. 어느 경우든 각 제품 ID는 동일한 타임스탬프를 가진 별도의 순차적 이벤트로 처리됩니다.
- **구매 객체를 선택한 경우:** `product_id` 또는 상호작용 이벤트의 `properties`에 있는 필드여야 합니다.
- **커스텀 이벤트를 선택한 경우:** 커스텀 이벤트의 `properties`에 있는 필드여야 합니다.
- 중첩된 필드는 `event_property.nested_property` 형식의 점 표기법으로 **Property Name** 드롭다운에 입력해야 합니다. 예를 들어, 이벤트 속성정보 `location` 내의 중첩된 속성정보 `district_name`을 선택하려면, `location.district_name`을 입력합니다. 커스텀 이벤트의 중첩된 속성정보에 대한 자세한 내용은 [중첩된 객체]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects)를 참조하세요.

#### 매핑 예시 {#example-mappings}

다음 매핑 예시는 모두 이 샘플 카탈로그를 참조합니다:

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table aria-label="매핑 예시" class="tg">
  <caption>매핑 예시</caption>
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
{% tab 커스텀 이벤트 %}

커스텀 이벤트 `added_to_cart`를 사용하여 고객이 결제하기 전에 유사한 제품을 추천하고 싶다고 가정해 보겠습니다. 이벤트 `added_to_cart`에는 이벤트 속성정보 `product_sku`가 있습니다.

이 경우 `product_sku` 속성정보에는 샘플 카탈로그의 `id` 열에 있는 값 중 하나 이상이 포함되어야 합니다: "ADI-BL-7", "ADI-RD-8", "ADI-WH-9" 또는 "ADI-PP-10". 모든 카탈로그 항목에 대한 이벤트가 필요한 것은 아니지만, 추천 엔진이 작동할 수 있는 충분한 콘텐츠를 갖추려면 일부는 필요합니다.

##### 커스텀 이벤트 객체 예시 {#example-custom-event-object}

이 이벤트에는 샘플 카탈로그의 첫 번째 항목과 일치하는 `"product_sku": "ADI-BL-7"`이 있습니다.

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

##### 제품 배열이 포함된 커스텀 이벤트 객체 예시 {#example-custom-event-object-with-an-array-of-products}

이벤트 속성정보에 배열로 여러 제품이 포함된 경우, 각 제품 ID는 별도의 순차적 이벤트로 처리됩니다. 이 이벤트는 `products.sku` 속성정보를 사용하여 샘플 카탈로그의 첫 번째 및 세 번째 항목과 일치시킬 수 있습니다.

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

##### 제품 ID 배열을 포함하는 중첩된 객체가 있는 커스텀 이벤트 객체 예시 {#example-custom-event-object-with-a-nested-object-containing-a-product-id-array}

제품 ID가 객체가 아닌 배열의 값인 경우에도 동일한 표기법을 사용할 수 있으며, 각 제품 ID는 별도의 순차적 이벤트로 처리됩니다. 이 방법은 다음 이벤트에서 중첩된 객체와 유연하게 결합할 수 있으며, 속성정보를 `purchase.product_skus`로 구성하여 샘플 카탈로그의 첫 번째 및 세 번째 항목과 일치시킬 수 있습니다.

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
{% tab 구매 객체 %}

구매 객체는 구매가 이루어졌을 때 API를 통해 전달됩니다.

매핑 측면에서, 구매 객체에도 커스텀 이벤트와 유사한 로직이 적용되지만, 구매 객체의 `product_id` 또는 `properties` 객체의 필드 중에서 선택할 수 있습니다.

모든 카탈로그 항목에 대한 이벤트가 필요한 것은 아니지만, 추천 엔진이 작동할 수 있는 충분한 콘텐츠를 갖추려면 일부는 필요합니다.

##### 제품 ID에 매핑된 구매 객체 예시 {#example-purchase-object-mapped-to-product-id}

이 이벤트에는 카탈로그의 첫 번째 항목에 매핑되는 `"product_id": "ADI-BL-7"`이 있습니다.

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

##### 속성정보 필드에 매핑된 구매 객체 예시 {#example-purchase-object-mapped-to-a-properties-field}

이 이벤트에는 카탈로그의 두 번째 항목에 매핑되는 `"sku": "ADI-RD-8"` 속성정보가 있습니다.

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
{% tab 주문 완료 이벤트 %}

##### 제품 ID에 매핑된 주문 완료 객체 예시 {#example-order-placed-object-mapped-to-product-id}

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

### 6단계: 추천 교육하기 {#step-6-train-the-recommendation}

준비가 되면 **Create Recommendation**을 선택합니다. 이 프로세스는 완료까지 10분에서 36시간까지 걸릴 수 있습니다. 추천이 성공적으로 교육되면 이메일 업데이트를 받거나, 생성이 실패한 이유에 대한 설명을 받게 됩니다.

**Predictions** 페이지에서 추천을 찾을 수 있으며, 필요에 따라 편집하거나 보관할 수 있습니다. 추천은 주별(유료) 또는 월별(무료)로 자동 재교육됩니다.