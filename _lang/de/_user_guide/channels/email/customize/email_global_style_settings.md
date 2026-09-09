---
nav_title: "Globale E-Mail-Stileinstellungen"
article_title: "Globale E-Mail-Stileinstellungen"
alias: "/dnd/global_style_settings/"
channel: email
page_order: 3
description: "Dieser Referenzartikel beschreibt, wie Sie globale E-Mail-Stileinstellungen im Drag-and-Drop-Editor für Ihre Campaigns und Canvases festlegen."
tool:
  - Campaigns
  - Canvas
---

# Globale E-Mail-Stileinstellungen {#email-global-style-settings}

> Mit globalen Stileinstellungen können Sie das Erscheinungsbild Ihrer E-Mail-Campaigns und Canvases personalisieren. Sie können ein Standard-Theme für Ihren Drag-and-Drop-Editor hinzufügen und anpassen. Dazu gehört die Bearbeitung Ihrer Stile für E-Mail-Titel, Text, Buttons und mehr. Eine Kombination dieser Einstellungen kann dazu beitragen, ein einheitliches Erscheinungsbild in Ihrem E-Mail-Messaging zu schaffen.

Um Ihre globalen Stileinstellungen zu bearbeiten, gehen Sie zu **Einstellungen** > **E-Mail-Präferenzen** > **Drag-and-Drop-E-Mail-Präferenzen**. Nachdem Sie die Stile im Drag-and-Drop-E-Mail-Editor bearbeitet haben, wählen Sie **Speichern**. Um Ihre E-Mail-Campaigns und Canvases weiter anzupassen, erfahren Sie, wie Sie [Editor-Blöcke (E-Mail)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=email) einbinden können.

![Abschnitt „Globale E-Mail-Stileinstellungen“ im Tab „Drag-and-Drop-E-Mail-Editor-Einstellungen“.]({% image_buster /assets/img_archive/dnd_global_style_settings.png %})

{% alert note %}
Änderungen an den globalen Stileinstellungen werden auf alle zukünftigen E-Mail-Campaigns und Canvases angewendet.
{% endalert %}

## Grundlegende Gestaltung {#basic-styling}

Unter **Basic Styling** können Sie die Standard-Hintergrundfarben für E-Mail und Inhalt Ihrer E-Mail-Campaigns und Canvases festlegen. Sie können außerdem eine Standardschriftart auswählen, eine benutzerdefinierte Schriftart hinzufügen und Linkfarben bearbeiten.

![Optionen für die grundlegende Gestaltung, einschließlich Optionen zum Bearbeiten der E-Mail- und Inhalts-Hintergrundfarben, des Standard-Schriftartnamens und der Standard-Linkfarbe.]({% image_buster /assets/img_archive/dnd_basic_styling.png %})

## Benutzerdefinierte Schriftart {#custom-font}

Mit benutzerdefinierten Schriftarten können Sie manuell eine Webschriftart hinzufügen, um die Markenkonsistenz über verschiedene E-Mail-Plattformen hinweg sicherzustellen. Sie können für jeden Gestaltungsbereich eine benutzerdefinierte Schriftart hinzufügen.

{% alert note %}
Alle Font-Weight-Einstellungen im CSS werden ignoriert. Wählen Sie stattdessen beim Verfassen der Nachricht eine der voreingestellten Schriftstärken aus.
{% endalert %}

### Voraussetzungen {#requirements}

Bevor Sie eine benutzerdefinierte Schriftart hinzufügen, stellen Sie sicher, dass die Datei der benutzerdefinierten Schriftart die folgenden Voraussetzungen erfüllt:

- CORS muss auf dem Server aktiviert sein, der die benutzerdefinierte Schriftartdatei bereitstellt. Dies wird in der Regel von Ihrem IT-Team verwaltet.
  - Die benutzerdefinierte Schriftartdatei muss den Header enthalten: `Access-Control-Allow-Origin: *`
- Die Datei-URL muss auf eine CSS-Datei verweisen (nicht WOFF oder OTF).
- Der Name der benutzerdefinierten Schriftart muss mit dem Namen der Font Face in der CSS-Datei übereinstimmen.

{% alert important %}
Der Anbieter der benutzerdefinierten Schriftart kann personenbezogene Daten Ihrer Empfänger:innen erfassen. Sie sollten die Richtlinien Ihres Schriftartanbieters vor der Verwendung prüfen.
{% endalert %}

### Eine benutzerdefinierte Schriftart hinzufügen {#adding-a-custom-font}

Um eine benutzerdefinierte Schriftart hinzuzufügen, gehen Sie wie folgt vor:

1. Wählen Sie im Abschnitt **Default Font Name** unter **Basic Styling** die Option **Add a custom font** aus.
2. Geben Sie im Feld **Font Name** denselben Schriftartnamen ein, der in Ihrer benutzerdefinierten Schriftartquelldatei erscheint. Achten Sie darauf, dass dieser Name korrekt großgeschrieben und mit Leerzeichen versehen ist.
3. Geben Sie die entsprechende URL im Feld **Font URL** ein.
4. Überprüfen Sie, ob die Vorschau Ihre benutzerdefinierte Schriftart anzeigt.
5. Wählen Sie **Save**, um die benutzerdefinierte Schriftart als Ihre Standard-E-Mail-Schriftart zu verwenden.

{% alert important %}
Gmail unterstützt keine benutzerdefinierten Schriftarten, sodass Ihre benutzerdefinierte Schriftart möglicherweise als Standard-Systemschriftart angezeigt wird. Überprüfen Sie bei anderen E-Mail-Plattformen, ob Ihre benutzerdefinierte Schriftart vor dem Versand Ihres E-Mail-Messagings korrekt angezeigt wird.
{% endalert %}

Um weitere benutzerdefinierte Schriftarten in Ihren E-Mail-Campaigns zu verwenden, können Sie ein [E-Mail-Template]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template) oder [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) erstellen, die die benutzerdefinierte Schriftart enthalten. Beispielsweise können Sie ein spezielles E-Mail-Template mit festlichen benutzerdefinierten Schriftarten erstellen, die auf Ihr Aktionsthema zugeschnitten sind. Achten Sie darauf, dass Ihre Schriftartwahl weiterhin websicher ist und auf Ihren E-Mail-Plattformen unterstützt wird.

### Fallback-Schriftart {#fallback-font}

Fallback-Schriftarten werden für Titel, Überschriften und Fließtext verwendet, wenn Ihre Standardschriftart vom Posteingangs-Anbieter oder Betriebssystem nicht unterstützt wird. Standardmäßig setzt Braze automatisch Arial als Fallback-Schriftart, wenn die globalen Stileinstellungen gespeichert werden. Sie haben außerdem die Möglichkeit, Serif oder Sans-Serif als Optionen für Ihre Standardschriftfamilie hinzuzufügen.

![Ein Beispiel mit „Arial“ als Fallback-Schriftart und „Sans-serif“ als Schriftfamilie.]({% image_buster /assets/img_archive/dnd_fallbacks.png %})

Sie können bis zu 17 Fallback-Schriftarten hinzufügen. Die zuerst ausgewählte Fallback-Schriftart wird als Erstes versucht. Die Fallback-Schriftart wird nur für neu erstellte Templates, E-Mail-Campaigns und Canvas-Komponenten angewendet. Die Fallback-Schriftart wird nicht automatisch für Nachrichten festgelegt, die vor der Angabe der Fallback-Schriftart erstellt wurden. Wir empfehlen dringend, Fallback-Schriftarten auszuwählen, die Ihrem E-Mail-Messaging ähnlich sind, um die Konsistenz Ihres Brandings zu gewährleisten.

## Stile für Überschriften {#title-styling}

Hier können Sie die Stile Ihrer E-Mail-Überschriften anpassen, indem Sie Schriftgröße, Schriftfarbe und Textausrichtung bearbeiten.

![Einstellungen für Überschriftenstile mit einer zentrierten Hauptüberschrift und einer sekundären Überschrift.]({% image_buster /assets/img_archive/dnd_title_styling.png %})

Optional können Sie den Standardstil Ihres Drag-and-Drop-Editor-Themes überschreiben. Wählen Sie **Override default style** aus, um Ihre gewählten Überschriftenstile anzuwenden. Dies kann das Festlegen einer anderen Schriftart und Linkfarbe umfassen.

## Absatzformatierung {#paragraph-styling}

Um einen Standard-Absatzstil festzulegen, navigieren Sie zu **Paragraph Styling**, geben Sie die **Font Size** ein und wählen Sie **Font Color** aus, um eine Schriftfarbe auszuwählen. Sie können auch die Blockformatierung für den Fließtext anpassen, indem Sie die Werte für **Padding Top**, **Padding Right**, **Padding Bottom** und **Padding Left** bearbeiten. Dies wird auf den Abstand um alle vier Bereiche des Absatzblocks angewendet.

![Einstellungen für die Absatzformatierung mit 14pt-Schrift.]({% image_buster /assets/img_archive/dnd_paragraph_styling.png %})

## Listenstile {#list-styling}

Wenn Sie Listen zu Ihren Nachrichten hinzufügen, sorgt der Bereich **List Styling** für ein einheitliches Erscheinungsbild Ihrer Listen. Dazu gehören Details wie:

- Schriftgröße
- Schriftfarbe
- Schriftstärke
- Zeilenhöhe
- Ausrichtung
- Textrichtung
- Zeichenabstand
- Abstand zwischen Listenelementen
- Einrückung von Listenelementen
- Listentyp
- Listenstiltyp

Sie können den **List Type** auf nummeriert oder mit Aufzählungszeichen festlegen. Der **List Style Type** bietet zusätzliche Anpassungsmöglichkeiten für den Stil Ihrer Listen. Zum Beispiel können Sie festlegen, dass die Listen immer Aufzählungszeichen verwenden und jedes Aufzählungszeichen ein Quadrat ist.

![Einstellungen für Listenstile bei einer Liste mit Aufzählungszeichen.]({% image_buster /assets/img_archive/dnd_list_styling.png %})

## Button-Stil {#button-styling}

Im Abschnitt **Button Styling** können Sie die folgenden Standardstile für den Button bearbeiten:
- Hintergrundfarbe
- Schriftgröße
- Schriftfarbe
- Rahmenradius
- Rahmenfarbe
- Rahmenstärke
- Button-Padding

![Einstellungen für den Button-Stil mit einem rechteckigen Button mit blauem Hintergrund.]({% image_buster /assets/img_archive/dnd_button_styling.png %})

Wie bei allen anderen Stilabschnitten können Sie den Blockstil anpassen, indem Sie die Werte für **Padding Top**, **Padding Right**, **Padding Bottom** und **Padding Left** bearbeiten.

## E-Mail-Template-Breite {#email-template-width}

Mit der E-Mail-Template-Breite können Sie eine Breite anpassen und festlegen, um Konsistenz in all Ihren E-Mail-Campaigns zu gewährleisten.

![E-Mail-Template-Breite auf 600 px eingestellt.]({% image_buster /assets/img_archive/dnd_email_template_width.png %})

## Content-Block-Breite {#content-block-width}

Diese Einstellung wird für alle zukünftigen Content Blocks vorkonfiguriert. Bestehende Content Blocks werden nicht aktualisiert. Sie können alle Content Blocks auf 100 % einstellen, sodass sie sich an die Breite anpassen, in die ein Content Block eingefügt wird, oder einen bestimmten Pixelwert festlegen.

Wir empfehlen, die Breite des Content Blocks an die Breite des E-Mail-Templates anzupassen.

![Content-Block-Breite auf 600 px eingestellt.]({% image_buster /assets/img_archive/dnd_content_block_width_update.png %})