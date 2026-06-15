---
nav_title: 스윔
article_title: 스윔
description: "이 참고 문서에서는 쇼핑객이 제품을 저장하고 웹사이트, 모바일 앱, 리테일 스토어에서 원활하게 쇼핑을 이어갈 수 있도록 지원하는 Braze와 Swym의 파트너십에 대해 설명합니다."
alias: /partners/swym/
page_type: partner
search_tag: Partner
---

# Swym

> [Swym](https://getswym.com/)은 위시리스트, 나중에 저장, 선물 등록 및 재입고 알림을 통해 이커머스 브랜드가 쇼핑 의도를 파악할 수 있도록 지원합니다. 풍부한 권한 기반 데이터를 사용하여 하이퍼 타겟팅 캠페인을 제작하고 개인화된 쇼핑 경험을 제공하여 참여를 유도하고 전환율을 높이며 로열티를 높일 수 있습니다.

*이 통합은 Swym에서 유지 관리합니다.*

## 통합 정보 {#about-the-integration}

Swym과 Braze의 통합을 통해 쇼핑객의 의도를 판매로 전환하는 개인화된 이벤트 기반 마케팅 캠페인을 제공할 수 있습니다. 이 통합을 사용하면 쇼핑객이 중단한 부분부터 다시 시작하고, 쇼핑 여정 전반에 걸쳐 다른 사람들과 협업하며, 성과가 뛰어난 리타겟팅 캠페인을 받을 수 있습니다.

## 필수 조건 {#prerequisites}

시작하기 전에 다음이 필요합니다:

| 요구 사항 | 설명 |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Swym | 이커머스 플랫폼(Shopify 또는 BigCommerce)에 Swym Wishlist Plus, Back in Stock 앱 또는 둘 다 설치되어 있어야 하며 Enterprise 플랜을 사용 중이어야 합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/api/basics/#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 활용 사례 {#use-cases}

Swym의 Wishlist Plus 및 Back in Stock Alerts 앱을 Braze와 연결하면 위시리스트 추가, 재입고 구독, 가격 인하 알림, 리마인더 등의 쇼핑객 활동 이벤트를 커스텀 이벤트로 Braze에 자동으로 전송할 수 있습니다. 이러한 이벤트는 Braze에서 자동화된 메시지를 트리거하는 데 사용할 수 있으며, 이를 통해 시의적절하고 관련성 있는 매력적인 커뮤니케이션을 제공하여 쇼핑객이 다시 구매로 이어질 수 있도록 유도합니다.

## Swym 통합하기 {#integrating-swym}

### 1단계: Swym 앱을 Braze에 연결하기 {#step-1-connect-your-swym-app-to-braze}

현재 Swym과의 Braze 통합은 관리형 통합이며 셀프 서비스가 아닙니다. 시작하려면 Swym 지원팀([support@getswym.com](mailto:support@getswym.com))에 문의하여 다음 정보를 제공하면 Swym에서 대신 통합을 설정할 수 있습니다:

1. Braze 대시보드에서 `users.track` 권한이 있는 [REST API 키]({{site.baseurl}}/api/basics/#about-rest-api-keys)를 생성합니다.

![Braze에서 API 키 생성하기.]({% image_buster /assets/img/swym/braze-api-key.png %})

{% alert important %}
API 키를 보호하기 위해 Swym에서는 일회성 자동 파괴 링크 도구(예: [OneTimeSecret](https://onetimesecret.com/))를 사용하여 자격 증명을 안전하게 공유할 것을 권장합니다.
{% endalert %}

{: start="2"}
2. Braze는 대시보드와 REST 엔드포인트를 위한 여러 인스턴스를 관리합니다. 프로비저닝된 인스턴스의 [REST 엔드포인트]({{site.baseurl}}/api/basics/#endpoints)를 제공합니다.

3. API 키와 인스턴스 URL을 Swym 지원팀에 공유하면 통합을 설정하고 확인 응답을 보내드립니다.

4. 설정이 완료되면 Swym의 커스텀 이벤트가 Braze에 자동으로 등록됩니다. Braze 대시보드에서 **데이터 설정** > **커스텀 이벤트**로 이동하여 등록된 Swym 이벤트 목록을 확인할 수 있습니다.

5. 해당 커스텀 이벤트의 **Manage Properties**를 선택하면 각 Swym 이벤트의 등록정보를 볼 수 있습니다. 이러한 등록정보에는 메시지를 개인화하는 데 사용할 수 있는 이벤트 값이 포함되어 있습니다.

![Braze의 커스텀 등록정보.]({% image_buster /assets/img/swym/braze-custom-properties.png %})

### 2단계: Braze에 보내고 싶은 이벤트 구독하기 {#step-2-subscribe-to-events-you-want-to-send-to-braze}

Wishlist Plus 앱에서 **Marketing** 탭으로 이동하여 **Automations** 섹션을 찾습니다. 여기에서 구독할 이벤트를 선택할 수 있습니다.

![구독할 이벤트.]({% image_buster /assets/img/swym/braze-event-subscription.png %})

#### Swym Wishlist Plus 앱 이벤트 {#swym-wishlist-plus-app-events}

| 이벤트 이름 | 이 이벤트가 트리거되는 경우 |
|------------|------------------------------|
| Share Wishlist | 쇼핑객이 다른 사람과 위시리스트를 공유하는 경우 |
| Add to Wishlist | 쇼핑객이 위시리스트에 상품을 추가하는 경우 |
| Wishlist Reminder | 쇼핑객의 위시리스트에 있는 상품에 대한 리마인더 |
| Saved for Later Reminder | 쇼핑객의 나중에 저장된 상품에 대한 리마인더 |
| Price Drop alert | 위시리스트에 있는 제품이 할인 판매를 시작하는 경우 |
| Low Stock alert | 위시리스트에 있는 제품의 재고가 부족한 경우 |
| Back in Stock alert | 위시리스트에 있는 제품이 재입고된 경우 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Swym Wishlist Plus app events" }

#### Swym Back in Stock Alerts 앱 이벤트 {#swym-back-in-stock-alerts-app-events}

| 이벤트 이름 | 이 이벤트가 트리거되는 경우 |
|------------|------------------------------|
| Back in Stock Acknowledgment | 쇼핑객이 제품 재입고 시 알림을 받도록 구독하는 경우 |
| Restock Alert | 쇼핑객이 재입고 알림을 요청한 제품이 재입고된 경우 |
| Restock Reminder | 후속 알림(일반적으로 첫 번째 재입고 알림 후 약 24시간 후, 구성 가능) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Swym Back in Stock Alerts app events" }

### 3단계: Braze Campaign 또는 Canvas 생성하기 {#step-3-create-a-braze-campaign-or-canvas}

쇼핑객을 위한 개인화된 메시지 전달을 자동화하려면 구독한 각 이벤트에 대해 Braze에서 별도의 Campaign 또는 Canvas를 생성해야 합니다. 각 Campaign 또는 Canvas는 특정 이벤트에 따라 트리거되도록 구성하고 해당 이벤트 등록정보를 사용하여 메시지에 동적 콘텐츠를 채워야 합니다. 단계별 안내는 [시작하기: Campaigns 및 Canvases]({{site.baseurl}}/user_guide/get_started/campaigns_and_canvases/)를 참조하세요.

![액션 기반 이벤트.]({% image_buster /assets/img/swym/braze-canvas-setup.png %})

자세한 내용은 [Swym 도움말 센터](https://help.getswym.com/en/articles/12344153-braze-integration)를 참조하거나 Swym 지원팀([support@getswym.com](mailto:support@getswym.com))으로 문의하세요.