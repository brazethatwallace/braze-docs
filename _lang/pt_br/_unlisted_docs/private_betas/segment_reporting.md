---
nav_title: Relatórios por Segment
article_title: Relatórios por Segment no Report Builder
permalink: /segment_reporting_report_builder/
description: "Este artigo de referência aborda o uso de Segments como dimensão de relatório no Report Builder, incluindo como gerar relatórios por Segments, detalhar por Segment e quais combinações são compatíveis."
hidden: true
noindex: true
page_type: reference
---

# Relatórios por Segment no Report Builder {#segment-reporting-in-report-builder}

> Este artigo explica como usar Segments como dimensão de relatório no Report Builder, incluindo como gerar relatórios por Segments, detalhar por Segment e quais combinações são compatíveis.

{% multi_lang_include alerts/early_access_beta_alert.md feature='Segment reporting' contact='customer success manager' %}

O Report Builder oferece suporte a **Segments** em linhas e como opção de detalhamento, para que você possa ver o desempenho dos seus Segments e detalhar o desempenho de Campaigns ou Canvas por associação a Segments. Se **Segments** não aparecer nos menus suspensos **Rows** ou **Drilldown**, esse recurso ainda não foi ativado para a sua conta.

Você pode responder a perguntas como:

- Como um Segment específico está se saindo ao longo do tempo?
- Quais Campaigns e Canvas estão direcionados a um determinado Segment, e qual foi o desempenho de cada um?
- Como o engajamento se compara entre Segments para uma única Campaign ou Canvas?

{% alert note %}
Os relatórios por Segment estão disponíveis apenas para Segments com [rastreamento de análise de dados]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking) ativado. Para selecionar **Segments** no menu suspenso **Rows**, você precisa da [permissão "View Dashboard Reports"]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) no nível do espaço de trabalho.
{% endalert %}

## Gerar relatórios por Segments {#report-on-segments}

Para gerar relatórios diretamente por Segments:

1. Acesse **Analytics** > **Report Builder (New)**.
2. Clique em **Create New Report**.
3. No menu suspenso **Rows**, selecione **Segments**.
4. (Opcional) Selecione **Add drilldown** para detalhar ainda mais os dados do Segment:
   - **Campaigns and Canvases:** veja quais Campaigns e Canvas foram direcionados ao Segment e qual foi o desempenho de cada um.
   - **Date:** veja como o tamanho ou o desempenho de um Segment evolui ao longo do tempo. Combine com um gráfico de linhas para visualizar a tendência.
5. Em **Report content**, abra o menu suspenso **Segments** e selecione os Segments que deseja adicionar ao relatório.
6. Selecione as métricas em **Columns** > **Customize Metrics** e defina o intervalo de datas em **Report content**.
7. Se você adicionou um detalhamento por **Campaigns and Canvases**, adicione as Campaigns e Canvas que deseja incluir no relatório.
8. Clique em **Save and run**.

Para ver o fluxo completo do Report Builder, consulte [Criando um relatório]({{site.baseurl}}/user_guide/analytics/reports/report_builder#creating-a-report).

## Detalhar por Segment {#drill-down-by-segment}

Para detalhar relatórios de Campaigns, Canvas ou canais por Segment:

1. No menu suspenso **Rows**, selecione **Campaigns**, **Canvases** ou **Campaigns and Canvases**.
2. Selecione **Add drilldown** e escolha **Segment**.
3. Em **Report content**, abra o menu suspenso **Segments** e selecione os Segments que deseja adicionar ao relatório.
4. Selecione as métricas em **Columns** > **Customize Metrics** e defina o intervalo de datas em **Report content**.
5. Adicione as Campaigns ou Canvas que deseja incluir no relatório.
6. Clique em **Save and run** para ver o desempenho detalhado por cada Segment ao qual suas Campaigns ou Canvas foram direcionados.

Isso é especialmente útil para espaços de trabalho que enviam a mesma Campaign ou Canvas para vários Segments. Você pode ver como cada Segment respondeu sem precisar cruzar manualmente a associação ao Segment com o desempenho da Campaign.

## Combinações compatíveis {#supported-combinations}

As seguintes combinações de **Rows** e **Drilldown** são compatíveis com relatórios por Segment:

| Rows | Drilldown |
| ----- | ----- |
| Segment | Campaigns and Canvases |
| Segment | Date |
| Campaign | Segment |
| Campaign | Variant |
| Canvas | Segment |
| Campaigns and Canvases | Segment |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Combinações compatíveis de linhas e detalhamento"}

{% alert note %}
O Report Builder suporta apenas um detalhamento por vez. Se você selecionar **Campaigns** no menu suspenso **Rows**, poderá detalhar por **Variant** ou **Segment**, mas não ambos no mesmo relatório.
{% endalert %}

## Disponibilidade de métricas {#metrics-availability}

Nem todas as métricas do Report Builder estão disponíveis quando você gera relatórios por Segments. As métricas que podem ser selecionadas também dependem de **Segments** estar em **Rows** ou **Drilldown** e de o relatório incluir uma dimensão de Campaign ou Canvas.

| Métrica | Disponibilidade |
| ----- | ----- |
| Métricas de canal e de envio de mensagens gerais | Disponíveis para combinações compatíveis de linhas e detalhamento. |
| Contagens de conversão (Conversões A–D) e nomes de eventos de conversão | Disponíveis quando as dimensões de Segment e Campaign ou Canvas aparecem juntas. Use **Segments** em linhas com um detalhamento por **Campaigns and Canvases**; ou use **Campaigns**, **Canvases** ou **Campaigns and Canvases** em linhas com um detalhamento por **Segment**. |
| Receita e taxa de conversão | Não disponíveis para relatórios com dimensão de Segment. |
| Receita de compras e contagem por Segment | Disponíveis apenas quando **Segments** está em linhas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Disponibilidade de métricas para relatórios por Segment"}

Para saber mais sobre como suas seleções de linhas e detalhamento afetam as métricas, consulte [Disponibilidade de métricas]({{site.baseurl}}/user_guide/analytics/reports/report_builder#metrics-availability) no Report Builder.