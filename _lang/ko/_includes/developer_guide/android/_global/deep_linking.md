{% multi_lang_include developer_guide/prerequisites/android.md %}

## 범용 델리게이트 만들기 {#creating-a-universal-delegate}

Android SDK는 Content Cards, 인앱 메시지, 푸시 알림에서 Braze가 여는 모든 딥링크를 커스텀 처리하도록 단일 델리게이트 오브젝트를 설정할 수 있는 기능을 제공합니다.

델리게이트 오브젝트는 [`IBrazeDeeplinkHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui/-braze-deeplink-handler/index.html) 인터페이스를 구현하고 [`BrazeDeeplinkHandler.setBrazeDeeplinkHandler()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui/-braze-deeplink-handler/-companion/set-braze-deeplink-handler.html)를 사용하여 설정해야 합니다. 대부분의 경우 델리게이트는 앱의 `Application.onCreate()`에서 설정해야 합니다.

다음은 YouTube URL에 대한 커스텀 동작 및 커스텀 인텐트 플래그로 기본 [`UriAction`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.actions/-uri-action/index.html) 동작을 재정의하는 예제입니다.

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

## 앱 설정으로 딥링킹 {#deep-linking-to-app-settings}

딥링크가 앱 설정을 직접 열 수 있도록 하려면 커스텀 `BrazeDeeplinkHandler`가 필요합니다. 다음 예제에서는 `open_notification_page`라는 커스텀 키-값 페어가 있으면 딥링크가 앱 설정 페이지를 엽니다.

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

## WebView 액티비티 커스터마이징 {#Custom_Webview_Activity}

Braze가 앱 내에서 웹사이트 딥링크를 열 때, 딥링크는 [`BrazeWebViewActivity`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui/-braze-web-view-activity/index.html)에 의해 처리됩니다.

{% alert note %}
커스텀 HTML 인앱 메시지의 경우, `target="_blank"`로 구성된 링크는 기기의 기본 웹 브라우저에서 열리며 `BrazeWebViewActivity`에 의해 처리되지 않습니다.
{% endalert %}

이를 변경하려면:

1. `com.braze.Constants.BRAZE_WEBVIEW_URL_EXTRA` 키를 사용하여 `Intent.getExtras()`에서 대상 URL을 처리하는 새 액티비티를 생성합니다. 예제는 [`BrazeWebViewActivity.kt`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/BrazeWebViewActivity.kt)를 참조하세요.
2. 해당 액티비티를 `AndroidManifest.xml`에 추가하고 `exported`를 `false`로 설정합니다.
    ```xml
    <activity
        android:name=".MyCustomWebViewActivity"
        android:exported="false" />
    ```
3. `BrazeConfig` [빌더 오브젝트](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-custom-web-view-activity-class.html)에서 커스텀 액티비티를 설정합니다. 빌더를 구축하고 [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate())에서 [`Braze.configure()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html)에 전달합니다.
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

## 문제 해결 {#troubleshooting}

푸시 알림의 딥링크가 Android에서 작동하지 않는 경우 다음 단계를 시도해 보세요.

1. **Braze 외부에서 딥링크를 테스트합니다.** 이메일이나 브라우저 등 다른 앱에서 딥링크 URL을 열어 보세요. 앱이 열리지 않으면 `AndroidManifest.xml`에서 딥링크가 올바르게 구성되지 않았을 수 있습니다. 자세한 내용은 Android의 [딥링크 만들기](https://developer.android.com/training/app-links/deep-linking) 설명서를 참조하세요.
2. **자동 딥링크 처리가 활성화되어 있는지 확인합니다.** `braze.xml`에서 `com_braze_handle_push_deep_links_automatically`가 `true`로 설정되어 있는지 확인하거나, [런타임 구성]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=android)을 통해 이 옵션을 설정하세요. 이 설정이 없으면 사용자가 푸시 알림을 탭할 때 Braze가 자동으로 앱을 열고 딥링크 대상으로 이동하지 않습니다.
3. **딥링크 핸들러 델리게이트를 확인합니다.** 커스텀 `IBrazeDeeplinkHandler`를 설정한 경우, `gotoUri` 구현이 URI를 올바르게 처리하고 누락시키지 않는지 확인하세요.
4. **채널 간 테스트를 수행합니다.** 동일한 딥링크가 인앱 메시지에서는 작동하지만 푸시에서는 작동하지 않는 경우, 문제는 딥링크 자체가 아니라 푸시 딥링크 처리에 있을 가능성이 높습니다.

## Jetpack Compose 사용하기 {#using-jetpack-compose}

NavHost와 함께 Jetpack Compose를 사용할 때 딥링크를 처리하려면:

1. 딥링크를 처리하는 액티비티가 Android Manifest에 등록되어 있는지 확인합니다.
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
2. NavHost에서 처리할 딥링크를 지정합니다.
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
3. 앱 아키텍처에 따라 현재 액티비티로 전송되는 새로운 인텐트도 처리해야 할 수 있습니다.
    ```kotlin
    DisposableEffect(Unit) {
        val listener = Consumer<Intent> {
            navHostController.handleDeepLink(it)
        }
        addOnNewIntentListener(listener)
        onDispose { removeOnNewIntentListener(listener) }
    }
    ```