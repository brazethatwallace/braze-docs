---
nav_title: "WhatsApp y sistemas externos"
article_title: "WhatsApp y sistemas externos"
page_order: 2
description: "Este artículo de referencia proporciona una guía paso a paso para integrar Braze y WhatsApp con un sistema externo de IA o comunicación."
page_type: reference
alias: /whatsapp_external_system_integration/
channel:
  - WhatsApp
---

# Integrar Braze y WhatsApp con un sistema externo de IA o comunicación {#integrate-braze-and-whatsapp-with-an-external-ai-or-communication-system}

> Aprovecha el poder de los chatbots de IA y las transferencias a agentes en vivo en el canal de WhatsApp para optimizar tus operaciones de soporte al cliente. Al automatizar consultas rutinarias y hacer una transición fácilmente a agentes humanos cuando sea necesario, puedes mejorar significativamente los tiempos de respuesta y la experiencia del cliente en general.

## Requisitos previos {#prerequisites}

| Requisitos | Descripción |
| - | - |
| Sistema externo | Un sistema de IA o comunicación de terceros capaz de crear y administrar chatbots, sistemas automatizados de servicio al cliente mediante API, o ambos. |
| Integración de Braze y WhatsApp | Un número de WhatsApp administrado por Braze |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional con permisos de `campaigns.trigger.send`. Se puede crear en el dashboard de Braze yendo a **Configuración** > **Claves de API**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Cómo funciona {#how-it-works}

La integración entre Braze y el sistema externo de IA o comunicación funciona como una calle de doble sentido, donde Braze es el canal de comunicación y el sistema externo es la "inteligencia" que procesa los mensajes y formula las respuestas.

El flujo de trabajo de la integración se puede dividir en dos flujos clave:
**Flujo de entrada:** El mensaje de un usuario llega a Braze y luego se reenvía a tu sistema externo para su procesamiento.
**Flujo de salida:** Después de procesar el mensaje, tu sistema externo envía una respuesta a Braze, que luego entrega el mensaje al usuario final.

Para automatizar eficientemente esta comunicación, esta integración utiliza dos características clave de Braze: [Campaigns de webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook) y [Campaigns activadas por API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery).

![Arquitectura de la integración entre el canal de WhatsApp de Braze y un sistema externo.]({% image_buster /assets/img/whatsapp/external_system_architecture.png %})
## Configurar la integración {#configuring-the-integration}

### Paso 1: Crear una Campaign de webhook para mensajes de entrada {#step-1-create-a-webhook-campaign-for-inbound-messages}

Primero, crea una Campaign de webhook para establecer una forma de enviar los mensajes de WhatsApp recibidos por Braze a tu sistema externo.

1. En Braze, crea una Campaign de webhook.
2. En el creador de webhooks, selecciona **Redactar webhook**.
3. En el campo **Webhook URL**, introduce el punto de conexión de la API (URL) del sistema externo que recibirá el mensaje.
4. Selecciona **Raw text** para el cuerpo de la solicitud e introduce una carga útil con personalización que contenga el `external_id` y el número de teléfono del usuario, el contenido del mensaje y otra información relevante, como:

{% raw %}
```liquid
{
  "user_id": "{{${user_id}}}",
  "phone_number": "{{${phone_number}}}",
  "message": "{{whats_app.${inbound_message_body}}}"
}
```
{% endraw %}

{: start="5"}
5. En el paso **Planificación de entrega** del creador de tu Campaign, selecciona **Basada en acciones** para el tipo de entrega y **Send a WhatsApp inbound message** para el desencadenador de la Campaign.

![Entrega basada en acciones con un desencadenador de envío de un mensaje de entrada de WhatsApp.]({% image_buster /assets/img/whatsapp/inbound_message_trigger.png %})

{: start="6"}
6. Termina de redactar tu Campaign, luego guárdala y lánzala. Después de lanzar la Campaign, cada vez que se reciba un mensaje, Braze enviará un webhook a tu sistema externo.

### Paso 2: Crear una Campaign activada por API para mensajes de salida {#step-2}

A continuación, crea una Campaign activada por API para establecer una forma en que tu sistema externo envíe mensajes de vuelta a los usuarios a través de WhatsApp.

1. En Braze, crea una Campaign de WhatsApp.
2. En el creador de mensajes, selecciona **WhatsApp Template Message** o **Response Message**, y luego selecciona la plantilla o el diseño del mensaje de respuesta. Puedes seleccionar cualquier diseño de mensaje de respuesta porque el mensaje de entrada abrió la ventana de 24 horas de WhatsApp.

![Creador de mensajes con opciones para seleccionar el tipo de mensaje y el diseño del mensaje.]({% image_buster /assets/img/whatsapp/response_message_layout.png %})

{: start="3"}
3. Añade la propiedad de desencadenador de API al cuerpo del mensaje, como {% raw %}`{{api_trigger_properties.${external_system_msg+body}}}`{% endraw %}. Esto permite que tu sistema de IA rellene el mensaje que se enviará.

![Creador de mensajes con el cuerpo del mensaje que contiene propiedades de desencadenador.]({% image_buster /assets/img/whatsapp/api_trigger_properties.png %})

{: start="4"}
4. En el paso **Planificación de entrega** del creador de tu Campaign, selecciona **Basada en acciones** para el tipo de entrega.
5. Guarda la Campaign y toma nota del `campaign_id` único que Braze genera para esta Campaign. Necesitarás el ID para el siguiente paso.

### Paso 3: Conectar el sistema externo a la Campaign activada por API {#step-3-connect-the-external-system-to-the-api-triggered-campaign}

Por último, configura tu sistema externo para llamar a Braze y enviar la respuesta.

1. En el código de tu sistema externo, después de procesar el mensaje recibido y generar la respuesta, realiza una solicitud POST al punto de conexión `/messages/send` de Braze.
2. En el cuerpo de la solicitud `/messages/send`, incluye el `campaign_id` del [Paso 2](#step-2), el `external_id` del usuario y el contenido de la respuesta del sistema externo.
3. Usa la propiedad de desencadenador de API del [Paso 2](#step-2) para insertar la respuesta del sistema externo, y no olvides incluir tu clave de API en el encabezado de solicitud para la autenticación, como en este ejemplo de cURL:

{% raw %}
```bash
curl -X POST \
  -H 'Content-Type:application/json' \
  -H 'Authorization: Bearer a valid rest API key' \
  -d '{
    "campaign_id": "campaign_id",
    "recipients": [
      {
        "external_user_id": "external_id",
        "trigger_properties": {
          "external_system_msg_body": "your external system message"
        }
      }
    ]
  }' \
  {{Braze endpoint}}/campaigns/trigger/send
```
{% endraw %}

¡Ahora tienes una base sólida para construir un flujo de trabajo de chatbot de IA!

### Personalizar tu flujo de trabajo {#customizing-your-workflow}

Puedes ampliar la lógica de tu integración para:
- Usar diferentes palabras clave para desencadenar distintas Campaigns de webhook.
- Crear flujos de conversación más complejos con Campaigns activadas por API de varios pasos.
- Registrar información del chat en Braze como atributos personalizados para enriquecer el perfil de usuario y segmentar futuras Campaigns.