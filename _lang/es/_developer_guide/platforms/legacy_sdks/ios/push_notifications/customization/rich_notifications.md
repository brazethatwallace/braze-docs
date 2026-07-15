---
nav_title: Crear notificaciones enriquecidas
article_title: Creación de notificaciones push enriquecidas para iOS
platform: iOS
page_order: 3
description: "Este artículo de referencia cubre la implementación de notificaciones push enriquecidas en tu aplicación iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Notificaciones enriquecidas de iOS 10 {#ios-10-rich-notifications}

iOS 10 introduce la posibilidad de enviar notificaciones push con imágenes, GIF y video. Para habilitar esta funcionalidad, los clientes deben crear un `Service Extension`, un nuevo tipo de extensión que permite modificar una carga útil push antes de que se muestre.

## Crear una extensión de servicio {#creating-a-service-extension}

Para crear una [`Notification Service Extension`](https://developer.apple.com/reference/usernotifications/unnotificationserviceextension), ve a **File > New > Target** en Xcode y selecciona **Notification Service Extension**.

![Selector de destino de Xcode creando una Notification Service Extension para notificaciones enriquecidas.]({% image_buster /assets/img_archive/ios10_se_at.png %}){: style="max-width:90%"}

Asegúrate de que la opción **Embed In Application** está activada para incrustar la extensión en tu aplicación.

## Configuración de la extensión de servicio {#setting-up-the-service-extension}

Un `Notification Service Extension` es un binario propio que se incluye con tu aplicación. Debe configurarse en el [Portal del Desarrollador de Apple](https://developer.apple.com) con su propio ID de aplicación y perfil de aprovisionamiento.

El ID del paquete de `Notification Service Extension` debe ser distinto del ID del paquete de tu aplicación principal. Por ejemplo, si el ID del paquete de tu aplicación es `com.company.appname`, puedes utilizar `com.company.appname.AppNameServiceExtension` para la extensión de tu servicio.

### Configurar la extensión de servicio para que funcione con Braze {#configuring-the-service-extension-to-work-with-braze}

Braze envía una carga útil adjunta en la carga útil de APNs bajo la clave `ab` que utilizamos para configurar, descargar y mostrar contenido enriquecido. Por ejemplo:

```json
{
  "ab" :
    {
    ...

    "att" :
      {
       "url" : "http://mysite.com/myimage.jpg",
       "type" : "jpg"
       }
    },
  "aps" :
    {
    ...
    }
}
```

Los valores relevantes de la carga útil son:

```objc
// The Braze dictionary key
static NSString *const AppboyAPNSDictionaryKey = @"ab";

// The attachment dictionary
static NSString *const AppboyAPNSDictionaryAttachmentKey = @"att";

// The attachment URL
static NSString *const AppboyAPNSDictionaryAttachmentURLKey = @"url";

// The type of the attachment - a suffix for the file you save
static NSString *const AppboyAPNSDictionaryAttachmentTypeKey = @"type";
```

Para mostrar manualmente el push con una carga útil de Braze, descarga el contenido del valor en `AppboyAPNSDictionaryAttachmentURLKey`, guárdalo como un archivo con el tipo de archivo almacenado en la clave `AppboyAPNSDictionaryAttachmentTypeKey` y añádelo a los archivos adjuntos de la notificación.

### Ejemplo de código {#example-code}

Puedes escribir la extensión de servicio en Objective-C o Swift.

Para utilizar nuestro código de ejemplo en Objective-C, sustituye el contenido del `NotificationService.m` autogenerado de tu destino `Notification Service Extension` por el contenido de Appboy [`NotificationService.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/StopwatchNotificationService/NotificationService.m).

Para utilizar nuestro código de ejemplo en Swift, sustituye el contenido del `NotificationService.swift` autogenerado de tu destino `Notification Service Extension` por el contenido de Appboy [`NotificationService.swift`](https://github.com/Appboy/appboy-ios-sdk/blob/master/HelloSwift/HelloSwiftNotificationExtension/NotificationService.swift).

## Crear una notificación enriquecida en tu panel {#creating-a-rich-notification-in-your-dashboard}

Para crear una notificación enriquecida en tu panel de Braze, crea un push de iOS, adjunta una imagen o GIF, o proporciona una URL que aloje una imagen, GIF o video. Ten en cuenta que los activos se descargan al recibir las notificaciones push, por lo que debes prever grandes picos sincrónicos de solicitudes si alojas tu contenido.

Consulta [`unnotificationattachment`](https://developer.apple.com/reference/usernotifications/unnotificationattachment) para ver la lista de tipos y tamaños de archivo admitidos.