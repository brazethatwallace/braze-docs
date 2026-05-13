---
nav_title: "GET: Mostrar el estado del grupo de suscripción de los usuarios"
article_title: "GET: Listar el estado del grupo de suscripción del usuario"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto de conexión Listar el estado del grupo de suscripción del usuario de Braze."

---
{% api %}
# Listar el estado del grupo de suscripción del usuario {#list-users-subscription-group-status}
{% apimethod get %}
/subscription/status/get
{% endapimethod %}

> Utiliza este punto de conexión para obtener el estado de suscripción de un usuario en un grupo de suscripción.

Estos grupos estarán disponibles en la página **Subscription Group**. La respuesta de este punto de conexión incluirá el ID externo y el valor suscrito, dado de baja o desconocido para el grupo de suscripción específico solicitado en la llamada a la API. Esto se puede utilizar para actualizar el estado del grupo de suscripción en posteriores llamadas a la API o para mostrarlo en una página web alojada.

Si quieres ver ejemplos o probar este punto de conexión para **Email Subscription Groups**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#488c8923-fa44-4124-9245-036d13c615f2 {% endapiref %}

Si quieres ver ejemplos o probar este punto de conexión para **SMS Subscription Groups**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

Si quieres ver ejemplos o probar este punto de conexión para **WhatsApp Groups**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este punto de conexión, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `subscription.status.get`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types/?tab=subscription%20group%20ids) | Obligatorio | Cadena | El `id` de tu grupo de suscripción. |
| `external_id` | Obligatorio* | Cadena | El `external_id` del usuario (debe incluir como mínimo uno y como máximo 50 `external_ids`). <br><br>Cuando se envían tanto un `external_id` como un `email`/`phone`, solo se aplicarán a la consulta de resultados los `external_id` proporcionados. |
| `email` | Obligatorio* | Cadena | La dirección de correo electrónico del usuario. Se puede pasar como una matriz de cadenas con un máximo de 50.<br><br> Si envías una dirección de correo electrónico y un número de teléfono (sin `external_id`), se producirá un error. |
| `phone` | Obligatorio* | Cadena en formato [E.164](https://en.wikipedia.org/wiki/E.164) | El número de teléfono del usuario. Si no se incluye el correo electrónico, deberás incluir al menos un número de teléfono (con un máximo de 50).<br><br> Si envías una dirección de correo electrónico y un número de teléfono (sin `external_id`), se producirá un error. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Request parameters" }

*Se requiere uno de `external_id`, `email` o `phone` para cada usuario.

- Para los grupos de suscripción de SMS y WhatsApp, se requiere `external_id` o `phone`. Cuando se envían ambos, solo se utiliza el `external_id` para la consulta y el número de teléfono se aplica a ese usuario.
- Para los grupos de suscripción por correo electrónico, se requiere `external_id` o `email`. Cuando se envían ambos, solo se utiliza el `external_id` para la consulta y la dirección de correo electrónico se aplica a ese usuario.

## Ejemplo de solicitud {#example-request}

{% tabs %}
{% tab Multiple Users %}
{% raw %}
```
https://rest.iad-03.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&external_id[]=1&external_id[]=2
```
{% endraw %}
{% endtab %}
{% tab SMS and WhatsApp %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&phone=+11112223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% tab Email %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&email=example@braze.com' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Respuesta {#response}

Todas las respuestas correctas devolverán `Subscribed`, `Unsubscribed` o `Unknown` dependiendo del estado y del historial del usuario con el grupo de suscripción.

```json
{
  "status": {
    "1": "Unsubscribed",
    "2": "Subscribed"
  },
  "message": "success"
}
```

{% alert important %}
Este punto de conexión devuelve el estado del grupo de suscripción de forma independiente del estado de suscripción global del usuario. Si un usuario cancela su suscripción globalmente, el panel de Braze lo muestra como dado de baja de cada grupo de suscripción. Sin embargo, este punto de conexión sigue devolviendo el último estado guardado del grupo de suscripción (por ejemplo, `Subscribed`) porque el estado global de las suscripciones sustituye a los grupos de suscripción individuales sin sobrescribirlos.<br><br>Braze conserva los estados individuales de los grupos de suscripción, de modo que, si el usuario vuelve a suscribirse globalmente, cada grupo de suscripción vuelve al estado guardado anteriormente. Para determinar el estado efectivo de la suscripción de un usuario, comprueba tanto su estado de suscripción global como el estado del grupo de suscripción devuelto por este punto de conexión.
{% endalert %}

{% endapi %}