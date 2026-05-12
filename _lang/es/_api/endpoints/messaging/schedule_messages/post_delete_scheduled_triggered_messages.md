---
nav_title: "POST: Eliminar campañas programadas desencadenadas por API"
article_title: "POST: Eliminar campañas programadas desencadenadas por API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto de conexión Eliminar campañas programadas desencadenadas por API de Braze."

---
{% api %}
# Eliminar campañas programadas desencadenadas por API {#delete-scheduled-api-triggered-campaigns}
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/trigger/schedule/delete
{% endapimethod %}

> Utiliza este punto de conexión para cancelar un mensaje Canvas que hayas programado previamente a través de la API antes de que se haya enviado.

Los mensajes programados o desencadenados que se eliminan cerca de la hora a la que debían enviarse o durante la misma se actualizan con el máximo esfuerzo, por lo que Braze puede aplicar eliminaciones de último momento a todos, a algunos o a ninguno de tus usuarios objetivo.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7d34037f-4bf2-4fab-bc9c-c972988051a7 {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este punto de conexión, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `campaigns.trigger.schedule.delete`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Cuerpo de la solicitud {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) the campaign identifier,
  "schedule_id": (required, string) the `schedule_id` to delete (obtained from the response to create schedule)
}
```

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Obligatorio | Cadena | Ver [identificador de campaña]({{site.baseurl}}/api/identifier_types/). |
| `schedule_id` | Obligatorio | Cadena | El `schedule_id` a eliminar (obtenido de la respuesta a crear planificación). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }


## Ejemplo de solicitud {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "schedule_id": "schedule_identifier"
}'
```

{% endapi %}