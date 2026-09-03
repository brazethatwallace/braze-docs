---
nav_title: "POST: Actualizar Campaigns programadas activadas por API"
article_title: "POST: Actualizar Campaigns programadas activadas por API"
search_tag: Endpoint
page_order: 4
layout: api_page
description: "En este artículo se describen los detalles del endpoint de Braze Actualizar Campaigns programadas activadas por API."

---
{% api %}
# Actualizar Campaigns programadas activadas por API {#update-scheduled-api-triggered-campaigns}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/campaigns/trigger/schedule/update
{% endapimethod %}

> Usa este endpoint para actualizar las Campaigns programadas activadas por API creadas en el panel, lo que te permite decidir qué acción debe desencadenar el envío del mensaje.

Puedes pasar `trigger_properties` que Braze incluye como plantilla en el propio mensaje.

Ten en cuenta que para enviar mensajes con este endpoint, debes tener un ID de Campaign, creado al crear una [Campaign activada por API]({{site.baseurl}}/api/api_campaigns).

Cualquier programación sobrescribe completamente la que proporcionaste en la solicitud de creación de programación o en las solicitudes de actualización de programación anteriores. Por ejemplo, si originalmente estableces la programación en `"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}` y más tarde la actualizas a `"schedule" : {"time" : "2015-02-20T14:14:47"}`, Braze envía el mensaje a la hora especificada en UTC, no en la hora local del usuario.

Los desencadenantes programados que se actualizan cerca de la hora a la que debían enviarse, o durante la misma, se actualizan con el máximo esfuerzo para que Braze pueda aplicar los cambios de último momento a todos, algunos o ninguno de tus usuarios objetivo. Las actualizaciones no se aplican si la programación original utilizaba la hora local y la hora original ya ha pasado en cualquier zona horaria.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6d2a6e66-9d6f-4ae1-965a-79fa52b86b1d {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `campaigns.trigger.schedule.update`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Cuerpo de la solicitud {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "schedule_id": (required, string) the `schedule_id` to update (obtained from the response to create schedule),
  "schedule": {
    // required, see create schedule documentation
  }
}
```

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Obligatorio | Cadena | Ver [identificador de Campaign]({{site.baseurl}}/api/identifier_types) |
| `schedule_id` | Obligatorio | Cadena | El `schedule_id` a actualizar (obtenido de la respuesta para crear una programación). |
| `schedule` | Obligatorio | Objeto | Ver [objeto de programación]({{site.baseurl}}/api/objects_filters/schedule_object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

## Ejemplo de solicitud {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "schedule_id": "schedule_identifier",
  "schedule": {
    "time": "2017-05-24T21:30:00Z",
    "in_local_time": true
  }
}'
```

{% endapi %}