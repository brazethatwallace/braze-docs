{% multi_lang_include developer_guide/prerequisites/android.md %}

## Acerca de los mensajes HTML {#about-html-messages}

Con la interfaz JavaScript de Braze, puedes aprovechar Braze dentro de las WebViews personalizadas de tu aplicación. La [`InAppMessageJavascriptInterface`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.jsinterface/-in-app-message-javascript-interface/index.html) es responsable de:

1. Inyectar el puente JavaScript de Braze en tu WebView, como se describe en la [Guía del usuario: mensajes HTML dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages).
2. Pasar los métodos del puente recibidos de tu WebView al [SDK or kit de desarrollo de software de Braze para Android](https://github.com/braze-inc/braze-android-sdk).

## Añadir la interfaz a una WebView {#adding-the-interface-to-a-webview}

Puedes utilizar la funcionalidad de Braze desde una WebView en tu aplicación añadiendo la interfaz JavaScript de Braze a tu WebView. Una vez añadida la interfaz, la misma API disponible para la [Guía del usuario: mensajes HTML dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages) estará disponible en tu WebView personalizada.

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

## Incrustar contenido de YouTube {#embedding-youtube-content}

YouTube y otros contenidos HTML5 pueden reproducirse en mensajes HTML dentro de la aplicación. Esto requiere que la aceleración por hardware esté habilitada en la actividad en la que se muestra el mensaje dentro de la aplicación; consulta la [guía del desarrollador de Android](https://developer.android.com/guide/topics/graphics/hardware-accel.html#controlling) para más detalles. La aceleración por hardware solo está disponible en las versiones 11 y posteriores de la API de Android.

A continuación se muestra un ejemplo de un video de YouTube incrustado en un fragmento de código HTML:

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

## Uso de vínculos profundos {#using-deep-links}

Cuando utilices vínculos profundos o enlaces externos en mensajes HTML dentro de aplicaciones Android, **no** llames a `brazeBridge.closeMessage()` en tu JavaScript. La lógica interna del SDK or kit de desarrollo de software cierra automáticamente el mensaje dentro de la aplicación cuando redirige a un enlace. Llamar a `brazeBridge.closeMessage()` interfiere en este proceso y puede provocar que el mensaje deje de responder cuando los usuarios vuelvan a tu aplicación.

A continuación se muestra un ejemplo de un vínculo profundo en un fragmento de código:

{% raw %}
```javascript
<script>
document.querySelectorAll('[data-button-id]').forEach(function (node)
Unknown macro: { node.addEventListener('click', function () { brazeBridge.logClick(node.dataset.buttonId); brazeBridge.closeMessage(); }); }
);
</script>
```
{% endraw %}