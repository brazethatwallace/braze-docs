{% multi_lang_include developer_guide/prerequisites/swift.md %} También tendrás que [configurar las notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

## Configuración de notificaciones push enriquecidas {#setting-up-rich-push-notifications}

### Paso 1: Crear una extensión de servicio {#step-1-creating-a-service-extension}

Para crear una [extensión del servicio de notificación](https://developer.apple.com/reference/usernotifications/unnotificationserviceextension), ve a **File > New > Target** en Xcode y selecciona **Notification Service Extension**.

![Selector de destino de Xcode creando una extensión del servicio de notificación para notificaciones push enriquecidas.]({% image_buster /assets/img_archive/ios10_se_at.png %}){: style="max-width:90%"}

Asegúrate de que la opción **Embed In Application** está activada para incrustar la extensión en tu aplicación.

### Paso 2: Configuración de la extensión del servicio de notificación {#step-2-setting-up-the-notification-service-extension}

Una extensión del servicio de notificación es un binario propio que se incluye con tu aplicación. Debe configurarse en el [Portal del Desarrollador de Apple](https://developer.apple.com) con su propio ID de aplicación y perfil de aprovisionamiento.

El ID del paquete de la extensión del servicio de notificación debe ser distinto del ID del paquete de tu aplicación principal. Por ejemplo, si el ID del paquete de tu aplicación es `com.company.appname`, puedes utilizar `com.company.appname.AppNameServiceExtension` para la extensión de tu servicio.

### Paso 3: Añadir un grupo de aplicaciones {#step-3-adding-an-app-group}

En Xcode, añade la capacidad App Groups desde el panel **Signing & Capabilities** tanto a tu objetivo de aplicación principal como al objetivo de la extensión del servicio de notificaciones. Después, haz clic en el botón **+**. Utiliza el ID del paquete de tu aplicación para crear el grupo de aplicaciones. Por ejemplo, si el ID del paquete de tu aplicación es `com.company.appname`, puedes llamar a tu grupo de aplicaciones `group.com.company.appname.xyz`.

{% alert important %}
En este contexto, App Groups se refiere al [derecho de App Groups](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups) de Apple y no a tu ID de espacio de trabajo Braze (antes "grupo de aplicaciones").
{% endalert %}

Necesitas un grupo de aplicaciones compartido para que tu aplicación principal y la extensión del servicio de notificaciones puedan acceder a los datos compartidos. Si no añades tu aplicación a un grupo de aplicaciones, es posible que tu aplicación no pueda rellenar determinados campos de la carga útil de la notificación push y no funcione correctamente como se espera.

### Paso 4: Integración de notificaciones push enriquecidas {#step-4-integrating-rich-push-notifications}

Para una guía paso a paso sobre la integración de notificaciones push enriquecidas con `BrazeNotificationService`, consulta nuestro [tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).

Para ver un ejemplo, consulta el uso en [`NotificationService`](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/Swift/Sources/PushNotificationsServiceExtension/NotificationService.swift) de nuestra aplicación de ejemplos.

#### Añadir el framework de notificaciones push enriquecidas a tu aplicación {#adding-the-rich-push-framework-to-your-app}

{% tabs local %}
{% tab Swift Package Manager %}

Después de seguir la [guía de integración de Swift Package Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration/?tab=swift%20package%20manager/), añade `BrazeNotificationService` a tu `Notification Service Extension` haciendo lo siguiente:

1. En Xcode, en frameworks y bibliotecas, selecciona el icono <i class="fas fa-plus"></i> para añadir un framework. <br><br>![El icono más se encuentra debajo de frameworks y bibliotecas en Xcode.]({% image_buster /assets/img_archive/rich_notification.png %})<br><br>

2. Selecciona el framework "BrazeNotificationService". <br><br>![El framework "BrazeNotificationService" se puede seleccionar en la ventana modal que se abre.]({% image_buster /assets/img_archive/rich_notification2.png %})

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

Tras actualizar el archivo de bibliotecas, ve al directorio de tu proyecto de aplicación Xcode dentro de tu terminal y ejecuta `pod install`.

{% endtab %}

{% tab Manual %}

Para añadir `BrazeNotificationService.xcframework` a tu `Notification Service Extension`, consulta [Integración manual]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration?tab=manual/).

![Proyecto de Xcode con BrazeNotificationService.xcframework añadido a la extensión del servicio de notificación.]({% image_buster /assets/img/swift/rich_push/manual1.png %})

{% endtab %}
{% endtabs %}

#### Utilizar tu propia UNNotificationServiceExtension {#using-your-own-unnotificationserviceextension}

Si necesitas utilizar tu propia UNNotificationServiceExtension, puedes llamar en su lugar a [`brazeHandle`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazenotificationservice/brazehandle(request:contenthandler:)) en tu método `didReceive`.

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

### Paso 5: Configuración del grupo de aplicaciones en Braze {#step-5-configuring-the-app-group-in-braze}

Antes de inicializar Braze, asigna el nombre de tu grupo de aplicaciones a la propiedad [`push.appGroup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/appgroup) de tu configuración de Braze.

```swift
let configuration = Braze.Configuration(apiKey: "<YOUR-BRAZE-API-KEY>",
                                        endpoint: "<YOUR-BRAZE-ENDPOINT>")
configuration.push.appGroup = "REPLACE_WITH_APPGROUP"
let braze = Braze(configuration: configuration)
```

### Paso 6: Crear una notificación enriquecida en tu panel {#step-6-creating-a-rich-notification-in-your-dashboard}

Tu equipo de marketing también puede crear notificaciones enriquecidas desde el panel. Crea una notificación push a través del creador de push y adjunta una imagen o un GIF, o proporciona una URL que aloje una imagen, un GIF o un video. Ten en cuenta que los activos se descargan al recibir las notificaciones push, por lo que debes prever grandes picos sincrónicos de solicitudes si alojas tu contenido.