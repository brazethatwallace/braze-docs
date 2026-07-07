---
nav_title: "GET: Enumerar los detalles del elemento del catálogo"
article_title: "GET: Enumerar los detalles del elemento del catálogo"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto de conexión Enumerar los detalles del elemento del catálogo de Braze."

---
{% api %}
# Enumerar los detalles del elemento del catálogo {#list-catalog-item-details}
{% apimethod get %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> Utiliza este punto de conexión para devolver un elemento del catálogo y su contenido.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#52c6631c-7366-48e5-9e0e-16de7b6285cc {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este punto de conexión, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key) con el permiso `catalogs.get_item`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## Parámetros de ruta {#path-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `catalog_name` | Obligatorio | Cadena | Nombre del catálogo. |
| `item_id` | Obligatorio | Cadena | El ID del elemento del catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de ruta" }

## Parámetros de la solicitud {#request-parameters}

No hay cuerpo de solicitud para este punto de conexión.

## Ejemplo de solicitud {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Respuesta {#response}

Hay dos respuestas de código de estado para este punto de conexión: `200` y `404`.

### Ejemplo de respuesta correcta {#example-success-response}

El código de estado `200` podría devolver el siguiente cuerpo de respuesta.

```json
{
  "items": [
    {
      "id": "restaurant3",
      "Name": "Restaurant1",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": true,
      "Open_Time": "2022-11-01T09:03:19.967Z"
    }
  ],
  "message": "success"
}
```

### Ejemplo de respuesta de error {#example-error-response}

El código de estado `404` podría devolver la siguiente respuesta. Consulta la sección [Solución de problemas](#troubleshooting) para obtener más información sobre los errores que puedas encontrar.

```json
{
  "errors": [
    {
      "id": "item-not-found",
      "message": "Could not find item",
      "parameters": [
        "item_id"
      ],
      "parameter_values": [
        "restaurant34"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## Solución de problemas {#troubleshooting}

La siguiente tabla enumera los posibles errores devueltos y sus pasos asociados para la solución de problemas, si procede.

| Error | Solución de problemas |
| --- | --- |
| `catalog-not-found` | Comprueba que el nombre del catálogo es válido. |
| `item-not-found` | Comprueba que el elemento está en el catálogo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solución de problemas" }

{% endapi %}