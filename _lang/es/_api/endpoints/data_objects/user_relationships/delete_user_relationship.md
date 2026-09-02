---
nav_title: "DELETE: Eliminar relación de usuario"
article_title: "DELETE: Eliminar relación de usuario"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Este artículo describe los detalles del endpoint Eliminar relación de usuario."
---
{% api %}
# Eliminar relación de usuario {#delete-user-relationship}
{% apimethod delete %}
/data_objects/objects/{type_name}/{external_id}/users
{% endapimethod %}

> Usa este endpoint para eliminar una relación entre un usuario y un objeto.

{% alert important %}
Los objetos de datos se encuentran actualmente en acceso anticipado. Tu espacio de trabajo debe estar habilitado antes de que los permisos de clave de API de objetos de datos aparezcan en **Configuración** > **Claves de API**.
{% endalert %}

## Requisitos previos {#prerequisites}

Para usar este endpoint, necesitas una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `data_objects.user_relationships.delete`.

## Límite de velocidad {#rate-limit}

Este endpoint se encuentra en el contenedor de escritura de objetos de datos con un límite predeterminado de 50 solicitudes por minuto.

## Parámetros de ruta {#path-parameters}

La siguiente tabla enumera y describe los parámetros de ruta para el endpoint `/data_objects/objects/{type_name}/{external_id}/users`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `type_name` | Obligatorio | Cadena | Tipo de objeto |
| `external_id` | Obligatorio | Cadena | Identificador de objeto |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de ruta para eliminar relación de usuario" }

## Parámetros de solicitud {#request-parameters}

La siguiente tabla enumera y describe los parámetros del cuerpo de la solicitud JSON para el endpoint `/data_objects/objects/{type_name}/{external_id}/users`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `braze_id` | Obligatorio | Cadena | ID de usuario de Braze |
| `rel_kind` | Obligatorio | Cadena | Tipo de relación |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de solicitud para eliminar relación de usuario" }

{% alert note %}
Este endpoint `DELETE` espera un cuerpo de solicitud JSON. Valida que tu cliente HTTP envíe cuerpos de solicitud en las llamadas `DELETE`.
{% endalert %}

## Ejemplo de solicitud {#example-request}

Esta sección incluye un ejemplo de carga útil JSON y un ejemplo de solicitud cURL.

### Ejemplo de carga útil de solicitud {#sample-request-payload}

```json
{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user"
}
```

### Ejemplo de solicitud cURL {#sample-curl-request}

Este ejemplo elimina la relación `account_user` entre el usuario especificado y `acct-123`. Tanto el perfil de usuario como el registro de cuenta se mantienen.

```bash
curl --location --request DELETE 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/users' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user"
}'
```

## Respuesta {#response}

Esta sección incluye un ejemplo de respuesta exitosa y los campos de respuesta.

### Ejemplo de respuesta exitosa {#example-success-response}

El código de estado `200` podría devolver el siguiente cuerpo de respuesta.

```json
{ "deleted": true }
```

### Parámetros de respuesta {#response-parameters}

La siguiente tabla enumera y describe los campos de una respuesta exitosa.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `deleted` | Obligatorio | Booleano | Si la eliminación de la relación fue exitosa |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de respuesta para eliminar relación de usuario" }

## Errores {#errors}

La siguiente tabla enumera los errores comunes de este endpoint y cómo resolverlos.

| Estado | Causa | Orientación |
|---|---|---|
| `400` | Error de validación | Confirma que el cuerpo de la solicitud incluya valores válidos de `braze_id` y `rel_kind`. |
| `404` | Relación u objeto no encontrado | Confirma que el objeto, el usuario y los valores de la clave de relación existan. |
| `401` | Clave de API REST or transferencia de estado representacional faltante o no válida | Verifica que el encabezado `Authorization` use `Bearer YOUR_REST_API_KEY` y que la clave esté activa. |
| `403` | La clave de API carece de permiso o la solicitud está bloqueada por la lista de permitidos | Confirma que la clave tenga el permiso `data_objects.user_relationships.delete` y que tu IP de origen esté en la lista de permitidos de la clave, si está configurada. |
| `429` | Límite de velocidad excedido | Reintenta después de `X-RateLimit-Reset` y reduce la frecuencia de solicitudes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Errores de eliminación de relación de usuario" }
{% endapi %}