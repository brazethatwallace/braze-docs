---
nav_title: "POST: Crear y actualizar usuarios (masivo)"
article_title: "POST: Crear y actualizar usuarios (masivo)"
search_tag: Endpoint
page_order: 4.25
layout: api_page
page_type: reference
alias:
  - /unlisted_docs/track_users_bulk_partners/
  - /api/endpoints/user_data/post_user_track_bulk_partners/
description: "Este artículo describe los detalles del punto de conexión masivo de seguimiento de usuarios."
---
{% api %}
# Crear y actualizar usuarios (masivo) {#create-and-update-users-bulk}
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/track/bulk
{% endapimethod %}

Utiliza este punto de conexión para registrar eventos personalizados y compras, y actualizar atributos de perfiles de usuario de forma masiva.

{% alert important %}
Este punto de conexión se encuentra actualmente en **beta limitada**. Aunque no estamos añadiendo nuevos clientes a la beta en este momento, comunícale a tu director de cuentas de Braze si crees que esta característica podría ser útil para tu integración con Braze.
{% endalert %}

## Cuándo usar este punto de conexión {#when-to-use-this-endpoint}

Al igual que el [punto de conexión `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), puedes usar este punto de conexión para actualizar perfiles de usuario. Este punto de conexión es más adecuado para actualizaciones masivas:

- **Solicitudes más grandes:** Envía hasta 1000 usuarios por solicitud, de modo que puedas hacer menos solicitudes para grandes rellenos de datos y sincronizaciones.
- **Priorización:** Durante condiciones de tráfico pico, las solicitudes a `/users/track` tienen prioridad sobre las solicitudes a `/users/track/bulk`.

Usa este punto de conexión cuando estés rellenando muchos perfiles de usuario durante la incorporación, o sincronizando grandes volúmenes de perfiles como parte de una sincronización diaria.

{% alert note %}
Los límites del objeto de solicitud del punto de conexión `/users/track` varían según el modelo de precios y la configuración. Usa `/users/track/bulk` para la ingesta masiva.
{% endalert %}

## Requisitos previos {#prerequisites}

Para usar este punto de conexión, necesitas una [clave de API]({{site.baseurl}}/api/api_key/) con el permiso `users.track.bulk`.

Si estás realizando llamadas de servidor a servidor detrás de un firewall, es posible que necesites incluir en la lista de permitidos tu punto de conexión REST de Braze (por ejemplo, `rest.iad-01.braze.com`). Para más información, consulta [Puntos de conexión de API]({{site.baseurl}}/api/basics/#api-definitions).

## Límite de velocidad {#rate-limit}

{% multi_lang_include api/user_track_custom_attributes_data_points.md endpoint="/users/track/bulk" %}

Para la mayoría de los clientes, este punto de conexión tiene un límite de velocidad base de 50 solicitudes por segundo.

Los clientes con contratos más recientes pueden tener en su lugar límites de ráfaga (por segundo) y estables (por hora) basados en los usuarios activos al mes contratados.

Cada solicitud a `/users/track/bulk` tiene un límite de carga útil de 2 MB y puede incluir hasta 1000 objetos en total entre atributos, eventos y compras, dependiendo de la política de límite de velocidad masivo de tu cuenta.

Cada objeto puede actualizar un usuario, por lo que una sola solicitud puede actualizar hasta el límite de objetos de solicitud de tu cuenta de usuarios diferentes. Además, cada solicitud puede contener un máximo de 100 objetos por perfil de usuario entre atributos, eventos y compras.

## Cuerpo de la solicitud {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, array of attributes object),
  "events": (optional, array of event object),
  "purchases": (optional, array of purchase object)
}
```

### Parámetros de la solicitud {#request-parameters}

{% alert important %}
Para cada objeto de solicitud, debes incluir uno de los siguientes: `external_id`, `user_alias`, `braze_id`, `email` o `phone`.
{% endalert %}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --- | --- | --- | --- |
| `attributes` | Opcional | Array de objetos de atributos | Consulta [objeto de atributos de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Opcional | Array de objetos de eventos | Consulta [objeto de eventos]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Opcional | Array de objetos de compras | Consulta [objeto de compras]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de la solicitud" }

## Ejemplos de solicitudes {#example-requests}

### Actualizar perfiles de usuario de forma masiva en una solicitud {#bulk-update-user-profiles-in-one-request}

Actualiza hasta el límite de objetos de solicitud de tu cuenta de perfiles de usuario en una sola solicitud.

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/bulk' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "user1",
      "string_attribute": "fruit",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": [
        "banana",
        "apple"
      ]
    },
    {
      "external_id": "user2",
      "string_attribute": "vegetables",
      "boolean_attribute_1": false,
      "integer_attribute": 25,
      "array_attribute": [
        "broccoli",
        "asparagus"
      ]
    }
  ]
}'
```

### Enviar atributos y eventos en una solicitud {#send-attributes-and-events-in-one-request}

Incluye atributos y eventos en la misma solicitud, hasta el límite total de objetos de tu cuenta.

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/bulk' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "user1",
      "string_attribute": "fruit",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": [
        "banana",
        "apple"
      ]
    }
  ],
  "events": [
    {
      "external_id": "user2",
      "app_id": "your_app_identifier",
      "name": "rented_movie",
      "time": "2022-12-06T19:20:45+01:00",
      "properties": {
        "release": {
          "studio": "FilmStudio",
          "year": "2022"
        },
        "cast": [
          {
            "name": "Actor1"
          },
          {
            "name": "Actor2"
          }
        ]
      }
    }
  ]
}'
```

## Respuestas {#responses}

### Mensaje de éxito {#successful-message}

Los mensajes exitosos devuelven la siguiente respuesta:

```json
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this returns an integer of the number of external IDs with attributes that Braze queued for processing,
  "events_processed": (optional, integer), if events are included in the request, this returns an integer of the number of events that Braze queued for processing,
  "purchases_processed": (optional, integer), if purchases are included in the request, this returns an integer of the number of purchases that Braze queued for processing
}
```

### Mensaje de éxito con errores no fatales {#successful-message-with-non-fatal-errors}

Si tu solicitud es exitosa pero tiene errores no fatales (por ejemplo, un objeto de evento no válido en un lote grande), recibirás la siguiente respuesta:

```json
{
  "message": "success",
  "errors": [
    {
      <minor error message>
    }
  ]
}
```

### Mensaje con errores fatales {#message-with-fatal-errors}

Si tu solicitud tiene un error fatal, recibirás la siguiente respuesta:

```json
{
  "message": <fatal error message>,
  "errors": [
    {
      <fatal error message>
    }
  ]
}
```

### Códigos de respuesta de errores fatales {#fatal-error-response-codes}

Para los códigos de estado y los mensajes de error asociados que Braze devuelve cuando tu solicitud tiene un error fatal, consulta [Errores fatales y respuestas]({{site.baseurl}}/api/errors/#fatal-errors).

Si recibes el error "provided external_id is blacklisted and disallowed", tu solicitud puede incluir un "usuario ficticio". Para más información, consulta [Bloqueo de correo no deseado]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking).

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Debo usar este punto de conexión o `/users/track`? {#should-i-use-this-endpoint-or-userstrack}

Usa ambos puntos de conexión según tu caso de uso:

- Para grandes rellenos de datos y sincronizaciones, usa `/users/track/bulk`.
- Para casos de uso en tiempo real, usa `/users/track`.

### ¿Qué identificadores puedo usar en `/users/track/bulk`? {#what-identifiers-can-i-use-in-userstrackbulk}

Para cada objeto de solicitud, incluye uno de los siguientes: `external_id`, `braze_id`, `user_alias`, `email` o `phone`.

### ¿Puedo incluir atributos, eventos y compras en una solicitud? {#can-i-include-attributes-events-and-purchases-in-one-request}

Sí. Incluye cualquier combinación de atributos, eventos y compras, hasta el límite combinado de objetos de solicitud de tu cuenta.

{% endapi %}