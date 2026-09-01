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

## Comprendre le workflow Braze/APNs {#understanding-the-brazeapns-workflow}

Le service Apple Push Notification (APNs) est l'infrastructure d'Apple pour l'envoi de notifications push aux applications iOS et OS X. Voici la structure simplifiée du fonctionnement de l'activation des notifications push pour les appareils de vos utilisateurs et la façon dont Braze peut leur envoyer des notifications push :

{% multi_lang_include developer_guide/push_notifications/push_registration_flow_steps.md %}

### Étape 1 : Configurer le certificat push et le profil de provisionnement {#step-1-configuring-the-push-certificate-and-provisioning-profile}

Lors du développement de votre application, créez un certificat SSL pour activer les notifications push. Ce certificat est inclus dans le profil de provisionnement avec lequel votre application est compilée et doit également être téléchargé sur le tableau de bord de Braze. Le certificat permet à Braze d'indiquer aux APNs que nous sommes autorisés à envoyer des notifications push en votre nom.

Il existe deux types de [profils de provisionnement](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html) et de certificats : développement et distribution. Nous recommandons d'utiliser uniquement les profils et certificats de distribution pour éviter toute confusion. Si vous choisissez d'utiliser des profils et certificats différents pour le développement et la distribution, assurez-vous que le certificat téléchargé sur le tableau de bord correspond au profil de provisionnement que vous utilisez actuellement.

{% alert warning %}
Ne modifiez pas l'environnement du certificat push (développement versus production). Changer le certificat push pour le mauvais environnement peut entraîner la suppression accidentelle du jeton push de vos utilisateurs, les rendant injoignables par notification push.
{% endalert %}

#### Étape 2 : Les appareils s'enregistrent auprès des APNs et fournissent des jetons push à Braze {#step-2-devices-register-for-apns-and-provide-braze-with-push-tokens}

Lorsque les utilisateurs ouvrent votre application, ils sont invités à accepter les notifications push. S'ils acceptent cette invite, les APNs génèrent un jeton push pour cet appareil particulier. Le SDK iOS enverra immédiatement et de manière asynchrone le jeton push pour les applications utilisant la [politique de vidage automatique]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/fine_network_traffic_control#automatic-request-processing) par défaut. Une fois qu'un jeton push est associé à un utilisateur, celui-ci apparaîtra comme « Push Registered » dans le tableau de bord sur son profil utilisateur sous l'onglet **Engagement** et sera éligible pour recevoir des notifications push provenant de Campaigns Braze.

{% alert note %}
À partir de Xcode 14, vous pouvez tester les notifications push distantes sur un simulateur iOS.
{% endalert %}

#### Étape 3 : Lancer une Campaign push Braze {#step-3-launching-a-braze-push-campaign}

Lorsqu'une Campaign push est lancée, Braze envoie des requêtes aux APNs pour distribuer votre message. Braze utilisera le certificat SSL push téléchargé sur le tableau de bord pour s'authentifier et vérifier que nous sommes autorisés à envoyer des notifications push aux jetons push fournis. Si un appareil est en ligne, la notification devrait être reçue peu après l'envoi de la Campaign. Notez que Braze définit la [date d'expiration](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607) par défaut des APNs pour les notifications à 30 jours.

#### Étape 4 : Supprimer les jetons invalides {#step-4-removing-invalid-tokens}

Si les [APNs](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) nous informent que l'un des jetons push auxquels nous tentions d'envoyer un message est invalide, nous supprimons ces jetons des profils utilisateur auxquels ils étaient associés.

## Utilisation des journaux d'erreurs push {#utilizing-the-push-error-logs}

Braze fournit un journal des erreurs de notifications push dans le **journal d'activité des messages**. Ce journal d'erreurs fournit une variété d'avertissements qui peuvent être très utiles pour identifier pourquoi vos Campaigns ne fonctionnent pas comme prévu. Sélectionner un message d'erreur vous redirige vers la documentation pertinente pour vous aider à résoudre un incident particulier.

![Journaux d'erreurs push affichant l'heure de l'erreur, le nom de l'application, le canal, le type d'erreur et le message d'erreur.]({% image_buster /assets/img_archive/message_activity_log.png %})

Les erreurs courantes que vous pourriez voir ici incluent des notifications spécifiques à l'utilisateur, telles que [« Received Unregistered Sending to Push Token »](#received-unregistered-sending).

De plus, Braze fournit également un journal des modifications push sur le profil utilisateur sous l'onglet **Engagement**. Ce journal des modifications offre un aperçu du comportement d'inscription push, tel que l'invalidation de jetons, les erreurs d'inscription push, les jetons transférés vers de nouveaux utilisateurs, etc.

![Exemple de content card animée.]({% image_buster /assets/img_archive/push_changelog.gif %}){: style="max-width:50%;" }

## Problèmes d'inscription aux notifications push {#push-registration-issues}

Pour ajouter une vérification de la logique d'inscription aux notifications push de votre application, implémentez les [tests unitaires push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/unit_tests).

### Pas d'invite d'inscription aux notifications push {#no-push-registration-prompt}

Si l'application ne vous invite pas à vous inscrire aux notifications push, il y a probablement un problème avec votre intégration de l'inscription aux notifications push. Assurez-vous d'avoir suivi notre [documentation]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration) et d'avoir correctement intégré notre inscription aux notifications push. Vous pouvez également définir des points d'arrêt dans votre code pour vous assurer que le code d'inscription aux notifications push s'exécute.

#### Aucun utilisateur « inscrit aux notifications push » n'apparaît dans le tableau de bord {#no-push-registered-users-showing-in-the-dashboard}

- Vérifiez que votre application vous invite à autoriser les notifications push. En général, cette invite apparaît lors de votre première ouverture de l'application, mais elle peut être programmée pour apparaître ailleurs. Si elle n'apparaît pas là où elle devrait, le problème vient probablement de la configuration de base des capacités push de votre application.
  - Vérifiez que les étapes d'[intégration des notifications push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration) ont été réalisées avec succès.
  - Vérifiez que le profil de provisionnement avec lequel votre application a été compilée inclut les autorisations pour les notifications push. Assurez-vous de télécharger tous les profils de provisionnement disponibles depuis votre compte développeur Apple. Pour confirmer cela, effectuez les étapes suivantes :
    1. Dans Xcode, accédez à **Preferences > Accounts** (ou utilisez le raccourci clavier <kbd>Command</kbd>+<kbd>,</kbd>).
    2. Sélectionnez l'identifiant Apple que vous utilisez pour votre compte développeur et cliquez sur **View Details**.
    3. Sur la page suivante, cliquez sur **<i class="fas fa-redo-alt"></i> Refresh** et confirmez que vous téléchargez bien tous les profils de provisionnement disponibles.
- Vérifiez que vous avez [correctement activé la capacité push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-2-enable-push-capabilities) dans votre application.
- Vérifiez que votre profil de provisionnement push correspond à l'environnement dans lequel vous effectuez vos tests. Les certificats universels peuvent être configurés dans le tableau de bord de Braze pour envoyer vers l'environnement APN de développement ou de production. L'utilisation d'un certificat de développement pour une application en production ou d'un certificat de production pour une application de développement ne fonctionnera pas.
- Vérifiez que vous appelez bien notre méthode `registerPushToken` en définissant un point d'arrêt dans votre code.
- Vérifiez que vous êtes sur un appareil (les notifications push ne fonctionnent pas sur un simulateur) et que vous disposez d'une bonne connectivité réseau.

## Appareils ne recevant pas les notifications push {#devices-not-receiving-push-notifications}

### Les utilisateurs ne sont plus « enregistrés pour les notifications push » après l'envoi d'une notification push {#users-no-longer-push-registered-after-sending-a-push-notification}

Cela indique probablement que l'utilisateur possédait un jeton de notification push invalide. Cela peut se produire pour plusieurs raisons :

#### Non-concordance entre le certificat du tableau de bord et celui de l'application {#dashboard-and-app-certificate-mismatch}

Si le certificat push que vous avez importé dans le tableau de bord n'est pas le même que celui du profil de provisionnement avec lequel votre application a été créée, les APN rejetteront le jeton. Vérifiez que vous avez importé le bon certificat et effectué une nouvelle session dans l'application avant de tenter une autre notification de test.

##### Désinstallations {#uninstalls}

Si un utilisateur a désinstallé votre application, son jeton de notification push sera invalide et supprimé lors du prochain envoi.

##### Régénérer votre profil de provisionnement {#regenerating-your-provisioning-profile}

En dernier recours, repartir de zéro et créer un tout nouveau profil de provisionnement peut résoudre les erreurs de configuration liées au travail avec plusieurs environnements, profils et applications en même temps. La configuration des notifications push pour les applications iOS comporte de nombreux « éléments variables », il est donc parfois préférable de recommencer depuis le début. Cela aidera également à isoler le problème si vous devez poursuivre la résolution des problèmes.

#### Les utilisateurs sont toujours « enregistrés pour les notifications push » après l'envoi d'une notification push {#users-still-push-registered-after-sending-a-push-notification}

##### L'application est au premier plan {#app-is-foregrounded}

Sur les versions d'iOS qui n'intègrent pas les notifications push via le framework `UserNotifications`, si l'application est au premier plan lorsque la notification push est reçue, elle ne sera pas affichée. Vous devez mettre l'application en arrière-plan sur vos appareils de test avant d'envoyer des messages de test.

##### Notification de test mal planifiée {#test-notification-scheduled-incorrectly}

Vérifiez la planification que vous avez définie pour votre message de test. Si elle est configurée sur une distribution en fuseau horaire local ou avec le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing), il est possible que vous n'ayez tout simplement pas encore reçu le message (ou que l'application ait été au premier plan lors de sa réception).

#### L'utilisateur n'est pas « enregistré pour les notifications push » pour l'application testée {#user-not-push-registered-for-the-app-being-tested}

Consultez le profil de l'utilisateur à qui vous essayez d'envoyer un message de test. Sous l'onglet **Engagement**, une liste des « applications activées pour les notifications push » devrait apparaître. Vérifiez que l'application à laquelle vous essayez d'envoyer des messages de test figure dans cette liste. Les utilisateurs apparaîtront comme « enregistrés pour les notifications push » s'ils possèdent un jeton de notification push pour n'importe quelle application de votre espace de travail, ce qui pourrait constituer un faux positif.

Ce qui suit indiquerait un problème d'enregistrement pour les notifications push ou que le jeton de l'utilisateur a été renvoyé à Braze comme invalide par les APN après un envoi :

![Un profil utilisateur affichant les paramètres de contact d'un utilisateur. Vous pouvez y voir pour quelles applications les notifications push sont enregistrées.]({% image_buster /assets/img_archive/registration_problem.png %}){: style="max-width:50%"}

## Les notifications push ne s'envoient pas {#push-messages-not-sending}

Pour résoudre les problèmes de notifications push qui ne s'envoient pas, consultez [Résolution des problèmes des notifications push]({{site.baseurl}}/user_guide/channels/push/troubleshooting).

## Erreurs du journal d'activité des messages {#message-activity-log-errors}

### Envoi non enregistré reçu vers le jeton push {#received-unregistered-sending}

- Assurez-vous que le jeton push envoyé à Braze depuis la méthode `[[Appboy sharedInstance] registerPushToken:]` est valide. Vous pouvez consulter le **journal d'activité des messages** pour voir le jeton push. Il devrait ressembler à quelque chose comme `6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6`, une longue chaîne contenant un mélange de lettres et de chiffres. Si votre jeton push semble différent, vérifiez votre [code]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-4-register-push-tokens-with-braze) pour l'envoi des jetons push à Braze.
- Assurez-vous que votre profil de provisionnement push correspond à l'environnement que vous testez. Les certificats universels peuvent être configurés dans le tableau de bord de Braze pour envoyer vers l'environnement APNs de développement ou de production. L'utilisation d'un certificat de développement pour une application de production ou d'un certificat de production pour une application de développement ne fonctionnera pas.
 - Vérifiez que le jeton push que vous avez téléchargé vers Braze correspond au profil de provisionnement utilisé pour créer l'application à partir de laquelle le jeton push a été envoyé.

#### Le jeton d'appareil ne correspond pas au sujet {#device-token-not-for-topic}

Cette erreur indique que le certificat push de votre application et l'identifiant de bundle ne correspondent pas. Vérifiez que le certificat push que vous avez téléchargé vers Braze correspond au profil de provisionnement utilisé pour créer l'application à partir de laquelle le jeton push a été envoyé.

#### BadDeviceToken lors de l'envoi au jeton push {#baddevicetoken-sending-to-push-token}

Le `BadDeviceToken` est un code d'erreur APNs et ne provient pas de Braze. Plusieurs raisons peuvent expliquer cette réponse, notamment les suivantes :

{% multi_lang_include developer_guide/push_notifications/invalid_push_token_reasons.md %}

## Problèmes après la distribution des notifications push {#issues-after-push-delivery}

Pour ajouter une vérification de la gestion des notifications push de votre application, implémentez des [tests unitaires pour les notifications push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/unit_tests).

### Les clics sur les notifications push ne sont pas enregistrés {#push-clicks-not-logged}

- Si cela ne se produit que sur iOS 10, assurez-vous d'avoir suivi les étapes d'intégration des notifications push pour [iOS 10]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-5-enable-push-handling).
- Braze ne gère pas les notifications push reçues silencieusement au premier plan (par exemple, le comportement par défaut des notifications push au premier plan avant le framework `UserNotifications`). Cela signifie que les liens ne seront pas ouverts et que les clics sur les notifications push ne seront pas enregistrés. Si votre application n'a pas encore intégré le framework `UserNotifications`, Braze ne gérera pas les notifications push lorsque l'état de l'application est `UIApplicationStateActive`. Vous devez vous assurer que votre application ne retarde pas les appels à nos [méthodes de gestion des notifications push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-5-enable-push-handling) ; sinon, le SDK iOS pourrait traiter les notifications push comme des événements push silencieux au premier plan et ne pas les gérer.

#### Les liens web issus des clics sur les notifications push ne s'ouvrent pas {#web-links-from-push-clicks-not-opening}

iOS 9+ exige que les liens soient conformes à l'ATS pour être ouverts dans les vues web. Assurez-vous que vos liens web utilisent HTTPS. Consultez notre article sur la [conformité ATS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking#app-transport-security-ats) pour plus d'informations.

#### Les deep links issus des clics sur les notifications push ne s'ouvrent pas {#deep-links-from-push-clicks-not-opening}

La majeure partie du code qui gère les deep links gère également les ouvertures de notifications push. Tout d'abord, assurez-vous que les ouvertures de notifications push sont bien enregistrées. Si ce n'est pas le cas, [corrigez ce problème](#push-clicks-not-logged) (car la correction résout souvent aussi le traitement des liens).

Si les ouvertures sont enregistrées, vérifiez s'il s'agit d'un problème avec le deep link en général ou avec la gestion des clics push par deep link. Pour ce faire, testez si un deep link depuis un clic sur un message in-app fonctionne.

#### Peu ou pas d'ouvertures directes {#few-or-no-direct-opens}

Si au moins un utilisateur ouvre votre notification push iOS, mais que peu ou pas d'_ouvertures directes_ sont enregistrées dans Braze, il se peut qu'il y ait un problème avec votre [intégration SDK]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview). Gardez à l'esprit que les _ouvertures directes_ ne sont pas enregistrées pour les envois de test ou les notifications push silencieuses.

- Assurez-vous que les messages ne sont pas envoyés en tant que [notifications push silencieuses]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications#sending-silent-push-notifications). Le message doit contenir du texte dans le titre ou le corps pour ne pas être considéré comme silencieux.
- Revérifiez les étapes suivantes du [guide d'intégration des notifications push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration) :
   - [S'inscrire aux notifications push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-1-register-for-push-notifications-with-apns) : À chaque lancement de l'application, de préférence dans `application:didFinishLaunchingWithOptions:`, le code de l'étape 3 doit être exécuté. La propriété delegate de `UNUserNotificationCenter.current()` doit être assignée à un objet qui implémente `UNUserNotificationCenterDelegate` et contient la méthode `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:`.
   - [Activer la gestion des notifications push]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/push_notifications/integration#step-5-enable-push-handling) : Vérifiez que la méthode `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` a été implémentée.

### Les clics sur les images Push Stories ne produisent aucun effet {#push-story-image-clicks-do-nothing}

Cette section s'applique à l'intégration Push Stories du SDK Objective-C. Si vous utilisez le module `BrazePushStory` du SDK Swift, définissez `UNNotificationExtensionUserInteractionEnabled` sur `YES`. Consultez [Push Stories]({{site.baseurl}}/developer_guide/push_notifications/push_stories/?sdktab=swift).

Si appuyer sur une image Push Story n'ouvre pas l'action attendue, ouvrez le fichier `Info.plist` de l'extension Notification Content Extension et vérifiez que les clés correspondent à la [configuration des Push Stories]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/push_story) :

- `UNNotificationExtensionCategory` = `ab_cat_push_story_v2`
- `UNNotificationExtensionDefaultContentHidden` = `YES`
- `UNNotificationExtensionInitialContentSizeRatio` = `0.65`

Si `UNNotificationExtensionUserInteractionEnabled` est présent dans ce plist, supprimez-le. La configuration Push Stories en Objective-C n'inclut pas cette clé.