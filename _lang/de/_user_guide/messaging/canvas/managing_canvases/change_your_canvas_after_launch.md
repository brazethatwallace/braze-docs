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

- Canvas-Name und -Beschreibung
- Teams
- Tags
  - Wenn Sie nach dem Start einen Tag hinzufügen, können Sie Nutzer:innen in Segments mit Filtern wie `Received Message from Campaign or Canvas with Tag` retargeten.
- Entry-Typ, Zeitplan und Kontrollen
- Abo-Status
- Rate-Limits
- Frequency-Capping
- Ruhezeiten
- Zielgruppe

Nach dem Start eines Canvas:

- Konversions-Events können nicht bearbeitet werden.
- Die folgenden Schritte können nicht hinzugefügt oder entfernt und nicht neu angeordnet werden, um die Rangfolge anzupassen: [Zielgruppenpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths), [Aktionspfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) und [Experimentpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step).
  - **Workaround 1:** Erstellen Sie einen neuen Zielgruppenpfad, Aktionspfad oder Experimentpfad und konfigurieren Sie die Pfade für diesen neuen Schritt neu.
  - **Workaround 2:** Duplizieren Sie den Canvas, um Ihre Änderungen vorzunehmen.

### Einzelne Schritte {#individual-steps}

Für einzelne Canvas-Schritte können Sie nach dem Start die folgenden Details bearbeiten:

* Name
* Nachrichteninhalt
* Trigger
* Zielgruppe
* Ausnahme-Events
* Verzögerungen (nur für Verzögerungsschritte)

Der Zeitplantyp und die Kontrollprozentsätze des Schritts können nach dem Start jedoch nicht bearbeitet werden. Bei Aktionspfad- und Zielgruppenpfad-Schritten sind die Rangfolgen und Auswertungsfenster nach dem Start nicht bearbeitbar.

#### Schritt „An Ziel senden“ {#send-to-destination-step}

Wenn Sie den Schritt [An Ziel senden]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination) in einem aktiven Canvas bearbeiten, gelten die folgenden Verhaltensweisen:

- **Ändern des Ziel-Canvas:** Das Bearbeiten des Schritts „An Ziel senden“, um auf einen anderen Ziel-Canvas zu verweisen, folgt denselben allgemeinen Bearbeitungsregeln nach dem Start. Änderungen betreffen nur Nutzer:innen, die den Schritt „An Ziel senden“ noch nicht erreicht haben.
  - Nutzer:innen, die den Schritt bereits durchlaufen haben, verbleiben im ursprünglichen Ziel-Canvas – sie werden nicht umgeleitet.
  - Nutzer:innen, die sich derzeit in früheren Schritten in der Warteschlange befinden (z. B. in einem Verzögerungsschritt vor dem Schritt „An Ziel senden“ warten), werden anhand der Entry- und Zielgruppenkriterien des neuen Ziel-Canvas ausgewertet, wenn sie den Schritt erreichen. Berechtigte Nutzer:innen werden an den neuen Ziel-Canvas gesendet.
- **Gestoppter Ziel-Canvas:** Wenn der Ziel-Canvas gestoppt wird, während Ihr Quell-Canvas noch aktiv ist, werden Nutzer:innen, die den Schritt „An Ziel senden“ erreichen, nicht an den Ziel-Canvas gesendet. Dies führt zu einem Nutzer:innen-Abbruch bei der Übergabe, nicht zu einer Pause, während das Ziel gestoppt ist.
  - Nutzer:innen, die den gestoppten Ziel-Canvas nicht betreten können, setzen ihren Weg im Quell-Canvas fort, wenn nach dem Schritt „An Ziel senden“ weitere Schritte folgen. Weitere Informationen zum Fortschrittsverhalten finden Sie unter [An Ziel senden]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination#how-does-advancement-behavior-work-for-send-to-destination-steps).
  - Sie können keinen Quell-Canvas mit einem Schritt „An Ziel senden“ starten, der auf ein gestopptes Ziel verweist. Dieses Verhalten gilt, wenn ein Ziel-Canvas gestoppt wird, nachdem der Quell-Canvas bereits aktiv ist.

### Canvas-Varianten-Prozentsätze {#canvas-variant-percentages}

Nach dem Start eines Canvas können Sie die Prozentsätze der Kontrollvariante nur verringern. Wenn ein Varianten-Prozentsatz in Canvas geändert wird, können Ihre Nutzer:innen auf andere Varianten umverteilt werden.

Anfangs werden diesen Nutzer:innen zufällig eine bestimmte Variante zugewiesen, bevor sie zum ersten Mal eine Campaign erhalten. Von da an erhalten sie jedes weitere Mal, wenn die Campaign empfangen wird (oder die Nutzer:innen erneut in eine Canvas-Variante eintreten), dieselbe Variante, es sei denn, die Varianten-Prozentsätze werden geändert.

Wenn sich die Varianten-Prozentsätze ändern, können Nutzer:innen auf andere Varianten umverteilt werden. Nutzer:innen bleiben in diesen Varianten, bis die Prozentsätze erneut geändert werden. Beachten Sie, dass bei Canvases, die Verzweigungen mit `NOT`-Filtern mit zufälligen Bucket-Nummern verwenden, Nutzer:innen möglicherweise nicht bei jedem Wiedereintritt in den Canvas denselben Zweig in ihrer User Journey erhalten.

#### Kontrollgruppen {#control-groups}

Kontrollgruppen bleiben konsistent, wenn der Varianten-Prozentsatz unverändert bleibt. Wenn der Prozentsatz einer Kontrollgruppe verringert oder erhöht wird, können Nutzer:innen, die zuvor Nachrichten erhalten haben, bei einem späteren Versand nicht in die Kontrollgruppe eintreten, und keine Nutzer:innen in der Kontrollgruppe würden jemals eine Nachricht erhalten.

### Lokale Sendezeit {#local-send-time}

Canvases, die zu einer lokalen Sendezeit gestartet werden sollen, können bis zu 24 Stunden vor der geplanten Sendezeit bearbeitet werden. Dieses Fenster wird als „sichere Zone“ bezeichnet.

{% alert tip %}
Wenn Sie größere Änderungen vornehmen möchten, die zur Erstellung einer vollständig neuen Canvas-Kopie führen, denken Sie daran, Nutzer:innen auszuschließen, die den ersten Canvas erhalten haben, und die Canvas-Zeitplanzeiten anzupassen, um den Versand nach Zeitzonen zu ermöglichen.
{% endalert %}

Wenn ein Entry-Zeitplan so eingestellt ist, dass Nutzer:innen sofort beim Start eintreten, wird der Canvas zum nächstgelegenen Zeitpunkt in 5-Minuten-Schritten gestartet. Wenn Sie beispielsweise einen Canvas aktualisieren, damit Nutzer:innen sofort um 8:31 Uhr PST eintreten, wird die Startzeit auf 8:30 Uhr PST und in der Zeitzone des Unternehmens festgelegt.

### Varianten löschen {#deleting-variants}

Wenn Varianten aus einem Canvas gelöscht werden, geschieht Folgendes:

- Schritte innerhalb der Variante (einschließlich solcher, die mit anderen Varianten geteilt werden) werden gelöscht.
- Die Schritt-Analytics und die übergeordneten Analytics für den Canvas, wie _Gesamteintritte_, _Gesamtaustritte_ und _Konversionsrate_, werden gelöscht.
- Nutzer:innen in gelöschten Varianten werden aus den Schritten entfernt, und alle folgenden Nachrichten werden nicht gesendet.

### Canvas-Entry-Eigenschaften {#canvas-entry-properties}

Canvas-Entry-Eigenschaften werden beim Senden nicht in Schritte eingebunden. Das bedeutet, dass Änderungen an Canvas-Entry-Eigenschaften nach dem Start eines Canvas nur für neue Nutzer:innen gelten, die den Canvas betreten. Wenn Ihr Canvas Nutzer:innen den erneuten Eintritt erlaubt, werden alle Nutzer:innen, die erneut eintreten, anhand der aktualisierten Canvas-Entry-Eigenschaften bestimmt.

## Best Practices {#best-practices}

Beachten Sie diese Best Practices, wenn Sie Ihren Canvas nach dem Start bearbeiten oder ergänzen.

{% alert important %}
Vermeiden Sie es generell, Änderungen vorzunehmen, während der Canvas aktiv ist und Nutzer:innen in die Warteschlange eingereiht werden.
{% endalert %}

### Nicht verbundene Schritte {#disconnected-steps}

Sie können Ihren Canvas mit nicht verbundenen Schritten starten und diese Canvases auch nach dem Start speichern. Bevor Sie einen Schritt von Ihrem Workflow trennen, empfehlen wir, die Analytics-Ansicht der Schritte auf wartende Nutzer:innen zu überprüfen.

Nehmen wir an, ein:e Nutzer:in befindet sich in einem nicht verbundenen Schritt Ihres Canvas-Workflows. Diese:r Nutzer:in rückt zum nachfolgenden Schritt vor, sofern einer vorhanden ist. Die Einstellungen des Schritts bestimmen, wie der Fortschritt erfolgen soll.

Durch das Erstellen oder Bearbeiten nicht verbundener Schritte können Sie Änderungen an diesen unabhängigen Schritten vornehmen, ohne sie direkt mit dem Rest Ihres Canvas verbinden zu müssen. Dies hilft beim Testen Ihrer Schritte, bevor Sie Ihren Canvas erneut starten.

### Experimentpfad-Schritt {#experiment-path-step}

Wenn Ihr Canvas ein aktives oder laufendes Winning-Path- oder Personalized-Path-Experiment enthält und Sie den aktiven Canvas aktualisieren (unabhängig davon, ob Sie den Experimentpfad-Schritt selbst aktualisieren), wird das laufende Experiment beendet, und der Experimentpfad-Schritt ermittelt keinen Gewinnerpfad oder personalisierte Pfade. Um das Experiment neu zu starten, können Sie den bestehenden Experimentpfad trennen und einen neuen starten oder den Canvas duplizieren und einen neuen Canvas starten. Andernfalls durchlaufen Nutzer:innen den Experimentpfad, als ob keine Optimierungsmethode ausgewählt worden wäre.

### Zeitverzögerungen {#time-delays}

Das Bearbeiten von Canvases mit Zeitverzögerungen kann etwas knifflig sein. Beachten Sie daher die folgenden Details, wenn Sie Änderungen an Ihren Canvases vornehmen:

- Wenn Sie die Verzögerung in einem Delay-Schritt aktualisieren, erhalten nur neue Nutzer:innen, die den Canvas betreten, und Nutzer:innen, die noch nicht für diesen Schritt in die Warteschlange eingereiht wurden, die Nachricht mit der aktualisierten Zeitverzögerung.
- Wenn Sie einen Schritt mit einer Zeitverzögerung löschen (z. B. Delay oder Aktionspfade) und diese Nutzer:innen in einen anderen Canvas-Schritt umleiten möchten, werden die Nutzer:innen erst nach Ablauf der Zeitverzögerung des Schritts umgeleitet. Nehmen wir beispielsweise an, Sie löschen einen Delay-Schritt mit einer eintägigen Verzögerung und leiten diese Nutzer:innen zu einem Nachrichten-Schritt um. In diesem Fall werden die Nutzer:innen erst nach Ablauf der eintägigen Verzögerung umgeleitet.
- Wenn Ihr Canvas einen oder mehrere Experimentpfad-Schritte enthält, kann das Löschen von Schritten die Ergebnisse dieses Schritts ungültig machen.

### Canvases stoppen {#stopping-canvases}

Das Stoppen eines Canvas bewirkt nicht, dass Nutzer:innen, die in einem Schritt warten, den Canvas verlassen. Wenn Sie den Canvas erneut aktivieren und die Nutzer:innen noch warten, schließen sie den Schritt ab und gehen zum nächsten Schritt über. Wenn jedoch der Zeitpunkt, zu dem die Nutzer:innen zum nächsten Schritt hätten vorrücken sollen, bereits verstrichen ist, verlassen sie stattdessen den Canvas.

Nehmen wir beispielsweise an, Sie haben einen Canvas mit dem Canvas-Flow-Workflow erstellt, der um 14:00 Uhr starten soll, mit einer Variante und zwei Schritten: einem Delay-Schritt mit einer einstündigen Verzögerung, gefolgt von einem Nachrichten-Schritt.

Ein:e Nutzer:in betritt diesen Canvas um 14:01 Uhr und gelangt gleichzeitig in den Delay-Schritt. Das bedeutet, dass diese:r Nutzer:in planmäßig um 15:01 Uhr zum nächsten Schritt der User Journey (dem Nachrichten-Schritt) vorrückt. Wenn Sie den Canvas um 14:30 Uhr stoppen und um 15:30 Uhr erneut aktivieren, verlässt der/die Nutzer:in den Canvas, da es bereits nach 15:01 Uhr ist. Wenn Sie den Canvas jedoch um 14:40 Uhr erneut aktivieren, rückt der/die Nutzer:in wie erwartet um 15:01 Uhr zum Nachrichten-Schritt vor.

## Wissenswertes {#things-to-know}

Die folgenden häufigen Probleme können auftreten, wenn Sie nach dem Start eines Canvas Komponenten bearbeiten oder weitere Komponenten zu einer beliebigen anderen Komponente in einem Canvas hinzufügen.

{% alert important %}
Die folgenden Probleme sind vermeidbar. Wenn Sie nach dem Start Änderungen an einem Canvas vornehmen müssen, empfehlen wir, zunächst sicherzustellen, dass alle Nutzer:innen, die bereits in das Canvas eingetreten sind, ihre User Journey abgeschlossen haben. Darüber hinaus empfehlen wir, keine Schritte zu löschen, die bereits von mindestens einer/einem Nutzer:in durchlaufen wurden.
{% endalert %}

- Fehlende Berichtsdaten (wenn Nachrichtenvarianten gelöscht und erneut hinzugefügt werden)
- Nutzer:innen folgen nicht dem erwarteten Pfad
- Nachrichten werden zu unerwarteten Zeiten gesendet
- Die Änderungen überschreiben keine Currents-Daten, sodass Ihnen möglicherweise Abweichungen zwischen Canvas-Schritten auffallen (z. B. `canvas_step_ids`, die aufgrund einer Löschung nicht mehr im Canvas vorhanden sind)
- Nutzer:innen können dieselbe Nachricht zweimal erhalten
- Nutzer:innen erhalten aufgrund des bestehenden Rate-Limits keine Nachrichten
  - Wenn Sie das Rate-Limit eines aktiven Canvas aktualisieren, gilt das neue Rate-Limit nur für Nutzer:innen, die den Nachrichten-Schritt nach der Änderung des Rate-Limits durchlaufen. Nutzer:innen, die sich bereits in der Warteschlange für einen Nachrichten-Schritt befinden, behalten das ursprüngliche Rate-Limit bei, das zum Zeitpunkt ihrer Einreihung in die Warteschlange galt. Um ein neues Rate-Limit auf alle Nutzer:innen anzuwenden, stoppen Sie das Canvas, duplizieren Sie es mit dem aktualisierten Rate-Limit und starten Sie das neue Canvas. Verwenden Sie einen Filter, um zu verhindern, dass Nutzer:innen, die Nachrichten aus dem ursprünglichen Canvas erhalten haben, in das Duplikat eintreten.
- Wenn ein Canvas [automatisch gestoppt]({{site.baseurl}}/user_guide/messaging/governance/statuses#available-statuses) wird, werden auch die nach dem Start erstellten Entwürfe des Canvas gelöscht.