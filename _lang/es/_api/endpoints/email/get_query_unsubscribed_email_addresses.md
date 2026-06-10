---
nav_title: "GET: Consultar lista de direcciones de correo electrónico dadas de baja"
article_title: "GET: Consultar lista de direcciones de correo electrónico dadas de baja"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto de conexión de Braze para recuperar la lista o consultar las cancelaciones de suscripción de correo electrónico."

---
{% api %}
# Consultar lista de direcciones de correo electrónico dadas de baja {#query-list-of-unsubscribed-email-addresses}
{% apimethod get %}
/email/unsubscribes
{% endapimethod %}

> Utiliza este punto de conexión para devolver los últimos correos electrónicos que se han dado de baja durante el periodo de tiempo comprendido entre `start_date` y `end_date`. Para obtener un historial completo del estado de la suscripción, utiliza [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) para hacer un seguimiento de estos datos.

Puedes utilizar este punto de conexión para configurar una sincronización bidireccional entre Braze y otros sistemas de correo electrónico o tu propia base de datos.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d2966b81-188a-407b-ba7e-e6c252c44b4a {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este punto de conexión, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `email.unsubscribe`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| ----------|-----------| ---------|------ |
| `start_date` | Opcional <br>(ver nota) | Cadena en formato AAAA-MM-DD | Fecha de inicio del intervalo para recuperar las cancelaciones de suscripción; debe ser anterior a end_date. La API la trata como medianoche en hora UTC. |
| `end_date` | Opcional <br>(ver nota) | Cadena en formato AAAA-MM-DD | Fecha de finalización del intervalo para recuperar las cancelaciones de suscripción. La API la trata como medianoche en hora UTC. |
| `limit` | Opcional | Entero | Campo opcional para limitar el número de resultados devueltos. De forma predeterminada es 100, el máximo es 500. |
| `offset` | Opcional | Entero | Punto de inicio opcional de la lista desde el que recuperar. |
| `sort_direction` | Opcional | Cadena | Introduce el valor `asc` para ordenar las cancelaciones de suscripción de la más antigua a la más reciente. Introduce `desc` para ordenar de más reciente a más antigua. Si no se incluye `sort_direction`, el orden predeterminado es de más reciente a más antigua. |
| `email` | Opcional <br>(ver nota) | Cadena | Si se proporciona, devolveremos si el usuario se ha dado de baja o no. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

{% alert note %}
Debes proporcionar un valor para `end_date`, así como para `email` o `start_date`.
{% endalert %}

Si tu intervalo de fechas tiene más cancelaciones de suscripción que el número indicado en `limit`, tendrás que hacer varias llamadas a la API, aumentando cada vez el `offset` hasta que una llamada devuelva menos de `limit` o cero resultados.

## Ejemplo de solicitud {#example-request}
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/unsubscribes?start_date=2020-01-01&end_date=2020-02-01&limit=1&offset=1&sort_direction=desc&email=example@braze.com' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Respuesta {#response}

Las entradas aparecen en orden descendente.

```json
{
  "emails": [
    {
      "email": (string) an email that has been unsubscribed,
      "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
    },
    {
      "email": (string) an email that has been unsubscribed,
      "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
    },
    {
      "email": (string) an email that has been unsubscribed,
      "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
    }
  ],
  "message": "success"
}
```
{% endapi %}