---
nav_title: API de envio de mensagens do dispositivo
article_title: API de envio de mensagens do dispositivo
search_tag: Endpoint
page_order: 2.2
layout: dev_guide
permalink: /api/device_messaging_api
description: "Esta landing page apresenta a API de envio de mensagens do dispositivo da Braze."
page_type: landing
hidden: true
guide_top_header: "API de envio de mensagens do dispositivo"
guide_top_text: "Use a API de envio de mensagens do dispositivo da Braze para recuperar propriedades de Banner e reportar eventos de impressão e clique de Banner sem integrar um SDK da Braze. A API de envio de mensagens do dispositivo oferece suporte a integrações do lado do cliente e do lado do servidor e usa chaves da API REST do lado do cliente com escopo para um único espaço de trabalho."
guide_top_text2: "Nota: esta API recupera apenas as propriedades de um determinado Banner, e não o HTML do Banner."
guide_featured_title: "Primeiros passos"
guide_featured_list:
  - name: "Visão geral da API de envio de mensagens do dispositivo"
    link: /docs/api/device_messaging_api/overview
    image: /assets/img/braze_icons/annotation-info.svg
  - name: "Autenticação e segurança"
    link: /docs/api/device_messaging_api/authentication
    image: /assets/img/braze_icons/key-01.svg
  - name: "Tratamento de erros e novas tentativas"
    link: /docs/api/device_messaging_api/error_handling
    image: /assets/img/braze_icons/alert-circle.svg
  - name: "Limites de taxa"
    link: /docs/api/device_messaging_api/rate_limits
    image: /assets/img/braze_icons/speedometer-01.svg
guide_menu_title: "Endpoints de Banner"
guide_menu_list:
  - name: "POST: Recuperar Banners para um usuário"
    link: /docs/api/device_messaging_api/endpoints/banners/post_sync_banners
    image: /assets/img/braze_icons/download-01.svg
  - name: "POST: Rastrear eventos de análise de dados de Banner"
    link: /docs/api/device_messaging_api/endpoints/banners/post_track_banner_events
    image: /assets/img/braze_icons/line-chart-up-02.svg
---

{% alert important %}
Esta página está em beta. Os recursos e a documentação da API de envio de mensagens do dispositivo estão sujeitos a alterações.
{% endalert %}