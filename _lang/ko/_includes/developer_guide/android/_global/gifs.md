## GIF 정보 {#about-gifs}

Braze는 커스텀 이미지 라이브러리를 사용하여 애니메이션 GIF를 표시하는 기능을 제공합니다. 다음 예시에서는 [Glide](https://bumptech.github.io/glide/)를 사용하지만, GIF를 지원하는 모든 이미지 라이브러리가 호환됩니다.

## 커스텀 이미지 라이브러리 통합 {#integrating-a-custom-image-library}

### 1단계: 이미지 로더 델리게이트 생성 {#step-1-creating-the-image-loader-delegate}

이미지 로더 델리게이트는 다음 메서드를 구현해야 합니다:

* [`getInAppMessageBitmapFromUrl()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/get-in-app-message-bitmap-from-url.html)
* [`getPushBitmapFromUrl()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/get-push-bitmap-from-url.html)
* [`renderUrlIntoCardView()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/render-url-into-card-view.html)
* [`renderUrlIntoInAppMessageView()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/render-url-into-in-app-message-view.html)
* [`setOffline()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/set-offline.html)

다음 통합 예제는 Braze Android SDK에 포함된 [Glide 통합 샘플 앱](https://github.com/braze-inc/braze-android-sdk/tree/master/samples/glide-image-integration)에서 가져온 것입니다.

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

### Android SDK 36.0.0 이상에서 이미지 로딩 수정 {#fixing-image-loading-for-android-sdk-3600-and-later}

Android SDK 36.0.0 이상에서는 `displayInAppMessage()`가 `suspend` 함수입니다. 이는 `renderUrlIntoInAppMessageView()`가 메인 스레드 대신 백그라운드 스레드에서 실행된다는 의미입니다.

커스텀 이미지 로더가 `renderUrlIntoInAppMessageView()`에서 `Glide.into(imageView)`를 호출하면 "You must call this method on the main thread."라는 오류로 앱이 실패할 수 있습니다.

이를 방지하려면 다음과 같이 합니다:

1. 백그라운드 스레드에서 `submit().get()`으로 이미지를 로드합니다.
2. `imageView.post { ... }`로 UI 업데이트를 메인 스레드에 게시합니다.
3. 로드된 결과가 GIF drawable인 경우, 뷰에 설정한 후 애니메이션을 시작합니다.

이렇게 하면 이미지 로딩과 UI 렌더링이 분리되어 커스텀 이미지 로더가 Android SDK 36.0.0 이상과 호환됩니다.

이 가이드는 Android 커스텀 이미지 로더에 적용됩니다. 웹 인앱 메시지는 GIF를 기본적으로 지원합니다.

다음 Kotlin 샘플은 이 패턴을 보여주기 위해 입력 안내 값을 사용합니다:

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

### 2단계: 이미지 로더 델리게이트 설정 {#step-2-setting-the-image-loader-delegate}

Braze SDK는 [`IBrazeImageLoader`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/index.html)로 설정된 커스텀 이미지 로더를 사용합니다. 커스텀 Application 서브클래스에서 커스텀 이미지 로더를 설정하는 것을 권장합니다:

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

### Glide 이미지 로드 문제 해결 {#troubleshooting-glide-image-loads}

커스텀 [`IBrazeImageLoader`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/index.html)를 설정한 후(예: Glide 사용 시) 이미지가 로드되지 않으면, 글로벌 OkHttp 인터셉터가 모든 요청에 인증 헤더를 추가하고 있는지 확인하세요.

이 페이지의 Glide 샘플은 Content Cards, 인앱 메시지, 푸시에 동일한 로드 경로를 사용합니다. Braze에서 호스팅하는 이미지는 CDN URL이며 REST API 인증을 사용하지 않습니다. 인터셉터를 자체 API 호스트로 범위를 제한하거나, Braze 이미지 호스트를 제외하세요. Glide 통합 후 Content Cards 이미지가 실패하는 것은 이 인터셉터 패턴의 일반적인 증상입니다.

## Jetpack Compose를 사용한 커스텀 이미지 로드 {#custom-image-loading-with-jetpack-compose}

Jetpack Compose에서 이미지 로드를 재정의하려면 [`imageComposable`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#-808910455%2FProperties%2F-1725759721)에 값을 전달하면 됩니다. 이 함수는 `Card`를 받아 이미지와 필요한 수정자를 렌더링합니다. 또는 `ContentCardsList`의 `customCardComposer`를 사용하여 전체 카드를 렌더링할 수도 있습니다.

다음 예제에서는 `imageComposable` 함수에 나열된 카드에 대해 Glide의 Compose 라이브러리를 사용합니다:

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
