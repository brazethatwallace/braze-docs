---
nav_title: Relatório de receitas
article_title: Relatório de receitas
page_order: 7
page_type: reference
description: "Esta página descreve onde encontrar o Relatório de receitas no dashboard da Braze e como visualizar dados de receita em períodos específicos, a receita de um produto específico e a receita total do seu app."
tool: Reports
---

# Relatório de receitas {#revenue-report}

> A página **Relatório de receitas** permite visualizar dados de receita em períodos específicos, a receita de um produto específico e a receita total do seu app.

Para visualizar o relatório de receitas no dashboard da Braze, acesse **Analytics** > **Reports** > **Revenue Report**.

## Personalizando seu relatório de receita {#customizing-your-revenue-report}

Você pode personalizar seu relatório de receita selecionando um intervalo de datas, os apps sobre os quais deseja gerar o relatório e os parâmetros.

![A página "Revenue Report" mostrando o gráfico "Performance Over Time" com "Revenue" definido como parâmetro.]({% image_buster /assets/img/revenue_report.png %})

### Filtrando por data e apps {#filtering-by-date-and-apps}

Selecione o intervalo de datas para seu relatório de receita e, se desejar, um app específico ou uma seleção de apps.

### Filtrando por parâmetros {#filtering-by-parameters}

O gráfico **Performance Over Time** mostra os dados para diferentes parâmetros, que podem ser selecionados no menu suspenso **Statistics for**. Opcionalmente, você pode detalhar os dados de determinados parâmetros no menu suspenso **Breakdown**.

Você pode visualizar os seguintes dados no **gráfico Performance Over Time**:
- Fórmulas de KPI
- Compras
    - (Opcional) Compras por produto
- Receita
    - (Opcional) Receita por Segment
    - (Opcional) Receita por produto
- Receita por hora
    - (Opcional) Receita por hora por Segment
- Receita por usuário

## Entendendo os cálculos de receita {#understanding-revenue-calculations}

{% alert note %}
Quando você registra receita em uma moeda sem taxa de câmbio, a Braze registra como uma compra de US $0,00.
{% endalert %}

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Entendendo os cálculos de receita">
  <caption>Entendendo os cálculos de receita</caption>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definição</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#lifetime-revenue">Receita vitalícia</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#lifetime-value-per-user">Valor vitalício por usuário</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#average-daily-revenue">Receita média diária</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#daily-purchases">Compras diárias</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#daily-revenue-per-user">Receita diária por usuário</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}</td>
        </tr>
    </tbody>
</table>

## Visualizando o detalhamento de produtos {#viewing-the-product-breakdown}

Consulte a tabela **Product Breakdown** para ver uma lista dos produtos comprados durante o período selecionado, quantas unidades de cada produto foram compradas e quanta receita cada produto gerou.

![A tabela "Product Breakdown" mostrando as colunas "Product Name", "Purchased" e "Revenue".]({% image_buster /assets/img/revenue_report_product_breakdown.png %})

## Exportando dados de receita {#exporting-revenue-data}

Para exportar seus dados de receita, selecione <i class="fas fa-bars" title="Menu de contexto do gráfico"></i> **Menu de contexto do gráfico** no gráfico **Desempenho ao longo do tempo** e selecione sua opção de exportação.

{% alert tip %}
Procurando mais formas de obter dados de receita? Tente adicionar comportamento de compra (assim como compra de um produto) a Campaigns ou Canvas como [eventos de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events).
{% endalert %}

Você também pode visualizar estatísticas de receita caso a caso nas páginas de [análise de Campaign]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics) ou [análise de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics).

{% alert tip %}
Relatórios de receita não podem ser exportados por API. Para ajuda com exportações em CSV, consulte [solução de problemas de exportação]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}