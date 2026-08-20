---
nav_title: 권한
article_title: 회사 사용자 권한
page_order: 1
page_type: reference
alias: /braze_permissions/
description: "이 참조 문서에서는 Braze에서 사용자 권한이 어떻게 작동하는지 다룹니다. 여기에서 사용자 권한을 편집하고 설정하는 방법, 대시보드에서 앱에 접근할 수 있는 사용자를 선택하는 방법을 알아볼 수 있습니다."
tool: Dashboard

---

# Braze 권한 {#braze-permissions}

> 권한 세트 생성, 역할 생성, 사용자 권한 편집, 사용자 권한 내보내기 방법을 알아보고, 사용자가 가장 필요한 워크스페이스와 기능에만 접근할 수 있도록 관리하세요.
>
> {% multi_lang_include video.html id="nv699nw706" source="wistia" %}

## 권한 세트 만들기 {#create-a-permission-set}

권한 세트를 사용하여 특정 주제 영역이나 동작과 관련된 권한을 묶을 수 있습니다. 서로 다른 워크스페이스에서 동일한 접근 권한이 필요한 대시보드 사용자에게 권한 세트를 적용할 수 있습니다. 권한 세트를 만들려면 **설정** > **사용자 관리** > **권한 세트**로 이동한 다음 **권한 세트 만들기**를 선택합니다. 각 권한에 대한 설명은 [권한 목록]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions)을 참조하세요.

{% tabs local %}
{% tab 권한 세트 예시 %}
| 이름 | 권한 |
|-----------|----------------|
| 개발자 | "View API Keys", "Edit API Keys", "View Internal Groups", "Edit Internal Groups", "View Message Activity Log", "View Event User Log", "View API identifiers", "View API Usage Dashboard", "View API Limits", "View API Usage Alerts", "Edit API Usage Alerts", "View SDK Debugger", "Edit SDK Debugger". |
| 마케터 | "View Campaigns", "Edit Campaigns", "Archive Campaigns", "View Canvases", "Edit Canvases", "Archive Canvases", "View Frequency Capping Rules", "Edit Frequency Capping Rules", "View Message Prioritization", "Edit Message Prioritization", "View Content Blocks", "View Feature Flags", "Edit Feature Flags", "Archive Feature Flags", "View Segments", "Edit Segments", "Edit Global Control Group", "View IAM Templates", "Edit IAM Templates", "Archive IAM Templates", "View Email Templates", "Edit Email Templates", "Archive Email Templates", "View Webhook Templates", "Edit Webhook Templates", "Archive Webhook Templates", "View Email Link Templates", "Edit Email Link Templates", "View Media Library Assets", "View Locations", "Edit Locations", "Archive Locations", "View Promotion Codes", "Edit Promotion Codes", "Export Promotion Codes", "View Preference Centers", "Edit Preference Centers", "Edit Dashboard Reports", "View Banner Templates", "View Localization Settings", "Use Operator", "View Decisioning Studio Agents". |
| 사용자 관리 | "Edit Dashboard Users", "View Teams", "Edit Teams", "Archive Teams". |
{: .reset-td-br-1 .reset-td-br-2 aria-label="권한 세트 예시" }
{% endtab %}
{% endtabs %}

## 역할 만들기 {#creating-a-role}

역할을 사용하면 개별 커스텀 권한과 워크스페이스 접근 제어를 묶어 보다 체계적으로 관리할 수 있습니다. 이 기능은 하나의 대시보드에 여러 브랜드나 지역별 워크스페이스가 있는 경우 특히 유용합니다. 역할을 사용하면 대시보드 사용자를 적절한 워크스페이스에 추가하고 관련 권한을 직접 부여할 수 있습니다. 역할을 만들려면 **설정** > **사용자 관리** > **역할**로 이동한 다음 **역할 만들기**를 선택합니다. 각 권한에 대한 설명은 [권한 목록]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions)을 참조하세요.

{% tabs local %}
{% tab 역할 예시 %}
| 역할 이름 | 워크스페이스 | 권한 |
| ----------- | ----------- | --------- |
| 마케터 - 패션 브랜드 | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand {:/} | "View Campaigns", "Edit Campaigns", "Archive Campaigns", "View Canvases", "Edit Canvases", "Archive Canvases", "View Content Blocks", "Edit Content Blocks", "Archive Content Blocks", "Launch Content Blocks", "View Feature Flags", "Edit Feature Flags", "Archive Feature Flags", "View Segments", "Edit Segments", "View Banner Templates", "Edit Banner Templates", "View Email Templates", "Edit Email Templates", "View Media Library Assets", "Edit Media Library Assets", "Delete Media Library Assets", "View Locations", "Edit Locations", "Archive Locations", "View Promotion Codes", "Edit Promotion Codes", "Export Promotion Codes", "View Preference Centers", "Edit Preference Centers". |
| 마케터 - 스킨케어 브랜드 | {::nomarkdown}[DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | "View Campaigns", "Edit Campaigns", "Archive Campaigns", "View Canvases", "Edit Canvases", "Archive Canvases", "View Content Blocks", "Edit Content Blocks", "Archive Content Blocks", "Launch Content Blocks", "View Feature Flags", "Edit Feature Flags", "Archive Feature Flags", "View Segments", "Edit Segments", "View Banner Templates", "Edit Banner Templates", "View Email Templates", "Edit Email Templates", "View Media Library Assets", "Edit Media Library Assets", "Delete Media Library Assets", "View Locations", "Edit Locations", "Archive Locations", "View Promotion Codes", "Edit Promotion Codes", "Export Promotion Codes", "View Preference Centers", "Edit Preference Centers". |
| 사용자 관리 - 전체 브랜드 | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand, [DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | "Edit Dashboard Users", "View Teams", "Edit Teams", "Archive Teams" |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="역할 예시" }
{% endtab %}
{% endtabs %}

## 권한 세트와 역할은 Teams와 어떻게 다른가요? {#how-do-permission-sets-and-roles-differ-from-teams}

{% multi_lang_include permissions/differences.md content="Differences" %}

### Teams에 사용자 권한을 추가할 때 고려 사항 {#considerations-for-adding-user-permissions-to-teams}

Braze 대시보드에서 권한을 저장할 때, 특히 워크스페이스에서 사용자를 추가하거나 제거하거나 Teams에 추가할 때 어려움이 발생할 수 있습니다. 사용자의 권한이 워크스페이스 수준에서 이미 보유한 권한과 동일한 경우 **Save/Update Users** 버튼이 회색으로 비활성화될 수 있습니다. 이 제한은 모든 사용자가 전체 워크스페이스와 동일한 권한을 보유하고 있다면 Teams를 사용하는 이점이 없기 때문에 존재합니다.

동일한 권한을 유지하면서 사용자를 Teams에 성공적으로 추가하려면 워크스페이스 수준에서는 권한을 할당하지 마세요. 대신 팀 수준에서만 권한을 할당하세요.

## 제한된 사용자 {#limited-users}

제한된 사용자는 회사 관리자 및 워크스페이스 관리자에 비해 제한이 있지만, Braze 대시보드의 특정 측면을 관리할 수 있는 특정 권한을 가지고 있습니다.

| 범위 | 설명 |
| --- | --- |
| 권한 | 제한된 사용자는 "대시보드 사용자 편집" 권한이 있는 경우 다른 제한된 사용자의 권한을 편집할 수 있습니다. 또한 새로운 제한된 사용자를 생성하고 권한 세트를 수정할 수 있습니다. 그러나 회사 관리자 계정을 생성하거나 관리할 수는 없습니다. |
| 역할 제한 | 제한된 사용자가 "워크스페이스 관리자"를 제외한 모든 권한을 가지고 있더라도, 워크스페이스 관리자에게 일반적으로 부여되는 다른 모든 권한에는 접근할 수 있습니다. |
| 권한 가시성 | 제한된 사용자가 하나의 워크스페이스(예: Dev)에 대해 "대시보드 사용자 편집" 권한을 가지고 있지만 다른 워크스페이스(예: Prod)에 대해서는 가지고 있지 않은 경우, 대시보드 사용자 상세 페이지에서 Prod 워크스페이스 권한이 표시되지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="제한된 사용자의 권한" }

### 제한된 사용자 비교 {#compare-limited-users}

| 제한된 사용자 유형 | 설명 |
| --- | --- |
| 워크스페이스 관리자 | 워크스페이스 관리자는 워크스페이스 관리에 특화된 권한을 가지지만, 회사 관리자와 동일한 권한을 가지지는 않습니다. 제한된 사용자는 필요한 권한이 체크되어 있으면 워크스페이스 관리자와 유사한 권한을 상속받을 수 있습니다. |
| 관리자(회사 관리자) | 회사 관리자는 대시보드 사용자 삭제 기능을 포함하여 더 넓은 권한을 가집니다. 그러나 자신의 계정은 삭제할 수 없으며, 해당 작업을 위해서는 다른 회사 관리자에게 연락해야 합니다. |
| 보기 전용 접근 | Campaigns 페이지와 같은 대시보드의 특정 부분에 접근하려면 사용자에게 보기 권한이 할당되어 있어야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="제한된 사용자 비교" }

### 제한된 접근 오류 {#limited-access-error}

사용자는 "이 페이지에 접근하려면 '랜딩 페이지 보기' 권한이 필요합니다"와 같은 메시지를 볼 수 있습니다. 이러한 경우, 사용자와 계정 관리자는 필요한 권한이 부여되어 있는지 확인해야 합니다. 권한이 부여되어 있다면, 사용자의 권한을 비활성화한 후 다시 활성화하여 문제를 해결해 보세요.

{% alert note %}
한 대시보드 사용자의 사용자 권한을 다른 사용자로 병합하거나 가져오는 것은 불가능합니다.
{% endalert %}

## 사용자 권한의 세부 사항 {#nuances-of-user-permissions}

대시보드 접근 권한을 할당할 때 다음 동작을 유의하세요:

- **워크스페이스 관리자 vs 회사 관리자:** 워크스페이스 관리자는 할당된 워크스페이스 내에서 권한을 관리합니다. 회사 관리자는 다른 대시보드 사용자 삭제를 포함하여 회사 전체에 대한 권한을 가집니다.
- **제한된 사용자:** "대시보드 사용자 편집" 권한이 있는 제한된 사용자는 다른 제한된 사용자를 관리할 수 있지만, 회사 관리자 계정을 생성하거나 관리할 수는 없습니다.
- **대시보드 사용자 관리 범위:** 사용자 상세 페이지에서 권한은 편집자가 접근할 수 있는 워크스페이스에 대해서만 표시됩니다. 하나의 워크스페이스에서 사용자를 편집할 수 있는 제한된 사용자는 다른 워크스페이스의 권한 체크박스를 볼 수 없을 수 있습니다.
- **권한 할당 버튼:** 사용자를 편집할 때 해당 사용자가 이미 관리 가능한 모든 워크스페이스에 대해 워크스페이스 수준 권한 또는 권한 세트를 보유하고 있으면 **권한 할당** 버튼이 사라집니다. 이는 워크스페이스 수준에서 추가로 할당할 워크스페이스가 남아 있지 않기 때문입니다.
- **사용자 데이터 내보내기:** 사용자 데이터를 내보내려면 내보내기 권한 외에 워크스페이스 수준의 접근 권한이 필요합니다.
- **복합 권한:** 일부 영역에서는 여러 권한이 필요합니다. 예를 들어, [기술 파트너]({{site.baseurl}}/partners)를 구성하려면 일반적으로 파트너 접근 권한과 관련 워크스페이스 기능에 대한 기본 읽기 권한이 모두 필요합니다.
- **사용자 데이터 가져오기 및 업데이트:** 이 권한에는 대시보드 사용자 레코드뿐만 아니라 가져오기 플로우를 통해 앱 사용자 프로필을 편집하는 기능도 포함됩니다.

## 사용자 권한 편집 {#edit-a-users-permissions}

사용자의 현재 관리자, 회사 또는 워크스페이스 권한을 편집하려면 **설정** > **사용자 관리** > **회사 사용자**로 이동한 다음 해당 사용자의 이름을 선택합니다.

![대시보드 사용자 테이블이 표시된 Braze의 "회사 사용자" 페이지.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %})

{% tabs local %}
{% tab 관리자 %}

### 관리자 {#admin}

관리자는 모든 기능에 접근할 수 있으며 회사 설정을 변경할 수 있습니다. 관리자는 다음을 수행할 수 있습니다:

- [승인 설정]({{site.baseurl}}/user_guide/messaging/governance/approvals#turning-on-the-approval-workflow) 변경
- 다른 [Braze 사용자]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users#adding-company-users) 추가, 편집, 삭제, 일시 중지 또는 일시 중지 해제
- Braze 사용자를 CSV 파일로 내보내기

관리자 권한을 부여하거나 제거하려면 **이 사용자는 관리자입니다**를 선택한 다음 **사용자 업데이트**를 선택합니다.

{% alert warning %}
사용자에게서 관리자 권한을 제거하면 해당 사용자에게 최소 하나의 [회사 수준 또는 워크스페이스 수준 권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#edit-a-users-permissions)을 할당하기 전까지 Braze에 접근할 수 없습니다.
{% endalert %}

{% endtab %}
{% tab 회사 %}

### 회사 {#company}

사용자의 다음 회사 수준 권한을 관리하려면 해당 권한 옆의 체크박스를 선택하거나 해제합니다. 완료되면 **사용자 업데이트**를 선택합니다.

| 권한 이름 | 설명 |
|----------|-----------|
| 회사 설정 관리 | 사용자가 권한 설정 및 발신자 인증을 수정할 수 있도록 허용합니다. |
| 워크스페이스 생성 및 삭제 | 사용자가 워크스페이스를 생성하고 삭제할 수 있도록 허용합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="회사 수준 권한" }

{% endtab %}
{% tab 워크스페이스 %}

### 워크스페이스 {#workspace}

Braze에서 사용자가 속한 각 워크스페이스에 대해 서로 다른 권한을 부여할 수 있습니다. 워크스페이스 수준 권한을 관리하려면 **워크스페이스 및 권한 선택**을 선택한 다음 수동으로 권한을 선택하거나 이전에 생성한 [권한 세트 또는 역할]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#create-a-permission-set)을 할당합니다. 서로 다른 워크스페이스에 대해 다른 권한을 부여해야 하는 경우 필요한 만큼 이 과정을 반복합니다. 각 권한에 대한 설명은 [권한 목록]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions)을 참조하세요.

{% subtabs %}
{% subtab 수동 선택 %}

**워크스페이스**에서 드롭다운을 통해 하나 이상의 워크스페이스를 선택합니다. 그런 다음 **권한**에서 하나 이상의 권한을 선택합니다. 선택한 워크스페이스에 대해서만 해당 권한이 할당됩니다. 선택적으로 해당 워크스페이스에 대한 전체 권한을 부여하려면 **워크스페이스 관리자 접근 권한 할당**을 선택할 수 있습니다.

완료되면 **사용자 업데이트**를 선택합니다.

![Braze에서 워크스페이스 수준 권한을 수동으로 선택하는 화면.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})

{% endsubtab %}
{% subtab 권한 세트 할당 %}

**워크스페이스**에서 드롭다운을 통해 하나 이상의 워크스페이스를 선택합니다. 그런 다음 **권한 세트**에서 하나의 권한 세트를 선택합니다. 선택한 워크스페이스에 대해서만 해당 권한이 할당됩니다.

완료되면 **사용자 업데이트**를 선택합니다.

![Braze에서 권한 세트를 통해 워크스페이스 수준 권한을 할당하는 화면.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})

{% endsubtab %}
{% subtab 역할 할당 %}

**워크스페이스**에서 드롭다운을 통해 하나 이상의 워크스페이스를 선택합니다. 그런 다음 **역할**에서 하나의 역할을 선택합니다. 선택한 워크스페이스에 대해서만 해당 권한이 할당됩니다.

완료되면 **사용자 업데이트**를 선택합니다.

![Braze에서 역할을 통해 워크스페이스 수준 권한을 할당하는 화면.]({% image_buster /assets/img/braze_permissions/workspace_level_role.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 사용자 권한 내보내기 {#exporting-user-permissions}

사용자 목록과 해당 권한을 다운로드하려면 **설정** > **사용자 관리** > **회사 사용자**로 이동한 다음 **사용자 내보내기**를 선택합니다. 잠시 후 CSV 파일이 이메일 주소로 전송됩니다.

## 권한 목록 {#list-of-permissions}

### 메시징 {#messaging}

| 제품 영역 | 권한 | 정의 |
| --- | --- | --- |
| Campaigns | Campaigns 보기 | Campaigns 보기 |
| Campaigns | Campaigns 실행 | 기존 Campaigns 시작, 중지, 일시 중지 또는 재개 |
| Campaigns | Campaigns 보관 | Campaigns를 보관함으로 이동 |
| Campaigns | Campaigns 편집 | Campaigns 생성 및 업데이트 |
| Campaigns | Campaigns 승인 및 거부 | Campaigns를 승인하거나 거부합니다. 이 권한이 적용되려면 [Campaigns 승인 워크플로]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals)가 활성화되어 있어야 합니다. 이 설정은 현재 얼리 액세스 중입니다. 얼리 액세스 참여에 관심이 있으시면 계정 매니저에게 문의하세요. |
| Canvas | Canvases 보기 | Canvases 보기 |
| Canvas | Canvases 보관 | Canvases를 보관함으로 이동 |
| Canvas | Canvases 편집 | Canvases 생성 및 업데이트 |
| Canvas | Canvases 실행 | 기존 Canvases 시작, 중지, 일시 중지 또는 재개 |
| Canvas | Canvases 승인 및 거부 | Canvases를 승인하거나 거부합니다. 이 권한이 적용되려면 [Canvases 승인 워크플로]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals)가 활성화되어 있어야 합니다. 이 설정은 현재 얼리 액세스 중입니다. 얼리 액세스 참여에 관심이 있으시면 계정 매니저에게 문의하세요. |
| 기능 플래그 | 기능 플래그 보기 | 기능 플래그 보기 |
| 기능 플래그 | 기능 플래그 보관 | 기능 플래그를 보관함으로 이동 |
| 기능 플래그 | 기능 플래그 편집 | 기능 플래그 생성 및 업데이트 |
| 최대 게재빈도 설정 | 최대 게재빈도 설정 규칙 보기 | 최대 게재빈도 설정 규칙 보기 |
| 최대 게재빈도 설정 | 최대 게재빈도 설정 규칙 편집 | 최대 게재빈도 설정 규칙 생성 및 업데이트 |
| 랜딩 페이지 | 랜딩 페이지 보기 | 랜딩 페이지 보기 |
| 랜딩 페이지 | 랜딩 페이지 게시 | 초안 랜딩 페이지를 활성화 |
| 랜딩 페이지 | 랜딩 페이지 초안 편집 | 랜딩 페이지 초안 생성 및 저장 |
| 메시지 보관 설정 | 메시지 보관 설정 보기 | 변경 없이 메시지 보관 설정 보기 |
| 메시지 보관 설정 | 메시지 보관 설정 편집 | 메시지 보관 설정 생성 및 업데이트 |
| 메시지 우선순위 | 메시지 우선순위 보기 | 변경 없이 메시지 우선순위 설정 보기 |
| 메시지 우선순위 | 메시지 우선순위 편집 | 메시지 우선순위 설정 생성 및 업데이트 |
| WhatsApp Flows | WhatsApp Flows 보기 | 모든 WhatsApp Flows 보기 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="메시징 권한" }

### 오디언스 {#audience}

| 제품 영역 | 권한 | 정의 |
| --- | --- | --- |
| 글로벌 컨트롤 그룹 | 글로벌 컨트롤 그룹 보기 | 글로벌 컨트롤 그룹 설정 페이지 보기 |
| 글로벌 컨트롤 그룹 | 글로벌 컨트롤 그룹 편집 | 글로벌 컨트롤 그룹 생성 및 변경 사항 저장. "글로벌 컨트롤 그룹 편집" 권한이 있는 사용자는 "Campaigns 편집" 및 "Canvases 편집" 권한도 부여받아야 합니다. "글로벌 컨트롤 그룹 편집" 권한이 있는 사용자에게는 "글로벌 컨트롤 그룹 보기" 권한도 부여됩니다. |
| 위치 | 위치 보관 | 위치를 보관함으로 이동 |
| 위치 | 위치 보기 | 위치 보기 |
| 위치 | 위치 편집 | 위치 생성 및 편집 |
| Segments | Segments 보기 | Segments 보기. "Segments 편집" 또는 "Segments 보관" 권한을 가지려면 "Segments 보기" 권한이 있어야 합니다. |
| Segments | Segments 보관 | Segments 보관 및 보관 해제. "Segments 보관" 권한이 있는 사용자는 "Segments 보기" 권한도 부여받아야 합니다. |
| Segments | Segments 편집 | Segments 생성 및 업데이트. "Segments 편집" 권한이 있는 사용자는 "Segments 보기" 권한도 부여받아야 합니다. |
| 사용자 데이터 | 사용자 가져오기 보기 | 변경 없이 CSV 사용자 가져오기 보기 |
| 사용자 데이터 | 사용자 가져오기 | 대시보드에 사용자 업로드 |
| 사용자 데이터 | 사용자 데이터 편집 | 사용자 데이터 생성 및 업데이트 |
| 사용자 데이터 | 사용자 데이터 내보내기 | 대시보드에서 사용자 다운로드 |
| 중복 사용자 | 사용자 병합 기록 보기 | 사용자 병합 기록 목록 보기 |
| 사용자 | 고객 프로필 보기 (PII 삭제됨) | PII 준수 방식으로 고객 프로필을 봅니다. 이 권한이 있는 사용자는 "PII로 표시된 커스텀 속성 보기" 권한이 없는 한 PII로 표시된 커스텀 속성을 참조하는 Campaigns를 저장하거나 실행할 수 없습니다.<br><br>"고객 프로필 보기 (PII 삭제됨)" 권한은 사용 전에 활성화해야 합니다. 워크스페이스에서 활성화하려면 고객 성공 매니저에게 문의하세요. |
| 사용자 | 사용자 이벤트 속성정보 보기 | 고객 프로필의 **이벤트 기록** 탭에서 이벤트 속성정보 보기 |
| 중복 사용자 | 중복 사용자 병합 | 중복 사용자를 하나의 사용자로 결합합니다. 병합 후 중복 항목은 제거됩니다. |
| 사용자 삭제 | 사용자 삭제 기록 보기 | 사용자 삭제 기록 목록 보기 |
| 사용자 삭제 | 사용자 삭제 | 대시보드에서 개별 또는 일괄로 사용자를 영구 삭제 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="오디언스 권한" }

### 템플릿 {#template}

| 제품 영역 | 권한 | 정의 |
| --- | --- | --- |
| 배너 템플릿 | 배너 템플릿 보기 | 배너 템플릿 보기 |
| 배너 템플릿 | 배너 템플릿 보관 | 배너 템플릿을 보관함으로 이동 |
| 배너 템플릿 | 배너 템플릿 편집 | 배너 템플릿 생성 및 업데이트 |
| Canvas 템플릿 | Canvas 템플릿 보기 | Canvas 템플릿 보기 |
| Canvas 템플릿 | Canvas 템플릿 보관 | Canvas 템플릿을 보관함으로 이동 |
| Canvas 템플릿 | Canvas 템플릿 생성 및 편집 | Canvas 템플릿 생성 및 업데이트 |
| Content Blocks | Content Blocks 보기 | Content Blocks 보기 |
| Content Blocks | Content Blocks 실행 | 초안 Content Blocks 게시, 실행된 Content Blocks 편집, 보관 및 보관 해제 |
| Content Blocks | Content Blocks 보관 | Content Blocks를 보관함으로 이동 |
| Content Blocks | Content Blocks 편집 | Content Blocks 생성 및 초안 Content Blocks 편집 |
| 이메일 링크 템플릿 | 이메일 링크 템플릿 보기 | 변경 없이 링크 템플릿 보기 |
| 이메일 링크 템플릿 | 이메일 링크 템플릿 편집 | 링크 템플릿 생성 및 업데이트 |
| 이메일 템플릿 | 이메일 템플릿 보기 | 이메일 템플릿 보기 |
| 이메일 템플릿 | 이메일 템플릿 보관 | 이메일 템플릿을 보관함으로 이동 |
| 이메일 템플릿 | 이메일 템플릿 편집 | 이메일 템플릿 생성 및 업데이트 |
| IAM 템플릿 | IAM 템플릿 보기 | 변경 없이 인앱 메시지 템플릿 보기 |
| IAM 템플릿 | IAM 템플릿 보관 | IAM 템플릿을 보관함으로 이동 |
| IAM 템플릿 | IAM 템플릿 편집 | 인앱 메시지 템플릿 생성 및 업데이트 |
| 랜딩 페이지 템플릿 | 랜딩 페이지 템플릿 보기 | 랜딩 페이지 템플릿 보기 |
| 랜딩 페이지 템플릿 | 랜딩 페이지 템플릿 보관 | 랜딩 페이지 템플릿을 보관함으로 이동 |
| 랜딩 페이지 템플릿 | 랜딩 페이지 템플릿 편집 | 랜딩 페이지 템플릿 생성 및 업데이트 |
| 웹훅 템플릿 | 웹훅 템플릿 보기 | 변경 없이 웹훅 템플릿 보기 |
| 웹훅 템플릿 | 웹훅 템플릿 보관 | 웹훅 템플릿을 보관함으로 이동 |
| 웹훅 템플릿 | 웹훅 템플릿 편집 | 웹훅 템플릿 생성 및 업데이트 |
| WhatsApp 메시지 템플릿 | WhatsApp 메시지 템플릿 보기 | 사용자가 [WhatsApp 메시지 템플릿]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#step-2-compose-your-whatsapp-message)을 볼 수 있도록 허용합니다. |
| WhatsApp 메시지 템플릿 | WhatsApp 메시지 템플릿 편집 | 사용자가 템플릿 빌더에서 WhatsApp 메시지 템플릿을 생성할 수 있도록 허용합니다. 이 기능은 현재 얼리 액세스 중입니다. |
| Meta의 WhatsApp 메시지 템플릿 | Meta의 WhatsApp 메시지 템플릿 보기 | 모든 WhatsApp 템플릿 보기 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="템플릿 권한" }

### 파트너 통합 {#partner-integrations}

| 제품 영역 | 권한 | 정의 |
| --- | --- | --- |
| 커런츠 통합 | 커런츠 통합 보기 | 커런츠 통합 보기 |
| 커런츠 통합 | 커런츠 통합 편집 | 커런츠 통합 생성, 업데이트 및 삭제 |
| 기술 파트너 | 기술 파트너 편집 | 기술 파트너 생성 및 업데이트 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="파트너 통합 권한" }

### 데이터 설정 {#data-settings}

| 제품 영역 | 권한 | 정의 |
| --- | --- | --- |
| 카탈로그 | 카탈로그 보기 | 카탈로그 및 셀렉션 보기 |
| 카탈로그 | 카탈로그 삭제 | 카탈로그 영구 삭제 |
| 카탈로그 | 카탈로그 내보내기 | 대시보드에서 카탈로그 다운로드 |
| 카탈로그 | 카탈로그 편집 | 카탈로그 및 셀렉션 생성 및 업데이트 |
| 클라우드 데이터 수집 | 클라우드 데이터 수집 편집 | 소스 및 동기화 생성, 업데이트 및 삭제 |
| 커스텀 속성 | 커스텀 속성 보기 | 커스텀 속성 및 사용 보고서 보기 |
| 커스텀 속성 | 커스텀 속성 내보내기 | 대시보드에서 커스텀 속성 다운로드 |
| 커스텀 속성 | 커스텀 속성 삭제 | 커스텀 속성 영구 삭제 |
| 커스텀 속성 | 커스텀 속성 차단 목록 | 대시보드에서 사용을 제한하는 차단 목록에 커스텀 속성 추가 |
| 커스텀 속성 | 커스텀 속성 편집 | 커스텀 속성 생성 및 업데이트 |
| 커스텀 이벤트 속성정보 세분화 | 커스텀 이벤트 속성정보 세분화 편집 | 커스텀 이벤트 속성정보에 대한 세분화 활성화 및 비활성화 |
| 커스텀 이벤트 | 커스텀 이벤트 보기 | 커스텀 이벤트 및 사용 보고서 보기, 일일 분석 보고서 이메일에 커스텀 이벤트 추가 |
| 커스텀 이벤트 | 커스텀 이벤트 내보내기 | 대시보드에서 커스텀 이벤트 다운로드 |
| PII | PII 보기 | PII 보기 |
| 커스텀 이벤트 | 커스텀 이벤트 삭제 | 커스텀 이벤트 영구 삭제 |
| 커스텀 이벤트 | 커스텀 이벤트 차단 목록 | 대시보드에서 사용을 제한하는 차단 목록에 커스텀 이벤트 추가 |
| 커스텀 이벤트 | 커스텀 이벤트 편집 | 커스텀 이벤트 생성 및 업데이트 |
| 제품 | 제품 보기 | 제품 보기 |
| 제품 | 제품 차단 목록 | 대시보드에서 사용을 제한하는 차단 목록에 제품 추가 |
| 제품 | 제품 편집 | 제품 생성 및 업데이트 |
| 구매 속성정보 세분화 | 구매 속성정보 세분화 편집 | 구매 이벤트 속성정보에 대한 세분화 활성화 및 비활성화 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="데이터 설정 권한" }

### 설정 {#settings}

| 제품 영역 | 권한 | 정의 |
| --- | --- | --- |
| API 식별자 | API 식별자 보기 | API 식별자 및 기타 식별자 보기 |
| API 키 | API 키 보기 | API 키 보기 |
| API 키 | API 키 편집 | API 키 생성 및 업데이트 |
| API 제한 | API 제한 보기 | API 사용량 제한 보기 |
| API 사용 알림 | API 사용 알림 보기 | API 사용 알림 보기 |
| API 사용 알림 | API 사용 알림 편집 | API 사용 알림 생성 및 업데이트 |
| API 사용 데이터 | API 사용 대시보드 보기 | API 사용 대시보드 보기 |
| 앱 설정 | 앱 설정 편집 | 앱 설정 내에서 앱 생성, 편집 및 업데이트 |
| 앱 설정 | 앱 설정 보기 | 앱 설정 페이지 보기 |
| 오디언스 동기화 설정 | 오디언스 동기화 설정 보기 | 연결된 오디언스 동기화 파트너의 모든 설정 보기 |
| 대시보드 사용자 | 대시보드 사용자 편집 | 회사 사용자 보기, 생성 및 편집 |
| 이메일 설정 | 이메일 설정 보기 | 이메일 환경설정 보기 |
| 이메일 설정 | 이메일 설정 편집 | 이메일 환경설정 활성화 및 업데이트 |
| 이벤트 사용자 로그 | 이벤트 사용자 로그 보기 | 이벤트 사용자 로그 보기 |
| 내부 그룹 | 내부 사용자 그룹 보기 | 내부 그룹 보기 |
| 내부 그룹 | 내부 사용자 그룹 삭제 | 내부 그룹 삭제 |
| 내부 그룹 | 내부 사용자 그룹 편집 | 내부 그룹 생성 및 업데이트 |
| 메시지 활동 로그 | 메시지 활동 로그 보기 | 메시지 활동 로그 보기 |
| 다국어 설정 | 현지화 설정 보기 | 다국어 로케일 설정 페이지 보기 |
| 다국어 설정 | 현지화 설정 삭제 | 다국어 로케일 삭제 |
| 다국어 설정 | 현지화 설정 편집 | 다국어 로케일 생성 |
| 환경설정 센터 | 환경설정 센터 보기 | 환경설정 센터 보기 |
| 환경설정 센터 | 환경설정 센터 편집 | 환경설정 센터 생성 및 업데이트 |
| 환경설정 센터 | 환경설정 센터 실행 | 초안 환경설정 센터를 활성화하거나 기존 환경설정 센터 업데이트 |
| 푸시 설정 | 푸시 설정 보기 | 푸시 설정 보기 |
| 푸시 설정 | 푸시 설정 편집 | 푸시 설정 생성 및 업데이트 |
| SDK 디버거 | SDK 디버거 보기 | SDK 디버거 또는 디버깅 세션 보기 |
| SDK 디버거 | SDK 디버거 편집 | SDK 디버거 세션 생성 및 다운로드 |
| 태그 | 태그 보기 | 태그 보기 |
| 태그 | 태그 삭제 | 태그 영구 삭제 |
| 태그 | 태그 편집 | 태그 생성 및 업데이트 |
| Teams | Teams 보기 | Teams 보기 |
| Teams | Teams 보관 | Teams를 보관함으로 이동 |
| Teams | Teams 편집 | Teams 생성 및 업데이트 |
| WhatsApp 설정 | WhatsApp 설정 보기 | 모든 WhatsApp 채널 설정 보기 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="설정 권한" }

### Decisioning Studio

| 제품 영역 | 권한 | 정의 |
| --- | --- | --- |
| Decisioning Studio 에이전트 | Decisioning Studio 에이전트 보기 | 변경 없이 Decisioning Studio 에이전트 구성 보기 |
| Decisioning Studio 오디언스 | Decisioning Studio 오디언스 보기 | Decisioning Studio 에이전트 구성 요약에서 오디언스 세부 정보 보기 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Decisioning Studio 권한" }

### 기타 {#other}

| 제품 영역 | 권한 | 정의 |
| --- | --- | --- |
| 앱 사용량 | 사용 데이터 보기 | 사용 데이터 보기 |
| 청구 | 청구 세부 정보 보기 | 청구 세부 정보 보기 |
| 커스텀 에이전트 | 에이전트 콘솔 AI 에이전트 보기 | 사용자가 커스텀 AI 에이전트를 볼 수 있도록 허용 |
| 커스텀 에이전트 | 에이전트 콘솔 AI 에이전트 보관 | 사용자가 커스텀 AI 에이전트를 보관할 수 있도록 허용 |
| 커스텀 에이전트 | 에이전트 콘솔 AI 에이전트 편집 | 사용자가 커스텀 AI 에이전트를 생성 및 업데이트할 수 있도록 허용 |
| PII로 표시된 커스텀 속성 | PII로 표시된 커스텀 속성 보기 | PII로 표시된 커스텀 속성 보기 |
| 대시보드 보고서 | 대시보드 보고서 보기 | 변경 없이 보고서 보기 |
| 대시보드 보고서 | 대시보드 보고서 삭제 | 보고서 영구 삭제 |
| 대시보드 보고서 | 대시보드 보고서 편집 | 보고서 생성 및 업데이트 |
| 도메인 설정 | 도메인 설정 편집 | 인증된 도메인에서 위임된 도메인 및 커스텀 도메인 추가 |
| 필드 수준 암호화 | 식별자 필드 수준 암호화 편집 | 필드 수준 암호화 설정 활성화 및 업데이트 |
| 미디어 라이브러리 에셋 | 미디어 라이브러리 에셋 보기 | 미디어 라이브러리 에셋 보기 |
| 미디어 라이브러리 에셋 | 미디어 라이브러리 에셋 삭제 | UI에서 미디어 라이브러리 에셋을 제거합니다. 삭제된 에셋은 해당 에셋을 참조하는 메시지가 깨지지 않도록 Braze에서 계속 호스팅됩니다. 에셋을 영구적으로 삭제하려면 Braze 지원팀에 문의하세요. |
| 미디어 라이브러리 에셋 | 미디어 라이브러리 에셋 편집 | 미디어 라이브러리 에셋 생성 및 업데이트 |
| 미디어 라이브러리 에셋 | 미디어 라이브러리 에셋 교체 | URL 및 에셋 ID를 유지하면서 기존 미디어 라이브러리 에셋의 파일 교체 |
| 메시징 사용량 제한 | 메시징 사용량 제한 보기 | 워크스페이스 수준 메시징 사용량 제한 보기 |
| 메시징 사용량 제한 | 메시징 사용량 제한 편집 | 워크스페이스 수준 메시징 사용량 제한 구성 및 편집 |
| Operator | BrazeAI Operator<sup>TM</sup> 사용 | Braze Operator에 접근하여 질문에 답하고, 설정을 탐색하고, 문제를 해결하고, 아이디어를 브레인스토밍합니다. |
| 배치 | 배치 보기 | 배너 배치 보기 |
| 배치 | 배치 보관 | 배너 배치를 보관함으로 이동 |
| 배치 | 배치 편집 | 배너 배치 생성 및 업데이트 |
| 프로모션 코드 | 프로모션 코드 보기 | 프로모션 코드 보기 |
| 프로모션 코드 | 프로모션 코드 내보내기 | 대시보드에서 프로모션 코드 목록 다운로드 |
| 프로모션 코드 | 프로모션 코드 편집 | 프로모션 코드 생성 및 업데이트 |
| 구독 그룹 | 구독 편집 | 구독 그룹 생성 및 업데이트 |
| 변환 | 데이터 변환 편집 | 데이터 변환 생성 및 업데이트 |
| 변환 | 데이터 변환 보기 | 데이터 변환 보기 |
| 지원 티켓 | 지원 티켓 생성 | 지원 티켓 생성 및 업데이트 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="기타 권한" }