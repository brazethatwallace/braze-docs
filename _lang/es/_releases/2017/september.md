---
nav_title: Septiembre
page_order: 4
noindex: true
page_type: update
description: "Este artículo contiene notas de la versión de septiembre de 2017."
---

# Septiembre de 2017 {#september-2017}

## Nueva funcionalidad para los informes de participación {#new-functionality-for-engagement-reports}

Ahora puedes utilizar [los informes de participación]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports#engagement-reports) para agregar métricas de una Campaign en periodos de tiempo específicos. Por ejemplo, puedes exportar el número total de aperturas de un trimestre, o el número total de clics de toda la vida de una Campaign o Canvas. Esto es todo lo que tienes que hacer:
- Selecciona un periodo de tiempo a partir del cual exportar los datos,
- Programa un informe de participación que se envíe a uno o varios destinatarios de forma periódica, y
- Añade Campaigns y Canvas a tu informe basándote en sus etiquetas.

## Actualizaciones de la página de perfil de usuario {#updates-to-user-profile-page}

Se ha actualizado [la página de perfil de usuario]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#access-profiles).

## Notificaciones push web que requieren la acción del usuario para ser descartadas {#web-push-notifications-that-require-user-action-to-dismiss}

Ahora puedes configurar el comportamiento de cierre de mensajes para los push web de Chrome, que requiere que el destinatario interactúe con el mensaje para que este se descarte. Esta característica requiere el SDK Web versión 1.6.13 o superior.

## Preencabezados de correo electrónico {#email-preheaders}

Al crear un mensaje de correo electrónico en Braze, ahora puedes insertar fácilmente un preencabezado en la sección **Sending Info**.

## Nuevo endpoint de la API para la exportación de eventos sin procesar {#new-api-endpoint-for-raw-event-export}

Hemos añadido un nuevo [endpoint de la API]({{site.baseurl}}/developer_guide/rest_api/api_network_connectivity_issues#whitelisting-brazes-api-endpoint-ip-ranges), `/raw_data/status`, que te permite consultar si un día determinado se ha cargado en la exportación de eventos sin procesar. Puedes utilizarlo para comprobar si los datos brutos de un día concreto están disponibles, como ayuda para la depuración y la automatización.