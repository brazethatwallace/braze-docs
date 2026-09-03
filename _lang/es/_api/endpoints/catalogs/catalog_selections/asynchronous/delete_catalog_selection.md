---
nav_title: "DELETE: Eliminar selección de catálogo"
article_title: "DELETE: Eliminar selección de catálogo"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del endpoint Eliminar selección de catálogo de Braze."

---
{% api %}
# Eliminar selección de catálogo {#delete-catalog-selection}
{% apimethod delete %}
/catalogs/{catalog_name}/selections/{selection_name}
{% endapimethod %}

> Utiliza este endpoint para eliminar una selección de catálogo.

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `catalogs.delete_selection`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog selections' %}

## Parámetros de ruta {#path-parameters}

| Parámetro        | Obligatorio | Tipo de datos | Descripción                          |
| ---------------- | ----------- | ------------- | ------------------------------------ |
| `catalog_name`   | Obligatorio | Cadena        | Nombre del catálogo.                 |
| `selection_name` | Obligatorio | Cadena        | Nombre de la selección del catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de ruta" }

## Ejemplo de solicitud {#example-request}

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/selections/favorite_list' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
```

## Respuesta {#response}

Hay dos respuestas de código de estado para este endpoint: `202` y `404`.

### Ejemplo de respuesta correcta {#example-success-response}

El código de estado `202` podría devolver el siguiente cuerpo de respuesta:

```json
{
  "message": "success"
}
```

### Ejemplo de respuesta de error {#example-error-response}

El código de estado `404` podría devolver el siguiente cuerpo de respuesta. Consulta la sección [Solución de problemas](#troubleshooting) para obtener más información sobre los errores que puedes encontrar.

```json
{
  "errors": [
    {
      "id": "catalog-not-found",
      "message": "Could not find catalog",
      "parameters": [
        "catalog_name"
      ],
      "parameter_values": [
        "restaurants"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## Solución de problemas {#troubleshooting}

La siguiente tabla enumera los posibles errores devueltos y sus pasos asociados para la solución de problemas.

| Error                | Solución de problemas                                    |
| -------------------- | -------------------------------------------------------- |
| `catalog-not-found`  | Comprueba que el nombre del catálogo es válido.          |
| `invalid-selection`  | Comprueba que el nombre de la selección es válido.       |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solución de problemas" }

{% endapi %}