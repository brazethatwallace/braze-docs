---
nav_title: Central de Preferências
article_title: Central de Preferências
page_order: 8
layout: dev_guide
guide_top_header: "Central de Preferências"
guide_top_text: "Uma Central de Preferências de e-mail permite que os usuários gerenciem suas preferências de notificação para Campaigns de e-mail e newsletters a partir de uma página personalizada no seu app ou website. Use estes artigos para criar e gerenciar uma Central de Preferências com a <a href='/docs/API or interface de programação do aplicativo (API)/endpoints/preference_center'>API or interface de programação do aplicativo (API) da Central de Preferências da Braze</a> ou com o editor de arrastar e soltar, incluindo grupos de inscrições, estados de aceitação e personalização de páginas hospedadas."
description: "Esta landing page inclui artigos sobre a Central de Preferências de e-mail da Braze e como usar a API or interface de programação do aplicativo (API) da Central de Preferências."
channel:
  - email

guide_featured_title: "Artigos da seção"
guide_featured_list:
- name: Central de Preferências de e-mail via API
  link: /docs/user_guide/audience/subscription_preferences/preference_center/api_preference_center
  image: /assets/img/braze_icons/list.svg
- name: Central de Preferências de e-mail com arrastar e soltar
  link: /docs/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center
  image: /assets/img/braze_icons/mail-01.svg

---

{% multi_lang_include alerts/tip_alerts.md alert="Landing pages manage subscriptions" %}

## Perguntas frequentes {#frequently-asked-questions}

### O que é uma Central de Preferências de e-mail? {#what-is-an-email-preference-center}

Uma Central de Preferências de e-mail é uma página hospedada em que os usuários atualizam o status de inscrição de e-mail e escolhem categorias de mensagens. A Braze oferece suporte a Centrais de Preferências criadas via API or interface de programação do aplicativo (API) e com o editor de arrastar e soltar.

### Devo usar a API or interface de programação do aplicativo (API) da Central de Preferências ou o editor de arrastar e soltar? {#should-i-use-the-preference-center-api-or-the-drag-and-drop-editor}

Use a [Central de Preferências de e-mail com arrastar e soltar]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center) para uma configuração mais rápida e com menos código. Use a [Central de Preferências de e-mail via API or interface de programação do aplicativo (API)]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/api_preference_center) quando você precisar de controle total sobre o layout, a hospedagem e a lógica personalizada.