---
nav_title: Reorientar usuarios
article_title: Reorientar usuarios
description: "Aprende a reorientar a los usuarios que han enviado un formulario a través de una página de inicio."
page_order: 3
---

# Reorientar usuarios a través de una página de inicio {#retarget-users-through-a-landing-page}

> Aprende a reorientar a los usuarios que han enviado un formulario a través de una página de inicio creando un segmento dedicado o desencadenando un mensaje cuando se envía el formulario.

## Requisitos previos {#prerequisites}

Antes de comenzar, crea una [página de destino]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages).

## Reorientar usuarios {#retargeting-users}

Braze rastrea automáticamente cuándo un usuario envía un formulario de página de destino. Puedes ver el número total de envíos de un formulario en [análisis de páginas de destino]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#view-analytics). Para reorientar usuarios específicos, hazlo a través del formulario de tu página de destino utilizando uno de los siguientes métodos:

{% tabs local %}
{% tab Usando un Segment %}

Crea un nuevo Segment para identificar automáticamente a los usuarios que han enviado o no un formulario de página de destino. Cuando [crees un Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment), en el grupo "Retargeting", selecciona **Submitted Form on Landing Page**.

![Creación de un Segment con el grupo de filtros seleccionado como "Submitted Form on Landing Page".]({% image_buster /assets/img/landing_pages/segmentation_selected.png %})

Desde aquí, puedes segmentar a los usuarios en función de si han enviado o no un formulario de página de destino para tu página de destino.
{% endtab %}

{% tab Usando un desencadenador de mensaje %}

Configura un desencadenador de mensaje para enviar automáticamente un mensaje a los usuarios o ingresarlos en un Canvas después de que envíen el formulario. Cuando elijas tu opción de entrega para tu [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns) o [Canvas]({{site.baseurl}}/user_guide/messaging/canvas), selecciona **Action Based Delivery** y luego **Submitted a Landing Page form**.

Todos los usuarios que envíen un formulario a través de este formulario de página de destino recibirán un mensaje a través del canal de mensajería elegido o ingresarán en el Canvas elegido.

![Acción desencadenante de página de destino en mensajería.]({% image_buster /assets/img/landing_pages/trigger.png %})

{% alert note %}
La opción de entrega basada en acciones para páginas de destino no está disponible para mensajes dentro de la aplicación. Para dirigirte a usuarios que han enviado un formulario en una página de destino con un mensaje dentro de la aplicación, selecciona el filtro **Submitted Form on Landing Page** en las **Targeting Options** de tu Campaign.
{% endalert %}

{% endtab %}
{% endtabs %}

### Formulario de varios pasos {#multi-step-form}

Para un [formulario de varios pasos]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/multi_step_forms), ambos métodos de reorientación dependen del evento **Submitted a Landing Page form**, que solo se registra después de que un usuario completa todos los pasos. Un usuario que envía algunos pasos pero no todos se guarda en su perfil, pero no se incluye en ninguno de los dos métodos hasta que complete el formulario completo. Para más información, consulta [Rastrear datos de formularios parcialmente completados]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/multi_step_forms#track-data-from-partially-completed-forms).