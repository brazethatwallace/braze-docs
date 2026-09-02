---
nav_title: "Visão geral da API or interface de programação do aplicativo (API)"
article_title: "Visão geral da API or interface de programação do aplicativo (API)"
page_order: 2.1
description: "Este artigo de referência aborda os conceitos básicos da API or interface de programação do aplicativo (API), incluindo o que é uma REST or transferir estado representacional API or interface de programação do aplicativo (API), a terminologia e uma visão geral das chaves de API or interface de programação do aplicativo (API)."
page_type: reference
alias: /api/api_key/
---

# Visão geral da API or interface de programação do aplicativo (API) {#api-overview}

> Este artigo de referência aborda os conceitos básicos da API or interface de programação do aplicativo (API), incluindo a terminologia comum e uma visão geral das chaves da REST or transferir estado representacional API or interface de programação do aplicativo (API), permissões e como mantê-las seguras.

## Coleção da REST or transferir estado representacional API or interface de programação do aplicativo (API) da Braze {#braze-rest-api-collection}

| Coleção                                                                    | Finalidade                                                                                      |
|----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| [Catálogos]({{site.baseurl}}/api/endpoints/catalogs)                       | Crie e gerencie catálogos e itens de catálogo para referenciar nas suas Campaigns da Braze.     |
| [Ingestão de dados na nuvem]({{site.baseurl}}/api/endpoints/cdi)           | Gerencie suas integrações e sincronizações de data warehouse.                                   |
| [Listas e endereços de e-mail]({{site.baseurl}}/api/endpoints/email)       | Configure e gerencie a sincronização bidirecional entre a Braze e seus sistemas de e-mail.      |
| [Exportação]({{site.baseurl}}/api/endpoints/export)                        | Acesse e exporte diversos detalhes das suas Campaigns, Canvas, KPIs e muito mais.               |
| [Biblioteca de mídia]({{site.baseurl}}/api/endpoints/media_library)        | Gerencie ativos na Braze.                                                                       |
| [Mensagens]({{site.baseurl}}/api/endpoints/messaging)                      | Agende, envie e gerencie suas Campaigns e Canvas.                                               |
| [Central de Preferências]({{site.baseurl}}/api/endpoints/preference_center) | Crie sua Central de Preferências e atualize o estilo dela.                                      |
| [SCIM]({{site.baseurl}}/api/endpoints/scim)                                | Gerencie identidades de usuários em aplicativos e serviços baseados na nuvem.                   |
| [SMS]({{site.baseurl}}/api/endpoints/sms)                                  | Gerencie os números de telefone dos seus usuários nos seus grupos de inscrições.                |
| [Grupos de inscrições]({{site.baseurl}}/api/endpoints/subscription_groups) | Liste e atualize os grupos de inscrições de SMS e e-mail armazenados no dashboard da Braze.     |
| [Modelos]({{site.baseurl}}/api/endpoints/templates)                        | Crie e atualize modelos para envio de mensagens por e-mail e Content Blocks.                    |
| [Dados de usuários]({{site.baseurl}}/api/endpoints/user_data)              | Identifique, rastreie e gerencie seus usuários.                                                 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Coleção da REST or transferir estado representacional API or interface de programação do aplicativo (API) da Braze" }

## Definições da API or interface de programação do aplicativo (API) {#api-definitions}

A seguir está uma visão geral dos termos que você pode encontrar na documentação da REST or transferir estado representacional API or interface de programação do aplicativo (API) da Braze.

### Endpoints

A Braze gerencia diversas instâncias diferentes para nosso dashboard e endpoints REST or transferir estado representacional. Quando sua conta é provisionada, você faz login em uma das seguintes URLs. Use o endpoint REST or transferir estado representacional correto com base na instância para a qual você foi provisionado. Se não tiver certeza, abra um [ticket de suporte]({{site.baseurl}}/user_guide/administer/personal/braze_support) ou use a tabela a seguir para associar a URL do dashboard que você utiliza ao endpoint REST or transferir estado representacional correto.

Para encontrar seu endpoint REST or transferir estado representacional na Braze:

1. Faça login na Braze e acesse **Configurações** > **APIs e identificadores** > **Chaves de API or interface de programação do aplicativo (API)**.
2. Selecione uma chave de API or interface de programação do aplicativo (API) existente ou selecione **Criar chave de API or interface de programação do aplicativo (API)** para criar uma nova chave.
3. Copie o endpoint REST or transferir estado representacional exibido nesta guia e use esse endpoint para suas solicitações de API or interface de programação do aplicativo (API).

{% alert important %}
Ao usar endpoints para chamadas de API or interface de programação do aplicativo (API), use o endpoint REST or transferir estado representacional.

Para integração SDK or kit de desenvolvimento de software, use o [endpoint de SDK or kit de desenvolvimento de software or endpoint do SDK or kit de desenvolvimento de software]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints), não o endpoint REST or transferir estado representacional.
{% endalert %}

{% multi_lang_include administer/data_centers.md datacenters='instances' %}

### Limites da API or interface de programação do aplicativo (API) {#api-limits}

Para a maioria das APIs, a Braze possui um limite de frequência padrão de 250.000 solicitações por hora. No entanto, determinados tipos de solicitação possuem seu próprio limite de frequência aplicado para lidar melhor com grandes volumes de dados na base de clientes. Para saber mais, consulte [Limites de frequência da API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/api_limits)

### IDs de usuários {#user-ids}

- **ID externo do usuário**: O `external_id` serve como um identificador exclusivo do usuário para o qual você está enviando dados. Esse identificador deve ser o mesmo que você definiu no SDK or kit de desenvolvimento de software da Braze para evitar a criação de múltiplos perfis para o mesmo usuário.
- **ID de usuário Braze**: O `braze_id` serve como um identificador exclusivo de usuário definido pela Braze. Você pode usar esse identificador para excluir usuários por meio da REST or transferir estado representacional API or interface de programação do aplicativo (API), além dos external_ids.

Para saber mais, consulte os seguintes artigos com base na sua plataforma: [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=swift), [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=android) e [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web).

## Sobre as chaves da REST or transferir estado representacional API or interface de programação do aplicativo (API) {#about-rest-api-keys}

Uma chave da REST or transferir estado representacional API or interface de programação do aplicativo (API) (interface de programação de aplicativos REST or transferir estado representacional) é um código exclusivo que você passa para uma API or interface de programação do aplicativo (API) a fim de autenticar a chamada de API or interface de programação do aplicativo (API) e identificar o aplicativo ou usuário que faz a chamada. Você acessa a API or interface de programação do aplicativo (API) usando solicitações web HTTPS no endpoint da REST or transferir estado representacional API or interface de programação do aplicativo (API) da sua empresa. As chaves da REST or transferir estado representacional API or interface de programação do aplicativo (API) funcionam em conjunto com as chaves de identificação de app para rastrear, acessar, enviar, exportar e analisar dados, ajudando a garantir que tudo funcione sem problemas.

Os espaços de trabalho e as chaves de API or interface de programação do aplicativo (API) caminham juntos na Braze. Os espaços de trabalho foram projetados para abrigar versões do mesmo aplicativo em várias plataformas. Muitos clientes também usam espaços de trabalho para conter versões gratuitas e premium de seus aplicativos na mesma plataforma. Como você pode notar, esses espaços de trabalho também utilizam a REST or transferir estado representacional API or interface de programação do aplicativo (API) e possuem suas próprias chaves da REST or transferir estado representacional API or interface de programação do aplicativo (API). Essas chaves podem ter escopos individuais definidos para incluir acesso a endpoints específicos da API or interface de programação do aplicativo (API). Cada chamada à API or interface de programação do aplicativo (API) deve incluir uma chave com acesso ao endpoint chamado.

Nós nos referimos tanto à chave da REST or transferir estado representacional API or interface de programação do aplicativo (API) quanto à chave de API or interface de programação do aplicativo (API) do espaço de trabalho como `api_key`. A `api_key` é incluída em cada solicitação como um cabeçalho da solicitação e funciona como uma chave de autenticação que permite o uso das nossas REST or transferir estado representacional APIs. Essas REST or transferir estado representacional APIs são usadas para rastrear usuários, enviar mensagens, exportar dados de usuários e muito mais. Ao criar uma nova chave da REST or transferir estado representacional API or interface de programação do aplicativo (API), você deve conceder acesso a endpoints específicos. Ao atribuir permissões específicas a uma chave de API or interface de programação do aplicativo (API), você pode limitar exatamente quais chamadas essa chave de API or interface de programação do aplicativo (API) pode autenticar.

![Painel de chaves da REST or transferir estado representacional API or interface de programação do aplicativo (API) na guia Chaves de API or interface de programação do aplicativo (API).]({% image_buster /assets/img_archive/rest-api-key.png %})

{% alert tip %}
Além das chaves da REST or transferir estado representacional API or interface de programação do aplicativo (API), existe também um tipo de chave chamado chaves de identificação, que pode ser usado para referenciar itens específicos — como apps, modelos, Canvas, Campaigns, Content Cards e Segments — a partir da API or interface de programação do aplicativo (API). Para saber mais, consulte [Tipos de identificadores de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/identifier_types).
{% endalert %}

### Criando chaves da REST or transferir estado representacional API or interface de programação do aplicativo (API) {#creating-rest-api-keys}

Para criar uma nova chave da REST or transferir estado representacional API or interface de programação do aplicativo (API):

1. Acesse **Configurações** > **APIs e identificadores**.
2. Selecione **Criar chave de API or interface de programação do aplicativo (API)**.
3. Dê à sua nova chave um nome para identificação rápida.
4. Especifique os [endereços IP na lista de permissões](#api-ip-allowlisting) e sub-redes para a nova chave.
5. Selecione quais [permissões](#rest-api-key-permissions) você deseja associar à sua nova chave.

{% alert important %}
Tenha em mente que, após criar uma nova chave de API or interface de programação do aplicativo (API), você não poderá editar o escopo de permissões ou os IPs na lista de permissões. Essa limitação existe por motivos de segurança. Se você precisar alterar o escopo de uma chave, crie uma nova chave com as permissões atualizadas e implemente-a no lugar da antiga. Após concluir a implementação, você poderá excluir a chave antiga.
{% endalert %}

### Permissões da chave da REST or transferir estado representacional API or interface de programação do aplicativo (API) {#rest-api-key-permissions}

As permissões da chave de API or interface de programação do aplicativo (API) são permissões que você pode atribuir a um usuário ou grupo para limitar o acesso deles a determinadas chamadas de API or interface de programação do aplicativo (API). Para visualizar sua lista de permissões de chave de API or interface de programação do aplicativo (API), acesse **Configurações** > **APIs e identificadores** e selecione sua chave de API or interface de programação do aplicativo (API).

{% tabs %}
{% tab Dados de usuário %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `users.track` | [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) | Registrar atributos de usuário, eventos personalizados e compras. |
| `users.delete` | [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) | Excluir qualquer usuário. |
| `users.alias.new` | [`/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias) | Criar um novo alias para um usuário existente. |
| `users.identify` | [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) | Identificar um usuário somente com alias usando um ID externo. |
| `users.export.ids` | [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) | Consultar informações do perfil de usuário por ID de usuário. |
| `users.export.segment` | [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) | Consultar informações do perfil de usuário por Segment or segmento. |
| `users.merge` | [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) | Mesclar dois usuários existentes. |
| `users.external_ids.rename` | [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename) | Alterar o ID externo de um usuário existente. |
| `users.external_ids.remove` | [`/users/external_ids/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove) | Remover o ID externo de um usuário existente. |
| `users.alias.update` | [`/users/alias/update`]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update) | Atualizar um alias para um usuário existente. |
| `users.export.global_control_group` | [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group) | Consultar informações do perfil de usuário no grupo de controle global. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissões da chave da REST or transferir estado representacional API or interface de programação do aplicativo (API)" }

 {% endtab %}
 {% tab E-mail %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `email.unsubscribe` | [`/email/unsubscribes`]({{site.baseurl}}/api/endpoints/email/get_query_unsubscribed_email_addresses) | Consultar endereços de e-mail com inscrição cancelada. |
| `email.status` | [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status) | Alterar o status de um endereço de e-mail. |
| `email.hard_bounces` | [`/email/hard_bounces`]({{site.baseurl}}/api/endpoints/email/get_list_hard_bounces) | Consultar endereços de e-mail com hard bounce. |
| `email.bounce.remove` | [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces) | Remover endereços de e-mail da sua lista de hard bounce. |
| `email.spam.remove` | [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam) | Remover endereços de e-mail da sua lista de SPAM. |
| `email.blacklist` | [`/email/blacklist`]({{site.baseurl}}/api/endpoints/email/post_blacklist) | Adicionar endereços de e-mail à lista de proibições. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissões da chave da REST or transferir estado representacional API or interface de programação do aplicativo (API)" }

{% endtab %}
{% tab Mensagens %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `messages.send` | [`/messages/send `]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) | Enviar uma mensagem imediata para usuários específicos. |
| `messages.schedule.create` | [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages) | Agendar uma mensagem para ser enviada em um horário específico. |
| `messages.schedule.update` | [`/messages/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages) | Atualizar uma mensagem agendada. |
| `messages.schedule.delete` | [`/messages/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages) | Excluir uma mensagem agendada. |
| `messages.schedule_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled) | Consultar todas as mensagens de transmissão agendadas. |
| `messages.live_activity.update` | [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) | Atualizar uma Live Activity do iOS. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissões da chave da REST or transferir estado representacional API or interface de programação do aplicativo (API)" }

{% endtab %}
{% tab Campaigns %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `campaigns.trigger.send` | [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) | Disparar o envio de uma Campaign existente. |
| `campaigns.trigger.schedule.create` | [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns) | Agendar um envio de Campaign com entrega disparada por API or interface de programação do aplicativo (API). |
| `campaigns.trigger.schedule.update` | [`/campaigns/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns) | Atualizar uma Campaign agendada com entrega disparada por API or interface de programação do aplicativo (API). |
| `campaigns.trigger.schedule.delete` | [`/campaigns/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages) | Excluir uma Campaign agendada com entrega disparada por API or interface de programação do aplicativo (API). |
| `campaigns.list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | Consultar uma lista de Campaigns. |
| `campaigns.data_series` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | Consultar análise de dados de Campaigns em um intervalo de tempo. |
| `campaigns.details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | Consultar detalhes de uma Campaign específica. |
| `sends.data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | Consultar análise de dados de envio de mensagens em um intervalo de tempo. |
| `sends.id.create` | [`/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids) | Criar um ID de envio para rastreamento de envios em massa de mensagens. |
| `campaigns.url_info.details` | [`/campaigns/url_info/details`]({{site.baseurl}}) | Consultar detalhes de URL de uma variação de mensagem específica dentro de uma Campaign. |
| `transactional.send` | [`/transactional/v1/campaigns/{campaign_id}/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message) | Permite o envio de mensagens transacionais usando o endpoint de mensagens transacionais. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissões da chave da REST or transferir estado representacional API or interface de programação do aplicativo (API)" }

{% endtab %}
{% tab Canvas %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `canvas.trigger.send` | [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) | Disparar o envio de um Canvas existente. |
| `canvas.trigger.schedule.create` | [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases) | Agendar um envio de Canvas com entrega disparada por API or interface de programação do aplicativo (API). |
| `canvas.trigger.schedule.update` | [`/canvas/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases) | Atualizar um Canvas agendado com entrega disparada por API or interface de programação do aplicativo (API). |
| `canvas.trigger.schedule.delete` | [`/canvas/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases) | Excluir um Canvas agendado com entrega disparada por API or interface de programação do aplicativo (API). |
| `canvas.list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | Consultar uma lista de Canvas. |
| `canvas.data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | Consultar análise de dados de Canvas em um intervalo de tempo. |
| `canvas.details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | Consultar detalhes de um Canvas específico. |
| `canvas.data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | Consultar resumos de análise de dados de Canvas em um intervalo de tempo. |
| `canvas.url_info.details` | [`/canvas/url_info/details`]({{site.baseurl}}/get_canvas_link_alias) | Consultar detalhes de URL de uma variação de mensagem específica dentro de uma etapa do Canvas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissões da chave da REST or transferir estado representacional API or interface de programação do aplicativo (API)" }

{% endtab %}
{% tab Segments %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `segments.list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | Consultar uma lista de Segments. |
| `segments.data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | Consultar análise de dados de Segments em um intervalo de tempo. |
| `segments.details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | Consultar detalhes de um Segment or segmento específico. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissões da chave da REST or transferir estado representacional API or interface de programação do aplicativo (API)" }

{% endtab %}
{% tab Compras %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `purchases.product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | Consultar uma lista de produtos comprados no seu app. |
| `purchases.revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | Consultar o total de dinheiro gasto por dia no seu app em um intervalo de tempo. |
| `purchases.quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | Consultar o número total de compras por dia no seu app em um intervalo de tempo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissões da chave da REST or transferir estado representacional API or interface de programação do aplicativo (API)" }

{% endtab %}
{% tab Eventos %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `events.list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | Consultar uma lista de eventos personalizados. |
| `events.data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | Consultar ocorrências de um evento personalizado em um intervalo de tempo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissões da chave da REST or transferir estado representacional API or interface de programação do aplicativo (API)" }

{% endtab %}
{% tab Sessões %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `sessions.data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | Consultar sessões por dia em um intervalo de tempo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissões da chave da REST or transferir estado representacional API or interface de programação do aplicativo (API)" }

{% endtab %}
{% tab KPIs %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `kpi.dau.data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | Consultar usuários ativos únicos por dia em um intervalo de tempo. |
| `kpi.mau.data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | Consultar o total de usuários ativos únicos em uma janela móvel de 30 dias em um intervalo de tempo. |
| `kpi.new_users.data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | Consultar novos usuários por dia em um intervalo de tempo. |
| `kpi.uninstalls.data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | Consultar desinstalações do app por dia em um intervalo de tempo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissões da chave da REST or transferir estado representacional API or interface de programação do aplicativo (API)" }

{% endtab %}
{% tab Modelos %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `templates.email.create` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template) | Criar um novo modelo de e-mail no dashboard. |
| `templates.email.info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | Consultar informações de um modelo específico. |
| `templates.email.list` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | Consultar uma lista de modelos de e-mail. |
| `templates.email.update` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template) | Atualizar um modelo de e-mail armazenado no dashboard. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissões da chave da REST or transferir estado representacional API or interface de programação do aplicativo (API)" }

{% endtab %}
{% tab SSO %}

| Permissão | Descrição |
| --- | --- |
| `sso.saml.login` | Configurar login iniciado pelo provedor de identidade. Para saber mais, consulte [Login iniciado pelo provedor de serviço (SP)]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Permissões da chave da REST or transferir estado representacional API or interface de programação do aplicativo (API)" }

{% endtab %}
{% tab Content Blocks %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `content_blocks.info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | Consultar informações de um modelo específico. |
| `content_blocks.list` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | Consultar uma lista de Content Blocks. |
| `content_blocks.create` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block) | Criar um novo Content Block no dashboard. |
| `content_blocks.update` | [`/content_blocks_update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block) | Atualizar um Content Block existente no dashboard. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissões da chave da REST or transferir estado representacional API or interface de programação do aplicativo (API)" }

{% endtab %}
{% tab Central de Preferências %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `preference_center.get` | [`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | Obter uma Central de Preferências. |
| `preference_center.list` | [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center) | Listar centrais de preferências. |
| `preference_center.update` | [`/preference_center/v1`]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center)<br><br>[`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center) | Criar ou atualizar uma Central de Preferências. |
| `preference_center.user.get` | [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center) | Obter um link da Central de Preferências para um usuário. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissões da chave da REST or transferir estado representacional API or interface de programação do aplicativo (API)" }

{% endtab %}
{% tab Inscrição %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `subscription.status.set` | [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) | Definir o status do grupo de inscrições. |
| `subscription.status.get` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) | Obter o status do grupo de inscrições. |
| `subscription.groups.get` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) | Obter o status dos grupos de inscrições nos quais usuários específicos estão explicitamente inscritos ou com inscrição cancelada. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissões da chave da REST or transferir estado representacional API or interface de programação do aplicativo (API)" }

{% endtab %}
{% tab SMS %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `sms.invalid_phone_numbers` | [`/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers) | Consultar números de telefone inválidos. |
| `sms.invalid_phone_numbers.remove` | [`/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers) | Remover a sinalização de número de telefone inválido dos usuários. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissões da chave da REST or transferir estado representacional API or interface de programação do aplicativo (API)" }

{% endtab %}
{% tab Catálogos %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `catalogs.add_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk) | Adicionar vários itens a um catálogo existente. |
| `catalogs.update_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk) | Atualizar vários itens em um catálogo existente. |
| `catalogs.delete_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk) | Excluir vários itens de um catálogo existente. |
| `catalogs.get_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | Obter um único item de um catálogo existente. |
| `catalogs.update_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item) | Atualizar um único item em um catálogo existente. |
| `catalogs.create_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item) | Criar um único item em um catálogo existente. |
| `catalogs.delete_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item) | Excluir um único item de um catálogo existente. |
| `catalogs.replace_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item) | Substituir um único item de um catálogo existente. |
| `catalogs.create` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog) | Criar um catálogo. |
| `catalogs.get` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | Obter uma lista de catálogos. |
| `catalogs.delete` | [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog) | Excluir um catálogo. |
| `catalogs.get_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | Obter prévia de itens de um catálogo existente. |
| `catalogs.replace_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items) | Substituir itens em um catálogo existente. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissões da chave da REST or transferir estado representacional API or interface de programação do aplicativo (API)" }

{% endtab %}
{% tab Autenticação do SDK or kit de desenvolvimento de software %}

| Permissão | Endpoint | Descrição |
|---|---|---|
| `sdk_authentication.create` | [`/app_group/sdk_authentication/create`]({{site.baseurl}}/api/endpoints/sdk_authentication/post_create_sdk_authentication_key) | Criar uma nova chave de autenticação do SDK or kit de desenvolvimento de software para o seu app. |
| `sdk_authentication.primary` | [`/app_group/sdk_authentication/primary`]({{site.baseurl}}/api/endpoints/sdk_authentication/put_primary_sdk_authentication_key) | Marcar uma chave de autenticação do SDK or kit de desenvolvimento de software como a chave principal do seu app. |
| `sdk_authentication.delete` | [`/app_group/sdk_authentication/delete`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key) | Excluir uma chave de autenticação do SDK or kit de desenvolvimento de software do seu app. |
| `sdk_authentication.keys` | [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | Obter todas as chaves de autenticação do SDK or kit de desenvolvimento de software do seu app. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permissões da chave da REST or transferir estado representacional API or interface de programação do aplicativo (API)" }

{% endtab %}
{% endtabs %}

### Gerenciando chaves da REST or transferir estado representacional API or interface de programação do aplicativo (API) {#managing-rest-api-keys}

Você pode visualizar detalhes ou excluir chaves da REST or transferir estado representacional API or interface de programação do aplicativo (API) existentes em **Configurações** > **APIs e identificadores** > guia **Chaves de API or interface de programação do aplicativo (API)**. Observe que não é possível editar chaves da REST or transferir estado representacional API or interface de programação do aplicativo (API) após criá-las.

A guia **Chaves de API or interface de programação do aplicativo (API)** inclui as seguintes informações para cada chave:

| Campo | Descrição |
| ------------ | :------------------------------------------------------------------------------------------------------------------ |
| Nome da chave de API or interface de programação do aplicativo (API) | O nome dado à chave no momento da criação. |
| Identificador | A chave de API or interface de programação do aplicativo (API). |
| Criada por | O endereço de e-mail do usuário que criou a chave. Este campo aparece como "N/A" para chaves criadas antes de junho de 2023. |
| Data de criação | A data em que esta chave foi criada. |
| Último uso | A data em que esta chave foi usada pela última vez. Este campo aparece como "N/A" para chaves que nunca foram usadas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Gerenciando chaves da REST or transferir estado representacional API or interface de programação do aplicativo (API)" }

Para visualizar os detalhes de uma chave de API or interface de programação do aplicativo (API), passe o cursor sobre a chave e selecione <i class="fa-solid fa-eye" alt="Visualizar"></i> **Visualizar**. Isso inclui todas as permissões que esta chave possui, IPs na lista de permissões (se houver) e se esta chave está habilitada para a lista de permissões de IP da Braze.

![A lista de permissões de chave de API or interface de programação do aplicativo (API) no dashboard da Braze.]({% image_buster /assets/img_archive/view-api-key.png %})

Observe que, ao [excluir um usuário]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users), a Braze não exclui as chaves de API or interface de programação do aplicativo (API) associadas que esse usuário criou. Para excluir uma chave, passe o cursor sobre a chave e selecione <i class="fa-solid fa-trash-can" alt="Excluir"></i> **Excluir**.

![Uma chave de API or interface de programação do aplicativo (API) chamada 'Last Seen' com o ícone de lixeira destacado, mostrando 'Excluir'.]({% image_buster /assets/img_archive/api-key-options.png %}){: style="max-width:30%;"}

### Segurança da chave da REST or transferir estado representacional API or interface de programação do aplicativo (API) {#rest-api-key-security}

As chaves de API or interface de programação do aplicativo (API) são usadas para autenticar uma chamada de API or interface de programação do aplicativo (API). Ao criar uma nova chave da REST or transferir estado representacional API or interface de programação do aplicativo (API), você precisa conceder acesso a endpoints específicos. Ao atribuir permissões específicas a uma chave de API or interface de programação do aplicativo (API), você pode limitar exatamente quais chamadas essa chave de API or interface de programação do aplicativo (API) pode autenticar.

Considerando que as chaves da REST or transferir estado representacional API or interface de programação do aplicativo (API) permitem acesso a endpoints potencialmente sensíveis da REST or transferir estado representacional API or interface de programação do aplicativo (API), proteja essas chaves e compartilhe-as apenas com parceiros confiáveis. Elas nunca devem ser expostas publicamente. Por exemplo, não use essa chave para fazer chamadas AJAX do seu website nem a exponha de nenhuma outra forma pública.

Uma boa prática de segurança é atribuir a um usuário apenas o acesso necessário para realizar seu trabalho: esse princípio também pode ser aplicado a chaves de API or interface de programação do aplicativo (API), atribuindo permissões a cada chave. Essas permissões oferecem maior segurança e controle sobre as diferentes áreas da sua conta.

{% alert warning %}
Considerando que as chaves da REST or transferir estado representacional API or interface de programação do aplicativo (API) permitem acesso a endpoints potencialmente sensíveis da REST or transferir estado representacional API or interface de programação do aplicativo (API), certifique-se de que elas sejam armazenadas e usadas com segurança. Por exemplo, não use essa chave para fazer chamadas AJAX do seu website nem a exponha de nenhuma outra forma pública.
{% endalert %}

Se você acidentalmente expor uma chave, poderá excluí-la do console de desenvolvedor. Para obter ajuda com esse processo, abra um [ticket de suporte]({{site.baseurl}}/user_guide/administer/personal/braze_support).

### Segurança das chaves da REST or transferir estado representacional API or interface de programação do aplicativo (API) e das chaves da API or interface de programação do aplicativo (API) SDK or kit de desenvolvimento de software {#security-of-rest-api-keys-and-sdk-api-keys}

As chaves da REST or transferir estado representacional API or interface de programação do aplicativo (API) e as chaves da API or interface de programação do aplicativo (API) SDK or kit de desenvolvimento de software possuem perfis de segurança diferentes.

| | Chaves da REST or transferir estado representacional API or interface de programação do aplicativo (API) | Chaves da API or interface de programação do aplicativo (API) SDK or kit de desenvolvimento de software |
|---|---|---|
| Finalidade | Autenticação do lado do servidor para a REST or transferir estado representacional API or interface de programação do aplicativo (API) (envio de mensagens, exportação de dados, gerenciamento de usuários) | Identificação do lado do cliente para o SDK or kit de desenvolvimento de software da Braze (ingestão de dados, mensagens no app, Content Cards) |
| Visibilidade | **Deve permanecer privada**. Nunca exponha em código do lado do cliente, repositórios públicos ou aplicativos de usuário. | Projetada para ser pública. Incluída dentro do binário do seu app ou visível no JavaScript do navegador de internet or navegador web, de forma semelhante a um ID de rastreamento do Google Analytics. |
| Solução se exposta | Revogue a chave imediatamente e crie uma substituta em **Configurações** > **APIs e identificadores** > **Chaves de API or interface de programação do aplicativo (API)**. Uma chave da REST or transferir estado representacional API or interface de programação do aplicativo (API) exposta pode ser usada para enviar mensagens, exportar dados de usuários ou modificar configurações da conta. | Nenhuma ação necessária. Uma chave da API or interface de programação do aplicativo (API) SDK or kit de desenvolvimento de software pode apenas ingerir dados e recuperar mensagens do lado do cliente (como mensagens no app e Content Cards). Ela não pode exportar dados de usuários, enviar mensagens em seu nome ou modificar Campaigns. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Segurança das chaves da REST or transferir estado representacional API or interface de programação do aplicativo (API) e das chaves da API or interface de programação do aplicativo (API) SDK or kit de desenvolvimento de software" }

### Lista de permissões de IP da API or interface de programação do aplicativo (API) {#api-ip-allowlisting}

Para segurança adicional, você pode especificar uma lista de endereços IP e sub-redes com permissão para fazer solicitações da REST or transferir estado representacional API or interface de programação do aplicativo (API) para uma determinada chave da REST or transferir estado representacional API or interface de programação do aplicativo (API). Isso é chamado de lista de permissões (ou whitelisting). Para permitir endereços IP ou sub-redes específicos, adicione-os à seção **Whitelist IPs** ao criar uma nova chave da REST or transferir estado representacional API or interface de programação do aplicativo (API):

![Opção para adicionar IPs à lista de permissões ao criar uma chave de API or interface de programação do aplicativo (API).]({% image_buster /assets/img_archive/api-key-ip-whitelisting.png %})

Se você não especificar nenhum, as solicitações poderão ser enviadas de qualquer endereço IP.

{% alert tip %}
Se você estiver criando um webhook Braze-para-Braze e usando lista de permissões, consulte a lista de [IPs para adicionar à lista de permissões]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook).
{% endalert %}

## Autenticação e segurança da API or interface de programação do aplicativo (API) {#api-authentication-and-security}

### Autenticação por token Bearer {#bearer-token-authentication}

A Braze autentica solicitações da REST or transferir estado representacional API or interface de programação do aplicativo (API) usando a chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional passada como um token Bearer no cabeçalho de solicitação `Authorization`. Ao enviar uma solicitação, inclua sua chave de API or interface de programação do aplicativo (API) no seguinte formato:

```bash
Authorization: Bearer YOUR_REST_API_KEY
```

Em cada solicitação, a Braze executa as seguintes verificações de validação no lado do servidor:

1. **Validade do token:** verifica se a chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional existe na Braze e está ativa (por exemplo, não foi revogada ou desabilitada).
2. **Autorização do token:** confirma se a chave de API or interface de programação do aplicativo (API) tem as permissões necessárias para o endpoint solicitado.

Se a autenticação falhar, a API or interface de programação do aplicativo (API) retorna uma resposta de erro com um código de status HTTP. Por exemplo, `401 Unauthorized` indica uma chave inválida ou ausente, enquanto `403 Forbidden` indica que a chave não tem permissão para o endpoint solicitado. Para saber mais, consulte [Erros de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/errors).

### Casing do cabeçalho de solicitação {#header-casing}

Os nomes de cabeçalhos HTTP não diferenciam maiúsculas de minúsculas, então `Authorization` e `authorization` são equivalentes. O mesmo se aplica a outros cabeçalhos de solicitação padrão, como `Content-Type`. Envie o casing que seu cliente HTTP produzir.

A Braze também aceita qualquer casing do esquema `Bearer` (`Bearer`, `bearer` ou `BEARER`). Envie a chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional exatamente como ela foi emitida.

### Segurança em nível de rede {#network-level-security}

As solicitações da REST or transferir estado representacional API or interface de programação do aplicativo (API) para a Braze são protegidas por criptografia Transport Layer Security (TLS) em todo o caminho da solicitação. A tabela a seguir descreve o fluxo de rede de uma solicitação de API or interface de programação do aplicativo (API) do seu servidor até a Braze:

| Etapa | Componente | Descrição |
| --- | --- | --- |
| 1 | Seu servidor | Inicia uma solicitação HTTPS com criptografia TLS. |
| 2 | Cloudflare | Encerra a conexão TLS do cliente e aplica proteções em nível de rede. |
| 3 | Network Load Balancer (NLB) | Encaminha os pacotes para a infraestrutura do aplicativo. Os NLBs operam na Camada 4, o que significa que não há proxy na Camada 7. Os pacotes são encaminhados sem inspeção ou modificação em nível HTTP. |
| 4 | Ingress NGINX | Encerra a conexão TLS interna e roteia a solicitação. |
| 5 | Unicorn (servidor de aplicação) | Processa a solicitação autenticada. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Segurança em nível de rede" }

A criptografia TLS cobre todos os elos da cadeia. Seu servidor se conecta ao Cloudflare via TLS, e o Cloudflare estabelece uma conexão TLS separada através do NLB até o ingress NGINX, de modo que sua chave de API or interface de programação do aplicativo (API) e os dados da solicitação permanecem criptografados em trânsito.

## Recursos adicionais {#additional-resources}

### Biblioteca de cliente Ruby {#ruby-client-library}

Se você está implementando a Braze usando Ruby, pode usar a [biblioteca de cliente Ruby](https://github.com/braze-inc/braze-api-client-ruby) para reduzir o tempo de importação de dados. Uma biblioteca de cliente é uma coleção de código específica para uma linguagem de programação — neste caso, Ruby — que facilita o uso de uma API or interface de programação do aplicativo (API).

A biblioteca de cliente Ruby é compatível com os [endpoints de usuário]({{site.baseurl}}/api/endpoints/user_data).

{% alert important %}
Esta biblioteca de cliente está em beta. Para ajudar a melhorá-la, envie feedback para [smb-product@braze.com](mailto:smb-product@braze.com).
{% endalert %}