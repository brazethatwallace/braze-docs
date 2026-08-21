{% multi_lang_include developer_guide/prerequisites/swift.md %}

## HTML 메시지 정보 {#about-html-messages}

Braze JavaScript 인터페이스를 사용하면 앱 내 커스텀 WebView에서 Braze를 활용할 수 있습니다. 인터페이스의 [`ScriptMessageHandler`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler)가 담당하는 역할은 다음과 같습니다:

1. [사용자 가이드: HTML 인앱 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize#custom-html-messages)에 설명된 대로 WebView에 Braze JavaScript 브릿지를 삽입합니다.
2. WebView에서 받은 브릿지 메서드를 [Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk)에 전달합니다.

## 웹뷰에 인터페이스 추가하기 {#adding-the-interface-to-a-webview}

먼저 `WebViewBridge`의 [`ScriptMessageHandler`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler)를 앱에 추가합니다.

```swift
let scriptMessageHandler = Braze.WebViewBridge.ScriptMessageHandler(
  channel: .inAppMessage,
  braze: braze
)
```

초기화된 `scriptMessageHandler`를 WkWebView의 `userContentController`에 추가합니다.

```swift
configuration.userContentController.add(
  scriptMessageHandler,
  name: Braze.WebViewBridge.ScriptMessageHandler.name
)
```

그런 다음 설정을 사용하여 웹뷰를 생성합니다.

```swift
let webView = WKWebView(frame: .zero, configuration: configuration)
```

완료되면 코드는 다음과 유사해야 합니다:

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

## 예제: 커스텀 이벤트 로깅 {#example-logging-a-custom-event}

다음 예제에서 `BrazeBridge`는 기존 웹 콘텐츠에서 Braze Swift SDK로 커스텀 이벤트를 로깅합니다.

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
