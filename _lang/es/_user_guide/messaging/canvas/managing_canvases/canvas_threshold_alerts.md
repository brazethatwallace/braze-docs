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

Establece un umbral de volumen o porcentaje para las entradas de usuarios o los mensajes enviados, y Braze te notificará por correo electrónico o webhook si se supera ese umbral. También puedes crear múltiples alertas para el mismo Canvas; por ejemplo, una alerta para entradas de usuarios y otra para mensajes enviados.

¿No sabes por dónde empezar? [Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities) puede guiarte para configurar una alerta de umbral de Canvas.

## Paso 1: Crear una alerta {#step-1-create-an-alert}

Las alertas se configuran a nivel de Canvas, y puedes configurarlas tanto para Canvas activos como en borrador. Para abrir la página **Gestionar alertas** de un Canvas, puedes:

- Ir a **Messaging** > **Canvas** y seleccionar **Gestionar alertas** en el menú contextual de un Canvas individual.
- Para Canvas activos, abrir **Canvas Analytics** y seleccionar **Gestionar alertas**.

Desde la página **Gestionar alertas**, selecciona **Configurar alerta** para crear una nueva alerta.

## Paso 2: Nombra tu alerta y selecciona un Canvas {#step-2-name-your-alert-and-select-a-canvas}

Dale un nombre a tu alerta y confirma el Canvas al que se aplica.

![El panel Configurar alerta mostrando los campos de nombre de alerta y nombre de Canvas, un grupo de reglas vacío y una barra lateral de resumen para reglas de alerta, programación y notificaciones.]({% image_buster /assets/img/canvas_threshold_alerts/configure_alert.png %})

## Paso 3: Configurar reglas de alerta {#step-3-set-alert-rules}

Las reglas de alerta definen el umbral que desencadena una notificación. Puedes crear reglas utilizando dos métricas:

- **Entradas de usuarios:** Número de usuarios que entraron en el Canvas
- **Mensajes enviados:** Número de mensajes enviados desde el Canvas

Para cada regla, elige una comparación (menor que, mayor que, menor o igual que, mayor o igual que, o igual a), una unidad y un umbral.

- **Volumen:** Compara el recuento absoluto en la ventana de verificación actual. Por ejemplo, "Entradas de usuarios menor que 3,000" marca un Canvas que normalmente alcanza a miles de usuarios, pero que se ha detenido repentinamente, una señal de un problema de audiencia o entrada upstream que vale la pena investigar.
- **Porcentaje:** Compara el recuento actual con una línea base para este Canvas. La línea base es el promedio de la misma ventana de tiempo durante los 7 días anteriores. Por ejemplo, si la alerta se verifica cada 3 horas, una verificación de 2 a 5 p. m. se compara con el promedio de las siete ventanas previas de 2 a 5 p. m. Una regla de "Mensajes enviados menor que 50%" marca una caída a menos de la mitad de ese volumen habitual.

Los umbrales son números enteros. Para reglas de porcentaje con **menor que** o **menor o igual que**, introduce un valor de 1 a 100. Para **mayor que**, **mayor o igual que** o **igual a**, el porcentaje puede ser 0 o superior, incluyendo valores por encima de 100, para que puedas alertar sobre un pico en relación con la línea base.

Puedes agrupar múltiples reglas juntas, incluyendo la combinación de reglas de volumen y porcentaje, y combinar grupos de reglas con lógica AND u OR para crear condiciones de alerta más específicas.

## Paso 4: Configura el horario de alertas {#step-4-set-the-alert-schedule}

Define con qué frecuencia se comprueban tus reglas de alerta. Puedes configurar la frecuencia de comprobación en cualquier intervalo de 3 a 12 horas (en incrementos de 1 hora), o cada 24 horas. Una vez activada, una alerta continúa comprobándose según este horario mientras la alerta y su Canvas asociado estén activos.

## Paso 5: Configurar las notificaciones {#step-5-set-up-notifications}

Elige quién debe recibir una notificación cuando se cumpla una regla de alerta y cómo se le notifica:

- **Correo electrónico:** Añade una o más direcciones de correo electrónico de destinatarios
- **Webhook:** Introduce la URL del webhook para notificar y, opcionalmente, añade encabezados de solicitud personalizados que requiera tu destino de webhook

Puedes habilitar uno o ambos métodos de notificación para una sola alerta.

Las alertas de webhook son útiles para enrutar notificaciones a plataformas externas, como un canal de Slack. Para más información, consulta la documentación de Slack sobre [enviar mensajes usando webhooks entrantes](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/). Cada notificación de webhook envía una carga útil JSON con el nombre de la alerta, la ventana de evaluación y las condiciones que activaron la alerta. Cada condición incluye un `threshold_unit` de `volume` o `percentage`. Las condiciones de porcentaje también incluyen `percentage_metric_value` (el recuento observado como porcentaje en número entero de la línea base). `metric_value` es siempre el recuento absoluto.

### Ejemplo de carga útil de webhook {#example-webhook-payload}

A continuación se muestra un ejemplo de la carga útil JSON enviada en una solicitud POST a tu endpoint de webhook cuando se activa una alerta. La primera condición es una regla de volumen. La segunda es una regla de porcentaje: 51.235 mensajes enviados, lo que representa un 57 % de la línea base de la misma ventana de 7 días, frente a un umbral de más del 55 %.

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
      "group_index": 0,
      "threshold_unit": "volume"
    },
    {
      "subject": "messages_sent",
      "operator": "gt",
      "threshold_value": 55,
      "metric_value": 51235.0,
      "group_index": 0,
      "threshold_unit": "percentage",
      "percentage_metric_value": 57
    }
  ]
}
```

## Paso 6: Guarda tu alerta {#step-6-save-your-alert}

Revisa las reglas de tu alerta, la programación y la configuración de notificaciones en el panel de resumen, y luego selecciona **Save alert**.

## Paso 7: Activar la alerta {#step-7-activate-the-alert}

Guardar una alerta no la activa. Para activarla, ve a la página **Administrar alertas** y usa el alternador de **Estado** de tu alerta. Una alerta permanece activa hasta que la desactivas o hasta que su Canvas asociado deja de estar activo. La columna **Alertas configuradas** en la página de **Canvas** muestra un icono de campana para cualquier Canvas que tenga al menos una alerta guardada.

## Consideraciones {#considerations}

- **Canvas en borrador:** Puedes configurar una alerta de umbral para un Canvas que aún esté en borrador, pero la alerta no comenzará a verificar tus reglas hasta que el Canvas se lance.
- **Línea base de porcentaje:** Las reglas de porcentaje necesitan siete días completos previos de la misma ventana después de que el Canvas se lance. Hasta que esas ventanas existan, o cuando el promedio de la línea base sea cero (sin actividad en esas ventanas previas), las reglas de porcentaje no desencadenan una notificación.

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Las alertas de umbral de Canvas cuentan para el uso de webhooks? {#do-canvas-threshold-alerts-count-toward-webhook-usage}

No. Las alertas de umbral de Canvas no cuentan para los límites de velocidad de webhooks ni para las métricas de uso.