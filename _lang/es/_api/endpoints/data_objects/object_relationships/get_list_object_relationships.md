---
nav_title: "GET: Listar relaciones de objetos"
article_title: "GET: Listar relaciones de objetos"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Este artículo describe los detalles del endpoint Listar relaciones de objetos."
---
{% api %}
# Listar relaciones de objetos {#list-object-relationships}
{% apimethod get %}
/data_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> Utiliza este endpoint para listar objetos de datos relacionados a partir de un objeto de anclaje.

{% alert important %}
Los objetos de datos se encuentran actualmente en acceso anticipado. Tu espacio de trabajo debe estar habilitado antes de que los permisos de clave de API de objetos de datos aparezcan en **Configuración** > **Claves de API**.
{% endalert %}

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitas una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `data_objects.read`.

## Límite de velocidad {#rate-limit}

Este endpoint se encuentra en el contenedor de lectura de objetos de datos con un límite predeterminado de 50 solicitudes por minuto.

## Parámetros de ruta {#path-parameters}

La siguiente tabla enumera y describe los parámetros de ruta del endpoint `/data_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `type_name` | Obligatorio | Cadena | Tipo de objeto de origen |
| `external_id` | Obligatorio | Cadena | Identificador del objeto de origen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de ruta de listar relaciones de objetos" }

## Parámetros de consulta {#query-parameters}

La siguiente tabla enumera y describe los parámetros de consulta del endpoint `/data_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `anchor` | Opcional | Cadena | `source` (predeterminado) o `target` |
| `rel_kind` | Opcional | Cadena | Filtrar por un tipo de relación |
| `limit` | Opcional | Entero | Tamaño de página. Predeterminado `100`. Limitado de `1` a `250` |
| `offset` | Opcional | Entero | Desplazamiento. Predeterminado `0`. Los valores negativos se ajustan a `0` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de consulta de listar relaciones de objetos" }

## Solicitud de ejemplo {#example-request}

Esta sección incluye una carga útil de parámetros de ejemplo y una solicitud cURL de ejemplo.

### Carga útil de solicitud de ejemplo {#sample-request-payload}

Utiliza este objeto JSON como referencia para los parámetros de solicitud.

```json
{
  "type_name": "account",
  "external_id": "acct-123",
  "anchor": "source",
  "rel_kind": "subaccount",
  "limit": 100,
  "offset": 0
}
```

### Solicitud cURL de ejemplo {#sample-curl-request}

Este ejemplo lista los registros `subaccount` a los que `acct-123` enlaza, devolviendo la primera página de resultados.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/object_relationships?anchor=source&rel_kind=subaccount&limit=100&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Respuesta {#response}

Esta sección incluye una respuesta exitosa de ejemplo y los campos de la respuesta.

### Ejemplo de respuesta exitosa {#example-success-response}

El código de estado `200` podría devolver el siguiente cuerpo de respuesta.

```json
{
  "items": [
    {
      "rel_kind": "subaccount",
      "to_data_object": {
        "type_name": "account",
        "external_id": "acct-456",
        "attributes": { "name": "Child Account" }
      },
      "attributes": {}
    }
  ],
  "total_count": 1,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 100
}
```

Con `anchor=target`, los objetos relacionados se devuelven como `from_data_object`.

### Parámetros de respuesta {#response-parameters}

La siguiente tabla enumera y describe los campos de una respuesta exitosa.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `items` | Obligatorio | Array | Lista de registros de relaciones de objetos |
| `items[].rel_kind` | Obligatorio | Cadena | Valor del tipo de relación |
| `items[].to_data_object` | Condicional | Objeto | Objeto relacionado cuando `anchor=source` |
| `items[].from_data_object` | Condicional | Objeto | Objeto relacionado cuando `anchor=target` |
| `items[].to_data_object.type_name` | Condicional | Cadena | Nombre del tipo de objeto relacionado |
| `items[].to_data_object.external_id` | Condicional | Cadena | ID externo del objeto relacionado |
| `items[].to_data_object.attributes` | Condicional | Objeto | Atributos del objeto relacionado |
| `items[].from_data_object.type_name` | Condicional | Cadena | Nombre del tipo de objeto relacionado |
| `items[].from_data_object.external_id` | Condicional | Cadena | ID externo del objeto relacionado |
| `items[].from_data_object.attributes` | Condicional | Objeto | Atributos del objeto relacionado |
| `items[].attributes` | Obligatorio | Objeto | Atributos de la relación |
| `total_count` | Obligatorio | Entero | Número total de registros coincidentes |
| `has_more` | Obligatorio | Booleano | Si hay otra página de resultados disponible |
| `next_offset` | Opcional | Entero | Desplazamiento para la siguiente página cuando `has_more` es `true` |
| `offset` | Obligatorio | Entero | Desplazamiento de la página actual |
| `limit` | Obligatorio | Entero | Tamaño de página utilizado por la solicitud |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de respuesta de listar relaciones de objetos" }

## Errores {#errors}

La siguiente tabla enumera los errores comunes de este endpoint y cómo resolverlos.

| Estado | Causa | Orientación |
|---|---|---|
| `400` | `anchor` no válido | Usa `source` o `target` para `anchor`. |
| `404` | Tipo u objeto no encontrado | Confirma que `type_name` y `external_id` existen en el espacio de trabajo. |
| `401` | Clave de API REST or transferencia de estado representacional faltante o no válida | Verifica que el encabezado `Authorization` utilice `Bearer YOUR_REST_API_KEY` y que la clave esté activa. |
| `403` | La clave de API no tiene permiso o la solicitud está bloqueada por la lista de permitidos | Confirma que la clave tenga `data_objects.read` y que tu IP de origen esté en la lista de permitidos de la clave, si está configurada. |
| `429` | Límite de velocidad excedido | Reintenta después de `X-RateLimit-Reset` y reduce la frecuencia de solicitudes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Errores de listar relaciones de objetos" }
{% endapi %}