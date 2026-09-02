---
nav_title: Frühere Generationen
article_title: Frühere Generationen von In-App-Nachrichten
page_order: 20
page_type: reference
description: "Dieser Artikel gibt einen Überblick über frühere Informationen zu In-App-Nachrichten in Braze."
channel: in-app messages
noindex: true
hidden : true
---

# Frühere Generationen von In-App-Nachrichten {#previous-in-app-message-generations}

{% alert important %}
Auf dieser Seite finden Sie frühere Informationen zu unseren In-App-Nachrichten. Die aktuellsten Informationen über unsere aktuelle Generation von In-App-Nachrichten finden Sie in unserer Dokumentation zu den [In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages/).
{% endalert %}

## Universal

Hier können Sie frühere Informationen zu unseren In-App-Nachrichten einsehen. Die aktuellsten Informationen über unsere aktuelle Generation von In-App-Nachrichten finden Sie in unserer [Dokumentation zur Übersicht über In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages/).

{% details Vollbild %}
Diese sind am ansprechendsten, aber auch am aufdringlichsten, da sie den gesamten Bildschirm Ihrer Nutzer:innen bedecken. Sie eignen sich hervorragend für die Darstellung großer, reichhaltiger Bilder und können sehr nützlich sein, um wichtige Informationen zu vermitteln, z. B. über wichtige neue Features und auslaufende Aktionen. Da sie das Nutzererlebnis stärker unterbrechen, sollten Sie sie sparsam für Inhalte mit höchster Priorität verwenden.

![Vollbild-Nachricht]({% image_buster /assets/img_archive/braze_fullscreen.png %}){: style="max-width:80%;"}

**Anpassbare Features**

- Überschrift und Textkörper
- Ein großes Bild
- Bis zu zwei Aktions-Buttons mit separatem Klickverhalten und Deeplinks
- Verschiedene Farben für die Kopfzeile, den Text, die Buttons und den Hintergrund
- Schlüssel-Wert-Paare

{% enddetails %}
{% details  Modal %}
Diese Nachrichten sind nicht so aufdringlich wie Vollbild-Nachrichten, da sie den Nutzer:innen immer noch einen Teil der UI Ihrer App zeigen. Da sie immer noch Buttons und Bilder enthalten, sind modale Nachrichten möglicherweise eine bessere Option als Slideups, wenn Sie eine interaktivere, visuelle Kampagne wünschen. Diese eignen sich hervorragend für Inhalte mit mittlerer Priorität, wie z. B. App-Updates und nicht dringende Angebote und Ereignisse.

![Modale Nachricht]({% image_buster /assets/img_archive/braze_modal.png %}){: style="max-width:80%;"}

**Anpassbare Features**

- Überschrift und Textkörper
- Ein Bild oder ein anpassbares Badge-Symbol
- Bis zu zwei Aktions-Buttons mit separatem Klickverhalten und Deeplinks
- Verschiedene Farben für die Kopfzeile, den Text, die Buttons und den Hintergrund
- Schlüssel-Wert-Paare

{% enddetails %}

{% details Traditionelles Slideup %}
Dies ist die am wenigsten aufdringliche Art von Nachrichten, obwohl sie je nach Verwendung von Farben und Badge-Symbolen mehr oder weniger Aufmerksamkeit erregen können. Dieses Nachrichtenformat eignet sich am besten für das Onboarding neuer Nutzer:innen und die Hinführung zu bestimmten Features in der App, da es das App-Erlebnis nicht unterbricht und eine kontinuierliche Erkundung ermöglicht.

![Slideup-Nachricht]({% image_buster /assets/img_archive/stopwatch_slideup_IAM.gif %}){: style="max-width:50%;"}

**Anpassbare Features**

- Haupttext
- Ein Bild oder ein anpassbares Badge-Symbol
- Verschiedene Farben für Slideup-Hintergrund, Text und Symbol
- Verhalten beim Schließen von Nachrichten
- Slideup-Position (oben oder unten auf dem Bildschirm der App)
- Schlüssel-Wert-Paare

{% enddetails %}

<br>

## Web

Hier finden Sie frühere Informationen über stärker angepasste In-App-Nachrichten. Die aktuellsten Informationen über unsere aktuelle Generation von In-App-Nachrichten finden Sie in unserer [Dokumentation zur Anpassung]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/).

{% details E-Mail-Erfassungsnachricht %}
Mit Nachrichten zur E-Mail-Erfassung können Sie Nutzer:innen Ihrer Website auf einfache Weise auffordern, ihre E-Mail-Adresse zu übermitteln. Diese steht dann im Braze-System für alle Ihre Messaging-Kampagnen zur Verfügung.

![E-Mail-Erfassungsnachricht]({% image_buster /assets/img_archive/web-email-capture.png %}){: style="max-width:60%;"}

>  Um In-App-Nachrichten zur E-Mail-Erfassung über das Web SDK or Software-Development-Kit zu aktivieren, müssen Sie Braze die Initialisierungsoption `allowUserSuppliedJavascript` zur Verfügung stellen, zum Beispiel `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Dies geschieht aus Sicherheitsgründen – In-App-Nachrichten im HTML-Format können JavaScript ausführen, sodass ein Website-Betreiber sie aktivieren muss.

**Anpassbare Features**

- Überschrift, Textkörper und Text des Buttons „Senden“
- Ein optionales Bild
- Ein optionaler Link zu den „Nutzungsbedingungen“
- Verschiedene Farben für die Kopfzeile, den Text, die Buttons und den Hintergrund
- Schlüssel-Wert-Paare

{% enddetails %}

{% details Angepasste HTML-Nachricht %}

Während die Standard-In-App-Nachrichten von Braze auf vielfältige Weise angepasst werden können, haben Sie mit Nachrichten, die mit HTML, CSS und JavaScript entworfen und erstellt wurden, eine noch größere Kontrolle über das Aussehen Ihrer Campaigns. Mit einer einfachen Zusammenstellung können Sie angepasste Funktionen und ein individuelles Branding freischalten, das Ihren Bedürfnissen entspricht. In-App-Nachrichten im HTML-Format ermöglichen eine bessere Kontrolle über das Aussehen einer Nachricht, und alles, was HTML5 unterstützt, wird auch von Braze unterstützt.

**JavaScript-Brücke (appboyBridge)**

In-App-Nachrichten im HTML-Format unterstützen eine JavaScript-„Bridge“-Schnittstelle zum Braze Web SDK or Software-Development-Kit, die es Ihnen erlaubt, angepasste Braze-Aktionen auszulösen, wenn Nutzer:innen auf Elemente mit Links klicken oder sich anderweitig mit Ihren Inhalten beschäftigen. Die folgenden JavaScript-Methoden werden in den HTML-In-App-Nachrichten von Braze unterstützt:

{% multi_lang_include archive/appboyBridge.md platform="web" %}

Für das Analytics-Tracking protokolliert jedes `<a>`- oder `<button>`-Element in Ihrem HTML-Code automatisch eine „Klick“-Aktion für die Campaign, die mit der In-App-Nachricht verknüpft ist. Um einen „Button-Klick“ anstelle eines „Body-Klicks“ zu protokollieren, geben Sie entweder einen Query-String-Wert von abButtonId in der href des Links an (z. B. `<a href="http://mysite.com?abButtonId=0">click me</a>`) oder eine ID im HTML-Element (z. B. `<a id="0" href="http://mysite.com">click me</a>`). Beachten Sie, dass derzeit nur die Button-IDs „0“ und „1“ akzeptiert werden. Ein Link mit einer Button-ID von 0 wird auf dem Dashboard als „Button 1“ dargestellt, während ein Link mit einer Button-ID von 1 als „Button 2“ dargestellt wird.

>  Um In-App-Nachrichten im HTML-Format über das Web SDK or Software-Development-Kit zu aktivieren, müssen Sie Braze die Initialisierungsoption `allowUserSuppliedJavascript` zur Verfügung stellen, zum Beispiel `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Dies geschieht aus Sicherheitsgründen – In-App-Nachrichten im HTML-Format können JavaScript ausführen, sodass ein Website-Betreiber sie aktivieren muss.

{% enddetails %}

{% details HTML-In-App-Nachricht-Templates %}

Wir haben eine Reihe von HTML5-Templates für In-App-Nachrichten entworfen, die Ihnen den Einstieg erleichtern. Sehen Sie sich unser [GitHub-Repository](https://github.com/braze-inc/in-app-message-templates) an, das detaillierte Anweisungen zur Verwendung und Anpassung dieser Templates an Ihre Bedürfnisse enthält.

**Anpassbare Features**

- Schriftarten
- Stile
- Bilder + Videos
- On-Klick, der or klicken-Verhalten
- Interaktive Komponenten

{% enddetails %}

<br>

## Spezifikationen {#specifications}

Hier finden Sie frühere Informationen zu unseren kreativen Spezifikationen für In-App-Nachrichten. Die aktuellsten Informationen zu unserer aktuellen Generation von In-App-Nachrichten finden Sie in unserer [Dokumentation zu den kreativen Spezifikationen]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/).

### Zeichen- und Bildgrenzen {#character-and-image-limits}

Für alle in der folgenden Tabelle aufgeführten Arten von In-App-Nachrichten gelten die folgenden zusätzlichen Richtlinien:

- **Empfohlene Bildgröße:** 500&nbsp;KB
- **Maximale Bildgröße:** 5&nbsp;MB
- **Unterstützte Dateitypen:** PNG, JPEG, GIF

| Typ                               | Seitenverhältnis | Maximale Zeichenzahl |
| :--------------------------------- | :----------: | :-----------------: |
| Hochformat Vollbild (nur Bild)  |    10:16     |         240         |
| Hochformat Vollbild (mit Text)   |     5:4      |         240         |
| Querformat Vollbild (mit Text)  |     16:5     |         240         |
| Querformat Vollbild (nur Bild) |    16:10     |         240         |
| Slideup                            |     1:1      |         140         |
| Modal (nur Bild)                 |     1:1      |         140         |
| Modal (mit Text)                  |    29:10     |         140         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Zeichen- und Bildgrenzen" }

### Die Dateigröße von In-App-Nachrichten klein halten {#keeping-in-app-message-file-sizes-small}

Braze empfiehlt Ihnen, Ihre Bilder und HTML-Asset-ZIPs aus mehreren Gründen so klein wie möglich zu halten:

- Kleinere HTML- und Bildnachrichten werden schneller heruntergeladen und für Ihre Kund:innen schneller und zuverlässiger angezeigt.
- Kleinere HTML- und Bildnachrichten halten auch die Datenkosten Ihrer Kund:innen niedrig. In-App-Nachrichten von Braze werden bei Sitzungsbeginn im Hintergrund heruntergeladen, sodass sie in Realtime auf der Grundlage der von Ihnen ausgewählten Kriterien getriggert werden können. Wenn Sie also 10 In-App-Nachrichten im HTML-Format mit einer Größe von je 1&nbsp;MB haben, fallen für alle Ihre Kund:innen 10&nbsp;MB an Datenkosten an, selbst wenn sie diese Nachrichten nie getriggert haben. Das kann sich im Laufe der Zeit schnell summieren, auch wenn die In-App-Nachrichten zwischengespeichert und nicht von Sitzung zu Sitzung erneut heruntergeladen werden.

Die folgenden Strategien sind hilfreich, um die Dateigrößen gering zu halten:

- Referenzieren Sie in Ihrer App oder Website eingebettete Schriftarten, um Ihre In-App-Nachrichten im HTML-Format anzupassen, anstatt die Schriftdateien in den ZIP-Ordner Ihres HTML-Assets aufzunehmen.
- Vergewissern Sie sich, dass keine überflüssigen oder doppelten CSS- oder JavaScript-Dateien in Ihren HTML-Asset-ZIPs enthalten sind.
- Verwenden Sie [ImageOptim](https://imageoptim.com/) für alle Bilder, um die Bilder auf die kleinstmögliche Größe zu komprimieren, ohne dass die Qualität darunter leidet.

### iPhone-5-Spezifikationen {#iphone-5-specs}

![iPhone-5-Spezifikationen]({% image_buster /assets/img_archive/In-AppMsg_Mockups+Specs_05.png %})

### iPhone-6-Spezifikationen {#iphone-6-specs}

![iPhone-6-Spezifikationen]({% image_buster /assets/img_archive/In-AppMsg_Mockups+Specs_06.png %})