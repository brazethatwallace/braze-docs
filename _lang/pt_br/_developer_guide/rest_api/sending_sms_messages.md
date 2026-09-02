---
nav_title: Enviar mensagens SMS
article_title: Envio de mensagens SMS usando a REST or transferir estado representacional API or interface de programação do aplicativo (API)
page_order: 2
page_type: reference
description: "Este artigo de referência explica como enviar mensagens SMS usando a REST or transferir estado representacional API or interface de programação do aplicativo (API) da Braze e uma Campanha da API or interface de programação do aplicativo (API)."
channel:
  - SMS
---

# Envio de mensagens SMS usando a REST or transferir estado representacional API or interface de programação do aplicativo (API) {#sending-sms-messages-using-the-rest-api}

> Use a REST or transferir estado representacional API or interface de programação do aplicativo (API) da Braze para enviar mensagens SMS transacionais do seu backend em tempo real. Essa abordagem permite que você construa um serviço que envia mensagens SMS programaticamente enquanto rastreia a análise de entrega junto com suas outras campanhas e Canvas no dashboard da Braze.

Isso pode ser especialmente útil para envio de mensagens transacionais de alto volume, onde o conteúdo é definido nos seus sistemas de backend. Por exemplo, você pode notificar os consumidores quando eles receberem uma mensagem de outro usuário, convidando-os a visitar seu site e verificar sua caixa de entrada.

Com essa abordagem, você pode:

- Disparar mensagens SMS do seu backend em tempo real.
- Rastrear análises junto com todas as suas Campaigns e Canvas de marketing.
- Ampliar o caso de uso com recursos adicionais da Braze, como postergação de mensagens, redirecionamento de acompanhamento e testes A/B.
- Opcionalmente, mudar para [entrega disparada por API or interface de programação do aplicativo (API)]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) para definir seus modelos de mensagem no dashboard da Braze enquanto ainda dispara envios do seu backend.

Para enviar uma mensagem SMS pela REST or transferir estado representacional API or interface de programação do aplicativo (API), você precisa configurar uma Campanha da API or interface de programação do aplicativo (API) no dashboard da Braze e então usar o endpoint [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) para enviar a mensagem.

## Pré-requisitos {#prerequisites}

Para completar este guia, você precisa de:

| Requisito | Descrição |
| --- | --- |
| Chave da REST or transferir estado representacional API or interface de programação do aplicativo (API) da Braze | Uma chave com a permissão `messages.send`. Para criar uma, acesse **Configurações** > **APIs e identificadores** > **Chaves de API or interface de programação do aplicativo (API)**. |
| Grupo de inscrições SMS | Um grupo de inscrições SMS configurado no seu espaço de trabalho da Braze. |
| Serviço de backend | Um serviço de backend ou ambiente de script capaz de fazer solicitações HTTP POST para a REST or transferir estado representacional API or interface de programação do aplicativo (API) da Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Etapa 1: Criar uma Campanha da API or interface de programação do aplicativo (API) {#step-1-create-an-api-campaign}

1. No dashboard da Braze, acesse **Messaging** > **Campaigns**.
2. Selecione **Create Campaign** e depois selecione **API or interface de programação do aplicativo (API) Campaigns**.
3. Digite um nome e uma descrição para sua campanha, como "notificação de mensagem SMS".
4. Adicione tags relevantes para identificação e rastreamento.
5. Selecione **Add canal de envio de mensagens** e depois selecione **SMS**.
6. Anote o **Campaign ID** e o **Message Variation ID** exibidos na página da campanha. Você precisará de ambos os valores ao construir sua solicitação de API or interface de programação do aplicativo (API).

## Etapa 2: Enviar uma mensagem SMS usando a API or interface de programação do aplicativo (API) {#step-2-send-an-sms-message-using-the-api}

Construa uma solicitação POST para o endpoint [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages). Inclua o ID da campanha, o ID de usuário externo do destinatário e o conteúdo do SMS na carga útil da solicitação.

{% alert important %}
Cada destinatário referenciado em `external_user_ids` já deve existir na Braze. Envios somente por API or interface de programação do aplicativo (API) não criam novos perfis de usuário. Se você precisar criar usuários como parte de um envio, use [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) primeiro, ou use uma [campanha disparada por API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) em vez disso.
{% endalert %}

### Exemplo de solicitação {#example-request}

```
POST YOUR_REST_ENDPOINT/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

Substitua `YOUR_REST_ENDPOINT` pela [URL do endpoint REST or transferir estado representacional]({{site.baseurl}}/api/basics#endpoints) do seu espaço de trabalho.

{% raw %}
```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "external_user_ids": ["user123"],
  "messages": {
    "sms": {
      "app_id": "YOUR_APP_ID",
      "subscription_group_id": "YOUR_SMS_SUBSCRIPTION_GROUP_ID",
      "message_variation_id": "YOUR_MESSAGE_VARIATION_ID",
      "body": "Hi {{${first_name}}}, you have a new message in your inbox. Check it out at https://yourwebsite.com/messages. Text STOP to opt out."
    }
  }
}
```
{% endraw %}

Substitua os valores de espaço reservado pelos seus IDs reais. O campo `body` suporta [personalização Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid), para que você possa adaptar o conteúdo da mensagem para cada destinatário. Para a lista completa de parâmetros suportados pelo objeto de envio de SMS, consulte [objeto SMS]({{site.baseurl}}/api/objects_filters/messaging/sms_object).

Após construir a solicitação, envie a solicitação POST do seu serviço de backend para a REST or transferir estado representacional API or interface de programação do aplicativo (API) da Braze.

## Etapa 3: Verificar sua integração {#step-3-verify-your-integration}

Após concluir a configuração, verifique sua integração:

1. Envie uma solicitação de API or interface de programação do aplicativo (API) conforme descrito na [Etapa 2](#step-2-send-an-sms-message-using-the-api), usando seu próprio ID de usuário como destinatário.
2. Confirme se a mensagem SMS foi entregue ao seu telefone.
3. No dashboard da Braze, acesse a página de resultados da campanha e confirme se o envio está registrado.
4. Monitore os resultados de perto à medida que você expande sua campanha.

## Considerações {#considerations}

- Confirme que suas campanhas de SMS estão em conformidade com as regulamentações relevantes e os requisitos da operadora. Inclua instruções de descadastramento (como "Envie STOP para cancelar") em cada mensagem. Para saber mais, consulte [Leis e regulamentações de SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations) e [Palavras-chave de opt-in e descadastramento]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout).
- Use os [recursos de personalização]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) da Braze para adaptar o conteúdo de SMS para consumidores individuais, incluindo conteúdo dinâmico e dados específicos do usuário.
- A REST or transferir estado representacional API or interface de programação do aplicativo (API) da Braze oferece [endpoints de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging) adicionais para agendar mensagens, disparar campanhas e mais.