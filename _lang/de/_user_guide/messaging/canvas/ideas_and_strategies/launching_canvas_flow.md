---
nav_title: Mit Canvas Flow starten
article_title: Mit Canvas Flow starten
page_order: 3
description: "Dieser Referenzartikel beschreibt, wie Sie einen mit Canvas Flow erstellten Canvas vor dem Start vorbereiten und testen."
page_type: reference
tool: Canvas
---

# Mit Canvas Flow starten {#launch-with-canvas-flow}

> Dieser Referenzartikel beschreibt, wie Sie einen mit Canvas Flow erstellten Canvas vor dem Start vorbereiten und testen. Dazu gehört die Identifizierung wichtiger Canvas-Checkpoints wie Canvas-Eingangsbedingungen, Zielgruppen-Zusammenfassungen und Nutzer:innen-Segmente.

Wenn Sie sich auf den Start Ihres Canvas vorbereiten, empfiehlt Braze, Ihren Canvas in jeder Phase des Canvas-Builders auf Einstellungen zu überprüfen, die sich auf den Nachrichtenversand auswirken können, darunter:
* [Race-Conditions](#race-conditions)
* [Zustellzeiten](#delivery-times)
* [Nutzer:innen-Segmente](#segment-users)

## Race-Conditions {#race-conditions}

Berücksichtigen Sie die [Race-Conditions]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions), die vor dem Start Ihres Canvas auftreten können.

Um in einen Canvas einzutreten, müssen Nutzer:innen sich in der Entry-Zielgruppe befinden, bevor der Entry-Zeitplan eintritt – unabhängig davon, ob der Canvas geplant, aktionsbasiert oder API-getriggert ist.

![Ein aktionsbasierter Canvas, der Nutzer:innen aufnimmt, wenn sie einen beliebigen Kauf tätigen, in der Ortszeit der Nutzer:innen vom 30. April 2025 um 12 Uhr bis zum 7. Mai 2025 um 12 Uhr.]({% image_buster /assets/img_archive/launch_with_canvas_flow_example.png %}){: style="max-width:75%;"}

Beachten Sie, dass Nutzer:innen, die sich erst nach dem Start des Canvas für Ihre Entry-Zielgruppe qualifizieren, nicht in den Canvas eintreten werden.

{% alert tip %}
Sehen Sie sich die [Entry-Zeitplan-Typen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule) an, um Hinweise und Details zu erhalten, wann Sie geplante, aktionsbasierte oder API-getriggerte Zustellung für Ihren Canvas verwenden sollten!
{% endalert %}

### Entry-Zielgruppen-Filter überprüfen {#review-entry-audience-filters}

Vermeiden Sie es generell, einen aktionsbasierten oder API-getriggerten Canvas mit demselben Trigger wie dem Zielgruppen-Filter zu konfigurieren. Nachdem ein Canvas gestartet wurde, werden Nutzer:innen, die eine bestimmte Aktion ausführen, beispielsweise in die Entry-Zielgruppe aufgenommen, sodass es nicht nötig ist, das Event als Zielgruppen-Filter hinzuzufügen.

Weitere Details zu verfügbaren Segmentierungs-Filtern für die Zielgruppenansprache finden Sie unter [Segmentierungs-Filter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).

### Mehrere API-Anfragen bündeln {#batch-multiple-api-requests}

Stellen Sie Ihre Anfragen im selben API-Aufruf statt in mehreren Aufrufen, um sicherzustellen, dass das Nutzerprofil zuerst erstellt oder aktualisiert wird. Weitere Beispiele finden Sie unter [Mehrere Endpunkte verwenden]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions#using-multiple-api-endpoints).

### Eine Verzögerung hinzufügen {#add-a-delay}

Eine weitere Möglichkeit, Race-Conditions zu vermeiden, besteht darin, den Verzögerungsschritt (idealerweise auf 5 Minuten eingestellt) als ersten Schritt Ihres Canvas zu verwenden.

Dies gibt Zeit, damit Attribute, E-Mail-Adressen und Push-Token für neue Nutzerprofile verarbeitet werden, bevor sie für die folgenden Canvas-Schritte angesprochen werden. Ohne diesen Verzögerungsschritt ist es möglich, dass eine E-Mail an Nutzer:innen gesendet wird, deren E-Mail-Adresse noch nicht aktualisiert wurde.

## Zustellzeiten {#delivery-times}

Das Festlegen einer Canvas-Zustellzeit in Realtime kann zu höherem Engagement und höheren Konversionsraten führen. Beachten Sie, welche Zustellzeit Sie für Ihren Canvas eingestellt haben. Um Engagement und Konversionsraten zu steigern, ist es am besten, Canvases in Realtime zu triggern, anstatt auf geplanter, wiederkehrender Basis.

Wenn Sie eine geplante Zustellung für Ihren Canvas ausgewählt haben, empfiehlt Braze, Ihren Canvas mindestens 24 Stunden vor dem gewünschten Starttermin zu planen, um Anpassungen an Ihrem Canvas zu ermöglichen.

## Nutzer:innen-Segmente {#user-segments}

Bevor Sie Ihre Canvas Flow User-Journey mit Komponenten überladen, überlegen Sie, wie Sie eine User-Journey einfach halten können. Verwenden Sie die vereinfachte Ansicht im Canvas-Editor, um einen besseren Überblick über die Verzweigungen Ihrer User-Journey zu erhalten.

Es gibt vier Hauptkomponenten, die Sie verwenden können, um Ihre Nutzer:innen auf einfache und effektive Weise zu segmentieren:

* [Zielgruppenpfade](#audience-paths)
* [Decision-Split](#decision-split)
* [Aktionspfade](#action-paths)
* [Experimentpfade](#experiment-paths)

### Zielgruppenpfade {#audience-paths}

Verwenden Sie [Zielgruppenpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths)-Schritte, um Nutzer:innen innerhalb des Canvas basierend auf angepassten Attributen, angepassten Events und früheren Nachrichten-Engagement-Daten aus Nutzerprofilen zu segmentieren.

### Decision-Split {#decision-split}

Der [Decision-Split]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split)-Schritt ermöglicht es Ihnen, Ihre Nutzer:innen basierend auf ihren Antworten auf eine Ja/Nein-Frage auf verschiedene User-Journey-Pfade zu leiten.

### Aktionspfade {#action-paths}

[Aktionspfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) konzentrieren sich auf die Segmentierung von Nutzer:innen basierend auf Realtime-Verhalten wie angepassten Events, Kauf-Events und Änderungen angepasster Attribute.

### Experimentpfade {#experiment-paths}

Ähnlich wie Aktionspfade können Sie [Experimentpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step)-Schritte in Ihrem Canvas nutzen, um mehrere Canvas-Pfade gegeneinander zu testen, zusammen mit einer Kontrollgruppe. Dies verfolgt die Pfad-Performance und ermöglicht es Ihnen, fundierte Entscheidungen beim Aufbau Ihrer Canvas-Journey zu treffen.

## Testen vor dem Start {#testing-before-launch}

Nachdem Sie die Details Ihres Canvas überprüft haben, sehen Sie sich [Test-Canvases senden]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases) an, um verschiedene Methoden kennenzulernen, mit denen Sie Ihren Canvas mit Testnutzer:innen testen können.

## Start-Checkliste {#launch-checklist}

### Nutzerverfügbarkeit prüfen {#check-user-availability}

- Stellen Sie sicher, dass Ihre Nutzer:innen Ihre Segmentierungskriterien erfüllen.
- Bestätigen Sie, dass ihr Abo-Status „Abonniert“ oder „Opted-in“ ist und ihr Push-Token vorhanden ist. Wenn Sie diese als Canvas-Eingangsregeln hinzugefügt haben, ist es möglich, dass sich die Nutzer:innen zwischen dem Eintritt in Ihren Canvas und dem Empfang des Nachrichten-Schritts abgemeldet haben.
- Bestätigen Sie, dass sie Ihren Canvas-Sendeeinstellungen entsprechen. (Wenn Nutzer:innen „Abonniert“ sind, die Einstellungen aber auf „Opted-in“ stehen, werden Nutzer:innen für den Kanal nicht aktiviert.)
- Wenn globales Frequency-Capping für Ihren Canvas aktiviert ist, prüfen Sie, ob Ihre Regeln einschränken, wie oft jede:r Nutzer:in eine Nachricht von einem bestimmten Kanal erhalten kann.
- Wenn Ruhezeiten aktiviert sind, könnte Ihre Nachrichtensendezeit beeinflusst werden, was bedeutet, dass Ihre Nachricht zum nächsten verfügbaren Zeitpunkt (wenn die Ruhezeiten enden) gesendet oder ganz abgebrochen werden könnte.
- Prüfen Sie die Nutzerverfügbarkeit für zusätzliche Filter in Ihrem Canvas-Schritt.

### Bestätigen, dass das erforderliche angepasste Event oder der Kauf durchgeführt wurde {#confirm-that-they-performed-the-prerequisite-custom-event-or-purchase}

- Prüfen Sie, ob eine Race-Condition vorliegt, die sich auf die Nachrichten auswirkt, die Nutzer:innen erhalten, wenn sie mehrere Aktionen gleichzeitig triggern.
- Stellen Sie sicher, dass keine spezifischen Filter im Schritt vorhanden sind, die Nutzer:innen am Empfang der Nachricht gehindert haben könnten.
- Suchen Sie nach Konflikten zwischen verschiedenen Schritten innerhalb desselben Canvas. Beispielsweise könnten Nutzer:innen, die die Nachricht nicht erhalten haben, durch einen Filter gestoppt worden sein, der den Abschluss eines anderen Schritts in einem anderen Branch erfordert.
- Bestätigen Sie, dass Nutzer:innen zusätzliche Validierungsregeln erfüllen.
- Bestätigen Sie, dass der Canvas-Schritt zum Zeitpunkt des Versands mit dem vorhergehenden Schritt verbunden war.

### Bestätigen, dass Ihr Canvas korrekt gespeichert wird und alle Schritte gültig sind {#confirm-your-canvas-saves-correctly-and-all-steps-are-valid}

Wenn Ihr Canvas nicht lädt und nicht fortschreitet, kann dies daran liegen, dass eine frühere Version des Canvas nicht korrekt gespeichert wurde und ungültige Schritte enthält. Sie können den Canvas über das Dashboard duplizieren. Wenn das Problem weiterhin besteht, eröffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support).

## Fehlerbehebung {#troubleshooting}

{% details Warum erhalten meine Nutzer:innen meine Canvas-Nachrichten nicht? %}
**Nutzerverfügbarkeit prüfen**
- Stellen Sie sicher, dass sie Ihre Segmentierungskriterien erfüllen.
- Bestätigen Sie, dass ihr Push-Abo-Status „Abonniert“ oder „Opted-in“ ist **und** ihr **Push aktiviert**-Status auf „true“ gesetzt ist. Wenn Sie diese als Canvas-Eingangsregeln hinzugefügt haben, ist es möglich, dass sich die Nutzer:innen zwischen dem Eintritt in Ihren Canvas und dem Empfang des Nachrichten-Schritts abgemeldet haben.
- Bestätigen Sie, dass sie Ihren Canvas-Sendeeinstellungen entsprechen. (Wenn Nutzer:innen „Abonniert“ sind, die Einstellungen aber auf „Opted-in“ stehen, werden Nutzer:innen für den Kanal nicht aktiviert.)
- Wenn globales Frequency-Capping für Ihren Canvas aktiviert ist, prüfen Sie, ob Ihre Regeln einschränken, wie oft jede:r Nutzer:in eine Nachricht von einem bestimmten Kanal erhalten kann.
- Wenn Ruhezeiten aktiviert sind, könnte Ihre Nachrichtensendezeit beeinflusst werden, was bedeutet, dass Ihre Nachricht zum nächsten verfügbaren Zeitpunkt (wenn die Ruhezeiten enden) gesendet oder ganz abgebrochen werden könnte.

**Nutzerverfügbarkeit für zusätzliche Filter in Ihrem Canvas-Schritt prüfen**
- Bestätigen Sie, dass das erforderliche angepasste Event oder der Kauf durchgeführt wurde.
- Prüfen Sie, ob eine [Race-Condition]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions) vorliegt, die sich auf die Nachrichten auswirkt, die Nutzer:innen erhalten, wenn sie mehrere Aktionen gleichzeitig triggern.
- Stellen Sie sicher, dass keine spezifischen Filter im Schritt vorhanden sind, die Nutzer:innen am Empfang der Nachricht gehindert haben könnten.
- Suchen Sie nach Konflikten zwischen verschiedenen Schritten innerhalb desselben Canvas. Beispielsweise könnten Nutzer:innen, die die Nachricht nicht erhalten haben, durch einen Filter gestoppt worden sein, der den Abschluss eines anderen Schritts in einem anderen Branch erfordert.
- Bestätigen Sie, dass Nutzer:innen zusätzliche Validierungsregeln erfüllen.
- Bestätigen Sie, dass der Canvas-Schritt zum Zeitpunkt des Versands mit dem vorhergehenden Schritt verbunden war.
{% enddetails %}