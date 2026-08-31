---
page_order: 10.9
nav_title: Résolution des problèmes
article_title: Résolution des problèmes des notifications push pour le SDK Braze
description: "Diagnostiquez les problèmes de distribution et d'affichage des notifications push à l'aide d'un index de symptômes, d'un parcours d'investigation standard et de vérifications spécifiques au SDK par plateforme."
channel:
  - push notifications
---

# Résolution des problèmes des notifications push {#troubleshoot-push-notifications}

> Utilisez cette page pour diagnostiquer les problèmes de distribution et d'affichage des notifications push sur un appareil. Pour les vérifications de distribution côté tableau de bord (statut d'abonnement, segments, plafonds), consultez [Résolution des problèmes des notifications push]({{site.baseurl}}/user_guide/channels/push/troubleshooting).

Avant de déboguer, ajoutez-vous en tant qu'[utilisateur test]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#adding-test-users) et consultez [Envoi de messages de test]({{site.baseurl}}/developer_guide/push_notifications/sending_test_messages).

## Commencez ici : identifiez votre symptôme {#start-here-match-your-symptom}

Trouvez le comportement que vous observez dans le tableau, puis suivez les étapes de la section correspondante. Si vous ne savez pas quelle section s'applique, utilisez le [parcours d'investigation standard](#standard-investigation-path).

| Symptôme | Aller à |
| --- | --- |
| Notification push non reçue sur une plateforme | Sélectionnez l'onglet de votre SDK dans [Résolution des problèmes spécifiques à la plateforme](#platform-specific-troubleshooting) |
| Les sauts de ligne autour des étiquettes Liquid semblent incorrects lors de l'enregistrement | [Sauts de ligne dans les notifications push](#push-linebreaks) |
| Vérifications de distribution dans le tableau de bord (abonnement, segment, plafonds) | [Résolution des problèmes des notifications push]({{site.baseurl}}/user_guide/channels/push/troubleshooting) |
| Le deep link d'une notification push ne s'ouvre pas correctement | [Résolution des problèmes de deep linking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting) |
| Codes d'erreur courants des notifications push | [Messages d'erreur courants des notifications push]({{site.baseurl}}/user_guide/channels/push/push_error_codes) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Symptôme push SDK" }

## Parcours d'investigation standard {#standard-investigation-path}

Utilisez ce flux de travail pour chaque incident de notification push. Commencez à l'étape 1.

1. Confirmez que l'appareil dispose d'un jeton push valide et que l'autorisation push est accordée dans les paramètres de l'appareil.
2. Dans le tableau de bord, confirmez que l'utilisateur test correspond au [Segment]({{site.baseurl}}/user_guide/channels/push/troubleshooting#segment) de la Campaign ou du Canvas et qu'il ne fait pas partie du [groupe de contrôle]({{site.baseurl}}/user_guide/channels/push/troubleshooting#control-group-status).
3. Envoyez une [notification push de test]({{site.baseurl}}/developer_guide/push_notifications/sending_test_messages) à l'appareil de test.
4. [Activez la journalisation détaillée]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging), reproduisez le problème et consultez les instructions spécifiques à la plateforme dans votre [onglet SDK](#platform-specific-troubleshooting).
5. Si le problème persiste, contactez l'[Assistance Braze]({{site.baseurl}}/braze_support) en fournissant les journaux détaillés, la plateforme, la version du SDK et l'ID de la Campaign ou du Canvas.

## Résolution des problèmes spécifiques à chaque plateforme {#platform-specific-troubleshooting}

Sélectionnez l'onglet de votre SDK pour les vérifications de configuration et d'affichage spécifiques à la plateforme.

{% sdktabs %}
{% sdktab web %}
## Résolution des problèmes {#troubleshooting}

Si vous rencontrez des problèmes après la configuration des notifications push, tenez compte des éléments suivants :

- Les notifications push Web nécessitent que votre site soit en HTTPS.
- Tous les navigateurs ne peuvent pas recevoir des messages push. Assurez-vous que `braze.isPushSupported()` renvoie `true` dans le navigateur.
- Certains navigateurs, comme Firefox, n'affichent pas les images dans les notifications push. Pour plus de détails sur la compatibilité des navigateurs, consultez la [documentation MDN pour les images de Notification](https://developer.mozilla.org/en-US/docs/Web/API/Notification/image).
- Si un utilisateur a refusé l'accès push à un site, il ne sera plus invité à donner son autorisation tant qu'il n'aura pas supprimé le statut de refus dans les préférences de son navigateur.

{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab swift %}
## Comprendre le flux de travail Braze/APNs {#understanding-the-brazeapns-workflow}

L'Apple Push Notification service (APNs) est l'infrastructure d'envoi des notifications push aux applications fonctionnant sur les plateformes Apple. Voici la structure simplifiée de la manière dont les notifications push sont activées pour les appareils de vos utilisateurs et comment Braze peut leur envoyer des notifications push :

{% multi_lang_include developer_guide/push_notifications/push_registration_flow_steps.md %}

### Étape 1 : Configurer le certificat push et le profil de provisionnement {#step-1-configuring-the-push-certificate-and-provisioning-profile}

Pour développer votre application, créez un certificat SSL pour activer les notifications push. Ce certificat est inclus dans le profil de provisionnement avec lequel votre application est compilée et doit également être téléversé dans le tableau de bord de Braze. Le certificat permet à Braze d'informer APNs qu'il est autorisé à envoyer des notifications push en votre nom.

Il existe deux types de [profils de provisionnement](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html) et de certificats : développement et distribution. Nous recommandons d'utiliser uniquement les profils et certificats de distribution afin d'éviter toute confusion. Si vous choisissez d'utiliser des profils et certificats différents pour le développement et la distribution, assurez-vous que le certificat téléversé dans le tableau de bord correspond au profil de provisionnement que vous utilisez actuellement.

{% alert warning %}
Ne modifiez pas l'environnement du certificat push (développement versus production). Changer le certificat push vers le mauvais environnement peut entraîner la suppression accidentelle des jetons push de vos utilisateurs, les rendant inaccessibles par push.
{% endalert %}

### Étape 2 : Les appareils s'inscrivent auprès d'APNs et fournissent à Braze les jetons push {#step-2-devices-register-for-apns-and-provide-braze-with-push-tokens}

Lorsque les utilisateurs ouvrent votre application, ils sont invités à accepter les notifications push. S'ils acceptent cette invite, APNs génère un jeton push pour cet appareil particulier. Le SDK Swift envoie immédiatement et de manière asynchrone le jeton push pour les applications utilisant la [politique de vidage automatique]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/advanced_use_cases/fine_network_traffic_control#automatic-request-processing) par défaut. Une fois qu'un jeton push est associé à un utilisateur, celui-ci apparaît comme « Push Registered » dans le tableau de bord sur son profil utilisateur sous l'onglet **Engagement** et est éligible pour recevoir des notifications push depuis les Campaigns Braze.

{% alert note %}
À partir de macOS 13, sur certains appareils, vous pouvez tester les notifications push sur un simulateur iOS 16 fonctionnant sous Xcode 14. Pour plus de détails, consultez les [Notes de version de Xcode 14](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes).
{% endalert %}

#### Considérations pour la génération de jetons push {#considerations-for-push-token-generation}

- Si les utilisateurs installent votre application sur un autre appareil, Braze crée et capture un autre jeton de la même manière.
- Si les utilisateurs réinstallent votre application, le SDK génère un nouveau jeton et le transmet à Braze. Cependant, APNs et Braze peuvent toujours considérer le jeton d'origine comme valide.
- Si les utilisateurs désinstallent votre application, Braze ne reçoit pas immédiatement de notification, et le jeton apparaît toujours comme valide jusqu'à ce qu'APNs le retire.
- À un moment donné, APNs retire les anciens jetons. Braze ne contrôle pas ce processus et n'a pas de visibilité sur celui-ci.

### Étape 3 : Lancer une Campaign push Braze {#step-3-launching-a-braze-push-campaign}

Lorsqu'une Campaign push est lancée, Braze envoie des requêtes à APNs pour distribuer votre message. Plus précisément, les requêtes sont transmises à APNs pour chaque jeton push valide en cours, sauf si **Envoyer à l'appareil le plus récent d'un utilisateur** est sélectionné. Après que Braze a reçu une réponse positive d'APNs, Braze enregistre une distribution réussie sur le profil utilisateur, bien que l'utilisateur puisse ne pas avoir reçu le message effectif pour les raisons suivantes :
- Son appareil est éteint.
- Son appareil n'est pas connecté à Internet (Wi-Fi ou données cellulaires).
- Il a récemment désinstallé l'application.

Braze utilise le certificat push SSL téléversé dans le tableau de bord pour s'authentifier et vérifier qu'il est autorisé à envoyer des notifications push aux jetons push fournis. Si un appareil est en ligne, la notification devrait être reçue peu après l'envoi de la Campaign. Notez que Braze définit la [date d'expiration](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607) APNs par défaut des notifications à 30 jours.

### Étape 4 : Supprimer les jetons invalides {#step-4-removing-invalid-tokens}

Si [APNs](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) nous informe que l'un des jetons push auxquels nous tentions d'envoyer un message est invalide, nous supprimons ces jetons des profils utilisateurs auxquels ils étaient associés.

{% alert note %}
Il est normal qu'APNs renvoie initialement un statut de succès même si un jeton n'est plus enregistré, car APNs ne signale pas immédiatement les événements d'invalidation de jetons. APNs retarde intentionnellement le renvoi d'un statut `410` pour les jetons invalides selon un calendrier aléatoire, conçu pour protéger la vie privée des utilisateurs et empêcher le suivi des désinstallations d'applications. Vous pouvez continuer à envoyer des notifications en toute sécurité vers un jeton non enregistré jusqu'à ce qu'APNs renvoie un statut `410`.
{% endalert %}

## Utiliser les journaux d'erreurs push {#using-the-push-error-logs}

Le [Journal d'activité des messages]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab) vous permet de consulter tous les messages (en particulier les messages d'erreur) associés à vos Campaigns et envois, y compris les erreurs de notifications push. Ce journal d'erreurs fournit une variété d'avertissements qui peuvent être très utiles pour identifier pourquoi vos Campaigns ne fonctionnent pas comme prévu. Sélectionner un message d'erreur vous redirige vers la documentation pertinente pour vous aider à résoudre un incident particulier.

![Journaux d'erreurs push affichant l'heure de l'erreur, le nom de l'application, le canal, le type d'erreur et le message d'erreur.]({% image_buster /assets/img_archive/message_activity_log.png %})

Les erreurs courantes que vous pourriez voir ici incluent des notifications spécifiques à l'utilisateur, telles que [« Received Unregistered Sending to Push Token »](#swift_received-unregistered-sending).

De plus, Braze fournit également un journal des modifications push sur le profil utilisateur sous l'onglet **Engagement**. Ce journal donne un aperçu du comportement d'inscription push, comme l'invalidation de jetons, les erreurs d'inscription push, les jetons transférés à de nouveaux utilisateurs, etc.

![Onglet Engagement du profil utilisateur Braze affichant le journal des modifications d'inscription push.]({% image_buster /assets/img_archive/push_changelog.gif %}){: style="max-width:50%;" }

### Erreurs du journal d'activité des messages {#message-activity-log-errors}

#### « Received unregistered sending to push token » {#received-unregistered-sending}

- Assurez-vous que le jeton push envoyé à Braze depuis la méthode `AppDelegate.braze?.notifications.register(deviceToken:)` est valide. Vous pouvez consulter le **Journal d'activité des messages** pour voir le jeton push. Il devrait ressembler à quelque chose comme `6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6`, une longue chaîne contenant un mélange de lettres et de chiffres. Si votre jeton push semble différent, vérifiez votre [code]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-32-register-push-tokens-with-braze) pour l'envoi des jetons push à Braze.
- Assurez-vous que votre profil de provisionnement push correspond à l'environnement que vous testez. Les certificats universels peuvent être configurés dans le tableau de bord de Braze pour envoyer vers l'environnement APNs de développement ou de production. Utiliser un certificat de développement pour une application en production ou un certificat de production pour une application de développement ne fonctionnera pas.
 - Vérifiez que le jeton push que vous avez téléversé dans Braze correspond au profil de provisionnement utilisé pour compiler l'application depuis laquelle vous avez envoyé le jeton push.

#### « Device token not for topic » {#device-token-not-for-topic}

APNs renvoie `DeviceTokenNotForTopic` (statut HTTP 400) lorsque le jeton push ne correspond pas au topic (identifiant de bundle) configuré pour vos identifiants. Braze peut afficher cela dans le **Journal d'activité des messages** ou les journaux de distribution push comme `DeviceTokenNotForTopic`.

Pour résoudre l'incompatibilité :

1. Confirmez que l'**identifiant de bundle** de l'application correspond à l'**App Bundle ID** dans Braze (**Paramètres** > **Paramètres de l'application** > **Paramètres de notification push**).
2. Vérifiez que le profil de provisionnement utilisé pour compiler l'application inclut la capacité push pour cet identifiant de bundle.
3. Confirmez que les identifiants push téléversés dans Braze correspondent à l'environnement de l'application (développement versus production).
4. Pour les clés `.p8`, vérifiez que le **Team ID** et le **Key ID** dans Braze correspondent à votre compte Apple Developer.
5. Re-téléversez une clé `.p8` valide ou un certificat `.p12` si les identifiants ont été renouvelés ou révoqués.

Préférez les clés d'authentification `.p8` lorsque cela est possible. Pour les types d'identifiants et les indicateurs de statut du tableau de bord, consultez [Migrer vers une clé d'authentification .p8]({{site.baseurl}}/user_guide/channels/push/troubleshooting#migrate-to-a-p8-authentication-key).

#### « BadDeviceToken sending to push token » {#baddevicetoken-sending-to-push-token}

Le `BadDeviceToken` est un code d'erreur APNs et ne provient pas de Braze. Il peut y avoir plusieurs raisons pour lesquelles cette réponse est renvoyée, notamment les suivantes :

{% multi_lang_include developer_guide/push_notifications/invalid_push_token_reasons.md %}

## Problèmes d'inscription push {#push-registration-issues}

### Pas d'invite d'inscription push {#no-push-registration-prompt}

Si l'application ne vous invite pas à vous inscrire aux notifications push, il y a probablement un problème avec votre intégration de l'inscription push. Assurez-vous d'avoir suivi notre [documentation]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) et d'avoir correctement intégré l'inscription push. Vous pouvez également définir des points d'arrêt dans votre code pour vous assurer que le code d'inscription push s'exécute bien.

### Aucun utilisateur « push registered » n'apparaît dans le tableau de bord (avant l'envoi de messages) {#no-push-registered-users-showing-in-the-dashboard-prior-to-sending-messages}

Assurez-vous que votre application est correctement configurée pour autoriser les notifications push. Les points de défaillance courants à vérifier sont les suivants :

- Vérifiez que votre application vous invite à autoriser les notifications push. Généralement, cette invite apparaît lors de la première ouverture de l'application, mais elle peut être programmée pour apparaître ailleurs. Si elle n'apparaît pas là où elle devrait, le problème réside probablement dans la configuration de base des capacités push de votre application.
  - Vérifiez que les étapes d'[intégration push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) ont été accomplies avec succès.
  - Vérifiez que le profil de provisionnement avec lequel votre application a été compilée inclut les autorisations pour le push. Assurez-vous de télécharger tous les profils de provisionnement disponibles depuis votre compte développeur Apple. Pour confirmer cela, effectuez les étapes suivantes :
    1. Dans Xcode, accédez à **Preferences > Accounts** (ou utilisez le raccourci clavier <kbd>Command</kbd>+<kbd>,</kbd>).
    2. Sélectionnez l'Apple ID que vous utilisez pour votre compte développeur et cliquez sur **View Details**.
    3. Sur la page suivante, cliquez sur **<i class="fas fa-redo-alt"></i> Refresh** et confirmez que vous téléchargez tous les profils de provisionnement disponibles.
- Vérifiez que vous avez [correctement activé la capacité push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-2-enable-push-capabilities) dans votre application.
- Vérifiez que votre profil de provisionnement push correspond à l'environnement dans lequel vous testez. Les certificats universels peuvent être configurés dans le tableau de bord de Braze pour envoyer vers l'environnement APNs de développement ou de production. Utiliser un certificat de développement pour une application en production ou un certificat de production pour une application de développement ne fonctionnera pas.
- Vérifiez que vous appelez notre méthode `registerPushToken` en définissant un point d'arrêt dans votre code.
- Assurez-vous de tester avec un appareil (le push ne fonctionnera pas sur un simulateur) et de disposer d'une bonne connectivité réseau.

## Notifications push envoyées mais non affichées sur les appareils des utilisateurs {#push-notifications-sent-but-not-displayed-on-users-devices}

### Les utilisateurs « push registered » ne sont plus activés après l'envoi de messages {#push-registered-users-no-longer-enabled-after-sending-messages}

Cela indique probablement que l'utilisateur avait un jeton push invalide. Cela peut se produire pour plusieurs raisons :

#### Incompatibilité entre le certificat du tableau de bord et celui de l'application {#dashboard-and-app-certificate-mismatch}

Si le certificat push que vous avez téléversé dans le tableau de bord n'est pas le même que celui du profil de provisionnement avec lequel votre application a été compilée, APNs rejettera le jeton. Vérifiez que vous avez téléversé le bon certificat et effectuez une autre session dans l'application avant de tenter une autre notification de test.

#### L'application a été désinstallée {#application-was-uninstalled}

Si un utilisateur a désinstallé votre application, son jeton push sera invalide et supprimé lors du prochain envoi.

#### Régénérer votre profil de provisionnement {#regenerating-your-provisioning-profile}

En dernier recours, repartir de zéro et créer un tout nouveau profil de provisionnement peut résoudre les erreurs de configuration provenant du travail avec plusieurs environnements, profils et applications en même temps. Il y a beaucoup de « pièces mobiles » dans la configuration des notifications push, donc parfois il est préférable de recommencer depuis le début. Cela vous aidera également à isoler le problème si vous devez poursuivre la résolution des problèmes.

### Messages non distribués aux utilisateurs « push registered » {#messages-not-delivered-to-push-registered-users}

#### L'application est au premier plan {#app-is-foregrounded}

Sur les versions d'iOS qui n'intègrent pas le push via le framework `UserNotifications`, si l'application est au premier plan lorsque le message push est reçu, il ne sera pas affiché. Vous devez mettre l'application en arrière-plan sur vos appareils de test avant d'envoyer des messages de test.

#### Notification de test planifiée incorrectement {#test-notification-scheduled-incorrectly}

Vérifiez la planification que vous avez définie pour votre message de test. Si elle est configurée pour une distribution selon le fuseau horaire local ou avec le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing), il se peut que vous n'ayez simplement pas encore reçu le message (ou que l'application ait été au premier plan lors de la réception).

### L'utilisateur n'est pas « push registered » pour l'application testée {#user-not-push-registered-for-the-app-being-tested}

Vérifiez le profil de l'utilisateur auquel vous essayez d'envoyer un message de test. Sous l'onglet **Engagement**, il devrait y avoir une liste des « applications pushables ». Vérifiez que l'application à laquelle vous essayez d'envoyer des messages de test figure dans cette liste. Les utilisateurs apparaîtront comme « Push Registered » s'ils ont un jeton push pour n'importe quelle application dans votre espace de travail, ce qui pourrait constituer un faux positif.

Le scénario suivant indiquerait un problème avec l'inscription push ou que le jeton de l'utilisateur a été renvoyé à Braze comme invalide par APNs après l'envoi push :

![Un profil utilisateur affichant les paramètres de contact d'un utilisateur. Sous Push, « No Apps » est affiché.]({% image_buster /assets/img_archive/registration_problem.png %}){: style="max-width:50%"}

## Les clics push ne sont pas enregistrés {#push-clicks-not-logged}

- Assurez-vous d'avoir suivi les [étapes d'intégration push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-33-enable-push-handling).
- Braze ne gère pas les notifications push reçues silencieusement au premier plan (comportement push au premier plan par défaut avant le framework `UserNotifications`). Cela signifie que les liens ne seront pas ouverts et que les clics push ne seront pas enregistrés. Si votre application n'a pas encore intégré le framework `UserNotifications`, Braze ne gérera pas les notifications push lorsque l'état de l'application est `UIApplicationStateActive`. Assurez-vous que votre application ne retarde pas les appels aux [méthodes de gestion push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-33-enable-push-handling) ; sinon, le SDK Swift pourrait traiter les notifications push comme des événements push silencieux au premier plan et ne pas les gérer.

## Les deep links ne fonctionnent pas {#deep-links-not-working}

Pour une résolution des problèmes complète sur tous les canaux — y compris les liens universels, les schémas personnalisés, les e-mails et les fournisseurs tiers comme Branch — consultez [Résolution des problèmes de deep linking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting).

### Les liens Web issus des clics push ne s'ouvrent pas {#web-links-from-push-clicks-not-opening}

Les liens dans les notifications push doivent être conformes à ATS pour être ouverts dans les vues Web. Assurez-vous que vos liens Web utilisent HTTPS. Pour plus d'informations, consultez [Conformité ATS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/advanced_use_cases/linking#app-transport-security-ats).

### Les deep links issus des clics push ne s'ouvrent pas {#deep-links-from-push-clicks-not-opening}

La majeure partie du code qui gère les deep links gère également les ouvertures push. Tout d'abord, assurez-vous que les ouvertures push sont bien enregistrées. Si ce n'est pas le cas, corrigez ce problème (car la correction résout souvent également la gestion des liens).

Si les ouvertures sont enregistrées, vérifiez s'il s'agit d'un problème avec le deep link en général ou avec la gestion du clic push via deep link. Pour ce faire, testez si un deep link fonctionne depuis un clic sur un message in-app.

### Les appuis sur les images Push Story ne font rien {#push-story-image-taps-do-nothing}

Si le fait d'appuyer sur une image Push Story ne fait rien, ouvrez le fichier `Info.plist` de la Notification Content Extension et confirmez que `UNNotificationExtensionUserInteractionEnabled` est défini sur `YES`. Le module `BrazePushStory` du SDK Swift a besoin de cette clé pour que l'extension puisse recevoir les appuis. Consultez [Push Stories]({{site.baseurl}}/developer_guide/push_notifications/push_stories/?sdktab=swift).

{% endsdktab %}

{% sdktab fireos %}
{% multi_lang_include developer_guide/android/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab flutter %}
{% multi_lang_include developer_guide/flutter/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin) %}
## Résolution des problèmes

### Le push n'apparaît pas après la fermeture de l'application depuis le sélecteur de tâches {#push-doesnt-appear-after-app-is-closed-from-task-switcher}

Si vous constatez que les notifications push n'apparaissent plus après la fermeture de l'application depuis le sélecteur de tâches, votre application est probablement en mode Debug. .NET MAUI ajoute un échafaudage en mode Debug qui empêche les applications de recevoir des notifications push après que leur processus est arrêté. Si vous exécutez votre application en mode Release, vous devriez voir les notifications push même après la fermeture de l'application depuis le sélecteur de tâches.

### La fabrique de notifications personnalisée n'est pas configurée correctement {#custom-notification-factory-not-being-set-correctly}

Les fabriques de notifications personnalisées (et tous les délégués) doivent étendre [`Java.Lang.Object`](https://developer.xamarin.com/api/type/Android.Runtime.IJavaObject/) pour fonctionner correctement à travers la frontière C# et Java. Consultez la documentation [Xamarin](https://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/working_with_jni/#Implementing_Interfaces) sur l'implémentation des interfaces Java pour plus d'informations.

{% endsdktab %}
{% endsdktabs %}

## Sauts de ligne dans les notifications push {#push-linebreaks}

Lors de la rédaction de notifications push avec des étiquettes Liquid, les sauts de ligne adjacents aux étiquettes Liquid sont automatiquement supprimés avant l'envoi du message. Dans le [compositeur de notifications push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message), ces sauts de ligne sont réajoutés afin que votre message reste lisible pendant la modification. Si vous remarquez des sauts de ligne autour des étiquettes Liquid lors de l'enregistrement de votre message, il s'agit d'un comportement attendu.