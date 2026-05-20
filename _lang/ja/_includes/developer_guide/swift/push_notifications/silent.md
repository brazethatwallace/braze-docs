{% multi_lang_include developer_guide/prerequisites/swift.md %} [プッシュ通知の設定]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)も必要です。

## iOSの制限 {#ios-limitations}

iOSオペレーティングシステムは、一部の機能の通知をゲートする場合があります。これらの機能で問題が発生している場合は、iOSのサイレント通知ゲートが原因である可能性があることに注意してください。詳細については、Appleの[インスタンスメソッド](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application)および[未受信通知](https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23)のドキュメントを参照してください。

## サイレント・プッシュ通知を設定する {#setting-up-silent-push-notifications}

サイレントプッシュ通知を使用してバックグラウンド作業をトリガーするには、アプリがバックグラウンドでも通知を受け取れるように設定する必要があります。これを行うには、Xcodeのメインアプリターゲットに、**Signing & Capabilities**ペインを使用してBackground Modesケイパビリティを追加します。**Remote notifications**チェックボックスを選択します。

![Xcodeの「capabilities」の下に「remote notifications」モードのチェックボックスが表示されています。]({% image_buster /assets/img_archive/background_mode.png %} "background mode enabled")

リモート通知バックグラウンドモードが有効になっている場合でも、ユーザーがアプリケーションを強制終了した場合、システムはアプリをバックグラウンドで起動しません。システムによってアプリがバックグラウンドで自動的に起動される前に、ユーザーはアプリケーションを明示的に起動するか、デバイスを再起動する必要があります。

詳細については、[バックグラウンド更新のプッシュ](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app)および `application:didReceiveRemoteNotification:fetchCompletionHandler:` の[ドキュメント](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplicationDelegate_Protocol/index.html#//apple_ref/occ/intfm/UIApplicationDelegate/application:didReceiveRemoteNotification:fetchCompletionHandler:)を参照してください。

## サイレントプッシュ通知の送信 {#sending-silent-push-notifications}

サイレントプッシュ通知を送信するには、プッシュ通知ペイロードで `content-available` フラグを `1` に設定します。

{% alert note %}
Appleがリモート通知と呼ぶものは、`content-available` フラグが設定された通常のプッシュ通知です。
{% endalert %}

`content-available` フラグは、Brazeダッシュボードおよび[メッセージングAPI]({{site.baseurl}}/api/endpoints/messaging/)の[Appleプッシュオブジェクト]({{site.baseurl}}/api/objects_filters/messaging/apple_object/)内で設定できます。

{% alert warning %}
タイトルと本文の両方を `content-available=1` で付与することは、未定義の動作につながる可能性があるため、推奨されません。通知が本当にサイレントであることを確認するには、`content-available` フラグを `1` に設定するときに、タイトルと本文の両方を除外してください。詳細については、[バックグラウンド更新に関するAppleの公式ドキュメント](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app)を参照してください。
{% endalert %}

![プッシュコンポーザーの「settings」タブにある「content-available」チェックボックスを表示するBrazeダッシュボード。]({% image_buster /assets/img_archive/remote_notification.png %} "content available")

サイレントプッシュ通知を送信する際、アプリケーションがイベントを参照できるように、通知ペイロードにデータを含めることもできます。これにより、ネットワークリクエストを削減し、アプリの応答性を向上させることができます。

## 内部プッシュ通知を無視する {#ignoring-internal-push-notifications}

Brazeは、サイレントプッシュ通知を使用して、アンインストール追跡などの特定の高度な機能を内部的に処理します。アプリの起動時やバックグラウンドプッシュ時に自動アクションを実行する場合は、そのアクティビティが内部プッシュ通知によってトリガーされないようにゲーティングすることを検討してください。

たとえば、バックグラウンドプッシュやアプリケーション起動のたびにサーバーに新しいコンテンツを要求するロジックがある場合、不必要なネットワークトラフィックを避けるために、Brazeの内部プッシュがトリガーされないようにすることをお勧めします。Brazeは、ある種の内部プッシュを全ユーザーにほぼ同時に送信するため、内部プッシュからの起動時ネットワーク呼び出しがゲートされていない場合、サーバーに大きな負荷が発生する可能性があります。

### ステップ 1:アプリの自動アクションを確認する {#step-1-check-your-app-for-automatic-actions}

次の場所でアプリケーションの自動アクションを確認し、Brazeの内部プッシュを無視するようにコードを更新します。

1. **プッシュレシーバー。**バックグラウンドプッシュ通知により、`UIApplicationDelegate`の `application:didReceiveRemoteNotification:fetchCompletionHandler:` が呼び出されます。
2. **アプリケーションデリゲート。**バックグラウンドプッシュにより、[中断された](https://developer.apple.com/documentation/uikit/app_and_environment/managing_your_app_s_life_cycle)アプリがバックグラウンドで起動し、`UIApplicationDelegate`の `application:willFinishLaunchingWithOptions:` および `application:didFinishLaunchingWithOptions:` メソッドがトリガーされます。これらのメソッドの `launchOptions` をチェックして、アプリケーションがバックグラウンドプッシュから起動されたかどうかを判断できます。

### ステップ 2:内部プッシュユーティリティメソッドを使用する {#step-2-use-the-internal-push-utility-method}

`Braze.Notifications`の静的ユーティリティメソッドを使用して、アプリがBrazeの内部プッシュを受信したか、または内部プッシュによって起動されたかを確認できます。[`Braze.Notifications.isInternalNotification(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/isinternalnotification(_:))は、すべてのBraze内部プッシュ通知で `true` を返します。これには、アンインストール追跡および[フィーチャーフラグ]({{site.baseurl}}/user_guide/messaging/feature_flags/)同期通知が含まれます。

以下に例を示します。

{% tabs %}
{% tab swift %}


```swift
func application(_ application: UIApplication,
                 didReceiveRemoteNotification userInfo: [AnyHashable : Any],
                 fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
  if (!Braze.Notifications.isInternalNotification(userInfo)) {
    // Gated logic here (for example pinging server for content)
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}


`````````objc
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult result))completionHandler {
  if (![BRZNotifications isInternalNotification:userInfo]) {
    // Gated logic here (for example pinging server for content)
  }
}
```

{% endtab %}
{% endtabs %}