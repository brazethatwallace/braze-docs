---
nav_title: Abril
page_order: 9
noindex: true
page_type: update
description: "Este artículo contiene notas de la versión de abril de 2019."
---

# Abril de 2019 {#april-2019}

## Nuevos eventos y campos de Currents {#new-currents-events-fields}

Además de algunas correcciones en la sección, se ha añadido un nuevo [evento de suscripción]({{ site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/#subscription-events) a la página de eventos de interacción con mensajes.

Ahora puedes exportar los datos de cambio de estado del grupo de suscripción de Braze a [Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/#integration-details) y [mParticle]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle_for_currents/), así como esos datos y los eventos de atribución de instalación en [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/).

Además, se ha añadido la propiedad `canvas_step_id` a los [eventos de conversión]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/#conversion-events) disponibles.

{% alert important %}
Para aprovechar estas actualizaciones, tendrás que editar la configuración de tu conector de Currents y habilitar los eventos que quieras utilizar. Ponte en contacto con tu director de cuentas si tienes alguna pregunta.
{% endalert %}

## Archivo de grupos de suscripción {#subscription-groups-archiving}

¡Ahora puedes [archivar grupos de suscripción]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#archiving-groups)! Los grupos de suscripción archivados no se pueden editar y ya no aparecerán en los filtros de Segment. Si intentas archivar un grupo que se está utilizando como filtro de Segment en cualquier correo electrónico, Campaign o Canvas, recibirás un mensaje de error que te impedirá archivar el grupo hasta que elimines todos sus usos.