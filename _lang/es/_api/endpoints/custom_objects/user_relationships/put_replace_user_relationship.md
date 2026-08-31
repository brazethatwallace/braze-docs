---
nav_title: "PUT: Reemplazar relación de usuario"
article_title: "PUT: Reemplazar relación de usuario"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Este artículo describe los detalles del endpoint Reemplazar relación de usuario."
---
{% api %}
# Reemplazar relación de usuario {#replace-user-relationship}
{% apimethod put %}
/custom_objects/objects/{type_name}/{external_id}/users
{% endapimethod %}

> Usa este endpoint para crear o reemplazar una relación de usuario.

{% alert important %}
Los objetos personalizados se encuentran actualmente en acceso anticipado. Tu espacio de trabajo debe estar habilitado antes de que los permisos de clave de API de objetos personalizados aparezcan en **Configuración** > **Claves de API**.
{% endalert %}

## Requisitos previos {#prerequisites}

Para usar este endpoint, necesitas una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `custom_objects.user_relationships.update`.

## Límite de velocidad {#rate-limit}

Este endpoint se encuentra en el contenedor de escritura de objetos personalizados con un límite predeterminado de 50 solicitudes por minuto.

## Parámetros de ruta {#path-parameters}

La siguiente tabla enumera y describe los parámetros de ruta del endpoint `/custom_objects/objects/{type_name}/{external_id}/users`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `type_name` | Obligatorio | Cadena | Tipo de objeto |
| `external_id` | Obligatorio | Cadena | Identificador de objeto |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de ruta para reemplazar relación de usuario" }

## Parámetros de solicitud {#request-parameters}

La siguiente tabla enumera y describe los parámetros del cuerpo de solicitud JSON del endpoint `/custom_objects/objects/{type_name}/{external_id}/users`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `braze_id` | Obligatorio | Cadena | ID de usuario de Braze |
| `rel_kind` | Obligatorio | Cadena | Tipo de relación |
| `attributes` | Opcional | Objeto | Atributos de la relación |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de solicitud para reemplazar relación de usuario" }

## Ejemplo de solicitud {#example-request}

Esta sección incluye una carga útil JSON de ejemplo y una solicitud cURL de ejemplo.

### Carga útil de solicitud de ejemplo {#sample-request-payload}

```json
{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user",
  "attributes": {
    "role": "admin"
  }
}
```

### Solicitud cURL de ejemplo {#sample-curl-request}

Este ejemplo reemplaza los atributos en la relación `account_user` entre el usuario y `acct-123`, sobrescribiendo cualquier atributo almacenado previamente en ella.

```bash
curl --location --request PUT 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123/users' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user",
  "attributes": {
    "role": "admin"
  }
}'
```

## Respuesta {#response}

Esta sección incluye un ejemplo de respuesta exitosa y los campos de la respuesta.

### Ejemplo de respuesta exitosa {#example-success-response}

El código de estado `200` podría devolver el siguiente cuerpo de respuesta.

```json
{
  "user_relationship": {
    "type_name": "account",
    "external_id": "acct-123",
    "rel_kind": "account_user",
    "user": { "braze_id": "507f1f77bcf86cd799439011" },
    "attributes": { "role": "admin" }
  }
}
```

### Parámetros de respuesta {#response-parameters}

La siguiente tabla enumera y describe los campos en una respuesta exitosa.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `user_relationship` | Obligatorio | Objeto | Registro de relación de usuario creado o reemplazado |
| `user_relationship.type_name` | Obligatorio | Cadena | Nombre de máquina del tipo de objeto personalizado |
| `user_relationship.external_id` | Obligatorio | Cadena | Identificador del objeto personalizado |
| `user_relationship.rel_kind` | Obligatorio | Cadena | Valor del tipo de relación |
| `user_relationship.user` | Obligatorio | Objeto | Objeto de usuario vinculado |
| `user_relationship.user.braze_id` | Obligatorio | Cadena | Identificador de usuario de Braze |
| `user_relationship.attributes` | Obligatorio | Objeto | Atributos de la relación |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de respuesta para reemplazar relación de usuario" }

## Errores {#errors}

La siguiente tabla enumera los errores comunes de este endpoint y cómo resolverlos.

| Estado | Causa | Orientación |
|---|---|---|
| `400` | Error de validación | Confirma que `rel_kind` es válido para el tipo de objeto y que `attributes` coincide con el esquema de la relación. |
| `404` | Relación u objeto no encontrado (`custom-object-relationship-not-found`) | Confirma que el objeto, el usuario y los valores clave de la relación existen. |
| `422` | Se alcanzó el límite de objetos por usuario (`custom-objects-per-user-limit-exceeded`) o el límite de usuarios por objeto (`users-per-custom-object-limit-exceeded`) | Reduce el número de relaciones para el usuario o el objeto, o contacta con soporte de Braze sobre los límites de tu espacio de trabajo. |
| `401` | Clave de API REST faltante o no válida | Verifica que el encabezado `Authorization` utilice `Bearer YOUR_REST_API_KEY` y que la clave esté activa. |
| `403` | La clave de API no tiene permiso o la solicitud está bloqueada por la lista de permitidos | Confirma que la clave tiene el permiso `custom_objects.user_relationships.update` y que tu IP de origen está en la lista de permitidos de la clave, si está configurada. |
| `429` | Límite de velocidad excedido | Reintenta después de `X-RateLimit-Reset` y reduce la frecuencia de solicitudes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Errores de reemplazar relación de usuario" }
{% endapi %}