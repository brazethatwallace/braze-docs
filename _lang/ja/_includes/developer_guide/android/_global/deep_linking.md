{% multi_lang_include developer_guide/prerequisites/android.md %}

## ユニバーサルデリゲートの作成 {#creating-a-universal-delegate}

Android SDKは、Content Cards、アプリ内メッセージ、プッシュ通知にわたってBrazeによって開かれたすべてのディープリンクをカスタム処理するための単一のデリゲートオブジェクトを設定する機能を提供しています。

デリゲートオブジェクトは[`IBrazeDeeplinkHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui/-braze-deeplink-handler/index.html)インターフェイスを実装し、[`BrazeDeeplinkHandler.setBrazeDeeplinkHandler()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui/-braze-deeplink-handler/-companion/set-braze-deeplink-handler.html)を使用して設定する必要があります。ほとんどの場合、デリゲートはアプリの`Application.onCreate()`で設定します。

以下は、カスタムインテントフラグとYouTube URLのカスタム動作でデフォルトの[`UriAction`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.actions/-uri-action/index.html)動作をオーバーライドする例です。

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

## アプリ設定へのディープリンク {#deep-linking-to-app-settings}

ディープリンクでアプリの設定を直接開けるようにするには、カスタムの`BrazeDeeplinkHandler`が必要です。以下の例では、`open_notification_page`というカスタムのキーと値のペアが存在する場合、ディープリンクがアプリの設定ページを開きます。

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

## WebViewアクティビティのカスタマイズ {#Custom_Webview_Activity}

Brazeがアプリ内でWebサイトのディープリンクを開く場合、そのディープリンクは[`BrazeWebViewActivity`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui/-braze-web-view-activity/index.html)によって処理されます。

{% alert note %}
カスタムHTMLのアプリ内メッセージでは、`target="_blank"`が設定されたリンクはデバイスのデフォルトWebブラウザで開かれ、`BrazeWebViewActivity`では処理されません。
{% endalert %}

これを変更するには、以下の手順を行います。

1. キー`com.braze.Constants.BRAZE_WEBVIEW_URL_EXTRA`で`Intent.getExtras()`からターゲットURLを処理する新しいアクティビティを作成します。例については、[`BrazeWebViewActivity.kt`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/BrazeWebViewActivity.kt)を参照してください。
2. そのアクティビティを`AndroidManifest.xml`に追加し、`exported`を`false`に設定します。
    ```xml
    <activity
        android:name=".MyCustomWebViewActivity"
        android:exported="false" />
    ```
3. カスタムアクティビティを`BrazeConfig`[ビルダーオブジェクト](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-custom-web-view-activity-class.html)に設定します。ビルダーをビルドし、[`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate())内で[`Braze.configure()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html)に渡します。
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

## トラブルシューティング {#troubleshooting}

プッシュ通知からのディープリンクがAndroidで動作しない場合は、以下のステップを試してください。

1. **Braze以外でディープリンクをテストします。** メールやブラウザなど、別のアプリからディープリンクURLを開いてみてください。アプリが開かない場合、`AndroidManifest.xml`でディープリンクが正しく設定されていない可能性があります。詳細については、Androidの[Create Deep Links](https://developer.android.com/training/app-links/deep-linking)ドキュメントを参照してください。
2. **自動ディープリンク処理が有効になっていることを確認します。** `braze.xml`で`com_braze_handle_push_deep_links_automatically`が`true`に設定されているか、[ランタイム設定]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#runtime-configuration)でこのオプションを設定しているか確認してください。この設定がないと、プッシュ通知をタップしたときにBrazeがアプリとディープリンクの送信先を自動的に開きません。
3. **ディープリンクハンドラーデリゲートを確認します。** カスタムの`IBrazeDeeplinkHandler`を設定している場合、`gotoUri`の実装がURIを正しく処理し、ドロップしていないことを確認してください。
4. **チャネル間でテストします。** 同じディープリンクがアプリ内メッセージでは動作するがプッシュからは動作しない場合、問題はディープリンク自体ではなく、プッシュのディープリンク処理にある可能性が高いです。

## Jetpack Composeの使用 {#using-jetpack-compose}

Jetpack ComposeとNavHostを使用する際にディープリンクを処理するには、以下の手順を行います。

1. ディープリンクを処理するアクティビティがAndroidマニフェストに登録されていることを確認します。
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
2. NavHostで、処理するディープリンクを指定します。
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
3. アプリのアーキテクチャによっては、現在のアクティビティに送信される新しいインテントも処理する必要がある場合があります。
    ```kotlin
    DisposableEffect(Unit) {
        val listener = Consumer<Intent> {
            navHostController.handleDeepLink(it)
        }
        addOnNewIntentListener(listener)
        onDispose { removeOnNewIntentListener(listener) }
    }
    ```