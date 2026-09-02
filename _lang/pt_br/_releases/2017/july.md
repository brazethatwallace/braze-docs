---
nav_title: Julho
page_order: 6
noindex: true
page_type: update
description: "Este artigo contém notas de versão de julho de 2017."
---

# Julho de 2017 {#july-2017}

## Imagens grandes em push para a web {#large-images-in-web-push}

Adicionamos suporte para imagens grandes no push para a web no Chrome para Windows e Android, oferecendo a capacidade de criar experiências ricas e envolventes para os clientes. Saiba mais sobre [push para a web]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/web/).

## Atualizações nos campos de e-mail {#updates-to-email-fields}

Agora você pode bloquear e-mails para um conjunto específico de endereços de remetente, garantindo que você não insira acidentalmente o endereço errado. O formulário de composição de e-mail será pré-preenchido com endereços usados nos últimos 6 meses para agilizar o processo. Confira as [melhores práticas de e-mail]({{site.baseurl}}/user_guide/channels/email/best_practices/) para saber mais.

## Atualizações na API or interface de programação do aplicativo (API) de detalhes da campanha {#updates-to-campaign-details-api}

O endpoint `/campaign/details` agora oferece informações sobre suas mensagens, permitindo que você obtenha campos de assunto, corpo HTML, endereço de remetente e resposta usando a API or interface de programação do aplicativo (API). Saiba mais sobre as [APIs da Braze]({{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api).

## Atualizações na modelagem Liquid {#updates-to-liquid-templating}

Adicionamos a capacidade de criar modelos de atributos de variantes em Canvas e Campaigns. No Canvas, agora você pode modelar tanto o ID da API or interface de programação do aplicativo (API) da variante quanto o nome da variante, e em Campaigns você pode modelar o `message_api_id` e o `message_name` de uma mensagem. Ambas as atualizações permitem mais flexibilidade no seu envio de mensagens, possibilitando a criação de campanhas personalizadas. Saiba mais sobre [envio de mensagens personalizado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/).

## Novo editor de e-mail em HTML {#new-html-email-editor}

Agora você pode escrever e testar e-mails facilmente com um editor de HTML em tela cheia que permite pré-visualização ao vivo, personalização via Liquid e um editor de texto em tela cheia aprimorado com números de linha e realce de sintaxe. Saiba mais sobre a [composição de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template).

## Atualizações nas pré-visualizações {#updates-to-previews}

Agora você pode acompanhar a janela da tela enquanto rola as pré-visualizações de mensagens em Campaigns e Canvas, garantindo que você sempre possa ver as mudanças refletidas. Saiba mais sobre [pré-visualização e teste]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#step-6-preview-message).

## Novo filtro de associação de Segment or segmento {#new-segment-membership-filter}

Adicionamos o filtro [Segment Membership]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#targeting-filters), permitindo que você direcione usuários com base na associação deles em qualquer um dos seus Segments existentes. Além disso, adicionamos a capacidade de usar tanto a lógica "E" quanto a lógica "Ou" nos filtros de Segment or segmento, bem como a capacidade de aninhar segmentos uns dentro dos outros. Essas atualizações permitem que você envie mensagens personalizadas para seus clientes com mais precisão.

## Atualização na pré-visualização do Android {#update-to-android-preview}

Atualizamos a [pré-visualização do Android]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#step-5-preview-message) para refletir versões mais recentes do Android desde o Android N.