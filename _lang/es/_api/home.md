---
page_order: 0
nav_title: Inicio
article_title: Guía de la API de Braze
layout: api_glossary
glossary_top_header: "Guía de la API de Braze"
glossary_top_text: "Braze ofrece una REST API de alto rendimiento para rastrear usuarios, enviar mensajes, exportar datos y gestionar Campaigns, Canvas, catálogos y más. Usa este glosario para explorar los endpoints por tipo, abre artículos de referencia para ver detalles de solicitudes y respuestas, y encuentra enlaces a documentación sobre autenticación, límites de velocidad y objetos."
description: "Explora los endpoints de la REST or transferencia de estado representacional API de Braze por tipo, con enlaces a documentación sobre autenticación, límites de velocidad y referencia de objetos."
page_type: glossary
glossary_tag_name: Tipo de endpoint

glossary_filter_text: "Selecciona el tipo de endpoint para filtrar el glosario:"

glossary_mid_text: "Búsqueda de endpoints"
guide_featured_list:
  - name: Resumen de la API
    image: /assets/img/braze_icons/annotation-info.svg
    link: /docs/api/basics
  - name: Tipos de identificadores de API
    link: /docs/api/identifier_types
    image: /assets/img/braze_icons/clipboard-check.svg
  - name: Objetos y filtros
    link: /docs/api/objects_filters
    image: /assets/img/braze_icons/settings-01.svg
  - name: Errores y respuestas
    link: /docs/api/errors
    image: /assets/img/braze_icons/list.svg
  - name: Retención de datos
    link: /docs/api/data_retention
    image: /assets/img/braze_icons/laptop-02.svg
  - name: Límites de velocidad
    link: /docs/api/api_limits
    image: /assets/img/braze_icons/hand.svg

# channel to icon/fa or image mapping
glossary_tags:
  - name: Apps
  - name: Campaigns
  - name: Canvas
  - name: Catalogs
  - name: Content Blocks
  - name: Custom Events
  - name: Data Objects
  - name: Email List
  - name: Email Templates
  - name: Webhook Templates
  - name: KPI
  - name: Media Library
  - name: Device Messaging API
  - name: Purchases
  - name: Preference Center
  - name: Schedule Messages
  - name: SCIM
  - name: SDK Authentication
  - name: Segments
  - name: Send Messages
  - name: SMS
  - name: Subscription Groups
  - name: User Data
  - name: Live Activity
  - name: Cloud Data Ingestion

glossaries:
  - name: <a href='/docs/api/endpoints/apps/post_update_push_credential'>/apps/push_credential/update</a>
    description: Actualiza las credenciales push de una sola aplicación.
    tags:
      - Apps
  - name: <a href='/docs/api/endpoints/user_data/post_user_alias'>/users/alias/new</a>
    description: Añade nuevos alias de usuario para usuarios identificados existentes o crea nuevos usuarios no identificados.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_users_alias_update'>/users/alias/update</a>
    description: Actualiza los nombres de alias de usuario existentes a nuevos nombres de alias de usuario.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_user_delete'>/users/delete</a>
    description: Elimina cualquier perfil de usuario especificando un identificador de usuario conocido.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/export/user_data/post_users_global_control_group'>/users/export/global_control_group</a>
    description: Exporta todos los usuarios de un grupo de control global.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/export/user_data/post_users_identifier'>/users/export/ids</a>
    description: Exporta datos de cualquier perfil de usuario especificando un identificador de usuario.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/export/user_data/post_users_segment'>/users/export/segment</a>
    description: Exporta todos los usuarios de un Segment.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename'>/users/external_ids/rename</a>
    description: Cambia el nombre de los ID externos de tus usuarios.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove'>/users/external_ids/remove</a>
    description: Elimina los antiguos ID externos obsoletos de tus usuarios.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_user_identify'>/users/identify</a>
    description: Identifica a un usuario no identificado (solo alias).
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_user_track'>/users/track</a>
    description: Registra eventos personalizados, compras y actualiza los atributos del perfil de usuario.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_users_merge'>/users/merge</a>
    description: Fusiona un perfil de usuario con otro usuario.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/data_objects'>/data_objects/*</a>
    description: Consulta la referencia completa de endpoints de Data Objects, incluidos tipos de objeto, objetos y endpoints de relaciones.
    tags:
      - Data Objects
  - name: <a href='/docs/api/endpoints/data_objects/types/get_list_data_object_types'>/data_objects/types</a>
    description: Lista los tipos de Data Objects en el espacio de trabajo.
    tags:
      - Data Objects
  - name: <a href='/docs/api/endpoints/data_objects/types/get_data_object_type'>/data_objects/types/{type_name}</a>
    description: Obtiene un tipo de Data Object y su definición de esquema.
    tags:
      - Data Objects
  - name: <a href='/docs/api/endpoints/data_objects/types/get_list_user_relationship_types'>/data_objects/types/{type_name}/user_relationship_types</a>
    description: Lista los tipos de relación de usuario para un tipo de Data Object.
    tags:
      - Data Objects
  - name: <a href='/docs/api/endpoints/data_objects/types/get_list_object_relationship_types'>/data_objects/types/{type_name}/object_relationship_types</a>
    description: Lista los tipos de relación de objeto para un tipo de Data Object.
    tags:
      - Data Objects
  - name: <a href='/docs/api/endpoints/data_objects/objects/get_list_data_objects'>/data_objects/objects/{type_name}</a>
    description: Lista los Data Objects de un tipo.
    tags:
      - Data Objects
  - name: <a href='/docs/api/endpoints/data_objects/objects/get_data_object'>/data_objects/objects/{type_name}/{external_id}</a>
    description: Obtiene un Data Object, o lo reemplaza, actualiza y elimina.
    tags:
      - Data Objects
  - name: <a href='/docs/api/endpoints/data_objects/object_relationships/get_list_object_relationships'>/data_objects/objects/{type_name}/{external_id}/object_relationships</a>
    description: Lista, crea, reemplaza, actualiza y elimina relaciones entre objetos.
    tags:
      - Data Objects
  - name: <a href='/docs/api/endpoints/data_objects/user_relationships/get_list_user_relationships'>/data_objects/objects/{type_name}/{external_id}/user_relationships</a>
    description: Lista las relaciones de usuario para un Data Object.
    tags:
      - Data Objects
  - name: <a href='/docs/api/endpoints/data_objects/user_relationships/post_create_user_relationship'>/data_objects/objects/{type_name}/{external_id}/users</a>
    description: Crea, reemplaza, actualiza y elimina relaciones entre usuarios y objetos.
    tags:
      - Data Objects
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns'>/campaigns/trigger/send</a>
    description: Envía mensajes inmediatos y puntuales a usuarios designados mediante entrega desencadenada por API.
    tags:
      - Send Messages
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases'>/canvas/trigger/send</a>
    description: Envía mensajes de Canvas mediante entrega desencadenada por API.
    tags:
      - Send Messages
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_send_messages'>/messages/send</a>
    description: Envía mensajes inmediatos y puntuales a usuarios designados a través de la API de Braze.
    tags:
      - Send Messages
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_create_send_ids'>/sends/id/create</a>
    description: Crea ID de envío para enviar mensajes y realizar el seguimiento del rendimiento de los mensajes de forma programática, sin necesidad de crear una Campaign para cada envío.
    tags:
      - Send Messages
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_send_transactional_message'>/transactional/v1/campaigns/{CAMPAIGN_ID}/send</a>
    description: Envía mensajes transaccionales inmediatos y puntuales a un usuario designado.
    tags:
      - Send Messages
  - name: <a href='/docs/api/device_messaging_api/endpoints/banners/post_sync_banners'>/v1/device-messaging/banners/sync</a>
    description: Recupera los banners elegibles para un usuario y un conjunto de ubicaciones.
    tags:
      - Device Messaging API
  - name: <a href='/docs/api/device_messaging_api/endpoints/banners/post_track_banner_events'>/v1/device-messaging/banners/track</a>
    description: Registra eventos de impresión y clic para banners.
    tags:
      - Device Messaging API
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns'>/campaigns/trigger/schedule/create</a>
    description: Envía mensajes de Campaign creados en el panel mediante entrega desencadenada por API.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages'>/campaigns/trigger/schedule/delete</a>
    description: Cancela mensajes de Campaign desencadenados por API que hayas programado previamente antes de que se hayan enviado.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns'>/campaigns/trigger/schedule/update</a>
    description: Actualiza Campaigns programadas desencadenadas por API creadas en el panel.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases'>/canvas/trigger/schedule/delete</a>
    description: Cancela un mensaje de Canvas que hayas programado previamente mediante entrega desencadenada por API antes de que se haya enviado.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases'>/canvas/trigger/schedule/create</a>
    description: Programa mensajes de Canvas mediante entrega desencadenada por API.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages'>/messages/schedule/update</a>
    description: Actualiza los mensajes programados. Este endpoint acepta actualizaciones del parámetro <code>schedule</code> o <code>messages</code>, o ambos.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages'>/messages/schedule/delete</a>
    description: Cancela un mensaje programado previamente antes de que se haya enviado.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_messages'>/messages/schedule/create</a>
    description: Programa una Campaign, un Canvas u otro mensaje para que se envíe a una hora determinada.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases'>/canvas/trigger/schedule/update</a>
    description: Actualiza Canvas programados desencadenados por API que creaste en el panel.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled'>/messages/scheduled_broadcasts</a>
    description: Devuelve una lista JSON con información sobre Campaigns programadas y Canvas de entrada entre el momento actual y el <code>end_time</code> especificado en la solicitud.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/live_activity/update'>/messages/live_activity/update</a>
    description: Actualiza una Live Activity de iOS.
    tags:
      - Live Activity
  - name: <a href='/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status'>/subscription/status/set</a>
    description: Actualiza por lotes el estado de suscripción de hasta 50 usuarios en el panel de Braze.
    tags:
      - Subscription Groups
  - name: <a href='/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2'>/v2/subscription/status/set</a>
    description: Actualiza por lotes el estado de suscripción de hasta 50 usuarios en el panel de Braze.
    tags:
      - Subscription Groups
  - name: <a href='/docs/api/endpoints/subscription_groups/get_list_user_subscription_group_status'>/subscription/status/get</a>
    description: Obtiene el estado de suscripción de un usuario en un grupo de suscripción.
    tags:
      - Subscription Groups
  - name: <a href='/docs/api/endpoints/subscription_groups/get_list_user_subscription_groups'>/subscription/user/status</a>
    description: Lista y obtiene los grupos de suscripción de un determinado usuario.
    tags:
      - Subscription Groups
  - name: <a href='/docs/api/endpoints/email/post_blacklist'>/email/blacklist</a>
    description: Cancela la suscripción de un usuario de correo electrónico y lo marca como rebote duro.
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/email/post_remove_hard_bounces'>/email/bounce/remove</a>
    description: Elimina direcciones de correo electrónico de tu lista de rebotes de Braze.
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/email/post_remove_spam'>/email/spam/remove</a>
    description: Elimina direcciones de correo electrónico de tu lista de correo no deseado de Braze.
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/email/post_email_subscription_status'>/email/status</a>
    description: Establece el estado de suscripción de correo electrónico para tus usuarios.
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/templates/email_templates/post_create_email_template'>/templates/email/create</a>
    description: Crea plantillas de correo electrónico en el panel de Braze.
    tags:
      - Email Templates
  - name: <a href='/docs/api/endpoints/templates/email_templates/post_update_email_template'>/templates/email/update</a>
    description: Actualiza plantillas de correo electrónico en el panel de Braze.
    tags:
      - Email Templates
  - name: <a href='/docs/api/endpoints/email/get_list_hard_bounces'>/email/hard_bounces</a>
    description: Obtiene una lista de las direcciones de correo electrónico que han tenido un "rebote duro" en tus mensajes de correo electrónico en un plazo determinado.
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/email/get_query_unsubscribed_email_addresses'>/email/unsubscribes</a>
    description: Devuelve los correos electrónicos que cancelaron su suscripción durante el periodo de tiempo de <code>start_date</code> a <code>end_date</code>.
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/templates/email_templates/get_see_email_template_information'>/templates/email/info</a>
    description: Obtiene información sobre tus plantillas de correo electrónico.
    tags:
      - Email Templates
  - name: <a href='/docs/api/endpoints/templates/email_templates/get_list_email_templates'>/templates/email/list</a>
    description: Obtiene una lista de las plantillas de correo electrónico disponibles en tu cuenta de Braze.
    tags:
      - Email Templates
  - name: <a href='/docs/api/endpoints/translations/webhook_templates/get_view_source_webhook_template'>/templates/webhook/translations/source</a>
    description: Consulta las traducciones de origen predeterminadas de una plantilla de webhook.
    tags:
      - Webhook Templates
  - name: <a href='/docs/api/endpoints/translations/webhook_templates/get_view_translations_webhook_template'>/templates/webhook/translations</a>
    description: Consulta las traducciones de una plantilla de webhook.
    tags:
      - Webhook Templates
  - name: <a href='/docs/api/endpoints/translations/webhook_templates/put_update_webhook_template'>/templates/webhook/translations</a>
    description: Actualiza las traducciones de una plantilla de webhook.
    tags:
      - Webhook Templates
  - name: <a href='/docs/api/endpoints/export/campaigns/get_campaign_analytics'>/campaigns/data_series</a>
    description: Recupera una serie diaria de diversas estadísticas de una Campaign a lo largo del tiempo.
    tags:
      - Campaigns
  - name: <a href='/docs/api/endpoints/export/campaigns/get_campaign_details'>/campaigns/details</a>
    description: Recupera información relevante sobre una Campaign especificada.
    tags:
      - Campaigns
  - name: <a href='/docs/api/endpoints/export/campaigns/get_campaigns'>/campaigns/list</a>
    description: Exporta una lista de Campaigns, cada una de las cuales incluye su nombre, el identificador de API de la Campaign, si se trata de una Campaign de API y las etiquetas asociadas a la Campaign.
    tags:
      - Campaigns
  - name: <a href='/docs/api/endpoints/export/campaigns/get_send_analytics'>/sends/data_series</a>
    description: Recupera una serie diaria de diversas estadísticas de un <code>send_id</code> con seguimiento.
    tags:
      - Campaigns
  - name: <a href='/docs/api/endpoints/export/canvas/get_canvas_analytics'>/canvas/data_series</a>
    description: Exporta datos de series temporales para un Canvas.
    tags:
      - Canvas
  - name: <a href='/docs/api/endpoints/export/canvas/get_canvas_analytics_summary'>/canvas/data_summary</a>
    description: Exporta resúmenes acumulados de datos de series temporales para un Canvas, proporcionando un resumen conciso de los resultados del Canvas.
    tags:
      - Canvas
  - name: <a href='/docs/api/endpoints/export/canvas/get_canvas_details'>/canvas/details</a>
    description: Exporta metadatos sobre un Canvas, como el nombre, la hora de creación, el estado actual y más.
    tags:
      - Canvas
  - name: <a href='/docs/api/endpoints/export/canvas/get_canvases'>/canvas/list</a>
    description: Exporta una lista de Canvas, incluido el nombre, el identificador de API del Canvas y las etiquetas asociadas.
    tags:
      - Canvas
  - name: <a href='/docs/api/endpoints/export/segments/get_segment_analytics'>/segments/data_series</a>
    description: Recupera una serie diaria del tamaño estimado de un Segment a lo largo del tiempo.
    tags:
      - Segments
  - name: <a href='/docs/api/endpoints/export/segments/get_segment_details'>/segments/details</a>
    description: Recupera información relevante sobre un Segment.
    tags:
      - Segments
  - name: <a href='/docs/api/endpoints/export/segments/get_segment'>/segments/list</a>
    description: Exporta una lista de Segments, cada uno de los cuales incluye su nombre, el identificador de API del Segment y si tiene habilitado el seguimiento de análisis.
    tags:
      - Segments
  - name: <a href='/docs/api/endpoints/export/segments/post_cancel_export'>/export/segment/cancel</a>
    description: Cancela las exportaciones para el ID de Segment proporcionado.
    tags:
      - Segments
  - name: <a href='/docs/api/endpoints/export/sessions/get_sessions_analytics'>/sessions/data_series</a>
    description: Recupera una serie del número de sesiones de tu aplicación durante un periodo de tiempo determinado.
    tags:
      - Sessions
  - name: <a href='/docs/api/endpoints/export/custom_attributes/get_custom_attributes'>/custom_attributes</a>
    description: Exporta una lista de atributos personalizados que incluye el nombre, la descripción, el tipo de datos, la longitud de la matriz (si corresponde), el estado y las etiquetas asociadas.
    tags:
      - Custom Attributes
  - name: <a href='/docs/api/endpoints/export/custom_events/get_custom_events_analytics'>/events/data_series</a>
    description: Recupera una serie del número de ocurrencias de un evento personalizado en tu aplicación durante un periodo de tiempo determinado.
    tags:
      - Custom Events
  - name: <a href='/docs/api/endpoints/export/custom_events/get_custom_events_data'>/events</a>
    description: Exporta una lista de eventos personalizados que incluye el nombre, la descripción, el estado, las etiquetas asociadas y la inclusión en informes de análisis.
    tags:
      - Custom Events
  - name: <a href='/docs/api/endpoints/export/custom_events/get_custom_events'>/events/list</a>
    description: Exporta una lista con los nombres de los eventos personalizados registrados para tu aplicación.
    tags:
      - Custom Events
  - name: <a href='/docs/api/endpoints/templates/content_blocks_templates/post_create_email_content_block'>/content_blocks/create</a>
    description: Crea un Content Block de correo electrónico.
    tags:
      - Content Blocks
  - name: <a href='/docs/api/endpoints/templates/content_blocks_templates/post_update_content_block'>/content_blocks/update</a>
    description: Actualiza un Content Block de correo electrónico.
    tags:
      - Content Blocks
  - name: <a href='/docs/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information'>/content_blocks/info</a>
    description: Consulta información de tu Content Block de correo electrónico existente.
    tags:
      - Content Blocks
  - name: <a href='/docs/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks'>/content_blocks/list</a>
    description: Lista la información de tus Content Blocks existentes.
    tags:
      - Content Blocks
  - name: <a href='/docs/api/endpoints/export/kpi/get_kpi_dau_date'>/kpi/dau/data_series</a>
    description: Recupera una serie diaria del número total de usuarios activos únicos en cada fecha.
    tags:
      - KPI
  - name: <a href='/docs/api/endpoints/export/kpi/get_kpi_mau_30_days'>/kpi/mau/data_series</a>
    description: Recupera una serie diaria del número total de usuarios activos únicos durante una ventana móvil de 30 días.
    tags:
      - KPI
  - name: <a href='/docs/api/endpoints/export/kpi/get_kpi_daily_new_users_date'>/kpi/new_users/data_series</a>
    description: Recupera una serie diaria del número total de nuevos usuarios en cada fecha.
    tags:
      - KPI
  - name: <a href='/docs/api/endpoints/export/kpi/get_kpi_uninstalls_date'>/kpi/uninstalls/data_series</a>
    description: Recupera una serie diaria del número total de desinstalaciones en cada fecha.
    tags:
      - KPI
  - name: <a href='/docs/api/endpoints/sms/post_remove_invalid_numbers'>/sms/invalid_phone_numbers/remove</a>
    description: "Elimina números de teléfono \"no válidos\" de la lista de no válidos en Braze. Usa esto para volver a validar los números de teléfono después de que Braze los haya marcado como no válidos."
    tags:
      - SMS
  - name: <a href='/docs/api/endpoints/sms/get_query_invalid_numbers'>/sms/invalid_phone_numbers</a>
    description: Obtiene una lista de números de teléfono que Braze ha marcado como "no válidos" en un periodo de tiempo determinado.
    tags:
      - SMS
  - name: <a href='/docs/api/endpoints/export/purchases/get_list_product_id'>/purchases/product_list</a>
    description: Devuelve una lista paginada de ID de productos.
    tags:
      - Purchases
  - name: <a href='/docs/api/endpoints/export/purchases/get_number_of_purchases'>/purchases/quantity_series</a>
    description: Devuelve el número total de compras en tu aplicación durante un intervalo de tiempo.
    tags:
      - Purchases
  - name: <a href='/docs/api/endpoints/export/purchases/get_revenue_series'>/purchases/revenue_series</a>
    description: Devuelve el dinero total gastado en tu aplicación durante un intervalo de tiempo.
    tags:
      - Purchases
  - name: <a href='/docs/api/endpoints/preference_center/get_create_url_preference_center'>/preference_center/v1/{preferenceCenterExternalId}/url/{userId}</a>
    description: Crea una URL para un centro de preferencias.
    tags:
      - Preference Center
  - name: <a href='/docs/api/endpoints/preference_center/get_list_preference_center'>/preference_center/v1/list</a>
    description: Lista los centros de preferencias disponibles.
    tags:
      - Preference Center
  - name: <a href='/docs/api/endpoints/preference_center/get_view_details_preference_center'>/preference_center/v1/{preferenceCenterExternalId}</a>
    description: Consulta los detalles de tu centro de preferencias, incluyendo cuándo se creó y actualizó.
    tags:
      - Preference Center
  - name: <a href='/docs/api/endpoints/preference_center/post_create_preference_center'>/preference_center/v1</a>
    description: Crea un centro de preferencias que permita a los usuarios gestionar sus preferencias de notificación para Campaigns de correo electrónico.
    tags:
      - Preference Center
  - name: <a href='/docs/api/endpoints/preference_center/put_update_preference_center'>/preference_center/v1/{preferenceCenterExternalId}</a>
    description: Actualiza un centro de preferencias.
    tags:
      - Preference Center
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk'>/catalogs/{catalog_name}/items</a>
    description: Elimina varios elementos de tu catálogo.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details'>/catalogs/{catalog_name}/items/{item_id}</a>
    description: Lista un elemento del catálogo y sus detalles.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk'>/catalogs/{catalog_name}/items</a>
    description: Edita varios elementos de tu catálogo.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk'>/catalogs/{catalog_name}/items</a>
    description: Crea varios elementos en tu catálogo.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog'>/catalogs/{catalog_name}</a>
    description: Elimina un catálogo.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog'>/catalogs</a>
    description: Crea un catálogo.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs'>/catalogs</a>
    description: Lista los catálogos de un espacio de trabajo.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item'>/catalogs/{catalog_name}/items/{item_id}</a>
    description: Crea un elemento en un catálogo.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item'>/catalogs/{catalog_name}/items/{item_id}</a>
    description: Edita un elemento de un catálogo.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk'>/catalogs/{catalog_name}/items</a>
    description: Devuelve varios elementos del catálogo y su contenido.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item'>/catalogs/{catalog_name}/items/{item_id}</a>
    description: Elimina un elemento de un catálogo.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item'>/catalogs/{catalog_name}/items/{item_id}</a>
    description: Reemplaza un elemento en un catálogo.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items'>/catalogs/{catalog_name}/items/</a>
    description: Reemplaza varios elementos en un catálogo.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields'>/catalogs/{catalog_name}/fields/</a>
    description: Crea varios campos en un catálogo.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field'>/catalogs/{catalog_name}/fields/{field_name}</a>
    description: Elimina un campo de un catálogo.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections'>/catalogs/{catalog_name}/selections</a>
    description: Crea una selección en un catálogo.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection'>/catalogs/{catalog_name}/selections/{selection_name}</a>
    description: Elimina una selección del catálogo.
    tags:
      - Catalogs
  - name: <a href='/docs/post_create_user_account'>/scim/v2/Users</a>
    description: Crea una nueva cuenta de usuario del panel especificando correo electrónico, nombre y apellidos, y permisos (para establecer permisos a nivel de empresa, espacio de trabajo y equipo).
    tags:
      - SCIM
  - name: <a href='/docs/get_see_user_account_information'>/scim/v2/Users/{id}</a>
    description: Busca una cuenta de usuario existente en el panel especificando su ID de recurso.
    tags:
      - SCIM
  - name: <a href='/docs/post_update_existing_user_account'>/scim/v2/Users/{id}</a>
    description: Actualiza una cuenta de usuario existente en el panel especificando correo electrónico, nombre y apellidos, y permisos (para establecer permisos a nivel de empresa, espacio de trabajo y equipo).
    tags:
      - SCIM
  - name: <a href='/docs/delete_existing_dashboard_user'>/scim/v2/Users/{id}</a>
    description: Elimina de forma permanente un usuario existente del panel.
    tags:
      - SCIM
  - name: <a href='/docs/get_search_existing_dashboard_user_email'>/scim/v2/Users?filter={userName@example.com}</a>
    description: Busca una cuenta de usuario existente en el panel especificando su dirección de correo electrónico.
    tags:
      - SCIM
  - name: <a href='/docs/api/endpoints/cdi/get_integration_list'>/cdi/integrations</a>
    description: Devuelve una lista de las integraciones existentes.
    tags:
      - Cloud Data Ingestion
  - name: <a href='/docs/api/endpoints/cdi/post_job_sync'>/cdi/integrations/{integration_id}/sync</a>
    description: Activa una sincronización para una integración determinada.
    tags:
      - Cloud Data Ingestion
  - name: <a href='/docs/api/endpoints/cdi/get_job_sync_status'>/cdi/integrations/{integration_id}/job_sync_status</a>
    description: Devuelve una lista de estados de sincronización.
    tags:
      - Cloud Data Ingestion
  - name: <a href='/docs/api/endpoints/sdk_authentication/post_create_sdk_authentication_key'>/app_group/sdk_authentication/create</a>
    description: Crea una nueva clave de autenticación del SDK or kit de desarrollo de software para tu aplicación.
    tags:
      - SDK Authentication
  - name: <a href='/docs/api/endpoints/sdk_authentication/get_sdk_authentication_keys'>/app_group/sdk_authentication/keys</a>
    description: Lista las claves de autenticación del SDK or kit de desarrollo de software para tu aplicación.
    tags:
      - SDK Authentication
  - name: <a href='/docs/api/endpoints/sdk_authentication/put_primary_sdk_authentication_key'>/app_group/sdk_authentication/primary</a>
    description: Establece una clave de autenticación del SDK or kit de desarrollo de software como clave principal para tu aplicación.
    tags:
      - SDK Authentication
  - name: <a href='/docs/api/endpoints/sdk_authentication/delete_sdk_authentication_key'>/app_group/sdk_authentication/delete</a>
    description: Elimina una clave de autenticación del SDK or kit de desarrollo de software para tu aplicación.
    tags:
      - SDK Authentication
  - name: <a href='/docs/api/endpoints/media_library/manage_assets/create'>/media_library/create</a>
    description: Sube un activo a la biblioteca de medios.
    tags:
      - Media Library
---