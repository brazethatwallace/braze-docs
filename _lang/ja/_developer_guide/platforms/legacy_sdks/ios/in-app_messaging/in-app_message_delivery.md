---
nav_title: アプリ内メッセージ配信
article_title: iOS 向けアプリ内メッセージ配信
platform: iOS
page_order: 3
description: "この参考記事では、iOSのアプリ内メッセージ配信について説明し、さまざまなトリガータイプ、配信セマンティクス、イベントトリガーステップについて説明します。"
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# アプリ内メッセージ配信 {#in-app-message-delivery}

## トリガーの種類 {#trigger-types}

アプリ内メッセージ製品では、`Any Purchase`、`Specific Purchase`、`Session Start`、`Custom Event`、`Push Click` など、いくつかの異なるイベントタイプの結果としてアプリ内メッセージの表示をトリガーできます。さらに、`Specific Purchase` と `Custom Event` のトリガーには、堅牢なプロパティフィルターが含まれています。

{% alert note %}
トリガーされたアプリ内メッセージは、Braze SDKを通じて記録されたカスタムイベントでのみ機能します。アプリ内メッセージは、APIやAPIイベント（購入イベントなど）によってトリガーすることはできません。iOSを使用している場合は、[カスタムイベントのトラッキング]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=swift)の記事で詳細をご覧ください。
{% endalert %}

## 配信セマンティクス {#delivery-semantics}

ユーザーが受信対象となるすべてのアプリ内メッセージは、セッション開始時にユーザーのデバイスに配信されます。1つのイベントによって2つのアプリ内メッセージがトリガーされた場合、優先度の高いアプリ内メッセージが表示されます。SDKのセッション開始セマンティクスの詳細については、[セッションライフサイクル]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/analytics/tracking_sessions#session-lifecycle)をお読みください。配信時に、SDKはアセットをプリフェッチして、トリガー時にすぐに利用できるようにし、表示の遅延を最小限に抑えます。

トリガーイベントに複数の対象となるアプリ内メッセージが関連付けられている場合、最も優先度の高いアプリ内メッセージのみが配信されます。

配信時にすぐ表示されるアプリ内メッセージ（セッション開始、プッシュクリック）では、アセットがプリフェッチされていないため、多少の遅延が発生する場合があります。

## トリガー間の最小時間間隔 {#minimum-time-interval-between-triggers}

デフォルトでは、質の高いユーザーエクスペリエンスを促進するために、アプリ内メッセージのレート制限は30秒に1回に設定されています。

この値は、`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` に渡される `appboyOptions` パラメーター内の `ABKMinimumTriggerTimeIntervalKey` を使用してオーバーライドできます。`ABKMinimumTriggerTimeIntervalKey` を、アプリ内メッセージ間の最小時間（秒単位）として設定したい整数値に設定してください。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Sets the minimum trigger time interval to 5 seconds
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKMinimumTriggerTimeIntervalKey : @(5) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:[ABKMinimumTriggerTimeIntervalKey : 5])
```

{% endtab %}
{% endtabs %}

## 一致するトリガーが見つからない場合 {#failing-to-find-a-matching-trigger}

Brazeが特定のイベントに対して一致するトリガーを見つけられなかった場合、[`ABKInAppMessageControllerDelegate`](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_in_app_message_controller_delegate-p.html)の[noMatchingTriggerForEvent:name:](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_in_app_message_controller_delegate-p.html#ab4d57b13c51545d487227945a37d4ab8)メソッドが呼び出されます。このシナリオを処理するには、デリゲートプロトコルを採用しているクラスにこのメソッドを実装してください。

## ローカルのアプリ内メッセージ配信 {#local-in-app-message-delivery}

### アプリ内メッセージスタック {#the-in-app-message-stack}

#### アプリ内メッセージの表示 {#showing-in-app-messages}

ユーザーがアプリ内メッセージを受信する資格がある場合、`ABKInAppMessageController`はアプリ内メッセージスタックから最新のアプリ内メッセージを取得します。スタックはメモリ内に保存されたアプリ内メッセージのみを保持し、アプリが中断モードから起動されるたびにクリアされます。

{% alert important %}
キーボードが画面に表示されているときにアプリ内メッセージを表示しないでください。この状況ではレンダリングが未定義となります。
{% endalert %}

#### アプリ内メッセージをスタックに追加する {#adding-in-app-messages-to-the-stack}

ユーザーは以下の状況でアプリ内メッセージを受信する資格があります。

- アプリ内メッセージのトリガーイベントが発火した場合
- セッション開始イベント
- プッシュ通知からアプリが開かれた場合

トリガーされたアプリ内メッセージは、トリガーイベントが発火したときにスタックに配置されます。複数のアプリ内メッセージがスタックにあり表示待ちの場合、Brazeは最も最近受信したアプリ内メッセージを最初に表示します（後入れ先出し）。

#### アプリ内メッセージをスタックに戻す {#returning-in-app-messages-to-the-stack}

トリガーされたアプリ内メッセージは、以下の状況でスタックに戻すことができます。

- アプリがバックグラウンドにあるときにアプリ内メッセージがトリガーされた場合。
- 別のアプリ内メッセージが現在表示されている場合。
- 非推奨の`beforeInAppMessageDisplayed:withKeyboardIsUp:`[UIデリゲートメソッド]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates#in-app-message-delegate)が実装されておらず、キーボードが現在表示されている場合。
- `beforeInAppMessageDisplayed:`[デリゲートメソッド]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates#core-in-app-message-delegate)または非推奨の`beforeInAppMessageDisplayed:withKeyboardIsUp:`[UIデリゲートメソッド]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates#in-app-message-delegate)が`ABKDisplayInAppMessageLater`を返した場合。

#### アプリ内メッセージの破棄 {#discarding-in-app-messages}

トリガーされたアプリ内メッセージは、以下の状況で破棄されます。

- `beforeInAppMessageDisplayed:`[デリゲートメソッド]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates#core-in-app-message-delegate)または非推奨の`beforeInAppMessageDisplayed:withKeyboardIsUp:`[UIデリゲートメソッド]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates#in-app-message-delegate)が`ABKDiscardInAppMessage`を返した場合。
- アプリ内メッセージのアセット（画像またはZIPファイル）のダウンロードに失敗した場合。
- アプリ内メッセージが表示準備完了であるが、タイムアウト時間を超過した場合。
- デバイスの向きがトリガーされたアプリ内メッセージの向きと一致しない場合。
- アプリ内メッセージがフルアプリ内メッセージであるが、画像がない場合。
- アプリ内メッセージが画像のみのモーダルアプリ内メッセージであるが、画像がない場合。

#### アプリ内メッセージ表示を手動でキューに入れる {#manually-queue-in-app-message-display}

アプリ内の他のタイミングでアプリ内メッセージを表示したい場合は、以下のメソッドを呼び出してスタックの最上位のアプリ内メッセージを手動で表示できます。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].inAppMessageController displayNextInAppMessage];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()!.inAppMessageController.displayNextInAppMessage()
```

{% endtab %}
{% endtabs %}

### リアルタイムのアプリ内メッセージ作成と表示 {#real-time-in-app-message-creation-and-display}

アプリ内メッセージはアプリ内でローカルに作成し、Brazeを通じて表示することもできます。これは、アプリ内でリアルタイムにトリガーしたいメッセージを表示する場合に特に便利です。Brazeはローカルで作成されたアプリ内メッセージの分析をサポートしていません。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
  ABKInAppMessageSlideup *customInAppMessage = [[ABKInAppMessageSlideup alloc] init];
  customInAppMessage.message = @"YOUR_CUSTOM_SLIDEUP_MESSAGE";
  customInAppMessage.duration = 2.5;
  customInAppMessage.extras = @{@"key" : @"value"};
  [[Appboy sharedInstance].inAppMessageController addInAppMessage:customInAppMessage];
```

{% endtab %}
{% tab swift %}

```swift
  let customInAppMessage = ABKInAppMessageSlideup.init()
  customInAppMessage.message = "YOUR_CUSTOM_SLIDEUP_MESSAGE"
  customInAppMessage.duration = 2.5
  customInAppMessage.extras = ["key": "value"]
  Appboy.sharedInstance()!.inAppMessageController.add(customInAppMessage)
```

{% endtab %}
{% endtabs %}