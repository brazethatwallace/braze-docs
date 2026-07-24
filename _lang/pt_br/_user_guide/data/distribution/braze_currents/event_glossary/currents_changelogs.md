---
nav_title: Changelogs de eventos do Currents
page_order: 6
description: "Esta página inclui as mudanças de eventos para cada lançamento do Currents."
tool: Currents
---

# Changelog do Currents {#currents-changelog}

## Mudanças na versão 11 (data de lançamento 2026-08-05) {#changes-in-version-11-release-date-2026-08-05}

### Mudanças para armazenamento: {#changes-for-storage}

* Adicionado novo tipo de evento `contentoptimizer.ComponentStore`.

* Adicionado novo tipo de evento `users.canvas.costep.Conversion`.

* Adicionado novo tipo de evento `users.messages.landingpage.Click`.

* Adicionado novo tipo de evento `users.messages.landingpage.FormSubmission`.

* Adicionado novo tipo de evento `users.messages.landingpage.Impression`.

* Adicionado novo tipo de evento `users.messages.survey.Response`.

* Mudanças de campo para o tipo de evento `agentconsole.AgentExecuted`:
    * Adicionado novo campo `string` `thinking_level`: o nível de raciocínio utilizado para a solicitação

* Mudanças de campo para o tipo de evento `users.messages.banner.Click`:
    * Adicionado novo campo `boolean` `is_unique`: Se este foi o primeiro clique do usuário na variação da mensagem, contando para as estatísticas de cliques únicos

* Mudanças de campo para o tipo de evento `users.messages.banner.Dismiss`:
    * Adicionado novo campo `boolean` `is_unique`: Se esta foi a primeira dispensa do usuário da variação da mensagem, contando para as estatísticas de dispensas únicas

* Mudanças de campo para o tipo de evento `users.messages.banner.Impression`:
    * Adicionado novo campo `boolean` `is_unique`: Se esta foi a primeira impressão do usuário da variação da mensagem, contando para as estatísticas de impressões únicas

* Mudanças de campo para o tipo de evento `users.messages.contentcard.Click`:
    * Adicionado novo campo `boolean` `is_unique`: Se este foi o primeiro clique do usuário na variação da mensagem, contando para as estatísticas de cliques únicos

* Mudanças de campo para o tipo de evento `users.messages.contentcard.Dismiss`:
    * Adicionado novo campo `boolean` `is_unique`: Se esta foi a primeira dispensa do usuário da variação da mensagem, contando para as estatísticas de dispensas únicas

* Mudanças de campo para o tipo de evento `users.messages.contentcard.Impression`:
    * Adicionado novo campo `boolean` `is_unique`: Se esta foi a primeira impressão do usuário da variação da mensagem, contando para as estatísticas de impressões únicas

* Mudanças de campo para o tipo de evento `users.messages.featureflag.Impression`:
    * Adicionado novo campo `boolean` `is_unique`: Se esta foi a primeira impressão do usuário para esta Feature Flag, contando para as estatísticas de impressões únicas

## Mudanças na versão 10 (data de lançamento 2026-07-01) {#changes-in-version-10-release-date-2026-07-01}

### Mudanças para armazenamento:

* Adicionado novo tipo de evento `users.canvas.costep.Send`.

* Adicionado novo tipo de evento `users.UserDeleteRequest`.

* Adicionado novo tipo de evento `users.UserOrphan`.

* Mudanças de campo para o tipo de evento `users.messages.rcs.Abort`:
    * Adicionado novo campo `string` `canvas_id`: ID da API do Canvas ao qual este evento pertence

* Mudanças de campo para o tipo de evento `users.messages.rcs.Click`:
    * Adicionado novo campo `string` `canvas_id`: ID da API do Canvas ao qual este evento pertence

* Mudanças de campo para o tipo de evento `users.messages.rcs.Delivery`:
    * Adicionado novo campo `string` `canvas_id`: ID da API do Canvas ao qual este evento pertence

* Mudanças de campo para o tipo de evento `users.messages.rcs.InboundReceive`:
    * Adicionado novo campo `string` `canvas_id`: ID da API do Canvas ao qual este evento pertence

* Mudanças de campo para o tipo de evento `users.messages.rcs.Read`:
    * Adicionado novo campo `string` `canvas_id`: ID da API do Canvas ao qual este evento pertence

* Mudanças de campo para o tipo de evento `users.messages.rcs.Rejection`:
    * Adicionado novo campo `string` `canvas_id`: ID da API do Canvas ao qual este evento pertence

* Mudanças de campo para o tipo de evento `users.messages.rcs.Send`:
    * Adicionado novo campo `string` `canvas_id`: ID da API do Canvas ao qual este evento pertence

## Mudanças na versão 9 (data de lançamento 2026-06-03) {#changes-in-version-9-release-date-2026-06-03}

### Mudanças para armazenamento:

* Mudanças de campo para o tipo de evento `users.messages.email.Send`:
    * Adicionado novo campo `string` `from_domain`: Domínio de envio do e-mail

## Mudanças na versão 8 (data de lançamento 2026-05-06) {#changes-in-version-8-release-date-2026-05-06}

### Mudanças para armazenamento:

* Adicionado novo tipo de evento `users.messages.banner.Dismiss`.

* Mudanças de campo para o tipo de evento `users.messages.whatsapp.Abort`:
    * Adicionado novo campo `string` `bsuid`: O WhatsApp Business-Scoped User ID do destinatário associado a este evento.

* Mudanças de campo para o tipo de evento `users.messages.whatsapp.Delivery`:
    * Adicionado novo campo `string` `bsuid`: O WhatsApp Business-Scoped User ID do destinatário associado a este evento.

* Mudanças de campo para o tipo de evento `users.messages.whatsapp.Failure`:
    * Adicionado novo campo `string` `bsuid`: O WhatsApp Business-Scoped User ID do destinatário associado a este evento.

* Mudanças de campo para o tipo de evento `users.messages.whatsapp.InboundReceive`:
    * Adicionado novo campo `string` `bsuid`: O WhatsApp Business-Scoped User ID do usuário do qual a mensagem foi recebida.
    * O campo `user_phone_number` agora é *opcional*.

* Mudanças de campo para o tipo de evento `users.messages.whatsapp.Read`:
    * Adicionado novo campo `string` `bsuid`: O WhatsApp Business-Scoped User ID do destinatário associado a este evento.

* Mudanças de campo para o tipo de evento `users.messages.whatsapp.Retry`:
    * Adicionado novo campo `string` `bsuid`: O WhatsApp Business-Scoped User ID do destinatário associado a este evento.

* Mudanças de campo para o tipo de evento `users.messages.whatsapp.Send`:
    * Adicionado novo campo `string` `bsuid`: O WhatsApp Business-Scoped User ID do destinatário associado a este evento.

## Mudanças na versão 7 (data de lançamento 2026-04-01) {#changes-in-version-7-release-date-2026-04-01}

### Mudanças para armazenamento:

* Adicionado novo tipo de evento `users.profile.Update`.

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

## Mudanças na versão 6 (data de lançamento 2026-03-04) {#changes-in-version-6-release-date-2026-03-04}

### Mudanças para armazenamento:

* Mudanças de campo para o tipo de evento `agentconsole.AgentExecuted`:
    * Adicionado novo campo `string` `error`: Descrição do erro

* Mudanças de campo para o tipo de evento `agentconsole.ToolInvocation`:
    * Adicionado novo campo `string` `request_id`: ID único para esta solicitação geral de LLM e execução completa

* Mudanças de campo para o tipo de evento `users.messages.rcs.InboundReceive`:
    * Adicionado novo campo `string` `canvas_variation_name`: Nome da variação do Canvas que este usuário recebeu

## Mudanças na versão 5 (data de lançamento 2026-02-04) {#changes-in-version-5-release-date-2026-02-04}

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

## Mudanças na versão 4 (data de lançamento 2026-01-07) {#changes-in-version-4-release-date-2026-01-07}

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

## Mudanças na versão 3 (data de lançamento 2025-10-08) {#changes-in-version-3-release-date-2025-10-08}

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
    * Adicionado novo campo `boolean` `is_sms_fallback`: Indica que uma mensagem SMS de fallback foi enviada devido a uma mensagem RCS rejeitada. A mensagem pode resultar em entrega, falha de entrega ou rejeição. Pode ser vinculada ao evento de rejeição RCS por meio de um send ID e dispatch ID

* Mudanças de campo para o tipo de evento `users.messages.sms.DeliveryFailure`:
    * Adicionado novo campo `boolean` `is_sms_fallback`: Indica que uma mensagem SMS de fallback foi enviada devido a uma mensagem RCS rejeitada. A mensagem pode resultar em entrega, falha de entrega ou rejeição. Pode ser vinculada ao evento de rejeição RCS por meio de um send ID e dispatch ID

* Mudanças de campo para o tipo de evento `users.messages.sms.Rejection`:
    * Adicionado novo campo `boolean` `is_sms_fallback`: Indica que uma mensagem SMS de fallback foi enviada devido a uma mensagem RCS rejeitada. A mensagem pode resultar em entrega, falha de entrega ou rejeição. Pode ser vinculada ao evento de rejeição RCS por meio de um send ID e dispatch ID

* Mudanças de campo para o tipo de evento `users.messages.whatsapp.Delivery`:
    * Adicionado novo campo `string` `flow_id`: O ID único do Flow no WhatsApp Manager. Presente se a mensagem incluir um CTA para responder a um WhatsApp Flow
    * Adicionado novo campo `string` `template_name`: [IPI] Nome do modelo no WhatsApp Manager. Presente ao enviar uma mensagem de modelo
    * Adicionado novo campo `string` `message_id`: O ID único gerado pela Meta para esta mensagem

* Mudanças de campo para o tipo de evento `users.messages.whatsapp.Failure`:
    * Adicionado novo campo `string` `message_id`: O ID único gerado pela Meta para esta mensagem
    * Adicionado novo campo `string` `template_name`: [IPI] Nome do modelo no WhatsApp Manager. Presente ao enviar uma mensagem de modelo
    * Adicionado novo campo `string` `flow_id`: O ID único do Flow no WhatsApp Manager. Presente se a mensagem incluir um CTA para responder a um WhatsApp Flow

* Mudanças de campo para o tipo de evento `users.messages.whatsapp.InboundReceive`:
    * Adicionado novo campo `string` `catalog_id`: ID do catálogo de um produto, caso um produto seja mencionado na mensagem recebida. Caso contrário, vazio.
    * Adicionado novo campo `string` `product_id`: SKU do produto, caso um produto seja mencionado na mensagem recebida. Caso contrário, vazio.
    * Adicionado novo campo `string` `flow_id`: O ID único do Flow no WhatsApp Manager. Presente se o usuário estiver respondendo a um WhatsApp Flow.
    * Adicionado novo campo `string` `flow_response_json`: [IPI] Os valores do formulário com os quais o usuário respondeu. Presente se o usuário estiver respondendo a um WhatsApp Flow.
    * Adicionado novo campo `string` `message_id`: O ID único gerado pela Meta para esta mensagem
    * Adicionado novo campo `string` `in_reply_to`: O message_id da mensagem à qual esta mensagem estava respondendo

* Mudanças de campo para o tipo de evento `users.messages.whatsapp.Read`:
    * Adicionado novo campo `string` `template_name`: [IPI] Nome do modelo no WhatsApp Manager. Presente ao enviar uma mensagem de modelo
    * Adicionado novo campo `string` `message_id`: O ID único gerado pela Meta para esta mensagem
    * Adicionado novo campo `string` `flow_id`: O ID único do Flow no WhatsApp Manager. Presente se a mensagem incluir um CTA para responder a um WhatsApp Flow

* Mudanças de campo para o tipo de evento `users.messages.whatsapp.Send`:
    * Adicionado novo campo `string` `flow_id`: O ID único do Flow no WhatsApp Manager. Presente se a mensagem incluir um CTA para responder a um WhatsApp Flow
    * Adicionado novo campo `string` `template_name`: [IPI] Nome do modelo no WhatsApp Manager. Presente ao enviar uma mensagem de modelo
    * Adicionado novo campo `string` `message_id`: O ID único gerado pela Meta para esta mensagem

## Mudanças na versão 2 (data de lançamento nula) {#changes-in-version-2-release-date-null}

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