---
nav_title: "PATCH: Actualizar relación de objeto"
article_title: "PATCH: Actualizar relación de objeto"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artículo describe los detalles del endpoint Actualizar relación de objeto."
---
{% api %}
# Actualizar relación de objeto {#update-object-relationship}
{% apimethod patch %}
/data_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> Utiliza este endpoint para fusionar atributos en una relación de objeto existente.

{% alert important %}
Los objetos de datos se encuentran actualmente en acceso anticipado. Tu espacio de trabajo debe estar habilitado antes de que los permisos de clave de API de objetos de datos aparezcan en **Configuración** > **Claves de API**.
{% endalert %}

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitas una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `data_objects.object_relationships.update`.

## Límite de velocidad {#rate-limit}

Este endpoint se encuentra en el contenedor de escritura de objetos de datos con un límite predeterminado de 50 solicitudes por minuto.

## Parámetros de ruta {#path-parameters}

La siguiente tabla enumera y describe los parámetros de ruta para el endpoint `/data_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `type_name` | Obligatorio | Cadena | Tipo de objeto en la URL |
| `external_id` | Obligatorio | Cadena | Identificador de objeto en la URL |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de ruta de actualizar relación de objeto" }

## Parámetros de solicitud {#request-parameters}

La siguiente tabla enumera y describe los parámetros del cuerpo de solicitud JSON para el endpoint `/data_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `rel_kind` | Obligatorio | Cadena | Tipo de relación |
| `related_type_name` | Obligatorio | Cadena | Tipo de objeto relacionado |
| `related_external_id` | Obligatorio | Cadena | Identificador de objeto relacionado |
| `anchor` | Opcional | Cadena | `source` (predeterminado) o `target` |
| `attributes` | Opcional | Objeto | Atributos de relación a fusionar |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de solicitud de actualizar relación de objeto" }

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

Este ejemplo fusiona atributos en la relación `subaccount` existente entre `acct-123` y `acct-456`, dejando sin cambios los atributos que omitas.

```bash
curl --location --request PATCH 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/object_relationships' \
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

Esta sección incluye un ejemplo de respuesta exitosa y los campos de respuesta.

### Ejemplo de respuesta exitosa {#example-success-response}

El código de estado `200` podría devolver el siguiente cuerpo de respuesta.

```json
{
  "object_relationship": {
    "rel_kind": "subaccount",
    "to_data_object": {
      "type_name": "account",
      "external_id": "acct-456",
      "attributes": { "name": "Child Account" }
    },
    "attributes": {}
  }
}
```

### Parámetros de respuesta {#response-parameters}

La siguiente tabla enumera y describe los campos en una respuesta exitosa.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `object_relationship` | Obligatorio | Objeto | Registro de relación actualizado |
| `object_relationship.rel_kind` | Obligatorio | Cadena | Valor del tipo de relación |
| `object_relationship.to_data_object` | Condicional | Objeto | Objeto relacionado cuando `anchor=source` |
| `object_relationship.from_data_object` | Condicional | Objeto | Objeto relacionado cuando `anchor=target` |
| `object_relationship.attributes` | Obligatorio | Objeto | Atributos de relación después de la fusión |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de respuesta de actualizar relación de objeto" }

## Errores {#errors}

La siguiente tabla enumera los errores comunes de este endpoint y cómo resolverlos.

| Estado | Causa | Orientación |
|---|---|---|
| `400` | Error de validación | Confirma que `rel_kind`, `anchor` y `attributes` son válidos para el tipo de relación. |
| `404` | Relación no encontrada (`data-object-relationship-not-found`) | Confirma que el objeto de origen, el objeto relacionado y los valores de clave de relación existen. |
| `401` | Clave de API REST faltante o no válida | Verifica que el encabezado `Authorization` use `Bearer YOUR_REST_API_KEY` y que la clave esté activa. |
| `403` | La clave de API no tiene permiso o la solicitud está bloqueada por la lista de permitidos | Confirma que la clave tiene el permiso `data_objects.object_relationships.update` y que tu IP de origen está en la lista de permitidos de la clave, si está configurada. |
| `429` | Límite de velocidad excedido | Reintenta después de `X-RateLimit-Reset` y reduce la frecuencia de solicitudes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Errores de actualizar relación de objeto" }
{% endapi %}