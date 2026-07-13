{% multi_lang_include developer_guide/prerequisites/swift.md %} [プッシュ通知の設定]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)も必要です。

## リッチプッシュ通知の設定 {#setting-up-rich-push-notifications}

### ステップ 1: サービス拡張の作成 {#step-1-creating-a-service-extension}

[通知サービス拡張](https://developer.apple.com/reference/usernotifications/unnotificationserviceextension)を作成するには、Xcode で **File > New > Target** に移動し、**Notification Service Extension** を選択します。

![リッチプッシュ用の Notification Service Extension を作成する Xcode のターゲットピッカー。]({% image_buster /assets/img_archive/ios10_se_at.png %}){: style="max-width:90%"}

**Embed In Application** がアプリケーションに拡張機能を埋め込むように設定されていることを確認します。

### ステップ 2: 通知サービス拡張機能のセットアップ {#step-2-setting-up-the-notification-service-extension}

通知サービス拡張機能は、アプリにバンドルされる独自のバイナリです。[Apple Developer Portal](https://developer.apple.com) で独自のアプリ ID とプロビジョニングプロファイルを設定する必要があります。

通知サービス拡張機能のバンドル ID は、メインアプリターゲットのバンドル ID とは異なる必要があります。たとえば、アプリのバンドル ID が `com.company.appname` の場合、サービス拡張に `com.company.appname.AppNameServiceExtension` を使用できます。

### ステップ 3: アプリグループの追加 {#step-3-adding-an-app-group}

Xcode で、**Signing & Capabilities** ペインからメインアプリターゲットと通知サービス拡張ターゲットの両方にアプリグループ機能を追加します。次に、**+** ボタンをクリックします。アプリのバンドル ID を使用してアプリグループを作成します。たとえば、アプリのバンドル ID が `com.company.appname` の場合、アプリグループに `group.com.company.appname.xyz` という名前を付けることができます。

{% alert important %}
ここでいうアプリグループとは、Apple の [App Groups Entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups) のことであり、Brazeのワークスペース（旧アプリグループ）ID のことではありません。
{% endalert %}

メインアプリと通知サービス拡張が共有データにアクセスできるようにするには、共有アプリグループが必要です。アプリをアプリグループに追加しない場合、アプリはプッシュペイロードから特定のフィールドを読み込めず、期待通りに完全に動作しない可能性があります。

### ステップ 4: リッチプッシュ通知の統合 {#step-4-integrating-rich-push-notifications}

`BrazeNotificationService` を使用したリッチプッシュ通知の統合に関するステップバイステップガイドについては、[チュートリアル](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications)を参照してください。

サンプルを確認するには、サンプルアプリの [`NotificationService`](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/Swift/Sources/PushNotificationsServiceExtension/NotificationService.swift) の使用法を参照してください。

#### アプリへのリッチプッシュフレームワークの追加 {#adding-the-rich-push-framework-to-your-app}

{% tabs local %}
{% tab Swift Package Manager %}

[Swift Package Managerの統合ガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration/?tab=swift%20package%20manager/)に従って、以下を実行して `BrazeNotificationService` を `Notification Service Extension` に追加します。

1. Xcode で、フレームワークとライブラリの下にある<i class="fas fa-plus" aria-label="追加アイコン"></i>追加アイコンを選択してフレームワークを追加します。<br><br>![プラスアイコンは Xcode のフレームワークとライブラリの下にあります。]({% image_buster /assets/img_archive/rich_notification.png %})<br><br>

2. 「BrazeNotificationService」フレームワークを選択します。<br><br>![開いたモーダルで「BrazeNotificationService」フレームワークを選択できます。]({% image_buster /assets/img_archive/rich_notification2.png %})

{% endtab %}
{% tab CocoaPods %}

以下を Podfile に追加します。

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
Push Storiesを実装する手順については、[ドキュメント]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/push_story/?tab=swift%20package%20manager)を参照してください。
{% endalert %}

Podfile を更新したら、ターミナルで Xcode アプリプロジェクトのディレクトリに移動し、`pod install` を実行します。

{% endtab %}

{% tab Manual %}

`BrazeNotificationService.xcframework` を `Notification Service Extension` に追加するには、[手動統合]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration?tab=manual/)を参照してください。

![BrazeNotificationService.xcframework が通知サービス拡張に追加された Xcode プロジェクト。]({% image_buster /assets/img/swift/rich_push/manual1.png %})

{% endtab %}
{% endtabs %}

#### 独自の UNNotificationServiceExtension の使用 {#using-your-own-unnotificationserviceextension}

独自の UNNotificationServiceExtension を使用する必要がある場合は、`didReceive` メソッドで [`brazeHandle`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazenotificationservice/brazehandle(request:contenthandler:)) を呼び出すことができます。

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

### ステップ 5: Brazeでのアプリグループの設定 {#step-5-configuring-the-app-group-in-braze}

Brazeを初期化する前に、アプリグループの名前をBraze設定の [`push.appGroup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/appgroup) プロパティに割り当てます。

```swift
let configuration = Braze.Configuration(apiKey: "<YOUR-BRAZE-API-KEY>",
                                        endpoint: "<YOUR-BRAZE-ENDPOINT>")
configuration.push.appGroup = "REPLACE_WITH_APPGROUP"
let braze = Braze(configuration: configuration)
```

### ステップ 6: ダッシュボードでリッチプッシュ通知を作成する {#step-6-creating-a-rich-notification-in-your-dashboard}

マーケティングチームはダッシュボードからリッチプッシュ通知を作成することもできます。プッシュコンポーザーでプッシュ通知を作成し、画像やGIFを添付するか、画像・GIF・動画をホストしているURLを提供します。アセットはプッシュ通知の受信時にダウンロードされるため、コンテンツをホスティングしている場合は、リクエストが大規模に同期的に急増することを想定する必要があります。