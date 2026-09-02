{% multi_lang_include developer_guide/prerequisites/web.md %} También tendrás que [configurar las notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web) para el SDK or kit de desarrollo de software Web. Ten en cuenta que solo puedes enviar notificaciones push a usuarios de iOS y iPadOS que utilicen [Safari v16.4](https://developer.apple.com/documentation/safari-release-notes/safari-16_4-release-notes) o posterior.

## Configurar push de Safari para dispositivos móviles {#setting-up-safari-push-for-mobile}

### Paso 1: Crear un archivo de manifiesto {#manifest}

Un [manifiesto de aplicación web](https://developer.mozilla.org/en-US/docs/Web/Manifest) es un archivo JSON que controla cómo se presenta tu sitio web cuando se instala en la pantalla de inicio del usuario.

Por ejemplo, puedes configurar el color del tema de fondo y el icono que usa el [SELECTOR de aplicaciones](https://support.apple.com/en-us/HT202070), si se renderiza a pantalla completa para parecerse a una aplicación nativa, o si la aplicación debe abrirse en modo horizontal o vertical.

Crea un nuevo archivo `manifest.json` en el directorio raíz de tu sitio web, con los siguientes campos obligatorios.

```json
{
  "name": "your app name",
  "short_name": "your app name",
  "display": "fullscreen",
  "icons": [{
    "src": "favicon.ico",
    "sizes": "128x128",
  }]
}
```

La lista completa de campos admitidos se encuentra en la [documentación de MDN sobre el manifiesto de aplicación web](https://developer.mozilla.org/en-US/docs/Web/Manifest).

### Paso 2: Vincular el archivo de manifiesto {#manifest-link}

Añade la siguiente etiqueta `<link>` al elemento `<head>` de tu sitio web, apuntando a la ubicación donde está alojado tu archivo de manifiesto.

```html
<link rel="manifest" href="/manifest.json" />
```

### Paso 3: Añadir un prestador de servicios {#service-worker}

Tu sitio web debe tener un archivo de prestador de servicios que importe la biblioteca de prestador de servicios de Braze, como se describe en nuestra [guía de integración de notificaciones push web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration#step-1-configure-your-sites-service-worker).

### Paso 4: Añadir a la pantalla de inicio {#add-to-homescreen}

Los navegadores populares (como Safari, Chrome, FireFox y Edge) admiten notificaciones push web en sus versiones más recientes. Para solicitar permiso de push en iOS o iPadOS, tu sitio web debe añadirse a la pantalla de inicio del usuario seleccionando **Compartir** > **Añadir a la pantalla de inicio**. [Añadir a la pantalla de inicio](https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc) permite a los usuarios guardar tu sitio web como favorito, añadiendo tu icono a su valiosa pantalla de inicio.

![Un iPhone mostrando opciones para guardar un sitio web como favorito y añadirlo a la pantalla de inicio]({% image_buster /assets/img/push_implementation_guide/add-to-homescreen.png %}){: style="max-width:40%"}

### Paso 5: Mostrar la solicitud de push nativa {#push-prompt}
Una vez que la aplicación se ha añadido a tu pantalla de inicio, puedes solicitar permiso de push cuando el usuario realice una acción (como hacer clic en un botón). Esto se puede hacer usando el método [`requestPushPermission`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestpushpermission), o con un [mensaje dentro de la aplicación de preparación de push sin código]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages).

{% alert note %}
Después de aceptar o rechazar la solicitud, necesitas eliminar y reinstalar el sitio web en tu pantalla de inicio para poder mostrar la solicitud de nuevo.
{% endalert %}

![Una solicitud de push preguntando si se desea "permitir" o "no permitir" las notificaciones]({% image_buster /assets/img/push_implementation_guide/safari-mobile-push-prompt.png %}){: style="max-width:40%"}

Por ejemplo:

```typescript
import { requestPushPermission } from "@braze/web-sdk";

button.onclick = function(){
    requestPushPermission(() => {
        console.log(`User accepted push prompt`);
    }, (temporary) => {
        console.log(`User ${temporary ? "temporarily dismissed" : "permanently denied"} push prompt`);
    });
};
```

## Siguientes pasos {#next-steps}

A continuación, envíate un [mensaje de prueba]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages) para validar la integración. Una vez completada tu integración, puedes utilizar nuestros [mensajes push primer sin código]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) para optimizar tus tasas de adhesión voluntaria a las notificaciones push.