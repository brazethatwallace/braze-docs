{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## 데이터 추적 비활성화하기 {#disabling-data-tracking}

데이터 수집을 비활성화하려면 `disableSDK` 메서드를 사용합니다. 이 메서드를 호출하면 Braze SDK가 Braze 서버로 데이터를 전송하는 것을 중지합니다.

```javascript
Braze.disableSDK();
```

## 데이터 추적 재개하기 {#resuming-data-tracking}

데이터 수집을 비활성화한 후 다시 재개하려면 `enableSDK` 메서드를 사용하세요.

```javascript
Braze.enableSDK();
```

## 로컬에 저장된 데이터 삭제하기 {#wiping-data}

기기에 로컬로 저장된 모든 Braze SDK 데이터를 삭제하려면 `wipeData` 메서드를 사용하세요. 이 메서드를 호출하면 SDK가 비활성화되며, `enableSDK`를 사용하여 다시 활성화해야 합니다.

```javascript
Braze.wipeData();
```

## 데이터 플러시 {#flushing-data}

Braze 서버로 대기 중인 데이터를 즉시 플러시하려면 `requestImmediateDataFlush`를 사용하세요.

```javascript
Braze.requestImmediateDataFlush();
```

## 광고 추적 활성화 설정 {#setting-ad-tracking-enabled}

Braze에 이 기기에서 광고 추적이 활성화되어 있는지 알리려면 `setAdTrackingEnabled` 메서드를 사용하세요. SDK는 이 데이터를 자동으로 수집하지 않습니다.

```javascript
Braze.setAdTrackingEnabled(true, "GOOGLE_ADVERTISING_ID");
```

두 번째 매개변수는 Google 광고 ID이며 Android에서만 사용됩니다.

## 추적 속성정보 허용 목록 업데이트하기 (iOS 전용) {#updating-the-tracking-property-allow-list-ios-only}

추적으로 선언된 데이터 유형 목록을 업데이트하려면 `updateTrackingPropertyAllowList`를 사용하세요. 이 메서드는 Android에서는 아무 작업도 수행하지 않습니다.

```javascript
Braze.updateTrackingPropertyAllowList({
  adding: [Braze.TrackingProperty.EMAIL, Braze.TrackingProperty.FIRST_NAME],
  removing: [],
  addingCustomEvents: ["my_custom_event"],
  removingCustomEvents: [],
  addingCustomAttributes: ["my_custom_attribute"],
  removingCustomAttributes: []
});
```

자세한 내용은 [개인정보 보호 매니페스트]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest)를 참조하세요.

## 로그아웃 및 푸시 등록 해제 {#logout-and-unregister-push}

이 기능은 아직 React Native SDK에서 지원되지 않습니다.