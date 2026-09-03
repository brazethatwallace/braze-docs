## Le manifeste de confidentialité d'Apple {#privacy-manifest}

### Qu'est-ce que les données de suivi ? {#what-is-tracking-data}

Apple définit les « données de suivi » comme des données collectées dans votre application à propos d'un utilisateur final ou d'un appareil, liées à des données third-party (telles que la publicité ciblée) ou à un courtier en données. Pour une définition complète avec des exemples, consultez [Apple : Suivi](https://developer.apple.com/app-store/app-privacy-details/#user-tracking).

Par défaut, le SDK Braze ne collecte pas de données de suivi. Cependant, selon la configuration de votre SDK Braze, vous pourriez être amené à répertorier les données spécifiques à Braze dans le manifeste de confidentialité de votre application.

### Qu'est-ce qu'un manifeste de confidentialité ? {#what-is-a-privacy-manifest}

Un manifeste de confidentialité est un fichier dans votre projet Xcode qui décrit les raisons pour lesquelles votre application et les SDK tiers collectent des données, ainsi que leurs méthodes de collecte. Chacun de vos SDK tiers qui effectue un suivi des données nécessite son propre manifeste de confidentialité. Lorsque vous [créez le rapport de confidentialité de votre application](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests#4239187), ces fichiers de manifeste de confidentialité sont automatiquement agrégés en un seul rapport.

### Domaines de données de suivi d'API {#api-tracking-data-domains}

À partir d'iOS 17.2, Apple bloquera tous les endpoints de suivi déclarés dans votre application jusqu'à ce que l'utilisateur final accepte une [invite de transparence du suivi publicitaire (ATT)](https://support.apple.com/en-us/HT212025). Braze fournit des endpoints de suivi pour acheminer vos données de suivi, tout en vous permettant d'acheminer les données first-party non liées au suivi vers l'endpoint d'origine.

## Déclarer les données de suivi Braze {#declaring-braze-tracking-data}

{% alert tip %}
Pour un guide complet, consultez le [tutoriel Privacy Tracking Data](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking/).
{% endalert %}

### Prérequis {#prerequisites}

La version suivante du SDK Braze est requise pour implémenter cette fonctionnalité :

{% sdk_min_versions swift:9.0.0 %}

### Étape 1 : Examiner vos politiques actuelles {#step-1-review-your-current-policies}

Passez en revue les politiques actuelles de collecte de données de votre SDK Braze avec votre équipe juridique afin de déterminer si votre application collecte des données de suivi [telles que définies par Apple](#what-is-tracking-data). Si vous ne collectez aucune donnée de suivi, vous n'avez pas besoin de personnaliser votre manifeste de confidentialité pour le SDK Braze pour le moment. Pour plus d'informations sur les politiques de collecte de données du SDK Braze, consultez la section [Collecte de données du SDK]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection).

{% alert important %}
Si l'un de vos SDK non-Braze collecte des données de suivi, vous devrez examiner ces politiques séparément.
{% endalert %}

### Étape 2 : Créer un manifeste de confidentialité {#step-2-create-a-privacy-manifest}

Vérifiez d'abord si vous disposez déjà d'un manifeste de confidentialité en recherchant un fichier `PrivacyInfo.xcprivacy` dans votre projet Xcode. Si vous disposez déjà de ce fichier, vous pouvez passer à l'étape suivante. Sinon, consultez [Apple : Créer un manifeste de confidentialité](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files).

### Étape 3 : Ajouter votre endpoint au manifeste de confidentialité {#step-3-add-your-endpoint-to-the-privacy-manifest}

Dans votre projet Xcode, ouvrez le fichier `PrivacyInfo.xcprivacy` de votre application, puis faites un clic droit sur le tableau et cochez **Raw Keys and Values**.

{% alert note %}

{% endalert %}

![Un projet Xcode avec le menu contextuel ouvert et « Raw Keys and Values » mis en surbrillance.]({% image_buster /assets/img/apple/privacy_manifest/check_raw_keys_and_values.png %})

Sous **App Privacy Configuration**, choisissez **NSPrivacyTracking** et définissez sa valeur sur **YES**.

![Le fichier « PrivacyInfo.xcprivacy » ouvert avec « NSPrivacyTracking » défini sur « YES ».]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytracking.png %})

Sous **App Privacy Configuration**, choisissez **NSPrivacyTrackingDomains**. Dans le tableau de domaines, ajoutez un nouvel élément et définissez sa valeur sur l'endpoint que vous avez [précédemment ajouté à votre `AppDelegate`]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration#update-your-app-delegate), préfixé par `sdk-tracking`.

![Le fichier « PrivacyInfo.xcprivacy » ouvert avec un endpoint de suivi Braze répertorié sous « NSPrivacyTrackingDomains ».]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytrackingdomains.png %})

### Étape 4 : Déclarer vos données de suivi {#step-4-declare-your-tracking-data}

Ensuite, ouvrez `AppDelegate.swift` puis listez chaque [propriété de suivi](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/trackingproperty/) que vous souhaitez déclarer en créant une liste de suivi statique ou dynamique. Gardez à l'esprit qu'Apple bloquera ces propriétés jusqu'à ce que l'utilisateur final accepte l'invite ATT. Ne listez donc que les propriétés que vous et votre équipe juridique considérez comme des données de suivi. Par exemple :

{% tabs %}
{% tab Exemple statique %}
Dans l'exemple suivant, `dateOfBirth`, `customEvent` et `customAttribute` sont déclarés comme données de suivi dans une liste statique.

```swift
import UIKit
import BrazeKit

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    let configuration = Braze.Configuration(apiKey: brazeApiKey, endpoint: brazeEndpoint)
    // Declare which types of data you wish to collect for user tracking.
    configuration.api.trackingPropertyAllowList = [
      .dateOfBirth,
      .customEvent(["event-1"]),
      .customAttribute(["attribute-1", "attribute-2"])
    ]
    let braze = Braze(configuration: configuration)
    AppDelegate.braze = braze
    return true
  }
}
```
{% endtab %}

{% tab Exemple dynamique %}
Dans l'exemple suivant, la liste de suivi est automatiquement mise à jour après que l'utilisateur final a accepté l'[invite App Tracking Transparency (ATT)](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/requesttrackingauthorization(completionhandler:)). La demande d'autorisation lors de l'activation de l'application est un événement par scène. Ce code appartient donc à la méthode `sceneDidBecomeActive(_:)` de votre fichier `SceneDelegate.swift` plutôt qu'à la méthode `applicationDidBecomeActive(_:)` de `AppDelegate.swift` (nécessaire pour les applications ayant adopté le [cycle de vie `UIScene`](https://developer.apple.com/documentation/technotes/tn3187-migrating-to-the-uikit-scene-based-life-cycle)). Votre instance Braze reste accessible depuis `SceneDelegate` via la propriété statique `AppDelegate.braze` configurée à l'étape 1.

```swift
func sceneDidBecomeActive(_ scene: UIScene) {
  // Request and check your user's tracking authorization status.
  ATTrackingManager.requestTrackingAuthorization { status in
    // Let Braze know whether user data is allowed to be collected for tracking.
    let enableAdTracking = status == .authorized
    AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)

    // Add the `.firstName` and `.lastName` properties, while removing the `.everything` configuration.
    AppDelegate.braze?.updateTrackingAllowList(
      adding: [.firstName, .lastName],
      removing: [.everything]
    )
  }
}
```
{% endtab %}
{% endtabs %}

### Étape 5 : Empêcher les boucles de réessai infinies {#step-5-prevent-infinite-retry-loops}

Pour empêcher le SDK d'entrer dans une boucle de réessai infinie, utilisez la méthode `set(adTrackingEnabled: enableAdTracking)` pour gérer les autorisations ATT. La propriété `adTrackingEnabled` dans votre méthode `SceneDelegate.swift` doit être gérée de manière similaire à l'exemple suivant :

```swift
func sceneDidBecomeActive(_ scene: UIScene) {
    // Request and check your user's tracking authorization status.
    ATTrackingManager.requestTrackingAuthorization { status in
      // Let Braze know whether user data is allowed to be collected for tracking.
      let enableAdTracking = status == .authorized
      AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)
    }
}
```

## Désactivation du suivi des données {#disabling-data-tracking}

Pour désactiver le suivi des données sur le SDK Swift, définissez la propriété [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled) sur `false` sur votre instance Braze. Lorsque `enabled` est défini sur `false`, le SDK Braze ignore tous les appels à l'API publique. Le SDK annule également toutes les actions en cours, telles que les requêtes réseau, le traitement des événements, etc.

## Effacer les données précédemment stockées {#wiping-previously-stored-data}

Vous pouvez utiliser la méthode [`wipeData()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata()) pour effacer complètement les données du SDK stockées localement sur l'appareil d'un utilisateur.

Pour les versions 7.0.0 et ultérieures du SDK Braze Swift, le SDK et la méthode `wipeData()` génèrent aléatoirement un UUID pour l'ID de l'appareil. Cependant, si votre `useUUIDAsDeviceId` est défini sur `false` _ou_ si vous utilisez la version 5.7.0 ou antérieure du SDK Swift, vous devrez également effectuer une requête POST vers [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) car votre IDFV sera automatiquement utilisé comme ID d'appareil de cet utilisateur.

Si vous utilisez l'intégration manuelle des notifications push et que votre application appelle `wipeData()` puis réactive le SDK au cours de la même exécution de l'application, appelez à nouveau `registerForRemoteNotifications()` afin que Braze puisse recevoir un jeton d'appareil actualisé. Pour plus d'informations, consultez la section [configuration des notifications push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

## Reprise du suivi des données {#resuming-data-tracking}

Pour reprendre la collecte de données, définissez [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/) sur `true`. Gardez à l'esprit que cela ne restaurera aucune donnée précédemment effacée.

## Déconnexion et désinscription push {#logout-and-unregister-push}

Le SDK Braze fournit des méthodes pour arrêter le ciblage d'un appareil lorsqu'un utilisateur se désinscrit des notifications push ou se déconnecte. Ces méthodes suppriment les données d'inscription push de l'utilisateur actuel sur le serveur Braze et dans le SDK, de sorte que Braze n'envoie plus de futures Campaigns de notifications push à cet utilisateur.

### Déconnexion {#logout}

Lorsqu'un utilisateur se déconnecte d'une application, appelez la méthode `logout` du SDK pour supprimer l'inscription push de l'appareil de l'utilisateur actuel et effectuer automatiquement des actions de nettoyage sur le SDK. La méthode `logout` effectue les opérations suivantes :

- Désinscrit le jeton push de l'appareil, ainsi que tous les jetons push-to-start des Live Activities, de l'utilisateur actuel sur le serveur Braze.
- Si l'appel de désinscription réussit, le SDK efface les données SDK stockées localement et désactive le SDK.
- En cas d'échec, une erreur est levée avec un indicateur `isRetriable` permettant à l'intégrateur d'agir.

{% subtabs local %}
{% subtab Swift %}

L'exemple suivant avec gestionnaire de rappel montre la gestion du succès et de l'échec de `logout`. Utilisez-le pour les flux basés sur des rappels, et remplacez la journalisation par la logique de nouvelle tentative ou de ré-authentification de votre application.

```swift
// Completion handler
AppDelegate.braze?.logout { result in
  switch result {
  case .success:
    print("Logout successful")
  case .failure(let error):
    print("Logout failed: \(error.message), isRetriable: \(error.isRetriable)")
  }
}
```

L'exemple async suivant montre l'API suspensive `logout`. Utilisez-le pour les workflows asynchrones et personnalisez les branches de succès et d'échec pour votre application.

```swift
// Async/await
do {
  try await AppDelegate.braze?.logout()
  print("Logout successful")
} catch let error as Braze.LogoutErrorResult {
  print("Logout failed: \(error.message), isRetriable: \(error.isRetriable)")
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

Cet exemple Objective-C montre la gestion de `logout` basée sur un rappel. Utilisez-le dans les intégrations Objective-C et remplacez la journalisation par le flux de votre application.

```objc
[AppDelegate.braze logoutWithCompletion:^(NSError * _Nullable error) {
  if (error) {
    NSNumber *isRetriable = error.userInfo[BRZLogoutErrorUserInfoKey.isRetriable];
    NSLog(@"Logout failed: %@, isRetriable=%@", error.localizedDescription, isRetriable);
  }
}];
```

{% endsubtab %}
{% endsubtabs local %}

{% alert note %}
`logout` ne met pas fin aux Live Activities en cours d'exécution. Dans le rappel de succès, terminez manuellement toutes les Live Activities en cours en utilisant la méthode [`end(_:dismissalPolicy:)`](https://developer.apple.com/documentation/activitykit/activity/end(_:dismissalpolicy:)) d'ActivityKit.
{% endalert %}

#### Réactiver le suivi et le push après `logout` {#re-enable-tracking-and-push-after-logout}

Après un `logout` réussi, définissez [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/) à `true`, puis réinscrivez-vous aux notifications auprès de votre système d'exploitation (OS) ou fournisseur push en suivant la [configuration push Swift]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

#### Éviter les appels de désinscription immédiats {#avoid-immediate-unregister-calls}

Évitez d'appeler `logout` ou `unregisterPush` directement après l'inscription aux notifications push auprès de l'OS ou du fournisseur push. En raison du traitement asynchrone du serveur, cela peut dans de rares cas réajouter le jeton push à l'utilisateur Braze.

### Désinscription push {#unregister-push}

Pour arrêter l'envoi de notifications push à un appareil sans nettoyage automatisé supplémentaire, utilisez la méthode `unregisterPush`. Cela supprime le jeton push de l'appareil de l'utilisateur actuel sur le serveur Braze et efface le jeton stocké localement.

{% subtabs local %}
{% subtab Swift %}

L'exemple suivant avec gestionnaire de rappel montre la gestion du succès et de l'échec de `unregisterPush`. Utilisez-le pour les flux basés sur des rappels, et remplacez la journalisation par votre propre logique de nouvelle tentative.

```swift
// Completion handler
AppDelegate.braze?.notifications.unregisterPush { result in
  switch result {
  case .success:
    print("Push unregistered successfully")
  case .failure(let error):
    print("Push unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
  }
}
```

L'exemple async suivant montre l'API suspensive `unregisterPush`. Utilisez-le pour les workflows asynchrones et personnalisez les branches de succès et d'échec pour votre application.

```swift
// Async/await
do {
  try await AppDelegate.braze?.notifications.unregisterPush()
  print("Push unregistered successfully")
} catch let error as Braze.PushUnregistrationError {
  print("Push unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

Cet exemple Objective-C montre la gestion de `unregisterPush` basée sur un rappel. Utilisez-le dans les intégrations Objective-C et remplacez la journalisation par le flux de votre application.

```objc
[AppDelegate.braze.notifications unregisterPushWithCompletion:^(NSError * _Nullable error) {
  if (error) {
    NSNumber *isRetriable = error.userInfo[BRZPushUnregistrationErrorUserInfoKey.isRetriable];
    NSNumber *statusCode = error.userInfo[BRZPushUnregistrationErrorUserInfoKey.httpStatusCode];
    NSLog(@"Push unregistration failed: %@, isRetriable=%@ status=%@",
          error.localizedDescription, isRetriable, statusCode);
  }
}];
```

{% endsubtab %}
{% endsubtabs local %}

#### Réinscrire les notifications push après `unregisterPush` {#re-register-push-after-unregisterpush}

Après avoir appelé `unregisterPush`, réinscrivez-vous aux notifications auprès de votre OS ou fournisseur push en suivant la [configuration push Swift]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) avant d'envoyer à nouveau des notifications push Braze.

#### Éviter les appels de désinscription immédiats

Évitez d'appeler `logout` ou `unregisterPush` directement après l'inscription aux notifications push auprès de l'OS ou du fournisseur push. En raison du traitement asynchrone du serveur, cela peut dans de rares cas réajouter le jeton push à l'utilisateur Braze.

### Désinscrire les jetons push-to-start pour les Live Activities {#unregister-push-to-start}

Les Live Activities peuvent être démarrées à distance à l'aide de jetons push-to-start. Pour empêcher Braze de démarrer à distance des Live Activities sur un appareil, appelez la méthode `unregisterPushToStart` pour désinscrire tous les types actuellement enregistrés (par défaut) ou une liste spécifiée de types d'Activity.

Notez que les Live Activities en cours d'exécution continuent de recevoir des mises à jour et que cette méthode supprime uniquement la possibilité de démarrer de nouvelles activités à distance. Pour plus d'informations sur les Live Activities, consultez [Live Activities]({{site.baseurl}}/developer_guide/live_notifications/live_activities).

#### Terminer les Live Activities en cours {#end-any-running-live-activities}

`unregisterPushToStart` ne met pas fin aux Live Activities en cours d'exécution. Dans le rappel de succès, terminez manuellement toutes les Live Activities en cours en utilisant la méthode [`end(_:dismissalPolicy:)`](https://developer.apple.com/documentation/activitykit/activity/end(_:dismissalpolicy:)) d'ActivityKit.

{% alert note %}
Évitez d'appeler `logout` ou `unregisterPushToStart` directement après avoir appelé `registerPushToStart` pour une Live Activity. En raison de la nature asynchrone du traitement serveur, cela peut dans de rares cas entraîner le réajout du jeton push-to-start à l'utilisateur Braze.
{% endalert %}

L'exemple suivant montre comment désinscrire tous les types d'activités push-to-start. Utilisez-le lorsqu'un utilisateur déconnecté ne devrait plus recevoir de nouvelles Live Activities démarrées à distance.

```swift
// Unregister all currently-registered activity types
// Completion handler
AppDelegate.braze?.liveActivities.unregisterPushToStart { result in
  switch result {
  case .success:
    print("Push-to-start unregistered successfully")
  case .failure(let error):
    print("Push-to-start unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
  }
}

// Async/await
do {
  try await AppDelegate.braze?.liveActivities.unregisterPushToStart()
  print("Push-to-start unregistered successfully")
} catch let error as Braze.PushUnregistrationError {
  print("Push-to-start unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
}
```

L'exemple suivant montre comment désinscrire des types d'activités spécifiques. Utilisez-le lorsque seules certaines Live Activities doivent cesser d'être démarrées à distance.

```swift
// Unregister specific activity types
AppDelegate.braze?.liveActivities.unregisterPushToStart(types: ["ActivityType1", "ActivityType2"]) { result in
  switch result {
  case .success:
    print("Push-to-start unregistered successfully")
  case .failure(let error):
    print("Push-to-start unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
  }
}
```

{% alert note %}
`unregisterPushToStart` ne dispose pas d'une API Objective-C, car les Live Activities reposent sur des types exclusivement Swift.
{% endalert %}

## Collecte de l'IDFV {#idfv-collection}

Dans les versions précédentes du SDK iOS de Braze, le champ IDFV (Identifier for Vendor) était automatiquement collecté en tant qu'identifiant d'appareil de l'utilisateur. À partir de la version `v5.7.0` du SDK Swift, le champ IDFV pouvait être optionnellement désactivé et Braze définissait alors un UUID aléatoire comme identifiant d'appareil. À partir de la version `v7.0.0` du SDK Swift, le champ IDFV ne sera plus collecté par défaut et un UUID sera défini comme identifiant d'appareil à la place.

La fonctionnalité `useUUIDAsDeviceId` configure le [SDK Swift](https://github.com/braze-inc/braze-swift-sdk) pour définir l'identifiant d'appareil comme un UUID. Traditionnellement, le SDK iOS attribuait à l'identifiant d'appareil la valeur IDFV générée par Apple. Avec cette fonctionnalité activée par défaut sur votre application iOS, tous les nouveaux utilisateurs créés via le SDK se verront attribuer un identifiant d'appareil égal à un UUID.

Si vous souhaitez toujours collecter l'IDFV séparément, vous pouvez utiliser [`set(identifierforvendor:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforvendor:)).

{% alert note %}
Apple est responsable de la création de l'IDFV, et l'IDFV est géré par Apple. Braze ne transforme ni ne modifie les IDFV, et Apple ne fournit aucune garantie concernant la casse ou le format.
{% endalert %}

{% alert note %}
La lecture de `braze.deviceId` bloque le thread appelant jusqu'à ce que le SDK ait terminé ses opérations post-initialisation. Pour les contextes de thread principal ou sensibles à la latence, utilisez plutôt les alternatives non bloquantes.

{% subtabs local %}
{% subtab Swift %}
```swift
// Completion handler — always delivers on the main thread.
AppDelegate.braze?.getDeviceId { deviceId in
  print("Device ID:", deviceId)
}

// Async/await (iOS 13.0+, tvOS 13.0+, watchOS 6.0+, macOS 10.15+)
let deviceId = await AppDelegate.braze?.getDeviceId()
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// Completion handler — always delivers on the main thread.
[AppDelegate.braze getDeviceIdWithCompletion:^(NSString *deviceId) {
  NSLog(@"Device ID: %@", deviceId);
}];
```
{% endsubtab %}
{% endsubtabs local %}
{% endalert %}

### Considérations {#considerations}

#### Version du SDK {#sdk-version}

Dans le SDK Swift `v7.0.0+`, lorsque `useUUIDAsDeviceId` est activé (par défaut), tous les nouveaux utilisateurs créés se verront attribuer un identifiant d'appareil aléatoire. Tous les utilisateurs précédemment existants conserveront la même valeur d'identifiant d'appareil, qui peut avoir été un IDFV.

Lorsque cette fonctionnalité n'est pas activée, les appareils continueront de se voir attribuer un IDFV lors de leur création.

#### En aval {#downstream}

**Partenaires technologiques** : lorsque cette fonctionnalité est activée, les partenaires technologiques qui dérivent la valeur IDFV de l'identifiant d'appareil Braze n'auront plus accès à cette donnée. Si la valeur IDFV dérivée de l'appareil est nécessaire pour votre intégration partenaire, nous vous recommandons de définir cette fonctionnalité sur `false`.

**Currents** : `useUUIDAsDeviceId` défini sur true signifie que l'identifiant d'appareil envoyé dans Currents ne correspondra plus à la valeur IDFV.

### Questions fréquentes {#frequently-asked-questions}

#### Ce changement impactera-t-il mes utilisateurs existants dans Braze ? {#will-this-change-impact-my-existing-users-in-braze}

Non. Lorsqu'elle est activée, cette fonctionnalité n'écrasera aucune donnée utilisateur dans Braze. Les nouveaux identifiants d'appareil UUID seront uniquement créés pour les nouveaux appareils ou lorsque `wipedata()` est appelé.

#### Puis-je désactiver cette fonctionnalité après l'avoir activée ? {#can-i-turn-this-feature-off-after-turning-it-on}

Oui, cette fonctionnalité peut être activée et désactivée à votre convenance. Les identifiants d'appareil précédemment stockés ne seront jamais écrasés.

#### Puis-je toujours capturer la valeur IDFV via Braze ailleurs ? {#can-i-still-capture-the-idfv-value-through-braze-elsewhere}

Oui, vous pouvez toujours collecter optionnellement l'IDFV via le SDK Swift (la collecte est désactivée par défaut).