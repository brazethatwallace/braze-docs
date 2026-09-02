---
nav_title: Shopify Markets
article_title: Shopify Markets
description: "이 참고 문서에서는 Braze와 Shopify Markets 통합을 설정하고 사용하는 방법을 다룹니다."
page_type: partner
search_tag: Partner
permalink: "/shopify_markets/"
hidden: true
---

# Shopify Markets

> 이 문서에서는 Shopify Markets 통합(현재 베타)에 대해 다루며, 범위에 포함되는 내용, 작동 방식, 메시징에서 마켓 데이터를 사용하는 방법을 설명합니다. Braze는 베타 기간 동안 추가 Markets 기능을 점진적으로 출시하며, 시간이 지남에 따라 더 복잡한 마켓 구조를 지원하도록 확장하고 있습니다.

{% alert important %}
Shopify Markets는 현재 베타 버전입니다. 자세한 내용은 Braze 고객 성공 매니저에게 문의하세요.
{% endalert %}

## 통합 작동 방식 {#how-the-integration-works}

Shopify Markets는 기존 Shopify 통합을 확장합니다. [표준]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration) 또는 [커스텀(SDK)]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration) 통합 경로를 통해 기본 스토어프론트를 연결한 다음, 스토어에 구성된 마켓 중 Braze가 동기화할 마켓을 선택합니다. 기존 통합에서는 카탈로그, 구독 그룹 또는 이벤트를 중단하지 않고 마켓을 추가할 수 있습니다. 단계별 지침은 [Shopify Markets 설정](#shopify-markets-setup)을 참조하세요.

Shopify Markets는 다음과 같은 기능을 제공합니다:

- **마켓 인식 프로필.** 통합은 Braze의 표준 국가 및 언어 속성과 함께 각 사용자의 Shopify 로케일을 캡처하므로, 커스텀 설정 없이 마켓별로 세분화하고 트리거할 수 있습니다.
- **현지화된 카탈로그.** 마켓별 제품 데이터가 매일 동기화됩니다: 마켓별 가격, 통화, 가용성, 그리고 번역된 제목, 설명, 제품 URL이 포함됩니다.
- **마켓 인식 개인화.** {% raw %}`{% shopify_market %}`{% endraw %} Liquid 태그를 사용하여 Shopify의 번역된 콘텐츠를 포함한 각 사용자 마켓의 카탈로그 제품으로 개인화할 수 있습니다. `ecommerce.order_placed`와 같은 지원되는 Shopify 이벤트에서 표시 통화 등 마켓 세부 정보를 참조할 수도 있습니다.
- **기본 스토어 대체.** 사용자가 연결된 마켓 중 하나에 속하지 않는 경우, Braze는 기본 스토어 설정과 제품을 사용하여 모든 사용자가 완전하고 정확한 메시지를 받을 수 있도록 합니다.

예시는 [Markets 사용자 데이터 사용](#use-markets-user-data) 및 [마켓 인식 카탈로그 사용 사례](#tutorial-show-products-and-prices-per-market)를 참조하세요.

## 지원되는 Shopify 마켓 유형 {#supported-shopify-market-types}

이 베타 단계에서는 다음 규칙에 따라 Braze에서 최대 25개의 단일 국가 마켓을 선택할 수 있습니다:

- 선택한 각 마켓은 활성 [단일 국가 마켓](https://help.shopify.com/en/manual/markets/getting-started/market-types#country-or-region-markets)이어야 합니다. B2B 및 소매 마켓은 지원되지 않습니다.
  - Shopify의 "현지 통화 사용" 설정은 지원되지 않습니다
- 한 국가는 선택한 마켓 중 하나에만 속할 수 있습니다.
- 다국가 마켓은 이 베타 단계에서 지원되지 않습니다.

선택한 각 마켓에는 Braze가 지원하기 위해 활성 제품이 포함된 마켓 카탈로그가 필요합니다:

- 마켓 카탈로그에 설정된 통화를 사용한 제품의 마켓별 가격
- 마켓별 제품 가용성
- Shopify 번역 및 적응 앱을 통해 만든 제품 번역(예: 제품 제목 또는 배리언트 제목)

![호주 마켓에 대한 Shopify 마켓 프로필.]({% image_buster /assets/img/shopify/shopify_markets_example.png %})

### 고려 사항 {#considerations}

#### 일반 {#general}

- **하나의 연결된 스토어:** 한 번에 하나의 Markets 지원 Shopify 스토어만 Braze 워크스페이스에 연결할 수 있습니다.
- **로케일 범위:** 로케일은 Shopify 번역 및 적응 앱을 사용하여 구성한 내용을 기반으로 번역된 제품 제목과 설명을 가져오며, 로케일별 URL도 포함됩니다. 가격, 통화 및 기타 공유 카탈로그 필드는 마켓 내 로케일 간에 동일하게 유지됩니다. 기본적으로 Braze는 각 마켓의 [기본 언어](https://help.shopify.com/en/manual/markets/languages), 즉 Shopify가 해당 마켓에 할당한 기본 로케일을 사용합니다. 계정에 확장 로케일 지원이 활성화된 경우, Braze는 해당 마켓에 구성된 추가 로케일을 동기화합니다.

#### 마켓 카탈로그 {#market-catalog}

- **기존 Shopify 카탈로그의 새 마켓 뷰:** Markets는 별도의 카탈로그를 생성하지 않습니다. 대신 기존 Shopify 카탈로그의 일부로 표시됩니다. Markets 데이터는 Shopify 카탈로그에 새 카탈로그 행으로 추가됩니다.
- **카탈로그 셀렉션:** 최대 30개의 카탈로그 셀렉션.
- **새로고침 타이밍:** 마켓 카탈로그 제품 데이터는 하루에 한 번 새로고침됩니다.
- **가격 전용 마켓 카탈로그:** 가격 전용 마켓 카탈로그는 판매 채널에 제품을 게시하지 않고 마켓별 가격을 설정합니다. 재고 및 제품 가용성은 기본 스토어 카탈로그에서 동기화되며, 가격은 마켓 카탈로그의 가격 목록 또는 상황별 가격을 반영합니다.

### 지원되지 않는 기능 {#unsupported-features}

이 베타에서는 다음 기능이 지원되지 않습니다:

- 마켓 카탈로그에 대한 가격 인하 및 재입고 트리거
- 마켓 구성 구독 그룹에 대한 이메일 및 SMS 이중 옵트인
- 현재 단일 국가 및 다국가 선택 모델을 넘어서는 중첩 마켓 그룹 또는 국가 그룹 워크플로
- 25개 이상의 마켓 선택
- 마켓 지원 카탈로그에 대한 카탈로그 내보내기
- Shopify의 현지 통화 변환, 반올림 규칙, 탐색 및 결제 시 다중 카탈로그 최저가 동작과의 완전한 동등성

## Shopify Markets 설정 {#shopify-markets-setup}

### 1단계: Markets 지원 Shopify 스토어 연결 {#step-1-connect-your-shopify-markets-enabled-store}

1. [Shopify 표준 통합]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration) 또는 [Shopify 커스텀 통합]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration) 경로를 사용하여 스토어를 연결합니다. 스토어가 연결된 후 설정 컴포저에서 Shopify Markets를 구성합니다.
2. OAuth 플로를 완료하고 Braze가 OAuth에서 마켓 범위를 요청하는지 확인합니다:
   - `read_markets`
   - `read_publications`
   - `read_locales`
3. 인증이 성공하고 설정 컴포저가 열리면 **설정 시작**을 선택합니다.
4. Braze SDK를 활성화합니다.

### 2단계: 마켓 및 데이터 설정 선택 {#step-2-select-your-market-and-data-settings}

1. **Shopify 데이터 추적**에서 **Shopify Markets 데이터 동기화**를 선택합니다.
2. **마켓 선택**을 선택하여 마켓을 선택하고, 행동 이벤트와 사용자 속성을 추적하도록 선택했는지 확인합니다.
   - (선택 사항) 과거 데이터 백필 활성화

#### Markets 사용자 데이터 {#markets-user-data}

Shopify Markets를 지원하기 위해 Braze는 통합의 [표준 이벤트 및 속성]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#tracked-shopify-events)보다 더 많은 데이터를 동기화합니다.

Braze는 각 고객 프로필에 다음과 같은 추가 마켓 컨텍스트를 기록합니다:

| 데이터 유형 | 값 | 데이터 소스 |
| --- | --- | --- |
| 커스텀 속성 | `shopify_locale` | Shopify |
| 표준 속성 | 브라우저 언어 | Braze SDK |
| 표준 속성 | 국가 | Braze SDK |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="고객 프로필 데이터 유형"}

Braze는 마켓 컨텍스트를 지원하기 위해 다음과 같은 추가 주문 이벤트 속성정보도 수집합니다:

| 데이터 유형 | 영향받는 이벤트 | 추가된 새 속성정보 |
| --- | --- | --- |
| 이커머스 권장 이벤트 | `ecommerce.order_placed`<br>`ecommerce.order_cancelled`<br>`ecommerce.order_refunded` | `country`, `presentment_currency`, `market_handle` |
| 커스텀 이벤트 | `shopify_paid_order`<br>`shopify_fulfilled_order`<br>`shopify_partially_fulfilled_order` | `country`, `presentment_currency`, `market_handle` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="주문 이벤트 데이터 유형"}

각 속성정보는 다음 소스에서 파생됩니다:

| 속성정보 | 데이터 소스 |
| --- | --- |
| `country` | Shopify 고객 `default_address`; 사용할 수 없는 경우 Braze는 `shipping_address`를 사용합니다 |
| `presentment_currency` | Shopify 표시 금액 값 |
| `market_handle` | 주문 국가에 대해 구성된 Shopify 마켓; 마켓이 구성되어 있고 국가가 일치하는 경우에만 설정됩니다 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="주문 이벤트 속성정보 데이터 소스"}

### 3단계: 사용자 관리 {#step-3-manage-users}

1. 드롭다운에서 `external_id` 유형을 선택합니다.
2. Shopify에서 이메일 및 SMS 옵트인을 활성화하면 Braze가 Shopify에서 이메일 및 SMS 구독 상태를 동기화할 수 있습니다. 두 가지 옵션이 있습니다:
  - **통합 사용:** Braze가 이메일 및 SMS 상태를 동기화합니다. 동기화할 구독 그룹만 선택하면 됩니다.
  - **직접 구축:** 상태 관리를 더 세밀하게 제어하려면 Braze 구독 그룹 엔드포인트를 사용하여 커스텀 통합을 구축할 수 있습니다.
3. 설정 중 동기화된 마켓과 연결된 각 국가에 대해 기본 구독 그룹을 생성합니다.
  - **새 Shopify 통합:** 국가별로 기본 이메일 및 SMS 구독 그룹을 할당합니다.
  - **기존 Shopify 통합:** 스토어의 현재 기본 그룹이 동기화를 중지합니다. 국가별로 새 기본 이메일 및 SMS 그룹을 할당합니다. 이전 설정은 자동으로 이전되지 않습니다.

#### 옵트인 및 탈퇴 작동 방식 {#how-opt-ins-and-unsubscribes-work}

설정 중에 동기화된 마켓과 연결된 각 국가(최대 25개국)에 대해 기본 이메일 및 SMS 구독 그룹을 구성합니다. 이는 국가 구성을 저장하기 전에 필수입니다. 동의를 둘 이상의 목록으로 라우팅하려면 국가별로 추가 구독 그룹을 할당할 수도 있습니다.

##### 동의는 구성된 모든 국가에 적용됩니다 {#consent-applies-to-all-configured-countries}

사용자의 동의 상태가 Shopify에서 변경되면, Braze는 사용자의 특정 국가뿐만 아니라 연결된 스토어에 연결된 모든 국가의 기본 구독 그룹에 해당 변경 사항을 적용합니다:
  - 사용자가 Shopify에서 구독 상태가 되면, 구성한 각 국가의 기본 이메일 또는 SMS 구독 그룹에 구독됩니다.
  - 사용자가 Shopify에서 구독 취소 상태가 되면, 구성한 각 국가의 기본 이메일 또는 SMS 구독 그룹에서 구독 취소됩니다.

{% alert important %}
Shopify 동의는 스토어 단위이며 국가 단위가 아닙니다. Shopify에서 동의는 고객 레코드당 이메일 한 번, SMS 한 번으로 추적되며, 국가별 또는 목록 유형별로 구독하거나 구독 취소하지 않습니다. 이 때문에 Braze는 단일 국가 또는 단일 구독 그룹에 동의 변경을 적용할 수 없습니다. Shopify에서의 구독 또는 구독 취소 이벤트는 항상 구성된 모든 국가의 기본 구독 그룹에 한꺼번에 적용됩니다. <br><br> 그러나 Braze 내에서는 사용자가 메시징 채널과 상호작용할 때 구독 그룹 수준의 옵트인 및 옵트아웃을 더 세밀하게 제어할 수 있습니다.
{% endalert %}

### 4단계: 제품 동기화 {#step-4-sync-products}

1. 마켓 내 제품을 동기화하려면 **Shopify 제품 및 배리언트를 Braze에 동기화**를 선택합니다.
2. Braze **카탈로그 ID**를 할당하고 추가 설정을 구성합니다.

카탈로그에는 스토어의 기본 제품에 대한 마켓별 뷰가 포함됩니다. 마켓에 게시된 각 제품에 대해 Braze는 이미 지원되는 [표준 Shopify 카탈로그 필드]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs#supported-shopify-catalog-data) 위에 기존 카탈로그에 마켓 행을 추가합니다. 기존 통합에서 Shopify Markets를 활성화하면 동기화에 몇 분이 걸릴 수 있습니다.

마켓 행에서 다음 필드는 마켓별 값을 가집니다:

| 필드 | 설명 |
| --- | --- |
| {% raw %}`market_handle`{% endraw %} | 행의 마켓을 식별합니다. 기본 마켓 행은 `default`를 사용하고, 추가 마켓은 해당 핸들을 사용합니다(예: `au`). |
| {% raw %}`locale`{% endraw %} | 확장 로케일 지원이 활성화된 경우 행의 로케일을 식별합니다(예: `fr`). |
| {% raw %}`price`{% endraw %} | 마켓의 상황별 가격에서 가져온 마켓별 가격. |
| {% raw %}`compare_at_price`{% endraw %} | 마켓별 비교 가격, 또는 Shopify에 해당 마켓의 비교 가격이 없는 경우 `0`. |
| {% raw %}`product_title`{% endraw %} | 행의 로케일에 대한 Shopify 번역이 있는 경우 번역된 제품 제목. |
| {% raw %}`variant_title`{% endraw %} | 행의 로케일에 대한 Shopify 번역이 있는 경우 번역된 배리언트 제목. |
| {% raw %}`product_url`{% endraw %} | 현지화된 URL이 활성화된 경우 마켓 및 로케일에 대한 스토어프론트 URL; 그렇지 않으면 기본 `myshopify.com` 제품 URL. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="마켓 행 카탈로그 필드"}

마켓 행은 마켓 핸들이 접두사로 붙은 복합 `id`를 사용합니다(예: `<market>_<variant_id>`). 확장 로케일 지원이 활성화된 경우 ID에 로케일도 포함됩니다(예: `<market>_<locale>_<variant_id>`). 기본 제품은 원래 ID를 유지합니다.

### 5단계: 채널 활성화 {#step-5-activate-channels}

1. (선택 사항) **인브라우저 메시징**을 활성화할지 선택합니다.
2. **설정 완료**를 선택합니다.

## Markets 사용자 데이터 사용 {#use-markets-user-data}

이러한 속성과 속성정보가 고객 프로필에 설정되면, 마켓별로 사용자를 타겟팅하고 메시지를 개인화하는 데 사용할 수 있습니다.

### 세분화에서 마켓별 타겟팅 {#target-by-market-in-segmentation}

Segments 및 Campaign 또는 Canvas 진입 기준에서 국가, 브라우저 언어 또는 `shopify_locale`으로 필터링합니다. 예를 들어, 특정 마켓의 사용자 오디언스를 구축하거나 로케일별로 Canvas를 분할할 수 있습니다.

### Liquid로 개인화 및 트리거 {#personalize-and-trigger-with-liquid}

메시지에서 데이터를 직접 참조합니다.

| 참조할 사용자 데이터 | 사용할 Liquid |
| --- | --- |
| 사용자의 로케일 | {% raw %}`{{custom_attribute.${shopify_locale}}}`{% endraw %} |
| 사용자의 국가 | {% raw %}`{{${country}}}`{% endraw %} |
| 주문의 국가(트리거된 메시지에서) | {% raw %}`{{event_properties.${country}}}`{% endraw %} |
| 주문의 마켓(트리거된 메시지에서) | {% raw %}`{{event_properties.${market_handle}}}`{% endraw %} |
| 주문의 통화(트리거된 메시지에서) | {% raw %}`{{event_properties.${presentment_currency}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liquid로 참조할 사용자 데이터"}

### 주문 활동에서 메시지 트리거 {#trigger-messages-from-order-activity}

새 주문 속성정보는 각 주문 이벤트와 함께 전달되므로, 주문에서 메시지를 트리거하고 마켓 인식 세부 정보를 사용하여 메시지 내용을 개인화할 수 있습니다.

메시지 본문의 간단한 버전은 다음과 같을 수 있습니다:

{% raw %}
```liquid
Thanks for your order! Your total: {{event_properties.${presentment_currency}}} {{event_properties.${total_value}}}
```
{% endraw %}

속성정보가 이벤트 자체에 있으므로, 추가 설정 없이 각 사용자의 마켓에 맞게 메시지가 정확하게 유지됩니다.

## 튜토리얼: 마켓별 제품 및 가격 표시 {#tutorial-show-products-and-prices-per-market}

마켓 인식 카탈로그를 사용하여 각 사용자에게 자신의 마켓에 맞는 제품과 가격을 보여주는 단일 메시지를 작성합니다.

1. 마켓 데이터를 사용하는 셀렉션을 생성합니다.
2. Liquid로 메시지에서 셀렉션을 참조합니다.

메시지가 하나의 특정 마켓을 타겟팅하는 경우 고정 마켓을 사용할 수 있습니다.

### 1단계: 마켓 데이터를 사용하여 셀렉션 생성 {#step-1-create-a-selection-using-markets-data}

[셀렉션]({{site.baseurl}}/catalog_selections)은 메시지에서 참조하는 큐레이트된 제품 세트입니다. 동기화된 마켓이 있는 Shopify 카탈로그의 경우, **필터 설정** 섹션에 제품 데이터를 하나의 마켓으로 범위를 지정하거나 사용자별로 개인화하는 **마켓 범위** 영역이 포함됩니다.

1. Shopify 카탈로그로 이동하여 **셀렉션** 탭을 엽니다.
2. **셀렉션 생성**을 선택한 다음 셀렉션 이름을 지정하고, 선택적 설명을 추가하고, 결과 제한을 설정합니다.
3. **필터 설정**의 **마켓 범위**에서 **마켓** 드롭다운을 사용하여 셀렉션이 마켓별 제품을 확인하는 방식을 선택합니다:
   - **개인화:** 각 수신자는 프로필의 `country` 속성과 일치하는 마켓의 제품과 가격을 봅니다.
   - **동기화된 마켓:** 이름으로 마켓을 선택하여 셀렉션을 해당 마켓의 제품과 가격에 고정합니다. 메시지가 단일 마켓만 타겟팅하는 경우 사용합니다.
4. 추가 필터 기준을 완료한 다음 셀렉션을 저장합니다.
5. **사용자로 미리보기**에서 사용자를 선택하여 해당 프로필에 대해 셀렉션이 반환하는 내용을 확인합니다. **개인화**를 사용하는 셀렉션은 사용자를 선택한 후에만 미리볼 수 있습니다.

| 타겟 | 필터 |
| --- | --- |
| 특정 마켓 | `market_handle` = `au` |
| 기본 제품만 | `market_handle` = `default` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="타겟 및 관련 필터"}

{% alert note %}
마켓을 지정하지 않으면 Braze는 기본 제품을 사용합니다.
{% endalert %}

### 2단계: 메시지에 마켓 인식 카탈로그 셀렉션 추가 {#step-2-add-market-aware-catalog-selections-to-messages}

단일 메시지에서 모든 사용자에게 자신의 마켓 제품을 제공하려면 다음 필터로 하나의 셀렉션을 생성합니다:

| 셀렉션 이름 | 필드 | 연산자 | 값 |
| --- | --- | --- | --- |
| `market_products` | `market_handle` | equals | {% raw %}`{{shopify_market.handle}}`{% endraw %} |
| `default_products` | `market_handle` | equals | `default` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="셀렉션 이름 및 관련 필터"}

전송 시 Braze는 {% raw %}`{{shopify_market.handle}}`{% endraw %}을 각 사용자의 마켓으로 대체하므로, `market_products`는 모든 사용자에게 올바른 제품을 제공합니다. `default_products`는 일치하는 마켓이 없는 사용자를 위한 대체입니다.

{% raw %}`{% shopify_market %}`{% endraw %} 태그를 사용하여 메시지에서 셀렉션을 참조합니다:

{% raw %}
```liquid
{% shopify_market %}
{% if shopify_market.handle %}
  {% catalog_selection_items <your_catalog_name> <your_market-catalog_selection_name> %}
  {% for item in items %}
    {{ item.product_title }} — {{ item.price }}
  {% endfor %}
{% else %}
  {% catalog_selection_items <your_catalog_name> <your_default-catalog_selection_name> %}
  {% for item in items %}
    {{ item.product_title }} — {{ item.price }}
  {% endfor %}
{% endif %}
```
{% endraw %}

- {% raw %}`{% shopify_market %}`{% endraw %}를 {% raw %}`{% catalog_selection_items %}`{% endraw %} 앞에 배치하여 셀렉션이 실행되기 전에 사용자의 마켓이 설정되도록 합니다.
- `<your_catalog_name>`을 카탈로그 이름으로 바꾸고, 셀렉션 이름이 다른 경우 자체 셀렉션 이름을 사용합니다.
- {% raw %}`{{shopify_market.handle}}`{% endraw %} 확인은 일치하는 마켓이 없는 사용자를 `default_products`로 라우팅하여 빈 메시지 대신 제품을 받을 수 있도록 합니다.

마켓의 사용자로 미리보기하여 메시지가 해당 마켓의 제품, 가격 및 번역된 제목을 표시하는지 확인합니다.