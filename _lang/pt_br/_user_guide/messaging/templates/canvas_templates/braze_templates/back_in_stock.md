---
nav_title: De volta ao estoque
article_title: De volta ao estoque
page_order: 2
page_type: reference
description: "Este artigo descreve como usar um modelo de Canvas da Braze para impulsionar compras notificando seus usuários quando um item está de volta ao estoque com mensagens personalizadas."
tool: Canvas
---

# De volta ao estoque {#back-in-stock}

> Use o modelo de volta ao estoque para criar mensagens direcionadas a usuários que visualizaram ou demonstraram interesse em um item que estava fora de estoque, mas agora está disponível para compra. Isso ajuda os usuários a obterem os produtos que desejam, engajando-os no momento crítico em que um produto volta a estar disponível.

Este artigo vai guiar você por um caso de uso do modelo **De volta ao estoque**, que é projetado para a etapa de conversão do ciclo de vida do usuário. Ao finalizar, você terá criado um Canvas que envia push (web ou celular), SMS ou e-mail para os usuários quando um item estiver de volta ao estoque, além de até dois lembretes.

## Pré-requisitos {#prerequisites}

Para usar este modelo com sucesso, você precisará do seguinte:

- Um [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/create) contendo informações sobre seu item
- [Notificações de volta ao estoque]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications#how-back-in-stock-notifications-work) devem estar configuradas para o item sobre o qual você deseja enviar mensagens aos usuários

## Adaptando o modelo às suas necessidades {#tailoring-the-template-to-your-needs}

Digamos que trabalhamos para a PantsLabyrinth, uma varejista de roupas direta ao consumidor especializada em calças sociais, jeans, culottes e muitos outros tipos de calças. Podemos usar o modelo de volta ao estoque para notificar clientes em vários canais quando um par popular de jeans, o Classic Straight Leg, estiver de volta ao estoque.

Antes de criar o Canvas, [configuramos um catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/create) que contém informações sobre nosso inventário de calças de corte reto e [configuramos notificações de volta ao estoque]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications#setting-up-back-in-stock-notifications) para o jeans Classic Straight Leg. Fizemos com que os usuários se inscrevam nas notificações após realizarem o evento personalizado de favoritar o jeans Classic Straight Leg no app.

Para acessar o modelo de volta ao estoque, ao criar um novo Canvas, selecione **Use a Canvas template** > **Braze templates**. Em seguida, ao lado de **Back in Stock**, selecione **Apply Template**. Agora, podemos percorrer o modelo para adaptá-lo às nossas necessidades.

### Etapa 1: Configurar os detalhes {#step-1-set-up-the-details}

Vamos ajustar os detalhes do Canvas para refletir nosso objetivo.

1. Selecione **Edit** ao lado do nome do modelo.

![O título e a descrição atuais do Canvas.]({% image_buster /assets/img/canvas_templates/back_in_stock_old_name_description.png %}){: style="max-width:45%;"}

{:start="2"}
2. Atualize o nome do Canvas para especificar que ele é direcionado a usuários quando nosso produto Classic Straight Leg estiver de volta ao estoque.
3. Atualize a descrição para explicar que este Canvas contém mensagens personalizadas.
4. Adicione a tag **Back in Stock**, que está aninhada sob a tag **Promotional**, para que possamos filtrá-la na página inicial do Canvas.

![Etapa "Configurar detalhes do Canvas" com o nome "Back in Stock - Classic Straight Leg" e uma breve descrição do Canvas.]({% image_buster /assets/img/canvas_templates/back_in_stock_1.png %})

### Etapa 2: Atribuir eventos de conversão {#step-2-assign-conversion-events}

Altere o **Primary Conversion Event - A** para **Make a specific purchase** e selecione **Classic Straight Leg** como o nome do produto.

![Seção "Atribuir eventos de conversão" para o tipo de evento de conversão de compra do produto Classic Straight Leg com um prazo de conversão de 7 dias.]({% image_buster /assets/img/canvas_templates/back_in_stock_2.png %})

### Etapa 3: Adaptar o cronograma de entrada {#step-3-tailor-the-entry-schedule}

Vamos manter o cronograma de entrada como **Action-Based** para que os usuários entrem no nosso Canvas quando realizarem uma ação, que o modelo já definiu como **Perform a Back in Stock Event**.

Faremos dois ajustes nesta etapa:

1. Selecione o catálogo que inclui informações sobre nosso jeans Classic Straight Leg, que nomeamos como "Straight Leg Pants".

![Etapa "Cronograma de entrada" para um Canvas baseado em ação.]({% image_buster /assets/img/canvas_templates/back_in_stock_3.png %})

{: start="2"}
2. Defina o **Start Time (Required)** para a data e hora de início desejadas.

![Seção "Janela de entrada" com horário de início em 2 de janeiro de 2025 às 00h.]({% image_buster /assets/img/canvas_templates/back_in_stock_4.png %})

### Etapa 4: Selecionar o público-alvo {#step-4-select-the-target-audience}

Vamos definir nosso público-alvo como usuários que acreditamos ter maior probabilidade de comprar o jeans Classic Straight Leg.

1. Selecione nosso segmento alvo, "Favorited - Classic Straight Leg Jeans", que consiste em usuários que favoritaram nosso jeans Classic Straight Leg no app ou site.
2. Selecione um filtro para incluir usuários que compraram "Jeans" mais de "0" vezes.

![Etapa "Público-alvo" com o segmento "Favorited - Classic Straight Leg Jeans".]({% image_buster /assets/img/canvas_templates/back_in_stock_5.png %})

{: start="3"}
3. Ajuste os controles de entrada para permitir que os usuários reentrem no Canvas após a duração máxima do Canvas, para reduzir a probabilidade de os usuários acionarem a mesma etapa simultaneamente.

![Seção "Controles de entrada" com uma caixa de seleção para permitir que os usuários reentrem neste Canvas com a duração máxima do Canvas.]({% image_buster /assets/img/canvas_templates/back_in_stock_6.png %})

{: start="4"}
4. Ajuste os critérios de saída para remover usuários que realizaram o evento personalizado de desfavoritar o jeans Classic Straight Leg.

![Seção "Critérios de saída" com uma exceção para usuários que realizam o evento personalizado "Unfavorited".]({% image_buster /assets/img/canvas_templates/back_in_stock_7.png %})

### Etapa 5: Selecionar suas configurações de envio {#step-5-select-your-send-settings}

Vamos manter as configurações de inscrição padrão, para enviar apenas a usuários que se inscreveram ou optaram por receber mensagens ou notificações, e pular as outras configurações (limite de frequência, horário de silêncio e grupos de teste).

![Etapa "Configurações de envio" direcionada a usuários que estão inscritos ou optaram por receber.]({% image_buster /assets/img/canvas_templates/back_in_stock_8.png %})

### Etapa 6: Personalizar seu Canvas {#step-6-customize-your-canvas}

Agora, vamos construir nosso Canvas personalizando os canais e o conteúdo que serão enviados aos usuários. Como estamos usando todos os quatro canais do modelo (push para celular e web, SMS e e-mail) e usando o filtro [Canal Inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel), não precisamos adicionar ou remover nenhum.

{% alert tip %}
Você pode usar [propriedades de entrada do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) para personalizar as mensagens no seu Canvas com base no produto ao qual você está se referindo.
{% endalert %}

Vamos começar nossa personalização percorrendo cada etapa de mensagem para atualizar o conteúdo.

1. Substitua `!!YOURCATALOGHERE!!` pelo nome do nosso catálogo ("Straight_Leg_Pants").
2. Substitua `[0]` pelo número de índice do jeans Classic Straight Leg, que é "9" porque o jeans é o décimo item no array `items` do nosso catálogo. (Os arrays são indexados a partir de zero em Liquid, então o primeiro item é `0` e não `1`.)
3. Repita as etapas 1 e 2 para todas as etapas de mensagem restantes, incluindo:
    - A mensagem "In-Product Msg & Email" que é enviada após uma postergação de um dia
    - As mensagens "Push+Email Alert" que são enviadas para usuários que não realizaram uma compra
4. Atualize a etapa de jornadas de ação selecionando o grupo de ação **Purchase**. Em seguida, selecione **Make a specific purchase** e escolha o jeans Classic Straight Leg como produto.

![Etapa de push para celular do Canvas com uma mensagem notificando os usuários de que um produto está de volta ao estoque.]({% image_buster /assets/img/canvas_templates/back_in_stock_9.png %})

### Etapa 7: Testar e lançar seu Canvas {#step-7-test-and-launch-your-canvas}

Após testar e revisar nosso Canvas para garantir que funciona conforme esperado, vamos lançá-lo selecionando **Launch Canvas**. Agora, nossos usuários que favoritaram o jeans Classic Straight Leg e se inscreveram nos nossos canais de envio de mensagens receberão notificações quando estiverem de volta ao estoque!

{% alert tip %}
Confira nossa [Lista de verificação pré e pós-lançamento]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist#things-to-consider-before-launch) para itens a considerar antes e depois de lançar um Canvas.
{% endalert %}