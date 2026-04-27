---
nav_title: Antworten zwischenspeichern
article_title: Connected-Content-Antworten zwischenspeichern
page_order: 2.5
description: "Dieser Artikel beschreibt, wie Sie Connected-Content-Antworten über verschiedene Kampagnen oder Nachrichten im selben Workspace zwischenspeichern können, um die Sendegeschwindigkeit zu optimieren."
---

# Connected-Content-Antworten zwischenspeichern

> Connected-Content-Antworten können über verschiedene Kampagnen oder Nachrichten (im selben Workspace) zwischengespeichert werden, um die Sendegeschwindigkeit zu optimieren.

Braze speichert Connected-Content-**Antwortkörper** nicht dauerhaft. Während des Nachrichten-Renderings können Antworten vorübergehend gehalten werden (zum Beispiel im Arbeitsspeicher und im Cache), damit Braze Liquid rendern und die Nachricht senden kann.

Um das Caching zu verhindern, können Sie `:no_cache` angeben, was zu erhöhtem Netzwerkverkehr führen kann. Zur Fehlerbehebung und Überwachung des Systemzustands protokolliert Braze Connected-Content-Anfragemetadaten (wie die vollständig gerenderte Anfrage-URL und den Antwortstatuscode) für erfolgreiche und fehlgeschlagene Aufrufe. Diese Protokolle werden bis zu 30 Tage aufbewahrt.

{% details Connected-Content-Rendering und Datenverarbeitung (erweitert) %}
Dieser Abschnitt bietet einen detaillierteren End-to-End-Überblick darüber, wie Braze Liquid und Connected-Content rendert und wo Daten vorübergehend existieren können, bevor eine Nachricht gesendet wird. Dies kann bei Datenschutz- und Datenverarbeitungsprüfungen hilfreich sein.

#### Was gespeichert wird und was nicht

- **Connected-Content-Antwortkörper:** Wird von Braze nicht dauerhaft gespeichert. Er kann vorübergehend im Arbeitsspeicher gehalten und, wenn Caching aktiviert ist, im Cache mit einer Time-to-Live (TTL) gespeichert werden.
- **Connected-Content-Anfragemetadaten:** Anfragemetadaten wie die vollständig gerenderte URL, der HTTP-Statuscode und die Antwortdauer werden zur Fehlerbehebung und Überwachung protokolliert. Diese Protokolle werden bis zu 30 Tage aufbewahrt.
- **Endgültig gerenderte Nachricht:** Existiert während des Renderings im Arbeitsspeicher. Diese kann je nach Ihrer Konfiguration und dem Kanal auch an anderer Stelle gespeichert werden (zum Beispiel Nachrichtenarchivierung oder Content-Cards).

#### Rendering-Ablauf (Überblick)

Der folgende Ablauf beschreibt, wie Braze Nachrichten für anbieterbasierte Kanäle wie E-Mail, SMS und Push rendert und sendet. SDK-basierte Kanäle wie Content-Cards verwenden dasselbe zugrunde liegende Liquid- und Connected-Content-Rendering, unterscheiden sich jedoch darin, wann der Inhalt generiert und wie er zugestellt wird.

1. Ein Hintergrund-Worker rendert das Liquid-Template für eine Nachricht, wenn die Nachricht zur Zustellung vorbereitet wird.
2. Connected-Content-Tags werden während des Liquid-Renderings ausgewertet.
3. Für jedes Connected-Content-Tag prüft Braze einen mehrstufigen Cache. Wenn kein zwischengespeicherter Wert vorhanden ist (oder Caching deaktiviert ist), ruft Braze Ihren Endpunkt auf und empfängt die Antwort.
4. Die Antwort wird in das Liquid-Template eingespeist und die Nachricht wird vollständig gerendert.
5. Bei anbieterbasierten Kanälen wird die gerenderte Nachricht an den Kanalanbieter und dann an die Nutzer:innen gesendet. Bei SDK-basierten Kanälen wie Content-Cards wird der gerenderte Inhalt mit dem Braze SDK synchronisiert und kann bei der ersten Impression oder Anzeigezeit generiert werden, woraufhin er den Nutzer:innen angezeigt wird.

#### Wo Connected-Content-Antworten vorübergehend existieren können

Braze verwendet einen mehrstufigen Cache für Connected-Content-Antworten mit TTLs zwischen fünf Minuten und vier Stunden, abhängig von Ihrer Verwendung von `:cache_max_age` und anderen Caching-Regeln:

- **In-Process-Arbeitsspeicher-Cache:** Transienter Cache innerhalb des Worker-Prozesses. Daten können nur für die Dauer des Jobs existieren (bis zu ~11 Minuten basierend auf dem Worker-Timeout).
- **Lokaler Maschinen-Cache:** Ein Pro-Worker-Cache, wie eine lokale Memcached-Instanz.
- **Clusterweiter Cache:** Ein verteilter Cache, der über Worker hinweg geteilt wird, wie ein Memcached-Cluster.

Diese Cache-Schichten sind flüchtig und können Daten früher als die konfigurierte TTL entfernen.

#### Was sich ändert, wenn Sie `:no_cache` verwenden

Für Endpunkte, die nicht innerhalb der Braze-Infrastruktur gehostet werden, verhindert die Verwendung von `:no_cache`, dass der Connected-Content-Antwortkörper in Memcached gespeichert wird. In diesen Fällen existiert die Antwort nur im Arbeitsspeicher des Worker-Prozesses für die Dauer des Rendering-Jobs (bis zu ~11 Minuten). Für Endpunkte, die zu Braze-internen Hosts aufgelöst werden, können Antworten weiterhin wie unter [Cache-Busting](#cache-busting) beschrieben zwischengespeichert werden.

#### Wo die endgültig gerenderte Ausgabe existieren kann

- **Nachrichtenarchivierung:** Wenn die Nachrichtenarchivierung aktiviert ist, kann Braze die endgültig gerenderte Nachricht in Ihren konfigurierten Cloud-Speicher-Bucket schreiben. Wenn Ihre Connected-Content-Antwort in der gerenderten Nachricht enthalten ist, wird sie in der archivierten Kopie enthalten sein.
- **Nutzergeräte:** Nach der Zustellung kann der vollständig gerenderte Nachrichteninhalt für eine unbestimmte Zeit auf Nutzergeräten verbleiben.
- **Content-Cards:** Gerenderter Inhalt für Content-Cards wird in einer Braze-Datenbank gespeichert, bis die Card abläuft.
{% enddetails %}

## Standard-Cache-Einstellungen

Die Cache-Dauer beträgt bis zu fünf Minuten (300 Sekunden). Sie können dies aktualisieren, indem Sie den Parameter `:cache_max_age` zum Connected-Content-Aufruf hinzufügen. Ein Beispiel:

{% raw %}
```
{{ {% connected_content [https://example.com/webservice.json] :cache_max_age 900 %}}}
```
{% endraw %}

GET-Anfragen werden zwischengespeichert. Sie können dies konfigurieren, indem Sie den Parameter `:no_cache` zum Connected-Content-Aufruf hinzufügen.

POST-Anfragen werden standardmäßig nicht zwischengespeichert, können aber durch Hinzufügen des Parameters `:cache_max_age` zum Connected-Content-Aufruf zwischengespeichert werden. Die minimale Cache-Zeit beträgt 5 Minuten und die maximale Cache-Zeit beträgt 4 Stunden.

{% alert note %}
Cache-Einstellungen sind nicht garantiert. Caching kann Aufrufe an Ihre Endpunkte reduzieren, daher empfehlen wir, mehrere Aufrufe pro Endpunkt innerhalb der Cache-Dauer zu verwenden, anstatt sich übermäßig auf das Caching zu verlassen.
{% endalert %}

### Cache-Größenlimit

Der Connected-Content-Antwortkörper kann bis zu 1&nbsp;MB groß sein. Wenn der Antwortkörper größer als 1&nbsp;MB ist, wird er nicht zwischengespeichert.

## Cache-Zeit

Connected-Content speichert den von GET-Endpunkten zurückgegebenen Wert für mindestens fünf Minuten zwischen. Wenn keine Cache-Zeit angegeben ist, beträgt die Standard-Cache-Zeit fünf Minuten.

Die Connected-Content-Cache-Zeit kann mit `:cache_max_age` verlängert werden, wie im folgenden Beispiel gezeigt. Die minimale Cache-Zeit beträgt fünf Minuten und die maximale Cache-Zeit beträgt vier Stunden. Connected-Content-Daten werden im Arbeitsspeicher mithilfe eines flüchtigen Cache-Systems wie Memcached zwischengespeichert.

Daher können Connected-Content-Daten unabhängig von der angegebenen Cache-Zeit früher als angegeben aus dem Braze-Arbeitsspeicher-Cache entfernt werden. Das bedeutet, dass die Cache-Dauern Richtwerte sind und möglicherweise nicht die tatsächliche Dauer darstellen, für die die Daten garantiert von Braze zwischengespeichert werden. Es kann daher vorkommen, dass Sie bei einer bestimmten Cache-Dauer mehr Connected-Content-Anfragen sehen als erwartet.

### Cache für eine bestimmte Anzahl von Sekunden

Dieses Beispiel speichert für 900 Sekunden (oder 15 Minuten) zwischen.

{% raw %}
```
{% connected_content https://example.com/webservice.json :cache_max_age 900 %}
```
{% endraw %}

### Cache-Busting {#cache-busting}

Um zu verhindern, dass Connected-Content den von einer GET-Anfrage zurückgegebenen Wert zwischenspeichert, können Sie die Konfiguration `:no_cache` verwenden. Antworten von Braze-internen Hosts werden jedoch weiterhin zwischengespeichert.

{% raw %}
```js
{% connected_content https://example.com/webservice.json :no_cache %}
```
{% endraw %}

{% alert important %}
Stellen Sie sicher, dass der angegebene Connected-Content-Endpunkt große Datenverkehrsspitzen verarbeiten kann, bevor Sie diese Option verwenden, da Sie andernfalls wahrscheinlich eine erhöhte Sendelatenz (längere Verzögerungen oder größere Zeitintervalle zwischen Anfrage und Antwort) feststellen werden, weil Braze für jede einzelne Nachricht Connected-Content-Anfragen stellt.
{% endalert %}

Bei einem POST müssen Sie kein Cache-Busting durchführen, da POST-Anfragen standardmäßig nicht zwischengespeichert werden. Um eine POST-Antwort zwischenzuspeichern, fügen Sie `:cache_max_age` hinzu; um das Caching eines POST zu vermeiden, lassen Sie `:cache_max_age` weg.

## Wissenswertes

- Caching kann dazu beitragen, doppelte Connected-Content-Aufrufe zu reduzieren. Es ist jedoch nicht garantiert, dass es immer zu einem einzigen Connected-Content-Aufruf pro Nutzer:in führt.
- Connected-Content-Caching basiert auf der URL und dem Workspace. Wenn der Connected-Content-Aufruf an dieselbe URL geht, kann er über Kampagnen und Canvases hinweg zwischengespeichert werden.
- Der Cache basiert auf einer eindeutigen URL, nicht auf einer Nutzer-ID oder Kampagne. Das bedeutet, dass die zwischengespeicherte Version eines Connected-Content-Aufrufs über mehrere Nutzer:innen und Kampagnen in einem Workspace hinweg verwendet werden kann, wenn die URL identisch ist.