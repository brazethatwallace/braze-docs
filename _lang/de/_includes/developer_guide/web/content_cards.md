{% multi_lang_include archive/web-v4-rename.md %}

## Voraussetzungen {#prerequisites}

Bevor Sie Content Cards verwenden können, müssen Sie das [Braze Web SDK integrieren]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web). Es ist keine zusätzliche Einrichtung erforderlich. Wenn Sie stattdessen eine eigene UI erstellen möchten, lesen Sie den [Leitfaden zur Anpassung von Content Cards]({{site.baseurl}}/developer_guide/content_cards).

{% alert note %}
Einige Werbeblocker und Browser-Datenschutzerweiterungen können das Braze Web SDK-Skript oder zugehörige Netzwerkanfragen blockieren, was dazu führen kann, dass Content Cards nicht geladen werden. Wenn Sie die CDN-Integrationsmethode verwenden, sollten Sie zur [NPM-Integrationsmethode]({{site.baseurl}}/developer_guide/sdk_integration/?subtab=package%20manager&sdktab=web) wechseln, die SDK-Bibliotheken lokal auf Ihrer Website speichert und einige Probleme im Zusammenhang mit Werbeblockern vermeiden kann.
{% endalert %}

## Standard-Feed-UI

Um die enthaltene Content-Cards-UI zu verwenden, müssen Sie angeben, wo der Feed auf Ihrer Website angezeigt werden soll.

In diesem Beispiel haben wir ein `<div id="feed"></div>`, in das wir den Content-Cards-Feed platzieren möchten. Wir verwenden drei Buttons, um den Feed auszublenden, anzuzeigen oder umzuschalten (basierend auf seinem aktuellen Status aus- oder einblenden).

```html

<button id="toggle" type="button">Toggle Cards Feed</button>
<button id="hide" type="button">Hide Cards Feed</button>
<button id="show" type="button">Show Cards Feed</button>

<nav>
    <h1>Your Personalized Feed</h1>
    <div id="feed"></div>
</nav>

<script>
   const toggle = document.getElementById("toggle");
   const hide = document.getElementById("hide");
   const show = document.getElementById("show");
   const feed = document.getElementById("feed");

   toggle.onclick = function(){
      braze.toggleContentCards(feed);
   }

   hide.onclick = function(){
      braze.hideContentCards();
   }

   show.onclick = function(){
      braze.showContentCards(feed);
   }
</script>
```

Wenn Sie die Methoden `toggleContentCards(parentNode, filterFunction)` und `showContentCards(parentNode, filterFunction)` verwenden und keine Argumente übergeben werden, werden alle Content Cards in einer fixierten Seitenleiste auf der Seite angezeigt. Andernfalls wird der Feed in der angegebenen `parentNode`-Option platziert.

| Parameter | Beschreibung |
|---|---|
| `parentNode` | Der HTML-Knoten, in dem die Content Cards gerendert werden. Wenn der übergeordnete Knoten bereits eine Braze-Content-Cards-Ansicht als direktes Unterelement hat, werden die vorhandenen Content Cards ersetzt. Sie sollten zum Beispiel `document.querySelector(".my-container")` übergeben. |
| `filterFunction` | Eine Filter- oder Sortierfunktion für die in dieser Ansicht angezeigten Cards. Wird mit dem Array von `Card`-Objekten aufgerufen, sortiert nach `{pinned, date}`. Es wird erwartet, dass ein Array sortierter `Card`-Objekte zurückgegeben wird, die für diese:n Nutzer:in gerendert werden sollen. Wenn weggelassen, werden alle Cards angezeigt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Standard-Feed-UI" }

[Weitere Informationen finden Sie in der SDK-Referenzdokumentation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards) zum Umschalten von Content Cards.

## Content Cards im Web testen {#testing-content-cards-on-the-web}

Sie können Ihre Content-Cards-Integration mithilfe der Entwickler:innen-Tools Ihres Browsers testen.

1. Erstellen Sie eine Content-Card-Campaign und richten Sie sie auf Ihre:n Testnutzer:in aus.
2. Melden Sie sich auf der Website an, auf der Ihre Web-SDK-Integration eingerichtet ist.
3. Öffnen Sie die Browserkonsole. In Chrome klicken Sie mit der rechten Maustaste auf die Seite, wählen Sie **Untersuchen** und dann den Tab **Konsole** aus.
4. Führen Sie diese Befehle in der Konsole aus:
   - `window.braze.getCachedContentCards()`
   - `window.braze.toggleContentCards()`

## Card-Typen und Eigenschaften {#card-types-and-properties}

Das Content-Card-Datenmodell ist im Web SDK verfügbar und bietet die folgenden Content-Card-Typen: [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html), [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html) und [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html). Jeder Typ erbt gemeinsame Eigenschaften von einem Basismodell [Card](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html) und hat die folgenden zusätzlichen Eigenschaften.

{% alert tip %}
Informationen zum Protokollieren von Content-Card-Daten finden Sie unter [Analytics protokollieren]({{site.baseurl}}/developer_guide/content_cards/logging_analytics).
{% endalert %}

### Basis-Card-Modell {#base-card-model}

Alle Content Cards haben diese gemeinsamen Eigenschaften:

| Eigenschaft | Beschreibung |
|---|---|
| `expiresAt` | Der UNIX-Zeitstempel des Ablaufzeitpunkts der Card. |
| `extras` | (Optional) Schlüssel-Wert-Paar-Daten, formatiert als String-Objekt mit einem Wert-String. |
| `id` | (Optional) Die ID der Card. Diese wird zu Analytics-Zwecken zusammen mit Events an Braze zurückgemeldet. |
| `pinned` | Diese Eigenschaft gibt an, ob die Card im Dashboard als „angepinnt“ eingerichtet wurde. |
| `updated` | Der UNIX-Zeitstempel der letzten Änderung dieser Card. |
| `viewed` | Diese Eigenschaft gibt an, ob die Nutzer:in die Card angesehen hat oder nicht. |
| `isControl` | Diese Eigenschaft ist `true`, wenn eine Card eine „Kontrollgruppe“ innerhalb eines A/B-Tests ist. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Basis-Card-Modell" }

### Nur Bild {#image-only}

[ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html)-Cards sind anklickbare Bilder in voller Größe.

| Eigenschaft | Beschreibung |
|---|---|
| `aspectRatio` | Das Seitenverhältnis des Card-Bildes; dient als Hinweis, bevor das Laden des Bildes abgeschlossen ist. Beachten Sie, dass diese Eigenschaft unter bestimmten Umständen möglicherweise nicht bereitgestellt wird. |
| `categories` | Diese Eigenschaft dient ausschließlich der Organisation in Ihrer angepassten Implementierung; diese Kategorien können im Dashboard-Composer festgelegt werden. |
| `clicked` | Diese Eigenschaft gibt an, ob diese Card jemals auf diesem Gerät angeklickt wurde. |
| `created` | Der UNIX-Zeitstempel des Erstellungszeitpunkts der Card in Braze. |
| `dismissed` | Diese Eigenschaft gibt an, ob diese Card geschlossen wurde. |
| `dismissible` | Diese Eigenschaft gibt an, ob die Nutzer:in die Card schließen und aus der Ansicht entfernen kann. |
| `imageUrl` | Die URL des Card-Bildes. |
| `linkText` | Der Anzeigetext für die URL. |
| `url` | Die URL, die nach dem Anklicken der Card geöffnet wird. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nur Bild" }

### Bild mit Untertitel {#captioned-image}

[CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html)-Cards sind anklickbare Bilder in voller Größe mit beschreibendem Begleittext.

| Eigenschaft | Beschreibung |
|---|---|
| `aspectRatio` | Das Seitenverhältnis des Card-Bildes; dient als Hinweis, bevor das Laden des Bildes abgeschlossen ist. Beachten Sie, dass diese Eigenschaft unter bestimmten Umständen möglicherweise nicht bereitgestellt wird. |
| `categories` | Diese Eigenschaft dient ausschließlich der Organisation in Ihrer angepassten Implementierung; diese Kategorien können im Dashboard-Composer festgelegt werden. |
| `clicked` | Diese Eigenschaft gibt an, ob diese Card jemals auf diesem Gerät angeklickt wurde. |
| `created` | Der UNIX-Zeitstempel des Erstellungszeitpunkts der Card in Braze. |
| `dismissed` | Diese Eigenschaft gibt an, ob diese Card geschlossen wurde. |
| `dismissible` | Diese Eigenschaft gibt an, ob die Nutzer:in die Card schließen und aus der Ansicht entfernen kann. |
| `imageUrl` | Die URL des Card-Bildes. |
| `linkText` | Der Anzeigetext für die URL. |
| `title` | Der Titeltext für diese Card. |
| `url` | Die URL, die nach dem Anklicken der Card geöffnet wird. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Bild mit Untertitel" }

### Klassisch {#classic}

Das [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html)-Modell kann ein Bild ohne Text oder einen Text mit Bild enthalten.

| Eigenschaft | Beschreibung |
|---|---|
| `aspectRatio` | Das Seitenverhältnis des Card-Bildes; dient als Hinweis, bevor das Laden des Bildes abgeschlossen ist. Beachten Sie, dass diese Eigenschaft unter bestimmten Umständen möglicherweise nicht bereitgestellt wird. |
| `categories` | Diese Eigenschaft dient ausschließlich der Organisation in Ihrer angepassten Implementierung; diese Kategorien können im Dashboard-Composer festgelegt werden. |
| `clicked` | Diese Eigenschaft gibt an, ob diese Card jemals auf diesem Gerät angeklickt wurde. |
| `created` | Der UNIX-Zeitstempel des Erstellungszeitpunkts der Card in Braze. |
| `description` | Der Fließtext für diese Card. |
| `dismissed` | Diese Eigenschaft gibt an, ob diese Card geschlossen wurde. |
| `dismissible` | Diese Eigenschaft gibt an, ob die Nutzer:in die Card schließen und aus der Ansicht entfernen kann. |
| `imageUrl` | Die URL des Card-Bildes. |
| `linkText` | Der Anzeigetext für die URL. |
| `title` | Der Titeltext für diese Card. |
| `url` | Die URL, die nach dem Anklicken der Card geöffnet wird. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Klassisch" }

### Bildformate {#image-formats}

Content-Card-Bilder (einschließlich GIFs) werden mit Standard-HTML-`<img>`-Tags gerendert. Die GIF-Unterstützung hängt von den Fähigkeiten des Browsers der Nutzer:innen ab und erfordert keine Mindestversion des Web SDK. Alle modernen Browser unterstützen die GIF-Wiedergabe nativ.

## Kontrollgruppe {#control-group}

Wenn Sie den Standard-Feed für Content Cards verwenden, werden Impressionen und Klicks automatisch erfasst.

Wenn Sie eine angepasste Integration für Content Cards verwenden, müssen Sie [Impressionen protokollieren]({{site.baseurl}}/developer_guide/content_cards/logging_analytics), wenn eine Kontroll-Card angezeigt worden wäre. Stellen Sie dabei sicher, dass Sie Kontroll-Cards beim Protokollieren von Impressionen in einem A/B-Test berücksichtigen. Diese Cards sind leer, und obwohl sie von den Nutzer:innen nicht gesehen werden, sollten Sie dennoch Impressionen protokollieren, um ihre Performance mit Nicht-Kontroll-Cards vergleichen zu können.

Um festzustellen, ob eine Content-Card zur Kontrollgruppe eines A/B-Tests gehört, prüfen Sie die Eigenschaft `card.isControl` (Web SDK v4.5.0+) oder überprüfen Sie, ob die Card eine `ControlCard`-Instanz ist (`card instanceof braze.ControlCard`).

## Card-Methoden {#card-methods}

### Standard-Feed-Methoden {#default-feed-methods}

Verwenden Sie diese Methoden, wenn Sie Content Cards mit der Standard-Feed-UI von Braze anzeigen:

|Methode | Beschreibung |
|---|---|
|[`showContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards)| Zeigt den Standard-Content-Cards-Feed an. Rendert Cards in ein bereitgestelltes `parentNode`-HTML-Element oder als Sidebar mit fester Position, wenn kein Element angegeben wird. Akzeptiert eine optionale `filterFunction`, um Cards vor der Anzeige zu sortieren oder zu filtern. |
|[`hideContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#hidecontentcards)| Blendet den Standard-Content-Cards-Feed aus, wenn er aktuell angezeigt wird. |
|[`toggleContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards)| Zeigt den Standard-Content-Cards-Feed an, wenn er ausgeblendet ist, oder blendet ihn aus, wenn er sichtbar ist. Wenn Sie mehrere Content-Card-Feeds gleichzeitig anzeigen möchten, verwenden Sie stattdessen `showContentCards` und `hideContentCards`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Standard-Feed-Methoden" }

### Angepasste Feed-Methoden {#custom-feed-methods}

Verwenden Sie diese Methoden, wenn Sie Ihre eigene Content-Card-UI erstellen:

| Methode | Beschreibung |
|---|---|
| [`subscribeToContentCardsUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetocontentcardsupdates) | Registriert eine Callback-Funktion, die aufgerufen wird, wenn Content Cards für die:den aktuelle:n Nutzer:in aktualisiert werden, z. B. beim Sitzungsstart. Verwenden Sie diese Methode als primären Weg, um Card-Daten für Ihren angepassten Feed zu erhalten. Muss vor `openSession()` aufgerufen werden, um Updates bei der ersten Sitzung zu empfangen. |
| [`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards) | Gibt alle aktuell verfügbaren Cards aus der letzten Content-Cards-Aktualisierung zurück. Verwenden Sie diese Methode, um Cards beim Laden der Seite sofort anzuzeigen, ohne auf eine neue Serveranfrage warten zu müssen – z. B. wenn Nutzer:innen während einer aktiven Sitzung zu einer Seite zurückkehren. |
| [`requestContentCardsRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh) | Fordert eine sofortige Aktualisierung der Content Cards von den Braze-Servern an. Standardmäßig werden Cards beim Sitzungsstart und beim erneuten Öffnen des Standard-Feeds aktualisiert. Verwenden Sie diese Methode, um eine Aktualisierung zu anderen Zeitpunkten zu erzwingen, z. B. nach einer bestimmten Nutzer:innenaktion. Beachten Sie die [Rate-Limits]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed#rate-limit). |
| [`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions) | Protokolliert Impressionen-Events für ein Array von Cards. Rufen Sie diese Methode auf, wenn Cards gerendert und für Nutzer:innen sichtbar sind. Erforderlich für ein genaues Campaign-Reporting bei Verwendung einer angepassten UI, da Impressionen außerhalb des Standard-Feeds nicht automatisch erfasst werden. |
| [`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick) | Protokolliert ein Klick-Event für eine einzelne Card. Rufen Sie diese Methode auf, wenn Nutzer:innen in Ihrer angepassten UI mit einer Card interagieren. Erforderlich für ein genaues Campaign-Reporting, da Klicks außerhalb des Standard-Feeds nicht automatisch erfasst werden. |
| [`handleBrazeAction`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#handlebrazeaction) | Verarbeitet die URL einer Card und führt die konfigurierte Klick-Aktion aus, einschließlich Braze-Aktionen (`brazeActions://`-URLs) und Standard-URL-Navigation. Rufen Sie diese Methode in Ihrem Card-Klick-Handler auf, um sicherzustellen, dass die im Braze-Dashboard konfigurierten Klick-Verhaltensweisen ausgeführt werden. |
| [`dismissCard`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html#dismisscard) | Schließt eine Card programmatisch und entfernt sie aus dem Feed der:des Nutzer:in. Verwenden Sie diese Methode, um Nutzer:innen zu ermöglichen, Cards in Ihrer angepassten UI zu schließen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Angepasste Feed-Methoden" }

Weitere Details finden Sie in der [SDK-Referenzdokumentation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html).

## Best Practices

### Methoden in der richtigen Reihenfolge aufrufen {#call-methods-in-the-correct-order}

Bei angepassten Feeds werden Content Cards nur beim Sitzungsstart aktualisiert, wenn `subscribeToContentCardsUpdates()` vor `openSession()` aufgerufen wird. Rufen Sie Ihre Braze-Methoden in dieser Reihenfolge auf:

```javascript
import * as braze from "@braze/web-sdk";

// Step 1: Initialize the SDK
braze.initialize("YOUR-API-KEY", { baseUrl: "YOUR-SDK-ENDPOINT" });

// Step 2: Subscribe to card updates
braze.subscribeToContentCardsUpdates((updates) => {
  const cards = updates.cards;
  renderCards(cards);
});

// Step 3: Identify the user
braze.changeUser("USER_ID");

// Step 4: Start the session
braze.openSession();
```

### Gecachte Cards verwenden, um Inhalte über Seitenladevorgänge hinweg beizubehalten {#use-cached-cards-to-persist-content-across-page-loads}

Da `subscribeToContentCardsUpdates()` seinen Callback nur aufruft, wenn neue Updates vorliegen (z. B. beim Sitzungsstart), können Cards aus Ihrem angepassten Feed verschwinden, wenn Nutzer:innen die Seite mitten in einer Sitzung aktualisieren. Um dies zu verhindern, verwenden Sie `getCachedContentCards()`, um Cards sofort aus dem lokalen Cache zu rendern, zusätzlich zu Ihrem Abo für neue Updates:

```javascript
import * as braze from "@braze/web-sdk";

function renderCards(cards) {
  const container = document.getElementById("content-cards");
  container.textContent = "";
  const displayedCards = [];

  cards.forEach(card => {
    if (card instanceof braze.ClassicCard || card instanceof braze.CaptionedImage) {
      const cardElement = document.createElement("div");

      const h3 = document.createElement("h3");
      h3.textContent = card.title || "";
      cardElement.appendChild(h3);

      const p = document.createElement("p");
      p.textContent = card.description || "";
      cardElement.appendChild(p);

      if (card.imageUrl) {
        const img = document.createElement("img");
        img.src = card.imageUrl;
        img.alt = card.title || "";
        cardElement.appendChild(img);
      }

      if (card.url) {
        cardElement.addEventListener("click", () => {
          braze.logContentCardClick(card);
          braze.handleBrazeAction(card.url);
        });
      }

      container.appendChild(cardElement);
      displayedCards.push(card);
    }
  });

  if (displayedCards.length > 0) {
    braze.logContentCardImpressions(displayedCards);
  }
}

// Display cached cards immediately
const cached = braze.getCachedContentCards();
if (cached && cached.cards.length > 0) {
  renderCards(cached.cards);
}

// Subscribe to future updates
braze.subscribeToContentCardsUpdates((updates) => {
  renderCards(updates.cards);
});
```

### Analytics für angepasste Feeds protokollieren {#log-analytics-for-custom-feeds}

Bei Verwendung einer angepassten UI werden Impressionen, Klicks und Schließungen nicht automatisch erfasst. Sie müssen jedes Ereignis manuell protokollieren:

- **Impressionen:** Rufen Sie `logContentCardImpressions([card1, card2, ...])` mit einem Array von Card-Objekten auf, wenn Cards für die Nutzer:innen sichtbar werden.
- **Klicks:** Rufen Sie `logContentCardClick(card)` auf, wenn Nutzer:innen mit einer Card interagieren.
- **Klickverhalten:** Rufen Sie `handleBrazeAction(card.url)` auf, um die konfigurierte Klickaktion der Card auszuführen (z. B. Navigation zu einer URL oder Protokollierung eines angepassten Events).

{% alert warning %}
Das an `logContentCardClick()` übergebene Argument muss ein originales Braze-`Card`-Objekt sein. Wenn Sie die Card-Daten transformieren oder rekonstruieren (z. B. durch Serialisierung und Deserialisierung), werden Klicks nicht protokolliert und Sie sehen den Fehler: „card must be a Card object.“
{% endalert %}

## Verwendung von Google Tag Manager {#using-google-tag-manager}

Google Tag Manager funktioniert, indem das [Braze CDN]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#install-cdn) (eine Version unseres Web-SDK) direkt in Ihren Website-Code eingespeist wird. Das bedeutet, dass alle SDK-Methoden verfügbar sind, genau wie bei einer Integration des SDK ohne Google Tag Manager – mit Ausnahme der Implementierung von Content Cards.

### Content Cards einrichten {#setting-up-content-cards}

{% tabs local %}
{% tab Google Tag Manager %}
Für eine Standard-Integration des Content-Card-Feeds können Sie ein **Custom HTML**-Tag im Google Tag Manager verwenden. Fügen Sie Folgendes zu Ihrem Custom-HTML-Tag hinzu, um den Standard-Content-Card-Feed zu aktivieren:

```html
<script>
   window.braze.showContentCards();
</script>
```

![Tag-Konfiguration im Google Tag Manager eines Custom-HTML-Tags, das den Content-Card-Feed anzeigt.]({% image_buster /assets/img/web-gtm/gtm_content_cards.png %})
{% endtab %}

{% tab Manuell %}
Wenn Sie mehr Freiheit bei der Anpassung des Erscheinungsbilds von Content Cards und ihres Feeds wünschen, können Sie Content Cards direkt in Ihre native Website integrieren. Dafür gibt es zwei Ansätze: die Standard-Feed-UI oder eine angepasste Feed-UI.

{% subtabs local %}
{% subtab Standard-Feed %}
Bei der Implementierung der [Standard-Feed-UI]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration#standard-feed-ui) muss `window.` an den Anfang der Braze-Methoden hinzugefügt werden. Zum Beispiel sollte `braze.showContentCards` stattdessen `window.braze.showContentCards` lauten.
{% endsubtab %}

{% subtab Angepasster Feed %}
Für die Gestaltung eines [angepassten Feeds]({{site.baseurl}}/developer_guide/content_cards/creating_cards) sind die Schritte identisch mit denen einer SDK-Integration ohne GTM. Wenn Sie beispielsweise die Breite des Content-Card-Feeds anpassen möchten, können Sie Folgendes in Ihre CSS-Datei einfügen:

{% raw %}
```css
body .ab-feed {
    width: 800px;
}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Templates upgraden {#upgrading}

Um auf die neueste Version des Braze Web SDK zu upgraden, führen Sie die folgenden drei Schritte in Ihrem Google Tag Manager-Dashboard aus:

1. **Tag-Template aktualisieren**<br>Gehen Sie zur Seite **Templates** in Ihrem Workspace. Hier sollten Sie ein Symbol sehen, das darauf hinweist, dass ein Update verfügbar ist.<br><br>![Seite „Templates“ mit Hinweis auf ein verfügbares Update]({% image_buster /assets/img/web-gtm/gtm-update-available.png %})<br><br>Klicken Sie auf dieses Symbol und klicken Sie nach Überprüfung der Änderung auf **Accept Update**.<br><br>![Ein Vergleich des alten und neuen Tag-Templates mit einem Button „Accept Update“]({% image_buster /assets/img/web-gtm/gtm-accept-update.png %})<br><br>
2. **Versionsnummer aktualisieren**<br>Sobald Ihr Tag-Template aktualisiert wurde, bearbeiten Sie das Braze Initialization Tag und aktualisieren Sie die SDK-Version auf die neueste `major.minor`-Version. Wenn die neueste Version beispielsweise `4.1.2` ist, geben Sie `4.1` ein. Sie können eine Liste der SDK-Versionen in unserem [Changelog](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md) einsehen.<br><br>![Braze Initialization Template mit einem Eingabefeld zur Änderung der SDK-Version]({% image_buster /assets/img/web-gtm/gtm-version-number.png %})<br><br>
3. **QA und Veröffentlichung**<br>Überprüfen Sie die neue SDK-Version mit dem [Debugging-Tool](https://support.google.com/tagmanager/answer/6107056?hl=en) von Google Tag Manager, bevor Sie ein Update für Ihren Tag-Container veröffentlichen.

### Fehlerbehebung {#troubleshooting}

#### Tag-Debugging aktivieren {#debugging}

Jedes Braze-Tag-Template verfügt über ein optionales Kontrollkästchen **GTM Tag Debugging**, mit dem Debug-Nachrichten in der JavaScript-Konsole Ihrer Webseite protokolliert werden können.

![Das Debugging-Tool von Google Tag Manager]({% image_buster /assets/img/web-gtm/gtm-tag-debugging.png %})

#### Debug-Modus aufrufen {#enter-debug-mode}

Eine weitere Möglichkeit, das Debugging Ihrer Google Tag Manager-Integration zu unterstützen, ist die Verwendung des [Vorschaumodus](https://support.google.com/tagmanager/answer/6107056) von Google.

Dies hilft dabei, zu identifizieren, welche Werte von der Datenschicht Ihrer Webseite an jedes ausgelöste Braze-Tag gesendet werden, und erklärt auch, welche Tags ausgelöst oder nicht ausgelöst wurden.

![Die Übersichtsseite des Braze Initialization Tags bietet einen Überblick über das Tag, einschließlich Informationen darüber, welche Tags ausgelöst wurden.]({% image_buster /assets/img/web-gtm/gtm-debug-mode.png %})

#### Tag-Reihenfolge für angepasste Events überprüfen {#tag-sequencing}

Wenn angepasste Events oder andere Aktionen nicht in Braze protokolliert werden, ist eine häufige Ursache eine Race-Condition, bei der ein Aktions-Tag (z. B. **Custom Event** oder **Purchase**) ausgelöst wird, bevor das **Braze Initialization**-Tag abgeschlossen ist. Um dies zu beheben, konfigurieren Sie die [Tag-Reihenfolge](https://support.google.com/tagmanager/answer/6238868) in GTM:

1. Öffnen Sie das Aktions-Tag, das nicht korrekt protokolliert wird.
2. Wählen Sie unter **Advanced Settings** > **Tag Sequencing** die Option **A tag that fires before \[this tag\]** aus.
3. Wählen Sie Ihr **Braze Initialization**-Tag als Setup-Tag aus.

Dadurch wird sichergestellt, dass das SDK vollständig initialisiert ist, bevor Aktions-Tags versuchen, Daten an Braze zu senden.

#### Ausführliches Logging aktivieren {#enable-verbose-logging}

Um detaillierte Protokolle für die Fehlerbehebung zu erfassen, können Sie ausführliches Logging für Ihre Google Tag Manager-Integration aktivieren. Diese Protokolle werden im Tab **Console** der [Entwicklertools](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools) Ihres Browsers angezeigt.

Navigieren Sie in Ihrer Google Tag Manager-Integration zu Ihrem Braze Initialization Tag und wählen Sie **Enable Web SDK Logging** aus.

![Die Übersichtsseite des Braze Initialization Tags mit aktivierter Option „Enable Web SDK Logging“.]({% image_buster /assets/img/web-gtm/gtm_verbose_logging.png %})

[changelog]: https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md