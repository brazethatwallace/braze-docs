---
nav_title: "POST: Enviar mensajes Canvas mediante entrega desencadenada por API"
article_title: "POST: Enviar mensajes Canvas mediante entrega desencadenada por API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artículo describe en detalle el punto de conexión de Braze para enviar Canvas mediante entrega desencadenada por API."

---
{% api %}
# Enviar mensajes Canvas mediante entrega desencadenada por API {#send-canvas-messages-using-api-triggered-delivery}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/canvas/trigger/send
{% endapimethod %}

> Utiliza este punto de conexión para enviar mensajes Canvas con entrega desencadenada por la API.

La entrega desencadenada por la API te permite almacenar el contenido de los mensajes en el panel de Braze, al tiempo que dictas cuándo se envía un mensaje y a quién mediante tu API.

Para poder enviar mensajes con este punto de conexión, debes tener un [ID de Canvas]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier) (que se crea cuando construyes un Canvas).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c9a8a5fe-a101-4755-99f2-73aa8fc146fe {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este punto de conexión, deberás generar una clave de API con el permiso `canvas.trigger.send`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='send messages endpoints' %}

## Cuerpo de la solicitud {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) see Canvas identifier,
  "context": (optional, object) Canvas context properties that apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if `recipients` is omitted,
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message sends to the entire segment targeted by the Canvas)
    [{
      // Either "external_user_id" or "user_alias" or "email" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "email": (optional, string) email address of user to receive message,
      "prioritization": (optional, array) prioritization array; required when using email,
      "context": (optional, object) Canvas context properties for this user; key-value pairs override any keys that conflict with the parent `context`,
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases; if set to `false`, an `attributes` object must also be included,
      "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
    }],
    ...
}
```

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `canvas_id` | Obligatorio | Cadena | Ver [identificador de Canvas]({{site.baseurl}}/api/identifier_types/). |
| `context` | Opcional | Objeto | Propiedades de contexto de Canvas para todos los destinatarios de esta solicitud. Los pares clave-valor de personalización se aplican a todos los usuarios a menos que un `context` por destinatario sobrescriba una clave. El objeto `context` puede tener un tamaño máximo de 50 KB. |
| `broadcast` | Opcional | Booleano | Debes establecer `broadcast` en true cuando envíes un mensaje a todo el segmento configurado como audiencia objetivo del Canvas en el panel de Braze. Este parámetro está predeterminado como false (desde el 31 de agosto de 2017). <br><br> Si `broadcast` tiene el valor true, no se puede incluir una lista `recipients`. Sin embargo, ten cuidado al configurar `broadcast: true`, ya que si lo haces involuntariamente puede que envíes tu mensaje a una audiencia mayor de la esperada. |
| `audience` | Opcional | Objeto de audiencia conectada | Ver [audiencia conectada]({{site.baseurl}}/api/objects_filters/connected_audience/). Cuando incluyes `audience`, el mensaje solo se envía a los usuarios que coinciden con los filtros definidos, como los atributos personalizados y los estados de suscripción. |
| `recipients` | Opcional | Matriz | Ver [objeto de destinatarios]({{site.baseurl}}/api/objects_filters/recipient_object/). <br><br>Si `send_to_existing_only` es `false`, se debe incluir un objeto `attributes` en el destinatario. <br><br>Si no se proporciona y `broadcast` está configurado en `true`, el mensaje se envía a todo el segmento configurado como audiencia objetivo del Canvas en el panel de Braze.<br><br> La matriz `recipients` puede contener hasta 50 objetos. Cada objeto debe incluir exactamente uno de `external_user_id`, `user_alias` o `email`, y puede incluir un objeto `context` por destinatario para las propiedades de contexto de Canvas (las claves por destinatario sobrescriben el `context` del nivel superior cuando entran en conflicto). <br><br>Si `email` es el identificador, debes incluir [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email) en el objeto de destinatarios. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

## Ejemplo de solicitud {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "context": {"product_name" : "shoes", "product_price" : 79.99},
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
      "external_user_id": "user_identifier",
      "send_to_existing_only": true,
      "attributes": {
          "first_name" : "Alex"
      }
    }
  ]
}'
```

## Detalles de la respuesta {#response-details}

Las respuestas de los puntos de conexión de envío de mensajes incluyen el `dispatch_id` del mensaje como referencia al envío del mensaje. El `dispatch_id` es el ID del envío del mensaje (ID único para cada "transmisión" enviada desde la plataforma Braze). Consulta [Comportamiento de Dispatch ID]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id/) para obtener más información.

### Ejemplo de respuesta correcta {#example-success-response}

El código de estado `201` podría devolver el siguiente cuerpo de respuesta. Si el Canvas está archivado, detenido o en pausa, no se envía a través de este punto de conexión.

```
{
  "notice": "The Canvas is paused. Resume the Canvas to ensure trigger requests will take effect.",
  "dispatch_id": "example_dispatch_id",
  "message": "success"
}
```

Si tu Canvas está archivado, verás este mensaje `notice`: "The Canvas is archived. Unarchive the Canvas to ensure trigger requests will take effect." Si tu Canvas no está activo, verás este mensaje `notice`: "The Canvas is paused. Resume the Canvas to ensure trigger requests will take effect."

Si tu solicitud encuentra un error fatal, consulta [Errores y respuestas]({{site.baseurl}}/api/errors/#fatal-errors) para ver el código de error y la descripción.

## Consideraciones {#considerations}

Ten en cuenta lo siguiente al realizar llamadas a la API para enviar mensajes de Canvas mediante la entrega desencadenada por API:

- **Envío a usuarios existentes**: Cuando `send_to_existing_only` se establece en `true` (el valor predeterminado), el mensaje solo se envía a los usuarios existentes en Braze.
- **Creación de nuevos usuarios**: Cuando `send_to_existing_only` se establece en `false`, debes incluir un objeto `attributes`. Si no existe un usuario con el ID especificado, Braze crea un usuario con ese ID y esos atributos antes de enviar el mensaje.
- **Los perfiles nuevos necesitan `attributes` con `send_to_existing_only: false`.** Braze ejecuta la creación o actualización previa al envío a partir del objeto `attributes` en el mismo destinatario. Si estableces `send_to_existing_only` en `false` pero omites `attributes` (o envías un objeto vacío), Braze no hidrata los datos del perfil de la misma manera, por lo que no obtienes el comportamiento combinado de "crear o actualizar usuario y luego enviar" para el que está diseñado este patrón.
- **Direccionamiento de correo electrónico y SMS.** Para la mayoría de los envíos desencadenados por API de correo electrónico o SMS a alguien que aún no está en Braze, incluye los campos de entrega que necesitas dentro de `attributes` (por ejemplo, `email`, o los atributos de teléfono que tu espacio de trabajo utiliza para SMS). También puedes establecer la pertenencia a un grupo de suscripción o el estado de suscripción allí cuando el estado de adhesión voluntaria deba cambiar en la misma llamada.
- **Elegibilidad del Canvas.** Después de que el perfil exista o se actualice, ese usuario aún debe coincidir con la audiencia objetivo del Canvas en el dashboard y las reglas de envío del canal (por ejemplo, adhesión voluntaria para correo electrónico) o Braze no envía el mensaje.
- **Limitación de alias de usuario**: El indicador `send_to_existing_only` no se puede utilizar con alias de usuario. Para enviar a un usuario que solo tiene un alias, este debe existir ya en Braze.
- **Segmentación por segmentos**: El parámetro `segment_id` no es compatible con este punto de conexión. Para dirigirte a un segmento, configúralo en los ajustes de audiencia objetivo del Canvas en el panel de Braze y utiliza `broadcast: true`, o utiliza el parámetro `audience` con los filtros de [audiencia conectada]({{site.baseurl}}/api/objects_filters/connected_audience/).
- **Segmentación combinada**: Cuando incluyes tanto el parámetro `recipients` como configuras un segmento de destino en el dashboard, el mensaje solo se envía a los perfiles de usuario que se especifican en la llamada a la API y que también coinciden con los filtros del segmento.
- **Llamadas de servidor a servidor**: Si estás realizando llamadas de servidor a servidor, es posible que tengas que incluir la URL de la API correspondiente en la lista de permitidos si estás protegido por un cortafuegos.

## Objeto de atributos para Canvas {#attributes-object-for-canvas}

Utiliza el objeto de mensajería `attributes` para añadir, crear o actualizar atributos y valores de un usuario antes de enviarle un Canvas desencadenado por la API utilizando el punto de conexión `canvas/trigger/send`. Esta llamada a la API procesa el objeto de atributos del usuario antes de procesar y enviar el Canvas. Esto ayuda a minimizar el riesgo de problemas causados por [condiciones de carrera]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions/). Sin embargo, de forma predeterminada, los grupos de suscripción no pueden actualizarse de esta forma.

{% alert note %}
¿Buscas la versión de Campaign de este punto de conexión? Consulta [Enviar mensajes de Campaign mediante entrega desencadenada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/).
{% endalert %}

{% endapi %}