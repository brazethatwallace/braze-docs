## Braze Vega SDK 정보 {#about-the-braze-vega-sdk}

Braze Vega SDK를 사용하면 분석 데이터를 수집하고 사용자에게 풍부한 인앱 메시지를 표시할 수 있습니다. Braze Vega SDK의 대부분의 메서드는 비동기적이며, await하거나 resolve해야 하는 프로미스를 반환합니다.

## Braze Vega SDK 통합하기 {#integrating-the-braze-vega-sdk}

### 1단계: Braze 라이브러리 설치 {#step-1-install-the-braze-library}

선호하는 패키지 매니저를 사용하여 Braze Vega SDK를 설치합니다.

{% tabs local %}
{% tab npm %}
프로젝트에서 NPM을 사용하는 경우, Braze Vega SDK를 종속성으로 추가할 수 있습니다.

```bash
npm install @braze/vega-sdk --save
```

설치 후 필요한 메서드를 가져올 수 있습니다:

```javascript
import { initialize, changeUser, openSession } from "@braze/vega-sdk";
```
{% endtab %}

{% tab yarn %}
프로젝트에서 Yarn을 사용하는 경우, Braze Vega SDK를 종속성으로 추가할 수 있습니다.

```bash
yarn add @braze/vega-sdk
```

설치 후 필요한 메서드를 가져올 수 있습니다:

```javascript
import { initialize, changeUser, openSession } from "@braze/vega-sdk";
```
{% endtab %}
{% endtabs %}

### 2단계: SDK 초기화 {#step-2-initialize-the-sdk}

Braze Vega SDK가 프로젝트에 추가되면, Braze 대시보드의 **설정** > **앱 설정**에서 확인할 수 있는 API 키와 [SDK 엔드포인트 URL]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)을 사용하여 라이브러리를 초기화합니다.

{% alert important %}
다른 Braze 메서드를 호출하기 전에 `changeUser` 프로미스를 await하거나 resolve해야 합니다. 그렇지 않으면 이벤트와 속성이 잘못된 사용자에게 설정될 수 있습니다.
{% endalert %}

```javascript
import { useEffect } from "react-native";
import {
  initialize,
  changeUser,
  logCustomEvent,
  openSession,
  setCustomUserAttribute,
  setUserCountry
} from "@braze/vega-sdk";

const App = () => {
  useEffect(() => {
    const initBraze = async () => {
      // Initialize the SDK
      await initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
        sessionTimeoutInSeconds: 60,
        appVersionNumber: "1.2.3.4",
        enableLogging: true, // set to `true` for debugging
      });

      // Change user
      await changeUser("user-id-123");

      // Start a session
      await openSession();

      // Log custom events and set user attributes
      logCustomEvent("visited-page", { pageName: "home" });
      setCustomUserAttribute("my-attribute", "my-attribute-value");
      setUserCountry("USA");
    };

    initBraze();
  }, []);

  return (
    // Your app components
  );
};
```

{% alert important %}
익명 사용자도 [MAU]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data#monthly-active-users)에 포함될 수 있습니다. 따라서 이러한 사용자를 MAU 집계에서 제외하려면 SDK를 조건부로 로드하거나 초기화하는 것이 좋습니다.
{% endalert %}

## 선택적 구성 {#optional-configurations}

### 로깅 {#logging}

디버깅 및 문제 해결에 도움이 되도록 SDK 로깅을 활성화할 수 있습니다. 로깅을 활성화하는 방법은 여러 가지가 있습니다.

#### 초기화 시 로깅 활성화 {#enable-logging-during-initialization}

`initialize()`에 `enableLogging: true`를 전달하면 콘솔에 디버깅 메시지가 기록됩니다:

```javascript
initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
  enableLogging: true
});
```

{% alert important %}
기본 로그는 모든 사용자에게 표시되므로, 코드를 프로덕션에 배포하기 전에 로깅을 비활성화하는 것을 권장합니다.
{% endalert %}

#### 초기화 후 로깅 활성화 {#enable-logging-after-initialization}

`toggleLogging()`을 사용하여 초기화 후에 SDK 로깅을 활성화하거나 비활성화할 수 있습니다:

```javascript
import { toggleLogging } from "@braze/vega-sdk";

// Enable logging
toggleLogging();
```

#### 커스텀 로깅 {#custom-logging}

`setLogger()`를 사용하여 SDK 로그 처리 방식을 보다 세밀하게 제어할 수 있는 커스텀 로거 함수를 제공할 수 있습니다:

```javascript
import { setLogger } from "@braze/vega-sdk";

setLogger((message) => {
  console.log("Braze Custom Logger: " + message);
  // Add your custom logging logic here
});
```

### 구성 옵션 {#configuration-options}

`initialize()`에 추가 구성 옵션을 전달하여 SDK 동작을 커스터마이즈할 수 있습니다:

```javascript
await initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
  sessionTimeoutInSeconds: 60,        // Configure session timeout (default is 1800 seconds)
  appVersionNumber: "1.2.3.4",        // Set your app version
  enableLogging: true,                 // Enable SDK logging
});
```

## SDK 업그레이드 {#upgrading-the-sdk}

NPM 또는 Yarn에서 Braze Vega SDK를 참조하는 경우, 패키지 종속성을 업데이트하여 최신 버전으로 업그레이드할 수 있습니다:

```bash
npm update @braze/vega-sdk
# or, using yarn:
yarn upgrade @braze/vega-sdk
```

## 통합 테스트하기 {#testing-your-integration}

SDK 통합이 올바르게 작동하는지 확인하려면 다음을 수행하세요:

1. `enableLogging: true`로 SDK를 초기화하여 콘솔에서 디버그 메시지를 확인합니다.
2. 다른 SDK 메서드를 호출하기 전에 `await changeUser()`를 호출해야 합니다.
3. `await openSession()`을 호출하여 세션을 시작합니다.
4. Braze 대시보드의 **개요**에서 세션 데이터가 기록되고 있는지 확인합니다.
5. 커스텀 이벤트를 로깅한 후 대시보드에 표시되는지 테스트합니다.