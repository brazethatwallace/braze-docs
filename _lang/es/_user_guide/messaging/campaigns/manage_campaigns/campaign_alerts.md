---
nav_title: Alertas de campaña
article_title: Alertas de campaña
page_order: 6

page_type: reference
description: "Este artículo de referencia ofrece un resumen de las alertas de campaña, sus beneficios y cómo configurarlas para darte tranquilidad."
tool: Campaigns
channel:
- email
- webhooks

---

# Alertas de campaña {#campaign-alerts}

> Queremos alertarte cuando algo no parece funcionar como se esperaba y darte la tranquilidad de que todo marcha sin problemas. Las alertas de umbral de Campaign te dan tranquilidad: sé la primera persona en saber si una Campaign importante envía más o menos mensajes de los que esperas.

¿Buscas la misma funcionalidad en un Canvas? Consulta [Alertas de umbral de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/canvas_threshold_alerts).

Las alertas de Campaign están disponibles para las siguientes Campaigns:

- Campaigns recurrentes programadas
- Campaigns basadas en acciones
- Campaigns desencadenadas por API

## Configuración de la alerta de tu campaña {#setting-up-your-campaign-alert}

Navega a la página de análisis de tu Campaign para empezar a configurar tu alerta. Cuando selecciones **Set Up Alert**, podrás especificar umbrales de alerta superiores e inferiores, así como los destinatarios y canales de la alerta.

![Cuadro de diálogo de monitoreo de Campaign con dos botones: Cancelar y Guardar.]({% image_buster /assets/img_archive/campaign_alerts.png %})

Para una Campaign recurrente programada, puedes establecer umbrales superiores e inferiores para los mensajes enviados cada vez que la Campaign se envía. Para una Campaign desencadenada, puedes establecer umbrales superiores e inferiores para la cantidad de mensajes enviados por hora y por día.

Puedes configurar una alerta por correo electrónico, una alerta por webhook o ambas. Las alertas por webhook pueden ser muy útiles, ya que te permiten enviar una alerta a un canal de Slack. Para más información sobre la integración de alertas de Campaign con Slack, consulta la documentación de Slack sobre [Envío de mensajes mediante webhooks entrantes](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/).

{% alert note %}
Al configurar alertas de Campaign para Campaigns futuras, es posible que recibas actualizaciones antes de que la Campaign comience y después de que termine. Esto se debe a que las alertas de Campaign seguirán enviándose hasta que la Campaign se detenga manualmente.
{% endalert %}

## Carga útil del webhook de alerta de Campaign {#campaign-alert-webhook-payload}

A continuación se muestra un ejemplo de carga útil para el cuerpo de un webhook de alerta de Campaign. Este ejemplo utiliza una alerta configurada para enviarse cuando los mensajes enviados caen por debajo de 500 para un envío determinado de Campaign.

```
{"text":"Your campaign 'Sample campaign' had fewer than 500 messages sent this run. It had 4 messages sent this run. See https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"data":{"url":"https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"app_group_name":"Sample workspace",
"campaign_name":"Sample campaign",
"campaign_api_id":"fe787bc5-d13f-4123-b22f-3bd48f9fc407","upper_threshold":0,"lower_threshold":500,"value":4}}
```

