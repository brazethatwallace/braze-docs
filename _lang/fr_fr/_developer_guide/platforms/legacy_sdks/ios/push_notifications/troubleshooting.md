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

Le service de notification push Apple (APNs) est l'infrastructure d'Apple pour l'envoi de notifications push aux applications iOS et OS X. Voici la structure simplifiée du fonctionnement de l'activation des notifications push pour les appareils de vos utilisateurs et de la façon dont Braze peut leur envoyer des notifications push :

{% multi_lang_include developer_guide/push_notifications/push_registration_flow_steps.md %}

### Étape 1 : Configurer le certificat push et le profil de provisionnement {#step-1-configuring-the-push-certificate-and-provisioning-profile}

Lorsque vous développez votre application, créez un certificat SSL pour activer les notifications push. Ce certificat est inclus dans le profil de provisionnement avec lequel votre application est construite et doit également être téléversé dans le tableau de bord de Braze. Le certificat permet à Braze d'indiquer aux APNs que nous sommes autorisés à envoyer des notifications push en votre nom.

Il existe deux types de [profils de provisionnement](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html) et de certificats : développement et distribution. Nous recommandons d'utiliser uniquement les profils et certificats de distribution pour éviter toute confusion. Si vous choisissez d'utiliser des profils et certificats différents pour le développement et la distribution, assurez-vous que le certificat téléversé dans le tableau de bord correspond au profil de provisionnement que vous utilisez actuellement.

{% alert warning %}
Ne modifiez pas l'environnement du certificat push (développement versus production). Changer le certificat push vers le mauvais environnement peut entraîner la suppression accidentelle du jeton push de vos utilisateurs, les rendant injoignables par notification push.
{% endalert %}

#### Étape 2 : Les appareils s'enregistrent auprès des APNs et fournissent à Braze les jetons push {#step-2-devices-register-for-apns-and-provide-braze-with-push-tokens}

Lorsque les utilisateurs ouvrent votre application, ils seront invités à accepter les notifications push. S'ils acceptent cette invite, les APNs génèreront un jeton push pour cet appareil particulier. Le SDK iOS enverra immédiatement et de manière asynchrone le jeton push pour les applications utilisant la [politique de vidage automatique]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/advanced_use_cases/fine_network_traffic_control#automatic-request-processing) par défaut. Une fois qu'un jeton push est associé à un utilisateur, celui-ci apparaîtra comme « Push enregistré » dans le tableau de bord sur son profil utilisateur sous l'onglet **Engagement** et sera éligible pour recevoir des notifications push provenant de Campaigns Braze.

{% alert note %}
À partir de Xcode 14, vous pouvez tester les notifications push distantes sur un simulateur iOS.
{% endalert %}

#### Étape 3 : Lancer une Campaign push Braze {#step-3-launching-a-braze-push-campaign}

Lorsqu'une Campaign push est lancée, Braze envoie des requêtes aux APNs pour distribuer votre message. Braze utilisera le certificat SSL push téléversé dans le tableau de bord pour s'authentifier et vérifier que nous sommes autorisés à envoyer des notifications push aux jetons push fournis. Si un appareil est en ligne, la notification devrait être reçue peu après l'envoi de la Campaign. Notez que Braze définit la [date d'expiration](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607) APNs par défaut des notifications à 30 jours.

#### Étape 4 : Supprimer les jetons invalides {#step-4-removing-invalid-tokens}

Si les [APNs](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) nous informent que certains des jetons push auxquels nous tentions d'envoyer un message sont invalides, nous supprimons ces jetons des profils utilisateur auxquels ils étaient associés.

## Utilisation des journaux d'erreurs push {#utilizing-the-push-error-logs}

Braze fournit un journal des erreurs de notification push dans le **Journal d'activité des messages**. Ce journal d'erreurs contient une variété d'avertissements qui peuvent être très utiles pour identifier pourquoi vos campagnes ne fonctionnent pas comme prévu. Sélectionner un message d'erreur vous redirige vers la documentation pertinente pour vous aider à résoudre un incident particulier.

![Journaux d'erreurs push affichant l'heure de l'erreur, le nom de l'application, le canal, le type d'erreur et le message d'erreur.]({% image_buster /assets/img_archive/message_activity_log.png %})

Parmi les erreurs courantes que vous pourriez voir ici figurent des notifications spécifiques aux utilisateurs, telles que [« Received Unregistered Sending to Push Token »](#received-unregistered-sending).

De plus, Braze fournit également un journal des modifications push sur le profil utilisateur sous l'onglet **Engagement**. Ce journal fournit des informations sur le comportement d'inscription aux notifications push, telles que l'invalidation des jetons, les erreurs d'inscription push, les jetons transférés à de nouveaux utilisateurs, etc.

![Exemple animé de Content Card.]({% image_buster /assets/img_archive/push_changelog.gif %}){: style="max-width:50%;" }

## Problèmes d'inscription aux notifications push {#push-registration-issues}

Pour ajouter une vérification à la logique d'inscription aux notifications push de votre application, implémentez les [tests unitaires push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/unit_tests).

### Aucune invite d'inscription aux notifications push {#no-push-registration-prompt}

Si l'application ne vous invite pas à vous inscrire aux notifications push, il y a probablement un problème avec votre intégration d'inscription aux notifications push. Assurez-vous d'avoir suivi notre [documentation]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration) et d'avoir correctement intégré notre inscription aux notifications push. Vous pouvez également placer des points d'arrêt dans votre code pour vous assurer que le code d'inscription aux notifications push s'exécute.

#### Aucun utilisateur « inscrit aux notifications push » n'apparaît dans le tableau de bord {#no-push-registered-users-showing-in-the-dashboard}

- Vérifiez que votre application vous invite à autoriser les notifications push. En général, cette invite apparaît lors de la première ouverture de l'application, mais elle peut être programmée pour apparaître ailleurs. Si elle n'apparaît pas là où elle devrait, le problème est probablement lié à la configuration de base des fonctionnalités push de votre application.
  - Vérifiez que les étapes de l'[intégration push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration) ont été complétées avec succès.
  - Vérifiez que le profil de provisioning avec lequel votre application a été compilée inclut les permissions pour les notifications push. Assurez-vous de télécharger tous les profils de provisioning disponibles depuis votre compte développeur Apple. Pour le confirmer, effectuez les étapes suivantes :
    1. Dans Xcode, accédez à **Preferences > Accounts** (ou utilisez le raccourci clavier <kbd>Command</kbd>+<kbd>,</kbd>).
    2. Sélectionnez l'identifiant Apple que vous utilisez pour votre compte développeur et cliquez sur **View Details**.
    3. Sur la page suivante, cliquez sur **<i class="fas fa-redo-alt"></i> Refresh** et confirmez que vous téléchargez bien tous les profils de provisioning disponibles.
- Vérifiez que vous avez [correctement activé la fonctionnalité push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration#step-2-enable-push-capabilities) dans votre application.
- Vérifiez que votre profil de provisioning push correspond à l'environnement dans lequel vous testez. Les certificats universels peuvent être configurés dans le tableau de bord de Braze pour envoyer vers l'environnement APN de développement ou de production. Utiliser un certificat de développement pour une application de production ou un certificat de production pour une application de développement ne fonctionnera pas.
- Vérifiez que vous appelez notre méthode `registerPushToken` en plaçant un point d'arrêt dans votre code.
- Vérifiez que vous êtes sur un appareil (les notifications push ne fonctionnent pas sur un simulateur) et que vous disposez d'une bonne connectivité réseau.

## Les appareils ne reçoivent pas de notifications push {#devices-not-receiving-push-notifications}

### Les utilisateurs ne sont plus « push registered » après l'envoi d'une notification push {#users-no-longer-push-registered-after-sending-a-push-notification}

Cela indique probablement que l'utilisateur avait un jeton push invalide. Cela peut se produire pour plusieurs raisons :

#### Incompatibilité entre le certificat du tableau de bord et celui de l'application {#dashboard-and-app-certificate-mismatch}

Si le certificat push que vous avez téléchargé dans le tableau de bord n'est pas le même que celui du profil de provisionnement avec lequel votre application a été créée, les APN rejetteront le jeton. Vérifiez que vous avez téléchargé le bon certificat et effectuez une autre session dans l'application avant de tenter une nouvelle notification de test.

##### Désinstallations {#uninstalls}

Si un utilisateur a désinstallé votre application, son jeton push sera invalide et supprimé lors du prochain envoi.

##### Régénération de votre profil de provisionnement {#regenerating-your-provisioning-profile}

En dernier recours, repartir de zéro et créer un tout nouveau profil de provisionnement peut résoudre les erreurs de configuration qui surviennent lorsqu'on travaille avec plusieurs environnements, profils et applications en même temps. Il y a de nombreux « éléments en mouvement » dans la configuration des notifications push pour les applications iOS, il est donc parfois préférable de tout reprendre depuis le début. Cela vous aidera également à isoler le problème si vous devez continuer la résolution des problèmes.

#### Les utilisateurs sont toujours « push registered » après l'envoi d'une notification push {#users-still-push-registered-after-sending-a-push-notification}

##### L'application est au premier plan {#app-is-foregrounded}

Sur les versions d'iOS qui n'intègrent pas les notifications push via le framework `UserNotifications`, si l'application est au premier plan lorsque le message push est reçu, il ne sera pas affiché. Vous devez mettre l'application en arrière-plan sur vos appareils de test avant d'envoyer des messages de test.

##### Notification de test planifiée incorrectement {#test-notification-scheduled-incorrectly}

Vérifiez la planification que vous avez définie pour votre message de test. S'il est configuré pour une distribution selon le fuseau horaire local ou le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing), il se peut que vous n'ayez tout simplement pas encore reçu le message (ou que l'application ait été au premier plan lors de sa réception).

#### L'utilisateur n'est pas « push registered » pour l'application testée {#user-not-push-registered-for-the-app-being-tested}

Vérifiez le profil utilisateur de la personne à qui vous essayez d'envoyer un message de test. Sous l'onglet **Engagement**, une liste d'« applications pouvant recevoir des notifications push » devrait apparaître. Vérifiez que l'application à laquelle vous essayez d'envoyer des messages de test figure dans cette liste. Les utilisateurs apparaîtront comme « Push Registered » s'ils disposent d'un jeton push pour n'importe quelle application dans votre espace de travail, ce qui pourrait constituer un faux positif.

Les éléments suivants indiqueraient un problème d'inscription push ou que le jeton de l'utilisateur a été renvoyé à Braze comme invalide par les APN après un envoi :

![Un profil utilisateur affichant les paramètres de contact d'un utilisateur. Ici, vous pouvez voir pour quelles applications les notifications push sont enregistrées.]({% image_buster /assets/img_archive/registration_problem.png %}){: style="max-width:50%"}

## Les notifications push ne s'envoient pas {#push-messages-not-sending}

Pour résoudre les problèmes liés aux notifications push qui ne s'envoient pas, consultez [Résolution des problèmes des notifications push]({{site.baseurl}}/user_guide/channels/push/troubleshooting).

## Journal d'activité des messages – erreurs {#message-activity-log-errors}

### Réception non enregistrée lors de l'envoi au jeton push {#received-unregistered-sending}

- Assurez-vous que le jeton push envoyé à Braze depuis la méthode `[[Appboy sharedInstance] registerPushToken:]` est valide. Vous pouvez consulter le **journal d'activité des messages** pour voir le jeton push. Il devrait ressembler à quelque chose comme `6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6`, une longue chaîne de caractères contenant un mélange de lettres et de chiffres. Si votre jeton push semble différent, vérifiez votre [code]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration#step-4-register-push-tokens-with-braze) pour l'envoi des jetons push à Braze.
- Assurez-vous que votre profil de provisionnement push correspond à l'environnement que vous testez. Les certificats universels peuvent être configurés dans le tableau de bord de Braze pour envoyer vers l'environnement APNs de développement ou de production. Utiliser un certificat de développement pour une application de production ou un certificat de production pour une application de développement ne fonctionnera pas.
 - Vérifiez que le jeton push que vous avez téléchargé sur Braze correspond au profil de provisionnement que vous avez utilisé pour compiler l'application à partir de laquelle le jeton push a été envoyé.

#### Le jeton d'appareil ne correspond pas au sujet {#device-token-not-for-topic}

Cette erreur indique que le certificat push de votre application et l'identifiant de bundle ne correspondent pas. Vérifiez que le certificat push que vous avez téléchargé sur Braze correspond au profil de provisionnement utilisé pour compiler l'application à partir de laquelle le jeton push a été envoyé.

#### BadDeviceToken lors de l'envoi au jeton push {#baddevicetoken-sending-to-push-token}

Le `BadDeviceToken` est un code d'erreur APNs et ne provient pas de Braze. Plusieurs raisons peuvent expliquer cette réponse, notamment les suivantes :

{% multi_lang_include developer_guide/push_notifications/invalid_push_token_reasons.md %}

## Problèmes après la distribution des notifications push {#issues-after-push-delivery}

Pour ajouter une vérification de la gestion des notifications push de votre application, implémentez des [tests unitaires de notifications push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/unit_tests).

### Les clics sur les notifications push ne sont pas enregistrés {#push-clicks-not-logged}

- Si cela ne se produit que sur iOS 10, assurez-vous d'avoir suivi les étapes d'intégration des notifications push pour [iOS 10]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration#step-5-enable-push-handling).
- Braze ne gère pas les notifications push reçues silencieusement au premier plan (par exemple, le comportement par défaut des notifications push au premier plan avant le framework `UserNotifications`). Cela signifie que les liens ne seront pas ouverts et que les clics sur les notifications push ne seront pas enregistrés. Si votre application n'a pas encore intégré le framework `UserNotifications`, Braze ne gérera pas les notifications push lorsque l'état de l'application est `UIApplicationStateActive`. Vous devez vous assurer que votre application ne retarde pas les appels à nos [méthodes de gestion des notifications push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration#step-5-enable-push-handling) ; sinon, le SDK iOS peut traiter les notifications push comme des événements push silencieux au premier plan et ne pas les gérer.

#### Les liens web issus des clics sur les notifications push ne s'ouvrent pas {#web-links-from-push-clicks-not-opening}

iOS 9+ exige que les liens soient conformes à l'ATS pour être ouverts dans les vues web. Assurez-vous que vos liens web utilisent HTTPS. Consultez notre article sur la [conformité ATS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/advanced_use_cases/linking#app-transport-security-ats) pour plus d'informations.

#### Les deep links issus des clics sur les notifications push ne s'ouvrent pas {#deep-links-from-push-clicks-not-opening}

La plupart du code qui gère les deep links gère également les ouvertures de notifications push. Tout d'abord, assurez-vous que les ouvertures de notifications push sont bien enregistrées. Si ce n'est pas le cas, [corrigez ce problème](#push-clicks-not-logged) (car la correction résout souvent aussi la gestion des liens).

Si les ouvertures sont enregistrées, vérifiez s'il s'agit d'un problème avec le deep link en général ou avec la gestion des clics de deep link via les notifications push. Pour ce faire, testez si un deep link à partir d'un clic sur un message in-app fonctionne.

#### Peu ou pas d'ouvertures directes {#few-or-no-direct-opens}

Si au moins un utilisateur ouvre votre notification push iOS, mais que peu ou pas d'*ouvertures directes* sont enregistrées dans Braze, il se peut qu'il y ait un problème avec votre [intégration SDK]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview). Gardez à l'esprit que les *ouvertures directes* ne sont pas enregistrées pour les envois de test ou les notifications push silencieuses.

- Assurez-vous que les messages ne sont pas envoyés en tant que [notifications push silencieuses]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/silent_push_notifications#sending-silent-push-notifications). Le message doit contenir du texte dans le titre ou le corps pour ne pas être considéré comme silencieux.
- Vérifiez à nouveau les étapes suivantes du [guide d'intégration des notifications push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration) :
   - [S'inscrire aux notifications push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration#step-3-register-for-push-notifications) : À chaque lancement de l'application, de préférence dans `application:didFinishLaunchingWithOptions:`, le code de l'étape 3 doit être exécuté. La propriété delegate de `UNUserNotificationCenter.current()` doit être attribuée à un objet qui implémente `UNUserNotificationCenterDelegate` et contient la méthode `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:`.
   - [Activer la gestion des notifications push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration#step-5-enable-push-handling) : Vérifiez que la méthode `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` a été implémentée.

### Les clics sur les images des Push Stories ne font rien {#push-story-image-clicks-do-nothing}

Cette section s'applique à l'intégration Push Story du SDK Objective-C. Si vous utilisez le module `BrazePushStory` du SDK Swift, définissez `UNNotificationExtensionUserInteractionEnabled` sur `YES`. Consultez [Push Stories]({{site.baseurl}}/developer_guide/push_notifications/push_stories/?sdktab=swift).

Si le fait d'appuyer sur une image Push Story n'ouvre pas l'action attendue, ouvrez le `Info.plist` de l'extension Notification Content Extension et vérifiez que les clés correspondent à la [configuration de Push Story]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/push_story) :

- `UNNotificationExtensionCategory` = `ab_cat_push_story_v2`
- `UNNotificationExtensionDefaultContentHidden` = `YES`
- `UNNotificationExtensionInitialContentSizeRatio` = `0.65`

Si `UNNotificationExtensionUserInteractionEnabled` figure dans ce plist, supprimez-le. La configuration Push Story en Objective-C n'inclut pas cette clé.