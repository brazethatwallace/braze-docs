---
nav_title: "GET: Listar centros de preferencias"
article_title: "GET: Listar centros de preferencias"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del endpoint Listar centros de preferencias de Braze."

---
{% api %}
# Listar centros de preferencias {#list-preference-centers}
{% apimethod get %}
/preference_center/v1/list
{% endapimethod %}

> Utiliza este endpoint para listar tus centros de preferencias disponibles.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#dd8f6667-5eba-4e19-a29e-ba74644c0b8e {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `preference_center.list`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='get centro de preferencias' %}

## Parámetros de ruta y solicitud {#path-and-request-parameters}

No hay parámetros de ruta o solicitud para este endpoint.

## Ejemplo de solicitud {#example-request}

```
curl --location -g --request GET https://rest.iad-01.braze.com/preference_center/v1/list \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Respuesta {#response}

```json
{
  "preference_centers": [
    {
      "name": "My Preference Center 1",
      "preference_center_api_id": "preference_center_api_id",
      "created_at": "2022-08-17T15:46:10Z",
      "updated_at": "2022-08-17T15:46:10Z"
    },
    {
      "name": "My Preference Center 2",
      "preference_center_api_id": "preference_center_api_id",
      "created_at": "2022-08-19T11:13:06Z",
      "updated_at": "2022-08-19T11:13:06Z"
    },
    {
      "name": "My Preference Center 3",
      "preference_center_api_id": "preference_center_api_id",
      "created_at": "2022-08-19T11:30:50Z",
      "updated_at": "2022-08-19T11:30:50Z"
    },
    {
      "name": "My Preference Center 4",
      "preference_center_api_id": "preference_center_api_id",
      "created_at": "2022-09-13T20:41:34Z",
      "updated_at": "2022-09-13T20:41:34Z"
    }
  ]
}
```

{% endapi %}