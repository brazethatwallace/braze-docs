{% multi_lang_include developer_guide/prerequisites/android.md %}

## Configuration des géorepérages {#setting-up-geofences}

### Étape 1 : Activer dans Braze {#step-1-enable-in-braze}

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### Étape 2 : Mettre à jour `build.gradle` {#step-2-update-buildgradle}

Ajoutez `android-sdk-location` à votre `build.gradle` au niveau de l'application. Ajoutez également le [package de localisation](https://developers.google.com/android/reference/com/google/android/gms/location/package-summary) des services Google Play en utilisant le [guide de configuration](https://developers.google.com/android/guides/setup) des services Google Play :

```
dependencies {
  implementation "com.braze:android-sdk-location:+"
  implementation "com.google.android.gms:play-services-location:${PLAY_SERVICES_VERSION}"
}
```

### Étape 3 : Mettre à jour le manifeste {#step-3-update-the-manifest}

Ajoutez les autorisations de démarrage, de localisation précise et de localisation en arrière-plan à votre `AndroidManifest.xml` :

```xml
<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
```

{% alert important %}
L'autorisation d'accès à la localisation en arrière-plan a été ajoutée dans Android 10 et est requise pour que les géorepérages fonctionnent lorsque l'application est en arrière-plan sur tous les appareils Android 10 et ultérieurs.
{% endalert %}

Ajoutez le récepteur de démarrage Braze à l'élément `application` de votre `AndroidManifest.xml` :

```xml
<receiver android:name="com.braze.BrazeBootReceiver">
  <intent-filter>
    <action android:name="android.intent.action.BOOT_COMPLETED" />
  </intent-filter>
</receiver>
```

### Étape 4 : Activer la collecte de localisation Braze {#step-4-enable-braze-location-collection}

Si vous n'avez pas encore activé la collecte de localisation Braze, mettez à jour votre fichier `braze.xml` pour y inclure `com_braze_enable_location_collection` et confirmez que sa valeur est définie sur `true` :

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
À partir de la version 3.6.0 du SDK Braze pour Android, la collecte de localisation Braze est désactivée par défaut.
{% endalert %}

Les géorepérages Braze sont activés si la collecte de localisation Braze est activée. Si vous souhaitez désactiver la collecte de localisation par défaut tout en continuant à utiliser les géorepérages, vous pouvez les activer de manière sélective en définissant la valeur de la clé `com_braze_geofences_enabled` sur `true` dans `braze.xml`, indépendamment de la valeur de `com_braze_enable_location_collection` :

```xml
<bool name="com_braze_geofences_enabled">true</bool>
```

### Étape 5 : Obtenir les autorisations de localisation de l'utilisateur final {#step-5-obtain-location-permissions-from-the-end-user}

Pour Android M et les versions ultérieures, vous devez demander les autorisations de localisation à l'utilisateur final avant de collecter des informations de localisation ou d'enregistrer des géorepérages.

Ajoutez l'appel suivant pour notifier Braze lorsqu'un utilisateur accorde l'autorisation de localisation à votre application :

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

Le SDK demandera alors des géorepérages aux serveurs Braze et initialisera le suivi des géorepérages.

Consultez [`RuntimePermissionUtils.java`](https://github.com/braze-inc/braze-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/util/RuntimePermissionUtils.kt) dans notre exemple d'application pour un exemple d'implémentation.

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

Voici comment utiliser l'exemple de code précédent :

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

### Étape 6 : Demander manuellement des mises à jour de géorepérage (facultatif) {#step-6-manually-request-geofence-updates-optional}

Par défaut, Braze récupère automatiquement la localisation de l'appareil et demande des géorepérages en fonction de la localisation collectée. Cependant, vous pouvez fournir manuellement une coordonnée GPS qui sera utilisée pour récupérer les géorepérages Braze à proximité. Pour demander manuellement des géorepérages Braze, vous devez désactiver les demandes automatiques de géorepérage Braze et fournir une coordonnée GPS pour les demandes.

#### Étape 6.1 : Désactiver les demandes automatiques de géorepérage {#step-61-disable-automatic-geofence-requests}

Les demandes automatiques de géorepérage Braze peuvent être désactivées dans votre fichier `braze.xml` en définissant `com_braze_automatic_geofence_requests_enabled` sur `false` :

```xml
<bool name="com_braze_automatic_geofence_requests_enabled">false</bool>
```

Cela peut également être effectué au moment de l'exécution via :

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

#### Étape 6.2 : Demander manuellement un géorepérage Braze avec des coordonnées GPS {#step-62-manually-request-braze-geofence-with-gps-coordinate}

Les géorepérages Braze sont demandés manuellement via la méthode [`requestGeofences()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-geofences.html) :

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
Les géorepérages ne peuvent être demandés qu'une seule fois par session, soit automatiquement par le SDK, soit manuellement avec cette méthode.
{% endalert %}