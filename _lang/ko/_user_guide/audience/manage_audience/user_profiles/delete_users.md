---
nav_title: 사용자 삭제
article_title: 사용자 삭제
page_order: 6
toc_headers: h2
description: "Braze 대시보드를 통해 개별 사용자 또는 Segment의 사용자를 직접 삭제하는 방법을 알아보세요."
alias: /delete_users/
---

# 사용자 삭제 {#delete-users}

> Braze 대시보드를 통해 개별 사용자 또는 Segment의 사용자를 직접 삭제하는 방법을 알아보세요.

{% alert important %}
사용자 삭제는 현재 얼리 액세스 중입니다. 참여에 관심이 있으시면 고객 성공 매니저에게 문의하세요.
{% endalert %}

## 필수 조건 {#prerequisites}

사용자를 삭제하려면 관리자이거나 **Delete Users** 권한이 있어야 합니다. 사용자 삭제 기록을 보려면 관리자이거나 **View User Deletion Records** 권한이 있어야 합니다. 다음 권한이 사용자 삭제 및 삭제 기록을 제어합니다:

| 권한 | 설명 |
|------------|-------------|
| Delete Users | 사용자를 개별적으로 또는 일괄적으로 영구 삭제합니다. |
| View User Deletion Records | 사용자 삭제 기록을 조회합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 사용자 삭제에 대해 {#about-user-deletion}

사용자 삭제를 통해 더 이상 필요하지 않거나, 오류로 생성되었거나, 규정 준수(예: GDPR 또는 CCPA)를 위해 삭제해야 하는 프로필을 제거하여 데이터베이스를 관리할 수 있습니다.

| 고려 사항 | 세부 정보 |
|---------------|---------|
| 최대 크기 | Segment 삭제 시 최대 1억 개의 사용자 프로필을 삭제할 수 있습니다. |
| 대기 기간 | 모든 Segment 삭제에는 7일의 대기 기간과 삭제 처리에 소요되는 시간이 필요합니다. |
| 작업 제한 | 한 번에 하나의 Segment만 삭제할 수 있으며, 여기에는 7일의 대기 기간이 포함됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="About user deletion" }

## 사용자 삭제하기 {#deleting-users}

Braze 대시보드를 통해 [개별 사용자](#delete-individual) 또는 [Segment의 사용자](#delete-segment)를 삭제할 수 있습니다:

### 개별 사용자 삭제 {#delete-individual}

Braze에서 개별 사용자를 삭제하려면 **Audience** > **Search Users**로 이동한 다음 사용자를 검색하고 선택합니다. 중복 사용자 프로필을 삭제하는 경우 올바른 프로필을 선택했는지 확인하세요.

![Braze의 'Search Users' 페이지.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:75%;"}

{% alert warning %}
단일 사용자 삭제는 영구적입니다. 삭제된 프로필은 복구할 수 없습니다.
{% endalert %}

프로필 페이지에서 <i class="fa-solid fa-ellipsis-vertical"></i> **Show options** > **Delete User**를 선택합니다. 사용자가 Braze에서 완전히 삭제되기까지 몇 분이 소요될 수 있습니다.

![세로 줄임표 메뉴가 열려 있고 사용자 삭제 옵션이 표시된 Braze의 사용자.]({% image_buster /assets/img/audience_management/deleting_users/delete_user.png %}){: style="max-width:85%;"}

### Segment 삭제 {#delete-segment}

아직 하지 않았다면, 삭제하려는 사용자 프로필이 포함된 [Segment를 생성]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/)하세요. 중복 사용자를 삭제하는 경우 모든 사용자 프로필을 포함해야 합니다.

Braze에서 **Audience** > **Manage Audience**로 이동한 다음 **Delete Users** 탭을 선택합니다.

![Braze 대시보드의 'Manage Audience' 섹션에 있는 'Delete Users' 탭.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

**Delete users**를 선택하고, 삭제할 Segment를 선택한 다음 **Next**를 선택합니다.

![삭제할 Segment가 선택된 팝업 창.]({% image_buster /assets/img/audience_management/deleting_users/choose_segment_to_delete.png %}){: style="max-width:75%;"}

요청을 확인하기 위해 **DELETE**를 입력한 다음 **Delete users**를 선택합니다.

![확인 상자에 'DELETE'가 입력된 확인 페이지.]({% image_buster /assets/img/audience_management/deleting_users/confirm_segment_delete.png %}){: style="max-width:75%;"}

이 Segment의 사용자는 즉시 삭제되지 않습니다. 대신 향후 7일 동안 삭제 대기 상태로 표시됩니다. 이 기간이 지나면 삭제가 진행되며, 완료 시 이메일로 알려드립니다.

{% alert tip %}
Segment 변경과 관계없이 정확히 이 사용자들이 삭제되도록 **Pending Deletion**이라는 Segment 필터가 자동으로 생성됩니다. [이 필터를 사용]({{site.baseurl}}/user_guide/audience/segments/managing_segments/#filters)하여 삭제 대기 상태를 확인할 수 있습니다.
{% endalert %}

## Segment 삭제 확인 {#confirming-segment-deletions}

Braze는 삭제 대기 중인 프로필 수가 포함된 확인 이메일을 발송합니다.

삭제를 계속 진행하려면 Braze에 로그인하여 삭제 요청을 확인하세요.

이메일에 표시된 기간 내에 확인하지 않으면 삭제 요청이 만료되어 진행되지 않습니다.

## Segment 삭제 취소 {#cancel}

대기 중인 Segment 삭제를 취소할 수 있는 기간은 7일입니다. 취소하려면 **Audience** > **Manage Audience**로 이동한 다음 **Delete Users** 탭을 선택합니다.

![Braze 대시보드의 'Manage Audience' 섹션에 있는 'Delete Users' 탭.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

대기 중인 Segment 삭제 옆에 있는 <i class="fa-solid fa-eye"></i>를 선택하여 삭제 기록 세부 정보를 엽니다.

!['Delete Users' 탭에 있는 대기 중인 Segment 삭제.]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

삭제 기록 세부 정보에서 **Cancel deletion**을 선택합니다.

!['Delete Users' 탭의 'Deletion Record Details' 창.]({% image_buster /assets/img/audience_management/deleting_users/deletion_record_details.png %}){: style="max-width:55%;"}

{% alert tip %}
대량 사용자 삭제가 진행 중일 때 언제든지 취소할 수 있습니다. 그러나 취소 전에 이미 삭제된 사용자는 복원할 수 없습니다.
{% endalert %}

## 삭제 상태 확인 {#status}

[Segment 필터](#segment-filters), [오디언스 관리](#manage-audience) 페이지 또는 [보안 이벤트 보고서](#security-event-report)를 사용하여 삭제 상태를 확인할 수 있습니다.

### Segment 필터 {#segment-filters}

사용자 Segment의 삭제를 요청하면 **Pending Deletion**이라는 [Segment 필터]({{site.baseurl}}/user_guide/audience/segments/managing_segments/#filters)가 자동으로 생성됩니다. 이를 사용하여 다음을 수행할 수 있습니다:

- 특정 삭제 실행 날짜에 연결된 정확한 사용자 집합을 확인합니다.
- 해당 사용자를 Campaigns에서 제외하여 제거 전에 메시지를 받지 않도록 합니다.
- 규정 준수 또는 기록 보관을 위해 목록을 내보냅니다.

### 오디언스 관리 {#manage-audience}

{% alert note %}
삭제될 정확한 사용자 목록을 확인하려면 [Pending Deletion Segment 필터](#segment-filters)를 사용하세요.
{% endalert %}

**Audience** > **Manage Audience**로 이동한 다음 **Delete Users** 탭을 선택합니다.

![Braze 대시보드의 'Manage Audience' 섹션에 있는 'Delete Users' 탭.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

이 페이지에서 현재 및 대기 중인 모든 삭제에 대한 다음 일반 정보를 확인할 수 있습니다:

| 필드 | 설명 |
|-------|-------------|
| 요청 날짜 | 요청이 처음 이루어진 날짜입니다. **Pending Deletion** 필터와 함께 사용하여 삭제 대기 중인 프로필 목록을 확인할 수 있습니다. |
| 요청자 | 삭제 요청을 시작한 사용자입니다. |
| Segment 이름 | 삭제 대기 중인 사용자를 선택하는 데 사용된 Segment의 이름입니다. |
| 상태 | 삭제 요청이 대기 중인지, 진행 중인지, 완료되었는지를 표시합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Manage audience" }

특정 요청에 대한 자세한 내용을 보려면 <i class="fa-solid fa-eye"></i>를 선택하여 삭제 기록 세부 정보를 표시합니다. 여기에서 [대기 중인 Segment 삭제를 취소](#cancel)할 수도 있습니다.

!['Delete Users' 탭에 있는 대기 중인 Segment 삭제.]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

### 보안 이벤트 보고서 {#security-event-report}

보안 이벤트 보고서를 다운로드하여 이전 삭제의 상태를 확인할 수도 있습니다. 자세한 내용은 [보안 설정]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings/#security-event-report)을 참조하세요.

## 자주 묻는 질문 {#faq}

### 1억 명 이상의 사용자가 포함된 Segment를 삭제할 수 있나요? {#can-i-delete-segments-with-more-than-100-million-users}

아니요. 1억 명 이상의 사용자가 포함된 Segment는 삭제할 수 없습니다. 이 규모의 Segment를 삭제하는 데 도움이 필요하면 [Braze 고객지원]({{site.baseurl}}/user_guide/administer/personal/braze_support/)에 문의하세요.

### 1억 명의 사용자를 삭제할 수 없고 1천만 명으로 제한되는 것 같습니다. 이것은 버그인가요? {#it-looks-like-i-am-not-able-to-delete-100-million-users-and-am-limited-to-deleting-only-10-million-is-this-a-bug}

아니요, 이것은 버그가 아닙니다. 얼리 액세스(EA) 프로그램 기간 동안 특정 고객은 삭제할 수 있는 사용자 수가 제한됩니다.

EA 프로그램이 진행됨에 따라 모든 고객이 최대 1억 명의 사용자를 삭제할 수 있도록 이 용량이 증가할 예정입니다.

이 용량을 늘리고 싶으시면 Braze 계정 매니저에게 문의하세요. 요청은 제품 팀의 재량에 따라 승인됩니다.

### 자동 사용자 병합이 사용자 삭제에 영향을 미치나요? {#does-automated-user-merging-affect-user-deletion}

예약된 병합에 삭제 대기 중인 사용자 프로필이 포함된 경우, Braze는 해당 프로필을 건너뛰고 병합하지 않습니다. 이러한 프로필을 병합하려면 먼저 삭제에서 제거해야 합니다.

### 삭제 대기 중인 사용자에게 전송된 데이터는 어떻게 되나요? {#what-happens-to-data-sent-to-users-pending-deletion}

외부 시스템이나 SDK에서 전송된 데이터는 여전히 수신되지만, 해당 사용자는 활동과 관계없이 예정대로 삭제됩니다.

### 삭제 대기 중인 사용자에 대해 Canvases와 Campaigns가 트리거되나요? {#do-canvases-and-campaigns-trigger-for-users-pending-deletion}

네. 그러나 Segment 포함 필터를 추가하여 **Pending Deletion** [Segment 필터](#segment-filters)로 모든 사용자를 제외할 수 있습니다.

### 삭제된 사용자 프로필을 복구할 수 있나요? {#can-i-recover-deleted-user-profiles}

개별 사용자 삭제는 영구적입니다.

[Segment 삭제는 취소](#cancel)할 수 있으며, 요청 후 처음 7일 이내에 가능합니다. 그러나 취소 전에 이미 삭제된 사용자는 복원할 수 없습니다.

### 대시보드 대신 API를 사용하여 사용자를 삭제할 수 있나요? {#can-i-delete-users-with-the-api-instead-of-the-dashboard}

네. 소규모 배치의 경우 [`/users/delete` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)를 사용할 수 있으며, 요청당 최대 50개의 식별자를 허용하고 해당 엔드포인트의 [사용량 제한]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/#rate-limit)이 적용됩니다. Segment 기반 대시보드 삭제는 매우 큰 오디언스에 더 적합하지만 [7일 대기 기간](#about-user-deletion)이 포함됩니다.