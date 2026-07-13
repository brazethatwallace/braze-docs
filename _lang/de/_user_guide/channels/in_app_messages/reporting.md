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

## In-App-Nachrichten-Metriken {#in-app-message-metrics}

Hier finden Sie die wichtigsten Metriken für In-App-Nachrichten, die in Ihren Analytics angezeigt werden können. Definitionen aller in Braze verwendeten Metriken finden Sie im [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/analytics/metrics_glossary).

{% alert note %}
Für In-App-Nachrichten definiert diese Seite eindeutige Impressionen anhand einer Kalendertag-Grenze in der Zeitzone Ihres Workspace.
{% endalert %}

| Begriff | Definition |
| --- | --- |
| Eindeutige Impressionen | Die Gesamtzahl der Personen, die die In-App-Nachricht tatsächlich angesehen haben. Wenn Nutzer:innen die Nachricht am selben Kalendertag in der Zeitzone Ihres Workspace mehr als einmal erhalten, wird an diesem Tag nur eine eindeutige Impression gezählt. <br><br> **Wenn die erneute Berechtigung aktiviert ist:** Eindeutige Impressionen können an einem neuen Kalendertag in der Zeitzone Ihres Workspace erneut inkrementiert werden, wenn Nutzer:innen die Trigger-Aktion erneut ausführen. Bei In-App-Nachrichten entsprechen *Eindeutige Impressionen* den *Eindeutigen Empfänger:innen*, da beide an einem neuen Kalendertag inkrementiert werden. |
| Gesamte Impressionen | Die Anzahl der Aufrufe der In-App-Nachricht. Eine Impression wird protokolliert, wenn die Nachricht auf dem Bildschirm sichtbar wird. Wenn Nutzer:innen die Nachricht zweimal ansehen, werden sie zweimal gezählt. <br><br> **Wenn mehrere Geräte vorhanden sind und die erneute Berechtigung deaktiviert ist:** Nutzer:innen sehen die In-App-Nachricht nur einmal. Selbst wenn sie mehrere Geräte verwenden, wird die Nachricht nur auf dem ersten angesprochenen Gerät angezeigt. Dies setzt voraus, dass das Profil konsolidierte Geräte hat und Nutzer:innen mit einer Nutzer-ID über alle Geräte hinweg angemeldet sind. <br><br> **Wenn die erneute Berechtigung aktiviert ist:** Eine Impression wird jedes Mal protokolliert, wenn Nutzer:innen die In-App-Nachricht sehen. <br><br> **Hinweis:** *Gesamte Impressionen* zählt jede Ansicht. *Eindeutige Empfänger:innen* ist eine separate Metrik, die anhand einer Kalendertag-Grenze in der Zeitzone Ihres Workspace erfasst wird. |
| Conversions | Das Conversion-Tracking beginnt, nachdem Nutzer:innen eine Impression einer In-App-Nachricht protokolliert haben. Eine Conversion wird gezählt, wenn Nutzer:innen die In-App-Nachrichten-Campaign erhalten und angesehen haben und anschließend das definierte Konversions-Event innerhalb des festgelegten Conversion-Fensters ausführen – unabhängig davon, ob sie auf die Nachricht geklickt haben oder nicht. <br><br> Conversions werden der zuletzt erhaltenen Nachricht zugeordnet. Wenn die erneute Berechtigung aktiviert ist, wird die Conversion der zuletzt erhaltenen In-App-Nachricht zugewiesen, sofern sie innerhalb des definierten Conversion-Fensters erfolgt. Wenn der In-App-Nachricht jedoch bereits eine Conversion zugewiesen wurde, kann für diese spezifische Nachricht keine neue Conversion protokolliert werden. Dadurch wird sichergestellt, dass jede In-App-Nachrichten-Zustellung nur mit einer Conversion verknüpft ist. |
| Gesamte Conversions | Wenn Nutzer:innen eine In-App-Nachrichten-Campaign nur einmal ansehen, wird nur eine Conversion gezählt, selbst wenn sie das Konversions-Event später mehrfach ausführen. Wenn jedoch die erneute Berechtigung aktiviert ist und Nutzer:innen die In-App-Nachrichten-Campaign mehrfach sehen, können die *Gesamten Conversions* für jede protokollierte Impression einer neuen Instanz der In-App-Nachrichten-Campaign um eins steigen. <br><br> Wenn Nutzer:innen beispielsweise eine In-App-Nachricht zweimal triggern und nach jeder Impression konvertieren (was zu zwei Conversions führt), steigen die *Gesamten Conversions* um zwei. Wenn es jedoch nur eine Impression gab, gefolgt von zwei Konversions-Events, wird nur eine Conversion protokolliert und die *Gesamten Conversions* steigen um eins. |
| Konversionsrate | Die Metrik der täglichen eindeutigen Impressionen (*Eindeutige Impressionen*) wird zur Berechnung der Konversionsrate verwendet. <br><br> Konversionsrate = (Primäre Conversions) / (Eindeutige Impressionen) <br><br> Bei In-App-Nachrichten können *Eindeutige Impressionen* pro Kalendertag in der Zeitzone Ihres Workspace nur einmal gezählt werden. Die Anzahl der Ausführungen einer gewünschten Aktion (eine „Conversion“) kann innerhalb desselben Kalendertags steigen. Wenn Nutzer:innen also eine Conversion innerhalb eines Tages mehrfach ausführen, kann die *Konversionsrate* entsprechend steigen, aber *Eindeutige Impressionen* werden für diesen Kalendertag nur einmal gezählt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="In-App-Nachrichten-Metriken" }

{% alert tip %}
*Gesamte Impressionen* können *Eindeutige Impressionen* übersteigen, wenn Nutzer:innen die Nachricht am selben Kalendertag mehr als einmal ansehen (siehe die Metrikdefinitionen in der obigen Tabelle). Um Nutzer:innen mit überhöhten Impression-Zahlen zu untersuchen, erstellen Sie ein Segment mit dem Filter **Device Count** auf **more than** `1` und dem Filter **Received Message from Campaign** für die jeweilige Campaign.
{% endalert %}

Informationen zu Ungleichgewichten bei Impressionen zwischen Kontrollgruppe und Variante in A/B-Tests finden Sie unter [Diskrepanzen zwischen Kontrollgruppe und Variante]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics#discrepancies-between-the-control-group-and-variant).

## Wie werden Conversions bei erneuter Berechtigung inkrementiert? {#how-do-conversions-increment-with-re-eligibility}

Braze weist jeder In-App-Nachrichten-Zustellung nur eine Conversion zu und ordnet sie der zuletzt erhaltenen Nachricht zu.

Wenn die erneute Berechtigung aktiviert ist, kann jede neue Zustellung ihre eigene Conversion generieren. Wenn Nutzer:innen beispielsweise dieselbe In-App-Nachricht fünfmal sehen und nach jeder Impression konvertieren, werden fünf Conversions gezählt. Wenn Nutzer:innen die Nachricht nur einmal sehen, aber danach mehrfach konvertieren, wird nur eine Conversion gezählt.

Wenn Nutzer:innen eine In-App-Nachricht an zwei verschiedenen Tagen ansehen, aber am dritten Tag konvertieren, protokolliert Braze die Conversion gegen die Impression des zweiten Tages. Bei Canvases werden Conversions pro Canvas-Eintritt erfasst, nicht pro Schritt. Wenn Nutzer:innen bei mehreren Schritten während desselben Eintritts konvertieren, zählt dies trotzdem nur als eine Conversion.

{% tabs local %}
{% tab Szenario 1 %}

*Nutzer:innen erhalten dieselbe In-App-Nachricht fünfmal an einem einzigen Tag und konvertieren fünfmal am selben Tag.*

Sarah erhält eine In-App-Nachricht von einer Shopping-App über einen zeitlich begrenzten Sale ihrer Lieblingsschuhmarke. Sie klickt auf die Nachricht und kauft zwei Paar Schuhe.

Ein paar Stunden später erhält sie dieselbe In-App-Nachricht erneut und entscheidet sich, ein weiteres Paar Schuhe zu kaufen. Dies geschieht insgesamt fünfmal an einem einzigen Tag, und Sarah tätigt am Ende fünf separate Käufe, jedes Mal nachdem sie auf die In-App-Nachricht geklickt hat.

**Ergebnisse:** *Gesamte Conversions* und *Gesamte Impressionen* für Sarah werden an diesem einzelnen Tag jeweils um fünf inkrementiert. Da *Eindeutige Impressionen* erst nach einer Kalendertag-Grenze in der Zeitzone des Workspace erneut inkrementiert werden können, bleiben die *Eindeutigen Impressionen* gleich. Dies führt dazu, dass die *Konversionsrate* innerhalb dieses Zeitraums steigt.

{% alert note %}
Jede Impression und Conversion in diesem Szenario wird als separates SDK-Ereignis verarbeitet. Wenn Ihr SDK eine Impression und ein Konversions-Event zusammen bündelt, kann die Conversion-Anzahl abweichen.
{% endalert %}

{% endtab %}
{% tab Szenario 2 %}

*Nutzer:innen erhalten eine In-App-Nachricht und konvertieren an einem einzigen Tag.*

Lena erhält eine In-App-Nachricht über einen neuen Lernkurs. Sie klickt auf die Nachricht und beginnt den Kurs. Während sie in der App ist, meldet sie sich auch für vier weitere Kurse an. All dies geschieht am selben Tag, nachdem sie nur eine Nachricht erhalten hat.

**Ergebnisse:** *Gesamte Conversions* und *Gesamte Impressionen* für Lena werden jeweils um eins inkrementiert.

{% endtab %}
{% tab Szenario 3 %}

*Nutzer:innen erhalten eine In-App-Nachricht und konvertieren einen Tag später.*

Tom ist ein regelmäßiger Kunde einer E-Commerce-App. Er erhält eine In-App-Nachricht, die einen zeitlich begrenzten Rabatt auf ein Produkt bewirbt, an dem er interessiert ist. Tom klickt auf die Nachricht, entscheidet sich aber, nicht sofort zu kaufen. Am nächsten Tag erinnert sich Tom an den Rabatt und tätigt den Kauf, der der In-App-Nachricht zugeordnet wird, die er am Vortag erhalten hat.

**Ergebnisse:** *Gesamte Conversions* und *Gesamte Impressionen* für Tom werden jeweils um eins inkrementiert.

{% endtab %}
{% tab Szenario 4 %}

*Nutzer:innen erhalten eine In-App-Nachricht und konvertieren einen Tag später zweimal.*

Alex hat kürzlich eine Arcade-App heruntergeladen. Eines Tages erhält Alex eine In-App-Nachricht, die dazu ermutigt, ein Level in einem neuen Spiel abzuschließen. Alex klickt auf die Nachricht, wird aber abgelenkt und schließt kein Level ab. Am nächsten Tag schließt Alex zwei Level im selben Spiel ab.

**Ergebnisse:** Da das Abschließen eines Levels das Konversions-Event ist, hat Alex am zweiten Tag zweimal konvertiert. Da Alex jedoch nur eine In-App-Nachricht erhalten hat, werden *Gesamte Conversions* und *Gesamte Impressionen* für Alex jeweils um eins inkrementiert.

{% endtab %}
{% tab Szenario 5 %}

*Nutzer:innen erhalten dieselbe In-App-Nachricht zweimal an einem einzigen Tag und konvertieren am folgenden Tag zweimal.*

John ist ein vielbeschäftigter Berufstätiger, der eine Liefer-App nutzt, um Essen von seinen Lieblingsrestaurants zu bestellen. Auf dem Weg zur Arbeit triggert er einen Geofence und erhält eine In-App-Nachricht, die Restaurants in der Nähe bewirbt. Als er später nach Hause fährt, erhält er dieselbe Nachricht erneut, da die erneute Berechtigung aktiviert ist. Obwohl ihm die Angebote gefallen, entscheidet er sich, an diesem Tag nichts zu bestellen.

Am nächsten Tag bestellt John Mittag- und Abendessen über die App und führt das Konversions-Event zweimal aus.

**Ergebnisse:** *Gesamte Conversions* für John wird um eins inkrementiert, und *Gesamte Impressionen* wird um zwei inkrementiert. Da die erneute Berechtigung aktiviert ist, wird die Conversion der zuletzt erhaltenen In-App-Nachricht von John zugewiesen (der zweiten Impression). Eine Conversion kann für jede In-App-Nachrichten-Zustellung nur einmal protokolliert werden.

{% endtab %}
{% endtabs %}