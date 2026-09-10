---
nav_title: Okta
article_title: Okta
page_order: 3
page_type: tutorial
description: "이 문서에서는 Okta를 사용하여 싱글 사인온을 위해 Braze를 구성하는 방법을 안내합니다."

---

# Okta

> Okta는 모든 기기에서 모든 사람을 모든 애플리케이션과 연결합니다. 클라우드를 위해 구축된 엔터프라이즈급 ID 관리 서비스로, 많은 온프레미스 애플리케이션과 호환됩니다. Okta를 사용하면 IT 팀이 모든 직원의 애플리케이션 또는 기기에 대한 액세스를 관리할 수 있습니다.

{% alert note %}
사전 구축된 Braze Okta 마켓플레이스 앱은 공유 Entity ID `braze_dashboard`를 사용합니다. 이 대시보드에 고유한 Entity ID가 필요한 경우(예: Okta를 통해 여러 Braze 대시보드를 연결하려는 경우) 마켓플레이스 앱 대신 커스텀 SAML 앱을 설정한 다음, [커스텀 Entity ID 사용]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#using-a-custom-entity-id)을 따르세요.
{% endalert %}

## 요구 사항 {#requirements}

| 요구 사항 | 세부 정보 |
| ----------- | ------- |
| 계정에 Okta 활성화 | Braze 계정 매니저에게 연락하여 계정에 Okta를 활성화하세요. |
| Okta 관리자 권한 | Okta를 설정하기 전에 관리자 권한이 있는지 확인하세요. |
| Braze 관리자 권한 | Okta를 설정하기 전에 관리자 권한이 있는지 확인하세요. |
| RelayState API 키 | IdP 로그인을 활성화하려면 **설정** > **설정 및 테스트** > **API 및 식별자**로 이동하여 **API 키** 탭을 열고 `sso.saml.login` 권한이 있는 API 키를 생성하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="요구 사항" }

## 1단계: Braze 구성 {#step-1-configure-braze}

### 1a단계: Braze에서 보안 설정으로 이동 {#step-1a-navigate-to-security-settings-in-braze}

계정 매니저가 계정에 대해 SAML SSO를 활성화한 후, **설정** > **관리자 설정** > **보안 설정**으로 이동하여 SAML SSO 섹션을 **켜기**로 토글합니다.

![보안 설정 페이지에서 Okta SAML SSO가 활성화된 화면.]({% image_buster/assets/img/Okta/okta1.png %})

### 1b단계: SAML SSO 설정 편집 {#step-1b-edit-saml-sso-settings}

Okta 관리자 대시보드에서 Okta가 제공하는 대상 URL(로그인 URL)과 `x.509` 인증서를 Braze 계정의 **보안 설정** 페이지에 입력해야 합니다.

![1b단계 관련 스크린샷: SAML SSO 설정 편집.]({% image_buster /assets/img/Okta/okta5.png %}){: style="max-width:75%"}

| 요구 사항 | 세부 정보 |
|---|---|
| `SAML Name` | 로그인 화면의 버튼 텍스트로 표시됩니다. 일반적으로 ID 제공업체의 이름입니다. 예: "Okta". |
| `Target URL` | Okta 관리자 대시보드에서 제공하는 로그인 URL입니다. **Applications** > 해당 애플리케이션 > **General** 탭 > **App Embed Link** > **Embed Link**로 이동하면 찾을 수 있습니다. |
| `Certificate` | ID 제공업체에서 제공하는 `x.509` PEM 인코딩된 인증서입니다. 이 필드에 복사하여 붙여넣어야 합니다. Okta에서 **SAML Signing Certificates**로 이동한 후 **Actions** > **Download certificate**를 선택하여 가져올 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="1b단계: SAML SSO 설정 편집" }

완료되면 페이지 하단에서 **Save Changes**를 선택합니다.

{% alert note %}
ID 제공업체에서 회사별 SAML 엔티티 ID가 필요하고 계정이 이를 지원하는 경우, **보안 설정**에서 **Custom Entity ID**를 활성화하고 Okta에 `braze_dashboard_<companyID>`를 구성합니다. 기본 엔티티 ID는 `braze_dashboard`입니다. **Custom Entity ID** 설정은 모든 회사에서 사용할 수 있는 것은 아닙니다. 자세한 내용은 [SAML SSO 설정]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#requirements)을 참조하세요.
{% endalert %}

## 2단계: Okta 구성 {#step-2-configure-okta}

Okta에서 Braze SAML 앱의 **Sign On** 탭을 선택한 다음 **Edit**을 클릭합니다.

그런 다음 `sso.saml.login` 권한이 있는 RelayState API 키를 **Default Relay State** 필드에 입력합니다.

![Sign On 탭의 Okta Default RelayState.]({% image_buster /assets/img/Okta/okta2.png %}){: style="max-width:75%"}

이 새 설정을 반드시 저장하세요.

{% alert tip %}
Braze 계정 사용자가 SAML SSO로만 로그인하도록 하려면 **설정** > **회사 설정** > **관리자 설정** > **보안 설정**에서 [SSO 인증을 제한]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup#restriction)할 수 있습니다.
{% endalert %}

## 3단계: 로그인 {#step-3-log-in}

이제 Okta를 사용하여 Braze에 로그인할 수 있습니다!

![Okta SSO가 활성화된 Braze 대시보드 로그인 화면.]({% image_buster /assets/img/Okta/okta4.png %}){: style="max-width:60%"}