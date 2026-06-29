---
nav_title: "POST: Cambiar el estado de la suscripción por correo electrónico"
article_title: "POST: Cambiar el estado de la suscripción por correo electrónico"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto de conexión Cambiar el estado de la suscripción por correo electrónico del usuario de Braze."

---
{% api %}
# Cambiar el estado de la suscripción por correo electrónico {#change-email-subscription-status}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/email/status
{% endapimethod %}

> Utiliza este punto de conexión para establecer el estado de suscripción de correo electrónico para tus usuarios.

Los usuarios pueden ser `opted_in`, `unsubscribed` o `subscribed` (sin opción específica de inclusión o exclusión).

Puedes establecer el estado de suscripción por correo electrónico para una dirección de correo electrónico que aún no esté asociada a ninguno de tus usuarios dentro de Braze. Cuando esa dirección de correo electrónico se asocie posteriormente a un usuario, se establecerá automáticamente el estado de suscripción de correo electrónico que cargaste.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#be852462-0cda-4a48-b68b-85bd8a9f2147 {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este punto de conexión, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key) con el permiso `email.status`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Cuerpo de la solicitud {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@example.com",
  "subscription_state": "subscribed"
}
```

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `email` | Obligatorio | Cadena o matriz | Cadena de direcciones de correo electrónico a modificar, o una matriz de hasta 50 direcciones de correo electrónico a modificar. |
| `subscription_state` | Obligatorio | Cadena | "subscribed", "unsubscribed" u "opted_in". |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

## Solución de problemas de bloqueos de correo electrónico de SendGrid {#troubleshooting-sendgrid-email-blocks}

Cuando SendGrid bloquea a un destinatario, actualiza el estado de suscripción con este punto de conexión y revisa la interacción con filtros de segmento. Utiliza los eventos de rebote suave de [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) para monitorear la capacidad de entrega, y confirma el estado de suscripción antes de reintentar los envíos.

## Ejemplo de solicitud {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/status' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": "example@example.com",
  "subscription_state": "subscribed"
}'
```


{% endapi %}