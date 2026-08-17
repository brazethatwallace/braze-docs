{% multi_lang_include developer_guide/prerequisites/swift.md %}

## HTMLメッセージについて {#about-html-messages}

Braze JavaScriptインターフェイスを使用すると、アプリ内のカスタムWebViewでBrazeを活用できます。インターフェイスの[`ScriptMessageHandler`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler)は以下の役割を担います。

1. [ユーザーガイド：HTMLアプリ内メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize#custom-html-messages)に記載されているように、WebViewにBraze JavaScriptブリッジを挿入します。
2. WebViewから受け取ったブリッジメソッドを[Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk)に渡します。

## WebViewへのインターフェイスの追加 {#adding-the-interface-to-a-webview}

まず、`WebViewBridge`の[`ScriptMessageHandler`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler)をアプリに追加します。

```swift
let scriptMessageHandler = Braze.WebViewBridge.ScriptMessageHandler(
  channel: .inAppMessage,
  braze: braze
)
```

初期化した`scriptMessageHandler`をWkWebViewの`userContentController`に追加します。

```swift
configuration.userContentController.add(
  scriptMessageHandler,
  name: Braze.WebViewBridge.ScriptMessageHandler.name
)
```

次に、設定を使用してWebViewを作成します。

```swift
let webView = WKWebView(frame: .zero, configuration: configuration)
```

完了すると、コードは以下のようになります。

```swift
// Create the script message handler using your initialized Braze instance.
let scriptMessageHandler = Braze.WebViewBridge.ScriptMessageHandler(
  channel: .inAppMessage,
  braze: braze
)

// Create a web view configuration and setup the script message handler.
let configuration = WKWebViewConfiguration()
configuration.userContentController.addUserScript(
  Braze.WebViewBridge.ScriptMessageHandler.script
)
configuration.userContentController.add(
  scriptMessageHandler,
  name: Braze.WebViewBridge.ScriptMessageHandler.name
)

// Create the webview using the configuration
let webView = WKWebView(frame: .zero, configuration: configuration)
```

## 例：カスタムイベントのログ記録 {#example-logging-a-custom-event}

以下の例では、`BrazeBridge`が既存のWebコンテンツからBraze Swift SDKにカスタムイベントをログ記録します。

```javascript
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Logging data via BrazeBridge Example</title>
    <script>
      function logData(data) {
        window.brazeBridge.logCustomEvent(data);
      }
    </script>
  </head>

  <body>
    <input
      type="button"
      value="Click to log a custom Event 'completed_level'"
      onclick="logData('completed_level')"
    />
  </body>
</html>
```
