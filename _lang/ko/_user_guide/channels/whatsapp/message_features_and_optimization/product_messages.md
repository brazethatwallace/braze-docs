---
nav_title: 제품 메시지
article_title: 제품 메시지
page_order: 4
description: "이 페이지에서는 WhatsApp 제품 메시지를 사용하여 Meta 카탈로그의 제품을 소개하는 인터랙티브 WhatsApp 메시지를 보내는 방법을 다룹니다."
page_type: reference
alias: "/whatsapp_product_messages/"
tool:
 - Campaigns
channel:
 - WhatsApp
---

# 제품 메시지 {#product-messages}

> 제품 메시지를 사용하면 Meta 카탈로그에서 직접 제품을 소개하는 인터랙티브 WhatsApp 메시지를 보낼 수 있습니다.

사용자에게 WhatsApp 제품 메시지를 보내면, 사용자는 다음과 같은 고객 여정을 거치게 됩니다:

1. 사용자가 WhatsApp에서 제품 또는 카탈로그 메시지를 수신합니다.
2. 사용자가 WhatsApp에서 직접 장바구니에 제품을 추가합니다.
3. 사용자가 WhatsApp에서 **Place order**를 탭합니다.
4. 웹사이트 또는 앱이 Braze로부터 장바구니 데이터를 수신하고 결제 링크를 생성합니다.
5. 사용자가 웹사이트 또는 앱으로 이동하여 결제를 완료합니다.

사용자가 카탈로그 메시지를 통해 장바구니에 항목을 추가하면, Braze는 후속 조치를 위한 웹훅 데이터를 수신합니다.

## 요구 사항 {#requirements}

| 요구 사항 | 설명 |
| --- | --- |
| WhatsApp 비즈니스 계정 | WhatsApp 제품 메시지를 사용하려면 Braze에 연결된 WhatsApp 비즈니스 계정이 있어야 합니다. |
| Meta 카탈로그 | Commerce Manager에서 Meta 카탈로그를 설정해야 합니다. |
| 약관 준수 | [Meta Commerce 약관 및 정책](https://www.facebook.com/policies_center/commerce)을 준수해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requirements" }

## 제품 메시지 유형 {#product-message-types}

{% alert note %}
[제품 메시지 설정](#setting-up-product-messages)의 4단계에서 접근할 수 있는 통합 제품 선택기를 사용하여 제품 메시지 경험을 향상시킬 수 있습니다.
{% endalert %}

{% tabs local %}
{% tab 카탈로그 메시지 %}

카탈로그 메시지는 전체 제품 카탈로그를 인터랙티브 형식으로 표시합니다. [템플릿 및 응답 메시지](#building-a-product-message)로 사용할 수 있습니다.

[설정](#setting-up-product-messages) 중에 Braze에 카탈로그 권한을 활성화한 경우, 사용자에게 표시되는 썸네일을 선택할 수 있습니다.

{% alert note %}
카탈로그 연결은 Meta에서 관리되므로 제품 카탈로그에 자동으로 상속되기 때문에, Braze에서 추가적인 제품 선택을 할 필요가 없습니다.
{% endalert %}


{% endtab %}
{% tab 다중 제품 메시지 %}

다중 제품 메시지는 카탈로그에서 특정 제품을 강조 표시하며, 메시지당 최대 30개의 항목을 강조할 수 있습니다. [템플릿 및 응답 메시지](#building-a-product-message)로 사용할 수 있습니다.

ID를 사용하여 수동으로 제품을 선택하거나, [설정](#setting-up-product-messages) 중에 카탈로그 권한을 활성화한 경우 드롭다운 제품 선택기를 사용할 수 있습니다.

{% alert important %}
Meta에서 다중 제품 메시지 템플릿의 헤더 표시 문제가 알려져 있습니다. Meta는 이 문제를 인지하고 있으며 수정 작업을 진행 중입니다.
{% endalert %}

{% endtab %}
{% tab 단일 제품 %}

단일 제품 메시지는 제품 카탈로그에서 하나의 특정 제품을 강조 표시합니다. [응답 메시지](#building-a-product-message)로 사용할 수 있습니다.

ID를 사용하여 수동으로 제품을 선택하거나, [설정](#setting-up-product-messages) 중에 카탈로그 권한을 활성화한 경우 드롭다운 제품 선택기를 사용할 수 있습니다.

{% endtab %}
{% endtabs %}

## 제품 메시지 설정 {#setting-up-product-messages}

1. [Meta Commerce Manager](https://business.facebook.com/business/loginpage/?next=https%3A%2F%2Fbusiness.facebook.com%2Fcommerce_manager%2F#)에서 [Meta의 안내](https://www.facebook.com/business/help/1275400645914358?id=725943027795860&ref=search_new_1)를 따라 Meta 카탈로그를 생성합니다. Braze에 연결된 WhatsApp 비즈니스 계정이 있는 동일한 Meta 비즈니스 포트폴리오에 있는지 확인하세요.
2. Meta의 안내를 따라 Meta Business Manager에서 "Manage Catalog" 권한을 할당하여 [Meta 카탈로그를 연결](https://www.facebook.com/business/help/1953352334878186?id=2042840805783715)합니다.

![Meta "Catalogs" 페이지에서 "sweeney_catalog"이라는 카탈로그의 "Assign partner" 버튼을 가리키는 화살표가 있는 화면.]({% image_buster /assets/img/whatsapp/meta_catalog.png %}){: style="max-width:90%;"}

파트너 비즈니스 ID로 Braze Business Manager ID `332231937299182`를 사용하세요.

![파트너 비즈니스 ID를 입력하고 "Manage catalog" 권한을 할당하는 필드가 포함된 파트너와 카탈로그를 공유하는 창.]({% image_buster /assets/img/whatsapp/share_meta_catalog.png %}){: style="max-width:70%;"}

{: start="3"}
3. Meta 카탈로그 설정을 선택합니다. 카탈로그 메시지를 보내려면 **Show catalog icon in chat header**를 선택해야 합니다.

!["Catalog_products" 카탈로그에 대한 WhatsApp Manager 설정 페이지.]({% image_buster /assets/img/whatsapp/meta_catalog_settings.png %}){: style="max-width:90%;"}

{: start="4"}
4. Braze에서 [임베디드 가입]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup/) 프로세스를 진행하여 권한을 제공합니다. 권한을 제공할 카탈로그를 **모두** 선택해야 합니다. 이렇게 하면 Braze 통합 제품 선택기가 활성화됩니다.

![권한을 제공하기 위해 5개의 카탈로그가 선택된 창.]({% image_buster /assets/img/whatsapp/select_catalogs.png %}){: style="max-width:50%;"}

{% alert tip %}
Meta 카탈로그를 만들 때 따라야 할 모범 사례는 [Commerce Manager에서 고품질 카탈로그 구축을 위한 팁](https://www.facebook.com/business/help/2086567618225367?id=725943027795860)을 참조하세요.
{% endalert %}

## 제품 메시지 작성 {#building-a-product-message}

WhatsApp 템플릿 메시지 또는 응답 메시지를 사용하여 제품 메시지를 작성할 수 있습니다.

{% tabs local %}
{% tab WhatsApp 메시지 템플릿 %}

1. Meta Business Manager에서 **Message Templates**로 이동합니다.
2. 형식으로 **Catalog**를 선택한 다음, **Catalog message**(전체 카탈로그 표시)와 **Multi-product catalog message**(특정 항목 강조) 중에서 선택합니다.
3. Braze에서 WhatsApp Campaign 또는 Canvas 메시지 단계를 생성합니다.
4. 템플릿을 제출한 구독 그룹과 일치하는 구독 그룹을 선택합니다.
5. **WhatsApp Template Message**를 선택합니다.
6. 사용할 템플릿을 선택합니다.
    - 다중 제품 템플릿을 선택한 경우, 강조할 제품의 섹션 제목과 콘텐츠 ID를 제공합니다. Meta Commerce Manager에서 직접 콘텐츠 ID를 복사하거나, 통합 제품 선택기에 대한 권한을 활성화한 경우 항목을 선택할 수 있습니다.

![섹션 제목과 콘텐츠 ID를 입력하는 필드가 있는 항목 목록.]({% image_buster /assets/img/whatsapp/multi_product_template.png %}){: style="max-width:60%;"}

![선택할 수 있는 항목의 드롭다운이 있는 항목 목록.]({% image_buster /assets/img/whatsapp/content_id_items.png %}){: style="max-width:60%;"}

{: start="7"}
7. 메시지 작성을 계속합니다.

{% endtab %}
{% tab 응답 메시지 %}

1. Braze에서 WhatsApp Campaign 또는 Canvas 메시지 단계를 생성합니다.
2. 구독 그룹을 선택합니다.
3. **Response Message**를 선택합니다.
4. **Meta Product Messages**를 선택합니다.

![메시지 유형과 응답 메시지 레이아웃을 선택하는 옵션으로, "Response Message"와 "Meta Product Messages"가 강조 표시된 화면.]({% image_buster /assets/img/whatsapp/response_message_layouts.png %}){: style="max-width:90%;"}

{: start="5"}
5. 사용할 [메시지 유형](#product-message-types)을 선택합니다.

!["Multi-product"의 메시지 레이아웃 선택.]({% image_buster /assets/img/whatsapp/multi-product_message_layout.png %}){: style="max-width:90%;"}

{: start="6"}
6. 메시지 작성을 계속합니다.

![제품 정보가 입력된 Meta 제품 메시지 예시.]({% image_buster /assets/img/whatsapp/example_response_message.png %}){: style="max-width:90%;"}

{% endtab %}
{% endtabs %}

## 제품 관리 {#managing-products}

### Commerce Manager 접근 {#accessing-commerce-manager}

Meta Business Manager에서 **Commerce Manager**로 이동하여 조직을 선택합니다. 여기에서 다음과 같은 카탈로그 자산을 관리할 수 있습니다:
- 새 카탈로그 생성
- 기존 카탈로그에 제품 추가
- 제품 정보 업데이트
- 단종된 항목 제거

{% alert important %}
카탈로그에서 참조된 제품을 제거하면 관련 메시지가 전송에 실패합니다.
{% endalert %}

## 인바운드 제품 질문 수신 {#receiving-inbound-product-questions}

사용자는 제품 또는 카탈로그 메시지에 제품 질문으로 응답할 수 있습니다. 이러한 질문은 인바운드 메시지로 도착하며, [행동 경로]({{site.baseurl}}/action_paths/)를 사용하여 분류할 수 있습니다.

또한 Braze는 이러한 질문에서 제품 ID와 카탈로그 ID를 추출하므로, 응답을 자동화하거나 다른 팀(예: 고객지원)에 질문을 전달하려는 경우 해당 세부 정보를 포함할 수 있습니다. 예를 들어, `inbound_product_id` 또는 `inbound_catalog_id`의 WhatsApp 등록정보를 사용하여 응답을 개인화할 수 있습니다.

![개인화 유형이 "WhatsApp Properties"이고 "inbound_product_id" 속성이 강조 표시된 "Add Personalization" 창.]({% image_buster /assets/img/whatsapp/inbound_product_questions.png %}){: style="max-width:60%;"}

## 결제: 장바구니 처리 및 웹훅 {#checkout-cart-processing-and-webhooks}

사용자가 WhatsApp 제품 메시지와 상호작용할 때 제품을 탐색하고 장바구니에 항목을 추가할 수 있습니다. 그러나 현재 배송 정보나 결제 처리를 위한 내장 결제 기능은 없습니다. 대신, 자체 앱이나 웹사이트에서 장바구니를 생성하고 커스텀 링크를 사용하여 사용자를 해당 장바구니로 안내하는 것을 권장합니다.

### 고려 사항 {#considerations}

- **인앱 결제 없음:** 사용자는 WhatsApp 내에서 직접 구매를 완료할 수 없습니다. 모든 거래는 웹사이트 또는 앱으로 리디렉션되어야 합니다.
- **커스텀 링크 필요:** 사용자를 플랫폼의 장바구니로 안내하는 커스텀 링크를 생성해야 합니다.
- **수동 설정:** 설정 프로세스에는 장바구니 및 메시징 워크플로의 수동 구성이 필요합니다.

{% alert note %}
현재 WhatsApp에서 직접 결제를 지원하지 않으며, 향후 지원은 국가별로 제공될 예정입니다(현재 Meta는 인도, 브라질, 싱가포르에 기반을 두고 해당 국가의 사용자와 직접 거래하는 기업에만 제공합니다).
{% endalert %}

### 장바구니 이벤트 트리거 설정 {#setting-up-cart-event-triggers}

고객이 WhatsApp에서 주문하면 Braze가 자동으로 다음을 수행합니다:
1. WhatsApp에서 장바구니 내용(제품 ID, 수량 및 기타 주문 데이터)을 수신합니다.
2. `source = whats_app`을 포함한 모든 관련 데이터가 포함된 `ecommerce.cart_update` eCommerce 이벤트를 생성합니다.
3. 응답을 트리거하여 주문에 대한 자동화된 Campaign을 설정할 수 있습니다.

`ecommerce.cart_update` eCommerce 이벤트는 이벤트가 전송된 후에만 Braze에 목록으로 표시되며, Braze에서 테스트 제품 메시지를 생성하고 장바구니 이벤트를 제출하여 수행할 수 있습니다.
장바구니 이벤트에는 다음이 포함됩니다:

- **Cart ID:** 장바구니의 고유 식별자
- **Products:** 제품 ID, 수량 및 가격이 포함된 항목 목록
- **Total Value:** 모든 항목의 합계
- **Currency:** 장바구니의 통화
- **Source:** "whats_app"으로 표시
- **Metadata:** 카탈로그 ID 및 메시지 텍스트와 같은 추가 데이터

추가적인 Braze 장바구니 이벤트 정보는 [eCommerce 권장 이벤트 유형]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events/#types-of-ecommerce-recommended-events)에서 확인할 수 있습니다.

### 트리거 응답 설정 {#setting-up-a-triggered-response}

1. `ecommerce.cart_updated`에 대한 커스텀 이벤트 트리거를 생성합니다.
2. `source = "whats_app"`에 대한 등록정보 필터를 추가합니다.

![기본 등록정보 "source"가 `whats_app`과 같은 `ecommerce.cart_updated` 커스텀 이벤트 트리거가 있는 Canvas 단계.]({% image_buster /assets/img/whatsapp/product_message_canvas_step.png %})

{: start="3"}
3. 장바구니 데이터를 기반으로 후속 동작을 구성합니다.

### 권장 결제 구현 {#recommended-checkout-implementations}

{% tabs local %}
{% tab 간단한 Liquid 기반 장바구니 링크 %}

Liquid를 사용하여 응답 메시지에서 직접 장바구니 URL을 작성합니다. WhatsApp과 eCommerce 플랫폼 간에 일관된 제품 ID가 있는 경우에 가장 적합합니다.

#### Liquid 예시 {#example-liquid}

{% raw %}
```liquid
{% assign cart_link = "http://alejandro-test-new.myshopify.com/cart/" %}
{% for product in event_properties.products %}
 {% assign variant_id = product.product_id %}
 {% assign quantity = product.quantity %}
 {% if forloop.first %}
   {% assign cart_link = cart_link | append: variant_id | append: ":" | append: quantity %}
 {% else %}
   {% assign cart_link = cart_link | append: "," | append: variant_id | append: ":" | append: quantity %}
 {% endif %}
{% endfor %}
{{ cart_link }}
```
{% endraw %}

#### 설정 {#setup}

1. `ecommerce.cart_update` eCommerce 이벤트를 트리거로 하는 WhatsApp 응답 메시지 Campaign을 생성합니다.
2. 장바구니 URL이 포함된 후속 메시지를 생성합니다.
3. Liquid로 장바구니 URL을 작성합니다. Shopify를 사용하는 경우, 위의 Liquid 예시를 사용하여 [장바구니 퍼머링크를 생성](https://shopify.dev/docs/apps/build/checkout/create-cart-permalinks)할 수 있습니다.

![Liquid로 생성된 장바구니의 결제 경험 워크플로를 보여주는 다이어그램: Meta가 Braze에 주문 수신 메시지를 보내면, 액션 기반 트리거가 실행되어 장바구니 링크가 포함된 메시지를 생성하고, WhatsApp 메시지를 전송합니다.]({% image_buster /assets/img/whatsapp/liquid_generated_cart_link_checkout.png %})

{% endtab %}
{% tab 연결된 콘텐츠 %}

eCommerce 시스템에 API 호출을 하여 개인화된 결제 URL을 생성합니다. 동적 장바구니 URL 생성이나 복잡한 제품 매핑이 필요한 경우에 가장 적합합니다.

#### 설정

1. [`ecommerce.cart_update`]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events?tab=ecommerce.cart_updated) eCommerce 이벤트에 의해 트리거되는 웹훅 Campaign 또는 Canvas 단계를 생성하여 장바구니 데이터를 eCommerce 시스템에 전송합니다.
2. 동일한 eCommerce 이벤트에 의해 트리거되는 WhatsApp Campaign 또는 Canvas 메시지 단계를 생성하여 사용자에게 장바구니 URL이 포함된 WhatsApp 응답 메시지를 보냅니다. 후속 응답 메시지의 안내에 따라 [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)를 사용합니다.

![연결된 콘텐츠 호출의 결제 경험 워크플로를 보여주는 다이어그램: Meta가 Braze에 주문 수신 메시지를 보내면, Braze가 eCommerce 플랫폼과 양방향 호출을 수행한 후 WhatsApp 메시지를 전송합니다.]({% image_buster /assets/img/whatsapp/connected_content_checkout.png %})

{% endtab %}
{% tab 웹훅 및 커스텀 이벤트 %}

웹훅을 사용하여 장바구니 데이터를 시스템에 전송한 다음, 커스텀 이벤트를 통해 후속 메시지를 트리거합니다. 광범위한 장바구니 처리나 다단계 워크플로가 필요한 복잡한 통합에 가장 적합합니다.

#### 설정

`ecommerce.cart_update` eCommerce 이벤트에 의해 트리거되는 웹훅 Campaign 또는 Canvas 단계를 생성하여 장바구니 데이터를 eCommerce 시스템에 전송합니다. 그러면 API가 다음을 수행합니다:
1. 장바구니 데이터 수신
2. 시스템에서 장바구니 생성
3. 결제 URL 생성
4. Braze에 `checkout_started` 이벤트를 전송하여 결제 링크가 포함된 WhatsApp 메시지 전송을 트리거

![웹훅 및 커스텀 이벤트의 결제 경험 워크플로를 보여주는 다이어그램: Meta가 Braze에 주문 수신 메시지를 보내면, Braze가 eCommerce 플랫폼과 양방향 호출을 수행한 후 장바구니 URL이 포함된 WhatsApp 메시지를 전송합니다.]({% image_buster /assets/img/whatsapp/webhooks_custom_events_checkout.png %})

{% endtab %}
{% endtabs %}

## 테스트 및 검증 {#testing-and-validation}

### 테스트 메시지 요구 사항 {#test-message-requirements}

장바구니 기능은 테스트 메시지 간에 유지되지만, 인바운드 결과의 처리는 유지되지 않습니다.

### 메시지 미리보기 {#message-preview}

- 제품 이미지와 세부 정보는 Meta 카탈로그에서 가져옵니다.
- 인터랙티브 미리보기는 통합이 완료될 때까지 플레이스홀더를 표시합니다.

### 오류 코드 {#error-codes}

- 제품 ID가 카탈로그에 존재하지 않는 경우, `product not found for product_retailer_id, fake-product-id, in catalog_id, 1903196950214359` 오류가 발생합니다.
- 카탈로그가 WABA에서 연결 해제된 경우, `Check if catalog is linked to the WhatsApp Business Account and the catalog is enabled in the WhatsApp Commerce Settings` 오류가 발생합니다.