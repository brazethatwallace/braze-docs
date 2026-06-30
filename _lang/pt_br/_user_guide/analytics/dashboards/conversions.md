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

1. Acesse **Analytics** > **Conversões**.
2. Selecione um **Período** para o relatório, com uma janela de até 90 dias.
3. Selecione as campanhas ou Canvas (ou ambos) para analisar.
   - (opcional) Filtre campanhas e Canvas selecionando uma tag.
4. Selecione o(s) **Canal(is)** para analisar nas suas mensagens.
5. Selecione uma camada de **Detalhamento por** para visualizar diferentes dimensões de dados, como por variante, etapa do Canvas, país ou idioma.
6. (Opcional) Se você quiser calcular conversões de um evento que não foi configurado como evento de conversão na campanha ou no Canvas, ative [Usar eventos personalizados](#using-custom-events).
7. Selecione um [método de atribuição](#attribution-methods) para analisar as mensagens selecionadas.

{% alert note %}
Se você estiver analisando conversões para múltiplos canais, seu **Método de atribuição** será definido automaticamente como **Atribuição de último ponto de contato**.
{% endalert %}

{:start="8"}
8. Selecione **Criar** para executar o relatório.

Após o carregamento da página, selecione um **Evento de conversão** para filtrar o relatório por dados de conversão. As opções disponíveis incluirão os eventos pré-configurados nos Canvas e campanhas. Se você selecionou um evento personalizado ao configurar o relatório (etapa 6), essa opção não estará disponível.

### Usando eventos personalizados {#using-custom-events}

Para que as métricas de eventos personalizados apareçam no dashboard de conversões, você precisa ter um evento de conversão e um evento de entrada do Canvas no período especificado na página.

Para calcular conversões de um evento que não foi configurado como evento de conversão na campanha ou no Canvas, selecione um evento personalizado específico para usar como evento de conversão.

1. Ao configurar seu relatório, ative **Usar eventos personalizados**.
2. Selecione um evento personalizado para usar como evento de conversão.
3. Selecione a janela de conversão dentro da qual o evento deve ter ocorrido para ser contabilizado como conversão.

{% alert note %}
Se você selecionar um evento personalizado, não verá o menu suspenso **Evento de conversão** na página e precisará executar o relatório novamente para visualizar conversões de diferentes eventos personalizados.
{% endalert %}

### Considerações {#considerations}

Para que um usuário seja contabilizado no relatório, ele deve atender aos seguintes critérios dentro do período selecionado:
1. Entrar no Canvas ou campanha.
2. Registrar um [método de atribuição]({{site.baseurl}}/user_guide/analytics/dashboards/conversions#attribution-methods).
3. Realizar o evento de conversão.

Por exemplo, digamos que um usuário faça o seguinte:
1. Entra no Canvas em 30 de setembro.
2. Registra um método de atribuição em 1º de outubro.
3. Realiza o evento de conversão em 2 de outubro.

Esse usuário **não aparecerá** em um relatório com período de 1º a 7 de outubro. Isso ocorre porque o usuário entrou no Canvas antes do período do relatório, mesmo que o evento de conversão tenha ocorrido dentro do período definido. Para que o usuário apareça no relatório, o período deve incluir 30 de setembro.

## Entendendo seu relatório {#understanding-your-report}

Seu relatório é dividido em três seções:

- [Detalhes da conversão](#conversion-details)
- [Funil de conversão](#conversion-funnel)
- [Conversões ao longo do tempo](#conversions-over-time)

### Detalhes da conversão {#conversion-details}

A tabela de detalhes da conversão sempre exibe uma coluna para *Destinatários* e outra para *Conversões* (taxa e total). As duas colunas restantes que aparecem dependem das opções selecionadas ao configurar o relatório.

![Tabela de detalhes da conversão mostrando Pontos de contato como método de atribuição para as colunas três e quatro.]({% image_buster /assets/img_archive/conversions2_details.png %}){: style="border:none"}

A tabela a seguir descreve as métricas possíveis.

| Métrica exibida | Descrição |
| --- | --- |
| Destinatários | O número de usuários que receberam uma mensagem pelo canal selecionado dentro do período do relatório |
| Taxa de conversão (Destinatários) | Calculada como: (Número de conversões) / (Número de destinatários) |
| Método de atribuição | Definido pelo [método de atribuição](#attribution-methods) selecionado ao configurar o relatório. Para atribuição de último ponto de contato ou se múltiplos canais forem selecionados, aparece como [Pontos de contato](#terms-to-know). |
| Taxa de conversão (Método de atribuição) | Definida pelo [método de atribuição](#attribution-methods) selecionado ao configurar o relatório. Se múltiplos canais forem selecionados, o padrão é atribuição de último ponto de contato. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Detalhes da conversão" }

Se você selecionou detalhes em nível de detalhamento para campanhas ou Canvas ao [configurar seu relatório](#setting-up-your-report) (etapa 5), clique em <i class="fas fa-angle-down"></i> **Expandir** para expandir a tabela.

### Funil de conversão {#conversion-funnel}

Este gráfico de barras mostra as contagens absolutas de cada [evento de engajamento]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) com base no canal selecionado. A contagem de conversões será definida conforme o método de atribuição selecionado.

Por padrão, todas as campanhas e Canvas selecionados são exibidos. Para desmarcar uma campanha ou Canvas, selecione o nome da campanha ou Canvas que deseja excluir. Para mais detalhes sobre o evento de engajamento, passe o cursor sobre cada barra.

Para baixar os dados da série temporal, selecione uma opção de download: PNG, JPEG, PDF, SVG ou CSV.

{% alert note %}
Este gráfico exibe dados de apenas um canal por vez. Use o menu suspenso **Canal** no gráfico para selecionar um único canal.
{% endalert %}

![Gráfico de barras do funil de conversões para duas campanhas de e-mail mostrando resultados semelhantes para E-mail entregue, E-mail aberto, E-mail clicado e Conversões.]({% image_buster /assets/img_archive/conversions2_funnel.png %})

### Conversões ao longo do tempo {#conversions-over-time}

Este gráfico de série temporal inclui uma representação das conversões por campanha ou Canvas ao longo do tempo. Por padrão, todas as campanhas e Canvas selecionados são exibidos. Para desmarcar uma campanha ou Canvas, clique no nome da campanha ou Canvas que deseja excluir.

Para baixar os dados da série temporal, selecione <i class="fas fa-bars" title="Menu de contexto do gráfico"></i> **Menu de contexto do gráfico** e depois selecione a opção de download. As opções disponíveis são PNG, JPEG, PDF, SVG ou CSV.

![Gráfico de série temporal de conversões ao longo do tempo para duas campanhas de e-mail, mostrando conversões por dia.]({% image_buster /assets/img_archive/conversions2_over_time.png %})

### Métodos de atribuição {#attribution-methods}

| Método de atribuição | Definição | Cálculo da taxa | Opções específicas por canal |
| --- | --- | --- | --- |
| Ao receber | Número total de conversões que ocorreram após o recebimento da mensagem | Calculado como (Conversões únicas ao receber) / (Destinatários únicos) | {::nomarkdown}<ul><li>Ao entregar e-mail</li><li>Ao entregar SMS</li></ul>{:/} |
| Ao enviar | Número total de conversões que ocorreram após o envio da mensagem | Calculado como (Conversões únicas ao enviar) / (Destinatários únicos) | {::nomarkdown}<ul><li>Ao enviar push</li><li>Ao enviar cartão de conteúdo</li><li>Ao enviar SMS</li></ul>{:/} |
| Ao abrir | Número total de conversões que ocorreram após a abertura da mensagem | Calculado como (Conversões únicas ao abrir) / (Destinatários únicos) | {::nomarkdown}<ul><li>Ao abrir e-mail</li><li>Ao abrir push</li></ul>{:/} |
| Ao clicar | Número total de conversões que ocorreram após o clique na mensagem | Calculado como (Conversões únicas ao clicar) / (Destinatários únicos) | {::nomarkdown}<ul><li>Ao clicar em e-mail</li><li>Ao clicar em cartão de conteúdo</li><li>Ao clicar em mensagem no app</li></ul>{:/} |
| Ao visualizar | Número total de conversões que ocorreram após uma impressão | Calculado como (Conversões únicas por impressão) / (Destinatários únicos) | {::nomarkdown}<ul><li>Ao visualizar mensagem no app</li><li>Ao visualizar cartão de conteúdo</li></ul>{:/} |
| Último ponto de contato | Conversões que atribuem todo o crédito à última mensagem tocada ou clicada durante a janela de conversão. | Calculado como (Número de pontos de contato) / (Destinatários únicos) | A atribuição de último ponto de contato é selecionada automaticamente se múltiplos canais forem adicionados ao relatório. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Métodos de atribuição" }

## Termos importantes {#terms-to-know}

| Termo | Definição |
| --- | --- |
| Ponto de contato | Uma interação física ou ponto de contato com uma mensagem.<br><br>Os pontos de contato podem incluir:<br>{::nomarkdown}<ul><li>Clique em e-mail</li><li>Abertura de push</li><li>Clique em cartão de conteúdo</li><li>Clique em mensagem no app</li><li>Clique em SMS</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Termos importantes" }

## Solução de problemas {#troubleshooting}

### Por que minhas conversões de campanha ou Canvas estão baixas? {#why-do-i-have-low-campaign-or-canvas-conversions}

Suas conversões podem não estar tão altas quanto o esperado em comparação com campanhas anteriores ou suas expectativas. As conversões dependem de duas funções principais: rastreamento de eventos e prazos de conversão.

Para solucionar o problema, verifique o rastreamento de eventos e os prazos de conversão.

#### Rastreamento de eventos {#event-tracking}

Quando uma campanha dispara um início de sessão ou evento personalizado, você deve garantir que esse evento, ou sessão, esteja ocorrendo com frequência suficiente para disparar a mensagem. Verifique o [dashboard inicial]({{site.baseurl}}/user_guide/analytics/dashboards/home) para dados de sessão ou o relatório de [eventos personalizados]({{site.baseurl}}/user_guide/analytics/reports/configure_reporting).

#### Prazos de conversão {#conversion-deadlines}

Para cada evento de conversão selecionado por campanha, você define o [prazo]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events#creating-a-campaign-with-conversion-tracking). Isso significa que você está definindo um limite de tempo dentro do qual uma conversão deve ocorrer para ser contabilizada em cada campanha respectiva.

Verifique se você revisou as informações sobre [regras de rastreamento de conversão]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events#conversion-tracking-rules) para entender as métricas da sua campanha. Para conversões de usuários no Canvas, consulte as [Perguntas frequentes sobre Canvas]({{site.baseurl}}/user_guide/messaging/canvas/faqs#how-are-user-conversions-tracked-in-a-canvas).