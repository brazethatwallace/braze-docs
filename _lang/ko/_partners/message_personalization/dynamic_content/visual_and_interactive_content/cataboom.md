---
nav_title: CataBoom
article_title: CataBoom
description: "Catapult, 고유 URL 요청, 연결된 콘텐츠를 사용하여 CataBoom 게임화 경험을 Braze에 연결하는 방법을 알아보세요."
alias: /partners/cataboom/
page_type: partner
search_tag: Partner
---

# CataBoom

> [CataBoom](https://www.cataboom.com/)은 게임화 플랫폼입니다. 브랜드는 이를 사용하여 스핀 투 윈 게임, 퀴즈, 인스턴트 윈 게임 등 인터랙티브 디지털 경험을 구축하고 출시합니다. 이러한 경험은 인게이지먼트를 심화하고 퍼스트파티 데이터를 수집합니다.

*이 통합은 CataBoom에서 유지 관리합니다.*

## 이 통합에 대하여 {#about-this-integration}

Braze와 CataBoom 통합을 사용하여 메시지에 개인화된 게임 링크를 추가하세요. Catapult Campaign과 Braze 간에 사용자 식별자와 속성을 실시간으로 전달할 수 있습니다. 그런 다음 해당 데이터를 활용하여 개인화된 Campaign, 트리거, 후속 여정을 구동할 수 있습니다.

## 필수 조건 {#prerequisites}

시작하기 전에 다음이 필요합니다:

| 필수 조건 | 설명 |
| --- | --- |
| Catapult 계정 | 이 통합을 사용하려면 Catapult 계정이 필요합니다. |
| Braze REST API 키 (선택 사항) | Catapult 웹훅을 사용하는 경우, 사용 사례에 필요한 사용자 데이터 권한이 있는 Braze REST API 키가 필요합니다. Braze에서 **설정** > **API 및 식별자** > **API 키**로 이동하여 키를 생성하세요. |
| Braze REST 엔드포인트 (선택 사항) | Catapult 웹훅을 사용하는 경우, [Braze 인스턴스]({{site.baseurl}}/api/basics#endpoints)에 해당하는 Braze URL과 일치하는 REST 엔드포인트 URL을 사용하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 1단계: 게임 경험 만들기 {#step-1-create-your-game-experience}

Catapult 플랫폼에서 게임 경험을 만드세요. 다음 단계에서는 **Link Configuration** 페이지에서 Request Unique URL API를 사용하는 간단한 스피너 설정을 보여줍니다. CataBoom은 확률 기반 메커니즘, 스킬 기반 메커니즘, 펀치 카드 및 수집 후 당첨 등의 유틸리티를 포함하여 200개 이상의 게임 옵션을 제공합니다. 다른 게임 유형에도 유사한 흐름을 따를 수 있습니다. CataBoom과 Catapult에 대한 자세한 내용은 [CataBoom 웹사이트](https://www.cataboom.com)를 참조하세요.

1. Campaign을 생성합니다.

상단 내비게이션 영역에서 **New Campaign**을 선택합니다. Campaign 이름을 입력하고, URL 슬러그를 선택하고, 게임 카테고리와 게임 유형을 선택합니다.

![Campaign 이름, URL, 게임 카테고리, 게임 유형 필드가 있는 CataBoom 대시보드 New Campaign 양식.]({% image_buster /assets/img/cataboom/new_campaign.png %})

{: start="2"}
2. Request Unique URL API를 활성화합니다.

내비게이션 메뉴에서 **Link Configuration**을 선택합니다.

**Link Configuration** 페이지에서 **Request Unique URL API**를 활성화합니다. 이 옵션은 나중에 Braze에서 콘텐츠 카드 등에 사용할 수 있는 시스템 간 URL을 생성합니다.

![Request Unique URL API가 활성화되어 있고 API URL이 표시된 CataBoom Link Configuration 페이지.]({% image_buster /assets/img/cataboom/link_configuration.png %})

{: start="3"}
3. 플레이 추적을 Account ID로 설정합니다.

내비게이션 메뉴에서 **Play Control**을 선택합니다.

**Play Control** 페이지의 **Play Tracking** 아래에서 **Play Count Tracked By**를 **Account ID Parameter**로 설정합니다.

추적, 플레이 제한, 웹훅 및 기타 플레이어별 동작을 위해 각 플레이어에 대한 Account ID를 전달할 수 있습니다. 다른 시스템에서는 Account ID를 멤버 ID, 플레이어 ID, 로열티 ID 또는 유사한 이름으로 부르기도 합니다.

![Play Count Tracked By가 Account ID Parameter로 설정된 CataBoom Play Control 페이지.]({% image_buster /assets/img/cataboom/play_control.png %})

이제 Braze에서 테스트를 실행하기에 충분한 구성이 완료되었습니다. 이 섹션의 선택 단계는 일반적인 전체 게임 설정을 완료합니다. Catapult는 게임플레이를 커스터마이즈하는 데 사용할 수 있는 다양한 설정도 제공합니다.

{: start="4"}
4. 크리에이티브를 추가합니다 (선택 사항).

내비게이션 메뉴에서 **Creative**를 선택합니다.

자산을 업로드합니다. Catapult는 게임 경험에 대한 전체 브랜딩 제어를 지원합니다.

![그래픽 다운로드 및 업로드 동작과 게임 미리보기가 있는 CataBoom Creative 페이지.]({% image_buster /assets/img/cataboom/creative.png %})

{: start="5"}
5. 확률 기반 게임의 상품을 구성합니다 (선택 사항).

내비게이션 메뉴에서 **Summary**를 선택합니다.

**Summary** 페이지에서 **Prize Options**를 확장합니다.

Catapult는 시간 기반 상품, 확률 기반 상품 또는 둘 다를 지원합니다. 이를 구성하려면 필요에 따라 **Timed Prizes and Codes**, **Prize Control and Odds Setup** 또는 둘 다를 사용하세요.

다음 스크린샷은 Campaign 요약의 **Prize Options**와 레벨 1에서 50% 당첨 확률을 가진 간단한 확률 구성을 보여줍니다.

![Prize Options 섹션이 확장된 CataBoom Summary 페이지.]({% image_buster /assets/img/cataboom/prize_options_summary.png %})

![상품 레벨, 백분율, 레벨 제어가 있는 CataBoom Odds 페이지.]({% image_buster /assets/img/cataboom/prize_odds.png %})

## 2단계: Braze에서 메시지 만들기 {#step-2-create-a-message-in-braze}

이 예시에서는 **Link Configuration** 페이지의 Request Unique URL을 사용하는 **콘텐츠 카드**를 만드는 방법을 보여줍니다.

1. 플레이 URL에 대한 연결된 콘텐츠를 추가합니다.

콘텐츠 카드에서 필요에 따라 문구와 동적 콘텐츠를 추가합니다. CataBoom Request Unique URL을 [연결된 콘텐츠]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) 태그로 감쌉니다. Catapult에서 사용하는 식별자와 일치하는 Braze 개인화 태그를 사용하여 `AccountID` 쿼리 파라미터를 추가합니다. 이 예시에서는 {% raw %}`{{${user_id}}}`{% endraw %}를 사용합니다.

기본 URL과 `username` 및 `password` 쿼리 파라미터를 Catapult에서 해당 Campaign의 **Link Configuration** 페이지에 있는 값으로 교체하세요.

{% raw %}
```liquid
{% connected_content https://secure.cataboom.com/dplayurl/YOUR_CAMPAIGN_SLUG?username=YOUR_API_USERNAME&password=YOUR_API_PASSWORD&AccountID={{${user_id}}} :save result %}
```
{% endraw %}

저장된 `result`를 카드에서 사용합니다(예: 링크 URL 또는 메시지 본문). Campaign에 대한 CataBoom API의 응답 형식을 따르세요. 쿼리 파라미터와 URL의 Liquid에 대한 자세한 내용은 [API 호출하기]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call)를 참조하세요.

![메시지 필드에 연결된 콘텐츠가 표시되고 카드의 모바일 미리보기가 있는 Braze 콘텐츠 카드 작성기.]({% image_buster /assets/img/cataboom/braze_content_card.png %})

연결된 콘텐츠는 사용자가 콘텐츠 카드를 열 때 고유한 플레이 링크를 요청합니다. 더 맞춤화된 경험을 위해 다른 쿼리 파라미터를 추가할 수 있습니다.