## Android SDK 통합하기 {#integrating-the-android-sdk}

### 1단계: Gradle 빌드 설정 업데이트 {#step-1-update-your-gradle-build-configuration}

프로젝트의 리포지토리 설정(예: `settings.gradle`, `settings.gradle.kts` 또는 최상위 `build.gradle`)에서 리포지토리 목록에 [`mavenCentral()`](https://docs.gradle.org/current/kotlin-dsl/gradle/org.gradle.api.artifacts.dsl/-repository-handler/maven-central.html)을 추가합니다. 이 구문은 Groovy와 Kotlin DSL 모두 동일합니다.

```groovy
repositories {
  mavenCentral()
}
```

다음으로 Braze를 의존성에 추가합니다. 아래 예시에서 `SDK_VERSION`을 현재 사용 중인 Android Braze SDK 버전으로 대체하세요. 전체 버전 목록은 [체인지로그]({{site.baseurl}}/developer_guide/changelogs/?sdktab=android)를 참조하세요.

{% alert note %}
- Kotlin DSL(`build.gradle.kts`)의 경우 `implementation("...")` 구문을 사용합니다.
- Groovy(`build.gradle`)의 경우 `implementation '...'` 구문을 사용합니다.
- [버전 카탈로그](https://developer.android.com/build/migrate-to-catalogs)의 경우 `gradle/libs.versions.toml` 파일에 항목을 추가하고 생성된 접근자를 사용하여 참조합니다.
{% endalert %}

{% tabs local %}
{% tab base only %}
Braze UI 컴포넌트를 사용할 계획이 없는 경우 다음을 의존성에 추가합니다.

{% subtabs local %}
{% subtab Groovy %}
```groovy
dependencies {
    implementation 'com.braze:android-sdk-base:SDK_VERSION' // (Required) Adds dependencies for the base Braze SDK.
    implementation 'com.braze:android-sdk-location:SDK_VERSION' // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% subtab Kotlin DSL %}
```kotlin
dependencies {
    implementation("com.braze:android-sdk-base:SDK_VERSION") // (Required) Adds dependencies for the base Braze SDK.
    implementation("com.braze:android-sdk-location:SDK_VERSION") // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% subtab Version catalog %}
`gradle/libs.versions.toml` 파일에 다음을 추가합니다:

```toml
[versions]
braze = "SDK_VERSION"

[libraries]
braze-android-sdk-base = { group = "com.braze", name = "android-sdk-base", version.ref = "braze" }
braze-android-sdk-location = { group = "com.braze", name = "android-sdk-location", version.ref = "braze" }
```

그런 다음 `build.gradle` 또는 `build.gradle.kts` 파일에 다음 의존성을 추가합니다. 이 구문은 Groovy와 Kotlin DSL 모두 동일합니다.

```groovy
dependencies {
    implementation(libs.braze.android.sdk.base) // (Required) Adds dependencies for the base Braze SDK.
    implementation(libs.braze.android.sdk.location) // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab with ui components %}
Braze UI 컴포넌트를 사용할 계획인 경우 다음을 의존성에 추가합니다.

{% subtabs local %}
{% subtab Groovy %}
```groovy
dependencies {
    implementation 'com.braze:android-sdk-ui:SDK_VERSION' // (Required) Adds dependencies for the Braze SDK and Braze UI components.
    implementation 'com.braze:android-sdk-location:SDK_VERSION' // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% subtab Kotlin DSL %}
```kotlin
dependencies {
    implementation("com.braze:android-sdk-ui:SDK_VERSION") // (Required) Adds dependencies for the Braze SDK and Braze UI components.
    implementation("com.braze:android-sdk-location:SDK_VERSION") // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% subtab Version catalog %}
`gradle/libs.versions.toml` 파일에 다음을 추가합니다:

```toml
[versions]
braze = "SDK_VERSION"

[libraries]
braze-android-sdk-ui = { group = "com.braze", name = "android-sdk-ui", version.ref = "braze" }
braze-android-sdk-location = { group = "com.braze", name = "android-sdk-location", version.ref = "braze" }
```

그런 다음 `build.gradle` 또는 `build.gradle.kts` 파일에 다음 의존성을 추가합니다. 이 구문은 Groovy와 Kotlin DSL 모두 동일합니다.

```groovy
dependencies {
    implementation(libs.braze.android.sdk.ui) // (Required) Adds dependencies for the Braze SDK and Braze UI components.
    implementation(libs.braze.android.sdk.location) // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### 2단계: `braze.xml` 설정 {#step-2-configure-your-brazexml}

{% alert note %}
2019년 12월부터 커스텀 엔드포인트는 더 이상 제공되지 않습니다. 기존에 커스텀 엔드포인트가 있는 경우 계속 사용할 수 있습니다. 자세한 내용은 <a href="{{site.baseurl}}/api/basics/#endpoints">사용 가능한 엔드포인트 목록</a> 을 참조하세요.
{% endalert %}

프로젝트의 `res/values` 폴더에 `braze.xml` 파일을 생성합니다. 특정 데이터 클러스터를 사용하거나 기존에 커스텀 엔드포인트가 있는 경우 `braze.xml` 파일에 엔드포인트도 지정해야 합니다.

해당 파일의 내용은 다음 코드 스니펫과 유사해야 합니다. `YOUR_APP_IDENTIFIER_API_KEY`를 Braze 대시보드의 **설정 관리** 페이지에서 확인한 식별자로 대체하세요. [dashboard.braze.com](https://dashboard.braze.com)에 로그인하여 [클러스터 주소]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)를 확인하세요.

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

### 3단계: `AndroidManifest.xml`에 권한 추가 {#step-3-add-permissions-to-androidmanifestxml}

다음으로 `AndroidManifest.xml`에 다음 권한을 추가합니다:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert note %}
Android M 출시와 함께, Android는 설치 시 권한 모델에서 런타임 권한 모델로 전환했습니다. 하지만 이 두 권한은 일반 권한이며, 앱 매니페스트에 나열되어 있으면 자동으로 부여됩니다. 자세한 내용은 Android의 [권한 문서](https://developer.android.com/training/permissions/index.html)를 참조하세요.
{% endalert %}

### 4단계: 지연 초기화 활성화 (선택 사항) {#step-4-enable-delayed-initialization-optional}

지연 초기화를 사용하려면 다음 최소 Braze SDK 버전이 필요합니다:

{% sdk_min_versions android:38.0.0 %}

{% alert note %}
지연 초기화가 활성화된 동안에는 모든 네트워크 연결이 취소되어 SDK가 Braze 서버로 데이터를 전송하지 않습니다.
{% endalert %}

#### 4.1단계: `braze.xml` 업데이트 {#step-41-update-your-brazexml}

지연 초기화는 기본적으로 비활성화되어 있습니다. 활성화하려면 다음 옵션 중 하나를 사용하세요:

{% tabs %}
{% tab Braze XML 파일 %}
프로젝트의 `braze.xml` 파일에서 `com_braze_enable_delayed_initialization`을 `true`로 설정합니다.

```xml
<bool name="com_braze_enable_delayed_initialization">true</bool>
```
{% endtab %}

{% tab 런타임 %}
런타임에서 지연 초기화를 활성화하려면 다음 메서드를 사용합니다.

{% subtabs %}
{% subtab JAVA %}

```java
Braze.enableDelayedInitialization(context);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert note %}
지연 초기화가 활성화된 상태에서 푸시 알림에 딥링크 동작이 포함되어 있으면 딥링크가 해석되지 않습니다.
{% endalert %}

#### 4.2단계: 푸시 분석 설정 (선택 사항) {#step-42-configure-push-analytics-optional}

지연 초기화가 활성화되면 푸시 분석은 기본적으로 대기열에 추가됩니다. 하지만 푸시 분석을 [명시적으로 대기열에 추가](#explicitly-queue-push-analytics)하거나 [삭제](#drop-push-analytics)하도록 선택할 수도 있습니다.

##### 명시적으로 대기열에 추가 {#explicitly-queue-push-analytics}

푸시 분석을 명시적으로 대기열에 추가하려면 다음 옵션 중 하나를 선택합니다:

{% tabs %}
{% tab Braze XML 파일 %}
`braze.xml` 파일에서 `com_braze_delayed_initialization_analytics_behavior`를 `QUEUE`로 설정합니다:

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">QUEUE</string>
```
{% endtab %}

{% tab 런타임 %}
[`Braze.enableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-delayed-initialization.html) 메서드에 `QUEUE`를 추가합니다:

{% subtabs %}
{% subtab JAVA %}

```java
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.QUEUE);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.QUEUE)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

##### 삭제 {#drop-push-analytics}

푸시 분석을 삭제하려면 다음 옵션 중 하나를 선택합니다:

{% tabs %}
{% tab Braze XML 파일 %}
`braze.xml` 파일에서 `com_braze_delayed_initialization_analytics_behavior`를 `DROP`으로 설정합니다:

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">DROP</string>
```
{% endtab %}

{% tab 런타임 %}
[`Braze.enableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-delayed-initialization.html) 메서드에 `DROP`을 추가합니다:

{% subtabs %}
{% subtab JAVA %}

```java
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.DROP);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.DROP)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### 4.3단계: SDK 수동 초기화 {#step-43-manually-initialize-the-sdk}

선택한 지연 기간이 지난 후 [`Braze.disableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-delayed-initialization.html) 메서드를 사용하여 SDK를 수동으로 초기화합니다.

{% tabs local %}
{% tab JAVA %}

```java
Braze.disableDelayedInitialization(context);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.disableDelayedInitialization(context)
```

{% endtab %}
{% endtabs %}

### 5단계: 사용자 세션 추적 활성화 {#step-5-enable-user-session-tracking}

사용자 세션 추적을 활성화하면 `openSession()`, `closeSession()`, [`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html) 호출 및 `InAppMessageManager` 등록이 자동으로 처리됩니다.

액티비티 라이프사이클 콜백을 등록하려면 `Application` 클래스의 `onCreate()` 메서드에 다음 코드를 추가합니다.

{% tabs local %}
{% tab JAVA %}

```java
public class MyApplication extends Application {
  @Override
  public void onCreate() {
    super.onCreate();
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class MyApplication : Application() {
  override fun onCreate() {
    super.onCreate()
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
  }
}
```

사용 가능한 매개변수 목록은 [`BrazeActivityLifecycleCallbackListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html)를 참조하세요.

{% endtab %}
{% endtabs %}

## 세션 추적 테스트 {#testing-session-tracking}

{% alert tip %}
[SDK 디버거]({{site.baseurl}}/developer_guide/debugging)를 사용하여 SDK 문제를 진단할 수도 있습니다.
{% endalert %}

테스트 중 문제가 발생하면 [상세 로깅](#android_enabling-logs)을 활성화한 다음, logcat을 사용하여 액티비티에서 누락된 `openSession` 및 `closeSession` 호출을 감지하세요.

1. Braze에서 **개요**로 이동하여 앱을 선택한 다음, **Display Data For** 드롭다운에서 **Today**를 선택합니다.
    ![Braze의 "개요" 페이지에서 "Display Data For" 필드가 "Today"로 설정된 모습.]({% image_buster /assets/img_archive/android_sessions.png %})
2. 앱을 열고 Braze 대시보드를 새로고침합니다. 측정기준이 1만큼 증가했는지 확인합니다.
3. 앱 내에서 이동하며 Braze에 하나의 세션만 기록되었는지 확인합니다.
4. 앱을 최소 10초 이상 백그라운드로 보낸 다음 다시 포그라운드로 가져옵니다. 새로운 세션이 기록되었는지 확인합니다.

## 선택적 구성 {#optional-configurations}

### 런타임 구성 {#runtime-configuration}

Braze 옵션을 `braze.xml` 파일 대신 코드에서 설정하려면 [런타임 구성](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html)을 사용하세요. 두 곳 모두에 값이 존재하는 경우 런타임 값이 우선 적용됩니다. 필요한 모든 설정이 런타임에 제공되면 `braze.xml` 파일을 삭제할 수 있습니다.

다음 예시에서는 [빌더 객체](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html)를 생성한 다음 [`Braze.configure()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html)에 전달합니다. 사용 가능한 런타임 옵션 중 일부만 표시됩니다&#8212;전체 목록은 [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html)을 참조하세요.

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
        .setApiKey("api-key-here")
        .setCustomEndpoint("YOUR_CUSTOM_ENDPOINT_OR_CLUSTER")
        .setSessionTimeout(60)
        .setHandlePushDeepLinksAutomatically(true)
        .setGreatNetworkDataFlushInterval(10)
        .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setApiKey("api-key-here")
        .setCustomEndpoint("YOUR_CUSTOM_ENDPOINT_OR_CLUSTER")
        .setSessionTimeout(60)
        .setHandlePushDeepLinksAutomatically(true)
        .setGreatNetworkDataFlushInterval(10)
        .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

{% alert tip %}
다른 예시를 찾고 계신가요? [Hello Braze 샘플 앱](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/hello-braze/src/main/java/com/braze/helloworld/CustomApplication.java)을 확인해 보세요.
{% endalert %}

### Google 광고 ID {#google-advertising-id}

[Google 광고 ID(GAID)](https://support.google.com/googleplay/android-developer/answer/6048248/advertising-id?hl=en)는 Google Play 서비스에서 제공하는 선택적이고, 사용자별이며, 익명이고, 고유하며, 재설정 가능한 광고용 ID입니다. GAID를 통해 사용자는 식별자를 재설정하고, Google Play 앱 내에서 관심 기반 광고를 차단할 수 있으며, 개발자에게는 앱 수익 창출을 지속할 수 있는 간단하고 표준적인 시스템을 제공합니다.

Google 광고 ID는 Braze SDK에서 자동으로 수집되지 않으며 [`Braze.setGoogleAdvertisingId()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html) 메서드를 통해 수동으로 설정해야 합니다.

{% tabs local %}
{% tab JAVA %}

```java
new Thread(new Runnable() {
  @Override
  public void run() {
    try {
      AdvertisingIdClient.Info idInfo = AdvertisingIdClient.getAdvertisingIdInfo(getApplicationContext());
      Braze.getInstance(getApplicationContext()).setGoogleAdvertisingId(idInfo.getId(), idInfo.isLimitAdTrackingEnabled());
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}).start();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
suspend fun fetchAndSetAdvertisingId(
  context: Context,
  scope: CoroutineScope = GlobalScope
) {
  scope.launch(Dispatchers.IO) {
    try {
      val idInfo = AdvertisingIdClient.getAdvertisingIdInfo(context)
      Braze.getInstance(context).setGoogleAdvertisingId(
        idInfo.id,
        idInfo.isLimitAdTrackingEnabled
      )
    } catch (e: Exception) {
      e.printStackTrace()
    }
  }
}
```

{% endtab %}
{% endtabs %}

{% alert important %}
Google은 광고 ID를 UI가 아닌 스레드에서 수집하도록 요구합니다.
{% endalert %}


### 위치 추적 {#location-tracking}

Braze 위치 수집을 활성화하려면 `braze.xml` 파일에서 `com_braze_enable_location_collection`을 `true`로 설정합니다:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
Braze Android SDK 버전 3.6.0부터 Braze 위치 수집은 기본적으로 비활성화되어 있습니다.
{% endalert %}

### 로깅 {#logging}

기본적으로 Braze Android SDK 로그 레벨은 `INFO`로 설정되어 있습니다. 이러한 로그를 [억제](#android_suppressing-logs)하거나 `VERBOSE`, `DEBUG`, `WARN` 등 [다른 로그 레벨을 설정](#android_enabling-logs)할 수 있습니다.

#### 로그 활성화 {#enabling-logs}

앱의 문제를 해결하거나 Braze 지원팀과의 처리 시간을 단축하기 위해 SDK에 대해 상세 로그를 활성화할 수 있습니다. Braze 지원팀에 상세 로그를 전송할 때는 애플리케이션을 실행하자마자 로그가 시작되고 문제가 발생한 후 충분히 지나서 종료되도록 해야 합니다. 중앙 집중식 개요는 [상세 로깅]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)을 참조하세요. 로그 출력을 해석하는 방법은 [상세 로그 읽기]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs)를 참조하세요.

상세 로그는 개발 환경에서만 사용하도록 되어 있으므로 앱을 출시하기 전에 비활성화해야 합니다.

{% alert important %}
로그가 최대한 완전하게 기록되도록 `Application.onCreate()`에서 다른 호출보다 먼저 상세 로그를 활성화하세요.
{% endalert %}

{% tabs local %}
{% tab 애플리케이션 %}
앱에서 직접 로그를 활성화하려면 다른 메서드보다 먼저 애플리케이션의 `onCreate()` 메서드에 다음을 추가합니다.

{% subtabs local %}
{% subtab JAVA %}
```java
BrazeLogger.setLogLevel(Log.MIN_LOG_LEVEL);
```
{% endsubtab %}

{% subtab KOTLIN %}
```kotlin
BrazeLogger.logLevel = Log.MIN_LOG_LEVEL
```
{% endsubtab %}
{% endsubtabs %}

`MIN_LOG_LEVEL`을 최소 로그 레벨로 설정하려는 로그 레벨의 **상수**로 대체합니다. 설정한 `MIN_LOG_LEVEL` 이상(`>=`)의 로그는 Android의 기본 [`Log`](https://developer.android.com/reference/android/util/Log) 메서드로 전달됩니다. 설정한 `MIN_LOG_LEVEL` 미만(`<`)의 로그는 버려집니다.

| 상수 | 값 | 설명 |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE` | 2 | 디버깅 및 개발을 위한 가장 상세한 메시지를 기록합니다. |
| `DEBUG` | 3 | 디버깅 및 개발을 위한 설명 메시지를 기록합니다. |
| `INFO` | 4 | 일반적인 주요 사항에 대한 정보 메시지를 기록합니다. |
| `WARN` | 5 | 잠재적으로 유해한 상황을 식별하기 위한 경고 메시지를 기록합니다. |
| `ERROR` | 6 | 애플리케이션 실패 또는 심각한 문제를 나타내는 오류 메시지를 기록합니다. |
| `ASSERT` | 7 | 개발 중 조건이 거짓일 때 어서션 메시지를 기록합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="로그 활성화" }

예를 들어, 다음 코드는 로그 레벨 `2`, `3`, `4`, `5`, `6`, `7`을 `Log` 메서드로 전달합니다.

{% subtabs local %}
{% subtab JAVA %}
```java
BrazeLogger.setLogLevel(Log.VERBOSE);
```
{% endsubtab %}

{% subtab KOTLIN %}
```kotlin
BrazeLogger.logLevel = Log.VERBOSE
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab xml %}
`braze.xml`에서 로그를 활성화하려면 파일에 다음을 추가합니다:

```xml
<integer name="com_braze_logger_initial_log_level">MIN_LOG_LEVEL</integer>
```

`MIN_LOG_LEVEL`을 최소 로그 레벨로 설정하려는 로그 레벨의 **값**으로 대체합니다. 설정한 `MIN_LOG_LEVEL` 이상(`>=`)의 로그는 Android의 기본 [`Log`](https://developer.android.com/reference/android/util/Log) 메서드로 전달됩니다. 설정한 `MIN_LOG_LEVEL` 미만(`<`)의 로그는 버려집니다.

| 상수 | 값 | 설명 |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE` | 2 | 디버깅 및 개발을 위한 가장 상세한 메시지를 기록합니다. |
| `DEBUG` | 3 | 디버깅 및 개발을 위한 설명 메시지를 기록합니다. |
| `INFO` | 4 | 일반적인 주요 사항에 대한 정보 메시지를 기록합니다. |
| `WARN` | 5 | 잠재적으로 유해한 상황을 식별하기 위한 경고 메시지를 기록합니다. |
| `ERROR` | 6 | 애플리케이션 실패 또는 심각한 문제를 나타내는 오류 메시지를 기록합니다. |
| `ASSERT` | 7 | 개발 중 조건이 거짓일 때 어서션 메시지를 기록합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="로그 활성화" }

예를 들어, 다음 코드는 로그 레벨 `2`, `3`, `4`, `5`, `6`, `7`을 `Log` 메서드로 전달합니다.

```xml
<integer name="com_braze_logger_initial_log_level">2</integer>
```
{% endtab %}
{% endtabs %}

#### 상세 로그 확인 {#verifying-verbose-logs}

로그가 `VERBOSE`로 설정되었는지 확인하려면 로그에 `V/Braze`가 나타나는지 확인합니다. 나타난다면 상세 로그가 성공적으로 활성화된 것입니다. 예를 들면:

```
2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Request started
```

#### 로그 억제 {#suppressing-logs}

Braze Android SDK의 모든 로그를 억제하려면 애플리케이션의 `onCreate()` 메서드에서 다른 메서드보다 _먼저_ 로그 레벨을 `BrazeLogger.SUPPRESS`로 설정합니다.

{% tabs local %}
{% tab JAVA %}
```java
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS);
```
{% endtab %}

{% tab KOTLIN %}
```kotlin
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS)
```
{% endtab %}
{% endtabs %}

### 다중 API 키 {#multiple-api-keys}

다중 API 키의 가장 일반적인 사용 사례는 디버그와 릴리스 빌드 배리언트에 대해 API 키를 분리하는 것입니다.

빌드에서 다중 API 키를 쉽게 전환하려면 각 관련 [빌드 배리언트](https://developer.android.com/studio/build/build-variants.html)에 대해 별도의 `braze.xml` 파일을 생성하는 것이 좋습니다. 빌드 배리언트는 빌드 유형과 제품 플레이버의 조합입니다. 기본적으로 새 Android 프로젝트는 [`debug` 및 `release` 빌드 유형](https://developer.android.com/reference/tools/gradle-api/8.3/null/com/android/build/api/dsl/BuildType)으로 구성되며 제품 플레이버는 없습니다.

각 관련 빌드 배리언트에 대해 `src/<build variant name>/res/values/` 디렉토리에 새 `braze.xml`을 생성합니다. 빌드 배리언트가 컴파일되면 새 API 키가 사용됩니다.

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```

{% alert tip %}
코드에서 API 키를 설정하는 방법은 [런타임 구성]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#runtime-configuration)을 참조하세요.
{% endalert %}

### 인앱 메시지 전용 TalkBack {#exclusive-in-app-message-talkback}

[Android 접근성 가이드라인](https://developer.android.com/guide/topics/ui/accessibility)에 따라 Braze Android SDK는 기본적으로 Android TalkBack을 제공합니다. 앱 타이틀 바나 내비게이션 같은 다른 화면 요소를 포함하지 않고 인앱 메시지의 콘텐츠만 음성으로 읽히도록 하려면 TalkBack의 배타적 모드를 활성화할 수 있습니다.

인앱 메시지에 대한 배타적 모드를 활성화하려면:

{% tabs local %}
{% tab Braze XML %}
```xml
<bool name="com_braze_device_in_app_message_accessibility_exclusive_mode_enabled">true</bool>
```
{% endtab %}

{% tab Kotlin %}
```kotlin
val brazeConfigBuilder = BrazeConfig.Builder()
brazeConfigBuilder.setIsInAppMessageAccessibilityExclusiveModeEnabled(true)
Braze.configure(this, brazeConfigBuilder.build())
```
{% endtab %}

{% tab Java %}
```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
brazeConfigBuilder.setIsInAppMessageAccessibilityExclusiveModeEnabled(true);
Braze.configure(this, brazeConfigBuilder.build());
```
{% endtab %}
{% endtabs %}

### R8 및 ProGuard {#r8-and-proguard}

[코드 축소](https://developer.android.com/build/shrink-code) 구성은 Braze 통합에 자동으로 포함됩니다.

Braze 코드를 난독화하는 클라이언트 앱은 Braze가 스택 트레이스를 해석할 수 있도록 릴리스 매핑 파일을 저장해야 합니다. 모든 Braze 코드를 계속 유지하려면 ProGuard 파일에 다음을 추가하세요:

```
-keep class bo.app.** { *; }
-keep class com.braze.** { *; }
```
