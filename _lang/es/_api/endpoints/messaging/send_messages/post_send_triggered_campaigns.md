---
nav_title: "POST: Enviar campañas utilizando la entrega desencadenada por API"
article_title: "Enviar mensajes de Campaign mediante entrega desencadenada por API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artículo describe en detalle el endpoint de Braze para enviar campañas mediante entrega desencadenada por API."
---
{% api %}
# Enviar mensajes de Campaign mediante entrega desencadenada por API {#send-campaign-messages-using-api-triggered-delivery}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/campaigns/trigger/send
{% endapimethod %}

> Utiliza este endpoint para enviar mensajes inmediatos y puntuales a usuarios designados mediante la entrega desencadenada por API.

La entrega desencadenada por API te permite alojar el contenido de los mensajes dentro del panel de Braze, al tiempo que dictas cuándo se envía un mensaje y a quién mediante tu API.

Si te diriges a un Segment, se almacena un registro de tu solicitud en la [consola para desarrolladores](https://dashboard.braze.com/app_settings/developer_console/activitylog/). Para enviar mensajes con este endpoint, debes tener un [ID de Campaign]({{site.baseurl}}/api/identifier_types) creado al crear una [Campaign desencadenada por API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aef185ae-f591-452a-93a9-61d4bc023b05 {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, deberás generar una clave de API con el permiso `campaigns.trigger.send`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='send messages endpoints' %}

## Cuerpo de la solicitud {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "send_id": (optional, string) see send identifier,
  "trigger_properties": (optional, object) personalization key-value pairs that apply to all users in this request,
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' sends to only users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to `false`, message sends to the entire segment targeted by the campaign)
    [
      {
      // Either "external_user_id" or "user_alias" or "email" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "email": (optional, string) email address of user to receive message,
      "prioritization": (optional, array) prioritization array; required when using email,
      "trigger_properties": (optional, object) personalization key-value pairs that apply to this user (these key-value pairs override any keys that conflict with the parent trigger_properties),
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases; if set to `false`, an attributes object must also be included,
      "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
    }
  ],
  "attachments": (optional, array) array of JSON objects that define the files you need attached, defined by "file_name", "url", and optionally "basic_auth_credential",
    [
      {
       "file_name": (required, string) the name of the file you want to attach to your email, excluding the extension (for example, ".pdf"). Attach files up to 2 MB. This is required if you use "attachments",
       "url": (required, string) the corresponding URL of the file you want to attach to your email. The file name's extension is detected automatically from the URL defined, which should return the appropriate "Content-Type" as a response header. This is required if you use "attachments",
       "basic_auth_credential": (optional, string) the name of the stored basic authentication credential to use when the attachment URL requires a login,
      }
    ]
}
```

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Obligatorio | Cadena | Ver [identificador de Campaign]({{site.baseurl}}/api/identifier_types). |
| `send_id` | Opcional | Cadena | Ver [identificador de envío]({{site.baseurl}}/api/identifier_types). |
| `trigger_properties` | Opcional | Objeto | Ver [propiedades del desencadenante]({{site.baseurl}}/api/objects_filters/trigger_properties_object). Los pares clave-valor de personalización se aplican a todos los usuarios de esta solicitud. |
| `broadcast` | Opcional | Booleano | Debes establecer `broadcast` en verdadero cuando envíes un mensaje a todo el Segment configurado como público objetivo de la Campaign en el panel de Braze. Este parámetro está predeterminado como falso (a 31 de agosto de 2017). <br><br> Si `broadcast` tiene el valor true, no se puede incluir una lista `recipients`. Sin embargo, ten cuidado al configurar `broadcast: true`, ya que si lo haces involuntariamente puede que envíes tu mensaje a una audiencia mayor de la esperada. |
| `audience` | Opcional | Objeto de audiencia conectada | Ver [audiencia conectada]({{site.baseurl}}/api/objects_filters/connected_audience). Cuando incluyes `audience`, el mensaje solo se envía a los usuarios que coinciden con los filtros definidos, como los atributos personalizados y los estados de suscripción. |
| `recipients` | Opcional | Matriz | Ver [objeto de destinatarios]({{site.baseurl}}/api/objects_filters/recipient_object).<br><br>Si `send_to_existing_only` es `false`, debe incluirse un objeto `attributes`.<br><br>Puedes actualizar el estado del grupo de suscripción de un usuario incluyendo `subscription_groups` en el objeto `attributes` anidado. Para más detalles, consulta [Objeto de atributos de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object).<br><br>Si no se proporciona `recipients` y `broadcast` se establece en verdadero, el mensaje se envía a todo el Segment configurado como público objetivo de la Campaign en el panel de Braze.<br><br>Si `email` es el identificador, debes incluir [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email-addresses-and-phone-numbers) en el objeto de destinatarios. |
| `attachments` | Opcional | Matriz | Si `broadcast` está configurado como verdadero, no se puede incluir la lista `attachments`. <br><br>Cuando la URL de un archivo adjunto requiera inicio de sesión, incluye `basic_auth_credential` en ese archivo adjunto y establécelo con el nombre de una credencial de autenticación básica almacenada. Para configurar una credencial, consulta [Autenticación para archivos adjuntos de correo electrónico]({{site.baseurl}}/api/objects_filters/messaging/email_object#authentication-for-email-file-attachments). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

### Comportamiento de resolución de destinatarios {#recipient-resolution-behavior}

Esta sección explica cómo Braze selecciona un perfil de usuario para el envío y qué sucede cuando no se selecciona un perfil.

El estado del grupo de suscripción de un usuario puede actualizarse mediante la inclusión de un parámetro `subscription_groups` dentro del objeto `attributes`. Para más detalles, consulta [Objeto de atributos de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object).

#### Límites de destinatarios y creación de perfiles {#recipient-limits-and-profile-creation}

Obtén más información sobre cómo funcionan los límites de destinatarios y la creación de perfiles para este endpoint.

- La matriz `recipients` puede contener hasta 50 objetos, cada uno con una única cadena `external_user_id` y un objeto `trigger_properties`.
- Cuando `send_to_existing_only` es `true` (el valor predeterminado), Braze envía el mensaje solo a los usuarios existentes.
- Cuando `send_to_existing_only` es `false` y se proporciona un objeto `attributes`, Braze crea un nuevo usuario si no existe ninguno.
- **Los perfiles nuevos necesitan `attributes` con `send_to_existing_only: false`.** Braze ejecuta la creación o actualización previa al envío a partir del objeto `attributes` en el mismo destinatario. Si estableces `send_to_existing_only` en `false` pero omites `attributes` (o envías un objeto vacío), Braze no hidrata los datos del perfil de la misma manera, por lo que no obtienes el comportamiento combinado de "crear o actualizar usuario y luego enviar" para el que está diseñado este patrón.
- **Direccionamiento de correo electrónico y servicio de mensajes cortos.** Para la mayoría de los envíos de correo electrónico o servicio de mensajes cortos desencadenados por API a alguien que aún no está en Braze, incluye los campos de entrega que necesitas dentro de `attributes` (por ejemplo, `email`, o los atributos de teléfono que tu espacio de trabajo utiliza para servicio de mensajes cortos). También puedes establecer la pertenencia al grupo de suscripción o el estado de suscripción allí cuando el estado de adhesión voluntaria deba cambiar en la misma llamada.
- **Elegibilidad de la Campaign.** Después de que el perfil exista o se actualice, ese usuario aún debe coincidir con el público objetivo de la Campaign en el panel y las reglas de envío del canal (por ejemplo, adhesión voluntaria para correo electrónico) o Braze no envía el mensaje.
- Configurar `send_to_existing_only` en `false` no es compatible con los alias de usuario. No se pueden crear nuevos usuarios solo con alias a través de este endpoint. Para enviar a un usuario que solo tiene un alias de usuario, este debe existir ya en Braze.

#### Identificador de correo electrónico y empates de priorización {#email-identifier-and-prioritization-ties}

Cuando identificas destinatarios por correo electrónico, Braze utiliza `prioritization`. Braze envía solo cuando `prioritization` devuelve un perfil.

- Si utilizas `email` como identificador, Braze resuelve el destinatario usando `prioritization`.
- Si `prioritization` devuelve un empate, Braze no envía.
- Braze envía después de que se resuelva el empate y `prioritization` devuelva un perfil. Por ejemplo, si las actualizaciones de perfil cambian los campos de ordenación de un usuario, Braze envía una vez que `prioritization` pueda identificar de forma única un perfil (consulta [Comportamiento de reintentos y `send_to_existing_only`](#retry-behavior-and-send_to_existing_only)).
- Braze tampoco envía cuando `prioritization` no devuelve ningún perfil.

#### Comportamiento de reintentos y send_to_existing_only {#retry-behavior-and-send_to_existing_only}

Descubre qué sucede cuando `prioritization` no devuelve exactamente un perfil.

- Cuando `prioritization` no devuelve exactamente un perfil de usuario, Braze reintenta la resolución hasta 40 veces. Este comportamiento de reintento es esperado.
- La configuración de `send_to_existing_only` no cambia el comportamiento de empate de `prioritization`. El mismo comportamiento de empate y reintento se aplica tanto si esta configuración es `true` como `false`.

Si desencadenas una Campaign solo de correo electrónico para un destinatario identificado por `external_user_id` o `user_alias`, y ese perfil de usuario no tiene una dirección de correo electrónico en el momento de la llamada, Braze reintenta el envío durante aproximadamente 2 horas. Esto cubre el patrón habitual de crear un usuario y establecer su dirección de correo electrónico en rápida sucesión. Para enviar sin demora, incluye el atributo `email` dentro de `recipients[].attributes` para que la dirección se establezca en la misma llamada que el desencadenante.

{% alert note %}
El parámetro `segment_id` no es compatible con este endpoint. Para dirigirte a un Segment, configúralo en los ajustes de público objetivo de la Campaign en el panel de Braze y utiliza `"broadcast": true`, o bien utiliza el parámetro `audience` con los filtros de [audiencia conectada]({{site.baseurl}}/api/objects_filters/connected_audience).
{% endalert %}

## Ejemplo de solicitud {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "trigger_properties": "",
  "broadcast": false,
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "eye_color",
          "comparison": "equals",
          "value": "blue"
        }
      },
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_foods",
          "comparison": "includes_value",
          "value": "pizza"
        }
      },
      {
        "OR": [
          {
            "custom_attribute": {
              "custom_attribute_name": "last_purchase_time",
              "comparison": "less_than_x_days_ago",
              "value": 2
            }
          },
          {
            "push_subscription_status": {
              "comparison": "is",
              "value": "opted_in"
            }
          }
        ]
      },
      {
        "email_subscription_status": {
          "comparison": "is_not",
          "value": "subscribed"
        }
      },
      {
        "last_used_app": {
          "comparison": "after",
          "value": "2019-07-22T13:17:55+0000"
        }
      }
    ]
  },
  "recipients": [
    {
      "user_alias": {
        "alias_name" : "example_name",
        "alias_label" : "example_label"
      },
      "external_user_id": "external_user_identifier",
      "trigger_properties": "",
      "send_to_existing_only": true,
      "attributes": {
        "first_name" : "Alex"
      }
    }
  ],
  "attachments": [
    {
      "file_name" : "YourFileName",
      "url" : "https://exampleurl.com/YourFileName.pdf",
      "basic_auth_credential": "company_basic_auth_credential_name"
    }
  ]
}'
```

## Detalles de la respuesta {#response-details}

Las respuestas de los endpoints de envío de mensajes incluyen el `dispatch_id` del mensaje como referencia del envío. El `dispatch_id` es el ID del envío del mensaje, un ID único para cada transmisión enviada desde Braze. Al utilizar este endpoint, recibes un único `dispatch_id` para todo un conjunto de usuarios por lotes. Para más información sobre `dispatch_id`, consulta nuestra documentación sobre [el comportamiento de Dispatch ID]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id).

Si tu solicitud encuentra un error fatal, consulta [Errores y respuestas]({{site.baseurl}}/api/errors#fatal-errors) para ver el código de error y la descripción.

## Objeto de atributos para Campaigns {#attributes-object-for-campaigns}

Braze tiene un objeto de mensajería llamado `attributes` que te permite añadir, crear o actualizar atributos y valores para un usuario antes de enviarle una Campaign desencadenada por API. Usar el endpoint `campaign/trigger/send` como esta llamada a la API procesa el objeto de atributos de usuario antes de procesar y enviar la Campaign. Esto ayuda a minimizar el riesgo de que se produzcan problemas causados por [condiciones de carrera]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions).

{% alert tip %}
¿Buscas la versión Canvas de este endpoint? Consulta [Enviar mensajes Canvas mediante entrega desencadenada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases).
{% endalert %}

### ¿Por qué Liquid no se renderiza cuando lo pongo directamente en el cuerpo JSON? {#why-doesnt-liquid-render-when-i-put-it-directly-in-my-json-body}

Cuando el cuerpo de tu solicitud es JSON válido, Braze evalúa cualquier Liquid en la carga útil en el servidor. Si incrustas Liquid como cadenas sin procesar, pon entre comillas y escapa esas cadenas para que el cuerpo siga siendo JSON válido; por ejemplo, escapa las comillas dobles dentro de las cadenas. Si el cuerpo no pasa el análisis JSON, Braze devuelve un `400` antes de evaluar cualquier Liquid. Cuando sea posible, pasa los valores dinámicos a través de [`trigger_properties`]({{site.baseurl}}/api/objects_filters/trigger_properties_object) en lugar de incrustar Liquid directamente en la carga útil.

{% endapi %}