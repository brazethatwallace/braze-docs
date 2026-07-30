---
nav_title: Alertas de Canvas
article_title: Alertas de umbral de Canvas
page_order: 4
page_type: reference
description: "Este artículo de referencia explica cómo configurar alertas de umbral para un Canvas, de modo que recibas notificaciones proactivas cuando las entradas de usuarios o los mensajes enviados estén fuera del rango esperado."
tool: Canvas
channel:
- email
- webhooks
---

# Alertas de umbral de Canvas {#canvas-threshold-alerts}

> Las alertas de umbral de Canvas te avisan cuando algo en un Canvas no está funcionando según lo previsto, para que puedas detectar un recorrido detenido o una caída inesperada antes de que afecte a tus clientes.

{% multi_lang_include alerts/early_access_beta_alert.md feature='Canvas threshold alerts' %}

Establece un umbral de volumen para las entradas de usuarios o los mensajes enviados, y Braze te notificará por correo electrónico o webhook si se supera ese umbral. También puedes crear múltiples alertas para el mismo Canvas; por ejemplo, una alerta para entradas de usuarios y otra para mensajes enviados.

¿No sabes por dónde empezar? [Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities) puede guiarte para configurar una alerta de umbral de Canvas.

## Paso 1: Crear una alerta {#step-1-create-an-alert}

Las alertas se configuran a nivel de Canvas y puedes establecerlas tanto para Canvas activos como en borrador. Para abrir la página **Administrar alertas** de un Canvas, puedes:

- Ir a **Mensajería** > **Canvas** y seleccionar **Administrar alertas** en el menú contextual de un Canvas individual.
- Para Canvas activos, abrir **Análisis de Canvas** y seleccionar **Administrar alertas**.

Desde la página **Administrar alertas**, selecciona **Configurar alerta** para crear una nueva alerta.

## Paso 2: Nombrar la alerta y seleccionar un Canvas {#step-2-name-your-alert-and-select-a-canvas}

Dale un nombre a tu alerta y confirma el Canvas al que se aplica.

![El panel Configurar alerta mostrando los campos de nombre de alerta y nombre de Canvas, un grupo de reglas vacío y una barra lateral de resumen para reglas de alerta, programación y notificaciones.]({% image_buster /assets/img/canvas_threshold_alerts/configure_alert.png %})

## Paso 3: Establecer las reglas de alerta {#step-3-set-alert-rules}

Las reglas de alerta definen el umbral que desencadena una notificación. Puedes crear reglas usando dos métricas:

- **Entradas de usuarios:** número de usuarios que entraron al Canvas
- **Mensajes enviados:** número de mensajes enviados desde el Canvas

Para cada regla, elige una comparación (menor que o mayor que) y un umbral de volumen. Por ejemplo, una regla de "Entradas de usuarios menor que 3.000" señala un Canvas que normalmente alcanza miles de usuarios pero que se ha detenido repentinamente, lo que indica un problema de audiencia o entrada que vale la pena investigar.

Puedes agrupar múltiples reglas y combinar grupos de reglas con lógica AND u OR para crear condiciones de alerta más específicas.

## Paso 4: Establecer la programación de la alerta {#step-4-set-the-alert-schedule}

Define con qué frecuencia se verifican las reglas de alerta. Puedes establecer la frecuencia de verificación entre 3 y 12 horas (en incrementos de 1 hora), o cada 24 horas. Una vez activada, la alerta continúa verificando según esta programación mientras la alerta y su Canvas asociado estén activos.

## Paso 5: Configurar las notificaciones {#step-5-set-up-notifications}

Elige quién debe ser notificado cuando se cumpla una regla de alerta y cómo se le notifica:

- **Correo electrónico:** agrega una o más direcciones de correo electrónico de destinatarios
- **Webhook:** ingresa la URL del webhook para notificar y, opcionalmente, agrega encabezados de solicitud personalizados requeridos por el destino de tu webhook

Puedes habilitar uno o ambos métodos de notificación para una sola alerta.

![La sección de notificaciones del panel Configurar alerta, mostrando los alternadores de correo electrónico y webhook, un campo de destinatarios de correo electrónico, un campo de URL de webhook, una nota sobre el contenido de la carga útil y campos opcionales de encabezados de solicitud.]({% image_buster /assets/img/canvas_threshold_alerts/notifications.png %})

Las alertas por webhook son útiles para enrutar notificaciones a plataformas externas, como un canal de Slack. Para más información, consulta la documentación de Slack sobre [enviar mensajes usando webhooks entrantes](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/). Cada notificación por webhook incluye una carga útil con el nombre del Canvas, la métrica de la alerta, la dirección del umbral, el valor que desencadenó la alerta y un enlace directo al Canvas.

## Paso 6: Guardar la alerta {#step-6-save-your-alert}

Revisa las reglas de alerta, la programación y la configuración de notificaciones en el panel de resumen, y luego selecciona **Guardar alerta**.

## Paso 7: Activar la alerta {#step-7-activate-the-alert}

Guardar una alerta no la activa. Para activarla, ve a la página **Administrar alertas** y usa el alternador de **Estado** de tu alerta. Una alerta permanece activa hasta que la desactives o hasta que su Canvas asociado deje de estar activo. La columna **Alertas configuradas** en la página de **Canvas** muestra un ícono de campana para cualquier Canvas que tenga al menos una alerta guardada.

## Consideraciones {#considerations}

- **Canvas en borrador:** puedes configurar una alerta de umbral para un Canvas que aún esté en borrador, pero la alerta no comenzará a verificar tus reglas hasta que el Canvas se lance.