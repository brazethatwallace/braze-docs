{% multi_lang_include developer_guide/prerequisites/android.md %}

## Über HTML-Nachrichten {#about-html-messages}

Mit der Braze JavaScript-Schnittstelle können Sie Braze innerhalb der angepassten WebViews Ihrer App nutzen. Die [`InAppMessageJavascriptInterface`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.jsinterface/-in-app-message-javascript-interface/index.html) ist verantwortlich für:

1. Einspeisen der Braze JavaScript-Bridge in Ihre WebView, wie beschrieben in [Nutzerhandbuch: In-App-Nachrichten im HTML-Format]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages).
2. Übergabe der von Ihrer WebView empfangenen Bridge-Methoden an das [Braze Android SDK or Software-Development-Kit](https://github.com/braze-inc/braze-android-sdk).

## Hinzufügen der Schnittstelle zu einer WebView {#adding-the-interface-to-a-webview}

Sie können die Braze-Funktionen von einer WebView in Ihrer App nutzen, indem Sie die Braze JavaScript-Schnittstelle zu Ihrer WebView hinzufügen. Nachdem die Schnittstelle hinzugefügt wurde, steht dieselbe API, die auch für [Nutzerhandbuch: In-App-Nachrichten im HTML-Format]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages) verfügbar ist, in Ihrer angepassten WebView zur Verfügung.

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

## YouTube-Inhalte einbetten {#embedding-youtube-content}

YouTube und andere HTML5-Inhalte können in HTML-In-App-Nachrichten abgespielt werden. Dazu muss die Hardware-Beschleunigung in der Activity aktiviert sein, in der die In-App-Nachricht angezeigt wird. Weitere Informationen finden Sie im [Android-Entwicklerhandbuch](https://developer.android.com/guide/topics/graphics/hardware-accel.html#controlling). Die Hardware-Beschleunigung ist nur für Android-API-Versionen ab Version 11 verfügbar.

Im Folgenden sehen Sie ein Beispiel für ein eingebettetes YouTube-Video in einem HTML-Snippet:

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

## Verwendung von Deeplinks {#using-deep-links}

Bei der Verwendung von Deeplinks oder externen Links in Android-HTML-In-App-Nachrichten sollten Sie `brazeBridge.closeMessage()` in Ihrem JavaScript **nicht** aufrufen. Die interne Logik des SDK or Software-Development-Kit schließt die In-App-Nachricht automatisch, wenn sie zu einem Link weiterleitet. Der Aufruf von `brazeBridge.closeMessage()` beeinträchtigt diesen Prozess und kann dazu führen, dass die Nachricht nicht mehr reagiert, wenn Nutzer:innen zu Ihrer App zurückkehren.

Im Folgenden sehen Sie ein Beispiel für einen Deeplink in einem Code-Snippet:

{% raw %}
```javascript
<script>
document.querySelectorAll('[data-button-id]').forEach(function (node)
Unknown macro: { node.addEventListener('click', function () { brazeBridge.logClick(node.dataset.buttonId); brazeBridge.closeMessage(); }); }
);
</script>
```
{% endraw %}