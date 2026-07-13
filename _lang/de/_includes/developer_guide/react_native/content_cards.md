## Über React Native Content Cards {#about-react-native-content-cards}

Die Braze SDKs enthalten einen Standard-Kartenfeed, der Ihnen den Einstieg in die Arbeit mit Content Cards erleichtert. Sie können den Kartenfeed mit der Methode `Braze.launchContentCards()` anzeigen. Der im Braze SDK enthaltene Standard-Kartenfeed verarbeitet das gesamte Analytics-Tracking, Ausblendungen und die Darstellung der Content Cards für Nutzer:innen.

{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Kartenmethoden {#cards-methods}

Um Ihre eigene UI zu erstellen, können Sie eine Liste der verfügbaren Karten abrufen und auf Aktualisierungen der Karten warten:

```javascript
// Set initial cards
const [cards, setCards] = useState([]);

// Listen for updates as a result of card refreshes, such as:
// a new session, a manual refresh with `requestContentCardsRefresh()`, or after the timeout period
Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, async (update) => {
    setCards(update.cards);
});

// Manually trigger a refresh of cards
Braze.requestContentCardsRefresh();
```

{% alert important %}
Wenn Sie Ihre eigene UI zur Anzeige von Karten erstellen möchten, müssen Sie `logContentCardImpression` aufrufen, um Analytics für diese Karten zu erhalten. Dies gilt auch für Karten des Typs `control`, die nachverfolgt werden müssen, auch wenn sie Nutzer:innen nicht angezeigt werden.
{% endalert %}

Mit diesen zusätzlichen Methoden können Sie einen angepassten Content-Card-Feed in Ihrer App erstellen:

| Methode                                  | Beschreibung                                                                                           |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `launchContentCards()`                   | Startet das Content-Card-UI-Element.                                                                   |
| `requestContentCardsRefresh()`           | Fordert die neuesten Content Cards vom Braze-SDK-Server an. Die resultierende Kartenliste wird an jeden der zuvor registrierten [Content-Card-Event-Listener](#reactnative_cards-methods) weitergegeben. |
| `getContentCards()`                      | Ruft Content Cards aus dem Braze SDK ab. Gibt ein Promise zurück, das mit der neuesten Kartenliste vom Server aufgelöst wird. |
| `getCachedContentCards()`                | Gibt das aktuellste Content-Card-Array aus dem Cache zurück.                                           |
| `logContentCardClicked(cardId)`          | Protokolliert einen Klick für die angegebene Content-Card-ID. Diese Methode wird nur zu Analytics-Zwecken verwendet. Rufen Sie zum Ausführen der Klick-Aktion zusätzlich `processContentCardClickAction(cardId)` auf. |
| `logContentCardImpression(cardId)`       | Protokolliert eine Impression für die angegebene Content-Card-ID.                                      |
| `logContentCardDismissed(cardId)`        | Protokolliert eine Ausblendung für die angegebene Content-Card-ID.                                     |
| `processContentCardClickAction(cardId)`  | Führt die Aktion einer bestimmten Karte aus.                                                           |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Kartenmethoden" }

## Kartentypen und Eigenschaften {#card-types-and-properties}

Das Content-Card-Datenmodell ist im React Native SDK verfügbar und bietet die folgenden Content-Card-Kartentypen: [Nur Bild](#image-only), [Bildunterschrift](#captioned-image) und [Klassisch](#classic). Es gibt auch einen speziellen Kartentyp [Kontrollgruppe](#control), der an Nutzer:innen zurückgegeben wird, die sich in der Kontrollgruppe für eine bestimmte Karte befinden. Jeder Typ erbt gemeinsame Eigenschaften von einem Basismodell zusätzlich zu seinen eigenen spezifischen Eigenschaften.

{% alert tip %}
Eine vollständige Referenz des Content-Card-Datenmodells finden Sie in der [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html)- und der [iOS-Dokumentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard).
{% endalert %}

### Basis-Kartenmodell {#base-card-model}

Das Basis-Kartenmodell bietet grundlegende Verhaltensweisen für alle Karten.

| Eigenschaft    | Beschreibung                                                                                                           |
|--------------|------------------------------------------------------------------------------------------------------------------------|
| `id`          | Die von Braze festgelegte ID der Karte.                                                                               |
| `created`     | Der Unix-Zeitstempel der Erstellungszeit der Karte von Braze.                                                          |
| `expiresAt`   | Der Unix-Zeitstempel des Ablaufzeitpunkts der Karte. Wenn der Wert kleiner als 0 ist, bedeutet dies, dass die Karte nie abläuft. |
| `viewed`      | Ob die Karte von Nutzer:innen gelesen oder ungelesen ist. Damit werden keine Analytics protokolliert.                  |
| `clicked`     | Ob die Karte von Nutzer:innen angeklickt wurde.                                                                       |
| `pinned`      | Ob die Karte angeheftet ist.                                                                                           |
| `dismissed`   | Ob Nutzer:innen diese Karte ausgeblendet haben. Eine bereits ausgeblendete Karte erneut als ausgeblendet zu markieren, hat keine Auswirkung. |
| `dismissible` | Ob die Karte von Nutzer:innen ausgeblendet werden kann.                                                               |
| `url`         | (Optional) Der URL-String, der mit der Klick-Aktion der Karte verknüpft ist.                                          |
| `openURLInWebView` | Ob URLs für diese Karte in der Braze WebView geöffnet werden sollen oder nicht.                                   |
| `isControl`   | Ob diese Karte eine Kontrollkarte ist. Kontrollkarten sollten Nutzer:innen nicht angezeigt werden.                     |
| `extras`      | Die Map der Key-Value-Extras für diese Karte.                                                                          |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Basis-Kartenmodell" }

Eine vollständige Referenz der Basiskarte finden Sie in der [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html)- und [iOS-Dokumentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct).

### Nur Bild {#image-only}

Nur-Bild-Karten sind anklickbare Bilder in voller Größe.

| Eigenschaft         | Beschreibung                                                                                                      |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| `type`             | Der Content-Card-Typ, `IMAGE_ONLY`.                                                                              |
| `image`            | Die URL des Kartenbilds.                                                                                          |
| `imageAspectRatio` | Das Seitenverhältnis des Kartenbilds. Es dient als Hinweis, bevor das Laden des Bilds abgeschlossen ist. Beachten Sie, dass diese Eigenschaft unter bestimmten Umständen nicht bereitgestellt werden kann. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nur Bild" }

Eine vollständige Referenz zu Karten des Typs „Nur Bild“ finden Sie in der [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html)- bzw. [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/imageonly-swift.struct)-Dokumentation.

### Bildunterschrift {#captioned-image}

Bildunterschriftenkarten sind anklickbare Bilder in voller Größe mit begleitendem beschreibendem Text.

| Eigenschaft         | Beschreibung                                                                                                      |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| `type`             | Der Content-Card-Typ, `CAPTIONED`.                                                                               |
| `image`            | Die URL des Kartenbilds.                                                                                          |
| `imageAspectRatio` | Das Seitenverhältnis des Kartenbilds. Es dient als Hinweis, bevor das Laden des Bilds abgeschlossen ist. Beachten Sie, dass diese Eigenschaft unter bestimmten Umständen nicht bereitgestellt werden kann. |
| `title`            | Der Titeltext für die Karte.                                                                                      |
| `cardDescription`  | Der Beschreibungstext für die Karte.                                                                              |
| `domain`           | (Optional) Der Linktext für die Eigenschafts-URL, zum Beispiel `"braze.com/resources/"`. Er kann auf der UI der Karte angezeigt werden, um die Aktion/Richtung beim Anklicken der Karte anzugeben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Bildunterschrift" }

Eine vollständige Referenz zu Karten des Typs „Bildunterschrift“ finden Sie in der [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html)- bzw. [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/captionedimage-swift.struct)-Dokumentation.

### Klassisch {#classic}

Klassische Karten haben einen Titel, eine Beschreibung und ein optionales Bild vor dem Text.

| Eigenschaft         | Beschreibung                                                                                                      |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| `type`             | Der Content-Card-Typ, `CLASSIC`.                                                                                  |
| `image`            | (Optional) Die URL des Kartenbilds.                                                                               |
| `title`            | Der Titeltext für die Karte.                                                                                      |
| `cardDescription`  | Der Beschreibungstext für die Karte.                                                                              |
| `domain`           | (Optional) Der Linktext für die Eigenschafts-URL, zum Beispiel `"braze.com/resources/"`. Er kann auf der UI der Karte angezeigt werden, um die Aktion/Richtung beim Anklicken der Karte anzugeben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Klassisch" }

Eine vollständige Referenz der klassischen Content-Card (Textankündigung) finden Sie in der Dokumentation für [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) und [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classic-swift.struct). Die klassische Bildkarte (Kurznachrichten) finden Sie in der Dokumentation für [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html) und [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classicimage-swift.struct).

### Kontrollgruppe {#control}

Kontrollkarten enthalten alle Basiseigenschaften, mit einigen wichtigen Unterschieden. Das Wichtigste:

- Die Eigenschaft `isControl` ist garantiert `true`.
- Die Eigenschaft `extras` ist garantiert leer.

Eine vollständige Referenz der Kontrollkarte finden Sie in der [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-control-card/index.html)- bzw. [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control-swift.struct)-Dokumentation.