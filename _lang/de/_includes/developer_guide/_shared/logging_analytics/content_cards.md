> Beim Erstellen einer angepassten UI für Content Cards müssen Sie Analytics wie Impressionen, Klicks und Ausblendungen manuell protokollieren, da dies nur für Standard-Kartenmodelle automatisch erfolgt. Die Protokollierung dieser Ereignisse ist ein Standardbestandteil der Integration von Content Cards und für eine genaue Campaign-Berichterstattung und Abrechnung unerlässlich. Füllen Sie dazu Ihre angepasste UI mit Daten aus den Braze-Datenmodellen und protokollieren Sie die Ereignisse anschließend manuell. Sobald Sie wissen, wie man Analytics protokolliert, können Sie sehen, wie Braze-Kund:innen häufig [angepasste Content Cards erstellen]({{site.baseurl}}/developer_guide/content_cards/creating_cards).

## Analytics protokollieren {#logging-analytics}

Wenn Sie Ihre angepassten Content Cards implementieren, können Sie die Content-Card-Objekte parsen und deren Payload-Daten wie `title`, `cardDescription` und `imageUrl` extrahieren. Anschließend können Sie die resultierenden Modelldaten verwenden, um Ihre angepasste UI zu befüllen.

Um die Content-Card-Datenmodelle zu erhalten, abonnieren Sie Content-Card-Updates. Zwei Eigenschaften verdienen besondere Aufmerksamkeit:

* **`id`**: Repräsentiert den Content-Card-ID-String. Dies ist der eindeutige Bezeichner, der zum Protokollieren von Analytics aus angepassten Content Cards verwendet wird.
* **`extras`**: Umfasst alle Schlüssel-Wert-Paare aus dem Braze-Dashboard.

Alle Eigenschaften außer `id` und `extras` sind für angepasste Content Cards optional zu parsen. Weitere Informationen zum Datenmodell finden Sie im Integrationsartikel der jeweiligen Plattform: [Android]({{site.baseurl}}/developer_guide/content_cards/?sdktab=android), [iOS]({{site.baseurl}}/developer_guide/content_cards/?sdktab=swift), [Web]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web).


{% tabs %}
{% tab web %}

Registrierung or registrieren Sie eine Callback-Funktion, um Updates zu abonnieren, wenn Cards aktualisiert werden.

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToContentCardsUpdates((updates) => {
  const cards = updates.cards;
// For example:
  cards.forEach(card => {
    if (card.isControl) {
      // Do not display the control card, but remember to call `logContentCardImpressions([card])`
    }
    else if (card instanceof braze.ClassicCard || card instanceof braze.CaptionedImage) {
      // Use `card.title`, `card.imageUrl`, etc.
    }
    else if (card instanceof braze.ImageOnly) {
      // Use `card.imageUrl`, etc.
    }
  })
});

braze.openSession();
```

{% alert note %}
Content Cards werden nur beim Sitzungsstart aktualisiert, wenn eine Abonnement-Anfrage vor `openSession()` aufgerufen wird. Sie können den [Feed auch jederzeit manuell Update or aktualisieren or aktualisieren]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed).
{% endalert %}

{% endtab %}
{% tab android %}
{% subtabs local %}
{% subtab Java %}

### Schritt 1: Erstellen Sie eine private Abonnent-Variable {#step-1-create-a-private-subscriber-variable}

Um Card-Updates zu abonnieren, deklarieren Sie zunächst eine private Variable in Ihrer angepassten Klasse, die Ihren Abonnenten hält:

```java
// subscriber variable
private IEventSubscriber<ContentCardsUpdatedEvent> mContentCardsUpdatedSubscriber;
```

### Schritt 2: Updates abonnieren {#step-2-subscribe-to-updates}

Fügen Sie als Nächstes den folgenden Code hinzu, um Content-Card-Updates von Braze zu abonnieren – typischerweise innerhalb der `Activity.onCreate()`-Methode Ihrer angepassten Content-Cards-Activity:

```java
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
mContentCardsUpdatedSubscriber = new IEventSubscriber<ContentCardsUpdatedEvent>() {
    @Override
    public void trigger(ContentCardsUpdatedEvent event) {
        // List of all Content Cards
        List<Card> allCards = event.getAllCards();

        // Your logic below
    }
};
Braze.getInstance(context).subscribeToContentCardsUpdates(mContentCardsUpdatedSubscriber);
Braze.getInstance(context).requestContentCardsRefresh();
```

### Schritt 3: Abonnement beenden {#step-3-unsubscribe}

Wir empfehlen außerdem, das Abonnement zu beenden, wenn Ihre angepasste Activity nicht mehr sichtbar ist. Fügen Sie den folgenden Code zur `onDestroy()`-Lifecycle-Methode Ihrer Activity hinzu:

```java
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
```

{% endsubtab %}
{% subtab Kotlin %}

### Schritt 1: Erstellen Sie eine private Abonnent-Variable

Um Card-Updates zu abonnieren, deklarieren Sie zunächst eine private Variable in Ihrer angepassten Klasse, die Ihren Abonnenten hält:

```kotlin
private var contentCardsUpdatedSubscriber: IEventSubscriber<ContentCardsUpdatedEvent>? = null
```

### Schritt 2: Updates abonnieren

Fügen Sie als Nächstes den folgenden Code hinzu, um Content-Card-Updates von Braze zu abonnieren – typischerweise innerhalb der `Activity.onCreate()`-Methode Ihrer angepassten Content-Cards-Activity:

```kotlin
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).removeSingleSubscription(contentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
contentCardsUpdatedSubscriber = IEventSubscriber { event ->
  // List of all Content Cards
  val allCards = event.allCards

  // Your logic below
}
Braze.getInstance(context).subscribeToContentCardsUpdates(contentCardsUpdatedSubscriber)
Braze.getInstance(context).requestContentCardsRefresh(true)
```

### Schritt 3: Abonnement beenden

Wir empfehlen außerdem, das Abonnement zu beenden, wenn Ihre angepasste Activity nicht mehr sichtbar ist. Fügen Sie den folgenden Code zur `onDestroy()`-Lifecycle-Methode Ihrer Activity hinzu:

```kotlin
Braze.getInstance(context).removeSingleSubscription(contentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}

Um auf das Content-Cards-Datenmodell zuzugreifen, rufen Sie [`contentCards.cards`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/cards) auf Ihrer `braze`-Instanz auf.

{% subtabs local %}
{% subtab Swift %}

```swift
let cards: [Braze.ContentCard] = AppDelegate.braze?.contentCards.cards
```

{% alert note %}
Das Lesen von `contentCards.cards`, `contentCards.unviewedCards` oder `contentCards.lastUpdate` blockiert den aufrufenden Thread, bis das SDK or Software-Development-Kit seine Post-Initialisierungsoperationen abgeschlossen hat. Verwenden Sie die nicht-blockierenden Getter unter [Nicht-blockierende Snapshot-Zugriffsmethoden](#non-blocking-snapshot-accessors) für Main-Thread- oder latenzempfindliche Kontexte.
{% endalert %}

Zusätzlich können Sie auch ein Abonnement aufrechterhalten, um Änderungen an Ihren Content Cards zu beobachten. Dies ist auf zwei Arten möglich:
1. Über ein Cancellable; oder
2. Über einen `AsyncStream`.

### Cancellable

```swift
// This subscription is maintained through a Braze cancellable, which will observe for changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.contentCards.subscribeToUpdates { [weak self] contentCards in
  // Implement your completion handler to respond to updates in `contentCards`.
}
```

### AsyncStream

```swift
let stream: AsyncStream<[Braze.ContentCard]> = AppDelegate.braze?.contentCards.cardsStream
```

### Nicht-blockierende Snapshot-Zugriffsmethoden {#non-blocking-snapshot-accessors}

Verwenden Sie diese Methoden, um den aktuellen gecachten Zustand zu lesen, ohne den aufrufenden Thread zu blockieren. Jeder Completion-Handler wird immer auf dem Main-Thread ausgeliefert.

```swift
// All cached cards.
AppDelegate.braze?.contentCards.getCachedContentCards { cards in
  // Use `cards` here.
}

// Unviewed cards only (excludes control cards).
AppDelegate.braze?.contentCards.getUnviewedCards { cards in
  // Use `cards` here.
}

// Date of the last server sync for the current user (nil until the first sync completes).
AppDelegate.braze?.contentCards.getLastUpdate { date in
  // Use `date` here.
}
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
NSArray<BRZContentCardRaw *> *contentCards = AppDelegate.braze.contentCards.cards;
```

Wenn Sie zusätzlich ein Abonnement für Ihre Content Cards aufrechterhalten möchten, können Sie [`subscribeToUpdates`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/subscribetoupdates(_:)) aufrufen:

```objc
// This subscription is maintained through Braze cancellable, which will continue to observe for changes until the subscription is cancelled.
BRZCancellable *cancellable = [self.braze.contentCards subscribeToUpdates:^(NSArray<BRZContentCardRaw *> *contentCards) {
  // Implement your completion handler to respond to updates in `contentCards`.
}];
```

Um den aktuellen gecachten Zustand zu lesen, ohne den aufrufenden Thread zu blockieren, verwenden Sie die folgenden Methoden. Jeder Completion-Handler wird auf dem Main-Thread ausgeliefert.

```objc
// All cached cards.
[AppDelegate.braze.contentCards getCachedContentCardsWithCompletion:^(NSArray<BRZContentCardRaw *> *cards) {
  // Use `cards` here.
}];

// Unviewed cards only (excludes control cards).
[AppDelegate.braze.contentCards getUnviewedCardsWithCompletion:^(NSArray<BRZContentCardRaw *> *cards) {
  // Use `cards` here.
}];

// Date of the last server sync for the current user (nil until the first sync completes).
[AppDelegate.braze.contentCards getLastUpdateWithCompletion:^(NSDate * _Nullable date) {
  // Use `date` here.
}];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab react native %}

Um auf Updates zu lauschen, abonnieren Sie Content-Card-Update or aktualisieren-Events:

```javascript
const subscription = Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, (update) => {
  const cards = update.cards;
  cards.forEach(card => {
    if (card.isControl) {
      // Do not display the control card, but remember to log an impression
    } else {
      // Use card.title, card.cardDescription, card.image, etc.
    }
  });
});
```

Um die zuletzt gecachten Content-Card-Daten abzurufen:

```javascript
import Braze from "@braze/react-native-sdk";

const cachedCards = await Braze.getCachedContentCards();
```

Um eine manuelle Aktualisierung der Content Cards von den Braze-Servern anzufordern:

```javascript
Braze.requestContentCardsRefresh();
```

{% endtab %}
{% endtabs %}

## Events protokollieren {#logging-events}

Das Protokollieren wertvoller Metriken wie Impressionen, Klicks und Schließungen ist schnell und einfach. Richten Sie einen angepassten Klick-Listener ein, um diese Analytics manuell zu verarbeiten.

{% tabs %}
{% tab web %}

Protokollieren Sie Impression-Events, wenn Cards von Nutzer:innen angesehen werden, mit [`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions):

```javascript
import * as braze from "@braze/web-sdk";

braze.logContentCardImpressions([card1, card2, card3]);
```

Protokollieren Sie Klick-Events, wenn Nutzer:innen mit einer Card interagieren, mit [`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick):

```javascript
import * as braze from "@braze/web-sdk";

braze.logContentCardClick(card);
```

{% endtab %}
{% tab android %}

Der [`BrazeManager`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt) kann auf Braze-SDK or Software-Development-Kit-Abhängigkeiten wie die Content-Card-Objekt-Array-Liste verweisen, um das [`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html)-Objekt abzurufen und die Braze-Protokollierungsmethoden aufzurufen. Verwenden Sie die `ContentCardable`-Basisklasse, um einfach auf Daten zu verweisen und sie dem `BrazeManager` bereitzustellen.

Um eine Impression oder einen Klick auf eine Card zu protokollieren, rufen Sie [`Card.logClick()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html) bzw. [`Card.logImpression()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html) auf.

Sie können eine Content-Card manuell protokollieren oder für eine bestimmte Card bei Braze als „geschlossen“ markieren, indem Sie [`isDismissed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/is-dismissed.html) verwenden. Wenn eine Card bereits als geschlossen markiert ist, kann sie nicht erneut als geschlossen markiert werden.

Um einen angepassten Klick-Listener zu erstellen, erstellen Sie eine Klasse, die [`IContentCardsActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/index.html) implementiert, und Registrierung or registrieren Sie sie beim [`BrazeContentCardsManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.managers/-braze-content-cards-manager/index.html). Implementieren Sie die Methode [`onContentCardClicked()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/on-content-card-clicked.html), die aufgerufen wird, wenn Nutzer:innen auf eine Content-Card klicken. Weisen Sie Braze dann an, Ihren Content-Card-Klick-Listener zu verwenden.

{% subtabs local %}
{% subtab Java %}

Zum Beispiel:

```java
BrazeContentCardsManager.getInstance().setContentCardsActionListener(new IContentCardsActionListener() {
  @Override
  public boolean onContentCardClicked(Context context, Card card, IAction cardAction) {
    return false;
  }

  @Override
  public void onContentCardDismissed(Context context, Card card) {

  }
});
```

{% endsubtab %}
{% subtab Kotlin %}

Zum Beispiel:

```kotlin
BrazeContentCardsManager.getInstance().contentCardsActionListener = object : IContentCardsActionListener {
  override fun onContentCardClicked(context: Context, card: Card, cardAction: IAction): Boolean {
    return false
  }

  override fun onContentCardDismissed(context: Context, card: Card) {

  }
}
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Um Kontrollvarianten-Content-Cards in Ihrer angepassten UI zu verarbeiten, übergeben Sie Ihr [`com.braze.models.cards.Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html)-Objekt und rufen Sie dann die Methode `logImpression` auf, wie Sie es bei jedem anderen Content-Card-Typ tun würden. Das Objekt protokolliert implizit eine Kontroll-Impression, um unsere Analytics darüber zu informieren, wann Nutzer:innen die Kontroll-Card gesehen hätten.{% endalert %}

{% endtab %}

{% tab swift %}

Implementieren Sie das Protokoll [`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate) und setzen Sie Ihr Delegate-Objekt als `delegate`-Eigenschaft Ihres `BrazeContentCardUI.ViewController`. Dieses Delegate übernimmt die Weitergabe der Daten Ihres angepassten Objekts an Braze zur Protokollierung. Ein Beispiel finden Sie im [Content Cards UI-Tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui/).

{% subtabs local %}
{% subtab Swift %}

```swift
// Set the delegate when creating the Content Cards controller
contentCardsController.delegate = delegate

// Method to implement in delegate
func contentCard(
    _ controller: BrazeContentCardUI.ViewController,
    shouldProcess clickAction: Braze.ContentCard.ClickAction,
    card: Braze.ContentCard
  ) -> Bool {
  // Intercept the content card click action here.
  return true
}
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
// Set the delegate when creating the Content Cards controller
contentCardsController.delegate = delegate;

// Method to implement in delegate
- (BOOL)contentCardController:(BRZContentCardUIViewController *)controller
                shouldProcess:(NSURL *)url
                         card:(BRZContentCardRaw *)card {
  // Intercept the content card click action here.
  return YES;
}
```
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Um Kontrollvarianten-Content-Cards in Ihrer angepassten UI zu verarbeiten, übergeben Sie Ihr [`Braze.ContentCard.Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control(_:))-Objekt und rufen Sie dann die Methode `logImpression` auf, wie Sie es bei jedem anderen Content-Card-Typ tun würden. Das Objekt protokolliert implizit eine Kontroll-Impression, um unsere Analytics darüber zu informieren, wann Nutzer:innen die Kontroll-Card gesehen hätten.
{% endalert %}
{% endtab %}

{% tab react native %}

Protokollieren Sie Impression-Events, wenn Cards von Nutzer:innen angesehen werden:

```javascript
Braze.logContentCardImpression(card.id);
```

Protokollieren Sie Klick-Events, wenn Nutzer:innen mit einer Card interagieren:

```javascript
Braze.logContentCardClicked(card.id);
```

Protokollieren Sie Schließungs-Events, wenn Nutzer:innen eine Card schließen:

```javascript
Braze.logContentCardDismissed(card.id);
```

{% endtab %}
{% endtabs %}

## Verhalten bei Klick-Aktionen {#handling-on-click-behavior}

{% tabs %}
{% tab web %}

Wenn Nutzer:innen in einem angepassten Feed auf eine Content-Card klicken, wird das Klick-Verhalten (z. B. Navigation zu einer URL, Deeplinking oder Protokollierung eines angepassten Events) nicht automatisch verarbeitet. Verwenden Sie [`handleBrazeAction`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#handlebrazeaction), um die URL der Card zu verarbeiten und die konfigurierte Klick-Aktion auszuführen, einschließlich Braze-Aktionen (`brazeActions://`-URLs).

```javascript
import * as braze from "@braze/web-sdk";

// In your card click handler
function onCardClick(card) {
  // Log the click
  braze.logContentCardClick(card);

  // Handle the on-click behavior
  if (card.url) {
    braze.handleBrazeAction(card.url);
  }
}
```

| Parameter | Beschreibung |
|---|---|
| `url` | Eine gültige URL oder eine gültige Braze-Aktions-URL mit dem Schema `brazeActions://`. |
| `openLinkInNewTab` | (Optional) Ob die URL in einem neuen Tab geöffnet werden soll. Standardmäßig `false`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Verhalten bei Klick-Aktionen" }

{% alert important %}
Wenn Sie `handleBrazeAction()` nicht aufrufen, werden im Braze-Dashboard konfigurierte Klick-Aktionen (z. B. „Angepasstes Event protokollieren“ oder „Zu URL navigieren“) für Cards in einem angepassten Feed nicht ausgeführt.
{% endalert %}

{% endtab %}
{% tab android %}

Das Klick-Verhalten wird von der Standard-Content-Cards-UI automatisch verarbeitet. Für angepasste Implementierungen verwenden Sie die Schnittstelle [`IContentCardsActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/index.html), die unter **Analytics protokollieren** beschrieben ist.

{% endtab %}
{% tab swift %}

Das Klick-Verhalten wird von der Standard-Content-Cards-UI automatisch verarbeitet. Für angepasste Implementierungen verwenden Sie das Protokoll [`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate), das unter **Analytics protokollieren** beschrieben ist.

{% endtab %}
{% tab React Native %}

Wenn Nutzer:innen in einem angepassten Feed auf eine Content-Card klicken, wird das Klick-Verhalten nicht automatisch verarbeitet. Nachdem Sie den Klick mit `Braze.logContentCardClicked(cardId)` protokolliert haben, rufen Sie `Braze.processContentCardClickAction(cardId)` auf, um Deeplinks, URLs und `brazeActions://`-Aktionen zu verarbeiten. Eine Methodenreferenz finden Sie unter [React Native Content Cards]({{site.baseurl}}/developer_guide/content_cards/?sdktab=react%20native).

```javascript
import Braze from "@braze/react-native-sdk";

function onCardPress(card) {
  Braze.logContentCardClicked(card.id);

  if (card.url) {
    Braze.processContentCardClickAction(card.id);
  }
}
```

{% alert important %}
Wenn Sie `processContentCardClickAction()` nicht aufrufen, werden im Braze-Dashboard konfigurierte Klick-Aktionen für Cards in einem angepassten Feed nicht ausgeführt.
{% endalert %}

{% endtab %}
{% endtabs %}