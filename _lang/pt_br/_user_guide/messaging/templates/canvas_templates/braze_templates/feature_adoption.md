---
nav_title: Adoção de funcionalidades
article_title: Adoção de funcionalidades
page_order: 3
page_type: reference
description: "Este artigo descreve como usar um modelo de Canvas da Braze para enviar mensagens personalizadas e oportunas que destacam os benefícios e dicas de uso."
tool: Canvas
---

# Adoção de funcionalidades {#feature-adoption}

> Este modelo foi criado para impulsionar o uso de novas funcionalidades, produtos existentes, ofertas adicionais ou qualquer outra área que você queira que seus clientes experimentem. Ao aproveitar a comunicação personalizada e um conjunto estruturado de mensagens, você pode apresentar novas funcionalidades aos usuários de forma integrada e obter feedback valioso deles.

Neste artigo, vamos apresentar um caso de uso para o modelo **Feature Adoption**, voltado para as etapas de retenção e fidelidade do ciclo de vida do usuário. Ao final deste artigo, você terá personalizado uma jornada de usuário que incentiva os usuários a usar novas funcionalidades e coleta o sentimento dos usuários.

## Pré-requisitos {#prerequisites}

Para usar este modelo com sucesso, você precisará de um [evento personalizado]({{site.baseurl}}/user_guide/data/activation/events/custom_events) que registre quando os usuários utilizaram a funcionalidade.

## Adaptando o modelo às suas necessidades {#tailoring-the-template-to-your-needs}

Digamos que você trabalha na Calorie Rocket, um app de entrega de comida que lançou recentemente o Cruise Control, uma funcionalidade para agendar entregas recorrentes de comida, e você quer incentivar mais usuários a adotar essa nova funcionalidade. No nosso exemplo, usaremos o evento personalizado `scheduled_delivery` para rastrear quando os usuários experimentaram a funcionalidade Cruise Control.

Para acessar o modelo de volta ao estoque, ao criar um novo Canvas, selecione **Use a Canvas template** > **Braze templates**. Em seguida, ao lado de **Feature Adoption**, selecione **Apply Template**. Agora, podemos percorrer o modelo para adaptá-lo às nossas necessidades.

### Etapa 1: Configure os detalhes {#step-1-set-up-the-details}

Vamos ajustar os detalhes do Canvas para refletir nosso objetivo.

1. Selecione **Edit** ao lado do nome do modelo.

![O título e a descrição atuais do Canvas.]({% image_buster /assets/img/canvas_templates/feature_adoption/select_edit_details.png %}){: style="max-width:60%;"}

{:start="2"}
2. Atualize o nome do Canvas para especificar que ele é voltado para direcionar usuários e coletar feedback.
3. Atualize a descrição para especificar que o Canvas é para incentivar os usuários a enviar feedback e rastrear o sentimento dos usuários sobre a nova funcionalidade Cruise Control.
4. Adicione a tag **Feature adoption** para que possamos filtrá-la na página inicial do Canvas.

![O novo nome e descrição do Canvas. A nova descrição diz: "Um Canvas de adoção de funcionalidades para rastrear a adoção e o sentimento dos usuários sobre o Cruise Control, uma funcionalidade para agendar entregas recorrentes de comida."]({% image_buster /assets/img/canvas_templates/feature_adoption/enter_new_canvas_name.png %}){: style="max-width:60%;"}

### Etapa 2: Atribua um evento de conversão {#step-2-assign-a-conversion-event}

Em seguida, vamos adicionar um evento de conversão ao nosso Canvas para sinalizar a adoção da funcionalidade. Isso nos permitirá personalizar a jornada experimental na jornada do usuário mais adiante.

1. Em **Assign Conversion Events**, selecione **Add Conversion Event**.
2. Em **Primary Conversion Event - A**, selecione **Performs Custom Event** como o **Conversion event type**.
3. Selecione nosso evento personalizado `scheduled_delivery`.
4. Vamos manter o prazo de conversão como três dias.

![A janela de evento de conversão no Canvas.]({% image_buster /assets/img/canvas_templates/feature_adoption/assign_conversion_event_cruise_control.png %}){: style="max-width:90%;"}

### Etapa 3: Adapte o cronograma de entrada {#step-3-tailor-the-entry-schedule}

Nosso objetivo é incentivar nossos usuários a adotar o Cruise Control, mas não queremos que nossas mensagens sejam muito frequentes. Então, vamos manter este Canvas como entrega agendada e fazer os seguintes ajustes na seção **Time-Based Options**.

1. Atualize a **Entry Frequency** para **Weekly**.
2. Mantenha a recorrência como está.
3. Selecione **Mon** para direcionar os usuários no início da semana.
4. Selecione o horário de início do nosso Canvas.
5. Atualize os **Ending parameters** para encerrar o Canvas no último dia do ano.

Vamos manter a opção de permitir que os usuários entrem no Canvas no horário local deles.

### Etapa 4: Selecione o público-alvo {#step-4-select-the-target-audience}

Agora, vamos configurar nosso público-alvo atualizando os seguintes detalhes no modelo:

1. Selecione o segmento **All Users**.
2. Remova os filtros adicionais do modelo.
3. Crie este filtro usando nosso evento personalizado: `Has scheduled_delivery for exactly 0 times`. Isso nos permite excluir os usuários que já usaram a funcionalidade de entrar no nosso Canvas.

![O segmento para todos os usuários que não usaram o Cruise Control.]({% image_buster /assets/img/canvas_templates/feature_adoption/cruise_control_segment.png %}){: style="max-width:90%;"}

{: start="4"}
4. Tendo em mente que a Calorie Rocket permitiu anteriormente que alguns usuários fizessem testes beta da nova funcionalidade Cruise Control, vamos atualizar os critérios de saída para excluir esses usuários de entrar no Canvas.

### Etapa 5: Selecione suas configurações de envio {#step-5-select-your-send-settings}

Vamos manter as configurações de inscrição padrão, para enviar apenas para usuários que se inscreveram ou optaram por receber mensagens ou notificações, e pular as outras configurações (limite de frequência, horário de silêncio e grupos de teste).

### Etapa 6: Personalize seu Canvas {#step-6-customize-your-canvas}

#### Construa a jornada de ação {#build-out-the-action-path}

Em seguida, vamos construir a primeira etapa de jornada de ação, que serve para indicar se nossos usuários têm interesse na nova funcionalidade. Faremos os seguintes ajustes no modelo:

1. Como a funcionalidade Cruise Control só está disponível depois que um pedido é adicionado ao carrinho, vamos nomear o primeiro grupo de ação como **Added to cart** e selecionar `added_to_cart` para o evento personalizado.

![O nome do grupo de ação definido como "Added to cart" e o "Perform Custom Event" definido como "added_to_cart".]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_added_to_cart.png %}){: style="max-width:60%;"}

{: start="2"}
2. Mantenha o segundo grupo de ação **Taken Tour** como está, pois queremos avaliar se os usuários fizeram um tour pelo app e, se fizeram, eles avançarão para a segunda jornada.
3. Para a jornada de ação subsequente chamada **Assess Usage**, substitua **Used Feature >3x** por **Viewed Cruise Control settings**.
4. Selecione o menu suspenso **Perform Custom Event** e, em seguida, selecione `scheduled_delivery` para o evento personalizado.

![O nome do grupo de ação definido como "Used Feature >3x" e o "Perform Custom Event" definido como "scheduled_delivery".]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_assess_usage.png %}){: style="max-width:60%;"}

#### Configure a pesquisa de feedback {#set-up-feedback-survey}

Em seguida, vamos até a etapa de mensagem chamada **Feedback Survey** para incluir nossa pesquisa de feedback para os usuários preencherem após usar o Cruise Control pela primeira vez. As opções de resposta da pesquisa para nossos usuários são:

- **Loved it!**
- **Not for me.**

1. Para as duas opções da pesquisa, selecione **Experience Feedback** como nosso atributo personalizado para capturar e rastrear o feedback sobre o Cruise Control. Esse atributo personalizado terá dois valores para representar as respostas da pesquisa (`good` e `bad`).
2. Atualize os valores do atributo para corresponder às opções da pesquisa. Isso nos permitirá rastrear a resposta de um usuário.

### Etapa 7: Teste e lance seu Canvas {#step-7-test-and-launch-your-canvas}

Após testar e revisar nosso Canvas para garantir que ele funciona como esperado, selecione **Launch Canvas** para lançar o Canvas. Agora, podemos direcionar os usuários com uma jornada personalizada para incentivá-los a adotar nossa nova funcionalidade Cruise Control.

{% alert tip %}
Confira nossa [lista de verificação pré e pós-lançamento]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist#things-to-consider-before-launch) para saber o que considerar antes e depois de lançar um Canvas.
{% endalert %}