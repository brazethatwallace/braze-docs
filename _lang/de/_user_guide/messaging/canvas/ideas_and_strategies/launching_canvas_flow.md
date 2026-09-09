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

Um in einen Canvas einzutreten, müssen Nutzer:innen zur Entry-Zielgruppe gehören, bevor der Eintritts-Zeitplan greift – unabhängig davon, ob der Canvas geplant, aktionsbasiert oder API-getriggert ist.

![Ein aktionsbasierter Canvas, der Nutzer:innen eintreten lässt, wenn sie während ihrer Ortszeit zwischen dem 30. April 2025 um 12 Uhr und dem 7. Mai 2025 um 12 Uhr einen beliebigen Kauf tätigen.]({% image_buster /assets/img_archive/launch_with_canvas_flow_example.png %}){: style="max-width:75%;"}

Beachten Sie, dass Nutzer:innen, die sich erst nach dem Start des Canvas für Ihre Entry-Zielgruppe qualifizieren, nicht in den Canvas eintreten.

{% alert tip %}
Lesen Sie [Entry-Zeitplantypen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule) für Anleitungen und Details, wann Sie die geplante, aktionsbasierte oder API-getriggerte Zustellung für Ihren Canvas verwenden sollten!
{% endalert %}

### Entry-Zielgruppenfilter überprüfen {#review-entry-audience-filters}

Vermeiden Sie es generell, einen aktionsbasierten oder API-getriggerten Canvas mit demselben Trigger wie dem Zielgruppenfilter zu konfigurieren. Nachdem ein Canvas gestartet wurde, werden Nutzer:innen, die eine bestimmte Aktion ausführen, beispielsweise automatisch in die Entry-Zielgruppe aufgenommen – daher ist es nicht nötig, das Event zusätzlich als Zielgruppenfilter hinzuzufügen.

Weitere Details zu verfügbaren Segmentierungsfiltern für die Zielgruppenansprache finden Sie unter [Segmentierungsfilter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).

### Mehrere API-Anfragen bündeln {#batch-multiple-api-requests}

Fassen Sie Ihre Anfragen in einem einzigen API-Aufruf zusammen, anstatt mehrere Aufrufe zu verwenden, um sicherzustellen, dass das Kundenprofil zuerst erstellt oder aktualisiert wird. Weitere Beispiele finden Sie unter [Mehrere Endpunkte verwenden]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions#scenario-2-using-multiple-api-endpoints).

### Eine Verzögerung hinzufügen {#add-a-delay}

Eine weitere Möglichkeit, Race-Conditions zu vermeiden, besteht darin, den Delay-Schritt (idealerweise auf 5 Minuten eingestellt) als ersten Schritt Ihres Canvas zu verwenden.

So bleibt ausreichend Zeit, damit Attribute, E-Mail-Adressen und Push-Token für neue Nutzerprofile verarbeitet werden, bevor diese für die nachfolgenden Canvas-Schritte angesprochen werden. Ohne diesen Delay-Schritt kann es vorkommen, dass eine E-Mail an Nutzer:innen gesendet wird, deren E-Mail-Adresse noch nicht aktualisiert wurde.

## Zustellungszeiten {#delivery-times}

Das Festlegen einer Canvas-Zustellungszeit in Realtime kann zu einer Steigerung von Engagement und Konversionsraten führen. Achten Sie darauf, welche Zustellungszeit Sie für Ihr Canvas eingestellt haben. Um Engagement und Konversionsraten zu steigern, ist es am besten, Canvases in Realtime zu triggern, anstatt sie auf geplanter, wiederkehrender Basis zu versenden.

Wenn Sie eine geplante Zustellung für Ihr Canvas ausgewählt haben, empfiehlt Braze, Ihr Canvas mindestens 24 Stunden vor dem gewünschten Start zu planen, damit genügend Zeit für Anpassungen an Ihrem Canvas bleibt.

## Nutzer:innen-Segmente {#user-segments}

Bevor Sie Ihren Canvas-Flow mit Komponenten überladen, überlegen Sie, wie Sie die User-Journey möglichst einfach halten können. Nutzen Sie die vereinfachte Ansicht im Canvas-Editor, um einen besseren Überblick darüber zu erhalten, wie sich Ihre User-Journey verzweigt.

Es gibt vier zentrale Komponenten, mit denen Sie Ihre Nutzer:innen einfach und effektiv segmentieren können:

* [Zielgruppenpfade](#audience-paths)
* [Decision-Split](#decision-split)
* [Aktionspfade](#action-paths)
* [Experimentpfade](#experiment-paths)

### Zielgruppenpfade {#audience-paths}

Verwenden Sie [Zielgruppenpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths)-Schritte, um Nutzer:innen innerhalb des Canvas anhand von angepassten Attributen, angepassten Events und früheren Nachrichten-Engagement-Daten aus Nutzerprofilen zu segmentieren.

### Decision-Split {#decision-split}

Der [Decision-Split]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split)-Schritt ermöglicht es Ihnen, Ihre Nutzer:innen basierend auf ihren Antworten auf eine Ja-/Nein-Frage auf verschiedene User-Journey-Pfade zu leiten.

### Aktionspfade {#action-paths}

[Aktionspfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) konzentrieren sich auf die Segmentierung von Nutzer:innen anhand von Realtime-Verhaltensweisen wie angepassten Events, Kauf-Events und Änderungen an angepassten Attributen.

### Experimentpfade {#experiment-paths}

Ähnlich wie Aktionspfade können Sie [Experimentpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step)-Schritte in Ihrem Canvas nutzen, um mehrere Canvas-Pfade gegeneinander sowie gegen eine Kontrollgruppe zu testen. Damit lässt sich die Performance der Pfade nachverfolgen, sodass Sie beim Aufbau Ihrer Canvas-Journey fundierte Entscheidungen treffen können.

## Testen vor dem Start {#testing-before-launch}

Nachdem Sie die Details Ihres Canvas überprüft haben, finden Sie unter [Test-Canvases senden]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases) verschiedene Methoden, die Sie nutzen können, um Ihren Canvas mit Testnutzer:innen zu testen.

## Checkliste für den Start {#launch-checklist}

### Nutzerverfügbarkeit prüfen {#check-user-availability}

- Stellen Sie sicher, dass Ihre Nutzer:innen Ihre Segmentierungskriterien erfüllen.
- Bestätigen Sie, dass der Abo-Status „subscribed“ oder „opted-in“ ist und das Push-Token vorhanden ist. Wenn Sie diese als Canvas-Eintrittsregeln hinzugefügt haben, ist es möglich, dass sich Nutzer:innen zwischen dem Eintritt in Ihren Canvas und dem Empfang des Nachrichtenschritts abgemeldet haben.
- Bestätigen Sie, dass sie mit Ihren Canvas-Sendeeinstellungen übereinstimmen. (Wenn Nutzer:innen „subscribed“ sind, aber die Einstellungen auf „Opted-in“ gesetzt sind, werden Nutzer:innen für den Kanal nicht aktiviert.)
- Wenn globales Frequency-Capping für Ihren Canvas aktiviert ist, prüfen Sie, ob Ihre Regeln einschränken, wie oft jede:r Nutzer:in eine Nachricht von einem bestimmten Kanal erhalten kann.
- Wenn Ruhezeiten aktiviert sind, kann die Sendezeit Ihrer Nachricht beeinflusst werden, was bedeutet, dass Ihre Nachricht zum nächsten verfügbaren Zeitpunkt (wenn die Ruhezeiten enden) gesendet oder ganz storniert werden kann.
- Prüfen Sie die Nutzerverfügbarkeit für zusätzliche Filter in Ihrem Canvas-Schritt.

### Bestätigen, dass das erforderliche angepasste Event oder der Kauf durchgeführt wurde {#confirm-that-they-performed-the-prerequisite-custom-event-or-purchase}

- Prüfen Sie, ob eine Race-Condition vorliegt, die sich auf die Nachrichten auswirkt, die Nutzer:innen erhalten, wenn sie mehrere Aktionen gleichzeitig auslösen.
- Stellen Sie sicher, dass keine spezifischen Filter im Schritt vorhanden sind, die Nutzer:innen am Empfang der Nachricht hindern könnten.
- Suchen Sie nach Konflikten zwischen verschiedenen Schritten innerhalb desselben Canvas. Beispielsweise könnten Nutzer:innen, die die Nachricht nicht erhalten haben, durch einen Filter gestoppt worden sein, der den Abschluss eines anderen Schritts in einem anderen Branch erfordert.
- Bestätigen Sie, dass die Nutzer:innen zusätzliche Validierungsregeln erfüllen.
- Bestätigen Sie, dass der Canvas-Schritt zum Zeitpunkt des Sendens mit dem vorhergehenden Schritt verbunden war.

### Bestätigen, dass Ihr Canvas korrekt gespeichert wird und alle Schritte gültig sind {#confirm-your-canvas-saves-correctly-and-all-steps-are-valid}

Wenn Ihr Canvas nicht lädt und nicht fortschreitet, kann dies daran liegen, dass eine frühere Version des Canvas nicht ordnungsgemäß gespeichert wurde und ungültige Schritte enthält. Sie können den Canvas über das Dashboard duplizieren. Wenn das Problem weiterhin besteht, öffnen Sie ein [Support-Ticket]({{site.baseurl}}/user_guide/administer/personal/braze_support).

## Fehlerbehebung {#troubleshooting}

{% details Warum erhalten meine Nutzer:innen meine Canvas-Nachrichten nicht? %}
**Verfügbarkeit der Nutzer:innen prüfen**
- Stellen Sie sicher, dass sie Ihre Segmentierungskriterien erfüllen.
- Bestätigen Sie, dass ihr Push-Abo-Status auf „subscribed“ oder „opted-in“ gesetzt ist **und** ihr Status **Push Enabled** auf „true“ steht. Wenn Sie diese als Canvas-Eintrittsregeln hinzugefügt haben, ist es möglich, dass sich die Nutzer:innen zwischen dem Eintritt in Ihr Canvas und dem Empfang des Nachrichtenschritts abgemeldet haben.
- Bestätigen Sie, dass sie Ihren Canvas-Sendeeinstellungen entsprechen. (Wenn Nutzer:innen „subscribed“ sind, die Einstellungen aber auf „Opted-in“ stehen, sind die Nutzer:innen für den Kanal nicht aktiviert.)
- Wenn globales Frequency-Capping für Ihr Canvas aktiviert ist, prüfen Sie, ob Ihre Regeln einschränken, wie oft jede:r Nutzer:in eine Nachricht über einen bestimmten Kanal erhalten kann.
- Wenn Ruhezeiten aktiviert sind, kann die Sendezeit Ihrer Nachricht beeinflusst werden. Das bedeutet, dass Ihre Nachricht zum nächsten verfügbaren Zeitpunkt (wenn die Ruhezeiten enden) gesendet oder ganz abgebrochen werden kann.

**Verfügbarkeit der Nutzer:innen für zusätzliche Filter in Ihrem Canvas-Schritt prüfen**
- Bestätigen Sie, dass sie das erforderliche angepasste Event oder den Kauf durchgeführt haben.
- Prüfen Sie, ob es eine [Race-Condition]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions) gibt, die die Nachrichten beeinflusst, die Nutzer:innen erhalten, wenn sie mehrere Aktionen gleichzeitig auslösen.
- Stellen Sie sicher, dass es keine bestimmten Filter im Schritt gibt, die Nutzer:innen am Empfang der Nachricht gehindert haben könnten.
- Suchen Sie nach Konflikten zwischen verschiedenen Schritten innerhalb desselben Canvas. Beispielsweise könnten Nutzer:innen, die die Nachricht nicht erhalten haben, durch einen Filter gestoppt worden sein, der den Abschluss eines anderen Schritts in einem anderen Branch erfordert.
- Bestätigen Sie, dass die Nutzer:innen zusätzliche Validierungsregeln erfüllen.
- Bestätigen Sie, dass der Canvas-Schritt zum Zeitpunkt des Versands mit dem vorhergehenden Schritt verbunden war.
{% enddetails %}