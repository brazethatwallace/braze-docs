---
nav_title: "POST: Crear relación de usuario"
article_title: "POST: Crear relación de usuario"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Este artículo describe los detalles del endpoint Crear relación de usuario."
---
{% api %}
# Crear relación de usuario {#create-user-relationship}
{% apimethod post %}
/custom_objects/objects/{type_name}/{external_id}/users
{% endapimethod %}

> Usa este endpoint para vincular un usuario de Braze a un objeto personalizado.

{% alert important %}
Los objetos personalizados se encuentran actualmente en acceso anticipado. Tu espacio de trabajo debe estar habilitado antes de que los permisos de clave de API de objetos personalizados aparezcan en **Configuración** > **Claves de API**.
{% endalert %}

## Requisitos previos {#prerequisites}

Para usar este endpoint, necesitas una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `custom_objects.user_relationships.create`.

## Límite de velocidad {#rate-limit}

Este endpoint está en el contenedor de escritura de objetos personalizados con un límite predeterminado de 50 solicitudes por minuto.

## Parámetros de ruta {#path-parameters}

La siguiente tabla enumera y describe los parámetros de ruta del endpoint `/custom_objects/objects/{type_name}/{external_id}/users`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `type_name` | Obligatorio | Cadena | Tipo de objeto |
| `external_id` | Obligatorio | Cadena | Identificador de objeto |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de ruta de crear relación de usuario" }

## Parámetros de solicitud {#request-parameters}

La siguiente tabla enumera y describe los parámetros del cuerpo de la solicitud JSON del endpoint `/custom_objects/objects/{type_name}/{external_id}/users`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `braze_id` | Obligatorio | Cadena | ID de usuario de Braze |
| `rel_kind` | Obligatorio | Cadena | Tipo de relación |
| `attributes` | Opcional | Objeto | Atributos de la relación |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de solicitud de crear relación de usuario" }

## Ejemplo de solicitud {#example-request}

Esta sección incluye una carga útil JSON de ejemplo y una solicitud cURL de ejemplo.

### Carga útil de solicitud de ejemplo {#sample-request-payload}

```json
{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user",
  "attributes": {
    "role": "owner"
  }
}
```

### Solicitud cURL de ejemplo {#sample-curl-request}

Este ejemplo vincula un usuario a `acct-123` como `account_user` y registra su `role` como `owner`.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123/users' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user",
  "attributes": {
    "role": "owner"
  }
}'
```

## Respuesta {#response}

Esta sección incluye un ejemplo de respuesta exitosa y los campos de respuesta.

### Ejemplo de respuesta exitosa {#example-success-response}

El código de estado `201` podría devolver el siguiente cuerpo de respuesta.

```json
{
  "user_relationship": {
    "type_name": "account",
    "external_id": "acct-123",
    "rel_kind": "account_user",
    "user": { "braze_id": "507f1f77bcf86cd799439011" },
    "attributes": { "role": "owner" }
  }
}
```

### Parámetros de respuesta {#response-parameters}

La siguiente tabla enumera y describe los campos en una respuesta exitosa.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `user_relationship` | Obligatorio | Objeto | Registro de relación de usuario creado |
| `user_relationship.type_name` | Obligatorio | Cadena | Nombre de máquina del tipo de objeto personalizado |
| `user_relationship.external_id` | Obligatorio | Cadena | Identificador de objeto personalizado |
| `user_relationship.rel_kind` | Obligatorio | Cadena | Valor del tipo de relación |
| `user_relationship.user` | Obligatorio | Objeto | Objeto de usuario vinculado |
| `user_relationship.user.braze_id` | Obligatorio | Cadena | Identificador de usuario de Braze |
| `user_relationship.attributes` | Obligatorio | Objeto | Atributos de la relación |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de respuesta de crear relación de usuario" }

## Errores {#errors}

La siguiente tabla enumera los errores comunes de este endpoint y cómo resolverlos.

| Estado | Causa | Orientación |
|---|---|---|
| `400` | `rel_kind` desconocido para el tipo o error de validación de esquema | Confirma que `rel_kind` es válido para el tipo de objeto y que `attributes` coincide con el esquema de la relación. |
| `404` | Tipo u objeto no encontrado | Confirma que tanto `type_name` como `external_id` existen en el espacio de trabajo. |
| `409` | Relación duplicada (`duplicate-user-relationship`) | Usa `PUT` para reemplazar la relación existente, o elimínala antes de crearla de nuevo. |
| `422` | Límite de objetos por usuario alcanzado (`custom-objects-per-user-limit-exceeded`) o límite de usuarios por objeto alcanzado (`users-per-custom-object-limit-exceeded`) | Reduce la cantidad de relaciones para el usuario o el objeto, o contacta a soporte de Braze para consultar los límites de tu espacio de trabajo. |
| `401` | Clave de API REST faltante o no válida | Verifica que el encabezado `Authorization` use `Bearer YOUR_REST_API_KEY` y que la clave esté activa. |
| `403` | La clave de API no tiene permisos o la solicitud está bloqueada por la lista de permitidos | Confirma que la clave tiene el permiso `custom_objects.user_relationships.create` y que tu IP de origen está en la lista de permitidos de la clave, si está configurada. |
| `429` | Límite de velocidad excedido | Reintenta después de `X-RateLimit-Reset` y reduce la frecuencia de solicitudes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Errores de crear relación de usuario" }
{% endapi %}