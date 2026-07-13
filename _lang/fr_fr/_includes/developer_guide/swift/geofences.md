{% alert important %}
À partir d'iOS 14, les géorepérages ne fonctionnent pas de manière fiable pour les utilisateurs qui choisissent de n'autoriser que leur emplacement approximatif.
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Configuration des géorepérages {#setting-up-geofences}

### Étape 1 : Activer dans Braze {#step-1-enable-in-braze}

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### Étape 2 : Activer les services de localisation de votre application {#step-2-enable-your-apps-location-services}

Par défaut, les services de localisation de Braze ne sont pas activés. Pour les activer dans votre application, suivez les étapes ci-dessous. Pour un tutoriel étape par étape, consultez [Tutoriel : Emplacements Braze et géorepérages](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/).

#### Étape 2.1 : Ajouter le module `BrazeLocation` {#step-21-add-the-brazelocation-module}

Dans Xcode, ouvrez l'onglet **General**. Sous **Frameworks, Libraries, and Embedded Content**, ajoutez le module `BrazeLocation`.

![Ajout du module BrazeLocation dans votre projet Xcode]({% image_buster /assets/img/sdk_geofences/add-brazeLocation-module-xcode.png %})

#### Étape 2.2 : Mettre à jour votre `Info.plist` {#step-22-update-your-infoplist}

Dans votre `info.plist`, attribuez une valeur `String` à l'une des clés suivantes qui décrit pourquoi votre application doit suivre la localisation. Cette chaîne de caractères s'affichera lorsque vos utilisateurs seront invités à activer les services de localisation. Veillez donc à expliquer clairement l'intérêt d'activer cette fonctionnalité pour votre application.

- `NSLocationAlwaysAndWhenInUseUsageDescription`
- `NSLocationWhenInUseUsageDescription`

![Chaînes de caractères de localisation dans Info.plist sous Xcode]({% image_buster /assets/img/sdk_geofences/info-plist-location-strings.png %})

{% alert important %}
Apple a déprécié `NSLocationAlwaysUsageDescription`. Pour plus d'informations, consultez [la documentation pour développeurs d'Apple](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationalwaysusagedescription).
{% endalert %}

### Étape 3 : Activer les géorepérages dans votre code {#step-3-enable-geofences-in-your-code}

Dans le code de votre application, activez les géorepérages en définissant `location.geofencesEnabled` sur `true` dans l'objet `configuration` qui initialise l'instance [`Braze`](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/). Pour d'autres options de configuration `location`, consultez la [référence du SDK Braze Swift](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/location-swift.class).

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
configuration.location.brazeLocationProvider = BrazeLocationProvider()
configuration.location.automaticLocationCollection = true
configuration.location.geofencesEnabled = true
configuration.location.automaticGeofenceRequests = true

// Additional configuration customization...

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                    endpoint:brazeEndpoint];
configuration.logger.level = BRZLoggerLevelInfo;
configuration.location.brazeLocationProvider = [[BrazeLocationProvider alloc] init];
configuration.location.automaticLocationCollection = YES;
configuration.location.geofencesEnabled = YES;
configuration.location.automaticGeofenceRequests = YES;

// Additional configuration customization...

Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

#### Étape 3.1 : Activer les rapports en arrière-plan (facultatif) {#step-31-enable-background-reporting-optional}

Par défaut, les événements de géorepérage ne sont surveillés que si votre application est au premier plan ou dispose de l'autorisation `Always`, qui surveille tous les états de l'application.

Cependant, vous pouvez également choisir de surveiller les événements de géorepérage si votre application est en arrière-plan ou dispose de [l'autorisation `When In Use`](#swift_request-authorization).

Pour surveiller ces événements de géorepérage supplémentaires, ouvrez votre projet Xcode, puis accédez à **Signing & Capabilities**. Sous **Background Modes**, cochez **Location updates**.

![Dans Xcode, Background Mode > Location Updates]({% image_buster /assets/img/sdk_geofences/xcode-background-modes-location-updates.png %})

Ensuite, activez `allowBackgroundGeofenceUpdates` dans le code de votre application. Cela permet à Braze de prolonger le statut « When In Use » de votre application en surveillant en permanence les mises à jour de localisation. Ce paramètre ne fonctionne que lorsque votre application est en arrière-plan. Lorsque l'application se rouvre, tous les processus d'arrière-plan existants sont mis en pause et les processus de premier plan sont prioritaires.

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)

// Additional configuration customization...

// Enable background geofence reporting with `When In Use` authorization.
configuration.location.allowBackgroundGeofenceUpdates = true

// Determines the number of meters required to trigger a new location update.
configuration.location.distanceFilter = 8000

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                    endpoint:brazeEndpoint];

// Additional configuration customization...

// Enable background geofence reporting with `When In Use` authorization.
configuration.location.allowBackgroundGeofenceUpdates = YES;

// Determines the number of meters required to trigger a new location update.
configuration.location.distanceFilter = 8000;

Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

{% alert important %}
Afin d'éviter une décharge excessive de la batterie et une limitation du débit, configurez `distanceFilter` à une valeur qui répond aux besoins spécifiques de votre application. En définissant une valeur plus élevée pour `distanceFilter`, vous évitez que votre application ne demande trop souvent la localisation de l'utilisateur.
{% endalert %}

### Étape 4 : Demander l'autorisation {#request-authorization}

Lorsque vous sollicitez l'autorisation d'un utilisateur, demandez l'autorisation `When In Use` ou `Always`.

{% tabs local %}
{% tab When In Use %}
Pour demander l'autorisation `When In Use`, utilisez la méthode `requestWhenInUseAuthorization()` :

{% subtabs %}
{% subtab swift %}
```swift
var locationManager = CLLocationManager()
locationManager.requestWhenInUseAuthorization()
```
{% endsubtab %}

{% subtab OBJECTIVE-C %}
```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestWhenInUseAuthorization];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Always %}
Par défaut, `requestAlwaysAuthorization()` n'accorde à votre application que l'autorisation `When In Use` et demandera à nouveau à votre utilisateur l'autorisation `Always` après un certain temps.

Cependant, vous pouvez choisir de solliciter immédiatement votre utilisateur en appelant d'abord `requestWhenInUseAuthorization()`, puis en appelant `requestAlwaysAuthorization()` après avoir reçu votre autorisation initiale `When In Use`.

{% alert important %}
Vous ne pouvez demander immédiatement l'autorisation `Always` qu'une seule fois.
{% endalert %}

{% subtabs %}
{% subtab swift %}
```swift
var locationManager = CLLocationManager()
locationManager.requestAlwaysAuthorization()
```
{% endsubtab %}

{% subtab OBJECTIVE-C %}
```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestAlwaysAuthorization];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Demander manuellement des géorepérages {#manually-request-geofences}

Lorsque le SDK Braze demande des géorepérages au backend, il communique la localisation actuelle de l'utilisateur et reçoit les géorepérages jugés les plus pertinents en fonction de la localisation communiquée.

Pour contrôler la localisation que le SDK signale afin de recevoir les géorepérages les plus pertinents, vous pouvez demander manuellement des géorepérages en fournissant les coordonnées souhaitées.

### Étape 1 : Définir `automaticGeofenceRequests` sur `false` {#step-1-set-automaticgeofencerequests-to-false}

Vous pouvez désactiver les demandes automatiques de géorepérage dans votre objet `configuration` passé à [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/init(configuration:)). Définissez `automaticGeofenceRequests` sur `false`.

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "{BRAZE_API_KEY}",
  endpoint: "{BRAZE_ENDPOINT}"
)
configuration.automaticGeofencesRequest = false
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration =
  [[BRZConfiguration alloc] initWithApiKey:{BRAZE_API_KEY}
                                  endpoint:{BRAZE_ENDPOINT}];
configuration.automaticGeofencesRequest = NO;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

### Étape 2 : Appeler `requestGeofences` manuellement {#step-2-call-requestgeofences-manually}

Dans votre code, demandez des géorepérages avec la latitude et la longitude appropriées.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.requestGeofences(latitude: latitude, longitude: longitude)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze requestGeofencesWithLatitude:latitude
                                      longitude:longitude];
```

{% endtab %}
{% endtabs %}

## Foire aux questions (FAQ) {#faq}

### Pourquoi est-ce que je ne reçois pas de géorepérages sur mon appareil ? {#why-am-i-not-receiving-geofences-on-my-device}

Pour vérifier si les géorepérages sont bien reçus sur votre appareil, commencez par utiliser l'[outil de débogage du SDK]({{site.baseurl}}/developer_guide/sdk_integration/debugging#debugging-the-braze-sdk) afin de consulter les journaux du SDK. Vous pourrez alors vérifier si les géorepérages sont correctement reçus depuis le serveur et s'il existe des erreurs notables.

Voici d'autres raisons possibles pour lesquelles les géorepérages peuvent ne pas être reçus sur votre appareil :

#### Limitations du système d'exploitation iOS {#ios-operating-system-limitations}

Le système d'exploitation iOS ne permet de stocker que 20 géorepérages maximum pour une application donnée. Avec les géorepérages activés, Braze utilisera une partie de ces 20 emplacements disponibles.

Afin d'éviter toute perturbation accidentelle ou indésirable des autres fonctionnalités liées aux géorepérages dans votre application, vous devez activer les géorepérages de localisation pour chaque application sur le tableau de bord. Pour que nos services de localisation fonctionnent correctement, vérifiez que votre application n'utilise pas tous les emplacements de géorepérage disponibles.

#### Limitation du débit {#rate-limiting}

Braze impose une limite d'une actualisation de géorepérage par session afin d'éviter les requêtes superflues.

### Comment cela fonctionne-t-il si j'utilise à la fois les fonctionnalités de géorepérage de Braze et d'autres fournisseurs ? {#how-does-it-work-if-i-am-using-both-braze-and-non-braze-geofence-features}

Comme mentionné précédemment, iOS permet à une seule application de stocker un maximum de 20 géorepérages. Cet espace de stockage est partagé entre les géorepérages Braze et les autres, et il est géré par [CLLocationManager](https://developer.apple.com/documentation/corelocation/cllocationmanager).

Par exemple, si votre application contient 20 géorepérages non Braze, il n'y aurait pas d'espace disponible pour suivre les géorepérages Braze (et vice versa). Afin de recevoir de nouveaux géorepérages, vous devrez utiliser [les API de localisation d'Apple](https://developer.apple.com/documentation/corelocation) pour désactiver la surveillance de certains géorepérages existants sur l'appareil.

### La fonctionnalité de géorepérage peut-elle être utilisée lorsqu'un appareil est hors ligne ? {#can-the-geofences-feature-be-used-while-a-device-is-offline}

Un appareil doit être connecté à Internet uniquement lors d'une actualisation. Une fois les géorepérages reçus avec succès depuis le serveur, il est possible d'enregistrer une entrée ou une sortie de géorepérage même si l'appareil est hors ligne. En effet, la localisation d'un appareil fonctionne indépendamment de sa connexion Internet.

Par exemple, supposons qu'un appareil ait reçu et enregistré avec succès des géorepérages au début de la session, puis se déconnecte. Si l'utilisateur pénètre dans l'une de ces zones de géorepérage enregistrées, cela peut déclencher une Campaign Braze.

### Pourquoi les géorepérages ne sont-ils pas surveillés lorsque mon application est en arrière-plan ou fermée ? {#why-are-geofences-not-monitored-when-my-app-is-backgroundedterminated}

Sans l'autorisation `Always`, Apple limite l'exécution des services de localisation lorsqu'une application n'est pas utilisée. Cette mesure est appliquée par le système d'exploitation et échappe au contrôle du SDK Braze. Bien que Braze propose des configurations distinctes pour exécuter des services lorsque l'application est en arrière-plan, il n'existe aucun moyen de contourner ces restrictions pour les applications fermées sans l'autorisation explicite de l'utilisateur.