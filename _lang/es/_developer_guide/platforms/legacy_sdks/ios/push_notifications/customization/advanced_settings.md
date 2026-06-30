---
nav_title: Configuración avanzada
article_title: Configuración push avanzada
platform: iOS
page_order: 5
description: "Este artículo de referencia cubre la configuración avanzada de las notificaciones push de iOS, como las opciones de alerta, los sonidos, la caducidad y mucho más."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Configuración avanzada {#advanced-settings}

Al crear una campaña push, en el paso de composición, selecciona **Settings** para ver la configuración avanzada disponible.

![Configuración avanzada de una campaña push de iOS en el panel de Braze.]({% image_buster /assets/img_archive/ios_advanced_settings.png %})

## Extraer datos de pares clave-valor push {#extracting-data-from-push-key-value-pairs}

Braze te permite enviar pares clave-valor de cadena definidos a medida, conocidos como `extras`, junto con una notificación push a tu aplicación. Los extras pueden definirse a través del dashboard o de la API y estarán disponibles como pares clave-valor dentro del diccionario `notification` pasado a tus implementaciones de delegados push.

## Opciones de alerta {#alert-options}

Marca la casilla **Alert Options** para ver un desplegable de valores clave disponibles para ajustar cómo aparece la notificación en los dispositivos.

## Añadir la flag de contenido disponible {#adding-content-available-flag}

Marca la casilla **Add Content-Available Flag** para indicar a los dispositivos que descarguen nuevos contenidos en segundo plano. Lo más habitual es marcar esta opción si te interesa enviar [notificaciones silenciosas]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/silent_push_notifications).

## Añadir la flag de contenido mutable {#adding-mutable-content-flag}

Marca la casilla **Add Mutable-Content Flag** para habilitar la personalización avanzada del receptor en dispositivos iOS 10+. Esta flag se enviará automáticamente al componer una [notificación enriquecida]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/rich_notifications), independientemente del valor de esta casilla.

## Actualizar recuento de señales de la aplicación {#update-app-badge-count}

Introduce el número con el que quieres actualizar el recuento de tus señales, o utiliza la sintaxis Liquid para establecer tus condiciones personalizadas. También puedes actualizar manualmente el recuento de tus señales a través de la propiedad `applicationIconBadgeNumber` de tu aplicación o de la carga útil de la notificación push. Para saber más, consulta nuestro artículo dedicado al [recuento de señales]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/badges).

## Sonidos {#sounds}

Aquí puedes introducir una ruta a un archivo de sonido en el paquete de tu aplicación para especificar un sonido que se reproducirá cuando se reciba el mensaje push. Si el archivo de sonido especificado no existe o si se introduce la palabra clave "default", Braze utilizará el sonido de alerta predeterminado del dispositivo. Para más información sobre la personalización, consulta nuestro artículo dedicado a [los sonidos personalizados]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/custom_sounds).

## ID de colapso {#collapse-id}

Especifica un ID de colapso para agrupar notificaciones similares. Si envías varias notificaciones con el mismo ID de colapso, el dispositivo solo mostrará la notificación recibida más recientemente. Consulta la documentación de Apple sobre [notificaciones agrupadas](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1).

## Caducidad {#expiry}

Si marcas la casilla **Expiry**, podrás establecer un tiempo de caducidad para tu mensaje. Si el dispositivo de un usuario pierde la conectividad, Braze seguirá intentando enviar el mensaje hasta la hora especificada. Si no se configura, la plataforma tendrá una caducidad predeterminada de 30 días. Ten en cuenta que las notificaciones push que caducan antes de la entrega no se consideran fallidas y no se registrarán como rebotadas.