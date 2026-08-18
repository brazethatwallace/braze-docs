---
nav_title: Statut d'abonnement
article_title: Statut d'abonnement
page_order: 0
page_type: reference
description: "Découvrez comment Braze suit le statut d'abonnement pour l'e-mail, LINE, le SMS, le RCS et WhatsApp, et comment le statut conditionne la distribution des messages."

---

# Statut d'abonnement {#subscription-status}

> Découvrez comment Braze suit le statut d'abonnement sur les différents canaux de communication, comment l'état global et le statut du groupe d'abonnement interagissent, et où les règles spécifiques à chaque canal s'appliquent.

Le statut d'abonnement indique à Braze si un utilisateur est éligible pour recevoir des messages sur un canal. Ce statut peut conditionner le ciblage des Campaigns et des Canvas, les filtres de Segments, et déterminer si Braze tente la distribution.

## Fonctionnement du statut d'abonnement dans Braze {#how-subscription-status-works-in-braze}

Braze suit le statut d'abonnement à deux niveaux :

| Niveau | Ce qu'il contrôle | Canaux |
| ------ | ------------------ | ------ |
| État d'abonnement global | Si un utilisateur peut recevoir des messages sur ce canal | E-mail, notification push |
| Statut du groupe d'abonnement | Si un utilisateur est abonné à un groupe spécifique au sein d'un canal | E-mail, SMS, MMS, RCS, WhatsApp, LINE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Fonctionnement du statut d'abonnement dans Braze" }

L'état global et le statut du groupe d'abonnement fonctionnent ensemble. Pour l'e-mail, un utilisateur globalement désabonné ne recevra pas d'e-mail même s'il est abonné à un groupe d'abonnement. Pour le SMS, le RCS, WhatsApp et LINE, les utilisateurs doivent être abonnés au groupe d'abonnement correspondant pour recevoir des messages de ce groupe.

Vous pouvez consulter et mettre à jour le statut d'abonnement sur le profil d'un utilisateur dans **Engagement** > **Paramètres de contact**, via la REST API, le SDK, l'import CSV, les centres de préférences et les flux d'abonnement spécifiques à chaque canal. Braze ne comptabilise pas les changements d'état d'abonnement dans vos points de donnée.

{% alert note %}
Les groupes d'abonnement ajoutent un abonnement granulaire au sein d'un canal (par exemple, SMS promotionnel versus transactionnel). L'état global de l'e-mail et l'appartenance au groupe d'abonnement fonctionnent ensemble pour déterminer qui est joignable.
{% endalert %}

## E-mail {#email}

Braze dispose de trois états d'abonnement globaux pour l'e-mail. Ces états déterminent si les utilisateurs reçoivent les messages ciblant les audiences abonnées ou ayant explicitement accepté. Par exemple, les utilisateurs à l'état `unsubscribed` ne reçoivent pas les messages ciblant les utilisateurs `subscribed` ou `opted-in`.

| État | Définition |
| ---- | ---------- |
| Opted-in | Un utilisateur a explicitement confirmé qu'il souhaite recevoir des e-mails. Braze recommande un processus d'abonnement explicite pour obtenir le consentement des utilisateurs avant l'envoi d'e-mails. |
| Subscribed | Un utilisateur ne s'est ni désabonné ni explicitement abonné pour recevoir des e-mails. Il s'agit de l'état d'abonnement par défaut lors de la création d'un profil utilisateur. |
| Unsubscribed | Un utilisateur s'est explicitement désabonné de vos e-mails. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="États d'abonnement e-mail" }

### Comportement spécifique à l'e-mail {#email-specific-behavior}

- **Désabonnements et signalements de courrier indésirable :** Braze désabonne automatiquement les utilisateurs qui se désabonnent via un [pied de page personnalisé]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer). Si un utilisateur signale un e-mail comme courrier indésirable, Braze n'envoie que des e-mails transactionnels (messages envoyés avec **Envoyer à tous les utilisateurs, y compris les désabonnés**).
- **Échecs d'envoi définitifs :** Lorsqu'une adresse e-mail subit un échec d'envoi définitif, Braze ne définit pas automatiquement l'état d'abonnement de l'utilisateur sur `unsubscribed`. Braze marque l'adresse comme invalide et cesse les envois jusqu'à ce que l'utilisateur mette à jour son adresse e-mail.
- **Adresses e-mail partagées :** Lorsque l'état d'abonnement global d'un utilisateur change, Braze propage cet état aux autres profils partageant la même adresse e-mail, jusqu'à 100 profils par changement.
- **Mises à jour d'adresse e-mail :** Lorsqu'un utilisateur met à jour son adresse e-mail, son état d'abonnement est défini sur `subscribed`, sauf si l'adresse mise à jour existe déjà sur un autre profil, auquel cas l'utilisateur hérite de l'état de ce profil.

Pour la mise à jour de l'état d'abonnement, la vérification du statut, les centres de préférences et le ciblage des Campaigns, consultez [Abonnements e-mail]({{site.baseurl}}/user_guide/channels/email/subscriptions).

## LINE {#line}

LINE est la source de vérité pour le statut d'abonnement LINE. Même si un profil utilisateur possède un `native_line_id`, Braze ne distribuera pas de messages LINE à moins que cet utilisateur ne suive votre canal LINE.

Le statut d'abonnement LINE est suivi par `native_line_id`, et non par `external_id`. Si plusieurs profils partagent le même `native_line_id`, ils héritent du même statut d'abonnement LINE.

| État | Définition |
| ---- | ---------- |
| Subscribed | L'utilisateur a suivi votre canal LINE depuis son application LINE. |
| Unsubscribed | L'utilisateur n'a pas suivi votre canal LINE, ou s'en est explicitement désabonné. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="États d'abonnement LINE" }

### Outil de synchronisation des abonnements {#subscription-sync-tool}

Après une intégration réussie du canal LINE, Braze déploie un outil de synchronisation des abonnements pour aligner les profils Braze existants avec les données des abonnés LINE :

- Les profils avec un `native_line_id` qui suit votre canal sont mis à jour en `subscribed`.
- Les abonnés sans profil Braze correspondant obtiennent un profil anonyme avec un `native_line_id`, un alias d'utilisateur `line_id` et le statut `subscribed`.

Vous ne pouvez pas définir manuellement l'état du groupe d'abonnement LINE pendant l'intégration — LINE contrôle le statut, et Braze le synchronise.

### Mises à jour par événements de suivi et de désabonnement {#follow-and-unfollow-event-updates}

Lorsque Braze reçoit des événements webhook LINE pour votre canal intégré :

- **Suivi :** Tous les profils avec un `native_line_id` correspondant sont définis sur `subscribed`. Si aucun profil n'existe, Braze [crée un utilisateur anonyme]({{site.baseurl}}/user_guide/channels/line/message_users/user_management).
- **Désabonnement :** Tous les profils avec un `native_line_id` correspondant sont définis sur `unsubscribed`.

Pour les étapes de configuration, la réconciliation des utilisateurs et les cas d'usage, consultez [Configuration LINE]({{site.baseurl}}/user_guide/channels/line/line_setup#user-setup) et [Groupes d'abonnement LINE]({{site.baseurl}}/user_guide/channels/line/message_users/subscription_groups).

## SMS et RCS {#sms-and-rcs}

Le SMS et le RCS utilisent le statut du groupe d'abonnement, et non un état global de canal distinct. Un utilisateur peut être `subscribed` à un groupe transactionnel et `unsubscribed` d'un groupe promotionnel en même temps.

| État | Définition |
| ---- | ---------- |
| Subscribed | L'utilisateur est abonné pour recevoir des SMS et RCS d'un groupe d'abonnement spécifique, soit via l'API d'abonnement Braze, un mot-clé d'abonnement, ou une autre méthode prise en charge. Lorsque le [double abonnement]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in) est activé, les utilisateurs doivent confirmer leur abonnement avant que le statut ne passe à `Subscribed`. |
| Unsubscribed | L'utilisateur s'est désabonné de ce groupe d'abonnement en envoyant un mot-clé de désabonnement ou via l'[API d'abonnement Braze]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="États d'abonnement SMS et RCS" }

### Comportement spécifique au SMS et au RCS {#sms-and-rcs-specific-behavior}

- **Héritage du numéro de téléphone :** Lorsqu'un numéro de téléphone est ajouté ou mis à jour sur un profil, le numéro hérite du statut du groupe d'abonnement du profil ou de tout profil existant utilisant déjà ce numéro.
- **Gestion des mots-clés :** Les utilisateurs peuvent s'abonner ou se désabonner en envoyant des [mots-clés]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout) par défaut ou personnalisés. Braze met à jour automatiquement l'état d'abonnement.
- **Conformité :** Braze n'envoie jamais de SMS ou de RCS aux utilisateurs qui ne sont pas abonnés au groupe d'abonnement sélectionné.

Pour la configuration, l'envoi et la gestion des groupes d'abonnement, consultez [Groupes d'abonnement SMS, MMS et RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups).

## WhatsApp {#whatsapp}

WhatsApp utilise également le statut du groupe d'abonnement. Meta exige un [consentement d'abonnement explicite](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) avant l'envoi de messages marketing.

| État | Définition |
| ---- | ---------- |
| Subscribed | L'utilisateur a explicitement confirmé qu'il souhaite recevoir des messages WhatsApp de votre entreprise, via un flux d'abonnement ou l'API d'abonnement Braze. |
| Unsubscribed | L'utilisateur ne s'est pas abonné, ou son abonnement a été retiré. Les utilisateurs désabonnés ne reçoivent pas de messages provenant des numéros de téléphone de ce groupe d'abonnement. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="États d'abonnement WhatsApp" }

### Exigences d'abonnement {#opt-in-requirements}

Pour envoyer des messages aux utilisateurs sur WhatsApp, fournissez à Braze un `external_id`, un [numéro de téléphone]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers) et un statut d'abonnement mis à jour pour chaque utilisateur. Collectez les abonnements sur votre site web, votre application, par SMS, via des messages in-app, des fils WhatsApp entrants, ou par import CSV d'utilisateurs ayant déjà donné leur consentement ailleurs.

### Méthodes de désabonnement {#opt-out-methods}

Les utilisateurs peuvent se désabonner via :

- **Flux de mots-clés entrants :** Canvas ou Campaigns déclenchés par des mots-clés de désabonnement (par exemple, « STOP »), avec une étape de suivi qui met à jour le statut d'abonnement.
- **Réponses rapides de désabonnement marketing :** Modèles de messages avec le bouton de désabonnement marketing de Meta, associés à une étape de mise à jour du groupe d'abonnement dans votre Canvas.
- **Blocages et signalements :** Si un utilisateur bloque votre entreprise, les messages suivants ne sont pas distribués et ne sont pas facturés, mais le statut d'abonnement Braze n'est pas mis à jour. Les signalements des utilisateurs ne modifient pas non plus le statut d'abonnement.

### Bouton « Offres et annonces » de WhatsApp {#whatsapp-offers-and-announcements-toggle}

Le bouton natif **Offres et annonces** de WhatsApp est distinct des groupes d'abonnement Braze. Lorsqu'un utilisateur le désactive dans WhatsApp, Meta bloque la distribution marketing même si Braze affiche `subscribed`. Les deux couches ne se synchronisent pas automatiquement.

Pour les flux d'abonnement et de désabonnement étape par étape, consultez [Abonnements et désabonnements WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs) et [Groupes d'abonnement WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups).

## Segmenter et cibler par statut d'abonnement {#segment-and-target-by-subscription-status}

Utilisez les filtres de statut d'abonnement dans le générateur de Segments pour cibler ou exclure des audiences par canal — par exemple, les filtres **Email Subscription Status**, **Push Subscription Status** et **Subscription Group**.

Lors de la création de Campaigns et de Canvas, les options **Send Settings** et **Target Audience** vous permettent d'envoyer uniquement aux utilisateurs ayant un statut d'abonnement spécifique (comme abonné et ayant explicitement accepté). Pour les définitions des filtres e-mail et notification push, consultez [Filtres de segmentation]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).