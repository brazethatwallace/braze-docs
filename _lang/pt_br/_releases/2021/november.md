---
nav_title: Novembro
page_order: 1
noindex: true
page_type: update
description: "Este artigo contém notas de versão para novembro de 2021."
---
# Novembro de 2021 {#november-2021}

## Métrica de relatório de taxa de clique para abertura {#click-to-open-rate-reporting-metric}
A Braze adicionou uma nova métrica de e-mail, taxa de cliques por abertura, disponível no [Criador de relatórios]({{site.baseurl}}/user_guide/analytics/reports/report_builder/). Essa métrica representa a porcentagem de e-mails abertos que foram clicados.

## Métrica de abertura por máquina {#machine-open-reporting-metric}

Uma nova métrica de e-mail, [Aberturas por máquina]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/#machine-opens), está disponível nas páginas de análise de dados de Canvas e Campaigns para e-mails. Essa métrica identifica aberturas de e-mail que não são humanas (como as abertas pelos servidores da Apple), exibidas como um subconjunto do total de aberturas.

## Variável Liquid random_bucket_number {#randombucketnumber-liquid-variable}
Uma variável `random_bucket_number` foi adicionada à lista de [variáveis Liquid suportadas]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags) para personalização de mensagens.

## Diretrizes de notificação por push avançada do iOS 15 {#ios-15-rich-push-notification-guidelines}
Novas [diretrizes de notificação por push do iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications/) foram adicionadas à documentação de notificações avançadas do iOS, incluindo informações sobre estados de notificação e uma análise das variáveis de truncamento de texto.

## IPs para lista de permissões na UE para webhooks e conteúdo conectado {#ips-to-whitelist-in-eu-for-webhooks-and-connected-content}
IPs adicionais para incluir na lista de permissões na UE para webhooks e conteúdo conectado foram adicionados ao nosso artigo de [webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/) e [conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/). Esses novos IPs incluem `18.157.135.97`, `3.123.166.46`, `3.64.27.36`, `3.65.88.25`, `3.68.144.188` e `3.70.107.88`.

## Endpoint de exportação de compras {#export-purchases-endpoint}
Um novo [endpoint `/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) foi adicionado à Braze. Esse endpoint retorna listas paginadas de IDs de produtos.

## Novas parcerias Braze {#new-braze-partnerships}

### Adobe - CDP or plataforma de dados do cliente or CDP or plataforma de dados do cliente or plataforma de dados do cliente {#adobe-customer-data-platform}
A integração da Braze com a [Adobe]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/adobe/#adobe) permite que as marcas conectem e mapeiem seus dados da Adobe (atributos personalizados e segmentos) para a Braze em tempo real. As marcas podem então agir com base nesses dados, oferecendo experiências personalizadas e direcionadas a esses usuários.

### BlueConic - CDP or plataforma de dados do cliente or CDP or plataforma de dados do cliente or plataforma de dados do cliente {#blueconic-customer-data-platform}
Com a [BlueConic]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/blueconic/#blueconic), os usuários da empresa podem unificar dados em perfis individuais persistentes e, em seguida, sincronizá-los em pontos de contato e sistemas de clientes para apoiar uma ampla gama de iniciativas focadas no crescimento, incluindo orquestração do ciclo de vida do cliente, modelagem e análise de dados, produtos e experiências digitais, monetização baseada em público e mais.

### Worthy - Conteúdo dinâmico {#worthy-dynamic-content}
A integração da Braze com a [Worthy]({{site.baseurl}}/partners/message_personalization/dynamic_content/worthy/#worthy) permite que você crie facilmente experiências personalizadas e ricas no app usando o editor de conteúdo dinâmico de arrastar e soltar da Worthy e as entregue por meio da Braze.

### Judo - Conteúdo dinâmico {#judo-dynamic-content}
A integração entre [Judo]({{site.baseurl}}/partners/message_personalization/dynamic_content/judo/#judo) e Braze permite que você substitua componentes da sua campanha por experiências Judo. Os dados da Braze podem ser usados para apoiar conteúdo personalizado em uma experiência Judo. Eventos do usuário e dados da experiência podem ser retroalimentados na Braze para atribuição e direcionamento.

### LINE - Envio de mensagens {#line-messaging}
A integração [LINE]({{site.baseurl}}/partners/message_orchestration/additional_channels/messaging/line/#line) e Braze permite que você aproveite os webhooks, segmentação avançada, personalização e recursos de disparo da Braze para enviar mensagens aos seus usuários no LINE por meio da [API or interface de programação do aplicativo (API) de envio de mensagens do LINE](https://developers.line.biz/en/docs/messaging-api/overview/).

### RevenueCat - Pagamentos {#revenuecat-payments}
A integração [RevenueCat]({{site.baseurl}}/partners/data_and_infrastructure_agility/payments/revenuecat/#revenuecat) e Braze permite que você sincronize automaticamente os eventos do ciclo de vida de compra e inscrição dos seus clientes em todas as plataformas. Isso permite que você crie campanhas que reagem ao estágio do ciclo de vida da inscrição dos seus clientes, como engajar com clientes que cancelaram durante o período de teste gratuito ou enviar lembretes para clientes com problemas de faturamento.

### Punchh - Fidelidade {#punchh-loyalty}
A [Punchh]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#punchh) fez parceria com a Braze para sincronizar dados entre as duas plataformas para fins de presentes e fidelidade. Os dados publicados na Braze estarão disponíveis para segmentação e podem sincronizar dados de usuários de volta ao Punchh por meio de modelos de webhook configurados na Braze.