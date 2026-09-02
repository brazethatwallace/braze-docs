---
nav_title: An Ziel senden
article_title: An Ziel senden
alias: "/send_to_destination/"
page_order: 11.5
page_type: reference
description: "Dieser Referenzartikel behandelt die Komponente „An Ziel senden“ und wie Sie sie in Ihren Canvase verwenden können."
tool: Canvas
---

# Canvas-Schritt „An Ziel senden“ {#send-to-destination-step}

> Der Canvas-Schritt „An Ziel senden“ ermöglicht es Ihnen, Nutzer:innen von einem Canvas in einen anderen zu senden. So können Sie beispielsweise Canvase verbinden, die gemeinsames Messaging für Aktionsangebote nutzen.

## So funktioniert es {#how-it-works}

![Ein „An Ziel senden“-Schritt, um Nutzer:innen an einen neuen Canvas zu senden.]({% image_buster /assets/img/send_to_destination1.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Ihr aktueller Canvas mit dem „An Ziel senden“-Schritt ist die Quelle. Innerhalb des Schritts können Sie den Ziel-Canvas auswählen. Nutzer:innen aus dem Quell-Canvas müssen die Zielgruppenkriterien des Ziel-Canvas erfüllen. Nehmen wir an, Sie haben zwei Canvase:

- **Quelle:** Canvas 1 enthält einen „An Ziel senden“-Schritt, der Nutzer:innen an Canvas 2 sendet
- **Ziel:** Canvas 2 mit Zielgruppenkriterien für Nutzer:innen, die einen Artikel bestellt haben

Dieser Schritt ermöglicht es, Nutzer:innen von Canvas 1 an Canvas 2 zu senden. Wenn Nutzer:innen aus Canvas 1 den „An Ziel senden“-Schritt erreichen, werden sie anhand der Zielgruppenkriterien von Canvas 2 bewertet, um festzustellen, ob sie berechtigt sind, den Canvas zu betreten. In diesem Fall können Nutzer:innen, die einen Artikel bestellt haben, Canvas 2 betreten und gleichzeitig ihre Journey in Canvas 1 fortsetzen. Nutzer:innen, die keinen Artikel bestellt haben, setzen ihre Journey nur in Canvas 1 fort.

### Entry-Verhalten {#entry-behavior}

Der „An Ziel senden“-Schritt lässt Nutzer:innen in den Ziel-Canvas eintreten, sobald sie diesen Schritt erreichen. Dieser Schritt fungiert als einmaliger Entry-Punkt in den Ziel-Canvas. Nutzer:innen, die die Zielgruppenkriterien des Ziel-Canvas erfüllen, beginnen diese Canvas-Journey. Nutzer:innen, die diese Kriterien zu diesem Zeitpunkt nicht erfüllen, betreten den Ziel-Canvas nicht und setzen ihre Journey im Quell-Canvas fort.

„An Ziel senden“ berücksichtigt auch die [Wiedereintrittseinstellungen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) des Ziel-Canvas unter **Entry Controls**. Wenn Nutzer:innen nicht berechtigt sind, erneut in den Ziel-Canvas einzutreten, werden sie nicht dorthin gesendet und setzen ihre Journey im Quell-Canvas fort.

Wenn der Ziel-Canvas einen geplanten Eintrittszeitplan verwendet, umgeht der „An Ziel senden“-Schritt diesen Eintrittszeitplan. Er umgeht außerdem die Einstellung [**Eintrittsvolumen begrenzen**]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) unter **Entry Controls** im Ziel-Canvas, wenn diese auf **Every time Canvas is schedule** eingestellt ist. Nutzer:innen, die über diesen Schritt gesendet werden, warten nicht auf das nächste geplante Auswertungsfenster – sie werden sofort anhand der Zielgruppenkriterien des Ziel-Canvas bewertet und treten ein, sobald sie den „An Ziel senden“-Schritt erreichen.

Wenn der Ziel-Canvas einen aktionsbasierten Eintritt verwendet, umgeht der „An Ziel senden“-Schritt die Anforderung, dass Nutzer:innen die konfigurierte Eintrittsaktion ausführen müssen, um diesen Canvas zu betreten.

## Einen „An Ziel senden“-Schritt erstellen {#create-a-send-to-destination-step}

### Schritt 1: Einen Schritt hinzufügen {#step-1-add-a-step}

Ziehen Sie die Komponente **An Ziel senden** per Drag-and-drop aus der Seitenleiste, oder wählen Sie den <i class="fas fa-plus-circle"></i> Plus-Button am unteren Rand eines Schritts und wählen Sie **An Ziel senden**.

### Schritt 2: Ihr Ziel auswählen {#step-2-choose-your-destination}

Wählen Sie das Dropdown-Menü aus oder geben Sie den Canvas-Namen in das Feld **Ziel** ein. Wählen Sie dann **Fertig**.

![Ein „An Ziel senden“-Schritt, der so eingerichtet ist, dass Nutzer:innen von einem Canvas namens „Feature Adoption“ zu „New Canvas“ gesendet werden.]({% image_buster /assets/img/send_to_destination2.png %})

### Schritt 3: Ihr Ziel in der Vorschau anzeigen {#step-3-preview-your-destination}

Sie können **Ziel in der Vorschau anzeigen** auswählen, um den Canvas anzuzeigen, an den Sie Nutzer:innen senden.

Nachdem Sie diesen Canvas-Schritt eingerichtet haben, können Sie [den Nutzerpfad in der Vorschau anzeigen]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths), um zu sehen, ob Nutzer:innen zum nächsten Schritt im aktuellen Canvas weitergeleitet werden und ob sie auch zum Ziel-Canvas weitergeleitet werden.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Kann ich ein Canvas im Entwurfsstatus als Ziel festlegen? {#can-i-set-the-destination-to-a-draft-canvas}

Ja. Das Ziel-Canvas kann den Status „Entwurf“ oder „Inaktiv“ haben.

### Bleiben Kontextvariablen erhalten? {#are-context-variables-preserved}

Ja. Der [Kontext]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) des Quell-Canvas wird an das Ziel-Canvas übergeben. Kontextvariablen müssen jedoch innerhalb des Quell-Canvas aufgerufen werden, damit sie an das Ziel-Canvas übergeben werden.

### Kann ich den Schritt „An Ziel senden“ verwenden, um Canvase zu verbinden, anstatt API- oder User-Update or aktualisieren-Workarounds zu nutzen? {#can-i-use-the-send-to-destination-step-to-connect-canvases-instead-of-using-api-or-user-update-workarounds}

Ja. Sie können Canvase mit dem Schritt „An Ziel senden“ verbinden, wenn Nutzer:innen direkt in eine andere Canvas-Journey wechseln sollen.

Sie benötigen keine separaten User-Update or aktualisieren-Schritte, API-Trigger or triggern oder Webhooks, nur um Nutzer:innen zwischen Canvase zu verschieben – vorausgesetzt, sie erfüllen die Zielgruppenkriterien des Ziel-Canvas zum Zeitpunkt des Versands.

### Treten Nutzer:innen am Anfang des Ziel-Canvas ein? {#do-users-enter-at-the-start-of-the-destination-canvas}

Berechtigte Nutzer:innen treten sofort beim ersten Schritt des Ziel-Canvas ein. Sie warten nicht auf einen späteren geplanten Eintrittszeitpunkt des Ziel-Canvas. Ein Einstieg in einen bestimmten Canvas-Schritt innerhalb des Ziel-Canvas ist nicht möglich.

### Berücksichtigt der Schritt „An Ziel senden“ den geplanten Eintrittszeitplan eines Ziel-Canvas? {#does-the-send-to-destination-step-respect-a-scheduled-destination-canvas-entry-schedule}

Nein. Wenn das Ziel-Canvas einen geplanten Eintrittstyp verwendet, warten Nutzer:innen, die über den Schritt „An Ziel senden“ gesendet werden, nicht auf das nächste geplante Evaluierungsfenster. Sie werden sofort anhand der Zielgruppenkriterien ausgewertet und treten ein, sobald sie den Schritt „An Ziel senden“ erreichen.

### Wie funktioniert das Fortschrittsverhalten bei Schritten vom Typ „An Ziel senden“? {#how-does-advancement-behavior-work-for-send-to-destination-steps}

Nutzer:innen, die den Schritt „An Ziel senden“ erreichen, setzen ihre Journey fort, wenn im Quell-Canvas weitere Schritte vorhanden sind. Wenn Nutzer:innen zusätzlich die Zielgruppenkriterien des Ziel-Canvas erfüllen, können sie in dieses Canvas eintreten und diese Journey beginnen.

### Unterliegt der Schritt „An Ziel senden“ API-Rate-Limits? {#is-the-send-to-destination-step-subject-to-api-rate-limits}

Nein. Nutzer:innen werden innerhalb von Braze zwischen Canvase verschoben, ohne dass externe API-Aufrufe erfolgen.