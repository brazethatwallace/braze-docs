---
nav_title: 자동화된 사용자 프로비저닝
article_title: 자동화된 사용자 프로비저닝
page_order: 3
page_type: reference
description: "이 참조 문서에서는 자동화된 사용자 프로비저닝을 위해 제공해야 하는 정보와 생성된 SCIM(System for Cross-domain Identity Management) 토큰을 사용하는 방법 및 위치에 대해 설명합니다."
alias: /scim/automated_user_provisioning/

---

# 자동화된 사용자 프로비저닝 {#automated-user-provisioning}

> 자동화된 사용자 프로비저닝을 사용하면 대시보드에서 수동으로 관리하는 대신 API를 통해 Braze 사용자를 생성하고 관리할 수 있습니다. Braze는 SCIM(System for Cross-domain Identity Management)을 통해 이를 지원합니다. 이 문서에서는 제공해야 하는 정보, SCIM 토큰을 생성하는 방법, SCIM API 엔드포인트를 찾는 위치에 대해 안내합니다.

## SCIM 프로비저닝 설정에 접근하기 {#accessing-scim-provisioning-settings}

1. Braze 대시보드에서 **설정** > **관리자 설정** > **SCIM 프로비저닝**으로 이동한 다음 **SCIM 통합 구성**을 선택합니다.
2. **Braze 구성** 단계에서 프로비저닝 방법을 선택하고 접근 설정을 제공합니다.

![프로비저닝 방법을 선택하고 접근 설정을 제공하는 섹션이 있는 SCIM 통합 설정 페이지입니다.]({% image_buster /assets/img_archive/scim_braze_config.png %}){: style="max-width:70%;"}

{: start="3"}
3. **IdP 구성** 단계에서 선택한 프로비저닝 방법에 대한 플랫폼 내의 단계를 따릅니다.

{% tabs %}
{% tab Okta - Braze app %}

{% multi_lang_include alerts/early_access_beta_alert.md feature='The Okta integration' %}

Okta에서 SAML SSO를 위해 Braze 앱을 설정한 경우 **Okta - Braze app** 옵션을 사용합니다. SSO를 위해 커스텀 앱을 설정한 경우 [Okta - Custom app integration]({{site.baseurl}}/user_guide/administer/global/user_management/automated_user_provisioning?tab=okta%20-%20custom%20app%20integration#step-1-set-up-scim-provisioning) 탭의 지침을 따릅니다.

## 1단계: SCIM 프로비저닝 설정하기 {#step-1-set-up-scim-provisioning}

### 1.1단계: SCIM 활성화 {#step-11-enable-scim}

1. Okta에서 **Applications** > **Applications**로 이동한 다음 **Create App Integration**을 선택합니다. 로그인 방법으로 **SAML 2.0**을 선택합니다.
2. 커스텀 앱을 만들기 위해 다음 세부 정보를 입력합니다(이는 Braze [**IdP 구성** 단계](#accessing-scim-provisioning-settings)에 있습니다):
- 앱 로고
- 싱글 사인온 URL
- 오디언스 URL (SP 엔터티 ID)
3. **Finish**를 선택합니다.
4. **General** 탭을 선택합니다.
5. **App Settings** 섹션에서 **Edit**를 선택합니다.
6. **Provisioning** 필드에서 **SCIM**을 선택합니다.

### 1.2단계: 애플리케이션 표시 비활성화 {#step-12-disable-application-visibility}

1. **Application visibility** 필드에서 **Do not display application icon to user** 체크박스를 선택합니다. 이렇게 하면 사용자가 앱을 통해 SSO에 접근하는 것을 방지하며, 이 앱은 SCIM 전용으로 사용됩니다.
2. **Save**를 선택합니다.

### 1.3단계: SCIM 통합 설정하기 {#step-13-set-up-the-scim-integration}

1. **Provisioning** 탭을 선택합니다.
2. **Settings** > **Integration** > **SCIM Connection**에서 **Edit**를 선택하고 **Setup SCIM provisioning** 페이지의 테이블에 표시되는 필드 값을 입력합니다.

### 1.4단계: API 자격 증명 테스트하기 {#step-14-test-the-api-credentials}

**Test API Credentials**를 선택합니다. 통합이 성공하면 확인 메시지가 나타나며 저장할 수 있습니다.

### 1.5단계: 앱에 대한 프로비저닝 활성화하기 {#step-15-enable-provisioning-to-the-app}

1. **Provisioning** > **Settings** > **To App** > **Provisioning to App**에서 **Edit**를 선택합니다.
2. 다음을 활성화합니다:
    - Create Users
    - Update Users Attributes
    - Deactivate Users
3. **Setup SCIM provisioning** 페이지의 테이블에 표시되는 매핑으로 **Attribute Mapping** 섹션을 검토하고 구성합니다.

## 2단계: 앱에 사용자 할당하기 {#step-2-assign-users-to-the-app}

1. **Assignment** 탭을 선택합니다.
2. **Assign**을 선택하고 옵션을 선택합니다.
3. Braze에 접근해야 하는 사용자에게 앱을 할당합니다.
4. 할당이 완료되면 **Done**을 선택합니다.

{% endtab %}
{% tab Okta - Custom app integration %}

{% multi_lang_include alerts/early_access_beta_alert.md feature='The Okta integration' %}

SSO를 위해 커스텀 앱을 설정한 경우 **Okta - Custom app integration** 옵션을 사용합니다. Okta에서 SAML SSO를 위해 Braze 앱을 설정한 경우 [Okta - Braze app]({{site.baseurl}}/user_guide/administer/global/user_management/automated_user_provisioning?tab=okta%20-%20braze%20app#step-1-set-up-scim-provisioning) 탭의 지침을 따릅니다.

## 1단계: SCIM 프로비저닝 설정하기

### 1.1단계: SCIM 활성화

1. Okta에서 Braze 앱으로 이동합니다.
2. **General** 탭을 선택합니다.
3. **App Settings** 섹션에서 **Edit**를 선택합니다.
4. **Provisioning** 필드에서 **SCIM**을 선택합니다.
5. **Save**를 선택합니다.

### 1.2단계: SCIM 통합 설정하기 {#step-12-set-up-scim-integration}

1. **Provisioning** 탭을 선택합니다.
2. **Settings** > **Integration** > **SCIM Connection**에서 **Edit**를 선택하고 **Setup SCIM provisioning** 페이지의 테이블에 표시되는 필드 값을 입력합니다.
3. **Test API Credentials**를 선택하여 API 자격 증명을 테스트합니다.
4. **Save**를 선택합니다.

### 1.3단계: 앱에 대한 프로비저닝 활성화하기 {#step-13-enable-provisioning-to-the-app}

1. **Provisioning** > **Settings** > **To App** > **Provisioning to App**에서 **Edit**를 선택합니다.
2. 다음을 활성화합니다:
    - Create Users
    - Update Users Attributes
    - Deactivate Users
3. **Setup SCIM provisioning** 페이지의 테이블에 표시되는 매핑으로 **Attribute Mapping** 섹션을 검토하고 구성합니다.

## 2단계: 앱에 사용자 할당하기

1. **Assignment** 탭을 선택합니다.
2. **Assign**을 선택하고 옵션을 선택합니다.
3. Braze에 접근해야 하는 사용자에게 앱을 할당합니다.
4. **Done**을 선택합니다.

{% endtab %}
{% tab Entra ID %}

{% multi_lang_include alerts/early_access_beta_alert.md feature='The Entra ID integration' %}

## 1단계: SCIM 프로비저닝 앱 설정하기 {#step-1-set-up-scim-provisioning-app}

### 1.1단계: Microsoft Entra 관리 센터에 로그인하기 {#step-11-log-into-microsoft-entra-admin-center}

Microsoft Entra 관리 센터에 로그인합니다.

### 1.2단계: SCIM 앱 생성 및 설정하기 {#step-12-create-and-set-up-your-scim-app}

1. 탐색 메뉴에서 **Entra ID** > **Enterprise apps**로 이동합니다.
2. **New application**을 선택합니다.
3. **Create your own application**을 선택합니다.
4. 패널에서 앱 이름을 입력합니다.
5. **What are you looking to do with your application?** 섹션에서 **Integrate application you don't find in the gallery (Non-gallery)**를 선택합니다.
6. **Create**를 선택합니다.

### 1.3단계: SCIM 통합 설정하기 {#step-13-set-up-scim-integration}

1. SCIM 애플리케이션의 **Manage** > **Provisioning** 섹션으로 이동합니다.
2. **Connect your application** 또는 **New configuration**을 선택하고 **Setup SCIM provisioning** 페이지의 테이블에 표시되는 필드 값을 입력합니다.

### 1.4단계: 앱에 대한 프로비저닝 활성화하기 {#step-14-enable-provisioning-to-the-app}

1. SCIM 애플리케이션의 **Manage** > **Attribute mapping (Preview)** 섹션으로 이동합니다.
2. **Provision Microsoft Entra ID Users**를 선택합니다.
3. **Setup SCIM provisioning** 페이지의 테이블에 표시되는 속성과 일치하도록 **Attribute Mapping** 섹션을 검토하고 구성합니다.
4. **Attribute Mapping** 페이지를 닫습니다.

## 2단계: 앱에 사용자 할당하기

1. **Manage** > **Users and Groups**로 이동합니다.
2. **Add user/group**을 선택합니다.
3. **None Selected**를 선택하여 앱에 사용자를 할당합니다.
4. **Select** 버튼을 선택하여 할당을 확인합니다.

{% endtab %}
{% tab 커스텀 %}

## 1단계: SCIM 설정 구성하기 {#step-1-configure-your-scim-settings}

- **기본 워크스페이스:** 새 사용자가 기본적으로 추가될 워크스페이스를 선택합니다. [SCIM API 요청]({{site.baseurl}}/post_create_user_account)에서 워크스페이스를 지정하지 않으면 Braze가 사용자를 이 워크스페이스에 할당합니다.
- **서비스 오리진:** SCIM 요청의 오리진 도메인을 입력합니다. Braze는 이를 `X-Request-Origin` 헤더에서 사용하여 요청의 출처를 확인합니다.
- **IP 허용 목록(선택 사항):** SCIM 요청을 특정 IP 주소로 제한할 수 있습니다. 허용할 IP 주소를 쉼표로 구분된 목록 또는 범위로 입력합니다. 각 요청의 `X-Request-Origin` 헤더를 사용하여 요청 IP 주소를 허용 목록과 대조합니다.

## 2단계: SCIM 토큰 생성하기 {#step-2-generate-a-scim-token}

필수 필드를 모두 입력한 후 **SCIM 토큰 생성**을 눌러 SCIM 토큰을 생성하고 SCIM API 엔드포인트를 확인합니다. 페이지를 벗어나기 전에 SCIM 토큰을 반드시 복사하세요. **이 토큰은 한 번만 표시됩니다.**

![마스킹된 값과 복사 버튼이 있는 SCIM API 엔드포인트 및 SCIM 토큰 필드입니다. 토큰 필드 아래에 '토큰 재설정' 버튼이 있습니다.]({% image_buster /assets/img/scim.png %})

Braze는 모든 SCIM 요청에 HTTP `Authorization` 헤더를 통해 SCIM API 베어러 토큰이 포함되어 있어야 합니다.

{% endtab %}
{% endtabs %}