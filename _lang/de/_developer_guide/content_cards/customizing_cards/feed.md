---
nav_title: Standard-Feed
article_title: Den Feed für Content Cards anpassen
page_order: 3
description: "Dieser Artikel behandelt die Anpassungsmöglichkeiten von Content-Card-Feeds."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Den Feed für Content Cards anpassen {#customize-the-feed-for-content-cards}

> Ein Content-Card-Feed ist die Abfolge von Content Cards in Ihren Mobil- oder Internet-Apps. Dieser Artikel befasst sich mit der Konfiguration, wann der Feed aktualisiert wird, der Reihenfolge der Karten, der Verwaltung mehrerer Feeds und den Fehlermeldungen „leerer Feed“. Eine vollständige Liste der Content-Card-Typen finden Sie unter [Über Content Cards]({{site.baseurl}}/developer_guide/content_cards).

{% multi_lang_include developer_guide/_shared/about_session_lifecycle.md %}

## Aktualisieren des Feeds {#refreshing-the-feed}

### Automatische Aktualisierung {#automatic-refresh}

Standardmäßig wird der Content-Card-Feed automatisch aktualisiert, wenn:

- Eine neue Sitzung gestartet wird
- Der standardmäßige Content-Card-Feed geschlossen und nach mehr als 60 Sekunden seit der letzten Aktualisierung erneut geöffnet wird.

{% alert tip %}
Um aktuelle Content Cards dynamisch anzuzeigen, ohne den Feed manuell zu aktualisieren, wählen Sie bei der Erstellung der Karte **At first impression** aus. Diese Karten werden aktualisiert, sobald sie verfügbar sind.
{% endalert %}

### Realtime-Zustellung {#real-time-delivery}

Braze sendet Content-Card-Updates auch sofort an das Gerät, sobald sie auftreten – über eine aktive Verbindung, die das SDK während der Sitzung aufrechterhält. Nutzer:innen müssen keine neue Sitzung starten oder auf eine Aktualisierung warten, um die Änderung zu sehen.

Die Realtime-Zustellung umfasst folgende Updates:

- Nutzer:innen werden während einer Sitzung für eine Content-Card-Kampagne berechtigt.
- Nutzer:innen erreichen einen Content-Card-Schritt in einem Canvas.
- Eine Karte wird aus dem Feed von Nutzer:innen entfernt.
- Eine Karte wird über die API gesendet, z. B. mit dem [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)-, [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)- oder [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)-Endpunkt.

Die Realtime-Zustellung erfordert die folgenden minimalen SDK-Versionen:

{% sdk_min_versions swift:18.0.0 android:43.1.1 web:6.12.0 %}

Bei älteren SDK-Versionen werden Karten weiterhin beim Sitzungsstart und bei der Aktualisierung zugestellt.

### Manuelle Aktualisierung {#manual-refresh}

So aktualisieren Sie den Feed zu einem bestimmten Zeitpunkt manuell:

{% tabs %}
{% tab web %}

Fordern Sie jederzeit eine manuelle Aktualisierung der Braze Content Cards über das Web-SDK an, indem Sie [`requestContentCardsRefresh()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh) aufrufen.

Sie können auch [`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards) aufrufen, um alle derzeit verfügbaren Karten seit der letzten Content-Card-Aktualisierung abzurufen.

```javascript
import * as braze from "@braze/web-sdk";

function refresh() {
  braze.requestContentCardsRefresh();
}
```

Um Content-Card-Links in einem neuen Browser-Tab statt im gleichen Tab zu öffnen, setzen Sie `openCardsInNewTab: true` in Ihren Web-SDK-Initialisierungsoptionen. Weitere Informationen zu Initialisierungsoptionen finden Sie im [Web-SDK-Repository-Leitfaden]({{site.baseurl}}/developer_guide/sdk_repository_guides/web).

{% endtab %}
{% tab android %}

Fordern Sie jederzeit eine manuelle Aktualisierung der Braze Content Cards über das Android-SDK an, indem Sie [`requestContentCardsRefresh`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-content-cards-refresh.html) aufrufen.

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

Fordern Sie jederzeit eine manuelle Aktualisierung der Braze Content Cards über das Swift-SDK an, indem Sie die [`requestRefresh`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/requestrefresh(_:))-Methode der [`Braze.ContentCards`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class)-Klasse aufrufen:

{% subtabs local %}
{% subtab Swift %}

In Swift können Content Cards entweder mit einem optionalen Completion-Handler oder mit einer asynchronen Rückgabe über die nativen Swift-Concurrency-APIs aktualisiert werden.

#### Completion-Handler {#completion-handler}

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

### Vollständige Synchronisierung vs. teilweise Synchronisierung {#full-sync-vs-partial-sync}

Das Braze SDK verwendet zwei Arten der Synchronisierung beim Abrufen von Content Cards vom Server:

- **Vollständige Synchronisierung:** Ruft alle Content Cards ab, für die Nutzer:innen berechtigt sind. Vollständige Synchronisierungen erfolgen automatisch alle 7 Tage oder immer dann, wenn `changeUser()` aufgerufen wird.
- **Teilweise Synchronisierung:** Ruft nur neue Content Cards seit der letzten Anfrage ab. Wenn Nutzer:innen für keine neuen Karten berechtigt sind, gibt die Antwort null Karten zurück. Teilweise Synchronisierungen erfolgen bei jedem Aufruf von `requestContentCardsRefresh()` (es sei denn, seit der letzten vollständigen Synchronisierung sind 7 Tage vergangen – in diesem Fall wird stattdessen eine vollständige Synchronisierung ausgelöst).

Teilweise Synchronisierungen reduzieren die Serverlast und den Gerätebatterieverbrauch. Content Cards, die bereits empfangen wurden, werden lokal im SDK gespeichert, sodass Nutzer:innen ihre verfügbaren Karten auch dann weiterhin sehen, wenn eine teilweise Synchronisierung null neue Karten zurückgibt.

### Rate-Limits {#rate-limit}

Braze verwendet einen Token-Bucket-Algorithmus, um die folgenden Rate-Limits durchzusetzen:
- Bis zu 5 Aktualisierungsaufrufe pro Gerät, gemeinsam genutzt über Nutzer:innen und Aufrufe von `openSession()`
- Nach Erreichen des Limits wird ein neuer Aufruf alle 180 Sekunden (3 Minuten) verfügbar
- Das System hält bis zu fünf Aufrufe für Sie bereit, die Sie jederzeit verwenden können
- `subscribeToContentCards()` gibt auch bei aktiven Rate-Limits weiterhin zwischengespeicherte Karten zurück

{% alert important %}
Das Braze SDK wendet ebenfalls Rate-Limits für Performance und Zuverlässigkeit an. Beachten Sie dies bei automatisierten Tests oder manueller Qualitätssicherung. Weitere Informationen finden Sie unter [Braze SDK Rate-Limits]({{site.baseurl}}/developer_guide/sdk_integration/rate_limits).
{% endalert %}

## Anpassen der angezeigten Kartenreihenfolge {#customizing-displayed-card-order}

Sie können die Reihenfolge ändern, in der Ihre Content Cards angezeigt werden. So können Sie die Nutzererfahrung optimieren, indem Sie bestimmte Inhaltstypen priorisieren, zum Beispiel zeitkritische Aktionen.

{% tabs %}
{% tab web %}

Passen Sie die Anzeigereihenfolge von Content Cards in Ihrem Feed an, indem Sie den [`filterFunction`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards)-Parameter von `showContentCards():` verwenden. Zum Beispiel:

```javascript
braze.showContentCards(null, (cards) => {
  return sortBrazeCards(cards); // Where sortBrazeCards is your sorting function that returns the sorted card array
});
```

{% endtab %}
{% tab android %}
{% subtabs %}
{% subtab android view controller %}
Das [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) nutzt einen [`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html), um Content Cards vor der Anzeige im Feed zu sortieren oder zu modifizieren. Ein benutzerdefinierter Update-Handler kann über [`setContentCardUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/set-content-card-update-handler.html) auf Ihrem `ContentCardsFragment` festgelegt werden.

Der folgende Standard-`IContentCardsUpdateHandler` kann als Ausgangspunkt für Anpassungen verwendet werden:

{% details Java-Beispiel anzeigen %}
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

{% details Kotlin-Beispiel anzeigen %}
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
Den Quellcode von `ContentCardsFragment` finden Sie auf [GitHub](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/ContentCardsFragment.kt).
{% endalert %}
{% endsubtab %}
{% subtab Jetpack Compose %}
Um Content Cards in Jetpack Compose zu filtern und zu sortieren, legen Sie den Parameter `cardUpdateHandler` fest. Zum Beispiel:

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

Passen Sie die Reihenfolge des Card-Feeds an, indem Sie die statische Variable [`Attributes.defaults`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults) direkt modifizieren.

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

Die Anpassung über `BrazeContentCardUI.ViewController.Attributes` ist in Objective-C nicht verfügbar.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Anpassen der „Leerer Feed“-Nachricht {#customizing-empty-feed-message}

Wenn ein:e Nutzer:in sich nicht für Content Cards qualifiziert, zeigt das SDK eine „Leerer Feed“-Fehlermeldung an: „We have no updates. Please check again later.“ Sie können diese Fehlermeldung ähnlich wie im folgenden Beispiel anpassen:

![Eine „Leerer Feed“-Fehlermeldung mit dem Text „This is a custom empty state message.“]({% image_buster/assets/img/content_cards/content-card-customization-empty.png %})

{% tabs %}
{% tab web %}

Das Web-SDK unterstützt das programmgesteuerte Ersetzen der „Leerer Feed“-Sprache nicht. Sie können sie optional jedes Mal ersetzen, wenn der Feed angezeigt wird, dies wird jedoch nicht empfohlen, da der Feed möglicherweise einige Zeit zum Aktualisieren benötigt und der Text für den leeren Feed nicht sofort angezeigt wird.

{% endtab %}
{% tab android %}
{% subtabs %}
{% subtab android view system %}

Wenn das [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) feststellt, dass ein:e Nutzer:in sich nicht für Content Cards qualifiziert, wird die Fehlermeldung für den leeren Feed angezeigt.

Ein spezieller Adapter, der [`EmptyContentCardsAdapter`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/adapters/EmptyContentCardsAdapter.kt), ersetzt den Standard-[`ContentCardAdapter`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/adapters/ContentCardAdapter.kt), um diese Fehlermeldung anzuzeigen. Um die benutzerdefinierte Nachricht festzulegen, überschreiben Sie die String-Ressource `com_braze_feed_empty`.

Der Stil, der zur Anzeige dieser Nachricht verwendet wird, ist unter [`Braze.ContentCardsDisplay.Empty`](https://github.com/braze-inc/braze-android-sdk/blob/2e386dfa59a87bfc24ef7cb6ff5adf6b16f44d24/android-sdk-ui/src/main/res/values/styles.xml#L522-L530) zu finden und wird im folgenden Code-Snippet wiedergegeben:

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

Weitere Informationen zum Anpassen von Content-Card-Stilelementen finden Sie unter [Stil anpassen]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style).
{% endsubtab %}
{% subtab Jetpack Compose %}
Um die „Leerer Feed“-Fehlermeldung mit Jetpack Compose anzupassen, können Sie einen `emptyString` an [`ContentCardsList`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards/-content-cards-list.html) übergeben. Sie können auch [`emptyTextStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-list-styling/index.html#1193499348%2FProperties%2F-1725759721) an `ContentCardListStyling` übergeben, um diese Nachricht weiter anzupassen.

```kotlin
ContentCardsList(
    emptyString = "No messages today",
    style = ContentCardListStyling(
        emptyTextStyle = TextStyle(...)
    )
)
```

Wenn Sie ein Composable haben, das Sie stattdessen anzeigen möchten, können Sie `emptyComposable` an [`ContentCardsList`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards/-content-cards-list.html) übergeben. Wenn `emptyComposable` angegeben ist, wird `emptyString` nicht verwendet.

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

Passen Sie den leeren Zustand des View Controllers an, indem Sie die zugehörigen [`Attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults) festlegen.

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.emptyStateMessage = "This is a custom empty state message"
attributes.emptyStateMessageFont = .preferredFont(forTextStyle: .title1)
attributes.emptyStateMessageColor = .secondaryLabel
```

{% endsubtab %}
{% subtab Objective-C %}

Ändern Sie die Sprache, die automatisch in leeren Content-Card-Feeds angezeigt wird, indem Sie die lokalisierbaren Content-Card-Strings in der Datei [`ContentCardsLocalizable.strings`](https://github.com/braze-inc/braze-swift-sdk/tree/main/Sources/BrazeUI/Resources/Localization/en.lproj) Ihrer App neu definieren.

{% alert note %}
Wenn Sie diese Nachricht in verschiedenen Gebietsschema-Sprachen aktualisieren möchten, suchen Sie die entsprechende Sprache in der [Ordnerstruktur für Ressourcen](https://github.com/braze-inc/braze-swift-sdk/tree/main/Sources/BrazeUI/Resources/Localization) mit dem String `ContentCardsLocalizable.strings`.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Mehrere Feeds implementieren {#implementing-multiple-feeds}

Content Cards können in Ihrer App gefiltert werden, sodass nur bestimmte Cards angezeigt werden. So können Sie mehrere Content-Card-Feeds für unterschiedliche Anwendungsfälle einrichten. Beispielsweise können Sie sowohl einen transaktionalen Feed als auch einen Marketing-Feed pflegen. Erstellen Sie dazu verschiedene Kategorien von Content Cards, indem Sie Schlüssel-Wert-Paare im Braze-Dashboard festlegen. Erstellen Sie dann Feeds in Ihrer App oder Website, die diese Arten von Content Cards unterschiedlich behandeln, indem bestimmte Typen herausgefiltert und andere angezeigt werden.

### Schritt 1: Schlüssel-Wert-Paare für Cards festlegen {#step-1-set-key-value-pairs-on-cards}

Legen Sie beim Erstellen einer Content-Card-Kampagne [Schlüssel-Wert-Paar-Daten]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/behavior) für jede Card fest. Sie verwenden dieses Schlüssel-Wert-Paar, um Cards zu kategorisieren. Schlüssel-Wert-Paare werden in der Eigenschaft `extras` im Datenmodell der Card gespeichert.

In diesem Beispiel legen wir ein Schlüssel-Wert-Paar mit dem Schlüssel `feed_type` fest, das bestimmt, in welchem Content-Card-Feed die Card angezeigt werden soll. Der Wert entspricht dem jeweiligen benutzerdefinierten Feed, z. B. `home_screen` oder `marketing`.

### Schritt 2: Content Cards filtern {#step-2-filter-content-cards}

Nachdem Schlüssel-Wert-Paare zugewiesen wurden, erstellen Sie einen Feed mit einer Logik, die die gewünschten Cards anzeigt und Cards anderer Typen herausfiltert. In diesem Beispiel werden nur Cards mit dem passenden Schlüssel-Wert-Paar `feed_type: "Transactional"` angezeigt.

{% tabs %}
{% tab web %}

Das folgende Beispiel zeigt den Content-Cards-Feed für Cards des Typs `Transactional`:

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

Anschließend können Sie einen Umschalter für Ihren benutzerdefinierten Feed einrichten:

```javascript
// show the "Transactional" feed when this button is clicked
document.getElementById("show-transactional-feed").onclick = function() {
  showCardsByFeedType("Transactional");
};
```

Weitere Informationen finden Sie in der [SDK-Methodendokumentation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards).

{% endtab %}
{% tab android %}
{% subtabs %}
{% subtab android view system %}

Standardmäßig wird der Content-Cards-Feed in einem [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) angezeigt, und [`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html) gibt eine Liste von Cards zurück, die nach Empfang eines [`ContentCardsUpdatedEvent`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.events/-content-cards-updated-event/index.html) vom Braze SDK angezeigt werden sollen. Er sortiert jedoch nur Cards und übernimmt keine direkte Filterung.

#### Schritt 2.1: Einen benutzerdefinierten Handler erstellen {#step-21-create-a-custom-handler}

Sie können Content Cards herausfiltern, indem Sie einen benutzerdefinierten [`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html) implementieren. Verwenden Sie dazu die im Dashboard über [`Card.getExtras()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/extras.html) festgelegten Schlüssel-Wert-Paare und passen Sie ihn so an, dass alle Cards aus der Liste entfernt werden, die nicht dem zuvor festgelegten Wert für `feed_type` entsprechen.

{% details Java-Beispiel anzeigen %}
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

{% details Kotlin-Beispiel anzeigen %}
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

#### Schritt 2.2: Zum Fragment hinzufügen {#step-22-add-it-to-a-fragment}

Nachdem Sie einen [`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html) erstellt haben, erstellen Sie ein [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html), das ihn verwendet. Dieser benutzerdefinierte Feed kann wie jedes andere `ContentCardsFragment` verwendet werden. In den verschiedenen Bereichen Ihrer App können Sie unterschiedliche Content-Card-Feeds basierend auf dem im Dashboard festgelegten Schlüssel anzeigen. Jeder `ContentCardsFragment`-Feed zeigt dank des benutzerdefinierten `IContentCardsUpdateHandler` auf jedem Fragment einen eigenen Satz von Cards an.

{% details Java-Beispiel anzeigen %}
```java
// We want a Content Cards feed that only shows "Transactional" cards.
ContentCardsFragment customContentCardsFragment = new ContentCardsFragment();
customContentCardsFragment.setContentCardUpdateHandler(getUpdateHandlerForFeedType("Transactional"));
```
{% enddetails %}

{% details Kotlin-Beispiel anzeigen %}
```kotlin
// We want a Content Cards feed that only shows "Transactional" cards.
val customContentCardsFragment = ContentCardsFragment()
customContentCardsFragment.contentCardUpdateHandler = getUpdateHandlerForFeedType("Transactional")
```
{% enddetails %}
{% endsubtab %}

{% subtab Jetpack Compose %}
Um zu filtern, welche Content Cards in diesem Feed angezeigt werden, verwenden Sie `cardUpdateHandler`. Zum Beispiel:

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

Um noch einen Schritt weiterzugehen, können die im View Controller angezeigten Cards gefiltert werden, indem Sie die Eigenschaft `transform` in Ihrer `Attributes`-Struktur so setzen, dass nur die nach Ihren Kriterien gefilterten Cards angezeigt werden.

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