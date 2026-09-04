# Funciones del servidor MCP de Braze {#braze-mcp-server-functions}

> El servidor MCP de Braze expone herramientas de lectura y escritura que se corresponden con endpoints específicos de la REST API de Braze. Para más información, consulta [Servidor MCP de Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

{% alert note %}
El servidor MCP de Braze incluye herramientas que solo están disponibles para los clientes que participan en programas beta. Si intentas acceder a una herramienta que forma parte de un programa beta y tu cuenta no tiene la característica habilitada, es posible que recibas una respuesta de error. Para unirte a un programa beta, ponte en contacto con tu director de cuentas.
{% endalert %}

## Requisitos previos {#prerequisites}

Antes de poder usar esta característica, necesitarás [configurar el servidor MCP de Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## Funciones API disponibles en Braze {#available-braze-api-functions}

Tu cliente MCP hace referencia a estas herramientas para interactuar con el servidor MCP de Braze.

### Espacios de trabajo {#workspaces}

| Herramienta | Endpoint de API | Acceso | Descripción |
| --- | --- | --- | --- |
| `get_workspaces` | N/A | lectura | Descubre a qué espacios de trabajo de Braze puede acceder el token de acceso OAuth actual. Llama a esta herramienta primero: cada `id` de espacio de trabajo devuelto es el `app_group_id` que requieren todas las demás herramientas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Espacios de trabajo" }

### Campaigns

| Herramienta | Endpoint de API | Acceso | Descripción |
| --- | --- | --- | --- |
| `get_campaign_list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | lectura | Exporta una lista de Campaigns con nombre, identificador de API de la campaña, indicador de campaña API y etiquetas. |
| `get_campaign_details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | lectura | Recupera información relevante sobre una campaña especificada mediante `campaign_id`. |
| `get_campaign_dataseries` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | lectura | Series diarias de estadísticas de campaña a lo largo del tiempo (envíos, aperturas, clics, conversiones por canal). |
| `duplicate_campaign` | [`/campaigns/duplicate`]({{site.baseurl}}/api/endpoints/messaging/duplicate_messages/post_duplicate_campaigns) | creación | Duplica una campaña existente. |
| `create_campaign`<sup>*</sup> | N/A | creación | Crea una nueva campaña. |
| `edit_campaign`<sup>*</sup> | N/A | actualización | Edita una campaña existente. |
| `launch_campaign`<sup>*</sup> | N/A | actualización | Lanza una campaña. |
| `stop_campaign`<sup>*</sup> | N/A | actualización | Detiene una campaña en ejecución. |
| `archive_campaign`<sup>*</sup> | N/A | actualización | Archiva una campaña. |
| `unarchive_campaign`<sup>*</sup> | N/A | actualización | Desarchiva una campaña. |
| `get_campaign_draft`<sup>*</sup> | N/A | lectura | Recupera los detalles de un borrador de campaña. |
| `get_campaign_live_details`<sup>*</sup> | N/A | lectura | Recupera los detalles de una campaña en vivo. |
| `create_campaign_message`<sup>*</sup> | N/A | creación | Crea un mensaje dentro de una campaña. |
| `update_campaign_message`<sup>*</sup> | N/A | actualización | Actualiza un mensaje de campaña. |
| `delete_campaign_message`<sup>*</sup> | N/A | eliminación | Elimina un mensaje de campaña. |
| `create_campaign_message_variation`<sup>*</sup> | N/A | creación | Crea una variación de mensaje dentro de una campaña. |
| `update_campaign_message_variation`<sup>*</sup> | N/A | actualización | Actualiza una variación de mensaje de campaña. |
| `delete_campaign_message_variation`<sup>*</sup> | N/A | eliminación | Elimina una variación de mensaje de campaña. |
| `update_campaign_distribution`<sup>*</sup> | N/A | actualización | Actualiza la configuración de distribución de una campaña. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Campaigns" }

<sup>*</sup> Esta herramienta solo está disponible para los clientes que participan en el programa beta de API de Campaigns. Si tu cuenta no tiene esta característica habilitada, es posible que recibas un error al intentar usarla. Para unirte al programa beta, contacta a tu director de cuentas.
{: .reset-td-br-1 }

### Canvas {#canvases}

| Herramienta | Endpoint de API | Acceso | Descripción |
| --- | --- | --- | --- |
| `get_canvas_list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | lectura | Exporta una lista de Canvas con nombre, identificador de API de Canvas y etiquetas. |
| `get_canvas_details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | lectura | Exporta metadatos de Canvas: nombre, fecha de creación, estado actual y más. |
| `get_canvas_data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | lectura | Exporta datos de series temporales para un Canvas. |
| `get_canvas_data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | lectura | Exporta resúmenes agregados de datos de series temporales de Canvas para un resumen conciso de resultados. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Canvas" }

### Catálogos {#catalogs}

| Herramienta | Endpoint de API | Acceso | Descripción |
| --- | --- | --- | --- |
| `get_catalogs` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | lectura | Lista los catálogos en un espacio de trabajo. |
| `get_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | lectura | Devuelve múltiples elementos del catálogo y su contenido. |
| `get_catalog_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | lectura | Devuelve un único elemento del catálogo y su contenido. |
| `create_catalog` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog) | creación | Crea un catálogo. |
| `delete_catalog` | [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog) | eliminación | Elimina un catálogo. |
| `create_catalog_fields` | [`/catalogs/{catalog_name}/fields`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields) | creación | Crea múltiples campos en un catálogo. |
| `delete_catalog_field` | [`/catalogs/{catalog_name}/fields/{field_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field) | eliminación | Elimina un campo de catálogo. |
| `create_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk) | creación | Crea múltiples elementos en un catálogo. Hasta 50 elementos por solicitud. |
| `edit_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk) | actualización | Edita múltiples elementos existentes en un catálogo. Hasta 50 elementos por solicitud. |
| `replace_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items) | actualización | Reemplaza múltiples elementos en un catálogo. Crea los elementos si no existen. Hasta 50 elementos por solicitud. |
| `delete_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk) | eliminación | Elimina múltiples elementos en un catálogo. Hasta 50 elementos por solicitud. |
| `create_catalog_selection` | [`/catalogs/{catalog_name}/selections`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections) | creación | Crea una selección en un catálogo. |
| `delete_catalog_selection` | [`/catalogs/{catalog_name}/selections/{selection_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection) | eliminación | Elimina una selección de catálogo. |
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
| `get_events_list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | lectura | Exporta los nombres de eventos personalizados, en grupos de 250, en orden alfabético (paginación por página). |
| `get_events_data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | lectura | Ocurrencias de un evento personalizado durante un período de tiempo designado. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Eventos personalizados" }

### Integraciones CDI {#cdi-integrations}

| Herramienta | Endpoint de API | Acceso | Descripción |
| --- | --- | --- | --- |
| `list_integrations` | [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | lectura | Lista las integraciones de ingesta de datos en la nube existentes, 10 por llamada. |
| `get_integration_job_sync_status` | [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | lectura | Estados de sincronización anteriores para una integración CDI determinada, 10 por llamada. |
| `trigger_integration_sync` | [`/cdi/integrations/{integration_id}/sync`]({{site.baseurl}}/api/endpoints/cdi/post_job_sync) | escritura | Desencadena una sincronización para una integración CDI determinada. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Integraciones CDI" }

### indicador clave de rendimiento

| Herramienta | Endpoint de API | Acceso | Descripción |
| --- | --- | --- | --- |
| `get_dau_data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | lectura | Serie diaria de usuarios activos únicos por fecha. |
| `get_mau_data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | lectura | Serie diaria de usuarios activos únicos en una ventana móvil de 30 días. |
| `get_new_users_data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | lectura | Serie diaria del total de nuevos usuarios por fecha. |
| `get_uninstalls_data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | lectura | Serie diaria del total de desinstalaciones por fecha. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="indicador clave de rendimiento" }

### Biblioteca de medios {#media-library}

| Herramienta | Endpoint de API | Acceso | Descripción |
| --- | --- | --- | --- |
| `create_media_library_asset` | [`/media_library/create`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create) | creación | Sube un activo a la biblioteca de medios de Braze mediante una URL externa o contenido de archivo en base64. Se debe proporcionar exactamente un modo de carga. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Biblioteca de medios" }

### Compras {#purchases}

| Herramienta | Endpoint de API | Acceso | Descripción |
| --- | --- | --- | --- |
| `get_product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | lectura | Lista paginada de ID de productos. |
| `get_quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | lectura | Número total de compras en tu aplicación durante un rango de tiempo. |
| `get_revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | lectura | Total de dinero gastado en tu aplicación durante un rango de tiempo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Compras" }

### Segments

| Herramienta | Endpoint de API | Acceso | Descripción |
| --- | --- | --- | --- |
| `get_segment_list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | lectura | Exporta Segments con nombre, identificador de API de Segment e indicador de seguimiento de análisis. |
| `get_segment_details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | lectura | Recupera información relevante sobre un Segment mediante `segment_id`. |
| `get_segment_data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | lectura | Serie diaria del tamaño estimado de un Segment a lo largo del tiempo. |
| `get_segment_filters`<sup>*</sup> | N/A | lectura | Recupera las definiciones de filtros de Segment. |
| `create_segment`<sup>*</sup> | N/A | creación | Crea un nuevo Segment. |
| `edit_segment`<sup>*</sup> | N/A | actualización | Edita un Segment existente. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Segments" }

<sup>*</sup> Esta herramienta solo está disponible para los clientes que participan en el programa beta de API de Segments. Si tu cuenta no tiene esta característica habilitada, es posible que recibas un error al intentar usarla. Para unirte al programa beta, contacta a tu director de cuentas.
{: .reset-td-br-1 }

### Envíos {#sends}

| Herramienta | Endpoint de API | Acceso | Descripción |
| --- | --- | --- | --- |
| `get_send_data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | lectura | Estadísticas diarias para un `send_id` con seguimiento (Campaigns de API). Braze almacena los análisis de envío durante 14 días después del envío. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Envíos" }

### Sesiones {#sessions}

| Herramienta | Endpoint de API | Acceso | Descripción |
| --- | --- | --- | --- |
| `get_session_data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | lectura | Número de sesiones de tu aplicación durante un período de tiempo designado. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Sesiones" }

### Plantillas {#templates}

| Herramienta | Endpoint de API | Acceso | Descripción |
| --- | --- | --- | --- |
| `get_email_templates` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | lectura | Lista las plantillas de correo electrónico disponibles en tu cuenta de Braze. |
| `get_email_template_info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | lectura | Obtiene información de una plantilla de correo electrónico específica. Las plantillas del editor de arrastrar y soltar no se aceptan. |
| `create_email_template` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template) | creación | Crea una plantilla de correo electrónico en el panel de Braze. |
| `update_email_template` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template) | actualización | Actualiza una plantilla de correo electrónico existente. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Plantillas" }

### Content Blocks

| Herramienta | Endpoint de API | Acceso | Descripción |
| --- | --- | --- | --- |
| `get_content_blocks` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | lectura | Lista información de los bloques de contenido existentes. |
| `get_content_block_info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | lectura | Obtiene información de un bloque de contenido existente, opcionalmente con datos de inclusión en Campaigns o Canvas. |
| `create_content_block` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block) | creación | Crea un bloque de contenido. |
| `update_content_block` | [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block) | actualización | Actualiza un bloque de contenido. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Content Blocks" }

### Operator

| Herramienta | Endpoint de API | Acceso | Descripción |
| --- | --- | --- | --- |
| `send_operator_prompt` | N/A | actualización | Envía un prompt en lenguaje natural a BrazeAI Operator. Envía un trabajo en segundo plano y devuelve un job_id. |
| `get_operator_result` | N/A | lectura | Consulta el resultado de un trabajo de Operator enviado mediante su job_id. |
| `cancel_operator_job` | N/A | actualización | Cancela un trabajo de Operator en ejecución. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Operator" }

{% alert important %}
Estas herramientas solo están disponibles para los clientes que participan en el programa beta de Operator. Si tu cuenta no tiene esta característica habilitada, es posible que recibas un error al intentar usarla. Para unirte al programa beta, contacta a tu director de cuentas.
{% endalert %}

{% multi_lang_include mcp_server/legal_disclaimer.md %}