---
nav_title: "GET: Listar objetos de datos"
article_title: "GET: Listar objetos de datos"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Este artículo describe los detalles del endpoint Listar objetos de datos."
---
{% api %}
# Listar objetos de datos {#list-data-objects}
{% apimethod get %}
/data_objects/objects/{type_name}
{% endapimethod %}

> Utiliza este endpoint para listar objetos de un tipo de objeto de datos específico.

{% alert important %}
Los objetos de datos se encuentran actualmente en acceso anticipado. Tu espacio de trabajo debe estar habilitado antes de que los permisos de clave de API de objetos de datos aparezcan en **Configuración** > **Claves de API**.
{% endalert %}

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitas una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `data_objects.read`.

## Límite de velocidad {#rate-limit}

Este endpoint se encuentra en el contenedor de lectura de objetos de datos con un límite predeterminado de 50 solicitudes por minuto.

## Parámetros de ruta {#path-parameters}

La siguiente tabla enumera y describe los parámetros de ruta del endpoint `/data_objects/objects/{type_name}`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `type_name` | Obligatorio | Cadena | Nombre de máquina del tipo de objeto de datos |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de ruta de listar objetos de datos" }

## Parámetros de consulta {#query-parameters}

La siguiente tabla enumera y describe los parámetros de consulta del endpoint `/data_objects/objects/{type_name}`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `search_term` | Opcional | Cadena | Filtro de subcadena en el identificador del objeto |
| `limit` | Opcional | Entero | Tamaño de página. Predeterminado `100`. Limitado de `1` a `250` |
| `offset` | Opcional | Entero | Desplazamiento. Predeterminado `0`. Los valores negativos se redondean a `0` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de consulta de listar objetos de datos" }

## Ejemplo de solicitud {#example-request}

Esta sección incluye una carga útil de parámetros de ejemplo y una solicitud cURL de ejemplo.

### Carga útil de solicitud de ejemplo {#sample-request-payload}

Utiliza este objeto JSON como referencia para los parámetros de solicitud.

```json
{
  "type_name": "account",
  "search_term": "acct",
  "limit": 100,
  "offset": 0
}
```

### Solicitud cURL de ejemplo {#sample-curl-request}

Este ejemplo lista los registros de `account` que coinciden con el término de búsqueda `acct`, devolviendo la primera página de resultados.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/data_objects/objects/account?search_term=acct&limit=100&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Respuesta {#response}

Esta sección incluye un ejemplo de respuesta exitosa y los campos de respuesta.

### Ejemplo de respuesta exitosa {#example-success-response}

El código de estado `200` podría devolver el siguiente cuerpo de respuesta.

```json
{
  "items": [
    {
      "type_name": "account",
      "external_id": "acct-123",
      "attributes": { "name": "Acme", "industry": "software" }
    }
  ],
  "total_count": 1,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 100
}
```

### Parámetros de respuesta {#response-parameters}

La siguiente tabla enumera y describe los campos en una respuesta exitosa.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `items` | Obligatorio | Array | Lista de registros de objetos de datos |
| `items[].type_name` | Obligatorio | Cadena | Nombre de máquina del tipo de objeto de datos |
| `items[].external_id` | Obligatorio | Cadena | Identificador del objeto de datos |
| `items[].attributes` | Obligatorio | Objeto | Atributos del objeto indexados por nombre de campo |
| `total_count` | Obligatorio | Entero | Número total de registros coincidentes |
| `has_more` | Obligatorio | Booleano | Si hay otra página de resultados disponible |
| `next_offset` | Opcional | Entero | Desplazamiento para la siguiente página cuando `has_more` es `true` |
| `offset` | Obligatorio | Entero | Desplazamiento de la página actual |
| `limit` | Obligatorio | Entero | Tamaño de página utilizado por la solicitud |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de respuesta de listar objetos de datos" }

## Errores {#errors}

La siguiente tabla enumera los errores comunes de este endpoint y cómo resolverlos.

| Estado | Causa | Orientación |
|---|---|---|
| `404` | Tipo no encontrado (`data-object-type-not-found`) | Confirma que `type_name` existe en el espacio de trabajo y coincide exactamente con el nombre de máquina. |
| `401` | Clave de API REST or transferencia de estado representacional ausente o no válida | Verifica que el encabezado `Authorization` utiliza `Bearer YOUR_REST_API_KEY` y que la clave está activa. |
| `403` | La clave de API no tiene permiso o la solicitud está bloqueada por la lista de permitidos | Confirma que la clave tiene el permiso `data_objects.read` y que tu IP de origen está en la lista de permitidos de la clave, si está configurada. |
| `429` | Límite de velocidad excedido | Reintenta después de `X-RateLimit-Reset` y reduce la frecuencia de solicitudes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Errores de listar objetos de datos" }
{% endapi %}