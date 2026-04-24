---
nav_title: 추천 이벤트
article_title: 추천 이벤트
alias: /recommended_events/
page_order: 2
page_type: reference
description: "이 참조 문서에서는 Braze가 이커머스 이벤트에 대해 제공하는 추천 이벤트에 대해 설명합니다."
---

# 추천 이벤트

> 추천 이벤트는 가장 일반적인 이커머스 사용 사례에 매핑됩니다. 추천 이벤트를 사용하면 사전 구축된 캔버스 템플릿, 고객 생애주기에 매핑되는 리포팅 대시보드 등을 활용할 수 있습니다.

예를 들어, 사용자가 장바구니에 제품을 추가, 제거 또는 업데이트할 때 이를 캡처하기 위해 "cart_updated" 또는 "update_to_cart"라는 커스텀 이벤트를 사용하고 있을 수 있습니다. 추천 이벤트의 경우, Braze가 이 이벤트에 대해 정의된 이름과 관련 등록정보를 포함하는 이벤트 템플릿을 제공합니다.

{% alert important %}
추천 이벤트는 현재 얼리 액세스 단계입니다. 이 얼리 액세스에 참여하고 싶으시면 Braze 고객 성공 매니저에게 문의하세요. <br><br>새로운 [Shopify 커넥터]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector)를 활용하고 있다면, 이러한 추천 이벤트는 통합을 통해 자동으로 사용할 수 있습니다.
{% endalert %}

## 작동 방식

Braze는 모든 추천 이벤트에 특별한 유효성 검사를 적용하며, 일부 추천 이벤트에는 특별한 후처리 동작이 있습니다. 특정 산업 추천 이벤트의 경우, Braze는 캠페인 및 캔버스에 대한 새로운 액션 기반 트리거와 같은 특별한 처리를 지원할 수 있습니다.

추천 이벤트는 [커스텀 이벤트]({{site.baseurl}}/user_guide/data/activation/events/custom_events/)와 유사하게 작동합니다. 추천 이벤트를 커런츠에서 내보내기하고, 차단 목록에 추가하고, 리포팅에 사용할 수 있습니다. 또한 [Braze SDK]({{site.baseurl}}/developer_guide/getting_started/sdk_overview) 또는 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)를 사용하여 이러한 이벤트를 추적하기 위한 데이터를 Braze로 전송할 수 있습니다.

### 이커머스 추천 이벤트

[이커머스 추천 이벤트]({{site.baseurl}}/ecommerce_events/)는 추천 이벤트를 기반으로 합니다. 이러한 이커머스 추천 이벤트는 제품 조회, 장바구니 업데이트, 결제 프로세스 시작 등 고객이 수행하는 행동을 추적합니다.

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_refunded`
- `ecommerce.order_cancelled`

#### 이커머스 캔버스 템플릿

필수 전략을 구현하기 위해 Braze 캔버스 사전 구축 템플릿을 사용하는 방법에 대한 더 많은 아이디어는 전용 [이커머스 활용 사례]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases/)를 확인하세요.

## 자주 묻는 질문

### 추천 이벤트는 커스텀 이벤트와 동일한가요?

아닙니다. Braze는 추천 이벤트에 대해 명확한 데이터 스키마를 정의합니다. 여기에는 Braze에서 유효성 검사 프로세스를 거치는 필수 및 선택 사항 이벤트 등록정보가 포함됩니다. [커스텀 이벤트]({{site.baseurl}}/user_guide/data/activation/events/custom_events/)는 앱이나 웹사이트에서 사용자가 수행하거나 사용자에 대해 업데이트되는 특정 동작으로, 추적하고자 하는 것입니다. 이벤트 이름과 추적 대상을 커스터마이즈할 수 있습니다.

### 추천 이벤트의 이름을 커스터마이즈할 수 있나요?

아닙니다. 추천 이벤트에는 표준화된 이벤트 이름과 등록정보가 있습니다. 이러한 표준화는 데이터 전반에 걸쳐 일관성을 유지하는 데 도움이 됩니다.

### 구매를 기록하기 위해 구매 이벤트를 계속 사용할 수 있나요?

이커머스 추천 이벤트의 출시와 함께, Braze는 향후 레거시 구매 이벤트를 단계적으로 폐지할 예정입니다. 현재 구매 이벤트를 사용하고 있다면, 지원 중단 계획에 대한 사전 공지를 받게 됩니다. 그때까지는 공식 지원 중단일까지 구매 이벤트를 계속 사용할 수 있습니다.