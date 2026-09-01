---
nav_title: "PUT: Reemplazar relación de objeto"
article_title: "PUT: Reemplazar relación de objeto"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Este artículo describe los detalles del endpoint Reemplazar relación de objeto."
---
{% api %}
# Reemplazar relación de objeto {#replace-object-relationship}
{% apimethod put %}
/custom_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> Usa este endpoint para crear o reemplazar una relación de objeto.

{% alert important %}
Los objetos personalizados se encuentran actualmente en acceso anticipado. Tu espacio de trabajo debe estar habilitado antes de que los permisos de clave de API de objetos personalizados aparezcan en **Configuración** > **Claves de API**.
{% endalert %}

## Requisitos previos {#prerequisites}

Para usar este endpoint, necesitas una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `custom_objects.object_relationships.update`.

## Límite de velocidad {#rate-limit}

Este endpoint se encuentra en el contenedor de escritura de objetos personalizados con un límite predeterminado de 50 solicitudes por minuto.

## Parámetros de ruta {#path-parameters}

La siguiente tabla enumera y describe los parámetros de ruta del endpoint `/custom_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `type_name` | Obligatorio | Cadena | Tipo de objeto en la URL |
| `external_id` | Obligatorio | Cadena | Identificador de objeto en la URL |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de ruta de reemplazar relación de objeto" }

## Parámetros de solicitud {#request-parameters}

La siguiente tabla enumera y describe los parámetros del cuerpo de solicitud JSON del endpoint `/custom_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `rel_kind` | Obligatorio | Cadena | Tipo de relación |
| `related_type_name` | Obligatorio | Cadena | Tipo de objeto relacionado |
| `related_external_id` | Obligatorio | Cadena | Identificador de objeto relacionado |
| `anchor` | Opcional | Cadena | `source` (predeterminado) o `target` |
| `attributes` | Opcional | Objeto | Atributos de la relación |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de solicitud de reemplazar relación de objeto" }

## Ejemplo de solicitud {#example-request}

Esta sección incluye una carga útil JSON de ejemplo y una solicitud cURL de ejemplo.

### Carga útil de solicitud de ejemplo {#sample-request-payload}

```json
{
  "rel_kind": "subaccount",
  "related_type_name": "account",
  "related_external_id": "acct-456",
  "anchor": "source",
  "attributes": {}
}
```

### Solicitud cURL de ejemplo {#sample-curl-request}

Este ejemplo reemplaza la relación `subaccount` entre `acct-123` y `acct-456`, sobrescribiendo cualquier atributo previamente almacenado en ella.

```bash
curl --location --request PUT 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123/object_relationships' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "rel_kind": "subaccount",
  "related_type_name": "account",
  "related_external_id": "acct-456",
  "anchor": "source",
  "attributes": {}
}'
```

## Respuesta {#response}

Esta sección incluye un ejemplo de respuesta exitosa y los campos de la respuesta.

### Ejemplo de respuesta exitosa {#example-success-response}

El código de estado `200` podría devolver el siguiente cuerpo de respuesta.

```json
{
  "object_relationship": {
    "rel_kind": "subaccount",
    "to_custom_object": {
      "type_name": "account",
      "external_id": "acct-456",
      "attributes": { "name": "Child Account" }
    },
    "attributes": {}
  }
}
```

### Parámetros de respuesta {#response-parameters}

La siguiente tabla enumera y describe los campos de una respuesta exitosa.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `object_relationship` | Obligatorio | Objeto | Registro de relación creado o reemplazado |
| `object_relationship.rel_kind` | Obligatorio | Cadena | Valor del tipo de relación |
| `object_relationship.to_custom_object` | Condicional | Objeto | Objeto relacionado cuando `anchor=source` |
| `object_relationship.from_custom_object` | Condicional | Objeto | Objeto relacionado cuando `anchor=target` |
| `object_relationship.attributes` | Obligatorio | Objeto | Atributos de la relación |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de respuesta de reemplazar relación de objeto" }

## Errores {#errors}

La siguiente tabla enumera los errores comunes de este endpoint y cómo resolverlos.

| Estado | Causa | Orientación |
|---|---|---|
| `400` | Error de validación | Confirma que `rel_kind`, `anchor` y `attributes` sean válidos para el tipo de relación. |
| `404` | Relación u objetos del endpoint no encontrados (`custom-object-relationship-not-found`) | Confirma que ambos objetos y los nombres de tipo relacionado existen en el espacio de trabajo. |
| `422` | Límite de relaciones por objeto alcanzado (`custom-object-relationship-limit-exceeded`) | Reduce la cantidad de relaciones del objeto o contacta a soporte de Braze para consultar los límites del espacio de trabajo. |
| `401` | Clave de API REST faltante o no válida | Verifica que el encabezado `Authorization` use `Bearer YOUR_REST_API_KEY` y que la clave esté activa. |
| `403` | La clave de API no tiene permiso o la solicitud está bloqueada por la lista de permitidos | Confirma que la clave tenga el permiso `custom_objects.object_relationships.update` y que tu IP de origen esté en la lista de permitidos de la clave, si está configurada. |
| `429` | Límite de velocidad excedido | Vuelve a intentarlo después de `X-RateLimit-Reset` y reduce la frecuencia de las solicitudes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Errores de reemplazar relación de objeto" }
{% endapi %}