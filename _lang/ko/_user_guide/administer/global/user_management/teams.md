---
nav_title: Teams
article_title: Teams
page_order: 2
page_type: reference
alias: /teams/
description: "이 참조 문서에서는 대시보드에서 Braze Teams를 사용하는 방법을 다룹니다. Teams를 생성하고, 역할을 할당하고, 태그와 필터를 할당하는 방법을 알아볼 수 있습니다."

---

# Teams {#teams}

> Braze 관리자는 다양한 사용자 역할과 권한을 가진 Teams로 회사 사용자를 그룹화할 수 있습니다. 이를 통해 편집할 수 있는 콘텐츠 유형을 분리하여 하나의 워크스페이스에서 여러 개의 관련 없는 회사 사용자 그룹이 함께 작업할 수 있습니다.

Teams는 고객 기반 위치, 언어, 커스텀 속성에 따라 설정할 수 있으므로 Teams 멤버와 비멤버가 메시징 기능과 고객 데이터에 대해 서로 다른 접근 권한을 가질 수 있습니다. 다양한 참여 툴에서 Teams 필터와 태그를 할당할 수 있습니다. 워크스페이스에서 생성할 수 있는 Teams 수에는 제한이 없습니다.

모든 Braze 계약에서 Teams를 사용할 수 있는 것은 아닙니다. 이 기능에 접근하려면 Braze 계정 매니저에게 문의하거나 [저희에게 연락하세요](mailto:success@braze.com).

## Teams은 권한 세트 및 역할과 어떻게 다른가요? {#how-do-teams-differ-from-permission-sets-and-roles}

{% multi_lang_include permissions/differences.md content="Differences" %}

## Teams 생성 {#creating-teams}

**설정** > **내부 팀**으로 이동하여 <i class="fas fa-plus"></i> **팀 추가**를 선택합니다.

![새 팀을 추가하는 창.]({% image_buster /assets/img_archive/adding_a_team.png %})

**팀 이름**을 입력합니다. 원하는 경우 **팀 정의(선택 사항)** 필드를 사용하여 커스텀 속성, 위치 또는 언어를 선택하여 Teams가 접근할 수 있는 사용자 데이터를 추가로 정의할 수 있습니다. 예를 들어, 가능한 사용 사례는 커스텀 속성으로 식별되는 테스트 사용자에게만 접근할 수 있는 개발 Teams를 생성하여 [Teams로 테스트](#test-with-teams)를 수행하는 것입니다. 또 다른 사용 사례는 제품에 따라 사용자와의 커뮤니케이션을 제한하는 것입니다.

Teams가 커스텀 속성, 언어 또는 국가로 정의된 경우, 해당 Teams를 사용하여 Campaigns, Canvases, Content Cards, Segments 등의 기능에 대해 최종 사용자를 필터링할 수 있습니다. 자세한 내용은 [Teams 태그 할당](#tags-and-filters)을 참조하세요.

## Teams에 사용자 할당 {#assign-users-to-teams}

Braze 관리자 및 "회사 설정 관리 가능" 회사 수준 권한을 가진 제한된 사용자는 제한된 액세스 권한을 가진 회사 사용자에게 팀 수준 권한을 할당할 수 있습니다. 팀에 할당되면 회사 사용자는 팀이 생성될 때 정의된 사용자 언어, 위치 또는 커스텀 속성과 같이 해당 팀에서 사용할 수 있는 데이터만 읽거나 쓸 수 있도록 제한됩니다.

### 사용자를 삭제하지 않고 회사 사용자 권한 제한 {#limit-company-user-permissions-without-deleting-a-user}

회사 사용자의 계정을 유지하면서 로그인을 중지하려면 사용자를 삭제하는 대신 [사용자를 일시 중지]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users#suspending-company-users)하세요. 일시 중지하면 계정이 비활성 상태가 되어 사용자가 로그인할 수 없습니다.

사용자가 제한된 기능으로 계속 로그인할 수 있어야 하는 경우, **설정** > **회사 사용자**로 이동하여 사용자를 선택하고 권한을 편집하세요. Campaigns, Canvases, Segments 및 사용자 데이터에 대한 워크스페이스 수준 권한을 제거하고 최소한의 액세스만 남겨두세요(예: "미디어 라이브러리 에셋 보기"). 자세한 내용은 [사용자 권한 편집]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#edit-a-users-permissions)을 참조하세요.

팀 권한은 워크스페이스 권한 위에서 작동합니다. 사용자를 팀에 할당하는 경우, 필요한 최소한의 팀 수준 권한만 부여하고 Campaigns, Canvases, Segments 또는 고객 프로필에 대한 권한은 부여하지 마세요. 사용자는 워크스페이스에 남아 있고 로그인할 수 있지만, 대부분의 메시징 또는 오디언스 작업을 수행할 수 없습니다.

사용자를 팀에 할당하려면 **설정** > **회사 사용자**로 이동하여 팀에 추가할 사용자를 선택하세요.

그런 다음 다음 단계를 수행하세요:

1. **워크스페이스 수준 권한** 섹션에서 사용자가 아직 포함되어 있지 않은 경우 적절한 워크스페이스에 추가하세요.

![배너 템플릿 권한이 설정된 워크스페이스 수준 권한.]({% image_buster /assets/img/team_level_permissions.png %})

{: start="2"}
2. **+ 팀 수준 권한 추가**를 선택한 다음, 이 사용자를 추가할 **팀**을 선택하세요.
3. **팀** 권한 섹션에서 특정 권한을 할당하세요.

![팀 수준 랜딩 페이지 템플릿 권한.]({% image_buster /assets/img/teams.png %})

### 사용 가능한 팀 수준 권한 {#available-team-level-permissions}

다음은 팀 수준에서 할당할 수 있는 모든 사용 가능한 권한입니다. 여기에 나열되지 않은 권한은 워크스페이스 수준에서만 부여되며, 이러한 권한은 **Teams** 권한 열에 "--"로 표시됩니다.

- Campaigns 보기
- Campaigns 편집
- Campaigns 보관
- Campaigns 실행
- Campaigns 승인
- Canvases 보기
- Canvases 편집
- Canvases 보관
- Canvases 실행
- Canvases 승인
- Content Blocks 보기
- Content Blocks 편집
- Content Blocks 보관
- Content Blocks 실행
- Segments 보기
- Segments 편집
- Segments 보관
- IAM 템플릿 보기
- IAM 템플릿 편집
- IAM 템플릿 보관
- 이메일 템플릿 보기
- 이메일 템플릿 편집
- 이메일 템플릿 보관
- 웹훅 템플릿 보기
- 웹훅 템플릿 편집
- 웹훅 템플릿 보관
- 이메일 링크 템플릿 보기
- 이메일 링크 템플릿 편집
- 미디어 라이브러리 에셋 보기
- 미디어 라이브러리 에셋 편집
- 미디어 라이브러리 에셋 삭제
- 사용자 데이터 내보내기
- 고객 프로필 보기 (PII 수정됨)
- PII 보기
- 대시보드 사용자 편집
- Canvas 템플릿 편집
- Canvas 템플릿 보기
- Canvas 템플릿 보관
- 대시보드 보고서 보기
- 대시보드 보고서 편집
- 대시보드 보고서 삭제

각 사용자 권한에 포함된 내용과 사용 방법에 대한 설명은 [사용자 권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) 섹션을 확인하세요.

## Teams 태그 할당 {#tags-and-filters}

**팀 추가** 필터를 사용하여 Canvases, Campaigns, Content Cards, Segments, 이메일 템플릿, 웹훅 템플릿, Content Blocks 및 미디어 라이브러리 자산에 Teams를 할당할 수 있습니다.

Canvases의 경우, Braze는 사용자가 Canvas에 진입할 때만 Teams 필터 기준과 일치하는지 확인합니다. 사용자가 Canvas에 진입한 후에는 속성이 변경되어 더 이상 Teams 필터 기준과 일치하지 않더라도 모든 캔버스 단계에서 메시지를 계속 수신합니다. Teams 필터는 각 메시지 단계 전송 시 사용자를 재평가하는 [전달 유효성 검사]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations)와는 다르게 동작합니다.

![Campaign에 Teams 태그를 추가하는 모습.]({% image_buster /assets/img/teams1.png %}){: style="max-width:70%;"}

- Teams 생성 시 적용된 정의에 따라, Teams 필터가 할당되면 해당 참여 툴의 오디언스는 정의와 일치하는 고객 프로필로 제한됩니다.
- 할당된 권한에 따라, Teams 멤버는 자신의 Teams 필터가 설정된 대시보드 참여 툴에만 접근할 수 있습니다. 워크스페이스 권한이 제한적이거나 없는 경우, 특정 오브젝트를 저장하거나 실행하기 전에 Teams 필터를 추가해야 합니다. Teams 멤버는 또한 Teams별로 Canvases, Campaigns, Content Cards 및 Segments를 필터링하여 관련 콘텐츠를 식별할 수 있습니다.
- Teams 수준 권한만 가진 사용자에게는 Segments, Campaigns 또는 Canvas 페이지에서 **Created by** 또는 **Last edited by** 필터가 표시되지 않습니다. Braze는 Teams 전용 사용자가 해당 드롭다운에서 모든 Braze 사용자를 탐색할 수 없도록 이러한 필터를 숨깁니다.

### 사용 사례 {#use-cases}

Braze의 마케터인 Michelle에 대한 다음 두 가지 시나리오를 살펴보세요. Michelle은 "Development"라는 Teams의 멤버입니다. Development Teams에 대한 모든 Teams 수준 권한을 가지고 있습니다.

{% tabs %}
{% tab 시나리오 1 - Teams 권한만 %}

이 시나리오에서 Michelle은 워크스페이스 수준 권한이 없는 제한된 사용자입니다. 그녀의 권한은 다음과 같습니다:

![워크스페이스 수준 권한이 없고 16개의 Teams 기반 권한이 있는 커스텀 권한.]({% image_buster /assets/img_archive/scenario1.png %})

Michelle의 할당된 권한에 따라, Campaign을 생성할 때 해당 Campaign에 "Development" Teams만 할당할 수 있습니다. Teams가 할당되지 않으면 Campaign을 실행할 수 없으며, 다른 Teams 태그를 보거나 접근할 수 없습니다.

!["Development" Teams 태그만 표시되는 Campaign Teams 태그 드롭다운.]({% image_buster /assets/img_archive/team_permissions_scenario1.gif %})

{% endtab %}
{% tab 시나리오 2 - Teams 권한과 워크스페이스 권한 %}

이 시나리오에서 Michelle은 여전히 Development Teams의 멤버이지만, 추가적인 워크스페이스 수준 권한도 가지고 있습니다.

![하나의 워크스페이스 수준 권한과 15개의 Teams 기반 권한이 있는 커스텀 권한.]({% image_buster /assets/img_archive/scenario2.png %})

Michelle은 "Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, and Preference Centers"라는 워크스페이스 수준 권한을 가지고 있으므로, 생성하는 Campaign에 다른 Teams 필터를 보고 할당할 수 있습니다.

![여러 Teams 태그가 있는 Campaign Teams 태그 드롭다운]({% image_buster /assets/img_archive/team_permissions_scenario2.gif %})

첫 번째 시나리오와 마찬가지로, Michelle은 Campaign을 실행하기 전에 Development Teams 태그를 추가해야 합니다.

{% endtab %}
{% endtabs %}

## Teams를 활용한 테스트 {#test-with-teams}

Teams의 가능한 사용 사례 중 하나는 프로덕션 환경에서 콘텐츠를 테스트하고 출시하기 위한 Teams 기반 승인 시스템을 만드는 것입니다.

이를 위해 테스트 사용자에게만 액세스할 수 있는 "Development" 팀을 만드세요. 테스트 사용자가 커스텀 속성으로 식별 가능한 경우, 팀이 테스트 사용자에게만 액세스하도록 제한할 수 있습니다. 그런 다음, 팀을 만들거나 편집할 때 해당 커스텀 속성을 정의로 추가하세요(앞의 [Teams 만들기](#creating-Teams) 섹션을 참조하세요). 승인자는 모든 사용자에 대한 액세스 권한을 가져야 합니다.

일반적인 프로세스는 다음과 같습니다:

1. Development 팀이 Campaign을 만들고 "Development" 팀 태그를 추가합니다.
2. Development 팀이 테스트 사용자에게 Campaign을 실행합니다.
3. 승인자 팀이 로컬 Campaign 디자인을 검증하고, 승격한 후 실행합니다. 실행하려면 승인자 팀이 팀 태그를 "Development"에서 "[All Teams]"로 변경하고 Campaign을 다시 실행합니다.

활성 Campaign에 대한 변경 사항:

1. Development 팀이 실행 중인 Campaign을 복제하고, "Development" 팀 태그를 추가한 후 저장합니다.
2. Development 팀이 수정 사항을 적용하고 승인자 팀과 공유합니다.
3. 승인자 팀이 "Development" 팀 태그를 제거하고, 이전 Campaign을 일시 중지한 후 새 Campaign을 실행합니다.

## 기존 팀 보관하기 {#archive-an-existing-team}

**내부 Teams** 페이지에서 Teams를 보관할 수 있습니다.

보관할 Teams를 하나 또는 여러 개 선택합니다. 해당 팀이 Braze 내의 어떤 오브젝트와도 연결되어 있지 않으면 즉시 보관됩니다. 팀이 오브젝트와 연결되어 있는 경우, 보관 프로세스 후 팀을 제거하거나 팀을 교체하는 옵션이 표시됩니다.

![Braze에서 오브젝트와 연결된 팀을 보관하는 화면]({% image_buster /assets/img_archive/archive_a_team.png %}){: style="max-width:70%;"}

Braze 관리자는 보관된 팀을 선택한 후 **보관 해제**를 선택하여 팀의 보관을 해제할 수 있습니다.