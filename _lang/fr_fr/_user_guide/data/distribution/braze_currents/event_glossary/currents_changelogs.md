---
nav_title: Journal des modifications des événements Currents
page_order: 6
description: "Cette page présente les modifications apportées aux événements pour chaque version de Currents."
tool: Currents
---

# Journal des modifications de Currents {#currents-changelog}

## Modifications de la version 12 (date de publication : 02/09/2026) {#changes-in-version-12-release-date-2026-09-02}

### Modifications pour le stockage : {#changes-for-storage}

* Modifications de champs pour le type d'événement `users.messages.email.Abort` :
    * Ajout d'un nouveau champ `string` `message_extras` : [PII] Chaîne JSON des paires clé-valeur étiquetées lors du rendu Liquid

* Modifications de champs pour le type d'événement `users.messages.email.Bounce` :
    * Ajout d'un nouveau champ `int` `send_time` : Heure de l'événement d'envoi correspondant

* Modifications de champs pour le type d'événement `users.messages.email.Click` :
    * Ajout d'un nouveau champ `int` `send_time` : Heure en secondes de l'événement d'envoi correspondant
    * Ajout d'un nouveau champ `boolean` `has_url_parameters` : Indique si l'URL cliquée contenait des paramètres de requête
    * Ajout d'un nouveau champ `boolean` `link_aliasing_enabled` : Indique si l'aliasage de lien or aliasing de lien était activé pour l'espace de travail lors du traitement de ce clic

* Modifications de champs pour le type d'événement `users.messages.email.Deferral` :
    * Ajout d'un nouveau champ `int` `send_time` : Heure de l'événement d'envoi correspondant

* Modifications de champs pour le type d'événement `users.messages.email.Delivery` :
    * Ajout d'un nouveau champ `int` `send_time` : Heure de l'événement d'envoi correspondant

* Modifications de champs pour le type d'événement `users.messages.email.MarkAsSpam` :
    * Ajout d'un nouveau champ `int` `send_time` : Heure de l'événement d'envoi correspondant

* Modifications de champs pour le type d'événement `users.messages.email.Open` :
    * Ajout d'un nouveau champ `int` `send_time` : Heure de l'événement d'envoi correspondant

* Modifications de champs pour le type d'événement `users.messages.email.SoftBounce` :
    * Ajout d'un nouveau champ `int` `send_time` : Heure de l'événement d'envoi correspondant

* Modifications de champs pour le type d'événement `users.messages.line.Abort` :
    * Ajout d'un nouveau champ `string` `message_extras` : [PII] Chaîne JSON des paires clé-valeur étiquetées lors du rendu Liquid

* Modifications de champs pour le type d'événement `users.messages.pushnotification.Abort` :
    * Ajout d'un nouveau champ `string` `message_extras` : [PII] Chaîne JSON des paires clé-valeur étiquetées lors du rendu Liquid

* Modifications de champs pour le type d'événement `users.messages.rcs.Abort` :
    * Ajout d'un nouveau champ `string` `message_extras` : [PII] Chaîne JSON des paires clé-valeur étiquetées lors du rendu Liquid

* Modifications de champs pour le type d'événement `users.messages.sms.Abort` :
    * Ajout d'un nouveau champ `string` `message_extras` : [PII] Chaîne JSON des paires clé-valeur étiquetées lors du rendu Liquid

* Modifications de champs pour le type d'événement `users.messages.webhook.Abort` :
    * Ajout d'un nouveau champ `string` `message_extras` : [PII] Chaîne JSON des paires clé-valeur étiquetées lors du rendu Liquid

* Modifications de champs pour le type d'événement `users.messages.whatsapp.Abort` :
    * Ajout d'un nouveau champ `string` `message_extras` : [PII] Chaîne JSON des paires clé-valeur étiquetées lors du rendu Liquid

## Modifications de la version 11 (date de publication : 05/08/2026) {#changes-in-version-11-release-date-2026-08-05}

### Modifications pour le stockage :

* Ajout du nouveau type d'événement `contentoptimizer.ComponentStore`.

* Ajout du nouveau type d'événement `users.canvas.costep.Conversion`.

* Ajout du nouveau type d'événement `users.messages.landingpage.Click`.

* Ajout du nouveau type d'événement `users.messages.landingpage.FormSubmission`.

* Ajout du nouveau type d'événement `users.messages.landingpage.Impression`.

* Ajout du nouveau type d'événement `users.messages.survey.Response`.

* Modifications de champs pour le type d'événement `agentconsole.AgentExecuted` :
    * Ajout du nouveau champ `string` `thinking_level` : le niveau de réflexion/raisonnement utilisé pour la requête

* Modifications de champs pour le type d'événement `users.messages.banner.Click` :
    * Ajout du nouveau champ `boolean` `is_unique` : indique s'il s'agissait du premier clic de l'utilisateur sur la variante du message, comptabilisé dans les statistiques de clics uniques

* Modifications de champs pour le type d'événement `users.messages.banner.Dismiss` :
    * Ajout du nouveau champ `boolean` `is_unique` : indique s'il s'agissait du premier rejet de la variante du message par l'utilisateur, comptabilisé dans les statistiques de rejets uniques

* Modifications de champs pour le type d'événement `users.messages.banner.Impression` :
    * Ajout du nouveau champ `boolean` `is_unique` : indique s'il s'agissait de la première impression de la variante du message pour l'utilisateur, comptabilisée dans les statistiques d'impressions uniques

* Modifications de champs pour le type d'événement `users.messages.contentcard.Click` :
    * Ajout du nouveau champ `boolean` `is_unique` : indique s'il s'agissait du premier clic de l'utilisateur sur la variante du message, comptabilisé dans les statistiques de clics uniques

* Modifications de champs pour le type d'événement `users.messages.contentcard.Dismiss` :
    * Ajout du nouveau champ `boolean` `is_unique` : indique s'il s'agissait du premier rejet de la variante du message par l'utilisateur, comptabilisé dans les statistiques de rejets uniques

* Modifications de champs pour le type d'événement `users.messages.contentcard.Impression` :
    * Ajout du nouveau champ `boolean` `is_unique` : indique s'il s'agissait de la première impression de la variante du message pour l'utilisateur, comptabilisée dans les statistiques d'impressions uniques

* Modifications de champs pour le type d'événement `users.messages.featureflag.Impression` :
    * Ajout du nouveau champ `boolean` `is_unique` : indique s'il s'agissait de la première impression de ce feature flag pour l'utilisateur, comptabilisée dans les statistiques d'impressions uniques

## Modifications dans la version 10 (date de publication : 01/07/2026) {#changes-in-version-10-release-date-2026-07-01}

### Modifications pour le stockage :

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

## Modifications dans la version 9 (date de publication : 03/06/2026) {#changes-in-version-9-release-date-2026-06-03}

### Modifications pour le stockage :

* Modifications de champs pour le type d'événement `users.messages.email.Send` :
    * Ajout d'un nouveau champ `string` `from_domain` : Domaine d'envoi de l'e-mail

## Modifications dans la version 8 (date de publication : 06/05/2026) {#changes-in-version-8-release-date-2026-05-06}

### Modifications pour le stockage :

* Ajout du nouveau type d'événement `users.messages.banner.Dismiss`.

* Modifications des champs pour le type d'événement `users.messages.whatsapp.Abort` :
    * Ajout du nouveau champ `string` `bsuid` : L'identifiant utilisateur WhatsApp Business-Scoped du destinataire associé à cet événement.

* Modifications des champs pour le type d'événement `users.messages.whatsapp.Delivery` :
    * Ajout du nouveau champ `string` `bsuid` : L'identifiant utilisateur WhatsApp Business-Scoped du destinataire associé à cet événement.

* Modifications des champs pour le type d'événement `users.messages.whatsapp.Failure` :
    * Ajout du nouveau champ `string` `bsuid` : L'identifiant utilisateur WhatsApp Business-Scoped du destinataire associé à cet événement.

* Modifications des champs pour le type d'événement `users.messages.whatsapp.InboundReceive` :
    * Ajout du nouveau champ `string` `bsuid` : L'identifiant utilisateur WhatsApp Business-Scoped de l'utilisateur à partir duquel le message a été reçu.
    * Le champ `user_phone_number` est désormais *facultatif*.

* Modifications des champs pour le type d'événement `users.messages.whatsapp.Read` :
    * Ajout du nouveau champ `string` `bsuid` : L'identifiant utilisateur WhatsApp Business-Scoped du destinataire associé à cet événement.

* Modifications des champs pour le type d'événement `users.messages.whatsapp.Retry` :
    * Ajout du nouveau champ `string` `bsuid` : L'identifiant utilisateur WhatsApp Business-Scoped du destinataire associé à cet événement.

* Modifications des champs pour le type d'événement `users.messages.whatsapp.Send` :
    * Ajout du nouveau champ `string` `bsuid` : L'identifiant utilisateur WhatsApp Business-Scoped du destinataire associé à cet événement.

## Modifications de la version 7 (date de publication : 01/04/2026) {#changes-in-version-7-release-date-2026-04-01}

### Modifications pour le stockage :

* Ajout d'un nouveau type d'événement `users.profile.Update`.

* Modifications de champs pour le type d'événement `users.messages.banner.Abort` :
    * Ajout d'un nouveau champ `string` `canvas_name` : nom du Canvas
    * Ajout d'un nouveau champ `string` `canvas_step_name` : nom de l'étape du Canvas
    * Ajout d'un nouveau champ `string` `canvas_variation_name` : nom de la variation du Canvas reçue par cet utilisateur
    * Ajout d'un nouveau champ `string` `canvas_id` : ID API du Canvas auquel cet événement appartient
    * Ajout d'un nouveau champ `string` `canvas_step_id` : ID API de l'étape du Canvas à laquelle cet événement appartient
    * Ajout d'un nouveau champ `string` `canvas_step_message_variation_id` : ID API de la variation de message de l'étape du Canvas reçue par cet utilisateur
    * Ajout d'un nouveau champ `string` `canvas_variation_id` : ID API de la variation du Canvas à laquelle cet événement appartient

* Modifications de champs pour le type d'événement `users.messages.banner.Click` :
    * Ajout d'un nouveau champ `string` `canvas_id` : ID API du Canvas auquel cet événement appartient
    * Ajout d'un nouveau champ `string` `canvas_step_id` : ID API de l'étape du Canvas à laquelle cet événement appartient
    * Ajout d'un nouveau champ `string` `canvas_name` : nom du Canvas
    * Ajout d'un nouveau champ `string` `canvas_step_name` : nom de l'étape du Canvas
    * Ajout d'un nouveau champ `string` `canvas_step_message_variation_id` : ID API de la variation de message de l'étape du Canvas reçue par cet utilisateur
    * Ajout d'un nouveau champ `string` `canvas_variation_id` : ID API de la variation du Canvas à laquelle cet événement appartient
    * Ajout d'un nouveau champ `string` `canvas_variation_name` : nom de la variation du Canvas reçue par cet utilisateur

* Modifications de champs pour le type d'événement `users.messages.banner.Impression` :
    * Ajout d'un nouveau champ `string` `canvas_id` : ID API du Canvas auquel cet événement appartient
    * Ajout d'un nouveau champ `string` `canvas_step_id` : ID API de l'étape du Canvas à laquelle cet événement appartient
    * Ajout d'un nouveau champ `string` `canvas_name` : nom du Canvas
    * Ajout d'un nouveau champ `string` `canvas_step_name` : nom de l'étape du Canvas
    * Ajout d'un nouveau champ `string` `canvas_step_message_variation_id` : ID API de la variation de message de l'étape du Canvas reçue par cet utilisateur
    * Ajout d'un nouveau champ `string` `canvas_variation_id` : ID API de la variation du Canvas à laquelle cet événement appartient
    * Ajout d'un nouveau champ `string` `canvas_variation_name` : nom de la variation du Canvas reçue par cet utilisateur

## Changements dans la version 6 (date de publication : 04/03/2026) {#changes-in-version-6-release-date-2026-03-04}

### Changements pour Storage :

* Modifications de champs pour le type d'événement `agentconsole.AgentExecuted` :
    * Ajout d'un nouveau champ `string` `error` : Description de l'erreur

* Modifications de champs pour le type d'événement `agentconsole.ToolInvocation` :
    * Ajout d'un nouveau champ `string` `request_id` : ID unique pour cette requête LLM globale et l'exécution complète

* Modifications de champs pour le type d'événement `users.messages.rcs.InboundReceive` :
    * Ajout d'un nouveau champ `string` `canvas_variation_name` : Nom de la variation Canvas reçue par cet utilisateur

## Modifications dans la version 5 (date de publication : 2026-02-04) {#changes-in-version-5-release-date-2026-02-04}

### Modifications pour Storage :

* Ajout du nouveau type d'événement `agentconsole.AgentExecuted`.

* Ajout du nouveau type d'événement `agentconsole.ToolInvocation`.

* Ajout du nouveau type d'événement `users.messages.email.Retry`.

* Ajout du nouveau type d'événement `users.messages.line.Retry`.

* Ajout du nouveau type d'événement `users.messages.pushnotification.Retry`.

* Ajout du nouveau type d'événement `users.messages.sms.Retry`.

* Ajout du nouveau type d'événement `users.messages.webhook.Retry`.

* Ajout du nouveau type d'événement `users.messages.whatsapp.Retry`.

* Modifications des champs pour le type d'événement `users.behaviors.pushnotification.TokenStateChange` :
    * Ajout du nouveau champ `long` `time_ms` : Heure en millisecondes à laquelle l'événement s'est produit

## Modifications dans la version 4 (date de publication : 07/01/2026) {#changes-in-version-4-release-date-2026-01-07}

### Modifications pour le stockage :

* Modifications des champs pour le type d'événement `users.behaviors.pushnotification.TokenStateChange` :
    * Ajout d'un nouveau champ `string` `push_token` : jeton de notification push de l'événement

* Modifications des champs pour le type d'événement `users.messages.pushnotification.Bounce` :
    * Ajout d'un nouveau champ `string` `push_token` : jeton de notification push de l'événement

* Modifications des champs pour le type d'événement `users.messages.pushnotification.Send` :
    * Ajout d'un nouveau champ `string` `push_token` : jeton de notification push de l'événement

* Modifications des champs pour le type d'événement `users.messages.rcs.Click` :
    * Ajout d'un nouveau champ `string` `canvas_variation_name` : nom de la variation Canvas reçue par cet utilisateur
    * Le champ `user_phone_number` est désormais *facultatif*.

* Modifications des champs pour le type d'événement `users.messages.rcs.InboundReceive` :
    * Le champ `user_id` est désormais *facultatif*.

* Modifications des champs pour le type d'événement `users.messages.rcs.Rejection` :
    * Ajout d'un nouveau champ `string` `canvas_step_message_variation_id` : ID API de la variation de message de l'étape Canvas reçue par cet utilisateur

## Modifications dans la version 3 (date de publication : 2025-10-08) {#changes-in-version-3-release-date-2025-10-08}

### Modifications pour Storage :

* Ajout du nouveau type d'événement `users.messages.line.Abort`.

* Ajout du nouveau type d'événement `users.messages.line.Click`.

* Ajout du nouveau type d'événement `users.messages.line.InboundReceive`.

* Ajout du nouveau type d'événement `users.messages.line.Send`.

* Ajout du nouveau type d'événement `users.messages.rcs.Abort`.

* Ajout du nouveau type d'événement `users.messages.rcs.Click`.

* Ajout du nouveau type d'événement `users.messages.rcs.Delivery`.

* Ajout du nouveau type d'événement `users.messages.rcs.InboundReceive`.

* Ajout du nouveau type d'événement `users.messages.rcs.Read`.

* Ajout du nouveau type d'événement `users.messages.rcs.Rejection`.

* Ajout du nouveau type d'événement `users.messages.rcs.Send`.

* Modifications de champs pour le type d'événement `users.messages.sms.Delivery` :
    * Ajout du nouveau champ `boolean` `is_sms_fallback` : Indique qu'un message SMS de repli a été envoyé en raison d'un message RCS rejeté. Le message peut aboutir à une réception, un échec de réception ou un rejet. Il peut être associé à l'événement de rejet RCS via un ID d'envoi et un ID de distribution.

* Modifications de champs pour le type d'événement `users.messages.sms.DeliveryFailure` :
    * Ajout du nouveau champ `boolean` `is_sms_fallback` : Indique qu'un message SMS de repli a été envoyé en raison d'un message RCS rejeté. Le message peut aboutir à une réception, un échec de réception ou un rejet. Il peut être associé à l'événement de rejet RCS via un ID d'envoi et un ID de distribution.

* Modifications de champs pour le type d'événement `users.messages.sms.Rejection` :
    * Ajout du nouveau champ `boolean` `is_sms_fallback` : Indique qu'un message SMS de repli a été envoyé en raison d'un message RCS rejeté. Le message peut aboutir à une réception, un échec de réception ou un rejet. Il peut être associé à l'événement de rejet RCS via un ID d'envoi et un ID de distribution.

* Modifications de champs pour le type d'événement `users.messages.whatsapp.Delivery` :
    * Ajout du nouveau champ `string` `flow_id` : L'ID unique du Flow dans le WhatsApp gestionnaire. Présent si le message inclut un CTA pour répondre à un WhatsApp Flow.
    * Ajout du nouveau champ `string` `template_name` : [PII] Nom du modèle dans le WhatsApp gestionnaire. Présent si un message de modèle est envoyé.
    * Ajout du nouveau champ `string` `message_id` : L'ID unique généré par Meta pour ce message.

* Modifications de champs pour le type d'événement `users.messages.whatsapp.Failure` :
    * Ajout du nouveau champ `string` `message_id` : L'ID unique généré par Meta pour ce message.
    * Ajout du nouveau champ `string` `template_name` : [PII] Nom du modèle dans le WhatsApp gestionnaire. Présent si un message de modèle est envoyé.
    * Ajout du nouveau champ `string` `flow_id` : L'ID unique du Flow dans le WhatsApp gestionnaire. Présent si le message inclut un CTA pour répondre à un WhatsApp Flow.

* Modifications de champs pour le type d'événement `users.messages.whatsapp.InboundReceive` :
    * Ajout du nouveau champ `string` `catalog_id` : ID du catalogue d'un produit si un produit est référencé dans le message entrant. Sinon, vide.
    * Ajout du nouveau champ `string` `product_id` : Unité de gestion des stocks du produit si un produit est référencé dans le message entrant. Sinon, vide.
    * Ajout du nouveau champ `string` `flow_id` : L'ID unique du Flow dans le WhatsApp gestionnaire. Présent si l'utilisateur répond à un WhatsApp Flow.
    * Ajout du nouveau champ `string` `flow_response_json` : [PII] Les valeurs de formulaire avec lesquelles l'utilisateur a répondu. Présent si l'utilisateur répond à un WhatsApp Flow.
    * Ajout du nouveau champ `string` `message_id` : L'ID unique généré par Meta pour ce message.
    * Ajout du nouveau champ `string` `in_reply_to` : Le message_id du message auquel ce message répondait.

* Modifications de champs pour le type d'événement `users.messages.whatsapp.Read` :
    * Ajout du nouveau champ `string` `template_name` : [PII] Nom du modèle dans le WhatsApp gestionnaire. Présent si un message de modèle est envoyé.
    * Ajout du nouveau champ `string` `message_id` : L'ID unique généré par Meta pour ce message.
    * Ajout du nouveau champ `string` `flow_id` : L'ID unique du Flow dans le WhatsApp gestionnaire. Présent si le message inclut un CTA pour répondre à un WhatsApp Flow.

* Modifications de champs pour le type d'événement `users.messages.whatsapp.Send` :
    * Ajout du nouveau champ `string` `flow_id` : L'ID unique du Flow dans le WhatsApp gestionnaire. Présent si le message inclut un CTA pour répondre à un WhatsApp Flow.
    * Ajout du nouveau champ `string` `template_name` : [PII] Nom du modèle dans le WhatsApp gestionnaire. Présent si un message de modèle est envoyé.
    * Ajout du nouveau champ `string` `message_id` : L'ID unique généré par Meta pour ce message.

## Modifications dans la version 2 (date de publication nulle) {#changes-in-version-2-release-date-null}

### Modifications pour Storage :

* Ajout du nouveau type d'événement `users.behaviors.app.FirstSession`.

* Ajout du nouveau type d'événement `users.behaviors.app.SessionEnd`.

* Ajout du nouveau type d'événement `users.behaviors.app.SessionStart`.

* Ajout du nouveau type d'événement `users.behaviors.CustomEvent`.

* Ajout du nouveau type d'événement `users.behaviors.InstallAttribution`.

* Ajout du nouveau type d'événement `users.behaviors.liveactivity.PushToStartTokenChange`.

* Ajout du nouveau type d'événement `users.behaviors.liveactivity.UpdateTokenChange`.

* Ajout du nouveau type d'événement `users.behaviors.Location`.

* Ajout du nouveau type d'événement `users.behaviors.Purchase`.

* Ajout du nouveau type d'événement `users.behaviors.pushnotification.TokenStateChange`.

* Ajout du nouveau type d'événement `users.behaviors.subscription.GlobalStateChange`.

* Ajout du nouveau type d'événement `users.behaviors.subscriptiongroup.StateChange`.

* Ajout du nouveau type d'événement `users.behaviors.Uninstall`.

* Ajout du nouveau type d'événement `users.campaigns.Conversion`.

* Ajout du nouveau type d'événement `users.campaigns.EnrollInControl`.

* Ajout du nouveau type d'événement `users.canvas.Conversion`.

* Ajout du nouveau type d'événement `users.canvas.Entry`.

* Ajout du nouveau type d'événement `users.canvas.exit.MatchedAudience`.

* Ajout du nouveau type d'événement `users.canvas.exit.PerformedEvent`.

* Ajout du nouveau type d'événement `users.canvas.experimentstep.Conversion`.

* Ajout du nouveau type d'événement `users.canvas.experimentstep.SplitEntry`.

* Ajout du nouveau type d'événement `users.canvasstep.Progression`.

* Ajout du nouveau type d'événement `users.messages.banner.Abort`.

* Ajout du nouveau type d'événement `users.messages.banner.Click`.

* Ajout du nouveau type d'événement `users.messages.banner.Impression`.

* Ajout du nouveau type d'événement `users.messages.contentcard.Abort`.

* Ajout du nouveau type d'événement `users.messages.contentcard.Click`.

* Ajout du nouveau type d'événement `users.messages.contentcard.Dismiss`.

* Ajout du nouveau type d'événement `users.messages.contentcard.Impression`.

* Ajout du nouveau type d'événement `users.messages.contentcard.Send`.

* Ajout du nouveau type d'événement `users.messages.email.Abort`.

* Ajout du nouveau type d'événement `users.messages.email.Bounce`.

* Ajout du nouveau type d'événement `users.messages.email.Click`.

* Ajout du nouveau type d'événement `users.messages.email.Deferral`.

* Ajout du nouveau type d'événement `users.messages.email.Delivery`.

* Ajout du nouveau type d'événement `users.messages.email.MarkAsSpam`.

* Ajout du nouveau type d'événement `users.messages.email.Open`.

* Ajout du nouveau type d'événement `users.messages.email.Send`.

* Ajout du nouveau type d'événement `users.messages.email.SoftBounce`.

* Ajout du nouveau type d'événement `users.messages.email.Unsubscribe`.

* Ajout du nouveau type d'événement `users.messages.featureflag.Impression`.

* Ajout du nouveau type d'événement `users.messages.inappmessage.Abort`.

* Ajout du nouveau type d'événement `users.messages.inappmessage.Click`.

* Ajout du nouveau type d'événement `users.messages.inappmessage.Impression`.

* Ajout du nouveau type d'événement `users.messages.liveactivity.Outcome`.

* Ajout du nouveau type d'événement `users.messages.liveactivity.Send`.

* Ajout du nouveau type d'événement `users.messages.pushnotification.Abort`.

* Ajout du nouveau type d'événement `users.messages.pushnotification.Bounce`.

* Ajout du nouveau type d'événement `users.messages.pushnotification.IosForeground`.

* Ajout du nouveau type d'événement `users.messages.pushnotification.Open`.

* Ajout du nouveau type d'événement `users.messages.pushnotification.Send`.

* Ajout du nouveau type d'événement `users.messages.sms.Abort`.

* Ajout du nouveau type d'événement `users.messages.sms.CarrierSend`.

* Ajout du nouveau type d'événement `users.messages.sms.Delivery`.

* Ajout du nouveau type d'événement `users.messages.sms.DeliveryFailure`.

* Ajout du nouveau type d'événement `users.messages.sms.InboundReceive`.

* Ajout du nouveau type d'événement `users.messages.sms.Rejection`.

* Ajout du nouveau type d'événement `users.messages.sms.Send`.

* Ajout du nouveau type d'événement `users.messages.sms.ShortLinkClick`.

* Ajout du nouveau type d'événement `users.messages.webhook.Abort`.

* Ajout du nouveau type d'événement `users.messages.webhook.Failure`.

* Ajout du nouveau type d'événement `users.messages.webhook.Send`.

* Ajout du nouveau type d'événement `users.messages.whatsapp.Abort`.

* Ajout du nouveau type d'événement `users.messages.whatsapp.Click`.

* Ajout du nouveau type d'événement `users.messages.whatsapp.Delivery`.

* Ajout du nouveau type d'événement `users.messages.whatsapp.Failure`.

* Ajout du nouveau type d'événement `users.messages.whatsapp.InboundReceive`.

* Ajout du nouveau type d'événement `users.messages.whatsapp.Read`.

* Ajout du nouveau type d'événement `users.messages.whatsapp.Send`.

* Ajout du nouveau type d'événement `users.RandomBucketNumberUpdate`.