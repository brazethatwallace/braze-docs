---
nav_title: Dashboard de receita de eCommerce
article_title: Dashboard de receita de eCommerce
alias: "/ecommerce_revenue_dashboard/"
page_order: 1
description: "Este artigo fornece uma visão geral do dashboard de receita de eCommerce com atribuição de último ponto de contato."
---

# Dashboard de receita de eCommerce {#ecommerce-revenue-dashboard}

> O dashboard **eCommerce Revenue - Last Touch Attribution** rastreia a receita atribuída ao último ponto de contato para Campaigns e Canvas usando [eventos recomendados de eCommerce]({{site.baseurl}}/ecommerce_events). Use esse dashboard para entender quais mensagens geram receita e para monitorar o desempenho geral do eCommerce ao longo do tempo.

{% alert note %}
Se você está usando o novo [conector do Shopify]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores?tab=shopify%20connector), os eventos recomendados de eCommerce estarão disponíveis automaticamente por meio da integração. Caso contrário, esses eventos precisam ser implementados antes que os dados apareçam nesse dashboard.
{% endalert %}

Para visualizar o dashboard de receita de eCommerce, acesse **Analytics** > **Criador de dashboard** e selecione **eCommerce Revenue - Last Touch Attribution**. Esse dashboard reporta a receita atribuída à última Campaign ou Canvas com a qual o usuário interagiu antes de fazer um pedido, dentro da janela de conversão selecionada.

![Dashboard eCommerce Revenue - Last Touch Attribution mostrando estatísticas de receita de eCommerce, pedidos diários realizados e receita média diária de eCommerce, além de um gráfico de receita de eCommerce ao longo do tempo.]({% image_buster /assets/img/ecommerce/ecommerce_revenue_dashboard.png %})

## Métricas disponíveis {#available-metrics}

| Métrica | Definição |
| --- | --- |
| Receita de eCommerce | Receita total atribuída ao último ponto de contato com base no período e na janela de conversão selecionados. |
| Pedidos diários realizados | O número médio de pedidos distintos realizados por dia. |
| Receita média diária de eCommerce | Receita média atribuída por dia para o período selecionado. |
| Receita de eCommerce ao longo do tempo | Série temporal da receita atribuída no período selecionado. |
| Receita de eCommerce por Campaign | Receita atribuída detalhada por Campaign. |
| Receita de eCommerce por Canvas | Receita atribuída detalhada por Canvas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métricas disponíveis" }

![Gráficos de receita de eCommerce por Campaign e receita de eCommerce por Canvas.]({% image_buster /assets/img/ecommerce/ecommerce_revenue_charts.png %})

## Modelo de atribuição {#attribution-model}

O dashboard **eCommerce Revenue - Last Touch Attribution** usa a atribuição de último ponto de contato. Isso significa que a receita é atribuída à Campaign ou Canvas da Braze mais recente com a qual o usuário interagiu antes de fazer um pedido.

As seguintes interações com mensagens são consideradas eventos de contato para atribuição:

- Clique em e-mail
- Abertura de push
- Clique em cartão de conteúdo
- Clique em mensagem no app
- Clique em link curto de SMS
- Clique em link curto de WhatsApp

{% alert important %}
As interações com mensagens devem ter ocorrido dentro da janela de conversão selecionada. Pedidos sem uma interação elegível com mensagem dentro da janela de conversão não são atribuídos.
{% endalert %}

## Dados incluídos {#included-data}

O dashboard **eCommerce Revenue - Last Touch Attribution** utiliza dados dos eventos recomendados de eCommerce:

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_refunded`
- `ecommerce.order_cancelled`

{% alert note %}
Para que os dados sejam preenchidos no dashboard **eCommerce Revenue - Last Touch Attribution**, os campos `total_value`, `product.price` e `product.quantity` do evento `ecommerce.order_placed` devem ser `0` ou superior.
{% endalert %}

A receita e a contagem de pedidos usam cálculos padronizados da Braze.

| Métrica | Cálculo |
| --- | --- |
| Receita total | Soma dos valores de pedidos realizados − Soma dos valores reembolsados |
| Total de pedidos | Pedidos distintos realizados − Pedidos distintos cancelados |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Dados incluídos" }

### Dados excluídos {#excluded-data}

Compras registradas usando o evento de compra legado não são incluídas. O dashboard **eCommerce Revenue - Last Touch Attribution** atualmente não oferece suporte a recursos vinculados a eventos de compra legados, como LTV ou relatório de receitas dentro de Campaigns ou Canvas.

## Tratamento de moedas {#currency-handling}

Toda a receita é exibida em USD. Moedas diferentes de USD são convertidas para USD usando a taxa de câmbio da data em que o evento foi reportado. Para evitar a conversão, defina a moeda como `USD` de forma fixa ao enviar os eventos.