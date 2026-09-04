## Limitation du débit {#rate-limits}

Les notifications push sont limitées en débit, alors n'hésitez pas à en envoyer autant que votre application en a besoin. iOS et les serveurs du service de notification push d'Apple (APNs) contrôleront la fréquence de livraison, et vous n'aurez pas de problèmes si vous en envoyez trop. Si vos notifications push sont limitées, elles peuvent être retardées jusqu'à la prochaine fois que l'appareil envoie un paquet de maintien de connexion ou reçoit une autre notification.

## Configuration des notifications push {#setting-up-push-notifications}

### Étape 1 : Téléverser votre jeton APNs {#step-1-upload-your-apns-token}

{% multi_lang_include developer_guide/swift/apns_token.md %}

### Étape 2 : Activer les capacités push {#step-2-enable-push-capabilities}

Dans Xcode, accédez à la section **Signing & Capabilities** de la cible principale de l'application et ajoutez la capacité de notifications push.

![La section « Signing & Capabilities » dans un projet Xcode.]({% image_buster /assets/img_archive/Enable_push_capabilities.png %})

### Étape 3 : Configurer la gestion des notifications push {#step-3-set-up-push-handling}

Vous pouvez utiliser le SDK Swift pour automatiser le traitement des notifications distantes reçues depuis Braze. Il s'agit de la méthode la plus simple pour gérer les notifications push et c'est la méthode de gestion recommandée.

{% tabs local %}
{% tab Automatique %}
#### Étape 3.1 : Activer l'automatisation dans la propriété push {#step-31-enable-automation-in-the-push-property}

Pour activer l'intégration push automatique, définissez la propriété `automation` de la configuration `push` sur `true` :

{% subtabs %}
{% subtab Swift %}
```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}", endpoint: "{YOUR-BRAZE-API-ENDPOINT}")
configuration.push.automation = true
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"{YOUR-BRAZE-API-KEY}" endpoint:@"{YOUR-BRAZE-API-ENDPOINT}"];
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
```

{% endsubtab %}
{% endsubtabs %}

Cela indique au SDK de :
- Enregistrer votre application pour les notifications push auprès du système.
- Demander l'autorisation des notifications push lors de l'initialisation.
- Fournir dynamiquement des implémentations pour les méthodes déléguées système liées aux notifications push.

{% alert note %}
Les étapes d'automatisation effectuées par le SDK sont compatibles avec les intégrations de gestion des notifications push préexistantes dans votre code. Le SDK automatise uniquement le traitement des notifications distantes reçues depuis Braze. Tout gestionnaire système implémenté pour traiter vos propres notifications distantes ou celles d'un autre SDK tiers continuera de fonctionner lorsque l'`automation` est activée.
{% endalert %}

{% alert warning %}
Le SDK doit être initialisé sur le thread principal pour activer l'automatisation des notifications push. L'initialisation du SDK doit avoir lieu avant que l'application n'ait fini de se lancer ou dans l'implémentation [`application(_:didFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) de votre AppDelegate.
Si votre application nécessite une configuration supplémentaire avant l'initialisation du SDK, veuillez consulter la page de documentation [Initialisation différée]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift#step-2-set-up-delayed-initialization-optional).
{% endalert %}

#### Étape 3.2 : Remplacer des configurations individuelles (facultatif) {#step-32-override-individual-configurations-optional}

Pour un contrôle plus précis, chaque étape d'automatisation peut être activée ou désactivée individuellement :

{% subtabs %}
{% subtab Swift %}

```swift
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = true
configuration.push.automation.requestAuthorizationAtLaunch = false
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
configuration.push.automation.requestAuthorizationAtLaunch = NO;
```

{% endsubtab %}
{% endsubtabs %}

Consultez [`Braze.Configuration.Push.Automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.class) pour toutes les options disponibles et [`automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.property) pour plus d'informations sur le comportement de l'automatisation.
{% endtab %}

{% tab Manuelle %}
{% alert note %}
Si vous dépendez des notifications push pour des comportements supplémentaires spécifiques à votre application, vous pourriez tout de même utiliser l'intégration push automatique au lieu de l'intégration manuelle des notifications push. La méthode [`subscribeToUpdates(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(_:)) offre un moyen d'être notifié des notifications distantes traitées par Braze.
{% endalert %}

#### Étape 3.1 : S'enregistrer pour les notifications push auprès des APNs {#step-31-register-for-push-notifications-with-apns}

Incluez l'exemple de code approprié dans la [méthode déléguée `application:didFinishLaunchingWithOptions:`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) de votre application afin que les appareils de vos utilisateurs puissent s'enregistrer auprès des APNs. Assurez-vous d'appeler tout le code d'intégration push sur le thread principal de votre application.

Braze fournit également des catégories push par défaut pour la prise en charge des boutons d'action push, qui doivent être ajoutées manuellement à votre code d'enregistrement push. Consultez les [boutons d'action push]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_customizing-push-categories) pour les étapes d'intégration supplémentaires.

Ajoutez le code suivant à la méthode `application:didFinishLaunchingWithOptions:` du délégué de votre application.

{% alert note %}
L'exemple de code suivant inclut l'intégration de l'authentification push provisoire (lignes 5 et 6). Si vous ne prévoyez pas d'utiliser l'autorisation provisoire dans votre application, vous pouvez supprimer les lignes de code qui ajoutent `UNAuthorizationOptionProvisional` aux options `requestAuthorization`.<br>Consultez les [options de notification iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options) pour en savoir plus sur l'authentification push provisoire.
{% endalert %}

{% subtabs %}
{% subtab Swift %}

```swift
application.registerForRemoteNotifications()
let center = UNUserNotificationCenter.current()
center.setNotificationCategories(Braze.Notifications.categories)
center.delegate = self
var options: UNAuthorizationOptions = [.alert, .sound, .badge]
if #available(iOS 12.0, *) {
  options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
}
center.requestAuthorization(options: options) { granted, error in
  print("Notification authorization, granted: \(granted), error: \(String(describing: error))")
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
[application registerForRemoteNotifications];
UNUserNotificationCenter *center = UNUserNotificationCenter.currentNotificationCenter;
[center setNotificationCategories:BRZNotifications.categories];
center.delegate = self;
UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
if (@available(iOS 12.0, *)) {
  options = options | UNAuthorizationOptionProvisional;
}
[center requestAuthorizationWithOptions:options
                      completionHandler:^(BOOL granted, NSError *_Nullable error) {
                        NSLog(@"Notification authorization, granted: %d, "
                              @"error: %@)",
                              granted, error);
}];
```

{% endsubtab %}
{% endsubtabs %}

{% alert warning %}
Vous devez assigner votre objet délégué en utilisant `center.delegate = self` de manière synchrone avant que votre application ne finisse de se lancer, de préférence dans `application:didFinishLaunchingWithOptions:`. Ne pas le faire peut empêcher votre application de recevoir les notifications push entrantes. Consultez la documentation Apple [`UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate) pour en savoir plus.
Si votre application appelle `wipeData()` et réactive ensuite le SDK Braze dans la même exécution de l'application, vous devez appeler à nouveau `registerForRemoteNotifications()` pour repeupler le jeton d'appareil utilisé par le SDK.
{% endalert %}

#### Étape 3.2 : Enregistrer les jetons push auprès de Braze {#step-32-register-push-tokens-with-braze}

Une fois l'enregistrement APNs terminé, transmettez le `deviceToken` résultant à Braze pour activer les notifications push pour l'utilisateur.

{% subtabs %}
{% subtab Swift %}

Ajoutez le code suivant à la méthode `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)` de votre application :

```swift
AppDelegate.braze?.notifications.register(deviceToken: deviceToken)
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

Ajoutez le code suivant à la méthode `application:didRegisterForRemoteNotificationsWithDeviceToken:` de votre application :

```objc
[AppDelegate.braze.notifications registerDeviceToken:deviceToken];
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
La méthode déléguée `application:didRegisterForRemoteNotificationsWithDeviceToken:` est appelée à chaque fois après l'appel de `application.registerForRemoteNotifications()`. <br><br>Si vous migrez vers Braze depuis un autre service push et que l'appareil de votre utilisateur est déjà enregistré auprès des APNs, cette méthode collectera les jetons des enregistrements existants lors du prochain appel, et les utilisateurs n'auront pas besoin de se réabonner aux notifications push.
{% endalert %}

#### Étape 3.3 : Activer la gestion des notifications push {#step-33-enable-push-handling}

Ensuite, transmettez les notifications push reçues à Braze. Cette étape est nécessaire pour l'enregistrement des données analytiques push et la gestion des liens. Assurez-vous d'appeler tout le code d'intégration push sur le thread principal de votre application.

##### Gestion push par défaut {#default-push-handling}

{% subtabs %}
{% subtab Swift %}
Pour activer la gestion push par défaut de Braze, ajoutez le code suivant à la méthode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` de votre application :

```swift
if let braze = AppDelegate.braze, braze.notifications.handleBackgroundNotification(
  userInfo: userInfo,
  fetchCompletionHandler: completionHandler
) {
  return
}
completionHandler(.noData)
```

Ensuite, ajoutez le code suivant à la méthode `userNotificationCenter(_:didReceive:withCompletionHandler:)` de votre application :

```swift
if let braze = AppDelegate.braze, braze.notifications.handleUserNotification(
  response: response,
  withCompletionHandler: completionHandler
) {
  return
}
completionHandler()
```
{% endsubtab %}

{% subtab OBJECTIVE-C %}
Pour activer la gestion push par défaut de Braze, ajoutez le code suivant à la méthode `application:didReceiveRemoteNotification:fetchCompletionHandler:` de votre application :

```objc
BOOL processedByBraze = AppDelegate.braze != nil && [AppDelegate.braze.notifications handleBackgroundNotificationWithUserInfo:userInfo
                                                                                                       fetchCompletionHandler:completionHandler];
if (processedByBraze) {
  return;
}

completionHandler(UIBackgroundFetchResultNoData);
```

Ensuite, ajoutez le code suivant à la méthode `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` de votre application :

```objc
BOOL processedByBraze = AppDelegate.braze != nil && [AppDelegate.braze.notifications handleUserNotificationWithResponse:response
                                                                                                  withCompletionHandler:completionHandler];
if (processedByBraze) {
  return;
}

completionHandler();
```
{% endsubtab %}
{% endsubtabs %}

##### Gestion push au premier plan {#foreground-push-handling}

{% subtabs %}
{% subtab Swift %}
Pour activer les notifications push au premier plan et permettre à Braze de les reconnaître lorsqu'elles sont reçues, implémentez `UNUserNotificationCenter.userNotificationCenter(_:willPresent:withCompletionHandler:)`. Si un utilisateur appuie sur votre notification au premier plan, le délégué push `userNotificationCenter(_:didReceive:withCompletionHandler:)` sera appelé et Braze enregistrera l'événement de clic push.

```swift
func userNotificationCenter(
  _ center: UNUserNotificationCenter,
  willPresent notification: UNNotification,
  withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions
) -> Void) {
  if let braze = AppDelegate.braze {
    // Forward notification payload to Braze for processing.
    braze.notifications.handleForegroundNotification(notification: notification)
  }

  // Configure application's foreground notification display options.
  if #available(iOS 14.0, *) {
    completionHandler([.list, .banner])
  } else {
    completionHandler([.alert])
  }
}
```
{% endsubtab %}

{% subtab OBJECTIVE-C %}
Pour activer les notifications push au premier plan et permettre à Braze de les reconnaître lorsqu'elles sont reçues, implémentez `userNotificationCenter:willPresentNotification:withCompletionHandler:`. Si un utilisateur appuie sur votre notification au premier plan, le délégué push `userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` sera appelé et Braze enregistrera l'événement de clic push.

```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
       willPresentNotification:(UNNotification *)notification
         withCompletionHandler:(void (^)(UNNotificationPresentationOptions options))completionHandler {
  if (AppDelegate.braze != nil) {
    // Forward notification payload to Braze for processing.
    [AppDelegate.braze.notifications handleForegroundNotificationWithNotification:notification];
  }

  // Configure application's foreground notification display options.
  if (@available(iOS 14.0, *)) {
    completionHandler(UNNotificationPresentationOptionList | UNNotificationPresentationOptionBanner);
  } else {
    completionHandler(UNNotificationPresentationOptionAlert);
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Tester les notifications {#push-testing}

Si vous souhaitez tester les notifications in-app et push via la ligne de commande, vous pouvez envoyer une notification unique depuis le terminal via cURL et l'[API d'envoi de messages]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages). Vous devrez remplacer les champs suivants par les valeurs appropriées pour votre cas de test :

- `YOUR_API_KEY` — disponible dans **Paramètres** > **Clés API**.
- `YOUR_EXTERNAL_USER_ID` — disponible sur la page **Rechercher des utilisateurs**. Consultez [Attribution d'un ID utilisateur]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids#assigning-a-user-id) pour plus d'informations.
- `YOUR_KEY1` (facultatif)
- `YOUR_VALUE1` (facultatif)

Dans l'exemple suivant, l'instance `US-01` est utilisée. Si vous n'êtes pas sur cette instance, consultez notre [documentation API]({{site.baseurl}}/api/basics) pour savoir vers quel endpoint envoyer vos requêtes.

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert":"Test push",
      "extra": {
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

## S'abonner aux mises à jour des notifications push {#subscribing-to-push-notifications-updates}

Pour accéder aux payloads de notifications push traités par Braze, utilisez la méthode [`Braze.Notifications.subscribeToUpdates(payloadTypes:_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(payloadtypes:_:)/).

Vous pouvez utiliser le paramètre `payloadTypes` pour spécifier si vous souhaitez vous abonner aux notifications impliquant des événements d'ouverture de notification push, des événements de réception de notification push, ou les deux.

{% tabs %}
{% tab Swift %}

```swift
// This subscription is maintained through a Braze cancellable, which will observe for changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.notifications.subscribeToUpdates(payloadTypes: [.open, .received]) { payload in
  print("Braze processed notification with title '\(payload.title)' and body '\(payload.body)'")
}
```

{% alert important %}
Gardez à l'esprit que les événements de réception de notification push ne se déclenchent que pour les notifications au premier plan et les notifications en arrière-plan de type `content-available`. Ils ne se déclenchent pas pour les notifications reçues lorsque l'application est arrêtée, ni pour les notifications en arrière-plan sans le champ `content-available`.
{% endalert %}

{% endtab %}

{% tab OBJECTIVE-C %}

```objc
NSInteger filtersValue = BRZNotificationsPayloadTypeFilter.opened.rawValue | BRZNotificationsPayloadTypeFilter.received.rawValue;
BRZNotificationsPayloadTypeFilter *filters = [[BRZNotificationsPayloadTypeFilter alloc] initWithRawValue: filtersValue];
BRZCancellable *cancellable = [notifications subscribeToUpdatesWithPayloadTypes:filters update:^(BRZNotificationsPayload * _Nonnull payload) {
  NSLog(@"Braze processed notification with title '%@' and body '%@'", payload.title, payload.body);
}];
```

{% alert important %}
Gardez à l'esprit que les événements de réception de notification push ne se déclenchent que pour les notifications au premier plan et les notifications en arrière-plan de type `content-available`. Ils ne se déclenchent pas pour les notifications reçues lorsque l'application est arrêtée, ni pour les notifications en arrière-plan sans le champ `content-available`.
{% endalert %}

{% endtab %}

{% endtabs %}
{% alert note %}
Lorsque vous utilisez l'intégration push automatique, `subscribeToUpdates(_:)` est le seul moyen d'être informé des notifications à distance traitées par Braze. Les méthodes système `UIAppDelegate` et `UNUserNotificationCenterDelegate` ne sont pas appelées lorsque la notification est automatiquement traitée par Braze.
{% endalert %}

{% alert tip %}
Créez votre abonnement aux notifications push dans `application(_:didFinishLaunchingWithOptions:)` pour vous assurer que votre abonnement est déclenché lorsqu'un utilisateur final appuie sur une notification alors que votre application est dans un état arrêté.
{% endalert %}

## Gestion des notifications au premier plan {#handling-foreground-notifications}

Par défaut, lorsqu'une notification push arrive alors que votre application est au premier plan, iOS ne l'affiche pas automatiquement. Pour afficher les notifications push au premier plan et les suivre avec l'analyse Braze, appelez la méthode `handleForegroundNotification(notification:)` dans votre implémentation de `UNUserNotificationCenterDelegate.userNotificationCenter(_:willPresent:withCompletionHandler:)`.

### Fonctionnement {#how-it-works}

Lorsque vous appelez `handleForegroundNotification(notification:)`, Braze traite le payload de la notification pour enregistrer les données analytiques et gérer les deep links ou les actions de boutons. Le comportement d'affichage réel est contrôlé par les `UNNotificationPresentationOptions` que vous transmettez au gestionnaire de complétion.

```swift
import BrazeKit
import UserNotifications

extension AppDelegate: UNUserNotificationCenterDelegate {
  func userNotificationCenter(
    _ center: UNUserNotificationCenter,
    willPresent notification: UNNotification,
    withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void
  ) {
    // Let Braze process the notification payload
    if let braze = AppDelegate.braze {
      braze.notifications.handleForegroundNotification(notification: notification)
    }

    // Control how the notification appears in the foreground
    if #available(iOS 14.0, *) {
      completionHandler([.banner, .list, .sound])
    } else {
      completionHandler([.alert, .sound])
    }
  }
}
```

Pour un exemple complet, consultez l'[exemple d'intégration manuelle des notifications push](https://github.com/braze-inc/braze-swift-sdk/blob/e31907eaa0dbd151dc2e6826de66cc494242ba60/Examples/Swift/Sources/PushNotifications-Manual/AppDelegate.swift#L1-L120) dans le dépôt du SDK Swift de Braze.

## Amorces push {#push-primers}

Les campagnes d'amorce push encouragent vos utilisateurs à activer les notifications push sur leur appareil pour votre application. Cela peut se faire sans personnalisation du SDK grâce à notre [amorce push sans code]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages).

## Gestion dynamique de la passerelle APNs {#dynamic-apns-gateway-management}

La gestion dynamique de la passerelle Apple Push Notification Service (APNs) améliore la fiabilité et l'efficacité des notifications push iOS en détectant automatiquement l'environnement APNs approprié. Auparavant, vous deviez sélectionner manuellement les environnements APNs (développement ou production) pour vos notifications push, ce qui pouvait parfois entraîner des configurations de passerelle incorrectes, des échecs de réception et des erreurs `BadDeviceToken`.

Avec la gestion dynamique de la passerelle APNs, vous bénéficiez des avantages suivants :

- **Fiabilité améliorée :** les notifications sont toujours envoyées vers l'environnement APNs approprié, ce qui réduit les échecs de réception.
- **Configuration simplifiée :** vous n'avez plus besoin de gérer manuellement les paramètres de la passerelle APNs.
- **Résilience aux erreurs :** les valeurs de passerelle invalides ou manquantes sont gérées de manière transparente, assurant un service ininterrompu.

### Prérequis {#prerequisites}

Braze prend en charge la gestion dynamique de la passerelle APNs pour les notifications push sur iOS avec la version minimale de SDK suivante :

{% sdk_min_versions swift:10.0.0 %}

### Fonctionnement

Lorsqu'une application iOS s'intègre au SDK Swift de Braze, elle envoie des données relatives à l'appareil, y compris [`aps-environment`](https://developer.apple.com/documentation/bundleresources/entitlements/aps-environment), à l'API du SDK de Braze, si disponible. La valeur `apns_gateway` indique si l'application utilise l'environnement APNs de développement (`dev`) ou de production (`prod`).

Braze stocke également la valeur de passerelle rapportée pour chaque appareil. Si une nouvelle valeur de passerelle valide est reçue, Braze met à jour automatiquement la valeur stockée.

Lorsque Braze envoie une notification push :

- Si une valeur de passerelle valide (dev ou prod) est stockée pour l'appareil, Braze l'utilise pour déterminer l'environnement APNs approprié.
- Si aucune valeur de passerelle n'est stockée, Braze utilise par défaut l'environnement APNs configuré dans la page **App Settings**.

### Questions fréquemment posées {#frequently-asked-questions}

#### Pourquoi cette fonctionnalité a-t-elle été introduite ? {#why-was-this-feature-introduced}

Avec la gestion dynamique de la passerelle APNs, l'environnement approprié est sélectionné automatiquement. Auparavant, vous deviez configurer manuellement la passerelle APNs, ce qui pouvait entraîner des erreurs `BadDeviceToken`, l'invalidation des jetons et des problèmes potentiels de limitation du débit APNs.

#### Quel est l'impact sur les performances de réception des notifications push ? {#how-does-this-impact-push-delivery-performance}

Cette fonctionnalité améliore les taux de réception en acheminant toujours les jetons push vers l'environnement APNs approprié, évitant ainsi les échecs causés par des passerelles mal configurées.

#### Puis-je désactiver cette fonctionnalité ? {#can-i-disable-this-feature}

La gestion dynamique de la passerelle APNs est activée par défaut et apporte des améliorations en termes de fiabilité. Si vous avez des cas d'usage spécifiques nécessitant une sélection manuelle de la passerelle, contactez l'[assistance Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support).