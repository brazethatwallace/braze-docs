---
nav_title: Criador de relatórios (legado)
article_title: Criador de relatórios (legado)
alias: /report_builder_legacy/
page_order: 1
page_type: reference
description: "Esta página aborda como executar um relatório usando o criador de relatórios legado, incluindo relatórios de comparação de Campaigns e Canvas, além da criação de relatórios e gráficos."
tool:
  - Reports

---

# Criador de relatórios (legado) {#report-builder-legacy}

> O Criador de relatórios permite comparar os resultados de várias Campaigns ou Canvas em uma única visualização, facilitando a identificação de quais estratégias de engajamento mais impactaram suas métricas principais. Tanto para Campaigns quanto para Canvas, você pode exportar seus dados e salvar seu relatório para consulta futura.<br><br>Para uma lista descritiva das métricas que você encontrará em seus relatórios, consulte o [Glossário de métricas de relatório]({{site.baseurl}}/user_guide/analytics/metrics_glossary).

![Exemplo de comparação de Campaigns]({% image_buster /assets/img/campaign_comparison/campaign_main.png %}){: style="max-width:80%;"}

Use este relatório para responder a perguntas importantes sobre engajamento, como:

- Quais foram as Campaigns ou Canvas com melhor desempenho para uma tag ou canal específico?
- Quais variantes de Campaigns multivariantes tiveram maior impacto em relação ao grupo de controle?
- Qual Campaign de promoção sazonal gerou uma taxa de compra mais alta — a liquidação de verão, de outono ou de inverno?
- Quais notificações por push dentro deste Canvas tiveram as maiores taxas de abertura?
- Quais etapas neste grupo de Canvas tiveram mais conversões?
- A Versão 1 de um e-mail de boas-vindas ou a Versão 2 gerou maior engajamento e conversão? As mudanças funcionaram?
- Como diferentes métodos de entrega (por exemplo, 3 pushes agendados, 3 pushes baseados em ação e 3 pushes disparados por API) impactam suas taxas de abertura, taxas de conversão ou taxas de compra?
- As melhorias contínuas nas mensagens para usuários inativos impactaram positivamente seus KPIs ao longo do tempo?

{% alert tip %}
Tente usar os mesmos eventos de conversão para conversão A, B e assim por diante nas Campaigns e Canvas que você deseja comparar, para que seja possível alinhar essas conversões nos seus relatórios do Criador de relatórios.
{% endalert %}

## Executando um relatório {#running-a-report}

### Etapa 1: Criar um novo relatório {#step-1-create-a-new-report}

No dashboard, navegue até **Analytics** > **Report Builder**.

Selecione **Criar novo relatório** e escolha entre um relatório de comparação de Campaigns ou um relatório de comparação de Canvas.

Se você optar por executar um relatório sobre Campaigns, poderá escolher entre um relatório **Manual** ou **Automatizado**. Os relatórios podem conter Campaigns ou Canvas, mas não ambos juntos. Quaisquer Campaigns e Canvas que tenham enviado mensagens nos últimos 12 meses serão elegíveis para um relatório.

![Dashboard de Campaigns]({% image_buster /assets/img/campaign_comparison/create_report.png %}){: style="max-width:80%;"}

A seguir estão as diferenças entre essas duas opções:

| **Ação** | **Manual** | **Automatizado** |
| ---- | ---------- | ------------- |
| **Criação do relatório** | Você poderá refinar sua lista de Campaigns usando filtros e, em seguida, marcar Campaigns específicas. | Você criará seu relatório usando as opções de filtro para refinar sua lista de Campaigns. |
| **Salvar e visualizar o relatório** | Você pode salvar seu relatório. Na próxima vez que visualizá-lo, poderá ver as mesmas Campaigns adicionadas anteriormente, pois elas ainda se enquadram no filtro "Last Sent". | Você pode salvar seu relatório. Na próxima vez que visualizá-lo, o relatório será atualizado automaticamente para incluir todas as Campaigns que correspondem aos seus filtros. |
| **Editar o relatório** | Você pode selecionar **Editar relatório** para adicionar ou remover Campaigns do seu relatório. | Você pode editar seu relatório ajustando os critérios de filtro. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Etapa 1: Criar um novo relatório" }

{% alert note %}
Tanto os relatórios **Manual** quanto os **Automatizado** podem incluir no máximo 250 Campaigns em um relatório.
{% endalert %}

Os relatórios de Canvas funcionam de forma semelhante a um relatório manual de Campaigns, pois as seleções de Canvas e as atualizações do relatório também devem ser feitas manualmente. Você pode incluir no máximo cinco Canvas em um relatório.

### Etapa 2: Escolher suas métricas {#step-2-choose-your-metrics}

Depois de criar seu relatório, você encontrará uma tabela em branco com Campaigns em cada linha. A tabela será preenchida após você selecionar **Editar colunas** e escolher as métricas que deseja adicionar.

![Opções de Campaigns]({% image_buster /assets/img/campaign_comparison/campaign_comparison_columns.png %}){: style="max-width:80%;"}

Sua tabela será preenchida com as métricas escolhidas. Para definições dessas métricas, consulte o [Glossário de métricas de relatório]({{site.baseurl}}/user_guide/analytics/metrics_glossary). Algumas métricas estão disponíveis apenas para relatórios de comparação de Campaigns.

Você também pode alternar os cálculos de **Média** para qualquer taxa ou métrica numérica e **Total** para qualquer métrica numérica.

### Etapa 3: Escolher um período de tempo {#step-3-choose-a-time-period}

Você pode selecionar um período de tempo específico para visualizar os dados do seu relatório. Se uma Campaign, Canvas, variante de Canvas ou componente de Canvas específico não tiver dados para o período selecionado, os resultados dessa linha ficarão em branco.

![Métrica numérica de Campaign]({% image_buster /assets/img/campaign_comparison/metric.png %}){: style="max-width:60%;"}

### Etapa 4: Nomear e salvar seu relatório {#step-4-name-and-save-your-report}

Nomeie seu relatório antes de salvá-lo. Se um relatório for salvo sem nome, a Braze aplicará o nome padrão "Campaign Comparison Report".

![Nota de Campaign]({% image_buster /assets/img/campaign_comparison/comparison_name.png %}){: style="max-width:60%;"}

Quando estiver pronto, selecione **Salvar**. Os relatórios salvos podem ser visualizados posteriormente na página do **Criador de relatórios**.

## Relatório de comparação de Campaigns com Campaigns multivariantes {#campaign-comparison-report-with-multivariate-campaigns}

Para qualquer Campaign multivariante, você pode visualizar essas métricas detalhadas por variantes e grupo de controle clicando na seta ao lado do nome da Campaign. As linhas contendo suas variantes incluirão os resultados de desempenho dessa variante, e a linha contendo seu grupo de controle incluirá apenas os resultados dos seus eventos de conversão.

![Nota de Campaign]({% image_buster /assets/img/campaign_comparison/compare_note.png %}){: style="float:right;max-width:15%;margin-left:15px;"}

As métricas que preenchem a linha da sua Campaign geral refletirão o desempenho de suas variantes, mas não incluirão o desempenho do grupo de controle. Por exemplo, a conversão primária A da sua Campaign geral será a soma da conversão primária A de suas variantes, e isso não incluirá a conversão primária A do seu grupo de controle.

{% alert important %}
Se você excluir uma variante de uma Campaign multivariante, os dados dessa variante não estarão disponíveis para uso em um relatório futuro.
{% endalert %}

## Detalhamento do relatório de comparação de Canvas {#canvas-comparison-report-breakdown}

Em um relatório de Canvas, você pode visualizar seus Canvas detalhados por variante, etapas ou mensagem.

### Variante {#variant}

Selecionar **detalhamento por variante** permite visualizar as estatísticas de alto nível dos seus Canvas gerais, bem como as estatísticas de cada variante, que podem ser expandidas clicando na seta ao lado do nome do Canvas.

![Variantes]({% image_buster /assets/img/campaign_comparison/campaign_comparison1.png %}){: style="max-width:90%;"}

### Etapas {#steps}

Selecionar **detalhamento por etapas** permite visualizar métricas no nível de etapa, com cada linha do relatório contendo uma etapa.

![Etapas]({% image_buster /assets/img/campaign_comparison/campaign_comparison2.png %}){: style="max-width:90%;"}

### Mensagem {#message}

Semelhante ao detalhamento por etapa, selecionar **detalhamento por mensagem** mostra o nome das etapas em cada linha. No entanto, em **Editar colunas**, você terá acesso a métricas no nível de mensagem, como estatísticas específicas de canal, como cliques em e-mail e aberturas de push.

![Relatório]({% image_buster /assets/img/campaign_comparison/campaign_comparison3.png %}){: style="max-width:90%;"}

Observe que, no dashboard da Braze, você pode pré-visualizar as primeiras 50 linhas do seu relatório de Canvas. Você pode acessar o relatório completo ao exportar um CSV.

## Acessando relatórios salvos {#accessing-saved-reports}

Ao acessar um **relatório manual** salvo, você pode visualizar as mesmas Campaigns adicionadas anteriormente, pois elas ainda se enquadram no filtro "Last Sent".

Ao acessar um **relatório automatizado** salvo, o relatório será atualizado automaticamente para incluir todas as Campaigns que correspondem aos seus filtros. Por exemplo, se seu relatório filtrou Campaigns com a tag "Promotion", cada vez que você visualizar este relatório, poderá ver todas as Campaigns com a tag "Promotion", mesmo que essas Campaigns tenham sido criadas após a criação do relatório.

## Editando relatórios {#editing-reports}

Em um **relatório manual**, você pode editar um relatório selecionando **Editar**. A partir daí, você pode selecionar ou desmarcar Campaigns para incluir no seu relatório.

Em um **relatório automatizado**, alterne seus filtros para refinar os resultados do seu relatório.

## Exportando relatórios {#exporting-reports}

Você também pode selecionar **Exportar** para baixar seu relatório em CSV.

Se seu relatório contiver Campaigns multivariantes, sua exportação incluirá dois arquivos CSV:

- Um arquivo contendo apenas as métricas de nível superior de cada Campaign
- Um arquivo contendo métricas no nível de variante

O arquivo contendo métricas de variante terá `variant_` adicionado ao início do seu nome. Na primeira vez que você exportar um relatório automatizado, receberá um pop-up solicitando permissão para baixar múltiplos arquivos — clique em **Permitir**.

![Download de Campaign]({% image_buster /assets/img/campaign_comparison/download.png %}){: style="max-width:60%;"}

### Exportando relatórios de comparação de Canvas {#exporting-canvas-comparison-reports}

Sua exportação em CSV refletirá a visualização de detalhamento em que você estava quando selecionou **Exportar**. Por exemplo, se você estava na visualização de detalhamento por etapa, sua exportação conterá dados sobre as métricas de etapa. Para exportar dados de um detalhamento diferente, você precisará navegar até esse detalhamento primeiro e selecionar **Exportar** a partir de lá.

Se você baixar um relatório de Canvas com detalhamento por variante, receberá dois arquivos CSV:

- Um arquivo contendo apenas métricas de nível superior de cada Canvas
- Um arquivo contendo métricas no nível de variante

## Criando gráficos {#building-charts}

Use gráficos para visualizar uma métrica selecionada no seu relatório. Os gráficos estão disponíveis para relatórios que apresentam Campaigns e que tenham pelo menos uma métrica adicionada às suas colunas.

![Gráfico de desempenho de Campaign com a métrica Mensagens enviadas selecionada]({% image_buster /assets/img/campaign_comparison/report_builder_charts.png %})

Por padrão, o gráfico em cada relatório exibirá a métrica na primeira coluna do relatório. Para selecionar uma métrica diferente para o gráfico, escolha sua métrica no menu suspenso. Qualquer métrica na tabela do seu relatório estará disponível para exibição no gráfico.

Você pode representar graficamente no máximo três métricas. As unidades de todas as métricas devem ser as mesmas — por exemplo, se você escolher uma taxa no primeiro menu suspenso, apenas taxas estarão disponíveis para seleção no segundo menu suspenso.

Se seu gráfico contiver apenas uma métrica, ele exibirá até 30 Campaigns em ordem decrescente com base na métrica selecionada. Por exemplo, se a métrica do seu gráfico for cliques em e-mail, o gráfico exibirá as 30 Campaigns de e-mail com mais cliques, ordenadas do maior para o menor número de cliques. Se seu relatório contiver mais de 30 Campaigns, apenas as 30 principais serão exibidas no gráfico. Se você selecionar mais de uma métrica, o gráfico exibirá apenas as cinco principais Campaigns com base na primeira métrica selecionada.

Atualmente, os gráficos não são salvos quando você salva seu relatório.