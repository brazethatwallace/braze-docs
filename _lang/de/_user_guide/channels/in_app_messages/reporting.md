---
nav_title: Reporting
article_title: In-App-Nachrichten-Reporting
page_order: 21
description: "Dieser Referenzartikel behandelt das Reporting und die Analytics für In-App-Nachrichten, einschließlich Kampagnendetails, Nachrichten-Performance und historischer Performance."
channel:
  - in-app messages
tool:
  - Reports

---

# In-App-Nachrichten-Reporting {#iam-reporting}

> Dieser Referenzartikel behandelt das Reporting und die Analytics für In-App-Nachrichten, einschließlich Kampagnendetails, Nachrichten-Performance und historischer Performance.

{% multi_lang_include analytics/campaign_analytics.md channel="in-app message" %}

## In-App-Nachricht-Metriken {#in-app-message-metrics}

Hier finden Sie die wichtigsten Metriken für In-App-Nachrichten, die in Ihren Analytics angezeigt werden können. Definitionen aller in Braze verwendeten Metriken finden Sie im [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/analytics/metrics_glossary).

{% alert note %}
Für In-App-Nachrichten definiert diese Seite eindeutige Impressionen anhand einer Kalendertag-Grenze in der Zeitzone Ihres Workspace.
{% endalert %}

| Begriff | Definition |
| --- | --- |
| Eindeutige Impressionen | Die Gesamtzahl der Personen, die die In-App-Nachricht tatsächlich angesehen haben. Wenn Nutzer:innen die Nachricht am selben Kalendertag in der Zeitzone Ihres Workspace mehr als einmal erhalten, wird an diesem Tag nur eine eindeutige Impression gezählt. <br><br> **Wenn die erneute Berechtigung aktiviert ist:** Eindeutige Impressionen können an einem neuen Kalendertag in der Zeitzone Ihres Workspace erneut inkrementiert werden, wenn die Nutzer:innen die Trigger-Aktion erneut ausführen. Bei In-App-Nachrichten entspricht *Eindeutige Impressionen* den *Eindeutigen Empfänger:innen*, da beide an einem neuen Kalendertag inkrementiert werden. |
| Gesamte Impressionen | Die Anzahl der Aufrufe der In-App-Nachricht. Eine Impression wird protokolliert, wenn die Nachricht auf dem Bildschirm sichtbar wird. Wenn Nutzer:innen die Nachricht zweimal ansehen, werden sie zweimal gezählt. <br><br> **Wenn mehrere Geräte vorhanden sind und die erneute Berechtigung deaktiviert ist:** Die Nutzer:innen sehen die In-App-Nachricht nur einmal. Selbst wenn sie mehrere Geräte verwenden, sehen sie die Nachricht nur auf dem zuerst angesprochenen Gerät. Dies setzt voraus, dass das Profil konsolidierte Geräte hat und die Nutzer:innen mit einer Nutzer-ID auf allen Geräten angemeldet sind. <br><br> **Wenn die erneute Berechtigung aktiviert ist:** Eine Impression wird jedes Mal protokolliert, wenn die Nutzer:innen die In-App-Nachricht sehen. <br><br> **Hinweis:** *Gesamte Impressionen* zählt jeden Aufruf. *Eindeutige Empfänger:innen* ist eine separate Metrik, die anhand einer Kalendertag-Grenze in der Zeitzone Ihres Workspace erfasst wird. |
| Konversionen | Das Konversions-Tracking beginnt, nachdem Nutzer:innen eine Impression einer In-App-Nachricht protokolliert haben. Eine Konversion wird gezählt, wenn die Nutzer:innen die In-App-Nachricht-Campaign erhalten und angesehen haben und anschließend das spezifische Konversions-Event innerhalb des definierten Konversionsfensters ausführen – unabhängig davon, ob sie auf die Nachricht geklickt haben oder nicht. <br><br> Konversionen werden der zuletzt empfangenen Nachricht zugeordnet. Wenn die erneute Berechtigung aktiviert ist, wird die Konversion der zuletzt empfangenen In-App-Nachricht zugewiesen, sofern sie innerhalb des definierten Konversionsfensters erfolgt. Wurde der In-App-Nachricht jedoch bereits eine Konversion zugewiesen, kann für diese spezifische Nachricht keine neue Konversion protokolliert werden. Dadurch wird sichergestellt, dass jede In-App-Nachricht-Zustellung nur mit einer Konversion verknüpft ist. |
| Gesamte Konversionen | Wenn Nutzer:innen eine In-App-Nachricht-Campaign nur einmal ansehen, wird nur eine Konversion gezählt, selbst wenn sie das Konversions-Event später mehrfach ausführen. Wenn jedoch die erneute Berechtigung aktiviert ist und die Nutzer:innen die In-App-Nachricht-Campaign mehrfach sehen, kann *Gesamte Konversionen* für jede protokollierte Impression einer neuen Instanz der In-App-Nachricht-Campaign um eins steigen. <br><br> Wenn Nutzer:innen beispielsweise eine In-App-Nachricht zweimal triggern und nach jeder Impression konvertieren (was zu zwei Konversionen führt), steigt *Gesamte Konversionen* um zwei. Wenn es jedoch nur eine Impression gab, gefolgt von zwei Konversions-Events, wird nur eine Konversion protokolliert und *Gesamte Konversionen* steigt um eins. |
| Konversionsrate | Die Metrik der täglichen eindeutigen Impressionen (*Eindeutige Impressionen*) wird zur Berechnung der Konversionsrate verwendet. <br><br> Konversionsrate = (Primäre Konversionen) / (Eindeutige Impressionen) <br><br> Bei In-App-Nachrichten können *Eindeutige Impressionen* pro Kalendertag in der Zeitzone Ihres Workspace nur einmal gezählt werden. Die Anzahl der Ausführungen einer gewünschten Aktion (eine „Konversion“) kann innerhalb desselben Kalendertags steigen. Wenn Nutzer:innen also innerhalb eines Tages mehrfach konvertieren, kann die *Konversionsrate* entsprechend steigen, aber *Eindeutige Impressionen* werden für diesen Kalendertag nur einmal gezählt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="In-App-Nachricht-Metriken" }

{% alert tip %}
*Gesamte Impressionen* können *Eindeutige Impressionen* übersteigen, wenn Nutzer:innen die Nachricht am selben Kalendertag mehr als einmal ansehen (siehe die Metrikdefinitionen in der obigen Tabelle). Um Nutzer:innen mit überhöhten Impressionszahlen zu untersuchen, erstellen Sie ein Segment mit dem Filter **Geräteanzahl** auf **mehr als** `1` und dem Filter **Nachricht von Campaign erhalten** für die spezifische Campaign.
{% endalert %}

### Klick-Tracking {#click-tracking}

Braze protokolliert eine Impression, wenn eine In-App-Nachricht auf dem Bildschirm sichtbar wird. Für In-App-Nachrichten, die mit dem [traditionellen Editor]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional) erstellt wurden, zeigt die folgende Tabelle, was als Klick gezählt wird.

| Nutzeraktion | Klick protokolliert |
|-------------|--------------|
| Nutzer:innen klicken auf den Nachrichtentext, wenn die Nachricht keine Buttons hat | Ja (Body-Klick) |
| Nutzer:innen klicken auf einen Button | Ja (Button-Klick) |
| Nutzer:innen klicken auf den Schließen-Button (X) | Nein |
| Nutzer:innen tippen oder klicken außerhalb der Nachricht, um sie zu schließen (wenn aktiviert) | Nein |
| Nutzer:innen schließen die App, während die Nachricht angezeigt wird | Nein |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Klick-Tracking" }

#### Vollbild-Nachricht-Metriken nach Nutzeraktion {#fullscreen-metrics-by-user-action}

Für [Vollbild]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/fullscreen)-In-App-Nachrichten, die mit dem traditionellen Editor erstellt wurden, zeigt die folgende Tabelle, was Braze bei gängigen Nutzeraktionen protokolliert. Eine Impression wird protokolliert, wenn die Nachricht auf dem Bildschirm sichtbar wird.

| Nutzeraktion | Vollbild mit Buttons | Vollbild ohne Buttons |
| --- | --- | --- |
| Nutzer:innen sehen eine In-App-Nachricht, klicken nichts und schließen die App | 1 Impression | 1 Impression |
| Nutzer:innen sehen eine In-App-Nachricht und klicken den Schließen-Button | 1 Impression | 1 Impression |
| Nutzer:innen sehen eine In-App-Nachricht und klicken einen CTA-Button | 1 Button-Klick und 1 Impression | N/A |
| Nutzer:innen sehen eine In-App-Nachricht und tippen auf den Bildschirm, aber nicht auf einen Button | 1 Impression<br><br>Das Tippen auf die In-App-Nachricht schließt die Nachricht nicht | 1 Body-Klick und 1 Impression<br><br>Das Tippen auf die In-App-Nachricht schließt die Nachricht oder löst das On-Click-Verhalten aus |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Vollbild-In-App-Nachricht-Metriken nach Nutzerverhalten" }

{% alert note %}
Body-Klicks werden für In-App-Nachrichten, die mit dem [Drag-and-Drop-Editor]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop) erstellt wurden, nicht automatisch erfasst. Um Body-Klicks zu protokollieren, fügen Sie einen **Custom Code**-Block hinzu und rufen Sie `brazeBridge.logClick()` auf. Weitere Details finden Sie unter [Button-Tracking]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#button-tracking-improvements) und [JavaScript-Bridge]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#javascript-bridge).
{% endalert %}

Definitionen von Body-Klicks und Button-Klicks finden Sie im [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/analytics/metrics_glossary).

Informationen zu Ungleichgewichten bei Impressionen zwischen Kontrollgruppe und Variante in A/B-Tests finden Sie unter [Diskrepanzen zwischen Kontrollgruppe und Variante]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics#discrepancies-between-the-control-group-and-variant).

## Wie werden Konversionen bei erneuter Berechtigung gezählt? {#how-do-conversions-increment-with-re-eligibility}

Braze ordnet jeder In-App-Nachrichten-Zustellung nur eine Konversion zu und schreibt sie der zuletzt empfangenen Nachricht zu.

Wenn die erneute Berechtigung aktiviert ist, kann jede neue Zustellung eine eigene Konversion erzeugen. Wenn beispielsweise ein:e Nutzer:in dieselbe In-App-Nachricht fünfmal sieht und nach jeder Impression konvertiert, werden fünf Konversionen gezählt. Wenn ein:e Nutzer:in die Nachricht nur einmal sieht, aber danach mehrfach konvertiert, wird nur eine Konversion gezählt.

Wenn ein:e Nutzer:in eine In-App-Nachricht an zwei verschiedenen Tagen sieht, aber am dritten Tag konvertiert, protokolliert Braze die Konversion für die Impression des zweiten Tages. Bei Canvases werden Konversionen pro Canvas-Entry erfasst, nicht pro Schritt. Wenn ein:e Nutzer:in bei mehreren Schritten während desselben Entrys konvertiert, zählt dies trotzdem nur als eine Konversion.

{% tabs local %}
{% tab Szenario 1 %}

*Ein:e Nutzer:in erhält dieselbe In-App-Nachricht fünfmal an einem einzigen Tag und konvertiert fünfmal am selben Tag.*

Sarah erhält eine In-App-Nachricht von einer Shopping-App über einen zeitlich begrenzten Sale ihrer Lieblingsschuhmarke. Sie klickt auf die Nachricht und kauft zwei Paar Schuhe.

Ein paar Stunden später erhält sie dieselbe In-App-Nachricht erneut und entscheidet sich, ein weiteres Paar Schuhe zu kaufen. Dies geschieht insgesamt fünfmal an einem einzigen Tag, und Sarah tätigt am Ende fünf separate Käufe, jedes Mal nachdem sie auf die In-App-Nachricht geklickt hat.

**Ergebnisse:** *Total Conversions* und *Total Impressions* für Sarah erhöhen sich jeweils um fünf für diesen einzelnen Tag. Da *Unique Impressions* erst nach einer Kalendertagsgrenze in der Zeitzone des Workspace erneut erhöht werden können, bleibt *Unique Impressions* gleich. Dies führt dazu, dass die *Conversion Rate* innerhalb dieses Zeitraums steigt.

{% alert note %}
Jede Impression und Konversion in diesem Szenario wird als separates SDK-Event verarbeitet. Wenn Ihr SDK ein Impressions- und ein Konversions-Event zusammen bündelt, kann die Konversionsanzahl abweichen.
{% endalert %}

{% endtab %}
{% tab Szenario 2 %}

*Ein:e Nutzer:in erhält eine In-App-Nachricht und konvertiert an einem einzigen Tag.*

Lena erhält eine In-App-Nachricht über einen neuen Lernkurs. Sie klickt auf die Nachricht und beginnt den Kurs. Während sie in der App ist, meldet sie sich auch für vier weitere Kurse an. All dies geschieht am selben Tag, nachdem sie nur eine Nachricht erhalten hat.

**Ergebnisse:** *Total Conversions* und *Total Impressions* für Lena erhöhen sich jeweils um eins.

{% endtab %}
{% tab Szenario 3 %}

*Ein:e Nutzer:in erhält eine In-App-Nachricht und konvertiert einen Tag später.*

Tom ist ein regelmäßiger Kunde einer E-Commerce-App. Er erhält eine In-App-Nachricht, die einen zeitlich begrenzten Rabatt auf ein Produkt bewirbt, an dem er interessiert ist. Tom klickt auf die Nachricht, entscheidet sich aber, nicht sofort zu kaufen. Am nächsten Tag erinnert sich Tom an den Rabatt und tätigt den Kauf, der der In-App-Nachricht zugeschrieben wird, die er am Vortag erhalten hat.

**Ergebnisse:** *Total Conversions* und *Total Impressions* für Tom erhöhen sich jeweils um eins.

{% endtab %}
{% tab Szenario 4 %}

*Ein:e Nutzer:in erhält eine In-App-Nachricht und konvertiert zweimal einen Tag später.*

Alex hat kürzlich eine Arcade-App heruntergeladen. Eines Tages erhält Alex eine In-App-Nachricht, die dazu ermutigt, ein Level in einem neuen Spiel abzuschließen. Alex klickt auf die Nachricht, wird aber abgelenkt und schließt kein Level ab. Am nächsten Tag schließt Alex zwei Level im selben Spiel ab.

**Ergebnisse:** Da das Abschließen eines Levels das Konversions-Event ist, hat Alex am zweiten Tag zweimal konvertiert. Da jedoch nur eine In-App-Nachricht empfangen wurde, erhöhen sich *Total Conversions* und *Total Impressions* für Alex jeweils nur um eins.

{% endtab %}
{% tab Szenario 5 %}

*Ein:e Nutzer:in erhält dieselbe In-App-Nachricht zweimal an einem einzigen Tag und konvertiert am folgenden Tag zweimal.*

John ist ein vielbeschäftigter Berufstätiger, der eine Liefer-App nutzt, um Essen von seinen Lieblingsrestaurants zu bestellen. Auf dem Weg zur Arbeit triggert er einen Geofence und erhält eine In-App-Nachricht, die Restaurants in der Nähe bewirbt. Als er später nach Hause fährt, erhält er dieselbe Nachricht erneut, da die erneute Berechtigung aktiviert ist. Obwohl ihm die Angebote gefallen, entscheidet er sich, an diesem Tag nichts zu bestellen.

Am nächsten Tag bestellt John Mittag- und Abendessen über die App und führt das Konversions-Event zweimal aus.

**Ergebnisse:** *Total Conversions* für John erhöht sich um eins, und *Total Impressions* erhöht sich um zwei. Da die erneute Berechtigung aktiviert ist, wird die Konversion der letzten In-App-Nachricht zugeordnet, die John erhalten hat (der zweiten Impression). Eine Konversion kann pro In-App-Nachrichten-Zustellung nur einmal protokolliert werden.

{% endtab %}
{% endtabs %}