---
nav_title: Shopify 업그레이드 개요
article_title: Shopify 업그레이드 개요
description: "이 참조 문서에서는 Shopify 통합을 최신 버전으로 업그레이드하는 방법을 설명합니다."
page_type: partner
search_tag: Partner
permalink: "/shopify_upgrade_overview/"
hidden: true
---

# Shopify 업그레이드 개요 {#shopify-upgrade-overview}

> 최상의 경험을 제공하기 위한 노력의 일환으로, 모든 Shopify 통합은 2025년 8월 28일까지 최신 버전으로 [업그레이드]({{site.baseurl}}/shopify/)해야 합니다. 이 업그레이드는 Shopify 기술의 중요한 변경 사항이 통합 기능에 영향을 미치기 때문에 필수적입니다.

## 주요 일정 {#key-dates}

- **2월 말~4월:** 특정 그룹(코호트)의 업그레이드 준비가 완료되면 알림을 받게 됩니다. 이 중요한 정보를 놓치지 마세요.
- **업그레이드 마감일:** 모든 고객은 **2025년 8월 28일**까지 업그레이드를 완료해야 합니다.

{% multi_lang_include partners/shopify_alerts.md alert='breaking' %}

## Shopify 통합에서 변경되는 사항 {#whats-changing-in-the-shopify-integration}

Shopify의 결제 확장성 강화 계획의 일환으로, Braze와의 통합에 중요한 변경 사항이 적용됩니다. 알아야 할 사항은 다음과 같습니다:

- **Script Tags 및 `checkout.liquid` 지원 중단:** Shopify는 Script Tags와 `checkout.liquid`를 단계적으로 폐지하고 있습니다. 2025년 8월 이후, 최신 버전의 통합으로 마이그레이션하지 않으면 Braze Web SDK가 Script Tags를 통해 결제 페이지에서 더 이상 로드되지 않습니다.
- **통합의 전반적인 개선 사항:**
    - **권장 이벤트 도입:** 통합에 권장 이커머스 이벤트를 추가하여, Braze의 사전 구축된 템플릿을 통해 일반적인 이커머스 사용 사례를 간소화합니다.
    - **간소화된 ID 관리:** 사용자 ID 관리 방식을 개선하여 익명 사용자 데이터의 추적 및 기여도 분석을 향상시킵니다. ID 관리 처리 방식에 대한 자세한 내용은 [사용자 및 데이터 동기화]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview/#user-and-data-syncing)를 참조하세요.
    - **이메일 및 SMS 가입자 목록:** 현재 이메일 및 SMS 가입자를 수집하고 있는 경우, 업그레이드 과정에서 각 채널에 대한 기본 구독 그룹이 자동으로 생성됩니다. Braze가 이메일 및 SMS 옵트인을 동기화할 때, Braze는 더 이상 고객 프로필의 글로벌 구독 상태를 덮어쓰지 않고 구독 그룹 옵트인만 업데이트합니다.
    - 현재 버전에서 새 버전으로의 모든 변경 사항에 대한 자세한 내용은 [체인지로그](#full-changelog)를 참조하세요.

{% alert important %}
이 업그레이드는 Shopify와 Braze 간 통합의 기능을 유지하는 데 필수적입니다. 개발팀과 긴밀히 협력하여 이러한 변경 사항의 범위와 영향을 평가하고 원활한 전환을 진행하는 것을 권장합니다.
{% endalert %}

## 업그레이드 요구 사항 {#upgrade-requirements}

Shopify 통합 페이지에서 업그레이드 프로세스를 시작하기 전에, 엔지니어링 팀과 함께 다음 요구 사항을 완료하세요:

- **SDK 커스터마이징 확인:** Braze와 Shopify 통합을 커스터마이징한 경우(예: 커스텀 이벤트 또는 속성 로깅), 업그레이드 후에도 이러한 커스터마이징이 올바르게 작동하는지 확인하세요. "상품 조회" 또는 "장바구니 업데이트"와 같은 동작에 대해 자체 브라우저 이벤트를 생성한 경우, 새 커넥터에서 제공하는 기능과 중복되므로 업그레이드 전에 개발자와 협력하여 해당 이벤트를 제거하세요.

{% alert important %}
Shopify 온라인 스토어를 사용 중이며 개발자가 Braze SDK를 Shopify 사이트에 직접 구현했거나, Google Tag Manager 또는 고객 데이터 플랫폼을 통해 구현한 경우, 새 Shopify 커넥터로 업그레이드하면서 기존 방식의 사용을 중단할 계획을 세워야 합니다.
{% endalert %}

- **ID 관리 검토:** Braze 외부 ID를 사용하고 있는 경우, 개발팀과 협력하여 새 통합과의 호환성을 확인하세요. Shopify 스토어 경험 내에서 외부 ID를 설정한 경우, [새로운 ID 관리 프로세스]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_overview/#user-and-data-syncing)와의 충돌을 방지하도록 개발자에게 조정을 요청하세요.
- **영향을 받는 Campaigns, Canvases, Segments 준비:** 가이드 업그레이드 프로세스 중에 Shopify 데이터에 의존하는 Campaigns, Canvases, Segments를 확인하고 내보낼 수 있습니다. 활성 메시지의 원활한 업그레이드를 위해 "OR" 연산자를 사용하여 새로운 필수 Shopify 이벤트 및 속성을 추가하는 것을 권장합니다.
- **유기한 장바구니 및 결제 사용자 여정 생성:** 유기한 장바구니 사용자 여정은 이제 Canvas의 진입 기준에서 "Performed Cart Updated" 트리거를 사용해야 합니다. 또한 유기한 장바구니 및 유기한 결제 사용자 여정 모두에 새로운 장바구니 Liquid 태그를 사용해야 합니다. 시작하는 데 도움이 되도록 새로운 [캔버스 템플릿]({{site.baseurl}}/using_shopify_with_braze/#create-your-canvas-user-journeys)을 사용할 수 있습니다.

이러한 단계를 완료하면 Shopify 통합의 최신 버전으로 성공적으로 업그레이드하는 데 도움이 됩니다.

## 통합 옵션 {#integration-options}

Braze는 이커머스 비즈니스의 다양한 요구를 충족하도록 설계된 두 가지 Shopify 통합 옵션을 제공합니다: **표준 통합**과 **커스텀 통합**.

{% tabs local %}
{% tab 표준 %}
표준 통합은 Shopify 온라인 스토어에 맞춤화되어 원활하고 간편한 설정 프로세스를 제공합니다. 이 옵션을 사용하면 Shopify 스토어를 Braze에 빠르게 연결하여, 광범위한 기술 전문 지식 없이도 강력한 고객 참여 툴을 활용할 수 있습니다. 이 통합 옵션을 통해 고객 데이터를 동기화하고, 개인화된 메시징을 자동화하며, 포괄적인 Braze 기능을 통해 마케팅 활동을 강화할 수 있습니다.

표준 업그레이드 경로를 통해 기존 Shopify 통합을 업그레이드하려면 [Shopify 통합 업그레이드(표준)]({{site.baseurl}}/shopify_standard_upgrade/)를 참조하세요.
{% endtab %}

{% tab 커스텀 %}
커스텀 통합은 Shopify Hydrogen을 사용하거나 헤드리스 스토어를 지원하는 경우 더 유연하고 구성 가능한 솔루션을 제공합니다. 이 옵션을 사용하면 Braze SDK를 Shopify 환경에 직접 구현하여 더 깊은 통합과 맞춤형 기능을 구현할 수 있습니다. 고유한 고객 경험을 만들거나 특정 워크플로를 최적화하려는 경우, 커스텀 통합은 헤드리스 설정에서 Braze의 기능을 완전히 활용하는 데 필요한 도구를 제공합니다.

커스텀 업그레이드 경로를 통해 기존 Shopify 통합을 업그레이드하려면 [Shopify 통합 업그레이드(커스텀)]({{site.baseurl}}/shopify_custom_upgrade/)를 참조하세요.
{% endtab %}
{% endtabs %}

## 체인지로그 {#changelog}

{% alert important %}
이 통합은 Shopify를 지원되는 속성 및 이벤트의 신뢰할 수 있는 소스로 사용합니다. 따라서 데이터가 동기화될 때 Shopify가 고객 프로필의 기존 값(표준 또는 커스텀 속성 등)을 대체할 수 있습니다.
{% endalert %}

### 표준 통합 {#standard-integration}

| 이전 버전 | 최신 버전 |
| --- | --- |
| {::nomarkdown}<ul><li>Script Tag support</li><li>Braze Web SDK only</li><li>Shopify webhooks for events and products</li></ul>{:/} | {::nomarkdown}<ul><li>Web Pixel API support</li><li>New Braze app embed</li><li>Braze Web SDK & JavaScript SDK</li><li>Shopify webhooks for events and products</ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="표준 통합" }

### 통합에서 지원하는 사용자 식별자 {#user-identifiers-supported-by-the-integration}

| 사용자 식별자 | 이전 버전 | 최신 버전 |
| --- | --- | --- |
| Braze 기기 ID |  {::nomarkdown}<ul><li>A randomly generated ID that is stored on the browser</li></ul>{:/} | {::nomarkdown} <ul><li>A randomly generated ID that is stored on the browser</li></ul>{:/}|
| Braze 별칭 | {::nomarkdown}<ul><li>Shopify customer ID</li><li>Shopify email</li></ul>{:/} | {::nomarkdown}<ul><li>Shopify cart token</li><li>Shopify checkout token</li></ul>{:/}|
| Braze 외부 ID | {::nomarkdown}<ul><li>N/A</li></ul>{:/}| {::nomarkdown}<ul><li>Shopify customer ID</li><li>Email</li><li>Hashed email (SHA-256, SHA-1, MD5)</li><li>Custom external ID</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="통합에서 지원하는 사용자 식별자" }

사용자 동기화 및 ID 관리에 대한 자세한 내용은 [사용자 데이터 및 동기화]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_overview/#user-and-data-syncing)를 참조하세요.

{% alert note %}
기본적으로 Braze는 Shopify의 이메일을 외부 ID로 사용하기 전에 자동으로 소문자로 변환합니다. 이메일 또는 해시된 이메일을 외부 ID로 사용하는 경우, 외부 ID로 할당하기 전이나 다른 데이터 소스에서 해싱하기 전에 이메일 주소도 소문자로 변환되었는지 확인하세요. 이렇게 하면 외부 ID의 불일치를 방지하고 Braze에서 중복 고객 프로필이 생성되는 것을 방지할 수 있습니다.
{% endalert %}

### 지원되는 Shopify 이벤트 {#supported-shopify-events}

| 이벤트 또는 속성 | 이전 버전 | 최신 버전 |
| --- | --- | --- |
| 이벤트 |  {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=product%20viewed">shopify_product_viewed</a></li></ul>{:/} | {::nomarkdown}<ul><li>Replaced with <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=product%20viewed">ecommerce.product_viewed</a></li><li>Added <a href="{{ site.homeurl }}{{ site.baseurl }}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#abandoned-browse">abandoned browse Canvas template</a></li></ul>{:/} |
| 이벤트 |  {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?tab=example%20payload">shopify_product_clicked</a></li></ul>{:/} | {::nomarkdown}<ul><li>Deprecated event</li></ul>{:/} |
| 이벤트 | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=abandoned%20cart&tab=example%20payload">shopify_abandoned_cart</a></li><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/setting_up_shopify/#advanced-settings-optional">Abandoned cart timer setting</a></li></ul>{:/} | {::nomarkdown}<ul><li>Replaced with <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=cart%20updated">ecommerce.cart_updated</a></li><li>Deprecated abandoned cart timer setting</li><li>Added <a href="{{ site.homeurl }}{{ site.baseurl }}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#abandoned-cart">abandoned cart Canvas template</a></li></ul>{:/} |
| 이벤트 | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=abandoned%20checkout&tab=example%20payload">shopify_abandoned_checkout</a></li><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/setting_up_shopify/#advanced-settings-optional">Abandoned cart timer setting</a></li></ul>{:/}| {::nomarkdown}<ul><li>Replaced with <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=checkout%20started">ecommerce.checkout_started</a></li><li>Deprecated abandoned checkout timer setting</li><li>Added <a href="{{ site.homeurl }}{{ site.baseurl }}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#abandoned-checkout">abandoned checkout Canvas template</a></li></ul>{:/}|
| 이벤트 | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=created%20order&tab=example%20payload">shopify_created_order</a></li></ul>{:/} | {::nomarkdown}<ul><li>Replaced with <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=order%20placed">ecommerce.order_placed</a></li><li>Added <a href="{{ site.homeurl }}{{ site.baseurl }}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#order-confirmation-and-feedback-survey">order confirmation & post-purchase survey Canvas template</a></li></ul>{:/}|
| 이벤트 | {::nomarkdown}<ul><li><a href="https://braze.com/unlisted_docs/using_shopify_with_braze/?tab=order%20confirmation">Braze purchase event</a></li></ul>{:/}| {::nomarkdown}<ul><li>Deprecated event. Use <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=order%20placed">ecommerce.order_placed</a>.</li></ul>{:/}|
| 이벤트 | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=paid%20order&tab=example%20payload">shopify_paid_order</a></li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| 이벤트 | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=partially%20fulfilled%20order&tab=example%20payload">shopify_partially_fulfilled_order</a></li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| 이벤트 | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=fulfilled%20order&tab=example%20payload">shopify_fulfilled_order</a></li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| 이벤트 | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=cancelled%20order&tab=example%20payload">shopify_cancelled_order</a></li></ul>{:/}| {::nomarkdown}<ul><li>Replaced with <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=order%20cancelled">ecommerce.order_cancelled</a></li></ul>{:/}|
| 이벤트 | {::nomarkdown}<ul><li><a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/?subtab=created%20refund&tab=example%20payload">shopify_created_refund</a></li></ul>{:/}| {::nomarkdown}<ul><li>Replaced with <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=order%20refunded">ecommerce.order_refunded</a></li></ul>{:/}|
| 이벤트 | {::nomarkdown}<ul><li>No Shopify account login event</li></ul>{:/}| {::nomarkdown}<ul><li>Added <a href="{{ site.homeurl }}{{ site.baseurl }}/partners/ecommerce/shopify/shopify_data_features/?subtab=account%20login#tracked-shopify-events">shopify_account_login</a></li></ul>{:/}|
| 속성 | {::nomarkdown}<ul><li>shopify_total_spent</li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| 속성 | {::nomarkdown}<ul><li>shopify_order_count</li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| 속성 | {::nomarkdown}<ul><li>shopify_last_order_id</li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| 속성 | {::nomarkdown}<ul><li>shopify_last_order_name</li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| 속성 | {::nomarkdown}<ul><li>shopify_zipcode</li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
| 속성 | {::nomarkdown}<ul><li>shopify_province</li></ul>{:/}| {::nomarkdown}<ul><li>No changes</li></ul>{:/}|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="지원되는 Shopify 이벤트" }

### 가입자 수집 {#subscriber-collection}

| 수집 유형 | 이전 버전 | 최신 버전 |
| --- | --- | --- |
| 이메일 가입자 수집 |  {::nomarkdown}<ul><li>Override for global email subscription state</li><li>Ability to assign one or more subscription groups</li><li>No default subscription group for the integration for the connected Shopify store</li></ul>{:/} | {::nomarkdown}<ul><li>Deprecated override functionality</li><li>A default subscription group will be created as part of the upgrade</li><li>Ability to assign additional subscription groups</li></ul>{:/} |
| SMS 가입자 수집 |  {::nomarkdown}<ul><li>Required to assign one or more subscription groups</li><li>No default subscription group for the integration for the connected Shopify store</li></ul>{:/} | {::nomarkdown}<ul><li>A default subscription group will be created as part of the upgrade</li><li>Ability to assign additional subscription groups</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="가입자 수집" }

{% alert note %}
현재 이메일 또는 SMS 가입자를 수집하고 있는 경우, 업그레이드가 완료된 후 새로운 기본 구독 그룹이 생성됩니다. 기본 구독 그룹은 Shopify 스토어프론트의 이름으로 지정됩니다. 이 프로세스는 최대 5시간이 소요될 수 있습니다. <br><br>구독 그룹이 사용 가능해지면, 가입한 쇼핑객에게 효과적으로 도달할 수 있도록 활성 Campaigns, Segments 또는 Canvases에 해당 구독 그룹을 포함하세요.
{% endalert %}

### 상품 동기화 {#product-sync}

| 동기화 유형 | 이전 버전 | 최신 버전 |
| --- | --- | --- |
| 초기 상품 동기화 | {::nomarkdown}<ul><li>If product syncing is enabled, initial import of all products in your storefront</li><li>Ability to only import active products</li></ul>{:/} | {::nomarkdown}<ul><li>No&nbsp;changes</li></ul>{:/} |
| 실시간 상품 동기화 | {::nomarkdown}<ul><li>Real-time syncs when products are created, updated, or deleted from your store</li></ul>{:/} | {::nomarkdown}<ul><li>No&nbsp;changes</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="상품 동기화" }

### 채널 {#channels}

| 채널 | 이전 버전 | 최신 버전 |
| --- | --- | --- |
| 인앱 메시지 |  {::nomarkdown}<ul><li>Included within standard integrations for Shopify online stores</li></ul>{:/} | {::nomarkdown}<ul><li>No changes</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="채널" }