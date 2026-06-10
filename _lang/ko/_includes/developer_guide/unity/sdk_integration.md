## Unity Braze SDK 소개 {#about-the-unity-braze-sdk}

유형, 함수, 변수 등의 전체 목록은 [Unity 선언 파일](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs)을 참조하세요. 또한 이미 iOS용 Unity를 수동으로 통합한 경우 [자동화된 통합으로 전환](#unity_automated-integration)할 수 있습니다.

## Unity SDK 통합하기 {#integrating-the-unity-sdk}

### 필수 조건 {#prerequisites}

시작하기 전에 사용 중인 환경이 [최신 Braze Unity SDK 버전](https://github.com/braze-inc/braze-unity-sdk/releases)에서 지원되는지 확인하세요.

### 1단계: Braze Unity 패키지 선택 {#step-1-choose-your-braze-unity-package}

{% tabs %}
{% tab Android %}
Braze [`.unitypackage`](https://docs.unity3d.com/Manual/AssetPackages.html)는 C# 인터페이스와 함께 Android 및 iOS 플랫폼용 네이티브 바인딩을 번들로 제공합니다.

[Braze Unity 릴리즈 페이지](https://github.com/Appboy/appboy-unity-sdk/releases)에서 여러 Braze Unity 패키지를 다운로드할 수 있습니다:

- `Appboy.unitypackage`
    - 이 패키지는 Braze Android 및 iOS SDK와 iOS SDK에 대한 [SDWebImage](https://github.com/SDWebImage/SDWebImage) 종속성을 번들로 제공하며, iOS에서 Braze 인앱 메시지 및 Content Cards 기능이 제대로 작동하는 데 필요합니다. SDWebImage 프레임워크는 GIF를 포함한 이미지를 다운로드하고 표시하는 데 사용됩니다. Braze의 모든 기능을 활용하려면 이 패키지를 다운로드하여 가져오세요.
- `Appboy-nodeps.unitypackage`
    - 이 패키지는 [SDWebImage](https://github.com/SDWebImage/SDWebImage) 프레임워크가 포함되지 않는다는 점을 제외하면 `Appboy.unitypackage`와 유사합니다. iOS 앱에 SDWebImage 프레임워크를 포함하지 않으려는 경우에 유용합니다.

{% alert note %}
Unity 2.6.0부터 번들로 제공되는 Braze Android SDK 아티팩트에는 [AndroidX](https://developer.android.com/jetpack/androidx) 종속성이 필요합니다. 이전에 `jetified` unitypackage를 사용했다면 해당하는 `unitypackage`로 안전하게 전환할 수 있습니다.

Android 빌드가 "This project uses AndroidX dependencies, but the 'android.useAndroidX' property is not enabled" 오류로 실패하는 경우, Unity 퍼블리싱 설정에서 [Custom Gradle Properties Template](https://docs.unity3d.com/Manual/class-PlayerSettingsAndroid.html#Publishing)을 활성화하세요. 그런 다음 `Assets/Plugins/Android/gradleTemplate.properties`를 열고 `android.useAndroidX=true`로 설정합니다. 작동하는 템플릿은 [Braze Unity 샘플 앱](https://github.com/braze-inc/braze-unity-sdk/tree/master/unity-samples)과 해당 [`gradleTemplate.properties`](https://github.com/braze-inc/braze-unity-sdk/blob/master/unity-samples/Assets/Plugins/Android/gradleTemplate.properties) 파일을 참조하세요.
{% endalert %}
{% endtab %}

{% tab Swift %}
Braze [`.unitypackage`](https://docs.unity3d.com/Manual/AssetPackages.html)는 C# 인터페이스와 함께 Android 및 iOS 플랫폼용 네이티브 바인딩을 번들로 제공합니다.

Braze Unity 패키지는 두 가지 통합 옵션과 함께 [Braze Unity 릴리즈 페이지](https://github.com/Appboy/appboy-unity-sdk/releases)에서 다운로드할 수 있습니다:

1. `Appboy.unitypackage`만 사용
  - 이 패키지는 추가 종속성 없이 Braze Android 및 iOS SDK를 번들로 제공합니다. 이 통합 방법을 사용하면 iOS에서 Braze 인앱 메시지 및 Content Cards 기능이 제대로 작동하지 않습니다. 커스텀 코드 없이 Braze의 모든 기능을 활용하려면 아래 옵션을 사용하세요.
  - 이 통합 옵션을 사용하려면 Unity UI의 "Braze Configuration" 아래에서 `Import SDWebImage dependency` 옆의 확인란이 *선택 해제*되어 있는지 확인하세요.
2. `Appboy.unitypackage`와 `SDWebImage` 함께 사용
  - 이 통합 옵션은 Braze Android 및 iOS SDK와 iOS SDK에 대한 [SDWebImage](https://github.com/SDWebImage/SDWebImage) 종속성을 번들로 제공하며, iOS에서 Braze 인앱 메시지 및 Content Cards 기능이 제대로 작동하는 데 필요합니다. `SDWebImage` 프레임워크는 GIF를 포함한 이미지를 다운로드하고 표시하는 데 사용됩니다. Braze의 모든 기능을 활용하려면 이 패키지를 다운로드하여 가져오세요.
  - `SDWebImage`를 자동으로 가져오려면 Unity UI의 "Braze Configuration" 아래에서 `Import SDWebImage dependency` 옆의 확인란을 *선택*해야 합니다.

{% alert note %}
iOS 프로젝트에 [SDWebImage](https://github.com/SDWebImage/SDWebImage) 종속성이 필요한지 확인하려면 [iOS 인앱 메시지 설명서]({{ site.baseurl }}/developer_guide/platform_integration_guides/swift/in-app_messaging/overview/)를 참조하세요.
{% endalert %}
{% endtab %}
{% endtabs %}

### 2단계: 패키지 가져오기 {#step-2-import-the-package}

{% tabs %}
{% tab Android %}
Unity 편집기에서 **Assets > Import Package > Custom Package**로 이동하여 패키지를 Unity 프로젝트로 가져옵니다. 그런 다음 **Import**를 클릭합니다.

또는 커스텀 Unity 패키지 가져오기에 대한 자세한 가이드는 [Unity 자산 패키지 가져오기](https://docs.unity3d.com/Manual/AssetPackages.html) 지침을 따르세요.

{% alert note %}
iOS 또는 Android 플러그인만 가져오려면 Braze `.unitypackage`를 가져올 때 `Plugins/Android` 또는 `Plugins/iOS` 하위 디렉토리를 선택 해제하세요.
{% endalert %}
{% endtab %}

{% tab Swift %}
Unity 편집기에서 **Assets > Import Package > Custom Package**로 이동하여 패키지를 Unity 프로젝트로 가져옵니다. 그런 다음 **Import**를 클릭합니다.

또는 커스텀 Unity 패키지 가져오기에 대한 자세한 가이드는 [Unity 자산 패키지 가져오기](https://docs.unity3d.com/Manual/AssetPackages.html) 지침을 따르세요.

{% alert note %}
iOS 또는 Android 플러그인만 가져오려면 Braze `.unitypackage`를 가져올 때 `Plugins/Android` 또는 `Plugins/iOS` 하위 디렉토리를 선택 해제하세요.
{% endalert %}
{% endtab %}
{% endtabs %}

### 3단계: SDK 구성하기 {#step-3-configure-the-sdk}

{% tabs %}
{% tab Android %}
#### 3.1단계: `AndroidManifest.xml` 구성 {#step-31-configure-androidmanifestxml}

Braze SDK가 작동할 수 있도록 [`AndroidManifest.xml`](https://docs.unity3d.com/Manual/android-manifest.html)을 구성합니다. 앱에 `AndroidManifest.xml`이 없는 경우 다음을 템플릿으로 사용할 수 있습니다. 이미 `AndroidManifest.xml`이 있는 경우에는 기존 `AndroidManifest.xml`에 다음 중 누락된 섹션이 추가되었는지 확인하세요.

1. `Assets/Plugins/Android/` 디렉토리로 이동하여 `AndroidManifest.xml` 파일을 엽니다. 이 위치는 [Unity 편집기의 기본 위치](https://docs.unity3d.com/Manual/android-manifest.html)입니다.
2. `AndroidManifest.xml`에서 다음 템플릿의 필수 권한 및 액티비티를 추가합니다.
3. 완료되면 `AndroidManifest.xml`에는 `"android.intent.category.LAUNCHER"`가 있는 하나의 액티비티만 포함되어야 합니다.

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="REPLACE_WITH_YOUR_PACKAGE_NAME">

  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
  <uses-permission android:name="android.permission.INTERNET" />

  <application android:icon="@drawable/app_icon"
               android:label="@string/app_name">

    <!-- Calls the necessary Braze methods to ensure that analytics are collected and that push notifications are properly forwarded to the Unity application. -->
    <activity android:name="com.braze.unity.BrazeUnityPlayerActivity"
      android:theme="@style/UnityThemeSelector"
      android:label="@string/app_name"
      android:configChanges="fontScale|keyboard|keyboardHidden|locale|mnc|mcc|navigation|orientation|screenLayout|screenSize|smallestScreenSize|uiMode|touchscreen"
      android:screenOrientation="sensor">
      <meta-data android:name="android.app.lib_name" android:value="unity" />
      <meta-data android:name="unityplayer.ForwardNativeEventsToDalvik" android:value="true" />
      <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
      </intent-filter>
    </activity>

    <!-- A Braze specific FirebaseMessagingService used to handle push notifications. -->
    <service android:name="com.braze.push.BrazeFirebaseMessagingService"
      android:exported="false">
      <intent-filter>
        <action android:name="com.google.firebase.MESSAGING_EVENT" />
      </intent-filter>
    </service>
  </application>
</manifest>
```

{% alert important %}
`AndroidManifest.xml` 파일에 등록된 모든 액티비티 클래스는 Braze Android SDK와 완전히 통합되어야 하며, 그렇지 않으면 분석 데이터가 수집되지 않습니다. 자체 액티비티 클래스를 추가하는 경우 이를 방지할 수 있도록 [Braze Unity 플레이어를 확장](#unity_extend-unity-player)해야 합니다.
{% endalert %}

#### 3.2단계: 패키지 이름으로 `AndroidManifest.xml` 업데이트 {#step-32-update-androidmanifestxml-with-your-package-name}

패키지 이름을 찾으려면 **File > Build Settings > Player Settings > Android Tab**을 클릭합니다.

![]({% image_buster /assets/img_archive/UnityPackageName.png %})

`AndroidManifest.xml`에서 `REPLACE_WITH_YOUR_PACKAGE_NAME`의 모든 인스턴스를 이전 단계의 `Package Name`으로 바꿔야 합니다.

#### 3.3단계: Gradle 종속성 추가 {#step-33-add-gradle-dependencies}

Unity 프로젝트에 Gradle 종속성을 추가하려면 먼저 퍼블리싱 설정에서 ["Custom Main Gradle Template"](https://docs.unity3d.com/Manual/class-PlayerSettingsAndroid.html#Publishing)을 활성화합니다. 그러면 프로젝트에서 사용할 템플릿 Gradle 파일이 생성됩니다. Gradle 파일은 종속성 설정 및 기타 빌드 시점 프로젝트 설정을 처리합니다. 자세한 내용은 Braze Unity 샘플 앱의 [mainTemplate.gradle](https://github.com/braze-inc/braze-unity-sdk/blob/master/unity-samples/Assets/Plugins/Android/mainTemplate.gradle)을 확인하세요.

다음 종속성이 필요합니다:

```groovy
implementation 'com.google.firebase:firebase-messaging:22.0.0'
implementation "androidx.swiperefreshlayout:swiperefreshlayout:1.1.0"
implementation "androidx.recyclerview:recyclerview:1.2.1"
implementation "org.jetbrains.kotlin:kotlin-stdlib:1.6.0"
implementation "org.jetbrains.kotlinx:kotlinx-coroutines-android:1.6.1"
implementation 'androidx.core:core:1.6.0'
```

[External Dependency Manager](https://github.com/googlesamples/unity-jar-resolver)를 사용하여 이러한 종속성을 설정할 수도 있습니다.

#### 3.4단계: Unity Android 통합 자동화 {#step-34-automate-the-unity-android-integration}

Braze는 Unity Android 통합을 자동화하기 위한 네이티브 Unity 솔루션을 제공합니다.

1. Unity 편집기에서 **Braze > Braze Configuration**으로 이동하여 Braze 구성 설정을 엽니다.
2. **Automate Unity Android Integration** 확인란을 선택합니다.
3. **Braze API Key** 필드에 Braze 대시보드의 **설정 관리**에서 찾은 애플리케이션의 API 키를 입력합니다.

{% alert note %}
이 자동 통합은 수동으로 생성한 `braze.xml` 파일과 함께 사용해서는 안 됩니다. 프로젝트 빌드 중에 구성 값이 충돌할 수 있기 때문입니다. 수동 `braze.xml`이 필요한 경우 자동 통합을 비활성화하세요.
{% endalert %}
{% endtab %}

{% tab Swift %}
#### 3.1단계: API 키 설정 {#step-31-set-your-api-key}

Braze는 Unity iOS 통합을 자동화하기 위한 네이티브 Unity 솔루션을 제공합니다. 이 솔루션은 Unity의 [`PostProcessBuildAttribute`](http://docs.unity3d.com/ScriptReference/Callbacks.PostProcessBuildAttribute.html)를 사용하여 빌드된 Xcode 프로젝트를 수정하고 `IMPL_APP_CONTROLLER_SUBCLASS` 매크로를 사용하여 `UnityAppController`를 서브클래스로 구성합니다.

1. Unity 편집기에서 **Braze > Braze Configuration**으로 이동하여 Braze 구성 설정을 엽니다.
2. **Automate Unity iOS Integration** 확인란을 선택합니다.
3. **Braze API Key** 필드에 **설정 관리**에서 찾은 애플리케이션의 API 키를 입력합니다.

![]({% image_buster /assets/img_archive/unity-ios-appboyconfig.png %})

애플리케이션에서 이미 다른 `UnityAppController` 서브클래스를 사용하고 있는 경우, 서브클래스 구현을 `AppboyAppDelegate.mm`과 병합해야 합니다.
{% endtab %}
{% endtabs %}

## Unity 패키지 커스터마이징 {#customizing-the-unity-package}

### 1단계: 리포지토리 복제 {#step-1-clone-the-repository}

터미널에서 [Braze Unity SDK GitHub 리포지토리](https://github.com/braze-inc/braze-unity-sdk)를 복제한 다음 해당 폴더로 이동합니다:

{% tabs local %}
{% tab MacOS %}
```bash
git clone git@github.com:braze-inc/braze-unity-sdk.git
cd ~/PATH/TO/DIRECTORY/braze-unity-sdk
```
{% endtab %}

{% tab Windows Powershell %}
```powershell
git clone git@github.com:braze-inc/braze-unity-sdk.git
cd C:\PATH\TO\DIRECTORY\braze-unity-sdk
```
{% endtab %}
{% endtabs %}

### 2단계: 리포지토리에서 패키지 내보내기 {#step-2-export-package-from-repository}

먼저 Unity를 실행하고 백그라운드에서 계속 실행합니다. 그런 다음 리포지토리 루트에서 다음 명령을 실행하여 패키지를 `braze-unity-sdk/unity-package/`로 내보냅니다.

{% tabs local %}
{% tab MacOS %}
```bash
/Applications/Unity/Unity.app/Contents/MacOS/Unity -batchmode -nographics -projectPath "$(pwd)" -executeMethod Appboy.Editor.Build.ExportAllPackages -quit
```
{% endtab %}

{% tab Windows Powershell %}
```powershell
"%UNITY_PATH%" -batchmode -nographics -projectPath "%PROJECT_ROOT%" -executeMethod Appboy.Editor.Build.ExportAllPackages -quit
```
{% endtab %}
{% endtabs %}

{% alert tip %}
이러한 명령을 실행한 후 문제가 발생하면 [Unity: 명령줄 인수](https://docs.unity3d.com/2017.2/Documentation/Manual/CommandLineArguments.html)를 참조하세요.
{% endalert %}

### 3단계: Unity로 패키지 가져오기 {#step-3-import-package-into-unity}

1. Unity에서 **Assets** > **Import Package** > **Custom Package**로 이동하여 원하는 패키지를 Unity 프로젝트로 가져옵니다.
2. 가져오지 않으려는 파일이 있다면 지금 선택을 해제하세요.
3. `Assets/Editor/Build.cs`에 있는 내보낸 Unity 패키지를 커스터마이징합니다.

## 자동화된 통합으로 전환(Swift만 해당) {#automated-integration}

Braze Unity SDK에서 제공하는 자동화된 iOS 통합을 활용하려면 수동 통합에서 자동 통합으로 전환하는 다음 단계를 따르세요.

1. Xcode 프로젝트의 `UnityAppController` 서브클래스에서 모든 Braze 관련 코드를 제거합니다.
2. Unity 또는 Xcode 프로젝트에서 Braze iOS 라이브러리를 제거합니다(예: `Appboy_iOS_SDK.framework` 및 `SDWebImage.framework`).
3. Braze Unity 패키지를 프로젝트에 다시 가져옵니다. 전체 안내는 [2단계: 패키지 가져오기](#unity_step-2-import-the-package)를 참조하세요.
4. API 키를 다시 설정합니다. 전체 안내는 [3.1단계: API 키 설정](#unity_step-31-set-your-api-key)을 참조하세요.

## 선택적 구성 {#optional-configurations}

### 상세 로깅 {#verbose-logging}

Unity 편집기에서 상세 로깅을 활성화하려면 다음을 수행합니다:

1. **Braze** > **Braze Configuration**으로 이동하여 Braze 구성 설정을 엽니다.
2. **Show Braze Android Settings** 드롭다운을 클릭합니다.
3. **SDK Log Level** 필드에 "0" 값을 입력합니다.

### Prime 31 호환성 {#prime-31-compatibility}

Prime31 플러그인과 함께 Braze Unity 플러그인을 사용하려면 프로젝트의 `AndroidManifest.xml`을 편집하여 Prime31 호환 액티비티 클래스를 사용합니다.
`com.braze.unity.BrazeUnityPlayerActivity`의 모든 참조를 `com.braze.unity.prime31compatible.BrazeUnityPlayerActivity`로 변경하세요.

### Amazon Device Messaging(ADM) {#amazon-device-messaging-adm}

Braze는 Unity 앱에 [ADM 푸시](https://developer.amazon.com/public/apis/engage/device-messaging) 통합을 지원합니다. ADM 푸시를 통합하려면 ADM API 키가 포함된 `api_key.txt` 파일을 만들어 `Plugins/Android/assets/` 폴더에 넣으세요. ADM을 Braze와 통합하는 방법에 대한 자세한 내용은 [ADM 푸시 통합 지침]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=unity)을 참조하세요.

### Braze Unity 플레이어 확장(Android만 해당) {#extend-unity-player}

제공된 예제 `AndroidManifest.xml` 파일에는 하나의 액티비티 클래스([`BrazeUnityPlayerActivity`](https://github.com/braze-inc/braze-android-sdk/blob/e804cb3a10ae68364b354b52abf1bef8a0d1a9dc/android-sdk-unity/src/main/java/com/braze/unity/BrazeUnityPlayerActivity.kt))가 등록되어 있습니다. 이 클래스는 Braze SDK와 통합되어 있으며 세션 처리, 인앱 메시지 등록, 푸시 알림 분석 로깅 등의 기능으로 `UnityPlayerActivity`를 확장합니다. `UnityPlayerActivity` 클래스 확장에 대한 자세한 내용은 [Unity](https://docs.unity3d.com/Manual/AndroidUnityPlayerActivity.html)를 참조하세요.

라이브러리 또는 플러그인 프로젝트에서 커스텀 `UnityPlayerActivity`를 만드는 경우, 커스텀 기능을 Braze와 통합하려면 `BrazeUnityPlayerActivity`를 확장해야 합니다. `BrazeUnityPlayerActivity` 확장 작업을 시작하기 전에 Unity 프로젝트에 Braze를 통합하기 위한 지침을 따르세요.

1. [Braze Android SDK 통합 지침]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)에서 설명한 대로 라이브러리 또는 플러그인 프로젝트에 Braze Android SDK를 종속성으로 추가합니다.
2. Unity 전용 기능이 포함된 Unity `.aar`을 Unity용으로 빌드 중인 Android 라이브러리 프로젝트에 통합합니다. `appboy-unity.aar`은 [공개 리포지토리](https://github.com/braze-inc/braze-unity-sdk/tree/master/Assets/Plugins/Android)에서 사용할 수 있습니다. Unity 라이브러리가 성공적으로 통합되면 `BrazeUnityPlayerActivity`를 확장하도록 `UnityPlayerActivity`를 수정합니다.
3. 라이브러리 또는 플러그인 프로젝트를 내보내고 평소처럼 `/<your-project>/Assets/Plugins/Android`에 넣습니다. Braze 소스 코드는 이미 `/<your-project>/Assets/Plugins/Android`에 있으므로 라이브러리나 플러그인에 포함하지 마세요.
4. `/<your-project>/Assets/Plugins/Android/AndroidManifest.xml`을 수정하여 `BrazeUnityPlayerActivity` 서브클래스를 메인 액티비티로 지정합니다.

이제 Braze와 완전히 통합되고 커스텀 `UnityPlayerActivity` 기능이 포함된 `.apk`를 Unity IDE에서 패키징할 수 있습니다.

## 문제 해결 {#troubleshooting}

### 오류: "File could not be read" {#error-file-could-not-be-read}

다음과 유사한 오류는 안전하게 무시해도 됩니다. Apple 소프트웨어는 Unity가 인식하지 못하는 CgBI라는 독점 PNG 확장을 사용합니다. 이러한 오류는 iOS 빌드나 Braze 번들에서 관련 이미지의 올바른 표시에 영향을 미치지 않습니다.

```
Could not create texture from Assets/Plugins/iOS/AppboyKit/Appboy.bundle/...png: File could not be read
```
