---
nav_title: "GET: Listar tipos de objetos de datos"
article_title: "GET: Listar tipos de objetos de datos"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Este artículo describe los detalles del endpoint Listar tipos de objetos de datos."
---
{% api %}
# Listar tipos de objetos de datos {#list-data-object-types}
{% apimethod get %}
/data_objects/types
{% endapimethod %}

> Usa este endpoint para listar los tipos de objetos de datos en un espacio de trabajo.

{% alert important %}
Los objetos de datos se encuentran actualmente en acceso anticipado. Tu espacio de trabajo debe estar habilitado antes de que los permisos de clave de API de objetos de datos aparezcan en **Configuración** > **Claves de API**.
{% endalert %}

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitas una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `data_objects.read`.

## Límite de velocidad {#rate-limit}

Este endpoint se encuentra en el contenedor de lectura de objetos de datos con un límite predeterminado de 50 solicitudes por minuto.

## Parámetros de consulta {#query-parameters}

La siguiente tabla enumera y describe los parámetros de consulta para el endpoint `/data_objects/types`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `search_term` | Opcional | Cadena | Filtro de prefijo que no distingue entre mayúsculas y minúsculas sobre el nombre del tipo |
| `limit` | Opcional | Entero | Tamaño de página. Predeterminado `100`. Se limita de `1` a `250` |
| `offset` | Opcional | Entero | Desplazamiento. Predeterminado `0`. Los valores negativos se redondean a `0` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de consulta para listar tipos de objetos de datos" }

## Ejemplo de solicitud {#example-request}

Esta sección incluye una carga útil de ejemplo con parámetros de consulta y una solicitud cURL de ejemplo.

### Carga útil de solicitud de ejemplo {#sample-request-payload}

Usa este objeto JSON como referencia para los parámetros de consulta de esta solicitud.

```json
{
  "search_term": "acc",
  "limit": 2,
  "offset": 0
}
```

### Solicitud cURL de ejemplo {#sample-curl-request}

Este ejemplo lista los tipos de objetos de datos que coinciden con el término de búsqueda `acc`, devolviendo dos resultados por página.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/data_objects/types?search_term=acc&limit=2&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Respuesta {#response}

Esta sección incluye una respuesta exitosa de ejemplo y los campos de la respuesta.

### Ejemplo de respuesta exitosa {#example-success-response}

El código de estado `200` podría devolver el siguiente cuerpo de respuesta.

```json
{
  "items": [
    {
      "type_name": "account",
      "metadata": { "display_name_source": "name" }
    },
    {
      "type_name": "contact",
      "metadata": {}
    }
  ],
  "total_count": 2,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 100
}
```

`metadata.display_name_source` está presente cuando se ha configurado un campo de nombre de visualización para el tipo.

### Parámetros de respuesta {#response-parameters}

La siguiente tabla enumera y describe los campos en una respuesta exitosa.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `items` | Obligatorio | Array | Lista de registros de tipos de objetos de datos |
| `items[].type_name` | Obligatorio | Cadena | Nombre de máquina del tipo de objeto de datos |
| `items[].metadata` | Obligatorio | Objeto | Objeto de metadatos del tipo |
| `total_count` | Obligatorio | Entero | Número total de registros coincidentes |
| `has_more` | Obligatorio | Booleano | Si hay otra página de resultados disponible |
| `next_offset` | Opcional | Entero | Desplazamiento para la siguiente página cuando `has_more` es `true` |
| `offset` | Obligatorio | Entero | Desplazamiento de la página actual |
| `limit` | Obligatorio | Entero | Tamaño de página utilizado por la solicitud |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de respuesta para listar tipos de objetos de datos" }

## Errores {#errors}

La siguiente tabla enumera los errores comunes de este endpoint y cómo resolverlos.

| Estado | Causa | Orientación |
|---|---|---|
| `400` | Tipo o valor de parámetro de consulta no válido | Asegúrate de que `limit` y `offset` sean enteros y que todos los valores de los parámetros sean válidos. |
| `401` | Clave de API REST faltante o no válida | Verifica que el encabezado `Authorization` utilice `Bearer YOUR_REST_API_KEY` y que la clave esté activa. |
| `403` | La clave de API no tiene permiso o la solicitud está bloqueada por la lista de permitidos | Confirma que la clave tiene el permiso `data_objects.read` y que tu IP de origen está en la lista de permitidos de la clave, si está configurada. |
| `429` | Límite de velocidad excedido | Reintenta después de `X-RateLimit-Reset` y reduce la frecuencia de las solicitudes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Errores de listar tipos de objetos de datos" }
{% endapi %}