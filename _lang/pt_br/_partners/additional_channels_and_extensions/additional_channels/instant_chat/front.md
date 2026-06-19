---
nav_title: Front
article_title: Front
description: "Saiba como integrar o Front com a Braze"
alias: /partners/front/
page_type: partner
search_tag: Partner

---

# Front

> A integração do Front permite que você aproveite a Transformação de dados da Braze e os webhooks de cada plataforma para configurar um pipeline de SMS conversacional bidirecional.

O webhook de entrada do Front conterá uma carga útil que inclui a mensagem enviada pelo agente ao vivo. A solicitação precisará ser reformatada antes de ser aceita pelos endpoints da Braze. O modelo de Transformação de dados do Front reformatará a carga útil e gravará um evento personalizado no perfil do usuário intitulado **Outbound SMS Sent**, com o corpo da mensagem sendo passado como uma propriedade do evento.

Antes de configurar uma nova transformação na Braze, recomendamos revisar a matriz de suporte para cada nível em nossa documentação de [Transformação de dados]({{site.baseurl}}/user_guide/data/unification/data_transformation/). Nossos níveis Free e Pro oferecem um número diferente de transformações ativas e solicitações de entrada por mês. Confirme se o plano atual em que você está pode suportar seu caso de uso.

## Pré-requisitos {#prerequisites}

Antes de começar, você precisará do seguinte:

| Pré-requisito | Descrição |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Uma conta Front | É necessário ter uma conta Front para aproveitar essa parceria. |
| URL do webhook de Transformação de dados da Braze | A [Transformação de dados da Braze]({{site.baseurl}}/user_guide/data/unification/data_transformation/) será usada para reformatar o webhook de entrada do Front para que ele possa ser aceito pelo endpoint /users/track da Braze. |
| Uma chave da API REST do Front | Uma chave da API REST do Front será usada para fazer uma solicitação de webhook de saída da Braze para o Front. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

- Simplifique seu processo de geração de leads usando o envio automatizado de mensagens SMS da Braze para identificar as preferências do usuário e permitir que agentes de vendas ao vivo façam o acompanhamento e fechem as vendas.
- Reengaje os clientes que abandonaram seus carrinhos de compras, impulsionando as conversões de vendas por meio de respostas automatizadas por SMS e suporte por chat ao vivo.

## Integração do Front {#integrating-front}

### Etapa 1: Criar uma transformação de dados {#step-1-create-a-data-transformation}

Primeiro, você criará uma nova transformação de dados na Braze. As etapas a seguir são simplificadas; para um passo a passo completo, consulte [Criando uma transformação]({{site.baseurl}}/user_guide/data/unification/data_transformation/creating_a_transformation/).

1. Na Braze, acesse **Configurações de dados** > **Transformações de dados** e selecione **Criar transformação**.
2. Em **Editing Experience**, selecione **Start from scratch**.
3. Em **Select Destination**, selecione **POST: Track Users**.
4. Copie e cole o seguinte modelo de transformação e depois salve e ative o endpoint.
    {% raw %}
    ```liquid

    // This is a default template that you can use as a starting point. Feel free to delete this entirely to start from
    // scratch, or to delete specific components as you see fit

    // First, this code defines a variable, "brazecall", to build up a /users/track request
    // Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in
    // desired values in your /users/track request with JS dot notation, such as payload.x.y.z

    let brazecall = {
    "events": [
      {
      "phone": payload.recipients[1].handle,
      "_update_existing_only": true,
      "name": "Outbound SMS Sent",
      "time": new Date().toISOString(),
      "properties": {
        "message_id": payload.id,
        "message_body": payload.body,
        "front_author_username": payload.author.username
      }
      }
    ]
    };

    // After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
    return brazecall;
    ```
    {% endraw %}

    Sua transformação deve espelhar o exemplo JavaScript acima, ajustando nomes de propriedades e caminhos para corresponder à carga útil do webhook do Front.

{% alert tip %}
Você pode modificar esse modelo para atender às suas necessidades específicas. Por exemplo, você pode personalizar o nome do evento personalizado predefinido. Para saber mais, consulte [Visão geral da Transformação de dados]({{site.baseurl}}/user_guide/data/unification/data_transformation/).
{% endalert %}

### Etapa 2: Criar uma campanha de SMS de saída {#step-2-create-an-outbound-sms-campaign}

Em seguida, você criará uma campanha de SMS que ouvirá webhooks do Front e enviará uma resposta de SMS personalizada para seus clientes.

#### Etapa 2.1: Redija sua mensagem {#step-21-compose-your-message}

Na caixa de texto **Mensagem**, adicione o seguinte código Liquid, juntamente com qualquer linguagem de descadastramento ou outro conteúdo estático.

{% raw %}
```liquid
{{event_properties.${message_body}}}
```
{% endraw %}

Sua mensagem deve ser semelhante à seguinte:

![Um exemplo de mensagem usando código Liquid.]({% image_buster /assets/img/front/sms_to_braze.png %}){: style="max-width:80%;"}

#### 2.2 Programar a entrega {#22-schedule-the-delivery}

Para o tipo de entrega, selecione **Entrega baseada em ação**; em seguida, para o gatilho de evento personalizado, selecione **Outbound SMS Sent**.

![A página "Programar entrega".]({% image_buster /assets/img/front/custom_event_trigger.png %})

{% alert note %}
Esse evento personalizado é a Transformação de dados que grava no perfil do usuário. As mensagens do agente serão salvas como uma propriedade de evento nesse evento.
{% endalert %}

Por fim, em **Controles de entrega**, ative a reelegibilidade.

![Reelegibilidade ativada em "Controles de entrega".]({% image_buster /assets/img/front/braze_reeligibility.png %})

### Etapa 3: Criar um canal personalizado {#step-3-create-a-custom-channel}

No dashboard do Front, acesse **Settings** > **Channels** > **Add Channels**, selecione **Custom Channel** e insira um nome para seu novo canal da Braze.

![Um canal personalizado para a Braze no dashboard do Front.]({% image_buster /assets/img/front/front_custom_channel.png %})

### Etapa 4: Configurar as definições {#step-4-configure-the-settings}

No campo de endpoint da API de saída, insira a URL do webhook de Transformação de dados [que você criou anteriormente](#step-1-set-up-a-data-transformation-in-braze). Todas as mensagens de saída de agentes ao vivo no seu novo canal da Braze serão enviadas para cá. Esse canal também fornece uma URL de endpoint para a Braze encaminhar mensagens SMS no campo **Incoming URL**.

Não se esqueça de anotar essa URL&#8212;você precisará dela mais tarde.

![As configurações de canal para o canal da Braze recém-criado no Front.]({% image_buster /assets/img/front/front_custom_channel2.png %}){: style="max-width:65%;"}

### Etapa 5: Configurar o encaminhamento de SMS de entrada {#step-5-set-up-inbound-sms-forwarding}

Em seguida, você criará duas novas campanhas de webhook na Braze para encaminhar SMS recebidos de clientes para a caixa de entrada do Front.

| Número | Finalidade |
|---|---|
| Campanha de webhook 1 | Sinaliza ao Front que uma conversa de chat ao vivo está sendo solicitada. |
| Campanha de webhook 2 | Encaminha todas as respostas de SMS conversacionais enviadas pelo cliente para a caixa de entrada do Front. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 5: Configurar o encaminhamento de SMS de entrada" }

#### Etapa 5.1: Criar uma categoria de palavra-chave SMS {#step-51-create-an-sms-keyword-category}

No dashboard da Braze, acesse **Público**, escolha seu **grupo de inscrições de SMS** e selecione **Adicionar palavra-chave personalizada**. Para criar uma categoria de palavra-chave de SMS exclusiva para o Front, preencha os campos a seguir.

| Campo | Descrição |
|---|---|
| Categoria da palavra-chave | O nome da categoria da palavra-chave, como `FrontSMS1`. |
| Palavras-chave | Suas palavras-chave personalizadas, como `TIMETOMOW`. Evite palavras comuns para evitar disparos acidentais. Lembre-se de que as palavras-chave não diferenciam maiúsculas de minúsculas, portanto `lawn` corresponderia a `LAWN`. |
| Mensagem de resposta | A mensagem que será enviada quando uma palavra-chave for detectada, como "Um paisagista entrará em contato com você em breve." |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 5.1: Criar uma categoria de palavra-chave SMS" }

![Um exemplo de categoria de palavra-chave SMS na Braze.]({% image_buster /assets/img/front/front_keyword.png %}){: style="max-width:65%;"}

#### Etapa 5.2: Crie sua primeira campanha de webhook {#step-52-create-your-first-webhook-campaign}

No dashboard da Braze, crie sua primeira campanha de webhook usando a URL [que você criou anteriormente](#step-3-configure-the-settings-for-your-new-custom-braze-channel).

![Um exemplo da primeira campanha de webhook que deve ser criada na Braze.]({% image_buster /assets/img/front/sms_to_front.png %}){: style="max-width:65%;"}

Adicione o seguinte ao corpo da solicitação:

{% raw %}
```liquid
{
 "sender": {
  "handle": "{{${phone_number}}}",
  "name": "{{${user_id}}}"
 },
 "body_format": "markdown",
 "metadata": {
  "headers": {
   "first_name": "{{${first_name}}}",
   "last_name": "{{${last_name}}}"
  }
 },
 "body": "{{sms.${inbound_message_body} | default : "no body available" }}"
}
```
{% endraw %}

Na guia Configurações, configure os cabeçalhos de solicitação `Authorization`, `content-type` e `accept`.

![Um exemplo de solicitação com os três cabeçalhos necessários.]({% image_buster /assets/img/front/webhook_settings.png %}){: style="max-width:65%;"}

#### Etapa 5.3: Agendar a primeira entrega {#step-53-schedule-the-first-delivery}

Em **Programar entrega**, selecione **Entrega baseada em ação** e, em seguida, escolha **Enviar uma mensagem de entrada SMS** para o tipo de gatilho. Adicione também o grupo de inscrições de SMS e a categoria de palavras-chave que você [configurou anteriormente](#step-51-create-an-sms-keyword-category).

![A página "Programar entrega" da primeira campanha de webhook.]({% image_buster /assets/img/front/front_actionbased_keyword.png %})

Em **Controles de entrega**, ative a reelegibilidade.

![Reelegibilidade selecionada em "Controles de entrega" para a primeira campanha de webhook.]({% image_buster /assets/img/front/braze_reeligibility.png %})

#### Etapa 5.4: Crie sua segunda campanha de webhook {#step-54-create-your-second-webhook-campaign}

Como sua segunda campanha de webhook é igual à primeira, você pode [duplicar a primeira e renomeá-la]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns/#duplicating-segments-or-campaigns).

#### Etapa 5.5: Agendar a segunda entrega {#step-55-schedule-the-second-delivery}

Em **Programar entrega**, defina o **gatilho baseado em ação** e o **grupo de inscrições de SMS** com os mesmos valores da [primeira entrega](#step-53-schedule-the-first-delivery). Porém, para a **categoria de palavra-chave**, escolha **Other**.

![A página "Programar entrega" da segunda campanha de webhook, com "Other" escolhido como a categoria de palavra-chave.]({% image_buster /assets/img/front/front_actionbased_other_keyword.png %})

#### Etapa 5.6: Adicionar um filtro de público {#step-56-add-an-audience-filter}

Sua campanha de webhook agora pode encaminhar respostas de SMS recebidas de seus clientes. Para filtrar as respostas de SMS de modo que somente as mensagens de chats ao vivo sejam encaminhadas, adicione o filtro de segmentação **Last Received Message From Specific Campaign** à **etapa de públicos-alvo**.

![Um filtro de público com a opção "Last Received Message From Specific Campaign" selecionada.]({% image_buster /assets/img/front/front_segment_last_received_message.png %}){: style="max-width:65%;"}

Em seguida, configure seu filtro:

1. Em **Campaign**, selecione a campanha de SMS [que você criou anteriormente](#step-2-create-an-outbound-sms-campaign).
2. Em **Operator**, selecione **Less Than**.
3. Em **Time Window**, escolha o período de tempo em que o chat deve permanecer aberto sem uma resposta do cliente.

![As definições de configuração do filtro de público selecionado.]({% image_buster /assets/img/front/front_target_audience.png %})

## Considerações {#considerations}

### Segmentos faturáveis {#billable-segments}

- As mensagens SMS na Braze são cobradas por segmento de mensagem. Entender o que define um segmento e como essas mensagens serão divididas é fundamental para entender como você será cobrado pelas mensagens. Para saber mais, consulte nossa [documentação]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator/).
- Respostas longas dos agentes consumirão mais segmentos faturáveis.

### Registro de pontos de dados {#logging-data-points}

No momento, essa integração exige que um evento personalizado seja gravado em um perfil de usuário toda vez que um agente ao vivo envia um SMS pelo Front. Isso pode ser adequado para trocas rápidas que duram apenas algumas mensagens, mas à medida que as conversas se tornam mais longas, as implicações nos pontos de dados também aumentam. Se você tiver dúvidas sobre as nuances dos pontos de dados da Braze, seu gerente de conta da Braze poderá respondê-las.

### Inclusão de links em mensagens SMS {#including-links-in-sms-messages}

O envio de um link pelo chat ao vivo do Front será renderizado com tags HTML extras.

### Anexar arquivo de imagem pelo Front {#attaching-image-file-from-front}

Os arquivos de imagem no Front não serão renderizados em mensagens SMS enviadas pela Braze.

### Descadastramento {#opt-outs}

As mensagens conversacionais têm um risco maior de conter a palavra "pare" ou termos semelhantes que podem ser reconhecidos como descadastramentos imprecisos.