## Comprendre le flux de travail Braze/APNs {#understanding-the-brazeapns-workflow}

Le service Apple Push Notification (APNs) est l'infrastructure permettant d'envoyer des notifications push aux applications fonctionnant sur les plateformes Apple. Voici la structure simplifiée du fonctionnement des notifications push pour les appareils de vos utilisateurs et de la manière dont Braze peut leur envoyer des notifications push :

1. Vous configurez le certificat push et le profil de provisionnement
2. Les appareils s'enregistrent auprès des APNs et fournissent à Braze les jetons push
3. Vous lancez une Campaign push via Braze
4. Braze supprime les jetons invalides

### Étape 1 : Configurer le certificat push et le profil de provisionnement {#step-1-configuring-the-push-certificate-and-provisioning-profile}

Lors du développement de votre application, vous devrez créer un certificat SSL pour activer les notifications push. Ce certificat sera inclus dans le profil de provisionnement avec lequel votre application est créée et devra également être téléchargé sur le tableau de bord de Braze. Le certificat permet à Braze d'indiquer aux APNs que nous sommes autorisés à envoyer des notifications push en votre nom.

Il existe deux types de [profils de provisionnement](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html) et de certificats : développement et distribution. Nous recommandons d'utiliser uniquement les profils et certificats de distribution afin d'éviter toute confusion. Si vous choisissez d'utiliser des profils et certificats différents pour le développement et la distribution, assurez-vous que le certificat téléchargé sur le tableau de bord correspond au profil de provisionnement que vous utilisez actuellement.

{% alert warning %}
Ne modifiez pas l'environnement du certificat push (développement versus production). Changer le certificat push vers le mauvais environnement peut entraîner la suppression accidentelle du jeton push de vos utilisateurs, les rendant injoignables par notification push.
{% endalert %}

### Étape 2 : Les appareils s'enregistrent auprès des APNs et fournissent à Braze les jetons push {#step-2-devices-register-for-apns-and-provide-braze-with-push-tokens}

Lorsque les utilisateurs ouvrent votre application, ils sont invités à accepter les notifications push. S'ils acceptent cette invite, les APNs génèrent un jeton push pour cet appareil particulier. Le SDK Swift enverra immédiatement et de manière asynchrone le jeton push pour les applications utilisant la [politique de vidage automatique]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/fine_network_traffic_control#automatic-request-processing) par défaut. Une fois qu'un jeton push est associé à un utilisateur, celui-ci apparaîtra comme « Push Registered » dans le tableau de bord sur son profil utilisateur sous l'onglet **Engagement** et sera éligible pour recevoir des notifications push des Campaigns Braze.

{% alert note %}
À partir de macOS 13, sur certains appareils, vous pouvez tester les notifications push sur un simulateur iOS 16 fonctionnant sur Xcode 14. Pour plus de détails, consultez les [Notes de version de Xcode 14](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes).
{% endalert %}

#### Considérations pour la génération de jetons push {#considerations-for-push-token-generation}

- Si les utilisateurs installent votre application sur un autre appareil, un autre jeton sera créé et capturé de la même manière.
- Si les utilisateurs réinstallent votre application, un nouveau jeton sera généré et transmis à Braze. Cependant, le jeton original peut encore être enregistré comme valide par les APNs et Braze.
- Si les utilisateurs désinstallent votre application, Braze n'en est pas immédiatement informé et le jeton apparaîtra toujours comme valide jusqu'à ce qu'il soit retiré par les APNs.
- À un moment donné, les APNs retireront les anciens jetons. Braze n'a aucun contrôle ni visibilité sur ce processus.

### Étape 3 : Lancer une Campaign push via Braze {#step-3-launching-a-braze-push-campaign}

Lorsqu'une Campaign push est lancée, Braze envoie des requêtes aux APNs pour distribuer votre message. Plus précisément, les requêtes sont transmises aux APNs pour chaque jeton push valide actuel, sauf si l'option **Send to a user's most recent device** est sélectionnée. Après que Braze a reçu une réponse positive des APNs, une réception réussie est enregistrée dans le profil utilisateur, bien que l'utilisateur puisse ne pas avoir reçu le message réel pour les raisons suivantes :
- Son appareil est éteint.
- Son appareil n'est pas connecté à Internet (Wi-Fi ou réseau cellulaire).
- Il a récemment désinstallé l'application.

Braze utilisera le certificat push SSL téléchargé dans le tableau de bord pour s'authentifier et vérifier que nous sommes autorisés à envoyer des notifications push aux jetons push fournis. Si un appareil est en ligne, la notification devrait être reçue peu après l'envoi de la Campaign. Notez que Braze définit la [date d'expiration](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607) APNs par défaut des notifications à 30 jours.

### Étape 4 : Supprimer les jetons invalides {#step-4-removing-invalid-tokens}

Si les [APNs](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) nous informent que l'un des jetons push auxquels nous tentions d'envoyer un message est invalide, nous supprimons ces jetons des profils utilisateurs auxquels ils étaient associés.

{% alert note %}
Il est normal que les APNs renvoient initialement un statut de succès même si un jeton devient non enregistré, car les APNs ne signalent pas immédiatement les événements d'invalidation de jetons. Les APNs retardent intentionnellement le renvoi d'un statut `410` pour les jetons invalides selon un calendrier aléatoire, conçu pour protéger la confidentialité des utilisateurs et empêcher le suivi des désinstallations d'applications. Vous pouvez continuer à envoyer des notifications à un jeton non enregistré en toute sécurité jusqu'à ce que les APNs renvoient un statut `410`.
{% endalert %}

## Utilisation des journaux d'erreurs push {#using-the-push-error-logs}

Le [Journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) vous permet de consulter tous les messages (en particulier les messages d'erreur) associés à vos Campaigns et à vos envois, y compris les erreurs de notifications push. Ce journal d'erreurs fournit divers avertissements qui peuvent être très utiles pour identifier pourquoi vos Campaigns ne fonctionnent pas comme prévu. En cliquant sur un message d'erreur, vous serez redirigé vers la documentation pertinente pour vous aider à résoudre un incident particulier.

![Journaux d'erreurs push affichant l'heure de l'erreur, le nom de l'application, le canal, le type d'erreur et le message d'erreur.]({% image_buster /assets/img_archive/message_activity_log.png %})

Les erreurs courantes que vous pourriez voir ici incluent des notifications spécifiques à l'utilisateur, telles que [« Received Unregistered Sending to Push Token »](#swift_received-unregistered-sending).

De plus, Braze fournit également un journal des modifications push sur le profil utilisateur, sous l'onglet **Engagement**. Ce journal donne un aperçu du comportement d'inscription push, comme l'invalidation des jetons, les erreurs d'inscription push, les jetons transférés à de nouveaux utilisateurs, etc.

![Onglet Engagement du profil utilisateur Braze affichant le journal des modifications de l'inscription push.]({% image_buster /assets/img_archive/push_changelog.gif %}){: style="max-width:50%;" }

### Erreurs du journal d'activité des messages {#message-activity-log-errors}

#### Received unregistered sending to push token {#received-unregistered-sending}

- Assurez-vous que le jeton push envoyé à Braze depuis la méthode `AppDelegate.braze?.notifications.register(deviceToken:)` est valide. Vous pouvez consulter le **Journal d'activité des messages** pour voir le jeton push. Il devrait ressembler à quelque chose comme `6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6`, une longue chaîne contenant un mélange de lettres et de chiffres. Si votre jeton push semble différent, vérifiez votre [code]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-4-register-push-tokens-with-braze) pour l'envoi des jetons push à Braze.
- Assurez-vous que votre profil de provisionnement push correspond à l'environnement que vous testez. Les certificats universels peuvent être configurés dans le tableau de bord de Braze pour envoyer vers l'environnement APNs de développement ou de production. Utiliser un certificat de développement pour une application de production ou un certificat de production pour une application de développement ne fonctionnera pas.
 - Vérifiez que le jeton push que vous avez téléchargé sur Braze correspond au profil de provisionnement utilisé pour compiler l'application à partir de laquelle vous avez envoyé le jeton push.

#### Device token not for topic

APNs renvoie `DeviceTokenNotForTopic` (statut HTTP 400) lorsque le jeton push ne correspond pas au topic (identifiant de bundle) configuré pour vos identifiants. Braze peut afficher cela dans le **Journal d'activité des messages** ou dans les journaux de distribution push sous la forme `DeviceTokenNotForTopic`.

Pour résoudre cette incohérence :

1. Confirmez que l'**identifiant de bundle** de l'application correspond à l'**App Bundle ID** dans Braze (**Paramètres** > **Paramètres de l'application** > **Paramètres des notifications push**).
2. Vérifiez que le profil de provisionnement utilisé pour compiler l'application inclut la capacité push pour cet identifiant de bundle.
3. Confirmez que les identifiants push téléchargés sur Braze correspondent à l'environnement de l'application (développement ou production).
4. Pour les clés `.p8`, vérifiez que le **Team ID** et le **Key ID** dans Braze correspondent à votre compte Apple Developer.
5. Téléchargez à nouveau une clé `.p8` ou un certificat `.p12` valide si les identifiants ont été renouvelés ou révoqués.

Préférez les clés d'authentification `.p8` lorsque c'est possible. Pour les types d'identifiants et les indicateurs de statut du tableau de bord, consultez [Migrer vers une clé d'authentification .p8]({{site.baseurl}}/user_guide/channels/push/troubleshooting#migrate-to-a-p8-authentication-key).

#### BadDeviceToken sending to push token

`BadDeviceToken` est un code d'erreur APNs et ne provient pas de Braze. Plusieurs raisons peuvent expliquer cette réponse, notamment les suivantes :

- L'application a reçu un jeton push invalide pour les identifiants téléchargés dans le tableau de bord.
- Les notifications push ont été désactivées pour cet espace de travail.
- L'utilisateur a refusé les notifications push.
- L'application a été désinstallée.
- Apple a actualisé le jeton push, ce qui a invalidé l'ancien jeton.
- L'application a été compilée pour un environnement de production, mais les identifiants push téléchargés sur Braze sont configurés pour un environnement de développement (ou inversement).

## Problèmes d'inscription aux notifications push {#push-registration-issues}

### Aucune invite d'inscription aux notifications push {#no-push-registration-prompt}

Si l'application ne vous invite pas à vous inscrire aux notifications push, il y a probablement un problème avec votre intégration de l'inscription push. Assurez-vous d'avoir suivi notre [documentation]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) et d'avoir correctement intégré notre inscription push. Vous pouvez également définir des points d'arrêt dans votre code pour vous assurer que le code d'inscription push s'exécute.

### Aucun utilisateur « inscrit aux notifications push » n'apparaît dans le tableau de bord (avant l'envoi de messages) {#no-push-registered-users-showing-in-the-dashboard-prior-to-sending-messages}

Assurez-vous que votre application est correctement configurée pour autoriser les notifications push. Voici les points de défaillance courants à vérifier :

- Vérifiez que votre application vous invite à autoriser les notifications push. En général, cette invite apparaît lors de la première ouverture de l'application, mais elle peut être programmée pour apparaître ailleurs. Si elle n'apparaît pas là où elle devrait, le problème vient probablement de la configuration de base des fonctionnalités push de votre application.
  - Vérifiez que les étapes de l'[intégration push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) ont été correctement réalisées.
  - Vérifiez que le profil de provisionnement avec lequel votre application a été compilée inclut les permissions pour les notifications push. Assurez-vous de récupérer tous les profils de provisionnement disponibles depuis votre compte Apple Developer. Pour confirmer cela, effectuez les étapes suivantes :
    1. Dans Xcode, accédez à **Preferences > Accounts** (ou utilisez le raccourci clavier <kbd>Command</kbd>+<kbd>,</kbd>).
    2. Sélectionnez l'Apple ID que vous utilisez pour votre compte développeur et cliquez sur **View Details**.
    3. Sur la page suivante, cliquez sur **<i class="fas fa-redo-alt"></i> Refresh** et confirmez que vous récupérez bien tous les profils de provisionnement disponibles.
- Vérifiez que vous avez [correctement activé la fonctionnalité push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-2-enable-push-capabilities) dans votre application.
- Vérifiez que votre profil de provisionnement push correspond à l'environnement dans lequel vous effectuez vos tests. Les certificats universels peuvent être configurés dans le tableau de bord de Braze pour envoyer vers l'environnement APN de développement ou de production. Utiliser un certificat de développement pour une application en production ou un certificat de production pour une application en développement ne fonctionnera pas.
- Vérifiez que vous appelez bien notre méthode `registerPushToken` en définissant un point d'arrêt dans votre code.
- Assurez-vous de tester sur un appareil physique (les notifications push ne fonctionnent pas sur un simulateur) et de disposer d'une bonne connectivité réseau.

## Notifications push envoyées mais non affichées sur les appareils des utilisateurs {#push-notifications-sent-but-not-displayed-on-users-devices}

### Les utilisateurs « enregistrés pour les notifications push » ne sont plus activés après l'envoi de messages {#push-registered-users-no-longer-enabled-after-sending-messages}

Cela indique probablement que l'utilisateur avait un jeton push invalide. Cela peut se produire pour plusieurs raisons :

#### Incompatibilité entre le certificat du tableau de bord et celui de l'application {#dashboard-and-app-certificate-mismatch}

Si le certificat push que vous avez téléchargé dans le tableau de bord n'est pas le même que celui du profil de provisionnement avec lequel votre application a été créée, les APN rejetteront le jeton. Vérifiez que vous avez téléchargé le bon certificat et effectué une autre session dans l'application avant de tenter une autre notification de test.

#### L'application a été désinstallée {#application-was-uninstalled}

Si un utilisateur a désinstallé votre application, son jeton push sera invalide et supprimé lors du prochain envoi.

#### Régénération de votre profil de provisionnement {#regenerating-your-provisioning-profile}

En dernier recours, recommencer à zéro et créer un tout nouveau profil de provisionnement peut résoudre les erreurs de configuration qui surviennent lorsque vous travaillez avec plusieurs environnements, profils et applications en même temps. Il y a de nombreux « éléments en mouvement » dans la configuration des notifications push, il est donc parfois préférable de recommencer depuis le début. Cela aidera également à isoler le problème si vous devez poursuivre la résolution des problèmes.

### Messages non distribués aux utilisateurs « enregistrés pour les notifications push » {#messages-not-delivered-to-push-registered-users}

#### L'application est au premier plan {#app-is-foregrounded}

Sur les versions iOS qui n'intègrent pas les notifications push via le framework `UserNotifications`, si l'application est au premier plan lorsque la notification push est reçue, elle ne sera pas affichée. Vous devez mettre l'application en arrière-plan sur vos appareils de test avant d'envoyer des messages de test.

#### Notification de test mal planifiée {#test-notification-scheduled-incorrectly}

Vérifiez la planification que vous avez définie pour votre message de test. S'il est configuré pour une distribution selon le fuseau horaire local ou le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing), il est possible que vous n'ayez tout simplement pas encore reçu le message (ou que l'application ait été au premier plan lors de sa réception).

### L'utilisateur n'est pas « enregistré pour les notifications push » pour l'application testée {#user-not-push-registered-for-the-app-being-tested}

Vérifiez le profil utilisateur de la personne à laquelle vous essayez d'envoyer un message de test. Sous l'onglet **Engagement**, il devrait y avoir une liste des « applications compatibles push ». Vérifiez que l'application à laquelle vous essayez d'envoyer des messages de test figure dans cette liste. Les utilisateurs apparaîtront comme « enregistrés pour les notifications push » s'ils ont un jeton push pour n'importe quelle application dans votre espace de travail, ce qui pourrait être un faux positif.

Les éléments suivants indiqueraient un problème d'enregistrement push ou que le jeton de l'utilisateur a été renvoyé à Braze comme invalide par les APN après un envoi push :

![Un profil utilisateur affichant les paramètres de contact d'un utilisateur. Sous Push, « No Apps » est affiché.]({% image_buster /assets/img_archive/registration_problem.png %}){: style="max-width:50%"}

## Les clics sur les notifications push ne sont pas enregistrés {#push-clicks-not-logged}

- Assurez-vous d'avoir suivi les [étapes de l'intégration push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-5-enable-push-handling).
- Braze ne gère pas les notifications push reçues silencieusement au premier plan (comportement push de premier plan par défaut avant le framework `UserNotifications`). Cela signifie que les liens ne seront pas ouverts et que les clics ne seront pas enregistrés. Si votre application n'a pas encore intégré le framework `UserNotifications`, Braze ne traitera pas les notifications push lorsque l'état de l'application est `UIApplicationStateActive`. Veillez à ce que votre application ne retarde pas les appels aux [méthodes de gestion push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-5-enable-push-handling) ; sinon, le SDK Swift risque de considérer les notifications push comme des événements push silencieux de premier plan et de ne pas les traiter.

## Les deep links ne fonctionnent pas {#deep-links-not-working}

Pour une résolution des problèmes complète sur tous les canaux — y compris les liens universels, les schémas personnalisés, l'e-mail et les fournisseurs tiers comme Branch or branche — consultez [Résolution des problèmes de deep linking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting).

### Les liens web issus des clics push ne s'ouvrent pas {#web-links-from-push-clicks-not-opening}

Les liens dans les notifications push doivent être conformes à l'ATS pour pouvoir être ouverts dans les vues web. Assurez-vous que vos liens web utilisent HTTPS. Pour plus d'informations, consultez [Conformité ATS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking#app-transport-security-ats).

### Les deep links issus des clics push ne s'ouvrent pas {#deep-links-from-push-clicks-not-opening}

La majeure partie du code qui gère les deep links gère également les ouvertures push. Commencez par vérifier que les ouvertures push sont bien enregistrées. Si ce n'est pas le cas, corrigez ce problème (car la correction résout souvent aussi la gestion des liens).

Si les ouvertures sont bien enregistrées, vérifiez s'il s'agit d'un problème avec le deep link en général ou avec la gestion du clic push pour le deep linking. Pour cela, testez si un deep link fonctionne lorsqu'il est déclenché par un clic sur un message in-app.