---
nav_title: 統合
article_title: iOS 向けのプッシュ統合
platform: iOS
page_order: 0
description: "この参照記事では、iOS アプリケーションにプッシュ通知を統合する方法について説明します。"
channel:
  - push
search_rank: 5

local_redirect:
  ios-10-rich-notifications: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/'
local_redirect:
  creating-a-service-extension: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#creating-a-service-extension'
local_redirect:
  setting-up-the-service-extension: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#setting-up-the-service-extension'
local_redirect:
  creating-a-rich-notification-in-your-dashboard: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#creating-a-rich-notification-in-your-dashboard'
local_redirect:
  push-action-buttons-integration: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/'
local_redirect:
  step-1-adding-braze-default-push-categories: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/#step-1-adding-braze-default-push-categories'
local_redirect:
  step-2-enable-interactive-push-handling: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/#step-2-enable-interactive-push-handling'

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# プッシュ統合 {#push-integration}

## ステップ 1:APNsトークンのアップロード {#step-1-upload-your-apns-token}

{% multi_lang_include developer_guide/swift/apns_token.md %}

## ステップ 2:プッシュ機能の有効化 {#step-2-enable-push-capabilities}

プロジェクト設定で、**Capabilities**タブの**Push Notifications**機能がオンになっていることを確認します。

![プロジェクト設定で、CapabilitiesタブのPush Notifications機能がオンになっていることを確認します。]({% image_buster /assets/img_archive/Enable_push_capabilities.png %})

開発用と本番用で別々のプッシュ証明書を使用している場合は、**General**タブの**Automatically manage signing**チェックボックスをオフにしてください。これにより、ビルド構成ごとに異なるプロビジョニングプロファイルを選択できるようになります。Xcodeの自動コード署名機能は開発用の署名のみを行うためです。

![Xcodeプロジェクト設定のGeneralタブ。このタブで「Automatically manage signing」オプションがオフになっています。]({% image_buster /assets/img_archive/xcode8_auto_signing.png %})

## ステップ 3:プッシュ通知の登録 {#step-3-register-for-push-notifications}

ユーザーのデバイスがAPNsに登録するために、適切なコードサンプルをアプリの`application:didFinishLaunchingWithOptions:`デリゲートメソッドに含める必要があります。すべてのプッシュ統合コードをアプリケーションのメインスレッドで呼び出すようにしてください。

Brazeは、プッシュアクションボタンをサポートするためのデフォルトのプッシュカテゴリも提供しており、プッシュ登録コードに手動で追加する必要があります。追加の統合ステップについては、[プッシュアクションボタン]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/action_buttons)を参照してください。

{% alert warning %}
[プッシュのベストプラクティス]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/troubleshooting)に記載されているカスタムプッシュプロンプトを実装している場合は、ユーザーがアプリにプッシュ権限を付与した後、**アプリが実行されるたびに**以下のコードを呼び出すようにしてください。**[デバイストークンは任意に変更される可能性がある](https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/BackgroundExecution/BackgroundExecution.html)ため、アプリはAPNsに再登録する必要があります。**
{% endalert %}

### UserNotificationフレームワークの使用（iOS 10以降） {#using-usernotification-framework-ios-10}

iOS 10で導入された`UserNotifications`フレームワーク（推奨）を使用している場合は、アプリデリゲートの`application:didFinishLaunchingWithOptions:`メソッドに以下のコードを追加してください。

{% alert important %}
以下のコードサンプルには、仮プッシュ認証の統合が含まれています（5行目と6行目）。アプリで仮認証を使用する予定がない場合は、`requestAuthorization`オプションに`UNAuthorizationOptionProvisional`を追加するコード行を削除できます。<br>プッシュの仮認証について詳しくは、[iOS通知オプション]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options)を参照してください。
{% endalert %}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
if (floor(NSFoundationVersionNumber) > NSFoundationVersionNumber_iOS_9_x_Max) {
  UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
  center.delegate = self;
  UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
  if (@available(iOS 12.0, *)) {
  options = options | UNAuthorizationOptionProvisional;
  }
  [center requestAuthorizationWithOptions:options
                        completionHandler:^(BOOL granted, NSError * _Nullable error) {
                          [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];
  [[UIApplication sharedApplication] registerForRemoteNotifications];
} else {
  UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:nil];
  [[UIApplication sharedApplication] registerForRemoteNotifications];
  [[UIApplication sharedApplication] registerUserNotificationSettings:settings];
}
```

{% endtab %}
{% tab swift %}

```swift
if #available(iOS 10, *) {
  let center = UNUserNotificationCenter.current()
  center.delegate = self as? UNUserNotificationCenterDelegate
  var options: UNAuthorizationOptions = [.alert, .sound, .badge]
  if #available(iOS 12.0, *) {
    options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
  }
  center.requestAuthorization(options: options) { (granted, error) in
    Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
  }
  UIApplication.shared.registerForRemoteNotifications()
} else {
  let types : UIUserNotificationType = [.alert, .badge, .sound]
  let setting : UIUserNotificationSettings = UIUserNotificationSettings(types:types, categories:nil)
  UIApplication.shared.registerUserNotificationSettings(setting)
  UIApplication.shared.registerForRemoteNotifications()
}
```

{% endtab %}
{% endtabs %}


{% alert warning %}
デリゲートオブジェクトは、アプリの起動が完了する前に`center.delegate = self`を使用して同期的に割り当てる必要があります。できれば`application:didFinishLaunchingWithOptions:`内で行ってください。これを行わないと、アプリが受信プッシュ通知を受け取れない場合があります。詳しくは、Appleの[`UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate)ドキュメントを参照してください。
{% endalert %}

### UserNotificationsフレームワークを使用しない場合 {#without-usernotifications-framework}

`UserNotifications`フレームワークを使用していない場合は、アプリデリゲートの`application:didFinishLaunchingWithOptions:`メソッドに以下のコードを追加してください。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:nil];
[[UIApplication sharedApplication] registerForRemoteNotifications];
[[UIApplication sharedApplication] registerUserNotificationSettings:settings];
```

{% endtab %}
{% tab swift %}

```swift
let types : UIUserNotificationType = UIUserNotificationType.Badge | UIUserNotificationType.Sound | UIUserNotificationType.Alert
var setting : UIUserNotificationSettings = UIUserNotificationSettings(forTypes: types, categories: nil)
UIApplication.shared.registerUserNotificationSettings(setting)
UIApplication.shared.registerForRemoteNotifications()
```

{% endtab %}
{% endtabs %}

## ステップ 4:Brazeにプッシュトークンを登録する {#step-4-register-push-tokens-with-braze}

APNs登録が完了したら、以下のメソッドを変更して、結果の`deviceToken`をBrazeに渡し、ユーザーがプッシュ通知を受信できるようにする必要があります。

{% tabs %}
{% tab OBJECTIVE-C %}

`application:didRegisterForRemoteNotificationsWithDeviceToken:`メソッドに以下のコードを追加します。

```objc
[[Appboy sharedInstance] registerDeviceToken:deviceToken];
```

{% endtab %}
{% tab swift %}

アプリの`application(_:didRegisterForRemoteNotificationsWithDeviceToken:)`メソッドに以下のコードを追加します。

```swift
Appboy.sharedInstance()?.registerDeviceToken(deviceToken)
```

{% endtab %}
{% endtabs %}

{% alert important %}
`application:didRegisterForRemoteNotificationsWithDeviceToken:`デリゲートメソッドは、`[[UIApplication sharedApplication] registerForRemoteNotifications]`が呼び出されるたびに呼び出されます。他のプッシュサービスからBrazeに移行する場合で、ユーザーのデバイスがすでにAPNsに登録されている場合、このメソッドは次回呼び出された際に既存の登録からトークンを収集するため、ユーザーがプッシュ通知に再度オプトインする必要はありません。
{% endalert %}

## ステップ 5:プッシュ処理の有効化 {#step-5-enable-push-handling}

以下のコードは、受信したプッシュ通知をBrazeに渡すもので、プッシュ分析とリンク処理のログ記録に必要です。すべてのプッシュ統合コードをアプリケーションのメインスレッドで呼び出すようにしてください。

### iOS 10以降

iOS 10以降に対応してビルドする場合は、`UserNotifications`フレームワークを統合し、以下の手順を実行することをお勧めします。

{% tabs %}
{% tab OBJECTIVE-C %}

アプリケーションの`application:didReceiveRemoteNotification:fetchCompletionHandler:`メソッドに以下のコードを追加します。

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo
                      fetchCompletionHandler:completionHandler];
```

次に、アプリの`(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:`メソッドに以下のコードを追加します。

```objc
[[Appboy sharedInstance] userNotificationCenter:center
                 didReceiveNotificationResponse:response
                          withCompletionHandler:completionHandler];
```

**フォアグラウンドプッシュの処理**

アプリがフォアグラウンドにある状態でプッシュ通知を表示するには、`userNotificationCenter:willPresentNotification:withCompletionHandler:`を実装します。

```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
       willPresentNotification:(UNNotification *)notification
         withCompletionHandler:(void (^)(UNNotificationPresentationOptions options))completionHandler {
  if (@available(iOS 14.0, *)) {
    completionHandler(UNNotificationPresentationOptionList | UNNotificationPresentationOptionBanner);
  } else {
    completionHandler(UNNotificationPresentationOptionAlert);
  }
}
```

フォアグラウンド通知がクリックされると、iOS 10のプッシュデリゲート`userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:`が呼び出され、Brazeがプッシュクリックイベントを記録します。

{% endtab %}
{% tab swift %}

アプリの`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`メソッドに以下のコードを追加します。

```swift
Appboy.sharedInstance()?.register(application,
                                            didReceiveRemoteNotification: userInfo,
                                            fetchCompletionHandler: completionHandler)
```

次に、アプリの`userNotificationCenter(_:didReceive:withCompletionHandler:)`メソッドに以下のコードを追加します。

```swift
Appboy.sharedInstance()?.userNotificationCenter(center,
                                               didReceive: response,
                                               withCompletionHandler: completionHandler)
```

**フォアグラウンドプッシュの処理**

アプリがフォアグラウンドにある状態でプッシュ通知を表示するには、`userNotificationCenter(_:willPresent:withCompletionHandler:)`を実装します。

```swift
func userNotificationCenter(_ center: UNUserNotificationCenter,
                              willPresent notification: UNNotification,
                              withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {
  if #available(iOS 14.0, *) {
    completionHandler([.list, .banner]);
  } else {
    completionHandler([.alert]);
  }
}
```

フォアグラウンド通知がクリックされると、iOS 10のプッシュデリゲート`userNotificationCenter(_:didReceive:withCompletionHandler:)`が呼び出され、Brazeがプッシュクリックイベントを記録します。

{% endtab %}
{% endtabs %}

### iOS 10より前 {#pre-ios-10}

iOS 10では動作が更新され、プッシュがクリックされたときに`application:didReceiveRemoteNotification:fetchCompletionHandler:`が呼び出されなくなりました。このため、iOS 10以降向けのビルドに更新せず`UserNotifications`フレームワークを使用しない場合は、以前の統合方式とは異なり、古いスタイルの両方のデリゲートからBrazeを呼び出す必要があります。

SDK < iOS 10向けにビルドするアプリの場合は、以下の手順に従ってください。

{% tabs %}
{% tab OBJECTIVE-C %}

プッシュ通知の開封トラッキングを有効にするには、アプリの`application:didReceiveRemoteNotification:fetchCompletionHandler:`メソッドに以下のコードを追加します。

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo
                      fetchCompletionHandler:completionHandler];
```

iOS 10でのプッシュ分析をサポートするには、アプリの`application:didReceiveRemoteNotification:`デリゲートメソッドにも以下のコードを追加する必要があります。

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo];
```

{% endtab %}
{% tab swift %}

プッシュ通知の開封トラッキングを有効にするには、アプリの`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`メソッドに以下のコードを追加します。

```swift
Appboy.sharedInstance()?.register(application,
  didReceiveRemoteNotification: userInfo,
  fetchCompletionHandler: completionHandler)
```

iOS 10でのプッシュ分析をサポートするには、アプリの`application(_:didReceiveRemoteNotification:)`デリゲートメソッドにも以下のコードを追加する必要があります。

```swift
Appboy.sharedInstance()?.register(application,
  didReceiveRemoteNotification: userInfo)
```

{% endtab %}
{% endtabs %}

## ステップ 6: ディープリンク {#step-6-deep-linking}

プッシュからアプリへのディープリンクは、標準のプッシュ統合ドキュメントを通じて自動的に処理されます。アプリ内の特定の場所にディープリンクを追加する方法について詳しくは、[高度なユースケース]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/advanced_use_cases/linking#linking-handling-customization)を参照してください。

## ステップ 7:ユニットテスト（オプション） {#step-7-unit-tests-optional}

ここまでの統合ステップにテストカバレッジを追加するには、[プッシュユニットテスト]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/unit_tests)を実装してください。