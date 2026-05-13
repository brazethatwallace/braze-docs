# Funciones del servidor MCP de Braze {#braze-mcp-server-functions}

> El servidor MCP de Braze expone un conjunto de funciones API que se corresponden con puntos finales específicos de la REST API de Braze. Los clientes MCP como Claude y Cursor pueden llamar a estas funciones para recuperar datos sin PII y, con los permisos adecuados, realizar acciones de escritura sin PII. Para obtener información más general, consulta [Servidor MCP de Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Requisitos previos {#prerequisites}

Antes de poder utilizar esta característica, tendrás que [configurar el servidor MCP de Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## Funciones disponibles de la API de Braze {#available-braze-api-functions}

Tu cliente MCP hace referencia a las siguientes funciones API para interactuar con el servidor MCP de Braze.

### Funciones generales {#general-functions}

Estas funciones ayudan a tu cliente MCP a descubrir y ejecutar las funciones disponibles de la API de Braze.

| Función | Descripción |
|----------|-------------|
| `list_functions` | Enumera todas las funciones disponibles de la API de Braze con sus descripciones y parámetros. |
| `call_function` | Llama a una función específica de solo lectura de la API de Braze con los parámetros proporcionados. |
| `call_write_function` | Llama a una función específica de escritura de la API de Braze con los parámetros proporcionados. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="General functions" }

### Campaigns

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `get_campaign_list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) | Exporta una lista de Campaigns con metadatos. |
| `get_campaign_details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) | Obtén información detallada sobre Campaigns específicas. |
| `get_campaign_dataseries` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) | Recupera datos de análisis de series temporales para Campaigns. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Campaigns" }

### Canvas {#canvases}

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `get_canvas_list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) | Exporta una lista de Canvas con metadatos. |
| `get_canvas_details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) | Obtén información detallada sobre Canvas específicos. |
| `get_canvas_data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/) | Obtén análisis resumidos del rendimiento de Canvas. |
| `get_canvas_data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) | Recupera datos de análisis de series temporales para Canvas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Canvases" }

### Catálogos {#catalogs}

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `get_catalogs` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) | Devuelve una lista de catálogos en un espacio de trabajo. |
| `get_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/) | Devuelve varios elementos del catálogo y su contenido con soporte para paginación. |
| `get_catalog_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/) | Devuelve un elemento específico del catálogo y su contenido por ID. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Catalogs" }

### Ingesta de datos de Cloud {#cloud-data-ingestion}

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `list_integrations` | [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list/) | Devuelve una lista de integraciones CDI existentes. |
| `get_integration_job_sync_status` | [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status/) | Devuelve los estados de sincronización anteriores para una integración CDI determinada. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Cloud Data Ingestion" }

### Content Blocks

Las funciones `create_content_block` y `update_content_block` son funciones de escritura. Tu cliente MCP debe llamarlas con `call_write_function`, y tu clave de API debe tener el permiso correspondiente `content_blocks.create` o `content_blocks.update`.

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `get_content_blocks_list` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) | Enumera los bloques de contenido disponibles. |
| `get_content_blocks_info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) | Obtén información sobre tus bloques de contenido. |
| `create_content_block` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/) | Crea un bloque de contenido. Requiere `name` y `content`. Los campos opcionales son `description`, `state` (debe ser `active` o `draft`) y `tags`. |
| `update_content_block` | [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) | Actualiza un bloque de contenido existente. Requiere `content_block_id` y al menos un campo actualizable: `name`, `content`, `description`, `state` (debe ser `active` o `draft`) o `tags`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Content Blocks" }

### Atributos personalizados {#custom-attributes}

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `get_custom_attributes` | [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes/) | Exporta los atributos personalizados registrados para tu aplicación. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Custom Attributes" }

### Eventos {#events}

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `get_events_list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/) | Exporta una lista de eventos personalizados registrados para tu aplicación. |
| `get_events_data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/) | Recupera datos de series temporales para eventos personalizados. |
| `get_events` | [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data/) | Obtén datos detallados sobre los eventos con soporte para paginación. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Events" }

### KPI {#kpis}

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `get_new_users_data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/) | Serie diaria de recuentos de nuevos usuarios. |
| `get_dau_data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/) | Datos de series temporales de usuarios activos diarios. |
| `get_mau_data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/) | Datos de series temporales de usuarios activos al mes. |
| `get_uninstalls_data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/) | Datos de series temporales de desinstalaciones de la aplicación. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="KPIs" }

### Biblioteca de medios {#media-library}

La función `create_media_library_asset` es una función de escritura. Tu cliente MCP debe llamarla con `call_write_function`, y tu clave de API debe tener el permiso `media_library.create`.

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `create_media_library_asset` | [`/media_library/create`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create/) | Carga un activo a tu biblioteca de medios de Braze. Puedes proporcionar una URL de acceso público (`asset_url`) o un archivo codificado en base64 (`asset_file_base64`), pero no ambos. Las imágenes tienen un límite de tamaño de 5 MB. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Media Library" }

### Mensajes {#messages}

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `get_scheduled_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/) | Enumera las próximas Campaigns y Canvas programados. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Messages" }

### Centros de preferencias {#preference-centers}

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `get_preference_centers` | [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/) | Enumera los centros de preferencias disponibles. |
| `get_preference_center_details` | [`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/) | Muestra los detalles de un centro de preferencias específico, incluido el contenido HTML y las opciones. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Preference Centers" }

### Compras {#purchases}

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `get_product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) | Exporta una lista paginada de ID de productos. |
| `get_revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series/) | Datos de series temporales de análisis de ingresos. |
| `get_quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases/) | Datos de series temporales de cantidades de compras. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Purchases" }

### Segments

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `get_segment_list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) | Exporta una lista de Segments con el estado de seguimiento de análisis. |
| `get_segment_data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/) | Datos de análisis de series temporales para Segments. |
| `get_segment_details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/) | Información detallada sobre Segments específicos. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Segments" }

### Envíos {#sends}

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `get_send_data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) | Análisis diarios de los envíos de Campaigns con seguimiento. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Sends" }

### Sesiones {#sessions}

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `get_session_data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/) | Datos de series temporales del recuento de sesiones de la aplicación. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Sessions" }

### Claves de Autenticación SDK {#sdk-authentication-keys}

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `get_sdk_authentication_keys` | [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys/) | Enumera todas las claves de Autenticación SDK para tu aplicación. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SDK Authentication Keys" }

### Suscripción {#subscription}

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `get_user_subscription_groups` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) | Enumera y obtiene los grupos de suscripción de un usuario determinado. |
| `get_subscription_group_status` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) | Obtiene el estado de suscripción de un usuario en un grupo de suscripción. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Subscription" }

### Plantillas {#templates}

Las funciones `create_email_template` y `update_email_template` son funciones de escritura. Tu cliente MCP debe llamarlas con `call_write_function`, y tu clave de API debe tener el permiso correspondiente `templates.email.create` o `templates.email.update`.

| Función | Punto de conexión | Descripción |
|----------|----------|-------------|
| `get_email_templates_list` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) | Enumera las plantillas de correo electrónico disponibles. |
| `get_email_template_info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | Obtén información sobre tus plantillas de correo electrónico. |
| `create_email_template` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/) | Crea una plantilla de correo electrónico. Requiere `template_name`, `subject` y `body`. Los campos opcionales son `plaintext_body`, `preheader`, `tags` y `should_inline_css`. |
| `update_email_template` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/) | Actualiza una plantilla de correo electrónico existente. Requiere `email_template_id` y al menos un campo actualizable: `template_name`, `subject`, `body`, `plaintext_body`, `preheader`, `tags` o `should_inline_css`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Templates" }

{% multi_lang_include mcp_server/legal_disclaimer.md %}