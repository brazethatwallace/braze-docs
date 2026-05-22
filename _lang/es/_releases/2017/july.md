---
nav_title: Julio
page_order: 6
noindex: true
page_type: update
description: "Este artículo contiene notas de la versión de julio de 2017."
---

# Julio de 2017 {#july-2017}

## Imágenes grandes en la notificación push web {#large-images-in-web-push}

Hemos añadido compatibilidad con imágenes grandes para notificación push web en Chrome para Windows y Android, dándote la posibilidad de crear experiencias del cliente enriquecidas y atractivas. Más información sobre [notificaciones push web]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/web/).

## Actualizaciones de los campos de correo electrónico {#updates-to-email-fields}

Ahora puedes bloquear correos electrónicos a un conjunto específico de direcciones de origen, para asegurarte de que no introduces accidentalmente una dirección incorrecta. El formulario de composición de correo electrónico se rellenará previamente con las direcciones utilizadas en los últimos 6 meses para agilizar el proceso. Consulta [las mejores prácticas de correo electrónico]({{site.baseurl}}/user_guide/channels/email/best_practices/) para obtener más información.

## Actualizaciones de la API de detalles de campaña {#updates-to-campaign-details-api}

El punto de conexión `/campaign/details` ahora proporciona información sobre sus mensajes, permitiéndote extraer los campos asunto, cuerpo HTML, dirección del remitente y responder a mediante la API. Más información sobre [las API de Braze]({{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api).

## Actualizaciones de la plantilla Liquid {#updates-to-liquid-templating}

Hemos añadido la posibilidad de crear plantillas de atributos de variantes en Canvas y Campaigns. En Canvas, ahora puedes crear plantillas tanto para el ID de API de la variante como para el nombre de la variante, y en Campaigns ahora puedes crear plantillas para `message_api_id` y `message_name` de un mensaje. Ambas actualizaciones permiten una mayor flexibilidad en tu mensajería, permitiéndote crear campañas personalizadas. Más información sobre [mensajería personalizada]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/).

## Nuevo editor de correo electrónico HTML {#new-html-email-editor}

Ahora puedes escribir y probar fácilmente correos electrónicos con un editor HTML a pantalla completa que habilita la vista previa en vivo, la personalización mediante Liquid y un editor de texto a pantalla completa mejorado con números de línea y resaltado de sintaxis. Más información sobre [la composición del correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template).

## Actualizaciones de vistas previas {#updates-to-previews}

Ahora puedes seguir la ventana de la pantalla mientras te desplazas por las vistas previas de mensajes en Campaigns y Canvas, asegurándote de que siempre puedes ver reflejados los cambios. Más información sobre [la vista previa y las pruebas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#step-6-preview-message).

## Nuevo filtro de pertenencia a segmento {#new-segment-membership-filter}

Hemos añadido el [filtro de pertenencia a Segment]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#targeting-filters), que te permite dirigirte a los usuarios en función de su pertenencia a cualquiera de tus Segments existentes. Además, hemos añadido la posibilidad de utilizar la lógica "Y" y "O" en los filtros de segmentos, así como la posibilidad de anidar segmentos entre sí. Estas actualizaciones te permiten enviar mensajes personalizados a tus clientes con mayor precisión.

## Actualización de la vista previa de Android {#update-to-android-preview}

Hemos actualizado la [vista previa de Android]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#step-5-preview-message) para reflejar las versiones más recientes de Android desde Android N.