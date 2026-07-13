## Appleのプライバシーマニフェスト {#privacy-manifest}

### トラッキングデータとは？ {#what-is-tracking-data}

Appleは「トラッキングデータ」を、アプリ内でエンドユーザーやデバイスについて収集され、サードパーティのデータ（ターゲット広告など）やデータブローカーにリンクされたデータと定義しています。完全な定義と例については、[Apple: Tracking](https://developer.apple.com/app-store/app-privacy-details/#user-tracking)を参照してください。

デフォルトでは、Braze SDKはトラッキングデータを収集しません。ただし、Braze SDKの設定によっては、アプリのプライバシーマニフェストにBraze固有のデータを記載する必要がある場合があります。

### プライバシーマニフェストとは？ {#what-is-a-privacy-manifest}

プライバシーマニフェストは、アプリとサードパーティSDKがデータを収集する理由と、そのデータ収集方法を説明するXcodeプロジェクト内のファイルです。データをトラッキングするサードパーティSDKには、それぞれ独自のプライバシーマニフェストが必要です。[アプリのプライバシーレポートを作成](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests#4239187)すると、これらのプライバシーマニフェストファイルは自動的に1つのレポートに集約されます。

### APIトラッキングデータドメイン {#api-tracking-data-domains}

iOS 17.2以降、Appleはエンドユーザーが[Ad Tracking Transparency (ATT) プロンプト](https://support.apple.com/en-us/HT212025)を受け入れるまで、アプリ内で宣言されたすべてのトラッキングエンドポイントをブロックします。Brazeはトラッキングデータをルーティングするためのトラッキングエンドポイントを提供しており、トラッキング以外のファーストパーティデータは元のエンドポイントにルーティングすることもできます。

## Brazeのトラッキングデータを宣言する {#declaring-braze-tracking-data}

{% alert tip %}
詳細な手順については、[Privacy Tracking Data tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking/)を参照してください。
{% endalert %}

### 前提条件 {#prerequisites}

この機能を実装するには、以下のBraze SDKバージョンが必要です。

{% sdk_min_versions swift:9.0.0 %}

### ステップ1：現在のポリシーを確認する {#step-1-review-your-current-policies}

Braze SDKの現在のデータ収集ポリシーを法務チームと確認し、アプリが[Appleの定義に従って](#what-is-tracking-data)トラッキングデータを収集しているかどうかを判断してください。トラッキングデータを収集していない場合は、現時点でBraze SDKのプライバシーマニフェストをカスタマイズする必要はありません。Braze SDKのデータ収集ポリシーの詳細については、[SDKデータ収集]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection)を参照してください。

{% alert important %}
Braze以外のSDKがトラッキングデータを収集する場合は、それらのポリシーを別途確認する必要があります。
{% endalert %}

### ステップ2：プライバシーマニフェストを作成する {#step-2-create-a-privacy-manifest}

まず、Xcodeプロジェクトで`PrivacyInfo.xcprivacy`ファイルを検索して、プライバシーマニフェストがすでに存在するかどうかを確認します。すでにこのファイルがある場合は、次のステップに進んでください。ない場合は、[Apple: Create a privacy manifest](sdk-tracking.iad-01.braze.com)を参照してください。

### ステップ3：エンドポイントをプライバシーマニフェストに追加する {#step-3-add-your-endpoint-to-the-privacy-manifest}

Xcodeプロジェクトでアプリの`PrivacyInfo.xcprivacy`ファイルを開き、テーブルを右クリックして**Raw Keys and Values**にチェックを入れます。

{% alert note %}

{% endalert %}

![コンテキストメニューが開かれ、「Raw Keys and Values」がハイライトされたXcodeプロジェクト。]({% image_buster /assets/img/apple/privacy_manifest/check_raw_keys_and_values.png %})

**App Privacy Configuration**で**NSPrivacyTracking**を選択し、値を**YES**に設定します。

![「NSPrivacyTracking」が「YES」に設定された状態で開かれた「PrivacyInfo.xcprivacy」ファイル。]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytracking.png %})

**App Privacy Configuration**で**NSPrivacyTrackingDomains**を選択します。ドメイン配列に新しい要素を追加し、その値を、[以前に`AppDelegate`に追加した]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration#update-your-app-delegate)エンドポイントに`sdk-tracking`プレフィックスを付けたものに設定します。

![「NSPrivacyTrackingDomains」の下にBrazeトラッキングエンドポイントが記載された状態で開かれた「PrivacyInfo.xcprivacy」ファイル。]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytrackingdomains.png %})

### ステップ4：トラッキングデータを宣言する {#step-4-declare-your-tracking-data}

次に`AppDelegate.swift`を開き、静的または動的トラッキングリストを作成して、宣言する各[トラッキングプロパティ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/trackingproperty/)をリストします。Appleはエンドユーザーが ATTプロンプトを受け入れるまでこれらのプロパティをブロックするため、あなたと法務チームがトラッキングと見なすプロパティのみをリストしてください。以下に例を示します。

{% tabs %}
{% tab 静的な例 %}
以下の例では、`dateOfBirth`、`customEvent`、および`customAttribute`が静的リスト内でトラッキングデータとして宣言されています。

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
以下の例では、エンドユーザーがATTプロンプトを受け入れた後、トラッキングリストが自動的に更新されます。

```swift
func applicationDidBecomeActive(_ application: UIApplication) {
  // Request and check your user's tracking authorization status.
  ATTrackingManager.requestTrackingAuthorization { status in
    // Let Braze know whether user data is allowed to be collected for tracking.
    let enableAdTracking = status == .authorized
    AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)

    // Add the `.firstName` and `.lastName` properties, while removing the `.everything` configuration.
    AppDelegate.braze.updateTrackingAllowList(
      adding: [.firstName, .lastName],
      removing: [.everything]
    )
  }
}
```
{% endtab %}
{% endtabs %}

### ステップ5：無限リトライループを防止する {#step-5-prevent-infinite-retry-loops}

SDKが無限リトライループに入るのを防ぐため、`set(adTrackingEnabled: enableAdTracking)`メソッドを使用してATT権限を処理します。メソッド内の`adTrackingEnabled`プロパティは、以下のように処理する必要があります。

```swift
func applicationDidBecomeActive(_ application: UIApplication) {
    // Request and check your user's tracking authorization status.
    ATTrackingManager.requestTrackingAuthorization { status in
      // Let Braze know whether user data is allowed to be collected for tracking.
      let enableAdTracking = status == .authorized
      AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)
    }
}
```

## データトラッキングを無効にする {#disabling-data-tracking}

Swift SDKのデータトラッキングアクティビティを無効にするには、Brazeインスタンスの[`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled)プロパティを`false`に設定します。`enabled`を`false`に設定すると、Braze SDKはパブリックAPIへの呼び出しをすべて無視します。また、SDKはネットワークリクエストやイベント処理など、進行中のすべてのアクションもキャンセルします。

## 以前に保存したデータを消去する {#wiping-previously-stored-data}

[`wipeData()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata())メソッドを使用すると、ユーザーのデバイスにローカルに保存されたSDKデータを完全に消去できます。

Braze Swiftバージョン7.0.0以降では、SDKと`wipeData()`メソッドがデバイスIDのUUIDをランダムに生成します。ただし、`useUUIDAsDeviceId`が`false`に設定されている場合、_または_ Swift SDKバージョン5.7.0以前を使用している場合は、[`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete)へのPOSTリクエストも行う必要があります。これは、IDFV（Identifier for Vendors）がそのユーザーのデバイスIDとして自動的に使用されるためです。

手動プッシュ連携を使用していて、アプリが`wipeData()`を呼び出した後、同じアプリ実行中にSDKを再度有効にする場合は、`registerForRemoteNotifications()`を再度呼び出して、Brazeが更新されたデバイストークンを受信できるようにしてください。詳細については、[プッシュ通知の設定]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)を参照してください。

## データトラッキングを再開する {#resuming-data-tracking}

データ収集を再開するには、[`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/)を`true`に設定します。ただし、以前に消去されたデータは復元されないことに注意してください。

## IDFVの収集 {#idfv-collection}

Braze iOS SDKの以前のバージョンでは、IDFV（Identifier for Vendor）フィールドがユーザーのデバイスIDとして自動的に収集されていました。Swift SDK `v5.7.0`以降、IDFVフィールドはオプションで無効にできるようになり、代わりにBrazeがランダムなUUIDをデバイスIDとして設定するようになりました。Swift SDK `v7.0.0`以降、IDFVフィールドはデフォルトでは収集されず、代わりにUUIDがデバイスIDとして設定されます。

`useUUIDAsDeviceId`機能は、デバイスIDをUUIDとして設定するよう[Swift SDK](https://github.com/braze-inc/braze-swift-sdk)を構成します。従来、iOS SDKではAppleが生成したIDFV値と同じデバイスIDが割り当てられていました。iOSアプリでこの機能がデフォルトで有効になっている場合、SDKを介して作成されたすべての新規ユーザーにUUIDと同じデバイスIDが割り当てられます。

それでもIDFVを別途収集したい場合は、[`set(identifierforvendor:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforvendor:))を使用できます。

{% alert note %}
`braze.deviceId`を読み取ると、SDKの初期化後の処理が完了するまで呼び出しスレッドがブロックされます。メインスレッドやレイテンシに敏感なコンテキストでは、代わりにノンブロッキングの代替手段を使用してください。

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

Swift SDK `v7.0.0+`で`useUUIDAsDeviceId`が有効（デフォルト）の場合、新規作成されたすべてのユーザーにはランダムなデバイスIDが割り当てられます。既存のユーザーは同じデバイスID値を保持します（IDFVである場合もあります）。

この機能が有効でない場合、デバイスには引き続き作成時にIDFVが割り当てられます。

#### ダウンストリーム {#downstream}

**テクノロジーパートナー**: この機能を有効にすると、BrazeデバイスIDからIDFV値を取得するテクノロジーパートナーは、このデータにアクセスできなくなります。パートナー連携にデバイスから得られるIDFV値が必要な場合は、この機能を`false`に設定することを推奨します。

**Currents**: `useUUIDAsDeviceId`をtrueに設定すると、Currentsで送信されるデバイスIDはIDFV値と等しくなくなります。

### よくある質問 {#frequently-asked-questions}

#### この変更はBrazeの既存ユーザーに影響しますか？ {#will-this-change-impact-my-existing-users-in-braze}

いいえ。この機能を有効にしても、Brazeのユーザーデータは上書きされません。新しいUUIDデバイスIDは、新しいデバイスまたは`wipedata()`が呼び出された場合にのみ作成されます。

#### この機能をオンにした後にオフにすることはできますか？ {#can-i-turn-this-feature-off-after-turning-it-on}

はい、この機能は自由にオンとオフを切り替えることができます。以前に保存されたデバイスIDは上書きされません。

#### Brazeを介してIDFV値を別の場所で収集することはできますか？ {#can-i-still-capture-the-idfv-value-via-braze-elsewhere}

はい、オプションでSwift SDKを使用してIDFVを収集することもできます（収集はデフォルトでは無効です）。