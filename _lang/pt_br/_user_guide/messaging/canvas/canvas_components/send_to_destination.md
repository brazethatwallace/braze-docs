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

> A etapa Enviar para Destino permite enviar usuários de um Canvas para outro. Por exemplo, se você tem dois Canvas que compartilham envio de mensagens de ofertas promocionais, pode usar o Enviar para Destino para conectar esses Canvas.

## Como funciona {#how-it-works}

![Uma etapa Enviar para Destino para enviar usuários a um novo Canvas.]({% image_buster /assets/img/send_to_destination1.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

O Canvas atual com a etapa Enviar para Destino é a origem. Dentro da etapa, você pode escolher o Canvas de destino. Os usuários que chegam do Canvas de origem devem seguir as regras de entrada do Canvas de destino. Digamos que você tenha dois Canvas:

- **Origem:** Canvas 1, inclui uma etapa Enviar para Destino que envia usuários para o Canvas 2
- **Destino:** Canvas 2, com os critérios de entrada para admitir usuários que fizeram um pedido

Essa etapa permite que os usuários do Canvas 1 sejam enviados para o Canvas 2. Quando os usuários do Canvas 1 entram na etapa Enviar para Destino, eles são avaliados pelas regras de entrada do Canvas 2 para determinar se são elegíveis para entrar no Canvas. Nesse caso, os usuários que fizeram um pedido podem entrar no Canvas 2 e também continuar sua jornada no Canvas 1. Para os usuários que não fizeram um pedido, eles continuam sua jornada apenas no Canvas 1.

## Criar uma etapa Enviar para Destino {#create-a-send-to-destination-step}

### Etapa 1: Adicionar uma etapa {#step-1-add-a-step}

Arraste e solte o componente **Send to Destination** da barra lateral, ou selecione o botão de adição <i class="fas fa-plus-circle" aria-label="Adicionar"></i> na parte inferior de uma etapa e selecione **Send to Destination**.

### Etapa 2: Escolher o destino {#step-2-choose-your-destination}

Selecione o menu suspenso ou digite o nome do Canvas no campo **Destination**. Em seguida, selecione **Done**.

![Uma etapa Enviar para Destino configurada para enviar usuários de um Canvas chamado "Feature Adoption" para "New Canvas".]({% image_buster /assets/img/send_to_destination2.png %})

### Etapa 3: Pré-visualizar o destino {#step-3-preview-your-destination}

Você pode selecionar **Preview destination** para ver a jornada dos usuários que atendem aos critérios de entrada do Canvas de destino.

Após configurar essa etapa do Canvas, você pode [pré-visualizar a jornada do usuário]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths/) para verificar se um usuário avança para a próxima etapa no Canvas atual e se também segue para o Canvas de destino.

## Perguntas frequentes {#frequently-asked-questions}

### Posso definir o destino como um Canvas em rascunho? {#can-i-set-the-destination-to-a-draft-canvas}

Sim. O Canvas de destino pode ter status de rascunho ou sem atividades.

### As variáveis de contexto são preservadas? {#are-context-variables-preserved}

Sim. O [contexto]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/) do Canvas de origem é sempre passado para o Canvas de destino.