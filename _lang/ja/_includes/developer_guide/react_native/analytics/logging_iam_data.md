{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## ロギングのメソッド {#methods-for-logging}

これらのメソッドを使用するには、`BrazeInAppMessage` インスタンスを渡して分析をログに記録し、アクションを実行します。

| メソッド                                                    | 説明                                                                           |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `logInAppMessageClicked(inAppMessage)`                    | 提供されたアプリ内メッセージデータのクリックを記録します。                                    |
| `logInAppMessageImpression(inAppMessage)`                 | 提供されたアプリ内メッセージデータのインプレッションを記録します。                              |
| `logInAppMessageButtonClicked(inAppMessage, buttonId)`    | 提供されたアプリ内メッセージデータとボタンIDのボタンクリックを記録します。               |
| `hideCurrentInAppMessage()`                               | 現在表示されているアプリ内メッセージを閉じます。                                     |
| `performInAppMessageAction(inAppMessage)`                 | アプリ内メッセージのアクションを実行します。                                            |
| `performInAppMessageButtonAction(inAppMessage, buttonId)` | アプリ内メッセージボタンのアクションを実行します。                                     |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ロギングのメソッド" }

## メッセージデータの処理 {#handling-message-data}

ほとんどの場合、`Braze.addListener` メソッドを使用して、アプリ内メッセージからのデータを処理するイベントリスナーを登録できます。

さらに、`Braze.subscribeToInAppMessage` メソッドを呼び出して、アプリ内メッセージがトリガーされたときにSDKに `inAppMessageReceived` イベントを発行させることで、JavaScriptレイヤーのアプリ内メッセージデータにアクセスできます。アプリ内メッセージがトリガーされてリスナーによって受信されたときに独自のコードを実行するには、このメソッドにコールバックを渡します。

メッセージデータの処理方法をカスタマイズするには、以下の実装例を参照してください。

{% tabs local %}
{% tab basic %}
デフォルトの動作を強化するため、またはネイティブのiOSやAndroidコードをカスタマイズするアクセス権がない場合は、デフォルトのUIを無効にしながら、Brazeからアプリ内メッセージイベントを受信することをお勧めします。デフォルトのUIを無効にするには、`Braze.subscribeToInAppMessage` メソッドに `false` を渡し、アプリ内メッセージデータを使用してJavaScriptで独自のメッセージを作成します。デフォルトのUIを無効にする場合は、メッセージの分析を手動でログに記録する必要があります。

```javascript
import Braze from "@braze/react-native-sdk";

// Option 1: Listen for the event directly via `Braze.addListener`.
//
// You may use this method to accomplish the same thing if you don't
// wish to make any changes to the default Braze UI.
Braze.addListener(Braze.Events.IN_APP_MESSAGE_RECEIVED, (event) => {
  console.log(event.inAppMessage);
});

// Option 2: Call `subscribeToInAppMessage`.
//
// Pass in `false` to disable the automatic display of in-app messages.
Braze.subscribeToInAppMessage(false, (event) => {
  console.log(event.inAppMessage);
  // Use `event.inAppMessage` to construct your own custom message UI.
});
```
{% endtab %}

{% tab advanced %}
組み込みUIを使用してアプリ内メッセージを表示するかどうかを決定するためのより高度なロジックを組み込むには、ネイティブレイヤーを介してアプリ内メッセージを実装します。

{% alert warning %}
これは高度なカスタマイズオプションであるため、デフォルトのBraze実装をオーバーライドすると、アプリ内メッセージイベントをJavaScriptリスナーに送信するロジックも無効になることに注意してください。[アプリ内メッセージデータへのアクセス](#accessing-in-app-message-data)の説明に従って `Braze.subscribeToInAppMessage` または `Braze.addListener` を引き続き使用する場合は、イベントの発行を自分で処理する必要があります。
{% endalert %}

{% subtabs %}
{% subtab Android %}
[カスタムマネージャーリスナー]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android#android_setting-custom-manager-listeners)に関するAndroidの記事で説明されているように、`IInAppMessageManagerListener` を実装します。`beforeInAppMessageDisplayed` 実装では、`inAppMessage` データにアクセスしてJavaScriptレイヤーに送信し、戻り値に基づいてネイティブメッセージを表示するかどうかを決定できます。

これらの値の詳細については、[Androidのドキュメント]({{site.baseurl}}/developer_guide/in_app_messages)を参照してください。

```java
// In-app messaging
@Override
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
    WritableMap parameters = new WritableNativeMap();
    parameters.putString("inAppMessage", inAppMessage.forJsonPut().toString());
    getReactNativeHost()
        .getReactInstanceManager()
        .getCurrentReactContext()
        .getJSModule(DeviceEventManagerModule.RCTDeviceEventEmitter.class)
        .emit("inAppMessageReceived", parameters);
    // Note: return InAppMessageOperation.DISCARD if you would like
    // to prevent the Braze SDK from displaying the message natively.
    return InAppMessageOperation.DISPLAY_NOW;
}
```
{% endsubtab %}
{% subtab iOS %}
### デフォルトのUIデリゲートをオーバーライドする {#overriding-the-default-ui-delegate}

デフォルトでは、`braze` インスタンスを初期化すると、[`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/)が作成されて割り当てられます。`BrazeInAppMessageUI`は[`BrazeInAppMessagePresenter`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter)プロトコルの実装であり、受信したアプリ内メッセージの処理をカスタマイズするために使用できる `delegate` プロパティが付属しています。

1. [こちらのiOSの記事](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui)で説明されているように、`BrazeInAppMessageUIDelegate` デリゲートを実装します。

2. `inAppMessage(_:displayChoiceForMessage:)` デリゲートメソッドでは、`inAppMessage` データにアクセスしてJavaScriptレイヤーに送信し、戻り値に基づいてネイティブメッセージを表示するかどうかを決定できます。

これらの値の詳細については、[iOSのドキュメント](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/)を参照してください。

```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui
                            displayChoiceForMessage:(BRZInAppMessageRaw *)message {
  // Convert the message to a JavaScript representation.
  NSData *inAppMessageData = [message json];
  NSString *inAppMessageString = [[NSString alloc] initWithData:inAppMessageData encoding:NSUTF8StringEncoding];
  NSDictionary *arguments = @{
    @"inAppMessage" : inAppMessageString
  };

  // Send to JavaScript.
  [self sendEventWithName:@"inAppMessageReceived" body:arguments];

  // Note: Return `BRZInAppMessageUIDisplayChoiceDiscard` if you would like
  // to prevent the Braze SDK from displaying the message natively.
  return BRZInAppMessageUIDisplayChoiceNow;
}
```

このデリゲートを使用するには、`braze` インスタンスを初期化した後に `brazeInAppMessagePresenter.delegate` に割り当てます。

{% alert note %}
`BrazeUI`はObjective-CまたはSwiftでのみインポートできます。Objective-C++を使用している場合は、これを別のファイルで処理する必要があります。
{% endalert %}

```objc
@import BrazeUI;

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  ((BrazeInAppMessageUI *)braze.inAppMessagePresenter).delegate = [[CustomDelegate alloc] init];
  AppDelegate.braze = braze;
}
```

### デフォルトのネイティブUIをオーバーライドする {#overriding-the-default-native-ui}

ネイティブiOSレイヤーでアプリ内メッセージの表示を完全にカスタマイズしたい場合は、[`BrazeInAppMessagePresenter`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter)プロトコルに準拠し、以下のサンプルに従ってカスタムプレゼンターを割り当てます。

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
Braze *braze = [BrazeReactBridge initBraze:configuration];
braze.inAppMessagePresenter = [[MyCustomPresenter alloc] init];
AppDelegate.braze = braze;
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}