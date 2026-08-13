---
nav_title: "GET: Lista de grupos de suscripción de usuarios"
article_title: "GET: Lista de grupos de suscripción de usuarios"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del endpoint de Braze Lista de grupos de suscripción de usuarios."

---
{% api %}
# Lista de grupos de suscripción del usuario {#list-users-subscription-groups}
{% apimethod get %}
/subscription/user/status
{% endapimethod %}

> Utiliza este endpoint para listar y obtener los grupos de suscripción con el historial de un determinado usuario.

Si quieres ver ejemplos o probar este endpoint para **grupos de suscripción por correo electrónico**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d1c3b617-22f1-47bf-9ee8-499526824470 {% endapiref %}

Si quieres ver ejemplos o probar este endpoint para **grupos de suscripción SMS**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

Si quieres ver ejemplos o probar este endpoint para **grupos de WhatsApp**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `subscription.groups.get`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `external_id` | Obligatorio | Cadena | El `external_id` del usuario (debe incluir al menos uno y como máximo 50 `external_ids`). |
| `email` | Obligatorio* | Cadena | La dirección de correo electrónico del usuario, puede pasarse como una matriz de cadenas. Debe incluir al menos una dirección de correo electrónico (con un máximo de 50). |
| `phone` | Obligatorio* | Cadena en formato [E.164](https://en.wikipedia.org/wiki/E.164) | El número de teléfono del usuario. Debe incluir al menos un número de teléfono (con un máximo de 50). |
| `limit` | Opcional | Entero | El límite del número máximo de resultados devueltos. El `limit` predeterminado (y máximo) es 100. |
| `offset` | Opcional | Entero | Número de plantillas que saltar antes de devolver el resto de plantillas que se ajustan a los criterios de búsqueda. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

{% alert tip %}
Si hay varios usuarios (varios `external_ids`) que comparten la misma dirección de correo electrónico, todos los usuarios serán devueltos como usuarios separados (aunque tengan la misma dirección de correo electrónico o grupo de suscripción).
{% endalert %}

## Ejemplo de solicitud {#example-request}

{% tabs %}
{% tab Multiple Users %}
{% raw %}
`https://rest.iad-03.braze.com/subscription/user/status?external_id[]=1&external_id[]=2`
{% endraw %}
{% endtab %}
{% tab SMS and WhatsApp %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/user/status?external_id={{external_id}}&limit=100&offset=1&phone=+11112223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% tab Email %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/user/status?external_id={{external_id}}&email=example@example.com&limit=100&offset=0' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Ejemplo de respuesta {#example-response}

Solo se incluirán en una respuesta correcta los grupos de suscripción que hayan tenido una actualización del estado de suscripción en el historial de un usuario. Esto significa que los grupos de suscripción recién creados no aparecerán en la lista.

```json
{
    "users": [
        {
            "email": "test@example.com",
            "phone": "+11112223333",
            "external_id": "external_identifier",
            "subscription_groups": [
                {
                  "id": "ec2fcc919fca",
                  "name": "ActivationGroup",
                  "channel": "email",
                  "status": "Subscribed"
                },
                {
                  "id": "7d7af9dd5556",
                  "name": "ReactivationGroup",
                  "channel": "email",
                  "status": "Subscribed"
                },
                {
                  "id": "a5e84fd16220",
                  "name": "MarketingGroup",
                  "channel": "sms",
                  "status": "Unsubscribed"
                },
                {
                  "id": "64d8cad9176c",
                  "name": "TransactionalGroup",
                  "channel": "sms",
                  "status": "Unsubscribed"
                },
                {
                  "id": "b2134cd63942",
                  "name": "BankerMarketingGroup",
                  "channel": "sms",
                  "status": "Subscribed"
                }
            ]
        }
    ],
    "total_count": 1,
    "message": "success"
}
```

{% endapi %}