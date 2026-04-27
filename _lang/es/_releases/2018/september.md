---
nav_title: Septiembre
page_order: 5
noindex: true
page_type: update
description: "Este artículo contiene notas de la versión de septiembre de 2018."
---
# Septiembre de 2018 {#september-2018}

## Grupos de notificaciones de iOS 12: capacidades adicionales {#ios-12-notification-groups-additional-abilities}

¡Ya puedes acceder a [las características del grupo de notificaciones de Apple]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#notification-groups) utilizando Braze! Puedes añadir argumentos de resumen y grupos, utilizar alertas críticas, filtrar por usuarios autenticados provisionalmente y ver el estado de autenticación provisional en los perfiles de usuario.

## Horas tranquilas {#quiet-time}

Ahora los clientes pueden especificar [horas tranquilas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-5-select-your-send-settings) (el tiempo durante el cual no se enviarán tus mensajes) para Canvas. Solo tienes que ir a tu **configuración de envío de Canvas** y marcar "Habilitar horas tranquilas". A continuación, selecciona tus horas tranquilas en la hora local de tu usuario y qué acción seguirá si el mensaje se desencadena dentro de esas horas tranquilas.

Las Campaigns ahora también utilizan las horas tranquilas en lugar de "envía este mensaje durante una parte específica del día".

## Clientes de Adjust {#adjust-customers}

Los clientes de Braze que utilicen [Adjust]({{site.baseurl}}/partners/message_orchestration/attribution/adjust/) ahora pueden ver su clave de API de Braze y la URL de su instancia de Braze, que luego utilizarán en la plataforma Adjust para la integración.

## Filtro "no en el segmento" {#not-in-segment-filter}

Ahora los clientes pueden crear un segmento a partir de los usuarios que [no están incluidos en un segmento determinado]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#retargeting).

## Exportaciones CSV de destinatarios de Canvas {#canvas-recipient-csv-exports}

Ahora los clientes pueden [exportar datos]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_canvas_data/) sobre los usuarios que han entrado en un Canvas. El CSV generado será similar al CSV de la Campaign.

## Filtro de segmento de iOS 12 autorizado provisionalmente {#provisionally-authorized-ios-12-segment-filter}

Se ha añadido un [filtro de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#other) que te permite encontrar usuarios que están provisionalmente autorizados en iOS 12 para una aplicación determinada.

## Cargador de imágenes de mensajes dentro de la aplicación {#in-app-message-image-uploader}

El cargador de imágenes para mensajes dentro de la aplicación se ha movido del panel de diseño al panel de redacción.

## Permisos de solo lectura en la página de perfil de usuario {#read-only-permissions-on-user-profile-page}

Antes de esta versión, los clientes podían cambiar el estado de la suscripción y la dirección de correo electrónico en el perfil de usuario con [permisos de solo lectura]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions). Cambiamos el nombre del permiso `import_user` a permiso `import_and_update_user` y restringimos el acceso de edición al estado de la suscripción y a la dirección de correo electrónico. Ahora, cuando un desarrollador se hace pasar por alguien de solo lectura o carece de este permiso, no puede cambiar el estado de la suscripción ni la dirección de correo electrónico.