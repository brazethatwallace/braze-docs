---
nav_title: Enviar para Destino
article_title: Enviar para Destino
alias: "/send_to_destination/"
page_order: 11.5
page_type: reference
description: "Este artigo de referência aborda o componente Enviar para Destino e como usá-lo nos seus Canvas."
tool: Canvas
---

# Etapa Enviar para Destino {#send-to-destination-step}

> A etapa Enviar para Destino permite enviar usuários de um Canvas para outro. Por exemplo, você pode conectar Canvas que compartilham envio de mensagens de ofertas promocionais.

## Como funciona {#how-it-works}

![Uma etapa Enviar para Destino para enviar usuários para um novo Canvas.]({% image_buster /assets/img/send_to_destination1.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Seu Canvas atual com a etapa Enviar para Destino é a origem. Dentro da etapa, você pode escolher o Canvas de destino. Os usuários do Canvas de origem devem atender aos critérios de público do Canvas de destino. Digamos que você tenha dois Canvas:

- **Origem:** Canvas 1, inclui uma etapa Enviar para Destino que envia usuários para o Canvas 2
- **Destino:** Canvas 2, com critérios de público para admitir usuários que fizeram um pedido

Essa etapa permite que os usuários do Canvas 1 sejam enviados para o Canvas 2. Quando os usuários do Canvas 1 entram na etapa Enviar para Destino, eles são avaliados em relação aos critérios de público do Canvas 2 para determinar se são elegíveis para entrar no Canvas. Nesse caso, os usuários que fizeram um pedido podem entrar no Canvas 2 e também continuar sua jornada no Canvas 1. Para os usuários que não fizeram um pedido, eles continuam sua jornada apenas no Canvas 1.

### Comportamento de entrada {#entry-behavior}

A etapa Enviar para Destino insere os usuários no Canvas de destino assim que eles alcançam essa etapa. Essa etapa funciona como um ponto de entrada único no Canvas de destino. Os usuários que atendem aos critérios de público do Canvas de destino iniciam essa jornada no Canvas. Os usuários que não atendem a esses critérios naquele momento não entram no Canvas de destino e continuam no Canvas de origem.

A etapa Enviar para Destino também respeita as [configurações de reentrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) do Canvas de destino em **Entry Controls**. Se um usuário não for elegível para reentrar no Canvas de destino, ele não será enviado para lá e continuará no Canvas de origem.

Se o Canvas de destino usar um cronograma de entrada agendado, a etapa Enviar para Destino ignora esse cronograma de entrada. Ela também ignora o [**Limit entrance volume**]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) em **Entry Controls** no Canvas de destino quando estiver configurado como **Every time Canvas is schedule**. Os usuários enviados por essa etapa não aguardam a próxima janela de avaliação agendada — eles são avaliados em relação aos critérios de público do Canvas de destino e inseridos imediatamente quando alcançam a etapa Enviar para Destino.

Se o Canvas de destino usar entrada baseada em ação, a etapa Enviar para Destino ignora o requisito de que os usuários realizem a ação de entrada configurada para entrar nesse Canvas.

## Criar uma etapa Enviar para Destino {#create-a-send-to-destination-step}

### Etapa 1: Adicionar uma etapa {#step-1-add-a-step}

Arraste e solte o componente **Enviar para Destino** da barra lateral, ou selecione o botão de adição <i class="fas fa-plus-circle"></i> na parte inferior de uma etapa e selecione **Enviar para Destino**.

### Etapa 2: Escolher seu destino {#step-2-choose-your-destination}

Selecione o menu suspenso ou insira o nome do Canvas no campo **Destino**. Em seguida, selecione **Concluído**.

![Uma etapa Enviar para Destino configurada para enviar usuários de um Canvas chamado "Feature Adoption" para "New Canvas".]({% image_buster /assets/img/send_to_destination2.png %})

### Etapa 3: Visualizar seu destino {#step-3-preview-your-destination}

Você pode selecionar **Visualizar destino** para ver o Canvas para o qual você está enviando os usuários.

Depois de configurar essa etapa do Canvas, você pode [visualizar a jornada do usuário]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths) para verificar se um usuário avança para a próxima etapa no Canvas atual e se ele também avança para o Canvas de destino.

## Perguntas frequentes {#frequently-asked-questions}

### Posso definir o destino como um Canvas em rascunho? {#can-i-set-the-destination-to-a-draft-canvas}

Sim. O Canvas de destino pode ter o status de rascunho ou sem atividades.

### As variáveis de contexto são preservadas? {#are-context-variables-preserved}

Sim. O [contexto]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) do Canvas de origem é passado para o Canvas de destino. No entanto, as variáveis de contexto precisam ser invocadas dentro do Canvas de origem para serem passadas ao Canvas de destino.

### Posso usar a etapa Enviar para Destino para conectar Canvas em vez de usar soluções alternativas com API ou Atualização de Usuário? {#can-i-use-the-send-to-destination-step-to-connect-canvases-instead-of-using-api-or-user-update-workarounds}

Sim. Você pode conectar Canvas com a etapa Enviar para Destino quando os usuários devem ser movidos diretamente para outra jornada de Canvas.

Você não precisa de etapas separadas de Atualização de Usuário, disparos de API ou webhooks apenas para mover usuários entre Canvas, desde que eles atendam aos critérios de público do Canvas de destino no momento do envio.

### Os usuários entram no início do Canvas de destino? {#do-users-enter-at-the-start-of-the-destination-canvas}

Os usuários elegíveis entram imediatamente na primeira etapa do Canvas de destino. Eles não esperam por um horário de entrada agendado posterior no Canvas de destino. Não é possível vincular a uma etapa específica do Canvas dentro do Canvas de destino.

### A etapa Enviar para Destino respeita o cronograma de entrada agendado do Canvas de destino? {#does-the-send-to-destination-step-respect-a-scheduled-destination-canvas-entry-schedule}

Não. Se o Canvas de destino usa um tipo de entrada agendada, os usuários enviados pela etapa Enviar para Destino não esperam pela próxima janela de avaliação agendada. Eles são avaliados em relação aos critérios de público e entram imediatamente quando chegam à etapa Enviar para Destino.

### Como funciona o comportamento de avanço para as etapas Enviar para Destino? {#how-does-advancement-behavior-work-for-send-to-destination-steps}

Os usuários que entram na etapa Enviar para Destino continuam sua jornada se houver etapas adicionais no Canvas de origem. Se os usuários também atenderem aos critérios de público do Canvas de destino, eles podem entrar nesse Canvas e iniciar essa jornada.

### A etapa Enviar para Destino está sujeita a limites de frequência de API? {#is-the-send-to-destination-step-subject-to-api-rate-limits}

Não. Os usuários são enviados entre Canvas dentro da Braze sem fazer chamadas de API externas.