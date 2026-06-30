---
nav_title: "POST: Cancelar exportaciones por segmento"
article_title: "POST: Cancelar exportaciones por segmento"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto de conexión de Braze Cancelar exportaciones por segmento."

---
{% api %}
# Cancelar exportaciones por segmento {#cancel-exports-by-segment}
{% apimethod post %}
/export/segment/cancel
{% endapimethod %}

> Utiliza este punto de conexión para cancelar todas las exportaciones en curso con un ID de segmento especificado.

## Requisitos previos {#prerequisites}

Para utilizar este punto de conexión, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key) con el permiso `segments.list`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Cuerpo de la solicitud {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "segment_id": (required, string) the `segment_id` to locate and cancel its ongoing exports
}
```

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `segment_id` | Obligatorio | Cadena | El `segment_id` para cancelar sus exportaciones en curso. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

## Ejemplo de solicitud {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/export/segment/cancel' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "segment_id": "segment_identifier"
}'
```

{% endapi %}