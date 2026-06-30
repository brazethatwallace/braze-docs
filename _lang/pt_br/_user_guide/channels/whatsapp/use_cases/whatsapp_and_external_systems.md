---
nav_title: "WhatsApp e sistemas externos"
article_title: "WhatsApp e sistemas externos"
page_order: 2
description: "Este artigo de referência fornece um guia passo a passo para integrar a Braze e o WhatsApp com um sistema externo de IA ou comunicação."
page_type: reference
alias: /whatsapp_external_system_integration/
channel:
  - WhatsApp
---

# Integrar a Braze e o WhatsApp com um sistema externo de IA ou comunicação {#integrate-braze-and-whatsapp-with-an-external-ai-or-communication-system}

> Aproveite o poder dos chatbots de IA e das transferências para agentes ao vivo no canal WhatsApp para otimizar suas operações de suporte ao cliente. Ao automatizar consultas rotineiras e fazer a transição para agentes humanos quando necessário, você pode melhorar significativamente os tempos de resposta e aprimorar a experiência geral do cliente.

## Pré-requisitos {#prerequisites}

| Requisitos | Descrição |
| - | - |
| Sistema externo | Um sistema de IA ou comunicação de terceiros capaz de criar e gerenciar chatbots, sistemas automatizados de atendimento ao cliente usando APIs, ou ambos. |
| Integração da Braze com WhatsApp | Um número de WhatsApp gerenciado pela Braze |
| Chave da API REST da Braze | Uma chave da API REST com permissões de `campaigns.trigger.send`. Ela pode ser criada no dashboard da Braze acessando **Configurações** > **Chaves de API**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Como funciona {#how-it-works}

A integração entre a Braze e o sistema externo de IA ou comunicação funciona como uma via de mão dupla, onde a Braze é o canal de comunicação e o sistema externo é a "inteligência" que processa as mensagens e formula as respostas.

O fluxo de trabalho da integração pode ser dividido em dois fluxos principais:
**Fluxo de entrada:** A mensagem de um usuário chega na Braze e é encaminhada para o seu sistema externo para processamento.
**Fluxo de saída:** Após processar a mensagem, o seu sistema externo envia uma resposta para a Braze, que então entrega a mensagem ao usuário final.

Para automatizar essa comunicação de forma eficiente, essa integração utiliza dois recursos principais da Braze: [Campaigns de webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook) e [Campaigns disparadas por API]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery).

![Arquitetura da integração entre o canal WhatsApp da Braze e um sistema externo.]({% image_buster /assets/img/whatsapp/external_system_architecture.png %})
## Configurando a integração {#configuring-the-integration}

### Etapa 1: Criar uma Campaign de webhook para mensagens de entrada {#step-1-create-a-webhook-campaign-for-inbound-messages}

Primeiro, crie uma Campaign de webhook para estabelecer uma forma de enviar as mensagens de WhatsApp recebidas pela Braze para o seu sistema externo.

1. Na Braze, crie uma Campaign de webhook.
2. No criador de webhook, selecione **Compose webhook**.
3. No campo **Webhook URL**, insira o endpoint de API (URL) do sistema externo que receberá a mensagem.
4. Selecione **Raw text** para o corpo da requisição e insira uma carga útil com personalização que contenha o `external_id` e o número de telefone do usuário, o conteúdo da mensagem e outras informações relevantes, como:

{% raw %}
```liquid
{
  "user_id": "{{${user_id}}}",
  "phone_number": "{{${phone_number}}}",
  "message": "{{whats_app.${inbound_message_body}}}"
}
```
{% endraw %}

{: start="5"}
5. Na etapa **Schedule Delivery** do criador da Campaign, selecione **Action-Based** para o tipo de entrega e **Send a WhatsApp inbound message** para o gatilho da Campaign.

![Entrega baseada em ação com um gatilho de envio de mensagem de entrada do WhatsApp.]({% image_buster /assets/img/whatsapp/inbound_message_trigger.png %})

{: start="6"}
6. Finalize a composição da sua Campaign, depois salve e lance a Campaign. Após o lançamento, toda vez que uma mensagem for recebida, a Braze enviará um webhook para o seu sistema externo.

### Etapa 2: Criar uma Campaign disparada por API para mensagens de saída {#step-2}

Em seguida, crie uma Campaign disparada por API para estabelecer uma forma de o seu sistema externo enviar mensagens de volta aos usuários pelo WhatsApp.

1. Na Braze, crie uma Campaign de WhatsApp.
2. No criador de mensagens, selecione **WhatsApp Template Message** ou **Response Message** e, em seguida, selecione o modelo ou a disposição da mensagem de resposta. Você pode selecionar qualquer disposição de mensagem de resposta porque a mensagem de entrada abriu a janela de 24 horas do WhatsApp.

![Criador de mensagens com opções para selecionar o tipo de mensagem e a disposição da mensagem.]({% image_buster /assets/img/whatsapp/response_message_layout.png %})

{: start="3"}
3. Adicione a propriedade de gatilho de API ao corpo da mensagem, como {% raw %}`{{api_trigger_properties.${external_system_msg+body}}}`{% endraw %}. Isso permite que o seu sistema de IA preencha a mensagem que será enviada.

![Criador de mensagens com corpo da mensagem que contém propriedades de gatilho.]({% image_buster /assets/img/whatsapp/api_trigger_properties.png %})

{: start="4"}
4. Na etapa **Schedule Delivery** do criador da Campaign, selecione **Action-Based** para o tipo de entrega.
5. Salve a Campaign e anote o `campaign_id` único que a Braze gera para essa Campaign. Você precisará do ID para a próxima etapa.

### Etapa 3: Conectar o sistema externo à Campaign disparada por API {#step-3-connect-the-external-system-to-the-api-triggered-campaign}

Por último, configure o seu sistema externo para chamar a Braze e enviar a resposta.

1. No código do seu sistema externo, após processar a mensagem recebida e gerar a resposta, faça uma requisição POST para o endpoint `/messages/send` da Braze.
2. No corpo da requisição `/messages/send`, inclua o `campaign_id` da [Etapa 2](#step-2), o `external_id` do usuário e o conteúdo da resposta do sistema externo.
3. Use a propriedade de gatilho de API da [Etapa 2](#step-2) para inserir a resposta do sistema externo e não se esqueça de incluir sua chave de API no cabeçalho da requisição para autenticação, como neste exemplo de cURL:

{% raw %}
```bash
curl -X POST \
  -H 'Content-Type:application/json' \
  -H 'Authorization: Bearer a valid rest API key' \
  -d '{
    "campaign_id": "campaign_id",
    "recipients": [
      {
        "external_user_id": "external_id",
        "trigger_properties": {
          "external_system_msg_body": "your external system message"
        }
      }
    ]
  }' \
  {{Braze endpoint}}/campaigns/trigger/send
```
{% endraw %}

Agora você tem uma base sólida para construir um fluxo de trabalho de chatbot de IA!

### Personalizando seu fluxo de trabalho {#customizing-your-workflow}

Você pode expandir a lógica da sua integração para:
- Usar diferentes palavras-chave para disparar Campaigns de webhook distintas.
- Criar fluxos de conversa mais complexos com Campaigns disparadas por API em múltiplas etapas.
- Registrar informações do chat na Braze como atributos personalizados para enriquecer o perfil de usuário e segmentar Campaigns futuras.