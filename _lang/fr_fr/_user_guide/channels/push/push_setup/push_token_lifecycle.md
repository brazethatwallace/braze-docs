---
nav_title: "Cycle de vie des jetons de notification push"
article_title: "Cycle de vie des jetons de notification push"
page_order: 1
page_type: reference
description: "Cet article de référence explique ce que signifie être enregistré pour les notifications push et comment Braze envoie des messages push et gère les jetons de notification push et l'enregistrement push."
channel:
 - push

---

# Cycle de vie des jetons de notification push {#push-token-lifecycle}

> Cet article couvre le processus par lequel un utilisateur se voit attribuer un jeton de notification push, et comment Braze envoie des messages push à vos utilisateurs.

## À propos des jetons de notification push {#push-tokens}

Lorsqu'une application demande les autorisations push à un appareil, le fournisseur de service push de l'appareil génère un jeton de notification push pour cette application. Chaque application reçoit son propre jeton de notification push unique et anonyme, qui permet d'identifier l'appareil et l'instance actuelle de l'application lors de l'envoi d'une notification push.

Gardez à l'esprit que les jetons de notification push ne sont pas des identifiants statiques qui durent indéfiniment&#8212;ils peuvent être mis à jour et ils peuvent [expirer](#push-token-expire).

{% alert tip %}
Pour des détails spécifiques à chaque plateforme, consultez [Enregistrement des jetons de notification push](#push-token-registration).
{% endalert %}

### Push au premier plan et en arrière-plan {#foreground-vs-background}

Les jetons de notification push sont utilisés pour envoyer des notifications push au premier plan et en arrière-plan.

| Type | Nécessite un opt-in ? | Description |
|------------------|------------------|--------------------------------------------------------------------------------------------------------------|
| Push au premier plan | Oui | Une notification est affichée de manière visible à l'utilisateur lorsque l'application est au premier plan. |
| Push en arrière-plan | Non | Une notification est délivrée silencieusement en arrière-plan sans être affichée. Souvent utilisée pour des fonctionnalités comme le suivi des désinstallations. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Push au premier plan et en arrière-plan" }

Lorsqu'un utilisateur accepte les notifications push pour votre application, il est considéré comme « enregistré pour le push », ce qui signifie qu'il peut désormais être ciblé à l'aide du filtre de segmentation `Foreground Push Enabled for App` dans Braze.

{% alert note %}
Ceci est différent du filtre de segmentation `Foreground Push Enabled`, qui est utilisé pour identifier les utilisateurs ayant accepté les notifications push pour au moins une de vos applications, et non une application spécifique. Pour plus d'informations, consultez [Filtres de segmentation]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#foreground-push-enabled).
{% endalert %}

### Plusieurs utilisateurs sur un même appareil {#multiple-users-on-a-device}

Les jetons de notification push sont uniques à la fois pour l'appareil et l'application, ce qui signifie qu'ils ne peuvent pas être utilisés pour cibler un utilisateur spécifique si plusieurs utilisateurs partagent le même appareil.

Par exemple, supposons que vous ayez deux utilisateurs : Charlie et Kim. Si Charlie a activé les notifications push pour votre application sur son téléphone et que Kim utilise le téléphone de Charlie pour se déconnecter du profil de Charlie et se connecter au sien, le jeton de notification push sera réattribué au profil de Kim. Le jeton de notification push restera alors attribué au profil de Kim sur cet appareil jusqu'à ce qu'elle se déconnecte et que Charlie se reconnecte.

Une application ou un site web ne peut avoir qu'un seul abonnement push par appareil. Ainsi, lorsqu'un utilisateur se déconnecte d'un appareil ou d'un site web et qu'un nouvel utilisateur se connecte, le jeton de notification push est réattribué au nouvel utilisateur. Cela se reflète dans le profil de l'utilisateur dans la section **Contact Settings** de l'onglet **Engagement** :

![Journal des modifications du jeton de notification push dans l'onglet Engagement du profil d'un utilisateur, qui indique quand le jeton de notification push a été transféré à un autre utilisateur et quel était le jeton.]({% image_buster /assets/img/push_token_changelog.png %})

Comme il n'existe aucun moyen pour les fournisseurs push (APNs/FCM) de distinguer plusieurs utilisateurs sur un même appareil, nous transmettons le jeton de notification push au dernier utilisateur connecté pour déterminer quel utilisateur cibler sur l'appareil pour le push.

{% alert tip %}
Si vous voyez un message d'erreur dans **Contact Settings** > **Push Changelog**, consultez [Messages d'erreur push courants]({{site.baseurl}}/user_guide/channels/push/push_error_codes/) pour des explications et les étapes suivantes.
{% endalert %}

## Enregistrement des jetons de notification push {#push-token-registration}

Chaque plateforme d'appareil gère l'enregistrement des jetons de notification push différemment. Consultez les informations suivantes pour des détails spécifiques à chaque plateforme :

{% tabs local %}
{% tab web %}
Vous devez demander un opt-in explicite aux utilisateurs via la boîte de dialogue d'autorisation native du navigateur. Un jeton sera reçu après que les utilisateurs auront accepté. Contrairement à iOS et Android, qui permettent à votre application d'afficher l'invite d'autorisation à tout moment, certains navigateurs modernes n'afficheront l'invite que si elle est déclenchée par un « geste utilisateur » (clic de souris ou frappe au clavier). Si votre site tente de demander l'autorisation de notification push au chargement de la page, elle sera probablement ignorée ou réduite au silence par le navigateur.
{% endtab %}

{% tab android %}
Lorsque votre application est installée, un jeton de notification push est automatiquement généré pour votre application&#8212;cependant, il ne peut être utilisé que pour les [notifications push en arrière-plan](#foreground-vs-background) jusqu'à ce que l'utilisateur accepte explicitement. De plus, l'enregistrement est géré différemment selon les versions d'Android :

| Version | Détails |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Android 13** | L'autorisation push doit être demandée et accordée par l'utilisateur. Votre application peut demander l'autorisation manuellement, ou les utilisateurs seront invités automatiquement après la création d'un [canal de notification](https://developer.android.com/reference/android/app/NotificationChannel). |
| **Android 12 et versions antérieures** | Tous les utilisateurs sont considérés comme `Subscribed` après leur première session. Braze demande automatiquement un jeton de notification push à ce moment-là, rendant l'utilisateur activé pour le push avec un jeton valide et un état d'abonnement par défaut de `Subscribed`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Enregistrement des jetons de notification push" }
{% endtab %}

{% tab ios %}
iOS ne génère pas automatiquement de jetons de notification push pour une application lors de son installation. De plus, l'enregistrement est géré différemment selon les versions d'iOS :

| Version | Autorisation provisoire ? | Détails |
|------------------------------------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **iOS 12** | Oui | Lorsqu'un utilisateur accepte les notifications push, vous obtenez une autorisation standard, vous permettant d'envoyer des [notifications push au premier plan](#foreground-vs-background). Cependant, vous pouvez également demander une [autorisation provisoire]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options/#provisional-push), qui vous permet d'envoyer silencieusement des [notifications push en arrière-plan](#foreground-vs-background) directement dans le centre de notifications. |
| **iOS 11 ou versions antérieures** | Non | Tous les utilisateurs doivent explicitement accepter de recevoir des notifications push. Un jeton de notification push n'est généré qu'après l'octroi de l'autorisation. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Enregistrement des jetons de notification push" }
{% endtab %}
{% endtabs %}

### Vérifier l'état d'abonnement push d'un utilisateur {#checking-users-push-subscription-state}

![Profil utilisateur de Jane Doe affichant l'état d'abonnement push et les détails d'enregistrement push dans l'onglet Engagement.]({% image_buster /assets/img/push_implementation_guide/checking-users-push-subscription-state.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Il existe deux façons de vérifier l'état d'abonnement push d'un utilisateur avec Braze :

- **Profil utilisateur** : Vous pouvez accéder aux profils utilisateurs individuels via le tableau de bord de Braze sur la page [Recherche d'utilisateurs]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/). Après avoir trouvé le profil d'un utilisateur (via l'adresse e-mail, le numéro de téléphone ou l'ID utilisateur externe), vous pouvez sélectionner l'onglet **Engagement** pour consulter et ajuster manuellement l'état d'abonnement d'un utilisateur.
- **Export via REST API** : Vous pouvez exporter les profils utilisateurs individuels au format JSON en utilisant les endpoints d'export [Utilisateurs par Segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) ou [Utilisateurs par identifiant]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/). Braze renverra un objet de jetons de notification push contenant les informations d'activation push par appareil.

### Vérifier l'état d'enregistrement push {#checking-push-registration-status}

Dans l'onglet **Engagement** du profil d'un utilisateur, vous verrez **Push Registered For** suivi d'un nom d'application. Si aucune information d'application n'existe pour cet appareil, vous verrez deux tirets (**&#45;&#45;**). Il y aura une entrée pour chaque appareil appartenant à l'utilisateur.

Si le nom de l'application de l'entrée de l'appareil est préfixé par `Foreground:`, l'application est autorisée à recevoir à la fois des notifications push au premier plan (visibles par l'utilisateur) et des notifications push en arrière-plan (non visibles par l'utilisateur) sur cet appareil.

![Journal des modifications push avec un exemple de jeton de notification push.]({% image_buster /assets/img/push_changelog.png %}){: style="float:right;max-width:40%;margin-left:15px;margin-top:10px;"}

En revanche, si le nom de l'application de l'entrée de l'appareil est préfixé par `Background:`, l'application est uniquement autorisée à recevoir des [notifications push en arrière-plan]({{site.baseurl}}/user_guide/channels/push/types/#background-push-notifications) et ne peut pas afficher de notifications visibles par l'utilisateur sur cet appareil. Cela indique généralement que l'utilisateur a désactivé les notifications pour l'application sur cet appareil.

Si un jeton de notification push est transféré à un autre utilisateur sur le même appareil, le premier utilisateur ne sera plus enregistré pour le push.

## Gestion des jetons de notification push {#push-token-management}

Consultez le tableau suivant pour les actions qui entraînent des modifications ou la suppression des jetons de notification push des profils utilisateurs.

| Action | Description |
| ------ | ----------- |
| Appel de la méthode `changeUser()` | La méthode `changeUser()` de Braze change l'ID utilisateur auquel les SDK attribuent les données de comportement utilisateur. Cette méthode est généralement appelée lorsqu'un utilisateur se connecte à une application. Lorsque `changeUser()` est appelée avec un ID utilisateur différent ou nouveau sur un appareil spécifique, le jeton de notification push de cet appareil sera transféré au profil Braze correspondant avec l'ID utilisateur approprié. |
| Une erreur push survient | Certaines erreurs push courantes qui entraînent la suppression du jeton incluent `MismatchSenderId`, `InvalidRegistration` et d'autres types de rebonds push. <br><br>Consultez notre liste complète des [erreurs push]({{site.baseurl}}/user_guide/channels/push/push_error_codes/) courantes. |
| L'utilisateur désinstalle l'application | Lorsqu'un utilisateur désinstalle l'application d'un appareil, Braze supprime le jeton de notification push du profil de l'utilisateur. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Gestion des jetons de notification push" }

### À quoi cela ressemble-t-il à plus grande échelle ? {#what-does-this-look-like-on-a-broader-scale}

Lorsqu'un utilisateur ouvre une nouvelle application et accorde l'accès push via une invite push, un appel est effectué depuis le SDK Braze vers les fournisseurs push. Lorsque cet appel est effectué, le fournisseur push vérifie que tout est correctement configuré. Si c'est le cas, un jeton de notification push est transmis à votre appareil. Lorsque ce jeton arrive, le SDK le communique à Braze. Une fois que Braze a reçu le jeton du fournisseur push, nous mettons à jour ou créons un nouveau profil utilisateur. Ces utilisateurs sont alors considérés comme enregistrés.

Si nous voulons lancer une campagne, nous créons une Campaign dans Braze qui génère un payload push à envoyer au fournisseur push. À partir de là, le fournisseur délivre le payload push à l'appareil de l'utilisateur et le SDK transmet l'état de l'envoi de messages à Braze.

![Un diagramme de flux illustrant le processus push décrit ci-dessus entre Braze, le client et le service Apple Push Notification ou Firebase Cloud Messaging.]({% image_buster /assets/img/push_process.png %})

| Étapes d'enregistrement | Étapes d'envoi de messages |
| ------------------ | --------------- |
| 1. Le client (appareil) s'enregistre auprès du fournisseur push<br>2. Le fournisseur génère et délivre le jeton de notification push<br>3. Transmission des jetons à Braze |1. Braze envoie le payload push au fournisseur<br>2. Le fournisseur délivre le payload push à l'appareil<br>3. Le SDK transmet les statistiques d'envoi de messages à Braze |
{: .reset-td-br-1 .reset-td-br-2 aria-label="À quoi cela ressemble-t-il à plus grande échelle ?" }

## Questions fréquemment posées {#frequently-asked-questions}

### Que se passe-t-il lorsqu'un utilisateur ayant accepté les notifications supprime puis retélécharge mon application ? {#what-happens-when-an-opted-in-user-deletes-and-then-redownloads-my-app}

Supposons qu'un utilisateur accepte les notifications push, reçoive quelques messages push, puis supprime l'application. Cela supprimera le consentement push au niveau de l'appareil. À partir de là, le premier push ayant rebondi après la désinstallation entraînera automatiquement la désinscription de cet utilisateur des futurs messages push. Ensuite, si un utilisateur réinstalle l'application mais ne la lance pas, Braze ne pourra pas lui envoyer de notification push car les jetons de notification push n'ont pas été réattribués pour votre application.

De plus, si un utilisateur réactive les notifications push au premier plan, il faudra un démarrage de session pour mettre à jour cette information dans son profil utilisateur et commencer à recevoir des messages push.

### Quand les jetons de notification push expirent-ils ? {#push-token-expire}

Malheureusement, APNs et FCM ne définissent pas vraiment cela. Les jetons de notification push peuvent expirer lorsqu'une application est mise à jour, lorsque les utilisateurs transfèrent leurs données vers un nouvel appareil, ou lorsqu'ils réinstallent un système d'exploitation. Dans la plupart des cas, nous n'avons pas vraiment de visibilité sur les raisons pour lesquelles les fournisseurs push font expirer certains jetons de notification push.

Pour tenir compte de cette ambiguïté, nos intégrations push du SDK enregistrent et transmettent toujours les jetons au démarrage de la session afin de garantir que nous disposons du jeton le plus à jour.