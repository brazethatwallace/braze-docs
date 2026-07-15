---
nav_title: Currents-Changelog
page_order: 6
description: "Diese Seite enthält die Event-Änderungen für jede Currents-Version."
tool: Currents
---

# Currents-Changelog {#currents-changelog}

## Änderungen in Version 10 (Veröffentlichungsdatum: 01.07.2026) {#changes-in-version-10-release-date-2026-07-01}

### Änderungen für Storage: {#changes-for-storage}

* Neuer Event-Typ `users.canvas.costep.Send` hinzugefügt.

* Neuer Event-Typ `users.UserDeleteRequest` hinzugefügt.

* Neuer Event-Typ `users.UserOrphan` hinzugefügt.

* Feldänderungen am Event-Typ `users.messages.rcs.Abort`:
    * Neues `string`-Feld `canvas_id` hinzugefügt: API-ID des Canvas, zu dem dieses Event gehört

* Feldänderungen am Event-Typ `users.messages.rcs.Click`:
    * Neues `string`-Feld `canvas_id` hinzugefügt: API-ID des Canvas, zu dem dieses Event gehört

* Feldänderungen am Event-Typ `users.messages.rcs.Delivery`:
    * Neues `string`-Feld `canvas_id` hinzugefügt: API-ID des Canvas, zu dem dieses Event gehört

* Feldänderungen am Event-Typ `users.messages.rcs.InboundReceive`:
    * Neues `string`-Feld `canvas_id` hinzugefügt: API-ID des Canvas, zu dem dieses Event gehört

* Feldänderungen am Event-Typ `users.messages.rcs.Read`:
    * Neues `string`-Feld `canvas_id` hinzugefügt: API-ID des Canvas, zu dem dieses Event gehört

* Feldänderungen am Event-Typ `users.messages.rcs.Rejection`:
    * Neues `string`-Feld `canvas_id` hinzugefügt: API-ID des Canvas, zu dem dieses Event gehört

* Feldänderungen am Event-Typ `users.messages.rcs.Send`:
    * Neues `string`-Feld `canvas_id` hinzugefügt: API-ID des Canvas, zu dem dieses Event gehört

## Änderungen in Version 9 (Veröffentlichungsdatum: 03.06.2026) {#changes-in-version-9-release-date-2026-06-03}

### Änderungen für Storage:

* Feldänderungen am Event-Typ `users.messages.email.Send`:
    * Neues `string`-Feld `from_domain` hinzugefügt: Sende-Domain für die E-Mail

## Änderungen in Version 8 (Veröffentlichungsdatum: 06.05.2026) {#changes-in-version-8-release-date-2026-05-06}

### Änderungen für Storage:

* Neuer Event-Typ `users.messages.banner.Dismiss` hinzugefügt.

* Feldänderungen am Event-Typ `users.messages.whatsapp.Abort`:
    * Neues `string`-Feld `bsuid` hinzugefügt: Die WhatsApp Business-Scoped User ID der Empfängerin bzw. des Empfängers, die bzw. der mit diesem Event verknüpft ist.

* Feldänderungen am Event-Typ `users.messages.whatsapp.Delivery`:
    * Neues `string`-Feld `bsuid` hinzugefügt: Die WhatsApp Business-Scoped User ID der Empfängerin bzw. des Empfängers, die bzw. der mit diesem Event verknüpft ist.

* Feldänderungen am Event-Typ `users.messages.whatsapp.Failure`:
    * Neues `string`-Feld `bsuid` hinzugefügt: Die WhatsApp Business-Scoped User ID der Empfängerin bzw. des Empfängers, die bzw. der mit diesem Event verknüpft ist.

* Feldänderungen am Event-Typ `users.messages.whatsapp.InboundReceive`:
    * Neues `string`-Feld `bsuid` hinzugefügt: Die WhatsApp Business-Scoped User ID der Nutzer:innen, von denen die Nachricht empfangen wurde.
    * Das Feld `user_phone_number` ist jetzt *optional*.

* Feldänderungen am Event-Typ `users.messages.whatsapp.Read`:
    * Neues `string`-Feld `bsuid` hinzugefügt: Die WhatsApp Business-Scoped User ID der Empfängerin bzw. des Empfängers, die bzw. der mit diesem Event verknüpft ist.

* Feldänderungen am Event-Typ `users.messages.whatsapp.Retry`:
    * Neues `string`-Feld `bsuid` hinzugefügt: Die WhatsApp Business-Scoped User ID der Empfängerin bzw. des Empfängers, die bzw. der mit diesem Event verknüpft ist.

* Feldänderungen am Event-Typ `users.messages.whatsapp.Send`:
    * Neues `string`-Feld `bsuid` hinzugefügt: Die WhatsApp Business-Scoped User ID der Empfängerin bzw. des Empfängers, die bzw. der mit diesem Event verknüpft ist.

## Änderungen in Version 7 (Veröffentlichungsdatum: 01.04.2026) {#changes-in-version-7-release-date-2026-04-01}

### Änderungen für Storage:

* Neuer Event-Typ `users.profile.Update` hinzugefügt.

* Feldänderungen am Event-Typ `users.messages.banner.Abort`:
    * Neues `string`-Feld `canvas_name` hinzugefügt: Name des Canvas
    * Neues `string`-Feld `canvas_step_name` hinzugefügt: Name des Canvas-Schritts
    * Neues `string`-Feld `canvas_variation_name` hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Neues `string`-Feld `canvas_id` hinzugefügt: API-ID des Canvas, zu dem dieses Event gehört
    * Neues `string`-Feld `canvas_step_id` hinzugefügt: API-ID des Canvas-Schritts, zu dem dieses Event gehört
    * Neues `string`-Feld `canvas_step_message_variation_id` hinzugefügt: API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Nutzer:in erhalten hat
    * Neues `string`-Feld `canvas_variation_id` hinzugefügt: API-ID der Canvas-Variante, zu der dieses Event gehört

* Feldänderungen am Event-Typ `users.messages.banner.Click`:
    * Neues `string`-Feld `canvas_id` hinzugefügt: API-ID des Canvas, zu dem dieses Event gehört
    * Neues `string`-Feld `canvas_step_id` hinzugefügt: API-ID des Canvas-Schritts, zu dem dieses Event gehört
    * Neues `string`-Feld `canvas_name` hinzugefügt: Name des Canvas
    * Neues `string`-Feld `canvas_step_name` hinzugefügt: Name des Canvas-Schritts
    * Neues `string`-Feld `canvas_step_message_variation_id` hinzugefügt: API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Nutzer:in erhalten hat
    * Neues `string`-Feld `canvas_variation_id` hinzugefügt: API-ID der Canvas-Variante, zu der dieses Event gehört
    * Neues `string`-Feld `canvas_variation_name` hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat

* Feldänderungen am Event-Typ `users.messages.banner.Impression`:
    * Neues `string`-Feld `canvas_id` hinzugefügt: API-ID des Canvas, zu dem dieses Event gehört
    * Neues `string`-Feld `canvas_step_id` hinzugefügt: API-ID des Canvas-Schritts, zu dem dieses Event gehört
    * Neues `string`-Feld `canvas_name` hinzugefügt: Name des Canvas
    * Neues `string`-Feld `canvas_step_name` hinzugefügt: Name des Canvas-Schritts
    * Neues `string`-Feld `canvas_step_message_variation_id` hinzugefügt: API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Nutzer:in erhalten hat
    * Neues `string`-Feld `canvas_variation_id` hinzugefügt: API-ID der Canvas-Variante, zu der dieses Event gehört
    * Neues `string`-Feld `canvas_variation_name` hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat

## Änderungen in Version 6 (Veröffentlichungsdatum: 04.03.2026) {#changes-in-version-6-release-date-2026-03-04}

### Änderungen für Storage:

* Feldänderungen am Event-Typ `agentconsole.AgentExecuted`:
    * Neues `string`-Feld `error` hinzugefügt: Beschreibung des Fehlers

* Feldänderungen am Event-Typ `agentconsole.ToolInvocation`:
    * Neues `string`-Feld `request_id` hinzugefügt: Eindeutige ID für diese gesamte LLM-Anfrage und vollständige Ausführung

* Feldänderungen am Event-Typ `users.messages.rcs.InboundReceive`:
    * Neues `string`-Feld `canvas_variation_name` hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat

## Änderungen in Version 5 (Veröffentlichungsdatum: 04.02.2026) {#changes-in-version-5-release-date-2026-02-04}

### Änderungen für Storage:

* Neuer Event-Typ `agentconsole.AgentExecuted` hinzugefügt.

* Neuer Event-Typ `agentconsole.ToolInvocation` hinzugefügt.

* Neuer Event-Typ `users.messages.email.Retry` hinzugefügt.

* Neuer Event-Typ `users.messages.line.Retry` hinzugefügt.

* Neuer Event-Typ `users.messages.pushnotification.Retry` hinzugefügt.

* Neuer Event-Typ `users.messages.sms.Retry` hinzugefügt.

* Neuer Event-Typ `users.messages.webhook.Retry` hinzugefügt.

* Neuer Event-Typ `users.messages.whatsapp.Retry` hinzugefügt.

* Feldänderungen am Event-Typ `users.behaviors.pushnotification.TokenStateChange`:
    * Neues `long`-Feld `time_ms` hinzugefügt: Zeitpunkt in Millisekunden, zu dem das Event stattfand

## Änderungen in Version 4 (Veröffentlichungsdatum: 07.01.2026) {#changes-in-version-4-release-date-2026-01-07}

### Änderungen für Storage:

* Feldänderungen am Event-Typ `users.behaviors.pushnotification.TokenStateChange`:
    * Neues `string`-Feld `push_token` hinzugefügt: Push-Token des Events

* Feldänderungen am Event-Typ `users.messages.pushnotification.Bounce`:
    * Neues `string`-Feld `push_token` hinzugefügt: Push-Token des Events

* Feldänderungen am Event-Typ `users.messages.pushnotification.Send`:
    * Neues `string`-Feld `push_token` hinzugefügt: Push-Token des Events

* Feldänderungen am Event-Typ `users.messages.rcs.Click`:
    * Neues `string`-Feld `canvas_variation_name` hinzugefügt: Name der Canvas-Variante, die diese Nutzer:in erhalten hat
    * Das Feld `user_phone_number` ist jetzt *optional*.

* Feldänderungen am Event-Typ `users.messages.rcs.InboundReceive`:
    * Das Feld `user_id` ist jetzt *optional*.

* Feldänderungen am Event-Typ `users.messages.rcs.Rejection`:
    * Neues `string`-Feld `canvas_step_message_variation_id` hinzugefügt: API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Nutzer:in erhalten hat

## Änderungen in Version 3 (Veröffentlichungsdatum: 08.10.2025) {#changes-in-version-3-release-date-2025-10-08}

### Änderungen für Storage:

* Neuer Event-Typ `users.messages.line.Abort` hinzugefügt.

* Neuer Event-Typ `users.messages.line.Click` hinzugefügt.

* Neuer Event-Typ `users.messages.line.InboundReceive` hinzugefügt.

* Neuer Event-Typ `users.messages.line.Send` hinzugefügt.

* Neuer Event-Typ `users.messages.rcs.Abort` hinzugefügt.

* Neuer Event-Typ `users.messages.rcs.Click` hinzugefügt.

* Neuer Event-Typ `users.messages.rcs.Delivery` hinzugefügt.

* Neuer Event-Typ `users.messages.rcs.InboundReceive` hinzugefügt.

* Neuer Event-Typ `users.messages.rcs.Read` hinzugefügt.

* Neuer Event-Typ `users.messages.rcs.Rejection` hinzugefügt.

* Neuer Event-Typ `users.messages.rcs.Send` hinzugefügt.

* Feldänderungen am Event-Typ `users.messages.sms.Delivery`:
    * Neues `boolean`-Feld `is_sms_fallback` hinzugefügt: Gibt an, dass aufgrund einer abgelehnten RCS-Nachricht eine SMS-Fallback-Nachricht gesendet wurde. Die Nachricht kann zugestellt werden, fehlschlagen oder abgelehnt werden. Sie kann über eine Sende-ID und eine Dispatch-ID mit dem RCS-Rejection-Event verknüpft werden.

* Feldänderungen am Event-Typ `users.messages.sms.DeliveryFailure`:
    * Neues `boolean`-Feld `is_sms_fallback` hinzugefügt: Gibt an, dass aufgrund einer abgelehnten RCS-Nachricht eine SMS-Fallback-Nachricht gesendet wurde. Die Nachricht kann zugestellt werden, fehlschlagen oder abgelehnt werden. Sie kann über eine Sende-ID und eine Dispatch-ID mit dem RCS-Rejection-Event verknüpft werden.

* Feldänderungen am Event-Typ `users.messages.sms.Rejection`:
    * Neues `boolean`-Feld `is_sms_fallback` hinzugefügt: Gibt an, dass aufgrund einer abgelehnten RCS-Nachricht eine SMS-Fallback-Nachricht gesendet wurde. Die Nachricht kann zugestellt werden, fehlschlagen oder abgelehnt werden. Sie kann über eine Sende-ID und eine Dispatch-ID mit dem RCS-Rejection-Event verknüpft werden.

* Feldänderungen am Event-Typ `users.messages.whatsapp.Delivery`:
    * Neues `string`-Feld `flow_id` hinzugefügt: Die eindeutige ID des Flows im WhatsApp Manager. Vorhanden, wenn die Nachricht einen CTA enthält, um auf einen WhatsApp-Flow zu antworten.
    * Neues `string`-Feld `template_name` hinzugefügt: [PII] Name des Templates im WhatsApp Manager. Vorhanden, wenn eine Template-Nachricht gesendet wird.
    * Neues `string`-Feld `message_id` hinzugefügt: Die von Meta für diese Nachricht generierte eindeutige ID

* Feldänderungen am Event-Typ `users.messages.whatsapp.Failure`:
    * Neues `string`-Feld `message_id` hinzugefügt: Die von Meta für diese Nachricht generierte eindeutige ID
    * Neues `string`-Feld `template_name` hinzugefügt: [PII] Name des Templates im WhatsApp Manager. Vorhanden, wenn eine Template-Nachricht gesendet wird.
    * Neues `string`-Feld `flow_id` hinzugefügt: Die eindeutige ID des Flows im WhatsApp Manager. Vorhanden, wenn die Nachricht einen CTA enthält, um auf einen WhatsApp-Flow zu antworten.

* Feldänderungen am Event-Typ `users.messages.whatsapp.InboundReceive`:
    * Neues `string`-Feld `catalog_id` hinzugefügt: Katalog-ID eines Produkts, falls ein Produkt in der eingehenden Nachricht referenziert wird. Andernfalls leer.
    * Neues `string`-Feld `product_id` hinzugefügt: Produkt-SKU, falls ein Produkt in der eingehenden Nachricht referenziert wird. Andernfalls leer.
    * Neues `string`-Feld `flow_id` hinzugefügt: Die eindeutige ID des Flows im WhatsApp Manager. Vorhanden, wenn die Nutzer:in auf einen WhatsApp-Flow antwortet.
    * Neues `string`-Feld `flow_response_json` hinzugefügt: [PII] Die Formularwerte, mit denen die Nutzer:in geantwortet hat. Vorhanden, wenn die Nutzer:in auf einen WhatsApp-Flow antwortet.
    * Neues `string`-Feld `message_id` hinzugefügt: Die von Meta für diese Nachricht generierte eindeutige ID
    * Neues `string`-Feld `in_reply_to` hinzugefügt: Die `message_id` der Nachricht, auf die diese Nachricht eine Antwort darstellt.

* Feldänderungen am Event-Typ `users.messages.whatsapp.Read`:
    * Neues `string`-Feld `template_name` hinzugefügt: [PII] Name des Templates im WhatsApp Manager. Vorhanden, wenn eine Template-Nachricht gesendet wird.
    * Neues `string`-Feld `message_id` hinzugefügt: Die von Meta für diese Nachricht generierte eindeutige ID
    * Neues `string`-Feld `flow_id` hinzugefügt: Die eindeutige ID des Flows im WhatsApp Manager. Vorhanden, wenn die Nachricht einen CTA enthält, um auf einen WhatsApp-Flow zu antworten.

* Feldänderungen am Event-Typ `users.messages.whatsapp.Send`:
    * Neues `string`-Feld `flow_id` hinzugefügt: Die eindeutige ID des Flows im WhatsApp Manager. Vorhanden, wenn die Nachricht einen CTA enthält, um auf einen WhatsApp-Flow zu antworten.
    * Neues `string`-Feld `template_name` hinzugefügt: [PII] Name des Templates im WhatsApp Manager. Vorhanden, wenn eine Template-Nachricht gesendet wird.
    * Neues `string`-Feld `message_id` hinzugefügt: Die von Meta für diese Nachricht generierte eindeutige ID

## Änderungen in Version 2 (Veröffentlichungsdatum: null) {#changes-in-version-2-release-date-null}

### Änderungen für Storage:

* Neuer Event-Typ `users.behaviors.app.FirstSession` hinzugefügt.

* Neuer Event-Typ `users.behaviors.app.SessionEnd` hinzugefügt.

* Neuer Event-Typ `users.behaviors.app.SessionStart` hinzugefügt.

* Neuer Event-Typ `users.behaviors.CustomEvent` hinzugefügt.

* Neuer Event-Typ `users.behaviors.InstallAttribution` hinzugefügt.

* Neuer Event-Typ `users.behaviors.liveactivity.PushToStartTokenChange` hinzugefügt.

* Neuer Event-Typ `users.behaviors.liveactivity.UpdateTokenChange` hinzugefügt.

* Neuer Event-Typ `users.behaviors.Location` hinzugefügt.

* Neuer Event-Typ `users.behaviors.Purchase` hinzugefügt.

* Neuer Event-Typ `users.behaviors.pushnotification.TokenStateChange` hinzugefügt.

* Neuer Event-Typ `users.behaviors.subscription.GlobalStateChange` hinzugefügt.

* Neuer Event-Typ `users.behaviors.subscriptiongroup.StateChange` hinzugefügt.

* Neuer Event-Typ `users.behaviors.Uninstall` hinzugefügt.

* Neuer Event-Typ `users.campaigns.Conversion` hinzugefügt.

* Neuer Event-Typ `users.campaigns.EnrollInControl` hinzugefügt.

* Neuer Event-Typ `users.canvas.Conversion` hinzugefügt.

* Neuer Event-Typ `users.canvas.Entry` hinzugefügt.

* Neuer Event-Typ `users.canvas.exit.MatchedAudience` hinzugefügt.

* Neuer Event-Typ `users.canvas.exit.PerformedEvent` hinzugefügt.

* Neuer Event-Typ `users.canvas.experimentstep.Conversion` hinzugefügt.

* Neuer Event-Typ `users.canvas.experimentstep.SplitEntry` hinzugefügt.

* Neuer Event-Typ `users.canvasstep.Progression` hinzugefügt.

* Neuer Event-Typ `users.messages.banner.Abort` hinzugefügt.

* Neuer Event-Typ `users.messages.banner.Click` hinzugefügt.

* Neuer Event-Typ `users.messages.banner.Impression` hinzugefügt.

* Neuer Event-Typ `users.messages.contentcard.Abort` hinzugefügt.

* Neuer Event-Typ `users.messages.contentcard.Click` hinzugefügt.

* Neuer Event-Typ `users.messages.contentcard.Dismiss` hinzugefügt.

* Neuer Event-Typ `users.messages.contentcard.Impression` hinzugefügt.

* Neuer Event-Typ `users.messages.contentcard.Send` hinzugefügt.

* Neuer Event-Typ `users.messages.email.Abort` hinzugefügt.

* Neuer Event-Typ `users.messages.email.Bounce` hinzugefügt.

* Neuer Event-Typ `users.messages.email.Click` hinzugefügt.

* Neuer Event-Typ `users.messages.email.Deferral` hinzugefügt.

* Neuer Event-Typ `users.messages.email.Delivery` hinzugefügt.

* Neuer Event-Typ `users.messages.email.MarkAsSpam` hinzugefügt.

* Neuer Event-Typ `users.messages.email.Open` hinzugefügt.

* Neuer Event-Typ `users.messages.email.Send` hinzugefügt.

* Neuer Event-Typ `users.messages.email.SoftBounce` hinzugefügt.

* Neuer Event-Typ `users.messages.email.Unsubscribe` hinzugefügt.

* Neuer Event-Typ `users.messages.featureflag.Impression` hinzugefügt.

* Neuer Event-Typ `users.messages.inappmessage.Abort` hinzugefügt.

* Neuer Event-Typ `users.messages.inappmessage.Click` hinzugefügt.

* Neuer Event-Typ `users.messages.inappmessage.Impression` hinzugefügt.

* Neuer Event-Typ `users.messages.liveactivity.Outcome` hinzugefügt.

* Neuer Event-Typ `users.messages.liveactivity.Send` hinzugefügt.

* Neuer Event-Typ `users.messages.pushnotification.Abort` hinzugefügt.

* Neuer Event-Typ `users.messages.pushnotification.Bounce` hinzugefügt.

* Neuer Event-Typ `users.messages.pushnotification.IosForeground` hinzugefügt.

* Neuer Event-Typ `users.messages.pushnotification.Open` hinzugefügt.

* Neuer Event-Typ `users.messages.pushnotification.Send` hinzugefügt.

* Neuer Event-Typ `users.messages.sms.Abort` hinzugefügt.

* Neuer Event-Typ `users.messages.sms.CarrierSend` hinzugefügt.

* Neuer Event-Typ `users.messages.sms.Delivery` hinzugefügt.

* Neuer Event-Typ `users.messages.sms.DeliveryFailure` hinzugefügt.

* Neuer Event-Typ `users.messages.sms.InboundReceive` hinzugefügt.

* Neuer Event-Typ `users.messages.sms.Rejection` hinzugefügt.

* Neuer Event-Typ `users.messages.sms.Send` hinzugefügt.

* Neuer Event-Typ `users.messages.sms.ShortLinkClick` hinzugefügt.

* Neuer Event-Typ `users.messages.webhook.Abort` hinzugefügt.

* Neuer Event-Typ `users.messages.webhook.Failure` hinzugefügt.

* Neuer Event-Typ `users.messages.webhook.Send` hinzugefügt.

* Neuer Event-Typ `users.messages.whatsapp.Abort` hinzugefügt.

* Neuer Event-Typ `users.messages.whatsapp.Click` hinzugefügt.

* Neuer Event-Typ `users.messages.whatsapp.Delivery` hinzugefügt.

* Neuer Event-Typ `users.messages.whatsapp.Failure` hinzugefügt.

* Neuer Event-Typ `users.messages.whatsapp.InboundReceive` hinzugefügt.

* Neuer Event-Typ `users.messages.whatsapp.Read` hinzugefügt.

* Neuer Event-Typ `users.messages.whatsapp.Send` hinzugefügt.

* Neuer Event-Typ `users.RandomBucketNumberUpdate` hinzugefügt.