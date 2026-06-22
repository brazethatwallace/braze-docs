---
nav_title: Braze Pilot
page_order: 10.5
layout: dev_guide
guide_top_header: "Braze Pilot"
guide_top_text: "Braze Pilot은 Braze 대시보드와 원활하게 연결되도록 설계된 모바일 앱입니다. 이 앱을 통해 Campaign과 Canvas를 앱으로 실행하여 Braze 메시지를 자신의 휴대폰에서 직접 확인할 수 있습니다. Braze Pilot에는 다양한 산업을 대표하는 가상 브랜드의 앱 시뮬레이션 라이브러리가 포함되어 있어, 고객의 관점에서 메시징이 어떻게 보일지 체험할 수 있습니다."
description: "Braze 대시보드에서 휴대폰으로 메시지를 전송하는 다양한 방법을 확인해 보세요."

guide_featured_title: "섹션 문서"
guide_featured_list:
  - name: Braze Pilot 시작하기
    link: /docs/user_guide/get_started/braze_pilot/getting_started
    image: /assets/img/braze_icons/brush-02.svg
  - name: 데이터 사전
    link: /docs/user_guide/get_started/braze_pilot/data_dictionary
    image: /assets/img/braze_icons/book-closed.svg
  - name: 내비게이션 딥링크
    link: /docs/user_guide/get_started/braze_pilot/deep_links
    image: /assets/img/braze_icons/link-03.svg

---

## Pilot 앱 시뮬레이션 {#pilot-app-simulations}

Braze Pilot의 핵심은 앱 시뮬레이션 라이브러리입니다. 각 앱은 산업별 가상 브랜드를 사실적으로 시뮬레이션한 것으로, 다양한 이벤트와 속성을 기록하도록 계측되어 일반적인 Braze 사용 사례를 구현할 수 있는 무한한 기회를 제공합니다.

{% tabs local %}
{% tab Fitness %}

### Steppington

Steppington은 운동, 운동 목표, Steppington+ 프리미엄 서비스를 제공하는 피트니스 앱입니다. [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards/)를 시연할 수 있는 여러 영역, [기능 플래그]({{site.baseurl}}/developer_guide/feature_flags/)로 표시할 수 있는 섹션, 그리고 이 산업의 다양한 고객 여정을 보여줄 수 있는 풍부한 커스텀 이벤트 로깅 라이브러리를 제공합니다.

![마라톤 훈련, 요가, 사이클링, 웨이트 아이콘이 있는 Steppington 홈 페이지.]({% image_buster /assets/img/braze_pilot/steppington_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab eCommerce %}

### PantsLabyrinth

PantsLabyrinth는 (예상하셨겠지만) 바지를 판매하는 이커머스 앱입니다! PantsLabyrinth 앱에는 전체 장바구니 결제 경험, 피처 플래그로 활성화할 수 있는 선택적 위시리스트 기능, 그리고 영국 친구들과 재치 있는 농담을 나눌 수 있는 다양한 기회가 포함되어 있습니다.

![장바구니에 청바지를 추가할 수 있는 옵션이 있는 PantsLabyrinth 제품 페이지.]({% image_buster /assets/img/braze_pilot/pantslabyrinth_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab Streaming %}

### MovieCanon

MovieCanon은 콘텐츠 참여와 관련된 일반적인 Braze 사용 사례를 보여주기 위해 완벽하게 설계된 스트리밍 서비스입니다.

![시청할 수 있는 다양한 스릴러가 있는 MovieCanon 앱.]({% image_buster /assets/img/braze_pilot/moviecanon_app.png %}){:style="max-width:50%"}

{% endtab %}
{% endtabs %}

## Pilot이 Braze 대시보드와 연결되는 방법 {#how-pilot-connects-with-your-braze-dashboard}

Braze SDK는 앱이나 웹사이트에 통합된 후 사용자로부터 데이터를 수집하는 코드 패키지입니다. Pilot을 대시보드에 연결하면 휴대폰의 Pilot 앱과 Braze SDK 간의 연결이 초기화되며, 대시보드의 API 키 식별자를 Pilot에 제공하여 Braze 인스턴스와의 고유한 연결을 설정합니다.

![Pilot 설정의 첫 번째 단계.]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

Pilot이 Braze 대시보드에 연결되면, Braze SDK는 자체 앱이나 웹사이트에 SDK를 통합한 것과 동일하게 앱에서 작동합니다. 이는 Braze가 다음을 수행한다는 의미입니다:

- 앱 내 가상 브랜드에 특화된 커스텀 데이터를 포함하여 Pilot에서의 사용자 활동 데이터를 저장합니다.
- 세션 데이터, 기기 정보, 푸시 토큰을 자동으로 수집합니다.
- SDK 통합이 필요한 푸시 알림, 인앱 메시지, Content Cards 메시징 채널을 지원합니다.

Braze SDK에 대한 자세한 내용은 [통합]({{site.baseurl}}/user_guide/get_started/integrations/)을 확인하세요.

![통합, API, 데이터 수집을 위한 SDK, 분류, 오케스트레이션, 개인화, 그리고 고객과의 상호 피드백 루프를 위한 메시징 채널의 동작을 포함하는 Braze 고객 참여 스택.]({% image_buster /assets/img/braze_pilot/braze_sdk_diagram.png %}){:style="max-width:70%"}

## Braze의 고객 프로필 {#user-profiles-in-braze}

Braze에 전송된 모든 데이터는 앱이나 웹사이트의 특정 사용자에게 할당된 고객 프로필에 저장됩니다. Pilot을 Braze 대시보드에 연결하면, Braze는 Pilot 사용자인 여러분에 대한 데이터를 기록하기 시작합니다. 이 연결을 통해 생성될 수 있는 사용자 유형은 익명 사용자와 식별된 사용자, 두 가지입니다.

### 익명 사용자 {#anonymous}

이 연결 상태는 아직 로그인하지 않은 앱이나 웹사이트의 게스트 경험을 나타냅니다. Pilot을 익명 사용자로 초기화하면, Braze는 [익명 사용자 프로필]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users/)을 생성하고 해당 프로필에 활동 데이터를 기록합니다. 익명 사용자도 Campaign의 타겟이 될 수 있지만, Braze 대시보드에서 직접 고객 프로필을 조회할 수는 없습니다.

### 식별된 사용자 {#identified}

이 연결 상태는 Braze가 외부 식별자라고 하는 고유 식별자를 통해 고객 프로필을 인식하고 있음을 의미합니다. 대시보드의 **사용자 검색** 페이지에서 이 외부 식별자를 검색하여 고객 프로필을 찾을 수 있으며, 해당 프로필에는 앱에서의 활동을 기반으로 Pilot에서 기록된 모든 사용자 속성과 이벤트가 저장됩니다. Braze 대시보드에서 **Audience** > **사용자 검색**으로 이동한 뒤 Pilot **외부 ID**를 입력하고 프로필을 열어 속성과 이벤트를 확인하세요.

### 연결 유형 {#connection-type}

연결 유형을 확인하려면 Pilot 앱 오른쪽 상단의 연결 상태 표시를 확인하세요.

{% tabs local %}
{% tab 익명 사용자 %}

**익명**은 익명 사용자로 데이터를 기록하고 있음을 나타냅니다. 상태 영역에 **익명** 레이블(예: 마스크 또는 시크릿 스타일 배지)이 표시됩니다.

{% endtab %}
{% tab 식별된 사용자 %}

식별된 사용자로 데이터를 기록하는 경우, 상태 영역에 **식별된 사용자**와 외부 ID가 표시됩니다.

{% endtab %}
{% tab 연결되지 않음 %}

**연결되지 않음**은 아직 Pilot과 Braze SDK 연결을 초기화하지 않았음을 나타냅니다. 상태 영역에는 Pilot이 아직 Braze 워크스페이스에 연결되지 않았음이 표시됩니다.

{% endtab %}
{% endtabs %}

## Campaigns 및 Canvases {#campaigns-and-canvases}

Campaigns와 Canvases는 사용자에게 메시지를 보내는 방법입니다.

- Campaigns는 다양한 채널을 통해 특정 오디언스 세그먼트에 단일 메시지를 보내는 데 가장 적합합니다.
- Canvases는 여러 채널에서 개인화된 고객 여정을 자동화하고 오케스트레이션할 수 있는 고급 Campaign 워크플로우입니다. Canvas 내에서 분기 로직, 지연, 결정 지점, 전환 이벤트를 설정하여 일련의 상호작용을 통해 고객을 안내할 수 있습니다. Canvases는 다양한 접점에서 일관되고 원활한 커뮤니케이션을 보장하여 고객 참여와 전환 가능성을 높이는 데 도움을 줍니다.

## 지원되는 메시징 채널 {#supported-messaging-channels}

Braze Pilot은 현재 [인앱 메시지]({{site.baseurl}}/in-app_messages/)를 지원하며, 사용자가 적극적으로 참여하는 동안 앱 내에서 적시에 메시지를 전달합니다.

![MovieCanon 앱의 인앱 메시지 "MovieCanon을 즐기고 계신가요? 친구를 추천하세요!" 추천을 보내기 위해 이메일 주소를 입력할 수 있는 옵션이 있습니다.]({% image_buster /assets/img/braze_pilot/moviecanon_iam.png %}){:style="max-width:40%"}