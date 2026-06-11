---
nav_title: Jornadas do experimento
article_title: Jornadas do experimento
alias: /experiment_step/
page_order: 4
page_type: reference
description: "Este artigo aborda as Jornadas do experimento, um componente que permite testar múltiplas jornadas do Canvas entre si e contra um grupo de controle em qualquer ponto da jornada do usuário."
tool: Canvas
---

# Jornadas do experimento {#experiment-paths}

> As Jornadas do experimento permitem testar múltiplas jornadas do Canvas entre si e contra um grupo de controle em qualquer ponto da jornada do usuário. Com esse componente, você pode acompanhar o desempenho de cada jornada para tomar decisões informadas sobre sua jornada no Canvas.

Quando você inclui uma etapa de Jornadas do experimento na jornada do usuário, ela atribui aleatoriamente os usuários a diferentes jornadas (ou a um grupo de controle opcional) que você criar. Partes do público serão atribuídas a diferentes jornadas de acordo com as porcentagens que você selecionar, permitindo testar diferentes mensagens ou jornadas entre si e determinar qual é a mais eficaz.

![Uma etapa de Jornada do experimento que se divide em Jornada 1, Jornada 2 e Controle.]({% image_buster /assets/img/experiment_step/experiment_step.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

## Pré-requisitos {#prerequisites}

Para usar as Jornadas do experimento, seu Canvas deve incluir eventos de conversão. Embora não seja possível adicionar eventos de conversão após o lançamento de um Canvas, você pode clonar o Canvas lançado e adicionar eventos de conversão para incluir Jornadas do experimento.

## Casos de uso {#use-cases}

As Jornadas do experimento são mais adequadas para testar entrega, cadência, texto da mensagem e combinações de canais.

- **Entrega:** Compare os resultados entre mensagens enviadas com diferentes [postergações]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step/), com base em ações do usuário ([Jornadas de ação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths/)) e usando [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/#canvas).<br><br>
- **Cadência:** Teste múltiplos fluxos de envio de mensagens durante um período específico. Por exemplo, você pode testar duas cadências de integração diferentes:
    - Cadência 1: Enviar 2 mensagens nas primeiras 2 semanas do usuário
    - Cadência 2: Enviar 3 mensagens nas primeiras 2 semanas do usuário

    Ao direcionar usuários inativos, você pode testar a eficácia de enviar duas mensagens de recuperação em uma semana em comparação com enviar apenas uma.
- **Texto da mensagem:** Semelhante a um [teste A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/) padrão, você pode testar diferentes textos de mensagem para ver qual redação resulta em uma taxa de conversão mais alta.<br><br>
- **Combinações de canais:** Teste a eficácia de diferentes combinações de canais de mensagem. Por exemplo, você pode comparar o impacto de usar apenas um e-mail versus um e-mail combinado com um push.

## Criando uma jornada experimental {#creating-an-experiment-path}

Para criar um componente de Jornadas do experimento, primeiro adicione uma etapa ao seu Canvas. Arraste e solte o componente da barra lateral, ou clique no botão de mais <i class="fas fa-plus-circle"></i> na parte inferior de uma etapa e selecione **Experiment Paths**.

Na configuração padrão desse componente, existem duas jornadas padrão, **Path 1** e **Path 2**, com 50% do público sendo enviado por cada jornada. Clique no componente para expandir o painel **Experiment Settings** e você verá as opções de configuração do componente.

### Etapa 1: Escolha o número de jornadas e a distribuição do público {#step-1-choose-the-number-of-paths-and-audience-distribution}

Você pode adicionar até quatro jornadas clicando em **Add Path** e um grupo de controle opcional marcando **Add a Control Group**. Usando as caixas de porcentagem para cada jornada, você pode especificar a porcentagem do público que deve seguir por cada jornada e pelo grupo de controle. As porcentagens fornecidas devem somar 100% para prosseguir. Se quiser definir rapidamente todas as jornadas disponíveis (e o controle) com a mesma porcentagem, clique em **Distribute Paths Evenly**.

Você também pode escolher se os usuários no grupo de controle devem continuar no Canvas ou sair após a janela de rastreamento de conversão em **Control Group Behavior**. Opcionalmente, você pode adicionar uma descrição para explicar a outros o que essa jornada experimental pretende testar ou incluir informações adicionais que possam ser úteis.

![Configurações do experimento onde você pode adicionar jornadas e distribuir a porcentagem de usuários em cada jornada.]({% image_buster /assets/img/experiment_step/exp_settings.png %})

{% alert note %}
Se a reelegibilidade do Canvas estiver ativada, os usuários que entrarem no Canvas e seguirem por uma jornada escolhida aleatoriamente seguirão pela mesma jornada novamente se se tornarem reelegíveis e reentrarem no Canvas. Isso mantém a validade do experimento e da análise de dados associada. Se você quiser que a etapa sempre randomize a atribuição de jornada, selecione **Randomized Paths in Experiment Paths**. Essa opção não está disponível ao usar Jornada vencedora ou Jornadas personalizadas.
{% endalert %}

### Etapa 2: Ative a Jornada vencedora ou as Jornadas personalizadas (opcional) {#step-2}

Você pode otimizar seu experimento ativando a [Jornada vencedora]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/winning_path/) ou as [Jornadas personalizadas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/personalized_paths/). Ambas as opções funcionam testando inicialmente suas jornadas com uma parte do seu público. Após o término do experimento, os usuários restantes e subsequentes são enviados pela jornada com melhor desempenho geral (Jornada vencedora) ou pela jornada com melhor desempenho para cada usuário (Jornadas personalizadas).

### Etapa 3: Crie as jornadas {#step-3-create-paths}

Por fim, você deve construir suas jornadas subsequentes. Selecione **Done** e retorne ao construtor do Canvas. Clique no botão de mais <i class="fas fa-plus-circle"></i> abaixo de cada jornada para começar a criar jornadas usando as ferramentas habituais do Canvas como preferir, e lance o Canvas quando estiver pronto.

![Adicionando etapas a cada jornada que se divide a partir de um componente de Jornada do experimento.]({% image_buster /assets/img/experiment_step/experiment_downstream_paths.gif %}){: style="max-width:75%"}

Tenha em mente que as jornadas e suas etapas subsequentes não podem ser removidas de um Canvas após serem criadas. No entanto, após o lançamento, você pode modificar a distribuição do público entre as jornadas como preferir. Por exemplo, se um dia após o lançamento de um Canvas você concluir que uma jornada é superior às demais com base na análise de dados, pode definir essa jornada como 100% e as outras como 0%. Ou, dependendo das suas necessidades, pode continuar enviando usuários por múltiplas jornadas.

{% alert important %}
Para evitar contaminação do experimento, se o seu Canvas tiver um experimento ativo ou em andamento de Jornada vencedora ou Jornadas personalizadas e você atualizar o Canvas ativo, independentemente de atualizar a própria etapa da Jornada do experimento, o experimento em andamento será encerrado e a etapa do experimento não determinará uma jornada vencedora ou jornadas personalizadas. Para reiniciar o experimento, você pode desconectar a Jornada do experimento existente e lançar uma nova, ou duplicar o Canvas e lançar um novo Canvas. Caso contrário, os usuários fluirão pela jornada experimental como se nenhum método de otimização tivesse sido selecionado. Você também não pode ativar Jornadas personalizadas ou Jornada vencedora para um Canvas já ativo com uma etapa de Jornada do experimento.<br><br>Para saber mais, consulte [Editando Canvas após o lançamento]({{site.baseurl}}/post-launch_edits/).
{% endalert %}

## Acompanhando o desempenho {#tracking-performance}

Na página **Canvas Analytics**, selecione a Jornada do experimento para abrir uma [tabela detalhada]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch/#performance-breakdown-by-variant) idêntica à guia **Analyze Variants** para comparar estatísticas detalhadas de desempenho e conversão entre as jornadas. Você também pode exportar a tabela via CSV e comparar as variações percentuais para métricas de interesse em relação à jornada ou ao controle que você selecionar.

Cada etapa em cada jornada exibe estatísticas na visualização de [Canvas Analytics]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/), assim como qualquer etapa do Canvas. No entanto, tenha em mente que a análise de dados de etapas individuais e a análise de dados da Jornada do experimento medem conversões de forma diferente:

- **Análise de dados da Jornada do experimento** rastreia conversões a partir do momento em que o usuário entra na etapa da Jornada do experimento. Essa é a visualização recomendada para comparar o desempenho entre jornadas, pois todas as jornadas compartilham o mesmo ponto de partida.
- **Análise de dados de etapas individuais** (como análise de dados da etapa de Mensagem) rastreia conversões a partir do momento em que o usuário recebe aquela etapa específica (por exemplo, quando a mensagem é enviada).

Como essas janelas de conversão têm pontos de partida diferentes, elas podem mostrar taxas de conversão diferentes para a mesma jornada — especialmente quando há postergações entre a etapa do experimento e uma mensagem subsequente. Para a comparação mais confiável entre jornadas, use a análise de dados da Jornada do experimento.

### Desempenho da Jornada vencedora e das Jornadas personalizadas {#winning-path-and-personalized-paths-performance}

Aproveite a Jornada vencedora para acompanhar o desempenho ao longo de um período e, em seguida, enviar automaticamente os usuários subsequentes pela jornada com melhor desempenho. Para saber mais sobre a análise de dados quando a **Jornada vencedora** ou as **Jornadas personalizadas** estão ativadas para seu experimento, consulte:

- [Jornada vencedora]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/winning_path/#analytics)
- [Jornadas personalizadas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/personalized_paths/#analytics)

A métrica vencedora e a análise de dados exibida nas Jornadas do experimento podem diferir:

- O evento de conversão que você configura para a **Jornada vencedora** ou as **Jornadas personalizadas** determina como a Braze compara as jornadas e seleciona uma vencedora durante a janela do experimento.
- A análise de dados da Jornada do experimento ainda segue o mesmo framework de [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) do Canvas como o restante do Canvas, incluindo seu [evento de conversão primária]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/#primary-conversion-event). Como resultado, as métricas destacadas no dashboard podem não corresponder à métrica vencedora.
- Para push, *aberturas diretas* e *total de aberturas* diferem. Para saber mais, consulte [Aberturas por influência]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens/).

### Configurações adicionais {#additional-settings}

As Jornadas do experimento registram os usuários que entram em cada etapa e convertem enquanto estão na jornada atribuída. Isso rastreia todos os eventos de conversão especificados na configuração do Canvas. Na guia **Additional Settings**, insira quantos dias (entre 1 e 30) você deseja que este experimento rastreie conversões. A janela de tempo que você especificar aqui determina por quanto tempo os eventos de conversão (escolhidos na configuração do Canvas) são rastreados para o experimento. As janelas de conversão por evento especificadas na configuração do Canvas não se aplicam ao rastreamento desta etapa e são substituídas por esta janela de conversão.

A janela de conversão começa quando o usuário entra na etapa da Jornada do experimento, não quando uma mensagem subsequente é enviada. Se uma jornada incluir postergações — como uma etapa de postergação ou [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/) — essas postergações consomem parte da janela de conversão.

{% alert important %}
Se você estiver usando Intelligent Timing em uma etapa de Mensagem dentro de uma jornada experimental, o tempo entre a entrada no experimento e o envio real da mensagem reduz a janela de conversão efetiva para essa jornada. Por exemplo, se seu experimento tem uma janela de conversão de 5 dias e o Intelligent Timing atrasa a mensagem em 2 dias, os usuários nessa jornada têm apenas 3 dias após receber a mensagem para converter dentro da janela do experimento — mesmo que a análise de dados da própria etapa de Mensagem rastreie conversões a partir do momento do envio da mensagem.<br><br>Para uma análise de dados do experimento mais limpa, coloque quaisquer postergações (como etapas de postergação) **antes** da etapa da Jornada do experimento, em vez de dentro de uma jornada experimental. Dessa forma, todas as jornadas começam do mesmo ponto e as postergações não consomem nenhuma parte da janela de conversão.
{% endalert %}

## Perguntas frequentes {#frequently-asked-questions}

### Por que os envios diferem entre jornadas quando a divisão do experimento parece equilibrada? {#why-do-sends-differ-across-paths-when-the-experiment-split-looks-even}

Os _envios_ subsequentes dependem das etapas de cada jornada, postergações, elegibilidade de canal e conteúdo, não apenas da divisão percentual na Jornada do experimento. Por exemplo, postergações diferentes, horários de envio inteligente ou status de inscrição podem alterar quantos usuários recebem uma mensagem, mesmo quando a atribuição de jornada estava equilibrada. Para comparar os resultados das jornadas, use a [análise de dados da Jornada do experimento](#tracking-performance), que mede conversões a partir de um ponto de entrada comum.

### Quanto tempo dura a janela de conversão do experimento? {#how-long-does-the-experiment-conversion-window-last}

A janela de conversão em **Additional Settings** (de 1 a 30 dias) começa quando o usuário entra na etapa da Jornada do experimento. O tempo gasto em etapas de postergação subsequentes ou aguardando o Intelligent Timing conta contra essa janela. Consulte [Acompanhando o desempenho](#tracking-performance) para mais detalhes.