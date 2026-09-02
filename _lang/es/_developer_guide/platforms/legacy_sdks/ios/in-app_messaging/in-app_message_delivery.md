---
nav_title: Entrega de mensajes dentro de la aplicación
article_title: Entrega de mensajes dentro de la aplicación para iOS
platform: iOS
page_order: 3
description: "Este artículo de referencia trata sobre la entrega de mensajes dentro de la aplicación en iOS, enumerando los distintos tipos de desencadenantes, la semántica de la entrega y los pasos para desencadenar eventos."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Entrega de mensajes dentro de la aplicación {#in-app-message-delivery}

## Tipos de desencadenadores {#trigger-types}

Nuestro producto de In-App Messages te permite desencadenar la visualización de mensajes dentro de la aplicación como resultado de varios tipos de eventos diferentes: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event` y `Push Click`. Además, los desencadenadores `Specific Purchase` y `Custom Event` contienen filtros de propiedades robustos.

{% alert note %}
Los mensajes dentro de la aplicación desencadenados solo funcionan con eventos personalizados registrados a través de Braze SDK or kit de desarrollo de software. Los mensajes dentro de la aplicación no se pueden desencadenar a través de la API ni mediante eventos de la API (como los eventos de compra). Si estás trabajando con iOS, visita nuestro artículo sobre [seguimiento de eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=swift) para obtener más información.
{% endalert %}

## Semántica de entrega {#delivery-semantics}

Todos los mensajes dentro de la aplicación para los que un usuario es elegible se entregan al dispositivo del usuario al inicio de la sesión. En el caso de que un evento desencadene dos mensajes dentro de la aplicación, se mostrará el mensaje dentro de la aplicación con mayor prioridad. Para más información sobre la semántica de inicio de sesión del SDK or kit de desarrollo de software, consulta nuestro [ciclo de vida de la sesión]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/analytics/tracking_sessions#session-lifecycle). Tras la entrega, el SDK or kit de desarrollo de software precargará los activos para que estén disponibles de inmediato en el momento del desencadenamiento, minimizando la latencia de visualización.

Cuando un evento desencadenante tiene más de un mensaje dentro de la aplicación elegible asociado, solo se entregará el mensaje dentro de la aplicación con la prioridad más alta.

Puede haber cierta latencia en los mensajes dentro de la aplicación que se muestran inmediatamente tras la entrega (inicio de sesión, clic en push) debido a que los activos no se han precargado.

## Intervalo de tiempo mínimo entre desencadenadores {#minimum-time-interval-between-triggers}

De forma predeterminada, limitamos la tasa de los mensajes dentro de la aplicación a una vez cada 30 segundos para facilitar una experiencia de usuario de calidad.

Puedes anular este valor a través de `ABKMinimumTriggerTimeIntervalKey` dentro del parámetro `appboyOptions` que se pasa a `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Establece `ABKMinimumTriggerTimeIntervalKey` en el valor entero que desees como tiempo mínimo en segundos entre mensajes dentro de la aplicación:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Sets the minimum trigger time interval to 5 seconds
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKMinimumTriggerTimeIntervalKey : @(5) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:[ABKMinimumTriggerTimeIntervalKey : 5])
```

{% endtab %}
{% endtabs %}

## Cuando no se encuentra un desencadenante coincidente {#failing-to-find-a-matching-trigger}

Cuando Braze no encuentra un desencadenante coincidente para un evento en particular, llamará al método [noMatchingTriggerForEvent:name:](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_in_app_message_controller_delegate-p.html#ab4d57b13c51545d487227945a37d4ab8) del [`ABKInAppMessageControllerDelegate`](https://appboy.github.io/appboy-ios-sdk/docs/protocol_a_b_k_in_app_message_controller_delegate-p.html). Implementa este método en tu clase que adopte el protocolo de delegado para manejar este escenario.

## Entrega local de mensajes dentro de la aplicación {#local-in-app-message-delivery}

### La pila de mensajes dentro de la aplicación {#the-in-app-message-stack}

#### Mostrar mensajes dentro de la aplicación {#showing-in-app-messages}

Cuando un usuario es elegible para recibir un mensaje dentro de la aplicación, se ofrecerá al `ABKInAppMessageController` el mensaje dentro de la aplicación más reciente de la pila de mensajes dentro de la aplicación. La pila solo conserva los mensajes dentro de la aplicación almacenados en memoria y se vacía entre los lanzamientos de la aplicación desde el modo suspendido.

{% alert important %}
No muestres mensajes dentro de la aplicación cuando el teclado esté visible en pantalla, ya que el renderizado no está definido en esta circunstancia.
{% endalert %}

#### Añadir mensajes dentro de la aplicación a la pila {#adding-in-app-messages-to-the-stack}

Los usuarios son elegibles para recibir un mensaje dentro de la aplicación en las siguientes situaciones:

- Se dispara un evento desencadenante de mensaje dentro de la aplicación
- Evento de inicio de sesión
- La aplicación se abre desde una notificación push

Los mensajes dentro de la aplicación desencadenados se colocan en la pila cuando se dispara su evento desencadenante. Si hay varios mensajes dentro de la aplicación en la pila esperando a ser mostrados, Braze mostrará primero el mensaje dentro de la aplicación recibido más recientemente (último en entrar, primero en salir).

#### Devolver mensajes dentro de la aplicación a la pila {#returning-in-app-messages-to-the-stack}

Un mensaje dentro de la aplicación desencadenado puede devolverse a la pila en las siguientes situaciones:

- El mensaje dentro de la aplicación se desencadena cuando la aplicación está en segundo plano.
- Otro mensaje dentro de la aplicación está visible en ese momento.
- El [método de delegado de UI]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates#in-app-message-delegate) obsoleto `beforeInAppMessageDisplayed:withKeyboardIsUp:` no se ha implementado y el teclado se está mostrando actualmente.
- El [método de delegado]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates#core-in-app-message-delegate) `beforeInAppMessageDisplayed:` o el [método de delegado de UI]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates#in-app-message-delegate) obsoleto `beforeInAppMessageDisplayed:withKeyboardIsUp:` devolvió `ABKDisplayInAppMessageLater`.

#### Descartar mensajes dentro de la aplicación {#discarding-in-app-messages}

Un mensaje dentro de la aplicación desencadenado se descartará en las siguientes situaciones:

- El [método de delegado]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates#core-in-app-message-delegate) `beforeInAppMessageDisplayed:` o el [método de delegado de UI]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates#in-app-message-delegate) obsoleto `beforeInAppMessageDisplayed:withKeyboardIsUp:` devolvió `ABKDiscardInAppMessage`.
- El activo (imagen o archivo ZIP) del mensaje dentro de la aplicación no se pudo descargar.
- El mensaje dentro de la aplicación está listo para mostrarse, pero ha superado la duración del tiempo de espera.
- La orientación del dispositivo no coincide con la orientación del mensaje dentro de la aplicación desencadenado.
- El mensaje dentro de la aplicación es un mensaje dentro de la aplicación a pantalla completa pero no tiene imagen.
- El mensaje dentro de la aplicación es un mensaje modal dentro de la aplicación de solo imagen pero no tiene imagen.

#### Poner manualmente en cola la visualización de mensajes dentro de la aplicación {#manually-queue-in-app-message-display}

Si deseas mostrar un mensaje dentro de la aplicación en otros momentos dentro de tu aplicación, puedes mostrar manualmente el mensaje dentro de la aplicación en la parte superior de la pila llamando al siguiente método:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].inAppMessageController displayNextInAppMessage];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()!.inAppMessageController.displayNextInAppMessage()
```

{% endtab %}
{% endtabs %}

### Creación y visualización de mensajes dentro de la aplicación en tiempo real {#real-time-in-app-message-creation-and-display}

Los mensajes dentro de la aplicación también se pueden crear localmente dentro de la aplicación y mostrarse a través de Braze. Esto es particularmente útil para mostrar mensajes que deseas desencadenar dentro de la aplicación en tiempo real. Braze no admite análisis de mensajes dentro de la aplicación creados localmente.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
  ABKInAppMessageSlideup *customInAppMessage = [[ABKInAppMessageSlideup alloc] init];
  customInAppMessage.message = @"YOUR_CUSTOM_SLIDEUP_MESSAGE";
  customInAppMessage.duration = 2.5;
  customInAppMessage.extras = @{@"key" : @"value"};
  [[Appboy sharedInstance].inAppMessageController addInAppMessage:customInAppMessage];
```

{% endtab %}
{% tab swift %}

```swift
  let customInAppMessage = ABKInAppMessageSlideup.init()
  customInAppMessage.message = "YOUR_CUSTOM_SLIDEUP_MESSAGE"
  customInAppMessage.duration = 2.5
  customInAppMessage.extras = ["key": "value"]
  Appboy.sharedInstance()!.inAppMessageController.add(customInAppMessage)
```

{% endtab %}
{% endtabs %}