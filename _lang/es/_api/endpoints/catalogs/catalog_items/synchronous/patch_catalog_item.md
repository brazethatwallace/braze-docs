---
nav_title: "PATCH: Editar elemento del catálogo"
article_title: "PATCH: Editar elemento del catálogo"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto de conexión Editar elemento del catálogo de Braze."

---
{% api %}
# Editar elemento del catálogo {#edit-catalog-item}
{% apimethod patch %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> Usa este punto de conexión para editar un elemento existente en tu catálogo.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e35976ae-ff77-42b7-b691-a883c980d8c0 {% endapiref %}

## Requisitos previos {#prerequisites}

Para usar este punto de conexión, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `catalogs.update_item`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## Parámetros de la ruta {#path-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `catalog_name` | Obligatorio | Cadena | Nombre del catálogo. |
| `item_id` | Obligatorio | Cadena | El ID del elemento del catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Path parameters" }

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `items` | Obligatorio | Matriz | Un array que contiene objetos de elemento. Los objetos de elemento deben contener campos que existan en el catálogo, excepto el campo `id`. Solo se permite un objeto de elemento por solicitud. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Request parameters" }

## Ejemplo de solicitud {#example-request}

```
curl --location --request PATCH 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "Name": "Restaurant",
      "Loyalty_Program": false,
      "Location": [-73.988103, 40.779109],
      "Preferences": {
        "favorite_brand": "Nike",
        "shirt_size": "L"
      },
      "Top_Dishes": {
        "$add": [
          "Biscuits",
          "Coleslaw"
        ],
        "$remove": [
          "French Fries"
        ]
      },
      "Open_Time": "2021-09-03T09:03:19.967+00:00"
    }
  ]
}'
```

{% alert note %}
- El campo `Location` utiliza el tipo de datos `geo`, que espera un array con el formato `[longitude, latitude]`.
- Los operadores `$add` y `$remove` solo son aplicables a campos de tipo array, y solo son compatibles con los puntos de conexión PATCH.
{% endalert %}

## Respuesta {#response}

Existen tres respuestas de código de estado para este punto de conexión: `200`, `400` y `404`.

### Ejemplo de respuesta correcta {#example-success-response}

El código de estado `200` podría devolver el siguiente cuerpo de respuesta.

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
      "id": "invalid-fields",
      "message": "Some of the fields given do not exist in the catalog",
      "parameters": [
        "id"
      ],
      "parameter_values": [
        "restaurant1"
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
| `filtered-set-field-too-long` | El valor del campo se está utilizando en un conjunto filtrado que supera el límite de caracteres de un elemento. |
| `id-in-body` | Ya existe un ID de elemento en el catálogo. |
| `ids-too-large` | El límite de caracteres para cada ID de elemento es de 250 caracteres. |
| `invalid-ids` | Los caracteres admitidos para los nombres de ID de elementos son letras, números, guiones y guiones bajos. |
| `invalid-fields` | Confirma que los campos de la solicitud existen en el catálogo. |
| `invalid-keys-in-value-object` | Las claves de objeto de elemento no pueden incluir `.` ni `$`. |
| `item-not-found` | Comprueba que el elemento está en el catálogo. |
| `item-array-invalid` | `items` debe ser un array de objetos. |
| `items-too-large` | El límite de caracteres para cada elemento es de 5000 caracteres. |
| `request-includes-too-many-items` | Solo puedes editar un elemento del catálogo por solicitud. |
| `too-deep-nesting-in-value-object` | Los objetos de elemento no pueden tener más de 50 niveles de anidamiento. |
| `unable-to-coerce-value` | Los tipos de elemento no se pueden convertir. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting" }

{% endapi %}