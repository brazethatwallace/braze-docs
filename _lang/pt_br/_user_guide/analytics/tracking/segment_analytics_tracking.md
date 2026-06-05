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

Se você não ativar o rastreamento de análise de dados para um segmento, ainda poderá acessar [estatísticas em tempo real]({{site.baseurl}}/user_guide/audience/segments/segment_data/#segment-statistics) para esse segmento e direcionar seus usuários com Campaigns. A única diferença é se você pode acessar as ferramentas de análise específicas mencionadas nesta página.

## Ativação da análise de dados do segmento {#turning-on-segment-analytics}

Na seção **Segment Details** da página de um segmento, ative **Analytics Tracking**.

![Alternância de rastreamento de análise de dados para um segmento]({% image_buster /assets/img_archive/A_Tracking_2.png %})

Um app pode ter o rastreamento ativado para até 25 segmentos. A Braze recomenda o rastreamento de segmentos que são importantes para sua análise ao entender os efeitos das suas Campaigns sobre sessões, receita e compras.

{% alert note %}
Após ativar o rastreamento de análise de dados, pode haver um atraso até que os dados do segmento sejam preenchidos. Se os dados não forem preenchidos em 24 horas, [fale com o Suporte]({{site.baseurl}}/braze_support/).
{% endalert %}

## Visualização da receita e das compras ao longo do tempo {#viewing-revenue-and-purchases-over-time}

Acesse **Analytics** > **Revenue Report** para visualizar dados sobre [receita e compras ao longo do tempo para esse segmento]({{site.baseurl}}/user_guide/analytics/reports/revenue_report/).

Os gráficos de receita e compras refletem a atividade registrada após a ativação do rastreamento de análise de dados para esse segmento. Ativar o rastreamento não preenche retroativamente compras anteriores nesses relatórios. Ao comparar segmentos, use apenas intervalos de tempo em que o rastreamento estava ativado para cada segmento selecionado.

![Dados de receita por segmento]({% image_buster /assets/img_archive/Revenue.png %})

Para comparar visualmente os dados do segmento em qualquer intervalo de tempo personalizado, adicione ou remova segmentos do gráfico. Selecione **By Segment** no menu suspenso **Breakdown** e, em seguida, selecione seus segmentos em **Breakdown values**.

Selecione qualquer nome de segmento acima do gráfico para ativar ou desativar a visibilidade das métricas desse segmento.

![Receita para vários segmentos]({% image_buster /assets/img_archive/segment_revenue_multiple.png %})

## Sessões ao longo do tempo {#sessions-over-time}

Da mesma forma, você pode encontrar dados sobre [sessões ao longo do tempo para esse segmento específico]({{site.baseurl}}/user_guide/analytics/dashboards/home/#exporting-app-usage-data) na página **Home**.

![Dados de sessão por segmento]({% image_buster /assets/img_archive/events_over_time2.png %})

## Visualizar eventos personalizados ao longo do tempo {#view-custom-events-over-time}

Visualize dados sobre [eventos personalizados ao longo do tempo para segmentos]({{site.baseurl}}/user_guide/data/activation/events/custom_events/#analytics) acessando **Analytics** > **Custom events report**.

## Uso de modelos do Criador de consultas {#using-query-builder-templates}

Quando o rastreamento de análise de dados está ativado, você pode usar os modelos de relatório do Criador de consultas para detalhar métricas de desempenho de Campaigns, Canvas, variantes e etapas por segmentos. Para saber mais, confira [Dados do segmento]({{site.baseurl}}/user_guide/audience/segments/segment_data/#performance-data-by-segment).

## Perguntas frequentes {#frequently-asked-questions}

### O que devo verificar se o rastreamento de análise de dados parece incorreto ou vazio? {#what-should-i-check-if-analytics-tracking-looks-wrong-or-empty}

Confirme se **Analytics Tracking** ainda está ativado em **Segment Details**, se você não excedeu o limite por app (25 segmentos com rastreamento) e aguarde até 24 horas para que os dados sejam preenchidos após a primeira ativação do rastreamento. Se os problemas persistirem, verifique a definição do segmento e o intervalo de datas do relatório e, em seguida, [fale com o Suporte]({{site.baseurl}}/braze_support/).