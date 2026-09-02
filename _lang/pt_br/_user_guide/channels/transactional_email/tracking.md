---
nav_title: "Configurar rastreamento"
article_title: "Rastreamento"
page_order: 2
description: "Este artigo de referência aborda como configurar o rastreamento em tempo real para campanhas de e-mail de transação."
page_type: reference
tool:
  - Campaigns
channel: email

---

# Rastrear e-mails de transação {#track-transactional-emails}

> Esta página descreve como configurar o rastreamento em tempo real para [campanhas de e-mail de transação]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email). Para saber mais sobre o endpoint em si, consulte [Enviar e-mails de transação usando entrega disparada por API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message).

Quando você envia e-mails de transação — como confirmações de pedido ou redefinições de senha — é essencial saber se eles chegam aos seus clientes. Com os postbacks de eventos HTTP transacionais da Braze, você obtém insights em tempo real sobre o status de cada e-mail de transação, para que possa agir rapidamente se houver algum problema.

Use esse recurso para:

- **Monitorar seus e-mails em tempo real:** veja imediatamente se as mensagens foram enviadas, processadas, entregues ou se encontraram problemas.
- **Responder proativamente:** reenvie mensagens, mude para outro canal como SMS ou use sistemas de fallback para garantir que suas comunicações sejam entregues.

## Rastreamento dos seus e-mails de transação {#tracking-your-transactional-emails}

{% multi_lang_include channels/transactional_email/http_event_postback.md %}