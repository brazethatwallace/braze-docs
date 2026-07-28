---
nav_title: Entrega desencadenada por API
article_title: Entrega desencadenada por API
page_order: 2
page_type: reference
description: "Este artículo de referencia describe cómo planificar y configurar una campaña desencadenada por API."
tool: Campaigns
platform: API

---

# Entrega desencadenada por API {#api-triggered-delivery}

> Las campañas desencadenadas por API o campañas desencadenadas por servidor son ideales para casos de uso transaccionales más avanzados. Las campañas desencadenadas por API de Braze permiten a los especialistas en marketing gestionar el texto de la campaña, las pruebas multivariante y las reglas de reelegibilidad dentro del panel de Braze, mientras desencadenan la entrega de ese contenido desde sus propios servidores y sistemas. La solicitud de API para desencadenar el mensaje también puede incluir datos adicionales que se incorporan a la plantilla del mensaje en tiempo real.

## Configurar una campaña desencadenada por API {#setting-up-an-api-triggered-campaign}

Configurar una campaña desencadenada por API requiere algunos pasos. Primero, crea una nueva campaña multicanal o de un solo canal (con pruebas multivariante).

{% alert note %}
Una campaña desencadenada por API es diferente de una [campaña de API]({{site.baseurl}}/developer_guide/rest_api/api_campaigns#api-campaigns).
{% endalert %}

A continuación, configura tu texto y notificaciones de la misma manera que lo harías normalmente para notificaciones planificadas y selecciona **API-Triggered Delivery**. Para más información sobre cómo desencadenar estas campañas desde tu servidor, consulta este artículo sobre [envío de campañas desencadenadas por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns).

![Configura tu texto y notificaciones de la misma manera que lo harías normalmente para notificaciones planificadas y selecciona API-Triggered Delivery. Para más información sobre cómo desencadenar estas campañas desde tu servidor, consulta el artículo sobre envío de campañas desencadenadas por API.]({% image_buster /assets/img_archive/api_triggered_campaign_delivery.png %})

## Reducir el retraso entre el desencadenador de API y el envío {#reducing-delay-between-your-api-trigger-and-send}

Si los mensajes tardan más de lo esperado en enviarse después de llamar al endpoint de desencadenamiento, comprueba si el perfil de usuario está listo en el momento del desencadenamiento.

De forma predeterminada, `send_to_existing_only` es `true` en [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns). Braze solo envía a usuarios existentes y no crea perfiles nuevos en esa llamada. Para crear o actualizar un usuario y enviar en la misma solicitud, establece `send_to_existing_only` en `false` e incluye un objeto `attributes` en cada destinatario.

Para campañas de correo electrónico, incluye también `email` (y cualquier otro campo de entrega requerido) dentro de `attributes`. Si el perfil no tiene una dirección de correo electrónico cuando desencadenas el envío, Braze reintenta durante aproximadamente 2 horas mientras espera a que lleguen los datos del perfil. Incluir `email` en la misma llamada evita ese retraso.

Para ver todos los parámetros de solicitud, ejemplos y el comportamiento de reintentos, consulta [Enviar campañas desencadenadas por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns#recipient-limits-and-profile-creation) y el [objeto de destinatarios]({{site.baseurl}}/api/objects_filters/recipient_object).

{% alert note %}
Esta guía aplica a campañas desencadenadas por API (`/campaigns/trigger/send`). El [endpoint de correo transaccional]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message) utiliza una estructura de solicitud diferente (`recipient`, singular) y no admite `send_to_existing_only`. Para crear un usuario de forma integrada con envíos transaccionales, pasa `attributes` en el objeto `recipient`.
{% endalert %}

## Uso del contenido con plantilla incluido en una solicitud de API {#using-the-templated-content-included-with-an-api-request}

Además de desencadenar el mensaje, también puedes incluir contenido con la solicitud de API para incorporarlo como plantilla en el mensaje dentro del objeto `trigger_properties`. Este contenido puede referenciarse en el cuerpo del mensaje. Usa exactamente dos llaves por cada etiqueta de Liquid en `trigger_properties` y en el texto del mensaje. Un ejemplo es: {% raw %}`{{api_trigger_properties.${your_property}}}`.{% endraw %} Una `{` o `}` adicional es una causa común de [fallos de personalización desencadenada por API]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/faq#why-is-my-api-triggered-liquid-failing-in-braze).

Consulta el siguiente ejemplo de notificación social para contexto adicional.

![La propiedad de desencadenamiento mencionada anteriormente incluida en el mensaje para autocompletar el nombre del usuario seguido del texto: "liked your photo! Click here to see what they've been up to."]({% image_buster /assets/img_archive/api_triggered_photo_social_example_1.png %}){: style="max-width:70%;"}

## Reelegibilidad con campañas desencadenadas por API {#re-eligibility-with-api-triggered-campaigns}

El número de veces que un usuario recibe una campaña desencadenada por API puede limitarse mediante la configuración de reelegibilidad. Esto significa que el usuario recibirá la campaña solo una vez o una vez en una ventana determinada, independientemente de cuántas veces se active el desencadenador de API.

Por ejemplo, supongamos que estás usando una campaña desencadenada por API para enviar al usuario una campaña sobre un artículo que vio recientemente. En este caso, puedes limitar la campaña para enviar un máximo de un mensaje al día, independientemente de cuántos artículos haya visto, mientras se activa el desencadenador de API para cada artículo. Por otro lado, si tu campaña desencadenada por API es transaccional, querrás asegurarte de que el usuario reciba la campaña cada vez que realice la transacción, estableciendo el retraso en cero minutos.

![Captura de pantalla relacionada con la reelegibilidad en campañas desencadenadas por API.]({% image_buster /assets/img_archive/api_triggered_reeligible.png %})