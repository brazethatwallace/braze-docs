## Voraussetzungen {#prerequisites}

Bevor Sie Content Cards verwenden können, müssen Sie das [Braze Swift SDK or Software-Development-Kit]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) in Ihre App integrieren. Es ist jedoch keine zusätzliche Einrichtung erforderlich.

## View-Controller-Kontexte {#view-controller-contexts}

Die standardmäßige Content-Cards-UI kann aus der Bibliothek `BrazeUI` des Braze SDK or Software-Development-Kit integriert werden. Erstellen Sie den Content-Cards-View-Controller unter Verwendung der `braze`-Instanz. Wenn Sie den Lifecycle der Content-Card-UI abfangen und darauf reagieren möchten, implementieren Sie [`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate) als Delegaten für Ihren `BrazeContentCardUI.ViewController`.

{% alert note %}
Weitere Informationen zu den Optionen für iOS-View-Controller finden Sie in der [Apple-Entwicklerdokumentation](https://developer.apple.com/documentation/uikit/view_controllers/showing_and_hiding_view_controllers).
{% endalert %}

Die Bibliothek `BrazeUI` des Swift SDK or Software-Development-Kit bietet zwei Standard-View-Controller-Kontexte: [Navigation](#swift_navigation) oder [Modal](#swift_modal). Das bedeutet, dass Sie Content Cards in diese Kontexte integrieren können, indem Sie ein paar Codezeilen zu Ihrer App oder Website hinzufügen. Beide Ansichten bieten Anpassungs- und Gestaltungsmöglichkeiten, wie in der [Anpassungsanleitung]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_styles/?tab=ios) beschrieben. Sie können auch einen angepassten Content-Card-View-Controller erstellen, anstatt den Standard-Controller von Braze zu verwenden, um noch mehr Anpassungsmöglichkeiten zu haben – ein Beispiel finden Sie im [Content Cards UI-Tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui/).

{% alert important %}
Um Content Cards als Kontrollvariante in Ihrer angepassten UI zu verarbeiten, übergeben Sie Ihr [`Braze.ContentCard.Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control(_:))-Objekt und rufen dann die Methode `logImpression` auf, wie Sie es mit jedem anderen Content-Card-Typ tun würden. Das Objekt protokolliert implizit eine Kontroll-Impression, um unsere Analytics darüber zu informieren, wann Nutzer:innen die Kontrollkarte gesehen hätten.
{% endalert %}

### Navigation {#swift_navigation}

Ein Navigationscontroller ist ein View-Controller, der mindestens einen untergeordneten View-Controller in einer Navigationsschnittstelle verwaltet. Hier ist ein Beispiel, wie Sie eine Instanz von `BrazeContentCardUI.ViewController` in einen Navigationscontroller pushen:

{% tabs %}
{% tab swift %}

```swift
func pushViewController() {
  guard let braze = AppDelegate.braze else { return }
  let contentCardsController = BrazeContentCardUI.ViewController(braze: braze)
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  contentCardsController.delegate = self
  self.navigationController?.pushViewController(contentCardsController, animated: true)
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)pushViewController {
  BRZContentCardUIViewController *contentCardsController = [[BRZContentCardUIViewController alloc] initWithBraze:self.braze];
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  [contentCardsController setDelegate:self];
  [self.navigationController pushViewController:contentCardsController animated:YES];
}
```

{% endtab %}
{% endtabs %}

### Modal {#swift_modal}

Verwenden Sie modale Präsentationen, um den Workflow Ihrer App vorübergehend zu unterbrechen, z. B. indem Sie Nutzer:innen zur Angabe wichtiger Informationen auffordern. Diese modale Ansicht verfügt über eine Navigationsleiste am oberen Rand und einen **Done**-Button an der Seite der Leiste. Hier ist ein Beispiel, wie Sie eine Instanz von `BrazeContentCard.ViewController` in einen modalen Controller pushen:

{% tabs %}
{% tab swift %}

```swift
func presentModalViewController() {
  guard let braze = AppDelegate.braze else { return }
  let contentCardsModal = BrazeContentCardUI.ModalViewController(braze: braze)
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  contentCardsModal.viewController.delegate = self
  self.navigationController?.present(contentCardsModal, animated: true, completion: nil)
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)presentModalViewController {
  BRZContentCardUIModalViewController *contentCardsModal = [[BRZContentCardUIModalViewController alloc] initWithBraze:AppDelegate.braze];
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  [contentCardsModal.viewController setDelegate:self];
  [self.navigationController presentViewController:contentCardsModal animated:YES completion:nil];
}
```

{% endtab %}
{% endtabs %}

Ein Beispiel für die Verwendung von `BrazeUI`-View-Controllern finden Sie in den entsprechenden Content Cards UI-Beispielen in unserer [Beispiel-App](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples).

## Basis-Kartenmodell {#base-card-model}

Das Content-Cards-Datenmodell ist im Modul `BrazeKit` des Braze Swift SDK or Software-Development-Kit verfügbar. Dieses Modul enthält die folgenden Content-Card-Typen, die eine Implementierung des Typs `Braze.ContentCard` sind. Eine vollständige Liste der Content-Card-Eigenschaften und ihrer Verwendung finden Sie unter [`ContentCard`-Klasse](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard).

- Nur Bild
- Bild mit Bildunterschrift
- Klassisch
- Klassisches Bild
- Kontrollgruppe

Um auf das Content-Cards-Datenmodell zuzugreifen, rufen Sie `contentCards.cards` in Ihrer `braze`-Instanz auf. Weitere Informationen zum Abonnieren von Kartendaten finden Sie unter [Analytics protokollieren]({{site.baseurl}}/developer_guide/content_cards/logging_analytics).

{% alert note %}
Das Lesen von `contentCards.cards`, `contentCards.unviewedCards` oder `contentCards.lastUpdate` blockiert den aufrufenden Thread, bis das SDK or Software-Development-Kit seine Post-Initialisierungsoperationen abgeschlossen hat. Für Main-Thread- oder latenzempfindliche Kontexte verwenden Sie stattdessen die nicht-blockierenden Alternativen [`getCachedContentCards(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/getcachedcontentcards(_:)), [`getUnviewedCards(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/getunviewedcards(_:)) oder [`getLastUpdate(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/getlastupdate(_:)).
{% endalert %}

{% alert note %}
Beachten Sie, dass `BrazeKit` eine alternative [`ContentCardRaw`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcardraw)-Klasse für Objective-C-Kompatibilität bietet.
{% endalert %}

## Karten-Methoden {#card-methods}

Jede Karte wird mit einem `Context`-Objekt initialisiert, das verschiedene Methoden zur Verwaltung des Kartenstatus enthält. Rufen Sie diese Methoden auf, wenn Sie die entsprechende Statuseigenschaft für ein bestimmtes Kartenobjekt ändern möchten.

| Methode | Beschreibung |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `card.context?.logImpression()` | Protokolliert das Content-Card-Impression-Ereignis. |
| `card.context?.logClick()` | Protokolliert das Content-Card-Klick-Ereignis. |
| `card.context?.processClickAction()` | Verarbeitet eine gegebene [`ClickAction`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/clickaction)-Eingabe. |
| `card.context?.logDismissed()` | Protokolliert das Ereignis „Content-Card ausgeblendet“. |
| `card.context?.logError()` | Protokolliert einen Fehler im Zusammenhang mit der Content-Card. |
| `card.context?.loadImage()` | Lädt ein bestimmtes Content-Card-Bild von einer URL. Diese Methode kann nil sein, wenn die Content-Card kein Bild enthält. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Karten-Methoden" }

Weitere Einzelheiten finden Sie in der [Dokumentation zur `Context`-Klasse](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcardraw/context-swift.class).