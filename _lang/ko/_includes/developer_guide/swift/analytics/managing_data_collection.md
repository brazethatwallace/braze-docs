## Apple의 개인정보 취급방침 {#privacy-manifest}

### 추적 데이터란 무엇인가요? {#what-is-tracking-data}

Apple은 "추적 데이터"를 서드파티 데이터(예: 타겟 광고) 또는 데이터 브로커에 연결된 최종사용자 또는 기기에 대해 앱에서 수집한 데이터로 정의합니다. 예제와 함께 전체 정의는 [Apple: 추적](https://developer.apple.com/app-store/app-privacy-details/#user-tracking)을 참조하세요.

기본적으로 Braze SDK는 추적 데이터를 수집하지 않습니다. 하지만 Braze SDK 구성에 따라 앱의 개인정보 보호 매니페스트에 Braze 관련 데이터를 나열해야 할 수도 있습니다.

### 개인정보 보호 매니페스트란? {#what-is-a-privacy-manifest}

개인정보 보호 매니페스트는 앱 및 서드파티 SDK가 데이터를 수집하는 이유와 데이터 수집 방법을 설명하는 Xcode 프로젝트의 파일입니다. 데이터를 추적하는 각 서드파티 SDK에는 자체 개인정보 보호 매니페스트가 필요합니다. [앱의 프라이버시 보고서를 생성](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests#4239187)하면 이러한 개인정보 보호 매니페스트 파일이 단일 보고서로 자동 집계됩니다.

### API 추적 데이터 도메인 {#api-tracking-data-domains}

iOS 17.2부터 Apple은 최종사용자가 [광고 추적 투명성(ATT) 프롬프트](https://support.apple.com/en-us/HT212025)를 수락할 때까지 앱에서 선언된 모든 추적 엔드포인트를 차단합니다. Braze는 추적 데이터를 라우팅할 수 있는 추적 엔드포인트를 제공하는 동시에, 추적하지 않는 퍼스트파티 데이터를 원래 엔드포인트로 라우팅할 수 있도록 합니다.

## Braze 추적 데이터 선언하기 {#declaring-braze-tracking-data}

{% alert tip %}
전체 안내는 [개인정보 추적 데이터 튜토리얼](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking/)을 참조하세요.
{% endalert %}

### 전제 조건 {#prerequisites}

이 기능을 구현하려면 다음 Braze SDK 버전이 필요합니다:

{% sdk_min_versions swift:9.0.0 %}

### 1단계: 현재 정책 검토하기 {#step-1-review-your-current-policies}

법무팀과 함께 Braze SDK의 현재 데이터 수집 정책을 검토하여 앱이 [Apple이 정의한](#what-is-tracking-data) 추적 데이터를 수집하는지 확인하세요. 추적 데이터를 수집하지 않는 경우, 현재 Braze SDK의 개인정보 보호 매니페스트를 커스텀할 필요가 없습니다. Braze SDK의 데이터 수집 정책에 대한 자세한 내용은 [SDK 데이터 수집]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection)을 참조하세요.

{% alert important %}
Braze 이외의 SDK가 추적 데이터를 수집하는 경우, 해당 정책을 별도로 검토해야 합니다.
{% endalert %}

### 2단계: 개인정보 보호 매니페스트 생성하기 {#step-2-create-a-privacy-manifest}

먼저 Xcode 프로젝트에서 `PrivacyInfo.xcprivacy` 파일을 검색하여 개인정보 보호 매니페스트가 이미 있는지 확인하세요. 이 파일이 이미 있는 경우 다음 단계로 진행할 수 있습니다. 그렇지 않은 경우 [Apple: 개인정보 보호 매니페스트 생성하기](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files)를 참조하세요.

### 3단계: 개인정보 보호 매니페스트에 엔드포인트 추가하기 {#step-3-add-your-endpoint-to-the-privacy-manifest}

Xcode 프로젝트에서 앱의 `PrivacyInfo.xcprivacy` 파일을 열고, 테이블을 마우스 오른쪽 버튼으로 클릭한 다음 **Raw Keys and Values**를 선택하세요.

{% alert note %}

{% endalert %}

![컨텍스트 메뉴가 열려 있고 'Raw Keys and Values'가 강조 표시된 Xcode 프로젝트.]({% image_buster /assets/img/apple/privacy_manifest/check_raw_keys_and_values.png %})

**App Privacy Configuration**에서 **NSPrivacyTracking**을 선택하고 값을 **YES**로 설정하세요.

!['NSPrivacyTracking'이 'YES'로 설정된 'PrivacyInfo.xcprivacy' 파일.]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytracking.png %})

**App Privacy Configuration**에서 **NSPrivacyTrackingDomains**를 선택하세요. 도메인 배열에 새 요소를 추가하고, [이전에 `AppDelegate`에 추가한]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration#update-your-app-delegate) 엔드포인트 앞에 `sdk-tracking`을 접두사로 붙여 값을 설정하세요.

!['NSPrivacyTrackingDomains' 아래에 Braze 추적 엔드포인트가 나열된 'PrivacyInfo.xcprivacy' 파일.]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytrackingdomains.png %})

### 4단계: 추적 데이터 선언하기 {#step-4-declare-your-tracking-data}

다음으로 `AppDelegate.swift`를 열고 정적 또는 동적 추적 목록을 생성하여 선언하려는 각 [추적 속성정보](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/trackingproperty/)를 나열하세요. Apple은 최종사용자가 ATT 프롬프트를 수락할 때까지 이러한 속성정보를 차단하므로, 본인과 법무팀이 추적으로 간주하는 속성정보만 나열하세요. 예를 들어:

{% tabs %}
{% tab 정적 예시 %}
다음 예시에서는 `dateOfBirth`, `customEvent`, `customAttribute`가 정적 목록 내에서 추적 데이터로 선언됩니다.

```swift
import UIKit
import BrazeKit

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    let configuration = Braze.Configuration(apiKey: brazeApiKey, endpoint: brazeEndpoint)
    // Declare which types of data you wish to collect for user tracking.
    configuration.api.trackingPropertyAllowList = [
      .dateOfBirth,
      .customEvent(["event-1"]),
      .customAttribute(["attribute-1", "attribute-2"])
    ]
    let braze = Braze(configuration: configuration)
    AppDelegate.braze = braze
    return true
  }
}
```
{% endtab %}

{% tab 동적 예시 %}
다음 예시에서는 최종사용자가 [앱 추적 투명성(ATT) 프롬프트](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/requesttrackingauthorization(completionhandler:))를 수락한 후 추적 목록이 자동으로 업데이트됩니다. 앱 활성화 시 권한을 요청하는 것은 씬(scene) 단위 이벤트이므로, 이 코드는 `AppDelegate.swift`의 `applicationDidBecomeActive(_:)`가 아닌 `SceneDelegate.swift` 파일의 `sceneDidBecomeActive(_:)` 메서드에 위치해야 합니다([`UIScene` 생명주기](https://developer.apple.com/documentation/technotes/tn3187-migrating-to-the-uikit-scene-based-life-cycle)를 채택한 앱에 필요). Braze 인스턴스는 1단계에서 구성한 `AppDelegate.braze` 정적 속성정보를 통해 `SceneDelegate`에서 접근할 수 있습니다.

```swift
func sceneDidBecomeActive(_ scene: UIScene) {
  // Request and check your user's tracking authorization status.
  ATTrackingManager.requestTrackingAuthorization { status in
    // Let Braze know whether user data is allowed to be collected for tracking.
    let enableAdTracking = status == .authorized
    AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)

    // Add the `.firstName` and `.lastName` properties, while removing the `.everything` configuration.
    AppDelegate.braze?.updateTrackingAllowList(
      adding: [.firstName, .lastName],
      removing: [.everything]
    )
  }
}
```
{% endtab %}
{% endtabs %}

### 5단계: 무한 재시도 루프 방지하기 {#step-5-prevent-infinite-retry-loops}

SDK가 무한 재시도 루프에 빠지는 것을 방지하려면 `set(adTrackingEnabled: enableAdTracking)` 메서드를 사용하여 ATT 권한을 처리하세요. `SceneDelegate.swift` 메서드의 `adTrackingEnabled` 속성정보는 다음과 유사하게 처리해야 합니다:

```swift
func sceneDidBecomeActive(_ scene: UIScene) {
    // Request and check your user's tracking authorization status.
    ATTrackingManager.requestTrackingAuthorization { status in
      // Let Braze know whether user data is allowed to be collected for tracking.
      let enableAdTracking = status == .authorized
      AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)
    }
}
```

## 데이터 추적 비활성화하기 {#disabling-data-tracking}

Swift SDK에서 데이터 추적 활동을 비활성화하려면 Braze 인스턴스의 [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled) 속성을 `false`로 설정하세요. `enabled`가 `false`로 설정되면 Braze SDK는 공개 API에 대한 모든 호출을 무시합니다. 또한 SDK는 네트워크 요청, 이벤트 처리 등 진행 중인 모든 작업을 취소합니다.

## 이전에 저장된 데이터 삭제 {#wiping-previously-stored-data}

[`wipeData()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata()) 메서드를 사용하여 사용자 기기에 로컬로 저장된 SDK 데이터를 완전히 삭제할 수 있습니다.

Braze Swift 버전 7.0.0 이상에서는 SDK와 `wipeData()` 메서드가 기기 ID에 대해 UUID를 무작위로 생성합니다. 그러나 `useUUIDAsDeviceId`가 `false`로 설정되어 있거나 Swift SDK 버전 5.7.0 이하를 사용하는 경우, IDFV가 해당 사용자의 기기 ID로 자동 사용되므로 [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete)에 POST 요청도 보내야 합니다.

수동 푸시 통합을 사용하고 있으며, 앱에서 `wipeData()`를 호출한 후 동일한 앱 실행 중에 SDK를 다시 활성화하는 경우, Braze가 갱신된 기기 토큰을 수신할 수 있도록 `registerForRemoteNotifications()`를 다시 호출하세요. 자세한 내용은 [푸시 알림 설정]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)을 참조하세요.

## 데이터 추적 재개하기 {#resuming-data-tracking}

데이터 수집을 재개하려면 [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/)를 `true`로 설정하세요. 이전에 삭제된 데이터는 복원되지 않는다는 점에 유의하세요.

## 로그아웃 및 푸시 등록 해제 {#logout-and-unregister-push}

Braze SDK는 사용자가 푸시 알림 등록을 해제하거나 로그아웃할 때 기기를 타겟팅 대상에서 제거하는 메서드를 제공합니다. 이 메서드는 Braze 서버와 SDK에서 현재 사용자의 푸시 등록 데이터를 제거하므로, Braze는 더 이상 해당 사용자에게 푸시 알림 Campaigns를 전송하지 않습니다.

### 로그아웃 {#logout}

사용자가 애플리케이션에서 로그아웃할 때, SDK의 `logout` 메서드를 호출하여 현재 사용자로부터 기기의 푸시 등록을 제거하고 SDK에서 자동으로 정리 작업을 수행합니다. `logout` 메서드는 다음을 수행합니다:

- Braze 서버에서 현재 사용자의 기기 푸시 토큰 및 모든 Live Activities push-to-start 토큰의 등록을 해제합니다.
- 등록 해제 호출이 성공하면, SDK는 로컬에 저장된 SDK 데이터를 삭제하고 SDK를 비활성화합니다.
- 실패 시, 오류와 `isRetriable` 플래그를 발생시켜 통합 담당자가 조치를 취할 수 있도록 합니다.

{% subtabs local %}
{% subtab Swift %}

다음 completion-handler 예제는 `logout`의 성공 및 실패 처리를 보여줍니다. 콜백 기반 흐름에 사용하며, 로깅 부분을 앱의 재시도 또는 재인증 로직으로 교체하세요.

```swift
// Completion handler
AppDelegate.braze?.logout { result in
  switch result {
  case .success:
    print("Logout successful")
  case .failure(let error):
    print("Logout failed: \(error.message), isRetriable: \(error.isRetriable)")
  }
}
```

다음 async 예제는 일시 중단 가능한 `logout` API를 보여줍니다. async 워크플로에 사용하며, 앱에 맞게 성공 및 실패 분기를 커스터마이즈하세요.

```swift
// Async/await
do {
  try await AppDelegate.braze?.logout()
  print("Logout successful")
} catch let error as Braze.LogoutErrorResult {
  print("Logout failed: \(error.message), isRetriable: \(error.isRetriable)")
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

이 Objective-C 예제는 completion 기반 `logout` 처리를 보여줍니다. Objective-C 통합에서 사용하며, 로깅 부분을 앱 흐름에 맞게 교체하세요.

```objc
[AppDelegate.braze logoutWithCompletion:^(NSError * _Nullable error) {
  if (error) {
    NSNumber *isRetriable = error.userInfo[BRZLogoutErrorUserInfoKey.isRetriable];
    NSLog(@"Logout failed: %@, isRetriable=%@", error.localizedDescription, isRetriable);
  }
}];
```

{% endsubtab %}
{% endsubtabs local %}

{% alert note %}
`logout`은 현재 실행 중인 Live Activities를 종료하지 않습니다. 성공 콜백에서 ActivityKit의 [`end(_:dismissalPolicy:)`](https://developer.apple.com/documentation/activitykit/activity/end(_:dismissalpolicy:)) 메서드를 사용하여 실행 중인 Live Activities를 수동으로 종료하세요.
{% endalert %}

#### `logout` 후 추적 및 푸시 다시 활성화하기 {#re-enable-tracking-and-push-after-logout}

`logout`이 성공한 후, [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/)를 다시 `true`로 설정한 다음, [Swift 푸시 설정]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)을 따라 운영 체제(OS) 또는 푸시 공급자에 알림을 다시 등록하세요.

#### 즉시 등록 해제 호출 피하기 {#avoid-immediate-unregister-calls}

OS 또는 푸시 공급자에 푸시 알림을 등록한 직후에 `logout` 또는 `unregisterPush`를 호출하지 마세요. 비동기 서버 처리로 인해 드물게 푸시 토큰이 Braze 사용자에게 다시 추가될 수 있습니다.

### 푸시 등록 해제 {#unregister-push}

추가적인 자동 정리 없이 기기에 대한 푸시 전송을 중지하려면 `unregisterPush` 메서드를 사용하세요. 이 메서드는 Braze 서버에서 현재 사용자의 기기 푸시 토큰을 제거하고, 로컬에 저장된 토큰을 삭제합니다.

{% subtabs local %}
{% subtab Swift %}

다음 completion-handler 예제는 `unregisterPush`의 성공 및 실패 처리를 보여줍니다. 콜백 기반 흐름에 사용하며, 로깅 부분을 자체 재시도 로직으로 교체하세요.

```swift
// Completion handler
AppDelegate.braze?.notifications.unregisterPush { result in
  switch result {
  case .success:
    print("Push unregistered successfully")
  case .failure(let error):
    print("Push unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
  }
}
```

다음 async 예제는 일시 중단 가능한 `unregisterPush` API를 보여줍니다. async 워크플로에 사용하며, 앱에 맞게 성공 및 실패 분기를 커스터마이즈하세요.

```swift
// Async/await
do {
  try await AppDelegate.braze?.notifications.unregisterPush()
  print("Push unregistered successfully")
} catch let error as Braze.PushUnregistrationError {
  print("Push unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

이 Objective-C 예제는 completion 기반 `unregisterPush` 처리를 보여줍니다. Objective-C 통합에서 사용하며, 로깅 부분을 앱 흐름에 맞게 교체하세요.

```objc
[AppDelegate.braze.notifications unregisterPushWithCompletion:^(NSError * _Nullable error) {
  if (error) {
    NSNumber *isRetriable = error.userInfo[BRZPushUnregistrationErrorUserInfoKey.isRetriable];
    NSNumber *statusCode = error.userInfo[BRZPushUnregistrationErrorUserInfoKey.httpStatusCode];
    NSLog(@"Push unregistration failed: %@, isRetriable=%@ status=%@",
          error.localizedDescription, isRetriable, statusCode);
  }
}];
```

{% endsubtab %}
{% endsubtabs local %}

#### `unregisterPush` 후 푸시 다시 등록하기 {#re-register-push-after-unregisterpush}

`unregisterPush`를 호출한 후, Braze 푸시 알림을 다시 전송하기 전에 [Swift 푸시 설정]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)을 따라 OS 또는 푸시 공급자에 알림을 다시 등록하세요.

#### 즉시 등록 해제 호출 피하기

OS 또는 푸시 공급자에 푸시 알림을 등록한 직후에 `logout` 또는 `unregisterPush`를 호출하지 마세요. 비동기 서버 처리로 인해 드물게 푸시 토큰이 Braze 사용자에게 다시 추가될 수 있습니다.

### Live Activities의 push-to-start 토큰 등록 해제 {#unregister-push-to-start}

Live Activities는 push-to-start 토큰을 사용하여 원격으로 시작할 수 있습니다. Braze가 기기에서 Live Activities를 원격으로 시작하는 것을 중지하려면, `unregisterPushToStart` 메서드를 호출하여 현재 등록된 모든 유형(기본값) 또는 지정된 Activity 유형 목록의 등록을 해제하세요.

현재 실행 중인 Live Activities는 계속 업데이트를 수신하며, 이 메서드는 새로운 활동을 원격으로 시작하는 기능만 제거합니다. Live Activities에 대한 자세한 내용은 [Live Activities]({{site.baseurl}}/developer_guide/live_notifications/live_activities)를 참조하세요.

#### 실행 중인 Live Activities 종료하기 {#end-any-running-live-activities}

`unregisterPushToStart`는 현재 실행 중인 Live Activities를 종료하지 않습니다. 성공 콜백에서 ActivityKit의 [`end(_:dismissalPolicy:)`](https://developer.apple.com/documentation/activitykit/activity/end(_:dismissalpolicy:)) 메서드를 사용하여 실행 중인 Live Activities를 수동으로 종료하세요.

{% alert note %}
Live Activity에 대해 `registerPushToStart`를 호출한 직후에 `logout` 또는 `unregisterPushToStart`를 호출하지 마세요. 서버 처리의 비동기 특성으로 인해 드물게 push-to-start 토큰이 Braze 사용자에게 다시 추가될 수 있습니다.
{% endalert %}

다음 예제는 모든 push-to-start 활동 유형의 등록을 해제하는 방법을 보여줍니다. 로그아웃한 사용자가 더 이상 원격으로 시작된 새로운 Live Activities를 수신하지 않아야 할 때 사용하세요.

```swift
// Unregister all currently-registered activity types
// Completion handler
AppDelegate.braze?.liveActivities.unregisterPushToStart { result in
  switch result {
  case .success:
    print("Push-to-start unregistered successfully")
  case .failure(let error):
    print("Push-to-start unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
  }
}

// Async/await
do {
  try await AppDelegate.braze?.liveActivities.unregisterPushToStart()
  print("Push-to-start unregistered successfully")
} catch let error as Braze.PushUnregistrationError {
  print("Push-to-start unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
}
```

다음 예제는 특정 활동 유형의 등록을 해제하는 방법을 보여줍니다. 선택한 Live Activities만 원격 시작을 중지해야 할 때 사용하세요.

```swift
// Unregister specific activity types
AppDelegate.braze?.liveActivities.unregisterPushToStart(types: ["ActivityType1", "ActivityType2"]) { result in
  switch result {
  case .success:
    print("Push-to-start unregistered successfully")
  case .failure(let error):
    print("Push-to-start unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
  }
}
```

{% alert note %}
`unregisterPushToStart`는 Objective-C API가 없습니다. Live Activities가 Swift 전용 타입에 의존하기 때문입니다.
{% endalert %}

## IDFV 수집 {#idfv-collection}

이전 버전의 Braze iOS SDK에서는 IDFV(Identifier for Vendor) 필드가 사용자의 기기 ID로 자동 수집되었습니다. Swift SDK `v5.7.0`부터 IDFV 필드를 선택적으로 비활성화할 수 있게 되었으며, 대신 Braze가 랜덤 UUID를 기기 ID로 설정하게 되었습니다. Swift SDK `v7.0.0`부터는 IDFV 필드가 기본적으로 수집되지 않으며, 대신 UUID가 기기 ID로 설정됩니다.

`useUUIDAsDeviceId` 기능은 [Swift SDK](https://github.com/braze-inc/braze-swift-sdk)가 기기 ID를 UUID로 설정하도록 구성합니다. 기존에는 iOS SDK가 Apple에서 생성한 IDFV 값과 동일한 기기 ID를 할당했습니다. 이 기능이 iOS 앱에서 기본적으로 활성화되면, SDK를 통해 생성된 모든 신규 사용자에게 UUID와 동일한 기기 ID가 할당됩니다.

IDFV를 별도로 수집하려면 [`set(identifierforvendor:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforvendor:))를 사용할 수 있습니다.

{% alert note %}
`braze.deviceId`를 읽으면 SDK가 초기화 후 작업을 완료할 때까지 호출 스레드가 차단됩니다. 메인 스레드 또는 지연 시간에 민감한 컨텍스트에서는 대신 비차단 대안을 사용하세요.

{% subtabs local %}
{% subtab Swift %}
```swift
// Completion handler — always delivers on the main thread.
AppDelegate.braze?.getDeviceId { deviceId in
  print("Device ID:", deviceId)
}

// Async/await (iOS 13.0+, tvOS 13.0+, watchOS 6.0+, macOS 10.15+)
let deviceId = await AppDelegate.braze?.getDeviceId()
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// Completion handler — always delivers on the main thread.
[AppDelegate.braze getDeviceIdWithCompletion:^(NSString *deviceId) {
  NSLog(@"Device ID: %@", deviceId);
}];
```
{% endsubtab %}
{% endsubtabs local %}
{% endalert %}

### 고려 사항 {#considerations}

#### SDK 버전 {#sdk-version}

Swift SDK `v7.0.0+`에서 `useUUIDAsDeviceId`가 활성화(기본값)되면, 새로 생성된 모든 사용자에게 랜덤 기기 ID가 할당됩니다. 기존에 존재하던 모든 사용자는 동일한 기기 ID 값을 유지하며, 이 값은 IDFV였을 수 있습니다.

이 기능이 활성화되지 않은 경우, 기기는 생성 시 계속 IDFV가 할당됩니다.

#### 다운스트림 {#downstream}

**기술 파트너**: 이 기능이 활성화되면, Braze 기기 ID에서 IDFV 값을 파생하는 기술 파트너는 더 이상 이 데이터에 접근할 수 없습니다. 파트너 통합에 기기에서 파생된 IDFV 값이 필요한 경우, 이 기능을 `false`로 설정하는 것을 권장합니다.

**Currents**: `useUUIDAsDeviceId`를 true로 설정하면 Currents에서 전송되는 기기 ID가 더 이상 IDFV 값과 동일하지 않게 됩니다.

### 자주 묻는 질문 {#frequently-asked-questions}

#### 이 변경 사항이 Braze의 기존 사용자에게 영향을 미치나요? {#will-this-change-impact-my-existing-users-in-braze}

아니요. 이 기능을 활성화해도 Braze의 기존 사용자 데이터를 덮어쓰지 않습니다. 새로운 UUID 기기 ID는 새 기기에서만 생성되거나 `wipedata()`가 호출될 때만 생성됩니다.

#### 이 기능을 켠 후 다시 끌 수 있나요? {#can-i-turn-this-feature-off-after-turning-it-on}

네, 이 기능은 필요에 따라 자유롭게 켜고 끌 수 있습니다. 이전에 저장된 기기 ID는 절대 덮어쓰이지 않습니다.

#### Braze의 다른 곳에서 IDFV 값을 여전히 캡처할 수 있나요? {#can-i-still-capture-the-idfv-value-through-braze-elsewhere}

네, Swift SDK를 통해 IDFV를 선택적으로 수집할 수 있습니다(기본적으로 수집은 비활성화되어 있습니다).