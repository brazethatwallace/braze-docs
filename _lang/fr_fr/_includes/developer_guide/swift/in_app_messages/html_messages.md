{% multi_lang_include developer_guide/prerequisites/swift.md %}

## À propos des messages HTML {#about-html-messages}

Grâce à l'interface JavaScript de Braze, vous pouvez exploiter Braze à l'intérieur des WebViews personnalisées de votre application. Le [`ScriptMessageHandler`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler) de l'interface est responsable de :

1. Injecter le pont JavaScript de Braze dans votre WebView, comme indiqué dans le [guide d'utilisation : Messages HTML in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize#custom-html-messages).
2. Transmettre les méthodes de pont reçues de votre WebView au [SDK Swift de Braze](https://github.com/braze-inc/braze-swift-sdk).

## Ajouter l'interface à une WebView {#adding-the-interface-to-a-webview}

Tout d'abord, ajoutez le [`ScriptMessageHandler`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler) de `WebViewBridge` à votre application.

```swift
let scriptMessageHandler = Braze.WebViewBridge.ScriptMessageHandler(
  channel: .inAppMessage,
  braze: braze
)
```

Ajoutez le `scriptMessageHandler` initialisé au `userContentController` d'une WkWebView.

```swift
configuration.userContentController.add(
  scriptMessageHandler,
  name: Braze.WebViewBridge.ScriptMessageHandler.name
)
```

Créez ensuite la WebView en utilisant votre configuration.

```swift
let webView = WKWebView(frame: .zero, configuration: configuration)
```

Lorsque vous avez terminé, votre code devrait ressembler à ce qui suit :

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

## Exemple : journaliser un événement personnalisé {#example-logging-a-custom-event}

Dans l'exemple suivant, `BrazeBridge` journalise un événement personnalisé à partir de contenu web existant vers le SDK Swift de Braze.

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
