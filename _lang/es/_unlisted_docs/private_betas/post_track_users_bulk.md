---
nav_title: "POST: Rastrear usuarios (masivo)"
layout: api_page
page_type: reference
hidden: true
permalink: /track_users_bulk/
description: "Este artículo describe los detalles del punto de conexión Rastrear usuarios (masivo)."
---

{% api %}
# Rastrear usuarios (masivo) {#track-users-bulk}
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/track/bulk
{% endapimethod %}

> Utiliza este punto de conexión para registrar eventos personalizados y compras, y actualizar atributos de perfiles de usuario de forma masiva.

{% alert important %}
Este punto de conexión se encuentra actualmente en fase beta. Ponte en contacto con tu director de cuentas de Braze si te interesa participar en la beta.
{% endalert %}

## Cuándo utilizar este punto de conexión {#when-to-use-this-endpoint}

De forma similar al [punto de conexión POST: Rastrear usuarios]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#prerequisites), puedes utilizar este punto de conexión para actualizar perfiles de usuario. Sin embargo, este punto de conexión es más adecuado para realizar actualizaciones masivas:

- **Solicitudes más grandes:** Este punto de conexión permite 10 000 usuarios por solicitud, lo que significa que tienes que hacer menos solicitudes para lograr tus necesidades de actualización masiva.
- **Priorización:** Durante condiciones de tráfico pico, las solicitudes de `/users/track` tendrán prioridad sobre las solicitudes de `/users/track/bulk`. Utilizar ambos puntos de conexión te proporciona más control sobre la ingesta de datos.

Considera utilizar este punto de conexión cuando estés rellenando muchos perfiles de usuario durante la incorporación o sincronizando grandes cantidades de perfiles de usuario como parte de una sincronización diaria.

{% alert note %}
A partir del 26 de mayo de 2025, este punto de conexión se puede utilizar para rastrear métricas de conversión, así como para desencadenar eventos de excepción, o Campaigns y Canvas basados en acciones. Este comportamiento es similar a cualquier otro método de ingesta de datos de Braze.
{% endalert %}

## Requisitos previos {#prerequisites}

Para utilizar este punto de conexión, necesitarás una clave de API con el permiso `users.track.bulk`.

Si estás utilizando la API para llamadas de servidor a servidor, es posible que necesites incluir en la lista de permitidos el punto de conexión (por ejemplo, `rest.iad-01.braze.com`) si estás detrás de un firewall. Consulta los [puntos de conexión por instancia]({{site.baseurl}}/api/basics/#endpoints) para obtener más información.

## Límite de velocidad {#rate-limit}

Aplicamos un límite de velocidad base de 5 solicitudes por segundo a este punto de conexión para todos los clientes.

Cada solicitud de `/users/sync/bulk` tiene un límite de carga útil de 4&nbsp;MB y puede contener hasta 10 000 objetos de evento, atributo o compra.

Cada objeto (matrices de eventos, atributos y compras) puede actualizar un usuario cada uno, lo que significa que se pueden actualizar hasta 10 000 usuarios diferentes en una sola solicitud. Un único perfil de usuario se puede actualizar con hasta 100 objetos en una sola solicitud.

{% alert note %}
Si necesitas que se aumente tu límite de velocidad, ponte en contacto con tu administrador del éxito del cliente.
{% endalert %}


## Cuerpo de la solicitud {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, array of attributes object),
  "events": (optional, array of event object),
  "purchases": (optional, array of purchase object),
}
```

### Parámetros de la solicitud {#request-parameters}

{% alert important %}
Para cada componente de solicitud enumerado en la siguiente tabla, se requiere uno de `external_id`, `user_alias`, `braze_id`, `email` o `phone`.
{% endalert %}

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `attributes` | Opcional | Matriz de objetos de atributos | Consulta [objeto de atributos de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Opcional | Matriz de objetos de eventos | Consulta [objeto de eventos]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Opcional | Matriz de objetos de compras | Consulta [objeto de compras]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Solicitudes de ejemplo {#example-requests}

### Actualizar 10 000 perfiles de usuario de forma masiva en una solicitud {#bulk-update-10000-user-profiles-in-one-request}

Puedes actualizar hasta 10 000 perfiles de usuario. Aquí tienes un ejemplo truncado en el que la solicitud consta de 10 000 objetos de atributos:

```json
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
                "asparagus",
            ]
        },

...

        {
            "external_id": "user10000",
            "string_attribute": "nuts",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "hazelnut",
                "pistachio"
            ]
        }
    ]
}'
```

Aquí tienes un ejemplo en el que la solicitud consta de objetos de atributos y de eventos:

```json
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
        },
...
        {
            "external_id": "user10000",
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2023-09-16T08:00:00+10:00",
            "properties": {
                "release": {
                    "studio": "FilmStudio",
                    "year": "1988"
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

### Mensajes correctos {#successful-messages}

Los mensajes correctos recibirán la siguiente respuesta:

```json
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this will return an integer of the number of external_ids with attributes that were queued to be processed,
  "events_processed": (optional, integer), if events are included in the request, this will return an integer of the number of events that were queued to be processed,
  "purchases_processed": (optional, integer), if purchases are included in the request, this will return an integer of the number of purchases that were queued to be processed,
}
```

#### Mensaje correcto con errores no fatales {#successful-message-with-non-fatal-errors}

Si tu mensaje es correcto pero tiene errores no fatales, como un objeto de evento no válido en una lista larga de eventos, recibirás la siguiente respuesta:

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

Si tu mensaje tiene un error fatal, recibirás la siguiente respuesta:

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

#### Códigos de respuesta de errores fatales {#fatal-error-response-codes}

Para los códigos de estado y los mensajes de error asociados que se devolverán si tu solicitud encuentra un error fatal, consulta [Errores fatales y respuestas]({{site.baseurl}}/api/errors/#fatal-errors).

Si recibes el error `provided external_id is blacklisted and disallowed`, tu solicitud puede haber incluido un "usuario ficticio". Para obtener más información, consulta [Bloqueo de correo no deseado]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking).

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Debo utilizar este punto de conexión o el `/users/track` normal? {#should-i-use-this-endpoint-or-regular-userstrack}

Recomendamos utilizar ambos.

- Para rellenos y sincronizaciones masivas de perfiles de usuario, utiliza el punto de conexión `/users/track/bulk`.
- Para casos de uso en tiempo real, utiliza el punto de conexión `/users/track`.

### ¿Qué identificadores puedo utilizar en /users/track/bulk? {#what-identifiers-can-i-use-in-userstrackbulk}

Se requiere uno de `external_id`, `braze_id`, `user_alias`, `email` o `phone`. Para más ejemplos, consulta nuestra documentación sobre el [objeto de atributos de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object/), el [objeto de eventos]({{site.baseurl}}/api/objects_filters/event_object/) o el [objeto de compras]({{site.baseurl}}/api/objects_filters/purchase_object/).

### ¿Puedo incluir atributos, eventos y compras en una sola solicitud? {#can-i-include-attributes-events-and-purchases-in-one-request}

Sí. Puedes construir tu solicitud con cualquier cantidad de objetos de atributos, eventos y compras, hasta 10 000 objetos por solicitud.


{% endapi %}