---
nav_title: "POST: Crear y actualizar usuarios"
article_title: "POST: Crear y actualizar usuarios"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Realizar un seguimiento de los usuarios de Braze."
toc_headers: h2
---
{% api %}
# Crear y actualizar usuarios {#create-and-update-users}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/users/track
{% endapimethod %}

> Utiliza este punto final para registrar eventos personalizados y compras, y actualizar los atributos del perfil de usuario.

{% multi_lang_include api/user_track_custom_attributes_data_points.md endpoint="/users/track" %}

Braze procesa los datos pasados a través de la API tal cual, y solo debes pasar deltas (datos que han cambiado) para minimizar el registro innecesario de puntos de datos.

## ¿Necesitas actualizar usuarios de forma masiva? {#need-to-update-users-in-bulk}

Utiliza el [punto final `/users/track/bulk`]({{site.baseurl}}/api/endpoints/user_data/post_user_track_bulk/) para enviar lotes más grandes y reducir el volumen de solicitudes.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4cf57ea9-9b37-4e99-a02e-4373c9a4ee59 {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/api_key/) con el permiso `users.track`.

Es posible que los clientes que utilicen la API para llamadas de servidor a servidor tengan que incluir en la lista de permitidos `rest.iad-01.braze.com` si están detrás de un cortafuegos.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='users track' %}

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
Para cada componente de la solicitud que aparece en la tabla siguiente, debes incluir uno de los siguientes: `external_id`, `user_alias`, `braze_id`, `email` o `phone`.
{% endalert %}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `attributes` | Opcional | Matriz de objetos de atributos | Ver [objeto de atributos del usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object/#migrating-push-tokens) |
| `events` | Opcional | Matriz de objetos de eventos | Ver [objeto de eventos]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Opcional | Matriz de objetos de compra | Ver [objeto de compras]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

### Resolución de identificadores {#identifier-resolution}

Cada objeto de solicitud debe incluir al menos un identificador. La siguiente tabla describe cómo Braze determina qué identificador utilizar para la búsqueda del perfil de usuario.

| Tipo de identificador | Identificadores | Comportamiento |
| --------------- | ----------- | -------- |
| Primario | `external_id`, `user_alias`, `braze_id` | Se utiliza para la búsqueda del perfil de usuario. Solo se permite un identificador primario por objeto de solicitud; incluir más de uno provoca que ese objeto sea rechazado. |
| Secundario | `email`, `phone` | Se utiliza para la búsqueda del perfil de usuario **solo** cuando no hay un identificador primario presente. Si se incluyen tanto `email` como `phone` sin un identificador primario, `email` tiene prioridad. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Resolución de identificadores" }

Cuando hay un identificador primario presente, cualquier valor de `email` o `phone` en el mismo objeto de solicitud se trata como atributo del perfil, no como identificador para la búsqueda de usuario. Por ejemplo, si una solicitud incluye tanto un `external_id` como un `email`:

- Braze busca el perfil de usuario por `external_id`.
- El valor de `email` se establece (o actualiza) como atributo en el perfil resuelto.

{% alert important %}
Incluir un identificador primario que no coincida con ningún perfil existente puede crear un perfil duplicado, incluso cuando el `email` o `phone` en la misma solicitud coincidan con un perfil existente. Para más información, consulta [¿Cómo evito crear perfiles de usuario duplicados?](#how-do-i-avoid-creating-duplicate-user-profiles).
{% endalert %}

## Ejemplos de solicitudes {#example-requests}

### Actualizar un perfil de usuario por dirección de correo electrónico {#update-a-user-profile-by-email-address}

Puedes actualizar el perfil de un usuario por dirección de correo electrónico utilizando el punto final `/users/track`.

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "email": "test@braze.com",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 26,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ],
    "events": [
        {
            "email": "test@braze.com",
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
        {
            "user_alias": {
                "alias_name": "device123",
                "alias_label": "my_device_identifier"
            },
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2013-07-16T19:20:50+01:00"
        }
    ],
    "purchases": [
        {
            "email": "test@braze.com",
            "app_id": "your_app_identifier",
            "product_id": "product_name",
            "currency": "USD",
            "price": 12.12,
            "quantity": 6,
            "time": "2017-05-12T18:47:12Z",
            "properties": {
                "color": "red",
                "monogram": "ABC",
                "checkout_duration": 180,
                "size": "Large",
                "brand": "Backpack Locker"
            }
        }
    ]
}'
```

### Actualizar un perfil de usuario por número de teléfono {#update-a-user-profile-by-phone-number}

Puedes actualizar un perfil de usuario por número de teléfono utilizando el punto final `/users/track`. Este punto final solo funciona si incluyes un número de teléfono válido.

{% alert important %}
Si incluyes una solicitud con tanto `email` como `phone`, Braze utiliza el correo electrónico como identificador.
{% endalert %}

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "phone": "+15043277269",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ],
}'
```
### Configurar grupos de suscripción {#set-subscription-groups}

Este ejemplo muestra cómo crear un usuario y establecer su grupo de suscripción dentro del objeto de atributos de usuario.

La actualización del estado de suscripción con este punto final actualiza al usuario especificado por su `external_id` (como Usuario1) y actualiza el estado de suscripción de cualquier usuario con el mismo correo electrónico que ese usuario (Usuario1).

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
  {
    "external_id": "user_identifier",
    "email": "example@email.com",
    "email_subscribe": "subscribed",
    "subscription_groups": [{
      "subscription_group_id": "subscription_group_identifier_1",
      "subscription_state": "unsubscribed"
      },
      {
        "subscription_group_id": "subscription_group_identifier_2",
        "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_3",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}'
```

{% alert note %}
Para los grupos de suscripción de SMS, cuando estableces el `subscription_state` de un grupo como `subscribed`, puedes incluir el parámetro opcional `use_double_opt_in_logic` establecido en `true` dentro de ese objeto de grupo de suscripción para que el usuario entre en el flujo de trabajo de [doble adhesión voluntaria de SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in/). Si se omite este parámetro o se establece en `false` cuando `subscription_state` es `subscribed`, el usuario se suscribe sin entrar en el flujo de trabajo de doble adhesión voluntaria. Este parámetro no se aplica cuando `subscription_state` se establece con otros valores, como `unsubscribed`.
{% endalert %}

### Ejemplo de solicitud para crear un usuario solo con alias {#example-request-to-create-an-alias-only-user}

Puedes utilizar el punto final `/users/track` para crear un usuario de solo alias estableciendo la clave `_update_existing_only` con un valor de `false` en el cuerpo de la solicitud. Si omites este valor, Braze no crea el perfil de usuario de solo alias. Utilizar un usuario de solo alias garantiza que exista un perfil con ese alias. Esto es especialmente útil al crear una integración, ya que evita que Braze cree perfiles de usuario duplicados.

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "_update_existing_only": false,
            "user_alias": {
                "alias_name": "example_name",
                "alias_label": "example_label"
            },
            "email": "email@example.com"
        }
    ],
}'
```


## Respuestas {#responses}

Al utilizar cualquiera de las solicitudes de API mencionadas, deberías recibir una de las tres respuestas generales siguientes: un [mensaje correcto](#successful-message), un [mensaje correcto con errores no fatales](#successful-message-with-non-fatal-errors) o un [mensaje con errores fatales](#message-with-fatal-errors).

### Mensaje correcto {#successful-message}

Los mensajes exitosos reciben la siguiente respuesta:

```json
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this returns an integer of the number of external_ids with attributes that Braze queued for processing,
  "events_processed": (optional, integer), if events are included in the request, this returns an integer of the number of events that Braze queued for processing,
  "purchases_processed": (optional, integer), if purchases are included in the request, this returns an integer of the number of purchases that Braze queued for processing,
}
```

### Mensaje correcto con errores no fatales {#successful-message-with-non-fatal-errors}

Si tu mensaje tiene éxito pero presenta errores no fatales, como un objeto de evento no válido en una larga lista de eventos, recibirás la siguiente respuesta:

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

En los mensajes de éxito, Braze sigue procesando todos los datos no afectados por un error en la matriz `errors`.

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

### Códigos de respuesta de error fatal {#fatal-error-response-codes}

Para conocer los códigos de estado y los mensajes de error asociados que devuelve Braze si tu solicitud encuentra un error fatal, consulta [Errores fatales y respuestas]({{site.baseurl}}/api/errors/#fatal-errors).

Si recibes el error "provided external_id is blacklisted and disallowed", es posible que tu solicitud haya incluido un "usuario ficticio". Para más información, consulta [Bloqueo de correo no deseado]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking).

### Errores específicos del punto final {#endpoint-specific-errors}

Los siguientes errores son específicos del punto final `/users/track` y se devuelven en la matriz `errors` de la respuesta. Utilízalos para solucionar problemas con objetos individuales en una solicitud.

| Error | Descripción |
|---|---|
| `BAD_DEVICE_ID` | El `device_id` para una importación de token debe tener entre 8 y 255 bytes. |
| `BAD_EMAIL_SUBSCRIPTION_STATE` | `email_subscribe` debe ser `subscribed`, `unsubscribed` u `opted_in`. |
| `BAD_LOCATION_UPDATE` | `current_location` debe ser un objeto que contenga `longitude` y `latitude`. |
| `BAD_PUSH_SUBSCRIPTION_STATE` | `push_subscribe` debe ser `subscribed`, `unsubscribed` u `opted_in`. |
| `BAD_PUSH_TOKEN_APP_ID` | El `app_id` en una importación de token debe ser un identificador de aplicación válido del espacio de trabajo actual. |
| `BAD_PUSH_TOKEN_IMPORT` | Las importaciones de tokens deben incluir tokens y excluir `external_id` y `braze_id`. |
| `BAD_PUSH_TOKEN_STRING` | El valor de `token` en una importación de token debe ser una cadena. |
| `BAD_PUSH_TOKEN_VALUE` | `push_tokens` debe ser una matriz de objetos. |
| `BAD_SUBSCRIPTION_GROUP_ARRAY` | `subscription_groups` debe ser una matriz. |
| `BAD_SUBSCRIPTION_GROUP_HASH` | Cada elemento de la matriz `subscription_groups` debe ser un objeto JSON con las claves `subscription_group_id` y `subscription_state`. |
| `BAD_SUBSCRIPTION_GROUP_ID` | `subscription_group_id` debe ser un UUID de grupo de suscripción válido. |
| `BAD_SUBSCRIPTION_GROUP_STATE` | `subscription_state` para un grupo de suscripción debe ser `subscribed` o `unsubscribed`. |
| `BLACKLISTED_EXTERNAL_USER_ID` | El `external_id` proporcionado está en la lista de bloqueados y no está permitido. |
| `EMAIL_BAD_FORMAT` | El valor proporcionado para `email` no es una dirección de correo electrónico válida. |
| `EXTERNAL_USER_ID_TOO_LARGE` | El `external_id` supera la longitud máxima permitida de 987 bytes. |
| `INVALID_ATTRIBUTE_EMAIL_SUBSCRIPTION_INFO` | `email_subscription_info` no es un atributo válido. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Errores específicos del punto final" }

## Preguntas frecuentes {#frequently-asked-questions}

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

### ¿Qué ocurre cuando se encuentran varios perfiles con la misma dirección de correo electrónico? {#what-happens-when-multiple-profiles-with-the-same-email-address-are-found}
Si existe el `external_id`, Braze da prioridad al perfil actualizado más recientemente con un ID externo para las actualizaciones. Si el `external_id` no existe, Braze da prioridad al perfil actualizado más recientemente para las actualizaciones.

### ¿Qué ocurre si no existe ningún perfil con la dirección de correo electrónico? {#what-happens-if-no-profile-with-the-email-address-exists}
Braze crea un perfil y un usuario de solo correo electrónico, y establece el campo de correo electrónico en test@braze.com, como se indica en el ejemplo de solicitud de actualización de un perfil de usuario por dirección de correo electrónico. Braze no crea un alias.

### ¿Cómo se utiliza `/users/track` para importar datos de usuario heredados? {#how-do-you-use-userstrack-to-import-legacy-user-data}
Puedes enviar datos a través de la API de Braze de un usuario que aún no haya utilizado tu aplicación móvil para generar un perfil de usuario. Si el usuario utiliza posteriormente la aplicación, toda la información posterior a su identificación mediante el SDK se fusiona con el perfil de usuario existente que creaste mediante la llamada a la API. Cualquier comportamiento de usuario registrado de forma anónima por el SDK antes de la identificación se pierde al fusionarse con el perfil de usuario existente generado por la API.

La herramienta de segmentación incluye a estos usuarios independientemente de si han interactuado o no con la aplicación. Si quieres excluir a los usuarios cargados mediante la API de usuario que aún no han interactuado con la aplicación, añade el filtro `Session Count > 0`.

### ¿Cómo evito crear perfiles de usuario duplicados? {#how-do-i-avoid-creating-duplicate-user-profiles}

Los perfiles duplicados pueden ocurrir cuando una solicitud incluye un identificador primario (como `external_id`) que no coincide con ningún perfil existente, junto con un valor de `email` o `phone` que sí coincide con un perfil existente. Dado que los identificadores primarios se utilizan para la búsqueda de usuarios, Braze crea un nuevo perfil para el `external_id` no reconocido en lugar de actualizar el perfil existente de solo correo electrónico o solo teléfono.

Para evitar duplicados:

- Al hacer la transición de usuarios de perfiles de solo correo electrónico o solo teléfono a perfiles identificados, utiliza el [punto final `/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) para asignar un `external_id` al perfil existente, en lugar de enviar ambos a `/users/track`.
- Si ya existen duplicados, fusiónalos utilizando el [punto final `/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/).

### ¿Cómo gestiona `/users/track` los eventos duplicados? {#how-does-userstrack-handle-duplicate-events}

Cada objeto de evento en la matriz de eventos representa una única ocurrencia de un evento personalizado por parte de un usuario en un momento determinado. Esto significa que cada evento ingestado en Braze tiene su propio ID de evento, por lo que los eventos "duplicados" se tratan como eventos separados y únicos.

### ¿Cómo gestiona `/users/track` los atributos personalizados anidados no válidos? {#how-does-userstrack-handle-invalid-nested-custom-attributes}

Cuando un atributo personalizado anidado contiene algún valor no válido (como formatos de hora no válidos o valores nulos), Braze elimina del procesamiento todas las actualizaciones de atributos personalizados anidados de la solicitud. Esto se aplica a todas las estructuras anidadas dentro de ese atributo específico. Para garantizar el éxito del procesamiento, comprueba que todos los valores de los atributos personalizados anidados son válidos antes de enviarlos.

### ¿Se garantiza que las solicitudes a `/users/track` se procesen en orden? {#are-requests-to-userstrack-guaranteed-to-be-processed-in-order}

Cuando realizas múltiples llamadas a la API `/users/track` en rápida sucesión, Braze no puede garantizar que las solicitudes se procesen en el orden exacto en que se envían o reciben. Esto se debe a que Braze utiliza procesamiento asíncrono para maximizar la velocidad y la flexibilidad.

Por ejemplo, si envías múltiples solicitudes de actualización para el mismo usuario en cuestión de segundos, algunas con valores de atributo nulos y otras con valores válidos, las solicitudes que contienen valores nulos pueden procesarse después de las solicitudes con valores válidos, incluso si se enviaron antes. Esto puede provocar que los valores de los atributos parezcan revertirse o no reflejar la actualización enviada más recientemente.

Para evitar condiciones de carrera al actualizar datos de usuario:

- **Agrupa las actualizaciones en una sola solicitud:** incluye todas las actualizaciones de atributos de un usuario en una sola llamada a la API en lugar de realizar llamadas consecutivas separadas.
- **Añade retrasos entre solicitudes:** si debes realizar llamadas separadas para el mismo usuario, añade un retraso (de unos segundos) entre solicitudes para permitir que la primera solicitud complete su procesamiento antes de enviar la siguiente.
- **Evita actualizaciones superpuestas para el mismo campo:** si dos solicitudes actualizan el mismo atributo con valores diferentes, envía esas actualizaciones en una sola solicitud o sepáralas con un retraso para reducir la posibilidad de resultados desordenados.

Para más información sobre condiciones de carrera y buenas prácticas, consulta [Condiciones de carrera]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions/).

### ¿Por qué la respuesta de `/users/track` es más lenta de lo esperado? {#why-is-my-userstrack-response-slower-than-i-expect}

Las llamadas exitosas a `/users/track` generalmente se aceptan rápidamente, pero Braze sigue procesando las actualizaciones de atributos, eventos y compras de forma asíncrona. La latencia percibida puede aumentar cuando las cargas útiles son grandes o cuando el enrutamiento de red hacia tu [punto final REST]({{site.baseurl}}/api/basics/#endpoints) es lento. Si necesitas un acuse de recibo síncrono por usuario o un orden más estricto entre llamadas, consulta [`/users/track/sync`]({{site.baseurl}}/api/endpoints/user_data/post_user_track_synchronous/) (**beta limitada**).

### ¿Cómo afectan los límites de velocidad a `/users/track`? {#how-do-rate-limits-affect-userstrack}

Cuando te acercas a tu [límite de velocidad](#rate-limit), recibes respuestas `429`. Para las respuestas que no son `429` en contratos compatibles, puedes utilizar los encabezados de respuesta `X-RateLimit-*` descritos en [Encabezados de límite de velocidad para usuarios activos al mes CY 24-25, MAU universal, MAU web y MAU móvil](#rate-limit-headers-for-monthly-active-users-cy-24-25-universal-mau-web-mau-and-mobile-mau) para ver cuánto queda de tu ventana actual.

### ¿Por qué recibo `400 Bad Request` con un error de sintaxis o análisis? {#why-do-i-get-400-bad-request-with-a-bad-syntax-or-parse-error}

Un HTTP `400` con un error de sintaxis o análisis generalmente significa que el cuerpo de la solicitud no es JSON válido. Las causas comunes incluyen comas finales, comentarios dentro del JSON, cadenas con comillas simples, una llave de apertura `{` adicional antes de la carga útil, o enviar un cuerpo que no es JSON mientras el encabezado `Content-Type` es `application/json`. Valida las cargas útiles con un linter de JSON antes de enviarlas, confirma que tu cliente HTTP codifica los objetos en JSON (en lugar de concatenar cadenas sin procesar) y confirma que el cuerpo está codificado en UTF-8. Para otras respuestas `400` (por ejemplo, límites de tamaño de carga útil y de objetos por solicitud), consulta [Errores fatales y respuestas]({{site.baseurl}}/api/errors/#fatal-errors) y la tabla de [Errores específicos del punto final](#endpoint-specific-errors) en esta página.

## Usuarios activos al mes CY 24-25, MAU universal, MAU web y MAU móvil {#monthly-active-users-cy-24-25-universal-mau-web-mau-and-mobile-mau}

Para los clientes con nuevos precios, los límites de velocidad se aplican a nivel de empresa. Los clientes pueden establecer límites de velocidad en el espacio de trabajo para los límites horarios, pero los límites de ráfaga se siguen compartiendo entre todos los espacios de trabajo.

Para los clientes que hayan comprado usuarios activos al mes CY 24-25, MAU universal, MAU web o MAU móvil, Braze gestiona diferentes límites de velocidad en su punto final `/users/track`:
- Los límites de velocidad por hora se establecen en función de la actividad prevista de ingesta de datos en tu cuenta, que puede corresponder al número de usuarios activos al mes que hayas comprado, al sector, a la estacionalidad o a otros factores.
- Además del límite horario, Braze aplica un límite de ráfaga al número de solicitudes que pueden enviarse cada tres segundos.
- Cada solicitud puede contener hasta 75 actualizaciones combinadas de objetos de atributo, evento o compra.

Los límites actuales basados en la ingesta prevista se pueden encontrar en el dashboard en **Configuración** > **API e identificadores** > **Panel de uso de la API**. Podemos modificar los límites de velocidad para proteger la estabilidad del sistema o permitir un mayor caudal de datos en tu cuenta. Ponte en contacto con el soporte de Braze o con tu administrador del éxito del cliente si tienes preguntas o dudas sobre el límite de solicitudes por hora o por segundo y las necesidades de tu empresa.

### Encabezados de límite de velocidad para usuarios activos al mes CY 24-25, MAU universal, MAU web y MAU móvil {#rate-limit-headers-for-monthly-active-users-cy-24-25-universal-mau-web-mau-and-mobile-mau}

Todas las respuestas sin límite de velocidad (como las que no son `429`) contienen los siguientes encabezados de respuesta HTTP que indican al cliente el estado de la ventana de límite de velocidad por hora. Utiliza estos encabezados para administrar tu tasa de solicitudes:

| Nombre del encabezado | Descripción |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| `X-RateLimit-Limit`     | El número de solicitudes permitidas por periodo de tiempo |
| `X-RateLimit-Remaining` | El número aproximado de solicitudes restantes dentro de una ventana |
| `X-RateLimit-Reset`     | El número de segundos restantes antes de que se reinicie la ventana actual |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Encabezados de límite de velocidad para usuarios activos al mes CY 24-25, MAU universal, MAU web y MAU móvil" }

Ten en cuenta que los encabezados `RateLimit-Limit`, `RateLimit-Remaining` y `RateLimit-Reset` no se devuelven cuando se produce un error HTTP `429`. Cuando se produce el error, esos encabezados se sustituyen por un encabezado `X-Ratelimit-Retry-After` que devuelve un número entero que indica el número de segundos que faltan para que puedas empezar a hacer solicitudes.

{% endapi %}