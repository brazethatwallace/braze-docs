{% multi_lang_include developer_guide/prerequisites/swift.md %} También tendrás que [configurar las notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

## Configuración de notificaciones push enriquecidas {#setting-up-rich-push-notifications}

### Paso 1: Crear una extensión del servicio {#step-1-creating-a-service-extension}

Para crear una [extensión del servicio de notificación](https://developer.apple.com/reference/usernotifications/unnotificationserviceextension), en Xcode ve a **File > New > Target** y selecciona **Notification Service Extension**.

![SELECTOR de destino de Xcode creando una extensión del servicio de notificación para push enriquecido.]({% image_buster /assets/img_archive/ios10_se_at.png %}){: width="1442" height="1030" style="max-width:90%"}

Asegúrate de que **Embed In Application** esté configurado para incrustar la extensión en tu aplicación.

### Paso 2: Configurar la extensión del servicio de notificación {#step-2-setting-up-the-notification-service-extension}

Una extensión del servicio de notificación es su propio binario que se empaqueta con tu aplicación. Debe configurarse en el [Apple Developer Portal](https://developer.apple.com) con su propio ID de aplicación y perfil de aprovisionamiento.

El ID de paquete de la extensión del servicio de notificación debe ser distinto al ID de paquete del destino principal de tu aplicación. Por ejemplo, si el ID de paquete de tu aplicación es `com.company.appname`, puedes usar `com.company.appname.AppNameServiceExtension` para tu extensión del servicio.

### Paso 3: Añadir un grupo de aplicaciones {#step-3-adding-an-app-group}

En Xcode, añade la capacidad App Groups desde el panel **Signing & Capabilities** tanto a tu destino principal de la aplicación como al destino de la extensión del servicio de notificación. Luego, haz clic en el botón **+**. Usa el ID de paquete de tu aplicación para crear el grupo de aplicaciones. Por ejemplo, si el ID de paquete de tu aplicación es `com.company.appname`, puedes nombrar tu grupo de aplicaciones `group.com.company.appname.xyz`.

{% alert important %}
Los grupos de aplicaciones en este contexto se refieren a los [App Groups Entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups) de Apple y no al ID de tu espacio de trabajo de Braze (anteriormente grupo de aplicaciones).
{% endalert %}

Necesitas un grupo de aplicaciones compartido para que tu aplicación principal y la extensión del servicio de notificación puedan acceder a datos compartidos. Si no añades tu aplicación a un grupo de aplicaciones, tu aplicación podría no poder rellenar ciertos campos de la carga útil del push y no funcionará completamente como se espera.

### Paso 4: Integrar notificaciones push enriquecidas {#step-4-integrating-rich-push-notifications}

Para obtener una guía paso a paso sobre la integración de notificaciones push enriquecidas con `BrazeNotificationService`, consulta nuestro [tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).

Para ver un ejemplo, consulta el uso en [`NotificationService`](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/Swift/Sources/PushNotificationsServiceExtension/NotificationService.swift) de nuestra aplicación de ejemplos.

#### Añadir el framework de push enriquecido a tu aplicación {#adding-the-rich-push-framework-to-your-app}

{% tabs local %}
{% tab Swift Package Administrador %}

Después de seguir la [guía de integración de Swift Package Administrador]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration/?tab=swift%20package%20manager/), añade `BrazeNotificationService` a tu `Notification Service Extension` haciendo lo siguiente:

1. En Xcode, en frameworks y bibliotecas, selecciona el icono <i class="fas fa-plus" aria-label="Añadir"></i> para añadir un framework. <br><br>![El icono de más se encuentra en frameworks y bibliotecas en Xcode.]({% image_buster /assets/img_archive/rich_notification.png %}){: width="1930" height="446"}<br><br>

2. Selecciona el framework "BrazeNotificationService". <br><br>![El framework BrazeNotificationService se puede seleccionar en el modal que se abre.]({% image_buster /assets/img_archive/rich_notification2.png %}){: width="2248" height="1102"}

{% endtab %}
{% tab CocoaPods %}

Añade lo siguiente a tu archivo de bibliotecas:

```ruby
target 'YourAppTarget' do
  pod 'BrazeKit'
  pod 'BrazeUI'
  pod 'BrazeLocation'
end

target 'YourNotificationServiceExtensionTarget' do
  pod 'BrazeNotificationService'
end

# Only include the below if you want to also integrate Push Stories
target 'YourNotificationContentExtensionTarget' do
  pod 'BrazePushStory'
end
```

{% alert note %}
Para obtener instrucciones sobre cómo implementar Push Stories, consulta la [documentación]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/push_story/?tab=swift%20package%20manager).
{% endalert %}

Después de actualizar el archivo de bibliotecas, ve al directorio de tu proyecto de Xcode dentro de tu terminal y ejecuta `pod install`.

{% endtab %}

{% tab Manual %}

Para añadir `BrazeNotificationService.xcframework` a tu `Notification Service Extension`, consulta [Integración manual]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration?tab=manual/).

![Proyecto de Xcode con BrazeNotificationService.xcframework añadido a la extensión del servicio de notificación.]({% image_buster /assets/img/swift/rich_push/manual1.png %}){: width="1069" height="170"}

{% endtab %}
{% endtabs %}

#### Usar tu propio UNNotificationServiceExtension {#using-your-own-unnotificationserviceextension}

Si necesitas usar tu propio UNNotificationServiceExtension, puedes en su lugar llamar a [`brazeHandle`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazenotificationservice/brazehandle(request:contenthandler:)) en tu método `didReceive`.

```swift
import BrazeNotificationService
import UserNotifications

class NotificationService: UNNotificationServiceExtension {

  override func didReceive(
    _ request: UNNotificationRequest,
    withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void
  ) {
    if brazeHandle(request: request, contentHandler: contentHandler) {
      return
    }

    // Custom handling here

    contentHandler(request.content)
  }
}
```

### Paso 5: Configurar el grupo de aplicaciones en Braze {#step-5-configuring-the-app-group-in-braze}

Antes de inicializar Braze, asigna el nombre de tu grupo de aplicaciones a la propiedad [`push.appGroup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/appgroup) de la configuración de Braze.

```swift
let configuration = Braze.Configuration(apiKey: "<YOUR-BRAZE-API-KEY>",
                                        endpoint: "<YOUR-BRAZE-ENDPOINT>")
configuration.push.appGroup = "REPLACE_WITH_APPGROUP"
let braze = Braze(configuration: configuration)
```

### Paso 6: Crear una notificación enriquecida en tu panel {#step-6-creating-a-rich-notification-in-your-dashboard}

Tu equipo de marketing también puede crear notificaciones enriquecidas desde el panel. Crea una notificación push a través del creador de push y adjunta una imagen o GIF, o proporciona una URL que aloje una imagen, GIF o video. Ten en cuenta que los activos se descargan al recibir las notificaciones push, por lo que debes planificar grandes picos síncronos en las solicitudes si alojas tu propio contenido.