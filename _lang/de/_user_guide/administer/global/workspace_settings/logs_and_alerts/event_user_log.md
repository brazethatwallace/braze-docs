---
nav_title: Event-Nutzerprotokoll
article_title: Event-Nutzerprotokoll
page_order: 1
page_type: reference
description: "Dieser Referenzartikel behandelt das Event-Nutzerprotokoll, das Ihnen bei der Fehlersuche und Fehlerbehebung in Ihrer Braze-Integration helfen kann."

---

# Event-Nutzerprotokoll {#event-user-log}

> Das Event-Nutzerprotokoll kann Ihnen helfen, Probleme in Ihrer Braze-Integration aufzuschlüsseln, zu debuggen oder anderweitig zu beheben. Dieser Tab zeigt Ihnen ein Fehlerprotokoll, das den Fehlertyp, die zugehörige App, den Zeitpunkt des Auftretens und häufig auch die Möglichkeit enthält, die zugehörigen Rohdaten einzusehen.

{% alert tip %}
Zusätzlich zu diesem Artikel empfehlen wir Ihnen auch unseren Braze-Lernkurs [Quality Assurance and Debugging Tools](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/), der erklärt, wie Sie das Event-Nutzerprotokoll für Ihre eigene Fehlerbehebung und Ihr Debugging nutzen können.
{% endalert %}

Um auf das Protokoll zuzugreifen, gehen Sie zu **Einstellungen** > **Event-Nutzerprotokoll**.

Um Ihre Protokolle leicht zu finden, können Sie nach folgenden Kriterien filtern:

* SDK oder API
* App-Namen
* Zeitraum
* Nutzer:in

Jedes Protokoll ist in mehrere Abschnitte unterteilt, die Folgendes umfassen können:

* Geräteattribute
* Nutzerattribute
* Events
* Campaign-Events
* Antwortdaten

Wählen Sie das Symbol **Daten erweitern** aus, um die JSON-Rohdaten für das jeweilige Protokoll anzuzeigen.

![Das Symbol „Daten erweitern“ neben einem bestimmten Protokoll.]({% image_buster /assets/img_archive/expand_data.png %})

Event-Nutzerprotokolle bleiben nach der Protokollierung 30 Tage lang im Dashboard verfügbar.

![Rohprotokolle für Events]({% image_buster /assets/img_archive/rawlogs.png %}){: style="max-width:60%;"}

## Fehlerbehebung {#troubleshooting}

### Fehlende SDK-Protokolle für Testnutzer:innen {#missing-sdk-logs-for-test-users}

Wenn Sie eine:n Nutzer:in zu einer internen Gruppe hinzugefügt haben, aber keine SDK-Protokolle im Event-Nutzerprotokoll angezeigt werden, kann dies an einer fehlenden Konfigurationsoption liegen. Um SDK-Protokolle zu erfassen, stellen Sie sicher, dass Sie **Nutzer-Events für Gruppenmitglieder aufzeichnen** in den **Einstellungen für interne Gruppen** für diese [interne Gruppe]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups) ausgewählt haben.

### Verzögerung bei Protokollaktualisierungen {#delay-in-logs-updates}

Dies kann eine normale Verzögerung seitens unserer API sein.

Wenn Sie SDK-Methoden aufrufen, speichert das SDK diese Events in der Regel lokal zwischen und sendet sie alle 10 Sekunden an den Server. Es kann je nach Gesamtlast zu diesem Zeitpunkt zwischen einer Sekunde und einigen Minuten dauern, bis unsere Verarbeitungswarteschlange die Events aufnimmt.

Wenn Sie möchten, dass Events so schnell wie möglich eintreffen, versuchen Sie, die Funktion `requestImmediateDataFlush()` aufzurufen.

### Fehlgeschlagene Impressions von In-App-Nachrichten {#in-app-message-impression-failures}

Wenn eine In-App-Nachricht nicht angezeigt wird, können Sie den Grund im Event-Nutzerprotokoll finden, indem Sie die JSON-Rohdaten für die entsprechende SDK-Anfrage erweitern und in der Antwort nach dem Feld `error_code` suchen. Der `error_code` identifiziert den spezifischen Grund für die fehlgeschlagene Impression (z. B. ein ungültiger Farbwert oder ein Rendering-Problem). Teilen Sie diesen Fehlercode dem [Braze-Support]({{site.baseurl}}/braze_support) mit, wenn eine weitere Untersuchung erforderlich ist.

### Sitzungsende und Sitzungsstart haben ähnliche Zeitstempel (iOS) {#session-end-and-session-start-have-similar-timestamps-ios}

Das Event-Nutzerprotokoll zeigt den Zeitstempel an, zu dem Braze über das Sitzungsende benachrichtigt wurde – dieser liegt Millisekunden vor dem Start der nächsten Sitzung. Braze kann nicht wissen, dass die Sitzung beendet wurde, bevor die App erneut geöffnet wird, da iOS die Ausführung von Threads aggressiv stoppt, wenn die App im Hintergrund läuft – daher können keine Daten an Braze gesendet werden, bis die App wieder geöffnet wird.

Obwohl die Sitzungsendzeit als Sekunden vor dem Sitzungsstart angegeben wird, wird die Sitzungsdauer beim Senden des Events separat übermittelt und ist korrekt – sie spiegelt die Zeit wider, in der die App geöffnet war. Daher hat dieses Verhalten keinen Einfluss auf den Filter `Median Session Duration`.

In Bezug auf Nutzersitzungen können Sie Braze verwenden, um Daten wie die folgenden zu überwachen:

- Wie viele Sitzungen ein:e Nutzer:in hatte
- Wann ein:e Nutzer:in zuletzt eine Sitzung gestartet hat
- Ob der/die Nutzer:in nach Erhalt einer Campaign eine Sitzung startet
- Wie lang die mediane Sitzungsdauer des/der Nutzer:in ist

Diese Verhaltensweisen werden nicht dadurch beeinflusst, dass das Sitzungsende-Event in der nächsten Sitzung gesendet wird.