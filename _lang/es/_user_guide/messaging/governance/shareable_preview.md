---
nav_title: Vista previa compartible
article_title: Comparte una vista previa del mensaje con las partes interesadas
page_order: 5
page_type: reference
description: "Este artículo de referencia explica cómo generar y compartir un enlace de vista previa de un mensaje o contenido, para que las partes interesadas sin acceso al panel puedan revisarlo antes de enviarlo."
---

# Comparte una vista previa del mensaje con las partes interesadas {#share-a-message-preview-with-stakeholders}

> La vista previa compartible te permite generar un enlace a una vista previa de tu mensaje o contenido y compartirlo con revisores, como partes interesadas, equipos legales o equipos de cumplimiento, que no tienen acceso a tu panel de Braze. Los destinatarios pueden ver la vista previa en su navegador sin iniciar sesión en Braze.

## Canales compatibles {#supported-channels}

Puedes generar un enlace de vista previa compartible para los siguientes canales y tipos de contenido:

- Banners
- Content Blocks
- Content Cards
- Correo electrónico y pie de correo electrónico
- Páginas de destino
- LINE
- Notificaciones push
- Páginas de suscripción
- servicio de mensajes cortos y RCS
- WhatsApp

{% alert note %}
La vista previa compartible se está implementando gradualmente y puede que aún no esté disponible para todos los canales en tu espacio de trabajo. Ponte en contacto con tu director de cuentas de Braze si no ves la opción para un canal listado en esta sección.
{% endalert %}

## Cómo funciona la vista previa compartible {#how-shareable-preview-works}

El siguiente comportamiento es consistente en todos los canales compatibles.

### Generar un enlace {#generating-a-link}

Mientras redactas tu mensaje o contenido, selecciona **Copiar enlace de vista previa** para generar un enlace compartible. Braze copia automáticamente el enlace a tu portapapeles.

- El enlace abre una instantánea estática de solo lectura de tu mensaje tal como aparecía en el momento en que generaste el enlace. No se actualiza automáticamente a medida que sigues editando. Genera un nuevo enlace para capturar tus últimos cambios.
- Si tu mensaje incluye personalización, como Liquid o contenido conectado que se resuelve contra un usuario de prueba, un perfil de usuario personalizado o un usuario aleatorio, la vista previa refleja esa misma personalización, coincidiendo con lo que ves en **Vista previa y prueba**.
- Seleccionar **Regenerar enlace** crea una nueva instantánea con su propia fecha de expiración. Esto no invalida el enlace anterior. Ambos enlaces siguen funcionando de forma independiente hasta que cada uno expire.

### Ver el enlace {#viewing-the-link}

Cualquier persona con el enlace puede ver la vista previa. No se requiere inicio de sesión en Braze ni permisos del panel.

{% alert important %}
Trata un enlace como cualquier otro documento compartible: envíalo solo a las personas a las que deseas dar acceso y evita publicarlo en un lugar público.
{% endalert %}

### Expiración del enlace {#link-expiration}

- Cada enlace de vista previa compartible expira siete días después de haberse generado.
- Cuando un enlace expira, ya no se abre. Genera un nuevo enlace desde el creador para obtener uno nuevo.
- No hay forma de revocar o desactivar manualmente un enlace antes de que expire. Regenerar un enlace no revoca el anterior; cada enlace simplemente expira según su propio calendario de siete días.

## Particularidades por canal {#per-channel-nuances}

Aunque la experiencia principal es la misma en todas partes, algunos canales tienen pequeñas diferencias que vale la pena conocer.

{% alert note %}
La vista previa compartible no está disponible para mensajes dentro de la aplicación.
{% endalert %}

| Canal | Qué cambia |
|---|---|
| Correo electrónico | La vista previa incluye los campos Para, De y línea del asunto del mensaje, además del cuerpo del mensaje. <br><br>Si estás personalizando como un usuario personalizado, los valores introducidos como propiedades de activación de API o propiedades del evento pueden no aparecer en la vista previa, aunque se muestren correctamente en **Vista previa y prueba**. Los atributos personalizados, los usuarios de prueba y los usuarios aleatorios no se ven afectados. |
| Banner (editor de arrastrar y soltar) | La vista previa refleja el contenido de la última vez que abriste la pestaña **Vista previa** en el creador, no necesariamente tus ediciones más recientes. <br><br>Abre **Vista previa** de nuevo antes de generar o regenerar un enlace para asegurarte de que esté actualizado. |
| servicio de mensajes cortos y RCS | Ambos se rigen por la misma funcionalidad de vista previa compartible, pero cada uno genera su propio enlace independiente. |
| WhatsApp | La vista previa compartible está disponible por separado tanto para mensajes de plantilla de WhatsApp como para mensajes de respuesta de WhatsApp. |
| Content Blocks, pies de correo electrónico y páginas de suscripción | Estos generan una vista previa del contenido independiente, sin depender de ninguna Campaign o Canvas específico en el que se utilicen. |
| Páginas de destino | La vista previa se comporta de manera diferente para las páginas de destino que para otros canales. Consulta [Vista previa de la página]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-5-preview-the-page) para más detalles. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Particularidades por canal" }

## Preguntas frecuentes {#frequently-asked-questions}

{% details ¿El destinatario necesita una cuenta de Braze para ver la vista previa? %}
No. Cualquier persona con el enlace puede ver la vista previa en su navegador sin iniciar sesión.
{% enddetails %}

{% details ¿La vista previa se actualiza si sigo editando mi mensaje? %}
No. Un enlace de vista previa compartible es una instantánea del momento en que se creó. Selecciona **Regenerar enlace** para capturar tus últimos cambios y obtener un nuevo enlace.
{% enddetails %}

{% details ¿Cuánto tiempo permanece activo el enlace? %}
Siete días desde que se generó. Si regeneras el enlace, el nuevo enlace obtiene su propia expiración de siete días, independiente del anterior.
{% enddetails %}

{% details ¿Puedo revocar un enlace antes de tiempo? %}
No, no puedes revocar un enlace. Regenerar el enlace no invalida el anterior. Todos los enlaces funcionan hasta que expiran después de siete días.
{% enddetails %}