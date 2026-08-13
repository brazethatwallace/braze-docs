---
nav_title: "GET: Generar URL del centro de preferencias"
article_title: "GET: Generar URL del centro de preferencias"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del endpoint Generar URL del centro de preferencias de Braze."

---
{% api %}
# Generar URL del centro de preferencias {#generate-preference-center-url}
{% apimethod get %}
/preference_center/v1/{preferenceCenterExternalID}/url/{userID}
{% endapimethod %}

> Usa este endpoint para generar una URL para un centro de preferencias.

La URL de cada centro de preferencias es única para cada usuario.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0bc750ff-068e-4391-897e-6eddca2561cd {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `preference_center.user.get`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='get preference center' %} Este límite de velocidad es fijo y no es configurable.

## Parámetros de ruta {#path-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
|`preferenceCenterExternalID`| Obligatorio | Cadena | El ID de tu centro de preferencias. |
|`userID`| Obligatorio | Cadena | El ID de usuario. |
{: aria-label="Parámetros de ruta" }

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `preference_center_api_id`| Obligatorio | Cadena | El ID de tu centro de preferencias. |
| `external_id`| Obligatorio | Cadena | El ID externo de un usuario. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

## Ejemplo de solicitud {#example-request}

```
curl --location --request GET 'https://rest.iad-01.braze.com/preference_center/v1/$preference_center_external_id/url/$user_external_id' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Respuesta {#response}

```json
{
  "preference_center_url": "https://www.example.com/preferences"
}
```

{% endapi %}

{% alert note %}
Este endpoint solo genera URL para el nuevo centro de preferencias (como los centros de preferencias creados mediante nuestra API o el editor de arrastrar y soltar).
{% endalert %}