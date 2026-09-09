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

Shopify Markets는 기존 Shopify 통합을 확장합니다. [표준]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration) 또는 [커스텀(SDK)]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration) 통합 경로를 통해 기본 스토어프런트를 연결한 다음, 스토어에 구성된 마켓 중 Braze에서 동기화할 마켓을 선택합니다. 기존 통합에서는 카탈로그, 구독 그룹 또는 이벤트를 중단하지 않고 마켓을 추가할 수 있습니다. 단계별 안내는 [Shopify Markets 설정](#shopify-markets-setup)을 참조하세요.

Shopify Markets는 다음과 같은 기능을 제공합니다:

- **마켓 인식 프로필:** 이 통합은 Braze의 표준 국가 및 언어 속성과 함께 각 사용자의 Shopify 로캘을 캡처하므로, 별도의 커스텀 설정 없이 마켓별로 세분화하고 트리거할 수 있습니다.
- **현지화된 카탈로그:** 번역된 제목, 설명, 제품 URL과 함께 가격 및 통화를 포함한 마켓별 제품 데이터가 매일 동기화됩니다.
- **마켓 인식 개인화:** {% raw %}`{% shopify_market %}`{% endraw %} Liquid 태그를 사용하여 Shopify의 번역된 콘텐츠를 포함한 각 사용자의 마켓 카탈로그 제품으로 개인화할 수 있습니다. 또한 `ecommerce.order_placed`와 같은 지원되는 Shopify 이벤트에서 표시 통화 등의 마켓 세부 정보를 참조할 수도 있습니다.
- **기본 스토어 대체:** 사용자가 연결된 마켓 중 어디에도 속하지 않는 경우, Braze는 기본 스토어 설정 및 제품을 사용하므로 모든 사용자가 완전하고 정확한 메시지를 받게 됩니다.

예시는 [Markets 사용자 데이터 사용](#use-markets-user-data) 및 [튜토리얼: 마켓별 제품 및 가격 표시](#tutorial-show-products-and-prices-per-market)를 참조하세요.

## 지원되는 Shopify 마켓 유형 {#supported-shopify-market-types}

최대 25개의 활성 [단일 국가 또는 다중 국가 마켓](https://help.shopify.com/en/manual/markets/getting-started/market-types#country-or-region-markets)을 선택할 수 있습니다. 각 국가는 하나의 선택된 마켓에만 속할 수 있습니다.

하위 지역 마켓, 소매 마켓, B2B 마켓 및 채널 마켓은 지원되지 않습니다.

### 각 마켓에 필요한 사항 {#what-each-market-needs}

선택한 각 마켓에는 활성 제품이 포함된 마켓 카탈로그가 필요합니다. Braze는 해당 카탈로그에서 다음 데이터를 읽습니다:

| 데이터 | 설명 |
| --- | --- |
| 가격 | 마켓 카탈로그에서 해당 마켓의 지정 통화로 설정됩니다. Shopify의 "현지 통화 사용" 설정은 지원되지 않습니다. |
| 번역 | Shopify Translate & Adapt 앱을 통해 만든 맞춤 번역(예: 제품 제목 및 배리언트 제목). Braze는 현재 특정 마켓 언어 설정을 지원하지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="각 마켓에 필요한 사항" }

![호주 마켓에 대한 Shopify 마켓 프로필.]({% image_buster /assets/img/shopify/shopify_markets_example.png %})

### 고려 사항 {#considerations}

#### 일반 {#general}

- **하나의 연결된 스토어:** 한 번에 하나의 마켓 활성화된 Shopify 스토어만 Braze 워크스페이스에 연결할 수 있습니다.
- **로케일 범위:** 로케일은 Shopify Translate & Adapt 앱을 사용하여 구성한 내용을 기반으로 번역된 제품 제목과 설명을 가져오며, 로케일별 URL도 포함됩니다. 가격, 통화 및 기타 공유 카탈로그 필드는 마켓 내 로케일 간에 동일하게 유지됩니다. 기본적으로 Braze는 각 마켓의 [기본 언어](https://help.shopify.com/en/manual/markets/languages), 즉 Shopify가 해당 마켓에 할당한 기본 로케일을 사용합니다. 확장 로케일 지원을 활성화하면 Braze는 해당 마켓에 구성된 추가 로케일을 동기화합니다.

#### 마켓 카탈로그 {#market-catalog}

- **기존 Shopify 카탈로그의 새 마켓 뷰:** 마켓은 별도의 카탈로그를 생성하지 않습니다. 대신 Braze는 기존 Shopify 카탈로그의 일부로 표시합니다. 마켓 데이터는 Shopify 카탈로그에 새 카탈로그 행으로 추가됩니다.
- **카탈로그 셀렉션:** 최대 30개의 카탈로그 셀렉션.
- **새로고침 타이밍:** 마켓 카탈로그 제품 데이터는 하루에 한 번 새로고침됩니다.
- **마켓 가격 및 현지화된 콘텐츠:** 마켓 행에는 마켓의 가격과 `compare_at_price`가 포함되며, Shopify Translate & Adapt 앱을 통해 번역이 설정된 경우 현지화된 제품 및 배리언트 제목과 제품 URL도 포함됩니다.
- **재고 수량:** 마켓 행에는 집계된 재고 값이 포함됩니다. Braze는 현재 위치별 재고를 구분하는 기능을 제공하지 않습니다.
- **가격 인하:** 마켓 카탈로그에 대해 지원됩니다. 마켓 카탈로그의 가격 변경은 기본 스토어 가격이 아닌 해당 마켓의 가격을 기준으로 트리거됩니다. 마켓 카탈로그 제품 데이터는 하루에 한 번 새로고침되므로, 가격 인하는 Shopify에서 가격이 변경될 때가 아니라 매일 감지됩니다.
- **재입고:** [재입고]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications)는 기본 스토어 카탈로그의 제품에 대해 지원됩니다. 마켓 행은 재입고 알림을 트리거하지 않습니다. 재입고는 모든 Shopify 위치에 걸쳐 제품 배리언트의 전체 가용 재고를 확인하므로, 소매 위치에서 재고가 추가되면 알림이 트리거될 수 있습니다.

## Shopify Markets 설정 {#shopify-markets-setup}

### 이미 활성화된 Shopify 통합이 있는 경우 {#if-you-already-have-an-active-shopify-integration}

Markets는 현재 통합에 추가됩니다. 연결을 해제하거나 설정을 다시 구축할 필요가 없습니다.

- 구독 그룹은 스토어 전체 그룹이 되며, 추가로 할당한 그룹을 포함하여 모든 옵트인을 계속 수신합니다.
- 기존 구독자는 이미 속해 있는 그룹에 그대로 유지됩니다. 나중에 국가 그룹을 추가해도 Braze는 기존 구독자를 해당 그룹에 추가하지 않습니다.
- 카탈로그는 계속 동기화됩니다. 마켓 행은 새 카탈로그가 아닌 기존 카탈로그에 추가되며, 기존 선택 항목은 기본값 행에 대해 계속 작동합니다.
- 기본값 스토어가 선택한 마켓과 함께 표시되어, 구독 그룹을 할당하고 카탈로그 선택 항목을 동일한 방식으로 구축할 수 있습니다.

스토어가 이미 연결되어 있는 경우, [2단계](#step-2-select-your-market-user-data)부터 시작하여 각 구성과 작동 방식에 대해 자세히 알아보세요.

### 1단계: Shopify Markets가 활성화된 스토어 연결하기 {#step-1-connect-your-shopify-markets-enabled-store}

1. [Shopify 표준 통합]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration) 또는 [Shopify 커스텀 통합]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration) 경로를 사용하여 스토어를 연결합니다. 스토어가 연결된 후, 설정 컴포저에서 Shopify Markets를 구성합니다.
2. OAuth 플로우를 완료하고 Braze가 OAuth에서 마켓 스코프를 요청하는지 확인합니다:
   - `read_markets`
   - `read_publications`
   - `read_locales`
3. 인증이 성공하고 설정 컴포저가 열리면, **설정 시작**을 선택합니다.
4. Braze SDK를 켭니다.

### 2단계: 마켓 사용자 데이터 선택하기 {#step-2-select-your-market-user-data}

1. **Shopify 데이터 추적**에서 **Shopify Markets 데이터 동기화**를 선택합니다.
2. **마켓 선택**을 선택하여 마켓을 선택하고, 행동 이벤트 및 사용자 속성을 추적하도록 설정했는지 확인합니다.
   - (선택 사항) 히스토리컬 백필 켜기

#### 마켓 사용자 데이터 {#markets-user-data}

Shopify Markets를 지원하기 위해, Braze는 통합의 [표준 이벤트 및 속성]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#tracked-shopify-events) 외에 추가 데이터를 동기화합니다.

##### 고객 프로필 속성 {#user-profile-attributes}

| 속성 | 데이터 타입 | 설명 | 데이터 소스 |
| --- | --- | --- | --- |
| `shopify_locale` | 커스텀 속성 | 고객이 스토어를 탐색하는 언어(예: `en` 또는 `fr-CA`). 고객이 스토어프론트 언어를 변경하면 함께 변경됩니다. | Shopify 고객 로케일 |
| `browser_language` | 표준 속성 | 고객의 브라우저에 설정된 언어. | Braze SDK |
| `country` | 표준 속성 | 고객의 국가. | Braze SDK |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="고객 프로필 속성"}

##### 주문 이벤트 속성정보 {#order-event-properties}

| 속성정보 | 설명 | 데이터 소스 |
| --- | --- | --- |
| `country` | 고객의 2자리 국가 코드. | Shopify에서 고객의 `default_address`, 또는 기본 주소가 설정되지 않은 경우 주문의 `shipping_address` |
| `presentment_currency` | 고객이 결제한 통화로, 스토어 통화와 다를 수 있습니다. | Shopify 주문 표시 통화 |
| `market_handle` | 고객의 국가와 일치하는 마켓의 핸들. 구성된 마켓과 일치하는 것이 없으면 비어 있습니다. | Braze, 마켓 구성에서 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="주문 이벤트 속성정보"}

이러한 속성정보는 다음에 추가됩니다:

- 이커머스 권장 이벤트: `ecommerce.order_placed`, `ecommerce.order_cancelled`, `ecommerce.order_refunded`
- 커스텀 이벤트: `shopify_paid_order`, `shopify_fulfilled_order`, `shopify_partially_fulfilled_order`

##### 마켓 이벤트 속성정보 작동 방식 {#how-these-market-event-properties-work}

| 속성정보 | 작동 방식 |
| --- | --- |
| `market_handle` | `market_handle`은 Shopify에서 마켓에 지정한 핸들(예: `france`)입니다. 동일한 핸들이 카탈로그의 마켓 행 ID 접두사로 사용됩니다(예: `france_46714756268231`). 마켓을 구성하지 않았거나, 주문의 국가가 구성한 마켓과 일치하지 않는 경우 비어 있으므로, Liquid 또는 Segment 필터에서 사용하기 전에 빈 값 여부를 확인하세요. |
| `country` | `country`는 고객의 기본 주소에서 가져오며, 기본 주소가 없으면 `shipping_address`를 사용합니다. 예를 들어, 프랑스에 있는 고객이 일본으로 주문을 보내도 프랑스 마켓으로 유지됩니다. |
| 이벤트 속성정보 | 이벤트 속성정보는 이벤트가 발생한 시점의 스냅샷이며 이후에 변경되지 않습니다. 고객이 나중에 기본 주소를 업데이트하면, 새 이벤트는 새 국가를 사용하지만 과거 이벤트는 기록 당시의 국가를 유지합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="마켓 이벤트 속성정보 작동 방식"}

##### 통화 {#currency}

지원되는 Shopify 장바구니, 결제, 주문 이벤트에는 두 가지 값 세트가 포함됩니다:
- 기존 가격 및 합계 필드에 포함된 스토어 통화(변경 없음)
- 고객이 보고 결제한 금액을 담고 있는 `presentment_currency` 객체

주문 확인 또는 유기한 장바구니 메시지 등에서 고객이 결제한 금액을 표시할 때는 `presentment_currency`를 사용하세요. 마켓 간 매출을 비교할 때는 이미 단일 통화로 되어 있는 스토어 통화 값을 사용하세요.

##### 현지화된 제품 정보 {#localized-product-information}

지원되는 Shopify 이벤트는 기본값 스토어 언어로 제품 및 배리언트 제목을 전달합니다. Braze는 이벤트 페이로드를 번역하지 않습니다.

번역된 제목, 설명 및 제품 URL은 마켓 카탈로그 행에 있습니다. 메시지에서 현지화된 제품 정보를 표시하려면, 이벤트의 제품 또는 배리언트 ID를 사용하여 카탈로그에서 제품을 검색하세요.

### 3단계: 사용자 관리하기 {#step-3-manage-users}

1. 드롭다운에서 `external_id` 유형을 선택합니다.
2. Shopify에서 이메일 및 SMS 옵트인을 켭니다. 이를 통해 Braze가 Shopify에서 이메일 및 SMS 가입 상태를 동기화할 수 있습니다. 두 가지 옵션이 있습니다:
   - **통합 사용:** Braze가 이메일 및 SMS 상태를 동기화합니다. 동기화할 구독 그룹을 선택합니다.
   - **직접 구축:** 상태 관리에 대한 더 많은 제어를 위해, Braze 구독 그룹 엔드포인트를 사용하여 커스텀 통합을 구축합니다.
3. Shopify 동의가 동기화되는 구독 그룹을 선택합니다:
   - **스토어 전체 그룹(필수):** 이메일 그룹 하나와 SMS 그룹 하나 이상을 선택합니다. Braze가 Shopify에서 수신하는 모든 옵트인이 여기에 기록됩니다.
   - **국가 그룹(선택 사항):** 동기화된 마켓의 모든 국가에 하나 이상의 그룹을 할당합니다. Braze가 고객의 국가를 판별할 수 있는 경우 옵트인이 여기에도 기록됩니다.

#### 옵트인 및 옵트아웃 작동 방식 {#how-opt-ins-and-opt-outs-work}

Shopify에서 각 고객은 하나의 이메일 동의 상태와 하나의 SMS 동의 상태를 갖습니다. 고객이 옵트인하면 국가나 목록이 아닌 브랜드에 가입합니다.

Braze는 각 옵트인을 스토어 전체 그룹에 기록합니다. 국가 그룹을 설정했고 Braze가 고객이 어느 국가에 있는지 알 수 있는 경우, 해당 국가의 그룹에도 옵트인이 기록됩니다.

국가 그룹을 설정하지 않으면, 옵트인은 스토어 전체 그룹에만 적용되며, 이는 Shopify가 현재 동의를 처리하는 방식과 동일합니다.

#### Braze가 국가를 판별하는 방법 {#how-braze-determines-country}

| 채널 | 국가 판별 |
| ------- | ---------------------------- |
| 이메일   | 고객의 Shopify 로케일을 먼저 사용하며, 사용할 수 없는 경우 Braze 프로필의 국가 속성을 사용합니다. |
| SMS     | E.164 국가 라우팅 패턴에 따라 결정된 전화번호의 국가를 사용합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="채널별 Braze 국가 판별"}

로케일은 `fr-FR`처럼 지역이 포함된 경우에만 국가를 식별합니다. `fr`만으로는 식별되지 않습니다.

SMS의 경우, 국가는 전화번호에서 가져옵니다. 쇼핑객은 해당 번호로 메시지를 보낼 수 있는 구독 그룹에 추가되어야 합니다.

#### 옵트인 시 발생하는 일 {#what-happens-when-someone-opts-in}

| 국가 상태                           | 스토어 전체 그룹 | 국가 그룹                        |
|------------------------------------------|-------------------|---------------------------------------|
| 판별되었으며, 마켓에 구성됨 | 구독됨        | 해당 국가 그룹에 구독됨   |
| 판별할 수 없음                      | 구독됨        | 구독되지 않음                        |
| 판별되었지만, 마켓에 구성되지 않음 | 구독됨    | 구독되지 않음                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="국가 상태별 옵트인 결과"}

구독 그룹 멤버십은 Shopify의 동의 이벤트를 기반으로 합니다. 쇼핑객의 국가 또는 로케일이 변경되더라도 그룹 멤버십은 변경되지 않습니다. Braze는 Shopify가 새로운 동의 이벤트를 보낼 때만 업데이트합니다. 예를 들어, 국가나 로케일이 변경된 후 쇼핑객으로부터 Shopify에서 동의가 다시 수집된 경우가 해당됩니다.

{% alert note %}
국가 그룹은 언어가 아닌 동의를 제어합니다. 하나의 국가에 여러 언어가 있을 수 있습니다. 캐나다의 영어 및 프랑스어 고객(`en-CA` 및 `fr-CA`)은 동일한 국가 그룹에 속합니다. 메시지에서 언어를 지정하려면 `shopify_locale`을 사용하세요.
{% endalert %}

#### 옵트아웃 시 발생하는 일 {#what-happens-when-someone-opts-out}

Shopify에서의 옵트아웃은 Shopify 통합에 할당된 모든 구독 그룹에서 사용자를 제거합니다. 마켓 사이트를 통해 옵트아웃했든 Shopify 계정 페이지를 통해 옵트아웃했든 동일합니다.

통합에 할당되지 않은 워크스페이스의 구독 그룹은 영향을 받지 않습니다.

#### 구성하지 않은 국가에서의 옵트인 {#opt-ins-from-countries-you-havent-configured}

고객이 구성된 마켓에 포함되지 않은 국가(추가하지 않았거나 해당 마켓을 제거한 경우)에서 옵트인하면, 스토어 전체 그룹에 가입됩니다. 국가 그룹에는 추가되지 않습니다.

마켓 구성은 메시지를 보낼 수 있는 대상을 제한하지 않습니다. 법적 또는 규제상의 이유로 특정 국가에 메시지를 보낼 수 없는 경우, Segment 필터로 해당 사용자를 제외하거나 별도의 구독 그룹으로 라우팅하세요.

{% alert tip %}
해당 Segment를 서비스하지 않는 국가의 차단 목록이 아닌, 서비스하는 국가의 허용 목록으로 구축하세요. 국가를 판별할 수 없는 사용자는 국가 값이 없으므로, 차단 목록으로는 이들을 포착할 수 없습니다.
{% endalert %}

SMS의 경우, 각 구독 그룹의 국가 권한이 여전히 전송을 제어합니다. 해당 그룹에서 국가가 허용되지 않는 사용자는 해당 그룹에서 메시지를 받지 못합니다.

#### 사용자가 나중에 국가 그룹에 추가되지 않음 {#users-arent-added-to-country-groups-later}

Braze가 옵트인 시 고객의 국가를 판별할 수 없는 경우, 스토어 전체 그룹에만 추가됩니다. 나중에 국가가 알려져도 해당 국가의 그룹에 자동으로 추가되지 않습니다.

기존 통합 스토어에서 Markets를 켜면, 기존 구독 그룹이 스토어 전체 그룹이 됩니다. 기존 구독자는 이 그룹에 구독된 상태로 유지되며 새로운 국가 그룹에 자동으로 추가되지 않습니다.

직접 추가하려면, 해당 사용자를 위한 Segment를 구축하고 Canvas [사용자 업데이트]({{site.baseurl}}/user_update) 단계를 사용하여 구독하세요.

#### 그룹 간 구독자 계산 {#counting-subscribers-across-groups}

하나의 옵트인이 사용자를 둘 이상의 구독 그룹에 추가할 수 있으므로, 그룹 합계를 더하면 동일한 사용자가 여러 번 계산됩니다. 고유 구독자 수가 필요한 경우 Segment를 사용하세요.

#### 작동 방식 {#how-it-works}

1. 고객이 결제 시 또는 양식을 통해 SMS에 가입합니다.
2. Shopify가 가입을 Braze에 전송합니다.
3. Braze가 사용자를 보류 상태로 설정하고 확인 문자를 전송합니다.
4. 고객이 확인 키워드로 응답하면 구독됩니다.
5. 확인 기간이 종료되기 전에 응답하지 않으면 보류 상태로 유지됩니다.

자세한 내용은 [더블 옵트인]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in)을 참조하세요.
### 4단계: 제품 동기화하기 {#step-4-sync-products}

1. 마켓 내 제품을 동기화하려면, **Shopify 제품 및 배리언트를 Braze에 동기화**를 선택합니다.
2. Braze 카탈로그 ID를 할당하고 추가 설정을 구성합니다.

카탈로그에는 스토어의 기본값 제품에 대한 마켓별 보기가 포함됩니다. 마켓에 게시된 각 제품에 대해, Braze는 이미 지원되는 [표준 Shopify 카탈로그 필드]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs#supported-shopify-catalog-data) 위에 기존 카탈로그에 마켓 행을 추가합니다. 기존 통합에서 Shopify Markets를 켜면 동기화에 몇 분 정도 걸릴 수 있습니다.

마켓 행에서 다음 필드는 마켓별 값을 갖습니다:

| 필드 | 설명 |
| --- | --- |
| `id` | 마켓 핸들이 접두사로 붙는 복합 ID(예: `france_46714756268231`). 기본값 행은 원래 항목 ID를 유지합니다. |
| `market_handle` | Shopify에서 마켓에 지정한 핸들(예: `france`). |
| `locale` | 마켓의 로케일로, 번역된 콘텐츠의 언어를 결정합니다. |
| `price` | 가격 목록 조정이 적용된 후 마켓의 상황별 가격에서 가져온 마켓별 가격. |
| `compare_at_price` | 조정 후 마켓별 비교 가격. 마켓의 가격 목록이 비교 가격을 무효화하도록 설정된 경우를 포함하여, 해당 마켓에 대해 비교 가격이 확인되지 않으면 Braze는 `0`을 반환합니다. |
| `product_title` 및 `variant_title` | Shopify Translate & Adapt 앱을 통해 번역을 설정한 경우 번역된 제목. |
| `product_url` | 해당 마켓의 제품 URL. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="마켓 행 카탈로그 필드"}

{% alert important %}
`inventory_quantity`는 마켓 행에 포함되지 않습니다. 기본값 행에만 표시되며, 모든 Shopify 위치에서 제품 배리언트의 총 가용 재고를 반영합니다.<br><br>Liquid에서 `compare_at_price`를 사용할 때, 표시하거나 할인을 계산하기 전에 "0" 여부를 확인하세요. 비교 가격이 없는 마켓은 가격이 0이거나 잘못된 할인으로 렌더링됩니다.
{% endalert %}

### 5단계: 채널 활성화하기 {#step-5-activate-channels}

1. (선택 사항) 인브라우저 메시징 활성화 여부를 선택합니다.
2. **설정 완료**를 선택합니다.

## Markets 사용자 데이터 활용 {#use-markets-user-data}

이러한 속성과 속성정보가 고객 프로필에 저장되면, 이를 사용하여 마켓별로 사용자를 타겟팅하고 메시지를 개인화할 수 있습니다.

### 세분화에서 마켓별 타겟팅 {#target-by-market-in-segmentation}

Segments 및 Campaign 또는 Canvas 진입 기준에서 국가, 브라우저 언어 또는 `shopify_locale`으로 필터링합니다. 예를 들어, 특정 마켓의 사용자로 오디언스를 구성하거나 로캘별로 Canvas를 분할할 수 있습니다.

### Liquid로 트리거 및 개인화 {#trigger-and-personalize-with-liquid}

다음 Liquid 변수를 사용하여 메시지에서 마켓 데이터를 참조할 수 있습니다.

#### 고객 프로필에서 {#from-the-user-profile}

| 속성 | Liquid |
| --- | --- |
| 고객의 언어 | {% raw %}`{{custom_attribute.${shopify_locale}}}`{% endraw %} |
| 고객의 국가 | {% raw %}`{{${country}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Markets 고객 프로필 Liquid 변수"}

#### 주문 이벤트에서 {#from-order-events}

| 이벤트 속성정보 | Liquid |
| --- | --- |
| 주문의 국가 | {% raw %}`{{event_properties.${country}}}`{% endraw %} |
| 주문의 마켓 | {% raw %}`{{event_properties.${market_handle}}}`{% endraw %} |
| 고객이 결제한 통화 | {% raw %}`{{event_properties.${metadata}.presentment_currency.code}}`{% endraw %} |
| 해당 통화의 주문 합계 | {% raw %}`{{event_properties.${metadata}.presentment_currency.<total_value>}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Markets 주문 이벤트 Liquid 변수"}

#### 고객의 통화로 가격 표시 {#show-prices-in-the-customers-currency}

금액은 항상 통화 코드와 함께 표시해야 합니다. 금액만 단독으로 표시하는 것은 멀티 마켓 메시징에서 가장 흔한 실수입니다. "129.95"는 각 마켓에서 서로 다른 의미를 가지기 때문입니다.

확인 메시지 같은 주문 수준 메시지에는 주문 합계를, 장바구니나 추천 같은 제품 수준 콘텐츠에는 제품 가격을 사용합니다.

{% raw %}
```liquid
Thanks for your order! Your total: {{event_properties.${metadata}.presentment_currency.code}}
{{event_properties.${metadata}.presentment_currency.<total field>}}
```
{% endraw %}

이러한 속성정보는 이벤트와 함께 전달되므로, 추가 설정 없이도 각 고객의 마켓에 맞는 정확한 메시지가 유지됩니다.

#### 빈 값 확인 {#check-for-empty-values}

두 가지 값은 항상 존재하지 않을 수 있으며, 누락된 경우 잘못 렌더링됩니다.

`market_handle`은 고객의 국가가 구성된 마켓과 일치하지 않을 때 비어 있습니다. 이 값을 기준으로 분기하기 전에 확인합니다:

{% raw %}
```liquid
{% if event_properties.${market_handle} != blank %}
  ...
{% endif %}
```
{% endraw %}

`compare_at_price`는 해당 마켓에 대해 비교 가격이 확인되지 않을 때 `0`을 반환합니다. 표시하거나 할인을 계산하기 전에 `0`인지 확인해야 합니다. 그렇지 않으면 고객이 0원으로 취소선이 그어진 가격을 볼 수 있습니다.

#### 현지화된 제품 정보 표시 {#show-localized-product-information}

이벤트의 제품 이름은 기본 스토어 언어로 되어 있습니다. 번역된 제목, 설명 또는 제품 URL을 표시하려면 이벤트의 제품 또는 배리언트 ID를 사용하여 카탈로그에서 제품을 조회합니다. 예시는 [튜토리얼: 마켓별 제품 및 가격 표시](#tutorial-show-products-and-prices-per-market)를 참조하세요.

### 주문 활동에서 메시지 트리거 {#trigger-messages-from-order-activity}

마켓 속성정보는 지원되는 Shopify 이벤트에 포함되므로, 주문에 의해 트리거되는 Campaign 또는 Canvas는 추가 설정 없이 이를 사용할 수 있습니다. 이러한 이벤트에는 `country`, `presentment_currency`, `market_handle`이 포함됩니다.

| 이벤트 유형 | 이벤트 |
| --- | --- |
| 이커머스 추천 이벤트 | `ecommerce.order_placed`, `ecommerce.order_cancelled`, `ecommerce.order_refunded` |
| 커스텀 이벤트 | `shopify_paid_order`, `shopify_fulfilled_order`, `shopify_partially_fulfilled_order` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="마켓 속성정보가 포함된 Shopify Markets 주문 이벤트"}

`presentment_currency`는 다른 속성정보에 비해 가장 넓은 범위를 지원합니다. 지원되는 장바구니, 결제, 주문 이벤트에 포함되므로, 장바구니 이벤트에 `country`나 `market_handle`이 포함되지 않더라도 유기한 장바구니 메시지에서 고객이 본 금액을 표시할 수 있습니다. 자세한 내용은 [통화](#currency)를 참조하세요.

## 마켓 보고서 {#markets-reporting}

마켓이 활성화되면, Braze는 매출과 메시지 성능을 국가별로 분류합니다.

### 국가별 매출 {#revenue-by-country}

매출 보고서에는 전체 기간 및 선택한 기간 모두에 대해 앱 분류와 함께 국가별 분류가 포함됩니다.

각 주문은 하나의 국가에 귀속되며, 해당 주문의 전체 매출은 그 국가에 반영됩니다. 국가는 먼저 주문 정보에서 선택되고, 그 다음으로 구매자의 프로필에서 선택됩니다. 두 가지 모두 확인할 수 없는 주문은 **알 수 없음** 아래에 표시됩니다.

매출은 매출 보고서의 나머지 부분과 동일하게 USD로 표시됩니다. 구매자가 실제로 결제한 금액을 확인하려면 주문 이벤트의 `presentment_currency`를 사용하세요.

### 국가별 성능 {#performance-by-country}

Campaign 및 Canvas 분석에는 각 국가에서 메시지가 어떻게 수행되었는지와 국가별 합계 행을 보여주는 **국가별 성능** 테이블이 포함됩니다. 통화 및 총 매출은 주문의 `presentment_currency`에서 집계됩니다.

| 열 | 표시 내용 |
| --- | --- |
| 국가 | 메시지가 도달한 각 국가입니다. |
| 통화 | presentment_currency 기준으로 집계된 해당 국가의 매출 통화입니다. |
| 총 매출 | 해당 국가에 귀속된 매출입니다. |
| 구매 | 해당 국가에 귀속된 구매입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="국가별 성능 열에 표시되는 내용"}

## 마켓 제거 {#remove-a-market}

마켓을 제거하면 Braze가 해당 국가의 새 데이터를 동기화하지 않습니다. 이미 보유하고 있는 데이터는 삭제되지 않습니다.

### 구독 그룹 {#subscription-groups}

마켓을 제거하면 마켓 구성이 업데이트됩니다. 워크스페이스에서 구독 그룹이 삭제되거나 국가 그룹에 이미 구독한 사용자가 제거되지는 않습니다.

#### 설정에서 변경되는 사항 {#what-changes-in-your-setup}

- 제거된 마켓의 국가는 더 이상 마켓 UI에 표시되지 않습니다.
- Braze는 통합 구성에서 해당 국가의 구독 그룹 할당을 제거합니다.

#### 변경되지 않는 사항 {#what-stays-the-same}

- 국가 구독 그룹은 워크스페이스에 그대로 남아 타겟팅에 사용할 수 있지만, Shopify는 더 이상 해당 그룹에 옵트아웃을 동기화하지 않습니다. Shopify에서 옵트아웃한 사용자는 다른 방법(예: [구독 그룹 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups) 또는 Braze의 옵트아웃 워크플로)으로 구독 상태를 업데이트하지 않는 한, 해당 국가 그룹에서 여전히 구독 상태로 표시될 수 있습니다.
- 제거된 마켓의 국가 그룹에 이미 구독한 사용자는 구독 상태를 유지합니다.

#### 향후 동의 동기화 {#future-consent-sync}

- 제거된 국가의 쇼핑객이 새로 옵트인하면, [구성하지 않은 국가의 옵트인](#opt-ins-from-countries-you-havent-configured)과 동일하게 스토어 전체 그룹에만 동기화됩니다.
- Braze는 더 이상 제거된 국가의 국가 그룹에 새로운 옵트인 또는 옵트아웃을 동기화하지 않습니다.
- 스토어 전체 구독 그룹은 계속해서 동의 업데이트를 수신합니다.

### 사용자 데이터 {#user-data}

- `shopify_locale` 및 `country`를 포함하여 사용자 프로필에 이미 있는 속성은 변경되지 않습니다.
- 새 주문 이벤트 내의 `market_handle`은 더 이상 사용할 수 없습니다.
- 제거된 마켓에 대한 Shopify 마켓 Segment 필터는 더 이상 사용할 수 없습니다.
- 제거된 마켓을 참조하는 Liquid는 더 이상 사용할 수 없습니다.

### 카탈로그 {#catalogs}

- 해당 마켓의 마켓 행은 더 이상 새로고침되지 않으며 카탈로그에서 제거됩니다.
- 해당 마켓 행을 기반으로 구축된 카탈로그 셀렉션은 더 이상 제품을 반환하지 않습니다. 다음 발송 전에 해당 셀렉션을 업데이트하거나 제거하세요.
- 기본 행과 이를 기반으로 구축된 셀렉션은 영향을 받지 않습니다.

## 튜토리얼: 마켓별 제품 및 가격 표시 {#tutorial-show-products-and-prices-per-market}

마켓 인식 카탈로그를 사용하여 각 사용자에게 자신의 마켓에 해당하는 제품과 가격을 보여주는 단일 메시지를 작성하세요.

1. 마켓 데이터를 사용하는 셀렉션을 만듭니다.
2. Liquid를 사용하여 메시지에서 셀렉션을 참조합니다.

메시지가 특정 마켓 하나만을 대상으로 할 때는 고정 마켓을 사용할 수 있습니다.

### 1단계: 마켓 데이터를 사용하여 셀렉션 생성 {#step-1-create-a-selection-using-markets-data}

[셀렉션]({{site.baseurl}}/catalog_selections)은 메시지에서 참조하는 큐레이트된 제품 집합입니다. 동기화된 마켓이 있는 Shopify 카탈로그의 경우, **필터 설정** 섹션에 제품 데이터를 하나의 마켓으로 범위 지정하거나 사용자별로 개인화할 수 있는 **마켓 범위** 영역이 포함되어 있습니다.

1. Shopify 카탈로그로 이동하여 **셀렉션** 탭을 엽니다.
2. **셀렉션 만들기**를 선택한 다음, 셀렉션 이름을 지정하고 선택적 설명을 추가한 후 결과 제한을 설정합니다.
3. **필터 설정**의 **마켓 범위** 아래에서, **마켓** 드롭다운을 통해 셀렉션이 마켓별 제품을 확인하는 방식을 선택합니다:
   - **개인화된:** 각 수신자가 프로필의 `country` 속성과 일치하는 마켓의 제품과 가격을 봅니다.
   - **동기화된 마켓:** 마켓 이름을 선택하여 해당 마켓의 제품과 가격에 셀렉션을 고정합니다. 메시지가 단일 마켓만을 대상으로 할 때 사용합니다.
4. 추가 필터 기준을 완료한 후 셀렉션을 저장합니다.
5. **사용자로 미리보기**에서 사용자를 선택하여 해당 프로필에 대해 셀렉션이 반환하는 결과를 확인합니다. **개인화된**을 사용하는 셀렉션은 사용자를 선택한 후에만 미리볼 수 있습니다.

| 대상 | 필터 |
| --- | --- |
| 특정 마켓 | `market_handle` = `au` |
| 기본 제품만 | `market_handle` = `default` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="대상 및 관련 필터"}

{% alert note %}
마켓을 지정하지 않으면 Braze는 기본 제품을 사용합니다.
{% endalert %}

### 2단계: 메시지에 마켓 인식 카탈로그 셀렉션 추가 {#step-2-add-market-aware-catalog-selections-to-messages}

단일 메시지에서 모든 사용자에게 자신의 마켓에 해당하는 제품을 제공하려면 다음 필터로 셀렉션 하나를 만듭니다:

| 셀렉션 이름 | 필드 | 연산자 | 값 |
| --- | --- | --- | --- |
| `market_products` | `market_handle` | equals | {% raw %}`{{shopify_market.handle}}`{% endraw %} |
| `default_products` | `market_handle` | equals | `default` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="셀렉션 이름 및 관련 필터"}

전송 시 Braze는 {% raw %}`{{shopify_market.handle}}`{% endraw %}를 각 사용자의 마켓으로 대체하므로, `market_products`는 모든 사용자에게 적절한 제품을 제공합니다. `default_products`는 일치하는 마켓이 없는 사용자를 위한 대체 항목입니다.

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
- `<your_catalog_name>`을 카탈로그 이름으로 교체하고, 셀렉션 이름이 다른 경우 본인의 셀렉션 이름을 사용합니다.
- {% raw %}`{{shopify_market.handle}}`{% endraw %} 확인은 일치하는 마켓이 없는 사용자를 `default_products`로 라우팅하므로, 빈 메시지 대신 제품을 수신하게 됩니다.
- Liquid에서 `compare_at_price`를 사용할 때는 표시하거나 할인을 계산하기 전에 "0"인지 확인합니다. 비교 가격이 없는 마켓은 가격을 0으로 렌더링하거나 잘못된 할인을 생성합니다.

마켓의 사용자로 미리보기하여 메시지가 해당 마켓의 제품, 가격 및 번역된 제목을 올바르게 표시하는지 확인합니다.