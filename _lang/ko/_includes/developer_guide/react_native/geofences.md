{% alert important %}
지오펜스는 React Native SDK에서 **iOS와 Android 모두** 지원됩니다. `requestLocationInitialization` 메서드는 Android 전용이며 iOS에서는 필요하지 않습니다. `requestGeofences` 메서드는 두 플랫폼 모두에서 사용할 수 있습니다. 기본적으로 SDK는 위치가 사용 가능할 때 자동으로 지오펜스를 요청하고 모니터링할 수 있습니다. 이 자동 구성에 의존하거나 `requestGeofences`를 호출하여 수동으로 요청할 수 있습니다.
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## 지오펜스 설정 {#setting-up-geofences}

### 1단계: Braze에서 활성화 {#step-1-enable-in-braze}

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### 2단계: 네이티브 Android 설정 완료 {#step-2-complete-native-android-setup}

React Native SDK는 네이티브 Braze Android SDK를 사용하므로, 프로젝트에 대한 네이티브 Android 지오펜스 설정을 완료하세요. 이 단계의 iOS에 해당하는 내용은 네이티브 Swift SDK 지오펜스 가이드([2.2단계에서 3.1단계]({{site.baseurl}}/developer_guide/geofences/?sdktab=swift#swift_step-21-add-the-brazelocation-module)에서 다루고 있습니다. 2.1단계(BrazeLocation 모듈 추가)는 BrazeLocation이 Braze React Native SDK에 이미 암묵적으로 포함되어 있으므로 React Native에서는 필요하지 않습니다.

1. **`build.gradle` 업데이트:** `android-sdk-location` 및 Google Play 서비스 위치를 추가하세요. [Android 지오펜스]({{site.baseurl}}/developer_guide/geofences/?sdktab=android)를 참조하세요.
2. **매니페스트 업데이트:** 위치 권한 및 Braze 부트 리시버를 추가하세요. [Android 지오펜스]({{site.baseurl}}/developer_guide/geofences/?sdktab=android)를 참조하세요.
3. **Braze 위치 수집 활성화:** `braze.xml` 파일을 업데이트하세요. [Android 지오펜스]({{site.baseurl}}/developer_guide/geofences/?sdktab=android)를 참조하세요.

### 3단계: 네이티브 iOS 설정 완료 {#step-3-complete-native-ios-setup}

React Native SDK는 네이티브 Braze iOS SDK를 사용하므로, 프로젝트에 대한 네이티브 iOS 지오펜스 설정을 완료하려면 2.2단계부터 시작하여 네이티브 Swift SDK 지침을 따르세요. `Info.plist`에 위치 사용 설명을 업데이트하고(2.2단계), `automaticGeofenceRequests = true`를 포함하여 Braze 구성에서 지오펜스를 활성화하세요(3단계). 선택적으로 백그라운드 보고를 활성화하세요(3.1단계). 2.1단계(BrazeLocation 모듈 추가)는 필요하지 않습니다. BrazeLocation은 이미 Braze React Native SDK에 암묵적으로 포함되어 있습니다. [iOS 지오펜스, 2.2단계에서 3.1단계]({{site.baseurl}}/developer_guide/geofences/?sdktab=swift#swift_step-21-add-the-brazelocation-module)를 참조하세요.

### 4단계: JavaScript에서 지오펜스 요청하기 {#step-4-request-geofences-from-javascript}

**Android에서:** 사용자가 위치 권한을 부여한 후, `requestLocationInitialization()`을 호출하여 Braze 위치 기능을 초기화하고 Braze 서버에서 지오펜스를 요청하세요. 이 메서드는 iOS에서 지원되지 않으며 iOS에서는 필요하지 않습니다.

**iOS에서:** 이에 해당하는 방법은 네이티브 Swift 또는 Objective-C Braze 구성에서 `automaticGeofenceRequests` 구성을 활성화하는 것입니다(3단계 참조). 이 설정이 활성화되면, SDK는 위치가 사용 가능할 때 자동으로 지오펜스를 요청하고 모니터링합니다. `requestLocationInitialization`에 해당하는 JavaScript 호출은 필요하지 않습니다.

```javascript
import Braze from '@braze/react-native-sdk';

// Android only: call this after the user grants location permission
Braze.requestLocationInitialization();
```

### 5단계: 수동으로 지오펜스 요청하기(선택 사항) {#step-5-manually-request-geofences-optional}

iOS와 Android 모두에서 `requestGeofences`를 사용하여 특정 GPS 좌표에 대한 지오펜스 업데이트를 수동으로 요청할 수 있습니다. 기본적으로 Braze는 기기의 위치를 자동으로 검색하고 지오펜스를 요청합니다. 좌표를 수동으로 제공하려면 다음을 수행하세요.

1. 자동 지오펜스 요청을 비활성화합니다. Android에서는 `braze.xml`에서 `com_braze_automatic_geofence_requests_enabled`를 `false`로 설정하세요. iOS에서는 Braze 구성에서 `automaticGeofenceRequests`를 `false`로 설정하세요.
2. 원하는 위도와 경도로 `requestGeofences`를 호출하세요.

```javascript
import Braze from '@braze/react-native-sdk';

Braze.requestGeofences(33.078947, -116.601356);
```

{% alert important %}
지오펜스는 세션당 한 번만 요청할 수 있으며, SDK에 의해 자동으로 요청하거나 이 메서드를 사용하여 수동으로 요청할 수 있습니다.
{% endalert %}