---
nav_title: Fuente predeterminada
article_title: Personalizar la fuente para Content Cards
page_order: 3
description: "Este artículo trata de las opciones de personalización de la fuente de Content Cards."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Personalizar la fuente para Content Cards {#customize-the-feed-for-content-cards}

> Una fuente de Content Cards es la secuencia de Content Cards en tus aplicaciones móviles o web. Este artículo cubre la configuración de cuándo se actualiza la fuente, el orden de las tarjetas, la gestión de múltiples fuentes y los mensajes de error de "fuente vacía". Para obtener la lista completa de tipos de tarjetas de contenido, consulta [Acerca de Content Cards]({{site.baseurl}}/developer_guide/content_cards).

{% multi_lang_include developer_guide/_shared/about_session_lifecycle.md %}

## Actualizar la fuente {#refreshing-the-feed}

### Actualización automática {#automatic-refresh}

De forma predeterminada, la fuente de Content Cards se actualizará automáticamente cuando:

- Se inicie una nueva sesión
- La fuente predeterminada de Content Cards se cierre y se vuelva a abrir después de que hayan transcurrido más de 60 segundos desde la última actualización.

{% alert tip %}
Para mostrar dinámicamente Content Cards actualizadas sin necesidad de actualizar manualmente, selecciona **At first impression** durante la creación de la tarjeta. Estas tarjetas se actualizarán cuando estén disponibles.
{% endalert %}

### Entrega en tiempo real {#real-time-delivery}

Braze también envía actualizaciones de Content Cards al dispositivo en cuanto ocurren, a través de una conexión en vivo que el SDK mantiene durante la sesión. Los usuarios no necesitan iniciar una nueva sesión ni esperar una actualización para ver el cambio.

La entrega en tiempo real cubre las siguientes actualizaciones:

- Un usuario se vuelve elegible para una campaña de Content Cards durante una sesión.
- Un usuario avanza a un paso de Content Cards en un Canvas.
- Se elimina una tarjeta de la fuente de un usuario.
- Se envía una tarjeta a través de la API, como con el endpoint [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages), [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) o [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases).

La entrega en tiempo real requiere las siguientes versiones mínimas del SDK:

{% sdk_min_versions swift:18.0.0 android:43.1.1 web:6.12.0 %}

En versiones anteriores del SDK, las tarjetas siguen llegando al inicio de sesión y durante la actualización.

### Actualización manual {#manual-refresh}

Para actualizar manualmente la fuente en un momento específico:

{% tabs %}
{% tab web %}

Solicita una actualización manual de Content Cards de Braze desde el SDK Web en cualquier momento llamando a [`requestContentCardsRefresh()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh).

También puedes llamar a [`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards) para obtener todas las tarjetas disponibles actualmente desde la última actualización de Content Cards.

```javascript
import * as braze from "@braze/web-sdk";

function refresh() {
  braze.requestContentCardsRefresh();
}
```

Para abrir los enlaces de Content Cards en una nueva pestaña del navegador en lugar de la misma pestaña, establece `openCardsInNewTab: true` en las opciones de inicialización del SDK Web. Para más información sobre las opciones de inicialización, consulta la [guía del repositorio del SDK Web]({{site.baseurl}}/developer_guide/sdk_repository_guides/web).

{% endtab %}
{% tab android %}

Solicita una actualización manual de Content Cards de Braze desde el SDK de Android en cualquier momento llamando a [`requestContentCardsRefresh`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-content-cards-refresh.html).

{% subtabs local %}
{% subtab Java %}

```java
Braze.getInstance(context).requestContentCardsRefresh();
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
Braze.getInstance(context).requestContentCardsRefresh()
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}

Solicita una actualización manual de Content Cards de Braze desde el SDK de Swift en cualquier momento llamando al método [`requestRefresh`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/requestrefresh(_:)) en la clase [`Braze.ContentCards`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class):

{% subtabs local %}
{% subtab Swift %}

En Swift, Content Cards se pueden actualizar con un controlador de finalización opcional o con un retorno asíncrono utilizando las API nativas de concurrencia de Swift.

#### Controlador de finalización {#completion-handler}

```swift
AppDelegate.braze?.contentCards.requestRefresh { result in
  // Implement completion handler
}
```

#### Async/Await

```swift
let contentCards = await AppDelegate.braze?.contentCards.requestRefresh()
```
{% endsubtab %}
{% subtab Objective-C %}

```objc
[AppDelegate.braze.contentCards requestRefreshWithCompletion:^(NSArray<BRZContentCardRaw *> * contentCards, NSError * error) {
  // Implement completion handler
}];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Sincronización completa vs. sincronización parcial {#full-sync-vs-partial-sync}

El SDK de Braze utiliza dos tipos de sincronización al obtener Content Cards del servidor:

- **Sincronización completa:** Descarga todas las Content Cards para las que un usuario es elegible. Las sincronizaciones completas se realizan automáticamente cada 7 días o cuando se llama a `changeUser()`.
- **Sincronización parcial:** Descarga solo las Content Cards nuevas desde la última solicitud. Si el usuario no es elegible para ninguna tarjeta nueva, la respuesta devuelve cero tarjetas. Las sincronizaciones parciales se realizan cada vez que se llama a `requestContentCardsRefresh()` (a menos que hayan transcurrido 7 días desde la última sincronización completa, en cuyo caso se desencadena una sincronización completa).

Las sincronizaciones parciales reducen la carga del servidor y el consumo de batería del dispositivo. Las Content Cards que ya se han recibido se almacenan localmente en el SDK, por lo que los usuarios seguirán viendo sus tarjetas disponibles incluso cuando una sincronización parcial devuelva cero tarjetas nuevas.

### Límite de velocidad {#rate-limit}

Braze utiliza un algoritmo de contenedor de tokens para aplicar los siguientes límites de velocidad:
- Hasta 5 llamadas de actualización por dispositivo, compartidas entre usuarios y llamadas a `openSession()`
- Después de alcanzar el límite, una nueva llamada estará disponible cada 180 segundos (3 minutos)
- El sistema mantendrá hasta cinco llamadas para que las utilices en cualquier momento
- `subscribeToContentCards()` seguirá devolviendo tarjetas en caché incluso cuando se aplique el límite de velocidad

{% alert important %}
El SDK de Braze también aplica límites de velocidad para el rendimiento y la fiabilidad. Ten esto en cuenta al ejecutar pruebas automatizadas o realizar pruebas manuales de control de calidad. Consulta [Límites de velocidad del SDK de Braze]({{site.baseurl}}/developer_guide/sdk_integration/rate_limits) para más información.
{% endalert %}

## Personalización del orden de visualización de las tarjetas {#customizing-displayed-card-order}

Puedes cambiar el orden en que se muestran tus Content Cards. Esto te permite ajustar la experiencia del usuario priorizando ciertos tipos de contenido, como promociones con tiempo limitado.

{% tabs %}
{% tab web %}

Personaliza el orden de visualización de las Content Cards en tu fuente usando el parámetro [`filterFunction`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards) de `showContentCards():`. Por ejemplo:

```javascript
braze.showContentCards(null, (cards) => {
  return sortBrazeCards(cards); // Where sortBrazeCards is your sorting function that returns the sorted card array
});
```

{% endtab %}
{% tab android %}
{% subtabs %}
{% subtab android view controller %}
El [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) se apoya en un [`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html) para manejar cualquier ordenación o modificación de las Content Cards antes de que se muestren en la fuente. Se puede establecer un controlador de actualización personalizado mediante [`setContentCardUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/set-content-card-update-handler.html) en tu `ContentCardsFragment`.

El siguiente es el `IContentCardsUpdateHandler` predeterminado y puede usarse como punto de partida para la personalización:

{% details Mostrar ejemplo en Java %}
```java
public class DefaultContentCardsUpdateHandler implements IContentCardsUpdateHandler {

  // Interface that must be implemented and provided as a public CREATOR
  // field that generates instances of your Parcelable class from a Parcel.
  public static final Parcelable.Creator<DefaultContentCardsUpdateHandler> CREATOR = new Parcelable.Creator<DefaultContentCardsUpdateHandler>() {
    public DefaultContentCardsUpdateHandler createFromParcel(Parcel in) {
      return new DefaultContentCardsUpdateHandler();
    }

    public DefaultContentCardsUpdateHandler[] newArray(int size) {
      return new DefaultContentCardsUpdateHandler[size];
    }
  };

  @Override
  public List<Card> handleCardUpdate(ContentCardsUpdatedEvent event) {
    List<Card> sortedCards = event.getAllCards();
    // Sort by pinned, then by the 'updated' timestamp descending
    // Pinned before non-pinned
    Collections.sort(sortedCards, new Comparator<Card>() {
      @Override
      public int compare(Card cardA, Card cardB) {
        // A displays above B
        if (cardA.getIsPinned() && !cardB.getIsPinned()) {
          return -1;
        }

        // B displays above A
        if (!cardA.getIsPinned() && cardB.getIsPinned()) {
          return 1;
        }

        // At this point, both A & B are pinned or both A & B are non-pinned
        // A displays above B since A is newer
        if (cardA.getUpdated() > cardB.getUpdated()) {
          return -1;
        }

        // B displays above A since A is newer
        if (cardA.getUpdated() < cardB.getUpdated()) {
          return 1;
        }

        // At this point, every sortable field matches so keep the natural ordering
        return 0;
      }
    });

    return sortedCards;
  }

  // Parcelable interface method
  @Override
  public int describeContents() {
    return 0;
  }

  // Parcelable interface method
  @Override
  public void writeToParcel(Parcel dest, int flags) {
    // No state is kept in this class so the parcel is left unmodified
  }
}
```
{% enddetails %}

{% details Mostrar ejemplo en Kotlin %}
```kotlin
class DefaultContentCardsUpdateHandler : IContentCardsUpdateHandler {
  override fun handleCardUpdate(event: ContentCardsUpdatedEvent): List<Card> {
    val sortedCards = event.allCards
    // Sort by pinned, then by the 'updated' timestamp descending
    // Pinned before non-pinned
    sortedCards.sortWith(Comparator sort@{ cardA: Card, cardB: Card ->
      // A displays above B
      if (cardA.isPinned && !cardB.isPinned) {
        return@sort -1
      }

      // B displays above A
      if (!cardA.isPinned && cardB.isPinned) {
        return@sort 1
      }

      // At this point, both A & B are pinned or both A & B are non-pinned
      // A displays above B since A is newer
      if (cardA.updated > cardB.updated) {
        return@sort -1
      }

      // B displays above A since A is newer
      if (cardA.updated < cardB.updated) {
        return@sort 1
      }
      0
    })
    return sortedCards
  }

  // Parcelable interface method
  override fun describeContents(): Int {
    return 0
  }

  // Parcelable interface method
  override fun writeToParcel(dest: Parcel, flags: Int) {
    // No state is kept in this class so the parcel is left unmodified
  }

  companion object {
    // Interface that must be implemented and provided as a public CREATOR
    // field that generates instances of your Parcelable class from a Parcel.
    val CREATOR: Parcelable.Creator<DefaultContentCardsUpdateHandler?> = object : Parcelable.Creator<DefaultContentCardsUpdateHandler?> {
      override fun createFromParcel(`in`: Parcel): DefaultContentCardsUpdateHandler? {
        return DefaultContentCardsUpdateHandler()
      }

      override fun newArray(size: Int): Array<DefaultContentCardsUpdateHandler?> {
        return arrayOfNulls(size)
      }
    }
  }
}
```
{% enddetails %}

{% alert tip %}
El código fuente de `ContentCardsFragment` se encuentra en [GitHub](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/ContentCardsFragment.kt).
{% endalert %}
{% endsubtab %}
{% subtab Jetpack Compose %}
Para filtrar y ordenar Content Cards en Jetpack Compose, establece el parámetro `cardUpdateHandler`. Por ejemplo:

```kotlin
ContentCardsList(
    cardUpdateHandler = {
        it.sortedWith { cardA, cardB ->
            // A displays above B
            if (cardA.isPinned && !cardB.isPinned) {
                return@sortedWith -1
            }
            // B displays above A
            if (!cardA.isPinned && cardB.isPinned) {
                return@sortedWith 1
            }
            // At this point, both A & B are pinned or both A & B are non-pinned
            // A displays above B since A is newer
            if (cardA.updated > cardB.updated) {
                return@sortedWith -1
            }
            // B displays above A since A is newer
            if (cardA.updated < cardB.updated) {
                return@sortedWith 1
            }
            0
        }
    }
)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}

{% subtabs %}
{% subtab Swift %}

Personaliza el orden de la fuente de tarjetas modificando directamente la variable estática [`Attributes.defaults`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults).

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.transform = { cards in
    cards.sorted {
        if $0.pinned && !$1.pinned {
            return true
        } else if !$0.pinned && $1.pinned {
            return false
        } else {
            return $0.createdAt > $1.createdAt
        }
    }
}
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

La personalización mediante `BrazeContentCardUI.ViewController.Attributes` no está disponible en Objective-C.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Personalizar el mensaje de "fuente vacía" {#customizing-empty-feed-message}

Cuando un usuario no califica para ninguna Content Cards, el SDK muestra un mensaje de error de "fuente vacía" que dice: "We have no updates. Please check again later." Puedes personalizar este mensaje de error de "fuente vacía" de forma similar a la siguiente:

![Un mensaje de error de fuente vacía que dice "This is a custom empty state message."]({% image_buster/assets/img/content_cards/content-card-customization-empty.png %})

{% tabs %}
{% tab web %}

El SDK Web no admite reemplazar el idioma de la "fuente vacía" de forma programática. Puedes optar por reemplazarlo cada vez que se muestre la fuente, pero no se recomienda porque la fuente puede tardar un tiempo en actualizarse y el texto de fuente vacía no se mostrará de inmediato.

{% endtab %}
{% tab android %}
{% subtabs %}
{% subtab android view system %}

Si el [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) determina que el usuario no califica para ninguna Content Cards, muestra el mensaje de error de fuente vacía.

Un adaptador especial, el [`EmptyContentCardsAdapter`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/adapters/EmptyContentCardsAdapter.kt), reemplaza al [`ContentCardAdapter`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/adapters/ContentCardAdapter.kt) estándar para mostrar este mensaje de error. Para establecer el mensaje personalizado, redefine el recurso de cadena `com_braze_feed_empty`.

El estilo utilizado para mostrar este mensaje se puede encontrar en [`Braze.ContentCardsDisplay.Empty`](https://github.com/braze-inc/braze-android-sdk/blob/2e386dfa59a87bfc24ef7cb6ff5adf6b16f44d24/android-sdk-ui/src/main/res/values/styles.xml#L522-L530) y se reproduce en el siguiente fragmento de código:

```xml
<style name="Braze.ContentCardsDisplay.Empty">
  <item name="android:lineSpacingExtra">1.5dp</item>
  <item name="android:text">@string/com_braze_feed_empty</item>
  <item name="android:textColor">@color/com_braze_content_card_empty_text_color</item>
  <item name="android:textSize">18.0sp</item>
  <item name="android:gravity">center</item>
  <item name="android:layout_height">match_parent</item>
  <item name="android:layout_width">match_parent</item>
</style>
```

Para obtener más información sobre cómo personalizar los elementos de estilo de Content Cards, consulta [Personalizar el estilo]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style).
{% endsubtab %}
{% subtab Jetpack Compose %}
Para personalizar el mensaje de error de "fuente vacía" con Jetpack Compose, puedes pasar un `emptyString` a [`ContentCardsList`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards/-content-cards-list.html). También puedes pasar [`emptyTextStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-list-styling/index.html#1193499348%2FProperties%2F-1725759721) a `ContentCardListStyling` para personalizar aún más este mensaje.

```kotlin
ContentCardsList(
    emptyString = "No messages today",
    style = ContentCardListStyling(
        emptyTextStyle = TextStyle(...)
    )
)
```

Si tienes un Composable que te gustaría mostrar en su lugar, puedes pasar `emptyComposable` a [`ContentCardsList`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards/-content-cards-list.html). Si se especifica `emptyComposable`, no se utilizará el `emptyString`.

```kotlin
ContentCardsList(
    emptyComposable = {
        Image(
            painter = painterResource(id = R.drawable.noMessages),
            contentDescription = "No messages"
        )
    }
)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}
{% subtabs local %}
{% subtab Swift %}

Personaliza el estado vacío del controlador de vista configurando los [`Attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults) relacionados.

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.emptyStateMessage = "This is a custom empty state message"
attributes.emptyStateMessageFont = .preferredFont(forTextStyle: .title1)
attributes.emptyStateMessageColor = .secondaryLabel
```

{% endsubtab %}
{% subtab Objective-C %}

Cambia el idioma que aparece automáticamente en las fuentes de Content Cards vacías redefiniendo las cadenas localizables de Content Cards en el archivo [`ContentCardsLocalizable.strings`](https://github.com/braze-inc/braze-swift-sdk/tree/main/Sources/BrazeUI/Resources/Localization/en.lproj) de tu aplicación.

{% alert note %}
Si deseas actualizar este mensaje en diferentes idiomas de configuración regional, busca el idioma correspondiente en la [estructura de carpetas de recursos](https://github.com/braze-inc/braze-swift-sdk/tree/main/Sources/BrazeUI/Resources/Localization) con la cadena `ContentCardsLocalizable.strings`.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Implementar múltiples fuentes {#implementing-multiple-feeds}

Las Content Cards se pueden filtrar en tu aplicación para que solo se muestren tarjetas específicas, lo que te permite tener múltiples fuentes de Content Cards para diferentes casos de uso. Por ejemplo, puedes mantener tanto una fuente transaccional como una fuente de marketing. Para lograr esto, crea diferentes categorías de Content Cards configurando pares clave-valor en el panel de Braze. Luego, crea fuentes en tu aplicación o sitio que traten estos tipos de Content Cards de manera diferente, filtrando algunos tipos y mostrando otros.

### Paso 1: Configurar pares clave-valor en las tarjetas {#step-1-set-key-value-pairs-on-cards}

Al crear una campaña de Content Cards, configura los [datos de par clave-valor]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/behavior) en cada tarjeta. Utilizarás este par clave-valor para categorizar las tarjetas. Los pares clave-valor se almacenan en la propiedad `extras` del modelo de datos de la tarjeta.

Para este ejemplo, configuraremos un par clave-valor con la clave `feed_type` que designará en qué fuente de Content Cards debe mostrarse la tarjeta. El valor será el que corresponda a tus fuentes personalizadas, como `home_screen` o `marketing`.

### Paso 2: Filtrar Content Cards {#step-2-filter-content-cards}

Una vez que se hayan asignado los pares clave-valor, crea una fuente con lógica que muestre las tarjetas que deseas mostrar y filtre las tarjetas de otros tipos. En este ejemplo, solo mostraremos las tarjetas con un par clave-valor coincidente de `feed_type: "Transactional"`.

{% tabs %}
{% tab web %}

El siguiente ejemplo mostrará la fuente de Content Cards para tarjetas de tipo `Transactional`:

```javascript

/**
 * @param {String} feed_type - value of the "feed_type" KVP to filter
 */
function showCardsByFeedType(feed_type) {
  braze.showContentCards(null, function(cards) {
    return cards.filter((card) => card.extras["feed_type"] === feed_type);
  });
}
```

Luego, puedes configurar un alternador para tu fuente personalizada:

```javascript
// show the "Transactional" feed when this button is clicked
document.getElementById("show-transactional-feed").onclick = function() {
  showCardsByFeedType("Transactional");
};
```

Para más información, consulta la [documentación de métodos del SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards).

{% endtab %}
{% tab android %}
{% subtabs %}
{% subtab android view system %}

De forma predeterminada, la fuente de Content Cards se muestra en un [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) y [`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html) devuelve una lista de tarjetas para mostrar después de recibir un [`ContentCardsUpdatedEvent`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.events/-content-cards-updated-event/index.html) del SDK de Braze. Sin embargo, solo ordena las tarjetas y no maneja ningún filtrado directamente.

#### Paso 2.1: Crear un controlador personalizado {#step-21-create-a-custom-handler}

Puedes filtrar Content Cards implementando un [`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html) personalizado usando los pares clave-valor configurados por [`Card.getExtras()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/extras.html) en el panel, luego modificándolo para eliminar cualquier tarjeta de la lista que no coincida con el valor de `feed_type` que configuraste anteriormente.

{% details Mostrar ejemplo en Java %}
```java
private IContentCardsUpdateHandler getUpdateHandlerForFeedType(final String desiredFeedType) {
  return new IContentCardsUpdateHandler() {
    @Override
    public List<Card> handleCardUpdate(ContentCardsUpdatedEvent event) {
      // Use the default card update handler for a first
      // pass at sorting the cards. This is not required
      // but is done for convenience.
      final List<Card> cards = new DefaultContentCardsUpdateHandler().handleCardUpdate(event);

      final Iterator<Card> cardIterator = cards.iterator();
      while (cardIterator.hasNext()) {
        final Card card = cardIterator.next();

        // Make sure the card has our custom KVP
        // from the dashboard with the key "feed_type"
        if (card.getExtras().containsKey("feed_type")) {
          final String feedType = card.getExtras().get("feed_type");
          if (!desiredFeedType.equals(feedType)) {
            // The card has a feed type, but it doesn't match
            // our desired feed type, remove it.
            cardIterator.remove();
          }
        } else {
          // The card doesn't have a feed
          // type at all, remove it
          cardIterator.remove();
        }
      }

      // At this point, all of the cards in this list have
      // a feed type that explicitly matches the value we put
      // in the dashboard.
      return cards;
    }
  };
}
```
{% enddetails %}

{% details Mostrar ejemplo en Kotlin %}
```kotlin
private fun getUpdateHandlerForFeedType(desiredFeedType: String): IContentCardsUpdateHandler {
  return IContentCardsUpdateHandler { event ->
    // Use the default card update handler for a first
    // pass at sorting the cards. This is not required
    // but is done for convenience.
    val cards = DefaultContentCardsUpdateHandler().handleCardUpdate(event)

    val cardIterator = cards.iterator()
    while (cardIterator.hasNext()) {
      val card = cardIterator.next()

      // Make sure the card has our custom KVP
      // from the dashboard with the key "feed_type"
      if (card.extras.containsKey("feed_type")) {
        val feedType = card.extras["feed_type"]
        if (desiredFeedType != feedType) {
          // The card has a feed type, but it doesn't match
          // our desired feed type, remove it.
          cardIterator.remove()
        }
      } else {
        // The card doesn't have a feed
        // type at all, remove it
        cardIterator.remove()
      }
    }

    // At this point, all of the cards in this list have
    // a feed type that explicitly matches the value we put
    // in the dashboard.
    cards
  }
}
```
{% enddetails %}

#### Paso 2.2: Añadirlo a un fragmento {#step-22-add-it-to-a-fragment}

Una vez que hayas creado un [`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html), crea un [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) que lo utilice. Esta fuente personalizada se puede usar como cualquier otro `ContentCardsFragment`. En las diferentes partes de tu aplicación, muestra diferentes fuentes de Content Cards basándote en la clave proporcionada en el panel. Cada fuente de `ContentCardsFragment` tendrá un conjunto único de tarjetas mostradas gracias al `IContentCardsUpdateHandler` personalizado en cada fragmento.

{% details Mostrar ejemplo en Java %}
```java
// We want a Content Cards feed that only shows "Transactional" cards.
ContentCardsFragment customContentCardsFragment = new ContentCardsFragment();
customContentCardsFragment.setContentCardUpdateHandler(getUpdateHandlerForFeedType("Transactional"));
```
{% enddetails %}

{% details Mostrar ejemplo en Kotlin %}
```kotlin
// We want a Content Cards feed that only shows "Transactional" cards.
val customContentCardsFragment = ContentCardsFragment()
customContentCardsFragment.contentCardUpdateHandler = getUpdateHandlerForFeedType("Transactional")
```
{% enddetails %}
{% endsubtab %}

{% subtab Jetpack Compose %}
Para filtrar qué Content Cards se muestran en esta fuente, usa `cardUpdateHandler`. Por ejemplo:

```kotlin
ContentCardsList(
     cardUpdateHandler = {
         it.filter { card ->
             card.extras["feed_type"] == "Transactional"
         }
     }
 )
 ```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}

The following example will show the Content Cards feed for `Transactional` type cards:

{% subtabs %}
{% subtab Swift %}

```swift
// Filter cards by the `Transactional` feed type based on your key-value pair.
let transactionalCards = cards.filter { $0.extras["feed_type"] as? String == "Transactional" }
```

Para ir un paso más allá, las tarjetas presentadas en el controlador de vista se pueden filtrar configurando la propiedad `transform` en tu estructura `Attributes` para mostrar solo las tarjetas filtradas por tus criterios.

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.transform = { cards in
  cards.filter { $0.extras["feed_type"] as? String == "Transactional" }
}

// Pass your attributes containing the transformed cards to the Content Card UI.
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
// Filter cards by the `Transactional` feed type based on your key-value pair.
NSMutableArray<BRZContentCardRaw *> *transactionalCards = [[NSMutableArray alloc] init];
for (BRZContentCardRaw *card in AppDelegate.braze.contentCards.cards) {
  if ([card.extras[@"feed_type"] isEqualToString:@"Transactional"]) {
    [transactionalCards addObject:card];
  }
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}