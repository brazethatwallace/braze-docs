# Funciones del servidor MCP de Braze {#braze-mcp-server-functions}

> El servidor MCP de Braze expone herramientas de lectura y escritura que se corresponden con endpoints específicos de la REST API de Braze. Para más información, consulta [Servidor MCP de Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Requisitos previos {#prerequisites}

Antes de poder utilizar esta característica, tendrás que [configurar el servidor MCP de Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## Funciones disponibles de la API de Braze {#available-braze-api-functions}

Tu cliente MCP hace referencia a estas herramientas para interactuar con el servidor MCP de Braze.

### Espacios de trabajo {#workspaces}

| Herramienta | Endpoint de API | Acceso | Descripción |
| --- | --- | --- | --- |
| `get_workspaces` | N/A | lectura | Descubre a qué espacios de trabajo de Braze puede acceder el token de acceso OAuth actual. Llama a esta función primero: cada `id` de espacio de trabajo devuelto es el `app_group_id` que requieren todas las demás herramientas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Espacios de trabajo" }

### Campaigns

| Herramienta | Endpoint de API | Acceso | Descripción |
| --- | --- | --- | --- |
| `get_campaign_list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | lectura | Exporta una lista de Campaigns con nombre, identificador de API de la campaña, indicador de API-campaign y etiquetas. |
| `get_campaign_details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | lectura | Recupera información relevante sobre una Campaign específica mediante `campaign_id`. |
| `get_campaign_dataseries` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | lectura | Serie diaria de estadísticas de Campaigns a lo largo del tiempo (envíos, aperturas, clics, conversiones por canal). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Campaigns" }

### Canvas {#canvases}

| Herramienta | Endpoint de API | Acceso | Descripción |
| --- | --- | --- | --- |
| `get_canvas_list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | lectura | Exporta una lista de Canvas con nombre, identificador de API de Canvas y etiquetas. |
| `get_canvas_details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | lectura | Exporta metadatos de Canvas: nombre, fecha de creación, estado actual y más. |
| `get_canvas_data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | lectura | Exporta datos de series temporales para un Canvas. |
| `get_canvas_data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | lectura | Exporta resúmenes acumulados de datos de series temporales de Canvas para un resumen conciso de resultados. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Canvas" }

### Catálogos {#catalogs}

| Herramienta | Endpoint de API | Acceso | Descripción |
| --- | --- | --- | --- |
| `get_catalogs` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | lectura | Lista los catálogos en un espacio de trabajo. |
| `get_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | lectura | Devuelve varios elementos del catálogo y su contenido. |
| `get_catalog_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | lectura | Devuelve un único elemento del catálogo y su contenido. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Catálogos" }

### Atributos personalizados {#custom-attributes}

| Herramienta | Endpoint de API | Acceso | Descripción |
| --- | --- | --- | --- |
| `get_custom_attributes` | [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) | lectura | Exporta los atributos personalizados registrados para tu aplicación, en grupos de 50, en orden alfabético. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Atributos personalizados" }

### Eventos personalizados {#custom-events}

| Herramienta | Endpoint de API | Acceso | Descripción |
| --- | --- | --- | --- |
| `get_events` | [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) | lectura | Exporta los eventos personalizados registrados para tu aplicación, en grupos de 50, en orden alfabético (paginación por cursor). |
| `get_events_list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | lectura | Exporta nombres de eventos personalizados, en grupos de 250, en orden alfabético (paginación por página). |
| `get_events_data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | lectura | Ocurrencias de un evento personalizado durante un periodo de tiempo designado. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Eventos personalizados" }

### Integraciones CDI {#cdi-integrations}

| Herramienta | Endpoint de API | Acceso | Descripción |
| --- | --- | --- | --- |
| `list_integrations` | [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | lectura | Lista las integraciones existentes de Cloud Data Ingestion, 10 por llamada. |
| `get_integration_job_sync_status` | [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | lectura | Estados de sincronización anteriores para una integración CDI determinada, 10 por llamada. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Integraciones CDI" }

### KPI

| Herramienta | Endpoint de API | Acceso | Descripción |
| --- | --- | --- | --- |
| `get_dau_data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | lectura | Serie diaria de usuarios activos únicos por fecha. |
| `get_mau_data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | lectura | Serie diaria de usuarios activos únicos en una ventana móvil de 30 días. |
| `get_new_users_data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | lectura | Serie diaria del total de nuevos usuarios por fecha. |
| `get_uninstalls_data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | lectura | Serie diaria del total de desinstalaciones por fecha. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="KPI" }

### Biblioteca de medios {#media-library}

| Herramienta | Endpoint de API | Acceso | Descripción |
| --- | --- | --- | --- |
| `create_media_library_asset` | [`/media_library/create`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create) | creación | Carga un activo a la biblioteca de medios de Braze mediante una URL externa o contenido de archivo en base64. Se debe proporcionar exactamente un modo de carga. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Biblioteca de medios" }

### Mensajes {#messages}

| Herramienta | Endpoint de API | Acceso | Descripción |
| --- | --- | --- | --- |
| `get_scheduled_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled) | lectura | Lista las Campaigns programadas y los Canvas de entrada entre el momento actual y un `end_time` designado. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Mensajes" }

### Compras {#purchases}

| Herramienta | Endpoint de API | Acceso | Descripción |
| --- | --- | --- | --- |
| `get_product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | lectura | Lista paginada de ID de productos. |
| `get_quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | lectura | Número total de compras en tu aplicación durante un rango de tiempo. |
| `get_revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | lectura | Total de dinero gastado en tu aplicación durante un rango de tiempo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Compras" }

### Autenticación SDK {#sdk-authentication}

| Herramienta | Endpoint de API | Acceso | Descripción |
| --- | --- | --- | --- |
| `get_sdk_authentication_keys` | [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | lectura | Recupera todas las claves de autenticación SDK para una aplicación. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Autenticación SDK" }

### Segments

| Herramienta | Endpoint de API | Acceso | Descripción |
| --- | --- | --- | --- |
| `get_segment_list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | lectura | Exporta Segments con nombre, identificador de API de Segment e indicador de seguimiento de análisis. |
| `get_segment_details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | lectura | Recupera información relevante sobre un Segment mediante `segment_id`. |
| `get_segment_data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | lectura | Serie diaria del tamaño estimado de un Segment a lo largo del tiempo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Segments" }

### Envíos {#sends}

| Herramienta | Endpoint de API | Acceso | Descripción |
| --- | --- | --- | --- |
| `get_send_data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | lectura | Estadísticas diarias para un `send_id` con seguimiento (Campaigns de API). Braze almacena los análisis de envío durante 14 días después del envío. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Envíos" }

### Sesiones {#sessions}

| Herramienta | Endpoint de API | Acceso | Descripción |
| --- | --- | --- | --- |
| `get_session_data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | lectura | Número de sesiones de tu aplicación durante un periodo de tiempo designado. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Sesiones" }

### Grupos de suscripción {#subscription-groups}

| Herramienta | Endpoint de API | Acceso | Descripción |
| --- | --- | --- | --- |
| `get_subscription_group_status` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) | lectura | Estado de suscripción de un usuario en un grupo de suscripción. |
| `get_user_subscription_groups` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) | lectura | Lista los grupos de suscripción de un usuario. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Grupos de suscripción" }

### Plantillas {#templates}

| Herramienta | Endpoint de API | Acceso | Descripción |
| --- | --- | --- | --- |
| `get_email_templates` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | lectura | Lista las plantillas de correo electrónico disponibles en tu cuenta de Braze. |
| `get_email_template_info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | lectura | Obtén información sobre una plantilla de correo electrónico específica. No se aceptan plantillas del editor de arrastrar y soltar. |
| `create_email_template` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template) | creación | Crea una plantilla de correo electrónico en el panel de Braze. |
| `update_email_template` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template) | actualización | Actualiza una plantilla de correo electrónico existente. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Plantillas" }

### Content Blocks

| Herramienta | Endpoint de API | Acceso | Descripción |
| --- | --- | --- | --- |
| `get_content_blocks` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | lectura | Lista la información de los bloques de contenido existentes. |
| `get_content_block_info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | lectura | Obtén información sobre un bloque de contenido existente, opcionalmente con datos de inclusión en Campaigns o Canvas. |
| `create_content_block` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block) | creación | Crea un bloque de contenido. |
| `update_content_block` | [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block) | actualización | Actualiza un bloque de contenido. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Content Blocks" }

{% multi_lang_include mcp_server/legal_disclaimer.md %}