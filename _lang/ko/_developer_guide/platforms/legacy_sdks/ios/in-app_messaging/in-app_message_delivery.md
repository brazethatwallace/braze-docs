---
nav_title: 인앱 메시지 전달
article_title: iOS용 인앱 메시지 전달
platform: iOS
page_order: 3
description: "이 참조 문서에서는 iOS 인앱 메시지 전달을 다루며, 다양한 트리거 유형, 전달 의미 체계 및 이벤트 트리거 단계를 설명합니다."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 인앱 메시지 전달 {#in-app-message-delivery}

## 트리거 유형 {#trigger-types}

인앱 메시지 제품을 사용하면 여러 가지 이벤트 유형의 결과로 인앱 메시지 표시를 트리거할 수 있습니다: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, `Push Click`. 또한 `Specific Purchase`와 `Custom Event` 트리거에는 강력한 속성정보 필터가 포함되어 있습니다.

{% alert note %}
트리거된 인앱 메시지는 Braze SDK를 통해 기록된 커스텀 이벤트에서만 작동합니다. 인앱 메시지는 API 또는 API 이벤트(예: 구매 이벤트)를 통해 트리거할 수 없습니다. iOS를 사용하는 경우, [커스텀 이벤트 추적]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=swift) 문서를 방문하여 자세히 알아보세요.
{% endalert %}

## 전달 방식 {#delivery-semantics}

사용자가 수신 자격이 있는 모든 인앱 메시지는 세션 시작 시 사용자의 기기로 전달됩니다. 하나의 이벤트로 두 개의 인앱 메시지가 트리거되는 경우, 우선순위가 더 높은 인앱 메시지가 표시됩니다. SDK의 세션 시작 방식에 대한 자세한 내용은 [세션 라이프사이클]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/analytics/tracking_sessions#session-lifecycle)을 참고하세요. 전달 시 SDK는 트리거 시점에 즉시 사용할 수 있도록 에셋을 미리 가져와 표시 지연을 최소화합니다.

트리거 이벤트에 수신 자격이 있는 인앱 메시지가 여러 개 연결되어 있는 경우, 우선순위가 가장 높은 인앱 메시지만 전달됩니다.

전달 즉시 표시되는 인앱 메시지(세션 시작, 푸시 클릭)의 경우 에셋이 미리 가져오기되지 않아 약간의 지연이 발생할 수 있습니다.

## 트리거 간 최소 시간 간격 {#minimum-time-interval-between-triggers}

기본적으로, 양질의 사용자 경험을 위해 인앱 메시지는 30초에 한 번으로 사용량 제한이 적용됩니다.

`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`에 전달되는 `appboyOptions` 파라미터 안의 `ABKMinimumTriggerTimeIntervalKey`를 통해 이 값을 재정의할 수 있습니다. `ABKMinimumTriggerTimeIntervalKey`를 인앱 메시지 간 최소 시간(초)으로 원하는 정수 값으로 설정하세요:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Sets the minimum trigger time interval to 5 seconds
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKMinimumTriggerTimeIntervalKey : @(5) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:[ABKMinimumTriggerTimeIntervalKey : 5])
```

{% endtab %}
{% endtabs %}

## 일치하는 트리거를 찾지 못하는 경우 {#failing-to-find-a-matching-trigger}

Braze가 특정 이벤트에 대해 일치하는 트리거를 찾지 못하면, [`ABKInAppMessageControllerDelegate`](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_in_app_message_controller_delegate-p.html)의 [noMatchingTriggerForEvent:name:](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_in_app_message_controller_delegate-p.html#ab4d57b13c51545d487227945a37d4ab8) 메서드를 호출합니다. 이 시나리오를 처리하려면 델리게이트 프로토콜을 채택하는 클래스에서 이 메서드를 구현하세요.

## 로컬 인앱 메시지 전달 {#local-in-app-message-delivery}

### 인앱 메시지 스택 {#the-in-app-message-stack}

#### 인앱 메시지 표시 {#showing-in-app-messages}

사용자가 인앱 메시지를 수신할 자격이 있으면, `ABKInAppMessageController`가 인앱 메시지 스택에서 가장 최근의 인앱 메시지를 제공합니다. 스택은 메모리에 저장된 인앱 메시지만 유지하며, 앱이 일시 중지 모드에서 다시 실행될 때 초기화됩니다.

{% alert important %}
키보드가 화면에 표시되어 있을 때는 인앱 메시지를 표시하지 마세요. 이 상황에서는 렌더링 동작이 정의되지 않습니다.
{% endalert %}

#### 스택에 인앱 메시지 추가 {#adding-in-app-messages-to-the-stack}

사용자는 다음과 같은 상황에서 인앱 메시지를 수신할 자격이 있습니다:

- 인앱 메시지 트리거 이벤트가 발생한 경우
- 세션 시작 이벤트
- 푸시 알림을 통해 앱이 열린 경우

트리거된 인앱 메시지는 트리거 이벤트가 발생할 때 스택에 추가됩니다. 스택에 여러 인앱 메시지가 대기 중인 경우, Braze는 가장 최근에 수신된 인앱 메시지를 먼저 표시합니다(후입선출).

#### 스택으로 인앱 메시지 반환 {#returning-in-app-messages-to-the-stack}

트리거된 인앱 메시지는 다음과 같은 상황에서 스택으로 반환될 수 있습니다:

- 앱이 백그라운드에 있을 때 인앱 메시지가 트리거된 경우
- 다른 인앱 메시지가 현재 표시 중인 경우
- 지원이 중단된 `beforeInAppMessageDisplayed:withKeyboardIsUp:` [UI 델리게이트 메서드]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates#in-app-message-delegate)가 구현되지 않았고, 키보드가 현재 표시 중인 경우
- `beforeInAppMessageDisplayed:` [델리게이트 메서드]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates#core-in-app-message-delegate) 또는 지원이 중단된 `beforeInAppMessageDisplayed:withKeyboardIsUp:` [UI 델리게이트 메서드]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates#in-app-message-delegate)가 `ABKDisplayInAppMessageLater`를 반환한 경우

#### 인앱 메시지 폐기 {#discarding-in-app-messages}

트리거된 인앱 메시지는 다음과 같은 상황에서 폐기됩니다:

- `beforeInAppMessageDisplayed:` [델리게이트 메서드]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates#core-in-app-message-delegate) 또는 지원이 중단된 `beforeInAppMessageDisplayed:withKeyboardIsUp:` [UI 델리게이트 메서드]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates#in-app-message-delegate)가 `ABKDiscardInAppMessage`를 반환한 경우
- 인앱 메시지의 에셋(이미지 또는 ZIP 파일) 다운로드에 실패한 경우
- 인앱 메시지가 표시 준비가 되었지만 제한 시간이 초과된 경우
- 기기 방향이 트리거된 인앱 메시지의 방향과 일치하지 않는 경우
- 인앱 메시지가 전체 화면 인앱 메시지이지만 이미지가 없는 경우
- 인앱 메시지가 이미지 전용 Modal 인앱 메시지이지만 이미지가 없는 경우

#### 인앱 메시지 표시를 수동으로 대기줄에 추가 {#manually-queue-in-app-message-display}

앱 내 다른 시점에서 인앱 메시지를 표시하고 싶다면, 다음 메서드를 호출하여 스택의 최상위 인앱 메시지를 수동으로 표시할 수 있습니다:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].inAppMessageController displayNextInAppMessage];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()!.inAppMessageController.displayNextInAppMessage()
```

{% endtab %}
{% endtabs %}

### 실시간 인앱 메시지 생성 및 표시 {#real-time-in-app-message-creation-and-display}

인앱 메시지는 앱 내에서 로컬로 생성하여 Braze를 통해 표시할 수도 있습니다. 이 기능은 앱 내에서 실시간으로 트리거하고 싶은 메시지를 표시할 때 특히 유용합니다. Braze는 로컬에서 생성된 인앱 메시지에 대한 분석을 지원하지 않습니다.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
  ABKInAppMessageSlideup *customInAppMessage = [[ABKInAppMessageSlideup alloc] init];
  customInAppMessage.message = @"YOUR_CUSTOM_SLIDEUP_MESSAGE";
  customInAppMessage.duration = 2.5;
  customInAppMessage.extras = @{@"key" : @"value"};
  [[Appboy sharedInstance].inAppMessageController addInAppMessage:customInAppMessage];
```

{% endtab %}
{% tab swift %}

```swift
  let customInAppMessage = ABKInAppMessageSlideup.init()
  customInAppMessage.message = "YOUR_CUSTOM_SLIDEUP_MESSAGE"
  customInAppMessage.duration = 2.5
  customInAppMessage.extras = ["key": "value"]
  Appboy.sharedInstance()!.inAppMessageController.add(customInAppMessage)
```

{% endtab %}
{% endtabs %}