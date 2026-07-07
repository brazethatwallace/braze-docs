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

## 권한 세트 생성 {#create-a-permission-set}

권한 세트를 사용하여 특정 주제 영역이나 동작과 관련된 권한을 묶을 수 있습니다. 서로 다른 워크스페이스에서 동일한 접근 권한이 필요한 대시보드 사용자에게 권한 세트를 적용할 수 있습니다. 권한 세트를 생성하려면 **설정** > **사용자 관리** > **권한 세트**로 이동한 다음 **권한 세트 생성**을 선택합니다. 각 권한에 대한 설명은 [권한 목록]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions)을 참조하세요.

{% tabs local %}
{% tab 권한 세트 예시 %}
| 이름 | 권한 |
|-----------|----------------|
| Developers | "View API Keys", "Edit API Keys", "View Internal Groups", "Edit Internal Groups", "View Message Activity Log", "View Event User Log", "View API identifiers", "View API Usage Dashboard", "View API Limits", "View API Usage Alerts", "Edit API Usage Alerts", "View SDK Debugger", "Edit SDK Debugger". |
| Marketers | "View Campaigns", "Edit Campaigns", "Archive Campaigns", "View Canvases", "Edit Canvases", "Archive Canvases", "View Frequency Capping Rules", "Edit Frequency Capping Rules", "View Message Prioritization", "Edit Message Prioritization", "View Content Blocks", "View Feature Flags", "Edit Feature Flags", "Archive Feature Flags", "View Segments", "Edit Segments", "Edit Global Control Group", "View IAM Templates", "Edit IAM Templates", "Archive IAM Templates", "View Email Templates", "Edit Email Templates", "Archive Email Templates", "View Webhook Templates", "Edit Webhook Templates", "Archive Webhook Templates", "View Email Link Templates", "Edit Email Link Templates", "View Media Library Assets", "View Locations", "Edit Locations", "Archive Locations", "View Promotion Codes", "Edit Promotion Codes", "Export Promotion Codes", "View Preference Centers", "Edit Preference Centers", "Edit Dashboard Reports", "View Banner Templates", "View Localization Settings", "Use Operator", "View Decisioning Studio Agents". |
| User Management | "Edit Dashboard Users", "View Teams", "Edit Teams", "Archive Teams". |
{: .reset-td-br-1 .reset-td-br-2 aria-label="권한 세트 예시" }
{% endtab %}
{% endtabs %}

## 역할 생성 {#creating-a-role}

역할은 개별 커스텀 권한과 워크스페이스 접근 제어를 묶어 더 체계적인 구조를 제공합니다. 이는 하나의 대시보드에 여러 브랜드나 지역별 워크스페이스가 있는 경우 특히 유용합니다. 역할을 사용하면 대시보드 사용자를 올바른 워크스페이스에 추가하고 관련 권한을 직접 부여할 수 있습니다. 역할을 생성하려면 **설정** > **사용자 관리** > **역할**로 이동한 다음 **역할 생성**을 선택합니다. 각 권한에 대한 설명은 [권한 목록]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions)을 참조하세요.

{% tabs local %}
{% tab 역할 예시 %}
| 역할 이름 | 워크스페이스 | 권한
----------- | ----------- | ---------
| Marketer - Fashion Brands | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand {:/} | "View Campaigns", "Edit Campaigns", "Archive Campaigns", "View Canvases", "Edit Canvases", "Archive Canvases", "View Content Blocks", "Edit Content Blocks", "Archive Content Blocks", "Launch Content Blocks", "View Feature Flags", "Edit Feature Flags", "Archive Feature Flags", "View Segments", "Edit Segments", "View Banner Templates", "Edit Banner Templates", "View Email Templates", "Edit Email Templates", "View Media Library Assets", "Edit Media Library Assets", "Delete Media Library Assets", "View Locations", "Edit Locations", "Archive Locations", "View Promotion Codes", "Edit Promotion Codes", "Export Promotion Codes", "View Preference Centers", "Edit Preference Centers". |
| Marketer - Skincare Brands | {::nomarkdown}[DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | "View Campaigns", "Edit Campaigns", "Archive Campaigns", "View Canvases", "Edit Canvases", "Archive Canvases", "View Content Blocks", "Edit Content Blocks", "Archive Content Blocks", "Launch Content Blocks", "View Feature Flags", "Edit Feature Flags", "Archive Feature Flags", "View Segments", "Edit Segments", "View Banner Templates", "Edit Banner Templates", "View Email Templates", "Edit Email Templates", "View Media Library Assets", "Edit Media Library Assets", "Delete Media Library Assets", "View Locations", "Edit Locations", "Archive Locations", "View Promotion Codes", "Edit Promotion Codes", "Export Promotion Codes", "View Preference Centers", "Edit Preference Centers". |
| User Management - All Brands | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand, [DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | "Edit Dashboard Users", "View Teams", "Edit Teams", "Archive Teams" |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="역할 예시" }
{% endtab %}
{% endtabs %}

## 권한 세트와 역할은 Teams와 어떻게 다른가요? {#how-do-permission-sets-and-roles-differ-from-teams}

{% multi_lang_include permissions/differences.md content="Differences" %}

### Teams에 사용자 권한을 추가할 때 고려 사항 {#considerations-for-adding-user-permissions-to-teams}

Braze 대시보드에서 권한을 저장할 때, 특히 워크스페이스에서 사용자를 추가하거나 제거하거나 Team에 추가할 때 어려움이 발생할 수 있습니다. 사용자의 권한이 워크스페이스 수준에서 이미 가지고 있는 권한과 동일한 경우 **사용자 저장/업데이트** 버튼이 회색으로 비활성화될 수 있습니다. 이 제한은 모든 사용자가 전체 워크스페이스와 동일한 권한을 가지고 있다면 Team을 사용하는 이점이 없기 때문에 존재합니다.

사용자를 동일한 권한을 유지하면서 Team에 성공적으로 추가하려면, 워크스페이스 수준에서는 권한을 할당하지 마세요. 대신 팀 수준에서만 권한을 할당하세요.

## 제한된 사용자 {#limited-users}

제한된 사용자는 회사 관리자 및 워크스페이스 관리자에 비해 제한이 있지만, Braze 대시보드의 특정 측면을 관리할 수 있는 특정 권한을 가지고 있습니다.

| 범위 | 설명 |
| --- | --- |
| 권한 | 제한된 사용자는 "Edit Dashboard Users" 권한이 있는 경우 다른 제한된 사용자의 권한을 편집할 수 있습니다. 또한 새로운 제한된 사용자를 생성하고 권한 세트를 수정할 수 있습니다. 그러나 회사 관리자 계정을 생성하거나 관리할 수는 없습니다. |
| 역할 제한 | 제한된 사용자가 "Workspace Admin"을 제외한 모든 권한을 가지고 있더라도, 워크스페이스 관리자에게 일반적으로 부여되는 다른 모든 권한에는 접근할 수 있습니다. |
| 권한 가시성 | 제한된 사용자가 하나의 워크스페이스(예: Dev)에 대해 "Edit Dashboard Users" 권한을 가지고 있지만 다른 워크스페이스(예: Prod)에 대해서는 가지고 있지 않은 경우, 대시보드 사용자 세부 정보 페이지에서 Prod 워크스페이스 권한을 볼 수 없습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="제한된 사용자의 권한" }

### 제한된 사용자 비교 {#compare-limited-users}

| 제한된 사용자 유형 | 설명 |
| --- | --- |
| 워크스페이스 관리자 | 워크스페이스 관리자는 워크스페이스 관리에 특화된 권한을 가지지만, 회사 관리자와 동일한 권한은 없습니다. 제한된 사용자는 필요한 권한이 체크되어 있으면 워크스페이스 관리자와 유사한 권한을 상속받을 수 있습니다. |
| 관리자(회사 관리자) | 회사 관리자는 대시보드 사용자를 삭제하는 기능을 포함하여 더 넓은 권한을 가집니다. 그러나 자신의 계정은 삭제할 수 없으며, 해당 작업을 위해 다른 회사 관리자에게 연락해야 합니다. |
| 보기 전용 접근 | Campaigns 페이지와 같은 대시보드의 일부에 접근하려면 사용자에게 보기 권한이 할당되어 있어야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="제한된 사용자 비교" }

### 제한된 접근 오류 {#limited-access-error}

사용자가 "이 페이지에 접근하려면 'View Landing Pages' 권한이 필요합니다"와 같은 메시지를 볼 수 있습니다. 이 경우 사용자와 계정 관리자가 필요한 권한이 부여되었는지 확인해야 합니다. 권한이 부여되어 있다면, 사용자의 권한을 비활성화한 후 다시 활성화하여 문제를 해결해 보세요.

{% alert note %}
한 대시보드 사용자의 사용자 권한을 다른 사용자에게 병합하거나 가져오는 것은 불가능합니다.
{% endalert %}

## 사용자 권한의 세부 사항 {#nuances-of-user-permissions}

대시보드 접근 권한을 할당할 때 다음 동작을 유의하세요:

- **워크스페이스 관리자 vs 회사 관리자:** 워크스페이스 관리자는 할당된 워크스페이스 내에서 권한을 관리합니다. 회사 관리자는 다른 대시보드 사용자를 삭제하는 것을 포함하여 회사 전체에 대한 권한을 가집니다.
- **제한된 사용자:** "Edit Dashboard Users" 권한이 있는 제한된 사용자는 다른 제한된 사용자를 관리할 수 있지만, 회사 관리자 계정을 생성하거나 관리할 수는 없습니다.
- **대시보드 사용자 관리 범위:** 사용자 세부 정보 페이지에서는 편집자가 접근할 수 있는 워크스페이스의 권한만 표시됩니다. 하나의 워크스페이스에서 사용자를 편집할 수 있는 제한된 사용자는 다른 워크스페이스의 권한 체크박스를 볼 수 없을 수 있습니다.
- **사용자 데이터 내보내기:** 사용자 데이터를 내보내려면 내보내기 권한 외에 워크스페이스 수준 접근 권한이 필요합니다.
- **복합 권한:** 일부 영역에는 여러 권한이 필요합니다. 예를 들어, [기술 파트너]({{site.baseurl}}/partners)를 구성하려면 일반적으로 파트너 접근 권한과 관련 워크스페이스 기능에 대한 기본 읽기 권한이 모두 필요합니다.
- **사용자 데이터 가져오기 및 업데이트:** 이 권한에는 대시보드 사용자 레코드뿐만 아니라 가져오기 플로우를 통해 앱 사용자 프로필을 편집하는 기능도 포함됩니다.

## 사용자 권한 편집 {#edit-a-users-permissions}

사용자의 현재 관리자, 회사 또는 워크스페이스 권한을 편집하려면 **설정** > **사용자 관리** > **회사 사용자**로 이동한 다음 해당 사용자의 이름을 선택합니다.

![대시보드 사용자 테이블이 표시된 Braze의 "회사 사용자" 페이지]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %})

{% tabs local %}
{% tab 관리자 %}

### 관리자 {#admin}

관리자는 모든 기능에 접근할 수 있으며 모든 회사 설정을 수정할 수 있습니다. 관리자는 다음을 수행할 수 있습니다:

- [승인 설정]({{site.baseurl}}/user_guide/messaging/governance/approvals#turning-on-the-approval-workflow) 변경
- 다른 [Braze 사용자]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users#adding-company-users) 추가, 편집, 삭제, 일시 중지 또는 일시 중지 해제
- Braze 사용자를 CSV로 내보내기

관리자 권한을 부여하거나 제거하려면 **This user is an admin**을 선택한 다음 **Update user**를 선택합니다.

{% alert warning %}
사용자에게서 관리자 권한을 제거하면, 최소 하나의 [회사 수준 또는 워크스페이스 수준 권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions?tab=company&sdktab=granular%20permissions#granularpermissions_editing-a-users-permissions)을 할당하기 전까지 해당 사용자는 Braze에 접근할 수 없습니다.
{% endalert %}

{% endtab %}
{% tab 회사 %}

### 회사 {#company}

사용자의 다음 회사 수준 권한을 관리하려면 해당 권한 옆의 체크박스를 선택하거나 해제합니다. 완료되면 **Update user**를 선택합니다.

| 권한 이름 | 설명 |
|----------|-----------|
| Manage company settings | 사용자가 권한 설정 및 발신자 인증을 수정할 수 있습니다. |
| Create and delete workspaces | 사용자가 워크스페이스를 생성하고 삭제할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="회사 수준 권한" }

{% endtab %}
{% tab 워크스페이스 %}

### 워크스페이스 {#workspace}

Braze에서 사용자가 속한 각 워크스페이스에 대해 서로 다른 권한을 부여할 수 있습니다. 워크스페이스 수준 권한을 관리하려면 **Select workspaces and permissions**를 선택한 다음 수동으로 권한을 선택하거나 이전에 생성한 [권한 세트 또는 역할]({{site.baseurl}}/user_guide/administer/global/user_management/permissions?sdktab=granular%20permissions#granularpermissions_creating-a-permission-set)을 할당합니다. 서로 다른 워크스페이스에 대해 다른 권한을 부여해야 하는 경우 필요한 만큼 이 과정을 반복합니다. 각 권한에 대한 설명은 [권한 목록]({{site.baseurl}}/user_guide/administer/global/user_management/permissions?sdktab=granular%20permissions#granularpermissions_list-of-permissions)을 참조하세요.

{% subtabs %}
{% subtab 수동 선택 %}

**Workspaces**에서 드롭다운으로 하나 이상의 워크스페이스를 선택합니다. 그런 다음 **Permissions**에서 하나 이상의 권한을 선택합니다. 선택한 워크스페이스에 대해서만 이 권한이 할당됩니다. 선택적으로, 이 워크스페이스에 대한 전체 권한을 부여하려면 **Assign workspace admin access**를 선택할 수 있습니다.

완료되면 **Update user**를 선택합니다.

![Braze에서 워크스페이스 수준 권한을 수동으로 선택하는 화면]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})

{% endsubtab %}
{% subtab 권한 세트 할당 %}

**Workspaces**에서 드롭다운으로 하나 이상의 워크스페이스를 선택합니다. 그런 다음 **Permission Sets**에서 하나의 권한 세트를 선택합니다. 선택한 워크스페이스에 대해서만 이 권한이 할당됩니다.

완료되면 **Update user**를 선택합니다.

![Braze에서 권한 세트를 통해 워크스페이스 수준 권한을 할당하는 화면]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})

{% endsubtab %}
{% subtab 역할 할당 %}

**Workspaces**에서 드롭다운으로 하나 이상의 워크스페이스를 선택합니다. 그런 다음 **Role**에서 하나의 역할을 선택합니다. 선택한 워크스페이스에 대해서만 이 권한이 할당됩니다.

완료되면 **Update user**를 선택합니다.

![Braze에서 역할을 통해 워크스페이스 수준 권한을 할당하는 화면]({% image_buster /assets/img/braze_permissions/workspace_level_role.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 사용자 권한 내보내기 {#exporting-user-permissions}

사용자 및 권한 목록을 다운로드하려면 **설정** > **사용자 관리** > **회사 사용자**로 이동한 다음 **Export Users**를 선택합니다. 잠시 후 CSV 파일이 이메일 주소로 전송됩니다.

## 권한 목록 {#list-of-permissions}

### 메시징 {#messaging}

| 제품 영역 | 권한 | 정의 |
| --- | --- | --- |
| Campaigns | View Campaigns | Campaign(캠페인) 보기 |
| Campaigns | Launch Campaigns | 기존 Campaign 시작, 중지, 일시 중지 또는 재개 |
| Campaigns | Archive Campaigns | Campaign을 아카이브로 이동 |
| Campaigns | Edit Campaigns | Campaign 생성 및 업데이트 |
| Campaigns | Approve and Deny Campaigns | Campaign 승인 또는 거부. [Campaign 승인 워크플로우]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals)가 활성화되어 있어야 이 권한이 적용됩니다. 이 설정은 현재 얼리 액세스 중입니다. 얼리 액세스 참여에 관심이 있으시면 계정 매니저에게 문의하세요. |
| Canvas | View Canvases | Canvases 보기 |
| Canvas | Archive Canvases | Canvases를 아카이브로 이동 |
| Canvas | Edit Canvases | Canvases 생성 및 업데이트 |
| Canvas | Launch Canvases | 기존 Canvases 시작, 중지, 일시 중지 또는 재개 |
| Canvas | Approve and Deny Canvases | Canvases 승인 또는 거부. [Canvases 승인 워크플로우]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals)가 활성화되어 있어야 이 권한이 적용됩니다. 이 설정은 현재 얼리 액세스 중입니다. 얼리 액세스 참여에 관심이 있으시면 계정 매니저에게 문의하세요. |
| 기능 플래그 | View Feature Flags | 기능 플래그 보기 |
| 기능 플래그 | Archive Feature Flags | 기능 플래그를 아카이브로 이동 |
| 기능 플래그 | Edit Feature Flags | 기능 플래그 생성 및 업데이트 |
| 최대 게재빈도 설정 | View Frequency Capping Rules | 최대 게재빈도 설정 규칙 보기 |
| 최대 게재빈도 설정 | Edit Frequency Capping Rules | 최대 게재빈도 설정 규칙 생성 및 업데이트 |
| 랜딩 페이지 | View Landing Pages | 랜딩 페이지 보기 |
| 랜딩 페이지 | Publish Landing Pages | 임시 저장된 랜딩 페이지를 활성화 |
| 랜딩 페이지 | Edit Landing Page Drafts | 랜딩 페이지 임시 저장본 생성 및 저장 |
| 메시지 아카이브 설정 | View Message Archiving Settings | 변경 없이 메시지 아카이브 설정 보기 |
| 메시지 아카이브 설정 | Edit Message Archiving Settings | 메시지 아카이브 설정 생성 및 업데이트 |
| 메시지 우선순위 | View Message Prioritization | 변경 없이 메시지 우선순위 설정 보기 |
| 메시지 우선순위 | Edit Message Prioritization | 메시지 우선순위 설정 생성 및 업데이트 |
| WhatsApp Flows | View WhatsApp Flows | 모든 WhatsApp Flows 보기 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="메시징 권한" }

### 오디언스 {#audience}

| 제품 영역 | 권한 | 정의 |
| --- | --- | --- |
| 글로벌 컨트롤 그룹 | View Global Control Group | 글로벌 컨트롤 그룹 설정 페이지 보기 |
| 글로벌 컨트롤 그룹 | Edit Global Control Group | 글로벌 컨트롤 그룹 생성 및 변경 사항 저장. "Edit Global Control Group" 권한이 있는 사용자는 "Edit Campaigns" 및 "Edit Canvases" 권한도 부여받아야 합니다. "Edit Global Control Group" 권한이 있는 사용자에게는 "View Global Control Group" 권한도 부여됩니다. |
| 위치 | Archive Locations | 위치를 아카이브로 이동 |
| 위치 | View Locations | 위치 보기 |
| 위치 | Edit Locations | 위치 생성 및 편집 |
| Segments | View Segments | Segments 보기. "Edit Segments" 또는 "Archive Segments" 권한을 가지려면 "View Segments" 권한이 있어야 합니다 |
| Segments | Archive Segments | Segments 아카이브 및 아카이브 해제. "Archive Segments" 권한이 있는 사용자는 "View Segments" 권한도 부여받아야 합니다 |
| Segments | Edit Segments | Segments 생성 및 업데이트. "Edit Segments" 권한이 있는 사용자는 "View Segments" 권한도 부여받아야 합니다 |
| 사용자 데이터 | View Import Users | 변경 없이 CSV 사용자 가져오기 보기 |
| 사용자 데이터 | Import Users | 대시보드에 사용자 업로드 |
| 사용자 데이터 | Edit User Data | 사용자 데이터 생성 및 업데이트 |
| 사용자 데이터 | Export User Data | 대시보드에서 사용자 다운로드 |
| 중복 사용자 | View User Merge Records | 사용자 병합 기록 목록 보기 |
| 사용자 | View User Profiles (PII Redacted) | PII 준수 방식으로 고객 프로필 보기 |
| 사용자 | View User Event Properties | 고객 프로필의 **이벤트 기록** 탭에서 이벤트 속성정보 보기 |
| 중복 사용자 | Merge Duplicate Users | 중복 사용자를 하나의 사용자로 결합. 병합 후 중복 항목은 제거됩니다 |
| 사용자 삭제 | View User Deletion Records | 사용자 삭제 기록 목록 보기 |
| 사용자 삭제 | Delete Users | 대시보드에서 사용자를 개별 또는 일괄로 영구 삭제 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="오디언스 권한" }

### 템플릿 {#template}

| 제품 영역 | 권한 | 정의 |
| --- | --- | --- |
| 배너 템플릿 | View Banner Templates | 배너 템플릿 보기 |
| 배너 템플릿 | Archive Banner Templates | 배너 템플릿을 아카이브로 이동 |
| 배너 템플릿 | Edit Banner Templates | 배너 템플릿 생성 및 업데이트 |
| Canvas 템플릿 | View Canvas Templates | Canvas 템플릿 보기 |
| Canvas 템플릿 | Archive Canvas Templates | Canvas 템플릿을 아카이브로 이동 |
| Canvas 템플릿 | Create and Edit Canvas Templates | Canvas 템플릿 생성 및 업데이트 |
| Content Blocks | View Content Blocks | Content Blocks 보기 |
| Content Blocks | Launch Content Blocks | 임시 저장된 Content Blocks 게시, 시작된 Content Blocks 편집, 아카이브 및 아카이브 해제 |
| Content Blocks | Archive Content Blocks | Content Blocks를 아카이브로 이동 |
| Content Blocks | Edit Content Blocks | Content Blocks 생성 및 임시 저장된 Content Blocks 편집 |
| 이메일 링크 템플릿 | View Email Link Templates | 변경 없이 링크 템플릿 보기 |
| 이메일 링크 템플릿 | Edit Email Link Templates | 링크 템플릿 생성 및 업데이트 |
| 이메일 템플릿 | View Email Templates | 이메일 템플릿 보기 |
| 이메일 템플릿 | Archive Email Templates | 이메일 템플릿을 아카이브로 이동 |
| 이메일 템플릿 | Edit Email Templates | 이메일 템플릿 생성 및 업데이트 |
| IAM 템플릿 | View IAM Templates | 변경 없이 인앱 메시지 템플릿 보기 |
| IAM 템플릿 | Archive IAM Templates | IAM 템플릿을 아카이브로 이동 |
| IAM 템플릿 | Edit IAM Templates | 인앱 메시지 템플릿 생성 및 업데이트 |
| 랜딩 페이지 템플릿 | View Landing Page Templates | 랜딩 페이지 템플릿 보기 |
| 랜딩 페이지 템플릿 | Archive Landing Page Template | 랜딩 페이지 템플릿을 아카이브로 이동 |
| 랜딩 페이지 템플릿 | Edit Landing Page Templates | 랜딩 페이지 템플릿 생성 및 업데이트 |
| 웹훅 템플릿 | View Webhook Templates | 변경 없이 웹훅 템플릿 보기 |
| 웹훅 템플릿 | Archive Webhook Templates | 웹훅 템플릿을 아카이브로 이동 |
| 웹훅 템플릿 | Edit Webhook Templates | 웹훅 템플릿 생성 및 업데이트 |
| WhatsApp 메시지 템플릿 | View WhatsApp Message Templates | 사용자가 [WhatsApp 메시지 템플릿]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#step-2-compose-your-whatsapp-message)을 볼 수 있습니다 |
| WhatsApp 메시지 템플릿 | Edit WhatsApp Message Templates | 사용자가 템플릿 빌더에서 WhatsApp 메시지 템플릿을 생성할 수 있습니다. 이 기능은 현재 얼리 액세스 중입니다. |
| Meta의 WhatsApp 메시지 템플릿 | View WhatsApp Message Templates From Meta | 모든 WhatsApp 템플릿 보기 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="템플릿 권한" }

### 파트너 통합 {#partner-integrations}

| 제품 영역 | 권한 | 정의 |
| --- | --- | --- |
| Currents 통합 | View Currents Integration | Currents 통합 보기 |
| Currents 통합 | Edit Currents Integrations | Currents 통합 생성, 업데이트 및 삭제 |
| 기술 파트너 | Edit Technology Partners | 기술 파트너 생성 및 업데이트 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="파트너 통합 권한" }

### 데이터 설정 {#data-settings}

| 제품 영역 | 권한 | 정의 |
| --- | --- | --- |
| 카탈로그 | View Catalogs | 카탈로그 및 선택 항목 보기 |
| 카탈로그 | Delete Catalogs | 카탈로그 영구 삭제 |
| 카탈로그 | Export Catalogs | 대시보드에서 카탈로그 다운로드 |
| 카탈로그 | Edit Catalogs | 카탈로그 및 선택 항목 생성 및 업데이트 |
| 클라우드 데이터 수집 | Edit Cloud Data Ingestion | 소스 및 동기화 생성, 업데이트 및 삭제 |
| 커스텀 속성 | View Custom Attributes | 커스텀 속성 및 사용 보고서 보기 |
| 커스텀 속성 | Export Custom Attributes | 대시보드에서 커스텀 속성 다운로드 |
| 커스텀 속성 | Delete Custom Attributes | 커스텀 속성 영구 삭제 |
| 커스텀 속성 | Blocklist Custom Attributes | 대시보드에서 사용을 제한하는 차단 목록에 커스텀 속성 추가 |
| 커스텀 속성 | Edit Custom Attributes | 커스텀 속성 생성 및 업데이트 |
| 커스텀 이벤트 속성정보 세분화 | Edit Custom Event Property Segmentation | 커스텀 이벤트 속성정보에 대한 세분화 활성화 및 비활성화 |
| 커스텀 이벤트 | View Custom Events | 커스텀 이벤트 및 사용 보고서 보기, 일일 분석 보고서 이메일에 커스텀 이벤트 추가 |
| 커스텀 이벤트 | Export Custom Events | 대시보드에서 커스텀 이벤트 다운로드 |
| PII | View PII | PII 보기 |
| 커스텀 이벤트 | Delete Custom Events | 커스텀 이벤트 영구 삭제 |
| 커스텀 이벤트 | Blocklist Custom Events | 대시보드에서 사용을 제한하는 차단 목록에 커스텀 이벤트 추가 |
| 커스텀 이벤트 | Edit Custom Events | 커스텀 이벤트 생성 및 업데이트 |
| 제품 | View Products | 제품 보기 |
| 제품 | Blocklist Products | 대시보드에서 사용을 제한하는 차단 목록에 제품 추가 |
| 제품 | Edit Products | 제품 생성 및 업데이트 |
| 구매 속성정보 세분화 | Edit Purchase Property Segmentation | 구매 이벤트 속성정보에 대한 세분화 활성화 및 비활성화 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="데이터 설정 권한" }

### 설정 {#settings}

| 제품 영역 | 권한 | 정의 |
| --- | --- | --- |
| API 식별자 | View API identifiers | API 식별자 및 기타 식별자 보기 |
| API 키 | View API Keys | API 키 보기 |
| API 키 | Edit API Keys | API 키 생성 및 업데이트 |
| API 제한 | View API Limits | API 사용량 제한 보기 |
| API 사용 알림 | View API Usage Alerts | API 사용 알림 보기 |
| API 사용 알림 | Edit API Usage Alerts | API 사용 알림 생성 및 업데이트 |
| API 사용 데이터 | View API Usage Dashboard | API 사용 대시보드 보기 |
| 앱 설정 | Edit App Settings | 앱 설정 내에서 앱 생성, 편집 및 업데이트 |
| 앱 설정 | View App Settings | 앱 설정 페이지 보기 |
| 오디언스 동기화 설정 | View Audience Sync Settings | 연결된 오디언스 동기화 파트너의 모든 설정 보기 |
| 대시보드 사용자 | Edit Dashboard Users | 회사 사용자 보기, 생성 및 편집 |
| 이메일 설정 | View Email Settings | 이메일 환경설정 보기 |
| 이메일 설정 | Edit Email Settings | 이메일 환경설정 활성화 및 업데이트 |
| 이벤트 사용자 로그 | View Event User Log | 이벤트 사용자 로그 보기 |
| 내부 그룹 | View Internal User Groups | 내부 그룹 보기 |
| 내부 그룹 | Delete Internal User Groups | 내부 그룹 삭제 |
| 내부 그룹 | Edit Internal User Groups | 내부 그룹 생성 및 업데이트 |
| 메시지 활동 로그 | View Message Activity Log | 메시지 활동 로그 보기 |
| 다국어 설정 | View Localization Settings | 다국어 로케일 설정 페이지 보기 |
| 다국어 설정 | Delete Localization Settings | 다국어 로케일 삭제 |
| 다국어 설정 | Edit Localization Settings | 다국어 로케일 생성 |
| 환경설정 센터 | View Preference Centers | 환경설정 센터 보기 |
| 환경설정 센터 | Edit Preference Centers | 환경설정 센터 생성 및 업데이트 |
| 환경설정 센터 | Launch Preference Centers | 임시 저장된 환경설정 센터를 활성화하거나 기존 환경설정 센터를 업데이트 |
| 푸시 설정 | View Push Settings | 푸시 설정 보기 |
| 푸시 설정 | Edit Push Settings | 푸시 설정 생성 및 업데이트 |
| SDK 디버거 | View SDK Debugger | SDK 디버거 또는 디버깅 세션 보기 |
| SDK 디버거 | Edit SDK Debugger | SDK 디버거 세션 생성 및 다운로드 |
| 태그 | View Tags | 태그 보기 |
| 태그 | Delete Tags | 태그 영구 삭제 |
| 태그 | Edit Tags | 태그 생성 및 업데이트 |
| Teams | View Teams | Teams 보기 |
| Teams | Archive Teams | Teams를 아카이브로 이동 |
| Teams | Edit Teams | Teams 생성 및 업데이트 |
| WhatsApp 설정 | View WhatsApp Settings | 모든 WhatsApp 채널 설정 보기 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="설정 권한" }

### Decisioning Studio

| 제품 영역 | 권한 | 정의 |
| --- | --- | --- |
| Decisioning Studio 에이전트 | View Decisioning Studio Agent | 변경 없이 Decisioning Studio 에이전트 구성 보기 |
| Decisioning Studio 오디언스 | View Decisioning Studio Audience | Decisioning Studio 에이전트 구성 요약에서 오디언스 세부 정보 보기 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Decisioning Studio 권한" }

### 기타 {#other}

| 제품 영역 | 권한 | 정의 |
| --- | --- | --- |
| 앱 사용량 | View Usage Data | 사용량 데이터 보기 |
| 청구 | View Billing Details | 청구 세부 정보 보기 |
| 커스텀 에이전트 | View Agent Console AI Agents | 사용자가 커스텀 AI 에이전트를 볼 수 있습니다 |
| 커스텀 에이전트 | Archive Agent Console AI Agents | 사용자가 커스텀 AI 에이전트를 아카이브할 수 있습니다 |
| 커스텀 에이전트 | Edit Agent Console AI Agents | 사용자가 커스텀 AI 에이전트를 생성하고 업데이트할 수 있습니다 |
| PII로 표시된 커스텀 속성 | View Custom Attributes Marked as PII | PII로 표시된 커스텀 속성 보기 |
| 대시보드 보고서 | View Dashboard Reports | 변경 없이 보고서 보기 |
| 대시보드 보고서 | Delete Dashboard Reports | 보고서 영구 삭제 |
| 대시보드 보고서 | Edit Dashboard Reports | 보고서 생성 및 업데이트 |
| 도메인 설정 | Edit Domain Settings | 확인된 도메인에서 위임된 도메인 및 커스텀 도메인 추가 |
| 필드 수준 암호화 | Edit Identifier Field-Level Encryption | 필드 수준 암호화 설정 활성화 및 업데이트 |
| 미디어 라이브러리 자산 | View Media Library Assets | 미디어 라이브러리 자산 보기 |
| 미디어 라이브러리 자산 | Delete Media Library Assets | 미디어 라이브러리 자산 영구 삭제 |
| 미디어 라이브러리 자산 | Edit Media Library Assets | 미디어 라이브러리 자산 생성 및 업데이트 |
| 미디어 라이브러리 자산 | Replace Media Library Assets | 기존 미디어 라이브러리 자산의 파일을 URL 및 자산 ID를 유지하면서 교체 |
| 메시징 사용량 제한 | View Messaging Rate Limits | 워크스페이스 수준 메시징 사용량 제한 보기 |
| 메시징 사용량 제한 | Edit Messaging Rate Limits | 워크스페이스 수준 메시징 사용량 제한 구성 및 편집 |
| Operator | Use BrazeAI Operator<sup>TM</sup> | Braze Operator에 접근하여 질문에 답하고, 설정을 안내하고, 문제를 해결하고, 아이디어를 브레인스토밍합니다 |
| 배치 | View Placements | 배너 배치 보기 |
| 배치 | Archive Placements | 배너 배치를 아카이브로 이동 |
| 배치 | Edit Placements | 변경 없이 배너 배치 보기 |
| 프로모션 코드 | View Promotion Codes | 프로모션 코드 보기 |
| 프로모션 코드 | Export Promotion Codes | 대시보드에서 프로모션 코드 목록 다운로드 |
| 프로모션 코드 | Edit Promotion Codes | 프로모션 코드 생성 및 업데이트 |
| 구독 그룹 | Edit Subscriptions | 구독 그룹 생성 및 업데이트 |
| 데이터 변환 | Edit Data Transformation | 데이터 변환 생성 및 업데이트 |
| 데이터 변환 | View Data Transformation | 데이터 변환 보기 |
| 고객지원 티켓 | Create Support Ticket | 고객지원 티켓 생성 및 업데이트 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="기타 권한" }