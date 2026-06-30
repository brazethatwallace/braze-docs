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

다음 단계는 프로덕션 코드가 호출하는 `BrazeManager` 헬퍼 파일을 빌드하는 데 도움이 됩니다. 이 헬퍼 파일은 아래 나열된 통합 주제에 대한 다양한 확장을 추가하여 모든 Braze 관련 종속성을 처리합니다. 각 주제에는 Swift 및 Objective-C 모두에 대한 가로 탭 단계와 코드 스니펫이 포함됩니다. 애플리케이션에서 해당 채널을 사용할 계획이 없는 경우 Content Cards 및 인앱 메시지 단계는 통합에 필요하지 않습니다.

- [BrazeManager.swift 생성](#create-brazemanagerswift)
- [SDK 초기화](#initialize-the-sdk)
- [푸시 알림](#push-notifications)
- [사용자 변수 및 메서드 액세스](#access-user-variables-and-methods)
- [분석 로깅](#log-analytics)
- [인앱 메시지(선택 사항)](#in-app-messages)
- [Content Cards(선택 사항)](#content-cards)
- [다음 단계](#next-steps)

### BrazeManager.swift 생성 {#create-brazemanagerswift}

{% tabs local %}
{% tab BrazeManager swift 생성 %}

#### BrazeManager.swift 생성
`BrazeManager.swift` 파일을 빌드하려면 _BrazeManager_라는 이름의 새 Swift 파일을 생성하여 원하는 위치의 프로젝트에 추가합니다. 그런 다음 `import Foundation`을 SPM의 경우 `import AppboyUI`(CocoaPods의 경우 `import Appboy_iOS_SDK`)로 바꾸고, 모든 Braze 관련 메서드와 변수를 호스팅하는 데 사용할 `BrazeManager` 클래스를 생성합니다. `Appboy_iOS_SDK`

{% alert note %}
- `BrazeManager`는 구조체가 아닌 `NSObject` 클래스이므로 `ABKInAppMessageUIDelegate`와 같은 ABK 델리게이트를 준수할 수 있습니다.
- `BrazeManager`는 설계상 싱글톤 클래스이므로 이 클래스의 인스턴스 하나만 사용됩니다. 이는 오브젝트에 대한 통합 액세스 지점을 제공하기 위한 것입니다.
{% endalert %}

1. `BrazeManager` 클래스를 초기화하는 _shared_라는 정적 변수를 추가합니다. 이는 한 번만 지연 초기화되도록 보장합니다.
2. 그런 다음 _apiKey_라는 비공개 상수 변수를 추가하고 Braze 대시보드의 워크스페이스에서 API 키 값으로 설정합니다.
3. SDK에 대한 구성 값을 저장할 _appboyOptions_라는 비공개 계산 변수를 추가합니다. 지금은 비어 있습니다.

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
{% tab 1단계: BrazeManager swift에서 SDK 초기화 %}

#### BrazeManager.swift에서 SDK 초기화 {#initialize-sdk-from-brazemanagerswift}
다음으로 SDK를 초기화해야 합니다. 이 가이드에서는 이미 Xcode 프로젝트에 [SDK를 추가]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview)했다고 가정합니다. 또한 `Info.plist` 파일 또는 `appboyOptions`에서 [워크스페이스 SDK 엔드포인트]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration#step-2-specify-your-data-cluster)와 [`LogLevel`]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations#braze-log-level)이 설정되어 있어야 합니다.

`BrazeManager.swift` 파일에서 반환 유형 없이 `AppDelegate.swift` 파일의 `didFinishLaunchingWithOptions` 메서드를 추가합니다. `BrazeManager.swift` 파일에 유사한 메서드를 생성하면 `AppDelegate.swift` 파일에 `import AppboyUI` 문이 필요하지 않습니다.

그런 다음 새로 선언한 `apiKey` 및 `appboyOptions` 변수를 사용하여 SDK를 초기화합니다.

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
{% tab 2단계: Appboy 초기화 처리 %}

##### AppDelegate.swift에서 Appboy 초기화 처리 {#handle-appboy-initialization-in-the-appdelegateswift}
그런 다음 `AppDelegate.swift` 파일로 돌아가 AppDelegate의 `didFinishLaunchingWithOptions` 메서드에 다음 코드 스니펫을 추가하여 `BrazeManager.swift` 헬퍼 파일에서 Appboy 초기화를 처리합니다. `AppDelegate.swift`에 `import AppboyUI` 문을 추가할 필요가 없다는 점을 기억하세요.

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
코드를 컴파일하고 애플리케이션을 실행합니다.<br><br>이 시점에서 SDK가 가동 및 실행 중이어야 합니다. 대시보드에서 더 진행하기 전에 세션이 기록되는지 확인합니다.
{% endalert %}

### 푸시 알림 {#push-notifications}

{% tabs local %}
{% tab 1단계: 푸시 인증서 추가 %}

#### 푸시 인증서 추가 {#add-push-certificate}

Braze 대시보드에서 기존 워크스페이스로 이동합니다. **푸시 알림 설정**에서 푸시 인증서 파일을 Braze 대시보드에 업로드하고 저장합니다.

![APNs 키 업로드 필드가 있는 Braze 대시보드 푸시 알림 설정.]({% image_buster /assets/img/ios_sdk/ios_sdk2.png %}){: style="max-width:60%;"}

{% endtab %}
{% tab 2단계: 알림 등록 %}

{% alert important %}
이 단계의 마지막에 있는 전용 체크포인트를 놓치지 마세요!
{% endalert %}

##### 푸시 알림 등록 {#register-for-push-notifications}

다음으로 푸시 알림을 등록합니다. 이 가이드에서는 Apple 개발자 포털 및 Xcode 프로젝트에서 [푸시 자격 증명을 올바르게 설정]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration)했다고 가정합니다.

푸시 알림을 등록하는 코드는 `BrazeManager.swift` 파일의 `didFinishLaunching...` 메서드에 추가됩니다. 초기화 코드는 다음과 같이 완성되어야 합니다:

1. 사용자와 상호 작용하기 위한 권한 요청 콘텐츠를 구성합니다. 이러한 옵션은 예시로 나열되어 있습니다.
2. 사용자에게 푸시 알림을 보낼 수 있는 권한을 요청합니다. 푸시 알림을 허용하거나 거부하는 사용자의 응답은 `granted` 변수에서 추적됩니다.
3. 사용자가 알림 프롬프트와 상호 작용한 후 푸시 인증 결과를 Braze에 전달합니다.
4. APNs로 등록 프로세스를 시작합니다. 이 작업은 메인 스레드에서 수행해야 합니다. 등록이 성공하면 앱이 `AppDelegate` 오브젝트의 `didRegisterForRemoteNotificationsWithDeviceToken` 메서드를 호출합니다.

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
코드를 컴파일하고 애플리케이션을 실행합니다.
- 더 진행하기 전에 앱에서 푸시 알림 프롬프트가 표시되는지 확인하세요.
- 프롬프트가 표시되지 않으면 앱을 삭제한 후 다시 설치하여 이전에 푸시 알림 프롬프트가 표시되지 않았는지 확인합니다.

더 진행하기 전에 푸시 알림 프롬프트가 표시되는지 확인합니다.
{% endalert %}

{% endtab %}
{% tab 3단계: 메서드 전달 %}

##### 푸시 알림 메서드 전달 {#forward-push-notification-methods}

다음으로 Braze iOS SDK에서 처리하도록 시스템 푸시 알림 메서드를 `AppDelegate.swift`에서 `BrazeManager.swift`로 전달합니다.

###### 1단계: 푸시 알림 코드 확장 생성 {#step-1-create-extension-for-push-notification-code}

`BrazeManager.swift` 파일에 푸시 알림 코드의 확장을 생성하여 헬퍼 파일에서 어떤 용도를 지원하는지 보다 체계적으로 파악할 수 있도록 합니다:

1. `AppDelegate`에 `import AppboyUI` 문을 포함하지 않는 패턴에 따라 `BrazeManager.swift` 파일에서 푸시 알림 메서드를 처리합니다. 사용자의 기기 토큰은 `didRegisterForRemote...` 메서드를 통해 Braze에 전달되어야 합니다. 이 메서드는 무음 푸시 알림을 구현하는 데 필요합니다. 그런 다음 `BrazeManager` 클래스에 `AppDelegate`와 동일한 메서드를 추가합니다.
2. 메서드 안에 다음 줄을 추가하여 기기 토큰을 Braze에 등록합니다. 이는 Braze가 토큰을 현재 기기와 연결하기 위해 필요합니다.

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
**Signing & Capabilities** 탭에서 **Background Modes** 지원을 추가하고 **Remote notifications**를 선택하여 Braze에서 발생하는 원격 푸시 알림 지원을 시작합니다.<br><br>![Signing & Capabilities]({% image_buster /assets/img/ios_sdk/ios_sdk3.png %})

###### 3단계: 원격 알림 처리 {#step-3-remote-notification-handling}
Braze SDK는 Braze에서 발생하는 원격 푸시 알림을 처리할 수 있습니다. 원격 알림을 Braze로 전달하면 SDK가 Braze에서 발생하지 않은 푸시 알림을 자동으로 무시합니다. 푸시 알림 확장의 `BrazeManager.swift` 파일에 다음 메서드를 추가합니다.

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

Braze SDK는 Braze에서 발생하는 푸시 알림의 응답을 처리할 수 있습니다. 알림의 응답을 Braze로 전달하면 SDK가 Braze에서 발생하지 않은 푸시 알림의 응답을 자동으로 무시합니다. `BrazeManager.swift` 파일에 다음 메서드를 추가합니다:

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
코드를 컴파일하고 애플리케이션을 실행합니다. <br><br>더 진행하기 전에 Braze 대시보드에서 푸시 알림을 직접 보내고 푸시 알림에서 분석이 기록되는지 확인합니다.
{% endalert %}

### 사용자 변수 및 메서드 액세스 {#access-user-variables-and-methods}

{% tabs local %}
{% tab 사용자 변수 및 메서드 생성 %}

#### 사용자 변수 및 메서드 생성 {#create-user-variables-and-methods}

다음으로 `ABKUser` 변수와 메서드에 쉽게 액세스할 수 있어야 합니다. `BrazeManager.swift` 파일에 사용자 코드의 확장을 생성하여 헬퍼 파일에서 어떤 용도를 지원하는지 보다 체계적으로 파악할 수 있도록 합니다:

1. `ABKUser` 오브젝트는 iOS 애플리케이션에서 알려진 사용자 또는 익명 사용자를 나타냅니다. `ABKUser`를 검색하는 계산 변수를 추가합니다. 이 변수는 사용자에 대한 변수를 검색하는 데 재사용됩니다.
2. 사용자 변수를 쿼리하여 `userId`에 쉽게 액세스할 수 있습니다. 다른 변수 중에서도 `ABKUser` 오브젝트는 `firstName`, `lastName`, `phone`, `homeCity` 등을 담당합니다.
3. 해당 `userId`로 `changeUser()`를 호출하여 사용자를 설정합니다.

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
코드를 컴파일하고 애플리케이션을 실행합니다.<br><br>로그인/가입에 성공한 사용자를 식별해 보세요. 적절한 사용자 식별자와 부적절한 사용자 식별자를 확실히 이해해야 합니다. <br><br>대시보드에서 더 진행하기 전에 사용자 식별자가 기록되는지 확인합니다.
{% endalert %}

### 분석 로깅 {#log-analytics}

{% tabs local %}
{% tab 1단계: 커스텀 이벤트 %}

#### 커스텀 이벤트 로깅 메서드 생성 {#create-log-custom-event-method}

다음 Braze SDK `logCustomEvent` 메서드를 기반으로 일치하는 메서드를 생성합니다.

**Braze `logCustomEvent` 참조 메서드**<br>
`BrazeManager.swift` 파일만 Braze iOS SDK 메서드에 직접 액세스할 수 있기 때문에 의도된 설계입니다. 따라서 일치하는 메서드를 생성하면 결과는 동일하며 프로덕션 코드에서 Braze iOS SDK에 직접 종속될 필요 없이 수행됩니다.

```
open func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable : Any]?)
```

**매칭 메서드**<br>
`Appboy` 오브젝트에서 Braze로 커스텀 이벤트를 로깅합니다. `Properties`는 기본값이 nil인 선택적 매개변수입니다. 커스텀 이벤트에는 속성이 필요하지 않지만 이름은 필수입니다.

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
{% tab 2단계: 커스텀 속성 %}

##### 커스텀 속성 로깅 메서드 생성 {#create-log-custom-attributes-method}

SDK는 다양한 유형을 커스텀 속성으로 로깅할 수 있습니다. 설정할 수 있는 각 값 유형에 대해 헬퍼 메서드를 만들 필요가 없습니다. 대신 적절한 값으로 필터링할 수 있는 하나의 메서드만 노출하세요.

```
- (BOOL)setCustomAttributeWithKey:(NSString *)key andBOOLValue:(BOOL)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andIntegerValue:(NSIntenger)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDoubleValue:(double)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andStringValue:(NSString *)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDateValue:(NSDate *)value;
```

커스텀 속성은 `ABKUser` 오브젝트에서 로깅됩니다.

속성에 설정할 수 있는 모든 유형을 포괄하는 **하나의 메서드**를 생성합니다. 분석 확장의 `BrazeManager.swift` 파일에 이 메서드를 추가합니다. 유효한 커스텀 속성 유형을 필터링하고 일치하는 유형과 연결된 메서드를 호출하면 됩니다.

- `value` 매개변수는 `Equatable` 프로토콜을 따르는 제네릭 유형입니다. 이는 명시적으로 수행되므로 유형이 Braze iOS SDK가 예상하는 것과 다르면 컴파일 시 오류가 발생합니다.
- `key` 및 `value` 매개변수는 메서드에서 조건부로 언래핑되는 선택적 매개변수입니다. 이는 nil이 아닌 값이 Braze iOS SDK에 전달되도록 보장하는 한 가지 방법일 뿐입니다.

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
{% tab 3단계: 구매 %}

##### 구매 로깅 메서드 생성 {#create-log-purchase-method}

다음으로 Braze SDK `logPurchase` 메서드를 기반으로 일치하는 메서드를 생성합니다.

**Braze `logPurchase` 참조 메서드**<br>
`BrazeManager.swift` 파일만 Braze iOS SDK 메서드에 직접 액세스할 수 있기 때문에 의도된 설계입니다. 따라서 일치하는 메서드를 생성하면 결과는 동일하며 프로덕션 코드에서 Braze iOS SDK에 직접 종속될 필요 없이 수행됩니다.

```
open func logPurchase(_ productIdentifier: String, inCurrency currency: String, atPrice price: NSDecimalNumber, withoutQuantity quantity: UInt)
```
**매칭 메서드**<br>
`Appboy` 오브젝트에서 구매를 Braze에 로깅합니다. SDK에는 구매를 로깅하는 여러 가지 메서드가 있으며, 이는 한 가지 예시일 뿐입니다. 이 메서드는 `NSDecimal` 및 `UInt` 오브젝트 생성도 처리합니다. 이 부분을 어떻게 처리할지는 여러분이 결정할 수 있으며, 이는 하나의 예시일 뿐입니다.

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
코드를 컴파일하고 애플리케이션을 실행합니다. <br><br>커스텀 이벤트를 로깅해 보세요.<br><br>대시보드에서 더 진행하기 전에 커스텀 이벤트가 기록되는지 확인합니다.
{% endalert %}

### 인앱 메시지 {#in-app-messages}

{% tabs local %}
{% tab 1단계: 델리게이트 준수 %}

{% alert important %}
애플리케이션에서 이 채널을 사용할 계획이 없는 경우 다음 인앱 메시지 섹션은 통합에 필요하지 않습니다.
{% endalert %}

#### ABKInAppMessageUIDelegate 준수 {#conform-to-abkinappmessageuidelegate}

다음으로 `ABKInAppMessageUIDelegate`를 준수하도록 `BrazeManager.swift` 파일 코드를 활성화하여 관련 메서드를 직접 처리합니다.

델리게이트를 준수하기 위한 코드는 `BrazeManager.swift` 파일의 `didFinishLaunching...` 메서드에 추가됩니다. 초기화 코드는 다음과 같이 완성됩니다:

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
{% tab 2단계: 델리게이트 메서드 추가 %}

##### 델리게이트 메서드 추가 {#add-delegate-methods}
다음으로 `ABKInAppMessageUIDelegate`를 준수하는 확장을 생성합니다.

분석 섹션에 다음 코드 스니펫을 추가합니다. `BrazeManager.swift` 오브젝트가 델리게이트로 설정되어 있으며, 여기에서 `BrazeManager.swift` 파일이 모든 `ABKInAppMessageUIDelegate` 메서드를 처리합니다.

{% alert important %}
`ABKInAppMessageUIDelegate`에는 필수 메서드가 제공되지 않지만 다음은 한 가지 예시입니다.
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
코드를 컴파일하고 애플리케이션을 실행합니다. <br><br>인앱 메시지를 직접 보내 보세요. <br><br>`BrazeManager.swift` 파일에서 예제 `ABKInAppMessageUIDelegate` 메서드의 진입점에 중단점을 설정합니다. 더 진행하기 전에 인앱 메시지를 직접 보내고 중단점에 도달하는지 확인합니다.
{% endalert %}

### Content Cards {#content-cards}

{% tabs local %}
{% tab Content Cards 변수 및 메서드 생성 %}

{% alert important %}
애플리케이션에서 이 채널을 사용할 계획이 없는 경우 다음 Content Cards 섹션은 통합에 필요하지 않습니다.
{% endalert %}

#### Content Cards 변수 및 메서드 생성 {#create-content-card-variables-and-methods}

불필요한 `import AppboyUI` 문 없이도 프로덕션 코드에서 Content Cards 뷰 컨트롤러를 표시할 수 있습니다.

`BrazeManager.swift` 파일에 Content Cards 코드의 확장을 생성하여 헬퍼 파일에서 어떤 용도를 지원하는지 보다 체계적으로 파악할 수 있도록 합니다:

1. `ABKContentCardsTableViewController`를 표시합니다. `navigationController` 옵션은 뷰 컨트롤러를 표시하거나 푸시하는 데 필요한 유일한 매개변수입니다.
2. `ABKContentCardsTableViewController` 오브젝트를 초기화하고 선택적으로 제목을 변경합니다. 또한 초기화된 뷰 컨트롤러를 내비게이션 스택에 추가해야 합니다.

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
코드를 컴파일하고 애플리케이션을 실행합니다.<br><br>더 진행하기 전에 애플리케이션에서 `ABKContentCardsTableViewController`를 표시해 보세요.
{% endalert %}

## 다음 단계 {#next-steps}

축하합니다! 이 모범 사례 통합 가이드를 완료하셨습니다! 예제 `BrazeManager` 헬퍼 파일은 [GitHub](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/BrazeManager.swift)에서 찾을 수 있습니다.

나머지 프로덕션 코드에서 Braze iOS SDK에 대한 종속성을 분리했으므로 다음 고급 구현 가이드(선택 사항)를 확인하세요:
- [고급 푸시 알림 구현 가이드]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/implementation_guide)
- [고급 인앱 메시지 구현 가이드]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/implementation_guide)
- [고급 Content Cards 구현 가이드]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/implementation_guide)