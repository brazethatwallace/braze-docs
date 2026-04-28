---
nav_title: "Mensajes push rápidos"
article_title: "Mensajes push rápidos"
alias: "/quick_push/"
description: "Este artículo describe lo que debes saber al crear una campaña push o un Canvas utilizando la experiencia de edición de push rápido."
page_order: 4
---

# Mensajes push rápidos {#quick-push-messages}

> Este artículo describe lo que debes saber al crear una campaña push o un Canvas utilizando la experiencia de edición de push rápido para dirigirte a múltiples plataformas y dispositivos desde un solo compositor.

Al crear una campaña push o un Canvas en Braze, puedes seleccionar múltiples plataformas y dispositivos para elaborar un mensaje para todas las plataformas en una única experiencia de edición llamada push rápido.

## Casos de uso {#use-cases}

Esta experiencia de edición es ideal para los siguientes casos de uso:

- Campaigns push para móvil y pasos de mensaje en Canvas que necesitan enviarse a múltiples tipos de dispositivos (como iOS y Android).
- Notificaciones push urgentes que necesitan dirigirse a múltiples plataformas de forma rápida y precisa, donde el contenido es el mismo en todas las plataformas (como noticias de última hora o actualizaciones de juegos en vivo).

## Crear una campaña o Canvas de push rápido {#creating-a-quick-push-campaign-or-canvas}

Para crear una campaña dirigida a múltiples plataformas y dispositivos:

1. Crea una campaña o añade un [paso de mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/) a un Canvas.
2. Selecciona **Push notification**.
3. Selecciona las plataformas deseadas (Mobile, Web, Kindle) y los dispositivos móviles (iOS, Android). Si seleccionas múltiples dispositivos, las pruebas multivariante no estarán disponibles para tu campaña.

### Seleccionar plataformas para una campaña {#selecting-platforms-for-a-campaign}
![Opciones para seleccionar múltiples plataformas para una campaña push, como Mobile, Web y Kindle, y múltiples dispositivos, como iOS y Android.]({% image_buster /assets/img_archive/quick_push_1.png %})

### Seleccionar plataformas para un paso en Canvas {#selecting-platforms-for-a-canvas-step}
![Opciones para seleccionar múltiples plataformas para un paso de mensaje push, como Mobile, Web y Kindle, y múltiples dispositivos, como iOS y Android.]({% image_buster /assets/img_archive/quick_push_4.png %})

{:start="4"}
4. Selecciona **Confirm**. Después de seleccionar **Confirm**, no podrás cambiar las plataformas o dispositivos seleccionados.
5. Continúa configurando tu campaña o Canvas.

Tu compositor se verá ligeramente diferente de lo habitual. Sigue leyendo para ver qué ha cambiado.

### Qué es diferente {#whats-different}

En la pestaña **Compose**, puedes especificar un título, un mensaje y un comportamiento de clic para todas las plataformas y dispositivos elegidos.

El panel de vista previa muestra una aproximación de cómo se verá tu mensaje en cada plataforma. Aunque puede darte un buen indicador de dónde podrías alcanzar los límites de caracteres, recuerda siempre probar tus mensajes en un dispositivo real antes de enviar tu campaña.

![Vista de edición única con un título, un mensaje y un campo de comportamiento de clic para tres tipos de push: iOS, Android y Web.]({% image_buster /assets/img_archive/quick_push_2.png %})

En la sección **Assets**, selecciona o carga las imágenes que deseas que aparezcan para cada plataforma. Ten en cuenta que los diferentes dispositivos tienen distintas especificaciones para imágenes y recuentos de caracteres. Consulta [Formatos de mensajes e imágenes push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats/) para obtener ayuda.

![Sección de activos de la vista de edición única con campos para Push Icon Image, imagen de notificación iOS, imagen de notificación Android e imagen de notificación Web.]({% image_buster /assets/img_archive/quick_push_3.png %}){:style="max-width:50%"}

Luego, termina de configurar tu campaña push como de costumbre. Consulta [Crear una campaña push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/) para más detalles.

## Cosas que debes saber {#things-to-know}

### Tipo de notificación {#notification-type}

El tipo de notificación se establece de forma predeterminada como "Push estándar" y no se puede cambiar. Si deseas crear un push diferente, como Push Stories o imagen en línea (Android), crea campañas separadas para cada tipo de dispositivo.

### Pruebas multivariante {#multivariate-testing}

Si seleccionas múltiples dispositivos para plataformas móviles, como iOS y Android, las pruebas multivariante no estarán disponibles para tu campaña. Si deseas realizar pruebas multivariante, crea campañas separadas para cada tipo de dispositivo.

### Configuración específica del dispositivo {#device-specific-settings}

Puedes editar la configuración específica de la plataforma en el editor. Esto incluye configuraciones como [botones de acción para notificación push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_action_buttons/), canales y grupos de notificación, TTL, prioridad de visualización, sonidos y más.

Ten en cuenta que los botones de acción para notificación push no son compatibles cuando se dirigen tanto a iOS como a Android utilizando campañas de push rápido. Para más información sobre la configuración específica del dispositivo, consulta las siguientes colecciones de artículos:

- [Opciones de iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/)
- [Opciones de Android]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/)