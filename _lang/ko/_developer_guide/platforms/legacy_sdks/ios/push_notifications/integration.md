---
nav_title: 통합
article_title: iOS용 푸시 통합
platform: iOS
page_order: 0
description: "이 참조 문서에서는 iOS 애플리케이션에서 푸시 알림을 통합하는 방법에 대해 설명합니다."
channel:
  - push
search_rank: 5

local_redirect:
  ios-10-rich-notifications: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/'
local_redirect:
  creating-a-service-extension: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#creating-a-service-extension'
local_redirect:
  setting-up-the-service-extension: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#setting-up-the-service-extension'
local_redirect:
  creating-a-rich-notification-in-your-dashboard: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#creating-a-rich-notification-in-your-dashboard'
local_redirect:
  push-action-buttons-integration: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/'
local_redirect:
  step-1-adding-braze-default-push-categories: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/#step-1-adding-braze-default-push-categories'
local_redirect:
  step-2-enable-interactive-push-handling: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/#step-2-enable-interactive-push-handling'

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 푸시 통합 {#push-integration}

## 1단계: APN 토큰 업로드 {#step-1-upload-your-apns-token}

{% multi_lang_include developer_guide/swift/apns_token.md %}

## 2단계: 푸시 기능 활성화 {#step-2-enable-push-capabilities}

프로젝트 설정에서 **Capabilities** 탭 아래의 **Push Notifications** 기능이 토글되어 활성화되어 있는지 확인하세요.

![프로젝트 설정에서 Capabilities 탭 아래의 Push Notifications 기능이 토글되어 활성화되어 있는지 확인하세요.]({% image_buster /assets/img_archive/Enable_push_capabilities.png %})

개발용과 프로덕션용 푸시 인증서가 별도로 있는 경우, **General** 탭에서 **Automatically manage signing** 체크박스를 해제하세요. 이렇게 하면 각 빌드 구성에 대해 서로 다른 프로비저닝 프로필을 선택할 수 있습니다. Xcode의 자동 코드 서명 기능은 개발 서명만 처리하기 때문입니다.

![Xcode 프로젝트 설정의 General 탭을 보여주는 화면. 이 탭에서 Automatically manage signing 옵션이 해제되어 있습니다.]({% image_buster /assets/img_archive/xcode8_auto_signing.png %})

## 3단계: 푸시 알림 등록 {#step-3-register-for-push-notifications}

사용자의 기기가 APN에 등록되도록 하려면 앱의 `application:didFinishLaunchingWithOptions:` 델리게이트 메서드에 적절한 코드 샘플을 포함해야 합니다. 모든 푸시 통합 코드를 애플리케이션의 메인 스레드에서 호출해야 합니다.

Braze는 푸시 실행 버튼 지원을 위한 기본 푸시 카테고리도 제공하며, 이를 푸시 등록 코드에 수동으로 추가해야 합니다. 추가 통합 단계는 [푸시 실행 버튼]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/action_buttons)을 참조하세요.

{% alert warning %}
[푸시 모범 사례]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/troubleshooting)에 설명된 대로 커스텀 푸시 프롬프트를 구현한 경우, 사용자가 앱에 푸시 권한을 부여한 후 **앱이 실행될 때마다** 다음 코드를 호출해야 합니다. **[기기 토큰은 임의로 변경될 수 있으므로](https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/BackgroundExecution/BackgroundExecution.html) 앱은 APN에 다시 등록해야 합니다.**
{% endalert %}

### UserNotification 프레임워크 사용 (iOS 10+) {#using-usernotification-framework-ios-10}

iOS 10에서 도입된 `UserNotifications` 프레임워크(권장)를 사용하는 경우, 앱 델리게이트의 `application:didFinishLaunchingWithOptions:` 메서드에 다음 코드를 추가합니다.

{% alert important %}
다음 코드 샘플에는 임시 푸시 인증에 대한 통합이 포함되어 있습니다(5행 및 6행). 앱에서 임시 인증을 사용할 계획이 없다면 `requestAuthorization` 옵션에 `UNAuthorizationOptionProvisional`을 추가하는 코드 행을 제거할 수 있습니다.<br>푸시 임시 인증에 대해 자세히 알아보려면 [iOS 알림 옵션]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options)을 방문하세요.
{% endalert %}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
if (floor(NSFoundationVersionNumber) > NSFoundationVersionNumber_iOS_9_x_Max) {
  UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
  center.delegate = self;
  UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
  if (@available(iOS 12.0, *)) {
  options = options | UNAuthorizationOptionProvisional;
  }
  [center requestAuthorizationWithOptions:options
                        completionHandler:^(BOOL granted, NSError * _Nullable error) {
                          [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];
  [[UIApplication sharedApplication] registerForRemoteNotifications];
} else {
  UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:nil];
  [[UIApplication sharedApplication] registerForRemoteNotifications];
  [[UIApplication sharedApplication] registerUserNotificationSettings:settings];
}
```

{% endtab %}
{% tab swift %}

```swift
if #available(iOS 10, *) {
  let center = UNUserNotificationCenter.current()
  center.delegate = self as? UNUserNotificationCenterDelegate
  var options: UNAuthorizationOptions = [.alert, .sound, .badge]
  if #available(iOS 12.0, *) {
    options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
  }
  center.requestAuthorization(options: options) { (granted, error) in
    Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
  }
  UIApplication.shared.registerForRemoteNotifications()
} else {
  let types : UIUserNotificationType = [.alert, .badge, .sound]
  let setting : UIUserNotificationSettings = UIUserNotificationSettings(types:types, categories:nil)
  UIApplication.shared.registerUserNotificationSettings(setting)
  UIApplication.shared.registerForRemoteNotifications()
}
```

{% endtab %}
{% endtabs %}


{% alert warning %}
앱이 실행을 완료하기 전에, 가급적 `application:didFinishLaunchingWithOptions:`에서 `center.delegate = self`를 사용하여 델리게이트 객체를 동기적으로 할당해야 합니다. 그렇지 않으면 앱이 수신되는 푸시 알림을 놓칠 수 있습니다. 자세한 내용은 Apple의 [`UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate) 설명서를 참조하세요.
{% endalert %}

### UserNotifications 프레임워크 미사용 {#without-usernotifications-framework}

`UserNotifications` 프레임워크를 사용하지 않는 경우, 앱 델리게이트의 `application:didFinishLaunchingWithOptions:` 메서드에 다음 코드를 추가합니다:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:nil];
[[UIApplication sharedApplication] registerForRemoteNotifications];
[[UIApplication sharedApplication] registerUserNotificationSettings:settings];
```

{% endtab %}
{% tab swift %}

```swift
let types : UIUserNotificationType = UIUserNotificationType.Badge | UIUserNotificationType.Sound | UIUserNotificationType.Alert
var setting : UIUserNotificationSettings = UIUserNotificationSettings(forTypes: types, categories: nil)
UIApplication.shared.registerUserNotificationSettings(setting)
UIApplication.shared.registerForRemoteNotifications()
```

{% endtab %}
{% endtabs %}

## 4단계: Braze에 푸시 토큰 등록 {#step-4-register-push-tokens-with-braze}

APN 등록이 완료되면 다음 메서드를 수정하여 결과 `deviceToken`을 Braze에 전달해야 사용자가 푸시 알림을 받을 수 있습니다.

{% tabs %}
{% tab OBJECTIVE-C %}

`application:didRegisterForRemoteNotificationsWithDeviceToken:` 메서드에 다음 코드를 추가합니다:

```objc
[[Appboy sharedInstance] registerDeviceToken:deviceToken];
```

{% endtab %}
{% tab swift %}

앱의 `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)` 메서드에 다음 코드를 추가합니다:

```swift
Appboy.sharedInstance()?.registerDeviceToken(deviceToken)
```

{% endtab %}
{% endtabs %}

{% alert important %}
`application:didRegisterForRemoteNotificationsWithDeviceToken:` 델리게이트 메서드는 `[[UIApplication sharedApplication] registerForRemoteNotifications]`가 호출된 후 매번 호출됩니다. 다른 푸시 서비스에서 Braze로 마이그레이션하는 경우 사용자의 기기가 이미 APN에 등록되어 있다면, 이 메서드는 다음 호출 시 기존 등록에서 토큰을 수집하므로 사용자가 푸시를 다시 옵트인할 필요가 없습니다.
{% endalert %}

## 5단계: 푸시 처리 활성화 {#step-5-enable-push-handling}

다음 코드는 수신된 푸시 알림을 Braze에 전달하며, 푸시 분석 로깅 및 링크 처리에 필요합니다. 모든 푸시 통합 코드를 애플리케이션의 메인 스레드에서 호출해야 합니다.

### iOS 10+

iOS 10 이상을 대상으로 빌드할 때는 `UserNotifications` 프레임워크를 통합하고 다음을 수행하는 것을 권장합니다.

{% tabs %}
{% tab OBJECTIVE-C %}

애플리케이션의 `application:didReceiveRemoteNotification:fetchCompletionHandler:` 메서드에 다음 코드를 추가합니다.

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo
                      fetchCompletionHandler:completionHandler];
```

다음으로, 앱의 `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` 메서드에 다음 코드를 추가합니다.

```objc
[[Appboy sharedInstance] userNotificationCenter:center
                 didReceiveNotificationResponse:response
                          withCompletionHandler:completionHandler];
```

**포그라운드 푸시 처리**

앱이 포그라운드에 있을 때 푸시 알림을 표시하려면 `userNotificationCenter:willPresentNotification:withCompletionHandler:`를 구현합니다.

```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
       willPresentNotification:(UNNotification *)notification
         withCompletionHandler:(void (^)(UNNotificationPresentationOptions options))completionHandler {
  if (@available(iOS 14.0, *)) {
    completionHandler(UNNotificationPresentationOptionList | UNNotificationPresentationOptionBanner);
  } else {
    completionHandler(UNNotificationPresentationOptionAlert);
  }
}
```

포그라운드 알림을 클릭하면 iOS 10 푸시 델리게이트 `userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:`가 호출되고, Braze는 푸시 클릭 이벤트를 기록합니다.

{% endtab %}
{% tab swift %}

앱의 `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` 메서드에 다음 코드를 추가합니다.

```swift
Appboy.sharedInstance()?.register(application,
                                            didReceiveRemoteNotification: userInfo,
                                            fetchCompletionHandler: completionHandler)
```

다음으로, 앱의 `userNotificationCenter(_:didReceive:withCompletionHandler:)` 메서드에 다음 코드를 추가합니다.

```swift
Appboy.sharedInstance()?.userNotificationCenter(center,
                                               didReceive: response,
                                               withCompletionHandler: completionHandler)
```

**포그라운드 푸시 처리**

앱이 포그라운드에 있을 때 푸시 알림을 표시하려면 `userNotificationCenter(_:willPresent:withCompletionHandler:)`를 구현합니다.

```swift
func userNotificationCenter(_ center: UNUserNotificationCenter,
                              willPresent notification: UNNotification,
                              withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {
  if #available(iOS 14.0, *) {
    completionHandler([.list, .banner]);
  } else {
    completionHandler([.alert]);
  }
}
```

포그라운드 알림을 클릭하면 iOS 10 푸시 델리게이트 `userNotificationCenter(_:didReceive:withCompletionHandler:)`가 호출되고, Braze는 푸시 클릭 이벤트를 기록합니다.

{% endtab %}
{% endtabs %}

### iOS 10 이전 {#pre-ios-10}

iOS 10에서는 푸시를 클릭했을 때 더 이상 `application:didReceiveRemoteNotification:fetchCompletionHandler:`를 호출하지 않도록 동작이 변경되었습니다. 이러한 이유로, iOS 10 이상으로 빌드를 업데이트하고 `UserNotifications` 프레임워크를 사용하지 않는 경우, 이전 통합 방식과는 다르게 이전 스타일의 두 델리게이트 모두에서 Braze를 호출해야 합니다.

SDK < iOS 10을 대상으로 빌드하는 앱의 경우 다음 지침을 따르세요.

{% tabs %}
{% tab OBJECTIVE-C %}

푸시 알림에서 열람 추적을 활성화하려면 앱의 `application:didReceiveRemoteNotification:fetchCompletionHandler:` 메서드에 다음 코드를 추가합니다.

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo
                      fetchCompletionHandler:completionHandler];
```

iOS 10에서 푸시 분석을 지원하려면 앱의 `application:didReceiveRemoteNotification:` 델리게이트 메서드에도 다음 코드를 추가해야 합니다.

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo];
```

{% endtab %}
{% tab swift %}

푸시 알림에서 열람 추적을 활성화하려면 앱의 `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` 메서드에 다음 코드를 추가합니다.

```swift
Appboy.sharedInstance()?.register(application,
  didReceiveRemoteNotification: userInfo,
  fetchCompletionHandler: completionHandler)
```

iOS 10에서 푸시 분석을 지원하려면 앱의 `application(_:didReceiveRemoteNotification:)` 델리게이트 메서드에도 다음 코드를 추가해야 합니다.

```swift
Appboy.sharedInstance()?.register(application,
  didReceiveRemoteNotification: userInfo)
```

{% endtab %}
{% endtabs %}

## 6단계: 딥링킹 {#step-6-deep-linking}

푸시에서 앱으로의 딥링킹은 표준 푸시 통합 설명서를 통해 자동으로 처리됩니다. 앱의 특정 위치에 딥링크를 추가하는 방법에 대해 자세히 알아보려면 [고급 사용 사례]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/advanced_use_cases/linking#linking-handling-customization)를 참조하세요.

## 7단계: 단위 테스트(선택 사항) {#step-7-unit-tests-optional}

방금 수행한 통합 단계에 대한 테스트 커버리지를 추가하려면 [푸시 단위 테스트]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/unit_tests)를 구현합니다.