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

> Quando o rastreamento de análise de dados está ativado para um segmento, você pode visualizar sessões, eventos personalizados e receita ao longo do tempo para esse segmento.

Se você não ativar o rastreamento de análise de dados para um segmento, ainda poderá acessar [estatísticas em tempo real]({{site.baseurl}}/user_guide/audience/segments/segment_data#segment-statistics) para esse segmento e direcionar seus usuários com Campaigns. A única diferença é se você pode acessar as ferramentas de análise específicas mencionadas nesta página.

## Ativando a análise de dados do Segment {#turning-on-segment-analytics}

Na seção **Detalhes do Segment** da página de um Segment, ative o **Rastreamento de análise de dados**.

![Alternância de rastreamento de análise de dados para um Segment]({% image_buster /assets/img_archive/A_Tracking_2.png %})

Um espaço de trabalho pode ter o rastreamento ativado para até 25 Segments. A Braze recomenda rastrear Segments que são importantes para você analisar ao entender os efeitos das suas Campaigns em sessões, receita e compras.

{% alert note %}
Após ativar o rastreamento de análise de dados, espere uma postergação antes que os dados do Segment sejam preenchidos nos seus relatórios. Se os dados não forem preenchidos em 24 horas, [entre em contato com o Suporte]({{site.baseurl}}/braze_support).
{% endalert %}

## Visualizando receita e compras ao longo do tempo {#viewing-revenue-and-purchases-over-time}

Acesse **Analytics** > **Revenue Report** para visualizar dados sobre [receita e compras ao longo do tempo para esse segment]({{site.baseurl}}/user_guide/analytics/reports/revenue_report).

Os gráficos de receita e compras refletem a atividade registrada após o rastreamento de análise de dados ser ativado para esse segment. Ativar o rastreamento não preenche retroativamente compras anteriores nesses relatórios. Ao comparar segments, use apenas intervalos de tempo em que o rastreamento estava ativado para cada segment selecionado.

![Dados de receita por segment]({% image_buster /assets/img_archive/Revenue.png %})

Para comparar visualmente os dados de segments em qualquer intervalo de tempo personalizado, adicione ou remova segments do gráfico. Selecione **By Segment** no menu suspenso **Breakdown** e, em seguida, selecione seus segments em **Breakdown values**.

Selecione qualquer nome de segment na legenda do gráfico para ativar ou desativar a visibilidade das métricas desse segment.

![Receita para múltiplos segments]({% image_buster /assets/img_archive/segment_revenue_multiple.png %})

## Sessões ao longo do tempo {#sessions-over-time}

Da mesma forma, você pode encontrar dados sobre [sessões ao longo do tempo para esse Segment específico]({{site.baseurl}}/user_guide/analytics/dashboards/home) na página **Home**.

![Dados de sessão por segmento]({% image_buster /assets/img_archive/events_over_time2.png %})

## Visualizar eventos personalizados ao longo do tempo {#view-custom-events-over-time}

Visualize dados sobre [Eventos personalizados ao longo do tempo para Segments]({{site.baseurl}}/user_guide/data/activation/events/custom_events#analytics) acessando **Analytics** > **Relatório de eventos personalizados**.

## Usando modelos do Query Builder {#using-query-builder-templates}

Quando o rastreamento de análise de dados está ativado, você pode usar modelos de relatório do Query Builder para detalhar métricas de performance para Campaigns, Canvas, variantes e etapas por Segments. Para saber mais, confira [Dados de Segment]({{site.baseurl}}/user_guide/audience/segments/segment_data#viewing-performance-data-by-segment).

## Perguntas frequentes {#frequently-asked-questions}

### O que devo verificar se o rastreamento de análise de dados parece incorreto ou vazio? {#what-should-i-check-if-analytics-tracking-looks-wrong-or-empty}

Confirme se o **Analytics Tracking** ainda está ativado em **Segment Details**, se você não excedeu o limite por espaço de trabalho (25 segments com rastreamento) e aguarde até 24 horas para que os dados sejam preenchidos após ativar o rastreamento pela primeira vez. Se os problemas persistirem, verifique a definição do segment e o intervalo de datas do relatório e, em seguida, [entre em contato com o Suporte]({{site.baseurl}}/braze_support).