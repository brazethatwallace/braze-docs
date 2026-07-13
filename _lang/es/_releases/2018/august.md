---
nav_title: Agosto
page_order: 6
noindex: true
page_type: update
description: "Este artículo contiene notas de la versión de agosto de 2018."
---
# Agosto de 2018 {#august-2018}

## Grupos de notificaciones de iOS 12 {#ios-12-notification-groups}

La reciente versión de iOS 12 admite la agrupación de notificaciones (similar a los canales de notificación de Android) para aplicaciones. [Braze te permite utilizar esta característica de agrupación en iOS utilizando nuestro creador de mensajes.]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#notification-groups)

## Desencadenamiento de historias push {#push-story-triggering}

Ahora puedes reorientar a los usuarios en función de los clics específicos en las páginas de las diapositivas de las historias push. Utiliza el filtro adicional para **Interacted with Campaign**.

## Eventos de datos de S3 y Azure de usuarios anónimos {#s3-and-azure-data-events-from-anonymous-users}

 Los clientes que exportan datos a Amazon S3 y Microsoft Azure ahora pueden incluir eventos de usuarios anónimos. Esta funcionalidad estará activada de forma predeterminada para todas las integraciones recién creadas, pero permanecerá desactivada para todas las integraciones existentes. Si tienes alguna pregunta, ponte en contacto con tu director de cuentas o abre un [ticket de soporte]({{site.baseurl}}/braze_support/).

## Integración de cohortes de Mixpanel {#mixpanel-cohorts-integration}

Los clientes de Braze y Mixpanel ahora pueden integrar y [enviar cohortes de Mixpanel a Braze como filtros de segmento]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/#mixpanel-cohort-import). Puedes configurar una exportación manual única o una exportación dinámica cada dos horas. Cada usuario actualizado contará como un punto de datos, pero Mixpanel solo envía los cambios desde la última sincronización.