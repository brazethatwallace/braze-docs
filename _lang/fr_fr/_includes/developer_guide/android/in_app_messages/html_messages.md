{% multi_lang_include developer_guide/prerequisites/android.md %}

## À propos des messages HTML {#about-html-messages}

Grâce à l'interface JavaScript de Braze, vous pouvez exploiter Braze à l'intérieur des WebViews personnalisées de votre application. L'élément [`InAppMessageJavascriptInterface`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.jsinterface/-in-app-message-javascript-interface/index.html) est responsable de :

1. Injecter le pont JavaScript de Braze dans votre WebView, comme indiqué dans le [guide d'utilisation : Messages HTML in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages).
2. Transmettre les méthodes de pont reçues de votre WebView au [SDK Android de Braze](https://github.com/braze-inc/braze-android-sdk).

## Ajouter l'interface à une WebView {#adding-the-interface-to-a-webview}

Pour utiliser les fonctionnalités de Braze à partir d'une WebView dans votre application, ajoutez l'interface JavaScript de Braze à votre WebView. Une fois l'interface ajoutée, la même API disponible pour le [guide d'utilisation : Messages HTML in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages) sera accessible dans votre WebView personnalisée.

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

## Intégration de contenu YouTube {#embedding-youtube-content}

YouTube et d'autres contenus HTML5 peuvent être lus dans des messages in-app HTML. Cela nécessite que l'accélération matérielle soit activée dans l'activité où le message in-app est affiché. Consultez le [guide du développeur Android](https://developer.android.com/guide/topics/graphics/hardware-accel.html#controlling) pour plus de détails. L'accélération matérielle est uniquement disponible sur les versions 11 et ultérieures de l'API Android.

Voici un exemple de vidéo YouTube intégrée dans un extrait de code HTML :

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

## Utilisation des liens profonds {#using-deep-links}

Lorsque vous utilisez des liens profonds ou des liens externes dans des messages in-app HTML Android, **n'appelez pas** `brazeBridge.closeMessage()` dans votre JavaScript. La logique interne du SDK ferme automatiquement le message in-app lorsqu'il redirige vers un lien. L'appel de `brazeBridge.closeMessage()` interfère avec ce processus et peut entraîner un blocage du message lorsque les utilisateurs reviennent à votre application.

Voici un exemple de lien profond dans un extrait de code :

{% raw %}
```javascript
<script>
document.querySelectorAll('[data-button-id]').forEach(function (node)
Unknown macro: { node.addEventListener('click', function () { brazeBridge.logClick(node.dataset.buttonId); brazeBridge.closeMessage(); }); }
);
</script>
```
{% endraw %}