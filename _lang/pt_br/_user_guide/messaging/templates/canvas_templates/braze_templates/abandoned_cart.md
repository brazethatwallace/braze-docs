---
nav_title: Intenção abandonada
article_title: Intenção abandonada
page_order: 1
page_type: reference
description: "Este artigo descreve como usar um modelo de Canvas da Braze para engajar usuários em tempo real e incentivá-los a concluir suas compras."
tool: Canvas
---

# Intenção abandonada {#abandoned-intent}

> Engaje usuários em tempo real para incentivá-los a concluir suas compras enquanto os produtos ainda estão frescos na memória. Este modelo disparado por API insere os usuários imediatamente quando abandonam um carrinho, envia lembretes oportunos pelo canal ideal (e-mail, SMS ou mensagem no app), verifica a conclusão da compra em dois pontos da jornada e sincroniza os usuários que não convertem com públicos de anúncios para redirecionamento.

Neste artigo, vamos apresentar um caso de uso do modelo **Abandoned Intent**, que é destinado à etapa de consideração do ciclo de vida do usuário. Ao final deste artigo, você terá personalizado uma jornada do usuário que incentiva compras de usuários que não concluíram suas compras após adicionar itens aos carrinhos.

{% alert tip %}
Use o [BrazeAI Operator<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/operator) para configurar e personalizar este modelo. Selecione **BrazeAI Operator<sup>TM</sup>** ao lado do seu perfil de usuário ao criar ou editar seu Canvas. Em seguida, descreva seu objetivo, como "Me ajude a configurar o modelo Abandoned Intent para reengajar usuários que abandonaram o carrinho".
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar este modelo com sucesso, você precisará do seguinte:

- Uma jornada de Canvas separada para pós-compra, já que realizar uma compra neste Canvas fará com que os usuários saiam do Canvas.
- Uma [Sincronização de Público da Braze]({{site.baseurl}}/partners/canvas_audience_sync) configurada com os parceiros e públicos que você utiliza.

## Adaptando o modelo às suas necessidades {#tailoring-the-template-to-your-needs}

Digamos que trabalhamos na Kitchenerie, uma marca de varejo especializada em utensílios de cozinha, e nosso objetivo é reengajar usuários que adicionaram o produto mais recente, "Enormous Paper Plate", aos seus carrinhos, mas não concluíram suas compras.

Antes de criar o Canvas, configuramos a integração [Sincronização de Público da Braze com o Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync) para que possamos adicionar dados de usuários da Braze aos públicos do Facebook e enviar anúncios com base em gatilhos comportamentais, segmentação e muito mais.

O modelo **Abandoned Intent** segue este fluxo: verificar compra, enviar um lembrete imediato, aguardar, direcionar para o canal ideal, fazer acompanhamento, verificar novamente e redirecionar os que não converteram. Ele inclui as seguintes etapas:

| Etapa do Canvas | Nome da etapa no modelo | Finalidade |
|---|---|---|
| Jornadas de ação | Made purchase? | Primeira verificação de conclusão; usuários que já compraram saem do Canvas. |
| Mensagem | Itemized Reminder | Lembrete imediato do carrinho enviado logo após a entrada. |
| Postergação | Delay | Espera de 30 minutos para que o acompanhamento chegue enquanto o produto ainda está fresco na memória. |
| Jornadas do público | Intelligent Channel split | Direciona os usuários para e-mail ou SMS com base na classificação do [Canal Inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel). |
| Mensagem | Abandoned Cart Email, Abandoned Cart SMS e Abandoned Cart In-App Message | Acompanhamentos específicos por canal. O Canal Inteligente seleciona entre e-mail e SMS; a mensagem no app é enviada em uma jornada separada no modelo. |
| Jornadas de ação | Made purchase? (2) | Segunda verificação de conclusão antes do redirecionamento. |
| Sincronização de Público | Ad Retargeting | Sincroniza os que não converteram com públicos de anúncios (como Facebook) para redirecionamento fora do canal. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Etapas do modelo Abandoned Intent" }

### Etapa 1: Configure os detalhes {#step-1-set-up-the-details}

Vamos aplicar o modelo de Canvas e atualizar os detalhes para refletir nosso objetivo.

1. Acesse **Messaging** > **Canvas**.
2. Selecione **Create Canvas** > **Use a Canvas Template**.
3. Selecione a guia **Braze templates** e, em seguida, selecione **Apply Template** ao lado de **Abandoned Intent**.
4. Atualize a descrição para especificar que o Canvas é para incentivar os usuários a concluírem compras do lançamento sazonal mais recente de utensílios de cozinha.
5. Adicione a tag **Intent** para que possamos filtrá-la na página inicial do Canvas.

![O novo nome, descrição e tag do Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent_new_name_description.png %}){: style="max-width:60%;"}

### Etapa 2: Atribua seus eventos de conversão {#step-2-assign-your-conversion-events}

O modelo define o **Evento de conversão primária - A** como **Makes Purchase (Legacy)** com **Make any purchase (Legacy)** selecionado por padrão. Como nosso foco é o produto "Enormous Paper Plate", personalizamos o evento de conversão da seguinte forma:

1. Selecione **Make a specific purchase (Legacy)**.
2. Em **Product name**, insira **Enormous Paper Plate**.

![Evento de conversão primária - A com o tipo de conversão "Makes Purchase" e o nome do produto "Enormous Paper Plate". Há um prazo de conversão de 3 dias.]({% image_buster /assets/img/canvas_templates/abandoned_intent1.png %})

{% alert note %}
Se o seu espaço de trabalho usa o evento de conversão **Places order**, as opções relacionadas a compras podem aparecer com **(Legacy)** no rótulo. As etapas neste artigo usam o fluxo de conversão de compra legado.
{% endalert %}

### Etapa 3: Defina um cronograma de entrada {#step-3-set-an-entry-schedule}

O modelo **Abandoned Intent** usa um cronograma de entrada **Disparado por API** para que você possa inserir os usuários no Canvas assim que eles abandonarem o carrinho. Isso se encaixa no nosso caso de uso porque queremos responder enquanto o produto ainda está fresco na memória.

1. Mantenha **API-Triggered** como o tipo de cronograma de entrada.
2. Anote o ID do Canvas e use o [endpoint `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) para adicionar usuários quando seu app ou site detectar um carrinho abandonado.
3. Opcionalmente, você pode passar [variáveis de contexto]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) (como nome do produto ou detalhes do carrinho) para personalizar as mensagens subsequentes.

Se preferir uma entrada baseada em ação, selecione **Action-Based** e escolha um gatilho que corresponda à forma como sua marca rastreia carrinhos abandonados — por exemplo, **Perform Custom Event** para um evento `abandoned_cart` registrado.

### Etapa 4: Determine quem entra no Canvas {#step-4-determine-who-enters-the-canvas}

Em seguida, vamos definir nosso público-alvo como usuários que compraram exclusivamente online conosco nos últimos 90 dias. Isso nos ajuda a restringir nosso público a usuários que sabemos que estão engajados com nossos produtos.

!["Online Shoppers Segment - 90 Days" como o segmento de usuários a ser direcionado para este Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent3.png %})

Vamos manter os controles de entrada como estão, para que os usuários não possam reentrar neste Canvas e não haja limite para o número de pessoas que podem potencialmente entrar neste Canvas.

O modelo não define critérios de saída globais por padrão. Em vez disso, os usuários saem quando fazem uma compra nas etapas de Jornadas de ação **Made purchase?**, que personalizaremos na Etapa 6.

### Etapa 5: Selecione suas configurações de envio {#step-5-select-your-send-settings}

Vamos manter as configurações de inscrição padrão, para que enviemos mensagens apenas para usuários que se inscreveram ou optaram por receber mensagens ou notificações, e deixar as outras configurações como estão.

### Etapa 6: Personalize seu Canvas {#step-6-customize-your-canvas}

Personalize as etapas do Canvas na ordem em que os usuários as experimentam:

#### Verificar compra na entrada {#check-for-purchase-at-entry}

1. Selecione a etapa de Jornadas de ação **Made purchase?** e, em seguida, selecione o grupo de ação **Made purchase**.
2. Em **Make Purchase**, selecione **Make a specific purchase (Legacy)** e escolha **Enormous Paper Plate** como o produto. Os usuários que comprarem este produto sairão do Canvas.

#### Enviar o lembrete imediato {#send-the-immediate-reminder}

1. Selecione a etapa de Mensagem **Itemized Reminder** e, em seguida, selecione **Edit message** para personalizar o primeiro e-mail de lembrete. Esta mensagem é enviada imediatamente após a entrada, antes da postergação.
2. Mantenha a etapa de **Postergação** como está. O modelo usa uma postergação de 30 minutos antes do envio das mensagens de acompanhamento, dando aos usuários tempo para concluir a compra enquanto o produto ainda está fresco na memória.

{% alert tip %}
Você pode usar as [propriedades de contexto do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) para personalizar as mensagens no seu Canvas com base no produto ao qual você está se referindo.
{% endalert %}

#### Direcionar para o canal ideal {#route-to-the-optimal-channel}

1. Revise a etapa de Jornadas do público **Intelligent Channel split**. Ela direciona os usuários para **Abandoned Cart Email** ou **Abandoned Cart SMS** com base na classificação do [Canal Inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel). Ajuste as jornadas conforme necessário.
2. Personalize as etapas **Abandoned Cart Email**, **Abandoned Cart SMS** e **Abandoned Cart In-App Message**. Selecione **Edit message** em cada etapa para atualizar o texto e a mensagem daquele canal. A mensagem no app é executada em uma jornada separada da divisão do Canal Inteligente e não é selecionada pela classificação do Canal Inteligente.

#### Redirecionar os que não converteram {#retarget-non-converters}

1. Selecione a etapa de Jornadas de ação **Made purchase? (2)** e, em seguida, selecione o grupo de ação **Made purchase**.
2. Selecione **Make a specific purchase (Legacy)** e escolha **Enormous Paper Plate** como o produto. Os usuários que comprarem aqui saem do Canvas antes de chegar ao redirecionamento.
3. Selecione a etapa de Sincronização de Público **Ad Retargeting** e configure-a para sincronizar com o Facebook. Os usuários que chegam a esta etapa não compraram — sincronize-os com seu público de anúncios para redirecionamento fora do canal.

### Etapa 7: Teste e lance o Canvas {#step-7-test-and-launch-the-canvas}

Após testar e revisar nosso Canvas para garantir que ele funcione conforme esperado, selecione **Launch Canvas** para lançar o Canvas. Agora, podemos direcionar usuários de forma consciente com uma jornada personalizada para incentivá-los a finalizar a compra do produto que adicionaram aos seus carrinhos!

{% alert tip %}
Confira nossa [Lista de verificação pré e pós-lançamento]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist#things-to-consider-before-launch) para saber o que considerar antes e depois de lançar um Canvas.
{% endalert %}