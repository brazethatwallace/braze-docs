---
nav_title: Changelog do Currents
article_title: Changelog do Currents
page_order: 3
description: "Esta página inclui as mudanças de eventos para cada lançamento do Currents."
tool: Currents
---

# Changelog do Currents

> Esta página lista as mudanças de eventos e esquemas para cada lançamento da Braze Currents.

## Mudanças na Versão 8 (data de lançamento 2026-05-06)

### Mudanças para armazenamento:

* Adicionado novo tipo de evento `users.messages.banner.Dismiss`.

* Mudanças de campo para o tipo de evento `users.messages.whatsapp.Abort`:
    * Adicionado novo campo `string` `bsuid`: O ID de usuário com escopo de negócio do WhatsApp Business do destinatário associado a este evento.

* Mudanças de campo para o tipo de evento `users.messages.whatsapp.Delivery`:
    * Adicionado novo campo `string` `bsuid`: O ID de usuário com escopo de negócio do WhatsApp Business do destinatário associado a este evento.

* Mudanças de campo para o tipo de evento `users.messages.whatsapp.Failure`:
    * Adicionado novo campo `string` `bsuid`: O ID de usuário com escopo de negócio do WhatsApp Business do destinatário associado a este evento.

* Mudanças de campo para o tipo de evento `users.messages.whatsapp.InboundReceive`:
    * Adicionado novo campo `string` `bsuid`: O ID de usuário com escopo de negócio do WhatsApp Business do usuário do qual a mensagem foi recebida.
    * O campo `user_phone_number` agora é *opcional*.

* Mudanças de campo para o tipo de evento `users.messages.whatsapp.Read`:
    * Adicionado novo campo `string` `bsuid`: O ID de usuário com escopo de negócio do WhatsApp Business do destinatário associado a este evento.

* Mudanças de campo para o tipo de evento `users.messages.whatsapp.Retry`:
    * Adicionado novo campo `string` `bsuid`: O ID de usuário com escopo de negócio do WhatsApp Business do destinatário associado a este evento.

* Mudanças de campo para o tipo de evento `users.messages.whatsapp.Send`:
    * Adicionado novo campo `string` `bsuid`: O ID de usuário com escopo de negócio do WhatsApp Business do destinatário associado a este evento.

## Mudanças na Versão 7 (data de lançamento 2026-04-01)

### Mudanças para armazenamento:

* Mudanças de campo para o tipo de evento `users.messages.banner.Abort`:
    * Adicionado novo campo `string` `canvas_name`: Nome do Canvas
    * Adicionado novo campo `string` `canvas_step_name`: Nome da etapa do Canvas
    * Adicionado novo campo `string` `canvas_variation_name`: Nome da variação do Canvas que este usuário recebeu
    * Adicionado novo campo `string` `canvas_id`: ID da API do Canvas ao qual este evento pertence
    * Adicionado novo campo `string` `canvas_step_id`: ID da API da etapa do Canvas à qual este evento pertence
    * Adicionado novo campo `string` `canvas_step_message_variation_id`: ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
    * Adicionado novo campo `string` `canvas_variation_id`: ID da API da variação do Canvas à qual este evento pertence

* Mudanças de campo para o tipo de evento `users.messages.banner.Click`:
    * Adicionado novo campo `string` `canvas_id`: ID da API do Canvas ao qual este evento pertence
    * Adicionado novo campo `string` `canvas_step_id`: ID da API da etapa do Canvas à qual este evento pertence
    * Adicionado novo campo `string` `canvas_name`: Nome do Canvas
    * Adicionado novo campo `string` `canvas_step_name`: Nome da etapa do Canvas
    * Adicionado novo campo `string` `canvas_step_message_variation_id`: ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
    * Adicionado novo campo `string` `canvas_variation_id`: ID da API da variação do Canvas à qual este evento pertence
    * Adicionado novo campo `string` `canvas_variation_name`: Nome da variação do Canvas que este usuário recebeu

* Mudanças de campo para o tipo de evento `users.messages.banner.Impression`:
    * Adicionado novo campo `string` `canvas_id`: ID da API do Canvas ao qual este evento pertence
    * Adicionado novo campo `string` `canvas_step_id`: ID da API da etapa do Canvas à qual este evento pertence
    * Adicionado novo campo `string` `canvas_name`: Nome do Canvas
    * Adicionado novo campo `string` `canvas_step_name`: Nome da etapa do Canvas
    * Adicionado novo campo `string` `canvas_step_message_variation_id`: ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu
    * Adicionado novo campo `string` `canvas_variation_id`: ID da API da variação do Canvas à qual este evento pertence
    * Adicionado novo campo `string` `canvas_variation_name`: Nome da variação do Canvas que este usuário recebeu

## Mudanças na Versão 6 (data de lançamento 2026-03-04)

### Mudanças para armazenamento:

* Mudanças de campo para o tipo de evento `agentconsole.AgentExecuted`:
    * Adicionado novo campo `string` `error`: Descrição do erro

* Mudanças de campo para o tipo de evento `agentconsole.ToolInvocation`:
    * Adicionado novo campo `string` `request_id`: ID único para esta solicitação geral de LLM e execução completa

* Mudanças de campo para o tipo de evento `users.messages.rcs.InboundReceive`:
    * Adicionado novo campo `string` `canvas_variation_name`: Nome da variação do Canvas que este usuário recebeu

## Mudanças na Versão 5 (data de lançamento 2026-02-04)

### Mudanças para armazenamento:

* Adicionado novo tipo de evento `agentconsole.AgentExecuted`.

* Adicionado novo tipo de evento `agentconsole.ToolInvocation`.

* Adicionado novo tipo de evento `users.messages.email.Retry`.

* Adicionado novo tipo de evento `users.messages.line.Retry`.

* Adicionado novo tipo de evento `users.messages.pushnotification.Retry`.

* Adicionado novo tipo de evento `users.messages.sms.Retry`.

* Adicionado novo tipo de evento `users.messages.webhook.Retry`.

* Adicionado novo tipo de evento `users.messages.whatsapp.Retry`.

* Mudanças de campo para o tipo de evento `users.behaviors.pushnotification.TokenStateChange`:
    * Adicionado novo campo `long` `time_ms`: Tempo em milissegundos de quando o evento aconteceu

## Mudanças na Versão 4 (data de lançamento 2026-01-07)

### Mudanças para armazenamento:

* Mudanças de campo para o tipo de evento `users.behaviors.pushnotification.TokenStateChange`:
    * Adicionado novo campo `string` `push_token`: Token por push do evento

* Mudanças de campo para o tipo de evento `users.messages.pushnotification.Bounce`:
    * Adicionado novo campo `string` `push_token`: Token por push do evento

* Mudanças de campo para o tipo de evento `users.messages.pushnotification.Send`:
    * Adicionado novo campo `string` `push_token`: Token por push do evento

* Mudanças de campo para o tipo de evento `users.messages.rcs.Click`:
    * Adicionado novo campo `string` `canvas_variation_name`: Nome da variação do Canvas que este usuário recebeu
    * O campo `user_phone_number` agora é *opcional*.

* Mudanças de campo para o tipo de evento `users.messages.rcs.InboundReceive`:
    * O campo `user_id` agora é *opcional*.

* Mudanças de campo para o tipo de evento `users.messages.rcs.Rejection`:
    * Adicionado novo campo `string` `canvas_step_message_variation_id`: ID da API da variação de mensagem da etapa do Canvas que este usuário recebeu

## Mudanças na Versão 3 (data de lançamento 2025-10-08)

### Mudanças para armazenamento:

* Adicionado novo tipo de evento `users.messages.line.Abort`.

* Adicionado novo tipo de evento `users.messages.line.Click`.

* Adicionado novo tipo de evento `users.messages.line.InboundReceive`.

* Adicionado novo tipo de evento `users.messages.line.Send`.

* Adicionado novo tipo de evento `users.messages.rcs.Abort`.

* Adicionado novo tipo de evento `users.messages.rcs.Click`.

* Adicionado novo tipo de evento `users.messages.rcs.Delivery`.

* Adicionado novo tipo de evento `users.messages.rcs.InboundReceive`.

* Adicionado novo tipo de evento `users.messages.rcs.Read`.

* Adicionado novo tipo de evento `users.messages.rcs.Rejection`.

* Adicionado novo tipo de evento `users.messages.rcs.Send`.

* Mudanças de campo para o tipo de evento `users.messages.sms.Delivery`:
    * Adicionado novo campo `boolean` `is_sms_fallback`: Indica que uma mensagem SMS de fallback foi enviada devido a uma mensagem RCS rejeitada. A mensagem pode resultar em entrega, falha de entrega ou rejeição. Pode ser vinculada ao evento de rejeição RCS por meio de um ID de envio e ID de despacho

* Mudanças de campo para o tipo de evento `users.messages.sms.DeliveryFailure`:
    * Adicionado novo campo `boolean` `is_sms_fallback`: Indica que uma mensagem SMS de fallback foi enviada devido a uma mensagem RCS rejeitada. A mensagem pode resultar em entrega, falha de entrega ou rejeição. Pode ser vinculada ao evento de rejeição RCS por meio de um ID de envio e ID de despacho

* Mudanças de campo para o tipo de evento `users.messages.sms.Rejection`:
    * Adicionado novo campo `boolean` `is_sms_fallback`: Indica que uma mensagem SMS de fallback foi enviada devido a uma mensagem RCS rejeitada. A mensagem pode resultar em entrega, falha de entrega ou rejeição. Pode ser vinculada ao evento de rejeição RCS por meio de um ID de envio e ID de despacho. (Propriedade do evento)

* Mudanças de campo para o tipo de evento `users.messages.whatsapp.Delivery`:
    * Adicionado novo campo `string` `flow_id`: O ID único do fluxo no gerenciador do WhatsApp. Presente se a mensagem incluir um CTA para responder a um fluxo do WhatsApp
    * Adicionado novo campo `string` `template_name`: [IPI] Nome do modelo no gerenciador do WhatsApp. Presente ao enviar uma mensagem de modelo
    * Adicionado novo campo `string` `message_id`: O ID único gerado pela Meta para esta mensagem

* Mudanças de campo para o tipo de evento `users.messages.whatsapp.Failure`:
    * Adicionado novo campo `string` `message_id`: O ID único gerado pela Meta para esta mensagem
    * Adicionado novo campo `string` `template_name`: [IPI] Nome do modelo no gerenciador do WhatsApp. Presente ao enviar uma mensagem de modelo
    * Adicionado novo campo `string` `flow_id`: O ID único do fluxo no gerenciador do WhatsApp. Presente se a mensagem incluir um CTA para responder a um fluxo do WhatsApp

* Mudanças de campo para o tipo de evento `users.messages.whatsapp.InboundReceive`:
    * Adicionado novo campo `string` `catalog_id`: ID do catálogo de produto, caso um produto seja mencionado na mensagem recebida. Caso contrário, permanece vazio.
    * Adicionado novo campo `string` `product_id`: SKU do produto, caso um produto seja mencionado na mensagem recebida. Caso contrário, permanece vazio.
    * Adicionado novo campo `string` `flow_id`: O ID único do fluxo no gerenciador do WhatsApp. Presente se o usuário estiver respondendo a um fluxo do WhatsApp.
    * Adicionado novo campo `string` `flow_response_json`: [IPI] Os valores do formulário com os quais o usuário respondeu. Presente se o usuário estiver respondendo a um fluxo do WhatsApp.
    * Adicionado novo campo `string` `message_id`: O ID único gerado pela Meta para esta mensagem
    * Adicionado novo campo `string` `in_reply_to`: O message_id da mensagem à qual esta mensagem estava respondendo

* Mudanças de campo para o tipo de evento `users.messages.whatsapp.Read`:
    * Adicionado novo campo `string` `template_name`: [IPI] Nome do modelo no gerenciador do WhatsApp. Presente ao enviar uma mensagem de modelo
    * Adicionado novo campo `string` `message_id`: O ID único gerado pela Meta para esta mensagem
    * Adicionado novo campo `string` `flow_id`: O ID único do fluxo no gerenciador do WhatsApp. Presente se a mensagem incluir um CTA para responder a um fluxo do WhatsApp

* Mudanças de campo para o tipo de evento `users.messages.whatsapp.Send`:
    * Adicionado novo campo `string` `flow_id`: O ID único do fluxo no gerenciador do WhatsApp. Presente se a mensagem incluir um CTA para responder a um fluxo do WhatsApp
    * Adicionado novo campo `string` `template_name`: [IPI] Nome do modelo no gerenciador do WhatsApp. Presente ao enviar uma mensagem de modelo
    * Adicionado novo campo `string` `message_id`: O ID único gerado pela Meta para esta mensagem

## Mudanças na Versão 2 (data de lançamento nula)

### Mudanças para armazenamento:

* Adicionado novo tipo de evento `users.behaviors.app.FirstSession`.

* Adicionado novo tipo de evento `users.behaviors.app.SessionEnd`.

* Adicionado novo tipo de evento `users.behaviors.app.SessionStart`.

* Adicionado novo tipo de evento `users.behaviors.CustomEvent`.

* Adicionado novo tipo de evento `users.behaviors.InstallAttribution`.

* Adicionado novo tipo de evento `users.behaviors.liveactivity.PushToStartTokenChange`.

* Adicionado novo tipo de evento `users.behaviors.liveactivity.UpdateTokenChange`.

* Adicionado novo tipo de evento `users.behaviors.Location`.

* Adicionado novo tipo de evento `users.behaviors.Purchase`.

* Adicionado novo tipo de evento `users.behaviors.pushnotification.TokenStateChange`.

* Adicionado novo tipo de evento `users.behaviors.subscription.GlobalStateChange`.

* Adicionado novo tipo de evento `users.behaviors.subscriptiongroup.StateChange`.

* Adicionado novo tipo de evento `users.behaviors.Uninstall`.

* Adicionado novo tipo de evento `users.campaigns.Conversion`.

* Adicionado novo tipo de evento `users.campaigns.EnrollInControl`.

* Adicionado novo tipo de evento `users.canvas.Conversion`.

* Adicionado novo tipo de evento `users.canvas.Entry`.

* Adicionado novo tipo de evento `users.canvas.exit.MatchedAudience`.

* Adicionado novo tipo de evento `users.canvas.exit.PerformedEvent`.

* Adicionado novo tipo de evento `users.canvas.experimentstep.Conversion`.

* Adicionado novo tipo de evento `users.canvas.experimentstep.SplitEntry`.

* Adicionado novo tipo de evento `users.canvasstep.Progression`.

* Adicionado novo tipo de evento `users.messages.banner.Abort`.

* Adicionado novo tipo de evento `users.messages.banner.Click`.

* Adicionado novo tipo de evento `users.messages.banner.Impression`.

* Adicionado novo tipo de evento `users.messages.contentcard.Abort`.

* Adicionado novo tipo de evento `users.messages.contentcard.Click`.

* Adicionado novo tipo de evento `users.messages.contentcard.Dismiss`.

* Adicionado novo tipo de evento `users.messages.contentcard.Impression`.

* Adicionado novo tipo de evento `users.messages.contentcard.Send`.

* Adicionado novo tipo de evento `users.messages.email.Abort`.

* Adicionado novo tipo de evento `users.messages.email.Bounce`.

* Adicionado novo tipo de evento `users.messages.email.Click`.

* Adicionado novo tipo de evento `users.messages.email.Deferral`.

* Adicionado novo tipo de evento `users.messages.email.Delivery`.

* Adicionado novo tipo de evento `users.messages.email.MarkAsSpam`.

* Adicionado novo tipo de evento `users.messages.email.Open`.

* Adicionado novo tipo de evento `users.messages.email.Send`.

* Adicionado novo tipo de evento `users.messages.email.SoftBounce`.

* Adicionado novo tipo de evento `users.messages.email.Unsubscribe`.

* Adicionado novo tipo de evento `users.messages.featureflag.Impression`.

* Adicionado novo tipo de evento `users.messages.inappmessage.Abort`.

* Adicionado novo tipo de evento `users.messages.inappmessage.Click`.

* Adicionado novo tipo de evento `users.messages.inappmessage.Impression`.

* Adicionado novo tipo de evento `users.messages.liveactivity.Outcome`.

* Adicionado novo tipo de evento `users.messages.liveactivity.Send`.

* Adicionado novo tipo de evento `users.messages.pushnotification.Abort`.

* Adicionado novo tipo de evento `users.messages.pushnotification.Bounce`.

* Adicionado novo tipo de evento `users.messages.pushnotification.IosForeground`.

* Adicionado novo tipo de evento `users.messages.pushnotification.Open`.

* Adicionado novo tipo de evento `users.messages.pushnotification.Send`.

* Adicionado novo tipo de evento `users.messages.sms.Abort`.

* Adicionado novo tipo de evento `users.messages.sms.CarrierSend`.

* Adicionado novo tipo de evento `users.messages.sms.Delivery`.

* Adicionado novo tipo de evento `users.messages.sms.DeliveryFailure`.

* Adicionado novo tipo de evento `users.messages.sms.InboundReceive`.

* Adicionado novo tipo de evento `users.messages.sms.Rejection`.

* Adicionado novo tipo de evento `users.messages.sms.Send`.

* Adicionado novo tipo de evento `users.messages.sms.ShortLinkClick`.

* Adicionado novo tipo de evento `users.messages.webhook.Abort`.

* Adicionado novo tipo de evento `users.messages.webhook.Failure`.

* Adicionado novo tipo de evento `users.messages.webhook.Send`.

* Adicionado novo tipo de evento `users.messages.whatsapp.Abort`.

* Adicionado novo tipo de evento `users.messages.whatsapp.Click`.

* Adicionado novo tipo de evento `users.messages.whatsapp.Delivery`.

* Adicionado novo tipo de evento `users.messages.whatsapp.Failure`.

* Adicionado novo tipo de evento `users.messages.whatsapp.InboundReceive`.

* Adicionado novo tipo de evento `users.messages.whatsapp.Read`.

* Adicionado novo tipo de evento `users.messages.whatsapp.Send`.

* Adicionado novo tipo de evento `users.RandomBucketNumberUpdate`.