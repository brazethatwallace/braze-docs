---
nav_title: Vorschau der Nutzerpfade
article_title: Vorschau der Nutzerpfade
page_order: 0.3
alias: /preview_user_paths/
description: "Auf dieser Seite erfahren Sie, wie Sie in Canvas eine Vorschau der Nutzerpfade anzeigen können."
tool:
  - Canvas
---

# Vorschau der Nutzerpfade in Canvas {#preview-user-paths-in-canvas}

> Erleben Sie die Canvas-Journey, die Sie für Ihre Nutzer:innen erstellt haben. Dies umfasst die Vorschau des Timings und der Nachrichten, die Ihre Nutzer:innen erhalten. Diese Testläufe dienen der Qualitätssicherung, um sicherzustellen, dass Ihre Nachrichten an die richtige Zielgruppe gesendet werden – noch bevor Sie Ihr Canvas versenden.

## Erstellen eines Testlaufs {#creating-a-test-run}

Führen Sie die folgenden Schritte aus, um eine Vorschau Ihrer User Journey anzuzeigen:

1. Gehen Sie zu Ihrem Canvas-Builder. Speichern Sie alle nicht gespeicherten Änderungen und beheben Sie alle Fehler.
2. Wählen Sie **Canvas testen** in der Fußzeile aus.
3. Wählen Sie eine:n Testnutzer:in aus.
4. (Optional) Wählen Sie eine:n Empfänger:in für den Test aus.
5. Wählen Sie **Test ausführen** aus.

Sie können eine Vorschau ausführen, auch wenn Sie keine Berechtigung zum Bearbeiten eines Canvas haben. Diese Vorschau wird jedoch mit nicht gespeicherten Änderungen ausgeführt, falls welche vorhanden sind.

### Unterstützte Schritte {#supported-steps}

Die folgenden Schritte werden unterstützt:
- Nachricht
- Zielgruppenpfad
- Decision-Split
- Verzögerung
- Aktionspfad
- Experimentpfad
- Agent
- Nutzer:innen-Update (nur im UI-Editor, d. h. Schritte, die den JSON-Editor verwenden, werden übersprungen)

Wenn der Test auf einen Schritttyp trifft, der in diesem Abschnitt nicht aufgeführt ist, wird der nicht unterstützte Schritt übersprungen, und die/der Testnutzer:in fährt mit dem nächsten unterstützten Schritt fort.

### Agent-Schritte {#agent-steps}

Wenn ein Testlauf einen [Agent-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step) erreicht, pausiert Braze und fragt: **Möchten Sie den Agenten „{agentName}“ ausführen?** Wählen Sie, wie Sie fortfahren möchten:

- **Ja:** Fügen Sie optional Kontext im Textfeld hinzu (zusätzlich zum Profil der/des Testnutzer:in und dem bereits in der Journey vorhandenen Canvas-Kontext) und wählen Sie dann **Antwort simulieren** aus, um den Agenten aufzurufen. Sie können Beispielwerte in natürlicher Sprache eingeben – zum Beispiel eine Beschreibung des Warenkorb-Inhalts oder des eingehenden Nachrichtentexts –, um den Laufzeitkontext nachzuahmen, den der Agent in der Produktion erhalten würde.
- **Nein:** Braze ruft den Agenten nicht auf. Der Schritt verwendet die konfigurierte **Fallback-Ausgabe** des Agenten aus dem Abschnitt **Output** in der [Agent Console]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values).

Wenn Sie **Ja** und **Antwort simulieren** auswählen, wird der Agent für die/den Vorschau-Nutzer:in ausgeführt, speichert seine Ausgabe in der Ausgabevariable des Agent-Schritts, und der Test wird entlang der Journey fortgesetzt. Aufrufe über **Antwort simulieren** werden auf das tägliche Aufruflimit des Agenten angerechnet und erscheinen unter **Agent Console** > **Logs**.

Um einen Agent-Schritt isoliert zu testen (ohne den vollständigen Canvas-Pfad auszuführen), verwenden Sie die schrittinterne Vorschau im Canvas-Builder. Einzelheiten zur Einrichtung finden Sie unter [Den Agenten testen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step#step-5-test-the-agent) im Abschnitt „Agent-Schritt“.

Wenn Ihr Agent-Schritt von Daten aus einem vorgelagerten [Kontextschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) abhängt, führen Sie **Canvas testen** aus, damit die Kontextvariablen entlang des Pfads befüllt werden. Seed-Gruppen werten Kontextschritte oder Kontextvariablen für Seed-Empfänger:innen nicht aus.

### Details zu Canvas-Schritten {#canvas-step-details}

Um weitere Details zu den Eintrittskriterien anzuzeigen, wählen Sie **Mehr anzeigen** aus. Schritte mit Segmentierung zeigen die erfüllten oder nicht erfüllten Kriterien an. Nachrichten zeigen dies auch für Zustellungsvalidierungen und Kanalberechtigung an. Nachrichtenschritte zeigen, welche Kanäle gesendet bzw. nicht gesendet wurden.

### Liquid

Braze verarbeitet Liquid-Logik während eines Testlaufs, auch wenn Sie keine tatsächliche Testnachricht senden. Das bedeutet, dass die [Logik zum Abbrechen von Nachrichten]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) und andere Liquid-Logik berücksichtigt werden und die Canvas-User-Journey beeinflussen können.

Wenn Ihre Vorschau den letzten Schritt Ihrer User Journey sendet, anstatt abzubrechen, verwendet die Vorschau möglicherweise die aktuelle Uhrzeit als den für die Liquid-Auswertung getesteten Zeitpunkt und nicht die tatsächliche Zeit, zu der sich die/der Nutzer:in basierend auf der Canvas-Eintrittszeit im Schritt befinden würde.

## Vorschau für das Timing {#previews-for-timing}

Bei geplanten Canvases tritt der/die Testnutzer:in zum nächsten geplanten Eintrittszeitpunkt ein. Bei aktionsbasierten Canvases mit Startdaten tritt der/die Testnutzer:in zum Startdatum und zur Startzeit ein.

Obwohl die standardmäßigen Startzeiten weiterhin gelten, ist der Eintrittszeitpunkt in allen Fällen konfigurierbar, sodass Sie ein Datum in der Vergangenheit oder Zukunft simulieren können. Sie können jedoch nicht vor dem Startdatum oder nach dem Enddatum des Canvas testen.

Nachrichten- und Verzögerungsschritte zeigen den Zeitpunkt an, zu dem Nutzer:innen weitergeleitet werden oder die Nachricht erhalten würden, ohne dass die Verzögerungen neu konfiguriert werden müssen. Beachten Sie, dass die Schritte zwar anzeigen, ob intelligentes Timing verwendet wird, diese Vorschau des Nutzerpfads jedoch keine Schätzung für eine:n Testnutzer:in berechnet.

Bei Canvases mit einem Aktions-Trigger wie „Änderung des Werts eines angepassten Attributs“ versucht Braze, die Änderung zu simulieren, indem das Attribut der/des Nutzer:in im Trigger vorübergehend auf leer gesetzt wird – **nur für den Testlauf des Canvas** (dies hat keine Auswirkungen auf das Nutzerprofil). Damit soll getestet werden, dass sich das Attribut gegenüber seinem aktuellen Wert ändert.

## Wann Nutzer:innen eintreten und austreten {#when-users-enter-and-exit}

Testnutzer:innen treten in die Vorschau ein, auch wenn sie im echten Betrieb nicht berechtigt wären. Falls sie nicht berechtigt sind, können Sie sehen, warum sie die Kriterien nicht erfüllt haben. Wenn Testnutzer:innen die Vorschau betreten, wird davon ausgegangen, dass sie die Zielgruppenkriterien erfüllt und die Aktions-Trigger-Kriterien ausgeführt haben. Beispielsweise wird bei einem Canvas, der angepasste Events in den Eintrittskriterien verwendet, davon ausgegangen, dass die Testnutzer:innen das angepasste Event wie in den Eintrittskriterien erwartet ausgeführt haben. Wenn jedoch dasselbe angepasste Event an anderer Stelle im Canvas verwendet wird (z. B. in den Exit-Kriterien), sollten Sie berücksichtigen, wie sich dies auf den Nutzerpfad auswirken könnte.

Events, API-Trigger, angepasste Attribute und Canvas-Entry-Eigenschaften, bei denen angenommen wird, dass sie Testnutzer:innen den Eintritt in den Canvas ermöglichen, werden nicht im tatsächlichen Nutzerprofil aktualisiert und bleiben über den Testlauf hinaus nicht bestehen. Wenn beispielsweise während des Tests ein angepasstes Attribut als Canvas-Trigger verwendet wird, werden die Trigger-Kriterien auf die Vorschau der Nutzer:innen angewendet, **als ob** sie die Änderung des angepassten Attributs getriggert hätten.

### Hinweis {#consideration}

Wenn Sie einen Aktionspfad mit Aktionen testen, die den Exit-Kriterien entsprechen (einschließlich Event-Eigenschaften), werden die Exit-Kriterien ausgelöst und der Testlauf endet. Wenn Sie einen Nachrichtenschritt testen, der den Exit-Kriterien entspricht, werden die Exit-Kriterien ausgelöst und der Testlauf endet.

Derzeit können Sie kein bestimmtes Event oder keine bestimmte Eigenschaft innerhalb eines Aktionspfads auswählen, um Exit-Kriterien auszulösen (nur den Pfad als Ganzes). Wenn Nutzer:innen potenziell mehrere Exit-Kriterien erfüllen könnten, wird das erste, das verarbeitet wird und das sie erfüllen, als Ergebnis angezeigt.

## Experimentpfade und Canvas-Varianten {#experiment-paths-and-canvas-variants}

- Wählen Sie bei Canvases mit Varianten auf oberster Ebene zu Beginn des Tests eine Variante aus.
- Wählen Sie bei Experimentpfaden die Variante aus, die die Testnutzer:in durchläuft, wenn sie den Canvas-Schritt erreicht.
- Bei Experimentpfaden mit personalisiertem Pfad oder Gewinnervariante gibt es eine Verzögerungsphase, in der die Testnutzer:in in einem Nachrichten-Schritt wartet. Diese Verzögerung wird jedoch nicht berücksichtigt, da Braze davon ausgeht, dass die Nutzer:in die ausgewählte Variante sofort durchlaufen hat.

## Testsendungen {#test-sends}

Sie können sich dafür entscheiden, Testnachrichten an eine interne Testgruppe oder eine:n einzelne:n Nutzer:in zu senden, während der Testlauf durchgeführt wird. Das bedeutet, dass nur Nachrichten gesendet werden, auf die die Nutzer:innen entlang des Testpfads stoßen. Die Empfänger:innen erhalten Nachrichten standardmäßig mit ihren eigenen Attributen, Sie können diese jedoch mit den Attributen der Testnutzer:innen überschreiben.

Um alle Testnachrichten in einem Canvas auf einmal zu senden, unabhängig vom Pfad und ohne den Pfad in der Vorschau anzuzeigen, können Sie im Tab **Testsendungen** die Option **Alle Testnachrichten senden** auswählen.

## Responsivität {#responsiveness}

Canvas-Schritte reagieren bei der Vorschau von Nutzerpfaden auf das Timing. Aktualisierungen, die über den Nutzeraktualisierungsschritt vorgenommen werden, werden in nachfolgenden Schritten im Ablauf berücksichtigt, aber nicht auf das tatsächliche Nutzerprofil angewendet. Die Auswirkungen des Eintritts von Nutzer:innen in eine Variante werden in zukünftigen Schritten einer Vorschau berücksichtigt.

Ebenso erkennen Filter Aktionen, die als Ergebnis der Interaktion der Testnutzer:in mit anderen Schritten im Canvas stattgefunden haben. Dieser Vorschaumodus erkennt beispielsweise, dass Nutzer:innen auf einen Nachrichtenschritt gestoßen sind, der zuvor im Canvas „gesendet“ wurde, und er erkennt, dass die Testnutzer:in eine „Aktion ausgeführt“ hat, um durch einen Aktionspfad voranzukommen.

Weitere Informationen zum responsiven Verhalten finden Sie unter [Exit-Kriterien]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria).

## Connected Content {#connected-content}

Connected Content wird ausgeführt, wenn es im Canvas enthalten ist. Das bedeutet, wenn Sie ein Canvas testen, das Connected-Content-Aufrufe oder Content Blocks mit Connected Content enthält, sendet das Canvas möglicherweise die Connected-Content-Aufrufe, was die Daten verändern könnte, auf die in anderen Campaigns oder Canvases verwiesen wird.

Wenn Sie Nutzerpfade in der Vorschau anzeigen, sollten Sie den Connected Content entfernen, der Nutzerprofile oder Daten verändert, auf die in anderen Canvases oder Campaigns verwiesen wird.

## Webhooks {#webhooks}

Webhooks werden ausgeführt, wenn Testnachrichten gesendet werden, jedoch nicht während des Testlaufs. Ähnlich wie bei Connected-Content sollten Sie Webhooks entfernen, die Nutzerprofile oder Daten verändern, auf die in anderen Canvases oder Campaigns verwiesen wird.

## Kontextvariablen und Seed-Gruppen {#context-variables-and-seed-groups}

Für einen Nachrichten-Schritt mit E-Mail als Messaging-Kanal senden Seed-Gruppen Seed-Kopien von E-Mails, wenn Nutzer:innen diesen Schritt im Canvas erreichen. Diese Seed-Kopien werden nicht als Teil der eigenen Canvas-Journeys der Seed-Gruppen-Empfänger:innen gesendet, sodass Braze keine [Kontext-Schritte]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) ausführt und keine Kontextvariablen für diese Empfänger:innen auswertet. Wenn Ihr E-Mail-Inhalt auf Kontextvariablen verweist, erhalten Seed-Gruppen-Empfänger:innen eine Seed-Kopie, in der diese Daten nicht befüllt sind. Um Nachrichten zu testen, die auf Kontextvariablen-Daten angewiesen sind, verwenden Sie die **Test Canvas**-Vorschau mit Testversand anstelle von Seed-Gruppen.

## Von Nutzer:innen empfangene Nachrichten anzeigen {#view-messages-sent-to-users}

„Nutzerpfade in der Vorschau anzeigen“ simuliert eine Journey – es ersetzt nicht die Überprüfung tatsächlicher Sendungen im Nutzerprofil. Um Nachrichten zu überprüfen, die Braze an bestimmte Nutzer:innen gesendet hat, öffnen Sie deren Profil über **Audience** > **Search Users** und verwenden Sie dann die Tabs **Messaging History** und **Engagement**.

Informationen zu Suchfeldern, Tab-Details und dem 30-Tage-Fenster für den Messaging-Verlauf finden Sie unter [Nutzerprofile]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles).

## Anwendungsfall {#use-case}

In diesem Szenario ist der Canvas so eingerichtet, dass Nutzer:innen angesprochen werden, die keine Sitzung in einer App hatten. Diese Journey umfasst einen Nachrichtenschritt mit einer Willkommens-E-Mail, einen Verzögerungsschritt von einem Tag und einen Zielgruppenpfade-Schritt, der sich in zwei Pfade aufteilt: Nutzer:innen mit mindestens einer Sitzung und alle anderen. Je nachdem, in welchen Zielgruppenpfad eine Nutzer:in fällt, wird der nachfolgende Nachrichtenschritt gesendet.

![Ein Beispiel für einen Canvas mit einem Nachrichtenschritt, einem Verzögerungsschritt, einem Zielgruppenpfade-Schritt und zwei Nachrichtenschritten.]({% image_buster /assets/img/preview_user_path_example.png %}){:style="max-width:70%"}

Da unsere Testnutzer:in die Canvas-Eintrittskriterien erfüllt, kann sie den Canvas betreten und die User-Journey durchlaufen. Da unsere Testnutzer:in die App jedoch am letzten Kalendertag nicht geöffnet hat, wird sie auf dem Pfad „Alle anderen“ weitergeleitet und erhält eine Push-Benachrichtigung mit dem Text: „Letzte Chance! Schließe deine erste Aufgabe ab und sichere dir einen exklusiven Bonus.“

![Der Abschnitt „Testergebnisse“ zeigt, dass die Testnutzer:in die Eintrittskriterien erfüllt hat, und bietet eine Zusammenfassung der Journey, einschließlich der Schritte, die gesendet wurden.]({% image_buster /assets/img/preview_user_path_results_example.png %})