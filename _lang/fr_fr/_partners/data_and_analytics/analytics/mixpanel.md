---
nav_title: Mixpanel
article_title: Mixpanel
alias: /partners/mixpanel/
description: "Cet article de référence présente le partenariat entre Braze et Mixpanel, une plateforme d'analyse commerciale, vous permettant d'importer des cohortes Mixpanel dans Braze afin de créer des segments Braze qui peuvent être utilisés pour cibler les utilisateurs dans de futures campagnes ou Canvas Braze."
page_type: partner
search_tag: Partner
tool: Currents

---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/mixpanel-integration-with-braze/339085/scorm/2u7y2e6qrldh2){: style="float:right;width:120px;border:0;" class="noimgborder"}Mixpanel {#braze-learning-course-imagebuster-assetsimgblicon3png-httpslearningbrazecommixpanel-integration-with-braze339085scorm2u7y2e6qrldh2-stylefloatrightwidth120pxborder0-classnoimgbordermixpanel}

> [Mixpanel](https://mixpanel.com/) est une plateforme d'analyse commerciale qui vous permet d'exporter des événements de Mixpanel vers d'autres plateformes afin d'effectuer des analyses plus approfondies. Les données collectées peuvent ensuite être utilisées pour créer des rapports personnalisés et mesurer l'engagement et la rétention des utilisateurs.

L'intégration de Braze et Mixpanel vous permet d'[importer des cohortes Mixpanel dans Braze]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/mixpanel_cohort_import/) afin de créer des segments Braze qui peuvent cibler les utilisateurs dans de futures campagnes ou Canvas Braze. Vous pouvez également tirer parti de Braze Currents pour [exporter vos événements Braze vers Mixpanel](#data-export-integration) afin d'obtenir des analyses plus approfondies sur les conversions, la rétention et l'utilisation des produits.

## Conditions préalables {#prerequisites}

| Condition | Description |
|---|---|
| Compte Mixpanel | Un [compte Mixpanel](https://mixpanel.com/) est nécessaire pour profiter de ce partenariat. |
| Currents | Pour pouvoir exporter des données vers Mixpanel, vous devez avoir configuré [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration de l'exportation des données {#data-export-integration}

Vous trouverez ci-dessous une liste complète des événements qui peuvent être exportés de Braze vers Mixpanel. Tous les événements envoyés à Mixpanel comprendront l'`external_user_id` de l'utilisateur comme ID distinct de Mixpanel. À l'heure actuelle, Braze n'envoie pas de données d'événement pour les utilisateurs dont l'`external_user_id` n'est pas défini.

Vous pouvez exporter deux types d'événements vers Mixpanel : les [événements d'engagement lié aux messages](#supported-currents-events), constitués des événements Braze directement liés à l'envoi de messages, et les [événements de comportement des clients](#supported-currents-events), comprenant d'autres activités de l'application ou du site web telles que les sessions, les événements personnalisés et les achats suivis par l'intermédiaire de la plateforme. Tous les événements personnalisés sont précédés du préfixe `[Braze Custom Event]`. Les propriétés d'événements personnalisés et les propriétés d'événements d'achat sont précédées des préfixes `[Custom event property]` et `[Purchase property]`, respectivement.

Contactez votre gestionnaire de compte ou ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support/) si vous avez besoin d'accéder à des droits d'événements supplémentaires.

### Étape 1 : Obtenir les informations d'identification de Mixpanel {#step-1-get-mixpanel-credentials}

Dans votre tableau de bord Mixpanel, cliquez sur **Project Settings** dans un projet nouveau ou existant. Vous y trouverez le secret de l'API Mixpanel et le jeton Mixpanel. Ces informations d'identification seront utilisées à l'étape suivante pour créer votre connexion Currents.

### Étape 2 : Créer un flux Braze Currents {#step-2-create-braze-current}

1. Dans Braze, accédez à **Currents** > **+ Create Current** > **Create Mixpanel Export**.
2. Indiquez le nom de l'intégration, l'e-mail du contact, le secret de l'API Mixpanel et le jeton Mixpanel dans les champs répertoriés.
3. Sélectionnez les événements que vous souhaitez suivre ; une liste des événements disponibles est fournie.
4. Cliquez sur **Launch Current**.

![La page Braze Mixpanel Currents. Cette page comprend des champs pour spécifier le nom de l'intégration, l'e-mail du contact, le secret de l'API et le jeton d'exportation Mixpanel. La moitié inférieure de la page Currents répertorie les événements Currents disponibles que vous pouvez envoyer.]({% image_buster /assets/img_archive/mixpanel4.png %}){: style="max-width:80%;"}

{% tab note %}
Consultez la [documentation sur l'intégration](https://help.mixpanel.com/hc/en-us/articles/360001243663) de Mixpanel pour en savoir plus.
{% endtab %}

## Événements Currents pris en charge {#supported-currents-events}

Braze prend en charge l'exportation vers Mixpanel des données suivantes répertoriées dans les glossaires des événements de [comportement des utilisateurs]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) et d'[engagement lié aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) :

### Comportements {#behaviors}
- Événement personnalisé : `users.behaviors.CustomEvent`
- Attribution d'installation : `users.behaviors.InstallAttribution`
- Emplacement : `users.behaviors.Location`
- Achat : `users.behaviors.Purchase`
- Désinstallation : `users.behaviors.Uninstall`
- Application (première session, fin de session, début de session)
  - `users.behaviors.app.FirstSession`
  - `users.behaviors.app.SessionEnd`
  - `users.behaviors.app.SessionStart`
- Abonnement (changement d'état global) : `users.behaviors.subscription.GlobalStateChange`
- Groupe d'abonnement (changement d'état) : `users.behaviors.subscriptiongroup.StateChange`

### Campaigns
- Abandon : `users_campaigns_abort`
- Conversion : `users.campaigns.Conversion`
- EnrollinControl : `users.campaigns.EnrollInControl`

### Canvas
- Abandon : `users_canvas_abort`
- Conversion : `users.canvas.Conversion`
- Entrée : `users.canvas.Entry`
- Sortie (audience correspondante, événement réalisé)
  - `users.canvas.exit.MatchedAudience`
  - `users.canvas.exit.PerformedEvent`
- Étape d'expérience (conversion, entrée fractionnée)
  - `users.canvas.experimentstep.Conversion`
  - `users.canvas.experimentstep.SplitEntry`

### Messages
- Carte de contenu (abandon, clic, fermeture, impression, envoi)
  - `users.messages.contentcard.Abort`
  - `users.messages.contentcard.Click`
  - `users.messages.contentcard.Dismiss`
  - `users.messages.contentcard.Impression`
  - `users.messages.contentcard.Send`
- E-mail (abandon, rebond, clic, distribution, marquage comme spam, ouverture, envoi, rejet temporaire, désinscription)
  - `users.messages.email.Abort`
  - `users.messages.email.Bounce`
  - `users.messages.email.Click`
  - `users.messages.email.Delivery`
  - `users.messages.email.MarkAsSpam`
  - `users.messages.email.Open`
  - `users.messages.email.Send`
  - `users.messages.email.SoftBounce`
  - `users.messages.email.Unsubscribe`
- Message in-app (abandon, clic, impression)
  - `users.messages.inappmessage.Abort`
  - `users.messages.inappmessage.Click`
  - `users.messages.inappmessage.Impression`
- Notification push (abandon, rebond, iOSforeground, ouverture, envoi)
  - `users.messages.pushnotification.Abort`
  - `users.messages.pushnotification.Bounce`
  - `users.messages.pushnotification.IosForeground`
  - `users.messages.pushnotification.Open`
  - `users.messages.pushnotification.Send`
- SMS (abandon, envoi par l'opérateur, distribution, échec de distribution, réception entrante, rejet, envoi, clic sur un lien court)
  - `users.messages.sms.Abort`
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.InboundReceive`
  - `users.messages.sms.Rejection`
  - `users.messages.sms.Send`
  - `users.messages.sms.ShortLinkClick`
- Webhook (abandon, envoi)
  - `users.messages.webhook.Abort`
  - `users.messages.webhook.Send`
- WhatsApp (abandon, distribution, échec, réception entrante, lecture, envoi)
  - `users.messages.whatsapp.Abort`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.InboundReceive`
  - `users.messages.whatsapp.Read`
  - `users.messages.whatsapp.Send`

## Résolution des problèmes {#troubleshooting}

### Vérifier la clé API Mixpanel et l'ID externe Braze {#verify-mixpanel-api-key-and-braze-external-id}

Confirmez que votre clé API Mixpanel et les valeurs `braze_external_id` correspondent à ce que vous attendez dans Braze et Mixpanel. L'API de synchronisation des cohortes partage des groupes d'utilisateurs entre les produits, et la synchronisation ne fonctionnera pas correctement si l'`external_id` dans Braze et l'identifiant envoyé par Mixpanel ne correspondent pas. Les synchronisations de cohortes depuis Mixpanel s'exécutent selon le calendrier de Mixpanel — par exemple, une fois ou environ toutes les deux heures — laissez donc du temps entre les vérifications.

### Vérifier l'état de l'implémentation {#check-implementation-status}

Confirmez que `braze_external_id` est implémenté dans Mixpanel.

### Définir la propriété utilisateur directement {#set-the-user-property-directly}

Pour réduire toute ambiguïté, définissez `braze_external_id` directement dans Mixpanel.

### Définition automatique de la propriété (SDK) {#automatic-property-setting-sdks}

Le SDK Mixpanel peut définir `braze_external_id` automatiquement lorsque le SDK Braze est intégré dans la même application. Si vous implémentez Mixpanel et Braze ensemble, vous n'avez généralement pas besoin de configuration supplémentaire au-delà de l'installation des deux SDK.

{% alert note %}
`braze_external_id` n'est pas défini lorsque `changeUser()` est appelé dans Braze ; il est défini lorsque Mixpanel s'initialise ou démarre une session (lors de l'« init » ou du « start session »).
{% endalert %}