## Comprendre le flux de travail Braze/APNs {#understanding-the-brazeapns-workflow}

Le service Apple Push Notification (APNs) est l'infrastructure permettant d'envoyer des notifications push aux applications fonctionnant sur les plateformes d'Apple. Voici la structure simplifiée de la manière dont les notifications push sont activées pour les appareils de vos utilisateurs et la façon dont Braze peut leur envoyer des notifications push :

1. Vous configurez le certificat push et le profil de provisionnement
2. Les appareils s'enregistrent auprès des APNs et fournissent à Braze des jetons de notification push
3. Vous lancez une Campaign de notifications push Braze
4. Braze supprime les jetons non valides

### Étape 1 : Configurer le certificat push et le profil de provisionnement {#step-1-configuring-the-push-certificate-and-provisioning-profile}

Lors du développement de votre application, vous devez créer un certificat SSL pour activer les notifications push. Ce certificat sera inclus dans le profil de provisionnement avec lequel votre application est créée et devra également être téléchargé sur le tableau de bord de Braze. Le certificat permet à Braze de communiquer aux APNs que nous sommes autorisés à envoyer des notifications push en votre nom.

Il existe deux types de [profils de provisionnement](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html) et de certificats : développement et distribution. Nous vous recommandons d'utiliser uniquement des profils et des certificats de distribution pour éviter toute confusion. Si vous choisissez d'utiliser différents profils et certificats pour le développement et la distribution, assurez-vous que le certificat téléchargé sur le tableau de bord correspond au profil de provisionnement que vous utilisez actuellement.

{% alert warning %}
Ne modifiez pas l'environnement du certificat push (développement par rapport à la production). Modifier le certificat push pour un environnement incorrect peut entraîner la suppression accidentelle du jeton de notification push de vos utilisateurs, les rendant inaccessibles par notification push.
{% endalert %}

### Étape 2 : Les appareils s'enregistrent auprès des APNs et fournissent à Braze des jetons de notification push {#step-2-devices-register-for-apns-and-provide-braze-with-push-tokens}

Lorsque les utilisateurs ouvrent votre application, ils sont invités à accepter les notifications push. S'ils acceptent cette invite, les APNs génèrent un jeton de notification push pour cet appareil particulier. Le SDK Swift enverra immédiatement et de manière asynchrone le jeton push pour les applications utilisant la [politique de vidage automatique]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/fine_network_traffic_control#automatic-request-processing) par défaut. Une fois qu'un jeton push est associé à un utilisateur, celui-ci apparaîtra comme « Push Registered » dans le tableau de bord sur son profil utilisateur sous l'onglet **Engagement** et sera éligible pour recevoir des notifications push des Campaigns Braze.

{% alert note %}
À partir de macOS 13, sur certains appareils, vous pouvez tester les notifications push sur un simulateur iOS 16 fonctionnant sous Xcode 14. Pour plus de détails, reportez-vous aux [notes de version de Xcode 14](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes).
{% endalert %}

#### Considérations relatives à la génération de jetons push {#considerations-for-push-token-generation}

- Si les utilisateurs installent votre application sur un autre appareil, un autre jeton sera généré et capturé de la même manière.
- Si les utilisateurs réinstallent votre application, un nouveau jeton sera généré et transmis à Braze. Cependant, le jeton d'origine peut toujours être enregistré comme valide par les APNs et Braze.
- Si les utilisateurs désinstallent votre application, Braze n'en est pas immédiatement informé et le jeton continuera d'apparaître comme valide jusqu'à ce qu'il soit retiré par les APNs.
- À un moment donné, les APNs retireront les anciens jetons. Braze n'a aucun contrôle ni aucune visibilité sur ce point.

### Étape 3 : Lancer une Campaign de notifications push Braze {#step-3-launching-a-braze-push-campaign}

Lorsqu'une Campaign de notifications push est lancée, Braze effectue des requêtes auprès des APNs pour distribuer votre message. Plus précisément, les requêtes sont transmises aux APNs pour chaque jeton push valide actuel, sauf si l'option **Envoyer à l'appareil le plus récent de l'utilisateur** est sélectionnée. Une fois que Braze a reçu une réponse positive de la part des APNs, nous enregistrons une distribution réussie dans le profil utilisateur, même si celui-ci n'a pas reçu le message pour diverses raisons, notamment :
- Son appareil est éteint.
- Son appareil n'est pas connecté à Internet (Wi-Fi ou réseau cellulaire).
- Il a récemment désinstallé l'application.

Braze utilisera le certificat push SSL téléchargé dans le tableau de bord pour authentifier et vérifier que nous sommes autorisés à envoyer des notifications push aux jetons de notification push fournis. Si un appareil est en ligne, la notification devrait être reçue peu de temps après l'envoi de la Campaign. Notez que Braze fixe à 30 jours la [date d'expiration](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607) par défaut des APNs pour les notifications.

### Étape 4 : Supprimer les jetons non valides {#step-4-removing-invalid-tokens}

Si les [APNs](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) nous informent que l'un des jetons push auxquels nous avons tenté d'envoyer un message n'est pas valide, nous supprimons ces jetons des profils utilisateurs auxquels ils étaient associés.

{% alert note %}
Il est courant que les APNs renvoient initialement un statut de réussite même si un jeton n'est plus enregistré, car les APNs ne signalent pas immédiatement les événements d'invalidation des jetons. Les APNs retardent intentionnellement le renvoi d'un statut `410` pour les jetons non valides selon une planification aléatoire, afin de protéger la confidentialité des utilisateurs et d'empêcher le suivi des désinstallations d'applications. Vous pouvez continuer à envoyer des notifications à un jeton non enregistré en toute sécurité jusqu'à ce que les APNs renvoient un statut `410`.
{% endalert %}

## Utilisation des journaux d'erreurs push {#using-the-push-error-logs}

Le [journal d'activité des messages]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab) vous donne la possibilité de voir tous les messages (en particulier les messages d'erreur) associés à vos Campaigns et à vos envois, y compris les erreurs de notification push. Ce journal d'erreurs fournit de nombreux avertissements qui peuvent être très utiles pour identifier les raisons pour lesquelles vos Campaigns ne fonctionnent pas comme prévu. Cliquer sur un message d'erreur vous redirigera vers la documentation pertinente pour vous aider à résoudre un incident particulier.

![Journaux d'erreurs push affichant l'heure à laquelle l'erreur s'est produite, le nom de l'application, le canal, le type d'erreur et le message d'erreur.]({% image_buster /assets/img_archive/message_activity_log.png %})

Les erreurs courantes que vous pouvez voir ici comprennent des notifications spécifiques à l'utilisateur, telles que [« Received Unregistered Sending to Push Token »](#swift_received-unregistered-sending).

En outre, Braze fournit également un journal des modifications push sur le profil utilisateur, sous l'onglet **Engagement**. Ce journal des modifications donne un aperçu du comportement d'enregistrement des notifications push, comme l'invalidation des jetons, les erreurs d'enregistrement push, les jetons déplacés vers de nouveaux utilisateurs, etc.

![Journal des modifications de l'enregistrement push dans l'onglet Engagement du profil utilisateur Braze.]({% image_buster /assets/img_archive/push_changelog.gif %}){: style="max-width:50%;" }

### Erreurs du journal d'activité des messages {#message-activity-log-errors}

#### Réception d'un envoi non enregistré au jeton de notification push {#received-unregistered-sending}

- Assurez-vous que le jeton de notification push envoyé à Braze à partir de la méthode `AppDelegate.braze?.notifications.register(deviceToken:)` est valide. Vous pouvez consulter le **journal d'activité des messages** pour voir le jeton de notification push. Il devrait ressembler à quelque chose comme `6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6`, une longue chaîne de caractères contenant un mélange de lettres et de chiffres. Si votre jeton push semble différent, vérifiez votre [code]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-4-register-push-tokens-with-braze) d'envoi des jetons push à Braze.
- Vérifiez que votre profil de provisionnement push correspond à l'environnement dans lequel vous effectuez des tests. Les certificats universels peuvent être configurés dans le tableau de bord de Braze pour envoyer vers l'environnement de développement ou de production des APNs. L'utilisation d'un certificat de développement pour une application de production ou d'un certificat de production pour une application de développement ne fonctionnera pas.
 - Vérifiez que le jeton de notification push que vous avez téléchargé sur Braze correspond au profil de provisionnement que vous avez utilisé pour créer l'application à partir de laquelle vous avez envoyé le jeton de notification push.

#### Jeton d'appareil non destiné à la rubrique {#device-token-not-for-topic}

Les APNs renvoient `DeviceTokenNotForTopic` (statut HTTP 400) lorsque le jeton push ne correspond pas à la rubrique (bundle ID) configurée pour vos identifiants. Braze peut afficher cette erreur dans le **journal d'activité des messages** ou les journaux de distribution push sous la forme `DeviceTokenNotForTopic`.

Pour résoudre cette incohérence :

1. Confirmez que le **bundle ID** de l'application correspond au **App Bundle ID** dans Braze (**Paramètres** > **Paramètres des applications** > **Paramètres des notifications push**).
2. Vérifiez que le profil de provisionnement utilisé pour créer l'application inclut la capacité push pour ce bundle ID.
3. Confirmez que les identifiants push téléchargés sur Braze correspondent à l'environnement de l'application (développement par rapport à la production).
4. Pour les clés `.p8`, vérifiez que le **équipe ID** et le **Key ID** dans Braze correspondent à votre compte Apple Developer.
5. Téléchargez à nouveau une clé `.p8` ou un certificat `.p12` valide si les identifiants ont été renouvelés ou révoqués.

Préférez les clés d'authentification `.p8` lorsque c'est possible. Pour les types d'identifiants et les indicateurs de statut du tableau de bord, consultez [Migrer vers une clé d'authentification .p8]({{site.baseurl}}/user_guide/channels/push/troubleshooting#migrate-to-a-p8-authentication-key).

#### BadDeviceToken lors de l'envoi au jeton de notification push {#baddevicetoken-sending-to-push-token}

Le `BadDeviceToken` est un code d'erreur des APNs et ne provient pas de Braze. Cette réponse peut être renvoyée pour plusieurs raisons, notamment :

- L'application a reçu un jeton de notification push qui n'était pas valide pour les identifiants téléchargés sur le tableau de bord.
- La fonctionnalité push a été désactivée pour cet espace de travail.
- L'utilisateur s'est désinscrit des notifications push.
- L'application a été désinstallée.
- Apple a actualisé le jeton de notification push, ce qui a invalidé l'ancien jeton.
- L'application a été conçue pour un environnement de production, mais les identifiants push téléchargés sur Braze sont définis pour un environnement de développement (ou l'inverse).

## Problèmes d'enregistrement push {#push-registration-issues}

### Pas d'invite d'enregistrement push {#no-push-registration-prompt}

Si l'application ne vous invite pas à vous inscrire aux notifications push, il y a probablement un problème avec votre intégration d'enregistrement push. Assurez-vous d'avoir suivi notre [documentation]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) et d'avoir correctement intégré notre enregistrement push. Vous pouvez également définir des points d'arrêt dans votre code pour vous assurer que le code d'enregistrement push est en cours d'exécution.

### Aucun utilisateur « Push Registered » n'apparaît dans le tableau de bord (avant l'envoi des messages) {#no-push-registered-users-showing-in-the-dashboard-prior-to-sending-messages}

Assurez-vous que votre application est correctement configurée pour autoriser les notifications push. Les points de défaillance fréquents à vérifier comprennent :

- Vérifiez que votre application vous invite à autoriser les notifications push. En général, cette invite apparaît lors de votre première ouverture de l'application, mais elle peut être programmée pour apparaître ailleurs. Si elle n'apparaît pas là où elle le devrait, le problème est probablement lié à la configuration de base des capacités push de votre application.
  - Vérifiez que les étapes de l'[intégration push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) ont été effectuées avec succès.
  - Vérifiez que le profil de provisionnement avec lequel votre application a été créée inclut les autorisations pour les notifications push. Assurez-vous de récupérer tous les profils de provisionnement disponibles depuis votre compte développeur Apple. Pour confirmer cela, procédez comme suit :
    1. Dans Xcode, accédez à **Preferences > Accounts** (ou utilisez le raccourci clavier <kbd>Command</kbd>+<kbd>,</kbd>).
    2. Sélectionnez l'identifiant Apple que vous utilisez pour votre compte développeur et cliquez sur **View Details**.
    3. Sur la page suivante, cliquez sur **<i class="fas fa-redo-alt"></i> Refresh** et confirmez que vous récupérez tous les profils de provisionnement disponibles.
- Vérifiez que vous avez [correctement activé la capacité push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-2-enable-push-capabilities) dans votre application.
- Vérifiez que votre profil de provisionnement push correspond à l'environnement dans lequel vous effectuez des tests. Les certificats universels peuvent être configurés dans le tableau de bord de Braze pour envoyer vers l'environnement de développement ou de production des APNs. L'utilisation d'un certificat de développement pour une application de production ou d'un certificat de production pour une application de développement ne fonctionnera pas.
- Vérifiez que vous appelez notre méthode `registerPushToken` en définissant un point d'arrêt dans votre code.
- Assurez-vous que vous testez à l'aide d'un appareil (les notifications push ne fonctionnent pas sur un simulateur) et que vous disposez d'une bonne connectivité réseau.

## Notifications push envoyées mais non affichées sur les appareils des utilisateurs {#push-notifications-sent-but-not-displayed-on-users-devices}

### Les utilisateurs « Push Registered » ne sont plus activés après l'envoi de messages {#push-registered-users-no-longer-enabled-after-sending-messages}

Ceci indique probablement que l'utilisateur avait un jeton de notification push non valide. Cela peut se produire pour plusieurs raisons :

#### Incohérence entre le tableau de bord et le certificat de l'application {#dashboard-and-app-certificate-mismatch}

Si le certificat push que vous avez téléchargé dans le tableau de bord n'est pas le même que celui du profil de provisionnement avec lequel votre application a été créée, les APNs rejetteront le jeton. Vérifiez que vous avez téléchargé le bon certificat et terminé une autre session dans l'application avant de tenter une autre notification de test.

#### L'application a été désinstallée {#application-was-uninstalled}

Si un utilisateur a désinstallé votre application, son jeton de notification push sera invalide et supprimé lors du prochain envoi.

#### Régénération de votre profil de provisionnement {#regenerating-your-provisioning-profile}

En dernier recours, repartir de zéro et créer un tout nouveau profil de provisionnement peut éliminer les erreurs de configuration résultant de l'utilisation simultanée de plusieurs environnements, profils et applications. La mise en place des notifications push comporte de nombreuses « pièces mobiles », c'est pourquoi il est parfois préférable de recommencer depuis le début. Cela permettra également d'isoler le problème si vous devez poursuivre la résolution des problèmes.

### Messages non distribués aux utilisateurs « Push Registered » {#messages-not-delivered-to-push-registered-users}

#### L'application est au premier plan {#app-is-foregrounded}

Sur les versions iOS qui n'intègrent pas les notifications push via le framework `UserNotifications`, si l'application est au premier plan lorsque le message push est reçu, il ne s'affichera pas. Vous devez mettre l'application en arrière-plan sur vos appareils de test avant d'envoyer des messages de test.

#### Notification de test planifiée de manière incorrecte {#test-notification-scheduled-incorrectly}

Vérifiez la planification que vous avez définie pour votre message de test. S'il est configuré pour une distribution par fuseau horaire local ou avec le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing), il se peut que vous n'ayez pas encore reçu le message (ou que l'application ait été au premier plan au moment de sa réception).

### L'utilisateur n'est pas « Push Registered » pour l'application testée {#user-not-push-registered-for-the-app-being-tested}

Vérifiez le profil utilisateur de l'utilisateur auquel vous essayez d'envoyer un message de test. Sous l'onglet **Engagement**, il devrait y avoir une liste d'« applications pouvant recevoir des notifications push ». Vérifiez que l'application à laquelle vous essayez d'envoyer des messages de test figure dans cette liste. Les utilisateurs apparaîtront comme « Push Registered » s'ils ont un jeton push pour n'importe quelle application dans votre espace de travail, ce qui pourrait donc être un faux positif.

Ce qui suit indiquerait un problème avec l'enregistrement push ou que le jeton de l'utilisateur a été renvoyé à Braze comme invalide par les APNs après avoir été envoyé :

![Profil utilisateur affichant les paramètres de contact d'un utilisateur. Sous Notification push, « Pas d'application » s'affiche.]({% image_buster /assets/img_archive/registration_problem.png %}){: style="max-width:50%"}

## Les clics sur les notifications push ne sont pas enregistrés {#push-clicks-not-logged}

- Assurez-vous d'avoir suivi les [étapes de l'intégration push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-5-enable-push-handling).
- Braze ne gère pas les notifications push reçues silencieusement au premier plan (comportement push de premier plan par défaut avant le framework `UserNotifications`). Cela signifie que les liens ne seront pas ouverts et que les clics ne seront pas enregistrés. Si votre application n'a pas encore intégré le framework `UserNotifications`, Braze ne traitera pas les notifications push lorsque l'état de l'application est `UIApplicationStateActive`. Veillez à ce que votre application ne retarde pas les appels aux [méthodes de gestion push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-5-enable-push-handling) ; sinon, le SDK Swift risque de considérer les notifications push comme des événements push silencieux de premier plan et de ne pas les traiter.

## Les liens profonds ne fonctionnent pas {#deep-links-not-working}

Pour une résolution des problèmes complète sur tous les canaux — y compris les liens universels, les schémas personnalisés, les e-mails et les fournisseurs tiers tels que Branch — consultez [Résolution des problèmes de liens profonds]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting).

### Les liens web issus des clics sur les notifications push ne s'ouvrent pas {#web-links-from-push-clicks-not-opening}

Les liens dans les notifications push doivent être conformes à la norme ATS pour être ouverts dans des vues web. Assurez-vous que vos liens web utilisent HTTPS. Pour plus d'informations, consultez [Conformité ATS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking#app-transport-security-ats).

### Les liens profonds issus des clics sur les notifications push ne s'ouvrent pas {#deep-links-from-push-clicks-not-opening}

La plupart du code qui gère les liens profonds gère également les ouvertures push. Tout d'abord, assurez-vous que les ouvertures push sont enregistrées. Si ce n'est pas le cas, corrigez ce problème (car la correction permet souvent de résoudre la gestion des liens).

Si les ouvertures sont enregistrées, vérifiez s'il s'agit d'un problème avec le lien profond en général ou avec la gestion des clics push du lien profond. Pour ce faire, testez si un lien profond issu d'un clic sur un message in-app fonctionne.