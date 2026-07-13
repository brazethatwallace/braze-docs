---
nav_title: Microsoft Entra SSO
article_title: Microsoft Entra SSO
page_order: 2
page_type: tutorial
description: "이 문서에서는 Braze에서 Microsoft Entra 싱글 사인온 기능을 설정하는 방법을 안내합니다."

---

# Microsoft Entra SSO {#microsoft-entra-sso}

> [Microsoft Entra SSO](https://learn.microsoft.com/en-us/entra/identity/saas-apps/braze-tutorial)는 Microsoft의 클라우드 기반 ID 및 액세스 관리 서비스로, 직원들이 로그인하고 리소스에 액세스할 수 있도록 도와줍니다. Entra SSO를 사용하면 비즈니스 요구 사항에 따라 앱 및 앱 리소스에 대한 액세스를 제어할 수 있습니다.

## 요구 사항 {#requirements}

설정 시 Assertion Consumer Service(ACS) URL을 제공하라는 요청을 받게 됩니다.

| 요구 사항 | 세부 정보 |
|---|---|
| Assertion Consumer Service(ACS) URL | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br> 일부 ID 공급자에서는 이를 Reply URL, Audience URL 또는 Audience URI라고도 합니다. |
| Entity ID | `braze_dashboard`|
| RelayState API 키 | ID 공급자 로그인을 활성화하려면 **설정** > **API 키**로 이동하여 `sso.saml.login` 권한이 있는 API 키를 생성합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="요구 사항" }

## Microsoft Entra SSO 내 서비스 공급자(SP) 시작 로그인 {#service-provider-sp-initiated-login-within-microsoft-entra-sso}

### 1단계: 갤러리에서 Braze 추가 {#step-1-add-braze-from-the-gallery}

1. Microsoft Entra 관리 센터에서 **Identity** > **Applications** > **Enterprise Applications**로 이동한 다음 **New application**을 선택합니다.
2. 검색 상자에서 **Braze**를 검색하고 결과 패널에서 선택한 다음 **Add**를 선택합니다.

### 2단계: Microsoft Entra SSO 구성 {#step-2-configure-microsoft-entra-sso}

1. Microsoft Entra 관리 센터에서 Braze 애플리케이션 통합 페이지로 이동하여 **Single sign-on**을 선택합니다.
2. **Select a single sign-on method** 페이지에서 방법으로 **SAML**을 선택합니다.
3. **Set up Single Sign-On with SAML** 페이지에서 **Basic SAML Configuration**의 편집 아이콘을 선택합니다.
4. [Braze 인스턴스]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints#braze-instances)와 다음 패턴을 결합한 **Reply URL**을 입력하여 IdP 시작 모드로 애플리케이션을 구성합니다: `https://<SUBDOMAIN>.braze.com/auth/saml/callback`.
5. **Relay State** 필드에 Relay State 생성 API 키를 입력하여 RelayState를 구성합니다.

{% alert important %}
**Sign-On URL** 필드를 설정하지 **마세요**. IdP 시작 SAML SSO에 문제가 발생하지 않도록 이 필드를 비워 두세요.
{% endalert %}

{: start="6"}
6. Braze에서 기대하는 특정 형식으로 SAML 어설션을 포맷합니다. 이러한 속성과 값의 형식을 이해하려면 사용자 속성 및 사용자 클레임에 대한 다음 탭을 참조하세요.

{% tabs %}
{% tab 사용자 속성 %}
**Application Integration** 페이지의 **User Attributes** 섹션에서 이러한 값을 관리할 수 있습니다.

다음 속성 쌍을 사용합니다:

- `givenname` = `user.givenname`
- `surname`= `user.surname`
- `emailaddress` = `user.mail`
- `name` = `user.userprincipalname`
- `email` = `user.userprincipalname`
- `first_name` = `user.givenname`
- `last_name` = `user.surname`
- `Unique User Identifier` = `user.userprincipalname`

{% alert important %}
이메일 필드가 Braze에서 사용자에 대해 설정된 것과 일치하는 것이 매우 중요합니다. 대부분의 경우 `user.userprincipalname`과 동일하지만, 다른 구성을 사용하는 경우 시스템 관리자와 협력하여 이러한 필드가 정확히 일치하는지 확인하세요.
{% endalert %}

{% endtab %}
{% tab 사용자 클레임 %}

**Set up Single Sign-On with SAML** 페이지에서 **Edit**를 선택하여 **User Attributes** 대화 상자를 엽니다. 그런 다음 적절한 형식에 따라 사용자 클레임을 편집합니다.

다음 클레임 이름 쌍을 사용합니다:

- `claims/givenname` = `user.givenname`
- `claims/surname` = `user.surname`
- `claims/emailaddress` = `user.userprincipalname`
- `claims/name` = `user.userprincipalname`
- `claims/nameidentifier` = `user.userprincipalname`

{% alert important %}
이메일 필드가 Braze에서 사용자에 대해 설정된 것과 일치하는 것이 매우 중요합니다. 대부분의 경우 `user.userprincipalname`과 동일하지만, 다른 구성을 사용하는 경우 시스템 관리자와 협력하여 이러한 필드가 정확히 일치하는지 확인하세요.
{% endalert %}

**Manage claim** 섹션에서 이러한 사용자 클레임과 값을 관리할 수 있습니다.

{% endtab %}
{% endtabs %}

{: start="8"}
8. **Set up Single Sign-On with SAML** 페이지로 이동한 다음 **SAML Signing Certificate** 섹션으로 스크롤하여 요구 사항에 따라 적절한 **Certificate (Base64)**를 다운로드합니다.
9. **Set up Braze** 섹션으로 이동하여 [Braze 구성](#step-3)에서 사용할 적절한 URL을 복사합니다.

### 3단계: Braze 내에서 Microsoft Entra SSO 구성 {#step-3}

Microsoft Entra 관리 센터에서 Braze를 설정한 후, Microsoft Entra가 타겟 URL(로그인 URL)과 **x.509** 인증서를 제공하며, 이를 Braze 계정에 입력합니다.

계정 매니저가 계정에 대해 SAML SSO를 활성화한 후 다음을 수행합니다:

1. **설정** > **관리자 설정** > **보안 설정**으로 이동하여 SAML SSO 섹션을 **ON**으로 토글합니다.
2. 같은 페이지에서 다음을 추가합니다:

| 요구 사항 | 세부 정보 |
|---|---|
| `SAML Name` | 로그인 화면에서 버튼 텍스트로 표시됩니다. 일반적으로 "Microsoft Entra"와 같은 ID 공급자의 이름입니다. |
| `Target URL` | Microsoft Entra에서 제공하는 로그인 URL입니다.|
| `Certificate` | `x.509` PEM 인코딩 인증서는 ID 공급자가 제공합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="3단계: Braze 내에서 Microsoft Entra SSO 구성" }

{% alert tip %}
Braze 계정 사용자가 SAML SSO로만 로그인하도록 하려면 **회사 설정** 페이지에서 [싱글 사인온 인증을 제한]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#restriction)할 수 있습니다.
{% endalert %}