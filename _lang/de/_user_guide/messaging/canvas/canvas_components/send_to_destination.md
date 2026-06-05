---
nav_title: An Ziel senden
article_title: An Ziel senden
alias: "/send_to_destination/"
page_order: 11.5
page_type: reference
description: "Dieser Referenzartikel behandelt die Komponente „An Ziel senden“ und wie Sie sie in Ihren Canvases verwenden können."
tool: Canvas
---

# Canvas-Schritt „An Ziel senden“ {#send-to-destination-step}

> Der Canvas-Schritt „An Ziel senden“ ermöglicht es Ihnen, Nutzer:innen von einem Canvas in einen anderen zu senden. So können Sie beispielsweise Canvases verbinden, die gemeinsames Messaging für Aktionsangebote nutzen.

## So funktioniert es {#how-it-works}

![Ein Canvas-Schritt „An Ziel senden“, um Nutzer:innen in einen neuen Canvas zu senden.]({% image_buster /assets/img/send_to_destination1.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Ihr aktueller Canvas mit dem Canvas-Schritt „An Ziel senden“ ist die Quelle. Innerhalb des Schritts können Sie den Ziel-Canvas auswählen. Nutzer:innen aus dem Quell-Canvas müssen die Eingangs- und Zielgruppenkriterien des Ziel-Canvas erfüllen. Nehmen wir an, Sie haben zwei Canvases:

- **Quelle:** Canvas 1, enthält einen Canvas-Schritt „An Ziel senden“, der Nutzer:innen an Canvas 2 sendet
- **Ziel:** Canvas 2, mit dem Eingangskriterium, Nutzer:innen aufzunehmen, die einen Artikel bestellt haben

Dieser Schritt ermöglicht es, Nutzer:innen von Canvas 1 an Canvas 2 zu senden. Wenn Nutzer:innen aus Canvas 1 den Canvas-Schritt „An Ziel senden“ erreichen, werden sie anhand der Eingangs- und Zielgruppenkriterien von Canvas 2 geprüft, um festzustellen, ob sie berechtigt sind, den Canvas zu betreten. In diesem Fall können Nutzer:innen, die einen Artikel bestellt haben, Canvas 2 betreten und gleichzeitig ihre Journey in Canvas 1 fortsetzen. Nutzer:innen, die keinen Artikel bestellt haben, setzen ihre Journey nur in Canvas 1 fort.

### Realtime-Eintritt {#real-time-entry}

„An Ziel senden“ leitet Nutzer:innen in den Ziel-Canvas, sobald sie diesen Schritt erreichen. Dieser Schritt fungiert als einmaliger Eintrittspunkt in den Ziel-Canvas. Nutzer:innen, die die Eingangs- und Zielgruppenkriterien des Ziel-Canvas erfüllen, beginnen diese Canvas-Journey in Realtime. Nutzer:innen, die diese Kriterien zu diesem Zeitpunkt nicht erfüllen, betreten den Ziel-Canvas nicht und setzen ihre Journey im Quell-Canvas fort.

## Einen Canvas-Schritt „An Ziel senden“ erstellen {#create-a-send-to-destination-step}

### 1. Schritt: Einen Schritt hinzufügen {#step-1-add-a-step}

Ziehen Sie die Komponente **Send to Destination** per Drag-and-Drop aus der Seitenleiste, oder wählen Sie den <i class="fas fa-plus-circle"></i> Plus-Button am unteren Rand eines Schritts und wählen Sie **Send to Destination**.

### 2. Schritt: Ihr Ziel auswählen {#step-2-choose-your-destination}

Wählen Sie das Dropdown aus oder geben Sie den Canvas-Namen im Feld **Destination** ein. Wählen Sie dann **Done**.

![Ein Canvas-Schritt „An Ziel senden“, der so eingerichtet ist, dass Nutzer:innen von einem Canvas namens „Feature Adoption“ an „New Canvas“ gesendet werden.]({% image_buster /assets/img/send_to_destination2.png %})

### 3. Schritt: Vorschau Ihres Ziels {#step-3-preview-your-destination}

Sie können **Preview destination** auswählen, um die Journey für Nutzer:innen zu sehen, die die Eingangskriterien für den Ziel-Canvas erfüllen.

Nachdem Sie diesen Canvas-Schritt eingerichtet haben, können Sie eine [Vorschau des Nutzerpfads]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths/) anzeigen, um zu sehen, ob Nutzer:innen zum nächsten Schritt im aktuellen Canvas weitergeleitet werden und ob sie auch zum Ziel-Canvas weitergeleitet werden.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Kann ich als Ziel einen Canvas im Entwurfsstatus festlegen? {#can-i-set-the-destination-to-a-draft-canvas}

Ja. Der Ziel-Canvas kann den Status „Entwurf“ oder „Inaktiv“ haben.

### Bleiben Kontextvariablen erhalten? {#are-context-variables-preserved}

Ja. Der [Kontext]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/) des Quell-Canvas wird immer an den Ziel-Canvas übergeben.

### Kann ich den Canvas-Schritt „An Ziel senden“ verwenden, um Canvases zu verbinden, anstatt API- oder Nutzeraktualisierungs-Workarounds zu nutzen? {#can-i-use-the-send-to-destination-step-to-connect-canvases-instead-of-using-api-or-user-update-workarounds}

Ja. Sie können Canvases mit dem Canvas-Schritt „An Ziel senden“ verbinden, wenn Nutzer:innen direkt in eine andere Canvas-Journey wechseln sollen.

Sie benötigen keine separaten Nutzeraktualisierungs-Schritte, API-Trigger oder Webhooks, nur um Nutzer:innen zwischen Canvases zu verschieben – vorausgesetzt, sie erfüllen die Kriterien des Ziel-Canvas zum Zeitpunkt des Sendens.

### Betreten Nutzer:innen den Ziel-Canvas am Anfang? {#do-users-enter-at-the-start-of-the-destination-canvas}

Berechtigte Nutzer:innen betreten sofort den ersten Schritt des Ziel-Canvas. Sie warten nicht auf einen späteren geplanten Eintrittszeitpunkt des Ziel-Canvas. Es ist nicht möglich, auf einen bestimmten Canvas-Schritt innerhalb des Ziel-Canvas zu verlinken.

### Berücksichtigt der Canvas-Schritt „An Ziel senden“ den geplanten Entry-Zeitplan eines Ziel-Canvas? {#does-the-send-to-destination-step-respect-a-scheduled-destination-canvas-entry-schedule}

Nein. Wenn der Ziel-Canvas einen geplanten Entry-Typ verwendet, warten Nutzer:innen, die über den Canvas-Schritt „An Ziel senden“ gesendet werden, nicht auf das nächste geplante Auswertungsfenster. Sie werden ausgewertet und eingetragen, wenn sie den Canvas-Schritt „An Ziel senden“ erreichen, sofern sie die Eingangs- und Zielgruppenkriterien des Ziel-Canvas erfüllen.

### Wie funktioniert das Fortschrittsverhalten bei Canvas-Schritten „An Ziel senden“? {#how-does-advancement-behavior-work-for-send-to-destination-steps}

Nutzer:innen, die den Canvas-Schritt „An Ziel senden“ erreichen, setzen ihre Journey fort, wenn es weitere Schritte im Quell-Canvas gibt. Wenn Nutzer:innen auch die Eingangsregeln des Ziel-Canvas erfüllen, können sie diesen Canvas betreten und diese Journey beginnen.