---
nav_title: Jornada vencedora
article_title: Jornada vencedora nas jornadas experimentais
page_type: reference
description: "Este artigo de referência aborda a Jornada vencedora, um recurso que permite automatizar seus testes A/B quando ativado em uma etapa de jornada experimental."
tool: Canvas
---

# Jornada vencedora nas jornadas experimentais {#winning-path-in-experiment-paths}

> A Jornada vencedora testa automaticamente as jornadas do Canvas e envia os usuários subsequentes pela jornada com melhor desempenho.

Quando a Jornada vencedora está ativada em uma etapa de jornada experimental, após um período especificado, todos os usuários subsequentes são enviados pela jornada com a maior taxa de conversão.

## Usando a Jornada Vencedora {#using-winning-path}

### Etapa 1: Adicionar uma etapa de jornada experimental {#step-1-add-an-experiment-path-step}

Adicione uma [jornada experimental]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) ao seu Canvas e ative a **Jornada Vencedora**.

![Configurações na jornada experimental intitulada "Distribuir usuários subsequentes para a Jornada Vencedora". A seção inclui um botão de alternância para Jornada Vencedora e opções para configurar o evento de conversão e a janela do experimento.]({% image_buster /assets/img/experiment_step/experiment_winning_path_recurring.png %})

### Etapa 2: Definir as configurações da Jornada Vencedora {#step-2-configure-winning-path-settings}

Especifique o evento de conversão que determinará o vencedor. Se não houver eventos de conversão disponíveis, volte à primeira etapa de configuração do Canvas e [atribua eventos de conversão]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#choose-conversion-events).

Se você escolher aberturas ou cliques como evento de conversão, certifique-se de que a primeira etapa da jornada seja uma [etapa de mensagem]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step). A Braze conta apenas o engajamento da primeira etapa de mensagem em cada jornada correspondente. Se a jornada começar com uma etapa diferente (como uma etapa de postergação ou jornada do público) e a mensagem vier depois, essa mensagem não será incluída na avaliação de desempenho.

Em seguida, defina a **Janela do Experimento**. A **Janela do Experimento** especifica por quanto tempo o experimento é executado antes que a Jornada Vencedora seja determinada e todos os usuários seguintes sejam enviados por essa jornada. A janela começa quando o primeiro usuário entra na etapa.

![Configurações da Jornada Vencedora com o evento de conversão "Cliques" selecionado para uma janela de experimento de 12 horas.]({% image_buster /assets/img/experiment_step/experiment_winning_settings.png %})

### Etapa 3: Determinar o fallback {#statistical-significance}

Por padrão, se os resultados do teste não forem suficientes para determinar um vencedor com significância estatística, todos os usuários futuros serão enviados pela jornada com melhor desempenho. Como alternativa, você pode selecionar **Continuar enviando todos os usuários futuros pela combinação de jornadas**. Essa opção envia os usuários futuros pela combinação de jornadas de acordo com as porcentagens especificadas na distribuição da jornada experimental.

Em caso de empate, a Braze seleciona a jornada que aparece primeiro.

!["Continuar enviando todos os usuários futuros pela combinação de jornadas" selecionado como o que acontece com os usuários se o resultado do teste não tiver significância estatística.]({% image_buster /assets/img/experiment_step/experiment_winning_statistical.png %})

{% alert note %}
Um grupo de postergação aparece na distribuição de jornadas apenas se o seu Canvas estiver configurado para entrada única e a etapa de experimento tiver três jornadas ou menos. Canvas recorrentes e disparados não possuem grupo de postergação quando a Jornada Vencedora está ativada.
{% endalert %}

### Etapa 4: Adicionar suas jornadas e lançar o Canvas {#step-4-add-your-paths-and-launch-the-canvas}

Um único componente de jornada experimental pode conter até quatro jornadas. No entanto, se o seu Canvas estiver configurado para [entrada única](#one-time-entry), uma jornada precisa ser reservada para o grupo de postergação que a Braze adiciona automaticamente quando a Jornada Vencedora é ativada. Isso significa que, para Canvas com entrada única, você pode adicionar até três jornadas ao seu experimento.

Finalize a configuração do seu Canvas conforme necessário e, em seguida, lance-o. Quando o primeiro usuário entrar no experimento, você poderá verificar o Canvas para ver a análise de dados conforme os resultados chegam e [acompanhar o desempenho do experimento]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step#tracking-performance).

Após a conclusão de uma Jornada Vencedora, todos os usuários subsequentes que entrarem no Canvas seguirão pela Jornada Vencedora, incluindo usuários que reentraram e estavam anteriormente no grupo de controle da etapa de jornada experimental.

## Análise de dados {#analytics}

Se a Jornada vencedora estiver ativada, sua visualização de análise de dados é separada em duas guias: **Experimento inicial** e **Jornada vencedora**.

- **Experimento inicial:** Mostra as métricas de cada jornada durante o período do experimento, qual jornada foi selecionada como vencedora e as métricas de conversão do Canvas. O evento de conversão usado para escolher o vencedor, configurado nas configurações da Jornada vencedora, pode não ser o mesmo que a métrica de conversão destacada na análise de dados do Canvas. Para saber mais sobre como a análise de dados das Jornadas do experimento se relaciona com os eventos de conversão do Canvas e a métrica vencedora, consulte [Jornadas do experimento]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step#winning-path-and-personalized-paths-performance).
- **Jornada vencedora:** Mostra apenas as métricas da Jornada vencedora a partir do momento em que o Experimento inicial foi concluído.

## O que saber {#things-to-know}

### Entrada única {#one-time-entry}

Ao usar jornadas vencedoras em um Canvas onde os usuários podem entrar apenas uma vez, um grupo de postergação é incluído automaticamente. Durante a duração do experimento, uma porcentagem de usuários é mantida no grupo de postergação enquanto os demais entram nas suas jornadas experimentais.

![Etapa de experimento com um grupo de postergação para jornada vencedora]({% image_buster /assets/img/experiment_step/experiment_one_time.png %}){: style="max-width:75%"}

Quando o teste termina e uma jornada vencedora é determinada, os usuários atribuídos ao grupo de postergação são direcionados para a jornada escolhida e continuam pelo Canvas.

![Etapa de experimento com um grupo de postergação enviado pela jornada vencedora]({% image_buster /assets/img/experiment_step/experiment_one_time_results.png %}){: style="max-width:75%"}

### Entrega no horário local {#local-time-delivery}

Não recomendamos o uso de entrega no horário local em Canvas com jornadas vencedoras. Isso porque as janelas de experimento começam quando o primeiro usuário passa pela etapa. Usuários que estão em fusos horários muito adiantados podem entrar na etapa e disparar o início da janela de experimento muito antes do esperado, o que pode fazer com que o experimento termine antes que a maior parte dos seus usuários em fusos horários mais comuns tenha tido tempo suficiente para entrar no Canvas, converter, ou ambos.

Como alternativa, se você quiser usar entrega no horário local, use uma janela de experimento de 24 a 48 horas ou mais. Dessa forma, os usuários em fusos horários adiantados entram no Canvas e disparam o início do experimento, mas ainda resta bastante tempo na janela de experimento. Os usuários em fusos horários posteriores ainda terão tempo suficiente para entrar no Canvas e na etapa de experimento com jornadas vencedoras e possivelmente converter antes que a janela de experimento expire.

### Variantes baseadas em cliques {#variants-based-on-clicks}

Se você está configurando uma variante de jornada vencedora com base em cliques, observe que as definições de aberturas e cliques variam por canal. Para métricas e definições específicas por canal, consulte o [Glossário de métricas de relatório]({{site.baseurl}}/user_guide/analytics/metrics_glossary) e o [Glossário de métricas de relatório de e-mail]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary).