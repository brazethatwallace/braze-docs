---
nav_title: Campaigns y Canvas
article_title: "Cómo empezar: Campaigns y Canvas"
page_order: 3
page_type: reference
description: "Este artículo ofrece un resumen de las distintas formas en que puedes enviar mensajes con Braze."
---

# Cómo empezar: Campaigns y Canvas {#get-started-campaigns-and-canvases}

> Este artículo ofrece un resumen de las distintas formas en que puedes enviar mensajes con Braze. En Braze, puedes enviar mensajes a través de una [Campaign](#campaigns) o de un [Canvas](#canvas).

- Para enviar un único mensaje dirigido a un grupo de usuarios, elige una Campaign. Una Campaign es un paso de mensaje único para conectar con tus usuarios en varios canales de mensajería.
- Para enviar una serie de mensajes continuos en un recorrido global del cliente, elige Canvas, nuestra herramienta de orquestación de recorridos. Mientras que las Campaigns son buenas para enviar mensajes sencillos y específicos, Canvas es donde llevas tus relaciones con los clientes al siguiente nivel.

## Campaigns {#campaigns}

Si bien las Campaigns se pueden crear de forma única según el canal, hay cuatro tipos principales de Campaigns en Braze que debes conocer:

| Tipo de Campaign     | Descripción                                                                                                                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Regular              | Este es el tipo más común de Campaign. Puedes dirigirte a uno o más canales según tus objetivos de mensajería, y diseñar, personalizar y probar tu contenido directamente en Braze con nuestros editores visuales. Aprende cómo [crear una Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign). |
| Pruebas A/B          | Para Campaigns dirigidas a un solo canal, puedes enviar más de una versión de la misma Campaign y ver cuál obtiene mejores resultados. Puedes probar el texto, la personalización y más para hasta ocho versiones diferentes con una [Campaign multivariante]({{site.baseurl}}/user_guide/messaging/ab_testing). |
| API                  | Las [Campaigns de API]({{site.baseurl}}/api/api_campaigns) te permiten enviar mensajes oportunos lo más rápido posible. A diferencia de otros tipos de Campaigns, no especificas el mensaje, los destinatarios ni la programación en el panel de Braze. En su lugar, pasas estos identificadores en tus llamadas a la API. Normalmente se usan para mensajería transaccional en tiempo real o noticias de última hora.  |
| Correos transaccionales | Los [correos transaccionales]({{site.baseurl}}/user_guide/channels/email) de Braze están diseñados específicamente para enviar mensajes de correo electrónico automatizados y no promocionales con el fin de facilitar una transacción acordada entre tú y tus clientes. Envían notificaciones críticas para el negocio a un solo usuario donde la velocidad es de suma importancia. *Disponible para paquetes seleccionados.* |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campaigns" }

{% alert note %}
Las Campaigns regulares y de pruebas A/B se pueden programar (como informar a una lista de usuarios sobre un evento próximo) o automatizar para que se envíen en respuesta a una acción del usuario (como enviar un correo electrónico cuando alguien se suscribe a tu boletín). Más información sobre [programar Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).
{% endalert %}

Independientemente del tipo de Campaign que crees, tus Campaigns pueden escuchar las necesidades de tus usuarios y entregar una respuesta reflexiva y personalizada. Después de enviar tu Campaign, usa nuestras [herramientas de análisis integradas]({{site.baseurl}}/user_guide/analytics/reports) para ver su rendimiento y cuántos usuarios convirtieron según tus [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events).

Consulta estos recursos adicionales para aprender más sobre Campaigns en Braze:

- Braze Learning: [Configuración de Campaigns](https://learning.braze.com/campaign-setup-delivery-targeting-conversions)
- [Crear una Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign)
- [Ideas y estrategias]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies)

## Canvas {#canvas}

En lugar de enviar mensajes esporádicos a través de múltiples Campaigns, Canvas crea una conversación continua y fluida con los usuarios. Esto se debe a que el recorrido de un usuario a través de un Canvas puede dividirse en diferentes caminos dependiendo de sus acciones (o inacción) con tu marca, lo que te permite avanzar automáticamente a los usuarios a través de un flujo específico en tiempo real.

![Diagrama de flujo del proceso descrito.]({% image_buster /assets/img/getting_started/canvas_flow.png %})

De esta manera, Canvas es ideal para lanzar una red que capture a los usuarios que se desvían del camino hacia la conversión y colocarlos en las iniciativas de contacto más efectivas.

Cuando creas un Canvas, sigues muchos de los mismos pasos que al configurar una Campaign: especificar una audiencia general, condiciones de entrada y configuración de envío. Tu Canvas comienza cuando alguien coincide con tu condición de desencadenamiento. Luego avanza a través de un camino en el Canvas hasta que cumple tus condiciones de salida.

Tu Canvas puede tener cualquier combinación de [mensajes]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step), [retrasos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step), [experimentos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) y más. Puedes enviar en cualquier canal de mensajería compatible, e incluso [integrarte con plataformas sociales y de anuncios]({{site.baseurl}}/partners/canvas_audience_sync/overview) como Facebook, Google o TikTok.

Consulta estos recursos adicionales para aprender más sobre Canvas:

- Braze Learning: [Orquestación de recorridos con Canvas Flow](https://learning.braze.com/path/journey-orchestration-with-canvas-flow)
- [Crear un Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)
- [Esquemas de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/canvas_outlines)

## Canales de mensajería {#messaging-channels}

Los canales de mensajería son los distintos canales de comunicación a través de los cuales puedes interactuar con tus clientes y entregar mensajes segmentados.

![Diagrama de los canales de mensajería de Braze disponibles a través del SDK.]({% image_buster /assets/img/getting_started/channels.png %})

La siguiente tabla describe nuestros canales compatibles.

| Canal                                                                                              | Descripción                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Correo electrónico]({{site.baseurl}}/user_guide/channels/email)                        | Envía correos electrónicos personalizados al buzón de entrada de tus usuarios.                                                                                                       |
| [Push móvil]({{site.baseurl}}/user_guide/channels/push/create_a_push_message)                   | Entrega mensajes directamente a los dispositivos móviles de los usuarios como notificaciones.                                                                                   |
| [Push web]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/web)                         | Entrega notificaciones a los navegadores web de los usuarios, incluso cuando no están activamente en tu sitio web.                                                         |
| [In-App Messages]({{site.baseurl}}/user_guide/channels/in_app_messages)    | Muestra mensajes dentro de tu aplicación móvil mientras los usuarios la están usando activamente.                                                                             |
| [servicio de mensajes cortos, MMS y RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs)*                   | Envía mensajes de texto a los teléfonos móviles de los usuarios.                                                                                                            |
| [WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)*              | Envía mensajes a través de la popular plataforma de mensajería WhatsApp para llegar a tus usuarios e interactuar con ellos.                                                   |
| [Banner]({{site.baseurl}}/user_guide/channels/banners)*       | Inserta mensajes directamente en tu aplicación o sitio web. |
| [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)*       | Ofrece un buzón de entrada dentro de tu aplicación o sitio web donde los usuarios pueden recibir e interactuar con mensajes, o muestra mensajes en un carrusel, como banner, y más. |
| [TV conectada]({{site.baseurl}}/developer_guide/platforms/tv_and_ott)                           | Interactúa con los usuarios en plataformas de televisión conectada.                                                                                                   |
| [Webhooks]({{site.baseurl}}/user_guide/channels/webhooks) | Habilita la comunicación en tiempo real y la integración con sistemas externos a través de devoluciones de llamada HTTP personalizadas.                                                    |
| [LINE]({{site.baseurl}}/user_guide/channels/line) | Interactúa con los usuarios en LINE, la aplicación de mensajería más popular de Japón.                                                    |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canales de mensajería" }

<sup>Disponible como característica adicional.</sup>

{% alert tip %}
Para mensajes cortos y urgentes que se pueden comunicar a través de la mayoría de los canales (correo electrónico, servicio de mensajes cortos, push), aprovecha el filtro de [canal inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel) para enviar automáticamente el mensaje a través del mejor canal para cada usuario.
{% endalert %}