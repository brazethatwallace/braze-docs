{% multi_lang_include developer_guide/prerequisites/xamarin.md %}

## Requisitos previos {#prerequisites}

Estas son las versiones mínimas del SDK or kit de desarrollo de software necesarias para empezar a utilizar geovallas:

{% sdk_min_versions xamarin:9.0.0 %}

## Configuración de geovallas {#setting-up-geofences}

### Paso 1: Habilitar en Braze {#step-1-enable-in-braze}

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

---

A continuación, sigue las instrucciones específicas de la plataforma para Android o iOS:

{% tabs %}
{% tab Android %}

### Paso 2: Añadir dependencias {#step-2-add-dependencies}

Añade la siguiente referencia al paquete NuGet a tu proyecto:

- `BrazePlatform.BrazeAndroidLocationBinding`

### Paso 3: Actualiza tu AndroidManifest.xml {#step-3-update-your-androidmanifestxml}

Añade los siguientes permisos a tu `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
```

{% alert important %}
Se requiere el permiso de acceso a la ubicación en segundo plano para que las geovallas funcionen mientras la aplicación está en segundo plano en dispositivos con Android 10 o superior.
{% endalert %}

### Paso 4: Configurar la recopilación de ubicación de Braze {#step-4-configure-braze-location-collection}

Asegúrate de que la recopilación de ubicación esté habilitada en tu configuración de Braze. Si deseas habilitar las geovallas sin la recopilación automática de la ubicación, configura lo siguiente en tu `Braze.xml`:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
<bool name="com_braze_geofences_enabled">true</bool>
```

### Paso 5: Solicitar permisos de ubicación en tiempo de ejecución {#step-5-request-location-permissions-at-runtime}

Debes solicitar permisos de ubicación al usuario antes de registrar geovallas. En tu código C#, utiliza el siguiente patrón:

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

Una vez concedidos los permisos, inicializa la recopilación de ubicación de Braze:

```csharp
Braze.GetInstance(this).RequestLocationInitialization();
```

### Paso 6: Solicitar manualmente actualizaciones de geovallas (opcional) {#step-6-manually-request-geofence-updates-optional}

Para solicitar manualmente geovallas para una ubicación específica:

```csharp
Braze.GetInstance(this).RequestGeofences(latitude, longitude);
```

{% alert important %}
Las geovallas solo pueden solicitarse una vez por sesión, ya sea automáticamente por el SDK or kit de desarrollo de software o manualmente con este método.
{% endalert %}
{% endtab %}
{% tab iOS %}

### Paso 2: Añadir dependencias

Añade la siguiente referencia al paquete NuGet a tu proyecto:

- `Braze.iOS.BrazeLocation`

### Paso 3: Configura el uso de la ubicación en Info.plist {#step-3-configure-location-usage-in-infoplist}

Añade una cadena con la descripción del uso de los servicios de ubicación en tu `Info.plist`:

```xml
<key>NSLocationAlwaysAndWhenInUseUsageDescription</key>
<string>This app uses your location to enable geofences and location-based messaging.</string>
<key>NSLocationWhenInUseUsageDescription</key>
<string>This app uses your location to enable geofences and location-based messaging.</string>
```

{% alert important %}
Apple ha dejado de utilizar `NSLocationAlwaysUsageDescription`. Utiliza las claves anteriores para iOS 14+.
{% endalert %}

### Paso 4: Habilita las geovallas en tu configuración de Braze {#step-4-enable-geofences-in-your-braze-configuration}

En el código de inicio de tu aplicación (por ejemplo, `App.xaml.cs`), configura Braze con las geovallas habilitadas:

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

### Paso 5: Habilita las actualizaciones de ubicación en segundo plano (opcional) {#step-5-enable-background-location-updates-optional}

Para supervisar las geovallas en segundo plano, habilita el modo de fondo **Location updates** añadiendo la siguiente configuración a tu `Info.plist`:

```xml
<key>UIBackgroundModes</key>
<array>
  <string>location</string>
</array>
```

A continuación, en tu configuración de Braze, establece:

```csharp
configuration.Location.AllowBackgroundGeofenceUpdates = true;
configuration.Location.DistanceFilter = 8000; // meters
```

{% alert important %}
Establece `DistanceFilter` con un valor que se ajuste a las necesidades de tu aplicación para evitar que se agote la batería.
{% endalert %}

### Paso 6: Solicitar autorización de ubicación {#step-6-request-location-authorization}

Solicita al usuario la autorización `When In Use` o `Always`:

```csharp
using CoreLocation;

var locationManager = new CLLocationManager();
locationManager.RequestWhenInUseAuthorization();
// or
locationManager.RequestAlwaysAuthorization();
```

{% alert important %}
Sin la autorización `Always`, iOS restringe el funcionamiento de los servicios de ubicación mientras la aplicación no está en uso. Esto lo impone el sistema operativo y el SDK or kit de desarrollo de software de Braze no puede eludirlo.
{% endalert %}
{% endtab %}
{% endtabs %}