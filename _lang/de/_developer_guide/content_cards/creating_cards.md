---
nav_title: Karten erstellen
article_title: Content Cards erstellen
page_order: 0
description: "Dieser Artikel behandelt die Komponenten zur Erstellung einer angepassten Content-Card-UI."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Content Cards erstellen {#create-content-cards}

> Dieser Artikel beschreibt den grundlegenden Ansatz, den Sie bei der Implementierung angepasster Content Cards verwenden, sowie drei häufige Anwendungsfälle. Es wird davon ausgegangen, dass Sie bereits die anderen Artikel der Anleitung zur Anpassung von Content Cards gelesen haben, um zu verstehen, was standardmäßig möglich ist und was angepassten Code erfordert. Es ist besonders hilfreich zu verstehen, wie Sie [Analytics protokollieren]({{site.baseurl}}/developer_guide/content_cards/logging_analytics) für Ihre angepassten Content Cards.

{% multi_lang_include banners/content_card_alert.md %}

## Eine Card erstellen {#creating-a-card}

### Schritt 1: Eine benutzerdefinierte UI erstellen {#step-1-create-a-custom-ui}

{% tabs local %}
{% tab web %}

Erstellen Sie zunächst Ihre benutzerdefinierte HTML-Komponente, die zum Rendern der Cards verwendet wird.

{% endtab %}
{% tab android %}

Erstellen Sie zunächst Ihr eigenes benutzerdefiniertes Fragment. Das Standard-[`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) ist nur für die Verarbeitung unserer Standard-Content-Card-Typen konzipiert, bietet aber einen guten Ausgangspunkt.

{% endtab %}
{% tab swift %}

Erstellen Sie zunächst Ihre eigene benutzerdefinierte View-Controller-Komponente. Der Standard-[`BrazeContentCardUI.ViewController`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller) ist nur für die Verarbeitung unserer Standard-Content-Card-Typen konzipiert, bietet aber einen guten Ausgangspunkt.

{% endtab %}
{% endtabs %}

### Schritt 2: Card-Aktualisierungen abonnieren {#step-2-subscribe-to-card-updates}

Registrierung Sie eine Callback-Funktion, um Datenaktualisierungen zu abonnieren, wenn Cards aktualisiert werden. Sie können die Content-Card-Objekte parsen und deren Payload-Daten wie `title`, `cardDescription` und `imageUrl` extrahieren und dann die resultierenden Modelldaten verwenden, um Ihre benutzerdefinierte UI zu befüllen.

Um die Content-Card-Datenmodelle zu erhalten, abonnieren Sie Content-Card-Aktualisierungen. Achten Sie besonders auf die folgenden Eigenschaften:

* **`id`:** Repräsentiert den Content-Card-ID-String. Dies ist der eindeutige Bezeichner, der zum Protokollieren von Analytics aus benutzerdefinierten Content Cards verwendet wird.
* **`extras`:** Umfasst alle Schlüssel-Wert-Paare aus dem Braze-Dashboard.

Alle Eigenschaften außer `id` und `extras` sind für benutzerdefinierte Content Cards optional zu parsen. Weitere Informationen zum Datenmodell finden Sie in den Integrationsartikeln der jeweiligen Plattform: [Android]({{site.baseurl}}/developer_guide/content_cards?sdktab=android), [iOS]({{site.baseurl}}/developer_guide/content_cards?sdktab=swift), [Web]({{site.baseurl}}/developer_guide/content_cards?sdktab=web).

{% tabs local %}
{% tab web %}

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
Content Cards werden nur beim Sitzungsstart aktualisiert, wenn `subscribeToContentCardsUpdates()` vor `openSession()` aufgerufen wird. Sie können den Feed auch jederzeit [manuell aktualisieren]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed).
{% endalert %}

{% endtab %}
{% tab android %}
{% subtabs local %}
{% subtab Java %}

#### Schritt 2a: Eine private Abonnent-Variable erstellen {#step-2a-create-a-private-subscriber-variable}

Um Card-Aktualisierungen zu abonnieren, deklarieren Sie zunächst eine private Variable in Ihrer benutzerdefinierten Klasse, um Ihren Abonnenten zu halten:

```java
// subscriber variable
private IEventSubscriber<ContentCardsUpdatedEvent> mContentCardsUpdatedSubscriber;
```

#### Schritt 2b: Aktualisierungen abonnieren {#step-2b-subscribe-to-updates}

Fügen Sie den folgenden Code hinzu, um Content-Card-Aktualisierungen von Braze zu abonnieren, typischerweise innerhalb der `Activity.onCreate()` Ihrer benutzerdefinierten Content-Cards-Aktivität:

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

#### Schritt 2c: Abonnement beenden {#step-2c-unsubscribe}

Beenden Sie das Abonnement, wenn Ihre benutzerdefinierte Aktivität aus dem Sichtfeld verschwindet. Fügen Sie den folgenden Code in die `onDestroy()`-Lebenszyklusmethode Ihrer Aktivität ein:

```java
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
```

{% endsubtab %}
{% subtab Kotlin %}

#### Schritt 2a: Eine private Abonnent-Variable erstellen

Um Card-Aktualisierungen zu abonnieren, deklarieren Sie zunächst eine private Variable in Ihrer benutzerdefinierten Klasse, um Ihren Abonnenten zu halten:

```kotlin
private var contentCardsUpdatedSubscriber: IEventSubscriber<ContentCardsUpdatedEvent>? = null
```

#### Schritt 2b: Aktualisierungen abonnieren

Fügen Sie den folgenden Code hinzu, um Content-Card-Aktualisierungen von Braze zu abonnieren, typischerweise innerhalb der `Activity.onCreate()` Ihrer benutzerdefinierten Content-Cards-Aktivität:

```kotlin
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).subscribeToContentCardsUpdates(contentCardsUpdatedSubscriber)
Braze.getInstance(context).requestContentCardsRefresh()
  // List of all Content Cards
  val allCards = event.allCards

  // Your logic below
}
Braze.getInstance(context).subscribeToContentCardsUpdates(mContentCardsUpdatedSubscriber)
Braze.getInstance(context).requestContentCardsRefresh(true)
```

#### Schritt 2c: Abonnement beenden

Beenden Sie das Abonnement, wenn Ihre benutzerdefinierte Aktivität aus dem Sichtfeld verschwindet. Fügen Sie den folgenden Code in die `onDestroy()`-Lebenszyklusmethode Ihrer Aktivität ein:

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

Zusätzlich können Sie ein Abonnement aufrechterhalten, um Änderungen an Ihren Content Cards zu beobachten. Dies ist auf zwei Arten möglich:
1. Durch Aufrechterhaltung eines Cancellable; oder
2. Durch Aufrechterhaltung eines `AsyncStream`.

##### Cancellable {#cancellable}

```swift
// This subscription is maintained through a Braze cancellable, which will observe for changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.contentCards.subscribeToUpdates { [weak self] contentCards in
  // Implement your completion handler to respond to updates in `contentCards`.
}
```

##### AsyncStream

```swift
let stream: AsyncStream<[Braze.ContentCard]> = AppDelegate.braze?.contentCards.cardsStream
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
NSArray<BRZContentCardRaw *> *contentCards = AppDelegate.braze.contentCards.cards;
```

Wenn Sie außerdem ein Abonnement für Ihre Content Cards aufrechterhalten möchten, können Sie [`subscribeToUpdates`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/subscribetoupdates(_:)) aufrufen:

```objc
// This subscription is maintained through Braze cancellable, which will continue to observe for changes until the subscription is cancelled.
BRZCancellable *cancellable = [self.braze.contentCards subscribeToUpdates:^(NSArray<BRZContentCardRaw *> *contentCards) {
  // Implement your completion handler to respond to updates in `contentCards`.
}];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}


### Schritt 3: Analytics implementieren {#step-3-implement-analytics}

Content-Card-Impressionen, Klicks und Abweisungen werden in Ihrer benutzerdefinierten Ansicht nicht automatisch protokolliert. Sie müssen [jede entsprechende Methode implementieren]({{site.baseurl}}/developer_guide/content_cards/logging_analytics), um alle Metriken ordnungsgemäß an die Braze-Dashboard-Analytics zurückzumelden.

### Schritt 4: Ihre Card testen (optional) {#step-4-test-your-card-optional}

So testen Sie Ihre Content Card:

1. Legen Sie eine:n aktive:n Nutzer:in in Ihrer Anwendung fest, indem Sie die [`changeUser()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)-Methode aufrufen.
2. Gehen Sie in Braze zu **Campaigns** und [erstellen Sie eine neue Content-Card-Campaign]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card).
3. Wählen Sie in Ihrer Campaign **Test** aus und geben Sie dann die `user-id` der Testnutzer:in ein. Wenn Sie bereit sind, wählen Sie **Send Test**. Sie können in Kürze eine Content Card auf Ihrem Gerät starten.

![Eine Braze Content-Card-Campaign, die zeigt, dass Sie Ihre eigene Nutzer-ID als Testempfänger:in hinzufügen können, um Ihre Content Card zu testen.]({% image_buster /assets/img/react-native/content-card-test.png %} "Content Card Campaign Test")

## Content-Card-Platzierungen {#content-card-placements}

Content Cards können auf viele verschiedene Arten eingesetzt werden. Drei gängige Implementierungen sind die Verwendung als Nachrichtenzentrale, als dynamische Bildanzeige oder als Bildkarussell. Für jede dieser Platzierungen weisen Sie Ihren Content Cards [Schlüssel-Wert-Paare]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/behavior) (die `extras`-Eigenschaft im Datenmodell) zu und passen basierend auf den Werten das Verhalten, das Erscheinungsbild oder die Funktionalität der Card zur Laufzeit dynamisch an.

![Diagramm mit drei Beispielen für Content-Card-Platzierungen: Nachrichtenposteingang, dynamische Bildanzeige und Bildkarussell.]({% image_buster /assets/img_archive/cc_placements.png %}){: style="border:0px;"}

### Nachrichtenposteingang {#message-inbox}

Content Cards können verwendet werden, um eine Nachrichtenzentrale zu simulieren. In diesem Format ist jede Nachricht eine eigene Card, die [Schlüssel-Wert-Paare]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/behavior) enthält, welche Klick-Ereignisse steuern. Diese Schlüssel-Wert-Paare sind die zentralen Bezeichner, anhand derer die App entscheidet, wohin navigiert werden soll, wenn Nutzer:innen auf eine Posteingangs-Nachricht klicken. Die Werte der Schlüssel-Wert-Paare sind beliebig wählbar.

#### Beispiel {#example}

Beispielsweise möchten Sie möglicherweise zwei Nachrichten-Cards erstellen: einen Handlungsaufruf, damit Nutzer:innen Leseempfehlungen aktivieren, und einen Gutscheincode für Ihr Segment neuer Abonnent:innen.

Schlüssel wie `body`, `title` und `buttonText` können einfache String-Werte haben, die Ihre Marketer festlegen können. Schlüssel wie `terms` können Werte enthalten, die eine kleine Sammlung von Formulierungen bereitstellen, die von Ihrer Rechtsabteilung genehmigt wurden. Schlüssel wie `style` und `class_type` haben String-Werte, die Sie festlegen können, um zu bestimmen, wie Ihre Card in Ihrer App oder auf Ihrer Website dargestellt wird.

{% tabs local %}
{% tab Leseempfehlungen %}
Schlüssel-Wert-Paare für die Leseempfehlungs-Card:

| Schlüssel   | Wert                                                                 |
|------------|----------------------------------------------------------------------|
| `body`       | Fügen Sie Ihre Interessen Ihrem Politer-Weekly-Profil hinzu, um persönliche Leseempfehlungen zu erhalten. |
| `style`      | info                                                                 |
| `class_type` | notification_center                                                 |
| `card_priority` | 1                                                                 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Beispiel" }
{% endtab %}

{% tab Gutschein für neue Abonnent:innen %}
Schlüssel-Wert-Paare für einen Gutschein für neue Abonnent:innen:

| Schlüssel   | Wert                                                             |
|------------|------------------------------------------------------------------|
| `title`      | Abonnieren Sie für unbegrenzte Spiele                            |
| `body`       | Sommer-Spezial – Genießen Sie 10 % Rabatt auf Politer-Spiele    |
| `buttonText` | Jetzt abonnieren                                                 |
| `style`      | promo                                                            |
| `class_type` | notification_center                                              |
| `card_priority` | 2                                                              |
| `terms`      | new_subscribers_only                                             |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Beispiel" }
{% endtab %}
{% endtabs %}

{% details Zusätzliche Informationen für Android %}

Im Android- und FireOS-SDK wird die Nachrichtenzentrale-Logik durch den `class_type`-Wert gesteuert, der von den Schlüssel-Wert-Paaren aus Braze bereitgestellt wird. Mit der Methode [`createContentCardable`]({{site.baseurl}}/developer_guide/content_cards) können Sie diese Klassentypen filtern und identifizieren.

{% tabs local %}
{% tab Kotlin %}
**Verwendung von `class_type` für das Klick-Verhalten**<br>
Wenn wir die Content-Card-Daten in unsere benutzerdefinierten Klassen übertragen, verwenden wir die `ContentCardClass`-Eigenschaft der Daten, um zu bestimmen, welche konkrete Unterklasse zum Speichern der Daten verwendet werden soll.

```kotlin
 private fun createContentCardable(metadata: Map<String, Any>, type: ContentCardClass?): ContentCardable?{
        return when(type){
            ContentCardClass.AD -> Ad(metadata)
            ContentCardClass.MESSAGE_WEB_VIEW -> WebViewMessage(metadata)
            ContentCardClass.NOTIFICATION_CENTER -> FullPageMessage(metadata)
            ContentCardClass.ITEM_GROUP -> Group(metadata)
            ContentCardClass.ITEM_TILE -> Tile(metadata)
            ContentCardClass.COUPON -> Coupon(metadata)
            else -> null
        }
    }
```

Wenn wir dann die Nutzer:innen-Interaktion mit der Nachrichtenliste verarbeiten, können wir den Typ der Nachricht verwenden, um zu bestimmen, welche Ansicht den Nutzer:innen angezeigt werden soll.

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        //...
        listView.onItemClickListener = AdapterView.OnItemClickListener { parent, view, position, id ->
           when (val card = dataProvider[position]){
                is WebViewMessage -> {
                    val intent = Intent(this, WebViewActivity::class.java)
                    val bundle = Bundle()
                    bundle.putString(WebViewActivity.INTENT_PAYLOAD, card.contentString)
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
                is FullPageMessage -> {
                    val intent = Intent(this, FullPageContentCard::class.java)
                    val bundle = Bundle()
                    bundle.putString(FullPageContentCard.CONTENT_CARD_IMAGE, card.icon)
                    bundle.putString(FullPageContentCard.CONTENT_CARD_TITLE, card.messageTitle)
                    bundle.putString(FullPageContentCard.CONTENT_CARD_DESCRIPTION, card.cardDescription)
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
            }

        }
    }
```
{% endtab %}
{% tab Java %}
**Verwendung von `class_type` für das Klick-Verhalten**<br>
Wenn wir die Content-Card-Daten in unsere benutzerdefinierten Klassen übertragen, verwenden wir die `ContentCardClass`-Eigenschaft der Daten, um zu bestimmen, welche konkrete Unterklasse zum Speichern der Daten verwendet werden soll.

```java
private ContentCardable createContentCardable(Map<String, ?> metadata,  ContentCardClass type){
    switch(type){
        case ContentCardClass.AD:{
            return new Ad(metadata);
        }
        case ContentCardClass.MESSAGE_WEB_VIEW:{
            return new WebViewMessage(metadata);
        }
        case ContentCardClass.NOTIFICATION_CENTER:{
            return new FullPageMessage(metadata);
        }
        case ContentCardClass.ITEM_GROUP:{
            return new Group(metadata);
        }
        case ContentCardClass.ITEM_TILE:{
            return new Tile(metadata);
        }
        case ContentCardClass.COUPON:{
            return new Coupon(metadata);
        }
        default:{
            return null;
        }
    }
}

```

Wenn wir dann die Nutzer:innen-Interaktion mit der Nachrichtenliste verarbeiten, können wir den Typ der Nachricht verwenden, um zu bestimmen, welche Ansicht den Nutzer:innen angezeigt werden soll.

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState)
        //...
        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id){
               ContentCardable card = dataProvider.get(position);
               if (card instanceof WebViewMessage){
                    Bundle intent = new Intent(this, WebViewActivity.class);
                    Bundle bundle = new Bundle();
                    bundle.putString(WebViewActivity.INTENT_PAYLOAD, card.getContentString());
                    intent.putExtras(bundle);
                    startActivity(intent);
                }
                else if (card instanceof FullPageMessage){
                    Intent intent = new Intent(this, FullPageContentCard.class);
                    Bundle bundle = Bundle();
                    bundle.putString(FullPageContentCard.CONTENT_CARD_IMAGE, card.getIcon());
                    bundle.putString(FullPageContentCard.CONTENT_CARD_TITLE, card.getMessageTitle());
                    bundle.putString(FullPageContentCard.CONTENT_CARD_DESCRIPTION, card.getCardDescription());
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
            }

        });
    }
```

{% endtab %}
{% endtabs %}
{% enddetails %}

### Karussell {#carousel}

Sie können Content Cards in Ihrem vollständig angepassten Karussell-Feed einrichten und Nutzer:innen so ermöglichen, durch weitere hervorgehobene Cards zu wischen und sie anzuzeigen. Standardmäßig werden Content Cards nach Erstellungsdatum sortiert (neueste zuerst), und Ihre Nutzer:innen sehen alle Cards, für die sie berechtigt sind.

So implementieren Sie ein Content-Card-Karussell:

1. Erstellen Sie benutzerdefinierte Logik, die [Änderungen an Ihren Content Cards]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed) beobachtet und den Eingang von Content Cards verarbeitet.
2. Erstellen Sie benutzerdefinierte clientseitige Logik, um eine bestimmte Anzahl von Cards gleichzeitig im Karussell anzuzeigen. Beispielsweise könnten Sie die ersten fünf Content-Card-Objekte aus dem Array auswählen oder Schlüssel-Wert-Paare einführen, um bedingte Logik aufzubauen.

{% alert tip %}
Wenn Sie ein Karussell als sekundären Content-Cards-Feed implementieren, stellen Sie sicher, dass Sie [Cards mithilfe von Schlüssel-Wert-Paaren dem richtigen Feed zuordnen]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed).
{% endalert %}

### Nur Bild {#image-only}

Content Cards müssen nicht wie „Cards“ aussehen. Beispielsweise können Content Cards als dynamisches Bild erscheinen, das dauerhaft auf Ihrer Startseite oder am oberen Rand bestimmter Seiten angezeigt wird.

Um dies zu erreichen, erstellen Ihre Marketer eine Campaign oder einen Canvas-Schritt mit dem Content-Card-Typ **Nur Bild**. Legen Sie dann Schlüssel-Wert-Paare fest, die für die Verwendung von [Content Cards als ergänzende Inhalte]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/behavior) geeignet sind.