---
nav_title: Journal des modifications des événements Currents
page_order: 6
description: "Cette page présente les modifications apportées aux événements pour chaque version de Currents."
tool: Currents
---

# Journal des modifications de Currents {#currents-changelog}

## Modifications de la version 11 (date de publication : 05/08/2026) {#changes-in-version-11-release-date-2026-08-05}

### Modifications relatives au stockage : {#changes-for-storage}

* Ajout d'un nouveau type d'événement `contentoptimizer.ComponentStore`.

* Ajout d'un nouveau type d'événement `users.canvas.costep.Conversion`.

* Ajout d'un nouveau type d'événement `users.messages.landingpage.Click`.

* Ajout d'un nouveau type d'événement `users.messages.landingpage.FormSubmission`.

* Ajout d'un nouveau type d'événement `users.messages.landingpage.Impression`.

* Ajout d'un nouveau type d'événement `users.messages.survey.Response`.

* Modifications de champs pour le type d'événement `agentconsole.AgentExecuted` :
    * Ajout d'un nouveau champ `string` `thinking_level` : le niveau de réflexion ou de raisonnement utilisé pour la requête

* Modifications de champs pour le type d'événement `users.messages.banner.Click` :
    * Ajout d'un nouveau champ `boolean` `is_unique` : indique s'il s'agissait du premier clic de l'utilisateur sur la variante du message, comptabilisé dans les statistiques de clics uniques

* Modifications de champs pour le type d'événement `users.messages.banner.Dismiss` :
    * Ajout d'un nouveau champ `boolean` `is_unique` : indique s'il s'agissait du premier rejet du message par l'utilisateur pour cette variante, comptabilisé dans les statistiques de rejets uniques

* Modifications de champs pour le type d'événement `users.messages.banner.Impression` :
    * Ajout d'un nouveau champ `boolean` `is_unique` : indique s'il s'agissait de la première impression de l'utilisateur pour cette variante du message, comptabilisée dans les statistiques d'impressions uniques

* Modifications de champs pour le type d'événement `users.messages.contentcard.Click` :
    * Ajout d'un nouveau champ `boolean` `is_unique` : indique s'il s'agissait du premier clic de l'utilisateur sur la variante du message, comptabilisé dans les statistiques de clics uniques

* Modifications de champs pour le type d'événement `users.messages.contentcard.Dismiss` :
    * Ajout d'un nouveau champ `boolean` `is_unique` : indique s'il s'agissait du premier rejet du message par l'utilisateur pour cette variante, comptabilisé dans les statistiques de rejets uniques

* Modifications de champs pour le type d'événement `users.messages.contentcard.Impression` :
    * Ajout d'un nouveau champ `boolean` `is_unique` : indique s'il s'agissait de la première impression de l'utilisateur pour cette variante du message, comptabilisée dans les statistiques d'impressions uniques

* Modifications de champs pour le type d'événement `users.messages.featureflag.Impression` :
    * Ajout d'un nouveau champ `boolean` `is_unique` : indique s'il s'agissait de la première impression de l'utilisateur pour ce feature flag, comptabilisée dans les statistiques d'impressions uniques

## Modifications de la version 10 (date de publication : 01/07/2026) {#changes-in-version-10-release-date-2026-07-01}

### Modifications relatives au stockage :

* Ajout d'un nouveau type d'événement `users.canvas.costep.Send`.

* Ajout d'un nouveau type d'événement `users.UserDeleteRequest`.

* Ajout d'un nouveau type d'événement `users.UserOrphan`.

* Modifications de champs pour le type d'événement `users.messages.rcs.Abort` :
    * Ajout d'un nouveau champ `string` `canvas_id` : ID API du Canvas auquel cet événement appartient

* Modifications de champs pour le type d'événement `users.messages.rcs.Click` :
    * Ajout d'un nouveau champ `string` `canvas_id` : ID API du Canvas auquel cet événement appartient

* Modifications de champs pour le type d'événement `users.messages.rcs.Delivery` :
    * Ajout d'un nouveau champ `string` `canvas_id` : ID API du Canvas auquel cet événement appartient

* Modifications de champs pour le type d'événement `users.messages.rcs.InboundReceive` :
    * Ajout d'un nouveau champ `string` `canvas_id` : ID API du Canvas auquel cet événement appartient

* Modifications de champs pour le type d'événement `users.messages.rcs.Read` :
    * Ajout d'un nouveau champ `string` `canvas_id` : ID API du Canvas auquel cet événement appartient

* Modifications de champs pour le type d'événement `users.messages.rcs.Rejection` :
    * Ajout d'un nouveau champ `string` `canvas_id` : ID API du Canvas auquel cet événement appartient

* Modifications de champs pour le type d'événement `users.messages.rcs.Send` :
    * Ajout d'un nouveau champ `string` `canvas_id` : ID API du Canvas auquel cet événement appartient

## Modifications de la version 9 (date de publication : 03/06/2026) {#changes-in-version-9-release-date-2026-06-03}

### Modifications relatives au stockage :

* Modifications de champs pour le type d'événement `users.messages.email.Send` :
    * Ajout d'un nouveau champ `string` `from_domain` : domaine d'envoi de l'e-mail

## Modifications de la version 8 (date de publication : 06/05/2026) {#changes-in-version-8-release-date-2026-05-06}

### Modifications relatives au stockage :

* Ajout d'un nouveau type d'événement `users.messages.banner.Dismiss`.

* Modifications de champs pour le type d'événement `users.messages.whatsapp.Abort` :
    * Ajout d'un nouveau champ `string` `bsuid` : ID utilisateur WhatsApp Business-Scoped du destinataire associé à cet événement.

* Modifications de champs pour le type d'événement `users.messages.whatsapp.Delivery` :
    * Ajout d'un nouveau champ `string` `bsuid` : ID utilisateur WhatsApp Business-Scoped du destinataire associé à cet événement.

* Modifications de champs pour le type d'événement `users.messages.whatsapp.Failure` :
    * Ajout d'un nouveau champ `string` `bsuid` : ID utilisateur WhatsApp Business-Scoped du destinataire associé à cet événement.

* Modifications de champs pour le type d'événement `users.messages.whatsapp.InboundReceive` :
    * Ajout d'un nouveau champ `string` `bsuid` : ID utilisateur WhatsApp Business-Scoped de l'utilisateur ayant envoyé le message.
    * Le champ `user_phone_number` est désormais *facultatif*.

* Modifications de champs pour le type d'événement `users.messages.whatsapp.Read` :
    * Ajout d'un nouveau champ `string` `bsuid` : ID utilisateur WhatsApp Business-Scoped du destinataire associé à cet événement.

* Modifications de champs pour le type d'événement `users.messages.whatsapp.Retry` :
    * Ajout d'un nouveau champ `string` `bsuid` : ID utilisateur WhatsApp Business-Scoped du destinataire associé à cet événement.

* Modifications de champs pour le type d'événement `users.messages.whatsapp.Send` :
    * Ajout d'un nouveau champ `string` `bsuid` : ID utilisateur WhatsApp Business-Scoped du destinataire associé à cet événement.

## Modifications de la version 7 (date de publication : 01/04/2026) {#changes-in-version-7-release-date-2026-04-01}

### Modifications relatives au stockage :

* Ajout d'un nouveau type d'événement `users.profile.Update`.

* Modifications de champs pour le type d'événement `users.messages.banner.Abort` :
    * Ajout d'un nouveau champ `string` `canvas_name` : nom du Canvas
    * Ajout d'un nouveau champ `string` `canvas_step_name` : nom de l'étape du Canvas
    * Ajout d'un nouveau champ `string` `canvas_variation_name` : nom de la variante du Canvas reçue par cet utilisateur
    * Ajout d'un nouveau champ `string` `canvas_id` : ID API du Canvas auquel cet événement appartient
    * Ajout d'un nouveau champ `string` `canvas_step_id` : ID API de l'étape du Canvas à laquelle cet événement appartient
    * Ajout d'un nouveau champ `string` `canvas_step_message_variation_id` : ID API de la variante de message de l'étape du Canvas reçue par cet utilisateur
    * Ajout d'un nouveau champ `string` `canvas_variation_id` : ID API de la variante du Canvas à laquelle cet événement appartient

* Modifications de champs pour le type d'événement `users.messages.banner.Click` :
    * Ajout d'un nouveau champ `string` `canvas_id` : ID API du Canvas auquel cet événement appartient
    * Ajout d'un nouveau champ `string` `canvas_step_id` : ID API de l'étape du Canvas à laquelle cet événement appartient
    * Ajout d'un nouveau champ `string` `canvas_name` : nom du Canvas
    * Ajout d'un nouveau champ `string` `canvas_step_name` : nom de l'étape du Canvas
    * Ajout d'un nouveau champ `string` `canvas_step_message_variation_id` : ID API de la variante de message de l'étape du Canvas reçue par cet utilisateur
    * Ajout d'un nouveau champ `string` `canvas_variation_id` : ID API de la variante du Canvas à laquelle cet événement appartient
    * Ajout d'un nouveau champ `string` `canvas_variation_name` : nom de la variante du Canvas reçue par cet utilisateur

* Modifications de champs pour le type d'événement `users.messages.banner.Impression` :
    * Ajout d'un nouveau champ `string` `canvas_id` : ID API du Canvas auquel cet événement appartient
    * Ajout d'un nouveau champ `string` `canvas_step_id` : ID API de l'étape du Canvas à laquelle cet événement appartient
    * Ajout d'un nouveau champ `string` `canvas_name` : nom du Canvas
    * Ajout d'un nouveau champ `string` `canvas_step_name` : nom de l'étape du Canvas
    * Ajout d'un nouveau champ `string` `canvas_step_message_variation_id` : ID API de la variante de message de l'étape du Canvas reçue par cet utilisateur
    * Ajout d'un nouveau champ `string` `canvas_variation_id` : ID API de la variante du Canvas à laquelle cet événement appartient
    * Ajout d'un nouveau champ `string` `canvas_variation_name` : nom de la variante du Canvas reçue par cet utilisateur

## Modifications de la version 6 (date de publication : 04/03/2026) {#changes-in-version-6-release-date-2026-03-04}

### Modifications relatives au stockage :

* Modifications de champs pour le type d'événement `agentconsole.AgentExecuted` :
    * Ajout d'un nouveau champ `string` `error` : description de l'erreur

* Modifications de champs pour le type d'événement `agentconsole.ToolInvocation` :
    * Ajout d'un nouveau champ `string` `request_id` : ID unique pour cette requête LLM globale et son exécution complète

* Modifications de champs pour le type d'événement `users.messages.rcs.InboundReceive` :
    * Ajout d'un nouveau champ `string` `canvas_variation_name` : nom de la variante du Canvas reçue par cet utilisateur

## Modifications de la version 5 (date de publication : 04/02/2026) {#changes-in-version-5-release-date-2026-02-04}

### Modifications relatives au stockage :

* Ajout d'un nouveau type d'événement `agentconsole.AgentExecuted`.

* Ajout d'un nouveau type d'événement `agentconsole.ToolInvocation`.

* Ajout d'un nouveau type d'événement `users.messages.email.Retry`.

* Ajout d'un nouveau type d'événement `users.messages.line.Retry`.

* Ajout d'un nouveau type d'événement `users.messages.pushnotification.Retry`.

* Ajout d'un nouveau type d'événement `users.messages.sms.Retry`.

* Ajout d'un nouveau type d'événement `users.messages.webhook.Retry`.

* Ajout d'un nouveau type d'événement `users.messages.whatsapp.Retry`.

* Modifications de champs pour le type d'événement `users.behaviors.pushnotification.TokenStateChange` :
    * Ajout d'un nouveau champ `long` `time_ms` : horodatage en millisecondes de l'événement

## Modifications de la version 4 (date de publication : 07/01/2026) {#changes-in-version-4-release-date-2026-01-07}

### Modifications relatives au stockage :

* Modifications de champs pour le type d'événement `users.behaviors.pushnotification.TokenStateChange` :
    * Ajout d'un nouveau champ `string` `push_token` : jeton de notification push de l'événement

* Modifications de champs pour le type d'événement `users.messages.pushnotification.Bounce` :
    * Ajout d'un nouveau champ `string` `push_token` : jeton de notification push de l'événement

* Modifications de champs pour le type d'événement `users.messages.pushnotification.Send` :
    * Ajout d'un nouveau champ `string` `push_token` : jeton de notification push de l'événement

* Modifications de champs pour le type d'événement `users.messages.rcs.Click` :
    * Ajout d'un nouveau champ `string` `canvas_variation_name` : nom de la variante du Canvas reçue par cet utilisateur
    * Le champ `user_phone_number` est désormais *facultatif*.

* Modifications de champs pour le type d'événement `users.messages.rcs.InboundReceive` :
    * Le champ `user_id` est désormais *facultatif*.

* Modifications de champs pour le type d'événement `users.messages.rcs.Rejection` :
    * Ajout d'un nouveau champ `string` `canvas_step_message_variation_id` : ID API de la variante de message de l'étape du Canvas reçue par cet utilisateur

## Modifications de la version 3 (date de publication : 08/10/2025) {#changes-in-version-3-release-date-2025-10-08}

### Modifications relatives au stockage :

* Ajout d'un nouveau type d'événement `users.messages.line.Abort`.

* Ajout d'un nouveau type d'événement `users.messages.line.Click`.

* Ajout d'un nouveau type d'événement `users.messages.line.InboundReceive`.

* Ajout d'un nouveau type d'événement `users.messages.line.Send`.

* Ajout d'un nouveau type d'événement `users.messages.rcs.Abort`.

* Ajout d'un nouveau type d'événement `users.messages.rcs.Click`.

* Ajout d'un nouveau type d'événement `users.messages.rcs.Delivery`.

* Ajout d'un nouveau type d'événement `users.messages.rcs.InboundReceive`.

* Ajout d'un nouveau type d'événement `users.messages.rcs.Read`.

* Ajout d'un nouveau type d'événement `users.messages.rcs.Rejection`.

* Ajout d'un nouveau type d'événement `users.messages.rcs.Send`.

* Modifications de champs pour le type d'événement `users.messages.sms.Delivery` :
    * Ajout d'un nouveau champ `boolean` `is_sms_fallback` : indique qu'un SMS de secours a été envoyé suite au rejet d'un message RCS. Ce message peut aboutir à une distribution réussie, à un échec de distribution ou à un rejet. Il peut être associé à l'événement de rejet RCS via un ID d'envoi et un ID d'expédition.

* Modifications de champs pour le type d'événement `users.messages.sms.DeliveryFailure` :
    * Ajout d'un nouveau champ `boolean` `is_sms_fallback` : indique qu'un SMS de secours a été envoyé suite au rejet d'un message RCS. Ce message peut aboutir à une distribution réussie, à un échec de distribution ou à un rejet. Il peut être associé à l'événement de rejet RCS via un ID d'envoi et un ID d'expédition.

* Modifications de champs pour le type d'événement `users.messages.sms.Rejection` :
    * Ajout d'un nouveau champ `boolean` `is_sms_fallback` : indique qu'un SMS de secours a été envoyé suite au rejet d'un message RCS. Ce message peut aboutir à une distribution réussie, à un échec de distribution ou à un rejet. Il peut être associé à l'événement de rejet RCS via un ID d'envoi et un ID d'expédition.

* Modifications de champs pour le type d'événement `users.messages.whatsapp.Delivery` :
    * Ajout d'un nouveau champ `string` `flow_id` : ID unique du Flow dans le gestionnaire WhatsApp. Présent si le message comprend un CTA pour répondre à un Flow WhatsApp.
    * Ajout d'un nouveau champ `string` `template_name` : [PII] Nom du modèle dans le gestionnaire WhatsApp. Présent lors de l'envoi d'un message modèle.
    * Ajout d'un nouveau champ `string` `message_id` : ID unique généré par Meta pour ce message

* Modifications de champs pour le type d'événement `users.messages.whatsapp.Failure` :
    * Ajout d'un nouveau champ `string` `message_id` : ID unique généré par Meta pour ce message
    * Ajout d'un nouveau champ `string` `template_name` : [PII] Nom du modèle dans le gestionnaire WhatsApp. Présent lors de l'envoi d'un message modèle.
    * Ajout d'un nouveau champ `string` `flow_id` : ID unique du Flow dans le gestionnaire WhatsApp. Présent si le message comprend un CTA pour répondre à un Flow WhatsApp.

* Modifications de champs pour le type d'événement `users.messages.whatsapp.InboundReceive` :
    * Ajout d'un nouveau champ `string` `catalog_id` : ID du catalogue d'un produit si celui-ci est mentionné dans le message entrant. Sinon, vide.
    * Ajout d'un nouveau champ `string` `product_id` : SKU du produit si celui-ci est mentionné dans le message entrant. Sinon, vide.
    * Ajout d'un nouveau champ `string` `flow_id` : ID unique du Flow dans le gestionnaire WhatsApp. Présent si l'utilisateur répond à un Flow WhatsApp.
    * Ajout d'un nouveau champ `string` `flow_response_json` : [PII] Valeurs du formulaire fournies par l'utilisateur. Présent si l'utilisateur répond à un Flow WhatsApp.
    * Ajout d'un nouveau champ `string` `message_id` : ID unique généré par Meta pour ce message
    * Ajout d'un nouveau champ `string` `in_reply_to` : le `message_id` du message auquel ce message répondait

* Modifications de champs pour le type d'événement `users.messages.whatsapp.Read` :
    * Ajout d'un nouveau champ `string` `template_name` : [PII] Nom du modèle dans le gestionnaire WhatsApp. Présent lors de l'envoi d'un message modèle.
    * Ajout d'un nouveau champ `string` `message_id` : ID unique généré par Meta pour ce message
    * Ajout d'un nouveau champ `string` `flow_id` : ID unique du Flow dans le gestionnaire WhatsApp. Présent si le message comprend un CTA pour répondre à un Flow WhatsApp.

* Modifications de champs pour le type d'événement `users.messages.whatsapp.Send` :
    * Ajout d'un nouveau champ `string` `flow_id` : ID unique du Flow dans le gestionnaire WhatsApp. Présent si le message comprend un CTA pour répondre à un Flow WhatsApp.
    * Ajout d'un nouveau champ `string` `template_name` : [PII] Nom du modèle dans le gestionnaire WhatsApp. Présent lors de l'envoi d'un message modèle.
    * Ajout d'un nouveau champ `string` `message_id` : ID unique généré par Meta pour ce message

## Modifications de la version 2 (date de publication non disponible) {#changes-in-version-2-release-date-null}

### Modifications relatives au stockage :

* Ajout d'un nouveau type d'événement `users.behaviors.app.FirstSession`.

* Ajout d'un nouveau type d'événement `users.behaviors.app.SessionEnd`.

* Ajout d'un nouveau type d'événement `users.behaviors.app.SessionStart`.

* Ajout d'un nouveau type d'événement `users.behaviors.CustomEvent`.

* Ajout d'un nouveau type d'événement `users.behaviors.InstallAttribution`.

* Ajout d'un nouveau type d'événement `users.behaviors.liveactivity.PushToStartTokenChange`.

* Ajout d'un nouveau type d'événement `users.behaviors.liveactivity.UpdateTokenChange`.

* Ajout d'un nouveau type d'événement `users.behaviors.Location`.

* Ajout d'un nouveau type d'événement `users.behaviors.Purchase`.

* Ajout d'un nouveau type d'événement `users.behaviors.pushnotification.TokenStateChange`.

* Ajout d'un nouveau type d'événement `users.behaviors.subscription.GlobalStateChange`.

* Ajout d'un nouveau type d'événement `users.behaviors.subscriptiongroup.StateChange`.

* Ajout d'un nouveau type d'événement `users.behaviors.Uninstall`.

* Ajout d'un nouveau type d'événement `users.campaigns.Conversion`.

* Ajout d'un nouveau type d'événement `users.campaigns.EnrollInControl`.

* Ajout d'un nouveau type d'événement `users.canvas.Conversion`.

* Ajout d'un nouveau type d'événement `users.canvas.Entry`.

* Ajout d'un nouveau type d'événement `users.canvas.exit.MatchedAudience`.

* Ajout d'un nouveau type d'événement `users.canvas.exit.PerformedEvent`.

* Ajout d'un nouveau type d'événement `users.canvas.experimentstep.Conversion`.

* Ajout d'un nouveau type d'événement `users.canvas.experimentstep.SplitEntry`.

* Ajout d'un nouveau type d'événement `users.canvasstep.Progression`.

* Ajout d'un nouveau type d'événement `users.messages.banner.Abort`.

* Ajout d'un nouveau type d'événement `users.messages.banner.Click`.

* Ajout d'un nouveau type d'événement `users.messages.banner.Impression`.

* Ajout d'un nouveau type d'événement `users.messages.contentcard.Abort`.

* Ajout d'un nouveau type d'événement `users.messages.contentcard.Click`.

* Ajout d'un nouveau type d'événement `users.messages.contentcard.Dismiss`.

* Ajout d'un nouveau type d'événement `users.messages.contentcard.Impression`.

* Ajout d'un nouveau type d'événement `users.messages.contentcard.Send`.

* Ajout d'un nouveau type d'événement `users.messages.email.Abort`.

* Ajout d'un nouveau type d'événement `users.messages.email.Bounce`.

* Ajout d'un nouveau type d'événement `users.messages.email.Click`.

* Ajout d'un nouveau type d'événement `users.messages.email.Deferral`.

* Ajout d'un nouveau type d'événement `users.messages.email.Delivery`.

* Ajout d'un nouveau type d'événement `users.messages.email.MarkAsSpam`.

* Ajout d'un nouveau type d'événement `users.messages.email.Open`.

* Ajout d'un nouveau type d'événement `users.messages.email.Send`.

* Ajout d'un nouveau type d'événement `users.messages.email.SoftBounce`.

* Ajout d'un nouveau type d'événement `users.messages.email.Unsubscribe`.

* Ajout d'un nouveau type d'événement `users.messages.featureflag.Impression`.

* Ajout d'un nouveau type d'événement `users.messages.inappmessage.Abort`.

* Ajout d'un nouveau type d'événement `users.messages.inappmessage.Click`.

* Ajout d'un nouveau type d'événement `users.messages.inappmessage.Impression`.

* Ajout d'un nouveau type d'événement `users.messages.liveactivity.Outcome`.

* Ajout d'un nouveau type d'événement `users.messages.liveactivity.Send`.

* Ajout d'un nouveau type d'événement `users.messages.pushnotification.Abort`.

* Ajout d'un nouveau type d'événement `users.messages.pushnotification.Bounce`.

* Ajout d'un nouveau type d'événement `users.messages.pushnotification.IosForeground`.

* Ajout d'un nouveau type d'événement `users.messages.pushnotification.Open`.

* Ajout d'un nouveau type d'événement `users.messages.pushnotification.Send`.

* Ajout d'un nouveau type d'événement `users.messages.sms.Abort`.

* Ajout d'un nouveau type d'événement `users.messages.sms.CarrierSend`.

* Ajout d'un nouveau type d'événement `users.messages.sms.Delivery`.

* Ajout d'un nouveau type d'événement `users.messages.sms.DeliveryFailure`.

* Ajout d'un nouveau type d'événement `users.messages.sms.InboundReceive`.

* Ajout d'un nouveau type d'événement `users.messages.sms.Rejection`.

* Ajout d'un nouveau type d'événement `users.messages.sms.Send`.

* Ajout d'un nouveau type d'événement `users.messages.sms.ShortLinkClick`.

* Ajout d'un nouveau type d'événement `users.messages.webhook.Abort`.

* Ajout d'un nouveau type d'événement `users.messages.webhook.Failure`.

* Ajout d'un nouveau type d'événement `users.messages.webhook.Send`.

* Ajout d'un nouveau type d'événement `users.messages.whatsapp.Abort`.

* Ajout d'un nouveau type d'événement `users.messages.whatsapp.Click`.

* Ajout d'un nouveau type d'événement `users.messages.whatsapp.Delivery`.

* Ajout d'un nouveau type d'événement `users.messages.whatsapp.Failure`.

* Ajout d'un nouveau type d'événement `users.messages.whatsapp.InboundReceive`.

* Ajout d'un nouveau type d'événement `users.messages.whatsapp.Read`.

* Ajout d'un nouveau type d'événement `users.messages.whatsapp.Send`.

* Ajout d'un nouveau type d'événement `users.RandomBucketNumberUpdate`.