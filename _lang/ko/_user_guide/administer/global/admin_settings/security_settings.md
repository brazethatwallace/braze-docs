---
nav_title: 보안 설정
article_title: 보안 설정
page_order: 2
toc_headers: h2
page_type: reference
description: "이 참조 문서에서는 인증 규칙, IP 허용 목록, PII, 2단계 인증(2FA) 등 일반적인 회사 간 보안 설정에 대해 설명합니다."

---

# 보안 설정 {#security-settings}

> 관리자로서 보안은 우선 사항 목록에서 높은 순위를 차지합니다. **보안 설정** 페이지는 인증 규칙, IP 허용 목록 및 2단계 인증을 포함한 일반적인 회사 간 보안 설정을 관리하는 데 도움이 됩니다.

이 페이지에 액세스하려면 **설정** > **관리자 설정** > **보안 설정**으로 이동합니다.

## 인증 규칙 {#authentication-rules}

### 비밀번호 길이 {#password-length}

이 필드를 사용하여 요구되는 최소 비밀번호 길이를 변경합니다. 기본 최소 길이는 8자입니다.

### 비밀번호 복잡도 {#password-complexity}

**복잡한 비밀번호 강제 적용**을 선택하여 비밀번호에 다음 중 적어도 하나를 포함하도록 요구합니다:
- 대문자
- 소문자
- 숫자
- 특수 문자

### 비밀번호 재사용성 {#password-re-usability}

사용자가 비밀번호를 재사용하기 전에 설정해야 하는 새 비밀번호의 최소 개수를 결정합니다. 기본값은 3개입니다.

### 비밀번호 만료 규칙 {#password-expiration-rules}

이 필드를 사용하여 Braze 계정 사용자가 비밀번호를 재설정할 시기를 설정합니다.

### 세션 지속 시간 규칙 {#session-duration-rules}

이 필드를 사용하여 Braze가 세션을 활성 상태로 유지할 기간을 정의합니다. Braze가 세션을 비활성으로 간주한 후(정의된 분 수 동안 활동 없음), Braze는 사용자를 로그아웃합니다. 2단계 인증이 회사에 대해 시행되는 경우 입력할 수 있는 최대 분 수는 10,080(1주와 동일)이며, 그렇지 않으면 최대 세션 기간은 1,440분(24시간과 동일)입니다.

### 싱글 사인온(SSO) 인증 {#single-sign-on-sso-authentication}

사용자가 비밀번호 또는 SSO를 사용하여 로그인하지 못하도록 제한할 수 있습니다.

[SAML SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/)의 경우, 고객은 시행하기 전에 SAML 설정을 구성해야 합니다. 고객이 Google SSO를 사용하는 경우 추가 작업 없이 보안 설정 페이지만 적용하면 됩니다.

## 대시보드 IP 허용 목록 {#dashboard-ip-allowlisting}

표시된 필드를 사용하여 사용자가 계정에 로그인할 수 있는 특정 IP 주소 및 서브넷(예: 회사 네트워크 또는 VPN)을 허용 목록에 추가할 수 있습니다. 쉼표로 구분된 목록에 IP 주소 및 서브넷을 CIDR 범위로 지정하세요. 지정되지 않은 경우 사용자는 모든 IP 주소에서 로그인할 수 있습니다.

## 2단계 인증(2FA) {#two-factor-authentication-2fa}

모든 회사 사용자에게 2단계 인증이 필요합니다. 계정 로그인에 두 번째 수준의 신원 확인을 추가하여 사용자 이름과 비밀번호만 사용하는 것보다 더 안전하게 보호합니다. 대시보드에서 2단계 인증을 지원할 수 없는 경우 고객 성공 매니저에게 문의하세요.

2단계 인증이 켜져 있는 경우:

- 비밀번호 입력 외에도 사용자는 Braze 계정에 로그인할 때 인증 코드를 입력해야 합니다. 코드는 인증 앱, 이메일 또는 SMS를 통해 전송될 수 있습니다.
- **이 계정을 30일 동안 기억** 체크박스가 사용자에게 제공됩니다.

Braze는 2단계 인증을 설정하지 않은 사용자의 Braze 계정을 잠급니다. Braze 계정 사용자는 관리자가 요구하지 않더라도 **계정 설정**에서 직접 2단계 인증을 설정할 수도 있습니다.

페이지를 떠나기 전에 변경 사항을 저장하세요!

### 이 계정을 30일 동안 기억 {#remember-me}

이 기능은 2단계 인증이 켜져 있을 때 사용할 수 있습니다.

**이 계정을 30일 동안 기억**을 선택하면 기기에 쿠키가 저장되어 30일 동안 한 번만 2단계 인증으로 로그인하면 됩니다.

![이 계정을 30일 동안 기억 체크박스]({% image_buster /assets/img/remember_me.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

대시보드 회사 아래에 여러 계정을 가진 고객은 쿠키가 특정 기기에 연결되어 있기 때문에 이 기능을 사용할 때 문제가 발생할 수 있습니다. 사용자가 동일한 기기를 사용하여 여러 계정에 로그인하면 해당 기기에서 이전에 인증된 계정의 쿠키가 교체됩니다. Braze는 하나의 기기가 하나의 계정에 연결되는 것을 기대하며, 하나의 기기로 여러 계정에 연결하는 것은 지원하지 않습니다.

### 사용자 인증 재설정 {#resetting-user-authentication}

2단계 인증으로 로그인하는 데 문제가 있는 경우 회사 관리자에게 2단계 인증 재설정을 요청하세요. 관리자는 다음 단계를 수행할 수 있습니다:

1. **설정** > **회사 사용자**로 이동합니다.
2. 제공된 목록에서 사용자를 선택합니다.
3. **2단계 인증** 아래에서 **재설정**을 선택합니다.

재설정은 인증 앱 문제, 이메일 인증 미전송, SMS 장애 또는 사용자 오류로 인한 로그인 실패 등 일반적인 인증 문제를 해결할 수 있습니다.

### 회사 수준의 2FA 요구 사항 {#requirements-for-2fa-at-the-company-level}

먼저 **회사 설정** > **보안 설정** > **2단계 인증**으로 이동하여 대시보드에서 2FA가 활성화되어 있는지 확인하세요. 토글이 회색이면 회사에 대해 2FA가 켜지지 않은 것이며 모든 회사 사용자에게 필수가 아닙니다.

#### 2FA가 필수가 아닌 경우의 사용자 옵션 {#user-options-when-2fa-isnt-mandatory}

회사 수준에서 2FA가 시행되지 않는 경우 개별 사용자가 계정 설정 페이지에서 직접 2FA를 설정할 수 있습니다. 이 경우 사용자가 설정하지 않아도 계정이 잠기지 않습니다. 사용자 관리 페이지에서 어떤 사용자가 2FA를 활성화했는지 확인할 수 있습니다.

#### 2FA가 필수인 경우의 요구 사항 {#requirements-when-2fa-is-mandatory}

회사 수준에서 2FA가 시행되는 경우 로그인 시 자체 계정에서 2FA를 설정하지 않은 사용자는 대시보드에서 잠깁니다. 사용자는 액세스를 유지하려면 2FA 설정을 완료해야 합니다.

{% alert important %}
2FA는 싱글 사인온(SSO)이 활성화되지 않은 경우에만 모든 회사 사용자에게 필수입니다. SSO가 사용 중인 경우 회사 수준에서 2FA를 시행할 필요가 없습니다.
{% endalert %}

## 수동으로 2FA 설정 {#manually-set-up-2fa}

Braze 계정에서 2단계 인증(2FA)을 수동으로 활성화하려면 다음 단계를 따르세요:

1. Braze에서 글로벌 헤더의 프로필 아이콘을 선택한 다음 **내 계정 관리**를 선택합니다. **2단계 인증** 섹션으로 스크롤한 다음 **설정 시작**을 선택합니다.
2. 로그인 모달에 비밀번호를 입력한 다음 **비밀번호 확인**을 선택합니다.
3. **2단계 인증 설정** 모달에서 전화번호를 입력한 다음 **활성화**를 선택합니다.
4. 이메일 또는 SMS 메시지에서 생성된 7자리 코드를 복사한 다음 Braze로 돌아가서 **2단계 인증 설정** 모달에 붙여넣습니다. **확인**을 선택합니다.
5. (선택 사항) 다음 30일 동안 2FA를 입력하지 않으려면 **이 계정을 30일 동안 기억** 옵션을 활성화합니다.

## 상승된 액세스 {#elevated-access}

상승된 액세스는 Braze 대시보드에서 민감한 작업에 대한 추가 보안 계층을 추가합니다. 활성화되면 사용자는 Segment를 내보내거나 API 키를 보기 전에 계정을 다시 인증해야 합니다. 상승된 액세스를 사용하려면 **설정** > **관리자 설정** > **보안 설정**으로 이동하여 토글을 켭니다.

사용자가 다시 인증할 수 없는 경우 이전 위치로 리디렉션되며 민감한 작업을 계속할 수 없습니다. 성공적으로 다시 인증한 후에는 로그아웃하지 않는 한 다음 1시간 동안 다시 인증할 필요가 없습니다.

![상승된 액세스 토글.]({% image_buster /assets/img/elevated_access.png %})

## 보안 이벤트 보고서 다운로드 {#security-event-report}

보안 이벤트 보고서는 계정 초대, 계정 제거, 실패 및 성공한 로그인 시도 및 기타 활동과 같은 보안 이벤트의 CSV 보고서입니다. 내부 감사를 수행하는 데 사용할 수 있습니다.

이 보고서를 다운로드하려면 다음을 수행하세요:

1. **설정** > **관리자 설정**으로 이동합니다.
2. **보안 설정** 탭을 선택하고 **보안 이벤트 다운로드** 섹션으로 이동합니다.
3. **보고서 다운로드**를 선택합니다.

이 수동 보고서 다운로드에는 계정의 가장 최근 10,000개의 보안 이벤트만 포함됩니다.

이 행 제한 없이 보안 이벤트를 Amazon S3로 내보내려면 [Amazon S3로 보안 이벤트 내보내기]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings/security_export_s3/)를 참조하세요.

{% details 보고되는 보안 이벤트 %}
### 로그인 및 계정 {#login-and-account}
- Signed In
- Failed Login
- Two-Factor Auth Setup Completed
- Two-Factor Auth Reset Completed
- Cleared Developer 2FA
- Added Additional Developer
- Added Account
- Developer Suspended
- Developer Unsuspended
- Developer Updated
- Removed Developer
- Removed Account
- User Subscription Status Updated
- User Updated
- Developer Account Updated

### 상승된 액세스
- Started Elevated Access Flow
- Completed Elevated Access Flow
- Failed 2FA Verification For Elevated Access
- Enabled Elevated Access Enforcement
- Disabled Elevated Access Enforcement

Campaign
- Added Campaign
- Edited Campaign

Canvas
- Added Journey
- Edited Journey

### Segment
- Added Segment
- Edited Segment
- Exported data to CSV
- Exported Segment via API
- Segment Users Deleted
- Cleared Cohort

### REST API 키 {#rest-api-key}
- Added REST API key
- Removed REST API key

### 기본 인증 자격 증명 {#basic-authentication-credential}
- Added Basic Auth credential
- Updated Basic Auth credential
- Removed Basic Auth credential

### 권한 {#permission}
- Cleared Developer 2FA
- Updated Account Permission
- Added Team
- Edited Team
- Archived Team
- Unarchived Team
- Created App Group Permission Set
- Edited App Group Permission Set
- Removed App Group Permission Set
- Created Custom Role
- Updated Custom Role
- Deleted Custom Role

### 회사 설정 {#company-settings}
- Added App Group
- Added App
- Company Settings Changed
- Updated Company Security Settings
- Updated Security Event Cloud Export
- Added Landing Pages Custom Domain
- Removed Landing Pages Custom Domain
- Custom Domain Created
- Custom Domain Deleted
- Enabled Global Control Group
- Disabled Global Control Group
- Updated Global Control Exclusions
- Updated Subscription Group SMS Allow List

### 이메일 템플릿 {#email-template}
- Added Email Template
- Updated Email Template

### 푸시 자격 증명 {#push-credential}
Updated Push Credential
Removed Push Credential

### SDK 디버거 {#sdk-debugger}
- Started SDK Debugger Session
- Exported SDK Debugger Log

### 사용자 {#users}
- Users Deleted
- Users Viewed
- User Import Started
- User Subscription Group Status Updated
- User Deleted
- Single User Deletion Cancelled
- Bulk User Deletion Cancelled

### 카탈로그 {#catalogs}
- Catalog Created
- Catalog Deleted

### Braze Agents
- Created Agent
- Edited Agent

### BrazeAI Operator
- Requested BrazeAI Operator Response
- BrazeAI Operator Responded
{% enddetails %}

## 개인 식별 정보(PII) 보기 {#view-pii}

**PII 보기** 권한은 일부 선택된 회사 사용자만 액세스할 수 있습니다. 기본적으로 모든 관리자는 사용자 권한에서 **PII 보기** 권한이 켜져 있습니다. 이는 회사가 PII로 정의한 모든 표준 및 커스텀 속성을 대시보드 전체에서 볼 수 있음을 의미합니다. 사용자에 대해 이 권한이 꺼져 있으면 해당 사용자는 이러한 속성을 볼 수 없습니다.

{% alert note %}
[쿼리 빌더]({{site.baseurl}}/user_guide/analytics/reports/query_builder/building_queries/)를 사용하려면 **PII 보기** 권한이 필요합니다. 이는 일부 고객 데이터에 직접 액세스할 수 있기 때문입니다.
{% endalert %}

기존 팀 권한 기능에 대해서는 [사용자 권한 설정]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#available-limited-and-team-role-permissions)을 참조하세요.

### PII 정의 {#defining-pii}

{% alert important %}
특정 필드를 PII 필드로 선택하고 정의하는 것은 Braze 대시보드에서 사용자가 볼 수 있는 내용에만 영향을 미치며, 해당 PII 필드의 최종 사용자 데이터가 처리되는 방식에는 영향을 미치지 않습니다.<br><br>[데이터 보존]({{site.baseurl}}/data_retention/)과 관련된 규정을 포함하여 회사에 적용되는 개인정보 보호 규정 및 정책에 맞게 대시보드 설정을 조정하려면 법무팀에 문의하세요.
{% endalert %}

대시보드에서 회사가 PII로 지정하는 필드를 선택할 수 있습니다. 이렇게 하려면 **회사 설정** > **관리자 설정** > **보안 설정**으로 이동합니다.

다음 속성은 PII로 지정하여 **PII 보기** 권한이 없는 회사 사용자에게 숨길 수 있습니다.

#### 잠재적 PII 속성 {#potential-pii-attributes}

| 표준 속성 | 커스텀 속성 |
| ------------------- | ----------------- |
| {::nomarkdown} <ul> <li>이메일 주소 </li> <li> 전화번호 </li> <li> 이름 </li> <li> 성 </li> <li> 성별 </li> <li> 생년월일 </li> <li> 기기 ID </li> <li> 최근 위치 </li> </ul> {:/} | {::nomarkdown} <ul> <li> 모든 커스텀 속성<ul><li>모든 속성을 숨길 필요가 없는 경우 개별 커스텀 속성을 PII로 표시할 수 있습니다.</li></ul></li> </ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 제한된 영역 {#limited-areas}

다음은 모든 필드가 PII로 설정되어 있고 언급된 사용자가 Braze 플랫폼을 사용하는 회사 사용자라고 가정합니다. 또한 "앞서 언급한" 속성은 [잠재적 PII 속성](#potential-pii-attributes) 표의 속성을 의미합니다. 사용자에게서 PII 권한을 제거하면 여기에 나열된 영역 외에도 사용성에 영향을 미칠 수 있습니다.

| 대시보드 탐색 | 결과 | 참고 |
| -------------------- | ------ | ----- |
| 사용자 검색 | 로그인한 사용자는 이메일 주소, 전화번호, 이름 또는 성으로 검색할 수 없습니다: {::nomarkdown} <ul> <li> 고객 프로필을 볼 때 앞서 언급한 표준 및 커스텀 속성이 표시되지 않습니다. </li> <li> Braze 대시보드에서 고객 프로필의 앞서 언급한 표준 속성을 편집할 수 없습니다. </li> <li> 고객 프로필의 구독 상태를 업데이트할 수 없습니다. </li></ul> {:/} | 이 섹션에 액세스하려면 여전히 고객 프로필 보기 권한이 필요합니다. |
| 사용자 가져오기 | 사용자는 **사용자 가져오기** 페이지에서 파일을 다운로드할 수 없습니다. | |
| {::nomarkdown} <ul> <li> Segments </li> <li> Campaigns </li> <li> Canvas </li> </ul> {:/} | **사용자 데이터** 드롭다운에서: {::nomarkdown} <ul> <li> 사용자에게 <b>CSV 내보내기 이메일 주소</b> 옵션이 표시되지 않습니다. </li> <li> <b>CSV 내보내기 사용자 데이터</b>를 선택할 때 CSV 파일에 앞서 언급한 표준 및 커스텀 속성이 제공되지 않습니다. </li> </ul> {:/} | |
| 내부 테스트 그룹 | 사용자는 내부 테스트 그룹에 추가된 모든 사용자의 앞서 언급한 표준 속성에 액세스할 수 없습니다. | |
| 메시지 활동 로그 | 사용자는 메시지 활동 로그에서 식별된 모든 사용자의 앞서 언급한 표준 속성에 액세스할 수 없습니다. | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
메시지를 미리 볼 때 **PII 보기** 권한이 적용되지 않으므로, Liquid를 통해 메시지에서 참조된 경우 사용자는 [앞서 언급한 표준 속성](#potential-pii-attributes)을 볼 수 있습니다.
{% endalert %}

## 데이터 삭제 기본 설정 {#data-deletion-preferences}

이 설정을 사용하여 사용자 삭제 프로세스 중 이벤트에서 Braze가 특정 필드를 삭제할지 여부에 대한 기본 설정을 지정할 수 있습니다. 이러한 기본 설정은 Braze가 삭제한 사용자의 데이터에만 적용됩니다.

사용자가 삭제되면 Braze는 이벤트 데이터에서 모든 PII를 제거하지만 분석 목적으로 익명화된 데이터를 유지합니다. 일부 사용자 정의 필드에는 최종 사용자 정보를 Braze에 전송하는 경우 PII가 포함될 수 있습니다. 이러한 필드에 PII가 포함된 경우 Braze가 삭제된 사용자의 이벤트 데이터를 익명화할 때 데이터를 삭제하도록 선택할 수 있습니다. 필드에 PII가 포함되지 않은 경우 분석을 위해 유지할 수 있습니다.

워크스페이스에 대한 올바른 기본 설정을 결정하는 것은 귀하의 책임입니다. 적절한 설정을 결정하는 가장 좋은 방법은 Braze에 이벤트 데이터를 전송하는 내부 팀과 Braze에서 메시지 추가 정보를 사용하는 팀에 검토하여 필드에 PII가 포함될 수 있는지 확인하는 것입니다.

### 관련 필드 {#relevant-fields}

| 이벤트 이름 또는 유형 | 필드 | 참고 |
| -------------------- | ------ | ----- |
| 커스텀 이벤트 | properties |  |
| 구매 이벤트 | properties |  |
| 메시지 전송 | message_extras | 여러 이벤트 유형에 `message_extras` 필드가 포함되어 있습니다. 이 기본 설정은 향후 추가되는 이벤트 유형을 포함하여 `message_extras`를 지원하는 모든 메시지 전송 이벤트 유형에 적용됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert warning %}
**삭제는 영구적입니다!** 삭제된 사용자에 대해 Snowflake에서 필드를 제거하도록 선택하면 해당 설정은 워크스페이스의 모든 과거 데이터와 향후 삭제되는 사용자의 모든 이벤트에 적용됩니다. Braze가 삭제된 사용자의 과거 이벤트 데이터에 설정을 적용하는 프로세스를 실행한 후에는 데이터를 **복원할 수 없습니다**.
{% endalert %}

### 기본 설정 구성 {#configure-preferences}

사용자가 삭제될 경우 Braze가 제거해야 하는 필드의 체크박스를 선택하여 기본 설정을 지정합니다. PII가 포함된 필드를 선택하세요. 이 기본 설정은 워크스페이스가 기본 설정 그룹에 명시적으로 추가되지 않는 한 모든 현재 및 향후 워크스페이스에 적용됩니다.

워크스페이스별로 기본 설정을 사용자 지정하려면 기본값과 다른 설정으로 기본 설정 그룹을 추가할 수 있습니다. 추가 기본 설정 그룹에 추가되지 않은 워크스페이스에는 향후 생성되는 워크스페이스를 포함하여 기본 설정이 적용됩니다.

![워크스페이스별 데이터 삭제 기본 설정을 사용자 지정하기 위한 토글이 켜진 데이터 삭제 기본 설정 섹션.]({% image_buster /assets/img/deletion_preferences_1.png %})

## 문제 해결 {#troubleshooting}

### 2단계 인증(2FA) 설정 루프 문제 {#two-factor-authentication-2fa-setup-loop-issues}

2FA를 위해 전화번호를 성공적으로 입력한 후 루프에 빠져 로그인 페이지로 리디렉션되는 경우, 이는 첫 번째 시도에서 인증에 실패했기 때문일 수 있습니다. 이 문제를 해결하려면 다음 단계를 따르세요:

1. 광고 차단기를 끕니다.
2. 브라우저 설정에서 쿠키를 활성화합니다.
3. PC 또는 노트북을 재시작합니다.
4. 2FA 설정을 다시 시도합니다.

이러한 단계를 수행한 후에도 문제가 지속되면 [고객지원]({{site.baseurl}}/braze_support/)에 문의하세요.

### 2단계 인증(2FA)을 활성화할 수 없음 {#cant-enable-two-factor-authentication-2fa}

2FA가 활성화되어 있지만 **활성화** 버튼을 선택해도 아무 일도 일어나지 않는 경우, 브라우저가 SMS를 통해 인증 코드를 전송하는 데 필요한 리디렉션을 차단하고 있기 때문일 수 있습니다. 이 문제를 해결하는 단계는 다음과 같습니다:

1. 브라우저에서 활성화된 광고 차단기를 일시적으로 중지합니다.
2. 브라우저 설정에서 서드파티 쿠키를 활성화했는지 확인합니다.
3. 2FA 설정을 시도합니다.

### 인증 코드가 전송되지 않음 {#verification-code-doesnt-send}

Authy 페이지에서 전화번호를 입력할 때 문제가 발생하고 SMS를 받지 못하는 경우 다음 단계를 따르세요:

1. 휴대폰에 Authy 앱을 설치하고 Authy 인증기에 로그인합니다.
2. 전화번호를 입력하고 Authy 앱에서 변경 사항이나 SMS 알림을 확인합니다.
3. 여전히 SMS를 받지 못하는 경우 홈 네트워크나 비기업 Wi-Fi와 같은 다른 네트워크 연결을 사용해 보세요. 기업 네트워크에는 SMS 전달을 방해하는 보안 정책이 있을 수 있습니다.

문제가 지속되면 Authy 앱에서 이전 프로필을 삭제하고 QR 코드를 다시 스캔하여 2FA를 설정하세요. 설정을 다시 시도하기 전에 광고 차단기를 비활성화하고, 서드파티 쿠키를 활성화하거나, 다른 브라우저를 사용했는지 확인하세요.

## 다음 단계 {#next-steps}

인증 및 액세스에 대한 자세한 내용은 다음을 참조하세요:

- [SAML 및 싱글 사인온]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/)으로 ID 공급자와 SSO를 설정합니다.
- [권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/)으로 사용자가 대시보드에서 수행할 수 있는 작업을 제어합니다.