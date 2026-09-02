---
nav_title: Checklist de pré e pós-lançamento
article_title: Checklist de pré e pós-lançamento
page_order: 2
description: "Este artigo fornece um guia sobre o que verificar antes e depois de lançar um Canvas."
tool: Canvas

---

# Checklist de pré e pós-lançamento {#pre-and-post-launch-checklist}

> Este artigo fornece um guia sobre o que verificar antes e depois de lançar um Canvas.

## Coisas a considerar antes do lançamento {#things-to-consider-before-launch}

Antes de lançar um Canvas, há vários detalhes que você pode verificar para garantir que suas mensagens e horários de envio estejam alinhados com as preferências do seu público. Entre as coisas a considerar estão variações de fuso horário, configurações de entrada e mais. Use esta checklist como guia para ajustar essas áreas com base no seu caso de uso e contribuir para o sucesso do seu Canvas.

### Revise as configurações de fuso horário {#review-time-zone-settings}

Se você está inserindo usuários de acordo com o fuso local deles usando um cronograma de entrada agendado, você deve lançar seu Canvas pelo menos 24 horas antes do horário em que deseja que os usuários entrem no seu Canvas. Por exemplo, aqui está um Canvas que não deixou tempo suficiente entre o lançamento e o horário de entrada agendado. Nesse cenário, alguns usuários podem não entrar no seu Canvas porque o horário de entrada agendado já passou em determinados fusos horários.

{% alert tip %}
Você verá um alerta se não tiver agendado tempo suficiente como margem. Uma solução rápida é ajustar o horário de envio para garantir que os usuários possam permanecer no Segment or segmento de destino por 24 horas completas.
{% endalert %}

![Um Canvas agendado para inserir usuários em um horário específico, começando às 10h do dia 30 de abril de 2025, no fuso local deles.]({% image_buster /assets/img_archive/canvas_checklist1.png %}){: style="max-width:75%;"}

### Considere usar expressões regulares para filtros de público {#consider-using-regular-expressions-for-audience-filters}

Após configurar os detalhes preliminares de quando seus usuários devem entrar em um Canvas, é recomendável verificar seus Segments ou filtros na etapa **Público-alvo** da criação do Canvas. Nessa etapa, você também pode revisar o resumo do **Público-alvo** para ver como seu público-alvo foi configurado.

Aqui, considere usar uma expressão regular para Segments ou filtros em etapas de jornadas do público, configurações de validação de entrega em etapas de mensagem e divisão de decisão. Uma [expressão regular]({{site.baseurl}}/user_guide/audience/segments/regex) (também chamada de regex) é uma string, o que significa que ela reconhece padrões e leva em consideração os caracteres, em vez de coisas como capitalização. Isso significa que, se você estiver usando "É igual a / Não é igual a", pode estar limitando o tamanho do seu público por causa de simples erros de sintaxe.

Se você notar que seu público-alvo é menor do que o esperado, tente usar "Corresponde a Regex" ou "Não corresponde a Regex" em vez de "É igual a" ou "Não é igual a". Isso pode contemplar os usuários que estavam faltando e atingir um público maior.

### Identifique configurações de entrada e condições de corrida {#identify-entry-settings-and-race-conditions}

Uma condição de corrida pode ocorrer quando você usa os mesmos critérios de entrada tanto nas configurações de **Cronograma de entrada** quanto nas de **Público-alvo**.

Se você estiver usando entrada baseada em ação, verifique se não usou a mesma ação-gatilho aqui e no seu público-alvo. Uma condição de corrida pode ocorrer quando o usuário não está no público no momento em que realiza o evento-gatilho, o que significa que ele não entrará no Canvas.

{% alert tip %}
Confira as [práticas recomendadas]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions#scenario-3-matching-action-based-triggers-and-audience-filters) para evitar essa condição de corrida ao configurar um Canvas baseado em ação com o mesmo gatilho do filtro de público.
{% endalert %}

### Verifique as propriedades de entrada do Canvas e as propriedades de evento {#check-canvas-entry-properties-and-event-properties}

Embora tenham nomes semelhantes, as [propriedades de entrada do Canvas e as propriedades de evento]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) funcionam de maneiras diferentes nos fluxos de trabalho do seu Canvas. As propriedades de entrada do Canvas estão vinculadas às suas configurações de entrada e podem ser referenciadas em qualquer componente de mensagem ao longo do seu Canvas. As propriedades de entrada do Canvas são propriedades do evento ou da chamada de API or interface de programação do aplicativo (API) que dispara a entrada de um usuário no Canvas, usando configurações de entrada baseada em ação ou disparada por API or interface de programação do aplicativo (API).

As propriedades de evento, por outro lado, só podem ser referenciadas na primeira etapa de mensagem após uma etapa de jornadas de ação. As propriedades de evento são propriedades de um evento personalizado ou evento de compra que o usuário realizou durante a janela de avaliação de uma etapa de jornadas de ação, e que dispara a progressão dele por uma das jornadas de ação definidas.

Verifique a prévia da mensagem para qualquer etapa de mensagem que faça referência a propriedades de entrada do Canvas ou propriedades de evento.

### Revise as etapas de mensagem para o avanço do usuário {#review-message-steps-for-user-advancement}

Por padrão, os usuários avançarão por todas as etapas de mensagem independentemente de terem recebido a mensagem. Se você quiser avançar os usuários que receberam uma mensagem específica, pode fazer isso adicionando uma etapa de divisão de decisão diretamente após o componente de mensagem. Adicione o filtro "Recebeu mensagem da etapa do Canvas" como filtro adicional, e então selecione o Canvas e a etapa de mensagem.

Para etapas de mensagem com mensagens no app, você pode querer usar um componente de jornadas de ação em vez do componente de divisão de decisão. Isso permitirá avançar os usuários com base em se eles visualizaram sua mensagem no app. Defina um grupo de ação adicionando o filtro "Interagir com etapa" e selecione **Visualizar mensagem no app**. Em seguida, defina a janela de avaliação da etapa para a janela de expiração da mensagem no app.

Para um componente de mensagem em envio de mensagens multicanal, recomendamos o seguinte:
* Inclua uma etapa de postergação entre suas etapas de mensagem e de divisão de decisão, e defina a postergação para pelo menos cinco segundos
* Se o componente inclui Intelligent Timing, defina a postergação para 24 horas
* Se o componente inclui limite de frequência, divida suas mensagens em várias etapas de mensagem de canal único e conecte-as. Em seguida, conecte a etapa de divisão de decisão diretamente após a última etapa de mensagem para verificar se o usuário recebeu alguma das mensagens. Você também pode usar esse método como alternativa para uma etapa de mensagem multicanal com Intelligent Timing.

## Pontos a considerar após o lançamento {#things-to-consider-after-launch}

Você lançou seu Canvas! E agora? Use este checklist para ver como revisar e ajustar seu Canvas em caso de discrepâncias após o lançamento com base nos cenários a seguir.

### Muitas entradas, mas poucos envios {#many-entries-but-few-sends}

Por exemplo, digamos que você notou uma disparidade entre o número de mensagens enviadas e o total de entradas. Você pode identificar e descobrir áreas para ajustar seu Canvas verificando estas áreas principais.

#### Público de entrada {#entry-audience}

Se estiver usando uma Campaign de envio agendado, verifique novamente seu público-alvo revisando seu público-alvo. Como estão os números em cada canal, e como isso se relaciona com os canais usados no seu Canvas? Se os números mais baixos correspondem aos canais usados no seu Canvas, você pode ter encontrado o problema.

#### Primeiro componente do Canvas {#first-component-of-the-canvas}

Revise quaisquer filtros de público, ações-gatilho ou Segments usados nos componentes iniciais do seu Canvas. Existem erros de digitação ou condições restritivas demais que estão impedindo o Canvas de começar corretamente? Você está usando "Equals" quando deveria usar "Matches Regex"?

#### Grupo de controle do Canvas {#canvas-control-group}

Revise a distribuição de usuários entre suas variantes e seu grupo de controle. O grupo de controle é maior do que você pretendia? Se sim, você pode editar essa configuração. Se **Optimize with BrazeAI<sup>TM</sup>** estiver ativado e o grupo de controle estiver ganhando, considere parar seu Canvas e tentar uma nova abordagem.

### Público total vazio {#an-empty-total-audience}

Se você não está vendo nenhum dado de entrada no seu Canvas, o motivo pelo qual os usuários podem não estar entrando no Canvas pode ser devido a condições de corrida e filtros de segmentação de público restritivos.

Se estiver usando entrada baseada em ação no seu cronograma de entrada, verifique se você não usou a mesma ação-gatilho aqui e no seu **público-alvo**. Uma condição de corrida pode ocorrer quando o usuário não está no público no momento em que realiza o evento-gatilho, o que significa que ele não entrará no Canvas.

Além disso, verifique se o Segment or segmento selecionado tem usuários revisando a tabela de **público-alvo** nas configurações de **público-alvo**. Se esse número estiver baixo, veja como ajustar suas configurações de entrada ou revise seus Segments ou filtros selecionados para verificar possíveis erros.

### Queda inesperada entre etapas {#unexpected-drop-off-between-steps}

Outra forma clara de identificar áreas de ajuste no seu Canvas é quando há uma grande queda de uma etapa do Canvas para a próxima. Nesse caso, verifique se seus filtros de público e eventos de exceção não possuem erros de digitação ou de capitalização. E como sempre, verifique se seus filtros de público não são tão restritivos a ponto de excluir a maioria dos seus usuários de entrar no Canvas.

Em seguida, é importante identificar as configurações que podem afetar quando e se as mensagens são enviadas aos seus usuários:
- [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing)
- [Horário de silêncio]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)
- Validações de entrega

De modo geral, escolha Intelligent Timing ou [horário de silêncio]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours) para o seu Canvas, não ambos. A mesma sugestão se aplica ao uso de Intelligent Timing ou [limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping), e não ambos. Para saber mais sobre como usar o Intelligence Suite da melhor forma, leia nossos [casos de uso do Intelligence Suite]({{site.baseurl}}/user_guide/brazeai/intelligence_suite#use-cases).

### Volumes de envio suspeitos entre jornadas {#suspicious-send-volumes-between-paths}

Quando o volume de envios entre duas ou mais jornadas (sejam jornadas do público ou jornadas de ação) não é o esperado, essa pode ser uma oportunidade para verificar seus Segments, filtros ou ações-gatilho. Além disso, identifique e remova quaisquer filtros sobrepostos.