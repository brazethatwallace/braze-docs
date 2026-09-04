## レート制限 {#rate-limits}

プッシュ通知にはレート制限があるため、アプリケーションで必要なだけ送信しても構いません。iOSとApple Push Notification service（APNs）サーバーが配信頻度をコントロールするため、送信しすぎても問題が発生することはありません。プッシュ通知がスロットリングされている場合、デバイスが次にキープアライブパケットを送信するか、別の通知を受信するまで遅延する可能性があります。

## プッシュ通知の設定 {#setting-up-push-notifications}

### ステップ1:APNsトークンをアップロードする {#step-1-upload-your-apns-token}

{% multi_lang_include developer_guide/swift/apns_token.md %}

### ステップ2:プッシュ機能を有効にする {#step-2-enable-push-capabilities}

Xcodeで、メインアプリターゲットの**Signing & Capabilities**セクションに移動し、プッシュ通知機能を追加します。

![Xcodeプロジェクトの「Signing & Capabilities」セクション]({% image_buster /assets/img_archive/Enable_push_capabilities.png %})

### ステップ3:プッシュ処理を設定する {#step-3-set-up-push-handling}

Swift SDKを使用して、Brazeから受信したリモート通知の処理を自動化できます。これはプッシュ通知を処理する最も簡単な方法であり、推奨される処理方法です。

{% tabs local %}
{% tab 自動 %}
#### ステップ3.1:pushプロパティでオートメーションを有効にする {#step-31-enable-automation-in-the-push-property}

自動プッシュ統合を有効にするには、`push`設定の`automation`プロパティを`true`に設定します。

{% subtabs %}
{% subtab Swift %}
```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}", endpoint: "{YOUR-BRAZE-API-ENDPOINT}")
configuration.push.automation = true
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"{YOUR-BRAZE-API-KEY}" endpoint:@"{YOUR-BRAZE-API-ENDPOINT}"];
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
```

{% endsubtab %}
{% endsubtabs %}

これにより、SDKは以下を行います。
- システム上でプッシュ通知用にアプリケーションを登録します。
- 初期化時にプッシュ通知の認可/許可をリクエストします。
- プッシュ通知関連のシステムデリゲートメソッドの実装を動的に提供します。

{% alert note %}
SDKが実行するオートメーションステップは、コードベース内の既存のプッシュ通知処理統合と互換性があります。SDKはBrazeから受信したリモート通知の処理のみを自動化します。独自またはサードパーティSDKのリモート通知を処理するために実装されたシステムハンドラーは、`automation`が有効になっていても引き続き動作します。
{% endalert %}

{% alert warning %}
プッシュ通知のオートメーションを有効にするには、SDKをメインスレッドで初期化する必要があります。SDK初期化は、アプリケーションの起動完了前、またはAppDelegateの[`application(_:didFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application)実装内で行う必要があります。
SDKの初期化前に追加のセットアップが必要な場合は、[遅延初期化]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift#step-2-set-up-delayed-initialization-optional)のドキュメントページを参照してください。
{% endalert %}

#### ステップ3.2:個別の設定をオーバーライドする（オプション） {#step-32-override-individual-configurations-optional}

より細かい制御が必要な場合、各オートメーションステップを個別に有効または無効にできます。

{% subtabs %}
{% subtab Swift %}

```swift
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = true
configuration.push.automation.requestAuthorizationAtLaunch = false
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
configuration.push.automation.requestAuthorizationAtLaunch = NO;
```

{% endsubtab %}
{% endsubtabs %}

利用可能なすべてのオプションについては[`Braze.Configuration.Push.Automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.class)を、オートメーションの動作の詳細については[`automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.property)を参照してください。
{% endtab %}

{% tab 手動 %}
{% alert note %}
アプリ固有の追加動作にプッシュ通知を利用している場合でも、手動プッシュ通知統合の代わりに自動プッシュ統合を使用できる場合があります。[`subscribeToUpdates(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(_:))メソッドは、Brazeが処理したリモート通知の通知を受け取る方法を提供します。
{% endalert %}

#### ステップ3.1:APNsにプッシュ通知を登録する {#step-31-register-for-push-notifications-with-apns}

アプリの[`application:didFinishLaunchingWithOptions:`デリゲートメソッド](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application)内に適切なコードサンプルを含めて、ユーザーのデバイスがAPNsに登録できるようにします。すべてのプッシュ統合コードをアプリケーションのメインスレッドで呼び出してください。

Brazeは、プッシュアクションボタンサポート用のデフォルトプッシュカテゴリも提供しており、プッシュ登録コードに手動で追加する必要があります。追加の統合手順については、[プッシュアクションボタン]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_customizing-push-categories)を参照してください。

アプリデリゲートの`application:didFinishLaunchingWithOptions:`メソッドに以下のコードを追加します。

{% alert note %}
以下のコードサンプルには、仮プッシュ認証の統合が含まれています（5行目と6行目）。アプリで仮認可を使用する予定がない場合は、`requestAuthorization`オプションに`UNAuthorizationOptionProvisional`を追加するコード行を削除できます。<br>プッシュの仮認証について詳しくは、[iOS通知オプション]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options)をご覧ください。
{% endalert %}

{% subtabs %}
{% subtab Swift %}

```swift
application.registerForRemoteNotifications()
let center = UNUserNotificationCenter.current()
center.setNotificationCategories(Braze.Notifications.categories)
center.delegate = self
var options: UNAuthorizationOptions = [.alert, .sound, .badge]
if #available(iOS 12.0, *) {
  options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
}
center.requestAuthorization(options: options) { granted, error in
  print("Notification authorization, granted: \(granted), error: \(String(describing: error))")
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
[application registerForRemoteNotifications];
UNUserNotificationCenter *center = UNUserNotificationCenter.currentNotificationCenter;
[center setNotificationCategories:BRZNotifications.categories];
center.delegate = self;
UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
if (@available(iOS 12.0, *)) {
  options = options | UNAuthorizationOptionProvisional;
}
[center requestAuthorizationWithOptions:options
                      completionHandler:^(BOOL granted, NSError *_Nullable error) {
                        NSLog(@"Notification authorization, granted: %d, "
                              @"error: %@)",
                              granted, error);
}];
```

{% endsubtab %}
{% endsubtabs %}

{% alert warning %}
デリゲートオブジェクトは、アプリの起動完了前に`center.delegate = self`を同期的に割り当てる必要があります。`application:didFinishLaunchingWithOptions:`内で行うことが推奨されます。これを行わないと、アプリが受信プッシュ通知を見逃す可能性があります。詳しくはAppleの[`UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate)ドキュメントをご覧ください。
アプリが`wipeData()`を呼び出し、同じアプリ実行中に後でBraze SDKを再度有効にする場合は、SDKが使用するデバイストークンを再設定するために`registerForRemoteNotifications()`を再度呼び出す必要があります。
{% endalert %}

#### ステップ3.2:Brazeにプッシュトークンを登録する {#step-32-register-push-tokens-with-braze}

APNs登録が完了したら、結果の`deviceToken`をBrazeに渡して、ユーザーのプッシュ通知を有効にします。

{% subtabs %}
{% subtab Swift %}

アプリの`application(_:didRegisterForRemoteNotificationsWithDeviceToken:)`メソッドに以下のコードを追加します。

```swift
AppDelegate.braze?.notifications.register(deviceToken: deviceToken)
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

アプリの`application:didRegisterForRemoteNotificationsWithDeviceToken:`メソッドに以下のコードを追加します。

```objc
[AppDelegate.braze.notifications registerDeviceToken:deviceToken];
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
`application:didRegisterForRemoteNotificationsWithDeviceToken:`デリゲートメソッドは、`application.registerForRemoteNotifications()`が呼び出されるたびに呼び出されます。<br><br>別のプッシュサービスからBrazeに移行する場合で、ユーザーのデバイスがすでにAPNsに登録されている場合、このメソッドは次回呼び出されたときに既存の登録からトークンを収集するため、ユーザーはプッシュに再度オプトインする必要はありません。
{% endalert %}

#### ステップ3.3:プッシュ処理を有効にする {#step-33-enable-push-handling}

次に、受信したプッシュ通知をBrazeに渡します。このステップは、プッシュ分析のログ記録とリンク処理に必要です。すべてのプッシュ統合コードをアプリケーションのメインスレッドで呼び出してください。

##### デフォルトのプッシュ処理 {#default-push-handling}

{% subtabs %}
{% subtab Swift %}
Brazeのデフォルトプッシュ処理を有効にするには、アプリの`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`メソッドに以下のコードを追加します。

```swift
if let braze = AppDelegate.braze, braze.notifications.handleBackgroundNotification(
  userInfo: userInfo,
  fetchCompletionHandler: completionHandler
) {
  return
}
completionHandler(.noData)
```

次に、アプリの`userNotificationCenter(_:didReceive:withCompletionHandler:)`メソッドに以下を追加します。

```swift
if let braze = AppDelegate.braze, braze.notifications.handleUserNotification(
  response: response,
  withCompletionHandler: completionHandler
) {
  return
}
completionHandler()
```
{% endsubtab %}

{% subtab OBJECTIVE-C %}
Brazeのデフォルトプッシュ処理を有効にするには、アプリケーションの`application:didReceiveRemoteNotification:fetchCompletionHandler:`メソッドに以下のコードを追加します。

```objc
BOOL processedByBraze = AppDelegate.braze != nil && [AppDelegate.braze.notifications handleBackgroundNotificationWithUserInfo:userInfo
                                                                                                       fetchCompletionHandler:completionHandler];
if (processedByBraze) {
  return;
}

completionHandler(UIBackgroundFetchResultNoData);
```

次に、アプリの`(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:`メソッドに以下のコードを追加します。

```objc
BOOL processedByBraze = AppDelegate.braze != nil && [AppDelegate.braze.notifications handleUserNotificationWithResponse:response
                                                                                                  withCompletionHandler:completionHandler];
if (processedByBraze) {
  return;
}

completionHandler();
```
{% endsubtab %}
{% endsubtabs %}

##### フォアグラウンドプッシュ処理 {#foreground-push-handling}

{% subtabs %}
{% subtab Swift %}
フォアグラウンドプッシュ通知を有効にし、受信時にBrazeが認識できるようにするには、`UNUserNotificationCenter.userNotificationCenter(_:willPresent:withCompletionHandler:)`を実装します。ユーザーがフォアグラウンド通知をタップすると、`userNotificationCenter(_:didReceive:withCompletionHandler:)`プッシュデリゲートが呼び出され、Brazeがプッシュクリックイベントをログに記録します。

```swift
func userNotificationCenter(
  _ center: UNUserNotificationCenter,
  willPresent notification: UNNotification,
  withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions
) -> Void) {
  if let braze = AppDelegate.braze {
    // Forward notification payload to Braze for processing.
    braze.notifications.handleForegroundNotification(notification: notification)
  }

  // Configure application's foreground notification display options.
  if #available(iOS 14.0, *) {
    completionHandler([.list, .banner])
  } else {
    completionHandler([.alert])
  }
}
```
{% endsubtab %}

{% subtab OBJECTIVE-C %}
フォアグラウンドプッシュ通知を有効にし、受信時にBrazeが認識できるようにするには、`userNotificationCenter:willPresentNotification:withCompletionHandler:`を実装します。ユーザーがフォアグラウンド通知をタップすると、`userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:`プッシュデリゲートが呼び出され、Brazeがプッシュクリックイベントをログに記録します。

```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
       willPresentNotification:(UNNotification *)notification
         withCompletionHandler:(void (^)(UNNotificationPresentationOptions options))completionHandler {
  if (AppDelegate.braze != nil) {
    // Forward notification payload to Braze for processing.
    [AppDelegate.braze.notifications handleForegroundNotificationWithNotification:notification];
  }

  // Configure application's foreground notification display options.
  if (@available(iOS 14.0, *)) {
    completionHandler(UNNotificationPresentationOptionList | UNNotificationPresentationOptionBanner);
  } else {
    completionHandler(UNNotificationPresentationOptionAlert);
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 通知のテスト {#push-testing}

コマンドラインからアプリ内通知とプッシュ通知をテストする場合は、CURLと[メッセージングAPI]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)を介してターミナルから単一の通知を送信できます。次のフィールドをテストケースの正しい値に置き換える必要があります。

- `YOUR_API_KEY` - **設定** > **APIキー**で確認できます。
- `YOUR_EXTERNAL_USER_ID` - **ユーザー検索**ページで確認できます。詳しくは[ユーザーIDの割り当て]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids#assigning-a-user-id)を参照してください。
- `YOUR_KEY1`（オプション）
- `YOUR_VALUE1`（オプション）

以下の例では、`US-01` インスタンスを使用しています。このインスタンスを使用していない場合は、[APIドキュメント]({{site.baseurl}}/api/basics)を参照して、どのエンドポイントにリクエストを行うかを確認してください。

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert":"Test push",
      "extra": {
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

## プッシュ通知の更新を購読する {#subscribing-to-push-notifications-updates}

Brazeが処理したプッシュ通知のペイロードにアクセスするには、[`Braze.Notifications.subscribeToUpdates(payloadTypes:_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(payloadtypes:_:)/) メソッドを使用します。

`payloadTypes` パラメーターを使用して、プッシュ開封イベント、プッシュ受信イベント、またはその両方を含む通知を購読するかどうかを指定できます。

{% tabs %}
{% tab Swift %}

```swift
// This subscription is maintained through a Braze cancellable, which will observe for changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.notifications.subscribeToUpdates(payloadTypes: [.open, .received]) { payload in
  print("Braze processed notification with title '\(payload.title)' and body '\(payload.body)'")
}
```

{% alert important %}
プッシュ受信イベントは、フォアグラウンド通知と `content-available` バックグラウンド通知に対してのみトリガーされることに注意してください。アプリが終了している間に受信した通知や、`content-available` フィールドのないバックグラウンド通知ではトリガーされません。
{% endalert %}

{% endtab %}

{% tab OBJECTIVE-C %}

```objc
NSInteger filtersValue = BRZNotificationsPayloadTypeFilter.opened.rawValue | BRZNotificationsPayloadTypeFilter.received.rawValue;
BRZNotificationsPayloadTypeFilter *filters = [[BRZNotificationsPayloadTypeFilter alloc] initWithRawValue: filtersValue];
BRZCancellable *cancellable = [notifications subscribeToUpdatesWithPayloadTypes:filters update:^(BRZNotificationsPayload * _Nonnull payload) {
  NSLog(@"Braze processed notification with title '%@' and body '%@'", payload.title, payload.body);
}];
```

{% alert important %}
プッシュ受信イベントは、フォアグラウンド通知と `content-available` バックグラウンド通知に対してのみトリガーされることに注意してください。アプリが終了している間に受信した通知や、`content-available` フィールドのないバックグラウンド通知ではトリガーされません。
{% endalert %}

{% endtab %}

{% endtabs %}
{% alert note %}
自動プッシュ統合を使用している場合、`subscribeToUpdates(_:)` はBrazeが処理したリモート通知について通知を受け取る唯一の方法です。通知がBrazeによって自動的に処理される場合、`UIAppDelegate` および `UNUserNotificationCenterDelegate` のシステムメソッドは呼び出されません。
{% endalert %}

{% alert tip %}
アプリが終了状態にあるときにエンドユーザーが通知をタップした後に購読がトリガーされるように、`application(_:didFinishLaunchingWithOptions:)` でプッシュ通知の購読を作成してください。
{% endalert %}

## フォアグラウンド通知の処理 {#handling-foreground-notifications}

デフォルトでは、アプリがフォアグラウンドにある状態でプッシュ通知が届いた場合、iOSは自動的に通知を表示しません。フォアグラウンドでプッシュ通知を表示し、Brazeの分析で追跡するには、`UNUserNotificationCenterDelegate.userNotificationCenter(_:willPresent:withCompletionHandler:)` の実装内で `handleForegroundNotification(notification:)` メソッドを呼び出します。

### 仕組み {#how-it-works}

`handleForegroundNotification(notification:)` を呼び出すと、Brazeは通知ペイロードを処理して分析データをログに記録し、ディープリンクやボタンアクションを処理します。実際の表示動作は、完了ハンドラーに渡す `UNNotificationPresentationOptions` によってコントロールされます。

```swift
import BrazeKit
import UserNotifications

extension AppDelegate: UNUserNotificationCenterDelegate {
  func userNotificationCenter(
    _ center: UNUserNotificationCenter,
    willPresent notification: UNNotification,
    withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void
  ) {
    // Let Braze process the notification payload
    if let braze = AppDelegate.braze {
      braze.notifications.handleForegroundNotification(notification: notification)
    }

    // Control how the notification appears in the foreground
    if #available(iOS 14.0, *) {
      completionHandler([.banner, .list, .sound])
    } else {
      completionHandler([.alert, .sound])
    }
  }
}
```

完全な例については、Braze Swift SDKリポジトリの[プッシュ通知手動統合サンプル](https://github.com/braze-inc/braze-swift-sdk/blob/e31907eaa0dbd151dc2e6826de66cc494242ba60/Examples/Swift/Sources/PushNotifications-Manual/AppDelegate.swift#L1-L120)を参照してください。

## プッシュプライマー {#push-primers}

プッシュプライマーキャンペーンは、アプリのプッシュ通知をデバイスで有効にするようユーザーに促します。これは、[ノーコードプッシュプライマー]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)を使用して、SDKのカスタマイズなしで行うことができます。

## ダイナミックAPNsゲートウェイ管理 {#dynamic-apns-gateway-management}

ダイナミックApple Push Notification Service（APNs）ゲートウェイ管理は、正しいAPNs環境を自動検出することで、iOSプッシュ通知の信頼性と効率性を向上させます。以前は、プッシュ通知のAPNs環境（開発または本番）を手動で選択する必要があり、ゲートウェイの設定ミス、配信失敗、`BadDeviceToken`エラーが発生することがありました。

ダイナミックAPNsゲートウェイ管理により、次のメリットがあります。

- **信頼性の向上：**通知は常に正しいAPNs環境に配信されるため、配信失敗が減少します。
- **設定の簡素化：**APNsゲートウェイ設定を手動で管理する必要がなくなります。
- **エラー耐性：**無効なゲートウェイ値や欠落したゲートウェイ値が適切に処理され、中断のないサービスが提供されます。

### 前提条件 {#prerequisites}

Brazeは、以下のSDKバージョン要件を満たすiOSのプッシュ通知に対して、ダイナミックAPNsゲートウェイ管理をサポートしています。

{% sdk_min_versions swift:10.0.0 %}

### 仕組み

iOSアプリがBraze Swift SDKと統合されると、[`aps-environment`](https://developer.apple.com/documentation/bundleresources/entitlements/aps-environment)を含むデバイス関連データが、利用可能な場合にBraze SDK APIに送信されます。`apns_gateway`の値は、アプリが開発（`dev`）または本番（`prod`）のAPNs環境を使用しているかを示します。

Brazeは各デバイスについて報告されたゲートウェイ値も保存します。新しい有効なゲートウェイ値を受信すると、Brazeは保存された値を自動的に更新します。

Brazeがプッシュ通知を送信する場合：

- デバイスに有効なゲートウェイ値（devまたはprod）が保存されている場合、Brazeはそれを使用して正しいAPNs環境を決定します。
- ゲートウェイ値が保存されていない場合、Brazeは**アプリ設定**ページで構成されたAPNs環境をデフォルトとして使用します。

### よくある質問 {#frequently-asked-questions}

#### この機能が導入された理由は何ですか？ {#why-was-this-feature-introduced}

ダイナミックAPNsゲートウェイ管理により、正しい環境が自動的に選択されます。以前は、APNsゲートウェイを手動で設定する必要があり、`BadDeviceToken`エラー、トークンの無効化、APNsのレート制限の問題が発生する可能性がありました。

#### プッシュ配信パフォーマンスにどのような影響がありますか？ {#how-does-this-impact-push-delivery-performance}

この機能は、プッシュトークンを常に正しいAPNs環境にルーティングすることで配信率を向上させ、ゲートウェイの設定ミスによる失敗を回避します。

#### この機能を無効にできますか？ {#can-i-disable-this-feature}

ダイナミックAPNsゲートウェイ管理はデフォルトで有効になっており、信頼性の向上を提供します。手動でのゲートウェイ選択が必要な特定のユースケースがある場合は、[Brazeサポート]({{site.baseurl}}/user_guide/administer/personal/braze_support)にお問い合わせください。