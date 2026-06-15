---
nav_title: Reorientar usuarios
article_title: Reorientar usuarios
description: "Aprende a reorientar a los usuarios que han enviado un formulario a través de una página de inicio."
page_order: 3
---

# Reorientar usuarios a través de una página de inicio {#retarget-users-through-a-landing-page}

> Aprende a reorientar a los usuarios que han enviado un formulario a través de una página de inicio creando un segmento dedicado o desencadenando un mensaje cuando se envía el formulario.

## Requisitos previos {#prerequisites}

Antes de empezar, tendrás que crear una [página de inicio]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/).

## Reorientar usuarios {#retargeting-users}

Braze realiza un seguimiento automático cuando un usuario envía un formulario de página de inicio. Puedes ver el número total de envíos de un formulario en [análisis de páginas de inicio]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/#viewing-analytics). Sin embargo, para reorientar a usuarios específicos, tendrás que reorientar a los usuarios a través del formulario de tu página de inicio utilizando uno de los siguientes métodos:

- **Usando un segmento:** Puedes crear un nuevo segmento para identificar automáticamente a los usuarios que han enviado o no un formulario de página de inicio.
- **Usando un desencadenante de mensaje:** Puedes configurar un desencadenante de mensaje para enviar automáticamente un mensaje a los usuarios o introducirlos en un Canvas después de que envíen el formulario.

{% tabs local %}
{% tab Usando un segmento %}
Cuando [crees un segmento]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/), en el grupo "Reorientación", elige **Submitted form on Landing Page**.

![Creación de un segmento con el grupo de filtros seleccionado como "Submitted Form on Landing Page".]({% image_buster /assets/img/landing_pages/segmentation_selected.png %})

Desde aquí, puedes segmentar a los usuarios en función de si han enviado o no un formulario de página de inicio para tu página de inicio.
{% endtab %}

{% tab Usando un desencadenante de mensaje %}
Cuando elijas tu opción de entrega para tu [campaign]({{site.baseurl}}/user_guide/messaging/campaigns/) o [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/), selecciona **Action Based Delivery** y luego **Submitted Landing Page form**.

Todos los usuarios que envíen un formulario a través de este formulario de página de inicio recibirán un mensaje a través del canal de mensajería elegido o serán introducidos en el Canvas elegido.

![Acción desencadenante de página de inicio en mensajería.]({% image_buster /assets/img/landing_pages/trigger.png %})

{% alert note %}
La opción de entrega basada en acciones para páginas de inicio no está disponible para mensajes dentro de la aplicación. Para dirigirte a los usuarios que han enviado un formulario en una página de inicio con un mensaje dentro de la aplicación, selecciona el filtro **Submitted Form on Landing Page** en las **Opciones de segmentación** de tu campaign.
{% endalert %}

{% endtab %}
{% endtabs %}