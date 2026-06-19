---
nav_title: Aktionspfade
article_title: Aktionspfade
alias: /action_paths/
page_order: 1
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie Aktionspfade verwenden – eine Komponente, mit der Sie Nutzer:innen basierend auf ihren Aktionen sortieren können."
tool: Canvas
---

# Aktionspfade {#action-paths}

> Aktionspfade in Canvas ermöglichen es Ihnen, Ihre Nutzer:innen basierend auf ihren Aktionen zu sortieren.

![Ein Aktionspfade-Schritt in einer Canvas-Nutzer-Journey.]({% image_buster /assets/img/canvas_actionpath.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Mit Aktionspfaden können Sie:

* Nutzerpfade basierend auf einer bestimmten Aktion anpassen, einschließlich Engagement-Events und angepasster Events
* Nutzer:innen für einen bestimmten Zeitraum halten, um ihren nächsten Pfad basierend auf ihren Aktionen während dieses Auswertungszeitraums zu priorisieren

## Einen Aktions-Pfad erstellen {#creating-an-action-path}

Um einen Aktions-Pfad zu erstellen, fügen Sie eine Komponente zu Ihrem Canvas hinzu. Ziehen Sie die Komponente per Drag-and-Drop aus der Seitenleiste, oder wählen Sie den <i class="fas fa-plus-circle"></i> Plus-Button am unteren Rand eines Schritts und wählen Sie **Action Paths**.

### Aktionseinstellungen {#action-settings}

Legen Sie in den **Action Settings** das **Evaluation Window** fest, um zu bestimmen, wie lange Nutzer:innen im Schritt gehalten werden. Standardmäßig werden Nutzer:innen innerhalb eines Tages ausgewertet, aber Sie können dieses Fenster je nach Ihrem Canvas in Sekunden, Minuten, Stunden, Tagen und Wochen anpassen. Das maximale Auswertungsfenster für einen Aktions-Pfad beträgt 31 Tage.

In den **Action Settings** können Sie auch die Rangfolge für Ihre Komponenten aktivieren, indem Sie den Toggle **Advance users based on ranked order** umschalten.

![Die Aktionseinstellungen mit einem Auswertungsfenster von 1 Tag.]({% image_buster /assets/img/actionpath_settings.png %})

Standardmäßig ist **Ranking** deaktiviert. Wenn Nutzer:innen den Aktions-Pfad betreten und das Trigger-Event einer beliebigen Aktionsgruppe ausführen, werden sie sofort durch die entsprechende Aktionsgruppe weitergeleitet – basierend auf der **ersten qualifizierenden Aktion**, die sie nach dem Betreten des Schritts ausführen. Wenn Nutzer:innen eine zweite Aktion ausführen, die einer anderen Aktionsgruppe entspricht, wechseln sie nicht den Pfad – die erste Aktion bestimmt ihre Route. Wenn Nutzer:innen kein Trigger-Event ausführen, werden sie am Ende des Auswertungszeitraums durch die Standardgruppe **Alle anderen** weitergeleitet.

Wenn **Advance users based on ranked order** aktiviert ist, bedeutet dies, dass **Ranking** aktiv ist. Alle Nutzer:innen werden dann bis zum Ende des Auswertungsfensters gehalten. Am Ende des Auswertungszeitraums werden Nutzer:innen durch die Aktionsgruppe mit der höchsten Priorität weitergeleitet, für die sie am Ende des Auswertungsfensters qualifiziert sind. Nutzer:innen, die während des Auswertungsfensters keine der Aktionen ausführen, werden durch die Standardgruppe **Alle anderen** weitergeleitet.

{% alert tip %}
Um Nutzer:innen basierend auf ihren aktuellen Attributen oder Segment-Zugehörigkeit statt auf ausgeführten Aktionen weiterzuleiten, verwenden Sie stattdessen [Zielgruppenpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths/).
{% endalert %}

Beachten Sie, dass Sie einen Aktions-Pfad triggern können, wenn sich ein verschachteltes angepasstes Attribut-Objekt ändert, jedoch nicht für Arrays von verschachtelten angepassten Attributen oder Änderungen an Objekt-Array-Datentypen.

#### In-App-Nachrichten {#in-app-messages}

Beachten Sie: Wenn der Trigger der Aktionsgruppe das Starten einer Sitzung ist und der nächste Schritt eine In-App-Nachricht ist, müssen Nutzer:innen zwei Sitzungsstarts durchführen, um die In-App-Nachricht zu erhalten. Der erste Sitzungsstart ordnet die Nutzer:innen der Aktionsgruppe innerhalb des Aktions-Pfads zu, und der zweite Sitzungsstart triggert die In-App-Nachricht.

#### Beispiel für den Rangfolge-Status {#ranking-status-example}

Nehmen wir an, Sie haben einen Aktions-Pfad mit einem Auswertungszeitraum von einem Tag und zwei Aktionsgruppen: Gruppe 1 und Gruppe 2. Gruppe 1 hat das Trigger-Event „Sitzung starten“ und Gruppe 2 hat „Kauf tätigen“. Wenn **Ranking** aktiviert ist, werden alle Nutzer:innen im Aktions-Pfad für einen Tag „gehalten“. Am Ende des Tages werden Nutzer:innen, die eine Sitzung gestartet und einen Kauf getätigt haben, zum Pfad mit dem höchsten Rang weitergeleitet. In diesem Fall würden die Nutzer:innen zu Gruppe 1 weitergeleitet.

Wenn im vorherigen Beispiel **Ranking** deaktiviert ist und Nutzer:innen eines der Trigger-Events ausführen („Sitzung starten“ oder „Kauf tätigen“), werden sie basierend auf der Trigger-Aktion in der entsprechenden Aktionsgruppe weitergeleitet.

Beachten Sie, dass sich Canvas-Eingangs-Eigenschaften von Event-Eigenschaften unterscheiden. Canvas-Eingangs-Eigenschaften sind Eigenschaften des Events, das den Canvas getriggert hat. Diese Eigenschaften können nur im ersten vollständigen Schritt eines Canvas verwendet werden, wenn der ursprüngliche Canvas-Workflow genutzt wird. Bei Verwendung von Canvas ermöglichen persistente Eingangs-Eigenschaften die Wiederverwendung der Eingangs-Eigenschaften im gesamten Canvas. Im Gegensatz dazu stammen Event-Eigenschaften von einem Event oder einer Aktion, die stattfindet, während Nutzer:innen ihren Workflow durchlaufen.

### Aktionsgruppen {#action-groups}

Fügen Sie einen oder mehrere Trigger hinzu, um Ihre Aktionsgruppen zu definieren. Hier können Sie eine Reihe von Triggern auswählen, z. B. ob Nutzer:innen:

- Einen Kauf tätigen
- Eine Sitzung starten
- Ein [angepasstes Event]({{site.baseurl}}/user_guide/data/activation/events/custom_events/) ausführen
- Ein Konversions-Event ausführen
- Eine E-Mail-Adresse hinzufügen
- Einen angepassten Attributwert ändern
  - Dies umfasst auch das erstmalige Hinzufügen eines neuen Attributs mit einem Wert zu einem Nutzerprofil (wenn das Attribut zuvor nicht vorhanden war).
  - Attribut-Trigger sind für Array-Attribute nicht verfügbar.
- Ihren Abo-Status oder Abo-Gruppenstatus aktualisieren
- Mit einer Campaign oder Content-Card interagieren
- Einen Standort betreten
- Einen Geofence triggern
- Eine eingehende SMS- oder WhatsApp-Nachricht senden

#### Trigger „E-Mail-Adresse hinzufügen“ {#add-an-email-address-trigger}

Der Aktionsgruppen-Trigger **Add an Email Address** wird ausgelöst, wenn eine E-Mail-Adresse während des **Evaluation Window** des Aktions-Pfads zu einem Nutzerprofil hinzugefügt oder aktualisiert wird. Dieses Verhalten entspricht anderen Profilaktualisierungs-Triggern: Nutzer:innen werden durch die Aktionsgruppe weitergeleitet, wenn die Profiländerung unter Ihrer Konfiguration qualifiziert ist, einschließlich aller Filter auf dem Trigger.

![Eine Aktionsgruppe namens „Gruppe 1“ für Nutzer:innen, die einen beliebigen Kauf tätigen.]({% image_buster /assets/img/actionpath_group.png %})

In jeder Aktionsgruppeneinstellung haben Sie auch die Möglichkeit, das Kontrollkästchen **I want this group to exit the Canvas** zu aktivieren. Das bedeutet, dass die Nutzer:innen in dieser Gruppe den Canvas am Ende des Auswertungszeitraums verlassen.

### Canvases mit erneuter Berechtigung {#canvases-with-re-eligibility}

Wenn Nutzer:innen einen Aktions-Pfad mehrfach betreten und gleichzeitig mehrere Einträge im Aktions-Pfad haben, variiert das erwartete Verhalten je nach **Ranking**-Status.

| Ranking-Status | Verhalten des Aktions-Pfads |
|---|--------------|
| **Deaktiviert** | Nutzer:innen können einen Aktions-Pfad mehr als einmal betreten. Diese Einträge werden im Aktions-Pfad gehalten, bis eine Trigger-Aktion oder ein Event erfasst wird. Wenn das Trigger-Event die Eigenschaftsfilter eines Eintrags nicht erfüllt (z. B. wenn eine [Kontextvariable]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_variables/) nicht mit den Eigenschaftsfiltern des Triggers übereinstimmt), verbleibt der Eintrag im Aktions-Pfad. <br><br>Wenn das Trigger-Event mehr als einen Eintrag erfüllt, dedupliziert Braze nur diese Einträge und leitet den frühesten übereinstimmenden Eintrag sofort durch die entsprechende Aktionsgruppe weiter. |
| **Aktiviert** | Alle Einträge werden am Ende des jeweiligen Auswertungsfensters weitergeleitet. Es findet keine Deduplizierung statt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canvases mit erneuter Berechtigung" }

Beachten Sie, dass die Rangfolgen nach dem Start [nicht mehr bearbeitet werden können]({{site.baseurl}}/post-launch_edits/).