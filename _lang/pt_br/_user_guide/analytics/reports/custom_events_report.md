---
nav_title: Relatório de eventos personalizados
article_title: Relatório de eventos personalizados
page_order: 6
page_type: reference
description: "Esta página descreve como usar o relatório de eventos personalizados para visualizar ocorrências de eventos personalizados ao longo do tempo, segmentadas por Segment."
tool: Reports
---

# Relatório de eventos personalizados {#custom-events-report}

> O relatório de eventos personalizados permite visualizar as ocorrências de um ou mais eventos personalizados ao longo do tempo. Você pode segmentar os resultados por Segment, aplicar fórmulas de KPI e exportar os dados para análises adicionais.

## Visualizar um relatório {#view-a-report}

Para visualizar este relatório no dashboard, acesse **Analytics** > **Custom Events Report**. Selecione os eventos personalizados que você deseja analisar. O gráfico é gerado automaticamente após a seleção de um evento.

![Eventos personalizados]({% image_buster /assets/img_archive/Export_events.png %})

### Eventos personalizados de API e filtros de app {#api-custom-events-and-app-filters}

Eventos personalizados enviados pelo endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) podem incluir opcionalmente o `app_id`. Diferentemente dos eventos registrados pelo SDK, os eventos de API não são automaticamente associados a um app. Sem o `app_id`, os eventos são registrados, mas não aparecem no gráfico de eventos personalizados quando um filtro de app é aplicado.

## Configure seu relatório {#configure-your-report}

Use as opções a seguir para personalizar quais dados aparecem no gráfico de eventos personalizados.

| Opção | Descrição |
| --- | --- |
| Apps | Por padrão, o relatório inclui dados de todos os apps. Use este menu suspenso para restringir o relatório a um app específico. |
| Agrupar eventos personalizados por | Controla como a série temporal do evento personalizado selecionado é agrupada. Por padrão, o gráfico mostra a tendência agregada geral por data. Alterne para **Custom Events by Hour** para ver padrões intradiários, ou **Custom Events per MAU** para normalizar o volume de eventos em relação à contagem de MAU. |
| Filtrar por Segments | Ative esta opção para dividir as contagens de eventos por um ou mais Segments. Quando ativado, selecione os Segments que você deseja comparar. O gráfico mostra o número de usuários em cada Segment que realizaram o evento personalizado. |
| Fórmula de KPI | Substitui a contagem bruta de eventos por uma métrica calculada, construída a partir de um numerador (como uma contagem de eventos personalizados) e um denominador (como usuários ativos diários, MAU ou o tamanho de um Segment com análise de dados ativada). Quando você seleciona uma ou mais fórmulas, o gráfico plota o valor de cada fórmula ao longo do intervalo de datas selecionado, para que você possa comparar o desempenho normalizado (por exemplo, "eventos por usuário ativo") em vez do volume total de eventos. Se não houver dados disponíveis para o intervalo de tempo e as fórmulas selecionadas, a Braze exibirá uma mensagem de "sem dados" — amplie o intervalo de tempo ou escolha fórmulas diferentes. Selecione **Manage KPI formulas** para criar ou editar fórmulas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configure seu relatório" }

## Exportar dados {#export-data}

Para exportar os dados dos seus eventos personalizados, selecione <i class="fas fa-bars" title="Menu de contexto do gráfico"></i> **Menu de contexto do gráfico** no gráfico de eventos personalizados e selecione a opção de exportação desejada.

{% alert tip %}
Para obter ajuda com exportações de CSV e API, consulte [Solução de problemas de exportação]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}

## Solução de problemas {#troubleshooting}

### O detalhamento por Segment não corresponde aos totais do espaço de trabalho {#segment-breakdown-doesnt-match-workspace-totals}

Quando você usa **Filtrar por Segments** ou restringe o relatório com o menu suspenso **Apps**, o gráfico conta os usuários no Segment (ou app) selecionado que realizaram o evento personalizado — e não todas as ocorrências do evento em todo o espaço de trabalho.

Se você comparar uma linha de Segment com uma visualização sem filtros (ou com **All Apps**), os totais frequentemente diferem porque:

- **All Apps** pode incluir usuários e eventos de todos os apps no espaço de trabalho.
- Um filtro de app único inclui apenas perfis vinculados àquele app.
- Filtros de Segment contam os usuários que correspondem à definição do Segment no momento da consulta, o que pode excluir usuários que realizaram o evento fora dos critérios do Segment.

Para fazer uma comparação equivalente, use o mesmo filtro de app e a mesma seleção de Segment para cada série que você comparar, ou exporte os dados e reconcilie as contagens na sua ferramenta de análise de dados.