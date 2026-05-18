{% multi_lang_include developer_guide/prerequisites/android.md %}

## ジオフェンスの設定 {#setting-up-geofences}

### ステップ 1: Brazeで有効にする {#step-1-enable-in-braze}

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### ステップ 2: `build.gradle`を更新する {#step-2-update-buildgradle}

`android-sdk-location`をアプリレベルの`build.gradle`に追加します。また、Google Play Servicesの[セットアップガイド](https://developers.google.com/android/guides/setup)を使用して、Google Play Servicesの[位置情報パッケージ](https://developers.google.com/android/reference/com/google/android/gms/location/package-summary)を追加します。

```
dependencies {
  implementation "com.braze:android-sdk-location:+"
  implementation "com.google.android.gms:play-services-location:${PLAY_SERVICES_VERSION}"
}
```

### ステップ 3: マニフェストを更新する {#step-3-update-the-manifest}

`AndroidManifest.xml`にブート、精度の高い位置情報、バックグラウンド位置情報の権限を追加します。

`````````xml
<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
```

{% alert important %}
バックグラウンド位置情報アクセス権限はAndroid 10で追加されたもので、Android 10以降のすべてのデバイスでは、アプリがバックグラウンドで動作している間ジオフェンスが機能するために必要です。
{% endalert %}

`AndroidManifest.xml`の`application`エレメントにBrazeブートレシーバーを追加します。

`````````xml
<receiver android:name="com.braze.BrazeBootReceiver">
  <intent-filter>
    <action android:name="android.intent.action.BOOT_COMPLETED" />
  </intent-filter>
</receiver>
```

### ステップ 4: Brazeの位置情報収集機能を有効にする {#step-4-enable-braze-location-collection}

まだBrazeの位置情報収集機能を有効にしていない場合は、`com_braze_enable_location_collection`を含むように`braze.xml`ファイルを更新し、その値が`true`に設定されていることを確認します。

`````````xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
Braze Android SDKバージョン3.6.0以降、Brazeの位置情報収集機能はデフォルトで無効になっています。
{% endalert %}

Brazeのジオフェンスは、Brazeの位置情報収集機能が有効になっている場合に有効になります。デフォルトの位置情報収集機能をオプトアウトしながらもジオフェンスを使用したい場合は、`com_braze_enable_location_collection`の値とは独立して、`braze.xml`のキー`com_braze_geofences_enabled`の値を`true`に設定することで、選択的に有効にすることができます。

`````````xml
<bool name="com_braze_geofences_enabled">true</bool>
```

### ステップ 5: エンドユーザーから位置情報の権限を取得する {#step-5-obtain-location-permissions-from-the-end-user}

Android M以降のバージョンでは、位置情報を収集したりジオフェンスを登録したりする前に、エンドユーザーに位置情報の権限を求める必要があります。

ユーザーがアプリに位置情報の権限を付与したときにBrazeに通知するために、以下の呼び出しを追加します。

{% tabs %}
{% tab JAVA %}

`````````java
Braze.getInstance(context).requestLocationInitialization();
```

{% endtab %}
{% tab KOTLIN %}

`````````kotlin
Braze.getInstance(context).requestLocationInitialization()
```

{% endtab %}
{% endtabs %}

これにより、SDKはBrazeサーバーにジオフェンスを要求し、ジオフェンスのトラッキングを初期化します。

実装例については、サンプルアプリケーションの[`RuntimePermissionUtils.java`](https://github.com/braze-inc/braze-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/util/RuntimePermissionUtils.kt)を参照してください。

{% tabs %}
{% tab JAVA %}

`````````java
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

`````````kotlin
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

上記のサンプルコードは、以下のように使用します。

{% tabs %}
{% tab JAVA %}

`````````java
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

`````````kotlin
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

### ステップ 6: ジオフェンスの更新を手動でリクエストする（オプション） {#step-6-manually-request-geofence-updates-optional}

デフォルトでは、Brazeは自動的にデバイスの位置情報を取得し、その取得した位置情報に基づいてジオフェンスを要求します。しかし、代わりに近接するBrazeジオフェンスを取得するために使用されるGPS座標を手動で指定することもできます。手動でBrazeジオフェンスをリクエストするには、自動Brazeジオフェンスリクエストを無効にし、リクエスト用にGPS座標を指定する必要があります。

#### ステップ 6.1: 自動ジオフェンスリクエストを無効にする {#step-61-disable-automatic-geofence-requests}

自動Brazeジオフェンスリクエストは、`com_braze_automatic_geofence_requests_enabled`を`false`に設定することで、`braze.xml`ファイルで無効にすることができます。

`````````xml
<bool name="com_braze_automatic_geofence_requests_enabled">false</bool>
```

これはさらに、ランタイム時に以下の方法で行うこともできます。

{% tabs %}
{% tab JAVA %}

`````````java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
    .setAutomaticGeofenceRequestsEnabled(false);
Braze.configure(getApplicationContext(), brazeConfigBuilder.build());
```

{% endtab %}
{% tab KOTLIN %}

`````````kotlin
val brazeConfigBuilder = BrazeConfig.Builder()
    .setAutomaticGeofenceRequestsEnabled(false)
Braze.configure(applicationContext, brazeConfigBuilder.build())
```

{% endtab %}
{% endtabs %}

#### ステップ 6.2: GPS座標でBrazeジオフェンスを手動でリクエストする {#step-62-manually-request-braze-geofence-with-gps-coordinate}

Brazeジオフェンスは、[`requestGeofences()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-geofences.html)メソッドを使用して手動でリクエストします。

{% tabs %}
{% tab JAVA %}

`````````java
Braze.getInstance(getApplicationContext()).requestGeofences(latitude, longitude);
```

{% endtab %}
{% tab KOTLIN %}

`````````kotlin
Braze.getInstance(applicationContext).requestGeofences(33.078947, -116.601356)
```

{% endtab %}
{% endtabs %}

{% alert important %}
ジオフェンスは、SDKにより自動的に、またはこのメソッドにより手動で、セッションごとに一度だけリクエストできます。
{% endalert %}