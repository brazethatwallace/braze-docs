{% multi_lang_include developer_guide/prerequisites/xamarin.md %}

## Voraussetzungen {#prerequisites}

Dies sind die Mindestversionen des SDK, die erforderlich sind, um Geofences zu verwenden:

{% sdk_min_versions xamarin:9.0.0 %}

## Einrichten von Geofences {#setting-up-geofences}

### Schritt 1: Enablement in Braze {#step-1-enable-in-braze}

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

---

Befolgen Sie anschließend die unten aufgeführten plattformspezifischen Anweisungen für Android oder iOS:

{% tabs %}
{% tab Android %}

### Schritt 2: Abhängigkeiten hinzufügen {#step-2-add-dependencies}

Fügen Sie die folgende NuGet-Paket-Referenz zu Ihrem Projekt hinzu:

- `BrazePlatform.BrazeAndroidLocationBinding`

### Schritt 3: AndroidManifest.xml aktualisieren {#step-3-update-your-androidmanifestxml}

Fügen Sie die folgenden Berechtigungen zu Ihrer `AndroidManifest.xml` hinzu:

```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
```

{% alert important %}
Die Berechtigung für den Zugriff auf den Standort im Hintergrund ist erforderlich, damit Geofences funktionieren, während sich die App auf Android 10+-Geräten im Hintergrund befindet.
{% endalert %}

### Schritt 4: Braze-Standorterfassung konfigurieren {#step-4-configure-braze-location-collection}

Stellen Sie sicher, dass die Standorterfassung in Ihrer Braze-Konfiguration aktiviert ist. Wenn Sie Geofences ohne automatische Standorterfassung aktivieren möchten, nehmen Sie die folgenden Einstellungen in Ihrer `Braze.xml` vor:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
<bool name="com_braze_geofences_enabled">true</bool>
```

### Schritt 5: Standortberechtigungen zur Laufzeit anfordern {#step-5-request-location-permissions-at-runtime}

Sie müssen Standortberechtigungen von den Nutzer:innen anfordern, bevor Sie Geofences registrieren. Verwenden Sie in Ihrem C#-Code das folgende Muster:

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

Nachdem die Berechtigungen erteilt wurden, initialisieren Sie die Braze-Standorterfassung:

```csharp
Braze.GetInstance(this).RequestLocationInitialization();
```

### Schritt 6: Geofence-Updates manuell anfordern (optional) {#step-6-manually-request-geofence-updates-optional}

Um Geofences für einen bestimmten Standort manuell anzufordern:

```csharp
Braze.GetInstance(this).RequestGeofences(latitude, longitude);
```

{% alert important %}
Geofences können nur einmal pro Sitzung angefordert werden – entweder automatisch durch das SDK oder manuell mit dieser Methode.
{% endalert %}
{% endtab %}
{% tab iOS %}

### Schritt 2: Abhängigkeiten hinzufügen

Fügen Sie die folgende NuGet-Paket-Referenz zu Ihrem Projekt hinzu:

- `Braze.iOS.BrazeLocation`

### Schritt 3: Standortnutzung in der Info.plist konfigurieren {#step-3-configure-location-usage-in-infoplist}

Fügen Sie einen Beschreibungstext für die Nutzung von Standortdiensten in Ihrer `Info.plist` hinzu:

```xml
<key>NSLocationAlwaysAndWhenInUseUsageDescription</key>
<string>This app uses your location to enable geofences and location-based messaging.</string>
<key>NSLocationWhenInUseUsageDescription</key>
<string>This app uses your location to enable geofences and location-based messaging.</string>
```

{% alert important %}
Apple hat `NSLocationAlwaysUsageDescription` als veraltet markiert. Verwenden Sie die oben genannten Schlüssel für iOS 14+.
{% endalert %}

### Schritt 4: Geofences in Ihrer Braze-Konfiguration aktivieren {#step-4-enable-geofences-in-your-braze-configuration}

Konfigurieren Sie Braze in Ihrem App-Startcode (z. B. `App.xaml.cs`) mit aktivierten Geofences:

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

### Schritt 5: Standort-Updates im Hintergrund aktivieren (optional) {#step-5-enable-background-location-updates-optional}

Um Geofences im Hintergrund zu überwachen, aktivieren Sie den Hintergrundmodus **Location updates**, indem Sie die folgende Konfiguration zu Ihrer `Info.plist` hinzufügen:

```xml
<key>UIBackgroundModes</key>
<array>
  <string>location</string>
</array>
```

Legen Sie anschließend in Ihrer Braze-Konfiguration Folgendes fest:

```csharp
configuration.Location.AllowBackgroundGeofenceUpdates = true;
configuration.Location.DistanceFilter = 8000; // meters
```

{% alert important %}
Setzen Sie `DistanceFilter` auf einen Wert, der den Anforderungen Ihrer App entspricht, um einen übermäßigen Batterieverbrauch zu vermeiden.
{% endalert %}

### Schritt 6: Standortautorisierung anfordern {#step-6-request-location-authorization}

Fordern Sie entweder die `When In Use`- oder die `Always`-Autorisierung von den Nutzer:innen an:

```csharp
using CoreLocation;

var locationManager = new CLLocationManager();
locationManager.RequestWhenInUseAuthorization();
// or
locationManager.RequestAlwaysAuthorization();
```

{% alert important %}
Ohne die `Always`-Autorisierung schränkt iOS die Ausführung von Standortdiensten ein, wenn die App nicht verwendet wird. Dies wird vom Betriebssystem erzwungen und kann vom Braze SDK nicht umgangen werden.
{% endalert %}
{% endtab %}
{% endtabs %}