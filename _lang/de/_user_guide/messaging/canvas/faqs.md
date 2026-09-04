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

### Wie viele Schritte kann ich in einen Canvas einfügen? {#how-many-steps-i-can-include-in-a-canvas}

Sie können bis zu 200 Schritte in einen Canvas einfügen.

### Gibt es Größenbeschränkungen für Canvas-Entry-Eigenschaften? {#are-there-size-limits-for-canvas-entry-properties}

Ja. Das [Canvas-Kontextobjekt]({{site.baseurl}}/api/objects_filters/context_object) (Canvas-Entry-Eigenschaften) hat eine maximale Größe von 50&nbsp;KB. Halten Sie Payloads innerhalb dieses Limits so klein wie möglich. Informationen zur Funktionsweise von Entry- und Event-Eigenschaften in Canvas finden Sie unter [Kontext- und Event-Eigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties).

### Warum sehe ich den Fehler „Too many Canvas branches“? {#why-do-i-see-a-too-many-canvas-branches-error}

Dieser Fehler erscheint, wenn die Kombination aus Schritt-Verzweigungen und der Größe der Einstiegs-Zielgruppe zu Performance-Problemen im Cluster führen kann, die das Senden von Nachrichten verhindern. Lösungsschritte – einschließlich der Verwendung von [Zielgruppenpfaden]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths), der Reduzierung von Verzweigungen oder Zielgruppengrößen und der Neuerstellung im Canvas Flow – finden Sie unter [Fehler „Too many Canvas branches“]({{site.baseurl}}/user_guide/messaging/canvas/troubleshooting#too-many-canvas-branches-error).

### Kann ich „Optimize with BrazeAI<sup>TM</sup>“ mit erneuter Berechtigung in einem Canvas verwenden? {#can-i-use-optimize-with-brazeai-with-re-eligibility-in-a-canvas}

Ja. Canvases können [Optimize with BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#optimize-canvas-variants-with-brazeai) verwenden, wenn die erneute Berechtigung aktiviert ist. Braze kann bei einem erneuten Eintritt nicht dieselbe Variante garantieren, da sich die Zuordnung im Laufe der Zeit verschiebt. Campaigns erfordern ein Fenster für erneute Berechtigung von mindestens 24 Stunden, wenn **Optimize with BrazeAI<sup>TM</sup>** aktiviert ist.

### Was ist der Unterschied zwischen einer Komponente und einem Schritt? {#whats-the-difference-between-a-component-and-a-step}

Eine [Komponente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about) ist ein einzelner Bestandteil Ihres Canvas, mit dem Sie die Effektivität Ihres Canvas bestimmen können. Komponenten können Aktionen wie das Aufteilen Ihrer User Journey, das Hinzufügen einer Verzögerung und sogar das Testen mehrerer Canvas-Pfade umfassen. Ein Schritt in Canvas bezieht sich auf die personalisierte User Journey in Ihren Canvas-Branches. Im Wesentlichen besteht Ihr Canvas aus einzelnen Komponenten, die Schritte für Ihre User Journey erstellen.

### Kann ich einen Canvas mit nicht verbundenen Schritten starten? {#can-i-launch-a-canvas-with-disconnected-steps}

Ja. Sie können Canvases auch nach dem Start mit nicht verbundenen Schritten speichern.

### Wohin gelangen Nutzer:innen, wenn sie einen nicht verbundenen Schritt erreicht haben? {#where-do-users-go-when-theyve-reached-a-disconnected-step}

Wenn sich ein:e Nutzer:in in einem nicht verbundenen Schritt Ihres Canvas-Workflows befindet, rückt er/sie zum nachfolgenden Schritt vor, sofern einer vorhanden ist. Die Einstellung des Schritts bestimmt, wie der/die Nutzer:in fortschreiten soll. Dies soll es ermöglichen, Änderungen an Schritten vorzunehmen, ohne sie direkt mit dem restlichen Canvas verbinden zu müssen. Außerdem bietet es Spielraum für Tests, bevor Sie sofort live gehen – im Grunde können Sie so einen Entwurf speichern.

Wir empfehlen, die Analytics-Ansicht auf wartende Nutzer:innen in einem Canvas-Schritt zu prüfen, bevor Sie einen Schritt trennen.

### Was passiert, wenn Zielgruppe und Sendezeit für einen Canvas mit einer Variante, aber mehreren Branches identisch sind? {#what-happens-if-the-audience-and-send-time-are-identical-for-a-canvas-that-has-one-variant-but-multiple-branches}

Wir stellen einen Job für jeden Schritt in die Warteschlange – sie werden ungefähr zur gleichen Zeit ausgeführt, und einer davon „gewinnt“. In der Praxis kann dies relativ gleichmäßig verteilt sein, aber es gibt wahrscheinlich zumindest eine leichte Tendenz zugunsten des Schritts, der zuerst erstellt wurde.

Außerdem können wir keine Garantien dafür geben, wie diese Verteilung genau aussieht. Wenn Sie eine gleichmäßige Aufteilung wünschen, fügen Sie einen Filter für [zufällige Bucket-Nummern]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) hinzu.

### Wie werden Canvas-Zielgruppen ausgewertet? {#how-are-canvas-audiences-evaluated}

Standardmäßig werden Filter und Segmente für vollständige Schritte im Canvas zum Sendezeitpunkt geprüft. Der Decision-Split-Schritt führt eine Auswertung direkt nach dem Empfang eines vorherigen Schritts durch (oder vor einer Verzögerung).

### Wann wird ein Ausnahme-Event ausgelöst? {#when-does-an-exception-event-trigger}

Ausnahme-Events werden nur ausgelöst, während der/die Nutzer:in darauf wartet, die zugehörige Canvas-Komponente zu empfangen. Wenn ein:e Nutzer:in eine Aktion im Voraus ausführt, wird das Ausnahme-Event nicht ausgelöst. Wenn Sie Nutzer:innen ausschließen möchten, die ein bestimmtes Event bereits ausgeführt haben, verwenden Sie stattdessen [Filter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).

### Wie wirkt sich die Bearbeitung eines Canvas auf Nutzer:innen aus, die sich bereits im Canvas befinden? {#how-does-editing-a-canvas-affect-users-already-in-the-canvas}

Wenn Sie einige Schritte eines mehrstufigen Canvas bearbeiten, erhalten Nutzer:innen, die bereits in der Zielgruppe waren, aber die Schritte noch nicht erhalten haben, die aktualisierte Version der Nachricht. Beachten Sie, dass dies nur geschieht, wenn sie noch nicht für den Schritt ausgewertet wurden.

Weitere Informationen darüber, was Sie nach dem Start bearbeiten können, finden Sie unter [Canvas nach dem Start ändern]({{site.baseurl}}/post-launch_edits).

### Was passiert, wenn Sie einen Canvas stoppen? {#what-happens-when-you-stop-a-canvas}

Wenn Sie einen Canvas stoppen, gilt Folgendes:

- Nutzer:innen werden daran gehindert, den Canvas zu betreten.
- Es werden keine weiteren Nachrichten gesendet, unabhängig davon, wo sich ein:e Nutzer:in im Flow befindet.
- **Ausnahme:** Canvases mit E-Mails werden nicht sofort gestoppt. Nachdem die Sendeanfragen an SendGrid übergeben wurden, können wir nicht verhindern, dass sie an den/die Nutzer:in zugestellt werden.

### Sollte ich einen Canvas oder separate Canvases pro Nutzer-Lebenszyklus erstellen? {#should-i-build-one-canvas-or-separate-canvases-per-user-lifecycle}

Je nachdem, was Sie mit Ihrem Canvas erreichen möchten, benötigen Sie möglicherweise unterschiedliche Ansätze beim Aufbau Ihrer User Journey. Die Flexibilität von Canvas ermöglicht es Ihnen, User Journeys für jede Phase des Nutzer-Lebenszyklus abzubilden. Sehen Sie sich unsere [Braze-Canvas-Templates]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates) für mehrere Beispiele optimierter Ansätze zur Erstellung effektiver User Journeys an.

## Nachrichten und Zustellung {#messages-and-delivery}

### Wann werden In-App-Nachrichten in Canvas gesendet? {#when-are-in-app-messages-in-canvas-sent}

In-App-Nachrichten werden beim nächsten Sitzungsstart gesendet. Das bedeutet: Wenn Nutzer:innen den Canvas-Schritt betreten, bevor der Canvas gestoppt wird, erhalten sie die In-App-Nachricht trotzdem beim nächsten Sitzungsstart – sofern die In-App-Nachricht noch nicht abgelaufen ist.

Es ist möglich, dass Nutzer:innen eine Sitzung starten, bevor der Canvas gestoppt wird, die In-App-Nachricht aber nicht sofort angezeigt wird. Dies kann vorkommen, wenn die In-App-Nachricht durch ein angepasstes Event getriggert wird oder verzögert ist. Das bedeutet, dass Nutzer:innen eine Impression für die In-App-Nachricht protokollieren und die In-App-Nachricht „empfangen“ können, nachdem der Canvas gestoppt wurde. Allerdings müssten die Nutzer:innen die Sitzung gestartet haben, bevor der Canvas gestoppt wurde, aber **nachdem** sie den Canvas-Schritt erhalten haben.

{% alert note %}
Das Stoppen eines Canvas führt nicht dazu, dass Nutzer:innen, die auf den Empfang von Nachrichten warten, die User-Journey verlassen. Wenn Sie den Canvas erneut aktivieren und Nutzer:innen noch auf die Nachricht warten, werden sie diese erhalten (es sei denn, der Zeitpunkt, zu dem die Nachricht hätte gesendet werden sollen, ist bereits verstrichen – dann erhalten sie sie nicht).
{% endalert %}

### Warum kann ein Canvas null Sends anzeigen, obwohl Impressionen protokolliert werden? {#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged}

Wenn _Messages sent_ für einen Canvas mit einem In-App-Nachricht-Schritt immer null ist, liegt das daran, dass die Zustellung von In-App-Nachrichten anders funktioniert als bei anderen Messaging-Kanälen.

In-App-Nachrichten werden vom SDK „abgerufen“ (Pull) und nicht von Braze „gesendet“ (Push). In-App-Nachrichten für berechtigte Nutzer:innen werden beim Sitzungsstart automatisch zugestellt und „warten“ auf das Trigger-Event, bevor sie angezeigt werden. Da berechtigte Nutzer:innen die Nachricht erhalten, wenn sie eine Sitzung starten, meldet Braze dies nicht als Send-Event. Wenn Nutzer:innen das Trigger-Event ausführen, wird die Nachricht angezeigt und Braze protokolliert eine Impression und markiert den Canvas-Schritt (oder die Campaign) als empfangen im Kundenprofil. Folglich ist die Gesamtzahl der _Sends_ für In-App-Nachrichten null.

### Warum haben Nutzer:innen meine In-App-Nachricht nach einer langen Verzögerung oder Verzweigung nicht erhalten? {#why-didnt-users-receive-my-in-app-message-after-a-long-delay-or-branch}

Nachdem vorgelagerte [Delay]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step)-Schritte und Zielgruppenprüfungen abgeschlossen sind, werden Nutzer:innen erst für eine In-App-Nachricht berechtigt, wenn sie den Nachrichten-Schritt erreichen. Wenn die Nachricht an einem Kalenderdatum abläuft oder ein kurzes Fenster **Dauer nach Verfügbarkeit des Schritts** hat, können Nutzer:innen auf langsameren Pfaden nach dem Ablauf ankommen und die Nachricht nie sehen. Passen Sie den Ablauf an Ihre längsten realistischen Pfadverzögerungen an. Weitere Informationen und Beispiele finden Sie unter [Ablauf von In-App-Nachrichten]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas#in-app-message-expiration).

### Warum sehe ich die Meldung „Canvas Entry Properties may not be used in In-App Messages.“? {#why-do-i-see-canvas-entry-properties-may-not-be-used-in-in-app-messages}

Diese Meldung erscheint, wenn Personalisierungen auf Felder verweisen, die In-App-Nachrichten in Canvas nicht auflösen können. Verwenden Sie das `context`-Objekt, wie unter [Kontext- und Event-Eigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) und [Nachrichten-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) beschrieben. Der veraltete Liquid-Namespace `canvas_entry_properties` unterliegt anderen Einschränkungen als `context`. Wenn Sie Werte über mehrere Schritte hinweg beibehalten müssen, besprechen Sie [persistente Eigenschaften im originalen Canvas-Editor]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties) mit Ihrem Braze-Team. Gespeicherte Werte werden gelöscht, wenn Nutzer:innen den Canvas verlassen, bevor das Gerät die In-App-Payload heruntergeladen hat.

### Wo finde ich Button-Klicks für Drag-and-Drop-In-App-Nachrichten in Canvas? {#where-can-i-find-button-clicks-for-drag-and-drop-in-app-messages-in-canvas}

Metriken auf Button-Ebene für Drag-and-Drop-In-App-Nachrichten erscheinen auf der Analytics-Karte des **Nachrichten**-Schritts in den **Canvas-Details**, nicht nur in der übergeordneten Canvas-Zusammenfassung. Öffnen Sie den Canvas, wählen Sie den Nachrichten-Schritt aus und überprüfen Sie dort das In-App-Engagement. Informationen zu Reporting-Konzepten finden Sie unter [Messen und Testen mit Canvas-Analytics]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics).

### Kann ich unterschiedliche Sendezeiten für jede Variante im selben Canvas-Nachrichten-Schritt oder multivariaten Versand planen? {#can-i-schedule-different-send-times-for-each-variant-in-the-same-canvas-message-step-or-multivariate-send}

Nein. Varianten in derselben multivariaten Konfiguration oder demselben Nachrichten-Schritt teilen sich einen Zustellungsplan. Sie können nicht eine Variante um 18 Uhr und eine andere um 19 Uhr für denselben geplanten Versand zuweisen.

Um Versendungen zeitlich zu staffeln oder unterschiedliche Zeiten pro Pfad zu verwenden, probieren Sie die folgenden Methoden:

- Verwenden Sie separate Nachrichten-Schritte mit Delay-Schritten dazwischen, damit jede Nachricht einen eigenen Zeitplan hat.
- Verwenden Sie Verzweigungen oder einen [Experimentpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step)-Schritt, damit Nutzer:innen Pfaden mit unterschiedlichem Timing folgen.
- Verwenden Sie separate Campaigns, wenn der Anwendungsfall nicht innerhalb eines Canvas bleiben muss.

Informationen zu multivariaten und A/B-Konzepten in Campaigns finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing).

### Was passiert, wenn für Nutzer:innen bei einem Canvas-Nachrichten-Schritt ein globales Frequency-Capping greift? {#what-happens-if-a-user-is-global-frequency-capped-at-a-canvas-message-step}

Die Nutzer:innen erhalten den Versand für den begrenzten Kanal nicht, aber Nachrichten-Schritte lassen Nutzer:innen trotzdem fortschreiten, wenn eine Nachricht aufgrund des globalen Frequency-Cappings nicht gesendet wird. Informationen zu den einzelnen Fortschrittsfällen finden Sie unter [Wie Nutzer:innen fortschreiten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance). Globales Frequency-Capping allein führt nicht dazu, dass Nutzer:innen einen Canvas verlassen; dieses Verhalten ist unabhängig von den **Zustellungsvalidierungen** eines Nachrichten-Schritts. Weitere Details finden Sie unter [Rate-Limiting und Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping).

### Warum sind die Sends niedriger als die geschätzte Zielgruppengröße? {#why-are-sends-lower-than-the-estimated-audience-size}

Sends können aus vielen der gleichen Gründe niedriger sein als die **Geschätzte Zielgruppe** wie bei [Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/faq#why-are-sends-lower-than-the-estimated-audience-size), einschließlich Frequency-Caps, strikter Geräte- oder Browser-Filter, Wiederbetretbarkeits-Fenster, Rate-Limiting und kanalbezogener Ausschlüsse (z. B. Push-Erreichbarkeit oder E-Mail-Abo- und Zustellbarkeitsprüfungen).

Canvas-spezifische Faktoren gelten ebenfalls:

- **Aktionsbasierter oder API-getriggerter Eintritt:** Nutzer:innen treten nur ein (und erhalten Schritte), nachdem sie das Eintrittsverhalten ausgeführt haben. Die tatsächlichen Sends liegen daher hinter der anfänglichen Schätzung zurück, bis diese Aktionen erfolgen.
- **Zielgruppenpfade:** Nutzer:innen werden zum Pfad mit der höchsten Priorität geleitet, für den sie sich qualifizieren. Nachgelagerte Pfade können daher weniger Nutzer:innen erhalten, als eine einfache Segmentzählung vermuten lässt.
- **Zielgruppen- und Sendezeitprüfungen:** Vollständige Schritte bewerten Filter zum Sendezeitpunkt erneut, sofern Sie nichts anderes konfigurieren. Nutzer:innen, die sich bei der Erstellung des Canvas qualifiziert haben, können vor dem Versand einer Nachricht ausscheiden.
- **Kontrollgruppen:** Globale oder Canvas-Kontrollgruppen halten einen Anteil der Eintretenden vom Messaging zurück.
- **Ruhezeiten und Verzögerungen:** Nachrichten können zurückgehalten oder umgeplant werden, wodurch Sends aus dem Berichtszeitraum verschoben werden, den Sie gerade betrachten.
- **Maximale Eintritts- oder Zielgruppenlimits:** Eintritts- oder Sendelimits stoppen weitere Nutzer:innen, selbst wenn das zugrunde liegende Segment größer ist.
- **Berichtszeitraum:** Der Analytics-Bereich umfasst möglicherweise nicht jeden Send, den Sie mit der Schätzung vergleichen.

### Warum stimmen die geschätzte Zielgruppe und die Canvas-Nutzerzahlen nicht überein? {#why-dont-estimated-audience-and-canvas-user-counts-match}

Die **Geschätzte Zielgruppe** spiegelt wider, wer zum Zeitpunkt der Schätzung Ihrem Segment und Ihren Eintrittsfiltern entspricht. Nach diesem Zeitpunkt können verzögerte oder aktionsbasierte Eintritte, Wiederbetretbarkeit, API-Trigger oder Pfadverteilung dazu führen, dass mehr Profile die Journey durchlaufen als im Snapshot. Nutzer:innen können auch ausscheiden, wenn Sendezeit-Filter fehlschlagen, was die tatsächlichen Eintritte oder Sends senkt. Vergleichen Sie Timing, Limits und Bewertungseinstellungen zusammen mit [Warum sind die Sends niedriger als die geschätzte Zielgruppengröße?](#why-are-sends-lower-than-the-estimated-audience-size).

### Warum ist _Unique Recipients_ höher als die Anzahl der angezielten Nutzer:innen? {#why-is-_unique-recipients_-higher-than-the-number-of-users-i-targeted}

_Unique Recipients_ kann höher sein als die erwartete Zielgruppe, da Braze **eindeutige tägliche Empfänger:innen** für das Canvas- und Campaign-Reporting erfasst. Dies ermöglicht eine genaue Konversions-Attribution jedes Mal, wenn Nutzer:innen eine Nachricht in der Journey erhalten.

Wenn Nutzer:innen beispielsweise am Montag und am Freitag einen Canvas-Schritt erhalten und nach jedem Versand konvertieren, kann Braze zwei Empfänger:innen-Zeilen und zwei zugehörige Konversionen zählen. Bei wiederkehrenden Eintritten oder Wiederbetretbarkeit kann dieselbe kleine Gruppe von Profilen über mehrere Tage hinweg mehrere _Unique Recipients_ erzeugen.

### Warum weist mein Canvas niedrigere Versandraten auf? {#why-is-my-canvas-experiencing-lower-send-rates}

Wenn Sie feststellen, dass Ihr täglich geplanter Canvas im Laufe der Zeit an weniger Nutzer:innen sendet, überprüfen Sie Folgendes:

- **Prüfen Sie, ob die Wiederbetretbarkeit aktiviert ist:** Ohne Wiederbetretbarkeit lässt Braze jede:n Nutzer:in nur einmal in den Canvas eintreten. Bei täglich geplanten Canvases sind nur Nutzer:innen berechtigt, die der Zielgruppe entsprechen und den Canvas noch nicht betreten haben. Da immer mehr Nutzer:innen eintreten, hat jeder spätere Eintritt weniger berechtigte Nutzer:innen, sodass das Eintrittsvolumen sinkt.
- **Prüfen Sie, ob die Zielgruppe eine feste Mitgliedschaft hat:** Zielgruppen, die aus einer festen Nutzerliste erstellt wurden (z. B. ein [CSV-Import]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import), der als Segmentfilter verwendet wird), gewinnen nicht automatisch neue Mitglieder. Ohne neue Eintretende kann das Eintrittsvolumen nicht wieder steigen, sobald Nutzer:innen den Canvas betreten haben.

Informationen zu [Rate-Limits für die Zustellgeschwindigkeit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) und anderen Faktoren, die Sends für ein einzelnes Vorkommen senken, finden Sie unter [Warum sind die Sends niedriger als die geschätzte Zielgruppengröße?](#why-are-sends-lower-than-the-estimated-audience-size).

### Warum zeigt ein kleines Kontrollgruppen-Segment Veränderungen in der historischen Mitgliedschaft? {#why-does-a-small-control-group-segment-show-changes-in-historical-membership}

Diagramme zur historischen Mitgliedschaft verwenden geschätzte Stichproben, sodass kleine Segmente – einschließlich [globaler Kontrollgruppen]({{site.baseurl}}/user_guide/audience/global_control_group)-Segmente – tägliche Schwankungen zeigen können, selbst wenn die zugrunde liegende Zielgruppe stabil ist. Informationen zur Funktionsweise der Schätzungen und warum Diagramme schwanken können, finden Sie unter [Historische Segmentmitgliedschaftsgröße anzeigen]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size#viewing-historical-segment-membership-size).

## Analytics und Konversionen {#analytics-and-conversions}

### Wie ordnet das Conversions-Dashboard Canvas-Konversionen zu? {#how-does-the-conversions-dashboard-attribute-canvas-conversions}

Das [Conversions-Dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/conversions) ordnet Canvas-Konversionen basierend auf der von Ihnen gewählten [Attributionsmethode]({{site.baseurl}}/user_guide/analytics/dashboards/conversions#attribution-methods) zu (z. B. **Upon Receipt**, **Upon Send**, **Upon Open** oder **Upon Click**). Damit ein:e Nutzer:in im Bericht erscheint, muss er/sie den Canvas oder die Campaign betreten, die ausgewählte Attributionsmethode auslösen und das Konversions-Event innerhalb Ihrer Berichtseinstellungen ausführen.

Informationen zu Konversionsregeln auf Schritt- und Variantenebene in der Canvas-Analyse finden Sie unter [Wie werden Nutzer-Konversionen in einem Canvas getrackt?](#how-are-user-conversions-tracked-in-a-canvas).

### Wie werden Nutzer-Konversionen in einem Canvas getrackt? {#how-are-user-conversions-tracked-in-a-canvas}

Ein:e Nutzer:in kann pro Canvas-Eintritt nur einmal konvertieren. Konversionen werden der zuletzt empfangenen Nachricht für diesen Eintritt zugeordnet. Der Zusammenfassungsblock am Anfang eines Canvas spiegelt alle Konversionen wider, die von Nutzer:innen innerhalb dieses Pfades durchgeführt wurden, unabhängig davon, ob sie eine Nachricht erhalten haben. Jeder nachfolgende Schritt zeigt nur Konversionen an, die stattfanden, während dieser Schritt der zuletzt empfangene war.

{% alert note %}
Wenn ein:e Nutzer:in erneut in einen Canvas eintritt, werden Konversions-Events nur für den letzten Eintritt getrackt. Konversions-Events werden nicht für vorherige Eintritte protokolliert, selbst wenn das Konversions-Event nachträglich ergänzt wird.
{% endalert %}

{% details Beispiele anzeigen %}

**Beispiel 1**

Es gibt einen Canvas-Pfad mit 10 Push-Benachrichtigungen und das Konversions-Event ist „Sitzungsstart“ („App öffnen“):

- Nutzer:in A öffnet die App nach dem Eintritt, aber bevor die erste Nachricht empfangen wird.
- Nutzer:in B öffnet die App nach jeder Push-Benachrichtigung.

**Ergebnis:** Die Zusammenfassung zeigt zwei Konversionen an, während die einzelnen Schritte eine Konversion beim ersten Schritt und null bei allen nachfolgenden Schritten anzeigen.

{% alert note %}
Wenn Ruhezeiten aktiv sind, wenn das Konversions-Event stattfindet, gelten dieselben Regeln.
{% endalert %}

**Beispiel 2**

Es gibt einen Canvas mit einem einzigen Schritt und aktivierten Ruhezeiten:

1. Nutzer:in tritt in den Canvas ein.
2. Der erste Schritt hat keine Verzögerung, liegt aber innerhalb der festgelegten Ruhezeiten, sodass die Nachricht unterdrückt wird.
3. Nutzer:in führt das Konversions-Event aus.

**Ergebnis:** Der/die Nutzer:in wird in der gesamten Canvas-Variante als konvertiert gezählt, aber nicht im Schritt, da er/sie den Schritt nicht erhalten hat.

{% enddetails %}

### Was ist der Unterschied zwischen den verschiedenen Konversionsraten-Typen? {#whats-the-difference-between-the-different-conversion-rate-types}

- Gesamte Canvas-Konversionen spiegeln wider, wie viele eindeutige Nutzer:innen ein Konversions-Event abgeschlossen haben, nicht wie viele Konversionen jede:r einzelne durchgeführt hat.
- Die Varianten-Konversionsrate oder der Zusammenfassungsblock am Anfang eines Canvas spiegelt alle Konversionen wider, die von Nutzer:innen innerhalb dieses Pfades durchgeführt wurden, unabhängig davon, ob sie eine Nachricht erhalten haben, als aggregierte Gesamtzahl.
- Die Schritt-Konversionsrate gibt an, wie viele Personen diesen Nachrichtenschritt erhalten und eines der definierten Konversions-Events abgeschlossen haben.

### Warum ist die Konversionsrate meines Canvas-Schritts nicht gleich der gesamten Konversionsrate meiner Canvas-Variante? {#why-is-my-canvas-step-conversion-rate-not-equal-to-my-canvas-variant-total-conversion-rate}

Es ist üblich, dass die Konversionsgesamtzahl einer Canvas-Variante größer ist als die Summe der Schritt-Konversionen. Dies geschieht, weil ein:e Nutzer:in ein Konversions-Event für eine Variante ausführen kann, sobald er/sie die Variante betritt. Dasselbe Konversions-Event zählt jedoch nicht für einen Canvas-Schritt. Jede:r Nutzer:in, der/die in den Canvas eintritt und das Konversions-Event ausführt, bevor er/sie den ersten Canvas-Schritt erhält, wird in die Varianten-Konversionsgesamtzahl eingerechnet, aber nicht in die Schritt-Gesamtzahl. Gleiches gilt für Nutzer:innen, die in den Canvas eintreten, aber den Canvas verlassen, bevor sie einen Schritt erhalten.

Beachten Sie, dass es auch möglich ist, dass ein:e Nutzer:in eine Variante betritt, von keinem Schritt eine Nachricht erhält und dann konvertiert. In diesem Fall wird keine Konversion auf Schrittebene protokolliert. Da der/die Nutzer:in jedoch technisch gesehen konvertiert hat, wird eine Konversion auf Canvas-Ebene protokolliert.

### Wie kann ich bestätigen, ob meine Nutzer:innen einen API-getriggerten Canvas erhalten haben? {#how-can-i-confirm-if-my-users-received-an-api-triggered-canvas}

Sie können [ein Segment erstellen]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment), das einen Canvas-Filter verwendet, um zu bestätigen, ob Nutzer:innen den Canvas betreten oder einen bestimmten Canvas-Schritt erhalten haben. Verwenden Sie z. B. einen Canvas-Eintrittsfilter, wenn Sie bestätigen möchten, dass Nutzer:innen den API-getriggerten Canvas betreten haben, oder einen Filter für empfangene Schritte, wenn Sie bestätigen möchten, dass sie eine Nachricht aus dem Canvas erhalten haben. Verwenden Sie dann den [`/users/export/segment`-Endpunkt]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment), um die Nutzer:innen in diesem Segment zu exportieren.

### Kann ich einen Canvas löschen? {#can-i-delete-a-canvas}

Nein, aber Sie können [einen Canvas archivieren]({{site.baseurl}}/user_guide/messaging/governance/archiving).

### Wie setze ich einen archivierten Canvas oder eine archivierte Campaign fort? {#how-do-i-resume-an-archived-canvas-or-campaign}

Archivierte Nachrichten werden nicht gesendet, bis Sie sie in einen bearbeitbaren Zustand zurückversetzen. [Dearchivieren]({{site.baseurl}}/user_guide/messaging/governance/archiving#unarchiving) Sie die Campaign oder den Canvas, legen Sie den Eintrittszeitplan oder die Sendezeit auf ein zukünftiges Zeitfenster fest (oder duplizieren Sie die Journey, wenn Sie eine saubere Kopie benötigen), und wählen Sie dann **Fortsetzen** oder starten Sie wie gewünscht. Siehe [Campaigns und Canvases archivieren]({{site.baseurl}}/user_guide/messaging/governance/archiving).

### Warum wird mein Canvas nicht gespeichert, wenn kein Fehler angezeigt wird? {#why-doesnt-my-canvas-save-when-no-error-appears}

Leere **angepasstes Attribut**-Filter in Zielgruppen- oder Schritt-Filtern können das Speichern blockieren, ohne eine detaillierte Validierungsmeldung auszugeben. Öffnen Sie jede Filterkarte, entfernen Sie unvollständige Regeln für angepasste Attribute oder geben Sie sowohl den Attributnamen als auch den Wert ein, und wählen Sie dann erneut **Speichern**.

### Warum ist ein Tag von meinem Canvas oder meiner Campaign verschwunden? {#why-did-a-tag-disappear-from-my-canvas-or-campaign}

Wenn ein [Tag]({{site.baseurl}}/user_guide/messaging/governance/tags) aus Ihrem Workspace gelöscht wird, entfernt Braze es aus jeder Campaign und jedem Canvas, die darauf verwiesen haben. Diese Bereinigung erzeugt nicht immer einen eigenen Eintrag im Canvas-Änderungsprotokoll.

### Wie kann ich die Analytics für jede meiner Canvas-Komponenten anzeigen? {#how-can-i-view-analytics-for-each-of-my-canvas-components}

Um die Analytics einer Canvas-Komponente anzuzeigen, gehen Sie zu Ihrem Canvas und scrollen Sie auf der Seite **Canvas-Details** nach unten. Dort können Sie die Analytics jeder Komponente einsehen. Weitere Details finden Sie unter [Canvas-Analytics]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics).

### Wann ist das Engagement eines Canvas-Schritts auf einem Kundenprofil sichtbar? {#when-is-engagement-from-a-canvas-step-visible-on-a-user-profile}

Filter wie `Received Message from Canvas Step` werden aktualisiert, nachdem Braze das entsprechende Sende-, Empfangs- oder Engagement-Event für diesen Schritt protokolliert hat. In-App-Nachrichten können Impressionen separat von sendebezogenen Metriken protokollieren. Siehe [Warum kann ein Canvas null Sendungen anzeigen, obwohl Impressionen protokolliert werden?](#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged). Dieselben Events erscheinen in den Schritt-Metriken unter **Canvas-Details**.

### Was ist genauer, wenn es um die Anzahl eindeutiger Nutzer:innen geht – die Canvas-Analytics oder der Segmenter? {#when-looking-at-the-number-of-unique-users-is-canvas-analytics-or-the-segmenter-more-accurate}

Der Segmenter liefert eine genauere Statistik für eindeutige Nutzerdaten als die Canvas- oder Campaign-Statistiken. Das liegt daran, dass Canvas- und Campaign-Statistiken Zahlen sind, die Braze bei jedem Ereignis inkrementiert – es gibt also Variablen, die dazu führen können, dass diese Zahl von der des Segmenters abweicht. Zum Beispiel können Nutzer:innen für einen Canvas oder eine Campaign mehr als einmal konvertieren.

### Warum weicht die Anzahl der Nutzer:innen, die in einen Canvas eintreten, von der erwarteten Anzahl ab? {#why-does-the-number-of-users-entering-a-canvas-not-match-the-expected-number}

Die Anzahl der Nutzer:innen, die in einen Canvas eintreten, kann von Ihrer erwarteten Zahl abweichen, da Zielgruppen und Trigger unterschiedlich ausgewertet werden. In Braze wird die Zielgruppe vor dem Trigger ausgewertet (es sei denn, Sie verwenden einen [Änderung des angepassten Attributwerts]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)-Trigger). Dies führt dazu, dass Nutzer:innen aus dem Canvas herausfallen, wenn sie nicht Teil Ihrer ausgewählten Zielgruppe sind, bevor Trigger-Aktionen ausgewertet werden.

### Was passiert mit anonymen Nutzer:innen während ihrer Canvas-Journey? {#what-happens-to-anonymous-users-during-their-canvas-journey}

Anonyme Nutzer:innen können zwar in Canvases eintreten und diese verlassen, aber ihre Aktionen werden keinem bestimmten Kundenprofil zugeordnet, bis sie identifiziert werden, sodass ihre Interaktionen möglicherweise nicht vollständig in Ihren Analytics getrackt werden. Sie können den [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder) verwenden, um einen Bericht über diese Metriken zu erstellen.

{% alert tip %}
Für weitere Unterstützung bei der Canvas-Fehlerbehebung wenden Sie sich bitte innerhalb von 30 Tagen nach Auftreten Ihres Problems an den Braze-Support, da uns nur die Diagnoseprotokolle der letzten 30 Tage zur Verfügung stehen.
{% endalert %}

### Kann ich Nutzer:innen, die sich derzeit in einer Canvas-Journey befinden, von einer Campaign oder einem Segment ausschließen? {#can-i-exclude-users-who-are-currently-in-a-canvas-journey-from-a-campaign-or-segment}

Verwenden Sie [Segmentierungsfilter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) wie `Entered Canvas Variation`, `In Canvas Control Group` oder `Received Message from Canvas Step`, um Nutzer:innen basierend auf Canvas-Eintritt, Variantenzuweisung oder Schritt-Engagement anzusprechen. Diese Filter werten den Eintrittsverlauf und die Interaktionen aus – sie geben nicht an, ob ein:e Nutzer:in noch eine aktive Journey durchläuft.

Um Nutzer:innen basierend auf aktiver Canvas-Teilnahme ein- oder auszuschließen, fügen Sie [Nutzeraktualisierungs]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)-Schritte beim Canvas-Eintritt und -Austritt hinzu, um angepasste Attribute zu setzen und zu löschen, und filtern Sie dann in Campaigns oder Segments nach diesen Attributen.

## Segmentierung {#segmentation}

### Was ist der Unterschied zwischen „Hat keine Canvas-Variante betreten“ und „Ist nicht in der Canvas-Kontrollgruppe“? {#what-is-the-difference-between-has-not-entered-canvas-variation-and-is-not-in-canvas-control-group}

Die vollständigen Filterdefinitionen finden Sie unter [Segmentierungsfilter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).

#### Hat keine Canvas-Variante betreten {#has-not-entered-canvas-variation}

Die/der Nutzer:in hat nie einen Varianten-Pfad eines bestimmten Canvas betreten. Alle Nutzer:innen, die sich nicht in der Kontrollgruppe befinden, sind eingeschlossen – unabhängig davon, ob sie den Canvas betreten haben. Das umfasst Nutzer:innen, die eine andere Variante betreten haben, und Nutzer:innen, die keine Variante betreten haben.

#### Ist nicht in der Canvas-Kontrollgruppe {#is-not-in-canvas-control-group}

Die/der Nutzer:in hat den Canvas betreten, befindet sich aber nicht in der Kontrollgruppe und hat folglich eine Variante erhalten. Dies umfasst nur Nutzer:innen, die den Canvas betreten haben.

Beachten Sie, dass die Variantenzuweisung beim Canvas-Entry erfolgt. Wenn ein:e Nutzer:in einen Canvas nicht betreten hat, wird ihr/ihm keine Variante zugewiesen. Mit anderen Worten: Sie befinden sich weder in der Kontrollgruppe noch in einer Variante.

## Originaler Canvas-Editor {#original-canvas-editor}

{% details Für FAQs zum originalen Canvas-Editor aufklappen %}

### Wie konvertiere ich einen bestehenden Canvas vom originalen Editor zum aktuellen Editor? {#how-do-i-convert-an-existing-canvas-from-the-original-editor-to-the-current-editor}

Sie können [Ihren Canvas Klon]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases). Dadurch wird eine Kopie Ihres originalen Canvas im aktuellsten Canvas-Workflow erstellt.

### Was sind die wesentlichen Unterschiede zwischen dem aktuellen und dem originalen Canvas-Editor? {#what-are-the-main-differences-between-the-current-and-original-canvas-editors}

#### Canvas-Komponenten-Toolbar {#canvas-component-toolbar}

Zuvor wurde beim originalen Canvas-Editor standardmäßig ein vollständiger Schritt hinzugefügt, wenn Sie einen Schritt in Ihrer User-Journey erstellt haben. Diese vollständigen Schritte werden durch verschiedene Canvas-Komponenten ersetzt, was Ihnen den Vorteil einer besseren Übersichtlichkeit und Anpassungsfähigkeit beim Bearbeiten bietet. Sie können sofort alle Ihre Canvas-Komponenten über die Canvas-Schritt-Toolbar sehen.

#### Schrittverhalten {#step-behavior}

Zuvor enthielt jeder vollständige Schritt Informationen wie Verzögerungs- und Zeitplaneinstellungen, Ausnahme-Events, Zielgruppenfilter, Nachrichtenkonfiguration und Optionen zum Nachrichtenfortschritt – alles in einer einzigen Komponente. Im aktuellen Editor sind dies separate Einstellungen, um das Canvas-Erstellungserlebnis anpassbarer zu gestalten, und es gibt einige Unterschiede in der Funktionalität.

#### Fortschritt bei Nachrichten-Komponenten {#message-component-advancement}

[Nachrichten-Komponenten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) bringen alle Nutzer:innen, die den Schritt betreten, weiter voran. Es ist nicht erforderlich, das Fortschrittsverhalten für Nachrichten festzulegen, was die Konfiguration des gesamten Schritts vereinfacht. Wenn Sie die Option **Fortschritt bei gesendeter Nachricht** implementieren möchten, fügen Sie einen separaten Zielgruppenpfad hinzu, um Nutzer:innen herauszufiltern, die den vorherigen Schritt nicht erhalten haben.

#### Verzögerungs-Verhalten „in“ {#delay-in-behavior}

[Verzögerungskomponenten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) warten die gesamte Verzögerungszeit ab, bevor sie zum nächsten Schritt übergehen.

Nehmen wir an, am 12. April haben wir eine Verzögerungskomponente, bei der die Verzögerung so eingestellt ist, dass Nutzer:innen am nächsten Tag um 14 Uhr zum nächsten Schritt weitergeleitet werden. Ein:e Nutzer:in betritt die Komponente am 13. April um 14:01 Uhr.
- Beim originalen Workflow würden Nutzer:innen am 14. April um 14 Uhr zum nächsten Schritt übergehen, was weniger als einen Tag nach dem Eintrittszeitpunkt ist.
- Im aktuellen Editor würden Nutzer:innen am 15. April um 14 Uhr zum nächsten Schritt übergehen. Beachten Sie, dass dies dieselbe Uhrzeit ist, aber mehr als ein Tag seit dem Eintrittszeitpunkt.

#### Verhalten von intelligentem Timing {#intelligent-timing-behavior}

Da [intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) in der Nachrichten-Komponente gespeichert ist, werden Verzögerungen vor den Berechnungen des intelligenten Timings angewendet. Das bedeutet, dass Nutzer:innen je nach Eintrittszeitpunkt in die Komponente die Nachricht möglicherweise später erhalten als in einem Canvas, der mit dem originalen Canvas-Workflow erstellt wurde.

Nehmen wir an, Ihre Verzögerung ist auf 2 Tage eingestellt, intelligentes Timing ist aktiviert und hat ermittelt, dass der beste Zeitpunkt zum Senden Ihrer Nachricht 14 Uhr ist. Ein:e Nutzer:in betritt den Verzögerungsschritt um 14:01 Uhr.
- **Aktueller Workflow:** Es dauert 48 Stunden, bis die Verzögerung abgelaufen ist, sodass Nutzer:innen die Nachricht am dritten Tag um 14 Uhr erhalten.
- **Originaler Workflow:** Nutzer:innen erhalten die Nachricht am zweiten Tag um 14 Uhr.

Beachten Sie: Wenn intelligentes Timing aktiviert ist, wird die Nachricht innerhalb von 24 Stunden nach dem Betreten der Nachrichten-Komponente zum ermittelten intelligenten Zeitpunkt gesendet (auch wenn keine Verzögerungskomponente beteiligt ist).

#### Ausnahme-Events {#exception-events}

##### Ruhezeiten {#quiet-hours}

Ausnahme-Events werden mithilfe von Aktionspfaden angewendet, die von Nachrichten-Schritten getrennt sind. Ruhezeiten werden in der Nachrichten-Komponente durchgesetzt. Das bedeutet: Wenn ein:e Nutzer:in den Aktionspfad bereits passiert hat (und nicht durch das Ausnahme-Event ausgeschlossen wurde), dann auf Ruhezeiten trifft, wenn er/sie die Nachrichten-Komponente erreicht, und der Canvas so konfiguriert ist, dass die Nachricht nach der Ruhezeit erneut gesendet wird, wird das Ausnahme-Event nicht mehr angewendet. Beachten Sie, dass dieser Anwendungsfall nicht häufig vorkommt.

Für Segmente und Filter bietet der Nachrichten-Schritt Zustellungsvalidierungen, mit denen Nutzer:innen zusätzliche Segmente und Filter konfigurieren können, die zum Sendezeitpunkt validiert werden. Dies verhindert den oben genannten Ruhezeiten-Sonderfall.

##### Zeitplaneinstellung „in“ oder „am nächsten“ {#in-or-on-the-next-schedule-setting}

Ausnahme-Events werden mithilfe von Aktionspfaden erstellt. Aktionspfade unterstützen nur „nach einem X-Zeitfenster“ und nicht „in X Zeit“ oder „am nächsten X Zeitpunkt“.

{% enddetails %}

### Was sollte ich bei der Einreichung eines Support-Tickets für einen „Request Timed Out“-Fehler angeben? {#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error}

Wenn beim Bearbeiten eines Canvas ein „Request Timed Out“-Fehler auftritt und Sie den [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) kontaktieren müssen, fügen Sie die folgenden Informationen bei, um die Lösung zu beschleunigen:

{% multi_lang_include messaging/support_ticket_request_timed_out_details.md context='canvas' %}

## Canvas-Zustellung und Fehlerbehebung {#canvas-delivery-and-troubleshooting}

### Sind verwaiste Nutzer:innen berechtigt, Canvas-Nachrichten zu empfangen? {#are-orphaned-users-eligible-to-receive-canvas-messages}

Nein. [Verwaiste Nutzer:innen]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#what-happens-when-you-identify-anonymous-users) sind nicht berechtigt, Nachrichten zu empfangen. Wenn ein Profil verwaist, während sich ein:e Nutzer:in in einem Canvas-Journey befindet, wird der Flow stillschweigend verlassen. Analytics zeigt möglicherweise nicht immer ein **Exited**-Event für diesen Exit an, und die Workflow-Zusammenfassung kann ein `partial_update_token` ohne `exited_date` oder `exit_reason` enthalten.

Weitere Informationen zu Zusammenführungen und verwaisten Profilen finden Sie unter [Doppelte Nutzer:innen zusammenführen]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users).

### Wenn ich ein aktives Canvas oder eine aktive Campaign stoppe, werden bereits an den E-Mail-Anbieter gesendete Nachrichten trotzdem zugestellt? {#if-i-stop-an-active-canvas-or-campaign-do-messages-already-sent-to-the-esp-still-deliver}

Ja. Nachdem Braze eine Anfrage an Ihren E-Mail-Anbieter (E-Mail-Anbieter) gesendet hat, kann Braze diesen Versand nicht zurückrufen. Das Stoppen eines Canvas oder einer Campaign verhindert neue Versandanfragen, aber bereits an den E-Mail-Anbieter übergebene Nachrichten können weiterhin zugestellt werden und die Versandzähler erhöhen, während der E-Mail-Anbieter sie verarbeitet.

Dies ist dasselbe Verhalten, das für das [Stoppen eines Canvas](#what-happens-when-you-stop-a-canvas) beschrieben wird: E-Mail-Versendungen, die sich bereits im Versand befinden, werden nicht sofort gestoppt.

### Wie kann ich bestätigen, dass ein Canvas-Webhook-Schritt ohne für Nutzer:innen sichtbaren Inhalt ausgelöst wurde? {#how-can-i-confirm-a-canvas-webhook-step-fired-without-user-visible-content}

Braze trackt Webhook-**Versendungen** und zugehörige Zustellungsergebnisse für [Webhook]({{site.baseurl}}/user_guide/channels/webhooks)-Schritte in Campaigns und Canvases. Verwenden Sie Schritt-Analytics, [Webhook-Berichte]({{site.baseurl}}/user_guide/channels/webhooks/reporting) oder [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)-Webhook-Events, um zu bestätigen, dass der Schritt ausgeführt wurde. Die Anfrage-Logs Ihres Endpunkts liefern eine zusätzliche Bestätigung, wenn Sie einen serverseitigen Empfangsnachweis benötigen.

Braze enthält kein integriertes unsichtbares Tracking-Pixel für Webhook-Schritte. Verlassen Sie sich auf Braze-Webhook-Metriken und das Logging Ihres Endpunkts anstatt auf angepasste Ein-Pixel-Bildanfragen.

### Warum hat mein Webhook-Schritt kein Body-Feld? {#why-does-my-webhook-step-have-no-body-field}

Webhook-Schritte verwenden einen Request-Body für `POST`, `PUT`, `PATCH` und `DELETE`. Wenn Sie die Methode auf `GET` umschalten, entfernt Braze das Body-Feld, da GET-Anfragen keinen Request-Body unterstützen. Wechseln Sie zurück zu einer Methode mit Body-Unterstützung, wenn Sie JSON- oder Formulardaten senden müssen. Weitere Informationen zu Methoden finden Sie unter [Einen Webhook erstellen]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#http-method).

### Wie verwende ich spacer.gif in einem Webhook-Schritt? {#how-do-i-use-spacergif-in-a-webhook-step}

Braze hostet ein `spacer.gif`-Platzhalterbild auf `cdn.braze.com` und `braze-images.com`. Einige Teams verweisen mit einer Webhook-URL auf dieses Bild, wenn ein Schritt ausgelöst werden muss, ohne einen externen Endpunkt aufzurufen. Standard-Webhook-Schritte sollten einen echten Endpunkt aufrufen. Verwenden Sie [Webhook-Berichte]({{site.baseurl}}/user_guide/channels/webhooks/reporting) und die Logs Ihres Endpunkts, um die Zustellung zu bestätigen, wie unter [Wie kann ich bestätigen, dass ein Canvas-Webhook-Schritt ohne für Nutzer:innen sichtbaren Inhalt ausgelöst wurde?](#how-can-i-confirm-a-canvas-webhook-step-fired-without-user-visible-content) beschrieben.

### Warum lädt mein Canvas nicht und zeigt den Fehler „invalid next-step-id“? {#why-wont-my-canvas-load-with-an-invalid-next-step-id-error}

Dieser Konsolenfehler bedeutet, dass mindestens ein Schritt auf einen fehlenden oder ungültigen nächsten Schritt verweist – zum Beispiel nach einem teilweisen Löschen, Klon oder Import. Öffnen Sie das Canvas im Editor, verbinden Sie verwaiste Schritte erneut oder entfernen Sie Schritte, die keinen gültigen nachgelagerten Pfad mehr haben. Wenn das Canvas immer noch nicht lädt, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) mit der Canvas-ID und einem Screenshot des Konsolenfehlers.

### Warum unterscheidet sich ein Canvas-Konversions-Zeitstempel in Currents von meinen Canvas-Analytics? {#why-does-a-canvas-conversion-timestamp-in-currents-differ-from-my-canvas-analytics}

Currents protokolliert Canvas-Konversionen als [`users.canvas.Conversion`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#canvas-conversion-events)-Events. Die Event-`time` gibt an, wann das Konversions-Event aufgetreten ist. Das Feld `conversion_behavior` dieses Events beschreibt die Konversionsdefinition (Typ und Zeitfenster). Canvas-Analytics können Konversionen auch relativ zum Canvas-Eintritt innerhalb des Konversionsfensters zusammenfassen. Vergleichen Sie beim Abgleich von Exporten die Currents-`time` mit dem Zeitstempel des Konversions-Events und Ihren Canvas-Konversionsfenster-Einstellungen.

### Warum ist `canvas_step_name` in Currents null? {#why-is-canvas_step_name-null-in-currents}

Campaign- und Canvas-Namensfelder wie `canvas_step_name` können `null` sein, wenn ein Currents-Event gesendet wird, bevor Braze die Schritt-Metadaten vollständig übertragen hat – beispielsweise nachdem Sie einen Schritt erstellt oder umbenannt haben. Weitere Details finden Sie unter [Warum ist der Campaign-Name oder Canvas-Schrittname `NULL` in meinen Currents-Daten?]({{site.baseurl}}/user_guide/data/distribution/braze_currents/faq#why-is-the-campaign-name-or-canvas-step-name-null-in-my-currents-data).

### Warum wird mein Array in einem Nutzer:innen-aktualisieren-Schritt nicht aktualisiert? {#why-isnt-my-array-updating-in-a-user-update-step}

Überprüfen Sie den JSON in Ihrem [Nutzer:innen aktualisieren]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)-Schritt. Array- und verschachtelte Attribut-Aktualisierungen benötigen gültige Pfade und Werte für das Attribut, das Sie ändern. Fügen Sie keine Felder hinzu, die der Schritt automatisch bereitstellt, wie z. B. die externe Nutzer-ID. Verwenden Sie den Tab **Vorschau und Test** des Schritts, um den Payload vor dem Start zu bestätigen.

### Kann ich Canvas-Nachrichten an Nutzer:innen ohne `external_id` senden? {#can-i-send-canvas-messages-to-users-without-an-external_id}

Ja, wenn bereits ein Braze-Kundenprofil existiert. Nutzer:innen ohne `external_id` sind [anonyme Nutzer:innen]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#anonymous-user-profiles) und können mit einer `braze_id` oder einem [Nutzer-Alias]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases) referenziert werden. Erstellen oder aktualisieren Sie das Profil mit dem [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) oder Ihrem SDK vor dem Canvas-Eintritt und verwenden Sie dann [aktionsbasierten oder API-getriggerten Eintritt]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule). Standard-Canvas-Targeting erfordert weiterhin ein Braze-Kundenprofil – Sie können keine Canvas-Nachrichten nur an eine E-Mail-Adresse ohne Profil senden.

### Warum ist ein:e Nutzer:in seltener in ein Canvas eingetreten, als er/sie das Trigger-Event ausgeführt hat? {#why-did-a-user-enter-a-canvas-fewer-times-than-they-performed-the-trigger-event}

Bei aktionsbasierten und API-getriggerten Canvases dedupliziert Braze Trigger-Events, sodass ein:e Nutzer:in für dasselbe Canvas höchstens etwa **einmal pro Sekunde** eintreten kann. Wenn ein:e Nutzer:in dasselbe Trigger-Event mehrmals innerhalb einer Sekunde ausführt, wird nur ein Eintritt verarbeitet.

Um mehrere Eintritte in derselben Sekunde zu ermöglichen, planen Sie Trigger-Events mit mindestens 1,1 Sekunden Abstand (zum Beispiel, wenn Sie das Event-Timing von Ihrem Server aus steuern). Für Campaign-ähnliches Verhalten, das mehrere gleichzeitige Trigger erlaubt, vergleichen Sie Ihren Anwendungsfall mit [Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns) mit entsprechenden Zeitplan- und Wiederzulässigkeitseinstellungen.

### Wann werden Nutzer:innen in API-getriggerten Canvases dedupliziert? {#when-are-users-de-duplicated-in-api-triggered-canvases}

Wenn ein:e Nutzer:in erneut in ein API-getriggertes Canvas eintritt und einen Verzögerungsschritt erreicht, in dem er/sie bereits aus einem vorherigen Eintritt für eine identische Nachricht eingereiht ist, dedupliziert Braze den/die Nutzer:in, um doppelte Versendungen zu verhindern. Die zweite Canvas-Instanz wird beendet, sodass die Anzahl der Eintritte die Anzahl der Versendungen übersteigen kann.

### Warum geht ein Test-Push an die falsche App, aber Live-Versendungen sehen korrekt aus? {#why-does-a-test-push-go-to-the-wrong-app-but-live-sends-look-correct}

**Test-Push** auf einem Kundenprofil wird an jedes Push-fähige Gerät für dieses Profil zugestellt. Wenn mehrere Apps auf einem Gerät installiert sind, liefert das Betriebssystem die Test-Benachrichtigung typischerweise an die erste verfügbare App, die möglicherweise nicht die App ist, die Sie validieren möchten.

Um app-spezifisches Targeting zu bestätigen, senden Sie eine Live- oder Testnachricht über eine Campaign oder ein Canvas mit einer engen Zielgruppe (z. B. Filter nach `external_id`), anstatt sich ausschließlich auf **Test-Push** im Profil zu verlassen.

Aktivieren Sie für **Canvas**-Nachrichtenschritte mit mehreren Apps die Option **Zielgruppe bei Nachrichtenversand validieren** im Nachrichtenschritt, damit Segment- und Filterprüfungen zum Versandzeitpunkt durchgeführt werden. Weitere Informationen finden Sie unter [Nachrichtenschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step).

Allgemeine Informationen zum Test-Push-Verhalten finden Sie unter [Testnachrichten senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) und [Push-FAQ]({{site.baseurl}}/user_guide/channels/push/faqs).

### Wie debugge ich Push Stories auf iOS und Android? {#how-do-i-debug-push-stories-on-ios-and-android}

Beginnen Sie mit [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories) für Einrichtung und kreative Anforderungen. Informationen zur Implementierung und zur Handhabung von Rich-Benachrichtigungen finden Sie unter [Rich-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/rich) und [Push Stories]({{site.baseurl}}/developer_guide/push_notifications/push_stories) im Entwicklerhandbuch.

### Wer erhält die E-Mail „Canvas Messages Delayed 24+ Hours“? {#who-receives-the-canvas-messages-delayed-24-hours-email}

Braze sendet diese Benachrichtigung, wenn Canvas-Nachrichten durch Rate-Limiting um 24 Stunden oder mehr verzögert werden. Die E-Mail geht an Dashboard-Nutzer:innen, die zuvor Änderungen am betroffenen Canvas vorgenommen haben (basierend auf Canvas-Änderungsprotokollen). Wenn Braze diese Empfänger:innen nicht ermitteln kann, wird die E-Mail an **Unternehmensadministrator:innen** für den Workspace gesendet.

### Wann erhält ein:e Nutzer:in nach einem Ausnahme-Event keine Nachrichten mehr? {#when-does-a-user-stop-receiving-messages-after-an-exception-event}

Braze erfasst den Exit, sobald das Ausnahme-Event eintritt, aber Nutzer:innen können innerhalb eines Schritts verbleiben, bis Timer abgelaufen sind – am deutlichsten sichtbar bei Verzögerungsschritten. Das Verhalten unterscheidet sich auch zwischen geplanten Schritten und event-getriggerten Schritten. Zeitleisten, Beispiele und Analytics-Nuancen finden Sie unter [Exit-Kriterien]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria).

### Warum zeigt mein Aktionspfade-Schritt einen Fehler an, wenn ich eine Link-Alias-Interaktion auswähle? {#why-does-my-action-paths-step-show-an-error-when-i-select-a-link-alias-interaction}

Aktionsgruppen, die E-Mail-Interaktivitäts-Trigger verwenden (z. B. **Alias in E-Mail geklickt** oder **Alias in einer beliebigen Campaign oder einem Canvas-Schritt geklickt**), benötigen einen Nachrichtenschritt, der die Nachricht mit diesem Link bereits gesendet hat. Fügen Sie Schritte hinzu oder ordnen Sie sie neu an, damit die E-Mail vor der Auswertung des Aktionspfade-Schritts gesendet wird, oder wählen Sie eine Interaktion, die zu einer Nachricht passt, die der/die Nutzer:in bereits in diesem Canvas erhalten hat. Die vollständige Liste der Interaktions-Trigger finden Sie unter [Aktionsbasierte Zustellung]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery).

### Wie wirken sich historische Zeitstempel angepasster Events auf aktionsbasierte Canvases und Campaigns aus? {#how-do-historical-custom-event-timestamps-affect-action-based-canvases-and-campaigns}

Braze wertet aktionsbasierte Journeys aus, wenn qualifizierende Events aufgenommen werden und der/die Nutzer:in Ihre Zielgruppenregeln erfüllt. Wenn ein Event außerhalb des Zeitfensters, in dem Ihr Canvas oder Ihre Campaign aktiv war, auf dem Profil ankommt, oder bevor der/die Nutzer:in Ihrer Zielgruppe entsprach, treten Eintritte oder nachgelagerte Versendungen möglicherweise nicht wie erwartet ein. Vergleichen Sie Event-Zeitstempel mit den Go-Live-Zeiten und der Segmentzugehörigkeit mithilfe des Aktivitätsprotokolls im Kundenprofil und den Fehlerbehebungsschritten unter [Fehlerbehebung bei angepassten Events]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#troubleshooting-custom-events). Wenn das Verhalten dennoch nicht den Erwartungen entspricht, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support).