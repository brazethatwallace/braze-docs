---
nav_title: Integración
article_title: Integración push para iOS
platform: iOS
page_order: 0
description: "Este artículo de referencia explica cómo integrar notificaciones push en tu aplicación iOS."
channel:
  - push
search_rank: 5

local_redirect:
  ios-10-rich-notifications: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/'
local_redirect:
  creating-a-service-extension: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#creating-a-service-extension'
local_redirect:
  setting-up-the-service-extension: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#setting-up-the-service-extension'
local_redirect:
  creating-a-rich-notification-in-your-dashboard: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#creating-a-rich-notification-in-your-dashboard'
local_redirect:
  push-action-buttons-integration: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/'
local_redirect:
  step-1-adding-braze-default-push-categories: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/#step-1-adding-braze-default-push-categories'
local_redirect:
  step-2-enable-interactive-push-handling: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/#step-2-enable-interactive-push-handling'

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Integración push {#push-integration}

## Paso 1: Sube tu token de APN {#step-1-upload-your-apns-token}

{% multi_lang_include developer_guide/swift/apns_token.md %}

## Paso 2: Habilitar las capacidades de push {#step-2-enable-push-capabilities}

En la configuración de tu proyecto, asegúrate de que en la pestaña **Capabilities**, la capacidad **Push Notifications** esté activada.

![En la configuración de tu proyecto, asegúrate de que en la pestaña Capabilities, la capacidad Push Notifications esté activada.]({% image_buster /assets/img_archive/Enable_push_capabilities.png %})

Si tienes certificados push de desarrollo y producción separados, asegúrate de desmarcar la casilla **Automatically manage signing** en la pestaña **General**. Esto te permitirá elegir diferentes perfiles de aprovisionamiento para cada configuración de compilación, ya que la función de firma automática de código de Xcode solo realiza la firma de desarrollo.

![Configuración del proyecto Xcode mostrando la pestaña "General". En esta pestaña, la opción "Automatically manage signing" está desmarcada.]({% image_buster /assets/img_archive/xcode8_auto_signing.png %})

## Paso 3: Registrarse para notificaciones push {#step-3-register-for-push-notifications}

El ejemplo de código apropiado debe incluirse dentro del método delegado `application:didFinishLaunchingWithOptions:` de tu aplicación para que los dispositivos de tus usuarios se registren con APN. Asegúrate de llamar a todo el código de integración push en el hilo principal de tu aplicación.

Braze también proporciona categorías push predeterminadas para la compatibilidad con botones de acción para notificación push, que deben añadirse manualmente a tu código de registro push. Consulta [botones de acción para notificación push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/action_buttons) para conocer los pasos de integración adicionales.

{% alert warning %}
Si has implementado un aviso push personalizado como se describe en nuestras [mejores prácticas de push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/troubleshooting), asegúrate de llamar al siguiente código **cada vez que se ejecute la aplicación** después de que concedan permisos push a tu aplicación. **Las aplicaciones necesitan volver a registrarse con APN, ya que [los tokens de dispositivo pueden cambiar de forma arbitraria](https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/BackgroundExecution/BackgroundExecution.html).**
{% endalert %}

### Uso del framework UserNotification (iOS 10+) {#using-usernotification-framework-ios-10}

Si estás utilizando el framework `UserNotifications` (recomendado) introducido en iOS 10, añade el siguiente código al método `application:didFinishLaunchingWithOptions:` del delegado de tu aplicación.

{% alert important %}
El siguiente ejemplo de código incluye la integración para la autenticación push provisional (líneas 5 y 6). Si no tienes previsto usar la autorización provisional en tu aplicación, puedes eliminar las líneas de código que añaden `UNAuthorizationOptionProvisional` a las opciones de `requestAuthorization`.<br>Visita [Opciones de notificación de iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options) para obtener más información sobre la autenticación push provisional.
{% endalert %}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
if (floor(NSFoundationVersionNumber) > NSFoundationVersionNumber_iOS_9_x_Max) {
  UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
  center.delegate = self;
  UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
  if (@available(iOS 12.0, *)) {
  options = options | UNAuthorizationOptionProvisional;
  }
  [center requestAuthorizationWithOptions:options
                        completionHandler:^(BOOL granted, NSError * _Nullable error) {
                          [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];
  [[UIApplication sharedApplication] registerForRemoteNotifications];
} else {
  UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:nil];
  [[UIApplication sharedApplication] registerForRemoteNotifications];
  [[UIApplication sharedApplication] registerUserNotificationSettings:settings];
}
```

{% endtab %}
{% tab swift %}

```swift
if #available(iOS 10, *) {
  let center = UNUserNotificationCenter.current()
  center.delegate = self as? UNUserNotificationCenterDelegate
  var options: UNAuthorizationOptions = [.alert, .sound, .badge]
  if #available(iOS 12.0, *) {
    options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
  }
  center.requestAuthorization(options: options) { (granted, error) in
    Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
  }
  UIApplication.shared.registerForRemoteNotifications()
} else {
  let types : UIUserNotificationType = [.alert, .badge, .sound]
  let setting : UIUserNotificationSettings = UIUserNotificationSettings(types:types, categories:nil)
  UIApplication.shared.registerUserNotificationSettings(setting)
  UIApplication.shared.registerForRemoteNotifications()
}
```

{% endtab %}
{% endtabs %}


{% alert warning %}
Debes asignar tu objeto delegado usando `center.delegate = self` de forma síncrona antes de que tu aplicación termine de iniciarse, preferiblemente en `application:didFinishLaunchingWithOptions:`. No hacerlo puede provocar que tu aplicación pierda notificaciones push entrantes. Visita la documentación de Apple sobre [`UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate) para obtener más información.
{% endalert %}

### Sin el framework UserNotifications {#without-usernotifications-framework}

Si no estás utilizando el framework `UserNotifications`, añade el siguiente código al método `application:didFinishLaunchingWithOptions:` del delegado de tu aplicación:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:nil];
[[UIApplication sharedApplication] registerForRemoteNotifications];
[[UIApplication sharedApplication] registerUserNotificationSettings:settings];
```

{% endtab %}
{% tab swift %}

```swift
let types : UIUserNotificationType = UIUserNotificationType.Badge | UIUserNotificationType.Sound | UIUserNotificationType.Alert
var setting : UIUserNotificationSettings = UIUserNotificationSettings(forTypes: types, categories: nil)
UIApplication.shared.registerUserNotificationSettings(setting)
UIApplication.shared.registerForRemoteNotifications()
```

{% endtab %}
{% endtabs %}

## Paso 4: Registrar tokens de notificaciones push con Braze {#step-4-register-push-tokens-with-braze}

Una vez que se complete el registro en APN, se debe modificar el siguiente método para pasar el `deviceToken` resultante a Braze, de modo que el usuario quede habilitado para recibir notificaciones push:

{% tabs %}
{% tab OBJECTIVE-C %}

Añade el siguiente código a tu método `application:didRegisterForRemoteNotificationsWithDeviceToken:`:

```objc
[[Appboy sharedInstance] registerDeviceToken:deviceToken];
```

{% endtab %}
{% tab swift %}

Añade el siguiente código al método `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)` de tu aplicación:

```swift
Appboy.sharedInstance()?.registerDeviceToken(deviceToken)
```

{% endtab %}
{% endtabs %}

{% alert important %}
El método delegado `application:didRegisterForRemoteNotificationsWithDeviceToken:` se llama cada vez que se ejecuta `[[UIApplication sharedApplication] registerForRemoteNotifications]`. Si estás migrando a Braze desde otro servicio push y el dispositivo de tu usuario ya se ha registrado con APN, este método recopilará los tokens de los registros existentes la próxima vez que se llame, y los usuarios no tendrán que volver a dar su adhesión voluntaria a las notificaciones push.
{% endalert %}

## Paso 5: Habilitar la gestión de push {#step-5-enable-push-handling}

El siguiente código pasa las notificaciones push recibidas a Braze y es necesario para registrar los análisis de push y la gestión de enlaces. Asegúrate de llamar a todo el código de integración push en el hilo principal de tu aplicación.

### iOS 10+

Al compilar con iOS 10+, te recomendamos que integres el framework `UserNotifications` y hagas lo siguiente:

{% tabs %}
{% tab OBJECTIVE-C %}

Añade el siguiente código al método `application:didReceiveRemoteNotification:fetchCompletionHandler:` de tu aplicación:

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo
                      fetchCompletionHandler:completionHandler];
```

A continuación, añade el siguiente código al método `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` de tu aplicación:

```objc
[[Appboy sharedInstance] userNotificationCenter:center
                 didReceiveNotificationResponse:response
                          withCompletionHandler:completionHandler];
```

**Gestión de push en primer plano**

Para mostrar una notificación push mientras la aplicación está en primer plano, implementa `userNotificationCenter:willPresentNotification:withCompletionHandler:`:

```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
       willPresentNotification:(UNNotification *)notification
         withCompletionHandler:(void (^)(UNNotificationPresentationOptions options))completionHandler {
  if (@available(iOS 14.0, *)) {
    completionHandler(UNNotificationPresentationOptionList | UNNotificationPresentationOptionBanner);
  } else {
    completionHandler(UNNotificationPresentationOptionAlert);
  }
}
```

Si se hace clic en la notificación en primer plano, se llamará al delegado de push de iOS 10 `userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:`, y Braze registrará un evento de clic de push.

{% endtab %}
{% tab swift %}

Añade el siguiente código al método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` de tu aplicación:

```swift
Appboy.sharedInstance()?.register(application,
                                            didReceiveRemoteNotification: userInfo,
                                            fetchCompletionHandler: completionHandler)
```

A continuación, añade el siguiente código al método `userNotificationCenter(_:didReceive:withCompletionHandler:)` de tu aplicación:

```swift
Appboy.sharedInstance()?.userNotificationCenter(center,
                                               didReceive: response,
                                               withCompletionHandler: completionHandler)
```

**Gestión de push en primer plano**

Para mostrar una notificación push mientras la aplicación está en primer plano, implementa `userNotificationCenter(_:willPresent:withCompletionHandler:)`:

```swift
func userNotificationCenter(_ center: UNUserNotificationCenter,
                              willPresent notification: UNNotification,
                              withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {
  if #available(iOS 14.0, *) {
    completionHandler([.list, .banner]);
  } else {
    completionHandler([.alert]);
  }
}
```

Si se hace clic en la notificación en primer plano, se llamará al delegado de push de iOS 10 `userNotificationCenter(_:didReceive:withCompletionHandler:)`, y Braze registrará un evento de clic de push.

{% endtab %}
{% endtabs %}

### Anterior a iOS 10 {#pre-ios-10}

iOS 10 actualizó el comportamiento de modo que ya no llama a `application:didReceiveRemoteNotification:fetchCompletionHandler:` cuando se hace clic en un push. Por esta razón, si no actualizas a compilar con iOS 10+ y usas el framework `UserNotifications`, tienes que llamar a Braze desde ambos delegados de estilo antiguo, lo que supone un cambio respecto a nuestra integración anterior.

Para aplicaciones que compilen con SDK or kit de desarrollo de software < iOS 10, utiliza las siguientes instrucciones:

{% tabs %}
{% tab OBJECTIVE-C %}

Para habilitar el seguimiento de aperturas en las notificaciones push, añade el siguiente código al método `application:didReceiveRemoteNotification:fetchCompletionHandler:` de tu aplicación:

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo
                      fetchCompletionHandler:completionHandler];
```

Para admitir los análisis de push en iOS 10, también debes añadir el siguiente código al método delegado `application:didReceiveRemoteNotification:` de tu aplicación:

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo];
```

{% endtab %}
{% tab swift %}

Para habilitar el seguimiento de aperturas en las notificaciones push, añade el siguiente código al método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` de tu aplicación:

```swift
Appboy.sharedInstance()?.register(application,
  didReceiveRemoteNotification: userInfo,
  fetchCompletionHandler: completionHandler)
```

Para admitir los análisis de push en iOS 10, también debes añadir el siguiente código al método delegado `application(_:didReceiveRemoteNotification:)` de tu aplicación:

```swift
Appboy.sharedInstance()?.register(application,
  didReceiveRemoteNotification: userInfo)
```

{% endtab %}
{% endtabs %}

## Paso 6: Vinculación en profundidad {#step-6-deep-linking}

La vinculación en profundidad desde una notificación push hacia la aplicación se gestiona automáticamente a través de nuestra documentación estándar de integración push. Si quieres saber más sobre cómo añadir vínculos profundos a ubicaciones específicas de tu aplicación, consulta nuestros [ejemplos avanzados]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/advanced_use_cases/linking#linking-handling-customization).

## Paso 7: Pruebas unitarias (opcional) {#step-7-unit-tests-optional}

Para añadir cobertura de pruebas a los pasos de integración que acabas de seguir, implementa [pruebas unitarias de push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/unit_tests).