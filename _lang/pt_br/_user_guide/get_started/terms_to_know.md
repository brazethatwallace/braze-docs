---
page_order: 10
nav_title: Termos a conhecer
article_title: Termos da Braze para conhecer

layout: glossary_page
glossary_top_header: "Termos a serem conhecidos"
glossary_top_text: "Esses termos devem ajudar você a começar sua jornada para criar melhores vínculos com clientes e usuários com a Braze. Leia este conteúdo antes de começar sua integração."
page_type: glossary
description: "Este glossário abrange termos importantes que você deve conhecer durante o processo de integração na Braze."

glossaries:
  - name: Active user
    description: "Para direcionamento de Campaigns, a Braze define um <a href=\"https://www.braze.com/docs/user_guide/messaging/campaigns/ideas_and_strategies/active_user_campaigns\">usuário ativo</a> em um determinado período como qualquer pessoa que tenha uma sessão nesse período (usuários atualizados pela API também contam para esse período). Para <a href=\"https://www.braze.com/docs/user_archival/#active-users\">arquivamento de usuários</a> e estatísticas de alcance, a Braze usa uma definição mais ampla que também inclui atualizações de perfil, mensagens enviadas ao usuário e interações com mensagens."
  - name: Alloys
    description: "Alloys são nossos <a href=\"https://www.braze.com/docs/partners/home/\">Parceiros de tecnologia</a>."
  - name: Anonymous users
    description: "Quando um perfil de usuário é reconhecido por meio do SDK, um perfil de usuário anônimo é criado com o <a href=\"https://www.braze.com/docs/api/basics/#user-ids\">ID de usuário da Braze</a> associado."
  - name: API campaigns
    description: "<a href=\"https://www.braze.com/docs/api/api_campaigns/\">Campaigns da API</a> usam o dashboard da Braze para gerar um <code>campaign_id</code> (e IDs de variação) enquanto você fornece o texto, o público, o agendamento e os ativos por meio das <a href=\"https://www.braze.com/docs/api/endpoints/messaging/\">APIs de envio de mensagens</a>. Elas diferem das <a href=\"https://www.braze.com/docs/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery/\">Campaigns disparadas por API</a>, em que você dispara uma Campaign totalmente configurada no dashboard por meio da API."
  - name: Application program interface (API)
    description: "A <a href=\"https://www.braze.com/docs/api/basics/#api-overview\">API da Braze</a> fornece um serviço da Web em que é possível registrar as ações realizadas pelos usuários diretamente via HTTP, em vez de usar os SDKs móveis. Isso permite, por exemplo, passar dados de usuários para a Braze que não são rastreados em seu app ou site."
  - name: App instance
    description: As instâncias do app referem-se aos diferentes sites e aplicativos que são coletados em um espaço de trabalho.
  - name: Braze (the product)
    description: "Às vezes chamado de dashboard, esse produto controla todos os dados e interações no centro da plataforma Braze. Os clientes da Braze o utilizam para gerenciar notificações, configurar Campaigns de mensagens direcionadas e visualizar análise de dados. Os desenvolvedores o utilizam para gerenciar as configurações de integração de apps, como chaves de API e credenciais de notificação por push."
  - name: Team
    description: "Os administradores da Braze podem dividir um subconjunto de usuários do dashboard em <a href=\"https://www.braze.com/docs/user_guide/administer/global/user_management/teams\">equipes</a> com funções e permissões de usuário variadas. Isso permite que os administradores da Braze limitem o acesso a determinados recursos por associação a grupos."
  - name: Campaign
    description: "Campaigns são métodos de envio de mensagens personalizáveis para fornecer respostas personalizadas aos seus clientes. Você pode <a href=\"https://www.braze.com/docs/user_guide/messaging/campaigns\">criar Campaigns</a> usando diferentes canais de envio de mensagens para enviar suas mensagens exclusivas."
  - name: Canvas
    description: "<a href=\"https://www.braze.com/docs/user_guide/messaging/canvas\">Canvas</a> é uma interface única e unificada na qual os profissionais de marketing podem configurar Campaigns com várias mensagens e etapas para formar uma jornada coesa. O Canvas permite comparar e otimizar essas experiências usando análise de dados abrangente para a experiência completa do usuário."
  - name: Connected Content
    description: "<a href=\"https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/connected_content\">Conteúdo conectado</a> amplia a personalização do marketing para aumentar o engajamento e as conversões dos clientes. É possível inserir qualquer informação acessível usando a API diretamente nas mensagens enviadas aos usuários. O Conteúdo conectado permite extrair conteúdo diretamente de seu servidor da Web ou de APIs acessíveis publicamente."
  - name: Content Cards
    description: "<a href=\"https://www.braze.com/docs/user_guide/channels/content_cards\">Content Cards</a> permitem o envio de um fluxo dinâmico e altamente direcionado de conteúdo avançado para seus clientes diretamente nos apps que eles adoram, sem interromper a experiência deles. Content Cards podem ser enviados para usuários de iOS, Android e Web."
  - name: Conversion event
    description: "Um <a href=\"https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/conversion_events\">evento de conversão</a> é uma métrica de sucesso que registra se um destinatário realizou uma ação de alto valor dentro de uma janela de conversão após receber sua mensagem (ou após entrar em um Canvas ou grupo de controle, dependendo do canal e da configuração). Use eventos de conversão para medir o desempenho de Campaigns e Canvas além dos envios."
  - name: Currents
    description: "<a href=\"https://www.braze.com/docs/user_guide/data/distribution/braze_currents\">Currents</a>, nossa exportação de fluxo de dados, está incluído em determinados pacotes da Braze. O Braze Currents permite a integração por meio do armazenamento de dados usando arquivos simples ou com nossos parceiros de análise comportamental e dados de clientes usando cargas úteis JSON em lote para um endpoint designado."
  - name: Custom attributes
    description: "<a href=\"https://www.braze.com/docs/user_guide/data/activation/attributes/custom_attributes\">Atributos personalizados</a> são uma coleção de características exclusivas de seus usuários. Eles são ideais para armazenar atributos sobre seus usuários ou informações sobre ações de baixo valor dentro do seu aplicativo. É possível atribuir atributos personalizados aos usuários dentro do dashboard. É possível filtrar e segmentar seus usuários de acordo com esses atributos para Campaigns <a href=\"https://www.braze.com/docs/developer_guide/analytics/setting_user_attributes/?sdktab=swift\">Swift</a> e <a href=\"https://www.braze.com/docs/developer_guide/analytics/setting_user_attributes/?sdktab=android\">Android</a>."
  - name: Custom events
    description: "<a href=\"https://www.braze.com/docs/user_guide/data/activation/events/custom_events\">Eventos personalizados</a> são ações realizadas pelos usuários; eles são mais adequados para o rastreamento de interações de alto valor do usuário com o seu aplicativo."
  - name: Data point
    description: "Um ponto de dados é contado quando um <a href=\"https://www.braze.com/docs/user_guide/data/activation/attributes/custom_attributes\">atributo personalizado</a> é definido ou atualizado (mesmo que esteja sendo atualizado com o mesmo valor), um <a href=\"https://www.braze.com/docs/user_guide/data/activation/events/custom_events\">evento personalizado</a> ou um evento de compra é registrado, qualquer dado padrão (por exemplo, <code>email</code>, <code>first_name</code>, <code>last_name</code>, <code>country</code> ou <code>home_city</code>) é registrado, quando uma sessão começa e quando uma sessão termina."
  - name: Deep linking
    description: "<a href=\"https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls/\">Deep links</a> são usados para direcionar os clientes para sua próxima ação ou engajamento. Usando deep links, é possível conectar uma mensagem a um conteúdo direcionado em um site ou app móvel."
  - name: Dormant users
    description: "Um usuário é considerado <a href=\"https://www.braze.com/docs/user_archival/#dormant-users\">inativo</a> quando não houve nenhuma atividade qualificada nos últimos doze meses — ele não usou nenhum app ou site no espaço de trabalho, não recebeu nenhuma mensagem do espaço de trabalho e não foi atualizado há mais de doze meses. Por padrão, a Braze usa uma janela de doze meses para arquivamento de inativos; as configurações da sua empresa podem substituir o número de dias."
  - name: Endpoint
    description: "Uma extremidade de um canal de comunicação, também conhecida como <a href=\"https://www.braze.com/docs/api/endpoints/\">endpoint</a> de API, é usada na API de envio de mensagens da Braze para enviar e agendar mensagens."
  - name: Exception event
    description: "No Canvas, <a href=\"https://www.braze.com/docs/user_guide/messaging/canvas/create_a_canvas/exit_criteria#exception-events\">eventos de exceção</a> são ações específicas que removem um usuário da jornada quando ocorrem (por exemplo, fazer um pedido). Eles mantêm as mensagens de acompanhamento relevantes depois que o usuário conclui seu objetivo. Consulte <a href=\"https://www.braze.com/docs/user_guide/messaging/canvas/create_a_canvas/exit_criteria/\">Critérios de saída</a> para saber como as saídas são avaliadas e cronometradas."
  - name: External ID
    description: "O <code>external_id</code> é o identificador principal de usuário em um perfil de usuário da Braze. Ele vincula a mesma pessoa entre canais e dispositivos quando você atribui IDs dos seus próprios sistemas. Perfis anônimos podem não ter um <code>external_id</code> até que você identifique o usuário. Para saber mais, consulte <a href=\"https://www.braze.com/docs/user_guide/get_started/users_and_segments/\">Usuários e segmentos</a> e <a href=\"https://www.braze.com/docs/api/basics/#user-ids\">IDs de usuário</a>."
  - name: Frequency capping
    description: "<a href=\"https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/frequency_capping/\">O limite de frequência</a> permite que você gerencie a comunicação sem sobrecarregar seu público. Trata-se de um limite automatizado de mensagens para evitar que os usuários recebam muitas comunicações em um curto período de tempo."
  - name: HIPAA
    description: "HIPAA é um acrônimo para Health Insurance Portability and Accountability Act (Lei de Portabilidade e Responsabilidade do Seguro de Saúde). A Braze está <a href=\"https://www.braze.com/docs/developer_guide/disclosures/security_qualifications/#hipaa\">em conformidade com a HIPAA</a>. Os requisitos da HIPAA envolvem segurança administrativa, física e técnica."
  - name: In-app message
    description: "<a href=\"https://www.braze.com/docs/user_guide/channels/in_app_messages\">In-App Messages</a> são mensagens móveis que aparecem dentro do seu aplicativo. Elas ajudam a levar o conteúdo ao usuário sem interromper o dia dele com uma notificação por push. Mensagens no app personalizadas e sob medida aprimoram a experiência do usuário e ajudam o público a obter o máximo valor do seu app."
  - name: Inactive users
    description: "Um usuário é considerado <a href=\"https://www.braze.com/docs/user_archival/#inactive-users\">inativo</a> quando não pode ser alcançado nos principais canais de envio de mensagens (por exemplo, e-mail, SMS, push, WhatsApp e LINE conforme sua configuração), não usou nenhum app ou site no espaço de trabalho há mais de seis meses, não recebeu nenhuma mensagem do espaço de trabalho há mais de seis meses e não foi atualizado há mais de seis meses. Usuários inativos são candidatos ao arquivamento junto com os usuários dormentes. Por padrão, a Braze usa uma janela de seis meses para arquivamento de inativos; as configurações da sua empresa podem substituir o número de dias."
  - name: IP warming
    description: "O <a href=\"https://www.braze.com/docs/user_guide/channels/email/email_setup/ip_warming\">aquecimento de IP</a> é a prática de aumentar gradualmente a quantidade de e-mails enviados de um IP dedicado. Isso ajuda a estabelecer uma reputação com os provedores de serviço de Internet, minimizando a probabilidade de suas mensagens serem sinalizadas."
  - name: Key-value pairs
    description: "<a href=\"https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs\">Pares de chave-valor</a> são itens de dados vinculados em que a chave é um identificador exclusivo e o valor é o conteúdo. Eles podem ser usados para enviar cargas úteis de dados extras para dispositivos de usuários."
  - name: Liquid
    description: "Liquid é uma linguagem de modelo comumente usada e voltada para o cliente, criada pela Shopify e escrita em Ruby. <a href=\"https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid\">Liquid</a> é usada para carregar e extrair conteúdo dinâmico. Liquid permite que você use objetos, tags e filtros para <a href=\"https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags\">adicionar personalização</a>."
  - name: Messaging channel
    description: "<a href=\"https://www.braze.com/docs/user_guide/channels/\">Canais de envio de mensagens</a> são formas de se comunicar virtualmente com seus clientes — por meio de notificações por push no telefone ou no navegador da Web, e-mail, mensagens no app e muito mais!"
  - name: Monthly active user (MAU)
    description: Esses são os usuários que tiveram uma sessão nos últimos 30 dias.
  - name: Multichannel messaging
    description: "Envio de mensagens a um usuário por vários meios, como uma combinação de e-mail, push para a web e notificações por push para celular. <a href=\"https://www.braze.com/docs/developer_guide/getting_started/platform_overview/#multichannel-messaging\">Os canais de envio de mensagens</a> são mais bem utilizados em conjunto e com regularidade para reengajar usuários perdidos, reter usuários ativos e energizar os embaixadores da sua marca."
  - name: Multivariate testing
    description: "<a href=\"https://www.braze.com/docs/user_guide/messaging/ab_testing\">Testes A/B</a> comparam um conjunto menor de versões de mensagens; <a href=\"https://www.braze.com/docs/user_guide/messaging/ab_testing/create_tests/\">testes multivariantes</a> comparam múltiplas variáveis ao mesmo tempo para ver qual combinação tem o melhor desempenho. Você pode configurar ambos no dashboard para os tipos de Campaign compatíveis."
  - name: New user
    description: "A Braze considera um novo usuário como qualquer pessoa que tenha instalado seu app recentemente. Alternativamente, um novo usuário também pode ser definido como um usuário com um ID de usuário que não tenha sido identificado anteriormente na Braze."
  - name: Personalization
    description: "Usar a tecnologia para levar em conta as preferências e tendências individuais de cada usuário ao se comunicar com ele. <a href=\"https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize\">O envio de mensagens personalizadas</a> ajuda a criar experiências valiosas para os clientes, adaptando-se às suas preferências."
  - name: Push message
    description: "Uma <a href=\"https://www.braze.com/docs/user_guide/channels/push\">mensagem push</a>, ou notificação por push, é uma notificação que aparece em um aplicativo móvel. As notificações por push geralmente aparecem como caixas de diálogo pop-up e banners para iOS e Android."
  - name: Push token
    description: "Um token por push é uma chave exclusiva, criada e atribuída pela Apple ou pelo Google para criar uma conexão entre um app e um dispositivo iOS, Android ou web. <a href=\"https://www.braze.com/docs/api/objects_filters/user_attributes_object/#migrating-push-tokens\">A migração de token por push</a> é a importação dessas chaves já geradas para a Braze."
  - name: Push time to live (TTL)
    description: "Também conhecido como <a href=\"https://www.braze.com/docs/user_guide/administer/global/workspace_settings/push_settings\">Push TTL</a>, o tempo de vida refere-se ao período em que as Campaigns continuarão a tentar ser entregues a um usuário off-line."
  - name: Race condition
    description: "Uma <a href=\"https://www.braze.com/docs/user_guide/messaging/ab_testing/concepts/race_conditions\">condição de corrida</a> é um conceito de engenharia de software que descreve uma situação indesejável que ocorre quando um sistema tenta realizar várias operações simultaneamente, mas, devido à natureza do sistema, as operações devem ser feitas na sequência correta para serem realizadas corretamente. <br><br>Na plataforma Braze, a segmentação de uma Campaign disparada com base nos dados de usuários registrados no momento do evento pode causar uma condição de corrida. Isso acontece quando uma alteração no atributo do usuário no qual a Campaign é segmentada ainda não foi processada para o usuário no momento em que a associação ao Segment é determinada e a Campaign é enviada, o que pode fazer com que o usuário não receba a Campaign."
  - name: Rate limiting
    description: "<a href=\"https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/frequency_capping/\">Limite de taxa</a> controla a velocidade com que as mensagens saem da Braze (por exemplo, velocidade de entrega por minuto ou limites centrados no usuário usando filtros de Segment). Funciona em conjunto com o limite de frequência na mesma página, que limita quantas mensagens um usuário recebe em uma janela de tempo."
  - name: Segmentation
    description: "A <a href=\"https://www.braze.com/docs/user_guide/audience/segments\">segmentação</a> do dashboard permite criar grupos ou extensões de usuários com base em filtros poderosos de seu comportamento no app, dados demográficos e muito mais."
  - name: Software development kit (SDK)
    description: "<a href=\"https://www.braze.com/docs/developer_guide/getting_started/sdk_overview/\">SDKs</a> são integrados aos seus apps móveis, sites e experiências conectadas e fornecem ferramentas de marketing, envio de mensagens e análise de dados. A Braze publica guias de integração de SDK para plataformas como <a href=\"https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=swift\">Swift</a> e <a href=\"https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=android\">Android</a>; para Web e outras plataformas, siga os caminhos de integração vinculados na visão geral do SDK."
  - name: Subscription groups
    description: "<a href=\"https://www.braze.com/docs/user_guide/channels/email/subscriptions/#subscription-groups\">Grupos de inscrições</a> se sobrepõem aos estados de inscrição globais para que você possa oferecer opções granulares de opt-in (por exemplo, newsletters versus promoções). Padrões semelhantes existem para canais como SMS e WhatsApp; sempre direcione um grupo de inscrições quando seu canal exigir."
  - name: Sunsetting
    description: "O sunsetting refere-se ao processo de identificação de usuários não engajados e de cessação do envio ativo de mensagens a esses usuários sem que eles tenham que tomar qualquer atitude. A criação de políticas de sunsetting para suas mensagens de <a href=\"https://www.braze.com/docs/user_guide/channels/email/best_practices/sunset_policies/\">e-mail</a> e <a href=\"https://www.braze.com/docs/user_guide/channels/push/best_practices/#implement-a-sunset-policy-for-unresponsive-users\">push</a> pode ajudar a reduzir os impactos nas taxas de abertura."
  - name: Tag
    description: "<a href=\"https://www.braze.com/docs/user_guide/administer/global/workspace_settings/tags\">Tags</a> são uma ferramenta que ajuda a categorizar, organizar e classificar seu engajamento em uma ou várias Campaigns."
  - name: User alias
    description: "<a href=\"https://www.braze.com/docs/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users#assigning-user-aliases\">Aliases de usuário</a> são identificadores alternativos que você pode atribuir a perfis anônimos antes de existir um <code>external_id</code>, para que você possa referenciar a mesma pessoa entre dispositivos ou canais até que ela faça login."
  - name: User archival
    description: "<a href=\"https://www.braze.com/docs/user_archival/\">O arquivamento de usuários</a> refere-se a usuários que foram arquivados. Na Braze, isso inclui tanto usuários inativos quanto usuários dormentes. O arquivamento avalia as regras de inatividade e dormência nos serviços da Braze (consulte Arquivamento de usuários para agendamento, elegibilidade do espaço de trabalho, como limites de contagem de usuários, e como personalizar janelas com configurações da empresa ou Canvas)."
  - name: User profile
    description: "Um <a href=\"https://www.braze.com/docs/user_guide/audience/manage_audience/user_profiles/\">perfil de usuário</a> é o registro central de cada pessoa na Braze, incluindo identificadores, atributos, eventos, compras, dispositivos, histórico de engajamento e histórico de mensagens. Os perfis alimentam fluxos de trabalho de segmentação, personalização e conformidade entre canais."
  - name: Webhook
    description: "<a href=\"https://www.braze.com/docs/user_guide/channels/webhooks\">Webhooks</a> permitem disparar ações que não são do app, como a entrega de mensagens de texto SMS. Você pode usar webhooks para fornecer informações em tempo real a outros sistemas e aplicativos. A flexibilidade desse recurso permite que você envie informações para qualquer endpoint."
  - name: Workspace
    description: "Um <a href=\"https://www.braze.com/docs/user_guide/get_started/workspaces/\">espaço de trabalho</a> é o contêiner onde a Braze armazena dados e onde sua equipe cria Campaigns, Canvas e Segments. Cada espaço de trabalho contém uma ou mais <a href=\"https://www.braze.com/docs/user_guide/get_started/workspaces/#understanding-workspaces\">instâncias do app</a> (os apps e sites individuais que enviam dados para esse espaço de trabalho)."

---