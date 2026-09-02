---
nav_title: "GET: Consultar números de teléfono no válidos"
article_title: "GET: Consultar números de teléfono no válidos"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del endpoint de Braze Consultar números de teléfono no válidos."
---
{% api %}
# Consultar números de teléfono no válidos {#query-invalid-phone-numbers}
{% apimethod get %}
/servicio de mensajes cortos/invalid_phone_numbers
{% endapimethod %}

> Utiliza este endpoint para obtener una lista de números de teléfono que se han marcado como "no válidos" en un periodo de tiempo determinado. Consulta la documentación [Manejo de números de teléfono no válidos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#handling-invalid-phone-numbers) para obtener más información.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81ceae19-15d1-4ac1-ad22-a6b86a92456d {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) con el permiso `sms.invalid_phone_numbers`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| ----------|-----------| ----------|----- |
| `start_date` | Opcional <br>(ver nota) | Cadena en formato AAAA-MM-DD | Fecha de inicio del intervalo para recuperar números de teléfono no válidos, debe ser anterior a `end_date`. La API la considera medianoche en hora UTC. |
| `end_date` | Opcional <br>(ver nota) | Cadena en formato AAAA-MM-DD | Fecha final del intervalo para recuperar números de teléfono no válidos. La API la considera medianoche en hora UTC. |
| `limit` | Opcional | Entero | Campo opcional para limitar el número de resultados devueltos. De forma predeterminada es 100, el máximo es 500. |
| `offset` | Opcional | Entero | Punto de inicio opcional de la lista desde el que recuperar. |
| `phone_numbers` | Opcional <br>(ver nota) | Matriz de cadenas en formato e.164 | Si lo proporcionas, te devolveremos el número de teléfono si se comprueba que no es válido. |
| `reason` | Opcional <br>(ver nota) | Cadena | Los valores disponibles son "provider_error" (el error del proveedor indica que el teléfono no puede recibir servicio de mensajes cortos) o "deactivated" (el número de teléfono ha sido desactivado). Si se omite, se devuelven todas las razones. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

{% alert note %}
Debes proporcionar un `start_date` y un `end_date` O `phone_numbers`. Si proporcionas los tres, `start_date`, `end_date` y `phone_numbers`, damos prioridad a los números de teléfono indicados y no tenemos en cuenta el intervalo de fechas.
{% endalert %}

Si tu intervalo de fechas tiene un número de teléfonos no válidos superior a `limit`, tendrás que realizar varias llamadas a la API aumentando `offset` cada vez hasta que una llamada devuelva menos de `limit` o cero resultados.

## Ejemplo de solicitud {#example-request}
```
curl --location --request GET 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&phone_numbers[]=12345678901' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Respuesta {#response}
Las entradas aparecen en orden descendente.

```json
{
  "sms": [
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
      "reason" : "provider_error"
    },
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
      "reason" : "deactivated"
    },
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
      "reason" : "provider_error"
    }
  ],
  "message": "success"
}
```
{% endapi %}