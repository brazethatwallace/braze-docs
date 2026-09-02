---
nav_title: Relatórios de funil
article_title: Relatórios de funil para Campaigns e Canvas
page_order: 8
page_type: reference
description: "Esta página aborda os benefícios dos relatórios de funil, como configurá-los e como interpretar seu relatório."
tool: Reports
---

# Relatórios de funil {#funnel-reports}

> A página **Relatório de funil** oferece um relatório visual que permite analisar as jornadas que seus clientes percorrem após receberem uma Campaign ou Canvas, incluindo as diferentes ações que os clientes realizam em seu caminho até a conversão e onde ocorrem as desistências. ![Captura de tela da página Relatório de funil mostrando um funil de conversão para desempenho de Campaign ou Canvas]({% image_buster /assets/img/funnel_report/funnel_report2.png %}){: style="float:right;max-width:15%;margin-bottom:15px; border: 0"}

Se sua Campaign ou Canvas usa um grupo de controle ou múltiplas variantes, você pode entender como as diferentes variantes impactaram o funil de conversão em um nível mais granular e otimizar com base nesses dados.

![Relatório de funil 1]({% image_buster /assets/img/funnel_report/funnel_report1.jpg %}){: style="max-width:80%;"}

## Casos de uso {#use-cases}

Os relatórios de funil podem responder perguntas como:

- **Integração:** Após enviar um Canvas "Bem-vindo, novato!", quantos usuários completaram cada etapa da jornada de integração?
- **Conclusão de compra:** Onde ocorreram as desistências de compra em uma promoção sazonal?
- **Conversões personalizadas:** Qual porcentagem de usuários iniciou uma sessão, ouviu uma faixa e criou uma playlist após um push de "Novo lançamento"?
- **Desistências de upsell:** Em um Canvas de upsell, onde os usuários saíram antes de assinar?
- **Comportamentos pós-engajamento:** Qual variante de e-mail gerou mais compras após os usuários abrirem?
- **Frequência de conversão:** Qual porcentagem de usuários indicou um amigo pelo menos três vezes após receber uma Campaign?

## Configurando relatórios de funil {#setting-up-funnel-reports}

![Relatório de funil 5]({% image_buster /assets/img/funnel_report/canvas_campaign.png %}){: style="float:right;max-width:40%;border:0;margin-left:15px;"}

Você pode executar relatórios de funil para Campaigns e Canvas ativos existentes. Esses relatórios mostram uma série de eventos pelos quais um destinatário de Campaign progride ao longo de 1 a 30 dias a partir da data em que entra no Canvas ou Campaign. Um usuário é considerado convertido em uma etapa do funil se realizar o evento na ordem especificada.

Os relatórios de funil estão disponíveis nos seguintes locais do dashboard:

- A página **Campaign Analytics** de uma Campaign específica
- A página **Canvas Details** de um Canvas específico, selecionando o botão **Analyze Variants**

{% alert important %}
Os relatórios de funil não estão disponíveis para [Campaigns da API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/api_campaigns).
{% endalert %}

### Etapa 1: Selecione um intervalo de datas {#step-1-select-a-date-range}

Você pode selecionar um período para seu relatório (dentro dos últimos seis meses) e refinar os dados para ver os usuários que, ao entrar na Campaign ou Canvas, completaram os eventos do funil dentro de um período definido (máximo de 30 dias). No exemplo a seguir, seu funil buscaria usuários que receberam essa Campaign ou Canvas nos últimos sete dias e completaram o funil em três dias.

{% alert note %}
Se você definir o período para completar o funil como um dia, o evento do funil deve ocorrer dentro de 24 horas após o recebimento da mensagem. No entanto, se você selecionar vários dias, o período é contado como dias corridos no fuso horário da empresa.
{% endalert %}

![Relatório de funil para um Canvas com "Últimos 7 dias" selecionado no menu suspenso de período.]({% image_buster /assets/img/funnel_report/funnel_report5.png %}){: style="max-width:90%;"}

### Etapa 2: Selecione eventos para as etapas do funil {#step-2-select-events-for-funnel-steps}

Para cada relatório de funil, o primeiro evento é quando o usuário recebe sua mensagem. A partir daí, os eventos subsequentes que você escolher afunilam o número de usuários que realizaram esses eventos, assim como os eventos anteriores.

#### Eventos disponíveis para relatórios de funil {#available-funnel-report-events}

| Campaign | Iniciou sessão, Realizou compra, Realizou evento personalizado, Evento de engajamento com mensagem |
| Canvas | Iniciou sessão, Realizou compra, Realizou evento personalizado, Recebeu etapa do Canvas, Interagiu com etapa |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Eventos disponíveis para relatórios de funil" }

{% alert note %}
O evento de relatório **Interagiu com etapa** só pode ser usado com etapas do Canvas que utilizam os canais de e-mail ou push.
{% endalert %}

![Relatório de funil para um Canvas com um menu suspenso dos eventos de relatório disponíveis.]({% image_buster /assets/img/funnel_report/funnel_report3.png %}){: style="max-width:80%;"}

Os relatórios de funil permitem comparar o sucesso de suas mensagens além dos eventos de conversão ou eventos de engajamento com mensagem que você configurou inicialmente. Então, se houver um evento de conversão que você não adicionou inicialmente, ainda é possível rastrear conversões para esse evento usando um funil.

Por exemplo, se você selecionar um período de relatório de 14 dias, seguido dos eventos `Added to cart` e `Made purchase`, verá tanto o número de usuários que adicionaram ao carrinho dentro de 14 dias após receber a mensagem quanto o número de usuários que adicionaram ao carrinho e depois realizaram uma compra dentro de 14 dias após receber a Campaign.

Como outro exemplo, você pode querer ver a porcentagem de usuários que converteram em um e-mail após clicar nele. Para calcular isso, você poderia criar um relatório onde o segundo evento é clicar no seu e-mail e o terceiro evento é realizar seu evento de conversão.

Após selecionar **Build Report**, o relatório de funil pode levar vários minutos para ser gerado. Durante esse tempo, você pode navegar para outras páginas no dashboard. Você receberá uma notificação no dashboard quando seu relatório estiver pronto.

## Interpretando seu relatório de funil {#interpreting-your-funnel-report}

No seu relatório de funil, você pode comparar diretamente o grupo de controle com as variantes que configurou. Cada evento consecutivo mostrará qual porcentagem dos usuários anteriores realizou aquela ação e converteu através do funil.

### Componentes do relatório de funil {#funnel-report-components}

- **Eixo horizontal**: Exibe a porcentagem de destinatários da mensagem que realizaram essas ações.
- **Gráfico**: Exibe o número de mensagens recebidas, o número de usuários que realizaram as ações anteriores, assim como a ação que você escolheu, a taxa de conversão e a variação percentual em relação ao controle.
- **Opção de regeneração**: Permite regenerar seu relatório e indica quando o relatório atual foi gerado pela última vez.
- **Variantes**: Representadas por colunas coloridas, o relatório de funil permite até 8 variantes e um grupo de controle. Por padrão, o **gráfico** mostrará apenas três variantes. Para ver mais, você pode selecionar manualmente as demais variantes.

![Gráfico do relatório de funil.]({% image_buster /assets/img/funnel_report/funnel_report4.jpg %})

**Para Campaigns com múltiplas variantes**: a Braze mostrará uma tabela com métricas para cada evento e variante e a variação percentual em relação ao controle. A taxa de conversão é o número de usuários que realizaram o evento (e os subsequentes) por destinatário da mensagem.

**Para Campaigns com reelegibilidade**: Se um usuário receber a Campaign mais de uma vez no período do relatório, a Braze determinará se o usuário deve ser incluído no funil com base nas ações que esse usuário realizou após a primeira vez que recebeu a Campaign dentro do período.
- Observe que pode haver uma discrepância entre os valores de conversão do funil e os valores de conversão padrão, pois os usuários podem converter mais de uma vez com reelegibilidade, mas os relatórios de funil converterão no máximo uma vez, mesmo que um usuário realize o evento mais de uma vez.

**Para Campaigns multivariantes com reelegibilidade**: Se um usuário receber múltiplas variantes da Campaign durante o período do relatório, a Braze determinará se ele deve ser incluído no funil da variante com base nas ações que esse usuário realizou após a primeira vez que recebeu a variante da Campaign. Isso significa que o mesmo usuário pode ser contado em múltiplas variantes diferentes se tiver recebido múltiplas variantes durante o período do funil.

{% alert important %}
Usuários órfãos não são rastreados nos relatórios de funil. Quando um usuário anônimo entra em um Canvas ou Campaign e posteriormente se torna identificado através do método `changeUser()`, seu ID da Braze muda. Os relatórios de funil rastreiam apenas eventos subsequentes que correspondem ao ID do usuário no momento da entrada e não consideram eventos realizados pelo usuário após a mudança de ID. Isso significa que eventos de conversão realizados pelo usuário após se tornar identificado não serão incluídos no relatório de funil.
{% endalert %}

## Perguntas frequentes {#frequently-asked-questions}

### Um usuário sai do relatório se pular um evento? {#does-a-user-fall-out-of-the-report-if-they-skip-an-event}

Sim. Um usuário sai do funil na primeira etapa em que não realiza o próximo evento na sequência exata que você configurou.

### Quantos eventos posso incluir em um relatório de funil? {#how-many-events-can-i-include-in-a-funnel-report}

Não há um limite rígido, mas de quatro a seis eventos cobre a maioria dos casos de uso. Funis muito longos podem ficar lentos ou expirar.

### Quais canais suportam o evento de funil **Interagiu com etapa**? {#what-channels-support-the-interacted-with-step-funnel-event}

**Interagiu com etapa** está disponível para etapas do Canvas que usam os canais de **e-mail** ou **push**.

### Por que meu relatório de funil está demorando para carregar? {#why-is-my-funnel-report-taking-a-long-time-to-load}

Consultas grandes podem expirar. Tente um período de relatório mais curto, menos etapas de funil, ou ambos.

### Por que a análise de dados no Canvas é diferente do relatório de funil? {#why-are-the-analytics-on-the-canvas-different-from-the-funnel-report}

A análise de dados das etapas do Canvas pode mostrar contagens mais altas do que o funil para as mesmas datas, porque a análise de dados das etapas inclui engajamento e conversões mais amplos, enquanto o funil aplica regras de ordem e tempo dos eventos.

#### Análise de dados do Canvas (Analyze Variants) {#canvas-analytics-analyze-variants}

O intervalo de datas filtra eventos por **quando ocorreram**. Se você selecionar 1 a 7 de janeiro, verá todas as entradas e eventos de conversão que aconteceram durante esse período, independentemente de quando o usuário entrou no Canvas. Um usuário que entrou em 1º de janeiro mas converteu em 8 de janeiro mostraria uma entrada e zero conversões, porque a conversão ficou fora das datas selecionadas. A janela de conversão configurada na etapa do Canvas pode se estender além do período máximo de acompanhamento do funil, então a análise de dados no nível da etapa pode capturar conversões em um horizonte mais longo.

#### Relatórios de funil

O intervalo de datas filtra usuários por **quando entraram** no Canvas. Se você selecionar 1 a 7 de janeiro, o relatório inclui todos os usuários que entraram durante esse período e então rastreia suas ações pelo período de conclusão do funil que você configurar (até 30 dias após a entrada). O mesmo usuário que entrou em 1º de janeiro e converteu em 8 de janeiro mostraria uma entrada e uma conversão, porque a conversão aconteceu dentro do período pós-entrada.

Além disso, os relatórios de funil exigem que os eventos ocorram na ordem especificada e contam cada usuário no máximo uma vez, enquanto a análise de dados do Canvas conta todas as conversões e engajamento sem restrição de ordem.