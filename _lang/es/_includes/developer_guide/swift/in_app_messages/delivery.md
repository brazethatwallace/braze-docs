{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Desencadenantes de mensajes {#message-triggers}

### Tipos de desencadenantes {#trigger-types}

Los mensajes dentro de la aplicación se desencadenan automáticamente cuando el SDK registra uno de los siguientes tipos de eventos personalizados: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event` y `Push Click`. Ten en cuenta que los desencadenantes `Specific Purchase` y `Custom Event` también contienen filtros de propiedades robustos.

{% alert note %}
Los mensajes dentro de la aplicación no se pueden desencadenar a través de la API ni mediante eventos de la API&#8212;solo mediante eventos personalizados registrados por el SDK. Para obtener más información sobre el registro, consulta [Registro de eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift).
{% endalert %}

### Semántica de la entrega {#delivery-semantics}

Todos los mensajes elegibles dentro de la aplicación se entregan al dispositivo del usuario al inicio de su sesión. Cuando se entregan, el SDK precargará los activos para que estén disponibles en el momento del desencadenamiento, minimizando así la latencia de visualización. Si el evento desencadenante tiene más de un mensaje dentro de la aplicación elegible, solo se entregará el mensaje con la prioridad más alta.

Para obtener más información sobre la semántica de inicio de sesión del SDK, consulta [Ciclo de vida de la sesión]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift).

### Límite de velocidad predeterminado {#default-rate-limit}

De forma predeterminada, el SDK limita la velocidad de los mensajes dentro de la aplicación desencadenados a una vez cada 30 segundos.

Para aplicaciones en producción, no establezcas este valor por debajo de 10 segundos, para que los usuarios no se vean abrumados con mensajes dentro de la aplicación consecutivos. Para pruebas y flujos de aplicaciones de ejemplo, 5 segundos es una configuración habitual.

Puedes establecer este intervalo en `0` para pruebas. Sin embargo, un intervalo de `0` segundos no fuerza a que aparezcan varios mensajes dentro de la aplicación al mismo tiempo. Si un mensaje es visible, otro mensaje desencadenado espera en la pila de mensajes dentro de la aplicación hasta que se pueda mostrar un mensaje.

Para anular esto, actualiza la propiedad `triggerMinimumTimeInterval` en tu configuración de Braze antes de que se inicialice la instancia de Braze. Se puede establecer en cualquier número entero no negativo y representa el intervalo de tiempo mínimo en segundos. Por ejemplo:

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
  endpoint: "YOUR-BRAZE-ENDPOINT"
)
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                    endpoint:@"<BRAZE_ENDPOINT>"];
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5;
Braze *braze = [BrazePlugin initBraze:configuration];
AppDelegate.braze = braze;
```
{% endtab %}
{% endtabs %}

## Pares clave-valor {#key-value-pairs}

Cuando creas una Campaign en Braze, puedes establecer pares clave-valor como `extras`, que el objeto de mensajería dentro de la aplicación puede utilizar para enviar datos a tu aplicación. Por ejemplo:

{% tabs %}
{% tab swift %}

```swift
let customization = message.extras["custom-display"] as? String
if customization == "colorful-slideup" {
  // Perform your custom logic.
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
if ([message.extras[@"custom-display"] isKindOfClass:[NSString class]]) {
  NSString *customization = message.extras[@"custom-display"];
  if ([customization isEqualToString:@"colorful-slideup"]) {
    // Perform your custom logic.
  }
}
```

{% endtab %}
{% endtabs %}

Para una implementación completa, puedes consultar los ejemplos de personalización de mensajes dentro de la aplicación en nuestra [aplicación de ejemplo](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples).

## Desactivación de los desencadenantes automáticos {#disabling-automatic-triggers}

Para evitar que los mensajes dentro de la aplicación se desencadenen automáticamente:

1. Implementa el delegado `BrazeInAppMessageUIDelegate` como se describe en nuestro [artículo sobre iOS aquí](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).
2. Actualiza tu método delegado `inAppMessage(_:displayChoiceForMessage:)` para que devuelva `.discard`.

## Desencadenamiento manual de mensajes {#manually-triggering-messages}

### Uso de un evento del lado del servidor {#using-a-server-side-event}

Para desencadenar mensajes dentro de la aplicación utilizando eventos del lado del servidor, envía un push silencioso al dispositivo para que este registre un evento basado en el SDK. Este evento del SDK puede desencadenar posteriormente el mensaje dentro de la aplicación dirigido al usuario.

#### Paso 1: Manejar el push silencioso y los pares clave-valor {#step-1-handle-silent-push-and-key-value-pairs}

Implementa la siguiente función y llámala dentro del [método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application/):

{% tabs %}
{% tab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  print("A push was received")
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    AppDelegate.braze?.logCustomEvent("IAM Trigger", properties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [AppDelegate.braze logCustomEvent:@"IAM Trigger" properties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
};
```

{% endtab %}
{% endtabs %}

Cuando se reciba el push silencioso, se registrará un evento "desencadenante de mensaje dentro de la aplicación" registrado por el SDK en el perfil de usuario.

{% alert important %}
Dado que se utiliza un mensaje push para registrar un evento personalizado del SDK, Braze necesitará almacenar un token de notificaciones push para cada usuario a fin de habilitar esta solución. Para los usuarios de iOS, Braze solo almacenará un token a partir del momento en que el usuario haya recibido el aviso push del sistema operativo. Antes de esto, el usuario no será localizable mediante push, y la solución anterior no será posible.
{% endalert %}

#### Paso 2: Crea una Campaign push silenciosa {#step-2-create-a-silent-push-campaign}

Crea una [Campaign push silenciosa]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift) que se desencadene a través del evento enviado por el servidor.

![Una Campaign de mensajes dentro de la aplicación con entrega basada en acciones que se entregará a los usuarios cuyos perfiles de usuario tengan el evento personalizado "server_event".]({% image_buster /assets/img_archive/iosServerSentPush.png %})

La Campaign push debe incluir extras de pares clave-valor, que indiquen que esta Campaign push se envía para registrar un evento personalizado del SDK. Este evento se utilizará para desencadenar el mensaje dentro de la aplicación.

![Una Campaign de mensajes dentro de la aplicación con entrega basada en acciones que tiene dos pares clave-valor. "CAMPAIGN_NAME" establecido como "Ejemplo de nombre de mensaje dentro de la aplicación", e "IS_SERVER_EVENT" establecido en "true".]({% image_buster /assets/img_archive/iOSServerPush.png %})

El código del método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` comprueba si existe la clave `IS_SERVER_EVENT` y registrará un evento personalizado del SDK si está presente.

Puedes modificar el nombre o las propiedades del evento enviando el valor deseado dentro de los extras de pares clave-valor de la carga útil push. Al registrar el evento personalizado, estos extras se pueden utilizar como parámetro del nombre del evento o como propiedad del evento.

#### Paso 3: Crea una Campaign de mensajes dentro de la aplicación {#step-3-create-an-in-app-message-campaign}

Crea tu Campaign de mensajes dentro de la aplicación visible para el usuario en el dashboard de Braze. Esta Campaign debe tener una entrega basada en acciones y desencadenarse desde el evento personalizado registrado en el método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`.

En el siguiente ejemplo, el mensaje específico dentro de la aplicación que se va a desencadenar se ha configurado enviando la propiedad del evento como parte del push silencioso inicial.

![Una Campaign de mensajes dentro de la aplicación con entrega basada en acciones que se entregará a los usuarios que realicen el evento personalizado "In-app message trigger" donde "campaign_name" es igual a "IAM Campaign Name Example".]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

{% alert note %}
Ten en cuenta que estos mensajes dentro de la aplicación solo se desencadenarán si se recibe el push silencioso mientras la aplicación está en primer plano.
{% endalert %}

### Mostrar un mensaje predefinido {#displaying-a-pre-defined}

Para mostrar manualmente un mensaje dentro de la aplicación predefinido, utiliza el siguiente método:

```swift
if let inAppMessage = AppDelegate.braze?.inAppMessagePresenter?.nextAvailableMessage() {
  AppDelegate.braze?.inAppMessagePresenter?.present(message: inAppMessage)
}
```

### Mostrar un mensaje en tiempo real {#displaying-a-message-in-real-time}

También puedes mostrar mensajes locales dentro de la aplicación en tiempo real llamando manualmente al método [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:)) en tu `inAppMessagePresenter`. Por ejemplo:

{% tabs %}
{% tab swift %}

```swift
let customInAppMessage = Braze.InAppMessage.slideup(
  .init(message: "YOUR_CUSTOM_SLIDEUP_MESSAGE", slideFrom: .bottom, themes: .defaults)
)
AppDelegate.braze?.inAppMessagePresenter?.present(message: customInAppMessage)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZInAppMessageRaw *customInAppMessage = [[BRZInAppMessageRaw alloc] init];
customInAppMessage.type = BRZInAppMessageRawTypeSlideup;
customInAppMessage.message = @"YOUR_CUSTOM_SLIDEUP_MESSAGE";
customInAppMessage.slideFrom = BRZInAppMessageRawSlideFromBottom;
customInAppMessage.themes = @{
  @"light": BRZInAppMessageRawTheme.defaultLight,
  @"dark": BRZInAppMessageRawTheme.defaultDark
};
[AppDelegate.braze.inAppMessagePresenter presentMessage:customInAppMessage];
```

{% endtab %}
{% endtabs %}

{% alert note %}
Al crear tu propio mensaje dentro de la aplicación, te excluyes de cualquier seguimiento de análisis y tendrás que gestionar manualmente el registro de clics e impresiones utilizando tu `message.context`.
{% endalert %}

## La pila de mensajes dentro de la aplicación {#the-in-app-message-stack}

### Añadir mensajes dentro de la aplicación a la pila {#adding-in-app-messages-to-the-stack}

Los usuarios son elegibles para recibir un mensaje dentro de la aplicación en las siguientes situaciones:

- Se dispara un evento desencadenante de mensajes dentro de la aplicación
- Se inicia una sesión
- La aplicación se abre desde una notificación push

Cuando se dispara el evento desencadenante de un mensaje dentro de la aplicación, este se coloca en una "pila". Si hay varios mensajes dentro de la aplicación en la pila esperando a ser mostrados, Braze mostrará primero el mensaje dentro de la aplicación recibido más recientemente (último en entrar, primero en salir).

Cuando un usuario sea elegible para recibir un mensaje dentro de la aplicación, el `BrazeInAppMessagePresenter` solicitará el último mensaje dentro de la aplicación de la pila de mensajes dentro de la aplicación. La pila solo conserva los mensajes dentro de la aplicación almacenados en memoria y se borra entre los lanzamientos de la aplicación desde el modo suspendido.

### Devolver mensajes dentro de la aplicación a la pila {#returning-in-app-messages-to-the-stack}

Un mensaje dentro de la aplicación desencadenado puede volver a la pila en las siguientes situaciones:

- El mensaje dentro de la aplicación se desencadena cuando la aplicación está en segundo plano.
- Actualmente hay visible otro mensaje dentro de la aplicación.
- El [método delegado](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) `inAppMessage(_:displayChoiceForMessage:)` devolvió `.reenqueue`.

El mensaje dentro de la aplicación desencadenado se colocará en la parte superior de la pila para su posterior visualización cuando un usuario sea elegible para recibir un mensaje dentro de la aplicación.

### Descartar mensajes dentro de la aplicación {#discarding-in-app-messages}

Un mensaje dentro de la aplicación desencadenado se descartará en las siguientes situaciones:

- El [método delegado](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) `inAppMessage(_:displayChoiceForMessage:)` devolvió `.discard`.
- No se ha podido descargar el activo (imagen o archivo ZIP) del mensaje dentro de la aplicación.
- El mensaje dentro de la aplicación está listo para mostrarse, pero ha superado el tiempo de espera.
- La orientación del dispositivo no coincide con la orientación del mensaje dentro de la aplicación desencadenado.

El mensaje dentro de la aplicación se eliminará de la pila. Tras ser descartado, el mensaje dentro de la aplicación puede ser desencadenado posteriormente por otra instancia del evento desencadenante.