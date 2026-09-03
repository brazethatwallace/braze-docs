---
nav_title: "Resumen de la API"
article_title: "Resumen de la API"
page_order: 2.1
description: "Este artículo de referencia cubre los aspectos básicos de la API, incluyendo qué es una REST API, la terminología y un resumen de las claves de API."
page_type: reference
alias: /api/api_key/
---

# Resumen de la API {#api-overview}

> Este artículo de referencia cubre los conceptos básicos de la API, incluida la terminología común y un resumen de las claves de la REST API, los permisos y cómo mantenerlas seguras.

## Colección de Braze REST API {#braze-rest-api-collection}

| Colección                                                                  | Propósito                                                                                      |
|----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| [Catálogos]({{site.baseurl}}/api/endpoints/catalogs)                       | Crea y gestiona catálogos y elementos de catálogo para hacer referencia en tus Braze Campaigns. |
| [Ingesta de datos en la nube]({{site.baseurl}}/api/endpoints/cdi)          | Gestiona las integraciones y sincronizaciones de tu almacén de datos.                          |
| [Listas y direcciones de correo electrónico]({{site.baseurl}}/api/endpoints/email) | Configura y gestiona la sincronización bidireccional entre Braze y tus sistemas de correo electrónico. |
| [Exportar]({{site.baseurl}}/api/endpoints/export)                         | Accede y exporta diversos detalles de tus Campaigns, Canvas, KPI y más.                       |
| [Biblioteca de medios]({{site.baseurl}}/api/endpoints/media_library)       | Gestiona los activos dentro de Braze.                                                          |
| [Mensajes]({{site.baseurl}}/api/endpoints/messaging)                      | Programa, envía y gestiona tus Campaigns y Canvas.                                             |
| [Centro de preferencias]({{site.baseurl}}/api/endpoints/preference_center) | Crea tu centro de preferencias y actualiza su estilo.                                          |
| [SCIM]({{site.baseurl}}/api/endpoints/scim)                               | Gestiona identidades de usuario en aplicaciones y servicios basados en la nube.                |
| [SMS]({{site.baseurl}}/api/endpoints/sms)                                 | Gestiona los números de teléfono de tus usuarios en tus grupos de suscripción.                 |
| [Grupos de suscripción]({{site.baseurl}}/api/endpoints/subscription_groups) | Lista y actualiza los grupos de suscripción de SMS y correo electrónico almacenados en el panel de Braze. |
| [Plantillas]({{site.baseurl}}/api/endpoints/templates)                    | Crea y actualiza plantillas para mensajería por correo electrónico y Content Blocks.           |
| [Datos de usuario]({{site.baseurl}}/api/endpoints/user_data)              | Identifica, rastrea y gestiona a tus usuarios.                                                 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Colección de Braze REST API" }

## Definiciones de la API {#api-definitions}

A continuación se presenta un resumen de los términos que puedes encontrar en la documentación de la REST API de Braze.

### Endpoints

Braze gestiona varias instancias diferentes para nuestro panel y endpoints REST. Cuando tu cuenta es provisionada, inicias sesión en una de las siguientes URL. Usa el endpoint REST correcto según la instancia a la que estés asignado. Si no estás seguro, abre un [ticket de soporte]({{site.baseurl}}/user_guide/administer/personal/braze_support) o usa la siguiente tabla para hacer coincidir la URL del panel que usas con el endpoint REST correcto.

Para encontrar tu endpoint REST en Braze:

1. Inicia sesión en Braze y ve a **Configuración** > **API e identificadores** > **Claves de API**.
2. Selecciona una clave de API existente o selecciona **Crear clave de API** para crear una nueva.
3. Copia el endpoint REST que se muestra en esta pestaña y usa ese endpoint para tus solicitudes de API.

{% alert important %}
Cuando uses endpoints para llamadas a la API, usa el endpoint REST.

Para la integración de SDK, usa el [punto final de SDK]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints), no el endpoint REST.
{% endalert %}

{% multi_lang_include administer/data_centers.md datacenters='instances' %}

### Límites de la API {#api-limits}

Para la mayoría de las API, Braze tiene un límite de velocidad predeterminado de 250 000 solicitudes por hora. Sin embargo, ciertos tipos de solicitud tienen su propio límite de velocidad aplicado para manejar mejor grandes volúmenes de datos en toda la base de clientes. Para más detalles, consulta [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits)

### ID de usuario {#user-ids}

- **ID externo de usuario**: El `external_id` sirve como identificador único del usuario para el cual estás enviando datos. Este identificador debe ser el mismo que estableces en el SDK de Braze para evitar crear múltiples perfiles para el mismo usuario.
- **ID de usuario de Braze**: El `braze_id` sirve como identificador único de usuario que Braze establece. Puedes usar este identificador para eliminar usuarios a través de la REST API, además de los external_ids.

Para más información, consulta los siguientes artículos según tu plataforma: [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=swift), [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=android) y [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web).

## Acerca de las claves de REST API {#about-rest-api-keys}

Una clave de REST Application Programming Interface (clave de REST API) es un código único que pasas a una API para autenticar la llamada a la API e identificar la aplicación o el usuario que realiza la llamada. Accedes a la API mediante solicitudes web HTTPS al endpoint de REST API de tu empresa. Las claves de REST API funcionan en conjunto con las claves de identificador de aplicación para rastrear, acceder, enviar, exportar y analizar datos, ayudando a garantizar que todo funcione sin problemas.

Los espacios de trabajo y las claves de API van de la mano en Braze. Los espacios de trabajo están diseñados para alojar versiones de la misma aplicación en múltiples plataformas. Muchos clientes también usan espacios de trabajo para contener versiones gratuitas y premium de sus aplicaciones en la misma plataforma. Como podrás notar, estos espacios de trabajo también utilizan la REST API y tienen sus propias claves de REST API. Estas claves pueden tener alcances individuales para incluir acceso a endpoints específicos de la API. Cada llamada a la API debe incluir una clave con acceso al endpoint invocado.

Nos referimos tanto a la clave de REST API como a la clave de API del espacio de trabajo como `api_key`. La `api_key` se incluye en cada solicitud como un encabezado de solicitud y actúa como una clave de autenticación que te permite usar nuestras REST API. Estas REST API se utilizan para rastrear usuarios, enviar mensajes, exportar datos de usuario y más. Cuando creas una nueva clave de REST API, debes darle acceso a endpoints específicos. Al asignar permisos específicos a una clave de API, puedes limitar exactamente qué llamadas puede autenticar una clave de API.

![Panel de claves de REST API en la pestaña Claves de API.]({% image_buster /assets/img_archive/rest-api-key.png %})

{% alert tip %}
Además de las claves de REST API, también existe un tipo de clave llamada claves de identificador que se pueden usar para hacer referencia a elementos específicos como aplicaciones, plantillas, Canvas, Campaigns, Content Cards y Segments desde la API. Para más información, consulta [Tipos de identificadores de API]({{site.baseurl}}/api/identifier_types).
{% endalert %}

### Crear claves de REST API {#creating-rest-api-keys}

Para crear una nueva clave de REST API:

1. Ve a **Configuración** > **API e identificadores**.
2. Selecciona **Crear clave de API**.
3. Asigna un nombre a tu nueva clave para identificarla de un vistazo.
4. Especifica las [direcciones IP permitidas](#api-ip-allowlisting) y subredes para la nueva clave.
5. Selecciona qué [permisos](#rest-api-key-permissions) deseas asociar con tu nueva clave.

{% alert important %}
Ten en cuenta que después de crear una nueva clave de API, no puedes editar el alcance de permisos ni las IP permitidas. Esta limitación existe por razones de seguridad. Si necesitas cambiar el alcance de una clave, crea una nueva clave con los permisos actualizados e impleméntala en lugar de la anterior. Una vez que hayas completado tu implementación, puedes eliminar la clave anterior.
{% endalert %}

### Permisos de claves de REST API {#rest-api-key-permissions}

Los permisos de claves de API son permisos que puedes asignar a un usuario o grupo para limitar su acceso a ciertas llamadas de API. Para ver tu lista de permisos de claves de API, ve a **Configuración** > **API e identificadores** y selecciona tu clave de API.

{% tabs %}
{% tab Datos de usuario %}

| Permiso | Endpoint | Descripción |
|---|---|---|
| `users.track` | [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) | Registrar atributos de usuario, eventos personalizados y compras. |
| `users.delete` | [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) | Eliminar cualquier usuario. |
| `users.alias.new` | [`/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias) | Crear un nuevo alias para un usuario existente. |
| `users.identify` | [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) | Identificar un usuario de solo alias con un ID externo. |
| `users.export.ids` | [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) | Consultar información de perfil de usuario por ID de usuario. |
| `users.export.segment` | [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) | Consultar información de perfil de usuario por Segment. |
| `users.merge` | [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) | Fusionar dos usuarios existentes entre sí. |
| `users.external_ids.rename` | [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename) | Cambiar el ID externo de un usuario existente. |
| `users.external_ids.remove` | [`/users/external_ids/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove) | Eliminar el ID externo de un usuario existente. |
| `users.alias.update` | [`/users/alias/update`]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update) | Actualizar un alias para un usuario existente. |
| `users.export.global_control_group` | [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group) | Consultar información de perfil de usuario en el grupo de control global. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permisos de claves de REST API" }

 {% endtab %}
 {% tab Correo electrónico %}

| Permiso | Endpoint | Descripción |
|---|---|---|
| `email.unsubscribe` | [`/email/unsubscribes`]({{site.baseurl}}/api/endpoints/email/get_query_unsubscribed_email_addresses) | Consultar direcciones de correo electrónico canceladas. |
| `email.status` | [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status) | Cambiar el estado de la dirección de correo electrónico. |
| `email.hard_bounces` | [`/email/hard_bounces`]({{site.baseurl}}/api/endpoints/email/get_list_hard_bounces) | Consultar direcciones de correo electrónico con rebotes duros. |
| `email.bounce.remove` | [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces) | Eliminar direcciones de correo electrónico de tu lista de rebotes duros. |
| `email.spam.remove` | [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam) | Eliminar direcciones de correo electrónico de tu lista de correo no deseado. |
| `email.blacklist` | [`/email/blacklist`]({{site.baseurl}}/api/endpoints/email/post_blacklist) | Añadir direcciones de correo electrónico a la lista negra. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permisos de claves de REST API" }

{% endtab %}
{% tab Mensajes %}

| Permiso | Endpoint | Descripción |
|---|---|---|
| `messages.send` | [`/messages/send `]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) | Enviar un mensaje inmediato a usuarios específicos. |
| `messages.schedule.create` | [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages) | Programar un mensaje para enviarlo en un momento específico. |
| `messages.schedule.update` | [`/messages/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages) | Actualizar un mensaje programado. |
| `messages.schedule.delete` | [`/messages/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages) | Eliminar un mensaje programado. |
| `messages.schedule_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled) | Consultar todos los mensajes de difusión programados. |
| `messages.live_activity.update` | [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) | Actualizar una Live Activity de iOS. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permisos de claves de REST API" }

{% endtab %}
{% tab Campaigns %}

| Permiso | Endpoint | Descripción |
|---|---|---|
| `campaigns.trigger.send` | [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) | Desencadenar el envío de una Campaign existente. |
| `campaigns.trigger.schedule.create` | [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns) | Programar un envío de una Campaign con entrega desencadenada por API. |
| `campaigns.trigger.schedule.update` | [`/campaigns/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns) | Actualizar una Campaign programada con entrega desencadenada por API. |
| `campaigns.trigger.schedule.delete` | [`/campaigns/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages) | Eliminar una Campaign programada con entrega desencadenada por API. |
| `campaigns.list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | Consultar una lista de Campaigns. |
| `campaigns.data_series` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | Consultar análisis de Campaign en un rango de tiempo. |
| `campaigns.details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | Consultar detalles de una Campaign específica. |
| `sends.data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | Consultar análisis de envío de mensajes en un rango de tiempo. |
| `sends.id.create` | [`/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids) | Crear un ID de envío para el seguimiento de envíos masivos de mensajes. |
| `campaigns.url_info.details` | [`/campaigns/url_info/details`]({{site.baseurl}}) | Consultar detalles de URL de una variación de mensaje específica dentro de una Campaign. |
| `transactional.send` | [`/transactional/v1/campaigns/{campaign_id}/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message) | Permite enviar mensajería transaccional usando el endpoint de mensajería transaccional. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permisos de claves de REST API" }

{% endtab %}
{% tab Canvas %}

| Permiso | Endpoint | Descripción |
|---|---|---|
| `canvas.trigger.send` | [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) | Desencadenar el envío de un Canvas existente. |
| `canvas.trigger.schedule.create` | [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases) | Programar un envío de un Canvas con entrega desencadenada por API. |
| `canvas.trigger.schedule.update` | [`/canvas/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases) | Actualizar un Canvas programado con entrega desencadenada por API. |
| `canvas.trigger.schedule.delete` | [`/canvas/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases) | Eliminar un Canvas programado con entrega desencadenada por API. |
| `canvas.list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | Consultar una lista de Canvas. |
| `canvas.data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | Consultar análisis de Canvas en un rango de tiempo. |
| `canvas.details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | Consultar detalles de un Canvas específico. |
| `canvas.data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | Consultar resúmenes de análisis de Canvas en un rango de tiempo. |
| `canvas.url_info.details` | [`/canvas/url_info/details`]({{site.baseurl}}/get_canvas_link_alias) | Consultar detalles de URL de una variación de mensaje específica dentro de un paso en Canvas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permisos de claves de REST API" }

{% endtab %}
{% tab Segments %}

| Permiso | Endpoint | Descripción |
|---|---|---|
| `segments.list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | Consultar una lista de Segments. |
| `segments.data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | Consultar análisis de Segment en un rango de tiempo. |
| `segments.details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | Consultar detalles de un Segment específico. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permisos de claves de REST API" }

{% endtab %}
{% tab Compras %}

| Permiso | Endpoint | Descripción |
|---|---|---|
| `purchases.product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | Consultar una lista de productos comprados en tu aplicación. |
| `purchases.revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | Consultar el dinero total gastado por día en tu aplicación en un rango de tiempo. |
| `purchases.quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | Consultar el número total de compras por día en tu aplicación en un rango de tiempo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permisos de claves de REST API" }

{% endtab %}
{% tab Eventos %}

| Permiso | Endpoint | Descripción |
|---|---|---|
| `events.list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | Consultar una lista de eventos personalizados. |
| `events.data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | Consultar ocurrencias de un evento personalizado en un rango de tiempo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permisos de claves de REST API" }

{% endtab %}
{% tab Sesiones %}

| Permiso | Endpoint | Descripción |
|---|---|---|
| `sessions.data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | Consultar sesiones por día en un rango de tiempo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permisos de claves de REST API" }

{% endtab %}
{% tab KPIs %}

| Permiso | Endpoint | Descripción |
|---|---|---|
| `kpi.dau.data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | Consultar usuarios activos únicos por día en un rango de tiempo. |
| `kpi.mau.data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | Consultar el total de usuarios activos únicos en una ventana móvil de 30 días en un rango de tiempo. |
| `kpi.new_users.data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | Consultar nuevos usuarios por día en un rango de tiempo. |
| `kpi.uninstalls.data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | Consultar desinstalaciones de la aplicación por día en un rango de tiempo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permisos de claves de REST API" }

{% endtab %}
{% tab Plantillas %}

| Permiso | Endpoint | Descripción |
|---|---|---|
| `templates.email.create` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template) | Crear una nueva plantilla de correo electrónico en el panel. |
| `templates.email.info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | Consultar información de una plantilla específica. |
| `templates.email.list` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | Consultar una lista de plantillas de correo electrónico. |
| `templates.email.update` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template) | Actualizar una plantilla de correo electrónico almacenada en el panel. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permisos de claves de REST API" }

{% endtab %}
{% tab SSO %}

| Permiso | Descripción |
| --- | --- |
| `sso.saml.login` | Configurar el inicio de sesión iniciado por el proveedor de identidad. Para más información, consulta [Inicio de sesión iniciado por el proveedor de servicios (SP)]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Permisos de claves de REST API" }

{% endtab %}
{% tab Content Blocks %}

| Permiso | Endpoint | Descripción |
|---|---|---|
| `content_blocks.info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | Consultar información de una plantilla específica. |
| `content_blocks.list` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | Consultar una lista de Content Blocks. |
| `content_blocks.create` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block) | Crear un nuevo Content Block en el panel. |
| `content_blocks.update` | [`/content_blocks_update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block) | Actualizar un Content Block existente en el panel. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permisos de claves de REST API" }

{% endtab %}
{% tab Centro de preferencias %}

| Permiso | Endpoint | Descripción |
|---|---|---|
| `preference_center.get` | [`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | Obtener un centro de preferencias. |
| `preference_center.list` | [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center) | Listar centros de preferencias. |
| `preference_center.update` | [`/preference_center/v1`]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center)<br><br>[`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center) | Crear o actualizar un centro de preferencias. |
| `preference_center.user.get` | [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center) | Obtener un enlace de centro de preferencias para un usuario. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permisos de claves de REST API" }

{% endtab %}
{% tab Suscripción %}

| Permiso | Endpoint | Descripción |
|---|---|---|
| `subscription.status.set` | [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) | Establecer el estado del grupo de suscripción. |
| `subscription.status.get` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) | Obtener el estado del grupo de suscripción. |
| `subscription.groups.get` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) | Obtener el estado de los grupos de suscripción a los que usuarios específicos están explícitamente suscritos y cancelados. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permisos de claves de REST API" }

{% endtab %}
{% tab SMS %}

| Permiso | Endpoint | Descripción |
|---|---|---|
| `sms.invalid_phone_numbers` | [`/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers) | Consultar números de teléfono no válidos. |
| `sms.invalid_phone_numbers.remove` | [`/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers) | Eliminar la marca de número de teléfono no válido de los usuarios. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permisos de claves de REST API" }

{% endtab %}
{% tab Catálogos %}

| Permiso | Endpoint | Descripción |
|---|---|---|
| `catalogs.add_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk) | Añadir múltiples elementos a un catálogo existente. |
| `catalogs.update_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk) | Actualizar múltiples elementos en un catálogo existente. |
| `catalogs.delete_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk) | Eliminar múltiples elementos de un catálogo existente. |
| `catalogs.get_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | Obtener un solo elemento de un catálogo existente. |
| `catalogs.update_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item) | Actualizar un solo elemento en un catálogo existente. |
| `catalogs.create_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item) | Crear un solo elemento en un catálogo existente. |
| `catalogs.delete_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item) | Eliminar un solo elemento de un catálogo existente. |
| `catalogs.replace_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item) | Reemplazar un solo elemento de un catálogo existente. |
| `catalogs.create` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog) | Crear un catálogo. |
| `catalogs.get` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | Obtener una lista de catálogos. |
| `catalogs.delete` | [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog) | Eliminar un catálogo. |
| `catalogs.get_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | Obtener la vista previa de elementos de un catálogo existente. |
| `catalogs.replace_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items) | Reemplazar elementos en un catálogo existente. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permisos de claves de REST API" }

{% endtab %}
{% tab Autenticación del SDK %}

| Permiso | Endpoint | Descripción |
|---|---|---|
| `sdk_authentication.create` | [`/app_group/sdk_authentication/create`]({{site.baseurl}}/api/endpoints/sdk_authentication/post_create_sdk_authentication_key) | Crear una nueva clave de autenticación de SDK para tu aplicación. |
| `sdk_authentication.primary` | [`/app_group/sdk_authentication/primary`]({{site.baseurl}}/api/endpoints/sdk_authentication/put_primary_sdk_authentication_key) | Marcar una clave de autenticación de SDK como la clave principal para tu aplicación. |
| `sdk_authentication.delete` | [`/app_group/sdk_authentication/delete`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key) | Eliminar una clave de autenticación de SDK para tu aplicación. |
| `sdk_authentication.keys` | [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | Obtener todas las claves de autenticación de SDK para tu aplicación. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permisos de claves de REST API" }

{% endtab %}
{% endtabs %}

### Gestionar claves de REST API {#managing-rest-api-keys}

Puedes ver detalles o eliminar claves de REST API existentes desde **Configuración** > **API e identificadores** > pestaña **Claves de API**. Ten en cuenta que no puedes editar las claves de REST API después de crearlas.

La pestaña **Claves de API** incluye la siguiente información para cada clave:

| Campo | Descripción |
| ------------ | :------------------------------------------------------------------------------------------------------------------ |
| Nombre de la clave de API | El nombre dado a la clave al momento de su creación. |
| Identificador | La clave de API. |
| Creada por | La dirección de correo electrónico del usuario que creó la clave. Este campo muestra "N/A" para las claves creadas antes de junio de 2023. |
| Fecha de creación | La fecha en que se creó esta clave. |
| Último uso | La fecha en que se usó esta clave por última vez. Este campo muestra "N/A" para las claves que nunca se han utilizado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Gestionar claves de REST API" }

Para ver los detalles de una clave de API, pasa el cursor sobre la clave y selecciona <i class="fa-solid fa-eye" aria-label="Ver"></i> **Ver**. Esto incluye todos los permisos que tiene esta clave, las IP de la lista blanca (si las hay) y si esta clave está incluida en la lista blanca de IP de Braze.

![La lista de permisos de claves de API en el panel de Braze.]({% image_buster /assets/img_archive/view-api-key.png %})

Ten en cuenta que al [eliminar un usuario]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users), Braze no elimina las claves de API asociadas que ese usuario creó. Para eliminar una clave, pasa el cursor sobre la clave y selecciona <i class="fa-solid fa-trash-can" aria-label="Eliminar"></i> **Eliminar**.

![Una clave de API llamada "Último uso" con el icono de la papelera resaltado, mostrando "Eliminar".]({% image_buster /assets/img_archive/api-key-options.png %}){: style="max-width:30%;"}

### Seguridad de las claves de REST API {#rest-api-key-security}

Las claves de API se usan para autenticar una llamada a la API. Cuando creas una nueva clave de REST API, necesitas darle acceso a endpoints específicos. Al asignar permisos específicos a una clave de API, puedes limitar exactamente qué llamadas puede autenticar una clave de API.

Dado que las claves de REST API permiten el acceso a endpoints de REST API potencialmente sensibles, protege estas claves y compártelas solo con partners de confianza. Nunca deben exponerse públicamente. Por ejemplo, no uses esta clave para hacer llamadas AJAX desde tu sitio web ni la expongas de ninguna otra manera pública.

Una buena práctica de seguridad es asignar a un usuario solo el acceso necesario para completar su trabajo: este principio también puede aplicarse a las claves de API asignando permisos a cada clave. Estos permisos te brindan mejor seguridad y control sobre las diferentes áreas de tu cuenta.

{% alert warning %}
Dado que las claves de REST API permiten el acceso a endpoints de REST API potencialmente sensibles, asegúrate de que se almacenen y usen de forma segura. Por ejemplo, no uses esta clave para hacer llamadas AJAX desde tu sitio web ni la expongas de ninguna otra manera pública.
{% endalert %}

Si expones una clave accidentalmente, puedes eliminarla desde la consola para desarrolladores. Para obtener ayuda con este proceso, abre un [ticket de soporte]({{site.baseurl}}/user_guide/administer/personal/braze_support).

### Seguridad de las claves de REST API y las claves de API de SDK {#security-of-rest-api-keys-and-sdk-api-keys}

Las claves de REST API y las claves de API de SDK tienen perfiles de seguridad diferentes.

| | Claves de REST API | Claves de API de SDK |
|---|---|---|
| Propósito | Autenticación del lado del servidor para la REST API (envío de mensajes, exportación de datos, gestión de usuarios) | Identificación del lado del cliente para el SDK de Braze (ingesta de datos, mensajes dentro de la aplicación, Content Cards) |
| Visibilidad | **Deben permanecer privadas**. Nunca las expongas en código del lado del cliente, repositorios públicos ni aplicaciones de usuario. | Diseñadas para ser públicas. Se incluyen dentro del binario de tu aplicación o son visibles en el JavaScript del navegador web, similar a un ID de seguimiento de Google Analytics. |
| Solución si se exponen | Revoca la clave inmediatamente y crea un reemplazo en **Configuración** > **API e identificadores** > **Claves de API**. Una clave de REST API expuesta puede usarse para enviar mensajes, exportar datos de usuario o modificar la configuración de la cuenta. | No se requiere ninguna acción. Una clave de API de SDK solo puede ingestar datos y recuperar mensajería del lado del cliente (como mensajes dentro de la aplicación y Content Cards). No puede exportar datos de usuario, enviar mensajes en tu nombre ni modificar Campaigns. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Seguridad de las claves de REST API y las claves de API de SDK" }

### Lista de IP permitidas para la API {#api-ip-allowlisting}

Para mayor seguridad, puedes especificar una lista de direcciones IP y subredes que tienen permitido hacer solicitudes de REST API para una clave de REST API determinada. Esto se conoce como lista de permitidos o lista blanca. Para permitir direcciones IP o subredes específicas, agrégalas a la sección **IPs de la lista blanca** al crear una nueva clave de REST API:

![Opción para añadir IPs a la lista de permitidos al crear una clave de API.]({% image_buster /assets/img_archive/api-key-ip-whitelisting.png %})

Si no especificas ninguna, las solicitudes se pueden enviar desde cualquier dirección IP.

{% alert tip %}
Si estás haciendo un webhook de Braze a Braze y usas la lista de permitidos, consulta la lista de [IPs a incluir en la lista blanca]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook).
{% endalert %}

## Autenticación y seguridad de la API {#api-authentication-and-security}

### Autenticación con token Bearer {#bearer-token-authentication}

Braze autentica las solicitudes de la REST API usando la clave de API REST pasada como un token Bearer en el encabezado de solicitud `Authorization`. Cuando envías una solicitud, incluye tu clave de API en el siguiente formato:

```bash
Authorization: Bearer YOUR_REST_API_KEY
```

En cada solicitud, Braze realiza las siguientes comprobaciones de validación del lado del servidor:

1. **Validez del token:** Verifica que la clave de API REST existe en Braze y está activa (por ejemplo, que no ha sido revocada ni deshabilitada).
2. **Autorización del token:** Confirma que la clave de API tiene los permisos necesarios para el endpoint solicitado.

Si la autenticación falla, la API devuelve una respuesta de error con un código de estado HTTP. Por ejemplo, `401 Unauthorized` indica una clave inválida o ausente, mientras que `403 Forbidden` indica que la clave no tiene permiso para el endpoint solicitado. Para más información, consulta [Errores de la API]({{site.baseurl}}/api/errors).

### Uso de mayúsculas y minúsculas en los encabezados de solicitud {#header-casing}

Los nombres de los encabezados HTTP no distinguen entre mayúsculas y minúsculas, por lo que `Authorization` y `authorization` son equivalentes. Lo mismo aplica a otros encabezados de solicitud estándar, como `Content-Type`. Envía el formato de mayúsculas y minúsculas que produzca tu cliente HTTP.

Braze también acepta cualquier formato de mayúsculas y minúsculas del esquema `Bearer` (`Bearer`, `bearer` o `BEARER`). Envía la clave de API REST exactamente como fue emitida.

### Seguridad a nivel de red {#network-level-security}

Las solicitudes de la REST API a Braze están protegidas mediante cifrado Transport Layer Security (TLS) a lo largo de toda la ruta de la solicitud. La siguiente tabla describe el flujo de red de una solicitud de API desde tu servidor hasta Braze:

| Paso | Componente | Descripción |
| --- | --- | --- |
| 1 | Tu servidor | Inicia una solicitud HTTPS con cifrado TLS. |
| 2 | Cloudflare | Termina la conexión TLS del cliente y aplica protecciones a nivel de red. |
| 3 | Network Load Balancer (NLB) | Reenvía los paquetes a la infraestructura de la aplicación. Los NLB operan en la capa 4, lo que significa que no hay proxying en la capa 7. Los paquetes se reenvían sin inspección ni modificación a nivel HTTP. |
| 4 | NGINX ingress | Termina la conexión TLS interna y enruta la solicitud. |
| 5 | Unicorn (servidor de aplicaciones) | Procesa la solicitud autenticada. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Seguridad a nivel de red" }

El cifrado TLS cubre cada enlace de la cadena. Tu servidor se conecta a Cloudflare a través de TLS, y Cloudflare establece una conexión TLS separada a través del NLB hacia el NGINX ingress, de modo que tu clave de API y los datos de la solicitud permanecen cifrados en tránsito.

## Recursos adicionales {#additional-resources}

### Biblioteca cliente de Ruby {#ruby-client-library}

Si estás implementando Braze con Ruby, puedes usar la [biblioteca cliente de Ruby](https://github.com/braze-inc/braze-api-client-ruby) para reducir el tiempo de importación de datos. Una biblioteca cliente es una colección de código específica para un lenguaje de programación, en este caso Ruby, que facilita el uso de una API.

La biblioteca cliente de Ruby es compatible con los [endpoints de usuario]({{site.baseurl}}/api/endpoints/user_data).

{% alert important %}
Esta biblioteca cliente está en fase beta. Para ayudar a mejorar esta biblioteca, envía tus comentarios a [smb-product@braze.com](mailto:smb-product@braze.com).
{% endalert %}