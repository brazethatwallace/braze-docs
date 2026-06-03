---
nav_title: "POST: Fusionar usuarios"
article_title: "POST: Fusionar usuarios"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto de conexión Fusionar usuarios de Braze."

---
{% api %}
# Fusionar usuarios {#merge-users}
{% apimethod post %}
/users/merge
{% endapimethod %}

> Utiliza este punto de conexión para fusionar un usuario con otro usuario.

Se pueden especificar hasta 50 fusiones por solicitud. Este punto de conexión es asíncrono.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d262b86d-cf84-46e2-b9d0-f882bb7078de {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este punto de conexión, necesitarás una [clave de API]({{site.baseurl}}/api/api_key/) con el permiso `users.merge`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='users merge' %}

## Cuerpo de la solicitud {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "merge_updates" : (required, array of objects)
}
```

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `merge_updates` | Obligatorio | Matriz | Una matriz de objetos. Cada objeto debe contener un objeto `identifier_to_merge` y un objeto `identifier_to_keep`, cada uno de los cuales debe hacer referencia a un usuario mediante `external_id`, `user_alias`, `phone` o `email`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Request parameters" }

### Comportamiento de la fusión {#merge-behavior}

El comportamiento que se documenta a continuación es válido para todas las características de Braze que **no** funcionan con Snowflake. Las fusiones de usuarios no se reflejarán en la pestaña **Messaging History**, Extensiones de segmento, Generador de consultas ni Currents.

{% alert important %}
El punto de conexión no garantiza la secuencia de actualización de los objetos de `merge_updates`.
{% endalert %}

Este punto de conexión fusiona los siguientes campos si no se encuentran en el usuario de destino.

- Nombre
- Apellido
- Direcciones de correo electrónico (a menos que estén [encriptadas]({{site.baseurl}}/user_guide/data/infrastructure/field_level_encryption/))
- Género
- Fecha de nacimiento
- Número de teléfono
- Zona horaria
- Ciudad de origen
- País
- Idioma
- Información del dispositivo
- Recuento de sesiones (la suma de las sesiones de ambos perfiles)
- Fecha de la primera sesión (Braze elige la fecha más temprana de las dos)
- Fecha de la última sesión (Braze elige la fecha más reciente de las dos)
- Atributos personalizados (Braze conserva los atributos personalizados existentes en el perfil de destino e incluye los atributos personalizados que no existían en el perfil de destino)
- Datos de eventos personalizados y eventos de compra
- Propiedades de eventos personalizados y de eventos de compra para la segmentación «X veces en Y días» (donde X<=50 e Y<=30)
- Resumen segmentable de eventos personalizados
  - Recuento de eventos (la suma de ambos perfiles)
  - Primera vez que ocurrió el evento (Braze elige la fecha más temprana de las dos)
  - Última vez que ocurrió el evento (Braze elige la fecha más reciente de las dos)
- Total de compras dentro de la aplicación en céntimos (la suma de ambos perfiles)
- Número total de compras (la suma de ambos perfiles)
- Fecha de la primera compra (Braze elige la fecha más temprana de las dos)
- Fecha de la última compra (Braze elige la fecha más reciente de las dos)
- Resúmenes de la aplicación
- Campos Last_X_at (Braze actualiza los campos si los campos del perfil huérfano son más recientes)
- Datos de interacción de Campaign (Braze selecciona los campos de fecha más recientes)
- Resúmenes del flujo de trabajo (Braze selecciona los campos de fecha más recientes)
- Historial de mensajes e interacción con mensajes
- Braze fusiona los datos de sesión solo si la aplicación existe en ambos perfiles de usuario.

{% alert note %}
Al fusionar usuarios, el uso del punto de conexión `/users/merge` funciona del mismo modo que el [método `changeUser()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser).
{% endalert %}

Braze gestiona de forma diferente tres tipos de usuarios durante la fusión: usuarios marcados para eliminación, usuarios de prueba y usuarios del Grupo de control global. Para más detalles, consulta [Comportamiento de la fusión de usuarios]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/merge_behavior/).

#### Comportamiento de la fecha de eventos personalizados y la fecha de eventos de compra {#custom-event-date-and-purchase-event-date-behavior}

Estos campos fusionados actualizan los filtros «para X eventos en Y días». Para los eventos de compra, estos filtros incluyen «número de compras en Y días» y «dinero gastado en los últimos Y días».

### Fusionar usuarios por correo electrónico o número de teléfono {#merging-users-by-email-or-phone-number}

Si se especifica `email` o `phone` como identificador, debes incluir un valor adicional de `prioritization` en el identificador. `prioritization` debe ser una matriz ordenada que especifique qué usuario fusionar si se encuentran varios usuarios. Esto significa que, si más de un usuario coincide a partir de una priorización, la fusión no se produce.

Los valores permitidos para la matriz son:

- `identified`
- `unidentified`
- `most_recently_updated` (se refiere a dar prioridad al usuario actualizado más recientemente)
- `least_recently_updated` (se refiere a dar prioridad al usuario actualizado menos recientemente)

En la matriz de priorización solo puede existir una de las siguientes opciones a la vez:

- `identified` se refiere a dar prioridad a un usuario con un `external_id`
- `unidentified` se refiere a dar prioridad a un usuario sin un `external_id`

{% alert important %}
Si ambos perfiles tienen números de teléfono no válidos, Braze no los fusiona. Los números no válidos no se almacenan en formato E.164 y el proceso de fusión no combina esos perfiles. El punto de conexión sigue devolviendo `202 Accepted` con un mensaje de éxito, por lo que la respuesta HTTP no indica que la fusión se omitió. Corrige los números de teléfono en uno o ambos perfiles antes de fusionar.
{% endalert %}

## Ejemplos de solicitudes {#example-requests}

### Solicitud básica {#basic-request}

Este es un cuerpo de solicitud básico para mostrar el patrón de la solicitud.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "external_id": "old-user1"
      },
      "identifier_to_keep": {
        "external_id": "current-user1"
      }
    },
    {
      "identifier_to_merge": {
        "email": "user1@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep":  {
        "email": "user2@braze.com",
        "prioritization": ["identified", "most_recently_updated"]
      }
    },
    {
      "identifier_to_merge": {
        "user_alias": {
          "alias_name": "old-user2@example.com",
          "alias_label": "email"
        }
      },
      "identifier_to_keep": {
        "user_alias": {
          "alias_name": "current-user2@example.com",
          "alias_label": "email"
        }
      }
    }
  ]
}'
```

### Fusionar usuario no identificado {#merging-unidentified-user}

La siguiente solicitud fusionaría el usuario no identificado actualizado más recientemente con la dirección de correo electrónico `john.smith@braze.com` con el usuario con ID externo `john`. En este ejemplo, el uso de `most_recently_updated` filtra la consulta a un usuario no identificado. Por lo tanto, si hubiera dos usuarios no identificados con esta dirección de correo electrónico, solo uno se fusionaría con el usuario que tiene el ID externo `john`.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep": {
        "external_id": "john"
      }
    }
  ]
}'
```

### Fusionar usuario no identificado en usuario identificado {#merging-unidentified-user-into-identified-user}

El siguiente ejemplo fusiona el usuario no identificado actualizado más recientemente con la dirección de correo electrónico `john.smith@braze.com` con el usuario identificado actualizado más recientemente con la dirección de correo electrónico `john.smith@braze.com`.

El uso de `most_recently_updated` filtra las consultas a un usuario (un usuario no identificado para `identifier_to_merge` y un usuario identificado para `identifier_to_keep`).

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep": {
        "email": "john.smith@braze.com",
        "prioritization": ["identified", "most_recently_updated"]
      }
    }
  ]
}'
```

### Fusionar un usuario no identificado sin incluir la priorización most_recently_updated {#merging-an-unidentified-user-without-including-the-most_recently_updated-prioritization}

Si hay dos usuarios no identificados con la dirección de correo electrónico `john.smith@braze.com`, esta solicitud de ejemplo no fusiona ningún usuario porque hay dos usuarios no identificados con esa dirección de correo electrónico. Esta solicitud solo funciona si hay un único usuario no identificado con la dirección de correo electrónico `john.smith@braze.com`.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified"]
      },
      "identifier_to_keep": {
        "external_id": "john"
      }
    }
  ]
}'
```

## Respuesta {#response}

Hay dos respuestas de código de estado para este punto de conexión: `202` y `400`.

### Ejemplo de respuesta satisfactoria {#example-success-response}

El código de estado `202` podría devolver el siguiente cuerpo de respuesta.

```json
{
  "message": "success"
}
```

### Ejemplo de respuesta de error {#example-error-response}

El código de estado `400` podría devolver el siguiente cuerpo de respuesta. Consulta la sección [Solución de problemas](#troubleshooting) para obtener más información sobre los errores que puedes encontrar.

```json
{
  "message": "'merge_updates' must be an array of objects"
}
```

## Solución de problemas {#troubleshooting}

En la tabla siguiente se enumeran los posibles mensajes de error que pueden aparecer.

| Error | Solución de problemas |
| --- | --- |
| `'merge_updates' must be an array of objects` | Comprueba que `merge_updates` es una matriz de objetos. |
| `a single request may not contain more than 50 merge updates` | Solo puedes especificar hasta 50 actualizaciones de fusión en una única solicitud. |
| `identifiers must be objects with an 'external_id' property that is a string, 'user_alias' property that is an object, 'email' property that is a string, or 'phone' property that is a string` | Comprueba los identificadores de tu solicitud. |
| `'merge_updates' must only have 'identifier_to_merge' and 'identifier_to_keep'` | Comprueba que `merge_updates` solo contiene los dos objetos `identifier_to_merge` e `identifier_to_keep`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting" }

{% endapi %}