---
nav_title: Actualizar a iOS 18
article_title: Actualizar a iOS 18
page_order: 7.1
platform:
  - iOS
description: "Este artículo contiene información sobre la versión iOS 18 para ayudarte a actualizar tu SDK fácilmente."
---

# Actualizar a iOS 18 {#upgrading-to-ios-18}

> ¿Tienes curiosidad por saber cómo se está preparando Braze para el próximo lanzamiento de iOS? Este artículo resume nuestra información sobre la versión de iOS 18 para ayudarte a crear una experiencia fluida para ti y tus usuarios.

La [WWDC](https://developer.apple.com/wwdc24/) de Apple tuvo lugar del 9 al 11 de junio de 2024. Obtén más información sobre sus anuncios en nuestra [entrada de blog](https://www.braze.com/resources/articles/wwdc-announcements-bring-apple-intelligence-rcs-and-more-to-ios-18), o sigue leyendo para saber cómo puedes aprovechar iOS 18 con Braze.

## Cambios en iOS 18 {#changes-in-ios-18}

### Live Activities en Apple Watch {#live-activities-on-apple-watch}

[Live Activities]({{site.baseurl}}/developer_guide/live_notifications?sdktab=swift) será compatible con watchOS 11. No se requiere configuración adicional. Sin embargo, Apple ofrece la opción de personalizar la interfaz del reloj.

### Apple Vision Pro

El Vision Pro ya está disponible en China, Japón, Singapur, Australia, Canadá, Francia, Alemania y el Reino Unido. Consulta nuestro blog para ver cómo [Braze es compatible con visionOS](https://www.braze.com/resources/articles/building-braze-a-new-era-of-customer-engagement-braze-announces-visionos-support).

### Notificaciones de iPhone en macOS {#iphone-notifications-on-macos}

La nueva característica de Apple, [duplicación de iPhone](https://www.apple.com/newsroom/2024/06/macos-sequoia-takes-productivity-and-intelligence-on-mac-to-new-heights/), permite a los usuarios recibir notificaciones de iPhone en sus dispositivos macOS. Ten en cuenta que algunos tipos de contenido multimedia, como las imágenes de historias push y los GIF, no son compatibles, ya que no se pueden renderizar como una notificación de macOS.

### Apple Intelligence

[Apple Intelligence](https://developer.apple.com/documentation/Updates/Apple-Intelligence) ya está disponible para dispositivos con iOS 18.1 y versiones posteriores.

Como usuario de Braze, la nueva característica más importante que debes conocer son los [resúmenes de notificaciones](https://support.apple.com/en-us/108781), que utilizan procesamiento en el dispositivo para agrupar automáticamente y generar resúmenes de texto para notificaciones push relacionadas enviadas desde una sola aplicación. Los usuarios finales pueden tocar para expandir un resumen y ver cada notificación push tal como se envió originalmente.

Debido a cómo se generan estos resúmenes, no tendrás control sobre su comportamiento específico ni sobre el texto generado. Sin embargo, esto no afectará a ninguna característica de análisis ni de informes, como el seguimiento de clics en push.

![Captura de pantalla de ejemplo de un resumen de vista previa de notificación push.]({% image_buster /assets/img/apple/apple_intelligence/notification_preview_summary.png %})