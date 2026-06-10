---
nav_title: Stileinstellungen
article_title: "Stileinstellungen für In-App-Nachrichten"
description: "Dieser Referenzartikel behandelt die Stiloptionen, die beim Erstellen einer In-App-Nachricht mit dem Drag-and-Drop-Editor verfügbar sind."
page_order: 1
---

# Stileinstellungen für In-App-Nachrichten {#in-app-message-style-settings}

> Die Drag-and-Drop-Bearbeitungserfahrung ist in zwei Bereiche unterteilt: **Build** und **Preview & Test**. Dieser Artikel behandelt, was Sie für die Arbeit im Tab **Build** des Editors wissen müssen, und setzt voraus, dass Sie bereits [eine In-App-Nachricht erstellt]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/) haben.

![Tab „Message Styles“.]({% image_buster /assets/img_archive/dnd_iam_message_styles.png %}){: style="float:right;max-width:25%;margin-left:15px;max-width:30%"}

## Stile auf Nachrichtenebene {#message-level-styles}

Sie können bestimmte Stile festlegen, die auf alle relevanten Blöcke in Ihrer In-App-Nachricht angewendet werden, und zwar über den Tab **Message Styles**. Beispielsweise möchten Sie vielleicht die Schriftart des gesamten Textes oder die Farbe aller Links in Ihrer Nachricht anpassen.

Die Stile in diesem Abschnitt werden überall in Ihrer Nachricht verwendet, es sei denn, Sie überschreiben sie für einen bestimmten Block. Wenn Ihre Nachricht [mehrere Seiten]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/#multi-page) hat, können Sie die Stile auf Nachrichtenebene auch für einzelne Seiten überschreiben, mit Ausnahme des Anzeigetyps und der maximalen Breite.

Für ein einfacheres Design-Erlebnis empfehlen wir, zuerst die Stile auf Nachrichtenebene einzurichten, bevor Sie Stile auf Blockebene anpassen.

Um jederzeit zum Tab **Message Styles** zurückzukehren:

- Klicken Sie auf die Schließen-X-Schaltfläche bei den einzelnen Blockeigenschaften
- Wählen Sie den Nachrichtencontainer, die Schließen-X-Schaltfläche der Nachricht oder den Editor-Hintergrund aus

### Benutzerdefinierte Schriftarten {#custom-fonts}

Wir akzeptieren die folgenden Dateitypen für Schriftarten: `.ttf`, `.woff`, `.otf` und `.woff2`. Weitere Informationen finden Sie unter [Asset-Dateien]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html/#asset-files).

Sie können mehrere Varianten einer Schriftfamilie hinzufügen, da einige Stiloptionen für benutzerdefinierte Schriftarten möglicherweise nicht verfügbar sind. Derzeit unterstützen wir das Hinzufügen von Schriftarten über URL nicht.

So fügen Sie eine benutzerdefinierte Schriftart hinzu:

1. Gehen Sie zum Abschnitt **Content** im Tab **Message styles**.
2. Klicken Sie auf **Add custom font**.
3. Laden Sie Ihre Schriftart über die Medienbibliothek hoch.

{% alert note %}
Die Schriftart auf Nachrichtenebene gilt nur für die aktuelle Nachricht und alle duplizierten Nachrichten, nicht jedoch für zukünftige Templates.
{% endalert %}

## Nachrichtenkomponenten {#message-components}

![Ein GIF, das die Erstellung einer werblichen In-App-Nachricht zeigt.]({% image_buster /assets/img_archive/dnd_iam_create.gif %})

Der Drag-and-Drop-Editor verwendet zwei Schlüsselkomponenten zum Erstellen von In-App-Nachrichten: **Zeilen** und **Blöcke**. Alle Blöcke müssen in einer Zeile platziert werden.

### Schließen-X-Button {#close-x-button}

Für modale und Vollbild-In-App-Nachrichten können Sie den Schließen-Button anpassen, der als <i class="fa-solid fa-xmark"></i> in der oberen rechten Ecke Ihrer Nachricht angezeigt wird. Zu den Anpassungsoptionen gehören Button-Position, Größe, Füllfarbe, Hintergrundfarbe, Rahmenstil und Rahmenradius.

![Optionen zur Anpassung des Schließen-X-Buttons in In-App-Nachrichten, einschließlich Button-Größe, Füllfarbe, Hintergrundfarbe, Rahmenstil und Rahmenradius.]({% image_buster /assets/img_archive/close_x_button.png %}){: style="max-width:40%"}

### Span-Styling {#span-styling}

Das Hinzufügen von Span-Styling zu Text innerhalb von In-App-Nachrichten ermöglicht eine erweiterte Anpassung des Nachrichtenerscheinungsbilds und erlaubt die Verwendung verschiedener Textfarben, Schriftarten und Größen. Span-Styling bietet Ihren Nutzer:innen ein ansprechenderes und visuell attraktiveres Erlebnis, indem es die Aufmerksamkeit auf wichtige Informationen lenkt und die allgemeine Klarheit der Nachricht verbessert.

![Option, die beim Hervorheben von Text in einer In-App-Nachricht angezeigt wird. Ein kleines Pinselsymbol zeigt, dass Sie den Text mit Span für Styling umschließen können.]({% image_buster /assets/img_archive/span_1.png %}){: style="max-width:40%"}

![Seitenpanel für „Span Properties“, das es ermöglicht, Schriftfamilie, Schriftstärke, Schriftgröße, Zeichenabstand und Textfarbe anzupassen.]({% image_buster /assets/img_archive/span_2.png %}){: style="max-width:40%"}

### Zeilen {#rows}

Zeilen sind strukturelle Einheiten, die die horizontale Zusammensetzung eines Abschnitts der Nachricht mithilfe von Zellen definieren.

![Zeilen, die Sie in Ihrer In-App-Nachricht hinzufügen können.]({% image_buster /assets/img_archive/dnd_iam_rows.png %}){: style="max-width:40%"}

Wenn eine Zeile ausgewählt ist, können Sie im Abschnitt **Column customization** die Anzahl der benötigten Spalten hinzufügen oder entfernen, um verschiedene Inhaltselemente nebeneinander zu platzieren.

Sie können auch die Größe vorhandener Spalten durch Verschieben anpassen.

![Anpassen von Spalten im Abschnitt „Column customization“.]({% image_buster /assets/img_archive/dnd_iam_column_customization.gif %}){: style="max-width:40%"}

Als Best Practice empfehlen wir, Ihre Zeilen- und Spalteneigenschaften zu formatieren, bevor Sie die Blöcke innerhalb der Zeilen formatieren. Es gibt viele Stellen, an denen Sie Abstände und Ausrichtung anpassen können, daher erleichtert es das Bearbeiten, wenn Sie von der Grundlage aus beginnen.

#### Hintergrundbild {#background-image}

Sie können ein Hintergrundbild zu einer Zeile im Panel **Row properties** hinzufügen. Aktivieren Sie **Background image** und geben Sie dann eine Bild-URL an oder wählen Sie ein Bild aus der [Medienbibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/) aus. Konfigurieren Sie abschließend Ihren Alternativtext, die Größe, die Position und ob das Bild wiederholt werden soll, um Muster über die Zeile hinweg zu erstellen.

![Ein Zeilen-Hintergrundbild einer Pizza mit einem horizontalen Wiederholungsmuster.]({% image_buster /assets/img_archive/background_row.png %})

### Blöcke {#blocks}

Blöcke repräsentieren verschiedene Inhaltstypen, die Sie in Ihrer Nachricht verwenden können. Ziehen Sie einen in ein vorhandenes Zeilensegment, und er passt sich automatisch an die Zellenbreite an.

{% alert tip %}
Bevor Sie Blöcke hinzufügen, richten Sie [Stile auf Nachrichtenebene](#set-message-level-styles) für den Nachrichtencontainer, die Schriftart, Farben und alles andere ein, was Sie anpassen möchten. Sie können dann einzelne Blöcke nach Bedarf anpassen. Der **Schließen-Button** bleibt im oberen Bereich Ihrer Nachricht, damit Nutzer:innen immer die Möglichkeit haben, die Nachricht zu schließen.
{% endalert %}

![Drag-and-Drop-Boxen zur Auswahl.]({% image_buster /assets/img_archive/dnd_iam_editor_blocks.png %}){: style="max-width:40%"}

Jeder Block hat seine eigenen Einstellungen, wie z. B. eine granulare Steuerung des Paddings. Das rechte Panel wechselt automatisch zu einem Styling-Panel für das ausgewählte Inhaltselement. Weitere Informationen finden Sie unter [Editor-Block-Eigenschaften]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages#inappmessages_properties).

Während Sie Ihre In-App-Nachricht erstellen, können Sie in der Symbolleiste eine Mobilgeräte-, Tablet- oder Desktop-Ansicht auswählen, um eine Vorschau zu sehen, wie Ihre In-App-Nachricht für Ihre Nutzergruppen aussehen wird. So stellen Sie sicher, dass Ihr Inhalt responsiv ist, und Sie können unterwegs alle notwendigen Anpassungen vornehmen.

## Kreative Details {#creative-details}

### Vollbild auf größeren Bildschirmen {#fullscreen}

Auf einem Tablet oder Desktop-Browser wird eine Vollbild-In-App-Nachricht in der Mitte des App-Bildschirms angezeigt. Alle Änderungen an der maximalen Breite der Vollbildnachricht gelten nur für Tablet- und Desktop-Geräte.

![Beispiel einer Vollbild-In-App-Nachricht.]({% image_buster /assets/img_archive/dnd_iam_fullscreen_example.png %}){: style="border:none"}

### Hintergrundbild hinzufügen {#adding-a-background-image}

Sie können ein Bild zum Hintergrund Ihrer Nachricht über den Tab **Message styles** hinzufügen.

1. Wählen Sie im Canvas-Bereich den Hintergrundcontainer aus. Dies ist der scrollbare Bereich Ihrer Nachricht.
2. Aktivieren Sie im Tab **Message styles** die Option **Background image**.
3. Fügen Sie ein Bild aus Ihrer Medienbibliothek hinzu oder geben Sie die URL ein, unter der Ihr Bild gehostet wird.

{% alert tip %}
Wenn Sie Schwierigkeiten haben, einen bestimmten Block auszuwählen, können Sie den Aufwärtspfeil in der Inline-Symbolleiste des Blocks verwenden, um den Fokus auf den jeweils übergeordneten Block zu verschieben.
{% endalert %}

### Liquid hinzufügen {#adding-liquid}

![Symbol zum Hinzufügen von Liquid-Personalisierung.]({% image_buster /assets/img_archive/dnd_iam_liquid.png %}){: style="float:right;max-width:25%;margin-left:15px"}

Um [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/) zu Ihrer In-App-Nachricht hinzuzufügen, wählen Sie <i class="fa-solid fa-circle-plus"></i> **Add Personalization** in der Editor-Symbolleiste. Hier können Sie verschiedene Personalisierungstypen hinzufügen, wie z. B. Standardattribute, Geräteattribute, angepasste Attribute und mehr.

Nehmen Sie als Nächstes Ihr generiertes Liquid-Snippet und fügen Sie es in Ihre Nachricht ein. Nachdem Sie Ihre In-App-Nachricht entworfen und erstellt haben, gehen Sie zu **Preview & Test**, um eine Vorschau Ihrer Nachricht anzuzeigen.

### Den KI-Texter verwenden {#using-the-ai-copywriter}

Wenn ein Textblock in Ihrer In-App-Nachricht ausgewählt ist, klicken Sie auf <i class="fa-solid fa-wand-magic-sparkles" title="KI-Texter"></i> in der Block-Symbolleiste, um den [KI-gestützten Textassistenten]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/) zu starten. Der KI-Textassistent übergibt einen kurzen Produktnamen oder eine Beschreibung an das GPT3-Textgenerierungstool von OpenAI, um menschenähnliche Marketingtexte für Ihre Nachrichten zu generieren.

{% alert tip %}
Sie können sich einige Klicks sparen, indem Sie Text innerhalb des Blocks markieren, bevor Sie auf das Symbol klicken. Der markierte Text wird dem Tool hinzugefügt, und der Text wird sofort generiert.
{% endalert %}

![GIF des KI-Texters.]({% image_buster /assets/img_archive/dnd_iam_ai_copywriter.gif %})

### Stile auf Standard zurücksetzen {#resetting-styles-to-default}

Eigenschaften, die Sie gegenüber dem Standardstil geändert haben, sind mit einem orangefarbenen Punkt markiert. Um eine bestimmte Eigenschaft auf ihren Standardstil zurückzusetzen, bewegen Sie den Mauszeiger über das Feld und wählen Sie **Reset to default**.

![Orangefarbener Punkt, der eine Textgröße auf ihre Standardgröße zurücksetzt.]({% image_buster /assets/img_archive/dnd_iam_reset_styles.gif %}){: style="max-width:45%"}

Sie können auch alle Stile für ein ausgewähltes Element zurücksetzen, indem Sie <i class="fas fa-paintbrush" title="Stile kopieren oder einfügen"></i> neben dem Namen des Eigenschaftenpanels auswählen und **Reset to default styles** wählen.

### Stile kopieren und einfügen {#copying-and-pasting-styles}

Nachdem Sie Änderungen am Stil eines Elements vorgenommen haben, können Sie diese Stile kopieren und auf ein anderes Element einfügen. Beim Einfügen von Stilen werden nur die für dieses Element relevanten Eigenschaften angewendet.

![Dropdown-Menü mit der Option zum Kopieren von Stilen.]({% image_buster /assets/img_archive/dnd_iam_copypaste_styles.png %}){: style="float:right;margin-left:15px;max-width:35%"}

1. Wählen Sie bei ausgewähltem Element <i class="fas fa-paintbrush" title="Stile kopieren oder einfügen"></i> neben dem Namen des Eigenschaftenpanels aus (wenn Sie beispielsweise einen Button ausgewählt haben, neben „Button properties“).
2. Klicken Sie auf **Copy styles** und wählen Sie das Element aus, auf das Sie den kopierten Stil anwenden möchten.
3. Wählen Sie erneut <i class="fas fa-paintbrush" title="Stile kopieren oder einfügen"></i> und wählen Sie **Paste styles**.

#### Tastaturkürzel {#keyboard-shortcuts}

Sie können auch Tastaturkürzel verwenden, um Stile zu kopieren und einzufügen:

| Aktion | Mac | Windows |
| ------------ | ---------------------------------------------- | ------------------------------------------------- |
| Stile kopieren | <kbd>⌘</kbd> + <kbd>Shift</kbd> + <kbd>c</kbd> | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>c</kbd> |
| Stile einfügen | <kbd>⌘</kbd> + <kbd>Shift</kbd> + <kbd>v</kbd> | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>v</kbd> |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tastaturkürzel" }