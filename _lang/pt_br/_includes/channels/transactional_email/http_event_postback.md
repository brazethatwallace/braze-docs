Todos os e-mails de transação são complementados com postbacks de status de evento enviados como uma solicitação HTTP de volta à URL especificada. Isso permite analisar o status da mensagem em tempo real e tomar providências para alcançar o usuário por outro canal se a mensagem não for entregue, ou fazer fallback para um sistema interno caso a Braze esteja enfrentando latência.

Você pode associar essas atualizações a mensagens individuais usando identificadores exclusivos:

- `dispatch_id`: um ID exclusivo que a Braze gera automaticamente para cada mensagem.
- `external_send_id`: um identificador personalizado que você fornece, como um número de pedido, para combinar atualizações com seus sistemas internos.

Por exemplo, se você incluir `external_send_id: 1234` na solicitação ao enviar um e-mail de confirmação de pedido, todos os postbacks de eventos subsequentes para esse e-mail — como `Sent` ou `Delivered` — incluirão `external_send_id: 1234`. Isso permite que você confirme se o cliente do pedido #1234 recebeu o e-mail de confirmação de pedido.

### Configurando postbacks {#setting-up-postbacks}

No dashboard da Braze:

1. Acesse **Configurações** > **Preferências de e-mail**.
2. Em **Transactional Event Status Postback**, insira a URL onde a Braze deve enviar atualizações de status para seus e-mails de transação.
3. Teste o postback.

![Campo de URL do Transactional Event Status Postback em Preferências de e-mail.]({% image_buster /assets/img/transactional_webhook_url.png %})

### Corpo do postback {#postback-body}

```json
{
  "dispatch_id": (string, a randomly-generated unique ID of the instance of this send),
  "status": (string, Current status of message from the following message status table,
  "metadata" : (object, additional information relating to the execution of an event)
   {
     "external_send_id" : (string, If provided at the time of the request, Braze will pass your internal identifier for this send for all postbacks),
     "campaign_api_id" : (string, API identifier of this transactional campaign),
     "received_at": (ISO 8601 DateTime string, Timestamp of when the request was received by Braze, only included for events with "sent" status),
     "enqueued_at": (ISO 8601 DateTime string, Timestamp of when the request was enqueued by Braze, only included for events with "sent" status),
     "executed_at": (ISO 8601 DateTime string, Timestamp of when the request was processed by Braze, only included for events with "sent" status),
     "sent_at": (ISO 8601 DateTime string, Timestamp of when the request was sent to the ESP by Braze, only included for events with "sent" status),
     "processed_at" : (ISO 8601 DateTime string, Timestamp the event was processed by the ESP, only included for events with "processed" status),
     "delivered_at" : (ISO 8601 DateTime string, Timestamp the event was delivered to the user's inbox provider, only included for events with "processed" status),
     "bounced_at" : (ISO 8601 DateTime string, Timestamp the event was bounced by the user's inbox provider, only included for events with "bounced" status),
     "aborted_at" : (ISO 8601 DateTime string, Timestamp the event was Aborted by Braze, only included for events with "aborted" status),
     "reason" : (string, The reason Braze or the Inbox provider was unable to process this message to the user, only included for events with "aborted" or "bounced" status),
   }
}
```

#### Status da mensagem {#message-status}

| Status | Descrição |
| ------------ | ----------- |
| `sent` | Mensagem enviada com sucesso para um parceiro de envio de e-mail da Braze |
| `processed` | O parceiro de envio de e-mail recebeu e preparou com êxito a mensagem para envio ao provedor da caixa de entrada do usuário |
| `aborted` | A Braze não conseguiu enviar a mensagem com êxito porque o usuário não tinha um endereço de e-mail válido ou a lógica de abortamento do Liquid foi chamada no corpo da mensagem. Todos os eventos abortados incluem um campo `reason` no objeto de metadados, indicando por que a mensagem foi abortada |
| `delivered` | A mensagem foi aceita pelo provedor da caixa de entrada de e-mail do usuário |
| `bounced` | A mensagem foi rejeitada pelo provedor da caixa de entrada de e-mail do usuário. Todos os eventos de bounce incluem um campo `reason` no objeto de metadados que reflete o código de erro de bounce fornecido pelo provedor da caixa de entrada |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Status da mensagem" }

### Exemplo de postback {#example-postback}
```json

// Sent Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "sent",
    "metadata": {
      "received_at": "2020-08-31T18:58:41.000+00:00",
      "enqueued_at": "2020-08-31T18:58:41.000+00:00",
      "executed_at": "2020-08-31T18:58:41.000+00:00",
      "sent_at": "2020-08-31T18:58:42.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Processed Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "processed",
    "metadata": {
      "processed_at": "2020-08-31T18:58:42.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Aborted
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "aborted",
    "metadata": {
      "reason": "User not emailable",
      "aborted_at": "2020-08-31T19:04:51.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Delivered Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "delivered",
    "metadata": {
      "delivered_at": "2020-08-31T18:27:32.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Bounced Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "bounced",
    "metadata": {
      "bounced_at": "2020-08-31T18:58:43.000+00:00",
      "reason": "550 5.1.1 The email account that you tried to reach does not exist",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

```

