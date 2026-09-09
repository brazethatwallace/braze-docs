---
nav_title: SDK 통합 가이드 (선택 사항)
article_title: iOS용 Braze SDK 통합 가이드(선택 사항)
alias: "/ios_sdk/"
description: "이 iOS 통합 가이드는 iOS SDK와 핵심 구성요소를 애플리케이션에 처음 통합할 때 설정 모범 사례를 단계별로 안내합니다. 이 가이드는 BrazeManager.swift 헬퍼 파일을 빌드하는 데 도움이 됩니다."
page_order: 10
platform: iOS

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Braze iOS SDK 통합 가이드 {#braze-ios-sdk-integration-guide}

> 이 iOS 통합 가이드(선택 사항)는 iOS SDK와 핵심 구성요소를 애플리케이션에 처음 통합할 때 설정 모범 사례를 단계별로 안내합니다. 이 가이드는 나머지 프로덕션 코드에서 Braze iOS SDK에 대한 모든 종속성을 분리하는 `BrazeManager.swift` 헬퍼 파일을 빌드하여 전체 애플리케이션에서 하나의 `import AppboyUI`만 사용하도록 합니다. 이 접근 방식은 과도한 SDK 가져오기로 인해 발생하는 문제를 제한하여 코드를 쉽게 추적, 디버그 및 변경할 수 있도록 합니다.

{% alert important %}
이 가이드에서는 이미 Xcode 프로젝트에 [SDK를 추가]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview)했다고 가정합니다.
{% endalert %}

## 통합 개요 {#integration-overview}

다음 단계는 프로덕션 코드에서 호출할 `BrazeManager` 헬퍼 파일을 빌드하는 방법을 안내합니다. 이 헬퍼 파일은 아래 나열된 다양한 통합 주제에 대한 여러 확장(extension)을 추가하여 모든 Braze 관련 의존성을 처리합니다. 각 주제에는 Swift와 Objective-C 코드 스니펫이 포함된 수평 탭 단계가 제공됩니다. 애플리케이션에서 해당 채널을 사용할 계획이 없다면, Content Cards 및 인앱 메시지 단계는 통합에 필수가 아닙니다.

- [BrazeManager.swift 생성](#create-brazemanagerswift)
- [SDK 초기화](#initialize-the-sdk)
- [푸시 알림](#push-notifications)
- [사용자 변수 및 메서드 접근](#access-user-variables-and-methods)
- [분석 로깅](#log-analytics)
- [인앱 메시지 (선택 사항)](#in-app-messages)
- [Content Cards (선택 사항)](#content-cards)
- [다음 단계](#next-steps)

### BrazeManager.swift 생성 {#create-brazemanagerswift}

{% tabs local %}
{% tab Create BrazeManager swift %}

#### BrazeManager.swift 생성
`BrazeManager.swift` 파일을 구성하려면, 프로젝트의 원하는 위치에 _BrazeManager_라는 이름의 새 Swift 파일을 생성합니다. 다음으로, `import Foundation`을 SPM의 경우 `import AppboyUI`로(CocoaPods의 경우 `import Appboy_iOS_SDK`) 교체한 후, 모든 Braze 관련 메서드와 변수를 호스팅할 `BrazeManager` 클래스를 생성합니다. `Appboy_iOS_SDK`

{% alert note %}
- `BrazeManager`는 구조체가 아닌 `NSObject` 클래스로, `ABKInAppMessageUIDelegate`와 같은 ABK 델리게이트를 준수할 수 있습니다.
- `BrazeManager`는 설계상 싱글턴 클래스이므로, 이 클래스의 인스턴스는 하나만 사용됩니다. 이를 통해 객체에 대한 통합 접근 지점을 제공합니다.
{% endalert %}

1. _shared_라는 정적 변수를 추가하여 `BrazeManager` 클래스를 초기화합니다. 이 변수는 한 번만 지연 초기화됩니다.
2. 다음으로, _apiKey_라는 프라이빗 상수 변수를 추가하고, Braze 대시보드의 워크스페이스에서 가져온 API 키 값을 설정합니다.
3. _appboyOptions_라는 프라이빗 계산 프로퍼티를 추가합니다. 이 변수는 SDK의 구성 값을 저장하며, 현재는 비어 있습니다.

{% subtabs global %}
{% subtab Swift %}

```swift
class BrazeManager: NSObject {
  // 1
  static let shared = BrazeManager()

  // 2
  private let apikey = "YOUR-API-KEY"

  // 3
  private var appboyOptions: [String:Any] {
    return [:]
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
@implementation BrazeManager

// 1
+ (instancetype)shared {
    static BrazeManager *shared = nil;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        shared = [[BrazeManager alloc] init];
        // Do any other initialisation stuff here
    });
    return shared;
}

// 2
- (NSString *)apiKey {
  return @"YOUR-API-KEY";
}

// 3
- (NSDictionary *)appboyOptions {
  return [NSDictionary dictionary];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### SDK 초기화 {#initialize-the-sdk}

{% tabs local %}
{% tab Step 1: Initialize SDK from BrazeManager swift %}

#### BrazeManager.swift에서 SDK 초기화 {#initialize-sdk-from-brazemanagerswift}
다음으로 SDK를 초기화해야 합니다. 이 가이드에서는 이미 Xcode 프로젝트에 [SDK를 추가]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview)했다고 가정합니다. 또한 `Info.plist` 파일이나 `appboyOptions`에 [워크스페이스 SDK 엔드포인트]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/completing_integration#step-2-specify-your-data-cluster)와 [`LogLevel`]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations#braze-log-level)이 설정되어 있어야 합니다.

`BrazeManager.swift` 파일에 `AppDelegate.swift` 파일의 `didFinishLaunchingWithOptions` 메서드를 반환 타입 없이 추가합니다. `BrazeManager.swift` 파일에 유사한 메서드를 생성하면 `AppDelegate.swift` 파일에 `import AppboyUI` 구문이 필요하지 않습니다.

다음으로, 새로 선언한 `apiKey`와 `appboyOptions` 변수를 사용하여 SDK를 초기화합니다.

{% alert important %}
초기화는 메인 스레드에서 수행해야 합니다.
{% endalert %}

{% subtabs global %}
{% subtab Swift %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) {
  Appboy.start(withApiKey: apikey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [Appboy startWithApiKey:[self apiKey] inApplication:application withLaunchOptions:launchOptions withAppboyOptions:[self appboyOptions]];
}
```
{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% tab Step 2: Handle Appboy Initialization %}

##### AppDelegate.swift에서 Appboy 초기화 처리 {#handle-appboy-initialization-in-the-appdelegateswift}
다음으로, `AppDelegate.swift` 파일로 돌아가서 AppDelegate의 `didFinishLaunchingWithOptions` 메서드에 다음 코드 스니펫을 추가하여 `BrazeManager.swift` 헬퍼 파일에서 Appboy 초기화를 처리합니다. `AppDelegate.swift`에 `import AppboyUI` 구문을 추가할 필요가 없습니다.

{% subtabs global %}
{% subtab Swift %}

```swift
func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
) -> Bool {
  // Override point for customization after application launch

  BrazeManager.shared.application(application, didFinishLaunchingWithOptions: launchOptions)

  return true
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Override point for customization after application launch

  [[BrazeManager shared] application:application didFinishLaunchingWithOptions:launchOptions];

  return YES;
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
코드를 컴파일하고 애플리케이션을 실행하세요.<br><br>이 시점에서 SDK가 작동해야 합니다. 대시보드에서 세션이 기록되고 있는지 확인한 후 다음 단계로 진행하세요.
{% endalert %}

### 푸시 알림 {#push-notifications}

{% tabs local %}
{% tab Step 1: Add Push Certificate %}

#### 푸시 인증서 추가 {#add-push-certificate}

Braze 대시보드에서 기존 워크스페이스로 이동합니다. **Push Notification Settings**에서 푸시 인증서 파일을 Braze 대시보드에 업로드하고 저장합니다.

![APN 키 업로드 필드가 있는 Braze 대시보드 Push Notification Settings.]({% image_buster /assets/img/ios_sdk/ios_sdk2.png %}){: style="max-width:60%;"}

{% endtab %}
{% tab Step 2: Register for Notifications %}

{% alert important %}
이 단계 끝에 있는 전용 체크포인트를 놓치지 마세요!
{% endalert %}

##### 푸시 알림 등록 {#register-for-push-notifications}

다음으로, 푸시 알림을 등록합니다. 이 가이드에서는 Apple 개발자 포털과 Xcode 프로젝트에서 [푸시 자격 증명을 올바르게 설정]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration)했다고 가정합니다.

푸시 알림 등록 코드는 `BrazeManager.swift` 파일의 `didFinishLaunching...` 메서드에 추가됩니다. 초기화 코드는 다음과 같이 구성됩니다:

1. 사용자와 상호작용하기 위한 인증 요청 콘텐츠를 구성합니다. 이 옵션들은 예시로 나열되어 있습니다.
2. 사용자에게 푸시 알림을 보낼 수 있는 인증을 요청합니다. 푸시 알림에 대한 사용자의 허용 또는 거부 응답은 `granted` 변수에 추적됩니다.
3. 사용자가 알림 프롬프트와 상호작용한 후 푸시 인증 결과를 Braze에 전달합니다.
4. APN 등록 프로세스를 시작합니다. 이 작업은 메인 스레드에서 수행해야 합니다. 등록이 성공하면 앱은 `AppDelegate` 객체의 `didRegisterForRemoteNotificationsWithDeviceToken` 메서드를 호출합니다.

{% subtabs global %}
{% subtab Swift %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions:[UIApplication.LaunchOptionsKey:Any]?) {
  Appboy.start(withAPIKey: apikey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)
  // 1
  let options: UNAuthorizationOptions = [.alert, .sound, .badge]
  // 2
  UNUserNotificationCenter.current().requestAuthorization(option: options) { (granted, error) in
  // 3
    Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
  }

  // 4
  UIApplications.shared.registerForRemoteNotificiations()
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [Appboy startWithApiKey:[self apiKey] inApplication:application withLaunchOptions:launchOptions withAppboyOptions:[self appboyOptions]];

  // 1
  UNAuthorizationOptions options = (UNAuthorizationOptionSound | UNAuthorizationOptionAlert | UNAuthorizationOptionBadge);

  // 2
  [[UNUserNotificationCenter currentNotificationCenter] requestAuthorizationWithOptions:options completionHandler:^(BOOL granted, NSError * _Nullable error) {
  // 3
    [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];

  // 4
  [[UIApplication sharedApplication] registerForRemoteNotifications];
}
```
{% endsubtab %}
{% endsubtabs %}

{% alert checkpoint %}
코드를 컴파일하고 애플리케이션을 실행하세요.
- 앱에서 푸시 알림에 대한 프롬프트가 표시되는지 확인한 후 다음 단계로 진행하세요.
- 프롬프트가 표시되지 않으면, 이전에 푸시 알림 프롬프트가 표시되지 않았는지 앱을 삭제하고 다시 설치해 보세요.

다음 단계로 진행하기 전에 푸시 알림 프롬프트가 표시되는지 확인하세요.
{% endalert %}

{% endtab %}
{% tab Step 3: Forward Methods %}

##### 푸시 알림 메서드 전달 {#forward-push-notification-methods}

다음으로, Braze iOS SDK에서 처리할 수 있도록 `AppDelegate.swift`에서 `BrazeManager.swift`로 시스템 푸시 알림 메서드를 전달합니다.

###### 1단계: 푸시 알림 코드용 확장 생성 {#step-1-create-extension-for-push-notification-code}

`BrazeManager.swift` 파일에 푸시 알림 코드용 확장(extension)을 생성하여 헬퍼 파일에서 어떤 목적을 수행하는지 더 체계적으로 읽을 수 있도록 합니다:

1. `AppDelegate`에 `import AppboyUI` 구문을 포함하지 않는 패턴에 따라, `BrazeManager.swift` 파일에서 푸시 알림 메서드를 처리합니다. 사용자의 기기 토큰은 `didRegisterForRemote...` 메서드에서 Braze에 전달되어야 합니다. 이 메서드는 무음 푸시 알림을 구현하는 데 필요합니다. 다음으로, `BrazeManager` 클래스에 `AppDelegate`의 동일한 메서드를 추가합니다.
2. 메서드 내부에 다음 줄을 추가하여 Braze에 기기 토큰을 등록합니다. 이는 Braze가 토큰을 현재 기기와 연결하는 데 필요합니다.

{% subtabs global %}
{% subtab Swift %}

```swift
// MARK - Push Notifications
extension BrazeManager {
  // 1
  func application(
    _ application: UIApplication,
    didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data
  ) {
    // 2
    Appboy.sharedInstance().?registerDeviceToken(deviceToken)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK - Push Notifications
// 1
- (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
  // 2
  [[Appboy sharedInstance] registerDeviceToken:deviceToken];
}
```
{% endsubtab %}
{% endsubtabs %}

###### 2단계: 원격 알림 지원 {#step-2-support-remote-notifications}
**Signing & Capabilities** 탭에서 **Background Modes** 지원을 추가하고 **Remote notifications**를 선택하여 Braze에서 발신하는 원격 푸시 알림 지원을 시작합니다.<br><br>![Signing & Capabilities 설정 화면]({% image_buster /assets/img/ios_sdk/ios_sdk3.png %})

###### 3단계: 원격 알림 처리 {#step-3-remote-notification-handling}
Braze SDK는 Braze에서 발신하는 원격 푸시 알림을 처리할 수 있습니다. 원격 알림을 Braze에 전달하면 SDK가 Braze에서 발신하지 않은 푸시 알림은 자동으로 무시합니다. 푸시 알림 확장(extension)에 있는 `BrazeManager.swift` 파일에 다음 메서드를 추가하세요.

{% subtabs global %}
{% subtab Swift %}
```swift
func application(
  _ application: UIApplication,
  didReceiveRemoteNotification userInfo: [AnyHashable : Any],
  fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void
) {
  Appboy.sharedInstance()?.register(
    application,
    didReceiveRemoteNotification: userInfo,
    fetchCompletionHandler: completionHandler
  )
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult))completionHandler {
  [[Appboy sharedInstance] registerApplication:application didReceiveRemoteNotification:userInfo fetchCompletionHandler:completionHandler];
}
```
{% endsubtab %}
{% endsubtabs %}

###### 4단계: 알림 응답 전달 {#step-4-forward-notification-responses}

Braze SDK는 Braze에서 발신하는 푸시 알림의 응답을 처리할 수 있습니다. 알림의 응답을 Braze에 전달하면 SDK가 Braze에서 발신하지 않은 푸시 알림의 응답은 자동으로 무시합니다. `BrazeManager.swift` 파일에 다음 메서드를 추가하세요:

{% subtabs global %}
{% subtab Swift %}

```swift
func userNotificationCenter(
  _ center: UNUserNotificationCenter,
  didReceive response: UNNotificationResponse,
  withCompletionHandler completionHandler: @escaping () -> Void
) {
  Appboy.sharedInstance()?.userNotificationCenter(
    center,
    didReceive: response,
    withCompletionHandler: completionHandler
  )
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
didReceiveNotificationResponse:(UNNotificationResponse *)response
         withCompletionHandler:(void (^)(void))completionHandler {
  [[Appboy sharedInstance] userNotificationCenter:center
                   didReceiveNotificationResponse:response
                            withCompletionHandler:completionHandler];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
코드를 컴파일하고 애플리케이션을 실행하세요.<br><br>Braze 대시보드에서 자신에게 푸시 알림을 보내보고, 다음 단계로 진행하기 전에 푸시 알림에서 분석이 기록되고 있는지 확인하세요.
{% endalert %}

### 사용자 변수 및 메서드 접근 {#access-user-variables-and-methods}

{% tabs local %}
{% tab Create User Variables and Methods %}

#### 사용자 변수 및 메서드 생성 {#create-user-variables-and-methods}

다음으로, `ABKUser` 변수와 메서드에 쉽게 접근할 수 있어야 합니다. `BrazeManager.swift` 파일에 사용자 코드용 확장(extension)을 생성하여 헬퍼 파일에서 어떤 목적을 수행하는지 더 체계적으로 읽을 수 있도록 합니다:

1. `ABKUser` 객체는 iOS 애플리케이션에서 알려진 또는 익명 사용자를 나타냅니다. `ABKUser`를 검색하기 위한 계산 프로퍼티를 추가합니다. 이 변수는 사용자에 대한 변수를 검색하는 데 재사용됩니다.
2. `userId`에 쉽게 접근하기 위해 사용자 변수를 쿼리합니다. 다른 변수들 중에서도 `ABKUser` 객체는 (`firstName`, `lastName`, `phone`, `homeCity` 등)을 관리합니다.
3. 해당하는 `userId`로 `changeUser()`를 호출하여 사용자를 설정합니다.

{% subtabs global %}
{% subtab Swift %}

```swift
// MARK: - User
extension BrazeManager {
  // 1
  var user: ABKUser? {
    return Appboy.sharedInstance()?.user
  }

  // 2
  var userId: String? {
    return user?.userID
  }

  // 3
  func changeUser(_ userId: String) {
    Appboy.sharedInstance()?.changeUser(userId)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK: - User
  // 1
- (ABKUser *)user {
  return [[Appboy sharedInstance] user];
}

   // 2
- (NSString *)userId {
  return [self user].userID;
}

  // 3
- (void)changeUser:(NSString *)userId {
  [[Appboy sharedInstance] changeUser:userId];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
코드를 컴파일하고 애플리케이션을 실행하세요.<br><br>성공적인 로그인/가입에서 사용자를 식별해 보세요. 적절한 사용자 식별자가 무엇이고 무엇이 아닌지 확실히 이해하고 있어야 합니다.<br><br>대시보드에서 사용자 식별자가 기록되고 있는지 확인한 후 다음 단계로 진행하세요.
{% endalert %}

### 분석 로깅 {#log-analytics}

{% tabs local %}
{% tab Step 1: Custom Events %}

#### 커스텀 이벤트 로깅 메서드 생성 {#create-log-custom-event-method}

다음 Braze SDK의 `logCustomEvent` 메서드를 기반으로 대응하는 메서드를 생성합니다.

**Braze `logCustomEvent` 참조 메서드**<br>
이는 오직 `BrazeManager.swift` 파일만 Braze iOS SDK 메서드에 직접 접근할 수 있도록 의도적으로 설계된 것입니다. 따라서 대응하는 메서드를 생성하면 결과는 동일하며, 프로덕션 코드에서 Braze iOS SDK에 대한 직접적인 의존성 없이 수행됩니다.

```
open func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable : Any]?)
```

**대응 메서드**<br>
`Appboy` 객체에서 Braze로 커스텀 이벤트를 로깅합니다. `Properties`는 기본값이 nil인 선택적 매개변수입니다. 커스텀 이벤트에는 프로퍼티가 필수가 아니지만 이름은 필수입니다.

{% subtabs global %}
{% subtab Swift %}
```swift
func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable: Any]? = nil) {
  Appboy.sharedInstance()?.logCustomEvent(eventName, withProperties: properties)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logCustomEvent:(NSString *)eventName withProperties:(nullable NSDictionary *)properties {
  [[Appboy sharedInstance] logCustomEvent:eventName withProperties:properties];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Step 2: Custom Attributes %}

##### 커스텀 속성 로깅 메서드 생성 {#create-log-custom-attributes-method}

SDK는 다양한 타입을 커스텀 속성으로 로깅할 수 있습니다. 설정할 수 있는 각 값 타입에 대해 헬퍼 메서드를 생성할 필요는 없습니다. 대신, 적절한 값으로 필터링할 수 있는 하나의 메서드만 노출하세요.

```
- (BOOL)setCustomAttributeWithKey:(NSString *)key andBOOLValue:(BOOL)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andIntegerValue:(NSIntenger)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDoubleValue:(double)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andStringValue:(NSString *)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDateValue:(NSDate *)value;
```

커스텀 속성은 `ABKUser` 객체에서 로깅됩니다.

속성에 설정할 수 있는 모든 사용 가능한 타입을 포괄할 수 있는 **하나의 메서드**를 생성합니다. 이 메서드를 `BrazeManager.swift` 파일의 분석 확장(extension)에 추가합니다. 유효한 커스텀 속성 타입을 필터링하고 일치하는 타입과 연관된 메서드를 호출하여 이를 수행할 수 있습니다.

- 매개변수 `value`는 `Equatable` 프로토콜을 준수하는 제네릭 타입입니다. 이는 타입이 Braze iOS SDK에서 기대하는 것과 다를 경우 컴파일 타임 오류가 발생하도록 명시적으로 설계된 것입니다.
- 매개변수 `key`와 `value`는 메서드 내에서 조건부로 언래핑되는 선택적 매개변수입니다. 이는 nil이 아닌 값이 Braze iOS SDK에 전달되도록 보장하는 방법 중 하나입니다.

{% subtabs global %}
{% subtab Swift %}

```swift
func setCustomAttributeWithKey<T: Equatable>(_ key: String?, andValue value: T?) {
  guard let key = key, let value = value else { return }
  switch value.self {
  case let value as Date:
    user?.setCustomAttributeWithKey(key, andDateValue: value)
  case let value as Bool:
    user?.setCustomAttributeWithKey(key, andBOOLValue: value)
  case let value as String:
    user?.setCustomAttributeWithKey(key, andStringValue: value)
  case let value as Double:
    user?.setCustomAttributeWithKey(key, andDoubleValue: value)
  case let value as Int:
    user?.setCustomAttributeWithKey(key, andIntegerValue: value)
  default:
   return
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)setCustomAttributeWith:(NSString *)key andValue:(id)value {
  if ([value isKindOfClass:[NSDate class]]) {
    [[self user] setCustomAttributeWithKey:key andDateValue:value];
  } else if ([value isKindOfClass:[NSString class]]) {
    [[self user] setCustomAttributeWithKey:key andStringValue:value];
  } else if ([value isKindOfClass:[NSNumber class]]) {
    if (strcmp([value objCType], @encode(double)) == 0) {
      [[self user] setCustomAttributeWithKey:key andDoubleValue:[value doubleValue]];
    } else if (strcmp([value objCType], @encode(int)) == 0) {
      [[self user] setCustomAttributeWithKey:key andIntegerValue:[value integerValue]];
    } else if ([value boolValue]) {
      [[self user] setCustomAttributeWithKey:key andBOOLValue:[value boolValue]];
    }
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Step 3: Purchases %}

##### 구매 로깅 메서드 생성 {#create-log-purchase-method}

다음으로, 아래 Braze SDK의 `logPurchase` 메서드를 기반으로 대응하는 메서드를 생성합니다.

**Braze `logPurchase` 참조 메서드**<br>
이는 오직 `BrazeManager.swift` 파일만 Braze iOS SDK 메서드에 직접 접근할 수 있도록 의도적으로 설계된 것입니다. 따라서 대응하는 메서드를 생성하면 결과는 동일하며, 프로덕션 코드에서 Braze iOS SDK에 대한 직접적인 의존성 없이 수행됩니다.

```
open func logPurchase(_ productIdentifier: String, inCurrency currency: String, atPrice price: NSDecimalNumber, withoutQuantity quantity: UInt)
```
**대응 메서드**<br>
`Appboy` 객체에서 Braze로 구매를 로깅합니다. SDK에는 구매를 로깅하는 여러 메서드가 있으며, 이것은 하나의 예시입니다. 이 메서드는 `NSDecimal` 및 `UInt` 객체 생성도 처리합니다. 해당 부분을 어떻게 처리할지는 여러분에게 달려 있으며, 여기서는 하나의 예시를 제공합니다.

{% subtabs global %}
{% subtab Swift %}

```swift
func logPurchase(_ productIdentifier: String, inCurrency currency: String, atPrice price:
String, withQuantity quantity: Int) {

  Appboy.sharedInstance()?.logPurchase(productIdentifier, inCurrency: currency, atPrice: NSDecimalNumber(string: price), withQuantity: UInt(quantity))

}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPurchase:(NSString *)productIdentifier inCurrency:(nonnull NSString *)currencyCode atPrice:(nonnull NSDecimalNumber *)price withQuantity:(NSUInteger)quantity {
  [[Appboy sharedInstance] logPurchase:productIdentifier inCurrency:currencyCode atPrice:price withQuantity:quantity];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
코드를 컴파일하고 애플리케이션을 실행하세요.<br><br>커스텀 이벤트를 로깅해 보세요.<br><br>대시보드에서 커스텀 이벤트가 기록되고 있는지 확인한 후 다음 단계로 진행하세요.
{% endalert %}

### 인앱 메시지 {#in-app-messages}

{% tabs local %}
{% tab Step 1: Conform to Delegate %}

{% alert important %}
애플리케이션에서 이 채널을 사용할 계획이 없다면 다음 인앱 메시지 섹션은 통합에 필수가 아닙니다.
{% endalert %}

#### ABKInAppMessageUIDelegate 준수 {#conform-to-abkinappmessageuidelegate}

다음으로, `BrazeManager.swift` 파일 코드가 `ABKInAppMessageUIDelegate`를 준수하여 관련 메서드를 직접 처리할 수 있도록 합니다.

델리게이트 준수 코드는 `BrazeManager.swift` 파일의 `didFinishLaunching...` 메서드에 추가됩니다. 초기화 코드는 다음과 같이 구성됩니다:

{% subtabs global %}
{% subtab swift %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) {
  Appboy.start(withApiKey: apiKey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)

  let options: UNAuthorizationOptions = [.alert, .sound, .badge]
  UNUserNotificationCenter.current().requestAuthorization(options: options) { (granted, error) in
    Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
  }
  UIApplication.shared.registerForRemoteNotifications()

  Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController?.setInAppMessageUIDelegate?(self)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [Appboy startWithApiKey:[self apiKey] inApplication:application withLaunchOptions:launchOptions withAppboyOptions:[self appboyOptions]];

  UNAuthorizationOptions options = (UNAuthorizationOptionSound | UNAuthorizationOptionAlert | UNAuthorizationOptionBadge);
  [[UNUserNotificationCenter currentNotificationCenter] requestAuthorizationWithOptions:options completionHandler:^(BOOL granted, NSError * _Nullable error) {
    [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];
  [[UIApplication sharedApplication] registerForRemoteNotifications];

  [[Appboy sharedInstance].inAppMessageController.inAppMessageUIController setInAppMessageUIDelegate:self];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Step 2: Add Delegate Methods %}

##### 델리게이트 메서드 추가 {#add-delegate-methods}
다음으로, `ABKInAppMessageUIDelegate`를 준수하는 확장(extension)을 생성합니다.

분석 섹션에 다음 스니펫을 추가합니다. `BrazeManager.swift` 객체가 델리게이트로 설정되어 있으므로, `BrazeManager.swift` 파일이 모든 `ABKInAppMessageUIDelegate` 메서드를 처리하게 됩니다.

{% alert important %}
`ABKInAppMessageUIDelegate`에는 필수 메서드가 없지만, 다음은 하나의 예시입니다.
{% endalert %}

{% subtabs global %}
{% subtab Swift %}
```swift
// MARK: - ABKInAppMessage UI Delegate
extension AppboyManager: ABKInAppMessageUIDelegate{
  func inAppMessageViewControllerWith(_ inAppMessage: ABKInAppMessage) -> ABKInAppMessageViewController {
    switch inAppMessage {
    case is ABKInAppMessageSlideup:
      return ABKInAppMessageSlideupViewController(inAppMessage: inAppMessage)
    case is ABKInAppMessageModal:
      return ABKInAppMessageModalViewController(inAppMessage: inAppMessage)
    case is ABKInAppMessageFull:
      return ABKInAppMessageFullViewController(inAppMessage: inAppMessage)
    case is ABKInAppMessageHTML:
      return ABKInAppMessageHTMLViewController(inAppMessage: inAppMessage)
    default:
      return ABKInAppMessageViewController(inAppMessage: inAppMessage)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK: - ABKInAppMessage UI Delegate
- (ABKInAppMessageViewController *)inAppMessageViewControllerWithInAppMessage:(ABKInAppMessage *)inAppMessage {
  if ([inAppMessage isKindOfClass:[ABKInAppMessageSlideup class]]) {
    return [[ABKInAppMessageSlideupViewController alloc] initWithInAppMessage:inAppMessage];
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageModal class]]) {
    return [[ABKInAppMessageModalViewController alloc] initWithInAppMessage:inAppMessage];
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageFull class]]) {
    return [[ABKInAppMessageFullViewController alloc] initWithInAppMessage:inAppMessage];
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageHTML class]]) {
    return [[ABKInAppMessageHTMLViewController alloc] initWithInAppMessage:inAppMessage];
  }
  return nil;
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
코드를 컴파일하고 애플리케이션을 실행하세요.<br><br>자신에게 인앱 메시지를 보내보세요.<br><br>`BrazeManager.swift` 파일에서 `ABKInAppMessageUIDelegate` 메서드 예제의 진입점에 브레이크포인트를 설정합니다. 자신에게 인앱 메시지를 보내고, 다음 단계로 진행하기 전에 브레이크포인트가 적중되는지 확인하세요.
{% endalert %}

### Content Cards {#content-cards}

{% tabs local %}
{% tab Create Content Card Variables and Methods %}

{% alert important %}
애플리케이션에서 이 채널을 사용할 계획이 없다면 다음 Content Cards 섹션은 통합에 필수가 아닙니다.
{% endalert %}

#### Content Cards 변수 및 메서드 생성 {#create-content-card-variables-and-methods}

불필요한 `import AppboyUI` 구문 없이 프로덕션 코드에서 Content Cards 뷰 컨트롤러를 표시할 수 있도록 합니다.

`BrazeManager.swift` 파일에 Content Cards 코드용 확장(extension)을 생성하여 헬퍼 파일에서 어떤 목적을 수행하는지 더 체계적으로 읽을 수 있도록 합니다:

1. `ABKContentCardsTableViewController`를 표시합니다. 뷰 컨트롤러를 present 또는 push하기 위해 필요한 유일한 매개변수는 선택적 `navigationController`입니다.
2. `ABKContentCardsTableViewController` 객체를 초기화하고 선택적으로 제목을 변경합니다. 또한 초기화된 뷰 컨트롤러를 내비게이션 스택에 추가해야 합니다.

{% subtabs global %}
{% subtab Swift %}
```swift
// MARK: - Content Cards
extension BrazeManager {

  // 1
  func displayContentCards(navigationController: UINavigationController?) {

    // 2
    let contentCardsVc = ABKContentCardsTableViewController()
    contentCardsVc.title = "Content Cards"
    navigationController?.pushViewController(contentCardsVc, animated: true)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK: - Content Cards
  // 1
- (void)displayContentCards:(UINavigationController *)navigationController {
  // 2
  ABKContentCardsTableViewController *contentCardsVc = [[ABKContentCardsTableViewController alloc] init];
  contentCardsVc.title = @"Content Cards";
  [navigationController pushViewController:contentCardsVc animated:YES];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
코드를 컴파일하고 애플리케이션을 실행하세요.<br><br>다음 단계로 진행하기 전에 애플리케이션에서 `ABKContentCardsTableViewController`를 표시해 보세요.
{% endalert %}

## 다음 단계 {#next-steps}

축하합니다! 모범 사례 통합 가이드를 완료했습니다! `BrazeManager` 헬퍼 파일 예시는 [GitHub](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/BrazeManager.swift)에서 확인할 수 있습니다.

이제 Braze iOS SDK에 대한 종속성을 나머지 프로덕션 코드와 분리했으므로, 선택적 고급 구현 가이드를 확인해 보세요:

{% article_tiles %}
- name: 고급 푸시 알림 구현 가이드
  link: /docs/developer_guide/platforms/legacy_sdks/ios/push_notifications/implementation_guide
  description: iOS 앱에서 푸시 알림 동작을 커스터마이징하기 위한 선택적 고급 패턴입니다.
- name: 고급 인앱 메시지 구현 가이드
  link: /docs/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/implementation_guide
  description: 인앱 메시지 전달 및 표시를 커스터마이징하기 위한 선택적 고급 패턴입니다.
- name: 고급 Content Cards 구현 가이드
  link: /docs/developer_guide/platforms/legacy_sdks/ios/content_cards/implementation_guide
  description: Content Cards 피드 및 UI를 커스터마이징하기 위한 선택적 고급 패턴입니다.
{% endarticle_tiles %}