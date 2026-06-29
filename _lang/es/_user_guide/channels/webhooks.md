---
nav_title: Webhooks
article_title: Webhooks
page_order: 9
page_type: landing
alias: /about_webhooks/
description: "Conecta tus sistemas con webhooks en Braze, desencadenados por eventos personalizados para enviar datos y mensajes programáticos a puntos de conexión externos."
channel:
  - webhooks
search_rank: 3
---

# Webhooks {#webhooks}

> Un webhook es un mensaje automatizado de un sistema a otro que se envía cuando se cumplen ciertos criterios. En Braze, estos criterios suelen ser el desencadenamiento de un evento personalizado. Los webhooks proporcionan acceso dinámico y flexible a datos y funcionalidad programática, y te permiten configurar recorridos del cliente que optimizan los procesos.

## Requisitos previos {#prerequisites}

La disponibilidad de los webhooks depende de tu paquete de Braze. Ponte en contacto con tu director de cuentas o administrador del éxito del cliente para empezar.

## Casos de uso {#use-cases}

Los webhooks son una excelente forma de conectar tus sistemas entre sí; después de todo, los webhooks son la forma en que las aplicaciones se comunican. Estos son algunos escenarios generales en los que los webhooks pueden ser particularmente útiles:

- Enviar datos hacia y desde Braze
- Enviar mensajes a tus clientes a través de canales no compatibles directamente con Braze
- Publicar en las API de Braze

Algunos casos de uso más específicos incluyen los siguientes:

- Crea un [flujo de trabajo de puntuación de leads]({{site.baseurl}}/user_guide/get_started/b2b_use_cases/lead_scoring) usando webhooks y Canvas para calificar y enrutar leads.
- Si un usuario cancela su suscripción al correo electrónico, podrías hacer que un webhook actualice tu base de datos de análisis o CRM con esa misma información, asegurando una visión integral del comportamiento de ese usuario.
- Envía [mensajes transaccionales]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign) a usuarios dentro de Facebook Messenger o Line.
- Envía correo directo a los clientes en respuesta a su actividad dentro de la aplicación y en la web usando webhooks para comunicarte con servicios de terceros como [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob).
- Si un jugador alcanza cierto nivel o acumula cierta cantidad de puntos, usa webhooks y tu configuración de API existente para enviar una mejora de personaje o monedas directamente a su cuenta. Si envías el webhook como parte de una campaña de mensajería multicanal, puedes enviar un push u otro mensaje para informar al jugador sobre la recompensa al mismo tiempo.
- Si eres una aerolínea, puedes usar webhooks y tu configuración de API existente para acreditar en la cuenta de un cliente un descuento después de que haya reservado cierto número de vuelos.
- Infinitas recetas "If This Then That" ([IFTTT](https://ifttt.com/about)); por ejemplo, si un cliente inicia sesión en la aplicación a través de correo electrónico, esa dirección puede configurarse automáticamente en Salesforce.

## Manejo de errores y límite de velocidad de webhooks {#webhook-error-handling-and-rate-limiting}

Braze reintenta la entrega de webhooks solo para ciertas respuestas HTTP (por ejemplo, `408`, `429` y `5XX`). La mayoría de las demás respuestas, incluyendo `401 Unauthorized` y otros errores `4XX`, no se reintentan. Los encabezados de respuesta como `Retry-After` y `X-Rate-Limit-*` pueden influir en el tiempo de espera **cuando una respuesta ya es elegible para reintento**; no hacen que Braze reintente errores que están fuera del conjunto reintentable.

Para la tabla completa de códigos de respuesta, límites de reintento y comportamiento de tiempo de espera, consulta [Códigos de respuesta y lógica de reintento]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#response-codes-and-retry-logic).

Si la mayoría de las solicitudes de webhook a un host específico están fallando, Braze difiere temporalmente todos los intentos de envío a ese host. El envío se reanuda después de un período de enfriamiento definido, permitiendo que tu sistema se recupere.

## Uso de webhooks con socios de Braze {#utilizing-webhooks}

Hay muchas formas de usar webhooks, y con nuestros socios tecnológicos (Alloys), puedes usar webhooks para mejorar tu comunicación directamente con tus clientes y usuarios.

Consulta:
* [Messenger]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/instant_chat/messenger)
* [Remerge]({{site.baseurl}}/partners/remerge)
* [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob)
* ¡Y muchos más de nuestros [socios tecnológicos]({{site.baseurl}}/partners/home)!

## Próximos pasos {#next-steps}

- [Crear un webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook)
- [Crear un webhook de Braze a Braze]({{site.baseurl}}/user_guide/channels/webhooks/use_case_create_a_braze_to_braze_webhook)