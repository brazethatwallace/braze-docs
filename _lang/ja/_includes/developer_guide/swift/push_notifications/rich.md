{% multi_lang_include developer_guide/prerequisites/swift.md %} [プッシュ通知の設定]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)も必要です。

## リッチプッシュ通知の設定 {#setting-up-rich-push-notifications}

### ステップ 1: サービス拡張機能を作成する {#step-1-creating-a-service-extension}

[通知サービス拡張機能](https://developer.apple.com/reference/usernotifications/unnotificationserviceextension)を作成するには、Xcode で **File > New > Target** に移動し、**Notification Service Extension** を選択します。

![リッチプッシュ用の Notification Service Extension を作成する Xcode のターゲットピッカー。]({% image_buster /assets/img_archive/ios10_se_at.png %}){: width="1442" height="1030" style="max-width:90%"}

**Embed In Application** がアプリケーションに拡張機能を埋め込むように設定されていることを確認してください。

### ステップ 2: 通知サービス拡張機能を設定する {#step-2-setting-up-the-notification-service-extension}

通知サービス拡張機能は、アプリにバンドルされる独自のバイナリです。[Apple Developer Portal](https://developer.apple.com) で独自のアプリ ID とプロビジョニングプロファイルを使用して設定する必要があります。

通知サービス拡張機能のバンドル ID は、メインアプリターゲットのバンドル ID とは異なるものにする必要があります。例えば、アプリのバンドル ID が `com.company.appname` の場合、サービス拡張機能には `com.company.appname.AppNameServiceExtension` を使用できます。

### ステップ 3: アプリグループを追加する {#step-3-adding-an-app-group}

Xcode で、**Signing & Capabilities** ペインからメインアプリターゲットと Notification Service Extension ターゲットの両方に App Groups 機能を追加します。次に、**+** ボタンをクリックします。アプリのバンドル ID を使用してアプリグループを作成します。例えば、アプリのバンドル ID が `com.company.appname` の場合、アプリグループに `group.com.company.appname.xyz` という名前を付けることができます。

{% alert important %}
ここでの App Groups は、Apple の [App Groups Entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups) を指しており、Braze のワークスペース（旧アプリグループ）ID ではありません。
{% endalert %}

メインアプリと Notification Service Extension が共有データにアクセスできるように、共有アプリグループが必要です。アプリをアプリグループに追加しない場合、アプリがプッシュペイロードの特定のフィールドを取得できず、期待通りに完全に動作しない可能性があります。

### ステップ 4: リッチプッシュ通知を統合する {#step-4-integrating-rich-push-notifications}

`BrazeNotificationService` を使用したリッチプッシュ通知の統合に関するステップバイステップガイドについては、[チュートリアル](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications)を参照してください。

サンプルを確認するには、Examples アプリの [`NotificationService`](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/Swift/Sources/PushNotificationsServiceExtension/NotificationService.swift) の使用方法を参照してください。

#### リッチプッシュフレームワークをアプリに追加する {#adding-the-rich-push-framework-to-your-app}

{% tabs local %}
{% tab Swift Package Manager %}

[Swift Package Manager 統合ガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration/?tab=swift%20package%20manager/)に従った後、以下の手順で `BrazeNotificationService` を `Notification Service Extension` に追加します。

1. Xcode で、フレームワークとライブラリの下にある <i class="fas fa-plus" aria-label="追加アイコン"></i> 追加アイコンを選択してフレームワークを追加します。<br><br>![Xcode のフレームワークとライブラリの下にあるプラスアイコン。]({% image_buster /assets/img_archive/rich_notification.png %}){: width="1930" height="446"}<br><br>

2. 「BrazeNotificationService」フレームワークを選択します。<br><br>![開いたモーダルで BrazeNotificationService フレームワークを選択できます。]({% image_buster /assets/img_archive/rich_notification2.png %}){: width="2248" height="1102"}

{% endtab %}
{% tab CocoaPods %}

Podfile に以下を追加します。

```ruby
target 'YourAppTarget' do
  pod 'BrazeKit'
  pod 'BrazeUI'
  pod 'BrazeLocation'
end

target 'YourNotificationServiceExtensionTarget' do
  pod 'BrazeNotificationService'
end

# Only include the below if you want to also integrate Push Stories
target 'YourNotificationContentExtensionTarget' do
  pod 'BrazePushStory'
end
```

{% alert note %}
Push Stories の実装手順については、[ドキュメント]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/push_story/?tab=swift%20package%20manager)を参照してください。
{% endalert %}

Podfile を更新した後、ターミナルで Xcode アプリプロジェクトのディレクトリに移動し、`pod install` を実行します。

{% endtab %}

{% tab 手動 %}

`BrazeNotificationService.xcframework` を `Notification Service Extension` に追加するには、[手動統合]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration?tab=manual/)を参照してください。

![BrazeNotificationService.xcframework が通知サービス拡張機能に追加された Xcode プロジェクト。]({% image_buster /assets/img/swift/rich_push/manual1.png %}){: width="1069" height="170"}

{% endtab %}
{% endtabs %}

#### 独自の UNNotificationServiceExtension を使用する {#using-your-own-unnotificationserviceextension}

独自の UNNotificationServiceExtension を使用する必要がある場合は、代わりに `didReceive` メソッドで [`brazeHandle`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazenotificationservice/brazehandle(request:contenthandler:)) を呼び出すことができます。

```swift
import BrazeNotificationService
import UserNotifications

class NotificationService: UNNotificationServiceExtension {

  override func didReceive(
    _ request: UNNotificationRequest,
    withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void
  ) {
    if brazeHandle(request: request, contentHandler: contentHandler) {
      return
    }

    // Custom handling here

    contentHandler(request.content)
  }
}
```

### ステップ 5: Braze でアプリグループを設定する {#step-5-configuring-the-app-group-in-braze}

Braze を初期化する前に、アプリグループの名前を Braze 設定の [`push.appGroup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/appgroup) プロパティに割り当てます。

```swift
let configuration = Braze.Configuration(apiKey: "<YOUR-BRAZE-API-KEY>",
                                        endpoint: "<YOUR-BRAZE-ENDPOINT>")
configuration.push.appGroup = "REPLACE_WITH_APPGROUP"
let braze = Braze(configuration: configuration)
```

### ステップ 6: ダッシュボードでリッチ通知を作成する {#step-6-creating-a-rich-notification-in-your-dashboard}

マーケティングチームはダッシュボードからリッチ通知を作成することもできます。プッシュコンポーザーを使用してプッシュ通知を作成し、画像や GIF を添付するか、画像、GIF、または動画をホストする URL を提供します。アセットはプッシュ通知の受信時にダウンロードされるため、コンテンツを自前でホストしている場合は、大規模な同期リクエストのスパイクに備えて計画する必要があります。