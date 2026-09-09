---
page_order: 0
nav_title: Início
article_title: Guia da API da Braze
layout: api_glossary
glossary_top_header: "Guia da API da Braze"
glossary_top_text: "A Braze oferece uma REST API de alta performance para rastrear usuários, enviar mensagens, exportar dados e gerenciar Campaigns, Canvas, catálogos e muito mais. Use este glossário para navegar pelos endpoints por tipo, abrir artigos de referência com detalhes de requisição e resposta, e encontrar links para autenticação, limites de frequência e documentação de objetos."
description: "Navegue pelos endpoints da REST API da Braze por tipo, com links para autenticação, limites de frequência e documentação de referência de objetos."
page_type: glossary
glossary_tag_name: Endpoint Type

glossary_filter_text: "Selecione o tipo de endpoint para refinar o glossário:"

glossary_mid_text: "Pesquisa de endpoint"
guide_featured_list:
  - name: Visão geral da API
    image: /assets/img/braze_icons/annotation-info.svg
    link: /docs/api/basics
  - name: Tipos de identificadores de API
    link: /docs/api/identifier_types
    image: /assets/img/braze_icons/clipboard-check.svg
  - name: Objetos e filtros
    link: /docs/api/objects_filters
    image: /assets/img/braze_icons/settings-01.svg
  - name: Erros e respostas
    link: /docs/api/errors
    image: /assets/img/braze_icons/list.svg
  - name: Retenção de dados
    link: /docs/api/data_retention
    image: /assets/img/braze_icons/laptop-02.svg
  - name: Limites de frequência
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
    description: Atualize as credenciais de push para um único app.
    tags:
      - Apps
  - name: <a href='/docs/api/endpoints/user_data/post_user_alias'>/users/alias/new</a>
    description: Adicione novos aliases de usuário para usuários identificados existentes ou crie novos usuários não identificados.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_users_alias_update'>/users/alias/update</a>
    description: Atualize nomes de alias de usuário existentes para novos nomes de alias de usuário.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_user_delete'>/users/delete</a>
    description: Exclua qualquer perfil de usuário especificando um identificador de usuário conhecido.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/export/user_data/post_users_global_control_group'>/users/export/global_control_group</a>
    description: Exporte todos os usuários de um grupo de controle global.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/export/user_data/post_users_identifier'>/users/export/ids</a>
    description: Exporte dados de qualquer perfil de usuário especificando um identificador de usuário.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/export/user_data/post_users_segment'>/users/export/segment</a>
    description: Exporte todos os usuários de um Segment.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename'>/users/external_ids/rename</a>
    description: Renomeie os IDs externos dos seus usuários.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove'>/users/external_ids/remove</a>
    description: Remova os IDs externos antigos e obsoletos dos seus usuários.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_user_identify'>/users/identify</a>
    description: Identifique um usuário não identificado (somente alias).
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_user_track'>/users/track</a>
    description: "Registre eventos personalizados, compras e atualize atributos do perfil de usuário."
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_users_merge'>/users/merge</a>
    description: Mescle um perfil de usuário em outro usuário.
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/data_objects'>/data_objects/*</a>
    description: "Veja a referência completa de endpoints de Data Objects, incluindo tipos de objetos, objetos e endpoints de relacionamento."
    tags:
      - Data Objects
  - name: <a href='/docs/api/endpoints/data_objects/types/get_list_data_object_types'>/data_objects/types</a>
    description: Liste os tipos de objetos de dados no espaço de trabalho.
    tags:
      - Data Objects
  - name: <a href='/docs/api/endpoints/data_objects/types/get_data_object_type'>/data_objects/types/{type_name}</a>
    description: Obtenha um tipo de objeto de dados e sua definição de esquema.
    tags:
      - Data Objects
  - name: <a href='/docs/api/endpoints/data_objects/types/get_list_user_relationship_types'>/data_objects/types/{type_name}/user_relationship_types</a>
    description: Liste os tipos de relacionamento de usuário para um tipo de objeto de dados.
    tags:
      - Data Objects
  - name: <a href='/docs/api/endpoints/data_objects/types/get_list_object_relationship_types'>/data_objects/types/{type_name}/object_relationship_types</a>
    description: Liste os tipos de relacionamento de objeto para um tipo de objeto de dados.
    tags:
      - Data Objects
  - name: <a href='/docs/api/endpoints/data_objects/objects/get_list_data_objects'>/data_objects/objects/{type_name}</a>
    description: Liste objetos de dados para um tipo.
    tags:
      - Data Objects
  - name: <a href='/docs/api/endpoints/data_objects/objects/get_data_object'>/data_objects/objects/{type_name}/{external_id}</a>
    description: "Obtenha um objeto de dados, ou substitua, atualize e exclua-o."
    tags:
      - Data Objects
  - name: <a href='/docs/api/endpoints/data_objects/object_relationships/get_list_object_relationships'>/data_objects/objects/{type_name}/{external_id}/object_relationships</a>
    description: "Liste, crie, substitua, atualize e exclua relacionamentos entre objetos."
    tags:
      - Data Objects
  - name: <a href='/docs/api/endpoints/data_objects/user_relationships/get_list_user_relationships'>/data_objects/objects/{type_name}/{external_id}/user_relationships</a>
    description: Liste os relacionamentos de usuário para um objeto de dados.
    tags:
      - Data Objects
  - name: <a href='/docs/api/endpoints/data_objects/user_relationships/post_create_user_relationship'>/data_objects/objects/{type_name}/{external_id}/users</a>
    description: "Crie, substitua, atualize e exclua relacionamentos entre usuários e objetos."
    tags:
      - Data Objects
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns'>/campaigns/trigger/send</a>
    description: Envie mensagens únicas e imediatas para usuários designados por meio de entrega disparada pela API.
    tags:
      - Send Messages
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases'>/canvas/trigger/send</a>
    description: Envie mensagens de Canvas por meio de entrega disparada pela API.
    tags:
      - Send Messages
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_send_messages'>/messages/send</a>
    description: Envie mensagens únicas e imediatas para usuários designados por meio da API da Braze.
    tags:
      - Send Messages
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_create_send_ids'>/sends/id/create</a>
    description: "Crie IDs de envio para enviar mensagens e rastrear o desempenho das mensagens de forma programática, sem a criação de Campaigns para cada envio."
    tags:
      - Send Messages
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_send_transactional_message'>/transactional/v1/campaigns/{CAMPAIGN_ID}/send</a>
    description: Envie mensagens transacionais únicas e imediatas para um usuário designado.
    tags:
      - Send Messages
  - name: <a href='/docs/api/device_messaging_api/endpoints/banners/post_sync_banners'>/v1/device-messaging/banners/sync</a>
    description: Recupere Banners elegíveis para um usuário e um conjunto de posicionamentos.
    tags:
      - Device Messaging API
  - name: <a href='/docs/api/device_messaging_api/endpoints/banners/post_track_banner_events'>/v1/device-messaging/banners/track</a>
    description: Registre eventos de impressão e clique para Banners.
    tags:
      - Device Messaging API
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns'>/campaigns/trigger/schedule/create</a>
    description: Envie mensagens de Campaign criadas no dashboard por meio de entrega disparada pela API.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages'>/campaigns/trigger/schedule/delete</a>
    description: Cancele mensagens de Campaign disparadas pela API que você programou anteriormente antes de serem enviadas.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns'>/campaigns/trigger/schedule/update</a>
    description: Atualize Campaigns programadas e disparadas pela API criadas no dashboard.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases'>/canvas/trigger/schedule/delete</a>
    description: Cancele uma mensagem de Canvas que você programou anteriormente via API antes de ser enviada.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases'>/canvas/trigger/schedule/create</a>
    description: Programe o envio de mensagens de Canvas por meio de entrega disparada pela API.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages'>/messages/schedule/update</a>
    description: Atualize mensagens programadas. Esse endpoint aceita atualizações para o parâmetro <code>schedule</code> ou <code>messages</code>, ou ambos.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages'>/messages/schedule/delete</a>
    description: Cancele uma mensagem que você programou anteriormente antes de ela ser enviada.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_messages'>/messages/schedule/create</a>
    description: "Programe o envio de uma Campaign, Canvas ou outra mensagem em um horário determinado."
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases'>/canvas/trigger/schedule/update</a>
    description: Atualize Canvas programados e disparados pela API que você criou no dashboard.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled'>/messages/scheduled_broadcasts</a>
    description: Retorne uma lista JSON de informações sobre Campaigns agendadas e Canvas de entrada entre agora e um <code>end_time</code> designado especificado na solicitação.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/live_activity/update'>/messages/live_activity/update</a>
    description: Atualize uma Live Activity do iOS.
    tags:
      - Live Activity
  - name: <a href='/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status'>/subscription/status/set</a>
    description: Atualize em lote o estado de inscrição de até 50 usuários no dashboard da Braze.
    tags:
      - Subscription Groups
  - name: <a href='/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2'>/v2/subscription/status/set</a>
    description: Atualize em lote o estado de inscrição de até 50 usuários no dashboard da Braze.
    tags:
      - Subscription Groups
  - name: <a href='/docs/api/endpoints/subscription_groups/get_list_user_subscription_group_status'>/subscription/status/get</a>
    description: Obtenha o estado de inscrição de um usuário em um grupo de inscrições.
    tags:
      - Subscription Groups
  - name: <a href='/docs/api/endpoints/subscription_groups/get_list_user_subscription_groups'>/subscription/user/status</a>
    description: Liste e obtenha os grupos de inscrições de um determinado usuário.
    tags:
      - Subscription Groups
  - name: <a href='/docs/api/endpoints/email/post_blacklist'>/email/blacklist</a>
    description: Cancele a inscrição de um usuário no e-mail e marque-o como hard bounce.
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/email/post_remove_hard_bounces'>/email/bounce/remove</a>
    description: Remova endereços de e-mail da sua lista de bounce da Braze.
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/email/post_remove_spam'>/email/spam/remove</a>
    description: Remova endereços de e-mail da sua lista de SPAM da Braze.
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/email/post_email_subscription_status'>/email/status</a>
    description: Defina o estado de inscrição de e-mail para seus usuários.
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/templates/email_templates/post_create_email_template'>/templates/email/create</a>
    description: Crie modelos de e-mail no dashboard da Braze.
    tags:
      - Email Templates
  - name: <a href='/docs/api/endpoints/templates/email_templates/post_update_email_template'>/templates/email/update</a>
    description: Atualize modelos de e-mail no dashboard da Braze.
    tags:
      - Email Templates
  - name: <a href='/docs/api/endpoints/email/get_list_hard_bounces'>/email/hard_bounces</a>
    description: "Obtenha uma lista de endereços de e-mail que tiveram \"hard bounce\" nas suas mensagens de e-mail em um determinado período."
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/email/get_query_unsubscribed_email_addresses'>/email/unsubscribes</a>
    description: Retorne e-mails que cancelaram a inscrição durante o período de <code>start_date</code> a <code>end_date</code>.
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/templates/email_templates/get_see_email_template_information'>/templates/email/info</a>
    description: Obtenha informações sobre seus modelos de e-mail.
    tags:
      - Email Templates
  - name: <a href='/docs/api/endpoints/templates/email_templates/get_list_email_templates'>/templates/email/list</a>
    description: Obtenha uma lista dos modelos de e-mail disponíveis na sua conta Braze.
    tags:
      - Email Templates
  - name: <a href='/docs/api/endpoints/translations/webhook_templates/get_view_source_webhook_template'>/templates/webhook/translations/source</a>
    description: Veja as traduções de origem padrão para um modelo de webhook.
    tags:
      - Webhook Templates
  - name: <a href='/docs/api/endpoints/translations/webhook_templates/get_view_translations_webhook_template'>/templates/webhook/translations</a>
    description: Veja as traduções para um modelo de webhook.
    tags:
      - Webhook Templates
  - name: <a href='/docs/api/endpoints/translations/webhook_templates/put_update_webhook_template'>/templates/webhook/translations</a>
    description: Atualize as traduções para um modelo de webhook.
    tags:
      - Webhook Templates
  - name: <a href='/docs/api/endpoints/export/campaigns/get_campaign_analytics'>/campaigns/data_series</a>
    description: Recupere uma série diária de várias estatísticas de uma Campaign ao longo do tempo.
    tags:
      - Campaigns
  - name: <a href='/docs/api/endpoints/export/campaigns/get_campaign_details'>/campaigns/details</a>
    description: Recupere informações relevantes sobre uma Campaign específica.
    tags:
      - Campaigns
  - name: <a href='/docs/api/endpoints/export/campaigns/get_campaigns'>/campaigns/list</a>
    description: "Exporte uma lista de Campaigns, cada uma incluindo seu nome, identificador de API da Campaign, se é uma Campaign da API e tags associadas à Campaign."
    tags:
      - Campaigns
  - name: <a href='/docs/api/endpoints/export/campaigns/get_send_analytics'>/sends/data_series</a>
    description: Recupere uma série diária de várias estatísticas para um <code>send_id</code> rastreado.
    tags:
      - Campaigns
  - name: <a href='/docs/api/endpoints/export/canvas/get_canvas_analytics'>/canvas/data_series</a>
    description: Exporte dados de séries temporais para um Canvas.
    tags:
      - Canvas
  - name: <a href='/docs/api/endpoints/export/canvas/get_canvas_analytics_summary'>/canvas/data_summary</a>
    description: "Exporte resumos de dados de séries temporais para um Canvas, fornecendo um resumo conciso dos resultados de um Canvas."
    tags:
      - Canvas
  - name: <a href='/docs/api/endpoints/export/canvas/get_canvas_details'>/canvas/details</a>
    description: "Exporte metadados sobre um Canvas, como o nome, a hora de criação, o status atual e muito mais."
    tags:
      - Canvas
  - name: <a href='/docs/api/endpoints/export/canvas/get_canvases'>/canvas/list</a>
    description: "Exporte uma lista de Canvas, incluindo o nome, o identificador de API do Canvas e as tags associadas."
    tags:
      - Canvas
  - name: <a href='/docs/api/endpoints/export/segments/get_segment_analytics'>/segments/data_series</a>
    description: Recupere uma série diária do tamanho estimado de um Segment ao longo do tempo.
    tags:
      - Segments
  - name: <a href='/docs/api/endpoints/export/segments/get_segment_details'>/segments/details</a>
    description: Recupere informações relevantes sobre um Segment.
    tags:
      - Segments
  - name: <a href='/docs/api/endpoints/export/segments/get_segment'>/segments/list</a>
    description: "Exporte uma lista de Segments, cada um incluindo seu nome, identificador de API do Segment e se possui rastreamento de análise de dados ativado."
    tags:
      - Segments
  - name: <a href='/docs/api/endpoints/export/segments/post_cancel_export'>/export/segment/cancel</a>
    description: Cancele exportações para o ID de Segment fornecido.
    tags:
      - Segments
  - name: <a href='/docs/api/endpoints/export/sessions/get_sessions_analytics'>/sessions/data_series</a>
    description: Recupere uma série do número de sessões do seu app em um período designado.
    tags:
      - Sessions
  - name: <a href='/docs/api/endpoints/export/custom_attributes/get_custom_attributes'>/custom_attributes</a>
    description: "Exporte uma lista de atributos personalizados, incluindo o nome, a descrição, o tipo de dados, o comprimento da matriz (se aplicável), o status e as tags associadas."
    tags:
      - Custom Attributes
  - name: <a href='/docs/api/endpoints/export/custom_events/get_custom_events_analytics'>/events/data_series</a>
    description: Recupere uma série do número de ocorrências de um evento personalizado no seu app em um período designado.
    tags:
      - Custom Events
  - name: <a href='/docs/api/endpoints/export/custom_events/get_custom_events_data'>/events</a>
    description: "Exporte uma lista de eventos personalizados, incluindo o nome, a descrição, o status, as tags associadas e a inclusão em relatórios de análise de dados."
    tags:
      - Custom Events
  - name: <a href='/docs/api/endpoints/export/custom_events/get_custom_events'>/events/list</a>
    description: Exporte uma lista de nomes de eventos personalizados registrados para o seu app.
    tags:
      - Custom Events
  - name: <a href='/docs/api/endpoints/templates/content_blocks_templates/post_create_email_content_block'>/content_blocks/create</a>
    description: Crie um Content Block de e-mail.
    tags:
      - Content Blocks
  - name: <a href='/docs/api/endpoints/templates/content_blocks_templates/post_update_content_block'>/content_blocks/update</a>
    description: Atualize um Content Block de e-mail.
    tags:
      - Content Blocks
  - name: <a href='/docs/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information'>/content_blocks/info</a>
    description: Consulte informações do seu Content Block de e-mail existente.
    tags:
      - Content Blocks
  - name: <a href='/docs/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks'>/content_blocks/list</a>
    description: Liste as informações dos seus Content Blocks existentes.
    tags:
      - Content Blocks
  - name: <a href='/docs/api/endpoints/export/kpi/get_kpi_dau_date'>/kpi/dau/data_series</a>
    description: Recupere uma série diária do número total de usuários ativos únicos em cada data.
    tags:
      - KPI
  - name: <a href='/docs/api/endpoints/export/kpi/get_kpi_mau_30_days'>/kpi/mau/data_series</a>
    description: Recupere uma série diária do número total de usuários ativos únicos em uma janela contínua de 30 dias.
    tags:
      - KPI
  - name: <a href='/docs/api/endpoints/export/kpi/get_kpi_daily_new_users_date'>/kpi/new_users/data_series</a>
    description: Recupere uma série diária do número total de novos usuários em cada data.
    tags:
      - KPI
  - name: <a href='/docs/api/endpoints/export/kpi/get_kpi_uninstalls_date'>/kpi/uninstalls/data_series</a>
    description: Recupere uma série diária do número total de desinstalações em cada data.
    tags:
      - KPI
  - name: <a href='/docs/api/endpoints/sms/post_remove_invalid_numbers'>/sms/invalid_phone_numbers/remove</a>
    description: "Remova números de telefone \"inválidos\" da lista de inválidos na Braze. Use isso para revalidar números de telefone após a Braze marcá-los como inválidos."
    tags:
      - SMS
  - name: <a href='/docs/api/endpoints/sms/get_query_invalid_numbers'>/sms/invalid_phone_numbers</a>
    description: "Obtenha uma lista de números de telefone que a Braze marcou como \"inválidos\" em um determinado período."
    tags:
      - SMS
  - name: <a href='/docs/api/endpoints/export/purchases/get_list_product_id'>/purchases/product_list</a>
    description: Retorne uma lista paginada de IDs de produtos.
    tags:
      - Purchases
  - name: <a href='/docs/api/endpoints/export/purchases/get_number_of_purchases'>/purchases/quantity_series</a>
    description: Retorne o número total de compras no seu app em um intervalo de tempo.
    tags:
      - Purchases
  - name: <a href='/docs/api/endpoints/export/purchases/get_revenue_series'>/purchases/revenue_series</a>
    description: Retorne o total de dinheiro gasto no seu app em um intervalo de tempo.
    tags:
      - Purchases
  - name: <a href='/docs/api/endpoints/preference_center/get_create_url_preference_center'>/preference_center/v1/{preferenceCenterExternalId}/url/{userId}</a>
    description: Crie uma URL para uma Central de Preferências.
    tags:
      - Preference Center
  - name: <a href='/docs/api/endpoints/preference_center/get_list_preference_center'>/preference_center/v1/list</a>
    description: Liste as Centrais de Preferências disponíveis.
    tags:
      - Preference Center
  - name: <a href='/docs/api/endpoints/preference_center/get_view_details_preference_center'>/preference_center/v1/{preferenceCenterExternalId}</a>
    description: "Veja os detalhes da sua Central de Preferências, incluindo quando foi criada e atualizada."
    tags:
      - Preference Center
  - name: <a href='/docs/api/endpoints/preference_center/post_create_preference_center'>/preference_center/v1</a>
    description: Crie uma Central de Preferências para permitir que os usuários gerenciem suas preferências de notificação para Campaigns de e-mail.
    tags:
      - Preference Center
  - name: <a href='/docs/api/endpoints/preference_center/put_update_preference_center'>/preference_center/v1/{preferenceCenterExternalId}</a>
    description: Atualize uma Central de Preferências.
    tags:
      - Preference Center
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk'>/catalogs/{catalog_name}/items</a>
    description: Exclua vários itens do seu catálogo.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details'>/catalogs/{catalog_name}/items/{item_id}</a>
    description: Liste um item de catálogo e seus detalhes.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk'>/catalogs/{catalog_name}/items</a>
    description: Edite vários itens do seu catálogo.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk'>/catalogs/{catalog_name}/items</a>
    description: Crie vários itens no seu catálogo.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog'>/catalogs/{catalog_name}</a>
    description: Exclua um catálogo.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog'>/catalogs</a>
    description: Crie um catálogo.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs'>/catalogs</a>
    description: Liste os catálogos em um espaço de trabalho.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item'>/catalogs/{catalog_name}/items/{item_id}</a>
    description: Crie um item em um catálogo.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item'>/catalogs/{catalog_name}/items/{item_id}</a>
    description: Edite um item em um catálogo.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk'>/catalogs/{catalog_name}/items</a>
    description: Retorne vários itens de catálogo e seu conteúdo.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item'>/catalogs/{catalog_name}/items/{item_id}</a>
    description: Exclua um item em um catálogo.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item'>/catalogs/{catalog_name}/items/{item_id}</a>
    description: Substitua um item em um catálogo.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items'>/catalogs/{catalog_name}/items/</a>
    description: Substitua vários itens em um catálogo.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields'>/catalogs/{catalog_name}/fields/</a>
    description: Crie vários campos em um catálogo.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field'>/catalogs/{catalog_name}/fields/{field_name}</a>
    description: Exclua um campo de um catálogo.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections'>/catalogs/{catalog_name}/selections</a>
    description: Crie uma seleção em um catálogo.
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection'>/catalogs/{catalog_name}/selections/{selection_name}</a>
    description: Exclua uma seleção de catálogo.
    tags:
      - Catalogs
  - name: <a href='/docs/post_create_user_account'>/scim/v2/Users</a>
    description: "Crie uma nova conta de usuário do dashboard especificando e-mail, nome e sobrenome, e permissões (para definir permissões no nível da empresa, do espaço de trabalho e da equipe)."
    tags:
      - SCIM
  - name: <a href='/docs/get_see_user_account_information'>/scim/v2/Users/{id}</a>
    description: Procure uma conta de usuário do dashboard existente especificando seu ID de recurso.
    tags:
      - SCIM
  - name: <a href='/docs/post_update_existing_user_account'>/scim/v2/Users/{id}</a>
    description: "Atualize uma conta de usuário do dashboard existente especificando e-mail, nome e sobrenome, e permissões (para definir permissões no nível da empresa, do espaço de trabalho e da equipe)."
    tags:
      - SCIM
  - name: <a href='/docs/delete_existing_dashboard_user'>/scim/v2/Users/{id}</a>
    description: Exclua permanentemente um usuário do dashboard existente.
    tags:
      - SCIM
  - name: <a href='/docs/get_search_existing_dashboard_user_email'>/scim/v2/Users?filter={userName@example.com}</a>
    description: Procure uma conta de usuário do dashboard existente especificando seu e-mail.
    tags:
      - SCIM
  - name: <a href='/docs/api/endpoints/cdi/get_integration_list'>/cdi/integrations</a>
    description: Retorne uma lista de integrações existentes.
    tags:
      - Cloud Data Ingestion
  - name: <a href='/docs/api/endpoints/cdi/post_job_sync'>/cdi/integrations/{integration_id}/sync</a>
    description: Dispare uma sincronização para uma determinada integração.
    tags:
      - Cloud Data Ingestion
  - name: <a href='/docs/api/endpoints/cdi/get_job_sync_status'>/cdi/integrations/{integration_id}/job_sync_status</a>
    description: Retorne uma lista de status de sincronização.
    tags:
      - Cloud Data Ingestion
  - name: <a href='/docs/api/endpoints/sdk_authentication/post_create_sdk_authentication_key'>/app_group/sdk_authentication/create</a>
    description: Crie uma nova chave de autenticação do SDK para o seu app.
    tags:
      - SDK Authentication
  - name: <a href='/docs/api/endpoints/sdk_authentication/get_sdk_authentication_keys'>/app_group/sdk_authentication/keys</a>
    description: Liste as chaves de autenticação do SDK para o seu app.
    tags:
      - SDK Authentication
  - name: <a href='/docs/api/endpoints/sdk_authentication/put_primary_sdk_authentication_key'>/app_group/sdk_authentication/primary</a>
    description: Defina uma chave de autenticação do SDK como a chave primária para o seu app.
    tags:
      - SDK Authentication
  - name: <a href='/docs/api/endpoints/sdk_authentication/delete_sdk_authentication_key'>/app_group/sdk_authentication/delete</a>
    description: Exclua uma chave de autenticação do SDK para o seu app.
    tags:
      - SDK Authentication
  - name: <a href='/docs/api/endpoints/media_library/manage_assets/create'>/media_library/create</a>
    description: Faça upload de um ativo para a biblioteca de mídia.
    tags:
      - Media Library
---