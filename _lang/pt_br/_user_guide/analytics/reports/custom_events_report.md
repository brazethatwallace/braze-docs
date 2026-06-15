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

Para visualizar esse relatório no dashboard, acesse **Analytics** > **Relatório de eventos personalizados**. Selecione os eventos personalizados que deseja analisar e selecione **Aplicar** para gerar o gráfico.

![Eventos personalizados]({% image_buster /assets/img_archive/Export_events.png %})

## Configurando seu relatório {#configuring-your-report}

Use as opções a seguir para personalizar quais dados aparecem no gráfico **Desempenho ao longo do tempo**.

| Opção | Descrição |
| --- | --- |
| Apps | Por padrão, o relatório inclui dados de todos os apps. Use esse menu suspenso para restringir o relatório a um app específico. |
| Agrupar eventos personalizados por | Controla como a série temporal do evento personalizado selecionado é agrupada. Por padrão, o gráfico mostra a tendência agregada geral por data. Alterne para **Eventos personalizados por hora** para ver padrões intradiários, ou **Eventos personalizados por MAU** para normalizar o volume de eventos em relação à contagem de usuários ativos mensais. |
| Filtrar por Segments | Ative essa opção para segmentar as contagens de eventos por um ou mais Segments. Quando ativado, selecione os Segments que deseja comparar. O gráfico mostra o número de usuários em cada segmento que realizaram o evento personalizado. |
| Fórmula de KPI | Substitui a contagem bruta de eventos por uma métrica calculada, composta por um numerador (como a contagem de um evento personalizado) e um denominador (como DAU, MAU ou o tamanho de um segmento com análise de dados ativada). Quando você seleciona uma ou mais fórmulas, o gráfico plota o valor de cada fórmula ao longo do período selecionado, permitindo comparar o desempenho normalizado (por exemplo, "eventos por usuário ativo") em vez do volume total de eventos. Se não houver dados disponíveis para o período e as fórmulas selecionadas, a Braze exibe uma mensagem de "sem dados" — amplie o período ou escolha fórmulas diferentes. Selecione **Gerenciar fórmulas de KPI** para criar ou editar fórmulas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configurando seu relatório" }

## Exportando dados {#exporting-data}

Para exportar os dados de eventos personalizados, selecione <i class="fas fa-bars" title="Menu de contexto do gráfico"></i> **Menu de contexto do gráfico** no gráfico **Desempenho ao longo do tempo** e selecione a opção de exportação desejada.

{% alert tip %}
Para ajuda com exportações de CSV e API, consulte [Solução de problemas de exportação]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting/).
{% endalert %}

## Solução de problemas {#troubleshooting}

### A segmentação por segmento não corresponde aos totais do espaço de trabalho {#segment-breakdown-doesnt-match-workspace-totals}

Quando você usa **Filtrar por Segments** ou restringe o relatório com o menu suspenso **Apps**, o gráfico conta os usuários no segmento (ou app) selecionado que realizaram o evento personalizado — e não todas as ocorrências do evento em todo o espaço de trabalho.

Se você comparar uma linha de segmento com uma visualização sem filtros (ou com **Todos os apps**), os totais frequentemente diferem porque:

- **Todos os apps** pode incluir usuários e eventos de todos os apps no espaço de trabalho.
- Um filtro de app único inclui apenas perfis vinculados a esse app.
- Filtros de segmento contam usuários que correspondem à definição do segmento no momento da consulta, o que pode excluir usuários que realizaram o evento fora dos critérios do segmento.

Para comparar de forma equivalente, use o mesmo filtro de app e a mesma seleção de segmento para cada série que você comparar, ou exporte os dados e reconcilie as contagens na sua ferramenta de análise de dados.