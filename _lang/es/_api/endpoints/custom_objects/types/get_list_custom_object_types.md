---
nav_title: "GET: Listar tipos de objetos personalizados"
article_title: "GET: Listar tipos de objetos personalizados"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Este artículo describe los detalles del endpoint Listar tipos de objetos personalizados."
---
{% api %}
# Listar tipos de objetos personalizados {#list-custom-object-types}
{% apimethod get %}
/custom_objects/types
{% endapimethod %}

> Usa este endpoint para listar los tipos de objetos personalizados en un espacio de trabajo.

{% alert important %}
Los objetos personalizados se encuentran actualmente en acceso anticipado. Tu espacio de trabajo debe estar habilitado antes de que los permisos de clave de API de objetos personalizados aparezcan en **Configuración** > **Claves de API**.
{% endalert %}

## Requisitos previos {#prerequisites}

Para usar este endpoint, necesitas una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `custom_objects.read`.

## Límite de velocidad {#rate-limit}

Este endpoint se encuentra en el contenedor de lectura de objetos personalizados con un límite predeterminado de 50 solicitudes por minuto.

## Parámetros de consulta {#query-parameters}

La siguiente tabla enumera y describe los parámetros de consulta del endpoint `/custom_objects/types`.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `search_term` | Opcional | Cadena | Filtro de prefijo sin distinción entre mayúsculas y minúsculas por nombre de tipo |
| `limit` | Opcional | Entero | Tamaño de página. Predeterminado `100`. Limitado de `1` a `250` |
| `offset` | Opcional | Entero | Desplazamiento. Predeterminado `0`. Los valores negativos se redondean a `0` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de consulta de listar tipos de objetos personalizados" }

## Ejemplo de solicitud {#example-request}

Esta sección incluye un ejemplo de carga útil de parámetros de consulta y un ejemplo de solicitud cURL.

### Ejemplo de carga útil de solicitud {#sample-request-payload}

Usa este objeto JSON como referencia para los parámetros de consulta en esta solicitud.

```json
{
  "search_term": "acc",
  "limit": 2,
  "offset": 0
}
```

### Ejemplo de solicitud cURL {#sample-curl-request}

Este ejemplo lista los tipos de objetos personalizados que coinciden con el término de búsqueda `acc`, devolviendo dos resultados por página.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/custom_objects/types?search_term=acc&limit=2&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Respuesta {#response}

Esta sección incluye un ejemplo de respuesta exitosa y los campos de la respuesta.

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

`metadata.display_name_source` está presente cuando se configura un campo de nombre de visualización para el tipo.

### Parámetros de respuesta {#response-parameters}

La siguiente tabla enumera y describe los campos en una respuesta exitosa.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `items` | Obligatorio | Array | Lista de registros de tipos de objetos personalizados |
| `items[].type_name` | Obligatorio | Cadena | Nombre de máquina del tipo de objeto personalizado |
| `items[].metadata` | Obligatorio | Objeto | Objeto de metadatos del tipo |
| `total_count` | Obligatorio | Entero | Número total de registros coincidentes |
| `has_more` | Obligatorio | Booleano | Si hay otra página de resultados disponible |
| `next_offset` | Opcional | Entero | Desplazamiento para la siguiente página cuando `has_more` es `true` |
| `offset` | Obligatorio | Entero | Desplazamiento de la página actual |
| `limit` | Obligatorio | Entero | Tamaño de página utilizado por la solicitud |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de respuesta de listar tipos de objetos personalizados" }

## Errores {#errors}

La siguiente tabla enumera los errores comunes de este endpoint y cómo resolverlos.

| Estado | Causa | Orientación |
|---|---|---|
| `400` | Tipo o valor de parámetro de consulta no válido | Asegúrate de que `limit` y `offset` sean enteros y de que todos los valores de los parámetros sean válidos. |
| `401` | Clave de API REST faltante o no válida | Verifica que el encabezado `Authorization` use `Bearer YOUR_REST_API_KEY` y que la clave esté activa. |
| `403` | La clave de API no tiene permiso o la solicitud está bloqueada por la lista de permitidos | Confirma que la clave tenga el permiso `custom_objects.read` y que tu IP de origen esté en la lista de permitidos de la clave, si está configurada. |
| `429` | Límite de velocidad excedido | Vuelve a intentarlo después de `X-RateLimit-Reset` y reduce la frecuencia de las solicitudes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Errores de listar tipos de objetos personalizados" }
{% endapi %}