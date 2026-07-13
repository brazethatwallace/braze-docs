{% multi_lang_include developer_guide/prerequisites/android.md %}

## 지오펜스 설정 {#setting-up-geofences}

### 1단계: Braze에서 활성화 {#step-1-enable-in-braze}

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### 2단계: `build.gradle` 업데이트 {#step-2-update-buildgradle}

앱 수준 `build.gradle`에 `android-sdk-location`을 추가합니다. 또한 Google Play 서비스 [설정 가이드](https://developers.google.com/android/guides/setup)를 사용하여 Google Play 서비스 [위치 패키지](https://developers.google.com/android/reference/com/google/android/gms/location/package-summary)를 추가합니다.

```
dependencies {
  implementation "com.braze:android-sdk-location:+"
  implementation "com.google.android.gms:play-services-location:${PLAY_SERVICES_VERSION}"
}
```

### 3단계: 매니페스트 업데이트 {#step-3-update-the-manifest}

`AndroidManifest.xml`에 부팅, 정밀 위치 및 백그라운드 위치 권한을 추가합니다.

```xml
<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
```

{% alert important %}
백그라운드 위치 접근 권한은 Android 10에 추가되었으며, 모든 Android 10 이상 기기에서 앱이 백그라운드에 있는 동안 지오펜스가 작동하는 데 필요합니다.
{% endalert %}

`AndroidManifest.xml`의 `application` 요소에 Braze 부트 리시버를 추가합니다:

```xml
<receiver android:name="com.braze.BrazeBootReceiver">
  <intent-filter>
    <action android:name="android.intent.action.BOOT_COMPLETED" />
  </intent-filter>
</receiver>
```

### 4단계: Braze 위치 수집 활성화 {#step-4-enable-braze-location-collection}

아직 Braze 위치 수집을 활성화하지 않았다면 `braze.xml` 파일을 업데이트하여 `com_braze_enable_location_collection`을 포함하고 해당 값이 `true`로 설정되어 있는지 확인합니다.

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
Braze Android SDK 버전 3.6.0부터 Braze 위치 수집은 기본적으로 비활성화되어 있습니다.
{% endalert %}

Braze 위치 수집이 활성화되어 있으면 Braze 지오펜스도 활성화됩니다. 기본 위치 수집은 옵트아웃하되 지오펜스는 계속 사용하고 싶다면, `braze.xml`에서 `com_braze_geofences_enabled` 키의 값을 `true`로 설정하여 `com_braze_enable_location_collection` 값과 독립적으로 선택적 활성화할 수 있습니다.

```xml
<bool name="com_braze_geofences_enabled">true</bool>
```

### 5단계: 최종 사용자로부터 위치 권한 얻기 {#step-5-obtain-location-permissions-from-the-end-user}

Android M 이상 버전에서는 위치 정보를 수집하거나 지오펜스를 등록하기 전에 최종 사용자에게 위치 권한을 요청해야 합니다.

사용자가 앱에 위치 권한을 부여할 때 Braze에 알리려면 다음 호출을 추가하세요:

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).requestLocationInitialization();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).requestLocationInitialization()
```

{% endtab %}
{% endtabs %}

이렇게 하면 SDK가 Braze 서버에 지오펜스를 요청하고 지오펜스 추적을 초기화합니다.

예제 구현은 샘플 애플리케이션의 [`RuntimePermissionUtils.java`](https://github.com/braze-inc/braze-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/util/RuntimePermissionUtils.kt)를 참조하세요.

{% tabs %}
{% tab JAVA %}

```java
public class RuntimePermissionUtils {
  private static final String TAG = BrazeLogger.getBrazeLogTag(RuntimePermissionUtils.class);
  public static final int DROIDBOY_PERMISSION_LOCATION = 40;

  public static void handleOnRequestPermissionsResult(Context context, int requestCode, int[] grantResults) {
    switch (requestCode) {
      case DROIDBOY_PERMISSION_LOCATION:
        // In Android Q, we require both FINE and BACKGROUND location permissions. Both
        // are requested simultaneously.
        if (areAllPermissionsGranted(grantResults)) {
          Log.i(TAG, "Required location permissions granted.");
          Toast.makeText(context, "Required location permissions granted.", Toast.LENGTH_SHORT).show();
          Braze.getInstance(context).requestLocationInitialization();
        } else {
          Log.i(TAG, "Required location permissions NOT granted.");
          Toast.makeText(context, "Required location permissions NOT granted.", Toast.LENGTH_SHORT).show();
        }
        break;
      default:
        break;
    }
  }

  private static boolean areAllPermissionsGranted(int[] grantResults) {
    for (int grantResult : grantResults) {
      if (grantResult != PackageManager.PERMISSION_GRANTED) {
        return false;
      }
    }
    return true;
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
object RuntimePermissionUtils {
  private val TAG = BrazeLogger.getBrazeLogTag(RuntimePermissionUtils::class.java!!)
  val DROIDBOY_PERMISSION_LOCATION = 40

  fun handleOnRequestPermissionsResult(context: Context, requestCode: Int, grantResults: IntArray) {
    when (requestCode) {
      DROIDBOY_PERMISSION_LOCATION ->
        // In Android Q, we require both FINE and BACKGROUND location permissions. Both
        // are requested simultaneously.
        if (areAllPermissionsGranted(grantResults)) {
          Log.i(TAG, "Required location permissions granted.")
          Toast.makeText(context, "Required location permissions granted.", Toast.LENGTH_SHORT).show()
          Braze.getInstance(context).requestLocationInitialization()
        } else {
          Log.i(TAG, "Required location permissions NOT granted.")
          Toast.makeText(context, "Required location permissions NOT granted.", Toast.LENGTH_SHORT).show()
        }
      else -> {
      }
    }
  }

  private fun areAllPermissionsGranted(grantResults: IntArray): Boolean {
    for (grantResult in grantResults) {
      if (grantResult != PackageManager.PERMISSION_GRANTED) {
        return false
      }
    }
    return true
  }
}
```

{% endtab %}
{% endtabs %}

위의 샘플 코드는 다음과 같이 사용합니다:

{% tabs %}
{% tab JAVA %}

```java
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
  if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
    boolean hasAllPermissions = PermissionUtils.hasPermission(getApplicationContext(), Manifest.permission.ACCESS_BACKGROUND_LOCATION)
        && PermissionUtils.hasPermission(getApplicationContext(), Manifest.permission.ACCESS_FINE_LOCATION);
    if (!hasAllPermissions) {
      // Request both BACKGROUND and FINE location permissions
      requestPermissions(new String[]{android.Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_BACKGROUND_LOCATION},
          RuntimePermissionUtils.DROIDBOY_PERMISSION_LOCATION);
    }
  } else {
    if (!PermissionUtils.hasPermission(getApplicationContext(), Manifest.permission.ACCESS_FINE_LOCATION)) {
      // Request only FINE location permission
      requestPermissions(new String[]{android.Manifest.permission.ACCESS_FINE_LOCATION},
          RuntimePermissionUtils.DROIDBOY_PERMISSION_LOCATION);
    }
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
  if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
    val hasAllPermissions = PermissionUtils.hasPermission(applicationContext, Manifest.permission.ACCESS_BACKGROUND_LOCATION)
        && PermissionUtils.hasPermission(applicationContext, Manifest.permission.ACCESS_FINE_LOCATION)
    if (!hasAllPermissions) {
      // Request both BACKGROUND and FINE location permissions
      requestPermissions(arrayOf(android.Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_BACKGROUND_LOCATION),
          RuntimePermissionUtils.DROIDBOY_PERMISSION_LOCATION)
    }
  } else {
    if (!PermissionUtils.hasPermission(applicationContext, Manifest.permission.ACCESS_FINE_LOCATION)) {
      // Request only FINE location permission
      requestPermissions(arrayOf(android.Manifest.permission.ACCESS_FINE_LOCATION),
          RuntimePermissionUtils.DROIDBOY_PERMISSION_LOCATION)
    }
  }
}
```

{% endtab %}
{% endtabs %}

### 6단계: 지오펜스 업데이트 수동 요청(선택 사항) {#step-6-manually-request-geofence-updates-optional}

기본적으로 Braze는 기기의 위치를 자동으로 검색하고 수집된 위치를 기반으로 지오펜스를 요청합니다. 그러나 근접한 Braze 지오펜스를 검색하는 데 사용할 GPS 좌표를 수동으로 제공할 수도 있습니다. Braze 지오펜스를 수동으로 요청하려면 자동 Braze 지오펜스 요청을 비활성화하고 요청에 사용할 GPS 좌표를 제공해야 합니다.

#### 6.1단계: 자동 지오펜스 요청 비활성화 {#step-61-disable-automatic-geofence-requests}

자동 Braze 지오펜스 요청은 `braze.xml` 파일에서 `com_braze_automatic_geofence_requests_enabled`를 `false`로 설정하여 비활성화할 수 있습니다.

```xml
<bool name="com_braze_automatic_geofence_requests_enabled">false</bool>
```

런타임에서도 다음과 같이 설정할 수 있습니다:

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
    .setAutomaticGeofenceRequestsEnabled(false);
Braze.configure(getApplicationContext(), brazeConfigBuilder.build());
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfigBuilder = BrazeConfig.Builder()
    .setAutomaticGeofenceRequestsEnabled(false)
Braze.configure(applicationContext, brazeConfigBuilder.build())
```

{% endtab %}
{% endtabs %}

#### 6.2단계: GPS 좌표로 Braze 지오펜스 수동 요청 {#step-62-manually-request-braze-geofence-with-gps-coordinate}

Braze 지오펜스는 [`requestGeofences()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-geofences.html) 메서드를 통해 수동으로 요청합니다:

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(getApplicationContext()).requestGeofences(latitude, longitude);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(applicationContext).requestGeofences(33.078947, -116.601356)
```

{% endtab %}
{% endtabs %}

{% alert important %}
지오펜스는 세션당 한 번만 요청할 수 있으며, SDK에 의해 자동으로 요청하거나 이 메서드를 사용하여 수동으로 요청할 수 있습니다.
{% endalert %}