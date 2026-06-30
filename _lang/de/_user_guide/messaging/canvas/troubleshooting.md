---
nav_title: Fehlerbehebung
article_title: Fehlerbehebung für Canvases
page_order: 7
page_type: reference
description: "Diagnostizieren Sie Probleme beim Canvas-Eintritt, beim Senden und bei Analytics mithilfe eines standardisierten Untersuchungspfads, eines Symptomindex und Links zum Messaging-Verlauf und zum Messaging-Diagnostics-Dashboard."
tool: Canvas
---

# Fehlerbehebung für Canvases {#troubleshoot-canvases}

> Verwenden Sie diese Seite, um Probleme beim Canvas-Eintritt, beim Senden und bei Analytics zu diagnostizieren. Definitionen und weiterführende Informationen finden Sie in den [Canvas-FAQ]({{site.baseurl}}/user_guide/messaging/canvas/faqs).

{% alert note %}
**Messaging-Verlauf** und **Messaging-Diagnostics**-Protokolle sind bis zu **30 Tage** ab dem Ereignis verfügbar. Kontaktieren Sie den [Braze-Support]({{site.baseurl}}/braze_support) innerhalb dieses Zeitraums, wenn Sie Hilfe bei der Untersuchung eines bestimmten Vorfalls benötigen.
{% endalert %}

## Hier starten: Symptom zuordnen {#start-here-match-your-symptom}

| Symptom | Gehe zu |
| --- | --- |
| Ein:e Nutzer:in ist nicht in den Canvas eingetreten | [Nutzer:in ist nicht in den Canvas eingetreten](#user-didnt-enter-the-canvas) |
| Ein:e Nutzer:in ist eingetreten, hat aber keine Nachricht oder keinen Schritt erhalten | [Nutzer:in hat keine Canvas-Nachricht oder keinen Canvas-Schritt erhalten](#user-didnt-receive-a-canvas-message-or-step) |
| Niemand oder weniger Nutzer:innen als erwartet sind eingetreten | [Niedrige oder keine Canvas-Eintritte](#low-or-zero-canvas-entries) |
| Sendungen oder Zustellungen sind niedriger als die geschätzte Zielgruppe | [Weniger Sendungen als erwartet](#lower-sends-than-expected) |
| Canvas-Analytics sehen falsch aus (Kontrollgruppe, Conversions, null Sendungen) | [Canvas-Analytics-Abweichungen](#canvas-analytics-mismatches) |
| Canvas lässt sich nicht speichern oder der Editor friert ein | [Editor- und Speicherprobleme](#editor-and-save-issues) |
| Ich habe den Canvas gestoppt, aber es wurden trotzdem Nachrichten gesendet | [Verhalten bei gestopptem Canvas](#stopped-canvas-behavior) |
| Fehler „Zu viele Canvas-Branches“ beim Starten | [Fehler „Zu viele Canvas-Branches“](#too-many-canvas-branches-error) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canvas-Symptom" }

## Standardmäßiger Untersuchungspfad {#standard-investigation-path}

Verwenden Sie diesen Workflow, um ein Problem für eine:n bestimmte:n Nutzer:in oder ein aggregiertes Sendeproblem zu untersuchen. Beginnen Sie bei jedem Vorfall mit Schritt 1.

1. Bestätigen Sie, dass der Canvas aktiv ist (nicht Entwurf, gestoppt oder archiviert).
2. Bestätigen Sie, dass der Entry-Zeitplan (geplantes Fenster, Zeitzone, aktionsbasierter Trigger oder API-getriggerter Eintritt) mit dem Zeitpunkt übereinstimmt, zu dem Sie den Eintritt von Nutzer:innen erwarten.
3. Überprüfen Sie den Messaging-Verlauf einer Nutzerin oder eines Nutzers, indem Sie zu **Zielgruppe** > **Nutzer:innen suchen** gehen, das Profil öffnen und **Messaging-Verlauf** (letzte 30 Tage) auswählen.
   - Wenn kein Eintrag für den erwarteten Sendezeitpunkt vorhanden ist, liegt das Problem beim Eintritt, nicht bei der Nachricht. Gehen Sie zu [Nutzer:in ist nicht in den Canvas eingetreten](#user-didnt-enter-the-canvas).
4. Überprüfen Sie den Canvas-**Changelog** und die Changelogs aller beim Targeting verwendeten Segmente. Bestätigen Sie, dass die Zielgruppe, die Schritte oder die Sendeeinstellungen während des Vorfalls nicht geändert wurden.
5. Überprüfen Sie die aggregierten Ergebnisse auf der Canvas-Analytics-Seite, indem Sie das [Messaging-Diagnostics-Dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) öffnen und Abbruch- und Verwerfungsgründe prüfen.
   - Wenn Sie ein Ergebnis sehen, das Sie nicht erkennen, lesen Sie [Abbruch-Ergebnisse]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard#abort-outcomes) in der Diagnostics-Dokumentation.
   - Wenn ein Schritt null Eintritte (nicht null Sendungen) anzeigt, überprüfen Sie den vorherigen Schritttyp ([Aktionspfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths), [Verzögerung]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step), [Zielgruppenpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) oder [Decision-Split]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split)).
6. Wenn Sie weiterhin nicht weiterkommen, kontaktieren Sie den [Braze-Support]({{site.baseurl}}/braze_support) innerhalb von 30 Tagen mit der Canvas-ID, den betroffenen Nutzer-IDs, Zeitstempeln (mit Zeitzone) und Screenshots aus dem Messaging-Verlauf oder Messaging-Diagnostics.

Verwenden Sie vor dem Start [Test-Canvases senden]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases) und [Nutzerpfade in der Vorschau anzeigen]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths), um Ihr Setup zu validieren.

## Nutzer:in ist nicht in den Canvas eingetreten {#user-didnt-enter-the-canvas}

**Symptom:** Ein:e Nutzer:in ist nicht wie erwartet in den Canvas eingetreten, oder es sind weniger Nutzer:innen eingetreten, als Ihre Trigger-Events vermuten lassen.

Nutzer:innen müssen die **Zielgruppe** erfüllen, bevor Braze den Entry-Trigger auswertet (mit Ausnahme von [Änderung eines Attributs]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)-Triggern). Ein Trigger allein garantiert keinen Eintritt, wenn die Nutzerin oder der Nutzer zum Zeitpunkt der Auswertung nicht zur Zielgruppe gehörte.

Wiedereintritts-Berechtigung und Wiedereintritt sind separate Steuerungen unter [Eingangs-Einstellungen auswählen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls):

- **Wiedereintritts-Berechtigung:** Bestimmt, ob ein:e Nutzer:in nach dem Verlassen erneut in den Canvas eintreten darf (Zeitfenster und Einstellung **Nutzer:innen den Wiedereintritt in den Canvas erlauben**).
- **Wiedereintritt:** Bestimmt, ob ein:e Nutzer:in, die/der sich derzeit im Canvas befindet, einen parallelen Pfad betreten kann.

Ein:e Nutzer:in kann wiedereintritts-berechtigt sein, aber blockiert werden, weil sie/er sich noch im Canvas befindet, oder kann den Canvas verlassen haben, sich aber noch außerhalb des Wiedereintritts-Berechtigungsfensters befinden. Überprüfen Sie beide Einstellungen, wenn ein:e Nutzer:in nicht erneut in einen Canvas eintritt.

Überprüfen Sie Folgendes:

- **Entry-Zeitplan und Zeitzone:** Bestätigen Sie, dass der Canvas aktiv war und die Nutzerin oder der Nutzer den Trigger während des [Entry-Fensters]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule) ausgeführt hat.
- **Zielgruppe zum Zeitpunkt der Auswertung:** Überprüfen Sie die Segment- und Filter-Changelogs. [Nutzersuche]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) kann bei einigen Filtertypen falsch-positive Ergebnisse anzeigen (z. B. als String formatierte Datumsattribute).
- **Entry-Obergrenzen:** [Maximale Eintritte]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) oder Zielgruppen-Obergrenzen wurden möglicherweise erreicht.
- **Globale Kontrollgruppe:** Nutzer:innen in der [globalen Kontrollgruppe]({{site.baseurl}}/user_guide/audience/global_control_group) treten nicht in Messaging-Canvases ein.
- **Canvas-Kontrollgruppe:** Nutzer:innen, die beim Eintritt der Canvas-Kontrollgruppe zugewiesen werden, erhalten keine Varianten-Nachrichten. Die Variantenzuweisung erfolgt beim Eintritt, nicht durch Segmentfilter. Siehe [Canvas-Analytics-Abweichungen](#canvas-analytics-mismatches).
- **Ausstiegskriterien:** Die Nutzerin oder der Nutzer hat möglicherweise die [Ausstiegskriterien]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria) vor oder während des Eintritts erfüllt. Wenn Eintritt und Ausstieg dasselbe Event verwenden, siehe [Übereinstimmende Eintritts- und Ausstiegskriterien]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/matching_entry_and_exit_criteria).
- **API-getriggerter Eintritt:** Bestätigen Sie, dass die Nutzerin oder der Nutzer mit dem [`/canvas/trigger/send`-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) hinzugefügt wurde. Sie können [ein Segment erstellen]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) mit einem Canvas-Eintrittsfilter und Nutzer:innen mit [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) exportieren.

### Trigger-Event-Anzahl ist höher als Canvas-Eintritte {#trigger-event-count-is-higher-than-canvas-entries}

**Symptom:** Das Trigger-Event-Volumen ist höher als die Canvas-Eintrittsanzahl.

Braze dedupliziert mehrere Eintrittsversuche, die im selben Moment stattfinden, sodass Sie möglicherweise weniger Canvas-Eintritte als Trigger-Events sehen. Zum Testen mehrerer Eintritte sollten Trigger-Events mindestens eine Sekunde auseinander liegen.

Wenn ein:e Nutzer:in denselben Trigger innerhalb einer Sekunde mehrfach ausführt, verarbeitet Braze nur einen Eintritt. Überprüfen Sie Messaging-Diagnostics auf Ergebnisse wie **Nutzer:in nicht wiedereintritts-berechtigt**, wenn Wiedereintritts- oder Wiedereintritts-Berechtigungsregeln gelten.

{% details Zeitumstellung und täglich geplante Canvases %}

An Tagen mit Zeitumstellung (Sommer-/Winterzeit) können täglich geplante Canvases bis zu eine Stunde früher oder später als üblich ausgeführt werden. Wenn Ihre Eintrittskriterien auf angepassten Attributen oder Events mit Zeitstempeln basieren, die innerhalb einer Stunde der geplanten Eintrittszeit liegen, qualifizieren sich Nutzer:innen am Tag der Zeitumstellung möglicherweise noch nicht, da das Attribut oder Event noch nicht protokolliert wurde.

Angenommen, Nutzer:innen erhalten typischerweise ein Update eines angepassten Attributs um 15:00 Uhr in der Zeitzone Ihres Canvas, und Ihr Canvas läuft täglich um 15:30 Uhr in derselben Zeitzone. An einem Tag mit Vorstellung der Uhr (Sommerzeit) kann der Canvas die Nutzer:innen bis zu eine Stunde früher als üblich relativ zu diesem Attribut-Update auswerten – bevor das Attribut protokolliert wurde. Wenn die Wiedereintritts-Berechtigung deaktiviert ist, können Nutzer:innen, die an vorherigen Tagen eingetreten sind, nicht erneut eintreten, was zu null Eintritten für diesen Tag führt.

Um dies zu vermeiden, stellen Sie sicher, dass Ihre Updates für angepasste Attribute oder Events mehr als eine Stunde vor der geplanten Eintrittszeit des Canvas erfolgen.

{% enddetails %}

## Nutzer:in hat keine Canvas-Nachricht oder keinen Canvas-Schritt erhalten {#user-didnt-receive-a-canvas-message-or-step}

**Symptom:** Ein:e Nutzer:in ist in den Canvas eingetreten, hat aber die erwartete Nachricht oder den erwarteten Schritt nicht erhalten.

Überprüfen Sie den [**Messaging-Verlauf**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#messaging-history-tab) der Nutzerin oder des Nutzers für den Canvas-Schritt und den Zeitstempel. Wenn kein Eintrag vorhanden ist, kehren Sie zu [Nutzer:in ist nicht in den Canvas eingetreten](#user-didnt-enter-the-canvas) zurück.

Überprüfen Sie dann Folgendes nach Trigger- oder Schritttyp:

- **Angepasste Events oder Kauf-Trigger:** Bestätigen Sie, dass das Event unter **Analytics** > **Bericht zu angepassten Events** (oder **Umsatz** für Käufe) angezeigt wird. Vergleichen Sie den Event-Zeitstempel mit dem Zeitpunkt, zu dem der Canvas live ging, und mit einer eventuellen geplanten Verzögerung des Schritts.
- **API-getriggerter Eintritt:** Bestätigen Sie den Eintritt mit einem Canvas-Segmentfilter und Export, wie unter [Nutzer:in ist nicht in den Canvas eingetreten](#user-didnt-enter-the-canvas) beschrieben.
- **Aktionspfade oder Nachrichten-Schritt-Trigger:** Bestätigen Sie, dass die Nutzerin oder der Nutzer das erforderliche Event ausgeführt hat und dass [Event-Eigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#event-properties) im Schritt verfügbar sind.
- **In-App-Nachrichten-Schritte:** In-App-Nachrichten werden beim nächsten Sitzungsstart gesendet, nachdem die Nutzerin oder der Nutzer den Schritt betreten hat, und nur durch SDK-Events (nicht über die REST API). Siehe [Wann werden In-App-Nachrichten in Canvas gesendet?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#when-are-in-app-messages-in-canvas-sent) in den Canvas-FAQ.
- **Canvas-Kontrollgruppe:** Überprüfen Sie, ob die Nutzerin oder der Nutzer beim Eintritt der Canvas-Kontrollgruppe zugewiesen wurde.
- **Kanalberechtigung und Sendeeinstellungen:** Bestätigen Sie den Abo-Status, den Push-Aktivierungsstatus und die [Sendeeinstellungen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-14-select-your-send-settings) pro Schritt (z. B. **Abo-Einstellungen** auf nur angemeldete Nutzer:innen gesetzt). Fügen Sie keine Einzelkanal-Filter zur **Zielgruppe** bei Multi-Channel-Canvases hinzu.
- **Zustellungsvalidierungen:** Wenn Sie **Zielgruppe bei Nachrichtenversand validieren** in einem Nachrichten-Schritt aktiviert haben, erhalten Nutzer:innen, die zum Sendezeitpunkt nicht mehr den Filtern entsprechen, die Nachricht nicht. Siehe [Zustellungsvalidierungen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations).
- **Ruhezeiten, intelligentes Timing, Häufigkeitsbegrenzungen und Rate-Limits:** Diese können Sendungen verzögern, unterdrücken oder abbrechen. Nutzer:innen können nach einem Ruhezeiten-Abbruch weiterhin im Canvas verbleiben.
- **Race-Conditions:** Wenn die Nutzerin oder der Nutzer mehrere Aktionen gleichzeitig getriggert hat, siehe [Race-Conditions]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions).

{% alert important %}
Wenn ein Canvas-Nachrichten-Schritt eine Sendung abbricht, rückt die Nutzerin oder der Nutzer trotzdem zum nächsten Schritt vor. Canvas rückt bei Abbruch vor, damit nachfolgende Verzögerungs- und Aktionspfad-Schritte nicht dauerhaft blockiert werden. Siehe [Wie Nutzer:innen vorrücken]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance) und [Abbruch-Ergebnisse]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard#abort-outcomes).
{% endalert %}

Informationen zu Filtern auf Schrittebene, Konflikten zwischen Branches und dem Verzweigungsverhalten von In-App-Nachrichten finden Sie unter [Mit Canvas Flow starten – Fehlerbehebung]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/launching_canvas_flow#troubleshooting) und in den [Canvas-FAQ]({{site.baseurl}}/user_guide/messaging/canvas/faqs#messages-and-delivery).

{% alert important %}
Wenn Ihr aktionsbasierter Canvas Nachrichten früher als erwartet sendet, überprüfen Sie, ob der Zeitstempel Ihres angepassten Events die aktuelle Uhrzeit verwendet und nicht eine zurückdatierte Uhrzeit. Braze berechnet Verzögerungen ab dem Zeitstempel, der mit dem Event gesendet wird. Siehe [Aktionsbasierte Zustellung]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule).
{% endalert %}

## Niedrige oder keine Canvas-Eintritte {#low-or-zero-canvas-entries}

**Symptom:** Niemand oder weniger Nutzer:innen als erwartet sind in den Canvas eingetreten.

Beginnen Sie mit der [Checkliste für den Start mit Canvas Flow]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/launching_canvas_flow#launch-checklist) und bestätigen Sie dann:

- Der Canvas ist aktiv und die aktuelle Uhrzeit liegt innerhalb des geplanten Entry-Fensters.
- Die [Eingangs-Einstellungen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) (Wiedereintritts-Berechtigung, maximale Eintritte und Entry-Obergrenzen) erlauben den Eintritt der erwarteten Nutzer:innen.
- Die Zielgruppe und die Segmentfilter stimmen nach dem Start noch mit den erwarteten Nutzer:innen überein.
- Die Prozentsätze der globalen und Canvas-Kontrollgruppe zeigen, welcher Anteil der Nutzer:innen in welchen Pfad eintritt und welcher Anteil Nachrichten erhält.
- Workspace-Rate-Limits oder Entry-Warteschlangen können Verzögerungen zwischen dem Zeitpunkt, zu dem sich Nutzer:innen qualifizieren, und dem Zeitpunkt, zu dem sie eintreten oder in einen Schritt vorrücken, verursachen.

Für eine:n einzelne:n Nutzer:in folgen Sie dem [standardmäßigen Untersuchungspfad](#standard-investigation-path). Für zeitumstellungsbedingte Null-Eintritte siehe den aufklappbaren Abschnitt unter [Nutzer:in ist nicht in den Canvas eingetreten](#user-didnt-enter-the-canvas).

## Weniger Sendungen als erwartet {#lower-sends-than-expected}

**Symptom:** Sendungen oder Zustellungen sind niedriger als die geschätzte Zielgruppe eines Canvas-Schritts.

Häufige Ursachen sind die Neubewertung der Zielgruppe zum Sendezeitpunkt, Kanalberechtigung, Kontrollgruppen, Ruhezeiten, intelligentes Timing, Rate-Limits und das Zustellungsverhalten von In-App-Nachrichten (null _Sendungen_ mit Impressionen ist bei In-App-Nachrichten erwartetes Verhalten).

Eine detaillierte Liste finden Sie unter [Warum sind die Sendungen niedriger als die geschätzte Zielgruppengröße?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#why-are-sends-lower-than-the-estimated-audience-size) in den Canvas-FAQ und [Warum sind die Sendungen niedriger als die geschätzte Zielgruppengröße?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#why-are-sends-lower-than-the-estimated-audience-size) für Campaigns.

Verwenden Sie das [Messaging-Diagnostics-Dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard), um Abbruch- und Verwerfungsgründe auf Schrittebene einzusehen.

## Canvas-Analytics-Abweichungen {#canvas-analytics-mismatches}

**Symptom:** Canvas-Analytics sehen falsch aus (Kontrollgruppen-Aufteilung, Conversions oder null Sendungen).

Die Zuweisung zu Kontrollgruppe und Variante erfolgt beim Canvas-Eintritt basierend auf den Prozentsätzen, die Sie im Builder festgelegt haben – nicht durch Segmentfilter. Nutzer:innen, die einen bestimmten Kanal nicht empfangen können, können trotzdem in eine Variante eintreten. Verwenden Sie die [Sendeeinstellungen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-14-select-your-send-settings) pro Schritt, um zu steuern, wer welchen Nachrichtentyp erhält, anstatt die **Zielgruppe** mit Kanalfiltern einzuschränken.

Unterscheiden Sie die Canvas-Kontrollgruppe von der [globalen Kontrollgruppe]({{site.baseurl}}/user_guide/audience/global_control_group). Für Filterdefinitionen siehe [Was ist der Unterschied zwischen „Hat keine Canvas-Variante betreten“ und „Ist nicht in der Canvas-Kontrollgruppe“?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-is-the-difference-between-has-not-entered-canvas-variation-and-is-not-in-canvas-control-group) in den Canvas-FAQ.

{% details Warum Varianten-Sendungen niedriger als der Varianten-Prozentsatz sein können %}

Stellen Sie sich folgendes Szenario vor:

- Ein Canvas hat eine einzelne Variante und eine Kontrollgruppe.
- Der erste Schritt der Variante ist eine Push-Benachrichtigung.
- 90 % der Nutzer:innen wurden ausgewählt, um in die Variante einzutreten, und 10 %, um in die Kontrollgruppe einzutreten.

![Canvas-Beispiel mit 90 % Variante und 10 % Kontrollgruppe.]({% image_buster /assets/img_archive/trouble15.png %})

In diesem Szenario treten 90 % der Nutzer:innen, die in den Canvas eintreten, in die Variante ein.

Wenn Sie sich das Segment der aktiven Nutzer:innen ansehen, können Sie feststellen, dass es zwar 29,8k Nutzer:innen enthält, aber nur 64 % von ihnen Push-aktiviert sind:

![Segment mit dem Filter „Push Enabled“ auf „true“ gesetzt und geschätzten 29,8k Nutzer:innen.]({% image_buster /assets/img_archive/trouble16.png %})

Das bedeutet, dass obwohl Sie festgelegt haben, dass 90 % der Nutzer:innen in die Variante eintreten sollen, nicht alle dieser Nutzer:innen eine Push-Benachrichtigung empfangen können. Nutzer:innen, die keine Push-Benachrichtigung empfangen können, treten trotzdem in die Variante ein – die Sendeanzahl spiegelt die Kanalberechtigung im Schritt wider, nicht die Variantenzuweisung beim Eintritt.

{% enddetails %}

Informationen zu Konversionsraten-Definitionen und Analytics auf Schrittebene finden Sie unter [Analytics und Conversions]({{site.baseurl}}/user_guide/messaging/canvas/faqs#analytics-and-conversions) in den Canvas-FAQ.

## Editor- und Speicherprobleme {#editor-and-save-issues}

**Symptom:** Der Canvas-Editor lädt nicht, friert ein oder speichert Ihre Änderungen nicht.

| Symptom | Wahrscheinlichste Ursache |
| --- | --- |
| Speichern-Button dreht sich endlos ohne Fehlermeldung | Leerer oder unvollständiger Filter für angepasste Attribute in der Canvas-Zielgruppe oder einem Schrittfilter – entfernen Sie den Filter oder wählen Sie ein gültiges Attribut aus |
| Fehler „Request Timed Out“ beim Bearbeiten | Störung durch Browser-Erweiterungen, Werbeblocker oder eine abgelaufene Sitzung – versuchen Sie es in einem Inkognito-Fenster oder einem anderen Browser |
| Speichern nach dem Archivieren einer Variante nicht möglich | Eine archivierte Variante wird weiterhin nachgelagert referenziert; überprüfen Sie die Schrittverbindungen und stellen Sie die Variante wieder her oder ersetzen Sie sie |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Editor-Symptom" }

Wenn der Editor bei einem großen oder komplexen Canvas einfriert, versuchen Sie Folgendes:

- Leeren Sie den Browser-Cache und die Cookies und laden Sie die Seite neu. Unternehmens-Werbeblocker oder Browser-Erweiterungen können die Braze-Plattform beeinträchtigen.
- Verwenden Sie die Canvas-Zoom-Steuerung, um die Ansicht auf 25 % oder 10 % zu reduzieren und die Menge an UI zu verringern, die der Browser rendern muss.
- Versuchen Sie es mit einem anderen Webbrowser.

Wenn der Canvas nicht lädt und nicht weiterkommt, wurde eine vorherige Version nicht korrekt gespeichert und enthält möglicherweise ungültige Schritte. Duplizieren Sie den Canvas über das Dashboard. Wenn das Problem weiterhin besteht, eröffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support).

Für „Request Timed Out“-Support-Tickets fügen Sie eine Bildschirmaufnahme, Zeitstempel und Zeitzone, Browser und Version, Schritte zur Reproduktion und optional ein HAR-Protokoll aus den Entwicklertools Ihres Browsers bei. Siehe [Was sollte ich bei einem Support-Ticket für einen „Request Timed Out“-Fehler angeben?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error) in den Canvas-FAQ.

## Verhalten bei gestopptem Canvas {#stopped-canvas-behavior}

**Symptom:** Sie haben den Canvas gestoppt, aber Nutzer:innen haben trotzdem Nachrichten erhalten.

Wenn Sie einen Canvas stoppen, können keine Nutzer:innen mehr eintreten und es werden keine weiteren Nachrichten aus dem Canvas-Flow gesendet. E-Mail-Sendungen, die bereits an Ihren E-Mail-Anbieter übergeben wurden, können nicht zurückgerufen werden.

Nutzer:innen, die auf einem Verzögerungs- oder Aktionspfad-Schritt warten, werden nicht automatisch aus der Journey entfernt, wenn Sie den Canvas stoppen. Wenn Sie den Canvas vor Ablauf der geplanten Sendezeit wieder aktivieren, erhalten sie möglicherweise noch ausstehende Schritte.

Alle Details finden Sie unter [Was passiert, wenn Sie einen Canvas stoppen?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-happens-when-you-stop-a-canvas) in den Canvas-FAQ.

## Fehler „Zu viele Canvas-Branches“ {#too-many-canvas-branches-error}

**Symptom:** Beim Starten eines geplanten Canvas wird der Fehler „Zu viele Canvas-Branches“ angezeigt.

Dieser Fehler erscheint, wenn die Kombination aus Schritt-Verzweigungen und der Größe der Entry-Zielgruppe zu Cluster-Performance-Problemen führen kann, die das Senden von Nachrichten verhindern. Braze zeigt diese Meldung an, wenn Sie einen Canvas mit geplantem Eintritt starten – nicht beim Speichern eines Entwurfs.

Um das Problem zu beheben:

- Reduzieren Sie die Schritt-Verzweigungen im Canvas.
- Reduzieren Sie die Größe der Entry-Zielgruppe.
- Verwenden Sie [Zielgruppenpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths), um Verzweigungen zu konsolidieren, anstatt viele parallele Pfade zu verwenden.
- Wenn Ihr Canvas den ursprünglichen Editor verwendet, [klonen Sie ihn zu Canvas Flow]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases) und bauen Sie ihn mit Canvas-Komponenten neu auf.

Wenn Sie den Canvas dennoch ohne Änderungen starten müssen und nicht zu Canvas Flow wechseln können, kontaktieren Sie den [Support]({{site.baseurl}}/support_contact).

## Wann Sie den Support kontaktieren sollten {#when-to-contact-support}

Kontaktieren Sie den [Braze-Support]({{site.baseurl}}/braze_support) innerhalb von 30 Tagen nach dem Auftreten des Problems, wenn Sie den [standardmäßigen Untersuchungspfad](#standard-investigation-path) abgeschlossen haben und weiterhin Hilfe benötigen.

Geben Sie Folgendes an:

- Canvas-ID und betroffene Nutzer-IDs (externe ID oder Braze-ID)
- Zeitstempel mit Zeitzone
- Screenshots oder Exporte aus **Messaging-Verlauf** oder **Messaging-Diagnostics**
- Für „Request Timed Out“-Fehler im Editor die unter [Editor- und Speicherprobleme](#editor-and-save-issues) aufgeführten Details