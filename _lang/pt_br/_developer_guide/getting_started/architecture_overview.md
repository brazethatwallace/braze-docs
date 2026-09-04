---
nav_title: Visão geral da arquitetura
article_title: Visão geral da arquitetura
page_order: 3
description: "Este artigo discute as diferentes partes e peças do stack de tecnologia da Braze, com links para artigos relevantes."
platform:
  - iOS
  - Android
  - Web
  - React Native
  - Flutter
  - Cordova
  - Roku
  - Swift
  - Unity
---

# Como começar: Visão geral da arquitetura {#getting-started-architectural-overview}

> Este artigo discute as diferentes partes e peças do stack de tecnologia da Braze, com links para artigos relevantes.

Em um nível geral, a Braze trata de dados. A plataforma da Braze, com o SDK, a REST API e as integrações com parceiros, permite que você agregue e atue em cima dos seus dados.

![A Braze tem diferentes camadas. No total, ela é formada pelo SDK, a API, o dashboard e as integrações com parceiros. Cada uma delas contribui com partes de uma camada de ingestão de dados, uma camada de classificação, uma camada de orquestração, uma camada de personalização e uma camada de ação. A camada de ação tem vários canais, incluindo push, mensagens no app, catálogo conectado, webhook, SMS e e-mail.]({% image_buster /assets/img/getting-started/braze_listen_understand_act.png %}){: style="display:block;margin:auto;" }

* [Ingestão de dados](#ingestion): A Braze extrai dados de uma variedade de fontes.
* [Classificação](#classification): Sua equipe de marketing segmenta dinamicamente sua base de usuários usando essas métricas.
* [Orquestração](#orchestration): A Braze coordena de forma inteligente as mensagens para diferentes segmentos de público no momento ideal.
* [Ação](#action): Sua equipe de marketing age com base nos dados, criando conteúdo por meio de uma variedade de canais de envio de mensagens, como SMS e e-mail.
* [Personalização](#personalization): Os dados são transformados em tempo real com informações personalizadas sobre seu público.
* [Exportação](#exporting-data): Em seguida, a Braze rastreia o engajamento dos seus usuários com essas mensagens e os alimenta novamente na plataforma, criando um loop. Você obtém insights sobre esses dados por meio de relatórios e análises em tempo real.

Tudo isso funciona em conjunto para criar interações bem-sucedidas entre sua base de usuários e sua marca, de modo que você possa atingir suas metas. A Braze faz tudo isso no contexto de algo que chamamos de nosso stack verticalmente integrado. Vamos nos aprofundar em cada camada, uma de cada vez.

## Ingestão de dados {#ingestion}

A Braze foi desenvolvida com base em uma arquitetura de fluxo de dados que utiliza Snowflake, Kafka, MongoDB e Redis. Dados de muitas fontes podem ser carregados na Braze por meio do SDK e da API. A plataforma pode lidar com qualquer dado em tempo real, independentemente de como esteja aninhado ou estruturado. Os dados na Braze são armazenados no perfil do usuário.

{% alert tip %}
A Braze pode rastrear os dados de um usuário durante toda a jornada dele com você, desde o momento em que ele é anônimo até o momento em que faz login no seu app e é conhecido. As IDs de usuário, chamadas `external_id`s na Braze, devem ser definidas para cada um dos seus usuários. Elas devem ser imutáveis e acessíveis quando um usuário abre o app, permitindo o rastreamento dos seus usuários entre dispositivos e plataformas. Consulte o artigo [Ciclo de vida do perfil de usuário]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle) para obter as práticas recomendadas.
{% endalert %}

![A Braze importa fontes de dados de backend da API, fontes de dados de frontend do SDK, dados de data warehouse pela Ingestão de Dados na Nuvem da Braze e de integrações com parceiros. Esses dados são exportados por meio da API da Braze]({% image_buster /assets/img/getting-started/import-export.png %}){: style="display:block;margin:auto;" }

{% alert note %}
Esse banco de dados de perfil de usuário centrado na pessoa permite velocidade interativa e em tempo real. A Braze pré-computa os valores quando os dados chegam e armazena os resultados em nosso formato de documento leve para recuperação rápida. E como a plataforma foi projetada dessa forma desde o início, ela é ideal para a maioria dos casos de uso de envio de mensagens, especialmente quando combinada com outros conceitos de dados, como Conteúdo Conectado, catálogos de produtos e atributos aninhados.
{% endalert %}

### Detalhamento das fontes de dados {#data-source-breakdown}

A Braze utiliza diferentes sistemas de armazenamento de dados para várias funcionalidades. Entender quais funcionalidades usam quais fontes de dados é importante para a gestão de dados e resolução de problemas.

#### Funcionalidades baseadas em MongoDB {#mongodb-powered-features}
- Eventos personalizados (rastreados pelo SDK e pela API)
- Atributos personalizados
- Perfis de usuário
- Eventos de compra
- A maioria das funcionalidades de segmentação e direcionamento

#### Funcionalidades baseadas em Snowflake {#snowflake-powered-features}
- [Extensões de Segment SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)
- [Pacote de previsões]({{site.baseurl}}/user_guide/brazeai)
- [Recomendações de itens personalizados por IA]({{site.baseurl}}/user_guide/brazeai/item_recommendations/creating_recommendations/ai)
- [Taxa de abertura real estimada]({{site.baseurl}}/user_guide/channels/email/reporting#estimated-real-open-rate) (não utiliza eventos personalizados)

{% alert important %}
**Considerações sobre remoção de dados:** Eventos personalizados são armazenados no MongoDB e são separados dos dados do Snowflake. Se você precisar remover dados de eventos personalizados errôneos, deve tratá-los no MongoDB. Funcionalidades baseadas em Snowflake (como extensões de Segment SQL e outras funcionalidades baseadas em Snowflake) utilizam dados do Snowflake, que são tratados separadamente. Remover dados de um sistema não remove automaticamente do outro.
{% endalert %}

### Fontes de dados de backend por meio da API da Braze {#backend-data-sources-through-the-braze-api}
A Braze pode extrair dados de bancos de dados de usuários, transações off-line e data warehouses por meio da nossa [REST API]({{site.baseurl}}/api/endpoints/user_data).

### Fontes de dados de frontend por meio do SDK da Braze {#frontend-data-sources-through-braze-sdk}
A Braze captura automaticamente dados primários de fontes de dados de frontend, como dispositivos dos usuários, por meio do [SDK da Braze]({{site.baseurl}}/user_guide/get_started/sdk_overview). O SDK lida com novos usuários (anônimos) e gerencia os dados do perfil de usuário durante todo o ciclo de vida.

### Integrações com parceiros {#partner-integrations}
A Braze tem mais de 150 parceiros de tecnologia, que chamamos de "Alloys". Você pode complementar seus feeds de dados por meio de uma rede significativamente robusta de [tecnologias interoperáveis e APIs de dados.]({{site.baseurl}}/partners/home)

### Conexão direta com o data warehouse por meio da Ingestão de Dados na Nuvem da Braze {#direct-warehouse-connection-through-braze-cloud-data-ingestion}
É possível enviar dados de clientes do seu data warehouse para a plataforma por meio da [Ingestão de Dados na Nuvem da Braze]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) em apenas alguns minutos, permitindo a sincronização de atributos, eventos e compras relevantes do usuário. A integração da Ingestão de Dados na Nuvem oferece suporte a estruturas de dados complexas, incluindo JSON aninhado e arrays de objetos.

A Ingestão de Dados na Nuvem pode sincronizar dados do Snowflake, Amazon Redshift, Databricks e Google BigQuery.

## Classificação {#classification}
A camada de classificação permite que sua equipe classifique e crie públicos dinamicamente, chamados [segmentos]({{site.baseurl}}/user_guide/audience/segments), com base nos dados que passam pela Braze.

{% alert note %}
As camadas de classificação, orquestração e personalização são onde sua equipe de marketing fará a maior parte do trabalho. Eles interagem com essas camadas com mais frequência por meio do dashboard da Braze, nossa interface web. Os desenvolvedores têm uma função na configuração e na personalização dessas camadas.
{% endalert %}

Muitos tipos comuns de atributos do usuário, como nome, e-mail, data de nascimento, país e outros, são automaticamente rastreados pelo SDK por padrão. Como desenvolvedor, você trabalhará com a sua equipe para definir quais dados adicionais e personalizados fazem sentido rastrear para o seu caso de uso. Seus dados personalizados afetarão a forma como sua base de usuários será classificada e segmentada. Você definirá esse modelo de dados durante o processo de implementação.

Saiba mais sobre [dados coletados automaticamente e dados personalizados]({{site.baseurl}}/developer_guide/analytics).

## Orquestração {#orchestration}
A camada de orquestração permite que sua equipe de marketing projete jornadas de usuário com base nos dados de usuários e no engajamento anterior. Esse trabalho é feito principalmente por meio da nossa interface de dashboard, mas você também tem a opção de lançar [campanhas por meio da API]({{site.baseurl}}/api/api_campaigns). Por exemplo, você pode fazer com que seu backend informe à Braze quando enviar as mensagens e campanhas que seus profissionais de marketing projetaram no dashboard e dispará-las de acordo com a sua lógica de backend. Um exemplo de mensagem disparada pela API pode ser a redefinição de senha ou a confirmação de envio.

{% alert note %}
As campanhas disparadas por API são ideais para casos de uso transacionais mais avançados. Elas permitem que os profissionais de marketing gerenciem o texto da campanha, os testes multivariantes e as regras de reelegibilidade no dashboard da Braze, enquanto disparam a entrega desse conteúdo a partir dos seus servidores e sistemas. A solicitação da API para disparar a mensagem também pode incluir dados adicionais a serem modelados na mensagem em tempo real.
{% endalert %}


### Feature Flags {#feature-flags}
A Braze permite ativar ou desativar remotamente a funcionalidade para uma seleção de usuários por meio de [Feature Flags]({{site.baseurl}}/developer_guide/feature_flags). Isso permite que os profissionais de marketing direcionem o Segment correto da sua base de usuários com envio de mensagens para recursos que ainda não foram implementados para todo o público. Mas, mais do que isso, as Feature Flags podem ser usadas para ativar e desativar um recurso em produção sem implementação de código adicional ou atualizações da loja de aplicativos. Isso permite que você implemente novos recursos com segurança e confiança.

## Personalização {#personalization}
A camada de personalização representa a capacidade de fornecer conteúdo dinâmico em suas mensagens. Ao usar o Liquid, uma linguagem de personalização amplamente utilizada, sua equipe pode extrair dinamicamente os dados existentes para exibir a mensagem personalizada para cada destinatário. Além disso, você pode inserir qualquer informação acessível no seu servidor web ou por meio da API diretamente nas mensagens que está enviando, como notificações por push ou e-mails, usando [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content). O Conteúdo conectado se baseia no Liquid e usa uma sintaxe familiar.

E como esse conteúdo dinâmico é programável, os profissionais de marketing podem incluir valores computados, respostas de outras chamadas ou itens do catálogo de produtos. Depois de configurar esses sistemas durante a implementação, sua equipe de marketing pode fazer isso com pouco ou nenhum suporte das equipes técnicas.

## Ação {#action}
A camada de ação permite o envio real de mensagens aos seus usuários. O objetivo da camada de ação é enviar a mensagem certa para o usuário certo no momento certo, com base nos dados disponíveis em todas as camadas discutidas anteriormente. O envio de mensagens é feito dentro do seu app ou site (como o envio de mensagens no app ou por meio de elementos gráficos como carrosséis e banners de Content Cards) ou fora da experiência no app (como o envio de notificações por push ou e-mails).

### Canais de envio de mensagens {#messaging-channels}
A Braze foi projetada para lidar com um cenário tecnológico em evolução com seu modelo de dados independente de canal e centrado no usuário. O dashboard gerencia a entrega de mensagens e os disparos transacionais. Por exemplo, seus profissionais de marketing podem disparar uma mensagem SMS oferecendo um cupom para uma das suas lojas recém-inauguradas quando um usuário entrar no geofence definido próximo a esse local, ou enviar um e-mail a um usuário para informá-lo de que seu programa favorito tem uma nova temporada.

O [SDK da Braze]({{site.baseurl}}/user_guide/get_started/sdk_overview) possibilita canais adicionais de envio de mensagens: push, mensagens no app e Content Cards. Você integra o SDK ao seu app ou site para permitir que sua equipe de marketing use o dashboard da Braze para coordenar suas campanhas em todos os canais de envio de mensagens compatíveis.

![Diagrama dos canais de envio de mensagens da Braze disponíveis por meio do SDK.]({% image_buster /assets/img/getting_started/channels.png %})

## Exportação de dados {#exporting-data}
É fundamental saber que todas as interações dos usuários finais com a Braze são rastreadas para que você possa medir seu engajamento e alcance. Depois que a Braze agrega seus dados de todas essas fontes, eles podem ser exportados de volta para sua stack de tecnologia usando diversas ferramentas, fechando o ciclo.

### Currents
O [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) é um complemento opcional da Braze que fornece uma exportação granular de streaming que alimenta continuamente outros destinos da sua stack. O Currents é um feed de dados brutos por usuário e por evento que exporta dados a cada cinco minutos ou a cada 15.000 eventos, o que ocorrer primeiro. Exemplos de destinos downstream para o Currents incluem Segment, S3, Redshift e Mixpanel, entre outros.

### Compartilhamento de dados do Snowflake {#snowflake-data-sharing}
A funcionalidade de [compartilhamento seguro de dados]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake) do Snowflake permite que a Braze ofereça acesso seguro aos dados em nosso portal Snowflake, sem preocupações com atritos no fluxo de trabalho, pontos de falha e custos desnecessários comuns em relacionamentos típicos com provedores de dados. Todo o compartilhamento é realizado por meio da camada de serviços e do armazenamento de metadados exclusivos do Snowflake: nenhum dado é copiado ou transferido entre contas. Esse é um conceito importante porque os dados compartilhados não ocupam espaço de armazenamento na conta do consumidor e, portanto, não contribuem para suas cobranças mensais de armazenamento de dados. As únicas cobranças para os consumidores são pelos recursos computacionais (ou seja, warehouses virtuais) usados para consultar os dados compartilhados.

### APIs de exportação da Braze {#braze-export-apis}
A API da Braze fornece [endpoints]({{site.baseurl}}/api/endpoints/export) que permitem exportar programaticamente análises de dados agregadas, bem como dados individuais de usuários. Esses dados podem ser exportados para públicos e Segments de qualquer tamanho.

### CSVs {#csvs}
Por fim, existe a opção de baixar seus dados em nível agregado diretamente do dashboard como um [CSV]({{site.baseurl}}/user_guide/data/distribution/export_braze_data). A opção de CSV permite que os membros da sua equipe exportem dados da Braze com facilidade.

{% alert tip %}
Embora a exportação em CSV tenha um limite base de 500.000 linhas, as APIs não possuem esse tipo de limite.
{% endalert %}

## Juntando tudo {#putting-it-all-together}
Uma das suas usuárias, vamos chamá-la de Mel, acabou de receber o anúncio do seu produto. Nos bastidores, todas as camadas da plataforma Braze trabalharam juntas para garantir que esse processo ocorresse sem problemas.

As informações da Mel foram importadas para a Braze a partir da sua plataforma de engajamento com clientes legada por meio de uma importação de CSV. Cada vez que a Mel interagiu com o seu app após a integração, mais dados foram adicionados ao perfil de usuário dela.

O anúncio do seu produto foi enviado para todos os clientes que curtiram um item semelhante no seu app. Você definiu esse dado como um evento personalizado. O SDK rastreou esse evento e segmentou a sua base de usuários de acordo. A Braze orquestrou o melhor horário do dia para enviar esse anúncio e personalizou a mensagem chamando a Mel pelo nome preferido dela.

Quando a Mel abre o anúncio, ela adiciona o novo produto à lista de desejos. A Braze rastreia automaticamente que ela clicou no e-mail. O SDK rastreia que ela adicionou o novo produto à lista de desejos. Cada vez que interagem com a sua marca, você e seus usuários aprendem mais uns sobre os outros.

![Diagrama mostrando como a Braze rastreia ações de usuários nos canais de envio de mensagens.]({% image_buster /assets/img/getting-started/putting-it-all-together.png %})