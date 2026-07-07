---
nav_title: "POST: Eliminar Canvas programados desencadenados por API"
article_title: "POST: Eliminar Canvas programados desencadenados por API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto de conexión Eliminar Canvas programados desencadenados por API de Braze."

---
{% api %}
# Eliminar Canvas programados desencadenados por API {#delete-scheduled-api-triggered-canvases}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/canvas/trigger/schedule/delete
{% endapimethod %}

> El punto de conexión para eliminar la programación te permite cancelar un mensaje que hayas programado previamente a través de Canvas desencadenados por API antes de que se haya enviado.

Los mensajes programados o desencadenados que se eliminan cerca de la hora a la que debían enviarse o durante la misma se actualizan con el máximo esfuerzo, por lo que Braze puede aplicar eliminaciones de último momento a todos, a algunos o a ninguno de tus usuarios objetivo.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7d34037f-4bf2-4fab-bc9c-c972988051a7 {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este punto de conexión, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key) con el permiso `canvas.trigger.schedule.delete`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Cuerpo de la solicitud {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) the Canvas identifier,
  "schedule_id": (required, string) the `schedule_id` to delete (obtained from the response to create schedule)
}
```

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `canvas_id` | Obligatorio | Cadena | Ver [identificador de Canvas]({{site.baseurl}}/api/identifier_types). |
| `schedule_id` | Obligatorio | Cadena | El `schedule_id` a eliminar (obtenido de la respuesta a crear programación). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }


## Ejemplo de solicitud {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "schedule_id": "schedule_identifier"
}'
```

{% endapi %}