---
nav_title: Groupes d'abonnement
article_title: Endpoints des groupes d'abonnement
page_order: 7
layout: dev_guide

#Required
description: "Cette page explique et répertorie les endpoints des groupes d'abonnement Braze pour les e-mails et les SMS."
page_type: landing
search_tag: Endpoint

guide_top_header: "Endpoints des groupes d'abonnement"
guide_top_text: "Utilisez les API REST des groupes d'abonnement pour gérer de manière programmatique les groupes d'abonnement que vous avez stockés dans le tableau de bord de Braze, sur la page <strong>Groupe d'abonnement</strong>. Ceci s'applique aux groupes d'abonnement SMS et e-mail.<br><br> Vous recherchez des conseils sur la création de groupes d'abonnement ? Consultez nos articles sur les <a href='/docs/user_guide/message_building_by_channel/sms/sms_subscription_group/'>groupes d'abonnement SMS</a> et les <a href='/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/'>groupes d'abonnement e-mail</a>."

guide_featured_title: ""
guide_featured_list:
  - name: "GET : Répertorier le statut du groupe d'abonnement d'un utilisateur"
    link: /docs/api/endpoints/subscription_groups/get_list_user_subscription_group_status
    image: /assets/img/braze_icons/users-01.svg
  - name: "GET : Répertorier les groupes d'abonnement d'un utilisateur"
    link: /docs/api/endpoints/subscription_groups/get_list_user_subscription_groups
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST : Mettre à jour le statut du groupe d'abonnement d'un utilisateur"
    link: /docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status
    image: /assets/img/braze_icons/user-plus-01.svg
  - name: "POST : Mettre à jour le statut du groupe d'abonnement d'un utilisateur V2"
    link: /docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2
    image: /assets/img/braze_icons/user-edit.svg
---
<br>
<br>


## Comprendre les séries temporelles des groupes d'abonnement {#understand-subscription-group-timeseries}

Sur la page **Groupe d'abonnement**, les graphiques de séries temporelles indiquent :

- **Taille du groupe d'abonnement :** nombre d'utilisateurs abonnés à ce groupe à une date donnée
- **Taille des désabonnés du groupe d'abonnement :** nombre d'utilisateurs désabonnés de ce groupe à une date donnée

Pour en savoir plus sur le tableau de bord, consultez [Afficher la taille des groupes d'abonnement]({{site.baseurl}}/user_guide/channels/email/subscriptions#viewing-subscription-group-sizes).

Ces indicateurs sont propres à chaque groupe. Ils peuvent différer du filtre de segment `Email Subscription Status is Unsubscribed`, qui reflète l'état d'abonnement global aux e-mails plutôt qu'un seul groupe d'abonnement. Pour les espaces de travail très volumineux, Braze peut afficher des estimations lorsque les comptages exacts ne sont pas disponibles.

## Éviter les doublons d'utilisateurs à partir des formulaires de capture d'e-mail {#avoid-duplicate-users-from-email-capture-forms}

Avant de créer un utilisateur à partir d'un formulaire de capture d'e-mail, appelez [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) pour vérifier si le profil existe déjà. Si la réponse est « User not found », créez l'utilisateur avec [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status). Sinon, mettez à jour le profil existant au lieu de créer un doublon.

## Événements Snowflake `USERS_MESSAGES_EMAIL_UNSUBSCRIBE` {#snowflake-users_messages_email_unsubscribe-events}

La table Snowflake `USERS_MESSAGES_EMAIL_UNSUBSCRIBE` enregistre les désabonnements e-mail au niveau du message provenant du côté du destinataire : clic sur un lien de désabonnement, List-Unsubscribe en un clic du client de messagerie, soumissions via le centre de préférences et désabonnements signalés par l'ESP. Les désabonnements effectués via la REST API ne sont pas inclus dans cette table ; ceux-ci émettent des événements [`users.behaviors.subscriptiongroup.StateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#subscription-group-state-change-events) ou [`users.behaviors.subscription.GlobalStateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#global-subscription-state-change-events) à la place.

## Messages de test SMS et groupes d'abonnement {#sms-test-messages-and-subscription-groups}

Pour recevoir un message de test SMS, le destinataire doit appartenir au groupe d'abonnement SMS que vous sélectionnez lors de l'envoi du test.