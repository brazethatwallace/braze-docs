---
nav_title: FAQ
article_title: FAQ
page_order: 30
description: "Cet article répond à certaines des questions les plus fréquemment posées lors de la configuration de campagnes push."
page_type: FAQ
channel:
  - Push
---

# Questions fréquemment posées {#frequently-asked-questions}

> Cet article fournit des réponses à certaines questions fréquemment posées sur le canal push.

## Pourquoi les notifications push sont-elles parfois retardées ? {#why-are-push-notifications-sometimes-delayed}

La distribution suit généralement trois étapes : le **traitement** par Braze (segmentation, planification et transmission au fournisseur), le transport de Braze vers **APNs ou FCM**, et la distribution du fournisseur vers l'**appareil**. Des retards peuvent survenir à chaque étape. Braze n'a pas de visibilité sur les files d'attente du fournisseur ou de l'appareil ; utilisez la [journalisation détaillée]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs) côté client lorsque vous devez identifier précisément les délais côté appareil.

## Que se passe-t-il lorsque plusieurs utilisateurs se connectent sur un même appareil ? {#what-happens-when-multiple-users-log-into-a-single-device}

Lorsqu'un utilisateur se déconnecte d'un appareil ou d'un site web, il reste joignable par push jusqu'à ce qu'un autre utilisateur se connecte. À ce moment-là, le jeton de notification push est réattribué au nouvel utilisateur. En effet, chaque appareil ne peut avoir qu'un seul abonnement push actif par application ou site web.

Lorsqu'un jeton de notification push est réattribué, la modification est reflétée dans le **Push Changelog** du profil utilisateur. Sur le profil utilisateur, accédez à l'onglet **Engagement**.

![Le « Push Changelog » dans la section « Contact Settings ».]({% image_buster /assets/img/push_changelog_faq.png %}){: style="max-width:50%;"}

## Lorsque j'envoie un push de test, est-il envoyé à tous mes appareils ? {#when-i-send-a-test-push-does-it-go-to-all-of-my-devices}

Oui. Le push de test est envoyé à chaque appareil compatible push associé au profil utilisateur sélectionné. Si vous avez plusieurs téléphones ou tablettes connectés avec le même utilisateur, chaque appareil disposant d'un jeton de notification push valide reçoit la notification.

Pour envoyer le push de test à un seul appareil, vous pouvez supprimer les jetons de notification push des autres appareils depuis le profil utilisateur avant le test. Sinon, si vous envoyez via l'[endpoint `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages), définissez `send_to_most_recent_device_only` sur `true` dans l'objet `apple_push` ou `android_push` afin que seul l'appareil le plus récemment actif reçoive le push.

## Que signifie « Error sending push because the payload was invalid » ? {#what-does-error-sending-push-because-the-payload-was-invalid-mean}

Ce message indique qu'APNs a rejeté la requête push en raison d'un payload invalide (par exemple, un payload vide ou un payload trop volumineux).

Pour plus de détails et les étapes suivantes, consultez [Messages d'erreur push courants]({{site.baseurl}}/user_guide/channels/push/push_error_codes).

## Pourquoi un utilisateur ayant accepté les notifications n'a-t-il pas de jeton de notification push ? {#why-doesnt-an-opted-in-user-have-a-push-token}

Cela peut se produire si le jeton de notification push de l'utilisateur a été réattribué à une autre personne ayant utilisé le même appareil.

1. Accédez au **Push Changelog** dans l'onglet **Engagement** du profil de l'utilisateur concerné.
2. Recherchez un message indiquant que le jeton de notification push a été transféré à un autre utilisateur.
3. Copiez le jeton de notification push et collez-le dans la barre de recherche d'utilisateurs.
4. Si le jeton de notification push existe toujours, vous serez redirigé vers l'utilisateur qui s'est connecté le plus récemment sur l'appareil.

Si vous souhaitez que le jeton de notification push soit réattribué à l'utilisateur d'origine :

1. Demandez à l'utilisateur d'origine de se connecter au profil avec le jeton de notification push manquant.
2. Déclenchez un nouvel envoi push. Cela transférera le jeton vers le compte si l'utilisateur a toujours les notifications push activées au niveau de l'appareil.

## Pourquoi « Open web URL inside mobile app » ouvre-t-il toujours l'application lorsque je teste un brouillon de Campaign ? {#why-does-open-web-url-inside-mobile-app-always-open-the-app-when-im-testing-a-draft-campaign}

Lorsqu'une Campaign est encore au statut **Draft** et que vous envoyez un push de test, appuyer sur la notification ouvre toujours l'application en premier, que l'option **Open web URL inside mobile app** soit sélectionnée ou non. Lorsque la Campaign est **Live**, le comportement au clic fonctionne comme configuré.

Si vous avez sélectionné **Open web URL** sans l'option **Inside App**, le lien s'ouvre directement dans le navigateur par défaut de l'appareil. Si vous avez sélectionné **Open web URL inside mobile app**, le lien s'ouvre dans une vue web in-app.

## Quelle est la différence entre « Send to Production » et « Send to Development » pour les certificats push iOS ? {#what-is-the-difference-between-send-to-production-and-send-to-development-for-ios-push-certificates}

Lors de l'ajout d'un certificat Apple Push dans Braze, les options **Send to Production** et **Send to Development** déterminent quelle passerelle APNs (Apple Push Notification service) Braze utilise pour envoyer les notifications push :

- **Send to Development :** Sélectionnez cette option si l'application a été compilée en mode développement dans Xcode et signée avec un profil de provisionnement de développement. Les notifications push sont acheminées via la passerelle de développement (sandbox) d'Apple.
- **Send to Production :** Sélectionnez cette option si l'application est distribuée via TestFlight d'Apple, l'App Store ou la distribution d'entreprise. Les notifications push sont acheminées via la passerelle de production d'Apple.

Si la mauvaise option est sélectionnée, les notifications push échouent silencieusement car le type de jeton de notification push ne correspond pas à la passerelle. En règle générale, les applications distribuées via TestFlight ou l'App Store doivent utiliser **Send to Production**.

## Quelle est la différence entre les filtres « Foreground Push Enabled » et « Background or Foreground Push Enabled » ? {#what-is-the-difference-between-the-foreground-push-enabled-and-background-or-foreground-push-enabled-filters}

Ces filtres de segmentation vérifient des conditions différentes :

| Filtre | Ce qu'il vérifie | Cas d'utilisation |
|--------|-----------------|-------------------|
| **Foreground Push Enabled** | L'utilisateur dispose d'un jeton de notification push de premier plan valide **et** son état d'abonnement push est `Opted-In` ou `Subscribed`. | Cibler les utilisateurs qui peuvent recevoir des notifications push visibles. |
| **Background or Foreground Push Enabled** | L'utilisateur dispose d'un jeton de notification push (premier plan ou arrière-plan) **et** son état d'abonnement push est `Opted-In` ou `Subscribed`. Cela inclut les utilisateurs qui ont désactivé les notifications push visibles mais qui disposent toujours d'un jeton de notification push en arrière-plan. | Utilisé pour le [suivi des désinstallations]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking), les [notifications push silencieuses]({{site.baseurl}}/developer_guide/push_notifications/silent) et le géorepérage. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Quelle est la différence entre les filtres « Foreground Push Enabled » et « Background or Foreground Push Enabled » ?" }

Un utilisateur peut être `Background or Foreground Push Enabled` sans être `Foreground Push Enabled`. Cela se produit lorsque l'utilisateur a désactivé les notifications push visibles dans les paramètres de son appareil, mais que l'application détient toujours un jeton de notification push en arrière-plan. Pour plus de détails, consultez [Utilisateurs push et abonnements]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#foreground-push-enabled).

## Comment Braze détermine-t-il qu'un message push a été envoyé avec succès ? {#how-does-braze-determine-when-a-push-message-is-sent-successfully}

Un message est enregistré comme envoyé dès qu'il est reçu par le fournisseur de service push. Cela ne signifie pas nécessairement que l'utilisateur a reçu ou consulté le message.

Pour iOS, le fournisseur de service push est Apple Push Notification Service (APNs), et pour Android, il s'agit généralement de Firebase Cloud Messaging (FCM). Le fournisseur de service push répond immédiatement avec un succès ou un échec. Un échec peut inclure un rebond ou une nouvelle tentative en cas de défaillance réseau.

Si un message de succès est renvoyé, l'envoi est enregistré par Braze, puis le service push tente de distribuer le message à l'appareil. Si l'appareil ne peut pas être atteint immédiatement, le service effectue de nouvelles tentatives jusqu'à l'expiration de l'option définie dans Braze (**TTL** pour Android, **Expiry** pour iOS). Si le message expire, le service push supprime la notification push, mais celle-ci n'est pas considérée comme un rebond.

- Pour les Campaigns push à livraison par événement, l'envoi du message est enregistré dès que l'utilisateur a effectué l'action qui déclenche la Campaign.
- Pour les Campaigns planifiées, l'heure d'envoi correspond au moment où le message a été mis en file d'attente et transmis au fournisseur de service push.
- Pour les deux types de livraison, le message est marqué comme « envoyé » dans Braze et dans le profil utilisateur sous **Campaigns Received**, même si l'utilisateur n'a pas encore vu ou reçu la notification push.

L'indicateur « distributions » pour les notifications push dans le tableau de bord est calculé au chargement de la page comme le nombre d'envois moins les rebonds.