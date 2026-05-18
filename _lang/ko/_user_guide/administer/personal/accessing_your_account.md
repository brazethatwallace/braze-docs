---
nav_title: 계정 접근
article_title: 계정 접근
page_order: 0
page_type: reference
description: "이 문서에서는 Braze 계정을 얻는 방법, 접근 권한이 부여된 후 로그인하는 방법, 대시보드 접근 및 대시보드 성능 문제를 해결하는 방법을 다룹니다."

---

# 계정 접근 {#access-your-account}

> 이 문서에서는 Braze 계정을 얻는 방법, 접근 권한이 부여된 후 로그인하는 방법, 대시보드 접근 및 대시보드 성능 문제를 해결하는 방법을 다룹니다.

회사의 첫 번째 Braze 사용자로서 처음 로그인하는 경우, 계약 첫날에 `@alerts.braze.com`에서 이메일 확인 및 로그인을 요청하는 환영 이메일을 받게 됩니다.

계정을 확인한 후, 대시보드의 [회사 사용자]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users/) 페이지에서 추가 사용자를 추가할 수 있습니다. 모든 사용자는 추가된 후 계정 확인을 요청하는 이메일을 받게 됩니다.

회사의 Braze 계정에서 첫 번째 사용자가 아닌 경우, 회사의 Braze 계정 관리자에게 연락하여 계정 생성을 요청하세요. 그러면 `@alerts.braze.com`에서 이메일 확인 및 로그인을 요청하는 환영 이메일을 받게 됩니다.

## 로그인 {#logging-in}

처음 로그인하든 백 번째 로그인하든, 대시보드에 접근하는 방법은 다음과 같습니다. 회사의 첫 번째 사용자인 경우, 이전 섹션의 안내를 따르세요. 그렇지 않은 경우, 회사의 Braze 관리자가 계정을 생성한 후 로그인할 수 있습니다.

[Braze.com](https://www.braze.com) 홈 사이트에서 로그인하거나, 특정 [Braze 인스턴스]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints/)에 해당하는 대시보드 URL을 사용할 수 있습니다. 편의를 위해 Braze는 다음과 같은 여러 SSO(싱글 사인온) 옵션을 제공합니다:

* [SAML SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup/)
    * [SAML 적시 프로비저닝]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_just_in_time_provisioning/)
* [Microsoft Entra SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso/)
* [Okta]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/okta/)
* [OneLogin]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/onelogin/)

SSO로 Braze에 로그인한 후에는 더 이상 비밀번호를 사용하여 대시보드에 로그인할 수 없습니다. 두 이메일 주소 모두 같은 받은편지함으로 이메일을 전달하지만, 로그인 시 Braze는 이를 별도의 계정으로 인식합니다. 쿠키를 삭제하면 로그아웃되므로 저장하지 않은 작업이 손실됩니다.

## 지원 브라우저 {#supported-browsers}

Braze 대시보드는 다음 브라우저를 지원합니다:
- Chrome (버전 87 이상)
- Firefox (버전 85 이상)
- Safari (버전 15.4 이상)
- Edge (버전 87 이상)

Braze 대시보드에서 예기치 않은 오류가 발생하고 브라우저 콘솔 도구에 `ReferenceError: structuredClone is not defined` 오류가 표시되면, 브라우저가 오래된 것입니다. 이 오류가 계속 발생하면 브라우저를 제거한 후 다시 설치하세요.

## 여러 Braze 대시보드 접근 {#accessing-multiple-braze-dashboards}

Braze는 동일한 클러스터 내에서 같은 이메일 주소를 여러 대시보드 사용자에 등록하는 것을 허용하지 않습니다(예: US-01에 두 개의 대시보드가 있는 경우). 다른 클러스터에서는 같은 이메일을 사용하여 계정을 생성할 수 있습니다(예: US-01에 하나의 대시보드가 있고 US-05에 하나가 있는 경우). 동일한 클러스터 내에서 여러 Braze 대시보드에 접근해야 하는 경우, 다음 방법을 사용할 수 있습니다:

### 이메일 별칭 사용 {#use-email-aliases}

이메일 제공업체가 Gmail인 경우, 이메일 주소에 `+` 기호와 임의의 텍스트를 추가하여 별칭을 만들 수 있습니다. 예를 들어:
- **원래 이메일:** `rocky@gmail.com`
- **별칭 이메일:** `rocky+1@gmail.com`

두 이메일 주소 모두 같은 받은편지함으로 이메일을 전달하지만, 로그인 시 Braze는 이를 별도의 계정으로 인식합니다.

### 다른 제공업체에서 별도의 별칭 생성 {#create-separate-aliases-with-other-providers}

이메일 제공업체가 `+` 별칭을 지원하지 않는 경우에도 별도의 별칭을 만들 수 있습니다. 예를 들어 `rocky@braze.com`이 `rocky.lotito@braze.com`으로 전달되도록 설정할 수 있습니다. 이렇게 하면 여러 주소가 같은 받은편지함으로 전달되면서도 Braze에서는 다른 이메일로 인식됩니다.

### 다중 회사 개발자 사용 {#use-multi-company-developers}

다중 회사 개발자 기능을 사용하면 단일 사용자 계정을 여러 회사에서 공유할 수 있습니다. 사용자는 고객 프로필 메뉴에서 다른 회사 대시보드 간에 전환할 수 있습니다.

SSO를 사용하고 있으며 다중 회사 개발자를 설정하려면, 커스텀 SAML SSO 통합을 설정하여 SAML 커스텀 엔티티 ID를 활성화해야 합니다. [서비스 공급자(SP) 시작 로그인]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup/)의 단계를 따르되, 다음 변경 사항을 적용하세요:
- 각 대시보드 통합에 대해 **Entity ID**를 `braze_dashboard_<companyID>`로 변경합니다.
- 각 대시보드에 대해 `saml_sso_custom_entity_id` 기능 플리퍼를 활성화하도록 고객 성공 매니저 또는 계정 매니저에게 문의하세요.

### SSO(싱글 사인온) 고려 사항 {#considerations-for-single-sign-on-sso}

SSO(싱글 사인온)를 사용하는 경우, 여러 다른 이메일 주소를 사용하면 문제가 발생할 수 있습니다. 접근 문제를 방지하려면 SSO 설정이 올바르게 구성되어 있는지 확인하세요.

## 문제 해결 {#troubleshooting}

### 비밀번호 재설정 {#resetting-your-password}

비밀번호를 재설정하려면 대시보드 로그인 페이지에서 **Forgot your password?** 링크를 선택하세요. 이메일을 입력하라는 메시지가 표시되며, 비밀번호를 재설정할 수 있는 링크를 받게 됩니다.

!["Forgot your password?" 프롬프트가 있는 대시보드 로그인 화면.]({% image_buster /assets/img_archive/enable_reset.png %}){: style="max-width:60%"}

### 브라우저 캐시 및 쿠키 삭제 {#clearing-your-browser-cache-and-cookies}

대시보드 성능에 문제가 있는 경우(예: 대시보드 또는 세그먼트 성능 목록이 로드되지 않는 경우), 해당 브라우저의 단계에 따라 브라우저 캐시와 쿠키를 삭제해 보세요.

{% alert important %}
쿠키를 삭제하면 로그아웃되므로 저장하지 않은 작업이 손실됩니다.
{% endalert %}

- [Chrome에서 캐시 및 쿠키 삭제](https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop)
- [Mac의 Safari에서 쿠키 삭제](https://support.apple.com/en-gb/guide/safari/sfri11471/16.1/mac/13.0)
- [Firefox에서 쿠키 및 사이트 데이터 삭제](https://support.mozilla.org/en-US/kb/clear-cookies-and-site-data-firefox)
- [Microsoft Edge에서 모든 쿠키 삭제](https://support.microsoft.com/en-us/windows/manage-cookies-in-microsoft-edge-view-allow-block-delete-and-use-168dab11-0753-043d-7c16-ede5947fc64d#bkmk_deleteallcookies)

브라우저 캐시와 쿠키를 삭제해도 문제가 해결되지 않으면 [고객지원]({{site.baseurl}}/support_contact/)에 문의하세요.

### Google Chrome에서 "Aw, Snap!" 오류 {#aw-snap-error-in-google-chrome}

Google Chrome에서 "Aw, Snap!" 오류가 표시되면, Chrome이 Braze 대시보드 페이지를 로드하는 데 문제가 있는 것입니다. 문제 해결 단계는 [Chrome에서 일반적인 오류 메시지에 대한 도움말 보기](https://support.google.com/chrome/answer/95669?co=GENIE.Platform%3DDesktop&hl=en)를 참조하세요.

### 대시보드 탐색 중 "Please Refresh Page" 또는 "Unexpected Error" {#please-refresh-page-or-unexpected-error-while-navigating-the-dashboard}

이 오류는 회사 사용자가 어떤 워크스페이스에도 속하지 않을 때 나타날 수 있습니다. 문제를 해결하려면:

1. [회사 사용자]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users/) 페이지로 이동합니다.
2. 해당 사용자가 워크스페이스에 추가되었는지 확인합니다.
3. 어떤 워크스페이스에도 속하지 않은 경우, 사용자를 추가하고 적절한 권한을 할당합니다.
4. 사용자에게 대시보드를 새로고침하도록 요청합니다.
5. 문제가 지속되면 [고객지원]({{site.baseurl}}/support_contact/)에 문의하세요.

### 드래그 앤 드롭 편집기 접근 {#accessing-the-drag-and-drop-editor}

대부분의 회사 사용자에게 드래그 앤 드롭 편집기가 로드됩니다. 그러나 VPN을 사용하거나 방화벽 뒤에 있는 경우, 도메인을 허용 목록에 추가해야 할 수 있습니다. IT 관리자에게 `*.bz-rndr.com`이 허용 목록에 있는지 확인하도록 문의하세요.

편집기는 다음과 같은 이유로 로딩 문제가 발생할 수 있습니다:

- **일시적 오류:** 연결, 통신 또는 데이터 전송에 영향을 줄 수 있는 일시적인 장애입니다. 다행히 이러한 오류는 일반적으로 단기적인 조건에 의해 발생하며 체계적인 문제를 나타내지 않으므로, 큰 개입 없이 자체적으로 해결되는 경우가 많습니다.
- **주요 오류:** 기본 인프라 또는 제품 문제가 관련될 수 있습니다. [Braze 시스템 상태 페이지](https://braze.statuspage.io/)를 확인하세요. 저희가 상황을 인지하고 적극적으로 해결하고 있을 가능성이 높습니다.

{% alert important %}
여전히 문제가 발생하는 경우, [지원 티켓을 열어주세요]({{site.baseurl}}/user_guide/administer/personal/braze_support/). 그 전에 IT 관리자가 `*.bz-rndr.com`이 허용 목록에 있는지 확인했는지 점검하세요.
{% endalert %}

### Braze 러닝 접근 {#accessing-braze-learning}

Braze 러닝에 로그인하는 데 문제가 있고 대시보드로 리디렉션되는 루프에 갇혀 있는 경우, 다음 단계를 수행하세요:

1. 여러 Braze 계정이 있는 경우, 잘못된 계정으로 두 번 로그인하면 Braze 대시보드로 이동됩니다. 올바른 계정으로 로그인하고 있는지 확인하세요.
2. 광고 차단기가 있는 경우, 꺼져 있는지 확인하세요. 싱글 사인온 기능에 필요한 쿠키를 차단할 수 있습니다.
3. **회사 설정** > **보안 설정**으로 이동하여 SSO(싱글 사인온)가 켜져 있는지 확인합니다.
4. 대시보드 사용자 프로필에 이름과 성이 모두 포함되어 있는지 확인합니다. 성이 없으면 로그인 프로세스가 중단될 수 있습니다.
5. 대시보드에서 **고객지원** > **Braze Learning**으로 이동하여 Braze 러닝에 접근합니다.
6. 문제가 계속되면 계정을 다시 생성하는 것을 고려하세요. 무료 체험 기간 동안 Braze 러닝에 접근했던 사용자는 현재 접근에 어려움을 겪을 수 있습니다.

### 2단계 인증(2FA) 문제 {#two-factor-authentication-2fa-issues}

사용자가 2단계 인증(2FA)에 문제가 있어 Braze 대시보드에 접근할 수 없는 경우, 여러 가지 이유가 있을 수 있습니다. 가장 일반적으로는 등록된 전화번호에 더 이상 접근할 수 없거나 Authy 앱이 설치된 기기에 접근할 수 없는 경우입니다.

관리자는 다음을 수행하여 영향을 받는 사용자의 2FA를 재설정해야 합니다:

1. **사용자 관리**로 이동합니다.
2. 2FA 문제가 있는 사용자에 대해 **Edit User**를 선택합니다.
3. 2FA 재설정 옵션을 선택합니다.
4. 메시지가 표시되면 2FA 재설정을 확인합니다.
5. 재설정으로 문제가 즉시 해결되지 않으면 쿠키와 캐시를 삭제하세요.

보안상의 이유로 Braze는 사용자를 대신하여 2FA를 재설정할 수 없으므로, 관리자가 2FA를 재설정할 수 없는 경우 지원 티켓을 생성하세요.

#### 고려 사항 {#considerations}

- 회사 수준에서 2FA가 적용된 경우: 재설정 후 Braze는 사용자가 다음 로그인 시 2FA를 다시 설정하도록 안내합니다.
- 회사 수준에서 2FA가 적용되지 않은 경우: 사용자는 2FA를 다시 설정할 필요 없이 대시보드에 로그인합니다. 2FA를 활성화하려면 계정 설정에서 할 수 있습니다.

{% alert note %}
이 재설정 프로세스는 지난 한 시간 내에 너무 많은 토큰을 요청하여 계정이 잠긴 사용자에게도 적용됩니다.
{% endalert %}

### 계정 잠김 {#locked-out-of-account}

Braze 계정이 잠긴 경우, 아래 단계를 따라 다시 접근할 수 있습니다.

수신하는 오류 메시지를 통해 어떤 종류의 잠김인지 알 수 있습니다:

- [비밀번호에 대한 오류가 표시됩니다.](#password-error)
- [오류는 표시되지 않지만 Braze에 접근할 수 없습니다.](#instance-error)
- [계정 정지에 대한 오류가 표시됩니다.](#account-suspension)

#### 비밀번호 오류 {#password-error}

계정 보안은 저희에게 중요하므로, Braze 계정에 로그인하려면 비밀번호가 필요합니다.
- 올바른 [Braze 대시보드 인스턴스]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints/)에 로그인하고 있는지 확인하세요. 계정 관리자 또는 Braze 계정 매니저에게 확인하세요.
- 비밀번호가 만료되었을 수 있으므로 [재설정](#resetting-your-password)해야 합니다.
- [싱글 사인온]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup/) 서비스를 사용하는 경우, 계정 관리자에게 설정이 올바르게 완료되었는지 확인하세요.
- 회사가 여러 Braze 인스턴스를 사용하는 경우, 잘못된 이메일로 로그인하고 있을 수 있습니다.

확실하지 않은 경우, 언제든지 [비밀번호를 재설정](#resetting-your-password)할 수 있습니다.

#### 인스턴스 오류 {#instance-error}

평소 로그인에 사용하는 동일한 기기를 사용하는 경우, Braze가 자동으로 올바른 인스턴스를 감지합니다. 그러나 감지되지 않거나 처음 로그인하는 경우, 다음을 고려하세요:

- 올바른 [Braze 대시보드 인스턴스]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints/)에 로그인하고 있는지 확인하세요. 계정 관리자 또는 Braze 계정 매니저에게 확인하세요.
- 회사가 여러 Braze 인스턴스를 사용하는 경우, 잘못된 이메일로 로그인하고 있을 수 있습니다.

#### 계정 정지 {#account-suspension}

이런 일은 자주 발생하지 않지만, Braze는 계정 정지 및 삭제를 매우 심각하게 다룹니다. 이 오류가 발생하면 회사의 Braze 관리자, Braze 계정 매니저 또는 [고객지원][support]에 문의하세요.

### Braze 대시보드가 로드되지 않거나 예상대로 작동하지 않음 {#braze-dashboard-wont-load-or-work-as-expected}

먼저 다른 브라우저에서 대시보드가 로드되는지 테스트하세요. 다른 브라우저에서 문제가 지속되지 않으면 다음을 시도하세요:

- **대시보드 다시 시작:** 로그아웃하고 브라우저를 종료한 다음, 대시보드에 다시 로그인해 보세요.
- **로컬 브라우저 새로고침:** [쿠키와 브라우저 캐시를 삭제](#clearing-your-browser-cache-and-cookies)한 다음, 대시보드에 다시 로그인해 보세요.
- **호환 가능한 플러그인 또는 서드파티 도구 사용:** 광고 차단기 또는 보안 소프트웨어가 Braze 대시보드 로딩을 방해할 수 있습니다. 광고 차단기를 비활성화한 후 Braze 대시보드에 로그인하여 테스트하세요.
        - 브라우저 콘솔 로그도 확인할 수 있습니다. `ERR_BLOCKED_BY_CLIENT` 관련 오류는 콘텐츠가 광고 차단기에 의해 차단되고 있음을 나타낼 수 있습니다.
- **연결 품질 확인:** 연결 품질이 좋지 않을 수 있습니다. 다른 기기에서 Braze 대시보드에 로그인해 보세요.
- **올바른 클러스터에 접근하고 있는지 확인:** 회사에 할당된 클러스터에 로그인하고 있는지 확인하세요. 예를 들어, US-03에 할당되었지만 US-01에 로그인하고 있을 수 있습니다.
- **브라우저 업데이트:** 브라우저를 최신 [지원 브라우저](#supported-browsers)로 업데이트한 다음, 대시보드에 로그인해 보세요.

모든 브라우저에서 문제가 발생하는 경우, 다음을 시도하세요:

- **네트워크 연결 확인:** 가능하면 VPN을 끄거나, 네트워크 연결을 비활성화했다가 다시 활성화하세요.
- **기기 재시작:** 기기를 재시작한 후 Braze 대시보드에 로그인해 보세요.

이전 문제를 해결했는데도 대시보드가 여전히 로드되지 않거나 예상대로 작동하지 않으면 [고객지원]({{site.baseurl}}/braze_support/)에 문의하세요.

### 사용자가 어떤 워크스페이스에도 속하지 않음 {#the-user-belongs-to-no-workspace}

**설정** > **회사 사용자**로 이동하여 사용자의 워크스페이스 수준 권한을 확인하세요. **Workspaces**에 필요한 워크스페이스를 추가하세요.

### 신규 사용자 문제 해결 {#troubleshooting-as-a-new-user}

새로운 Braze 사용자로서 로그인하거나 처음으로 계정에 접근하는 데 문제가 있는 경우, 다음 단계를 따라 일반적인 문제를 해결하세요:

#### 환영 이메일을 받지 못했습니다 {#i-never-received-the-welcome-email}

- 스팸 폴더 확인: 계정 활성화 이메일이 스팸 또는 정크 폴더로 필터링되지 않았는지 확인하세요.
- 이메일 주소 확인: 관리자에게 새 Braze 계정에 연결된 이메일 주소가 올바른지 확인하도록 요청하세요.
- IT 정책: IT 팀에 활성화 이메일 수신을 방해할 수 있는 정책이 있는지 확인하세요.

#### 이메일을 받았지만 2단계 인증(2FA) 설정에서 막혔습니다 {#i-received-the-email-but-im-stuck-setting-up-two-factor-authentication-2fa}

- 2FA 재설정: 2FA 설정에 문제가 있는 경우, 관리자가 설정에서 사용자 계정의 2FA를 재설정할 수 있습니다.
- 사용자 다시 추가: 문제가 지속되면 관리자가 대시보드에서 사용자 계정을 삭제하고 다시 추가할 수 있습니다. 이렇게 하면 동일한 세부 정보로 사용자를 다시 생성할 수 있습니다.

이러한 단계를 수행한 후에도 문제가 계속되면 [고객지원]({{site.baseurl}}/braze_support/)에 문의하여 추가 지원을 받으세요.

## 다음 단계 {#next-steps}

계정에 접근한 후, 다음 리소스를 살펴보세요:

- [Braze 대시보드]({{site.baseurl}}/user_guide/administer/personal/the_braze_dashboard/)에서 주요 기능과 도구를 탐색하는 방법을 알아보세요.
- [언어 설정]({{site.baseurl}}/user_guide/administer/personal/language_settings/)에서 선호하는 대시보드 언어를 설정하세요.