## Le manifeste de confidentialité d'Apple {#privacy-manifest}

### Qu'est-ce que les données de suivi ? {#what-is-tracking-data}

Apple définit les « données de suivi » comme des données collectées dans votre application à propos d'un utilisateur final ou d'un appareil, liées à des données third-party (telles que la publicité ciblée) ou à un courtier en données. Pour une définition complète avec des exemples, consultez [Apple : Suivi](https://developer.apple.com/app-store/app-privacy-details/#user-tracking).

Par défaut, le SDK Braze ne collecte pas de données de suivi. Cependant, selon la configuration de votre SDK Braze, vous pourriez être amené à répertorier les données spécifiques à Braze dans le manifeste de confidentialité de votre application.

### Qu'est-ce qu'un manifeste de confidentialité ? {#what-is-a-privacy-manifest}

Un manifeste de confidentialité est un fichier dans votre projet Xcode qui décrit les raisons pour lesquelles votre application et les SDK tiers collectent des données, ainsi que leurs méthodes de collecte. Chacun de vos SDK tiers qui effectue un suivi des données nécessite son propre manifeste de confidentialité. Lorsque vous [créez le rapport de confidentialité de votre application](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests#4239187), ces fichiers de manifeste de confidentialité sont automatiquement agrégés en un seul rapport.

### Domaines de données de suivi d'API {#api-tracking-data-domains}

À partir d'iOS 17.2, Apple bloquera tous les endpoints de suivi déclarés dans votre application jusqu'à ce que l'utilisateur final accepte une [invite de transparence du suivi publicitaire (ATT)](https://support.apple.com/en-us/HT212025). Braze fournit des endpoints de suivi pour acheminer vos données de suivi, tout en vous permettant d'acheminer les données first-party non liées au suivi vers l'endpoint d'origine.

## Déclaration des données de suivi Braze {#declaring-braze-tracking-data}

{% alert tip %}
Pour un guide complet, consultez le [tutoriel sur les données de suivi de la confidentialité](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking/).
{% endalert %}

### Conditions préalables {#prerequisites}

La version suivante du SDK Braze est requise pour implémenter cette fonctionnalité :

{% sdk_min_versions swift:9.0.0 %}

### Étape 1 : Examinez vos politiques actuelles {#step-1-review-your-current-policies}

Examinez les politiques actuelles de collecte de données de votre SDK Braze avec votre équipe juridique pour déterminer si votre application collecte des données de suivi [telles que définies par Apple](#what-is-tracking-data). Si vous ne collectez aucune donnée de suivi, vous n'avez pas besoin de personnaliser votre manifeste de confidentialité pour le SDK Braze pour le moment. Pour plus d'informations sur les politiques de collecte de données du SDK Braze, consultez [Collecte de données SDK]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection).

{% alert important %}
Si l'un de vos SDK autres que Braze collecte des données de suivi, vous devrez examiner ces politiques séparément.
{% endalert %}

### Étape 2 : Créez un manifeste de confidentialité {#step-2-create-a-privacy-manifest}

Commencez par vérifier si vous disposez déjà d'un manifeste de confidentialité en recherchant un fichier `PrivacyInfo.xcprivacy` dans votre projet Xcode. Si ce fichier existe déjà, vous pouvez passer à l'étape suivante. Sinon, consultez [Apple : Créer un manifeste de confidentialité](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files).

### Étape 3 : Ajoutez votre endpoint au manifeste de confidentialité {#step-3-add-your-endpoint-to-the-privacy-manifest}

Dans votre projet Xcode, ouvrez le fichier `PrivacyInfo.xcprivacy` de votre application, puis faites un clic droit sur le tableau et cochez **Raw Keys and Values**.

{% alert note %}

{% endalert %}

![Un projet Xcode avec le menu contextuel ouvert et « Raw Keys and Values » en surbrillance.]({% image_buster /assets/img/apple/privacy_manifest/check_raw_keys_and_values.png %})

Sous **App Privacy Configuration**, choisissez **NSPrivacyTracking** et définissez sa valeur sur **YES**.

![Le fichier « PrivacyInfo.xcprivacy » ouvert avec « NSPrivacyTracking » défini sur « YES ».]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytracking.png %})

Sous **App Privacy Configuration**, choisissez **NSPrivacyTrackingDomains**. Dans le tableau des domaines, ajoutez un nouvel élément et définissez sa valeur sur l'endpoint que vous [avez précédemment ajouté à votre `AppDelegate`]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration#update-your-app-delegate) préfixé par `sdk-tracking`.

![Le fichier « PrivacyInfo.xcprivacy » ouvert avec un endpoint de suivi Braze répertorié sous « NSPrivacyTrackingDomains ».]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytrackingdomains.png %})

### Étape 4 : Déclarez vos données de suivi {#step-4-declare-your-tracking-data}

Ensuite, ouvrez `AppDelegate.swift` puis listez chaque [propriété de suivi](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/trackingproperty/) que vous souhaitez déclarer en créant une liste de suivi statique ou dynamique. Gardez à l'esprit qu'Apple bloquera ces propriétés jusqu'à ce que l'utilisateur final accepte l'invite ATT. Ne listez donc que les propriétés que vous et votre équipe juridique considérez comme relevant du suivi. Par exemple :

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
Dans l'exemple suivant, la liste de suivi est automatiquement mise à jour après que l'utilisateur final a accepté l'[invite de transparence du suivi des applications (ATT)](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/requesttrackingauthorization(completionhandler:)). La demande d'autorisation lors de l'activation de l'application est un événement par scène. Ce code doit donc être placé dans la méthode `sceneDidBecomeActive(_:)` de votre fichier `SceneDelegate.swift` plutôt que dans la méthode `applicationDidBecomeActive(_:)` de `AppDelegate.swift` (requis pour les applications ayant adopté le [cycle de vie `UIScene`](https://developer.apple.com/documentation/technotes/tn3187-migrating-to-the-uikit-scene-based-life-cycle)). Votre instance Braze reste accessible depuis `SceneDelegate` via la propriété statique `AppDelegate.braze` configurée à l'étape 1.

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

### Étape 5 : Empêchez les boucles de réessai infinies {#step-5-prevent-infinite-retry-loops}

Pour empêcher le SDK d'entrer dans une boucle de réessai infinie, utilisez la méthode `set(adTrackingEnabled: enableAdTracking)` pour gérer les autorisations ATT. La propriété `adTrackingEnabled` dans la méthode de votre `SceneDelegate.swift` doit être gérée de manière similaire à ce qui suit :

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

## Effacement des données précédemment stockées {#wiping-previously-stored-data}

Vous pouvez utiliser la méthode [`wipeData()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata()) pour effacer complètement les données SDK stockées localement sur l'appareil d'un utilisateur.

À partir de la version 7.0.0 de Braze Swift, le SDK et la méthode `wipeData()` génèrent aléatoirement un UUID comme identifiant d'appareil. Cependant, si votre `useUUIDAsDeviceId` est défini sur `false` _ou_ si vous utilisez la version 5.7.0 ou antérieure du SDK Swift, vous devrez également effectuer une requête POST vers [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) car votre IDFV sera automatiquement utilisé comme identifiant d'appareil de cet utilisateur.

Si vous utilisez l'intégration manuelle des notifications push et que votre application appelle `wipeData()` puis réactive le SDK au cours de la même session, appelez à nouveau `registerForRemoteNotifications()` pour que Braze puisse recevoir un jeton d'appareil actualisé. Pour plus d'informations, consultez [Configuration des notifications push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

## Reprise du suivi des données {#resuming-data-tracking}

Pour reprendre la collecte de données, définissez [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/) sur `true`. Gardez à l'esprit que cela ne restaurera pas les données précédemment effacées.

## Collecte de l'IDFV {#idfv-collection}

Dans les versions antérieures du SDK iOS de Braze, le champ IDFV (Identifier for Vendor) était automatiquement collecté comme identifiant d'appareil de l'utilisateur. À partir du SDK Swift `v5.7.0`, le champ IDFV pouvait être désactivé de manière facultative, et Braze définissait à la place un UUID aléatoire comme identifiant d'appareil. À partir du SDK Swift `v7.0.0`, le champ IDFV n'est plus collecté par défaut, et un UUID est défini comme identifiant d'appareil à la place.

La fonctionnalité `useUUIDAsDeviceId` configure le [SDK Swift](https://github.com/braze-inc/braze-swift-sdk) pour définir l'identifiant d'appareil comme UUID. Traditionnellement, le SDK iOS attribuait un identifiant d'appareil égal à la valeur IDFV générée par Apple. Avec cette fonctionnalité activée par défaut sur votre application iOS, tous les nouveaux utilisateurs créés via le SDK se voient attribuer un identifiant d'appareil égal à un UUID.

Si vous souhaitez toujours collecter l'IDFV séparément, vous pouvez utiliser [`set(identifierforvendor:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforvendor:)).

{% alert note %}
La lecture de `braze.deviceId` bloque le thread appelant jusqu'à ce que le SDK ait terminé ses opérations post-initialisation. Pour les contextes sensibles à la latence ou exécutés sur le thread principal, utilisez plutôt les alternatives non bloquantes.

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

Dans le SDK Swift `v7.0.0+`, lorsque `useUUIDAsDeviceId` est activé (par défaut), tous les nouveaux utilisateurs créés se voient attribuer un identifiant d'appareil aléatoire. Tous les utilisateurs existants conservent leur valeur d'identifiant d'appareil actuelle, qui peut avoir été un IDFV.

Lorsque cette fonctionnalité n'est pas activée, les appareils continuent de se voir attribuer l'IDFV lors de leur création.

#### En aval {#downstream}

**Partenaires technologiques** : lorsque cette fonctionnalité est activée, les partenaires technologiques qui dérivent la valeur IDFV de l'identifiant d'appareil Braze n'auront plus accès à cette donnée. Si la valeur IDFV dérivée de l'appareil est nécessaire pour l'intégration de votre partenaire, nous vous recommandons de définir cette fonctionnalité sur `false`.

**Currents** : lorsque `useUUIDAsDeviceId` est défini sur true, l'identifiant d'appareil envoyé dans Currents ne correspondra plus à la valeur IDFV.

### Foire aux questions {#frequently-asked-questions}

#### Ce changement aura-t-il un impact sur mes utilisateurs existants dans Braze ? {#will-this-change-impact-my-existing-users-in-braze}

Non. Lorsqu'elle est activée, cette fonctionnalité n'écrase aucune donnée utilisateur dans Braze. Les nouveaux identifiants d'appareil UUID ne seront créés que pour les nouveaux appareils ou lorsque `wipeData()` est appelé.

#### Puis-je désactiver cette fonctionnalité après l'avoir activée ? {#can-i-turn-this-feature-off-after-turning-it-on}

Oui, cette fonctionnalité peut être activée et désactivée à votre discrétion. Les identifiants d'appareil précédemment stockés ne seront jamais écrasés.

#### Puis-je toujours collecter la valeur IDFV via Braze par un autre moyen ? {#can-i-still-capture-the-idfv-value-through-braze-elsewhere}

Oui, vous pouvez toujours collecter l'IDFV de manière facultative via le SDK Swift (la collecte est désactivée par défaut).