{% multi_lang_include developer_guide/prerequisites/web.md %} También tendrás que [configurar las notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web).

Si estás integrando Braze a través del kit integrado de mParticle en la web, consulta el [paso 3 en la integración de eventos web de Braze en mParticle](https://docs.mparticle.com/integrations/braze/event/#web) para obtener instrucciones sobre cómo implementar avisos de push suave.

## Acerca de los avisos de push suave {#about-soft-push-prompts}

A menudo es buena idea que los sitios implementen un aviso de push "suave" en el que "prepares" al usuario y le expliques por qué quieres enviarle notificaciones push antes de solicitar el permiso de push. Esto es útil porque el navegador limita la frecuencia con la que puedes solicitar permiso directamente al usuario, y si el usuario deniega el permiso, no puedes volver a pedírselo.

Como alternativa, si deseas incluir un manejo personalizado especial, en lugar de llamar a `requestPushPermission()` directamente como se describe en la [integración de push web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration#step-2-browser-registration) estándar, utiliza nuestros [mensajes dentro de la aplicación desencadenados]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web).

{% alert tip %}
Esto se puede hacer sin personalización del SDK or kit de desarrollo de software utilizando nuestro nuevo [push primer sin código]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages).
{% endalert %}

## Configuración de avisos de push suave {#setting-up-soft-push-prompts}

{% multi_lang_include archive/web-v4-rename.md %}

### Paso 1: Crear una Campaign de preparación para push {#step-1-create-a-push-primer-campaign}

Primero, debes crear una Campaign de mensajería dentro de la aplicación de "Preparación para push" en el panel de Braze:

1. Crea un mensaje dentro de la aplicación de tipo **Modal** con el texto y el estilo que desees.
2. A continuación, establece el comportamiento de clic en **Cerrar mensaje**. Este comportamiento se personalizará más adelante.
3. Añade un par clave-valor al mensaje donde la clave sea `msg-id` y el valor sea `push-primer`.
4. Asigna una acción desencadenante de evento personalizado (como "prime-for-push") al mensaje. Puedes crear el evento personalizado manualmente desde el panel si es necesario.

### Paso 2: Eliminar llamadas {#step-2-remove-calls}

En tu integración de SDK or kit de desarrollo de software de Braze, busca y elimina cualquier llamada a `automaticallyShowInAppMessages()` dentro de tu fragmento de código de carga.

### Paso 3: Actualizar la integración {#step-3-update-integration}

Por último, sustituye la llamada eliminada por el siguiente fragmento de código. Llama a `subscribeToInAppMessage()` antes de llamar a `openSession()`. Esto asegura que tu listener de mensajes dentro de la aplicación esté registrado a tiempo para recibir el mensaje de preparación para push.

```javascript
import * as braze from "@braze/web-sdk";
// Be sure to remove any calls to braze.automaticallyShowInAppMessages()
braze.subscribeToInAppMessage(function(inAppMessage) {
  // check if message is not a control variant
  if (inAppMessage instanceof braze.inAppMessage) {
    // access the key-value pairs, defined as `extras`
    const keyValuePairs = inAppMessage.extras || {};
    // check the value of our key `msg-id` defined in the Braze dashboard
    if (keyValuePairs["msg-id"] === "push-primer") {
      // We don't want to display the soft push prompt to users on browsers
      // that don't support push, or if the user has already granted/blocked permission
      if (
        braze.isPushSupported() === false ||
        braze.isPushPermissionGranted() ||
        braze.isPushBlocked()
      ) {
        // do not call `showInAppMessage`
        return;
      }

      // user is eligible to receive the native prompt
      // register a click handler on one of the two buttons
      if (inAppMessage.buttons[0]) {
        // Prompt the user when the first button is clicked
        inAppMessage.buttons[0].subscribeToClickedEvent(function() {
          braze.requestPushPermission(
            function() {
              // success!
            },
            function() {
              // user declined
            }
          );
        });
      }
    }
  }

  // show the in-app message now
  braze.showInAppMessage(inAppMessage);
});
```

Cuando quieras mostrar el aviso de push suave al usuario, llama a `braze.logCustomEvent` con el nombre de evento que desencadene este mensaje dentro de la aplicación.