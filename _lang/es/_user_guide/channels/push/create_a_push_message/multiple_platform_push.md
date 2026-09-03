---
nav_title: "Mensajes push para múltiples plataformas"
article_title: "Mensajes para múltiples plataformas"
alias: "/multiple_platform_push/"
description: "Este artículo describe lo que debes saber al crear una campaña push o un Canvas con múltiples plataformas seleccionadas."
page_order: 4
---

# Mensajes push para múltiples plataformas {#multiple-platform-push-messages}

> Este artículo describe lo que debes saber cuando creas una campaña push o un Canvas para dirigirte a múltiples plataformas y dispositivos desde un solo compositor.

Al crear una campaña push o un Canvas en Braze, puedes seleccionar múltiples plataformas y dispositivos para elaborar un mensaje para todas las plataformas en una única experiencia de edición.

## Ejemplos {#use-cases}

Esta experiencia de edición es ideal para los siguientes ejemplos:

- Campaigns push móviles y pasos de mensaje en Canvas que necesitan enviarse a múltiples tipos de dispositivos (como iOS y Android).
- Notificaciones push urgentes que necesitan dirigirse a múltiples plataformas de forma rápida y precisa, donde el contenido es el mismo en todas las plataformas (como noticias de última hora o actualizaciones en vivo de juegos).

## Creación de una Campaign push multiplataforma o un Canvas {#creating-a-multiple-platform-push-campaign-or-canvas}

Para crear una campaña dirigida a múltiples plataformas y dispositivos:

1. Crea una campaña o añade un [paso de mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) a un Canvas.
2. Selecciona **Notificación push**.
3. Selecciona las plataformas deseadas (Móvil, Web, Kindle) y los dispositivos móviles (iOS, Android). Si seleccionas varios dispositivos, las pruebas multivariante no estarán disponibles para tu campaña.

### Selección de plataformas para una campaña {#selecting-platforms-for-a-campaign}
![Opciones para seleccionar múltiples plataformas para una Campaign push, como Móvil, Web y Kindle, y múltiples dispositivos, como iOS y Android.]({% image_buster /assets/img_archive/push_multiple_platform_message_selection.png %})

### Selección de plataformas para un paso en Canvas {#selecting-platforms-for-a-canvas-step}
![Opciones para seleccionar múltiples plataformas para un paso de mensaje push, como Móvil, Web y Kindle, y múltiples dispositivos, como iOS y Android.]({% image_buster /assets/img_archive/push_multiple_platform_message_selection_canvas.png %})

{:start="4"}
4. Selecciona **Confirmar**. Después de seleccionar **Confirmar**, no podrás cambiar las plataformas ni los dispositivos seleccionados.
5. Continúa configurando tu campaña o Canvas.

## Ejecución de una prueba multivariante multiplataforma {#running-a-multi-platform-multivariate-test}

Las pruebas multivariante son compatibles con las Campaigns multiplataforma. Selecciona el icono de suma junto al nombre de la variante, como lo harías para una Campaign de una sola plataforma. Para ver los pasos de configuración, consulta [Crear pruebas multivariante y A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests).

Para optimizar automáticamente tus variantes, consulta [Optimización de pruebas A/B con BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection).

![Pruebas multivariante multiplataforma sencillas]({% image_buster /assets/img_archive/push_multiple_platform_message_composer_multivariate.png %})

## Aspectos a tener en cuenta {#things-to-know}

### Mensajería unificada {#unified-messaging}
En la pestaña **Redactar**, puedes especificar un título, un mensaje y un comportamiento de clic para todas las plataformas y dispositivos que hayas elegido.

El panel de vista previa muestra una aproximación del aspecto que tendrá tu mensaje en cada plataforma. Aunque puede darte un buen indicador de dónde podrías alcanzar los límites de caracteres, recuerda siempre probar tus mensajes en un dispositivo real antes de enviar tu Campaign.

![Vista de edición única con un campo de título, mensaje y comportamiento de clic para tres tipos de push: iOS, Android y Web.]({% image_buster /assets/img_archive/push_multiple_platform_message_composer.png %})

### Activos independientes {#separate-assets}
En la sección **Activos**, selecciona o carga las imágenes que quieres que aparezcan en cada plataforma. Ten en cuenta que los diferentes dispositivos tienen distintas especificaciones de imágenes y límites de caracteres. Consulta [Formatos de mensajes e imágenes push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats) para obtener ayuda.

![Sección de activos de la vista de edición única con campos para imagen del ícono push, imagen de notificación de iOS, imagen de notificación de Android e imagen de notificación Web.]({% image_buster /assets/img_archive/push_multiple_platform_message_composer_assets.png %}){:style="max-width:50%"}

### Tipo de notificación {#notification-type}

El tipo de notificación es "Notificación push estándar" de forma predeterminada y no se puede cambiar. Si deseas crear un tipo de push diferente, como Push Stories o imagen en línea (Android), crea Campaigns independientes para cada tipo de dispositivo.

### Configuración específica del dispositivo {#device-specific-settings}

Puedes editar la configuración específica de cada plataforma en el editor. Esto incluye ajustes como [botones de acción para notificación push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_action_buttons), canales y grupos de notificación, TTL, prioridad de visualización, sonidos y más.

Para obtener más información sobre la configuración específica de cada dispositivo, consulta las siguientes colecciones de artículos:

- [Opciones de iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios)
- [Opciones de Android]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android)

### Push Stories

Push Stories está disponible en múltiples plataformas solo en Android e iOS. Si seleccionas Web o Kindle como plataforma de envío, esta opción no estará disponible.