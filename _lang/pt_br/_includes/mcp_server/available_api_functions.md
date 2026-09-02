# Funções do servidor Braze MCP {#braze-mcp-server-functions}

> O servidor Braze MCP expõe ferramentas de leitura e escrita que mapeiam para endpoints específicos da REST or transferir estado representacional API or interface de programação do aplicativo (API) da Braze. Para saber mais, veja [servidor Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

{% alert note %}
O servidor Braze MCP inclui ferramentas que estão disponíveis apenas para clientes participando de programas beta. Se você tentar acessar uma ferramenta que faz parte de um programa beta e sua conta não tiver o recurso ativado, poderá receber uma resposta de erro. Para participar de um programa beta, entre em contato com seu gerente de conta.
{% endalert %}

## Pré-requisitos {#prerequisites}

Antes de usar este recurso, você precisará [configurar o servidor Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## Funções de API or interface de programação do aplicativo (API) Braze disponíveis {#available-braze-api-functions}

Seu cliente MCP faz referência a essas ferramentas para interagir com o servidor Braze MCP.

### Espaços de trabalho {#workspaces}

| Ferramenta | Endpoint de API or interface de programação do aplicativo (API) | Acesso | Descrição |
| --- | --- | --- | --- |
| `get_workspaces` | N/A | leitura | Descubra quais espaços de trabalho da Braze o token de acesso OAuth atual pode alcançar. Chame isso primeiro: cada `id` de espaço de trabalho retornado é o `app_group_id` que todas as outras ferramentas exigem. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Espaços de trabalho" }

### Campaigns

| Ferramenta | Endpoint de API or interface de programação do aplicativo (API) | Acesso | Descrição |
| --- | --- | --- | --- |
| `get_campaign_list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | leitura | Exporta uma lista de Campaigns com nome, identificador de API or interface de programação do aplicativo (API) da campanha, flag de API or interface de programação do aplicativo (API)-campaign e tags. |
| `get_campaign_details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | leitura | Recupera informações relevantes sobre uma campanha especificada por `campaign_id`. |
| `get_campaign_dataseries` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | leitura | Série diária de estatísticas da campanha ao longo do tempo (envios, aberturas, cliques, conversões por canal). |
| `duplicate_campaign` | [`/campaigns/duplicate`]({{site.baseurl}}/api/endpoints/messaging/duplicate_messages/post_duplicate_campaigns) | criação | Duplica uma campanha existente. |
| `create_campaign`<sup>*</sup> | N/A | criação | Cria uma nova campanha. |
| `edit_campaign`<sup>*</sup> | N/A | atualização | Edita uma campanha existente. |
| `launch_campaign`<sup>*</sup> | N/A | atualização | Lança uma campanha. |
| `stop_campaign`<sup>*</sup> | N/A | atualização | Interrompe uma campanha em execução. |
| `archive_campaign`<sup>*</sup> | N/A | atualização | Arquiva uma campanha. |
| `unarchive_campaign`<sup>*</sup> | N/A | atualização | Desarquiva uma campanha. |
| `get_campaign_draft`<sup>*</sup> | N/A | leitura | Recupera detalhes do rascunho de uma campanha. |
| `get_campaign_live_details`<sup>*</sup> | N/A | leitura | Recupera detalhes de uma campanha ativa. |
| `create_campaign_message`<sup>*</sup> | N/A | criação | Cria uma mensagem dentro de uma campanha. |
| `update_campaign_message`<sup>*</sup> | N/A | atualização | Atualiza uma mensagem de campanha. |
| `delete_campaign_message`<sup>*</sup> | N/A | exclusão | Exclui uma mensagem de campanha. |
| `create_campaign_message_variation`<sup>*</sup> | N/A | criação | Cria uma variação de mensagem dentro de uma campanha. |
| `update_campaign_message_variation`<sup>*</sup> | N/A | atualização | Atualiza uma variação de mensagem de campanha. |
| `delete_campaign_message_variation`<sup>*</sup> | N/A | exclusão | Exclui uma variação de mensagem de campanha. |
| `update_campaign_distribution`<sup>*</sup> | N/A | atualização | Atualiza as configurações de distribuição da campanha. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Campaigns" }

<sup>*</sup> Essa ferramenta está disponível apenas para clientes participantes do programa beta de APIs de campaign. Se a sua conta não tem esse recurso ativado, você pode receber um erro ao tentar usá-la. Para participar do programa beta, entre em contato com o seu gerente de conta.
{: .reset-td-br-1 }

### Canvas {#canvases}

| Ferramenta | Endpoint de API or interface de programação do aplicativo (API) | Acesso | Descrição |
| --- | --- | --- | --- |
| `get_canvas_list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | leitura | Exporta uma lista de Canvas com nome, identificador de API or interface de programação do aplicativo (API) do Canvas e tags. |
| `get_canvas_details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | leitura | Exporta metadados do Canvas: nome, data de criação, status atual e mais. |
| `get_canvas_data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | leitura | Exporta dados de série temporal para um Canvas. |
| `get_canvas_data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | leitura | Exporta resumos consolidados dos dados de série temporal do Canvas para uma visão concisa dos resultados. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Canvas" }

### Catálogos {#catalogs}

| Ferramenta | Endpoint de API or interface de programação do aplicativo (API) | Acesso | Descrição |
| --- | --- | --- | --- |
| `get_catalogs` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | leitura | Lista os catálogos em um espaço de trabalho. |
| `get_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | leitura | Retorna vários itens do catálogo e seus conteúdos. |
| `get_catalog_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | leitura | Retorna um único item do catálogo e seu conteúdo. |
| `create_catalog` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog) | criação | Cria um catálogo. |
| `delete_catalog` | [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog) | exclusão | Exclui um catálogo. |
| `create_catalog_fields` | [`/catalogs/{catalog_name}/fields`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields) | criação | Cria vários campos em um catálogo. |
| `delete_catalog_field` | [`/catalogs/{catalog_name}/fields/{field_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field) | exclusão | Exclui um campo do catálogo. |
| `create_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk) | criação | Cria vários itens em um catálogo. Até 50 itens por solicitação. |
| `edit_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk) | atualização | Edita vários itens existentes em um catálogo. Até 50 itens por solicitação. |
| `replace_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items) | atualização | Substitui vários itens em um catálogo. Cria itens caso não existam. Até 50 itens por solicitação. |
| `delete_catalog_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk) | exclusão | Exclui vários itens de um catálogo. Até 50 itens por solicitação. |
| `create_catalog_selection` | [`/catalogs/{catalog_name}/selections`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections) | criação | Cria uma seleção em um catálogo. |
| `delete_catalog_selection` | [`/catalogs/{catalog_name}/selections/{selection_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection) | exclusão | Exclui uma seleção do catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Catálogos" }

### Atributos personalizados {#custom-attributes}

| Ferramenta | Endpoint de API or interface de programação do aplicativo (API) | Acesso | Descrição |
| --- | --- | --- | --- |
| `get_custom_attributes` | [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) | leitura | Exporta atributos personalizados registrados para o seu app, em grupos de 50, em ordem alfabética. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Atributos personalizados" }

### Eventos personalizados {#custom-events}

| Ferramenta | Endpoint de API or interface de programação do aplicativo (API) | Acesso | Descrição |
| --- | --- | --- | --- |
| `get_events` | [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) | leitura | Exporta eventos personalizados registrados para o seu app, em grupos de 50, em ordem alfabética (paginação por cursor). |
| `get_events_list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | leitura | Exporta nomes de eventos personalizados, em grupos de 250, em ordem alfabética (paginação por página). |
| `get_events_data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | leitura | Ocorrências de um evento personalizado em um período de tempo designado. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Eventos personalizados" }

### Integrações CDI {#cdi-integrations}

| Ferramenta | Endpoint de API or interface de programação do aplicativo (API) | Acesso | Descrição |
| --- | --- | --- | --- |
| `list_integrations` | [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list) | leitura | Lista as integrações existentes de ingestão de dados na nuvem (CDI), 10 por chamada. |
| `get_integration_job_sync_status` | [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status) | leitura | Status de sincronizações anteriores para uma determinada integração CDI, 10 por chamada. |
| `trigger_integration_sync` | [`/cdi/integrations/{integration_id}/sync`]({{site.baseurl}}/api/endpoints/cdi/post_job_sync) | escrita | Dispara uma sincronização para uma determinada integração CDI. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Integrações CDI" }

### KPI

| Ferramenta | Endpoint de API or interface de programação do aplicativo (API) | Acesso | Descrição |
| --- | --- | --- | --- |
| `get_dau_data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | leitura | Série diária de usuários ativos únicos por data. |
| `get_mau_data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | leitura | Série diária de usuários ativos únicos em uma janela móvel de 30 dias. |
| `get_new_users_data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | leitura | Série diária do total de novos usuários por data. |
| `get_uninstalls_data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | leitura | Série diária do total de desinstalações por data. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="KPI" }

### Biblioteca de mídia {#media-library}

| Ferramenta | Endpoint de API or interface de programação do aplicativo (API) | Acesso | Descrição |
| --- | --- | --- | --- |
| `create_media_library_asset` | [`/media_library/create`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create) | criação | Faz upload de um ativo para a biblioteca de mídia da Braze por meio de URL externa ou conteúdo de arquivo em base64. Exatamente um modo de upload deve ser fornecido. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Biblioteca de mídia" }

### Compras {#purchases}

| Ferramenta | Endpoint de API or interface de programação do aplicativo (API) | Acesso | Descrição |
| --- | --- | --- | --- |
| `get_product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | leitura | Lista paginada de IDs de produtos. |
| `get_quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | leitura | Número total de compras no seu app em um intervalo de tempo. |
| `get_revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | leitura | Total de dinheiro gasto no seu app em um intervalo de tempo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Compras" }

### Segments

| Ferramenta | Endpoint de API or interface de programação do aplicativo (API) | Acesso | Descrição |
| --- | --- | --- | --- |
| `get_segment_list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | leitura | Exporta Segments com nome, identificador de API or interface de programação do aplicativo (API) do Segment or segmento e flag de rastreamento de análise de dados. |
| `get_segment_details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | leitura | Recupera informações relevantes sobre um Segment or segmento por `segment_id`. |
| `get_segment_data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | leitura | Série diária do tamanho estimado de um Segment or segmento ao longo do tempo. |
| `get_segment_filters`<sup>*</sup> | N/A | leitura | Recupera definições de filtros de Segment or segmento. |
| `create_segment`<sup>*</sup> | N/A | criação | Cria um novo Segment or segmento. |
| `edit_segment`<sup>*</sup> | N/A | atualização | Edita um Segment or segmento existente. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Segments" }

<sup>*</sup> Essa ferramenta está disponível apenas para clientes participantes do programa beta de APIs de Segment or segmento. Se a sua conta não tem esse recurso ativado, você pode receber um erro ao tentar usá-la. Para participar do programa beta, entre em contato com o seu gerente de conta.
{: .reset-td-br-1 }

### Envios {#sends}

| Ferramenta | Endpoint de API or interface de programação do aplicativo (API) | Acesso | Descrição |
| --- | --- | --- | --- |
| `get_send_data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | leitura | Estatísticas diárias de um `send_id` rastreado (API or interface de programação do aplicativo (API) campaigns). A Braze armazena análises de envios por 14 dias após o envio. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Envios" }

### Sessões {#sessions}

| Ferramenta | Endpoint de API or interface de programação do aplicativo (API) | Acesso | Descrição |
| --- | --- | --- | --- |
| `get_session_data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | leitura | Número de sessões do seu app em um período de tempo designado. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Sessões" }

### Modelos {#templates}

| Ferramenta | Endpoint de API or interface de programação do aplicativo (API) | Acesso | Descrição |
| --- | --- | --- | --- |
| `get_email_templates` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | leitura | Lista os modelos de e-mail disponíveis na sua conta Braze. |
| `get_email_template_info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | leitura | Obtém informações de um modelo de e-mail específico. Modelos do editor de arrastar e soltar não são aceitos. |
| `create_email_template` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template) | criação | Cria um modelo de e-mail no dashboard da Braze. |
| `update_email_template` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template) | atualização | Atualiza um modelo de e-mail existente. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Modelos" }

### Content Blocks

| Ferramenta | Endpoint de API or interface de programação do aplicativo (API) | Acesso | Descrição |
| --- | --- | --- | --- |
| `get_content_blocks` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | leitura | Lista informações dos blocos de conteúdo existentes. |
| `get_content_block_info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | leitura | Obtém informações de um bloco de conteúdo existente, opcionalmente com dados de inclusão em Campaigns ou Canvas. |
| `create_content_block` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block) | criação | Cria um bloco de conteúdo. |
| `update_content_block` | [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block) | atualização | Atualiza um bloco de conteúdo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Content Blocks" }

### Operator

| Ferramenta | Endpoint de API or interface de programação do aplicativo (API) | Acesso | Descrição |
| --- | --- | --- | --- |
| `send_operator_prompt` | N/A | atualização | Envia um prompt em linguagem natural para o BrazeAI Operator. Submete um job em segundo plano e retorna um job_id. |
| `get_operator_result` | N/A | leitura | Consulta o resultado de um job do Operator submetido usando seu job_id. |
| `cancel_operator_job` | N/A | atualização | Cancela um job do Operator em execução. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Operator" }

{% alert important %}
Essas ferramentas estão disponíveis apenas para clientes participantes do programa beta do Operator. Se a sua conta não tem esse recurso ativado, você pode receber um erro ao tentar usá-las. Para participar do programa beta, entre em contato com o seu gerente de conta.
{% endalert %}

{% multi_lang_include mcp_server/legal_disclaimer.md %}