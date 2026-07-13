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

## Casos de uso {#use-cases}

Esta experiencia de edición es ideal para los siguientes casos de uso:

- Campañas push para móvil y pasos de mensaje en Canvas que necesitan enviarse a múltiples tipos de dispositivos (como iOS y Android).
- Notificaciones push urgentes que necesitan dirigirse a múltiples plataformas de forma rápida y precisa, donde el contenido es el mismo en todas las plataformas (como noticias de última hora o actualizaciones en vivo de partidos).

## Crear una campaña push o un Canvas para múltiples plataformas {#creating-a-multiple-platform-push-campaign-or-canvas}

Para crear una campaña dirigida a múltiples plataformas y dispositivos:

1. Crea una campaña o añade un [paso de mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) a un Canvas.
2. Selecciona **Notificación push**.
3. Selecciona las plataformas deseadas (Móvil, Web, Kindle) y los dispositivos móviles (iOS, Android). Si seleccionas múltiples dispositivos, las pruebas multivariante no estarán disponibles para tu campaña.

### Seleccionar plataformas para una campaña {#selecting-platforms-for-a-campaign}
![Opciones para seleccionar múltiples plataformas para una campaña push, como Móvil, Web y Kindle, y múltiples dispositivos, como iOS y Android.]({% image_buster /assets/img_archive/push_multiple_platform_message_selection.png %})

### Seleccionar plataformas para un paso en Canvas {#selecting-platforms-for-a-canvas-step}
![Opciones para seleccionar múltiples plataformas para un paso de mensaje push, como Móvil, Web y Kindle, y múltiples dispositivos, como iOS y Android.]({% image_buster /assets/img_archive/push_multiple_platform_message_selection_canvas.png %})

{:start="4"}
4. Selecciona **Confirmar**. Después de seleccionar **Confirmar**, no podrás cambiar las plataformas o dispositivos seleccionados.
5. Continúa configurando tu campaña o Canvas.

## Ejecutar una prueba multivariante en múltiples plataformas {#running-a-multi-platform-multivariate-test}

Las pruebas multivariante son compatibles con las campañas de múltiples plataformas; simplemente selecciona el icono de más junto al nombre de la variante como lo harías normalmente para campañas de una sola plataforma. Te recomendamos [leer nuestra guía]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests) para crear pruebas multivariante y utilizar la [selección de variante de BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection) para automatizar y maximizar tu interacción.

![Pruebas multivariante fáciles en múltiples plataformas]({% image_buster /assets/img_archive/push_multiple_platform_message_composer_multivariate.png %})

## Cosas que debes saber {#things-to-know}

### Mensajería unificada {#unified-messaging}
En la pestaña **Redactar**, puedes especificar un título, un mensaje y un comportamiento al hacer clic para todas las plataformas y dispositivos que hayas elegido.

El panel de vista previa muestra una aproximación de cómo se ve tu mensaje en cada plataforma. Si bien puede darte un buen indicador de dónde podrías alcanzar los límites de caracteres, recuerda siempre probar tus mensajes en un dispositivo real antes de enviar tu campaña.

![Vista de edición única con un título, un mensaje y un campo de comportamiento al hacer clic para tres tipos de push: iOS, Android y Web.]({% image_buster /assets/img_archive/push_multiple_platform_message_composer.png %})

### Activos separados {#separate-assets}
En la sección **Activos**, selecciona o carga las imágenes que quieres que aparezcan para cada plataforma. Ten en cuenta que los diferentes dispositivos tienen distintas especificaciones para imágenes y recuentos de caracteres. Consulta [Formatos de mensajes e imágenes push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats) para obtener ayuda.

![Sección de activos de la vista de edición única con campos para imagen de icono push, imagen de notificación de iOS, imagen de notificación de Android e imagen de notificación web.]({% image_buster /assets/img_archive/push_multiple_platform_message_composer_assets.png %}){:style="max-width:50%"}

### Tipo de notificación {#notification-type}

El tipo de notificación se establece de forma predeterminada como "Push estándar" y no se puede cambiar. Si quieres crear un tipo de push diferente, como Push Stories o imagen en línea (Android), crea campañas separadas para cada tipo de dispositivo.

### Configuración específica del dispositivo {#device-specific-settings}

Puedes editar la configuración específica de cada plataforma en el editor. Esto incluye configuraciones como [botones de acción para notificación push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_action_buttons), canales y grupos de notificación, TTL, prioridad de visualización, sonidos y más.

Para más información sobre la configuración específica del dispositivo, consulta las siguientes colecciones de artículos:

- [Opciones de iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios)
- [Opciones de Android]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android)

### Push Stories

Push Stories está disponible en múltiples plataformas solo en Android e iOS. Si seleccionas Web o Kindle como plataforma de envío, esta opción no estará disponible.