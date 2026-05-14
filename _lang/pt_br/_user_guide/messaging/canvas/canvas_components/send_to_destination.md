---
nav_title: Enviar para Destino
article_title: Enviar para Destino
alias: "/send_to_destination/"
page_order: 11.5
page_type: reference
description: "Este artigo de referência aborda o componente Enviar para Destino e como usá-lo nos seus Canvas."
tool: Canvas
---

# Etapa Enviar para Destino

> A etapa Enviar para Destino permite enviar usuários de um Canvas para outro. Por exemplo, se você tem dois Canvas que compartilham envio de mensagens de ofertas promocionais, pode usar o Enviar para Destino para conectar esses Canvas.

## Como funciona

![Uma etapa Enviar para Destino para enviar usuários a um novo Canvas.]({% image_buster /assets/img/send_to_destination1.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

O Canvas atual com a etapa Enviar para Destino é a origem. Dentro da etapa, você pode escolher o Canvas de destino. A partir daí, os usuários são enviados para o Canvas de destino. Eles seguirão por esse Canvas se atenderem aos critérios de entrada e também continuarão avançando pelo Canvas de origem.

## Criar uma etapa Enviar para Destino

### Etapa 1: Adicionar uma etapa

Arraste e solte o componente **Enviar para Destino** da barra lateral, ou selecione o botão de adição <i class="fas fa-plus-circle"></i> na parte inferior de uma etapa e selecione **Enviar para Destino**.

### Etapa 2: Escolher o destino

Selecione o menu suspenso ou digite o nome do Canvas no campo **Destino**. Em seguida, selecione **Concluído**.

![Uma etapa Enviar para Destino configurada para enviar usuários de um Canvas chamado "Feature Adoption" para "New Canvas".]({% image_buster /assets/img/send_to_destination2.png %})

### Etapa 3: Pré-visualizar o destino

Você pode selecionar **Pré-visualizar destino** para ver a jornada dos usuários que atendem aos critérios de entrada do Canvas de destino.

Após configurar essa etapa do Canvas, você pode [pré-visualizar a jornada do usuário]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths) para verificar se um usuário avança para a próxima etapa no Canvas atual e se também segue para o Canvas de destino.

## Perguntas frequentes

### Posso definir o destino como um Canvas em rascunho?

Sim. O Canvas de destino pode ter status de rascunho ou sem atividades.

### As variáveis de contexto são preservadas?

Sim. O [contexto]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) do Canvas de origem é sempre passado para o Canvas de destino.