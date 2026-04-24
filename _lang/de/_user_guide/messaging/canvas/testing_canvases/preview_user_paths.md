---
nav_title: Nutzerpfade in der Vorschau anzeigen
article_title: Nutzerpfade in der Vorschau anzeigen
page_order: 0.3
alias: /preview_user_paths/
description: "Diese Seite beschreibt, wie Sie Nutzerpfade in Canvas in der Vorschau anzeigen können."
Tool:
  - Canvas
---

# Nutzerpfade in Canvas in der Vorschau anzeigen

> Erleben Sie die Canvas-Journey, die Sie für Ihre Nutzer:innen erstellt haben. Dazu gehört eine Vorschau des Timings und der Nachrichten, die Ihre Nutzer:innen erhalten. Diese Testläufe dienen der Qualitätssicherung, damit Ihre Nachrichten an die richtige Zielgruppe gesendet werden – und zwar bevor Sie Ihren Canvas versenden.

## Einen Testlauf erstellen

Folgen Sie diesen Schritten, um Ihre Nutzer-Journey in der Vorschau anzuzeigen:

1. Öffnen Sie Ihren Canvas-Builder. Speichern Sie alle ungespeicherten Änderungen und beheben Sie eventuelle Fehler.
2. Wählen Sie **Test Canvas** in der Fußzeile aus.
3. Wählen Sie eine:n Testnutzer:in aus.
4. (Optional) Wählen Sie eine:n Empfänger:in für den Test aus.
5. Wählen Sie **Run Test** aus.

Sie können eine Vorschau ausführen, auch wenn Sie keine Berechtigung zum Bearbeiten eines Canvas haben. Allerdings wird diese Vorschau mit ungespeicherten Änderungen ausgeführt, falls welche vorhanden sind.

### Unterstützte Schritte

Die folgenden Schritte werden unterstützt:
- Nachricht 
- Zielgruppenpfad
- Decision-Split
- Verzögerung
- Aktions-Pfad
- Experiment-Pfad
- Nutzeraktualisierung (nur im UI-Editor, d. h. Schritte mit JSON-Editor werden übersprungen)

Wenn der Test auf einen Schritttyp trifft, der oben nicht aufgeführt ist, wird der nicht unterstützte Schritt übersprungen, und die/der Testnutzer:in fährt mit dem nächsten unterstützten Schritt fort.

### Canvas-Schritt-Details

Um weitere Details zu den Eingangskriterien anzuzeigen, wählen Sie **See more** aus. Schritte mit Segmentierung zeigen die erfüllten oder nicht erfüllten Kriterien an. Nachrichten zeigen dies auch für Zustellungsvalidierungen und Kanalberechtigung an. Nachrichtenschritte zeigen, welche Kanäle gesendet bzw. nicht gesendet wurden.

### Liquid

Braze verarbeitet Liquid-Logik während eines Testlaufs, auch wenn Sie keine tatsächliche Testnachricht senden. Das bedeutet, dass die [Nachricht-abbrechen-Logik]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/#abort-messages) und andere Liquid-Logik berücksichtigt werden und die Canvas-Nutzer-Journey beeinflussen können.

Wenn Ihre Vorschau den letzten Schritt Ihrer Nutzer-Journey sendet, anstatt abzubrechen, verwendet die Vorschau möglicherweise die aktuelle Uhrzeit als Testzeitpunkt für die Liquid-Auswertung und nicht die tatsächliche Zeit, zu der sich die/der Nutzer:in basierend auf der Canvas-Eintrittszeit im Schritt befinden würde.

## Vorschau für Timing

Bei geplanten Canvases tritt die/der Testnutzer:in zum nächsten geplanten Eintrittszeitpunkt ein. Bei aktionsbasierten Canvases mit Startdatum tritt die/der Testnutzer:in zum Startdatum und zur Startzeit ein.

Obwohl die Standard-Startzeiten weiterhin gelten, ist die Eintrittszeit in allen Fällen konfigurierbar, sodass Sie ein Datum in der Vergangenheit oder Zukunft simulieren können. Sie können jedoch nicht vor dem Startdatum oder nach dem Enddatum des Canvas testen.

Nachrichten- und Verzögerungsschritte zeigen die Zeit an, zu der eine/ein Nutzer:in fortschreiten oder die Nachricht erhalten würde, ohne dass die Verzögerungen neu konfiguriert werden müssen. Beachten Sie, dass die Schritte zwar anzeigen, ob intelligentes Timing verwendet wird, diese Vorschau des Nutzerpfads jedoch keine Schätzung für eine:n Testnutzer:in berechnet.

Bei Canvases mit einem Aktionstrigger wie „Änderung des Werts eines angepassten Attributs" versucht Braze, die Änderung zu simulieren, indem das Attribut der/des Nutzers:in im Trigger vorübergehend auf leer gesetzt wird – **nur für den Testlauf des Canvas** (dies hat keinen Einfluss auf das Nutzerprofil). Damit soll getestet werden, dass sich das Attribut von seinem aktuellen Wert ändert.

## Wann Nutzer:innen eintreten und austreten

Testnutzer:innen treten in die Vorschau ein, auch wenn sie im echten Betrieb nicht berechtigt wären. Wenn sie nicht berechtigt sind, können Sie sehen, warum sie die Kriterien nicht erfüllt haben. Wenn eine/ein Testnutzer:in in die Vorschau eintritt, wird angenommen, dass sie/er die Zielgruppenkriterien erfüllt und die Aktionstrigger-Kriterien ausgeführt hat. Zum Beispiel wird bei einem Canvas, der angepasste Events in den Eingangskriterien verwendet, angenommen, dass die/der Testnutzer:in das angepasste Event wie in den Eingangskriterien erwartet ausgeführt hat. Wenn dasselbe angepasste Event jedoch an anderer Stelle im Canvas verwendet wird (z. B. in den Austrittskriterien), sollten Sie berücksichtigen, wie sich dies auf Ihren Nutzerpfad auswirken könnte.

Events, API-Trigger, angepasste Attribute und Canvas-Eingangs-Eigenschaften, die angenommen werden, um eine:n Testnutzer:in in den Canvas eintreten zu lassen, werden nicht im tatsächlichen Nutzerprofil aktualisiert und bleiben nicht über den Testlauf hinaus bestehen. Wenn beispielsweise während des Tests ein angepasstes Attribut als Canvas-Trigger verwendet wird, werden die Trigger-Kriterien auf die Vorschau der/des Nutzers:in angewendet, **als ob** sie/er die Änderung des angepassten Attributs ausgelöst hätte.

### Hinweis

Wenn Sie einen Aktions-Pfad mit Aktionen testen, die den Austrittskriterien entsprechen (einschließlich Event-Eigenschaften), werden die Austrittskriterien ausgelöst und der Testlauf endet. Wenn Sie einen Nachrichtenschritt testen, der den Austrittskriterien entspricht, werden die Austrittskriterien ausgelöst und der Testlauf endet.

Derzeit können Sie kein bestimmtes Event oder keine bestimmte Eigenschaft innerhalb eines Aktions-Pfads auswählen, um Austrittskriterien auszulösen (nur den Pfad als Ganzes). Wenn eine/ein Nutzer:in potenziell mehrere Austrittskriterien erfüllen könnte, wird das erste verarbeitete Kriterium, das erfüllt wird, als Ergebnis angezeigt.

## Experimentpfade und Canvas-Varianten

- Bei Canvases mit Varianten auf oberster Ebene wählen Sie zu Beginn des Tests eine Variante aus.
- Bei Experimentpfaden wählen Sie die Variante aus, durch die die/der Nutzer:in fortschreitet, wenn sie/er auf den Schritt trifft.
- Bei Experimentpfaden mit personalisiertem Pfad oder Gewinnervariante gibt es zwar eine Verzögerungsperiode, während der die/der Testnutzer:in in einem Nachrichtenschritt wartet, diese Verzögerung wird jedoch nicht berücksichtigt, da Braze davon ausgeht, dass die/der Nutzer:in sofort durch die ausgewählte Variante fortgeschritten ist.

## Testsendungen

Sie können sich dafür entscheiden, Testnachrichten an eine interne Testgruppe oder eine:n einzelne:n Nutzer:in zu senden, während der Testlauf ausgeführt wird. Das bedeutet, dass nur Nachrichten gesendet werden, auf die die/der Nutzer:in entlang des Testpfads trifft. Die Empfänger:innen erhalten Nachrichten standardmäßig mit ihren eigenen Attributen, aber Sie können diese mit den Attributen der/des Testnutzers:in überschreiben.

Um alle Testnachrichten in einem Canvas auf einmal zu senden – unabhängig vom Pfad und ohne den Pfad in der Vorschau anzuzeigen – können Sie **Send All Test Messages** im Tab **Test Sends** auswählen.

## Reaktionsfähigkeit

Canvas-Schritte reagieren auf das Timing bei der Vorschau von Nutzerpfaden. Aktualisierungen, die über den Nutzeraktualisierungsschritt vorgenommen werden, werden in nachfolgenden Schritten im Ablauf berücksichtigt, aber nicht auf das tatsächliche Nutzerprofil angewendet. Die Auswirkungen des Eintritts einer/eines Nutzers:in in eine Variante werden in zukünftigen Schritten der Vorschau berücksichtigt.

Ebenso erkennen Filter Aktionen, die als Ergebnis der Interaktion der/des Testnutzers:in mit anderen Schritten im Canvas aufgetreten sind. Zum Beispiel erkennt dieser Vorschaumodus, dass eine/ein Nutzer:in auf einen Nachrichtenschritt gestoßen ist, der zuvor im Canvas „gesendet" wurde, und er erkennt, dass die/der Testnutzer:in eine „Aktion ausgeführt" hat, um durch einen Aktions-Pfad fortzuschreiten.

Weitere Details zum reaktionsfähigen Verhalten finden Sie unter [Austrittskriterien]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria/).

## Connected-Content

Connected-Content wird ausgeführt, wenn er im Canvas enthalten ist. Das bedeutet: Wenn Sie einen Canvas testen, der Connected-Content-Aufrufe oder Content-Blöcke mit Connected-Content enthält, kann der Canvas die Connected-Content-Aufrufe senden, was die in anderen Kampagnen oder Canvases referenzierten Daten verändern könnte.

Wenn Sie Nutzerpfade in der Vorschau anzeigen, sollten Sie den Connected-Content entfernen, der Nutzerprofile oder Daten verändert, die in anderen Canvases oder Kampagnen referenziert werden.

## Webhooks

Webhooks werden ausgeführt, wenn Testnachrichten gesendet werden, aber nicht während des Testlaufs. Ähnlich wie bei Connected-Content sollten Sie Webhooks entfernen, die Nutzerprofile oder Daten verändern, die in anderen Canvases oder Kampagnen referenziert werden.

## Kontextvariablen und Seed-Gruppen

Bei einem Nachrichtenschritt mit E-Mail als Messaging-Kanal senden Seed-Gruppen Seed-Kopien von E-Mails, wenn eine/ein Nutzer:in diesen Schritt im Canvas erreicht. Diese Seed-Kopien werden nicht als Teil der eigenen Canvas-Journeys der Seed-Gruppen-Empfänger:innen gesendet, sodass Braze keine [Kontextschritte]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/) ausführt oder Kontextvariablen für diese Empfänger:innen auswertet. Wenn Ihr E-Mail-Inhalt Kontextvariablen referenziert, erhalten die Seed-Gruppen-Empfänger:innen eine Seed-Kopie ohne diese Daten. Um Nachrichten zu testen, die auf Kontextvariablendaten angewiesen sind, verwenden Sie die **Test Canvas**-Vorschau mit Testsendungen anstelle von Seed-Gruppen.

## Anwendungsfall

In diesem Szenario ist der Canvas so eingerichtet, dass er Nutzer:innen anspricht, die keine Sitzung in einer App hatten. Diese Journey umfasst einen Nachrichtenschritt mit einer Willkommens-E-Mail, einen Verzögerungsschritt von einem Tag und einen Zielgruppenpfade-Schritt, der sich in zwei Pfade aufteilt: Nutzer:innen mit mindestens einer Sitzung und alle anderen. Je nachdem, in welchen Zielgruppenpfad eine/ein Nutzer:in fällt, wird der nachfolgende Nachrichtenschritt gesendet.

![Ein Beispiel für einen Canvas mit einem Nachrichtenschritt, einem Verzögerungsschritt, einem Zielgruppenpfade-Schritt und zwei Nachrichtenschritten.]({% image_buster /assets/img/preview_user_path_example.png %}){:style="max-width:70%"}

Da unsere/unser Testnutzer:in die Canvas-Eingangskriterien erfüllt, kann sie/er in den Canvas eintreten und die Nutzer-Journey durchlaufen. Da unsere/unser Testnutzer:in die App jedoch am letzten Kalendertag nicht geöffnet hat, geht sie/er den Pfad „Alle anderen" weiter und erhält eine Push-Benachrichtigung mit dem Text: „Letzte Chance! Schließen Sie Ihre erste Aufgabe ab und erhalten Sie einen exklusiven Bonus."

![Der Abschnitt „Test Results" zeigt, dass die/der Testnutzer:in die Eingangskriterien erfüllt hat, und bietet eine Zusammenfassung der Journey, einschließlich der Schritte, die gesendet wurden.]({% image_buster /assets/img/preview_user_path_results_example.png %})