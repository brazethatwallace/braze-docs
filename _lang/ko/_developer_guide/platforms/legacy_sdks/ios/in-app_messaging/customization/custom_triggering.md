---
nav_title: 커스텀 트리거링
article_title: iOS용 인앱 메시지 트리거 커스터마이즈
platform: iOS
page_order: 7
description: "이 참조 문서에서는 iOS 애플리케이션의 커스텀 인앱 메시지 트리거에 대해 설명합니다."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 커스텀 인앱 메시지 트리거 {#custom-in-app-message-triggering}

기본적으로 인앱 메시지는 SDK에서 기록한 이벤트 유형에 의해 트리거됩니다. 서버에서 전송한 이벤트로 인앱 메시지를 트리거하려는 경우에도 이를 구현할 수 있습니다.

이 기능을 활성화하려면 기기에 무음 푸시를 전송하여 기기가 SDK 기반 이벤트를 기록할 수 있도록 합니다. 이 SDK 이벤트는 이후 사용자에게 표시되는 인앱 메시지를 트리거합니다.

## 1단계: 무음 푸시 및 키-값 페어 처리 {#step-1-handle-silent-push-and-key-value-pairs}

`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` 메서드에 다음 코드를 추가합니다:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [[Appboy sharedInstance] logCustomEvent:@"IAM Trigger" withProperties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
 };
```

{% endtab %}
{% tab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  NSLog("A push was received");
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    Appboy.sharedInstance()?.logCustomEvent("IAM Trigger", withProperties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endtab %}
{% endtabs %}

무음 푸시가 수신되면 SDK에서 기록한 이벤트 "인앱 메시지 트리거"가 고객 프로필에 기록됩니다. 이 인앱 메시지는 애플리케이션이 포그라운드에 있는 동안 무음 푸시가 수신된 경우에만 트리거됩니다.

## 2단계: 푸시 Campaign 생성 {#step-2-create-a-push-campaign}

서버 전송 이벤트를 통해 트리거되는 무음 푸시 Campaign을 생성합니다. 무음 푸시 Campaign 생성에 대한 자세한 내용은 [무음 푸시 알림]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/silent_push_notifications)을 참조하세요.

![커스텀 이벤트 "server_event"를 수행하는 사용자에게 전달되는 실행 기반 전달 인앱 메시지 Campaign.]({% image_buster /assets/img_archive/iosServerSentPush.png %})

푸시 Campaign에는 이 푸시 Campaign이 SDK 커스텀 이벤트를 기록하기 위해 전송되었음을 나타내는 키-값 페어 추가 항목이 포함되어야 합니다. 이 이벤트는 인앱 메시지를 트리거하는 데 사용됩니다:

![두 개의 키-값 페어가 있는 실행 기반 전달 인앱 메시지 Campaign. "CAMPAIGN_NAME"은 "인앱 메시지 이름 예시"로 설정되고, "IS_SERVER_EVENT"는 "true"로 설정됩니다.]({% image_buster /assets/img_archive/iOSServerPush.png %})

`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` 메서드 내의 코드는 `IS_SERVER_EVENT` 키를 확인하고, 이 키가 존재하면 SDK 커스텀 이벤트를 기록합니다.

푸시 페이로드의 키-값 페어 추가 항목 내에서 원하는 값을 전송하여 이벤트 이름이나 이벤트 속성정보를 변경할 수 있습니다. 커스텀 이벤트를 기록할 때 이러한 추가 항목은 이벤트 이름의 매개변수 또는 이벤트 속성정보로 사용할 수 있습니다.

## 3단계: 인앱 메시지 Campaign 생성 {#step-3-create-an-in-app-message-campaign}

Braze 대시보드에서 사용자에게 표시되는 인앱 메시지 Campaign을 생성합니다. 이 Campaign은 실행 기반 전달이어야 하며, `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` 메서드 내에서 기록된 커스텀 이벤트에 의해 트리거되어야 합니다.

다음 예제에서는 초기 무음 푸시의 일부로 이벤트 속성정보를 전송하여 트리거할 특정 인앱 메시지를 구성했습니다.

![커스텀 이벤트 "인앱 메시지 트리거"를 수행하는 사용자에게 전달되는 실행 기반 전달 인앱 메시지 Campaign. "campaign_name"이 "인앱 메시지 이름 예시"와 같습니다.]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

푸시 메시지가 SDK에서 기록한 커스텀 이벤트를 기록하는 데 사용되므로, Braze는 이 솔루션을 활성화하기 위해 각 사용자의 푸시 토큰을 저장해야 합니다. iOS와 Android 모두에서 Braze는 사용자에게 OS의 푸시 프롬프트가 제공된 시점부터 토큰을 저장합니다. 그 이전에는 푸시를 사용하여 사용자에게 도달할 수 없으며, 위의 솔루션도 사용할 수 없습니다.