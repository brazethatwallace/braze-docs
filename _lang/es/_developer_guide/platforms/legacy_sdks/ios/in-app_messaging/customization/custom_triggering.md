---
nav_title: Desencadenado personalizado
article_title: Personalizar la activación de mensajes dentro de la aplicación para iOS
platform: iOS
page_order: 7
description: "Este artículo de referencia trata sobre el desencadenado personalizado de mensajes dentro de la aplicación para tu aplicación de iOS."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Desencadenado personalizado de mensajes dentro de la aplicación {#custom-in-app-message-triggering}

Por defecto, los mensajes dentro de la aplicación se desencadenan por tipos de eventos registrados por el SDK. Si quieres desencadenar mensajes dentro de la aplicación mediante eventos enviados por el servidor, también puedes conseguirlo.

Para habilitar esta característica, enviarías un push silencioso al dispositivo, lo que permitiría al dispositivo registrar un evento basado en el SDK. Este evento del SDK desencadenaría posteriormente el mensaje dentro de la aplicación dirigido al usuario.

## Paso 1: Manejar el push silencioso y los pares clave-valor {#step-1-handle-silent-push-and-key-value-pairs}

Añade el siguiente código dentro del método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [[Appboy sharedInstance] logCustomEvent:@"IAM Trigger" withProperties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
 };
```

{% endtab %}
{% tab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  NSLog("A push was received");
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    Appboy.sharedInstance()?.logCustomEvent("IAM Trigger", withProperties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endtab %}
{% endtabs %}

Cuando se reciba el push silencioso, se registrará un evento del SDK "desencadenante de mensaje dentro de la aplicación" en el perfil de usuario. Ten en cuenta que estos mensajes dentro de la aplicación solo se desencadenarán si se recibe el push silencioso mientras la aplicación está en primer plano.

## Paso 2: Crear una Campaign push {#step-2-create-a-push-campaign}

Crea una Campaign push silenciosa que se desencadene a través del evento enviado por el servidor. Para más detalles sobre cómo crear una Campaign push silenciosa, consulta las [notificaciones push silenciosas]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/silent_push_notifications).

![Una Campaign de mensajes dentro de la aplicación con entrega basada en acciones que se entregará a los usuarios que realicen el evento personalizado "server_event".]({% image_buster /assets/img_archive/iosServerSentPush.png %})

La Campaign push debe incluir extras de par clave-valor, que indiquen que esta Campaign push se envía para registrar un evento personalizado del SDK. Este evento se utilizará para desencadenar el mensaje dentro de la aplicación:

![Una Campaign de mensajes dentro de la aplicación con entrega basada en acciones que tiene dos pares clave-valor. "CAMPAIGN_NAME" establecido como "In-app message name example" e "IS_SERVER_EVENT" establecido en "true".]({% image_buster /assets/img_archive/iOSServerPush.png %})

El código del método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` comprueba si existe la clave `IS_SERVER_EVENT` y registrará un evento personalizado del SDK si está presente.

Puedes modificar el nombre del evento o las propiedades del evento enviando el valor deseado dentro de los extras del par clave-valor de la carga útil push. Al registrar el evento personalizado, estos extras se pueden utilizar como parámetro del nombre del evento o como una propiedad del evento.

## Paso 3: Crear una Campaign de mensajes dentro de la aplicación {#step-3-create-an-in-app-message-campaign}

Crea tu Campaign de mensajes dentro de la aplicación, visible para el usuario, desde el dashboard de Braze. Esta Campaign debe tener una entrega basada en acciones y desencadenarse desde el evento personalizado registrado en el método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`.

En el siguiente ejemplo, el mensaje específico dentro de la aplicación que se va a desencadenar se ha configurado enviando la propiedad del evento como parte del push silencioso inicial.

![Una Campaign de mensajes dentro de la aplicación con entrega basada en acciones que se entregará a los usuarios que realicen el evento personalizado "In-app message trigger" donde "campaign_name" es igual a "In-app message name example".]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

Debido a que se utiliza un mensaje push para registrar un evento personalizado del SDK, Braze necesitará almacenar un token de notificaciones push para cada usuario para habilitar esta solución. Tanto para iOS como para Android, Braze solo almacenará un token a partir del momento en que el usuario haya recibido el aviso push del sistema operativo. Antes de esto, el usuario no será localizable mediante push, y la solución anterior no será posible.