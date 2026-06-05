---
nav_title: 워크스페이스 생성 및 관리
article_title: 워크스페이스 생성 및 관리
page_order: 0
layout: dev_guide
guide_top_header: "워크스페이스 생성 및 관리"
guide_top_text: "이 문서에서는 워크스페이스를 생성, 설정 및 관리하는 방법을 다룹니다."
page_type: reference
description: "이 문서에서는 워크스페이스를 생성, 설정 및 관리하는 방법을 다룹니다."

guide_featured_title: "섹션 문서"
guide_featured_list:
- name: 워크스페이스 간 데이터 마이그레이션
  link: /docs/user_guide/administer/global/create_and_manage_workspaces/migrate_workspace_data
  image: /assets/img/braze_icons/switch-horizontal-01.svg
---

<br>

# 워크스페이스 생성 및 관리 {#create-and-manage-workspaces}

> 이 문서에서는 워크스페이스를 생성, 설정 및 관리하는 방법을 다룹니다.

## 워크스페이스란? {#what-is-a-workspace}

Braze에서 하는 모든 작업은 워크스페이스 내에서 이루어집니다. 워크스페이스는 관련 모바일 앱이나 웹사이트의 참여를 추적하고 관리하기 위한 공유 환경입니다. 워크스페이스는 동일하거나 매우 유사한 앱을 함께 그룹화합니다. 예를 들어, 모바일 앱의 Android 버전과 iOS 버전을 하나의 워크스페이스에 묶을 수 있습니다.

## 워크스페이스 생성 {#creating-a-workspace}

### 1단계: 계획 수립 {#step-1-have-a-plan}

시작하기 전에 팀 및 Braze 온보딩 매니저와 함께 사용 사례에 가장 적합한 워크스페이스 구성을 결정하세요. Braze에서 워크스페이스를 계획하는 방법에 대해 자세히 알아보려면 [시작하기: 워크스페이스]({{site.baseurl}}/user_guide/get_started/workspaces/) 가이드를 확인하세요.

### 2단계: 워크스페이스 추가 {#step-2-add-your-workspace}

글로벌 헤더의 워크스페이스 드롭다운에서 새 워크스페이스를 생성하거나 기존 워크스페이스 간에 전환할 수 있습니다.

1. 워크스페이스 드롭다운을 선택한 다음 <i class="fa-solid fa-square-plus" style="color: #0b8294;"></i> **Create workspace**를 선택합니다.

![워크스페이스 생성 버튼이 있는 워크스페이스 드롭다운.]({% image_buster /assets/img/workspaces/workspace_create.png %}){: style="max-width:60%;"}

{:start="2"}
2. 워크스페이스에 이름을 지정합니다.

{% alert tip %}
회사 내 다른 사람들이 워크스페이스를 쉽게 찾을 수 있도록 명명 규칙을 채택하는 것이 좋습니다. 예: "Upon Voyage US – Production" 및 "Upon Voyage US – Staging".
{% endalert %}

{:start="3"}
3. **Create**를 선택합니다. Braze가 워크스페이스를 생성하는 데 몇 초가 걸릴 수 있습니다.

!["Upon Voyage US - Staging"이라는 이름이 입력된 "Create Workspace" 모달.]({% image_buster /assets/img/workspaces/workspace_name.png %}){: style="max-width:60%" }

앱 인스턴스를 추가할 수 있는 **App Settings** 페이지로 이동합니다. 이 페이지는 **Settings** > **App Settings**에서 언제든지 접근할 수 있습니다.

![앱 추가 버튼이 있는 Upon Voyage US - Staging 워크스페이스의 "App Settings" 페이지.]({% image_buster /assets/img/workspaces/workspace_empty_state.png %})

### 3단계: 앱 인스턴스 추가 {#step-3-add-your-app-instances}

워크스페이스 내에 수집되는 다양한 사이트와 앱을 "앱 인스턴스"라고 합니다.

1. **App Settings** 페이지에서 **+ Add app**을 선택합니다.
2. 앱 인스턴스에 이름을 지정하고 이 앱 인스턴스가 사용하는 플랫폼을 선택합니다. 여러 플랫폼을 선택하면 Braze가 각 플랫폼에 대해 하나의 앱 인스턴스를 생성합니다.

![앱 세부 정보를 선택할 수 있는 옵션이 있는 "Add New App to Upon Voyage US - Staging" 모달.]({% image_buster /assets/img/workspaces/workspace_add_app.png %}){: style="max-width:60%" }

{:start="3"}
3. **Add app**을 선택하여 확인합니다.

#### 앱 API 키 {#app-api-keys}

앱 인스턴스를 추가하면 해당 API 키에 접근할 수 있습니다. API 키는 앱 인스턴스와 Braze API 간의 요청을 수행할 때 사용됩니다. API 키는 Braze SDK를 앱이나 웹사이트에 통합하는 데에도 중요합니다.

![API Key 및 SDK Endpoint 필드가 있는 Upon Voyage iOS 앱의 설정 페이지.]({% image_buster /assets/img/workspaces/app_api_key.png %})

{% alert note %}
각 플랫폼의 앱 버전마다 별도의 앱 인스턴스를 생성해야 합니다. 예를 들어, iOS와 Android 모두에서 무료 버전과 프로 버전의 앱이 있는 경우 워크스페이스 내에 네 개의 앱 인스턴스(무료 iOS 앱, 무료 Android 앱, 프로 iOS 앱, 프로 Android 앱)를 생성합니다. 이렇게 하면 각 앱 인스턴스에 대해 하나씩 네 개의 API 키를 사용할 수 있습니다.
{% endalert %}

#### 라이브 SDK 버전 {#live-sdk-version}

특정 앱의 App Settings 페이지에 표시되는 라이브 SDK 버전은 전체 일일 세션의 5% 이상을 차지하고 지난 하루 동안 500회 이상의 세션이 있는 가장 높은 앱 버전입니다.

이 필드는 Braze SDK를 앱이나 웹사이트에 통합한 후에 나타납니다. 해당 플랫폼에 더 새로운 버전의 Braze SDK가 있는 경우 "Newer Version Available" 태그와 함께 여기에 표시됩니다.

![필드 값이 "5.4.0"이고 새 버전이 사용 가능하다는 아이콘이 있는 "Live SDK Version" 섹션.]({% image_buster /assets/img/workspaces/app_live_sdk_version.png %})

### 4단계: 필요에 따라 반복 {#step-4-repeat-as-needed}

계획에 필요한 만큼 워크스페이스를 설정하려면 2단계와 3단계를 반복합니다. 모범 사례로, 통합 및 Campaign 테스트를 위한 테스트 워크스페이스를 생성하는 것을 권장합니다.

{% alert tip %}
**테스트 워크스페이스 추가**<br>특정 사용자를 프로덕션 인스턴스에서 완전히 격리하여 앱 테스트를 수행할 수 있습니다. 새 워크스페이스를 생성하고, 애플리케이션을 게시할 때 Braze가 사용하는 API 키를 테스트 워크스페이스가 아닌 프로덕션 워크스페이스의 API 키로 변경하세요.
{% endalert %}

## 워크스페이스 관리 {#managing-workspaces}

### 즐겨찾기 추가 {#adding-favorites}

자주 사용하는 워크스페이스를 즐겨찾기에 추가하여 더 빠르게 접근할 수 있습니다.

!["Favorite workspaces" 탭이 있는 워크스페이스 드롭다운.]({% image_buster /assets/img/workspaces/workspace_favorites.png %}){: style="max-width:50%;"}

워크스페이스를 즐겨찾기에 추가하려면:

1. 프로필 드롭다운을 선택한 다음 **Manage your account**를 선택합니다.
2. **Account Profile** 섹션에서 **Favorite workspaces** 필드를 찾습니다.
3. 목록에서 워크스페이스를 선택합니다.
4. **Save changes**를 선택합니다.

즐겨찾기에 추가할 수 있는 워크스페이스 수에는 제한이 없지만, 편의를 위해 목록을 짧게 유지하는 것을 권장합니다.

### 워크스페이스 이름 변경 {#renaming-workspaces}

워크스페이스 이름을 변경하려면:

1. **Settings** > **App Settings**으로 이동합니다.
2. 워크스페이스 이름 위에 마우스를 올리고 <i class="fa-solid fa-pencil" style="color: #0b8294;"></i>을 선택합니다.
3. 워크스페이스에 새 이름을 지정한 다음 <i class="fa-solid fa-square-check" style="color: #0b8294;"></i> **Save**를 선택합니다.

![워크스페이스 이름 옆에 나타나는 연필 아이콘.]({% image_buster /assets/img/workspaces/workspace_rename.gif %}){: style="max-width:50%;"}

### 워크스페이스 및 앱 인스턴스 삭제 {#deleting-workspaces-and-app-instances}

워크스페이스 또는 앱 인스턴스를 삭제하려면:

1. **Settings** > **App Settings**으로 이동합니다.
2. 해당 워크스페이스를 삭제하려면 **Delete workspace**를 선택하거나, 해당 앱 인스턴스 옆의 휴지통 아이콘을 선택합니다.

현재 사용자 타겟팅에 사용 중이거나 1,000명 이상의 사용자가 있는 앱 인스턴스 또는 워크스페이스는 삭제할 수 없습니다. 삭제를 시도하면 오류 메시지가 표시됩니다. 삭제를 진행하려면 대시보드 링크와 삭제할 앱 인스턴스 또는 워크스페이스 이름을 포함하여 [고객지원 케이스를 생성]({{site.baseurl}}/user_guide/administer/personal/braze_support/)하세요.

{% alert warning %}
워크스페이스를 삭제할 때 주의하세요! 워크스페이스가 삭제되면 복원할 수 없습니다.
{% endalert %}

![워크스페이스 삭제 버튼과 앱 삭제를 위한 휴지통 아이콘이 있는 App Settings 페이지.]({% image_buster /assets/img/workspaces/workspace_delete.png %})

## 자주 묻는 질문 {#frequently-asked-questions}

### 업데이트된 앱을 출시할 때 새 워크스페이스를 생성해야 하나요? {#should-i-create-a-new-workspace-when-im-releasing-an-updated-app}

앱을 업데이트하는 것인지 완전히 새로운 앱을 만드는 것인지에 따라 다릅니다.

#### 앱 업데이트 {#updating-your-app}

앱을 업데이트하는 경우, 동일한 워크스페이스 내에 새 앱 인스턴스를 생성하여 이전 버전과 새 버전을 분리해야 합니다. 이렇게 하면 세분화 시 해당 앱을 선택하여 새 버전의 사용자를 효과적으로 타겟팅할 수 있습니다. 이전 버전의 사용자에게 메시지를 보내려면 필터를 사용하여 [이전 앱 버전을 타겟팅]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions)할 수 있습니다.

새 워크스페이스를 생성하면 사용자가 이전 워크스페이스와 새 워크스페이스 두 곳에 존재하게 됩니다. 또한 동일한 푸시 토큰을 가질 수도 있습니다. 이로 인해 이미 업그레이드한 사용자가 이전 워크스페이스 사용자만을 대상으로 한 마케팅 메시지를 받을 수 있습니다.

#### 새 앱 출시 {#releasing-a-new-app}

완전히 새로운 앱을 앱 스토어에 출시하는 경우, 새 워크스페이스를 생성해야 합니다. 새 워크스페이스를 생성하면 이전 앱 버전의 모든 과거 데이터와 고객 프로필이 이 새 워크스페이스에 존재하지 않습니다. 따라서 기존 사용자가 새 앱 버전으로 업그레이드하면 이전 앱의 행동 데이터 없이 새 프로필이 생성됩니다.

### 하나의 워크스페이스에 여러 앱 인스턴스가 있는 경우, 메시지를 단일 앱에만 타겟팅하려면 어떻게 해야 하나요? {#singular-app}

메시지가 특정 앱만 타겟팅하도록 하려면 선택한 앱 인스턴스의 사용자만 타겟팅하는 Segment를 추가하세요. 이는 사용자가 동일한 워크스페이스 내의 서로 다른 앱 인스턴스에 대해 두 개의 푸시 토큰을 가질 수 있는 경우 특히 중요합니다. 이 시나리오에서는 사용자가 현재 사용 중인 앱이 아닌 다른 앱에 대한 알림을 받을 수 있습니다. 이상적인 경험이 아닙니다!

기본적으로 Segment는 워크스페이스의 모든 앱과 웹사이트를 타겟팅합니다. 하나의 앱이나 웹사이트만 타겟팅하는 Segment를 설정하려면:

1. 의미 있는 이름으로 Segment를 생성합니다. Braze에서는 "All Users ({이름} {플랫폼})" 형식을 사용합니다. 예: "All Users (Upon Voyage iOS)".
2. **Apps and websites targeted**에서 **Users from specific apps**를 선택합니다.
3. **Specific apps** 드롭다운에서 앱이나 사이트를 선택합니다.

![특정 앱의 사용자를 타겟팅하는 Segment.]({% image_buster /assets/img/workspaces/users_from_specific_apps_filter.png %})

그런 다음 이 Segment를 메시지에 추가하고 필요에 따라 추가 Segment 및 필터로 오디언스를 더 세분화할 수 있습니다.

#### Campaigns

Campaigns의 경우, 작성기의 **Target Audiences** 단계에서 Segment를 추가합니다.

#### Canvas

Canvas에서는 메시지 단계의 **Delivery Validations** 섹션에서 Segment를 추가합니다. 전달 유효성 검사는 메시지 전송 시 오디언스가 전달 기준을 충족하는지 다시 한번 확인합니다. 올바른 앱에 전달되도록 각 메시지 단계에 대해 전달 유효성 검사를 지정하세요. 진입 수준에서 세분화할 필요는 없습니다.

{% details 기존 Canvas 워크플로의 단계를 보려면 펼치기 %}

기존 Canvas 워크플로에서는 **Audience** 섹션의 Canvas 구성요소 수준에서 Segment를 추가합니다. 진입 수준에서 세분화할 필요는 없습니다.

{% enddetails %}

## 다음 단계 {#next-steps}

워크스페이스를 생성한 후 다음을 구성하세요:

- [워크스페이스 설정]({{site.baseurl}}/user_guide/administer/global/workspace_settings/)에서 API 키, 이메일 환경설정, 푸시 설정 등을 설정합니다.
- [회사 사용자 관리]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users/)에서 이 워크스페이스에 사용자를 추가하고 권한을 할당합니다.