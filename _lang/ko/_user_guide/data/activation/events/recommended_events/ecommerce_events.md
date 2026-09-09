---
nav_title: eCommerce 추천 이벤트 사용하기
article_title: eCommerce 이벤트 사용 방법
page_type: reference
alias: /ecommerce_events/
description: "Braze에서 eCommerce 추천 이벤트를 사용하는 방법을 알아보세요. 지원되는 기능, 주요 측정기준, 세분화, 메시징에 대한 모범 사례를 포함합니다."
---

# eCommerce 이벤트 사용 방법 {#how-to-use-ecommerce-events}

> eCommerce [추천 이벤트]({{site.baseurl}}/recommended_events)는 공유된 주문 수준 스키마를 사용하므로, Braze가 eCommerce 데이터를 기반으로 고객 프로필, 세분화, 메시징, 보고, AI 기반 추천 등 신뢰할 수 있는 기능을 구축할 수 있습니다. 이 문서의 각 섹션에서는 Braze에서 각 기능을 사용하는 방법을 다룹니다.<br><br> 속성정보 요구 사항과 데이터 유형은 [이벤트 스키마]({{site.baseurl}}/user_guide/data/activation/events/recommended_events#event-schemas)를, 이벤트 유효성 검사에 실패했을 때 발생하는 상황은 [이벤트 유효성 검사 및 문제 해결]({{site.baseurl}}/user_guide/data/activation/events/recommended_events#event-validation-and-troubleshooting)을 참조하세요.

eCommerce 이벤트는 예측 가능한 스키마를 따르기 때문에, Braze는 매출 추적과 사전 구축된 Canvas 템플릿부터 AI 기반 추천까지 신뢰할 수 있는 기능을 구축할 수 있습니다. 다음 섹션에서는 각 기능에 대한 간략한 개요와 전체 설명서 링크를 제공합니다.

{% alert note %}
Braze eCommerce 이벤트와 세분화 가능한 이벤트 속성정보는 [데이터 포인트]({{site.baseurl}}/user_guide/data/infrastructure/data_points)에 포함되지 않습니다.
{% endalert %}

<a id="transactions-tab" aria-hidden="true"></a>

## Commerce 탭 {#commerce-tab}

각 고객 프로필의 **Commerce** 탭은 **주문 활동**(계산된 매출 및 주문 측정기준)과 **활성 장바구니**(`ecommerce.cart_updated` 이벤트의 최신 장바구니)라는 두 가지 모듈을 결합합니다.

### 주문 활동 {#order-activity}

**주문 활동** 모듈은 이벤트가 처리될 때 실시간으로 업데이트되는 세 가지 계산 측정기준을 표시합니다. 이러한 계산의 주문 수준 모델은 제품 가격과 총 주문 금액을 깔끔하게 분리합니다.

{% alert note %}
eCommerce 추천 이벤트는 **Commerce** 탭의 **구매 내역** 섹션에 표시되지 않습니다. 구매 내역은 레거시 구매 이벤트로 채워집니다. 추천 이벤트의 매출 및 주문 활동에는 다음 표의 측정기준을 사용하세요.
{% endalert %}

| 측정기준 | 공식 |
| ----- | ----- |
| 총 매출 | sum (`order_placed.total_value`) − sum (`order_refunded.total_value`) |
| 총 주문 수 | count (distinct `order_placed`) − count (distinct `order_cancelled`) |
| 총 환불 금액 | sum (`order_refunded.total_value`) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="주문 활동 측정기준" }

### 활성 장바구니 {#active-cart}

**활성 장바구니** 모듈은 고객 프로필의 최신 장바구니를 표시합니다. 이 뷰는 테스트 중에 특히 유용합니다. 장바구니 내용을 확인하거나, 장바구니 기반 여정을 검증하거나, `ecommerce.cart_updated` 이벤트가 프로필을 예상대로 업데이트하고 있는지 확인하는 데 사용할 수 있습니다.

**활성 장바구니**에는 다음이 포함됩니다:

- **장바구니 ID** — 마지막으로 `ecommerce.cart_updated` 이벤트를 수신한 장바구니의 식별자입니다.
- **마지막 업데이트** — 가장 최근 장바구니 업데이트의 타임스탬프입니다.
- **총 장바구니 금액** — 현재 장바구니에 있는 라인 항목의 총 금액입니다.
- **제품 보기** — 장바구니에 있는 제품 목록을 여는 링크입니다(최대 50개 제품).

## 이커머스 오케스트레이션 {#ecommerce-orchestration}

### 세분화 {#segmentation}

Braze는 이커머스 데이터를 기반으로 사용자를 세분화하는 세 가지 방법을 제공합니다:

- **이커머스 필터:** 세그먼터의 **이커머스** 카테고리를 사용합니다. 이 카테고리에는 이커머스 권장 이벤트로 구동되는 필터(**마지막 주문 완료**, **총 매출**, **평균 주문 금액** 등)가 포함되어 있습니다. 사용 가능한 필터의 전체 목록은 [Segment 필터]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)를 참조하세요.
- **커스텀 이벤트 필터:** 이커머스 이벤트는 커스텀 이벤트처럼 동작하므로 기존의 모든 커스텀 이벤트 필터를 바로 사용할 수 있습니다. 예를 들어, "커스텀 이벤트 `ecommerce.order_placed`를 X회 이상 수행한 사용자" 또는 "커스텀 이벤트 `ecommerce.order_placed`를 처음 수행한 사용자"로 필터링할 수 있습니다.
- **세그먼트 확장:** 중첩된 제품 배열이나 메타데이터 객체 속성정보를 포함한 중첩된 이벤트 속성정보를 기반으로 세분화하려면 중첩된 이벤트 속성정보 필터링과 함께 [세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension)을 사용하세요. 이를 통해 "지난 90일 이내에 제품 SKU-123을 구매한 사용자"와 같은 오디언스를 구성하거나, 동일한 주문의 여러 속성정보에 걸쳐 기준을 조합할 수 있습니다.

문서화된 이벤트 스키마에 포함되지 않은 커스텀 속성정보를 필터링해야 하는 경우, 이벤트를 기록할 때 해당 속성정보를 `metadata` 아래에 중첩하세요(예: `color` 대신 `metadata.color`). API 또는 SDK를 통해 전송한 커스텀 최상위 속성정보는 확장 속성정보 필터에 유효하지 않습니다. 해당 속성정보가 이벤트 데이터에 나타나더라도 마찬가지입니다. 허용 목록에 없는 최상위 속성정보를 사용하면 확장을 저장하거나 보관 해제할 수 없게 됩니다.

{% alert important %}
이커머스 권장 이벤트에 대한 세그먼트 확장은 유료 기능이며 얼리 액세스 중입니다. 얼리 액세스에 참여하려면 고객 성공 매니저에게 문의하세요. 팀에 중첩된 속성정보 세분화를 추천하기 전에 플랜에 액세스가 포함되어 있는지 확인하세요.
{% endalert %}

### 트리거 {#triggering}

Braze 전체에서 다른 커스텀 이벤트와 마찬가지로 이커머스 이벤트에 대해 커스텀 이벤트 수행 트리거를 사용할 수 있습니다. 유기한 장바구니 플로우의 경우, **장바구니 업데이트 이벤트 수행** 트리거를 사용하여 장바구니 업데이트를 올바르게 캡처하세요.

또한 Braze는 전용 **주문 완료** 트리거를 제공합니다. 이를 통해 모든 주문 또는 특정 제품이 포함된 주문을 기반으로 여정을 시작하거나 액션을 수행할 수 있습니다. 이 트리거는 제품 이름, `product_id` 또는 `variant_id`로 필터링하여 특정 구매 시나리오를 타겟팅할 수 있습니다. 자세한 내용은 [실행 기반 전달]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery)을 참조하세요.

![모든 주문을 완료하는 옵션이 선택된 주문 완료 트리거.]({% image_buster /assets/img/recommended_events/places_order_trigger.png %})

### Liquid 개인화 {#liquid-personalization}

이커머스 이벤트는 커스텀 이벤트와 동일한 방식으로 [Liquid 개인화]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid)를 지원합니다. 메시징에서 이벤트 속성정보를 직접 참조할 수 있습니다. 제품 이미지, 가격 또는 기타 카탈로그 데이터를 메시지에 가져오려면 `product_id` 또는 `variant_id`를 연결 식별자로 사용하여 카탈로그와 이벤트를 결합하세요. {% raw %}`{% shopping_cart %}`{% endraw %} Liquid 태그를 사용하면 유기한 장바구니 리마인더, 결제 안내 또는 주문 확인을 위해 사용자의 현재 장바구니 내용을 반복 출력할 수 있습니다. 바로 사용할 수 있는 코드 샘플은 [이커머스 사용 사례]({{site.baseurl}}/ecommerce_use_cases)를 참조하세요.

코드 없는 대안으로 [드래그 앤 드롭 제품 블록]({{site.baseurl}}/user_guide/messaging/design_and_edit/product_blocks)이 얼리 액세스 프로그램에서 제공됩니다.

### 이커머스 Canvas 템플릿 {#ecommerce-canvas-templates}

Braze는 이커머스 권장 이벤트를 진입, 종료 및 전환 기준으로 사전 구성한 바로 사용 가능한 Canvas 템플릿을 제공하므로, 커스텀 설정 없이 라이프사이클 플로우를 시작할 수 있습니다. 각 템플릿에는 드래그 앤 드롭 이메일 디자인이 포함되어 있으며 드래그 앤 드롭 제품 블록(현재 얼리 액세스)을 지원합니다. 자세한 사용 사례 및 Liquid 예시는 [이커머스 사용 사례]({{site.baseurl}}/ecommerce_use_cases)를 참조하세요.

이 템플릿은 가장 일반적인 이커머스 라이프사이클 플로우를 다룹니다. 출발점으로 사용한 후 타이밍, 채널 및 크리에이티브를 오디언스에 맞게 커스터마이징하세요.

{% tabs %}
{% tab 유기한 탐색 %}

제품을 조회했지만 장바구니에 추가하지 않은 사용자를 다시 참여시킵니다.

최근 조회했지만 행동으로 이어지지 않은 제품을 다시 고려하도록 브라우저를 유도하려면 이 템플릿을 사용하세요.

| 설정 | 값 |
| --- | --- |
| 진입 이벤트 | `ecommerce.product_viewed` |
| 종료 이벤트 | `ecommerce.product_viewed`, `ecommerce.cart_updated`, `ecommerce.checkout_started`, 주문 완료 |
| 전환 이벤트 | 주문 완료 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="이커머스 Canvas 템플릿" }

{% endtab %}
{% tab 유기한 장바구니 %}

장바구니에 상품을 추가했지만 결제를 시작하지 않은 사용자를 복구합니다.

장바구니에 있는 상품을 사용자에게 상기시키고 결제를 완료하도록 유도하려면 이 템플릿을 사용하세요.

| 설정 | 값 |
| --- | --- |
| 진입 이벤트 | `ecommerce.cart_updated` |
| 종료 이벤트 | `ecommerce.cart_updated`, `ecommerce.checkout_started`, 주문 완료 |
| 전환 이벤트 | 주문 완료 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="이커머스 Canvas 템플릿" }

{% alert tip %}
`ecommerce.cart_updated` 이벤트는 전체 장바구니 교체(각 이벤트가 전체 장바구니를 설명) 또는 선택적 `action` 속성정보의 `add` 및 `remove` 값을 사용한 증분 업데이트를 지원합니다. 장바구니당 하나의 접근 방식을 선택하고 동일한 `cart_id`에 대해 교체와 증분 장바구니 업데이트를 혼합하지 마세요. 저장된 장바구니는 가장 최근 장바구니 이벤트의 `currency`를 유지합니다. 다른 통화로 장바구니를 업데이트하면 두 통화의 값을 혼합하는 대신 저장된 장바구니가 교체됩니다. 전송 시점에 현재 장바구니 내용을 동적으로 표시하려면 메시지에서 {% raw %}`{% shopping_cart %}`{% endraw %} Liquid 태그를 사용하세요.
{% endalert %}

{% endtab %}
{% tab 유기한 결제 %}

결제를 시작했지만 구매를 완료하지 않은 사용자를 복구합니다.

퍼널에서 가장 높은 의도 단계의 구매를 복구하려면 이 템플릿을 사용하세요.

| 설정 | 값 |
| --- | --- |
| 진입 이벤트 | `ecommerce.checkout_started` |
| 종료 이벤트 | 주문 완료 |
| 전환 이벤트 | 주문 완료 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="이커머스 Canvas 템플릿" }

{% endtab %}
{% tab 주문 확인 및 설문조사 %}

성공적인 구매를 확인하고 피드백 설문조사를 후속 발송하여 리뷰 수집 및 구매 후 인게이지먼트를 촉진합니다.

구매 후 커뮤니케이션을 간소화하고 단일 워크플로우에서 고객 피드백을 수집하려면 이 템플릿을 사용하세요.

| 설정 | 값 |
| --- | --- |
| 진입 이벤트 | `ecommerce.order_placed` |
| 전환 이벤트 | 세션 시작 또는 `ecommerce.product_viewed` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="이커머스 Canvas 템플릿" }

{% endtab %}
{% endtabs %}

#### 템플릿 커스터마이징 {#customize-templates}

이 템플릿은 출발점으로 설계되었습니다. 일반적인 커스터마이징 항목은 다음과 같습니다:
  - **이메일 커스터마이징:** 각 템플릿에는 드래그 앤 드롭 에디터로 구성된 사전 설정 이메일이 포함되어 있으며, 브랜드와 콘텐츠에 맞게 완전히 편집할 수 있습니다.
  - **채널 추가:** 크로스채널 강화를 위해 이메일에 푸시, SMS 또는 인앱 메시지를 결합하세요.
  - **지연 및 결정 분할 추가:** 행동별로 사용자를 분기하거나(예: 고가치 장바구니 대 저가치 장바구니) 메시지 간 대기 기간을 설정하세요.
  - **크리에이티브 교체:** 포함된 이메일 템플릿을 브랜드의 비주얼 스타일로 교체하세요.
  - **제품 블록 사용:** 드래그 앤 드롭 제품 블록(얼리 액세스 프로그램)을 사용하여 커스텀 Liquid를 작성하지 않고도 유기한 장바구니 내용이나 탐색한 제품을 동적으로 렌더링하세요.

Liquid 개인화 예시를 포함한 고급 라이프사이클 전략은 [이커머스 사용 사례]({{site.baseurl}}/ecommerce_use_cases)를 참조하세요.

## 이커머스 보고 {#ecommerce-reporting}

이커머스 권장 이벤트는 고객이 이미 사용 중인 동일한 매출 보고 화면을 지원합니다. 통합에서 이커머스 이벤트를 전송하면 다음 보고서에 이커머스 매출이 자동으로 포함됩니다.

| 보고서                                      | 표시 내용                             |
|---------------------------------------------|-------------------------------------------|
| 매출 보고서                              | 선택한 기간 및 앱에 대해 모든 소스의 총 매출, 일평균 매출, 일별 구매, 사용자당 매출을 시간 경과에 따라 표시합니다.                                                                                     |
| 라스트 터치 기여도 매출 대시보드     | 사용자가 주문하기 전에 마지막으로 상호작용한 Campaign 또는 Canvas에 기여된 매출입니다. 터치 이벤트에는 이메일 클릭, 푸시 열람, 콘텐츠 카드 클릭, 인앱 메시지 클릭, SMS 또는 WhatsApp 짧은 링크 클릭이 포함됩니다. |
| Campaign 및 Canvas 분석                | 주요 전환 기간 내 특정 Campaign 또는 Canvas에 기여된 총 매출입니다.                                                                                   |
| 전환 보고서                          | Campaigns 및 Canvases의 전환 이벤트에 연결된 매출입니다.<br> **참고:** `ecommerce.order_placed` 매출을 집계하려면 Campaign 또는 Canvas에서 "Place Order" 전환 이벤트 유형을 전환 이벤트로 사용해야 합니다.                                                                                    |
| 세그먼트 인사이트                            | 세그먼트 인사이트 대시보드에서 Segments 간 매출 비교를 표시합니다.                                                               |
| 보고서 빌더                              | 보고서 빌더에서 작성한 커스텀 보고서의 매출 측정기준입니다.                                                                                  |
| 대시보드 빌더                           | 대시보드 빌더에서 작성한 커스텀 대시보드의 매출 측정기준입니다.                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="이커머스 보고" }

사용자 기반이 아닌 계산 필드(예: Campaign 또는 Canvas 매출)의 경우, 매출은 모든 보고서에서 동일한 방식으로 계산됩니다. 주문 내 제품별로 `price`에 `quantity`를 곱한 후, 각 `order_placed` 이벤트 내 제품 전체를 합산합니다.

{% alert note %}
매출 계산 시 개별 제품 수량은 주문당 1,000단위로 제한됩니다. 제품에 수량 필드가 누락된 경우 기본값은 1단위입니다. 원본 `ecommerce.order_placed` 이벤트에는 전송한 전체 수량이 유지되며, 매출 계산에만 상한이 적용됩니다.<br><br>
레거시 구매 이벤트에서 `ecommerce.order_placed`로 마이그레이션하는 경우, 통합을 변경하기 전에 Braze 계정 팀과 조율하세요. 전환 기간 동안 레거시 구매와 `ecommerce.order_placed` 이벤트를 모두 전송하여 올바르게 트리거되는지 확인하고, 활성 Campaigns, Canvases, Segments를 새 이벤트로 마이그레이션할 준비를 하세요. 계정 팀이 레거시 구매 이벤트에서 `ecommerce.order_placed`로 매출 보고를 전환하는 계획을 도와드릴 수 있습니다.
{% endalert %}

### BrazeAI<sup>TM</sup>

[예측 이벤트]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events), [예측 이탈]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn), [아이템 추천]({{site.baseurl}}/user_guide/brazeai/item_recommendations)은 이커머스 이벤트를 대상 이벤트 및 신호로 지원하며, 전용 "Order Placed" 옵션이 있습니다. 표준화된 스키마 덕분에 사용자 기반 전체에서 데이터가 일관되므로 이러한 모델의 신뢰성이 높아집니다.

### 데이터 내보내기 {#export-data}

Braze는 이커머스 이벤트 데이터를 데이터 웨어하우스, BI 도구 또는 다운스트림 시스템에서 사용할 수 있도록 여러 내보내기 방법을 제공합니다. 이커머스 권장 이벤트는 다른 이벤트 데이터와 동일한 채널을 통해 내보내집니다.

| 내보내기 경로                         | 포함 내용                                                                                                                                                                                 |
|------------------------------------- |------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)                            | 이커머스 이벤트가 커스텀 이벤트로 스트리밍됩니다. `ecommerce.*` 네임스페이스를 검색하여 찾을 수 있습니다. 각 주문의 제품은 구매 항목으로 확인할 수 있습니다.                                                |
| [Snowflake 데이터 공유]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing)               | 이커머스 이벤트가 커스텀 이벤트로 공유됩니다. `ecommerce.*` 네임스페이스를 검색하여 찾을 수 있습니다. 각 주문의 제품은 구매 테이블에서 확인할 수 있습니다.                                   |
| [Segment 데이터를 CSV로 내보내기]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv)           | Segment 멤버의 CSV 내보내기입니다. 이커머스 이벤트를 포함하려면 커스텀 이벤트 드롭다운에서 이름으로 선택합니다.                                                                                |
| [Segment별 사용자 프로필 내보내기 (API)]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment#prerequisites) | Segment 멤버의 사용자 프로필 데이터로, API를 통해 반환됩니다. 이커머스 이벤트는 커스텀 이벤트로 포함됩니다.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 aria-label="데이터 내보내기" }

### 특정 제품별로 사용자를 세분화하려면 어떻게 하나요? {#how-do-i-segment-users-by-a-specific-product}

세그먼터를 사용하면 사용자가 이커머스 이벤트를 수행한 횟수로 필터링할 수 있습니다. 특정 제품 속성정보(예: `product_id` 또는 `product_name`)로 필터링하려면 중첩된 이벤트 속성정보 필터링을 지원하는 [세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension)을 사용하세요. 예를 들어, 최근 90일 이내에 "SKU-123" 제품을 구매한 모든 사용자를 찾을 수 있습니다.