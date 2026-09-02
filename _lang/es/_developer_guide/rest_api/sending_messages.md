---
nav_title: Enviar mensajes
article_title: Envío de mensajes mediante la REST or transferencia de estado representacional API
page_order: 1
page_type: reference
description: "Este artículo de referencia describe las dos formas de enviar mensajes mediante programación utilizando la REST or transferencia de estado representacional API de Braze."
---

# Envío de mensajes mediante la REST or transferencia de estado representacional API {#sending-messages-using-the-rest-api}

> Puedes enviar mensajes desde tu backend en tiempo real utilizando dos endpoints diferentes de Braze. Cada uno tiene una forma de solicitud diferente: uno requiere el contenido completo del mensaje en la solicitud; el otro requiere un ID de Campaign y envía el contenido definido en el panel.

Este enfoque funciona con cualquier canal de mensajería compatible con la API (WhatsApp, correo electrónico, servicio de mensajes cortos, push, Content Cards, webhooks y más).

## Dos formas de enviar {#two-ways-to-send}

| | [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) | [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) |
| --- | --- | --- |
| **ID de Campaign** | Opcional. Omítelo para enviar sin seguimiento de Campaign en el panel, o proporciona un ID de Campaign de API más `message_variation_id` en cada mensaje para realizar el seguimiento en el panel. | Obligatorio. |
| **Contenido del mensaje** | Debes incluir un objeto `messages` en la solicitud (por ejemplo, `messages.whats_app`, `messages.email`). | No aceptado. El contenido del mensaje se define en la Campaign en el panel de Braze. |
| **Caso de uso** | Envía un mensaje con el contenido completamente especificado en la solicitud de la API. | Desencadena una Campaign predefinida (contenido en el panel) para destinatarios específicos a través de la API. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Dos formas de enviar" }

Para obtener información detallada sobre las solicitudes y respuestas, consulta las referencias de los endpoints [Enviar mensajes inmediatamente (solo API)]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) y [Enviar Campaigns mediante entrega desencadenada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns).

---

## Opción 1: Enviar con el contenido del mensaje en la solicitud (`/messages/send`) {#option-1-send-with-message-content-in-the-request-messagessend}

Utiliza este endpoint cuando desees especificar el contenido completo del mensaje en la solicitud de API. **Debes** incluir un objeto `messages` (por ejemplo, `messages.whats_app`, `messages.email` o `messages.sms`). Puedes omitir `campaign_id` para enviar sin seguimiento de Campaign, o incluir un ID de Campaign de API y `message_variation_id` en cada mensaje para realizar un seguimiento de los envíos en el panel (consulta la [referencia del endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) para obtener más detalles).

**Obligatorio:** clave de API con el permiso `messages.send`.

{% alert important %}
Cada destinatario en `external_user_ids` debe existir ya en Braze. Para crear usuarios como parte de un envío, utiliza [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) primero, o utiliza la [Opción 2](#option-2-trigger-a-campaign-with-content-in-the-dashboard-campaignstriggersend) (Campaign desencadenada por API) en su lugar.
{% endalert %}

### Ejemplo: mensaje de plantilla de WhatsApp {#example-whatsapp-template-message}

```
POST YOUR_REST_ENDPOINT/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "external_user_ids": ["user123"],
  "messages": {
    "whats_app": {
      "app_id": "YOUR_APP_ID",
      "subscription_group_id": "YOUR_WHATSAPP_SUBSCRIPTION_GROUP_ID",
      "message_type": "template_message",
      "message": {
        "template_name": "new_message_received",
        "template_language_code": "en_US"
      }
    }
  }
}
```

Para obtener la especificación completa del objeto WhatsApp, consulta [Objeto WhatsApp]({{site.baseurl}}/api/objects_filters/messaging/whats_app_object).

{% alert note %}
El endpoint `/messages/send` solo admite plantillas de WhatsApp con encabezados TEXT o IMAGE. Para DOCUMENT, VIDEO u otros tipos de encabezados multimedia, utiliza el [endpoint de Campaign desencadenada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) o el panel de Braze.
{% endalert %}

### Ejemplo: correo electrónico {#example-email}

```json
{
  "external_user_ids": ["user123"],
  "messages": {
    "email": {
      "app_id": "YOUR_APP_ID",
      "subject": "Your order has shipped",
      "from": "no-reply@example.com",
      "body": "<p>Your order #12345 is on its way.</p>"
    }
  }
}
```

Para otros canales, consulta [Objetos de mensajería]({{site.baseurl}}/api/objects_filters#messaging-objects).

---

## Opción 2: Desencadenar una Campaign con contenido en el panel (`/campaigns/trigger/send`) {#option-2-trigger-a-campaign-with-content-in-the-dashboard-campaignstriggersend}

Utiliza este endpoint cuando el contenido del mensaje se cree en el panel de Braze (Campaign desencadenada por API). Envías un `campaign_id` **obligatorio** y los destinatarios; **no** envías un objeto `messages`.

**Obligatorio:** clave de API con el permiso `campaigns.trigger.send`.

### Paso 1: Crear una Campaign desencadenada por API {#step-1-create-an-api-triggered-campaign}

1. En el panel de Braze, ve a **Mensajería** > **Campaigns**.
2. Selecciona **Crear campaña** y, a continuación, **Campaign desencadenada por API** (no "API Campaign").
3. Añade tu canal de mensajería (WhatsApp, correo electrónico, servicio de mensajes cortos, etc.) y crea el contenido del mensaje en el panel.
4. Anota el **Campaign ID** (y el **Send ID** si utilizas varias variantes de mensaje). Los utilizarás en la solicitud de API.

Para obtener más información sobre cómo crear Campaigns desencadenadas por API, consulta [Entrega desencadenada por API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery).

### Paso 2: Desencadenar la Campaign a través de la API {#step-2-trigger-the-campaign-via-the-api}

Envía una solicitud POST a `/campaigns/trigger/send` con `campaign_id` y `recipients` (o `broadcast`/`audience`). No incluyas un objeto `messages`: el contenido proviene de la Campaign.

```
POST YOUR_REST_ENDPOINT/campaigns/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "recipients": [
    {
      "external_user_id": "user123"
    }
  ]
}
```

Para ver el cuerpo completo de la solicitud (incluidos `trigger_properties`, `send_to_existing_only`, `attributes`, etc.), consulta la referencia del endpoint [Enviar Campaigns mediante entrega desencadenada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns#request-body).

---

## Verifica tu integración {#verify-your-integration}

1. Envía una solicitud utilizando una de las opciones disponibles, con tu propio ID de usuario como destinatario.
2. Confirma que el mensaje se ha entregado.
3. Si utilizas la opción 2, comprueba la Campaign en el panel de Braze para confirmar que el envío se ha registrado.

## Consideraciones {#considerations}

- Utiliza las [características de personalización]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) de Braze para adaptar el contenido cuando sea posible.
- Asegúrate de que tu mensajería cumpla con las normativas pertinentes e incluya las opciones de exclusión voluntaria y los avisos de privacidad necesarios.
- Para obtener más información sobre los endpoints (programación, desencadenadores de Canvas, etc.), consulta [Endpoints de mensajería]({{site.baseurl}}/api/endpoints/messaging).