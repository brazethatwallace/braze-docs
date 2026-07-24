---
nav_title: "GET: Exportar lista de segmentos"
article_title: "GET: Exportar lista de segmentos"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del endpoint Exportar la lista de segmentos de Braze."

---
{% api %}
# Exportar lista de segmentos {#export-segment-list}
{% apimethod get %}
/segments/list
{% endapimethod %}

> Utiliza este endpoint para exportar una lista de segmentos, cada uno de los cuales incluirá su nombre, identificador de API de Segment y si tiene habilitado el seguimiento de análisis.

Los segmentos se devuelven en grupos de 100 ordenados por hora de creación (de más antiguo a más reciente de forma predeterminada). No se incluyen los segmentos archivados.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1349e6f4-3ce7-4e60-b3e9-951c99c0993f {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `segments.list`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| -------- | -------- | --------- | ----------- |
| `page` | Opcional | Entero | La página de segmentos a devolver, de forma predeterminada es 0 (devuelve el primer conjunto de hasta 100). |
| `sort_direction` | Opcional | Cadena | - Ordenar la hora de creación de más reciente a más antigua: introduce el valor `desc`.<br> - Ordenar la hora de creación de más antiguo a más reciente: introduce el valor `asc`. <br><br>Si no se incluye `sort_direction`, el orden predeterminado es de más antiguo a más reciente. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

## Ejemplo de solicitud {#example-request}
```
curl --location --request GET 'https://rest.iad-01.braze.com/segments/list?page=1&sort_direction=desc' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Respuesta {#response}

```json
{
    "message": (string) returns 'success' when the request completes without errors,
    "segments" : [
        {
            "id" : (string) the Segment API identifier,
            "name" : (string) segment name,
            "analytics_tracking_enabled" : (boolean) whether the segment has analytics tracking enabled,
            "tags" : (array) the tag names associated with the segment formatted as strings
        },
        ...
    ]
}
```

{% alert tip %}
Para obtener ayuda con las exportaciones CSV y API, visita [Solución de problemas de exportación]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}

{% endapi %}