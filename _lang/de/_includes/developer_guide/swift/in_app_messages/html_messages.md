{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Über HTML-Nachrichten {#about-html-messages}

Mit der Braze JavaScript-Schnittstelle können Sie Braze innerhalb der angepassten WebViews Ihrer App nutzen. Der [`ScriptMessageHandler`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler) der Schnittstelle ist verantwortlich für:

1. Einspeisen der Braze JavaScript-Bridge in Ihre WebView, wie beschrieben in [Nutzerhandbuch: In-App-Nachrichten im HTML-Format]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize#custom-html-messages).
2. Übergabe der von Ihrer WebView empfangenen Bridge-Methoden an das [Braze Swift SDK or Software-Development-Kit](https://github.com/braze-inc/braze-swift-sdk).

## Hinzufügen der Schnittstelle zu einer WebView {#adding-the-interface-to-a-webview}

Fügen Sie zunächst den [`ScriptMessageHandler`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler) aus `WebViewBridge` zu Ihrer App hinzu.

```swift
let scriptMessageHandler = Braze.WebViewBridge.ScriptMessageHandler(
  channel: .inAppMessage,
  braze: braze
)
```

Fügen Sie den initialisierten `scriptMessageHandler` zum `userContentController` einer WkWebView hinzu.

```swift
configuration.userContentController.add(
  scriptMessageHandler,
  name: Braze.WebViewBridge.ScriptMessageHandler.name
)
```

Erstellen Sie dann die WebView mit Ihrer Konfiguration.

```swift
let webView = WKWebView(frame: .zero, configuration: configuration)
```

Wenn Sie fertig sind, sollte Ihr Code in etwa wie folgt aussehen:

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

## Beispiel: Ein angepasstes Event protokollieren {#example-logging-a-custom-event}

Im folgenden Beispiel protokolliert `BrazeBridge` ein angepasstes Event aus vorhandenen Web-Inhalten an das Braze Swift SDK or Software-Development-Kit.

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
