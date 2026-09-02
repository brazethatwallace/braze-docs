---
nav_title: Ausstiegskriterien mit Eingangs-Events abgleichen
article_title: Ausstiegskriterien mit Eingangs-Events abgleichen
page_order: 5
page_type: tutorial
description: "Erfahren Sie, wie Sie Ausstiegskriterien und Aktionspfade einrichten, die Event-Eigenschaften mit Canvas-Eingangs-Eigenschaften vergleichen, sodass Nutzer:innen nur dann aussteigen oder verzweigt werden, wenn sie genau die Aktion abschließen, mit der sie eingetreten sind."
tool: Canvas
---

# Ausstiegskriterien mit Eingangs-Events abgleichen {#matching-exit-criteria-to-entry-events}

> In diesem Artikel erfahren Sie, wie Sie Ausstiegskriterien und Aktionspfade einrichten, die direkt mit dem Canvas-Eingangs-Event korrelieren, sodass Nutzer:innen nur dann aussteigen oder verzweigt werden, wenn sie eine bestimmte Aktion ausführen, die mit dem Grund ihres Canvas-Eintritts zusammenhängt.

Durch den Vergleich von Event-Eigenschaften mit [Canvas-Eingangs-Eigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties) können Sie hochgradig zielgerichtete Flows erstellen. In einem Canvas für abgebrochene Checkouts können Sie beispielsweise konfigurieren, dass Nutzer:innen nur dann aussteigen, wenn sie genau den Artikel kaufen, den sie abgebrochen haben, während sie weiterhin Erinnerungsnachrichten erhalten, wenn sie einen anderen Artikel kaufen.

Dieser Ansatz verwendet [Kontext-Variablen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables), um Eigenschaften über Events hinweg zu vergleichen. Das Muster lässt sich auf viele Szenarien jenseits von E-Commerce anwenden, darunter Richtlinien-Verlängerungen, Buchungserinnerungen und Abo-Management.

## Ausstiegskriterien: Den Canvas verlassen, wenn eine übereinstimmende Aktion erfolgt {#exit-criteria-exiting-the-canvas-when-a-matching-action-occurs}

Verwenden Sie [Ausstiegskriterien]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria), wenn Nutzer:innen den Canvas vollständig verlassen sollen, nachdem sie eine Aktion ausgeführt haben, die mit ihrem Eingangs-Event übereinstimmt.

### Beispiel: Abgebrochener Ticketkauf {#example-abandoned-ticket-purchase}

In diesem Szenario treten Nutzer:innen in den Canvas ein, wenn sie das angepasste Event `Selected Ticket` ausführen, das eine Eigenschaft namens `event_id` enthält. Die Ausstiegskriterien sind so konfiguriert, dass beim Triggern des angepassten Events `Purchased Ticket` – das ebenfalls eine Eigenschaft namens `event_id` enthält – die Event-Eigenschaft des Ausstiegs-Events mit der Event-Eigenschaft des Eingangs-Events verglichen wird. Stimmen beide überein, verlassen die Nutzer:innen den Canvas.

Das bedeutet:

- Wenn Nutzer:innen dasselbe Ticket kaufen, das sie ursprünglich ausgewählt haben, verlassen sie den Canvas und erhalten keine Erinnerungen mehr.
- Wenn Nutzer:innen ein anderes Ticket kaufen, bleiben sie im Canvas und erhalten weiterhin Follow-up-Nachrichten zum ursprünglichen Ticket.

So richten Sie dies ein:

1. Richten Sie einen aktionsbasierten Canvas-Eingang mit dem triggernden angepassten Event (z. B. `Selected Ticket`) und der relevanten Eigenschaft (z. B. `event_id`) ein.
2. Konfigurieren Sie im Schritt **Zielgruppe** das Ausnahme-Event der Ausstiegskriterien mit dem abschließenden angepassten Event (z. B. `Purchased Ticket`).
3. Wählen Sie **Eigenschaftsfilter hinzufügen** aus und fügen Sie einen Filter hinzu, bei dem der Vergleich der Basiseigenschaft `event_id` auf `equals` gesetzt ist.
4. Aktivieren Sie den Toggle **Wert personalisieren**, setzen Sie den **Personalisierungstyp** auf `Context Variables` und das **Attribut** auf `event_id`.

Dadurch wird die `event_id` des `Purchased Ticket`-Events mit der `event_id` verglichen, die beim ursprünglichen Canvas-Eingangs-Event gespeichert wurde. Weitere Details zur Konfiguration dieser Filter finden Sie unter [Beispiele für Ausstiegskriterien]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#exit-criteria-examples).

## Aktionspfade: Verzweigung basierend auf einer übereinstimmenden Aktion {#action-paths-branching-based-on-a-matching-action}

Verwenden Sie [Aktionspfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths), wenn Nutzer:innen im Canvas bleiben, aber je nachdem, ob ihre nachfolgende Aktion mit dem Eingangs-Event übereinstimmt, einen anderen Pfad einschlagen sollen.

### Beispiel: Abgebrochener Checkout mit Verzweigungspfaden {#example-abandoned-checkout-with-branching-paths}

In diesem Szenario erhalten Nutzer:innen, die einen Artikel ausgewählt, aber den Kauf nicht abgeschlossen haben, zunächst eine Nachricht zum abgebrochenen Checkout. Anschließend werden sie in einem Aktionspfade-Schritt eine Woche lang gehalten, bevor sie basierend auf ihrem Verhalten in diesem Zeitraum in drei Pfade sortiert werden:

- **Ursprünglichen Kauf abgeschlossen:** Die ID der angepassten Event-Eigenschaft stimmt mit der ID der Eingangs-Eigenschaft überein. Diese Nutzer:innen könnten eine Dankesnachricht oder eine Cross-Sell-Empfehlung erhalten.
- **Einen anderen Kauf getätigt:** Die ID der angepassten Event-Eigenschaft stimmt nicht mit der ID der Eingangs-Eigenschaft überein. Diese Nutzer:innen könnten eine Erinnerung an den ursprünglichen Artikel erhalten.
- **Keinen Kauf getätigt:** Fällt in die Gruppe **Alle anderen**. Diese Nutzer:innen könnten einen stärkeren Anreiz oder eine letzte Erinnerung erhalten.

So richten Sie dies ein:

1. Fügen Sie einen [Aktionspfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)-Schritt hinzu und legen Sie das Auswertungsfenster fest (z. B. eine Woche).
2. Fügen Sie für die erste Aktionsgruppe (ursprünglicher Kauf) einen Trigger für das abschließende angepasste Event hinzu (z. B. `Purchased_Ticket`). Wählen Sie **Eigenschaftsfilter hinzufügen** aus und fügen Sie einen Filter hinzu, bei dem der Vergleich der Basiseigenschaft `event_id` auf `equals` gesetzt ist. Aktivieren Sie **Wert personalisieren**, setzen Sie den **Personalisierungstyp** auf `Context Variables` und das **Attribut** auf `event_id`.
3. Fügen Sie für die zweite Aktionsgruppe (anderer Kauf) dasselbe Trigger-Event hinzu, setzen Sie den Vergleich jedoch auf `does not equal` mit derselben Kontext-Variablen-Konfiguration.
4. Verwenden Sie die Gruppe **Alle anderen** für Nutzer:innen, die das abschließende Event überhaupt nicht ausgeführt haben.

Weitere Details zur Konfiguration dieser Filter finden Sie unter [Beispiele für Aktionspfade]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#action-path-examples).

## Weitere Anwendungsfälle {#other-applications}

Obwohl in diesem Artikel ein Beispiel für einen abgebrochenen Kauf verwendet wird, können Sie dasselbe Muster auf jedes Szenario anwenden, in dem eine abschließende Aktion mit der Eingangs-Aktion korrelieren muss, darunter:

- **Richtlinien-Verlängerungen:** Nutzer:innen aussteigen lassen, die die spezifische Richtlinie verlängern, die den Canvas getriggert hat.
- **Buchungserinnerungen:** Nutzer:innen verzweigen, je nachdem, ob sie ihre ursprüngliche Buchung bestätigt oder geändert haben.
- **Abo-Management:** Nutzer:innen unterschiedlich weiterleiten, je nachdem, ob sie den spezifischen Plan upgraden, zu dem sie aufgefordert wurden.
- **Event-Registrierungen:** Nutzer:innen aussteigen lassen, die die Registrierung für das spezifische Event abschließen, an dem sie Interesse gezeigt haben.

## Wissenswertes {#things-to-know}

- Die Konfigurationen in diesem Artikel sind illustrative Beispiele. Testen Sie alle Komponenten in Ihrer Entwicklungsumgebung, bevor Sie sie starten.
- Stellen Sie sicher, dass die Eigenschaftsnamen und Datentypen in Ihren Eingangs-Events mit denen übereinstimmen, die in Ihren Ausstiegskriterien oder Aktionspfaden verwendet werden.
- Lesen Sie den Artikel zu [Kontext-Variablen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables), um Details darüber zu erfahren, wie Eigenschaftsvergleiche über Events hinweg funktionieren.