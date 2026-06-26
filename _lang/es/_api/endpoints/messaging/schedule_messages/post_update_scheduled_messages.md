---
nav_title: "POST: Actualizar mensajes programados"
article_title: "POST: Actualizar mensajes programados"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto de conexión Actualizar mensajes programados de Braze."

---
{% api %}
# Actualizar mensajes programados {#update-scheduled-messages}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/messages/schedule/update
{% endapimethod %}

> Utiliza este punto de conexión para actualizar los mensajes programados.

Este punto de conexión acepta actualizaciones de los parámetros `schedule`, `messages` o ambos. Tu solicitud debe contener al menos una de esas dos claves.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f61edf74-4467-4551-b9c4-a4b8d188cd7a {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este punto de conexión, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `messages.schedule.update`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Cuerpo de la solicitud {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "schedule_id": (required, string) the `schedule_id` to update (obtained from the response to create schedule),
  "schedule": {
    // optional, see create schedule documentation
  },
  "messages": {
    // optional, see available messaging objects documentation
  }
}
```
## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `schedule_id` | Obligatorio | Cadena | El `schedule_id` a actualizar (obtenido de la respuesta de crear planificación). |
| `schedule` | Opcional | Objeto | Ver [objeto de planificación]({{site.baseurl}}/api/objects_filters/schedule_object/). |
| `messages` | Opcional | Objeto | Ver [objetos de mensajería disponibles]({{site.baseurl}}/api/objects_filters/#messaging-objects). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

## Ejemplo de solicitud {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "schedule_id": "schedule_identifier",
  "schedule": {
    "time": "2017-05-24T20:30:36Z"
   },
  "messages": {
    "apple_push": {
      "alert": "Updated Message!",
      "badge": 1
    },
    "android_push": {
      "title": "Updated title!",
      "alert": "Updated message!"
    },
    "sms": {
      "subscription_group_id": "subscription_group_identifier",
      "message_variation_id": "message_variation_identifier",
      "body": "This is my SMS body.",
      "app_id": "app_identifier"
    }
  }
}'
```

{% endapi %}