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

アプリ内メッセージは、SDKが以下のカスタムイベントタイプのいずれかをログに記録したときにトリガーされます: `Session Start`、`Push Click`、`Any Purchase`、`Specific Purchase`、`Custom Event`（最後の2つは堅牢なプロパティフィルターを含みます）。

ユーザーのセッション開始時に、Brazeは対象となるすべてのアプリ内メッセージをユーザーのデバイスに配信し、同時にアセットをプリフェッチして表示レイテンシーを最小化します。トリガーイベントに複数の適格なアプリ内メッセージがある場合、最も優先度の高いメッセージのみが配信されます。詳しくは[セッションライフサイクル]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/#about-the-session-lifecycle)を参照してください。

{% alert note %}
アプリ内メッセージは、APIまたはAPIイベントによってトリガーすることはできません。SDKによってログに記録されるカスタムイベントによってのみトリガーされます。ロギングの詳細については、[カスタムイベントのログ記録]({{site.baseurl}}/developer_guide/analytics/logging_events/)を参照してください。
{% endalert %}

## アプリ内メッセージのタイプ {#types-of-in-app-messages}

Brazeは、セッション開始時にユーザーのデバイスに以下のタイプのアプリ内メッセージを送信します: `inapp`と`templated_iam`。ダッシュボードユーザーとしては異なるタイプを目にすることはありませんが、Brazeはセットアップとコンテンツに応じてそれらを異なる方法で処理します。

### `inapp`（標準） {#inapp-standard}

`inapp`（または「[標準]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/#standard-message-types)」）アプリ内メッセージは、Brazeがすでに把握しているカスタム属性などの必要な情報がすでにテンプレート化されています。一般的に、アプリ内メッセージがデバイスにダウンロードされると、デバイスがオフラインまたは機内モードであっても、トリガーイベントによってSDKが`inapp`アプリ内メッセージを表示します。

### `templated_iam`（テンプレート化） {#templatediam-templated}

`templated_iam`（または「テンプレート化」）アプリ内メッセージは、まだ必要な情報がテンプレート化されていません。メッセージが表示される前に、Brazeは情報を取得するために別のリクエストを行う必要があります。

{% multi_lang_include in-app_messages/templated_iams.md %}

## キーと値のペア {#key-value-pairs}

Brazeでキャンペーンを作成する際、キーと値のペアを`extras`として設定できます。アプリ内メッセージングオブジェクトはこれを使用してアプリにデータを送信できます。

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
`````````java
Map<String, String> getExtras()
```
{% endsubtab %}
{% subtab KOTLIN %}
`````````kotlin
extras: Map<String, String>
```
{% endsubtab %}
{% endsubtabs %}

{% alert tip %}
詳細については、[KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html#1498425856%2FProperties%2F-1725759721)を参照してください。
{% endalert %}
{% endtab %}

{% tab swift %}
次の例では、カスタムロジックを使用して、`extras`のキーと値のペアに基づいてアプリ内メッセージの表示を設定します。完全なカスタマイズ例については、[サンプルアプリ](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples)を参照してください。

{% subtabs %}
{% subtab swift %}

`````````swift
let customization = message.extras["custom-display"] as? String
if customization == "colorful-slideup" {
  // Perform your custom logic.
}
```
{% endsubtab %}
{% subtab OBJECTIVE-C %}

`````````objc
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

## 自動トリガーを無効にする {#disabling-automatic-triggers}

デフォルトでは、アプリ内メッセージは自動的にトリガーされます。これを無効にするには:

{% tabs %}

{% tab web %}
読み込みスニペット内の`braze.automaticallyShowInAppMessages()`への呼び出しを削除し、アプリ内メッセージの表示/非表示を処理するカスタムロジックを作成します。

`````````javascript
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
`braze.automaticallyShowInAppMessages()`を削除せずに`braze.showInAppMessage`を呼び出すと、メッセージが2回表示される場合があります。
{% endalert %}

メッセージのタイミングをより高度にコントロールする方法（トリガーメッセージの遅延や復元を含む）については、[チュートリアル: トリガーメッセージの遅延と復元]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages/)を参照してください。
{% endtab %}

{% tab android %}
1. カスタムリスナーを設定するために[`IInAppMessageManagerListener`](https://www.braze.com/docs/developer_guide/in_app_messages/customization/?sdktab=android&tab=global%20listener#android_step-1-implement-the-custom-manager-listener)を実装します。
2. [`beforeInAppMessageDisplayed()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-displayed.html)メソッドを更新して、[`InAppMessageOperation.DISCARD`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/-d-i-s-c-a-r-d/index.html)を返すようにします。

メッセージのタイミングをより高度にコントロールするには（後から表示や再キューイングを含む）、[メッセージのカスタマイズ](https://www.braze.com/docs/developer_guide/in_app_messages/customization/?tab=global%20listener&subtab=kotlin#android_step-2-instruct-braze-to-use-the-custom-manager-listener)ページを参照してください。
{% endtab %}

{% tab swift %}
1. アプリに`BrazeInAppMessageUIDelegate`デリゲートを実装します。完全な手順については、[チュートリアル: アプリ内メッセージUI](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui)を参照してください。
2. `inAppMessage(_:displayChoiceForMessage:)`デリゲートメソッドを更新して`.discard`を返すようにします。

メッセージのタイミングをより高度にコントロールする方法（トリガーメッセージの遅延や復元を含む）については、[チュートリアル: トリガーメッセージの遅延と復元]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages/)を参照してください。
{% endtab %}

{% tab flutter %}
1. 自動統合初期化機能を使用していることを確認してください。この機能は、バージョン`2.2.0`以降でデフォルトで有効になっています。
2. 次の行を`braze.xml`ファイルに追加することで、アプリ内メッセージ操作のデフォルトを`DISCARD`に設定します。
    ```xml
    <string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
    ```
{% endtab %}

{% tab unity %}
{% subtabs %}
{% subtab Android %}
Androidの場合、Braze設定エディターで**Automatically Display In-App Messages**の選択を解除します。または、Unityプロジェクトの`braze.xml`で`com_braze_inapp_show_inapp_messages_automatically`を`false`に設定できます。

アプリ内メッセージの初期表示動作は、Braze設定の「In App Message Manager Initial Display Operation」で設定できます。
{% endsubtab %}

{% subtab iOS %}
iOSの場合、Braze設定エディターでゲームオブジェクトリスナーを設定し、**Braze Displays In-App Messages**が選択されていないことを確認します。

アプリ内メッセージの初期表示動作は、Braze設定の「In App Message Manager Initial Display Operation」で設定できます。
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 1つのセッションで2つのアプリ内メッセージを連鎖させる {#chaining-two-in-app-messages-in-one-session}

セッション開始時にアプリ内メッセージをトリガーし、最初のメッセージでボタンが押された後に2番目のアプリ内メッセージをトリガーできます。これを行うには、2番目のメッセージをトリガーするボタンクリックのカスタムイベントをログに記録します。2番目のメッセージのトリガーはすでにデバイス上にある必要があり（ユーザーはすでに2番目のメッセージの対象である必要があります）、デバイス側で発生する必要があります（Braze SDKはBrazeサーバーで発生するカスタム属性の変更を取得しません）。複数のアプリ内メッセージを素早く連続して表示するには、アプリ内メッセージトリガー間のデフォルトの30秒クールダウンを変更する必要があります。プラットフォーム固有の設定については、[デフォルトのレート制限をオーバーライドする](#overriding-the-default-rate-limit)を参照してください。

## デフォルトのレート制限をオーバーライドする {#overriding-the-default-rate-limit}

デフォルトでは、SDKはトリガーされたアプリ内メッセージを30秒に1回にレート制限しています。これをオーバーライドするには、Brazeインスタンスが初期化される前に、以下のプロパティを設定ファイルに追加します。この値は、新しいレート制限（秒単位）として使用されます。

本番アプリでは、ユーザーが連続するアプリ内メッセージに圧倒されないよう、この値を10秒未満に設定しないでください。テストやサンプルアプリのフローでは、5秒が一般的な設定です。

テスト用にこの間隔を`0`に設定できます。ただし、`0`秒の間隔は複数のアプリ内メッセージを同時に表示させるものではありません。1つのアプリ内メッセージがすでに表示されている場合、現在のメッセージが閉じられるまで、別のトリガーされたメッセージは表示されません。

{% tabs %}
{% tab web %}
`````````javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```
{% endtab %}

{% tab android %}
`````````xml
<integer name="com_braze_trigger_action_minimum_time_interval_seconds">5</integer>
```
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
`````````swift
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
`````````objc
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

## 手動でメッセージをトリガーする {#manually-triggering-messages}

デフォルトでは、アプリ内メッセージはSDKがカスタムイベントを記録したときに自動的にトリガーされます。しかし、これに加えて、以下の方法を使って手動でメッセージをトリガーすることもできます。

### サーバー側のイベントを使用する {#using-a-server-side-event}

{% tabs %}
{% tab web %}
現時点では、Web Braze SDKはサーバー側のイベントを使用して手動でメッセージをトリガーすることをサポートしていません。
{% endtab %}

{% tab android %}
サーバー送信イベントを使用してアプリ内メッセージをトリガーするには、サイレントプッシュ通知をデバイスに送信し、カスタムプッシュコールバックがSDKベースのイベントをログに記録できるようにします。このイベントは、その後ユーザー向けのアプリ内メッセージをトリガーします。

#### ステップ1: サイレントプッシュを受信するプッシュコールバックを作成する {#step-1-create-a-push-callback-to-receive-the-silent-push}

特定のサイレントプッシュ通知をリッスンするには、カスタムプッシュコールバックを登録します。詳細については、[プッシュ通知の設定]({{site.baseurl}}/developer_guide/push_notifications/#android_setting-up-push-notifications)を参照してください。

アプリ内メッセージが配信されるために2つのイベントが記録されます。1つはサーバーによって記録され、もう1つはカスタムプッシュコールバック内から記録されます。同じイベントが重複しないようにするには、プッシュコールバック内からログに記録されるイベントは、サーバー送信イベントと同じ名前ではなく、「アプリ内メッセージトリガーイベント」などの一般的な命名規則に従う必要があります。そうしないと、単一のユーザーアクションについてログに記録される重複イベントによって、セグメンテーションとユーザーデータが影響を受ける可能性があります。

{% subtabs %}
{% subtab JAVA %}

`````````java
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

`````````kotlin
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

#### ステップ2: プッシュキャンペーンを作成する {#step-2-create-a-push-campaign}

サーバー送信イベントを介してトリガーされる[サイレントプッシュキャンペーン]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android)を作成します。

![]({% image_buster /assets/img_archive/serverSentPush.png %})

プッシュキャンペーンにはキーと値のペアエクストラを含める必要があります。これは、このプッシュキャンペーンがSDKカスタムイベントを記録するために送信されることを示します。このイベントはアプリ内メッセージをトリガーするために使用されます。

![2組のキーと値のペア: IS_SERVER_EVENTが「true」に設定され、CAMPAIGN_NAMEが「example campaign name」に設定されている。]({% image_buster /assets/img_archive/kvpConfiguration.png %}){: style="max-width:70%;" }

前出のプッシュコールバックサンプルコードは、キーと値のペアを認識して、適切なSDKカスタムイベントをログに記録します。

「アプリ内メッセージトリガー」イベントに添付するイベントプロパティを含めるには、プッシュペイロードのキーと値のペアでプロパティを渡します。この例では、後続のアプリ内メッセージのキャンペーン名が含められています。カスタムプッシュコールバックは、カスタムイベントをログに記録するときに、イベントプロパティのパラメーターとして値を渡すことができます。

#### ステップ3: アプリ内メッセージキャンペーンを作成する {#step-3-create-an-in-app-message-campaign}

Brazeダッシュボードで、ユーザーに表示されるアプリ内メッセージキャンペーンを作成します。このキャンペーンにはアクションベースの配信が必要であり、カスタムプッシュコールバック内から記録されたカスタムイベントからトリガーされる必要があります。

以下の例では、イベントプロパティを最初のサイレントプッシュの一部として送信することで、トリガーされる特定のアプリ内メッセージが設定されています。

![アクションベースの配信キャンペーンで、「campaign_name」が「IAM campaign name example」と等しい場合にアプリ内メッセージがトリガーされる。]({% image_buster /assets/img_archive/iam_event_trigger.png %})

アプリがフォアグラウンドにないときにサーバー送信イベントがログに記録されると、イベントはログに記録されますが、アプリ内メッセージは表示されません。アプリケーションがフォアグラウンドになるまでイベントを遅延させたい場合は、カスタムプッシュレシーバーにチェックを含めて、アプリがフォアグラウンドになるまでイベントを無視または遅延させる必要があります。
{% endtab %}

{% tab swift %}
#### ステップ1: サイレントプッシュとキーと値のペアを処理する {#step-1-handle-silent-push-and-key-value-pairs}

次の関数を実装し、[`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`メソッド](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application/)内で呼び出します。

{% subtabs %}
{% subtab swift %}

`````````swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  print("A push was received")
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    AppDelegate.braze?.logCustomEvent("IAM Trigger", properties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

`````````objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [AppDelegate.braze logCustomEvent:@"IAM Trigger" properties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
};
```

{% endsubtab %}
{% endsubtabs %}

サイレントプッシュを受信すると、ユーザープロファイルに対してSDKが記録したイベント「アプリ内メッセージトリガー」がログに記録されます。

{% alert important %}
SDKのログに記録されたカスタムイベントの記録にプッシュメッセージが使用されているため、Brazeはこのソリューションを有効にするために、ユーザーごとにプッシュトークンを格納する必要があります。iOSユーザーの場合、BrazeではユーザーがOSのプッシュプロンプトを受け取った時点からのトークンのみが保存されます。これ以前では、ユーザーはプッシュを使用して到達できず、先行ソリューションも実行できません。
{% endalert %}

#### ステップ2: サイレントプッシュキャンペーンを作成する {#step-2-create-a-silent-push-campaign}

サーバー送信イベントを介してトリガーされる[サイレントプッシュキャンペーン]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift)を作成します。

![カスタムイベント「server_event」をユーザープロファイルに持つユーザーに配信される、アクションベースのアプリ内メッセージキャンペーン。]({% image_buster /assets/img_archive/iosServerSentPush.png %})

プッシュキャンペーンにはキーと値のペアエクストラを含める必要があります。これは、このプッシュキャンペーンがSDKカスタムイベントを記録するために送信されることを示します。このイベントはアプリ内メッセージをトリガーするために使用されます。

![アクションベースの配信アプリ内メッセージキャンペーンには、2つのキーと値のペアがある。「CAMPAIGN_NAME」が「In-app message name example」に設定され、「IS_SERVER_EVENT」が「true」に設定されている。]({% image_buster /assets/img_archive/iOSServerPush.png %})

`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`メソッド内のコードはキー`IS_SERVER_EVENT`をチェックし、存在する場合はSDKカスタムイベントをログに記録します。

プッシュペイロードのキーと値のペアエクストラ内で目的の値を送信することで、イベント名またはイベントプロパティのいずれかを変更できます。カスタムイベントを記録する場合、これらのエクストラはイベント名のパラメータまたはイベントプロパティとして使用できます。

#### ステップ3: アプリ内メッセージキャンペーンを作成する {#step-3-create-an-in-app-message-campaign}

Brazeダッシュボードで、ユーザーに表示されるアプリ内メッセージキャンペーンを作成します。このキャンペーンにはアクションベースの配信があり、`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`メソッド内から記録されたカスタムイベントからトリガーされる必要があります。

以下の例では、イベントプロパティを最初のサイレントプッシュの一部として送信することで、トリガーされる特定のアプリ内メッセージが設定されています。

![カスタムイベント「In-app message trigger」を実行したユーザーに配信される、アクションベースのアプリ内メッセージキャンペーン。「campaign_name」が「IAM キャンペーン Name Example」と等しい。]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

{% alert note %}
これらのアプリ内メッセージは、アプリケーションがフォアグラウンドにある間にサイレントプッシュが受信された場合にのみトリガーされます。
{% endalert %}
{% endtab %}
{% endtabs %}

### 事前定義されたメッセージを表示する {#displaying-a-pre-defined-message}

事前定義したアプリ内メッセージを手動で表示するには、以下の方法を使用します。

{% tabs %}
{% tab web %}
Web SDKでは、`braze.showInAppMessage(inAppMessage)`を使用してアプリ内メッセージを表示します。詳細と例については、[リアルタイムでメッセージを表示する](#displaying-a-message-in-real-time)を参照してください。
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab JAVA %}

`````````java
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage);
```

{% endsubtab %}
{% subtab KOTLIN %}

`````````kotlin
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
`````````swift
if let inAppMessage = AppDelegate.braze?.inAppMessagePresenter?.nextAvailableMessage() {
  AppDelegate.braze?.inAppMessagePresenter?.present(message: inAppMessage)
}
```
{% endtab %}
{% endtabs %}

### リアルタイムでメッセージを表示する {#displaying-a-message-in-real-time}

ダッシュボードで利用できるのと同じカスタマイズオプションを使って、ローカルのアプリ内メッセージをリアルタイムで作成・表示することもできます。そのためには:

{% tabs %}
{% tab web %}
`````````javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab JAVA %}

`````````java
// Initializes a new slideup type in-app message and specifies its message.
InAppMessageSlideup inAppMessage = new InAppMessageSlideup();
inAppMessage.setMessage("Welcome to Braze! This is a slideup in-app message.");
```

{% endsubtab %}
{% subtab KOTLIN %}

`````````kotlin
// Initializes a new slideup type in-app message and specifies its message.
val inAppMessage = InAppMessageSlideup()
inAppMessage.message = "Welcome to Braze! This is a slideup in-app message."
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
ソフトキーボードが画面に表示されているときは、レンダリングが定義されていないため、アプリ内メッセージを表示しないでください。
{% endalert %}
{% endtab %}

{% tab swift %}
`inAppMessagePresenter`で[`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:))メソッドを手動で呼び出します。以下に例を示します。

{% subtabs %}
{% subtab swift %}

`````````swift
let customInAppMessage = Braze.InAppMessage.slideup(
  .init(message: "YOUR_CUSTOM_SLIDEUP_MESSAGE", slideFrom: .bottom, themes: .defaults)
)
AppDelegate.braze?.inAppMessagePresenter?.present(message: customInAppMessage)
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

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

{% endsubtab %}
{% endsubtabs %}

{% alert note %}
独自のアプリ内メッセージを作成する場合、分析トラッキングをオプトアウトし、`message.context`を使用してクリックとインプレッションのロギングを手動で処理する必要があります。
{% endalert %}
{% endtab %}

{% tab unity %}
スタックの次のメッセージを表示するには、`DisplayNextInAppMessage()`メソッドを使用します。`DISPLAY_LATER`または`BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER`がアプリ内メッセージ表示アクションとして選択されている場合、メッセージはこのスタックに保存されます。

`````````csharp
Appboy.AppboyBinding.DisplayNextInAppMessage();
```
{% endtab %}
{% endtabs %}

## アプリ内メッセージの遅延の原因 {#causes-of-in-app-message-delays}

セッション開始後数秒でアプリ内メッセージキャンペーンを受信した場合、遅延は以下の原因で発生した可能性があります:

- キャンペーントリガーの遅延
- カスタマイズ
- トリガーイベントの記録が予想より遅かった場合（`templated_iam`の場合など）

## Web用Exit-intentメッセージ {#exit-intent-messages-for-web}

Exit-intentメッセージは、訪問者がWebサイトを離れる前に重要な情報を伝えるために使用される、中断のないアプリ内メッセージです。

Web SDKでこれらのメッセージタイプのトリガーを設定するには、Webサイトにexit-intentライブラリ（[ouibounceのオープンソースライブラリ](https://github.com/carlsednaoui/ouibounce)など）を実装し、次のコードを使ってBrazeのカスタムイベントとして`'exit intent'`をログに記録します。これで、今後のアプリ内メッセージキャンペーンでは、このメッセージタイプをカスタムイベントトリガーとして使用できます。

`````````javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```
