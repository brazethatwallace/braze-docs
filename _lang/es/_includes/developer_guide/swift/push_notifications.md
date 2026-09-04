## Límites de velocidad {#rate-limits}

Las notificaciones push tienen una tasa limitada, así que no temas enviar tantas como necesite tu aplicación. iOS y los servidores del servicio de notificaciones push de Apple (APN) controlarán la frecuencia con la que se entregan, y no te meterás en problemas por enviar demasiadas. Si tus notificaciones push están limitadas, podrían retrasarse hasta la próxima vez que el dispositivo envíe un paquete de mantenimiento de conexión o reciba otra notificación.

## Configurar las notificaciones push {#setting-up-push-notifications}

### Paso 1: Sube tu token de APNs {#step-1-upload-your-apns-token}

{% multi_lang_include developer_guide/swift/apns_token.md %}

### Paso 2: Habilitar las capacidades push {#step-2-enable-push-capabilities}

En Xcode, ve a la sección **Signing & Capabilities** del objetivo principal de la aplicación y añade la capacidad de notificaciones push.

![La sección "Signing & Capabilities" en un proyecto de Xcode.]({% image_buster /assets/img_archive/Enable_push_capabilities.png %})

### Paso 3: Configurar la gestión push {#step-3-set-up-push-handling}

Puedes utilizar el SDK de Swift para automatizar el procesamiento de las notificaciones remotas recibidas de Braze. Esta es la forma más sencilla de gestionar las notificaciones push y es el método de gestión recomendado.

{% tabs local %}
{% tab Automático %}
#### Paso 3.1: Habilitar la automatización en la propiedad push {#step-31-enable-automation-in-the-push-property}

Para habilitar la integración push automática, establece la propiedad `automation` de la configuración `push` en `true`:

{% subtabs %}
{% subtab Swift %}
```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}", endpoint: "{YOUR-BRAZE-API-ENDPOINT}")
configuration.push.automation = true
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"{YOUR-BRAZE-API-KEY}" endpoint:@"{YOUR-BRAZE-API-ENDPOINT}"];
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
```

{% endsubtab %}
{% endsubtabs %}

Esto indica al SDK que:
- Registre tu aplicación para notificaciones push en el sistema.
- Solicite la autorización/permiso de notificaciones push en la inicialización.
- Proporcione dinámicamente implementaciones para los métodos delegados del sistema relacionados con las notificaciones push.

{% alert note %}
Los pasos de automatización realizados por el SDK son compatibles con las integraciones preexistentes de gestión de notificaciones push en tu código. El SDK solo automatiza el procesamiento de las notificaciones remotas recibidas de Braze. Cualquier controlador del sistema implementado para procesar tus propias notificaciones remotas o las de otro SDK de terceros seguirá funcionando cuando `automation` esté habilitado.
{% endalert %}

{% alert warning %}
El SDK debe inicializarse en el hilo principal para habilitar la automatización de notificaciones push. La inicialización del SDK debe ocurrir antes de que la aplicación haya terminado de lanzarse o en la implementación de tu AppDelegate [`application(_:didFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application).
Si tu aplicación requiere configuración adicional antes de inicializar el SDK, consulta la página de documentación sobre [inicialización diferida]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift#step-2-set-up-delayed-initialization-optional).
{% endalert %}

#### Paso 3.2: Anular configuraciones individuales (opcional) {#step-32-override-individual-configurations-optional}

Para un control más granular, cada paso de automatización se puede habilitar o deshabilitar de forma individual:

{% subtabs %}
{% subtab Swift %}

```swift
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = true
configuration.push.automation.requestAuthorizationAtLaunch = false
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
configuration.push.automation.requestAuthorizationAtLaunch = NO;
```

{% endsubtab %}
{% endsubtabs %}

Consulta [`Braze.Configuration.Push.Automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.class) para ver todas las opciones disponibles y [`automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.property) para más información sobre el comportamiento de la automatización.
{% endtab %}

{% tab Manual %}
{% alert note %}
Si dependes de las notificaciones push para un comportamiento adicional específico de tu aplicación, es posible que aún puedas usar la integración push automática en lugar de la integración manual de notificaciones push. El método [`subscribeToUpdates(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(_:)) proporciona una forma de ser notificado de las notificaciones remotas procesadas por Braze.
{% endalert %}

#### Paso 3.1: Registrarse para notificaciones push con APNs {#step-31-register-for-push-notifications-with-apns}

Incluye el ejemplo de código apropiado dentro del [método delegado `application:didFinishLaunchingWithOptions:` de tu aplicación](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) para que los dispositivos de tus usuarios puedan registrarse con APNs. Asegúrate de llamar a todo el código de integración push en el hilo principal de tu aplicación.

Braze también proporciona categorías push predeterminadas para compatibilidad con los botones de acción para notificación push, que deben añadirse manualmente a tu código de registro push. Consulta [botones de acción para notificación push]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_customizing-push-categories) para conocer los pasos de integración adicionales.

Añade el siguiente código al método `application:didFinishLaunchingWithOptions:` del delegado de tu aplicación.

{% alert note %}
El siguiente ejemplo de código incluye la integración para la autenticación push provisional (líneas 5 y 6). Si no planeas utilizar la autorización provisional en tu aplicación, puedes eliminar las líneas de código que añaden `UNAuthorizationOptionProvisional` a las opciones de `requestAuthorization`.<br>Visita [opciones de notificación en iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options) para saber más sobre la autenticación push provisional.
{% endalert %}

{% subtabs %}
{% subtab Swift %}

```swift
application.registerForRemoteNotifications()
let center = UNUserNotificationCenter.current()
center.setNotificationCategories(Braze.Notifications.categories)
center.delegate = self
var options: UNAuthorizationOptions = [.alert, .sound, .badge]
if #available(iOS 12.0, *) {
  options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
}
center.requestAuthorization(options: options) { granted, error in
  print("Notification authorization, granted: \(granted), error: \(String(describing: error))")
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
[application registerForRemoteNotifications];
UNUserNotificationCenter *center = UNUserNotificationCenter.currentNotificationCenter;
[center setNotificationCategories:BRZNotifications.categories];
center.delegate = self;
UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
if (@available(iOS 12.0, *)) {
  options = options | UNAuthorizationOptionProvisional;
}
[center requestAuthorizationWithOptions:options
                      completionHandler:^(BOOL granted, NSError *_Nullable error) {
                        NSLog(@"Notification authorization, granted: %d, "
                              @"error: %@)",
                              granted, error);
}];
```

{% endsubtab %}
{% endsubtabs %}

{% alert warning %}
Debes asignar tu objeto delegado usando `center.delegate = self` de forma síncrona antes de que tu aplicación termine de lanzarse, preferiblemente en `application:didFinishLaunchingWithOptions:`. No hacerlo puede hacer que tu aplicación pierda notificaciones push entrantes. Visita la documentación de Apple sobre [`UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate) para saber más.
Si tu aplicación llama a `wipeData()` y posteriormente vuelve a habilitar el SDK de Braze en la misma ejecución de la aplicación, debes llamar a `registerForRemoteNotifications()` de nuevo para volver a llenar el token del dispositivo que usa el SDK.
{% endalert %}

#### Paso 3.2: Registrar los tokens de notificaciones push con Braze {#step-32-register-push-tokens-with-braze}

Una vez completado el registro de APNs, pasa el `deviceToken` resultante a Braze para habilitar las notificaciones push para el usuario.

{% subtabs %}
{% subtab Swift %}

Añade el siguiente código al método `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)` de tu aplicación:

```swift
AppDelegate.braze?.notifications.register(deviceToken: deviceToken)
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

Añade el siguiente código al método `application:didRegisterForRemoteNotificationsWithDeviceToken:` de tu aplicación:

```objc
[AppDelegate.braze.notifications registerDeviceToken:deviceToken];
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
El método delegado `application:didRegisterForRemoteNotificationsWithDeviceToken:` se llama cada vez después de que se invoque `application.registerForRemoteNotifications()`. <br><br>Si estás migrando a Braze desde otro servicio push y el dispositivo de tu usuario ya se ha registrado con APNs, este método recopilará tokens de los registros existentes la próxima vez que se llame al método, y los usuarios no tendrán que volver a dar su adhesión voluntaria a las notificaciones push.
{% endalert %}

#### Paso 3.3: Habilitar la gestión push {#step-33-enable-push-handling}

A continuación, pasa las notificaciones push recibidas a Braze. Este paso es necesario para registrar los análisis push y la gestión de enlaces. Asegúrate de llamar a todo el código de integración push en el hilo principal de tu aplicación.

##### Gestión push predeterminada {#default-push-handling}

{% subtabs %}
{% subtab Swift %}
Para habilitar la gestión push predeterminada de Braze, añade el siguiente código al método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` de tu aplicación:

```swift
if let braze = AppDelegate.braze, braze.notifications.handleBackgroundNotification(
  userInfo: userInfo,
  fetchCompletionHandler: completionHandler
) {
  return
}
completionHandler(.noData)
```

A continuación, añade lo siguiente al método `userNotificationCenter(_:didReceive:withCompletionHandler:)` de tu aplicación:

```swift
if let braze = AppDelegate.braze, braze.notifications.handleUserNotification(
  response: response,
  withCompletionHandler: completionHandler
) {
  return
}
completionHandler()
```
{% endsubtab %}

{% subtab OBJECTIVE-C %}
Para habilitar la gestión push predeterminada de Braze, añade el siguiente código al método `application:didReceiveRemoteNotification:fetchCompletionHandler:` de tu aplicación:

```objc
BOOL processedByBraze = AppDelegate.braze != nil && [AppDelegate.braze.notifications handleBackgroundNotificationWithUserInfo:userInfo
                                                                                                       fetchCompletionHandler:completionHandler];
if (processedByBraze) {
  return;
}

completionHandler(UIBackgroundFetchResultNoData);
```

A continuación, añade el siguiente código al método `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` de tu aplicación:

```objc
BOOL processedByBraze = AppDelegate.braze != nil && [AppDelegate.braze.notifications handleUserNotificationWithResponse:response
                                                                                                  withCompletionHandler:completionHandler];
if (processedByBraze) {
  return;
}

completionHandler();
```
{% endsubtab %}
{% endsubtabs %}

##### Gestión push en primer plano {#foreground-push-handling}

{% subtabs %}
{% subtab Swift %}
Para habilitar las notificaciones push en primer plano y permitir que Braze las reconozca cuando se reciben, implementa `UNUserNotificationCenter.userNotificationCenter(_:willPresent:withCompletionHandler:)`. Si un usuario toca tu notificación en primer plano, se llamará al delegado push `userNotificationCenter(_:didReceive:withCompletionHandler:)` y Braze registrará el evento de clic push.

```swift
func userNotificationCenter(
  _ center: UNUserNotificationCenter,
  willPresent notification: UNNotification,
  withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions
) -> Void) {
  if let braze = AppDelegate.braze {
    // Forward notification payload to Braze for processing.
    braze.notifications.handleForegroundNotification(notification: notification)
  }

  // Configure application's foreground notification display options.
  if #available(iOS 14.0, *) {
    completionHandler([.list, .banner])
  } else {
    completionHandler([.alert])
  }
}
```
{% endsubtab %}

{% subtab OBJECTIVE-C %}
Para habilitar las notificaciones push en primer plano y permitir que Braze las reconozca cuando se reciben, implementa `userNotificationCenter:willPresentNotification:withCompletionHandler:`. Si un usuario toca tu notificación en primer plano, se llamará al delegado push `userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` y Braze registrará el evento de clic push.

```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
       willPresentNotification:(UNNotification *)notification
         withCompletionHandler:(void (^)(UNNotificationPresentationOptions options))completionHandler {
  if (AppDelegate.braze != nil) {
    // Forward notification payload to Braze for processing.
    [AppDelegate.braze.notifications handleForegroundNotificationWithNotification:notification];
  }

  // Configure application's foreground notification display options.
  if (@available(iOS 14.0, *)) {
    completionHandler(UNNotificationPresentationOptionList | UNNotificationPresentationOptionBanner);
  } else {
    completionHandler(UNNotificationPresentationOptionAlert);
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Prueba de notificaciones {#push-testing}

Si quieres probar las notificaciones dentro de la aplicación y las notificaciones push a través de la línea de comandos, puedes enviar una única notificación a través del terminal mediante CURL y la [API de mensajería]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages). Tendrás que sustituir los siguientes campos por los valores correctos para tu caso de prueba:

- `YOUR_API_KEY` - disponible en **Configuración** > **Claves de API**.
- `YOUR_EXTERNAL_USER_ID` - disponible en la página **Buscar usuarios**. Para más información, consulta [asignar ID de usuario]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids#assigning-a-user-id).
- `YOUR_KEY1` (opcional)
- `YOUR_VALUE1` (opcional)

En el siguiente ejemplo, se utiliza la instancia `US-01`. Si no estás en esta instancia, consulta nuestra [documentación de la API]({{site.baseurl}}/api/basics) para ver a qué endpoint debes hacer solicitudes.

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert":"Test push",
      "extra": {
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

## Suscribirse a las actualizaciones de notificaciones push {#subscribing-to-push-notifications-updates}

Para acceder a las cargas útiles de notificaciones push procesadas por Braze, utiliza el método [`Braze.Notifications.subscribeToUpdates(payloadTypes:_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(payloadtypes:_:)/).

Puedes utilizar el parámetro `payloadTypes` para especificar si deseas suscribirte a notificaciones que involucren eventos de apertura push, eventos de recepción push, o ambos.

{% tabs %}
{% tab Swift %}

```swift
// This subscription is maintained through a Braze cancellable, which will observe for changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.notifications.subscribeToUpdates(payloadTypes: [.open, .received]) { payload in
  print("Braze processed notification with title '\(payload.title)' and body '\(payload.body)'")
}
```

{% alert important %}
Ten en cuenta que los eventos de recepción push solo se desencadenarán para las notificaciones en primer plano y las notificaciones en segundo plano con `content-available`. No se desencadenarán para las notificaciones recibidas mientras la aplicación está terminada ni para las notificaciones en segundo plano sin el campo `content-available`.
{% endalert %}

{% endtab %}

{% tab OBJECTIVE-C %}

```objc
NSInteger filtersValue = BRZNotificationsPayloadTypeFilter.opened.rawValue | BRZNotificationsPayloadTypeFilter.received.rawValue;
BRZNotificationsPayloadTypeFilter *filters = [[BRZNotificationsPayloadTypeFilter alloc] initWithRawValue: filtersValue];
BRZCancellable *cancellable = [notifications subscribeToUpdatesWithPayloadTypes:filters update:^(BRZNotificationsPayload * _Nonnull payload) {
  NSLog(@"Braze processed notification with title '%@' and body '%@'", payload.title, payload.body);
}];
```

{% alert important %}
Ten en cuenta que los eventos de recepción push solo se desencadenarán para las notificaciones en primer plano y las notificaciones en segundo plano con `content-available`. No se desencadenarán para las notificaciones recibidas mientras la aplicación está terminada ni para las notificaciones en segundo plano sin el campo `content-available`.
{% endalert %}

{% endtab %}

{% endtabs %}
{% alert note %}
Cuando utilizas la integración push automática, `subscribeToUpdates(_:)` es la única forma de recibir avisos sobre las notificaciones remotas procesadas por Braze. Los métodos del sistema `UIAppDelegate` y `UNUserNotificationCenterDelegate` no se invocan cuando Braze procesa automáticamente la notificación.
{% endalert %}

{% alert tip %}
Crea tu suscripción a notificaciones push en `application(_:didFinishLaunchingWithOptions:)` para asegurarte de que tu suscripción se desencadene después de que un usuario final toque una notificación mientras tu aplicación se encuentra en estado terminado.
{% endalert %}

## Gestionar las notificaciones en primer plano {#handling-foreground-notifications}

De forma predeterminada, cuando llega una notificación push mientras tu aplicación está en primer plano, iOS no la muestra automáticamente. Para mostrar las notificaciones push en primer plano y rastrearlas con los análisis de Braze, llama al método `handleForegroundNotification(notification:)` dentro de tu implementación de `UNUserNotificationCenterDelegate.userNotificationCenter(_:willPresent:withCompletionHandler:)`.

### Cómo funciona {#how-it-works}

Cuando llamas a `handleForegroundNotification(notification:)`, Braze procesa la carga útil de la notificación para registrar los análisis y gestionar cualquier vínculo profundo o acción de botón. El comportamiento real de visualización se controla mediante las `UNNotificationPresentationOptions` que pasas al controlador de finalización.

```swift
import BrazeKit
import UserNotifications

extension AppDelegate: UNUserNotificationCenterDelegate {
  func userNotificationCenter(
    _ center: UNUserNotificationCenter,
    willPresent notification: UNNotification,
    withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void
  ) {
    // Let Braze process the notification payload
    if let braze = AppDelegate.braze {
      braze.notifications.handleForegroundNotification(notification: notification)
    }

    // Control how the notification appears in the foreground
    if #available(iOS 14.0, *) {
      completionHandler([.banner, .list, .sound])
    } else {
      completionHandler([.alert, .sound])
    }
  }
}
```

Para ver un ejemplo completo, consulta el [ejemplo de integración manual de notificaciones push](https://github.com/braze-inc/braze-swift-sdk/blob/e31907eaa0dbd151dc2e6826de66cc494242ba60/Examples/Swift/Sources/PushNotifications-Manual/AppDelegate.swift#L1-L120) en el repositorio del SDK Swift de Braze.

## Push primers {#push-primers}

Las campañas de push primer animan a tus usuarios a habilitar las notificaciones push de tu aplicación en sus dispositivos. Esto puede hacerse sin necesidad de personalizar el SDK utilizando nuestro [push primer sin código]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages).

## Gestión dinámica de la pasarela de APNs {#dynamic-apns-gateway-management}

La gestión dinámica de la pasarela del servicio de notificaciones push de Apple (APNs) mejora la fiabilidad y la eficiencia de las notificaciones push en iOS al detectar automáticamente el entorno correcto de APNs. Anteriormente, tenías que seleccionar manualmente los entornos de APNs (desarrollo o producción) para tus notificaciones push, lo que a veces provocaba configuraciones de pasarela incorrectas, fallos en la entrega y errores `BadDeviceToken`.

Con la gestión dinámica de la pasarela de APNs, dispondrás de:

- **Fiabilidad mejorada:** las notificaciones siempre se entregan al entorno APNs correcto, lo que reduce las entregas fallidas.
- **Configuración simplificada:** ya no necesitas gestionar manualmente la configuración de la pasarela de APNs.
- **Resiliencia ante errores:** los valores de pasarela no válidos o ausentes se gestionan correctamente, proporcionando un servicio ininterrumpido.

### Requisitos previos {#prerequisites}

Braze es compatible con la gestión dinámica de la pasarela de APNs para notificaciones push en iOS con el siguiente requisito de versión del SDK:

{% sdk_min_versions swift:10.0.0 %}

### Cómo funciona

Cuando una aplicación iOS se integra con el SDK Swift de Braze, envía datos relacionados con el dispositivo, incluido [`aps-environment`](https://developer.apple.com/documentation/bundleresources/entitlements/aps-environment), a la API del SDK de Braze, si está disponible. El valor `apns_gateway` indica si la aplicación está utilizando el entorno APNs de desarrollo (`dev`) o de producción (`prod`).

Braze también almacena el valor de pasarela notificado para cada dispositivo. Si se recibe un nuevo valor de pasarela válido, Braze actualiza automáticamente el valor almacenado.

Cuando Braze envía una notificación push:

- Si se ha almacenado un valor de pasarela válido (dev o prod) para el dispositivo, Braze lo utiliza para determinar el entorno APNs correcto.
- Si no se ha almacenado ningún valor de pasarela, Braze utiliza de forma predeterminada el entorno APNs configurado en la página **Configuración de la aplicación**.

### Preguntas frecuentes {#frequently-asked-questions}

#### ¿Por qué se introdujo esta característica? {#why-was-this-feature-introduced}

Con la gestión dinámica de la pasarela de APNs, el entorno correcto se selecciona automáticamente. Anteriormente, tenías que configurar manualmente la pasarela de APNs, lo que podía provocar errores `BadDeviceToken`, invalidación de tokens y posibles problemas de límite de velocidad de APNs.

#### ¿Cómo afecta esto al rendimiento de la entrega push? {#how-does-this-impact-push-delivery-performance}

Esta característica mejora las tasas de entrega al enrutar siempre los tokens de notificaciones push al entorno APNs correcto, evitando fallos causados por pasarelas mal configuradas.

#### ¿Puedo desactivar esta característica? {#can-i-disable-this-feature}

La gestión dinámica de la pasarela de APNs está activada de forma predeterminada y proporciona mejoras de fiabilidad. Si tienes casos de uso específicos que requieran la selección manual de la pasarela, ponte en contacto con [soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support).