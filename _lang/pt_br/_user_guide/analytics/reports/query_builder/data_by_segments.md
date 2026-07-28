---
nav_title: Métricas por segmentos
article_title: Métricas por segmentos
page_order: 3
page_type: reference
description: "Esta página descreve como você pode usar modelos de relatório do Criador de consultas para detalhar métricas de desempenho de Campaigns, Canvas, variantes e etapas por segmentos."
tool:
  - Segments
  - Reports

---

# Métricas por segmentos {#metrics-by-segments}

> Use modelos de relatório do [Criador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder) para detalhar métricas de desempenho de Campaigns, Canvas, variantes e etapas por segmentos.

O [rastreamento de análise de dados]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking) deve estar ativado para os segmentos cujas métricas você deseja acessar.

Para executar esses relatórios, faça o seguinte:
1. No **Criador de consultas**, escolha criar um novo relatório SQL com um modelo.
2. Selecione **Segment breakdowns** para a métrica, o que filtra os modelos para aqueles em que as métricas incluem detalhamentos por segmento, que são:
- Métricas de desempenho de e-mail por segmento
- Métricas de engajamento de e-mail para variantes ou etapas, por segmento
- Compras e receita por segmento
- Compras e receita para variantes ou etapas, por segmento
- Desempenho de push por segmento

![A página de detalhamento por segmento contém um editor SQL, um painel lateral com guias para Variáveis, Tabelas de dados disponíveis, Histórico de consultas e o Criador de consultas com IA, além de uma seção de resultados.]({% image_buster /assets/img_archive/segment_breakdown.png %})

## Modelos de relatório {#report-templates}

{% tabs %}
{% tab Email engagement metrics by segment %}

### Visualizando métricas para Campaigns ou Canvas {#campaign-canvas-email}

Para visualizar métricas de desempenho de e-mail detalhadas por segmento no nível de Campaign ou Canvas, use a guia [Variáveis](#variables) para especificar as Campaigns ou Canvas e um período para extrair os dados. Se nenhuma Campaign ou Canvas for especificada, o relatório incluirá e-mails de todas as Campaigns e Canvas do período especificado. Você também pode optar por visualizar todas as Campaigns e Canvas com determinadas tags.

As seguintes métricas de e-mail estão disponíveis neste relatório:
- Envios
- Entregas
- Reclamações
- Aberturas únicas
- Aberturas únicas por máquina
- Aberturas únicas não realizadas por máquina
- Cliques únicos
- Cancelamentos de inscrição
- Bounces
- Soft bounces
- Adiados

#### Resultados {#results}

Seus resultados mostrarão métricas de engajamento de e-mail por segmento para as Campaigns ou Canvas que você selecionou. Se você não selecionou Campaigns ou Canvas específicas, seu relatório mostrará as métricas de e-mail para cada segmento em todas as Campaigns e Canvas de e-mail dentro do período do relatório.

- **Linhas:** Segments
- **Colunas:** Métricas de engajamento de e-mail

### Visualizando métricas para variantes ou etapas {#viewing-metrics-for-variants-or-steps}

Para visualizar o desempenho de e-mail detalhado por segmento no nível de variante de Campaign, variante de Canvas ou etapa do Canvas, primeiro escolha um relatório no nível de variante ou etapa (são relatórios que possuem "for variants or steps" no título) e, em seguida, use a guia **Variáveis** para especificar o seguinte:

- Campaign ou Canvas específica (obrigatório ao usar um relatório no nível de variante ou etapa)
- Variantes (obrigatório ao usar um relatório no nível de variante ou etapa)
- Etapa do Canvas (opcional)

As métricas são as mesmas oferecidas no modelo de [nível de Campaign ou Canvas](#campaign-canvas-email). Se você escolher múltiplas variantes, seus resultados serão agrupados por variante.

#### Resultados

Seus resultados mostrarão métricas de engajamento de e-mail por segmento para as variantes ou etapas selecionadas.

- **Linhas:** Segments
- **Colunas:** Métricas de engajamento de e-mail

{% endtab %}

{% tab Purchases and revenue by segment %}
### Visualizando métricas para Campaigns ou Canvas {#viewing-metrics-for-campaigns-or-canvases}

Para visualizar métricas de compra e receita detalhadas por segmento para uma Campaign ou Canvas específica, use a guia [Variáveis](#variables) para especificar o seguinte:

- Janela de conversão (o número de dias após o recebimento ou clique no e-mail em que a Braze deve atribuir compras ou receita)
- Produto específico (opcional)

Além disso, use a guia **Variáveis** para especificar se o relatório deve ser executado para uma ou mais Campaigns ou Canvas, ou uma ou mais tags. Se nenhuma Campaign, Canvas ou tag for escolhida, o relatório será executado para todos os e-mails de Campaigns ou Canvas durante o período escolhido.

Atualmente, este relatório extrai métricas apenas do canal de e-mail. Quaisquer dados de receita ou compra de canais além de e-mail não serão refletidos no relatório.

As seguintes métricas estão disponíveis para e-mails:

- Compras únicas após recebimento
- Receita após recebimento
- Compras únicas após clique
- Receita após clique
- Destinatários únicos
- Cliques únicos em e-mail

Todas as métricas de taxa usam destinatários únicos de e-mail como denominador.

#### Definições {#definitions}

- "Após recebimento" refere-se a eventos de compra ou receita que ocorreram dentro da janela de conversão especificada, após os usuários receberem as Campaigns ou Canvas especificadas.
- "Após clique" refere-se a eventos de compra ou receita que ocorreram após os eventos de compra, dentro da janela de conversão especificada, após os usuários clicarem nas Campaigns ou Canvas especificadas.

Por exemplo, digamos que um segmento contém 10 usuários e cinco deles fizeram uma compra após receber seu e-mail. Se um desses cinco fez uma compra após clicar no seu e-mail, sua "taxa de compras únicas após recebimento" seria de 50% e sua "taxa de compras únicas após clique" seria de 10%.

![O relatório mostra métricas de e-mail incluindo compras únicas após recebimento, receita após recebimento, compras únicas após clique, receita após clique, destinatários únicos e cliques únicos em e-mail.]({% image_buster /assets/img_archive/segment_breakdown_results.png %})

#### Resultados

Seus resultados mostrarão métricas de compra por segmento para as Campaigns ou Canvas selecionadas. Se você não selecionou Campaigns ou Canvas específicas, seu relatório mostrará as métricas de compra para cada segmento em todas as Campaigns ou Canvas de e-mail dentro do período do relatório.

- **Linhas:** Segments
- **Colunas:** Métricas de compra


### Visualizando métricas para variantes ou etapas

Para visualizar métricas de compra e receita detalhadas por segmento para uma variante de Campaign, variante de Canvas ou etapa do Canvas específica, use a guia [Variáveis](#variables) para especificar o seguinte:

- Campaign ou Canvas específica
- Variantes
- Etapa do Canvas (opcional)
- Período
- Produto específico (opcional)

#### Resultados

Seus resultados mostrarão métricas de compra por segmento para as variantes ou etapas selecionadas.

- **Linhas:** Segments
- **Colunas:** Métricas de compra

{% endtab %}
{% tab Top or bottom messaging for email engagement %}

### Visualizando métricas para os melhores ou piores desempenhos {#viewing-metrics-for-the-top-or-bottom-performers}

Este relatório na guia [Variáveis](#variables) exibe as Campaigns, Canvas ou etapas do Canvas que tiveram os melhores ou piores desempenhos para uma métrica de engajamento de e-mail especificada.

Casos de uso incluem:
- 10 Campaigns com as maiores taxas de abertura única de e-mail
- 25 Canvas com mais cancelamentos de inscrição de e-mail
- 50 etapas do Canvas com os maiores cliques únicos

As seguintes métricas de e-mail estão disponíveis neste relatório:
- Envios
- Entregas
- Reclamações
- Aberturas únicas
- Aberturas únicas por máquina
- Aberturas únicas não realizadas por máquina
- Cliques únicos
- Cancelamentos de inscrição
- Bounces
- Soft bounces
- Reclamações

Para visualizar este relatório, você deve especificar as seguintes variáveis na guia **Variáveis**:
- **Métricas:** selecione uma das métricas para classificar seus resultados
- **Número de relatórios:** selecione os melhores ou piores resultados e a quantidade de resultados, como os 10 melhores ou os 15 piores
- **Tipo de mensagem:** especifique se seus resultados são Campaigns, Canvas ou etapas do Canvas

#### Resultados

Seus resultados mostrarão as melhores (ou piores) Campaigns, Canvas ou etapas do Canvas que você selecionou. Por exemplo, se você selecionou as 10 melhores Campaigns por taxa de cliques, seus resultados mostrarão as 10 melhores Campaigns ordenadas da maior para a menor taxa de cliques. Suas colunas exibirão todas as métricas de engajamento de e-mail para cada linha (Campaigns, Canvas ou etapas de mensagem).

{% endtab %}
{% tab Top or bottom messaging for purchases %}

### Visualizando métricas para os melhores ou piores desempenhos

Este relatório na guia [Variáveis](#variables) exibe as Campaigns, Canvas ou etapas do Canvas que tiveram os melhores ou piores desempenhos para uma métrica de compra ou receita especificada.

Casos de uso incluem:
- 20 Campaigns com as maiores taxas de compra para um produto específico
- 25 Canvas com a maior receita gerada
- 10 etapas do Canvas com a menor taxa de compra de produto

As seguintes métricas de e-mail estão disponíveis neste relatório:
- Compras únicas após recebimento
- Receita após recebimento
- Compras únicas após clique
- Receita após clique
- Destinatários únicos
- Cliques únicos em e-mail

Para visualizar este relatório, você deve especificar as seguintes variáveis na guia **Variáveis**:
- **Métricas:** selecione uma das métricas para classificar seus resultados
- **Número de relatórios:** selecione os melhores ou piores resultados e a quantidade de resultados, como os 10 melhores ou os 15 piores
- **Tipo de mensagem:** especifique se seus resultados são Campaigns, Canvas ou etapas do Canvas
- **Janela de conversão:** o número de dias após o recebimento ou clique no e-mail em que a Braze atribuirá compras ou receita

#### Definições

- "Após recebimento" refere-se a eventos de compra ou receita que ocorreram dentro da janela de conversão especificada, após os usuários receberem as Campaigns ou Canvas especificadas.
- "Após clique" refere-se a eventos de compra ou receita que ocorreram após os eventos de compra, dentro da janela de conversão especificada, após os usuários clicarem nas Campaigns ou Canvas especificadas.

Por exemplo, digamos que um segmento contém 10 usuários e cinco deles fizeram uma compra após receber seu e-mail. Se um desses cinco fez uma compra após clicar no seu e-mail, sua taxa de "compras únicas após recebimento" seria de 50% e sua taxa de "compras únicas após clique" seria de 10%.

#### Resultados

Seus resultados mostrarão as melhores (ou piores) Campaigns, Canvas ou etapas do Canvas que você selecionou. Por exemplo, se você selecionou as 10 melhores Campaigns para "receita após clique", seus resultados mostrarão as 10 melhores Campaigns ordenadas da maior para a menor "receita após clique". Suas colunas exibirão todas as métricas de compra para cada linha (Campaigns, Canvas ou etapas de mensagem).

{% endtab %}
{% tab Push performance by segment %}

### Visualizando métricas de push para segmentos {#viewing-push-metrics-for-segments}

Este relatório na guia [Variáveis](#variables) exibe métricas de push detalhadas por segmentos.

Na guia **Variáveis**, especifique as Campaigns ou Canvas para visualizar as métricas e um período para extrair os dados. Se você não selecionar nenhuma Campaign ou Canvas, o relatório mostrará pushes de todas as Campaigns e Canvas no período especificado. Você também pode visualizar todas as Campaigns e Canvas com determinadas tags.

As seguintes métricas de push estão disponíveis neste relatório:

- Envios
- Bounces
- Entregas
- Aberturas Diretas

#### Resultados

Seu relatório exibirá os seguintes resultados:

- **Linhas:** Segments
- **Colunas:** Métricas de push
{% endtab %}
{% endtabs %}