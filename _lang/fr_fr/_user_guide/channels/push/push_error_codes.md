---
nav_title: Messages d'erreur push courants
article_title: Messages d'erreur push courants
page_order: 22
page_type: reference
description: "Cet article couvre les messages d'erreur courants liés aux notifications push pour iOS et Android, et vous guide à travers les solutions potentielles."
channel: push
platform:
- iOS
- Android
---

# Messages d'erreur push courants {#common-push-error-messages}

> Cette page couvre les messages d'erreur courants pour l'envoi de notifications push.

{% tabs %}
{% tab Android %}
## Rebond push : MismatchSenderId {#push-bounced-mismatchsenderid}
`MismatchSenderId` indique un échec d'authentification. Firebase Cloud Messaging (FCM) s'authentifie avec deux éléments clés : le senderID et la clé API FCM. Ces deux éléments doivent être validés pour leur exactitude. Pour plus d'informations, consultez la [documentation Android](https://firebase.google.com/docs/cloud-messaging/http-server-ref#error-codes) à ce sujet.

Les échecs courants peuvent inclure :
- Un [senderID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration#step-1-enable-firebase) incorrect
- Des enregistrements multiples si l'utilisateur s'enregistre auprès d'un autre service push avec un senderID différent

### Rebond push : InvalidRegistration {#push-bounced-invalidregistration}
`InvalidRegistration` peut se produire lorsqu'un jeton de notification push est malformé. Les échecs courants peuvent inclure les cas suivants :
- Les utilisateurs transmettent manuellement les jetons d'enregistrement à Braze mais n'appellent pas `getToken()`. Par exemple, ils peuvent transmettre l'intégralité de l'ID d'instance. Le jeton dans le message d'erreur ressemble à `&#124;ID&#124;1&#124;:[regular token]`.
- Les utilisateurs s'enregistrent auprès de plusieurs services. Nous nous attendons actuellement à ce que les intentions d'enregistrement push arrivent dans l'ancien format, donc si les utilisateurs s'enregistrent à plusieurs endroits et que nous interceptons des intentions provenant d'autres services, nous pouvons obtenir des jetons de notification push malformés.

### Rebond push : NotRegistered {#notregistered}

`NotRegistered` signifie généralement que l'application a été supprimée de l'appareil (ce qui constitue notre signal de désinstallation). Cela peut également se produire en cas d'enregistrements multiples, lorsqu'un second enregistrement invalide le jeton de notification push que Braze reçoit.

### DEVICE_UNREGISTERED {#device-unregistered}

Cette erreur apparaît dans le journal d'activité des messages sous la forme : `Received 'Error: DEVICE_UNREGISTERED, ' sending to '[Token String]'`

Cela se produit généralement pour l'une des raisons suivantes :

- L'utilisateur a désinstallé l'application. C'est la cause la plus courante. Lorsque l'application est supprimée d'un appareil, le jeton de notification push devient invalide.
- Les identifiants push ont été mis à jour dans l'application. Si votre équipe a modifié les identifiants FCM ou les certificats intégrés à l'application, les utilisateurs enregistrés avec les anciens identifiants ont des jetons invalides jusqu'à ce que l'application les réenregistre.
- Une logique personnalisée désenregistre les utilisateurs des notifications push. C'est rare, mais il est techniquement possible de désenregistrer programmatiquement un appareil des notifications push en utilisant le [SDK Firebase/Android](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessaging#deleteToken()).

{% alert note %}
Cette erreur ne signifie pas que l'utilisateur a désactivé les notifications push — seulement qu'un jeton spécifique a été supprimé de son profil. C'est courant pour les utilisateurs qui testent des fonctionnalités et installent et désinstallent fréquemment l'application. Pour vérifier si l'utilisateur dispose encore de jetons valides, accédez à **Recherche d'utilisateurs** et consultez la section **Paramètres de contact** dans l'onglet **Engagement**.
{% endalert %}

### L'entité demandée est introuvable {#requested-entity-was-not-found}

Cette erreur peut se produire pour les raisons suivantes :

- L'utilisateur final a désinstallé l'application. Vous pouvez consulter son profil utilisateur pour confirmer si c'est le cas.
- Le canal de notification est invalide. Selon votre intégration, les appareils peuvent avoir des jetons de notification push qui ne sont valides que pour certains canaux de notification. Lors de l'envoi vers un canal invalide, le message rebondit.
- La taille du payload est trop importante.

Pour plus d'informations, consultez la [documentation de Google](https://firebase.google.com/docs/cloud-messaging/manage-tokens#stale-and-expired-tokens) sur les jetons d'enregistrement obsolètes et expirés.

{% endtab %}
{% tab iOS %}

### Erreur d'envoi push car le payload était invalide {#error-sending-push-because-the-payload-was-invalid}

Ce message peut apparaître dans l'onglet **Engagement** du profil utilisateur sous **Paramètres de contact** > **Push Changelog** lorsque le service Apple Push Notification (APNs) rejette la requête push en raison d'un payload invalide.

Dans Braze, ce message du tableau de bord peut correspondre à l'une des raisons d'erreur APNs suivantes :

- `PayloadEmpty` : le payload ne contenait pas le contenu requis pour le type de notification push envoyée.
- `PayloadTooLarge` : le payload dépassait la taille maximale autorisée par APNs.

Les causes courantes incluent :

- Des clés personnalisées (et leurs valeurs) rendant le payload trop volumineux (cela peut inclure des valeurs rendues par Liquid de taille inattendue).
- Une alerte ou un corps vide ou manquant là où c'est requis (ou un payload `aps` autrement malformé).

Étapes suivantes :

- Réduisez la taille du payload en supprimant les clés personnalisées et en raccourcissant les grandes valeurs dynamiques.
- Si vous envoyez via l'API, validez le payload JSON final (y compris sa taille) avant l'envoi.

### Rebond push : BadToken {#push-bounced-badtoken}

L'erreur `BadToken` peut se produire pour plusieurs raisons :
- Le jeton de notification push n'est pas envoyé correctement à Braze (par exemple, dans `registerDeviceToken:` ou l'équivalent de votre plateforme).
	- Vérifiez le jeton dans le [Journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log). Il devrait généralement ressembler à une longue chaîne de lettres et de chiffres (comme `6e407a9be8d07f0cdeb9e714733a89445f57a89ec890d63867c482a483506fa6`). Si ce n'est pas le cas, vérifiez le code impliqué dans l'envoi du jeton de notification push à Braze.<br><br>
- Environnement de provisionnement non concordant :
	- Si vous vous enregistrez avec un certificat de développement et essayez d'envoyer avec un certificat de production, vous pouvez voir cette erreur.
	- Braze ne prend en charge que les certificats universels pour les environnements de production. Tester les notifications push dans les environnements de développement avec un certificat universel ne fonctionnera pas.
	- Ce rapport envoie des rebonds en production mais pas en développement.<br><br>
- Profil de provisionnement non concordant :
	- Cela peut se produire si votre certificat ne correspond pas à celui qui a été utilisé pour obtenir le jeton. Si cela est suspecté, les étapes suivantes incluent :
		- S'assurer que le certificat push utilisé pour envoyer des notifications push depuis le tableau de bord de Braze et le profil de provisionnement sont correctement configurés.
		- Recréer la certification APNS puis recréer le profil de provisionnement après que le certificat APNS est configuré pour l'`app_id`. Cela peut parfois résoudre certains problèmes plus visibles.

### ID de bundle non autorisé {#bundle-id-not-allowed}

L'erreur `TopicDisallowed` signifie qu'APNs a rejeté la notification push car le sujet (ID de bundle) dans la requête n'est pas autorisé pour les identifiants d'authentification utilisés. Pour résoudre ce problème :

1. **Vérifiez l'ID de bundle.** Confirmez que l'ID de bundle configuré dans les paramètres de votre application Braze correspond exactement à l'ID de bundle de votre application. Cela inclut toute variation de suffixe (par exemple, `.debug`, `.staging`).
2. **Vérifiez votre configuration d'authentification APNs.** Confirmez que votre application est configurée avec la bonne clé APNs `.p8` et que la clé est associée à la même équipe Apple Developer que l'application à laquelle vous envoyez.
3. **Confirmez l'environnement de l'application.** Si vous avez des ID d'application séparés dans Braze pour les builds de développement et de production, vérifiez que chacun est configuré avec les bons identifiants push et le bon environnement.

### Unregistered {#ios-unregistered}

Cette erreur apparaît dans le journal d'activité des messages sous la forme :

`Received 'Unregistered' sending to '[Token String]'`

C'est l'équivalent iOS de l'erreur Android [DEVICE_UNREGISTERED](#device-unregistered). Elle se produit généralement pour l'une des raisons suivantes :

- L'utilisateur a désinstallé l'application. C'est la cause la plus courante.
- Les certificats push ont été mis à jour. Si votre équipe a modifié ou renouvelé les certificats APNs, les utilisateurs enregistrés avec les anciens certificats peuvent avoir des jetons invalides jusqu'à ce que l'application les réenregistre.
- Une logique personnalisée désenregistre les utilisateurs des notifications push. C'est rare, mais il est techniquement possible de se désenregistrer programmatiquement des notifications à distance en utilisant le SDK iOS.

{% alert note %}
Cette erreur ne signifie pas que l'utilisateur a désactivé les notifications push — seulement qu'un jeton spécifique a été supprimé de son profil. Pour vérifier si l'utilisateur dispose encore de jetons valides, accédez à **Recherche d'utilisateurs** et consultez la section **Paramètres de contact** dans l'onglet **Engagement**.
{% endalert %}

### InvalidProviderToken

L'erreur `InvalidProviderToken` signifie qu'APNs a rejeté la requête car le jeton d'authentification (provenant d'une clé `.p8`) ou le certificat push (`.p12`) ne correspond pas à l'ID de bundle ou au équipe ID de l'application. Pour résoudre ce problème :

1. **Vérifiez votre équipe ID et Key ID :** si vous utilisez une clé d'authentification `.p8`, confirmez que le **équipe ID** et le **Key ID** configurés dans le tableau de bord de Braze (**Paramètres** > **Paramètres des applications** > sélectionnez votre application iOS) correspondent aux valeurs de votre compte Apple Developer.
2. **Vérifiez l'ID de bundle :** assurez-vous que l'ID de bundle enregistré dans Braze correspond à l'ID de bundle de votre application. Une discordance, comme une différence de casse ou un suffixe `.debug`, provoque cette erreur.
3. **Rechargez la clé ou le certificat :** si la clé `.p8` ou le certificat `.p12` a été récemment régénéré ou révoqué, chargez la nouvelle clé dans Braze et supprimez l'ancienne.
4. **Confirmez l'environnement APNs :** si vous utilisez un certificat `.p12`, vérifiez que vous avez sélectionné le bon environnement (développement versus production) lors du chargement. Pour les clés `.p8`, cela est géré automatiquement.

### Rebond push : le service de retour APNS a supprimé le jeton {#push-bounced-apns-feedback-service-removed}

Cela se produit généralement lorsqu'un utilisateur désinstalle l'application. Braze interroge le service de retour APNS chaque nuit pour obtenir une liste de jetons invalides. Pour plus d'informations, consultez la documentation d'Apple sur la [communication avec APNs](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html).

{% endtab %}
{% endtabs %}