---
nav_title: Enviar mensajes servicio de mensajes cortos
article_title: Envío de mensajes servicio de mensajes cortos mediante la REST or transferencia de estado representacional API
page_order: 2
page_type: reference
description: "Este artículo de referencia explica cómo enviar mensajes servicio de mensajes cortos utilizando la REST or transferencia de estado representacional API de Braze y una Campaña de API."
channel:
  - SMS
---

# Envío de mensajes servicio de mensajes cortos mediante la REST or transferencia de estado representacional API {#sending-sms-messages-using-the-rest-api}

> Utiliza la REST or transferencia de estado representacional API de Braze para enviar mensajes servicio de mensajes cortos transaccionales desde tu backend en tiempo real. Este enfoque te permite crear un servicio que envía mensajes servicio de mensajes cortos de forma programática, al tiempo que realiza el seguimiento de los análisis de entrega junto con tus otras Campaigns y Canvas en el dashboard de Braze.

Esto puede resultar especialmente útil para la mensajería transaccional de gran volumen cuyo contenido se define en tus sistemas backend. Por ejemplo, puedes notificar a los consumidores cuando reciban un mensaje de otro usuario, invitándolos a visitar tu sitio web y consultar su buzón de entrada.

Con este enfoque, puedes:

- Desencadenar mensajes servicio de mensajes cortos desde tu backend en tiempo real.
- Realizar un seguimiento de análisis junto con todas tus Campaigns y Canvas de marketing.
- Ampliar el caso de uso con características adicionales de Braze, como retrasos en los mensajes, reorientación de seguimiento y pruebas A/B.
- Opcionalmente, cambiar a la [entrega activada por API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) para definir tus plantillas de mensajes en el dashboard de Braze sin dejar de desencadenar los envíos desde tu backend.

Para enviar un mensaje servicio de mensajes cortos a través de la REST or transferencia de estado representacional API, debes configurar una Campaña de API en el dashboard de Braze y, a continuación, utilizar el punto de conexión [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) para enviar el mensaje.

## Requisitos previos {#prerequisites}

Para completar esta guía, necesitas:

| Requisito | Descripción |
| --- | --- |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave con el permiso `messages.send`. Para crear una, ve a **Configuración** > **API e identificadores** > **Claves de API**. |
| Grupo de suscripción servicio de mensajes cortos | Un grupo de suscripción servicio de mensajes cortos configurado en tu espacio de trabajo de Braze. |
| Servicio de backend | Un servicio backend o entorno de scripting capaz de realizar solicitudes HTTP POST a la REST or transferencia de estado representacional API de Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Paso 1: Crear una Campaña de API {#step-1-create-an-api-campaign}

1. En el dashboard de Braze, ve a **Mensajería** > **Campaigns**.
2. Selecciona **Crear campaña** y, a continuación, selecciona **API Campaigns**.
3. Introduce un nombre y una descripción para tu campaña, como «Notificación por mensaje servicio de mensajes cortos».
4. Añade etiquetas relevantes para su identificación y seguimiento.
5. Selecciona **Añadir canal de mensajería** y, a continuación, selecciona **servicio de mensajes cortos**.
6. Anota el **Campaign ID** y el **Message Variation ID** que se muestran en la página de la campaña. Necesitarás ambos valores al crear tu solicitud API.

## Paso 2: Enviar un mensaje servicio de mensajes cortos utilizando la API {#step-2-send-an-sms-message-using-the-api}

Crea una solicitud POST al punto de conexión [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages). Incluye el ID de la campaña, el ID de usuario externo del destinatario y el contenido del servicio de mensajes cortos en la carga útil de la solicitud.

{% alert important %}
Cada destinatario mencionado en `external_user_ids` debe existir ya en Braze. Los envíos solo por API no crean nuevos perfiles de usuario. Si necesitas crear usuarios como parte de un envío, utiliza [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) primero, o utiliza una [campaña activada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) en su lugar.
{% endalert %}

### Ejemplo de solicitud {#example-request}

```
POST YOUR_REST_ENDPOINT/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

Reemplaza `YOUR_REST_ENDPOINT` con la [URL del punto de conexión REST or transferencia de estado representacional]({{site.baseurl}}/api/basics#endpoints) de tu espacio de trabajo.

{% raw %}
```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "external_user_ids": ["user123"],
  "messages": {
    "sms": {
      "app_id": "YOUR_APP_ID",
      "subscription_group_id": "YOUR_SMS_SUBSCRIPTION_GROUP_ID",
      "message_variation_id": "YOUR_MESSAGE_VARIATION_ID",
      "body": "Hi {{${first_name}}}, you have a new message in your inbox. Check it out at https://yourwebsite.com/messages. Text STOP to opt out."
    }
  }
}
```
{% endraw %}

Reemplaza los valores de marcador de posición con tus ID reales. El campo `body` admite la [personalización Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid), por lo que puedes adaptar el contenido del mensaje a cada destinatario. Para obtener la lista completa de parámetros compatibles con el objeto de mensajería servicio de mensajes cortos, consulta [Objeto servicio de mensajes cortos]({{site.baseurl}}/api/objects_filters/messaging/sms_object).

Después de crear la solicitud, envía la solicitud POST desde tu servicio backend a la REST or transferencia de estado representacional API de Braze.

## Paso 3: Verifica tu integración {#step-3-verify-your-integration}

Una vez completada la configuración, verifica tu integración:

1. Envía una solicitud API tal y como se describe en el [paso 2](#step-2-send-an-sms-message-using-the-api), utilizando tu propio ID de usuario como destinatario.
2. Confirma que el mensaje servicio de mensajes cortos se ha entregado a tu teléfono.
3. En el dashboard de Braze, ve a la página de resultados de la campaña y confirma que el envío se ha registrado.
4. Supervisa de cerca los resultados a medida que amplías tu campaña.

## Consideraciones {#considerations}

- Confirma que tus campañas de servicio de mensajes cortos cumplen con las normativas pertinentes y los requisitos de los operadores. Incluye instrucciones para darse de baja (como «Envía STOP para darte de baja») en todos los mensajes. Para obtener más información, consulta [Leyes y normativas sobre servicio de mensajes cortos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations) y [Palabras clave para la adhesión voluntaria y la baja]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout).
- Utiliza las [características de personalización]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) de Braze para adaptar el contenido de los servicio de mensajes cortos a los consumidores individuales, incluyendo contenido dinámico y datos específicos del usuario.
- La REST or transferencia de estado representacional API de Braze ofrece [puntos de conexión de mensajería]({{site.baseurl}}/api/endpoints/messaging) adicionales para programar mensajes, activar campañas y mucho más.