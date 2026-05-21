# Funções do servidor Braze MCP {#braze-mcp-server-functions}

> O servidor Braze MCP expõe um conjunto de funções de API que mapeiam para endpoints específicos da REST API da Braze. Clientes MCP como Claude e Cursor podem chamar essas funções para recuperar dados sem IPI e, com as permissões adequadas, realizar ações de escrita sem IPI. Para mais informações gerais, veja [servidor Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Pré-requisitos {#prerequisites}

Antes de usar este recurso, você precisará [configurar o servidor Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## Funções de API da Braze disponíveis {#available-braze-api-functions}

Seu cliente MCP referencia as seguintes funções de API para interagir com o servidor Braze MCP.

### Funções gerais {#general-functions}

Essas funções ajudam seu cliente MCP a descobrir e executar as funções de API da Braze disponíveis.

| Função | Descrição |
|----------|-------------|
| `list_functions` | Lista todas as funções de API da Braze disponíveis com suas descrições e parâmetros. |
| `call_function` | Chama uma função específica de API da Braze somente leitura com os parâmetros fornecidos. |
| `call_write_function` | Chama uma função específica de API da Braze com capacidade de escrita com os parâmetros fornecidos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="General functions" }

### Campaigns

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `get_campaign_list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) | Exporta uma lista de Campaigns com metadados. |
| `get_campaign_details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) | Obtém informações detalhadas sobre Campaigns específicas. |
| `get_campaign_dataseries` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) | Recupera dados de análise de séries temporais para Campaigns. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Campaigns" }

### Canvas {#canvases}

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `get_canvas_list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) | Exporta uma lista de Canvas com metadados. |
| `get_canvas_details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) | Obtém informações detalhadas sobre Canvas específicos. |
| `get_canvas_data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/) | Obtém análises resumidas para o desempenho do Canvas. |
| `get_canvas_data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) | Recupera dados de análise de séries temporais para Canvas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Canvases" }

### Catálogos {#catalogs}

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `get_catalogs` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) | Retorna uma lista de catálogos em um espaço de trabalho. |
| `get_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/) | Retorna vários itens de catálogo e seu conteúdo com suporte à paginação. |
| `get_catalog_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/) | Retorna um item de catálogo específico e seu conteúdo por ID. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Catalogs" }

### Ingestão de dados na nuvem {#cloud-data-ingestion}

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `list_integrations` | [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list/) | Retorna uma lista de integrações CDI existentes. |
| `get_integration_job_sync_status` | [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status/) | Retorna os status de sincronização anteriores para uma integração CDI específica. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Cloud Data Ingestion" }

### Content Blocks

As funções `create_content_block` e `update_content_block` são funções de escrita. Seu cliente MCP deve chamá-las com `call_write_function`, e sua chave de API deve ter a permissão correspondente `content_blocks.create` ou `content_blocks.update`.

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `get_content_blocks_list` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) | Lista seus blocos de conteúdo disponíveis. |
| `get_content_blocks_info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) | Obtém informações sobre seus blocos de conteúdo. |
| `create_content_block` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/) | Cria um bloco de conteúdo. Requer `name` e `content`. Campos opcionais são `description`, `state` (deve ser `active` ou `draft`) e `tags`. |
| `update_content_block` | [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) | Atualiza um bloco de conteúdo existente. Requer `content_block_id` e pelo menos um campo atualizável: `name`, `content`, `description`, `state` (deve ser `active` ou `draft`) ou `tags`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Content Blocks" }

### Atributos personalizados {#custom-attributes}

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `get_custom_attributes` | [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes/) | Exporta atributos personalizados registrados para seu app. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Custom Attributes" }

### Eventos {#events}

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `get_events_list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/) | Exporta uma lista de eventos personalizados registrados para seu app. |
| `get_events_data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/) | Recupera dados de séries temporais para eventos personalizados. |
| `get_events` | [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data/) | Obtém dados detalhados de eventos com suporte à paginação. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Events" }

### KPIs

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `get_new_users_data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/) | Série diária de contagem de novos usuários. |
| `get_dau_data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/) | Dados de séries temporais de usuários ativos diários. |
| `get_mau_data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/) | Dados de séries temporais de usuários ativos mensais. |
| `get_uninstalls_data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/) | Dados de séries temporais de desinstalações do app. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="KPIs" }

### Biblioteca de mídia {#media-library}

A função `create_media_library_asset` é uma função de escrita. Seu cliente MCP deve chamá-la com `call_write_function`, e sua chave de API deve ter a permissão `media_library.create`.

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `create_media_library_asset` | [`/media_library/create`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create/) | Faz upload de um ativo para sua Biblioteca de mídia da Braze. Você pode fornecer uma URL acessível publicamente (`asset_url`) ou um arquivo codificado em base64 (`asset_file_base64`), mas não ambos. Imagens têm um limite de tamanho de 5 MB. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Media Library" }

### Mensagens {#messages}

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `get_scheduled_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/) | Lista Campaigns e Canvas agendados. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Messages" }

### Centrais de Preferências {#preference-centers}

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `get_preference_centers` | [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/) | Lista suas Centrais de Preferências disponíveis. |
| `get_preference_center_details` | [`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/) | Exibe detalhes de uma Central de Preferências específica, incluindo conteúdo HTML e opções. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Preference Centers" }

### Compras {#purchases}

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `get_product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) | Exporta lista paginada de IDs de produtos. |
| `get_revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series/) | Dados de séries temporais de análise de receita. |
| `get_quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases/) | Dados de séries temporais de quantidade de compras. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Purchases" }

### Segments

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `get_segment_list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) | Exporta lista de Segments com status de rastreamento de análise. |
| `get_segment_data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/) | Dados de análise de séries temporais para Segments. |
| `get_segment_details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/) | Informações detalhadas sobre Segments específicos. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Segments" }

### Envios {#sends}

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `get_send_data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) | Análise de dados diária para envios de Campaigns rastreadas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Sends" }

### Sessões {#sessions}

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `get_session_data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/) | Dados de séries temporais para contagem de sessões do app. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Sessions" }

### Chaves de Autenticação do SDK {#sdk-authentication-keys}

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `get_sdk_authentication_keys` | [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys/) | Lista todas as chaves de autenticação do SDK para seu app. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SDK Authentication Keys" }

### Inscrição {#subscription}

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `get_user_subscription_groups` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) | Lista e obtém os grupos de inscrições de um determinado usuário. |
| `get_subscription_group_status` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) | Obtém o estado da inscrição de um usuário em um grupo de inscrições. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Subscription" }

### Modelos {#templates}

As funções `create_email_template` e `update_email_template` são funções de escrita. Seu cliente MCP deve chamá-las com `call_write_function`, e sua chave de API deve ter a permissão correspondente `templates.email.create` ou `templates.email.update`.

| Função | Endpoint | Descrição |
|----------|----------|-------------|
| `get_email_templates_list` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) | Lista seus modelos de e-mail disponíveis. |
| `get_email_template_info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | Obtém informações sobre seus modelos de e-mail. |
| `create_email_template` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/) | Cria um modelo de e-mail. Requer `template_name`, `subject` e `body`. Campos opcionais são `plaintext_body`, `preheader`, `tags` e `should_inline_css`. |
| `update_email_template` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/) | Atualiza um modelo de e-mail existente. Requer `email_template_id` e pelo menos um campo atualizável: `template_name`, `subject`, `body`, `plaintext_body`, `preheader`, `tags` ou `should_inline_css`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Templates" }

{% multi_lang_include mcp_server/legal_disclaimer.md %}