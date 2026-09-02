---
nav_title: "POST: Registrar eventos de análisis de Banner"
article_title: "POST: Registrar eventos de análisis de Banner"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Usa este endpoint para registrar eventos de impresión, clic y descarte para Banners."
hidden: true
---

{% api %}
# Registrar eventos de análisis de Banner {#track-banner-analytics-events}
{% apimethod post %}
/v1/device-messaging/banners/track
{% endapimethod %}

> Usa este endpoint para registrar eventos de impresión, clic y descarte para Banners.

Braze valida cada evento por separado. Cuando una solicitud contiene eventos válidos e inválidos, Braze procesa los eventos válidos y devuelve detalles sobre los eventos omitidos en el array `errors`. Si ningún evento es válido, Braze devuelve un código de estado `400`.

{% alert important %}
Esta página está en fase beta. Las características y la documentación de la API de mensajería de dispositivos están sujetas a cambios. Ponte en contacto con tu director de cuentas de Braze para solicitar acceso.
{% endalert %}

## Requisitos previos {#prerequisites}

Para usar este endpoint, necesitas lo siguiente:

- Un espacio de trabajo con Banners habilitado
- Una [clave de API REST or transferencia de estado representacional del lado del cliente]({{site.baseurl}}/api/device_messaging_api/authentication) con el permiso `banners.track`
- El [endpoint REST or transferencia de estado representacional]({{site.baseurl}}/api/basics#endpoints) de tu instancia de Braze
- Un `id` de Banner devuelto por el [endpoint Recuperar Banners para un usuario]({{site.baseurl}}/api/device_messaging_api/endpoints/banners/post_sync_banners)

Incluye la clave de API REST or transferencia de estado representacional del lado del cliente en el encabezado `Authorization` como un token bearer.

## Límite de velocidad {#rate-limit}

Los límites de velocidad se aplican por espacio de trabajo. Si superas el límite de velocidad, Braze devuelve un código de estado `429`. Cuando estén disponibles, usa los encabezados de respuesta `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset` y `X-RateLimit-Retry-After` para monitorear tu uso y determinar cuándo reintentar.

Para más información, consulta [Límites de velocidad de la API de mensajería de dispositivos]({{site.baseurl}}/api/device_messaging_api/rate_limits).

## Descartar Banners {#dismissing-banners}

Registrar un evento `dismiss` descarta el Banner para el usuario dado. Las sincronizaciones de Banner posteriores para ese usuario no incluirán los Banners descartados previamente, a menos que se haya configurado la reelegibilidad en la campaña.

{% alert note %}
Los eventos de descarte se procesan de forma asíncrona y no se reflejan de inmediato. En casos excepcionales, el procesamiento puede tardar unos minutos. Evita llamar al [endpoint Recuperar Banners para un usuario]({{site.baseurl}}/api/device_messaging_api/endpoints/banners/post_sync_banners) inmediatamente después de un descarte, ya que el Banner podría seguir siendo devuelto durante esta ventana.
{% endalert %}

Braze no concilia el estado del Banner en tu interfaz. Ocultar el Banner después de un descarte y mantenerlo oculto hasta que Braze procese el evento depende de tu aplicación.

## Cuerpo de la solicitud {#request-body}

```json
{
  "external_user_id": "{EXTERNAL_USER_ID}",
  "app_id": "{APP_API_IDENTIFIER}",
  "app_version": "1.0.0",
  "events": [
    {
      "id": "{BANNER_ID}",
      "event_type": "impression",
      "timestamp": "2026-04-09T12:00:00Z"
    }
  ]
}
```

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción | Ejemplo |
|---|---|---|---|---|
| `external_user_id` | Obligatorio | Cadena | El ID externo del usuario asociado con todos los eventos de la solicitud. El valor codificado en UTF-8 debe tener menos de 987 bytes. | `user_abc123` |
| `app_id` | Obligatorio | Cadena | El [identificador de API de la aplicación]({{site.baseurl}}/api/identifier_types#app-identifier). Debe identificar una aplicación en el espacio de trabajo autenticado. | `26a39c72-e647-4766-b62e-4521fa2dae59` |
| `app_version` | Obligatorio | Cadena | La versión de la aplicación anfitriona. No debe superar los 255 caracteres. | `1.0.0` |
| `events` | Obligatorio | Array de objetos | Uno o más eventos de análisis de Banner para registrar. | `[{"id":"bnr_01HZ3K2QFGH9XVNJ4W8PCRMT5E","event_type":"impression","timestamp":"2026-04-09T12:00:00Z"}]` |
| `events[].id` | Obligatorio | Cadena | El `id` de Banner devuelto por el endpoint Recuperar Banners para un usuario. Usa el ID de Banner, no el `placement_id`, para que Braze atribuya el evento a la Campaign y la variante correctas. | `bnr_01HZ3K2QFGH9XVNJ4W8PCRMT5E` |
| `events[].event_type` | Obligatorio | Cadena | El tipo de evento. Los valores posibles son `impression`, `click` y `dismiss`. | `impression` |
| `events[].timestamp` | Obligatorio | Cadena | La fecha y hora en que ocurrió el evento, con formato de cadena [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). | `2026-04-09T12:00:00Z` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Parámetros de la solicitud" }

## Ejemplo de solicitud {#example-request}

Reemplaza *`YOUR_REST_API_URL`* con el [endpoint REST or transferencia de estado representacional]({{site.baseurl}}/api/basics#endpoints) de tu instancia de Braze.

```bash
curl --location --request POST '{YOUR_REST_API_URL}/v1/device-messaging/banners/track' \
--header 'Authorization: Bearer {YOUR_CLIENT_SIDE_REST_API_KEY}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "external_user_id": "user_abc123",
  "app_id": "26a39c72-e647-4766-b62e-4521fa2dae59",
  "app_version": "1.0.0",
  "events": [
    {
      "id": "bnr_01HZ3K2QFGH9XVNJ4W8PCRMT5E",
      "event_type": "impression",
      "timestamp": "2026-04-09T12:00:00Z"
    },
    {
      "id": "bnr_01HZ3K2QFGH9XVNJ4W8PCRMT5E",
      "event_type": "click",
      "timestamp": "2026-04-09T12:00:05Z"
    }
  ]
}'
```

## Parámetros de respuesta {#response-parameters}

| Parámetro | Tipo de datos | Descripción |
|---|---|---|
| `events_processed` | Entero | El número de eventos que Braze validó y puso en cola. |
| `message` | Cadena | El estado del lote de eventos aceptado. |
| `errors` | Array de objetos | Detalles sobre los eventos que Braze omitió. Este array está ausente cuando Braze procesa todos los eventos. |
| `errors[].type` | Cadena | El error de validación del evento omitido. |
| `errors[].index` | Entero | El índice basado en cero del evento omitido en el array `events` de la solicitud. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Parámetros de respuesta" }

## Ejemplos de respuesta {#example-responses}

### Todos los eventos procesados {#all-events-processed}

Cuando Braze acepta todos los eventos, devuelve un código de estado `202`.

```json
{
  "events_processed": 2,
  "message": "success"
}
```

### Algunos eventos omitidos {#some-events-skipped}

Braze también devuelve un código de estado `202` cuando acepta al menos un evento válido. La respuesta identifica los eventos omitidos.

```json
{
  "events_processed": 2,
  "message": "success",
  "errors": [
    {
      "type": "Invalid event_type. Valid types are: impression, click, dismiss.",
      "index": 2
    }
  ]
}
```

### Sin eventos válidos {#no-valid-events}

Si Braze no puede procesar ningún evento, devuelve un código de estado `400`.

```json
{
  "message": "No valid events provided.",
  "errors": [
    {
      "type": "Invalid event_type. Valid types are: impression, click, dismiss.",
      "index": 0
    },
    {
      "type": "'timestamp' is required",
      "index": 1
    }
  ]
}
```

## Códigos de estado {#status-codes}

| Código de estado | Descripción |
|---|---|
| `202` | Braze aceptó al menos un evento. La respuesta enumera los eventos omitidos. |
| `400` | La solicitud tiene un formato incorrecto, los campos obligatorios no son válidos o no hay eventos válidos. |
| `401` | La clave de API REST or transferencia de estado representacional del lado del cliente falta o no es válida. |
| `403` | La clave de API REST or transferencia de estado representacional del lado del cliente no tiene el permiso `banners.track`. |
| `404` | La característica de Banners no está habilitada para el espacio de trabajo. |
| `429` | El espacio de trabajo superó su límite de velocidad. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Códigos de estado" }

Para más información, consulta [Manejo de errores y reintentos de la API de mensajería de dispositivos]({{site.baseurl}}/api/device_messaging_api/error_handling).

{% endapi %}