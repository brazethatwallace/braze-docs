{% multi_lang_include developer_guide/prerequisites/web.md %}

## メッセージトリガー {#message-triggers}

## トリガーの種類 {#trigger-types}

アプリ内メッセージは、SDKが以下のカスタムイベントタイプのいずれかを記録した際に自動的にトリガーされます：`Any Purchase`、`Specific Purchase`、`Session Start`、`Custom Event`、および `Push Click`。なお、`Specific Purchase` および `Custom Event` トリガーには堅牢なプロパティフィルターも含まれています。

{% alert note %}
アプリ内メッセージは、APIまたはAPIイベントによってトリガーすることはできません。SDKによって記録されるカスタムイベントによってのみトリガーされます。ロギングの詳細については、[カスタムイベントのログ記録]({{site.baseurl}}/developer_guide/analytics/logging_events/)を参照してください。
{% endalert %}

### 配信セマンティクス {#delivery-semantics}

すべての適格なアプリ内メッセージは、ユーザーのセッション開始時にデバイスに配信されます。配信されると、SDKはアセットをプリフェッチするため、トリガー時にアセットが利用可能となり、表示の遅延を最小限に抑えます。トリガーイベントに複数の適格なアプリ内メッセージがある場合、最も優先度の高いメッセージのみが配信されます。

SDKのセッション開始セマンティクスについて詳しくは、[セッションのライフサイクル]({{site.baseurl}}/developer_guide/platform_integration_guides/analytics/tracking_sessions/)を参照してください。

### レート制限 {#rate-limits}

デフォルトでは、SDKはトリガーされたアプリ内メッセージを30秒に1回にレート制限しています。

本番アプリでは、この値を10秒未満に設定しないでください。連続するアプリ内メッセージでユーザーが圧倒されるのを防ぐためです。テストやサンプルアプリのフローでは、5秒が一般的な設定です。

テスト用にこの間隔を `0` に設定することもできます。ただし、`0` 秒の間隔は複数のアプリ内メッセージを同時に表示させるものではありません。別のモーダルまたはフルアプリ内メッセージがすでに表示されている場合、`braze.showInAppMessage` は `false` を返し、新しいメッセージは表示されません。

これを上書きするには、Brazeインスタンスが初期化される前に、Braze設定に以下のプロパティを追加します。任意の非負の整数に設定でき、最小の時間間隔を秒単位で表します。以下に例を示します。

```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```

## キーと値のペア {#key-value-pairs}

Brazeでキャンペーンを作成する際、キーと値のペアを `extras` として設定できます。アプリ内メッセージングオブジェクトはこれを使用してアプリにデータを送信できます。以下に例を示します。

`````````javascript
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

## 自動トリガーを無効にする {#disabling-automatic-triggers}

アプリ内メッセージが自動的にトリガーされるのを防ぐには：

読み込みスニペット内の `braze.automaticallyShowInAppMessages()` 呼び出しを削除し、アプリ内メッセージの表示・非表示を処理するカスタムロジックを作成します。

`````````javascript
braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message

  if (inAppMessage.isControl) { // v4.5.0+, otherwise use  `inAppMessage instanceof braze.ControlMessage`
     return braze.showInAppMessage(inAppMessage);
  }

  // Display the in-app message. You could defer display here by pushing this message to code within your own application.
  // If you don't want to use the Braze built-in display capabilities, you could alternatively pass the in-app message to your own display code here.

  if ( should_show_the_message_according_to_your_custom_logic ) {
      braze.showInAppMessage(inAppMessage);
  } else {
      // do nothing
  }
});
```

{% alert important %}
Webサイトから `braze.automaticallyShowInAppMessages()` を削除せずに `braze.showInAppMessage` を呼び出すと、メッセージが複数回表示される可能性があります。
{% endalert %}

`inAppMessage` パラメータは [`braze.InAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) サブクラスまたは [`braze.ControlMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.controlmessage.html) オブジェクトになり、それぞれにさまざまなライフサイクルイベントのサブスクリプションメソッドがあります。完全なドキュメントについては、[JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html)を参照してください。

[`Modal`]({{site.baseurl}}/developer_guide/in_app_messages/?tab=modal&sdktab=web) または [`Full`]({{site.baseurl}}/developer_guide/in_app_messages/?tab=full&sdktab=web) アプリ内メッセージは一度に1つしか表示できません。すでに1つのモーダルまたはフルメッセージが表示されているときに2つ目を表示しようとすると、`braze.showInAppMessage` はfalseを返し、2つ目のメッセージは表示されません。

## 手動でメッセージをトリガーする {#manually-triggering-messages}

### リアルタイムでメッセージを表示する {#displaying-a-message-in-real-time}

アプリ内メッセージはサイト内で作成し、リアルタイムでローカルに表示することもできます。ダッシュボードで使用できるすべてのカスタマイズオプションはローカルでも使用できます。これは、アプリ内でトリガーしたいメッセージをリアルタイムで表示する場合に特に便利です。ただし、これらのローカルで作成されたメッセージの分析は、Brazeダッシュボードでは利用できません。

`````````javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```

## 離脱意図メッセージのトリガー {#triggering-exit-intent-messages}

離脱意図メッセージとは、訪問者がサイトを離れる前に重要な情報を伝えるために使用される、邪魔にならないアプリ内メッセージです。

これらのメッセージタイプにトリガーを設定するには、Webサイトに離脱意図ライブラリー（[ouibounceのオープンソースライブラリー](https://github.com/carlsednaoui/ouibounce)など）を実装し、以下のコードを使用してBrazeでカスタムイベントとして `'exit intent'` を記録します。これにより、今後のアプリ内メッセージキャンペーンでこのメッセージタイプをカスタムイベントトリガーとして使用できます。

`````````javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```
