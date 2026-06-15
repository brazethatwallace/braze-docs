---
nav_title: "POST: Actualizar Canvas programados desencadenados por la API"
article_title: "POST: Actualizar Canvas programados desencadenados por la API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto de conexión de Braze Actualizar Canvas programados desencadenados por la API."

---
{% api %}
# Actualizar Canvas programados desencadenados por la API {#update-scheduled-api-triggered-canvases}
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/trigger/schedule/update
{% endapimethod %}

> Utiliza este punto de conexión para actualizar los Canvas programados desencadenados por la API que se crearon en el dashboard.

Esto te permite decidir qué acción desencadena el envío del mensaje. Puedes pasar `trigger_properties` que Braze utiliza como plantilla en el propio mensaje.

Ten en cuenta que para enviar mensajes con este punto de conexión, debes tener un ID de Canvas, creado cuando construyes un [Canvas]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier).

Cualquier planificación sobrescribirá completamente la que hayas proporcionado en la solicitud de creación de planificación o en anteriores solicitudes de actualización de planificación.
  - Por ejemplo, si originalmente proporcionas `"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}` y luego en tu actualización proporcionas `"schedule" : {"time" : "2015-02-20T14:14:47"}`, Braze envía tu mensaje a la hora proporcionada en UTC, no en la hora local del usuario.
  - Los desencadenantes programados que actualices cerca de la hora a la que debían enviarse o durante la misma se actualizan con el máximo esfuerzo, por lo que Braze puede aplicar cambios de último momento a todos, a algunos o a ninguno de tus usuarios objetivo.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8fdf158b-ce20-41d8-80e4-a9300a6706d4 {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este punto de conexión, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `canvas.trigger.schedule.update`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Cuerpo de la solicitud {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) see Canvas identifier,
  "schedule_id": (required, string) the `schedule_id` to update (obtained from the response to create schedule),
  "schedule": {
    // required, see create schedule documentation
  }
}
```

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `canvas_id` | Obligatorio | Cadena | Ver [identificador de Canvas]({{site.baseurl}}/api/identifier_types/). |
| `schedule_id` | Opcional | Cadena | El `schedule_id` a actualizar (obtenido de la respuesta de creación de planificación). |
| `schedule` | Obligatorio | Objeto | Ver [objeto de planificación]({{site.baseurl}}/api/objects_filters/schedule_object/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

## Ejemplo de solicitud {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "schedule_id": "schedule_identifier",
  "schedule": {
    "time": "2017-05-24T21:30:00Z",
    "in_local_time": true
  }
}'
```

{% endapi %}