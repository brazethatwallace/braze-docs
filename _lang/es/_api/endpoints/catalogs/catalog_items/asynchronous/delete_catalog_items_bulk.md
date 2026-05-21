---
nav_title: "DELETE: Eliminar varios elementos del catálogo"
article_title: "DELETE: Eliminar varios elementos del catálogo"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto de conexión Eliminar varios elementos del catálogo de Braze."

---
{% api %}
# Eliminar varios elementos del catálogo {#delete-multiple-catalog-items}
{% apimethod delete %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> Usa este punto de conexión para eliminar varios elementos de tu catálogo.

Cada solicitud puede admitir hasta 50 elementos. Este punto de conexión es asíncrono.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#647c82e8-8b38-4df2-bde2-b1d8e19fd332 {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este punto de conexión, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `catalogs.delete_items`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog item' %}

## Parámetros de la ruta {#path-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `catalog_name` | Obligatorio | Cadena | Nombre del catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Path parameters" }

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `items` | Obligatorio | Matriz | Un array que contiene objetos de elemento. Los objetos de elemento deben contener un `id` que haga referencia a los elementos que Braze debe eliminar. Se permite un máximo de 50 objetos por solicitud. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Request parameters" }

## Ejemplo de solicitud {#example-request}

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {"id": "restaurant1"},
    {"id": "restaurant2"},
    {"id": "restaurant3"}
  ]
}'
```

## Respuesta {#response}

Existen tres respuestas de código de estado para este punto de conexión: `202`, `400` y `404`.

### Ejemplo de respuesta correcta {#example-success-response}

El código de estado `202` podría devolver el siguiente cuerpo de respuesta.

```json
{
  "message": "success"
}
```

### Ejemplo de respuesta de error {#example-error-response}

El código de estado `400` podría devolver el siguiente cuerpo de respuesta. Consulta la sección [Solución de problemas](#troubleshooting) para obtener más información sobre los errores que puedes encontrar.

```json
{
  "errors": [
    {
      "id": "items-missing-ids",
      "message": "There are 1 item(s) that do not have ids",
      "parameters": [],
      "parameter_values": []
    }
  ],
  "message": "Invalid Request"
}
```

## Solución de problemas {#troubleshooting}

La siguiente tabla enumera los posibles errores devueltos y sus pasos asociados para la solución de problemas.

| Error | Solución de problemas |
| --- | --- |
| `catalog-not-found` | Comprueba que el nombre del catálogo es válido. |
| `ids-too-large` | Los ID de los elementos no pueden tener más de 250 caracteres. |
| `ids-not-unique` | Comprueba que los ID de los elementos sean únicos en la solicitud. |
| `ids-not-strings` | Los ID de los elementos deben ser de tipo cadena. |
| `items-missing-ids` | Algunos elementos no tienen ID de elemento. Comprueba que cada elemento tiene un ID de elemento. |
| `invalid-ids` | Los ID de elementos solo pueden incluir letras, números, guiones y guiones bajos. |
| `request-includes-too-many-items` | Tu solicitud tiene demasiados elementos. El límite de elementos por solicitud es de 50. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting" }

{% endapi %}