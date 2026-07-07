{% multi_lang_include developer_guide/prerequisites/android.md %}

## HTML 메시지 정보 {#about-html-messages}

Braze JavaScript 인터페이스를 사용하면 앱 내 커스텀 WebView에서 Braze를 활용할 수 있습니다. [`InAppMessageJavascriptInterface`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.jsinterface/-in-app-message-javascript-interface/index.html)가 담당하는 역할은 다음과 같습니다:

1. [사용자 가이드: HTML 인앱 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages)에 설명된 대로 WebView에 Braze JavaScript 브릿지를 삽입합니다.
2. WebView에서 받은 브릿지 메서드를 [Braze Android SDK](https://github.com/braze-inc/braze-android-sdk)에 전달합니다.

## 웹뷰에 인터페이스 추가하기 {#adding-the-interface-to-a-webview}

앱의 WebView에서 Braze 기능을 사용하려면 WebView에 Braze JavaScript 인터페이스를 추가하면 됩니다. 인터페이스가 추가되면 [사용자 가이드: HTML 인앱 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages)에서 사용할 수 있는 동일한 API를 커스텀 WebView 내에서도 사용할 수 있습니다.

{% tabs %}
{% tab JAVA %}

```java
String javascriptString = BrazeFileUtils.getAssetFileStringContents(context.getAssets(), "braze-html-bridge.js");
myWebView.loadUrl("javascript:" + javascriptString);

final InAppMessageJavascriptInterface javascriptInterface = new InAppMessageJavascriptInterface(context, inAppMessage);
myWebView.addJavascriptInterface(javascriptInterface, "brazeInternalBridge");
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val javascriptString = context.assets.getAssetFileStringContents("braze-html-bridge.js")
myWebView.loadUrl("javascript:" + javascriptString!!)

val javascriptInterface = InAppMessageJavascriptInterface(context, inAppMessage)
myWebView.addJavascriptInterface(javascriptInterface, "brazeInternalBridge")
```

{% endtab %}
{% endtabs %}

## YouTube 콘텐츠 삽입 {#embedding-youtube-content}

YouTube 및 기타 HTML5 콘텐츠는 HTML 인앱 메시지에서 재생할 수 있습니다. 이를 위해 인앱 메시지가 표시되는 액티비티에서 하드웨어 가속을 활성화해야 합니다. 자세한 내용은 [Android 개발자 가이드](https://developer.android.com/guide/topics/graphics/hardware-accel.html#controlling)를 참조하세요. 하드웨어 가속은 Android API 버전 11 이상에서만 사용할 수 있습니다.

다음은 HTML 스니펫에 삽입된 YouTube 동영상의 예시입니다:

```html
<body>
    <div class="box">
        <div class="relativeTopRight">
            <a href="appboy://close">X</a>
        </div>
        <iframe width="60%" height="50%" src="https://www.youtube.com/embed/_x45EB3BWqI" title="YouTube video player">
        </iframe>
    </div>
</body>
```

## 딥링크 사용 {#using-deep-links}

Android HTML 인앱 메시지에서 딥링크 또는 외부 링크를 사용할 때, JavaScript에서 `brazeBridge.closeMessage()`를 호출하지 **마세요**. SDK의 내부 로직은 링크로 리디렉션할 때 인앱 메시지를 자동으로 닫습니다. `brazeBridge.closeMessage()`를 호출하면 이 프로세스에 간섭하여 사용자가 앱으로 돌아올 때 메시지가 응답하지 않을 수 있습니다.

다음은 코드 스니펫에서 딥링크의 예시입니다:

{% raw %}
```javascript
<script>
document.querySelectorAll('[data-button-id]').forEach(function (node)
Unknown macro: { node.addEventListener('click', function () { brazeBridge.logClick(node.dataset.buttonId); brazeBridge.closeMessage(); }); }
);
</script>
```
{% endraw %}