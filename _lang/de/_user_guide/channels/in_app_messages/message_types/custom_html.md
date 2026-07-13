---
nav_title: "Angepasstes HTML"
article_title: "Angepasstes HTML"
page_order: 4
page_type: reference
description: "Dieser Artikel bietet einen Überblick über In-App-Nachrichten mit angepasstem Code, einschließlich JavaScript-Methoden, Button-Tracking und der Verwendung der interaktiven HTML-Vorschau in Braze."
channel:
  - in-app messages
---

# In-App-Nachrichten mit angepasstem HTML {#custom-html-messages}

> Unsere Standard-In-App-Nachrichten können zwar auf vielfältige Weise angepasst werden, aber mit Nachrichten, die mit HTML, CSS und JavaScript entworfen und erstellt werden, erhalten Sie noch mehr Kontrolle über das Erscheinungsbild Ihrer Campaigns. Mit etwas einfacher Gestaltung können Sie angepasste Funktionalität und Branding freischalten, die all Ihren Anforderungen entsprechen.

Dieser Nachrichtentyp ist im [traditionellen Editor]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional) verfügbar.

## So funktioniert es {#how-it-works}

HTML-In-App-Nachrichten ermöglichen eine größere Kontrolle über das Erscheinungsbild einer Nachricht, einschließlich der folgenden Möglichkeiten:

- Angepasste Schriftarten und Stile
- Videos
- Mehrere Bilder
- On-Click-Verhalten
- Interaktive Komponenten
- Angepasste Animationen

Angepasste HTML-Nachrichten können die [JavaScript-Bridge](#javascript-bridge)-Methoden verwenden, um Ereignisse zu protokollieren, angepasste Attribute zu setzen, die Nachricht zu schließen und mehr! Schauen Sie sich unser [GitHub-Repository](https://github.com/braze-inc/in-app-message-templates) an, das detaillierte Anleitungen enthält, wie Sie HTML-In-App-Nachrichten für Ihre Bedürfnisse verwenden und anpassen können, sowie eine Reihe von HTML5-In-App-Nachrichten-Templates, die Ihnen den Einstieg erleichtern.

{% alert note %}
Um HTML-In-App-Nachrichten über das Web-SDK zu aktivieren, müssen Sie die Initialisierungsoption `allowUserSuppliedJavascript` an Braze übergeben: zum Beispiel `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Dies geschieht aus Sicherheitsgründen, da HTML-In-App-Nachrichten JavaScript ausführen können, weshalb ein Website-Administrator sie aktivieren muss.
{% endalert %}

## JavaScript-Bridge {#javascript-bridge}

{% include javascript_bridge/reference.md %}

## Link-basierte Aktionen {#link-based-actions}

Zusätzlich zu angepasstem JavaScript können Braze-SDKs auch Analysedaten mit diesen praktischen URL-Shortcuts senden. Beachten Sie, dass diese Abfrageparameter und URL-Schemata alle case-sensitive sind.

### Button-Klick-Tracking (veraltet) {#button-click-tracking-deprecated}

{% alert warning %}
Die Verwendung von `abButtonID` wird bei Nachrichtentypen mit [HTML mit Vorschau]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#html-upload-with-preview) nicht unterstützt. Weitere Informationen finden Sie in unserem [Upgrade-Leitfaden]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#html-upload-with-preview).
{% endalert %}

Um Button-Klicks für die In-App-Nachrichten-Analyse zu protokollieren, können Sie `abButtonId` als Abfrageparameter zu jedem Deeplink, jeder Weiterleitungs-URL oder jedem Ankerelement `<a>` hinzufügen. Verwenden Sie `?abButtonId=0`, um einen „Button 1“-Klick zu protokollieren, und `?abButtonId=1`, um einen „Button 2“-Klick zu protokollieren.

Wie bei anderen URL-Parametern sollte der erste Parameter mit einem Fragezeichen `?` beginnen, während nachfolgende Parameter durch ein kaufmännisches Und `&` getrennt werden sollten.

#### Beispiel-URLs {#example-urls}

- `https://example.com/?abButtonId=0` – Button-1-Klick
- `https://example.com/?abButtonId=1` – Button-2-Klick
- `https://example.com/?utm_source=braze&abButtonId=0` – Button-1-Klick mit anderen vorhandenen URL-Parametern
- `myApp://deep-link?page=home&abButtonId=1` – Mobiler Deeplink mit Button-2-Klick
- `<a href="https://example.com/?abButtonId=1">` – Ankerelement `<a>` mit Button-2-Klick

{% alert note %}
In-App-Nachrichten unterstützen nur Button-1- und Button-2-Klicks. URLs, die keine dieser beiden Button-IDs angeben, werden als generische „Body-Klicks“ protokolliert.
{% endalert %}

### Link in neuem Fenster öffnen (nur mobil) {#open-link-in-new-window-mobile-only}

Um Links außerhalb Ihrer App in einem neuen Fenster zu öffnen, setzen Sie `?abExternalOpen=true`. Die Nachricht wird geschlossen, bevor der Link geöffnet wird.

Für Deeplinking öffnet Braze Ihre URL unabhängig vom Wert von `abExternalOpen`.

### Als Deeplink öffnen (nur mobil) {#open-as-deeplink-mobile-only}

Damit Braze Ihren HTTP- oder HTTPS-Link als Deeplink behandelt, setzen Sie `?abDeepLink=true`.

Wenn dieser Abfrage-String-Parameter fehlt oder auf `false` gesetzt ist, versucht Braze, den Weblink in einem internen Webbrowser innerhalb der Host-App zu öffnen.

### In-App-Nachricht schließen {#close-in-app-message}

Um eine In-App-Nachricht zu schließen, können Sie die JavaScript-Methode `brazeBridge.closeMessage()` verwenden.

Zum Beispiel schließt `<a onclick="brazeBridge.closeMessage()" href="#">Schließen</a>` die In-App-Nachricht.

## HTML-Upload mit Vorschau {#html-upload-with-preview}

Beim Erstellen von angepassten HTML-In-App-Nachrichten können Sie Ihre interaktiven Inhalte direkt in Braze in der Vorschau anzeigen.

Das Nachrichtenvorschau-Panel des Editors zeigt eine realistische Vorschau, die das in Ihrer Nachricht enthaltene JavaScript rendert. Sie können Ihre angepassten Nachrichten im Vorschau-Panel in der Vorschau anzeigen und mit ihnen interagieren, indem Sie durch Seiten blättern, Formulare oder Umfragen absenden, JavaScript-Animationen ansehen und mehr!

![Interaktion mit der HTML-Vorschau durch Wischen zwischen Seiten.]({% image_buster /assets/img/iam-beta-javascript-preview.gif %})

{% alert tip %}
Alle `brazeBridge`-JavaScript-Methoden, die Sie in Ihrem HTML verwenden, aktualisieren keine Nutzer:innenprofile, während Sie im Dashboard eine Vorschau anzeigen.
{% endalert %}

### SDK-Anforderungen {#supported-sdk-versions}

Um die HTML-Vorschau für In-App-Nachrichten zu verwenden, müssen Sie auf die folgenden Mindestversionen des Braze SDK aktualisieren:

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

{% alert warning %}
Da dieser Nachrichtentyp nur von bestimmten neueren SDK-Versionen empfangen werden kann, erhalten Nutzer:innen mit nicht unterstützten SDK-Versionen die Nachricht nicht. Erwägen Sie, diesen Nachrichtentyp erst zu verwenden, nachdem ein erheblicher Teil Ihrer Nutzerbasis erreichbar ist, oder richten Sie sich nur an Nutzer:innen, deren App-Version neuer als die Anforderungen ist. Erfahren Sie mehr über das [Filtern nach der neuesten App-Version]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/new_features#filtering-by-most-recent-app-versions).
{% endalert %}

### Eine Campaign erstellen {#instructions}

Ihre mobilen App-Nutzer:innen müssen auf die unterstützten SDK-Versionen aktualisieren, um eine In-App-Nachricht mit **angepasstem Code** zu erhalten. Wir empfehlen, [Nutzer:innen zum Aktualisieren aufzufordern]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/new_features), bevor Sie Campaigns starten, die von neueren Braze-SDK-Versionen abhängen.

#### Asset-Dateien {#asset-files}

Beim Erstellen von In-App-Nachrichten mit angepasstem Code und HTML-Upload können Sie Campaign-Assets in die [Medienbibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) hochladen, um sie in Ihrer Nachricht zu referenzieren.

Die folgenden Dateitypen werden für den Upload unterstützt:

| Dateityp           | Dateierweiterung                  |
| :------------------ | :-------------------------------- |
| Schriftdateien      | `.ttf`, `.woff`, `.otf`, `.woff2` |
| SVG-Bilder          | `.svg`                            |
| JavaScript-Dateien  | `.js`                             |
| CSS-Dateien         | `.css`                            |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Asset-Dateien" }

Braze empfiehlt das Hochladen von Assets in die Medienbibliothek aus zwei Gründen:

1. Assets, die über die Medienbibliothek zu einer Campaign hinzugefügt werden, ermöglichen die Anzeige Ihrer Nachrichten, auch wenn Nutzer:innen offline sind oder eine schlechte Internetverbindung haben.
2. In Braze hochgeladene Assets können über mehrere Campaigns hinweg wiederverwendet werden.

##### Asset-Dateien hinzufügen {#adding-asset-files}

Sie können neue oder vorhandene Assets zu Ihrer Campaign hinzufügen.

Um neue Assets zu Ihrer Campaign hinzuzufügen, verwenden Sie den Drag-and-Drop-Bereich zum Hochladen einer Datei. Assets, die in diesem Bereich hinzugefügt werden, werden auch automatisch zur Medienbibliothek hinzugefügt. Um Assets hinzuzufügen, die Sie bereits in die Medienbibliothek hochgeladen haben, wählen Sie **Aus Medienbibliothek hinzufügen**.

Nachdem Ihre Assets hinzugefügt wurden, erscheinen sie im Abschnitt **Assets für diese Campaign**.

Wenn der Dateiname eines Assets mit dem eines lokalen HTML-Assets übereinstimmt, wird es automatisch ersetzt (zum Beispiel wird `cat.png` hochgeladen und `<img src="cat.png" />` existiert).

Andernfalls fahren Sie mit der Maus über ein Asset in der Liste und wählen Sie <i class="fas fa-copy"></i> **Kopieren**, um die URL der Datei in Ihre Zwischenablage zu kopieren. Fügen Sie dann die kopierte Asset-URL in Ihr HTML ein, wie Sie es normalerweise beim Referenzieren eines Remote-Assets tun würden.

### HTML-Editor {#html-editor}

Änderungen, die Sie im HTML vornehmen, werden automatisch im Vorschau-Panel gerendert, während Sie tippen. Alle [`brazeBridge`-JavaScript](#bridge)-Methoden, die Sie in Ihrem HTML verwenden, aktualisieren keine Nutzer:innenprofile, während Sie im Dashboard eine Vorschau anzeigen.

{% alert tip %}
Sie können <i class="fa-solid fa-magnifying-glass"></i> **Suchen** im HTML-Editor auswählen, um in Ihrem Code zu suchen!
{% endalert %}

### Button-Tracking {#button-tracking-improvements}

Sie können die Performance innerhalb Ihrer In-App-Nachricht mit angepasstem Code mithilfe der JavaScript-Methode [`brazeBridge.logClick(button_id)`]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types) verfolgen. Dies ermöglicht es Ihnen, „Button 1“, „Button 2“ und „Body-Klicks“ programmatisch mit `brazeBridge.logClick('0')`, `brazeBridge.logClick('1')` bzw. `brazeBridge.logClick()` zu verfolgen.

| Klicks     | Methode                       |
| ---------- | ----------------------------- |
| Button 1   | `brazeBridge.logClick('0')` |
| Button 2   | `brazeBridge.logClick('1')` |
| Body-Klick | `brazeBridge.logClick()`    |
| Angepasstes Button-Tracking |`brazeBridge.logClick('your custom name here')`|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Button-Tracking" }

{% alert note %}
Diese Methode des Button-Trackings ersetzt die früheren automatischen Klick-Tracking-Methoden (wie `?abButtonId=0`), die entfernt wurden.
{% endalert %}

Verwenden Sie [`brazeBridge.logClick(button_id)`](#button-tracking-improvements) für HTML-Nachrichten mit Vorschau, wenn Sie mehr als zwei getrackte Buttons benötigen. Button 1 und Button 2 entsprechen `'0'` und `'1'`; zusätzliche Buttons verwenden angepasste IDs (bis zu 100 eindeutige IDs pro Campaign). Informationen zu Zeichenbeschränkungen für Button-IDs finden Sie unter [Button-Tracking](#button-tracking-improvements).

### Fehlerbehebung bei angepassten HTML-Links und Schließverhalten {#troubleshoot-custom-html-links-and-close-behavior}

#### Button-Klicks öffnen den Link nicht {#button-clicks-do-not-open-the-link}

Wenn ein Button in Ihrer angepassten HTML-In-App-Nachricht beim Klicken nicht lädt, überprüfen Sie, ob der Link eine gültige URL oder ein unterstütztes Deeplink-Schema verwendet. Fehlerhafte URLs oder nicht unterstützte angepasste Schemata können verhindern, dass die Klick-Aktion abgeschlossen wird.

#### Body-Klicks beim Schließen der Nachricht {#body-clicks-when-closing-the-message}

Der Aufruf von `brazeBridge.closeMessage()` schließt die Nachricht, protokolliert aber allein keine Analysedaten. Um einen Body-Klick zu protokollieren, wenn Nutzer:innen die Nachricht schließen, rufen Sie `brazeBridge.logClick()` vor `brazeBridge.closeMessage()` auf, damit die Klick-Protokollierung plattformübergreifend konsistent bleibt.

### Nicht abwärtskompatible Änderungen {#backward-incompatible-changes}

1. Die bemerkenswerteste inkompatible Änderung bei diesem neuen Nachrichtentyp sind die SDK-Anforderungen. Nutzer:innen, deren App-SDK die Mindest-[SDK-Versionsanforderungen](#supported-sdk-versions) nicht erfüllt, bekommen die Nachricht nicht angezeigt.
2. Der Deeplink `braze://close`, der zuvor auf mobilen Apps unterstützt wurde, wurde zugunsten der JavaScript-Methode `brazeBridge.closeMessage()` entfernt. Dies ermöglicht plattformübergreifende HTML-Nachrichten, da das Web keine Deeplinks unterstützt.
3. Automatisches Klick-Tracking, das `?abButtonId=0` für Button-IDs verwendete, und „Body-Klick“-Tracking auf Schließen-Buttons wurden entfernt. Die folgenden Codebeispiele zeigen, wie Sie Ihr HTML ändern, um unsere neuen Klick-Tracking-JavaScript-Methoden zu verwenden:

   | Vor | Nach |
   |:-------- |:------------|
   |<code>&lt;a href="braze://close"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="brazeBridge.logClick();brazeBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
   |<code>&lt;a href="braze://close?abButtonId=0"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="brazeBridge.logClick('0');brazeBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
   |<code>&lt;a href="app://deeplink?abButtonId=0">Track button 1&lt;/a&gt;</code>|<code>&lt;a href="app://deeplink" onclick="brazeBridge.logClick('0')"&gt;Track button 1&lt;/a&gt;</code>|
   |<code>&lt;script&gt;<br>location.href = "braze://close?abButtonId=1"<br>&lt;/script&gt;</code>|<code>&lt;script&gt;<br>window.addEventListener("ab.BridgeReady", function(){<br>&nbsp;&nbsp;brazeBridge.logClick("1");<br>&nbsp;&nbsp;brazeBridge.closeMessage();<br>});<br>&lt;/script&gt;</code>|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nicht abwärtskompatible Änderungen" }