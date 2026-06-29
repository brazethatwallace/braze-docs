---
nav_title: Enviar mensagens para usuários
article_title: Enviar mensagens para usuários
page_order: 3
description: "Este artigo de referência aborda como conversar com usuários usando Campaigns e Canvas com modelos."
page_type: reference
channel:
 - LINE
alias: /line/messaging_users/
---

# Enviar mensagens para usuários LINE {#message-line-users}

> LINE é um canal de comunicação bidirecional. Você pode ir além de simplesmente enviar mensagens e engajar em conversas com os usuários usando Campaigns e Canvas com modelos. Este artigo aborda os detalhes do envio de mensagens para usuários, como definir palavras-gatilho para mensagens recebidas e respostas não reconhecidas.

Existem vários métodos para conversar com os usuários pelo LINE, como usar palavras-gatilho do LINE. Você também pode usar chamadas para ação (CTAs) para incentivar o engajamento dos usuários com suas mensagens LINE.

## Gatilhos baseados em ação {#action-based-triggers}

Você pode criar Campaigns e Canvas que iniciam, ramificam e têm alterações no meio da jornada quando você recebe uma mensagem LINE de entrada (uma mensagem enviada por um usuário) que contém uma palavra-gatilho. Certifique-se de escolher palavras-gatilho que correspondam ao que você espera que os usuários enviem.

### Campaign

Defina suas palavras-gatilho ao agendar uma Campaign com entrega baseada em ação.

![Gatilho baseado em ação com a mensagem "Enviar esta campanha para usuários que enviaram LINE de entrada para o grupo de inscrições onde o corpo da mensagem é" e um campo em branco.]({% image_buster /assets/img/line/trigger_word_campaign.png %})

### Canvas

Defina suas palavras-gatilho dentro das [jornadas de ação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) no seu Canvas.

![Jornada de ação com um gatilho de "Enviar esta campanha para usuários que enviaram LINE de entrada para o grupo de inscrições onde o corpo da mensagem é" e um campo em branco.]({% image_buster /assets/img/line/trigger_word_canvas.png %})

### Requisitos {#requirements}

Cada letra da sua palavra-gatilho deve estar em maiúscula ao criar sua Campaign ou Canvas, mesmo que a Braze não exija que as palavras-gatilho de entrada estejam em maiúsculas. Por exemplo, se sua palavra-gatilho for "JOIN2023", uma mensagem de entrada "jOin2023" ainda acionará o Canvas ou a Campaign.

Se nenhuma palavra-gatilho for especificada, a Campaign ou o Canvas será executado para *todas* as mensagens LINE de entrada. Isso inclui mensagens que correspondem a frases em Campaigns e Canvas ativos, caso em que o usuário receberá duas mensagens LINE.

## Respostas não reconhecidas {#unrecognized-responses}

Você deve incluir uma opção de gatilho para respostas não reconhecidas em Canvas interativos. Isso informa os usuários sobre os prompts disponíveis (ou palavras-gatilho) e define suas expectativas para o canal.

### Criando um gatilho para respostas não reconhecidas {#creating-a-trigger-for-unrecognized-responses}

Após criar grupos de ação para as frases de filtro personalizadas, adicione outro grupo de ação à jornada de ação para **Enviar mensagem LINE** e não marque **Onde o corpo da mensagem**. Isso capturará todas as respostas não reconhecidas dos usuários, semelhante a uma cláusula "else".

Para essa mensagem, você deve enviar uma mensagem LINE informando o usuário que este canal não é monitorado por uma pessoa e, se necessário, direcioná-lo a um canal de suporte.