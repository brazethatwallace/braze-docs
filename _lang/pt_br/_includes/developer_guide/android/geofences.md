{% multi_lang_include developer_guide/prerequisites/android.md %}

## Configurando geofences {#setting-up-geofences}

### Etapa 1: Ativar na Braze {#step-1-enable-in-braze}

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### Etapa 2: Atualize `build.gradle` {#step-2-update-buildgradle}

Adicione `android-sdk-location` ao `build.gradle` do nível do app. Além disso, adicione o [pacote de localização](https://developers.google.com/android/reference/com/google/android/gms/location/package-summary) do Google Play Services usando o [guia de configuração](https://developers.google.com/android/guides/setup) do Google Play Services:

```
dependencies {
  implementation "com.braze:android-sdk-location:+"
  implementation "com.google.android.gms:play-services-location:${PLAY_SERVICES_VERSION}"
}
```

### Etapa 3: Atualizar o manifesto {#step-3-update-the-manifest}

Adicione permissões de inicialização, localização precisa e localização em segundo plano ao seu `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
```

{% alert important %}
A permissão de acesso à localização em segundo plano foi adicionada no Android 10 e é necessária para que os geofences funcionem enquanto o app estiver em segundo plano em todos os dispositivos Android 10+.
{% endalert %}

Adicione o receptor de inicialização da Braze ao elemento `application` do seu `AndroidManifest.xml`:

```xml
<receiver android:name="com.braze.BrazeBootReceiver">
  <intent-filter>
    <action android:name="android.intent.action.BOOT_COMPLETED" />
  </intent-filter>
</receiver>
```

### Etapa 4: Ativar a coleta de localização da Braze {#step-4-enable-braze-location-collection}

Se ainda não tiver ativado a coleta de localização da Braze, atualize seu arquivo `braze.xml` para incluir `com_braze_enable_location_collection` e confirme que seu valor está definido como `true`:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
A partir da versão 3.6.0 do SDK or kit de desenvolvimento de software da Braze para Android, a coleta de localização da Braze é desativada por padrão.
{% endalert %}

Os geofences da Braze são ativados se a coleta de localização da Braze estiver ativada. Se você quiser fazer o descadastramento da nossa coleta de localização padrão, mas ainda quiser usar geofences, isso pode ser ativado seletivamente definindo o valor da chave `com_braze_geofences_enabled` como `true` em `braze.xml`, independentemente do valor de `com_braze_enable_location_collection`:

```xml
<bool name="com_braze_geofences_enabled">true</bool>
```

### Etapa 5: Obter permissões de localização do usuário final {#step-5-obtain-location-permissions-from-the-end-user}

Para Android M e versões superiores, é necessário solicitar permissões de localização ao usuário final antes de coletar informações de localização ou registrar geofences.

Adicione a seguinte chamada para notificar a Braze quando um usuário conceder a permissão de localização ao seu app:

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

Isso fará com que o SDK or kit de desenvolvimento de software solicite geofences dos servidores da Braze e inicialize o rastreamento de geofences.

Veja [`RuntimePermissionUtils.java`](https://github.com/braze-inc/braze-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/util/RuntimePermissionUtils.kt) no nosso aplicativo de exemplo para ver uma implementação de referência.

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

O uso do código de exemplo anterior é feito da seguinte forma:

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

### Etapa 6: Solicitar manualmente atualizações de geofence (opcional) {#step-6-manually-request-geofence-updates-optional}

Por padrão, a Braze recupera automaticamente a localização do dispositivo e solicita geofences com base nessa localização coletada. No entanto, você pode fornecer manualmente uma coordenada GPS que será usada para recuperar geofences da Braze próximos. Para solicitar geofences da Braze manualmente, você deve desativar as solicitações automáticas de geofence e fornecer uma coordenada GPS para as solicitações.

#### Etapa 6.1: Desativar solicitações automáticas de geofence {#step-61-disable-automatic-geofence-requests}

As solicitações automáticas de geofence da Braze podem ser desativadas no seu arquivo `braze.xml`, definindo `com_braze_automatic_geofence_requests_enabled` como `false`:

```xml
<bool name="com_braze_automatic_geofence_requests_enabled">false</bool>
```

Isso também pode ser feito em tempo de execução por meio de:

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

#### Etapa 6.2: Solicitar manualmente geofence da Braze com coordenada GPS {#step-62-manually-request-braze-geofence-with-gps-coordinate}

Os geofences da Braze são solicitados manualmente por meio do método [`requestGeofences()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-geofences.html):

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
Os geofences só podem ser solicitados uma vez por sessão, seja automaticamente pelo SDK or kit de desenvolvimento de software ou manualmente com esse método.
{% endalert %}