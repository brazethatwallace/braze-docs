---
nav_title: Currents-Changelog
page_order: 6
description: "Diese Seite enthält die Event-Änderungen für jede Currents-Version."
tool: Currents
---

# Currents-Changelog {#currents-changelog}

## Änderungen in Version 12 (Veröffentlichungsdatum 02.09.2026) {#changes-in-version-12-release-date-2026-09-02}

### Änderungen für Speicher: {#changes-for-storage}

* Feldänderungen am Ereignistyp `users.messages.email.Abort`:
    * Neues `string`-Feld `message_extras` hinzugefügt: [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings

* Feldänderungen am Ereignistyp `users.messages.email.Bounce`:
    * Neues `int`-Feld `send_time` hinzugefügt: Zeitpunkt des zugehörigen Send-Ereignisses

* Feldänderungen am Ereignistyp `users.messages.email.Click`:
    * Neues `int`-Feld `send_time` hinzugefügt: Zeit in Sekunden des zugehörigen Send-Ereignisses
    * Neues `boolean`-Feld `has_url_parameters` hinzugefügt: Ob die angeklickte URL Abfrageparameter enthielt
    * Neues `boolean`-Feld `link_aliasing_enabled` hinzugefügt: Ob Link Aliasing für den Workspace aktiviert war, als dieser Klick verarbeitet wurde

* Feldänderungen am Ereignistyp `users.messages.email.Deferral`:
    * Neues `int`-Feld `send_time` hinzugefügt: Zeitpunkt des zugehörigen Send-Ereignisses

* Feldänderungen am Ereignistyp `users.messages.email.Delivery`:
    * Neues `int`-Feld `send_time` hinzugefügt: Zeitpunkt des zugehörigen Send-Ereignisses

* Feldänderungen am Ereignistyp `users.messages.email.MarkAsSpam`:
    * Neues `int`-Feld `send_time` hinzugefügt: Zeitpunkt des zugehörigen Send-Ereignisses

* Feldänderungen am Ereignistyp `users.messages.email.Open`:
    * Neues `int`-Feld `send_time` hinzugefügt: Zeitpunkt des zugehörigen Send-Ereignisses

* Feldänderungen am Ereignistyp `users.messages.email.SoftBounce`:
    * Neues `int`-Feld `send_time` hinzugefügt: Zeitpunkt des zugehörigen Send-Ereignisses

* Feldänderungen am Ereignistyp `users.messages.line.Abort`:
    * Neues `string`-Feld `message_extras` hinzugefügt: [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings

* Feldänderungen am Ereignistyp `users.messages.pushnotification.Abort`:
    * Neues `string`-Feld `message_extras` hinzugefügt: [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings

* Feldänderungen am Ereignistyp `users.messages.rcs.Abort`:
    * Neues `string`-Feld `message_extras` hinzugefügt: [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings

* Feldänderungen am Ereignistyp `users.messages.sms.Abort`:
    * Neues `string`-Feld `message_extras` hinzugefügt: [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings

* Feldänderungen am Ereignistyp `users.messages.webhook.Abort`:
    * Neues `string`-Feld `message_extras` hinzugefügt: [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings

* Feldänderungen am Ereignistyp `users.messages.whatsapp.Abort`:
    * Neues `string`-Feld `message_extras` hinzugefügt: [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings

## Änderungen in Version 11 (Veröffentlichungsdatum 05.08.2026) {#changes-in-version-11-release-date-2026-08-05}

### Änderungen für Speicher:

* Neuer Ereignistyp `contentoptimizer.ComponentStore` hinzugefügt.

* Neuer Ereignistyp `users.canvas.costep.Conversion` hinzugefügt.

* Neuer Ereignistyp `users.messages.landingpage.Click` hinzugefügt.

* Neuer Ereignistyp `users.messages.landingpage.FormSubmission` hinzugefügt.

* Neuer Ereignistyp `users.messages.landingpage.Impression` hinzugefügt.

* Neuer Ereignistyp `users.messages.survey.Response` hinzugefügt.

* Feldänderungen am Ereignistyp `agentconsole.AgentExecuted`:
    * Neues `string`-Feld `thinking_level` hinzugefügt: die für die Anfrage verwendete Denk-/Reasoning-Stufe

* Feldänderungen am Ereignistyp `users.messages.banner.Click`:
    * Neues `boolean`-Feld `is_unique` hinzugefügt: Ob dies der erste Klick der Nutzer:in auf die Nachrichtenvariante war, der zur eindeutigen Klick-Statistik zählt

* Feldänderungen am Ereignistyp `users.messages.banner.Dismiss`:
    * Neues `boolean`-Feld `is_unique` hinzugefügt: Ob dies das erste Verwerfen der Nachrichtenvariante durch die Nutzer:in war, das zur eindeutigen Verwerfungs-Statistik zählt

* Feldänderungen am Ereignistyp `users.messages.banner.Impression`:
    * Neues `boolean`-Feld `is_unique` hinzugefügt: Ob dies die erste Impression der Nachrichtenvariante für die Nutzer:in war, die zur eindeutigen Impression-Statistik zählt

* Feldänderungen am Ereignistyp `users.messages.contentcard.Click`:
    * Neues `boolean`-Feld `is_unique` hinzugefügt: Ob dies der erste Klick der Nutzer:in auf die Nachrichtenvariante war, der zur eindeutigen Klick-Statistik zählt

* Feldänderungen am Ereignistyp `users.messages.contentcard.Dismiss`:
    * Neues `boolean`-Feld `is_unique` hinzugefügt: Ob dies das erste Verwerfen der Nachrichtenvariante durch die Nutzer:in war, das zur eindeutigen Verwerfungs-Statistik zählt

* Feldänderungen am Ereignistyp `users.messages.contentcard.Impression`:
    * Neues `boolean`-Feld `is_unique` hinzugefügt: Ob dies die erste Impression der Nachrichtenvariante für die Nutzer:in war, die zur eindeutigen Impression-Statistik zählt

* Feldänderungen am Ereignistyp `users.messages.featureflag.Impression`:
    * Neues `boolean`-Feld `is_unique` hinzugefügt: Ob dies die erste Impression für dieses Feature-Flag der Nutzer:in war, die zur eindeutigen Impression-Statistik zählt

## Änderungen in Version 10 (Veröffentlichungsdatum: 01.07.2026) {#changes-in-version-10-release-date-2026-07-01}

### Änderungen für Speicher:

* Neuer Ereignistyp `users.canvas.costep.Send` hinzugefügt.

* Neuer Ereignistyp `users.UserDeleteRequest` hinzugefügt.

* Neuer Ereignistyp `users.UserOrphan` hinzugefügt.

* Feldänderungen am Ereignistyp `users.messages.rcs.Abort`:
    * Neues `string`-Feld `canvas_id` hinzugefügt: API-ID des Canvas, zu dem dieses Ereignis gehört

* Feldänderungen am Ereignistyp `users.messages.rcs.Click`:
    * Neues `string`-Feld `canvas_id` hinzugefügt: API-ID des Canvas, zu dem dieses Ereignis gehört

* Feldänderungen am Ereignistyp `users.messages.rcs.Delivery`:
    * Neues `string`-Feld `canvas_id` hinzugefügt: API-ID des Canvas, zu dem dieses Ereignis gehört

* Feldänderungen am Ereignistyp `users.messages.rcs.InboundReceive`:
    * Neues `string`-Feld `canvas_id` hinzugefügt: API-ID des Canvas, zu dem dieses Ereignis gehört

* Feldänderungen am Ereignistyp `users.messages.rcs.Read`:
    * Neues `string`-Feld `canvas_id` hinzugefügt: API-ID des Canvas, zu dem dieses Ereignis gehört

* Feldänderungen am Ereignistyp `users.messages.rcs.Rejection`:
    * Neues `string`-Feld `canvas_id` hinzugefügt: API-ID des Canvas, zu dem dieses Ereignis gehört

* Feldänderungen am Ereignistyp `users.messages.rcs.Send`:
    * Neues `string`-Feld `canvas_id` hinzugefügt: API-ID des Canvas, zu dem dieses Ereignis gehört

## Änderungen in Version 9 (Veröffentlichungsdatum: 03.06.2026) {#changes-in-version-9-release-date-2026-06-03}

### Änderungen für Speicher:

* Feldänderungen am Ereignistyp `users.messages.email.Send`:
    * Neues `string`-Feld `from_domain` hinzugefügt: Absende-Domain für die E-Mail

## Änderungen in Version 8 (Veröffentlichungsdatum 06.05.2026) {#changes-in-version-8-release-date-2026-05-06}

### Änderungen für Speicherung:

* Neuer Ereignistyp `users.messages.banner.Dismiss` hinzugefügt.

* Feldänderungen am Ereignistyp `users.messages.whatsapp.Abort`:
    * Neues `string`-Feld `bsuid` hinzugefügt: Die WhatsApp Business-Scoped User ID der Empfängerin bzw. des Empfängers, die bzw. der mit diesem Ereignis verknüpft ist.

* Feldänderungen am Ereignistyp `users.messages.whatsapp.Delivery`:
    * Neues `string`-Feld `bsuid` hinzugefügt: Die WhatsApp Business-Scoped User ID der Empfängerin bzw. des Empfängers, die bzw. der mit diesem Ereignis verknüpft ist.

* Feldänderungen am Ereignistyp `users.messages.whatsapp.Failure`:
    * Neues `string`-Feld `bsuid` hinzugefügt: Die WhatsApp Business-Scoped User ID der Empfängerin bzw. des Empfängers, die bzw. der mit diesem Ereignis verknüpft ist.

* Feldänderungen am Ereignistyp `users.messages.whatsapp.InboundReceive`:
    * Neues `string`-Feld `bsuid` hinzugefügt: Die WhatsApp Business-Scoped User ID der Nutzerin bzw. des Nutzers, von der bzw. dem die Nachricht empfangen wurde.
    * Feld `user_phone_number` ist jetzt *optional*.

* Feldänderungen am Ereignistyp `users.messages.whatsapp.Read`:
    * Neues `string`-Feld `bsuid` hinzugefügt: Die WhatsApp Business-Scoped User ID der Empfängerin bzw. des Empfängers, die bzw. der mit diesem Ereignis verknüpft ist.

* Feldänderungen am Ereignistyp `users.messages.whatsapp.Retry`:
    * Neues `string`-Feld `bsuid` hinzugefügt: Die WhatsApp Business-Scoped User ID der Empfängerin bzw. des Empfängers, die bzw. der mit diesem Ereignis verknüpft ist.

* Feldänderungen am Ereignistyp `users.messages.whatsapp.Send`:
    * Neues `string`-Feld `bsuid` hinzugefügt: Die WhatsApp Business-Scoped User ID der Empfängerin bzw. des Empfängers, die bzw. der mit diesem Ereignis verknüpft ist.

## Änderungen in Version 7 (Veröffentlichungsdatum 01.04.2026) {#changes-in-version-7-release-date-2026-04-01}

### Änderungen für Speicher:

* Neuer Ereignistyp `users.profile.Update` hinzugefügt.

* Feldänderungen am Ereignistyp `users.messages.banner.Abort`:
    * Neues `string`-Feld `canvas_name` hinzugefügt: Name des Canvas
    * Neues `string`-Feld `canvas_step_name` hinzugefügt: Name des Canvas-Schritts
    * Neues `string`-Feld `canvas_variation_name` hinzugefügt: Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
    * Neues `string`-Feld `canvas_id` hinzugefügt: API-ID des Canvas, zu dem dieses Ereignis gehört
    * Neues `string`-Feld `canvas_step_id` hinzugefügt: API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
    * Neues `string`-Feld `canvas_step_message_variation_id` hinzugefügt: API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
    * Neues `string`-Feld `canvas_variation_id` hinzugefügt: API-ID der Canvas-Variante, zu der dieses Ereignis gehört

* Feldänderungen am Ereignistyp `users.messages.banner.Click`:
    * Neues `string`-Feld `canvas_id` hinzugefügt: API-ID des Canvas, zu dem dieses Ereignis gehört
    * Neues `string`-Feld `canvas_step_id` hinzugefügt: API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
    * Neues `string`-Feld `canvas_name` hinzugefügt: Name des Canvas
    * Neues `string`-Feld `canvas_step_name` hinzugefügt: Name des Canvas-Schritts
    * Neues `string`-Feld `canvas_step_message_variation_id` hinzugefügt: API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
    * Neues `string`-Feld `canvas_variation_id` hinzugefügt: API-ID der Canvas-Variante, zu der dieses Ereignis gehört
    * Neues `string`-Feld `canvas_variation_name` hinzugefügt: Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat

* Feldänderungen am Ereignistyp `users.messages.banner.Impression`:
    * Neues `string`-Feld `canvas_id` hinzugefügt: API-ID des Canvas, zu dem dieses Ereignis gehört
    * Neues `string`-Feld `canvas_step_id` hinzugefügt: API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
    * Neues `string`-Feld `canvas_name` hinzugefügt: Name des Canvas
    * Neues `string`-Feld `canvas_step_name` hinzugefügt: Name des Canvas-Schritts
    * Neues `string`-Feld `canvas_step_message_variation_id` hinzugefügt: API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
    * Neues `string`-Feld `canvas_variation_id` hinzugefügt: API-ID der Canvas-Variante, zu der dieses Ereignis gehört
    * Neues `string`-Feld `canvas_variation_name` hinzugefügt: Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat

## Änderungen in Version 6 (Veröffentlichungsdatum 04.03.2026) {#changes-in-version-6-release-date-2026-03-04}

### Änderungen für Speicher:

* Feldänderungen am Ereignistyp `agentconsole.AgentExecuted`:
    * Neues `string`-Feld `error` hinzugefügt: Beschreibung des Fehlers

* Feldänderungen am Ereignistyp `agentconsole.ToolInvocation`:
    * Neues `string`-Feld `request_id` hinzugefügt: Eindeutige ID für diese gesamte LLM-Anfrage und vollständige Ausführung

* Feldänderungen am Ereignistyp `users.messages.rcs.InboundReceive`:
    * Neues `string`-Feld `canvas_variation_name` hinzugefügt: Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat

## Änderungen in Version 5 (Veröffentlichungsdatum 04.02.2026) {#changes-in-version-5-release-date-2026-02-04}

### Änderungen für Speicher:

* Neuer Ereignistyp `agentconsole.AgentExecuted` hinzugefügt.

* Neuer Ereignistyp `agentconsole.ToolInvocation` hinzugefügt.

* Neuer Ereignistyp `users.messages.email.Retry` hinzugefügt.

* Neuer Ereignistyp `users.messages.line.Retry` hinzugefügt.

* Neuer Ereignistyp `users.messages.pushnotification.Retry` hinzugefügt.

* Neuer Ereignistyp `users.messages.sms.Retry` hinzugefügt.

* Neuer Ereignistyp `users.messages.webhook.Retry` hinzugefügt.

* Neuer Ereignistyp `users.messages.whatsapp.Retry` hinzugefügt.

* Feldänderungen am Ereignistyp `users.behaviors.pushnotification.TokenStateChange`:
    * Neues `long`-Feld `time_ms` hinzugefügt: Zeit in Millisekunden, zu der das Ereignis aufgetreten ist

## Änderungen in Version 4 (Veröffentlichungsdatum 07.01.2026) {#changes-in-version-4-release-date-2026-01-07}

### Änderungen für Speicher:

* Feldänderungen am Ereignistyp `users.behaviors.pushnotification.TokenStateChange`:
    * Neues `string`-Feld `push_token` hinzugefügt: Push-Token des Ereignisses

* Feldänderungen am Ereignistyp `users.messages.pushnotification.Bounce`:
    * Neues `string`-Feld `push_token` hinzugefügt: Push-Token des Ereignisses

* Feldänderungen am Ereignistyp `users.messages.pushnotification.Send`:
    * Neues `string`-Feld `push_token` hinzugefügt: Push-Token des Ereignisses

* Feldänderungen am Ereignistyp `users.messages.rcs.Click`:
    * Neues `string`-Feld `canvas_variation_name` hinzugefügt: Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
    * Feld `user_phone_number` ist jetzt *optional*.

* Feldänderungen am Ereignistyp `users.messages.rcs.InboundReceive`:
    * Feld `user_id` ist jetzt *optional*.

* Feldänderungen am Ereignistyp `users.messages.rcs.Rejection`:
    * Neues `string`-Feld `canvas_step_message_variation_id` hinzugefügt: API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat

## Änderungen in Version 3 (Veröffentlichungsdatum: 08.10.2025) {#changes-in-version-3-release-date-2025-10-08}

### Änderungen für Speicher:

* Neuer Ereignistyp `users.messages.line.Abort` hinzugefügt.

* Neuer Ereignistyp `users.messages.line.Click` hinzugefügt.

* Neuer Ereignistyp `users.messages.line.InboundReceive` hinzugefügt.

* Neuer Ereignistyp `users.messages.line.Send` hinzugefügt.

* Neuer Ereignistyp `users.messages.rcs.Abort` hinzugefügt.

* Neuer Ereignistyp `users.messages.rcs.Click` hinzugefügt.

* Neuer Ereignistyp `users.messages.rcs.Delivery` hinzugefügt.

* Neuer Ereignistyp `users.messages.rcs.InboundReceive` hinzugefügt.

* Neuer Ereignistyp `users.messages.rcs.Read` hinzugefügt.

* Neuer Ereignistyp `users.messages.rcs.Rejection` hinzugefügt.

* Neuer Ereignistyp `users.messages.rcs.Send` hinzugefügt.

* Feldänderungen am Ereignistyp `users.messages.sms.Delivery`:
    * Neues `boolean`-Feld `is_sms_fallback` hinzugefügt: Gibt an, dass eine SMS-Fallback-Nachricht aufgrund einer abgelehnten RCS-Nachricht gesendet wurde. Die Nachricht kann zu einer erfolgreichen Zustellung, einem Zustellungsfehler oder einer Ablehnung führen. Sie kann über eine Send-ID und eine Dispatch-ID mit dem RCS-Rejection-Ereignis verknüpft werden.

* Feldänderungen am Ereignistyp `users.messages.sms.DeliveryFailure`:
    * Neues `boolean`-Feld `is_sms_fallback` hinzugefügt: Gibt an, dass eine SMS-Fallback-Nachricht aufgrund einer abgelehnten RCS-Nachricht gesendet wurde. Die Nachricht kann zu einer erfolgreichen Zustellung, einem Zustellungsfehler oder einer Ablehnung führen. Sie kann über eine Send-ID und eine Dispatch-ID mit dem RCS-Rejection-Ereignis verknüpft werden.

* Feldänderungen am Ereignistyp `users.messages.sms.Rejection`:
    * Neues `boolean`-Feld `is_sms_fallback` hinzugefügt: Gibt an, dass eine SMS-Fallback-Nachricht aufgrund einer abgelehnten RCS-Nachricht gesendet wurde. Die Nachricht kann zu einer erfolgreichen Zustellung, einem Zustellungsfehler oder einer Ablehnung führen. Sie kann über eine Send-ID und eine Dispatch-ID mit dem RCS-Rejection-Ereignis verknüpft werden.

* Feldänderungen am Ereignistyp `users.messages.whatsapp.Delivery`:
    * Neues `string`-Feld `flow_id` hinzugefügt: Die eindeutige ID des Flows im WhatsApp Manager:in. Vorhanden, wenn die Nachricht einen CTA zur Beantwortung eines WhatsApp Flows enthält.
    * Neues `string`-Feld `template_name` hinzugefügt: [PII] Name des Templates im WhatsApp Manager:in. Vorhanden, wenn eine Template-Nachricht gesendet wird.
    * Neues `string`-Feld `message_id` hinzugefügt: Die von Meta generierte eindeutige ID für diese Nachricht.

* Feldänderungen am Ereignistyp `users.messages.whatsapp.Failure`:
    * Neues `string`-Feld `message_id` hinzugefügt: Die von Meta generierte eindeutige ID für diese Nachricht.
    * Neues `string`-Feld `template_name` hinzugefügt: [PII] Name des Templates im WhatsApp Manager:in. Vorhanden, wenn eine Template-Nachricht gesendet wird.
    * Neues `string`-Feld `flow_id` hinzugefügt: Die eindeutige ID des Flows im WhatsApp Manager:in. Vorhanden, wenn die Nachricht einen CTA zur Beantwortung eines WhatsApp Flows enthält.

* Feldänderungen am Ereignistyp `users.messages.whatsapp.InboundReceive`:
    * Neues `string`-Feld `catalog_id` hinzugefügt: Katalog-ID eines Produkts, falls in der eingehenden Nachricht auf ein Produkt verwiesen wird. Andernfalls leer.
    * Neues `string`-Feld `product_id` hinzugefügt: Produkt-SKU, falls in der eingehenden Nachricht auf ein Produkt verwiesen wird. Andernfalls leer.
    * Neues `string`-Feld `flow_id` hinzugefügt: Die eindeutige ID des Flows im WhatsApp Manager:in. Vorhanden, wenn die Nutzer:innen auf einen WhatsApp Flow antworten.
    * Neues `string`-Feld `flow_response_json` hinzugefügt: [PII] Die Formularwerte, mit denen die Nutzer:innen geantwortet haben. Vorhanden, wenn die Nutzer:innen auf einen WhatsApp Flow antworten.
    * Neues `string`-Feld `message_id` hinzugefügt: Die von Meta generierte eindeutige ID für diese Nachricht.
    * Neues `string`-Feld `in_reply_to` hinzugefügt: Die message_id der Nachricht, auf die diese Nachricht geantwortet hat.

* Feldänderungen am Ereignistyp `users.messages.whatsapp.Read`:
    * Neues `string`-Feld `template_name` hinzugefügt: [PII] Name des Templates im WhatsApp Manager:in. Vorhanden, wenn eine Template-Nachricht gesendet wird.
    * Neues `string`-Feld `message_id` hinzugefügt: Die von Meta generierte eindeutige ID für diese Nachricht.
    * Neues `string`-Feld `flow_id` hinzugefügt: Die eindeutige ID des Flows im WhatsApp Manager:in. Vorhanden, wenn die Nachricht einen CTA zur Beantwortung eines WhatsApp Flows enthält.

* Feldänderungen am Ereignistyp `users.messages.whatsapp.Send`:
    * Neues `string`-Feld `flow_id` hinzugefügt: Die eindeutige ID des Flows im WhatsApp Manager:in. Vorhanden, wenn die Nachricht einen CTA zur Beantwortung eines WhatsApp Flows enthält.
    * Neues `string`-Feld `template_name` hinzugefügt: [PII] Name des Templates im WhatsApp Manager:in. Vorhanden, wenn eine Template-Nachricht gesendet wird.
    * Neues `string`-Feld `message_id` hinzugefügt: Die von Meta generierte eindeutige ID für diese Nachricht.

## Änderungen in Version 2 (Veröffentlichungsdatum null) {#changes-in-version-2-release-date-null}

### Änderungen für Speicher:

* Neuer Ereignistyp `users.behaviors.app.FirstSession` hinzugefügt.

* Neuer Ereignistyp `users.behaviors.app.SessionEnd` hinzugefügt.

* Neuer Ereignistyp `users.behaviors.app.SessionStart` hinzugefügt.

* Neuer Ereignistyp `users.behaviors.CustomEvent` hinzugefügt.

* Neuer Ereignistyp `users.behaviors.InstallAttribution` hinzugefügt.

* Neuer Ereignistyp `users.behaviors.liveactivity.PushToStartTokenChange` hinzugefügt.

* Neuer Ereignistyp `users.behaviors.liveactivity.UpdateTokenChange` hinzugefügt.

* Neuer Ereignistyp `users.behaviors.Location` hinzugefügt.

* Neuer Ereignistyp `users.behaviors.Purchase` hinzugefügt.

* Neuer Ereignistyp `users.behaviors.pushnotification.TokenStateChange` hinzugefügt.

* Neuer Ereignistyp `users.behaviors.subscription.GlobalStateChange` hinzugefügt.

* Neuer Ereignistyp `users.behaviors.subscriptiongroup.StateChange` hinzugefügt.

* Neuer Ereignistyp `users.behaviors.Uninstall` hinzugefügt.

* Neuer Ereignistyp `users.campaigns.Conversion` hinzugefügt.

* Neuer Ereignistyp `users.campaigns.EnrollInControl` hinzugefügt.

* Neuer Ereignistyp `users.canvas.Conversion` hinzugefügt.

* Neuer Ereignistyp `users.canvas.Entry` hinzugefügt.

* Neuer Ereignistyp `users.canvas.exit.MatchedAudience` hinzugefügt.

* Neuer Ereignistyp `users.canvas.exit.PerformedEvent` hinzugefügt.

* Neuer Ereignistyp `users.canvas.experimentstep.Conversion` hinzugefügt.

* Neuer Ereignistyp `users.canvas.experimentstep.SplitEntry` hinzugefügt.

* Neuer Ereignistyp `users.canvasstep.Progression` hinzugefügt.

* Neuer Ereignistyp `users.messages.banner.Abort` hinzugefügt.

* Neuer Ereignistyp `users.messages.banner.Click` hinzugefügt.

* Neuer Ereignistyp `users.messages.banner.Impression` hinzugefügt.

* Neuer Ereignistyp `users.messages.contentcard.Abort` hinzugefügt.

* Neuer Ereignistyp `users.messages.contentcard.Click` hinzugefügt.

* Neuer Ereignistyp `users.messages.contentcard.Dismiss` hinzugefügt.

* Neuer Ereignistyp `users.messages.contentcard.Impression` hinzugefügt.

* Neuer Ereignistyp `users.messages.contentcard.Send` hinzugefügt.

* Neuer Ereignistyp `users.messages.email.Abort` hinzugefügt.

* Neuer Ereignistyp `users.messages.email.Bounce` hinzugefügt.

* Neuer Ereignistyp `users.messages.email.Click` hinzugefügt.

* Neuer Ereignistyp `users.messages.email.Deferral` hinzugefügt.

* Neuer Ereignistyp `users.messages.email.Delivery` hinzugefügt.

* Neuer Ereignistyp `users.messages.email.MarkAsSpam` hinzugefügt.

* Neuer Ereignistyp `users.messages.email.Open` hinzugefügt.

* Neuer Ereignistyp `users.messages.email.Send` hinzugefügt.

* Neuer Ereignistyp `users.messages.email.SoftBounce` hinzugefügt.

* Neuer Ereignistyp `users.messages.email.Unsubscribe` hinzugefügt.

* Neuer Ereignistyp `users.messages.featureflag.Impression` hinzugefügt.

* Neuer Ereignistyp `users.messages.inappmessage.Abort` hinzugefügt.

* Neuer Ereignistyp `users.messages.inappmessage.Click` hinzugefügt.

* Neuer Ereignistyp `users.messages.inappmessage.Impression` hinzugefügt.

* Neuer Ereignistyp `users.messages.liveactivity.Outcome` hinzugefügt.

* Neuer Ereignistyp `users.messages.liveactivity.Send` hinzugefügt.

* Neuer Ereignistyp `users.messages.pushnotification.Abort` hinzugefügt.

* Neuer Ereignistyp `users.messages.pushnotification.Bounce` hinzugefügt.

* Neuer Ereignistyp `users.messages.pushnotification.IosForeground` hinzugefügt.

* Neuer Ereignistyp `users.messages.pushnotification.Open` hinzugefügt.

* Neuer Ereignistyp `users.messages.pushnotification.Send` hinzugefügt.

* Neuer Ereignistyp `users.messages.sms.Abort` hinzugefügt.

* Neuer Ereignistyp `users.messages.sms.CarrierSend` hinzugefügt.

* Neuer Ereignistyp `users.messages.sms.Delivery` hinzugefügt.

* Neuer Ereignistyp `users.messages.sms.DeliveryFailure` hinzugefügt.

* Neuer Ereignistyp `users.messages.sms.InboundReceive` hinzugefügt.

* Neuer Ereignistyp `users.messages.sms.Rejection` hinzugefügt.

* Neuer Ereignistyp `users.messages.sms.Send` hinzugefügt.

* Neuer Ereignistyp `users.messages.sms.ShortLinkClick` hinzugefügt.

* Neuer Ereignistyp `users.messages.webhook.Abort` hinzugefügt.

* Neuer Ereignistyp `users.messages.webhook.Failure` hinzugefügt.

* Neuer Ereignistyp `users.messages.webhook.Send` hinzugefügt.

* Neuer Ereignistyp `users.messages.whatsapp.Abort` hinzugefügt.

* Neuer Ereignistyp `users.messages.whatsapp.Click` hinzugefügt.

* Neuer Ereignistyp `users.messages.whatsapp.Delivery` hinzugefügt.

* Neuer Ereignistyp `users.messages.whatsapp.Failure` hinzugefügt.

* Neuer Ereignistyp `users.messages.whatsapp.InboundReceive` hinzugefügt.

* Neuer Ereignistyp `users.messages.whatsapp.Read` hinzugefügt.

* Neuer Ereignistyp `users.messages.whatsapp.Send` hinzugefügt.

* Neuer Ereignistyp `users.RandomBucketNumberUpdate` hinzugefügt.