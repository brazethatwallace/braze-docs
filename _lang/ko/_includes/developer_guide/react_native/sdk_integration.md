## React Native Braze SDK 소개 {#about-the-react-native-braze-sdk}

React Native Braze SDK를 통합하면 기본 분석 기능을 제공하고 iOS 및 Android 모두에 대해 하나의 코드베이스로 인앱 메시지 및 Content Cards를 통합할 수 있습니다.

## 새 아키텍처 호환성 {#new-architecture-compatibility}

다음 최소 SDK 버전은 [React Native의 새 아키텍처](https://reactnative.dev/docs/the-new-architecture/landing-page)를 사용하는 모든 앱과 호환됩니다:

{% sdk_min_versions reactnative:2.0.1 %}

SDK 버전 6.0.0부터 Braze는 React Native Turbo 모듈을 사용하며, 이는 새 아키텍처와 레거시 브리지 아키텍처 모두와 호환됩니다. 즉, 추가 설정이 필요하지 않습니다.

{% alert warning %}
iOS 앱이 `RCTAppDelegate`를 준수하고 이전 `AppDelegate` 설정을 따르는 경우, Turbo 모듈에서 이벤트를 구독할 때 발생할 수 있는 충돌을 방지하기 위해 [완전한 네이티브 설정](#reactnative_step-2-complete-native-setup)의 샘플을 검토하세요.
{% endalert %}

## React 및 React Native 버전 요구 사항 {#react-and-react-native-version-requirements}

Braze는 React Native SDK가 지원하는 것 이상의 별도 최소 React 버전을 게시하지 않습니다. SDK를 통합하려면 React Native 버전 0.71 이상을 사용하세요. 지원되는 React Native 버전의 전체 목록은 [React Native SDK GitHub 리포지토리](https://github.com/braze-inc/braze-react-native-sdk?tab=readme-ov-file#version-support)를 참조하세요.

React, React Native 또는 Braze SDK를 업그레이드할 때는 배포 전에 SDK [체인지로그](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)에서 호환성을 깨뜨리는 변경 사항을 검토하세요.

## React Native SDK 통합하기 {#integrating-the-react-native-sdk}

### 필수 조건 {#prerequisites}

지원되는 React Native 버전 및 업그레이드 안내는 [React 및 React Native 버전 요구 사항](#react-and-react-native-version-requirements)을 참조하세요.

### 1단계: Braze 라이브러리 통합 {#step-1-integrate-the-braze-library}

{% tabs local %}
{% tab npm %}
```bash
npm install @braze/react-native-sdk
```
{% endtab %}
{% tab yarn %}
```bash
yarn add @braze/react-native-sdk
```
{% endtab %}
{% endtabs %}

<a id="step-2-choose-a-setup-option"></a>
<a id="reactnative_step-2-complete-native-setup"></a>
### 2단계: 네이티브 설정 완료 {#step-2-complete-native-setup}

앱이 Expo를 사용하는 경우 [Expo 플러그인 사용](#reactnative-using-the-expo-plugin)을 참조하세요. 앱이 순수 React Native를 사용하는 경우 [React Native CLI 사용](#reactnative-using-react-native-cli)을 참조하세요.
각 버전 탭에서 Expo 플러그인 또는 React Native CLI 중 하나의 설정 방법을 선택하세요.

{% tabs %}
{% tab React Native SDK 19.2.0+ %}

#### 방법 1: Expo 플러그인 사용 {#reactnative-using-the-expo-plugin}

##### 2.1 Braze Expo 플러그인 설치 {#21-install-the-braze-expo-plugin} {#21-install-the-braze-expo-plugin}

Braze Expo 플러그인 버전이 4.1.0 이상인지 확인하세요. 지원되는 버전의 전체 목록은 [Braze Expo 플러그인 리포지토리](https://github.com/braze-inc/braze-expo-plugin?tab=readme-ov-file#version-support)를 참조하세요.

다음 코드 스니펫은 Braze Expo 플러그인을 설치하는 명령어입니다:

```bash
npx expo install @braze/expo-plugin
```

##### 2.2 app.json에 플러그인 추가 {#22-add-the-plugin-to-your-appjson} {#22-add-the-plugin-to-your-appjson}

`app.json`에 Braze Expo 플러그인을 추가하세요. API 키와 엔드포인트는 더 이상 여기에서 설정하지 않습니다. JavaScript에서 `Braze.initialize()`를 통해 런타임에 제공하세요. 구현 요구 사항에 따라 다음 선택적 구성 매개변수를 추가하세요:

| 메서드 | 유형 | 설명 |
| --------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enableBrazeIosPush` | boolean | iOS 전용. iOS에서 푸시 알림을 처리하기 위해 Braze를 사용할지 여부. |
| `enableFirebaseCloudMessaging` | boolean | Android 전용. 푸시 알림에 Firebase Cloud Messaging을 사용할지 여부. |
| `firebaseCloudMessagingSenderId` | string | Android 전용. Firebase Cloud Messaging 발신자 ID. |
| `sessionTimeout` | integer | 애플리케이션의 Braze 세션 타임아웃(초). |
| `enableSdkAuthentication` | boolean | [SDK 인증](https://www.braze.com/docs/developer_guide/platform_wide/sdk_authentication#sdk-authentication) 기능을 활성화할지 여부. |
| `logLevel` | integer | 애플리케이션의 로그 레벨. 기본 로그 레벨은 8이며 최소한의 정보를 기록합니다. 디버깅을 위해 상세 로깅을 활성화하려면 로그 레벨 0을 사용하세요. |
| `minimumTriggerIntervalInSeconds` | integer | 트리거 사이의 최소 시간 간격(초). 기본값은 30초입니다. |
| `enableAutomaticLocationCollection` | boolean | 자동 위치 수집이 활성화되어 있는지 여부(사용자가 허용하는 경우). |
| `enableGeofence` | boolean | 지오펜스가 활성화되어 있는지 여부. |
| `enableAutomaticGeofenceRequests` | boolean | 지오펜스 요청이 자동으로 이루어져야 하는지 여부. |
| `dismissModalOnOutsideTap` | boolean | iOS 전용. 사용자가 인앱 메시지 외부를 클릭할 때 모달 인앱 메시지가 해제되는지 여부. |
| `androidHandlePushDeepLinksAutomatically` | boolean | Android 전용. Braze SDK가 푸시 딥링크를 자동으로 처리해야 하는지 여부. |
| `androidPushNotificationHtmlRenderingEnabled` | boolean | Android 전용. 푸시 알림의 텍스트 콘텐츠를 `android.text.Html.fromHtml`을 사용하여 HTML로 해석하고 렌더링할지 여부를 설정합니다. |
| `androidNotificationAccentColor` | string | Android 전용. Android 알림 강조 색상을 설정합니다. |
| `androidNotificationLargeIcon` | string | Android 전용. Android 알림 큰 아이콘을 설정합니다. |
| `androidNotificationSmallIcon` | string | Android 전용. Android 알림 작은 아이콘을 설정합니다. |
| `iosRequestPushPermissionsAutomatically` | boolean | iOS 전용. 앱 실행 시 사용자에게 푸시 권한을 자동으로 요청할지 여부. |
| `enableBrazeIosRichPush` | boolean | iOS 전용. iOS에 리치 푸시 기능을 활성화할지 여부. |
| `enableBrazeIosPushStories` | boolean | iOS 전용. iOS용 Braze Push Stories를 활성화할지 여부. |
| `iosPushStoryAppGroup` | string | iOS 전용. iOS Push Stories에 사용되는 앱 그룹. |
| `iosUseUUIDAsDeviceId` | boolean | iOS 전용. 기기 ID가 무작위로 생성된 UUID를 사용할지 여부. |
| `iosForwardUniversalLinks` | boolean | iOS 전용. SDK가 자동으로 유니버설 링크를 인식하고 시스템 메서드로 전달할지 여부를 지정합니다(기본값: `false`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="2.2 Add the plugin to your app.json" }

다음 코드 스니펫은 `app.json` 구성 예시입니다:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "sessionTimeout": 60,
          "enableGeofence": false,
          "enableBrazeIosPush": false,
          "enableFirebaseCloudMessaging": false,
          "firebaseCloudMessagingSenderId": "YOUR-FCM-SENDER-ID",
          "androidHandlePushDeepLinksAutomatically": true,
          "enableSdkAuthentication": false,
          "logLevel": 0,
          "minimumTriggerIntervalInSeconds": 0,
          "enableAutomaticLocationCollection": false,
          "enableAutomaticGeofenceRequests": false,
          "dismissModalOnOutsideTap": true,
          "androidPushNotificationHtmlRenderingEnabled": true,
          "androidNotificationAccentColor": "#ff3344",
          "androidNotificationLargeIcon": "@drawable/custom_app_large_icon",
          "androidNotificationSmallIcon": "@drawable/custom_app_small_icon",
          "iosRequestPushPermissionsAutomatically": false,
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.example.myapp.PushStories",
          "iosForwardUniversalLinks": false
        }
      ]
    ]
  }
}
```

###### Android 푸시 알림 아이콘 구성 {#android-push-icons}

`androidNotificationLargeIcon` 및 `androidNotificationSmallIcon`을 사용할 때 올바른 아이콘 표시를 위해 다음 모범 사례를 따르세요:

**아이콘 배치 및 형식**

Braze Expo 플러그인으로 커스텀 푸시 알림 아이콘을 사용하려면:

1. 아래 나열된 아이콘 요구 사항에 따라 아이콘 파일을 만드세요.
2. 프로젝트의 Android 네이티브 디렉토리 `android/app/src/main/res/drawable-<density>/`에 배치하세요.
   예를 들어 `android/app/src/main/res/drawable-mdpi/` 및 `android/app/src/main/res/drawable-hdpi/`를 사용하세요.
3. 또는 React Native 디렉토리에서 자산을 관리하는 경우, Expo의 [app.json 아이콘 구성](https://docs.expo.dev/versions/latest/config/app/#icon)을 사용하거나 [Expo 구성 플러그인](https://docs.expo.dev/config-plugins/introduction/)을 만들어 프리빌드 중에 아이콘을 Android drawable 폴더로 복사할 수 있습니다.

Braze Expo 플러그인은 Android의 drawable 리소스 시스템을 사용하여 이러한 아이콘을 참조합니다.

**아이콘 요구 사항**

- **작은 아이콘:** 투명한 배경에 흰색 실루엣이어야 합니다(Android 플랫폼 요구 사항).
- **큰 아이콘:** 풀 컬러 이미지일 수 있습니다.
- **형식:** PNG 형식이 권장됩니다.
- **이름 지정:** 소문자, 숫자 및 밑줄만 사용하세요(예: `my_large_icon.png`).

**app.json에서의 구성**

다음 코드 스니펫은 `@drawable/` 접두사를 사용하여 `app.json`에서 Android 알림 아이콘을 참조하는 방법을 보여줍니다:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidNotificationLargeIcon": "@drawable/large_icon",
          "androidNotificationSmallIcon": "@drawable/small_icon"
        }
      ]
    ]
  }
}
```

{% alert important %}
아이콘을 참조할 때 상대 파일 경로(예: `src/assets/images/icon.png`)를 사용하거나 파일 확장자를 포함하지 마세요. Expo 플러그인은 프리빌드 프로세스 후 Android 네이티브 폴더에서 아이콘을 올바르게 찾기 위해 `@drawable/` 접두사가 필요합니다.
{% endalert %}

**작동 방식**

Braze Expo 플러그인은 Android `drawable` 디렉토리에서 아이콘 파일을 참조합니다. `npx expo prebuild`를 실행하면 Expo가 네이티브 Android 프로젝트 구조를 생성합니다. 아이콘은 빌드 프로세스 전에 Android `drawable` 폴더에 존재해야 합니다(수동으로 배치하거나 구성 플러그인을 통해 복사). 그런 다음 플러그인은 경로나 확장자 없이 이름으로 이러한 drawable 리소스를 사용하도록 Braze SDK를 구성합니다. 이것이 구성에서 `@drawable/` 접두사가 필요한 이유입니다.

Android 알림 아이콘에 대한 자세한 내용은 [Android의 알림 아이콘 가이드라인](https://developer.android.com/develop/ui/views/notifications#icon)을 참조하세요.

##### 2.3 애플리케이션 빌드 및 실행 {#23-build-and-run-your-application} {#23-build-and-run-your-application}

애플리케이션을 프리빌드하면 Braze Expo 플러그인이 작동하는 데 필요한 네이티브 파일이 생성됩니다.

다음 코드 스니펫은 애플리케이션을 프리빌드하는 명령어입니다:

```bash
npx expo prebuild
```

[Expo 문서](https://docs.expo.dev/workflow/customizing/)에 지정된 대로 애플리케이션을 실행하세요. 구성 옵션을 변경한 경우 애플리케이션을 다시 프리빌드하고 실행하세요.

#### 방법 2: React Native CLI 사용 {#reactnative-using-react-native-cli}

##### Android 설정 {#set-up-android}

**2.1 Kotlin Gradle 플러그인 추가**

다음 코드 스니펫은 최상위 프로젝트 `build.gradle`의 `buildscript` > `dependencies` 아래에 Kotlin Gradle 플러그인을 추가하는 방법을 보여줍니다:

```groovy
buildscript {
    dependencies {
        ...
        // Choose your Kotlin version
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:1.8.10")
    }
}
```

이렇게 하면 프로젝트에 Kotlin이 추가됩니다.

**2.2 Braze SDK 구성**

프로젝트의 `res/values` 폴더에 `braze.xml` 파일을 만드세요. API 키와 엔드포인트는 JavaScript에서 런타임에 제공되므로 이 파일에는 필요하지 않습니다. 다음 코드 스니펫은 `com_braze_enable_delayed_initialization`으로 지연 초기화를 활성화하는 방법을 보여줍니다:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <bool name="com_braze_enable_delayed_initialization">true</bool>
</resources>
```

{% alert note %}
`braze.xml`에 다른 네이티브 구성 값(예: 푸시, 세션 타임아웃, 로깅 설정)을 추가할 수 있습니다. 이러한 값은 JavaScript에서 `Braze.initialize()`가 호출될 때 자동으로 적용됩니다.
{% endalert %}

다음 코드 스니펫은 `AndroidManifest.xml` 파일에 필요한 권한입니다:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert tip %}
Braze Android SDK 버전 12.2.0 이상에서는 `gradle.properties` 파일에 `importBrazeLocationLibrary=true`를 설정하여 android-sdk-location 라이브러리를 자동으로 가져올 수 있습니다.
{% endalert %}

**2.3 사용자 세션 추적 구현**

`openSession()` 및 `closeSession()` 호출은 자동으로 처리됩니다.
다음 코드 스니펫은 `MainApplication` 클래스의 `onCreate()` 메서드에 추가할 내용을 보여줍니다:

{% subtabs local %}
{% subtab JAVA %}
```java
import com.braze.BrazeActivityLifecycleCallbackListener;

@Override
public void onCreate() {
    super.onCreate();
    ...
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
import com.braze.BrazeActivityLifecycleCallbackListener

override fun onCreate() {
    super.onCreate()
    ...
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
}
```
{% endsubtab %}
{% endsubtabs %}

**2.4 인텐트 업데이트 처리**

MainActivity의 `android:launchMode`가 `singleTask`로 설정된 경우, 다음 코드 스니펫은 `MainActivity` 클래스에 추가할 내용을 보여줍니다:

{% subtabs local %}
{% subtab JAVA %}
```java
@Override
public void onNewIntent(Intent intent) {
    super.onNewIntent(intent);
    setIntent(intent);
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
override fun onNewIntent(intent: Intent) {
    super.onNewIntent(intent)
    setIntent(intent)
}
```
{% endsubtab %}
{% endsubtabs %}

##### iOS 설정 {#set-up-ios}

**2.5 (선택 사항) 동적 XCFrameworks용 Podfile 구성**

BrazeUI와 같은 특정 Braze 라이브러리를 Objective-C++ 파일에 가져오려면 `#import` 구문을 사용해야 합니다. Braze Swift SDK 버전 `7.4.0`부터 바이너리는 이 구문과 호환되는 [동적 XCFrameworks로의 선택적 배포 채널](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic)을 제공합니다.

이 배포 채널을 사용하려면 Podfile에서 CocoaPods 소스 위치를 수동으로 재정의하세요. 아래 샘플을 참조하고 `{your-version}`을 가져오려는 관련 버전으로 바꾸세요:

```ruby
pod 'BrazeKit', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeKit.podspec'
pod 'BrazeUI', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeUI.podspec'
pod 'BrazeLocation', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeLocation.podspec'
```

**2.6 Pod 설치**

React Native는 라이브러리를 네이티브 플랫폼에 자동으로 연결하므로 CocoaPods를 사용하여 SDK를 설치할 수 있습니다.

다음 코드 스니펫은 프로젝트의 루트 폴더에서 Pod를 설치하는 방법을 보여줍니다:

```bash
# To install using the React Native New Architecture
cd ios && pod install

# To install using the React Native legacy architecture
cd ios && RCT_NEW_ARCH_ENABLED=0 pod install
```

**2.7 Braze SDK 구성**

`AppDelegate`에서 `BrazeReactInitializer.configure`를 사용하여 네이티브 구성을 등록하세요. 제공하는 클로저는 저장되었다가 나중에 JavaScript에서 `Braze.initialize(apiKey, endpoint)`가 호출될 때 적용됩니다.

{% subtabs local %}
{% subtab SWIFT %}

다음 코드 스니펫은 `AppDelegate.swift` 파일 상단에서 Braze SDK를 가져오는 방법을 보여줍니다:

```swift
import BrazeKit
import braze_react_native_sdk
```

`application(_:didFinishLaunchingWithOptions:)` 메서드에서 `BrazeReactInitializer.configure`를 사용하여 네이티브 구성을 등록하세요. 여기에서 API 키나 엔드포인트를 설정하지 마세요. JavaScript에서 `Braze.initialize()`를 통해 제공됩니다.

- **`configure` 클로저**: `Braze.Configuration`을 받아 네이티브 구성 속성(로깅, 푸시, 세션 등)을 설정할 수 있습니다.
- **`postInitialization` 클로저** *(선택 사항)*: 생성 후 라이브 `Braze` 인스턴스를 받아 인스턴스가 필요한 설정(예: 참조 저장 또는 델리게이트 설정)에 사용합니다.

다음 코드 스니펫은 `BrazeReactInitializer.configure`를 사용하는 `AppDelegate.swift` 구현 예시입니다:

```swift
@main
class AppDelegate: UIResponder, UIApplicationDelegate {
  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil
  ) -> Bool {
    BrazeReactInitializer.configure { configuration in
      configuration.logger.level = .info
      configuration.push.automation = true
    } postInitialization: { braze in
      AppDelegate.braze = braze
    }

    // ... React Native setup

    return true
  }
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

다음 코드 스니펫은 `AppDelegate.m` 파일 상단에서 Braze SDK를 가져오는 방법을 보여줍니다:

```objc
@import BrazeKit;
@import braze_react_native_sdk;
```

`application:didFinishLaunchingWithOptions:` 메서드에서 `BrazeReactInitializer`를 사용하여 네이티브 구성을 등록하세요. 여기에서 API 키나 엔드포인트를 설정하지 마세요. JavaScript에서 `Braze.initialize()`를 통해 제공됩니다.

다음 코드 스니펫은 `BrazeReactInitializer`를 사용하는 `AppDelegate.m` 구현 예시입니다:

```objc
- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [BrazeReactInitializer configure:^(BRZConfiguration *configuration) {
    configuration.logger.level = BRZLoggerLevelInfo;
    configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initWithAutomationEnabled:YES];
  } postInitialization:^(Braze *braze) {
    // Store the Braze instance for later use.
  }];

  /* Other configuration */

  return YES;
}
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
`BrazeReactInitializer.configure()`는 구성만 저장합니다. JavaScript에서 `Braze.initialize()`가 호출될 때까지 Braze 인스턴스가 존재하지 않으므로, `configure()` 이후 AppDelegate에서 Braze SDK 메서드를 호출하지 마세요.
`Braze.initialize()`를 다시 호출하면 동일한 `configure` 및 `postInitialization` 블록이 새 Braze 인스턴스에 적용됩니다.
{% endalert %}

{% endtab %}
{% tab React Native SDK 19.1.0 이하 %}

#### 방법 1: Expo 플러그인 사용 {#method-1-using-the-expo-plugin}

##### 2.1단계: Braze Expo 플러그인 설치 {#step-21-install-the-braze-expo-plugin}

Braze React Native SDK 버전이 1.37.0 이상인지 확인하세요. 지원되는 버전의 전체 목록은 [Braze React Native 리포지토리](https://github.com/braze-inc/braze-react-native-sdk?tab=readme-ov-file#version-support)를 참조하세요.

다음 코드 스니펫은 Braze Expo 플러그인을 설치하는 명령어입니다:

```bash
npx expo install @braze/expo-plugin
```

##### 2.2단계: app.json에 플러그인 추가 {#step-22-add-the-plugin-to-your-appjson}

`app.json`에 Braze Expo 플러그인을 추가하세요. 다음 구성 옵션을 제공할 수 있습니다:

| 메서드 | 유형 | 설명 |
| --------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `androidApiKey` | string | 필수. Braze 대시보드의 **설정 관리** 아래에 있는 Android 애플리케이션의 [API 키]({{site.baseurl}}/api/identifier_types/). |
| `iosApiKey` | string | 필수. Braze 대시보드의 **설정 관리** 아래에 있는 iOS 애플리케이션의 [API 키]({{site.baseurl}}/api/identifier_types/). |
| `baseUrl` | string | 필수. Braze 대시보드의 **설정 관리** 아래에 있는 애플리케이션의 [SDK 엔드포인트]({{site.baseurl}}/api/basics/#endpoints). |
| `enableBrazeIosPush` | boolean | iOS 전용. iOS에서 푸시 알림을 처리하기 위해 Braze를 사용할지 여부. React Native SDK v1.38.0 및 Expo Plugin v0.4.0에서 도입되었습니다. |
| `enableFirebaseCloudMessaging` | boolean | Android 전용. 푸시 알림에 Firebase Cloud Messaging을 사용할지 여부. React Native SDK v1.38.0 및 Expo Plugin v0.4.0에서 도입되었습니다. |
| `firebaseCloudMessagingSenderId` | string | Android 전용. Firebase Cloud Messaging 발신자 ID. React Native SDK v1.38.0 및 Expo Plugin v0.4.0에서 도입되었습니다. |
| `sessionTimeout` | integer | 애플리케이션의 Braze 세션 타임아웃(초). |
| `enableSdkAuthentication` | boolean | [SDK 인증](https://www.braze.com/docs/developer_guide/platform_wide/sdk_authentication#sdk-authentication) 기능을 활성화할지 여부. |
| `logLevel` | integer | 애플리케이션의 로그 레벨. 기본 로그 레벨은 8이며 최소한의 정보를 기록합니다. 디버깅을 위해 상세 로깅을 활성화하려면 로그 레벨 0을 사용하세요. |
| `minimumTriggerIntervalInSeconds` | integer | 트리거 사이의 최소 시간 간격(초). 기본값은 30초입니다. |
| `enableAutomaticLocationCollection` | boolean | 자동 위치 수집이 활성화되어 있는지 여부(사용자가 허용하는 경우). |
| `enableGeofence` | boolean | 지오펜스가 활성화되어 있는지 여부. |
| `enableAutomaticGeofenceRequests` | boolean | 지오펜스 요청이 자동으로 이루어져야 하는지 여부. |
| `dismissModalOnOutsideTap` | boolean | iOS 전용. 사용자가 인앱 메시지 외부를 클릭할 때 모달 인앱 메시지가 해제되는지 여부. |
| `androidHandlePushDeepLinksAutomatically` | boolean | Android 전용. Braze SDK가 푸시 딥링크를 자동으로 처리해야 하는지 여부. |
| `androidPushNotificationHtmlRenderingEnabled` | boolean | Android 전용. 푸시 알림의 텍스트 콘텐츠를 `android.text.Html.fromHtml`을 사용하여 HTML로 해석하고 렌더링할지 여부를 설정합니다. |
| `androidNotificationAccentColor` | string | Android 전용. Android 알림 강조 색상을 설정합니다. |
| `androidNotificationLargeIcon` | string | Android 전용. Android 알림 큰 아이콘을 설정합니다. |
| `androidNotificationSmallIcon` | string | Android 전용. Android 알림 작은 아이콘을 설정합니다. |
| `iosRequestPushPermissionsAutomatically` | boolean | iOS 전용. 앱 실행 시 사용자에게 푸시 권한을 자동으로 요청할지 여부. |
| `enableBrazeIosRichPush` | boolean | iOS 전용. iOS에 리치 푸시 기능을 활성화할지 여부. |
| `enableBrazeIosPushStories` | boolean | iOS 전용. iOS용 Braze Push Stories를 활성화할지 여부. |
| `iosPushStoryAppGroup` | string | iOS 전용. iOS Push Stories에 사용되는 앱 그룹. |
| `iosUseUUIDAsDeviceId` | boolean | iOS 전용. 기기 ID가 무작위로 생성된 UUID를 사용할지 여부. |
| `iosForwardUniversalLinks` | boolean | iOS 전용. SDK가 자동으로 유니버설 링크를 인식하고 시스템 메서드로 전달할지 여부를 지정합니다(기본값: `false`). 활성화되면 SDK는 [앱에서 유니버설 링크 지원](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks/)에 정의된 시스템 메서드로 유니버설 링크를 자동으로 전달합니다. React Native SDK v11.1.0 및 Expo Plugin v3.2.0에서 도입되었습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Step 2.2: Add the plugin to your app.json" }

다음 코드 스니펫은 `app.json` 구성 예시입니다:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidApiKey": "YOUR-ANDROID-API-KEY",
          "iosApiKey": "YOUR-IOS-API-KEY",
          "baseUrl": "YOUR-SDK-ENDPOINT",
          "sessionTimeout": 60,
          "enableGeofence": false,
          "enableBrazeIosPush": false,
          "enableFirebaseCloudMessaging": false,
          "firebaseCloudMessagingSenderId": "YOUR-FCM-SENDER-ID",
          "androidHandlePushDeepLinksAutomatically": true,
          "enableSdkAuthentication": false,
          "logLevel": 0,
          "minimumTriggerIntervalInSeconds": 0,
          "enableAutomaticLocationCollection": false,
          "enableAutomaticGeofenceRequests": false,
          "dismissModalOnOutsideTap": true,
          "androidPushNotificationHtmlRenderingEnabled": true,
          "androidNotificationAccentColor": "#ff3344",
          "androidNotificationLargeIcon": "@drawable/custom_app_large_icon",
          "androidNotificationSmallIcon": "@drawable/custom_app_small_icon",
          "iosRequestPushPermissionsAutomatically": false,
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.example.myapp.PushStories",
          "iosForwardUniversalLinks": false
        }
      ],
    ]
  }
}
```

###### Android 푸시 알림 아이콘 구성 {#configuring-android-push-notification-icons}

`androidNotificationLargeIcon` 및 `androidNotificationSmallIcon`을 사용할 때 올바른 아이콘 표시를 위해 다음 모범 사례를 따르세요:

**아이콘 배치 및 형식**

Braze Expo 플러그인으로 커스텀 푸시 알림 아이콘을 사용하려면:

1. 아래 나열된 아이콘 요구 사항에 따라 아이콘 파일을 만드세요.
2. 프로젝트의 Android 네이티브 디렉토리 `android/app/src/main/res/drawable-<density>/`에 배치하세요(예: `android/app/src/main/res/drawable-mdpi/`, `drawable-hdpi/` 등).
3. 또는 React Native 디렉토리에서 자산을 관리하는 경우, Expo의 [app.json 아이콘 구성](https://docs.expo.dev/versions/latest/config/app/#icon)을 사용하거나 [Expo 구성 플러그인](https://docs.expo.dev/config-plugins/introduction/)을 만들어 프리빌드 중에 아이콘을 Android drawable 폴더로 복사할 수 있습니다.

Braze Expo 플러그인은 Android의 drawable 리소스 시스템을 사용하여 이러한 아이콘을 참조합니다.

**아이콘 요구 사항**

- **작은 아이콘:** 투명한 배경에 흰색 실루엣이어야 합니다(Android 플랫폼 요구 사항).
- **큰 아이콘:** 풀 컬러 이미지일 수 있습니다.
- **형식:** PNG 형식이 권장됩니다.
- **이름 지정:** 소문자, 숫자 및 밑줄만 사용하세요(예: `my_large_icon.png`).

**app.json에서의 구성**

다음 코드 스니펫은 `@drawable/` 접두사를 사용하여 `app.json`에서 Android 알림 아이콘을 참조하는 방법을 보여줍니다:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidNotificationLargeIcon": "@drawable/large_icon",
          "androidNotificationSmallIcon": "@drawable/small_icon"
        }
      ]
    ]
  }
}
```

{% alert important %}
아이콘을 참조할 때 상대 파일 경로(예: `src/assets/images/icon.png`)를 사용하거나 파일 확장자를 포함하지 마세요. Expo 플러그인은 프리빌드 프로세스 후 Android 네이티브 폴더에서 아이콘을 올바르게 찾기 위해 `@drawable/` 접두사가 필요합니다.
{% endalert %}

**작동 방식**

Braze Expo 플러그인은 Android `drawable` 디렉토리에서 아이콘 파일을 참조합니다. `npx expo prebuild`를 실행하면 Expo가 네이티브 Android 프로젝트 구조를 생성합니다. 아이콘은 빌드 프로세스 전에 Android `drawable` 폴더에 존재해야 합니다(수동으로 배치하거나 구성 플러그인을 통해 복사). 그런 다음 플러그인은 경로나 확장자 없이 이름으로 이러한 drawable 리소스를 사용하도록 Braze SDK를 구성합니다. 이것이 구성에서 `@drawable/` 접두사가 필요한 이유입니다.

Android 알림 아이콘에 대한 자세한 내용은 [Android의 알림 아이콘 가이드라인](https://developer.android.com/develop/ui/views/notifications#icon)을 참조하세요.

##### 2.3단계: 애플리케이션 빌드 및 실행 {#step-23-build-and-run-your-application}

애플리케이션을 프리빌드하면 Braze Expo 플러그인이 작동하는 데 필요한 네이티브 파일이 생성됩니다.

다음 코드 스니펫은 애플리케이션을 프리빌드하는 명령어입니다:

```bash
npx expo prebuild
```

[Expo 문서](https://docs.expo.dev/workflow/customizing/)에 지정된 대로 애플리케이션을 실행하세요. 구성 옵션을 변경한 경우 애플리케이션을 다시 프리빌드하고 실행해야 합니다.

#### 방법 2: React Native CLI 사용 {#method-2-using-react-native-cli}

##### Android 설정

**2.1단계: Kotlin Gradle 플러그인 추가**

다음 코드 스니펫은 최상위 프로젝트 `build.gradle`의 `buildscript` > `dependencies` 아래에 Kotlin Gradle 플러그인을 추가하는 방법을 보여줍니다:

```groovy
buildscript {
    dependencies {
        ...
        // Choose your Kotlin version
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:1.8.10")
    }
}
```

이렇게 하면 프로젝트에 Kotlin이 추가됩니다.

**2.2단계: Braze SDK 구성**

Braze 서버에 연결하려면 프로젝트의 `res/values` 폴더에 `braze.xml` 파일을 만드세요. 다음 코드 스니펫은 `braze.xml` 구성 예시입니다. API [키]({{site.baseurl}}/api/identifier_types/) 및 [엔드포인트]({{site.baseurl}}/api/basics/#endpoints)를 실제 값으로 바꾸세요:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOU_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

다음 코드 스니펫은 `AndroidManifest.xml` 파일에 필요한 권한입니다:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert tip %}
Braze Android SDK 버전 12.2.0 이상에서는 `gradle.properties` 파일에 `importBrazeLocationLibrary=true`를 설정하여 android-sdk-location 라이브러리를 자동으로 가져올 수 있습니다.
{% endalert %}

**2.3단계: 사용자 세션 추적 구현**

`openSession()` 및 `closeSession()` 호출은 자동으로 처리됩니다.
다음 코드 스니펫은 `MainApplication` 클래스의 `onCreate()` 메서드에 추가할 내용을 보여줍니다:

{% subtabs local %}
{% subtab JAVA %}
```java
import com.braze.BrazeActivityLifecycleCallbackListener;

@Override
public void onCreate() {
    super.onCreate();
    ...
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
import com.braze.BrazeActivityLifecycleCallbackListener

override fun onCreate() {
    super.onCreate()
    ...
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
}
```
{% endsubtab %}
{% endsubtabs %}

**2.4단계: 인텐트 업데이트 처리**

MainActivity의 `android:launchMode`가 `singleTask`로 설정된 경우, 다음 코드 스니펫은 `MainActivity` 클래스에 추가할 내용을 보여줍니다:

{% subtabs local %}
{% subtab JAVA %}
```java
@Override
public void onNewIntent(Intent intent) {
    super.onNewIntent(intent);
    setIntent(intent);
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
override fun onNewIntent(intent: Intent) {
    super.onNewIntent(intent)
    setIntent(intent)
}
```
{% endsubtab %}
{% endsubtabs %}

##### iOS 설정

**2.5단계: (선택 사항) 동적 XCFrameworks용 Podfile 구성**

BrazeUI와 같은 특정 Braze 라이브러리를 Objective-C++ 파일에 가져오려면 `#import` 구문을 사용해야 합니다. Braze Swift SDK 버전 `7.4.0`부터 바이너리는 이 구문과 호환되는 [동적 XCFrameworks로의 선택적 배포 채널](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic)을 제공합니다.

이 배포 채널을 사용하려면 Podfile에서 CocoaPods 소스 위치를 수동으로 재정의하세요. 다음 코드 스니펫은 샘플 재정의입니다. `{your-version}`을 가져오려는 관련 버전으로 바꾸세요:

```ruby
pod 'BrazeKit', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeKit.podspec'
pod 'BrazeUI', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeUI.podspec'
pod 'BrazeLocation', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeLocation.podspec'
```

**2.6단계: Pod 설치**

React Native는 라이브러리를 네이티브 플랫폼에 자동으로 연결하므로 CocoaPods를 사용하여 SDK를 설치할 수 있습니다.

다음 코드 스니펫은 프로젝트의 루트 폴더에서 Pod를 설치하는 방법을 보여줍니다:

```bash
# To install using the React Native New Architecture
cd ios && pod install

# To install using the React Native legacy architecture
cd ios && RCT_NEW_ARCH_ENABLED=0 pod install
```

**2.7단계: Braze SDK 구성**

{% subtabs local %}
{% subtab SWIFT %}

다음 코드 스니펫은 `AppDelegate.swift` 파일 상단에서 Braze SDK를 가져오는 방법을 보여줍니다:
```swift
import BrazeKit
import braze_react_native_sdk
```

`application(_:didFinishLaunchingWithOptions:)` 메서드에서 API [키]({{site.baseurl}}/api/identifier_types/) 및 [엔드포인트]({{site.baseurl}}/api/basics/#endpoints)를 앱의 값으로 바꾸세요. 그런 다음 구성을 사용하여 Braze 인스턴스를 생성하고 `AppDelegate`에 정적 속성을 만들어 쉽게 액세스할 수 있도록 합니다.

{% alert note %}
이 예제는 React Native 설정에서 여러 추상화를 제공하는 [RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h)의 구현을 가정합니다. 앱에 다른 설정을 사용하는 경우 필요에 따라 구현을 조정하세요.
{% endalert %}

다음 코드 스니펫은 `AppDelegate.swift` 설정 예시입니다:

```swift
func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
    // Setup Braze
    let configuration = Braze.Configuration(
        apiKey: "{BRAZE_API_KEY}",
        endpoint: "{BRAZE_ENDPOINT}")
    // Enable logging and customize the configuration here.
    configuration.logger.level = .info
    let braze = BrazeReactBridge.perform(
      #selector(BrazeReactBridge.initBraze(_:)),
      with: configuration
    ).takeUnretainedValue() as! Braze

    AppDelegate.braze = braze

    /* Other configuration */

    return true
}

// MARK: - AppDelegate.braze

static var braze: Braze? = nil
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

다음 코드 스니펫은 `AppDelegate.m` 파일 상단에서 Braze SDK를 가져오는 방법을 보여줍니다:
```objc
#import <BrazeKit/BrazeKit-Swift.h>
#import "BrazeReactBridge.h"
```

`application:didFinishLaunchingWithOptions:` 메서드에서 API [키]({{site.baseurl}}/api/identifier_types/) 및 [엔드포인트]({{site.baseurl}}/api/basics/#endpoints)를 앱의 값으로 바꾸세요. 그런 다음 구성을 사용하여 Braze 인스턴스를 생성하고 `AppDelegate`에 정적 속성을 만들어 쉽게 액세스할 수 있도록 합니다.

{% alert note %}
이 예제는 React Native 설정에서 여러 추상화를 제공하는 [RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h)의 구현을 가정합니다. 앱에 다른 설정을 사용하는 경우 필요에 따라 구현을 조정하세요.
{% endalert %}

다음 코드 스니펫은 `AppDelegate.m` 설정 예시입니다:

```objc
- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Setup Braze
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"{BRAZE_API_KEY}"
                                                                    endpoint:@"{BRAZE_ENDPOINT}"];
  // Enable logging and customize the configuration here.
  configuration.logger.level = BRZLoggerLevelInfo;
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  AppDelegate.braze = braze;

  /* Other configuration */

  return YES;
}

#pragma mark - AppDelegate.braze

static Braze *_braze = nil;

+ (Braze *)braze {
  return _braze;
}

+ (void)setBraze:(Braze *)braze {
  _braze = braze;
}
```

{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% endtabs %}

### 3단계: SDK 초기화 {#step-3-initialize-the-sdk}

{% tabs %}
{% tab React Native SDK 19.2.0+ %}

다음 코드 스니펫은 React Native 코드에서 라이브러리를 가져오는 방법을 보여줍니다:

```javascript
import Braze from "@braze/react-native-sdk";
```

그런 다음 앱 식별자 API 키와 SDK 엔드포인트를 사용하여 `Braze.initialize()`를 호출하여 Braze 인스턴스를 생성하세요. 앱에서 이 메서드를 호출할 위치에 대해서는 아래 옵션을 참조하세요.

#### 표준 초기화 {#standard-initialization}

다음 코드 스니펫은 `useEffect`에서 `Braze.initialize()`를 호출하여 앱 시작 시 SDK를 초기화하는 방법을 보여줍니다:

```javascript
import React, { useEffect } from "react";
import Braze from "@braze/react-native-sdk";

const App = () => {
  useEffect(() => {
    Braze.initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT");
  }, []);

  return (
    // Your app components
  );
};
```

#### 지연 초기화 {#delayed-initialization}

다음 코드 스니펫은 세션 후반까지 SDK 초기화를 지연하는 방법을 보여줍니다. 예를 들어 사용자가 동의하거나 로그인을 완료한 후에 초기화할 수 있습니다:

```javascript
function onUserConsent() {
  Braze.initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT");
}
```

{% alert warning %}
iOS에서는 `Braze.initialize()` 전에 수신된 푸시 알림이 대기열에 추가되고 초기화 후에 처리됩니다. Android에서는 SDK가 초기화를 기다리는 동안 푸시 알림의 딥링크가 해결되지 않습니다. 앱이 실행 시 즉각적인 딥링크 처리에 의존하는 경우 [표준 초기화](#standard-initialization)를 대신 사용하세요.
{% endalert %}

#### 플랫폼별 API 키 {#platform-specific-api-keys}

다음 코드 스니펫은 Android와 iOS 앱이 서로 다른 API 키를 사용할 때 플랫폼 감지를 사용하는 방법을 보여줍니다:

```javascript
import { Platform } from "react-native";
import Braze from "@braze/react-native-sdk";

const apiKey = Platform.select({
  android: "YOUR-ANDROID-API-KEY",
  ios: "YOUR-IOS-API-KEY",
}) ?? "";

Braze.initialize(apiKey, "YOUR-SDK-ENDPOINT");
```

#### 재초기화 {#re-initialization}

세션 중에 다른 API 키와 엔드포인트로 SDK를 재초기화하기 위해 `Braze.initialize()`를 여러 번 호출할 수 있습니다. 각 호출은 이전 Braze 인스턴스를 해제하고 새 인스턴스를 생성합니다.

{% alert important %}
`Braze.initialize()` 전에 수행된 모든 SDK 메서드 호출은 iOS에서 무시되므로, 다른 Braze 메서드를 사용하기 전에 `Braze.initialize()`를 호출하세요.
{% endalert %}

{% endtab %}
{% tab React Native SDK 19.1.0 이하 %}

React Native SDK 19.1.0 이하에서는 네이티브 초기화가 2단계에서 수행됩니다. React Native 코드에서 라이브러리를 가져와 Braze 메서드를 호출하세요. 자세한 내용은 [샘플 프로젝트](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject)를 확인하세요.

```javascript
import Braze from "@braze/react-native-sdk";
```

{% endtab %}
{% endtabs %}

### 4단계: 통합 테스트(선택 사항) {#step-4-test-the-integration-optional}

{% tabs %}
{% tab React Native SDK 19.2.0+ %}

대시보드에서 세션 통계를 확인하여 SDK가 통합되었는지 확인할 수 있습니다. 어느 플랫폼에서든 애플리케이션을 실행하면 대시보드(**개요** 섹션)에 새 세션이 표시됩니다.

다음 코드 스니펫은 앱에서 특정 사용자에 대한 세션을 여는 방법을 보여줍니다:

```javascript
import Braze from "@braze/react-native-sdk";

Braze.initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT");
Braze.changeUser("{some-user-id}");
```

대시보드에서 **오디언스** > **사용자 검색**으로 이동하여 `{some-user-id}`로 사용자를 검색하세요. 세션 및 기기 데이터가 기록되었는지 확인할 수 있습니다.

{% endtab %}
{% tab React Native SDK 19.1.0 이하 %}

SDK 통합을 테스트하기 위해, 다음 코드 스니펫은 사용자에 대해 어느 플랫폼에서든 새 세션을 시작하는 방법을 보여줍니다.

```javascript
Braze.changeUser("userId");
```

다음 코드 스니펫은 앱 시작 시 사용자 ID를 할당하는 예시입니다:

```javascript
import React, { useEffect } from "react";
import Braze from "@braze/react-native-sdk";

const App = () => {
  useEffect(() => {
    Braze.changeUser("some-user-id");
  }, []);

  return (
    <div>
      ...
    </div>
  )
```

Braze 대시보드에서 [사용자 검색]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#using-user-search)으로 이동하여 `some-user-id`와 일치하는 ID를 가진 사용자를 찾으세요. 세션 및 기기 데이터가 기록되었는지 확인할 수 있습니다.

{% endtab %}
{% endtabs %}

## 다음 단계 {#next-steps}

Braze SDK를 통합한 후 일반 메시징 기능을 구현할 수 있습니다:

- [푸시 알림]({{site.baseurl}}/developer_guide/push_notifications/): 사용자에게 푸시 알림을 설정하고 전송하세요.
- [In-App Messages]({{site.baseurl}}/developer_guide/in_app_messages/): 앱 내에서 상황별 메시지를 표시하세요.
- [배너]({{site.baseurl}}/developer_guide/banners/): 앱 인터페이스에 지속 배너를 표시하세요.