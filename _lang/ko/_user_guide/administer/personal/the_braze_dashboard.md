---
nav_title: 대시보드
article_title: Braze 대시보드
page_order: 1
page_type: reference
description: "Braze 대시보드는 고객 참여를 구축, 관리, 분석하기 위한 중앙 워크스페이스입니다. 메시징 도구, 오디언스 인사이트, 세분화, 실시간 성과 데이터를 한곳에서 제공합니다."

---

# Braze 대시보드 {#the-braze-dashboard}

> Braze 대시보드는 고객 참여를 구축, 관리, 분석하기 위한 중앙 워크스페이스입니다. [dashboard.braze.com](https://dashboard.braze.com/) 또는 [dashboard.braze.eu](https://dashboard.braze.eu/)에서 접속할 수 있습니다.

Braze 대시보드를 사용하여 Campaign을 계획하고, 메시지를 시작 및 관리하고, 오디언스 인사이트를 탐색하고, 세분화를 조정하고, 실시간 성과 및 참여 측정기준을 단일 인터페이스에서 검토할 수 있습니다.

## 대시보드 개요 {#dashboard-overview}

로그인하면 대시보드에서 참여 툴과 데이터를 중앙 집중식으로 확인할 수 있습니다.

- **홈 페이지:** [최근 편집한 콘텐츠](#pick-up-where-you-left-off)와 주요 성과 측정기준을 한눈에 보여줍니다
- **왼쪽 내비게이션:** 기능별로 도구를 정리합니다(메시징, 오디언스, 분석, 설정)
- **글로벌 헤더:** 검색, 고객지원, 언어 설정, 알림, 계정에 빠르게 접근할 수 있습니다

대시보드 환경은 [워크스페이스]({{site.baseurl}}/user_guide/get_started/workspaces)별로 구성되어 있으며, 다양한 브랜드, 지역 또는 팀의 콘텐츠를 관리하는 데 도움이 됩니다. 사이드 내비게이션에서 언제든지 [워크스페이스를 전환](#workspace-switcher)할 수 있습니다.

## 대시보드에 접속하기 {#access-your-dashboard}

시작하려면 [Braze 계정에 로그인]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account)하세요. 대시보드 내 페이지에 대한 접근 권한과 특정 작업 수행 권한은 할당된 [사용자 권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions)에 따라 결정됩니다. 권한에 대해 도움이 필요하면 Braze 관리자에게 문의하세요.

## Braze 내비게이션 {#navigate-braze}

Braze 내비게이션은 다양한 기기에서 기능과 콘텐츠에 효율적으로 접근할 수 있도록 설계되었습니다. Braze 대시보드에는 글로벌 헤더와 사이드 내비게이션, 두 가지 수준의 내비게이션이 있습니다.

글로벌 헤더는 거의 항상 화면 상단에 표시됩니다. 다음을 포함한 필수 도구와 설정에 빠르게 접근할 수 있습니다.

- [검색](#search-your-dashboard)
- 고객지원 및 커뮤니티 링크
- [대시보드 언어]({{site.baseurl}}/user_guide/administer/personal/language_settings)
- 알림
- 계정 설정
- [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator)

### 사이드 내비게이션 사용하기 {#use-the-side-navigation}

왼쪽의 세로 메뉴는 Braze 도구를 기능별로 정리하고 자주 사용하는 항목을 쉽게 접근할 수 있도록 합니다. 메인 메뉴 항목을 선택하면 세로 레이아웃으로 옵션이 표시됩니다.

![Braze 대시보드의 워크스페이스 전환기]({% image_buster /assets/img/workspace_switcher.png %}){: style="max-width:35%;float:right;margin-left:15px"}

#### 워크스페이스 전환기 {#workspace-switcher}

사이드 내비게이션 상단에 위치한 워크스페이스 전환기를 사용하면 Braze 인스턴스 내의 다른 워크스페이스로 이동할 수 있습니다. 활성 워크스페이스가 강조 표시됩니다.

[워크스페이스]({{site.baseurl}}/user_guide/get_started/workspaces)는 브랜드, 지역, 제품 라인 또는 팀별로 콘텐츠를 정리하는 데 도움이 됩니다. 각 워크스페이스에는 자체 데이터, Campaigns, 설정이 포함됩니다. 워크스페이스마다 접근 권한이 다를 수 있습니다. 예를 들어, 한 워크스페이스에서는 편집 권한이 있고 다른 워크스페이스에서는 보기 전용 권한만 있을 수 있습니다.

워크스페이스를 전환하려면 사이드 내비게이션 상단의 워크스페이스 드롭다운을 선택하고 접근하려는 워크스페이스를 선택합니다. 자주 사용하는 워크스페이스에 더 빠르게 접근하려면 [워크스페이스 즐겨찾기](#favorite-workspaces)를 추가할 수도 있습니다.

#### 사이드 내비게이션 최소화 {#minimize-the-side-navigation}

Canvas 디자인과 같은 작업 중 시각적 혼잡을 줄이려면 사이드 내비게이션 패널을 최소화할 수 있습니다. **메뉴 최소화**를 눌러 접으세요. 최소화된 상태에서도 아이콘 위에 마우스를 올리면 메뉴 항목 이름이 포함된 툴팁을 볼 수 있습니다. 이를 통해 워크스페이스를 깔끔하게 유지하면서 도구 간에 빠르게 이동할 수 있습니다.

![메뉴 최소화 및 확대 아이콘]({% image_buster /assets/img/minimize_expand_menu.png %}){: style="max-width:60%;border:none"}

#### 반응형 내비게이션 {#responsive-navigation}

내비게이션은 다양한 화면 크기에 원활하게 적응합니다. 작은 화면에서는 사이드 내비게이션이 자동으로 접힙니다. 필요할 때 <i class="fa-solid fa-bars" aria-label="탐색 메뉴 열기"></i>를 눌러 메뉴를 열 수 있습니다.

![작은 화면에서는 사이드 내비게이션이 자동으로 접힙니다. 메뉴 아이콘을 탭하면 내비게이션 옵션이 열립니다.]({% image_buster /assets/img/navigation/navigation_small_screens.png %}){: style="max-width: 80%;border:none"}

## 대시보드 검색 {#search-your-dashboard}

헤더에 위치한 글로벌 검색 바는 Braze 대시보드 전체에서 콘텐츠를 찾는 가장 빠른 방법입니다. 선택하여 검색 인터페이스를 열고 필요한 항목으로 바로 이동하세요.

![검색어가 입력되지 않은 상태의 글로벌 검색, 최근 열어본 페이지가 표시됩니다.]({% image_buster /assets/img/navigation/search_recently_opened.png %})

최근 열어본 콘텐츠가 검색 바 아래에 표시됩니다. 여기에는 최근 상호작용한 Campaign, Canvas, 템플릿 또는 페이지가 포함되어 있어 작업으로 쉽게 돌아갈 수 있습니다.

### 무엇을 검색할 수 있나요? {#what-can-you-search-for}

다음 항목과 작업을 검색할 수 있습니다.

- Campaign 이름
- Canvas 이름
- Content Blocks
- Segment 이름
- 이메일 템플릿 이름
- Braze 내 페이지(동의어 포함)

{% alert tip %}
정확한 텍스트를 검색하려면 검색어를 따옴표로 묶으세요(""). 예를 들어, ["all users"]를 검색하면 이름에 "all users"라는 정확한 문구가 포함된 모든 항목이 반환됩니다.
{% endalert %}

### 콘텐츠 유형 및 상태 태그 {#content-type-and-status-tags}

각 결과에는 콘텐츠 유형(Campaign, Canvas, Segment 등)과 상태(활성, 아카이브됨, 중지됨)를 나타내는 태그가 표시됩니다.

### 활성 및 초안 콘텐츠 필터링 {#filter-for-active-and-draft-content}

기본적으로 검색에는 활성, 초안, 아카이브된 항목이 포함됩니다. **Show active and draft only** 토글을 사용하여 결과를 좁힐 수 있습니다.

!["Show active and draft only" 토글.]({% image_buster /assets/img/navigation/show_active_draft_new.png %})

### 키보드 단축키 {#keyboard-shortcuts}

키보드를 사용하여 검색 결과를 탐색할 수 있습니다.

<style>
  div.small_table + table {
    max-width: 60%;
  }
table th:nth-child(1),
table th:nth-child(2),
table td:nth-child(1),
table td:nth-child(2) {
    width:20%;
}
table td {
    word-break: break-word;
}
</style>

<div class="small_table"></div>

| 동작 | 키보드 단축키 |
| --- | --- |
| 검색 메뉴 열기 | {::nomarkdown} <ul> <li> Mac: <kbd>⌘</kbd>&nbsp;+&nbsp;<kbd>K</kbd> </li> <li>Windows: <kbd>Ctrl</kbd>&nbsp;+&nbsp;<kbd>K</kbd> </li> </ul> {:/} |
| 검색 결과 간 이동 | <kbd>⬆</kbd> / <kbd>⬇</kbd> |
| 검색 결과 선택 | <kbd>Enter</kbd> |
| 검색 메뉴 닫기 | <kbd>Esc</kbd> |
{: .reset-td-br-1 .reset-td-br-2 aria-label="키보드 단축키" }

## 생산성 기능 {#productivity-features}

Braze 대시보드에는 더 효율적으로 작업하고 자주 사용하는 도구와 콘텐츠에 빠르게 접근할 수 있도록 돕는 여러 기능이 포함되어 있습니다.

### BrazeAI Operator

BrazeAI Operator™는 대시보드에 내장된 AI 기반 어시스턴트입니다. 답변을 얻고, 설정을 안내받고, 문제를 해결하고, 아이디어를 브레인스토밍하는 데 사용할 수 있습니다. 프로필 옆 글로벌 헤더의 **BrazeAI Operator™**에서 열 수 있습니다. 자세한 내용은 [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator)를 참조하세요.

### 이전 작업 이어하기 {#pick-up-where-you-left-off}

**Home** 페이지에서 대시보드는 최근 편집하거나 생성한 Campaigns, Canvases, Segments를 표시합니다. 이를 통해 검색 없이도 진행 중인 작업으로 쉽게 돌아갈 수 있습니다. 각 항목에는 콘텐츠 유형과 상태(초안, 활성, 중지됨 등)를 나타내는 태그가 포함되어 있습니다.

![Canvas 초안, 활성 Segment, Campaign 초안이 "이전 작업 이어하기" 섹션에 표시됩니다.]({% image_buster /assets/img/pick_up_where_you_left_off.png %})

자세한 내용은 [홈 대시보드]({{site.baseurl}}/user_guide/analytics/dashboards/home#pick-up-where-you-left-off)를 참조하세요.

### 워크스페이스 즐겨찾기 {#favorite-workspaces}

여러 워크스페이스에서 작업하는 경우 자주 사용하는 워크스페이스를 즐겨찾기로 표시할 수 있습니다. 즐겨찾기 워크스페이스는 워크스페이스 전환기 상단에 표시되어 더 빠르게 접근할 수 있습니다.

워크스페이스 즐겨찾기를 추가하려면:

1. [프로필 설정에 접근합니다](#access-your-profile-settings).
2. **계정 프로필** 섹션에서 **워크스페이스 즐겨찾기** 필드를 찾습니다.
3. 즐겨찾기로 설정할 워크스페이스를 선택합니다.

### 프로필 설정에 접근하기 {#access-your-profile-settings}

계정 설정, 알림 환경설정, 개인 정보를 관리하려면:

1. 글로벌 헤더에서 프로필 아이콘을 선택합니다.
2. **내 계정 관리**를 선택하여 프로필 페이지에 접근합니다.

프로필 페이지에서 이메일 설정을 업데이트하고, 2단계 인증을 구성하고, API 키를 확인하고, 기타 계정 세부 정보를 관리할 수 있습니다.

## 대시보드의 접근성 {#accessibility-in-the-dashboard}

Braze 대시보드는 WCAG AA 표준의 색상 대비를 충족하는 브랜드 색상을 사용합니다. 이를 통해 모든 사용자에게 포용적인 경험을 지원하고 접근성 모범 사례에 부합합니다.

## 피드백 공유 {#sharing-feedback}

의견을 알려주고 싶으신가요? 내비게이션, 접근성, 사용성, 시각 디자인 등에 대한 피드백을 공유할 수 있습니다. 글로벌 헤더에서 **Support** 메뉴를 열고 **Share feedback**을 선택하세요. 모든 피드백을 검토하여 Braze 경험을 개선하는 데 활용합니다.

## 관련 리소스 {#related-resources}

### 관리 작업 {#administrative-tasks}

- [워크스페이스 생성 및 관리]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces)
- [Braze 사용자 관리]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users)
- [사용자 권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)
- [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams)

### 주요 작업 및 다음 단계 {#key-tasks-and-next-steps}

- **Campaign 구축**: [Campaign 생성]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign)
- **여정 만들기**: [Canvas 구축]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)
- **오디언스 정의**: [Segment 생성]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)
- **성과 검토**: [분석 개요]({{site.baseurl}}/user_guide/analytics/dashboards/home)
- **설정 구성**: [앱 설정]({{site.baseurl}}/user_guide/administer/global/workspace_settings)