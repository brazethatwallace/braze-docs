---
nav_title: Rastreamento de análise de dados por segmento
article_title: Rastreamento de análise de dados por segmento
page_order: 3
page_type: reference
description: "Este artigo de referência aborda o rastreamento de análise de dados por segmento e como visualizar receita e compras ao longo do tempo, sessões ao longo do tempo e eventos personalizados ao longo do tempo."
tool:
  - Segments
  - Reports
---

# Rastreamento de análise de dados por segmento {#segment-analytics-tracking}

> Quando o rastreamento de análise de dados está ativado para um **Segment**, você pode visualizar sessões, eventos personalizados e receita ao longo do tempo para esse **Segment**.

Se você não ativar o rastreamento de análise de dados para um **Segment**, ainda poderá acessar [estatísticas em tempo real]({{site.baseurl}}/user_guide/audience/segments/segment_data/#segment-statistics) para esse **Segment** e direcionar seus usuários com **Campaigns**. A única diferença é se você pode acessar as ferramentas de análise específicas mencionadas nesta página.

## Ativação da análise de dados do segmento {#turning-on-segment-analytics}

Na seção **Segment Details** da página de um **Segment**, ative **Analytics Tracking**.

![Alternância de rastreamento de análise de dados para um segmento]({% image_buster /assets/img_archive/A_Tracking_2.png %})

Um app pode ter o rastreamento ativado para até 25 **Segments**. A Braze recomenda o rastreamento de **Segments** que são importantes para sua análise ao entender os efeitos das suas **Campaigns** sobre sessões, receita e compras.

## Visualização da receita e das compras ao longo do tempo {#viewing-revenue-and-purchases-over-time}

Acesse **Analytics** > **Revenue Report** para visualizar dados sobre [receita e compras ao longo do tempo para esse **Segment**]({{site.baseurl}}/user_guide/analytics/reports/revenue_report/).

![Dados de receita por segmento]({% image_buster /assets/img_archive/Revenue.png %})

Para comparar visualmente os dados do **Segment** em qualquer intervalo de tempo personalizado, adicione ou remova **Segments** do gráfico. Selecione **By Segment** no menu suspenso **Breakdown** e, em seguida, selecione seus **Segments** em **Breakdown values**.

Selecione qualquer nome de **Segment** acima do gráfico para ativar ou desativar a visibilidade das métricas desse **Segment**.

![Receita para vários segmentos]({% image_buster /assets/img_archive/segment_revenue_multiple.png %})

## Sessões ao longo do tempo {#sessions-over-time}

Da mesma forma, você pode encontrar dados sobre [sessões ao longo do tempo para esse **Segment** específico]({{site.baseurl}}/user_guide/analytics/dashboards/home/#exporting-app-usage-data) na página **Home**.

![Dados de sessão por segmento]({% image_buster /assets/img_archive/events_over_time2.png %})

## Visualizar eventos personalizados ao longo do tempo {#view-custom-events-over-time}

Visualize dados sobre [eventos personalizados ao longo do tempo para **Segments**]({{site.baseurl}}/user_guide/data/activation/events/custom_events/#analytics) acessando **Analytics** > **Custom events report**.

## Uso de modelos do Criador de consultas {#using-query-builder-templates}

Quando o rastreamento de análise de dados está ativado, você pode usar os modelos de relatório do Criador de consultas para detalhar métricas de desempenho de **Campaigns**, **Canvas**, variantes e etapas por **Segments**. Para saber mais, confira [Dados do **Segment**]({{site.baseurl}}/user_guide/audience/segments/segment_data/#performance-data-by-segment).