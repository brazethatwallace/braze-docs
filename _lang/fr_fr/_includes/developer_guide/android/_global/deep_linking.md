{% multi_lang_include developer_guide/prerequisites/android.md %}

## Création d'un délégué universel {#creating-a-universal-delegate}

Le SDK Android permet de définir un objet délégué unique pour gérer de manière personnalisée tous les deep links ouverts par Braze via les Content Cards, les messages in-app et les notifications push.

Votre objet délégué doit implémenter l'interface [`IBrazeDeeplinkHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui/-braze-deeplink-handler/index.html) et être défini à l'aide de [`BrazeDeeplinkHandler.setBrazeDeeplinkHandler()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui/-braze-deeplink-handler/-companion/set-braze-deeplink-handler.html). Dans la plupart des cas, le délégué doit être défini dans le `Application.onCreate()` de votre application.

Voici un exemple de remplacement du comportement par défaut de [`UriAction`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.actions/-uri-action/index.html) avec des indicateurs d'intention personnalisés et un comportement personnalisé pour les URL YouTube :

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

## Création de deep links vers les paramètres de l'application {#deep-linking-to-app-settings}

Pour permettre aux deep links d'ouvrir directement les paramètres de votre application, vous aurez besoin d'un `BrazeDeeplinkHandler` personnalisé. Dans l'exemple suivant, la présence d'une paire clé-valeur personnalisée appelée `open_notification_page` fait en sorte que le deep link ouvre la page des paramètres de l'application :

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

## Personnalisation de l'activité WebView {#Custom_Webview_Activity}

Lorsque Braze ouvre des deep links vers des sites web à l'intérieur de l'application, ces liens sont gérés par [`BrazeWebViewActivity`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui/-braze-web-view-activity/index.html).

{% alert note %}
Pour les messages in-app HTML personnalisés, les liens configurés avec `target="_blank"` s'ouvrent dans le navigateur web par défaut de l'appareil et ne sont pas gérés par `BrazeWebViewActivity`.
{% endalert %}

Pour modifier ce comportement :

1. Créez une nouvelle activité qui gère l'URL cible depuis `Intent.getExtras()` avec la clé `com.braze.Constants.BRAZE_WEBVIEW_URL_EXTRA`. Pour un exemple, consultez [`BrazeWebViewActivity.kt`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/BrazeWebViewActivity.kt).
2. Ajoutez cette activité à `AndroidManifest.xml` et définissez `exported` sur `false`.
    ```xml
    <activity
        android:name=".MyCustomWebViewActivity"
        android:exported="false" />
    ```
3. Définissez votre activité personnalisée dans un [objet générateur](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-custom-web-view-activity-class.html) `BrazeConfig`. Construisez le générateur et transmettez-le à [`Braze.configure()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html) dans votre [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()).
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

## Résolution des problèmes {#troubleshooting}

Si les deep links provenant des notifications push ne fonctionnent pas sur Android, essayez les étapes suivantes :

1. **Testez le deep link en dehors de Braze.** Ouvrez l'URL du deep link depuis une autre application, comme un e-mail ou un navigateur. Si votre application ne s'ouvre pas, le deep link n'est peut-être pas correctement configuré dans votre `AndroidManifest.xml`. Pour plus d'informations, consultez la documentation Android [Create Deep Links](https://developer.android.com/training/app-links/deep-linking).
2. **Vérifiez que la gestion automatique des deep links est activée.** Assurez-vous que `com_braze_handle_push_deep_links_automatically` est défini sur `true` dans `braze.xml`, ou configurez cette option via la [configuration au moment de l'exécution]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#runtime-configuration). Sans ce paramètre, Braze n'ouvre pas automatiquement votre application ni la destination du deep link lorsqu'un utilisateur appuie sur une notification push.
3. **Vérifiez votre délégué de gestion des deep links.** Si vous avez défini un `IBrazeDeeplinkHandler` personnalisé, confirmez que votre implémentation de `gotoUri` gère bien l'URI et ne l'ignore pas.
4. **Testez sur différents canaux.** Si le même deep link fonctionne dans un message in-app mais pas depuis une notification push, le problème se situe probablement dans la gestion des deep links push, et non dans le deep link lui-même.

## Utilisation de Jetpack Compose {#using-jetpack-compose}

Pour gérer les deep links avec Jetpack Compose et NavHost :

1. Assurez-vous que l'activité gérant votre deep link est enregistrée dans le manifeste Android.
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
2. Dans NavHost, spécifiez les deep links que vous souhaitez gérer.
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
3. Selon l'architecture de votre application, vous devrez peut-être également gérer la nouvelle intention envoyée à votre activité actuelle.
    ```kotlin
    DisposableEffect(Unit) {
        val listener = Consumer<Intent> {
            navHostController.handleDeepLink(it)
        }
        addOnNewIntentListener(listener)
        onDispose { removeOnNewIntentListener(listener) }
    }
    ```