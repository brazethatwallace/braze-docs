---
nav_title: Checkliste vor und nach dem Start
article_title: Checkliste vor und nach dem Start
page_order: 2
description: "Dieser Artikel bietet eine Richtlinie für Dinge, die Sie vor und nach dem Start eines Canvas überprüfen sollten."
tool: Canvas

---

# Checkliste vor und nach dem Start {#pre-and-post-launch-checklist}

> Dieser Artikel bietet eine Richtlinie für Dinge, die Sie vor und nach dem Start eines Canvas überprüfen sollten.

## Vor dem Start zu beachten {#things-to-consider-before-launch}

Bevor Sie ein Canvas starten, gibt es mehrere Details, die Sie überprüfen können, um sicherzustellen, dass Ihr Messaging und Ihre Sendezeiten mit den Präferenzen Ihrer Zielgruppe übereinstimmen. Zu den Überlegungen gehören unter anderem Unterschiede bei Zeitzonen, Entry-Einstellungen und mehr. Nutzen Sie diese Checkliste als Leitfaden, um diese Bereiche basierend auf Ihrem Anwendungsfall zu optimieren und so zum Erfolg Ihres Canvas beizutragen.

### Zeitzoneneinstellungen überprüfen {#review-time-zone-settings}

Wenn Sie Nutzer:innen gemäß ihrer Ortszeit über einen geplanten Entry-Zeitplan eintreten lassen, sollten Sie Ihr Canvas mindestens 24 Stunden vor dem gewünschten Eintritt der Nutzer:innen starten. Hier ist zum Beispiel ein Canvas, bei dem zwischen dem Start und dem geplanten Entry-Zeitpunkt nicht genügend Zeit gelassen wurde. In diesem Szenario gibt es möglicherweise einige Nutzer:innen, die nicht in Ihr Canvas eintreten, da der geplante Entry-Zeitpunkt in bestimmten Zeitzonen bereits verstrichen ist.

{% alert tip %}
Sie erhalten eine Warnung, wenn Sie nicht genügend Puffer eingeplant haben. Eine schnelle Lösung besteht darin, die Sendezeit anzupassen, damit Nutzer:innen für volle 24 Stunden im Zielsegment verbleiben können.
{% endalert %}

![Ein Canvas, das so geplant ist, dass Nutzer:innen einmalig ab 10 Uhr am 30. April 2025 in ihrer Ortszeit eintreten.]({% image_buster /assets/img_archive/canvas_checklist1.png %}){: style="max-width:75%;"}

### Verwendung regulärer Ausdrücke für Zielgruppenfilter in Betracht ziehen {#consider-using-regular-expressions-for-audience-filters}

Nachdem Sie die grundlegenden Details festgelegt haben, wann Ihre Nutzer:innen in ein Canvas eintreten sollen, empfiehlt es sich, Ihre Segmente oder Filter im Schritt **Target Audience** beim Erstellen eines Canvas zu überprüfen. In diesem Schritt können Sie auch die Zusammenfassung der **Zielpopulation** einsehen, um zu sehen, wie Ihre Zielgruppe konfiguriert wurde.

Erwägen Sie hier die Verwendung eines regulären Ausdrucks für Segmente oder Filter in Zielgruppenpfad-Schritten sowie in den Zustellungsvalidierungseinstellungen in Nachrichten- und Decision-Split-Schritten. Ein [regulärer Ausdruck]({{site.baseurl}}/user_guide/audience/segments/regex) (auch als Regex bezeichnet) ist ein String, was bedeutet, dass er Muster erkennt und Zeichen berücksichtigt, anstatt beispielsweise Groß- und Kleinschreibung. Das bedeutet, wenn Sie „Equals / Does Not Equal“ verwenden, könnten Sie Ihre Zielgruppe aufgrund einfacher Syntaxfehler einschränken.

Wenn Sie bemerken, dass Ihre Zielgruppe kleiner als erwartet ist, versuchen Sie, „Matches Regex“ oder „Does Not Match Regex“ anstelle von „Equals“ oder „Does Not Equal“ zu verwenden. Dies kann die fehlenden Nutzer:innen berücksichtigen und eine größere Zielgruppe ansprechen.

### Entry-Einstellungen und Race-Conditions identifizieren {#identify-entry-settings-and-race-conditions}

Eine Race-Condition kann auftreten, wenn Sie dieselben Entry-Kriterien sowohl in Ihren Einstellungen für **Entry Schedule** als auch für **Target Audience** verwendet haben.

Wenn Sie einen aktionsbasierten Entry verwenden, überprüfen Sie, ob Sie hier nicht dieselbe Trigger-Aktion wie in Ihrer Zielgruppe verwendet haben. Eine Race-Condition kann auftreten, bei der sich die Nutzer:innen zum Zeitpunkt des Trigger-Events nicht in der Zielgruppe befinden, sodass sie nicht in das Canvas eintreten.

{% alert tip %}
Lesen Sie die [Best Practices]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions#scenario-3-matching-action-based-triggers-and-audience-filters) zur Vermeidung dieser Race-Condition, wenn Sie ein aktionsbasiertes Canvas mit demselben Trigger wie dem Zielgruppenfilter einrichten.
{% endalert %}

### Canvas-Entry-Eigenschaften und Event-Eigenschaften prüfen {#check-canvas-entry-properties-and-event-properties}

Obwohl sie ähnlich klingen, funktionieren [Canvas-Entry-Eigenschaften und Event-Eigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) innerhalb Ihrer Canvas-Workflows unterschiedlich. Canvas-Entry-Eigenschaften sind an Ihre Entry-Einstellungen gebunden und können in jeder Nachrichtenkomponente innerhalb Ihres Canvas referenziert werden. Canvas-Entry-Eigenschaften sind Eigenschaften des Events oder API-Aufrufs, der den Eintritt von Nutzer:innen in ein Canvas über aktionsbasierte oder API-getriggerte Entry-Einstellungen auslöst.

Event-Eigenschaften hingegen können nur im ersten Nachrichtenschritt nach einem Aktionspfad-Schritt referenziert werden. Event-Eigenschaften sind Eigenschaften eines angepassten Events oder Kauf-Events, das die Nutzer:innen während des Bewertungsfensters eines Aktionspfad-Schritts durchgeführt haben und das ihren Fortschritt entlang eines der definierten Aktionspfade auslöst.

Überprüfen Sie Ihre Nachrichtenvorschau auf alle Nachrichtenschritte, die auf Canvas-Entry-Eigenschaften oder Event-Eigenschaften verweisen.

### Nachrichtenschritte für den Fortschritt der Nutzer:innen überprüfen {#review-message-steps-for-user-advancement}

Standardmäßig durchlaufen Nutzer:innen alle Nachrichtenschritte, unabhängig davon, ob sie die Nachricht erhalten haben. Wenn Sie nur die Nutzer:innen voranbringen möchten, die eine bestimmte Nachricht erhalten haben, können Sie dies tun, indem Sie einen Decision-Split-Schritt direkt nach Ihrer Nachrichtenkomponente hinzufügen. Fügen Sie den Filter „Received Message from Canvas Step“ als zusätzlichen Filter hinzu und wählen Sie dann das Canvas und den Nachrichtenschritt aus.

Bei Nachrichtenschritten mit In-App-Nachrichten sollten Sie eine Aktionspfad-Komponente anstelle der Decision-Split-Komponente verwenden. Dadurch können Sie Nutzer:innen basierend darauf voranbringen, ob sie Ihre In-App-Nachricht gesehen haben. Definieren Sie eine Aktionsgruppe, indem Sie den Filter „Interact with Step“ hinzufügen und **View in app message** auswählen. Setzen Sie dann das Bewertungsfenster des Schritts auf das Ablaufzeitfenster der In-App-Nachricht.

Für eine Nachrichtenkomponente im Mehrkanalversand empfehlen wir Folgendes:
* Fügen Sie einen Verzögerungsschritt zwischen Ihren Nachrichten- und Decision-Split-Schritten ein und setzen Sie die Verzögerung auf mindestens fünf Sekunden.
* Wenn die Komponente intelligentes Timing enthält, setzen Sie die Verzögerung auf 24 Stunden.
* Wenn die Komponente Rate-Limiting enthält, teilen Sie Ihre Nachrichten in mehrere Einkanalversand-Nachrichtenschritte auf und verbinden Sie diese miteinander. Verbinden Sie dann den Decision-Split-Schritt direkt nach dem letzten Nachrichtenschritt, um zu prüfen, ob Nutzer:innen eine der Nachrichten erhalten haben. Sie können diese Methode auch als Alternative für einen Mehrkanal-Nachrichtenschritt mit intelligentem Timing verwenden.

## Überlegungen nach dem Start {#things-to-consider-after-launch}

Sie haben Ihr Canvas gestartet! Und jetzt? Verwenden Sie diese Checkliste, um zu überprüfen und anzupassen, wie Ihr Canvas in folgenden Szenarien auf Abweichungen nach dem Start reagiert.

### Viele Eintritte, aber wenige Sendungen {#many-entries-but-few-sends}

Angenommen, Sie haben eine Diskrepanz zwischen der Anzahl gesendeter Nachrichten und der Gesamtzahl der Eintritte festgestellt. Sie können Bereiche identifizieren und aufdecken, die in Ihrem Canvas angepasst werden müssen, indem Sie diese Schlüsselbereiche überprüfen.

#### Eintrittszielgruppe {#entry-audience}

Wenn Sie eine geplante Sendekampagne verwenden, überprüfen Sie Ihre Zielgruppe, indem Sie Ihre Zielpopulation nochmals kontrollieren. Wie sehen die Zahlen über die Kanäle hinweg aus, und in welchem Zusammenhang stehen sie mit den Kanälen, die Sie in Ihrem Canvas verwendet haben? Wenn die niedrigsten Zahlen den in Ihrem Canvas verwendeten Kanälen entsprechen, haben Sie möglicherweise das Problem gefunden.

#### Erste Komponente des Canvas {#first-component-of-the-canvas}

Überprüfen Sie alle Zielgruppenfilter, Aktionstrigger oder Segmente, die in den Anfangskomponenten Ihres Canvas verwendet werden. Gibt es Tippfehler oder zu strenge Bedingungen, die Ihren Canvas daran hindern, richtig zu starten? Verwenden Sie „Equals“, wenn Sie „Matches Regex“ verwenden sollten?

#### Canvas-Kontrollgruppe {#canvas-control-group}

Überprüfen Sie die Verteilung der Nutzer:innen zwischen Ihren Varianten und Ihrer Kontrollgruppe. Ist die Kontrollgruppe größer als beabsichtigt? Falls ja, können Sie diese Einstellung bearbeiten. Wenn **Optimize with BrazeAI<sup>TM</sup>** aktiviert ist und die Kontrollgruppe gewinnt, erwägen Sie, Ihr Canvas zu stoppen und einen neuen Ansatz zu versuchen.

### Eine leere Gesamtzielgruppe {#an-empty-total-audience}

Wenn Sie keine Eintrittsdaten für Ihr Canvas sehen, kann der Grund dafür, dass Nutzer:innen nicht in Ihr Canvas eintreten, an Race-Conditions und restriktiven Zielgruppen-Segmentierungsfiltern liegen.

Wenn Sie einen aktionsbasierten Eintritt in Ihrem Eintrittsplan verwenden, prüfen Sie, ob Sie hier nicht dieselbe Triggeraktion wie in Ihrer **Zielgruppe** verwendet haben. Eine Race-Condition kann auftreten, wenn sich die Nutzer:innen zum Zeitpunkt der Triggeraktion nicht in der Zielgruppe befinden, was bedeutet, dass sie nicht in das Canvas eintreten.

Überprüfen Sie außerdem, ob das ausgewählte Segment Nutzer:innen enthält, indem Sie die Tabelle **Zielpopulation** in den Einstellungen der **Zielgruppe** einsehen. Wenn diese Zahl niedrig ist, prüfen Sie, wie Sie Ihre Eintrittseinstellungen anpassen oder Ihre ausgewählten Segmente oder Filter auf Fehler überprüfen können.

### Unerwarteter Abfall zwischen Schritten {#unexpected-drop-off-between-steps}

Eine weitere offensichtliche Möglichkeit, Anpassungsbereiche für Ihr Canvas zu identifizieren, ist ein großer Abfall von einem Canvas-Schritt zum nächsten. Überprüfen Sie in diesem Fall, ob Ihre Zielgruppenfilter und Ausnahme-Events keine Tippfehler oder Großschreibungsfehler enthalten. Und wie immer: Stellen Sie sicher, dass Ihre Zielgruppenfilter nicht so streng sind, dass sie einen Großteil Ihrer Nutzer:innen vom Eintritt in das Canvas ausschließen.

Als Nächstes ist es wichtig, folgende Einstellungen zu identifizieren, die beeinflussen können, wann und ob Nachrichten an Ihre Nutzer:innen gesendet werden:
- [Intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing)
- [Ruhezeiten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)
- Zustellungsvalidierungen

Wählen Sie generell entweder intelligentes Timing oder [Ruhezeiten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours) für Ihr Canvas, nicht beides. Die gleiche Empfehlung gilt für die Verwendung von entweder intelligentem Timing oder [Rate-Limiting]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping), nicht beidem. Weitere Informationen zur optimalen Nutzung der Intelligence Suite finden Sie in unseren [Intelligence Suite-Anwendungsfällen]({{site.baseurl}}/user_guide/brazeai/intelligence_suite#use-cases).

### Verdächtige Sendevolumen zwischen Pfaden {#suspicious-send-volumes-between-paths}

Wenn das Volumen der Sendungen zwischen zwei oder mehr Pfaden (entweder Zielgruppenpfade oder Aktionspfade) nicht Ihren Erwartungen entspricht, kann dies eine Gelegenheit sein, Ihre Segmente, Filter oder Triggeraktionen zu überprüfen. Stellen Sie außerdem sicher, dass Sie überlappende Filter identifizieren und entfernen.