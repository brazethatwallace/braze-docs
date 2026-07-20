{% multi_lang_include developer_guide/prerequisites/android.md %}

## Criando um delegado universal {#creating-a-universal-delegate}

O SDK do Android oferece a capacidade de definir um único objeto delegado para tratar de forma personalizada todos os deep links abertos pela Braze nos Content Cards, mensagens no app e notificações por push.

Seu objeto delegado deve implementar a interface [`IBrazeDeeplinkHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui/-braze-deeplink-handler/index.html) e ser definido usando [`BrazeDeeplinkHandler.setBrazeDeeplinkHandler()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui/-braze-deeplink-handler/-companion/set-braze-deeplink-handler.html). Na maioria dos casos, o delegado deve ser definido no `Application.onCreate()` do seu app.

Veja a seguir um exemplo de substituição do comportamento padrão de [`UriAction`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.actions/-uri-action/index.html) com flags de intent personalizadas e comportamento personalizado para URLs do YouTube:

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

## Deep linking para as configurações do app {#deep-linking-to-app-settings}

Para permitir que deep links abram diretamente as configurações do seu app, você precisará de um `BrazeDeeplinkHandler` personalizado. No exemplo a seguir, a presença de um par de chave-valor personalizado chamado `open_notification_page` fará com que o deep link abra a página de configurações do app:

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

## Personalizando a atividade WebView {#Custom_Webview_Activity}

Quando a Braze abre deep links de sites dentro do app, eles são tratados pela [`BrazeWebViewActivity`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui/-braze-web-view-activity/index.html).

{% alert note %}
Para mensagens no app personalizadas em HTML, links configurados com `target="_blank"` abrem no navegador web padrão do dispositivo e não são tratados pela `BrazeWebViewActivity`.
{% endalert %}

Para mudar isso:

1. Crie uma nova Activity que trate a URL de destino a partir de `Intent.getExtras()` com a chave `com.braze.Constants.BRAZE_WEBVIEW_URL_EXTRA`. Para ver um exemplo, consulte [`BrazeWebViewActivity.kt`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/BrazeWebViewActivity.kt).
2. Adicione essa Activity ao `AndroidManifest.xml` e defina `exported` como `false`.
    ```xml
    <activity
        android:name=".MyCustomWebViewActivity"
        android:exported="false" />
    ```
3. Defina sua Activity personalizada em um [objeto builder](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-custom-web-view-activity-class.html) de `BrazeConfig`. Construa o builder e passe-o para [`Braze.configure()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html) no seu [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()).
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

## Solução de problemas {#troubleshooting}

Se os deep links de notificações por push não estiverem funcionando no Android, tente os seguintes passos:

1. **Teste o deep link fora da Braze.** Abra a URL do deep link a partir de outro app, como e-mail ou navegador. Se ele não abrir seu app, o deep link pode não estar configurado corretamente no seu `AndroidManifest.xml`. Para saber mais, consulte a documentação do Android sobre [Criar deep links](https://developer.android.com/training/app-links/deep-linking).
2. **Verifique se o tratamento automático de deep links está ativado.** Confirme que `com_braze_handle_push_deep_links_automatically` está definido como `true` no `braze.xml`, ou defina essa opção por meio da [configuração em tempo de execução]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#runtime-configuration). Sem essa configuração, a Braze não abre automaticamente seu app e o destino do deep link quando alguém toca em uma notificação por push.
3. **Verifique o delegado do seu deep link handler.** Se você definiu um `IBrazeDeeplinkHandler` personalizado, confirme que sua implementação de `gotoUri` trata a URI e não a descarta.
4. **Teste em diferentes canais.** Se o mesmo deep link funciona em uma mensagem no app, mas não a partir de push, o problema provavelmente está no tratamento do deep link de push, e não no deep link em si.

## Usando Jetpack Compose {#using-jetpack-compose}

Para tratar deep links ao usar Jetpack Compose com NavHost:

1. Certifique-se de que a Activity que trata seu deep link está registrada no Android Manifest.
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
2. No NavHost, especifique quais deep links você deseja que ele trate.
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
3. Dependendo da arquitetura do seu app, você também pode precisar tratar o novo intent que é enviado para sua Activity atual.
    ```kotlin
    DisposableEffect(Unit) {
        val listener = Consumer<Intent> {
            navHostController.handleDeepLink(it)
        }
        addOnNewIntentListener(listener)
        onDispose { removeOnNewIntentListener(listener) }
    }
    ```