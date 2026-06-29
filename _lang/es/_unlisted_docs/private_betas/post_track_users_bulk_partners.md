---
nav_title: "POST: Seguimiento de usuarios (masivo) para socios de Braze"
layout: api_page
page_type: reference
hidden: true
permalink: /track_users_bulk_partners/
description: "Si eres un socio de Braze, utiliza este punto de conexión para registrar eventos personalizados y compras, y actualizar atributos de perfil de usuario de forma masiva."
---

{% api %}
# Seguimiento de usuarios (masivo) para socios de Braze {#track-users-bulk-for-braze-partners}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/users/track/bulk
{% endapimethod %}

> Si eres un socio de Braze, utiliza este punto de conexión para registrar eventos personalizados y compras, y actualizar atributos de perfil de usuario de forma masiva.

{% alert important %}
Este punto de conexión está disponible para que los socios de Braze migren casos de uso masivos en su integración con Braze. Si tienes preguntas, ponte en contacto con [isv-support@braze.com](mailto:isv-support@braze.com).
{% endalert %}

## Cuándo usar este punto de conexión {#when-to-use-this-endpoint}

De forma similar al [punto de conexión POST: Seguimiento de usuarios]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#prerequisites), puedes usar este punto de conexión para actualizar perfiles de usuario. Sin embargo, este punto de conexión es más adecuado para realizar actualizaciones masivas:

- **Solicitudes más grandes:** Este punto de conexión permite 1000 usuarios por solicitud, lo que significa que tienes que hacer menos solicitudes para lograr tus necesidades de actualización masiva.
- **Priorización:** Durante condiciones de tráfico pico, las solicitudes de `/users/track` tendrán prioridad sobre las solicitudes de `/users/track/bulk`. Usar ambos puntos de conexión te proporciona más control sobre la ingesta de datos.

Considera usar este punto de conexión cuando estés rellenando muchos perfiles de usuario durante la incorporación o sincronizando grandes cantidades de perfiles de usuario como parte de una sincronización diaria.

{% alert note %}
Planeamos reducir el límite de objetos de `/users/track` de 225 a 5 para fomentar el uso de `/users/track/bulk` en su lugar. Tenlo en cuenta para que puedas asegurar que tu integración con Braze siga siendo compatible con futuras actualizaciones.
{% endalert %}

## Requisitos previos {#prerequisites}

Para usar este punto de conexión, necesitarás una [clave de API]({{site.baseurl}}/api/api_key/) con el permiso `users.track`. Este permiso proporciona acceso tanto a `/users/track` como a `/users/track/bulk`.

Dado que la mayoría de nuestros clientes compartidos ya estarán usando una clave de API con permisos `users.track` para su integración de socio con Braze, no necesitarán cambiar las claves de API a medida que migres tu integración para usar `/users/track/bulk`.

Si tus clientes están usando la API para llamadas de servidor a servidor, es posible que necesiten incluir el punto de conexión en la lista de permitidos (por ejemplo, `rest.iad-01.braze.com`) si estás detrás de un firewall. Consulta los [puntos de conexión por instancia]({{site.baseurl}}/api/basics/#endpoints) para más información.

## Límite de velocidad {#rate-limit}

Para la mayoría de los clientes, aplicamos un límite de velocidad base de 50 solicitudes por segundo a este punto de conexión.

Sin embargo, los clientes con contratos más recientes pueden recibir un límite de velocidad de ráfaga (por segundo) y estable (por hora), que está vinculado a su MAU contratado con Braze.

Para mejorar las interacciones en tiempo real con nuestra API, asegúrate de usar nuestros [encabezados de respuesta recomendados]({{site.baseurl}}/api/api_limits/#monitoring-your-rate-limits).

Cada solicitud de `/users/track/bulk` tiene un límite de carga útil de 2&nbsp;MB y puede contener hasta 1000 objetos de evento, atributo o compra.

Cada objeto (arrays de eventos, atributos y compras) puede actualizar un usuario cada uno, lo que significa que se puede actualizar un máximo de 1000 usuarios diferentes en una sola solicitud. Un solo perfil de usuario puede actualizar un máximo de 100 objetos en una sola solicitud.

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
Para cada componente de solicitud listado en la siguiente tabla, se requiere uno de `external_id`, `user_alias`, `braze_id`, `email` o `phone`.
{% endalert %}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `attributes` | Opcional | Array de objetos de atributos | Ver [objeto de atributos de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Opcional | Array de objetos de eventos | Ver [objeto de eventos]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Opcional | Array de objetos de compras | Ver [objeto de compras]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Solicitudes de ejemplo {#example-requests}

### Actualizar 1000 perfiles de usuario de forma masiva en una solicitud {#bulk-update-1000-user-profiles-in-one-request}

Puedes actualizar hasta 1000 perfiles de usuario usando el punto de conexión `/users/track/bulk`. Aquí tienes un ejemplo truncado donde la solicitud consta de 1000 objetos de atributos:

```javascript
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
            "external_id": "user1000",
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

Aquí tienes un ejemplo donde la solicitud consta de objetos de atributos y de eventos:

```javascript
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
            "external_id": "user1000",
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

```javascript
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this will return an integer of the number of external_ids with attributes that were queued to be processed,
  "events_processed": (optional, integer), if events are included in the request, this will return an integer of the number of events that were queued to be processed,
  "purchases_processed": (optional, integer), if purchases are included in the request, this will return an integer of the number of purchases that were queued to be processed,
}
```

#### Mensaje correcto con errores no fatales {#successful-message-with-non-fatal-errors}

Si tu mensaje es correcto pero tiene errores no fatales, como un objeto de evento no válido en una lista larga de eventos, recibirás la siguiente respuesta:

```javascript
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

```javascript
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

Si recibes el error `provided external\_id is blacklisted and disallowed`, tu solicitud puede haber incluido un `dummy user.` Para más información, consulta [Bloqueo de correo no deseado]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking).

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Debo usar este punto de conexión o `/users/track`? {#should-i-use-this-endpoint-or-userstrack}

Recomendamos usar ambos.

- Para rellenos y sincronizaciones masivas de perfiles de usuario, usa el punto de conexión `/users/track/bulk`.
- Para casos de uso en tiempo real, usa el punto de conexión `/users/track`.

{% alert note %}
Planeamos reducir el límite de objetos de `/users/track` de 225 a 5 para fomentar el uso de `/users/track/bulk` en su lugar. Tenlo en cuenta para que puedas asegurar que tu integración con Braze siga siendo compatible con futuras actualizaciones.
{% endalert %}

### ¿Qué identificadores puedo usar en `/users/track/bulk`? {#what-identifiers-can-i-use-in-userstrackbulk}

Se requiere uno de `external\_id`, `braze\_id`, `user\_alias`, `email` o `phone`. Consulta nuestra documentación sobre el [objeto de atributos de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object/), el [objeto de eventos]({{site.baseurl}}/api/objects_filters/event_object/) o el [objeto de compras]({{site.baseurl}}/api/objects_filters/purchase_object/) para más ejemplos.

### ¿Puedo incluir atributos, eventos y compras en una sola solicitud? {#can-i-include-attributes-events-and-purchases-in-one-request}

Sí. Puedes construir tu solicitud con cualquier cantidad de objetos de atributos, eventos y compras hasta el límite de 1000 objetos por solicitud.

{% endapi %}