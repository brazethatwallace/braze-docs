{% multi_lang_include developer_guide/prerequisites/xamarin.md %}

## Conditions préalables {#prerequisites}

Voici les versions minimales requises du SDK pour commencer à utiliser les géorepérages :

{% sdk_min_versions xamarin:9.0.0 %}

## Configuration des géorepérages {#setting-up-geofences}

### Étape 1 : Activer dans Braze {#step-1-enable-in-braze}

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

---

Veuillez ensuite suivre les instructions spécifiques à la plateforme ci-dessous, pour Android ou iOS :

{% tabs %}
{% tab Android %}

### Étape 2 : Ajouter des dépendances {#step-2-add-dependencies}

Ajoutez la référence au package NuGet suivante à votre projet :

- `BrazePlatform.BrazeAndroidLocationBinding`

### Étape 3 : Mettre à jour votre AndroidManifest.xml {#step-3-update-your-androidmanifestxml}

Ajoutez les autorisations suivantes à votre `AndroidManifest.xml` :

```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
```

{% alert important %}
L'autorisation d'accès à la localisation en arrière-plan est nécessaire pour que les géorepérages fonctionnent lorsque l'application est en arrière-plan sur les appareils Android 10+.
{% endalert %}

### Étape 4 : Configurer la collecte de localisation Braze {#step-4-configure-braze-location-collection}

Assurez-vous que la collecte de localisation est activée dans votre configuration Braze. Si vous souhaitez activer les géorepérages sans collecte automatique de localisation, définissez les paramètres suivants dans votre `Braze.xml` :

```xml
<bool name="com_braze_enable_location_collection">true</bool>
<bool name="com_braze_geofences_enabled">true</bool>
```

### Étape 5 : Demander les autorisations de localisation lors de l'exécution {#step-5-request-location-permissions-at-runtime}

Vous devez demander les autorisations de localisation à l'utilisateur avant d'enregistrer les géorepérages. Dans votre code C#, utilisez le modèle suivant :

```csharp
using AndroidX.Core.App;
using AndroidX.Core.Content;

private void RequestLocationPermission()
{
  // ...existing code for checking and requesting permissions...
}

public override void OnRequestPermissionsResult(int requestCode, string[] permissions, Permission[] grantResults)
{
  // ...existing code for handling permission result...
}
```

Une fois les autorisations accordées, initialisez la collecte de localisation Braze :

```csharp
Braze.GetInstance(this).RequestLocationInitialization();
```

### Étape 6 : Demander manuellement des mises à jour de géorepérage (facultatif) {#step-6-manually-request-geofence-updates-optional}

Pour demander manuellement des géorepérages pour un emplacement spécifique :

```csharp
Braze.GetInstance(this).RequestGeofences(latitude, longitude);
```

{% alert important %}
Les géorepérages ne peuvent être demandés qu'une seule fois par session, soit automatiquement par le SDK, soit manuellement avec cette méthode.
{% endalert %}
{% endtab %}
{% tab iOS %}

### Étape 2 : Ajouter des dépendances

Ajoutez la référence au package NuGet suivante à votre projet :

- `Braze.iOS.BrazeLocation`

### Étape 3 : Configurer l'utilisation de la localisation dans Info.plist {#step-3-configure-location-usage-in-infoplist}

Ajoutez une chaîne de caractères de description d'utilisation pour les services de localisation dans votre `Info.plist` :

```xml
<key>NSLocationAlwaysAndWhenInUseUsageDescription</key>
<string>This app uses your location to enable geofences and location-based messaging.</string>
<key>NSLocationWhenInUseUsageDescription</key>
<string>This app uses your location to enable geofences and location-based messaging.</string>
```

{% alert important %}
Apple a déprécié `NSLocationAlwaysUsageDescription`. Utilisez les clés ci-dessus pour iOS 14 et versions ultérieures.
{% endalert %}

### Étape 4 : Activer les géorepérages dans votre configuration Braze {#step-4-enable-geofences-in-your-braze-configuration}

Dans le code de démarrage de votre application (par exemple, `App.xaml.cs`), configurez Braze avec les géorepérages activés :

```csharp
using BrazeKit;
using BrazeLocation;

var configuration = new BRZConfiguration("<BRAZE_API_KEY>", "<BRAZE_ENDPOINT>");
configuration.Location.BrazeLocationProvider = new BrazeLocationProvider();
configuration.Location.AutomaticLocationCollection = true;
configuration.Location.GeofencesEnabled = true;
configuration.Location.AutomaticGeofenceRequests = true;
// ...other configuration...
var braze = new Braze(configuration);
```

### Étape 5 : Activer les mises à jour de localisation en arrière-plan (facultatif) {#step-5-enable-background-location-updates-optional}

Pour surveiller les géorepérages en arrière-plan, activez le mode arrière-plan **Location updates** en ajoutant la configuration suivante à votre `Info.plist` :

```xml
<key>UIBackgroundModes</key>
<array>
  <string>location</string>
</array>
```

Ensuite, dans votre configuration Braze, définissez :

```csharp
configuration.Location.AllowBackgroundGeofenceUpdates = true;
configuration.Location.DistanceFilter = 8000; // meters
```

{% alert important %}
Définissez `DistanceFilter` sur une valeur adaptée aux besoins de votre application afin d'éviter une consommation excessive de la batterie.
{% endalert %}

### Étape 6 : Demander l'autorisation de localisation {#step-6-request-location-authorization}

Demandez l'autorisation `When In Use` ou `Always` à l'utilisateur :

```csharp
using CoreLocation;

var locationManager = new CLLocationManager();
locationManager.RequestWhenInUseAuthorization();
// or
locationManager.RequestAlwaysAuthorization();
```

{% alert important %}
Sans l'autorisation `Always`, iOS empêche les services de localisation de fonctionner lorsque l'application n'est pas utilisée. Cette restriction est appliquée par le système d'exploitation et ne peut pas être contournée par le SDK Braze.
{% endalert %}
{% endtab %}
{% endtabs %}