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
| Eine:r Nutzer:in ist nicht in den Canvas eingetreten | [Nutzer:in ist nicht in den Canvas eingetreten](#user-didnt-enter-the-canvas) |
| Eine:r Nutzer:in ist eingetreten, hat aber keine Nachricht oder keinen Schritt erhalten | [Nutzer:in hat keine Canvas-Nachricht oder keinen Canvas-Schritt erhalten](#user-didnt-receive-a-canvas-message-or-step) |
| Niemand oder weniger Nutzer:innen als erwartet sind eingetreten | [Niedrige oder keine Canvas-Eintritte](#low-or-zero-canvas-entries) |
| Sendungen oder Zustellungen sind niedriger als die geschätzte Zielgruppe | [Weniger Sendungen als erwartet](#lower-sends-than-expected) |
| Canvas-Analytics sehen falsch aus (Kontrollgruppe, Konversionen, null Sendungen) | [Abweichungen in Canvas-Analytics](#canvas-analytics-mismatches) |
| Analytics zeigen weit mehr Sendungen als Eintritte oder mehr Exits als Eintritte | [Datumsbereichsfilterung kann unerwartete Zahlen anzeigen](#date-range-filtering-can-show-unexpected-numbers) |
| Canvas lässt sich nicht speichern oder der Editor friert ein | [Editor- und Speicherprobleme](#editor-and-save-issues) |
| Ich habe den Canvas gestoppt, aber es wurden trotzdem Nachrichten gesendet | [Verhalten bei gestopptem Canvas](#stopped-canvas-behavior) |
| Fehler „Too many Canvas branches“ beim Starten | [Fehler „Too many Canvas branches“](#too-many-canvas-branches-error) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canvas-Symptom" }

## Standardmäßiger Untersuchungspfad {#standard-investigation-path}

Verwenden Sie diesen Workflow, um ein Problem bei einer:m bestimmten Nutzer:in oder bei einem aggregierten Versand zu untersuchen. Beginnen Sie bei jedem Vorfall mit Schritt 1.

1. Bestätigen Sie, dass der Canvas aktiv ist (nicht im Entwurf, gestoppt oder archiviert).
2. Bestätigen Sie, dass der Entry-Zeitplan (geplantes Zeitfenster, Zeitzone, aktionsbasierter Trigger oder API-gesteuerter Entry) mit dem erwarteten Eintrittszeitpunkt der Nutzer:innen übereinstimmt.
3. Überprüfen Sie den Nachrichtenverlauf einer:s Nutzer:in, indem Sie zu **Audience** > **Search users** navigieren, das Profil öffnen und **Messaging History** (letzte 30 Tage) auswählen.
   - Wenn für den erwarteten Sendezeitpunkt kein Eintrag vorhanden ist, liegt das Problem beim Entry, nicht bei der Nachricht. Gehen Sie zu [Nutzer:in ist nicht in den Canvas eingetreten](#user-didnt-enter-the-canvas).
4. Überprüfen Sie den Canvas-**Changelog** und die Changelogs aller Segmente, die beim Targeting verwendet werden. Bestätigen Sie, dass die Zielgruppe, die Schritte oder die Sendeeinstellungen während des Vorfalls nicht geändert wurden.
5. Überprüfen Sie die aggregierten Ergebnisse auf der Canvas-Analytics-Seite, indem Sie das [Messaging Diagnostics Dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) öffnen und die Abbruch- und Verwerfungsgründe prüfen.
   - Wenn Sie ein Ergebnis sehen, das Sie nicht zuordnen können, lesen Sie [Abbruchergebnisse]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard#abort-outcomes) in der Diagnostik-Dokumentation.
   - Wenn ein Canvas-Schritt null Eintritte (nicht null Sendungen) anzeigt, überprüfen Sie den vorherigen Schritttyp ([Aktionspfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths), [Verzögerung]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step), [Zielgruppenpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) oder [Decision-Split]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split)).
6. Wenn Sie weiterhin nicht weiterkommen, kontaktieren Sie den [Braze-Support]({{site.baseurl}}/braze_support) innerhalb von 30 Tagen mit der Canvas-ID, den betroffenen Nutzer-IDs, Zeitstempeln (mit Zeitzone) und Screenshots aus Messaging History oder Messaging Diagnostics.

Verwenden Sie vor dem Start [Test-Canvases senden]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases) und [Nutzerpfade in der Vorschau anzeigen]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths), um Ihr Setup zu validieren.

## Nutzer:in ist nicht in den Canvas eingetreten {#user-didnt-enter-the-canvas}

**Symptom:** Eine:r Nutzer:in ist nicht wie erwartet in den Canvas eingetreten, oder es sind weniger Nutzer:innen eingetreten, als Ihre Trigger-Events vermuten lassen.

Nutzer:innen müssen der **Zielgruppe** entsprechen, bevor Braze den Entry-Trigger auswertet (mit Ausnahme von [Attributänderungs]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)-Triggern). Ein Trigger allein garantiert keinen Entry, wenn die:der Nutzer:in zum Zeitpunkt der Auswertung nicht zur Zielgruppe gehörte.

Wiederberechtigung und Wiedereintritt sind separate Einstellungen unter [Entry-Kontrollen auswählen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls):

- **Wiederberechtigung:** Bestimmt, ob eine:r Nutzer:in nach dem Verlassen des Canvas erneut eintreten darf (Zeitfenster und Einstellung **Nutzer:innen den Wiedereintritt in den Canvas erlauben**).
- **Wiedereintritt:** Bestimmt, ob eine:r Nutzer:in, die:der sich derzeit im Canvas befindet, einen parallelen Pfad betreten kann.

Eine:r Nutzer:in kann wiederberechtigt sein, aber blockiert werden, weil sie:er sich noch im Canvas befindet, oder sie:er kann den Canvas verlassen haben, sich aber noch außerhalb des Wiederberechtigungsfensters befinden. Überprüfen Sie beide Einstellungen, wenn eine:r Nutzer:in nicht erneut in einen Canvas eintritt.

Überprüfen Sie Folgendes:

- **Entry-Zeitplan und Zeitzone:** Bestätigen Sie, dass der Canvas aktiv war und die:der Nutzer:in den Trigger während des [Entry-Fensters]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule) ausgelöst hat.
- **Zielgruppe zum Zeitpunkt der Auswertung:** Überprüfen Sie die Änderungsprotokolle von Segmenten und Filtern. [Nutzersuche]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) kann bei einigen Filtertypen falsch positive Ergebnisse anzeigen (z. B. als String formatierte Datumsattribute).
- **Entry-Limits:** [Maximale Eintritte]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) oder Zielgruppen-Limits wurden möglicherweise erreicht.
- **Globale Kontrollgruppe:** Nutzer:innen in der [globalen Kontrollgruppe]({{site.baseurl}}/user_guide/audience/global_control_group) treten nicht in Messaging-Canvases ein.
- **Canvas-Kontrollgruppe:** Nutzer:innen, die beim Entry der Canvas-Kontrollgruppe zugewiesen werden, erhalten keine Varianten-Nachrichten. Die Variantenzuweisung erfolgt beim Entry, nicht über Segmentfilter. Siehe [Abweichungen in Canvas Analytics](#canvas-analytics-mismatches).
- **Exit-Kriterien:** Die:der Nutzer:in hat möglicherweise die [Exit-Kriterien]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria) vor oder während des Entry erfüllt. Wenn Entry und Exit dasselbe Event verwenden, siehe [Übereinstimmende Entry- und Exit-Kriterien]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/matching_entry_and_exit_criteria).
- **API-getriggerter Entry:** Bestätigen Sie, dass die:der Nutzer:in über den [`/canvas/trigger/send`-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) hinzugefügt wurde. Sie können [ein Segment erstellen]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) mit einem Canvas-Entry-Filter und Nutzer:innen mit [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) exportieren.

### Trigger-Event-Anzahl ist höher als Canvas-Eintritte {#trigger-event-count-is-higher-than-canvas-entries}

**Symptom:** Das Trigger-Event-Volumen ist höher als die Anzahl der Canvas-Eintritte.

Braze dedupliziert mehrere Entry-Versuche, die im selben Moment stattfinden, sodass Sie möglicherweise weniger Canvas-Eintritte als Trigger-Events sehen. Um mehrere Eintritte zu testen, planen Sie Trigger-Events mit mindestens einer Sekunde Abstand.

Wenn eine:r Nutzer:in denselben Trigger innerhalb einer Sekunde mehrmals auslöst, verarbeitet Braze nur einen Entry. Überprüfen Sie die Messaging-Diagnose auf Ergebnisse wie **Nutzer:in nicht wiederberechtigt**, wenn Wiedereintritts- oder Wiederberechtigungsregeln gelten.

{% details Sommerzeit und täglich geplante Canvases %}

An Tagen mit Sommerzeitumstellung können täglich geplante Canvases bis zu einer Stunde früher oder später als üblich ausgeführt werden. Wenn Ihre Entry-Kriterien auf angepassten Attributen oder Events mit Zeitstempeln basieren, die innerhalb einer Stunde der geplanten Entry-Zeit liegen, qualifizieren sich Nutzer:innen am Tag der Zeitumstellung möglicherweise noch nicht, weil das Attribut oder Event noch nicht protokolliert wurde.

Angenommen, Nutzer:innen erhalten typischerweise um 15:00 Uhr in der Zeitzone Ihres Canvas ein Update eines angepassten Attributs und Ihr Canvas läuft täglich um 15:30 Uhr in derselben Zeitzone. An einem Frühjahrs-Sommerzeitumstellungstag kann der Canvas Nutzer:innen bis zu eine Stunde früher als üblich relativ zu diesem Attribut-Update auswerten – bevor das Attribut protokolliert wurde. Wenn die Wiederberechtigung deaktiviert ist, können Nutzer:innen, die an vorherigen Tagen eingetreten sind, nicht erneut eintreten, was zu null Eintritten für diesen Tag führt.

Um dies zu vermeiden, stellen Sie sicher, dass Ihre Updates angepasster Attribute oder Events mehr als eine Stunde vor der geplanten Entry-Zeit des Canvas erfolgen.

{% enddetails %}

## Nutzer:in hat keine Canvas-Nachricht oder keinen Canvas-Schritt erhalten {#user-didnt-receive-a-canvas-message-or-step}

**Symptom:** Eine:r Nutzer:in ist in den Canvas eingetreten, hat aber die erwartete Nachricht oder den erwarteten Schritt nicht erhalten.

Überprüfen Sie den [**Nachrichtenverlauf**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#messaging-history-tab) der Nutzer:innen für den Canvas-Schritt und den Zeitstempel. Wenn kein Eintrag vorhanden ist, kehren Sie zu [Nutzer:in ist nicht in den Canvas eingetreten](#user-didnt-enter-the-canvas) zurück.

Überprüfen Sie dann Folgendes je nach Trigger- oder Schritttyp:

- **Angepasste Events oder Kauf-Trigger:** Bestätigen Sie, dass das Event unter **Analytics** > **Bericht zu angepassten Events** (oder **Umsatz** für Käufe) angezeigt wird. Vergleichen Sie den Event-Zeitstempel mit dem Zeitpunkt, zu dem der Canvas live ging, und mit einer eventuellen geplanten Verzögerung des Schritts.
- **API-getriggerter Entry:** Bestätigen Sie den Entry mit einem Canvas-Segment-Filter und -Export, wie unter [Nutzer:in ist nicht in den Canvas eingetreten](#user-didnt-enter-the-canvas) beschrieben.
- **Aktionspfade oder Nachrichten-Schritt-Trigger:** Bestätigen Sie, dass die Nutzer:innen das vorausgesetzte Event ausgeführt haben und dass [Event-Eigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#event-properties) im Schritt verfügbar sind.
- **In-App-Nachricht-Schritte:** In-App-Nachrichten werden beim nächsten Sitzungsstart gesendet, nachdem die Nutzer:innen den Schritt betreten haben, und nur über SDK-Events (nicht über die REST API). Siehe [Wann werden In-App-Nachrichten in Canvas gesendet?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#when-are-in-app-messages-in-canvas-sent) in den Canvas-FAQ.
- **Canvas-Kontrollgruppe:** Überprüfen Sie, ob die Nutzer:innen beim Entry nicht der Canvas-Kontrollgruppe zugewiesen wurden.
- **Kanalberechtigung und Sendeeinstellungen:** Bestätigen Sie den Abo-Status, den Push-Aktivierungsstatus und die [Sendeeinstellungen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-14-select-your-send-settings) pro Schritt (z. B. **Abo-Einstellungen** nur für Nutzer:innen mit Opt-in). Fügen Sie keine Einzelkanal-Filter zur **Zielgruppe** in Mehrkanalcanvases hinzu.
- **Zustellungsvalidierungen:** Wenn Sie **Zielgruppe beim Nachrichtenversand validieren** in einem Nachrichten-Schritt aktiviert haben, erhalten Nutzer:innen, die zum Sendezeitpunkt nicht mehr den Filtern entsprechen, die Nachricht nicht. Siehe [Zustellungsvalidierungen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations).
- **Ruhezeiten, intelligentes Timing, Frequency Caps und Rate-Limits:** Diese können Sendungen verzögern, unterdrücken oder abbrechen. Nutzer:innen können nach einem Abbruch durch Ruhezeiten weiterhin im Canvas verbleiben.
- **Race-Conditions:** Wenn die Nutzer:innen mehrere Aktionen gleichzeitig ausgelöst haben, siehe [Race-Conditions]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions).

{% alert important %}
Wenn ein Canvas-Nachrichten-Schritt einen Versand abbricht, rücken die Nutzer:innen trotzdem zum nächsten Schritt vor. Canvas rückt bei Abbruch vor, damit nachfolgende Verzögerungs- und Aktionspfad-Schritte nicht dauerhaft blockiert werden. Siehe [Wie Nutzer:innen vorrücken]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance) und [Abbruch-Ergebnisse]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard#abort-outcomes).
{% endalert %}

Informationen zu Filtern auf Schrittebene, Konflikten zwischen Branches und dem Branching-Verhalten von In-App-Nachrichten finden Sie unter [Mit Canvas Flow starten – Fehlerbehebung]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/launching_canvas_flow#troubleshooting) und in den [Canvas-FAQ]({{site.baseurl}}/user_guide/messaging/canvas/faqs#messages-and-delivery).

{% alert important %}
Wenn Ihr aktionsbasierter Canvas Nachrichten früher als erwartet sendet, überprüfen Sie, ob der Zeitstempel Ihres angepassten Events die aktuelle Uhrzeit verwendet und nicht eine rückdatierte Uhrzeit. Braze berechnet Verzögerungen anhand des mit dem Event gesendeten Zeitstempels. Siehe [Aktionsbasierte Zustellung]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule).
{% endalert %}

## Niedrige oder keine Canvas-Eintritte {#low-or-zero-canvas-entries}

**Symptom:** Keine oder weniger Nutzer:innen als erwartet sind in den Canvas eingetreten.

Beginnen Sie mit der [Checkliste für den Start mit Canvas Flow]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/launching_canvas_flow#launch-checklist) und überprüfen Sie dann Folgendes:

- Der Canvas ist aktiv und die aktuelle Uhrzeit liegt innerhalb des geplanten Entry-Fensters.
- Die [Entry-Einstellungen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) (erneute Berechtigung, maximale Eintritte und Entry-Limits) erlauben den Eintritt der erwarteten Nutzer:innen.
- Die Zielgruppe und die Segmentfilter stimmen auch nach dem Start noch mit den erwarteten Nutzer:innen überein.
- Die Prozentsätze der globalen Kontrollgruppe und der Canvas-Kontrollgruppe zeigen, welcher Anteil der Nutzer:innen in welchen Pfad eintritt und welcher Anteil Nachrichten erhält.
- Workspace-Rate-Limits oder Entry-Warteschlangen können erwartungsgemäß zu Verzögerungen zwischen dem Zeitpunkt, an dem Nutzer:innen sich qualifizieren, und dem Zeitpunkt, an dem sie eintreten oder in einen Schritt vorrücken, führen.

Für einzelne Nutzer:innen folgen Sie dem [standardmäßigen Untersuchungspfad](#standard-investigation-path). Für Null-Eintritte im Zusammenhang mit der Sommerzeit-/Winterzeitumstellung siehe den aufklappbaren Abschnitt unter [Nutzer:in ist nicht in den Canvas eingetreten](#user-didnt-enter-the-canvas).

## Weniger Sendungen als erwartet {#lower-sends-than-expected}

**Symptom:** Sendungen oder Zustellungen liegen unter der geschätzten Zielgruppe eines Canvas-Schritts.

Häufige Ursachen sind die erneute Zielgruppenbewertung zum Sendezeitpunkt, Kanalberechtigung, Kontrollgruppen, Ruhezeiten, intelligentes Timing, Rate-Limits und das Zustellverhalten von In-App-Nachrichten (null _Sendungen_ bei vorhandenen Impressionen ist bei In-App-Nachrichten erwartetes Verhalten).

Wenn ein Nachrichtenschritt viele eingetretene Nutzer:innen, aber wenige Sendungen anzeigt, prüfen Sie, ob Liquid `abort_message()` den Versand abgebrochen hat. Informationen zu Prüfungen im Nachrichtenaktivitätsprotokoll, fehlenden Attributen und Testsendungen finden Sie unter [Fehlerbehebung bei hohen Abbruchraten]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages#troubleshooting-high-abort-rates).

Eine ausführliche Liste finden Sie unter [Warum sind die Sendungen niedriger als die geschätzte Zielgruppengröße?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#why-are-sends-lower-than-the-estimated-audience-size) in den Canvas-FAQ und [Warum sind die Sendungen niedriger als die geschätzte Zielgruppengröße?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#why-are-sends-lower-than-the-estimated-audience-size) für Campaigns.

Verwenden Sie das [Messaging-Diagnostics-Dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard), um Abbruch- und Verwerfungsgründe auf Schrittebene einzusehen.

## Abweichungen in Canvas-Analytics {#canvas-analytics-mismatches}

**Symptom:** Canvas-Analytics sehen falsch aus (Kontrollgruppen-Aufteilung, Konversionen oder null Sendungen).

Die Zuweisung zu Kontrollgruppen und Varianten erfolgt beim Canvas-Eintritt basierend auf den Prozentsätzen, die Sie im Builder festgelegt haben – nicht über Segmentfilter. Nutzer:innen, die einen bestimmten Kanal nicht empfangen können, können trotzdem in eine Variante eintreten. Verwenden Sie die [Sendeeinstellungen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-14-select-your-send-settings) auf Schrittebene, um einzuschränken, wer welchen Nachrichtentyp erhält, anstatt die **Zielgruppe** mit Kanalfiltern einzugrenzen.

Unterscheiden Sie die Canvas-Kontrollgruppe von der [globalen Kontrollgruppe]({{site.baseurl}}/user_guide/audience/global_control_group). Filterdefinitionen finden Sie unter [Was ist der Unterschied zwischen „Has not entered Canvas variation“ und „Is not in Canvas control group“?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-is-the-difference-between-has-not-entered-canvas-variation-and-is-not-in-canvas-control-group) in den Canvas-FAQ.

{% details Warum die Sendungen einer Variante niedriger sein können als der Varianten-Prozentsatz %}

Stellen Sie sich folgendes Szenario vor:

- Ein Canvas hat eine einzelne Variante und eine Kontrollgruppe.
- Der erste Schritt der Variante ist eine Push-Benachrichtigung.
- 90 % der Nutzer:innen wurden ausgewählt, die Variante zu betreten, und 10 % die Kontrollgruppe.

![Canvas-Beispiel mit 90 % Variante und 10 % Kontrollgruppe.]({% image_buster /assets/img_archive/trouble15.png %})

In diesem Szenario betreten 90 % der Nutzer:innen, die in das Canvas eintreten, die Variante.

Wenn Sie sich das Segment der aktiven Nutzer:innen ansehen, werden Sie feststellen, dass es zwar 29,8k Nutzer:innen enthält, aber nur 64 % von ihnen Push-fähig sind:

![Segment mit dem Filter „Push Enabled“ auf „true“ gesetzt und geschätzten 29,8k Nutzer:innen.]({% image_buster /assets/img_archive/trouble16.png %})

Das bedeutet, dass nicht alle Nutzer:innen, die Sie zu 90 % in die Variante eingeteilt haben, eine Push-Benachrichtigung empfangen können. Nutzer:innen, die keine Push-Benachrichtigungen empfangen können, treten trotzdem in die Variante ein – die Sendeanzahl spiegelt die Kanalberechtigung auf Schrittebene wider, nicht die Variantenzuweisung beim Eintritt.

{% enddetails %}

### Datumsbereichsfilter können unerwartete Zahlen anzeigen {#date-range-filtering-can-show-unexpected-numbers}

**Symptom:** Canvas- oder Schritt-Analytics zeigen unerwartete oder unplausible Zahlen an, z. B. deutlich mehr Sendungen als Eintritte oder mehr Nutzer:innen, die einen Schritt verlassen, als ihn betreten haben.

Dies kann passieren, wenn Sie den Datumsbereichs-Kalenderfilter oben auf der Canvas-Analytics-Seite verwenden. Wenn Sie einen Datumsbereich auswählen, der einige Nutzeraktionen ausschließt, zeigen die angezeigten Metriken möglicherweise nur einen Teil der Journey jeder Nutzerin bzw. jedes Nutzers an.

Zum Beispiel:
- Sie sehen möglicherweise 100 Eintritte bei 8.000 Sendungen, wenn Ihr Datumsbereich nach dem Eintritt der meisten Nutzer:innen beginnt, aber den Zeitraum umfasst, in dem sie Nachrichten erhalten haben.
- Sie sehen möglicherweise mehr Nutzer:innen, die zum nächsten Schritt übergehen, als den vorherigen Schritt betreten haben, wenn Ihr Bereich nur die Exits, aber nicht die früheren Eintritte erfasst.

Um dies zu beheben, passen Sie den Datumsbereich so an, dass er entweder alle Daten vom Start des Canvas bis zur Gegenwart umfasst, oder wählen Sie einen Bereich, der den gesamten für die benötigten Metriken relevanten Zeitraum abdeckt.

Definitionen zu Konversionsraten und Analytics auf Schrittebene finden Sie unter [Analytics und Konversionen]({{site.baseurl}}/user_guide/messaging/canvas/faqs#analytics-and-conversions) in den Canvas-FAQ.

## Editor- und Speicherprobleme {#editor-and-save-issues}

**Symptom:** Der Canvas-Editor lädt nicht, friert ein oder speichert Ihre Änderungen nicht.

| Symptom | Wahrscheinlichste Ursache |
| --- | --- |
| Speicher-Button dreht sich endlos ohne Fehlermeldung | Leerer oder unvollständiger Filter für angepasste Attribute in der Canvas-Zielgruppe oder einem Schritt-Filter – entfernen Sie den Filter oder wählen Sie ein gültiges Attribut aus |
| Fehler „Request Timed Out“ beim Bearbeiten | Störung durch Browser-Erweiterungen, Werbeblocker oder eine abgelaufene Sitzung – versuchen Sie es in einem Inkognito-Fenster oder einem anderen Browser |
| Speichern nach dem Archivieren einer Variante nicht möglich | Eine archivierte Variante wird weiterhin nachgelagert referenziert; überprüfen Sie die Schrittverbindungen und stellen Sie die Variante wieder her oder ersetzen Sie sie |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Editor-Symptom" }

Wenn der Editor bei einem großen oder komplexen Canvas einfriert, versuchen Sie Folgendes:

- Leeren Sie den Browser-Cache und die Cookies und laden Sie die Seite neu. Unternehmens-Werbeblocker oder Browser-Erweiterungen können die Braze-Plattform beeinträchtigen.
- Verwenden Sie die Canvas-Zoom-Steuerung, um die Ansicht auf 25 % oder 10 % zu reduzieren und so die Menge an UI zu verringern, die der Browser rendern muss.
- Versuchen Sie es mit einem anderen Webbrowser.

Wenn das Canvas nicht lädt und nicht weiterkommt, wurde eine vorherige Version nicht korrekt gespeichert und enthält möglicherweise ungültige Schritte. Duplizieren Sie das Canvas über das Dashboard. Wenn das Problem weiterhin besteht, erstellen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support).

Fügen Sie bei Support-Tickets zu „Request Timed Out“ eine Bildschirmaufnahme, einen Zeitstempel mit Zeitzone, Browser und Version, Schritte zur Reproduktion und optional ein HAR-Protokoll aus den Entwicklertools Ihres Browsers bei. Siehe [Was sollte ich bei einem Support-Ticket für einen „Request Timed Out“-Fehler angeben?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error) in den Canvas-FAQ.

## Verhalten bei gestopptem Canvas {#stopped-canvas-behavior}

**Symptom:** Sie haben das Canvas gestoppt, aber Nutzer:innen haben weiterhin Nachrichten erhalten.

Wenn Sie ein Canvas stoppen, können keine Nutzer:innen mehr eintreten und es werden keine weiteren Nachrichten aus dem Canvas-Flow gesendet. E-Mail-Sendungen, die bereits an Ihren E-Mail-Anbieter übergeben wurden, können nicht zurückgerufen werden.

Nutzer:innen, die sich in einem Delay- oder Aktionspfad-Schritt befinden, werden nicht automatisch aus der Journey entfernt, wenn Sie das Canvas stoppen. Wenn Sie das Canvas erneut aktivieren, bevor die geplante Sendezeit abgelaufen ist, können diese Nutzer:innen ausstehende Schritte weiterhin erhalten.

Ausführliche Informationen finden Sie unter [Was passiert, wenn Sie ein Canvas stoppen?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-happens-when-you-stop-a-canvas) in den Canvas-FAQ.

## Fehler „Zu viele Canvas-Verzweigungen“ {#too-many-canvas-branches-error}

**Symptom:** Beim Starten eines geplanten Canvas wird der Fehler „Too many Canvas branches“ angezeigt.

Dieser Fehler tritt auf, wenn die Kombination aus Schrittverzweigungen und der Größe der Eintritts-Zielgruppe zu Cluster-Performance-Problemen führen kann, die den Nachrichtenversand verhindern. Braze zeigt diese Meldung an, wenn Sie ein Canvas mit geplantem Eintritt starten – beim Speichern eines Entwurfs erscheint sie nicht.

So beheben Sie das Problem:

- Reduzieren Sie die Schrittverzweigungen im Canvas.
- Verkleinern Sie die Eintritts-Zielgruppe.
- Verwenden Sie [Zielgruppenpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths), um Verzweigungen zu konsolidieren, anstatt viele parallele Pfade zu nutzen.
- Wenn Ihr Canvas den ursprünglichen Editor verwendet, [klonen Sie es in Canvas Flow]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases) und bauen Sie es mit Canvas-Komponenten neu auf.

Wenn Sie das Canvas dennoch ohne Änderungen starten müssen und nicht zu Canvas Flow wechseln können, wenden Sie sich an den [Support]({{site.baseurl}}/support_contact).

## Wann Sie den Support kontaktieren sollten {#when-to-contact-support}

Kontaktieren Sie den [Braze Support]({{site.baseurl}}/braze_support) innerhalb von 30 Tagen nach Auftreten des Problems, wenn Sie den [standardmäßigen Untersuchungspfad](#standard-investigation-path) abgeschlossen haben und weiterhin Hilfe benötigen.

Geben Sie folgende Informationen an:

- Canvas-ID und betroffene Nutzer:innen-IDs (externe ID oder Braze-ID)
- Zeitstempel mit Zeitzone
- Screenshots oder Exporte aus **Messaging History** oder **Messaging Diagnostics**
- Bei „Request Timed Out“-Fehlern im Editor die unter [Editor- und Speicherprobleme](#editor-and-save-issues) aufgeführten Details