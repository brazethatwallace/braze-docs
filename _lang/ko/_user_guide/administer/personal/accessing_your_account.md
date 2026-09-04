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

계정을 확인한 후, 대시보드의 [회사 사용자]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users) 페이지에서 추가 사용자를 추가할 수 있습니다. 모든 사용자는 추가된 후 계정 확인을 요청하는 이메일을 받게 됩니다.

회사의 Braze 계정에서 첫 번째 사용자가 아닌 경우, 회사의 Braze 계정 관리자에게 연락하여 계정 생성을 요청하세요. 그러면 `@alerts.braze.com`에서 이메일 확인 및 로그인을 요청하는 환영 이메일을 받게 됩니다.

## 로그인 {#logging-in}

처음 로그인하든 백 번째 로그인하든, 대시보드에 액세스하는 방법은 다음과 같습니다. 회사의 첫 번째 사용자인 경우 이전 섹션의 안내를 따르세요. 그렇지 않은 경우 회사의 Braze 관리자가 계정을 생성한 후 로그인할 수 있습니다.

[Braze.com](https://www.braze.com) 홈 사이트에서 로그인하거나, 특정 [Braze 인스턴스]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)에 해당하는 대시보드 URL을 사용할 수 있습니다. 편의를 위해 Braze는 다음과 같은 여러 SSO 옵션을 제공합니다:

* [SAML SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup)
    * [SAML 적시 프로비저닝]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_just_in_time_provisioning)
* [Microsoft Entra SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso)
* [Okta]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/okta)
* [OneLogin]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/onelogin)

SSO로 Braze에 로그인한 후에는 더 이상 비밀번호를 사용하여 대시보드에 로그인할 수 없습니다. 두 이메일 주소 모두 같은 받은편지함으로 이메일을 전달하지만, 로그인 시 Braze는 이를 별도의 계정으로 인식합니다. 쿠키를 삭제하면 로그아웃되므로, 저장하지 않은 작업은 손실됩니다.

## 지원 브라우저 {#supported-browsers}

Braze 대시보드는 다음 브라우저를 지원합니다:
- Chrome (버전 87 이상)
- Firefox (버전 85 이상)
- Safari (버전 15.4 이상)
- Edge (버전 87 이상)

Braze 대시보드에서 예기치 않은 오류가 표시되고 브라우저 콘솔 도구에 `ReferenceError: structuredClone is not defined` 오류가 나타나면, 브라우저가 오래된 것입니다. 이 오류가 계속 발생하면 브라우저를 제거한 후 다시 설치하세요.

## 여러 Braze 대시보드에 액세스하기 {#accessing-multiple-braze-dashboards}

Braze에서는 동일한 클러스터 내에서 같은 이메일 주소를 여러 대시보드 사용자에 등록하는 것을 허용하지 않습니다(예: US-01에 두 개의 대시보드가 있는 경우). 다른 클러스터에서는 동일한 이메일로 계정을 생성할 수 있습니다(예: US-01에 대시보드 하나, US-05에 대시보드 하나가 있는 경우). 동일한 클러스터 내에서 여러 Braze 대시보드에 액세스해야 하는 경우 다음 방법을 사용할 수 있습니다.

### 이메일 별칭 사용하기 {#use-email-aliases}

이메일 제공업체가 Gmail인 경우, 이메일 주소에 `+` 기호와 임의의 텍스트를 추가하여 별칭을 만들 수 있습니다. 예를 들어:
- **원본 이메일:** `rocky@gmail.com`
- **별칭 이메일:** `rocky+1@gmail.com`

두 이메일 주소 모두 동일한 받은편지함으로 이메일이 전달되지만, 로그인 시 Braze에서는 별도의 계정으로 인식합니다.

### 다른 제공업체에서 별도의 별칭 만들기 {#create-separate-aliases-with-other-providers}

이메일 제공업체가 `+` 별칭 기능을 지원하지 않는 경우에도 별도의 별칭을 만들 수 있습니다. 예를 들어 `rocky@braze.com`이 `rocky.lotito@braze.com`으로 전달되도록 설정할 수 있습니다. 이렇게 하면 여러 주소가 동일한 받은편지함으로 전달되면서도 Braze에서는 서로 다른 이메일로 인식됩니다.

### 멀티 컴퍼니 개발자 사용하기 {#use-multi-company-developers}

멀티 컴퍼니 개발자 기능을 사용하면 하나의 사용자 계정을 여러 회사에서 공유할 수 있습니다. 대시보드 사용자는 사용자 프로필 메뉴에서 서로 다른 회사 대시보드 간에 전환할 수 있습니다.

SSO를 사용 중이며 멀티 컴퍼니 개발자를 설정하려는 경우, 커스텀 SAML SSO 통합을 설정하여 SAML 커스텀 엔티티 ID를 활성화해야 합니다. [SP(서비스 공급자) 시작 로그인]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup)의 단계를 따르되, 다음 변경 사항을 적용하세요:
- **Entity ID**를 각 대시보드 통합에 대해 `braze_dashboard_<companyID>`로 변경합니다.
- 각 대시보드에 대해 `saml_sso_custom_entity_id` 기능 플리퍼를 활성화하도록 고객 성공 매니저 또는 계정 매니저에게 문의하세요.

#### 2단계 인증(2FA) {#two-factor-authentication-2fa}

멀티 컴퍼니 개발자의 2FA 작동 방식은 사용하는 2FA 방법에 따라 다릅니다:

- **이메일 및 SMS:** 2FA 설정이 연결된 모든 개발자 계정에 복사됩니다. 하나의 계정에서 이메일 또는 SMS 2FA를 설정하면 동일한 방법이 모든 회사 대시보드에 적용됩니다.
- **시간 기반 일회용 비밀번호(TOTP):** TOTP 설정은 계정 간에 동기화되지 않습니다. 인증 앱을 사용하는 경우, 직접 로그인하는 각 대시보드에 대해 별도의 코드를 설정해야 합니다.

대시보드 내에서 계정을 전환할 때는 해당 세션 중 연결된 계정에 처음 로그인할 때 한 번만 2FA를 완료하면 됩니다.

### SSO 사용 시 고려 사항 {#considerations-for-single-sign-on-sso}

SSO를 사용하는 경우, 서로 다른 여러 이메일 주소를 사용하면 문제가 발생할 수 있다는 점에 유의하세요. 액세스 문제를 방지하기 위해 SSO 설정이 올바르게 구성되어 있는지 확인하세요.

## 문제 해결 {#troubleshooting}

### 비밀번호 재설정 {#resetting-your-password}

비밀번호를 재설정하려면 대시보드 로그인 페이지에서 **Forgot your password?** 링크를 선택하세요. 비밀번호를 재설정할 수 있는 링크를 받기 위해 이메일을 입력하라는 안내가 표시됩니다.


#### 비밀번호 재설정 이메일을 받지 못한 경우 {#password-reset-email-not-received}

비밀번호 재설정을 요청했지만 이메일을 받지 못한 경우, 다음 문제 해결 단계를 시도해 보세요.

{% alert note %}
회사에서 [SSO(싱글 사인온)]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup)을 시행하는 경우, 비밀번호 로그인이 비활성화되어 있어 로그인 페이지에 **Forgot your password?**가 표시되지 않거나 비밀번호 재설정 이메일이 발송되지 않을 수 있습니다. 대신 조직의 ID 공급자를 통해 로그인하거나 Braze 관리자에게 문의하세요.
{% endalert %}

1. **이메일 주소 확인:** 관리자에게 요청하여 **설정** > **회사 사용자**에서 계정에 등록된 이메일 주소가 일치하는지 확인하세요. 재설정 링크는 시스템에 등록된 이메일로 발송됩니다.
2. **스팸 및 정크 폴더 확인:** 스팸 또는 정크 폴더에서 `@alerts.braze.com`의 이메일을 확인하세요.
3. **IT 이메일 필터 확인:** IT 팀에 `@alerts.braze.com`의 이메일이 차단되거나 필터링되고 있지 않은지 확인하세요.
4. **올바른 대시보드 인스턴스 확인:** 올바른 [Braze 대시보드 인스턴스]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)에서 재설정을 요청하고 있는지 확인하세요. 확실하지 않은 경우 계정 관리자 또는 Braze 계정 매니저에게 문의하세요.
5. **다른 브라우저 사용:** 일부 브라우저 확장 프로그램이나 설정이 비밀번호 재설정 프로세스에 영향을 줄 수 있습니다. 다른 브라우저나 시크릿 창을 사용해 보세요.

비밀번호 재설정 링크는 이메일 발송 후 2시간이 지나면 만료됩니다. 링크가 만료된 경우, 로그인 페이지에서 새로운 재설정을 요청하세요.

위 단계 중 어떤 것도 효과가 없는 경우, 관리자가 해결 방법으로 사용자 계정을 삭제하고 다시 생성할 수 있습니다. 자세한 내용은 [회사 사용자 관리]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users)를 참조하세요.

{% alert note %}
사용자 계정을 삭제하고 다시 생성하면 권한이 초기화되며, 해당 사용자가 이전에 소유하던 Campaigns, Canvases 및 기타 콘텐츠에 대한 자산 기여도에 영향을 줄 수 있습니다.
{% endalert %}

### 브라우저 캐시 및 쿠키 삭제 {#clearing-your-browser-cache-and-cookies}

대시보드 성능 문제가 발생하는 경우(예: 대시보드 또는 Segment 성능 목록이 로드되지 않는 경우) 사용 중인 브라우저에 맞는 단계에 따라 브라우저 캐시와 쿠키를 삭제해 보세요.

{% alert important %}
쿠키를 삭제하면 로그아웃되므로 저장하지 않은 작업이 손실됩니다.
{% endalert %}

- [Chrome에서 캐시 및 쿠키 삭제](https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop)
- [Mac의 Safari에서 쿠키 삭제](https://support.apple.com/en-gb/guide/safari/sfri11471/16.1/mac/13.0)
- [Firefox에서 쿠키 및 사이트 데이터 삭제](https://support.mozilla.org/en-US/kb/clear-cookies-and-site-data-firefox)
- [Microsoft Edge에서 모든 쿠키 삭제](https://support.microsoft.com/en-us/windows/manage-cookies-in-microsoft-edge-view-allow-block-delete-and-use-168dab11-0753-043d-7c16-ede5947fc64d#bkmk_deleteallcookies)

브라우저 캐시와 쿠키를 삭제해도 문제가 해결되지 않으면 [지원팀]({{site.baseurl}}/support_contact)에 문의하세요.

### Google Chrome에서 "이런!" 오류 {#aw-snap-error-in-google-chrome}

Google Chrome에서 "이런!" 오류가 표시되면 Chrome이 Braze 대시보드 페이지를 로드하는 데 문제가 있는 것입니다. 문제 해결 단계는 [Chrome에서 일반적인 오류 메시지에 대한 도움말](https://support.google.com/chrome/answer/95669?co=GENIE.Platform%3DDesktop&hl=en)을 참조하세요.

### 대시보드 탐색 중 "페이지를 새로고침하세요" 또는 "예기치 않은 오류" {#please-refresh-page-or-unexpected-error-while-navigating-the-dashboard}

이 오류는 회사 사용자가 어떤 워크스페이스에도 속하지 않은 경우 나타날 수 있습니다. 문제를 해결하려면:

1. [회사 사용자]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users) 페이지로 이동합니다.
2. 사용자가 워크스페이스에 추가되어 있는지 확인합니다.
3. 어떤 워크스페이스에도 속하지 않은 경우, 사용자를 추가하고 적절한 권한을 할당합니다.
4. 사용자에게 대시보드를 새로고침하도록 요청합니다.
5. 문제가 지속되면 [지원팀]({{site.baseurl}}/support_contact)에 문의하세요.

### 드래그 앤 드롭 편집기 접근 {#accessing-the-drag-and-drop-editor}

대부분의 회사 사용자는 드래그 앤 드롭 편집기를 로드할 수 있습니다. 그러나 VPN을 사용하거나 방화벽 뒤에 있는 경우 도메인을 허용 목록에 추가해야 할 수 있습니다. IT 관리자에게 `*.bz-rndr.com`이 허용 목록에 추가되어 있는지 확인해 달라고 요청하세요.

편집기는 다음과 같은 이유로 로딩 문제가 발생할 수 있습니다.

- **일시적 오류:** 연결, 커뮤니케이션 또는 데이터 전송에 영향을 줄 수 있는 일시적인 장애입니다. 다행히 이러한 오류는 단기적인 조건에 의해 발생하며 시스템적 문제를 나타내지 않으므로, 일반적으로 별도의 조치 없이 자동으로 해결됩니다.
- **주요 오류:** 기본 인프라 또는 제품 문제가 관련되어 있을 수 있습니다. [Braze 시스템 상태 페이지](https://braze.statuspage.io/)를 확인하세요. 저희가 이미 상황을 인지하고 적극적으로 해결에 나서고 있을 수 있습니다.

{% alert important %}
여전히 문제가 발생하는 경우, [지원 티켓을 열어 주세요]({{site.baseurl}}/user_guide/administer/personal/braze_support). 그 전에 IT 관리자가 `*.bz-rndr.com`이 허용 목록에 추가되어 있는지 확인했는지 점검하세요.
{% endalert %}

### Braze 학습 접근 {#accessing-braze-learning}

Braze 학습에 로그인할 때 문제가 발생하여 대시보드로 리디렉션되는 루프에 갇힌 경우, 다음 단계를 수행하세요.

1. Braze 계정이 여러 개인 경우, 잘못된 계정으로 두 번 로그인하면 Braze 대시보드로 이동합니다. 올바른 계정에 로그인하고 있는지 확인하세요.
2. 광고 차단기가 있는 경우, 꺼져 있는지 확인하세요. 광고 차단기가 SSO 기능에 필요한 쿠키를 차단할 수 있습니다.
3. **설정** > **회사 설정** > **관리자 설정** > **보안 설정**으로 이동하여 SSO(싱글 사인온)이 켜져 있는지 확인하세요.
4. 대시보드 사용자 프로필에 이름과 성이 모두 포함되어 있는지 확인하세요. 성이 없으면 로그인 프로세스가 중단될 수 있습니다.
5. 대시보드에서 **지원** > **Braze 학습**으로 이동하여 Braze 학습에 접근하세요.
6. 문제가 계속되면 계정을 다시 생성하는 것을 고려해 보세요. 무료 평가판 기간에 Braze 학습에 접근했던 사용자는 현재 접근에 어려움이 있을 수 있습니다.

### 2단계 인증(2FA) 문제 {#two-factor-authentication-2fa-issues}

사용자가 2단계 인증(2FA) 문제를 겪고 있어 Braze 대시보드에 접근할 수 없는 경우, 여러 가지 원인이 있을 수 있습니다. 가장 일반적으로 등록된 전화번호에 더 이상 접근할 수 없거나 Authy 앱이 설치된 기기에 접근할 수 없는 경우입니다.

관리자는 다음을 수행하여 영향을 받는 사용자의 2FA를 재설정해야 합니다.

1. **설정** > **사용자 관리**로 이동합니다.
2. 2FA 문제를 겪고 있는 사용자를 선택합니다.
3. **2단계 인증** 아래에서 **재설정**을 선택합니다.
4. 메시지가 표시되면 2FA 재설정을 확인합니다.
5. 재설정 후에도 문제가 즉시 해결되지 않으면 쿠키와 캐시를 삭제하세요.

보안상의 이유로 Braze에서는 사용자를 대신하여 2FA를 재설정할 수 없으므로, 관리자가 2FA를 재설정할 수 없는 경우 지원 티켓을 생성하세요.

#### 고려 사항 {#considerations}

- 회사 수준에서 2FA가 강제 적용되는 경우: 재설정 후, Braze는 사용자가 다음 로그인 시 2FA를 다시 설정하도록 안내합니다.
- 회사 수준에서 2FA가 강제 적용되지 않는 경우: 사용자는 2FA를 다시 설정할 필요 없이 대시보드에 로그인합니다. 2FA를 활성화하려면 계정 설정에서 설정할 수 있습니다.

{% alert note %}
이 재설정 프로세스는 지난 한 시간 동안 토큰을 너무 많이 요청하여 계정이 잠긴 사용자에게도 적용됩니다.
{% endalert %}

### 계정 잠금 {#locked-out-of-account}

Braze 계정이 잠긴 경우, 다음 단계에 따라 다시 로그인할 수 있습니다.

수신하는 오류 메시지를 통해 어떤 종류의 잠금인지 알 수 있습니다.

- [비밀번호 관련 오류가 표시됩니다.](#password-error)
- [오류는 표시되지 않지만 Braze에 여전히 로그인할 수 없습니다.](#instance-error)
- [계정 정지 관련 오류가 표시됩니다.](#account-suspension)

#### 비밀번호 오류 {#password-error}

계정 보안은 중요하므로, Braze 계정에 로그인하려면 비밀번호가 필요합니다.
- 올바른 [Braze 대시보드 인스턴스]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)에 로그인하고 있는지 확인하세요. 확실하지 않은 경우 계정 관리자 또는 Braze 계정 매니저에게 문의하세요.
- 비밀번호가 만료되었을 수 있으므로 [비밀번호를 재설정](#resetting-your-password)해야 합니다.
- [싱글 사인온]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup) 서비스를 사용하는 경우, 계정 관리자에게 설정이 올바르게 완료되었는지 확인하세요.
- 회사에서 여러 Braze 인스턴스를 사용하는 경우, 잘못된 이메일로 로그인하고 있을 수 있습니다.

확실하지 않은 경우, 언제든지 [비밀번호를 재설정](#resetting-your-password)할 수 있습니다.

#### 인스턴스 오류 {#instance-error}

평소에 사용하는 기기로 로그인하는 경우, Braze가 올바른 인스턴스를 자동으로 감지해야 합니다. 그러나 감지되지 않거나 처음 로그인하는 경우, 다음을 고려하세요.

- 올바른 [Braze 대시보드 인스턴스]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)에 로그인하고 있는지 확인하세요. 확실하지 않은 경우 계정 관리자 또는 Braze 계정 매니저에게 문의하세요.
- 회사에서 여러 Braze 인스턴스를 사용하는 경우, 잘못된 이메일로 로그인하고 있을 수 있습니다.

#### 계정 정지 {#account-suspension}

이런 경우는 자주 발생하지 않지만, Braze는 계정 정지 및 삭제를 매우 중요하게 다룹니다. 로그인 시도 시 "계정이 차단되었습니다" 오류가 표시되면, 대시보드 계정이 일시적으로 정지된 것입니다. 이는 여러 가지 이유로 발생할 수 있습니다.

| 사유 | 설명 |
| --- | --- |
| 결제 문제 | 회사의 Braze 계정에 미해결 청구 또는 결제 문제가 있을 수 있습니다. |
| 정책 위반 | 계정이 Braze 서비스 약관 또는 허용 가능한 사용 정책을 위반했을 수 있습니다. |
| 보안 우려 | 의심스러운 활동으로 인해 보안상의 이유로 자동 정지가 트리거되었을 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="계정 정지 사유" }

이 문제를 해결하려면 회사의 Braze 관리자, Braze 계정 매니저 또는 [지원팀]({{site.baseurl}}/support_contact)에 문의하세요.

### Braze 대시보드가 로드되지 않거나 예상대로 작동하지 않는 경우 {#braze-dashboard-wont-load-or-work-as-expected}

먼저 다른 브라우저에서 대시보드가 로드되는지 테스트해 보세요. 다른 브라우저에서는 문제가 발생하지 않는 경우, 다음을 시도해 보세요.

- **대시보드 다시 시작:** 로그아웃하고 브라우저를 종료한 다음 대시보드에 다시 로그인해 보세요.
- **로컬 브라우저 새로고침:** [쿠키 및 브라우저 캐시를 삭제](#clearing-your-browser-cache-and-cookies)한 후 대시보드에 다시 로그인해 보세요.
- **호환되는 플러그인 또는 서드파티 도구 사용:** 광고 차단기나 보안 소프트웨어가 Braze 대시보드 로딩을 방해할 수 있습니다. 광고 차단기를 비활성화한 후 Braze 대시보드에 로그인하여 테스트해 보세요.
        - 브라우저 콘솔 로그도 확인할 수 있습니다. `ERR_BLOCKED_BY_CLIENT` 관련 오류는 콘텐츠가 광고 차단기에 의해 차단되고 있음을 나타낼 수 있습니다.
- **연결 품질 확인:** 연결 품질이 좋지 않을 수 있습니다. 다른 기기에서 Braze 대시보드에 로그인해 보세요.
- **올바른 클러스터에 접근 중인지 확인:** 회사에 할당된 클러스터에 로그인하고 있는지 확인하세요. 예를 들어 US-03에 할당되어 있지만 US-01에 로그인하고 있을 수 있습니다.
- **브라우저 업데이트:** 브라우저를 최신 [지원 브라우저](#supported-browsers)로 업데이트한 후 대시보드에 로그인해 보세요.

모든 브라우저에서 문제가 발생하는 경우, 다음을 시도해 보세요.

- **네트워크 연결 확인:** 가능하면 VPN을 끄거나 네트워크 연결을 비활성화했다가 다시 활성화해 보세요.
- **기기 재시작:** 기기를 재시작한 후 Braze 대시보드에 로그인해 보세요.

위의 문제를 해결했지만 대시보드가 여전히 로드되지 않거나 예상대로 작동하지 않는 경우, [지원팀]({{site.baseurl}}/user_guide/administer/personal/braze_support)에 문의하세요.

### 사용자가 어떤 워크스페이스에도 속하지 않은 경우 {#the-user-belongs-to-no-workspace}

관리자는 **설정** > **사용자 관리**로 이동하여 사용자의 워크스페이스 수준 권한을 확인하고 필요한 워크스페이스를 **워크스페이스**에 추가하여 이를 해결할 수 있습니다.

### 신규 사용자를 위한 문제 해결 {#troubleshooting-as-a-new-user}

처음으로 Braze에 로그인하거나 계정에 접근하는 데 문제가 있는 신규 사용자라면, 다음 단계에 따라 일반적인 문제를 해결하세요.

#### 환영 이메일을 받지 못한 경우 {#i-never-received-the-welcome-email}

- 스팸 폴더 확인: 계정 활성화 이메일이 스팸 또는 정크 폴더로 필터링되지 않았는지 확인하세요.
- 이메일 주소 확인: 관리자에게 새 Braze 계정에 연결된 이메일 주소가 올바른지 확인해 달라고 요청하세요.
- IT 정책: IT 팀에 활성화 이메일 수신을 방해하는 정책이 있는지 확인하세요.

#### 이메일을 받았지만 2단계 인증(2FA) 설정에서 막힌 경우 {#i-received-the-email-but-im-stuck-setting-up-two-factor-authentication-2fa}

2FA 설정 중 **설정 시작**을 선택했지만 인증 코드(SMS 또는 이메일)를 받지 못하거나 인증 앱 설정을 완료할 수 없는 경우, 브라우저 확장 프로그램, 쿠키 설정 또는 네트워크 제한이 방해하고 있을 수 있습니다. 다음을 시도해 보세요.

- 광고 차단기 비활성화 및 서드파티 쿠키 활성화: 광고 차단기나 개인정보 보호 확장 프로그램이 2FA 인증 흐름을 차단할 수 있습니다. 일시적으로 비활성화하고 브라우저 설정에서 서드파티 쿠키가 활성화되어 있는지 확인하세요.
- 다른 브라우저 사용: 브라우저별 문제를 배제하기 위해 다른 브라우저로 전환해 보세요.
- 네트워크 전환: 회사 네트워크를 사용 중인 경우, 방화벽 정책이 2FA 설정에 영향을 줄 수 있습니다. 개인 연결이나 모바일 핫스팟으로 전환해 보세요.
- 브라우저 설정 전에 인증 앱 설치: 설정 중 **인증 앱**을 선택하기 전에 모바일 기기에 인증 앱(예: Authy, Google Authenticator 또는 LastPass Authenticator)을 다운로드하고 설치하세요.
- 오래된 인증 프로필 삭제: 이전에 인증 앱 설정을 시작했지만 완료하지 못한 경우, 앱에서 오래된 프로필을 삭제하고 QR 코드를 다시 스캔하세요.

이러한 단계를 시도한 후에도 문제가 계속되는 경우:

- 2FA 재설정: 관리자가 설정에서 사용자 계정의 2FA를 재설정할 수 있습니다.
- 사용자 다시 추가: 문제가 지속되면 관리자가 대시보드에서 사용자 계정을 삭제하고 다시 추가할 수 있습니다. 이렇게 하면 동일한 세부 정보로 사용자를 다시 생성할 수 있습니다.

이러한 단계를 수행한 후에도 문제가 계속되면 [지원팀]({{site.baseurl}}/user_guide/administer/personal/braze_support)에 문의하여 추가 도움을 받으세요.

## 다음 단계 {#next-steps}

계정에 접근한 후 다음 리소스를 살펴보세요:

{% article_tiles %}
- name: Braze 대시보드
  link: /docs/user_guide/administer/personal/the_braze_dashboard
- name: 언어 설정
  link: /docs/user_guide/administer/personal/language_settings
{% endarticle_tiles %}