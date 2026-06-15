{% multi_lang_include developer_guide/prerequisites/swift.md %}

## 메시지 트리거 {#message-triggers}

### 트리거 유형 {#trigger-types}

SDK가 다음 커스텀 이벤트 유형 중 하나를 기록하면 인앱 메시지가 자동으로 트리거됩니다: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, `Push Click`. `Specific Purchase` 및 `Custom Event` 트리거에는 강력한 속성 필터도 포함되어 있습니다.

{% alert note %}
인앱 메시지는 API 또는 API 이벤트를 통해 트리거할 수 없으며&#8212;SDK에서 기록한 커스텀 이벤트만 트리거할 수 있습니다. 로깅에 대해 자세히 알아보려면 [커스텀 이벤트 로깅]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift)을 참조하세요.
{% endalert %}

### 전달 의미 체계 {#delivery-semantics}

모든 적격 인앱 메시지는 세션 시작 시 사용자의 기기로 전달됩니다. 전달 시 SDK는 자산을 미리 가져와 트리거 시점에 바로 사용할 수 있도록 하여 표시 지연을 최소화합니다. 트리거 이벤트에 적격 인앱 메시지가 두 개 이상 있는 경우 우선순위가 가장 높은 메시지만 전달됩니다.

SDK의 세션 시작 의미 체계에 대한 자세한 내용은 [세션 수명 주기]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift)를 참조하세요.

### 기본 사용량 제한 {#default-rate-limit}

기본적으로 SDK는 트리거된 인앱 메시지를 30초에 한 번으로 제한합니다.

프로덕션 앱에서는 사용자가 연속적인 인앱 메시지에 압도되지 않도록 이 값을 10초 미만으로 설정하지 마세요. 테스트 및 샘플 앱 플로우에서는 5초가 일반적인 설정입니다.

테스트를 위해 이 간격을 `0`으로 설정할 수 있습니다. 그러나 `0`초 간격이 여러 인앱 메시지를 동시에 표시하도록 강제하지는 않습니다. 하나의 메시지가 표시 중이면 다른 트리거된 메시지는 메시지가 표시될 수 있을 때까지 인앱 메시지 스택에서 대기합니다.

이를 재정의하려면 Braze 인스턴스가 초기화되기 전에 Braze 구성의 `triggerMinimumTimeInterval` 속성을 업데이트하세요. 음이 아닌 정수로 설정할 수 있으며, 초 단위의 최소 시간 간격을 나타냅니다. 예를 들어:

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
  endpoint: "YOUR-BRAZE-ENDPOINT"
)
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                    endpoint:@"<BRAZE_ENDPOINT>"];
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5;
Braze *braze = [BrazePlugin initBraze:configuration];
AppDelegate.braze = braze;
```
{% endtab %}
{% endtabs %}

## 키-값 페어 {#key-value-pairs}

Braze에서 Campaign을 생성할 때 키-값 페어를 `extras`로 설정할 수 있으며, 인앱 메시징 오브젝트가 이를 사용하여 앱으로 데이터를 전송할 수 있습니다. 예를 들어:

{% tabs %}
{% tab swift %}

```swift
let customization = message.extras["custom-display"] as? String
if customization == "colorful-slideup" {
  // Perform your custom logic.
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
if ([message.extras[@"custom-display"] isKindOfClass:[NSString class]]) {
  NSString *customization = message.extras[@"custom-display"];
  if ([customization isEqualToString:@"colorful-slideup"]) {
    // Perform your custom logic.
  }
}
```

{% endtab %}
{% endtabs %}

전체 구현에 대해서는 [예제 앱](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples)의 인앱 메시지 커스터마이징 샘플을 참조할 수 있습니다.

## 자동 트리거 비활성화 {#disabling-automatic-triggers}

인앱 메시지가 자동으로 트리거되는 것을 방지하려면:

1. [여기 iOS 문서](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui)에서 설명한 대로 `BrazeInAppMessageUIDelegate` 델리게이트를 구현합니다.
2. `inAppMessage(_:displayChoiceForMessage:)` 델리게이트 메서드가 `.discard`를 반환하도록 업데이트합니다.

## 수동으로 메시지 트리거하기 {#manually-triggering-messages}

### 서버 측 이벤트 사용 {#using-a-server-side-event}

서버 측 이벤트를 사용하여 인앱 메시지를 트리거하려면 기기에 무음 푸시를 보내 기기가 SDK 기반 이벤트를 기록할 수 있도록 합니다. 이 SDK 이벤트는 이후에 사용자에게 표시되는 인앱 메시지를 트리거할 수 있습니다.

#### 1단계: 무음 푸시 및 키-값 페어 처리 {#step-1-handle-silent-push-and-key-value-pairs}

다음 함수를 구현하고 [`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` 메서드](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application/) 내에서 호출하세요:

{% tabs %}
{% tab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  print("A push was received")
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    AppDelegate.braze?.logCustomEvent("IAM Trigger", properties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [AppDelegate.braze logCustomEvent:@"IAM Trigger" properties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
};
```

{% endtab %}
{% endtabs %}

무음 푸시가 수신되면 SDK에서 기록한 이벤트 "인앱 메시지 트리거"가 고객 프로필에 기록됩니다.

{% alert important %}
푸시 메시지가 SDK에서 기록한 커스텀 이벤트를 기록하는 데 사용되므로, Braze는 이 솔루션을 활성화하기 위해 각 사용자의 푸시 토큰을 저장해야 합니다. iOS 사용자의 경우, Braze는 사용자가 OS의 푸시 프롬프트를 받은 시점부터만 토큰을 저장합니다. 그 이전에는 푸시를 사용하여 사용자에게 도달할 수 없으며, 위의 솔루션은 사용할 수 없습니다.
{% endalert %}

#### 2단계: 무음 푸시 Campaign 생성 {#step-2-create-a-silent-push-campaign}

서버 전송 이벤트를 통해 트리거되는 [무음 푸시 Campaign]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift)을 생성합니다.

![고객 프로필에 커스텀 이벤트 "server_event"가 있는 사용자에게 전달될 실행 기반 전달 인앱 메시지 Campaign.]({% image_buster /assets/img_archive/iosServerSentPush.png %})

푸시 Campaign에는 이 푸시 Campaign이 SDK 커스텀 이벤트를 기록하기 위해 전송되었음을 나타내는 키-값 페어 extras가 포함되어야 합니다. 이 이벤트는 인앱 메시지를 트리거하는 데 사용됩니다.

![두 개의 키-값 페어를 가진 실행 기반 전달 인앱 메시지 Campaign. "CAMPAIGN_NAME"은 "인앱 메시지 이름 예시"로 설정되고, "IS_SERVER_EVENT"는 "true"로 설정됩니다.]({% image_buster /assets/img_archive/iOSServerPush.png %})

`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` 메서드 내의 코드는 `IS_SERVER_EVENT` 키를 확인하고, 이 키가 존재하면 SDK 커스텀 이벤트를 기록합니다.

푸시 페이로드의 키-값 페어 extras 내에서 원하는 값을 전송하여 이벤트 이름이나 이벤트 속성정보를 변경할 수 있습니다. 커스텀 이벤트를 로깅할 때 이러한 extras는 이벤트 이름의 매개변수 또는 이벤트 속성정보로 사용할 수 있습니다.

#### 3단계: 인앱 메시지 Campaign 생성 {#step-3-create-an-in-app-message-campaign}

Braze 대시보드에서 사용자에게 표시되는 인앱 메시지 Campaign을 생성하세요. 이 Campaign은 실행 기반 전달이어야 하며 `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` 메서드 내에서 기록된 커스텀 이벤트에 의해 트리거되어야 합니다.

다음 예제에서는 초기 무음 푸시의 일부로 이벤트 속성정보를 전송하여 트리거할 특정 인앱 메시지를 구성합니다.

![사용자가 "인앱 메시지 트리거"라는 커스텀 이벤트를 수행하고 "campaign_name"이 "IAM Campaign 이름 예시"와 일치할 때 전달되는 실행 기반 전달 인앱 메시지 Campaign.]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

{% alert note %}
이 인앱 메시지는 애플리케이션이 포그라운드에 있을 때 무음 푸시를 수신해야만 트리거됩니다.
{% endalert %}

### 사전 정의된 메시지 표시 {#displaying-a-pre-defined}

사전 정의된 인앱 메시지를 수동으로 표시하려면 다음 메서드를 사용하세요:

```swift
if let inAppMessage = AppDelegate.braze?.inAppMessagePresenter?.nextAvailableMessage() {
  AppDelegate.braze?.inAppMessagePresenter?.present(message: inAppMessage)
}
```

### 실시간 메시지 표시 {#displaying-a-message-in-real-time}

`inAppMessagePresenter`에서 [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:)) 메서드를 수동으로 호출하여 로컬 인앱 메시지를 실시간으로 표시할 수도 있습니다. 예를 들어:

{% tabs %}
{% tab swift %}

```swift
let customInAppMessage = Braze.InAppMessage.slideup(
  .init(message: "YOUR_CUSTOM_SLIDEUP_MESSAGE", slideFrom: .bottom, themes: .defaults)
)
AppDelegate.braze?.inAppMessagePresenter?.present(message: customInAppMessage)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZInAppMessageRaw *customInAppMessage = [[BRZInAppMessageRaw alloc] init];
customInAppMessage.type = BRZInAppMessageRawTypeSlideup;
customInAppMessage.message = @"YOUR_CUSTOM_SLIDEUP_MESSAGE";
customInAppMessage.slideFrom = BRZInAppMessageRawSlideFromBottom;
customInAppMessage.themes = @{
  @"light": BRZInAppMessageRawTheme.defaultLight,
  @"dark": BRZInAppMessageRawTheme.defaultDark
};
[AppDelegate.braze.inAppMessagePresenter presentMessage:customInAppMessage];
```

{% endtab %}
{% endtabs %}

{% alert note %}
인앱 메시지를 직접 생성하면 모든 분석 추적이 옵트아웃되며, `message.context`를 사용하여 클릭 및 노출 횟수 로깅을 수동으로 처리해야 합니다.
{% endalert %}

## 인앱 메시지 스택 {#the-in-app-message-stack}

### 스택에 인앱 메시지 추가 {#adding-in-app-messages-to-the-stack}

사용자는 다음 상황에서 인앱 메시지를 받을 자격이 있습니다:

- 인앱 메시지 트리거 이벤트가 발생합니다
- 세션이 시작됩니다
- 푸시 알림에서 앱이 열립니다

인앱 메시지의 트리거 이벤트가 발생하면 "스택"에 배치됩니다. 여러 인앱 메시지가 스택에 있고 표시 대기 중인 경우, Braze는 가장 최근에 수신한 인앱 메시지를 먼저 표시합니다(후입선출).

사용자가 인앱 메시지를 받을 자격이 있으면 `BrazeInAppMessagePresenter`가 인앱 메시지 스택에서 최신 인앱 메시지를 요청합니다. 스택은 메모리에 저장된 인앱 메시지만 유지하며, 일시 중단 모드에서 앱이 실행될 때마다 초기화됩니다.

### 스택으로 인앱 메시지 반환 {#returning-in-app-messages-to-the-stack}

트리거된 인앱 메시지는 다음 상황에서 스택으로 반환될 수 있습니다:

- 앱이 백그라운드에 있을 때 인앱 메시지가 트리거됩니다.
- 다른 인앱 메시지가 현재 표시 중입니다.
- `inAppMessage(_:displayChoiceForMessage:)` [델리게이트 메서드](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb)가 `.reenqueue`를 반환했습니다.

트리거된 인앱 메시지는 사용자가 인앱 메시지를 받을 자격이 있을 때 나중에 표시할 수 있도록 스택 맨 위에 배치됩니다.

### 인앱 메시지 삭제 {#discarding-in-app-messages}

트리거된 인앱 메시지는 다음 상황에서 삭제됩니다:

- `inAppMessage(_:displayChoiceForMessage:)` [델리게이트 메서드](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb)가 `.discard`를 반환했습니다.
- 인앱 메시지의 자산(이미지 또는 ZIP 파일)을 다운로드하지 못했습니다.
- 인앱 메시지가 표시할 준비가 되었지만 시간 초과 기간이 지났습니다.
- 기기 방향이 트리거된 인앱 메시지의 방향과 일치하지 않습니다.

인앱 메시지는 스택에서 제거됩니다. 삭제된 후에도 인앱 메시지는 트리거 이벤트의 다른 인스턴스에 의해 나중에 다시 트리거될 수 있습니다.