---
nav_title: Grupos de inscrições
article_title: Endpoints de grupos de inscrições
page_order: 7
layout: dev_guide

#Required
description: "Esta landing page explica e lista os endpoints dos grupos de inscrições da Braze para e-mail e SMS."
page_type: landing
search_tag: Endpoint

guide_top_header: "Endpoints de grupos de inscrições"
guide_top_text: "Use as APIs REST de grupos de inscrições para gerenciar programaticamente os grupos de inscrições que você armazenou no dashboard da Braze, na página **Grupo de inscrições**. Isso se aplica a grupos de inscrições para SMS e e-mail.<br><br> Está procurando orientação sobre como criar grupos de inscrições? Confira nossos artigos sobre <a href='/docs/user_guide/message_building_by_channel/sms/sms_subscription_group'>grupos de inscrições para SMS</a> e <a href='/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions'>grupos de inscrições para e-mail</a>."

guide_featured_title: ""
guide_featured_list:
  - name: "GET: Listar o status do grupo de inscrições do usuário"
    link: /docs/api/endpoints/subscription_groups/get_list_user_subscription_group_status
    image: /assets/img/braze_icons/users-01.svg
  - name: "GET: Listar os grupos de inscrições do usuário"
    link: /docs/api/endpoints/subscription_groups/get_list_user_subscription_groups
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: Atualizar o status do grupo de inscrições do usuário"
    link: /docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status
    image: /assets/img/braze_icons/user-plus-01.svg
  - name: "POST: Atualizar o status do grupo de inscrições do usuário V2"
    link: /docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2
    image: /assets/img/braze_icons/user-edit.svg
---
<br>
<br>


## Entendendo as séries temporais de grupos de inscrições {#understand-subscription-group-timeseries}

Na página **Grupo de inscrições**, os gráficos de séries temporais exibem:

- **Tamanho do grupo de inscrições:** usuários inscritos naquele grupo em uma determinada data
- **Tamanho de cancelamentos do grupo de inscrições:** usuários que cancelaram a inscrição daquele grupo em uma determinada data

Para orientações sobre o dashboard, consulte [Visualizando tamanhos de grupos de inscrições]({{site.baseurl}}/user_guide/channels/email/subscriptions#viewing-subscription-group-sizes).

Essas métricas são específicas de cada grupo. Elas podem diferir do filtro de segmento `Email Subscription Status is Unsubscribed`, que reflete o estado global de inscrição de e-mail em vez de um único grupo de inscrições. Para espaços de trabalho muito grandes, a Braze pode exibir contagens estimadas quando contagens exatas não estão disponíveis.

## Evitar usuários duplicados em formulários de captura de e-mail {#avoid-duplicate-users-from-email-capture-forms}

Antes de criar um usuário a partir de um formulário de captura de e-mail, chame [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) para verificar se o perfil já existe. Se a resposta for "User not found", crie o usuário com [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status). Caso contrário, atualize o perfil existente em vez de criar um duplicado.

## Eventos `USERS_MESSAGES_EMAIL_UNSUBSCRIBE` no Snowflake {#snowflake-users_messages_email_unsubscribe-events}

A tabela `USERS_MESSAGES_EMAIL_UNSUBSCRIBE` do Snowflake registra cancelamentos de inscrição de e-mail no nível da mensagem originados do lado do destinatário — clique em um link de cancelamento de inscrição, o List-Unsubscribe de um clique do cliente de e-mail, envios pela Central de Preferências e cancelamentos de inscrição reportados pelo ESP. Cancelamentos de inscrição feitos pela REST API não são incluídos nessa tabela; esses geram eventos [`users.behaviors.subscriptiongroup.StateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#subscription-group-state-change-events) ou [`users.behaviors.subscription.GlobalStateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#global-subscription-state-change-events).

## Mensagens de teste de SMS e grupos de inscrições {#sms-test-messages-and-subscription-groups}

Para receber uma mensagem de teste de SMS, o destinatário deve pertencer ao grupo de inscrições de SMS que você selecionar ao enviar o teste.