### 필수 조건 {#prerequisites}

이 통합 방법을 사용하기 전에 [Google Tag 매니저에 대한 계정과 컨테이너를 생성](https://support.google.com/tagmanager/answer/14842164)해야 합니다.

### 1단계: 태그 템플릿 갤러리 열기 {#step-1-open-the-tag-template-gallery}

[Google Tag 매니저](https://tagmanager.google.com/)에서 워크스페이스를 선택한 다음 **Templates**를 선택합니다. **Tag Template** 창에서 **Search Gallery**를 선택합니다.

![Google Tag Manager의 예제 워크스페이스에 대한 템플릿 페이지입니다.]({% image_buster /assets/img/web-gtm/search_tag_template_gallery.png %}){: style="max-width:95%;"}

### 2단계: 초기화 태그 템플릿 추가 {#step-2-add-the-initialization-tag-template}

템플릿 갤러리에서 `braze-inc`을 검색한 다음 **Braze Initialization Tag**를 선택합니다.

![다양한 'braze-inc' 템플릿을 보여주는 템플릿 갤러리입니다.]({% image_buster /assets/img/web-gtm/template_gallery_results.png %}){: style="max-width:80%;"}

**Add to workspace** > **Add**를 선택합니다.

![Google Tag Manager의 'Braze Initialization Tag' 페이지입니다.]({% image_buster /assets/img/web-gtm/add_to_workspace.png %}){: style="max-width:70%;"}

### 3단계: 태그 구성 {#step-3-configure-the-tag}

**Templates** 섹션에서 새로 추가한 템플릿을 선택합니다.

![Braze Initialization Tag 템플릿을 보여주는 Google Tag Manager의 "Templates" 페이지입니다.]({% image_buster /assets/img/web-gtm/select_tag_template.png %}){: style="max-width:95%;"}

연필 아이콘을 선택하여 **Tag Configuration** 드롭다운을 엽니다.

![연필 아이콘이 표시된 Tag Configuration 타일입니다.]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

필수 최소 정보를 입력합니다:

| 필드         | 설명 |
| ------------- | ----------- |
| **API Key**   | Braze 대시보드의 **Settings** > **App Settings**에서 찾을 수 있는 [Braze API 키]({{site.baseurl}}/api/basics#about-rest-api-keys)입니다. |
| **API Endpoint** | REST 엔드포인트 URL입니다. 엔드포인트는 [인스턴스]({{site.baseurl}}/api/basics#endpoints)에 대한 Braze URL에 따라 달라집니다. |
| **SDK Version**  | [체인지로그]({{site.baseurl}}/developer_guide/changelogs/?sdktab=web)에 나열된 웹 Braze SDK의 가장 최근 `MAJOR.MINOR` 버전입니다. 예를 들어 최신 버전이 `4.1.2`인 경우 `4.1`을 입력합니다. 자세한 내용은 [SDK 버전 관리에 대한 정보]({{site.baseurl}}/developer_guide/sdk_integration/version_management)를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="3단계: 태그 구성" }

추가 초기화 설정을 위해 **Braze Initialization Options**를 선택하고 필요한 옵션을 선택합니다.

!['Tag Configuration' 아래의 Braze Initialization Options 목록입니다.]({% image_buster /assets/img/web-gtm/braze_initialization_options.png %}){: style="max-width:65%;"}

### 4단계: 초기화 옵션 선택 {#step-4-choose-initialization-options}

Braze Initialization Tag는 다음 옵션을 제공합니다. 대부분은 [웹 SDK `InitializationOptions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions)에 직접 매핑되며, 일부는 초기화 중 태그가 호출할 웹 SDK 메서드에 해당합니다. 통합 요구 사항에 맞는 옵션을 선택하세요:

| GTM 옵션 | 웹 SDK 구성 또는 메서드 | 설명 |
| --- | --- | --- |
| **Allow HTML In-App Messages** | `allowUserSuppliedJavascript` | HTML 인앱 메시지, 배너 및 사용자 제공 JavaScript 클릭 동작을 활성화합니다. 커스텀 HTML을 사용하는 [HTML 인앱 메시지]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html) 및 [배너]({{site.baseurl}}/developer_guide/banners/placements/?sdktab=web)에 필요합니다. HTML 및 JavaScript 콘텐츠를 신뢰할 수 있는 경우에만 활성화하세요. 사용자 제공 JavaScript 실행을 허용합니다. |
| **App Version Number** | `appVersion`, `appVersionNumber` | 세분화를 위한 앱 버전입니다(예: `1.2.3.4`). |
| **Automatically Open New Session** | `braze.openSession()` | SDK가 초기화된 후 이 메서드를 자동으로 호출하여 새 세션을 엽니다. |
| **Automatically show new in app messages** | `braze.automaticallyShowInAppMessages()` | 초기화 후 이 메서드를 호출하여 서버에서 도착한 새 인앱 메시지를 자동으로 표시합니다. |
| **Disable Automatic 푸시 토큰 Maintenance** | `disablePushTokenMaintenance` | 새 세션에서 SDK가 Braze 백엔드와 푸시 토큰을 동기화하지 않도록 합니다. |
| **Disable Automatic Service Worker Registration** | `manageServiceWorkerExternally` | 서비스 워커를 직접 등록하고 제어하는 경우 사용합니다. |
| **Disable Cookies** | `noCookies` | 사용자/세션 데이터에 쿠키 대신 localStorage를 사용합니다. 교차 서브도메인 인식을 방지합니다. |
| **Disable Font Awesome** | `doNotLoadFontAwesome` | SDK가 CDN에서 Font Awesome을 로드하지 않도록 합니다. 사이트에 자체 Font Awesome이 있는 경우 사용합니다. |
| **Enable SDK Authentication** | `enableSdkAuthentication` | [SDK 인증]({{site.baseurl}}/developer_guide/sdk_integration/authentication)을 활성화합니다. |
| **Enable Web SDK Logging** | `enableLogging` | 디버깅을 위한 콘솔 로깅을 활성화합니다. 프로덕션 전에 제거하세요. |
| **Minimum Interval Between Triggered Messages** | `minimumIntervalBetweenTriggerActionsInSeconds` | 트리거 동작 간 최소 초(기본값: 30). |
| **Open Cards in New Tab** | `openCardsInNewTab` | 기본 피드 UI를 사용할 때 콘텐츠 카드 링크를 새 탭에서 엽니다. |
| **Service Worker Location** | `serviceWorkerLocation` | 서비스 워커 파일의 커스텀 경로입니다(기본값: `/service-worker.js`). |
| **Session Timeout (seconds)** | `sessionTimeoutInSeconds` | 세션 타임아웃(초)입니다(기본값: 1800). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="4단계: 초기화 옵션 선택" }

{% alert note %}
Google Tag 매니저 Braze Initialization Tag를 사용할 때 [커스텀 HTML 인앱 메시지]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html)를 활성화하려면 **Braze Initialization Options**에서 **Allow HTML In-App Messages**를 선택하세요. 이 체크박스는 `braze.initialize()`의 `allowUserSuppliedJavascript` 초기화 옵션에 매핑되며 `true`로 설정됩니다. Google Tag 매니저 Braze Initialization Tag는 옵션 이름 대신 이 레이블을 사용합니다.
{% endalert %}

GTM 템플릿에서 노출되지 않는 옵션(예: `contentSecurityNonce`, `localization` 또는 `devicePropertyAllowlist`)의 경우 [런타임 초기화]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web)를 대신 사용하세요.

### 5단계: *모든 페이지*에서 트리거되도록 설정 {#step-5-set-to-trigger-on-all-pages}

초기화 태그는 사이트의 모든 페이지에서 실행되어야 합니다. 이를 통해 Braze SDK 메서드를 사용하고 웹 푸시 분석을 기록할 수 있습니다.

{% alert important %}
**태그 시퀀싱:** Braze Initialization 태그는 Braze SDK 메서드를 호출하는 다른 태그(예: `braze.getUser()` 또는 `braze.logCustomEvent()`)보다 먼저 실행되어야 합니다. SDK가 초기화되기 전에 커스텀 이벤트, 사용자 속성 또는 기타 Braze 메서드 호출이 실행되면 `Uncaught TypeError: Cannot read properties of undefined (reading 'getUser')`와 같은 오류가 발생할 수 있습니다. 올바른 시퀀싱을 보장하려면 Braze Initialization 태그를 설정 태그로 구성하거나 GTM의 태그 시퀀싱 기능을 사용하여 먼저 실행되도록 하세요. 자세한 내용은 [Braze 액션 태그의 태그 시퀀싱]({{site.baseurl}}/developer_guide/sdk_integration/google_tag_manager/?sdktab=web#web_tag-sequencing-for-braze-action-tags)을 참조하세요.
{% endalert %}

### 6단계: 통합 확인 {#step-6-verify-your-integration}

다음 옵션 중 하나를 사용하여 통합을 확인할 수 있습니다:

- **옵션 1:** Google Tag 매니저의 [디버깅 툴](https://support.google.com/tagmanager/answer/6107056?hl=en)을 사용하여 Braze Initialization Tag가 구성된 페이지나 이벤트에서 올바르게 트리거되는지 확인할 수 있습니다.
- **옵션 2:** 웹 페이지에서 Braze로 전송되는 네트워크 요청을 확인합니다. 또한 전역 `window.braze` 라이브러리가 정의되어 있어야 합니다.