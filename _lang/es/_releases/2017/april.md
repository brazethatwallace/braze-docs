---
nav_title: Abril
page_order: 9
noindex: true
page_type: update
description: "Este artículo contiene notas de la versión de abril de 2017."
---

# Abril de 2017 {#april-2017}

## Mensajes HTML en el navegador {#html-in-browser-messages}

Ahora admitimos tipos de mensajes interactivos en el navegador, incluidos HTML personalizado y formatos de captura de correo electrónico, lo que te permite llegar a tus clientes estén donde estén. Más información sobre [los mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/best_practices).

## Mensaje personalizado dentro de la aplicación con contenido conectado {#personalized-in-app-message-with-connected-content}

Hemos añadido los bloques {% raw %} {%connected_content%} {% endraw %} en los mensajes desencadenados dentro de la aplicación, lo que te permite añadir una personalización enriquecida insertando cualquier información accesible a través de la API directamente en tus mensajes. Ahora puedes utilizar contenido conectado dentro de tu aplicación, además de tus push, correos electrónicos y webhooks. Más información sobre [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content).

## Navegación mejorada para las tarjetas de News Feed {#improved-navigation-for-news-feed-cards}

Hemos mejorado la interfaz de usuario para crear tarjetas de News Feed, facilitándote la navegación y la creación de tus campañas. Más información sobre [las tarjetas de News Feed]({{site.baseurl}}/user_guide/engagement_tools/news_feed/creating_a_news_feed_item#news-feed-cards).

## Vista previa mejorada de las notificaciones enriquecidas de iOS {#improved-preview-for-ios-rich-notifications}

Nuestras notificaciones de vista previa en iOS muestran ahora notificaciones enriquecidas que te ofrecen una visión clara de lo que estás enviando exactamente a tus clientes, hasta el tamaño de la fuente. Más información sobre [las notificaciones enriquecidas de iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#ios-10-rich-notifications).

## Se ha añadido "Influenced Opens" a las estadísticas push {#added-influenced-opens-to-push-statistics}

Hemos añadido "Influenced Opens" a nuestra lista de estadísticas estándar de Campaign y Canvas ofrecidas en Braze, lo que facilita conocer el desglose de aperturas influenciadas, directas y totales de tus campañas. Más información sobre [Influenced Opens]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens).

## Actualización a grupos internos {#upgrade-to-internal-groups}

Ahora puedes crear varios grupos internos y asignar propiedades que indiquen si el grupo se utilizará para el registro del SDK, el registro de la REST API o la comprobación del contenido de los mensajes. Más información sobre [los registros de eventos de usuario]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab#event-user-log-tab).

> Actualización: Los grupos internos también pueden utilizarse para [enviar correos electrónicos semilla]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console#seed-groups).

## Nuevas opciones para las URL web {#new-options-for-web-urls}

Ahora tienes la opción de abrir URL web en un navegador web externo para mensajes push, mensajes dentro de la aplicación y en el navegador, y tarjetas de News Feed. La acción "Vínculo profundo a la aplicación" ahora también es compatible con los vínculos profundos HTTP/HTTPS. Si utilizas un partner como Branch o Universal Links de Apple, necesitarás personalizar el SDK. Más información sobre [vinculación en profundidad]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#what-is-deep-linking).

## Nuevo evento "Conversión realizada" en Canvas {#new-performed-conversion-event-canvas}

Hemos añadido un nuevo evento "Conversión realizada" y un filtro "En control de Canvas" para mejorar las opciones de reorientación. Más información sobre el uso de [filtros de reorientación]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns).