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

Las alertas se configuran a nivel de Canvas, y puedes configurarlas tanto para Canvas activos como en borrador. Para abrir la página **Gestionar alertas** de un Canvas, puedes:

- Ir a **Mensajería** > **Canvas** y seleccionar **Gestionar alertas** en el menú contextual de un Canvas individual.
- Para Canvas activos, abrir **Canvas Analytics** y seleccionar **Gestionar alertas**.

Desde la página **Gestionar alertas**, selecciona **Configurar alerta** para crear una nueva alerta.

## Paso 2: Nombra tu alerta y selecciona un Canvas {#step-2-name-your-alert-and-select-a-canvas}

Dale un nombre a tu alerta y confirma el Canvas al que se aplica.

![El panel Configurar alerta que muestra los campos de nombre de alerta y nombre de Canvas, un grupo de reglas vacío y una barra lateral de resumen para reglas de alerta, programación y notificaciones.]({% image_buster /assets/img/canvas_threshold_alerts/configure_alert.png %})

## Paso 3: Configurar reglas de alerta {#step-3-set-alert-rules}

Las reglas de alerta definen el umbral que desencadena una notificación. Puedes crear reglas usando dos métricas:

- **Entradas de usuarios:** Número de usuarios que entraron al Canvas
- **Mensajes enviados:** Número de mensajes enviados desde el Canvas

Para cada regla, elige una comparación (menor que, mayor que, menor o igual que, mayor o igual que, o igual a) y un umbral de volumen. Por ejemplo, una regla de "Entradas de usuarios menor que 3,000" marca un Canvas que normalmente alcanza a miles de usuarios pero que se ha detenido repentinamente, una señal de un problema de audiencia o entrada upstream que vale la pena investigar.

Puedes agrupar varias reglas juntas y combinar grupos de reglas con lógica AND u OR para crear condiciones de alerta más específicas.

## Paso 4: Configura el horario de alertas {#step-4-set-the-alert-schedule}

Define con qué frecuencia se comprueban tus reglas de alerta. Puedes establecer la frecuencia de comprobación en cualquier intervalo de 3 a 12 horas (en incrementos de 1 hora), o cada 24 horas. Una vez activada, una alerta continúa comprobándose según este horario mientras la alerta y su Canvas asociado estén activos.

## Paso 5: Configurar notificaciones {#step-5-set-up-notifications}

Elige quién debe recibir una notificación cuando se cumple una regla de alerta y cómo se le notifica:

- **Correo electrónico:** Añade una o más direcciones de correo electrónico de destinatarios
- **Webhook:** Introduce la URL del webhook para notificar y, opcionalmente, añade encabezados de solicitud personalizados requeridos por tu destino de webhook

Puedes habilitar uno o ambos métodos de notificación para una sola alerta.

![La sección Notificaciones del panel Configurar alerta, que muestra los alternadores de correo electrónico y webhook, un campo de destinatarios de correo electrónico, un campo de URL de webhook, una nota sobre el contenido de la carga útil y campos opcionales de encabezados de solicitud.]({% image_buster /assets/img/canvas_threshold_alerts/notifications.png %})

Las alertas de webhook son útiles para enrutar notificaciones a plataformas externas, como un canal de Slack. Para más información, consulta la documentación de Slack sobre [enviar mensajes usando webhooks entrantes](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/). Cada notificación de webhook envía una carga útil JSON con el nombre de la alerta, la ventana de evaluación y las condiciones que desencadenaron la alerta.

### Ejemplo de carga útil de webhook {#example-webhook-payload}

El siguiente es un ejemplo de la carga útil JSON enviada en una solicitud POST a tu endpoint de webhook cuando se desencadena una alerta:

```json
{
  "alert": {
    "name": "Canvas Alert - August 6, 2026",
    "target_type": "CANVAS"
  },
  "evaluation_window_start": "2026-08-06T10:28:01Z",
  "evaluation_window_end": "2026-08-06T13:28:01Z",
  "conditions": [
    {
      "subject": "user_entries",
      "operator": "lt",
      "threshold_value": 500,
      "metric_value": 0.0,
      "group_index": 0
    },
    {
      "subject": "messages_sent",
      "operator": "lt",
      "threshold_value": 500,
      "metric_value": 0.0,
      "group_index": 0
    }
  ]
}
```

## Paso 6: Guarda tu alerta {#step-6-save-your-alert}

Revisa las reglas de tu alerta, el horario y la configuración de notificaciones en el panel de resumen, luego selecciona **Save alert**.

## Paso 7: Activar la alerta {#step-7-activate-the-alert}

Guardar una alerta no la activa. Para activarla, ve a la página **Gestionar alertas** y usa el alternador de **Estado** de tu alerta. Una alerta permanece activa hasta que la desactives o hasta que su Canvas asociado deje de estar activo. La columna **Alertas configuradas** en la página de **Canvas** muestra un icono de campana para cualquier Canvas con al menos una alerta guardada.

## Consideraciones {#considerations}

- **Canvas en borrador:** Puedes configurar una alerta de umbral para un Canvas que aún esté en borrador, pero la alerta no comenzará a verificar tus reglas hasta que se lance el Canvas.