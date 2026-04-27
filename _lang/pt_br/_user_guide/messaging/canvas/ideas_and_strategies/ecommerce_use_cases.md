---
nav_title: Casos de uso de eCommerce
article_title: Casos de uso de eCommerce
alias: /ecommerce_use_cases/
page_order: 4
description: "Este artigo de referência aborda vários modelos pré-criados da Braze, desenvolvidos especificamente para profissionais de marketing de eCommerce, facilitando a implementação de estratégias essenciais."
toc_headers: h2
---

# Como usar eventos recomendados de eCommerce

> Esta página explica como e onde você pode usar eventos recomendados de eCommerce em toda a plataforma, incluindo como usar os modelos de Canvas para eCommerce da Braze.

{% alert important %}
Os [eventos recomendados de eCommerce]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events/) estão atualmente em acesso antecipado. Entre em contato com seu gerente de sucesso do cliente da Braze se tiver interesse em participar desse acesso antecipado. <br><br>Se você estiver usando o novo conector do Shopify, os eventos recomendados de eCommerce estarão disponíveis automaticamente por meio da integração.
{% endalert %}

## Usando um modelo de Canvas

Para usar um modelo de Canvas:
1. Acesse **Envio de mensagens** > **Canvas**.
2. Selecione **Criar Canvas** > **Usar um modelo de Canvas**.
3. Navegue pela guia **Modelos da Braze** para encontrar o modelo que deseja usar. Você pode pré-visualizar um modelo selecionando seu nome.
4. Selecione **Aplicar modelo** para o modelo que deseja usar.<br><br>![Página "Modelos de Canvas" aberta na guia "Modelos da Braze", mostrando uma lista de modelos usados recentemente e modelos da Braze selecionáveis.]({% image_buster /assets/img_archive/apply_template.png %}){: style="max-width:80%;"}

## Modelos de Canvas para eCommerce

A Braze oferece quatro modelos de Canvas para eCommerce.

{% multi_lang_include canvas/ecommerce_templates.md %}

## Personalização de mensagens

O [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/) é uma linguagem de modelagem poderosa usada pela Braze que permite criar conteúdo dinâmico e personalizado para seus clientes. Ao usar Liquid tags, você pode personalizar mensagens com base em dados do cliente, informações de produtos e outras variáveis, aprimorando a experiência de compra e impulsionando o engajamento.

### Principais recursos do Liquid

- **Conteúdo dinâmico:** insira informações específicas do cliente, como nomes, detalhes de pedidos e preferências, em suas mensagens.
- **Lógica condicional:** use instruções if/else para exibir conteúdos diferentes com base em condições específicas (como localização do cliente e histórico de compras).
- **Loops:** itere sobre coleções de produtos ou dados de clientes para exibir listas ou grades de itens.

### Primeiros passos com o Liquid

Para começar a personalizar suas mensagens usando Liquid tags, consulte os seguintes recursos:

- Referência de [dados do Shopify]({{site.baseurl}}/shopify_features/#shopify-data) com Liquid tags pré-definidas
- [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/)

## Segmentação

Use os segmentos da Braze para criar segmentos de clientes direcionados com base em atributos e comportamentos específicos, e entregue mensagens e campanhas personalizadas. Com esse recurso poderoso, você pode engajar seus clientes de forma eficaz, alcançando o público certo com a mensagem certa no momento certo.

Para saber mais sobre como começar com segmentos, confira [Sobre os segmentos da Braze]({{site.baseurl}}/user_guide/audience/segments#about-braze-segments).

### Eventos recomendados

Os eventos de eCommerce são baseados em [eventos recomendados]({{site.baseurl}}/recommended_events/).
Como os eventos recomendados são eventos personalizados mais específicos, você pode pesquisar os nomes dos eventos recomendados de eCommerce selecionando qualquer [filtro de evento personalizado]({{site.baseurl}}/user_guide/data/activation/events/custom_events#segmentation-filters).

### Filtros de eCommerce

Segmente seus usuários com filtros de eCommerce, como **Ecommerce Source** e **Total Revenue**, acessando a seção **eCommerce** dentro do segmentador.

Para ver uma lista de filtros de eCommerce e suas definições, consulte [Filtros de segmento]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/) e selecione a categoria de pesquisa "eCommerce".

![Menu suspenso de filtros de segmento com filtros "eCommerce".]({% image_buster /assets/img_archive/ecommerce_filters.png %}){: style="max-width:50%"}

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation for eCommerce filters' %}

## Propriedades de eventos aninhados

Para segmentar por propriedades de eventos aninhados, você pode usar as [Extensões de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension#why-use-segment-extensions). Por exemplo, você pode usar extensões de segmento para encontrar quem comprou o produto "SKU-123" nos últimos 90 dias.

## Análise de dados

### Relatório de eventos personalizados

Você pode acompanhar o volume de eventos recomendados de eCommerce no [Relatório de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events#analytics). Filtre por **Realizar evento personalizado** e especifique o [nome do evento recomendado de eCommerce]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events#types-of-ecommerce-recommended-events) para visualizar sua performance ao longo do tempo.

![Gráfico de eventos personalizados exibindo resultados para seis eventos selecionados.]({% image_buster /assets/img/ecommerce/custom_events_chart.png %})

### Dashboards

#### Dashboard de conversões

Depois de lançar uma campanha ou Canvas usando o evento de conversão "Places Order", você pode criar um [relatório de conversão]({{site.baseurl}}/user_guide/analytics/dashboards/conversions#setting-up-your-report) correspondente para acompanhar a performance.

![Tabela de detalhes de conversões com campanhas e Canvas, e as estatísticas de conversão associadas.]({% image_buster /assets/img_archive/conversion_details_table.png %})

#### Dashboard de receita de eCommerce

Para obter insights sobre a receita atribuída à última campanha ou Canvas com que um usuário interagiu antes de fazer um pedido, use o [dashboard de receita de eCommerce]({{site.baseurl}}/ecommerce_revenue_dashboard/) e selecione uma janela de conversão.

### Relatório de receitas

Para analisar dados desses novos eventos, acesse o [Criador de dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/) e visualize o [dashboard **eCommerce Revenue - Last Touch Attribution**]({{site.baseurl}}/ecommerce_revenue_dashboard/).