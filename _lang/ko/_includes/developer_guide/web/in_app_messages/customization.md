{% multi_lang_include developer_guide/prerequisites/web.md %}

## 커스텀 스타일 {#custom-styles}

Braze UI 요소는 자연스러운 인앱 메시지 경험을 조성하는 기본 모양과 느낌을 사용하며, 다른 Braze 모바일 플랫폼과의 일관성을 목표로 합니다. Braze 기본 스타일은 Braze SDK 내 CSS에 정의되어 있습니다.

### 기본 스타일 설정하기 {#setting-a-default-style}

애플리케이션에서 선택한 스타일을 재정의하여 자체 배경 이미지, 글꼴 패밀리, 스타일, 크기, 애니메이션 등으로 표준 인앱 메시지 유형을 사용자 지정할 수 있습니다.

예를 들어, 다음은 인앱 메시지의 헤더가 이탤릭체로 표시되도록 하는 오버라이드 예제입니다:

```css
  body .ab-in-app-message .ab-message-header {
    font-style: italic;
  }
```

자세한 내용은 [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html)를 참조하세요.

### z-index 사용자 지정하기 {#customizing-the-z-index}

기본적으로 인앱 메시지는 `z-index: 9001`을 사용하여 표시됩니다. 웹사이트가 이보다 높은 값으로 요소를 스타일링하는 경우 `inAppMessageZIndex ` [초기화 옵션](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions)을 사용하여 구성할 수 있습니다.

```javascript
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    inAppMessageZIndex: 12000
});
```

{% alert important %}
이 기능은 Web Braze SDK v3.3.0 이상에서만 사용할 수 있습니다.
{% endalert %}

## 메시지 해제 사용자 지정하기 {#customizing-message-dismissals}

기본적으로 인앱 메시지가 표시되는 동안 ESC 키를 누르거나 페이지의 회색 배경을 클릭하면 메시지가 해제됩니다. `requireExplicitInAppMessageDismissal` [초기화 옵션](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions)을 `true`로 설정하면 이 동작을 방지하고, 메시지를 해제하려면 명시적으로 버튼을 클릭해야 합니다.

```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    requireExplicitInAppMessageDismissal: true
});
```

## 표시 타이밍 사용자 지정하기 {#customizing-display-timing}

기본 표시 타이밍을 재정의하려면 `braze.automaticallyShowInAppMessages()` 호출을 제거하고 `braze.subscribeToInAppMessage()`에서 메시지를 처리하세요. `braze.openSession()` 전에 콜백을 등록하면 세션 시작 메시지를 가로채서 각 메시지를 표시할지 또는 지연할지 결정할 수 있습니다.

기본적으로 Braze는 인앱 메시지가 트리거되고 표시 자격이 있을 때 표시합니다. 앱 경험에 다른 동작이 필요한 경우 커스텀 콜백을 사용하여 자체 로직에 따라 메시지를 지연하거나 표시할 수 있습니다.

다음 예제는 트리거된 인앱 메시지를 구독하고, 선택한 메시지를 지연하고, 지연된 메시지를 나중에 표시하는 방법을 보여줍니다:

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT"
});

braze.subscribeToInAppMessage(function (message) {
    // Control-group messages should always be "shown" to log analytics.
    if (message.isControl || message instanceof braze.ControlMessage) {
        braze.showInAppMessage(message);
        return;
    }

    const shouldDefer = true; // Replace with your own display logic

    if (shouldDefer) {
        braze.deferInAppMessage(message);
        return;
    }

    braze.showInAppMessage(message);
});

braze.openSession();

// Later, when your app is ready to display a deferred message:
const deferredMessage = braze.getDeferredInAppMessage();
if (deferredMessage) {
    braze.showInAppMessage(deferredMessage);
}
```

관련 전달 사용자 지정 가이드는 다음을 참조하세요:

- [Web `deferInAppMessage` 참조](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#deferinappmessage)
- [Web `subscribeToInAppMessage` 참조](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage)

## 새 탭에서 링크 열기 {#opening-links-in-a-new-tab}

인앱 메시지 링크를 새 탭에서 열도록 설정하려면 `openInAppMessagesInNewTab` 옵션을 `true`로 설정하여 인앱 메시지 클릭 시 모든 링크가 새 탭 또는 새 창에서 열리도록 합니다.

```javascript
braze.initialize('api-key', { openInAppMessagesInNewTab: true} );
```
