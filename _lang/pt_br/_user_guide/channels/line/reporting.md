---
nav_title: Relatórios
article_title: Relatórios do LINE
page_order: 21
description: "Este artigo de referência aborda as métricas do LINE usadas na Braze, bem como onde visualizá-las nas suas campanhas do LINE."
page_type: reference
channel:
 - LINE
alias: /line/reporting/
---

# Relatórios do LINE {#line-reporting}

> Após lançar sua Campaign ou Canvas, você pode visualizar as principais métricas na página de detalhes da Campaign ou na análise de dados do Canvas. Este artigo aborda onde encontrar essas métricas e o que elas representam.

{% alert tip %}
Procurando definições para os termos e métricas do seu relatório? Consulte o [Glossário de métricas de relatório]({{site.baseurl}}/user_guide/analytics/metrics_glossary/).
{% endalert %}

## Análise de dados da Campaign {#campaign-analytics}

Na guia **Campaign Analytics**, você pode visualizar seus relatórios em uma série de painéis. Você pode ver mais ou menos do que os listados nas seções abaixo, mas cada um tem sua finalidade.

{% alert note %}
As estatísticas relacionadas a aberturas e cliques do LINE só são calculadas se mais de 20 usuários realizarem o evento em um determinado dia.
{% endalert %}

### Detalhes da Campaign {#campaign-details}

O painel **Campaign Details** mostra uma visão geral de alto nível do desempenho das suas mensagens do LINE.

Revise este painel para ver métricas gerais, como o número de mensagens enviadas para o número de destinatários, a taxa de conversão primária e a receita total gerada por esta mensagem. Você também pode revisar as configurações de entrega, público e conversão nesta página.

#### Grupos de controle {#control-groups}

Para medir o impacto de uma mensagem individual do LINE, você pode adicionar um [grupo de controle]({{site.baseurl}}/user_guide/messaging/ab_testing/) a um teste A/B. O painel de nível superior **Campaign Details** não inclui métricas da Variante do grupo de controle.

### Desempenho do LINE {#line-performance}

O painel **LINE Performance** descreve o desempenho da sua mensagem em várias dimensões. As métricas neste painel variam dependendo do canal de envio de mensagens escolhido e se você está executando um teste multivariante ou não. Você pode clicar no ícone <i class="fa fa-eye preview-icon"></i> **Preview** para visualizar sua mensagem para cada variante ou canal.

![O painel "LINE Performance" mostrando métricas para duas variantes.]({% image_buster /assets/img/line/line_performance.png %})

Se quiser simplificar sua visualização, selecione **+ Add/Remove Columns** e desmarque as métricas desejadas. Por padrão, todas as métricas são exibidas.

#### Métricas do LINE {#line-metrics}

Aqui estão algumas métricas importantes do LINE que você pode ver na sua análise de dados. Para ver as definições de todas as métricas do LINE usadas na Braze, consulte o [Glossário de métricas de relatório]({{site.baseurl}}/user_guide/analytics/metrics_glossary/).

| Termo | Definição |
| --- | --- |
| Envios | O número total de envios comunicados com sucesso entre a Braze e o LINE. Isso não significa que a mensagem foi recebida pelo usuário. |
| Aberturas únicas | O número total de mensagens do LINE enviadas que foram abertas pelos usuários após um limite mínimo de 20 mensagens por dia ter sido atingido. |
| Total de aberturas | O número total de vezes que as mensagens do LINE enviadas foram abertas pelos usuários após um limite mínimo de 20 mensagens por dia ter sido atingido. |
| Cliques únicos | O número total de mensagens do LINE enviadas que foram clicadas pelos usuários, após um limite mínimo de 20 mensagens por dia ter sido atingido. |
| Total de cliques | O número total de vezes que as mensagens do LINE enviadas foram clicadas pelos usuários após um limite mínimo de 20 mensagens por dia ter sido atingido. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métricas do LINE" }

### Desempenho histórico {#historical-performance}

O painel **Historical Performance** permite visualizar as métricas do painel **Message Performance** como um gráfico ao longo do tempo. Use os filtros na parte superior do painel para modificar as estatísticas e os canais exibidos no gráfico. O intervalo de tempo deste gráfico sempre corresponde ao intervalo de tempo especificado na parte superior da página.

Para obter um detalhamento dia a dia, selecione o menu hambúrguer <i class="fas fa-bars"></i> e selecione **Download CSV** para receber uma exportação CSV do relatório.

### Detalhes do evento de conversão {#conversion-event-details}

O painel **Conversion Event Details** mostra o desempenho dos seus eventos de conversão para a sua Campaign. Para saber mais, consulte [Eventos de conversão]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/conversion_correlation/).

### Correlação de conversão {#conversion-correlation}

O painel **Conversion Correlation** fornece insights sobre quais atributos e comportamentos dos usuários ajudam ou prejudicam os resultados que você definiu para as Campaigns. Para saber mais, consulte [Correlação de conversão]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/conversion_correlation/).