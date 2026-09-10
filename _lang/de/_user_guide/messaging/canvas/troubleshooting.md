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
**Messaging-Verlauf** und **Messaging-Diagnostics**-Protokolle sind bis zu **30 Tage** ab dem Ereignis verfügbar. Kontaktieren Sie den [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) innerhalb dieses Zeitraums, wenn Sie Hilfe bei der Untersuchung eines bestimmten Vorfalls benötigen.
{% endalert %}

## Hier starten: Symptom zuordnen {#start-here-match-your-symptom}

| Symptom | Gehe zu |
| --- | --- |
| Eine:r Nutzer:in ist nicht in den Canvas eingetreten | [Nutzer:in ist nicht in den Canvas eingetreten](#user-didnt-enter-the-canvas) |
| Eine:r Nutzer:in ist eingetreten, hat aber keine Nachricht oder keinen Schritt erhalten | [Nutzer:in hat keine Canvas-Nachricht oder keinen Canvas-Schritt erhalten](#user-didnt-receive-a-canvas-message-or-step) |
| Niemand oder weniger Nutzer:innen als erwartet sind eingetreten | [Niedrige oder keine Canvas-Eintritte](#low-or-zero-canvas-entries) |
| Sendungen oder Zustellungen sind niedriger als die geschätzte Zielgruppe | [Weniger Sendungen als erwartet](#lower-sends-than-expected) |
| Canvas-Analytics sehen falsch aus (Kontrollgruppe, Konversionen, null Sendungen) | [Canvas-Analytics-Abweichungen](#canvas-analytics-mismatches) |
| Analytics zeigen weit mehr Sendungen als Eintritte oder mehr Exits als Eintritte | [Datumsbereichsfilterung kann unerwartete Zahlen anzeigen](#date-range-filtering-can-show-unexpected-numbers) |
| Canvas lässt sich nicht speichern oder der Editor friert ein | [Editor- und Speicherprobleme](#editor-and-save-issues) |
| Eine Canvas-Variante kann nicht gelöscht werden | [Canvas-Variante kann wegen eines archivierten Segments nicht gelöscht werden](#cant-delete-a-canvas-variant-because-of-an-archived-segment) |
| Ich habe den Canvas gestoppt, aber Nachrichten wurden trotzdem gesendet | [Verhalten eines gestoppten Canvas](#stopped-canvas-behavior) |
| Fehler „Too many Canvas branches“ beim Starten | [Fehler „Too many Canvas branches“](#too-many-canvas-branches-error) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canvas-Symptom" }

## Standardmäßiger Untersuchungspfad {#standard-investigation-path}

Verwenden Sie diesen Workflow, um ein Problem bei bestimmten Nutzer:innen oder bei einem aggregierten Versand zu untersuchen. Beginnen Sie bei jedem Vorfall mit Schritt 1.

1. Bestätigen Sie, dass das Canvas aktiv ist (nicht im Entwurf, gestoppt oder archiviert).
2. Bestätigen Sie, dass der Eintrittszeitplan (geplantes Fenster, Zeitzone, aktionsbasierter Trigger oder API-gesteuerter Eintritt) mit dem erwarteten Eintrittszeitpunkt der Nutzer:innen übereinstimmt.
3. Prüfen Sie den Messaging-Verlauf von Nutzer:innen, indem Sie zu **Audience** > **Search users** navigieren, das Profil öffnen und **Messaging History** (letzte 30 Tage) auswählen.
   - Wenn kein Eintrag für den erwarteten Versandzeitpunkt vorhanden ist, liegt das Problem beim Eintritt, nicht bei der Nachricht. Gehen Sie zu [Nutzer:in ist nicht in das Canvas eingetreten](#user-didnt-enter-the-canvas).
4. Prüfen Sie den Canvas-**Changelog** und die Changelogs aller Segmente, die im Targeting verwendet werden. Bestätigen Sie, dass Zielgruppe, Schritte oder Versandeinstellungen während des Vorfalls nicht geändert wurden.
5. Prüfen Sie die aggregierten Ergebnisse auf der Canvas-Analytics-Seite, indem Sie das [Messaging-Diagnostics-Dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) öffnen und Abbruch- und Verwerfungsgründe überprüfen.
   - Wenn Sie ein Ergebnis sehen, das Sie nicht zuordnen können, lesen Sie [Abbruchergebnisse]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard#abort-outcomes) in der Diagnostics-Dokumentation.
   - Wenn ein Schritt null Eintritte (nicht null Versendungen) anzeigt, prüfen Sie den vorherigen Schritttyp ([Aktionspfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths), [Verzögerung]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step), [Zielgruppenpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) oder [Decision-Split]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split)).
6. Wenn Sie weiterhin blockiert sind, kontaktieren Sie den [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) innerhalb von 30 Tagen mit der Canvas-ID, den betroffenen Nutzer:innen-IDs, Zeitstempeln (mit Zeitzone) und Screenshots aus Messaging History oder Messaging Diagnostics.

Verwenden Sie vor dem Start [Test-Canvases senden]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases) und [Nutzerpfade in der Vorschau anzeigen]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths), um Ihre Konfiguration zu validieren.

## Nutzer:in ist nicht in den Canvas eingetreten {#user-didnt-enter-the-canvas}

**Symptom:** Eine Nutzer:in ist nicht wie erwartet in den Canvas eingetreten, oder es sind weniger Nutzer:innen eingetreten, als Ihre Trigger-Events vermuten lassen.

Nutzer:innen müssen die **Zielgruppe** erfüllen, bevor Braze den Entry-Trigger auswertet (mit Ausnahme von [Attributänderungs]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value)-Triggern). Ein Trigger allein garantiert keinen Entry, wenn die Nutzer:in zum Zeitpunkt der Auswertung nicht zur Zielgruppe gehörte.

Wiederzulässigkeit und Wiedereintritt sind separate Einstellungen unter [Entry-Einstellungen auswählen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls):

- **Wiederzulässigkeit:** Bestimmt, ob eine Nutzer:in nach dem Verlassen des Canvas erneut eintreten darf (Zeitfenster und Einstellung **Nutzer:innen erneuten Canvas-Entry erlauben**).
- **Wiedereintritt:** Bestimmt, ob eine Nutzer:in, die sich aktuell im Canvas befindet, einen parallelen Pfad betreten kann.

Eine Nutzer:in kann wiederzulässig sein, aber blockiert werden, weil sie sich noch im Canvas befindet, oder sie kann den Canvas verlassen haben, sich aber noch außerhalb des Wiederzulässigkeitsfensters befinden. Prüfen Sie beide Einstellungen, wenn eine Nutzer:in nicht erneut in einen Canvas eintritt.

Überprüfen Sie Folgendes:

- **Entry-Zeitplan und Zeitzone:** Bestätigen Sie, dass der Canvas aktiv war und die Nutzer:in den Trigger während des [Entry-Fensters]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule) ausgeführt hat.
- **Zielgruppe zum Zeitpunkt der Auswertung:** Überprüfen Sie die Änderungsprotokolle von Segmenten und Filtern. [User Lookup]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) kann bei einigen Filtertypen ein falsch-positives Ergebnis anzeigen (z. B. datumsbezogene Attribute im String-Format).
- **Entry-Limits:** [Maximale Eintritte]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) oder Zielgruppen-Obergrenzen wurden möglicherweise erreicht.
- **Globale Kontrollgruppe:** Nutzer:innen in der [globalen Kontrollgruppe]({{site.baseurl}}/user_guide/audience/global_control_group) treten nicht in Messaging-Canvases ein.
- **Canvas-Kontrollgruppe:** Nutzer:innen, die beim Entry der Canvas-Kontrollgruppe zugewiesen werden, erhalten keine Varianten-Nachrichten. Die Variantenzuweisung erfolgt beim Entry, nicht über Segmentfilter. Siehe [Abweichungen bei Canvas-Analytics](#canvas-analytics-mismatches).
- **Exit-Kriterien:** Die Nutzer:in hat möglicherweise die [Exit-Kriterien]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria) vor oder während des Entry erfüllt. Wenn Entry und Exit dasselbe Event verwenden, siehe [Übereinstimmung von Entry- und Exit-Kriterien]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/matching_entry_and_exit_criteria).
- **API-getriggerter Entry:** Bestätigen Sie, dass die Nutzer:in über den [`/canvas/trigger/send`-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) hinzugefügt wurde. Sie können [ein Segment erstellen]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) mit einem Canvas-Entry-Filter und Nutzer:innen über [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) exportieren.

### Trigger-Event-Anzahl ist höher als Canvas-Eintritte {#trigger-event-count-is-higher-than-canvas-entries}

**Symptom:** Das Trigger-Event-Volumen ist höher als die Anzahl der Canvas-Eintritte.

Braze dedupliziert mehrere Entry-Versuche, die im selben Moment auftreten, sodass Sie möglicherweise weniger Canvas-Eintritte als Trigger-Events sehen. Zum Testen mehrerer Eintritte sollten Sie Trigger-Events mindestens eine Sekunde auseinanderhalten.

Wenn eine Nutzer:in denselben Trigger innerhalb einer Sekunde mehrmals ausführt, verarbeitet Braze nur einen Entry. Überprüfen Sie die Messaging-Diagnose auf Ergebnisse wie **Nutzer:in nicht wiederzulässig**, wenn Wiedereintritts- oder Wiederzulässigkeitsregeln gelten.

{% details Sommerzeit und täglich geplante Canvases %}

An Tagen mit Sommerzeitumstellung können täglich geplante Canvases bis zu eine Stunde früher oder später als gewöhnlich ausgeführt werden. Wenn Ihre Entry-Kriterien auf angepassten Attributen oder Events mit Zeitstempeln basieren, die innerhalb einer Stunde der geplanten Entry-Zeit liegen, qualifizieren sich Nutzer:innen am Umstellungstag möglicherweise noch nicht, weil das Attribut oder Event noch nicht protokolliert wurde.

Angenommen, Nutzer:innen erhalten in der Regel um 15:00 Uhr in der Zeitzone Ihres Canvas ein angepasstes Attribut-Update und Ihr Canvas läuft täglich um 15:30 Uhr in derselben Zeitzone. An einem Sommerzeitumstellungstag (Vorstellung) kann der Canvas Nutzer:innen bis zu eine Stunde früher als üblich relativ zu diesem Attribut-Update auswerten — bevor das Attribut protokolliert wurde. Wenn die Wiederzulässigkeit deaktiviert ist, können Nutzer:innen, die an vorherigen Tagen eingetreten sind, nicht erneut eintreten, was zu null Eintritten für diesen Tag führt.

Um dies zu vermeiden, stellen Sie sicher, dass Ihre angepassten Attribut- oder Event-Updates mehr als eine Stunde vor der geplanten Canvas-Entry-Zeit erfolgen.

{% enddetails %}

## Nutzer:in hat keine Canvas-Nachricht oder keinen Canvas-Schritt erhalten {#user-didnt-receive-a-canvas-message-or-step}

**Symptom:** Eine Nutzer:in ist in das Canvas eingetreten, hat aber die erwartete Nachricht oder den erwarteten Schritt nicht erhalten.

Überprüfen Sie den [**Nachrichtenverlauf**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#messaging-history-tab) der Nutzer:in für den Canvas-Schritt und Zeitstempel. Wenn kein Eintrag vorhanden ist, kehren Sie zu [Nutzer:in ist nicht in das Canvas eingetreten](#user-didnt-enter-the-canvas) zurück.

Prüfen Sie dann Folgendes je nach Trigger- oder Schritttyp:

- **Angepasste Events oder Kauf-Trigger:** Bestätigen Sie, dass das Event in **Analytics** > **Bericht für angepasste Events** (oder **Umsatz** für Käufe) erscheint. Vergleichen Sie den Event-Zeitstempel mit dem Zeitpunkt, zu dem das Canvas live ging, und mit einer möglichen geplanten Verzögerung beim Schritt.
- **API-getriggerter Entry:** Bestätigen Sie den Entry mit einem Canvas-Segmentfilter und -export, wie in [Nutzer:in ist nicht in das Canvas eingetreten](#user-didnt-enter-the-canvas) beschrieben.
- **Aktionspfade oder Nachrichten-Schritt-Trigger:** Bestätigen Sie, dass die Nutzer:in das vorausgesetzte Event ausgeführt hat und dass [Event-Eigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#event-properties) im Schritt verfügbar sind.
- **In-App-Nachricht-Schritte:** In-App-Nachrichten werden beim nächsten Sitzungsstart gesendet, nachdem die Nutzer:in den Schritt betreten hat, und nur über SDK-Events (nicht über die REST API). Siehe [Wann werden In-App-Nachrichten in Canvas gesendet?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#when-are-in-app-messages-in-canvas-sent) in den Canvas-FAQ.
- **Canvas-Kontrollgruppe:** Überprüfen Sie, ob die Nutzer:in beim Entry der Canvas-Kontrollgruppe zugewiesen wurde.
- **Kanalberechtigung und Versandeinstellungen:** Bestätigen Sie den Abo-Status, den Push-Aktivierungsstatus und die [Versandeinstellungen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-14-select-your-send-settings) pro Schritt (zum Beispiel **Abo-Einstellungen** auf nur Nutzer:innen mit Opt-in). Fügen Sie keine Einzelkanal-Filter zur **Zielgruppe** in Mehrkanalcanvases hinzu.
- **Zustellungsvalidierungen:** Wenn Sie **Zielgruppe beim Nachrichtenversand validieren** in einem Nachrichten-Schritt aktiviert haben, erhalten Nutzer:innen, die zum Sendezeitpunkt nicht mehr den Filtern entsprechen, die Nachricht nicht. Siehe [Zustellungsvalidierungen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations).
- **Ruhezeiten, intelligentes Timing, Frequency-Caps und Rate-Limits:** Diese können Sendungen verschieben, unterdrücken oder abbrechen. Nutzer:innen können nach einem Ruhezeiten-Abbruch weiterhin im Canvas verbleiben.
- **Race-Conditions:** Wenn die Nutzer:in mehrere Aktionen gleichzeitig ausgelöst hat, siehe [Race-Conditions]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions).

{% alert important %}
Wenn ein Canvas-Nachrichten-Schritt einen Versand abbricht, rückt die Nutzer:in trotzdem zum nächsten Schritt vor. Canvas rückt bei Abbruch vor, damit nachfolgende Verzögerungs- und Aktionspfad-Schritte nicht dauerhaft blockiert werden. Siehe [Wie Nutzer:innen vorrücken]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance) und [Abbruch-Ergebnisse]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard#abort-outcomes).
{% endalert %}

Für Filter auf Schrittebene, Konflikte zwischen Branches und IAM-Branching-Verhalten siehe [Start mit Canvas Flow – Fehlerbehebung]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/launching_canvas_flow#troubleshooting) und die [Canvas-FAQ]({{site.baseurl}}/user_guide/messaging/canvas/faqs#messages-and-delivery).

{% alert important %}
Wenn Ihr aktionsbasiertes Canvas Nachrichten früher als erwartet sendet, prüfen Sie, ob Ihr Zeitstempel für angepasste Events die aktuelle Zeit verwendet und nicht eine zurückdatierte Zeit. Braze berechnet Verzögerungen anhand des mit dem Event gesendeten Zeitstempels. Siehe [Aktionsbasierte Zustellung]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule).
{% endalert %}

## Niedrige oder null Canvas-Eintritte {#low-or-zero-canvas-entries}

**Symptom:** Niemand oder weniger Nutzer:innen als erwartet sind in den Canvas eingetreten.

Beginnen Sie mit der [Checkliste zum Start mit Canvas Flow]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/launching_canvas_flow#launch-checklist) und überprüfen Sie dann Folgendes:

- Der Canvas ist aktiv und der aktuelle Zeitpunkt liegt innerhalb des geplanten Eintritts-Zeitfensters.
- Die [Entry-Einstellungen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) (erneute Berechtigung, maximale Eintritte und Eintritts-Obergrenzen) erlauben den erwarteten Nutzer:innen den Eintritt.
- Die Zielgruppe und die Segment-Filter stimmen nach dem Start noch mit den erwarteten Nutzer:innen überein.
- Die Prozentsätze der globalen und der Canvas-Kontrollgruppe zeigen, welcher Anteil der Nutzer:innen in welchen Pfad eintritt und wer Nachrichten erhält.
- Workspace-Rate-Limits oder Entry-Warteschlangen verursachen erwartungsgemäß Verzögerungen zwischen dem Zeitpunkt, zu dem Nutzer:innen sich qualifizieren, und dem Zeitpunkt, zu dem sie eintreten oder in einen Schritt vorrücken.

Für einzelne Nutzer:innen folgen Sie dem [standardmäßigen Untersuchungspfad](#standard-investigation-path). Bei Null-Eintritten aufgrund von Zeitumstellungen siehe den aufklappbaren Abschnitt unter [Nutzer:in ist nicht in den Canvas eingetreten](#user-didnt-enter-the-canvas).

## Weniger Versendungen als erwartet {#lower-sends-than-expected}

**Symptom:** Versendungen oder Zustellungen liegen unter der geschätzten Zielgruppe eines Canvas-Schritts.

Häufige Ursachen sind die erneute Zielgruppenbewertung zum Sendezeitpunkt, Kanalberechtigung, Kontrollgruppen, Ruhezeiten, intelligentes Timing, Rate-Limits und das Zustellverhalten von In-App-Nachrichten (null _Versendungen_ bei vorhandenen Impressionen ist bei In-App-Nachrichten erwartetes Verhalten).

Wenn ein Nachrichtenschritt viele eingetretene Nutzer:innen, aber wenige Versendungen zeigt, prüfen Sie, ob Liquid `abort_message()` den Versand abgebrochen hat. Informationen zu Prüfungen im Nachrichtenaktivitätsprotokoll, fehlenden Attributen und Testversand finden Sie unter [Fehlerbehebung bei hohen Abbruchraten]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages#troubleshooting-high-abort-rates).

Eine ausführliche Liste finden Sie unter [Warum liegen die Versendungen unter der geschätzten Zielgruppengröße?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#why-are-sends-lower-than-the-estimated-audience-size) in den Canvas-FAQ und [Warum liegen die Versendungen unter der geschätzten Zielgruppengröße?]({{site.baseurl}}/user_guide/messaging/campaigns/faq#why-are-sends-lower-than-the-estimated-audience-size) für Campaigns.

Verwenden Sie das [Messaging-Diagnose-Dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard), um Abbruch- und Drop-Gründe auf Schrittebene einzusehen.

## Analytics-Abweichungen bei Canvas {#canvas-analytics-mismatches}

**Symptom:** Canvas-Analytics sehen falsch aus (Kontrollgruppenaufteilung, Konversionen oder null Sendungen).

Die Zuweisung zu Kontrollgruppen und Varianten erfolgt beim Canvas-Eintritt basierend auf den Prozentsätzen, die Sie im Builder festgelegt haben – nicht über Segmentfilter. Nutzer:innen, die einen bestimmten Kanal nicht empfangen können, können trotzdem einer Variante zugewiesen werden. Verwenden Sie die [Sendeeinstellungen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-14-select-your-send-settings) pro Schritt, um einzuschränken, wer welchen Nachrichtentyp erhält, anstatt die **Zielgruppe** mit Kanalfiltern einzugrenzen.

Unterscheiden Sie die Canvas-Kontrollgruppe von der [globalen Kontrollgruppe]({{site.baseurl}}/user_guide/audience/global_control_group). Filterdefinitionen finden Sie unter [Was ist der Unterschied zwischen „Hat keine Canvas-Variante betreten“ und „Ist nicht in der Canvas-Kontrollgruppe“?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-is-the-difference-between-has-not-entered-canvas-variation-and-is-not-in-canvas-control-group) in den Canvas-FAQ.

{% details Warum Varianten-Sendungen niedriger sein können als der Varianten-Prozentsatz %}

Stellen Sie sich folgendes Szenario vor:

- Ein Canvas hat eine einzelne Variante und eine Kontrollgruppe.
- Der erste Schritt der Variante ist eine Push-Benachrichtigung.
- 90 % der Nutzer:innen wurden ausgewählt, die Variante zu betreten, und 10 % die Kontrollgruppe.

![Canvas-Beispiel mit 90 % Variante und 10 % Kontrollgruppe.]({% image_buster /assets/img_archive/trouble15.png %})

In diesem Szenario betreten 90 % der Nutzer:innen, die das Canvas betreten, die Variante.

Wenn Sie sich das Segment der aktiven Nutzer:innen ansehen, werden Sie feststellen, dass es zwar 29.800 Nutzer:innen enthält, aber nur 64 % davon Push-fähig sind:

![Segment mit dem Filter „Push-fähig“ auf „wahr“ gesetzt und geschätzten 29.800 Nutzer:innen.]({% image_buster /assets/img_archive/trouble16.png %})

Das bedeutet, dass nicht alle Nutzer:innen eine Push-Benachrichtigung empfangen können, obwohl Sie festgelegt haben, dass 90 % der Nutzer:innen die Variante betreten sollen. Nutzer:innen, die kein Push empfangen können, betreten trotzdem die Variante – die Sendeanzahl spiegelt die Kanalberechtigung beim jeweiligen Schritt wider, nicht die Variantenzuweisung beim Eintritt.

{% enddetails %}

### Datumsbereichsfilter können unerwartete Zahlen anzeigen {#date-range-filtering-can-show-unexpected-numbers}

**Symptom:** Canvas- oder Schritt-Analytics zeigen unerwartete oder unplausible Zahlen an, z. B. deutlich mehr Sendungen als Eintritte oder mehr Nutzer:innen, die einen Schritt verlassen, als ihn betreten haben.

Dies kann passieren, wenn Sie den Datumsbereichs-Kalenderfilter oben auf der Canvas-Analytics-Seite verwenden. Wenn Sie einen Datumsbereich auswählen, der einige Nutzeraktionen ausschließt, zeigen die dargestellten Metriken möglicherweise nur einen Teil der Journey jeder:jedes Nutzer:in an.

Beispiele:
- Sie sehen möglicherweise 100 Eintritte bei 8.000 Sendungen, wenn Ihr Datumsbereich nach dem Eintritt der meisten Nutzer:innen beginnt, aber den Zeitraum umfasst, in dem sie Nachrichten erhalten haben.
- Sie sehen möglicherweise mehr Nutzer:innen, die zum nächsten Schritt wechseln, als den vorherigen Schritt betreten haben, wenn Ihr Datumsbereich nur die Exits, aber nicht die früheren Eintritte erfasst.

Um dieses Problem zu beheben, passen Sie den Datumsbereich so an, dass er entweder alle Daten vom Start des Canvas bis heute umfasst, oder wählen Sie einen Bereich, der den gesamten für die benötigten Metriken relevanten Zeitraum abdeckt.

Informationen zu Konversionsraten-Definitionen und schrittweisen Analytics finden Sie unter [Analytics und Konversionen]({{site.baseurl}}/user_guide/messaging/canvas/faqs#analytics-and-conversions) in den Canvas-FAQ.

## Editor- und Speicherprobleme {#editor-and-save-issues}

**Symptom:** Der Canvas-Editor lädt nicht, friert ein oder speichert Ihre Änderungen nicht.

| Symptom | Wahrscheinlichste Ursache |
| --- | --- |
| Speicher-Button dreht sich endlos ohne Fehlermeldung | Leerer oder unvollständiger Filter für angepasste Attribute in der Canvas-Zielgruppe oder einem Schritt-Filter – entfernen Sie den Filter oder wählen Sie ein gültiges Attribut aus |
| Fehler „Request Timed Out“ beim Bearbeiten | Störung durch Browser-Erweiterungen, Werbeblocker oder eine veraltete Sitzung – versuchen Sie ein Inkognito-Fenster oder einen anderen Browser |
| Speichern nach Archivierung einer Variante nicht möglich | Eine archivierte Variante wird weiterhin nachgelagert referenziert; überprüfen Sie die Schritt-Verbindungen und stellen Sie die Variante wieder her oder ersetzen Sie sie |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Editor-Symptom" }

{% alert note %}
Wenn Sie dasselbe Canvas in mehreren Browser-Tabs geöffnet haben, kann das Speichern in einem Tab Änderungen überschreiben, die in einem anderen veralteten Tab vorgenommen wurden. Diese Race-Condition kann dazu führen, dass Zielgruppenfilter entfernt oder unbeabsichtigte Änderungen angewendet werden. Um Datenverlust zu vermeiden, schließen Sie alle doppelten Tabs, bevor Sie ein Canvas bearbeiten und speichern.
{% endalert %}

Wenn der Editor bei einem großen oder komplexen Canvas einfriert, versuchen Sie Folgendes:

- Leeren Sie den Browser-Cache und die Cookies und laden Sie die Seite neu. Unternehmens-Werbeblocker oder Browser-Erweiterungen können die Braze-Plattform beeinträchtigen.
- Verwenden Sie die Canvas-Zoomsteuerung, um die Ansicht auf 25 % oder 10 % zu reduzieren und so die Menge an UI zu verringern, die der Browser rendern muss.
- Versuchen Sie einen anderen Webbrowser.

Wenn das Canvas nicht lädt und nicht weiterkommt, wurde eine frühere Version nicht korrekt gespeichert und enthält möglicherweise ungültige Schritte. Duplizieren Sie das Canvas über das Dashboard. Wenn das Problem weiterhin besteht, eröffnen Sie ein [Support-Ticket]({{site.baseurl}}/user_guide/administer/personal/braze_support).

Für Support-Tickets bei „Request Timed Out“ fügen Sie eine Bildschirmaufnahme, Zeitstempel und Zeitzone, Browser und Version, Schritte zur Reproduktion und optional ein HAR-Log aus den Entwicklertools Ihres Browsers bei. Siehe [Was sollte ich bei einem Support-Ticket für einen „Request Timed Out“-Fehler angeben?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error) in den Canvas-FAQ.

{% multi_lang_include audience/segments.md section='Canvas variant archived segment' %}

## Verhalten eines gestoppten Canvas {#stopped-canvas-behavior}

**Symptom:** Sie haben das Canvas gestoppt, aber Nutzer:innen haben trotzdem Nachrichten erhalten.

Wenn Sie ein Canvas stoppen, können Nutzer:innen nicht mehr eintreten und es werden keine weiteren Nachrichten aus dem Canvas-Flow gesendet. E-Mail-Versendungen, die bereits an Ihren E-Mail-Anbieter übergeben wurden, können nicht zurückgerufen werden.

Nutzer:innen, die sich in einem Verzögerungs- oder Aktionspfad-Schritt befinden, werden nicht automatisch aus der Journey entfernt, wenn Sie das Canvas stoppen. Wenn Sie das Canvas erneut aktivieren, bevor die geplante Sendezeit abgelaufen ist, können diese Nutzer:innen noch ausstehende Schritte erhalten.

Alle Details finden Sie unter [Was passiert, wenn Sie ein Canvas stoppen?]({{site.baseurl}}/user_guide/messaging/canvas/faqs#what-happens-when-you-stop-a-canvas) in den Canvas-FAQ.

## Fehler „Zu viele Canvas-Branches“ {#too-many-canvas-branches-error}

**Symptom:** Beim Starten eines geplanten Canvas wird der Fehler „Too many Canvas branches“ angezeigt.

Dieser Fehler tritt auf, wenn die Kombination aus Schrittverzweigungen und der Größe der Eintrittszielgruppe zu Performance-Problemen im Cluster führen kann, die den Nachrichtenversand verhindern. Braze zeigt diese Meldung an, wenn Sie ein Canvas mit geplantem Eintritt starten – beim Speichern eines Entwurfs erscheint sie nicht.

So beheben Sie das Problem:

- Reduzieren Sie die Schrittverzweigungen im Canvas.
- Reduzieren Sie die Größe der Eintrittszielgruppe.
- Verwenden Sie [Zielgruppenpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths), um Verzweigungen zu konsolidieren, anstatt viele parallele Pfade zu nutzen.
- Wenn Ihr Canvas den ursprünglichen Editor verwendet, [klonen Sie es zu Canvas Flow]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases) und erstellen Sie es mit Canvas-Komponenten neu.

Wenn Sie das Canvas dennoch ohne Änderungen starten müssen und nicht zu Canvas Flow wechseln können, wenden Sie sich an den [Support]({{site.baseurl}}/support_contact).

## Wann Sie den Support kontaktieren sollten {#when-to-contact-support}

Kontaktieren Sie den [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) innerhalb von 30 Tagen nach Auftreten des Problems, wenn Sie den [standardmäßigen Untersuchungspfad](#standard-investigation-path) abgeschlossen haben und weiterhin Hilfe benötigen.

Geben Sie Folgendes an:

- Canvas-ID und betroffene Nutzer:innen-IDs (externe ID oder Braze-ID)
- Zeitstempel mit Zeitzone
- Screenshots oder Exporte aus **Messaging History** oder **Messaging Diagnostics**
- Bei „Request Timed Out“-Fehlern im Editor die unter [Editor- und Speicherprobleme](#editor-and-save-issues) aufgeführten Details