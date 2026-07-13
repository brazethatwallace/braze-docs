---
nav_title: "GET: Listar próximas Campaigns y Canvas programados"
article_title: "GET: Listar próximas Campaigns y Canvas programados"
search_tag: Endpoint
page_order: 0
layout: api_page
page_type: reference
description: "Este artículo describe los detalles del punto de conexión de Braze para listar próximas Campaigns y Canvas programados."

---
{% api %}
# Listar próximas Campaigns y Canvas programados {#list-upcoming-scheduled-campaigns-and-canvases}
{% apimethod get %}
/messages/scheduled_broadcasts
{% endapimethod %}

> Usa este punto de conexión para devolver una lista JSON de información sobre Campaigns programadas y Canvas de entrada entre ahora y un `end_time` designado especificado en la solicitud.

Los mensajes diarios y recurrentes solo aparecerán una vez con su siguiente ocurrencia. Los resultados devueltos en este punto de conexión incluyen Campaigns y Canvas creados y programados en el panel de Braze.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6f623cc3-383b-4bf7-b14d-7c56fc5562f5 {% endapiref %}

## Requisitos previos {#prerequisites}

Para usar este punto de conexión, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key) con el permiso `messages.schedule_broadcasts`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | -------- | --------- | ----------- |
| `end_time` | Obligatorio | Cadena en formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) | Fecha de fin del intervalo para recuperar las próximas Campaigns y Canvas programados. La API lo considera medianoche en hora UTC. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

## Ejemplo de solicitud {#example-request}
```
curl --location --request GET 'https://rest.iad-01.braze.com/messages/scheduled_broadcasts?end_time=2018-09-01T00:00:00-04:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Respuesta {#response}

```json
{
  "scheduled_broadcasts": [
    {
      "name": (string) the name of the scheduled broadcast,
      "id": (stings) the Canvas or campaign identifier,
      "type": (string) the broadcast type either Canvas or Campaign,
      "tags": (array) an array of tag names formatted as strings,
      "next_send_time": (string) The next send time formatted in ISO 8601, may also include time zone if not local/intelligent delivery,
      "schedule_type": (string) The schedule type, either local_time_zones, intelligent_delivery or the name of your company's time zone
    }
  ]
}
```

{% endapi %}