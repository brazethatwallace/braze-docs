---
nav_title: SAML SSO 설정
article_title: SAML SSO 설정
page_order: 0
page_type: tutorial
toc_headers: h2
description: "이 문서에서는 Braze 계정에 SAML SSO를 활성화하는 방법을 안내합니다."
---

# 서비스 공급자(SP) 시작 로그인 {#service-provider-sp-initiated-login}

> 이 문서에서는 Braze 계정에 SAML SSO를 활성화하는 방법과 SAML 트레이스를 얻는 방법을 안내합니다.

## 요구 사항 {#requirements}

설정 시 로그인 URL과 Assertion Consumer Service(ACS) URL을 입력하라는 메시지가 표시됩니다.

| 요구 사항 | 세부 사항 |
|---|---|
| Assertion Consumer Service(ACS) URL | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br><br> 유럽 연합 도메인의 경우, ACS URL은 `https://<SUBDOMAIN>.braze.eu/auth/saml/callback`입니다. <br><br> 일부 IdP에서는 이를 Reply URL, Sign-On URL, Audience URL 또는 Audience URI라고도 합니다. |
| 엔티티 ID | 기본값은 `braze_dashboard`입니다. IdP에서 회사별 엔티티 ID를 요구하는 경우, **보안 설정**에서 **커스텀 엔티티 ID**를 활성화하고 `braze_dashboard_<companyID>`를 사용하세요. |
| RelayState API 키 | **설정** > **설정 및 테스트** > **API 및 식별자**로 이동하여 **API 키** 탭을 열고 `sso.saml.login` 권한이 있는 API 키를 생성하세요. 생성된 API 키를 IdP 내의 `RelayState` 매개변수로 입력하세요. 자세한 단계는 [RelayState 설정](#setting-up-your-relaystate)을 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="요구 사항" }

## SAML SSO 설정 {#setting-up-saml-sso}

### 1단계: ID 공급자 구성 {#step-1-configure-your-identity-provider}

다음 정보를 사용하여 ID 공급자(IdP)에서 Braze를 서비스 공급자(SP)로 설정합니다. 또한 SAML 속성 매핑도 설정합니다.

{% alert important %}
Okta를 ID 공급자로 사용할 계획이라면 [Okta 사이트](https://www.okta.com/integrations/braze/)에서 제공하는 사전 구축된 통합을 사용하세요.
{% endalert %}

| SAML 속성 | 필수 여부 | 허용되는 SAML 속성 |
|---|---|---|
|`email` | 필수 | `email` <br> `mail` <br> `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/email` |
| `first_name` | 선택 사항 | `first_name` <br> `firstname` <br> `firstName`<br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/first_name` |
| `last_name` | 선택 사항 | `last_name` <br> `lastname` <br> `lastName` <br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/last_name` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="1단계: ID 공급자 구성" }

{% alert note %}
Braze는 SAML 어설션에서 `email`만 필수로 요구합니다.
{% endalert %}

### 2단계: Braze 구성 {#step-2-configure-braze}

ID 공급자에서 Braze 설정을 완료하면, ID 공급자가 Braze 계정에 입력할 대상 URL과 `x.509` 인증서를 제공합니다.

계정 매니저가 계정에 SAML SSO를 활성화한 후, **설정** > **회사 설정** > **관리자 설정** > **보안 설정**으로 이동하여 SAML SSO 섹션을 **켜기**로 토글합니다.

같은 페이지에서 다음 정보를 입력합니다.

| 요구 사항 | 세부 정보 |
|---|---|
| SAML 이름 | 로그인 화면에서 버튼 텍스트로 표시됩니다.<br>일반적으로 "Okta"와 같은 ID 공급자의 이름입니다. |
| 대상 URL | IdP 내에서 Braze를 설정한 후 제공됩니다.<br> 일부 IdP에서는 이를 SSO URL 또는 SAML 2.0 엔드포인트라고 합니다. |
| 인증서 | ID 공급자가 제공하는 `x.509` 인증서입니다.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="2단계: Braze 구성" }

### 커스텀 엔티티 ID {#custom-entity-id}

기본적으로 Braze는 엔티티 ID(일부 IdP에서는 오디언스 또는 오디언스 URI라고도 함)로 `braze_dashboard`를 사용합니다. IdP에서 회사별 엔티티 ID가 필요한 경우:

1. **보안 설정**에서 **커스텀 엔티티 ID**를 켭니다.
2. 생성된 엔티티 ID(`braze_dashboard_<companyID>`)를 복사합니다.
3. 해당 값을 IdP의 엔티티 ID, 오디언스 또는 오디언스 URI 필드에 붙여넣습니다.
4. 로그인을 테스트하기 전에 Braze와 IdP 모두에서 변경 사항을 저장합니다.

{% alert important %}
엔티티 ID가 Braze와 IdP 양쪽에서 일치할 때까지 사용자는 로그인할 수 없습니다. 커스텀 엔티티 ID를 사용하려면 ID 공급자에서 추가 구성이 필요합니다.
{% endalert %}

대시보드에 `x.509` 인증서를 추가할 때 다음 형식을 따르는지 확인합니다.

```
-----BEGIN CERTIFICATE-----
<certificate>
-----END CERTIFICATE-----
```

![토글이 선택된 SAML SSO 설정.]({% image_buster /assets/img/samlsso.png %})

### 3단계: Braze에 로그인 {#step-3-sign-into-braze}

보안 설정을 저장하고 로그아웃합니다. 그런 다음 ID 공급자를 사용하여 다시 로그인합니다.

## 커스텀 엔티티 ID 사용하기 {#using-a-custom-entity-id}

기본적으로 모든 Braze 대시보드는 공유 엔티티 ID `braze_dashboard`를 사용합니다. 커스텀 엔티티 ID를 사용하면 대시보드에 고유 식별자를 부여하여, ID 공급자가 로그인 요청이 해당 대시보드를 위한 것인지 확인할 수 있습니다. 동일한 ID 공급자에서 여러 Braze 회사에 대해 SAML SSO를 설정하는 경우에 유용합니다.

커스텀 엔티티 ID 사용은 선택 사항입니다. 활성화하지 않으면 대시보드는 계속 `braze_dashboard`를 사용합니다.

{% alert warning %}
사전 구축된 [Braze Okta 마켓플레이스 앱](https://www.okta.com/integrations/braze/)은 공유 엔티티 ID `braze_dashboard`를 적용하며, 커스텀 엔티티 ID와는 호환되지 않습니다. Braze Okta 마켓플레이스 앱으로 SAML SSO를 이미 설정한 상태에서 커스텀 SAML 앱을 통해 Okta의 엔티티 ID 필드를 업데이트하지 않고 커스텀 엔티티 ID를 켜면 로그인이 중단되어 사용자가 대시보드에 접근하지 못하게 될 수 있습니다. Okta에서 커스텀 엔티티 ID를 사용하려면 커스텀 SAML 앱을 대신 설정하세요.
{% endalert %}

### 1단계: 커스텀 엔티티 ID 켜기 {#step-1-turn-on-the-custom-entity-id}

**설정** > **관리자 설정** > **보안 설정**으로 이동하여 SAML SSO 섹션을 엽니다. **커스텀 엔티티 ID** 토글을 켭니다. Braze가 `braze_dashboard_<COMPANY_ID>` 형식으로 대시보드의 고유 엔티티 ID를 생성합니다. **커스텀 엔티티 ID** 옵션이 보이지 않으면 Braze 계정 매니저에게 문의하세요.

### 2단계: ID 공급자 업데이트 {#step-2-update-your-identity-provider}

생성된 엔티티 ID를 복사하여 ID 공급자의 Braze 애플리케이션에 있는 엔티티 ID 필드에 붙여넣습니다. 공급자에 따라 이 필드의 레이블이 **Entity ID**, **Audience** 또는 **Audience URI**로 표시될 수 있습니다.

{% alert important %}
엔티티 ID는 Braze와 ID 공급자 양쪽에서 일치해야 합니다. 양쪽이 동일한 값을 사용할 때까지 사용자는 SAML SSO로 로그인할 수 없습니다. 사용자가 잠기는 것을 방지하려면 이 페이지를 저장하기 전에 ID 공급자를 먼저 업데이트하세요.
{% endalert %}

### 3단계: 저장 및 테스트 {#step-3-save-and-test}

보안 설정을 저장하고 로그아웃한 다음, ID 공급자를 통해 다시 로그인하여 커스텀 엔티티 ID로 로그인이 정상적으로 작동하는지 확인합니다.

## RelayState 설정하기 {#setting-up-your-relaystate}

1. Braze에서 **설정** > **설정 및 테스트** > **API 및 식별자**로 이동합니다.
2. **API 키** 탭에서 **API 키 생성** 버튼을 선택합니다.
3. **API 키 이름** 필드에 키 이름을 입력합니다.
4. **권한** 아래 **SSO** 드롭다운을 펼치고 **sso.saml.login**을 체크합니다.
5. **API 키 생성**을 선택합니다.
6. **API 키** 탭에서 생성한 API 키 옆의 식별자를 복사합니다.
7. RelayState API 키를 IdP의 RelayState에 붙여넣습니다(IdP에 따라 "Relay State" 또는 "Default Relay State"로 표시될 수도 있습니다).

## IdP 시작 로그인 {#idp-initiated-login}

일부 ID 공급자는 IdP 시작 로그인을 지원하며, 이 경우 사용자는 Braze 로그인 페이지 대신 IdP 포털에서 시작합니다. IdP 시작 로그인에는 유효한 RelayState API 키와 올바른 ACS URL 구성이 필요합니다. 공급자별 설정 가이드는 다음과 같습니다:

- [Okta]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/okta)
- [OneLogin]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/onelogin)
- [Microsoft Entra SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso)

{% alert note %}
Microsoft Entra SSO IdP 시작 로그인을 사용하려면 **Sign-On URL** 필드를 비워 두어야 합니다. 자세한 내용은 [Microsoft Entra SSO]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso)를 참조하세요.
{% endalert %}

## SSO 동작 {#sso-behavior}

SSO를 사용하기로 선택한 멤버는 더 이상 비밀번호를 사용할 수 없습니다. 비밀번호를 계속 사용하는 사용자는 다음 설정에 의해 제한되지 않는 한 계속 사용할 수 있습니다.

## 제한 {#restriction}

조직 구성원이 Google SSO 또는 SAML SSO로만 로그인하도록 제한할 수 있습니다. 제한을 활성화하려면 **설정** > **회사 설정** > **관리자 설정** > **보안 설정**으로 이동하여 **Google SSO 전용 로그인 적용** 또는 **커스텀 SAML SSO 전용 로그인 적용**을 선택합니다.

![최소 비밀번호 길이 8자, 비밀번호 재사용 3회로 설정된 인증 규칙 섹션의 예시. 비밀번호는 180일 후에 만료되며, 사용자는 1,440분 동안 비활성 상태이면 로그아웃됩니다.]({% image_buster /assets/img/sso3.png %})

제한을 활성화하면 회사의 Braze 사용자는 이전에 비밀번호로 로그인한 적이 있더라도 더 이상 비밀번호를 사용하여 로그인할 수 없습니다.

{% alert important %}
SSO가 적용된 후에는 SSO 인증이 실패할 경우 대체 로그인 옵션이 없습니다. SSO 적용을 활성화하기 전에 SSO 구성이 올바른지, 모든 인증서가 최신 상태이며 갱신되었는지, 보안 설정이 올바르게 관리되고 있는지 확인하여 로그인 문제를 방지하세요.
{% endalert %}

## SAML 트레이스 획득하기 {#obtaining-a-saml-trace}

SSO와 관련된 로그인 문제가 발생하는 경우, SAML 트레이스를 획득하면 SAML 요청에서 전송되는 내용을 식별하여 SSO 연결 문제를 해결하는 데 도움이 됩니다.

### 사전 요구 사항 {#prerequisites}

SAML 트레이스를 실행하려면 SAML 트레이서가 필요합니다. 브라우저에 따라 두 가지 옵션이 있습니다:

- [Google Chrome](https://chromewebstore.google.com/detail/saml-tracer/mpdajninpobndbfcldcmbpnnbhibjmch)
- [Mozilla Firefox](https://addons.mozilla.org/en-US/firefox/addon/saml-tracer/)

### 1단계: SAML 트레이서 열기 {#step-1-open-the-saml-tracer}

브라우저 탐색 바에서 SAML 트레이서를 선택합니다. **Pause**가 선택되어 있지 않은지 확인하세요. 선택되어 있으면 SAML 트레이서가 SAML 요청에서 전송되는 내용을 캡처하지 못합니다. SAML 트레이서가 열리면 트레이스가 채워지는 것을 확인할 수 있습니다.

![Google Chrome용 SAML 트레이서.]({% image_buster /assets/img/saml_tracer_example.png %})

### 2단계: SSO를 사용하여 Braze에 로그인 {#step-2-sign-into-braze-using-sso}

Braze 대시보드로 이동하여 SSO를 사용하여 로그인을 시도합니다. 오류가 발생하면 SAML 트레이서를 열고 다시 시도합니다. `https://dashboard-XX.braze.com/auth/saml/callback`과 같은 URL과 주황색 SAML 태그가 있는 행이 표시되면 SAML 트레이스가 성공적으로 수집된 것입니다.

### 3단계: 내보내기 및 Braze에 전송 {#step-3-export-and-send-to-braze}

**Export**를 선택합니다. **Select cookie-filter profile**에서 **None**을 선택합니다. 그런 다음 **Export**를 선택합니다. 이렇게 하면 추가 문제 해결을 위해 Braze 지원팀에 보낼 수 있는 JSON 파일이 생성됩니다.

![옵션 'None'이 선택된 'SAML 트레이스 내보내기 환경설정' 메뉴.]({% image_buster /assets/img/export_saml_trace_preferences.png %})

## 문제 해결 {#troubleshooting}

### 사용자의 이메일 주소가 올바르게 설정되어 있나요? {#is-the-users-email-address-correctly-set-up}

`ERROR_CODE_SSO_INVALID_EMAIL` 오류가 발생하면 사용자의 이메일 주소가 유효하지 않은 것입니다. SAML 추적에서 `saml2:Attribute Name="email"` 필드가 사용자가 로그인에 사용하는 이메일 주소와 일치하는지 확인합니다. Microsoft Entra ID(이전의 Azure 액티브 디렉토리)를 사용하는 경우 속성 매핑은 `email = user.userprincipalname`입니다.

이메일 주소는 대소문자를 구분하며, Braze에서 설정된 주소(Okta, OneLogin, Microsoft Entra ID 등 ID 공급자에서 구성된 주소 포함)와 정확히 일치해야 합니다.

사용자의 이메일 주소에 문제가 있음을 나타내는 다른 오류는 다음과 같습니다:
- `ERROR_CODE_SSO_EMAIL_DOES_NOT_EXIST`: 사용자의 이메일 주소가 대시보드에 존재하지 않습니다.
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISSING`: 사용자의 이메일 주소가 비어 있거나 잘못 구성되어 있습니다.
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISMATCH` 또는 `ERROR_CODE_SSO_SIGN_IN_EMAIL_MISMATCH`: 사용자의 이메일 주소가 SSO 설정에 사용된 주소와 일치하지 않습니다.

### 유효한 SAML 인증서(x.509 인증서)를 가지고 있나요? {#do-you-have-a-valid-saml-certificate-x509-certificate}

[이 SAML 검증 도구](https://www.samltool.com/validate_response.php)를 사용하여 SAML 인증서를 검증할 수 있습니다. 만료된 SAML 인증서도 유효하지 않은 SAML 인증서입니다.

### 올바른 SAML 인증서(x.509 인증서)를 업로드했나요? {#did-you-upload-a-correct-saml-certificate-x509-certificate}

SAML 추적의 `ds:X509Certificate` 섹션에 있는 인증서가 Braze에 업로드한 인증서와 일치하는지 확인합니다. 여기에는 `-----BEGIN CERTIFICATE-----` 헤더와 `-----END CERTIFICATE-----` 푸터는 포함되지 않습니다.

### SAML 인증서(x.509 인증서)를 잘못 입력하거나 형식을 잘못 지정했나요? {#did-you-mistype-or-misformat-your-saml-certificate-x509-certificate}

Braze 대시보드에 제출한 인증서에 공백이나 여분의 문자가 없는지 확인합니다.

Braze에 인증서를 입력할 때 PEM(Privacy Enhanced Mail) 인코딩 및 올바른 형식(`-----BEGIN CERTIFICATE-----` 헤더와 `-----END CERTIFICATE-----` 푸터 포함)이어야 합니다.

다음은 올바르게 형식이 지정된 인증서 예시입니다:

```
-----BEGIN CERTIFICATE-----
THIS_IS_A_MOCKED_CERTIFICATE_4ysJLTzETANBgkqhkiG9w0BAQsFADA0MTIwMAYDVQQDEylNaWNyb3NvZnQgQXp1cmUgRmVkZXJhdGVkIFNTTyBDZXJ0aWZpY2F0ZTAeFw0yMjA1MjcwOTA4MzFaFw0yNTAbMjcwOTA4MzFaMDQxMjAwBgNVBAMTKU1pY3Jvca9mdCBBenVyZSBGZWRlcmF0ZWQgU1NPIENlcnAFWAOKGPAWIGKJPOAMWANBgkqhkiG9w0BAQEFAAaCAQ8AMIIBCgKCAQEA1+KFJwxoac6jdFztQd+vQu59qM8rgfX5RICk0ODfpXkuDUNudcI0XmOAkKHRoMNPYlmMEf5NSiZ7TMElEPtK9zZlpAoSchxxC0Ndegc1AMFi7i2BsEIqPwrer0G6kx2vuAjdrDROPPafkmwalkfmklaw23FlYmV7doE0Vrj2WxR1PG0eFAdsxPLsO1ny55fPj2ibwaqc0XpDkfTrO9GnFvmZAS8ebYtLZsYAMAGLKWAMLGKAWMLKMFDW6vBDaK290s9FdaWza3GPHTcDstawRhyqbXpVjiqpQ0mtxANW4WduSiohhpeqv05TlSOhx87QalkfmwalfmAWMFLKQEBCwUAA4IBAQBdZ5E9FqICfL1q+G6D1tChKl1Y6I6IVULQb4LESSJRaxv53nakmflwakmMALKFMWOYKAeUWO2hdED54qGMgUnLL6YheQBrsm6ilBC68F7ZFmIzVKycvw65yamWbTMi2f2lF60GNYMrq8sGQUkgO0O2zTN07J9wGTe9M+MAFLKWAMFLKalkmflkawoij4jpcsLXXFZJoHSXnF3+qQuzu+49D6pR2lF7DDW+5+PRoc1QpDSytdXxWzItsjQ6IFRuvIGsbrMg0FVaze7ePdKrc47wSlElno7SQ0H+6g40q25rsDSLO
-----END CERTIFICATE-----
```

### 사용자의 세션 토큰이 유효한가요? {#is-the-users-session-token-valid}

해당 사용자에게 [브라우저의 캐시와 쿠키를 삭제](https://its.uiowa.edu/services/how-clear-cache-and-cookies-your-web-browser)하도록 안내한 다음, SAML SSO로 다시 로그인을 시도합니다.

### RelayState를 설정했나요? {#did-you-set-your-relaystate}

`ERROR_CODE_SSO_INVALID_RELAY_STATE` 오류가 발생하면 RelayState가 잘못 구성되었거나 존재하지 않을 수 있습니다. 아직 설정하지 않았다면 IdP 관리 시스템에서 RelayState를 설정해야 합니다. 단계별 안내는 [RelayState 설정하기](#setting-up-your-relaystate)를 참조합니다.

### SSO 로그인에 성공해도 Braze 로그인 페이지로 돌아가나요? {#does-successful-sso-sign-in-return-you-to-the-braze-login-page}

RelayState가 올바르게 구성되지 않았을 때 이 현상이 발생할 수 있습니다. **설정** > **설정 및 테스트** > **API 및 식별자**에서 IdP 로그인용 API 키를 생성하고 해당 API 키를 IdP의 `RelayState` 매개변수로 설정했는지 확인합니다. RelayState는 로그인하려는 회사 계정을 식별합니다. 단계별 안내는 [RelayState 설정하기](#setting-up-your-relaystate)를 참조합니다.

여전히 로그인할 수 없는 경우, 가능하면 SAML 추적과 함께 [Braze 지원팀에 문의]({{site.baseurl}}/user_guide/administer/personal/braze_support)합니다. 추적 캡처에 대한 도움말은 [SAML 추적 얻기](#obtaining-a-saml-trace)를 참조합니다.

### 사용자가 Okta와 Braze 사이에서 로그인 루프에 빠져 있나요? {#is-the-user-stuck-in-a-sign-in-loop-between-okta-and-braze}

사용자가 Okta SSO와 Braze 대시보드 사이에서 계속 순환하며 로그인할 수 없는 경우, Okta에서 SSO URL 대상을 해당 [Braze 인스턴스]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)(예: `https://dashboard-07.braze.com`)로 설정해야 합니다.

다른 IdP를 사용하는 경우, 회사에서 올바른 SAML 또는 x.509 인증서를 Braze에 업로드했는지 확인합니다.

### 수동 통합을 사용하고 있나요? {#are-you-using-a-manual-integration}

회사에서 IdP의 앱 스토어에서 Braze 앱을 다운로드하지 않은 경우, 사전 구축된 통합을 다운로드해야 합니다. 예를 들어, Okta가 IdP인 경우 Okta의 [통합 페이지](https://www.okta.com/integrations/braze/)에서 Braze 앱을 다운로드합니다.

## Google SSO

회사에서 커스텀 SAML 대신 Google SSO를 사용하는 경우, Braze 계정 매니저에게 워크스페이스에 대한 Google SSO 활성화를 요청하세요. 활성화된 후 **설정** > **회사 설정** > **관리자 설정** > **보안 설정**으로 이동하여 **Google SSO 전용 로그인 적용**을 선택하면 모든 회사 사용자에게 Google 인증을 요구할 수 있습니다.

Google SSO 적용이 활성화되면 사용자는 Google 인증으로 로그인해야 하며 더 이상 Braze 비밀번호를 사용할 수 없습니다. 각 사용자는 Braze 대시보드 이메일 주소와 일치하는 Google 계정으로 로그인해야 합니다. 로그인 시 다른 Google 계정을 선택하면 Braze가 인증 시도를 거부합니다.

### Google SSO 로그인 문제 해결 {#troubleshooting-google-sso-sign-in}

일부 사용자가 Google SSO로 로그인할 수 없는 경우 다음을 확인하세요:

- 사용자의 Google 계정 이메일이 Braze 대시보드 이메일 주소와 정확히 일치하는지 확인합니다.
- 사용자가 회사 이메일 주소에 대한 Google 계정에 접근할 수 있는지 확인합니다.
- 사용자가 Braze에서 정지되지 않았는지 확인합니다(**설정** > **회사 사용자**).

## 다음 단계 {#next-steps}

SAML SSO를 설정한 후 다음을 수행할 수 있습니다.

- 보안 설정에서 [SSO 전용 로그인을 적용]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#single-sign-on-sso-authentication)하여 사용자가 비밀번호로 로그인하는 것을 제한할 수 있습니다.
- [SAML 적시 프로비저닝을 설정]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_just_in_time_provisioning)하여 신규 사용자가 처음 SSO로 로그인할 때 자동으로 Braze 계정을 생성하도록 할 수 있습니다.