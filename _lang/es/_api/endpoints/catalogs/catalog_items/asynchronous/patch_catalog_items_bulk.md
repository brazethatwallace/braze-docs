---
nav_title: "PATCH: Editar varios elementos del catálogo"
article_title: "PATCH: Editar varios elementos del catálogo"
alias: /catalogs_items_patch/
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto de conexión Editar varios elementos del catálogo de Braze."

---
{% api %}
# Editar varios elementos del catálogo {#edit-multiple-catalog-items}
{% apimethod patch %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> Utiliza este punto de conexión para editar varios elementos existentes en tu catálogo.

Cada solicitud puede admitir hasta 50 elementos. Este punto de conexión es asíncrono.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#03f3548e-4139-4f60-812d-7e1a695a738a {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este punto de conexión, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key) con el permiso `catalogs.update_items`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog item' %}

## Parámetros de la ruta {#path-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `catalog_name` | Obligatorio | Cadena | Nombre del catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de la ruta" }

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `items` | Obligatorio | Matriz | Una matriz que contiene objetos de elemento. Los objetos de elemento deben contener campos que existan en el catálogo. Se permiten hasta 50 objetos de elemento por solicitud. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de la solicitud" }

## Ejemplo de solicitud {#example-request}

```
curl --location --request PATCH 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "id": "restaurant1",
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
    },
    {
      "id": "restaurant3",
      "City": "San Francisco",
      "Rating": 2,
      "Top_Dishes": [
        "Buffalo Wings",
        "Philly Cheesesteak"
      ]
    }
  ]
}'
```

{% alert note %}
- El campo `Location` utiliza el tipo de datos `geo`, que espera una matriz con el formato `[longitude, latitude]`.
- Los operadores `$add` y `$remove` solo son aplicables a campos de tipo matriz y solo son compatibles con los puntos de conexión PATCH.
{% endalert %}

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
| `catalog-not-found` | Comprueba que el nombre del catálogo es válido. |
| `ids-too-large` | Los ID de los elementos no pueden tener más de 250 caracteres. |
| `ids-not-strings` | Los ID de los elementos deben ser de tipo cadena. |
| `ids-not-unique` | Los ID de los elementos deben ser únicos en la solicitud. |
| `invalid-ids` | Los ID de los elementos solo pueden incluir letras, números, guiones y guiones bajos. |
| `invalid-fields` | Confirma que todos los campos que envías en la solicitud de API ya existen en el catálogo. Esto no está relacionado con el campo ID mencionado en el error. |
| `invalid-keys-in-value-object` | Las claves de objeto de elemento no pueden incluir `.` ni `$`. |
| `items-missing-ids` | Algunos elementos no tienen ID de elemento. Comprueba que cada elemento tiene un ID de elemento. |
| `item-array-invalid` | `items` debe ser una matriz de objetos. |
| `items-too-large` | Los valores de los elementos no pueden superar los 5000 caracteres. |
| `request-includes-too-many-items` | Tu solicitud tiene demasiados elementos. El límite de elementos por solicitud es de 50. |
| `too-deep-nesting-in-value-object` | Los objetos de elemento no pueden tener más de 50 niveles de anidamiento. |
| `unable-to-coerce-value` | Los tipos de elemento no se pueden convertir. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solución de problemas" }

{% endapi %}