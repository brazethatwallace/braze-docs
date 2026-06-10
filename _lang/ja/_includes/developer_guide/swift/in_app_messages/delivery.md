{% multi_lang_include developer_guide/prerequisites/swift.md %}

## メッセージトリガー {#message-triggers}

### トリガーの種類 {#trigger-types}

アプリ内メッセージは、SDKが以下のカスタムイベントタイプのいずれかを記録した際に自動的にトリガーされます：`Any Purchase`、`Specific Purchase`、`Session Start`、`Custom Event`、および `Push Click`。なお、`Specific Purchase` および `Custom Event` トリガーには堅牢なプロパティフィルターも含まれています。

{% alert note %}
アプリ内メッセージは、APIまたはAPIイベントによってトリガーすることはできません。SDKによって記録されるカスタムイベントによってのみトリガーされます。ロギングの詳細については、[カスタムイベントのログ記録]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift)を参照してください。
{% endalert %}

### 配信セマンティクス {#delivery-semantics}

すべての適格なアプリ内メッセージは、ユーザーのセッション開始時にデバイスに配信されます。配信されると、SDKはアセットをプリフェッチするため、トリガー時にアセットが利用可能となり、表示の遅延を最小限に抑えます。トリガーイベントに複数の適格なアプリ内メッセージがある場合、最も優先度の高いメッセージのみが配信されます。

SDKのセッション開始の仕組みについて詳しくは、[セッションのライフサイクル]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift)を参照してください。

### デフォルトのレート制限 {#default-rate-limit}

デフォルトでは、SDKはトリガーされたアプリ内メッセージを30秒に1回にレート制限しています。

本番アプリでは、この値を10秒未満に設定しないでください。連続するアプリ内メッセージでユーザーが圧倒されるのを防ぐためです。テストやサンプルアプリのフローでは、5秒が一般的な設定です。

テスト用にこの間隔を `0` に設定することもできます。ただし、`0` 秒の間隔は複数のアプリ内メッセージを同時に表示させるものではありません。1つのメッセージが表示されている場合、別のトリガーされたメッセージはアプリ内メッセージスタックで待機し、メッセージが表示可能になるまで待ちます。

これを上書きするには、Brazeインスタンスが初期化される前に、Braze設定の `triggerMinimumTimeInterval` プロパティを更新します。任意の非負の整数に設定でき、最小の時間間隔を秒単位で表します。以下に例を示します。

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
  endpoint: "YOUR-BRAZE-ENDPOINT"
)
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% tab OBJECTIVE-C %}

`````````objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                    endpoint:@"<BRAZE_ENDPOINT>"];
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5;
Braze *braze = [BrazePlugin initBraze:configuration];
AppDelegate.braze = braze;
```
{% endtab %}
{% endtabs %}

## キーと値のペア {#key-value-pairs}

Brazeでキャンペーンを作成する際、キーと値のペアを `extras` として設定できます。これはアプリ内メッセージングオブジェクトがアプリにデータを送信する際に使用できます。以下に例を示します。

{% tabs %}
{% tab swift %}

`````````swift
let customization = message.extras["custom-display"] as? String
if customization == "colorful-slideup" {
  // Perform your custom logic.
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

`````````objc
if ([message.extras[@"custom-display"] isKindOfClass:[NSString class]]) {
  NSString *customization = message.extras[@"custom-display"];
  if ([customization isEqualToString:@"colorful-slideup"]) {
    // Perform your custom logic.
  }
}
```

{% endtab %}
{% endtabs %}

完全な実装については、[サンプルアプリ](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples)でアプリ内メッセージのカスタマイズサンプルを参照してください。

## 自動トリガーを無効にする {#disabling-automatic-triggers}

アプリ内メッセージが自動的にトリガーされるのを防ぐには、以下の手順を実行します。

1. [こちらのiOSの記事](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui)で説明されているように、`BrazeInAppMessageUIDelegate` デリゲートを実装します。
2. `.discard` を返すように `inAppMessage(_:displayChoiceForMessage:)` デリゲートメソッドを更新します。

## 手動でメッセージをトリガーする {#manually-triggering-messages}

### サーバー側のイベントを使用する {#using-a-server-side-event}

サーバー側のイベントを使用してアプリ内メッセージをトリガーするには、デバイスにサイレントプッシュを送信して、デバイスでSDKベースのイベントを記録できるようにします。このSDKイベントは、その後ユーザー向けのアプリ内メッセージをトリガーできます。

#### ステップ1:サイレントプッシュとキーと値のペアを処理する {#step-1-handle-silent-push-and-key-value-pairs}

次の関数を実装し、[`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` メソッド](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application/)内で呼び出します。

{% tabs %}
{% tab swift %}

`````````swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  print("A push was received")
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    AppDelegate.braze?.logCustomEvent("IAM Trigger", properties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

`````````objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [AppDelegate.braze logCustomEvent:@"IAM Trigger" properties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
};
```

{% endtab %}
{% endtabs %}

サイレントプッシュを受信すると、ユーザープロファイルに対してSDKが記録したイベント「アプリ内メッセージトリガー」がログに記録されます。

{% alert important %}
SDKが記録するカスタムイベントの記録にプッシュメッセージが使用されているため、Brazeはこのソリューションを有効にするために、ユーザーごとにプッシュトークンを保存する必要があります。iOSユーザーの場合、BrazeはユーザーがOSのプッシュプロンプトを受け取った時点からのトークンのみを保存します。これ以前では、ユーザーはプッシュを使用して到達できず、上記のソリューションも実行できません。
{% endalert %}

#### ステップ2:サイレントプッシュキャンペーンを作成する {#step-2-create-a-silent-push-campaign}

サーバー送信イベントを介してトリガーされる[サイレントプッシュキャンペーン]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift)を作成します。

![カスタムイベント「server_event」をユーザープロファイルに持つユーザーに配信される、アクションベースの配信アプリ内メッセージキャンペーン。]({% image_buster /assets/img_archive/iosServerSentPush.png %})

プッシュキャンペーンにはキーと値のペアのエクストラを含める必要があります。これは、このプッシュキャンペーンがSDKカスタムイベントを記録するために送信されることを示します。このイベントは次のアプリ内メッセージをトリガーするために使用されます。

![2つのキーと値のペアを持つアクションベースの配信アプリ内メッセージキャンペーン。「CAMPAIGN_NAME」が「In-app message name example」に設定され、「IS_SERVER_EVENT」が「true」に設定されています。]({% image_buster /assets/img_archive/iOSServerPush.png %})

`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` メソッド内のコードはキー `IS_SERVER_EVENT` をチェックし、存在する場合はSDKカスタムイベントをログに記録します。

プッシュペイロードのキーと値のペアのエクストラ内で目的の値を送信することで、イベント名またはイベントプロパティを変更できます。カスタムイベントを記録する際、これらのエクストラはイベント名のパラメータまたはイベントプロパティとして使用できます。

#### ステップ3:アプリ内メッセージキャンペーンを作成する {#step-3-create-an-in-app-message-campaign}

Brazeダッシュボードで、ユーザーに表示されるアプリ内メッセージキャンペーンを作成します。このキャンペーンにはアクションベースの配信を設定し、`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` メソッド内から記録されたカスタムイベントによってトリガーされるようにする必要があります。

以下の例では、イベントプロパティを最初のサイレントプッシュの一部として送信することで、トリガーされる特定のアプリ内メッセージが設定されています。

![カスタムイベント「In-app message trigger」を実行したユーザーに配信される、アクションベースの配信アプリ内メッセージキャンペーン。ここで「campaign_name」は「IAM キャンペーン Name Example」に等しい。]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

{% alert note %}
なお、これらのアプリ内メッセージは、アプリがフォアグラウンドにある間にサイレントプッシュが受信された場合にのみトリガーされます。
{% endalert %}

### 事前定義されたメッセージを表示する {#displaying-a-pre-defined}

事前定義したアプリ内メッセージを手動で表示するには、以下のメソッドを使用します。

`````````swift
if let inAppMessage = AppDelegate.braze?.inAppMessagePresenter?.nextAvailableMessage() {
  AppDelegate.braze?.inAppMessagePresenter?.present(message: inAppMessage)
}
```

### リアルタイムでメッセージを表示する {#displaying-a-message-in-real-time}

ローカルのアプリ内メッセージをリアルタイムで表示することもできます。`inAppMessagePresenter`の[`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:))メソッドを手動で呼び出します。以下に例を示します。

{% tabs %}
{% tab swift %}

`````````swift
let customInAppMessage = Braze.InAppMessage.slideup(
  .init(message: "YOUR_CUSTOM_SLIDEUP_MESSAGE", slideFrom: .bottom, themes: .defaults)
)
AppDelegate.braze?.inAppMessagePresenter?.present(message: customInAppMessage)
```

{% endtab %}
{% tab OBJECTIVE-C %}

`````````objc
BRZInAppMessageRaw *customInAppMessage = [[BRZInAppMessageRaw alloc] init];
customInAppMessage.type = BRZInAppMessageRawTypeSlideup;
customInAppMessage.message = @"YOUR_CUSTOM_SLIDEUP_MESSAGE";
customInAppMessage.slideFrom = BRZInAppMessageRawSlideFromBottom;
customInAppMessage.themes = @{
  @"light": BRZInAppMessageRawTheme.defaultLight,
  @"dark": BRZInAppMessageRawTheme.defaultDark
};
[AppDelegate.braze.inAppMessagePresenter presentMessage:customInAppMessage];
```

{% endtab %}
{% endtabs %}

{% alert note %}
独自のアプリ内メッセージを作成する場合、分析トラッキングはオプトアウトされるため、`message.context` を使用してクリックとインプレッションのロギングを手動で処理する必要があります。
{% endalert %}

## アプリ内メッセージスタック {#the-in-app-message-stack}

### アプリ内メッセージのスタックへの追加 {#adding-in-app-messages-to-the-stack}

ユーザーは、次の状況でアプリ内メッセージを受信できます。

- アプリ内メッセージのトリガーイベントが発生した
- セッションが開始された
- プッシュ通知からアプリを開いた

アプリ内メッセージのトリガーイベントが発生すると、そのメッセージは「スタック」に配置されます。複数のアプリ内メッセージがスタック内にあり、表示を待機している場合、Brazeは最後に受信したアプリ内メッセージを最初に表示します（後入れ先出し）。

ユーザーにアプリ内メッセージを受信する資格がある場合、`BrazeInAppMessagePresenter`がアプリ内メッセージスタックから最新のアプリ内メッセージをリクエストします。スタックはメモリに保存されたアプリ内メッセージのみを保持し、一時停止モードからのアプリ起動間でクリアされます。

### アプリ内メッセージをスタックに返す {#returning-in-app-messages-to-the-stack}

トリガーされたアプリ内メッセージは、次の状況でスタックに返されることがあります。

- アプリがバックグラウンドにあるときに、アプリ内メッセージがトリガーされた。
- 別のアプリ内メッセージが現在表示されている。
- `inAppMessage(_:displayChoiceForMessage:)` [デリゲートメソッド](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb)が `.reenqueue` を返した。

トリガーされたアプリ内メッセージは、ユーザーがアプリ内メッセージを受信する資格がある場合に後で表示されるよう、スタックの最上位に配置されます。

### アプリ内メッセージの破棄 {#discarding-in-app-messages}

トリガーされたアプリ内メッセージは、次の状況では破棄されます。

- `inAppMessage(_:displayChoiceForMessage:)` [デリゲートメソッド](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb)が `.discard` を返した。
- アプリ内メッセージのアセット（画像またはZIPファイル）のダウンロードに失敗した。
- アプリ内メッセージを表示する準備ができていたが、タイムアウト時間が経過した。
- デバイスの向きが、トリガーされたアプリ内メッセージの向きと一致しない。

アプリ内メッセージはスタックから削除されます。破棄された後も、アプリ内メッセージはトリガーイベントの別のインスタンスによって再度トリガーできます。