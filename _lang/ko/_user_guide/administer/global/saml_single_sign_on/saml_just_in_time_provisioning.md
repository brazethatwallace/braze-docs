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

회사에 대한 예외를 설정하려면 [고객지원]({{site.baseurl}}/braze_support)에 문의하세요.

## 필수 조건 {#prerequisites}

SAML JITP를 사용하려면 SAML SSO가 설정되고 통합되어 있어야 합니다. Google SSO와는 호환되지 않으며, ID 공급자 시작(IdP-initiated) 로그인 워크플로만 지원됩니다.

## SAML Just-in-Time 프로비저닝(JITP) 설정하기 {#setting-up-saml-just-in-time-provisioning-jitp}

Braze 관리자가 다음을 수행하도록 합니다:

1. **설정** > **관리자 설정** > **보안 설정**으로 이동합니다.
2. **SAML SSO** 섹션에서 **Automatic user provisioning** 옵션을 토글하여 켭니다.
3. 새로운 회사 사용자를 추가할 기본 워크스페이스를 선택합니다.
4. 새로운 회사 사용자에게 할당할 기본 권한 세트를 선택합니다. 권한 세트를 생성하는 방법은 [사용자 권한 설정]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)을 참조하세요.
6. 페이지 하단에서 **변경 사항 저장**을 선택합니다.
7. SSO 공급자의 설정에서 Braze 접근이 필요한 모든 사용자를 SSO 공급자의 디렉토리에 추가합니다.
8. 사용자에게 첫 번째 로그인 시 IdP 포털을 통해 Braze에 접근하도록 안내합니다. 이후에는 SAML 싱글 사인온 버튼이 표시되어 향후 로그인에 사용할 수 있습니다.

## 자주 묻는 질문 {#frequently-asked-questions}

### SAML JITP를 비활성화하려면 어떻게 하나요? {#how-do-i-disable-saml-jitp}

JITP를 설정한 후에는 [고객지원에 문의]({{site.baseurl}}/braze_support)하여 비활성화해야 합니다.

## 문제 해결 {#troubleshooting}

### Microsoft Entra ID에서 싱글 사인온 버튼이 표시되지 않음 {#single-sign-button-doesnt-appear-with-microsoft-entra-id}

Braze에 대한 Microsoft Entra의 **Basic SAML Configuration** 양식에서 **Sign-On URL** 필드가 설정되어 있으면, IdP-initiated 로그인 시 사용자에게 SSO 버튼 대신 비밀번호 옵션만 표시될 수 있습니다. 이 문제를 방지하려면 Microsoft Entra 관리 센터에서 Braze를 구성할 때 **Sign-On URL** 필드를 비워 두세요.