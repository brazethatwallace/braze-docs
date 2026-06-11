---
nav_title: Abril
page_order: 9
noindex: true
page_type: update
description: "Este artigo contém notas de versão de abril de 2017."
---

# Abril de 2017 {#april-2017}

## Mensagens no navegador em HTML {#html-in-browser-messages}

Agora, oferecemos suporte a tipos de mensagens interativas no navegador, incluindo HTML personalizado e formatos de captura de e-mail, o que permite alcançar seus clientes onde quer que eles estejam. Saiba mais sobre as [mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages/best_practices/).

## Mensagem personalizada no app com conteúdo conectado {#personalized-in-app-message-with-connected-content}

Adicionamos os blocos {% raw %} {%connected_content%} {% endraw %} nas mensagens no app disparadas, o que permite adicionar personalização avançada inserindo qualquer informação acessível via API diretamente em suas mensagens. Agora, você pode usar o Conteúdo conectado dentro do seu app, além de push, e-mail e webhooks. Saiba mais sobre o [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/).

## Navegação aprimorada para cartões do News Feed {#improved-navigation-for-news-feed-cards}

Melhoramos a interface do usuário para a criação de cartões do News Feed, facilitando a navegação e a criação de suas campanhas. Saiba mais sobre os [cartões do News Feed]({{site.baseurl}}/user_guide/engagement_tools/news_feed/creating_a_news_feed_item/#news-feed-cards).

## Prévia aprimorada das notificações Rich do iOS {#improved-preview-for-ios-rich-notifications}

Nossas prévias de notificações no iOS agora exibem notificações Rich, oferecendo uma visão clara do que exatamente está sendo enviado aos seus clientes, até o tamanho da fonte. Saiba mais sobre as [notificações Rich do iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#ios-10-rich-notifications).

## Adição de "aberturas por influência" às estatísticas de push {#added-influenced-opens-to-push-statistics}

Adicionamos "aberturas por influência" à nossa lista de estatísticas padrão de Campaign e Canvas oferecidas na Braze, facilitando o conhecimento do detalhamento de aberturas influenciadas, diretas e totais de suas campanhas. Saiba mais sobre as [aberturas por influência]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens/).

## Fazer upgrade para grupos internos {#upgrade-to-internal-groups}

Agora é possível criar vários Grupos internos e atribuir propriedades que indicam se o grupo será usado para registro de SDK, registro de REST API ou teste de conteúdo de mensagens. Saiba mais sobre os [registros de usuários de eventos]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab).

> Atualização: Os Grupos internos também podem ser usados para o [envio de e-mails de teste]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/#seed-groups).

## Novas opções para URLs da web {#new-options-for-web-urls}

Agora você tem a opção de abrir URLs da web em um navegador externo para mensagens push, mensagens no app e no navegador e cartões do News Feed. A ação "Deep Link into App" agora também é compatível com deep links HTTP/HTTPS. Se estiver usando um parceiro como a Branch ou o Universal Links da Apple, você precisará personalizar o SDK. Saiba mais sobre o [deep linking]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls/#what-is-deep-linking).

## Novo evento "Performed Conversion" no Canvas {#new-performed-conversion-event-canvas}

Adicionamos um novo evento "Performed Conversion" e um filtro "In Canvas Control" para melhorar as opções de redirecionamento. Saiba mais sobre o uso de [filtros de redirecionamento]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns/#retarget-campaigns).