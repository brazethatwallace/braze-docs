---
nav_title: "GET: Exportar análisis de segmentos"
article_title: "GET: Exportar análisis de segmentos"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del endpoint Exportar análisis de segmentos de Braze."

---
{% api %}
# Exportar análisis de segmentos {#export-segment-analytics}
{% apimethod get %}
/segments/data_series
{% endapimethod %}

> Usa este endpoint para recuperar una serie diaria del tamaño estimado de un segmento a lo largo del tiempo. <br><br>Si necesitas el tamaño exacto de un segmento, exporta sus usuarios con el [endpoint `/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) y cuenta los perfiles exportados.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#62d9d142-cdec-4aea-a287-c13efea7415e {% endapiref %}

## Requisitos previos {#prerequisites}

Para usar este endpoint, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `segments.data_series`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | -------- | --------- | ----------- |
| `segment_id` | Obligatorio | Cadena | Consulta [Identificador de API de segmento]({{site.baseurl}}/api/identifier_types).<br><br> El `segment_id` de un segmento determinado se puede encontrar en la página [Claves de API]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers) dentro de tu cuenta de Braze, o puedes usar el [endpoint Exportar lista de segmentos]({{site.baseurl}}/api/endpoints/export/segments/get_segment).  |
| `length` | Obligatorio | Entero | Número máximo de días antes de `ending_at` a incluir en la serie devuelta. Debe estar comprendido entre 1 y 100 (ambos inclusive). |
| `ending_at` | Opcional | Fecha y hora <br>(cadena [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Fecha en la que debe finalizar la serie de datos. De forma predeterminada, corresponde a la hora de la solicitud. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

## Ejemplo de solicitud {#example-request}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/segments/data_series?segment_id={{segment_identifier}}&length=14&ending_at=2018-06-27T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Respuesta {#response}

```json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) the date as ISO 8601 date,
            "size" : (int) the size of the segment on that date
        },
        ...
    ]
}
```

{% alert tip %}
Para obtener ayuda con las exportaciones CSV y API, visita [Solución de problemas de exportación]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}

{% endapi %}