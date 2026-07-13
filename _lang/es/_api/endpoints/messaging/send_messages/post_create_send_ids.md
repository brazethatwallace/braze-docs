---
nav_title: "POST: Crear ID de envío"
article_title: "POST: Crear ID de envío"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto de conexión Crear ID de envío de Braze."

---
{% api %}
# Crear ID de envío {#create-send-ids}
{% apimethod post %}
/sends/id/create
{% endapimethod %}

> Utiliza este punto de conexión para crear ID de envío que puedan utilizarse para enviar mensajes y hacer un seguimiento del rendimiento de los mensajes mediante programación, sin necesidad de crear campañas para cada envío.

Utilizar el identificador de envío para el seguimiento y envío de mensajes es útil si piensas generar y enviar contenido mediante programación.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#74a04e53-659f-4473-abc5-0f6f735550ff {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este punto de conexión, deberás generar una clave de API con el permiso `sends.id.create`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='sends id create' %}

## Cuerpo de la solicitud {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "send_id": (optional, string) see send identifier
}
```

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Obligatorio | Cadena | Ver [identificador de campaña]({{site.baseurl}}/api/identifier_types). |
| `send_id` | Opcional | Cadena | Ver [identificador de envío]({{site.baseurl}}/api/identifier_types). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

## Ejemplo de solicitud {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/sends/id/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier"
}'
```

## Respuesta {#response}

### Ejemplo de respuesta correcta {#example-success-response}

```json
{
  "message": "success",
  "send_id" : (string) the send identifier
}
```

{% endapi %}