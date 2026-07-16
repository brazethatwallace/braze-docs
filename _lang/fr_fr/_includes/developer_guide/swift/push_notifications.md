## Limites de débit {#rate-limits}

Les notifications push sont soumises à une limite de débit, vous pouvez donc en envoyer autant que votre application en a besoin sans crainte. iOS et les serveurs du service de notification push d'Apple (APNs) contrôlent la fréquence de distribution, et vous ne risquez rien en cas d'envoi massif. Si vos notifications push sont limitées, elles peuvent être retardées jusqu'à ce que l'appareil envoie un paquet keep-alive ou reçoive une autre notification.

## Configuration des notifications push {#setting-up-push-notifications}

### Étape 1 : Télécharger votre jeton APNs {#step-1-upload-your-apns-token}

{% multi_lang_include developer_guide/swift/apns_token.md %}

### Étape 2 : Activer les fonctionnalités push {#step-2-enable-push-capabilities}

Dans Xcode, rendez-vous dans la section **Signing & Capabilities** de la cible principale de l'application et ajoutez la fonctionnalité de notifications push.

![La section « Signing & Capabilities » dans un projet Xcode.]({% image_buster /assets/img_archive/Enable_push_capabilities.png %})

### Étape 3 : Configurer la gestion des notifications push {#step-3-set-up-push-handling}

Vous pouvez utiliser le SDK Swift pour automatiser le traitement des notifications à distance reçues de Braze. C'est la méthode la plus simple pour gérer les notifications push et celle que nous recommandons.

{% tabs local %}
{% tab Automatic %}
#### Étape 3.1 : Activer l'automatisation dans la propriété push {#step-31-enable-automation-in-the-push-property}

Pour activer l'intégration automatique des notifications push, définissez la propriété `automation` de la configuration `push` sur `true` :

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
- Demander l'autorisation/permission de notification push lors de l'initialisation.
- Fournir dynamiquement des implémentations pour les méthodes de délégation système liées aux notifications push.

{% alert note %}
Les étapes d'automatisation effectuées par le SDK sont compatibles avec les intégrations préexistantes de gestion des notifications push dans votre base de code. Le SDK automatise uniquement le traitement des notifications à distance reçues de Braze. Tout gestionnaire système implémenté pour traiter vos propres notifications à distance ou celles d'un SDK tiers continuera de fonctionner lorsque l'`automation` est activée.
{% endalert %}

{% alert warning %}
Le SDK doit être initialisé sur le thread principal pour permettre l'automatisation des notifications push. L'initialisation du SDK doit avoir lieu avant la fin du lancement de l'application ou dans l'implémentation [`application(_:didFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) de votre AppDelegate.
Si votre application nécessite une configuration supplémentaire avant l'initialisation du SDK, consultez la page de documentation [Initialisation différée]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift#step-2-set-up-delayed-initialization-optional).
{% endalert %}

#### Étape 3.2 : Remplacer les configurations individuelles (facultatif) {#step-32-override-individual-configurations-optional}

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

{% tab Manual %}
{% alert note %}
Si vous comptez sur les notifications push pour des comportements supplémentaires spécifiques à votre application, vous pouvez tout de même utiliser l'intégration push automatique au lieu de l'intégration manuelle. La méthode [`subscribeToUpdates(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(_:)) permet d'être notifié des notifications à distance traitées par Braze.
{% endalert %}

#### Étape 3.1 : S'inscrire aux notifications push auprès des APNs {#step-31-register-for-push-notifications-with-apns}

Incluez l'exemple de code approprié dans la [méthode de délégation `application:didFinishLaunchingWithOptions:`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) de votre application afin que les appareils de vos utilisateurs puissent s'enregistrer auprès des APNs. Assurez-vous d'appeler tout le code d'intégration push dans le thread principal de votre application.

Braze fournit également des catégories push par défaut pour la prise en charge des boutons d'action push, qui doivent être ajoutées manuellement à votre code d'enregistrement push. Reportez-vous aux [boutons d'action push]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_customizing-push-categories) pour les étapes d'intégration supplémentaires.

Ajoutez le code suivant à la méthode `application:didFinishLaunchingWithOptions:` de votre délégué d'application.

{% alert note %}
L'exemple de code suivant inclut l'intégration pour l'authentification provisoire des notifications push (lignes 5 et 6). Si vous ne prévoyez pas d'utiliser l'autorisation provisoire dans votre application, vous pouvez supprimer les lignes de code qui ajoutent `UNAuthorizationOptionProvisional` aux options `requestAuthorization`.<br>Consultez les [options de notification iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options) pour en savoir plus sur l'authentification provisoire push.
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
Vous devez assigner votre objet délégué avec `center.delegate = self` de manière synchrone avant que votre application ne termine son lancement, de préférence dans `application:didFinishLaunchingWithOptions:`. Sans cela, votre application risque de manquer des notifications push entrantes. Consultez la documentation Apple [`UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate) pour en savoir plus.
Si votre application appelle `wipeData()` puis réactive le SDK Braze au cours de la même exécution, vous devez appeler à nouveau `registerForRemoteNotifications()` pour repeupler le jeton d'appareil utilisé par le SDK.
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
La méthode de délégation `application:didRegisterForRemoteNotificationsWithDeviceToken:` est appelée à chaque fois après l'appel de `application.registerForRemoteNotifications()`. <br><br>Si vous migrez vers Braze depuis un autre service de notification push et que l'appareil de votre utilisateur est déjà enregistré auprès des APNs, cette méthode collectera les jetons des enregistrements existants lors du prochain appel, et les utilisateurs n'auront pas besoin de se réabonner aux notifications push.
{% endalert %}

#### Étape 3.3 : Activer la gestion des notifications push {#step-33-enable-push-handling}

Ensuite, transmettez les notifications push reçues à Braze. Cette étape est nécessaire pour la journalisation analytique des push et la gestion des liens. Assurez-vous d'appeler tout le code d'intégration push dans le thread principal de votre application.

##### Gestion par défaut des notifications push {#default-push-handling}

{% subtabs %}
{% subtab Swift %}
Pour activer la gestion par défaut des notifications push de Braze, ajoutez le code suivant à la méthode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` de votre application :

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
Pour activer la gestion par défaut des notifications push de Braze, ajoutez le code suivant à la méthode `application:didReceiveRemoteNotification:fetchCompletionHandler:` de votre application :

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

##### Gestion des notifications push au premier plan {#foreground-push-handling}

{% subtabs %}
{% subtab Swift %}
Pour activer les notifications push au premier plan et permettre à Braze de les reconnaître à la réception, implémentez `UNUserNotificationCenter.userNotificationCenter(_:willPresent:withCompletionHandler:)`. Si un utilisateur appuie sur votre notification au premier plan, le délégué push `userNotificationCenter(_:didReceive:withCompletionHandler:)` sera appelé et Braze enregistrera l'événement de clic push.

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
Pour activer les notifications push au premier plan et permettre à Braze de les reconnaître à la réception, implémentez `userNotificationCenter:willPresentNotification:withCompletionHandler:`. Si un utilisateur appuie sur votre notification au premier plan, le délégué push `userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` sera appelé et Braze enregistrera l'événement de clic push.

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

Pour accéder aux payloads des notifications push traitées par Braze, utilisez la méthode [`Braze.Notifications.subscribeToUpdates(payloadTypes:_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(payloadtypes:_:)/).

Vous pouvez utiliser le paramètre `payloadTypes` pour indiquer si vous souhaitez vous abonner aux notifications concernant les événements d'ouverture push, les événements de réception push, ou les deux.

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
Les événements de réception push ne se déclenchent que pour les notifications au premier plan et les notifications en arrière-plan `content-available`. Ils ne se déclenchent pas pour les notifications reçues lorsque l'application est terminée, ni pour les notifications en arrière-plan sans le champ `content-available`.
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
Les événements de réception push ne se déclenchent que pour les notifications au premier plan et les notifications en arrière-plan `content-available`. Ils ne se déclenchent pas pour les notifications reçues lorsque l'application est terminée, ni pour les notifications en arrière-plan sans le champ `content-available`.
{% endalert %}

{% endtab %}

{% endtabs %}
{% alert note %}
Lorsque vous utilisez l'intégration push automatique, `subscribeToUpdates(_:)` est le seul moyen d'être notifié des notifications à distance traitées par Braze. Les méthodes système `UIAppDelegate` et `UNUserNotificationCenterDelegate` ne sont pas appelées lorsque la notification est traitée automatiquement par Braze.
{% endalert %}

{% alert tip %}
Créez votre abonnement aux notifications push dans `application(_:didFinishLaunchingWithOptions:)` pour vous assurer que l'abonnement est déclenché lorsqu'un utilisateur appuie sur une notification alors que votre application est dans un état terminé.
{% endalert %}

## Gestion des notifications au premier plan {#handling-foreground-notifications}

Par défaut, lorsqu'une notification push arrive alors que votre application est au premier plan, iOS ne l'affiche pas automatiquement. Pour afficher les notifications push au premier plan et les suivre avec l'analytique de Braze, appelez la méthode `handleForegroundNotification(notification:)` dans votre implémentation de `UNUserNotificationCenterDelegate.userNotificationCenter(_:willPresent:withCompletionHandler:)`.

### Fonctionnement {#how-it-works}

Lorsque vous appelez `handleForegroundNotification(notification:)`, Braze traite le payload de la notification pour enregistrer les données analytiques et gérer les deep links ou les actions des boutons. Le comportement d'affichage réel est contrôlé par les `UNNotificationPresentationOptions` que vous transmettez au completion handler.

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

Pour un exemple complet, consultez l'[exemple d'intégration manuelle des notifications push](https://github.com/braze-inc/braze-swift-sdk/blob/e31907eaa0dbd151dc2e6826de66cc494242ba60/Examples/Swift/Sources/PushNotifications-Manual/AppDelegate.swift#L1-L120) dans le dépôt du SDK Braze Swift.

## Amorces push {#push-primers}

Les campagnes d'amorce push encouragent vos utilisateurs à activer les notifications push sur leur appareil pour votre application. Cela peut se faire sans personnalisation du SDK grâce à notre [amorce push sans code]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages).

## Gestion dynamique de la passerelle APNs {#dynamic-apns-gateway-management}

La gestion dynamique de la passerelle Apple Push Notification Service (APNs) améliore la fiabilité et l'efficacité des notifications push iOS en détectant automatiquement l'environnement APNs approprié. Auparavant, vous deviez sélectionner manuellement les environnements APNs (développement ou production) pour vos notifications push, ce qui pouvait entraîner des configurations de passerelle incorrectes, des échecs de distribution et des erreurs `BadDeviceToken`.

Avec la gestion dynamique de la passerelle APNs, vous bénéficiez de :

- **Fiabilité améliorée :** Les notifications sont toujours transmises à l'environnement APNs approprié, réduisant les échecs de distribution.
- **Configuration simplifiée :** Vous n'avez plus besoin de gérer manuellement les paramètres de la passerelle APNs.
- **Résilience aux erreurs :** Les valeurs de passerelle invalides ou manquantes sont gérées de manière transparente, garantissant un service ininterrompu.

### Conditions préalables {#prerequisites}

Braze prend en charge la gestion dynamique de la passerelle APNs pour les notifications push sur iOS avec la version SDK minimale suivante :

{% sdk_min_versions swift:10.0.0 %}

### Fonctionnement

Lorsqu'une application iOS s'intègre au SDK Braze Swift, elle envoie les données relatives à l'appareil, y compris [`aps-environment`](https://developer.apple.com/documentation/bundleresources/entitlements/aps-environment), à l'API du SDK Braze, si disponible. La valeur `apns_gateway` indique si l'application utilise l'environnement APNs de développement (`dev`) ou de production (`prod`).

Braze enregistre également la valeur de passerelle signalée pour chaque appareil. Si une nouvelle valeur de passerelle valide est reçue, Braze met automatiquement à jour la valeur enregistrée.

Lorsque Braze envoie une notification push :

- Si une valeur de passerelle valide (dev ou prod) est enregistrée pour l'appareil, Braze l'utilise pour déterminer l'environnement APNs approprié.
- Si aucune valeur de passerelle n'est enregistrée, Braze utilise par défaut l'environnement APNs configuré dans la page **Paramètres des applications**.

### Foire aux questions {#frequently-asked-questions}

#### Pourquoi cette fonctionnalité a-t-elle été introduite ? {#why-was-this-feature-introduced}

Avec la gestion dynamique de la passerelle APNs, l'environnement approprié est sélectionné automatiquement. Auparavant, vous deviez configurer manuellement la passerelle APNs, ce qui pouvait entraîner des erreurs `BadDeviceToken`, l'invalidation des jetons et d'éventuels problèmes de limite de débit APNs.

#### Quel est l'impact sur les performances de distribution push ? {#how-does-this-impact-push-delivery-performance}

Cette fonctionnalité améliore les taux de distribution en acheminant systématiquement les jetons push vers l'environnement APNs approprié, évitant ainsi les échecs causés par des passerelles mal configurées.

#### Puis-je désactiver cette fonctionnalité ? {#can-i-disable-this-feature}

La gestion dynamique de la passerelle APNs est activée par défaut et apporte des améliorations de fiabilité. Si vous avez des cas d'usage spécifiques nécessitant une sélection manuelle de la passerelle, contactez l'[assistance Braze]({{site.baseurl}}/user_guide/administrative/access_braze/support).