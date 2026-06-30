---
nav_title: Canvases nach dem Start bearbeiten
article_title: Canvases nach dem Start bearbeiten
page_order: 0
description: "Dieser Referenzartikel behandelt die verschiedenen Aspekte eines Canvas, die nach dem ersten Start geändert werden können."
alias: "/post-launch_edits/"
page_type: reference
tool:
  - Canvas

---

# Canvases nach dem Start bearbeiten {#edit-canvases-after-launch}

> Dieser Referenzartikel behandelt, was in einem Canvas nach dem ersten Start geändert werden kann.

Sie können Ihre Canvases nach dem Start bearbeiten, indem Sie:

* Neue Canvas-Schritte in die User-Journey einfügen
* Neue Varianten und Verbindungen hinzufügen
* Die Variantenverteilung anpassen
* Alle Canvas-Schritte stoppen oder fortsetzen

{% alert note %}
Die Verteilung der Kontrollgruppen-Variante kann nach dem Start nur verringert werden.
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

Im Abschnitt [Best Practices](#best-practices) finden Sie spezifische Anwendungsfälle für Bearbeitungen. Generell ist es empfehlenswert, das Bearbeiten von aktiven Canvases zu vermeiden, da es zu unerwartetem Verhalten kommen kann.

{% details Für Details zum originalen Canvas-Editor aufklappen %}

Beachten Sie die folgenden zulässigen Bearbeitungen nach dem Start, abhängig davon, mit welchem Workflow Ihr Canvas erstellt wurde. Wenn Ihr Canvas den originalen Canvas-Workflow verwendet, müssen Sie ihn zuerst zu Canvas Flow klonen, um Bearbeitungen nach dem Start durchzuführen.

Sie können bestehende Verbindungen nicht bearbeiten oder löschen, und Sie können keinen Schritt zwischen bestehenden verbundenen Schritten einfügen. Wenn Sie Schritte in Ihrer Canvas-User-Journey bearbeiten oder hinzufügen möchten, gelten die folgenden Details:

- Nutzer:innen, die den Canvas noch nicht betreten haben, sind für alle neu erstellten Schritte berechtigt.
- Wenn Ihre Canvas-Eingangseinstellungen es Nutzer:innen erlauben, Schritte erneut zu betreten, sind Nutzer:innen, die bereits neu erstellte Schritte passiert haben, berechtigt, erneut einzutreten.
- Nutzer:innen, die sich derzeit in einem gestarteten Canvas befinden, aber die neu hinzugefügten Schritte in der User-Journey noch nicht erreicht haben, sind berechtigt, diese neu hinzugefügten Schritte zu erhalten.
- Wenn ein Verzögerungsschritt der letzte Schritt im Canvas ist, werden Nutzer:innen, die diesen Schritt erreichen, automatisch aus dem Canvas herausgeführt und erhalten keine neu erstellten Schritte.

{% alert important %}
Wenn Sie die Einstellungen für **Verzögerung** oder **Fenster** eines Canvas-Schritts aktualisieren, halten sich Nutzer:innen, die sich zum Zeitpunkt des Updates in diesem Schritt befinden, an die Verzögerungszeit, die ihnen beim ursprünglichen Eintritt zugewiesen wurde. Nur neue Nutzer:innen, die den Canvas betreten, und diejenigen, die noch nicht für diesen Schritt in die Warteschlange eingereiht wurden, erhalten die Nachricht zur aktualisierten Zeit.
{% endalert %}

Das Stoppen eines Canvas führt nicht dazu, dass Nutzer:innen, die auf den Empfang einer Nachricht warten, den Canvas verlassen. Wenn Sie den Canvas wieder aktivieren und Nutzer:innen noch auf die Nachricht warten, erhalten sie die Nachricht (es sei denn, der Zeitpunkt, zu dem die Nachricht hätte gesendet werden sollen, ist bereits verstrichen – dann erhalten sie sie nicht).

{% enddetails %}

## Canvas-Details {#canvas-details}

Sie können die folgenden Einstellungen und Details nach dem Start eines Canvas bearbeiten:

* Canvas-Name und -Beschreibung
* Teams und Tags
* Eingangstyp, Zeitplan und Steuerungen
* Abo-Status
* Rate-Limits
* Frequency-Capping
* Ruhezeiten
* Zielgruppe

Nachdem ein Canvas gestartet wurde:

- Konversions-Events können nicht bearbeitet werden.
- Die folgenden Schritte können nicht hinzugefügt oder entfernt werden und können nicht umgeordnet werden, um die Rangfolge anzupassen: [Zielgruppenpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths), [Aktionspfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) und [Experimentpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step).
  - **Workaround 1:** Erstellen Sie einen neuen Zielgruppenpfad, Aktions-Pfad oder Experiment-Pfad und konfigurieren Sie die Pfade zu diesem neuen Schritt um.
  - **Workaround 2:** Duplizieren Sie den Canvas, um Ihre Änderungen vorzunehmen.

### Einzelne Schritte {#individual-steps}

Für einzelne Canvas-Schritte können Sie die folgenden Details nach dem Start bearbeiten:

* Name
* Nachrichteninhalt
* Trigger
* Zielgruppe
* Ausnahme-Events
* Verzögerungen (nur für Verzögerungsschritte)

Der Zeitplantyp und die Kontrollgruppen-Prozentsätze des Schritts sind nach dem Start jedoch nicht bearbeitbar. Für Aktionspfade- und Zielgruppenpfade-Schritte sind die Rangfolgen und Auswertungsfenster nach dem Start nicht bearbeitbar.

### Canvas-Varianten-Prozentsätze {#canvas-variant-percentages}

Nach dem Start eines Canvas können Sie nur die Kontrollgruppen-Varianten-Prozentsätze verringern. Wenn ein Varianten-Prozentsatz im Canvas geändert wird, können Ihre Nutzer:innen auf andere Varianten umverteilt werden.

Anfänglich wird diesen Nutzer:innen zufällig eine bestimmte Variante zugewiesen, bevor sie zum ersten Mal eine Campaign erhalten. Von da an erhalten sie bei jedem weiteren Empfang der Campaign (oder beim erneuten Eintritt in eine Canvas-Variante) dieselbe Variante, es sei denn, die Varianten-Prozentsätze werden geändert.

Wenn sich die Varianten-Prozentsätze ändern, können Nutzer:innen auf andere Varianten umverteilt werden. Nutzer:innen bleiben in diesen Varianten, bis die Prozentsätze erneut geändert werden. Beachten Sie, dass bei Canvases, die Verzweigungen mit `NOT`-Filtern mit zufälligen Bucket-Nummern verwenden, Nutzer:innen möglicherweise nicht bei jedem erneuten Eintritt in den Canvas denselben Branch in ihrer User-Journey erhalten.

#### Kontrollgruppen {#control-groups}

Kontrollgruppen bleiben konsistent, wenn der Varianten-Prozentsatz unverändert bleibt. Wenn der Prozentsatz einer Kontrollgruppe verringert oder erhöht wird, können Nutzer:innen, die zuvor Nachrichten erhalten haben, bei einem späteren Versand nicht in die Kontrollgruppe eintreten, und keine Nutzer:innen in der Kontrollgruppe würden jemals eine Nachricht erhalten.

### Lokale Sendezeit {#local-send-time}

Canvases, die zu einer lokalen Sendezeit geplant sind, können bis zu 24 Stunden vor der geplanten Sendezeit bearbeitet werden. Dieses Fenster wird als „sichere Zone“ bezeichnet.

{% alert tip %}
Wenn Sie größere Änderungen planen, die zur Erstellung einer komplett neuen Canvas-Kopie führen, denken Sie daran, Nutzer:innen auszuschließen, die den ersten Canvas erhalten haben, und die Canvas-Zeitplanzeiten anzupassen, um den Zeitzonenversand zu berücksichtigen.
{% endalert %}

Wenn ein Entry-Zeitplan so eingestellt ist, dass Nutzer:innen sofort beim Start eintreten, startet der Canvas zum nächstgelegenen Zeitpunkt in 5-Minuten-Schritten. Wenn Sie beispielsweise einen Canvas aktualisieren, damit Nutzer:innen sofort um 8:31 Uhr PST eintreten, wird die Startzeit auf 8:30 Uhr PST in der Zeitzone des Unternehmens festgelegt.

### Varianten löschen {#deleting-variants}

Wenn Varianten aus einem Canvas gelöscht werden, geschieht Folgendes:

- Schritte innerhalb der Variante (einschließlich solcher, die mit anderen Varianten geteilt werden) werden gelöscht.
- Die Schritt-Analytics und die übergeordneten Analytics für den Canvas, wie _Gesamteintritte_, _Gesamtaustritte_ und _Konversionsrate_, werden gelöscht.
- Nutzer:innen in gelöschten Varianten verlassen die Schritte, und alle nachfolgenden Nachrichten werden nicht gesendet.

### Canvas-Eingangs-Eigenschaften {#canvas-entry-properties}

Canvas-Eingangs-Eigenschaften werden beim Senden nicht in Schritte eingebunden. Das bedeutet, dass Änderungen an Canvas-Eingangs-Eigenschaften nach dem Start eines Canvas nur für neue Nutzer:innen gelten, die den Canvas betreten. Wenn Ihr Canvas es Nutzer:innen erlaubt, den Canvas erneut zu betreten, werden alle Nutzer:innen, die erneut eintreten, anhand der aktualisierten Canvas-Eingangs-Eigenschaften bestimmt.

## Best Practices {#best-practices}

Beachten Sie diese Best Practices, wenn Sie Ihren Canvas nach dem Start bearbeiten oder ergänzen.

{% alert important %}
Vermeiden Sie generell Änderungen, während der Canvas aktiv ist und Nutzer:innen in die Warteschlange einreiht.
{% endalert %}

### Nicht verbundene Schritte {#disconnected-steps}

Sie können Ihren Canvas mit nicht verbundenen Schritten starten und diese Canvases auch nach dem Start speichern. Bevor Sie einen Schritt von Ihrem Workflow trennen, empfehlen wir, die Analytics-Ansicht der Schritte auf wartende Nutzer:innen zu überprüfen.

Nehmen wir an, eine Nutzer:in befindet sich in einem nicht verbundenen Schritt Ihres Canvas-Workflows. Diese Nutzer:in rückt zum nachfolgenden Schritt vor, sofern einer vorhanden ist. Die Einstellungen des Schritts bestimmen, wie die Nutzer:in vorrücken soll.

Durch das Erstellen oder Bearbeiten nicht verbundener Schritte können Sie Änderungen an diesen unabhängigen Schritten vornehmen, ohne sie direkt mit dem Rest Ihres Canvas verbinden zu müssen. Dies hilft beim Testen Ihrer Schritte, bevor Sie Ihren Canvas erneut starten.

### Experimentpfad-Schritt {#experiment-path-step}

Wenn Ihr Canvas ein aktives oder laufendes Gewinnerpfad- oder Personalisierter-Pfad-Experiment hat und Sie den aktiven Canvas aktualisieren (unabhängig davon, ob Sie den Experimentpfad-Schritt selbst aktualisieren), endet das laufende Experiment, und der Experimentpfade-Schritt bestimmt keinen Gewinnerpfad oder personalisierte Pfade. Um das Experiment neu zu starten, können Sie den bestehenden Experiment-Pfad trennen und einen neuen starten oder den Canvas duplizieren und einen neuen Canvas starten. Andernfalls durchlaufen Nutzer:innen den Experiment-Pfad, als ob keine Optimierungsmethode ausgewählt worden wäre.

### Zeitverzögerungen {#time-delays}

Das Bearbeiten von Canvases mit Zeitverzögerungen kann etwas knifflig sein. Beachten Sie daher die folgenden Details, wenn Sie Änderungen an Ihren Canvases vornehmen:

- Wenn Sie die Verzögerung in einem Verzögerungsschritt aktualisieren, erhalten nur neue Nutzer:innen, die den Canvas betreten, und Nutzer:innen, die noch nicht für diesen Schritt in die Warteschlange eingereiht wurden, die Nachricht mit der aktualisierten Zeitverzögerung.
- Wenn Sie einen Schritt mit einer Zeitverzögerung löschen (z. B. Verzögerung oder Aktionspfade) und sich entscheiden, diese Nutzer:innen in einen anderen Canvas-Schritt umzuleiten, werden die Nutzer:innen erst umgeleitet, nachdem die Zeitverzögerung des Schritts abgelaufen ist. Nehmen wir beispielsweise an, Sie löschen einen Verzögerungsschritt mit einer eintägigen Verzögerung und leiten diese Nutzer:innen in einen Nachrichten-Schritt um. In diesem Fall werden die Nutzer:innen erst nach Ablauf der eintägigen Verzögerung umgeleitet.
- Wenn Ihr Canvas einen oder mehrere Experimentpfade-Schritte enthält, könnte das Löschen von Schritten die Ergebnisse dieses Schritts ungültig machen.

### Canvases stoppen {#stopping-canvases}

Das Stoppen eines Canvas führt nicht dazu, dass Nutzer:innen, die in einem Schritt warten, den Canvas verlassen. Wenn Sie den Canvas wieder aktivieren und die Nutzer:innen noch warten, schließen sie den Schritt ab und rücken zum nächsten Schritt vor. Wenn jedoch der Zeitpunkt, zu dem die Nutzer:innen zum nächsten Schritt hätten vorrücken sollen, bereits verstrichen ist, verlassen sie stattdessen den Canvas.

Nehmen wir beispielsweise an, Sie haben einen Canvas mit dem Canvas-Flow-Workflow erstellt, der um 14:00 Uhr starten soll, mit einer Variante mit zwei Schritten: einem Verzögerungsschritt mit einer einstündigen Verzögerung, der in einen Nachrichten-Schritt übergeht.

Eine Nutzer:in betritt diesen Canvas um 14:01 Uhr und tritt gleichzeitig in den Verzögerungsschritt ein. Das bedeutet, dass die Nutzer:in planmäßig um 15:01 Uhr zum nächsten Schritt der User-Journey (dem Nachrichten-Schritt) vorrückt. Wenn Sie den Canvas um 14:30 Uhr stoppen und um 15:30 Uhr wieder aktivieren, verlässt die Nutzer:in den Canvas, da es nach 15:01 Uhr ist. Wenn Sie den Canvas jedoch um 14:40 Uhr wieder aktivieren, rückt die Nutzer:in wie erwartet um 15:01 Uhr zum Nachrichten-Schritt vor.

## Wissenswertes {#things-to-know}

Die folgenden häufigen Probleme können durch das Bearbeiten oder Hinzufügen weiterer Komponenten zu einer beliebigen anderen Komponente in einem Canvas nach dem Start ausgelöst werden.

{% alert important %}
Die folgenden Probleme sind vermeidbar. Wenn Sie nach dem Start Änderungen an einem Canvas vornehmen müssen, empfehlen wir, zunächst zu bestätigen, dass alle Nutzer:innen, die den Canvas bereits betreten haben, ihre User-Journey abgeschlossen haben. Außerdem empfehlen wir, keine Schritte zu löschen, die bereits von mindestens einer Nutzer:in verarbeitet wurden.
{% endalert %}

- Fehlende Berichtsdaten (wenn Nachrichtenvarianten gelöscht und erneut hinzugefügt werden)
- Nutzer:innen folgen nicht dem erwarteten Pfad
- Nachrichten werden zu unerwarteten Zeiten gesendet
- Die Änderungen überschreiben keine Currents-Daten, sodass Sie Diskrepanzen zwischen Canvas-Schritten bemerken können (z. B. `canvas_step_ids`, die aufgrund von Löschungen nicht mehr im Canvas existieren)
- Nutzer:innen können dieselbe Nachricht zweimal erhalten
- Nutzer:innen erhalten keine Nachrichten aufgrund des bestehenden Rate-Limits
  - Wenn Sie das Rate-Limit eines aktiven Canvas aktualisieren, tritt das neue Rate-Limit für alle zukünftigen Nachrichtenversendungen in Kraft, einschließlich der Nutzer:innen, die sich bereits im Canvas befinden. Aufgrund von internem Caching (bis zu 30 Sekunden) kann es jedoch zu einer kurzen Verzögerung kommen, bevor das neue Rate-Limit vollständig angewendet wird. Beachten Sie, dass Braze Nutzer:innen für den Nachrichten-Schritt in die Warteschlange einreiht, an dem sie sich gerade befinden, sodass das Rate-Limit, das zum Zeitpunkt des tatsächlichen Versands der Nachricht jedes Schritts gilt, das maßgebliche ist.
- Wenn ein Canvas [automatisch gestoppt]({{site.baseurl}}/user_guide/messaging/governance/statuses#available-statuses) wird, werden auch die Entwürfe nach dem Start des Canvas gelöscht.