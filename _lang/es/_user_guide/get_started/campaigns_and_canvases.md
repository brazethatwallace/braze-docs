---
nav_title: Campañas y Canvas
article_title: "Cómo empezar: Campañas y Canvas"
page_order: 3
page_type: reference
description: "Este artículo ofrece un resumen de las distintas formas en que puedes enviar mensajes con Braze."

---

# Cómo empezar: Campañas y Canvas

En Braze, puedes enviar mensajes a través de una [campaña](#campaigns) o de un [Canvas](#canvas).

- Para enviar un único mensaje dirigido a un grupo de usuarios, elige una campaña. Una campaña es un paso de mensaje único para conectar con tus usuarios en varios canales de mensajería.
- Para enviar una serie de mensajes continuos en un recorrido global del cliente, elige Canvas, nuestra herramienta de orquestación de recorridos. Mientras que las campañas son buenas para enviar mensajes sencillos y específicos, Canvas es donde llevas tus relaciones con los clientes al siguiente nivel.

## Campañas

Aunque las campañas pueden construirse de forma única dependiendo del canal, hay cuatro tipos principales de campañas en Braze que debes conocer:

| Tipo de campaña        | Descripción                                                                                                                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Regular              | Es el tipo de campaña más común. Puedes dirigirte a uno o varios canales en función de tus objetivos de mensajería, y diseñar, personalizar y probar tu contenido directamente en Braze con nuestros editores visuales. Aprende a [crear una campaña]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign/). |
| Pruebas A/B          | En el caso de las campañas dirigidas a un único canal, puedes enviar más de una versión de la misma campaña y ver cuál sale ganadora. Puedes probar el texto, la personalización y más para un máximo de ocho versiones diferentes con una [campaña multivariante]({{site.baseurl}}/user_guide/messaging/ab_testing/). |
| API                  | Las [campañas de API]({{site.baseurl}}/api/api_campaigns/) te permiten enviar mensajes puntuales lo más rápidamente posible. A diferencia de otros tipos de campaña, no especificas el mensaje, los destinatarios ni la planificación en el dashboard de Braze. En su lugar, pasas estos identificadores a tus llamadas a la API. Suelen utilizarse para mensajería transaccional en tiempo real o noticias de última hora.  |
| Correos electrónicos transaccionales | Los [correos electrónicos transaccionales]({{site.baseurl}}/user_guide/channels/email/) de Braze están diseñados para enviar mensajes de correo electrónico automatizados y no promocionales con el fin de facilitar una transacción acordada entre tú y tus clientes. Envían notificaciones críticas para el negocio a un único usuario donde la velocidad es lo más importante. *Disponible para determinados paquetes.* |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Las campañas regulares y de pruebas A/B pueden programarse (como informar a una lista de usuarios sobre un próximo evento) o automatizarse para que se envíen en respuesta a una acción del usuario (como enviar un correo electrónico cuando alguien se suscribe a tu boletín). Más información sobre [la programación de campañas]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/).
{% endalert %}

Independientemente del tipo de campaña que crees, tus campañas pueden escuchar las necesidades de tus usuarios y ofrecer una respuesta pensada y personalizada. Una vez que hayas enviado tu campaña, utiliza nuestras [herramientas de análisis integradas]({{site.baseurl}}/user_guide/analytics/reports/) para ver cómo ha funcionado y cuántos usuarios convirtieron en función de tus [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/).

Consulta estos recursos adicionales para saber más sobre las campañas en Braze:

- Braze Learning: [Configuración de la campaña](https://learning.braze.com/campaign-setup-delivery-targeting-conversions)
- [Crear una campaña]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign/)
- [Ideas y estrategias]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/)

## Canvas

En lugar de enviar mensajes esporádicos a lo largo de varias campañas, Canvas crea una conversación fluida y continua con los usuarios. Esto se debe a que el recorrido de un usuario a través de un Canvas puede dividirse en diferentes caminos en función de sus acciones (o inacción) con tu marca, lo que te permite hacer avanzar automáticamente a los usuarios a través de un flujo específico en tiempo real.

![]({% image_buster /assets/img/getting_started/canvas_flow.png %})

De este modo, Canvas es ideal para lanzar una red y captar a los usuarios que se desvían del camino hacia la conversión, colocándolos en las iniciativas de difusión más eficaces.

Cuando creas un Canvas, sigues muchos de los mismos pasos que para configurar una campaña: especificar una audiencia general, condiciones de entrada y ajustes de envío. Tu Canvas comienza cuando alguien coincide con tu condición de activación. A continuación, se mueven a través de un camino en el Canvas hasta que cumplan tus condiciones de salida.

Tu Canvas puede tener cualquier combinación de [mensajes]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/), [retrasos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step/), [experimentos]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/) y más. Puedes enviar en cualquier canal de mensajería compatible, e incluso [integrarte con plataformas sociales y publicitarias]({{site.baseurl}}/partners/canvas_audience_sync/overview/) como Facebook, Google o TikTok.

Echa un vistazo a estos recursos adicionales para obtener más información sobre Canvas:

- Braze Learning: [Orquestación de recorridos con Canvas Flow](https://learning.braze.com/path/journey-orchestration-with-canvas-flow)
- [Crear un Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/)
- [Esquemas de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/canvas_outlines/)

## Canales de mensajería

Los canales de mensajería son los distintos canales de comunicación a través de los cuales puedes interactuar con tus clientes y entregar mensajes específicos. 

![]({% image_buster /assets/img/getting_started/channels.png %})

En la tabla siguiente se describen los canales que admitimos.

| Canal                                                                                              | Descripción                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Correo electrónico]({{site.baseurl}}/user_guide/channels/email/)                        | Envía correos electrónicos personalizados al buzón de entrada de tus usuarios.                                                                                                       |
| [Push móvil]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/)                   | Entrega mensajes directamente a los dispositivos móviles de los usuarios como notificaciones.                                                                                   |
| [Notificación push web]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/web/)                         | Entrega notificaciones a los navegadores web de los usuarios, incluso cuando no están activos en tu sitio web.                                                         |
| [Mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/)    | Muestra mensajes dentro de tu aplicación móvil mientras los usuarios la están utilizando activamente.                                                                             |
| [SMS, MMS y RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/)*                   | Envía mensajes de texto a los teléfonos móviles de los usuarios.                                                                                                            |
| [WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/)*              | Envía mensajes a través de la popular plataforma de mensajería WhatsApp para llegar a tus usuarios e interactuar con ellos.                                                   |
| [Banners]({{site.baseurl}}/user_guide/channels/banners/)*       | Incrusta mensajes directamente en tu aplicación o sitio web. |
| [Tarjetas de contenido]({{site.baseurl}}/user_guide/channels/content_cards/)*       | Proporciona un buzón de entrada dentro de tu aplicación o sitio web donde los usuarios pueden recibir mensajes e interactuar con ellos, o muestra los mensajes en un carrusel, como un banner y más. |
| [TV conectada]({{site.baseurl}}/developer_guide/platforms/tv_and_ott/)                           | Interactúa con los usuarios en plataformas de televisión conectadas.                                                                                                   |
| [Webhooks]({{site.baseurl}}/user_guide/channels/webhooks/) | Habilita la comunicación en tiempo real y la integración con sistemas externos mediante devoluciones de llamada HTTP personalizadas.                                                    |
| [LINE]({{site.baseurl}}/user_guide/channels/line/) | Interactúa con los usuarios en LINE, la aplicación de mensajería más popular de Japón.                                                    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<sup>Disponible como característica adicional.</sup>

{% alert tip %}
Para mensajes cortos y urgentes que pueden comunicarse a través de la mayoría de los canales (correo electrónico, SMS, push), aprovecha el filtro de [canal inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel/) para enviar automáticamente el mensaje a través del mejor canal para cada usuario.
{% endalert %}