---
nav_title: An Ziel senden
article_title: An Ziel senden
alias: "/send_to_destination/"
page_order: 11.5
page_type: reference
description: "Dieser Referenzartikel behandelt die Komponente „An Ziel senden“ und wie Sie sie in Ihren Canvases verwenden können."
tool: Canvas
---
# Canvas-Schritt „An Ziel senden"

> Der Canvas-Schritt „An Ziel senden" ermöglicht es Ihnen, Nutzer:innen von einem Canvas in einen anderen zu senden. Wenn Sie beispielsweise zwei Canvases haben, die Messaging für Aktionsangebote teilen, können Sie „An Ziel senden" verwenden, um diese Canvases zu verbinden.

## So funktioniert es

![Ein Canvas-Schritt „An Ziel senden", um Nutzer:innen in einen neuen Canvas zu senden.]({% image_buster /assets/img/send_to_destination1.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Ihr aktueller Canvas mit dem Canvas-Schritt „An Ziel senden" ist die Quelle. Innerhalb des Schritts können Sie den Ziel-Canvas auswählen. Von hier aus werden Nutzer:innen an den Ziel-Canvas gesendet. Sie durchlaufen diesen Canvas, wenn sie die dortigen Eingangskriterien erfüllen, und fließen gleichzeitig weiter durch den Quell-Canvas.

## Einen Canvas-Schritt „An Ziel senden" erstellen

### 1. Schritt: Einen Schritt hinzufügen

Ziehen Sie die Komponente **An Ziel senden** per Drag-and-Drop aus der Seitenleiste, oder wählen Sie den <i class="fas fa-plus-circle"></i> Plus-Button am unteren Rand eines Schritts und wählen Sie **An Ziel senden**.

### 2. Schritt: Ihr Ziel auswählen

Wählen Sie das Dropdown aus oder geben Sie den Canvas-Namen im Feld **Ziel** ein. Wählen Sie dann **Fertig**.

![Ein Canvas-Schritt „An Ziel senden", der so eingerichtet ist, dass Nutzer:innen von einem Canvas namens „Feature Adoption" an „New Canvas" gesendet werden.]({% image_buster /assets/img/send_to_destination2.png %})

### 3. Schritt: Vorschau Ihres Ziels

Sie können **Zielvorschau** auswählen, um die Journey für Nutzer:innen zu sehen, die die Eingangskriterien für den Ziel-Canvas erfüllen.

Nachdem Sie diesen Canvas-Schritt eingerichtet haben, können Sie eine [Vorschau des Nutzerpfads]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths) anzeigen, um zu sehen, ob Nutzer:innen zum nächsten Schritt im aktuellen Canvas weitergeleitet werden und ob sie auch zum Ziel-Canvas weitergeleitet werden.

## Häufig gestellte Fragen

### Kann ich als Ziel einen Canvas im Entwurfsstatus festlegen?

Ja. Der Ziel-Canvas kann den Status „Entwurf" oder „Inaktiv" haben.

### Bleiben Kontextvariablen erhalten?

Ja. Der [Kontext]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) des Quell-Canvas wird immer an den Ziel-Canvas übergeben.