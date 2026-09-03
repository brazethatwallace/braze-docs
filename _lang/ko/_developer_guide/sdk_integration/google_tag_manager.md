---
nav_title: Google tag 매니저
article_title: Google Tag 매니저 with the Braze SDK
platform:
  - Android
  - FireOS
  - Swift
page_order: 1.1
description: "Learn how to initialize the Braze SDK using methods like runtime initialization, delayed initialization, or Google Tag 매니저."

---
## 웹용 Google Tag 매니저 정보 {#google-tag-manager}

Google Tag 매니저(GTM)를 사용하면 프로덕션 코드 릴리스나 엔지니어링 리소스 없이도 웹사이트에 원격으로 태그를 추가, 제거, 편집할 수 있습니다. Braze는 웹 SDK를 위해 다음과 같은 템플릿을 제공합니다:

| 태그 유형 | 사용 사례 |
|--------|--------|
| 초기화 태그 | 이 태그를 사용하면 사이트의 코드를 수정할 필요 없이 [웹 Braze SDK를 통합]({{site.baseurl}}/developer_guide/sdk_integration/?tab=google%20tag%20manager&sdktab=web)할 수 있습니다.|
| 동작 태그 | 이 태그를 사용하면 [Content Cards를 생성]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_using-google-tag-manager)하고, [사용자 속성을 설정]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=google%20tag%20manager&sdktab=web)하고, [데이터 수집을 관리]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?tab=google%20tag%20manager&sdktab=web)할 수 있습니다.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="웹용 Google Tag 매니저 정보" }

## Braze 동작 태그의 태그 시퀀싱 {#tag-sequencing-for-braze-action-tags}

Braze 초기화 태그는 Braze SDK 메서드를 호출하는 모든 태그(예: `braze.getUser()`, `braze.logCustomEvent()`, `braze.logPurchase()`)보다 먼저 실행되어야 합니다. SDK가 초기화되기 전에 이러한 메서드가 실행되면 `Uncaught TypeError: Cannot read properties of undefined (reading 'getUser')`와 같은 오류가 발생할 수 있습니다.

Google Tag 매니저에서 태그 시퀀싱을 구성하려면 다음을 수행합니다:

1. Braze SDK 메서드를 호출하는 태그(예: 커스텀 HTML 태그 또는 Braze 동작 태그)를 엽니다.
2. **Advanced Settings** > **Tag Sequencing**으로 이동합니다.
3. **A tag that fires before [this tag] is fired**를 선택합니다.
4. **Braze Initialization** 태그를 선택합니다.

이렇게 하면 다른 태그가 Braze 메서드를 호출하기 전에 SDK가 완전히 로드됩니다.

자세한 내용은 [커스텀 이벤트의 태그 시퀀싱 확인]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_tag-sequencing)을 참조하세요.

## 문제 해결

### 웹 SDK 세션이 잘못된 사용자에게 귀속되는 경우

GTM이 앱에서 로그인한 사용자를 식별하기 전에 Braze 초기화 또는 이벤트 태그를 실행하면, 세션과 이벤트가 잘못된 프로필에 연결될 수 있습니다. 웹 SDK를 초기화하고, 로그인한 사용자의 `external_id`로 `changeUser()`를 호출한 다음, 이벤트를 기록하거나 속성을 설정하는 태그보다 먼저 `openSession()`을 호출하세요. GTM 태그 시퀀싱 또는 동의 트리거를 사용하여 인증 플로우가 완료된 후에만 Braze 태그가 실행되도록 설정하세요.

### Shopify 또는 스크립트 태그 설치에서의 웹 SDK 콘솔 로깅

Shopify 앱 임베드는 콘솔 로깅이 비활성화된 상태로 웹 SDK를 로드합니다. GTM 초기화 태그 또는 `initialize()` 옵션에서 로깅을 설정하세요. Braze 대시보드에는 이러한 로더에 대한 로깅 제어 기능이 포함되어 있지 않습니다.

브라우저 콘솔에 Braze 로그가 표시되면, 프로덕션에 배포하기 전에 GTM 초기화 태그 또는 커스텀 HTML에서 `enableLogging: true`를 제거하세요. 초기화 후에는 `toggleLogging()` 또는 `?brazeLogging=true` URL 파라미터를 사용하세요. 전체 웹 SDK 옵션은 [상세 로깅]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)을 참조하세요.

Braze가 초기화되지 않거나 이벤트가 예상대로 표시되지 않는 경우, GTM 컨테이너가 게시되었는지, 트리거와 태그 실행 순서가 SDK [수명 주기 및 초기화 전략]({{site.baseurl}}/developer_guide/sdk_integration)과 일치하는지, 그리고 테스트 기기가 Braze 엔드포인트를 차단하고 있지 않은지 확인하세요.

초기화 실패의 경우, Braze 태그 또는 커스텀 태그 제공업체가 예상되는 `actionType`과 파라미터를 수신하는지 확인하세요(이 페이지의 Android, Swift, 웹 탭 참조). GTM에서 실행된 이벤트를 검증하는 동안 상세 로깅을 사용하려면, 해당 탭에서 링크된 플랫폼 통합 가이드에 설명된 대로 플랫폼의 SDK 디버그 로깅을 활성화하세요.