---
nav_title: FAQ
article_title: Canvas FAQ
page_order: 8
alias: "/canvas_v2_101/"
description: "Dieser Artikel enthält Antworten auf häufig gestellte Fragen zu Canvas."
tool: Canvas
toc_headers: h2

---

# Häufig gestellte Fragen {#frequently-asked-questions}

> Dieser Artikel enthält Antworten auf einige häufig gestellte Fragen zu Canvas.

## Canvas erstellen und bearbeiten {#building-and-editing-canvas}

### Wie viele Schritte kann ich in ein Canvas einfügen? {#how-many-steps-i-can-include-in-a-canvas}

Sie können bis zu 200 Schritte in ein Canvas einfügen.

### Was ist der Unterschied zwischen einer Komponente und einem Schritt? {#whats-the-difference-between-a-component-and-a-step}

Eine [Komponente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about) ist ein einzelner Bestandteil Ihres Canvas, mit dem Sie die Effektivität Ihres Canvas bestimmen können. Komponenten können Aktionen wie das Aufteilen der User Journey, das Hinzufügen einer Verzögerung und sogar das Testen mehrerer Canvas-Pfade umfassen. Ein Schritt in Canvas bezieht sich auf die personalisierte User Journey in Ihren Canvas-Verzweigungen. Im Wesentlichen besteht Ihr Canvas aus einzelnen Komponenten, die Schritte für Ihre User Journey bilden.

### Kann ich ein Canvas mit nicht verbundenen Schritten starten? {#can-i-launch-a-canvas-with-disconnected-steps}

Ja. Sie können Canvases nach dem Start auch mit nicht verbundenen Schritten speichern.

### Wohin gelangen Nutzer:innen, wenn sie einen nicht verbundenen Schritt erreicht haben? {#where-do-users-go-when-theyve-reached-a-disconnected-step}

Wenn sich ein:e Nutzer:in in einem nicht verbundenen Schritt Ihres Canvas-Workflows befindet, wird er/sie zum nachfolgenden Schritt weitergeleitet, sofern einer vorhanden ist, und die Einstellung des Schritts bestimmt, wie der/die Nutzer:in fortschreiten soll. Dies soll es ermöglichen, Änderungen an Schritten vorzunehmen, ohne sie direkt mit dem Rest des Canvas verbinden zu müssen. Außerdem bietet es Spielraum zum Testen, bevor Sie sofort live gehen, und ermöglicht so effektiv das Speichern eines Entwurfs.

Wir empfehlen, die Analytics-Ansicht auf wartende Nutzer:innen in einem Canvas-Schritt zu prüfen, bevor Sie einen Schritt trennen.

### Was passiert, wenn Zielgruppe und Sendezeit für ein Canvas mit einer Variante, aber mehreren Verzweigungen identisch sind? {#what-happens-if-the-audience-and-send-time-are-identical-for-a-canvas-that-has-one-variant-but-multiple-branches}

Wir reihen einen Job für jeden Schritt in die Warteschlange ein – sie laufen ungefähr zur gleichen Zeit, und einer von ihnen „gewinnt“. In der Praxis kann dies einigermaßen gleichmäßig verteilt sein, aber es gibt wahrscheinlich zumindest eine leichte Tendenz zugunsten des Schritts, der zuerst erstellt wurde.

Darüber hinaus können wir keine Garantien dafür geben, wie diese Verteilung genau aussehen wird. Wenn Sie eine gleichmäßige Aufteilung wünschen, fügen Sie einen Filter für [zufällige Bucket-Nummern]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) hinzu.

### Wie werden Canvas-Zielgruppen ausgewertet? {#how-are-canvas-audiences-evaluated}

Standardmäßig werden Filter und Segmente für vollständige Schritte im Canvas zum Sendezeitpunkt geprüft. Der Decision-Split-Schritt führt eine Auswertung direkt nach dem Empfang eines vorherigen Schritts durch (oder vor einer Verzögerung).

### Wann wird ein Ausnahme-Event ausgelöst? {#when-does-an-exception-event-trigger}

Ausnahme-Events werden nur ausgelöst, während der/die Nutzer:in darauf wartet, die zugehörige Canvas-Komponente zu erhalten. Wenn ein:e Nutzer:in eine Aktion im Voraus ausführt, wird das Ausnahme-Event nicht ausgelöst. Wenn Sie Nutzer:innen ausschließen möchten, die ein bestimmtes Event bereits im Voraus ausgeführt haben, verwenden Sie stattdessen [Filter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).

### Wie wirkt sich die Bearbeitung eines Canvas auf Nutzer:innen aus, die sich bereits im Canvas befinden? {#how-does-editing-a-canvas-affect-users-already-in-the-canvas}

Wenn Sie einige Schritte eines mehrstufigen Canvas bearbeiten, erhalten Nutzer:innen, die sich bereits in der Zielgruppe befanden, aber die Schritte noch nicht erhalten haben, die aktualisierte Version der Nachricht. Beachten Sie, dass dies nur geschieht, wenn sie noch nicht für den Schritt ausgewertet wurden.

Weitere Informationen darüber, was Sie nach dem Start bearbeiten können, finden Sie unter [Canvas nach dem Start ändern]({{site.baseurl}}/post-launch_edits).

### Was passiert, wenn Sie ein Canvas stoppen? {#what-happens-when-you-stop-a-canvas}

Wenn Sie ein Canvas stoppen, gilt Folgendes:

- Nutzer:innen werden daran gehindert, das Canvas zu betreten.
- Es werden keine weiteren Nachrichten gesendet, unabhängig davon, wo sich ein:e Nutzer:in im Ablauf befindet.
- **Ausnahme:** Canvases mit E-Mails werden nicht sofort gestoppt. Nachdem die Sendeanfragen an SendGrid übermittelt wurden, können wir nichts mehr tun, um die Zustellung an den/die Nutzer:in zu verhindern.

### Sollte ich ein einzelnes Canvas oder separate Canvases pro Nutzer-Lifecycle erstellen? {#should-i-build-one-canvas-or-separate-canvases-per-user-lifecycle}

Je nachdem, was Sie mit Ihrem Canvas erreichen möchten, benötigen Sie möglicherweise unterschiedliche Ansätze für die Gestaltung Ihrer User Journey. Die Flexibilität von Canvas ermöglicht es Ihnen, User Journeys für jede Phase des Nutzer-Lifecycles abzubilden. Sehen Sie sich unsere [Braze-Canvas-Templates]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates) an, um verschiedene Beispiele für optimierte Ansätze zur Erstellung effektiver User Journeys zu finden.

## Nachrichten und Zustellung {#messages-and-delivery}

### Wann werden In-App-Nachrichten in Canvas gesendet? {#when-are-in-app-messages-in-canvas-sent}

In-App-Nachrichten werden beim nächsten Sitzungsstart gesendet. Das bedeutet: Wenn Nutzer:innen den Canvas-Schritt betreten, bevor der Canvas gestoppt wird, erhalten sie die In-App-Nachricht trotzdem beim nächsten Sitzungsstart – sofern die In-App-Nachricht noch nicht abgelaufen ist.

Es ist möglich, dass Nutzer:innen eine Sitzung starten, bevor der Canvas gestoppt wird, die In-App-Nachricht aber nicht sofort angezeigt wird. Das kann vorkommen, wenn die In-App-Nachricht durch ein angepasstes Event ausgelöst wird oder verzögert ist. In diesem Fall können Nutzer:innen eine In-App-Nachrichten-Impression protokollieren und die In-App-Nachricht „erhalten“, nachdem der Canvas gestoppt wurde. Die Sitzung muss jedoch vor dem Stoppen des Canvas gestartet worden sein, aber **nachdem** die Nutzer:innen den Canvas-Schritt erhalten haben.

{% alert note %}
Das Stoppen eines Canvas führt nicht dazu, dass Nutzer:innen, die auf den Empfang von Nachrichten warten, die User-Journey verlassen. Wenn Sie den Canvas wieder aktivieren und Nutzer:innen noch auf die Nachricht warten, erhalten sie diese (es sei denn, der Zeitpunkt, zu dem die Nachricht hätte gesendet werden sollen, ist bereits verstrichen – dann erhalten sie die Nachricht nicht).
{% endalert %}

### Warum kann ein Canvas null Sends anzeigen, obwohl Impressionen protokolliert werden? {#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged}

Wenn _Gesendete Nachrichten_ für einen Canvas mit einem In-App-Nachrichten-Schritt immer null sind, liegt das daran, dass die Zustellung von In-App-Nachrichten anders funktioniert als bei anderen Messaging-Kanälen.

In-App-Nachrichten werden vom SDK „abgerufen“ und nicht von Braze „gepusht“. In-App-Nachrichten für berechtigte Nutzer:innen werden automatisch beim Sitzungsstart zugestellt und „warten“ auf das Trigger-Event, bevor sie angezeigt werden. Da berechtigte Nutzer:innen die Nachricht beim Start einer Sitzung erhalten, meldet Braze dies nicht als Send-Event. Wenn Nutzer:innen das Trigger-Event ausführen, wird die Nachricht angezeigt und Braze protokolliert eine Impression und markiert den Canvas-Schritt (oder die Campaign) als empfangen im Nutzerprofil. Folglich ist die Gesamtzahl der _Sends_ für In-App-Nachrichten null.

### Warum haben Nutzer:innen meine In-App-Nachricht nach einer langen Verzögerung oder Verzweigung nicht erhalten? {#why-didnt-users-receive-my-in-app-message-after-a-long-delay-or-branch}

Nachdem vorgelagerte [Verzögerungs]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step)-Schritte und Zielgruppenprüfungen abgeschlossen sind, werden Nutzer:innen erst dann für eine In-App-Nachricht berechtigt, wenn sie den Nachrichten-Schritt erreichen. Wenn die Nachricht an einem Kalenderdatum oder innerhalb eines kurzen Zeitfensters **nach Verfügbarkeit des Schritts** abläuft, können Nutzer:innen auf langsameren Pfaden nach dem Ablauf ankommen und die Nachricht nie sehen. Stimmen Sie den Ablauf auf Ihre längsten realistischen Pfadverzögerungen ab. Weitere Informationen und Beispiele finden Sie unter [Ablauf von In-App-Nachrichten]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas#in-app-message-expiration).

### Warum sehe ich „Canvas Entry Properties may not be used in In-App Messages.“? {#why-do-i-see-canvas-entry-properties-may-not-be-used-in-in-app-messages}

Diese Meldung erscheint, wenn die Personalisierung auf Felder verweist, die In-App-Nachrichten in Canvas nicht auflösen können. Verwenden Sie das `context`-Objekt wie unter [Kontext- und Event-Eigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) und [Nachrichten-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) beschrieben. Der Legacy-Liquid-Namespace `canvas_entry_properties` hat andere Einschränkungen als `context`. Wenn Sie Werte über mehrere Schritte hinweg beibehalten müssen, prüfen Sie [persistente Eigenschaften im ursprünglichen Canvas-Editor]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties) mit Ihrem Braze-Team. Gespeicherte Werte werden gelöscht, wenn Nutzer:innen den Canvas verlassen, bevor das Gerät die In-App-Payload heruntergeladen hat.

### Wo finde ich Button-Klicks für Drag-and-Drop-In-App-Nachrichten in Canvas? {#where-can-i-find-button-clicks-for-drag-and-drop-in-app-messages-in-canvas}

Metriken auf Button-Ebene für Drag-and-Drop-In-App-Nachrichten erscheinen auf der Analytics-Karte des **Nachrichten**-Schritts unter **Canvas-Details**, nicht nur in der übergeordneten Canvas-Zusammenfassung. Öffnen Sie den Canvas, wählen Sie den Nachrichten-Schritt aus und überprüfen Sie dort das In-App-Engagement. Informationen zu Reporting-Konzepten finden Sie unter [Messen und Testen mit Canvas-Analytics]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics).

### Kann ich für jede Variante im selben Canvas-Nachrichten-Schritt oder multivariaten Versand unterschiedliche Sendezeiten planen? {#can-i-schedule-different-send-times-for-each-variant-in-the-same-canvas-message-step-or-multivariate-send}

Nein. Varianten in derselben multivariaten Konfiguration oder im selben Nachrichten-Schritt teilen sich einen Zustellungszeitplan. Sie können nicht eine Variante um 18 Uhr und eine andere um 19 Uhr für denselben geplanten Versand festlegen.

Um Versendungen zu staffeln oder unterschiedliche Zeiten pro Pfad zu verwenden, probieren Sie die folgenden Methoden:

- Separate Nachrichten-Schritte mit Verzögerungsschritten dazwischen, sodass jede Nachricht ihren eigenen Zeitplan hat.
- Verzweigungen oder einen [Experimentpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step)-Schritt, damit Nutzer:innen Pfaden mit unterschiedlichem Timing folgen.
- Separate Campaigns, wenn der Anwendungsfall nicht innerhalb eines Canvas bleiben muss.

Informationen zu multivariaten und A/B-Konzepten in Campaigns finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing).

### Was passiert, wenn Nutzer:innen an einem Canvas-Nachrichten-Schritt durch globales Frequency-Capping begrenzt werden? {#what-happens-if-a-user-is-global-frequency-capped-at-a-canvas-message-step}

Sie erhalten den Versand für den begrenzten Kanal nicht, aber Nachrichten-Schritte bringen Nutzer:innen trotzdem voran, wenn eine Nachricht aufgrund von globalem Frequency-Capping nicht gesendet wird. Informationen zu den schrittweisen Fortschrittsfällen finden Sie unter [Wie Nutzer:innen voranschreiten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance). Globales Frequency-Capping allein führt nicht dazu, dass Nutzer:innen einen Canvas verlassen; dieses Verhalten ist unabhängig von den **Zustellungsvalidierungen** eines Nachrichten-Schritts. Weitere Details finden Sie unter [Rate-Limiting und Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping).

### Warum sind die Sends niedriger als die geschätzte Zielgruppengröße? {#why-are-sends-lower-than-the-estimated-audience-size}

Sends können aus vielen der gleichen Gründe niedriger sein als die **geschätzte Zielgruppe** wie bei [Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/faq#why-are-sends-lower-than-the-estimated-audience-size), einschließlich Frequency-Caps, strikter Geräte- oder Browser-Filter, Wiedereintritts-Fenster, Rate-Limiting und kanalspezifischer Ausschlüsse (z. B. Push-Erreichbarkeit oder E-Mail-Abo- und Zustellbarkeitsprüfungen).

Canvas-spezifische Faktoren gelten ebenfalls:

- **Aktionsbasierter oder API-ausgelöster Eintritt:** Nutzer:innen treten erst ein (und erhalten Schritte), nachdem sie das Eintrittsverhalten ausgeführt haben, sodass die tatsächlichen Sends hinter der Vorabschätzung zurückbleiben, bis diese Aktionen stattfinden.
- **Zielgruppenpfade:** Nutzer:innen werden zum Zweig mit der höchsten Priorität geleitet, für den sie sich qualifizieren, sodass nachgelagerte Zweige weniger Nutzer:innen erhalten können, als eine flache Segmentzählung vermuten lässt.
- **Zielgruppen- und Sendezeitprüfungen:** Vollständige Schritte werten Filter zum Sendezeitpunkt erneut aus, sofern Sie nichts anderes konfigurieren. Nutzer:innen, die sich bei der Erstellung des Canvas qualifiziert haben, können vor dem Versand einer Nachricht herausfallen.
- **Kontrollgruppen:** Globale oder Canvas-Kontrollgruppen halten einen Anteil der Eintretenden vom Messaging zurück.
- **Ruhezeiten und Verzögerungen:** Nachrichten können zurückgehalten oder neu geplant werden, wodurch Sends aus dem Berichtszeitraum verschoben werden, den Sie betrachten.
- **Maximale Eintritts- oder Zielgruppen-Caps:** Eintritts- oder Sende-Caps stoppen zusätzliche Nutzer:innen, selbst wenn das zugrunde liegende Segment größer ist.
- **Berichtszeitraum:** Der Analytics-Bereich umfasst möglicherweise nicht jeden Send, den Sie mit der Schätzung vergleichen.

### Warum stimmen geschätzte Zielgruppe und Canvas-Nutzerzahlen nicht überein? {#why-dont-estimated-audience-and-canvas-user-counts-match}

Die **geschätzte Zielgruppe** spiegelt wider, wer zum Zeitpunkt der Schätzung Ihrem Segment und Ihren Eintrittsfiltern entspricht. Nach diesem Zeitpunkt können verzögerte oder aktionsbasierte Eintritte, Wiedereintritt, API-Trigger oder Verzweigungsrouting die Anzahl der Profile erhöhen, die die Journey berühren, im Vergleich zum Snapshot. Nutzer:innen können auch herausfallen, wenn Sendezeitfilter fehlschlagen, was die tatsächlichen Eintritte oder Sends verringert. Vergleichen Sie Timing, Caps und Auswertungseinstellungen zusammen mit [Warum sind die Sends niedriger als die geschätzte Zielgruppengröße?](#why-are-sends-lower-than-the-estimated-audience-size).

### Warum ist _Eindeutige Empfänger:innen_ höher als die Anzahl der Nutzer:innen, die ich angesprochen habe? {#why-is-_unique-recipients_-higher-than-the-number-of-users-i-targeted}

_Eindeutige Empfänger:innen_ kann höher sein als die erwartete Zielgruppe, da Braze **eindeutige tägliche Empfänger:innen** für Canvas- und Campaign-Reporting erfasst. Dies unterstützt eine genaue Konversions-Attribution jedes Mal, wenn Nutzer:innen eine Nachricht in der Journey erhalten.

Wenn Nutzer:innen beispielsweise am Montag einen Canvas-Schritt erhalten und am Freitag erneut und nach jedem Versand konvertieren, kann Braze zwei Empfängerzeilen und zwei zugehörige Konversionen zählen. Bei wiederkehrenden Eintritten oder Wiedereintritt kann dieselbe kleine Gruppe von Profilen über mehrere Tage hinweg mehrere _Eindeutige Empfänger:innen_ erzeugen.

### Warum verzeichnet mein Canvas niedrigere Sendraten? {#why-is-my-canvas-experiencing-lower-send-rates}

Wenn Sie feststellen, dass Ihr täglich geplanter Canvas im Laufe der Zeit an weniger Nutzer:innen sendet, prüfen Sie Folgendes:

- **Prüfen Sie, ob Wiedereintritt aktiviert ist:** Ohne Wiedereintritt lässt Braze jede:n Nutzer:in nur einmal in den Canvas eintreten. Bei täglich geplanten Canvases sind nur Nutzer:innen berechtigt, die der Zielgruppe entsprechen und den Canvas noch nicht betreten haben. Je mehr Nutzer:innen eintreten, desto weniger berechtigte Nutzer:innen gibt es bei jedem späteren Eintritt, sodass das Eintrittsvolumen sinkt.
- **Prüfen Sie, ob die Zielgruppe eine feste Mitgliedschaft hat:** Zielgruppen, die aus einer festen Nutzerliste erstellt wurden (z. B. ein [CSV-Import]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import), der als Segmentfilter verwendet wird), gewinnen nicht automatisch neue Mitglieder. Ohne neue Eintritte kann das Eintrittsvolumen nicht wieder ansteigen, wenn Nutzer:innen den Canvas betreten.

Informationen zu [Rate-Limits für die Zustellgeschwindigkeit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) und anderen Faktoren, die Sends für ein einzelnes Vorkommen verringern, finden Sie unter [Warum sind die Sends niedriger als die geschätzte Zielgruppengröße?](#why-are-sends-lower-than-the-estimated-audience-size).

## Analytics und Konversionen {#analytics-and-conversions}

### Wie werden Nutzerkonversionen in einem Canvas verfolgt? {#how-are-user-conversions-tracked-in-a-canvas}

Nutzer:innen können pro Canvas-Eintritt nur einmal konvertieren. Konversionen werden der zuletzt empfangenen Nachricht zugeordnet, die Nutzer:innen für diesen Eintritt erhalten haben. Der Zusammenfassungsblock am Anfang eines Canvas zeigt alle Konversionen an, die von Nutzer:innen innerhalb dieses Pfads durchgeführt wurden – unabhängig davon, ob sie eine Nachricht erhalten haben. Jeder nachfolgende Schritt zeigt nur Konversionen an, die stattfanden, während dieser Schritt der zuletzt empfangene war.

{% alert note %}
Wenn Nutzer:innen erneut in ein Canvas eintreten, werden Konversions-Events nur für den letzten Eintritt verfolgt. Konversions-Events werden nicht für vorherige Eintritte protokolliert, selbst wenn das Konversions-Event nachträglich ergänzt wird.
{% endalert %}

{% details Für Beispiele aufklappen %}

**Beispiel 1**

Es gibt einen Canvas-Pfad mit 10 Push-Benachrichtigungen und das Konversions-Event ist „Sitzungsstart“ („App öffnen“):

- Nutzer:in A öffnet die App nach dem Eintritt, aber bevor die erste Nachricht empfangen wird.
- Nutzer:in B öffnet die App nach jeder Push-Benachrichtigung.

**Ergebnis:** Die Zusammenfassung zeigt zwei Konversionen an, während die einzelnen Schritte eine Konversion beim ersten Schritt und null bei allen nachfolgenden Schritten anzeigen.

{% alert note %}
Wenn Ruhezeiten aktiv sind, wenn das Konversions-Event eintritt, gelten dieselben Regeln.
{% endalert %}

**Beispiel 2**

Es gibt ein Canvas mit einem Schritt und aktivierten Ruhezeiten:

1. Nutzer:in tritt in das Canvas ein.
2. Der erste Schritt hat keine Verzögerung, liegt aber innerhalb der festgelegten Ruhezeiten, sodass die Nachricht unterdrückt wird.
3. Nutzer:in führt das Konversions-Event aus.

**Ergebnis:** Die/der Nutzer:in wird als konvertiert in der gesamten Canvas-Variante gezählt, aber nicht im Schritt, da sie/er den Schritt nicht erhalten hat.

{% enddetails %}

### Was ist der Unterschied zwischen den verschiedenen Konversionsratentypen? {#whats-the-difference-between-the-different-conversion-rate-types}

- Die Gesamtkonversionen eines Canvas zeigen, wie viele eindeutige Nutzer:innen ein Konversions-Event abgeschlossen haben, nicht wie viele Konversionen sie jeweils durchgeführt haben.
- Die Variantenkonversionsrate oder der Zusammenfassungsblock am Anfang eines Canvas zeigt alle Konversionen, die von Nutzer:innen innerhalb dieses Pfads durchgeführt wurden, als Gesamtsumme an – unabhängig davon, ob sie eine Nachricht erhalten haben.
- Die Schrittkonversionsrate zeigt, wie viele Personen diesen Nachrichtenschritt erhalten und eines der definierten Konversions-Events abgeschlossen haben.

### Warum ist meine Canvas-Schrittkonversionsrate nicht gleich meiner Canvas-Variantengesamtkonversionsrate? {#why-is-my-canvas-step-conversion-rate-not-equal-to-my-canvas-variant-total-conversion-rate}

Es ist üblich, dass die Konversionsgesamtzahl einer Canvas-Variante größer ist als die Summe der Schrittgesamtzahlen. Dies geschieht, weil Nutzer:innen ein Konversions-Event für eine Variante ausführen können, sobald sie die Variante betreten. Dasselbe Konversions-Event zählt jedoch nicht für einen Canvas-Schritt. Nutzer:innen, die in das Canvas eintreten und das Konversions-Event vor dem Empfang des ersten Canvas-Schritts ausführen, werden also zur Variantenkonversionsgesamtzahl gezählt, nicht zur Schrittgesamtzahl. Dasselbe gilt für Nutzer:innen, die in das Canvas eintreten, es aber verlassen, bevor sie einen Schritt erhalten.

Beachten Sie, dass es auch möglich ist, dass Nutzer:innen eine Variante betreten, keine Nachricht von einem Schritt erhalten und dann konvertieren. In diesem Fall wird keine Konversion auf Schrittebene protokolliert. Da die/der Nutzer:in jedoch technisch gesehen konvertiert hat, wird eine Konversion auf Canvas-Ebene protokolliert.

### Wie kann ich bestätigen, ob meine Nutzer:innen ein API-getriggertes Canvas erhalten haben? {#how-can-i-confirm-if-my-users-received-an-api-triggered-canvas}

Sie können [ein Segment erstellen]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment), indem Sie einen Canvas-Filter verwenden, um zu bestätigen, ob Nutzer:innen in das Canvas eingetreten sind oder einen bestimmten Canvas-Schritt erhalten haben. Verwenden Sie beispielsweise einen Canvas-Eintrittsfilter, wenn Sie bestätigen möchten, dass Nutzer:innen in das API-getriggerte Canvas eingetreten sind, oder einen Filter für empfangene Schritte, wenn Sie bestätigen möchten, dass sie eine Nachricht aus dem Canvas erhalten haben. Verwenden Sie dann den [`/users/export/segment`-Endpunkt]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment), um die Nutzer:innen in diesem Segment zu exportieren.

### Kann ich ein Canvas löschen? {#can-i-delete-a-canvas}

Nein, aber Sie können [ein Canvas archivieren]({{site.baseurl}}/user_guide/messaging/governance/archiving).

### Wie setze ich ein archiviertes Canvas oder eine archivierte Campaign fort? {#how-do-i-resume-an-archived-canvas-or-campaign}

Archivierte Nachrichten werden nicht gesendet, bis Sie sie in einen bearbeitbaren Zustand zurückversetzen. [Dearchivieren]({{site.baseurl}}/user_guide/messaging/governance/archiving#unarchiving) Sie die Campaign oder das Canvas, legen Sie den Eintrittszeitplan oder die Sendezeit auf ein zukünftiges Fenster fest (oder duplizieren Sie die Journey, wenn Sie eine saubere Kopie benötigen), und wählen Sie dann **Fortsetzen** oder starten Sie nach Bedarf. Weitere Informationen finden Sie unter [Campaigns und Canvases archivieren]({{site.baseurl}}/user_guide/messaging/governance/archiving).

### Warum wird mein Canvas nicht gespeichert, obwohl kein Fehler angezeigt wird? {#why-doesnt-my-canvas-save-when-no-error-appears}

Leere **Angepasstes Attribut**-Filter in Zielgruppen- oder Schrittfiltern können das Speichern blockieren, ohne eine detaillierte Validierungsmeldung anzuzeigen. Öffnen Sie jede Filterkarte, entfernen Sie unvollständige Regeln für angepasste Attribute oder geben Sie sowohl den Attributnamen als auch den Wert ein, und wählen Sie dann erneut **Speichern**.

### Warum ist ein Tag von meinem Canvas oder meiner Campaign verschwunden? {#why-did-a-tag-disappear-from-my-canvas-or-campaign}

Wenn ein [Tag]({{site.baseurl}}/user_guide/messaging/governance/tags) aus Ihrem Workspace gelöscht wird, entfernt Braze es aus jeder Campaign und jedem Canvas, die darauf verwiesen haben. Diese Bereinigung erzeugt nicht immer einen eigenen Eintrag im Canvas-Änderungsprotokoll.

### Wie kann ich Analytics für jede meiner Canvas-Komponenten anzeigen? {#how-can-i-view-analytics-for-each-of-my-canvas-components}

Um die Analytics einer Canvas-Komponente anzuzeigen, navigieren Sie zu Ihrem Canvas und scrollen Sie auf der Seite **Canvas-Details** nach unten. Hier können Sie die Analytics jeder Komponente einsehen. Weitere Details finden Sie unter [Canvas-Analytics]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics).

### Wann ist das Engagement eines Canvas-Schritts im Nutzerprofil sichtbar? {#when-is-engagement-from-a-canvas-step-visible-on-a-user-profile}

Filter wie `Received Message from Canvas Step` werden aktualisiert, nachdem Braze das entsprechende Sende-, Empfangs- oder Engagement-Event für diesen Schritt protokolliert hat. In-App-Nachrichten können Impressionen getrennt von sendebezogenen Metriken protokollieren. Siehe [Warum kann ein Canvas null Sends anzeigen, obwohl Impressionen protokolliert werden?](#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged). Dieselben Events erscheinen in den Schrittmetriken unter **Canvas-Details**.

### Ist Canvas-Analytics oder der Segmentierer genauer, wenn man die Anzahl eindeutiger Nutzer:innen betrachtet? {#when-looking-at-the-number-of-unique-users-is-canvas-analytics-or-the-segmenter-more-accurate}

Der Segmentierer liefert eine genauere Statistik für eindeutige Nutzerdaten als Canvas- oder Campaign-Statistiken. Das liegt daran, dass Canvas- und Campaign-Statistiken Zahlen sind, die Braze inkrementiert, wenn etwas passiert – was bedeutet, dass es Variablen gibt, die dazu führen können, dass diese Zahl von der des Segmentierers abweicht. Beispielsweise können Nutzer:innen mehr als einmal für ein Canvas oder eine Campaign konvertieren.

### Warum weicht die Anzahl der Nutzer:innen, die in ein Canvas eintreten, von der erwarteten Anzahl ab? {#why-does-the-number-of-users-entering-a-canvas-not-match-the-expected-number}

Die Anzahl der Nutzer:innen, die in ein Canvas eintreten, kann von Ihrer erwarteten Anzahl abweichen, da Zielgruppen und Trigger unterschiedlich ausgewertet werden. In Braze wird eine Zielgruppe vor dem Trigger ausgewertet (es sei denn, es wird ein [Attributänderungs]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)-Trigger verwendet). Dies führt dazu, dass Nutzer:innen aus dem Canvas ausscheiden, wenn sie nicht Teil Ihrer ausgewählten Zielgruppe sind, bevor Trigger-Aktionen ausgewertet werden.

### Was passiert mit anonymen Nutzer:innen während ihrer Canvas-Journey? {#what-happens-to-anonymous-users-during-their-canvas-journey}

Obwohl anonyme Nutzer:innen in Canvases eintreten und diese verlassen können, werden ihre Aktionen erst dann einem bestimmten Nutzerprofil zugeordnet, wenn sie identifiziert werden, sodass ihre Interaktionen möglicherweise nicht vollständig in Ihren Analytics verfolgt werden. Sie können den [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder) verwenden, um einen Bericht über diese Metriken zu erstellen.

{% alert tip %}
Für weitere Unterstützung bei der Canvas-Fehlerbehebung wenden Sie sich bitte innerhalb von 30 Tagen nach Auftreten Ihres Problems an den Braze-Support, da uns nur die Diagnoseprotokolle der letzten 30 Tage zur Verfügung stehen.
{% endalert %}

### Kann ich Nutzer:innen, die sich derzeit in einer Canvas-Journey befinden, von einer Campaign oder einem Segment ausschließen? {#can-i-exclude-users-who-are-currently-in-a-canvas-journey-from-a-campaign-or-segment}

Verwenden Sie [Segmentierungsfilter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) wie `Entered Canvas Variation`, `In Canvas Control Group` oder `Received Message from Canvas Step`, um Nutzer:innen basierend auf Canvas-Eintritt, Variantenzuweisung oder Schritt-Engagement anzusprechen. Diese Filter werten den Eintrittsverlauf und die Interaktionen aus – sie geben nicht an, ob Nutzer:innen noch eine aktive Journey durchlaufen.

Um Nutzer:innen basierend auf aktiver Canvas-Teilnahme ein- oder auszuschließen, fügen Sie [Nutzeraktualisierungs]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)-Schritte beim Canvas-Eintritt und -Austritt hinzu, um angepasste Attribute zu setzen und zu löschen, und filtern Sie dann in Campaigns oder Segmenten nach diesen Attributen.

## Segmentierung {#segmentation}

### Was ist der Unterschied zwischen „Hat keine Canvas-Variante betreten“ und „Ist nicht in der Canvas-Kontrollgruppe“? {#what-is-the-difference-between-has-not-entered-canvas-variation-and-is-not-in-canvas-control-group}

Die vollständigen Filterdefinitionen finden Sie unter [Segmentierungsfilter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).

#### Hat keine Canvas-Variante betreten {#has-not-entered-canvas-variation}

Die/der Nutzer:in hat nie einen Varianten-Pfad eines bestimmten Canvas betreten. Alle Nutzer:innen, die sich nicht in der Kontrollgruppe befinden, sind eingeschlossen – unabhängig davon, ob sie das Canvas betreten haben. Dazu gehören Nutzer:innen, die eine andere Variante betreten haben, und Nutzer:innen, die keine Variante betreten haben.

#### Ist nicht in der Canvas-Kontrollgruppe {#is-not-in-canvas-control-group}

Die/der Nutzer:in hat das Canvas betreten, befindet sich aber nicht in der Kontrollgruppe und hat folglich eine Variante erhalten. Dies umfasst nur Nutzer:innen, die das Canvas betreten haben.

Beachten Sie, dass die Variantenzuweisung beim Eintritt in das Canvas erfolgt. Wenn ein:e Nutzer:in ein Canvas nicht betreten hat, wird ihr/ihm keine Variante zugewiesen. Mit anderen Worten: Sie befinden sich weder in der Kontrollgruppe noch in einer Variante.

## Originaler Canvas-Editor {#original-canvas-editor}

{% details Für FAQ zum originalen Canvas-Editor aufklappen %}

### Wie konvertiere ich ein bestehendes Canvas vom originalen Editor zum aktuellen Editor? {#how-do-i-convert-an-existing-canvas-from-the-original-editor-to-the-current-editor}

Sie können [Ihr Canvas klonen]({{site.baseurl}}/cloning_canvases). Dadurch wird eine Kopie Ihres originalen Canvas im aktuellsten Canvas-Workflow erstellt.

### Was sind die Hauptunterschiede zwischen dem aktuellen und dem originalen Canvas-Editor? {#what-are-the-main-differences-between-the-current-and-original-canvas-editors}

#### Canvas-Komponenten-Symbolleiste {#canvas-component-toolbar}

Zuvor wurde im originalen Canvas-Editor standardmäßig ein vollständiger Schritt hinzugefügt, wenn Sie einen Schritt in Ihrer User Journey erstellt haben. Diese vollständigen Schritte werden durch verschiedene Canvas-Komponenten ersetzt, was Ihnen den Vorteil einer besseren Übersichtlichkeit und Anpassbarkeit für Ihre Bearbeitungserfahrung bietet. Sie können alle Ihre Canvas-Komponenten sofort über die Canvas-Schritt-Symbolleiste sehen.

#### Schrittverhalten {#step-behavior}

Zuvor enthielt jeder vollständige Schritt Informationen wie Verzögerungs- und Zeitplaneinstellungen, Ausnahme-Events, Zielgruppenfilter, Nachrichtenkonfiguration und Optionen zum Nachrichtenfortschritt – alles in einer Komponente. Im aktuellen Editor sind dies separate Einstellungen, um Ihre Canvas-Erstellung anpassbarer zu gestalten, und es gibt einige Unterschiede in der Funktionalität.

#### Fortschritt bei Nachrichtenkomponenten {#message-component-advancement}

[Nachrichtenkomponenten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) lassen alle Nutzer:innen, die den Schritt betreten, fortschreiten. Es ist nicht erforderlich, ein Fortschrittsverhalten für Nachrichten festzulegen, was die Konfiguration des gesamten Schritts vereinfacht. Wenn Sie die Option **Bei gesendeter Nachricht fortschreiten** implementieren möchten, fügen Sie einen separaten Zielgruppenpfad hinzu, um Nutzer:innen herauszufiltern, die den vorherigen Schritt nicht erhalten haben.

#### Verzögerungsverhalten „in“ {#delay-in-behavior}

[Verzögerungskomponenten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) warten die gesamte Verzögerungszeit ab, bevor sie zum nächsten Schritt übergehen.

Nehmen wir an, am 12. April haben wir eine Verzögerungskomponente, bei der die Verzögerung so eingestellt ist, dass Nutzer:innen am nächsten Tag um 14 Uhr zum nächsten Schritt weitergeleitet werden. Ein:e Nutzer:in betritt die Komponente am 13. April um 14:01 Uhr.
- Im originalen Workflow würde der/die Nutzer:in am 14. April um 14 Uhr zum nächsten Schritt übergehen, was weniger als ein Tag ab dem Eintrittszeitpunkt ist.
- Im aktuellen Editor würde der/die Nutzer:in am 15. April um 14 Uhr zum nächsten Schritt übergehen. Beachten Sie, dass dies die gleiche Uhrzeit ist, aber mehr als ein Tag ab dem Eintrittszeitpunkt.

#### Verhalten bei intelligentem Timing {#intelligent-timing-behavior}

Da [intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) in der Nachrichtenkomponente gespeichert ist, werden Verzögerungen vor den Berechnungen des intelligenten Timings angewendet. Das bedeutet, dass Nutzer:innen je nach Eintrittszeitpunkt in die Komponente die Nachricht möglicherweise später erhalten als in einem Canvas, das mit dem originalen Canvas-Workflow erstellt wurde.

Nehmen wir an, Ihre Verzögerung ist auf 2 Tage eingestellt, intelligentes Timing ist aktiviert und hat festgestellt, dass die beste Sendezeit 14 Uhr ist. Ein:e Nutzer:in betritt den Verzögerungsschritt um 14:01 Uhr.
- **Aktueller Workflow:** Es dauert 48 Stunden, bis die Verzögerung abgelaufen ist, sodass der/die Nutzer:in die Nachricht am dritten Tag um 14 Uhr erhält.
- **Originaler Workflow:** Der/die Nutzer:in erhält die Nachricht am zweiten Tag um 14 Uhr.

Beachten Sie: Wenn intelligentes Timing aktiviert ist, wird die Nachricht innerhalb von 24 Stunden nach dem Eintritt des/der Nutzer:in in die Nachrichtenkomponente zur ermittelten intelligenten Zeit gesendet (auch wenn keine Verzögerungskomponente beteiligt ist).

#### Ausnahme-Events {#exception-events}

##### Ruhezeiten {#quiet-hours}

Ausnahme-Events werden mithilfe von Aktionspfaden angewendet, die von Nachrichtenschritten getrennt sind. Ruhezeiten werden in der Nachrichtenkomponente durchgesetzt. Das bedeutet: Wenn ein:e Nutzer:in den Aktionspfad bereits passiert hat (und nicht durch das Ausnahme-Event ausgeschlossen wurde), dann auf Ruhezeiten trifft, wenn er/sie die Nachrichtenkomponente erreicht, und das Canvas so konfiguriert ist, dass die Nachricht nach der Ruhezeitenperiode erneut gesendet wird, wird das Ausnahme-Event nicht mehr angewendet. Beachten Sie, dass dieser Anwendungsfall nicht häufig vorkommt.

Für Segmente und Filter verfügt der Nachrichtenschritt über Zustellungsvalidierungen, mit denen Nutzer:innen zusätzliche Segmente und Filter konfigurieren können, die zum Sendezeitpunkt validiert werden. Dies verhindert den oben genannten Grenzfall bei Ruhezeiten.

##### Zeitplaneinstellung „in“ oder „am nächsten“ {#in-or-on-the-next-schedule-setting}

Ausnahme-Events werden mithilfe von Aktionspfaden erstellt. Aktionspfade unterstützen nur „nach einem X-Zeitfenster“ und nicht „in X Zeit“ oder „am nächsten X Zeitpunkt“.

{% enddetails %}

### Was sollte ich angeben, wenn ich ein Support-Ticket für einen „Request Timed Out“-Fehler einreiche? {#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error}

Wenn beim Bearbeiten eines Canvas ein „Request Timed Out“-Fehler auftritt und Sie den [Braze-Support]({{site.baseurl}}/braze_support) kontaktieren müssen, geben Sie die folgenden Informationen an, um die Lösung zu beschleunigen:

{% multi_lang_include messaging/support_ticket_request_timed_out_details.md context='canvas' %}

## Canvas-Zustellung und Fehlerbehebung {#canvas-delivery-and-troubleshooting}

### Sind verwaiste Nutzer:innen berechtigt, Canvas-Nachrichten zu erhalten? {#are-orphaned-users-eligible-to-receive-canvas-messages}

Nein. [Verwaiste Nutzer:innen]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#what-happens-when-you-identify-anonymous-users) sind nicht berechtigt, Nachrichten zu erhalten. Wenn ein Profil verwaist wird, während sich ein:e Nutzer:in in einem Canvas-Journey befindet, verlässt er/sie den Flow stillschweigend. Analytics zeigt möglicherweise nicht immer ein **Exited**-Event für diesen Exit an, und die Workflow-Zusammenfassung kann ein `partial_update_token` ohne `exited_date` oder `exit_reason` enthalten.

Weitere Informationen zu Zusammenführungen und verwaisten Profilen finden Sie unter [Doppelte Nutzer:innen zusammenführen]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users).

### Werden bereits an den ESP gesendete Nachrichten noch zugestellt, wenn ich ein aktives Canvas oder eine Campaign stoppe? {#if-i-stop-an-active-canvas-or-campaign-do-messages-already-sent-to-the-esp-still-deliver}

Ja. Nachdem Braze eine Anfrage an Ihren E-Mail-Anbieter (ESP) gesendet hat, kann Braze diesen Versand nicht mehr zurückrufen. Das Stoppen eines Canvas oder einer Campaign verhindert neue Versandanfragen, aber bereits an den ESP übergebene Nachrichten können weiterhin zugestellt werden und die Versandzähler erhöhen, während der ESP sie verarbeitet.

Dies entspricht dem Verhalten, das unter [Stoppen eines Canvas](#what-happens-when-you-stop-a-canvas) beschrieben wird: E-Mail-Versendungen, die sich bereits im Versand befinden, werden nicht sofort angehalten.

### Wie kann ich bestätigen, dass ein Canvas-Webhook-Schritt ohne nutzersichtbaren Inhalt ausgelöst wurde? {#how-can-i-confirm-a-canvas-webhook-step-fired-without-user-visible-content}

Braze erfasst Webhook-**Sends** und zugehörige Zustellungsergebnisse für [Webhook]({{site.baseurl}}/user_guide/channels/webhooks)-Schritte in Campaigns und Canvases. Verwenden Sie die Schritt-Analytics, das [Webhook-Reporting]({{site.baseurl}}/user_guide/channels/webhooks/reporting) oder [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)-Webhook-Events, um zu bestätigen, dass der Schritt ausgeführt wurde. Die Anfrage-Logs Ihres Endpunkts bieten zusätzliche Bestätigung, wenn Sie einen serverseitigen Empfangsnachweis benötigen.

Braze enthält kein integriertes unsichtbares Tracking-Pixel für Webhook-Schritte. Verlassen Sie sich auf die Braze-Webhook-Metriken und Ihr Endpunkt-Logging anstelle von benutzerdefinierten Ein-Pixel-Bildanfragen.

### Warum ist ein:e Nutzer:in seltener in ein Canvas eingetreten, als er/sie das Trigger-Event ausgeführt hat? {#why-did-a-user-enter-a-canvas-fewer-times-than-they-performed-the-trigger-event}

Bei aktionsbasierten und API-getriggerten Canvases dedupliziert Braze Trigger-Events, sodass ein:e Nutzer:in für dasselbe Canvas höchstens etwa **einmal pro Sekunde** eintreten kann. Wenn ein:e Nutzer:in dasselbe Trigger-Event mehrmals innerhalb einer Sekunde ausführt, wird nur ein Eintritt verarbeitet.

Um mehrere Eintritte in derselben Sekunde zu ermöglichen, planen Sie Trigger-Events mit einem Abstand von mindestens 1,1 Sekunden (z. B. wenn Sie das Event-Timing von Ihrem Server aus steuern). Für Campaign-ähnliches Verhalten, das mehrere gleichzeitige Trigger erlaubt, vergleichen Sie Ihren Anwendungsfall mit [Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns) mit entsprechenden Zeitplan- und Wiederzulassungseinstellungen.

### Warum geht ein Test-Push an die falsche App, aber Live-Versendungen sehen korrekt aus? {#why-does-a-test-push-go-to-the-wrong-app-but-live-sends-look-correct}

**Test-Push** auf einem Nutzerprofil wird an jedes Push-fähige Gerät für dieses Profil zugestellt. Wenn mehrere Apps auf einem Gerät installiert sind, stellt das Betriebssystem die Testbenachrichtigung in der Regel an die erste verfügbare App zu, die möglicherweise nicht die App ist, die Sie validieren möchten.

Um app-spezifisches Targeting zu bestätigen, senden Sie eine Live- oder Testnachricht über eine Campaign oder ein Canvas mit einer engen Zielgruppe (z. B. filtern Sie nach `external_id`), anstatt sich allein auf **Test-Push** im Profil zu verlassen.

Aktivieren Sie bei **Canvas**-Nachrichtenschritten mit mehreren Apps die Option **Validate audience at message send** im Nachrichtenschritt, damit Segment- und Filterprüfungen zum Sendezeitpunkt ausgeführt werden. Weitere Informationen finden Sie unter [Nachrichtenschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step).

Allgemeine Informationen zum Test-Push-Verhalten finden Sie unter [Testnachrichten senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) und [Push-FAQ]({{site.baseurl}}/user_guide/channels/push/faqs).

### Wie debugge ich Push Stories auf iOS und Android? {#how-do-i-debug-push-stories-on-ios-and-android}

Beginnen Sie mit [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories) für die Einrichtung und die kreativen Anforderungen. Informationen zur Implementierung und zur Handhabung von Rich-Benachrichtigungen finden Sie unter [Rich-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/rich) und [Push Stories]({{site.baseurl}}/developer_guide/push_notifications/push_stories) im Entwicklerhandbuch.

### Wer erhält die E-Mail „Canvas Messages Delayed 24+ Hours“? {#who-receives-the-canvas-messages-delayed-24-hours-email}

Braze sendet diese Benachrichtigung, wenn Canvas-Nachrichten durch Rate-Limiting 24 Stunden oder länger verzögert werden. Die E-Mail geht an Dashboard-Nutzer:innen, die zuvor Änderungen am betroffenen Canvas vorgenommen haben (basierend auf den Canvas-Änderungsprotokollen). Wenn Braze diese Empfänger:innen nicht ermitteln kann, geht die E-Mail an die **Unternehmensadministrator:innen** des Workspace.

### Wann hört ein:e Nutzer:in auf, Nachrichten nach einem Ausnahme-Event zu erhalten? {#when-does-a-user-stop-receiving-messages-after-an-exception-event}

Braze erfasst den Exit, sobald das Ausnahme-Event eintritt, aber Nutzer:innen können innerhalb eines Schritts verbleiben, bis Timer abgelaufen sind – am deutlichsten sichtbar bei Delay-Schritten. Das Verhalten unterscheidet sich auch zwischen geplanten Schritten und Event-getriggerten Schritten. Zeitpläne, Beispiele und Analytics-Nuancen finden Sie unter [Exit-Kriterien]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria).

### Warum zeigt mein Aktionspfade-Schritt einen Fehler an, wenn ich eine Link-Alias-Interaktion auswähle? {#why-does-my-action-paths-step-show-an-error-when-i-select-a-link-alias-interaction}

Aktionsgruppen, die E-Mail-Interaktivitäts-Trigger verwenden (z. B. **Click alias in email** oder **Clicked alias in any campaign or Canvas step**), benötigen einen Nachrichtenschritt, der die Nachricht mit diesem Link bereits gesendet hat. Fügen Sie Schritte hinzu oder ordnen Sie sie neu an, sodass die E-Mail gesendet wird, bevor der Aktionspfade-Schritt den Klick auswertet, oder wählen Sie eine Interaktion, die zu einer Nachricht passt, die der/die Nutzer:in bereits in diesem Canvas erhalten hat. Die vollständige Liste der Interaktions-Trigger finden Sie unter [Aktionsbasierte Zustellung]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery).

### Wie wirken sich historische Zeitstempel angepasster Events auf aktionsbasierte Canvases und Campaigns aus? {#how-do-historical-custom-event-timestamps-affect-action-based-canvases-and-campaigns}

Braze wertet aktionsbasierte Journeys aus, wenn qualifizierende Events aufgenommen werden und der/die Nutzer:in Ihre Zielgruppenregeln erfüllt. Wenn ein Event auf dem Profil außerhalb des Zeitfensters eingeht, in dem Ihr Canvas oder Ihre Campaign aktiv war, oder bevor der/die Nutzer:in Ihrer Zielgruppe entsprach, erfolgen der Eintritt oder nachgelagerte Versendungen möglicherweise nicht wie erwartet. Vergleichen Sie Event-Zeitstempel mit den Go-Live-Zeiten und der Segmentzugehörigkeit mithilfe des Aktivitätsprotokolls im Nutzerprofil und den Schritten zur Fehlerbehebung unter [Fehlerbehebung bei angepassten Events]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#troubleshooting-custom-events). Wenn das Verhalten weiterhin nicht den Erwartungen entspricht, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/braze_support).