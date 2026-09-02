{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Sobre mensagens HTML {#about-html-messages}

Com a interface JavaScript da Braze, você pode aproveitar a Braze dentro das WebViews personalizadas em seu app. O [`ScriptMessageHandler`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler) da interface é responsável por:

1. Injetar a ponte JavaScript da Braze em sua WebView, conforme descrito em [Guia do Usuário: Mensagens HTML no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize#custom-html-messages).
2. Passar os métodos da ponte recebidos de sua WebView para o [Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk).

## Adição da interface a um WebView {#adding-the-interface-to-a-webview}

Primeiro, adicione o [`ScriptMessageHandler`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler) do `WebViewBridge` ao seu app.

```swift
let scriptMessageHandler = Braze.WebViewBridge.ScriptMessageHandler(
  channel: .inAppMessage,
  braze: braze
)
```

Adicione o `scriptMessageHandler` inicializado ao `userContentController` de um WkWebView.

```swift
configuration.userContentController.add(
  scriptMessageHandler,
  name: Braze.WebViewBridge.ScriptMessageHandler.name
)
```

Em seguida, crie o WebView usando sua configuração.

```swift
let webView = WKWebView(frame: .zero, configuration: configuration)
```

Quando terminar, seu código deve ser semelhante ao seguinte:

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

## Exemplo: Registrando um evento personalizado {#example-logging-a-custom-event}

No exemplo a seguir, `BrazeBridge` registra um evento personalizado a partir de conteúdo web existente para o SDK Swift da Braze.

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
