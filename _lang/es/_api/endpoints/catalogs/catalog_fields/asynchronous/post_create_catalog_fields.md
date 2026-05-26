---
nav_title: "POST: Crear campos de catálogo"
article_title: "POST: Crear campos de catálogo"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto de conexión Crear campos de catálogo de Braze."

---
{% api %}
# Crear campos de catálogo {#create-catalog-fields}
{% apimethod post %}
/catalogs/{catalog_name}/fields
{% endapimethod %}

> Utiliza este punto de conexión para crear varios campos en tu catálogo.

## Requisitos previos {#prerequisites}

Para utilizar este punto de conexión, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `catalogs.create_fields`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog fields' %}

## Parámetros de ruta {#path-parameters}

| Parámetro      | Obligatorio | Tipo de datos | Descripción          |
| -------------- | -------- | --------- | -------------------- |
| `catalog_name` | Obligatorio | Cadena    | Nombre del catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de ruta" }

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción                                                                                                  |
| --------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------ |
| `fields`  | Obligatorio | Matriz     | Una matriz que contiene objetos de campo. Los objetos de campo deben contener el nombre y el tipo de los nuevos campos. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de la solicitud" }

## Ejemplo de solicitud {#example-request}

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/fields' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "fields": [
    {
      "name": "Name",
      "type": "string"
    },
    {
      "name": "Ratings",
      "type": "number"
    },
    {
      "name": "Loyalty_Program",
      "type": "boolean"
    },
    {
      "name": "Created_At",
      "type": "time"
    },
    {
      "name": "Location",
      "type": "geo"
    }
  ]
}'
```

{% alert note %}
Debes proporcionar los valores de los campos de geolocalización como una matriz `[longitude, latitude]`, por ejemplo, `[-73.988103, 40.779109]`. La latitud debe estar entre -90 y 90; la longitud debe estar entre -180 y 180.
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

| Error                                | Solución de problemas                                                                                        |
|--------------------------------------|--------------------------------------------------------------------------------------------------------|
| `arbitrary-error`                    | Se ha producido un error arbitrario. Inténtalo de nuevo o ponte en contacto con [Soporte]({{site.baseurl}}/support_contact/). |
| `catalog-not-found`                  | Comprueba que el nombre del catálogo es válido.                                                                  |
| `company-size-limit-already-reached` | Se ha alcanzado el límite de tamaño de almacenamiento del catálogo.                                                             |
| `request-includes-too-many-fields`   | Cada solicitud puede admitir hasta 50 campos nuevos.                                                          |
| `catalog-exceeds-fields-limit`       | El catálogo no puede tener más de 500 campos.                                                              |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solución de problemas" }

{% endapi %}