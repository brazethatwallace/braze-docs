---
nav_title: Lançamento com Canvas Flow
article_title: Lançamento com Canvas Flow
page_order: 3
description: "Este artigo de referência aborda como preparar e testar um Canvas criado com Canvas Flow antes do lançamento."
page_type: reference
tool: Canvas
---

# Lançamento com Canvas Flow {#launch-with-canvas-flow}

> Este artigo de referência aborda como preparar e testar um Canvas criado com Canvas Flow antes do lançamento. Isso inclui a identificação de pontos de verificação importantes do Canvas, como condições de entrada, resumos de público e segmentos de usuários.

Ao se preparar para lançar seu Canvas, a Braze recomenda que você verifique seu Canvas em cada etapa do criador de Canvas para configurações que podem impactar o envio de mensagens, incluindo:
* [Condições de corrida](#race-conditions)
* [Horários de entrega](#delivery-times)
* [Segmentos de usuários](#segment-users)

## Condições de corrida {#race-conditions}

Considere as [condições de corrida]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions) que podem ocorrer antes de lançar seu Canvas.

Para entrar em um Canvas, os usuários devem estar no público de entrada antes que o cronograma de entrada ocorra, independentemente de o Canvas ser agendado, baseado em ação ou disparado por API.

![Um Canvas baseado em ação que insere usuários quando eles fazem qualquer compra durante o horário local do usuário, de 30 de abril de 2025 às 12h até 7 de maio de 2025 às 12h.]({% image_buster /assets/img_archive/launch_with_canvas_flow_example.png %}){: style="max-width:75%;"}

Observe que os usuários que se qualificarem para o público de entrada após o lançamento do Canvas não entrarão no Canvas.

{% alert tip %}
Confira os [tipos de cronograma de entrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule) para orientações e detalhes sobre quando usar entrega agendada, baseada em ação ou disparada por API para o seu Canvas!
{% endalert %}

### Revise os filtros do público de entrada {#review-entry-audience-filters}

De modo geral, evite configurar um Canvas baseado em ação ou disparado por API com o mesmo gatilho do filtro de público. Por exemplo, após o lançamento de um Canvas, os usuários que realizarem uma ação específica serão incluídos no público de entrada, então não é necessário adicionar o evento como filtro de público.

Para mais detalhes sobre os filtros de segmentação disponíveis para segmentar seu público, consulte [Filtros de segmentação]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).

### Agrupe múltiplas solicitações de API {#batch-multiple-api-requests}

Faça suas solicitações na mesma chamada de API, em vez de múltiplas chamadas, para garantir que o perfil de usuário seja criado ou atualizado primeiro. Consulte [Usando múltiplos endpoints]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions#using-multiple-api-endpoints) para mais exemplos.

### Adicione uma postergação {#add-a-delay}

Outra opção para evitar condições de corrida é usar a etapa de postergação (idealmente configurada para 5 minutos) como a primeira etapa do seu Canvas.

Isso permite tempo para que atributos, endereços de e-mail e tokens por push sejam processados nos novos perfis de usuário antes de serem direcionados para as etapas seguintes do Canvas. Sem essa etapa de postergação, é possível que um e-mail seja enviado a um usuário cujo endereço de e-mail ainda não foi atualizado.

## Horários de entrega {#delivery-times}

Configurar um horário de entrega do Canvas em tempo real pode aumentar as taxas de engajamento e conversão. Observe qual horário de entrega você definiu para o seu Canvas. Para ajudar a aumentar as taxas de engajamento e conversão, é melhor disparar Canvas em tempo real em vez de em uma base agendada e recorrente.

Se você selecionou uma entrega agendada para o seu Canvas, a Braze recomenda agendar seu Canvas pelo menos 24 horas antes do horário desejado de lançamento para permitir ajustes.

## Segmentos de usuários {#user-segments}

Antes de sobrecarregar a jornada do usuário no Canvas Flow com componentes, considere como você pode manter a jornada do usuário simples. Use a visualização simplificada no editor de Canvas para ter uma ideia melhor de como a jornada do usuário se ramifica.

Existem quatro componentes principais que você pode usar para segmentar seus usuários de forma simples e eficaz:

* [Jornadas do público](#audience-paths)
* [Divisão de decisão](#decision-split)
* [Jornadas de ação](#action-paths)
* [Jornadas do experimento](#experiment-paths)

### Jornadas do público {#audience-paths}

Use as etapas de [Jornadas do público]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) para segmentar usuários dentro do Canvas com base em atributos personalizados, eventos personalizados e dados de engajamento com mensagens anteriores dos perfis de usuário.

### Divisão de decisão {#decision-split}

A etapa de [Divisão de decisão]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split) permite enviar seus usuários para diferentes jornadas com base nas respostas a uma pergunta polar.

### Jornadas de ação {#action-paths}

As [Jornadas de ação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) focam na segmentação de usuários com base em comportamentos em tempo real, como eventos personalizados, eventos de compra e alterações de atributos personalizados.

### Jornadas do experimento {#experiment-paths}

Semelhante às Jornadas de ação, você pode aproveitar as etapas de [Jornadas do experimento]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) no seu Canvas para testar múltiplas jornadas do Canvas entre si, junto com um grupo de controle. Isso rastreia o desempenho das jornadas, permitindo que você tome decisões informadas ao construir a jornada do seu Canvas.

## Testes antes do lançamento {#testing-before-launch}

Após revisar os detalhes do seu Canvas, confira [Enviando Canvas de teste]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases) para conhecer diferentes métodos que você pode usar para testar seu Canvas com usuários teste.

## Checklist de lançamento {#launch-checklist}

### Verifique a disponibilidade dos usuários {#check-user-availability}

- Certifique-se de que seus usuários atendem aos critérios de segmentação.
- Confirme que o estado de inscrição deles é "Subscribed" ou "opted-in" e que o token por push existe. Se você adicionou essas regras como regras de entrada do Canvas, é possível que os usuários tenham cancelado a inscrição entre a entrada no Canvas e o recebimento da etapa de mensagem.
- Confirme que eles correspondem às configurações de envio do Canvas. (Se os usuários estão "Subscribed", mas as configurações são "Opted-in", os usuários não serão ativados para o canal.)
- Se o limite de frequência global está ativado para o seu Canvas, verifique se suas regras estão limitando quantas vezes cada usuário pode receber uma mensagem de um canal específico.
- Se o horário de silêncio está ativado, o horário de envio da sua mensagem pode ser afetado. Isso significa que sua mensagem pode ser enviada no próximo horário disponível (quando o horário de silêncio terminar) ou cancelada completamente.
- Verifique a disponibilidade dos usuários para filtros adicionais na etapa do Canvas.

### Confirme que eles realizaram o evento personalizado ou compra pré-requisito {#confirm-that-they-performed-the-prerequisite-custom-event-or-purchase}

- Verifique se há uma condição de corrida, que impacta as mensagens que os usuários recebem se eles dispararem múltiplas ações ao mesmo tempo.
- Certifique-se de que não há filtros específicos na etapa que possam ter bloqueado os usuários de receber a mensagem.
- Procure conflitos entre diferentes etapas dentro do mesmo Canvas. Por exemplo, usuários que não receberam a mensagem podem ter sido bloqueados por um filtro que exige a conclusão de outra etapa em uma ramificação diferente.
- Confirme que os usuários atendem a regras de validação adicionais.
- Confirme que a etapa do Canvas estava conectada à etapa anterior no momento do envio.

### Confirme que seu Canvas salva corretamente e que todas as etapas são válidas {#confirm-your-canvas-saves-correctly-and-all-steps-are-valid}

Se o seu Canvas não está carregando e não avança, isso pode ser causado quando uma versão anterior do Canvas não foi salva corretamente e contém etapas inválidas. Você pode duplicar o Canvas a partir do dashboard. Se o problema persistir, abra um [ticket de suporte]({{site.baseurl}}/braze_support).

## Solução de problemas {#troubleshooting}

{% details Por que meus usuários não estão recebendo as mensagens do Canvas? %}
**Verifique a disponibilidade dos usuários**
- Certifique-se de que eles atendem aos critérios de segmentação.
- Confirme que o estado de inscrição push deles é "Subscribed" ou "opted-in" **e** que o status **Push Enabled** está definido como "true". Se você adicionou essas regras como regras de entrada do Canvas, é possível que os usuários tenham cancelado a inscrição entre a entrada no Canvas e o recebimento da etapa de mensagem.
- Confirme que eles correspondem às configurações de envio do Canvas. (Se os usuários estão "Subscribed", mas as configurações são "Opted-in", os usuários não serão ativados para o canal.)
- Se o limite de frequência global está ativado para o seu Canvas, verifique se suas regras estão limitando quantas vezes cada usuário pode receber uma mensagem de um canal específico.
- Se o horário de silêncio está ativado, o horário de envio da sua mensagem pode ser afetado. Isso significa que sua mensagem pode ser enviada no próximo horário disponível (quando o horário de silêncio terminar) ou cancelada completamente.

**Verifique a disponibilidade dos usuários para filtros adicionais na etapa do Canvas**
- Confirme que eles realizaram o evento personalizado ou compra pré-requisito.
- Verifique se há uma [condição de corrida]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions), que impacta as mensagens que os usuários recebem se eles dispararem múltiplas ações ao mesmo tempo.
- Certifique-se de que não há filtros específicos na etapa que possam ter bloqueado os usuários de receber a mensagem.
- Procure conflitos entre diferentes etapas dentro do mesmo Canvas. Por exemplo, usuários que não receberam a mensagem podem ter sido bloqueados por um filtro que exige a conclusão de outra etapa em uma ramificação diferente.
- Confirme que os usuários atendem a regras de validação adicionais.
- Confirme que a etapa do Canvas estava conectada à etapa anterior no momento do envio.
{% enddetails %}