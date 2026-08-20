---
nav_title: Manejo de errores y reintentos
article_title: Manejo de errores y reintentos de la API de mensajería
page_order: 2
page_type: reference
description: "Aprende a manejar las respuestas, errores y reintentos de la API de mensajería."
hidden: true
---

# Manejo de errores y reintentos de la API de mensajería {#messaging-api-error-handling-and-retries}

{% alert important %}
Esta página está en beta. Las características y la documentación de la API de mensajería están sujetas a cambios.
{% endalert %}

Los cuerpos de respuesta y la semántica de éxito de la API de mensajería varían según el endpoint. Usa el esquema de respuesta y la tabla de códigos de estado de cada endpoint como el contrato de referencia.

## Respuestas de éxito {#success-responses}

Los endpoints de Banner usan diferentes respuestas de éxito:

- `POST /v1/device-messaging/banners/sync` devuelve un código de estado `200` con un objeto `banners`.
- `POST /v1/device-messaging/banners/track` devuelve un código de estado `202` con `events_processed` y `message`. Si Braze omite eventos individuales, la respuesta también incluye un array `errors`.

Una respuesta `202` del endpoint de seguimiento significa que Braze aceptó al menos un evento válido. Revisa el array `errors` para identificar los eventos omitidos.

## Respuestas de error {#error-responses}

Los campos de respuesta de error también varían:

- Los errores de recuperación de Banner usan un campo `error`.
- Los errores de seguimiento de Banner usan un campo `message` y pueden incluir un array `errors` indexado.

No analices el texto de los mensajes de error para determinar el comportamiento de la aplicación. Usa el código de estado HTTP y los campos específicos del endpoint en su lugar.

## Guía de reintentos {#retry-guidance}

Usa la siguiente guía para decidir si debes reintentar:

| Código de estado | Guía de reintento |
|---|---|
| `400` | Corrige la solicitud antes de reintentar. Para el seguimiento de Banner, corrige los eventos omitidos antes de reintentarlos. |
| `401` o `403` | Verifica la clave de API REST del lado del cliente y sus permisos antes de reintentar. |
| `404` | Confirma que la API de mensajería está habilitada para el espacio de trabajo y que la URL del endpoint es correcta. |
| `429` | Reduce la tasa de solicitudes y reintenta con retirada exponencial. Usa los encabezados de respuesta de límite de tasa cuando estén disponibles. |
| `5XX` | Reintenta con retirada exponencial y un número máximo de intentos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Guía de reintentos de la API de mensajería" }

Para conocer el cuerpo de respuesta exacto y los códigos de estado admitidos, consulta el endpoint correspondiente:

- [Recuperar Banners para un usuario]({{site.baseurl}}/api/messaging_api/endpoints/banners/post_sync_banners)
- [Registrar eventos de análisis de Banner]({{site.baseurl}}/api/messaging_api/endpoints/banners/post_track_banner_events)