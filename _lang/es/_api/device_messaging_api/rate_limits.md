---
nav_title: Límites de velocidad
article_title: Límites de velocidad de la API de mensajería del dispositivo
page_order: 3
page_type: reference
description: "Descubre cómo funcionan los límites de velocidad y los encabezados de respuesta de la API de mensajería del dispositivo."
hidden: true
---

# Límites de velocidad de la API de mensajería del dispositivo {#device-messaging-api-rate-limits}

Braze aplica límites de velocidad de la API de mensajería del dispositivo por espacio de trabajo. Si un espacio de trabajo supera un límite, Braze devuelve un código de estado `429 Too Many Requests`.

Los límites de la API de mensajería del dispositivo son independientes de los límites predeterminados documentados para otros endpoints de la REST API de Braze. No asumas que un límite, ventana de tiempo, tamaño de carga útil o programación de reinicio documentados para otro endpoint se aplican a la API de mensajería del dispositivo.

{% alert important %}
Esta página está en fase beta. Las características y la documentación de la API de mensajería del dispositivo están sujetas a cambios. Ponte en contacto con tu director de cuentas de Braze para solicitar acceso.
{% endalert %}

## Encabezados de límite de velocidad {#rate-limit-headers}

Cuando la información sobre el límite de velocidad está disponible, una respuesta incluye los siguientes encabezados:

| Encabezado | Descripción |
|---|---|
| `X-RateLimit-Limit` | El número máximo de solicitudes permitidas en el intervalo actual. |
| `X-RateLimit-Remaining` | El número de solicitudes restantes en la ventana de límite de velocidad actual. |
| `X-RateLimit-Reset` | La hora en formato epoch UTC en la que se restablece la ventana de límite de velocidad actual. |
| `X-RateLimit-Retry-After` | El número de segundos que debes esperar antes de reintentar una solicitud con límite de velocidad. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Encabezados de límite de velocidad de la API de mensajería del dispositivo" }

Usa estos encabezados para reducir o pausar solicitudes antes de alcanzar un límite. Es posible que los encabezados no estén presentes en todas las respuestas.

## Gestión de los límites de velocidad {#handling-rate-limits}

Cuando recibas una respuesta `429`:

1. Detén o reduce las solicitudes para el espacio de trabajo afectado.
2. Usa `X-RateLimit-Retry-After` cuando esté presente para determinar cuánto tiempo esperar. De lo contrario, usa `X-RateLimit-Reset` cuando esté disponible para determinar cuándo reanudar.
3. Reintenta con retirada exponencial y un número máximo de intentos.