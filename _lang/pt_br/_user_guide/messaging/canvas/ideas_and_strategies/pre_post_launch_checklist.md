---
nav_title: Checklist de pré e pós-lançamento
article_title: Checklist de pré e pós-lançamento
page_order: 2
description: "Este artigo fornece um guia sobre o que verificar antes e depois de lançar um Canvas."
tool: Canvas

---

# Checklist de pré e pós-lançamento {#pre-and-post-launch-checklist}

> Este artigo fornece um guia sobre o que verificar antes e depois de lançar um Canvas.

## O que considerar antes do lançamento {#things-to-consider-before-launch}

Antes de lançar um Canvas, há vários detalhes que você pode verificar para garantir que suas mensagens e horários de envio estejam alinhados com as preferências do seu público. Considere variações de fuso horário, configurações de entrada e muito mais. Use este checklist como guia para ajustar essas áreas com base no seu caso de uso e contribuir para o sucesso do seu Canvas.

### Revise as configurações de fuso horário {#review-time-zone-settings}

Se você está inserindo usuários de acordo com o horário local deles usando um cronograma de entrada agendado, lance seu Canvas pelo menos 24 horas antes do horário em que deseja que os usuários entrem. Por exemplo, aqui está um Canvas que não deixou tempo suficiente entre o lançamento e o horário de entrada agendado. Nesse cenário, alguns usuários podem não entrar no Canvas porque o horário de entrada agendado já passou em determinados fusos horários.

{% alert tip %}
Você verá um alerta se não tiver programado um intervalo suficiente. Uma solução rápida é ajustar o horário de envio para garantir que os usuários permaneçam no segmento-alvo por 24 horas completas.
{% endalert %}

![Um Canvas agendado para inserir usuários em um horário específico, começando às 10h do dia 30 de abril de 2025, no horário local.]({% image_buster /assets/img_archive/canvas_checklist1.png %}){: style="max-width:75%;"}

### Considere usar expressões regulares nos filtros de público {#consider-using-regular-expressions-for-audience-filters}

Depois de configurar os detalhes preliminares de quando seus usuários devem entrar em um Canvas, é recomendável verificar seus segmentos ou filtros na etapa **Público-alvo** da criação do Canvas. Nessa etapa, você também pode revisar o resumo do **Público-alvo** para ver como seu público foi configurado.

Aqui, considere usar uma expressão regular para segmentos ou filtros nas etapas de Jornadas do público, bem como nas configurações de validação de entrega nas etapas de Mensagem e Divisão de decisão. Uma [expressão regular]({{site.baseurl}}/user_guide/audience/segments/regex/) (também chamada de regex) é uma string, o que significa que ela reconhece padrões e leva em conta os caracteres, em vez de coisas como capitalização. Isso significa que, se você estiver usando "Equals / Does Not Equal", pode estar limitando o tamanho do seu público por causa de erros simples de sintaxe.

Se você perceber que seu público-alvo é menor do que o esperado, tente usar "Matches Regex" ou "Does Not Match Regex" em vez de "Equals" ou "Does Not Equal". Isso pode incluir os usuários que estavam faltando e alcançar um público maior.

### Identifique configurações de entrada e condições de corrida {#identify-entry-settings-and-race-conditions}

Uma condição de corrida pode ocorrer quando você usa os mesmos critérios de entrada tanto nas configurações do **Cronograma de entrada** quanto do **Público-alvo**.

Se você estiver usando entrada baseada em ação, verifique se não usou a mesma ação-gatilho aqui e no seu público-alvo. Uma condição de corrida pode ocorrer quando o usuário não está no público no momento em que realiza o evento de gatilho, o que significa que ele não entrará no Canvas.

{% alert tip %}
Confira as [práticas recomendadas]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions/#scenario-3-matching-action-based-triggers-and-audience-filters) para evitar essa condição de corrida ao configurar um Canvas baseado em ação com o mesmo gatilho do filtro de público.
{% endalert %}

### Verifique as propriedades de entrada do Canvas e as propriedades de evento {#check-canvas-entry-properties-and-event-properties}

Embora tenham nomes semelhantes, as [propriedades de entrada do Canvas e as propriedades de evento]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/) funcionam de maneira diferente nos fluxos de trabalho do Canvas. As propriedades de entrada do Canvas estão vinculadas às suas configurações de entrada e podem ser referenciadas em qualquer componente de mensagem ao longo do Canvas. Elas são propriedades do evento ou da chamada de API que aciona a entrada de um usuário no Canvas, usando configurações de entrada baseadas em ação ou acionadas por API.

As propriedades de evento, por outro lado, só podem ser referenciadas na primeira etapa de Mensagem após uma etapa de Jornadas de ação. Elas são propriedades de um evento personalizado ou evento de compra que o usuário realizou durante a janela de avaliação de uma etapa de Jornadas de ação, e que aciona a progressão dele por uma das jornadas de ação definidas.

Verifique a pré-visualização da mensagem para quaisquer etapas de Mensagem que referenciem propriedades de entrada do Canvas ou propriedades de evento.

### Revise as etapas de Mensagem para avanço de usuários {#review-message-steps-for-user-advancement}

Por padrão, os usuários avançam por todas as etapas de Mensagem independentemente de terem recebido a mensagem. Se você quiser avançar apenas os usuários que receberam uma mensagem específica, adicione uma etapa de Divisão de decisão logo após o componente de Mensagem. Adicione o filtro "Received Message from Canvas Step" como filtro adicional e selecione o Canvas e a etapa de Mensagem.

Para etapas de Mensagem com mensagens no app, você pode usar um componente de Jornadas de ação em vez do componente de Divisão de decisão. Isso permitirá avançar os usuários com base em se eles visualizaram sua mensagem no app. Defina um grupo de ação adicionando o filtro "Interact with Step" e selecione **View in app message**. Em seguida, defina a janela de avaliação da etapa para a janela de expiração da mensagem no app.

Para um componente de Mensagem com envio de mensagens multicanal, recomendamos o seguinte:
* Inclua uma etapa de postergação entre as etapas de Mensagem e Divisão de decisão, e defina a postergação para pelo menos cinco segundos
* Se o componente incluir Intelligent Timing, defina a postergação para 24 horas
* Se o componente incluir limite de taxa, divida suas mensagens em várias etapas de Mensagem de canal único e conecte-as. Em seguida, conecte a etapa de Divisão de decisão logo após a última etapa de Mensagem para verificar se o usuário recebeu alguma das mensagens. Você também pode usar esse método como alternativa para uma etapa de Mensagem multicanal com Intelligent Timing.

## O que considerar após o lançamento {#things-to-consider-after-launch}

Você lançou seu Canvas! E agora? Use este checklist para revisar e ajustar seu Canvas caso haja discrepâncias após o lançamento, com base nos cenários a seguir.

### Muitas entradas, mas poucos envios {#many-entries-but-few-sends}

Por exemplo, digamos que você notou uma disparidade entre o número de mensagens enviadas e o total de entradas. Você pode identificar e descobrir áreas para ajustar seu Canvas verificando estas áreas-chave.

#### Público de entrada {#entry-audience}

Se você estiver usando uma Campaign de envio agendado, verifique novamente seu público-alvo revisando o público-alvo. Como estão os números entre os canais, e como isso se relaciona com os canais que você usou no Canvas? Se os números mais baixos correspondem aos canais usados no Canvas, você pode ter encontrado o problema.

#### Primeiro componente do Canvas {#first-component-of-the-canvas}

Revise quaisquer filtros de público, gatilhos de ação ou segmentos usados nos componentes iniciais do Canvas. Há erros de digitação ou condições muito restritivas que estão impedindo o Canvas de começar corretamente? Você está usando "Equals" quando deveria usar "Matches Regex"?

#### Grupo de controle do Canvas {#canvas-control-group}

Revise a distribuição de usuários entre suas variantes e o grupo de controle. O grupo de controle é maior do que você pretendia? Se sim, você pode editar essa configuração. Se a **Seleção inteligente** estiver ativada e o grupo de controle estiver vencendo, considere parar o Canvas e tentar uma nova abordagem.

### Público total vazio {#an-empty-total-audience}

Se você não está vendo nenhum dado de entrada no Canvas, os motivos pelos quais os usuários podem não estar entrando podem ser condições de corrida e filtros de segmentação de público muito restritivos.

Se você estiver usando entrada baseada em ação no cronograma de entrada, verifique se não usou a mesma ação-gatilho aqui e no **Público-alvo**. Uma condição de corrida pode ocorrer quando o usuário não está no público no momento em que realiza o evento de gatilho, o que significa que ele não entrará no Canvas.

Além disso, verifique se o segmento selecionado tem usuários revisando a tabela **Público-alvo** nas configurações de **Público-alvo**. Se esse número for baixo, veja como ajustar suas configurações de entrada ou revise os segmentos ou filtros selecionados em busca de erros.

### Queda inesperada entre etapas {#unexpected-drop-off-between-steps}

Outra forma evidente de identificar áreas de ajuste no Canvas é quando há uma grande queda de uma etapa para a próxima. Nesse caso, verifique se seus filtros de público e eventos de exceção não têm erros de digitação ou capitalização. E, como sempre, verifique se seus filtros de público não são tão restritivos a ponto de excluir a maioria dos usuários da entrada no Canvas.

Em seguida, é importante identificar estas configurações que podem afetar quando e se as mensagens são enviadas aos seus usuários:
- [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/)
- [Horário de silêncio]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/)
- Validações de entrega

Em geral, escolha Intelligent Timing ou [horário de silêncio]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/) para o seu Canvas, não ambos. A mesma sugestão se aplica ao uso de Intelligent Timing ou [limite de taxa]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/), não ambos. Para saber mais sobre como usar melhor o Intelligence Suite, leia nossos [casos de uso do Intelligence Suite]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/#use-cases).

### Volumes de envio suspeitos entre jornadas {#suspicious-send-volumes-between-paths}

Quando o volume de envios entre duas ou mais jornadas (Jornadas do público ou Jornadas de ação) não é o esperado, essa pode ser uma oportunidade para verificar seus segmentos, filtros ou ações-gatilho. Além disso, certifique-se de identificar e remover quaisquer filtros sobrepostos.