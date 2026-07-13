{% multi_lang_include developer_guide/prerequisites/xamarin.md %}

## 필수 조건 {#prerequisites}

지오펜스를 사용하기 위해 필요한 최소 SDK 버전은 다음과 같습니다:

{% sdk_min_versions xamarin:9.0.0 %}

## 지오펜스 설정 {#setting-up-geofences}

### 1단계: Braze에서 활성화 {#step-1-enable-in-braze}

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

---

다음으로, Android 또는 iOS에 대한 플랫폼별 지침을 따르세요:

{% tabs %}
{% tab Android %}

### 2단계: 종속성 추가 {#step-2-add-dependencies}

다음 NuGet 패키지 참조를 프로젝트에 추가하세요:

- `BrazePlatform.BrazeAndroidLocationBinding`

### 3단계: AndroidManifest.xml 업데이트 {#step-3-update-your-androidmanifestxml}

다음 권한을 `AndroidManifest.xml`에 추가하세요:

```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
```

{% alert important %}
백그라운드 위치 접근 권한은 Android 10 이상 기기에서 앱이 백그라운드에 있는 동안 지오펜스가 작동하는 데 필요합니다.
{% endalert %}

### 4단계: Braze 위치 수집 구성 {#step-4-configure-braze-location-collection}

Braze 구성에서 위치 수집이 활성화되어 있는지 확인하세요. 자동 위치 수집 없이 지오펜스를 활성화하려면, `Braze.xml`에서 다음을 설정하세요:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
<bool name="com_braze_geofences_enabled">true</bool>
```

### 5단계: 런타임에 위치 권한 요청 {#step-5-request-location-permissions-at-runtime}

지오펜스를 등록하기 전에 사용자에게 위치 권한을 요청해야 합니다. C# 코드에서 다음 패턴을 사용하세요:

```csharp
using AndroidX.Core.App;
using AndroidX.Core.Content;

private void RequestLocationPermission()
{
  // ...existing code for checking and requesting permissions...
}

public override void OnRequestPermissionsResult(int requestCode, string[] permissions, Permission[] grantResults)
{
  // ...existing code for handling permission result...
}
```

권한이 부여된 후, Braze 위치 수집을 초기화하세요:

```csharp
Braze.GetInstance(this).RequestLocationInitialization();
```

### 6단계: 지오펜스 업데이트 수동 요청(선택 사항) {#step-6-manually-request-geofence-updates-optional}

특정 위치에 대한 지오펜스를 수동으로 요청하려면:

```csharp
Braze.GetInstance(this).RequestGeofences(latitude, longitude);
```

{% alert important %}
지오펜스는 세션당 한 번만 요청할 수 있으며, SDK에 의해 자동으로 요청하거나 이 메서드를 사용하여 수동으로 요청할 수 있습니다.
{% endalert %}
{% endtab %}
{% tab iOS %}

### 2단계: 종속성 추가

다음 NuGet 패키지 참조를 프로젝트에 추가하세요:

- `Braze.iOS.BrazeLocation`

### 3단계: Info.plist에서 위치 사용 구성 {#step-3-configure-location-usage-in-infoplist}

`Info.plist`에 위치 서비스에 대한 사용 설명 문자열을 추가하세요:

```xml
<key>NSLocationAlwaysAndWhenInUseUsageDescription</key>
<string>This app uses your location to enable geofences and location-based messaging.</string>
<key>NSLocationWhenInUseUsageDescription</key>
<string>This app uses your location to enable geofences and location-based messaging.</string>
```

{% alert important %}
Apple은 `NSLocationAlwaysUsageDescription`을 더 이상 지원하지 않습니다. iOS 14 이상에서는 위의 키를 사용하세요.
{% endalert %}

### 4단계: Braze 구성에서 지오펜스 활성화 {#step-4-enable-geofences-in-your-braze-configuration}

앱 시작 코드(예: `App.xaml.cs`)에서 지오펜스가 활성화된 상태로 Braze를 구성하세요:

```csharp
using BrazeKit;
using BrazeLocation;

var configuration = new BRZConfiguration("<BRAZE_API_KEY>", "<BRAZE_ENDPOINT>");
configuration.Location.BrazeLocationProvider = new BrazeLocationProvider();
configuration.Location.AutomaticLocationCollection = true;
configuration.Location.GeofencesEnabled = true;
configuration.Location.AutomaticGeofenceRequests = true;
// ...other configuration...
var braze = new Braze(configuration);
```

### 5단계: 백그라운드 위치 업데이트 활성화(선택 사항) {#step-5-enable-background-location-updates-optional}

백그라운드에서 지오펜스를 모니터링하려면, **Location updates** 백그라운드 모드를 활성화하고 다음 구성을 `Info.plist`에 추가하세요:

```xml
<key>UIBackgroundModes</key>
<array>
  <string>location</string>
</array>
```

그런 다음, Braze 구성에서 다음을 설정하세요:

```csharp
configuration.Location.AllowBackgroundGeofenceUpdates = true;
configuration.Location.DistanceFilter = 8000; // meters
```

{% alert important %}
배터리 소모를 방지하기 위해 `DistanceFilter`를 앱의 필요에 맞는 값으로 설정하세요.
{% endalert %}

### 6단계: 위치 권한 요청 {#step-6-request-location-authorization}

사용자에게 `When In Use` 또는 `Always` 권한을 요청하세요:

```csharp
using CoreLocation;

var locationManager = new CLLocationManager();
locationManager.RequestWhenInUseAuthorization();
// or
locationManager.RequestAlwaysAuthorization();
```

{% alert important %}
`Always` 권한이 없으면, iOS는 앱이 사용 중이지 않을 때 위치 서비스의 실행을 제한합니다. 이는 운영 체제에 의해 시행되며 Braze SDK로 우회할 수 없습니다.
{% endalert %}
{% endtab %}
{% endtabs %}