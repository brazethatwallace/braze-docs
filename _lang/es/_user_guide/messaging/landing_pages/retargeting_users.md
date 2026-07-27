---
nav_title: Reorientar usuarios
article_title: Reorientar usuarios
description: "Aprende a reorientar a los usuarios que han enviado un formulario a través de una página de inicio."
page_order: 3
---

# Reorientar usuarios a través de una página de inicio {#retarget-users-through-a-landing-page}

> Aprende a reorientar a los usuarios que han enviado un formulario a través de una página de inicio creando un segmento dedicado o desencadenando un mensaje cuando se envía el formulario.

## Requisitos previos {#prerequisites}

Antes de comenzar, necesitarás crear una [página de destino]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages).

## Reorientar usuarios {#retargeting-users}

Braze rastrea automáticamente cuándo un usuario envía un formulario de página de destino. Puedes ver el número total de envíos de un formulario en [análisis de páginas de destino]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#view-analytics). Sin embargo, para reorientar usuarios específicos, necesitarás reorientarlos a través del formulario de tu página de destino usando uno de los siguientes métodos:

- **Usando un Segment:** Puedes crear un nuevo Segment para identificar automáticamente a los usuarios que han enviado o no un formulario de página de destino.
- **Usando un desencadenador de mensaje:** Puedes configurar un desencadenador de mensaje para enviar mensajes automáticamente a los usuarios o ingresarlos en un Canvas después de que envíen el formulario.

{% tabs local %}
{% tab Usando un Segment %}
Cuando [crees un Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment), en el grupo "Retargeting", selecciona **Submitted form on Landing Page**.

![Creación de un Segment con el grupo de filtros seleccionado como "Submitted Form on Landing Page".]({% image_buster /assets/img/landing_pages/segmentation_selected.png %})

Desde aquí, puedes segmentar usuarios en función de si han enviado o no un formulario de página de destino para tu página de destino.
{% endtab %}

{% tab Usando un desencadenador de mensaje %}
Cuando elijas tu opción de entrega para tu [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns) o [Canvas]({{site.baseurl}}/user_guide/messaging/canvas), selecciona **Action Based Delivery** y luego **Submitted Landing Page form**.

Todos los usuarios que envíen un formulario a través de este formulario de página de destino recibirán un mensaje a través del canal de mensajería elegido o serán ingresados en el Canvas elegido.

![Acción desencadenante de página de destino en mensajería.]({% image_buster /assets/img/landing_pages/trigger.png %})

{% alert note %}
La opción de entrega basada en acciones para páginas de destino no está disponible para mensajes dentro de la aplicación. Para segmentar a los usuarios que han enviado un formulario en una página de destino con un mensaje dentro de la aplicación, selecciona el filtro **Submitted Form on Landing Page** en las **Targeting Options** de tu Campaign.
{% endalert %}

{% endtab %}
{% endtabs %}