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

アプリ内メッセージ製品を使用すると、`Any Purchase`、`Specific Purchase`、`Session Start`、`Custom Event`、`Push Click` など、さまざまなイベントタイプの結果としてアプリ内メッセージの表示をトリガーできます。さらに、`Specific Purchase`と`Custom Event`トリガーには堅牢なプロパティフィルターが含まれています。

{% alert note %}
トリガーされたアプリ内メッセージは、Braze SDKを通じて記録されたカスタムイベントでのみ機能します。アプリ内メッセージは、APIまたはAPIイベント（購入イベントなど）によってトリガーすることはできません。iOSを使用している場合は、[カスタムイベントの追跡]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=swift)に関する記事を参照して詳細を確認してください。
{% endalert %}

## 配信セマンティクス {#delivery-semantics}

ユーザーが対象になるすべてのアプリ内メッセージは、セッション開始時にユーザーのデバイスに配信されます。1つのイベントによって2つのアプリ内メッセージがトリガーされた場合、優先度の高いアプリ内メッセージが表示されます。SDKのセッション開始セマンティクスの詳細については、[セッションライフサイクル]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_sessions#session-lifecycle)に関する記事をお読みください。配信時に、SDKはアセットをプリフェッチしてトリガー時にすぐに利用できるようにし、表示遅延を最小限に抑えます。

トリガーイベントに複数の適格なアプリ内メッセージが関連付けられている場合、最も優先度の高いアプリ内メッセージのみが配信されます。

アセットがプリフェッチされていないため、配信時（セッション開始、プッシュクリック）にすぐに表示されるアプリ内メッセージには多少の遅延が発生する可能性があります。

## トリガー間の最小時間間隔 {#minimum-time-interval-between-triggers}

デフォルトでは、高品質のユーザーエクスペリエンスを促進するため、アプリ内メッセージのレートは30秒に1回に制限されています。

この値は、`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` に渡される `appboyOptions` パラメーター内の `ABKMinimumTriggerTimeIntervalKey` を使用してオーバーライドできます。`ABKMinimumTriggerTimeIntervalKey` を、アプリ内メッセージ間の最小時間（秒）として使用する整数値に設定します。

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

## 一致するトリガーが見つからない {#failing-to-find-a-matching-trigger}

Brazeが特定のイベントに一致するトリガーを検出できない場合、[`ABKInAppMessageControllerDelegate`](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_in_app_message_controller_delegate-p.html)の[noMatchingTriggerForEvent:name:](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_in_app_message_controller_delegate-p.html#ab4d57b13c51545d487227945a37d4ab8) メソッドを呼び出します。このシナリオを処理するには、デリゲートプロトコルを採用するクラスにこのメソッドを実装してください。

## ローカルのアプリ内メッセージ配信 {#local-in-app-message-delivery}

### アプリ内メッセージスタック {#the-in-app-message-stack}

#### アプリ内メッセージの表示 {#showing-in-app-messages}

ユーザーがアプリ内メッセージを受信する資格がある場合、`ABKInAppMessageController` にはアプリ内メッセージスタックから最新のアプリ内メッセージが提供されます。スタックはメモリに保存されたアプリ内メッセージのみを保持し、一時停止モードからのアプリ起動間にクリアされます。

{% alert important %}
キーボードが画面に表示されているときは、レンダリングが未定義のため、アプリ内メッセージを表示しないでください。
{% endalert %}

#### アプリ内メッセージをスタックに追加する {#adding-in-app-messages-to-the-stack}

ユーザーは、次の状況でアプリ内メッセージを受信できます。

- アプリ内メッセージトリガーイベントが発生した
- セッション開始イベント
- プッシュ通知からアプリを開いた

トリガーされたアプリ内メッセージは、トリガーイベントが発生するとスタックに配置されます。複数のアプリ内メッセージがスタック内にあり、表示を待機している場合、Brazeは最後に受信したアプリ内メッセージを最初に表示します（後入れ先出し）。

#### アプリ内メッセージをスタックに返す {#returning-in-app-messages-to-the-stack}

トリガーされたアプリ内メッセージは、次の状況でスタックに返されることがあります。

- アプリがバックグラウンドにあるときにアプリ内メッセージがトリガーされた。
- 別のアプリ内メッセージが現在表示されている。
- 非推奨の `beforeInAppMessageDisplayed:withKeyboardIsUp:` [UIデリゲートメソッド]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates#in-app-message-delegate)が実装されておらず、キーボードが現在表示されている。
- `beforeInAppMessageDisplayed:` [デリゲートメソッド]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates#core-in-app-message-delegate)または非推奨の `beforeInAppMessageDisplayed:withKeyboardIsUp:` [UIデリゲートメソッド]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates#in-app-message-delegate)が `ABKDisplayInAppMessageLater` を返した。

#### アプリ内メッセージの破棄 {#discarding-in-app-messages}

トリガーされたアプリ内メッセージは、次の状況では破棄されます。

- `beforeInAppMessageDisplayed:` [デリゲートメソッド]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates#core-in-app-message-delegate)または非推奨の `beforeInAppMessageDisplayed:withKeyboardIsUp:` [UIデリゲートメソッド]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates#in-app-message-delegate)が `ABKDiscardInAppMessage` を返した。
- アプリ内メッセージのアセット（画像またはZIPファイル）のダウンロードに失敗した。
- アプリ内メッセージを表示する準備ができているが、タイムアウト時間が経過した。
- デバイスの向きが、トリガーされたアプリ内メッセージの向きと一致しない。
- アプリ内メッセージはフルアプリ内メッセージだが、画像がない。
- アプリ内メッセージは画像のみのモーダルアプリ内メッセージだが、画像がない。

#### アプリ内メッセージ表示を手動でキューに入れる {#manually-queue-in-app-message-display}

アプリ内で別のタイミングでアプリ内メッセージを表示したい場合は、次のメソッドを呼び出してスタックの最上位のアプリ内メッセージを手動で表示できます。

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

### リアルタイムのアプリ内メッセージの作成と表示 {#real-time-in-app-message-creation-and-display}

アプリ内メッセージはアプリ内でローカルに作成し、Braze経由で表示することもできます。これは、アプリ内でリアルタイムにトリガーしたいメッセージを表示する場合に特に便利です。Brazeは、ローカルで作成されたアプリ内メッセージの分析をサポートしていません。

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