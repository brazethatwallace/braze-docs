## 데이터 추적 비활성화하기 {#disabling-data-tracking}

{% multi_lang_include archive/web-v4-rename.md %}

{% tabs %}
{% tab 표준 구현 %}
웹 SDK에서 데이터 추적 활동을 비활성화하려면 [`disableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) 메서드를 사용하세요. 이 메서드는 `disableSDK()`가 호출되기 전에 기록된 모든 데이터를 동기화하며, 이후 이 페이지 및 향후 페이지 로드에서 Braze 웹 SDK에 대한 모든 후속 호출이 무시됩니다.
{% endtab %}

{% tab Google Tag 매니저 %}
웹 추적을 비활성화하거나 다시 활성화하려면 **추적 비활성화** 또는 **추적 재개** 태그 유형을 사용하세요. 이 두 옵션은 각각 [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk)와 [`enableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk)를 호출합니다.
{% endtab %}
{% endtabs %}

### 모범 사례 {#best-practices}

사용자에게 추적을 중지할 수 있는 옵션을 제공하려면, 두 개의 링크 또는 버튼이 있는 간단한 페이지를 구축하는 것이 좋습니다. 하나는 클릭 시 `disableSDK()`를 호출하고, 다른 하나는 `enableSDK()`를 호출하여 사용자가 다시 옵트인할 수 있도록 합니다. 이러한 컨트롤을 사용하여 다른 데이터 하위 프로세서를 통한 추적도 시작하거나 중지할 수 있습니다.

{% alert note %}
Braze SDK는 `disableSDK()`를 호출하기 위해 초기화할 필요가 없으므로, 완전한 익명 사용자에 대해서도 추적을 비활성화할 수 있습니다. 반대로, `enableSDK()`는 Braze SDK를 초기화하지 않으므로 추적을 활성화하려면 이후에 `initialize()`도 호출해야 합니다.
{% endalert %}

## 데이터 추적 재개하기 {#resuming-data-tracking}

데이터 수집을 재개하려면 [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) 메서드를 사용하세요.

## 로그아웃 및 푸시 등록 해제 {#logout-and-unregister-push}

Braze SDK는 사용자가 푸시 알림 등록을 해제하거나 로그아웃할 때 기기를 타겟팅 대상에서 제거하는 메서드를 제공합니다. 이 메서드는 Braze 서버와 SDK에서 현재 사용자의 푸시 등록 데이터를 제거하므로, Braze는 해당 사용자에게 더 이상 푸시 알림 Campaign을 전송하지 않습니다.

### 로그아웃 {#logout}

사용자가 애플리케이션에서 로그아웃할 때 SDK의 `logout` 메서드를 호출하여 현재 사용자로부터 기기의 푸시 등록을 제거하고 SDK에서 자동으로 정리 작업을 수행합니다. `logout` 메서드는 다음 작업을 수행합니다:

- Braze 서버에서 현재 사용자의 기기 푸시 토큰 등록을 해제합니다.
- 등록 해제 호출이 성공하면 SDK가 로컬에 저장된 SDK 데이터를 삭제하고 SDK를 비활성화합니다.
- 실패 시 `errorCallback`을 호출하여 통합자가 조치를 취할 수 있도록 합니다.

다음 예제는 콜백 기반 `logout` 처리를 보여줍니다. 즉각적인 성공 및 오류 처리가 필요할 때 사용하며, 로깅 부분을 앱 흐름에 맞게 교체하세요.

```javascript
import { logout } from "@braze/web-sdk";

const successCallback = () => {
  console.log('Successfully logged out');
};

const errorCallback = () => {
  console.log('Failed to log out');
};

logout(successCallback, errorCallback);
```

#### `logout` 후 추적 및 푸시 다시 활성화하기 {#re-enable-tracking-and-push-after-logout}

`logout`이 성공한 후 [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk)를 호출한 다음, [웹 푸시 설정]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)을 따라 운영 체제(OS) 또는 푸시 공급자에 알림을 다시 등록하세요.

#### 즉시 등록 해제 호출 방지 {#avoid-immediate-unregister-calls}

OS 또는 푸시 공급자에 푸시 알림을 등록한 직후에 `logout` 또는 `unregisterPush`를 호출하지 마세요. 비동기 서버 처리로 인해 드물게 푸시 토큰이 Braze 사용자에게 다시 추가될 수 있습니다.

### 푸시 등록 해제 {#unregister-push}

추가적인 자동 정리 없이 기기에 대한 푸시 전송을 중지하려면 `unregisterPush` 메서드를 사용하세요. 이 메서드는 Braze 서버에서 현재 사용자의 기기 푸시 토큰을 제거하고 로컬에 저장된 토큰을 삭제합니다.

다음 예제는 콜백 기반 `unregisterPush` 처리를 보여줍니다. 즉각적인 성공 및 오류 처리가 필요할 때 사용하며, 로깅 부분을 앱 흐름에 맞게 교체하세요.

```javascript
import { unregisterPush } from "@braze/web-sdk";

const successCallback = () => {
  console.log('Successfully unregistered from push');
};

const errorCallback = () => {
  console.log('Failed to unregister from push');
};

unregisterPush(successCallback, errorCallback);
```

#### `unregisterPush` 후 푸시 다시 등록하기 {#re-register-push-after-unregisterpush}

`unregisterPush`를 호출한 후, Braze 푸시 알림을 다시 전송하기 전에 [웹 푸시 설정]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)을 따라 OS 또는 푸시 공급자에 알림을 다시 등록하세요.

{% alert note %}
지원되는 브라우저에서 활성 푸시 구독이 존재하는 경우, `unregisterPush`는 브라우저 Push API에서 구독을 해제한 후 Braze가 관리하는 서비스 워커도 등록 해제합니다. `manageServiceWorkerExternally`를 `true`로 설정하면 SDK가 서비스 워커를 등록 해제하지 않습니다.
{% endalert %}

#### 즉시 등록 해제 호출 방지

OS 또는 푸시 공급자에 푸시 알림을 등록한 직후에 `logout` 또는 `unregisterPush`를 호출하지 마세요. 비동기 서버 처리로 인해 드물게 푸시 토큰이 Braze 사용자에게 다시 추가될 수 있습니다.