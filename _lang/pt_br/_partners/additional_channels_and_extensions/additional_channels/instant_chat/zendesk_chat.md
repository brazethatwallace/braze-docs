---
nav_title: Zendesk
article_title: Zendesk Chat
description: "Saiba como integrar o Zendesk Chat à Braze e configurar uma conversa bidirecional por SMS."
alias: /partners/zendesk_chat/
page_type: partner
search_tag: Partner

---

# Zendesk Chat

> O [Zendesk Chat](https://www.zendesk.com/service/messaging/) usa webhooks de cada plataforma para configurar uma conversa bidirecional por SMS. Quando um usuário solicita suporte, um ticket é criado no Zendesk. As respostas dos agentes são encaminhadas à Braze por meio de uma Campaign de SMS disparada por API, e as respostas dos usuários são enviadas de volta ao Zendesk.

## Pré-requisitos {#prerequisites}


| Pré-requisito | Descrição |
|---|---|
| Uma conta do Zendesk | É necessário ter uma conta do Zendesk para aproveitar essa parceria.|
| Um token de autorização básica do Zendesk | Um token de autorização básica do Zendesk é usado para fazer uma solicitação de webhook de saída da Braze para o Zendesk.|
| Uma chave da API REST da Braze  | Uma chave da API REST da Braze com permissões `campaigns.trigger.send`. Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

Aumente a eficiência do suporte ao cliente combinando os recursos de SMS da Braze com as respostas dos agentes em tempo real do Zendesk para atender prontamente às consultas dos usuários com suporte humano.

## Integração do Zendesk Chat {#integrating-zendesk-chat}

### Etapa 1: Criar um webhook no Zendesk {#step-1-create-a-webhook-in-zendesk}

1. No console de desenvolvedor do Zendesk, acesse webhooks: {% raw %}`https://{{url}}.zendesk.com/admin/apps-integrations/webhooks/webhooks`{% endraw %}
2. Em **Create Webhook**, selecione **Trigger or automation**.
3. Para **Endpoint URL**, adicione o endpoint **/campaign/trigger/send**.
4. Em **Authentication**, selecione **Bearer token** e adicione a chave da API REST da Braze com as permissões `campaigns.trigger.send`.

![Um exemplo de webhook do Zendesk.]({% image_buster /assets/img/zendesk/instant_chat/chat1.png %}){: style="max-width:70%;"}

### Etapa 2: Criar uma Campaign de SMS de saída {#step-2-create-an-outbound-sms-campaign}

Em seguida, você criará uma Campaign de SMS que ouvirá webhooks do Zendesk e enviará uma resposta de SMS personalizada para seus clientes.

#### Etapa 2.1: Redija sua mensagem {#step-21-compose-your-message}

Quando o Zendesk envia o conteúdo de uma mensagem por meio da API, ele vem no seguinte formato:

```
**----------------------------------------------\n\n{Replier Name}, {Replier Date}\n\n{Message}**
```

Portanto, precisamos extrair os detalhes que desejamos dessa string para exibir na mensagem, caso contrário, o usuário verá todos os detalhes.

![Um exemplo de SMS sem formatação.]({% image_buster /assets/img/zendesk/instant_chat/chat2.png %}){: style="max-width:40%;"}

Na caixa de texto **Mensagem**, adicione o seguinte código Liquid e qualquer linguagem de descadastramento ou outro conteúdo estático:

{% raw %}
```liquid
{% assign body = {{api_trigger_properties.${msg_body}}} %}
{% assign msg = body | split: "
" %}
New message from Zendesk:
{{msg[2]}}

Feel free to respond directly to this number!
```
{% endraw %}

![Um exemplo de SMS com formatação.]({% image_buster /assets/img/zendesk/instant_chat/chat3.png %}){: style="max-width:70%;"}

#### Etapa 2.2: Agendar a entrega {#step-22-schedule-the-delivery}

Para o tipo de entrega, selecione **Entrega disparada por API** e, em seguida, copie o ID da Campaign, que será usado nas próximas etapas.

![Entrega disparada por API]({% image_buster /assets/img/zendesk/instant_chat/chat4.png %}){: style="max-width:70%;"}

Por fim, em **Controles de entrega**, ative a reelegibilidade.

![Reelegibilidade ativada em "Controles de entrega".]({% image_buster /assets/img/zendesk/instant_chat/chat5.png %})

### Etapa 3: Criar um gatilho no Zendesk para encaminhar as respostas do agente à Braze {#step-3-create-a-trigger-in-zendesk-to-forward-agent-replies-to-braze}

Acesse **Objects and rules** > **Business rules** > **Triggers**.

1. Crie uma nova **categoria** (por exemplo, **Trigger a message**).
2. Crie um novo **gatilho** (por exemplo, **Respond via SMS Braze**).
3. Em **Conditions**, selecione:
- **Ticket>Comment** está **Present and requester can see comment** para que a mensagem seja disparada sempre que um novo comentário público for incluído em uma atualização de ticket
- **Ticket>Update** *não é* **Web service (API)** para que, quando um usuário enviar uma mensagem pela Braze, ela não seja encaminhada de volta para o celular. Somente mensagens provenientes do Zendesk são encaminhadas.

![Respond via SMS Braze.]({% image_buster /assets/img/zendesk/instant_chat/chat6.png %}){: style="max-width:70%;"}

Em **Actions**, selecione **Notify by Webhook** e escolha o endpoint que você criou na etapa 1. Em seguida, especifique o corpo da chamada à API. Insira o `campaign_id` da [etapa 2.2](#step-22-schedule-the-delivery) no corpo da solicitação.

![Corpo JSON do Respond via SMS Braze.]({% image_buster /assets/img/zendesk/instant_chat/chat7.png %}){: style="max-width:70%;"}

{% raw %}
```liquid
{
    "campaign_id": "{{YOUR_CAMPAIGN_ID}}",
    "recipients": [
        {
            "external_user_id": "{{ticket.requester.custom_fields.braze_external_id}}",
			"trigger_properties": {
    "msg_body": "{{ticket.latest_public_comment_html}}"
		},
		"attributes": {
        "zendesk_ticket" : "{{ticket.id}}",
	"zendesk_ticket_open" : "true"
    }
        }
    ]
}
```
{% endraw %}


### Etapa 4: Criar um gatilho no Zendesk para atualizar um usuário quando um ticket for fechado {#step-4-create-a-trigger-in-zendesk-to-update-a-user-when-a-ticket-is-closed}

Se quiser notificar o usuário de que o ticket foi fechado, crie uma nova Campaign na Braze com o corpo de resposta modelado.

![Atualizar um usuário quando o ticket for fechado.]({% image_buster /assets/img/zendesk/instant_chat/chat8.png %}){: style="max-width:70%;"}

Selecione **Entrega disparada por API** e copie o ID da Campaign.

Em seguida, configure um gatilho para notificar a Braze quando o ticket for fechado:
- Categoria: **Trigger a message**
- Em Conditions, selecione **Ticket>Ticket Status** e altere para **Solved**

![Configuração de ticket resolvido no Zendesk.]({% image_buster /assets/img/zendesk/instant_chat/chat9.png %}){: style="max-width:70%;"}

Em **Actions**, selecione **Notify by Webhook** e escolha o segundo endpoint que você acabou de criar. A partir daí, precisamos especificar o corpo da chamada à API:

![Corpo JSON do ticket resolvido.]({% image_buster /assets/img/zendesk/instant_chat/chat10.png %}){: style="max-width:70%;"}

{% raw %}
```liquid
{
    "campaign_id": "{{YOUR_API_KEY}}",
    "recipients": [
        {
            "external_user_id": "{{ticket.requester.custom_fields.braze_external_id}}",
"trigger_properties": {
    "msg_body": "Your ticket has been closed"
		},
,
			"attributes": {
	"zendesk_ticket_open" : "false"
    }
        }
    ]
}
```
{% endraw %}

### Etapa 5: Adicionar um campo de usuário personalizado no Zendesk {#step-5-add-a-custom-user-field-in-zendesk}

Na Central de administração, selecione **People** na barra lateral e, em seguida, selecione **Configuration** > **User fields**. Adicione o campo de usuário personalizado `braze_external_id`.

### Etapa 6: Configurar o encaminhamento de SMS de entrada {#step-6-set-up-inbound-sms-forwarding}

Em seguida, você criará duas novas Campaigns de webhook na Braze para encaminhar SMS recebidos de clientes para a caixa de entrada do Zendesk.

| Campaign           | Finalidade                                                                              |
|--------------------|--------------------------------------------------------------------------------------|
| Campaign de webhook 1 | Cria um novo ticket no Zendesk.                                                     |
| Campaign de webhook 2 | Encaminha todas as respostas de SMS de conversação enviadas pelo cliente ao Zendesk. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 6: Configurar o encaminhamento de SMS de entrada" }

#### Etapa 6.1: Criar uma categoria de palavra-chave SMS {#step-61-create-an-sms-keyword-category}

No dashboard da Braze, acesse **Público**, escolha seu **grupo de inscrições de SMS** e selecione **Adicionar palavra-chave personalizada**. Preencha os campos a seguir para criar uma categoria de palavra-chave de SMS exclusiva para o Zendesk.

| Campo            | Descrição                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------|
| Categoria da palavra-chave | O nome da categoria da palavra-chave, como `ZendeskSMS1`.                                                                 |
| Palavras-chave         | Suas palavras-chave personalizadas, como `SUPPORT`.                                                                                  |
| Mensagem de resposta    | A mensagem enviada quando uma palavra-chave é detectada, como "Um representante de atendimento ao cliente entrará em contato com você em breve." |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 6.1: Criar uma categoria de palavra-chave SMS" }

![Um exemplo de categoria de palavra-chave SMS na Braze.]({% image_buster /assets/img/zendesk/instant_chat/chat11.png %}){: style="max-width:70%;"}

#### Etapa 6.2: Crie sua primeira Campaign de webhook {#step-62-create-your-first-webhook-campaign}

No dashboard da Braze, crie sua primeira Campaign de webhook. Essa mensagem sinalizará ao Zendesk que o suporte está sendo solicitado.

No criador do webhook, preencha os seguintes campos:
- URL do webhook: {% raw %}https://{{url}}.zendesk.com/api/v2/tickets{% endraw %}
- Método HTTP: POST
- Cabeçalhos de solicitação:
- Content-Type: application/json
- Authorization: Basic {{Token}}
- Corpo da solicitação:

{% raw %}
```liquid
{
  "ticket": {
    "subject": "Action Needed",
    "comment": {
      "body": "{{sms.${inbound_message_body}}}"
    },
"requester":{
"name": "{{${first_name}}} {{${last_name}}}",
"user_fields": {
"braze_external_id": "{{${user_id}}}"
}
},
    "priority": "normal",
    "type": "problem"
  }
}
```
{% endraw %}

![Um exemplo de solicitação com os dois cabeçalhos obrigatórios.]({% image_buster /assets/img/zendesk/instant_chat/chat12.png %}){: style="max-width:70%;"}


#### Etapa 6.3: Agendar a primeira entrega {#step-63-schedule-the-first-delivery}

Em **Programar entrega**, selecione **Entrega baseada em ação** e, em seguida, escolha **Enviar uma mensagem SMS de entrada** para o tipo de gatilho. Adicione também o grupo de inscrições de SMS e a categoria de palavras-chave que você configurou anteriormente.

![A página "Programar entrega" da primeira Campaign de webhook.]({% image_buster /assets/img/zendesk/instant_chat/chat13.png %})

Em **Controles de entrega**, ative a reelegibilidade.

![Reelegibilidade selecionada em "Controles de entrega" para a primeira Campaign de webhook.]({% image_buster /assets/img/zendesk/instant_chat/chat14.png %})

#### Etapa 6.4: Crie sua segunda Campaign de webhook {#step-64-create-your-second-webhook-campaign}

Configure uma Campaign de webhook para encaminhar as mensagens SMS restantes do usuário ao Zendesk:

Como o Zendesk envia o ID do ticket como uma string, crie um bloco de conteúdo para converter a string em um número inteiro para que você possa usá-lo no webhook do Zendesk.

{% raw %}
```liquid
{% assign var = {{custom_attribute.${zendesk_ticket}}} | to_i %}{{var}}
```
{% endraw %}

No criador do webhook:
- URL do webhook: {% raw %}https://{{url}}.zendesk.com/api/v2/tickets/{{content_blocks.${to_int}}}.json{% endraw %}
- Solicitação: PUT
- KVPs:
    - Content-Type:application/JSON
    - Authorization: Basic {{Token}}

Corpo de exemplo:

{% raw %}
```liquid
{
  "ticket": {
    "comment": {
      "body": "Inbound message from {{${first_name}}} {{${last_name}}}: {{sms.${inbound_message_body}}}"
    }
}
}
```
{% endraw %}

#### Etapa 6.5: Concluir a configuração da segunda Campaign de webhook {#step-65-complete-second-webhook-campaign-setup}
- Configure um gatilho baseado em ação para usuários que enviam uma mensagem de entrada na categoria "Other".
- Defina os critérios de reelegibilidade.
- Adicione públicos aplicáveis (neste caso, o atributo personalizado **zendesk_ticket_open** é **true**).

[2]: {% image_buster /assets/img/zendesk/instant_chat/chat2.png %}