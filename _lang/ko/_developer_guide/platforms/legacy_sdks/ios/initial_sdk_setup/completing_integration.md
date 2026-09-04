---
nav_title: 통합 완료
article_title: iOS SDK 통합 완료
platform: iOS
description: "이 참조 문서에서는 통합 옵션 중 하나를 통해 Braze SDK를 설치한 후 해당 통합을 완료하는 방법을 보여줍니다."
page_order: 2

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 통합 완료 {#complete-the-integration}

이 단계를 수행하기 전에 [Carthage]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/carthage_integration), [CocoaPods]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/cocoapods), [스위프트 패키지 매니저]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/swift_package_manager) 또는 [수동]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options) 통합을 사용하여 SDK를 통합했는지 확인하세요.

## 1단계: 앱 델리게이트 업데이트 {#step-1-update-your-app-delegate}

{% tabs %}
{% tab OBJECTIVE-C %}

Braze SDK를 CocoaPods, Carthage 또는 [동적 수동 통합]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options)으로 통합하는 경우, `AppDelegate.m` 파일에 다음 코드 줄을 추가합니다:

```objc
#import "Appboy-iOS-SDK/AppboyKit.h"
```

스위프트 패키지 매니저 또는 [정적 수동 통합]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options)으로 통합하는 경우, 대신 다음 줄을 사용합니다:

```objc
#import "AppboyKit.h"
```

그런 다음, `AppDelegate.m` 파일의 `application:didFinishLaunchingWithOptions:` 메서드 내에 다음 스니펫을 추가합니다:

```objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFIER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions];
```

`YOUR-APP-IDENTIFIER-API-KEY`를 **설정 관리** 페이지에서 올바른 값으로 업데이트합니다. 앱 식별자 API 키를 찾는 방법에 대한 자세한 내용은 [API 설명서]({{site.baseurl}}/api/identifier_types#app-identifier)를 확인하세요.

{% endtab %}
{% tab swift %}

Braze SDK를 CocoaPods, Carthage 또는 [동적 수동 통합]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options)으로 통합하는 경우, `AppDelegate.swift` 파일에 다음 코드 줄을 추가합니다:

```swift
import Appboy_iOS_SDK
```

스위프트 패키지 매니저 또는 [정적 수동 통합]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options)으로 통합하는 경우, 대신 다음 줄을 사용합니다:

```swift
import AppboyKit
```
Swift 프로젝트에서 Objective-C 코드를 사용하는 방법에 대한 자세한 내용은 [Apple 개발자 문서](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html)를 참조하세요.

그런 다음, `AppDelegate.swift`에서 `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`에 다음 스니펫을 추가합니다:

```swift
Appboy.start(withApiKey: "YOUR-APP-IDENTIFIER-API-KEY", in:application, withLaunchOptions:launchOptions)
```

`YOUR-APP-IDENTIFIER-API-KEY`를 **설정 관리** 페이지에서 올바른 값으로 업데이트합니다. 앱 식별자 API 키를 찾는 방법에 대한 자세한 내용은 [API 설명서]({{site.baseurl}}/api/identifier_types#app-identifier)를 확인하세요.

{% endtab %}
{% endtabs %}

{% alert note %}
`sharedInstance` 싱글턴은 `startWithApiKey:`가 호출되기 전까지 nil입니다. 이는 Braze 기능을 사용하기 위한 전제 조건입니다.
{% endalert %}

{% alert warning %}
반드시 애플리케이션의 메인 스레드에서 Braze를 초기화하세요. 비동기적으로 초기화하면 기능이 정상적으로 작동하지 않을 수 있습니다.
{% endalert %}

## 2단계: 데이터 클러스터 지정하기 {#step-2-specify-your-data-cluster}

{% alert note %}
2019년 12월부터 커스텀 엔드포인트는 더 이상 제공되지 않습니다. 기존에 보유한 커스텀 엔드포인트가 있는 경우 계속 사용할 수 있습니다. 자세한 내용은 <a href="{{site.baseurl}}/api/basics#endpoints">사용 가능한 엔드포인트 목록</a> 을 참조하세요.
{% endalert %}

### 컴파일 타임 엔드포인트 구성(권장) {#compile-time-endpoint-configuration-recommended}

기존에 보유한 커스텀 엔드포인트가 있는 경우:
- Braze iOS SDK v3.0.2부터 `Info.plist` 파일을 사용하여 커스텀 엔드포인트를 설정할 수 있습니다. `Info.plist` 파일에 `Braze` 사전을 추가합니다. `Braze` 사전 내에 `Endpoint` 문자열 하위 항목을 추가하고 값을 커스텀 엔드포인트 URL의 권한(예: `https://sdk.iad-01.braze.com`이 아닌 `sdk.iad-01.braze.com`)으로 설정합니다. Braze iOS SDK v4.0.2 이전에는 `Braze` 대신 `Appboy` 사전 키를 사용해야 합니다.

Braze 담당자가 이미 [올바른 엔드포인트]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)를 안내해 드렸을 것입니다.

### 런타임 엔드포인트 구성 {#runtime-endpoint-configuration}

기존에 보유한 커스텀 엔드포인트가 있는 경우:
- Braze iOS SDK v3.17.0 이상부터 `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`에 전달되는 `appboyOptions` 파라미터 내의 `ABKEndpointKey`를 통해 엔드포인트를 재정의하여 설정할 수 있습니다. 값을 커스텀 엔드포인트 URL의 권한(예: `https://sdk.iad-01.braze.com`이 아닌 `sdk.iad-01.braze.com`)으로 설정합니다.

## SDK 통합 완료 {#sdk-integration-complete}

이제 Braze가 애플리케이션에서 데이터를 수집하고 있으며, 기본 통합이 완료되었습니다. [커스텀 이벤트 추적]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=swift), [푸시 메시징]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration), 그리고 Braze 기능의 전체 스위트를 활성화하려면 다음 문서를 참조하세요.

## 시작 시 Braze 커스터마이징 {#customizing-braze-on-startup}

시작 시 Braze를 커스터마이징하려면, Braze 초기화 메서드 `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`를 사용하고, Braze 시작 키의 선택적 `NSDictionary`를 전달할 수 있습니다.
{% tabs %}
{% tab OBJECTIVE-C %}

`AppDelegate.m` 파일의 `application:didFinishLaunchingWithOptions:` 메서드 안에 다음 Braze 메서드를 추가합니다:

```objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFIER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

이 메서드는 `startWithApiKey:inApplication:withLaunchOptions:` 초기화 메서드를 대체합니다.

{% endtab %}
{% tab swift %}

`AppDelegate.swift`의 `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` 메서드 안에 다음 Braze 메서드를 추가합니다. 여기서 `appboyOptions`는 시작 구성 값의 `Dictionary`입니다:

```swift
Appboy.start(withApiKey: "YOUR-APP-IDENTIFIER-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:appboyOptions)
```

이 메서드는 `startWithApiKey:inApplication:withLaunchOptions:` 초기화 메서드를 대체합니다.

{% endtab %}
{% endtabs %}

이 메서드는 다음 매개변수와 함께 호출됩니다:

- `YOUR-APP-IDENTIFIER-API-KEY` – Braze 대시보드에서 확인할 수 있는 [앱 식별자]({{site.baseurl}}/api/identifier_types#app-identifier) API 키입니다.
- `application` – 현재 앱입니다.
- `launchOptions` – `application:didFinishLaunchingWithOptions:`에서 가져오는 `NSDictionary` 옵션입니다.
- `appboyOptions` – Braze의 시작 구성 값이 포함된 선택적 `NSDictionary`입니다.

Braze 시작 키 목록은 [Appboy.h](https://github.com/braze-inc/braze-ios-sdk/blob/master/AppboyKit/include/Appboy.h)를 참조하세요.

## Appboy.sharedInstance()와 Swift 널 가능성 {#appboysharedinstance-and-swift-nullability}
일반적인 관행과 다소 다르게, `Appboy.sharedInstance()` 싱글턴은 옵셔널입니다. 이는 `startWithApiKey:`가 호출되기 전에는 `sharedInstance`가 `nil`이며, 지연 초기화를 사용할 수 있는 비표준이지만 유효한 구현이 존재하기 때문입니다.

`didFinishLaunchingWithOptions:` 델리게이트에서 Appboy의 `sharedInstance`에 접근하기 전에 `startWithApiKey:`를 호출하면(표준 구현), `Appboy.sharedInstance()?.changeUser("testUser")`와 같이 옵셔널 체이닝을 사용하여 번거로운 검사를 피할 수 있습니다. 이는 널이 아닌 `sharedInstance`를 가정한 Objective-C 구현과 동일한 동작을 합니다.

## 추가 리소스 {#additional-resources}

SDK 메서드에 대한 추가 안내를 제공하는 전체 [iOS 클래스 설명서](http://appboy.github.io/appboy-ios-sdk/docs/annotated.html)를 이용할 수 있습니다.