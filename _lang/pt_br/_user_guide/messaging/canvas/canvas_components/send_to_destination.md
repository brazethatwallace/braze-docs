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

![Uma etapa Enviar para Destino para enviar usuários a um novo Canvas.]({% image_buster /assets/img/send_to_destination1.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

O Canvas atual com a etapa Enviar para Destino é a origem. Dentro da etapa, você pode escolher o Canvas de destino. Os usuários do Canvas de origem devem atender aos critérios de entrada e de público do Canvas de destino. Digamos que você tenha dois Canvas:

- **Origem:** Canvas 1, inclui uma etapa Enviar para Destino que envia usuários para o Canvas 2
- **Destino:** Canvas 2, com os critérios de entrada para admitir usuários que fizeram um pedido

Essa etapa permite que os usuários do Canvas 1 sejam enviados para o Canvas 2. Quando os usuários do Canvas 1 entram na etapa Enviar para Destino, eles são avaliados com base nos critérios de entrada e de público do Canvas 2 para determinar se são elegíveis para entrar no Canvas. Nesse caso, os usuários que fizeram um pedido podem entrar no Canvas 2 e também continuar sua jornada no Canvas 1. Para os usuários que não fizeram um pedido, eles continuam sua jornada apenas no Canvas 1.

### Comportamento de entrada {#entry-behavior}

A etapa Enviar para Destino insere os usuários no Canvas de destino assim que eles chegam a essa etapa. Ela funciona como um ponto de entrada único no Canvas de destino. Os usuários que atendem aos critérios de entrada e de público do Canvas de destino iniciam essa jornada no Canvas. Os usuários que não atendem a esses critérios naquele momento não entram no Canvas de destino e continuam no Canvas de origem.

Se o Canvas de destino usa um cronograma de entrada agendado, a etapa Enviar para Destino ignora esse cronograma de entrada. Ela também ignora a opção [**Limitar volume de entrada**]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) em **Controles de entrada** no Canvas de destino quando está definida como **Toda vez que o Canvas for agendado**. Os usuários enviados por essa etapa não aguardam a próxima janela de avaliação agendada — eles são avaliados e inseridos quando chegam à etapa Enviar para Destino, desde que atendam aos critérios de entrada e de público do Canvas de destino.

Se o Canvas de destino usa entrada baseada em ação, a etapa Enviar para Destino ignora a exigência de que os usuários realizem a ação de entrada configurada para entrar nesse Canvas.

## Criar uma etapa Enviar para Destino {#create-a-send-to-destination-step}

### Etapa 1: Adicionar uma etapa {#step-1-add-a-step}

Arraste e solte o componente **Send to Destination** da barra lateral, ou selecione o botão de adição <i class="fas fa-plus-circle"></i> na parte inferior de uma etapa e selecione **Send to Destination**.

### Etapa 2: Escolher o destino {#step-2-choose-your-destination}

Selecione o menu suspenso ou digite o nome do Canvas no campo **Destination**. Em seguida, selecione **Done**.

![Uma etapa Enviar para Destino configurada para enviar usuários de um Canvas chamado "Feature Adoption" para "New Canvas".]({% image_buster /assets/img/send_to_destination2.png %})

### Etapa 3: Pré-visualizar o destino {#step-3-preview-your-destination}

Você pode selecionar **Preview destination** para visualizar o Canvas para o qual está enviando os usuários.

Após configurar essa etapa do Canvas, você pode [pré-visualizar a jornada do usuário]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths) para verificar se um usuário avança para a próxima etapa no Canvas atual e se também segue para o Canvas de destino.

## Perguntas frequentes {#frequently-asked-questions}

### Posso definir o destino como um Canvas em rascunho? {#can-i-set-the-destination-to-a-draft-canvas}

Sim. O Canvas de destino pode ter status de rascunho ou sem atividades.

### As variáveis de contexto são preservadas? {#are-context-variables-preserved}

Sim. O [contexto]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) do Canvas de origem é sempre passado para o Canvas de destino.

### Posso usar a etapa Enviar para Destino para conectar Canvas em vez de usar soluções alternativas com API ou Atualização de usuário? {#can-i-use-the-send-to-destination-step-to-connect-canvases-instead-of-using-api-or-user-update-workarounds}

Sim. Você pode conectar Canvas com a etapa Enviar para Destino quando os usuários devem ser movidos diretamente para outra jornada de Canvas.

Não é necessário usar etapas separadas de Atualização de usuário, gatilhos de API ou webhooks apenas para mover usuários entre Canvas, desde que eles atendam aos critérios do Canvas de destino no momento do envio.

### Os usuários entram no início do Canvas de destino? {#do-users-enter-at-the-start-of-the-destination-canvas}

Os usuários elegíveis entram imediatamente na primeira etapa do Canvas de destino. Eles não aguardam um horário de entrada agendado posterior no Canvas de destino. Não é possível vincular a uma etapa específica do Canvas dentro do Canvas de destino.

### A etapa Enviar para Destino respeita o cronograma de entrada agendado do Canvas de destino? {#does-the-send-to-destination-step-respect-a-scheduled-destination-canvas-entry-schedule}

Não. Se o Canvas de destino usa um tipo de entrada agendada, os usuários enviados pela etapa Enviar para Destino não aguardam a próxima janela de avaliação agendada. Eles são avaliados e inseridos quando chegam à etapa Enviar para Destino, desde que atendam aos critérios de entrada e de público do Canvas de destino.

### Como funciona o comportamento de avanço nas etapas Enviar para Destino? {#how-does-advancement-behavior-work-for-send-to-destination-steps}

Os usuários que entram na etapa Enviar para Destino continuam sua jornada se houver etapas adicionais no Canvas de origem. Se os usuários também atenderem às regras de entrada do Canvas de destino, eles podem entrar nesse Canvas e iniciar essa jornada.