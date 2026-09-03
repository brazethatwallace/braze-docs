## GIFについて {#about-gifs}

Brazeでは、カスタムイメージライブラリを使用してアニメーションGIFを表示する機能を提供しています。以下の例では[Glide](https://bumptech.github.io/glide/)を使用していますが、GIFをサポートする任意のイメージライブラリと互換性があります。

## カスタムイメージライブラリの統合 {#integrating-a-custom-image-library}

### ステップ 1: イメージローダーデリゲートの作成 {#step-1-creating-the-image-loader-delegate}

イメージローダーデリゲートは、以下のメソッドを実装する必要があります。

* [`getInAppMessageBitmapFromUrl()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/get-in-app-message-bitmap-from-url.html)
* [`getPushBitmapFromUrl()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/get-push-bitmap-from-url.html)
* [`renderUrlIntoCardView()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/render-url-into-card-view.html)
* [`renderUrlIntoInAppMessageView()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/render-url-into-in-app-message-view.html)
* [`setOffline()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/set-offline.html)

以下の統合例は、Braze Android SDKに含まれる [Glide統合サンプルアプリ](https://github.com/braze-inc/braze-android-sdk/tree/master/samples/glide-image-integration) から引用しています。

{% tabs %}
{% tab JAVA %}

```java
import com.braze.support.BrazeLogger;
import com.bumptech.glide.load.resource.gif.GifDrawable;
import android.graphics.drawable.Drawable;

public class GlideBrazeImageLoader implements IBrazeImageLoader {
  private static final String TAG = GlideBrazeImageLoader.class.getName();

  private RequestOptions mRequestOptions = new RequestOptions();

  @Override
  public void renderUrlIntoCardView(Context context, Card card, String imageUrl, ImageView imageView, BrazeViewBounds viewBounds) {
    renderUrlIntoView(context, imageUrl, imageView);
  }

  @Override
  public void renderUrlIntoInAppMessageView(Context context, IInAppMessage inAppMessage, String imageUrl, ImageView imageView, BrazeViewBounds viewBounds) {
    renderUrlIntoView(context, imageUrl, imageView);
  }

  @Override
  public Bitmap getPushBitmapFromUrl(Context context, Bundle extras, String imageUrl, BrazeViewBounds viewBounds) {
    return getBitmapFromUrl(context, imageUrl, viewBounds);
  }

  @Override
  public Bitmap getInAppMessageBitmapFromUrl(Context context, IInAppMessage inAppMessage, String imageUrl, BrazeViewBounds viewBounds) {
    return getBitmapFromUrl(context, imageUrl, viewBounds);
  }

  private void renderUrlIntoView(Context context, String imageUrl, ImageView imageView) {
    try {
      final Drawable drawable = Glide.with(context)
          .load(imageUrl)
          .apply(mRequestOptions)
          .submit()
          .get();

      imageView.post(() -> {
        imageView.setImageDrawable(drawable);
        if (drawable instanceof GifDrawable) {
          ((GifDrawable) drawable).start();
        }
      });
    } catch (Exception e) {
      BrazeLogger.e(TAG, "Failed to render URL into view: " + imageUrl, e);
    }
  }

  private Bitmap getBitmapFromUrl(Context context, String imageUrl, BrazeViewBounds viewBounds) {
    try {
      return Glide.with(context)
          .asBitmap()
          .apply(mRequestOptions)
          .load(imageUrl).submit().get();
    } catch (Exception e) {
      Log.e(TAG, "Failed to retrieve bitmap at url: " + imageUrl, e);
    }
    return null;
  }

  @Override
  public void setOffline(boolean isOffline) {
    // If the loader is offline, then we should only be retrieving from the cache
    mRequestOptions = mRequestOptions.onlyRetrieveFromCache(isOffline);
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
import com.braze.support.BrazeLogger
import com.bumptech.glide.load.resource.gif.GifDrawable

class GlideBrazeImageLoader : IBrazeImageLoader {
  companion object {
    private val TAG = GlideBrazeImageLoader::class.qualifiedName
  }

  private var mRequestOptions = RequestOptions()

  override fun renderUrlIntoCardView(context: Context, card: Card, imageUrl: String, imageView: ImageView, viewBounds: BrazeViewBounds) {
    renderUrlIntoView(context, imageUrl, imageView)
  }

  override fun renderUrlIntoInAppMessageView(context: Context, inAppMessage: IInAppMessage, imageUrl: String, imageView: ImageView, viewBounds: BrazeViewBounds) {
    renderUrlIntoView(context, imageUrl, imageView)
  }

  override fun getPushBitmapFromUrl(context: Context, extras: Bundle, imageUrl: String, viewBounds: BrazeViewBounds): Bitmap? {
    return getBitmapFromUrl(context, imageUrl, viewBounds)
  }

  override fun getInAppMessageBitmapFromUrl(context: Context, inAppMessage: IInAppMessage, imageUrl: String, viewBounds: BrazeViewBounds): Bitmap? {
    return getBitmapFromUrl(context, imageUrl, viewBounds)
  }

  private fun renderUrlIntoView(context: Context, imageUrl: String, imageView: ImageView) {
    try {
      val drawable = Glide.with(context)
          .load(imageUrl)
          .apply(mRequestOptions)
          .submit()
          .get()

      imageView.post {
        imageView.setImageDrawable(drawable)
        if (drawable is GifDrawable) {
          drawable.start()
        }
      }
    } catch (e: Exception) {
      BrazeLogger.e(TAG, "Failed to render URL into view: $imageUrl", e)
    }
  }

  private fun getBitmapFromUrl(context: Context, imageUrl: String, viewBounds: BrazeViewBounds): Bitmap? {
    try {
      return Glide.with(context)
          .asBitmap()
          .apply(mRequestOptions)
          .load(imageUrl).submit().get()
    } catch (e: Exception) {
      Log.e(TAG, "Failed to retrieve bitmap at url: $imageUrl", e)
    }

    return null
  }

  override fun setOffline(isOffline: Boolean) {
    // If the loader is offline, then we should only be retrieving from the cache
    mRequestOptions = mRequestOptions.onlyRetrieveFromCache(isOffline)
  }
}
```

{% endtab %}
{% endtabs %}

### Android SDK 36.0.0以降での画像読み込みの修正 {#fixing-image-loading-for-android-sdk-3600-and-later}

Android SDK 36.0.0以降では、`displayInAppMessage()` は `suspend` 関数になっています。そのため、`renderUrlIntoInAppMessageView()` はメインスレッドではなくバックグラウンドスレッドで実行されます。

カスタムイメージローダーが `renderUrlIntoInAppMessageView()` 内で `Glide.into(imageView)` を呼び出している場合、「You must call this method on the main thread.」というエラーでアプリが失敗する可能性があります。

これを回避するには、次のようにします。

1. バックグラウンドスレッドで `submit().get()` を使用して画像を読み込みます。
2. `imageView.post { ... }` を使用して UI の更新をメインスレッドにポストします。
3. 読み込み結果が GIF ドローアブルの場合、ビューに設定した後にアニメーションを開始します。

これにより、画像の読み込みと UI のレンダリングが分離され、カスタムイメージローダーが Android SDK 36.0.0以降と互換性を保つことができます。

このガイダンスは Android のカスタムイメージローダーに適用されます。Web のアプリ内メッセージはGIFをデフォルトでサポートしています。

以下の Kotlin サンプルは、このパターンを示すためにプレースホルダー値を使用しています。

```kotlin
private const val TAG = "SampleGlideLoader"
private const val glideBrazeImageLoaderTag = "sample-loader"

private fun renderUrlIntoView(
    context: Context,
    imageUrl: String,
    imageView: ImageView
) {
    try {
        val drawable: Drawable = Glide.with(context)
            .load(imageUrl)
            .apply(mRequestOptions)
            .submit()
            .get()

        imageView.post {
            imageView.setImageDrawable(drawable)
            if (drawable is GifDrawable) {
                drawable.start()
            }
        }
    } catch (e: Exception) {
        Log.e(TAG, "$glideBrazeImageLoaderTag renderUrlIntoView failed: url=$imageUrl", e)
    }
}
```

### ステップ 2: イメージローダーデリゲートの設定 {#step-2-setting-the-image-loader-delegate}

Braze SDKは、[`IBrazeImageLoader`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/index.html) で設定されたカスタムイメージローダーを使用します。カスタムイメージローダーは、カスタムアプリケーションサブクラスで設定することをお勧めします。

{% tabs %}
{% tab JAVA %}

```java
public class GlideIntegrationApplication extends Application {
  @Override
  public void onCreate() {
    super.onCreate();
    Braze.getInstance(context).setImageLoader(new GlideBrazeImageLoader());
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class GlideIntegrationApplication : Application() {
  override fun onCreate() {
    super.onCreate()
    Braze.getInstance(context).imageLoader = GlideBrazeImageLoader()
  }
}
```

{% endtab %}
{% endtabs %}

### Glide 画像読み込みのトラブルシューティング {#troubleshooting-glide-image-loads}

カスタム [`IBrazeImageLoader`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/index.html) を設定した後（たとえば Glide を使用して）画像が読み込まれなくなった場合、グローバル OkHttp インターセプターがすべてのリクエストに認証ヘッダーを追加していないか確認してください。

このページの Glide サンプルは、Content Cards、アプリ内メッセージ、プッシュに対して同じ読み込みパスを使用しています。Braze がホストする画像は CDN URL であり、REST API認証を使用しません。インターセプターのスコープを自社の API ホストに限定するか、Braze の画像ホストを除外してください。Glide 統合後に Content Cardsの画像が失敗する場合は、このインターセプターパターンの一般的な症状です。

## Jetpack Composeによるカスタム画像読み込み {#custom-image-loading-with-jetpack-compose}

Jetpack Composeで画像の読み込みをオーバーライドするには、[`imageComposable`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#-808910455%2FProperties%2F-1725759721) に値を渡します。この関数は`Card`を受け取り、画像と必要なモディファイアをレンダリングします。あるいは、`ContentCardsList`の`customCardComposer`を使用してカード全体をレンダリングすることもできます。

以下の例では、`imageComposable`関数にリストされたカードに対して、GlideのComposeライブラリを使用しています。

```kotlin
ContentCardsList(
    cardStyle = ContentCardStyling(
        imageComposable = { card ->
            when (card.cardType) {
                CardType.CAPTIONED_IMAGE -> {
                    val captionedImageCard = card as CaptionedImageCard
                    GlideImage(
                        modifier = Modifier
                            .fillMaxWidth()
                            .wrapContentHeight()
                            .run {
                                if (captionedImageCard.aspectRatio > 0) {
                                    aspectRatio(captionedImageCard.aspectRatio)
                                } else {
                                    this
                                }
                            },
                        contentScale = ContentScale.Crop,
                        model = captionedImageCard.url,
                        loading = placeholder(R.drawable.pushpin),
                        contentDescription = ""
                    )
                }
                CardType.IMAGE -> {
                    val imageOnlyCard = card as ImageOnlyCard
                    GlideImage(
                        modifier = Modifier
                            .fillMaxWidth()
                            .run {
                                if (imageOnlyCard.aspectRatio > 0) {
                                    aspectRatio(imageOnlyCard.aspectRatio)
                                } else {
                                    this
                                }
                            },
                        contentScale = ContentScale.Crop,
                        model = imageOnlyCard.url,
                        loading = placeholder(R.drawable.pushpin),
                        contentDescription = ""
                    )
                }
                CardType.SHORT_NEWS -> {
                    val shortNews = card as ShortNewsCard
                    GlideImage(
                        modifier = Modifier
                            .width(100.dp)
                            .height(100.dp),
                        model = shortNews.url,
                        loading = placeholder(R.drawable.pushpin),
                        contentDescription = ""
                    )
                }
                else -> Unit
            }
        }
    )
)
```
