---
nav_title: FAQ
article_title: FAQ zum Drag-and-Drop-Editor
alias: "/dnd/faq/"
channel: email
page_order: 5
description: "Häufig gestellte Fragen zum Drag-and-Drop-E-Mail-Editor."
tool:
  - Campaigns
  - Canvas



---

# Häufig gestellte Fragen {#frequently-asked-questions}

> Diese Seite bietet Antworten auf einige häufig gestellte Fragen zum Drag-and-Drop-Editor für E-Mail.

## Kann ich eine Vorschau meiner E-Mail im Dark Mode anzeigen? {#can-i-preview-how-my-email-appears-in-dark-mode}

Ja. Gehen Sie zum Abschnitt **Vorschau und Test** des Drag-and-Drop-Editors und aktivieren Sie den **Dark Mode**. Wir empfehlen außerdem, Ihre E-Mails auf verschiedenen Nutzerplattformen in der Vorschau anzuzeigen und zu testen sowie nach Möglichkeit transparente Bilder für Zeilen-Hintergrundbilder zu verwenden.

## Wie sollte ich E-Mails für den Dark Mode und den Light Mode gestalten? {#how-should-i-design-emails-for-dark-mode-and-light-mode}

E-Mails müssen nicht in separaten Light- und Dark-Layouts versendet werden, da E-Mail-Clients und Geräte ihr eigenes dunkles Theme anwenden können. Allerdings kann dies dazu führen, dass Farben invertiert oder Hintergründe ausgeblendet werden, wenn auf dem äußeren Container und den Hauptbereichen keine expliziten Farben gesetzt sind. Um dies zu vermeiden, empfehlen wir, feste Hintergrundfarben zu setzen, damit Ihre Nachricht sowohl im Dark Mode als auch im Light Mode gut lesbar ist.

Einige E-Mail-Clients ersetzen Hintergrundbilder oder invertieren kontrastarmen Text im Dark Mode, sodass Fließtext fehlen oder zwischen verschiedenen Clients unterschiedlich dargestellt werden kann (zum Beispiel Gmail auf iOS im Vergleich zu Android). Setzen Sie `background-color` auf den äußeren Container und die Hauptbereiche, anstatt sich für helle Hintergründe ausschließlich auf Hintergrundbilder zu verlassen.

## Warum wird meine benutzerdefinierte Schriftart in der Drag-and-Drop-E-Mail-Vorschau nicht angezeigt? {#why-doesnt-my-custom-font-appear-in-drag-and-drop-email-preview}

Benutzerdefinierte Schriftarten werden in der Editor-Vorschau geladen, wenn ein **Text**-Block in der Nachricht auf die Schriftart verweist. Falls die Vorschau nach der Konfiguration einer benutzerdefinierten Schriftart in den Einstellungen des **Drag-and-Drop-E-Mail-Editors** weiterhin eine Fallback-Schriftart anzeigt, fügen Sie einen **Text**-Block hinzu, der diese Schriftart verwendet, damit der Editor sie für die Vorschau lädt. Stellen Sie sicher, dass Cross-Origin Resource Sharing (CORS) für Ihre Schriftdatei aktiviert ist. Überprüfen Sie **Vorschau und Test** sowie Ihre Ziel-E-Mail-Clients, bevor Sie senden. Informationen zur Einrichtung finden Sie unter [Benutzerdefinierte Schriftart]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings#custom-font).

## Wie kann ich Textformatierungen beim Kopieren und Einfügen aus einer anderen Anwendung übernehmen? {#how-can-i-carry-over-text-formatting-when-i-copy-and-paste-from-another-application}

Verschiedene Texteditoren und Anwendungen haben ihre eigenen Methoden zur Handhabung von Textformatierungen, die möglicherweise nicht universell erkannt werden. Wenn Sie formatierten Text von außerhalb von Braze in den Drag-and-Drop-Editor kopieren und einfügen, wird die Rich-Formatierung möglicherweise nicht übernommen.

Um Text ohne Rich-Formatierung einzufügen, verwenden Sie eine der folgenden Methoden:
- Auf dem Mac: Drücken Sie <kbd>cmd</kbd>+<kbd>shift</kbd>+<kbd>V</kbd> anstelle von <kbd>cmd</kbd>+<kbd>V</kbd>
- Unter Windows: Drücken Sie <kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>V</kbd> anstelle von <kbd>ctrl</kbd>+<kbd>V</kbd>
- Klicken Sie mit der rechten Maustaste im Editor und wählen Sie **Einfügen und Stil anpassen** aus

## Wie kann ich den E-Mail-Padding auf Mobilgeräten ändern, ohne das Padding in der Web-Ansicht zu aktualisieren? {#how-can-i-change-the-email-padding-on-mobile-without-updating-the-padding-in-the-web-view}

Sie können das Padding nicht ausschließlich für die mobile oder die Web-Ansicht bearbeiten, sodass alle Änderungen in beiden Ansichten übernommen werden. Sie können jedoch im HTML-Editor CSS-Logik hinzufügen, die das Padding basierend auf verschiedenen Bildschirmgrößen festlegt. Dies wird im Drag-and-Drop-Editor nicht unterstützt, sodass Sie die HTML-Datei exportieren und stattdessen den HTML-Editor verwenden können.

## Wie kann ich eine Reihe von Buttons optimieren, damit sie auf Desktop und Mobilgeräten horizontal bleiben? {#how-can-i-optimize-a-row-of-buttons-to-remain-horizontal-on-desktop-and-mobile}

Wenn Sie eine E-Mail mit dem Drag-and-Drop-Editor erstellen und eine horizontale Reihe von Call-to-Action-Buttons anlegen, kann es vorkommen, dass die Buttons auf Mobilgeräten in eine vertikale Ausrichtung umgewandelt werden.

Um dasselbe Format über verschiedene Gerätegrößen hinweg beizubehalten, empfehlen wir, eine separate Zeile mit CTA-Buttons zu erstellen, deren Padding für Mobilgeräte optimiert ist und bei der die Zeile auf Desktop-Geräten ausgeblendet wird. Durch zwei separate Zeilen können Sie das gewünschte Padding für die beste Textdarstellung auf Desktop- und Mobilgeräten festlegen.

## Kann ich die Zeilenhöhe im Drag-and-drop-Editor anpassen? {#can-i-adjust-the-row-height-in-the-drag-and-drop-editor}

Die Zeilenhöhe passt sich automatisch an den Inhalt an. Alternativ empfehlen wir Ihnen Folgendes:
1. Fügen Sie einen Trennlinien-Block hinzu.
2. Klicken Sie auf den Schalter, um die Transparenz zu aktivieren.
3. Passen Sie die Höhe an.

## Ist es möglich, im Editor mit Ebenen zu arbeiten? Kann ich ein Hintergrundbild hinzufügen, ein Bild darüber legen und darüber eine Textebene platzieren? {#is-it-possible-to-build-layers-in-the-editor-can-i-add-a-background-image-layer-on-an-image-and-add-a-text-layer-over-that}

Der Drag-and-Drop-Editor unterstützt derzeit zwei Ebenen. Sie können ein Hintergrundbild für eine Zeile festlegen und Hintergrundfarben anpassen.

## Kann ich meine Drag-and-Drop-E-Mail als Template speichern, nachdem ich sie in meiner Campaign oder meinem Canvas erstellt habe? {#can-i-save-my-drag-and-drop-email-as-a-template-after-i-build-it-within-my-campaign-or-canvas}

Nein. Sie können eine Drag-and-Drop-E-Mail aus einer Campaign oder einem Canvas nicht als Drag-and-Drop-**E-Mail-Template** unter **Templates** > **E-Mail-Templates** speichern. Erstellen Sie das Layout unter **Templates** > **E-Mail-Templates** neu, oder starten Sie beim nächsten Mal mit einem gespeicherten Template. Eine Anleitung finden Sie unter [E-Mail-Template erstellen]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template).

Wenn Sie stattdessen ein wiederverwendbares HTML-Template benötigen, wählen Sie beim Bearbeiten des Drag-and-Drop-Inhalts **Datei herunterladen** aus, öffnen Sie die HTML-Datei aus der ZIP-Datei und fügen Sie das Markup über den HTML-Code-Editor in ein [HTML-E-Mail-Template]({{site.baseurl}}/user_guide/messaging/templates/email_templates/html_email_template) ein. Überprüfen Sie anschließend Liquid, Links und gehostete Assets.

Weitere Informationen darüber, wo Templates zu finden sind, finden Sie unter [Templates und Medien]({{site.baseurl}}/user_guide/messaging/templates).

## Warum kann ich die Füllfarbe eines Buttons im Drag-and-Drop-Editor nicht ändern? {#why-cant-i-change-a-buttons-fill-color-in-the-drag-and-drop-editor}

Stile auf Seitenebene können Stile auf Nachrichtenebene überschreiben. Wenn das Aktualisieren von **Füllung** bei einem Button oder Block keine Wirkung zeigt, versuchen Sie Folgendes:
1. Öffnen Sie die [globalen E-Mail-Stileinstellungen]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings) und wählen Sie **Auf Standard zurücksetzen** für den betreffenden Seitenstil aus, damit die Farbe auf Nachrichtenebene angewendet werden kann.
2. Legen Sie die Farbe erneut für den Block fest.

## Kann ich E-Mail-Anhänge im Drag-and-Drop-Editor hinzufügen? {#can-i-add-email-attachments-to-the-drag-and-drop-editor}

Ja. Sie können Anhänge zu Ihrer E-Mail-Nachricht hinzufügen, indem Sie zu **Sendeeinstellungen** > **Erweitert** gehen.

## Wie lade ich das Roh-HTML für eine Drag-and-Drop-E-Mail herunter? {#how-do-i-download-the-raw-html-for-a-drag-and-drop-email}

Der Drag-and-Drop-Editor bietet die Option **Datei herunterladen**, um Ihre E-Mail als HTML-Datei in einer ZIP-Datei zu exportieren.

1. Öffnen Sie Ihre Campaign oder Ihr Canvas und bearbeiten Sie die E-Mail-Nachricht.
2. Wählen Sie **E-Mail-Text bearbeiten** aus, um den Drag-and-Drop-Editor zu öffnen.
3. Wählen Sie **Datei herunterladen** aus.
4. Entpacken Sie das Archiv, um auf das generierte HTML zuzugreifen.

{% alert tip %}
Verschieben Sie unter Windows die ZIP-Datei an einen dauerhaften Speicherort (z. B. Downloads), bevor Sie sie entpacken. Das Entpacken aus einem temporären Ordner kann dazu führen, dass Sie nach dem Löschen dieses Ordners nicht mehr auf die HTML-Datei zugreifen können.
{% endalert %}

Sie können dieses HTML in einen [HTML-Block]({{site.baseurl}}/user_guide/channels/email/drag_and_drop#content) oder den HTML-Editor einfügen, wenn Sie Änderungen auf Code-Ebene vornehmen möchten (zum Beispiel, um das [Klick-Tracking für bestimmte Links zu deaktivieren]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links#turning-off-click-tracking-on-a-link-to-link-basis)).

## Warum bricht mein Drag-and-Drop-Layout? {#why-is-my-drag-and-drop-layout-breaking}

Layoutprobleme werden häufig durch **angepasstes HTML oder CSS** verursacht, das mit dem vom Editor generierten Markup in Konflikt steht. Versuchen Sie die folgenden Schritte:

1. Entfernen oder isolieren Sie angepasste HTML-Blöcke, um zu sehen, ob das Problem verschwindet.
2. Überprüfen Sie die Einstellungen des **Drag-and-Drop-E-Mail-Editors** auf angepasste Schriftarten, die möglicherweise nicht in allen Clients geladen werden.
3. Überprüfen Sie unter **Row Properties** das Padding und die Breiten der Spalten.
4. Wenn Sie angepasstes HTML hinzufügen, bevorzugen Sie tabellenbasierte Layouts, flexible Bilder und Gesamttabellenbreiten, die zu Ihrer E-Mail-Breite passen – Bilder mit festen Pixelwerten oder Strukturen ohne Tabellen brechen häufig in Outlook und anderen Clients.

## Warum wird mein Content-Block in der E-Mail-Vorschau nicht gerendert? {#why-doesnt-my-content-block-render-in-email-preview}

Wenn ein Content-Block in der E-Mail-Vorschau nicht gerendert wird, prüfen Sie, ob nicht geschlossene Anchor-Tags vorhanden sind. Verwenden Sie für Connected-Content-URLs den `replace`-Filter, um doppelt kodierte Ampersands (`&amp;amp;`) in ein einfach kodiertes Ampersand (`&amp;`) umzuwandeln. Begrenzen Sie die Verschachtelung von Content Blocks auf zwei Ebenen.

## Warum verliert ein Drag-and-Drop-Content-Block die mobile Formatierung innerhalb eines Custom-Code-Blocks? {#why-does-a-drag-and-drop-content-block-lose-mobile-styling-inside-a-custom-code-block}

Wenn Sie einen Drag-and-Drop-**Content Block** in einen **Custom-Code**-Block (HTML) einfügen, werden mobilspezifische Formatierungen und Ausrichtungen aus dem Content Block möglicherweise nicht in der gesendeten Nachricht angewendet. Wenn sowohl der Content Block als auch das Template den Drag-and-Drop-Editor verwenden, fügen Sie den Content Block als eigene Zeile hinzu, anstatt ihn in Custom Code zu verschachteln.

Wenn Sie mehrere Content Blocks übereinander anordnen, verwenden Sie für jeden Block eine separate Zeile, anstatt mehrere Blöcke in einer einzelnen Zeile zu platzieren.

## Warum ignoriert der Drag-and-Drop-Editor die Ausrichtungseinstellungen? {#why-is-the-drag-and-drop-editor-ignoring-alignment-settings}

Wenn der Drag-and-Drop-Editor die Ausrichtungseinstellungen ignoriert, entfernen Sie benutzerdefiniertes CSS oder HTML-Blöcke, entfernen Sie benutzerdefinierte Schriftarten, prüfen Sie auf CSS-Konflikte und vermeiden Sie das Duplizieren von Zeilenblöcken. Kontaktieren Sie den Braze-Support, wenn das Problem weiterhin besteht.

## Warum stimmt mein gewählter Hex-Farbcode nicht mit der Schriftfarbe in meiner E-Mail überein? {#why-does-my-chosen-hex-color-code-not-match-the-font-in-my-email}

Wenn Sie einen Content Block verwenden, kann dieser eine eigene Schriftfarbeneinstellung haben. Wählen Sie den Textblock innerhalb des Content Blocks aus und entfernen Sie alle lokalen Überschreibungen der **Schriftfarbe**, damit Ihr Hex-Farbcode aus der globalen oder Absatzformatierung angewendet werden kann.