## Appleのプライバシーマニフェスト {#privacy-manifest}

### トラッキングデータとは？ {#what-is-tracking-data}

Appleは「トラッキングデータ」を、アプリ内でエンドユーザーやデバイスについて収集され、サードパーティのデータ（ターゲット広告など）やデータブローカーにリンクされたデータと定義しています。完全な定義と例については、[Apple: Tracking](https://developer.apple.com/app-store/app-privacy-details/#user-tracking)を参照してください。

デフォルトでは、Braze SDKはトラッキングデータを収集しません。ただし、Braze SDKの設定によっては、アプリのプライバシーマニフェストにBraze固有のデータを記載する必要がある場合があります。

### プライバシーマニフェストとは？ {#what-is-a-privacy-manifest}

プライバシーマニフェストは、アプリとサードパーティSDKがデータを収集する理由と、そのデータ収集方法を説明するXcodeプロジェクト内のファイルです。データをトラッキングするサードパーティSDKには、それぞれ独自のプライバシーマニフェストが必要です。[アプリのプライバシーレポートを作成](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests#4239187)すると、これらのプライバシーマニフェストファイルは自動的に1つのレポートに集約されます。

### APIトラッキングデータドメイン {#api-tracking-data-domains}

iOS 17.2以降、Appleはエンドユーザーが[Ad Tracking Transparency (ATT) プロンプト](https://support.apple.com/en-us/HT212025)を受け入れるまで、アプリ内で宣言されたすべてのトラッキングエンドポイントをブロックします。Brazeはトラッキングデータをルーティングするためのトラッキングエンドポイントを提供しており、トラッキング以外のファーストパーティデータは元のエンドポイントにルーティングすることもできます。

## Brazeトラッキングデータの宣言 {#declaring-braze-tracking-data}

{% alert tip %}
完全なウォークスルーについては、[プライバシートラッキングデータチュートリアル](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking/)を参照してください。
{% endalert %}

### 前提条件 {#prerequisites}

この機能を実装するには、以下のBraze SDKバージョンが必要です。

{% sdk_min_versions swift:9.0.0 %}

### ステップ1：現在のポリシーを確認する {#step-1-review-your-current-policies}

法務チームと協力して、Braze SDKの現在のデータ収集ポリシーを確認し、アプリが[Appleの定義する](#what-is-tracking-data)トラッキングデータを収集しているかどうかを判断します。トラッキングデータを収集していない場合、現時点ではBraze SDKのプライバシーマニフェストをカスタマイズする必要はありません。Braze SDKのデータ収集ポリシーの詳細については、[SDKデータ収集]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection)を参照してください。

{% alert important %}
Braze以外のSDKがトラッキングデータを収集している場合は、それらのポリシーを個別に確認する必要があります。
{% endalert %}

### ステップ2：プライバシーマニフェストを作成する {#step-2-create-a-privacy-manifest}

まず、Xcodeプロジェクトで`PrivacyInfo.xcprivacy`ファイルを検索して、プライバシーマニフェストが既に存在するかどうかを確認します。このファイルが既にある場合は、次のステップに進むことができます。ない場合は、[Apple: プライバシーマニフェストの作成](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files)を参照してください。

### ステップ3：プライバシーマニフェストにエンドポイントを追加する {#step-3-add-your-endpoint-to-the-privacy-manifest}

Xcodeプロジェクトで、アプリの`PrivacyInfo.xcprivacy`ファイルを開き、テーブルを右クリックして**Raw Keys and Values**にチェックを入れます。

{% alert note %}

{% endalert %}

![コンテキストメニューが開かれ「Raw Keys and Values」がハイライトされたXcodeプロジェクト。]({% image_buster /assets/img/apple/privacy_manifest/check_raw_keys_and_values.png %})

**App Privacy Configuration**で、**NSPrivacyTracking**を選択し、その値を**YES**に設定します。

![「NSPrivacyTracking」が「YES」に設定された「PrivacyInfo.xcprivacy」ファイル。]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytracking.png %})

**App Privacy Configuration**で、**NSPrivacyTrackingDomains**を選択します。ドメイン配列に新しい要素を追加し、[以前`AppDelegate`に追加した]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration#update-your-app-delegate)エンドポイントの先頭に`sdk-tracking`を付けた値を設定します。

![「NSPrivacyTrackingDomains」の下にBrazeトラッキングエンドポイントが表示された「PrivacyInfo.xcprivacy」ファイル。]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytrackingdomains.png %})

### ステップ4：トラッキングデータを宣言する {#step-4-declare-your-tracking-data}

次に、`AppDelegate.swift`を開き、静的または動的なトラッキングリストを作成して、宣言する各[トラッキングプロパティ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/trackingproperty/)をリストします。AppleはエンドユーザーがそのデバイスのATTプロンプトを承認するまでこれらのプロパティをブロックするため、あなたと法務チームがトラッキングと見なすプロパティのみをリストしてください。例：

{% tabs %}
{% tab 静的な例 %}
以下の例では、`dateOfBirth`、`customEvent`、`customAttribute`が静的リスト内でトラッキングデータとして宣言されています。

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

{% tab 動的な例 %}
以下の例では、エンドユーザーが[App Tracking Transparency（ATT）プロンプト](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/requesttrackingauthorization(completionhandler:))を承認した後、トラッキングリストが自動的に更新されます。アプリのアクティベーション時に認可をリクエストすることはシーンごとのイベントであるため、このコードは`AppDelegate.swift`の`applicationDidBecomeActive(_:)`ではなく、`SceneDelegate.swift`ファイルの`sceneDidBecomeActive(_:)`メソッドに配置する必要があります（[`UIScene`ライフサイクル](https://developer.apple.com/documentation/technotes/tn3187-migrating-to-the-uikit-scene-based-life-cycle)を採用しているアプリの場合に必要です）。Brazeインスタンスは、ステップ1で設定した`AppDelegate.braze`静的プロパティを通じて`SceneDelegate`からアクセスできます。

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

### ステップ5：無限リトライループを防止する {#step-5-prevent-infinite-retry-loops}

SDKが無限リトライループに入るのを防ぐには、`set(adTrackingEnabled: enableAdTracking)`メソッドを使用してATT権限を処理します。`SceneDelegate.swift`メソッドの`adTrackingEnabled`プロパティは、以下のように処理する必要があります。

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

## データトラッキングを無効にする {#disabling-data-tracking}

Swift SDKのデータトラッキングアクティビティを無効にするには、Brazeインスタンスの[`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled)プロパティを`false`に設定します。`enabled`が`false`に設定されている場合、Braze SDKはパブリックAPIへのすべての呼び出しを無視します。また、SDKはネットワークリクエストやイベント処理など、進行中のすべてのアクションもキャンセルします。

## 以前に保存されたデータを消去する {#wiping-previously-stored-data}

[`wipeData()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata())メソッドを使用して、ユーザーのデバイスにローカルに保存されたSDKデータを完全に消去できます。

Braze Swiftバージョン7.0.0以降では、SDKと`wipeData()`メソッドはデバイスIDとしてUUIDをランダムに生成します。ただし、`useUUIDAsDeviceId`が`false`に設定されている場合、_または_ Swift SDKバージョン5.7.0以前を使用している場合は、Identifier for Vendors（IDFV）がそのユーザーのデバイスIDとして自動的に使用されるため、[`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete)へのPOSTリクエストも行う必要があります。

手動プッシュ連携を使用しており、アプリが`wipeData()`を呼び出した後、同じアプリ実行中にSDKを再度有効にする場合は、Brazeが更新されたデバイストークンを受信できるように`registerForRemoteNotifications()`を再度呼び出してください。詳細については、[プッシュ通知の設定]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)を参照してください。

## データトラッキングを再開する {#resuming-data-tracking}

データ収集を再開するには、[`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/)を`true`に設定します。ただし、以前に消去されたデータは復元されません。

## ログアウトとプッシュ登録解除 {#logout-and-unregister-push}

Braze SDKは、ユーザーがプッシュ通知の登録を解除したりログアウトしたりする際に、デバイスへのターゲティングを停止するメソッドを提供します。これらのメソッドは、BrazeサーバーおよびSDKから現在のユーザーのプッシュ登録データを削除するため、Brazeはそのユーザーに今後のプッシュ通知キャンペーンを送信しなくなります。

### ログアウト {#logout}

ユーザーがアプリケーションからログアウトする際に、SDKの`logout`メソッドを呼び出して、現在のユーザーからデバイスのプッシュ登録を削除し、SDK上のクリーンアップアクションを自動的に実行します。`logout`メソッドは以下を実行します。

- Brazeサーバー上の現在のユーザーから、デバイスのプッシュトークンおよびすべてのLive Activitiesのpush-to-startトークンの登録を解除します。
- 登録解除の呼び出しが成功した場合、SDKはローカルに保存されたSDKデータを消去し、SDKを無効にします。
- 失敗した場合、エラーと`isRetriable`フラグを発生させ、インテグレーターがアクションを実行できるようにします。

{% subtabs local %}
{% subtab Swift %}

以下のcompletion handlerの例は、`logout`の成功と失敗の処理を示しています。コールバックベースのフローに使用し、ログ出力をアプリのリトライまたは再認証ロジックに置き換えてください。

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

以下のasyncの例は、サスペンド可能な`logout` APIを示しています。非同期ワークフローに使用し、アプリに合わせて成功と失敗のブランチをカスタマイズしてください。

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

このOBJECTIVE-Cの例は、completionベースの`logout`処理を示しています。OBJECTIVE-Cインテグレーションで使用し、ログ出力をアプリのフローに置き換えてください。

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
`logout`は現在実行中のLive Activitiesを終了しません。成功コールバック内で、ActivityKitの[`end(_:dismissalPolicy:)`](https://developer.apple.com/documentation/activitykit/activity/end(_:dismissalpolicy:))メソッドを使用して、実行中のLive Activitiesを手動で終了してください。
{% endalert %}

#### `logout`後のトラッキングとプッシュの再有効化 {#re-enable-tracking-and-push-after-logout}

`logout`が成功した後、[`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/)を`true`に戻し、[Swiftプッシュ設定]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)に従ってオペレーティングシステム（OS）またはプッシュプロバイダーで通知を再登録してください。

#### 即時の登録解除呼び出しを避ける {#avoid-immediate-unregister-calls}

OSまたはプッシュプロバイダーでプッシュ通知を登録した直後に`logout`または`unregisterPush`を呼び出すことは避けてください。非同期のサーバー処理により、まれにプッシュトークンがBrazeユーザーに再追加される可能性があります。

### プッシュ登録解除 {#unregister-push}

追加の自動クリーンアップなしにデバイスへのプッシュ送信を停止するには、`unregisterPush`メソッドを使用します。これにより、Brazeサーバー上の現在のユーザーからデバイスのプッシュトークンが削除され、ローカルに保存されたトークンがクリアされます。

{% subtabs local %}
{% subtab Swift %}

以下のcompletion handlerの例は、`unregisterPush`の成功と失敗の処理を示しています。コールバックベースのフローに使用し、ログ出力を独自のリトライロジックに置き換えてください。

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

以下のasyncの例は、サスペンド可能な`unregisterPush` APIを示しています。非同期ワークフローに使用し、アプリに合わせて成功と失敗のブランチをカスタマイズしてください。

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

このOBJECTIVE-Cの例は、completionベースの`unregisterPush`処理を示しています。OBJECTIVE-Cインテグレーションで使用し、ログ出力をアプリのフローに置き換えてください。

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

#### `unregisterPush`後のプッシュ再登録 {#re-register-push-after-unregisterpush}

`unregisterPush`を呼び出した後、Brazeプッシュ通知を再度送信する前に、[Swiftプッシュ設定]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)に従ってOSまたはプッシュプロバイダーで通知を再登録してください。

#### 即時の登録解除呼び出しを避ける

OSまたはプッシュプロバイダーでプッシュ通知を登録した直後に`logout`または`unregisterPush`を呼び出すことは避けてください。非同期のサーバー処理により、まれにプッシュトークンがBrazeユーザーに再追加される可能性があります。

### Live Activitiesのpush-to-startトークンの登録解除 {#unregister-push-to-start}

Live Activitiesは、push-to-startトークンを使用してリモートで開始できます。BrazeがデバイスでLive Activitiesをリモートで開始しないようにするには、`unregisterPushToStart`メソッドを呼び出して、現在登録されているすべてのタイプ（デフォルト）または指定されたActivityタイプのリストの登録を解除します。

現在実行中のLive Activitiesは引き続き更新を受信し、このメソッドは新しいアクティビティをリモートで開始する機能のみを削除します。Live Activitiesの詳細については、[Live Activities]({{site.baseurl}}/developer_guide/live_notifications/live_activities)を参照してください。

#### 実行中のLive Activitiesを終了する {#end-any-running-live-activities}

`unregisterPushToStart`は現在実行中のLive Activitiesを終了しません。成功コールバック内で、ActivityKitの[`end(_:dismissalPolicy:)`](https://developer.apple.com/documentation/activitykit/activity/end(_:dismissalpolicy:))メソッドを使用して、実行中のLive Activitiesを手動で終了してください。

{% alert note %}
Live Activityの`registerPushToStart`を呼び出した直後に`logout`または`unregisterPushToStart`を呼び出すことは避けてください。非同期のサーバー処理の性質上、まれにpush-to-startトークンがBrazeユーザーに再追加される可能性があります。
{% endalert %}

以下の例は、すべてのpush-to-startアクティビティタイプの登録を解除する方法を示しています。サインアウトしたユーザーがリモートで開始される新しいLive Activitiesを受信しないようにする場合に使用してください。

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

以下の例は、特定のアクティビティタイプの登録を解除する方法を示しています。選択したLive Activitiesのみリモートでの開始を停止する場合に使用してください。

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
`unregisterPushToStart`にはOBJECTIVE-C APIがありません。Live ActivitiesはSwift専用の型に依存しているためです。
{% endalert %}

## IDFVの収集 {#idfv-collection}

以前のバージョンのBraze iOS SDKでは、IDFV（Identifier for Vendor）フィールドはユーザーのデバイスIDとして自動的に収集されていました。Swift SDK `v5.7.0`以降、IDFVフィールドはオプションで無効にできるようになり、代わりにBrazeがランダムなUUIDをデバイスIDとして設定するようになりました。Swift SDK `v7.0.0`以降、IDFVフィールドはデフォルトでは収集されず、代わりにUUIDがデバイスIDとして設定されます。

`useUUIDAsDeviceId`機能は、[Swift SDK](https://github.com/braze-inc/braze-swift-sdk)がデバイスIDをUUIDとして設定するように構成します。従来、iOS SDKはAppleが生成したIDFV値と同じデバイスIDを割り当てていました。この機能がiOSアプリでデフォルトで有効になっている場合、SDKを通じて作成されたすべての新規ユーザーには、UUIDと同じデバイスIDが割り当てられます。

IDFVを個別に収集したい場合は、[`set(identifierforvendor:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforvendor:))を使用できます。

{% alert note %}
`braze.deviceId`の読み取りは、SDKが初期化後の処理を完了するまで呼び出しスレッドをブロックします。メインスレッドやレイテンシーに敏感なコンテキストでは、代わりにノンブロッキングの代替手段を使用してください。

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

### 考慮事項 {#considerations}

#### SDKバージョン {#sdk-version}

Swift SDK `v7.0.0+`では、`useUUIDAsDeviceId`が有効（デフォルト）の場合、新規に作成されたすべてのユーザーにランダムなデバイスIDが割り当てられます。既存のすべてのユーザーは、IDFVであった可能性のある同じデバイスID値を維持します。

この機能が有効でない場合、デバイスには引き続き作成時にIDFVが割り当てられます。

#### ダウンストリーム {#downstream}

**テクノロジーパートナー**：この機能が有効な場合、BrazeデバイスIDからIDFV値を取得しているテクノロジーパートナーは、このデータにアクセスできなくなります。パートナー連携にデバイスから取得したIDFV値が必要な場合は、この機能を`false`に設定することをお勧めします。

**Currents**：`useUUIDAsDeviceId`をtrueに設定すると、Currentsで送信されるデバイスIDはIDFV値と一致しなくなります。

### よくある質問 {#frequently-asked-questions}

#### この変更はBrazeの既存ユーザーに影響しますか？ {#will-this-change-impact-my-existing-users-in-braze}

いいえ。この機能を有効にしても、Brazeのユーザーデータは上書きされません。新しいUUIDデバイスIDは、新しいデバイスまたは`wipedata()`が呼び出された場合にのみ作成されます。

#### この機能を有効にした後に無効にできますか？ {#can-i-turn-this-feature-off-after-turning-it-on}

はい、この機能はお客様の判断でオンとオフを切り替えることができます。以前に保存されたデバイスIDが上書きされることはありません。

#### Brazeの他の場所でIDFV値を取得することはできますか？ {#can-i-still-capture-the-idfv-value-through-braze-elsewhere}

はい、Swift SDKを通じてIDFVをオプションで収集することは引き続き可能です（デフォルトでは収集は無効になっています）。