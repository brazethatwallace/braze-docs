## 웹 Braze SDK에 대하여 {#about-the-web-braze-sdk}

웹 Braze SDK를 사용하면 분석을 수집하고 웹 사용자에게 풍부한 인앱 메시지, 푸시 및 Content Cards 메시지를 표시할 수 있습니다. 자세한 내용은 [Braze JavaScript 참조 설명서](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)를 참조하세요.

{% multi_lang_include archive/web-v4-rename.md %}

## 웹 SDK 통합 {#integrate-the-web-sdk}

다음 방법을 사용하여 웹 Braze SDK를 통합할 수 있습니다. 추가 옵션은 [기타 통합 방법](#web_other-integration-methods)을 참조하세요.

- **코드 기반 통합:** 선호하는 패키지 관리자 또는 Braze CDN을 사용하여 코드베이스에 웹 Braze SDK를 직접 통합합니다. 이렇게 하면 SDK가 로드되고 구성되는 방식을 완전히 제어할 수 있습니다.
- **Google Tag Manager:** 사이트의 코드를 수정하지 않고 웹 Braze SDK를 통합할 수 있는 노코드 솔루션입니다. 자세한 내용은 [Google Tag Manager와 Braze SDK 사용하기]({{site.baseurl}}/developer_guide/sdk_integration/google_tag_manager)를 참조하세요.

{% alert important %}
[NPM 통합 방법]({{site.baseurl}}/developer_guide/sdk_integration/?subtab=package%20manager&sdktab=web)을 사용하는 것을 권장합니다. 이점으로는 SDK 라이브러리를 웹사이트에 로컬로 저장하고, 광고 차단기 확장 프로그램으로부터 면역을 제공하며, 번들러 지원의 일환으로 로드 시간을 단축하는 데 기여하는 것이 포함됩니다.
{% endalert %}

{% tabs local %}
{% tab 코드 기반 통합 %}
### 1단계: Braze 라이브러리 설치 {#step-1-install-the-braze-library}

다음 방법 중 하나를 사용하여 Braze 라이브러리를 설치할 수 있습니다. 그러나 웹사이트가 `Content-Security-Policy`를 사용하는 경우 계속하기 전에 [콘텐츠 보안 정책]({{site.baseurl}}/developer_guide/platforms/web/content_security_policy)을 검토하세요.

{% alert important %}
대부분의 광고 차단기가 Braze 웹 SDK를 차단하지 않지만, 일부 더 제한적인 광고 차단기는 문제를 일으키는 것으로 알려져 있습니다.
{% endalert %}

{% subtabs %}
{% subtab package manager %}
사이트에서 NPM 또는 Yarn 패키지 관리자를 사용하는 경우 [Braze NPM 패키지](https://www.npmjs.com/package/@braze/web-sdk)를 종속성으로 추가할 수 있습니다.

이제 v3.0.0부터 Typescript 정의가 포함됩니다. 2.x에서 3.x로 업그레이드할 때 참고할 사항은 [체인지로그](https://github.com/braze-inc/braze-web-sdk/blob/master/UPGRADE_GUIDE.md)를 참조하세요.

```bash
npm install --save @braze/web-sdk
# or, using yarn:
# yarn add @braze/web-sdk
```

설치가 완료되면 일반적인 방법으로 라이브러리를 `import` 또는 `require`할 수 있습니다:

```typescript
import * as braze from "@braze/web-sdk";
// or, using `require`
const braze = require("@braze/web-sdk");
```
{% endsubtab %}

{% subtab braze cdn %}
라이브러리를 비동기적으로 로드하는 CDN 호스팅 스크립트를 참조하여 Braze 웹 SDK를 HTML에 직접 추가합니다.

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Floading-snippet.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

{% alert important %}
Safari의 기본 **교차 사이트 추적 방지** 설정은 CDN 통합 방법을 사용할 때 배너 및 Content Cards와 같은 인앱 메시지 유형이 표시되지 않도록 할 수 있습니다. 이 문제를 피하려면 NPM 통합 방법을 사용하여 Safari가 이러한 메시지를 교차 사이트 트래픽으로 분류하지 않도록 하고 모든 지원되는 브라우저에서 웹 사용자가 이를 볼 수 있도록 하세요.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}

### 2단계: SDK 초기화 {#step-2-initialize-the-sdk}

Braze 웹 SDK가 웹사이트에 추가된 후, Braze 대시보드 내의 **설정** > **앱 설정**에서 찾은 API 키 및 [SDK 엔드포인트 URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints)로 라이브러리를 초기화하세요. `braze.initialize()`에 대한 옵션의 전체 목록과 다른 JavaScript 메서드는 [Braze JavaScript 설명서](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)를 참조하세요.

{% alert note %}
**웹 SDK 요청을 위한 커스텀 도메인은 지원되지 않습니다**: 웹 SDK `baseUrl`은 Braze SDK 엔드포인트여야 합니다(예: `sdk.iad-05.braze.com`). Braze는 고객 소유 도메인을 통해 CNAME 레코드를 사용하여 웹 SDK 트래픽을 라우팅하는 것을 지원하지 않습니다. 웹 SDK 요청이 귀하의 도메인에서 시작되도록 하려면 Braze 고객지원에 문의하세요.
{% endalert %}

```javascript
// initialize the SDK
braze.initialize('YOUR-API-KEY-HERE', {
    baseUrl: "YOUR-SDK-ENDPOINT-HERE",
    enableLogging: false, // set to `true` for debugging
    allowUserSuppliedJavascript: false, // set to `true` to support custom HTML messages
});

// Enable automatic display of in-app messages
// Required if you want in-app messages to display automatically when triggered
braze.automaticallyShowInAppMessages();

// if you use Content Cards
braze.subscribeToContentCardsUpdates(function(cards){
    // cards have been updated
});

// optionally set the current user's external ID before starting a new session
// you can also call `changeUser` later in the session after the user logs in
if (isLoggedIn){
    braze.changeUser(userIdentifier);
}

// `openSession` should be called last - after `changeUser` and `automaticallyShowInAppMessages`
braze.openSession();
```

{% alert important %}
**인앱 메시지 표시**: 트리거될 때 인앱 메시지를 자동으로 표시하려면 `braze.automaticallyShowInAppMessages()`를 호출해야 합니다. 이 호출이 없으면 인앱 메시지가 자동으로 표시되지 않습니다. 메시지 표시를 수동으로 관리하려면 이 호출을 제거하고 대신 `braze.subscribeToInAppMessage()`를 사용하세요. 자세한 내용은 [인앱 메시지 전달]({{site.baseurl}}/developer_guide/in_app_messages/delivery)을 참조하세요.
{% endalert %}

#### 익명 사용자의 세션 누락 문제 해결 {#troubleshooting-missing-sessions-for-anonymous-users}

"세션 누락" 동작이 보이거나 웹에서 익명으로 남아 있는 사용자의 세션을 추적할 수 없는 경우, 초기화 중에 `braze.openSession()`을 호출하는지 확인하세요.

- **시나리오:** 익명 사용자는 Braze ID를 반환할 수 있지만 세션 데이터는 비어 있거나 누락됩니다.
- **원인:** 구현에서 `braze.openSession()`을 호출하지 않습니다.
- **해결:** 항상 초기화 후 `braze.openSession()`을 호출하세요(외부 ID를 설정한 경우 `braze.changeUser()` 후에 호출).

자세한 내용은 [2단계: SDK 초기화]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web&tab=code-based%20integration#step-2-initialize-the-sdk)를 참조하세요.

{% alert important %}
모바일 또는 웹 기기의 익명 사용자도 [MAU]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data#monthly-active-users)에 포함될 수 있습니다. 따라서 조건부로 SDK를 로드하거나 초기화하여 이러한 사용자를 MAU 수에서 제외할 수 있습니다.
{% endalert %}
{% endtab %}

{% tab Google Tag Manager %}
{% multi_lang_include developer_guide/web/google_tag_manager/initialization_tag.md %}
{% endtab %}
{% endtabs %}

## 봇 트래픽 필터링 {#bot-filtering}

MAU에는 봇 사용자의 비율이 포함될 수 있으며, 이는 월간 활성 사용자 수를 부풀립니다. Braze 웹 SDK는 일부 일반 웹 크롤러(예: 검색 엔진 봇 및 소셜 미디어 미리보기 봇)에 대한 내장 감지를 포함하지만, SDK 업데이트만으로는 모든 새로운 봇을 일관되게 감지할 수 없으므로 강력한 솔루션으로 봇을 감지하는 데 적극적으로 대처하는 것이 특히 중요합니다.

### SDK 측 봇 감지의 한계 {#limitations-of-sdk-side-bot-detection}

웹 SDK는 알려진 크롤러를 필터링하는 기본 사용자 에이전트 기반 봇 감지를 포함합니다. 그러나 이 접근 방식에는 한계가 있습니다:

- **새로운 봇이 지속적으로 등장합니다**: AI 회사 및 기타 행위자들은 감지를 피하기 위해 자신을 위장할 수 있는 새로운 봇을 정기적으로 생성합니다.
- **사용자 에이전트 스푸핑**: 정교한 봇은 합법적인 브라우저 사용자 에이전트를 모방할 수 있습니다.
- **커스텀 봇**: 비기술적 사용자도 이제 대규모 언어 모델(LLM)을 사용하여 쉽게 봇을 생성할 수 있어 봇 행동이 예측 불가능해집니다.

### 봇 필터링 구현 {#implementing-bot-filtering}

{% alert important %}
아래에 설명된 솔루션은 일반적인 제안입니다. 봇 필터링 로직을 귀하의 고유한 환경 및 트래픽 패턴에 맞게 조정하세요.
{% endalert %}

가장 강력한 솔루션은 Braze SDK를 초기화하기 전에 자체 봇 필터링 로직을 구현하는 것입니다. 일반적인 접근 방식에는 다음이 포함됩니다:

#### 사용자 상호작용 요구 {#require-user-interaction}

사용자가 쿠키 동의 배너를 수락하거나 스크롤하거나 클릭하는 등의 의미 있는 상호작용을 수행할 때까지 SDK 초기화를 지연하는 것을 고려하세요. 이 접근 방식은 구현이 더 쉽고 봇 트래픽을 필터링하는 데 매우 효과적일 수 있습니다.

{% alert important %}
사용자 상호작용까지 SDK 초기화를 지연하면 배너와 Content Cards도 해당 상호작용이 발생할 때까지 표시되지 않을 수 있습니다.
{% endalert %}

#### 커스텀 봇 감지 {#custom-bot-detection}

특정 봇 트래픽 패턴에 기반한 커스텀 감지를 구현하세요. 예를 들어:

- 트래픽에서 식별한 패턴에 대한 사용자 에이전트 문자열 분석
- 헤드리스 브라우저 지표 확인
- 서드파티 봇 감지 서비스 사용
- 귀하의 사이트에 특정한 행동 신호 모니터링

**조건부 초기화 예시:**

```javascript
// Only initialize Braze if your custom bot detection determines this is not a bot
if (!isLikelyBot()) {
  braze.initialize('YOUR-API-KEY-HERE', {
    baseUrl: "YOUR-SDK-ENDPOINT-HERE"
  });
  braze.automaticallyShowInAppMessages();
  braze.openSession();
}
```

### 모범 사례 {#best-practices}

- MAU 데이터와 웹 트래픽 패턴을 정기적으로 분석하여 새로운 봇 행동을 식별하세요.
- 봇 필터링이 정상 사용자의 추적을 방해하지 않도록 철저히 테스트하세요.
- 환경에서 관찰한 봇 트래픽 패턴에 따라 필터링 로직을 업데이트하세요.

## 선택적 구성 {#optional-configurations}

### 로깅 {#logging}

로깅을 빠르게 활성화하려면 웹사이트 URL에 `?brazeLogging=true`를 매개변수로 추가하면 됩니다. 또는 [기본](#web_basic-logging) 또는 [커스텀](#web_custom-logging) 로깅을 활성화할 수 있습니다. 모든 플랫폼에 대한 중앙 집중식 개요는 [상세 로깅]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)을 참조하세요.

#### 기본 로깅 {#basic-logging}

{% tabs local %}
{% tab 초기화 전 %}
SDK가 초기화되기 전에 기본 디버깅 메시지를 JavaScript 콘솔에 기록하려면 `enableLogging`을 사용하세요.

```javascript
enableLogging: true
```

메서드는 다음과 유사해야 합니다:

```javascript
braze.initialize('API-KEY', {
    baseUrl: 'API-ENDPOINT',
    enableLogging: true
});
braze.openSession();
```
{% endtab %}

{% tab 초기화 후 %}
SDK가 초기화된 후 기본 디버깅 메시지를 JavaScript 콘솔에 기록하려면 `braze.toggleLogging()`을 사용하세요. 메서드는 다음과 유사해야 합니다:

```javascript
braze.initialize('API-KEY', {
    baseUrl: 'API-ENDPOINT',
});
braze.openSession();
...
braze.toggleLogging();
```
{% endtab %}
{% endtabs %}

{% alert important %}
기본 로그는 모든 사용자에게 표시되므로 코드를 프로덕션에 출시하기 전에 비활성화하거나 [`setLogger`](#web_custom-logging)로 전환하세요.
{% endalert %}

#### 커스텀 로깅 {#custom-logging}

JavaScript 콘솔에 커스텀 디버깅 메시지를 기록하려면 `setLogger`를 사용하세요. 기본 로그와 달리 이러한 로그는 사용자에게 표시되지 않습니다.

```javascript
setLogger(loggerFunction: (message: STRING) => void): void
```

`STRING`을 단일 문자열 매개변수로 메시지로 바꿉니다. 메서드는 다음과 유사해야 합니다:

```javascript
braze.initialize('API-KEY');
braze.setLogger(function(message) {
    console.log("Braze Custom Logger: " + message);
});
braze.openSession();
```

## SDK 업그레이드하기 {#upgrading-the-sdk}

{% multi_lang_include archive/web-v4-rename.md %}

콘텐츠 전송 네트워크에서 Braze 웹 SDK를 참조할 때, 예를 들어 `https://js.appboycdn.com/web-sdk/a.a/braze.min.js`(기본 통합 지침에서 권장하는 대로) 사용자는 사이트를 새로고침할 때 자동으로 소규모 업데이트(버그 수정 및 하위 호환 기능, 위의 예에서 `a.a.a`에서 `a.a.z` 버전)를 받습니다.

그러나 주요 변경 사항을 출시할 때는 통합에 영향을 미치지 않도록 Braze 웹 SDK를 수동으로 업그레이드해야 합니다. 또한 SDK를 다운로드하여 직접 호스팅하는 경우 자동으로 버전 업데이트를 받지 않으며 최신 기능과 버그 수정을 받으려면 수동으로 업그레이드해야 합니다.

RSS 리더 또는 원하는 서비스를 사용하여 [릴리스 피드를 따라](https://github.com/braze-inc/braze-web-sdk/tags.atom) 최신 릴리스를 확인할 수 있으며, 웹 SDK 릴리스 내역에 대한 전체 설명은 [체인지로그](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)를 참조하세요. Braze 웹 SDK를 업그레이드하려면:

- `https://js.appboycdn.com/web-sdk/[OLD VERSION NUMBER]/braze.min.js`의 버전 번호를 변경하거나 패키지 관리자의 종속성에서 Braze 라이브러리 버전을 업데이트합니다.
- 웹 푸시가 통합된 경우 사이트의 서비스 워커 파일을 업데이트합니다. 기본적으로 사이트의 루트 디렉토리 내 `/service-worker.js`에 있지만 일부 통합에서는 위치를 커스텀할 수 있습니다. 서비스 워커 파일을 호스팅하려면 루트 디렉토리에 액세스해야 합니다.

적절한 기능을 위해 이 두 파일을 서로 조정하여 업데이트해야 합니다.

## 기타 통합 방법 {#other-integration-methods}

### 가속 모바일 페이지(AMP) {#accelerated-mobile-pages-amp}
{% details 자세히 보기 %}
#### 1단계: AMP 웹 푸시 스크립트 포함 {#step-1-include-amp-web-push-script}

다음 비동기 스크립트 태그를 head에 추가하세요:

```js
<script async custom-element="amp-web-push" src="https://cdn.ampproject.org/v0/amp-web-push-0.1.js"></script>
```

#### 2단계: 구독 위젯 추가 {#step-2-add-subscription-widgets}

사용자가 푸시를 구독하고 탈퇴할 수 있도록 하는 위젯을 HTML 본문에 추가하세요.

```js
<!-- A subscription widget -->
<amp-web-push-widget visibility="unsubscribed" layout="fixed" width="250" height="80">
  <button on="tap:amp-web-push.subscribe">Subscribe to Notifications</button>
</amp-web-push-widget>

<!-- An unsubscription widget -->
<amp-web-push-widget visibility="subscribed" layout="fixed" width="250" height="80">
  <button on="tap:amp-web-push.unsubscribe">Unsubscribe from Notifications</button>
</amp-web-push-widget>
```

#### 3단계: `helper-iframe` 및 `permission-dialog` 추가 {#step-3-add-helper-iframe-and-permission-dialog}

AMP 웹 푸시 구성요소는 푸시 구독을 처리하기 위해 팝업을 생성하므로, 이 기능을 활성화하려면 다음 도우미 파일을 프로젝트에 추가해야 합니다:

- [`helper-iframe.html`](https://cdn.ampproject.org/v0/amp-web-push-helper-frame.html)
- [`permission-dialog.html`](https://cdn.ampproject.org/v0/amp-web-push-permission-dialog.html)

#### 4단계: 서비스 워커 파일 만들기 {#step-4-create-a-service-worker-file}

웹사이트의 루트 디렉토리에 `service-worker.js` 파일을 생성하고 다음 스니펫을 추가하세요:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### 5단계: AMP 웹 푸시 HTML 요소 구성 {#step-5-configure-the-amp-web-push-html-element}

다음 `amp-web-push` HTML 요소를 HTML 본문에 추가하세요. [`apiKey` 및 `baseUrl`](https://documenter.getpostman.com/view/4689407/SVYrsdsG)을 쿼리 매개변수로 `service-worker-URL`에 추가해야 한다는 점을 유의하세요.

```js
<amp-web-push
layout="nodisplay"
id="amp-web-push"
helper-iframe-url="FILE_PATH_TO_YOUR_HELPER_IFRAME"
permission-dialog-url="FILE_PATH_TO_YOUR_PERMISSION_DIALOG"
service-worker-url="FILE_PATH_TO_YOUR_SERVICE_WORKER?apiKey={YOUR_API_KEY}&baseUrl={YOUR_BASE_URL}"
>
```
{% enddetails %}

### 비동기 모듈 정의(AMD) {#asynchronous-module-definition-amd}

#### 지원 비활성화 {#disable-support}

사이트에서 RequireJS 또는 다른 AMD 모듈 로더를 사용하지만 이 목록의 다른 옵션 중 하나를 통해 Braze 웹 SDK를 로드하려는 경우, AMD 지원이 포함되지 않은 라이브러리 버전을 로드할 수 있습니다. 이 라이브러리 버전은 다음 CDN 위치에서 로드할 수 있습니다:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fno-amd-library.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### 모듈 로더 {#module-loader}

RequireJS 또는 기타 AMD 모듈 로더를 사용하는 경우 라이브러리 사본을 자체 호스팅하고 다른 리소스와 마찬가지로 참조하는 것이 좋습니다:

```javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  // Required if you want in-app messages to display automatically
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```

### Electron {#electron}

Electron은 웹 푸시 알림을 공식적으로 지원하지 않습니다(이 [GitHub 이슈](https://github.com/electron/electron/issues/6697) 참조). Braze에서 테스트하지 않은 다른 [오픈 소스 해결 방법](https://github.com/MatthieuLemoine/electron-push-receiver)을 시도해 볼 수 있습니다.

### Jest 프레임워크 {#jest}

Jest를 사용할 때 `SyntaxError: Unexpected token 'export'`와 유사한 오류가 표시될 수 있습니다. 이 문제를 해결하려면 Braze SDK를 무시하도록 `package.json`에서 구성을 조정합니다:

```
"jest": {
  "transformIgnorePatterns": [
    "/node_modules/(?!@braze)"
  ]
}
```

### SSR 프레임워크 {#ssr}

웹 SDK는 브라우저 환경에서 실행됩니다. SSR 프레임워크에서는 서버가 SDK 코드를 실행하지 않도록 클라이언트 전용 구성요소에서 Braze를 초기화하세요.

#### 프레임워크에 구애받지 않는 동적 가져오기 {#framework-agnostic-dynamic-import}

이 섹션에 프레임워크가 나열되지 않은 경우, 클라이언트 전용 라이프사이클 훅에서 Braze를 동적으로 가져올 수 있습니다.

```javascript
// MyComponent/braze-exports.js
// Export the parts of the SDK that you need.
export { initialize, openSession } from "@braze/web-sdk";

// MyComponent/MyComponent.js
useEffect(() => {
    import("./braze-exports.js").then(({ initialize, openSession }) => {
        initialize("YOUR-API-KEY-HERE", {
            baseUrl: "YOUR-SDK-ENDPOINT",
            enableLogging: true,
        });
        openSession();
    });
}, []);
```

webpack을 사용하는 경우, 특정 SDK 내보내기만 동적으로 가져올 수 있습니다.

```javascript
// MyComponent.js
useEffect(() => {
    import(
        /* webpackExports: ["initialize", "openSession"] */
        "@braze/web-sdk"
    ).then(({ initialize, openSession }) => {
        initialize("YOUR-API-KEY-HERE", {
            baseUrl: "YOUR-SDK-ENDPOINT",
            enableLogging: true,
        });
        openSession();
    });
}, []);
```

#### Next.js 및 Remix를 위한 공유 훅 {#shared-hook-for-nextjs-and-remix}

재사용 가능한 `useBraze` 훅을 생성하고 앱 루트 근처에서 호출하세요.

```tsx
// hooks/useBraze.ts
import { useEffect, useRef } from "react";

export function useBraze() {
  const didInit = useRef(false);

  useEffect(() => {
    if (didInit.current) {
      return;
    }
    didInit.current = true;

    import("@braze/web-sdk")
      .then((braze) => {
        const initialized = braze.initialize("YOUR-API-KEY-HERE", {
          // Use your Braze Web SDK endpoint, such as sdk.iad-01.braze.com.
          baseUrl: "YOUR-SDK-ENDPOINT",
          enableLogging: false,
        });
        if (!initialized) {
          return;
        }

        // Optional: Identify signed-in users before opening a session.
        // braze.changeUser("external-id");

        // Optional: Automatically display in-app messages.
        // braze.automaticallyShowInAppMessages();
        braze.openSession();
      })
      .catch((error) => {
        console.error("Unable to load Braze SDK:", error);
      });
  }, []);
}
```

#### Next.js(App Router) {#nextjs-app-router}

클라이언트 구성요소에서 `useBraze`를 호출하여 앱을 래핑하세요.

```tsx
// app/components/AppRoot.tsx
"use client";

import type { ReactNode } from "react";
import { useBraze } from "../hooks/useBraze";

export function AppRoot({ children }: { children: ReactNode }) {
  useBraze();
  return <>{children}</>;
}
```

```tsx
// app/layout.tsx
import type { ReactNode } from "react";
import { AppRoot } from "./components/AppRoot";

export default function RootLayout({
  children,
}: {
  children: ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <AppRoot>{children}</AppRoot>
      </body>
    </html>
  );
}
```

#### Next.js(Pages Router) {#nextjs-pages-router}

커스텀 앱 구성요소 상단에서 `useBraze`를 호출하세요.

```tsx
// pages/_app.tsx
import type { AppProps } from "next/app";
import { useBraze } from "../hooks/useBraze";

export default function App({ Component, pageProps }: AppProps) {
  useBraze();

  return (
    <Component {...pageProps} />
  );
}
```

#### Remix

루트 라우트 구성요소 상단에서 `useBraze`를 호출하세요.

로컬 Remix 유효성 검사 예시를 실행하려면 `PORT=4013 npm run dev`를 사용하세요.

```tsx
// app/root.tsx
import { Outlet } from "@remix-run/react";
import { useBraze } from "./hooks/useBraze";

export default function App() {
  useBraze();

  return <Outlet />;
}
```

#### 이벤트 로깅 및 사용자 업데이트 {#logging-events-and-updating-users}

`useBraze`가 앱 루트에서 SDK를 초기화한 후, 다른 클라이언트 구성요소에서 Braze 메서드를 호출할 수 있습니다. 일반적인 패턴은 `onClick`이나 `onSubmit`과 같은 사용자 액션 내에서 호출하는 것입니다. 이 예시에서는 SDK 메서드가 파일 상단이 아닌 클릭 핸들러 내에서 로드됩니다. 이렇게 하면 웹 SDK가 서버 코드에 포함되지 않고 해당 액션에 필요한 것만 로드됩니다. `webpackExports` 주석은 webpack에 포함할 메서드를 알려주므로 번들 크기가 작아집니다.

```tsx
// app/components/BuyButton.tsx
"use client";

export function BuyButton() {
  const handleClick = async () => {
    const { logCustomEvent, logPurchase, getUser } = await import(
      /* webpackExports: ["logCustomEvent", "logPurchase", "getUser"] */
      "@braze/web-sdk"
    );

    getUser()?.setCustomUserAttribute("last_purchase_date", "2026-05-04");
    logCustomEvent("clicked_buy", { source: "product_page" });
    logPurchase("sku_123", 19.99, "USD");
  };

  return <button onClick={handleClick}>Buy</button>;
}
```

이 예시는 누군가 **Buy**를 클릭할 때 활동을 기록하는 `BuyButton` 구성요소를 보여줍니다. 먼저 클릭 시점에 `logCustomEvent`, `logPurchase`, `getUser`만 가져옵니다. 그런 다음 사용자 속성을 업데이트하고, 커스텀 이벤트를 기록하고, 구매를 기록합니다. 이 패턴은 초기화를 `useBraze`에 중앙 집중화하면서도 모든 클라이언트 구성요소에서 의미 있는 액션을 추적할 수 있도록 합니다.

Vite와 함께 Remix를 사용하고 패키지 루트 가져오기가 런타임에 실패하는 경우, 기존 Vite 해결 방법을 사용하세요. 자세한 내용은 [Vite]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web#web_vite)를 참조하세요.

사용 가능한 메서드의 전체 목록은 [Braze JavaScript 참조 설명서](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)를 참조하세요.

### Tealium iQ

Tealium iQ는 기본적인 턴키 방식의 Braze 통합을 제공합니다. 통합을 구성하려면 Tealium 태그 관리 인터페이스에서 Braze를 검색하고 대시보드에서 웹 SDK API 키를 제공합니다.

자세한 내용이나 심층적인 Tealium 구성 지원이 필요하면 [통합 설명서]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium#about-tealium)를 확인하거나 Tealium 계정 매니저에게 문의하세요.

### Vite {#vite}

Vite를 사용할 때 순환 종속성 또는 `Uncaught TypeError: Class extends value undefined is not a constructor or null`에 대한 경고가 표시되는 경우 Braze SDK를 [종속성 검색](https://vitejs.dev/guide/dep-pre-bundling.html#customizing-the-behavior)에서 제외해야 할 수 있습니다:

```
optimizeDeps: {
    exclude: ['@braze/web-sdk']
},
```

### 기타 태그 관리자 {#other-tag-managers}

Braze는 커스텀 HTML 태그 내의 통합 지침에 따라 다른 태그 관리 솔루션과도 호환될 수 있습니다. 이러한 솔루션을 평가하는 데 도움이 필요하면 Braze 담당자에게 문의하세요.