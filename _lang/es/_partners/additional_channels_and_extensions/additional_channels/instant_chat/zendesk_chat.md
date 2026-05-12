---
nav_title: Zendesk
article_title: Chat de Zendesk
description: "Aprende a integrar Zendesk Chat con Braze y a configurar una conversación bidireccional por SMS."
alias: /partners/zendesk_chat/
page_type: partner
search_tag: Partner

---

# Chat de Zendesk {#zendesk-chat}

> [Zendesk Chat](https://www.zendesk.com/service/messaging/) utiliza webhooks de cada plataforma para establecer una conversación bidireccional por SMS. Cuando un usuario solicita soporte, se crea un ticket en Zendesk. Las respuestas de los agentes se reenvían a Braze a través de una Campaign de SMS desencadenada por la API, y las respuestas de los usuarios se devuelven a Zendesk.

## Requisitos previos {#prerequisites}


| Requisito | Descripción |
|---|---|
| Una cuenta de Zendesk | Se requiere una cuenta de Zendesk para aprovechar esta integración.|
| Un token de autorización básica de Zendesk | Se utiliza un token de autorización básica de Zendesk para realizar una solicitud de webhook saliente de Braze a Zendesk.|
| Una clave de API REST de Braze  | Una clave de API REST de Braze con permisos `campaigns.trigger.send`. Se puede crear en el dashboard de Braze desde **Settings** > **API Keys**.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Casos de uso {#use-cases}

Mejora la eficiencia de la atención al cliente combinando las capacidades de SMS de Braze con las respuestas en vivo de los agentes de Zendesk para atender las consultas de los usuarios con asistencia humana de forma rápida.

## Integración de Zendesk Chat {#integrating-zendesk-chat}

### Paso 1: Crear un webhook en Zendesk {#step-1-create-a-webhook-in-zendesk}

1. En la consola para desarrolladores de Zendesk, ve a webhooks: {% raw %}`https://{{url}}.zendesk.com/admin/apps-integrations/webhooks/webhooks`{% endraw %}
2. En **Create Webhook**, selecciona **Trigger or automation**.
3. Para **Endpoint URL**, añade el punto de conexión **/campaign/trigger/send**.
4. En **Authentication**, selecciona **Bearer token** y añade la clave de API REST de Braze con permisos `campaigns.trigger.send`.

![Un ejemplo de webhook de Zendesk.]({% image_buster /assets/img/zendesk/instant_chat/chat1.png %}){: style="max-width:70%;"}

### Paso 2: Crear una Campaign de SMS salientes {#step-2-create-an-outbound-sms-campaign}

A continuación, crearás una Campaign de SMS que escuchará los webhooks de Zendesk y enviará una respuesta SMS personalizada a tus clientes.

#### Paso 2.1: Redacta tu mensaje {#step-21-compose-your-message}

Cuando Zendesk envía el contenido de un mensaje a través de la API, este tiene el siguiente formato:

```
**----------------------------------------------\n\n{Replier Name}, {Replier Date}\n\n{Message}**
```

Así que necesitamos extraer el detalle que queremos de esta cadena para mostrarlo en el mensaje, o de lo contrario el usuario verá todos los detalles.

![Un SMS de ejemplo sin formato.]({% image_buster /assets/img/zendesk/instant_chat/chat2.png %}){: style="max-width:40%;"}

En el cuadro de texto **Message**, añade el siguiente código Liquid y cualquier texto de exclusión u otro contenido estático:

{% raw %}
```liquid
{% assign body = {{api_trigger_properties.${msg_body}}} %}
{% assign msg = body | split: "
" %}
New message from Zendesk:
{{msg[2]}}

Feel free to respond directly to this number!
```
{% endraw %}

![Un SMS de ejemplo con formato.]({% image_buster /assets/img/zendesk/instant_chat/chat3.png %}){: style="max-width:70%;"}

#### Paso 2.2: Programar la entrega {#step-22-schedule-the-delivery}

Para el tipo de entrega, selecciona **API-Triggered delivery** y, a continuación, copia el ID de la Campaign, que se utilizará en los pasos siguientes.

![Entrega desencadenada por API]({% image_buster /assets/img/zendesk/instant_chat/chat4.png %}){: style="max-width:70%;"}

Por último, en **Delivery Controls**, activa la reelegibilidad.

![Reelegibilidad habilitada en "Delivery Controls".]({% image_buster /assets/img/zendesk/instant_chat/chat5.png %})

### Paso 3: Crear un desencadenante en Zendesk para reenviar las respuestas de los agentes a Braze {#step-3-create-a-trigger-in-zendesk-to-forward-agent-replies-to-braze}

Ve a **Objects and rules** > **Business rules** > **Triggers**.

1. Crea una nueva **categoría** (por ejemplo, **Trigger a message**).
2. Crea un nuevo **desencadenante** (por ejemplo, **Respond via SMS Braze**).
3. En **Conditions**, selecciona:
- **Ticket>Comment** está **Present and requester can see comment** para que el mensaje se desencadene cada vez que se incluya un nuevo comentario público en la actualización de un ticket
- **Ticket>Update** *no es* **Web service (API)** para que cuando un usuario envíe un mensaje desde Braze, no se reenvíe a su teléfono móvil. Solo se reenvían los mensajes procedentes de Zendesk.

![Respond via SMS Braze.]({% image_buster /assets/img/zendesk/instant_chat/chat6.png %}){: style="max-width:70%;"}

En **Actions**, selecciona **Notify by Webhook** y elige el punto de conexión que creaste en el paso 1. A continuación, especifica el cuerpo de la llamada a la API. Introduce el `campaign_id` del [paso 2.2](#step-22-schedule-the-delivery) en el cuerpo de la solicitud.

![Cuerpo JSON de respuesta vía SMS Braze.]({% image_buster /assets/img/zendesk/instant_chat/chat7.png %}){: style="max-width:70%;"}

{% raw %}
```liquid
{
    "campaign_id": "{{YOUR_CAMPAIGN_ID}}",
    "recipients": [
        {
            "external_user_id": "{{ticket.requester.custom_fields.braze_external_id}}",
			"trigger_properties": {
    "msg_body": "{{ticket.latest_public_comment_html}}"
		},
		"attributes": {
        "zendesk_ticket" : "{{ticket.id}}",
	"zendesk_ticket_open" : "true"
    }
        }
    ]
}
```
{% endraw %}


### Paso 4: Crear un desencadenante en Zendesk para actualizar a un usuario cuando se cierra un ticket {#step-4-create-a-trigger-in-zendesk-to-update-a-user-when-a-ticket-is-closed}

Si quieres notificar al usuario que el ticket se ha cerrado, crea una nueva Campaign en Braze con el cuerpo de respuesta de la plantilla.

![Actualizar a un usuario cuando se cierra un ticket.]({% image_buster /assets/img/zendesk/instant_chat/chat8.png %}){: style="max-width:70%;"}

Selecciona **API-Triggered delivery** y copia el ID de la Campaign.

A continuación, configura un desencadenante para notificar a Braze cuando se cierre el ticket:
- Categoría: **Trigger a message**
- En Conditions, selecciona **Ticket>Ticket Status** y cámbialo a **Solved**

![Configuración de ticket resuelto en Zendesk.]({% image_buster /assets/img/zendesk/instant_chat/chat9.png %}){: style="max-width:70%;"}

En **Actions**, selecciona **Notify by Webhook** y elige el segundo punto de conexión que acabas de crear. A partir de ahí, necesitamos especificar el cuerpo de la llamada a la API:

![Cuerpo JSON de ticket resuelto.]({% image_buster /assets/img/zendesk/instant_chat/chat10.png %}){: style="max-width:70%;"}

{% raw %}
```liquid
{
    "campaign_id": "{{YOUR_API_KEY}}",
    "recipients": [
        {
            "external_user_id": "{{ticket.requester.custom_fields.braze_external_id}}",
"trigger_properties": {
    "msg_body": "Your ticket has been closed"
		},
,
			"attributes": {
	"zendesk_ticket_open" : "false"
    }
        }
    ]
}
```
{% endraw %}

### Paso 5: Añadir un campo de usuario personalizado en Zendesk {#step-5-add-a-custom-user-field-in-zendesk}

En el Centro de administración, selecciona **People** en la barra lateral y, a continuación, selecciona **Configuration** > **User fields**. Añade el campo de usuario personalizado `braze_external_id`.

### Paso 6: Configurar el reenvío de SMS entrantes {#step-6-set-up-inbound-sms-forwarding}

A continuación, crearás dos nuevas Campaigns de webhook en Braze para poder reenviar los SMS entrantes de los clientes al buzón de entrada de Zendesk.

| Campaign           | Propósito                                                                              |
|--------------------|--------------------------------------------------------------------------------------|
| Campaign de webhook 1 | Crea un nuevo ticket en Zendesk.                                                     |
| Campaign de webhook 2 | Reenvía todas las respuestas SMS conversacionales enviadas por el cliente a Zendesk. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 6: Configurar el reenvío de SMS entrantes" }

#### Paso 6.1: Crear una categoría de palabras clave SMS {#step-61-create-an-sms-keyword-category}

En el dashboard de Braze, ve a **Audience**, elige tu **SMS subscription group** y, a continuación, selecciona **Add Custom Keyword**. Rellena los siguientes campos para crear una categoría de palabras clave SMS exclusiva para Zendesk.

| Campo            | Descripción                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------|
| Keyword Category | El nombre de tu categoría de palabras clave, como `ZendeskSMS1`.                                                                 |
| Keywords         | Tus palabras clave personalizadas, como `SUPPORT`.                                                                                  |
| Reply Message    | El mensaje que se envía cuando se detecta una palabra clave, como "Un representante del servicio de atención al cliente se pondrá en contacto contigo en breve." |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 6.1: Crear una categoría de palabras clave SMS" }

![Un ejemplo de categoría de palabras clave SMS en Braze.]({% image_buster /assets/img/zendesk/instant_chat/chat11.png %}){: style="max-width:70%;"}

#### Paso 6.2: Crea tu primera Campaign de webhook {#step-62-create-your-first-webhook-campaign}

En el dashboard de Braze, crea tu primera Campaign de webhook. Este mensaje indicará a Zendesk que se está solicitando soporte.

En el compositor del webhook, rellena los siguientes campos:
- Webhook URL: {% raw %}https://{{url}}.zendesk.com/api/v2/tickets{% endraw %}
- HTTP Method: POST
- Request Headers:
- Content-Type: application/json
- Authorization: Basic {{Token}}
- Request body:

{% raw %}
```liquid
{
  "ticket": {
    "subject": "Action Needed",
    "comment": {
      "body": "{{sms.${inbound_message_body}}}"
    },
"requester":{
"name": "{{${first_name}}} {{${last_name}}}",
"user_fields": {
"braze_external_id": "{{${user_id}}}"
}
},
    "priority": "normal",
    "type": "problem"
  }
}
```
{% endraw %}

![Un ejemplo de solicitud con los dos encabezados requeridos.]({% image_buster /assets/img/zendesk/instant_chat/chat12.png %}){: style="max-width:70%;"}


#### Paso 6.3: Programar la primera entrega {#step-63-schedule-the-first-delivery}

Para **Schedule Delivery**, selecciona **Action-Based Delivery** y, a continuación, elige **Send an SMS Inbound Message** para tu tipo de desencadenante. Añade también el grupo de suscripción SMS y la categoría de palabras clave que configuraste anteriormente.

![La página "Schedule Delivery" de la primera Campaign de webhook.]({% image_buster /assets/img/zendesk/instant_chat/chat13.png %})

En **Delivery Controls**, activa la reelegibilidad.

![Reelegibilidad seleccionada en "Delivery Controls" para la primera Campaign de webhook.]({% image_buster /assets/img/zendesk/instant_chat/chat14.png %})

#### Paso 6.4: Crea tu segunda Campaign de webhook {#step-64-create-your-second-webhook-campaign}

Configura una Campaign de webhook para reenviar los mensajes SMS restantes del usuario a Zendesk:

Como Zendesk envía el ID del ticket como una cadena, crea un bloque de contenido para convertir la cadena en un número entero y poder utilizarlo en el webhook de Zendesk.

{% raw %}
```liquid
{% assign var = {{custom_attribute.${zendesk_ticket}}} | to_i %}{{var}}
```
{% endraw %}

En el compositor de webhooks:
- Webhook URL: {% raw %}https://{{url}}.zendesk.com/api/v2/tickets/{{content_blocks.${to_int}}}.json{% endraw %}
- Request: PUT
- KVPs:
    - Content-Type: application/JSON
    - Authorization: Basic {{Token}}

Cuerpo de muestra:

{% raw %}
```liquid
{
  "ticket": {
    "comment": {
      "body": "Inbound message from {{${first_name}}} {{${last_name}}}: {{sms.${inbound_message_body}}}"
    }
}
}
```
{% endraw %}

#### Paso 6.5: Completa la configuración de la segunda Campaign de webhook {#step-65-complete-second-webhook-campaign-setup}
- Configura un desencadenante basado en acciones para los usuarios que envían un mensaje entrante en la categoría "Other".
- Configura los criterios de reelegibilidad.
- Añade las audiencias aplicables (en este caso, el atributo personalizado **zendesk_ticket_open** es **true**).

[2]: {% image_buster /assets/img/zendesk/instant_chat/chat2.png %}