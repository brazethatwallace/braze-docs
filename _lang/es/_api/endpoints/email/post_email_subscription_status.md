---
nav_title: "POST: Cambiar el estado de la suscripción por correo electrónico"
article_title: "POST: Cambiar el estado de la suscripción por correo electrónico"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del endpoint de Braze Cambiar el estado de la suscripción por correo electrónico del usuario."

---
{% api %}
# Cambiar el estado de la suscripción por correo electrónico {#change-email-subscription-status}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/email/status
{% endapimethod %}

> Utiliza este endpoint para establecer el estado global de suscripción de correo electrónico para tus usuarios.

Los usuarios pueden ser `opted_in`, `unsubscribed` o `subscribed` (sin opción específica de inclusión o exclusión).

{% alert note %}
Este endpoint actualiza el estado global de suscripción de correo electrónico del usuario, que es diferente del estado del grupo de suscripción. El estado global de suscripción se aplica a todos los correos electrónicos, mientras que los [grupos de suscripción]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups) permiten un control más granular sobre tipos específicos de correos electrónicos. Cuando un usuario cancela su suscripción de forma global, no recibirá correos electrónicos independientemente del estado de su grupo de suscripción. Para consultar el estado del grupo de suscripción, utiliza el [endpoint Listar el estado del grupo de suscripción del usuario]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status).
{% endalert %}

Puedes establecer el estado de suscripción por correo electrónico para una dirección de correo electrónico que aún no esté asociada a ninguno de tus usuarios dentro de Braze. Cuando esa dirección de correo electrónico se asocie posteriormente a un usuario, se establecerá automáticamente el estado de suscripción de correo electrónico que cargaste.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#be852462-0cda-4a48-b68b-85bd8a9f2147 {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `email.status`.

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
| `email` | Obligatorio | Cadena o matriz | Cadena de dirección de correo electrónico a modificar, o una matriz de hasta 50 direcciones de correo electrónico a modificar. |
| `subscription_state` | Obligatorio | Cadena | "subscribed", "unsubscribed" u "opted_in". |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

## Solución de problemas de bloqueos de correo electrónico de SendGrid {#troubleshooting-sendgrid-email-blocks}

Cuando SendGrid bloquea a un destinatario, actualiza el estado de suscripción con este endpoint y revisa la participación con filtros de segmento. Utiliza los eventos de rebote suave de [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) para monitorear la capacidad de entrega, y confirma el estado de suscripción antes de reintentar los envíos.

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