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

Eine [Komponente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about/) ist ein einzelner Bestandteil Ihres Canvas, mit dem Sie die Effektivität Ihres Canvas bestimmen können. Komponenten können Aktionen wie das Aufteilen Ihrer User-Journey, das Hinzufügen einer Verzögerung und sogar das Testen mehrerer Canvas-Pfade umfassen. Ein Schritt in Canvas bezieht sich auf die personalisierte User-Journey in Ihren Canvas-Branches. Im Wesentlichen besteht Ihr Canvas aus einzelnen Komponenten, die Schritte für Ihre User-Journey bilden.

### Kann ich ein Canvas mit nicht verbundenen Schritten starten? {#can-i-launch-a-canvas-with-disconnected-steps}

Ja. Sie können Canvases auch nach dem Start mit nicht verbundenen Schritten speichern.

### Wohin gelangen Nutzer:innen, wenn sie einen nicht verbundenen Schritt erreicht haben? {#where-do-users-go-when-theyve-reached-a-disconnected-step}

Wenn sich ein:e Nutzer:in in einem nicht verbundenen Schritt Ihres Canvas-Workflows befindet, wird er/sie zum nächsten Schritt weitergeleitet, sofern einer vorhanden ist, und die Einstellung des Schritts bestimmt, wie der/die Nutzer:in fortschreiten soll. Dies soll es Ihnen ermöglichen, Änderungen an Schritten vorzunehmen, ohne sie direkt mit dem Rest des Canvas verbinden zu müssen. Außerdem haben Sie so Spielraum zum Testen, bevor Sie sofort live gehen – im Grunde können Sie so einen Entwurf speichern.

Wir empfehlen, die Analytics-Ansicht auf wartende Nutzer:innen in einem Canvas-Schritt zu prüfen, bevor Sie einen Schritt trennen.

### Was passiert, wenn die Zielgruppe und die Sendezeit für ein Canvas mit einer Variante, aber mehreren Branches identisch sind? {#what-happens-if-the-audience-and-send-time-are-identical-for-a-canvas-that-has-one-variant-but-multiple-branches}

Wir reihen einen Job für jeden Schritt in die Warteschlange ein – sie laufen ungefähr zur gleichen Zeit, und einer davon „gewinnt“. In der Praxis kann dies einigermaßen gleichmäßig verteilt sein, aber es gibt wahrscheinlich zumindest eine leichte Tendenz zugunsten des Schritts, der zuerst erstellt wurde.

Darüber hinaus können wir keine Garantien dafür geben, wie diese Verteilung genau aussehen wird. Wenn Sie eine gleichmäßige Aufteilung wünschen, fügen Sie einen Filter für [zufällige Bucket-Nummern]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers/) hinzu.

### Wie werden Canvas-Zielgruppen ausgewertet? {#how-are-canvas-audiences-evaluated}

Standardmäßig werden Filter und Segmente für vollständige Schritte im Canvas zum Sendezeitpunkt geprüft. Der Decision-Split-Schritt führt eine Auswertung direkt nach Erhalt eines vorherigen Schritts durch (oder vor einer Verzögerung).

### Wann wird ein Ausnahme-Event ausgelöst? {#when-does-an-exception-event-trigger}

Ausnahme-Events werden nur ausgelöst, während der/die Nutzer:in darauf wartet, die zugehörige Canvas-Komponente zu erhalten. Wenn ein:e Nutzer:in eine Aktion im Voraus ausführt, wird das Ausnahme-Event nicht ausgelöst. Wenn Sie Nutzer:innen ausschließen möchten, die ein bestimmtes Event bereits im Voraus ausgeführt haben, verwenden Sie stattdessen [Filter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/).

### Wie wirkt sich die Bearbeitung eines Canvas auf Nutzer:innen aus, die sich bereits im Canvas befinden? {#how-does-editing-a-canvas-affect-users-already-in-the-canvas}

Wenn Sie einige Schritte eines mehrstufigen Canvas bearbeiten, erhalten Nutzer:innen, die bereits zur Zielgruppe gehören, aber die Schritte noch nicht erhalten haben, die aktualisierte Version der Nachricht. Beachten Sie, dass dies nur geschieht, wenn sie noch nicht für den Schritt ausgewertet wurden.

Weitere Informationen darüber, was Sie nach dem Start bearbeiten können, finden Sie unter [Canvas nach dem Start ändern]({{site.baseurl}}/post-launch_edits/).

### Was passiert, wenn Sie ein Canvas stoppen? {#what-happens-when-you-stop-a-canvas}

Wenn Sie ein Canvas stoppen, gilt Folgendes:

- Nutzer:innen werden daran gehindert, das Canvas zu betreten.
- Es werden keine weiteren Nachrichten gesendet, unabhängig davon, wo sich ein:e Nutzer:in im Flow befindet.
- **Ausnahme:** Canvases mit E-Mails werden nicht sofort gestoppt. Nachdem die Sendeanfragen an SendGrid gesendet wurden, können wir nichts mehr tun, um die Zustellung an den/die Nutzer:in zu verhindern.

### Sollte ich ein Canvas oder separate Canvases pro User-Lifecycle erstellen? {#should-i-build-one-canvas-or-separate-canvases-per-user-lifecycle}

Je nachdem, was Sie mit Ihrem Canvas erreichen möchten, benötigen Sie möglicherweise unterschiedliche Ansätze für den Aufbau Ihrer User-Journey. Die Flexibilität von Canvas ermöglicht es Ihnen, User-Journeys für jede Phase des User-Lifecycles abzubilden. Schauen Sie sich unsere [Braze-Canvas-Templates]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates/) an, um verschiedene Beispiele für optimierte Ansätze zur Erstellung effektiver User-Journeys zu sehen.

## Nachrichten und Zustellung {#messages-and-delivery}

### Wann werden In-App-Nachrichten in Canvas gesendet? {#when-are-in-app-messages-in-canvas-sent}

In-App-Nachrichten werden beim nächsten Sitzungsstart gesendet. Das bedeutet: Wenn der/die Nutzer:in den Canvas-Schritt betritt, bevor das Canvas gestoppt wird, erhält er/sie die In-App-Nachricht beim nächsten Sitzungsstart, solange die In-App-Nachricht noch nicht abgelaufen ist.

Es ist möglich, dass ein:e Nutzer:in eine Sitzung startet, bevor das Canvas gestoppt wird, die In-App-Nachricht aber nicht sofort angezeigt wird. Dies kann vorkommen, wenn die In-App-Nachricht durch ein angepasstes Event getriggert wird oder verzögert ist. Das bedeutet, dass ein:e Nutzer:in eine In-App-Nachrichten-Impression protokollieren und die In-App-Nachricht „erhalten“ kann, nachdem das Canvas gestoppt wurde. Der/die Nutzer:in müsste die Sitzung jedoch vor dem Stoppen des Canvas gestartet haben, aber **nachdem** er/sie den Canvas-Schritt erhalten hat.

{% alert note %}
Das Stoppen eines Canvas führt nicht dazu, dass Nutzer:innen, die auf den Empfang von Nachrichten warten, die User-Journey verlassen. Wenn Sie das Canvas wieder aktivieren und Nutzer:innen noch auf die Nachricht warten, erhalten sie diese (es sei denn, der Zeitpunkt, zu dem die Nachricht hätte gesendet werden sollen, ist bereits verstrichen – dann erhalten sie sie nicht).
{% endalert %}

### Warum kann ein Canvas null Sends anzeigen, obwohl Impressionen protokolliert werden? {#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged}

Wenn _Gesendete Nachrichten_ für ein Canvas mit einem In-App-Nachrichten-Schritt immer null sind, liegt das daran, dass die Zustellung von In-App-Nachrichten anders funktioniert als bei anderen Messaging-Kanälen.

In-App-Nachrichten werden vom SDK „abgerufen“ und nicht von Braze „gepusht“. In-App-Nachrichten für berechtigte Nutzer:innen werden automatisch beim Sitzungsstart zugestellt und „warten“ auf das Trigger-Event, bevor sie angezeigt werden. Da berechtigte Nutzer:innen die Nachricht beim Start einer Sitzung erhalten, meldet Braze dies nicht als Sende-Event. Wenn Nutzer:innen das Trigger-Event ausführen, wird die Nachricht angezeigt und Braze protokolliert eine Impression und markiert den Canvas-Schritt (oder die Campaign) als empfangen im Nutzerprofil. Folglich ist die Gesamtzahl der _Sends_ für In-App-Nachrichten null.

### Kann ich unterschiedliche Sendezeiten für jede Variante im selben Canvas-Nachrichten-Schritt oder multivariaten Send planen? {#can-i-schedule-different-send-times-for-each-variant-in-the-same-canvas-message-step-or-multivariate-send}

Nein. Varianten in derselben multivariaten Konfiguration oder demselben Nachrichten-Schritt teilen sich einen Zustellungszeitplan. Sie können nicht eine Variante um 18 Uhr und eine andere um 19 Uhr für denselben geplanten Send zuweisen.

Um Sends zeitlich zu staffeln oder unterschiedliche Zeiten pro Pfad zu verwenden, probieren Sie die folgenden Methoden:

- Separate Nachrichten-Schritte mit Verzögerungsschritten dazwischen, sodass jede Nachricht ihren eigenen Zeitplan hat.
- Branches oder einen [Experimentpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/)-Schritt, damit Nutzer:innen Pfaden mit unterschiedlichem Timing folgen.
- Separate Campaigns, wenn der Anwendungsfall nicht innerhalb eines Canvas bleiben muss.

Für multivariate und A/B-Konzepte in Campaigns siehe [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing/).

### Was passiert, wenn ein:e Nutzer:in bei einem Canvas-Nachrichten-Schritt durch globales Frequency-Capping begrenzt wird? {#what-happens-if-a-user-is-global-frequency-capped-at-a-canvas-message-step}

Er/sie erhält den Send für den begrenzten Kanal nicht, aber Nachrichten-Schritte leiten Nutzer:innen trotzdem weiter, wenn eine Nachricht aufgrund von globalem Frequency-Capping nicht gesendet wird. Für die schrittweisen Fortschrittsfälle siehe [Wie Nutzer:innen fortschreiten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/#how-users-advance). Globales Frequency-Capping allein führt nicht dazu, dass Nutzer:innen ein Canvas verlassen; dieses Verhalten ist unabhängig von den **Zustellungsvalidierungen** eines Nachrichten-Schritts. Weitere Details finden Sie unter [Rate-Limiting und Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/).

### Warum sind die Sends niedriger als die geschätzte Zielgruppengröße? {#why-are-sends-lower-than-the-estimated-audience-size}

Sends können aus vielen der gleichen Gründe niedriger sein als die **geschätzte Zielgruppe** wie bei [Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/faq/#why-are-sends-lower-than-the-estimated-audience-size), einschließlich Frequency Caps, strikter Geräte- oder Browser-Filter, Wiederzulassungsfenster, Rate-Limiting und kanalspezifischer Ausschlüsse (zum Beispiel Push-Erreichbarkeit oder E-Mail-Abo- und Zustellbarkeitsprüfungen).

Canvas-spezifische Faktoren gelten ebenfalls:

- **Aktionsbasierter oder API-getriggerter Eintritt:** Nutzer:innen betreten das Canvas (und erhalten Schritte) erst, nachdem sie das Eintrittsverhalten ausgeführt haben, sodass die tatsächlichen Sends hinter der Vorabschätzung zurückbleiben, bis diese Aktionen eintreten.
- **Zielgruppenpfade:** Nutzer:innen werden zum Branch mit der höchsten Priorität weitergeleitet, für den sie sich qualifizieren, sodass nachgelagerte Branches möglicherweise weniger Nutzer:innen erhalten, als eine einfache Segment-Zählung vermuten lässt.
- **Zielgruppen- und Sendezeitprüfungen:** Vollständige Schritte werten Filter zum Sendezeitpunkt erneut aus, sofern Sie nichts anderes konfigurieren. Nutzer:innen, die sich beim Erstellen des Canvas qualifiziert haben, können vor dem Senden einer Nachricht herausfallen.
- **Kontrollgruppen:** Globale oder Canvas-Kontrollgruppen halten einen Anteil der Eintretenden vom Messaging zurück.
- **Ruhezeiten und Verzögerungen:** Nachrichten können zurückgehalten oder neu geplant werden, wodurch Sends aus dem Berichtszeitraum verschoben werden, den Sie gerade betrachten.
- **Maximale Eintritts- oder Zielgruppen-Caps:** Eintritts- oder Send-Caps stoppen zusätzliche Nutzer:innen, selbst wenn das zugrunde liegende Segment größer ist.
- **Berichtszeitraum:** Der Analytics-Bereich umfasst möglicherweise nicht jeden Send, den Sie mit der Schätzung vergleichen.

### Warum ist _Eindeutige Empfänger:innen_ höher als die Anzahl der Nutzer:innen, die ich angesprochen habe? {#why-is-_unique-recipients_-higher-than-the-number-of-users-i-targeted}

_Eindeutige Empfänger:innen_ kann höher sein als die erwartete Zielgruppe, da Braze **eindeutige tägliche Empfänger:innen** für Canvas- und Campaign-Berichte trackt. Dies unterstützt eine genaue Conversion-Attribution jedes Mal, wenn ein:e Nutzer:in eine Nachricht in der Journey erhält.

Wenn ein:e Nutzer:in beispielsweise am Montag und erneut am Freitag einen Canvas-Schritt erhält und nach jedem Send konvertiert, kann Braze zwei Empfänger:innen-Zeilen und zwei relevante Conversions zählen. Bei wiederkehrenden Eintritten oder Wiederzulassung kann dieselbe kleine Gruppe von Profilen über mehrere Tage hinweg mehrere _Eindeutige Empfänger:innen_ erzeugen.

## Analytics und Conversions {#analytics-and-conversions}

### Wie werden Nutzer-Conversions in einem Canvas getrackt? {#how-are-user-conversions-tracked-in-a-canvas}

Ein:e Nutzer:in kann pro Canvas-Eintritt nur einmal konvertieren. Conversions werden der zuletzt empfangenen Nachricht des/der Nutzer:in für diesen Eintritt zugeordnet. Der Zusammenfassungsblock am Anfang eines Canvas zeigt alle Conversions, die von Nutzer:innen innerhalb dieses Pfads durchgeführt wurden, unabhängig davon, ob sie eine Nachricht erhalten haben. Jeder nachfolgende Schritt zeigt nur Conversions an, die stattfanden, während dieser der letzte Schritt war, den der/die Nutzer:in erhalten hat.

{% alert note %}
Wenn ein:e Nutzer:in ein Canvas erneut betritt, werden Konversions-Events nur für den letzten Eintritt getrackt. Konversions-Events werden nicht für vorherige Eintritte protokolliert, selbst wenn das Konversions-Event nachträglich erfasst wird.
{% endalert %}

{% details Für Beispiele erweitern %}

**Beispiel 1**

Es gibt einen Canvas-Pfad mit 10 Push-Benachrichtigungen und das Konversions-Event ist „Sitzungsstart“ („App öffnen“):

- Nutzer:in A öffnet die App nach dem Eintritt, aber vor dem Empfang der ersten Nachricht.
- Nutzer:in B öffnet die App nach jeder Push-Benachrichtigung.

**Ergebnis:** Die Zusammenfassung zeigt zwei Conversions, während die einzelnen Schritte eine Conversion von eins beim ersten Schritt und null für alle nachfolgenden Schritte anzeigen.

{% alert note %}
Wenn Ruhezeiten aktiv sind, wenn das Konversions-Event eintritt, gelten dieselben Regeln.
{% endalert %}

**Beispiel 2**

Es gibt ein einstufiges Canvas mit aktivierten Ruhezeiten:

1. Nutzer:in betritt das Canvas.
2. Der erste Schritt hat keine Verzögerung, liegt aber innerhalb der festgelegten Ruhezeiten, sodass die Nachricht unterdrückt wird.
3. Nutzer:in führt das Konversions-Event aus.

**Ergebnis:** Der/die Nutzer:in wird in der gesamten Canvas-Variante als konvertiert gezählt, aber nicht im Schritt, da er/sie den Schritt nicht erhalten hat.

{% enddetails %}

### Was ist der Unterschied zwischen den verschiedenen Konversionsraten-Typen? {#whats-the-difference-between-the-different-conversion-rate-types}

- Gesamte Canvas-Conversions zeigen, wie viele eindeutige Nutzer:innen ein Konversions-Event abgeschlossen haben, nicht wie viele Conversions jede:r einzelne abgeschlossen hat.
- Die Varianten-Konversionsrate oder der Zusammenfassungsblock am Anfang eines Canvas zeigt alle Conversions, die von Nutzer:innen innerhalb dieses Pfads durchgeführt wurden, unabhängig davon, ob sie eine Nachricht erhalten haben, als Gesamtsumme.
- Die Schritt-Konversionsrate zeigt, wie viele Personen diesen Nachrichten-Schritt erhalten und eines der definierten Konversions-Events abgeschlossen haben.

### Warum ist meine Canvas-Schritt-Konversionsrate nicht gleich meiner Canvas-Varianten-Gesamtkonversionsrate? {#why-is-my-canvas-step-conversion-rate-not-equal-to-my-canvas-variant-total-conversion-rate}

Es ist üblich, dass die Conversions-Gesamtzahl einer Canvas-Variante größer ist als die Summe ihrer Schritt-Gesamtzahlen. Dies liegt daran, dass ein:e Nutzer:in ein Konversions-Event für eine Variante ausführen kann, sobald er/sie die Variante betritt. Dasselbe Konversions-Event zählt jedoch nicht für einen Canvas-Schritt. Jede:r Nutzer:in, der/die das Canvas betritt und das Konversions-Event vor dem Empfang des ersten Canvas-Schritts ausführt, wird zur Varianten-Conversions-Gesamtzahl gezählt, aber nicht zur Schritt-Gesamtzahl. Dasselbe gilt für Nutzer:innen, die das Canvas betreten, aber das Canvas verlassen, bevor sie einen Schritt erhalten.

Beachten Sie, dass es auch möglich ist, dass ein:e Nutzer:in eine Variante betritt, keine Nachricht von einem Schritt erhält und dann konvertiert. In diesem Fall wird keine Conversion auf Schrittebene protokolliert. Da der/die Nutzer:in jedoch technisch gesehen konvertiert hat, wird eine Conversion auf Canvas-Ebene protokolliert.

### Wie kann ich bestätigen, ob meine Nutzer:innen ein API-getriggertes Canvas erhalten haben? {#how-can-i-confirm-if-my-users-received-an-api-triggered-canvas}

Sie können [ein Segment erstellen]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/), indem Sie einen Canvas-Filter verwenden, um zu bestätigen, ob Nutzer:innen das Canvas betreten oder einen bestimmten Canvas-Schritt erhalten haben. Verwenden Sie beispielsweise einen Canvas-Eintrittsfilter, wenn Sie bestätigen möchten, dass Nutzer:innen das API-getriggerte Canvas betreten haben, oder einen Filter für empfangene Schritte, wenn Sie bestätigen möchten, dass sie eine Nachricht aus dem Canvas erhalten haben. Verwenden Sie dann den [`/users/export/segment`-Endpunkt]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/), um die Nutzer:innen in diesem Segment zu exportieren.

### Kann ich ein Canvas löschen? {#can-i-delete-a-canvas}

Nein, aber Sie können [ein Canvas archivieren]({{site.baseurl}}/user_guide/messaging/governance/archiving/).

### Wie kann ich die Analytics für jede meiner Canvas-Komponenten anzeigen? {#how-can-i-view-analytics-for-each-of-my-canvas-components}

Um die Analytics einer Canvas-Komponente anzuzeigen, gehen Sie zu Ihrem Canvas und scrollen Sie auf der Seite **Canvas-Details** nach unten. Hier können Sie die Analytics jeder Komponente einsehen. Weitere Details finden Sie unter [Canvas-Analytics]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/).

### Ist bei der Betrachtung der Anzahl eindeutiger Nutzer:innen Canvas-Analytics oder der Segmenter genauer? {#when-looking-at-the-number-of-unique-users-is-canvas-analytics-or-the-segmenter-more-accurate}

Der Segmenter ist eine genauere Statistik für eindeutige Nutzerdaten als Canvas- oder Campaign-Statistiken. Das liegt daran, dass Canvas- und Campaign-Statistiken Zahlen sind, die Braze inkrementiert, wenn etwas passiert – was bedeutet, dass es Variablen gibt, die dazu führen können, dass diese Zahl von der des Segmenters abweicht. Zum Beispiel können Nutzer:innen mehr als einmal für ein Canvas oder eine Campaign konvertieren.

### Warum weicht die Anzahl der Nutzer:innen, die ein Canvas betreten, von der erwarteten Anzahl ab? {#why-does-the-number-of-users-entering-a-canvas-not-match-the-expected-number}

Die Anzahl der Nutzer:innen, die ein Canvas betreten, kann von Ihrer erwarteten Anzahl abweichen, da Zielgruppen und Trigger unterschiedlich ausgewertet werden. In Braze wird eine Zielgruppe vor dem Trigger ausgewertet (es sei denn, es wird ein [Änderung eines Attributs]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers/#change-custom-attribute-value)-Trigger verwendet). Dies führt dazu, dass Nutzer:innen aus dem Canvas herausfallen, wenn sie nicht Teil Ihrer ausgewählten Zielgruppe sind, bevor Trigger-Aktionen ausgewertet werden.

### Was passiert mit anonymen Nutzer:innen während ihrer Canvas-Journey? {#what-happens-to-anonymous-users-during-their-canvas-journey}

Obwohl anonyme Nutzer:innen Canvases betreten und verlassen können, werden ihre Aktionen keinem bestimmten Nutzerprofil zugeordnet, bis sie identifiziert werden, sodass ihre Interaktionen möglicherweise nicht vollständig in Ihren Analytics getrackt werden. Sie können den [Abfrage-Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder/) verwenden, um einen Bericht über diese Metriken zu erstellen.

{% alert tip %}
Für weitere Unterstützung bei der Canvas-Fehlerbehebung wenden Sie sich bitte innerhalb von 30 Tagen nach Auftreten Ihres Problems an den Braze-Support, da uns nur die Diagnoseprotokolle der letzten 30 Tage zur Verfügung stehen.
{% endalert %}

### Kann ich Nutzer:innen, die sich derzeit in einer Canvas-Journey befinden, von einer Campaign oder einem Segment ausschließen? {#can-i-exclude-users-who-are-currently-in-a-canvas-journey-from-a-campaign-or-segment}

Verwenden Sie [Segmentierungs-Filter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/) wie `Entered Canvas Variation`, `In Canvas Control Group` oder `Received Message from Canvas Step`, um Nutzer:innen basierend auf Canvas-Eintritt, Variantenzuweisung oder Schritt-Engagement anzusprechen. Diese Filter werten den Eintrittsverlauf und Interaktionen aus – sie geben nicht an, ob ein:e Nutzer:in noch aktiv eine Journey durchläuft.

Um Nutzer:innen basierend auf aktiver Canvas-Teilnahme ein- oder auszuschließen, fügen Sie [Nutzeraktualisierung]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update/)-Schritte beim Canvas-Eintritt und -Austritt hinzu, um angepasste Attribute zu setzen und zu löschen, und filtern Sie dann in Campaigns oder Segmenten nach diesen Attributen.

## Segmentierung {#segmentation}

### Was ist der Unterschied zwischen „Hat keine Canvas-Variante betreten“ und „Ist nicht in der Canvas-Kontrollgruppe“? {#what-is-the-difference-between-has-not-entered-canvas-variation-and-is-not-in-canvas-control-group}

Die vollständigen Filterdefinitionen finden Sie unter [Segmentierungs-Filter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/).

#### Hat keine Canvas-Variante betreten {#has-not-entered-canvas-variation}

Der/die Nutzer:in hat nie einen Varianten-Pfad eines bestimmten Canvas betreten. Alle Nutzer:innen, die nicht in der Kontrollgruppe sind, werden einbezogen, unabhängig davon, ob sie das Canvas betreten haben. Dies umfasst Nutzer:innen, die eine andere Variante betreten haben, und Nutzer:innen, die keine Variante betreten haben.

#### Ist nicht in der Canvas-Kontrollgruppe {#is-not-in-canvas-control-group}

Der/die Nutzer:in hat das Canvas betreten, ist aber nicht in der Kontrollgruppe und hat folglich eine Variante erhalten. Dies umfasst nur Nutzer:innen, die das Canvas betreten haben.

Beachten Sie, dass die Variantenzuweisung beim Canvas-Eintritt erfolgt. Wenn ein:e Nutzer:in ein Canvas nicht betreten hat, wird ihm/ihr keine Variante zugewiesen. Mit anderen Worten: Er/sie befindet sich weder in der Kontrollgruppe noch in einer Variante.

## Originaler Canvas-Editor {#original-canvas-editor}

{% details Für FAQs zum originalen Canvas-Editor erweitern %}

### Wie konvertiere ich ein bestehendes Canvas vom originalen Editor zum aktuellen Editor? {#how-do-i-convert-an-existing-canvas-from-the-original-editor-to-the-current-editor}

Sie können [Ihr Canvas klonen]({{site.baseurl}}/cloning_canvases/). Dadurch wird eine Kopie Ihres originalen Canvas im aktuellsten Canvas-Workflow erstellt.

### Was sind die Hauptunterschiede zwischen dem aktuellen und dem originalen Canvas-Editor? {#what-are-the-main-differences-between-the-current-and-original-canvas-editors}

#### Canvas-Komponenten-Toolbar {#canvas-component-toolbar}

Zuvor wurde beim originalen Canvas-Editor standardmäßig ein vollständiger Schritt hinzugefügt, wenn Sie einen Schritt in Ihrer User-Journey erstellt haben. Diese vollständigen Schritte werden durch verschiedene Canvas-Komponenten ersetzt, was Ihnen den Vorteil einer besseren Übersichtlichkeit und Anpassungsmöglichkeiten für Ihre Bearbeitungserfahrung bietet. Sie können alle Ihre Canvas-Komponenten sofort über die Canvas-Schritt-Toolbar sehen.

#### Schrittverhalten {#step-behavior}

Zuvor enthielt jeder vollständige Schritt Informationen wie Verzögerungs- und Zeitplaneinstellungen, Ausnahme-Events, Zielgruppen-Filter, Nachrichtenkonfiguration und Optionen zum Nachrichtenfortschritt – alles in einer Komponente. Diese sind im aktuellen Editor separate Einstellungen, um Ihre Canvas-Erstellung anpassbarer zu gestalten, und führen zu einigen Unterschieden in der Funktionalität.

#### Fortschritt der Nachrichten-Komponente {#message-component-advancement}

[Nachrichten-Komponenten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/) leiten alle Nutzer:innen weiter, die den Schritt betreten. Es ist nicht erforderlich, das Fortschrittsverhalten der Nachricht festzulegen, was die Konfiguration des gesamten Schritts einfacher macht. Wenn Sie die Option **Fortschritt bei gesendeter Nachricht** implementieren möchten, fügen Sie einen separaten Zielgruppenpfad hinzu, um Nutzer:innen herauszufiltern, die den vorherigen Schritt nicht erhalten haben.

#### Verzögerungsverhalten „in“ {#delay-in-behavior}

[Verzögerungskomponenten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step/) warten die gesamte Verzögerungszeit ab, bevor sie zum nächsten Schritt übergehen.

Nehmen wir an, am 12. April haben wir eine Verzögerungskomponente, bei der die Verzögerung so eingestellt ist, dass der/die Nutzer:in in einem Tag um 14 Uhr zum nächsten Schritt weitergeleitet wird. Ein:e Nutzer:in betritt die Komponente am 13. April um 14:01 Uhr.
- Beim originalen Workflow würde der/die Nutzer:in am 14. April um 14 Uhr zum nächsten Schritt übergehen, was weniger als ein Tag ab dem Eintrittszeitpunkt ist.
- Im aktuellen Editor würde der/die Nutzer:in am 15. April um 14 Uhr zum nächsten Schritt übergehen. Beachten Sie, dass dies dieselbe Uhrzeit ist, aber mehr als ein Tag ab dem Eintrittszeitpunkt.

#### Verhalten des intelligenten Timings {#intelligent-timing-behavior}

Da [intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/) in der Nachrichten-Komponente gespeichert ist, werden Verzögerungen vor den Berechnungen des intelligenten Timings angewendet. Das bedeutet, dass Nutzer:innen je nach Eintrittszeitpunkt in die Komponente die Nachricht möglicherweise später erhalten als in einem Canvas, das mit dem originalen Canvas-Workflow erstellt wurde.

Nehmen wir an, Ihre Verzögerung ist auf 2 Tage eingestellt, intelligentes Timing ist aktiviert und hat bestimmt, dass die beste Sendezeit 14 Uhr ist. Ein:e Nutzer:in betritt den Verzögerungsschritt um 14:01 Uhr.
- **Aktueller Workflow:** Es dauert 48 Stunden, bis die Verzögerung abgelaufen ist, sodass der/die Nutzer:in die Nachricht am dritten Tag um 14 Uhr erhält.
- **Originaler Workflow:** Der/die Nutzer:in erhält die Nachricht am zweiten Tag um 14 Uhr.

Beachten Sie: Wenn intelligentes Timing aktiviert ist, wird die Nachricht innerhalb von 24 Stunden nach dem Eintritt des/der Nutzer:in in die Nachrichten-Komponente zur ermittelten intelligenten Zeit gesendet (auch wenn keine Verzögerungskomponente beteiligt ist).

#### Ausnahme-Events {#exception-events}

##### Ruhezeiten {#quiet-hours}

Ausnahme-Events werden mithilfe von Aktionspfaden angewendet, die von Nachrichten-Schritten getrennt sind. Ruhezeiten werden in der Nachrichten-Komponente durchgesetzt. Das bedeutet: Wenn ein:e Nutzer:in den Aktionspfad bereits passiert hat (und nicht durch das Ausnahme-Event ausgeschlossen wurde), dann auf Ruhezeiten trifft, wenn er/sie die Nachrichten-Komponente erreicht, und das Canvas so konfiguriert ist, dass die Nachricht nach der Ruhezeitperiode erneut gesendet wird, wird das Ausnahme-Event nicht mehr angewendet. Beachten Sie, dass dieser Anwendungsfall nicht häufig vorkommt.

Für Segmente und Filter verfügt der Nachrichten-Schritt über Zustellungsvalidierungen, mit denen Sie zusätzliche Segmente und Filter konfigurieren können, die zum Sendezeitpunkt validiert werden. Dies verhindert den oben genannten Ruhezeiten-Grenzfall.

##### Zeitplaneinstellung „in“ oder „am nächsten“ {#in-or-on-the-next-schedule-setting}

Ausnahme-Events werden mithilfe von Aktionspfaden erstellt. Aktionspfade unterstützen nur „nach einem X-Zeitfenster“ und nicht „in X Zeit“ oder „am nächsten X Zeitpunkt“.

{% enddetails %}

### Was sollte ich angeben, wenn ich ein Support-Ticket für einen „Request Timed Out“-Fehler einreiche? {#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error}

Wenn Sie beim Bearbeiten eines Canvas auf einen „Request Timed Out“-Fehler stoßen und den [Braze-Support]({{site.baseurl}}/braze_support/) kontaktieren müssen, geben Sie die folgenden Informationen an, um die Lösung zu beschleunigen:

- **Bildschirmaufnahme:** Eine Aufnahme der Schritte, die Sie vor dem Auftreten des Fehlers durchgeführt haben, einschließlich aller Seitenübergänge.
- **Zeitstempel und Zeitzone:** Der genaue Zeitpunkt, zu dem der Fehler aufgetreten ist, und Ihre Zeitzone.
- **Browser und Version:** Der Browser, den Sie verwenden (zum Beispiel Chrome 120, Safari 17), und ob Sie versucht haben, den Fehler in einem anderen Browser zu reproduzieren.
- **Schritte zur Reproduktion:** Eine klare Beschreibung der Aktionen, die den Fehler auslösen, einschließlich aller beteiligten Canvas-Schritte oder Konfigurationen.
- **Netzwerkprotokolle (optional):** Öffnen Sie die Entwicklertools Ihres Browsers (Tab **Netzwerk**), reproduzieren Sie den Fehler und exportieren Sie das Netzwerkprotokoll als HTTP-Archiv-(HAR)-Datei. Dies hilft dem Support-Team zu identifizieren, welcher API-Aufruf das Timeout verursacht.

## Canvas-Zustellung und Fehlerbehebung {#canvas-delivery-and-troubleshooting}

### Sind verwaiste Nutzer:innen berechtigt, Canvas-Nachrichten zu erhalten? {#are-orphaned-users-eligible-to-receive-canvas-messages}

Nein. [Verwaiste Nutzer:innen]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/#what-happens-when-you-identify-anonymous-users) sind nicht berechtigt, Nachrichten zu erhalten. Wenn ein Profil verwaist wird, während sich ein:e Nutzer:in in einer Canvas-Journey befindet, verlässt er/sie den Flow stillschweigend. Analytics zeigen möglicherweise nicht immer ein **Ausgetreten**-Event für diesen Austritt an, und die Workflow-Zusammenfassung kann ein `partial_update_token` ohne `exited_date` oder `exit_reason` enthalten.

Weitere Informationen zu Zusammenführungen und verwaisten Profilen finden Sie unter [Doppelte Nutzer:innen zusammenführen]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/).

### Wenn ich ein aktives Canvas oder eine aktive Campaign stoppe, werden bereits an den ESP gesendete Nachrichten trotzdem zugestellt? {#if-i-stop-an-active-canvas-or-campaign-do-messages-already-sent-to-the-esp-still-deliver}

Ja. Nachdem Braze eine Anfrage an Ihren E-Mail-Anbieter (ESP) gesendet hat, kann Braze diesen Send nicht zurückrufen. Das Stoppen eines Canvas oder einer Campaign verhindert neue Sendeanfragen, aber Nachrichten, die bereits an den ESP übergeben wurden, können weiterhin zugestellt werden und die Send-Zähler erhöhen, während der ESP sie verarbeitet.

Dies ist dasselbe Verhalten, das für das [Stoppen eines Canvas](#what-happens-when-you-stop-a-canvas) beschrieben wird: E-Mail-Sends, die sich bereits im Versand befinden, werden nicht sofort angehalten.

### Wie kann ich bestätigen, dass ein Canvas-Webhook-Schritt ohne nutzersichtbaren Inhalt ausgelöst wurde? {#how-can-i-confirm-a-canvas-webhook-step-fired-without-user-visible-content}

Braze trackt Webhook-**Sends** und zugehörige Zustellungsergebnisse für [Webhook]({{site.baseurl}}/user_guide/channels/webhooks/)-Schritte in Campaigns und Canvases. Verwenden Sie Schritt-Analytics, [Webhook-Berichte]({{site.baseurl}}/user_guide/channels/webhooks/reporting/) oder [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)-Webhook-Events, um zu bestätigen, dass der Schritt ausgeführt wurde. Die Anforderungsprotokolle Ihres Endpunkts bieten zusätzliche Bestätigung, wenn Sie einen serverseitigen Empfangsnachweis benötigen.

Braze enthält kein integriertes unsichtbares Tracking-Pixel für Webhook-Schritte. Verlassen Sie sich auf Braze-Webhook-Metriken und die Protokollierung Ihres Endpunkts anstelle von benutzerdefinierten Ein-Pixel-Bildanfragen.

### Warum hat ein:e Nutzer:in ein Canvas weniger oft betreten, als er/sie das Trigger-Event ausgeführt hat? {#why-did-a-user-enter-a-canvas-fewer-times-than-they-performed-the-trigger-event}

Für aktionsbasierte und API-getriggerte Canvases dedupliziert Braze Trigger-Events, sodass ein:e Nutzer:in für dasselbe Canvas höchstens etwa **einmal pro Sekunde** eintreten kann. Wenn ein:e Nutzer:in dasselbe Trigger-Event mehrmals innerhalb einer Sekunde ausführt, wird nur ein Eintritt verarbeitet.

Um mehrere Eintritte in derselben Sekunde zu ermöglichen, planen Sie Trigger-Events mit mindestens 1,1 Sekunden Abstand (zum Beispiel, wenn Sie das Event-Timing von Ihrem Server aus steuern). Für Campaign-ähnliches Verhalten, das mehrere gleichzeitige Trigger erlaubt, vergleichen Sie Ihren Anwendungsfall mit [Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/) mit entsprechenden Zeitplan- und Wiederzulassungseinstellungen.

### Warum geht ein Test-Push an die falsche App, aber Live-Sends sehen korrekt aus? {#why-does-a-test-push-go-to-the-wrong-app-but-live-sends-look-correct}

**Test-Push** auf einem Nutzerprofil wird an jedes Push-fähige Gerät für dieses Profil zugestellt. Wenn mehrere Apps auf einem Gerät installiert sind, liefert das Betriebssystem die Testbenachrichtigung in der Regel an die erste verfügbare App, die möglicherweise nicht die App ist, die Sie validieren möchten.

Um app-spezifisches Targeting zu bestätigen, senden Sie eine Live- oder Testnachricht über eine Campaign oder ein Canvas mit einer engen Zielgruppe (zum Beispiel nach `external_id` filtern), anstatt sich allein auf **Test-Push** im Profil zu verlassen.

Für **Canvas**-Nachrichten-Schritte mit mehreren Apps aktivieren Sie **Zielgruppe beim Nachrichtenversand validieren** im Nachrichten-Schritt, damit Segment- und Filterprüfungen zum Sendezeitpunkt ausgeführt werden. Weitere Informationen finden Sie unter [Nachrichten-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/).

Allgemeine Informationen zum Test-Push-Verhalten finden Sie unter [Testnachrichten senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/) und [Push-FAQ]({{site.baseurl}}/user_guide/channels/push/faqs/).

### Wie debugge ich Push Stories auf iOS und Android? {#how-do-i-debug-push-stories-on-ios-and-android}

Beginnen Sie mit [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories/) für Einrichtungs- und Kreativanforderungen. Für Implementierung und Rich-Benachrichtigungsverarbeitung siehe [Rich-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/rich/) und [Push Stories]({{site.baseurl}}/developer_guide/push_notifications/push_stories/) im Entwicklerhandbuch.

### Wer erhält die E-Mail „Canvas Messages Delayed 24+ Hours“? {#who-receives-the-canvas-messages-delayed-24-hours-email}

Braze sendet diese Benachrichtigung, wenn Canvas-Nachrichten durch Rate-Limiting um 24 Stunden oder mehr verzögert werden. Die E-Mail geht an Dashboard-Nutzer:innen, die zuvor Änderungen am betroffenen Canvas vorgenommen haben (basierend auf den Canvas-Änderungsprotokollen). Wenn Braze diese Empfänger:innen nicht ermitteln kann, geht die E-Mail an die **Unternehmensadministrator:innen** des Workspace.