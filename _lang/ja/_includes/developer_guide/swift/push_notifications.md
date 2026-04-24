## レート制限

プッシュ通知にはレート制限があるため、アプリケーションで必要なだけ送信しても構いません。iOS と Apple Push Notification service (APNs) サーバーが配信頻度を制御するため、送信しすぎても問題が発生することはありません。プッシュ通知がスロットリングされている場合、デバイスが次にキープアライブパケットを送信するか、別の通知を受信するまで遅延する可能性があります。

## プッシュ通知の設定

### ステップ 1: APNs トークンをアップロードする

{% multi_lang_include developer_guide/swift/apns_token.md %}

### ステップ 2: プッシュ機能を有効にする

Xcode で、メインアプリターゲットの **Signing & Capabilities** セクションに移動し、プッシュ通知機能を追加します。

![Xcode プロジェクト内の「Signing & Capabilities」セクション。]({% image_buster /assets/img_archive/Enable_push_capabilities.png %})

### ステップ 3: プッシュ処理を設定する

Swift SDK を使って、Braze から受信したリモート通知の処理を自動化できます。これがプッシュ通知を扱う最も簡単な方法であり、推奨される処理方法です。

{% tabs local %}
{% tab Automatic %}
#### ステップ 3.1: プッシュプロパティでオートメーションを有効にする

自動プッシュ統合を有効にするには、`push` 設定の `automation` プロパティを `true` に設定します。

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

これにより、SDK に次のことが指示されます。
- プッシュ通知用のアプリケーションをシステムに登録する。
- 初期化時にプッシュ通知の認証/許可を要求する。
- プッシュ通知関連のシステムデリゲートメソッドの実装をダイナミックに提供する。

{% alert note %}
SDK によって実行されるオートメーションステップは、コードベース内の既存のプッシュ通知処理統合と互換性があります。SDK は、Braze から受信したリモート通知の処理のみを自動化します。`automation` が有効になっている場合、独自または別のサードパーティ SDK のリモート通知を処理するために実装されたシステムハンドラは、引き続き機能します。
{% endalert %}

{% alert warning %}
プッシュ通知のオートメーションを有効にするには、SDK をメインスレッドで初期化する必要があります。SDK の初期化は、アプリケーションの起動が完了する前、または AppDelegate の [`application(_:didFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) 実装で行う必要があります。
アプリケーションが SDK を初期化する前に追加の設定を必要とする場合は、[遅延初期化]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=swift)に関するドキュメントページを参照してください。
{% endalert %}

#### ステップ 3.2: 個別の設定を上書きする（オプション）

よりきめ細かいコントロールのために、各オートメーションステップを個別に有効または無効にできます。

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

使用可能なすべてのオプションについては [`Braze.Configuration.Push.Automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.class) を、オートメーション動作の詳細については [`automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.property) を参照してください。
{% endtab %}

{% tab Manual %}
{% alert note %}
アプリ固有の追加動作をプッシュ通知に依存している場合でも、手動プッシュ通知統合ではなく自動プッシュ統合を使用できる場合があります。[`subscribeToUpdates(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(_:)) メソッドは、Braze が処理したリモート通知の通知を受け取る方法を提供します。
{% endalert %}

#### ステップ 3.1: APNs でプッシュ通知に登録する

ユーザーのデバイスが APNs に登録できるように、アプリの [`application:didFinishLaunchingWithOptions:` デリゲートメソッド](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application)内に適切なコードサンプルを含めてください。アプリケーションのメインスレッドですべてのプッシュ統合コードを呼び出すようにしてください。

Braze には、プッシュアクションボタンをサポートするデフォルトのプッシュカテゴリーも用意されており、プッシュ登録コードに手動で追加する必要があります。その他の統合ステップについては、[プッシュアクションボタン]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_customizing-push-categories)を参照してください。

アプリデリゲートの `application:didFinishLaunchingWithOptions:` メソッドに以下のコードを追加します。

{% alert note %}
次のコードサンプルには、仮のプッシュ認証の統合が含まれています（5行目と6行目）。アプリで仮許可を使用する予定がない場合は、`requestAuthorization` オプションに `UNAuthorizationOptionProvisional` を追加するコード行を削除できます。<br>プッシュ仮認証の詳細については、[iOS 通知オプション]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/)をご覧ください。
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
アプリの起動が完了する前に、`center.delegate = self` を使用してデリゲートオブジェクトを同期的に割り当てる必要があります（可能であれば `application:didFinishLaunchingWithOptions:` で）。そうしないと、アプリがプッシュ通知を受信できなくなる可能性があります。詳細については、Apple の [`UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate) ドキュメントを参照してください。
アプリが `wipeData()` を呼び出し、その後同じアプリ実行中に Braze SDK を再度有効にする場合は、SDK が使用するデバイストークンを再取得するために `registerForRemoteNotifications()` を再度呼び出す必要があります。
{% endalert %}

#### ステップ 3.2: Braze にプッシュトークンを登録する

APNs の登録が完了したら、結果の `deviceToken` を Braze に渡して、ユーザーのプッシュ通知を有効にします。

{% subtabs %}
{% subtab Swift %}

アプリの `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)` メソッドに次のコードを追加します。

```swift
AppDelegate.braze?.notifications.register(deviceToken: deviceToken)
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

アプリの `application:didRegisterForRemoteNotificationsWithDeviceToken:` メソッドに次のコードを追加します。

```objc
[AppDelegate.braze.notifications registerDeviceToken:deviceToken];
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
`application:didRegisterForRemoteNotificationsWithDeviceToken:` デリゲートメソッドは、`application.registerForRemoteNotifications()` の呼び出し後に毎回呼び出されます。<br><br>他のプッシュサービスから Braze に移行する場合、ユーザーのデバイスがすでに APNs に登録されていれば、このメソッドは次回呼び出された際に既存の登録からトークンを収集するため、ユーザーがプッシュに再オプトインする必要はありません。
{% endalert %}

#### ステップ 3.3: プッシュ処理を有効にする

次に、受信したプッシュ通知を Braze に渡します。このステップは、プッシュ分析とリンク処理のログ記録に必要です。アプリケーションのメインスレッドですべてのプッシュ統合コードを呼び出すようにしてください。

##### デフォルトのプッシュ処理

{% subtabs %}
{% subtab Swift %}
Braze のデフォルトプッシュ処理を有効にするには、アプリの `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` メソッドに以下のコードを追加します。

```swift
if let braze = AppDelegate.braze, braze.notifications.handleBackgroundNotification(
  userInfo: userInfo,
  fetchCompletionHandler: completionHandler
) {
  return
}
completionHandler(.noData)
```

次に、アプリの `userNotificationCenter(_:didReceive:withCompletionHandler:)` メソッドに以下を追加します。

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
Braze のデフォルトプッシュ処理を有効にするには、アプリケーションの `application:didReceiveRemoteNotification:fetchCompletionHandler:` メソッドに以下のコードを追加します。

```objc
BOOL processedByBraze = AppDelegate.braze != nil && [AppDelegate.braze.notifications handleBackgroundNotificationWithUserInfo:userInfo
                                                                                                       fetchCompletionHandler:completionHandler];
if (processedByBraze) {
  return;
}

completionHandler(UIBackgroundFetchResultNoData);
```

次に、アプリの `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` メソッドに次のコードを追加します。

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

##### フォアグラウンドでのプッシュ処理

{% subtabs %}
{% subtab Swift %}
フォアグラウンドのプッシュ通知を有効にし、受信時に Braze がそれを認識できるようにするには、`UNUserNotificationCenter.userNotificationCenter(_:willPresent:withCompletionHandler:)` を実装します。ユーザーがフォアグラウンド通知をタップすると、`userNotificationCenter(_:didReceive:withCompletionHandler:)` プッシュデリゲートが呼び出され、Braze はプッシュクリックイベントを記録します。

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
フォアグラウンドのプッシュ通知を有効にし、受信時に Braze がそれを認識できるようにするには、`userNotificationCenter:willPresentNotification:withCompletionHandler:` を実装します。ユーザーがフォアグラウンド通知をタップすると、`userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` プッシュデリゲートが呼び出され、Braze はプッシュクリックイベントを記録します。

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

コマンドラインからアプリ内通知とプッシュ通知をテストする場合は、CURL と[メッセージング API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) を介してターミナルから単一の通知を送信できます。次のフィールドをテストケースの正しい値に置き換える必要があります。

- `YOUR_API_KEY` - **設定** > **API キー**で確認できます。
- `YOUR_EXTERNAL_USER_ID` - **ユーザーを検索**ページで確認できます。詳しくは[ユーザー ID の割り当て]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#assigning-a-user-id)を参照してください。
- `YOUR_KEY1`（オプション）
- `YOUR_VALUE1`（オプション）

以下の例では、`US-01` インスタンスを使用しています。このインスタンスを使用していない場合は、[API ドキュメント]({{site.baseurl}}/api/basics/)を参照して、どのエンドポイントにリクエストを行うかを確認してください。

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

## プッシュ通知の更新を購読する

Braze が処理したプッシュ通知ペイロードにアクセスするには、[`Braze.Notifications.subscribeToUpdates(payloadTypes:_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(payloadtypes:_:)/) メソッドを使用します。

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
プッシュ受信イベントは、フォアグラウンド通知と `content-available` バックグラウンド通知に対してのみトリガーされます。終了中に受信した通知や、`content-available` フィールドのないバックグラウンド通知ではトリガーされません。
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
プッシュ受信イベントは、フォアグラウンド通知と `content-available` バックグラウンド通知に対してのみトリガーされます。終了中に受信した通知や、`content-available` フィールドのないバックグラウンド通知ではトリガーされません。
{% endalert %}

{% endtab %}

{% endtabs %}
{% alert note %}
自動プッシュ統合を使用する場合、Braze によって処理されるリモート通知の通知を受け取る唯一の方法は `subscribeToUpdates(_:)` です。`UIAppDelegate` と `UNUserNotificationCenterDelegate` のシステムメソッドは、通知が Braze によって自動的に処理されるときには呼び出されません。
{% endalert %}

{% alert tip %}
`application(_:didFinishLaunchingWithOptions:)` でプッシュ通知のサブスクリプションを作成し、アプリが終了状態にある間にエンドユーザーが通知をタップした後にサブスクリプションがトリガーされるようにしてください。
{% endalert %}

## フォアグラウンド通知の処理

デフォルトでは、アプリがフォアグラウンドにあるときにプッシュ通知が届いても、iOS は自動的に表示しません。プッシュ通知をフォアグラウンドで表示し、Braze の分析でトラッキングするには、`UNUserNotificationCenterDelegate.userNotificationCenter(_:willPresent:withCompletionHandler:)` の実装内で `handleForegroundNotification(notification:)` メソッドを呼び出します。

### 仕組み

`handleForegroundNotification(notification:)` を呼び出すと、Braze は通知ペイロードを処理して分析データを記録し、ディープリンクやボタンアクションを処理します。実際の表示動作は、完了ハンドラに渡す `UNNotificationPresentationOptions` によって制御されます。

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

完全な例については、Braze Swift SDK リポジトリ内の[プッシュ通知手動統合サンプル](https://github.com/braze-inc/braze-swift-sdk/blob/e31907eaa0dbd151dc2e6826de66cc494242ba60/Examples/Swift/Sources/PushNotifications-Manual/AppDelegate.swift#L1-L120)を参照してください。

## プッシュプライマー {#push-primers}

プッシュプライマーキャンペーンでは、アプリのデバイスでプッシュ通知を有効にするようユーザーに促します。これは、[ノーコードプッシュプライマー]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)を使用して、SDK のカスタマイズなしで行うことができます。

## ダイナミック APNs ゲートウェイ管理

ダイナミック Apple Push Notification service (APNs) ゲートウェイ管理は、適切な APNs 環境を自動的に検出することで、iOS プッシュ通知の信頼性と効率性を高めます。以前は、プッシュ通知用に APNs 環境（開発環境または本番環境）を手動で選択する必要があり、ゲートウェイ設定の誤りや配信失敗、`BadDeviceToken` エラーが発生することがありました。

ダイナミック APNs ゲートウェイ管理により、以下のメリットがあります。

- **信頼性の向上:** 通知は常に正しい APNs 環境に配信されるため、配信失敗が減少します。
- **設定の簡素化:** APNs ゲートウェイの設定を手動で管理する必要がなくなります。
- **エラー耐性:** 無効または欠落したゲートウェイ値は適切に処理され、サービスが中断されることはありません。

### 前提条件

Braze は iOS 向けプッシュ通知のダイナミック APNs ゲートウェイ管理をサポートしています。以下の SDK バージョン要件を満たす必要があります。

{% sdk_min_versions swift:10.0.0 %}

### 仕組み

iOS アプリが Braze Swift SDK と統合する場合、利用可能であれば [`aps-environment`](https://developer.apple.com/documentation/bundleresources/entitlements/aps-environment) を含むデバイス関連データを Braze SDK API に送信します。`apns_gateway` 値は、アプリが開発用（`dev`）または本番用（`prod`）の APNs 環境を使用しているかを示します。

Braze は各デバイスについて報告されたゲートウェイ値も保存します。新しい有効なゲートウェイ値が受信された場合、Braze は保存された値を自動的に更新します。

Braze がプッシュ通知を送信するとき：

- デバイスに有効なゲートウェイ値（dev または prod）が保存されている場合、Braze はそれを使用して正しい APNs 環境を決定します。
- ゲートウェイ値が保存されていない場合、Braze は**アプリ設定**ページで設定された APNs 環境をデフォルトとして使用します。

### よくある質問

#### なぜこの機能が導入されたのですか？

ダイナミック APNs ゲートウェイ管理により、適切な環境が自動的に選択されます。以前は、APNs ゲートウェイを手動で設定する必要があり、`BadDeviceToken` エラーやトークンの無効化、さらには APNs のレート制限の問題が発生する可能性がありました。

#### プッシュ配信パフォーマンスにどのような影響がありますか？

この機能は、プッシュトークンを常に正しい APNs 環境にルーティングすることで配信率を向上させ、誤設定されたゲートウェイによる失敗を回避します。

#### この機能を無効にできますか？

ダイナミック APNs ゲートウェイ管理はデフォルトで有効になっており、信頼性の向上を提供します。手動でのゲートウェイ選択が必要な具体的なユースケースがある場合は、[Braze サポート]({{site.baseurl}}/user_guide/administrative/access_braze/support/)にお問い合わせください。