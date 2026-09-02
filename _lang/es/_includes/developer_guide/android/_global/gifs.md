## Acerca de los GIF {#about-gifs}

Braze ofrece la posibilidad de utilizar una biblioteca de imágenes personalizada para mostrar GIF animados. Aunque el siguiente ejemplo utiliza [Glide](https://bumptech.github.io/glide/), cualquier biblioteca de imágenes compatible con GIF es válida.

## Integración de una biblioteca de imágenes personalizada {#integrating-a-custom-image-library}

### Paso 1: Crear el delegado del cargador de imágenes {#step-1-creating-the-image-loader-delegate}

El delegado del cargador de imágenes debe implementar los siguientes métodos:

* [`getInAppMessageBitmapFromUrl()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/get-in-app-message-bitmap-from-url.html)
* [`getPushBitmapFromUrl()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/get-push-bitmap-from-url.html)
* [`renderUrlIntoCardView()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/render-url-into-card-view.html)
* [`renderUrlIntoInAppMessageView()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/render-url-into-in-app-message-view.html)
* [`setOffline()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/set-offline.html)

El siguiente ejemplo de integración está tomado de la [aplicación de ejemplo de integración con Glide](https://github.com/braze-inc/braze-android-sdk/tree/master/samples/glide-image-integration) incluida con el SDK or kit de desarrollo de software de Braze para Android.

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

### Corrección de la carga de imágenes para Android SDK or kit de desarrollo de software 36.0.0 y posteriores {#fixing-image-loading-for-android-sdk-3600-and-later}

En Android SDK or kit de desarrollo de software 36.0.0 y posteriores, `displayInAppMessage()` es una función `suspend`. Esto significa que `renderUrlIntoInAppMessageView()` se ejecuta en un hilo en segundo plano en lugar del hilo principal.

Si tu cargador de imágenes personalizado llama a `Glide.into(imageView)` en `renderUrlIntoInAppMessageView()`, tu aplicación puede fallar con el error "You must call this method on the main thread."

Para evitar esto:

1. Carga la imagen en el hilo en segundo plano con `submit().get()`.
2. Publica la actualización de la interfaz de usuario en el hilo principal con `imageView.post { ... }`.
3. Si el resultado cargado es un drawable GIF, inicia la animación después de configurarlo en la vista.

Esto separa la carga de imágenes del renderizado de la interfaz de usuario y mantiene tu cargador de imágenes personalizado compatible con Android SDK or kit de desarrollo de software 36.0.0 y posteriores.

Esta guía aplica a cargadores de imágenes personalizados de Android. Los mensajes dentro de la aplicación Web admiten GIF de forma nativa.

El siguiente ejemplo en Kotlin utiliza valores de marcador de posición para mostrar este patrón:

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

### Paso 2: Configurar el delegado del cargador de imágenes {#step-2-setting-the-image-loader-delegate}

El SDK or kit de desarrollo de software de Braze utilizará cualquier cargador de imágenes personalizado configurado con [`IBrazeImageLoader`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/index.html). Recomendamos configurar el cargador de imágenes personalizado en una subclase personalizada de la aplicación:

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

### Solución de problemas en la carga de imágenes con Glide {#troubleshooting-glide-image-loads}

Si las imágenes dejan de cargarse después de configurar un [`IBrazeImageLoader`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.images/-i-braze-image-loader/index.html) personalizado (por ejemplo, con Glide), verifica si un interceptor global de OkHttp está añadiendo encabezados de autenticación a cada solicitud.

El ejemplo de Glide en esta página utiliza la misma ruta de carga para Content Cards, mensajes dentro de la aplicación y push. Las imágenes alojadas en Braze son URLs de CDN y no utilizan la autenticación de tu REST or transferencia de estado representacional API. Limita el alcance de los interceptores a los hosts de tu propia API, o excluye los hosts de imágenes de Braze. Una imagen de Content Cards que falla tras una integración con Glide es un síntoma común de este patrón de interceptor.

## Carga de imágenes personalizada con Jetpack Compose {#custom-image-loading-with-jetpack-compose}

Para anular la carga de imágenes con Jetpack Compose, puedes pasar un valor a [`imageComposable`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#-808910455%2FProperties%2F-1725759721). Esta función tomará un `Card` y renderizará la imagen y los modificadores necesarios. Como alternativa, puedes utilizar `customCardComposer` de `ContentCardsList` para renderizar la tarjeta completa.

En el siguiente ejemplo, se utiliza la biblioteca Compose de Glide para las tarjetas enumeradas en la función `imageComposable`:

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
