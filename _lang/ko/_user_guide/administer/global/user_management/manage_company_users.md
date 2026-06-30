---
nav_title: 회사 사용자
article_title: 회사 사용자 관리
page_order: 0
page_type: reference
description: "이 페이지에서는 사용자 추가 및 삭제, 사용자 권한 설정, Teams 생성, 회사 설정 관리 등 회사 사용자를 관리하는 방법을 다룹니다."
---

# 회사 사용자 관리 {#manage-company-users}

> 사용자 추가, 일시 중지, 삭제 등 회사 계정의 사용자를 관리하는 방법을 알아보세요.

## 회사 사용자 추가 {#adding-company-users}

Braze 계정에 사용자를 추가하려면 관리자 권한이 있어야 합니다.

새 사용자를 추가하려면:

1. **설정** > **사용자 관리** > **회사 사용자**로 이동합니다.
2. **+ 새 사용자 추가**를 선택합니다.
3. 이메일, 부서, [사용자 역할]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#creating-a-role) 등 요청된 정보를 입력합니다.
4. 관리자가 아닌 사용자의 경우, 해당 사용자에게 부여할 회사 수준 및 워크스페이스 수준 [권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#editing-a-users-permissions)을 선택합니다.

![커스텀 권한 필드 섹션이 있는 워크스페이스 수준 권한.]({% image_buster /assets/img/add_new_user_3.png %})

### 이메일 주소 요구 사항 {#email-address-requirements}

[인스턴스]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)에서 사용되는 모든 이메일 주소는 고유해야 합니다. 즉, 해당 인스턴스의 회사 워크스페이스에 대한 액세스 권한이 있었거나 현재 있는 사용자와 이미 연결된 이메일 주소를 추가하려고 하면 오류 메시지가 표시됩니다.

팀에서 Gmail을 사용하고 이메일 주소 추가에 문제가 있는 경우, 이메일 주소에 더하기 기호(+)를 추가하여 별칭을 만들 수 있습니다(예: "+1" 또는 "+test"). 예를 들어, `contractor@braze.com`의 별칭을 `contractor+1@braze.com`으로 만들 수 있습니다. `contractor+1@braze.com`으로 보낸 이메일은 여전히 `contractor@braze.com`으로 전달되지만, 별칭은 고유한 이메일 주소로 인식됩니다.

별칭 없이 여러 회사에서 하나의 계정을 사용하려면 [다중 회사 개발자 사용]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account#use-multi-company-developers)을 참조하세요. SSO를 사용하는 경우, 여러 이메일 주소로 등록하기 전에 [싱글 사인온(SSO) 고려 사항]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account#considerations-for-single-sign-on-sso)을 검토하세요.

### Braze 계정의 이메일 주소를 변경할 수 있나요? {#can-i-change-my-braze-accounts-email-address}

보안상의 이유로 사용자는 Braze 계정에 연결된 이메일 주소를 변경할 수 없습니다. 사용자가 이메일 주소를 업데이트하려면 관리자가 원하는 이메일 주소로 [새 계정을 생성](#adding-company-users)해야 합니다.

## 사용자 액세스 및 책임 할당 {#assigning-user-access-and-responsibilities}

{% multi_lang_include permissions/differences.md content="Differences" %}

## 회사 사용자 일시 중지 {#suspending-company-users}

사용자를 일시 중지하면 계정이 비활성 상태가 되어 더 이상 로그인할 수 없지만, 계정과 관련된 데이터는 보존됩니다. 관리자만 회사 사용자를 일시 중지하거나 일시 중지를 해제할 수 있습니다. 일시 중지된 사용자도 Braze에서 알림을 계속 수신할 수 있습니다.

사용자를 일시 중지하려면 **설정** > **사용자 관리** > **회사 사용자**로 이동하여 사용자 이름을 찾고 <i class="fa-solid fa-user-lock"></i> **일시 중지**를 선택합니다.

![사용자를 일시 중지하는 옵션.]({% image_buster /assets/img_archive/suspend_user.png %})

관리자는 목록에서 사용자 이름을 선택하고 하단의 **사용자 일시 중지**를 선택하여 사용자를 일시 중지할 수도 있습니다.

![사용자 세부 정보를 편집할 때 사용자를 일시 중지합니다.]({% image_buster /assets/img_archive/suspend_user2.png %}){: style="max-width:70%;"}

## 회사 사용자 삭제 {#deleting-company-users}

사용자를 삭제하려면 **설정** > **사용자 관리** > **회사 사용자**로 이동하여 사용자 이름을 찾고 <i class="fa fa-trash-can"></i> **사용자 삭제**를 선택합니다.

관리자만 회사 사용자를 삭제할 수 있으며, 회사 사용자는 자신의 계정을 삭제할 수 없습니다. 관리자는 자신의 대시보드 계정을 삭제할 수 없으며, 다른 관리자가 대신 삭제해야 합니다.

![사용자를 삭제합니다.]({% image_buster /assets/img_archive/delete_user_new.png %})

사용자가 삭제되면 Braze는 다음 계정 데이터를 보관하지 않습니다:

- 사용자가 가지고 있던 모든 속성
- 이메일 주소
- 전화번호
- 외부 사용자 ID
- 성별
- 국가
- 언어
- 기타 유사한 데이터

Braze는 다음 계정 데이터를 보관합니다:

- 계정과 관련된 커스텀 속성 또는 테스트 데이터
- 생성한 Campaigns 또는 Canvases(단, **마지막 수정자** 열에 표시되는 것과 같이 사용자 이름은 나타나지 않습니다)

### 대시보드 사용자 삭제의 영향 {#impact-of-deleting-a-dashboard-user}

대시보드 사용자가 삭제되어도 Campaigns, Segments, Canvases 등 대시보드 내에서 생성한 자산에는 큰 영향이 없습니다. 그러나 이러한 자산의 **생성자** 필드에는 삭제된 사용자의 이메일 주소 대신 "null" 값이 표시됩니다.

삭제된 사용자와 동일한 이메일 주소로 새 대시보드 사용자를 생성하더라도, Braze는 삭제된 사용자가 생성한 자산을 새 사용자와 다시 연결하지 않습니다. 새 대시보드 사용자는 처음부터 시작하며, 대시보드의 기존 자산에 대한 생성자로 표시되지 않습니다.

## 문제 해결 {#troubleshooting}

### 사용자 추가 시 "동작을 수행할 수 없습니다" 오류 {#unable-to-perform-action-when-adding-a-user}

대시보드 사용자를 추가할 때 "동작을 수행할 수 없습니다"(또는 유사한) 오류가 발생하는 경우:

- 이메일 주소에서 앞뒤 공백 및 숨겨진 문자를 제거합니다.
- 해당 주소가 조직에서 유효한 이메일 형식인지 확인합니다. 일부 특수 문자는 거부됩니다.
- 동일한 [클러스터]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account)에서 두 명의 대시보드 사용자에게 동일한 이메일을 사용할 수 없습니다. 해당 주소가 이미 해당 클러스터의 다른 워크스페이스에 등록되어 있는 경우, 다른 주소 또는 `user+1@company.com`과 같은 별칭을 사용하세요.

### 사용자를 추가하려고 할 때 "이메일이 이미 사용 중입니다" 오류 {#email-is-already-taken-when-trying-to-add-a-user}

새 사용자를 추가하려고 할 때 이메일이 이미 사용 중이라는 오류가 표시되지만 사용자 목록에서 해당 사용자를 찾을 수 없는 경우, 해당 사용자가 동일한 Braze 대시보드 클러스터의 다른 인스턴스에 존재할 가능성이 높습니다.

이 새 사용자를 생성하려면 다음 중 하나를 수행할 수 있습니다:

1. 다른 인스턴스에서 사용자를 삭제한 후 새 인스턴스에서 생성하거나,
2. 다른 이메일 문자열(예: `testing+01@braze.com`) 또는 다른 이메일 별칭을 사용하여 사용자를 생성합니다.

`testing+01@braze.com`을 사용할 때 받은편지함에서 활성화 메시지를 수신하지 못하는 경우, IT 팀에 해당 종류의 이메일 주소로 메시지를 수신할 수 있는지 확인하세요. 일부 관리자는 `+`가 포함된 이메일 주소로 전송된 메시지를 필터링합니다.

## 다음 단계 {#next-steps}

사용자를 추가한 후 액세스를 관리하세요:

- [권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)을 통해 각 사용자가 대시보드에서 수행할 수 있는 작업을 구성합니다.
- [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams)를 통해 특정 대시보드 오브젝트에 대한 공유 액세스 권한을 가진 그룹으로 사용자를 구성합니다.