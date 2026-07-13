---
nav_title: "Objeto de selección del catálogo"
article_title: Objeto de selección del catálogo API
page_order: 12
page_type: reference
description: "Este artículo de referencia explica los diferentes componentes del objeto de selección del catálogo."
tool: Catalogs

---

# Objeto de selección del catálogo {#catalog-selection-object}

> Al crear una selección de catálogo, puedes proporcionar un objeto de selección para definir los criterios de filtrado, ordenación y limitación de los elementos devueltos por tu catálogo.

El objeto `selection` te permite especificar qué elementos de tu catálogo deben incluirse en la selección según los filtros, cómo deben ordenarse y cuántos resultados devolver. Utiliza este objeto al crear selecciones de catálogo a través de la API.

## Cuerpo del objeto {#object-body}

```json
{
  "selection": {
    "name": "Sale",
    "description": "Sales Collection",
    "external_id": "12345678",
    "source": "Shopify",
    "filters": [
      {
        "field": "collection",
        "operator": "includes value",
        "value": "Best Seller"
      },
      {
        "field": "collection",
        "operator": "does not include value",
        "value": "Sale"
      }
    ],
    "results_limit": 5,
    "sort_field": "id",
    "sort_order": "asc"
  }
}
```

## Detalles del objeto {#object-details}

| Clave | Obligatorio | Tipo de datos | Descripción |
| --- | -------- | --------- | ----------- |
| `name` | Obligatorio | Cadena | El nombre de la selección del catálogo. |
| `description` | Opcional | Cadena | Una descripción de la selección del catálogo. |
| `external_id` | Obligatorio | Cadena | Un identificador único para la selección. |
| `source` | Opcional | Cadena | La fuente de los datos del catálogo. Para los catálogos de Shopify, configura este valor como `"Shopify"`. Los valores aceptados son `"Shopify"` y `"Braze"`. |
| `filters` | Opcional | Conjunto de objetos | Un conjunto de objetos de filtro que se aplican a los elementos del catálogo. Puedes especificar hasta cuatro filtros por solicitud. Si no se proporcionan filtros, se incluyen todos los elementos del catálogo. |
| `results_limit` | Opcional | Entero | El número máximo de resultados que se devolverán. Debe ser un número entre 1 y 50. |
| `sort_field` | Opcional | Cadena | El campo por el que ordenar los resultados. Debe combinarse con `sort_order`. Si no están presentes `sort_field` ni `sort_order`, los resultados se devuelven en orden aleatorio. |
| `sort_order` | Opcional | Cadena | El orden en el que clasificar los resultados. Los valores aceptados son `"asc"` (ascendente) o `"desc"` (descendente). Debe combinarse con `sort_field`. Si no están presentes `sort_field` ni `sort_order`, los resultados se devuelven en orden aleatorio. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Object details" }

### Objeto de filtro {#filter-object}

Cada objeto de filtro en el conjunto `filters` contiene los campos descritos en la siguiente tabla.

| Clave | Obligatorio | Tipo de datos                                   | Descripción |
| --- | -------- | ------------------------------------------- | ----------- |
| `field`    | Obligatorio | Cadena                                      | El campo del catálogo por el que filtrar. |
| `operator` | Obligatorio | Cadena                                      | El operador de comparación que se utilizará para filtrar. Algunos ejemplos son `"includes value"` y `"does not include value"`. |
| `value`    | Obligatorio | Varía (cadena, número, booleano, tiempo)     | El valor con el que comparar. Debe coincidir con el tipo de datos del campo del catálogo subyacente (por ejemplo, cadena, número, booleano, tiempo). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Filter object" }

{% alert note %}
La API admite un máximo de cuatro filtros por solicitud de selección. En el panel de Braze, puedes añadir hasta 10 filtros por selección. Los filtros se aplican en el orden en que aparecen en el conjunto.
{% endalert %}