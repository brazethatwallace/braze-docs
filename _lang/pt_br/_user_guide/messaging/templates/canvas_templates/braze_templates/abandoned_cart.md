---
nav_title: Carrinho abandonado
article_title: Carrinho abandonado
page_order: 1
page_type: reference
description: "Este artigo descreve como usar um modelo de Canvas da Braze para engajar usuários em tempo real e incentivá-los a concluir suas compras."
tool: Canvas
---

# Carrinho abandonado {#abandoned-cart}

> Engaje usuários em tempo real para incentivá-los a concluir suas compras. Use este modelo para criar uma jornada do usuário focada no envio de mensagens oportunas e personalizadas que lembrem os usuários de seus carrinhos abandonados, destacando os benefícios dos produtos e oferecendo incentivos, como códigos de desconto.

Neste artigo, vamos apresentar um caso de uso do modelo **Abandoned Intent**, que é destinado à etapa de consideração do ciclo de vida do usuário. Ao final deste artigo, você terá personalizado uma jornada do usuário que incentiva compras de usuários que não concluíram suas compras após adicionar itens aos carrinhos.

## Pré-requisitos {#prerequisites}

Para usar este modelo com sucesso, você precisará do seguinte:

- Uma jornada de Canvas separada para pós-compra, já que realizar uma compra neste Canvas fará com que os usuários saiam do Canvas.
- Uma [Sincronização de Público da Braze]({{site.baseurl}}/partners/canvas_audience_sync/) configurada com os parceiros e públicos que você utiliza.

## Adaptando o modelo às suas necessidades {#tailoring-the-template-to-your-needs}

Digamos que trabalhamos na Kitchenerie, uma marca de varejo especializada em utensílios de cozinha, e nosso objetivo é reengajar usuários que adicionaram o produto mais recente, "Enormous Paper Plate", aos seus carrinhos, mas não concluíram suas compras.

Antes de criar o Canvas, configuramos a integração [Sincronização de Público da Braze com o Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) para que possamos adicionar dados de usuários da Braze aos públicos do Facebook e enviar anúncios com base em gatilhos comportamentais, segmentação e muito mais.

Para acessar o modelo de intenção abandonada, ao criar um novo Canvas, selecione **Use a Canvas template** > **Braze templates**. Em seguida, ao lado de **Abandoned Intent**, selecione **Apply Template**. Agora, podemos percorrer o modelo para adaptá-lo às nossas necessidades.

### Etapa 1: Configure os detalhes {#step-1-set-up-the-details}

Vamos ajustar os detalhes do Canvas para refletir nosso objetivo.

1. Selecione **Edit** ao lado do nome do modelo.

![O título e a descrição atuais do Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent_old_name_description.png %}){: style="max-width:60%;"}

{:start="2"}
2. Atualize o nome do Canvas para especificar que ele é direcionado a usuários com carrinhos abandonados.
3. Atualize a descrição para especificar que o Canvas é para incentivar os usuários a concluírem compras do lançamento sazonal mais recente de utensílios de cozinha.
4. Adicione a tag **Abandon Cart** para que possamos filtrá-la na página inicial do Canvas.

![O novo nome, descrição e tag do Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent_new_name_description.png %}){: style="max-width:60%;"}

### Etapa 2: Atribua seus eventos de conversão {#step-2-assign-your-conversion-events}

Em seguida, vamos atribuir nosso evento de conversão. Como nosso foco é o produto "Enormous Paper Plate", faremos o seguinte para o **Evento de conversão primária A**:

1. Para o **Tipo de evento de conversão**, selecione **Makes Purchase**.
2. Selecione **Make a specific purchase**. Isso nos permite selecionar um nome de produto específico.
3. Selecione **Enormous Paper Plate**.

![Evento de conversão primária - A com o tipo de conversão "Makes Purchase" e o nome do produto "Enormous Paper Plate". Há um prazo de conversão de 3 dias.]({% image_buster /assets/img/canvas_templates/abandoned_intent1.png %})

### Etapa 3: Defina um cronograma de entrada {#step-3-set-an-entry-schedule}

Embora o cronograma de entrada deste modelo esteja definido como **Disparado por API**, nosso caso de uso se beneficiará mais com uma entrada baseada em ação para este Canvas, já que queremos focar em usuários que abandonaram seus carrinhos (o que é uma ação).

1. Selecione **Action-Based** como o tipo de cronograma de entrada.
2. Selecione **Abandoned Cart** como o gatilho.
3. Para o período de entrada, selecione a data de início.
4. Selecione a opção para permitir que os usuários entrem no fuso horário local deles. Isso pode manter nossas mensagens relevantes e levar a um maior engajamento se as mensagens forem enviadas em horários ideais.

![Um Canvas baseado em ação que direciona usuários que abandonaram seus carrinhos, com o período de entrada em 15 de outubro de 2024, 15h20, no fuso horário local dos usuários.]({% image_buster /assets/img/canvas_templates/abandoned_intent2.png %})

### Etapa 4: Determine quem entra no Canvas {#step-4-determine-who-enters-the-canvas}

Em seguida, vamos definir nosso público-alvo como usuários que compraram exclusivamente online conosco nos últimos 90 dias. Isso nos ajuda a restringir nosso público a usuários que sabemos que estão engajados com nossos produtos.

!["Online Shoppers Segment - 90 Days" como o Segment de usuários a ser direcionado para este Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent3.png %})

Vamos manter os controles de entrada como estão, para que os usuários não possam reentrar neste Canvas e não haja limite para o número de pessoas que podem potencialmente entrar neste Canvas.

Para os critérios de saída, os usuários sairão do Canvas se tiverem comprado o "Enormous Paper Plate". Dessa forma, eles não receberão mais mensagens sobre um item que já compraram.

![Critérios de saída que determinam que os usuários que fizerem uma compra específica do Enormous Paper Plate sairão do Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent4.png %})

### Etapa 5: Selecione suas configurações de envio {#step-5-select-your-send-settings}

Vamos manter as configurações de inscrição padrão, para que enviemos mensagens apenas para usuários que se inscreveram ou optaram por receber mensagens ou notificações, e deixar as outras configurações como estão.

### Etapa 6: Personalize seu Canvas {#step-6-customize-your-canvas}

Agora, vamos construir nosso Canvas personalizando as etapas do modelo:

1. Selecione a etapa Jornadas de ação e, em seguida, selecione o grupo de ação **Made purchase**.
2. Para **Make Purchase**, selecione **Make A Specific Purchase** e escolha **Enormous Paper Plate** como o produto. Semelhante aos critérios de saída, os usuários que comprarem este produto sairão do Canvas.

![Grupo de ação "Made purchase" que fará o usuário sair do Canvas se ele comprar o Enormous Paper Plate.]({% image_buster /assets/img/canvas_templates/abandoned_intent5.png %})

{: start="3"}
3. Na etapa Mensagem, selecione **Edit message** para personalizar o e-mail que será enviado aos nossos usuários, notificando-os sobre os itens em seus carrinhos abandonados.
4. Mantenha a etapa de postergação como está.
5. Nas etapas de Mensagem subsequentes à etapa Jornada do público, vamos personalizar o e-mail e a mensagem SMS que nossos usuários receberão. É aqui que queremos incentivar nossos usuários a comprar produtos com mensagens personalizadas.

![Uma pré-visualização da mensagem SMS que os usuários receberão: "Hi there, you left the enormous paper plate behind in your cart! Complete your purchase now and step up your hosting game. Use code MYPLATE at checkout for 20 percent off your order!"]({% image_buster /assets/img/canvas_templates/abandoned_intent6.png %})

{: start="6"}
6. Na próxima etapa Jornadas de ação, selecione o grupo de ação **Made purchase**. Em seguida, selecione **Make a specific purchase** e escolha **Enormous Paper Plate** como o produto. Esta etapa espelhará a primeira etapa de Jornadas de ação, fazendo com que os usuários que compraram nosso produto saiam para que não recebam mais mensagens.
7. Certifique-se de que nossa etapa de Sincronização de Público esteja configurada para sincronizar com o Facebook. Isso ajudará ainda mais com o redirecionamento de anúncios.

{% alert tip %}
Você pode usar as [propriedades de entrada do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/) para personalizar as mensagens no seu Canvas com base no produto ao qual você está se referindo.
{% endalert %}

### Etapa 7: Teste e lance o Canvas {#step-7-test-and-launch-the-canvas}

Após testar e revisar nosso Canvas para garantir que ele funcione conforme esperado, selecione **Launch Canvas** para lançar o Canvas. Agora, podemos direcionar usuários de forma consciente com uma jornada personalizada para incentivá-los a finalizar a compra do produto que adicionaram aos seus carrinhos!

{% alert tip %}
Confira nossa [Lista de verificação pré e pós-lançamento]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) para saber o que considerar antes e depois de lançar um Canvas.
{% endalert %}