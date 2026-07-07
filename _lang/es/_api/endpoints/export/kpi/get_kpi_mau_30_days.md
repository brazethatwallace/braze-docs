---
nav_title: "GET: Exportar los usuarios activos mensuales de los últimos 30 días"
article_title: "GET: Exportar usuarios activos mensuales de los últimos 30 días"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto de conexión Exportar usuarios activos al mes de Braze."

---
{% api %}
# Exportar los usuarios activos mensuales de los últimos 30 días {#export-monthly-active-users-for-last-30-days}
{% apimethod get %}
/kpi/mau/data_series
{% endapimethod %}

> Utiliza este punto de conexión para recuperar una serie diaria del número total de usuarios activos únicos durante una ventana móvil de 30 días.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#68f45461-3bf1-425c-b918-f0bbf3f87149 {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este punto de conexión, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key) con el permiso `kpi.mau.data_series`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| -------- | -------- | --------- | ----------- |
| `length` | Obligatorio | Entero | Número máximo de días antes de `ending_at` a incluir en la serie devuelta. Debe estar comprendido entre 1 y 100 (ambos inclusive). |
| `ending_at` | Opcional | Fecha y hora <br>(cadena [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Fecha en la que debe finalizar la serie de datos. De forma predeterminada, corresponde a la hora de la solicitud. |
| `app_id` | Opcional | Cadena | Identificador de API de la aplicación recuperado de la página [Claves de API]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers). Si se excluye, se devolverán los resultados de todas las aplicaciones del espacio de trabajo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

## Ejemplo de solicitud {#example-request}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/kpi/mau/data_series?length=7&ending_at=2018-06-28T23:59:59-05:00&app_id={{app_identifier}}' \
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
            "mau" : (int) the number of monthly active users
        },
        ...
    ]
}
```

{% alert tip %}
Para obtener ayuda con las exportaciones CSV y API, visita [Solución de problemas de exportación]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}

{% endapi %}