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

Um auf das Protokoll zuzugreifen, gehen Sie zu **Einstellungen** > **Einrichtung und Tests** > **Event-Nutzerprotokoll**.

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

Wenn Sie eine:n Nutzer:in zu einer internen Gruppe hinzugefügt haben, aber im Event-Nutzerprotokoll keine SDK-Protokolle angezeigt werden, kann dies an einer fehlenden Konfigurationsoption liegen. Um SDK-Protokolle zu erfassen, wählen Sie in den **Einstellungen für interne Gruppen** der jeweiligen [internen Gruppe]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups) die Option **Nutzerereignisse für Gruppenmitglieder aufzeichnen** aus.

### Verzögerung bei Protokollaktualisierungen {#delay-in-logs-updates}

Diese Verzögerung wird in der Regel durch die normale API-Verarbeitungslast verursacht.

Wenn Sie SDK-Methoden aufrufen, speichert das SDK diese Ereignisse im Allgemeinen lokal zwischen und überträgt sie alle 10 Sekunden an den Server. Je nach Gesamtlast zum jeweiligen Zeitpunkt kann es zwischen einer Sekunde und einigen Minuten dauern, bis unsere Verarbeitungswarteschlange die Ereignisse aufnimmt.

Wenn Sie möchten, dass Ereignisse so schnell wie möglich eintreffen, rufen Sie die Funktion `requestImmediateDataFlush()` auf.

### Fehlgeschlagene Impressions von In-App-Nachrichten {#in-app-message-impression-failures}

Wenn eine In-App-Nachricht nicht angezeigt wird, können Sie den Grund im Event-Nutzerprotokoll finden, indem Sie die JSON-Rohdaten der entsprechenden SDK-Anfrage aufklappen und im Antwortfeld nach dem Feld `error_code` suchen. Der `error_code` gibt den spezifischen Grund an, warum die Impression fehlgeschlagen ist (zum Beispiel ein ungültiger Farbwert oder ein Rendering-Problem). Teilen Sie diesen Fehlercode dem [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) mit, wenn eine weitere Untersuchung erforderlich ist.

### Session-Ende und Session-Start haben ähnliche Zeitstempel (iOS) {#session-end-and-session-start-have-similar-timestamps-ios}

Das Event-Nutzerprotokoll zeigt den Zeitstempel an, zu dem Braze über das Session-Ende benachrichtigt wurde – das ist Millisekunden vor dem Start der nächsten Session. Braze kann nicht wissen, dass die Session beendet wurde, bevor die App erneut geöffnet wird, da iOS die Ausführung von Threads aggressiv stoppt, wenn sich die App im Hintergrund befindet – sodass keine Daten an Braze übertragen werden können, bis die App wieder geöffnet wird.

Obwohl die Session-Endzeit als Sekunden vor dem Session-Start angegeben wird, wird die Session-Dauer beim Übertragen des Ereignisses separat übermittelt und ist korrekt – sie spiegelt die Zeit wider, in der die App geöffnet war. Daher hat dieses Verhalten keinen Einfluss auf den Filter `Median Session Duration`.

In Bezug auf Nutzer:innen-Sessions können Sie Braze verwenden, um Daten wie die folgenden zu überwachen:

- Wie viele Sessions eine:r Nutzer:in hatte
- Wann eine:r Nutzer:in zuletzt eine Session gestartet hat
- Ob die:der Nutzer:in eine Session startet, nachdem sie:er eine Campaign erhalten hat
- Wie lang die mittlere Session-Dauer der:des Nutzer:in ist

Diese Verhaltensweisen werden nicht davon beeinflusst, dass das Session-Ende-Ereignis bei der nächsten Session übertragen wird.