## Límites de velocidad {#rate-limits}

Las notificaciones push tienen un límite de velocidad, así que no tengas miedo de enviar tantas como necesite tu aplicación. iOS y los servidores del servicio de notificaciones push de Apple (APN) controlarán la frecuencia con la que se entregan, y no te meterás en problemas por enviar demasiadas. Si tus notificaciones push están limitadas, podrían retrasarse hasta la próxima vez que el dispositivo envíe un paquete de mantenimiento de conexión o reciba otra notificación.

## Configuración de notificaciones push {#setting-up-push-notifications}

### Paso 1: Sube tu token de APN {#step-1-upload-your-apns-token}

{% multi_lang_include developer_guide/swift/apns_token.md %}

### Paso 2: Habilitar las capacidades push {#step-2-enable-push-capabilities}

En Xcode, ve a la sección **Signing & Capabilities** del objetivo principal de la aplicación y añade la capacidad de notificaciones push.

![La sección "Signing & Capabilities" en un proyecto Xcode.]({% image_buster /assets/img_archive/Enable_push_capabilities.png %})

### Paso 3: Configurar la gestión de notificaciones push {#step-3-set-up-push-handling}

Puedes utilizar el SDK de Swift para automatizar el procesamiento de las notificaciones remotas recibidas de Braze. Esta es la forma más sencilla de gestionar las notificaciones push y es el método de gestión recomendado.

{% tabs local %}
{% tab Automatic %}
#### Paso 3.1: Habilita la automatización en la propiedad push {#step-31-enable-automation-in-the-push-property}

Para habilitar la integración push automática, establece la propiedad `automation` de la configuración de `push` en `true`:

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

Esto indica al SDK lo siguiente:
- Registrar tu aplicación para notificaciones push en el sistema.
- Solicitar la autorización/permiso de notificación push en la inicialización.
- Proporcionar dinámicamente implementaciones para los métodos de delegado del sistema relacionados con las notificaciones push.

{% alert note %}
Los pasos de automatización realizados por el SDK son compatibles con las integraciones de gestión de notificaciones push preexistentes en tu código base. El SDK solo automatiza el procesamiento de la notificación remota recibida de Braze. Cualquier controlador del sistema implementado para procesar tus propias notificaciones remotas o las de otro SDK de terceros seguirá funcionando cuando `automation` esté habilitado.
{% endalert %}

{% alert warning %}
El SDK debe inicializarse en el hilo principal para habilitar la automatización de las notificaciones push. La inicialización del SDK debe producirse antes de que la aplicación haya terminado de lanzarse o en tu implementación de AppDelegate [`application(_:didFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application).
Si tu aplicación requiere una configuración adicional antes de inicializar el SDK, consulta la página de documentación [Inicialización retardada]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=swift).
{% endalert %}

#### Paso 3.2: Anular configuraciones individuales (opcional) {#step-32-override-individual-configurations-optional}

Para un control más granular, cada paso de la automatización puede habilitarse o deshabilitarse individualmente:

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

Consulta [`Braze.Configuration.Push.Automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.class) para conocer todas las opciones disponibles y [`automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.property) para más información sobre el comportamiento de la automatización.
{% endtab %}

{% tab Manual %}
{% alert note %}
Si dependes de las notificaciones push para un comportamiento adicional específico de tu aplicación, aún puedes utilizar la integración push automática en lugar de la integración manual de notificaciones push. El método [`subscribeToUpdates(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(_:)) permite recibir notificaciones de las notificaciones remotas procesadas por Braze.
{% endalert %}

#### Paso 3.1: Registro para notificaciones push con APNs {#step-31-register-for-push-notifications-with-apns}

Incluye el ejemplo de código apropiado en el [método delegado `application:didFinishLaunchingWithOptions:`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) de tu aplicación para que los dispositivos de tus usuarios puedan registrarse con APNs. Asegúrate de que llamas a todo el código de integración push en el hilo principal de tu aplicación.

Braze también proporciona categorías push predeterminadas para el soporte del botón de acción para notificación push, que deben añadirse manualmente a tu código de registro push. Consulta los [botones de acción para notificación push]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_customizing-push-categories) para conocer los pasos adicionales de la integración.

Añade el siguiente código al método `application:didFinishLaunchingWithOptions:` del delegado de tu aplicación.

{% alert note %}
El siguiente ejemplo de código incluye la integración para la autenticación push provisional (líneas 5 y 6). Si no piensas utilizar la autorización provisional en tu aplicación, puedes eliminar las líneas de código que añaden `UNAuthorizationOptionProvisional` a las opciones de `requestAuthorization`.<br>Visita [las opciones de notificación de iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/) para saber más sobre la autenticación push provisional.
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
Debes asignar tu objeto delegado utilizando `center.delegate = self` de forma sincrónica antes de que tu aplicación termine de lanzarse, preferiblemente en `application:didFinishLaunchingWithOptions:`. Si no lo haces, puede que tu aplicación no reciba notificaciones push entrantes. Visita la documentación de Apple [`UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate) para obtener más información.
Si tu aplicación llama a `wipeData()` y posteriormente vuelve a habilitar el SDK de Braze en la misma ejecución de la aplicación, debes llamar a `registerForRemoteNotifications()` de nuevo para volver a rellenar el token de dispositivo utilizado por el SDK.
{% endalert %}

#### Paso 3.2: Registrar tokens de notificaciones push con Braze {#step-32-register-push-tokens-with-braze}

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
Se llama al método delegado `application:didRegisterForRemoteNotificationsWithDeviceToken:` cada vez que se llama a `application.registerForRemoteNotifications()`. <br><br>Si estás migrando a Braze desde otro servicio push y el dispositivo de tu usuario ya se ha registrado con APNs, este método recogerá tokens de los registros existentes la próxima vez que se llame al método, y los usuarios no tendrán que volver a adherirse a las notificaciones push.
{% endalert %}

#### Paso 3.3: Habilitar la gestión push {#step-33-enable-push-handling}

A continuación, pasa las notificaciones push recibidas a Braze. Este paso es necesario para registrar los análisis push y la gestión de enlaces. Asegúrate de que llamas a todo el código de integración push en el hilo principal de tu aplicación.

##### Gestión predeterminada de notificaciones push {#default-push-handling}

{% subtabs %}
{% subtab Swift %}
Para habilitar la gestión predeterminada de notificaciones push de Braze, añade el siguiente código al método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` de tu aplicación:

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
Para habilitar la gestión predeterminada de notificaciones push de Braze, añade el siguiente código al método `application:didReceiveRemoteNotification:fetchCompletionHandler:` de tu aplicación:

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

##### Gestión de notificaciones push en primer plano {#foreground-push-handling}

{% subtabs %}
{% subtab Swift %}
Para habilitar las notificaciones push en primer plano y permitir que Braze las reconozca cuando se reciban, implementa `UNUserNotificationCenter.userNotificationCenter(_:willPresent:withCompletionHandler:)`. Si un usuario toca tu notificación en primer plano, se llamará al delegado push `userNotificationCenter(_:didReceive:withCompletionHandler:)` y Braze registrará el evento de clic push.

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
Para habilitar las notificaciones push en primer plano y permitir que Braze las reconozca cuando se reciban, implementa `userNotificationCenter:willPresentNotification:withCompletionHandler:`. Si un usuario toca tu notificación en primer plano, se llamará al delegado push `userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` y Braze registrará el evento de clic push.

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

Si quieres probar las notificaciones dentro de la aplicación y las notificaciones push a través de la línea de comandos, puedes enviar una única notificación a través del terminal mediante CURL y la [API de mensajería]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/). Tendrás que sustituir los siguientes campos por los valores correctos para tu caso de prueba:

- `YOUR_API_KEY` - disponible en **Configuración** > **Claves de API**.
- `YOUR_EXTERNAL_USER_ID` - disponible en la página **Buscar usuarios**. Para más información, consulta [asignar ID de usuario]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#assigning-a-user-id).
- `YOUR_KEY1` (opcional)
- `YOUR_VALUE1` (opcional)

En el siguiente ejemplo, se utiliza la instancia `US-01`. Si no estás en esta instancia, consulta nuestra [documentación de la API]({{site.baseurl}}/api/basics/) para ver a qué punto de conexión debes hacer solicitudes.

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

Para acceder a las cargas útiles de notificación push procesadas por Braze, utiliza el método [`Braze.Notifications.subscribeToUpdates(payloadTypes:_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(payloadtypes:_:)/).

Puedes utilizar el parámetro `payloadTypes` para especificar si quieres suscribirte a notificaciones de eventos push abiertos, eventos push recibidos o ambos.

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
Ten en cuenta que los eventos push recibidos solo se desencadenarán para las notificaciones en primer plano y las notificaciones en segundo plano con `content-available`. No se desencadenarán para las notificaciones recibidas mientras la aplicación está terminada ni para las notificaciones en segundo plano sin el campo `content-available`.
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
Ten en cuenta que los eventos push recibidos solo se desencadenarán para las notificaciones en primer plano y las notificaciones en segundo plano con `content-available`. No se desencadenarán para las notificaciones recibidas mientras la aplicación está terminada ni para las notificaciones en segundo plano sin el campo `content-available`.
{% endalert %}

{% endtab %}

{% endtabs %}
{% alert note %}
Cuando utilices la integración push automática, `subscribeToUpdates(_:)` es la única forma de recibir notificaciones remotas procesadas por Braze. Los métodos del sistema `UIAppDelegate` y `UNUserNotificationCenterDelegate` no se llaman cuando la notificación es procesada automáticamente por Braze.
{% endalert %}

{% alert tip %}
Crea tu suscripción a notificaciones push en `application(_:didFinishLaunchingWithOptions:)` para asegurarte de que tu suscripción se desencadena cuando un usuario final toca una notificación mientras tu aplicación está en estado terminado.
{% endalert %}

## Gestión de notificaciones en primer plano {#handling-foreground-notifications}

De forma predeterminada, cuando llega una notificación push mientras tu aplicación está en primer plano, iOS no la muestra automáticamente. Para mostrar notificaciones push en primer plano y realizar su seguimiento con los análisis de Braze, llama al método `handleForegroundNotification(notification:)` dentro de tu implementación de `UNUserNotificationCenterDelegate.userNotificationCenter(_:willPresent:withCompletionHandler:)`.

### Cómo funciona {#how-it-works}

Cuando llamas a `handleForegroundNotification(notification:)`, Braze procesa la carga útil de la notificación para registrar los análisis y gestionar cualquier vínculo profundo o acción de botón. El comportamiento real de la visualización está controlado por las `UNNotificationPresentationOptions` que pasas al controlador de finalización.

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

Para ver un ejemplo completo, consulta la [muestra de integración manual de notificaciones push](https://github.com/braze-inc/braze-swift-sdk/blob/e31907eaa0dbd151dc2e6826de66cc494242ba60/Examples/Swift/Sources/PushNotifications-Manual/AppDelegate.swift#L1-L120) en el repositorio del SDK Swift de Braze.

## Push primers {#push-primers}

Las campañas de push primer animan a tus usuarios a habilitar las notificaciones push de tu aplicación en sus dispositivos. Esto puede hacerse sin necesidad de personalizar el SDK utilizando nuestro [push primer sin código]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

## Gestión dinámica de la puerta de enlace de APNs {#dynamic-apns-gateway-management}

La gestión dinámica de la puerta de enlace del servicio de notificaciones push de Apple (APNs) mejora la fiabilidad y la eficiencia de las notificaciones push de iOS al detectar automáticamente el entorno de APNs correcto. Anteriormente, debías seleccionar manualmente los entornos de APNs (desarrollo o producción) para tus notificaciones push, lo que a veces provocaba configuraciones de puerta de enlace incorrectas, fallos en la entrega y errores `BadDeviceToken`.

Con la gestión dinámica de la puerta de enlace de APNs, tendrás:

- **Mayor fiabilidad:** Las notificaciones siempre se entregan al entorno de APNs correcto, lo que reduce los fallos en la entrega.
- **Configuración simplificada:** Ya no es necesario administrar manualmente la configuración de la puerta de enlace de APNs.
- **Resistencia a errores:** Los valores de puerta de enlace no válidos o faltantes se gestionan correctamente, lo que garantiza un servicio ininterrumpido.

### Requisitos previos {#prerequisites}

Braze admite la gestión dinámica de puertas de enlace de APNs para notificaciones push en iOS con los siguientes requisitos de versión del SDK:

{% sdk_min_versions swift:10.0.0 %}

### Cómo funciona {#how-it-works-1}

Cuando una aplicación iOS se integra con el SDK Swift de Braze, envía datos relacionados con el dispositivo, incluido [`aps-environment`](https://developer.apple.com/documentation/bundleresources/entitlements/aps-environment), a la API del SDK de Braze, si está disponible. El valor `apns_gateway` indica si la aplicación utiliza el entorno de APNs de desarrollo (`dev`) o de producción (`prod`).

Braze también almacena el valor de puerta de enlace reportado para cada dispositivo. Si se recibe un nuevo valor de puerta de enlace válido, Braze actualiza automáticamente el valor almacenado.

Cuando Braze envía una notificación push:

- Si se almacena un valor de puerta de enlace válido (dev o prod) para el dispositivo, Braze lo utiliza para determinar el entorno de APNs correcto.
- Si no se almacena ningún valor de puerta de enlace, Braze utiliza de forma predeterminada el entorno de APNs configurado en la página **Configuración de la aplicación**.

### Preguntas frecuentes {#frequently-asked-questions}

#### ¿Por qué se introdujo esta característica? {#why-was-this-feature-introduced}

Con la gestión dinámica de la puerta de enlace de APNs, se selecciona automáticamente el entorno adecuado. Anteriormente, era necesario configurar manualmente la puerta de enlace de APNs, lo que podía provocar errores `BadDeviceToken`, la invalidación de tokens y posibles problemas de límite de velocidad de APNs.

#### ¿Cómo afecta esto al rendimiento de la entrega push? {#how-does-this-impact-push-delivery-performance}

Esta característica mejora las tasas de entrega al dirigir siempre los tokens de notificaciones push al entorno de APNs correcto, evitando fallos causados por puertas de enlace mal configuradas.

#### ¿Puedo desactivar esta característica? {#can-i-disable-this-feature}

La gestión dinámica de puertas de enlace de APNs está activada de forma predeterminada y proporciona mejoras en la fiabilidad. Si tienes casos de uso específicos que requieren la selección manual de la puerta de enlace, ponte en contacto con [soporte de Braze]({{site.baseurl}}/user_guide/administrative/access_braze/support/).