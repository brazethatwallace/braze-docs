---
page_order: 0
nav_title: Início
article_title: Parceiros de tecnologia
alias: /partners/partners/
layout: dev_guide
search_tag: Partner
description: "Explore os parceiros de tecnologia da Braze (Alloys) por categoria. Encontre documentação de integração para personalização, orquestração, dados, eCommerce, Audience Sync e muito mais."

guide_top_header: "Parceiros de tecnologia"
guide_top_text: "Bem-vindo à documentação de parceiros de tecnologia Braze Alloys. Navegue pelas categorias de parceiros para encontrar guias de integração técnica.<br><br>Para uma lista completa e filtrável de todos os parceiros de tecnologia da Braze, visite o <a href='https://marketplace.braze.com/t/type/technology-partner'>Braze Marketplace</a>. Quer participar da nossa comunidade de clientes que usam a Braze para modernizar a experiência do cliente? Confira nosso <a href='https://brazefirebrands.splashthat.com/'>Programa Customer Champions</a>."

guide_featured_title: "Categorias de parceiros"
guide_featured_list:
  - name: Personalização de mensagens
    link: /docs/partners/message_personalization
    image: /assets/img/braze_icons/magic-wand-02.svg
  - name: Orquestração de mensagens
    link: /docs/partners/message_orchestration
    image: /assets/img/braze_icons/send-01.svg
  - name: Dados e análise de dados
    link: /docs/partners/data_and_analytics
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: Canvas Audience Sync
    link: /docs/partners/canvas_audience_sync
    image: /assets/img/braze_icons/refresh-ccw-02.svg
  - name: eCommerce
    link: /docs/partners/ecommerce
    image: /assets/img/braze_icons/shopping-cart-03.svg
  - name: Canais adicionais e extensões
    link: /docs/partners/additional_channels_and_extensions
    image: /assets/img/braze_icons/puzzle-piece-01.svg
  - name: Provedores de modelos de IA
    link: /docs/partners/ai_model_providers
    image: /assets/img/braze_icons/stars-01.svg
---

## Solução de problemas de conexões com parceiros {#troubleshooting-partner-connections}

Se a integração exigir configuração no lado da Braze, faça login no dashboard da Braze e navegue até **Integrações de parceiros** > **Parceiros de tecnologia**.

{% alert note %}
Integrações totalmente gerenciadas pelo parceiro podem não estar listadas aqui. Consulte a documentação específica do parceiro para verificar a propriedade da integração e as etapas de configuração.
{% endalert %}

Se você vir **Credenciais inválidas** para um parceiro na Braze, mas a integração parecer correta no dashboard desse parceiro, desconecte e reconecte a integração na página de parceiros de tecnologia e confirme as chaves de API, tokens OAuth e permissões no lado do parceiro.

Alguns dashboards externos (por exemplo, ferramentas de entregabilidade ou monitoramento de caixa de entrada) podem mostrar um status de conexão ou verificação diferente da página de parceiros de tecnologia da Braze. Use o bloco do parceiro na Braze para verificar o estado de conexão que a Braze utiliza para sincronização e envio.