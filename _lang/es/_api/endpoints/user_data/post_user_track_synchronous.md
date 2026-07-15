---
nav_title: "POST: Crear y actualizar usuarios (sincrónico)"
article_title: "POST: Crear y actualizar usuarios (sincrónico)"
alias: /post_user_track_synchronous/
layout: api_page
page_order: 4.5
page_type: reference
description: "En este artículo se describen los detalles del endpoint sincrónico de seguimiento de usuarios de Braze."

---
{% api %}
# Crear y actualizar usuarios (sincrónico) {#create-and-update-users-synchronous}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/users/track/sync
{% endapimethod %}

> Utiliza este endpoint para registrar eventos personalizados y compras, y actualizar los atributos del perfil de usuario de forma sincrónica. Este endpoint funciona de forma similar al [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), que actualiza los perfiles de usuario de forma asíncrona.

{% alert important %}
Este endpoint se encuentra actualmente en **fase beta limitada**. Aunque por el momento no estamos añadiendo nuevos clientes a la versión beta, comunícaselo a tu director de cuentas de Braze si crees que esta característica podría ser útil para tu integración con Braze.
{% endalert %}

## Llamadas a la API síncronas y asíncronas {#synchronous-and-asynchronous-api-calls}

En una llamada asíncrona, la API devuelve el código de estado `201`, lo que indica que tu solicitud se ha recibido, comprendido y aceptado correctamente. Sin embargo, esto no significa que tu solicitud se haya completado en su totalidad.

En una llamada sincrónica, la API devuelve un código de estado `201` que indica que tu solicitud se ha recibido, comprendido, aceptado y completado correctamente. La respuesta a la llamada muestra campos seleccionados del perfil de usuario como resultado de la operación.

Este endpoint tiene un límite de velocidad menor que el endpoint `/users/track` (consulta [Límite de velocidad](#rate-limit)). Cada solicitud de `/users/track/sync` solo puede contener un objeto de evento, un objeto de atributo **o** un objeto de compra. Este endpoint debe reservarse para las actualizaciones del perfil de usuario en las que se necesite una llamada sincrónica. Para una implementación saludable, te recomendamos que utilices `/users/track/sync` y `/users/track` juntos.

Por ejemplo, si envías solicitudes consecutivas para el mismo usuario durante un breve período de tiempo, es posible que se produzcan condiciones de carrera con el endpoint asíncrono `/users/track`, pero con el endpoint `/users/track/sync` puedes enviar esas solicitudes en secuencia, cada una después de recibir una respuesta `2XX`.

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitarás una [clave de API]({{site.baseurl}}/api/api_key) con el permiso `users.track.sync`.

Es posible que los clientes que utilicen la API para llamadas de servidor a servidor tengan que incluir en la lista de permitidos `rest.iad-01.braze.com` si están detrás de un cortafuegos.

## Límite de velocidad {#rate-limit}

{% multi_lang_include api/user_track_custom_attributes_data_points.md endpoint="/users/track/sync" %}

Aplicamos un límite de velocidad base de 500 solicitudes por minuto a este endpoint para todos los clientes. Cada solicitud de `/users/track/sync` puede contener hasta un objeto de evento, un objeto de atributo o un objeto de compra. Cada objeto (evento, atributo y matrices de compra) puede actualizar un usuario cada uno.

## Cuerpo de la solicitud {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, one attributes object),
  "events": (optional, one event object),
  "purchases": (optional, one purchase object),
}
```

### Parámetros de la solicitud {#request-parameters}

{% alert important %}
Para cada componente de solicitud que se indica en la tabla siguiente, debes incluir uno de los siguientes: `external_id`, `user_alias`, `braze_id`, `email` o `phone`.
{% endalert %}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `attributes` | Opcional | Un objeto de atributos | Ver [objeto de atributos del usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrate-push-tokens) |
| `events` | Opcional | Un objeto de evento | Ver [objeto de eventos]({{site.baseurl}}/api/objects_filters/event_object) |
| `purchases` | Opcional | Un objeto de compra | Ver [objeto de compras]({{site.baseurl}}/api/objects_filters/purchase_object) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

## Respuestas {#responses}

Al utilizar los [parámetros de solicitud](#request-parameters) de este endpoint, deberías recibir una de las siguientes respuestas: un mensaje correcto o un mensaje con errores fatales.

### Mensaje correcto {#successful-message}

Los mensajes correctos devuelven la siguiente respuesta, que incluye información sobre los datos del perfil de usuario que Braze ha actualizado.

```json
{
    "users": (optional, object), the identifier of the user in the request. May be empty if no users are found and _update_existing_only key is set to true,
        "custom_attributes": (optional, object), the custom attributes as a result of the request. Braze lists only custom attributes from the request,
        "custom_events": (optional, object), the custom events as a result of the request. Braze lists only custom events from the request,
        "purchase_events": (optional, object), the purchase events as a result of the request. Braze lists only purchase events from the request,
    },
    "message": "success"
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

## Ejemplos de solicitudes y respuestas {#example-requests-and-responses}

### Actualizar un atributo personalizado por ID externo {#update-a-custom-attribute-by-external-id}

#### Solicitud {#request}

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "external_id": "xyz123",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ]
}'
```

#### Respuesta {#response}

```
{
    "users": [
        {
            "external_id": "xyz123",
            "custom_attributes": {
                "string_attribute": "fruit",
                "boolean_attribute_1": true,
                "integer_attribute": 25,
                "array_attribute": [
                    "banana",
                    "apple",
                ]
            }
        }
    ],
    "message": "success"
}
```

### Actualizar un evento personalizado por correo electrónico {#update-a-custom-event-by-email}

#### Solicitud

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "events": [
        {
            "email": "test@example.com",
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

#### Respuesta

```
{
    "users": [
        {
            "email": "test@example.com",
            "custom_events": [
                {
                "name": "rented_movie",
                "first": "2022-01-001T00:00:00.000Z",
                "last": "2022-12-06T18:20:45.000Z",
                "count": 10
                }
            ]
        }
    ],
    "message": "success"
}
```

### Actualizar un evento de compra por alias de usuario {#update-a-purchase-event-by-user-alias}

#### Solicitud

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "purchases" : [
    {
      "user_alias" : {
          "alias_name" : "device123",
          "alias_label" : "my_device_identifier"
      }
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "Completed Order",
      "currency" : "USD",
      "price" : 219.98,
      "time" : "2022-12-06T19:20:45+01:00",
      "properties" : {
          "products" : [
            {
              "name": "Monitor",
              "category": "Gaming",
              "product_amount": 19.99
            },
            {
              "name": "Gaming Keyboard",
              "category": "Gaming ",
              "product_amount": 199.99
            }
          ]
      }
   }
  ]
}'
```

#### Respuesta

```
{
    "users": [
        {
          "user_alias" : {
            "alias_name" : "device123",
            "alias_label" : "my_device_identifier"
          },
          "purchase_events": [
                {
                "product_id": "Completed Order",
                "first": "2013-07-16T19:20:30+01:00",
                "last": "2022-12-06T18:20:45.000Z",
                "count": 3
                }
            ]
        }
    ],
    "message": "success"
}
```

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Debo utilizar el endpoint asíncrono o sincrónico? {#should-i-use-the-asynchronous-or-synchronous-endpoint}

Para la mayoría de las actualizaciones de perfiles, el endpoint `/users/track` funciona mejor debido a su mayor límite de velocidad y flexibilidad, que te permite agrupar solicitudes. Sin embargo, el endpoint `/users/track/sync` es útil si experimentas condiciones de carrera debido a solicitudes rápidas y consecutivas para el mismo usuario.

### ¿Difiere el tiempo de respuesta del endpoint `/users/track`? {#does-the-response-time-differ-from-the-userstrack-endpoint}

Con una llamada sincrónica, la API espera hasta que Braze complete la solicitud para devolver una respuesta. Como resultado, las solicitudes sincrónicas tardan más tiempo en promedio que las solicitudes asíncronas a `/users/track`. Para la mayoría de las solicitudes, puedes esperar una respuesta en cuestión de segundos.

### ¿Puedo enviar varias solicitudes al mismo tiempo? {#can-i-send-multiple-requests-at-the-same-time}

Sí, siempre que las solicitudes sean para usuarios diferentes, o que cada solicitud actualice diferentes atributos, eventos o compras para un usuario.

Si envías varias solicitudes para un usuario, para el mismo atributo, evento o compra, Braze recomienda esperar una respuesta satisfactoria entre cada solicitud para evitar que se produzcan condiciones de carrera.

Si sigues observando un estado de perfil inconsistente al llamar a `/users/track` para el mismo usuario en rápida sucesión, cambia esas actualizaciones a `/users/track/sync` y envía una solicitud a la vez, esperando cada respuesta `2XX` antes de la siguiente. Ese orden es la forma admitida de evitar condiciones de carrera de lectura-después-de-escritura en bucles cerrados o workers paralelos.

### ¿Por qué el valor de respuesta no coincide con el de mi solicitud original? {#why-doesnt-the-response-value-match-the-one-in-my-original-request}

Aunque tu solicitud se ha completado, es posible que el valor de tu atributo personalizado no se haya actualizado. Esto puede ocurrir cuando la actualización de tu atributo personalizado supera el número máximo de caracteres, supera los límites de la matriz o si el usuario no existe en Braze y tienes `_update_existing_only = true`.

En estos casos, trata la respuesta como una indicación de que, aunque tu solicitud se completó, la actualización deseada no se ha realizado. Investiga las posibles razones mencionadas en [¿Por qué el valor de respuesta no coincide con el de mi solicitud original?](#why-doesnt-the-response-value-match-the-one-in-my-original-request).

{% endapi %}