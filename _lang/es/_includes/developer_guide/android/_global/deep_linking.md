{% multi_lang_include developer_guide/prerequisites/android.md %}

## Creación de un delegado universal {#creating-a-universal-delegate}

El SDK de Android ofrece la posibilidad de establecer un único objeto delegado para gestionar de forma personalizada todos los vínculos profundos abiertos por Braze a través de Content Cards, mensajes dentro de la aplicación y notificaciones push.

Tu objeto delegado debe implementar la interfaz [`IBrazeDeeplinkHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui/-braze-deeplink-handler/index.html) y configurarse mediante [`BrazeDeeplinkHandler.setBrazeDeeplinkHandler()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui/-braze-deeplink-handler/-companion/set-braze-deeplink-handler.html). En la mayoría de los casos, el delegado debe establecerse en el `Application.onCreate()` de tu aplicación.

A continuación se muestra un ejemplo de cómo anular el comportamiento predeterminado de [`UriAction`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.actions/-uri-action/index.html) con indicadores de intención personalizados y un comportamiento personalizado para las URL de YouTube:

{% tabs %}
{% tab JAVA %}

```java
public class CustomDeeplinkHandler implements IBrazeDeeplinkHandler {
  private static final String TAG = BrazeLogger.getBrazeLogTag(CustomDeeplinkHandler.class);

  @Override
  public void gotoUri(Context context, UriAction uriAction) {
    String uri = uriAction.getUri().toString();
    // Open YouTube URLs in the YouTube app and not our app
    if (!StringUtils.isNullOrBlank(uri) && uri.contains("youtube.com")) {
      uriAction.setUseWebView(false);
    }

    CustomUriAction customUriAction = new CustomUriAction(uriAction);
    customUriAction.execute(context);
  }

  public static class CustomUriAction extends UriAction {

    public CustomUriAction(@NonNull UriAction uriAction) {
      super(uriAction);
    }

    @Override
    protected void openUriWithActionView(Context context, Uri uri, Bundle extras) {
      Intent intent = getActionViewIntent(context, uri, extras);
      intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_SINGLE_TOP);
      if (intent.resolveActivity(context.getPackageManager()) != null) {
        context.startActivity(intent);
      } else {
        BrazeLogger.w(TAG, "Could not find appropriate activity to open for deep link " + uri + ".");
      }
    }
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class CustomDeeplinkHandler : IBrazeDeeplinkHandler {

  override fun gotoUri(context: Context, uriAction: UriAction) {
    val uri = uriAction.uri.toString()
    // Open YouTube URLs in the YouTube app and not our app
    if (!StringUtils.isNullOrBlank(uri) && uri.contains("youtube.com")) {
      uriAction.useWebView = false
    }

    val customUriAction = CustomUriAction(uriAction)
    customUriAction.execute(context)
  }

  class CustomUriAction(uriAction: UriAction) : UriAction(uriAction) {

    override fun openUriWithActionView(context: Context, uri: Uri, extras: Bundle) {
      val intent = getActionViewIntent(context, uri, extras)
      intent.flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TOP or Intent.FLAG_ACTIVITY_SINGLE_TOP
      if (intent.resolveActivity(context.packageManager) != null) {
        context.startActivity(intent)
      } else {
        BrazeLogger.w(TAG, "Could not find appropriate activity to open for deep link $uri.")
      }
    }
  }

  companion object {
    private val TAG = BrazeLogger.getBrazeLogTag(CustomDeeplinkHandler::class.java)
  }
}
```

{% endtab %}
{% endtabs %}

## Vinculación en profundidad a la configuración de la aplicación {#deep-linking-to-app-settings}

Para permitir que los vínculos profundos abran directamente la configuración de tu aplicación, necesitarás un `BrazeDeeplinkHandler` personalizado. En el siguiente ejemplo, la presencia de un par clave-valor personalizado llamado `open_notification_page` hará que el vínculo profundo abra la página de configuración de la aplicación:

{% tabs %}
{% tab JAVA %}

```java
BrazeDeeplinkHandler.setBrazeDeeplinkHandler(new IBrazeDeeplinkHandler() {
  @Override
  public void gotoUri(Context context, UriAction uriAction) {
    final Bundle extras = uriAction.getExtras();
    if (extras.containsKey("open_notification_page")) {
      Intent intent = new Intent();
      intent.setAction("android.settings.APP_NOTIFICATION_SETTINGS");
      intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);

      //for Android 5-7
      intent.putExtra("app_package", context.getPackageName());
      intent.putExtra("app_uid", context.getApplicationInfo().uid);

      // for Android 8 and later
      intent.putExtra("android.provider.extra.APP_PACKAGE", context.getPackageName());
      context.startActivity(intent);
    }
  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
BrazeDeeplinkHandler.setBrazeDeeplinkHandler(object : IBrazeDeeplinkHandler {
  override fun gotoUri(context: Context, uriAction: UriAction) {
    val extras = uriAction.extras
    if (extras.containsKey("open_notification_page")) {
      val intent = Intent()
      intent.action = "android.settings.APP_NOTIFICATION_SETTINGS"
      intent.flags = Intent.FLAG_ACTIVITY_NEW_TASK

      //for Android 5-7
      intent.putExtra("app_package", context.packageName)
      intent.putExtra("app_uid", context.applicationInfo.uid)

      // for Android 8 and later
      intent.putExtra("android.provider.extra.APP_PACKAGE", context.packageName)
      context.startActivity(intent)
    }
  }
})
```

{% endtab %}
{% endtabs %}

## Personalización de la actividad WebView {#Custom_Webview_Activity}

Cuando Braze abre vínculos profundos de sitios web dentro de la aplicación, estos son gestionados por [`BrazeWebViewActivity`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui/-braze-web-view-activity/index.html).

{% alert note %}
En el caso de los mensajes HTML personalizados dentro de la aplicación, los enlaces configurados con `target="_blank"` se abren en el navegador web predeterminado del dispositivo y no son gestionados por `BrazeWebViewActivity`.
{% endalert %}

Para cambiar esto:

1. Crea una nueva Activity que gestione la URL de destino de `Intent.getExtras()` con la clave `com.braze.Constants.BRAZE_WEBVIEW_URL_EXTRA`. Para ver un ejemplo, consulta [`BrazeWebViewActivity.kt`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/BrazeWebViewActivity.kt).
2. Añade esa actividad a `AndroidManifest.xml` y establece `exported` en `false`.
    ```xml
    <activity
        android:name=".MyCustomWebViewActivity"
        android:exported="false" />
    ```
3. Configura tu Activity personalizada en un [objeto constructor](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-custom-web-view-activity-class.html) de `BrazeConfig`. Construye el builder y pásalo a [`Braze.configure()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html) en tu [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()).
{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
    .setCustomWebViewActivityClass(MyCustomWebViewActivity::class)
    ...
    .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setCustomWebViewActivityClass(MyCustomWebViewActivity::class.java)
    ...
    .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

## Solución de problemas {#troubleshooting}

Si los vínculos profundos de las notificaciones push no funcionan en Android, prueba los siguientes pasos:

1. **Prueba el vínculo profundo fuera de Braze.** Abre la URL del vínculo profundo desde otra aplicación, como el correo electrónico o un navegador. Si no abre tu aplicación, es posible que el vínculo profundo no esté configurado correctamente en tu `AndroidManifest.xml`. Para más información, consulta la documentación de Android sobre [Crear vínculos profundos](https://developer.android.com/training/app-links/deep-linking).
2. **Comprueba que la gestión automática de vínculos profundos esté habilitada.** Verifica que `com_braze_handle_push_deep_links_automatically` esté establecido en `true` en `braze.xml`, o configura esta opción mediante la [configuración en tiempo de ejecución]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=android). Sin esta configuración, Braze no abre automáticamente tu aplicación ni el destino del vínculo profundo cuando alguien toca una notificación push.
3. **Verifica tu delegado de gestión de vínculos profundos.** Si configuraste un `IBrazeDeeplinkHandler` personalizado, confirma que tu implementación de `gotoUri` gestiona la URI y no la descarta.
4. **Prueba en distintos canales.** Si el mismo vínculo profundo funciona en un mensaje dentro de la aplicación pero no desde push, es probable que el problema esté en la gestión de vínculos profundos de push, no en el vínculo profundo en sí.

## Uso de Jetpack Compose {#using-jetpack-compose}

Para gestionar vínculos profundos cuando usas Jetpack Compose con NavHost:

1. Asegúrate de que la actividad que gestiona tu vínculo profundo esté registrada en el manifiesto de Android.
    ```xml
    <activity
      ...
      <intent-filter>
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.BROWSABLE" />
        <category android:name="android.intent.category.DEFAULT" />
        <data
            android:host="articles"
            android:scheme="myapp" />
      </intent-filter>
    </activity>
    ```
2. En NavHost, especifica qué vínculos profundos quieres que gestione.
    ```kotlin
    composableWithCompositionLocal(
        route = "YOUR_ROUTE_HERE",
        deepLinks = listOf(navDeepLink {
            uriPattern = "myapp://articles/{${MainDestinations.ARTICLE_ID_KEY}}"
        }),
        arguments = listOf(
            navArgument(MainDestinations.ARTICLE_ID_KEY) {
                type = NavType.LongType
            }
        ),
    ) { backStackEntry ->
        val arguments = requireNotNull(backStackEntry.arguments)
        val articleId = arguments.getLong(MainDestinations.ARTICLE_ID_KEY)
        ArticleDetail(
            articleId
        )
    }
    ```
3. Dependiendo de la arquitectura de tu aplicación, es posible que también necesites gestionar la nueva intención que se envía a tu actividad actual.
    ```kotlin
    DisposableEffect(Unit) {
        val listener = Consumer<Intent> {
            navHostController.handleDeepLink(it)
        }
        addOnNewIntentListener(listener)
        onDispose { removeOnNewIntentListener(listener) }
    }
    ```