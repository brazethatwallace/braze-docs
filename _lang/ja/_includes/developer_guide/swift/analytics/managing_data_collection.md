## Apple のプライバシーマニフェスト {#privacy-manifest}

### トラッキングデータとは？

Apple は「トラッキングデータ」を、アプリ内でエンドユーザーやデバイスについて収集され、サードパーティのデータ（ターゲット広告など）やデータブローカーにリンクされたデータと定義しています。完全な定義と例については、[Apple: Tracking](https://developer.apple.com/app-store/app-privacy-details/#user-tracking) を参照してください。

デフォルトでは、Braze SDK はトラッキングデータを収集しません。ただし、Braze SDK の設定によっては、アプリのプライバシーマニフェストに Braze 固有のデータを記載する必要がある場合があります。

### プライバシーマニフェストとは？

プライバシーマニフェストは、アプリとサードパーティ SDK がデータを収集する理由と、そのデータ収集方法を説明する Xcode プロジェクト内のファイルです。データをトラッキングするサードパーティ SDK には、それぞれ独自のプライバシーマニフェストが必要です。[アプリのプライバシーレポートを作成](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests#4239187)すると、これらのプライバシーマニフェストファイルは自動的に1つのレポートに集約されます。

### API トラッキングデータドメイン

iOS 17.2 以降、Apple はエンドユーザーが [Ad Tracking Transparency (ATT) プロンプト](https://support.apple.com/en-us/HT212025)を受け入れるまで、アプリ内で宣言されたすべてのトラッキングエンドポイントをブロックします。Braze はトラッキングデータをルーティングするためのトラッキングエンドポイントを提供しており、トラッキング以外のファーストパーティデータは元のエンドポイントにルーティングすることもできます。 

## Braze のトラッキングデータを宣言する

{% alert tip %}
詳細な手順については、[Privacy Tracking Data tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking/) を参照してください。
{% endalert %}

### 前提条件

この機能を実装するには、以下の Braze SDK バージョンが必要です。

{% sdk_min_versions swift:9.0.0 %}

### ステップ 1: 現在のポリシーを確認する

Braze SDK の現在のデータ収集ポリシーを法務チームと確認し、アプリが [Apple の定義に従って](#what-is-tracking-data)トラッキングデータを収集しているかどうかを判断してください。トラッキングデータを収集していない場合は、現時点で Braze SDK のプライバシーマニフェストをカスタマイズする必要はありません。Braze SDK のデータ収集ポリシーの詳細については、[SDK データ収集]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/)を参照してください。

{% alert important %}
Braze 以外の SDK がトラッキングデータを収集する場合は、それらのポリシーを別途確認する必要があります。
{% endalert %}

### ステップ 2: プライバシーマニフェストを作成する

まず、Xcode プロジェクトで `PrivacyInfo.xcprivacy` ファイルを検索して、プライバシーマニフェストがすでに存在するかどうかを確認します。すでにこのファイルがある場合は、次のステップに進んでください。ない場合は、[Apple: Create a privacy manifest](sdk-tracking.iad-01.braze.com) を参照してください。

### ステップ 3: エンドポイントをプライバシーマニフェストに追加する

Xcode プロジェクトでアプリの `PrivacyInfo.xcprivacy` ファイルを開き、テーブルを右クリックして **Raw Keys and Values** にチェックを入れます。

{% alert note %}

{% endalert %}

![コンテキストメニューが開かれ、「Raw Keys and Values」がハイライトされた Xcode プロジェクト。]({% image_buster /assets/img/apple/privacy_manifest/check_raw_keys_and_values.png %})

**App Privacy Configuration** で **NSPrivacyTracking** を選択し、値を **YES** に設定します。

![「NSPrivacyTracking」が「YES」に設定された状態で開かれた「PrivacyInfo.xcprivacy」ファイル。]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytracking.png %})

**App Privacy Configuration** で **NSPrivacyTrackingDomains** を選択します。ドメイン配列に新しい要素を追加し、その値を、`sdk-tracking` プレフィックスを付けて[以前に `AppDelegate` に追加した]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/#update-your-app-delegate)エンドポイントに設定します。

![「NSPrivacyTrackingDomains」の下に Braze トラッキングエンドポイントが記載された状態で開かれた「PrivacyInfo.xcprivacy」ファイル。]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytrackingdomains.png %})

### ステップ 4: トラッキングデータを宣言する

次に `AppDelegate.swift` を開き、静的または動的トラッキングリストを作成して、宣言する各[トラッキングプロパティ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/trackingproperty/)をリストします。Apple はエンドユーザーが ATT プロンプトを受け入れるまでこれらのプロパティをブロックするため、あなたと法務チームがトラッキングと見なすプロパティのみをリストしてください。以下に例を示します。

{% tabs %}
{% tab static example %}
以下の例では、`dateOfBirth`、`customEvent`、および `customAttribute` が静的リスト内でトラッキングデータとして宣言されています。 

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

{% tab dynamic example %}
以下の例では、エンドユーザーが ATT プロンプトを受け入れた後、トラッキングリストが自動的に更新されます。

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

### ステップ 5: 無限リトライループを防止する

SDK が無限リトライループに入るのを防ぐため、`set(adTrackingEnabled: enableAdTracking)` メソッドを使用して ATT 権限を処理します。メソッド内の `adTrackingEnabled` プロパティは、以下のように処理する必要があります。

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

## データトラッキングを無効にする

Swift SDK のデータトラッキングアクティビティを無効にするには、Braze インスタンスの [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled) プロパティを `false` に設定します。`enabled` が `false` に設定されると、Braze SDK はパブリック API への呼び出しをすべて無視します。また、SDK はネットワークリクエストやイベント処理など、進行中のすべてのアクションもキャンセルします。 

## 以前に保存したデータを消去する

[`wipeData()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata()) メソッドを使用すると、ユーザーのデバイスにローカルに保存された SDK データを完全に消去できます。

Braze Swift バージョン 7.0.0 以降では、SDK と `wipeData()` メソッドがデバイス ID の UUID をランダムに生成します。ただし、`useUUIDAsDeviceId` が `false` に設定されている場合、_または_ Swift SDK バージョン 5.7.0 以前を使用している場合は、[`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) への POST リクエストも行う必要があります。これは、IDFV がそのユーザーのデバイス ID として自動的に使用されるためです。

手動プッシュ連携を使用していて、アプリが `wipeData()` を呼び出した後、同じアプリ実行中に SDK を再度有効にする場合は、`registerForRemoteNotifications()` を再度呼び出して、Braze が更新されたデバイストークンを受信できるようにしてください。詳細については、[プッシュ通知の設定]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)を参照してください。

## データトラッキングを再開する

データ収集を再開するには、[`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/) を `true` に設定します。ただし、以前に消去されたデータは復元されないことに注意してください。

## IDFV の収集

Braze iOS SDK の以前のバージョンでは、IDFV（Identifier for Vendor）フィールドがユーザーのデバイス ID として自動的に収集されていました。Swift SDK `v5.7.0` 以降、IDFV フィールドはオプションで無効にできるようになり、代わりに Braze がランダムな UUID をデバイス ID として設定するようになりました。Swift SDK `v7.0.0` 以降、IDFV フィールドはデフォルトでは収集されず、代わりに UUID がデバイス ID として設定されます。

`useUUIDAsDeviceId` 機能は、デバイス ID を UUID として設定するよう [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) を構成します。従来、iOS SDK では Apple が生成した IDFV 値と同じデバイス ID が割り当てられていました。iOS アプリでこの機能がデフォルトで有効になっている場合、SDK を介して作成されたすべての新規ユーザーに UUID と同じデバイス ID が割り当てられます。

それでも IDFV を別途収集したい場合は、[`set(identifierforvendor:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforvendor:)) を使用できます。

### 考慮事項

#### SDK バージョン

Swift SDK `v7.0.0+` で `useUUIDAsDeviceId` が有効（デフォルト）の場合、新規作成されたすべてのユーザーにはランダムなデバイス ID が割り当てられます。既存のユーザーは同じデバイス ID 値を保持します（IDFV である場合もあります）。

この機能が有効でない場合、デバイスには引き続き作成時に IDFV が割り当てられます。

#### ダウンストリーム 

**テクノロジーパートナー**: この機能を有効にすると、Braze デバイス ID から IDFV 値を取得するテクノロジーパートナーは、このデータにアクセスできなくなります。パートナー連携にデバイスから得られる IDFV 値が必要な場合は、この機能を `false` に設定することを推奨します。

**Currents**: `useUUIDAsDeviceId` が true に設定されている場合、Currents で送信されるデバイス ID は IDFV 値と等しくなくなります。

### よくある質問

#### この変更は Braze の既存ユーザーに影響しますか？

いいえ。この機能を有効にしても、Braze のユーザーデータは上書きされません。新しい UUID デバイス ID は、新しいデバイスまたは `wipedata()` が呼び出された場合にのみ作成されます。

#### この機能をオンにした後にオフにすることはできますか？

はい、この機能は自由にオンとオフを切り替えることができます。以前に保存されたデバイス ID は上書きされません。

#### Braze を介して IDFV 値を別の場所で収集することはできますか？

はい、オプションで Swift SDK を使用して IDFV を収集することもできます（収集はデフォルトでは無効です）。