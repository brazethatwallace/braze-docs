---
nav_title: Enviar mensagens
article_title: Envio de mensagens usando a REST or transferir estado representacional API or interface de programação do aplicativo (API)
page_order: 1
page_type: reference
description: "Este artigo de referência cobre as duas maneiras de enviar mensagens programaticamente usando a REST or transferir estado representacional API or interface de programação do aplicativo (API) da Braze."
---

# Envio de mensagens usando a REST or transferir estado representacional API or interface de programação do aplicativo (API) {#sending-messages-using-the-rest-api}

> Você pode enviar mensagens do seu backend em tempo real usando dois endpoints diferentes da Braze. Cada um tem uma forma de requisição diferente: um requer o conteúdo completo da mensagem na requisição; o outro requer um ID de campanha e envia o conteúdo definido no dashboard.

Essa abordagem funciona com qualquer canal de envio de mensagens suportado pela API or interface de programação do aplicativo (API) (WhatsApp, e-mail, SMS, push, Content Cards, webhooks e mais).

## Duas maneiras de enviar {#two-ways-to-send}

| | [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) | [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) |
| --- | --- | --- |
| **ID da Campaign** | Opcional. Omita para enviar sem rastreamento de campanha no dashboard, ou forneça um ID de campanha da API or interface de programação do aplicativo (API) mais `message_variation_id` em cada mensagem para rastrear no dashboard. | Obrigatório. |
| **Conteúdo da mensagem** | Você deve incluir um objeto `messages` na requisição (por exemplo, `messages.whats_app`, `messages.email`). | Não aceito. O conteúdo da mensagem é definido na campanha no dashboard da Braze. |
| **Caso de uso** | Envie uma mensagem com o conteúdo totalmente especificado na requisição da API or interface de programação do aplicativo (API). | Dispare uma campanha pré-construída (conteúdo no dashboard) para destinatários específicos via API or interface de programação do aplicativo (API). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Duas maneiras de enviar" }

Para detalhes completos de requisição e resposta, consulte as referências dos endpoints [Enviar mensagens imediatamente (somente API or interface de programação do aplicativo (API))]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) e [Enviar campanhas usando entrega disparada por API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns).

---

## Opção 1: Enviar com conteúdo da mensagem na requisição (`/messages/send`) {#option-1-send-with-message-content-in-the-request-messagessend}

Use este endpoint quando quiser especificar o conteúdo completo da mensagem na requisição da API or interface de programação do aplicativo (API). Você **deve** incluir um objeto `messages` (por exemplo, `messages.whats_app`, `messages.email` ou `messages.sms`). Você pode omitir `campaign_id` para enviar sem rastreamento de campanha, ou incluir um ID de campanha da API or interface de programação do aplicativo (API) e `message_variation_id` em cada mensagem para rastrear envios no dashboard (consulte a [referência do endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) para detalhes).

**Obrigatório:** chave de API or interface de programação do aplicativo (API) com a permissão `messages.send`.

{% alert important %}
Cada destinatário em `external_user_ids` já deve existir na Braze. Para criar usuários como parte de um envio, use [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) primeiro, ou use a [Opção 2](#option-2-trigger-a-campaign-with-content-in-the-dashboard-campaignstriggersend) (campanha disparada por API or interface de programação do aplicativo (API)).
{% endalert %}

### Exemplo: mensagem de modelo do WhatsApp {#example-whatsapp-template-message}

```
POST YOUR_REST_ENDPOINT/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "external_user_ids": ["user123"],
  "messages": {
    "whats_app": {
      "app_id": "YOUR_APP_ID",
      "subscription_group_id": "YOUR_WHATSAPP_SUBSCRIPTION_GROUP_ID",
      "message_type": "template_message",
      "message": {
        "template_name": "new_message_received",
        "template_language_code": "en_US"
      }
    }
  }
}
```

Para a especificação completa do objeto WhatsApp, consulte [Objeto WhatsApp]({{site.baseurl}}/api/objects_filters/messaging/whats_app_object).

{% alert note %}
O endpoint `/messages/send` suporta apenas modelos do WhatsApp com cabeçalhos de TEXTO ou IMAGEM. Para tipos de cabeçalho de DOCUMENTO, VÍDEO ou outros tipos de mídia, use o [endpoint de campanha disparada por API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) ou o dashboard da Braze.
{% endalert %}

### Exemplo: e-mail {#example-email}

```json
{
  "external_user_ids": ["user123"],
  "messages": {
    "email": {
      "app_id": "YOUR_APP_ID",
      "subject": "Your order has shipped",
      "from": "no-reply@example.com",
      "body": "<p>Your order #12345 is on its way.</p>"
    }
  }
}
```

Para outros canais, consulte [Objetos de envio de mensagens]({{site.baseurl}}/api/objects_filters#messaging-objects).

---

## Opção 2: Disparar uma campanha com conteúdo no dashboard (`/campaigns/trigger/send`) {#option-2-trigger-a-campaign-with-content-in-the-dashboard-campaignstriggersend}

Use este endpoint quando o conteúdo da mensagem for construído no dashboard da Braze (campanha disparada por API or interface de programação do aplicativo (API)). Você envia um `campaign_id` **obrigatório** e os destinatários; você **não** envia um objeto `messages`.

**Obrigatório:** chave de API or interface de programação do aplicativo (API) com a permissão `campaigns.trigger.send`.

### Etapa 1: Crie uma campanha disparada por API or interface de programação do aplicativo (API) {#step-1-create-an-api-triggered-campaign}

1. No dashboard da Braze, acesse **Envio de mensagens** > **Campaigns**.
2. Selecione **Create Campaign** e depois **API or interface de programação do aplicativo (API)-Triggered Campaign** (não "API or interface de programação do aplicativo (API) Campaign").
3. Adicione seu canal de mensagem (WhatsApp, e-mail, SMS, etc.) e construa o conteúdo da mensagem no dashboard.
4. Anote o **Campaign ID** (e o **Send ID**, se você usar várias variantes de mensagem). Você usará esses valores na requisição da API or interface de programação do aplicativo (API).

Para mais informações sobre como construir campanhas disparadas por API or interface de programação do aplicativo (API), consulte [Entrega disparada por API or interface de programação do aplicativo (API)]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery).

### Etapa 2: Dispare a campanha via API or interface de programação do aplicativo (API) {#step-2-trigger-the-campaign-via-the-api}

Envie uma requisição POST para `/campaigns/trigger/send` com `campaign_id` e `recipients` (ou `broadcast`/`audience`). Não inclua um objeto `messages` — o conteúdo vem da campanha.

```
POST YOUR_REST_ENDPOINT/campaigns/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "recipients": [
    {
      "external_user_id": "user123"
    }
  ]
}
```

Para o corpo completo da requisição (incluindo `trigger_properties`, `send_to_existing_only`, `attributes`, etc.), consulte a referência do endpoint [Enviar campanhas usando entrega disparada por API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns#request-body).

---

## Verifique sua integração {#verify-your-integration}

1. Envie uma requisição usando uma das opções disponíveis, com seu próprio ID de usuário como destinatário.
2. Confirme que a mensagem foi entregue.
3. Se estiver usando a Opção 2, verifique a campanha no dashboard da Braze para confirmar que o envio foi registrado.

## Considerações {#considerations}

- Use os recursos de [personalização]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) da Braze para adaptar o conteúdo quando suportado.
- Garanta que seu envio de mensagens esteja em conformidade com as regulamentações aplicáveis e inclua as opções de descadastramento e os avisos de privacidade exigidos.
- Para mais endpoints (agendamento, disparos de Canvas, etc.), consulte [Endpoints de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging).