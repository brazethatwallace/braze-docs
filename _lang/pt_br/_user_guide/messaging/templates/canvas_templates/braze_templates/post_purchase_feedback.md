---
nav_title: Feedback pós-compra
article_title: Feedback pós-compra
page_order: 6
page_type: reference
description: "Este artigo descreve como usar um modelo de Canvas da Braze para orquestrar experiências personalizadas que permitem responder a feedbacks e construir um relacionamento com seus usuários."
tool: Canvas
---

# Feedback pós-compra {#post-purchase-feedback}

> Use o modelo de feedback pós-compra para obter insights essenciais sobre como seus clientes interagem com sua marca e garantir que eles continuem tendo experiências positivas. Ao aproveitar a comunicação personalizada e um conjunto estruturado de mensagens, você pode continuar construindo e fortalecendo seus relacionamentos com os clientes.

Este artigo vai guiar você por um caso de uso do modelo **Post-Purchase Feedback**, que é projetado para a etapa de conversão do ciclo de vida do usuário. Ao final, você terá criado um Canvas que incentiva os usuários a fornecer feedback para o seu app.

## Pré-requisitos {#prerequisites}

Para usar este modelo com sucesso, você precisará do seguinte:

- Um [atributo personalizado]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#managing-custom-attributes) para referenciar os resultados da pesquisa de feedback.
- Uma [Sincronização de Público da Braze]({{site.baseurl}}/partners/canvas_audience_sync) configurada com os parceiros e públicos que você utiliza.

## Adaptando o modelo às suas necessidades {#tailoring-the-template-to-your-needs}

Digamos que trabalhamos para a Decorumsoft, uma desenvolvedora de jogos para dispositivos móveis. Vamos usar o modelo de feedback pós-compra para avaliar o feedback do nosso lançamento mais recente, Proxy War 3: War of Thirst. Com esse feedback, vamos orientar nossos planos de desenvolvimento para o pacote de expansão, Liquid Mirage.

Antes de criar o Canvas, configuramos a integração [Sincronização de Público da Braze com o Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync) para que possamos adicionar dados de usuários da Braze aos Públicos do Google e enviar anúncios com base em gatilhos comportamentais, segmentação e muito mais.

Para acessar o modelo de feedback pós-compra, ao criar um novo Canvas, selecione **Use a Canvas template** > **Braze templates**. Em seguida, ao lado de **Post-Purchase Feedback**, selecione **Apply Template**. Agora, podemos percorrer o modelo para adaptá-lo às nossas necessidades.

### Etapa 1: Configurar os detalhes do Canvas {#step-1-set-up-canvas-details}

Vamos ajustar os detalhes do Canvas para refletir nosso objetivo.

1. Selecione **Edit** ao lado do nome do modelo.

![O título e a descrição atuais do Canvas.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/select_edit_details.png %}){: style="max-width:50%;"}

{:start="2"}
2. Atualize o nome do Canvas para especificar que ele é direcionado a usuários recentes.
3. Atualize a descrição para especificar que o Canvas é para incentivar os usuários a enviar feedback.
4. Adicione a tag **Feedback** para filtrá-lo na página inicial do Canvas.

![O novo nome e a nova descrição do Canvas. A nova descrição diz: "Um Canvas de feedback pós-compra para avaliar o interesse na próxima expansão do PWD3, Liquid Mirage."]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/enter_new_canvas_name.png %}){: style="max-width:50%;"}

### Etapa 2: Atribuir eventos de conversão {#step-2-assign-conversion-events}

Em seguida, vamos atribuir nossos eventos de conversão. Atualize o **conversão primária Event - A** para **Make a specific purchase** e selecione **Proxy War**.

![Seção "Assign Conversion Events" para o tipo de evento de conversão de compra do produto do jogo Proxy War.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/select_conversion_event.png %}){: style="max-width:90%;"}

Vamos manter o prazo de conversão do modelo de três dias, pois queremos direcionar nossos usuários mais recentes.

### Etapa 3: Definir um cronograma de entrada {#step-3-set-an-entry-schedule}

1. Mantenha o tipo de cronograma de entrada como **Action-Based**.
2. Defina o **Start Time** da janela de entrada para a data de lançamento do jogo.

### Etapa 4: Determinar quem entra no Canvas {#step-4-determine-who-enters-the-canvas}

Nosso público-alvo para feedback são os usuários que compraram recentemente Proxy War 3.

1. Selecione nosso Segment alvo, "Purchased Proxy War 3", que consiste em usuários que compraram o jogo.
2. Selecione um filtro para incluir usuários que compraram "Proxy War 3" mais de "0" vezes.

![Um segmento chamado "Purchased Proxy War 3" que segmenta usuários que compraram o jogo.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/entry_window_segment.png %}){: style="max-width:90%;"}

{: start="3"}
3. Atualize os controles de entrada para não permitir que os usuários reentrem no Canvas após a duração máxima do Canvas.

### Etapa 5: Selecionar suas configurações de envio {#step-5-select-your-send-settings}

Vamos manter as configurações de inscrição padrão, para enviar apenas a usuários que se inscreveram ou optaram por receber mensagens ou notificações.

Como queremos ser cuidadosos com nossos envios, vamos selecionar **Enable horário de silêncio** para evitar solicitar feedback entre 23h e 10h no fuso horário dos nossos usuários e enviar apenas no próximo horário disponível.

![Etapa "Send Settings" direcionada a usuários inscritos ou que optaram por receber. O horário de silêncio está ativado.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/send_settings_with_quiet_hours.png %}){: style="max-width:90%;"}

Para o nosso exemplo, vamos pular as outras configurações (limite de frequência e grupos de teste).

### Etapa 6: Personalizar seu Canvas {#step-6-customize-your-canvas}

Em seguida, vamos construir nosso Canvas personalizando os canais de envio de mensagens e o conteúdo que será enviado aos usuários. Como estamos buscando feedback apenas por e-mail, mensagem no app e canais de webhook, vamos percorrer o modelo e remover as variantes de SMS das etapas de Mensagem.

Vamos começar nossa personalização percorrendo cada componente de mensagem para atualizar o conteúdo. Nosso atributo personalizado de referência é `Experience Feedback`.

1. No construtor de Canvas, selecione a primeira etapa de Mensagem na jornada do usuário.
2. Selecione a variante **Email**.
3. Preencha as **Sending info** com um assunto que incentive o feedback do usuário.
4. Selecione **Edit message** para substituir a mensagem de e-mail do modelo pela nossa mensagem de pesquisa de feedback. Isso inclui substituir os links de cada chamada para ação para capturar qual opção foi selecionada, que será referenciada na etapa Action jornada da nossa jornada do usuário.

{% alert tip %}
Você pode usar [propriedades de entrada do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) para personalizar as mensagens no seu Canvas com base no produto ao qual você está se referindo.
{% endalert %}

#### Configurar a pesquisa de feedback {#set-up-feedback-survey}

Em seguida, precisamos preencher os detalhes da variante **In-App Message**. É aqui que precisamos especificar nosso atributo personalizado `Experience Feedback` que indica o sentimento do feedback do usuário. (Também vamos referenciar isso na etapa Action jornada subsequente.)

1. Na mesma primeira etapa de Mensagem, selecione a variante **In-App Messages**. Vamos manter os controles de mensagem como estão.
2. Para o cabeçalho e o corpo, vamos usar uma linguagem que incentive os usuários a serem honestos sobre sua experiência com Proxy War 3.
3. Como queremos que as respostas da pesquisa sejam registradas nos perfis dos usuários, vamos manter a pesquisa como **Single-choice selection** e **Log attributes upon submission**.
4. Para cada uma das três opções da pesquisa, selecione **Experience Feedback** como nosso atributo personalizado.
5. Vamos manter os valores de atributo no perfil do usuário como estão, pois esses valores estão alinhados com nosso atributo personalizado.

![Uma pesquisa que pergunta ao usuário se ele gostou da compra recente de Proxy War 3, com três opções: "Loved it", "It was OK" e "Not for me".]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/survey_example_iam.png %}){: style="max-width:90%;"}

#### Construir o Action jornada {#build-out-the-action-path}

Usando nosso atributo personalizado `Experience Feedback` e os valores de atributo da seção anterior, vamos atualizar o Action jornada do modelo para corresponder ao nosso atributo e valores.

![O grupo "Good feedback" para a etapa Action Path que inclui usuários que responderam "Loved it" à nossa pesquisa.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/action_path_good_example.png %}){: style="max-width:90%;"}

### Configurar o redirecionamento de anúncios {#set-up-ad-retargeting}

Vamos garantir que nossa sincronização de Google Audience esteja configurada na etapa **Ad Retargeting**. Isso incluirá selecionar nossa conta de anúncios, um público existente e a opção de adicionar usuários ao público.

### Configurar casos de suporte via webhook {#set-up-webhook-support-cases}

Em seguida, vamos configurar o webhook para acionar possíveis casos de suporte. Isso pode ser especialmente valioso em combinação com a análise do feedback dos nossos usuários.

Para a etapa de Mensagem chamada **Support Case Creation**, vamos atualizar o modelo para compor um webhook para usuários insatisfeitos com a compra que desejam um reembolso.

![Um webhook que cria casos de suporte para clientes com sentimento negativo que desejam um reembolso pela compra de Proxy War 3.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/webhook_example.png %}){: style="max-width:90%;"}

### Etapa 6: Testar e lançar o Canvas {#step-6-test-and-launch-the-canvas}

Após testar e revisar nosso Canvas para garantir que funciona conforme esperado, selecione **Launch Canvas** para lançar o Canvas. Agora, podemos direcionar os usuários de forma cuidadosa com uma jornada personalizada para incentivá-los a responder à nossa pesquisa de feedback com base na compra recente de Proxy War 3!

{% alert tip %}
Confira nossa [Lista de verificação pré e pós-lançamento]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist#things-to-consider-before-launch) para saber o que considerar antes e depois de lançar um Canvas.
{% endalert %}