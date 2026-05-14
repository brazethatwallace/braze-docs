{% multi_lang_include developer_guide/prerequisites/web.md %}

## 메시지 트리거 {#message-triggers}

## 트리거 유형 {#trigger-types}

SDK가 다음 커스텀 이벤트 유형 중 하나를 기록하면 인앱 메시지가 자동으로 트리거됩니다: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, `Push Click`. `Specific Purchase` 및 `Custom Event` 트리거에는 강력한 등록정보 필터도 포함되어 있습니다.

{% alert note %}
인앱 메시지는 API 또는 API 이벤트를 통해 트리거할 수 없으며&#8212;SDK에서 기록한 커스텀 이벤트만 트리거할 수 있습니다. 로깅에 대해 자세히 알아보려면 [커스텀 이벤트 로깅]({{site.baseurl}}/developer_guide/analytics/logging_events/)을 참조하세요.
{% endalert %}

### 전달 의미 체계 {#delivery-semantics}

모든 적격 인앱 메시지는 세션 시작 시 사용자의 기기로 전달됩니다. 전달 시 SDK는 자산을 미리 가져와 트리거 시점에 바로 사용할 수 있도록 하여 표시 지연을 최소화합니다. 트리거 이벤트에 적격 인앱 메시지가 두 개 이상 있는 경우 우선순위가 가장 높은 메시지만 전달됩니다.

SDK의 세션 시작 의미 체계에 대한 자세한 내용은 [세션 수명 주기]({{site.baseurl}}/developer_guide/platform_integration_guides/analytics/tracking_sessions/)를 참조하세요.

### 사용량 제한 {#rate-limits}

기본적으로 SDK는 트리거된 인앱 메시지를 30초에 한 번으로 제한합니다.

프로덕션 앱에서는 사용자가 연속적인 인앱 메시지에 압도되지 않도록 이 값을 10초 미만으로 설정하지 마세요. 테스트 및 샘플 앱 플로우에서는 5초가 일반적인 설정입니다.

테스트를 위해 이 간격을 `0`으로 설정할 수 있습니다. 그러나 `0`초 간격이 여러 인앱 메시지를 동시에 표시하도록 강제하지는 않습니다. 다른 모달 또는 전체 인앱 메시지가 이미 표시되고 있는 경우 `braze.showInAppMessage`는 `false`를 반환하고 새 메시지는 표시되지 않습니다.

이를 재정의하려면 Braze 인스턴스가 초기화되기 전에 Braze 구성에 다음 등록정보를 추가하세요. 음이 아닌 정수 값으로 설정할 수 있으며, 이는 초 단위의 최소 시간 간격을 나타냅니다. 예를 들어:

```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```

## 키-값 페어 {#key-value-pairs}

Braze에서 Campaign을 생성할 때 인앱 메시징 오브젝트가 앱에 데이터를 전송하는 데 사용할 수 있는 `extras`로 키-값 페어를 설정할 수 있습니다. 예를 들어:

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  if (inAppMessage instanceof braze.ControlMessage) {
    return braze.showInAppMessage(inAppMessage);
  }


  if (inAppMessage instanceof braze.InAppMessage) {
    const extras = inAppMessage.extras;
    if (extras) {
      for (const key in extras) {
        console.log("key: " + key + ", value: " + extras[key]);
      }
    }
  }
  braze.showInAppMessage(inAppMessage);
});
```

## 자동 트리거 비활성화 {#disabling-automatic-triggers}

인앱 메시지가 자동으로 트리거되는 것을 방지하려면:

로딩 스니펫 내에서 `braze.automaticallyShowInAppMessages()` 호출을 제거한 다음, 인앱 메시지 표시 여부를 처리하는 커스텀 로직을 생성하세요.

```javascript
braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message

  if (inAppMessage.isControl) { // v4.5.0+, otherwise use  `inAppMessage instanceof braze.ControlMessage`
     return braze.showInAppMessage(inAppMessage);
  }

  // Display the in-app message. You could defer display here by pushing this message to code within your own application.
  // If you don't want to use the Braze built-in display capabilities, you could alternatively pass the in-app message to your own display code here.

  if ( should_show_the_message_according_to_your_custom_logic ) {
      braze.showInAppMessage(inAppMessage);
  } else {
      // do nothing
  }
});
```

{% alert important %}
웹사이트에서 `braze.automaticallyShowInAppMessages()`를 제거하지 않은 상태에서 `braze.showInAppMessage`를 호출하면 메시지가 여러 번 표시될 수 있습니다.
{% endalert %}

`inAppMessage` 매개변수는 [`braze.InAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) 서브클래스 또는 [`braze.ControlMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.controlmessage.html) 오브젝트이며, 각각 다양한 생애주기 이벤트 구독 메서드를 포함합니다. 전체 설명서는 [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html)를 참조하세요.

한 번에 하나의 [`Modal`]({{site.baseurl}}/developer_guide/in_app_messages/?tab=modal&sdktab=web) 또는 [`Full`]({{site.baseurl}}/developer_guide/in_app_messages/?tab=full&sdktab=web) 인앱 메시지만 표시할 수 있습니다. 이미 하나가 표시되고 있는 동안 두 번째 모달 또는 전체 메시지를 표시하려고 하면 `braze.showInAppMessage`가 false를 반환하고 두 번째 메시지는 표시되지 않습니다.

## 수동으로 메시지 트리거하기 {#manually-triggering-messages}

### 실시간 메시지 표시 {#displaying-a-message-in-real-time}

인앱 메시지는 사이트 내에서 생성하여 실시간으로 로컬에 표시할 수도 있습니다. 대시보드에서 사용할 수 있는 모든 커스터마이징 옵션을 로컬에서도 사용할 수 있습니다. 이는 앱 내에서 실시간으로 트리거하려는 메시지를 표시할 때 특히 유용합니다. 그러나 로컬에서 생성된 메시지에 대한 분석은 Braze 대시보드에서 확인할 수 없습니다.

```javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```

## 이탈 의도 메시지 트리거 {#triggering-exit-intent-messages}

이탈 의도 메시지는 방문자가 사이트를 떠나기 전에 중요한 정보를 전달하기 위해 사용되는 비침해적 인앱 메시지입니다.

이러한 메시지 유형에 대한 트리거를 설정하려면 웹사이트에 이탈 의도 라이브러리(예: [ouibounce의 오픈소스 라이브러리](https://github.com/carlsednaoui/ouibounce))를 구현한 다음, 아래 코드를 사용하여 Braze에 `'exit intent'`를 커스텀 이벤트로 기록하세요. 이제 향후 인앱 메시지 Campaign에서 이 메시지 유형을 커스텀 이벤트 트리거로 사용할 수 있습니다.

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```
