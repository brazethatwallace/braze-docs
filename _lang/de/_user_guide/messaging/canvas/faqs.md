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

Dieser Fehler erscheint, wenn die Kombination aus Schrittverzweigungen und der Größe der Einstiegszielgruppe zu Cluster-Performance-Problemen führen kann, die das Senden von Nachrichten verhindern. Lösungsschritte – einschließlich der Verwendung von [Zielgruppenpfaden]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths), der Reduzierung von Verzweigungen oder der Zielgruppengröße sowie dem Neuaufbau in Canvas Flow – finden Sie unter [Fehler „Too many Canvas branches“]({{site.baseurl}}/user_guide/messaging/canvas/troubleshooting#too-many-canvas-branches-error).

### Kann ich „Optimize with BrazeAI<sup>TM</sup>“ mit erneuter Berechtigung in einem Canvas verwenden? {#can-i-use-optimize-with-brazeai-with-re-eligibility-in-a-canvas}

Ja. Canvases können [Optimize with BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#optimize-canvas-variants-with-brazeai) verwenden, wenn die erneute Berechtigung aktiviert ist. Braze kann bei einem erneuten Eintritt nicht garantieren, dass dieselbe Variante zugewiesen wird, da sich die Zuordnung im Laufe der Zeit verschiebt. Campaigns erfordern ein Fenster für die erneute Berechtigung von mindestens 24 Stunden, wenn **Optimize with BrazeAI<sup>TM</sup>** aktiviert ist.

### Was ist der Unterschied zwischen einer Komponente und einem Schritt? {#whats-the-difference-between-a-component-and-a-step}

Eine [Komponente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about) ist ein einzelner Bestandteil Ihres Canvas, mit dem Sie die Effektivität Ihres Canvas bestimmen können. Komponenten können Aktionen wie das Aufteilen der Nutzer:innen-Journey, das Hinzufügen einer Verzögerung und sogar das Testen mehrerer Canvas-Pfade umfassen. Ein Schritt in Canvas bezieht sich auf die personalisierte Nutzer:innen-Journey in Ihren Canvas-Verzweigungen. Im Wesentlichen besteht Ihr Canvas aus einzelnen Komponenten, die Schritte für Ihre Nutzer:innen-Journey erstellen.

### Kann ich ein Canvas mit nicht verbundenen Schritten starten? {#can-i-launch-a-canvas-with-disconnected-steps}

Ja. Sie können Canvases auch nach dem Start mit nicht verbundenen Schritten speichern.

### Wohin gelangen Nutzer:innen, wenn sie einen nicht verbundenen Schritt erreicht haben? {#where-do-users-go-when-theyve-reached-a-disconnected-step}

Wenn sich ein:e Nutzer:in in einem nicht verbundenen Schritt Ihres Canvas-Workflows befindet, rückt er/sie zum nachfolgenden Schritt vor, sofern einer vorhanden ist. Die Einstellung des Schritts bestimmt, wie der/die Nutzer:in fortfahren soll. Dies ist so beabsichtigt, damit Sie Änderungen an Schritten vornehmen können, ohne sie direkt mit dem Rest des Canvas verbinden zu müssen. So haben Sie auch Spielraum zum Testen, bevor Sie sofort live gehen – im Grunde können Sie so einen Entwurf speichern.

Wir empfehlen, die Analytics-Ansicht auf wartende Nutzer:innen in einem Canvas-Schritt zu prüfen, bevor Sie einen Schritt trennen.

### Was passiert, wenn Zielgruppe und Sendezeit für ein Canvas mit einer Variante, aber mehreren Verzweigungen identisch sind? {#what-happens-if-the-audience-and-send-time-are-identical-for-a-canvas-that-has-one-variant-but-multiple-branches}

Wir erstellen einen Job für jeden Schritt – sie werden ungefähr zur gleichen Zeit ausgeführt, und einer davon „gewinnt“. In der Praxis kann dies einigermaßen gleichmäßig verteilt sein, aber es gibt wahrscheinlich zumindest eine leichte Verzerrung zugunsten des Schritts, der zuerst erstellt wurde.

Darüber hinaus können wir keine Garantien dafür geben, wie diese Verteilung genau aussehen wird. Wenn Sie eine gleichmäßige Aufteilung wünschen, fügen Sie einen Filter für [zufällige Bucket-Nummern]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) hinzu.

### Wie werden Canvas-Zielgruppen ausgewertet? {#how-are-canvas-audiences-evaluated}

Standardmäßig werden Filter und Segmente für vollständige Schritte im Canvas zum Sendezeitpunkt geprüft. Der Decision-Split-Schritt führt eine Auswertung direkt nach Erhalt eines vorherigen Schritts durch (oder vor einer Verzögerung).

### Wann wird ein Ausnahme-Event ausgelöst? {#when-does-an-exception-event-trigger}

Ausnahme-Events werden nur ausgelöst, während der/die Nutzer:in darauf wartet, die Canvas-Komponente zu erhalten, mit der es verknüpft ist. Wenn ein:e Nutzer:in eine Aktion im Voraus ausführt, wird das Ausnahme-Event nicht ausgelöst. Wenn Sie Nutzer:innen ausschließen möchten, die ein bestimmtes Event bereits ausgeführt haben, verwenden Sie stattdessen [Filter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).

### Wie wirkt sich das Bearbeiten eines Canvas auf Nutzer:innen aus, die sich bereits im Canvas befinden? {#how-does-editing-a-canvas-affect-users-already-in-the-canvas}

Wenn Sie einige Schritte eines mehrstufigen Canvas bearbeiten, erhalten Nutzer:innen, die bereits in der Zielgruppe waren, aber die Schritte noch nicht erhalten haben, die aktualisierte Version der Nachricht. Beachten Sie, dass dies nur geschieht, wenn sie für den Schritt noch nicht ausgewertet wurden.

Weitere Informationen dazu, was Sie nach dem Start bearbeiten können, finden Sie unter [Änderungen an Ihrem Canvas nach dem Start]({{site.baseurl}}/post-launch_edits).

### Was passiert, wenn Sie ein Canvas stoppen? {#what-happens-when-you-stop-a-canvas}

Wenn Sie ein Canvas stoppen, gilt Folgendes:

- Nutzer:innen werden daran gehindert, in das Canvas einzutreten.
- Es werden keine weiteren Nachrichten gesendet, unabhängig davon, wo sich ein:e Nutzer:in im Flow befindet.
- **Ausnahme:** Canvases mit E-Mails werden nicht sofort gestoppt. Nachdem die Sendeanfragen an SendGrid übergeben wurden, können wir die Zustellung an die Nutzer:innen nicht mehr verhindern.

### Sollte ich ein einzelnes Canvas oder separate Canvases pro Nutzer:innen-Lebenszyklus erstellen? {#should-i-build-one-canvas-or-separate-canvases-per-user-lifecycle}

Je nachdem, was Sie mit Ihrem Canvas erreichen möchten, benötigen Sie möglicherweise unterschiedliche Ansätze für den Aufbau Ihrer Nutzer:innen-Journey. Die Flexibilität von Canvas ermöglicht es Ihnen, Nutzer:innen-Journeys für jede Phase des Nutzer:innen-Lebenszyklus abzubilden. Sehen Sie sich unsere [Braze-Canvas-Templates]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates) an, um verschiedene Beispiele für optimierte Ansätze zur Erstellung effektiver Nutzer:innen-Journeys zu finden.

## Nachrichten und Zustellung {#messages-and-delivery}

### Wann werden In-App-Nachrichten in Canvas gesendet? {#when-are-in-app-messages-in-canvas-sent}

In-App-Nachrichten werden beim nächsten Sitzungsstart gesendet. Das bedeutet: Wenn Nutzer:innen den Canvas-Schritt betreten, bevor der Canvas gestoppt wird, erhalten sie die In-App-Nachricht trotzdem beim nächsten Sitzungsstart – vorausgesetzt, die In-App-Nachricht ist noch nicht abgelaufen.

Es ist möglich, dass Nutzer:innen eine Sitzung starten, bevor der Canvas gestoppt wird, die In-App-Nachricht aber nicht sofort angezeigt bekommen. Das kann passieren, wenn die In-App-Nachricht durch ein angepasstes Event getriggert wird oder verzögert ist. Daher kann es vorkommen, dass Nutzer:innen eine Impression für eine In-App-Nachricht protokollieren und die In-App-Nachricht „erhalten“, nachdem der Canvas gestoppt wurde. Allerdings müsste die Sitzung vor dem Stoppen des Canvas begonnen worden sein, aber **nachdem** der Canvas-Schritt empfangen wurde.

{% alert note %}
Das Stoppen eines Canvas führt nicht dazu, dass Nutzer:innen, die auf den Empfang von Nachrichten warten, die User-Journey verlassen. Wenn Sie den Canvas wieder aktivieren und Nutzer:innen noch auf die Nachricht warten, erhalten sie diese (es sei denn, der Zeitpunkt, zu dem die Nachricht hätte gesendet werden sollen, ist bereits verstrichen – dann wird sie nicht zugestellt).
{% endalert %}

### Warum kann ein Canvas null Sendungen anzeigen, obwohl Impressionen protokolliert werden? {#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged}

Wenn _Gesendete Nachrichten_ für einen Canvas mit einem In-App-Nachrichten-Schritt immer null sind, liegt das daran, dass die Zustellung von In-App-Nachrichten anders funktioniert als bei anderen Messaging-Kanälen.

In-App-Nachrichten werden vom SDK „abgerufen“ und nicht von Braze „gepusht“. In-App-Nachrichten für berechtigte Nutzer:innen werden automatisch beim Sitzungsstart zugestellt und „warten“ auf das Trigger-Event, bevor sie angezeigt werden. Da berechtigte Nutzer:innen die Nachricht beim Start einer Sitzung erhalten, meldet Braze dies nicht als Sende-Event. Wenn Nutzer:innen das Trigger-Event ausführen, wird die Nachricht angezeigt und Braze protokolliert eine Impression und markiert den Canvas-Schritt (oder die Campaign) als empfangen im Nutzerprofil. Folglich ist die Gesamtzahl der _Sendungen_ für In-App-Nachrichten null.

### Warum haben Nutzer:innen meine In-App-Nachricht nach einer langen Verzögerung oder Verzweigung nicht erhalten? {#why-didnt-users-receive-my-in-app-message-after-a-long-delay-or-branch}

Nachdem vorgelagerte [Delay]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step)-Schritte und Zielgruppenprüfungen abgeschlossen sind, werden Nutzer:innen erst für eine In-App-Nachricht berechtigt, wenn sie den Nachrichten-Schritt erreichen. Wenn die Nachricht zu einem Kalenderdatum oder innerhalb eines kurzen Fensters **nach Verfügbarkeit des Schritts** abläuft, können Nutzer:innen auf langsameren Pfaden nach dem Ablauf ankommen und die Nachricht nie sehen. Stimmen Sie den Ablauf auf Ihre längsten realistischen Pfadverzögerungen ab. Weitere Informationen und Beispiele finden Sie unter [Ablauf von In-App-Nachrichten]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas#in-app-message-expiration).

### Warum sehe ich „Canvas Entry Properties may not be used in In-App Messages.“? {#why-do-i-see-canvas-entry-properties-may-not-be-used-in-in-app-messages}

Diese Meldung erscheint, wenn die Personalisierung auf Felder verweist, die In-App-Nachrichten in Canvas nicht auflösen können. Verwenden Sie das `context`-Objekt wie unter [Kontext- und Event-Eigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) und [Nachrichten-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) beschrieben. Der Legacy-Liquid-Namespace `canvas_entry_properties` unterliegt anderen Einschränkungen als `context`. Wenn Sie Werte über mehrere Schritte hinweg beibehalten müssen, besprechen Sie [persistente Eigenschaften im ursprünglichen Canvas-Editor]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties) mit Ihrem Braze-Team. Gespeicherte Werte werden gelöscht, wenn Nutzer:innen den Canvas verlassen, bevor das Gerät die In-App-Payload heruntergeladen hat.

### Wo finde ich Button-Klicks für Drag-and-Drop-In-App-Nachrichten in Canvas? {#where-can-i-find-button-clicks-for-drag-and-drop-in-app-messages-in-canvas}

Metriken auf Button-Ebene für Drag-and-Drop-In-App-Nachrichten erscheinen auf der Analytics-Karte des **Nachrichten**-Schritts unter **Canvas-Details** – nicht nur in der übergeordneten Canvas-Zusammenfassung. Öffnen Sie den Canvas, wählen Sie den Nachrichten-Schritt aus und überprüfen Sie dort das In-App-Engagement. Weitere Informationen zu Reporting-Konzepten finden Sie unter [Messen und Testen mit Canvas-Analytics]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics).

### Kann ich für jede Variante im selben Canvas-Nachrichten-Schritt oder multivariaten Versand unterschiedliche Sendezeiten planen? {#can-i-schedule-different-send-times-for-each-variant-in-the-same-canvas-message-step-or-multivariate-send}

Nein. Varianten in derselben multivariaten Konfiguration oder im selben Nachrichten-Schritt teilen sich einen Zustellungszeitplan. Sie können nicht eine Variante um 18 Uhr und eine andere um 19 Uhr für denselben geplanten Versand festlegen.

Um Sendungen zu staffeln oder unterschiedliche Zeiten pro Pfad zu verwenden, probieren Sie die folgenden Methoden:

- Separate Nachrichten-Schritte mit Delay-Schritten dazwischen, sodass jede Nachricht ihren eigenen Zeitplan hat.
- Verwenden Sie Verzweigungen oder einen [Experimentpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step)-Schritt, damit Nutzer:innen Pfaden mit unterschiedlichem Timing folgen.
- Separate Campaigns, wenn der Anwendungsfall nicht innerhalb eines Canvas bleiben muss.

Informationen zu multivariaten und A/B-Konzepten in Campaigns finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing).

### Was passiert, wenn Nutzer:innen bei einem Canvas-Nachrichten-Schritt ein globales Frequency-Capping erreichen? {#what-happens-if-a-user-is-global-frequency-capped-at-a-canvas-message-step}

Sie erhalten den Versand für den begrenzten Kanal nicht, aber Nachrichten-Schritte bringen Nutzer:innen trotzdem voran, wenn eine Nachricht aufgrund von globalem Frequency-Capping nicht gesendet wird. Die Schritt-für-Schritt-Fälle zum Fortschritt finden Sie unter [Wie Nutzer:innen vorankommen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance). Globales Frequency-Capping allein bewirkt nicht, dass Nutzer:innen einen Canvas verlassen; dieses Verhalten ist unabhängig von den **Zustellungsvalidierungen** eines Nachrichten-Schritts. Weitere Details finden Sie unter [Rate-Limiting und Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping).

### Warum sind die Sendungen niedriger als die geschätzte Zielgruppengröße? {#why-are-sends-lower-than-the-estimated-audience-size}

Sendungen können aus vielen der gleichen Gründe niedriger als die **geschätzte Zielgruppe** sein wie bei [Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/faq#why-are-sends-lower-than-the-estimated-audience-size), darunter Frequency-Caps, strenge Geräte- oder Browser-Filter, Fenster für erneute Berechtigung, Rate-Limiting und Ausschlüsse auf Kanalebene (z. B. Push-Erreichbarkeit oder Prüfungen des E-Mail-Abos und der Zustellbarkeit).

Canvas-spezifische Faktoren gelten ebenfalls:

- **Aktionsbasierter oder API-getriggerter Eintritt:** Nutzer:innen treten erst ein (und erhalten Schritte), nachdem sie das Eintrittsverhalten ausgeführt haben, sodass die tatsächlichen Sendungen hinter der Vorab-Schätzung zurückbleiben, bis diese Aktionen erfolgen.
- **Zielgruppenpfade:** Nutzer:innen werden zum Zweig mit der höchsten Priorität weitergeleitet, für den sie sich qualifizieren, sodass nachgelagerte Zweige möglicherweise weniger Nutzer:innen erhalten, als eine flache Segmentzählung vermuten lässt.
- **Zielgruppen- und Sendezeitprüfungen:** Vollständige Schritte werten Filter zum Sendezeitpunkt erneut aus, sofern Sie nichts anderes konfigurieren. Nutzer:innen, die sich zum Zeitpunkt der Canvas-Erstellung qualifiziert haben, können vor dem Versand einer Nachricht herausfallen.
- **Kontrollgruppen:** Globale oder Canvas-Kontrollgruppen halten einen Anteil der Eintretenden vom Messaging zurück.
- **Ruhezeiten und Verzögerungen:** Nachrichten können zurückgehalten oder umgeplant werden, wodurch Sendungen aus dem betrachteten Berichtszeitraum verschoben werden.
- **Maximale Eintritts- oder Zielgruppenlimits:** Eintritts- oder Sendelimits stoppen zusätzliche Nutzer:innen, selbst wenn das zugrunde liegende Segment größer ist.
- **Berichtszeitraum:** Der Analytics-Bereich enthält möglicherweise nicht jeden Versand, den Sie mit der Schätzung vergleichen.

### Warum stimmen geschätzte Zielgruppe und Canvas-Nutzerzahlen nicht überein? {#why-dont-estimated-audience-and-canvas-user-counts-match}

Die **geschätzte Zielgruppe** spiegelt wider, wer zum Zeitpunkt der Schätzung Ihren Segment- und Eintrittsfiltern entspricht. Danach können verzögerte oder aktionsbasierte Eintritte, erneute Berechtigung, API-Trigger oder Verzweigungsrouting dazu führen, dass mehr Profile die Journey berühren als in der Momentaufnahme. Nutzer:innen können auch herausfallen, wenn Sendezeitfilter fehlschlagen, was die tatsächlichen Eintritte oder Sendungen verringert. Vergleichen Sie Timing, Limits und Auswertungseinstellungen zusammen mit [Warum sind die Sendungen niedriger als die geschätzte Zielgruppengröße?](#why-are-sends-lower-than-the-estimated-audience-size).

### Warum ist _Eindeutige Empfänger:innen_ höher als die Anzahl der Nutzer:innen, die ich angesprochen habe? {#why-is-_unique-recipients_-higher-than-the-number-of-users-i-targeted}

_Eindeutige Empfänger:innen_ kann höher sein als die erwartete Zielgruppe, da Braze **eindeutige tägliche Empfänger:innen** für das Canvas- und Campaign-Reporting erfasst. Dies unterstützt eine genaue Konversions-Attribution jedes Mal, wenn Nutzer:innen eine Nachricht in der Journey erhalten.

Wenn Nutzer:innen beispielsweise am Montag einen Canvas-Schritt erhalten und am Freitag erneut und nach jedem Versand konvertieren, kann Braze zwei Empfänger:innen-Zeilen und zwei relevante Konversionen zählen. Bei wiederkehrenden Eintritten oder erneuter Berechtigung kann dieselbe kleine Gruppe von Profilen über mehrere Tage hinweg mehrere _eindeutige Empfänger:innen_ erzeugen.

### Warum verzeichnet mein Canvas niedrigere Sendungsraten? {#why-is-my-canvas-experiencing-lower-send-rates}

Wenn Sie feststellen, dass Ihr täglich geplanter Canvas im Laufe der Zeit an weniger Nutzer:innen sendet, prüfen Sie Folgendes:

- **Prüfen Sie, ob die erneute Berechtigung aktiviert ist:** Ohne erneute Berechtigung nimmt Braze jede:n Nutzer:in nur einmal in den Canvas auf. Bei täglich geplanten Canvases sind nur Nutzer:innen für jeden Eintritt berechtigt, die der Zielgruppe entsprechen und noch nicht in den Canvas eingetreten sind. Je mehr Nutzer:innen eintreten, desto weniger berechtigte Nutzer:innen gibt es bei jedem späteren Eintritt, sodass das Eintrittsvolumen abnimmt.
- **Prüfen Sie, ob die Zielgruppe eine feste Mitgliedschaft hat:** Zielgruppen, die aus einer festen Nutzerliste erstellt wurden (z. B. ein [CSV-Import]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import) als Segmentfilter), gewinnen nicht automatisch neue Mitglieder. Ohne neue Teilnehmende kann sich das Eintrittsvolumen nicht erholen, während Nutzer:innen in den Canvas eintreten.

Informationen zu [Rate-Limits für die Zustellgeschwindigkeit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) und anderen Faktoren, die Sendungen für ein einzelnes Vorkommen verringern, finden Sie unter [Warum sind die Sendungen niedriger als die geschätzte Zielgruppengröße?](#why-are-sends-lower-than-the-estimated-audience-size).

### Warum zeigt ein kleines Kontrollgruppen-Segment Änderungen in der historischen Mitgliedschaft? {#why-does-a-small-control-group-segment-show-changes-in-historical-membership}

Historische Mitgliedschafts-Charts verwenden geschätzte Stichproben, sodass kleine Segmente – einschließlich Segmente der [globalen Kontrollgruppe]({{site.baseurl}}/user_guide/audience/global_control_group) – tägliche Schwankungen zeigen können, selbst wenn die zugrunde liegende Zielgruppe stabil ist. Informationen dazu, wie Schätzungen funktionieren und warum Charts schwanken können, finden Sie unter [Historische Segmentmitgliedschaftsgröße anzeigen]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#viewing-historical-segment-membership-size).

## Analytics und Konversionen {#analytics-and-conversions}

### Wie ordnet das Conversions-Dashboard Canvas-Konversionen zu? {#how-does-the-conversions-dashboard-attribute-canvas-conversions}

Das [Conversions-Dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/conversions) ordnet Canvas-Konversionen basierend auf der [Attributionsmethode]({{site.baseurl}}/user_guide/analytics/dashboards/conversions#attribution-methods) zu, die Sie auswählen (z. B. **Upon Receipt**, **Upon Send**, **Upon Open** oder **Upon Click**). Damit Nutzer:innen im Bericht erscheinen, müssen sie den Canvas oder die Campaign betreten, die ausgewählte Attributionsmethode auslösen und das Konversions-Event innerhalb Ihrer Berichtseinstellungen durchführen.

Informationen zu Konversionsregeln auf Schritt- und Variantenebene in Canvas Analytics finden Sie unter [Wie werden Nutzerkonversionen in einem Canvas getrackt?](#how-are-user-conversions-tracked-in-a-canvas).

### Wie werden Nutzerkonversionen in einem Canvas getrackt? {#how-are-user-conversions-tracked-in-a-canvas}

Nutzer:innen können nur einmal pro Canvas-Entry konvertieren. Konversionen werden der zuletzt empfangenen Nachricht für diesen Entry zugewiesen. Der Zusammenfassungsblock am Anfang eines Canvas spiegelt alle Konversionen wider, die von Nutzer:innen innerhalb dieses Pfads durchgeführt wurden, unabhängig davon, ob sie eine Nachricht erhalten haben. Jeder nachfolgende Schritt zeigt nur Konversionen an, die stattfanden, während dieser der letzte Schritt war, den die Nutzer:innen erhalten haben.

{% alert note %}
Wenn Nutzer:innen einen Canvas erneut betreten, werden Konversions-Events nur für den letzten Entry getrackt. Konversions-Events werden nicht für vorherige Entries protokolliert, selbst wenn das Konversions-Event nachträglich ergänzt wird.
{% endalert %}

{% details Für Beispiele aufklappen %}

**Beispiel 1**

Es gibt einen Canvas-Pfad mit 10 Push-Benachrichtigungen, und das Konversions-Event ist „Sitzungsstart“ („App öffnen“):

- Nutzer:in A öffnet die App nach dem Entry, aber vor dem Empfang der ersten Nachricht.
- Nutzer:in B öffnet die App nach jeder Push-Benachrichtigung.

**Ergebnis:** Die Zusammenfassung zeigt zwei Konversionen, während die einzelnen Schritte eine Konversion beim ersten Schritt und null bei allen nachfolgenden Schritten anzeigen.

{% alert note %}
Wenn Ruhezeiten aktiv sind, wenn das Konversions-Event stattfindet, gelten die gleichen Regeln.
{% endalert %}

**Beispiel 2**

Es gibt einen Canvas mit einem Schritt und aktivierten Ruhezeiten:

1. Nutzer:in betritt den Canvas.
2. Der erste Schritt hat keine Verzögerung, fällt aber in die eingestellten Ruhezeiten, sodass die Nachricht unterdrückt wird.
3. Nutzer:in führt das Konversions-Event durch.

**Ergebnis:** Die/der Nutzer:in wird in der gesamten Canvas-Variante als konvertiert gezählt, aber nicht im Schritt, da sie/er den Schritt nicht erhalten hat.

{% enddetails %}

### Was ist der Unterschied zwischen den verschiedenen Konversionsraten-Typen? {#whats-the-difference-between-the-different-conversion-rate-types}

- Canvas-Gesamtkonversionen spiegeln wider, wie viele eindeutige Nutzer:innen ein Konversions-Event abgeschlossen haben, nicht wie viele Konversionen sie jeweils durchgeführt haben.
- Die Varianten-Konversionsrate oder der Zusammenfassungsblock am Anfang eines Canvas spiegelt alle Konversionen wider, die von Nutzer:innen innerhalb dieses Pfads durchgeführt wurden, unabhängig davon, ob sie eine Nachricht erhalten haben, als Gesamtsumme.
- Die Schritt-Konversionsrate gibt an, wie viele Personen diesen Nachrichtenschritt erhalten und eines der definierten Konversions-Events abgeschlossen haben.

### Warum ist meine Canvas-Schritt-Konversionsrate nicht gleich meiner Canvas-Varianten-Gesamtkonversionsrate? {#why-is-my-canvas-step-conversion-rate-not-equal-to-my-canvas-variant-total-conversion-rate}

Es ist üblich, dass die Konversions-Gesamtzahl einer Canvas-Variante größer ist als die Summe ihrer Schritt-Gesamtzahlen. Dies geschieht, weil Nutzer:innen ein Konversions-Event für eine Variante ausführen können, sobald sie die Variante betreten. Dieses Konversions-Event zählt jedoch nicht für einen Canvas-Schritt. Daher werden alle Nutzer:innen, die den Canvas betreten und das Konversions-Event vor dem Empfang des ersten Canvas-Schritts ausführen, in die Varianten-Konversions-Gesamtzahl einbezogen, aber nicht in die Schritt-Gesamtzahl. Das Gleiche gilt für Nutzer:innen, die den Canvas betreten, aber den Canvas verlassen, bevor sie einen Schritt erhalten.

Beachten Sie, dass es auch möglich ist, dass Nutzer:innen eine Variante betreten, keine Nachricht von einem Schritt erhalten und dann konvertieren. In diesem Fall wird auf Schrittebene keine Konversion protokolliert. Da die/der Nutzer:in jedoch technisch gesehen konvertiert hat, wird eine Konversion auf Canvas-Ebene protokolliert.

### Wie kann ich bestätigen, ob meine Nutzer:innen einen API-getriggerten Canvas erhalten haben? {#how-can-i-confirm-if-my-users-received-an-api-triggered-canvas}

Sie können [ein Segment erstellen]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment), indem Sie einen Canvas-Filter verwenden, um zu bestätigen, ob Nutzer:innen den Canvas betreten oder einen bestimmten Canvas-Schritt erhalten haben. Verwenden Sie beispielsweise einen Canvas-Entry-Filter, wenn Sie bestätigen möchten, dass Nutzer:innen den API-getriggerten Canvas betreten haben, oder einen Filter für empfangene Schritte, wenn Sie bestätigen möchten, dass sie eine Nachricht vom Canvas erhalten haben. Verwenden Sie dann den [`/users/export/segment`-Endpunkt]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment), um die Nutzer:innen in diesem Segment zu exportieren.

### Kann ich einen Canvas löschen? {#can-i-delete-a-canvas}

Nein, aber Sie können [einen Canvas archivieren]({{site.baseurl}}/user_guide/messaging/governance/archiving).

### Wie setze ich einen archivierten Canvas oder eine archivierte Campaign fort? {#how-do-i-resume-an-archived-canvas-or-campaign}

Archivierte Nachrichten werden erst gesendet, wenn Sie sie in einen bearbeitbaren Zustand zurückversetzen. [Dearchivieren]({{site.baseurl}}/user_guide/messaging/governance/archiving#unarchiving) Sie die Campaign oder den Canvas, legen Sie den Entry-Zeitplan oder die Sendezeit auf ein zukünftiges Fenster fest (oder duplizieren Sie die Journey, wenn Sie eine saubere Kopie benötigen), und wählen Sie dann **Fortsetzen** oder starten Sie wie gewünscht. Siehe [Campaigns und Canvases archivieren]({{site.baseurl}}/user_guide/messaging/governance/archiving).

### Warum wird mein Canvas nicht gespeichert, obwohl kein Fehler angezeigt wird? {#why-doesnt-my-canvas-save-when-no-error-appears}

Leere **Angepasstes Attribut**-Filter in Zielgruppen- oder Schritt-Filtern können das Speichern blockieren, ohne eine detaillierte Validierungsmeldung auszugeben. Öffnen Sie jede Filterkarte, entfernen Sie unvollständige Regeln für angepasste Attribute oder geben Sie sowohl den Attributnamen als auch den Wert ein, und wählen Sie dann erneut **Speichern**.

### Warum ist ein Tag von meinem Canvas oder meiner Campaign verschwunden? {#why-did-a-tag-disappear-from-my-canvas-or-campaign}

Wenn ein [Tag]({{site.baseurl}}/user_guide/messaging/governance/tags) aus Ihrem Workspace gelöscht wird, entfernt Braze ihn aus jeder Campaign und jedem Canvas, die darauf verwiesen haben. Diese Bereinigung erzeugt nicht immer einen eigenen Eintrag im Canvas-Änderungsprotokoll.

### Wie kann ich Analytics für jede meiner Canvas-Komponenten anzeigen? {#how-can-i-view-analytics-for-each-of-my-canvas-components}

Um die Analytics einer Canvas-Komponente anzuzeigen, navigieren Sie zu Ihrem Canvas und scrollen Sie auf der Seite **Canvas-Details** nach unten. Hier können Sie die Analytics jeder Komponente anzeigen. Weitere Details finden Sie unter [Canvas Analytics]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics).

### Wann ist das Engagement eines Canvas-Schritts auf einem Nutzerprofil sichtbar? {#when-is-engagement-from-a-canvas-step-visible-on-a-user-profile}

Filter wie `Received Message from Canvas Step` werden aktualisiert, nachdem Braze das entsprechende Sende-, Empfangs- oder Engagement-Event für diesen Schritt protokolliert hat. In-App-Nachrichten können Impressionen getrennt von sendebasierten Metriken protokollieren. Siehe [Warum kann ein Canvas null Sends anzeigen, obwohl Impressionen protokolliert wurden?](#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged). Dieselben Events erscheinen in den Schritt-Metriken unter **Canvas-Details**.

### Ist bei der Betrachtung der Anzahl eindeutiger Nutzer:innen Canvas Analytics oder der Segmentierer genauer? {#when-looking-at-the-number-of-unique-users-is-canvas-analytics-or-the-segmenter-more-accurate}

Der Segmentierer ist eine genauere Statistik für eindeutige Nutzerdaten im Vergleich zu Canvas- oder Campaign-Statistiken. Dies liegt daran, dass Canvas- und Campaign-Statistiken Zahlen sind, die Braze inkrementiert, wenn etwas passiert – was bedeutet, dass es Variablen gibt, die dazu führen können, dass diese Zahl von der des Segmentierers abweicht. Beispielsweise können Nutzer:innen mehr als einmal für einen Canvas oder eine Campaign konvertieren.

### Warum weicht die Anzahl der Nutzer:innen, die einen Canvas betreten, von der erwarteten Anzahl ab? {#why-does-the-number-of-users-entering-a-canvas-not-match-the-expected-number}

Die Anzahl der Nutzer:innen, die einen Canvas betreten, kann von Ihrer erwarteten Anzahl abweichen, je nachdem, wie Zielgruppen und Trigger ausgewertet werden. In Braze wird eine Zielgruppe vor dem Trigger ausgewertet (es sei denn, Sie verwenden einen [Änderung eines Attributs]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)-Trigger). Dies führt dazu, dass Nutzer:innen aus dem Canvas herausfallen, wenn sie nicht Teil Ihrer ausgewählten Zielgruppe sind, bevor Trigger-Aktionen ausgewertet werden.

### Was passiert mit anonymen Nutzer:innen während ihrer Canvas-Journey? {#what-happens-to-anonymous-users-during-their-canvas-journey}

Anonyme Nutzer:innen können zwar Canvases betreten und verlassen, aber ihre Aktionen werden keinem bestimmten Nutzerprofil zugeordnet, bis sie identifiziert werden, sodass ihre Interaktionen möglicherweise nicht vollständig in Ihren Analytics getrackt werden. Sie können den [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder) verwenden, um einen Bericht über diese Metriken zu erstellen.

{% alert tip %}
Für weitere Unterstützung bei der Canvas-Fehlerbehebung wenden Sie sich bitte innerhalb von 30 Tagen nach dem Auftreten Ihres Problems an den Braze-Support, da uns nur die Diagnoseprotokolle der letzten 30 Tage zur Verfügung stehen.
{% endalert %}

### Kann ich Nutzer:innen, die sich derzeit in einer Canvas-Journey befinden, von einer Campaign oder einem Segment ausschließen? {#can-i-exclude-users-who-are-currently-in-a-canvas-journey-from-a-campaign-or-segment}

Verwenden Sie [Segmentierungsfilter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) wie `Entered Canvas Variation`, `In Canvas Control Group` oder `Received Message from Canvas Step`, um Nutzer:innen basierend auf Canvas-Entry, Variantenzuweisung oder Schritt-Engagement anzusprechen. Diese Filter werten den Entry-Verlauf und die Interaktionen aus – sie zeigen nicht an, ob Nutzer:innen noch aktiv eine Journey durchlaufen.

Um Nutzer:innen basierend auf aktiver Canvas-Teilnahme ein- oder auszuschließen, fügen Sie [Nutzeraktualisierungs]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)-Schritte bei Canvas-Entry und -Exit hinzu, um angepasste Attribute zu setzen und zu löschen, und filtern Sie dann in Campaigns oder Segments nach diesen Attributen.

## Segmentierung {#segmentation}

### Was ist der Unterschied zwischen „Hat die Canvas-Variante nicht betreten“ und „Ist nicht in der Canvas-Kontrollgruppe“? {#what-is-the-difference-between-has-not-entered-canvas-variation-and-is-not-in-canvas-control-group}

Eine vollständige Übersicht der Filterdefinitionen finden Sie unter [Segmentierungsfilter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).

#### Hat die Canvas-Variante nicht betreten {#has-not-entered-canvas-variation}

Die/der Nutzer:in hat niemals einen Varianten-Pfad eines bestimmten Canvas betreten. Alle Nutzer:innen, die sich nicht in der Kontrollgruppe befinden, sind eingeschlossen – unabhängig davon, ob sie das Canvas betreten haben. Dies umfasst Nutzer:innen, die eine andere Variante betreten haben, sowie Nutzer:innen, die keine Variante betreten haben.

#### Ist nicht in der Canvas-Kontrollgruppe {#is-not-in-canvas-control-group}

Die/der Nutzer:in hat das Canvas betreten, befindet sich aber nicht in der Kontrollgruppe und hat folglich eine Variante erhalten. Dies umfasst nur Nutzer:innen, die das Canvas betreten haben.

Beachten Sie, dass die Variantenzuweisung beim Canvas-Eintritt erfolgt. Wenn ein:e Nutzer:in ein Canvas nicht betreten hat, wird keine Variante zugewiesen. Mit anderen Worten: Sie befinden sich weder in der Kontrollgruppe noch in einer Variante.

## Originaler Canvas-Editor {#original-canvas-editor}

{% details Für FAQ zum originalen Canvas-Editor aufklappen %}

### Wie konvertiere ich ein bestehendes Canvas vom originalen Editor zum aktuellen Editor? {#how-do-i-convert-an-existing-canvas-from-the-original-editor-to-the-current-editor}

Sie können [Ihr Canvas klonen]({{site.baseurl}}/cloning_canvases). Dadurch wird eine Kopie Ihres originalen Canvas im aktuellsten Canvas-Workflow erstellt.

### Was sind die Hauptunterschiede zwischen dem aktuellen und dem originalen Canvas-Editor? {#what-are-the-main-differences-between-the-current-and-original-canvas-editors}

#### Canvas-Komponenten-Symbolleiste {#canvas-component-toolbar}

Zuvor wurde im originalen Canvas-Editor standardmäßig ein vollständiger Schritt hinzugefügt, wenn Sie einen Schritt in der User Journey erstellt haben. Diese vollständigen Schritte werden durch verschiedene Canvas-Komponenten ersetzt, was Ihnen eine bessere Übersicht und mehr Anpassungsmöglichkeiten bei der Bearbeitung bietet. Sie können alle Ihre Canvas-Komponenten sofort über die Canvas-Schritt-Symbolleiste sehen.

#### Schrittverhalten {#step-behavior}

Zuvor enthielt jeder vollständige Schritt Informationen wie Verzögerungs- und Zeitplaneinstellungen, Ausnahme-Events, Zielgruppenfilter, Nachrichtenkonfiguration und Optionen für den Nachrichtenfortschritt – alles in einer Komponente. Im aktuellen Editor sind dies separate Einstellungen, um die Canvas-Erstellung anpassbarer zu gestalten, was auch einige Unterschiede in der Funktionalität mit sich bringt.

#### Fortschritt der Nachrichtenkomponente {#message-component-advancement}

[Nachrichtenkomponenten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) lassen alle Nutzer:innen, die den Schritt betreten, fortschreiten. Es ist nicht erforderlich, das Fortschrittsverhalten der Nachricht festzulegen, was die Konfiguration des gesamten Schritts vereinfacht. Wenn Sie die Option **Fortschritt bei gesendeter Nachricht** implementieren möchten, fügen Sie einen separaten Zielgruppenpfad hinzu, um Nutzer:innen herauszufiltern, die den vorherigen Schritt nicht erhalten haben.

#### Verzögerungsverhalten „in“ {#delay-in-behavior}

[Verzögerungskomponenten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) warten die gesamte Verzögerungszeit ab, bevor sie zum nächsten Schritt übergehen.

Angenommen, wir haben am 12. April eine Verzögerungskomponente, bei der die Verzögerung so eingestellt ist, dass Nutzer:innen am nächsten Tag um 14 Uhr zum nächsten Schritt weitergeleitet werden. Ein:e Nutzer:in betritt die Komponente am 13. April um 14:01 Uhr.
- Im originalen Workflow würde die Person am 14. April um 14 Uhr zum nächsten Schritt übergehen, was weniger als ein Tag nach dem Eintrittszeitpunkt ist.
- Im aktuellen Editor würde die Person am 15. April um 14 Uhr zum nächsten Schritt übergehen. Beachten Sie, dass dies die gleiche Uhrzeit ist, aber mehr als ein Tag nach dem Eintrittszeitpunkt.

#### Intelligentes Timing – Verhalten {#intelligent-timing-behavior}

Da [intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) in der Nachrichtenkomponente gespeichert wird, werden Verzögerungen vor den Berechnungen des intelligenten Timings angewendet. Das bedeutet, dass Nutzer:innen die Nachricht je nach Eintrittszeitpunkt in die Komponente möglicherweise später erhalten als in einem Canvas, das mit dem originalen Canvas-Workflow erstellt wurde.

Angenommen, Ihre Verzögerung ist auf 2 Tage eingestellt, intelligentes Timing ist aktiviert und hat ermittelt, dass die beste Zeit für den Nachrichtenversand 14 Uhr ist. Ein:e Nutzer:in betritt den Verzögerungsschritt um 14:01 Uhr.
- **Aktueller Workflow:** Es dauert 48 Stunden, bis die Verzögerung abgelaufen ist, sodass die Person die Nachricht am dritten Tag um 14 Uhr erhält.
- **Originaler Workflow:** Die Person erhält die Nachricht am zweiten Tag um 14 Uhr.

Beachten Sie: Wenn intelligentes Timing aktiviert ist, wird die Nachricht innerhalb von 24 Stunden nach Eintritt der Person in die Nachrichtenkomponente zum ermittelten optimalen Zeitpunkt gesendet (auch wenn keine Verzögerungskomponente beteiligt ist).

#### Ausnahme-Events {#exception-events}

##### Ruhezeiten {#quiet-hours}

Ausnahme-Events werden mithilfe von Aktionspfaden angewendet, die von Nachrichtenschritten getrennt sind. Ruhezeiten werden in der Nachrichtenkomponente durchgesetzt. Das bedeutet: Wenn ein:e Nutzer:in den Aktionspfad bereits passiert hat (und nicht durch das Ausnahme-Event ausgeschlossen wurde), dann auf Ruhezeiten trifft, wenn er/sie die Nachrichtenkomponente erreicht, und das Canvas so konfiguriert ist, dass die Nachricht nach den Ruhezeiten erneut gesendet wird, wird das Ausnahme-Event nicht mehr angewendet. Beachten Sie, dass dieser Anwendungsfall nicht häufig vorkommt.

Für Segmente und Filter bietet der Nachrichtenschritt Zustellungsvalidierungen, mit denen Nutzer:innen zusätzliche Segmente und Filter konfigurieren können, die zum Sendezeitpunkt überprüft werden. Dies verhindert den oben genannten Ruhezeiten-Sonderfall.

##### Zeitplaneinstellung „in“ oder „am nächsten“ {#in-or-on-the-next-schedule-setting}

Ausnahme-Events werden mithilfe von Aktionspfaden erstellt. Aktionspfade unterstützen nur „nach einem X-Zeitfenster“ und nicht „in X Zeit“ oder „am nächsten X Zeitpunkt“.

{% enddetails %}

### Was sollte ich bei der Einreichung eines Support-Tickets für einen „Request Timed Out“-Fehler angeben? {#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error}

Wenn beim Bearbeiten eines Canvas ein „Request Timed Out“-Fehler auftritt und Sie [Braze-Support]({{site.baseurl}}/braze_support) kontaktieren müssen, fügen Sie die folgenden Informationen bei, um die Lösung zu beschleunigen:

{% multi_lang_include messaging/support_ticket_request_timed_out_details.md context='canvas' %}

## Canvas-Zustellung und Fehlerbehebung {#canvas-delivery-and-troubleshooting}

### Können verwaiste Nutzer:innen Canvas-Nachrichten erhalten? {#are-orphaned-users-eligible-to-receive-canvas-messages}

Nein. [Verwaiste Nutzer:innen]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#what-happens-when-you-identify-anonymous-users) sind nicht berechtigt, Nachrichten zu erhalten. Wenn ein Profil verwaist, während sich ein:e Nutzer:in in einem Canvas-Journey befindet, wird der Flow stillschweigend verlassen. Analytics zeigt möglicherweise nicht immer ein **Exited**-Event für diesen Exit an, und die Workflow-Zusammenfassung kann ein `partial_update_token` ohne `exited_date` oder `exit_reason` enthalten.

Weitere Informationen über Zusammenführungen und verwaiste Profile finden Sie unter [Doppelte Nutzer:innen zusammenführen]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users).

### Werden bereits an den ESP gesendete Nachrichten noch zugestellt, wenn ich ein aktives Canvas oder eine Campaign stoppe? {#if-i-stop-an-active-canvas-or-campaign-do-messages-already-sent-to-the-esp-still-deliver}

Ja. Nachdem Braze eine Anfrage an Ihren E-Mail-Anbieter (ESP) gesendet hat, kann Braze diesen Versand nicht mehr zurückrufen. Das Stoppen eines Canvas oder einer Campaign verhindert neue Versandanfragen, aber Nachrichten, die bereits an den ESP übergeben wurden, können weiterhin zugestellt werden und die Versandzähler erhöhen, während der ESP sie verarbeitet.

Dies ist dasselbe Verhalten, das unter [Was passiert, wenn Sie ein Canvas stoppen](#what-happens-when-you-stop-a-canvas) beschrieben wird: E-Mail-Versendungen, die sich gerade im Versand befinden, werden nicht sofort angehalten.

### Wie kann ich bestätigen, dass ein Canvas-Webhook-Schritt ohne nutzersichtbaren Inhalt ausgeführt wurde? {#how-can-i-confirm-a-canvas-webhook-step-fired-without-user-visible-content}

Braze trackt Webhook-**Versendungen** und zugehörige Zustellergebnisse für [Webhook]({{site.baseurl}}/user_guide/channels/webhooks)-Schritte in Campaigns und Canvases. Verwenden Sie Schritt-Analytics, [Webhook-Reporting]({{site.baseurl}}/user_guide/channels/webhooks/reporting) oder [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)-Webhook-Events, um zu bestätigen, dass der Schritt ausgeführt wurde. Die Anfrage-Logs Ihres Endpunkts bieten zusätzliche Bestätigung, wenn Sie einen serverseitigen Empfangsnachweis benötigen.

Braze enthält kein integriertes unsichtbares Tracking-Pixel für Webhook-Schritte. Verlassen Sie sich auf die Braze-Webhook-Metriken und Ihre Endpunkt-Protokollierung anstatt auf benutzerdefinierte Ein-Pixel-Bildanfragen.

### Warum hat mein Webhook-Schritt kein Body-Feld? {#why-does-my-webhook-step-have-no-body-field}

Webhook-Schritte verwenden einen Request-Body für `POST`, `PUT`, `PATCH` und `DELETE`. Wenn Sie die Methode auf `GET` umstellen, entfernt Braze das Body-Feld, da GET-Anfragen keinen Request-Body unterstützen. Wechseln Sie zurück zu einer Methode, die einen Body unterstützt, wenn Sie JSON- oder Formulardaten senden möchten. Weitere Informationen zu Methoden finden Sie unter [Einen Webhook erstellen]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#http-method).

### Wie verwende ich spacer.gif in einem Webhook-Schritt? {#how-do-i-use-spacergif-in-a-webhook-step}

Braze hostet ein `spacer.gif`-Platzhalterbild auf `cdn.braze.com` und `braze-images.com`. Einige Teams verwenden eine Webhook-URL, die auf dieses Bild verweist, wenn ein Schritt ausgelöst werden muss, ohne einen externen Endpunkt aufzurufen. Standard-Webhook-Schritte sollten einen echten Endpunkt aufrufen. Verwenden Sie [Webhook-Reporting]({{site.baseurl}}/user_guide/channels/webhooks/reporting) und Ihre Endpunkt-Logs, um die Zustellung zu bestätigen, wie unter [Wie kann ich bestätigen, dass ein Canvas-Webhook-Schritt ohne nutzersichtbaren Inhalt ausgeführt wurde?](#how-can-i-confirm-a-canvas-webhook-step-fired-without-user-visible-content) beschrieben.

### Warum lädt mein Canvas nicht mit dem Fehler „invalid next-step-id“? {#why-wont-my-canvas-load-with-an-invalid-next-step-id-error}

Dieser Konsolenfehler bedeutet, dass mindestens ein Schritt auf einen fehlenden oder ungültigen nächsten Schritt verweist – zum Beispiel nach einem teilweisen Löschen, Klonen oder Import. Öffnen Sie das Canvas im Editor, verbinden Sie verwaiste Schritte erneut oder entfernen Sie Schritte, die keinen gültigen nachgelagerten Pfad mehr haben. Wenn das Canvas immer noch nicht lädt, wenden Sie sich mit der Canvas-ID und einem Screenshot des Konsolenfehlers an den [Braze-Support]({{site.baseurl}}/braze_support).

### Warum unterscheidet sich ein Canvas-Konversions-Zeitstempel in Currents von meiner Canvas-Analytics? {#why-does-a-canvas-conversion-timestamp-in-currents-differ-from-my-canvas-analytics}

Currents protokolliert Canvas-Konversionen als [`users.canvas.Conversion`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#canvas-conversion-events)-Events. Die Event-`time` ist der Zeitpunkt, an dem das Konversions-Event aufgetreten ist. Das Feld `conversion_behavior` dieses Events beschreibt die Konversionsdefinition (Typ und Fenster). Canvas-Analytics kann Konversionen auch relativ zum Canvas-Eintritt innerhalb des Konversionsfensters zusammenfassen. Beim Abgleich von Exporten vergleichen Sie die Currents-`time` mit dem Konversions-Event-Zeitstempel und Ihren Canvas-Konversionsfenster-Einstellungen.

### Warum ist `canvas_step_name` in Currents null? {#why-is-canvas_step_name-null-in-currents}

Campaign- und Canvas-Namensfelder wie `canvas_step_name` können `null` sein, wenn ein Currents-Event gesendet wird, bevor Braze die Schritt-Metadaten vollständig propagiert hat – zum Beispiel nachdem Sie einen Schritt erstellt oder umbenannt haben. Weitere Informationen finden Sie unter [Warum ist der Campaign-Name oder Canvas-Schrittname `NULL` in meinen Currents-Daten?]({{site.baseurl}}/user_guide/data/distribution/braze_currents/faq#why-is-the-campaign-name-or-canvas-step-name-null-in-my-currents-data).

### Warum wird mein Array in einem User-Update-Schritt nicht aktualisiert? {#why-isnt-my-array-updating-in-a-user-update-step}

Überprüfen Sie das JSON in Ihrem [User-Update]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)-Schritt. Array- und verschachtelte Attribut-Updates benötigen gültige Pfade und Werte für das Attribut, das Sie ändern. Fügen Sie keine Felder hinzu, die der Schritt automatisch bereitstellt, wie z. B. die externe Nutzer-ID. Verwenden Sie den Tab **Preview and test** des Schritts, um den Payload vor dem Start zu bestätigen.

### Kann ich Canvas-Nachrichten an Nutzer:innen ohne `external_id` senden? {#can-i-send-canvas-messages-to-users-without-an-external_id}

Ja, wenn bereits ein Braze-Nutzerprofil existiert. Nutzer:innen ohne `external_id` sind [anonyme Nutzer:innen]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#anonymous-user-profiles) und können mit einer `braze_id` oder einem [Nutzer-Alias]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases) referenziert werden. Erstellen oder aktualisieren Sie das Profil mit dem [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) oder Ihrem SDK vor dem Canvas-Eintritt und verwenden Sie dann den [aktionsbasierten oder API-getriggerten Eintritt]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule). Standard-Canvas-Targeting erfordert weiterhin ein Braze-Nutzerprofil – Sie können keine Canvas-Nachrichten allein an eine E-Mail-Adresse ohne Profil senden.

### Warum ist ein:e Nutzer:in weniger oft in ein Canvas eingetreten, als er/sie das Trigger-Event ausgeführt hat? {#why-did-a-user-enter-a-canvas-fewer-times-than-they-performed-the-trigger-event}

Bei aktionsbasierten und API-getriggerten Canvases dedupliziert Braze Trigger-Events, sodass ein:e Nutzer:in höchstens etwa **einmal pro Sekunde** für dasselbe Canvas eintreten kann. Wenn ein:e Nutzer:in dasselbe Trigger-Event mehrfach innerhalb einer Sekunde ausführt, wird nur ein Eintritt verarbeitet.

Um mehrere Eintritte in derselben Sekunde zu ermöglichen, planen Sie Trigger-Events im Abstand von mindestens 1,1 Sekunden (zum Beispiel, wenn Sie das Event-Timing von Ihrem Server aus steuern). Für ein Campaign-ähnliches Verhalten, das mehrere gleichzeitige Trigger erlaubt, vergleichen Sie Ihren Anwendungsfall mit [Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns) mit entsprechenden Zeitplan- und Wiedereintrittsberechtigungs-Einstellungen.

### Wann werden Nutzer:innen in API-getriggerten Canvases dedupliziert? {#when-are-users-de-duplicated-in-api-triggered-canvases}

Wenn ein:e Nutzer:in ein API-getriggertes Canvas erneut betritt und einen Delay-Schritt erreicht, in dem er/sie bereits aus einem vorherigen Eintritt für eine identische Nachricht eingereiht ist, dedupliziert Braze den/die Nutzer:in, um doppelte Versendungen zu verhindern. Die zweite Canvas-Instanz wird beendet, sodass die Anzahl der Eintritte die Anzahl der Versendungen übersteigen kann.

### Warum geht ein Test-Push an die falsche App, aber Live-Versendungen sehen korrekt aus? {#why-does-a-test-push-go-to-the-wrong-app-but-live-sends-look-correct}

**Test-Push** über ein Nutzerprofil wird an jedes Push-fähige Gerät für dieses Profil zugestellt. Wenn mehrere Apps auf einem Gerät installiert sind, stellt das Betriebssystem die Testbenachrichtigung typischerweise an die erste verfügbare App zu, die möglicherweise nicht die App ist, die Sie validieren möchten.

Um app-spezifisches Targeting zu bestätigen, senden Sie eine Live- oder Testnachricht über eine Campaign oder ein Canvas mit einer engen Zielgruppe (zum Beispiel nach `external_id` filtern), anstatt sich allein auf den **Test-Push** des Profils zu verlassen.

Aktivieren Sie für **Canvas**-Nachrichtenschritte mit mehreren Apps die Option **Validate audience at message send** im Nachrichtenschritt, damit Segment- und Filterprüfungen zum Sendezeitpunkt ausgeführt werden. Weitere Informationen finden Sie unter [Nachrichtenschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step).

Allgemeine Informationen zum Test-Push-Verhalten finden Sie unter [Testnachrichten senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) und [Push-FAQ]({{site.baseurl}}/user_guide/channels/push/faqs).

### Wie debugge ich Push Stories auf iOS und Android? {#how-do-i-debug-push-stories-on-ios-and-android}

Beginnen Sie mit [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories) für die Einrichtung und kreativen Anforderungen. Informationen zur Implementierung und zum Umgang mit Rich-Benachrichtigungen finden Sie unter [Rich-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/rich) und [Push Stories]({{site.baseurl}}/developer_guide/push_notifications/push_stories) im Entwicklerhandbuch.

### Wer erhält die E-Mail „Canvas Messages Delayed 24+ Hours“? {#who-receives-the-canvas-messages-delayed-24-hours-email}

Braze sendet diese Benachrichtigung, wenn Canvas-Nachrichten durch Rate-Limiting 24 Stunden oder länger verzögert werden. Die E-Mail geht an Dashboard-Nutzer:innen, die zuvor Änderungen am betroffenen Canvas vorgenommen haben (basierend auf den Canvas-Änderungsprotokollen). Wenn Braze diese Empfänger:innen nicht ermitteln kann, geht die E-Mail an die **Unternehmensadmins** des Workspace.

### Wann hört ein:e Nutzer:in auf, Nachrichten nach einem Ausnahme-Event zu erhalten? {#when-does-a-user-stop-receiving-messages-after-an-exception-event}

Braze erfasst den Exit, sobald das Ausnahme-Event eintritt, aber Nutzer:innen können innerhalb eines Schritts verbleiben, bis Timer ablaufen – am deutlichsten sichtbar bei Delay-Schritten. Das Verhalten unterscheidet sich auch zwischen geplanten Schritten und Event-getriggerten Schritten. Zeitpläne, Beispiele und Analytics-Nuancen finden Sie unter [Exit-Kriterien]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria).

### Warum zeigt mein Aktionspfade-Schritt einen Fehler an, wenn ich eine Link-Alias-Interaktion auswähle? {#why-does-my-action-paths-step-show-an-error-when-i-select-a-link-alias-interaction}

Aktionsgruppen, die E-Mail-Interaktivitäts-Trigger verwenden (zum Beispiel **Alias in E-Mail geklickt** oder **Alias in einer Campaign oder einem Canvas-Schritt geklickt**), benötigen einen Nachrichtenschritt, der die Nachricht mit diesem Link bereits gesendet hat. Fügen Sie Schritte hinzu oder ordnen Sie sie neu an, damit die E-Mail vor dem Aktionspfade-Schritt gesendet wird, der den Klick auswertet, oder wählen Sie eine Interaktion, die zu einer Nachricht passt, die der/die Nutzer:in bereits in diesem Canvas erhalten hat. Die vollständige Liste der Interaktions-Trigger finden Sie unter [Aktionsbasierte Zustellung]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery).

### Wie wirken sich historische Zeitstempel angepasster Events auf aktionsbasierte Canvases und Campaigns aus? {#how-do-historical-custom-event-timestamps-affect-action-based-canvases-and-campaigns}

Braze wertet aktionsbasierte Journeys aus, wenn qualifizierende Events aufgenommen werden und der/die Nutzer:in Ihre Zielgruppenregeln erfüllt. Wenn ein Event außerhalb des Zeitfensters, in dem Ihr Canvas oder Ihre Campaign aktiv war, oder bevor der/die Nutzer:in Ihrer Zielgruppe entsprach, auf dem Profil eingeht, erfolgt der Eintritt oder nachgelagerte Versendungen möglicherweise nicht wie erwartet. Vergleichen Sie Event-Zeitstempel mit den Go-Live-Zeiten und der Segmentzugehörigkeit mithilfe des Nutzer-Profil-Aktivitätsprotokolls und der Fehlerbehebungsschritte unter [Fehlerbehebung bei angepassten Events]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#troubleshooting-custom-events). Wenn das Verhalten immer noch nicht den Erwartungen entspricht, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/braze_support).