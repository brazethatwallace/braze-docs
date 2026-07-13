## Swift SDK 통합 {#integrating-the-swift-sdk}

스위프트 패키지 매니저(SPM), CocoaPods 또는 수동 통합 방법을 사용하여 Braze Swift SDK를 통합하고 커스터마이즈할 수 있습니다. 다양한 SDK 심볼에 대한 자세한 정보는 [Braze Swift 참조 설명서](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/)를 참조하세요.

### 필수 조건 {#prerequisites}

시작하기 전에 [최신 Braze Swift SDK 버전](https://github.com/braze-inc/braze-swift-sdk#version-information)에서 지원하는 환경인지 확인하세요.

### 1단계: Braze Swift SDK 설치 {#step-1-install-the-braze-swift-sdk}

Braze Swift SDK를 설치하려면 [스위프트 패키지 매니저(SwiftPM)](https://swift.org/package-manager/) 또는 [CocoaPods](http://cocoapods.org/)를 사용하는 것을 권장합니다. 또는 SDK를 수동으로 설치할 수도 있습니다.

{% tabs local %}
{% tab Swift Package Manager %}
#### 1.1단계: SDK 버전 가져오기 {#step-11-import-sdk-version}

프로젝트를 열고 프로젝트 설정으로 이동합니다. **Swift Packages** 탭을 선택하고 패키지 목록 아래에 있는 <i class="fas fa-plus"></i> 추가 버튼을 클릭합니다.

![Swift Packages 탭과 패키지 추가 버튼이 있는 Xcode 프로젝트 설정.]({% image_buster /assets/img/swiftpackages.png %})

{% alert note %}
버전 7.4.0부터 Braze Swift SDK는 [정적 XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static) 및 [동적 XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic)와 같은 추가 배포 채널을 제공합니다. 이러한 형식 중 하나를 사용하려면 해당 리포지토리의 설치 지침을 따르세요.
{% endalert %}

텍스트 필드에 iOS Swift SDK 리포지토리 URL `https://github.com/braze-inc/braze-swift-sdk`를 입력합니다. **Dependency Rule** 섹션에서 SDK 버전을 선택합니다. 마지막으로 **Add Package**를 클릭합니다.

![Braze Swift SDK 리포지토리 URL이 입력된 Xcode 패키지 추가 대화 상자.]({% image_buster /assets/img/importsdk_example.png %})

#### 1.2단계: 패키지 선택 {#step-12-select-your-packages}

Braze Swift SDK는 기능을 독립형 라이브러리로 분리하여 개발자가 프로젝트에 가져올 기능을 더 세밀하게 제어할 수 있도록 합니다.

| 패키지 | 세부 정보 |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `BrazeKit`      | 분석 및 푸시 알림을 지원하는 기본 SDK 라이브러리입니다. |
| `BrazeLocation` | 위치 분석 및 지오펜스 모니터링을 지원하는 위치 라이브러리입니다. |
| `BrazeUI`       | 인앱 메시지, Content Cards 및 배너를 위한 Braze 제공 사용자 인터페이스 라이브러리입니다. 기본 UI 구성요소를 사용하려면 이 라이브러리를 가져오세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="1.2단계: 패키지 선택" }

{: .ws-td-nw-1}

##### 확장 라이브러리 정보 {#about-extension-libraries}

{% alert warning %}
[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) 및 [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories)는 추가 기능을 제공하는 확장 모듈이므로 기본 애플리케이션 타겟에 직접 추가해서는 안 됩니다. 대신 링크된 가이드에 따라 각각의 타겟 확장에 개별적으로 통합하세요.
{% endalert %}

| 패키지 | 세부 정보 |
| -------------------------- | ------------------------------------------------------------------------------------- |
| `BrazeNotificationService` | 리치 푸시 알림을 지원하는 알림 서비스 확장 라이브러리입니다. |
| `BrazePushStory`           | Push Stories를 지원하는 알림 콘텐츠 확장 라이브러리입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="확장 라이브러리 정보" }

{: .ws-td-nw-1}

필요에 가장 적합한 패키지를 선택하고 **Add Package**를 클릭합니다. 최소한 `BrazeKit`를 선택해야 합니다.

![패키지 추가 전 BrazeKit이 선택된 Xcode 패키지 제품 목록.]({% image_buster /assets/img/add_package.png %})
{% endtab %}

{% tab CocoaPods %}
#### 1.1단계: CocoaPods 설치 {#step-11-install-cocoapods}

전체 안내는 CocoaPods의 [시작하기 가이드](https://guides.cocoapods.org/using/getting-started.html)를 참조하세요. 빠르게 시작하려면 다음 명령을 실행할 수 있습니다:

```bash
$ sudo gem install cocoapods
```

문제가 발생하면 CocoaPods의 [문제 해결 가이드](http://guides.cocoapods.org/using/troubleshooting.html)를 확인하세요.

#### 1.2단계: Podfile 구성 {#step-12-constructing-the-podfile}

다음으로, Xcode 프로젝트 디렉토리에 `Podfile`이라는 파일을 생성합니다.

{% alert note %}
버전 7.4.0부터 Braze Swift SDK는 [정적 XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static) 및 [동적 XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic)와 같은 추가 배포 채널을 제공합니다. 이러한 형식 중 하나를 사용하려면 해당 리포지토리의 설치 지침을 따르세요.
{% endalert %}

Podfile에 다음 줄을 추가합니다:

```
target 'YourAppTarget' do
  pod 'BrazeKit'
end
```

`BrazeKit`에는 분석 및 푸시 알림을 지원하는 기본 SDK 라이브러리가 포함되어 있습니다.

Pod 업데이트가 마이너 버전 업데이트보다 작은 변경 사항을 자동으로 가져오도록 Braze 버전을 지정하는 것을 권장합니다. `pod 'BrazeKit' ~> Major.Minor.Build`와 같은 형태입니다. 주요 변경 사항이 있더라도 최신 Braze SDK 버전을 자동으로 통합하려면 Podfile에서 `pod 'BrazeKit'`를 사용하면 됩니다.

##### 추가 라이브러리 정보 {#about-additional-libraries}

Braze Swift SDK는 기능을 독립형 라이브러리로 분리하여 개발자가 프로젝트에 가져올 기능을 더 세밀하게 제어할 수 있도록 합니다. `BrazeKit` 외에도 다음 라이브러리를 Podfile에 추가할 수 있습니다:

| 라이브러리 | 세부 정보 |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pod 'BrazeLocation'` | 위치 분석 및 지오펜스 모니터링을 지원하는 위치 라이브러리입니다. |
| `pod 'BrazeUI'`       | 인앱 메시지, Content Cards 및 배너를 위한 Braze 제공 사용자 인터페이스 라이브러리입니다. 기본 UI 구성요소를 사용하려면 이 라이브러리를 가져오세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="추가 라이브러리 정보" }

{: .ws-td-nw-1}

###### 확장 라이브러리 {#extension-libraries}

[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) 및 [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories)는 추가 기능을 제공하는 확장 모듈이며, 메인 애플리케이션 타겟에 직접 추가해서는 안 됩니다. 대신 이러한 모듈 각각에 대해 별도의 확장 타겟을 생성하고 해당 타겟으로 Braze 모듈을 가져와야 합니다.

| 라이브러리 | 세부 정보 |
| -------------------------------- | ------------------------------------------------------------------------------------- |
| `pod 'BrazeNotificationService'` | 리치 푸시 알림을 지원하는 알림 서비스 확장 라이브러리입니다. |
| `pod 'BrazePushStory'`           | Push Stories를 지원하는 알림 콘텐츠 확장 라이브러리입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="확장 라이브러리" }

{: .ws-td-nw-1}

#### 1.3단계: SDK 설치 {#step-13-install-the-sdk}

Braze SDK CocoaPod을 설치하려면 터미널에서 Xcode 앱 프로젝트 디렉토리로 이동한 후 다음 명령을 실행합니다:
```
pod install
```

이제 CocoaPods에서 생성한 새 Xcode 프로젝트 워크스페이스를 열 수 있어야 합니다. Xcode 프로젝트 대신 이 Xcode 워크스페이스를 사용해야 합니다.

![새 `BrazeExample.workspace`를 보여주도록 확장된 Braze 예제 폴더.]({% image_buster /assets/img/braze_example_workspace.png %})

#### CocoaPods를 사용하여 SDK 업데이트 {#updating-the-sdk-using-cocoapods}

CocoaPod을 업데이트하려면 프로젝트 디렉토리에서 다음 명령을 실행하면 됩니다:

```
pod update
```
{% endtab %}

{% tab Manual %}
#### 1.1단계: Braze SDK 다운로드 {#step-11-download-the-braze-sdk}

[GitHub의 Braze SDK 릴리스 페이지](https://github.com/braze-inc/braze-swift-sdk/releases)로 이동한 다음 `braze-swift-sdk-prebuilt.zip`을 다운로드합니다.

![GitHub의 Braze SDK 릴리스 페이지.]({% image_buster /assets/img/swift/sdk_integration/download-braze-swift-sdk-prebuilt.png %})

#### 1.2단계: 프레임워크 선택 {#step-12-choose-your-frameworks}

Braze Swift SDK에는 다양한 독립형 XCFrameworks가 포함되어 있어 모든 기능을 통합할 필요 없이 원하는 기능을 자유롭게 통합할 수 있습니다. 다음 표를 참조하여 XCFrameworks를 선택하세요:

| 패키지 | 필수 여부 | 설명 |
| -------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `BrazeKit`                 | 예       | 분석 및 푸시 알림을 지원하는 기본 SDK 라이브러리입니다. |
| `BrazeLocation`            | 아니요        | 위치 분석 및 지오펜스 모니터링을 지원하는 위치 라이브러리입니다. |
| `BrazeUI`                  | 아니요        | 인앱 메시지, Content Cards 및 배너를 위한 Braze 제공 사용자 인터페이스 라이브러리입니다. 기본 UI 구성요소를 사용하려면 이 라이브러리를 가져오세요. |
| `BrazeNotificationService` | 아니요        | 리치 푸시 알림을 지원하는 알림 서비스 확장 라이브러리입니다. 이 라이브러리를 기본 애플리케이션 타겟에 직접 추가하지 말고 [`BrazeNotificationService` 라이브러리를 별도로 추가](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications)하세요. |
| `BrazePushStory`           | 아니요        | Push Stories를 지원하는 알림 콘텐츠 확장 라이브러리입니다. 이 라이브러리를 기본 애플리케이션 타겟에 직접 추가하지 말고 [`BrazePushStory` 라이브러리를 별도로 추가](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories)하세요. |
| `BrazeKitCompat`           | 아니요        | `Appboy-iOS-SDK` 버전 4.X.X에서 사용 가능했던 모든 `Appboy` 및 `ABK*` 클래스와 메서드가 포함된 호환성 라이브러리입니다. 사용법에 대한 자세한 내용은 [마이그레이션 가이드](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/)의 최소 마이그레이션 시나리오를 참조하세요. |
| `BrazeUICompat`            | 아니요        | `Appboy-iOS-SDK` 버전 4.X.X의 `AppboyUI` 라이브러리에서 사용 가능했던 모든 `ABK*` 클래스와 메서드가 포함된 호환성 라이브러리입니다. 사용법에 대한 자세한 내용은 [마이그레이션 가이드](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/)의 최소 마이그레이션 시나리오를 참조하세요. |
| `SDWebImage`               | 아니요        | 최소 마이그레이션 시나리오에서 `BrazeUICompat`에서만 사용하는 종속성입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="1.2단계: 프레임워크 선택" }

{: .ws-td-nw-1 .reset-td-br-1 .reset-td-br-2 aria-label="1.2단계: 프레임워크 선택" }

#### 1.3단계: 파일 준비 {#step-13-prepare-your-files}

**정적** 또는 **동적** XCFrameworks 중 어떤 것을 사용할지 결정한 다음 파일을 준비합니다:

1. XCFrameworks를 위한 임시 디렉토리를 생성합니다.
2. `braze-swift-sdk-prebuilt`에서 `dynamic` 디렉토리를 열고 `BrazeKit.xcframework`를 디렉토리로 이동합니다. 디렉토리는 다음과 비슷해야 합니다:
    ```bash
    temp_dir
    └── BrazeKit.xcframework
    ```
3. [선택한 XCFrameworks](#swift_step-2-choose-your-frameworks) 각각을 임시 디렉토리로 이동합니다. 디렉토리는 다음과 비슷해야 합니다:
    ```bash
    temp_dir
    ├── BrazeKit.xcframework
    ├── BrazeKitCompat.xcframework
    ├── BrazeLocation.xcframework
    └── SDWebImage.xcframework
    ```

#### 1.4단계: 프레임워크 통합 {#step-14-integrate-your-frameworks}

다음으로, [이전에 준비한](#swift_step-3-prepare-your-files) **동적** 또는 **정적** XCFrameworks를 통합합니다:

Xcode 프로젝트에서 빌드 타겟을 선택한 다음 **General**을 선택합니다. **Frameworks, Libraries, and Embedded Content**에서 [이전에 준비한 파일](#swift_step-3-prepare-your-files)을 드래그 앤 드롭합니다.

![각 Braze 라이브러리가 'Embed & Sign'으로 설정된 예제 Xcode 프로젝트.]({% image_buster /assets/img/swift/sdk_integration/embed-and-sign.png %})

{% alert note %}
Swift SDK 12.0.0부터는 정적 및 동적 배리언트 모두에 대해 Braze XCFrameworks에 항상 **Embed & Sign**을 선택해야 합니다. 이렇게 하면 프레임워크 리소스가 앱 번들에 올바르게 포함됩니다.
{% endalert %}

{% alert tip %}
GIF 지원을 활성화하려면 `braze-swift-sdk-prebuilt/static` 또는 `braze-swift-sdk-prebuilt/dynamic`에 있는 `SDWebImage.xcframework`를 추가하세요.
{% endalert %}

#### Objective-C 프로젝트의 일반적인 오류 {#common-errors-for-objective-c-projects}

Xcode 프로젝트에 Objective-C 파일만 포함된 경우 프로젝트를 빌드하려고 할 때 "missing symbol" 오류가 발생할 수 있습니다. 이러한 오류를 해결하려면 프로젝트를 열고 파일 트리에 빈 Swift 파일을 추가합니다. 이렇게 하면 빌드 툴체인이 [Swift Runtime](https://support.apple.com/kb/dl1998)을 임베드하고 빌드 시 적절한 프레임워크에 링크하도록 강제합니다.

```bash
FILE_NAME.swift
```

`FILE_NAME`을 공백이 없는 문자열로 바꿉니다. 파일은 다음과 비슷하게 보일 것입니다:

```bash
empty_swift_file.swift
```
{% endtab %}
{% endtabs local %}

### 2단계: 지연 초기화 설정(선택 사항) {#step-2-set-up-delayed-initialization-optional}

Braze Swift SDK의 초기화를 지연할 수 있습니다. 이는 앱이 구성을 로드하거나 SDK를 시작하기 전에 사용자 동의를 기다려야 할 때 유용합니다. 지연 초기화는 SDK 초기화 전에 수신된 Braze 푸시 알림과 푸시 토큰이 대기줄에 추가되고 SDK가 초기화되면 처리되도록 보장합니다.

지연 초기화를 사용하려면 최소 Braze SDK 버전이 필요합니다:
{% sdk_min_versions swift:11.2.0 %}

#### 2.1단계: 지연 초기화 준비 {#step-21-prepare-for-delayed-initialization}

앱의 생명 주기에서 가능한 한 빨리, 이상적으로는 `application(_:didFinishLaunchingWithOptions:)` 내부 또는 그 이전에 `Braze.prepareForDelayedInitialization()`을 호출하세요. 이렇게 하면 SDK가 초기화되기 전에 수신된 푸시 알림이 올바르게 캡처되고 나중에 처리됩니다.

{% alert note %}
이것은 Braze의 푸시 알림에만 적용됩니다. 다른 푸시 알림은 시스템 델리게이트에 의해 정상적으로 처리됩니다.
{% endalert %}

{% tabs %}
{% tab Swift %}
{% subtabs local %}
{% subtab UIKit %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
  // Prepare the SDK for delayed initialization
  Braze.prepareForDelayedInitialization()

  // ... Additional non-Braze setup code

  return true
}
```
{% endsubtab %}

{% subtab SwiftUI %}
```swift
@main
struct MyApp: App {
  @UIApplicationDelegateAdaptor var appDelegate: AppDelegate

  var body: some Scene {
    WindowGroup {
      ContentView()
    }
  }
}

class AppDelegate: NSObject, UIApplicationDelegate {
  func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {
    // Prepare the SDK for delayed initialization
    Braze.prepareForDelayedInitialization()

    // ... Additional non-Braze setup code

    return true
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Objective-C %}
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Prepare the SDK for delayed initialization
  [Braze prepareForDelayedInitialization];

  // ... Additional non-Braze setup code

  return YES;
}
```
{% endtab %}
{% endtabs %}

지연 초기화를 사용할 때 푸시 알림 자동화가 암묵적으로 활성화됩니다. `pushAutomation` 매개변수를 전달하여 [푸시 자동화를 커스터마이즈](#swift_step-23-customize-push-automation-optional)할 수 있습니다.

#### 2.2단계: 푸시 분석 동작 구성(선택 사항) {#step-22-configure-push-analytics-behavior-optional}

지연 초기화가 활성화되면 푸시 분석이 기본적으로 대기줄에 추가됩니다. 그러나 푸시 분석을 명시적으로 대기줄에 추가하거나 삭제할 수도 있습니다.

##### 명시적으로 대기줄에 추가 {#explicitly-queue}

푸시 분석을 명시적으로 대기줄에 추가하려면(기본 동작) `.queue`를 `analyticsBehavior` 매개변수에 전달합니다. 초기화 전에 대기줄에 추가된 푸시 분석 이벤트는 초기화 시 처리되어 서버로 전송됩니다.

{% tabs local %}
{% tab Swift %}
```swift
Braze.prepareForDelayedInitialization(analyticsBehavior: .queue)
```
{% endtab %}
{% tab Objective-C %}
```objc
[Braze prepareForDelayedInitializationWithAnalyticsBehavior:BRZPushEnqueueBehaviorQueue];
```
{% endtab %}
{% endtabs %}

##### 삭제 {#drop}

SDK 초기화 전에 수신된 푸시 분석을 삭제하려면 `.drop`을 `analyticsBehavior` 매개변수에 전달합니다. 이 옵션을 사용하면 SDK가 초기화되지 않은 동안 발생하는 모든 푸시 분석 이벤트가 무시됩니다.

{% tabs local %}
{% tab Swift %}
```swift
Braze.prepareForDelayedInitialization(analyticsBehavior: .drop)
```
{% endtab %}
{% tab Objective-C %}
```objc
[Braze prepareForDelayedInitializationWithAnalyticsBehavior:BRZPushEnqueueBehaviorDrop];
```
{% endtab %}
{% endtabs %}

#### 2.3단계: 푸시 자동화 커스터마이즈(선택 사항) {#step-23-customize-push-automation-optional}

`pushAutomation` 매개변수를 전달하여 푸시 자동화 구성을 커스터마이즈할 수 있습니다. 기본적으로 `requestAuthorizationAtLaunch`를 제외한 모든 자동화 기능이 활성화되어 있습니다.

{% tabs local %}
{% tab SWIFT %}
```swift
// Enable all push automation
featuresBraze.prepareForDelayedInitialization(pushAutomation: true)

// Or customize specific automation options
let automation = Braze.Configuration.Push.Automation()
automation.automaticSetup = true
automation.requestAuthorizationAtLaunch = false
Braze.prepareForDelayedInitialization(pushAutomation: automation)
```
{% endtab %}

{% tab OBJECTIVE-C %}
```objc
// Enable all push automation features
[Braze prepareForDelayedInitializationWithPushAutomation:[[BRZConfigurationPushAutomation alloc] initWithAutomationEnabled:YES]];

// Or customize specific automation options
BRZConfigurationPushAutomation *automation = [[BRZConfigurationPushAutomation alloc] init];
automation.automaticSetup = YES;
automation.requestAuthorizationAtLaunch = NO;
[Braze prepareForDelayedInitializationWithPushAutomation:automation analyticsBehavior:BRZPushEnqueueBehaviorQueue];
```
{% endtab %}
{% endtabs %}

#### 2.4단계: SDK 초기화 {#step-24-initialize-the-sdk}

선택한 지연 기간(예: 서버에서 구성을 가져온 후 또는 사용자 동의 후) 후에 SDK를 정상적으로 초기화합니다:

{% tabs local %}
{% tab SWIFT %}
```swift
func initializeBraze() {
  let configuration = Braze.Configuration(apiKey: "YOUR-API-KEY", endpoint: "YOUR-ENDPOINT")

  // Enable push automation to match the delayed initialization configuration
  configuration.push.automation = true
  let braze = Braze(configuration: configuration)

  // Store the Braze instance for later use
  AppDelegate.braze = braze
}
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
- (void)initializeBraze {
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"YOUR-API-KEY" endpoint:@"YOUR-ENDPOINT"];

  // Enable push automation to match the delayed initialization configuration
  configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initWithAutomationEnabled:YES];
  Braze *braze = [[Braze alloc] initWithConfiguration:configuration];

  // Store the Braze instance for later use
  AppDelegate.braze = braze;
}
```
{% endtab %}
{% endtabs %}

{% alert note %}
SDK가 초기화되면 모든 대기 중인 푸시 알림, 푸시 토큰 및 딥링크가 자동으로 처리됩니다.
{% endalert %}

### 3단계: 앱 델리게이트 업데이트 {#step-3-update-your-app-delegate}

{% alert important %}
다음은 프로젝트에 `AppDelegate`를 이미 추가했다고 가정합니다(기본적으로 생성되지 않음). 또한 지연 초기화 기능을 사용하지 않는 경우입니다. `AppDelegate`를 사용할 계획이 없다면 앱 시작 시 가능한 한 빨리 Braze SDK를 초기화하세요. 지연 초기화 기능을 사용하는 경우 SDK 초기화에 대한 [2.4단계](#swift_step-24-initialize-the-sdk)를 참조하고 이 단계는 건너뛰세요.
{% endalert %}

{% subtabs local %}
{% subtab swift %}
Braze Swift SDK에 포함된 기능을 가져오려면 `AppDelegate.swift` 파일에 다음 코드를 추가합니다:

```swift
import BrazeKit
```

다음으로, `AppDelegate` 클래스에 정적 속성을 추가하여 애플리케이션의 수명 동안 Braze 인스턴스에 대한 강한 참조를 유지합니다:

```swift
class AppDelegate: UIResponder, UIApplicationDelegate {
  static var braze: Braze? = nil
}
```

SDK는 애플리케이션이 사용 기간 동안 Braze 인스턴스에 대한 강한 참조를 유지하도록 요구합니다. 예기치 않은 부작용을 방지하려면 Braze 인스턴스의 속성이나 메서드에 접근하거나 수정하기 전에 해당 참조를 완전히 캡처했는지 확인하세요.

마지막으로, `AppDelegate.swift`에서 `application:didFinishLaunchingWithOptions:` 메서드에 다음 스니펫을 추가합니다:

```swift
let configuration = Braze.Configuration(
    apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
    endpoint: "YOUR-BRAZE-ENDPOINT"
)
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

`YOUR-APP-IDENTIFIER-API-KEY` 및 `YOUR-BRAZE-ENDPOINT`를 **앱 설정** 페이지의 올바른 값으로 업데이트하세요. 앱 식별자 API 키를 찾을 수 있는 위치에 대한 자세한 내용은 [API 식별자 유형]({{site.baseurl}}/api/identifier_types/?tab=app%20ids)을 참조하세요.

{% endsubtab %}
{% subtab OBJECTIVE-C %}

`AppDelegate.m` 파일에 다음 코드를 추가합니다:

```objc
@import BrazeKit;
```

다음으로, `AppDelegate.m` 파일에 정적 변수를 추가하여 애플리케이션의 수명 동안 Braze 인스턴스에 대한 참조를 유지합니다:

```objc
static Braze *_braze;

@implementation AppDelegate
+ (Braze *)braze {
  return _braze;
}

+ (void)setBraze:(Braze *)braze {
  _braze = braze;
}
@end
```

SDK는 애플리케이션이 사용 기간 동안 Braze 인스턴스에 대한 강한 참조를 유지하도록 요구합니다. 예기치 않은 부작용을 방지하려면 Braze 인스턴스의 속성이나 메서드에 접근하거나 수정하기 전에 해당 참조를 완전히 캡처했는지 확인하세요.

마지막으로, `AppDelegate.m` 파일 내의 `application:didFinishLaunchingWithOptions:` 메서드에 다음 스니펫을 추가합니다:

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:"YOUR-APP-IDENTIFIER-API-KEY"
                                                                  endpoint:"YOUR-BRAZE-ENDPOINT"];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

`YOUR-APP-IDENTIFIER-API-KEY` 및 `YOUR-BRAZE-ENDPOINT`를 **설정 관리** 페이지의 올바른 값으로 업데이트하세요. 앱 식별자 API 키를 찾을 수 있는 위치에 대한 자세한 내용은 [API 설명서]({{site.baseurl}}/api/api_key#the-app-identifier-api-key)를 참조하세요.

{% endsubtab %}
{% endsubtabs local %}

{% alert note %}
`Braze.init`은 호출 스레드에서 즉시 반환됩니다. SDK는 내부 대기줄에서 시작 작업을 처리합니다. 메인 스레드에서 `init` 직후 `braze.deviceId`와 같은 동기 속성을 읽으면 SDK가 초기화 후 작업을 완료할 때까지 호출 스레드가 차단됩니다. 메인 스레드 또는 지연에 민감한 컨텍스트에서는 차단 없이 값을 읽으려면 `braze.getDeviceId(_:)` (Swift) 또는 `[braze getDeviceIdWithCompletion:^(NSString *deviceId) { ... }]` (Objective-C)를 사용하세요.
{% endalert %}

## 선택적 구성 {#optional-configurations}

### 로깅 {#logging}

모든 플랫폼에서 중앙 집중식 개요를 보려면 [상세 로깅]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)을 참조하세요. 로그 출력을 해석하는 방법을 알아보려면 [상세 로그 읽기]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs)를 참조하세요.

#### 로그 레벨 {#log-levels}

Braze Swift SDK의 기본 로그 레벨은 `.error`이며&#8212;로그가 활성화될 때 최소 지원 레벨이기도 합니다. 다음은 전체 로그 레벨 목록입니다:

| Swift       | Objective-C              | 설명                                                  |
| ----------- | ------------------------ | ------------------------------------------------------------ |
| `.debug`    | `BRZLoggerLevelDebug`    | 디버깅 정보 + `.info` + `.error`를 기록합니다.              |
| `.info`     | `BRZLoggerLevelInfo`     | 일반 SDK 정보(사용자 변경 사항 등) + `.error`를 기록합니다. |
| `.error`    | `BRZLoggerLevelError`    | 오류를 기록합니다.                                                  |
| `.disabled` | `BRZLoggerLevelDisabled` | 로깅이 발생하지 않습니다.                                           |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="로그 레벨" }

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="로그 레벨" }

#### 로그 레벨 설정 {#setting-the-log-level}

런타임에 `Braze.Configuration` 오브젝트에서 로그 레벨을 할당할 수 있습니다. 자세한 사용법은 [`Braze.Configuration.Logger`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/logger-swift.class)를 참조하세요.

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
// Enable logging of general SDK information (such as user changes, etc.)
configuration.logger.level = .info
let braze = Braze(configuration: configuration)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:self.APIKey
                                                                  endpoint:self.apiEndpoint];
// Enable logging of general SDK information (such as user changes, etc.)
[configuration.logger setLevel:BRZLoggerLevelInfo];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
```

{% endtab %}
{% endtabs %}