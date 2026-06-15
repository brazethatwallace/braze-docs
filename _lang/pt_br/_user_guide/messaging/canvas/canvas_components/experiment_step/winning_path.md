---
nav_title: Jornada vencedora
article_title: Jornada vencedora nas Jornadas do experimento
page_type: reference
description: "Este artigo de referência aborda a Jornada vencedora, um recurso que permite automatizar seus testes A/B quando ativado em uma etapa de Jornadas do experimento."
tool: Canvas
---

# Jornada vencedora nas Jornadas do experimento

> A Jornada vencedora é semelhante à [Variante vencedora]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations/) em campanhas e permite automatizar seus testes A/B.

Quando a Jornada vencedora está ativada em uma etapa de Jornadas do experimento, após um período especificado, todos os usuários subsequentes são enviados pela jornada com a maior taxa de conversão.

## Usando a Jornada vencedora

### Etapa 1: Adicionar uma etapa de Jornadas do experimento

Adicione uma [Jornada do experimento]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/) ao seu Canvas e ative a **Jornada vencedora**.

![Configurações na Jornada do experimento intitulada "Distribuir usuários subsequentes para a Jornada vencedora". A seção inclui um botão de alternância para Jornada vencedora e opções para configurar o evento de conversão e o período do experimento.]({% image_buster /assets/img/experiment_step/experiment_winning_path_recurring.png %})

### Etapa 2: Definir as configurações da Jornada vencedora

Especifique o evento de conversão que deve determinar o vencedor. Se não houver eventos de conversão disponíveis, volte à primeira etapa da configuração do Canvas e [atribua eventos de conversão]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#choose-conversion-events).

Se você escolher aberturas ou cliques como evento de conversão, certifique-se de que a primeira etapa na jornada seja uma [etapa de Mensagem]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/). A Braze conta apenas o engajamento da primeira etapa de Mensagem em cada jornada respectiva. Se a jornada começar com uma etapa diferente (como uma etapa de Postergação ou Jornada do público) e a mensagem vier depois, essa mensagem não será incluída na avaliação de performance.

Em seguida, defina o **Período do experimento**. O **Período do experimento** especifica por quanto tempo o experimento será executado antes que a Jornada vencedora seja determinada e todos os usuários subsequentes sejam enviados por essa jornada. O período começa quando o primeiro usuário entra na etapa.

![Configurações da Jornada vencedora com o evento de conversão "Cliques" selecionado para um período de experimento de 12 horas.]({% image_buster /assets/img/experiment_step/experiment_winning_settings.png %})

### Etapa 3: Determinar o fallback {#statistical-significance}

Por padrão, se os resultados do teste não forem suficientes para determinar um vencedor estatisticamente significativo, todos os usuários futuros são enviados pela jornada com melhor performance. Como alternativa, você pode selecionar **Continuar enviando todos os usuários futuros pela combinação de jornadas**. Essa opção envia os usuários futuros pela combinação de jornadas de acordo com as porcentagens especificadas na distribuição da jornada do experimento.

Em caso de empate, a Braze seleciona a jornada que aparece primeiro.

!["Continuar enviando todos os usuários futuros pela combinação de jornadas" selecionado como o que acontece com os usuários se o resultado do teste não for estatisticamente significativo.]({% image_buster /assets/img/experiment_step/experiment_winning_statistical.png %})

{% alert note %}
Um Grupo de postergação aparece na distribuição de jornadas somente se o seu Canvas estiver configurado para entrada única e a etapa de Experimento tiver três jornadas ou menos. Canvas recorrentes e disparados não possuem um Grupo de postergação quando a Jornada vencedora está ativada.
{% endalert %}

### Etapa 4: Adicionar suas jornadas e lançar o Canvas

Um único componente de Jornada do experimento pode conter até quatro jornadas. No entanto, se o seu Canvas estiver configurado para [entrada única](#one-time-entry), uma jornada deve ser reservada para o Grupo de postergação que a Braze adiciona automaticamente quando a Jornada vencedora está ativada. Isso significa que, para Canvas com entrada única, você pode adicionar até três jornadas ao seu experimento.

Finalize a configuração do seu Canvas conforme necessário e lance-o. Quando o primeiro usuário entrar no experimento, você pode verificar o Canvas para acompanhar a análise de dados à medida que chegam e [rastrear a performance do seu experimento]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step#tracking-performance).

Após a conclusão de uma Jornada vencedora, todos os usuários subsequentes que entrarem no Canvas seguem pela Jornada vencedora, incluindo usuários que reentraram e estavam anteriormente no grupo de controle da etapa de Jornadas do experimento.

## Análise de dados {#analytics}

Se a Jornada vencedora estiver ativada, sua visualização de análise de dados é separada em duas guias: **Experimento inicial** e **Jornada vencedora**.

- **Experimento inicial:** Mostra as métricas de cada jornada durante o período do experimento, qual jornada foi selecionada como vencedora e as métricas de conversão do Canvas. O evento de conversão usado para escolher o vencedor, configurado nas configurações da Jornada vencedora, pode não ser o mesmo que a métrica de conversão destacada na análise de dados do Canvas. Para saber mais sobre como a análise de dados das Jornadas do experimento se relaciona com os eventos de conversão do Canvas e a métrica vencedora, consulte [Jornadas do experimento]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#winning-path-and-personalized-paths-performance).
- **Jornada vencedora:** Mostra apenas as métricas da Jornada vencedora a partir do momento em que o Experimento inicial foi concluído.

## Informações importantes

### Entrada única {#one-time-entry}

Ao usar Jornadas vencedoras em um Canvas onde os usuários podem entrar apenas uma vez, um Grupo de postergação é incluído automaticamente. Durante a duração do experimento, uma porcentagem de usuários é mantida no Grupo de postergação enquanto os demais entram nas suas Jornadas do experimento.

![Etapa de Experimento com um Grupo de postergação para Jornada vencedora]({% image_buster /assets/img/experiment_step/experiment_one_time.png %}){: style="max-width:75%"}

Quando o teste termina e uma Jornada vencedora é determinada, os usuários atribuídos ao Grupo de postergação são direcionados para a jornada escolhida e continuam pelo Canvas.

![Etapa de Experimento com um Grupo de postergação enviado pela Jornada vencedora]({% image_buster /assets/img/experiment_step/experiment_one_time_results.png %}){: style="max-width:75%"}

### Entrega no horário local

Não recomendamos usar a entrega no horário local em Canvas com Jornadas vencedoras. Isso porque os períodos de experimento começam quando o primeiro usuário passa pela etapa. Usuários em fusos horários muito adiantados podem entrar na etapa e acionar o início do período do experimento muito antes do esperado. Isso pode fazer com que o experimento seja concluído antes que a maioria dos seus usuários em fusos horários mais comuns tenha tido tempo suficiente para entrar no Canvas, converter, ou ambos.

Como alternativa, se você deseja usar a entrega no horário local, use um período de experimento de 24 a 48 horas ou mais. Dessa forma, os usuários em fusos horários adiantados entram no Canvas e acionam o início do experimento, mas ainda resta bastante tempo no período do experimento. Os usuários em fusos horários mais atrasados ainda terão tempo suficiente para entrar no Canvas e na etapa de Experimento com Jornadas vencedoras e possivelmente converter antes que o período do experimento expire.

### Variantes baseadas em cliques

Se você estiver configurando uma variante de Jornada vencedora baseada em cliques, observe que as definições de aberturas e cliques diferem por canal. Para métricas e definições específicas por canal, consulte o [Glossário de métricas de relatório]({{site.baseurl}}/user_guide/analytics/reporting/report_metrics) e o [Glossário de métricas de relatório de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary).