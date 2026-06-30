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
| Eindeutige Impressionen | Die Gesamtzahl der Personen, die die In-App-Nachricht tatsächlich angesehen haben. Wenn eine Nutzer:in die Nachricht am selben Kalendertag in der Zeitzone Ihres Workspace mehr als einmal erhält, wird an diesem Tag nur eine eindeutige Impression gezählt. <br><br> **Wenn die erneute Berechtigung aktiviert ist:** Eindeutige Impressionen können an einem neuen Kalendertag in der Zeitzone Ihres Workspace erneut inkrementiert werden, wenn die Nutzer:in die Trigger-Aktion erneut ausführt. Bei In-App-Nachrichten entsprechen *Eindeutige Impressionen* den *Eindeutigen Empfänger:innen*, da beide an einem neuen Kalendertag inkrementiert werden. |
| Gesamte Impressionen | Die Anzahl der Aufrufe der In-App-Nachricht. Eine Impression wird protokolliert, wenn die Nachricht auf dem Bildschirm sichtbar wird. Wenn eine Nutzer:in die Nachricht zweimal ansieht, wird sie zweimal gezählt. <br><br> **Wenn mehrere Geräte vorhanden sind und die erneute Berechtigung deaktiviert ist:** Die Nutzer:in sieht die In-App-Nachricht nur einmal. Selbst wenn die Nutzer:in mehrere Geräte verwendet, wird sie nur auf dem ersten angesprochenen Gerät angezeigt. Dies setzt voraus, dass das Profil konsolidierte Geräte hat und die Nutzer:in mit einer Nutzer-ID über alle Geräte hinweg angemeldet ist. <br><br> **Wenn die erneute Berechtigung aktiviert ist:** Eine Impression wird jedes Mal protokolliert, wenn die Nutzer:in die In-App-Nachricht sieht. <br><br> **Hinweis:** *Gesamte Impressionen* zählt jede Ansicht. *Eindeutige Empfänger:innen* ist eine separate Metrik, die anhand einer Kalendertag-Grenze in der Zeitzone Ihres Workspace erfasst wird. |
| Conversions | Das Conversion-Tracking beginnt, nachdem eine Nutzer:in eine Impression einer In-App-Nachricht protokolliert hat. Eine Conversion wird gezählt, wenn die Nutzer:in die In-App-Nachrichten-Campaign erhalten und angesehen hat und anschließend das definierte Konversions-Event innerhalb des festgelegten Conversion-Fensters ausführt – unabhängig davon, ob sie auf die Nachricht geklickt hat oder nicht. <br><br> Conversions werden der zuletzt erhaltenen Nachricht zugeordnet. Wenn die erneute Berechtigung aktiviert ist, wird die Conversion der zuletzt erhaltenen In-App-Nachricht zugewiesen, sofern sie innerhalb des definierten Conversion-Fensters erfolgt. Wenn der In-App-Nachricht jedoch bereits eine Conversion zugewiesen wurde, kann für diese spezifische Nachricht keine neue Conversion protokolliert werden. Dadurch wird sichergestellt, dass jede In-App-Nachrichten-Zustellung nur mit einer Conversion verknüpft ist. |
| Gesamte Conversions | Wenn eine Nutzer:in eine In-App-Nachrichten-Campaign nur einmal ansieht, wird nur eine Conversion gezählt, selbst wenn sie das Konversions-Event später mehrfach ausführt. Wenn jedoch die erneute Berechtigung aktiviert ist und die Nutzer:in die In-App-Nachrichten-Campaign mehrfach sieht, können die *Gesamten Conversions* für jede protokollierte Impression einer neuen Instanz der In-App-Nachrichten-Campaign um eins steigen. <br><br> Wenn eine Nutzer:in beispielsweise eine In-App-Nachricht zweimal triggert und nach jeder Impression konvertiert (was zu zwei Conversions führt), steigen die *Gesamten Conversions* um zwei. Wenn es jedoch nur eine Impression gab, gefolgt von zwei Konversions-Events, wird nur eine Conversion protokolliert und die *Gesamten Conversions* steigen um eins. |
| Konversionsrate | Die Metrik der täglichen eindeutigen Impressionen (*Eindeutige Impressionen*) wird zur Berechnung der Konversionsrate verwendet. <br><br> Konversionsrate = (Primäre Conversions) / (Eindeutige Impressionen) <br><br> Bei In-App-Nachrichten können *Eindeutige Impressionen* pro Kalendertag in der Zeitzone Ihres Workspace nur einmal gezählt werden. Die Anzahl der Ausführungen einer gewünschten Aktion (eine „Conversion“) kann innerhalb desselben Kalendertags steigen. Wenn eine Nutzer:in also eine Conversion innerhalb eines Tages mehrfach ausführt, kann die *Konversionsrate* entsprechend steigen, aber *Eindeutige Impressionen* werden für diesen Kalendertag nur einmal gezählt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="In-App-Nachrichten-Metriken" }

{% alert note %}
In A/B-Tests können die *Eindeutigen Impressionen* der Kontrollgruppe die *Eindeutigen Impressionen* der Variante übersteigen, und die *Gesamten Impressionen* der Kontrollgruppe können die *Gesamten Impressionen* der Variante übersteigen, wenn Varianten-Nachrichten Renderzeit benötigen (z. B. große Bilder oder templated Connected-Content). Nutzer:innen, die die Nachricht triggern, aber die App verlassen, bevor die Variante fertig gerendert ist, protokollieren möglicherweise keine Varianten-Impressionen, während die Kontrollgruppe Impressionen ohne das Rendern einer Nachricht protokolliert.
{% endalert %}

## Wie werden Conversions bei erneuter Berechtigung inkrementiert? {#how-do-conversions-increment-with-re-eligibility}

Braze weist jeder In-App-Nachrichten-Zustellung nur eine Conversion zu und ordnet sie der zuletzt erhaltenen Nachricht zu.

Wenn die erneute Berechtigung aktiviert ist, kann jede neue Zustellung ihre eigene Conversion generieren. Wenn eine Nutzer:in beispielsweise dieselbe In-App-Nachricht fünfmal sieht und nach jeder Impression konvertiert, werden fünf Conversions gezählt. Wenn eine Nutzer:in die Nachricht nur einmal sieht, aber danach mehrfach konvertiert, wird nur eine Conversion gezählt.

Wenn eine Nutzer:in eine In-App-Nachricht an zwei verschiedenen Tagen ansieht, aber am dritten Tag konvertiert, protokolliert Braze die Conversion gegen die Impression des zweiten Tages. Bei Canvases werden Conversions pro Canvas-Eintritt erfasst, nicht pro Schritt. Wenn eine Nutzer:in bei mehreren Schritten während desselben Eintritts konvertiert, zählt dies trotzdem nur als eine Conversion.

{% tabs local %}
{% tab Szenario 1 %}

*Eine Nutzer:in erhält dieselbe In-App-Nachricht fünfmal an einem einzigen Tag und konvertiert fünfmal am selben Tag.*

Sarah erhält eine In-App-Nachricht von einer Shopping-App über einen zeitlich begrenzten Sale ihrer Lieblingsschuhmarke. Sie klickt auf die Nachricht und kauft zwei Paar Schuhe.

Ein paar Stunden später erhält sie dieselbe In-App-Nachricht erneut und entscheidet sich, ein weiteres Paar Schuhe zu kaufen. Dies geschieht insgesamt fünfmal an einem einzigen Tag, und Sarah tätigt am Ende fünf separate Käufe, jedes Mal nachdem sie auf die In-App-Nachricht geklickt hat.

**Ergebnisse:** *Gesamte Conversions* und *Gesamte Impressionen* für Sarah werden an diesem einzelnen Tag jeweils um fünf inkrementiert. Da *Eindeutige Impressionen* erst nach einer Kalendertag-Grenze in der Zeitzone des Workspace erneut inkrementiert werden können, bleiben die *Eindeutigen Impressionen* gleich. Dies führt dazu, dass die *Konversionsrate* innerhalb dieses Zeitraums steigt.

{% alert note %}
Jede Impression und Conversion in diesem Szenario wird als separates SDK-Event verarbeitet. Wenn Ihr SDK eine Impression und ein Konversions-Event zusammen bündelt, kann die Conversion-Anzahl abweichen.
{% endalert %}

{% endtab %}
{% tab Szenario 2 %}

*Eine Nutzer:in erhält eine In-App-Nachricht und konvertiert an einem einzigen Tag.*

Lena erhält eine In-App-Nachricht über einen neuen Lernkurs. Sie klickt auf die Nachricht und beginnt den Kurs. Während sie in der App ist, meldet sie sich auch für vier weitere Kurse an. All dies geschieht am selben Tag, nachdem sie nur eine Nachricht erhalten hat.

**Ergebnisse:** *Gesamte Conversions* und *Gesamte Impressionen* für Lena werden jeweils um eins inkrementiert.

{% endtab %}
{% tab Szenario 3 %}

*Eine Nutzer:in erhält eine In-App-Nachricht und konvertiert einen Tag später.*

Tom ist ein regelmäßiger Kunde einer E-Commerce-App. Er erhält eine In-App-Nachricht, die einen zeitlich begrenzten Rabatt auf ein Produkt bewirbt, an dem er interessiert ist. Tom klickt auf die Nachricht, entscheidet sich aber, nicht sofort zu kaufen. Am nächsten Tag erinnert sich Tom an den Rabatt und tätigt den Kauf, der der In-App-Nachricht zugeordnet wird, die er am Vortag erhalten hat.

**Ergebnisse:** *Gesamte Conversions* und *Gesamte Impressionen* für Tom werden jeweils um eins inkrementiert.

{% endtab %}
{% tab Szenario 4 %}

*Eine Nutzer:in erhält eine In-App-Nachricht und konvertiert einen Tag später zweimal.*

Alex hat kürzlich eine Arcade-App heruntergeladen. Eines Tages erhält Alex eine In-App-Nachricht, die dazu ermutigt, ein Level in einem neuen Spiel abzuschließen. Alex klickt auf die Nachricht, wird aber abgelenkt und schließt kein Level ab. Am nächsten Tag schließt Alex zwei Level im selben Spiel ab.

**Ergebnisse:** Da das Abschließen eines Levels das Konversions-Event ist, hat Alex am zweiten Tag zweimal konvertiert. Da Alex jedoch nur eine In-App-Nachricht erhalten hat, werden *Gesamte Conversions* und *Gesamte Impressionen* für Alex jeweils um eins inkrementiert.

{% endtab %}
{% tab Szenario 5 %}

*Eine Nutzer:in erhält dieselbe In-App-Nachricht zweimal an einem einzigen Tag und konvertiert am folgenden Tag zweimal.*

John ist ein vielbeschäftigter Berufstätiger, der eine Liefer-App nutzt, um Essen von seinen Lieblingsrestaurants zu bestellen. Auf dem Weg zur Arbeit triggert er einen Geofence und erhält eine In-App-Nachricht, die Restaurants in der Nähe bewirbt. Als er später nach Hause fährt, erhält er dieselbe Nachricht erneut, da die erneute Berechtigung aktiviert ist. Obwohl ihm die Angebote gefallen, entscheidet er sich, an diesem Tag nichts zu bestellen.

Am nächsten Tag bestellt John Mittag- und Abendessen über die App und führt das Konversions-Event zweimal aus.

**Ergebnisse:** *Gesamte Conversions* für John wird um eins inkrementiert, und *Gesamte Impressionen* wird um zwei inkrementiert. Da die erneute Berechtigung aktiviert ist, wird die Conversion der zuletzt erhaltenen In-App-Nachricht von John zugewiesen (der zweiten Impression). Eine Conversion kann für jede In-App-Nachrichten-Zustellung nur einmal protokolliert werden.

{% endtab %}
{% endtabs %}