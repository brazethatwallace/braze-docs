---
nav_title: Início
article_title: O que há de novo na Braze
description: "As notas de versão da Braze são publicadas mensalmente para que você possa se manter atualizado sobre os principais lançamentos de produtos, melhorias contínuas de produtos, parcerias da Braze, alterações significativas no SDK e descontinuações de recursos."
page_order: 0
search_rank: 1
page_type: reference

---

# O que há de novo na Braze {#whats-new-in-braze}

{% alert tip %}
Para saber mais sobre qualquer uma das atualizações listadas nesta página, entre em contato com o gerente da sua conta ou [abra um ticket de suporte]({{site.baseurl}}/user_guide/administer/personal/braze_support). Confira também nossos [Changelogs do SDK]({{site.baseurl}}/developer_guide/changelogs) para mais informações sobre nossas versões mensais do SDK, melhorias e alterações significativas.
{% endalert %}

{% details 20 de agosto de 2026 %}

## Lançamento de 20 de agosto de 2026 {#august-20-2026-release}

### Dados e relatórios {#data-reporting}

#### Editor SQL da Ingestão de Dados na Nuvem {#cloud-data-ingestion-sql-editor}

{% multi_lang_include release_type.md release="General availability" %}

O [editor SQL]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sql_editor) permite criar e editar sincronizações de Ingestão de Dados na Nuvem (CDI) escrevendo uma consulta SQL em qualquer tabela ou visualização no seu data warehouse, em vez de construir e manter uma tabela dedicada específica para a Braze. Ele está disponível para todos os tipos de dados de sincronização em todas as fontes de data warehouse CDI: Snowflake, Redshift, BigQuery, Databricks e Fabric.

#### Mapeador visual da Ingestão de Dados na Nuvem {#cloud-data-ingestion-visual-mapper}

{% multi_lang_include release_type.md release="Beta" %}

O [mapeador visual]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/visual_mapper) permite criar uma sincronização de Ingestão de Dados na Nuvem (CDI) mapeando as colunas de uma tabela existente do data warehouse para campos da Braze diretamente no dashboard, sem necessidade de SQL ou tabela dedicada. Esta versão beta suporta sincronizações de atributos de usuário em todas as fontes de data warehouse CDI. O mapeador visual e o editor SQL são complementares: use o mapeador visual para mapeamento direto de coluna para campo e o editor SQL para casos avançados como transformações, junções e lógica condicional.

#### Ingestão de Dados na Nuvem para Google Cloud Storage e Azure Blob Storage {#cloud-data-ingestion-for-google-cloud-storage-and-azure-blob-storage}

{% multi_lang_include release_type.md release="General availability" %}

A Ingestão de Dados na Nuvem (CDI) suporta duas novas fontes de armazenamento de arquivos: Google Cloud Storage, disponível agora, e Azure Blob Storage, chegando na semana de 31 de agosto de 2026. Ambas as fontes funcionam como a fonte existente do Amazon S3 — a Braze ingere os arquivos assim que são gravados no bucket ou contêiner — para que os clientes no Google Cloud ou Azure tenham a mesma velocidade e confiabilidade sem replicar arquivos no S3 ou construir uma integração personalizada.

#### Ingestão de Dados na Nuvem para o BrazeAI Decisioning Studio {#cloud-data-ingestion-to-brazeai-decisioning-studio}

{% multi_lang_include release_type.md release="Early access" %}

A Ingestão de Dados na Nuvem (CDI) agora pode sincronizar dados do data warehouse diretamente para o BrazeAI Decisioning Studio para clientes que usam ambos os produtos, para que você possa trazer dados além do seu espaço de trabalho da Braze para aprendizado por reforço e tomada de decisão por IA sem construir jobs ETL personalizados. Esta versão de acesso antecipado suporta fontes Snowflake, com fontes adicionais de data warehouse chegando em breve.

### BrazeAI<sup>TM</sup>

#### O Operator pode navegar pelo dashboard para você {#operator-can-navigate-the-dashboard-for-you}

{% multi_lang_include release_type.md release="General availability" %}

O [Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#navigate-the-dashboard) pode navegar para uma página diferente do dashboard para concluir sua solicitação. Quando um prompt precisa de uma parte diferente do dashboard, o Operator identifica o destino, propõe a navegação e leva você até lá antes de continuar seu trabalho.

Isso permite que o Operator encadeie trabalhos de várias etapas a partir de um único prompt. Por exemplo, se você pedir ao Operator na página inicial para configurar as definições do editor de arrastar e soltar para corresponder às diretrizes da sua marca, ele navega até as configurações de e-mail relevantes e continua ajudando você a partir daí.

Por padrão, o Operator pede sua aprovação antes de navegar para uma nova página. Para permitir que o Operator navegue sem esperar sua aprovação a cada vez, ative [Aprovar ações automaticamente]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions#auto-approve-actions).

#### O Operator pode atuar em mais páginas do dashboard {#operator-can-act-on-more-dashboard-pages}

{% multi_lang_include release_type.md release="General availability" %}

O [Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities) pode concluir trabalhos em páginas adicionais do dashboard quando você descreve o resultado em linguagem natural. Os exemplos incluem a criação de relatórios e dashboards, trabalho a partir de páginas de lista de modelos de e-mail e Content Blocks, importação ou gerenciamento de usuários, criação de previsões e atualização de mais superfícies de administração e configurações.

Por exemplo, na página do Criador de relatórios, peça ao Operator para criar um relatório que mostre o engajamento de SMS do espaço de trabalho nos últimos 30 dias.

Para uma cobertura representativa, consulte [O que você pode fazer com o Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities). Pergunte ao Operator na página em que você está para obter a resposta mais atualizada.

#### O Operator pode criar e editar Canvas {#operator-can-create-and-edit-canvases}

{% multi_lang_include release_type.md release="General availability" %}

O [Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities) pode criar um rascunho de Canvas a partir de uma descrição em linguagem natural e editar um Canvas existente da mesma forma. Descreva a jornada que você deseja — critérios de entrada, atrasos e mensagens — e o Operator monta um rascunho que você revisa e refina antes de lançar.

Por exemplo, peça ao Operator para criar uma jornada de carrinho abandonado que espere uma hora após o abandono do carrinho, envie um lembrete por e-mail e, em seguida, um push após 24 horas se o usuário ainda não tiver comprado.

Para etapas suportadas e limitações, consulte [O que você pode fazer com o Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities).

#### Atualizações da etapa do Otimizador de Conteúdo {#content-optimizer-step-updates}

{% multi_lang_include release_type.md release="Beta" %}

A etapa do [Otimizador de Conteúdo]({{site.baseurl}}/user_guide/brazeai/content_optimizer) inclui as seguintes atualizações:

- **Estados da etapa:** As etapas do Otimizador de Conteúdo mostram se estão em **Learning**, **Optimizing** ou **Action Recommended**, para que você possa ver onde cada etapa se encontra.
- **Verificações de configuração pré-lançamento:** O Otimizador de Conteúdo verifica configurações incorretas importantes enquanto você elabora o rascunho, para que você possa identificar problemas antes de lançar.
- **Rastrear qual combinação cada usuário recebeu:** Uma nova Liquid tag e visibilidade no perfil do usuário permitem rastrear qual combinação de variantes cada usuário recebeu, de ponta a ponta.
- **Novos dados do Currents:** Três novos tipos de evento permitem que você extraia dados do Otimizador de Conteúdo para o seu warehouse: `users.canvas.costep.Send`, `users.canvas.costep.Conversion` e `contentoptimizer.ComponentStore`.

Para detalhes de configuração, consulte [Etapa do Otimizador de Conteúdo]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/content_optimizer_step).

### Orquestração {#orchestration}

#### Horário de silêncio do espaço de trabalho {#workspace-quiet-hours}

{% multi_lang_include release_type.md release="Early access" %}

O [horário de silêncio do espaço de trabalho]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/workspace_quiet_hours) permite definir uma janela padrão de horário de silêncio para um canal de envio de mensagens em todo o seu espaço de trabalho. Cada Campaign e Canvas nesse canal respeita a janela no fuso horário local de cada destinatário. Você pode manter o padrão do espaço de trabalho ou optar por não usá-lo e aplicar uma janela específica da Campaign ou Canvas.

As mensagens que seriam enviadas durante a janela são retidas para entrega posterior ou abortadas, dependendo do tipo de campanha. O horário de silêncio do espaço de trabalho nunca modifica o conteúdo da mensagem.

#### Alertas de limite do Canvas {#canvas-threshold-alerts}

{% multi_lang_include release_type.md release="Early access" %}

Os [alertas de limite do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/canvas_threshold_alerts) notificam você quando as entradas de usuários ou mensagens enviadas ficam fora do volume esperado. Defina um limite, escolha com que frequência a Braze verifica (a cada 3 a 12 horas, ou a cada 24 horas) e receba notificações por e-mail, webhook ou ambos quando uma regra for atendida. Você pode criar vários alertas para o mesmo Canvas, inclusive em rascunhos — o alerta começa a verificar após o lançamento do Canvas.

#### Atribuição automática de equipe {#automatic-team-assignment}

{% multi_lang_include release_type.md release="General availability" %}

Para usuários com permissões apenas no nível de equipe, a Braze pode atribuir uma [equipe]({{site.baseurl}}/user_guide/administer/global/user_management/teams#automatic-team-assignment) automaticamente durante a criação do objeto.

### Canais e pontos de contato {#channels-touchpoints}

#### Depurador de Connected Content {#connected-content-debugger}

{% multi_lang_include release_type.md release="Early access" %}

O [depurador de Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/debugger) mostra a solicitação e a resposta ao vivo para cada chamada de Connected Content em **Preview & Test**, para que você possa verificar seu endpoint, cabeçalhos e Liquid tags antes de lançar uma Campaign ou Canvas. Abra **View details** para inspecionar o URL, método, código de status, cabeçalhos de solicitação e resposta, carga útil, duração e se a resposta foi servida do cache.

Durante o acesso antecipado, o depurador está disponível para Content Cards, e-mail, mensagens no app, push, SMS/MMS/RCS, webhooks e WhatsApp.

#### Pesquisas em mensagens no app e landing pages {#in-app-message-and-landing-page-surveys}

{% multi_lang_include release_type.md release="General availability" %}

As pesquisas da Braze coletam feedback em [mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys) e [landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys) que você pode analisar e usar em mensagens de acompanhamento.

#### Mensagem de carrossel do KakaoTalk {#kakaotalk-carousel-message}

{% multi_lang_include release_type.md release="General availability" %}

Uma [mensagem de carrossel do KakaoTalk]({{site.baseurl}}/user_guide/channels/kakaotalk/create_kakaotalk_message#step-2-compose-your-kakaotalk-message) inclui até seis cartões roláveis. Cada cartão tem uma imagem, cabeçalho, mensagem, URL de website opcional e pelo menos um botão.

#### Melhorias no WhatsApp Template Builder {#whatsapp-template-builder-improvements}

{% multi_lang_include release_type.md release="General availability" %}

O [WhatsApp Template Builder]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder) suporta mais caminhos de criação e opções de modelo:

- **Criar modelos ao construir Campaigns e Canvas:** Crie um novo modelo de WhatsApp diretamente no criador em vez de apenas selecionar modelos existentes do Conteúdo.
- **Mensagens de resposta em carrossel:** Crie layouts de carrossel como mensagens de resposta, não apenas como modelos de saída.
- **Novos tipos de modelo: Utility e Flow:** O Template Builder suporta modelos Utility e modelos Flow, inclusive quando você cria modelos a partir de Campaigns, Canvas ou da experiência independente de Modelos de conteúdo.

#### Blocos de formulário personalizados e ponte JavaScript para landing pages {#custom-form-blocks-and-javascript-bridge-for-landing-pages}

{% multi_lang_include release_type.md release="General availability" %}

As landing pages agora suportam [blocos de formulário personalizados]({{site.baseurl}}/user_guide/messaging/landing_pages/custom_form_blocks) e uma [ponte JavaScript]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge), para que você possa capturar entradas de formulário personalizadas e sincronizar eventos e atributos do lado do cliente por meio da sua experiência de landing page.

#### Formulários de landing page com várias etapas {#multi-step-landing-page-forms}

{% multi_lang_include release_type.md release="General availability" %}

Os [formulários de landing page com várias etapas]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/multi_step_forms) permitem dividir um formulário longo em várias etapas em uma única linha de **Formulário**, com uma etapa de confirmação integrada após o envio.

#### Bloco Gerenciar inscrições para landing pages {#manage-subscriptions-block-for-landing-pages}

{% multi_lang_include release_type.md release="General availability" %}

O bloco [Gerenciar inscrições]({{site.baseurl}}/user_guide/messaging/landing_pages/manage_subscriptions) permite que os usuários visualizem, optem por participar e atualizem grupos de inscrições de e-mail em uma landing page.

### Parcerias {#partnerships}

#### Audience Sync: Google Data Manager API

{% multi_lang_include release_type.md release="Early access" %}

O [Audience Sync para Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync) suporta a Google Data Manager API em acesso antecipado.

#### Amazon Bedrock - Provedor de modelos de IA {#amazon-bedrock-ai-model-provider}

O [Amazon Bedrock](https://aws.amazon.com/bedrock/) é um serviço AWS totalmente gerenciado que fornece acesso a modelos de base de empresas líderes de IA por meio de uma API unificada, para que as marcas possam construir e escalar aplicações de IA generativa na AWS.

Para saber mais, consulte [Amazon Bedrock]({{site.baseurl}}/partners/amazon_bedrock).

#### Bynder - Orquestração de mensagens - CMS e DAM {#bynder-message-orchestration-cms-and-dam}

O [Bynder](https://www.bynder.com) é uma plataforma de gerenciamento de ativos digitais (DAM) que ajuda os clientes a criar, gerenciar, encontrar e distribuir ativos digitais aprovados (imagens, vídeos e outros criativos) a partir de uma única fonte de verdade. Quando integrado à Braze, a extensão Universal Compact View (UCV) do Google Chrome do Bynder permite que os profissionais de marketing pesquisem e selecionem ativos do Bynder sem sair do dashboard da Braze. Insira links para esses ativos diretamente em Campaigns e Canvas.

Para saber mais, consulte [Bynder]({{site.baseurl}}/partners/bynder).

#### Multiplied Media - Personalização de mensagens - Conteúdo visual e interativo {#multiplied-media-message-personalization-visual-and-interactive-content}

O [Multiplied Media](https://multiplied.media) é um estúdio de criação e automação que usa seus dados de CRM para criar imagens, GIFs e vídeos personalizados — um ativo único para cada cliente. A integração entre o Multiplied Media e a Braze permite enviar essa mídia por e-mail, notificações por push, mensagens no app, Content Cards e WhatsApp.

Para saber mais, consulte [Multiplied Media]({{site.baseurl}}/partners/multiplied_media).

### SDK

As seguintes atualizações do SDK foram lançadas. Para mais detalhes, consulte os [Changelogs do SDK]({{site.baseurl}}/developer_guide/changelogs).

#### Atualizações significativas do SDK {#sdk-breaking-updates}

As atualizações mais recentes do SDK foram lançadas. As atualizações significativas estão listadas na seção de atualizações do SDK; todas as outras atualizações podem ser encontradas nos changelogs correspondentes do SDK.

- Unity SDK 12.0.0
    - Atualiza a bridge nativa do iOS [do Braze Swift SDK 14.1.0 para 18.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/14.1.0...18.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Atualiza a bridge nativa do Android [do Braze Android SDK 42.2.0 para 43.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v42.2.0...v43.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- Flutter SDK 22.0.0
    - Atualiza a bridge nativa do Android [do Braze Android SDK 42.3.1 para 43.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v42.3.1...v43.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Atualiza a bridge nativa do iOS [do Braze Swift SDK 17.0.0 para 18.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/17.0.0...18.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- Swift SDK 18.0.0-18.1.0
    - Renomeia `Braze.Ecommerce.ProductViewedEvent.typeIdentifiers` para `type` nas superfícies de API Swift e Objective-C.
    Renomeia os eventos de atualização push-to-start de Live Activities em `Braze.LiveActivities.UpdateEvent.ActivityType`, que são emitidos ao usar `Braze.LiveActivities.subscribeToStateUpdates(_:)`:
        - `pushToStartOptedOut` para `pushToStartUnregistered`
        - `pushToStartOptOutFlushed` para `pushToStartUnregisterFlushed`

#### Resumo dos recursos e correções recentes do SDK {#summary-of-recent-sdk-features-and-fixes}

- **Swift SDK v18.1.0:** Adiciona métodos de logout de token por push, além do método de logout de push existente, para suportar casos de uso adicionais de logout. Também atualiza o tipo de evento de eCommerce.
- **Flutter SDK v22.0.0:** Atualiza a bridge nativa para herdar funcionalidades dos SDKs Android e Swift.
- **Unity SDK v12.0.0:** Atualiza a bridge nativa para herdar funcionalidades dos SDKs Android e Swift.

Para mais detalhes, consulte os [Changelogs do SDK]({{site.baseurl}}/developer_guide/changelogs).
{% enddetails %}
{% details 23 de julho de 2026 %}

## Lançamento de 23 de julho de 2026 {#july-23-2026-release}

### Dados e relatórios

#### Dashboard de Diagnóstico de Mensagens {#messaging-diagnostics-dashboard}

{% multi_lang_include release_type.md release="General availability" %}

O [dashboard de Diagnóstico de Mensagens]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) fornece uma visão geral dos resultados de envio de mensagens, permitindo que você identifique tendências e diagnostique possíveis problemas na sua configuração de envio de mensagens. Esse dashboard pode ajudá-lo a entender por que as mensagens das suas Campaigns ou Canvas podem não ter sido enviadas como esperado. Entre em contato com o seu gerente de sucesso do cliente para obter acesso ao recurso.

#### Mapeador de eventos personalizados na importação por CSV {#csv-custom-events-mapper}

{% multi_lang_include release_type.md release="General availability" %}

O [fluxo de importação por CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import#about-csv-import) para eventos personalizados agora inclui um mapeador que permite mapear nomes de eventos e cabeçalhos de propriedades de eventos para campos da Braze antes da importação. Essa atualização alinha a experiência de eventos personalizados com o fluxo de atributos personalizados e reduz a necessidade de reformatar arquivos antes do upload. O fluxo inclui o upload de um CSV, o mapeamento de campos e eventos obrigatórios, o mapeamento de propriedades de eventos e, em seguida, a seleção de preferências de direcionamento antes da importação. Se o seu arquivo já corresponder ao formato esperado, você pode continuar pelo fluxo sem fazer alterações no mapeamento.

#### O armazenamento gratuito de catálogos agora suporta até 500 MB {#catalogs-free-storage-now-supports-up-to-500-mb}

{% multi_lang_include release_type.md release="General availability" %}

A versão gratuita dos [catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs/create#tiers) agora suporta até 500 MB de armazenamento em todos os arquivos CSV.

### BrazeAI<sup>TM</sup>

#### O Operator agora pode atualizar páginas de configurações para você {#operator-can-now-update-settings-pages-for-you}

{% multi_lang_include release_type.md release="General availability" %}

O [Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities) agora pode fazer alterações diretamente em mais páginas de configurações, para que você possa descrever uma alteração em linguagem natural em vez de navegar pelas telas de configuração. As páginas suportadas incluem:

- Horário de silêncio
- Configurações de push
- Limites de taxa de envio de mensagens
- Regras de envio de mensagens e fluxos de aprovação sempre ativos
- Outros identificadores e limites de API
- Informações de contato

Por exemplo, na página de Horário de silêncio, peça ao Operator para definir o horário de silêncio das 21h às 8h para SMS.

#### Servidor MCP remoto da Braze {#remote-braze-mcp-server}

{% multi_lang_include release_type.md release="Early access" %}

O [servidor MCP da Braze]({{site.baseurl}}/user_guide/brazeai/mcp_server) é uma conexão hospedada remotamente que permite conectar agentes de IA como Claude, ChatGPT, Cursor, VSCode, Codex, Google Antigravity e Claude Code diretamente à Braze. Por meio de linguagem natural, os agentes podem ler análises de Campaigns, Canvas e Segments, atributos personalizados, eventos, KPIs e catálogos, além de criar ou atualizar modelos de e-mail, Content Blocks e ativos da biblioteca de mídia. Nenhuma PII de perfil de usuário é exposta.

Para conectar, cole um único URL de endpoint no seu cliente MCP — `https://mcp.braze.com/mcp` para US ou `https://mcp.braze.eu/mcp` para EU — e faça login com OAuth, incluindo SSO. O servidor é iniciado com as ferramentas disponíveis.

### Orquestração

#### Escopo de público por equipes {#teams-audience-scoping}

{% multi_lang_include release_type.md release="General availability" %}

A configuração de público das [Equipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams) agora suporta múltiplos filtros.

### Canais e pontos de contato

#### Escala de avaliação de pesquisa para mensagens no app e landing pages {#survey-rating-scale-for-in-app-messages-and-landing-pages}

{% multi_lang_include release_type.md release="Early access" %}

Adicione uma escala de avaliação numérica a um bloco de formulário em [pesquisas de landing page]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys#rating-scale) e [pesquisas de mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys#rating-scale) para capturar sentimento, satisfação e probabilidade de recomendação sem nenhum código personalizado. Três intervalos são suportados: 1–10, 1–5 e 0–10 (o intervalo padrão de NPS).

#### Modelos de oferta por tempo limitado do WhatsApp {#whatsapp-limited-time-offer-templates}

{% multi_lang_include release_type.md release="General availability" %}

Os [modelos de oferta por tempo limitado do WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/message_and_image_formats#limited-time-offer-templates) exibem uma oferta promocional com prazo determinado e uma contagem regressiva opcional conforme a oferta se aproxima da expiração. Use esse layout para promoções com prazo definido, como vendas sazonais ou ofertas personalizadas com base em um atributo do usuário.

#### Upgrade de versão do SDK da Shopify por autoatendimento {#shopify-self-serve-sdk-version-upgrade}

{% multi_lang_include release_type.md release="General availability" %}

Novos clientes da [Shopify]({{site.baseurl}}/partners/ecommerce/shopify) são provisionados nas versões mais recentes do Braze Web SDK e JavaScript SDK durante a configuração. Clientes existentes podem visualizar sua versão atual do SDK nas configurações de integração, receber notificações quando uma versão mais recente estiver disponível e fazer upgrades por autoatendimento nas configurações de integração.

#### Editor de HTML para Banners {#html-editor-for-banners}

{% multi_lang_include release_type.md release="General availability" %}

Ao compor um Banner, agora você pode criá-lo [usando o editor de HTML]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#compose-a-banner). O editor de HTML é ideal para equipes que já mantêm seus próprios modelos HTML ou desejam controle total sobre a marcação e o estilo dos Banners. Você pode escrever ou colar HTML personalizado diretamente no editor.

#### Substituir um arquivo na biblioteca de mídia {#replace-a-file-in-the-media-library}

{% multi_lang_include release_type.md release="General availability" %}

Agora você pode [substituir o arquivo de um ativo existente na biblioteca de mídia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#replace-a-file) mantendo seu URL e ID de ativo estáveis. Como o URL não muda, qualquer Campaign, Canvas, Content Block ou modelo que referencia esse ativo reflete automaticamente o arquivo atualizado, então você não precisa fazer upload novamente ou vincular novamente em todos os lugares onde ele é usado.

#### Visualização em grade para a biblioteca de mídia {#grid-view-for-the-media-library}

{% multi_lang_include release_type.md release="General availability" %}

A biblioteca de mídia e bibliotecas de modelos selecionadas agora oferecem uma visualização em grade junto com a visualização em lista existente. A visualização em grade exibe os ativos como miniaturas com metadados essenciais (nome, tipo, última modificação), tornando mais rápido encontrar imagens e criativos visualmente em vez de pelo nome do arquivo. A filtragem e a busca funcionam da mesma forma em ambas as visualizações.

#### Suporte a prévia compartilhável para mais canais {#shareable-preview-support-for-more-channels}

{% multi_lang_include release_type.md release="General availability" %}

A [prévia compartilhável]({{site.baseurl}}/user_guide/channels/email/html_editor#step-3b-preview-and-test-your-message) agora suporta os seguintes canais adicionais:

- SMS, MMS e RCS
- WhatsApp
- Push
- Content Cards
- LINE

A partir de uma Campaign ou mensagem, gere um link e compartilhe-o com revisores que não têm acesso ao dashboard da Braze — equipe de marca, jurídico ou uma agência externa, por exemplo. Os destinatários abrem o link em qualquer navegador para ver a mensagem renderizada como um cliente veria, incluindo qualquer personalização de teste.

#### API de atualização de credenciais de push {#push-credentials-update-api}

{% multi_lang_include release_type.md release="General availability" %}

Agora você pode atualizar credenciais de push programaticamente com o [endpoint de atualização de credenciais de push]({{site.baseurl}}/api/endpoints/apps/post_update_push_credential). Cada solicitação atualiza um app e uma plataforma (`apple`, `firebase`, `huawei` ou `kindle`) e aceita cargas úteis de credenciais como valores codificados em Base64. Isso ajuda equipes a gerenciar grandes portfólios de apps e políticas de rotação de credenciais sem depender de uploads manuais no dashboard.

### Parcerias

#### Refiner - Pesquisas {#refiner-surveys}

O [Refiner](https://refiner.io) é uma plataforma de pesquisas no app para apps SaaS e móveis. Ele permite que equipes de produto e voz do cliente lancem pesquisas direcionadas no app e coletem continuamente NPS, CSAT, CES, feedback de produto e dados zero-party dos usuários.

#### Stayfilm - Conteúdo visual e interativo {#stayfilm-visual-and-interactive-content}

O [Stayfilm](https://www.stayfilm.com/) é uma REST API para produção automatizada e personalizada de vídeos em escala. A plataforma integra dados, imagens, texto, trilhas sonoras, narração e efeitos visuais para gerar conteúdo de vídeo personalizado para eCommerce, marketplaces, fluxos de trabalho de CRM e campanhas de marketing.

#### Validity - Dados e análises {#validity-data-and-analytics}

O [Validity Everest](https://www.validity.com/everest/) é uma plataforma de entregabilidade de e-mail que ajuda você a medir a colocação na caixa de entrada e proteger sua reputação de envio. A integração entre a Braze e a Validity sincroniza sua lista de sementes do Everest com a Braze, semeia automaticamente Campaigns e Canvas qualificados e puxa métricas de engajamento de volta para o Validity Inbox para que você possa comparar a colocação baseada em sementes com o engajamento real dos assinantes.

### SDK

As seguintes atualizações do SDK foram lançadas. Para mais detalhes, consulte os [Changelogs do SDK]({{site.baseurl}}/developer_guide/changelogs).

#### Atualizações significativas do SDK

As atualizações mais recentes do SDK foram lançadas. As atualizações significativas estão listadas na seção de atualizações do SDK; todas as outras atualizações podem ser encontradas nos changelogs correspondentes do SDK.

- [Android SDK 43.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v43.0.0)
    - Adiciona os métodos `unregisterPush` e logout.
    - Adiciona campos adicionais aos eventos de eCommerce.
    - Adiciona backoff exponencial para carregamento de imagens de notificações por push.
- [Swift SDK 17.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Adiciona campos adicionais aos eventos de eCommerce.
    - Torna os estados de dados previsíveis após a inicialização.
    - Adiciona acessores não bloqueantes para identificadores de dispositivo e usuário.
    - Remove a API de atualização push-to-start descontinuada em `Braze.LiveActivities`.
- [Web SDK 6.10.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
    - Adiciona os métodos `unregisterPush` e logout.
    - Adiciona campos adicionais aos eventos de eCommerce.
    - Corrige um problema de Banner e Content Card relacionado a atualizações redundantes na inicialização.
    - Adiciona um método público para dispensa de Banner.
- [Flutter SDK 21.0.0](https://github.com/braze-inc/braze-flutter-sdk/releases/tag/v21.0.0)
    - Atualiza a bridge nativa do iOS.
    - Remove métodos descontinuados.
    - Atualiza os handlers `changeUser`, `enableSDK` e `disableSDK` para retornar resultados de conclusão.
- [Expo SDK 5.2.0](https://github.com/braze-inc/braze-expo-plugin/releases/tag/v5.2.0)
    - Atualiza o app de exemplo para o Expo SDK 56.
- [React Native SDK 22.0.0](https://www.npmjs.com/package/@braze/react-native-sdk/v/22.0.0)
    - Adiciona suporte para dispensas de Banner.
    - Inclui atualizações de bindings.

{% enddetails %}
{% details 25 de junho de 2026 %}

## Lançamento de 25 de junho de 2026 {#june-25-2026-release}

### Dados e relatórios

#### Atualização do nome da métrica para Content Cards e Banners {#metric-name-update-for-content-cards-and-banners}

A métrica _Unique Recipients_ foi renomeada para _Unique Daily Impressions_ para Content Cards e Banners. _Unique Daily Impressions_ refere-se ao número recebido da Braze e é baseado no `user_id`. As impressões diárias únicas são contadas no nível da Campaign ou da etapa do Canvas. Para mais detalhes, consulte o [Glossário de métricas]({{site.baseurl}}/user_guide/analytics/metrics_glossary).

#### Exclusão de usuários {#user-deletion}

{% multi_lang_include release_type.md release="General availability" %}

A [exclusão de usuários]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users) permite gerenciar seu banco de dados removendo perfis que não são mais necessários, foram criados por engano ou precisam ser excluídos por conformidade (como GDPR ou CCPA).

#### Exclusões de pontos de dados {#data-point-exclusions}

{% multi_lang_include release_type.md release="General availability" %}

Os [eventos recomendados de eCommerce]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events) não contam mais para pontos de dados faturáveis. Você pode adotar os eventos de eCommerce da Braze (`ecommerce.product_viewed`, `ecommerce.cart_updated`, `ecommerce.checkout_started`, `ecommerce.order_placed`, `ecommerce.order_cancelled`, `ecommerce.order_refunded`) sem consumo de pontos de dados.

#### Guia Histórico de eventos {#event-history-tab}

{% multi_lang_include release_type.md release="General availability" %}

A guia **Event History** nos [perfis de usuário]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles) lista os eventos personalizados e compras do usuário nos últimos 30 dias (até os 100 mais recentes). Use-a para confirmar se uma integração de SDK ou API está enviando eventos conforme esperado, depurar por que um usuário entrou (ou não) em uma Campaign ou Canvas acionado por evento, ou investigar uma escalação de suporte sobre um usuário específico.

#### O Centro de Entregabilidade exibe dados do Microsoft SNDS para clientes do Amazon SES {#deliverability-center-surfaces-microsoft-snds-data-for-amazon-ses-customers}

Para espaços de trabalho que enviam e-mail pelo Amazon SES, o [Centro de Entregabilidade]({{site.baseurl}}/deliverability_center) exibe métricas do Microsoft SNDS para seus IPs de envio dedicados. A Braze preenche retroativamente até 90 dias de dados históricos do SNDS quando esse recurso é ativado para o seu espaço de trabalho.

### BrazeAI<sup>TM</sup>

#### Assistentes BrazeAI unificados no Operator {#unified-brazeai-assistants-in-operator}

Os assistentes BrazeAI independentes encontrados em todo o dashboard estão unificados no [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator), estabelecendo o Operator como o assistente de IA único para assistência de IA generativa voltada para profissionais de marketing em todo o dashboard. Os seguintes assistentes agora passam pelo Operator:

{% multi_lang_include releases/brazeai_operator_legacy_assistants.md %}

Os pontos de entrada existentes permanecem onde cada botão de assistente legado costumava estar. Em vez de abrir um assistente independente, esses pontos de entrada agora abrem o painel do Operator com prompts dinâmicos pré-configurados para sua tarefa. Esses pontos de entrada fornecem uma rota direta para o Operator para que você possa usar esses recursos sem ajustar seus fluxos de trabalho existentes.

#### Suporte do Operator para criação e edição de Campaigns {#operator-support-for-campaign-creation-and-editing}

O [Operator]({{site.baseurl}}/user_guide/brazeai/operator) agora pode criar e editar Campaigns inteiras, não apenas compor mensagens. A partir de um único prompt em linguagem natural ou briefing de campanha, o Operator constrói uma Campaign pronta para revisão de ponta a ponta — compondo a mensagem, agendando a entrega, direcionando um público e atribuindo eventos de conversão — e depois resume o que construiu na etapa de revisão. Anteriormente, o Operator podia compor a mensagem (uma das cinco etapas de criação de Campaign); agora ele tem visibilidade e controle sobre as etapas restantes de Agendamento, Direcionamento, Atribuição e Revisão.

Essa funcionalidade está disponível na página **Campaigns** ou de dentro de qualquer Campaign existente. Como resultado, o Operator pode:

{% multi_lang_include releases/brazeai_operator_campaign_creation_prompts.md %}

#### Suporte do Operator para Content Blocks {#operator-support-for-content-blocks}

O [Operator]({{site.baseurl}}/user_guide/brazeai/operator) agora pode criar e editar [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) — os trechos reutilizáveis que você cria uma vez e referencia em várias mensagens — diretamente a partir de um prompt em linguagem natural. Na página **Content Blocks**, peça ao Operator para criar um novo Content Block do zero ou editar um existente, e o Operator gera ou atualiza o conteúdo para sua revisão.

#### Modelos do Console do agente criados com o Operator {#agent-console-templates-built-with-operator}

Ao criar um agente no **Console do agente**, você pode optar por criar um agente personalizado ou selecionar uma opção em **Create an agent with Operator** para usar o BrazeAI Operator para aplicar um modelo inicial. O Operator pode pré-configurar instruções, campos de saída e contexto para os seguintes modelos iniciais do Console do agente.

Para mais detalhes, consulte [Criar agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator).

#### Melhorias no Console do agente {#agent-console-enhancements}

Você pode fazer o seguinte no [Console do agente]({{site.baseurl}}/user_guide/brazeai/agents):

{% multi_lang_include releases/brazeai_agent_console_enhancements.md %}

#### Editar uma etapa do Otimizador de Conteúdo já lançada {#edit-a-launched-content-optimizer-step}

{% multi_lang_include release_type.md release="Beta" %}

Depois que seu Canvas for lançado, agora você pode [atualizar uma etapa do Otimizador de Conteúdo]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/content_optimizer_step#edit-a-launched-step) para:

{% multi_lang_include messaging/canvas/content_optimizer_launched_step_actions.md %}

### Canais e pontos de contato

#### Dispensas de usuário para Banners {#user-dismissals-for-banners}

{% multi_lang_include release_type.md release="General availability" %}

Você pode permitir que os usuários dispensem manualmente um Banner selecionando **Banner can be dismissed** ao configurar o comportamento de dispensa. Essa opção é benéfica em cenários em que você deseja promover uma venda por tempo limitado para todos os usuários do app, mas permitir que eles dispensem a mensagem se não estiverem interessados.

Consulte [Configurar comportamento de dispensa]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#dismiss-behavior) para detalhes sobre como habilitar a dispensa e personalizar o botão de dispensa.

#### Rastreamento de cliques personalizado para Banners {#custom-click-tracking-for-banners}

{% multi_lang_include release_type.md release="General availability" %}

Para um rastreamento de cliques mais granular para Banners, você pode [atribuir um identificador personalizado]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#step-32-define-on-click-behavior-optional) a cada elemento interativo usando o campo **Identifier for Reporting** no painel de propriedades.

#### Reelegibilidade para Banners {#re-eligibility-for-banners}

Quando a reelegibilidade está habilitada para Campaigns de Banner, os usuários que dispensam um Banner podem se tornar elegíveis novamente após uma janela de espera configurável que começa na dispensa. Se a reelegibilidade não estiver ativada, os usuários que dispensaram permanecem inelegíveis. Para configurar a reelegibilidade, consulte [Configurar reelegibilidade]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#re-eligibility). Observe que as etapas de Banner do Canvas usam as configurações de reentrada do Canvas.

#### Testes A/B de Quick Push {#quick-push-ab-testing}

{% multi_lang_include release_type.md release="General availability" %}

Os testes A/B de Quick Push agora suportam Campaigns de push multiplataforma e etapas do Canvas por meio de grupos de variantes, para que você possa testar variações de mensagens alinhadas para iOS e Android em um único fluxo de trabalho. Para saber mais, consulte [Mensagens push multiplataforma]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/multiple_platform_push#use-cases).

#### BrazeAI<sup>TM</sup> Variant Selection {#brazeai-variant-selection}

{% multi_lang_include release_type.md release="Early access" %}

O BrazeAI<sup>TM</sup> Variant Selection é ativado automaticamente quando você adiciona múltiplas variantes de push, aplica padrões de experimento recomendados e otimiza para a variante de melhor desempenho para melhorar o engajamento. Você pode desativá-lo se precisar enviar imediatamente. Para saber mais, consulte [BrazeAI<sup>TM</sup> Variant Selection]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection).

#### Resultados de envio de teste do WhatsApp {#whatsapp-test-send-results}

Após enviar uma mensagem de teste do WhatsApp, você pode visualizar um [relatório de entrega detalhado]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#step-4-view-test-send-results) diretamente no criador de mensagens. Isso ajuda a confirmar que sua mensagem chegou ao destinatário pretendido e a solucionar falhas antes do lançamento.

### Parcerias

#### Convercus - Dados e análises - Fidelidade {#convercus-data-and-analytics-loyalty}

O [Convercus]({{site.baseurl}}/partners/data_and_analytics/loyalty/convercus) é uma plataforma SaaS de fidelidade e cupons que ajuda marcas e varejistas a aumentar a frequência de compra, o valor do carrinho e as taxas de recompra por meio de programas de fidelidade omnicanal e campanhas de cupons personalizadas.

#### Copy Pastd - Orquestração de mensagens - Modelos {#copy-pastd-message-orchestration-templates}

O [Copy Pastd]({{site.baseurl}}/partners/copy_pastd) Building Blocks é um construtor de e-mails de arrastar e soltar que envia Content Blocks com Liquid e modelos completos diretamente para o seu espaço de trabalho da Braze. Projete uma vez, sincronize com a Braze e reutilize os mesmos componentes em Campaigns, Canvas e fluxos acionados sem reconstruir o HTML a cada vez.

#### Databricks Mosaic - Provedores de modelos de IA {#databricks-mosaic-ai-model-providers}

O [Databricks Mosaic]({{site.baseurl}}/partners/databricks_mosaic) é a plataforma unificada da Databricks para construir, implantar e gerenciar modelos de IA e machine learning em escala na Databricks Data Intelligence Platform.

#### DinMo - Dados e análises - Reverse ETL {#dinmo-data-and-analytics-reverse-etl}

O [DinMo]({{site.baseurl}}/partners/dinmo) é uma plataforma de dados do cliente (CDP) composável que conecta seu data warehouse na nuvem à Braze por meio de Reverse Extract, Transform, Load (ETL). As equipes de marketing podem construir segmentos de público a partir de dados do warehouse, sincronizar atributos e eventos de usuários na Braze e manter os status de inscrição atualizados sem uploads de CSV ou suporte de engenharia.

#### EmailShepherd - Orquestração de mensagens - Modelos {#emailshepherd-message-orchestration-templates}

O [EmailShepherd]({{site.baseurl}}/partners/emailshepherd) é uma plataforma agêntica de criação de e-mails construída sobre seu sistema de design de e-mail que permite que toda a sua equipe de marketing — e agentes de IA — produza e-mails alinhados à marca e prontos para produção sem gargalos. A integração com a Braze publica e-mails aprovados diretamente no seu espaço de trabalho da Braze, para que os profissionais de marketing possam escalar a produção de e-mails na Braze sem sacrificar a consistência da marca.

#### Talkable - Personalização de mensagens - Indicações {#talkable-message-personalization-referrals}

O [Talkable]({{site.baseurl}}/partners/talkable) ajuda marcas de consumo a transformar clientes satisfeitos em um canal de indicação escalável. Com a integração da Braze, os opt-ins de e-mail de marketing capturados em campanhas de indicação do Talkable fluem para a Braze em tempo real, fornecendo à sua equipe o consentimento, o contexto e os dados de campanha necessários para dar boas-vindas, segmentar e engajar cada novo defensor e amigo.

### SDK

#### Atualizações significativas do SDK

As atualizações mais recentes do SDK foram lançadas. As atualizações significativas estão listadas na seção de atualizações do SDK; todas as outras atualizações podem ser encontradas nos changelogs correspondentes do SDK.

{% multi_lang_include releases/sdk/2026_6_25_26_updates.md %}

{% enddetails %}

{% details 28 de maio de 2026 %}

## Lançamento de 28 de maio de 2026 {#may-28-2026-release}

### Dados e relatórios

#### Dashboard de desempenho de push {#push-performance-dashboard}

O [dashboard de desempenho de push]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance?tab=push%20performance#push-performance-dashboard) oferece uma visão única e em nível de canal do engajamento com push, incluindo envios, bounces, entregas e taxas de abertura direta, influenciada e total em uma janela de tempo configurável. Use-o para entender a integridade geral do seu canal de push sem precisar consolidar dados de Campaigns ou Canvas individuais.

#### Campos de geolocalização em seleções de catálogo {#geolocation-fields-in-catalog-selections}

{% multi_lang_include release_type.md release="General availability" %}

Os catálogos agora suportam filtragem baseada em distância com o novo tipo de campo de geolocalização e operadores de seleção de catálogo. Isso ajuda você a criar experiências mais relevantes e baseadas em localização, como mostrar a cada usuário o restaurante mais próximo, filtrar propriedades abertas dentro de 50 km para uma campanha imobiliária ou direcionar lojas próximas a um evento específico. Em vez de aproximar o direcionamento geográfico com códigos de cidade ou região, você pode filtrar itens do catálogo por proximidade a um ponto central, incluindo um atributo Liquid do usuário, como a localização mais recente do usuário. Para saber mais, consulte [Seleções]({{site.baseurl}}/user_guide/data/activation/catalogs/selections).

#### Banner e RCS para o Criador de relatórios {#banner-and-rcs-for-report-builder}

O [Criador de relatórios]({{site.baseurl}}/report_builder) suporta Banner como canal e RCS como subcategoria em SMS, para que você possa medir o desempenho de ambos diretamente em seus relatórios personalizados junto com todos os outros canais da Braze.

#### Ações do evento `ecommerce.cart_updated` {#ecommercecart_updated-event-actions}

O [evento `ecommerce.cart_updated`]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/?tab=ecommerce.cart_updated#code-examples) suporta as ações `add` e `remove` além de `replace`, permitindo que você envie alterações incrementais no carrinho em vez de um snapshot completo do carrinho a cada atualização.

### BrazeAI<sup>TM</sup>

#### Otimizador de Conteúdo para mensagens SMS, MMS e RCS {#content-optimizer-for-sms-mms-and-rcs-messages}

{% multi_lang_include release_type.md release="Beta" %}

Você pode usar o [Otimizador de Conteúdo]({{site.baseurl}}/user_guide/brazeai/content_optimizer) para otimizar ganchos, corpos e CTAs para mensagens SMS, MMS e RCS. O Otimizador de Conteúdo ajuda você a testar e otimizar o conteúdo das mensagens em escala, usando IA para gerar e avaliar grandes volumes de variantes de conteúdo automaticamente.

### Orquestração

#### Fusos horários do espaço de trabalho {#workspace-time-zones}

{% multi_lang_include release_type.md release="General availability" %}

Use os [fusos horários do espaço de trabalho]({{site.baseurl}}/user_guide/administer/global/admin_settings/workspace_time_zone) para definir fusos horários específicos para espaços de trabalho individuais. Isso faz com que Campaigns e Canvas agendados (que não usam horário local ou Intelligent Timing) sejam enviados de acordo com o fuso horário designado do espaço de trabalho, em vez do fuso horário geral da empresa.

Os fusos horários do espaço de trabalho para envio de mensagens estão sendo implementados gradualmente, então talvez você ainda não veja essas configurações no seu dashboard.

### Canais e pontos de contato

#### WhatsApp `inbound_profile_name`

Você pode capturar automaticamente o nome de exibição do WhatsApp de um usuário a partir do webhook de mensagens de entrada do Meta e gravá-lo no perfil do usuário na Braze. Quando uma mensagem de entrada do WhatsApp é recebida, a Braze expõe o nome do perfil como um novo atributo Liquid do WhatsApp, [{% raw %}`{{whats_app.${inbound_profile_name}}}`{% endraw %}]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags), que você pode referenciar em uma etapa de Atualização de usuário do Canvas para salvar em um campo do perfil.

#### Estados de inscrição órfãos do SMS {#orphaned-sms-subscription-states}

A Braze [gerencia automaticamente registros de estado de inscrição órfãos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#how-braze-handles-orphaned-subscription-states) (dados de inscrição armazenados para um número de telefone ou endereço de e-mail não vinculado a nenhum perfil de usuário) para evitar herança não intencional de estado de inscrição. Isso protege os usuários de cenários em que um perfil de usuário recém-criado herda incorretamente o estado de inscrição de um usuário previamente excluído ou não relacionado.

### Parcerias

#### Chord - Plataforma de dados do cliente {#chord-customer-data-platform}

O [Chord](https://www.chord.co/) fornece uma plataforma de dados do cliente que captura e padroniza eventos da sua loja de eCommerce. Quando você conecta o Chord à Braze, atividades de compra, eventos comportamentais e atualizações de identidade fluem para a Braze, para que você possa acionar campanhas e manter os perfis atualizados sem precisar construir esses pipelines por conta própria.

Para saber mais, consulte [Chord]({{site.baseurl}}/partners/chord).

#### Better Email - Modelos {#better-email-templates}

O [Better Email](https://www.betteremail.dev) é uma plataforma colaborativa de criação de e-mails construída em torno de um sistema de design de e-mail. As equipes podem projetar, gerenciar e exportar e-mails prontos para produção a partir de um sistema compartilhado de blocos e estilos, garantindo consistência de marca em escala sem depender de desenvolvedores ou agências.

Para saber mais, consulte [Better Email]({{site.baseurl}}/partners/better_email).

#### DailyPlay - Conteúdo dinâmico {#dailyplay-dynamic-content}

O [DailyPlay](https://dailyplay.ai/) é uma plataforma de gamificação. Use-o para lançar jogos personalizados e de marca e sistemas de recompensa integrados que aprofundam o engajamento e melhoram a retenção.

Para saber mais, consulte [DailyPlay]({{site.baseurl}}/partners/dailyplay).

### SDK

#### Atualizações significativas do SDK

As atualizações mais recentes do SDK foram lançadas. As atualizações significativas estão listadas na seção de atualizações do SDK; todas as outras atualizações podem ser encontradas nos changelogs correspondentes do SDK.

{% multi_lang_include releases/sdk/2026_5_28_26_updates.md %}

{% enddetails %}
{% details 30 de abril de 2026 %}

## Lançamento de 30 de abril de 2026 {#april-30-2026-release}

### Dados e relatórios

#### Adição rápida de usuário para criação de perfil individual {#quick-user-add-for-individual-profile-creation}

{% multi_lang_include release_type.md release="General availability" %}

Agora você pode criar um perfil de usuário individual em **Import Users** selecionando **Quick User Add** e inserindo um e-mail ou ID externo.

Anteriormente, a criação de usuários a partir desse fluxo de trabalho exigia o upload de CSV ou um método de ingestão automatizado.

Para saber mais, consulte [Importação por CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import).

#### Sincronizações CDI sem cópia para acionadores de Canvas {#zero-copy-cdi-syncs-for-canvas-triggers}

{% multi_lang_include release_type.md release="General availability" %}

A CDI agora oferece suporte ao tipo de dados `Canvas triggers` para personalização sem cópia. Você pode acionar Canvas a partir de dados de warehouse ou S3 e transmitir campos de contexto sem persistir esses campos nos perfis de usuário da Braze.

Anteriormente, as sincronizações CDI exigiam que os dados fossem gravados nos perfis da Braze para esse tipo de fluxo de trabalho de personalização.

Para saber mais, consulte [Personalização sem cópia usando CDI]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync).

#### Eventos recomendados para eCommerce {#ecommerce-recommended-events}

{% multi_lang_include release_type.md release="General availability" %}

Os [eventos recomendados para eCommerce]({{site.baseurl}}/user_guide/data/activation/events/recommended_events) cobrem seis etapas da jornada de compra: `product_viewed`, `cart_updated`, `checkout_started`, `order_placed`, `order_cancelled` e `order_refunded`. Quando você envia esses eventos com sucesso, a Braze valida os dados e os disponibiliza para um conjunto crescente de recursos da plataforma.

### Currents e Datashare {#currents-and-datashare}

#### Novas atualizações de Banner e WhatsApp no Currents {#new-banner-and-whatsapp-currents-updates}

{% multi_lang_include release_type.md release="General availability" %}

O Currents e o Datashare agora incluem um novo evento `Banner.Dismiss` e campos adicionais para eventos existentes do WhatsApp.

Anteriormente, esses eventos de dispensa de Banner e campos do WhatsApp não estavam disponíveis nos dados de exportação.

Para saber mais, consulte o [changelog do Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs).

### Orquestração

#### Traduções multilíngues {#multi-language-translations}

{% multi_lang_include release_type.md release="General availability" %}

Componha [mensagens multilíngues]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) com uma configuração rápida e única de localidade que não requer código complexo e permite que você envie para todos os seus mercados com confiança.

#### Migração de permissões granulares {#granular-permissions-migration}

{% multi_lang_include release_type.md release="General availability" %}

Gerenciar quem pode acessar sua conta e executar ações específicas é fundamental tanto para a segurança quanto para a eficiência operacional. Para dar a você mais controle, a Braze está introduzindo [permissões granulares]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/granular_permissions_migration), uma forma mais flexível e precisa de gerenciar o acesso dos usuários em toda a sua conta.

#### Componente Send to Destination do Canvas {#send-to-destination-canvas-component}

{% multi_lang_include release_type.md release="General availability" %}

A [etapa Send to Destination]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination) permite enviar usuários de um Canvas para outro. Por exemplo, se você tem dois Canvas que compartilham mensagens de ofertas promocionais, pode usar Send to Destination para conectar esses Canvas.

#### Melhorias no Canvas Context {#canvas-context-enhancements}

{% multi_lang_include release_type.md release="General availability" %}

No Canvas, agora você pode referenciar variáveis de contexto para definir:

- Um evento de remoção para Content Cards
- A expiração de Content Cards

Para mais detalhes, consulte [Criação de cartão]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation/?tab=canvas).

#### Comportamento de avanço de validação de entrega para etapas de Mensagem {#delivery-validation-advancement-behavior-for-message-steps}

{% multi_lang_include release_type.md release="General availability" %}

As [validações de entrega]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations) fornecem uma verificação adicional para confirmar que seu público atende aos critérios de entrega no momento do envio da mensagem. Se um usuário não atender às validações de entrega definidas para uma etapa de Mensagem, você pode usar a configuração **Delivery validations advancement behavior** para determinar se o usuário deve avançar para a próxima etapa ou sair do Canvas.

#### Limites de taxa de envio de mensagens do espaço de trabalho {#workspace-messaging-rate-limits}

{% multi_lang_include release_type.md release="General availability" %}

Use os [limites de taxa de envio de mensagens do espaço de trabalho]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits) para regular a taxa de entrega das suas mensagens de saída da plataforma, garantindo que seus usuários recebam as mensagens de que precisam. Os limites de taxa de envio de mensagens do espaço de trabalho estão sendo implementados gradualmente, então talvez você ainda não veja essas configurações no seu dashboard.

### Canais e pontos de contato

#### WhatsApp Template Builder

{% multi_lang_include release_type.md release="Early access" %}

O [WhatsApp Template Builder]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization) permite criar e enviar modelos de mensagens do WhatsApp diretamente na Braze — sem precisar alternar entre a Braze e o Meta Business Manager. Depois que o Meta aprovar seu modelo, use-o em quantas Campaigns e Canvas quiser.

#### Tags de produto, metafields e coleções da Shopify {#shopify-product-tags-metafields-and-collections}

{% multi_lang_include release_type.md release="General availability" %}

Agora você pode [sincronizar tags de produto, coleções e metafields da Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs) da sua loja Shopify para o seu catálogo da Braze. Isso fornece dados de produto mais ricos para personalização, segmentação e envio de mensagens baseado em catálogo sem soluções alternativas personalizadas.

### Parcerias

#### GRAVITY - Dados e análises - Fidelidade {#gravity-data-and-analytics-loyalty}

{% multi_lang_include release_type.md release="General availability" %}

O [GRAVTY®](https://www.lji.io/) é uma plataforma de fidelidade de nível empresarial da Loyalty Juggernaut Inc. (LJI) que permite que marcas de varejo, viagens, restaurantes (incluindo restaurantes de serviço rápido) e serviços financeiros projetem, gerenciem e escalem programas de próxima geração — impulsionando crescimento mensurável em engajamento, retenção e valor do tempo de vida do cliente por meio de experiências personalizadas e orientadas por dados.

### SDK

As seguintes atualizações do SDK foram lançadas. Para mais detalhes, consulte os [changelogs do SDK]({{site.baseurl}}/releases/sdk_changelogs).

#### Atualizações significativas do SDK

{% multi_lang_include release_type.md release="General availability" %}

As atualizações mais recentes do SDK foram lançadas. As atualizações significativas estão listadas na seção de atualizações do SDK; todas as outras atualizações podem ser encontradas nos changelogs correspondentes do SDK.

{% multi_lang_include releases/sdk/2026_4_30_26_updates.md %}

{% enddetails %}
{% details 2 de abril de 2026 %}

## Lançamento de 2 de abril de 2026 {#april-2-2026-release}

### Dados e relatórios

#### Novos campos do canal Banner em eventos do Currents e Datashare {#new-banner-channel-fields-in-currents-and-datashare-events}

A Braze adicionou campos para eventos existentes do canal Banner nas exportações do Currents e Datashare. Para ver a lista dessas atualizações de eventos e campos, consulte [Alterações na Versão 7]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-for-storage).

#### Suporte a data centers da UE e Índia do Mixpanel para Currents {#mixpanel-eu-and-india-data-center-support-for-currents}

A integração do Currents com o Mixpanel agora oferece suporte aos data centers da UE e da Índia do Mixpanel. Ao configurar uma integração com o Mixpanel, você pode escolher para qual região do Mixpanel a Braze envia seus dados. Essa atualização oferece suporte à crescente presença internacional do Mixpanel para clientes em comum. Para saber mais, consulte [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel).

#### Fontes e sincronizações reutilizáveis de Ingestão de Dados na Nuvem (CDI) {#reusable-cloud-data-ingestion-cdi-sources-and-syncs}

{% multi_lang_include release_type.md release="Early access" %}

A Ingestão de Dados na Nuvem (CDI) tem um novo design que separa fontes e sincronizações, para que você possa reutilizar uma fonte em várias sincronizações. As sincronizações existentes são migradas automaticamente para o novo modelo de fontes e sincronizações sem tempo de inatividade. Acesse **Cloud Data Ingestion** > **Sources** para visualizar, editar ou criar fontes e, em seguida, selecione uma fonte no menu suspenso ao criar uma sincronização. Essa mudança reduz configurações repetitivas e cria uma base para melhorias futuras. Para saber mais, consulte [Configurando integrações de data warehouse]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#setting-up-data-warehouse-integrations).

### BrazeAI<sup>TM</sup>

#### Abra tickets de suporte pelo BrazeAI Operator<sup>TM</sup> {#file-support-tickets-from-brazeai-operatortm}

{% multi_lang_include release_type.md release="General availability" %}

O [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator) agora inclui um fluxo para abrir tickets de suporte da Braze sem sair do dashboard. Para ver os passos, o contexto incluído automaticamente e dicas para resolução mais rápida, consulte [Abrir tickets de suporte com o BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets).

### Orquestração

#### Traduções multilíngues

{% multi_lang_include release_type.md release="General availability" %}

Depois de adicionar localidades ao seu espaço de trabalho, use [traduções multilíngues]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales) para direcionar usuários em diferentes idiomas, tudo dentro de um único push, e-mail, Banner, mensagem no app ou Content Block.

![Pré-visualizações de localidade]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %}){: style="max-width:70%;"}

#### Melhorias no Canvas Context

{% multi_lang_include release_type.md release="General availability" %}

No Canvas, agora você pode referenciar variáveis de contexto para definir:

- Uma [expiração]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables#set-an-expiration) para Banners e mensagens no app em uma etapa de Mensagem
- [Atrasos personalizados]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables#action-path-delays) para etapas de jornadas de ação

No campo de nome da variável de contexto, você também pode digitar o nome da variável de contexto ou selecioná-lo no menu suspenso do editor de etapas. Para mais detalhes, consulte [Contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) e [Variáveis de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables).

### Canais e pontos de contato

#### KakaoTalk

{% multi_lang_include release_type.md release="General availability" %}

O [KakaoTalk]({{site.baseurl}}/kakaotalk) é um canal de envio de mensagens que permite o envio de mensagens em massa e chat 1:1 com os usuários. Crie uma experiência de usuário personalizada usando Liquid e outros conteúdos dinâmicos para construir um ambiente que promova e aprimore uma experiência rica com a sua marca.

![Uma mensagem de item de lista do KakaoTalk.]({% image_buster /assets/img/kakaotalk/wide_image.png %}){: style="max-width:70%;"}

#### Banners no Canvas {#banners-in-canvas}

{% multi_lang_include release_type.md release="General availability" %}

Você pode usar [Banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners) como canal de envio de mensagens nas [etapas de Mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step) do Canvas. Os Banners permitem personalizar o conteúdo do app ou site de forma dinâmica, refletindo a elegibilidade e o comportamento do usuário em tempo real.

### Parcerias

#### CataBoom - Personalização de mensagens - Conteúdo visual e interativo {#cataboom-message-personalization-visual-and-interactive-content}

O [CataBoom]({{site.baseurl}}/partners/cataboom) é uma plataforma de gamificação. As marcas o utilizam para criar e lançar experiências digitais interativas, incluindo jogos de girar para ganhar, quizzes e jogos de prêmio instantâneo. Essas experiências aprofundam o engajamento e coletam dados primários.

#### Denada - Orquestração de mensagens - Modelos {#denada-message-orchestration-templates}

O [Denada]({{site.baseurl}}/partners/denada) é uma plataforma de criação de marketing com IA que permite que especialistas no assunto criem materiais de marketing alinhados à marca por meio de conversas naturais. Com o Denada, as equipes podem ir da ideação ao conteúdo de e-mail finalizado sem precisar de expertise em design.

#### Poq - eCommerce - Plataforma de apps móveis {#poq-ecommerce-mobile-app-platform}

O [Poq]({{site.baseurl}}/partners/poq) permite que empresas lancem, gerenciem e escalem rapidamente apps nativos para iOS e Android, oferecendo experiências móveis de alto desempenho que impulsionam o comércio e dão vida à promessa da sua marca.

#### The Trade Desk – Canvas Audience Sync

Usando o [Braze Audience Sync para The Trade Desk]({{site.baseurl}}/partners/canvas_audience_sync/trade_desk_audience_sync), você pode sincronizar dinamicamente seus dados primários de usuários da Braze diretamente para o The Trade Desk para redirecionamento de anúncios, modelagem de semelhança e supressão.

### SDK

#### Conecte seu Ambiente de Desenvolvimento Integrado (IDE) ao Docs MCP {#connect-your-integrated-development-environment-ide-to-the-docs-mcp}

Use assistentes de codificação com IA para acelerar seu fluxo de trabalho de integração com a Braze conectando seu Ambiente de Desenvolvimento Integrado (IDE) ao Braze Docs MCP por meio do Context7. Isso dá ao seu assistente acesso direto à documentação atual da Braze, para que ele possa gerar orientações de SDK mais precisas, exemplos de código e ajuda para solução de problemas no seu ambiente de desenvolvimento. Para ver os passos de configuração no Cursor, Claude Desktop e VS Code, consulte [Construindo com um LLM]({{site.baseurl}}/developer_guide/getting_started/build_with_llm#connecting-to-the-braze-docs-mcp).

#### Atualizações significativas do SDK

As atualizações mais recentes do SDK foram lançadas. As atualizações significativas estão listadas na seção de atualizações do SDK; todas as outras atualizações podem ser encontradas nos changelogs correspondentes do SDK.

{% multi_lang_include releases/sdk/2026_4_2_26_updates.md %}

{% enddetails %}

{% details 5 de março de 2026 %}

## Lançamento de 5 de março de 2026 {#march-5-2026-release}

### Dados e relatórios

#### Novo data center {#new-data-center}

{% multi_lang_include release_type.md release="General availability" %}

A Braze lançou um novo [data center]({{site.baseurl}}/user_guide/data/infrastructure/data_centers): JP-01. Você pode se inscrever em data centers específicos por região ao configurar sua conta na Braze.

#### Variáveis de contexto {#context-variables}

{% multi_lang_include release_type.md release="General availability" %}

[Variáveis de contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) são dados temporários que você pode criar e usar dentro da jornada de um usuário em um Canvas específico. Cada vez que um usuário entra no Canvas — mesmo que já tenha entrado antes — as variáveis de contexto serão redefinidas com base nos dados de entrada mais recentes e na configuração do Canvas. Essa abordagem permite que cada entrada no Canvas mantenha seu próprio contexto independente, permitindo que os usuários tenham múltiplos estados ativos dentro da mesma jornada enquanto retêm o contexto específico de cada estado.

#### Fontes de Ingestão de Dados na Nuvem {#cloud-data-ingestion-sources}

{% multi_lang_include release_type.md release="Early access" %}

A [Ingestão de Dados na Nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations#setting-up-cloud-data-ingestion-in-braze) tem uma nova interface que separa fontes de sincronizações, permitindo que você reutilize uma única fonte em qualquer número de sincronizações. Isso reduz configurações duplicadas e simplifica a configuração quando você tem múltiplas sincronizações. Se você já tem sincronizações existentes, elas são migradas automaticamente para a nova estrutura de fontes e sincronizações sem tempo de inatividade. Para começar, acesse **Cloud Data Ingestion** > **Sources** para visualizar, editar ou criar fontes e, em seguida, selecione uma fonte no menu suspenso ao criar uma sincronização.

#### Campos adicionais para eventos do Currents e Data Share {#additional-fields-for-currents-and-data-share-events}

{% multi_lang_include release_type.md release="General availability" %}

Os [eventos do Currents e Data Share]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04) agora incluem os seguintes novos campos para aprofundar os dados disponíveis para análise e sistemas downstream:

{% multi_lang_include releases/currents/2026_3_5_26_field_changes.md %}

#### Campos de Campaign e Canvas para Snowflake Data Share {#campaign-and-canvas-fields-for-snowflake-data-share}

{% multi_lang_include release_type.md release="General availability" %}

O [Snowflake Data Share]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs) agora inclui campos adicionais refletindo informações de Campaign e Canvas em 66 tabelas existentes, incluindo:

- `campaign_name`
- `canvas_name`
- `canvas_step_name`
- `canvas_variation_name`
- `message_variation_name`
- `conversion_behavior`
- `experiment_split_name`

#### Validação pré-importação e relatório de erros para CSV {#csv-pre-import-validation-and-error-reporting}

{% multi_lang_include release_type.md release="General availability" %}

As [importações de usuários por CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users) agora suportam validação pré-importação e relatórios de erros detalhados. Antes de importar, selecione **Validate file before importing** na página **Import Users** — a Braze escaneará seu arquivo e gerará um relatório identificando linhas que falharão completamente (erros) e linhas que serão bem-sucedidas com alguns valores ignorados (avisos). Você pode baixar o relatório, corrigir seu CSV e reenviar, ou prosseguir como está. Após a conclusão da importação, um relatório para download de quaisquer linhas que falharam também está disponível, com o motivo exato de cada problema.

#### Dashboard de diagnóstico de mensagens

{% multi_lang_include release_type.md release="Early access" %}

O [dashboard de Diagnóstico de Mensagens]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) fornece uma visão geral dos resultados de envio de mensagens, permitindo que você identifique tendências e diagnostique possíveis problemas na sua configuração de envio de mensagens. Esse dashboard pode ajudá-lo a entender por que as mensagens das suas Campaigns ou Canvas podem não ter sido enviadas como esperado.

### BrazeAI<sup>TM</sup>

#### Braze Agents no Console do agente {#braze-agents-in-agent-console}

{% multi_lang_include release_type.md release="General availability" %}

Os [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents) são ajudantes com tecnologia de IA que você pode criar dentro da Braze. Os agentes podem gerar conteúdo, tomar decisões inteligentes e enriquecer seus dados para que você possa oferecer experiências mais personalizadas aos clientes. Ao criar um agente, você define seu propósito e estabelece limites para como ele deve se comportar. Depois de estar ativo, o agente pode ser [implantado]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents) na Braze para gerar textos personalizados, tomar decisões em tempo real ou atualizar campos de catálogo.

### Orquestração

#### Permissões granulares de usuário {#granular-user-permissions}

{% multi_lang_include release_type.md release="Early access" %}

A Braze está introduzindo [permissões granulares]({{site.baseurl}}/user_guide/administer/global/user_management/permissions), uma forma mais flexível de gerenciar o acesso dos usuários. Consulte [Migrando para permissões granulares]({{site.baseurl}}/granular_permissions_migration) para saber sobre o processo de migração, incluindo como as permissões legadas são mapeadas para permissões granulares.

#### Limite de taxa baseado em canal {#channel-based-rate-limiting}

{% multi_lang_include release_type.md release="General availability" %}

Ao definir um limite de taxa de velocidade de entrega para uma campanha multicanal ou Canvas, você pode optar por definir um limite de taxa compartilhado ou um [limite baseado em canal]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#multichannel-campaigns-and-canvases). Quando uma campanha multicanal ou Canvas usa limite de taxa baseado em canal, o limite de taxa se aplica a cada um dos canais selecionados. Por exemplo, você pode configurar sua campanha ou Canvas para enviar no máximo 5.000 webhooks e 2.500 mensagens SMS por minuto em toda a campanha ou Canvas.

#### Etapa de Contexto do Canvas {#canvas-context-step}

{% multi_lang_include release_type.md release="General availability" %}

As [etapas de Contexto do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) permitem criar e atualizar uma ou mais variáveis para um usuário conforme ele avança em um Canvas. Por exemplo, se você tem um Canvas que gerencia descontos sazonais, pode usar uma variável de contexto para armazenar um código de desconto diferente cada vez que um usuário entra no Canvas.

### Canais e pontos de contato

#### Traduzir localidades em Content Blocks {#translate-locales-in-content-blocks}

{% multi_lang_include release_type.md release="Early access" %}

Depois de adicionar localidades ao seu espaço de trabalho, você pode [direcionar usuários em diferentes idiomas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) tudo dentro de um Content Block.

### Parcerias

#### Algolia - Busca e recomendações {#algolia-search-recommendations}

O [Algolia]({{site.baseurl}}/partners/ecommerce/product_search_recommendations/algolia) é uma plataforma de busca e descoberta que ajuda desenvolvedores a construir experiências de busca rápidas, relevantes e escaláveis. Com uma abordagem poderosa baseada em API, o Algolia combina algoritmos avançados de classificação com insights orientados por IA para busca no site, navegação e descoberta de conteúdo personalizado.

#### Anthropic - Provedor de modelos de IA {#anthropic-ai-model-provider}

O [Anthropic]({{site.baseurl}}/partners/ai_model_providers/anthropic) é uma empresa de pesquisa e segurança em IA que desenvolve o Claude, um assistente de IA de próxima geração construído para ser útil, honesto e seguro para uma ampla gama de tarefas de linguagem.

#### Canva - Personalização de mensagens - Estúdio criativo {#canva-message-personalization-creative-studio}

O [Canva]({{site.baseurl}}/partners/canva) sincroniza suas imagens no Canva diretamente com a Biblioteca de mídia da Braze, otimizando seu fluxo de trabalho criativo e mantendo seus ativos visuais atualizados em todos os seus canais de envio de mensagens.

#### DOTS.ECO - Recompensas {#dotseco-rewards}

O [DOTS.ECO]({{site.baseurl}}/partners/additional_channels_and_extensions/extensions/rewards/dots_eco) permite recompensar os usuários com impacto ambiental real por meio de certificados digitais rastreáveis. Cada certificado pode incluir metadados como um URL de certificado compartilhável e URL de imagem, para que os usuários possam visualizar (e revisitar) sua prova de impacto.

#### Figma - Personalização de mensagens - Estúdio criativo {#figma-message-personalization-creative-studio}

O [Figma]({{site.baseurl}}/partners/figma) é uma plataforma de design colaborativo que permite construir, projetar e prototipar produtos. Use essa integração para enviar imagens e ativos visuais do Figma diretamente para a Biblioteca de mídia da Braze.

#### Flybuy - Personalização de mensagens - Localização {#flybuy-message-personalization-location}

O [Flybuy]({{site.baseurl}}/partners/message_personalization/location/flybuy) da Radius Networks é a principal plataforma de localização omnicanal que utiliza tecnologia com IA para otimizar a velocidade de atendimento em retirada, entrega, drive-thru e consumo no local. Por meio de seu Marketing Suite integrado, o Flybuy também permite que as marcas entreguem mensagens hiperdirecionadas e baseadas em momentos, ajudando a impulsionar o engajamento, aumentar o ticket médio e apoiar iniciativas mais amplas de fidelidade.

#### Google Gemini - Provedor de modelos de IA {#google-gemini-ai-model-provider}

O [Google Gemini]({{site.baseurl}}/partners/ai_model_providers/google_gemini) é a família de modelos de IA do Google que combina raciocínio avançado em texto, código e imagens para ajudar as marcas a oferecer experiências mais inteligentes e personalizadas.

#### Limbik - Personalização de mensagens - Motores de personalização {#limbik-message-personalization-personalization-engines}

O [Limbik]({{site.baseurl}}/partners/message_personalization/dynamic_content/personalization_engines/limbik) é sua camada de ressonância com IA — prevendo como públicos reais interpretam e respondem a mensagens, conceitos e saídas de IA antes de chegarem ao mercado. Alimentado por pesquisa primária contínua em mais de 60 países e 25+ idiomas, o Limbik oferece públicos sintéticos validados por humanos — populações digitais que simulam a resposta real do público na velocidade da máquina e com precisão de nível de pesquisa (95% de confiança, 1,5% a 3% de margem de erro). O Limbik dá a você a capacidade de garantir imediatamente que suas mensagens ressoem com o que seu público-alvo acredita e sente.

#### Linkrunner - Orquestração de mensagens - Atribuição {#linkrunner-message-orchestration-attribution}

O [Linkrunner]({{site.baseurl}}/partners/message_orchestration/attribution/linkrunner) é uma plataforma de atribuição e análise móvel que ajuda você a rastrear e analisar suas campanhas de aquisição de usuários.

#### Mailizio - Orquestração de mensagens - Modelos {#mailizio-message-orchestration-templates}

O [Mailizio]({{site.baseurl}}/partners/message_orchestration/templates/Mailizio) é uma plataforma de criação e gerenciamento de e-mails que facilita o design de conteúdo reutilizável e seguro para a marca usando um editor visual intuitivo. Com a integração do Mailizio à Braze, você pode exportar seus blocos de conteúdo e modelos de e-mail e, em seguida, gerar automaticamente mensagens no app a partir desses mesmos ativos, permitindo a implantação rápida e totalmente controlada de campanhas.

#### Open Loyalty - Dados e análises - Fidelidade {#open-loyalty-data-and-analytics-loyalty}

O [Open Loyalty]({{site.baseurl}}/partners/data_and_analytics/loyalty/openloyalty) é uma plataforma de programa de fidelidade baseada em nuvem que permite criar e gerenciar programas de fidelidade e recompensas para clientes. A integração entre a Braze e o Open Loyalty sincroniza dados de fidelidade — como saldo de pontos, alterações de nível e avisos de expiração — diretamente na Braze em tempo real. Isso permite acionar mensagens personalizadas (e-mail, push, SMS) quando o status de fidelidade de um usuário muda.

#### OpenAI - Provedor de modelos de IA {#openai-ai-model-provider}

A [OpenAI]({{site.baseurl}}/partners/ai_model_providers/openai) cria modelos avançados de IA, como o GPT, que permitem a compreensão e geração de linguagem natural, capacitando as marcas a construir e escalar interações significativas com os clientes.

#### Shopgate - Canais {#shopgate-channels}

O [Shopgate]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/shopgate) é uma plataforma de comércio móvel e omnicanal que ajuda comerciantes a criar apps de compras e melhorar a eficiência de lojas físicas por meio de ferramentas de fulfillment e clienteling, ou seja, suporte personalizado ao cliente na loja com base em dados do cliente.

#### Splio - Dados e análises - Importação de coorte {#splio-data-and-analytics-cohort-import}

O [Splio]({{site.baseurl}}/partners/data_and_analytics/cohort_import/splio) é uma ferramenta de construção de público que permite aumentar o número de campanhas e a receita sem prejudicar a experiência do cliente, e fornece análises para acompanhar o desempenho de campanhas de CRM tanto online quanto offline.

### SDK

#### Atualizações significativas do SDK

As atualizações mais recentes do SDK foram lançadas. As atualizações significativas estão listadas na seção de atualizações do SDK; todas as outras atualizações podem ser encontradas nos changelogs correspondentes do SDK.

{% multi_lang_include releases/sdk/2026_3_5_26_updates.md %}

{% enddetails %}

{% details 5 de fevereiro de 2026 %}

## Lançamento de 5 de fevereiro de 2026 {#february-5-2026-release}

### BrazeAI<sup>TM</sup>

#### Otimizador de Conteúdo {#content-optimizer}

{% multi_lang_include release_type.md release="Beta" %}

O [Otimizador de Conteúdo]({{site.baseurl}}/user_guide/brazeai/content_optimizer) é uma etapa do Canvas de teste de conteúdo contínuo e de alta variância que oferece otimização automatizada do engajamento. Usando uma interface de arrastar e soltar semelhante à etapa de mensagem, você pode definir os componentes que deseja testar, gerar variantes usando IA (ou inseri-las manualmente) e usar Liquid tags para mapear esses componentes para o conteúdo da mensagem.

Criado com base em um otimizador de bandido multiarmado não contextual, o Otimizador de Conteúdo envia uma única mensagem por usuário, determinando qual combinação de variantes de componentes deve ser fornecida com base em recomendações preditivas. À medida que a etapa coleta dados ao longo do tempo, as variantes de alto desempenho aumentam naturalmente na alocação de envio, enquanto as variantes de baixo desempenho diminuem. O Otimizador de Conteúdo funciona melhor com Canvas de envio repetido que têm um volume diário consistente de usuários (pelo menos alguns milhares de usuários por dia) para permitir a otimização contínua.

### Dados e relatórios

#### Eventos recomendados para eCommerce

{% multi_lang_include release_type.md release="Early access" %}

Para combinar os eventos recomendados de eCommerce com o evento de compra existente, adicionamos o [evento de conversão "Places Order"]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases#conversions-dashboard), que é semelhante a "Makes Purchase".

### Canais e pontos de contato

#### Traduzir localidades em banners {#translate-locales-in-banners}

{% multi_lang_include release_type.md release="Early access" %}

Depois de adicionar localidades ao seu espaço de trabalho, [direcione usuários em diferentes idiomas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages#use-locales) tudo dentro de um único banner.

#### Configurar largura para Content Blocks de arrastar e soltar {#configure-width-for-drag-and-drop-content-blocks}

[Ajuste a largura do seu Content Block]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=email) selecionando o botão no menu de navegação. A largura padrão é 100% quando não especificada nas configurações globais de estilo do seu e-mail; caso contrário, as configurações globais serão respeitadas.

![Uma seta de dois lados com uma opção para editar a largura.]({% image_buster /assets/img_archive/content_block_width_updated.png %}){: style="max-width:30%;" }

#### Use o aquecimento automatizado de IP {#use-automated-ip-warming}

{% multi_lang_include release_type.md release="Early access" %}

Use o [aquecimento automatizado de IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming#automated-ip-warming) para aumentar gradualmente seu volume de envio diário, permitindo que os provedores de caixa de entrada aprendam e confiem em seus padrões de envio. A Braze envia primeiro para seus assinantes mais engajados, o que permite que o volume diário cresça em um ritmo que corresponda às práticas recomendadas.

### Parcerias

#### LinkedIn – Canvas Audience Sync

Usando o [Braze Audience Sync para LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync), adicione dados de usuários da sua integração com a Braze às listas de clientes do LinkedIn para fornecer anúncios com base em acionadores comportamentais, segmentação e muito mais. Qualquer critério que você normalmente usaria para acionar uma mensagem (como push, e-mail, SMS e webhook) em um Braze Canvas com base nos dados do usuário agora pode acionar um anúncio para esse usuário em suas listas de clientes do LinkedIn.

#### Oracle Crowdtwist - Dados e análises {#oracle-crowdtwist-data-analytics}

O [Oracle Crowdtwist]({{site.baseurl}}/partners/crowdtwist) é uma solução líder de fidelização de clientes nativa da nuvem que capacita as marcas a oferecer experiências personalizadas aos clientes. Sua solução oferece mais de 100 caminhos de engajamento prontos para uso, proporcionando um rápido retorno do investimento para que os profissionais de marketing desenvolvam uma visão mais completa do cliente.

#### Fullstory - Conteúdo dinâmico {#fullstory-dynamic-content}

A plataforma de dados comportamentais da [Fullstory]({{site.baseurl}}/partners/fullstory) ajuda os líderes de tecnologia a tomar decisões melhores e mais bem informadas. Ao injetar dados comportamentais digitais em sua pilha de análise, a tecnologia patenteada da Fullstory libera o poder dos dados comportamentais de qualidade em escala, transformando cada visita digital em insights acionáveis.

#### Open Loyalty - Dados e análises {#open-loyalty-data-analytics}

O [Open Loyalty]({{site.baseurl}}/partners/openloyalty) é uma plataforma de programa de fidelidade baseada em nuvem que permite criar e gerenciar programas de fidelidade e recompensas para clientes. A integração entre a Braze e o Open Loyalty sincroniza dados de fidelidade — como saldo de pontos, alterações de nível e avisos de expiração — diretamente na Braze em tempo real. Isso permite acionar mensagens personalizadas (e-mail, push, SMS) quando o status de fidelidade de um usuário muda.

#### DOTS.ECO - Extensões {#dotseco-extensions}

O [DOTS.ECO]({{site.baseurl}}/partners/dots.eco) permite recompensar os usuários com impacto ambiental real por meio de certificados digitais rastreáveis. Cada certificado pode incluir metadados como um URL de certificado compartilhável e URL de imagem, para que os usuários possam visualizar (e revisitar) sua prova de impacto.

#### Mailizio - Orquestração de mensagens {#mailizio-message-orchestration}

O [Mailizio]({{site.baseurl}}/partners/mailizio) é uma plataforma de criação e gerenciamento de e-mails que facilita o design de conteúdo reutilizável e seguro para a marca usando um editor visual intuitivo. Com a integração do Mailizio à Braze, exporte seus blocos de conteúdo e modelos de e-mail e, em seguida, gere automaticamente mensagens no app a partir desses mesmos ativos, permitindo a implantação rápida e totalmente controlada de campanhas.

### APIs

#### APIs POST da Biblioteca de mídia {#media-library-post-apis}

{% multi_lang_include release_type.md release="General availability" %}

Os ativos da Biblioteca de mídia agora podem ser adicionados via API, permitindo que clientes, parceiros e agências automatizem mais fluxos de trabalho de criação de mensagens. Use a [API]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create) para fazer upload de um arquivo de ativo diretamente ou copiar um arquivo de um URL existente. Esse recurso desbloqueia recursos de integração e automação.

### Currents e Datashare

#### Eventos do Console do agente para destinos de armazenamento e Datashare {#agent-console-events-for-storage-destinations-and-datashare}

{% multi_lang_include release_type.md release="General availability" %}

Dois novos [eventos]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) estão agora disponíveis para destinos de armazenamento (AWS S3, GCS e Azure Blob Storage) e Snowflake Datashare: `agentconsole.AgentExecuted` e `agentconsole.ToolInvocation`. Esses eventos permitem que você analise o uso e os detalhes do Console do agente em seus sistemas downstream, ajudando-o a entender e aproveitar ao máximo o uso do agente. Os agentes permitem que você crie e implante agentes inteligentes que podem executar tarefas específicas na Braze, incluindo a geração de conteúdo em Canvas ou catálogos e o encaminhamento de usuários por diferentes caminhos com base em tomada de decisões inteligente. Para saber mais, consulte o [changelog do Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Novos eventos de nova tentativa para canais individuais {#new-retry-events-for-individual-channels}

{% multi_lang_include release_type.md release="General availability" %}

Novos [eventos de nova tentativa]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) agora estão disponíveis para canais de e-mail, LINE, notificações por push, SMS, webhooks e WhatsApp. Esses eventos fornecem visibilidade de quando o limite de frequência resulta no atraso de uma mensagem programada em vez de abortá-la. Quando uma mensagem é despriorizada ou tem limite de frequência, ela agora pode ser repetida dentro de uma janela de repetição configurada, o que lhe dá uma visão melhor dos padrões de entrega de mensagens e dos impactos do limite de frequência. Para saber mais, consulte o [changelog do Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Novo campo `time_ms` adicionado ao evento TokenStateChange {#add-new-time_ms-field-to-tokenstatechange-event}

{% multi_lang_include release_type.md release="General availability" %}

Um novo campo `time_ms` foi adicionado ao evento [`users.behaviors.pushnotification.TokenStateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events), fornecendo granularidade em nível de milissegundos para rastrear alterações no estado do token por push. Essa precisão aprimorada ajuda você a entender o status mais recente de um token por push quando várias alterações ocorrem no mesmo segundo, dando-lhe confiança nos sistemas downstream de que você tem o status de inscrição correto. Para saber mais, consulte o [changelog do Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Enviar usuário anônimo para destinos do Tealium {#send-anonymous-user-to-tealium-destinations}

{% multi_lang_include release_type.md release="General availability" %}

Os eventos que não têm um ID de usuário externo definido agora podem ser transmitidos para destinos do [Tealium]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_for_currents?redirected=1). Ao marcar a caixa de seleção "Include events from anonymous users" na integração do Currents, os eventos sem um ID de usuário externo serão enviados ao destino em vez de serem suprimidos. Esse recurso é essencial para análises downstream e casos de uso que envolvem usuários não identificados e anônimos.

##### Enviar usuário anônimo para destinos CustomHTTP {#send-anonymous-user-to-customhttp-destinations}

{% multi_lang_include release_type.md release="Beta" %}

Os eventos que não têm um ID de usuário externo definido agora podem ser transmitidos para destinos CustomHTTP. Ao marcar a caixa de seleção "Include events from anonymous users" na integração do Currents, os eventos sem um ID de usuário externo serão enviados ao destino em vez de serem suprimidos. Esse recurso é essencial para análises downstream e casos de uso que envolvem usuários não identificados e anônimos.

#### Evento de abertura de e-mail — campo "machine_open" {#email-open-event-machine_open-field}

O [evento de abertura de e-mail]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#email-open-events) agora gera o valor do campo "machine_open" para que você possa gerar relatórios sobre a métrica [_Abertura de máquina_]({{site.baseurl}}/user_guide/analytics/reporting/report_metrics#machine-opens).

### SDK

As seguintes atualizações do SDK foram lançadas. O Swift SDK v14.0.1 corrige um problema com o manuseio de links universais. O Android SDK v40.2.0 corrige um possível vazamento de memória e resolve um problema com a abertura de várias sessões quando atividades transparentes estão presentes. O Expo SDK v3.2.0 adiciona a opção `forwardUniversalLinks` (padrão: false) para configurar o tratamento nativo de links universais do Swift SDK.

#### Atualizações significativas do SDK

As atualizações mais recentes do SDK foram lançadas. As atualizações significativas estão listadas na seção de atualizações do SDK; todas as outras atualizações podem ser encontradas nos changelogs correspondentes do SDK.

{% multi_lang_include releases/sdk/2026_2_5_26_updates.md %}

{% enddetails %}