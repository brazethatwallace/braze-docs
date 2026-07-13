# 배너 {#banners}

> 배너를 사용하면 사용자에게 개인화된 메시징을 생성할 수 있으며, 이메일이나 푸시 알림과 같은 다른 채널의 도달 범위를 확장할 수 있습니다. 배너를 앱이나 웹사이트에 직접 삽입할 수 있어 자연스러운 경험을 통해 사용자와 소통할 수 있습니다.

## 필수 조건 {#prerequisites}

배너의 가용성은 Braze 패키지에 따라 다릅니다. 시작하려면 계정 매니저 또는 고객 성공 매니저에게 문의하세요.

시작하기 전에 앱이나 웹사이트에 [배너 배치]({{site.baseurl}}/developer_guide/banners/placements)가 생성되어 있는지 확인하세요.

![기기에서 렌더링된 배너 예시.]({% image_buster /assets/img/banners/sample_banner.png %})

## 배너를 사용하는 이유는 무엇인가요? {#why-use-banners}

배너를 사용하면 마케팅 및 제품 팀이 앱 또는 웹사이트 콘텐츠를 동적으로 개인화하여 실시간 사용자 적격성과 행동을 반영할 수 있습니다. 배너는 지속적으로 메시지를 인라인으로 표시하여 비침해적이고 상황별로 관련성 있는 경험을 제공하며, 세션 시작 시 또는 앱이나 웹사이트에서 명시적으로 요청할 때 세션 중간에 새로고침할 수 있습니다.

배너가 앱 또는 웹사이트에 통합된 후, 마케터는 드래그 앤 드롭 편집기 또는 전체 HTML 편집기를 사용하여 배너를 디자인하고 출시할 수 있으므로 지속적인 개발자 지원이 필요 없어 복잡성을 줄이고 효율성을 높일 수 있습니다.

| 사용 사례 | 설명 |
| --- | --- |
| 공지사항 | 다가오는 이벤트나 정책 변경과 같은 공지사항을 앱 경험의 최전선에 유지하세요. |
| 오퍼 개인화 | 각 사용자의 탐색 기록, 장바구니 내용, 구독 등급 및 로열티 상태에 따라 개인화된 프로모션 및 인센티브를 표시합니다. |
| 신규 사용자 참여 타겟팅 | 신규 사용자를 온보딩 흐름 및 계정 설정으로 안내합니다. |
| 세일 및 프로모션 | 사용자 경험을 방해하지 않으면서 홈페이지에서 지속적이고 직접적으로 추천 콘텐츠, 인기 제품 및 진행 중인 브랜드 Campaign을 강조합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="배너를 사용하는 이유는 무엇인가요?" }

## 기능 {#features}

배너의 기능은 다음과 같습니다:

- **쉬운 콘텐츠 구축:** 이미지, 텍스트, 버튼, 이메일 캡처 양식, 커스텀 코드 등을 지원하는 시각적 드래그 앤 드롭 편집기를 사용하여 배너를 생성하고 미리보기할 수 있습니다. 자체 마크업을 관리하려는 팀은 배너의 HTML과 스타일을 완전히 제어할 수 있는 HTML 편집기를 대신 사용하거나, [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-messages)에 설명을 입력하여 HTML을 생성할 수 있습니다.
- **유연한 배치:** 배너가 나타날 수 있는 애플리케이션 또는 웹사이트 내 여러 위치를 정의하여 특정 컨텍스트나 사용자 경험에 대한 정밀한 타겟팅을 가능하게 합니다.
- **동적 개인화:** 배너는 새로고침될 때마다 개인화(Liquid 로직)와 세분화를 다시 계산합니다. 사용자가 프로필을 업데이트하거나 커스텀 속성이 변경되면, 다음 배너 새로고침 시 해당 변경 사항이 반영됩니다.
- **네이티브 우선순위:** 여러 배너가 동일한 배치를 타겟팅할 때 표시 우선순위를 설정하여 올바른 메시지가 적시에 사용자에게 전달되도록 합니다.
- **커스텀 코드 편집기 블록:** 커스텀 코드 편집기 블록을 사용하여 고급 커스터마이징을 위한 커스텀 HTML을 추가하거나 기존 웹 스타일과 원활하게 통합할 수 있습니다.

## 배너에 대하여 {#about-banners}

### 배치 ID {#placement-id}

배너 배치는 [Braze SDK로 생성한]({{site.baseurl}}/developer_guide/banners/placements) 앱 또는 웹사이트의 특정 위치로, 배너가 나타날 수 있는 위치를 지정합니다.

일반적인 위치에는 홈페이지 상단, 제품 상세 페이지 및 체크아웃 흐름이 포함됩니다. 배치가 생성된 후, 배너는 [배너 Campaign에서 할당]({{site.baseurl}}/user_guide/channels/banners/create_a_banner)할 수 있습니다.

워크스페이스당 생성할 수 있는 배치 수에 대한 고정 제한은 없으며, 경험에 따라 필요한 만큼 많은 배치 ID를 생성할 수 있습니다. 각 배치는 워크스페이스 내에서 고유해야 합니다. 단일 배치 ID는 동시에 최대 25개의 활성 메시지에서 참조될 수 있습니다.

{% alert important %}
배너 Campaign을 시작한 후에는 배치 ID를 수정하지 마세요.
{% endalert %}

### 배너 우선순위 {#priority}

여러 배너 메시지가 동일한 배치 ID를 참조할 때, 배너는 우선순위에 따라 표시됩니다: 높음, 중간 또는 낮음. 기본적으로 배너는 중간으로 설정되지만, 배너 Campaign을 생성하거나 편집할 때 [우선순위를 수동으로 설정]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#set-banner-priority-optional)할 수 있습니다.

여러 배너가 동일한 우선순위로 설정된 경우, 사용자가 자격이 있는 가장 최신 배너가 먼저 표시됩니다.

### 배치 요청 {#requests}

{% multi_lang_include banners/placement_requests.md %}

### 메시지 전달 {#message-delivery}

배너 메시지는 HTML 콘텐츠로 앱 또는 웹사이트에 전달되며, 일반적으로 iframe 내에서 렌더링됩니다. 이를 통해 배너가 기기 전반에 걸쳐 일관되게 렌더링되며, 나머지 코드와 스타일 및 스크립트를 분리하는 데 도움이 됩니다.

iframe은 코드베이스 변경 없이 동적이고 개인화된 콘텐츠 업데이트를 가능하게 합니다. 각 iframe은 Campaign 타겟팅 및 개인화 로직을 사용하여 각 사용자 세션에 대한 HTML을 검색하고 표시합니다.

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}

### 크기 및 사이징 {#dimensions-and-sizing}

배너 크기 및 사이징에 대해 알아야 할 사항은 다음과 같습니다:

- 컴포저를 사용하면 배너를 다양한 크기로 미리보기할 수 있지만, 해당 정보는 SDK에 저장되거나 전송되지 않습니다.
- HTML은 렌더링되는 컨테이너의 전체 너비를 차지합니다.
- 고정된 크기의 요소를 만들고 컴포저에서 해당 크기를 테스트하는 것을 권장합니다.

## 제한 사항 {#limitations}

각 워크스페이스는 최대 200개의 활성 배너 Campaign을 지원할 수 있습니다. 이 한도에 도달하면 새 Campaign을 만들기 전에 기존 Campaign을 [아카이브하거나 비활성화]({{site.baseurl}}/user_guide/messaging/governance/statuses#changing-the-status)해야 합니다.

또한, 배너 메시지는 다음 기능을 지원하지 않습니다:

- API 트리거 및 액션 기반 Campaigns
- 연결된 콘텐츠
- 프로모션 코드
- [`:rerender` 태그]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs#using-liquid)를 사용하는 `catalog_items`

## 다음 단계 {#next-steps}

- [앱이나 웹사이트에 배너 배치 만들기]({{site.baseurl}}/developer_guide/banners/placements)
- [Braze에서 배너 Campaign 만들기]({{site.baseurl}}/user_guide/channels/banners/create_a_banner)
- [튜토리얼: 배치 ID로 배너 표시하기]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)

{% alert tip %}
다음 우선순위를 정하는 데 도움을 주고 싶으신가요? [banners-feedback@braze.com](mailto:banners-feedback@braze.com)으로 문의하세요.
{% endalert %}