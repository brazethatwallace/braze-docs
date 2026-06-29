---
nav_title: "POST: Crear varios elementos del catálogo"
article_title: "POST: Crear varios elementos del catálogo"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto de conexión Crear varios elementos del catálogo de Braze."

---
{% api %}
# Crear varios elementos del catálogo {#create-multiple-catalog-items}
{% apimethod post %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> Utiliza este punto de conexión para crear varios elementos en tu catálogo.

Cada solicitud puede admitir hasta 50 elementos. Este punto de conexión es asíncrono.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cea18bb3-b83a-4160-81fe-8cd42aa6e7cc {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este punto de conexión, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `catalogs.add_items`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog item' %}

## Parámetros de ruta {#path-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `catalog_name` | Obligatorio | Cadena | Nombre del catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Path parameters" }

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `items` | Obligatorio | Matriz | Un array que contiene objetos de elementos. Los objetos de elementos deben contener todos los campos del catálogo. Se permite un máximo de 50 objetos de elementos por solicitud. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Request parameters" }

## Ejemplo de solicitud {#example-request}

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "id": "restaurant1",
      "Name": "Restaurant1",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": true,
      "Location": [-73.988103, 40.779109],
      "Preferences": {
        "favorite_brand": "Nike",
        "shirt_size": "L"
      },
      "Top_Dishes": [
        "Hamburger",
        "Deluxe Cheeseburger"
      ],
      "Created_At": "2022-11-01T09:03:19.967+00:00"
    },
    {
      "id": "restaurant2",
      "Name": "Restaurant2",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 10,
      "Loyalty_Program": true,
      "Location": [-73.988103, 40.779109],
      "Preferences": {
        "favorite_brand": "Nike",
        "shirt_size": "L"
      },
      "Top_Dishes": [
        "Hot Dog",
        "French Fries"
      ],
      "Created_At": "2022-11-02T09:03:19.967+00:00"
    },
    {
      "id": "restaurant3",
      "Name": "Restaurant3",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 3,
      "Loyalty_Program": false,
      "Location": [-73.988103, 40.779109],
      "Preferences": {
        "favorite_brand": "Nike",
        "shirt_size": "L"
      },
      "Top_Dishes": [
        "Buffalo Wings",
        "Philly Cheesesteak"
      ],
      "Created_At": "2022-11-03T09:03:19.967+00:00"
    }
  ]
}'
```

{% alert note %}
El campo `Location` utiliza el tipo de datos `geo`, que espera un array con el formato `[longitude, latitude]`.
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

El código de estado `400` podría devolver el siguiente cuerpo de respuesta. Consulta [Solución de problemas](#troubleshooting) para obtener más información sobre los errores que puedes encontrar.

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
| `ids-not-strings` | Los ID de elementos deben ser de tipo cadena. |
| `ids-not-unique` | Los ID de los elementos deben ser únicos en la solicitud. |
| `ids-too-large` | Los ID de los elementos no pueden tener más de 250 caracteres. |
| `invalid-ids` | Los ID de elementos solo pueden incluir letras, números, guiones y guiones bajos. |
| `invalid-fields` | Confirma que todos los campos que envías en la solicitud de API ya existen en el catálogo. Esto no está relacionado con el campo ID mencionado en el error. |
| `invalid-keys-in-value-object` | Las claves de objeto de elemento no pueden incluir `.` ni `$`. |
| `item-array-invalid` | `items` debe ser un array de objetos. |
| `items-missing-ids` | Algunos elementos no tienen ID de elemento. Comprueba que cada elemento tiene un ID de elemento. |
| `items-too-large` | Los valores de los elementos no pueden superar los 5.000 caracteres. |
| `request-includes-too-many-items` | Tu solicitud tiene demasiados elementos. El límite de elementos por solicitud es de 50. |
| `too-deep-nesting-in-value-object` | Los objetos de elementos no pueden tener más de 50 niveles de anidamiento. |
| `unable-to-coerce-value` | Los tipos de elementos no se pueden convertir. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting" }

{% endapi %}