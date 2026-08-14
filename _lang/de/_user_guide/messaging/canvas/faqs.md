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

### Gibt es Größenbeschränkungen für Canvas-Entry-Eigenschaften? {#are-there-size-limits-for-canvas-entry-properties}

Ja. Das [Canvas-Kontextobjekt]({{site.baseurl}}/api/objects_filters/context_object) (Canvas-Entry-Eigenschaften) hat eine maximale Größe von 50&nbsp;KB. Halten Sie Payloads innerhalb dieses Limits so klein wie möglich. Informationen zur Funktionsweise von Entry- und Event-Eigenschaften in Canvas finden Sie unter [Kontext- und Event-Eigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties).

### Warum wird der Fehler „Too many Canvas branches“ angezeigt? {#why-do-i-see-a-too-many-canvas-branches-error}

Dieser Fehler tritt auf, wenn die Kombination aus Schritt-Verzweigungen und der Größe der Eintritts-Zielgruppe zu Cluster-Performance-Problemen führen kann, die den Nachrichtenversand verhindern. Lösungsschritte – einschließlich der Verwendung von [Zielgruppenpfaden]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths), der Reduzierung von Verzweigungen oder der Zielgruppengröße und dem Neuaufbau in Canvas Flow – finden Sie unter [Fehler „Too many Canvas branches“]({{site.baseurl}}/user_guide/messaging/canvas/troubleshooting#too-many-canvas-branches-error).

### Kann ich die intelligente Auswahl mit erneuter Berechtigung in einem Canvas verwenden? {#can-i-use-intelligent-selection-with-re-eligibility-in-a-canvas}

Ja. Canvases können die [intelligente Auswahl]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection) verwenden, wenn die erneute Berechtigung aktiviert ist, während Campaigns ein Fenster für die erneute Berechtigung von mindestens 24 Stunden erfordern, wenn die intelligente Auswahl aktiviert ist. Braze kann nicht garantieren, dass bei einem erneuten Eintritt dieselbe Variante zugewiesen wird, da sich die Zuordnung im Laufe der Zeit verschiebt.

### Was ist der Unterschied zwischen einer Komponente und einem Schritt? {#whats-the-difference-between-a-component-and-a-step}

Eine [Komponente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about) ist ein einzelner Bestandteil Ihres Canvas, mit dem Sie die Effektivität Ihres Canvas bestimmen können. Komponenten können Aktionen wie das Aufteilen der User Journey, das Hinzufügen einer Verzögerung und sogar das Testen mehrerer Canvas-Pfade umfassen. Ein Schritt in Canvas bezieht sich auf die personalisierte User Journey in Ihren Canvas-Branches. Im Wesentlichen besteht Ihr Canvas aus einzelnen Komponenten, die Schritte für Ihre User Journey bilden.

### Kann ich ein Canvas mit nicht verbundenen Schritten starten? {#can-i-launch-a-canvas-with-disconnected-steps}

Ja. Sie können Canvases nach dem Start auch mit nicht verbundenen Schritten speichern.

### Wohin gelangen Nutzer:innen, wenn sie einen nicht verbundenen Schritt erreicht haben? {#where-do-users-go-when-theyve-reached-a-disconnected-step}

Wenn sich ein:e Nutzer:in in einem nicht verbundenen Schritt Ihres Canvas-Workflows befindet, rückt er/sie zum nachfolgenden Schritt vor, sofern einer vorhanden ist, und die Einstellung des Schritts bestimmt, wie der/die Nutzer:in fortschreiten soll. Dies ist so konzipiert, dass Sie Änderungen an Schritten vornehmen können, ohne sie direkt mit dem Rest des Canvas verbinden zu müssen. Außerdem bietet es Ihnen Spielraum zum Testen, bevor Sie sofort live gehen – im Grunde ermöglicht es das Speichern eines Entwurfs.

Wir empfehlen, die Analytics-Ansicht auf wartende Nutzer:innen in einem Canvas-Schritt zu prüfen, bevor Sie einen Schritt trennen.

### Was passiert, wenn Zielgruppe und Sendezeit für ein Canvas mit einer Variante, aber mehreren Branches identisch sind? {#what-happens-if-the-audience-and-send-time-are-identical-for-a-canvas-that-has-one-variant-but-multiple-branches}

Wir reihen einen Job für jeden Schritt in die Warteschlange ein – sie laufen ungefähr zur gleichen Zeit, und einer von ihnen „gewinnt“. In der Praxis kann dies einigermaßen gleichmäßig verteilt sein, aber es gibt wahrscheinlich zumindest eine leichte Tendenz zugunsten des Schritts, der zuerst erstellt wurde.

Darüber hinaus können wir keine Garantien dafür geben, wie diese Verteilung genau aussehen wird. Wenn Sie eine gleichmäßige Aufteilung wünschen, fügen Sie einen Filter für [zufällige Bucket-Nummern]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) hinzu.

### Wie werden Canvas-Zielgruppen ausgewertet? {#how-are-canvas-audiences-evaluated}

Standardmäßig werden Filter und Segmente für vollständige Schritte im Canvas zum Sendezeitpunkt geprüft. Der Decision-Split-Schritt führt eine Auswertung direkt nach dem Empfang eines vorherigen Schritts durch (oder vor einer Verzögerung).

### Wann wird ein Ausnahme-Event ausgelöst? {#when-does-an-exception-event-trigger}

Ausnahme-Events werden nur ausgelöst, während der/die Nutzer:in darauf wartet, die Canvas-Komponente zu erhalten, der das Event zugeordnet ist. Wenn ein:e Nutzer:in eine Aktion im Voraus ausführt, wird das Ausnahme-Event nicht ausgelöst. Wenn Sie Nutzer:innen ausschließen möchten, die ein bestimmtes Event bereits ausgeführt haben, verwenden Sie stattdessen [Filter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).

### Wie wirkt sich die Bearbeitung eines Canvas auf Nutzer:innen aus, die sich bereits im Canvas befinden? {#how-does-editing-a-canvas-affect-users-already-in-the-canvas}

Wenn Sie einige Schritte eines mehrstufigen Canvas bearbeiten, erhalten Nutzer:innen, die bereits in der Zielgruppe waren, aber die Schritte noch nicht erhalten haben, die aktualisierte Version der Nachricht. Beachten Sie, dass dies nur geschieht, wenn sie noch nicht für den Schritt ausgewertet wurden.

Weitere Informationen darüber, was Sie nach dem Start bearbeiten können, finden Sie unter [Canvas nach dem Start ändern]({{site.baseurl}}/post-launch_edits).

### Was passiert, wenn Sie ein Canvas stoppen? {#what-happens-when-you-stop-a-canvas}

Wenn Sie ein Canvas stoppen, gilt Folgendes:

- Nutzer:innen werden daran gehindert, das Canvas zu betreten.
- Es werden keine weiteren Nachrichten gesendet, unabhängig davon, wo sich ein:e Nutzer:in im Flow befindet.
- **Ausnahme:** Canvases mit E-Mails werden nicht sofort gestoppt. Nachdem die Sendeanfragen an SendGrid übermittelt wurden, können wir nicht mehr verhindern, dass sie an den/die Nutzer:in zugestellt werden.

### Sollte ich ein einzelnes Canvas oder separate Canvases pro Nutzer-Lifecycle erstellen? {#should-i-build-one-canvas-or-separate-canvases-per-user-lifecycle}

Je nachdem, was Sie mit Ihrem Canvas erreichen möchten, benötigen Sie möglicherweise unterschiedliche Ansätze für den Aufbau Ihrer User Journey. Die Flexibilität von Canvas ermöglicht es Ihnen, User Journeys für jede Phase des Nutzer-Lifecycles abzubilden. Sehen Sie sich unsere [Braze-Canvas-Templates]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates) an, um verschiedene Beispiele für optimierte Ansätze zur Erstellung effektiver User Journeys zu finden.

## Nachrichten und Zustellung {#messages-and-delivery}

### Wann werden In-App-Nachrichten in Canvas gesendet? {#when-are-in-app-messages-in-canvas-sent}

In-App-Nachrichten werden beim nächsten Sitzungsstart gesendet. Das bedeutet: Wenn Nutzer:innen den Canvas-Schritt betreten, bevor der Canvas gestoppt wird, erhalten sie die In-App-Nachricht trotzdem beim nächsten Sitzungsstart – sofern die In-App-Nachricht noch nicht abgelaufen ist.

Es ist möglich, dass Nutzer:innen eine Sitzung starten, bevor der Canvas gestoppt wird, die In-App-Nachricht aber nicht sofort angezeigt wird. Das kann vorkommen, wenn die In-App-Nachricht durch ein angepasstes Event getriggert wird oder verzögert ist. In diesem Fall ist es möglich, dass Nutzer:innen eine In-App-Nachrichten-Impression protokollieren und die In-App-Nachricht „erhalten“, nachdem der Canvas gestoppt wurde. Die Sitzung müsste jedoch vor dem Stoppen des Canvas gestartet worden sein, aber **nachdem** sie den Canvas-Schritt erhalten haben.

{% alert note %}
Das Stoppen eines Canvas führt nicht dazu, dass Nutzer:innen, die auf den Empfang von Nachrichten warten, die User Journey verlassen. Wenn Sie den Canvas wieder aktivieren und Nutzer:innen noch auf die Nachricht warten, erhalten sie diese (es sei denn, der Zeitpunkt, zu dem die Nachricht hätte gesendet werden sollen, ist bereits verstrichen – dann erhalten sie die Nachricht nicht).
{% endalert %}

### Warum kann ein Canvas null Sends anzeigen, obwohl Impressionen protokolliert werden? {#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged}

Wenn _Gesendete Nachrichten_ für einen Canvas mit einem In-App-Nachrichten-Schritt immer null sind, liegt das daran, dass die Zustellung von In-App-Nachrichten anders funktioniert als bei anderen Messaging-Kanälen.

In-App-Nachrichten werden vom SDK „abgerufen“ und nicht von Braze „gepusht“. In-App-Nachrichten für berechtigte Nutzer:innen werden automatisch beim Sitzungsstart zugestellt und „warten“ auf das Trigger-Event, bevor sie angezeigt werden. Da berechtigte Nutzer:innen die Nachricht beim Start einer Sitzung erhalten, meldet Braze dies nicht als Send-Event. Wenn Nutzer:innen das Trigger-Event ausführen, wird die Nachricht angezeigt und Braze protokolliert eine Impression und markiert den Canvas-Schritt (oder die Campaign) als empfangen im Nutzerprofil. Folglich ist die Gesamtzahl der _Sends_ für In-App-Nachrichten null.

### Warum haben Nutzer:innen meine In-App-Nachricht nach einer langen Verzögerung oder Verzweigung nicht erhalten? {#why-didnt-users-receive-my-in-app-message-after-a-long-delay-or-branch}

Nachdem vorgelagerte [Verzögerungsschritte]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) und Zielgruppenprüfungen abgeschlossen sind, werden Nutzer:innen erst dann für eine In-App-Nachricht berechtigt, wenn sie den Nachrichtenschritt erreichen. Wenn die Nachricht an einem Kalenderdatum oder innerhalb eines kurzen Zeitfensters **nach Verfügbarkeit des Schritts** abläuft, können Nutzer:innen auf langsameren Pfaden nach dem Ablauf ankommen und die Nachricht nie sehen. Stimmen Sie den Ablauf auf Ihre längsten realistischen Pfadverzögerungen ab. Weitere Informationen und Beispiele finden Sie unter [Ablauf von In-App-Nachrichten]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas#in-app-message-expiration).

### Warum sehe ich „Canvas Entry Properties may not be used in In-App Messages.“? {#why-do-i-see-canvas-entry-properties-may-not-be-used-in-in-app-messages}

Diese Meldung erscheint, wenn die Personalisierung auf Felder verweist, die In-App-Nachrichten in Canvas nicht auflösen können. Verwenden Sie das `context`-Objekt wie unter [Kontext- und Event-Eigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) und [Nachrichtenschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) beschrieben. Der Legacy-Liquid-Namespace `canvas_entry_properties` hat andere Einschränkungen als `context`. Wenn Sie Werte über mehrere Schritte hinweg beibehalten müssen, prüfen Sie [persistente Eigenschaften im originalen Canvas-Editor]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties) mit Ihrem Braze-Team. Gespeicherte Werte werden gelöscht, wenn Nutzer:innen den Canvas verlassen, bevor das Gerät den In-App-Payload heruntergeladen hat.

### Wo finde ich Button-Klicks für Drag-and-Drop-In-App-Nachrichten in Canvas? {#where-can-i-find-button-clicks-for-drag-and-drop-in-app-messages-in-canvas}

Metriken auf Button-Ebene für Drag-and-Drop-In-App-Nachrichten erscheinen auf der Analytics-Karte des **Nachrichtenschritts** unter **Canvas-Details**, nicht nur in der übergeordneten Canvas-Zusammenfassung. Öffnen Sie den Canvas, wählen Sie den Nachrichtenschritt aus und überprüfen Sie dort das In-App-Engagement. Informationen zu Reporting-Konzepten finden Sie unter [Messen und Testen mit Canvas Analytics]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics).

### Kann ich für jede Variante im selben Canvas-Nachrichtenschritt oder multivariaten Versand unterschiedliche Sendezeiten planen? {#can-i-schedule-different-send-times-for-each-variant-in-the-same-canvas-message-step-or-multivariate-send}

Nein. Varianten in derselben multivariaten Konfiguration oder im selben Nachrichtenschritt teilen sich einen Zustellungszeitplan. Sie können nicht einer Variante den Versand um 18 Uhr und einer anderen um 19 Uhr für denselben geplanten Versand zuweisen.

Um Versendungen zu staffeln oder unterschiedliche Zeiten pro Pfad zu verwenden, probieren Sie die folgenden Methoden:

- Separate Nachrichtenschritte mit Verzögerungsschritten dazwischen, sodass jede Nachricht ihren eigenen Zeitplan hat.
- Verwenden Sie Verzweigungen oder einen [Experimentpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step)-Schritt, damit Nutzer:innen Pfaden mit unterschiedlichem Timing folgen.
- Separate Campaigns, wenn der Anwendungsfall nicht innerhalb eines Canvas bleiben muss.

Informationen zu multivariaten und A/B-Konzepten in Campaigns finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing).

### Was passiert, wenn Nutzer:innen bei einem Canvas-Nachrichtenschritt durch globales Frequency-Capping begrenzt werden? {#what-happens-if-a-user-is-global-frequency-capped-at-a-canvas-message-step}

Sie erhalten den Versand für den begrenzten Kanal nicht, aber Nachrichtenschritte bringen Nutzer:innen trotzdem voran, wenn eine Nachricht aufgrund von globalem Frequency-Capping nicht gesendet wird. Informationen zu den schrittweisen Fortschrittsfällen finden Sie unter [Wie Nutzer:innen voranschreiten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance). Globales Frequency-Capping allein führt nicht dazu, dass Nutzer:innen einen Canvas verlassen; dieses Verhalten ist unabhängig von den **Zustellungsvalidierungen** eines Nachrichtenschritts. Weitere Details finden Sie unter [Rate-Limiting und Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping).

### Warum sind die Sends niedriger als die geschätzte Zielgruppengröße? {#why-are-sends-lower-than-the-estimated-audience-size}

Sends können aus vielen der gleichen Gründe niedriger sein als die **geschätzte Zielgruppe** wie bei [Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/faq#why-are-sends-lower-than-the-estimated-audience-size), einschließlich Frequency-Caps, strikter Geräte- oder Browser-Filter, Wiedereintritts-Zeitfenster, Rate-Limiting und kanalbezogener Ausschlüsse (z. B. Push-Erreichbarkeit oder E-Mail-Abo- und Zustellbarkeitsprüfungen).

Canvas-spezifische Faktoren gelten ebenfalls:

- **Aktionsbasierter oder API-getriggerter Eintritt:** Nutzer:innen treten erst ein (und erhalten Schritte), nachdem sie das Eintrittsverhalten ausgeführt haben, sodass die tatsächlichen Sends hinter der Vorabschätzung zurückbleiben, bis diese Aktionen stattfinden.
- **Zielgruppenpfade:** Nutzer:innen werden zum Zweig mit der höchsten Priorität geleitet, für den sie sich qualifizieren, sodass nachgelagerte Zweige weniger Nutzer:innen erhalten können, als eine flache Segmentzählung vermuten lässt.
- **Zielgruppen- und Sendezeitprüfungen:** Vollständige Schritte werten Filter zum Sendezeitpunkt erneut aus, sofern Sie nichts anderes konfigurieren. Nutzer:innen, die sich bei der Erstellung des Canvas qualifiziert haben, können vor dem Versand einer Nachricht herausfallen.
- **Kontrollgruppen:** Globale oder Canvas-Kontrollgruppen halten einen Anteil der Eintretenden vom Messaging zurück.
- **Ruhezeiten und Verzögerungen:** Nachrichten können zurückgehalten oder neu geplant werden, wodurch Sends aus dem Berichtszeitraum verschoben werden, den Sie gerade betrachten.
- **Maximale Eintritts- oder Zielgruppenbegrenzungen:** Eintritts- oder Sendebegrenzungen stoppen zusätzliche Nutzer:innen, selbst wenn das zugrunde liegende Segment größer ist.
- **Berichtszeitraum:** Der Analytics-Bereich umfasst möglicherweise nicht jeden Send, den Sie mit der Schätzung vergleichen.

### Warum stimmen die geschätzte Zielgruppe und die Canvas-Nutzerzahlen nicht überein? {#why-dont-estimated-audience-and-canvas-user-counts-match}

Die **geschätzte Zielgruppe** spiegelt wider, wer zum Zeitpunkt der Schätzung Ihrem Segment und Ihren Eintrittsfiltern entspricht. Nach diesem Zeitpunkt können verzögerte oder aktionsbasierte Eintritte, Wiedereintritt, API-Trigger oder Verzweigungsrouting die Anzahl der Profile erhöhen, die die Journey berühren, im Vergleich zum Snapshot. Nutzer:innen können auch herausfallen, wenn Sendezeitfilter fehlschlagen, was die tatsächlichen Eintritte oder Sends senkt. Vergleichen Sie Timing, Begrenzungen und Auswertungseinstellungen zusammen mit [Warum sind die Sends niedriger als die geschätzte Zielgruppengröße?](#why-are-sends-lower-than-the-estimated-audience-size).

### Warum ist _Eindeutige Empfänger:innen_ höher als die Anzahl der Nutzer:innen, die ich angesprochen habe? {#why-is-_unique-recipients_-higher-than-the-number-of-users-i-targeted}

_Eindeutige Empfänger:innen_ kann höher sein als die erwartete Zielgruppe, da Braze **eindeutige tägliche Empfänger:innen** für Canvas- und Campaign-Reporting erfasst. Dies unterstützt eine genaue Konversions-Attribution jedes Mal, wenn Nutzer:innen eine Nachricht in der Journey erhalten.

Wenn Nutzer:innen beispielsweise am Montag und erneut am Freitag einen Canvas-Schritt erhalten und nach jedem Versand konvertieren, kann Braze zwei Empfängerzeilen und zwei zugehörige Konversionen zählen. Bei wiederkehrenden Eintritten oder Wiedereintritt kann dieselbe kleine Gruppe von Profilen über mehrere Tage hinweg mehrere _Eindeutige Empfänger:innen_ erzeugen.

### Warum hat mein Canvas niedrigere Sendraten? {#why-is-my-canvas-experiencing-lower-send-rates}

Wenn Sie feststellen, dass Ihr täglich geplanter Canvas im Laufe der Zeit an weniger Nutzer:innen sendet, prüfen Sie Folgendes:

- **Prüfen Sie, ob Wiedereintritt aktiviert ist:** Ohne Wiedereintritt lässt Braze jede:n Nutzer:in nur einmal in den Canvas eintreten. Bei täglich geplanten Canvases sind nur Nutzer:innen berechtigt, die der Zielgruppe entsprechen und den Canvas noch nicht betreten haben. Je mehr Nutzer:innen eintreten, desto weniger berechtigte Nutzer:innen gibt es bei jedem späteren Eintritt, sodass das Eintrittsvolumen sinkt.
- **Prüfen Sie, ob die Zielgruppe eine feste Mitgliedschaft hat:** Zielgruppen, die aus einer festen Nutzerliste erstellt wurden (z. B. ein [CSV-Import]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import), der als Segmentfilter verwendet wird), gewinnen nicht automatisch neue Mitglieder. Ohne neue Eintretende kann das Eintrittsvolumen nicht wieder ansteigen, wenn Nutzer:innen den Canvas betreten.

Informationen zu [Rate-Limits für die Zustellgeschwindigkeit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) und anderen Faktoren, die Sends für ein einzelnes Vorkommen senken, finden Sie unter [Warum sind die Sends niedriger als die geschätzte Zielgruppengröße?](#why-are-sends-lower-than-the-estimated-audience-size).

### Warum zeigt ein kleines Kontrollgruppen-Segment Änderungen in der historischen Mitgliedschaft? {#why-does-a-small-control-group-segment-show-changes-in-historical-membership}

Historische Mitgliedschafts-Charts verwenden geschätzte Stichproben, sodass kleine Segmente – einschließlich [globaler Kontrollgruppen]({{site.baseurl}}/user_guide/audience/global_control_group)-Segmente – tägliche Schwankungen zeigen können, selbst wenn die zugrunde liegende Zielgruppe stabil ist. Informationen zur Funktionsweise von Schätzungen und warum Charts schwanken können, finden Sie unter [Historische Segmentmitgliedschaftsgröße anzeigen]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#viewing-historical-segment-membership-size).

## Analytics und Konversionen {#analytics-and-conversions}

### Wie ordnet das Konversions-Dashboard Canvas-Konversionen zu? {#how-does-the-conversions-dashboard-attribute-canvas-conversions}

Das [Konversions-Dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/conversions) ordnet Canvas-Konversionen basierend auf der von Ihnen gewählten [Attributionsmethode]({{site.baseurl}}/user_guide/analytics/dashboards/conversions#attribution-methods) zu (zum Beispiel **Upon Receipt**, **Upon Send**, **Upon Open** oder **Upon Click**). Damit Nutzer:innen im Bericht erscheinen, müssen sie den Canvas oder die Campaign betreten, die ausgewählte Attributionsmethode auslösen und das Konversions-Event innerhalb Ihrer Berichtseinstellungen durchführen.

Informationen zu Konversionsregeln auf Schritt- und Variantenebene in Canvas Analytics finden Sie unter [Wie werden Nutzerkonversionen in einem Canvas getrackt?](#how-are-user-conversions-tracked-in-a-canvas).

### Wie werden Nutzerkonversionen in einem Canvas getrackt? {#how-are-user-conversions-tracked-in-a-canvas}

Nutzer:innen können pro Canvas-Entry nur einmal konvertieren. Konversionen werden der zuletzt empfangenen Nachricht für diesen Entry zugeordnet. Der Zusammenfassungsblock am Anfang eines Canvas zeigt alle Konversionen, die von Nutzer:innen innerhalb dieses Pfads durchgeführt wurden, unabhängig davon, ob sie eine Nachricht erhalten haben. Jeder nachfolgende Schritt zeigt nur Konversionen an, die stattfanden, während dieser Schritt der zuletzt empfangene war.

{% alert note %}
Wenn Nutzer:innen erneut in einen Canvas eintreten, werden Konversions-Events nur für den letzten Entry getrackt. Konversions-Events werden nicht für vorherige Entries protokolliert, selbst wenn das Konversions-Event nachträglich ergänzt wird.
{% endalert %}

{% details Für Beispiele aufklappen %}

**Beispiel 1**

Es gibt einen Canvas-Pfad mit 10 Push-Benachrichtigungen und das Konversions-Event ist „Sitzungsstart“ („App öffnen“):

- Nutzer:in A öffnet die App nach dem Eintritt, aber vor dem Empfang der ersten Nachricht.
- Nutzer:in B öffnet die App nach jeder Push-Benachrichtigung.

**Ergebnis:** Die Zusammenfassung zeigt zwei Konversionen, während die einzelnen Schritte eine Konversion beim ersten Schritt und null bei allen nachfolgenden Schritten anzeigen.

{% alert note %}
Wenn Ruhezeiten aktiv sind, wenn das Konversions-Event stattfindet, gelten dieselben Regeln.
{% endalert %}

**Beispiel 2**

Es gibt einen Canvas mit einem Schritt und aktivierten Ruhezeiten:

1. Nutzer:in tritt in den Canvas ein.
2. Der erste Schritt hat keine Verzögerung, liegt aber innerhalb der festgelegten Ruhezeiten, sodass die Nachricht unterdrückt wird.
3. Nutzer:in führt das Konversions-Event durch.

**Ergebnis:** Die/der Nutzer:in wird in der gesamten Canvas-Variante als konvertiert gezählt, aber nicht im Schritt, da sie/er den Schritt nicht erhalten hat.

{% enddetails %}

### Was ist der Unterschied zwischen den verschiedenen Konversionsratentypen? {#whats-the-difference-between-the-different-conversion-rate-types}

- Die Gesamtkonversionen eines Canvas zeigen, wie viele eindeutige Nutzer:innen ein Konversions-Event abgeschlossen haben, nicht wie viele Konversionen jede:r einzelne durchgeführt hat.
- Die Variantenkonversionsrate oder der Zusammenfassungsblock am Anfang eines Canvas zeigt alle Konversionen, die von Nutzer:innen innerhalb dieses Pfads durchgeführt wurden, unabhängig davon, ob sie eine Nachricht erhalten haben, als Gesamtsumme.
- Die Schrittkonversionsrate zeigt, wie viele Personen diesen Nachrichtenschritt erhalten und eines der definierten Konversions-Events abgeschlossen haben.

### Warum entspricht meine Canvas-Schrittkonversionsrate nicht meiner Canvas-Variantengesamtkonversionsrate? {#why-is-my-canvas-step-conversion-rate-not-equal-to-my-canvas-variant-total-conversion-rate}

Es ist üblich, dass die Konversionssumme einer Canvas-Variante größer ist als die Summe ihrer Schrittsummen. Dies geschieht, weil Nutzer:innen ein Konversions-Event für eine Variante durchführen können, sobald sie die Variante betreten. Dasselbe Konversions-Event zählt jedoch nicht für einen Canvas-Schritt. Nutzer:innen, die den Canvas betreten und das Konversions-Event vor dem Empfang des ersten Canvas-Schritts durchführen, werden also zur Variantenkonversionssumme gezählt, aber nicht zur Schrittsumme. Dasselbe gilt für Nutzer:innen, die den Canvas betreten, aber vor dem Empfang eines Schritts wieder verlassen.

Beachten Sie, dass es auch möglich ist, dass Nutzer:innen eine Variante betreten, keine Nachricht von einem Schritt erhalten und dann konvertieren. In diesem Fall wird keine Konversion auf Schrittebene protokolliert. Da die/der Nutzer:in jedoch technisch gesehen konvertiert hat, wird eine Konversion auf Canvas-Ebene protokolliert.

### Wie kann ich bestätigen, ob meine Nutzer:innen einen API-getriggerten Canvas erhalten haben? {#how-can-i-confirm-if-my-users-received-an-api-triggered-canvas}

Sie können [ein Segment erstellen]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment), indem Sie einen Canvas-Filter verwenden, um zu bestätigen, ob Nutzer:innen den Canvas betreten oder einen bestimmten Canvas-Schritt erhalten haben. Verwenden Sie beispielsweise einen Canvas-Entry-Filter, wenn Sie bestätigen möchten, dass Nutzer:innen den API-getriggerten Canvas betreten haben, oder einen Filter für empfangene Schritte, wenn Sie bestätigen möchten, dass sie eine Nachricht vom Canvas erhalten haben. Verwenden Sie dann den [`/users/export/segment`-Endpunkt]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment), um die Nutzer:innen in diesem Segment zu exportieren.

### Kann ich einen Canvas löschen? {#can-i-delete-a-canvas}

Nein, aber Sie können [einen Canvas archivieren]({{site.baseurl}}/user_guide/messaging/governance/archiving).

### Wie setze ich einen archivierten Canvas oder eine archivierte Campaign fort? {#how-do-i-resume-an-archived-canvas-or-campaign}

Archivierte Nachrichten werden nicht gesendet, bis Sie sie in einen bearbeitbaren Zustand zurückversetzen. [Dearchivieren]({{site.baseurl}}/user_guide/messaging/governance/archiving#unarchiving) Sie die Campaign oder den Canvas, legen Sie den Entry-Zeitplan oder die Sendezeit auf ein zukünftiges Fenster fest (oder duplizieren Sie die Journey, wenn Sie eine saubere Kopie benötigen), und wählen Sie dann **Fortsetzen** oder starten Sie nach Bedarf. Siehe [Campaigns und Canvases archivieren]({{site.baseurl}}/user_guide/messaging/governance/archiving).

### Warum wird mein Canvas nicht gespeichert, obwohl kein Fehler angezeigt wird? {#why-doesnt-my-canvas-save-when-no-error-appears}

Leere **Custom attribute**-Filter in Zielgruppen- oder Schrittfiltern können das Speichern ohne detaillierte Validierungsmeldung blockieren. Öffnen Sie jede Filterkarte, entfernen Sie unvollständige Regeln für angepasste Attribute, oder geben Sie sowohl den Attributnamen als auch den Wert ein, und wählen Sie dann erneut **Speichern**.

### Warum ist ein Tag von meinem Canvas oder meiner Campaign verschwunden? {#why-did-a-tag-disappear-from-my-canvas-or-campaign}

Wenn ein [Tag]({{site.baseurl}}/user_guide/messaging/governance/tags) aus Ihrem Workspace gelöscht wird, entfernt Braze es aus jeder Campaign und jedem Canvas, die darauf verwiesen haben. Diese Bereinigung erzeugt nicht immer einen eigenen Eintrag im Canvas-Änderungsprotokoll.

### Wie kann ich Analytics für jede meiner Canvas-Komponenten anzeigen? {#how-can-i-view-analytics-for-each-of-my-canvas-components}

Um die Analytics einer Canvas-Komponente anzuzeigen, navigieren Sie zu Ihrem Canvas und scrollen Sie auf der Seite **Canvas-Details** nach unten. Hier können Sie die Analytics jeder Komponente einsehen. Weitere Informationen finden Sie unter [Canvas Analytics]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics).

### Wann ist das Engagement eines Canvas-Schritts im Nutzerprofil sichtbar? {#when-is-engagement-from-a-canvas-step-visible-on-a-user-profile}

Filter wie `Received Message from Canvas Step` werden aktualisiert, nachdem Braze das entsprechende Sende-, Empfangs- oder Engagement-Event für diesen Schritt protokolliert hat. In-App-Nachrichten können Impressionen getrennt von sendebasierten Metriken protokollieren. Siehe [Warum kann ein Canvas null Sends anzeigen, obwohl Impressionen protokolliert werden?](#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged). Dieselben Events erscheinen in den Schrittmetriken unter **Canvas-Details**.

### Ist Canvas Analytics oder der Segmentierer genauer, wenn es um die Anzahl eindeutiger Nutzer:innen geht? {#when-looking-at-the-number-of-unique-users-is-canvas-analytics-or-the-segmenter-more-accurate}

Der Segmentierer liefert eine genauere Statistik für eindeutige Nutzerdaten als Canvas- oder Campaign-Statistiken. Das liegt daran, dass Canvas- und Campaign-Statistiken Zahlen sind, die Braze inkrementiert, wenn etwas passiert – was bedeutet, dass es Variablen gibt, die dazu führen können, dass diese Zahl von der des Segmentierers abweicht. Beispielsweise können Nutzer:innen für einen Canvas oder eine Campaign mehr als einmal konvertieren.

### Warum weicht die Anzahl der Nutzer:innen, die einen Canvas betreten, von der erwarteten Anzahl ab? {#why-does-the-number-of-users-entering-a-canvas-not-match-the-expected-number}

Die Anzahl der Nutzer:innen, die einen Canvas betreten, kann von Ihrer erwarteten Anzahl abweichen, da Zielgruppen und Trigger unterschiedlich ausgewertet werden. In Braze wird eine Zielgruppe vor dem Trigger ausgewertet (es sei denn, Sie verwenden einen [Attributänderungs]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)-Trigger). Dies führt dazu, dass Nutzer:innen aus dem Canvas herausfallen, wenn sie nicht Teil Ihrer ausgewählten Zielgruppe sind, bevor Trigger-Aktionen ausgewertet werden.

### Was passiert mit anonymen Nutzer:innen während ihrer Canvas-Journey? {#what-happens-to-anonymous-users-during-their-canvas-journey}

Obwohl anonyme Nutzer:innen Canvases betreten und verlassen können, werden ihre Aktionen keinem bestimmten Nutzerprofil zugeordnet, bis sie identifiziert werden, sodass ihre Interaktionen möglicherweise nicht vollständig in Ihren Analytics getrackt werden. Sie können den [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder) verwenden, um einen Bericht über diese Metriken zu erstellen.

{% alert tip %}
Für weitere Unterstützung bei der Canvas-Fehlerbehebung wenden Sie sich bitte innerhalb von 30 Tagen nach Auftreten Ihres Problems an den Braze-Support, da uns nur die Diagnoseprotokolle der letzten 30 Tage zur Verfügung stehen.
{% endalert %}

### Kann ich Nutzer:innen, die sich derzeit in einer Canvas-Journey befinden, von einer Campaign oder einem Segment ausschließen? {#can-i-exclude-users-who-are-currently-in-a-canvas-journey-from-a-campaign-or-segment}

Verwenden Sie [Segmentierungsfilter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) wie `Entered Canvas Variation`, `In Canvas Control Group` oder `Received Message from Canvas Step`, um Nutzer:innen basierend auf Canvas-Entry, Variantenzuordnung oder Schritt-Engagement anzusprechen. Diese Filter werten den Entry-Verlauf und Interaktionen aus – sie geben nicht an, ob Nutzer:innen noch aktiv eine Journey durchlaufen.

Um Nutzer:innen basierend auf aktiver Canvas-Teilnahme ein- oder auszuschließen, fügen Sie [User Update]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)-Schritte beim Canvas-Entry und -Exit hinzu, um angepasste Attribute zu setzen und zu löschen, und filtern Sie dann in Campaigns oder Segments nach diesen Attributen.

## Segmentierung {#segmentation}

### Was ist der Unterschied zwischen „Hat keine Canvas-Variante betreten“ und „Ist nicht in der Canvas-Kontrollgruppe“? {#what-is-the-difference-between-has-not-entered-canvas-variation-and-is-not-in-canvas-control-group}

Die vollständigen Filterdefinitionen finden Sie unter [Segmentierungsfilter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).

#### Hat keine Canvas-Variante betreten {#has-not-entered-canvas-variation}

Der/die Nutzer:in hat nie einen Varianten-Pfad eines bestimmten Canvas betreten. Alle Nutzer:innen, die sich nicht in der Kontrollgruppe befinden, sind eingeschlossen – unabhängig davon, ob sie das Canvas betreten haben. Dazu gehören Nutzer:innen, die eine andere Variante betreten haben, und Nutzer:innen, die keine Variante betreten haben.

#### Ist nicht in der Canvas-Kontrollgruppe {#is-not-in-canvas-control-group}

Der/die Nutzer:in hat das Canvas betreten, befindet sich aber nicht in der Kontrollgruppe und hat folglich eine Variante erhalten. Dies umfasst nur Nutzer:innen, die das Canvas betreten haben.

Beachten Sie, dass die Variantenzuweisung beim Canvas-Entry erfolgt. Wenn ein:e Nutzer:in ein Canvas nicht betreten hat, wird ihm/ihr keine Variante zugewiesen. Mit anderen Worten: Er/sie befindet sich weder in der Kontrollgruppe noch in einer Variante.

## Originaler Canvas-Editor {#original-canvas-editor}

{% details Für FAQ zum originalen Canvas-Editor aufklappen %}

### Wie konvertiere ich ein bestehendes Canvas vom originalen Editor zum aktuellen Editor? {#how-do-i-convert-an-existing-canvas-from-the-original-editor-to-the-current-editor}

Sie können [Ihr Canvas klonen]({{site.baseurl}}/cloning_canvases). Dadurch wird eine Kopie Ihres originalen Canvas im aktuellsten Canvas-Workflow erstellt.

### Was sind die Hauptunterschiede zwischen dem aktuellen und dem originalen Canvas-Editor? {#what-are-the-main-differences-between-the-current-and-original-canvas-editors}

#### Canvas-Komponenten-Toolbar {#canvas-component-toolbar}

Zuvor wurde im originalen Canvas-Editor standardmäßig ein vollständiger Schritt hinzugefügt, wenn Sie einen Schritt in Ihrer User Journey erstellt haben. Diese vollständigen Schritte werden durch verschiedene Canvas-Komponenten ersetzt, was Ihnen den Vorteil einer besseren Übersichtlichkeit und Anpassbarkeit für Ihre Bearbeitungserfahrung bietet. Sie können alle Ihre Canvas-Komponenten sofort über die Canvas-Schritt-Toolbar sehen.

#### Schrittverhalten {#step-behavior}

Zuvor enthielt jeder vollständige Schritt Informationen wie Verzögerungs- und Zeitplaneinstellungen, Ausnahme-Events, Zielgruppenfilter, Nachrichtenkonfiguration und Optionen zum Nachrichtenfortschritt – alles in einer Komponente. Diese sind im aktuellen Editor separate Einstellungen, um Ihre Canvas-Erstellung anpassbarer zu gestalten, und führen zu einigen Unterschieden in der Funktionalität.

#### Fortschritt der Nachrichtenkomponente {#message-component-advancement}

[Nachrichtenkomponenten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) bringen alle Nutzer:innen weiter, die den Schritt betreten. Es ist nicht erforderlich, das Fortschrittsverhalten für Nachrichten festzulegen, was die Konfiguration des gesamten Schritts vereinfacht. Wenn Sie die Option **Bei gesendeter Nachricht fortfahren** implementieren möchten, fügen Sie einen separaten Zielgruppenpfad hinzu, um Nutzer:innen herauszufiltern, die den vorherigen Schritt nicht erhalten haben.

#### Verzögerungsverhalten „in“ {#delay-in-behavior}

[Verzögerungskomponenten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) warten die gesamte Verzögerungszeit ab, bevor sie zum nächsten Schritt übergehen.

Nehmen wir an, am 12. April haben wir eine Verzögerungskomponente, bei der die Verzögerung so eingestellt ist, dass Nutzer:innen am nächsten Tag um 14 Uhr zum nächsten Schritt weitergeleitet werden. Ein:e Nutzer:in betritt die Komponente am 13. April um 14:01 Uhr.
- Im originalen Workflow würde der/die Nutzer:in am 14. April um 14 Uhr zum nächsten Schritt übergehen, was weniger als ein Tag ab dem Eintrittszeitpunkt ist.
- Im aktuellen Editor würde der/die Nutzer:in am 15. April um 14 Uhr zum nächsten Schritt übergehen. Beachten Sie, dass dies die gleiche Uhrzeit ist, aber mehr als ein Tag ab dem Eintrittszeitpunkt.

#### Verhalten von intelligentem Timing {#intelligent-timing-behavior}

Da [intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) in der Nachrichtenkomponente gespeichert ist, werden Verzögerungen vor den Berechnungen des intelligenten Timings angewendet. Das bedeutet, dass Nutzer:innen je nach Eintrittszeitpunkt in die Komponente die Nachricht möglicherweise später erhalten als in einem Canvas, das mit dem originalen Canvas-Workflow erstellt wurde.

Nehmen wir an, Ihre Verzögerung ist auf 2 Tage eingestellt, intelligentes Timing ist aktiviert und hat ermittelt, dass die beste Sendezeit für Ihre Nachricht 14 Uhr ist. Ein:e Nutzer:in betritt den Verzögerungsschritt um 14:01 Uhr.
- **Aktueller Workflow:** Es dauert 48 Stunden, bis die Verzögerung abgelaufen ist, sodass der/die Nutzer:in die Nachricht am dritten Tag um 14 Uhr erhält.
- **Originaler Workflow:** Der/die Nutzer:in erhält die Nachricht am zweiten Tag um 14 Uhr.

Beachten Sie: Wenn intelligentes Timing aktiviert ist, wird die Nachricht innerhalb von 24 Stunden nach dem Eintritt des/der Nutzer:in in die Nachrichtenkomponente zur ermittelten intelligenten Zeit gesendet (auch wenn keine Verzögerungskomponente beteiligt ist).

#### Ausnahme-Events {#exception-events}

##### Ruhezeiten {#quiet-hours}

Ausnahme-Events werden mithilfe von Aktionspfaden angewendet, die von Nachrichtenschritten getrennt sind. Ruhezeiten werden in der Nachrichtenkomponente durchgesetzt. Das bedeutet: Wenn ein:e Nutzer:in den Aktionspfad bereits passiert hat (und nicht durch das Ausnahme-Event ausgeschlossen wurde), dann auf Ruhezeiten trifft, wenn er/sie die Nachrichtenkomponente erreicht, und das Canvas so konfiguriert ist, dass die Nachricht nach der Ruhezeitenperiode erneut gesendet wird, wird das Ausnahme-Event nicht mehr angewendet. Beachten Sie, dass dieser Anwendungsfall nicht häufig vorkommt.

Für Segmente und Filter verfügt der Nachrichtenschritt über Zustellungsvalidierungen, die es Nutzer:innen ermöglichen, zusätzliche Segmente und Filter zu konfigurieren, die zum Sendezeitpunkt validiert werden. Dies verhindert den oben genannten Ruhezeiten-Grenzfall.

##### Zeitplaneinstellung „in“ oder „am nächsten“ {#in-or-on-the-next-schedule-setting}

Ausnahme-Events werden mithilfe von Aktionspfaden erstellt. Aktionspfade unterstützen nur „nach einem X-Zeitfenster“ und nicht „in X Zeit“ oder „am nächsten X Zeitpunkt“.

{% enddetails %}

### Was sollte ich angeben, wenn ich ein Support-Ticket für einen „Request Timed Out“-Fehler einreiche? {#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error}

Wenn Sie beim Bearbeiten eines Canvas auf einen „Request Timed Out“-Fehler stoßen und den [Braze-Support]({{site.baseurl}}/braze_support) kontaktieren müssen, geben Sie die folgenden Informationen an, um die Lösung zu beschleunigen:

{% multi_lang_include messaging/support_ticket_request_timed_out_details.md context='canvas' %}

## Canvas-Zustellung und Fehlerbehebung {#canvas-delivery-and-troubleshooting}

### Sind verwaiste Nutzer:innen berechtigt, Canvas-Nachrichten zu erhalten? {#are-orphaned-users-eligible-to-receive-canvas-messages}

Nein. [Verwaiste Nutzer:innen]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#what-happens-when-you-identify-anonymous-users) sind nicht berechtigt, Nachrichten zu erhalten. Wenn ein Profil verwaist, während sich ein:e Nutzer:in in einem Canvas-Journey befindet, verlässt er/sie den Flow stillschweigend. In den Analytics wird möglicherweise nicht immer ein **Exited**-Event für diesen Exit angezeigt, und die Workflow-Zusammenfassung kann ein `partial_update_token` ohne `exited_date` oder `exit_reason` enthalten.

Weitere Informationen zu Zusammenführungen und verwaisten Profilen finden Sie unter [Doppelte Nutzer:innen zusammenführen]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users).

### Werden bereits an den ESP gesendete Nachrichten noch zugestellt, wenn ich ein aktives Canvas oder eine Campaign stoppe? {#if-i-stop-an-active-canvas-or-campaign-do-messages-already-sent-to-the-esp-still-deliver}

Ja. Nachdem Braze eine Anfrage an Ihren E-Mail-Anbieter (ESP) gesendet hat, kann Braze diesen Versand nicht mehr zurückrufen. Das Stoppen eines Canvas oder einer Campaign verhindert neue Versandanfragen, aber bereits an den ESP übergebene Nachrichten können weiterhin zugestellt werden und die Versandzähler erhöhen, während der ESP sie verarbeitet.

Dies entspricht dem Verhalten, das unter [Was passiert, wenn Sie ein Canvas stoppen](#what-happens-when-you-stop-a-canvas) beschrieben wird: E-Mail-Versendungen, die sich bereits im Versand befinden, werden nicht sofort angehalten.

### Wie kann ich bestätigen, dass ein Canvas-Webhook-Schritt ohne nutzersichtbaren Inhalt ausgelöst wurde? {#how-can-i-confirm-a-canvas-webhook-step-fired-without-user-visible-content}

Braze erfasst Webhook-**Sends** und zugehörige Zustellungsergebnisse für [Webhook]({{site.baseurl}}/user_guide/channels/webhooks)-Schritte in Campaigns und Canvases. Verwenden Sie die Schritt-Analytics, das [Webhook-Reporting]({{site.baseurl}}/user_guide/channels/webhooks/reporting) oder [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)-Webhook-Events, um zu bestätigen, dass der Schritt ausgeführt wurde. Die Anfrage-Logs Ihres Endpunkts bieten zusätzliche Bestätigung, wenn Sie einen serverseitigen Empfangsnachweis benötigen.

Braze enthält kein integriertes unsichtbares Tracking-Pixel für Webhook-Schritte. Verlassen Sie sich auf die Braze-Webhook-Metriken und Ihre Endpunkt-Protokollierung anstelle von benutzerdefinierten Ein-Pixel-Bildanfragen.

### Warum hat mein Webhook-Schritt kein Body-Feld? {#why-does-my-webhook-step-have-no-body-field}

Webhook-Schritte verwenden einen Request-Body für `POST`, `PUT`, `PATCH` und `DELETE`. Wenn Sie die Methode auf `GET` umstellen, entfernt Braze das Body-Feld, da GET-Anfragen keinen Request-Body unterstützen. Wechseln Sie zurück zu einer Methode mit Body-Unterstützung, wenn Sie JSON- oder Formulardaten senden müssen. Weitere Informationen zu Methoden finden Sie unter [Einen Webhook erstellen]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#http-method).

### Wie verwende ich spacer.gif in einem Webhook-Schritt? {#how-do-i-use-spacergif-in-a-webhook-step}

Braze hostet ein `spacer.gif`-Platzhalterbild auf `cdn.braze.com` und `braze-images.com`. Einige Teams verweisen mit einer Webhook-URL auf dieses Bild, wenn ein Schritt ausgelöst werden muss, ohne einen externen Endpunkt aufzurufen. Standard-Webhook-Schritte sollten einen echten Endpunkt aufrufen. Verwenden Sie das [Webhook-Reporting]({{site.baseurl}}/user_guide/channels/webhooks/reporting) und Ihre Endpunkt-Logs, um die Zustellung zu bestätigen, wie unter [Wie kann ich bestätigen, dass ein Canvas-Webhook-Schritt ohne nutzersichtbaren Inhalt ausgelöst wurde?](#how-can-i-confirm-a-canvas-webhook-step-fired-without-user-visible-content) beschrieben.

### Warum lädt mein Canvas nicht und zeigt einen „invalid next-step-id“-Fehler? {#why-wont-my-canvas-load-with-an-invalid-next-step-id-error}

Dieser Konsolenfehler bedeutet, dass mindestens ein Schritt auf einen fehlenden oder ungültigen nächsten Schritt verweist – zum Beispiel nach einem teilweisen Löschen, Klonen oder Import. Öffnen Sie das Canvas im Editor, verbinden Sie verwaiste Schritte erneut oder entfernen Sie Schritte, die keinen gültigen nachgelagerten Pfad mehr haben. Wenn das Canvas immer noch nicht lädt, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/braze_support) mit der Canvas-ID und einem Screenshot des Konsolenfehlers.

### Warum unterscheidet sich ein Canvas-Konversions-Zeitstempel in Currents von meinen Canvas-Analytics? {#why-does-a-canvas-conversion-timestamp-in-currents-differ-from-my-canvas-analytics}

Currents protokolliert Canvas-Konversionen als [`users.canvas.Conversion`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#canvas-conversion-events)-Events. Die Event-`time` gibt an, wann das Konversions-Event aufgetreten ist. Das Feld `conversion_behavior` dieses Events beschreibt die Konversionsdefinition (Typ und Zeitfenster). Canvas-Analytics können Konversionen auch relativ zum Canvas-Eintritt innerhalb des Konversionsfensters zusammenfassen. Vergleichen Sie beim Abgleich von Exporten die Currents-`time` mit dem Zeitstempel des Konversions-Events und Ihren Canvas-Konversionsfenster-Einstellungen.

### Warum ist `canvas_step_name` in Currents null? {#why-is-canvas_step_name-null-in-currents}

Campaign- und Canvas-Namensfelder wie `canvas_step_name` können `null` sein, wenn ein Currents-Event gesendet wird, bevor Braze die Schritt-Metadaten vollständig propagiert hat – zum Beispiel nachdem Sie einen Schritt erstellt oder umbenannt haben. Weitere Informationen finden Sie unter [Warum ist der Campaign-Name oder Canvas-Schrittname `NULL` in meinen Currents-Daten?]({{site.baseurl}}/user_guide/data/distribution/braze_currents/faq#why-is-the-campaign-name-or-canvas-step-name-null-in-my-currents-data).

### Warum wird mein Array in einem User-Update-Schritt nicht aktualisiert? {#why-isnt-my-array-updating-in-a-user-update-step}

Überprüfen Sie das JSON in Ihrem [User-Update]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)-Schritt. Array- und verschachtelte Attribut-Updates benötigen gültige Pfade und Werte für das Attribut, das Sie ändern. Fügen Sie keine Felder ein, die der Schritt automatisch bereitstellt, wie z. B. die externe Nutzer-ID. Verwenden Sie den Tab **Preview and test** des Schritts, um die Payload vor dem Start zu bestätigen.

### Kann ich Canvas-Nachrichten an Nutzer:innen ohne `external_id` senden? {#can-i-send-canvas-messages-to-users-without-an-external_id}

Ja, wenn bereits ein Braze-Nutzerprofil existiert. Nutzer:innen ohne `external_id` sind [anonyme Nutzer:innen]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#anonymous-user-profiles) und können mit einer `braze_id` oder einem [Nutzer-Alias]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases) referenziert werden. Erstellen oder aktualisieren Sie das Profil mit dem [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) oder Ihrem SDK vor dem Canvas-Eintritt und verwenden Sie dann [aktionsbasierten oder API-getriggerten Eintritt]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule). Standard-Canvas-Targeting erfordert weiterhin ein Braze-Nutzerprofil – Sie können keine Canvas-Nachrichten nur an eine E-Mail-Adresse ohne Profil senden.

### Warum ist ein:e Nutzer:in seltener in ein Canvas eingetreten, als er/sie das Trigger-Event ausgeführt hat? {#why-did-a-user-enter-a-canvas-fewer-times-than-they-performed-the-trigger-event}

Bei aktionsbasierten und API-getriggerten Canvases dedupliziert Braze Trigger-Events, sodass ein:e Nutzer:in für dasselbe Canvas höchstens etwa **einmal pro Sekunde** eintreten kann. Wenn ein:e Nutzer:in dasselbe Trigger-Event mehrmals innerhalb einer Sekunde ausführt, wird nur ein Eintritt verarbeitet.

Um mehrere Eintritte in derselben Sekunde zu ermöglichen, planen Sie Trigger-Events mit mindestens 1,1 Sekunden Abstand (zum Beispiel, wenn Sie das Event-Timing von Ihrem Server aus steuern). Für Campaign-ähnliches Verhalten, das mehrere gleichzeitige Trigger erlaubt, vergleichen Sie Ihren Anwendungsfall mit [Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns) mit entsprechenden Zeitplan- und Wiederzulassungs-Einstellungen.

### Wann werden Nutzer:innen in API-getriggerten Canvases dedupliziert? {#when-are-users-de-duplicated-in-api-triggered-canvases}

Wenn ein:e Nutzer:in erneut in ein API-getriggertes Canvas eintritt und einen Delay-Schritt erreicht, in dem er/sie bereits aus einem vorherigen Eintritt für eine identische Nachricht in der Warteschlange steht, dedupliziert Braze den/die Nutzer:in, um doppelte Versendungen zu verhindern. Die zweite Canvas-Instanz wird beendet, sodass die Anzahl der Eintritte die Anzahl der Versendungen übersteigen kann.

### Warum geht ein Test-Push an die falsche App, aber Live-Versendungen sehen korrekt aus? {#why-does-a-test-push-go-to-the-wrong-app-but-live-sends-look-correct}

**Test-Push** auf einem Nutzerprofil wird an jedes Push-fähige Gerät für dieses Profil zugestellt. Wenn mehrere Apps auf einem Gerät installiert sind, stellt das Betriebssystem die Testbenachrichtigung in der Regel an die erste verfügbare App zu, die möglicherweise nicht die App ist, die Sie validieren möchten.

Um App-spezifisches Targeting zu bestätigen, senden Sie eine Live- oder Testnachricht über eine Campaign oder ein Canvas mit einer engen Zielgruppe (zum Beispiel filtern Sie nach `external_id`), anstatt sich allein auf **Test-Push** im Profil zu verlassen.

Aktivieren Sie für **Canvas**-Nachrichtenschritte mit mehreren Apps die Option **Validate audience at message send** im Nachrichtenschritt, damit Segment- und Filterprüfungen zum Sendezeitpunkt ausgeführt werden. Weitere Informationen finden Sie unter [Nachrichtenschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step).

Allgemeine Informationen zum Test-Push-Verhalten finden Sie unter [Testnachrichten senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) und [Push-FAQ]({{site.baseurl}}/user_guide/channels/push/faqs).

### Wie debugge ich Push Stories auf iOS und Android? {#how-do-i-debug-push-stories-on-ios-and-android}

Beginnen Sie mit [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories) für die Einrichtung und kreativen Anforderungen. Informationen zur Implementierung und Handhabung von Rich-Benachrichtigungen finden Sie unter [Rich-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/rich) und [Push Stories]({{site.baseurl}}/developer_guide/push_notifications/push_stories) im Entwicklerhandbuch.

### Wer erhält die E-Mail „Canvas Messages Delayed 24+ Hours“? {#who-receives-the-canvas-messages-delayed-24-hours-email}

Braze sendet diese Benachrichtigung, wenn Canvas-Nachrichten durch Rate-Limiting 24 Stunden oder länger verzögert werden. Die E-Mail geht an Dashboard-Nutzer:innen, die zuvor Änderungen am betroffenen Canvas vorgenommen haben (basierend auf den Canvas-Änderungsprotokollen). Wenn Braze diese Empfänger:innen nicht ermitteln kann, geht die E-Mail an die **Unternehmensadministrator:innen** des Workspace.

### Wann hört ein:e Nutzer:in auf, Nachrichten nach einem Ausnahme-Event zu erhalten? {#when-does-a-user-stop-receiving-messages-after-an-exception-event}

Braze erfasst den Exit, sobald das Ausnahme-Event eintritt, aber Nutzer:innen können innerhalb eines Schritts verbleiben, bis Timer abgelaufen sind – am deutlichsten sichtbar bei Delay-Schritten. Das Verhalten unterscheidet sich auch zwischen geplanten Schritten und Event-getriggerten Schritten. Informationen zu Zeitabläufen, Beispielen und Analytics-Nuancen finden Sie unter [Exit-Kriterien]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria).

### Warum zeigt mein Aktionspfade-Schritt einen Fehler an, wenn ich eine Link-Alias-Interaktion auswähle? {#why-does-my-action-paths-step-show-an-error-when-i-select-a-link-alias-interaction}

Aktionsgruppen, die E-Mail-Interaktivitäts-Trigger verwenden (zum Beispiel **Click alias in email** oder **Clicked alias in any campaign or Canvas step**), benötigen einen Nachrichtenschritt, der die Nachricht mit diesem Link bereits gesendet hat. Fügen Sie Schritte hinzu oder ordnen Sie sie neu an, sodass die E-Mail vor der Auswertung des Aktionspfade-Schritts gesendet wird, oder wählen Sie eine Interaktion, die zu einer Nachricht passt, die der/die Nutzer:in bereits in diesem Canvas erhalten hat. Die vollständige Liste der Interaktions-Trigger finden Sie unter [Aktionsbasierte Zustellung]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery).

### Wie wirken sich historische Zeitstempel angepasster Events auf aktionsbasierte Canvases und Campaigns aus? {#how-do-historical-custom-event-timestamps-affect-action-based-canvases-and-campaigns}

Braze wertet aktionsbasierte Journeys aus, wenn qualifizierende Events aufgenommen werden und der/die Nutzer:in Ihre Zielgruppenregeln erfüllt. Wenn ein Event außerhalb des Zeitfensters, in dem Ihr Canvas oder Ihre Campaign aktiv war, auf dem Profil eingeht, oder bevor der/die Nutzer:in Ihrer Zielgruppe entsprach, erfolgen Eintritt oder nachgelagerte Versendungen möglicherweise nicht wie erwartet. Vergleichen Sie Event-Zeitstempel mit den Go-Live-Zeiten und der Segment-Zugehörigkeit mithilfe des Nutzeraktivitätsprotokolls und den Schritten zur Fehlerbehebung unter [Fehlerbehebung bei angepassten Events]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#troubleshooting-custom-events). Wenn das Verhalten weiterhin nicht den Erwartungen entspricht, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/braze_support).