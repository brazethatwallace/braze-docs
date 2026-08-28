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
| `name` | Obligatorio | String | El nombre de la selección de catálogo. |
| `description` | Opcional | String | Una descripción de la selección de catálogo. |
| `external_id` | Opcional | String | Un identificador único para la selección. |
| `source` | Opcional | String | La fuente de los datos del catálogo. Para catálogos de Shopify, configura este valor como `"Shopify"`. Los valores aceptados son `"Shopify"` y `"Braze"`. |
| `filters` | Obligatorio | Matriz de objetos | Una matriz de objetos de filtro que se aplicará a los elementos del catálogo. Puedes especificar hasta diez filtros por solicitud. Si se proporciona una matriz vacía de filtros, se incluyen todos los elementos del catálogo. |
| `results_limit` | Obligatorio | Entero | El número máximo de resultados a devolver. Debe ser un número entre 1 y 50. |
| `sort_field` | Opcional | String | El campo por el que se ordenan los resultados. Debe emparejarse con `sort_order`. Si tanto `sort_field` como `sort_order` no están presentes, los resultados se devuelven en orden aleatorio. |
| `sort_order` | Opcional | String | El orden en que se clasifican los resultados. Los valores aceptados son `"asc"` (ascendente) o `"desc"` (descendente). Debe emparejarse con `sort_field`. Si tanto `sort_field` como `sort_order` no están presentes, los resultados se devuelven en orden aleatorio. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Detalles del objeto" }

### Objeto de filtro {#filter-object}

Cada objeto de filtro en la matriz `filters` contiene los campos descritos en la siguiente tabla.

| Clave | Obligatorio | Tipo de datos                                   | Descripción |
| --- | -------- | ------------------------------------------- | ----------- |
| `field`    | Obligatorio | String                                      | El campo del catálogo por el que se filtra. |
| `operator` | Obligatorio | String                                      | El operador de comparación que se usa para filtrar. Por ejemplo, `"includes value"` y `"does not include value"`. |
| `value`    | Obligatorio | Variable (cadena, número, booleano, hora)     | El valor con el que se compara. Debe coincidir con el tipo de datos del campo subyacente del catálogo (por ejemplo, cadena, número, booleano, hora). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Objeto de filtro" }

{% alert note %}
La API admite un máximo de diez filtros por solicitud de selección. Los filtros se aplican en el orden en que aparecen en la matriz.
{% endalert %}