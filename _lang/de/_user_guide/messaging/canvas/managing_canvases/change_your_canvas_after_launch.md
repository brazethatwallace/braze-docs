---
nav_title: Canvase nach dem Start bearbeiten
article_title: Canvase nach dem Start bearbeiten
page_order: 0
description: "Dieser Referenzartikel behandelt die verschiedenen Aspekte eines Canvas, die nach dem ersten Start geändert werden können."
alias: "/post-launch_edits/"
page_type: reference
tool:
  - Canvas

---

# Canvase nach dem Start bearbeiten {#edit-canvases-after-launch}

> Dieser Referenzartikel behandelt, was in einem Canvas nach dem ersten Start geändert werden kann.

Sie können Ihre Canvase nach dem Start bearbeiten, indem Sie:

* Neue Canvas-Schritte in die User-Journey einfügen
* Neue Varianten und Verbindungen hinzufügen
* Die Variantenverteilung anpassen
* Alle Canvas-Schritte stoppen oder fortsetzen

{% alert note %}
Die Verteilung der Kontrollvariante kann nach dem Start nur verringert werden.
{% endalert %}

Sie können Folgendes in Ihrer User-Journey löschen:

- [Canvas-Schritte]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about)
- Canvas-Varianten
- Verbindungen zwischen Canvas-Schritten

Wenn Sie Schritte in Ihrer Canvas-User-Journey bearbeiten oder hinzufügen möchten, gelten die folgenden Details:

- Nutzer:innen, die den Canvas noch nicht betreten haben, sind für alle neu erstellten Schritte berechtigt.
- Wenn Ihre Canvas-Eingangseinstellungen es Nutzer:innen erlauben, Schritte erneut zu betreten, sind Nutzer:innen, die bereits neu erstellte Schritte passiert haben, berechtigt, erneut einzutreten.
- Nutzer:innen, die sich derzeit in einem gestarteten Canvas befinden, aber die Punkte der User-Journey, an denen neue Schritte hinzugefügt wurden, noch nicht erreicht haben, sind berechtigt, diese neu hinzugefügten Schritte zu erhalten.

Wenn Sie einen [Verzögerungs]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step)- oder [Aktionspfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)-Schritt löschen, können Sie die Nutzer:innen, die derzeit im Schritt warten, optional in einen anderen Canvas-Schritt umleiten. Bei Verzögerungen bleiben die Nutzer:innen bis zum Ende der Verzögerungsperiode im Schritt. Bei Aktionspfaden bleiben die Nutzer:innen bis zum Ende des Auswertungsfensters im Schritt.

Beachten Sie, dass Braze beim ersten Start eines Canvas die Nutzer:innen für den Nachrichten-Schritt in die Warteschlange einreiht, an dem sie sich befinden, nicht für alle nachfolgenden Nachrichten im Canvas. Wenn Sie nach dem Start eine Änderung am Canvas vornehmen, befinden sich einige Nutzer:innen möglicherweise bereits in der Warteschlange und übernehmen die Änderungen nicht. Wenn Sie den Canvas stoppen, duplizieren, dann ändern und diese neue Version starten, bewertet der Canvas alle Nutzer:innen erneut – nicht nur diejenigen, die noch nicht in die Warteschlange eingereiht wurden.

Im Abschnitt [Best Practices](#best-practices) finden Sie spezifische Anwendungsfälle für Bearbeitungen. Generell ist es empfehlenswert, das Bearbeiten von aktiven Canvase zu vermeiden, da es zu unerwartetem Verhalten kommen kann.

{% details Für Details zum originalen Canvas-Editor aufklappen %}

Beachten Sie die folgenden zulässigen Bearbeitungen nach dem Start, abhängig davon, mit welchem Workflow Ihr Canvas erstellt wurde. Wenn Ihr Canvas den originalen Canvas-Workflow verwendet, müssen Sie ihn zuerst zu Canvas Flow Klon or klonen, um Bearbeitungen nach dem Start durchzuführen.

Sie können bestehende Verbindungen nicht bearbeiten oder löschen, und Sie können keinen Schritt zwischen bestehenden verbundenen Schritten einfügen. Wenn Sie Schritte in Ihrer Canvas-User-Journey bearbeiten oder hinzufügen möchten, gelten die folgenden Details:

- Nutzer:innen, die den Canvas noch nicht betreten haben, sind für alle neu erstellten Schritte berechtigt.
- Wenn Ihre Canvas-Eingangseinstellungen es Nutzer:innen erlauben, Schritte erneut zu betreten, sind Nutzer:innen, die bereits neu erstellte Schritte passiert haben, berechtigt, erneut einzutreten.
- Nutzer:innen, die sich derzeit in einem gestarteten Canvas befinden, aber die neu hinzugefügten Schritte in der User-Journey noch nicht erreicht haben, sind berechtigt, diese neu hinzugefügten Schritte zu erhalten.
- Wenn ein Verzögerungsschritt der letzte Schritt im Canvas ist, werden Nutzer:innen, die diesen Schritt erreichen, automatisch aus dem Canvas herausgeführt und erhalten keine neu erstellten Schritte.

{% alert important %}
Wenn Sie die Einstellungen für **Verzögerung** oder **Fenster** eines Canvas-Schritts Update or aktualisieren or aktualisieren, halten sich Nutzer:innen, die sich zum Zeitpunkt des Updates in diesem Schritt befinden, an die Verzögerungszeit, die ihnen beim ursprünglichen Eintritt zugewiesen wurde. Nur neue Nutzer:innen, die den Canvas betreten, und diejenigen, die noch nicht für diesen Schritt in die Warteschlange eingereiht wurden, erhalten die Nachricht zur aktualisierten Zeit.
{% endalert %}

Das Stoppen eines Canvas führt nicht dazu, dass Nutzer:innen, die auf den Empfang einer Nachricht warten, den Canvas verlassen. Wenn Sie den Canvas wieder aktivieren und Nutzer:innen noch auf die Nachricht warten, erhalten sie die Nachricht (es sei denn, der Zeitpunkt, zu dem die Nachricht hätte gesendet werden sollen, ist bereits verstrichen – dann erhalten sie sie nicht).

{% enddetails %}

## Canvas-Details {#canvas-details}

Sie können die folgenden Einstellungen und Details nach dem Start eines Canvas bearbeiten:

- Canvas-Name und -Beschreibung
- Teams
- Tags
  - Das Hinzufügen eines Tags nach dem Start ermöglicht es Ihnen, Nutzer:innen in Segmenten mit Filtern wie `Received Message from Campaign or Canvas with Tag` erneut anzusprechen.
- Entry-Typ, Zeitplan und Steuerungen
- Abo-Status
- Rate-Limiting
- Frequency-Capping
- Ruhezeiten
- Zielgruppe

Nach dem Start eines Canvas:

- Konversions-Events können nicht bearbeitet werden.
- Die folgenden Schritte können weder hinzugefügt oder entfernt noch umgeordnet werden, um die Rangfolge anzupassen: [Zielgruppenpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths), [Aktionspfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) und [Experimentpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step).
  - **Workaround 1:** Erstellen Sie einen neuen Zielgruppenpfad, Aktionspfad oder Experimentpfad und konfigurieren Sie die Pfade zu diesem neuen Schritt um.
  - **Workaround 2:** Duplizieren Sie das Canvas, um Ihre Änderungen vorzunehmen.

### Einzelne Schritte {#individual-steps}

Für einzelne Canvas-Schritte können Sie nach dem Start die folgenden Details bearbeiten:

* Name
* Nachrichteninhalt
* Trigger or triggern
* Zielgruppe
* Ausnahme-Events
* Verzögerungen (nur für Verzögerungsschritte)

Der Zeitplantyp und die Kontrollprozentsätze des Schritts sind jedoch nach dem Start nicht bearbeitbar. Für Aktionspfade und Zielgruppenpfade sind die Rangfolgen und Auswertungszeiträume nach dem Start nicht bearbeitbar.

#### Schritt „An Ziel senden“ {#send-to-destination-step}

Beim Bearbeiten des Schritts [An Ziel senden]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination) in einem aktiven Canvas gelten die folgenden Verhaltensweisen:

- **Ändern des Ziel-Canvas:** Das Bearbeiten des Schritts „An Ziel senden“, sodass er auf ein anderes Ziel-Canvas verweist, folgt den allgemeinen Regeln für die Bearbeitung nach dem Start. Änderungen betreffen nur Nutzer:innen, die den Schritt „An Ziel senden“ noch nicht erreicht haben.
  - Nutzer:innen, die den Schritt bereits durchlaufen haben, verbleiben im ursprünglichen Ziel-Canvas — sie werden nicht umgeleitet.
  - Nutzer:innen, die sich derzeit in vorherigen Schritten in der Warteschlange befinden (z. B. in einem Verzögerungsschritt vor dem Schritt „An Ziel senden“ warten), werden anhand der Eintritts- und Zielgruppenkriterien des neuen Ziel-Canvas geprüft, wenn sie den Schritt erreichen. Berechtigte Nutzer:innen werden an das neue Ziel-Canvas gesendet.
- **Gestopptes Ziel-Canvas:** Wenn das Ziel-Canvas gestoppt wird, während Ihr Quell-Canvas noch aktiv ist, werden Nutzer:innen, die den Schritt „An Ziel senden“ erreichen, nicht an das Ziel-Canvas gesendet. Dies führt zu einem Nutzer:innenabfall bei der Übergabe, nicht zu einer Pause, während das Ziel gestoppt ist.
  - Nutzer:innen, die nicht in das gestoppte Ziel-Canvas eintreten können, setzen ihren Weg im Quell-Canvas fort, wenn weitere Schritte nach dem Schritt „An Ziel senden“ folgen. Weitere Informationen zum Fortschrittsverhalten finden Sie unter [An Ziel senden]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination#how-does-advancement-behavior-work-for-send-to-destination-steps).
  - Sie können ein Quell-Canvas mit einem Schritt „An Ziel senden“, der auf ein gestopptes Ziel verweist, nicht starten. Dieses Verhalten gilt, wenn ein Ziel-Canvas gestoppt wird, nachdem das Quell-Canvas bereits aktiv ist.

### Canvas-Varianten-Prozentsätze {#canvas-variant-percentages}

Nach dem Start eines Canvas können Sie die Kontrollvarianten-Prozentsätze nur verringern. Wenn ein Varianten-Prozentsatz in Canvas geändert wird, kann es sein, dass Ihre Nutzer:innen auf andere Varianten umverteilt werden.

Anfangs werden diesen Nutzer:innen zufällig eine bestimmte Variante zugewiesen, bevor sie zum ersten Mal eine Campaign erhalten. Von da an erhalten sie jedes weitere Mal, wenn die Campaign empfangen wird (oder die Nutzer:innen erneut in eine Canvas-Variante eintreten), dieselbe Variante, es sei denn, die Varianten-Prozentsätze werden geändert.

Wenn sich die Varianten-Prozentsätze ändern, können Nutzer:innen auf andere Varianten umverteilt werden. Nutzer:innen verbleiben in diesen Varianten, bis die Prozentsätze erneut geändert werden. Beachten Sie, dass bei Canvase, die Verzweigungen mit `NOT`-Filtern und zufälligen Bucket-Nummern verwenden, Nutzer:innen möglicherweise nicht bei jedem Durchlauf ihrer User Journey denselben Branch erhalten, wenn sie erneut in das Canvas eintreten.

#### Kontrollgruppen {#control-groups}

Kontrollgruppen bleiben konsistent, wenn der Varianten-Prozentsatz unverändert bleibt. Wenn der Prozentsatz einer Kontrollgruppe verringert oder erhöht wird, könnten Nutzer:innen, die zuvor Nachrichten erhalten haben, bei einem späteren Versand nicht in die Kontrollgruppe gelangen, und keine Nutzer:innen in der Kontrollgruppe würden jemals eine Nachricht erhalten.

### Lokale Sendezeit {#local-send-time}

Canvase, die zu einer lokalen Sendezeit gestartet werden sollen, können bis zu 24 Stunden vor der geplanten Sendezeit bearbeitet werden. Dieses Zeitfenster wird als „sichere Zone“ bezeichnet.

{% alert tip %}
Wenn Sie größere Änderungen vornehmen möchten, die zur Erstellung einer komplett neuen Canvas-Kopie führen, denken Sie daran, Nutzer:innen auszuschließen, die das erste Canvas erhalten haben, und die Canvas-Zeitplanzeiten anzupassen, um den Versand nach Zeitzonen zu berücksichtigen.
{% endalert %}

Wenn ein Eintrittszeitplan so eingestellt ist, dass Nutzer:innen sofort beim Start eintreten, wird das Canvas zum nächstliegenden Zeitpunkt in 5-Minuten-Schritten gestartet. Wenn Sie beispielsweise ein Canvas so Update or aktualisieren or aktualisieren, dass Nutzer:innen sofort um 8:31 Uhr PST eintreten, wird die Startzeit auf 8:30 Uhr PST und in der Zeitzone des Unternehmens festgelegt.

### Varianten löschen {#deleting-variants}

Wenn Varianten aus einem Canvas gelöscht werden, geschieht Folgendes:

- Schritte innerhalb der Variante (einschließlich solcher, die mit anderen Varianten geteilt werden) werden gelöscht.
- Die Schrittanalysen und die übergeordneten Analytics für das Canvas, wie _Gesamte Eintritte_, _Gesamte Exits_ und _Konversionsrate_, werden gelöscht.
- Nutzer:innen in gelöschten Varianten werden aus den Schritten entfernt, und alle folgenden Nachrichten werden nicht gesendet.

### Canvas-Entry-Eigenschaften {#canvas-entry-properties}

Canvas-Entry-Eigenschaften werden nicht in Schritte beim Versand als Template eingefügt. Das bedeutet, dass Änderungen an Canvas-Entry-Eigenschaften nach dem Start eines Canvas nur für neue Nutzer:innen gelten, die in das Canvas eintreten. Wenn Ihr Canvas Nutzer:innen erlaubt, erneut in das Canvas einzutreten, werden alle Nutzer:innen, die erneut eintreten, anhand der aktualisierten Canvas-Entry-Eigenschaften bestimmt.

## Best Practices {#best-practices}

Beachten Sie diese Best Practices, wenn Sie Ihren Canvas nach dem Start bearbeiten oder ergänzen.

{% alert important %}
Vermeiden Sie generell Änderungen, während der Canvas aktiv ist und Nutzer:innen in die Warteschlange eingereiht werden.
{% endalert %}

### Nicht verbundene Schritte {#disconnected-steps}

Sie können Ihren Canvas mit nicht verbundenen Schritten starten und diese Canvase auch nach dem Start speichern. Bevor Sie einen Schritt von Ihrem Workflow trennen, empfehlen wir, in der Analytics-Ansicht der Schritte die wartenden Nutzer:innen zu prüfen.

Nehmen wir an, ein:e Nutzer:in befindet sich in einem nicht verbundenen Schritt Ihres Canvas-Workflows. Diese:r Nutzer:in rückt zum nächsten Schritt vor, sofern einer vorhanden ist. Die Einstellungen des Schritts bestimmen, wie der Fortschritt erfolgen soll.

Indem Sie nicht verbundene Schritte erstellen oder bearbeiten, können Sie Änderungen an diesen unabhängigen Schritten vornehmen, ohne sie direkt mit dem Representational State Transfer Ihres Canvas verbinden zu müssen. Das hilft beim Testen Ihrer Schritte, bevor Sie Ihren Canvas erneut starten.

### Experimentpfad-Schritt {#experiment-path-step}

Wenn Ihr Canvas ein aktives oder laufendes Winning-Path-Experiment enthält und Sie den aktiven Canvas Update or aktualisieren or aktualisieren, wird das Experiment beendet. Dies gilt auch dann, wenn Sie den Experimentpfad-Schritt nicht Update or aktualisieren or aktualisieren. Um das Experiment neu zu starten, trennen Sie den bestehenden Experimentpfad und starten Sie einen neuen, oder duplizieren Sie den Canvas und starten Sie das Duplikat. Andernfalls durchlaufen Nutzer:innen den Experimentpfad ohne Optimierung.

Bestehende Experimentpfad-Schritte, die personalisierte Pfade verwenden, laufen weiter. Das Update or aktualisieren or aktualisieren eines aktiven Canvas beendet auch ein laufendes Experiment mit personalisierten Pfaden.

### Zeitverzögerungen {#time-delays}

Das Bearbeiten von Canvase mit Zeitverzögerungen kann etwas knifflig sein. Beachten Sie daher die folgenden Details, wenn Sie Änderungen an Ihren Canvase vornehmen:

- Wenn Sie die Verzögerung in einem Delay-Schritt Update or aktualisieren or aktualisieren, erhalten nur neue Nutzer:innen, die den Canvas betreten, und Nutzer:innen, die noch nicht für diesen Schritt in die Warteschlange eingereiht wurden, die Nachricht mit der aktualisierten Zeitverzögerung.
- Wenn Sie einen Schritt mit einer Zeitverzögerung löschen (z. B. Delay oder Aktionspfade) und sich entscheiden, diese Nutzer:innen in einen anderen Canvas-Schritt umzuleiten, werden die Nutzer:innen erst umgeleitet, nachdem die Zeitverzögerung des Schritts abgelaufen ist. Nehmen wir beispielsweise an, Sie löschen einen Delay-Schritt mit einer eintägigen Verzögerung und leiten diese Nutzer:innen in einen Nachrichten-Schritt um. In diesem Fall werden die Nutzer:innen erst nach Ablauf der eintägigen Verzögerung umgeleitet.
- Wenn Ihr Canvas einen oder mehrere Experimentpfad-Schritte enthält, könnte das Löschen von Schritten die Ergebnisse dieses Schritts ungültig machen.

### Canvase anhalten {#stopping-canvases}

Das Anhalten eines Canvas bewirkt nicht, dass Nutzer:innen, die in einem Schritt warten, den Canvas verlassen. Wenn Sie den Canvas erneut aktivieren und die Nutzer:innen noch warten, schließen sie den Schritt ab und gehen zum nächsten Schritt über. Wenn jedoch der Zeitpunkt, zu dem die Nutzer:innen zum nächsten Schritt hätten vorrücken sollen, bereits verstrichen ist, verlassen sie stattdessen den Canvas.

Nehmen wir beispielsweise an, Sie haben einen Canvas mit dem Canvas-Flow-Workflow erstellt, der um 14:00 Uhr starten soll, mit einer Variante und zwei Schritten: einem Delay-Schritt mit einer einstündigen Verzögerung, der in einen Nachrichten-Schritt übergeht.

Ein:e Nutzer:in betritt diesen Canvas um 14:01 Uhr und tritt gleichzeitig in den Delay-Schritt ein. Das bedeutet, dass der/die Nutzer:in planmäßig um 15:01 Uhr zum nächsten Schritt der User Journey (dem Nachrichten-Schritt) vorrückt. Wenn Sie den Canvas um 14:30 Uhr anhalten und um 15:30 Uhr erneut aktivieren, verlässt der/die Nutzer:in den Canvas, da es bereits nach 15:01 Uhr ist. Wenn Sie den Canvas jedoch um 14:40 Uhr erneut aktivieren, rückt der/die Nutzer:in wie erwartet um 15:01 Uhr zum Nachrichten-Schritt vor.

## Wissenswertes {#things-to-know}

Die folgenden häufigen Probleme können auftreten, wenn Sie nach dem Start eines Canvas Komponenten bearbeiten oder neue Komponenten zu einer anderen Komponente in einem Canvas hinzufügen.

{% alert important %}
Die folgenden Probleme sind vermeidbar. Wenn Sie nach dem Start Änderungen an einem Canvas vornehmen müssen, empfehlen wir, zunächst sicherzustellen, dass alle Nutzer:innen, die bereits in den Canvas eingetreten sind, ihre User Journey abgeschlossen haben. Darüber hinaus empfehlen wir, keine Schritte zu löschen, die bereits von mindestens einer/einem Nutzer:in durchlaufen wurden.
{% endalert %}

- Fehlende Berichtsdaten (wenn Nachrichtenvarianten gelöscht und erneut hinzugefügt werden)
- Nutzer:innen folgen nicht dem erwarteten Pfad
- Nachrichten werden zu unerwarteten Zeiten gesendet
- Die Änderungen überschreiben keine Currents-Daten, sodass Diskrepanzen zwischen Canvas-Schritten auftreten können (z. B. `canvas_step_ids`, die aufgrund von Löschungen nicht mehr im Canvas existieren)
- Nutzer:innen können dieselbe Nachricht zweimal erhalten
- Nutzer:innen erhalten aufgrund des bestehenden Rate-Limits keine Nachrichten
  - Wenn Sie das Rate-Limit eines aktiven Canvas Update or aktualisieren or aktualisieren, gilt das neue Rate-Limit nur für Nutzer:innen, die nach der Änderung des Rate-Limits durch den Nachrichten-Schritt fließen. Nutzer:innen, die sich bereits in der Warteschlange für einen Nachrichten-Schritt befinden, behalten das ursprüngliche Rate-Limit bei, das zum Zeitpunkt des Einreihens in die Warteschlange galt. Um ein neues Rate-Limit auf alle Nutzer:innen anzuwenden, stoppen Sie den Canvas, duplizieren Sie ihn mit dem aktualisierten Rate-Limit und starten Sie den neuen Canvas. Verwenden Sie einen Filter, um zu verhindern, dass Nutzer:innen, die Nachrichten aus dem ursprünglichen Canvas erhalten haben, in den duplizierten Canvas eintreten.
- Wenn ein Canvas [automatisch gestoppt]({{site.baseurl}}/user_guide/messaging/governance/statuses#available-statuses) wird, werden die nach dem Start erstellten Entwürfe des Canvas ebenfalls gelöscht.