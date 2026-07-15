---
nav_title: Checkliste vor und nach dem Start
article_title: Checkliste vor und nach dem Start
page_order: 2
description: "Dieser Artikel bietet eine Richtlinie für Dinge, die Sie vor und nach dem Start eines Canvas überprüfen sollten."
tool: Canvas

---

# Checkliste vor und nach dem Start {#pre-and-post-launch-checklist}

> Dieser Artikel bietet eine Richtlinie für Dinge, die Sie vor und nach dem Start eines Canvas überprüfen sollten.

## Dinge, die Sie vor dem Start beachten sollten {#things-to-consider-before-launch}

Bevor Sie einen Canvas starten, gibt es mehrere Details, die Sie überprüfen können, um sicherzustellen, dass Ihr Messaging und Ihre Sendezeiten mit den Präferenzen Ihrer Zielgruppe übereinstimmen. Zu berücksichtigen sind unter anderem Unterschiede bei Zeitzonen, Entry-Einstellungen und mehr. Nutzen Sie diese Checkliste als Leitfaden und passen Sie diese Bereiche basierend auf Ihrem Anwendungsfall an, um zum Erfolg Ihres Canvas beizutragen.

### Zeitzonen-Einstellungen überprüfen {#review-time-zone-settings}

Wenn Sie Nutzer:innen gemäß ihrer Ortszeit über einen geplanten Entry-Zeitplan eintreten lassen, sollten Sie Ihren Canvas mindestens 24 Stunden vor dem gewünschten Eintrittszeitpunkt starten. Hier ist zum Beispiel ein Canvas, bei dem nicht genügend Zeit zwischen dem Start und der geplanten Eintrittszeit eingeplant wurde. In diesem Szenario gibt es möglicherweise einige Nutzer:innen, die nicht in Ihren Canvas eintreten, da die geplante Eintrittszeit in bestimmten Zeitzonen bereits verstrichen ist.

{% alert tip %}
Sie erhalten eine Warnung, wenn Sie nicht genügend Puffer eingeplant haben. Eine schnelle Lösung besteht darin, die Sendezeit anzupassen, damit Nutzer:innen volle 24 Stunden im Zielsegment verbleiben können.
{% endalert %}

![Ein Canvas, der so geplant ist, dass Nutzer:innen ab dem 30. April 2025 um 10 Uhr in ihrer Ortszeit eintreten.]({% image_buster /assets/img_archive/canvas_checklist1.png %}){: style="max-width:75%;"}

### Erwägen Sie die Verwendung regulärer Ausdrücke für Zielgruppen-Filter {#consider-using-regular-expressions-for-audience-filters}

Nachdem Sie die grundlegenden Details festgelegt haben, wann Ihre Nutzer:innen in einen Canvas eintreten sollen, empfiehlt es sich, Ihre Segmente oder Filter im Schritt **Zielgruppe** beim Erstellen eines Canvas zu überprüfen. In diesem Schritt können Sie auch die Zusammenfassung der **Zielpopulation** einsehen, um zu sehen, wie Ihre Zielgruppe konfiguriert wurde.

Erwägen Sie hier die Verwendung eines regulären Ausdrucks für Segmente oder Filter in Zielgruppenpfad-Schritten sowie für Zustellungsvalidierungseinstellungen in Nachrichten- und Decision-Split-Schritten. Ein [regulärer Ausdruck]({{site.baseurl}}/user_guide/audience/segments/regex) (auch als Regex bezeichnet) ist ein String, was bedeutet, dass er Muster erkennt und Zeichen berücksichtigt, anstatt beispielsweise Groß- und Kleinschreibung. Das bedeutet, wenn Sie „Equals / Does Not Equal“ verwenden, könnten Sie Ihre Zielgruppengröße aufgrund einfacher Syntaxfehler einschränken.

Wenn Sie feststellen, dass Ihre Zielgruppe kleiner als erwartet ist, versuchen Sie „Matches Regex“ oder „Does Not Match Regex“ anstelle von „Equals“ oder „Does Not Equal“ zu verwenden. Dies kann die fehlenden Nutzer:innen berücksichtigen und eine größere Zielgruppe ansprechen.

### Entry-Einstellungen und Race-Conditions identifizieren {#identify-entry-settings-and-race-conditions}

Eine Race-Condition kann auftreten, wenn Sie dieselben Eintrittskriterien sowohl in Ihren **Entry-Zeitplan**- als auch in Ihren **Zielgruppe**-Einstellungen verwendet haben.

Wenn Sie aktionsbasierten Eintritt verwenden, überprüfen Sie, ob Sie hier nicht dieselbe Trigger-Aktion wie in Ihrer Zielgruppe verwendet haben. Eine Race-Condition kann auftreten, bei der sich die Nutzer:innen zum Zeitpunkt des Trigger-Events nicht in der Zielgruppe befinden, was bedeutet, dass sie nicht in den Canvas eintreten.

{% alert tip %}
Sehen Sie sich die [Best Practices]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions#scenario-3-matching-action-based-triggers-and-audience-filters) an, um diese Race-Condition beim Einrichten eines aktionsbasierten Canvas mit demselben Trigger wie dem Zielgruppen-Filter zu vermeiden.
{% endalert %}

### Eingangs-Eigenschaften und Event-Eigenschaften überprüfen {#check-canvas-entry-properties-and-event-properties}

Obwohl sie ähnlich benannt sind, funktionieren [Eingangs-Eigenschaften und Event-Eigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) innerhalb Ihrer Canvas-Workflows unterschiedlich. Eingangs-Eigenschaften sind an Ihre Entry-Einstellungen gebunden und können in jeder Nachrichtenkomponente in Ihrem gesamten Canvas referenziert werden. Eingangs-Eigenschaften sind Eigenschaften des Events oder API-Aufrufs, der den Eintritt von Nutzer:innen in einen Canvas triggert, unter Verwendung aktionsbasierter oder API-getriggerter Entry-Einstellungen.

Event-Eigenschaften hingegen können nur im ersten Nachrichten-Schritt nach einem Aktionspfade-Schritt referenziert werden. Event-Eigenschaften sind Eigenschaften eines angepassten Events oder Kauf-Events, das die Nutzer:innen während des Auswertungsfensters eines Aktionspfade-Schritts ausgeführt haben und das ihren Fortschritt entlang eines der definierten Aktions-Pfade triggert.

Überprüfen Sie Ihre Nachrichtenvorschau für alle Nachrichten-Schritte, die Eingangs-Eigenschaften oder Event-Eigenschaften referenzieren.

### Nachrichten-Schritte für den Fortschritt der Nutzer:innen überprüfen {#review-message-steps-for-user-advancement}

Standardmäßig schreiten Nutzer:innen durch alle Nachrichten-Schritte voran, unabhängig davon, ob sie die Nachricht erhalten haben. Wenn Sie nur die Nutzer:innen voranbringen möchten, die eine bestimmte Nachricht erhalten haben, können Sie dies tun, indem Sie einen Decision-Split-Schritt direkt nach Ihrer Nachrichtenkomponente hinzufügen. Fügen Sie den Filter „Received Message from Canvas Step“ als zusätzlichen Filter hinzu und wählen Sie dann den Canvas und den Nachrichten-Schritt aus.

Für Nachrichten-Schritte mit In-App-Nachrichten möchten Sie möglicherweise eine Aktionspfade-Komponente anstelle der Decision-Split-Komponente verwenden. Dies ermöglicht es Ihnen, Nutzer:innen basierend darauf voranzubringen, ob sie Ihre In-App-Nachricht gesehen haben. Definieren Sie eine Aktionsgruppe, indem Sie den Filter „Interact with Step“ hinzufügen und **View in app message** auswählen. Setzen Sie dann das Auswertungsfenster des Schritts auf das Ablauf-Fenster der In-App-Nachricht.

Für eine Nachrichtenkomponente im Multi-Channel-Messaging empfehlen wir Folgendes:
* Fügen Sie einen Verzögerungsschritt zwischen Ihren Nachrichten- und Decision-Split-Schritten ein und setzen Sie die Verzögerung auf mindestens fünf Sekunden.
* Wenn die Komponente intelligentes Timing enthält, setzen Sie die Verzögerung auf 24 Stunden.
* Wenn die Komponente Rate-Limiting enthält, teilen Sie Ihre Nachrichten in mehrere Einkanal-Nachrichten-Schritte auf und verbinden Sie diese miteinander. Verbinden Sie dann den Decision-Split-Schritt direkt nach dem letzten Nachrichten-Schritt, um zu überprüfen, ob Nutzer:innen eine der Nachrichten erhalten haben. Sie können diese Methode auch als Alternative für einen Multi-Channel-Nachrichten-Schritt mit intelligentem Timing verwenden.

## Dinge, die Sie nach dem Start beachten sollten {#things-to-consider-after-launch}

Sie haben Ihren Canvas gestartet! Und jetzt? Nutzen Sie diese Checkliste, um zu sehen, wie Sie Ihren Canvas im Falle von Abweichungen nach dem Start basierend auf diesen Szenarien überprüfen und anpassen können.

### Viele Eintritte, aber wenige Sendungen {#many-entries-but-few-sends}

Nehmen wir zum Beispiel an, Sie haben eine Diskrepanz zwischen der Anzahl gesendeter Nachrichten und der Gesamtzahl der Eintritte festgestellt. Sie können Bereiche zur Anpassung Ihres Canvas identifizieren und aufdecken, indem Sie diese Schlüsselbereiche überprüfen.

#### Entry-Zielgruppe {#entry-audience}

Wenn Sie eine geplante Sende-Campaign verwenden, überprüfen Sie Ihre Zielgruppe, indem Sie Ihre Zielpopulation einsehen. Wie sehen die Zahlen über die Kanäle hinweg aus, und wie verhält sich das zu den Kanälen, die Sie in Ihrem Canvas verwendet haben? Wenn die niedrigsten Zahlen mit den Kanälen übereinstimmen, die Sie in Ihrem Canvas verwendet haben, haben Sie möglicherweise das Problem gefunden.

#### Erste Komponente des Canvas {#first-component-of-the-canvas}

Überprüfen Sie alle Zielgruppen-Filter, Aktions-Trigger oder Segmente, die in den Anfangskomponenten Ihres Canvas verwendet werden. Gibt es Tippfehler oder zu strenge Bedingungen, die Ihren Canvas daran hindern, richtig zu starten? Verwenden Sie „Equals“, wenn Sie „Matches Regex“ verwenden sollten?

#### Canvas-Kontrollgruppe {#canvas-control-group}

Überprüfen Sie die Verteilung der Nutzer:innen zwischen Ihren Varianten und Ihrer Kontrollgruppe. Ist die Kontrollgruppe größer als beabsichtigt? Wenn ja, können Sie diese Einstellung bearbeiten. Wenn Sie **Intelligente Auswahl** aktiviert haben und die Kontrollgruppe gewinnt, erwägen Sie, Ihren Canvas zu stoppen und einen neuen Ansatz zu versuchen.

### Eine leere Gesamtzielgruppe {#an-empty-total-audience}

Wenn Sie keine Eintrittsdaten für Ihren Canvas sehen, kann der Grund dafür, dass Nutzer:innen nicht in Ihren Canvas eintreten, an Race-Conditions und restriktiven Zielgruppen-Segmentierungsfiltern liegen.

Wenn Sie aktionsbasierten Eintritt in Ihrem Entry-Zeitplan verwenden, überprüfen Sie, ob Sie hier nicht dieselbe Trigger-Aktion wie in Ihrer **Zielgruppe** verwendet haben. Eine Race-Condition kann auftreten, bei der sich die Nutzer:innen zum Zeitpunkt des Trigger-Events nicht in der Zielgruppe befinden, was bedeutet, dass sie nicht in den Canvas eintreten.

Überprüfen Sie außerdem, ob das ausgewählte Segment Nutzer:innen enthält, indem Sie die Tabelle **Zielpopulation** in den **Zielgruppe**-Einstellungen einsehen. Wenn diese Zahl niedrig ist, prüfen Sie, wie Sie Ihre Entry-Einstellungen anpassen können, oder überprüfen Sie Ihre ausgewählten Segmente oder Filter auf Fehler.

### Unerwarteter Abfall zwischen Schritten {#unexpected-drop-off-between-steps}

Eine weitere offensichtliche Möglichkeit, Anpassungsbereiche für Ihren Canvas zu identifizieren, ergibt sich, wenn es einen großen Abfall von einem Canvas-Schritt zum nächsten gibt. Überprüfen Sie in diesem Fall, ob Ihre Zielgruppen-Filter und Ausnahme-Events keine Tippfehler oder Fehler bei der Groß- und Kleinschreibung aufweisen. Und wie immer: Stellen Sie sicher, dass Ihre Zielgruppen-Filter nicht so streng sind, dass sie die Mehrheit Ihrer Nutzer:innen vom Eintritt in den Canvas ausschließen.

Als Nächstes ist es wichtig, diese Einstellungen zu identifizieren, die beeinflussen können, wann und ob Nachrichten an Ihre Nutzer:innen gesendet werden:
- [Intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing)
- [Ruhezeiten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)
- Zustellungsvalidierungen

Wählen Sie im Allgemeinen entweder intelligentes Timing oder [Ruhezeiten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours) für Ihren Canvas, nicht beides. Die gleiche Empfehlung gilt für die Verwendung von entweder intelligentem Timing oder [Rate-Limiting]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping), nicht beides. Weitere Informationen zur optimalen Nutzung der Intelligence Suite finden Sie in unseren [Intelligence Suite-Anwendungsfällen]({{site.baseurl}}/user_guide/brazeai/intelligence_suite#use-cases).

### Verdächtige Sendevolumen zwischen Pfaden {#suspicious-send-volumes-between-paths}

Wenn das Sendevolumen zwischen zwei oder mehr Pfaden (entweder Zielgruppenpfade oder Aktionspfade) nicht Ihren Erwartungen entspricht, kann dies eine Gelegenheit sein, Ihre Segmente, Filter oder Trigger-Aktionen zu überprüfen. Stellen Sie außerdem sicher, dass Sie überlappende Filter identifizieren und entfernen.