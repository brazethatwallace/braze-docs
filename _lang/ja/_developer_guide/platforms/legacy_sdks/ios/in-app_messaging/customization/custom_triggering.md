---
nav_title: カスタムトリガー
article_title: iOS向けアプリ内メッセージのトリガー設定をカスタマイズする
platform: iOS
page_order: 7
description: "この参考記事では、iOS アプリケーションのアプリ内メッセージングのカスタムトリガーについて説明します。"
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# カスタムアプリ内メッセージトリガー {#custom-in-app-message-triggering}

デフォルトでは、アプリ内メッセージはSDKによって記録されるイベントタイプによってトリガーされます。サーバー送信イベントによってアプリ内メッセージをトリガーしたい場合にも実現できます。

この機能を有効にするには、サイレントプッシュをデバイスに送信し、デバイスがSDKベースのイベントをログに記録できるようにします。このSDKイベントは、その後、ユーザー向けのアプリ内メッセージをトリガーします。

## ステップ 1:サイレントプッシュとキーと値のペアを処理する {#step-1-handle-silent-push-and-key-value-pairs}

`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` メソッド内に次のコードを追加します。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [[Appboy sharedInstance] logCustomEvent:@"IAM Trigger" withProperties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
 };
```

{% endtab %}
{% tab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  NSLog("A push was received");
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    Appboy.sharedInstance()?.logCustomEvent("IAM Trigger", withProperties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endtab %}
{% endtabs %}

サイレントプッシュを受信すると、ユーザープロファイルに対してSDKが記録したイベント「アプリ内メッセージトリガー」がログに記録されます。なお、これらのアプリ内メッセージは、アプリケーションがフォアグラウンドにある間にサイレントプッシュが受信された場合にのみトリガーされます。

## ステップ 2:プッシュキャンペーンを作成する {#step-2-create-a-push-campaign}

サーバー送信イベントを介してトリガーされるサイレントプッシュキャンペーンを作成します。サイレントプッシュキャンペーンの作成の詳細については、[サイレントプッシュ通知]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/silent_push_notifications)を参照してください。

![カスタムイベント「server_event」を実行したユーザーに配信される、アクションベースの配信アプリ内メッセージキャンペーン。]({% image_buster /assets/img_archive/iosServerSentPush.png %})

プッシュキャンペーンにはキーと値のペアのエクストラを含める必要があります。これは、このプッシュキャンペーンがSDKカスタムイベントを記録するために送信されることを示します。このイベントはアプリ内メッセージをトリガーするために使用されます。

![2つのキーと値のペアを持つアクションベースの配信アプリ内メッセージキャンペーン。「CAMPAIGN_NAME」は「In-app message name example」に設定され、「IS_SERVER_EVENT」は「true」に設定されています。]({% image_buster /assets/img_archive/iOSServerPush.png %})

`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` メソッド内のコードはキー `IS_SERVER_EVENT` をチェックし、存在する場合はSDKカスタムイベントをログに記録します。

プッシュペイロードのキーと値のペアのエクストラ内で目的の値を送信することで、イベント名またはイベントプロパティのいずれかを変更できます。カスタムイベントを記録する場合、これらのエクストラはイベント名のパラメータまたはイベントプロパティとして使用できます。

## ステップ 3:アプリ内メッセージキャンペーンを作成する {#step-3-create-an-in-app-message-campaign}

Brazeダッシュボード内から、ユーザーに表示されるアプリ内メッセージキャンペーンを作成します。このキャンペーンにはアクションベースの配信を設定し、`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` メソッド内から記録されたカスタムイベントからトリガーされるようにする必要があります。

以下の例では、イベントプロパティを最初のサイレントプッシュの一部として送信することで、トリガーされる特定のアプリ内メッセージが設定されています。

![カスタムイベント「In-app message trigger」を実行したユーザーに配信される、アクションベースの配信アプリ内メッセージキャンペーン。ここで「campaign_name」は「In-app message name example」に等しい。]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

SDKが記録したカスタムイベントの記録にプッシュメッセージが使用されているため、Brazeはこのソリューションを有効にするために、ユーザーごとにプッシュトークンを保存する必要があります。iOSとAndroidの両方で、BrazeはユーザーがOSのプッシュプロンプトを受け取った時点からのトークンのみを保存します。これ以前では、ユーザーはプッシュを使用して到達できず、上記のソリューションも実行できません。