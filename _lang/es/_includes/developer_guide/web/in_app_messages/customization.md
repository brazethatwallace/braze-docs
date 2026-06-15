{% multi_lang_include developer_guide/prerequisites/web.md %}

## Estilos personalizados {#custom-styles}

Los elementos de la interfaz de usuario de Braze vienen con un aspecto predeterminado que crea una experiencia de mensajería dentro de la aplicación neutral y busca la coherencia con otras plataformas móviles de Braze. Los estilos predeterminados de Braze se definen en CSS dentro del SDK de Braze.

### Configuración de un estilo predeterminado {#setting-a-default-style}

Al anular los estilos seleccionados en tu aplicación, puedes personalizar nuestros tipos de mensajes dentro de la aplicación estándar con tus propias imágenes de fondo, familias de fuentes, estilos, tamaños, animaciones y mucho más.

Por ejemplo, lo siguiente es un ejemplo de modificación que hará que los encabezados de un mensaje dentro de la aplicación aparezcan en cursiva:

```css
  body .ab-in-app-message .ab-message-header {
    font-style: italic;
  }
```

Consulta los [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) para más información.

### Personalizar el índice z {#customizing-the-z-index}

De manera predeterminada, los mensajes dentro de la aplicación se muestran utilizando `z-index: 9001`. Esto es configurable mediante la [opción de inicialización](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) `inAppMessageZIndex ` en el caso de que tu sitio web estilice elementos con valores superiores a ese.

```javascript
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    inAppMessageZIndex: 12000
});
```

{% alert important %}
Esta característica solo está disponible para Web Braze SDK v3.3.0 y posteriores.
{% endalert %}

## Personalizar el descarte de mensajes {#customizing-message-dismissals}

De forma predeterminada, cuando se muestra un mensaje dentro de la aplicación, al pulsar el botón de escape o hacer clic en el fondo gris de la página se descartará el mensaje. Configura la [opción de inicialización](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) `requireExplicitInAppMessageDismissal` en `true` para evitar este comportamiento y requerir un clic explícito en el botón para descartar los mensajes.

```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    requireExplicitInAppMessageDismissal: true
});
```

## Personalizar el momento de visualización {#customizing-display-timing}

Para anular el momento de visualización predeterminado, elimina las llamadas a `braze.automaticallyShowInAppMessages()` y gestiona los mensajes en `braze.subscribeToInAppMessage()`. Registra tu devolución de llamada antes de `braze.openSession()`, para poder interceptar los mensajes de inicio de sesión y decidir si mostrar o aplazar cada mensaje.

De forma predeterminada, Braze muestra los mensajes dentro de la aplicación cuando se desencadenan y son elegibles para mostrarse. Si necesitas un comportamiento diferente para tu experiencia de la aplicación, utiliza una devolución de llamada personalizada para aplazar o mostrar mensajes según tu propia lógica.

El siguiente ejemplo muestra cómo suscribirse a mensajes dentro de la aplicación desencadenados, aplazar mensajes seleccionados y mostrar mensajes aplazados más tarde:

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT"
});

braze.subscribeToInAppMessage(function (message) {
    // Control-group messages should always be "shown" to log analytics.
    if (message.isControl || message instanceof braze.ControlMessage) {
        braze.showInAppMessage(message);
        return;
    }

    const shouldDefer = true; // Replace with your own display logic

    if (shouldDefer) {
        braze.deferInAppMessage(message);
        return;
    }

    braze.showInAppMessage(message);
});

braze.openSession();

// Later, when your app is ready to display a deferred message:
const deferredMessage = braze.getDeferredInAppMessage();
if (deferredMessage) {
    braze.showInAppMessage(deferredMessage);
}
```

Para obtener orientación relacionada sobre la personalización de la entrega, consulta:

- [Referencia Web de `deferInAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#deferinappmessage)
- [Referencia Web de `subscribeToInAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage)

## Abrir enlaces en una pestaña nueva {#opening-links-in-a-new-tab}

Para configurar tus enlaces de mensajes dentro de la aplicación para que se abran en una pestaña nueva, configura la opción `openInAppMessagesInNewTab` en `true` para forzar que todos los enlaces de los clics de mensajes dentro de la aplicación se abran en una pestaña o ventana nueva.

```javascript
braze.initialize('api-key', { openInAppMessagesInNewTab: true} );
```
