---
nav_title: "GET: Exportar detalles del segmento"
article_title: "GET: Exportar detalles del segmento"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del endpoint Exportar detalles del segmento de Braze."

---
{% api %}
# Exportar detalles del segmento {#export-segment-details}
{% apimethod get %}
/segments/details
{% endapimethod %}

> Utiliza este endpoint para recuperar información relevante sobre un segmento, que puede identificarse mediante el `segment_id`.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aab56ed9-0a28-476a-8b57-b79786dbb9c1 {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `segments.details`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parámetros de la solicitud {#request-parameters}

| Parámetro    | Obligatorio | Tipo de datos | Descripción            |
| ------------ | -------- | --------- | ---------------------- |
| `segment_id` | Obligatorio | Cadena | Ver [identificador de API del segmento]({{site.baseurl}}/api/identifier_types).<br><br> El `segment_id` de un segmento determinado se puede encontrar en la página [Claves de API]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers) dentro de tu cuenta de Braze, o puedes utilizar el [endpoint Exportar lista de segmentos]({{site.baseurl}}/api/endpoints/export/segments/get_segment).  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

## Ejemplo de solicitud {#example-request}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/segments/details?segment_id={{segment_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Respuesta {#response}

```json
{
      "message": (string) returns 'success' when the request completes without errors,
      "created_at" : (string) the date created as ISO 8601 date,
      "updated_at" : (string) the date last updated as ISO 8601 date,
      "name" : (string) the segment name,
      "description" : (string) a human-readable description of filters,
      "text_description" : (string) the segment description,
      "tags" : (array) the tag names associated with the segment formatted as strings,
      "teams" : (array) the names of the Teams associated with the campaign
}
```

{% alert tip %}
Para obtener ayuda con las exportaciones CSV y API, visita [Solución de problemas de exportación]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}

{% endapi %}