---
nav_title: Jornadas de ação
article_title: Jornadas de ação
alias: /action_paths/
page_order: 1
page_type: reference
description: "Este artigo de referência aborda como usar as Jornadas de ação, um componente que permite classificar os usuários com base em suas ações."
tool: Canvas
---

# Jornadas de ação {#action-paths}

> As Jornadas de ação no Canvas permitem classificar seus usuários com base em suas ações.

![Uma etapa de Jornadas de ação em uma jornada de usuário no Canvas.]({% image_buster /assets/img/canvas_actionpath.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Com as Jornadas de ação, você pode:

* Personalizar as jornadas dos usuários com base em uma ação específica, incluindo eventos de engajamento e eventos personalizados
* Reter os usuários por um período determinado para priorizar a próxima jornada com base nas ações realizadas durante esse período de avaliação

## Criando uma jornada de ação {#creating-an-action-path}

Para criar uma jornada de ação, adicione um componente ao seu Canvas. Arraste e solte o componente da barra lateral ou selecione o botão de adição <i class="fas fa-plus-circle"></i> na parte inferior de uma etapa e selecione **Jornadas de ação**.

### Configurações de ação {#action-settings}

Em **Configurações de ação**, defina o **Período de avaliação** para determinar por quanto tempo os usuários ficam retidos na etapa. Por padrão, os usuários são avaliados dentro de um dia, mas você pode ajustar esse período por segundos, minutos, horas, dias e semanas, dependendo do seu Canvas. O período máximo de avaliação para uma jornada de ação é de 31 dias.

Em **Configurações de ação**, você também pode ativar a ordem de classificação dos seus componentes alternando a opção **Avançar usuários com base na ordem de classificação**.

![As Configurações de ação com um período de avaliação de 1 dia.]({% image_buster /assets/img/actionpath_settings.png %})

Por padrão, a **Classificação** está desativada. Quando um usuário entra na jornada de ação e realiza o evento de gatilho vinculado a qualquer grupo de ação, ele avança imediatamente pelo grupo de ação relevante com base na **primeira ação qualificada** que realizar após entrar na etapa. Se um usuário realizar uma segunda ação que corresponda a um grupo de ação diferente, ele não muda de jornada — a primeira ação determina seu caminho. Se um usuário não realizar um evento de gatilho, ele avança pelo grupo padrão **Restante do público** ao final do período de avaliação.

Quando a opção **Avançar usuários com base na ordem de classificação** está ativada, a **Classificação** fica ativa. Portanto, todos os usuários são retidos até o final do período de avaliação. Ao final desse período, os usuários avançam pelo grupo de ação de maior prioridade para o qual são elegíveis. Os usuários que não realizarem nenhuma das ações durante o período de avaliação avançam pelo grupo padrão **Restante do público**.

{% alert tip %}
Para direcionar os usuários com base em seus atributos atuais ou pertencimento a segmentos, em vez de ações realizadas, use as [Jornadas do público]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths/).
{% endalert %}

Observe que você pode disparar uma jornada de ação quando um objeto de atributo personalizado aninhado muda, mas não para vetores de atributos personalizados aninhados ou alterações em tipos de dados de vetor de objeto.

#### Mensagens no app {#in-app-messages}

Quando o gatilho do grupo de ação é iniciar uma sessão e a próxima etapa é uma mensagem no app, o usuário precisa iniciar duas sessões para receber a mensagem no app. A primeira sessão atribui o usuário ao grupo de ação dentro da jornada de ação, e a segunda sessão dispara a mensagem no app.

#### Exemplo de status de classificação {#ranking-status-example}

Digamos que você tenha uma jornada de ação com um período de avaliação de um dia e dois grupos de ação: Grupo 1 e Grupo 2. O Grupo 1 tem o evento de gatilho "Iniciar sessão" e o Grupo 2 tem "Realizar compra". Se a **Classificação** estiver ativada, todos os usuários na jornada de ação ficam "retidos" por um dia. Ao final do dia, se um usuário tiver iniciado uma sessão e realizado uma compra, ele avança pela jornada de maior classificação. Nesse caso, o usuário avançaria para o Grupo 1.

No exemplo anterior, se a **Classificação** estiver desativada e um usuário realizar um dos eventos de gatilho ("Iniciar sessão" ou "Realizar compra"), esse usuário avança no grupo de ação relevante com base na ação-gatilho.

Observe que as propriedades de entrada do Canvas são diferentes das propriedades de evento. As propriedades de entrada do Canvas são propriedades do evento que disparou o Canvas. Essas propriedades só podem ser usadas na primeira etapa completa de um Canvas ao usar o fluxo de trabalho original do Canvas. Ao usar o Canvas, as propriedades de entrada persistentes são ativadas e permitem que as propriedades de entrada sejam reutilizadas em todo o Canvas. Por outro lado, as propriedades de evento se originam de um evento ou ação que ocorre enquanto o usuário percorre seu fluxo de trabalho.

### Grupos de ação {#action-groups}

Adicione um ou vários gatilhos para definir seus grupos de ação. Aqui, você pode selecionar uma variedade de gatilhos, como quando os usuários:

- Realizam uma compra
- Iniciam uma sessão
- Realizam um [evento personalizado]({{site.baseurl}}/user_guide/data/activation/events/custom_events/)
- Realizam um evento de conversão
- Adicionam um endereço de e-mail
- Alteram o valor de um atributo personalizado.
  - Isso inclui adicionar um novo atributo com um valor a um perfil de usuário pela primeira vez (quando o atributo não existia anteriormente).
  - Gatilhos de atributo não estão disponíveis para atributos de vetor.
- Atualizam o status de inscrição ou o status do grupo de inscrições
- Interagem com uma Campaign ou cartão de conteúdo
- Entram em um local
- Disparam uma geofence
- Enviam uma mensagem de entrada por SMS ou WhatsApp

![Um grupo de ação chamado "Grupo 1" para usuários que realizam qualquer compra.]({% image_buster /assets/img/actionpath_group.png %})

Em cada configuração de grupo de ação, você também tem a opção de marcar a caixa de seleção **Quero que este grupo saia do Canvas**, o que significa que os usuários desse grupo sairão do Canvas ao final do período de avaliação.

### Canvas com reelegibilidade {#canvases-with-re-eligibility}

Se os usuários entrarem em uma jornada de ação várias vezes e tiverem múltiplas entradas na jornada de ação ao mesmo tempo, o comportamento esperado varia dependendo do status da **Classificação**.

| Status da classificação | Comportamento da jornada de ação |
|---|--------------|
| **Desativada** | Um usuário pode entrar em uma jornada de ação mais de uma vez. Essas entradas ficam retidas na jornada de ação até que uma ação-gatilho ou evento seja registrado. Se o evento de gatilho não satisfizer os filtros de propriedade de uma entrada (por exemplo, uma [variável de contexto]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_variables/) não corresponder aos filtros de propriedade do gatilho), a entrada permanece na jornada de ação. <br><br>Se o evento de gatilho satisfizer mais de uma entrada, a Braze faz a deduplicação apenas dessas entradas e avança imediatamente a entrada correspondente mais antiga pelo grupo de ação relevante. |
| **Ativada** | Todas as entradas avançam ao final do período de avaliação correspondente. Nenhuma deduplicação ocorre. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canvas com reelegibilidade" }

Observe que as classificações não são [editáveis após o lançamento]({{site.baseurl}}/post-launch_edits/).