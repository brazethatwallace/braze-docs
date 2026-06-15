---
nav_title: "GET: Consultar correos electrónicos de rebote duro"
article_title: "GET: Consultar correos electrónicos de rebote duro"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto de conexión de Braze para consultar o enumerar las direcciones de correo electrónico con rebote duro."

---
{% api %}
# Consultar correos electrónicos de rebote duro {#query-hard-bounced-emails}
{% apimethod get %}
/email/hard_bounces
{% endapimethod %}

> Utiliza este punto de conexión para obtener una lista de direcciones de correo electrónico que han tenido un "rebote duro" en tus mensajes de correo electrónico dentro de un periodo de tiempo determinado.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7c2ef84f-ddf5-451a-a72c-beeabc06ad9d {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este punto de conexión, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `email.hard_bounces`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| ----------|-----------| ----------|----- |
| `start_date` | Opcional* | Cadena en formato AAAA-MM-DD | *Se requiere `start_date` o `email`. Es la fecha de inicio del intervalo para recuperar rebotes duros y debe ser anterior a `end_date`. La API la considera medianoche en hora UTC. |
| `end_date` | Obligatorio | Cadena en formato AAAA-MM-DD | Fecha de finalización del intervalo para recuperar rebotes duros. La API la considera medianoche en hora UTC. |
| `limit` | Opcional | Número entero | Campo opcional para limitar el número de resultados devueltos. De forma predeterminada es 100, el máximo es 500. |
| `offset` | Opcional | Número entero | Punto de inicio opcional de la lista desde el que recuperar. |
| `email` | Opcional* | Cadena | *Se requiere `start_date` o `email`. Si se proporciona, devolveremos si el usuario ha tenido un rebote duro o no. Comprueba que las cadenas de correo electrónico tienen el formato adecuado. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Request parameters" }

{% alert important %}
Debes proporcionar un `end_date`, y un `email` o un `start_date`. Si proporcionas los tres, `start_date`, `end_date` y un `email`, damos prioridad a los correos electrónicos proporcionados y no tenemos en cuenta el intervalo de fechas.
{% endalert %}

Si tu intervalo de fechas tiene más del número `limit` de rebotes duros, tendrás que hacer varias llamadas a la API, aumentando cada vez el `offset` hasta que una llamada devuelva menos de `limit` o cero resultados. Incluir los parámetros `offset` y `limit` con `email` puede devolver una respuesta vacía.

## Ejemplo de solicitud {#example-request}
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Respuesta {#response}
Las entradas aparecen en orden descendente.

```json
{
  "emails": [
    {
      "email": (string) an email that has hard bounced,
      "hard_bounced_at": (string) the time the email hard bounced in ISO 8601
    },
    {
      "email": (string) an email that has hard bounced,
      "hard_bounced_at": (string) the time the email hard bounced in ISO 8601
    },
    {
      "email": (string) an email that has hard bounced,
      "hard_bounced_at": (string) the time the email hard bounced in ISO 8601
    }
  ],
  "message": "success"
}
```
{% endapi %}