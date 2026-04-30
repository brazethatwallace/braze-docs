---
nav_title: Relatório de eventos personalizados
article_title: Relatório de eventos personalizados
page_order: 6
page_type: reference
description: "Esta página descreve como usar o relatório de eventos personalizados para visualizar ocorrências de eventos personalizados ao longo do tempo, segmentadas por segmento."
tool: Reports
---

# Relatório de eventos personalizados {#custom-events-report}

> O relatório de eventos personalizados permite visualizar as ocorrências de um ou mais eventos personalizados ao longo do tempo. Você pode segmentar os resultados por segmento, aplicar fórmulas de KPI e exportar os dados para análises adicionais.

## Visualizando um relatório {#viewing-a-report}

Para visualizar esse relatório no dashboard, acesse **Analytics** > **Relatório de eventos personalizados**. Selecione os eventos personalizados que deseja analisar e selecione **Apply** para gerar o gráfico.

![Eventos personalizados]({% image_buster /assets/img_archive/Export_events.png %})

## Configurando seu relatório {#configuring-your-report}

Use as opções a seguir para personalizar quais dados aparecem no gráfico **Performance Over Time**.

| Opção | Descrição |
| --- | --- |
| Apps | Por padrão, o relatório inclui dados de todos os apps. Use esse menu suspenso para restringir o relatório a um app específico. |
| Agrupar eventos personalizados por | Controla como a série temporal do evento personalizado selecionado é agrupada. Por padrão, o gráfico mostra a tendência agregada geral por data. Alterne para **Custom Events by Hour** para ver padrões intradiários, ou **Custom Events per MAU** para normalizar o volume de eventos em relação à contagem de usuários ativos mensais. |
| Filtrar por Segments | Ative essa opção para segmentar as contagens de eventos por um ou mais Segments. Quando ativado, selecione os Segments que deseja comparar. O gráfico mostra o número de usuários em cada segmento que realizaram o evento personalizado. |
| Fórmula de KPI | Substitui a contagem bruta de eventos por uma métrica calculada, composta por um numerador (como a contagem de um evento personalizado) e um denominador (como DAU, MAU ou o tamanho de um segmento com análise de dados ativada). Quando você seleciona uma ou mais fórmulas, o gráfico plota o valor de cada fórmula ao longo do período selecionado, permitindo comparar o desempenho normalizado (por exemplo, "eventos por usuário ativo") em vez do volume total de eventos. Se não houver dados disponíveis para o período e as fórmulas selecionadas, a Braze exibe uma mensagem de "sem dados" — amplie o período ou escolha fórmulas diferentes. Selecione **Manage KPI formulas** para criar ou editar fórmulas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Exportando dados {#exporting-data}

Para exportar os dados de eventos personalizados, selecione <i class="fas fa-bars" title="Menu de contexto do gráfico"></i> no gráfico **Performance Over Time** e selecione a opção de exportação desejada.

{% alert tip %}
Para ajuda com exportações de CSV e API, consulte [Solução de problemas de exportação]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting/).
{% endalert %}