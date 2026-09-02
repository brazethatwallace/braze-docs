---
nav_title: "POST: Enviar correos electrónicos transaccionales utilizando la entrega desencadenada por la API"
article_title: "Enviar correos electrónicos transaccionales utilizando la entrega desencadenada por la API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artículo describe en detalle el endpoint de Braze para enviar mensajes de correo electrónico transaccional mediante entrega desencadenada por API."
---

{% api %}
# Enviar correos electrónicos transaccionales utilizando la entrega desencadenada por la API {#send-transactional-emails-using-api-triggered-delivery}
{% apimethod post %}
/transactional/v1/campaigns/{campaign_id}/send
{% endapimethod %}

> Utiliza este endpoint para enviar mensajes transaccionales inmediatos y puntuales a un usuario designado.

Este endpoint se utiliza junto con la creación de una [Campaign de correo transaccional]({{site.baseurl}}/api/api_campaigns/transactional_campaigns) de Braze y el ID de Campaign correspondiente.

{% alert important %}
El correo transaccional está disponible actualmente como parte de determinados paquetes de Braze. Ponte en contacto con tu CSM or administrador de éxito de cliente or administrador de éxito de cliente de Braze para obtener más detalles.
{% endalert %}

Similar al [endpoint Enviar Campaign desencadenada]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns), este tipo de Campaign te permite alojar contenido de mensajes dentro del panel de Braze, al tiempo que dictas cuándo y a quién se envía un mensaje a través de tu API. A diferencia del endpoint Enviar Campaign desencadenada, que acepta una audiencia o Segment al que enviar mensajes, una solicitud a este endpoint debe especificar un único usuario, ya sea mediante `external_user_id` o `user_alias`, ya que este tipo de Campaign está diseñado para la mensajería 1:1 de alertas como confirmaciones de pedidos o restablecimiento de contraseñas.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cec874e1-fa51-42a6-9a8d-7fc57d6a63bc {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, deberás generar una clave de API con el permiso `transactional.send`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='transactional email' %}

## Parámetros de la ruta {#path-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `campaign_id` | Obligatorio | Cadena | ID de la Campaign |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de la ruta" }

## Cuerpo de la solicitud {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_send_id": (optional, string) see the following request parameters,
  "trigger_properties": (optional, object) personalization key-value pairs that apply to the user in this request,
  "recipient": (required, object)
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User alias object) User alias of the user to receive message,
      "external_user_id": (optional, string) External identifier of user to receive message,
      "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
    }
}
```

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `external_send_id` | Opcional | Cadena | Una cadena compatible con Base64. Validada con la siguiente regex:<br><br> `/^[a-zA-Z0-9-_+\/=]+$/` <br><br>Este campo opcional te permite pasar un identificador interno para este envío en particular, que se incluye en los eventos enviados desde el postback de eventos HTTP transaccionales. Cuando se transmite, este identificador también se utiliza como clave de deduplicación, que Braze almacena durante 24 horas. <br><br>Pasar el mismo identificador en otra solicitud no da lugar a una nueva instancia de envío por parte de Braze durante 24 horas. |
| `trigger_properties` | Opcional | Objeto | Ver [propiedades del desencadenante]({{site.baseurl}}/api/objects_filters/trigger_properties_object). Pares clave-valor de personalización que se aplican al usuario en esta solicitud. |
| `recipient` | Obligatorio | Objeto | El usuario al que diriges este mensaje. Puede contener `attributes` y un único `external_user_id` o `user_alias`.<br><br>Ten en cuenta que si proporcionas un ID externo de usuario que aún no existe en Braze, al pasar cualquier campo al objeto `attributes` se creará este perfil de usuario en Braze y se enviará este mensaje al usuario recién creado. <br><br>Si envías varias solicitudes al mismo usuario con datos diferentes en el objeto `attributes`, los atributos `first_name`, `last_name` y `email` se actualizan de forma sincronizada y se incluyen en tu mensaje mediante plantillas. Los atributos personalizados no tienen esta misma protección, así que procede con cautela cuando actualices a un usuario a través de esta API y pases diferentes valores de atributos personalizados en rápida sucesión. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

## Ejemplo de solicitud {#example-request}

```
curl -X POST \
  -H 'Content-Type:application/json' \
  -H 'Authorization: Bearer YOUR-REST-API-KEY' \
  -d '{
        "external_send_id" : YOUR_BASE64_COMPATIBLE_ID
        "trigger_properties": {
          "example_string_property": YOUR_EXAMPLE_STRING,
          "example_integer_property": YOUR_EXAMPLE_INTEGER
        },
        "recipient": {
          "external_user_id": TARGETED_USER_ID_STRING
        }
      }' \
  https://rest.iad-01.braze.com/transactional/v1/campaigns/{campaign_id}/send
```

## Respuesta {#response}

El endpoint de envío de correo transaccional responde con el `dispatch_id` del mensaje, que representa la instancia de envío de este mensaje. Este identificador puede utilizarse junto con los eventos del postback de eventos HTTP transaccionales para rastrear el estado de un correo electrónico individual enviado a un único usuario.

### Ejemplos de respuestas {#example-responses}

```json
{
    "dispatch_id": A randomly-generated unique ID of the instance of this send
    "status": Current status of the message
    "metadata" : Object containing additional information about the send instance
}
```

## Solución de problemas {#troubleshooting}

El endpoint también puede devolver un código de error y un mensaje legible en algunos casos, la mayoría de los cuales son errores de validación. Estos son algunos errores comunes que puedes obtener al realizar solicitudes no válidas.

| Error | Solución de problemas |
| ----- | --------------- |
| `The campaign is not a transactional campaign. Only transactional campaigns may use this endpoint` | El ID de Campaign proporcionado no corresponde a una Campaign transaccional. |
| `The external reference has been queued.  Please retry to obtain send_id.` | El external_send_id se ha creado recientemente, prueba un nuevo external_send_id si tienes intención de enviar un nuevo mensaje. |
| `Campaign does not exist` | El ID de Campaign proporcionado no corresponde a una Campaign existente. |
| `The campaign is archived. Unarchive the campaign in order for trigger requests to take effect.` | El ID de Campaign proporcionado corresponde a una Campaign archivada. |
| `The campaign is paused. Resume the campaign in order for trigger requests to take effect.` | El ID de Campaign proporcionado corresponde a una Campaign en pausa. |
| `campaign_id must be a string of the campaign api identifier` | El ID de Campaign proporcionado no tiene un formato válido. |
| `Error authenticating credentials` | La clave de API proporcionada no es válida. |
| `Invalid whitelisted IPs `| La dirección IP que envía la solicitud no está en la lista blanca de IP (si se está utilizando). |
| `You do not have permission to access this resource` | La clave de API utilizada no tiene permiso para realizar esta acción. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solución de problemas" }

La mayoría de los endpoints de Braze tienen una implementación de límite de velocidad que devuelve un código de respuesta 429 si realizas demasiadas solicitudes. El endpoint de envío transaccional tiene una asignación por hora de pago que se mide en unidades (por ejemplo, 50 000 unidades por hora, dependiendo de tu paquete). No hay un límite de velocidad por endpoint independiente para este endpoint: puedes enviar más allá del volumen asignado, pero solo el volumen asignado está cubierto por el SLA; las solicitudes que superen esa asignación se envían, pero no están cubiertas por el SLA. Las solicitudes a este endpoint cuentan para tu [límite de velocidad de API externa general]({{site.baseurl}}/api/api_limits). Si superas ese límite (por ejemplo, 250 000 solicitudes por hora en todos los endpoints), Braze devuelve 429 y limita las solicitudes hasta que se restablece el límite. El recuento del volumen de transacciones se restablece cada hora. Ponte en contacto con soporte de Braze si necesitas más información sobre esta funcionalidad.

## Postback de eventos HTTP transaccionales {#transactional-http-event-postback}

{% multi_lang_include channels/transactional_email/http_event_postback.md %}

{% endapi %}