---
nav_title: Segment para Currents
article_title: Segment para Currents
page_order: 2
alias: /partners/segment_for_currents/
description: "Este artículo de referencia describe la asociación entre Braze Currents y Segment, una plataforma de datos de clientes que recopila y encamina información entre fuentes de tu pila de marketing."
page_type: partner
tool: Currents
search_tag: Partner

---

# Segment para Currents {#segment-for-currents}

> [Segment](https://segment.com) es una plataforma de datos de clientes que te ayuda a recopilar, limpiar y activar los datos de tus clientes. Este artículo de referencia ofrece un resumen de la conexión entre Braze Currents y Segment, y describe los requisitos y procesos para una implementación y uso adecuados.

La integración de Braze y Segment te permite aprovechar Braze Currents para exportar tus eventos de Braze a Segment y obtener análisis más profundos de las conversiones, la retención y el uso del producto.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Segment | Se necesita una [cuenta de Segment](https://app.segment.com/login) para beneficiarse de esta asociación. |
| Destino Braze | Ya debes haber [configurado Braze como destino]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/) en tu integración de Segment.<br><br>Esto incluye proporcionar el centro de datos de Braze y la clave de API REST correctos en tu [configuración de conexión]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings). |
| Currents | Para volver a exportar datos a Segment, debes tener configurado [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) en tu cuenta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración {#integration}

### Paso 1: Obtener la clave de escritura de Segment {#step-1-obtain-segment-write-key}

En tu dashboard de Segment, selecciona tu fuente de Segment. A continuación, ve a **Settings > API keys**. Aquí encontrarás la **Segment Write Key**.

{% alert warning %}
Es importante mantener actualizada tu clave de escritura de Segment. Si las credenciales de tu conector caducan, el conector dejará de enviar eventos. Si esto persiste durante más de **5 días**, los eventos del conector se eliminarán y los datos se perderán permanentemente.
{% endalert %}

### Paso 2: Crear un nuevo conector de Currents {#step-2-create-a-new-currents-connector}

1. En Braze, ve a **Integraciones de socios** > **Exportación de datos**.
2. Haz clic en **+ Create New Current** > **Segment Data Export**.
3. A continuación, proporciona el nombre de la integración, el correo electrónico de contacto, la clave de escritura de Segment y la región de Segment.

![La página de Segment Currents en Braze. Aquí puedes encontrar campos para el nombre de la integración, el correo electrónico de contacto, la región de Segment y la clave de API.]({% image_buster /assets/img/segment/segment_currents_integration_config.png %})

### Paso 3: Exportar eventos de interacción con mensajes {#step-3-export-message-engagement-events}

A continuación, selecciona los eventos de interacción con mensajes que deseas exportar. Consulta la siguiente tabla de eventos y propiedades de exportación. Todos los eventos enviados a Segment incluirán el `external_user_id` del usuario como `userId` y el `braze_id` del usuario como `anonymousId`.

Ten en cuenta que Braze solo envía datos de eventos de usuarios sin `external_user_id` si está marcada la opción **Include events from anonymous users**.

{% multi_lang_include early_access_beta_alert.md feature='Anonymous user export' %}

![Lista de todos los eventos de interacción con mensajes disponibles en la página de Segment Currents en Braze.]({% image_buster /assets/img/segment/segment_currents_data_config.png %})

Por último, selecciona **Launch Current**.

{% multi_lang_include alerts/warning_alerts.md alert='Segment Currents multiple connectors' %}

Para saber más, visita la [documentación](https://segment.com/docs/connections/sources/catalog/cloud-apps/braze/) de Segment.

## Actualizar tu Current {#updating-your-current}

{% multi_lang_include updating_currents.md %}

## Eventos de Currents compatibles {#supported-currents-events}

Braze admite la exportación a Segment de los siguientes datos enumerados en los glosarios de eventos de [comportamiento del usuario]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) y de [interacción con mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) de Currents:

### Comportamientos {#behaviors}
- Desinstalación: `users.behaviors.Uninstall`
- Suscripción (cambio de estado global): `users.behaviors.subscription.GlobalStateChange`
- Grupo de suscripción (cambio de estado): `users.behaviors.subscriptiongroup.StateChange`

### Campaigns
- Cancelación: `users_campaigns_abort`
- Conversión: `users.campaigns.Conversion`
- EnrollinControl: `users.campaigns.EnrollInControl`

### Canvas
- Cancelación: `users_canvas_abort`
- Conversión: `users.canvas.Conversion`
- Entrada: `users.canvas.Entry`
- Salida (audiencia coincidente, evento realizado)
  - `users.canvas.exit.MatchedAudience`
  - `users.canvas.exit.PerformedEvent`
- Paso del experimento (conversión, entrada dividida)
  - `users.canvas.experimentstep.Conversion`
  - `users.canvas.experimentstep.SplitEntry`

### Mensajes {#messages}
- Tarjeta de contenido (cancelar, clic, descartar, impresión, envío)
  - `users.messages.contentcard.Abort`
  - `users.messages.contentcard.Click`
  - `users.messages.contentcard.Dismiss`
  - `users.messages.contentcard.Impression`
  - `users.messages.contentcard.Send`
- Correo electrónico (cancelar, rebote, clic, entrega, marcar como correo no deseado, apertura, envío, rebote suave, cancelar suscripción)
  - `users.messages.email.Abort`
  - `users.messages.email.Bounce`
  - `users.messages.email.Click`
  - `users.messages.email.Delivery`
  - `users.messages.email.MarkAsSpam`
  - `users.messages.email.Open`
  - `users.messages.email.Send`
  - `users.messages.email.SoftBounce`
  - `users.messages.email.Unsubscribe`
- Mensaje dentro de la aplicación (cancelar, clic, impresión)
  - `users.messages.inappmessage.Abort`
  - `users.messages.inappmessage.Click`
  - `users.messages.inappmessage.Impression`
- Notificación push (cancelar, rebote, iOSforeground, apertura, envío)
  - `users.messages.pushnotification.Abort`
  - `users.messages.pushnotification.Bounce`
  - `users.messages.pushnotification.IosForeground`
  - `users.messages.pushnotification.Open`
  - `users.messages.pushnotification.Send`
- SMS (cancelar, envío del operador, entrega, fallo de entrega, recepción entrante, rechazo, envío, clic en enlace corto)
  - `users.messages.sms.Abort`
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.InboundReceive`
  - `users.messages.sms.Rejection`
  - `users.messages.sms.Send`
  - `users.messages.sms.ShortLinkClick`
- Webhook (cancelar, envío)
  - `users.messages.webhook.Abort`
  - `users.messages.webhook.Send`
- WhatsApp (cancelar, entrega, fallo, recepción entrante, lectura, envío)
  - `users.messages.whatsapp.Abort`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.InboundReceive`
  - `users.messages.whatsapp.Read`
  - `users.messages.whatsapp.Send`