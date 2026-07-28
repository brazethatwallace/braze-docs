## Über GIFs {#about-gifs}

Braze bietet die Möglichkeit, eine eigene Bildbibliothek zu verwenden, um animierte GIFs anzuzeigen. Obwohl das folgende Beispiel [Glide](https://bumptech.github.io/glide/) verwendet, ist jede Bildbibliothek kompatibel, die GIFs unterstützt.

## Eigene Bildbibliothek integrieren {#integrating-a-custom-image-library}

### Schritt 1: Erstellen des Image-Loader-Delegaten {#step-1-creating-the-image-loader-delegate}

Der Image-Loader-Delegat muss die folgenden Methoden implementieren:

* [`getInAppMessageBitmapFromUrl()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/get-in-app-message-bitmap-from-url.html)
* [`getPushBitmapFromUrl()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/get-push-bitmap-from-url.html)
* [`renderUrlIntoCardView()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/render-url-into-card-view.html)
* [`renderUrlIntoInAppMessageView()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/render-url-into-in-app-message-view.html)
* [`setOffline()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/set-offline.html)

Das folgende Integrationsbeispiel stammt aus der [Glide-Integrationsbeispiel-App](https://github.com/braze-inc/braze-android-sdk/tree/master/samples/glide-image-integration), die im Braze Android SDK enthalten ist.

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

### Behebung des Bildladens für Android SDK 36.0.0 und höher {#fixing-image-loading-for-android-sdk-3600-and-later}

Ab Android SDK 36.0.0 ist `displayInAppMessage()` eine `suspend`-Funktion. Das bedeutet, dass `renderUrlIntoInAppMessageView()` auf einem Hintergrund-Thread statt auf dem Haupt-Thread ausgeführt wird.

Wenn Ihr eigener Image-Loader `Glide.into(imageView)` in `renderUrlIntoInAppMessageView()` aufruft, kann Ihre App mit der Meldung „You must call this method on the main thread“ fehlschlagen.

Um dies zu vermeiden:

1. Laden Sie das Bild auf dem Hintergrund-Thread mit `submit().get()`.
2. Übergeben Sie das UI-Update an den Haupt-Thread mit `imageView.post { ... }`.
3. Wenn das geladene Ergebnis ein GIF-Drawable ist, starten Sie die Animation, nachdem Sie es auf der View gesetzt haben.

Dadurch wird das Laden von Bildern vom UI-Rendering getrennt, und Ihr eigener Image-Loader bleibt mit Android SDK 36.0.0 und höher kompatibel.

Diese Anleitung gilt für eigene Image-Loader unter Android. Web-In-App-Nachrichten unterstützen GIFs standardmäßig.

Das folgende Kotlin-Beispiel verwendet Platzhalterwerte, um dieses Muster zu veranschaulichen:

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

### Schritt 2: Festlegen des Image-Loader-Delegaten {#step-2-setting-the-image-loader-delegate}

Das Braze SDK verwendet jeden eigenen Image-Loader, der mit [`IBrazeImageLoader`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/index.html) festgelegt wird. Wir empfehlen, den eigenen Image-Loader in einer eigenen Application-Unterklasse zu konfigurieren:

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

## Eigenes Laden von Bildern mit Jetpack Compose {#custom-image-loading-with-jetpack-compose}

Um das Laden von Bildern mit Jetpack Compose zu überschreiben, können Sie einen Wert an [`imageComposable`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#-808910455%2FProperties%2F-1725759721) übergeben. Diese Funktion nimmt eine `Card` entgegen und rendert das Bild sowie die benötigten Modifier. Alternativ können Sie auch `customCardComposer` von `ContentCardsList` verwenden, um die gesamte Karte zu rendern.

Im folgenden Beispiel wird die Compose-Bibliothek von Glide für die in der Funktion `imageComposable` aufgeführten Karten verwendet:

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
