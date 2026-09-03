---
nav_title: SAML Just-in-Time 프로비저닝
article_title: SAML Just-in-Time 프로비저닝
page_order: 1
page_type: tutorial
description: "이 문서에서는 SAML Just-in-Time 프로비저닝을 구성하여 새로운 회사 사용자가 처음 로그인할 때 Braze 계정을 생성할 수 있도록 하는 방법을 안내합니다."
---

# SAML Just-in-Time 프로비저닝 {#saml-just-in-time-provisioning}

> Just-in-Time 프로비저닝은 [SAML SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup)와 함께 작동하여 새로운 회사 사용자가 처음 로그인할 때 Braze 계정을 생성할 수 있도록 합니다. 이를 통해 관리자가 새로운 회사 사용자의 계정을 수동으로 생성하고, 권한을 선택하고, 워크스페이스에 할당하고, 계정이 활성화될 때까지 기다릴 필요가 없습니다.

보안 조치로서, SAML Just-in-Time 프로비저닝(JITP)은 회사에 이미 존재하는 이메일 도메인을 가진 사용자에게만 작동합니다. JITP는 회사 내에 이미 확인된 비가장 개발자가 한 명 이상 있는 도메인에서만 가능합니다.

예를 들어, `jon.smith@decorumsoft.com` 계정이 JITP를 사용하여 Decorumsoft에 로그인할 수 있다고 가정해 보겠습니다. `jane.smith@decorumsoft.com` 계정은 동일한 도메인을 가지고 있으므로 프로비저닝이 허용될 수 있습니다. 그러나 `jon.smith@decorumsoft.eu`로 JITP를 사용하려고 하면, Decorumsoft Braze 대시보드 내에 `decorumsoft.eu` 계정이 없기 때문에 프로비저닝이 허용되지 않습니다.

회사에 대한 예외를 설정하려면 [고객지원]({{site.baseurl}}/user_guide/administer/personal/braze_support)에 문의하세요.

## 전제 조건 {#prerequisites}

SAML JITP를 사용하려면 SAML SSO가 설정 및 통합되어 있어야 합니다. Google SSO와는 호환되지 않으며, IdP(Identity Provider) 시작 로그인 워크플로만 지원됩니다.

| 요구 사항 | 세부 정보 |
|---|---|
| SAML SSO | JITP를 활성화하기 전에 구성 및 테스트를 완료해야 합니다. [SAML SSO 설정]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup)을 참조하세요. |
| IdP 시작 로그인 | 사용자는 첫 로그인 시 IdP 포털을 통해 로그인해야 합니다. SP 시작 로그인만으로는 새 사용자가 프로비저닝되지 않습니다. |
| 이메일 도메인 | 사용자의 이메일 도메인이 회사에 이미 존재해야 합니다(해당 도메인에 가장이 아닌 확인된 개발자가 최소 한 명 있어야 합니다). |
| 회사 인에이블먼트 | **자동 사용자 프로비저닝** 토글이 표시되려면 Braze에서 회사에 대해 `saml_jit_provisioning` 기능을 활성화해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="JITP 전제 조건" }

{% alert important %}
SAML 적시(just-in-time) 프로비저닝은 Braze에서 회사에 대해 활성화해야 합니다. **자동 사용자 프로비저닝** 토글을 사용할 수 없는 경우 계정 매니저 또는 [Braze 지원팀]({{site.baseurl}}/user_guide/administer/personal/braze_support)에 문의하세요.
{% endalert %}

## JITP 작동 방식 {#how-jitp-works}

JITP가 활성화된 상태에서 새로운 사용자가 IdP를 통해 처음 로그인하면 다음과 같은 과정이 진행됩니다.

1. Braze가 SAML 어설션을 검증하고 사용자의 이메일 도메인이 JITP에 허용되어 있는지 확인합니다.
2. Braze가 SAML 어설션의 이메일을 사용하여 대시보드 사용자 계정을 생성합니다.
3. Braze가 **보안 설정**에서 구성된 기본 워크스페이스와 권한 세트를 할당합니다.
4. 사용자는 별도의 초대나 활성화 단계 없이 즉시 Braze에 접속할 수 있습니다.

JITP는 기존 사용자의 권한을 업데이트하지 않습니다. 회사에 아직 존재하지 않는 사용자에 대해서만 계정을 생성합니다.

## SAML 적시 프로비저닝(JITP) 설정하기 {#setting-up-saml-just-in-time-provisioning-jitp}

Braze 관리자가 다음을 수행하도록 합니다.

1. **설정** > **회사 설정** > **관리자 설정** > **보안 설정**으로 이동합니다.
2. **SAML SSO** 섹션에서 **자동 사용자 프로비저닝** 옵션을 토글하여 켭니다.
3. 새 회사 사용자를 추가할 기본 워크스페이스를 선택합니다.
4. 해당 새 회사 사용자에게 할당할 기본 권한 세트를 선택합니다. 권한 세트를 만드는 방법은 [사용자 권한 설정]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)을 참조하세요.

{% alert note %}
회사에서 세분화된 권한을 사용하는 경우, 마이그레이션 후 기본 권한 세트를 검토하여 새로운 JITP 사용자가 의도한 액세스 권한을 받는지 확인하세요.
{% endalert %}

5. **변경 사항 저장**을 선택합니다.
6. SSO 공급자의 설정에서 Braze 액세스가 필요한 모든 사용자를 SSO 공급자의 디렉터리에 추가합니다.
7. 사용자에게 첫 번째 로그인 시 IdP 포털을 통해 Braze에 접속하도록 안내합니다. 이후에는 SAML SSO 버튼이 표시되어 로그인할 수 있습니다.

## 자주 묻는 질문 {#frequently-asked-questions}

### SAML JITP를 비활성화하려면 어떻게 해야 하나요? {#how-do-i-disable-saml-jitp}

JITP를 설정한 후에는 [지원팀에 문의]({{site.baseurl}}/user_guide/administer/personal/braze_support)하여 비활성화를 요청해야 합니다.

### JITP로 사용자별로 다른 권한을 할당할 수 있나요? {#can-jitp-assign-different-permissions-per-user}

아니요. JITP로 생성된 모든 사용자는 **보안 설정**에서 구성된 기본 워크스페이스와 권한 세트를 부여받습니다. 다른 액세스 권한을 할당하려면 사용자를 수동으로 생성하거나 [SCIM 자동 사용자 프로비저닝]({{site.baseurl}}/scim/automated_user_provisioning)을 사용하세요.

### JITP는 SP 시작 로그인에서도 작동하나요? {#does-jitp-work-with-sp-initiated-login}

아니요. JITP는 사용자가 ID 공급자 포털에서 시작하는 IdP 시작 로그인 중에만 실행됩니다.

## 문제 해결 {#troubleshooting}

### 첫 번째 SSO 로그인 시 사용자가 프로비저닝되지 않은 경우 {#user-was-not-provisioned-on-first-sso-sign-in}

다음 사항을 확인하세요:

- **보안 설정**에서 JITP가 활성화되고 저장되어 있는지 확인합니다.
- 사용자가 Braze 로그인 페이지에서만이 아닌, IdP 포털을 통해 로그인(IdP 시작 방식)했는지 확인합니다.
- 사용자의 이메일 도메인이 회사에 이미 존재하는지 확인합니다.
- SAML 어설션에 사용자가 로그인할 때 사용하는 주소와 일치하는 유효한 `email` 속성이 포함되어 있는지 확인합니다.

### Microsoft Entra ID에서 SSO 버튼이 표시되지 않는 경우 {#single-sign-on-button-doesnt-appear-with-microsoft-entra-id}

Braze용 Microsoft Entra의 **기본 SAML 구성** 양식에 있는 **로그인 URL** 필드로 인해 IdP 시작 로그인 시 사용자에게 SSO 버튼 대신 비밀번호 옵션만 표시될 수 있습니다. 이 문제를 방지하려면 Microsoft Entra 관리 센터에서 Braze를 구성할 때 **로그인 URL** 필드를 비워 두세요.