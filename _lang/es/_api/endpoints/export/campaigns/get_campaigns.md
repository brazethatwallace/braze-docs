---
nav_title: "GET: Exportar lista de campañas"
article_title: "GET: Exportar lista de campañas"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto de conexión Exportar lista de campañas de Braze."

---
{% api %}
# Exportar lista de campañas {#export-campaigns-list}
{% apimethod get %}
/campaigns/list
{% endapimethod %}

> Usa este punto de conexión para exportar una lista de campañas, cada una de las cuales incluirá su nombre, el identificador de API de la campaña, si se trata de una campaña de API y las etiquetas asociadas a la campaña.

Las campañas se devuelven en grupos de 100 ordenadas por fecha de creación (de la más antigua a la más reciente, por defecto).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f3b0b3ef-04fb-4a31-8570-e6ad88dacb18 {% endapiref %}

## Requisitos previos {#prerequisites}

Para usar este punto de conexión, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key) con el permiso `campaigns.list`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | -------- | --------- | ----------- |
| `page` | Opcional | Entero | La página de campañas a devolver, predeterminada a 0 (devuelve el primer conjunto de hasta 100). |
| `include_archived` | Opcional | Booleano | Incluir o no campañas archivadas, predeterminado a false. |
| `sort_direction` | Opcional | Cadena | - Ordenar la hora de creación de más reciente a más antigua: introduce el valor `desc`.<br> - Ordenar la hora de creación de más antigua a más reciente: introduce el valor `asc`. <br><br>Si no se incluye `sort_direction`, el orden predeterminado es de la más antigua a la más reciente. |
| `last_edit.time[gt]` | Opcional | Tiempo | Filtra los resultados y solo devuelve las campañas que se hayan editado después del tiempo indicado hasta ahora. El formato es `yyyy-MM-DDTHH:mm:ss`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

## Ejemplo de solicitud {#example-request}

```
curl --location -g --request GET 'https://rest.iad-01.braze.com/campaigns/list?page=0&include_archived=false&sort_direction=desc&last_edit.time[gt]=2020-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Respuesta {#response}

```json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "campaigns" : [
        {
            "id" : (string) the Campaign API identifier,
            "last_edited": (ISO 8601 string) the last edited time for the message
            "name" : (string) the campaign name,
            "is_api_campaign" : (boolean) whether the campaign is an API campaign,
            "tags" : (array) the tag names associated with the campaign formatted as strings
        },
        ...
    ]
}
```

{% alert tip %}
Para obtener ayuda con las exportaciones CSV y API, visita [Solución de problemas de exportación]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}

{% endapi %}