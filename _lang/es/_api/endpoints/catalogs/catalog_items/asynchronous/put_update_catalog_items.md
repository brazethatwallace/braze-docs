---
nav_title: "PUT: Sustituir varios elementos del catálogo"
article_title: "PUT: Sustituir varios elementos del catálogo"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto de conexión de Braze Sustituir varios elementos del catálogo."

---
{% api %}
# Sustituir elementos del catálogo {#replace-catalog-items}
{% apimethod put %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> Utiliza este punto de conexión para sustituir varios elementos de tu catálogo.

Si un elemento del catálogo no existe, este punto de conexión creará el elemento en tu catálogo. Cada solicitud puede admitir hasta 50 elementos de catálogo. Este punto de conexión es asíncrono.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#ab30a4fc-60bc-4460-885c-1b92af8bc061 {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este punto de conexión, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key) con el permiso `catalogs.replace_items`.

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
| `items` | Obligatorio | Matriz | Una matriz que contiene objetos de elementos. Cada objeto debe tener un ID. Los objetos de elementos deben contener campos que existan en el catálogo. Se permiten hasta 50 objetos de elementos por solicitud. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de la solicitud" }

## Ejemplo de solicitud {#example-request}

```
curl --location --request PUT 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
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
      "Top_Dishes": [
        "Hamburger",
        "Deluxe Cheeseburger"
      ],
      "Open_Time": "2021-09-03T09:03:19.967+00:00"
    },
    {
      "id": "restaurant3",
      "City": "San Francisco",
      "Rating": 2,
      "Top_Dishes": [
        "Hot Dog",
        "French Fries"
      ]
    }
  ]
}'
```

{% alert note %}
El campo `Location` utiliza el tipo de datos `geo`, que espera una matriz con el formato `[longitude, latitude]`.
{% endalert %}

## Respuesta {#response}

Existen tres respuestas de código de estado para este punto de conexión: `202`, `400` y `404`.

{% alert note %}
El sistema también puede devolver una respuesta `400` si tu empresa ha alcanzado su límite de almacenamiento del catálogo. La versión gratuita de los catálogos tiene un límite de 100&nbsp;MB. Para más información sobre los niveles de almacenamiento y cómo actualizar, consulta [Limitaciones de almacenamiento de datos]({{site.baseurl}}/user_guide/data/activation/catalogs#data-storage-limitations).
{% endalert %}

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
| `company-size-limit-already-reached` | Se ha alcanzado el límite de almacenamiento del catálogo. Para obtener más información sobre los niveles de almacenamiento, consulta [Limitaciones de almacenamiento de datos]({{site.baseurl}}/user_guide/data/activation/catalogs#data-storage-limitations). |
| `company-size-limit-surge` | La solicitud supera el almacenamiento restante del catálogo de tu empresa. Inténtalo de nuevo con una actualización más pequeña. Para obtener más información sobre los niveles de almacenamiento, consulta [Limitaciones de almacenamiento de datos]({{site.baseurl}}/user_guide/data/activation/catalogs#data-storage-limitations). |
| `ids-not-string` | Confirma que el ID de cada elemento es una cadena. |
| `ids-not-unique` | Comprueba que el ID de cada elemento es único. |
| `ids-too-large` | El límite de caracteres para cada ID de elemento es de 250 caracteres. |
| `item-array-invalid` | `items` debe ser una matriz de objetos. |
| `items-missing-ids` | Algunos elementos no tienen ID de elemento. Confirma que cada elemento tiene un ID. |
| `items-too-large` | Los valores de los elementos no pueden superar los 5000 caracteres. |
| `invalid-ids` | Los caracteres admitidos para los nombres de ID de elementos son letras, números, guiones y guiones bajos. |
| `invalid-fields` | Confirma que todos los campos que estás enviando en la solicitud de API ya existen en el catálogo. Esto no está relacionado con el campo ID mencionado en el error. |
| `invalid-keys-in-value-object` | Las claves de objeto de elemento no pueden incluir `.` ni `$`. |
| `too-deep-nesting-in-value-object` | Los objetos de elemento no pueden tener más de 50 niveles de anidamiento. |
| `request-includes-too-many-items` | Tu solicitud tiene demasiados elementos. El límite de elementos por solicitud es de 50. |
| `unable-to-coerce-value` | Los tipos de elemento no se pueden convertir. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solución de problemas" }

{% endapi %}