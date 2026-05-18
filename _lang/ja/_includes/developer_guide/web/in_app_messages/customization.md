{% multi_lang_include developer_guide/prerequisites/web.md %}

## カスタムスタイル {#custom-styles}

BrazeのUI要素はデフォルトの外観と操作感を備えており、ニュートラルなアプリ内メッセージ体験を提供し、他のBrazeモバイルプラットフォームとの一貫性を目指しています。デフォルトのBrazeスタイルは、Braze SDK内のCSSで定義されています。

### デフォルトスタイルの設定 {#setting-a-default-style}

アプリケーションで選択したスタイルを上書きすることで、独自の背景画像、フォントファミリ、スタイル、サイズ、アニメーションなどを使用して標準アプリ内メッセージタイプをカスタマイズできます。

たとえば、次の例はアプリ内メッセージのヘッダーをイタリックで表示する上書きを示しています。

```css
  body .ab-in-app-message .ab-message-header {
    font-style: italic;
  }
```

詳細については[JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html)を参照してください。

### z-indexをカスタマイズする {#customizing-the-z-index}

デフォルトでは、アプリ内メッセージは `z-index: 9001` を使用して表示されます。Webサイトがそれよりも高い値で要素をスタイルしているシナリオでは、`inAppMessageZIndex ` [初期化オプション](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions)を使用して設定できます。

`````````javascript
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    inAppMessageZIndex: 12000
});
```

{% alert important %}
この機能は、Web Braze SDK v3.3.0以降でのみ使用できます。
{% endalert %}

## メッセージの閉じ方をカスタマイズする {#customizing-message-dismissals}

デフォルトでは、アプリ内メッセージが表示されているときにエスケープキーを押すか、ページのグレーアウトした背景をクリックすると、メッセージが閉じられます。`requireExplicitInAppMessageDismissal` [初期化オプション](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions)を`true`に設定すると、この動作を無効にし、メッセージを閉じるために明示的なボタンクリックを必要とするようにできます。

`````````javascript
import * as braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    requireExplicitInAppMessageDismissal: true
});
```

## 表示タイミングをカスタマイズする {#customizing-display-timing}

デフォルトの表示タイミングを上書きするには、`braze.automaticallyShowInAppMessages()` の呼び出しを削除し、`braze.subscribeToInAppMessage()` でメッセージを処理します。`braze.openSession()` の前にコールバックを登録することで、セッション開始メッセージをインターセプトし、各メッセージを表示するか延期するかを決定できます。

デフォルトでは、Brazeはアプリ内メッセージがトリガーされ、表示対象となったときに表示します。アプリ体験に異なる動作が必要な場合は、カスタムコールバックを使用して、独自のロジックに基づいてメッセージを延期または表示できます。

次の例は、トリガーされたアプリ内メッセージをサブスクライブし、選択したメッセージを延期し、延期したメッセージを後で表示する方法を示しています。

`````````javascript
import * as braze from "@braze/web-sdk";

braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT"
});

braze.subscribeToInAppMessage(function (message) {
    // Control-group messages should always be "shown" to log analytics.
    if (message.isControl || message instanceof braze.ControlMessage) {
        braze.showInAppMessage(message);
        return;
    }

    const shouldDefer = true; // Replace with your own display logic

    if (shouldDefer) {
        braze.deferInAppMessage(message);
        return;
    }

    braze.showInAppMessage(message);
});

braze.openSession();

// Later, when your app is ready to display a deferred message:
const deferredMessage = braze.getDeferredInAppMessage();
if (deferredMessage) {
    braze.showInAppMessage(deferredMessage);
}
```

関連する配信カスタマイズのガイダンスについては、以下を参照してください。

- [Web `deferInAppMessage` リファレンス](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#deferinappmessage)
- [Web `subscribeToInAppMessage` リファレンス](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage)

## リンクを新しいタブで開く {#opening-links-in-a-new-tab}

アプリ内メッセージのリンクを新しいタブで開くように設定するには、`openInAppMessagesInNewTab` オプションを `true` に設定して、アプリ内メッセージのクリックによるすべてのリンクが新しいタブまたはウィンドウで開くようにします。

`````````javascript
braze.initialize('api-key', { openInAppMessagesInNewTab: true} );
```
