# Funções do servidor Braze MCP {#braze-mcp-server-functions}

> O servidor Braze MCP expõe ferramentas de leitura e escrita que mapeiam para endpoints específicos da REST API da Braze. Para saber mais, veja [servidor Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Pré-requisitos {#prerequisites}

Antes de usar este recurso, você precisará [configurar o servidor Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## Funções de API da Braze disponíveis {#available-braze-api-functions}

Seu cliente MCP referencia essas ferramentas para interagir com o servidor Braze MCP.

### Espaços de trabalho {#workspaces}

| Ferramenta | Endpoint da API | Acesso | Descrição |
| --- | --- | --- | --- |
| `get_workspaces` | N/A | leitura | Descobre quais espaços de trabalho da Braze o token de acesso OAuth atual pode alcançar. Chame esta função primeiro: cada `id` de espaço de trabalho retornado é o `app_group_id` que todas as outras ferramentas exigem. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Espaços de trabalho" }

### Campaigns

| Ferramenta | Endpoint da API | Acesso | Descrição |
| --- | --- | --- | --- |
| `get_campaign_list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | leitura | Exporta uma lista de Campaigns com nome, identificador de API da Campaign, flag de API-campaign e tags. |
| `get_campaign_details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | leitura | Recupera informações relevantes sobre uma Campaign específica por `campaign_id`. |
| `get_campaign_dataseries` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | leitura | Série diária de estatísticas da Campaign ao longo do tempo (envios, aberturas, cliques, conversões por canal). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Campaigns" }

### Canvas {#canvases}

| Ferramenta | Endpoint da API | Acesso | Descrição |
| --- | --- | --- | --- |
| `get_canvas_list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | leitura | Exporta uma lista de Canvas com nome, identificador de API do Canvas e tags. |
| `get_canvas_details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | leitura | Exporta metadados do Canvas: nome, data de criação, status atual e mais. |
| `get_canvas_data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | leitura | Exporta dados de séries temporais para um Canvas. |
| `get_canvas_data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | leitura | Exporta resumos consolidados de dados de séries temporais do Canvas para um resumo conciso de resultados. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Canvas" }

### Catálogos {#catalogs}

| Ferramenta | Endpoint da API | Acesso | Descrição |
| --- | --- | --- | --- |
| `get_catalogs` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | leitura | Lista catálogos em um espaço de trabalho. |
| `get_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | leitura | Retorna vários itens de catálogo e seu conteúdo. |
| `get_catalog_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | leitura | Retorna um único item de catálogo e seu conteúdo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Catálogos" }

### Atributos personalizados {#custom-attributes}

| Ferramenta | Endpoint da API | Acesso | Descrição |
| --- | --- | --- | --- |
| `get_custom_attributes` | [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) | leitura | Exporta atributos personalizados registrados para seu app, em grupos de 50, em ordem alfabética. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Atributos personalizados" }

### Eventos personalizados {#custom-events}

| Ferramenta | Endpoint da API | Acesso | Descrição |
| --- | --- | --- | --- |
| `get_events` | [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) | leitura | Exporta eventos personalizados registrados para seu app, em grupos de 50, em ordem alfabética (paginação por cursor). |
| `get_events_list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | leitura | Exporta nomes de eventos personalizados, em grupos de 250, em ordem alfabética (paginação por página). |
| `get_events_data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | leitura | Ocorrências de um evento personalizado em um período de tempo designado. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Eventos personalizados" }

### Integrações CDI {#cdi-integrations}

| Ferramenta | Endpoint da API | Acesso | Descrição |
| --- | --- | --- | --- |
| `list_integrations` | [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | leitura | Lista integrações existentes de Cloud Data Ingestion, 10 por chamada. |
| `get_integration_job_sync_status` | [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | leitura | Status de sincronização anteriores para uma integração CDI específica, 10 por chamada. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Integrações CDI" }

### KPI

| Ferramenta | Endpoint da API | Acesso | Descrição |
| --- | --- | --- | --- |
| `get_dau_data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | leitura | Série diária de usuários ativos únicos por data. |
| `get_mau_data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | leitura | Série diária de usuários ativos únicos em uma janela móvel de 30 dias. |
| `get_new_users_data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | leitura | Série diária do total de novos usuários por data. |
| `get_uninstalls_data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | leitura | Série diária do total de desinstalações por data. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="KPI" }

### Biblioteca de mídia {#media-library}

| Ferramenta | Endpoint da API | Acesso | Descrição |
| --- | --- | --- | --- |
| `create_media_library_asset` | [`/media_library/create`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create) | criação | Faz upload de um ativo para a biblioteca de mídia da Braze por meio de URL externa ou conteúdo de arquivo em base64. Exatamente um modo de upload deve ser fornecido. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Biblioteca de mídia" }

### Mensagens {#messages}

| Ferramenta | Endpoint da API | Acesso | Descrição |
| --- | --- | --- | --- |
| `get_scheduled_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled) | leitura | Lista Campaigns e Canvas de entrada agendados entre agora e um `end_time` designado. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Mensagens" }

### Compras {#purchases}

| Ferramenta | Endpoint da API | Acesso | Descrição |
| --- | --- | --- | --- |
| `get_product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | leitura | Lista paginada de IDs de produtos. |
| `get_quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | leitura | Número total de compras no seu app em um intervalo de tempo. |
| `get_revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | leitura | Total de dinheiro gasto no seu app em um intervalo de tempo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Compras" }

### Autenticação do SDK {#sdk-authentication}

| Ferramenta | Endpoint da API | Acesso | Descrição |
| --- | --- | --- | --- |
| `get_sdk_authentication_keys` | [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | leitura | Recupera todas as chaves de autenticação do SDK para um app. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Autenticação do SDK" }

### Segments

| Ferramenta | Endpoint da API | Acesso | Descrição |
| --- | --- | --- | --- |
| `get_segment_list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | leitura | Exporta Segments com nome, identificador de API do Segment e flag de rastreamento de análise. |
| `get_segment_details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | leitura | Recupera informações relevantes sobre um Segment por `segment_id`. |
| `get_segment_data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | leitura | Série diária do tamanho estimado de um Segment ao longo do tempo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Segments" }

### Envios {#sends}

| Ferramenta | Endpoint da API | Acesso | Descrição |
| --- | --- | --- | --- |
| `get_send_data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | leitura | Estatísticas diárias para um `send_id` rastreado (Campaigns de API). A Braze armazena análises de envio por 14 dias após o envio. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Envios" }

### Sessões {#sessions}

| Ferramenta | Endpoint da API | Acesso | Descrição |
| --- | --- | --- | --- |
| `get_session_data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | leitura | Número de sessões do seu app em um período de tempo designado. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Sessões" }

### Grupos de inscrições {#subscription-groups}

| Ferramenta | Endpoint da API | Acesso | Descrição |
| --- | --- | --- | --- |
| `get_subscription_group_status` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) | leitura | Estado da inscrição de um usuário em um grupo de inscrições. |
| `get_user_subscription_groups` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) | leitura | Lista os grupos de inscrições de um usuário. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Grupos de inscrições" }

### Modelos {#templates}

| Ferramenta | Endpoint da API | Acesso | Descrição |
| --- | --- | --- | --- |
| `get_email_templates` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | leitura | Lista modelos de e-mail disponíveis na sua conta da Braze. |
| `get_email_template_info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | leitura | Obtém informações sobre um modelo de e-mail específico. Modelos do editor de arrastar e soltar não são aceitos. |
| `create_email_template` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template) | criação | Cria um modelo de e-mail no dashboard da Braze. |
| `update_email_template` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template) | atualização | Atualiza um modelo de e-mail existente. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Modelos" }

### Content Blocks

| Ferramenta | Endpoint da API | Acesso | Descrição |
| --- | --- | --- | --- |
| `get_content_blocks` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | leitura | Lista informações de Content Blocks existentes. |
| `get_content_block_info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | leitura | Obtém informações sobre um Content Block existente, opcionalmente com dados de inclusão em Campaigns ou Canvas. |
| `create_content_block` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block) | criação | Cria um Content Block. |
| `update_content_block` | [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block) | atualização | Atualiza um Content Block. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Content Blocks" }

{% multi_lang_include mcp_server/legal_disclaimer.md %}