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
Para obter mais informações sobre qualquer uma das atualizações listadas nesta página, entre em contato com o gerente da sua conta ou [abra um tíquete de suporte]({{site.baseurl}}/user_guide/administer/personal/braze_support/). Confira também nossos [Changelogs do SDK]({{site.baseurl}}/developer_guide/changelogs/) para mais informações sobre nossas versões mensais do SDK, melhorias e alterações significativas.
{% endalert %}

{% details 2 de abril de 2026 %}

## Lançamento de 2 de abril de 2026 {#april-2-2026-release}

### Dados e relatórios {#data-reporting}

#### Novos campos do canal Banner em eventos do Currents e Datashare {#new-banner-channel-fields-in-currents-and-datashare-events}

A Braze adicionou campos para eventos existentes do canal Banner nas exportações do Currents e Datashare. Para ver a lista dessas atualizações de eventos e campos, consulte [Alterações na Versão 7]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/#changes-for-storage).

#### Suporte a data centers da UE e Índia do Mixpanel para Currents {#mixpanel-eu-and-india-data-center-support-for-currents}

A integração do Currents com o Mixpanel agora oferece suporte aos data centers da UE e da Índia do Mixpanel. Ao configurar uma integração com o Mixpanel, você pode escolher para qual região do Mixpanel a Braze envia seus dados. Essa atualização oferece suporte à crescente presença internacional do Mixpanel para clientes em comum. Para saber mais, consulte [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/).

#### Fontes e sincronizações reutilizáveis de Ingestão de Dados na Nuvem (CDI) {#reusable-cloud-data-ingestion-cdi-sources-and-syncs}

{% multi_lang_include release_type.md release="Early access" %}

A Ingestão de Dados na Nuvem (CDI) tem um novo design que separa fontes e sincronizações, para que você possa reutilizar uma fonte em várias sincronizações. As sincronizações existentes são migradas automaticamente para o novo modelo de fontes e sincronizações sem tempo de inatividade. Acesse **Cloud Data Ingestion** > **Sources** para visualizar, editar ou criar fontes e, em seguida, selecione uma fonte no menu suspenso ao criar uma sincronização. Essa mudança reduz configurações repetitivas e cria uma base para melhorias futuras. Para saber mais, consulte [Configurando integrações de data warehouse]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/#setting-up-data-warehouse-integrations).

### BrazeAI<sup>TM</sup>

#### Abra tíquetes de suporte pelo BrazeAI Operator<sup>TM</sup> {#file-support-tickets-from-brazeai-operatortm}

{% multi_lang_include release_type.md release="General availability" %}

O [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/) agora inclui um fluxo para abrir tíquetes de suporte da Braze sem sair do dashboard. Para ver os passos, o contexto incluído automaticamente e dicas para resolução mais rápida, consulte [Abrir tíquetes de suporte com o BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets/).

### Orquestração {#orchestration}

#### Traduções multilíngues {#multi-language-translations}

{% multi_lang_include release_type.md release="General availability" %}

Depois de adicionar localidades ao seu espaço de trabalho, use [traduções multilíngues]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/) para direcionar usuários em diferentes idiomas, tudo dentro de um único push, e-mail, Banner, mensagem no app ou Content Block.

![Pré-visualizações de localidade]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %}){: style="max-width:70%;"}

#### Melhorias no Canvas Context {#canvas-context-enhancements}

{% multi_lang_include release_type.md release="General availability" %}

No Canvas, agora você pode referenciar variáveis de contexto para definir:

- Uma [expiração]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_variables/#set-an-expiration) para Banners e mensagens no app em uma etapa de Mensagem
- [Atrasos personalizados]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_variables/#action-path-delays) para etapas de Jornadas de ação

No campo de nome da variável de contexto, você também pode digitar o nome da variável de contexto ou selecioná-lo no menu suspenso do editor de etapas. Para mais detalhes, consulte [Contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/) e [Variáveis de contexto]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_variables/).

### Canais e pontos de contato {#channels-touchpoints}

#### KakaoTalk

{% multi_lang_include release_type.md release="General availability" %}

O [KakaoTalk]({{site.baseurl}}/kakaotalk/) é um canal de envio de mensagens que permite o envio de mensagens em massa e chat 1:1 com os usuários. Crie uma experiência de usuário personalizada usando Liquid e outros conteúdos dinâmicos para construir um ambiente que promova e aprimore uma experiência rica com a sua marca.

![Uma mensagem de item de lista do KakaoTalk.]({% image_buster /assets/img/kakaotalk/wide_image.png %}){: style="max-width:70%;"}

#### Banners no Canvas {#banners-in-canvas}

{% multi_lang_include release_type.md release="General availability" %}

Você pode usar [Banners]({{site.baseurl}}/user_guide/channels/banners/) como canal de envio de mensagens nas [etapas de Mensagem]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/) do Canvas. Os Banners permitem personalizar o conteúdo do app ou site de forma dinâmica, refletindo a elegibilidade e o comportamento do usuário em tempo real.

### Parcerias {#partnerships}

#### CataBoom - Personalização de mensagens - Conteúdo visual e interativo {#cataboom-message-personalization-visual-and-interactive-content}

O [CataBoom]({{site.baseurl}}/partners/cataboom/) é uma plataforma de gamificação. As marcas o utilizam para criar e lançar experiências digitais interativas, incluindo jogos de girar para ganhar, quizzes e jogos de prêmio instantâneo. Essas experiências aprofundam o engajamento e coletam dados primários.

#### Denada - Orquestração de mensagens - Modelos {#denada-message-orchestration-templates}

O [Denada]({{site.baseurl}}/partners/denada/) é uma plataforma de criação de marketing com IA que permite que especialistas no assunto criem materiais de marketing alinhados à marca por meio de conversas naturais. Com o Denada, as equipes podem ir da ideação ao conteúdo de e-mail finalizado sem precisar de expertise em design.

#### Poq - eCommerce - Plataforma de apps móveis {#poq-ecommerce-mobile-app-platform}

O [Poq]({{site.baseurl}}/partners/poq/) permite que empresas lancem, gerenciem e escalem rapidamente apps nativos para iOS e Android, oferecendo experiências móveis de alto desempenho que impulsionam o comércio e dão vida à promessa da sua marca.

#### The Trade Desk – Canvas Audience Sync

Usando o [Braze Audience Sync para The Trade Desk]({{site.baseurl}}/partners/canvas_audience_sync/trade_desk_audience_sync/), você pode sincronizar dinamicamente seus dados primários de usuários da Braze diretamente para o The Trade Desk para redirecionamento de anúncios, modelagem de semelhança e supressão.

### SDK

#### Conecte seu Ambiente de Desenvolvimento Integrado (IDE) ao Docs MCP {#connect-your-integrated-development-environment-ide-to-the-docs-mcp}

Use assistentes de codificação com IA para acelerar seu fluxo de trabalho de integração com a Braze conectando seu Ambiente de Desenvolvimento Integrado (IDE) ao Braze Docs MCP por meio do Context7. Isso dá ao seu assistente acesso direto à documentação atual da Braze, para que ele possa gerar orientações de SDK mais precisas, exemplos de código e ajuda para solução de problemas no seu ambiente de desenvolvimento. Para ver os passos de configuração no Cursor, Claude Desktop e VS Code, consulte [Construindo com um LLM]({{site.baseurl}}/developer_guide/getting_started/build_with_llm/#connecting-to-the-braze-docs-mcp).

#### Atualizações significativas do SDK {#sdk-breaking-updates}

As seguintes atualizações do SDK foram lançadas. As atualizações significativas estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [Cordova 15.0.0](https://github.com/braze-inc/braze-cordova-sdk/releases/tag/15.0.0)
    - Atualizada a ponte nativa do Android [do Braze Android SDK 39.0.0 para 41.1.1](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v41.1.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Atualizada a ponte nativa do iOS [do Braze Swift SDK 13.2.0 para 14.0.1](https://github.com/braze-inc/braze-swift-sdk/compare/13.2.0...14.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Corrige um problema com `subscribeToInAppMessage` envolvendo o retorno de chamada de sucesso.
- [Roku SDK 2.2.1](https://github.com/braze-inc/braze-roku-sdk/releases/tag/v2.2.1)
    - Corrige uma falha ao processar uma solicitação HTTP com falha para mensagens no app com modelo enquanto o dispositivo tem conectividade intermitente ou nenhuma conectividade.
- [Web SDK 6.6.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#660)
    - Adiciona a opção de inicialização `cookieExpiryInDays` para configurar a duração do cookie a partir do padrão de 400 dias.
- [Flutter SDK 18.0.0](https://pub.dev/packages/braze_plugin/changelog#1800)
    - Adiciona suporte à inicialização atrasada.
    - Simplifica o processo de integração do iOS para não exigir a escrita de código nativo para encaminhar atualizações de Content Cards, Banners, Feature Flags, mensagens no app ou notificações por push do SDK nativo.
        - O SDK agora configurará automaticamente essas assinaturas quando a instância da Braze for criada.
        - Isso corresponde ao comportamento existente no Android.
        - Para migrar, remova quaisquer chamadas manuais para `braze.contentCards.subscribeToUpdates()`, `braze.banners.subscribeToUpdates()`, `braze.notifications.subscribeToUpdates`, `braze.featureFlags.subscribeToUpdates` e `braze.inAppMessagePresenter` no `AppDelegate`.
        - Por padrão, as mensagens no app serão apresentadas. Para substituir isso, defina um apresentador de mensagens no app personalizado usando o closure `postInitialization` em `BrazePlugin.configure(_:postInitialization:)`.
- [Swift SDK 14.0.4](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1404)
    - Corrige um bug com a automação de push na reinicialização do SDK.
    - Corrige um problema em que imagens inválidas em Push Stories não eram filtradas.
- [Swift SDK 14.0.3](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1403)

{% enddetails %}

{% details 5 de março de 2026 %}

## Lançamento de 5 de março de 2026 {#march-5-2026-release}

### Dados e relatórios {#data-reporting}

#### Novo data center {#new-data-center}

{% multi_lang_include release_type.md release="General availability" %}

A Braze lançou um novo [data center]({{site.baseurl}}/user_guide/data/infrastructure/data_centers/): JP-01. Você pode se inscrever em data centers específicos por região ao configurar sua conta na Braze.

#### Variáveis de contexto {#context-variables}

{% multi_lang_include release_type.md release="General availability" %}

[Variáveis de contexto]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/) são dados temporários que você pode criar e usar dentro da jornada de um usuário em um Canvas específico. Cada vez que um usuário entra no Canvas — mesmo que já tenha entrado antes — as variáveis de contexto serão redefinidas com base nos dados de entrada mais recentes e na configuração do Canvas. Essa abordagem permite que cada entrada no Canvas mantenha seu próprio contexto independente, permitindo que os usuários tenham múltiplos estados ativos dentro da mesma jornada enquanto retêm o contexto específico de cada estado.

#### Fontes de Ingestão de Dados na Nuvem {#cloud-data-ingestion-sources}

{% multi_lang_include release_type.md release="Early access" %}

A [Ingestão de Dados na Nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations/#setting-up-cloud-data-ingestion-in-braze) tem uma nova interface que separa fontes de sincronizações, permitindo que você reutilize uma única fonte em qualquer número de sincronizações. Isso reduz configurações duplicadas e simplifica a configuração quando você tem múltiplas sincronizações. Se você já tem sincronizações existentes, elas são migradas automaticamente para a nova estrutura de fontes e sincronizações sem tempo de inatividade. Para começar, acesse **Cloud Data Ingestion** > **Sources** para visualizar, editar ou criar fontes e, em seguida, selecione uma fonte no menu suspenso ao criar uma sincronização.

#### Campos adicionais para eventos do Currents e Data Share {#additional-fields-for-currents-and-data-share-events}

{% multi_lang_include release_type.md release="General availability" %}

Os [eventos do Currents e Data Share]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/#changes-in-version-5-release-date-2026-02-04) agora incluem os seguintes novos campos para aprofundar os dados disponíveis para análise e sistemas downstream:

- `agentconsole.AgentExecuted`: Adicionado `error` (string) — uma descrição de qualquer erro que ocorreu.
- `agentconsole.ToolInvocation`: Adicionado `request_id` (string) — um ID único para a solicitação geral do LLM e execução completa.
- `users.messages.rcs.InboundReceive`: Adicionado `canvas_variation_name` (string) — o nome da variação do Canvas que o usuário recebeu.

#### Campos de Campaign e Canvas para Snowflake Data Share {#campaign-and-canvas-fields-for-snowflake-data-share}

{% multi_lang_include release_type.md release="General availability" %}

O [Snowflake Data Share]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/#changes-for-data-sharing-3) agora inclui campos adicionais refletindo informações de Campaign e Canvas em 66 tabelas existentes, incluindo:

- `campaign_name`
- `canvas_name`
- `canvas_step_name`
- `canvas_variation_name`
- `message_variation_name`
- `conversion_behavior`
- `experiment_split_name`

#### Validação pré-importação e relatório de erros para CSV {#csv-pre-import-validation-and-error-reporting}

{% multi_lang_include release_type.md release="General availability" %}

As [importações de usuários por CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/) agora suportam validação pré-importação e relatórios de erros detalhados. Antes de importar, selecione **Validate file before importing** na página **Import Users** — a Braze escaneará seu arquivo e gerará um relatório identificando linhas que falharão completamente (erros) e linhas que serão bem-sucedidas com alguns valores ignorados (avisos). Você pode baixar o relatório, corrigir seu CSV e reenviar, ou prosseguir como está. Após a conclusão da importação, um relatório para download de quaisquer linhas que falharam também está disponível, com o motivo exato de cada problema.

#### Dashboard de diagnóstico de mensagens {#messaging-diagnostics-dashboard}

{% multi_lang_include release_type.md release="Early access" %}

O [dashboard de Diagnóstico de Mensagens]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard/) fornece uma visão geral dos resultados de envio de mensagens, permitindo que você identifique tendências e diagnostique possíveis problemas na sua configuração de envio de mensagens. Esse dashboard pode ajudá-lo a entender por que as mensagens das suas campanhas ou Canvas podem não ter sido enviadas como esperado.

### BrazeAI<sup>TM</sup>

#### Braze Agents no Console do agente {#braze-agents-in-agent-console}

{% multi_lang_include release_type.md release="General availability" %}

Os [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/) são ajudantes com tecnologia de IA que você pode criar dentro da Braze. Os agentes podem gerar conteúdo, tomar decisões inteligentes e enriquecer seus dados para que você possa oferecer experiências mais personalizadas aos clientes. Ao criar um agente, você define seu propósito e estabelece limites para como ele deve se comportar. Depois de estar ativo, o agente pode ser [implantado]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/) na Braze para gerar textos personalizados, tomar decisões em tempo real ou atualizar campos de catálogo.

### Orquestração {#orchestration}

#### Permissões granulares de usuário {#granular-user-permissions}

{% multi_lang_include release_type.md release="Early access" %}

A Braze está introduzindo [permissões granulares]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/), uma forma mais flexível de gerenciar o acesso dos usuários. Consulte [Migrando para permissões granulares]({{site.baseurl}}/granular_permissions_migration/) para saber sobre o processo de migração, incluindo como as permissões legadas são mapeadas para permissões granulares.

#### Limite de taxa baseado em canal {#channel-based-rate-limiting}

{% multi_lang_include release_type.md release="General availability" %}

Ao definir um limite de taxa de velocidade de entrega para uma campanha multicanal ou Canvas, você pode optar por definir um limite de taxa compartilhado ou um [limite baseado em canal]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#multichannel-campaigns-and-canvases). Quando uma campanha multicanal ou Canvas usa limite de taxa baseado em canal, o limite de taxa se aplica a cada um dos canais selecionados. Por exemplo, você pode configurar sua campanha ou Canvas para enviar no máximo 5.000 webhooks e 2.500 mensagens SMS por minuto em toda a campanha ou Canvas.

#### Etapa de Contexto do Canvas {#canvas-context-step}

{% multi_lang_include release_type.md release="General availability" %}

As [etapas de Contexto do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/) permitem criar e atualizar uma ou mais variáveis para um usuário conforme ele avança em um Canvas. Por exemplo, se você tem um Canvas que gerencia descontos sazonais, pode usar uma variável de contexto para armazenar um código de desconto diferente cada vez que um usuário entra no Canvas.

### Canais e pontos de contato {#channels-touchpoints}

#### Traduzir localidades em Content Blocks {#translate-locales-in-content-blocks}

{% multi_lang_include release_type.md release="Early access" %}

Depois de adicionar localidades ao seu espaço de trabalho, você pode [direcionar usuários em diferentes idiomas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/) tudo dentro de um Content Block.

### Parcerias {#partnerships}

#### Algolia - Busca e recomendações {#algolia-search-recommendations}

O [Algolia]({{site.baseurl}}/partners/ecommerce/product_search_recommendations/algolia/) é uma plataforma de busca e descoberta que ajuda desenvolvedores a construir experiências de busca rápidas, relevantes e escaláveis. Com uma abordagem poderosa baseada em API, o Algolia combina algoritmos avançados de classificação com insights orientados por IA para busca no site, navegação e descoberta de conteúdo personalizado.

#### Anthropic - Provedor de modelos de IA {#anthropic-ai-model-provider}

O [Anthropic]({{site.baseurl}}/partners/ai_model_providers/anthropic/) é uma empresa de pesquisa e segurança em IA que desenvolve o Claude, um assistente de IA de próxima geração construído para ser útil, honesto e seguro para uma ampla gama de tarefas de linguagem.

#### Canva - Personalização de mensagens - Estúdio criativo {#canva-message-personalization-creative-studio}

O [Canva]({{site.baseurl}}/partners/canva/) sincroniza suas imagens no Canva diretamente com a Biblioteca de mídia da Braze, otimizando seu fluxo de trabalho criativo e mantendo seus ativos visuais atualizados em todos os seus canais de envio de mensagens.

#### DOTS.ECO - Recompensas {#dotseco-rewards}

O [DOTS.ECO]({{site.baseurl}}/partners/additional_channels_and_extensions/extensions/rewards/dots_eco/) permite recompensar os usuários com impacto ambiental real por meio de certificados digitais rastreáveis. Cada certificado pode incluir metadados como um URL de certificado compartilhável e URL de imagem, para que os usuários possam visualizar (e revisitar) sua prova de impacto.

#### Figma - Personalização de mensagens - Estúdio criativo {#figma-message-personalization-creative-studio}

O [Figma]({{site.baseurl}}/partners/figma/) é uma plataforma de design colaborativo que permite construir, projetar e prototipar produtos. Use essa integração para enviar imagens e ativos visuais do Figma diretamente para a Biblioteca de mídia da Braze.

#### Flybuy - Personalização de mensagens - Localização {#flybuy-message-personalization-location}

O [Flybuy]({{site.baseurl}}/partners/message_personalization/location/flybuy/) da Radius Networks é a principal plataforma de localização omnicanal que utiliza tecnologia com IA para otimizar a velocidade de atendimento em retirada, entrega, drive-thru e consumo no local. Por meio de seu Marketing Suite integrado, o Flybuy também permite que as marcas entreguem mensagens hiperdirecionadas e baseadas em momentos, ajudando a impulsionar o engajamento, aumentar o ticket médio e apoiar iniciativas mais amplas de fidelidade.

#### Google Gemini - Provedor de modelos de IA {#google-gemini-ai-model-provider}

O [Google Gemini]({{site.baseurl}}/partners/ai_model_providers/google_gemini/) é a família de modelos de IA do Google que combina raciocínio avançado em texto, código e imagens para ajudar as marcas a oferecer experiências mais inteligentes e personalizadas.

#### Limbik - Personalização de mensagens - Motores de personalização {#limbik-message-personalization-personalization-engines}

O [Limbik]({{site.baseurl}}/partners/message_personalization/dynamic_content/personalization_engines/limbik/) é sua camada de ressonância com IA — prevendo como públicos reais interpretam e respondem a mensagens, conceitos e saídas de IA antes de chegarem ao mercado. Alimentado por pesquisa primária contínua em mais de 60 países e 25+ idiomas, o Limbik oferece públicos sintéticos validados por humanos — populações digitais que simulam a resposta real do público na velocidade da máquina e com precisão de nível de pesquisa (95% de confiança, 1,5% a 3% de margem de erro). O Limbik dá a você a capacidade de garantir imediatamente que suas mensagens ressoem com o que seu público-alvo acredita e sente.

#### Linkrunner - Orquestração de mensagens - Atribuição {#linkrunner-message-orchestration-attribution}

O [Linkrunner]({{site.baseurl}}/partners/message_orchestration/attribution/linkrunner/) é uma plataforma de atribuição e análise móvel que ajuda você a rastrear e analisar suas campanhas de aquisição de usuários.

#### Mailizio - Orquestração de mensagens - Modelos {#mailizio-message-orchestration-templates}

O [Mailizio]({{site.baseurl}}/partners/message_orchestration/templates/Mailizio/) é uma plataforma de criação e gerenciamento de e-mails que facilita o design de conteúdo reutilizável e seguro para a marca usando um editor visual intuitivo. Com a integração do Mailizio à Braze, você pode exportar seus blocos de conteúdo e modelos de e-mail e, em seguida, gerar automaticamente mensagens no app a partir desses mesmos ativos, permitindo a implantação rápida e totalmente controlada de campanhas.

#### Open Loyalty - Dados e análises - Fidelidade {#open-loyalty-data-and-analytics-loyalty}

O [Open Loyalty]({{site.baseurl}}/partners/data_and_analytics/loyalty/openloyalty/) é uma plataforma de programa de fidelidade baseada em nuvem que permite criar e gerenciar programas de fidelidade e recompensas para clientes. A integração entre a Braze e o Open Loyalty sincroniza dados de fidelidade — como saldo de pontos, alterações de nível e avisos de expiração — diretamente na Braze em tempo real. Isso permite acionar mensagens personalizadas (e-mail, push, SMS) quando o status de fidelidade de um usuário muda.

#### OpenAI - Provedor de modelos de IA {#openai-ai-model-provider}

A [OpenAI]({{site.baseurl}}/partners/ai_model_providers/openai/) cria modelos avançados de IA, como o GPT, que permitem a compreensão e geração de linguagem natural, capacitando as marcas a construir e escalar interações significativas com os clientes.

#### Shopgate - Canais {#shopgate-channels}

O [Shopgate]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/shopgate/) é uma plataforma de comércio móvel e omnicanal que ajuda comerciantes a criar apps de compras e melhorar a eficiência de lojas físicas por meio de ferramentas de fulfillment e clienteling, ou seja, suporte personalizado ao cliente na loja com base em dados do cliente.

#### Splio - Dados e análises - Importação de coorte {#splio-data-and-analytics-cohort-import}

O [Splio]({{site.baseurl}}/partners/data_and_analytics/cohort_import/splio/) é uma ferramenta de construção de público que permite aumentar o número de campanhas e a receita sem prejudicar a experiência do cliente, e fornece análises para acompanhar o desempenho de campanhas de CRM tanto online quanto offline.

### SDK

#### Atualizações significativas do SDK {#sdk-breaking-updates}

As seguintes atualizações do SDK foram lançadas. As atualizações significativas estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [Android SDK 41.1.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 17.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [Swift SDK 14.0.2](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Xamarin SDK 9.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - Atualizada a vinculação do Android do [Braze Android SDK 37.0.0 para 41.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v41.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Atualizada a vinculação do iOS do [Braze Swift SDK 13.3.0 para 14.0.1](https://github.com/braze-inc/braze-swift-sdk/compare/13.3.0...14.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Adicionadas novas dependências transitivas do NuGet exigidas pelo Braze Android SDK:
        - Xamarin.AndroidX.DataStore.Preferences (1.1.7.1)
        - Xamarin.KotlinX.Serialization.Json.Jvm (1.9.0.2)
        - Xamarin.Kotlin.StdLib foi atualizado de 2.0.21.3 para 2.3.0.1. Se o seu projeto fixa explicitamente este pacote em uma versão mais antiga, você precisará atualizá-lo para evitar erros de restauração.
    - Removido o recurso News Feed.
        - Este recurso foi removido do SDK nativo do Android na versão [38.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v38.0.0).
        - Este recurso foi removido do SDK nativo do Swift na versão [14.0.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/14.0.0).
    - O caso de enum BRZInAppMessageDismissalReason.BRZInAppMessageDismissalReasonWipeData foi renomeado para BRZInAppMessageDismissalReason.WipeData.
- [Expo Plugin 4.0.0](https://github.com/braze-inc/braze-expo-plugin/releases/tag/4.0.0)
    - Esta versão requer a versão 19.0.0 do Braze React Native SDK.
    - (Android) Corrigido um vazamento de memória na camada de persistência de dados.
    - (Android) Adicionado suporte para `Braze.getInitialPushPayload()` para lidar com deep links de notificações por push quando o app é iniciado a partir de um estado encerrado. Isso resolve um problema em que deep links de notificações por push não eram tratados no Android quando o app era iniciado a frio.
- [React Native SDK 19.0.0](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/19.0.0)
    - Atualiza as vinculações da versão nativa do Swift SDK do Braze Swift SDK 13.3.0 para 14.0.1.
    - Atualiza as vinculações da versão nativa do Android SDK do Braze Android SDK 40.0.2 para 41.0.0.

{% enddetails %}

{% details 5 de fevereiro de 2026 %}

## Lançamento de 5 de fevereiro de 2026 {#february-5-2026-release}

### BrazeAI<sup>TM</sup>

#### Otimizador de Conteúdo {#content-optimizer}

{% multi_lang_include release_type.md release="Beta" %}

O [Otimizador de Conteúdo]({{site.baseurl}}/user_guide/brazeai/content_optimizer/) é uma etapa do Canvas de teste de conteúdo contínuo e de alta variância que oferece otimização automatizada do engajamento. Usando uma interface de arrastar e soltar semelhante à etapa de mensagem, você pode definir os componentes que deseja testar, gerar variantes usando IA (ou inseri-las manualmente) e usar Liquid tags para mapear esses componentes para o conteúdo da mensagem.

Criado com base em um otimizador de bandido multiarmado não contextual, o Otimizador de Conteúdo envia uma única mensagem por usuário, determinando qual combinação de variantes de componentes deve ser fornecida com base em recomendações preditivas. À medida que a etapa coleta dados ao longo do tempo, as variantes de alto desempenho aumentam naturalmente na alocação de envio, enquanto as variantes de baixo desempenho diminuem. O Otimizador de Conteúdo funciona melhor com Canvas de envio repetido que têm um volume diário consistente de usuários (pelo menos alguns milhares de usuários por dia) para permitir a otimização contínua.

### Dados e relatórios {#data-reporting}

#### Eventos recomendados para eCommerce {#ecommerce-recommended-events}

{% multi_lang_include release_type.md release="Early access" %}

Para combinar os eventos recomendados de eCommerce com o evento de compra existente, adicionamos o [evento de conversão "Places Order"]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases/#conversions-report), que é semelhante a "Makes Purchase".

### Canais e pontos de contato {#channels-touchpoints}

#### Traduzir localidades em banners {#translate-locales-in-banners}

{% multi_lang_include release_type.md release="Early access" %}

Depois de adicionar localidades ao seu espaço de trabalho, [direcione usuários em diferentes idiomas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/#translating-locales) tudo dentro de um único banner.

#### Configurar largura para Content Blocks de arrastar e soltar {#configure-width-for-drag-and-drop-content-blocks}

[Ajuste a largura do seu Content Block]({{site.baseurl}}/user_guide/channels/email/drag_and_drop/dnd_editor_blocks/#using-the-editor-to-add-a-content-block) selecionando o botão no menu de navegação. A largura padrão é 100% quando não especificada nas configurações globais de estilo do seu e-mail; caso contrário, as configurações globais serão respeitadas.

![Uma seta de dois lados com uma opção para editar a largura.]({% image_buster /assets/img_archive/content_block_width_updated.png %}){: style="max-width:30%;" }

#### Use o aquecimento automatizado de IP {#use-automated-ip-warming}

{% multi_lang_include release_type.md release="Early access" %}

Use o [aquecimento automatizado de IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/#automated-ip-warming) para aumentar gradualmente seu volume de envio diário, permitindo que os provedores de caixa de entrada aprendam e confiem em seus padrões de envio. A Braze envia primeiro para seus assinantes mais engajados, o que permite que o volume diário cresça em um ritmo que corresponda às práticas recomendadas.

### Parcerias {#partnerships}

#### LinkedIn – Canvas Audience Sync

Usando o [Braze Audience Sync para LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync/), adicione dados de usuários da sua integração com a Braze às listas de clientes do LinkedIn para fornecer anúncios com base em acionadores comportamentais, segmentação e muito mais. Qualquer critério que você normalmente usaria para acionar uma mensagem (como push, e-mail, SMS e webhook) em um Braze Canvas com base nos dados do usuário agora pode acionar um anúncio para esse usuário em suas listas de clientes do LinkedIn.

#### Oracle Crowdtwist - Dados e análises {#oracle-crowdtwist-data-analytics}

O [Oracle Crowdtwist]({{site.baseurl}}/partners/crowdtwist/) é uma solução líder de fidelização de clientes nativa da nuvem que capacita as marcas a oferecer experiências personalizadas aos clientes. Sua solução oferece mais de 100 caminhos de engajamento prontos para uso, proporcionando um rápido retorno do investimento para que os profissionais de marketing desenvolvam uma visão mais completa do cliente.

#### Fullstory - Conteúdo dinâmico {#fullstory-dynamic-content}

A plataforma de dados comportamentais da [Fullstory]({{site.baseurl}}/partners/fullstory/) ajuda os líderes de tecnologia a tomar decisões melhores e mais bem informadas. Ao injetar dados comportamentais digitais em sua pilha de análise, a tecnologia patenteada da Fullstory libera o poder dos dados comportamentais de qualidade em escala, transformando cada visita digital em insights acionáveis.

#### Open Loyalty - Dados e análises {#open-loyalty-data-analytics}

O [Open Loyalty]({{site.baseurl}}/partners/openloyalty/) é uma plataforma de programa de fidelidade baseada em nuvem que permite criar e gerenciar programas de fidelidade e recompensas para clientes. A integração entre a Braze e o Open Loyalty sincroniza dados de fidelidade — como saldo de pontos, alterações de nível e avisos de expiração — diretamente na Braze em tempo real. Isso permite acionar mensagens personalizadas (e-mail, push, SMS) quando o status de fidelidade de um usuário muda.

#### DOTS.ECO - Extensões {#dotseco-extensions}

O [DOTS.ECO]({{site.baseurl}}/partners/docs.eco) permite recompensar os usuários com impacto ambiental real por meio de certificados digitais rastreáveis. Cada certificado pode incluir metadados como um URL de certificado compartilhável e URL de imagem, para que os usuários possam visualizar (e revisitar) sua prova de impacto.

#### Mailizio - Orquestração de mensagens {#mailizio-message-orchestration}

O [Mailizio]({{site.baseurl}}/partners/mailizio/) é uma plataforma de criação e gerenciamento de e-mails que facilita o design de conteúdo reutilizável e seguro para a marca usando um editor visual intuitivo. Com a integração do Mailizio à Braze, exporte seus blocos de conteúdo e modelos de e-mail e, em seguida, gere automaticamente mensagens no app a partir desses mesmos ativos, permitindo a implantação rápida e totalmente controlada de campanhas.

### APIs

#### APIs POST da Biblioteca de mídia {#media-library-post-apis}

{% multi_lang_include release_type.md release="General availability" %}

Os ativos da Biblioteca de mídia agora podem ser adicionados via API, permitindo que clientes, parceiros e agências automatizem mais fluxos de trabalho de criação de mensagens. Use a [API]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create/) para fazer upload de um arquivo de ativo diretamente ou copiar um arquivo de um URL existente. Esse recurso desbloqueia recursos de integração e automação.

### Currents e Datashare {#currents-and-datashare}

#### Eventos do Console do agente para destinos de armazenamento e Datashare {#agent-console-events-for-storage-destinations-and-datashare}

{% multi_lang_include release_type.md release="General availability" %}

Dois novos [eventos](http://braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) estão agora disponíveis para destinos de armazenamento (AWS S3, GCS e Azure Blob Storage) e Snowflake Datashare: `agentconsole.AgentExecuted` e `agentconsole.ToolInvocation`. Esses eventos permitem que você analise o uso e os detalhes do Console do agente em seus sistemas downstream, ajudando-o a entender e aproveitar ao máximo o uso do agente. Os agentes permitem que você crie e implante agentes inteligentes que podem executar tarefas específicas na Braze, incluindo a geração de conteúdo em Canvas ou catálogos e o encaminhamento de usuários por diferentes caminhos com base em decisões inteligentes. Para saber mais, consulte o [changelog do Currents](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Novos eventos de "Retry" para canais individuais {#new-retry-events-for-individual-channels}

{% multi_lang_include release_type.md release="General availability" %}

Novos [eventos de nova tentativa](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) agora estão disponíveis para canais de e-mail, LINE, notificações por push, SMS, webhooks e WhatsApp. Esses eventos fornecem visibilidade de quando o limite de frequência resulta no atraso de uma mensagem programada em vez de abortá-la. Quando uma mensagem é despriorizada ou tem limite de frequência, ela agora pode ser repetida dentro de uma janela de repetição configurada, o que lhe dá uma visão melhor dos padrões de entrega de mensagens e dos impactos do limite de frequência. Para saber mais, consulte o [changelog do Currents](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Adicionar novo campo 'time_ms' ao evento TokenStateChange {#add-new-timems-field-to-tokenstatechange-event}

{% multi_lang_include release_type.md release="General availability" %}

Um novo campo `time_ms` foi adicionado ao evento [`users.behaviors.pushnotification.TokenStateChange`](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events), fornecendo granularidade em nível de milissegundos para rastrear alterações no estado do token por push. Essa precisão aprimorada ajuda você a entender o status mais recente de um token por push quando várias alterações ocorrem no mesmo segundo, dando-lhe confiança nos sistemas downstream de que você tem o status de inscrição correto. Para saber mais, consulte o [changelog do Currents](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Enviar usuário anônimo para destinos do Tealium {#send-anonymous-user-to-tealium-destinations}

{% multi_lang_include release_type.md release="General availability" %}

Os eventos que não têm um ID de usuário externo definido agora podem ser transmitidos para destinos do [Tealium]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_for_currents?redirected=1#tealium-for-currents). Ao marcar a caixa de seleção "Include events from anonymous users" na integração do Currents, os eventos sem um ID de usuário externo serão enviados ao destino em vez de serem suprimidos. Esse recurso é essencial para análises downstream e casos de uso que envolvem usuários não identificados e anônimos.

##### Enviar usuário anônimo para destinos CustomHTTP {#send-anonymous-user-to-customhttp-destinations}

{% multi_lang_include release_type.md release="Beta" %}

Os eventos que não têm um ID de usuário externo definido agora podem ser transmitidos para destinos CustomHTTP. Ao marcar a caixa de seleção "Include events from anonymous users" na integração do Currents, os eventos sem um ID de usuário externo serão enviados ao destino em vez de serem suprimidos. Esse recurso é essencial para análises downstream e casos de uso que envolvem usuários não identificados e anônimos.

#### Evento de abertura de e-mail — campo "machine_open" {#email-open-event-machineopen-field}

O [evento de abertura de e-mail]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/#email-open-events) agora gera o valor do campo "machine_open" para que você possa gerar relatórios sobre a métrica [_Abertura de máquina_]({{site.baseurl}}/user_guide/analytics/reporting/report_metrics/#machine-opens).

### SDK

As seguintes atualizações do SDK foram lançadas. O Swift SDK v14.0.1 corrige um problema com o manuseio de links universais. O Android SDK v40.2.0 corrige um possível vazamento de memória e resolve um problema com a abertura de várias sessões quando atividades transparentes estão presentes. O Expo SDK v3.2.0 adiciona a opção `forwardUniversalLinks` (padrão: false) para configurar o tratamento nativo de links universais do Swift SDK.

#### Atualizações significativas do SDK {#sdk-breaking-updates}

As seguintes atualizações do SDK foram lançadas. As atualizações significativas estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [Android SDK 41.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v41.0.0)
    - Renomeado `BrazeConfig.Builder.setIsLocationCollectionEnabled()` para `setIsAutomaticLocationCollectionEnabled()`.
    - Renomeado `BrazeConfig.isLocationCollectionEnabled` para `isAutomaticLocationCollectionEnabled`.
    - Renomeado `BrazeConfigurationProvider.isLocationCollectionEnabled` para `isAutomaticLocationCollectionEnabled`.
- [Android SDK 40.2.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4020)
- [Expo Plugin 3.2.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
- [Swift SDK 14.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)

{% enddetails %}

{% details 8 de janeiro de 2026 %}
## Lançamento de 8 de janeiro de 2026 {#january-8-2026-release}

### Dados e relatórios {#data-reporting}

#### Atualizações dos eventos do Currents {#updates-to-currents-events}

{% multi_lang_include release_type.md release="General availability" %}

As seguintes alterações foram feitas no Currents na Versão 4:

* Alterações de campo para o tipo de evento `users.behaviors.pushnotification.TokenStateChange`:
    * Adicionado novo campo `string` `push_token`: token por push do evento
* Alterações de campo para o tipo de evento `users.messages.pushnotification.Bounce`:
    * Adicionado novo campo `string` `push_token`: token por push do evento
* Alterações de campo para o tipo de evento `users.messages.pushnotification.Send`:
    * Adicionado novo campo `string` `push_token`: token por push do evento
* Alterações de campo para o tipo de evento `users.messages.rcs.Click`:
    * Adicionado novo campo `string` `canvas_variation_name`: nome da variação do Canvas que este usuário recebeu
    * O campo `user_phone_number` agora é *opcional*.
* Alterações de campo para o tipo de evento `users.messages.rcs.InboundReceive`:
    * O campo `user_id` agora é *opcional*.
* Alterações de campo para o tipo de evento `users.messages.rcs.Rejection`:
    * Adicionado novo campo `string` `canvas_step_message_variation_id`: API ID da variação da mensagem da etapa do Canvas que este usuário recebeu

Consulte o [changelog do Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/) para ver as alterações de eventos de cada versão.

#### Exportar registros de sincronização por todas as linhas {#export-sync-logs-by-all-rows}

{% multi_lang_include release_type.md release="Early access" %}

No [painel **Sync Log** da Ingestão de Dados na Nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/#exporting-sync-logs), você pode optar por exportar os registros em nível de linha para uma execução de sincronização por:

* **Rows with errors:** faz o download de um arquivo contendo apenas as linhas com status de **Error**.
* **All rows:** faz o download de um arquivo contendo todas as linhas processadas na execução.

### Canais e pontos de contato {#channels-touchpoints}

#### Conector Bring Your Own (BYO) WhatsApp {#bring-your-own-byo-whatsapp-connector}

O [conector Bring Your Own (BYO) WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/byo_connector/) oferece uma parceria entre a Braze e a Infobip, na qual você dá à Braze acesso ao seu Infobip WhatsApp Business Manager (WABA). Isso permite que você gerencie e pague pelos custos de mensagens diretamente com a Infobip enquanto usa a Braze para segmentação, personalização e orquestração de campanhas.

#### Banners no Canvas {#banners-in-canvas}

{% multi_lang_include release_type.md release="Early access" %}

Selecione **Banners** como canal de envio de mensagens em uma [etapa de Mensagem]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/) para o Canvas. Use o editor de arrastar e soltar para criar mensagens personalizadas em linha, proporcionando experiências não intrusivas e contextualmente relevantes que são atualizadas automaticamente no início de cada sessão do usuário.

#### BCC dinâmico {#dynamic-bcc}

{% multi_lang_include release_type.md release="General availability" %}

Com o [BCC dinâmico]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/?tab=bcc%20address#dynamic-bcc), use Liquid no seu endereço BCC. Observe que esse recurso está disponível apenas nas **Preferências de e-mail** e não pode ser definido na própria campanha. É permitido apenas um endereço BCC por destinatário de e-mail.

#### Limites de taxa baseados em canal {#channel-based-rate-limits}

Como alternativa a um limite de taxa compartilhado em toda uma campanha multicanal ou Canvas, selecione um limite de taxa específico por canal. Nesse caso, o limite de taxa se aplicará a cada um dos canais selecionados. Por exemplo, configure sua campanha ou Canvas para enviar no máximo 5.000 webhooks e 2.500 mensagens SMS por minuto em toda a campanha ou Canvas. Para mais detalhes, consulte [Limite de taxa e limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/).

### Parcerias {#partnerships}

#### LILT - Localização {#lilt-localization}

O [LILT]({{site.baseurl}}/partners/lilt/) é a solução completa de IA para tradução empresarial e criação de conteúdo. O LILT permite que organizações globais dimensionem e otimizem suas operações de conteúdo, produtos, comunicações e suporte, com agentes de IA e fluxos de trabalho totalmente automatizados.

### Atualizações significativas do SDK {#sdk-breaking-updates}

As seguintes atualizações do SDK foram lançadas. As atualizações significativas estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [Android 40.1.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4011)
- [Android SDK 40.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4010)
- [Swift SDK 14.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Remove o News Feed.
        - Isso remove totalmente todos os elementos de interface, modelos de dados e ações associadas ao News Feed.
- [Web SDK 6.4.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details 9 de dezembro de 2025 %}

## 9 de dezembro de 2025 {#december-9-2025}

### Dados e relatórios {#data-reporting}

#### Adição do Google Tag Manager a uma landing page {#adding-google-tag-manager-to-a-landing-page}

Para adicionar o Google Tag Manager às suas landing pages, adicione um bloco de código personalizado à sua landing page no editor de arrastar e soltar e, em seguida, [insira o código do Tag Manager]({{site.baseurl}}/user_guide/messaging/landing_pages/#adding-google-tag-manager-to-a-landing-page) no bloco.

### Orquestração {#orchestration}

#### Caso de uso do SMS Liquid {#sms-liquid-use-case}

O caso de uso [Responder com mensagens diferentes com base na palavra-chave do SMS de entrada]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases/#sms-keyword-response) incorpora o processamento dinâmico de palavras-chave do SMS para responder a mensagens de entrada específicas com diferentes textos de mensagem. Por exemplo, você pode enviar respostas diferentes quando alguém envia "START" ou "JOIN".

#### Lista de permissões para Conteúdo conectado {#allowlisting-for-connected-content}

Você pode adicionar URLs específicos à lista de permissões para uso com [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/). Para acessar esse recurso, entre em contato com o gerente de sucesso do cliente.

### Canais e pontos de contato {#channels-touchpoints}

#### Codificação de caracteres de SMS {#sms-character-encoding}

Nossa [calculadora de segmentos de SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator/#segment-calculator) agora tem codificação de caracteres! Selecione **Display Character Encoding** para identificar quais caracteres são codificados como GSM-7 ou UCS-2.

![Calculadora de segmentos de SMS com uma amostra de mensagem SMS inserida na caixa de texto e a codificação de caracteres ativada.]({% image_buster /assets/img/sms/character_encoding.png %}){: style="max-width:70%;"}

#### Mensagens do WhatsApp com otimização {#whatsapp-messages-with-optimization}

Como a MM API para WhatsApp não oferece 100% de entregabilidade, é importante entender como redirecionar os usuários que talvez não tenham recebido sua mensagem em outros canais.

Para redirecionar os usuários, recomendamos criar um segmento de usuários que não receberam uma mensagem específica. Para isso, filtre pelo código de erro `131049`, que indica que uma mensagem de modelo de marketing não foi enviada devido à aplicação do limite de modelo de marketing por usuário do WhatsApp. Você pode fazer isso [usando Braze Currents ou extensões de segmento SQL]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/optimized_delivery/#retargeting-users-on-other-braze-channels).

### Parcerias {#partnerships}

#### OtherLevels - Conteúdo dinâmico {#otherlevels-dynamic-content}

O [OtherLevels]({{site.baseurl}}/partners/otherlevels/) é uma plataforma de experiência que usa IA generativa para transformar a maneira como marcas esportivas, editoras e operadoras se conectam com seus clientes, transformando conteúdo tradicional em experiências de mídia avançada e vídeo personalizado de acordo com a marca em escala.

### SDK

#### Atualizações significativas do SDK {#sdk-breaking-updates}

As seguintes atualizações do SDK foram lançadas. As atualizações significativas estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [Web SDK 6.3.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details 11 de novembro de 2025 %}

## 11 de novembro de 2025 {#november-11-2025}

### Flexibilidade de dados {#data-flexibility}

#### Filtro de segmentação `Live Activities Push to Start Registered for App` {#live-activities-push-to-start-registered-for-app-segmentation-filter}

O filtro `Live Activities Push to Start Registered for App` segmenta seus usuários de acordo com o fato de estarem registrados para iniciar uma Live Activity por meio de notificações por push do iOS para um app específico.

#### Extensão de segmento SQL do RFM {#rfm-sql-segment-extension}

Você pode criar uma [extensão de segmento RFM (recência, frequência, monetário)]({{site.baseurl}}/rfm_segments/) para direcionar seus melhores usuários medindo seus hábitos de compra.

A análise de RFM é uma técnica de marketing que identifica seus melhores usuários pontuando-os em uma escala de 0 a 3 para cada categoria (recência, frequência, monetário), em que 3 é a melhor pontuação e 0 é a pior. Os valores de recência, frequência e monetário são todos baseados em dados de um intervalo de tempo específico de sua escolha.

#### Atributos personalizados — Valores {#custom-attributes-values}

Ao visualizar um relatório de uso, selecione a [guia **Values**]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/#values-tab) para visualizar os principais valores dos atributos personalizados selecionados com base em uma amostra de aproximadamente 250.000 usuários.

#### Registros de sincronização e observabilidade para Ingestão de Dados na Nuvem {#sync-logs-and-observability-for-cloud-data-ingestion}

{% multi_lang_include release_type.md release="General availability" %}

O [painel de Sync Log]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/) da Ingestão de Dados na Nuvem (CDI) permite monitorar todos os dados processados pelo CDI, verificar se os dados foram sincronizados com êxito e diagnosticar quaisquer problemas com dados "incorretos" ou ausentes.

#### Lançamentos de Feature Flag com múltiplas regras {#multi-rule-feature-flag-rollouts}

Use [lançamentos de Feature Flag com múltiplas regras]({{site.baseurl}}/developer_guide/feature_flags/create/#multi-rule-feature-flag-rollouts) para definir uma sequência de regras para avaliar os usuários, o que permite uma segmentação precisa e lançamentos de recursos controlados. Esse método é ideal para implementar o mesmo recurso em diversos públicos.

#### Mapeamento para campos de catálogo para blocos de produtos de arrastar e soltar {#mapping-to-catalog-fields-for-drag-and-drop-product-blocks}

Nas configurações do catálogo, você pode selecionar o botão de alternância **Product blocks** para [mapear para campos específicos]({{site.baseurl}}/user_guide/messaging/design_and_edit/product_blocks/#catalog-setup) e informações em seu catálogo. Isso permite que você selecione os campos a serem usados como título do produto, URL do produto e URL da imagem.

#### Eventos de cancelamento por limite de frequência no Currents {#frequency-capping-abort-events-in-currents}

Ao usar Currents, agora você pode fazer referência a `abort_type` nos eventos de cancelamento de canal. Isso identifica que uma mensagem foi abortada devido ao limite de frequência e inclui a regra de limite de frequência que causou o cancelamento. Isso ajuda a informar como você define suas regras de limite de frequência. Consulte [Eventos de engajamento de mensagens]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) para detalhes específicos dos eventos do Currents.

### Canais robustos {#robust-channels}

#### Imagens de fundo em linhas {#background-row-images}

{% multi_lang_include release_type.md release="General availability" %}

Você pode [adicionar uma imagem de fundo em linha]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings/#background-image) a uma mensagem no app ou landing page no painel **Row properties**. Ative a opção **Background image** e, em seguida, forneça o URL da imagem ou selecione uma imagem na [Biblioteca de mídia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/). Por fim, configure seu texto alternativo, tamanho, posição e se a imagem se repete para criar padrões na linha.

![Uma imagem de fundo em linha de uma pizza com um padrão de repetição horizontal.]({% image_buster /assets/img_archive/background_row.png %})

#### Copiar link de pré-visualização {#copy-preview-link}

Use **Copy preview link** em seus [Banners]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#step-5-test-your-message-optional), [rodapés personalizados de e-mail]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer/#creating-your-custom-footer) e [páginas de opt-in e cancelamento de inscrição de e-mail]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/?tab=custom%20footer#subscription-pages-and-footers) para gerar um link compartilhável que mostre como seu conteúdo será exibido para um usuário aleatório.

#### Mensagens do WhatsApp com entrega otimizada {#whatsapp-messages-with-optimized-delivery}

Use os sistemas avançados de IA do Meta para entregar suas mensagens de marketing a mais usuários que têm maior probabilidade de se engajar com elas, aumentando significativamente a entregabilidade e o engajamento com mensagens.

[As mensagens do WhatsApp com entrega otimizada]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/optimized_delivery/) são enviadas usando a nova [Marketing Messages Lite API](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/) do Meta, que oferece desempenho superior em comparação com a API tradicional da nuvem. Esse novo pipeline de envio ajuda você a alcançar melhor os usuários que valorizam e desejam receber suas mensagens.

#### WhatsApp Flows

Ao incorporar uma mensagem do WhatsApp Flow em um Braze Canvas ou campanha, talvez você queira capturar e utilizar informações específicas que os usuários enviam por meio do Flow. A Braze precisa receber informações adicionais sobre a estrutura da resposta do usuário, especificamente a forma esperada da resposta JSON, para gerar o esquema de atributo personalizado aninhado (NCA) necessário.

Agora você pode fornecer à Braze as informações sobre a estrutura da resposta [salvando a resposta do Flow como um atributo personalizado]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/whatsapp_flows/?tab=recommended%20method#step-1-generate-the-flow-custom-attribute) e concluindo um envio de teste.

#### Pré-visualização editável do usuário {#editable-user-preview}

Você pode [editar campos individuais de um usuário aleatório ou existente]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=webhook#customizing-an-existing-user) para ajudar a testar o conteúdo dinâmico em sua mensagem. Selecione **Edit** para converter o usuário selecionado em um usuário personalizado que possa ser modificado.

![A guia "Preview as a User" com um botão "Edit".]({% image_buster /assets/img_archive/edit_user_preview.png %}){: style="max-width:50%;"}

### Automação de IA e ML {#ai-and-ml-automation}

#### BrazeAI Decisioning Studio™ Go

Agora você pode configurar sua integração com o [BrazeAI Decisioning Studio™ Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/) consultando estes artigos de configuração para:

- [Braze]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/connect_data_sources/)
- [Klaviyo]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/connect_data_sources/)
- [Salesforce Marketing Cloud]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/connect_data_sources/)

#### Novos recursos para Braze Agents {#new-features-for-braze-agents}

{% multi_lang_include release_type.md release="Beta" %}

Agora você pode personalizar seu [Braze Agent]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/):

- Aplicando [diretrizes da marca]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines/) para que seu agente siga em sua resposta.
- Referenciando um catálogo para personalizar ainda mais sua mensagem.
- Estruturando a saída de um agente fornecendo o [formato de saída]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#output-format).
- Ajustando a [temperatura]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#temperature) para o nível de desvio da saída do seu agente.

### Modelos ChatGPT com BrazeAI Operator<sup>TM</sup> {#chatgpt-models-with-brazeai-operatortm}

{% multi_lang_include release_type.md release="Beta" %}

Você pode selecionar entre esses modelos GPT para usar em diferentes tipos de solicitação com o [Operator]({{site.baseurl}}/user_guide/brazeai/operator/):

- GPT-5 nano
- GPT-5 mini (padrão)
- GPT-5

### Novas parcerias da Braze {#new-braze-partnerships}

#### StackAdapt - Publicidade {#stackadapt-advertising}

O [StackAdapt]({{site.baseurl}}/partners/stackadapt/) é uma plataforma de marketing baseada em IA que oferece publicidade direcionada e orientada para desempenho. Ele permite que você sincronize dados de perfil de usuário da Braze com o StackAdapt Data Hub. Ao conectar as duas plataformas, você pode criar uma visão unificada dos seus clientes e ativar dados primários para melhorar o desempenho dos anúncios.

#### Cloudinary - Conteúdo dinâmico {#cloudinary-dynamic-content}

O [Cloudinary]({{site.baseurl}}/partners/cloudinary/) é uma plataforma de imagem e vídeo que permite gerenciar, editar, otimizar e fornecer imagens e vídeos em grande escala para qualquer campanha em todos os canais e jornadas de clientes. Quando integrado e ativado, o gerenciamento de mídia do Cloudinary potencializará e fornecerá a entrega de ativos dinâmicos, contextuais e personalizados para suas campanhas e Canvas da Braze.

#### Kameleoon - Testes A/B {#kameleoon-ab-testing}

O [Kameleoon]({{site.baseurl}}/partners/kameleoon/) é uma solução de otimização com experimentos, personalização baseada em IA e recursos de gerenciamento de recursos em uma única plataforma unificada.

### Atualizações do SDK {#sdk-updates}

As seguintes atualizações do SDK foram lançadas. As atualizações significativas estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [React Native SDK 18.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/16.1.0/CHANGELOG.md)
    - Corrige o tipo Typescript para o retorno de chamada de `subscribeToInAppMessage` e `addListener` para `Braze.Events.IN_APP_MESSAGE_RECEIVED`.
        - Esses ouvintes agora retornam corretamente um retorno de chamada com o novo tipo `InAppMessageEvent`. Anteriormente, os métodos eram anotados para retornar um tipo `BrazeInAppMessage`, mas na verdade estavam retornando um `String`.
         - Se estiver usando uma das APIs de assinatura, certifique-se de que o comportamento das suas mensagens no app não seja alterado após a atualização para esta versão. Veja nosso código de amostra em `BrazeProject.tsx`.
    - As APIs `logInAppMessageClicked`, `logInAppMessageImpression` e `logInAppMessageButtonClicked` agora aceitam apenas um objeto `BrazeInAppMessage` para corresponder à sua interface pública existente.
        - Anteriormente, aceitava tanto um objeto `BrazeInAppMessage` quanto um `String`.
    - `BrazeInAppMessage.toString()` agora retorna uma string legível em vez da representação de string JSON.
        - Para obter a representação de string JSON de uma mensagem no app, use `BrazeInAppMessage.inAppMessageJsonString`.
    - No iOS, `[[BrazeReactUtils sharedInstance] formatPushPayload:withLaunchOptions:]` foi movido para `[BrazeReactDataTranslator formatPushPayload:withLaunchOptions:]`.
        - Esse novo método agora é um método de classe em vez de um método de instância.
    - Adiciona anotações de nulabilidade aos métodos de `BrazeReactUtils`.
    - Remove os seguintes métodos e propriedades obsoletos da API:
        - `getInstallTrackingId(callback:)` em favor de `getDeviceId`.
        - `registerAndroidPushToken(token:)` em favor de `registerPushToken`.
        - `setGoogleAdvertisingId(googleAdvertisingId:adTrackingEnabled:)` em favor de `setAdTrackingEnabled`.
        - `PushNotificationEvent.push_event_type` em favor de `payload_type`.
        - `PushNotificationEvent.deeplink` em favor de `url`.
        - `PushNotificationEvent.content_text` em favor de `body`.
        - `PushNotificationEvent.raw_android_push_data` em favor de `android`.
        - `PushNotificationEvent.kvp_data` em favor de `braze_properties`.
    - Atualiza as vinculações da versão nativa do Android SDK [do Braze Android SDK 39.0.0 para 40.0.2](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.2#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [SDK do .NET MAUI (Xamarin) Versão 8.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - Atualizada a vinculação do iOS do [Braze Swift SDK 12.1.0 para 13.3.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.1.0...13.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed). Isso inclui suporte ao Xcode 26.
- [Flutter SDK 16.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - Atualiza a ponte nativa do Android do [Braze Android SDK 39.0.0 para 40.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Braze Swift SDK 13.3.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Web SDK 6.3.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Android SDK 40.0.0-40.0.2](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details 14 de outubro de 2025 %}

## Lançamento de 14 de outubro de 2025 {#october-14-2025-release}

### BrazeAI Decisioning Studio™

O [BrazeAI Decisioning Studio™](https://www.braze.com/product/brazeai-decisioning-studio/) substitui os testes A/B por decisões de IA que personalizam tudo e maximizam qualquer métrica: gere receita, não cliques. Com o BrazeAI Decisioning Studio™, você pode otimizar qualquer KPI de negócios. Consulte a nossa seção dedicada [BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/) para ver exemplos de casos de uso e os principais recursos.

### Flexibilidade de dados {#data-flexibility}

#### Novos eventos do Currents {#new-currents-events}

Esses novos eventos foram adicionados ao [glossário do Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/):

- `users.messages.rcs.Click`
- `users.messages.rcs.Rejection`
- `users.messages.line.Abort`
- `users.messages.line.Send`
- `users.messages.line.InboundReceive`
- `users.messages.line.Click`
- `users.messages.rcs.Delivery`
- `users.messages.rcs.InboundReceive`
- `users.messages.rcs.Read`
- `users.messages.rcs.Send`
- `users.messages.rcs.Abort`
- `users.messages.inappmessage.Abort`

Esses novos campos foram adicionados aos seguintes eventos do Currents:

- `is_sms_fallback`:
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.Rejection`
- `message_id`, `in_reply_to`, `flow_id`, `flow_response_json`, `product_id`, `catalog_id`:
  - `users.messages.whatsapp.InboundReceive`
- `message_id`, `flow_id`, `template_name`:
  - `users.messages.whatsapp.Send`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.Read`

#### Listas de supressão {#suppression-lists}

{% multi_lang_include release_type.md release="General availability" %}

[Listas de supressão]({{site.baseurl}}/user_guide/audience/suppression_lists/) são grupos de usuários que automaticamente não recebem nenhuma campanha ou Canvas. As listas de supressão são definidas por filtros de segmento, e os usuários entram e saem das listas de supressão à medida que atendem aos critérios de filtro.

#### Personalização sem cópia {#zero-copy-personalization}

{% multi_lang_include release_type.md release="Early access" %}

Sincronize os acionadores do Canvas usando a Ingestão de Dados na Nuvem para [personalização sem cópia]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync/). Esse recurso acessa informações específicas do usuário da sua solução de armazenamento de dados e as transmite para um Canvas de destino. As etapas do Canvas podem, opcionalmente, incluir campos de personalização que não são mantidos nos perfis de usuário da Braze.

#### Variáveis de contexto do Canvas para etapas de Jornadas do público e Divisão de decisão {#canvas-context-variables-for-audience-paths-and-decision-split-steps}

{% multi_lang_include release_type.md release="Early access" %}

Você pode [criar filtros de variáveis de contexto]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/#context-variable-filters) que usam variáveis de contexto declaradas anteriormente nas etapas [Jornadas do público]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths/) e [Divisão de decisão]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/).

### Liberando a criatividade {#unlocking-creativity}

#### Deal Cards para e-mails {#deal-cards-for-emails}

Use [Deal Cards]({{site.baseurl}}/user_guide/channels/email/html_editor/gmail_promotions_tab/) para fornecer informações importantes sobre ofertas diretamente no topo do corpo do e-mail. Isso permite que os destinatários entendam rapidamente os detalhes da oferta e tomem providências.

#### Modelos para Banners {#templates-for-banners}

Ao [compor seu Banner]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/), agora você pode começar com um modelo em branco, usar um modelo da Braze ou selecionar um modelo de Banner salvo.

### Canais robustos {#robust-channels}

#### Listas de supressão {#suppression-lists}

{% multi_lang_include release_type.md release="General availability" %}

[Listas de supressão]({{site.baseurl}}/user_guide/audience/suppression_lists/) especificam grupos de usuários que nunca receberão mensagens. Os administradores podem criar listas de supressão com filtros de segmento para restringir um grupo de usuários da mesma forma que você faria para segmentação.

#### Rastreamento de cliques no LINE {#line-click-tracking}

{% multi_lang_include release_type.md release="General availability" %}

Quando o [rastreamento de cliques LINE]({{site.baseurl}}/line/click_tracking/) está ativado, a Braze encurta automaticamente seus URLs, adiciona mecanismos de rastreamento e registra os cliques em tempo real. Enquanto o LINE oferece dados agregados de cliques, a Braze fornece informações granulares do usuário que são oportunas e acionáveis. Esses dados permitem que você crie estratégias de segmentação e redirecionamento mais direcionadas, como a segmentação de usuários com base no comportamento de cliques e o acionamento de mensagens em resposta a cliques específicos.

#### Filtragem de cliques de bots de SMS e RCS {#sms-and-rcs-bot-click-filtering}

{% multi_lang_include release_type.md release="General availability" %}

A [filtragem de cliques de bots de SMS e RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/bot_click_filtering/) aprimora a análise de campanhas e os fluxos de trabalho, excluindo cliques suspeitos de bots. Um "clique de bot" refere-se a cliques automatizados em links encurtados em mensagens SMS e RCS, como os de rastreadores da web, pré-visualizações de links do Android e iOS ou software de segurança CPaaS. Esse recurso facilita a geração de relatórios precisos, a segmentação e a orquestração para engajar usuários reais.

#### Transferir números de telefone do WhatsApp {#transfer-whatsapp-phone-numbers}

Transfira um número de telefone da WhatsApp Business Account (WABA) e seu grupo de inscrições associado [de um espaço de trabalho para outro]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/transfer_between_workspaces/) na Braze.

#### Mensagens de resposta e pré-visualização do WhatsApp Flows {#whatsapp-flows-response-messages-and-preview}

Em um Canvas, você pode criar uma etapa de mensagem do WhatsApp que use uma [mensagem de resposta]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/whatsapp_flows/?tab=response%20message#configuring-whatsapp-flow-messages-and-responses) e mensagem de fluxo. Você também pode selecionar **Preview Flow** para pré-visualizar o Flow diretamente na Braze e confirmar que ele se comporta como esperado.

#### Mensagens de produto no WhatsApp {#whatsapp-product-messages}

[Mensagens de produto]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/product_messages/) permitem que você envie mensagens interativas do WhatsApp que exibem produtos diretamente do seu catálogo do Meta.

#### Integração da Braze e WhatsApp com um sistema externo {#integrating-braze-and-whatsapp-with-an-external-system}

[Aproveite o poder dos chatbots com IA e das transferências de agentes ao vivo]({{site.baseurl}}/user_guide/channels/whatsapp/use_cases/whatsapp_and_external_systems/) no canal do WhatsApp para otimizar suas operações de suporte ao cliente. Ao automatizar as consultas de rotina e fazer a transição perfeita para agentes humanos quando necessário, você pode melhorar significativamente os tempos de resposta e aprimorar a experiência geral do cliente.

### Automação de IA e ML {#ai-and-ml-automation}

#### Braze Agents

{% multi_lang_include release_type.md release="Beta" %}

Os [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/) são ajudantes com tecnologia de IA que você pode criar dentro da Braze. Os agentes podem gerar conteúdo, tomar decisões inteligentes e enriquecer seus dados para que você possa oferecer experiências mais personalizadas aos clientes.

### Novas parcerias da Braze {#new-braze-partnerships}

#### Jasper - Modelos {#jasper-templates}

A integração do [Jasper]({{site.baseurl}}/partners/jasper/) com a Braze permite que você otimize a criação de conteúdo e a execução de campanhas. Com o Jasper, suas equipes de marketing podem gerar textos de alta qualidade e alinhados à marca em minutos. A Braze então facilita a entrega dessas mensagens ao público certo no momento ideal. Essa integração promove fluxos de trabalho contínuos, reduz o esforço manual e gera resultados de engajamento mais sólidos.

#### Swym - Fidelidade e redirecionamento {#swym-loyalty-and-retargeting}

O [Swym]({{site.baseurl}}/partners/swym/) ajuda marcas de eCommerce a capturar a intenção de compra com alertas de Wishlists, Save for Later, Gift Registry e Back-in-Stock. Usando dados avançados e baseados em permissões, você pode criar campanhas hiperdirecionadas e oferecer experiências de compras personalizadas que impulsionam o engajamento, aumentam as conversões e a fidelidade.

### Atualizações do SDK {#sdk-updates}

As seguintes atualizações do SDK foram lançadas. As atualizações significativas estão listadas abaixo; você pode encontrar todas as outras atualizações verificando os changelogs correspondentes do SDK.

- [Cordova SDK 14.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - Atualizada a ponte nativa do Android [do Braze Android SDK 37.0.0 para 39.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - A versão mínima exigida do GradlePluginKotlinVersion agora é 2.1.0.
    - Atualizada a ponte nativa do iOS [do Braze Swift SDK 12.0.0 para 13.2.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed). Isso inclui suporte ao Xcode 26.
    - Remove o suporte ao News Feed. As seguintes APIs foram removidas:
        - `launchNewsFeed`
        - `getNewsFeed`
        - `getNewsFeedUnreadCount`
        - `getNewsFeedCardCount`
        - `getCardCountForCategories`
        - `getUnreadCardCountForCategories`
- [React Native SDK 17.0.0-17.0.1](https://www.npmjs.com/package/@braze/react-native-sdk/v/17.0.1)
    - Atualiza as vinculações da versão nativa do Android SDK [do Braze Android SDK 37.0.0 para 39.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Remove o suporte ao News Feed. As seguintes APIs foram removidas:
        - `launchNewsFeed`
        - `requestFeedRefresh`
        - `getNewsFeedCards`
        - `logNewsFeedCardClicked`
        - `logNewsFeedCardImpression`
        - `getCardCountForCategories`
        - `getUnreadCardCountForCategories`
        - `Braze.Events.NEWS_FEED_CARDS_UPDATED`
        - `Braze.CardCategory`
- [Web SDK 6.2.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 15.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [Unity SDK 10.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
    - Atualizada a ponte nativa do iOS [do Braze Swift SDK 12.0.0 para 13.2.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed). Isso inclui suporte ao Xcode 26.

{% enddetails %}
{% details 16 de setembro de 2025 %}

## Lançamento de 16 de setembro de 2025 {#september-16-2025-release}

### Flexibilidade de dados {#data-flexibility}

#### Braze Data Platform

A Braze Data Platform é um conjunto abrangente e componível de recursos de dados e integrações de parceiros que permite criar experiências personalizadas e impactantes em todo o ciclo de vida do cliente. Saiba mais sobre os três trabalhos relacionados a dados a serem realizados:

- [Unificação de dados]({{site.baseurl}}/user_guide/data/unification/)
- [Ativação de dados]({{site.baseurl}}/user_guide/data/activation/)
- [Distribuição de dados]({{site.baseurl}}/user_guide/data/distribution/)

#### Propriedades personalizadas de Banner {#custom-banner-properties}

{% multi_lang_include release_type.md release="Early access" %}

Você pode usar propriedades personalizadas da sua campanha de Banner para recuperar dados de chave-valor por meio do SDK e modificar o comportamento ou a aparência do seu app. Para saber mais, consulte [Propriedades personalizadas de Banner]({{site.baseurl}}/developer_guide/banners/placements/#custom-properties).

#### Autenticação por token {#token-authentication}

{% multi_lang_include release_type.md release="General availability" %}

Ao usar Conteúdo conectado na Braze, você poderá descobrir que certas APIs exigem um token em vez de um nome de usuário e senha. A Braze pode armazenar credenciais que contêm [valores de cabeçalho de autenticação por token]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/#using-token-authentication).

#### Códigos de promoção {#promotion-codes}

Você pode salvar códigos de promoção no perfil de um usuário por meio de uma etapa de Atualização de usuário. Para saber mais, consulte [Salvando códigos de promoção em perfis de usuário]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/#save-to-profile).

### Liberando a criatividade {#unlocking-creativity}

#### Braze Pilot

O [Braze Pilot]({{site.baseurl}}/user_guide/get_started/braze_pilot/) é um app disponível publicamente para Android e iOS que permite lançar mensagens do seu dashboard da Braze para o seu telefone. Consulte [Introdução ao Braze Pilot]({{site.baseurl}}/user_guide/get_started/braze_pilot/getting_started/) para um passo a passo sobre o download do app, a inicialização da conexão com o dashboard da Braze e a conclusão da configuração.

### Novas parcerias da Braze {#new-braze-partnerships}

#### Blings - Conteúdo visual e interativo {#blings-visual-and-interactive-content}

O [Blings]({{site.baseurl}}/partners/blings/) é uma plataforma de vídeo personalizado de última geração que permite oferecer experiências de vídeo em tempo real, interativas e orientadas por dados em todos os canais e em grande escala.

#### Integração padrão da Shopify com ferramenta de terceiros {#shopify-standard-integration-with-third-party-tool}

Para lojas online da Shopify, recomendamos usar o método de integração padrão da Braze para oferecer suporte aos SDKs da Braze em seu site.

No entanto, entendemos que você pode preferir usar uma ferramenta de terceiros, como o Google Tag Manager, por isso elaboramos um guia sobre como fazer isso. Para começar, consulte [Shopify: marcação de terceiros]({{site.baseurl}}/shopify_standard_integration_third_party_tagging/).

### Atualizações do SDK {#sdk-updates}

As seguintes atualizações do SDK foram lançadas. As atualizações significativas estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [Braze Flutter SDK 15.0.0](https://github.com/braze-inc/braze-flutter-sdk/blob/main/CHANGELOG.md#1500)
    - Atualiza a ponte nativa do Android do Braze Android SDK `36.0.0` para `39.0.0`.
    - Atualiza a ponte nativa do iOS do Braze Swift SDK `12.0.0` para `13.2.0`. Isso inclui suporte ao Xcode 26.

- [Braze Swift SDK 7.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1300)
  - Atualiza as vinculações do Braze Swift SDK para exigir versões da denominação `13.0.0+` SemVer. Isso permite compatibilidade com qualquer versão do Braze SDK de `13.0.0` até, mas não incluindo, `14.0.0`.

{% enddetails %}
{% details 19 de agosto de 2025 %}

## Lançamento de 19 de agosto de 2025 {#august-19-2025-release}

### Padronização da consistência de fuso horário para o Canvas Context {#time-zone-consistency-standardization-to-canvas-context}

{% multi_lang_include release_type.md release="Early access" %}

Se você estiver participando do [acesso antecipado à etapa de Contexto do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/), todos os carimbos de data/hora com tipo datetime das propriedades de eventos de acionamento em Canvas baseados em ações serão sempre normalizados para [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). Para saber mais sobre isso, consulte [Padronização da consistência de fuso horário]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/#time-zone-consistency-standardization).

### Flexibilidade de dados {#data-flexibility}

#### Domínios personalizados de autoatendimento {#self-serve-custom-domains}

{% multi_lang_include release_type.md release="General access" %}

[Domínios personalizados de autoatendimento]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/custom_domains/) permitem que você configure e gerencie seus próprios domínios personalizados para SMS, RCS e WhatsApp — diretamente do dashboard da Braze. Você pode adicionar, monitorar e gerenciar facilmente até 10 domínios personalizados em um só lugar.

#### Estatísticas de funil de segmento {#segment-funnel-statistics}

Selecione [Exibir estatísticas do funil]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/#viewing-funnel-statistics) para exibir as estatísticas desse grupo de filtros e ver como cada filtro adicionado afeta as estatísticas do segmento. Você verá uma contagem estimada e uma porcentagem de usuários que são direcionados por todos os filtros até esse ponto. Depois que as estatísticas forem exibidas para um grupo de filtros, elas serão atualizadas automaticamente sempre que você alterar os filtros.

#### Novos campos de resposta para o endpoint `/campaigns/details` para notificações por push {#new-response-fields-for-campaignsdetails-endpoint-for-push-notifications}

A resposta `messages` para notificações por push agora inclui dois novos campos:

- `image_url`: um URL de imagem para uma imagem de notificação do Android, uma imagem de notificação do iOS ou uma imagem de ícone de push para a web.
- `large_image_url`: um URL de imagem de notificação da web para ações de push da web do Android Chrome e Windows.

#### Definição de campos de PII {#defining-pii-fields}

Selecionar e [definir determinados campos como campos de PII]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings/#view-pii) afeta apenas o que os usuários podem visualizar no dashboard da Braze e não afeta a forma como os dados do usuário final nesses campos de PII são tratados.

Consulte sua equipe jurídica para alinhar as configurações do seu dashboard com as normas e políticas de privacidade aplicáveis à sua empresa, inclusive aquelas relacionadas à [retenção de dados]({{site.baseurl}}/api/data_retention/).

#### Compartilhamento de um link de download do Criador de relatórios {#sharing-a-report-builder-download-link}

Você pode [compartilhar um link do dashboard]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/#sharing-a-report) para o relatório selecionando **Share** e, em seguida, **Share a link** ou **Send or schedule an email**.

### Liberando a criatividade {#unlocking-creativity}

#### Tags de cabeçalho personalizadas para e-mails de arrastar e soltar {#custom-head-tags-for-drag-and-drop-emails}

Use tags `<head>` para adicionar CSS e metadados em sua mensagem de e-mail. Por exemplo, você pode usar essas tags para adicionar uma folha de estilo ou um favicon. O Liquid é compatível com as tags `<head>`.

### Canais robustos {#robust-channels}

#### Práticas recomendadas de opt-out difuso {#fuzzy-out-out-best-practices}

Adicionamos uma [seção de práticas recomendadas]({{site.baseurl}}) para ajudá-lo a configurar cuidadosamente sua mensagem de opt-out difuso e criar uma experiência clara, compatível e positiva para seus assinantes.

#### WhatsApp Flows

{% multi_lang_include release_type.md release="Early access" %}

O [WhatsApp Flows]({{site.baseurl}}/whatsapp_flows/) é um aprimoramento do canal existente do WhatsApp, permitindo que você crie experiências de mensagens interativas e dinâmicas.

#### Perguntas sobre produtos recebidas pelo WhatsApp {#whatsapp-inbound-product-questions}

Os usuários podem responder à mensagem do seu produto ou catálogo com [perguntas sobre o produto]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/product_messages/#receiving-inbound-product-questions). Elas chegam como mensagens de entrada, que podem ser classificadas com uma Jornada de ação.

Além disso, a Braze extrai o ID do produto e o ID do catálogo dessas perguntas, portanto, se desejar automatizar as respostas ou enviar perguntas para outra equipe (como o suporte ao cliente), você poderá incluir esses detalhes.

### Automação de IA e ML {#ai-and-ml-automation}

#### Novos artigos sobre casos de uso do BrazeAI<sup>TM</sup> {#new-brazeai-use-case-articles}

Adicionamos novos artigos de casos de uso para ajudá-lo a obter o máximo do BrazeAI<sup>TM</sup>. Esses guias destacam maneiras práticas de aplicar a IA em suas estratégias de engajamento, incluindo:

- [Predictive Churn]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/use_case/): identifique os clientes em risco de churn e tome medidas antecipadamente.
- [Predictive Events]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/use_case/): antecipe as principais ações do usuário e molde as experiências em tempo real.
- [Recomendações]({{site.baseurl}}/user_guide/brazeai/recommendations/use_case /): forneça conteúdo e produtos mais relevantes com base no comportamento do cliente.

#### Servidor MCP {#mcp-server}

{% multi_lang_include release_type.md release="Beta" %}

O [servidor Braze MCP]({{site.baseurl}}/user_guide/brazeai/mcp_server/), uma conexão segura e somente leitura, permite que ferramentas de IA como Claude e Cursor acessem dados da Braze sem PII para responder a perguntas, analisar tendências e fornecer insights sem alterar os dados.

### Atualizações do SDK {#sdk-updates}

As seguintes atualizações do SDK foram lançadas. As atualizações significativas estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [Swift SDK 13.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Amplia a funcionalidade de `BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)` para ser acionado em caso de erros de autenticação "Optional".
        - O método delegado `BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)` agora será acionado para erros de autenticação "Required" e "Optional".
        - Se você quiser tratar apenas os erros de autenticação "Required" do SDK, adicione uma verificação para garantir que `BrazeSDKAuthError.optional` seja falso dentro da implementação desse método delegado.
    - Corrige o uso de `Braze.Configuration.sdkAuthentication` para que tenha efeito quando ativado.
        - Anteriormente, o valor dessa configuração não era consumido pelo SDK e o token era sempre anexado às solicitações, se estivesse presente.
        - Agora, o SDK só anexará o token de autenticação do SDK às solicitações de rede de saída quando essa configuração estiver ativada.
    - Os setters de todas as propriedades de `Braze.FeatureFlag` e de todas as propriedades de `Braze.Banner` foram tornados `private`. As propriedades dessas classes agora são somente leitura.
    - Remove a propriedade `Braze.Banner.id`, que foi descontinuada na versão `11.4.0`.
        - Em vez disso, use `Braze.Banner.trackingId` para ler o ID de rastreamento de campanha de um banner.
- [React Native SDK 16.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - Atualiza as vinculações da versão nativa do Android SDK do [Braze Android SDK 36.0.0 para 37.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Atualiza as vinculações da versão nativa do Swift SDK do [Braze Swift SDK 12.0.0 para 13.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - O evento `sdkAuthenticationError` agora será acionado para erros de autenticação "Required" e "Optional".
- [Xamarin SDK 7.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/7.0.0/CHANGELOG.md)
    - Adicionado suporte ao .NET 9.0 para as vinculações com iOS e Android.
        - Isso remove o suporte ao .NET 8.0.
        - Isso requer uma [versão mínima do iOS 12.2](https://learn.microsoft.com/en-us/dotnet/maui/whats-new/dotnet-9?view=net-maui-9.0).
    - Atualizada a vinculação do Android do [Braze Android 32.0.0 para 37.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v32.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Atualizada a vinculação do iOS do [Braze Swift SDK 10.0.0 para 12.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/10.0.0...12.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Esta versão contém APIs para o recurso Banners, mas atualmente não é totalmente compatível com este SDK. Se desejar usar Banners em seu app .NET MAUI, entre em contato com o gerente de suporte ao cliente antes de integrá-lo ao seu aplicativo.
- [Cordova SDK 13.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1300)
    - Atualizada a implementação interna do iOS do método `enableSdk` para usar `setEnabled`: em vez de `_requestEnableSDKOnNextAppRun`, que foi descontinuado no Swift SDK.
    - A chamada desse método não exige mais que o app seja reiniciado para ter efeito. O SDK será ativado assim que esse método for executado.
    - Atualizada a ponte nativa do Android do [Braze Android SDK `36.0.0` para `37.0.0`](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).

{% enddetails %}