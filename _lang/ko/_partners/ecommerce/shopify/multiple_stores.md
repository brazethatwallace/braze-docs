---
nav_title: 여러 스토어 연결
article_title: Shopify 다중 스토어 지원
alias: /shopify_connecting_multiple_stores/
page_order: 6
description: "이 참조 문서에서는 여러 Shopify 스토어를 단일 워크스페이스에 연결하고 구성하는 방법을 다룹니다."
---

# 여러 Shopify 스토어 연결 {#connect-multiple-shopify-stores}

> 여러 Shopify 스토어 도메인을 단일 워크스페이스에 연결하여 모든 시장에 걸쳐 고객을 통합적으로 파악할 수 있습니다. 지역별 스토어에서 중복 작업 없이 단일 워크스페이스에서 자동화 프로그램과 여정을 구축하고 시작하세요.

{% alert important %}
이 기능은 Shopify Markets 또는 Markets Pro를 지원하지 않습니다. 이에 대한 지원을 요청하려면 [제품 요청]({{site.baseurl}}/user_guide/administer/personal/product_portal/)을 제출하세요.
{% endalert %}

## 요구 사항 {#requirements}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Shopify 스토어 설정 | 이미 [Braze와 Shopify 스토어를 하나 이상 설정]({{site.baseurl}}/shopify_overview/)했는지 확인하세요. |
| 각 지역별 고유한 Shopify 스토어프론트 도메인 | 다중 스토어 지원은 서로 다른 지역 스토어프론트에 대해 고유한 Shopify 스토어 도메인을 사용하기 위한 것입니다. <br><br>여러 하위 브랜드를 Braze에 연결하려면 각 하위 브랜드에 대해 별도의 워크스페이스를 생성하는 것을 권장합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requirements" }

## 추가 스토어 연결 {#connecting-an-additional-store}
Shopify 스토어에 Braze 앱을 설치하고 첫 번째 스토어를 설치한 후 **+ Connect New Store**를 선택합니다.

![Shopify 통합 페이지의 "+ Connect New Store" 버튼.]({% image_buster /assets/img/shopify/begin_setup_button.png %}){: style="max-width:80%;"}

추가 Shopify 지역 스토어의 경우 **Begin setup**을 선택합니다.

!["Begin setup" 버튼이 있는 "Integration settings" 섹션.]({% image_buster /assets/img/shopify/multiple_stores.png %}){: style="max-width:80%;"}

첫 번째 Shopify 스토어 통합과 마찬가지로 표준 또는 커스텀 설정 중에서 선택할 수 있습니다.

![표준 또는 커스텀 설정으로 Braze 웹 SDK를 구현할 수 있는 옵션이 있는 "Enable the Braze SDKs" 섹션.]({% image_buster /assets/img/shopify/standard_or_custom.png %}){: style="max-width:80%;"}

필요에 가장 적합한 옵션을 선택하세요:

{% multi_lang_include partners/shopify.md section='Integration Tabs' %}

각 스토어 통합을 확인하고 고급 설정을 구성하려면 드롭다운 메뉴에서 스토어를 선택합니다.

![Shopify 스토어를 선택할 수 있는 드롭다운 메뉴가 있는 "Integration settings".]({% image_buster /assets/img/shopify/store_dropdown_menu.png %})

## 스토어 간 사용자 동기화 {#syncing-users-across-stores}

### Shopify 별칭 {#shopify-alias}

여러 스토어를 연결하면 로그인하거나 주문한 동기화된 Shopify 사용자는 {% raw %}`shopify_customer_id_{{storename}}`{% endraw %} 형식의 새 별칭을 받게 됩니다.

### Braze 외부 ID {#braze-external-id}

Braze 외부 ID에 대해 다음 옵션 중에서 선택할 수 있습니다:

| 옵션 | 설명 |
|------|-----------|
| Shopify 고객 ID | Shopify의 고객 ID를 Braze 외부 ID로 사용하면 각 스토어에서 각 사용자에 대해 고유한 고객 ID를 생성합니다. 즉, 사용자가 여러 스토어와 상호작용하면 Braze에서 별도의 프로필을 갖게 됩니다. |
| 이메일, 해시된 이메일 또는 커스텀 외부 ID | 이메일, 해시된 이메일 또는 커스텀 외부 ID 유형을 사용하면 여러 스토어에 참여하는 사용자가 로그인하거나 주문할 때 프로필이 하나의 통합 프로필로 병합됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze external ID" }

### 병합되는 필드 {#merged-fields}

사용자 프로필이 동기화되면 다음 필드가 병합됩니다. 병합 동작에 대한 자세한 내용은 [병합 동작]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior)을 참조하세요.

- 기기 정보
- 총 세션 수(두 프로필에서 합산)
- 커스텀 이벤트 및 구매 데이터
- 세분화를 위한 커스텀 이벤트 속성정보(예: X ≤ 50이고 Y ≤ 30인 경우 "Y일 동안 X회")
- 이벤트 수(두 프로필에서 합산)
- 첫 번째 및 마지막 이벤트 날짜(Braze는 가장 빠른 날짜와 가장 최근 날짜를 선택)
- Campaign 상호작용 데이터(가장 최근 날짜 필드)
- 워크플로 요약(가장 최근 날짜 필드)
- 메시지 및 참여 기록
- 구독 그룹

### 가입자 수집(선택 사항) {#collecting-subscribers-optional}

Braze를 통해 직접(Shopify 커넥터 설정에서) 또는 Shopify에서 데이터를 동기화하는 API 및 SDK 대안을 통해 가입자를 수집할 수 있습니다.

{% tabs local %}
{% tab Shopify 커넥터 %}
Shopify 커넥터 설정의 **사용자 관리** 단계에서 Braze를 사용하여 이메일 및 SMS 가입자 옵트인을 수집하고 전용 구독 그룹으로 구성할 수 있습니다:

1. 연결하는 각 스토어에 대해 고유한 구독 그룹을 생성합니다. 이렇게 하면 가입자가 어디에서 오는지에 대한 정확한 데이터를 유지할 수 있습니다.
2. 이메일 및 SMS 가입자 수집을 활성화합니다.
{% endtab %}

{% tab Braze API 또는 SDK %}
또는 Braze API 또는 SDK를 사용하여 Shopify에서 직접 이메일 및 SMS 마케팅 옵트인 정보를 동기화할 수 있습니다.

| 옵션 | 리소스 |
|------|---------|
| API | - 통합에서 지원하는 것을 직접 대체하는 [구독 그룹 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/)<br>- 구독 그룹 데이터 또는 [글로벌 이메일 구독 상태]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states)를 설정하는 [`Users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#set-subscription-groups)<br>- 더 맞춤화된 마케팅 옵트인 수집 옵션을 위한 [Braze 환경설정 센터]({{site.baseurl}}/user_guide/channels/email/subscriptions/) |
| SDK | - [`NotificationSubscriptionTypes`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#notificationsubscriptiontypes)<br>- [`addToSubscriptionGroup`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)<br>- [`removeFromSubscriptionGroup`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#removefromsubscriptiongroup)<br>- [`setEmailNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Collecting subscribers (optional)" }
{% endtab %}
{% endtabs %}

## Shopify 데이터 {#shopify-data}

### 동기화되는 속성 {#synced-attributes}

두 개 이상의 스토어를 연결하면 다음 속성이 Shopify 프로필의 가장 최근 상태와 동기화됩니다:
- 이름
- 성
- 이메일
- 성별
- 생년월일
- 국가
- 도시
- 마지막 사용 앱
- 언어
- 시간대
- Shopify 태그
- Shopify 주문 수
- Shopify 총 지출액

### 지원되는 이벤트 {#supported-events}

#### eCommerce 권장 이벤트 {#ecommerce-recommended-events}

여러 스토어를 연결하면 수신되는 eCommerce 권장 이벤트에 소스 이벤트 속성정보가 포함됩니다. 이 속성정보는 이벤트가 발생한 스토어프론트 URL을 식별하여 세분화 또는 특정 사용 사례 트리거에 이 정보를 활용할 수 있게 합니다.

![`ecommerce.order_placed` 커스텀 이벤트를 수행하는 사용자가 진입하도록 트리거가 설정된 액션 기반 Canvas.]({% image_buster /assets/img/shopify/ecommerce_order_placed.png %}){: style="max-width:80%;"}

Shopify 통합 내에서 지원되는 eCommerce 권장 이벤트는 다음과 같습니다:

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_cancelled`
- `ecommerce.order_refunded`

#### Shopify 커스텀 이벤트 {#shopify-custom-events}

수신되는 Shopify 커스텀 이벤트에는 `shopify_storefront`라는 이벤트 속성정보가 포함됩니다. 이 속성정보는 이벤트가 발생한 스토어프론트 URL을 나타내며, 세분화 또는 사용 사례 트리거에 활용할 수 있습니다.

![`shopify_paid_order` 커스텀 이벤트를 수행하는 사용자가 진입하도록 트리거가 설정된 액션 기반 Canvas.]({% image_buster /assets/img/shopify/shopify_paid_order.png %}){: style="max-width:80%;"}

지원되는 Shopify 커스텀 이벤트는 다음과 같습니다:

- `shopify_fulfilled_order`
- `shopify_partially_fulfilled_order`
- `shopify_paid_order`
- `shopify_account_login`

모든 이벤트 페이로드에 대한 전체 개요는 [Shopify 데이터 기능]({{site.baseurl}}/shopify_data_features/)을 참조하세요.

### Shopify 제품 동기화 {#shopify-product-sync}

Braze에서 각 Shopify 스토어를 연결하고 구성할 때 통합의 일부로 Shopify 제품 동기화를 선택적으로 활성화할 수 있습니다.

각 스토어에 대해 제품 동기화를 활성화하면 Braze는 카탈로그 이름에 Shopify 스토어 이름을 포함합니다. 이렇게 하면 서로 다른 스토어의 제품을 구분할 수 있습니다.

![카탈로그 이름에 Shopify 스토어 이름이 포함된 Shopify 카탈로그.]({% image_buster /assets/img/shopify/catalog_store_name.png %})