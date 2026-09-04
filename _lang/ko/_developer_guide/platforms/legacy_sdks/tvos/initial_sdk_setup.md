---
nav_title: 초기 SDK 설정
article_title: tvOS용 초기 SDK 설정
platform: tvOS
page_order: 0
page_type: reference
description: "이 페이지에서는 tvOS Braze SDK의 초기 설정 단계를 다룹니다."
search_rank: 1
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 초기 SDK 설정 {#initial-sdk-setup}

> 이 참조 문서에서는 tvOS용 Braze SDK를 설치하는 방법을 설명합니다. Braze SDK를 설치하면 기본적인 분석 기능을 사용할 수 있습니다.

{% alert note %}
현재 tvOS SDK는 분석 기능을 지원합니다. 대시보드에 tvOS 앱을 추가하려면 [지원 티켓]({{site.baseurl}}/user_guide/administer/personal/braze_support)을 여세요.
{% endalert %}

tvOS Braze SDK는 Objective-C 및 Swift 프로젝트의 종속성 매니저인 [CocoaPods](http://cocoapods.org/)를 사용하여 설치하거나 업데이트해야 합니다. CocoaPods를 사용하면 통합과 업데이트가 더욱 간편해집니다.

## tvOS SDK CocoaPods 통합 {#tvos-sdk-cocoapods-integration}

### 1단계: CocoaPods 설치 {#step-1-install-cocoapods}

tvOS [CocoaPods](http://cocoapods.org/)를 통해 SDK를 설치하면 대부분의 설치 과정이 자동화됩니다. 이 프로세스를 시작하기 전에 [Ruby 버전 2.0.0](https://www.ruby-lang.org/en/installation/) 이상을 사용하고 있는지 확인하세요.

시작하려면 다음 명령을 실행합니다:

```bash
$ sudo gem install cocoapods
```

- `rake` 실행 파일을 덮어쓸 것인지 묻는 메시지가 나타나면, CocoaPods.org의 [시작하기](http://guides.cocoapods.org/using/getting-started.html)를 참조하세요.
- CocoaPods와 관련된 문제가 있는 경우, [CocoaPods 문제 해결 가이드](http://guides.cocoapods.org/using/troubleshooting.html)를 참조하세요.

### 2단계: Podfile 구성 {#step-2-constructing-the-podfile}

CocoaPods Ruby Gem을 설치했으므로 이제 Xcode 프로젝트 디렉토리에 `Podfile`이라는 파일을 생성해야 합니다.

Podfile에 다음 줄을 추가합니다:

```
target 'YourAppTarget' do
  pod 'Appboy-tvOS-SDK'
end
```

Braze에 버전을 지정하여 pod 업데이트 시 마이너 버전 업데이트 미만의 변경 사항을 자동으로 가져오도록 하는 것이 좋습니다. `pod 'Appboy-tvOS-SDK' ~> Major.Minor.Build`와 같이 작성하면 됩니다. 메이저 변경 사항을 포함하여 최신 Braze SDK 버전을 자동으로 통합하려면, Podfile에서 `pod 'Appboy-tvOS-SDK'`를 사용할 수 있습니다.

### 3단계: Braze SDK 설치 {#step-3-installing-the-braze-sdk}

Braze SDK CocoaPods를 설치하려면, 터미널에서 Xcode 앱 프로젝트의 디렉토리로 이동한 후 다음 명령을 실행합니다:
```
pod install
```

이 시점에서 CocoaPods가 생성한 새로운 Xcode 프로젝트 워크스페이스를 열 수 있어야 합니다. Xcode 프로젝트 대신 이 Xcode 워크스페이스를 사용하세요.

![CocoaPods가 생성한 새로운 Xcode 프로젝트 워크스페이스를 열 수 있어야 합니다. Xcode 프로젝트 대신 이 Xcode 워크스페이스를 사용하세요.]({% image_buster /assets/img_archive/podsworkspace.png %})

### 4단계: 앱 델리게이트 업데이트 {#step-4-updating-your-app-delegate}

{% tabs %}
{% tab OBJECTIVE-C %}

`AppDelegate.m` 파일에 다음 코드 줄을 추가합니다:

```objc
#import <AppboyTVOSKit/AppboyKit.h>
```

`AppDelegate.m` 파일의 `application:didFinishLaunchingWithOptions` 메서드 내에 다음 스니펫을 추가합니다:

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
         inApplication:application
     withLaunchOptions:launchOptions];
```

마지막으로, `YOUR-API-KEY`를 **설정 관리** 페이지의 올바른 값으로 업데이트합니다.

{% endtab %}
{% tab swift %}

Braze SDK를 CocoaPods 또는 Carthage로 통합하는 경우, `AppDelegate.swift` 파일에 다음 코드 줄을 추가합니다:

```swift
import AppboyTVOSKit
```

Swift 프로젝트에서 Objective-C 코드를 사용하는 방법에 대한 자세한 내용은 [Apple 개발자 문서](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html)를 참조하세요.

`AppDelegate.swift`에서 `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` 내에 다음 스니펫을 추가합니다:

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions)
```

다음으로, `YOUR-API-KEY`를 **설정 관리** 페이지의 올바른 값으로 업데이트합니다.

`sharedInstance` 싱글톤은 `startWithApiKey:`가 호출되기 전에는 nil이 됩니다. 이는 Braze 기능을 사용하기 위한 전제 조건입니다.

{% endtab %}
{% endtabs %}

{% alert warning %}
애플리케이션의 메인 스레드에서 Braze를 초기화해야 합니다. 비동기적으로 초기화하면 기능이 손상될 수 있습니다.
{% endalert %}

### 5단계: 커스텀 엔드포인트 또는 데이터 클러스터 지정 {#step-5-specify-your-custom-endpoint-or-data-cluster}

{% alert note %}
2019년 12월부터 커스텀 엔드포인트는 더 이상 제공되지 않습니다. 기존 커스텀 엔드포인트가 있는 경우 계속 사용할 수 있습니다. 자세한 내용은 <a href="{{site.baseurl}}/api/basics#endpoints">사용 가능한 엔드포인트 목록</a> 을 참조하세요.
{% endalert %}

Braze 담당자가 이미 [올바른 엔드포인트]({{ site.baseurl }}/user_guide/administrative/access_braze/sdk_endpoints/)를 안내했을 것입니다.

#### 컴파일 시 엔드포인트 구성(권장) {#compile-time-endpoint-configuration-recommended}
기존 커스텀 엔드포인트가 제공된 경우:
- Braze iOS SDK v3.0.2부터 `Info.plist` 파일을 사용하여 커스텀 엔드포인트를 설정할 수 있습니다. Info.plist 파일에 `Appboy` 사전을 추가합니다. `Appboy` 사전 내에 `Endpoint` 문자열 하위 항목을 추가하고, 값을 커스텀 엔드포인트 URL의 권한 부분으로 설정합니다(예: `https://sdk.iad-01.braze.com`이 아닌 `sdk.iad-01.braze.com`).

#### 런타임 엔드포인트 구성 {#runtime-endpoint-configuration}
기존 커스텀 엔드포인트가 제공된 경우:
- Braze iOS SDK v3.17.0+부터 `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`에 전달되는 `appboyOptions` 매개변수 내의 `ABKEndpointKey`를 통해 엔드포인트를 재정의할 수 있습니다. 값을 커스텀 엔드포인트 URL의 권한 부분으로 설정합니다(예: `https://sdk.iad-01.braze.com`이 아닌 `sdk.iad-01.braze.com`).

{% alert note %}
Braze iOS SDK v3.17.0에서 `ABKAppboyEndpointDelegate`를 사용한 런타임 엔드포인트 설정 지원이 제거되었습니다. 이미 `ABKAppboyEndpointDelegate`를 사용하고 있다면, Braze iOS SDK 버전 v3.14.1~v3.16.0에서 `getApiEndpoint()` 메서드의 `dev.appboy.com`에 대한 모든 참조를 `sdk.iad-01.braze.com`에 대한 참조로 교체해야 합니다.
{% endalert %}

### SDK 통합 완료 {#sdk-integration-complete}

이제 Braze가 애플리케이션에서 데이터를 수집하고 있으며, 기본 통합이 완료되었습니다. tvOS 앱과 기타 서드파티 라이브러리를 컴파일할 때 Bitcode를 활성화해야 합니다.

### CocoaPods를 통한 Braze SDK 업데이트 {#updating-the-braze-sdk-via-cocoapods}

CocoaPod를 업데이트하려면 프로젝트 디렉토리 내에서 다음 명령을 실행하면 됩니다:

```
pod update
```

## 시작 시 Braze 커스터마이즈하기 {#customizing-braze-on-startup}

시작 시 Braze를 커스터마이즈하려면 Braze 초기화 메서드 `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`를 사용하고 Braze 시작 키의 선택적 `NSDictionary`를 전달할 수 있습니다.
{% tabs %}
{% tab OBJECTIVE-C %}

`AppDelegate.m` 파일의 `application:didFinishLaunchingWithOptions` 메서드 내에 다음 Braze 메서드를 추가합니다:

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endtab %}
{% tab swift %}

`AppDelegate.swift`의 `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` 메서드 내에 다음 Braze 메서드를 추가합니다:

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:appboyOptions)
```

여기서 `appboyOptions`는 시작 구성 값의 `Dictionary`입니다.

{% endtab %}
{% endtabs %}

이 메서드는 `startWithApiKey:inApplication:withLaunchOptions:` 초기화 메서드를 대체하며, 다음 매개변수를 사용하여 호출됩니다:

- `YOUR-API-KEY`: 애플리케이션의 API 키는 Braze 대시보드의 **설정 관리**에서 확인할 수 있습니다.
- `application`: 현재 앱입니다.
- `launchOptions`: `application:didFinishLaunchingWithOptions:`에서 가져오는 옵션 `NSDictionary`입니다.
- `appboyOptions`: Braze의 시작 구성 값이 포함된 선택적 `NSDictionary`입니다.

Braze 시작 키 목록은 [Appboy.h](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h)를 참조하세요.

## Appboy.sharedInstance()와 Swift 널 가능성 {#appboysharedinstance-and-swift-nullability}
일반적인 관행과 다소 다르게, `Appboy.sharedInstance()` 싱글턴은 옵셔널입니다. 이는 `startWithApiKey:`가 호출되기 전에 `sharedInstance`가 `nil`이기 때문이며, 지연 초기화를 사용할 수 있는 비표준이지만 유효한 구현이 존재하기 때문입니다.

`didFinishLaunchingWithOptions:` 델리게이트에서 Appboy의 `sharedInstance`에 접근하기 전에 `startWithApiKey:`를 호출하는 경우(표준 구현), `Appboy.sharedInstance()?.changeUser("testUser")`와 같은 옵셔널 체이닝을 사용하여 번거로운 검사를 피할 수 있습니다. 이는 널이 아닌 `sharedInstance`를 가정하는 Objective-C 구현과 동일한 동작을 합니다.

## 수동 통합 옵션 {#manual-integration-options}

tvOS SDK를 수동으로 통합할 수도 있습니다. [공개 리포지토리](https://github.com/appboy/appboy-ios-sdk)에서 프레임워크를 가져온 후 앞의 섹션에 설명된 대로 Braze를 초기화하면 됩니다.

## 사용자 식별 및 분석 보고 {#identifying-users-and-reporting-analytics}
사용자 ID 설정, 커스텀 이벤트 로깅, 사용자 속성 설정에 대한 정보는 [iOS 설명서]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=swift)를 참조하세요. 또한 [이벤트 명명 규칙]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions)을 숙지하는 것을 권장합니다.