{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Acerca de los mensajes HTML {#about-html-messages}

Con la interfaz JavaScript de Braze, puedes aprovechar Braze dentro de las WebViews personalizadas de tu aplicación. El [`ScriptMessageHandler`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler) de la interfaz es responsable de:

1. Inyectar el puente JavaScript de Braze en tu WebView, como se describe en la [Guía del usuario: mensajes HTML dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize#custom-html-messages).
2. Pasar los métodos del puente recibidos de tu WebView al [SDK or kit de desarrollo de software de Braze para Swift](https://github.com/braze-inc/braze-swift-sdk).

## Añadir la interfaz a una WebView {#adding-the-interface-to-a-webview}

Primero, añade el [`ScriptMessageHandler`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler) de `WebViewBridge` a tu aplicación.

```swift
let scriptMessageHandler = Braze.WebViewBridge.ScriptMessageHandler(
  channel: .inAppMessage,
  braze: braze
)
```

Añade el `scriptMessageHandler` inicializado al `userContentController` de un WkWebView.

```swift
configuration.userContentController.add(
  scriptMessageHandler,
  name: Braze.WebViewBridge.ScriptMessageHandler.name
)
```

A continuación, crea la WebView utilizando tu configuración.

```swift
let webView = WKWebView(frame: .zero, configuration: configuration)
```

Cuando hayas terminado, tu código debería ser similar al siguiente:

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

## Ejemplo: Registro de un evento personalizado {#example-logging-a-custom-event}

En el siguiente ejemplo, `BrazeBridge` registra un evento personalizado desde contenido web existente al SDK or kit de desarrollo de software de Braze para SWIFT.

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
