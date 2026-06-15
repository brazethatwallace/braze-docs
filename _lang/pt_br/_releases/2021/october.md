---
nav_title: Outubro
page_order: 2
noindex: true
page_type: update
description: "Este artigo contém notas de versão para outubro de 2021."
---

# Outubro de 2021 {#october-2021}

## Painel de uso de pontos de dados {#data-points-usage-dashboard}

Use o dashboard **Total de uso de pontos de dados** para acompanhar o ritmo de uso dos seus pontos de dados em relação à sua alocação contratual. Esse dashboard fornece informações sobre seu contrato, ciclo de faturamento atual, dados de faturamento da empresa e dados de faturamento do espaço de trabalho. Para saber mais, consulte [Faturamento]({{site.baseurl}}/user_guide/onboarding_with_braze/subscription_and_usage/#total-data-points-dashboard).

## Alteração na regeneração de extensões de segmento {#change-to-segment-extension-regeneration}

A partir de 1º de fevereiro de 2022, a configuração para regenerar extensões diariamente será desativada automaticamente para [extensões de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension/) não utilizadas. A Braze define extensões não utilizadas como aquelas que atendem aos seguintes critérios:

- Não utilizada em nenhuma Campaign, Canvas ou segmento ativo
- Não utilizada em nenhuma Campaign, Canvas ou segmento inativo (rascunho, interrompido ou arquivado)
- Sem modificação há mais de 7 dias

A Braze notificará o contato da empresa e quem criou a extensão quando essa configuração for desativada. A opção de regenerar extensões diariamente pode ser ativada novamente a qualquer momento.

## Guias avançados de implementação do Android {#android-advanced-implementation-guides}

### Content Cards

Este [guia de implementação]({{site.baseurl}}/developer_guide/content_cards/) opcional e avançado cobre considerações de código de Content Cards, três casos de uso personalizados criados por nossa equipe, trechos de código que o acompanham e orientações sobre o registro de impressões, cliques e dispensas.

### Mensagens no app {#in-app-messaging}

Este [guia de implementação]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android) opcional e avançado cobre considerações de código de mensagens no app, três casos de uso personalizados criados por nossa equipe e trechos de código que o acompanham.

### Notificações por push {#push-notifications}

Este [guia de implementação]({{site.baseurl}}/developer_guide/push_notifications/examples/?sdktab=android) opcional e avançado cobre maneiras de aproveitar uma subclasse personalizada de `FirebaseMessagingService` para obter o máximo de suas mensagens push. Inclui um caso de uso personalizado criado por nossa equipe, trechos de código de acompanhamento e orientações sobre o registro de análise de dados.

## Novas parcerias da Braze {#new-braze-partnerships}

### Adobe - Plataforma de dados do cliente {#adobe-customer-data-platform}

Construída na Adobe Experience Platform, a plataforma de dados do cliente em tempo real (real-time CDP) da Adobe ajuda as empresas a reunir dados conhecidos e anônimos de várias fontes empresariais para criar perfis de clientes que podem ser usados para fornecer experiências personalizadas aos clientes em todos os canais e dispositivos em tempo real.

A integração da Braze com o [Adobe]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/adobe/) CDP permite que as marcas conectem e mapeiem seus dados do Adobe (atributos personalizados e segmentos) para a Braze em tempo real. As marcas podem então agir com base nesses dados, oferecendo experiências personalizadas e direcionadas a esses usuários.

### Shopify - eCommerce

A [Shopify]({{site.baseurl}}/partners/shopify/) é uma empresa de comércio global líder que fornece ferramentas confiáveis para abrir, expandir, comercializar e gerenciar um negócio de varejo de qualquer tamanho. Juntas, a integração da Braze com a Shopify permite que as marcas conectem sua loja Shopify perfeitamente com a Braze para passar webhooks selecionados da Shopify para a Braze. Aproveite as estratégias cross-canal da Braze e o Canvas para redirecionar seus usuários com mensagens de checkout abandonado e incentivar os clientes a concluir sua compra, ou redirecionar os usuários com base em suas compras anteriores.