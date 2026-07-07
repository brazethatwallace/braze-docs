---
nav_title: Jornadas personalizadas
article_title: Jornadas personalizadas em Jornadas do experimento
page_type: reference
description: "As Jornadas personalizadas permitem personalizar qualquer ponto de uma jornada do Canvas para usuários individuais com base na probabilidade de conversão."
tool: Canvas
---

# Jornadas personalizadas em Jornadas do experimento {#personalized-paths-in-experiment-paths}

> As Jornadas personalizadas são semelhantes à [Variante personalizada]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations#personalized-variant) em Campaigns e permitem personalizar qualquer ponto de uma jornada do Canvas para usuários individuais com base na probabilidade de conversão.

## Como as Jornadas personalizadas funcionam {#how-personalized-paths-works}

Quando as Jornadas personalizadas estão ativadas em uma etapa de Jornada do experimento, o comportamento é ligeiramente diferente dependendo se o Canvas está configurado para envio único ou recorrente:

- **Canvas de envio único:** Um grupo de usuários é retido em um grupo de postergação. Os usuários restantes passam por um teste inicial para treinar um modelo preditivo durante um período que você configura — pelo menos 24 horas para melhores resultados. Após o teste, um modelo é criado para identificar quais comportamentos dos usuários estavam associados a uma maior probabilidade de conversão em uma determinada jornada. Por fim, cada usuário no grupo de postergação é enviado pela jornada com maior probabilidade de resultar em conversão para ele, com base nos comportamentos que apresenta e no que o modelo preditivo aprendeu durante o teste inicial.
- **Canvas recorrentes, disparados por ação e disparados por API:** Um experimento inicial é realizado com todos os usuários que entram na Jornada do experimento durante um período especificado. Para manter a integridade do experimento, se um usuário receber várias mensagens antes do fim do período, ele será atribuído à mesma variante todas as vezes. Após o período do experimento, cada usuário é enviado pela jornada com maior probabilidade de resultar em conversão para ele.

## Usando Jornadas personalizadas {#using-personalized-paths}

### Etapa 1: Adicionar uma Jornada do experimento {#step-1-add-an-experiment-path}

Adicione uma [Jornada do experimento]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) ao seu Canvas e ative **Jornadas personalizadas**.

![Adicione uma Jornada do experimento ao seu Canvas e ative Jornadas personalizadas.]({% image_buster /assets/img/experiment_step/experiment_personalized_path.png %})

### Etapa 2: Configurar as definições de Jornadas personalizadas {#step-2-configure-personalized-paths-settings}

Especifique o evento de conversão que deve determinar o vencedor. Se não houver eventos de conversão disponíveis, volte à primeira etapa da configuração do Canvas e [atribua eventos de conversão]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#choose-conversion-events).

Se você escolher aberturas ou cliques como evento de conversão, certifique-se de que a primeira etapa na jornada seja uma [etapa de Mensagem]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step). A Braze só contabiliza o engajamento da primeira etapa de Mensagem em cada jornada respectiva. Se a jornada começar com uma etapa diferente (como uma etapa de Postergação ou Jornada do público) e a mensagem vier depois, essa mensagem não será incluída na avaliação de desempenho.

Em seguida, defina o **Período do experimento**. O **Período do experimento** determina por quanto tempo os usuários serão enviados por todas as jornadas antes de escolher a melhor jornada para cada usuário no grupo de postergação. O período começa quando o primeiro usuário entra na etapa.

![Captura de tela relacionada à etapa 2: configurar as definições de Jornadas personalizadas.]({% image_buster /assets/img/experiment_step/experiment_personalized_settings.png %})

### Etapa 3: Determinar o fallback {#step-3-determine-fallback}

Por padrão, se os resultados do teste não forem suficientes para determinar um vencedor estatisticamente significativo, todos os usuários futuros serão enviados pela jornada com melhor desempenho geral.

Alternativamente, você pode selecionar **Continuar enviando todos os usuários futuros pela combinação de jornadas**.

![Alternativamente, você pode selecionar Continuar enviando todos os usuários futuros pela combinação de jornadas.]({% image_buster /assets/img/experiment_step/experiment_winning_statistical.png %})

Essa opção enviará os usuários futuros pela combinação de jornadas de acordo com as porcentagens especificadas na distribuição da jornada do experimento.

![Captura de tela relacionada à etapa 3: determinar o fallback.]({% image_buster /assets/img/experiment_step/experiment_personalized_percentages.png %})

### Etapa 4: Adicionar suas jornadas e lançar o Canvas {#step-4-add-your-paths-and-launch-the-canvas}

{% tabs local %}
{% tab Canvas de envio único %}

Um único componente de Jornada do experimento pode conter até quatro jornadas. No entanto, para Canvas de envio único, você pode adicionar até três jornadas quando as Jornadas personalizadas estão ativadas. A quarta jornada deve ser reservada para o Grupo de postergação que a Braze adiciona automaticamente ao seu experimento.

Termine de configurar seu Canvas conforme necessário e lance-o. Quando o primeiro usuário entrar no experimento, você pode verificar o Canvas para ver a análise de dados conforme eles chegam e [acompanhar o desempenho do seu experimento]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step#tracking-performance).

![Captura de tela relacionada à etapa 4: adicionar suas jornadas e lançar o Canvas.]({% image_buster /assets/img/experiment_step/experiment_personalized_delay_group_pending.png %}){: style="max-width:75%;" }

Quando o período do experimento passar e o experimento estiver concluído, a Braze enviará os usuários no grupo de postergação para suas respectivas jornadas com a maior probabilidade personalizada de conversão, com base na recomendação do modelo preditivo.

![Captura de tela relacionada à etapa 4: adicionar suas jornadas e lançar o Canvas.]({% image_buster /assets/img/experiment_step/experiment_personalized_delay_group_complete.png %}){: style="max-width:75%;" }

{% endtab %}
{% tab Canvas recorrente, disparado por ação ou disparado por API %}

Você pode testar até quatro jornadas em uma única Jornada do experimento. Adicione suas jornadas e termine de configurar seu Canvas conforme necessário, depois lance-o.

Quando o primeiro usuário entrar no experimento, você pode verificar o Canvas para ver a análise de dados conforme eles chegam e [acompanhar o desempenho do seu experimento]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step#tracking-performance).

Quando o período do experimento passar e o experimento estiver concluído, todos os usuários subsequentes que entrarem no Canvas serão enviados pela jornada com maior probabilidade de resultar em conversão para eles.

![Captura de tela relacionada à etapa 4: adicionar suas jornadas e lançar o Canvas.]({% image_buster /assets/img/experiment_step/experiment_personalized_recurring_analytics.png %}){: style="max-width:75%;" }

{% endtab %}
{% endtabs %}

## Análise de dados {#analytics}

Se as Jornadas personalizadas estiverem ativadas, sua visualização de análise de dados é separada em duas guias: **Experimento inicial** e **Jornadas personalizadas**.

{% tabs local %}
{% tab Experimento inicial %}

A guia **Experimento inicial** mostra as métricas de cada jornada durante o período do experimento. Você pode ver um resumo de como todas as jornadas se saíram para os eventos de conversão especificados.

![Resultados de um experimento inicial enviado para determinar a jornada com melhor desempenho para cada usuário. Uma tabela mostra o desempenho de cada jornada com base em várias métricas para o canal alvo.]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab1.png %})

Por padrão, o teste procura associações entre os eventos personalizados dos usuários e suas preferências de jornada, ou seja, a variante de mensagem à qual um usuário melhor responde. Essa análise detecta se eventos personalizados aumentam ou diminuem a probabilidade de responder a uma jornada específica. Essas relações são então usadas para determinar quais usuários são atribuídos a qual jornada após o período do experimento.

As relações entre eventos personalizados e preferências de jornada são exibidas na tabela da guia **Experimento inicial**.

![Tabela mostrando relações entre eventos personalizados e preferências de jornada.]({% image_buster /assets/img_archive/experiment_personalized_analytics_custom_data.png %})

Se o teste não encontrar uma relação significativa entre eventos personalizados e preferências de jornada, ele recorre a um método de análise baseado em sessões, e nenhuma tabela de dados de eventos personalizados é exibida.

{% details Método de análise de fallback %}

**Método de análise baseado em sessões**<br>
Se o método de fallback for usado para determinar as Jornadas personalizadas, a guia **Experimento inicial** mostra uma divisão das variantes preferidas dos usuários com base em uma combinação de certas características.

Essas características são:

- **Recência:** Quando tiveram a última sessão
- **Frequência:** Com que frequência têm sessões
- **Tempo de uso:** Há quanto tempo são usuários

![A tabela de Características do usuário, que mostra quais usuários têm previsão de preferir a Jornada 1 e a Jornada 2 com base nos três grupos em que se enquadram para recência, frequência e tempo de uso.]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab1_2.png %})

Pense na recência como quão recente foi a última interação do usuário com você, na frequência como a regularidade do engajamento, e no tempo de uso como o período total em que estiveram engajados com você. Agrupamos os usuários em "grupos" com base nessas três características (conforme explicado na tabela **Características do usuário**) e então verificamos qual grupo prefere qual jornada. É como classificar os usuários em centenas de listas diferentes com base em quando fizeram a última compra, com que frequência compram e há quanto tempo são clientes.

Na hora de escolher uma mensagem para um usuário, a Braze examina os grupos em que ele se enquadra. Cada grupo exerce uma influência distinta na seleção da jornada para os usuários. Quantificamos essa influência usando um método estatístico chamado [regressão logística](https://en.wikipedia.org/wiki/Logistic_regression), que é uma forma de prever comportamentos futuros com base em ações passadas. Esse método leva em conta as interações dos usuários durante o envio inicial da mensagem. Esta tabela apenas resume os resultados, exibindo qual jornada os usuários de cada grupo tenderam a engajar.

Em última análise, a Braze combina todos esses dados para selecionar uma jornada de mensagem personalizada para cada usuário, garantindo que seja o mais envolvente e relevante possível para eles.

{% alert note %}
Os intervalos de tempo para cada grupo são determinados com base nos dados de usuários específicos do Canvas, que podem variar entre Canvas.
{% endalert %}

**Como as Jornadas personalizadas são selecionadas**<br>
Com esse método, a mensagem recomendada para um usuário individual é a soma dos efeitos de sua recência, frequência e tempo de uso específicos. Recência, frequência e tempo de uso são divididos em grupos, conforme ilustrado na tabela **Características do usuário**. O intervalo de tempo de cada grupo é determinado pelos dados dos usuários em cada Canvas individual e mudará de Canvas para Canvas.

Cada grupo pode ter uma contribuição ou "impulso" diferente em direção a cada jornada. A força do impulso para cada grupo é determinada pelas respostas dos usuários no experimento inicial usando [regressão logística](https://en.wikipedia.org/wiki/Logistic_regression). Esta tabela apenas resume os resultados, exibindo qual jornada os usuários de cada grupo tenderam a engajar. A Jornada personalizada real de qualquer usuário individual depende da soma dos efeitos dos três grupos em que ele se enquadra — um para cada característica.

{% enddetails %}

{% endtab %}
{% tab Jornadas personalizadas %}

A guia **Jornadas personalizadas** mostra os resultados do experimento final, onde os usuários no Grupo de postergação foram enviados pela jornada com melhor desempenho para eles.

Os três cartões nesta página mostram o aumento projetado, os resultados gerais e os resultados projetados caso você tivesse enviado apenas pela Jornada vencedora. Mesmo que não haja aumento, o que pode acontecer às vezes, o resultado é o mesmo que enviar apenas pela Jornada vencedora (um teste A/B tradicional).

- **Aumento projetado:** A melhoria no evento de conversão selecionado devido ao uso de Jornadas personalizadas em vez de enviar todos os usuários pela jornada com melhor desempenho geral.
- **Resultados gerais:** Os resultados do segundo envio com base no seu evento de conversão.
- **Resultados projetados:** Os resultados projetados do segundo envio com base na métrica de otimização escolhida, caso você tivesse enviado apenas a Variante vencedora.

![Guia Jornadas personalizadas para um Canvas. Os cartões mostram o Aumento projetado, Conversões gerais (com Jornadas personalizadas) e Aberturas únicas projetadas (com Jornada vencedora).]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab2.png %})

{% endtab %}
{% endtabs %}

## Usando Jornadas personalizadas com entrega no horário local {#using-personalized-paths-with-local-time-delivery}

Não recomendamos usar entrega no horário local em Canvas com Jornadas personalizadas. Isso porque os períodos do experimento começam quando o primeiro usuário passa pela etapa. Usuários que estão em fusos horários muito adiantados podem entrar na etapa e acionar o início do período do experimento muito antes do esperado, o que pode resultar na conclusão do experimento antes que a maioria dos seus usuários em fusos horários mais comuns tenha tido tempo suficiente para entrar no Canvas e converter.

Se você deseja usar entrega no horário local, use um período de experimento de 24 a 48 horas ou mais. Dessa forma, os usuários em fusos horários adiantados entram no Canvas e acionam o início do experimento, mas ainda resta bastante tempo no período do experimento. Os usuários em fusos horários mais atrasados ainda terão tempo suficiente para entrar no Canvas e na etapa de Jornada do experimento com Jornadas personalizadas e possivelmente converter antes que o período do experimento expire.