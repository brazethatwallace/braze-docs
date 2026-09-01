---
nav_title: "POST: Crear relación de objeto"
article_title: "POST: Crear relación de objeto"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Este artículo describe los detalles del endpoint Crear relación de objeto."
---
{% api %}
# Crear relación de objeto {#create-object-relationship}
{% apimethod post %}
/custom_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> Usa este endpoint para crear una arista de relación direccional entre dos objetos personalizados.

{% alert important %}
Los objetos personalizados se encuentran actualmente en acceso anticipado. Tu espacio de trabajo debe estar habilitado antes de que los permisos de clave de API de objetos personalizados aparezcan en **Configuración** > **Claves de API**.
{% endalert %}

## Requisitos previos {#prerequisites}

Para usar este endpoint, necesitas una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `custom_objects.object_relationships.create`.

## Límite de velocidad {#rate-limit}

Este endpoint se encuentra en el contenedor de escritura de objetos personalizados con un límite predeterminado de 50 solicitudes por minuto.

## Parámetros de ruta {#path-parameters}

La siguiente tabla enumera y describe los parámetros de ruta del endpoint `/custom_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `type_name` | Obligatorio | Cadena | Tipo de objeto en la URL |
| `external_id` | Obligatorio | Cadena | Identificador del objeto en la URL |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de ruta para crear relación de objeto" }

## Parámetros de solicitud {#request-parameters}

La siguiente tabla enumera y describe los parámetros del cuerpo de solicitud JSON del endpoint `/custom_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `rel_kind` | Obligatorio | Cadena | Tipo de relación |
| `related_type_name` | Obligatorio | Cadena | Tipo de objeto relacionado |
| `related_external_id` | Obligatorio | Cadena | Identificador del objeto relacionado |
| `anchor` | Opcional | Cadena | `source` (predeterminado) o `target` |
| `attributes` | Opcional | Objeto | Atributos de la relación |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de solicitud para crear relación de objeto" }

## Solicitud de ejemplo {#example-request}

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

Este ejemplo vincula `acct-123` con `acct-456` como `subaccount`, con `acct-123` como origen de la relación.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123/object_relationships' \
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

El código de estado `201` podría devolver el siguiente cuerpo de respuesta.

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

La siguiente tabla enumera y describe los campos en una respuesta exitosa.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `object_relationship` | Obligatorio | Objeto | Registro de relación creado |
| `object_relationship.rel_kind` | Obligatorio | Cadena | Valor del tipo de relación |
| `object_relationship.to_custom_object` | Condicional | Objeto | Objeto relacionado cuando `anchor=source` |
| `object_relationship.from_custom_object` | Condicional | Objeto | Objeto relacionado cuando `anchor=target` |
| `object_relationship.to_custom_object.type_name` | Condicional | Cadena | Nombre del tipo de objeto relacionado |
| `object_relationship.to_custom_object.external_id` | Condicional | Cadena | ID externo del objeto relacionado |
| `object_relationship.to_custom_object.attributes` | Condicional | Objeto | Atributos del objeto relacionado |
| `object_relationship.from_custom_object.type_name` | Condicional | Cadena | Nombre del tipo de objeto relacionado |
| `object_relationship.from_custom_object.external_id` | Condicional | Cadena | ID externo del objeto relacionado |
| `object_relationship.from_custom_object.attributes` | Condicional | Objeto | Atributos del objeto relacionado |
| `object_relationship.attributes` | Obligatorio | Objeto | Atributos de la relación |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de respuesta para crear relación de objeto" }

## Errores {#errors}

La siguiente tabla enumera los errores comunes de este endpoint y cómo resolverlos.

| Estado | Causa | Orientación |
|---|---|---|
| `400` | `rel_kind` desconocido, `anchor` no válido, tipo relacionado no válido para el tipo de relación o violación del esquema | Confirma que `rel_kind` es válido para el par de tipos, usa un `anchor` válido y asegúrate de que `attributes` coincida con el esquema de relación. |
| `404` | Objeto de la URL, objeto relacionado, tipo de la URL o tipo relacionado no encontrado | Confirma que ambos objetos y ambos nombres de tipo existen en el espacio de trabajo. |
| `409` | Arista duplicada (`duplicate-object-relationship`) | Usa `PUT` para reemplazar la relación existente o elimínala antes de crearla de nuevo. |
| `422` | Se alcanzó el límite de relaciones por objeto (`custom-object-relationship-limit-exceeded`) | Reduce la cantidad de relaciones del objeto o contacta con soporte de Braze acerca de los límites del espacio de trabajo. |
| `401` | Clave de API REST faltante o no válida | Verifica que el encabezado `Authorization` use `Bearer YOUR_REST_API_KEY` y que la clave esté activa. |
| `403` | La clave de API no tiene permiso o la solicitud está bloqueada por la lista de permitidos | Confirma que la clave tenga el permiso `custom_objects.object_relationships.create` y que tu IP de origen esté en la lista de permitidos de la clave, si está configurada. |
| `429` | Se excedió el límite de velocidad | Reintenta después de `X-RateLimit-Reset` y reduce la frecuencia de las solicitudes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Errores de crear relación de objeto" }
{% endapi %}