---
nav_title: "DELETE: Eliminar relación de objetos"
article_title: "DELETE: Eliminar relación de objetos"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Este artículo describe los detalles del endpoint Eliminar relación de objetos."
---
{% api %}
# Eliminar relación de objetos {#delete-object-relationship}
{% apimethod delete %}
/data_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> Usa este endpoint para eliminar una arista de relación de objeto a objeto.

{% alert important %}
Los objetos de datos se encuentran actualmente en acceso anticipado. Tu espacio de trabajo debe estar habilitado antes de que los permisos de clave de API de objetos de datos aparezcan en **Configuración** > **Claves de API**.
{% endalert %}

## Requisitos previos {#prerequisites}

Para usar este endpoint, necesitas una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `data_objects.object_relationships.delete`.

## Límite de velocidad {#rate-limit}

Este endpoint se encuentra en el contenedor de escritura de objetos de datos con un límite predeterminado de 50 solicitudes por minuto.

## Parámetros de ruta {#path-parameters}

La siguiente tabla enumera y describe los parámetros de ruta para el endpoint `/data_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `type_name` | Obligatorio | String | Tipo de objeto en la URL |
| `external_id` | Obligatorio | String | Identificador de objeto en la URL |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de ruta de eliminar relación de objetos" }

## Parámetros de solicitud {#request-parameters}

La siguiente tabla enumera y describe los parámetros del cuerpo de la solicitud JSON para el endpoint `/data_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `rel_kind` | Obligatorio | String | Tipo de relación |
| `related_type_name` | Obligatorio | String | Tipo de objeto relacionado |
| `related_external_id` | Obligatorio | String | Identificador de objeto relacionado |
| `anchor` | Opcional | String | `source` (predeterminado) o `target` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de solicitud de eliminar relación de objetos" }

{% alert note %}
Este endpoint `DELETE` espera un cuerpo de solicitud en formato JSON. Verifica que tu cliente HTTP envíe cuerpos de solicitud en las llamadas `DELETE`.
{% endalert %}

## Ejemplo de solicitud {#example-request}

Esta sección incluye una carga útil JSON de ejemplo y una solicitud cURL de ejemplo.

### Carga útil de solicitud de ejemplo {#sample-request-payload}

```json
{
  "rel_kind": "subaccount",
  "related_type_name": "account",
  "related_external_id": "acct-456",
  "anchor": "source"
}
```

### Solicitud cURL de ejemplo {#sample-curl-request}

Este ejemplo elimina la relación `subaccount` entre `acct-123` y `acct-456`. Ambos registros de cuenta permanecen.

```bash
curl --location --request DELETE 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/object_relationships' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "rel_kind": "subaccount",
  "related_type_name": "account",
  "related_external_id": "acct-456",
  "anchor": "source"
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

La siguiente tabla enumera y describe los campos en una respuesta exitosa.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `deleted` | Obligatorio | Booleano | Si la eliminación de la relación se realizó correctamente |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de respuesta de eliminar relación de objetos" }

## Errores {#errors}

La siguiente tabla enumera los errores comunes de este endpoint y cómo resolverlos.

| Estado | Causa | Orientación |
|---|---|---|
| `400` | Error de validación | Confirma que el cuerpo de la solicitud incluya valores válidos para `rel_kind`, `related_type_name`, `related_external_id` y `anchor`. |
| `404` | Relación u objeto del endpoint no encontrado | Confirma que ambos objetos existan y que los valores de la clave de relación coincidan con una arista existente. |
| `401` | Clave de API REST or transferencia de estado representacional ausente o no válida | Verifica que el encabezado `Authorization` use `Bearer YOUR_REST_API_KEY` y que la clave esté activa. |
| `403` | La clave de API no tiene permiso o la solicitud está bloqueada por la lista de permitidos | Confirma que la clave tenga el permiso `data_objects.object_relationships.delete` y que tu IP de origen esté en la lista de permitidos de la clave, si está configurada. |
| `429` | Límite de velocidad excedido | Reintenta después de `X-RateLimit-Reset` y reduce la frecuencia de solicitudes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Errores de eliminar relación de objetos" }
{% endapi %}