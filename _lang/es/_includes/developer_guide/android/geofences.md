{% multi_lang_include developer_guide/prerequisites/android.md %}

## Configuración de geovallas {#setting-up-geofences}

### Paso 1: Habilitar en Braze {#step-1-enable-in-braze}

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### Paso 2: Actualiza `build.gradle` {#step-2-update-buildgradle}

Añade `android-sdk-location` al `build.gradle` a nivel de tu aplicación. Además, añade el [paquete de ubicación](https://developers.google.com/android/reference/com/google/android/gms/location/package-summary) de Google Play Services utilizando la [guía de configuración](https://developers.google.com/android/guides/setup) de Google Play Services:

```
dependencies {
  implementation "com.braze:android-sdk-location:+"
  implementation "com.google.android.gms:play-services-location:${PLAY_SERVICES_VERSION}"
}
```

### Paso 3: Actualiza el manifiesto {#step-3-update-the-manifest}

Añade permisos de arranque, ubicación precisa y ubicación en segundo plano a tu `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
```

{% alert important %}
El permiso de acceso a la ubicación en segundo plano se añadió en Android 10 y es necesario para que las geovallas funcionen mientras la aplicación está en segundo plano en todos los dispositivos Android 10+.
{% endalert %}

Añade el receptor de arranque de Braze al elemento `application` de tu `AndroidManifest.xml`:

```xml
<receiver android:name="com.braze.BrazeBootReceiver">
  <intent-filter>
    <action android:name="android.intent.action.BOOT_COMPLETED" />
  </intent-filter>
</receiver>
```

### Paso 4: Habilitar la recopilación de ubicaciones de Braze {#step-4-enable-braze-location-collection}

Si aún no has habilitado la recopilación de ubicaciones de Braze, actualiza tu archivo `braze.xml` para incluir `com_braze_enable_location_collection` y confirma que su valor es `true`:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
A partir de la versión 3.6.0 del SDK de Braze para Android, la recopilación de ubicaciones de Braze está desactivada de forma predeterminada.
{% endalert %}

Las geovallas de Braze se habilitan cuando la recopilación de ubicaciones de Braze está habilitada. Si deseas excluirte de nuestra recopilación predeterminada de ubicaciones, pero quieres seguir utilizando geovallas, puedes habilitarlas selectivamente estableciendo el valor de la clave `com_braze_geofences_enabled` en `true` en `braze.xml`, de forma independiente del valor de `com_braze_enable_location_collection`:

```xml
<bool name="com_braze_geofences_enabled">true</bool>
```

### Paso 5: Obtener permisos de ubicación del usuario final {#step-5-obtain-location-permissions-from-the-end-user}

Para Android M y versiones superiores, debes solicitar permisos de ubicación al usuario final antes de recopilar información de ubicación o registrar geovallas.

Añade la siguiente llamada para notificar a Braze cuando un usuario conceda el permiso de ubicación a tu aplicación:

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).requestLocationInitialization();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).requestLocationInitialization()
```

{% endtab %}
{% endtabs %}

Esto hará que el SDK solicite geovallas a los servidores de Braze e inicie el seguimiento de geovallas.

Consulta [`RuntimePermissionUtils.java`](https://github.com/braze-inc/braze-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/util/RuntimePermissionUtils.kt) en nuestra aplicación de ejemplo para ver un ejemplo de implementación.

{% tabs %}
{% tab JAVA %}

```java
public class RuntimePermissionUtils {
  private static final String TAG = BrazeLogger.getBrazeLogTag(RuntimePermissionUtils.class);
  public static final int DROIDBOY_PERMISSION_LOCATION = 40;

  public static void handleOnRequestPermissionsResult(Context context, int requestCode, int[] grantResults) {
    switch (requestCode) {
      case DROIDBOY_PERMISSION_LOCATION:
        // In Android Q, we require both FINE and BACKGROUND location permissions. Both
        // are requested simultaneously.
        if (areAllPermissionsGranted(grantResults)) {
          Log.i(TAG, "Required location permissions granted.");
          Toast.makeText(context, "Required location permissions granted.", Toast.LENGTH_SHORT).show();
          Braze.getInstance(context).requestLocationInitialization();
        } else {
          Log.i(TAG, "Required location permissions NOT granted.");
          Toast.makeText(context, "Required location permissions NOT granted.", Toast.LENGTH_SHORT).show();
        }
        break;
      default:
        break;
    }
  }

  private static boolean areAllPermissionsGranted(int[] grantResults) {
    for (int grantResult : grantResults) {
      if (grantResult != PackageManager.PERMISSION_GRANTED) {
        return false;
      }
    }
    return true;
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
object RuntimePermissionUtils {
  private val TAG = BrazeLogger.getBrazeLogTag(RuntimePermissionUtils::class.java!!)
  val DROIDBOY_PERMISSION_LOCATION = 40

  fun handleOnRequestPermissionsResult(context: Context, requestCode: Int, grantResults: IntArray) {
    when (requestCode) {
      DROIDBOY_PERMISSION_LOCATION ->
        // In Android Q, we require both FINE and BACKGROUND location permissions. Both
        // are requested simultaneously.
        if (areAllPermissionsGranted(grantResults)) {
          Log.i(TAG, "Required location permissions granted.")
          Toast.makeText(context, "Required location permissions granted.", Toast.LENGTH_SHORT).show()
          Braze.getInstance(context).requestLocationInitialization()
        } else {
          Log.i(TAG, "Required location permissions NOT granted.")
          Toast.makeText(context, "Required location permissions NOT granted.", Toast.LENGTH_SHORT).show()
        }
      else -> {
      }
    }
  }

  private fun areAllPermissionsGranted(grantResults: IntArray): Boolean {
    for (grantResult in grantResults) {
      if (grantResult != PackageManager.PERMISSION_GRANTED) {
        return false
      }
    }
    return true
  }
}
```

{% endtab %}
{% endtabs %}

El código de ejemplo anterior se utiliza de la siguiente manera:

{% tabs %}
{% tab JAVA %}

```java
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
  if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
    boolean hasAllPermissions = PermissionUtils.hasPermission(getApplicationContext(), Manifest.permission.ACCESS_BACKGROUND_LOCATION)
        && PermissionUtils.hasPermission(getApplicationContext(), Manifest.permission.ACCESS_FINE_LOCATION);
    if (!hasAllPermissions) {
      // Request both BACKGROUND and FINE location permissions
      requestPermissions(new String[]{android.Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_BACKGROUND_LOCATION},
          RuntimePermissionUtils.DROIDBOY_PERMISSION_LOCATION);
    }
  } else {
    if (!PermissionUtils.hasPermission(getApplicationContext(), Manifest.permission.ACCESS_FINE_LOCATION)) {
      // Request only FINE location permission
      requestPermissions(new String[]{android.Manifest.permission.ACCESS_FINE_LOCATION},
          RuntimePermissionUtils.DROIDBOY_PERMISSION_LOCATION);
    }
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
  if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
    val hasAllPermissions = PermissionUtils.hasPermission(applicationContext, Manifest.permission.ACCESS_BACKGROUND_LOCATION)
        && PermissionUtils.hasPermission(applicationContext, Manifest.permission.ACCESS_FINE_LOCATION)
    if (!hasAllPermissions) {
      // Request both BACKGROUND and FINE location permissions
      requestPermissions(arrayOf(android.Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_BACKGROUND_LOCATION),
          RuntimePermissionUtils.DROIDBOY_PERMISSION_LOCATION)
    }
  } else {
    if (!PermissionUtils.hasPermission(applicationContext, Manifest.permission.ACCESS_FINE_LOCATION)) {
      // Request only FINE location permission
      requestPermissions(arrayOf(android.Manifest.permission.ACCESS_FINE_LOCATION),
          RuntimePermissionUtils.DROIDBOY_PERMISSION_LOCATION)
    }
  }
}
```

{% endtab %}
{% endtabs %}

### Paso 6: Solicitar manualmente actualizaciones de geovallas (opcional) {#step-6-manually-request-geofence-updates-optional}

De forma predeterminada, Braze recupera automáticamente la ubicación del dispositivo y solicita geovallas basándose en esa ubicación recopilada. Sin embargo, puedes proporcionar manualmente una coordenada GPS que se utilizará para recuperar geovallas próximas de Braze. Para solicitar manualmente geovallas de Braze, debes desactivar las solicitudes automáticas de geovallas de Braze y proporcionar una coordenada GPS para las solicitudes.

#### Paso 6.1: Desactivar las solicitudes automáticas de geovallas {#step-61-disable-automatic-geofence-requests}

Las solicitudes automáticas de geovallas de Braze pueden desactivarse en tu archivo `braze.xml` configurando `com_braze_automatic_geofence_requests_enabled` como `false`:

```xml
<bool name="com_braze_automatic_geofence_requests_enabled">false</bool>
```

Esto también puede hacerse en tiempo de ejecución mediante:

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
    .setAutomaticGeofenceRequestsEnabled(false);
Braze.configure(getApplicationContext(), brazeConfigBuilder.build());
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfigBuilder = BrazeConfig.Builder()
    .setAutomaticGeofenceRequestsEnabled(false)
Braze.configure(applicationContext, brazeConfigBuilder.build())
```

{% endtab %}
{% endtabs %}

#### Paso 6.2: Solicitar manualmente geovallas de Braze con coordenadas GPS {#step-62-manually-request-braze-geofence-with-gps-coordinate}

Las geovallas de Braze se solicitan manualmente mediante el método [`requestGeofences()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-geofences.html):

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(getApplicationContext()).requestGeofences(latitude, longitude);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(applicationContext).requestGeofences(33.078947, -116.601356)
```

{% endtab %}
{% endtabs %}

{% alert important %}
Las geovallas solo pueden solicitarse una vez por sesión, ya sea automáticamente por el SDK o manualmente con este método.
{% endalert %}