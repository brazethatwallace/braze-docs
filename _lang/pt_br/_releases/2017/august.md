---
nav_title: Agosto
page_order: 5
noindex: true
page_type: update
description: "Este artigo contém notas de versão de agosto de 2017."
---

# Agosto de 2017 {#august-2017}

## Atualização dos botões de ação por push {#update-to-push-action-buttons}

Adicionamos suporte a [botões de ação por push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_action_buttons/#how-to-use-action-buttons) aos nossos endpoints de envio de mensagens da REST or transferir estado representacional API or interface de programação do aplicativo (API).

## Atualização do modelo Liquid {#update-to-liquid-templating}

Agora você pode [personalizar uma mensagem]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/) com base em:
- O dispositivo para o qual foi enviada,
- ID do dispositivo,
- Operadora,
- IDFA,
- Modelo,
- SO e
- Plataforma

## Canvas disparado por API or interface de programação do aplicativo (API) {#api-triggered-canvas}

Agora é possível disparar um [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/) por meio de endpoints da API or interface de programação do aplicativo (API) (enviar, programar, atualizar, excluir) que correspondem aos existentes para Campaigns, o que permite automatizar e otimizar ainda mais o seu marketing.

## Botões de ação por push na web {#web-push-action-buttons}

Adicionamos suporte para botões de ação por push no SDK or kit de desenvolvimento de software da web para o Chrome, o que permite aumentar o engajamento oferecendo aos usuários opções contextuais que simplificam suas vidas ocupadas. Confira as [práticas recomendadas para notificações por push]({{site.baseurl}}/user_guide/channels/push/best_practices/).

## Novos endpoints da API or interface de programação do aplicativo (API) {#new-api-endpoints}

Disponibilizamos novos endpoints da API or interface de programação do aplicativo (API): /email/hard_bounces, que permite extrair hard bounces por endereço de e-mail ou em um determinado intervalo de datas, e /messages/scheduled_broadcasts, que permite consultar o próximo horário de início das Campaigns agendadas e dos Canvas de entrada agendada. Esses novos endpoints permitem a personalização e a otimização adicionais das suas Campaigns. Saiba mais sobre nossos [endpoints da API or interface de programação do aplicativo (API)]({{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api).

## Geofences

Adicionamos um novo recurso, geofences, que permite disparar mensagens em tempo real quando os clientes entram e saem de áreas geográficas definidas, possibilitando uma comunicação personalizada e relevante com seus clientes. Saiba mais sobre [marketing de localização]({{site.baseurl}}/developer_guide/geofences/?sdktab=android).

## Atualização do editor de e-mail {#update-to-email-editor}

Adicionamos o preenchimento automático dinâmico ao nosso novo editor de e-mail, de modo que agora é possível preencher automaticamente os atributos e eventos personalizados reais dos seus clientes ao usar o Liquid, facilitando sua vida. Saiba mais sobre as [práticas recomendadas de e-mail]({{site.baseurl}}/user_guide/channels/email/best_practices/).

## Atualização dos filtros de data {#update-to-date-filters}

Adicionamos um filtro de data "nunca" para que você possa direcionar os clientes que nunca receberam ou interagiram com uma de suas mensagens, permitindo manter listas de clientes limpas e garantir a entregabilidade dos e-mails. Saiba mais sobre [filtros]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#segmentation-filters).

## Atualização do Canvas {#update-to-canvas}

Adicionamos porcentagens à parte superior de cada variante do Canvas para que você possa ver rapidamente quais variantes têm melhor desempenho. Saiba mais sobre o [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/).

## Canvas com Seleção Inteligente {#canvas-with-intelligent-selection}

O Canvas agora conta com Seleção Inteligente, permitindo que você teste seus Canvas com mais eficiência. Saiba mais sobre nosso [Intelligence Suite]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/).

## Atualização dos nomes de exibição de e-mail {#update-to-email-display-names}

Adicionamos suporte a caracteres UTF-8 especiais em nomes de exibição de e-mail, para que você possa criar e-mails ainda mais personalizados para seus clientes. Saiba mais sobre as [práticas recomendadas de e-mail]({{site.baseurl}}/user_guide/channels/email/best_practices/).

## Agregação de CSV de relatórios de engajamento {#engagement-reports-csv-aggregation}

Agora é possível receber dados consolidados de cada Campaign e de cada Canvas em dois arquivos separados, independentemente do número de Campaigns ou Canvas selecionados, permitindo que você tenha todos os dados de que precisa, quando precisar. Saiba mais sobre os [relatórios de engajamento]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports/).

> Conforme observado em nossas [notas de versão de setembro de 2017]({{site.baseurl}}/releases/2017/september/), agora é possível agregar dados de um período específico, bem como agendar exportações para serem executadas de forma recorrente.