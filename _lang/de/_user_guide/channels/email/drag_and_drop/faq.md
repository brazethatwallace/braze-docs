---
nav_title: FAQ
article_title: FAQ zum Drag-and-Drop-Editor
alias: "/dnd/faq/"
channel: email
page_order: 5
description: "Dieser Artikel behandelt verschiedene häufig gestellte Fragen zum Drag-and-Drop-Editor."
tool:
  - Campaigns
  - Canvas

---
# Häufig gestellte Fragen

> Diese Seite bietet Antworten auf einige häufig gestellte Fragen zum Drag-and-Drop-Editor für E-Mail.

### Kann ich eine Vorschau anzeigen, wie meine E-Mail im Dark Mode aussieht?

Ja. Gehen Sie zum Abschnitt **Vorschau und Test** des Drag-and-Drop-Editors und aktivieren Sie den **Dark Mode**. Wir empfehlen außerdem, Ihre E-Mails auf verschiedenen Plattformen in der Vorschau anzuzeigen und zu testen sowie nach Möglichkeit transparente Bilder für Zeilen-Hintergrundbilder zu verwenden.

### Wie sollte ich E-Mails für den Dark Mode und den Light Mode gestalten?

E-Mails müssen nicht in separaten Light- und Dark-Layouts versendet werden, da E-Mail-Clients und Geräte ihr eigenes dunkles Design anwenden können. Dies kann jedoch Farben invertieren oder Hintergründe ausblenden, wenn keine expliziten Farben für den äußeren Container und die Hauptabschnitte festgelegt sind. Um dies zu verhindern, empfehlen wir, feste Hintergrundfarben festzulegen, damit Ihre Nachricht sowohl im Dark Mode als auch im Light Mode gut lesbar ist.

### Wie kann ich das E-Mail-Padding auf Mobilgeräten ändern, ohne das Padding in der Web-Ansicht zu aktualisieren?

Sie können das Padding für Mobilgeräte- und Web-Ansichten nicht separat bearbeiten, sodass alle Änderungen in beiden Ansichten übernommen werden. Sie können jedoch CSS-Logik im HTML-Editor hinzufügen, die das Padding basierend auf verschiedenen Bildschirmgrößen festlegt. Dies wird im Drag-and-Drop-Editor nicht unterstützt, sodass Sie die HTML-Datei exportieren und stattdessen den HTML-Editor verwenden können.

### Wie kann ich eine Reihe von Buttons optimieren, damit sie auf Desktop und Mobilgeräten horizontal bleiben?

Wenn Sie eine E-Mail mit dem Drag-and-Drop-Editor erstellen und eine horizontale Reihe von Call-to-Action-Buttons anlegen, kann es vorkommen, dass die Buttons auf Mobilgeräten vertikal angeordnet werden.

Um das gleiche Format über verschiedene Gerätegrößen hinweg beizubehalten, empfehlen wir, eine separate Zeile mit CTA-Buttons zu erstellen, deren Padding für Mobilgeräte optimiert ist, und die Zeile auf Desktop-Geräten auszublenden. Durch zwei separate Zeilen können Sie das gewünschte Padding für die beste Textdarstellung auf Desktop- und Mobilgeräten festlegen.


### Kann ich die Zeilenhöhe im Drag-and-Drop-Editor anpassen?

Die Zeilenhöhe passt sich automatisch an den Inhalt an. Alternativ empfehlen wir Folgendes:
1. Fügen Sie einen Trennlinien-Block hinzu.
2. Klicken Sie auf den Schalter, um die Transparenz zu aktivieren.
3. Passen Sie die Höhe an.

### Ist es möglich, Ebenen im Editor zu erstellen? Kann ich ein Hintergrundbild hinzufügen, ein Bild darüberlegen und eine Textebene darüber platzieren?

Der Drag-and-Drop-Editor unterstützt derzeit zwei Ebenen. Sie können ein Zeilen-Hintergrundbild festlegen und Hintergrundfarben anpassen.

### Kann ich meine Drag-and-Drop-E-Mail als Template speichern, nachdem ich sie in meiner Kampagne oder meinem Canvas erstellt habe?

Nein, Sie müssen die E-Mail unter **E-Mail-Templates** neu erstellen, um sie zu speichern.

### Kann ich E-Mail-Anhänge zum Drag-and-Drop-Editor hinzufügen?

Nein, der Drag-and-Drop-Editor unterstützt das Hinzufügen von Anhängen zu Ihren E-Mails nicht.