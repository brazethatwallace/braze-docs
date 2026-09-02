---
nav_title: "Configuração"
article_title: Configuração de push
page_order: 0
layout: dev_guide
guide_top_header: "Configuração de push"
guide_top_text: "Entenda o ciclo de vida do token por push e os estados de inscrição para garantir que suas notificações por push cheguem aos usuários certos."

page_type: landing
description: "Saiba mais sobre o ciclo de vida do token por push e os estados de inscrição para notificações por push na Braze."

guide_featured_title: "Artigos da seção"
guide_featured_list:
  - name: Ciclo de vida do token por push
    link: /docs/user_guide/channels/push/push_setup/push_token_lifecycle
    image: /assets/img/braze_icons/refresh-ccw-02.svg
  - name: Estados de inscrição de push
    link: /docs/user_guide/channels/push/push_setup/push_subscription_states
    image: /assets/img/braze_icons/users-01.svg
---

## Pré-requisitos {#prerequisites}

Antes de criar e enviar qualquer mensagem push usando a Braze, você precisa trabalhar com seus desenvolvedores para integrar o push ao seu website ou app. Para etapas detalhadas, consulte nossos guias de integração para cada plataforma:

- [iOS]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/push_notifications?sdktab=android)
- [Web]({{site.baseurl}}/developer_guide/push_notifications?sdktab=web)

## Push priming {#push-priming}

Lembre-se de que os usuários precisam fazer a aceitação de push para receber suas mensagens, o que significa que é uma boa ideia usar In-App Messages para explicar aos seus clientes por que você deseja enviar notificações por push e como a ativação de push será benéfica para eles. Esse processo é chamado de [push priming]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages).