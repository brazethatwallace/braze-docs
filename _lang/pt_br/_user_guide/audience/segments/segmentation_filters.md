---
page_order: 3
nav_title: Filtros de segmentação
article_title: Filtros de segmentação
layout: glossary_page
glossary_top_header: "Filtros de segmentação"
glossary_top_text: "O SDK da Braze oferece um poderoso arsenal de filtros para segmentar e direcionar seus usuários com base em recursos e atributos específicos. Você pode pesquisar ou refinar esses filtros por categoria.<br><br>Para saber mais sobre os diferentes tipos de dados de atributos personalizados que você pode usar para segmentar usuários, consulte <a href=\"/docs/user_guide/data/activation/attributes/custom_attributes#custom-attribute-data-types\">Tipos de dados de atributos personalizados</a>. Observe que os filtros de intervalo são limitados a 100 anos."

page_type: glossary
tool: Segments
description: "Este glossário lista os filtros disponíveis para segmentar e direcionar seus usuários."
search_rank: 2
glossary_tag_name: Categoria do filtro
glossary_filter_text: "Selecione uma categoria para refinar o glossário:"

glossary_tags:
  - name: Segment or CSV membership
  - name: Custom attribute
  - name: Custom events
  - name: Sessions
  - name: Retargeting
  - name: Channel subscription behavior
  - name: Purchase behavior
  - name: eCommerce
  - name: Demographic attributes
  - name: App
  - name: Uninstall
  - name: Devices
  - name: Location
  - name: Cohort membership
  - name: Install attribution
  - name: Intelligence and predictive
  - name: Social activity
  - name: Other Filters
  - name: Advertising use cases
  - name: User Attributes

glossaries:
  - name: Segment Membership
    description: Permite filtrar com base na associação a segmentos em qualquer lugar onde filtros são usados (como segmentos, Campaigns e outros) e direcionar vários segmentos diferentes dentro de uma única Campaign. <br><br>Para capturar a associação a um segmento em um momento específico, exporte os usuários do segmento no dashboard ou chame o <a href="/docs/api/endpoints/export/user_data/post_users_segment/"><code>/users/export/segment</code> endpoint</a> antes de enviar uma Campaign ou Canvas. A Braze não armazena o histórico de segmentação por usuário, então você não pode verificar retroativamente se um usuário estava em um segmento em um momento passado. Para saber mais, consulte <a href="/docs/user_guide/data/distribution/export_braze_data/segment_data_to_csv/">Exportar dados de segmento para CSV</a>.<br><br>Observe que segmentos que já usam esse filtro não podem ser incluídos ou aninhados em outros segmentos, pois isso pode criar um ciclo em que o Segment A inclui o Segment B, que então tenta incluir o Segment A novamente. Se isso acontecesse, o segmento ficaria referenciando a si mesmo, tornando impossível calcular quem realmente pertence a ele. Além disso, aninhar segmentos dessa forma adiciona complexidade e pode deixar as coisas mais lentas. Em vez disso, recrie o segmento que você está tentando incluir usando os mesmos filtros.<br><br>Se um segmento não aparecer no menu suspenso do filtro **Segment Membership**, recrie-o com os mesmos filtros e selecione o novo segmento, ou confirme que ele não depende desse público de uma forma que criaria um ciclo.
    tags:
      - Segment or CSV membership
  - name: Braze Segment Extensions
    description: Depois de criar uma extensão de segmento no dashboard da Braze, você pode optar por incluir/excluir essas extensões no seu segmento.
    tags:
      - Segment or CSV membership
  - name: Updated/Imported from CSV
    description: Segmenta seus usuários com base em se eles fizeram parte de um upload de CSV ou não.
    tags:
      - Segment or CSV membership
  - name: Custom Attributes
    description: Determina se um usuário corresponde ou não a um valor de atributo personalizado registrado. <br><br>Fuso horário:<br>Fuso horário da empresa
    tags:
      - Custom attribute
  - name: Created At
    description: Segmenta os usuários por quando o perfil de usuário foi criado. Se um usuário foi adicionado por CSV ou API, esse filtro reflete a data em que foi adicionado. Se o usuário não foi adicionado por CSV ou API e teve sua primeira sessão rastreada pelo SDK, esse filtro reflete a data dessa primeira sessão.
    tags:
      - Other Filters
  - name: Created From
    description: "Segmenta os usuários por onde o perfil de usuário foi criado.<br><br>Os seguintes valores são suportados:<br>- SDK (<code>sdk</code>): Perfil de usuário criado pelo SDK da Braze.<br>- REST API (<code>rest</code>): Perfil de usuário criado pela REST API da Braze.<br>- Push Token Import (<code>pti</code>): Perfil de usuário criado por importação de token por push.<br>- CSV (<code>csv</code>): Perfil de usuário criado por importação de CSV.<br>- Demo (<code>demo</code>): Perfil de usuário criado por dados de demonstração.<br>- SMS (<code>sms</code>): Perfil de usuário criado por SMS.<br>- Shopify (<code>shopify</code>): Perfil de usuário criado pelo Shopify.<br>- WhatsApp (<code>whats_app</code>): Perfil de usuário criado pelo WhatsApp.<br>- Provider Event (<code>provider_event</code>): Perfil de usuário criado por um evento de provedor.<br>- Provider Sync (<code>provider_sync</code>): Perfil de usuário criado por uma sincronização de provedor.<br>- Landing Page (<code>landing_page</code>): Perfil de usuário criado por uma landing page."
    tags:
      - Other Filters
  - name: Nested Custom Attributes
    description: Atributos que são propriedades de atributos personalizados.<br><br>Ao filtrar um atributo personalizado aninhado do tipo data/hora, você pode optar por filtrar com base em "Dia do ano" ou "Hora". "Dia do ano" verifica apenas o mês e o dia para comparação. "Hora" compara o timestamp completo, incluindo o ano.
    tags:
      - Custom attribute
  - name: Day of Recurring Event
    description: Este filtro verifica o mês e o dia de um atributo personalizado com o tipo de dados "date", mas não verifica o ano. Esse filtro é útil para eventos anuais.<br><br>Fuso horário&#58;<br>Este filtro se ajusta ao fuso horário do usuário, desde que a mensagem seja enviada usando a opção de agendamento por horário local; caso contrário, usa o fuso horário da empresa.
    tags:
      - Custom attribute
  - name: Custom Event
    description: Determina se um usuário realizou ou não um evento especialmente registrado.<br><br> Exemplo:<br>Atividade concluída com a propriedade activity_name.<br><br>Fuso horário:<br>UTC - Dia corrido = 1 dia corrido considera 24-48 horas do histórico do usuário
    tags:
      - Custom events
  - name: First Did Custom Event
    description: Determina a primeira vez que um usuário realizou um evento especialmente registrado. (período de 24 horas) <br><br>Exemplo:<br> Primeiro carrinho abandonado há menos de 1 dia<br><br>Fuso horário:<br>Fuso horário da empresa
    tags:
      - Custom events
  - name: Last Did Custom Event
    description: Determina a última vez que um usuário realizou um evento especialmente registrado. Este filtro suporta decimais, como 0,25 horas. (período de 24 horas) <br><br>Exemplo:<br> Último carrinho abandonado há menos de 1 dia<br><br>Fuso horário:<br>Fuso horário da empresa
    tags:
      - Custom events
  - name: X Custom Event In Y Days
    description: Determina se um usuário realizou ou não um evento especialmente registrado entre 0 e 50 vezes no último número especificado de dias corridos entre 1 e 30. (Dia corrido = 1 dia corrido considera 24-48 horas do histórico do usuário)<br> <a href="/docs/x-in-y-behavior"> Saiba mais sobre o comportamento X em Y aqui.</a> <br><br>Exemplo:<br>Carrinho abandonado exatamente 0 vezes no último 1 dia corrido<br><br>Fuso horário:<br>UTC - Para considerar todos os fusos horários, 1 dia corrido considera 24-48 horas do histórico do usuário, dependendo do momento em que o segmento é avaliado; para 2 dias corridos, considera 48-72 horas do histórico do usuário, e assim por diante.
    tags:
      - Custom events
  - name: X Custom Event Property In Y Days
    description: Determina se um usuário realizou ou não um evento especialmente registrado em relação a uma propriedade específica entre 0 e 50 vezes no último número especificado de dias corridos entre 1 e 30. (Dia corrido = 1 dia corrido considera 24-48 horas do histórico do usuário)<br><a href="/docs/x-in-y-behavior">Saiba mais sobre o comportamento X em Y aqui.</a> <br><br>Exemplo:<br> Adicionado aos favoritos com a propriedade "event_name" exatamente 0 vezes no último 1 dia corrido<br><br>Fuso horário:<br>UTC - Para considerar todos os fusos horários, 1 dia corrido considera 24-48 horas do histórico do usuário, dependendo do momento em que o segmento é avaliado; para 2 dias corridos, considera 48-72 horas do histórico do usuário, e assim por diante.
    tags:
      - Custom events
  - name: Email Address
    description: Permite designar os destinatários da sua Campaign por endereços de e-mail individuais para testes. Também pode ser usado para enviar e-mails de transação a todos os seus usuários (incluindo os que cancelaram a inscrição) usando o especificador "Email Address is not Blank" dentro do filtro, para que você possa maximizar a entrega de e-mails independentemente do status de opt-in. <br><br>Este filtro verifica apenas se os perfis de usuário possuem um endereço de e-mail, enquanto o filtro <a href="/docs/user_guide/audience/segments/segmentation_filters#email-available">E-mail disponível</a> verifica critérios adicionais.
    tags:
      - Other Filters
  - name: External User ID
    description: Permite designar os destinatários da sua Campaign por IDs de usuário individuais para testes.
    tags:
      - Other Filters
  - name: "Random Bucket #"
    description: Segmenta seus usuários por um número atribuído aleatoriamente (de 0 a 9999, inclusive). Pode permitir a criação de segmentos uniformemente distribuídos de usuários verdadeiramente aleatórios para testes A/B e multivariantes.
    tags:
      - Other Filters
  - name: Session Count
    description: Segmenta seus usuários pelo número de sessões que tiveram em qualquer um dos seus apps dentro do seu espaço de trabalho.
    tags:
      - Sessions
  - name: Session Count For App
    description: Segmenta seus usuários pelo número de sessões que tiveram em um app específico designado.
    tags:
      - Sessions
  - name: X Sessions In Last Y Days
    description: Segmenta seus usuários pelo número de sessões (entre 0 e 50) que tiveram no seu app no último número especificado de dias corridos entre 1 e 30. <br> <a href="/docs/x-in-y-behavior">Saiba mais sobre o comportamento X em Y aqui.</a>
    tags:
      - Sessions
  - name: First Used App
    description: Segmenta seus usuários pela primeira vez registrada em que abriram seu app. <em>Isso captura a primeira sessão usando uma versão do seu app com o SDK da Braze integrado.</em> (período de 24 horas)<br><br>Fuso horário:<br>Fuso horário da empresa
    tags:
      - Sessions
  - name: First Used Specific App
    description: Segmenta seus usuários pela primeira vez registrada em que abriram qualquer um dos seus apps dentro do seu espaço de trabalho. (período de 24 horas)<br><br>Fuso horário:<br>Fuso horário da empresa
    tags:
      - Sessions
  - name: Last Used App
    description: Segmenta seus usuários pela última vez que abriram seu app. (período de 24 horas)<br><br>Fuso horário:<br>Fuso horário da empresa
    tags:
      - Sessions
  - name: Last Used Specific App
    description: Segmenta seus usuários pela última vez que abriram um app específico designado. (período de 24 horas)<br><br>Fuso horário:<br>Fuso horário da empresa
    tags:
      - Sessions
  - name: Median Session Duration
    description: Segmenta seus usuários pela duração mediana de suas sessões no seu app.
    tags:
      - Sessions
  - name: Received Message from Campaign
    description: Segmenta seus usuários por terem recebido ou não uma Campaign específica. <br><br>Para Content Cards, Banners e mensagens no app, isso ocorre quando um usuário registra uma impressão, não quando o cartão ou a mensagem no app é enviada.<br><br> Para push e webhooks, isso ocorre quando a mensagem é enviada ao usuário.<br><br> Para WhatsApp, isso ocorre quando a última solicitação de API de mensagem é enviada ao WhatsApp, não quando a mensagem é entregue ao dispositivo do usuário.<br><br> Para e-mails, o perfil de usuário direcionado corresponde a esse filtro quando uma solicitação de e-mail é enviada ao provedor de serviços de e-mail (independentemente de ser realmente entregue).<br><br> Para SMS e RCS, os usuários são considerados como tendo "recebido" uma mensagem no momento do envio. Mesmo que a mensagem não chegue ao dispositivo do usuário, o usuário ainda corresponde a esse filtro.<br><br> Quando uma mensagem é entregue, aberta ou clicada, a Braze atualiza os dados de todos os perfis que compartilham o mesmo identificador de canal (por exemplo, e-mail ou número de telefone), então usuários que compartilham um identificador com alguém que recebeu a mensagem podem corresponder a esse filtro mesmo que seu perfil não tenha recebido diretamente a Campaign.
    tags:
      - Retargeting
  - name: Received Campaign Variant
    description: Segmenta seus usuários por qual variante de uma Campaign multivariante eles receberam.<br><br>Este filtro se aplica a Campaigns multivariantes e Campaigns de push rápido multivariantes. Campaigns de API, Campaigns multicanal padrão e Campaigns de experimento de Feature Flag não aparecem no seletor de Campaign. Campaigns somente de webhook não aparecem no seletor de Campaign.<br><br>Para Content Cards, Banners e mensagens no app, isso ocorre quando um usuário registra uma impressão, não quando o cartão ou a mensagem no app é enviada.<br><br> Para push e webhooks, isso ocorre quando a mensagem é enviada ao usuário.<br><br> Para WhatsApp, isso ocorre quando a última solicitação de API de mensagem é enviada ao WhatsApp, não quando a mensagem é entregue ao dispositivo do usuário.<br><br> Para e-mails, o perfil de usuário direcionado corresponde a esse filtro quando uma solicitação de e-mail é enviada ao provedor de serviços de e-mail (independentemente de ser realmente entregue).<br><br> Para SMS e RCS, os usuários são considerados como tendo "recebido" uma mensagem no momento do envio. Mesmo que a mensagem não chegue ao dispositivo do usuário, o usuário ainda corresponde a esse filtro.<br><br> Quando uma mensagem é entregue, aberta ou clicada, a Braze atualiza os dados de todos os perfis que compartilham o mesmo identificador de canal (por exemplo, e-mail ou número de telefone), então usuários que compartilham um identificador com alguém que recebeu a mensagem podem corresponder a esse filtro mesmo que seu perfil não tenha recebido diretamente a Campaign.
    tags:
      - Retargeting
  - name: Received Message from Canvas Step
    description: Segmenta seus usuários por terem recebido ou não um componente específico do Canvas.<br><br>Para Content Cards e mensagens no app, isso ocorre quando um usuário registra uma impressão, não quando o cartão ou a mensagem no app é enviada.<br><br> Para push e webhooks, isso ocorre quando a mensagem é enviada ao usuário.<br><br> Para WhatsApp, isso ocorre quando a última solicitação de API de mensagem é enviada ao WhatsApp, não quando a mensagem é entregue ao dispositivo do usuário.<br><br> Para e-mails, o perfil de usuário direcionado corresponde a esse filtro quando uma solicitação de e-mail é enviada ao provedor de serviços de e-mail (independentemente de ser realmente entregue).<br><br> Para SMS e RCS, os usuários são considerados como tendo "recebido" uma mensagem no momento do envio. Mesmo que a mensagem não chegue ao dispositivo do usuário, o usuário ainda corresponde a esse filtro.<br><br> Quando uma mensagem é entregue, aberta ou clicada, a Braze atualiza os dados de todos os perfis que compartilham o mesmo identificador de canal (por exemplo, e-mail ou número de telefone), então usuários que compartilham um identificador com alguém que recebeu a mensagem podem corresponder a esse filtro mesmo que seu perfil não tenha recebido diretamente a Campaign.
    tags:
      - Retargeting
  - name: Last Received Message from Specific Canvas Step
    description: Segmenta seus usuários por quando receberam um componente específico do Canvas.<br><br> Como os dados são atualizados para todos os perfis que compartilham o mesmo identificador de canal (por exemplo, e-mail ou telefone) quando ocorre uma entrega, abertura ou clique, um usuário que compartilha um identificador com alguém que recebeu uma mensagem pode não corresponder a esse filtro mesmo que nunca tenha recebido a mensagem explicitamente. Use "Entered Canvas Variation" para isolar perfis de usuário de duplicatas.<br><br> Este filtro não considera quando os usuários receberam outros componentes do Canvas.
    tags:
      - Retargeting
  - name: Last Received Message from Specific Campaign
    description: Segmenta seus usuários por quando receberam uma Campaign específica.<br><br> Como os dados são atualizados para todos os perfis que compartilham o mesmo identificador de canal (por exemplo, e-mail ou telefone) quando ocorre uma entrega, abertura ou clique, um usuário que compartilha um identificador com alguém que recebeu uma mensagem pode não corresponder a esse filtro mesmo que nunca tenha recebido a mensagem explicitamente.<br><br> Este filtro não considera quando os usuários receberam outras Campaigns.
    tags:
      - Retargeting
  - name: Received Message from Campaign or Canvas with Tag
    description: Segmenta seus usuários por terem recebido ou não uma Campaign ou Canvas específico com uma tag específica.<br><br>A Braze avalia apenas as últimas 200 Campaigns e Canvas enviados que usam a tag selecionada quando esse filtro é executado.<br><br> Para Content Cards, Banners (somente Campaigns) e mensagens no app, isso ocorre quando um usuário registra uma impressão, não quando o cartão ou a mensagem no app é enviada.<br><br> Para push e webhooks, isso ocorre quando a mensagem é enviada ao usuário.<br><br> Para WhatsApp, isso ocorre quando a última solicitação de API de mensagem é enviada ao WhatsApp, não quando a mensagem é entregue ao dispositivo do usuário.<br><br> Para e-mails, o perfil de usuário direcionado corresponde a esse filtro quando uma solicitação de e-mail é enviada ao provedor de serviços de e-mail (independentemente de ser realmente entregue).<br><br> Para SMS e RCS, os usuários são considerados como tendo "recebido" uma mensagem no momento do envio. Mesmo que a mensagem não chegue ao dispositivo do usuário, o usuário ainda corresponde a esse filtro.<br><br> Quando uma mensagem é entregue, aberta ou clicada, a Braze atualiza os dados de todos os perfis que compartilham o mesmo identificador de canal (por exemplo, e-mail ou número de telefone), então usuários que compartilham um identificador com alguém que recebeu a mensagem podem corresponder a esse filtro mesmo que seu perfil não tenha recebido diretamente a Campaign.
    tags:
      - Retargeting
  - name: Last Received Message from Campaign or Canvas With Tag
    description: Segmenta seus usuários por quando receberam uma Campaign ou Canvas específico com uma tag específica. Este filtro não considera quando os usuários receberam outras Campaigns ou Canvas. (período de 24 horas)
    tags:
      - Retargeting
  - name: Has Never Received a Message from Campaign or Canvas Step
    description: Segmenta seus usuários por terem recebido ou não qualquer Campaign ou componente do Canvas.
    tags:
      - Retargeting
  - name: Last Received Email
    description: Segmenta seus usuários pela última vez que receberam um dos seus e-mails. (período de 24 horas)<br><br>Fuso horário:<br>Fuso horário da empresa
    tags:
      - Retargeting
  - name: Last Received Push
    description: Segmenta seus usuários pela última vez que receberam uma das suas notificações por push. (período de 24 horas)<br><br>Fuso horário:<br>Fuso horário da empresa
    tags:
      - Retargeting
  - name: Last In App Message Impression
    description: Segmenta seus usuários pela última vez que visualizaram uma mensagem no app.
    tags:
      - Retargeting
  - name: Last Received SMS
    description: Segmenta seus usuários pelo momento em que a última mensagem SMS, MMS ou RCS foi entregue ao provedor de SMS ou RCS. Isso não garante que a mensagem foi entregue ao dispositivo do usuário. (período de 24 horas)<br><br>Fuso horário:<br>Fuso horário da empresa
    tags:
      - Retargeting
  - name: Last Received Webhook
    description: Segmenta seus usuários pela última vez que a Braze enviou um webhook para esse usuário. (período de 24 horas)<br><br>Fuso horário:<br>Fuso horário da empresa
    tags:
      - Retargeting
  - name: Last Received WhatsApp
    description: Segmenta seus usuários pela última vez que receberam uma mensagem do WhatsApp. Isso ocorre quando a última solicitação de API de mensagem é enviada ao WhatsApp, não quando a mensagem é entregue ao dispositivo do usuário. (período de 24 horas)<br><br>Fuso horário:<br>Fuso horário da empresa
    tags:
      - Retargeting
  - name: Live Activities Push to Start Registered for App
    description: Segmenta seus usuários por estarem registrados para iniciar uma Live Activity por meio de notificações por push do iOS para um app específico.
    tags:
      - Devices
  - name: Clicked/Opened Campaign
    description: Filtra por interação com uma Campaign específica. Para mensagens no app, cliques em mensagens no app incluem cliques no corpo e nos botões. Não conta ações de dispensar ou fechar a mensagem com o X.<br><br>Para e-mails, o evento de abertura inclui tanto aberturas por máquina quanto aberturas não realizadas por máquina. Este filtro também inclui a opção de filtrar por "opened any email (machine opens)" e "opened any email (other opens)". Cliques em links de cancelamento de inscrição e centrais de preferências não contam para esse filtro. Se vários usuários compartilham o mesmo endereço de e-mail:<br>- Quando o e-mail é aberto ou clicado, todos os outros usuários com o mesmo endereço de e-mail também têm seus perfis atualizados. <br>- Se o usuário original alterar seu endereço de e-mail após o envio da mensagem e antes da abertura ou clique, a abertura ou clique é aplicado a todos os usuários restantes com aquele endereço de e-mail em vez do usuário original.<br><br>Para SMS e RCS, uma interação é definida como:<br>- O usuário enviou por último uma resposta de SMS ou RCS correspondendo a uma determinada categoria de palavra-chave. Isso é atribuído à Campaign mais recente recebida por todos os usuários com esse número de telefone. A Campaign deve ter sido recebida nas últimas quatro horas.<br>- O usuário selecionou por último qualquer link encurtado em uma mensagem SMS ou RCS que tem o rastreamento de cliques do usuário ativado, de uma determinada Campaign.
    tags:
      - Retargeting
  - name: Clicked/Opened Campaign or Canvas With Tag
    description: Filtra por interação com uma Campaign específica que possui uma tag específica. Para mensagens no app, cliques em mensagens no app incluem cliques no corpo e nos botões. Não conta ações de dispensar ou fechar a mensagem com o X.<br><br>Para e-mails, o evento de abertura inclui tanto aberturas por máquina quanto aberturas não realizadas por máquina. Este filtro também inclui a opção de filtrar por "opened any email (machine opens)" e "opened any email (other opens)". Se vários usuários compartilham o mesmo endereço de e-mail:<br>- Quando o e-mail é aberto ou clicado, todos os outros usuários com o mesmo endereço de e-mail também têm seus perfis atualizados. <br>- Se o usuário original alterar seu endereço de e-mail após o envio da mensagem e antes da abertura ou clique, a abertura ou clique é aplicado a todos os usuários restantes com aquele endereço de e-mail em vez do usuário original.<br><br>Para SMS e RCS, uma interação é definida como:<br>- O usuário enviou por último uma resposta de SMS ou RCS correspondendo a uma determinada categoria de palavra-chave. Isso é atribuído à Campaign mais recente recebida por todos os usuários com esse número de telefone. A Campaign deve ter sido recebida nas últimas quatro horas.<br>- Quando o usuário selecionou por último qualquer link encurtado em uma mensagem SMS ou RCS que tem o rastreamento de cliques do usuário ativado, de uma determinada Campaign ou etapa do Canvas com tag.
    tags:
      - Retargeting
  - name: Clicked/Opened Step
    description: Filtra por interação com um componente específico do Canvas. Para mensagens no app, cliques em mensagens no app também contam cliques no corpo e nos botões. Não conta ações de dispensar ou fechar a mensagem com o X.<br><br>Para e-mails, o evento de abertura inclui tanto aberturas por máquina quanto aberturas não realizadas por máquina. Este filtro também inclui a opção de filtrar por "opened any email (machine opens)" e "opened any email (other opens)".<br><br>Para SMS e RCS, uma interação é definida como:<br>- O usuário enviou por último uma resposta de SMS ou RCS correspondendo a uma determinada categoria de palavra-chave. Isso é atribuído à Campaign mais recente recebida por todos os usuários com esse número de telefone. A Campaign deve ter sido recebida nas últimas quatro horas. <br>- O usuário selecionou por último qualquer link encurtado em uma mensagem SMS ou RCS que tem o rastreamento de cliques do usuário ativado, de uma determinada etapa do Canvas.
    tags:
      - Retargeting
  - name: Clicked Alias in Campaign
    description: Filtra seus usuários por terem clicado ou não em um alias específico em uma Campaign específica. Isso se aplica apenas a mensagens de e-mail. <br><br> Se vários usuários compartilham o mesmo endereço de e-mail:<br>- Quando o e-mail é aberto ou clicado, todos os outros usuários com o mesmo endereço de e-mail também têm seus perfis atualizados. <br>- Se o usuário original alterar seu endereço de e-mail após o envio da mensagem e antes da abertura ou clique, a abertura ou clique é aplicado a todos os usuários restantes com aquele endereço de e-mail em vez do usuário original.
    tags:
      - Retargeting
  - name: Clicked Alias in Canvas Step
    description: Filtra seus usuários por terem clicado ou não em um alias específico em um Canvas específico. Isso se aplica apenas a mensagens de e-mail. <br><br> Se vários usuários compartilham o mesmo endereço de e-mail:<br>- Quando o e-mail é aberto ou clicado, todos os outros usuários com o mesmo endereço de e-mail também têm seus perfis atualizados. <br>- Se o usuário original alterar seu endereço de e-mail após o envio da mensagem e antes da abertura ou clique, a abertura ou clique é aplicado a todos os usuários restantes com aquele endereço de e-mail em vez do usuário original.
    tags:
      - Retargeting
  - name: Clicked Alias in Any Campaign or Canvas Step
    description: Filtra seus usuários por terem clicado ou não em um alias específico em qualquer Campaign ou Canvas. Isso se aplica apenas a mensagens de e-mail. <br><br> Se vários usuários compartilham o mesmo endereço de e-mail:<br>- Quando o e-mail é aberto ou clicado, todos os outros usuários com o mesmo endereço de e-mail também têm seus perfis atualizados. <br>- Se o usuário original alterar seu endereço de e-mail após o envio da mensagem e antes da abertura ou clique, a abertura ou clique é aplicado a todos os usuários restantes com aquele endereço de e-mail em vez do usuário original.
    tags:
      - Retargeting
  - name: Hard Bounced
    description: Segmenta seus usuários por se o endereço de e-mail deles sofreu hard bounce (como quando o endereço de e-mail é inválido). Para exportar usuários com e-mails inválidos, chame o <a href="/docs/api/endpoints/email/get_list_hard_bounces/"><code>/email/hard_bounces</code> endpoint</a> ou crie um segmento com filtros como "endereço de e-mail não está em branco", "e-mail não está disponível" e "status de inscrição de e-mail não é cancelado".
    tags:
      - Retargeting
  - name: Soft Bounced
    description: Segmenta seus usuários por terem sofrido soft bounce X vezes em Y dias. Os filtros de segmento só podem consultar os últimos 30 dias, mas você pode consultar períodos anteriores com extensões de segmento.<br><br>Este filtro opera de forma diferente de um evento de soft bounce no Currents. O filtro de segmento de soft bounce conta um soft bounce se não houve entrega bem-sucedida durante o período de tentativas de 72 horas. No Currents, cada tentativa malsucedida é enviada como um evento de soft bounce.
    tags:
      - Retargeting
  - name: Has Marked You As Spam
    description: Segmenta seus usuários por terem marcado suas mensagens como spam.
    tags:
      - Retargeting
  - name: Invalid Phone Number
    description: Segmenta seus usuários por se o número de telefone deles é inválido.
    tags:
      - Retargeting
  - name: Last Sent Specific SMS Inbound Keyword Category
    description: Segmenta seus usuários por quando enviaram por último um SMS, MMS ou RCS para um grupo de inscrições específico dentro de uma categoria de palavra-chave específica.
    tags:
      - Retargeting
  - name: Converted From Campaign
    description: Segmenta seus usuários por terem convertido ou não em uma Campaign específica. Este filtro não inclui usuários que estão no grupo de controle.
    tags:
      - Retargeting
  - name: Converted From Canvas
    description: Segmenta seus usuários por terem convertido ou não em um Canvas específico. Este filtro não inclui usuários que estão no grupo de controle.
    tags:
      - Retargeting
  - name: In Campaign Control Group
    description: Segmenta seus usuários por terem estado no grupo de controle de uma Campaign multivariante específica.
    tags:
      - Retargeting
  - name: In Canvas Control Group
    description: Segmenta seus usuários por terem estado no grupo de controle de um Canvas específico. Este filtro avalia apenas usuários que entraram no Canvas, então usuários que nunca entraram são totalmente excluídos dos resultados.<br><br>Por exemplo, se você filtrar por usuários que não estão no grupo de controle de um Canvas, receberá apenas usuários que entraram no Canvas e foram atribuídos a uma variante que não é de controle — usuários que nunca entraram no Canvas não são incluídos. Para incluir todos os usuários independentemente da entrada no Canvas, use o filtro <code>Entered Canvas Variation</code>.
    tags:
      - Retargeting
  - name: Last Enrolled in Any Control Group
    description: Segmenta seus usuários pela última vez que caíram no grupo de controle de uma Campaign. <br><br>Fuso horário:<br>Fuso horário da empresa
    tags:
      - Retargeting
  - name: Entered Canvas Variation
    description: Segmenta seus usuários por terem entrado ou não em um caminho de variação de um Canvas específico. Este filtro avalia todos os usuários.<br><br>Por exemplo, se você filtrar por usuários que não entraram em um grupo de controle de variação do Canvas, receberá todos os usuários que não estão no grupo de controle, independentemente de terem entrado no Canvas.
    tags:
      - Retargeting
  - name: Last Received Any Message
    description: Segmenta seus usuários determinando a última mensagem que foi recebida. (período de 24 horas)<br><br>Para Content Cards, Banners e mensagens no app, isso ocorre quando um usuário registrou por último uma impressão, não quando o cartão ou a mensagem no app foi enviada por último.<br><br>Para push e webhooks, isso ocorre quando qualquer mensagem foi enviada ao usuário.<br><br> Para WhatsApp, isso ocorre quando a última solicitação de API de mensagem foi enviada ao WhatsApp, não quando a mensagem foi entregue ao dispositivo do usuário.<br><br> Para e-mails, o perfil de usuário direcionado corresponde a esse filtro quando uma solicitação de e-mail é enviada ao provedor de serviços de e-mail (independentemente de ser realmente entregue).<br><br> Para SMS e RCS, os usuários são considerados como tendo "recebido" uma mensagem no momento do envio. Mesmo que a mensagem não chegue ao dispositivo do usuário, o usuário ainda corresponde a esse filtro.<br><br> Quando uma mensagem é entregue, aberta ou clicada, a Braze atualiza os dados de todos os perfis que compartilham o mesmo identificador de canal (por exemplo, e-mail ou número de telefone), então usuários que compartilham um identificador com alguém que recebeu a mensagem podem corresponder a esse filtro mesmo que seu perfil não tenha recebido diretamente a Campaign.<br><br>Exemplo:<br>Última mensagem recebida há menos de 1 dia = menos de 24 horas atrás<br><br>Fuso horário:<br>Fuso horário da empresa
    tags:
      - Retargeting
  - name: Last Engaged With Message
    description: Segmenta seus usuários pela última vez que clicaram ou abriram um dos seus canais de envio de mensagens (Banners, Content Cards, e-mail, mensagem no app, SMS, RCS, push, WhatsApp).<br><br>Para Content Cards, Banners e mensagens no app, isso ocorre quando um usuário registra uma impressão, não quando o cartão ou a mensagem no app é enviada.<br><br> Para push e webhooks, isso ocorre quando a mensagem é enviada ao usuário.<br><br> Para WhatsApp, isso ocorre quando a última solicitação de API de mensagem é enviada ao WhatsApp, não quando a mensagem é entregue ao dispositivo do usuário.<br><br> Para e-mails, o evento de abertura inclui tanto aberturas por máquina quanto aberturas não realizadas por máquina. (período de 24 horas)<br><br>Para e-mails, o perfil de usuário direcionado corresponde a esse filtro quando uma solicitação de e-mail é enviada ao provedor de serviços de e-mail (independentemente de ser realmente entregue). Isso também inclui a opção de filtrar por "opened any email (machine opens)" e "opened any email (other opens)".<br><br> Para SMS e RCS, isso ocorre quando o usuário selecionou por último qualquer link encurtado em uma mensagem que tem o rastreamento de cliques do usuário ativado.<br><br> Quando uma mensagem é entregue, aberta ou clicada, a Braze atualiza os dados de todos os perfis que compartilham o mesmo identificador de canal (por exemplo, e-mail ou número de telefone), então usuários que compartilham um identificador com alguém que recebeu a mensagem podem corresponder a esse filtro mesmo que seu perfil não tenha recebido diretamente a Campaign.<br><br>Fuso horário:<br>Fuso horário da empresa
    tags:
      - Retargeting
  - name: Clicked card
    description: Segmenta seus usuários por terem clicado ou não em um Content Card específico. Este filtro está disponível como subfiltro de "Clicked/Opened Campaign", "Clicked/Opened Campaign or Canvas With Tag" e "Clicked/Opened Step".
    tags:
      - Retargeting
  - name: Feature Flags
    description: O segmento dos seus usuários que possuem uma <a href="/docs/developer_guide/feature_flags">Feature Flag</a> específica atualmente ativada.
    tags:
      - Retargeting
  - name: Subscription Group
    description: Segmenta seus usuários pelo grupo de inscrições para e-mail, SMS, MMS, RCS ou WhatsApp. Grupos arquivados não aparecem e não podem ser usados.
    tags:
      - Channel subscription behavior
  - name: Email Available
    description: Segmenta seus usuários por terem um endereço de e-mail válido e por estarem inscritos ou com opt-in para e-mail. Este filtro verifica três critérios&#58; se o usuário cancelou a inscrição de e-mails, se a Braze recebeu um hard bounce e se o e-mail foi marcado como spam. Se qualquer um desses critérios for atendido, ou se um e-mail não existir para um usuário, o usuário não é incluído.<br><br>Usuários cujo E-mail disponível é <code>false</code> são excluídos do público da Campaign e não recebem o e-mail — mesmo que suas configurações de envio estejam definidas para enviar a todos os usuários (incluindo usuários que cancelaram a inscrição).<br><br>Para e-mails em que o status de opt-in é importante, use E-mail disponível em vez de <a href="/docs/user_guide/audience/segments/segmentation_filters#email-address">Endereço de e-mail</a>. Os critérios adicionais ajudam a direcionar usuários que são elegíveis para receber e-mail.
    tags:
      - Channel subscription behavior
  - name: Email Opt In Date
    description: Segmenta seus usuários pela data em que fizeram opt-in para e-mail.
    tags:
      - Channel subscription behavior
  - name: Email Subscription Status
    description: Segmenta seus usuários pelo status de inscrição para e-mail.
    tags:
      - Channel subscription behavior
  - name: Email Unsubscribed Date
    description: Segmenta seus usuários pela data em que cancelaram a inscrição de e-mails futuros.
    tags:
      - Channel subscription behavior
  - name: Foreground Push Enabled
    description: Segmenta seus usuários que possuem autorização provisória de push ou estão habilitados para push em primeiro plano. Especificamente, essa contagem inclui:<br>1. Usuários iOS que estão provisoriamente autorizados para push. <br>2. Usuários que estão habilitados para push em primeiro plano e cujo status de inscrição de push não é cancelado, para qualquer um dos seus apps. Para esses usuários, essa contagem inclui apenas push em primeiro plano.<br><br>Push em primeiro plano ativado não inclui usuários que cancelaram a inscrição. <br><br>Após segmentar com esse filtro, você pode ver um detalhamento de quem está nesse segmento para Android, iOS e web no painel inferior, chamado <em>Usuários contatáveis</em>.
    tags:
      - Channel subscription behavior
  - name: Foreground Push Enabled for App
    description: Segmenta por se os usuários têm push ativado para o seu app no dispositivo deles. Usuários que estão habilitados para push em primeiro plano para um app. Isso não leva em conta o status de inscrição de push. Essa contagem inclui usuários que autorizaram provisoriamente tokens de push em primeiro plano e em segundo plano.
    tags:
      - Channel subscription behavior
  - name: Background or Foreground Push Enabled
    description: Segmenta por se os usuários possuem um token de push e não cancelaram a inscrição. Usuários que estão habilitados para push em segundo plano ou primeiro plano para qualquer um dos seus apps.
    tags:
      - Channel subscription behavior
  - name: Push Opt In Date
    description: Segmenta seus usuários pela data em que fizeram opt-in para push.
    tags:
      - Channel subscription behavior
  - name: Push Subscription Status
    description: Segmenta seus usuários pelo <a href="/docs/user_guide/channels/push/push_setup/push_subscription_states#push-subscription-state">status de inscrição</a> para push.
    tags:
      - Channel subscription behavior
  - name: Push Unsubscribed Date
    description: Segmenta seus usuários pela data em que cancelaram a inscrição de notificações por push futuras.
    tags:
      - Channel subscription behavior
  - name: Purchased Product
    description: Segmenta seus usuários por produtos comprados no seu app.
    tags:
      - Purchase behavior
  - name: Total Number of Purchases
    description: Segmenta seus usuários por quantas compras fizeram no seu app.
    tags:
      - Purchase behavior
  - name: X Product Purchased In Y Days
    description: Filtra usuários pelas vezes que um produto específico foi comprado.
    tags:
      - Purchase behavior
  - name: X Purchases in Last Y Days
    description: Segmenta seus usuários pelo número de vezes (entre 0 e 50) que fizeram uma compra no último número especificado de dias corridos entre 1 e 30. <br> <a href="/docs/x-in-y-behavior">Saiba mais sobre o comportamento X em Y aqui.</a>
    tags:
      - Purchase behavior
  - name: X Purchase Property In Y Days
    description: Segmenta seus usuários pelo número de vezes que uma compra foi feita em relação a uma determinada propriedade de compra no último número especificado de dias corridos entre 1 e 30. <br> <a href="/docs/x-in-y-behavior">Saiba mais sobre o comportamento X em Y aqui.</a>
    tags:
      - Purchase behavior
  - name: First Made Purchase
    description: Segmenta seus usuários pela primeira vez que um usuário fez uma compra no seu app.
    tags:
      - Purchase behavior
  - name: First Purchase For App
    description: Segmenta seus usuários pela primeira vez que um usuário fez uma compra no seu app.
    tags:
      - Purchase behavior
  - name: Last Made Purchase
    description: Filtra usuários pela última vez que fizeram uma compra.
    tags:
      - Purchase behavior
  - name: Last Purchased Product
    description: Filtra usuários por quando compraram por último um produto específico.
    tags:
      - Purchase behavior
  - name: Money Spent
    description: Segmenta seus usuários pela quantia de dinheiro que gastaram no seu app.
    tags:
      - Purchase behavior
  - name: X Money Spent in Y Days
    description: Segmenta seus usuários pela quantia de dinheiro que gastaram no seu app no último número especificado de dias corridos entre 1 e 30. Esse valor inclui apenas a soma das últimas 50 compras. <br> <a href="/docs/x-in-y-behavior">Saiba mais sobre o comportamento X em Y aqui.</a>
    tags:
      - Purchase behavior
  - name: Last order placed (last 730 days)
    description: Segmenta seus usuários por quando realizaram o último pedido, com base no <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">evento recomendado de eCommerce</a> para pedido realizado (espaços de trabalho que não rastreiam eventos de eCommerce não possuem dados para esse filtro). Os usuários são avaliados para esse filtro uma vez por dia, e a janela máxima de consulta é de 2 anos.<br><br>Este filtro está em beta. Entre em contato com o gerente de conta da Braze se tiver interesse em usar esse filtro.
    tags:
      - eCommerce
  - name: Total orders count (last 730 days)
    description: Segmenta seus usuários pela contagem total de pedidos de um usuário nos últimos 2 anos, com base no <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">evento recomendado de eCommerce</a> para pedido realizado (espaços de trabalho que não rastreiam eventos de eCommerce não possuem dados para esse filtro). Essa contagem exclui pedidos cancelados, que devem ser rastreados usando o <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">evento recomendado de eCommerce</a> para pedido cancelado. Os usuários são avaliados para esse filtro uma vez por dia.<br><br>Este filtro está em beta. Entre em contato com o gerente de conta da Braze se tiver interesse em usar esse filtro.
    tags:
      - eCommerce
  - name: Total orders count
    description: Segmenta seus usuários pela contagem total de pedidos de um usuário ao longo de toda a vida, com base no <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">evento recomendado de eCommerce</a> para pedido realizado (espaços de trabalho que não rastreiam eventos de eCommerce não possuem dados para esse filtro). Essa contagem exclui pedidos cancelados, que devem ser rastreados usando o <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">evento recomendado de eCommerce</a> para pedido cancelado. Os usuários são avaliados para esse filtro em tempo real.<br><br>Este filtro está em beta. Entre em contato com o gerente de conta da Braze se tiver interesse em usar esse filtro.
    tags:
      - eCommerce
  - name: Total canceled orders count (last 730 days)
    description: Segmenta seus usuários pela contagem total de pedidos que um usuário cancelou nos últimos 2 anos, com base no <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">evento recomendado de eCommerce</a> para pedido cancelado (espaços de trabalho que não rastreiam eventos de eCommerce não possuem dados para esse filtro). Os usuários são avaliados para esse filtro uma vez por dia.<br><br>Este filtro está em beta. Entre em contato com o gerente de conta da Braze se tiver interesse em usar esse filtro.
    tags:
      - eCommerce
  - name: Customer lifetime value (last 730 days)
    description: Segmenta seus usuários pela receita total que se espera que um usuário gere ao longo do seu histórico de compras com a sua marca. O cálculo considera os últimos 730 dias e utiliza o valor médio do pedido (AOV), multiplica pelo número total de pedidos realizados e então considera a duração ativa de compras do usuário (o intervalo de tempo entre o primeiro e o pedido mais recente). Este filtro usa dados rastreados em <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eventos recomendados de eCommerce</a> (espaços de trabalho que não rastreiam eventos de eCommerce não possuem dados para esse filtro). Os usuários são avaliados para esse filtro uma vez por dia.<br><br>Este filtro está em beta. Entre em contato com o gerente de conta da Braze se tiver interesse em usar esse filtro.
    tags:
      - eCommerce
  - name: Total refund value (last 730 days)
    description: Segmenta seus usuários pelo valor de reembolsos concedidos a um usuário nos últimos 2 anos, com base no <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">evento recomendado de eCommerce</a> para pedido reembolsado (espaços de trabalho que não rastreiam eventos de eCommerce não possuem dados para esse filtro). Os usuários são avaliados para esse filtro uma vez por dia.<br><br>Este filtro está em beta. Entre em contato com o gerente de conta da Braze se tiver interesse em usar esse filtro.
    tags:
      - eCommerce
  - name: Total refund value
    description: Segmenta seus usuários pelo valor total de reembolsos concedidos a um usuário ao longo de toda a vida, com base no <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">evento recomendado de eCommerce</a> para pedido reembolsado (espaços de trabalho que não rastreiam eventos de eCommerce não possuem dados para esse filtro). Os usuários são avaliados para esse filtro em tempo real.<br><br>Este filtro está em beta. Entre em contato com o gerente de conta da Braze se tiver interesse em usar esse filtro.
    tags:
      - eCommerce
  - name: Total revenue (last 730 days)
    description: Segmenta seus usuários pela receita total gerada a partir dos pedidos de um usuário nos últimos 2 anos, calculada subtraindo a receita associada ao <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">evento recomendado de eCommerce</a> para pedido reembolsado da receita associada ao evento de eCommerce para pedido realizado (espaços de trabalho que não rastreiam eventos de eCommerce não possuem dados para esse filtro). Os usuários são avaliados para esse filtro uma vez por dia.<br><br>Este filtro está em beta. Entre em contato com o gerente de conta da Braze se tiver interesse em usar esse filtro.
    tags:
      - eCommerce
  - name: Total revenue
    description: Segmenta seus usuários pela receita total gerada a partir dos pedidos de um usuário ao longo de toda a vida, calculada subtraindo a receita associada ao <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">evento recomendado de eCommerce</a> para pedido reembolsado da receita associada ao evento de eCommerce para pedido realizado (espaços de trabalho que não rastreiam eventos de eCommerce não possuem dados para esse filtro). Os usuários são avaliados para esse filtro em tempo real.<br><br>Este filtro está em beta. Entre em contato com o gerente de conta da Braze se tiver interesse em usar esse filtro.
    tags:
      - eCommerce
  - name: Average order value (last 730 days)
    description: Segmenta seus usuários pelo valor médio (média) dos pedidos de um usuário nos últimos 2 anos, com base no <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">evento recomendado de eCommerce</a> para pedido realizado (espaços de trabalho que não rastreiam eventos de eCommerce não possuem dados para esse filtro). Os usuários são avaliados para esse filtro uma vez por dia.<br><br>Este filtro está em beta. Entre em contato com o gerente de conta da Braze se tiver interesse em usar esse filtro.
    tags:
      - eCommerce
  - name: Country
    description: Segmenta seus usuários pela última localização de país indicada.
    tags:
      - Demographic attributes
  - name: City
    description: Segmenta seus usuários pela última localização de cidade indicada.
    tags:
      - Demographic attributes
  - name: Language
    description: Segmenta seus usuários pelo idioma preferido.
    tags:
      - Demographic attributes
  - name: Age
    description: Segmenta seus usuários pela idade, conforme indicado dentro do seu app.
    tags:
      - Demographic attributes
  - name: Birthday
    description: Segmenta seus usuários pela data de aniversário, conforme indicado dentro do seu app. <br> Usuários com aniversário em 29 de fevereiro são incluídos em segmentos que incluem 1º de março.<br><br>Para direcionar aniversários de dezembro ou janeiro, insira apenas a lógica de filtro dentro do período de 12 meses do ano que você está direcionando. Em outras palavras, não insira lógica que consulte o dezembro do ano anterior ou o janeiro do próximo ano. Por exemplo, para direcionar aniversários de dezembro, você pode filtrar por "em 31 de dezembro", "antes de 31 de dezembro" ou "depois de 30 de novembro".
    tags:
      - Demographic attributes
  - name: Gender
    description: Segmenta seus usuários por gênero, conforme indicado dentro do seu app.
    tags:
      - Demographic attributes
  - name: Unformatted Phone Number
    description: Segmenta seus usuários pelo número de telefone não formatado. Não inclui parênteses, hifens ou outros símbolos.
    tags:
      - Demographic attributes
  - name: First Name
    description: Segmenta seus usuários pelo nome, conforme indicado dentro do seu app.
    tags:
      - Demographic attributes
  - name: Last Name
    description: Segmenta seus usuários pelo sobrenome, conforme indicado dentro do seu app.
    tags:
      - Demographic attributes
  - name: Has App
    description: Segmenta por se um usuário já instalou seu app. Isso inclui usuários que atualmente possuem seu app instalado e aqueles que desinstalaram no passado. Geralmente, isso requer que os usuários abram o app (iniciar uma sessão) para serem incluídos nesse filtro. No entanto, existem algumas exceções, como se um usuário foi importado para a Braze e associado manualmente ao seu app.
    tags:
      - App
  - name: Most Recent App Version Name
    description: Segmenta pelo nome mais recente da versão do app do usuário.<br><br>Ao usar "menor que" ou "menor ou igual a", se a versão principal do app não existir, esse filtro retorna <code>true</code> porque o usuário é mais antigo que a versão do app. Isso significa que, se a última versão principal do app do usuário não existir, ele automaticamente corresponde ao filtro.
    tags:
      - App
  - name: Most Recent App Version Number
    description: Segmenta pelo número da versão mais recente do app do usuário. O número da versão dentro dos parênteses é usado para filtragem, enquanto o número que o precede é apenas para referência — por exemplo, em "3.7.0(134.0.0.0)", "134.0.0.0" é o número da versão filtrado.<br><br>Ao usar "menor que" ou "menor ou igual a", se a versão principal do app não existir, esse filtro retorna <code>true</code> porque o usuário é mais antigo que a versão do app. Isso significa que, se a última versão principal do app do usuário não existir, ele automaticamente corresponde ao filtro.<br><br>Pode levar algum tempo para que as versões atuais do app sejam preenchidas. A versão do app no perfil do usuário é atualizada quando a informação é capturada pelo SDK, o que depende de quando os usuários abrem seus apps. Se o usuário não abrir o app, a versão atual não será atualizada. Esses filtros também não se aplicam retroativamente. É recomendável usar "maior que" ou "igual a" para versões atuais e futuras, mas usar filtros de versões passadas pode causar comportamentos inesperados.
    tags:
      - App
  - name: Uninstalled
    description: Segmenta seus usuários por estarem atualmente marcados como desinstalados no backend. Usuários que desinstalaram e depois reinstalaram o app não são incluídos. Este filtro reflete o estado atual de desinstalação, não um registro histórico de cada evento de desinstalação.
    tags:
      - Uninstall
  - name: Device Carrier
    description: Segmenta seus usuários pela operadora do dispositivo.
    tags:
      - Devices
  - name: Device Count
    description: Segmenta seus usuários por quantos dispositivos usaram seu app.
    tags:
      - Devices
  - name: Device Model
    description: Segmenta seus usuários pela versão do modelo do celular.
    tags:
      - Devices
  - name: Device OS
    description: Segmenta seus usuários que possuem um ou mais dispositivos com o sistema operacional especificado. Para segmentar usuários por uma faixa de sistemas operacionais, use o filtro <a href="/docs/user_guide/audience/segments/segmentation_filters#device-os-version-number">Número da versão do SO do dispositivo</a>.
    tags:
      - Devices
  - name: Device OS Version Number
    description: Segmenta seus usuários que possuem um ou mais dispositivos com uma versão de sistema operacional dentro de uma faixa especificada. Por exemplo, você pode direcionar usuários que possuem um sistema operacional iOS com versão maior ou igual a 26.0.
    tags:
      - Devices
  - name: Most Recent Device Locale
    description: Segmenta seus usuários pelas <a href="/docs/user_guide/messaging/messaging_fundamentals/localization">informações de localidade</a> do dispositivo usado mais recentemente.
    tags:
      - Devices
  - name: Most Recent Watch Model
    description: Segmenta seus usuários pelo modelo de smartwatch mais recente.
    tags:
      - Devices
  - name: Provisionally Authorized on iOS
    description: Permite encontrar usuários que estão provisoriamente autorizados no iOS 12 para um determinado app.
    tags:
      - Devices
  - name: Web Browser
    description: Segmenta seus usuários pelo navegador web que usam para acessar seu site. Este filtro corresponde a qualquer navegador no histórico de dispositivos do usuário, não apenas ao navegador usado mais recentemente.
    tags:
      - Devices
  - name: Device IDFA
    description: Permite designar os destinatários da sua Campaign por IDFA para testes.
    tags:
      - Advertising use cases
  - name: Device IDFV
    description: Permite designar os destinatários da sua Campaign por IDFV para testes.
    tags:
      - Advertising use cases
  - name: Device Google Ad ID
    description: Segmenta seus usuários pelo ID de anúncio do Google.
    tags:
      - Advertising use cases
  - name: Device Roku Ad ID
    description: Segmenta seus usuários pelo ID de anúncio Roku.
    tags:
      - Advertising use cases
  - name: Device Windows Ad ID
    description: Segmenta seus usuários pelo ID de anúncio Windows.
    tags:
      - Advertising use cases
  - name: Ad Tracking Enabled
    description: Permite filtrar com base em se seus usuários fizeram opt-in para rastreamento de anúncios. O rastreamento de anúncios está relacionado ao IDFA ou "identificador para anunciantes" atribuído a todos os dispositivos iOS pela Apple, que pode ser configurado por SDKs. Esse identificador permite que anunciantes rastreiem usuários e veiculem anúncios direcionados.
    tags:
      - Advertising use cases
  - name: Most Recent Location
    description: Segmenta seus usuários pela última localização registrada em que usaram seu app.
    tags:
      - Location
  - name: Location Available
    description: Segmenta seus usuários por terem reportado suas localizações. Para usar esse filtro, seu app precisa ter o <a href="/docs/search?query=location%20tracking">monitoramento de localização integrado.</a>
    tags:
      - Location
  - name: Amplitude Cohorts
    description: Clientes que usam o Amplitude podem complementar seus segmentos escolhendo e importando suas coortes no Amplitude.
    tags:
      - Cohort membership
  - name: Census Cohorts
    description: Clientes que usam o Census podem complementar seus segmentos escolhendo e importando suas coortes no Census.
    tags:
      - Cohort membership
  - name: Heap Cohorts
    description: Clientes que usam o Heap podem complementar seus segmentos escolhendo e importando suas coortes no Heap.
    tags:
      - Cohort membership
  - name: Hightouch Cohorts
    description: Clientes que usam o Hightouch podem complementar seus segmentos escolhendo e importando suas coortes no Hightouch.
    tags:
      - Cohort membership
  - name: Kubit Cohorts
    description: Clientes que usam o Kubit podem complementar seus segmentos escolhendo e importando suas coortes no Kubit.
    tags:
      - Cohort membership
  - name: Mixpanel Cohorts
    description: Clientes que usam o Mixpanel podem complementar seus segmentos escolhendo e importando suas coortes no Mixpanel.
    tags:
      - Cohort membership
  - name: Segment Cohorts
    description: Clientes que usam o Segment podem complementar seus segmentos escolhendo e importando suas coortes no Segment.
    tags:
      - Cohort membership
  - name: Tinyclues Cohorts
    description: Clientes que usam o Tinyclues podem complementar seus segmentos escolhendo e importando suas coortes no Tinyclues.
    tags:
      - Cohort membership
  - name: Install Attribution Ad
    description: Segmenta seus usuários pelo anúncio ao qual a instalação foi atribuída.
    tags:
      - User Attributes
  - name: Install Attribution Adgroup
    description: Segmenta seus usuários pelo grupo de anúncios ao qual a instalação foi atribuída.
    tags:
      - Install attribution
  - name: Install Attribution Campaign
    description: Segmenta seus usuários pela campanha de anúncio à qual a instalação foi atribuída.
    tags:
      - Install attribution
  - name: Install Attribution Source
    description: Segmenta seus usuários pela origem à qual a instalação foi atribuída.
    tags:
      - Install attribution
  - name: Churn Risk Category
    description: Segmenta seus usuários pela categoria de risco de churn de acordo com uma previsão específica.
    tags:
      - Intelligence and predictive
  - name: Churn Risk Score
    description: Segmenta seus usuários pela pontuação de risco de churn de acordo com uma previsão específica.
    tags:
      - Intelligence and predictive
  - name: Event Likelihood Category
    description: Segmenta seus usuários pela probabilidade de realizar um evento de acordo com uma previsão específica.
    tags:
      - Intelligence and predictive
  - name: Event Likelihood Score
    description: Segmenta seus usuários pela pontuação de probabilidade de realizar um evento de acordo com uma previsão específica.
    tags:
      - Intelligence and predictive
  - name: Intelligent Channel
    description: Segmenta seus usuários pelo canal mais ativo nos últimos três meses.
    tags:
      - Intelligence and predictive
  - name: Message Open Likelihood
    description: Filtra seus usuários com base na <a href="/docs/user_guide/brazeai/intelligence_suite/intelligent_channel#individual-channels">probabilidade de abrir uma mensagem em um canal especificado</a> em uma escala de 0 a 100%. Usuários sem dados suficientes para medir a probabilidade de um canal podem ser selecionados usando "está em branco".<br><br>Para e-mail, aberturas por máquina são excluídas do cálculo de probabilidade.
    tags:
      - Intelligence and predictive
  - name: Number of Facebook Friends Using App
    description: Segmenta seus usuários por quantos amigos do Facebook usam o mesmo app.
    tags:
      - Social activity
  - name: Connected Facebook
    description: Segmenta seus usuários por terem conectado seu app ao Facebook.
    tags:
      - Social activity
  - name: Connected Twitter
    description: Segmenta seus usuários por terem conectado seu app ao X (antigo Twitter).
    tags:
      - Social activity
  - name: Number of Twitter Followers
    description: Segmenta seus usuários por quantos seguidores possuem no X (antigo Twitter).
    tags:
      - Social activity
  - name: Phone Number
    description: Segmenta seus usuários pelo campo de número de telefone no formato E.164.<br><br> Quando um número de telefone é enviado para a Braze, a Braze tenta convertê-lo para o <a href="/docs/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#importing-phone-numbers">formato E.164</a> que é usado para enviar por canais SMS, RCS e WhatsApp. O processo de conversão pode falhar se o número não estiver formatado corretamente, o que resulta no perfil do usuário tendo um número de telefone não formatado, mas não um número de telefone de envio. Este filtro de segmento retorna usuários pelo número de telefone no formato E.164 (quando disponível).<br><br>Casos de uso:<br> - Use esse filtro para entender o tamanho mais preciso do público-alvo ao enviar mensagens SMS, RCS ou WhatsApp.<br>- Use expressões regulares (regex) com esse filtro para segmentar por números de telefone com um código de país específico. <br>- Use esse filtro para segmentar usuários por números de telefone que falharam no processo de conversão para E.164.
    tags:
      - Other Filters
---