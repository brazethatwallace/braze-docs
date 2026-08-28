---
nav_title: "POST: Crear nuevo alias de usuario"
article_title: "POST: Crear nuevo alias de usuario"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del endpoint Crear nuevo alias de usuario de Braze."

---
{% api %}
# Crear nuevo alias de usuario {#create-new-user-alias}
{% apimethod post %}
/users/alias/new
{% endapimethod %}

> Utiliza este endpoint para añadir nuevos alias de usuario para usuarios identificados existentes, o para crear nuevos usuarios no identificados.

Se pueden especificar hasta 50 alias de usuario por solicitud.

**Añadir un alias de usuario para un usuario existente** requiere incluir un `external_id` en el nuevo objeto alias de usuario. Si el `external_id` está presente en el objeto pero no hay ningún usuario con ese `external_id`, el alias no se añadirá a ningún usuario. Si `external_id` no está presente, se creará un usuario, pero será necesario identificarlo más tarde. Puedes hacerlo utilizando "Identificación de usuarios" y el endpoint `users/identify`.

La **creación de un nuevo usuario solo de alias** requiere que se omita `external_id` en el nuevo objeto alias de usuario. Una vez creado el usuario, utiliza el endpoint `/users/track` para asociar el usuario de solo alias con atributos, eventos y compras, y el endpoint `/users/identify` para identificar al usuario con un `external_id`.

Puedes enviar Campaigns activadas por API a usuarios mediante `user_alias` utilizando el endpoint [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns).

## Cuando `alias_label` y `alias_name` ya existen {#when-alias_label-and-alias_name-already-exist}

La combinación de `alias_label` y `alias_name` debe ser única en toda tu base de usuarios. Para más información, consulta [Alias de usuario]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases).

Si envías una solicitud en la que el par `alias_label` y `alias_name` ya existe para cualquier usuario (ya sea en el mismo usuario o en otro), el endpoint seguirá devolviendo una respuesta exitosa (por ejemplo, `"aliases_processed": 1`, `"message": "success"`). En ese caso, no se añade ningún alias nuevo al usuario de la solicitud. Dado que el par `alias_label` y `alias_name` ya está en uso, la solicitud no realiza ningún cambio, y puede parecer que el alias nunca se añadió al usuario en cuestión.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5cf18e64-fd02-452f-8c90-9a0f7c4d0487 {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitarás una [clave de API]({{site.baseurl}}/api/api_key) con el permiso `users.alias.new`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='users alias new' %}

## Cuerpo de la solicitud {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "user_aliases" : (required, array of new user alias object)
}
```

### Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `user_aliases` | Obligatorio | Matriz de nuevos objetos alias de usuario | Consulta [objeto alias de usuario]({{site.baseurl}}/api/objects_filters/user_alias_object).<br><br> Para más información sobre `alias_name` y `alias_label`, consulta nuestra documentación sobre [alias de usuario]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases).|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

### Cuerpo de la solicitud del endpoint con la especificación del nuevo objeto alias de usuario {#endpoint-request-body-with-new-user-alias-object-specification}

```json
{
  "external_id" : (optional, string),
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```

## Ejemplo de solicitud {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/alias/new' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "user_aliases" :[
    {
      "external_id": "external_identifier",
      "alias_name" : "example_name",
      "alias_label" : "example_label"
    }
  ]
}'
```

## Respuesta {#response}

Cuando se omite un alias porque la misma combinación de `alias_label` y `alias_name` ya existe para un usuario, el cuerpo de la respuesta puede seguir indicando éxito. Consulta [Cuando la etiqueta de alias y el nombre ya existen](#when-the-alias-label-and-name-already-exist) para más detalles.

```json
{
    "aliases_processed": 1,
    "message": "success"
}
```

## Solución de problemas {#troubleshooting}

### ¿Por qué mis atributos no se actualizan después de crear un alias de usuario con este endpoint? {#why-are-my-attributes-not-updating-after-i-create-a-user-alias-using-this-endpoint}

Esto suele ocurrir cuando a `/users/alias/new` le sigue una solicitud separada a `/users/track` que intenta actualizar atributos por alias. La solicitud de seguimiento puede procesarse antes de que Braze pueda resolver de forma consistente el nuevo par `alias_label` y `alias_name` a un perfil, por lo que los atributos no se aplican al usuario esperado.

**Enfoque recomendado:** Utiliza una única llamada a [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) solo cuando quieras crear un perfil de solo alias o actualizar un perfil mediante un alias que ya existe. En la matriz `attributes`, coloca `user_alias` y los campos de tu perfil en el mismo [objeto de atributos de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object) para que Braze resuelva al usuario y aplique la actualización en un solo paso.

Establece `_update_existing_only` en `false` cuando necesites crear un perfil de solo alias a partir de ese objeto. Si lo omites al usar `user_alias`, Braze utiliza de forma predeterminada el comportamiento de solo actualización y no crea el perfil de solo alias. Si el alias ya existe en un usuario de tu espacio de trabajo, la misma solicitud actualiza ese perfil con tus nuevos atributos.

No puedes usar `/users/track` para añadir un nuevo alias a un usuario existente identificado por `external_id`. En un objeto de atributos de usuario, `external_id` y `user_alias` son mutuamente excluyentes. Para añadir un alias a un usuario identificado, primero llama a `/users/alias/new`. Una vez que el alias esté vinculado, puedes actualizar ese perfil con `/users/track` mediante `external_id` o mediante el alias existente.

Por ejemplo, el siguiente cuerpo de `/users/track` crea un perfil de solo alias si el alias aún no existe, o actualiza el perfil existente que ya tiene ese alias:
```json
{
  "attributes": [
    {
      "user_alias": {
        "alias_name": "example@example.com",
        "alias_label": "email"
      },
      "_update_existing_only": false,
      "string_attribute": "test_alias_only_update"
    }
  ]
}
```

{% endapi %}