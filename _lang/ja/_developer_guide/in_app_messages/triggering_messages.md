---
nav_title: トリガーメッセージ
article_title: Braze SDKを通じてアプリ内メッセージをトリガーする
page_order: 0.2
description: "Braze SDKを通じてアプリ内メッセージをトリガーする方法について、1つのセッションでメッセージを連鎖させる方法やデフォルトのレート制限をオーバーライドする方法を含めて説明します。"
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# アプリ内メッセージをトリガーする {#trigger-in-app-messages}

> Braze SDKを通じてアプリ内メッセージをトリガーする方法を説明します。

## メッセージのトリガーと配信 {#message-triggers-and-delivery}

アプリ内メッセージは、SDKが次のカスタムイベントタイプのいずれかを記録したときにトリガーされます: `Session Start`、`Push Click`、`Any Purchase`、`Specific Purchase`、および`Custom Event`（最後の2つには堅牢なプロパティフィルターが含まれます）。

ユーザーのセッション開始時に、Brazeは対象となるすべてのアプリ内メッセージをデバイスに配信し、同時にアセットをプリフェッチして表示の遅延を最小限に抑えます。トリガーイベントに対象となるアプリ内メッセージが複数ある場合、最も優先度の高いメッセージのみが配信されます。詳細については、[セッションライフサイクル]({{site.baseurl}}/developer_guide/analytics/tracking_sessions)を参照してください。

{% alert note %}
アプリ内メッセージは、APIやAPIイベントによってトリガーすることはできません&#8212;SDKによって記録されたカスタムイベントのみで可能です。ログ記録の詳細については、[カスタムイベントのログ記録]({{site.baseurl}}/developer_guide/analytics/logging_events)を参照してください。
{% endalert %}

## アプリ内メッセージの種類 {#types-of-in-app-messages}

Brazeは、セッション開始時にユーザーのデバイスに次の種類のアプリ内メッセージを送信します：`inapp`と`templated_iam`です。ダッシュボードユーザーとしてはこれらの種類の違いを目にすることはありませんが、Brazeは設定やコンテンツに応じてそれぞれ異なる方法で処理します。

### `inapp`（標準） {#inapp-standard}

`inapp`（または「[標準]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages#standard-message-types)」）アプリ内メッセージは、Brazeがすでに把握しているカスタム属性など、必要な情報がすでにテンプレート化されています。一般的に、アプリ内メッセージがデバイスにダウンロードされると、デバイスがオフラインや機内モードであっても、トリガーイベントによってSDKが`inapp`アプリ内メッセージを表示します。

### `templated_iam`（テンプレート化） {#templated_iam-templated}

`templated_iam`（または「テンプレート化」）アプリ内メッセージは、必要な情報がまだテンプレート化されていません。メッセージを表示する前に、Brazeが情報を取得するために別のリクエストを行う必要があります。

アプリ内メッセージは、**表示前にキャンペーンの適格性を再評価する**が選択されている場合、またはメッセージに以下のいずれかのLiquidタグが含まれている場合に、テンプレート化アプリ内メッセージとして配信されます：

- `canvas_entry_properties`
- `connected_content`
- {% raw %}`{sms.${*}}`{% endraw %}などのSMS変数
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

これは、セッション開始時にデバイスがメッセージ全体ではなく、そのアプリ内メッセージのトリガーを受信することを意味します。ユーザーがアプリ内メッセージをトリガーすると、ユーザーのデバイスが実際のメッセージを取得するためにネットワークリクエストを行います。

{% alert note %}
デバイスがインターネットにアクセスできない場合、メッセージは配信されません。Liquidロジックの解決に時間がかかりすぎる場合も、メッセージが配信されないことがあります。
{% endalert %}

## キーと値のペア {#key-value-pairs}

Brazeでキャンペーンを作成する際、`extras` としてキーと値のペアを設定できます。アプリ内メッセージオブジェクトはこれを使用してアプリにデータを送信できます。

{% tabs %}
{% tab web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  if (inAppMessage instanceof braze.ControlMessage) {
    return braze.showInAppMessage(inAppMessage);
  }


  if (inAppMessage instanceof braze.InAppMessage) {
    const extras = inAppMessage.extras;
    if (extras) {
      for (const key in extras) {
        console.log("key: " + key + ", value: " + extras[key]);
      }
    }
  }
  braze.showInAppMessage(inAppMessage);
});
```
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab JAVA %}
```java
Map<String, String> getExtras()
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
extras: Map<String, String>
```
{% endsubtab %}
{% endsubtabs %}

{% alert tip %}
詳細については、[KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html#1498425856%2FProperties%2F-1725759721)を参照してください。
{% endalert %}
{% endtab %}

{% tab swift %}
以下の例では、`extras` のキーと値のペアに基づいてアプリ内メッセージの表示を設定するカスタムロジックを使用しています。完全なカスタマイズの例については、[サンプルアプリ](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples)をご確認ください。

{% subtabs %}
{% subtab swift %}

```swift
let customization = message.extras["custom-display"] as? String
if customization == "colorful-slideup" {
  // Perform your custom logic.
}
```
{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
if ([message.extras[@"custom-display"] isKindOfClass:[NSString class]]) {
  NSString *customization = message.extras[@"custom-display"];
  if ([customization isEqualToString:@"colorful-slideup"]) {
    // Perform your custom logic.
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 自動トリガーの無効化 {#disabling-automatic-triggers}

デフォルトでは、アプリ内メッセージは自動的にトリガーされます。これを無効にするには、以下の手順に従ってください。

{% tabs %}

{% tab web %}
読み込みスニペットから `braze.automaticallyShowInAppMessages()` の呼び出しを削除し、アプリ内メッセージの表示・非表示を処理するカスタムロジックを作成します。

```javascript
braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message

  if (inAppMessage.isControl) { // v4.5.0+, otherwise use  `inAppMessage instanceof braze.ControlMessage`
     return braze.showInAppMessage(inAppMessage);
  }

  // Display the in-app message. You could defer display here by pushing this message to code within your own application.
  // If you don't want to use the display capabilities in Braze, you could alternatively pass the in-app message to your own display code here.

  if ( should_show_the_message_according_to_your_custom_logic ) {
      braze.showInAppMessage(inAppMessage);
  } else {
      // do nothing
  }
});
```

{% alert important %}
`braze.automaticallyShowInAppMessages()` を削除せずに `braze.showInAppMessage` を呼び出すと、メッセージが二重に表示される場合があります。
{% endalert %}

メッセージのタイミングに関するより高度なコントロール（トリガーメッセージの遅延や復元など）については、[チュートリアル:トリガーメッセージの遅延と復元]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages)を参照してください。
{% endtab %}

{% tab android %}
1. [`IInAppMessageManagerListener`]({{site.baseurl}}/developer_guide/in_app_messages/customization?sdktab=android&tab=global%20listener#android_step-1-implement-the-custom-manager-listener)を実装してカスタムリスナーを設定します。
2. [`beforeInAppMessageDisplayed()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-displayed.html)メソッドを更新して[`InAppMessageOperation.DISCARD`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/-d-i-s-c-a-r-d/index.html)を返すようにします。

メッセージのタイミングに関するより高度なコントロール（後から表示する、再キューに入れるなど）については、[メッセージのカスタマイズ]({{site.baseurl}}/developer_guide/in_app_messages/customization?tab=global%20listener&subtab=kotlin#android_step-2-instruct-braze-to-use-the-custom-manager-listener)ページを参照してください。
{% endtab %}

{% tab swift %}
1. アプリに `BrazeInAppMessageUIDelegate` デリゲートを実装します。詳しい手順については、[チュートリアル:アプリ内メッセージUI](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui)を参照してください。
2. `inAppMessage(_:displayChoiceForMessage:)` デリゲートメソッドを更新して `.discard` を返すようにします。

メッセージのタイミングに関するより高度なコントロール（トリガーメッセージの遅延や復元など）については、[チュートリアル:トリガーメッセージの遅延と復元]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages)を参照してください。
{% endtab %}

{% tab flutter %}
1. デフォルトでバージョン `2.2.0` 以降で有効になっている自動統合イニシャライザーを使用していることを確認します。
2. `braze.xml` ファイルに以下の行を追加して、アプリ内メッセージ操作のデフォルトを `DISCARD` に設定します。
    ```xml
    <string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
    ```
{% endtab %}

{% tab unity %}
{% subtabs %}
{% subtab Android %}
Androidの場合、Braze設定エディターで**Automatically Display In-App Messages**の選択を解除します。または、Unityプロジェクトの `braze.xml` で `com_braze_inapp_show_inapp_messages_automatically` を `false` に設定することもできます。

アプリ内メッセージの初期表示操作は、Braze設定の「In App Message Manager Initial Display Operation」で設定できます。
{% endsubtab %}

{% subtab iOS %}
iOSの場合、Braze設定エディターでゲームオブジェクトリスナーを設定し、**Braze Displays In-App Messages**が選択されていないことを確認します。

アプリ内メッセージの初期表示操作は、Braze設定の「In App Message Manager Initial Display Operation」で設定できます。
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 1つのセッションで2つのアプリ内メッセージを連鎖させる {#chaining-two-in-app-messages-in-one-session}

セッション開始時にアプリ内メッセージをトリガーし、最初のメッセージのボタンが押された後に2つ目のアプリ内メッセージをトリガーできます。これを行うには、2つ目のメッセージをトリガーするボタンクリックのカスタムイベントを記録します。2つ目のメッセージのトリガーはすでにデバイス上に存在している必要があり（ユーザーはすでに2つ目のメッセージの対象である必要があります）、デバイス側で発生する必要があります（Braze SDKはBrazeサーバー上で発生したカスタム属性の変更を取得しません）。アプリ内メッセージを短い間隔で連続表示するには、アプリ内メッセージトリガー間のデフォルトの30秒クールダウンを変更する必要があります。プラットフォーム固有の設定については、[デフォルトのレート制限のオーバーライド](#overriding-the-default-rate-limit)を参照してください。

## デフォルトのレート制限のオーバーライド {#overriding-the-default-rate-limit}

デフォルトでは、SDKはトリガーされたアプリ内メッセージのレート制限を30秒に1回に設定しています。これをオーバーライドするには、Brazeインスタンスが初期化される前に、設定ファイルに以下のプロパティを追加します。この値は、新しいレート制限（秒単位）として使用されます。

本番アプリでは、ユーザーが連続するアプリ内メッセージに圧倒されないよう、この値を10秒未満に設定しないでください。テストやサンプルアプリのフローでは、5秒が一般的な設定です。

テスト用にこの間隔を`0`に設定できます。ただし、`0`秒の間隔を設定しても、複数のアプリ内メッセージが同時に表示されるわけではありません。1つのアプリ内メッセージがすでに表示されている場合、現在のメッセージが閉じられるまで、別のトリガーメッセージは表示されません。

{% tabs %}
{% tab web %}
```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```
{% endtab %}

{% tab android %}
```xml
<integer name="com_braze_trigger_action_minimum_time_interval_seconds">5</integer>
```
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
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
{% endsubtab %}
{% subtab OBJECTIVE-C %}
```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                    endpoint:@"<BRAZE_ENDPOINT>"];
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5;
Braze *braze = [BrazePlugin initBraze:configuration];
AppDelegate.braze = braze;
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## メッセージの手動トリガー {#manually-triggering-messages}

デフォルトでは、SDKがカスタムイベントを記録すると、アプリ内メッセージは自動的にトリガーされます。ただし、これに加えて、以下のメソッドを使用してメッセージを手動でトリガーすることもできます。

### サーバーサイドイベントの使用 {#using-a-server-side-event}

{% tabs %}
{% tab web %}
現時点では、Web Braze SDKはサーバーサイドイベントを使用したメッセージの手動トリガーをサポートしていません。
{% endtab %}

{% tab android %}
サーバー送信イベントを使用してアプリ内メッセージをトリガーするには、デバイスにサイレントプッシュ通知を送信し、カスタムプッシュコールバックでSDKベースのイベントを記録できるようにします。このイベントが、ユーザーに表示されるアプリ内メッセージをトリガーします。

#### ステップ1:サイレントプッシュを受信するプッシュコールバックを作成する {#step-1-create-a-push-callback-to-receive-the-silent-push}

特定のサイレントプッシュ通知をリッスンするカスタムプッシュコールバックを登録します。詳細については、[プッシュ通知の設定]({{site.baseurl}}/developer_guide/push_notifications#android_setting-up-push-notifications)を参照してください。

アプリ内メッセージを配信するために、2つのイベントが記録されます。1つはサーバーによるもの、もう1つはカスタムプッシュコールバック内からのものです。同じイベントが重複しないようにするため、プッシュコールバック内から記録されるイベントは、サーバー送信イベントと同じ名前ではなく、「アプリ内メッセージトリガーイベント」などの汎用的な命名規則に従う必要があります。これを行わないと、単一のユーザーアクションに対して重複イベントが記録され、セグメンテーションやユーザーデータに影響を与える可能性があります。

{% subtabs %}
{% subtab JAVA %}

```java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final Bundle kvps = event.getNotificationPayload().getBrazeExtras();
  if (kvps.containsKey("IS_SERVER_EVENT")) {
    BrazeProperties eventProperties = new BrazeProperties();

    // The campaign name is a string extra that clients can include in the push
    String campaignName = kvps.getString("CAMPAIGN_NAME");
    eventProperties.addProperty("campaign_name", campaignName);
    Braze.getInstance(context).logCustomEvent("IAM Trigger", eventProperties);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(applicationContext).subscribeToPushNotificationEvents { event ->
    val kvps = event.notificationPayload.brazeExtras
    if (kvps.containsKey("IS_SERVER_EVENT")) {
        val eventProperties = BrazeProperties()

        // The campaign name is a string extra that clients can include in the push
        val campaignName = kvps.getString("CAMPAIGN_NAME")
        eventProperties.addProperty("campaign_name", campaignName)
        Braze.getInstance(applicationContext).logCustomEvent("IAM Trigger", eventProperties)
    }
}
```

{% endsubtab %}
{% endsubtabs %}

#### ステップ2:プッシュキャンペーンを作成する {#step-2-create-a-push-campaign}

サーバー送信イベントによってトリガーされる[サイレントプッシュキャンペーン]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=android)を作成します。

![アクションベース配信で設定されたサイレントプッシュキャンペーンの配信ステップ。server_eventカスタムイベントトリガーが設定されています。]({% image_buster /assets/img_archive/serverSentPush.png %})

プッシュキャンペーンには、このプッシュキャンペーンがSDKカスタムイベントを記録するために送信されることを示すキーと値のペアのエクストラを含める必要があります。このイベントがアプリ内メッセージのトリガーに使用されます。

![2組のキーと値のペア：IS_SERVER_EVENTが「true」に設定され、CAMPAIGN_NAMEが「example campaign name」に設定されています。]({% image_buster /assets/img_archive/kvpConfiguration.png %}){: style="max-width:70%;" }

先ほどのプッシュコールバックのサンプルコードは、キーと値のペアを認識し、適切なSDKカスタムイベントを記録します。

「アプリ内メッセージトリガー」イベントにイベントプロパティを添付したい場合は、プッシュペイロードのキーと値のペアにそれらを渡すことで実現できます。この例では、後続のアプリ内メッセージのキャンペーン名が含まれています。カスタムプッシュコールバックは、カスタムイベントを記録する際に、イベントプロパティのパラメーターとしてその値を渡すことができます。

#### ステップ3:アプリ内メッセージキャンペーンを作成する {#step-3-create-an-in-app-message-campaign}

Brazeダッシュボードで、ユーザーに表示されるアプリ内メッセージキャンペーンを作成します。このキャンペーンはアクションベース配信を使用し、カスタムプッシュコールバック内から記録されたカスタムイベントによってトリガーされる必要があります。

以下の例では、最初のサイレントプッシュの一部としてイベントプロパティを送信することで、トリガーされる特定のアプリ内メッセージが設定されています。

![「campaign_name」が「IAM campaign name example」と等しい場合にアプリ内メッセージがトリガーされるアクションベース配信キャンペーン。]({% image_buster /assets/img_archive/iam_event_trigger.png %})

アプリがフォアグラウンドにない状態でサーバー送信イベントが記録された場合、イベントは記録されますが、アプリ内メッセージは表示されません。アプリケーションがフォアグラウンドになるまでイベントを遅延させたい場合は、カスタムプッシュレシーバーにチェックを含めて、アプリがフォアグラウンドに入るまでイベントを無視または遅延させる必要があります。
{% endtab %}

{% tab swift %}
#### ステップ1:サイレントプッシュとキーと値のペアを処理する {#step-1-handle-silent-push-and-key-value-pairs}

以下の関数を実装し、[`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`メソッド](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:didreceiveremotenotification:fetchcompletionhandler:))内で呼び出します。

{% subtabs %}
{% subtab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  print("A push was received")
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    AppDelegate.braze?.logCustomEvent("IAM Trigger", properties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [AppDelegate.braze logCustomEvent:@"IAM Trigger" properties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
};
```

{% endsubtab %}
{% endsubtabs %}

サイレントプッシュが受信されると、SDKが記録した「アプリ内メッセージトリガー」イベントがユーザープロファイルに対して記録されます。

{% alert important %}
プッシュメッセージを使用してSDK記録のカスタムイベントを記録するため、Brazeはこのソリューションを有効にするために各ユーザーのプッシュトークンを保存する必要があります。iOSユーザーの場合、BrazeはユーザーがOSのプッシュプロンプトを受け取った時点からのみトークンを保存します。それ以前は、ユーザーにプッシュで到達できないため、上記のソリューションは使用できません。
{% endalert %}

#### ステップ2:サイレントプッシュキャンペーンを作成する {#step-2-create-a-silent-push-campaign}

サーバー送信イベントによってトリガーされる[サイレントプッシュキャンペーン]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=swift)を作成します。

![カスタムイベント「server_event」を持つユーザープロファイルのユーザーに配信されるアクションベース配信のアプリ内メッセージキャンペーン。]({% image_buster /assets/img_archive/iosServerSentPush.png %})

プッシュキャンペーンには、このプッシュキャンペーンがSDKカスタムイベントを記録するために送信されることを示すキーと値のペアのエクストラを含める必要があります。このイベントがアプリ内メッセージのトリガーに使用されます。

![2つのキーと値のペアを持つアクションベース配信のアプリ内メッセージキャンペーン。「CAMPAIGN_NAME」が「In-app message name example」に設定され、「IS_SERVER_EVENT」が「true」に設定されています。]({% image_buster /assets/img_archive/iOSServerPush.png %})

`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`メソッド内のコードは、キー`IS_SERVER_EVENT`をチェックし、存在する場合はSDKカスタムイベントを記録します。

プッシュペイロードのキーと値のペアのエクストラ内に目的の値を送信することで、イベント名またはイベントプロパティを変更できます。カスタムイベントを記録する際、これらのエクストラをイベント名のパラメーターまたはイベントプロパティとして使用できます。

#### ステップ3:アプリ内メッセージキャンペーンを作成する

Brazeダッシュボードで、ユーザーに表示されるアプリ内メッセージキャンペーンを作成します。このキャンペーンはアクションベース配信を使用し、`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`メソッド内から記録されたカスタムイベントによってトリガーされる必要があります。

以下の例では、最初のサイレントプッシュの一部としてイベントプロパティを送信することで、トリガーされる特定のアプリ内メッセージが設定されています。

![カスタムイベント「In-app message trigger」を実行し、「campaign_name」が「IAM キャンペーン Name Example」と等しいユーザーに配信されるアクションベース配信のアプリ内メッセージキャンペーン。]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

{% alert note %}
これらのアプリ内メッセージは、アプリケーションがフォアグラウンドにある状態でサイレントプッシュが受信された場合にのみトリガーされます。
{% endalert %}
{% endtab %}
{% endtabs %}

### 事前定義されたメッセージの表示 {#displaying-a-pre-defined-message}

事前定義されたアプリ内メッセージを手動で表示するには、以下のメソッドを使用します。

{% tabs %}
{% tab web %}
Web SDKの場合、`braze.showInAppMessage(inAppMessage)`を使用して任意のアプリ内メッセージを表示します。詳細と例については、[リアルタイムでのメッセージ表示](#displaying-a-message-in-real-time)を参照してください。
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab JAVA %}

```java
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
```swift
if let inAppMessage = AppDelegate.braze?.inAppMessagePresenter?.nextAvailableMessage() {
  AppDelegate.braze?.inAppMessagePresenter?.present(message: inAppMessage)
}
```
{% endtab %}
{% endtabs %}

### リアルタイムでのメッセージ表示 {#displaying-a-message-in-real-time}

ダッシュボードで利用可能なものと同じカスタマイズオプションを使用して、ローカルのアプリ内メッセージをリアルタイムで作成・表示することもできます。これを行うには：

{% tabs %}
{% tab web %}
```javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab JAVA %}

```java
// Initializes a new slideup type in-app message and specifies its message.
InAppMessageSlideup inAppMessage = new InAppMessageSlideup();
inAppMessage.setMessage("Welcome to Braze! This is a slideup in-app message.");
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
// Initializes a new slideup type in-app message and specifies its message.
val inAppMessage = InAppMessageSlideup()
inAppMessage.message = "Welcome to Braze! This is a slideup in-app message."
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
ソフトキーボードが画面に表示されている間は、アプリ内メッセージを表示しないでください。この状況ではレンダリングが未定義となります。
{% endalert %}
{% endtab %}

{% tab swift %}
`inAppMessagePresenter`の[`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:))メソッドを手動で呼び出します。例：

{% subtabs %}
{% subtab swift %}

```swift
let customInAppMessage = Braze.InAppMessage.slideup(
  .init(message: "YOUR_CUSTOM_SLIDEUP_MESSAGE", slideFrom: .bottom, themes: .defaults)
)
AppDelegate.braze?.inAppMessagePresenter?.present(message: customInAppMessage)
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
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

{% endsubtab %}
{% endsubtabs %}

{% alert note %}
独自のアプリ内メッセージを作成すると、分析トラッキングからオプトアウトされるため、`message.context`を使用してクリックとインプレッションのログを手動で処理する必要があります。
{% endalert %}
{% endtab %}

{% tab unity %}
スタック内の次のメッセージを表示するには、`DisplayNextInAppMessage()`メソッドを使用します。アプリ内メッセージの表示アクションとして`DISPLAY_LATER`または`BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER`が選択された場合、メッセージはこのスタックに保存されます。

```csharp
Appboy.AppboyBinding.DisplayNextInAppMessage();
```
{% endtab %}
{% endtabs %}

## アプリ内メッセージの遅延の原因 {#causes-of-in-app-message-delays}

セッション開始から数秒後にアプリ内メッセージキャンペーンを受信した場合、その遅延は以下の原因で発生した可能性があります。

- キャンペーントリガーの遅延
- カスタマイズ
- トリガーイベントが予想よりも遅く記録された（`templated_iam` の場合など）

## Web向け離脱意図メッセージ {#exit-intent-messages-for-web}

離脱意図メッセージは、訪問者がWebサイトを離れる前に重要な情報を伝えるために使用される、非侵入型のアプリ内メッセージです。

Web SDKでこれらのメッセージタイプのトリガーを設定するには、Webサイトに離脱意図ライブラリ（[ouibounceのオープンソースライブラリ](https://github.com/carlsednaoui/ouibounce)など）を実装し、以下のコードを使用してBrazeで`'exit intent'`をカスタムイベントとして記録します。これにより、今後のアプリ内メッセージキャンペーンで、このメッセージタイプをカスタムイベントトリガーとして使用できます。

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```
