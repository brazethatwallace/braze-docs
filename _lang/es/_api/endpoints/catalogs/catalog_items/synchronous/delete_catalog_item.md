---
nav_title: "DELETE: Eliminar elemento del catálogo"
article_title: "DELETE: Eliminar elemento del catálogo"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto de conexión Eliminar elemento del catálogo de Braze."

---
{% api %}
# Eliminar un elemento del catálogo {#delete-a-catalog-item}
{% apimethod delete %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> Utiliza este punto de conexión para eliminar un elemento de tu catálogo.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0dcce797-1346-472f-9384-082f14541689 {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este punto de conexión, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `catalogs.delete_item`.

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
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
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

El código de estado `400` podría devolver el siguiente cuerpo de respuesta. Consulta [Solución de problemas](#troubleshooting) para obtener más información sobre los errores que puedes encontrar.

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

La siguiente tabla enumera los posibles errores devueltos y sus pasos asociados para la solución de problemas.

| Error | Solución de problemas |
| --- | --- |
| `arbitrary-error` | Se ha producido un error arbitrario. Inténtalo de nuevo o ponte en contacto con [Soporte]({{site.baseurl}}/support_contact/). |
| `catalog-not-found` | Comprueba que el nombre del catálogo es válido. |
| `item-not-found` | Comprueba que el elemento a eliminar existe en tu catálogo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solución de problemas" }

{% endapi %}