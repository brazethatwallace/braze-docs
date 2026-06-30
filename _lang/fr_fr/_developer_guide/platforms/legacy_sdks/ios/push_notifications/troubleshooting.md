---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes de notification push pour iOS
platform: iOS
page_order: 30
description: "Cet article de référence couvre les sujets potentiels de résolution des problèmes pour votre implémentation de notifications push iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Résolution des problèmes {#push-troubleshooting}

## Comprendre le flux de travail Braze/APNs {#understanding-the-brazeapns-workflow}

Le service Apple Push Notification (APNs) est l'infrastructure d'Apple pour l'envoi de notifications push aux applications iOS et OS X. Voici la structure simplifiée de la manière dont les notifications push sont activées pour les appareils de vos utilisateurs et la façon dont Braze peut leur envoyer des notifications push :

1. Vous configurez le certificat push et le profil de provisionnement
2. Les appareils s'enregistrent auprès des APNs et fournissent à Braze des jetons de notification push
3. Vous lancez une Campaign push Braze
4. Braze supprime les jetons non valides

### Étape 1 : Configurer le certificat push et le profil de provisionnement {#step-1-configuring-the-push-certificate-and-provisioning-profile}

Lors du développement de votre application, vous devez créer un certificat SSL pour activer les notifications push. Ce certificat sera inclus dans le profil de provisionnement avec lequel votre application est créée et devra également être téléchargé sur le tableau de bord de Braze. Le certificat permet à Braze de communiquer aux APNs que nous sommes autorisés à envoyer des notifications push en votre nom.

Il existe deux types de [profils de provisionnement](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html) et de certificats : le développement et la distribution. Nous vous recommandons d'utiliser uniquement des profils et des certificats de distribution pour éviter toute confusion. Si vous choisissez d'utiliser différents profils et certificats pour le développement et la distribution, assurez-vous que le certificat téléchargé sur le tableau de bord correspond au profil de provisionnement que vous utilisez actuellement.

{% alert warning %}
Ne modifiez pas l'environnement du certificat push (développement par rapport à la production). Modifier le certificat push pour un environnement incorrect peut entraîner la suppression accidentelle du jeton de notification push de vos utilisateurs, les rendant inaccessibles par notification push.
{% endalert %}

#### Étape 2 : Les appareils s'enregistrent auprès des APNs et fournissent à Braze des jetons de notification push {#step-2-devices-register-for-apns-and-provide-braze-with-push-tokens}

Lorsque les utilisateurs ouvrent votre application, ils sont invités à accepter les notifications push. S'ils acceptent cette invite, les APNs génèrent un jeton de notification push pour cet appareil particulier. Le SDK iOS enverra immédiatement et de manière asynchrone le jeton push pour les applications utilisant la [politique de vidage automatique]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/fine_network_traffic_control#automatic-request-processing) par défaut. Une fois qu'un jeton push est associé à un utilisateur, celui-ci apparaîtra comme « Push Registered » dans le tableau de bord sur son profil utilisateur sous l'onglet **Engagement** et sera éligible pour recevoir des notifications push des Campaigns Braze.

{% alert note %}
À partir de Xcode 14, vous pouvez tester les notifications push à distance sur un simulateur iOS.
{% endalert %}

#### Étape 3 : Lancer une Campaign push Braze {#step-3-launching-a-braze-push-campaign}

Lorsqu'une Campaign push est lancée, Braze effectue des requêtes auprès des APNs pour délivrer votre message. Braze utilise le certificat push SSL téléchargé dans le tableau de bord pour authentifier et vérifier que nous sommes autorisés à envoyer des notifications push aux jetons de notification push fournis. Si un appareil est en ligne, la notification devrait être reçue peu de temps après l'envoi de la campagne. Notez que Braze fixe à 30 jours la [date d'expiration](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607) par défaut des APNs pour les notifications.

#### Étape 4 : Supprimer les jetons non valides {#step-4-removing-invalid-tokens}

Si les [APNs](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) nous informent que l'un des jetons push auxquels nous avons tenté d'envoyer un message n'est pas valide, nous supprimons ces jetons des profils utilisateurs auxquels ils étaient associés.

## Utiliser les journaux d'erreur de notification push {#utilizing-the-push-error-logs}

Braze fournit un journal des erreurs de notification push dans le **Journal d'activité des messages**. Ce journal d'erreurs fournit de nombreux avertissements qui peuvent être très utiles pour identifier les raisons pour lesquelles vos campagnes ne fonctionnent pas comme prévu. Cliquer sur un message d'erreur vous redirigera vers la documentation pertinente pour vous aider à résoudre un incident particulier.

![Les journaux d'erreur push affichent l'heure à laquelle l'erreur s'est produite, le nom de l'application, le canal, le type d'erreur et le message d'erreur.]({% image_buster /assets/img_archive/message_activity_log.png %})

Les erreurs courantes que vous pouvez voir ici comprennent des notifications spécifiques à l'utilisateur, telles que [« Received Unregistered Sending to Push Token »](#received-unregistered-sending).

En outre, Braze fournit également un journal des modifications push sur le profil utilisateur, sous l'onglet **Engagement**. Ce journal des modifications donne un aperçu du comportement d'enregistrement des notifications push, comme l'invalidation des jetons, les erreurs d'enregistrement push, les jetons déplacés vers de nouveaux utilisateurs, etc.

![Exemple animé de carte de contenu.]({% image_buster /assets/img_archive/push_changelog.gif %}){: style="max-width:50%;" }

## Problèmes d'enregistrement de notifications push {#push-registration-issues}

Pour ajouter une vérification à la logique d'enregistrement push de votre application, mettez en place des [tests unitaires de push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/unit_tests).

### Pas d'invite d'enregistrement push {#no-push-registration-prompt}

Si l'application ne vous invite pas à vous inscrire aux notifications push, il y a probablement un problème avec votre intégration d'inscription push. Assurez-vous d'avoir suivi notre [documentation]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration) et d'avoir correctement intégré notre enregistrement push. Vous pouvez également définir des points d'arrêt dans votre code pour vous assurer que le code d'inscription aux notifications push est en cours d'exécution.

#### Aucun utilisateur « push registered » affiché dans le tableau de bord {#no-push-registered-users-showing-in-the-dashboard}

- Vérifiez que votre application vous invite à autoriser les notifications push. En général, cette invite apparaît lors de votre première ouverture de l'application, mais elle peut être programmée pour apparaître ailleurs. Si elle n'apparaît pas là où elle le devrait, le problème est probablement la configuration de base des capacités de notification push de votre application.
  - Vérifiez que les étapes de l'[intégration push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration) ont été effectuées avec succès.
  - Vérifiez que le profil de provisionnement avec lequel votre application a été créée inclut les autorisations pour les notifications push. Assurez-vous de télécharger tous les profils de provisionnement disponibles depuis votre compte développeur Apple. Pour confirmer cela, procédez comme suit :
    1. Dans Xcode, accédez à **Preferences > Accounts** (ou utilisez le raccourci clavier <kbd>Command</kbd>+<kbd>,</kbd>).
    2. Sélectionnez l'identifiant Apple que vous utilisez pour votre compte développeur et cliquez sur **View Details**.
    3. Sur la page suivante, cliquez sur **<i class="fas fa-redo-alt"></i> Refresh** et confirmez que vous téléchargez tous les profils de provisionnement disponibles.
- Vérifiez que vous avez [correctement activé la fonctionnalité push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-2-enable-push-capabilities) dans votre application.
- Vérifiez que votre profil de provisionnement push correspond à l'environnement dans lequel vous effectuez des tests. Les certificats universels peuvent être configurés dans le tableau de bord de Braze pour envoyer vers l'environnement de développement ou de production APNs. L'utilisation d'un certificat de développement pour une application de production ou d'un certificat de production pour une application de développement ne fonctionnera pas.
- Vérifiez que vous appelez bien notre méthode `registerPushToken` en définissant un point d'arrêt dans votre code.
- Vérifiez que vous êtes sur un appareil (les notifications push ne fonctionnent pas sur un simulateur) et que vous disposez d'une bonne connectivité réseau.

## Appareils ne recevant pas de notifications push {#devices-not-receiving-push-notifications}

### Utilisateurs qui ne sont plus « push registered » après l'envoi d'une notification push {#users-no-longer-push-registered-after-sending-a-push-notification}

Ceci indique probablement que l'utilisateur avait un jeton de notification push non valide. Cela peut se produire pour plusieurs raisons :

#### Incohérence entre le tableau de bord et le certificat de l'application {#dashboard-and-app-certificate-mismatch}

Si le certificat push que vous avez téléchargé dans le tableau de bord n'est pas le même que celui du profil de provisionnement avec lequel votre application a été créée, les APNs rejetteront le jeton. Vérifiez que vous avez téléchargé le bon certificat et effectué une autre session dans l'application avant de tenter une autre notification de test.

##### Désinstallations {#uninstalls}

Si un utilisateur a désinstallé votre application, son jeton de notification push sera invalide et supprimé lors du prochain envoi.

##### Régénération de votre profil de provisionnement {#regenerating-your-provisioning-profile}

En dernier recours, repartir de zéro et créer un tout nouveau profil de provisionnement peut éliminer les erreurs de configuration résultant de l'utilisation simultanée de plusieurs environnements, profils et applications. Il existe de nombreuses « pièces mobiles » dans la configuration des notifications push pour les applications iOS, il est donc parfois préférable de recommencer depuis le début. Cela permettra également d'isoler le problème si vous devez poursuivre la résolution des problèmes.

#### Utilisateurs encore « push registered » après l'envoi d'une notification push {#users-still-push-registered-after-sending-a-push-notification}

##### Application au premier plan {#app-is-foregrounded}

Sur les versions iOS qui n'intègrent pas les notifications push via le framework `UserNotifications`, si l'application est au premier plan lorsque le message push est reçu, il ne s'affichera pas. Vous devez mettre l'application en arrière-plan sur vos appareils de test avant d'envoyer des messages de test.

##### Notification de test planifiée de manière incorrecte {#test-notification-scheduled-incorrectly}

Vérifiez la planification que vous avez définie pour votre message de test. S'il est réglé sur la distribution par fuseau horaire local ou sur le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing), il se peut que vous n'ayez pas encore reçu le message (ou que l'application ait été au premier plan au moment de sa réception).

#### L'utilisateur n'est pas « push registered » pour l'application testée {#user-not-push-registered-for-the-app-being-tested}

Vérifiez le profil utilisateur de l'utilisateur auquel vous essayez d'envoyer un message de test. Sous l'onglet **Engagement**, il devrait y avoir une liste d'« applications poussables ». Vérifiez que l'application à laquelle vous essayez d'envoyer des messages de test figure dans cette liste. Les utilisateurs apparaîtront comme « Push Registered » s'ils ont un jeton push pour n'importe quelle application dans votre espace de travail, ce qui pourrait donc être un faux positif.

Ce qui suit indiquerait un problème avec l'inscription aux notifications push ou que le jeton de l'utilisateur a été renvoyé à Braze comme invalide par les APNs après avoir été envoyé :

![Profil utilisateur affichant les paramètres de contact d'un utilisateur. Vous pouvez voir ici les applications pour lesquelles les notifications push sont enregistrées.]({% image_buster /assets/img_archive/registration_problem.png %}){: style="max-width:50%"}

## Les messages push ne sont pas envoyés {#push-messages-not-sending}

Pour résoudre les problèmes liés aux notifications push qui ne sont pas envoyées, reportez-vous à la section [Résolution des problèmes des notifications push]({{site.baseurl}}/user_guide/channels/push/troubleshooting).

## Erreurs du journal d'activité des messages {#message-activity-log-errors}

### Réception d'un envoi non enregistré au jeton de notification push {#received-unregistered-sending}

- Assurez-vous que le jeton push envoyé à Braze depuis la méthode `[[Appboy sharedInstance] registerPushToken:]` est valide. Vous pouvez consulter le **Journal d'activité des messages** pour voir le jeton de notification push. Il devrait ressembler à quelque chose comme `6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6`, une longue chaîne de caractères contenant un mélange de lettres et de chiffres. Si votre jeton push semble différent, vérifiez votre [code]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-4-register-push-tokens-with-braze) d'envoi des jetons push à Braze.
- Vérifiez que votre profil de provisionnement push correspond à l'environnement dans lequel vous effectuez des tests. Les certificats universels peuvent être configurés dans le tableau de bord de Braze pour envoyer vers l'environnement de développement ou de production APNs. L'utilisation d'un certificat de développement pour une application de production ou d'un certificat de production pour une application de développement ne fonctionnera pas.
 - Vérifiez que le jeton push que vous avez téléchargé sur Braze correspond au profil de provisionnement que vous avez utilisé pour créer l'application à partir de laquelle vous avez envoyé le jeton push.

#### Jeton d'appareil non destiné à la rubrique {#device-token-not-for-topic}

Cette erreur indique que le certificat push et l'ID de lot (bundle ID) de votre application ne correspondent pas. Vérifiez que le certificat push que vous avez téléchargé sur Braze correspond au profil de provisionnement utilisé pour créer l'application à partir de laquelle le jeton push a été envoyé.

#### BadDeviceToken lors de l'envoi au jeton de notification push {#baddevicetoken-sending-to-push-token}

Le `BadDeviceToken` est un code d'erreur APNs et ne provient pas de Braze. Cette réponse peut être renvoyée pour plusieurs raisons, notamment :

- L'application a reçu un jeton push qui n'était pas valide pour les informations d'identification téléchargées sur le tableau de bord.
- La fonctionnalité push a été désactivée pour cet espace de travail.
- L'utilisateur s'est désinscrit des notifications push.
- L'application a été désinstallée.
- Apple a actualisé le jeton push, ce qui a invalidé l'ancien jeton.
- L'application a été conçue pour un environnement de production, mais les informations d'identification push téléchargées sur Braze sont définies pour un environnement de développement (ou l'inverse).

## Problèmes après la réception de la notification push {#issues-after-push-delivery}

Pour ajouter une vérification à la gestion push de votre application, mettez en place des [tests unitaires de push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/unit_tests).

### Les clics sur les notifications push ne sont pas enregistrés {#push-clicks-not-logged}

- Si cela ne se produit que sur iOS 10, assurez-vous d'avoir suivi les étapes d'intégration push pour [iOS 10]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-5-enable-push-handling).
- Braze ne gère pas les notifications push reçues silencieusement au premier plan (par exemple, le comportement par défaut des notifications push au premier plan avant le framework `UserNotifications`). Cela signifie que les liens ne seront pas ouverts et que les clics sur les notifications push ne seront pas enregistrés. Si votre application n'a pas encore intégré le framework `UserNotifications`, Braze ne traitera pas les notifications push lorsque l'état de l'application est `UIApplicationStateActive`. Vous devez vous assurer que votre application ne retarde pas les appels à nos [méthodes de gestion push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-5-enable-push-handling) ; dans le cas contraire, le SDK iOS peut considérer les notifications push comme des événements push silencieux de premier plan et ne pas les traiter.

#### Les liens web issus des clics sur les notifications push ne s'ouvrent pas {#web-links-from-push-clicks-not-opening}

iOS 9+ nécessite que les liens soient conformes à ATS pour être ouverts dans les vues web. Assurez-vous que vos liens web utilisent HTTPS. Pour plus d'informations, reportez-vous à notre article sur la [conformité ATS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking#app-transport-security-ats).

#### Les liens profonds issus des clics sur les notifications push ne s'ouvrent pas {#deep-links-from-push-clicks-not-opening}

La plupart du code qui gère les liens profonds gère également les ouvertures push. Tout d'abord, assurez-vous que les ouvertures de notifications push sont enregistrées. Si ce n'est pas le cas, [corrigez ce problème](#push-clicks-not-logged) (car la correction corrige souvent la gestion des liens).

Si les ouvertures sont enregistrées, vérifiez s'il s'agit d'un problème avec le lien profond en général ou avec la gestion des clics push sur les liens profonds. Pour ce faire, testez si un lien profond depuis un clic sur un message in-app fonctionne.

#### Peu ou pas d'ouvertures directes {#few-or-no-direct-opens}

Si au moins un utilisateur ouvre votre notification push iOS, mais que peu ou pas d'_ouvertures directes_ sont enregistrées dans Braze, il se peut qu'il y ait un problème avec votre [intégration SDK]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview). Gardez à l'esprit que les _ouvertures directes_ ne sont pas enregistrées pour les envois de test ou les notifications push silencieuses.

- Assurez-vous que les messages ne sont pas envoyés en tant que [notifications push silencieuses]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications#sending-silent-push-notifications). Le message doit comporter du texte dans le titre ou le corps pour ne pas être considéré comme silencieux.
- Vérifiez à nouveau les étapes suivantes du [guide d'intégration push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration) :
   - [S'inscrire aux notifications push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-1-register-for-push-notifications-with-apns) : À chaque lancement de l'application, de préférence dans `application:didFinishLaunchingWithOptions:`, le code de l'étape 3 doit être exécuté. La propriété delegate de `UNUserNotificationCenter.current()` doit être assignée à un objet qui implémente `UNUserNotificationCenterDelegate` et contient la méthode `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:`.
   - [Activer la gestion push]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/push_notifications/integration#step-5-enable-push-handling) : Vérifiez que la méthode `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` a été implémentée.