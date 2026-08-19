---
nav_title: Conversões
article_title: Dashboard de conversões
alias: "/conversions_dashboard_v2/"
description: "O dashboard de conversões permite analisar conversões em campanhas, Canvas e canais, usando diferentes métodos de atribuição."
page_order: 3
page_type: reference
tool:
  - Reports
---

# Dashboard de conversões {#conversions-dashboard}

> O dashboard de conversões analisa conversões em campanhas, Canvas e canais, usando vários [métodos de atribuição](#attribution-methods). Ao medir suas conversões, você pode especificar o período, o evento de conversão e a janela de conversão.

## Configurando seu relatório {#setting-up-your-report}

Para configurar o relatório do dashboard de conversões:

1. Acesse **Analytics** > **Conversions**.
2. Selecione um **Date Range** para o seu relatório, com uma janela de até 90 dias.
3. Selecione as Campaigns ou Canvas (ou ambos) para análise.
   - (opcional) Filtre Campaigns e Canvas selecionando uma tag.
4. Selecione o(s) **Channel(s)** para analisar nas suas mensagens.
5. Selecione uma camada de **Breakdown by** para visualizar diferentes dimensões de dados, como por variante, etapa do Canvas, país ou idioma.
6. (Opcional) Se você quiser calcular conversões de um evento que não foi configurado como evento de conversão na Campaign ou no Canvas, ative [Usar eventos personalizados](#using-custom-events).
7. Selecione um [método de atribuição](#attribution-methods) para analisar as mensagens selecionadas.

{% alert note %}
Se você estiver analisando conversões para múltiplos canais, seu **Attribution Method** será definido por padrão como **Last-Touch Attribution**.
{% endalert %}

{:start="8"}
8. Selecione **Create** para executar o relatório.

Após o carregamento da página, selecione um **Conversion Event** para filtrar o relatório por dados de conversão. As seleções disponíveis incluirão os eventos que foram pré-configurados nos Canvas e nas Campaigns. Se você selecionou um evento personalizado ao configurar seu relatório (etapa 6), essa opção não estará disponível.

### Usando eventos personalizados {#using-custom-events}

Para que as métricas de eventos personalizados apareçam no dashboard de conversões, você precisa ter um evento de conversão e um evento de entrada do Canvas no período especificado na página.

Para calcular conversões de um evento que não foi configurado como evento de conversão na Campaign ou no Canvas, selecione um evento personalizado específico para usar como evento de conversão.

1. Ao configurar seu relatório, ative **Use custom events**.
2. Selecione um evento personalizado para usar como evento de conversão.
3. Selecione a janela de conversão dentro da qual o evento deve ter ocorrido para ser contabilizado como uma conversão.

{% alert note %}
Se você selecionar um evento personalizado, não verá o menu suspenso **Conversion Event** na página e precisará executar o relatório novamente para visualizar conversões de diferentes eventos personalizados.
{% endalert %}

### Considerações {#considerations}

Para que um usuário seja contabilizado no relatório, ele deve atender aos seguintes critérios dentro do período selecionado:
1. Entrar no Canvas ou na Campaign.
2. Registrar um [método de atribuição]({{site.baseurl}}/user_guide/analytics/dashboards/conversions#attribution-methods).
3. Realizar o evento de conversão.

Por exemplo, digamos que um usuário faça o seguinte:
1. Entra no Canvas em 30 de setembro.
2. Registra um método de atribuição em 1º de outubro.
3. Realiza o evento de conversão em 2 de outubro.

Esse usuário **não aparecerá** em um relatório com período de 1º a 7 de outubro. Isso ocorre porque o usuário entrou no Canvas antes do período do relatório, mesmo que o evento de conversão tenha ocorrido dentro do período definido. Para que o usuário apareça no relatório, o período deve incluir 30 de setembro.

## Entendendo seu relatório {#understanding-your-report}

Seu relatório é dividido em três seções:

- [Detalhes de conversão](#conversion-details)
- [Funil de conversão](#conversion-funnel)
- [Conversões ao longo do tempo](#conversions-over-time)

### Detalhes de conversão {#conversion-details}

A tabela de detalhes de conversão sempre mostra uma coluna para *Destinatários* e outra para *Conversões* (taxa e total). As duas colunas restantes que aparecem dependem das opções que você selecionou ao configurar seu relatório.

![Tabela de detalhes de conversão mostrando Pontos de contato como método de atribuição para as colunas três e quatro.]({% image_buster /assets/img_archive/conversions2_details.png %}){: style="border:none"}

A tabela a seguir descreve as métricas possíveis.

| Métrica exibida | Descrição |
| --- | --- |
| Destinatários | O número de usuários que receberam uma mensagem pelo canal selecionado dentro do período do relatório |
| Taxa de conversão (Destinatários) | Calculada como: (Número de conversões) / (Número de destinatários) |
| Método de atribuição | Definido pelo [método de atribuição](#attribution-methods) que você selecionou ao configurar o relatório. Para atribuição de último ponto de contato ou se vários canais forem selecionados, isso aparece como [Pontos de contato](#terms-to-know). |
| Taxa de conversão (Método de atribuição) | Definida pelo [método de atribuição](#attribution-methods) que você selecionou ao configurar o relatório. Se vários canais forem selecionados, o padrão é a atribuição de último ponto de contato. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Detalhes de conversão" }

Se você selecionou detalhes no nível de detalhamento para Campaigns ou Canvas ao [configurar seu relatório](#setting-up-your-report) (etapa 5), você pode selecionar <i class="fas fa-angle-down"></i> **Expandir** para expandir a tabela.

### Funil de conversão {#conversion-funnel}

Este gráfico de barras mostra as contagens absolutas para cada [evento de engajamento]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) com base no canal selecionado. A contagem de conversões será definida conforme o método de atribuição selecionado.

Por padrão, todas as Campaigns e Canvas selecionados são exibidos. Para desmarcar uma Campaign ou Canvas, selecione o nome da Campaign ou Canvas que você deseja excluir. Para detalhes adicionais sobre o evento de engajamento, passe o cursor sobre cada barra.

Para baixar os dados da série temporal, selecione uma opção de download: PNG, JPEG, PDF, SVG ou CSV.

{% alert note %}
Este gráfico mostra dados de apenas um canal por vez. Use o menu suspenso **Canal** no gráfico para selecionar um único canal.
{% endalert %}

![Gráfico de barras do funil de conversão para duas Campaigns de e-mail mostrando resultados semelhantes para E-mail entregue, E-mail aberto, E-mail clicado e Conversões.]({% image_buster /assets/img_archive/conversions2_funnel.png %})

### Conversões ao longo do tempo {#conversions-over-time}

Este gráfico de série temporal inclui uma representação das conversões por Campaign ou Canvas ao longo do tempo. Por padrão, todas as Campaigns e Canvas selecionados são exibidos. Para desmarcar uma Campaign ou Canvas, clique no nome da Campaign ou Canvas que você deseja excluir.

Para baixar os dados da série temporal, selecione <i class="fas fa-bars" title="Menu de contexto do gráfico"></i> **Menu de contexto do gráfico** e depois selecione sua opção de download. As opções disponíveis são PNG, JPEG, PDF, SVG ou CSV.

![Gráfico de série temporal de conversões ao longo do tempo para duas Campaigns de e-mail, mostrando conversões por dia.]({% image_buster /assets/img_archive/conversions2_over_time.png %})

### Métodos de atribuição {#attribution-methods}

| Método de atribuição | Definição | Cálculo da taxa | Opções específicas do canal |
| --- | --- | --- | --- |
| Ao receber | Número total de conversões que ocorreram após o recebimento da mensagem | Calculado como (Conversões únicas por recebimento) / (Destinatários únicos) | {::nomarkdown}<ul><li>Ao entregar e-mail</li><li>Ao entregar SMS</li></ul>{:/} |
| Ao enviar | Número total de conversões que ocorreram após o envio da mensagem | Calculado como (Conversões únicas por envio) / (Destinatários únicos) | {::nomarkdown}<ul><li>Ao enviar push</li><li>Ao enviar cartão de conteúdo</li><li>Ao enviar SMS</li></ul>{:/} |
| Ao abrir | Número total de conversões que ocorreram após a abertura da mensagem | Calculado como (Conversões únicas por abertura) / (Destinatários únicos) | {::nomarkdown}<ul><li>Ao abrir e-mail</li><li>Ao abrir push</li></ul>{:/} |
| Ao clicar | Número total de conversões que ocorreram após o clique na mensagem | Calculado como (Conversões únicas por clique) / (Destinatários únicos) | {::nomarkdown}<ul><li>Ao clicar em e-mail</li><li>Ao clicar em cartão de conteúdo</li><li>Ao clicar em mensagem no app</li></ul>{:/} |
| Ao visualizar | Número total de conversões que ocorreram após uma impressão | Calculado como (Conversões únicas por impressão) / (Destinatários únicos) | {::nomarkdown}<ul><li>Ao visualizar mensagem no app</li><li>Ao visualizar cartão de conteúdo</li></ul>{:/} |
| Ao último ponto de contato | Conversões que atribuem todo o crédito à última mensagem tocada ou clicada durante a janela de conversão. | Calculado como (Número de pontos de contato) / (Destinatários únicos) | A atribuição de último ponto de contato é selecionada automaticamente se vários canais forem adicionados ao relatório. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Métodos de atribuição" }

## Termos importantes {#terms-to-know}

| Termo | Definição |
| --- | --- |
| Ponto de contato | Uma interação física ou ponto de contato com uma mensagem.<br><br>Os pontos de contato podem incluir:<br>{::nomarkdown}<ul><li>Clique no e-mail</li><li>Abertura de push</li><li>Clique no cartão de conteúdo</li><li>Clique na mensagem no app</li><li>Clique no SMS</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Termos importantes" }

## Solução de problemas {#troubleshooting}

### Por que minhas conversões de Campaign ou Canvas estão baixas? {#why-do-i-have-low-campaign-or-canvas-conversions}

Suas conversões podem não estar tão altas quanto o esperado em comparação com campanhas anteriores ou suas expectativas. As conversões dependem de duas funções principais: rastreamento de eventos e prazos de conversão.

Para solucionar o problema, verifique o rastreamento de eventos e os prazos de conversão.

#### Rastreamento de eventos {#event-tracking}

Quando uma Campaign dispara um início de sessão ou evento personalizado, você deve garantir que esse evento, ou sessão, esteja ocorrendo com frequência suficiente para disparar a mensagem. Verifique o [dashboard inicial]({{site.baseurl}}/user_guide/analytics/dashboards/home) para dados de sessão ou o relatório de [eventos personalizados]({{site.baseurl}}/user_guide/analytics/reports/configure_reporting).

#### Prazos de conversão {#conversion-deadlines}

Para cada evento de conversão selecionado por Campaign, você define o [prazo]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events#creating-a-campaign-with-conversion-tracking). Isso significa que você está definindo um limite de tempo dentro do qual uma conversão deve ocorrer para ser contabilizada em cada Campaign respectiva.

Revise as informações sobre [regras de rastreamento de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events#conversion-tracking-rules) para entender as métricas da sua Campaign. Para conversões de usuários no Canvas, consulte as [Perguntas frequentes sobre Canvas]({{site.baseurl}}/user_guide/messaging/canvas/faqs#how-are-user-conversions-tracked-in-a-canvas).

### Por que os totais de abertura de e-mail não correspondem ao Campaign Analytics? {#why-dont-email-open-totals-match-campaign-analytics}

O **Campaign Analytics** e o Report Builder contam as [aberturas por máquina]({{site.baseurl}}/user_guide/analytics/metrics_glossary#machine-opens) em *Aberturas únicas*. Consulte [A métrica *Aberturas únicas* inclui *Aberturas por máquina*?]({{site.baseurl}}/user_guide/channels/email/faq#does-the-unique-opens-metric-include-machine-opens) nas perguntas frequentes sobre e-mail para mais detalhes.

No **Conversion Dashboard**, a atribuição **Upon Email Open** conta apenas aberturas humanas. As [aberturas por máquina]({{site.baseurl}}/user_guide/analytics/metrics_glossary#machine-opens) não são incluídas na contagem de aberturas usada para esse método de atribuição.

Por causa dessa diferença, os totais de aberturas no Campaign Analytics podem ser maiores do que as contagens de aberturas usadas na atribuição do Conversion Dashboard para as mesmas Campaigns. Compare as métricas dentro da mesma superfície ou use *Other Opens* no Campaign Analytics quando quiser engajamento humano sem aberturas por máquina.