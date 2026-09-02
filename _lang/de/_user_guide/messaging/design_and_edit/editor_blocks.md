---
nav_title: Editor-Blöcke
article_title: Editor-Blöcke im Drag-and-Drop-Editor
alias: "/dnd/editor_blocks/"
channel:
- email
- in-app messages
- landing pages
- banners
- preference center
page_order: 3
page_type: reference
description: "Dieser Referenzartikel behandelt die Editor-Blöcke im Drag-and-Drop-Editor für E-Mail, In-App-Nachrichten, Landing-Pages, Banner und Drag-and-Drop-E-Mail-Präferenzzentren."
tool: Media
---

# Editor-Blöcke im Drag-and-Drop-Editor {#drag-and-drop-editor-blocks}

> Editor-Blöcke sind die Kacheln, die Sie im Drag-and-Drop-Editor in Zeilen und Spalten ziehen.

Wählen Sie den Editor aus, den Sie verwenden:

{% sdktabs %}

{% sdktab email %}
## E-Mail-Editor-Blöcke {#email-editor-blocks}

Editor-Blöcke befinden sich im Bereich **Content** für E-Mail-Nachrichten. Ziehen Sie einen Block in eine Spalte im **Drag-and-Drop-Editor**; er passt sich automatisch an die Spaltenbreite an.

Weitere Informationen zum Erstellen von E-Mails im **Drag-and-Drop-Editor** finden Sie unter [E-Mail per Drag-and-Drop erstellen]({{site.baseurl}}/user_guide/channels/email/drag_and_drop) und <a href="{{site.baseurl}}/user_guide/channels/email/drag_and_drop/#other-customizations">Weitere Anpassungen</a> in diesem Artikel.

{% alert tip %}
Sie können auch [angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types) zu jeder URL innerhalb der Editor-Blöcke `Image`, `Button` oder `Text` hinzufügen.
{% endalert %}

### Titel {#title}

Fügt Text für Überschriften innerhalb der E-Mail hinzu.

| Eigenschaft | Beschreibung |
|---|---|
| Title | Wählt den Überschriftenstil aus. |
| Font family | Der Schriftstil für Ihren Titel. |
| Font weight | Die allgemeine Fettung der Schrift. |
| Font size | Bestimmt die Größe Ihres Textes. |
| Text color | Ändert die Farbe des Titels. |
| Link color | Ändert die Farbe des Links. |
| Align | Verschiebt den Titel nach links, zentriert oder rechts. |
| Line height | Ändert den Abstand zwischen Textzeilen. |
| Letter spacing | Ändert den Abstand zwischen den einzelnen Zeichen. |
| Text direction | Standard ist links nach rechts, kann aber auf [rechts nach links]({{site.baseurl}}/right_to_left_messages) geändert werden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Titel" }

### Absatz {#paragraph}

Gibt Text in die Nachricht ein. Eine Symbolleiste hilft bei der Schrift- und Textbearbeitung.

| Eigenschaft | Beschreibung |
|---|---|
| Font family | Der Schriftstil für Ihren Absatztext. |
| Font weight | Die allgemeine Fettung der Schrift. |
| Font size | Bestimmt die Größe Ihres Textes. |
| Text color | Ändert die Farbe des Textes. |
| Link color | Ändert die Farbe des Links. |
| Align | Verschiebt den Text nach links, zentriert oder rechts. |
| Paragraph spacing | Ändert den Abstand zwischen Absätzen. |
| Line height | Ändert den Abstand zwischen Textzeilen. |
| Letter spacing | Ändert den Abstand zwischen den einzelnen Zeichen. |
| Text direction | Standard ist links nach rechts, kann aber auf [rechts nach links]({{site.baseurl}}/right_to_left_messages) geändert werden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Absatz" }

### Liste {#list}

Fügt eine Aufzählungsliste hinzu.

| Eigenschaft | Beschreibung |
|---|---|
| List type | Der Typ der Liste. Kann entweder Aufzählung oder Nummerierung sein. |
| List style type | Bestimmt den Stil Ihrer Liste. |
| Start list from | Bestimmt die Startnummer für Ihre Liste. |
| Font family | Der Schriftstil für Ihren Absatztext. |
| Font weight | Die allgemeine Fettung der Schrift. |
| Font size | Bestimmt die Größe Ihres Textes. |
| Text color | Ändert die Farbe des Textes. |
| Link color | Ändert die Farbe des Links. |
| Align | Verschiebt den Text nach links, zentriert oder rechts. |
| List items spacing | Ändert den Abstand zwischen Listenelementen. |
| List items indent | Ändert den Einzug der Listenelemente. |
| Line height | Ändert den Abstand zwischen Textzeilen. |
| Letter spacing | Ändert den Abstand zwischen den einzelnen Zeichen. |
| Text direction | Standard ist links nach rechts, kann aber auf [rechts nach links]({{site.baseurl}}/right_to_left_messages) geändert werden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liste" }

### Button {#button}

Fügt einen Standard-Button hinzu. Über die Eigenschaften können Sie das Styling bearbeiten und das Linkverhalten festlegen.

| Eigenschaft | Beschreibung |
|---|---|
| Button options | Legt verschiedene Button-Optionen fest, wie Schrift, Größe, Breite, Farbe und Padding. |
| Button hover | Der Stil des Buttons, wenn Nutzer:innen mit einer Maus oder einem Trackpad darüber fahren. Umfasst die Hintergrundfarbe, Schriftfarbe und Rahmenstile des Buttons. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Button" }

#### Klickverhalten {#on-click-behavior}

| Eigenschaft | Beschreibung |
|---|---|
| Link type | Bestimmt die Aktion beim Klicken auf den Button und legt das entsprechende Protokoll fest. |
| URL | Dynamisch basierend auf dem Linktyp **Open web page**. |
| Mail to, subject, and body | Für den Linktyp **Send email**: Legt die Empfänger-E-Mail-Adresse, den Betreff und den Inhalt fest, die in einem E-Mail-Entwurf vorausgefüllt werden, wenn Nutzer:innen den Button auswählen. |
| Tel | Für die Linktypen **Make call** und **Send SMS**: Legt die Telefonnummer fest, die Nutzer:innen anrufen oder an die sie eine SMS senden, wenn sie den Button auswählen. |
| Message | Für den Linktyp **Send SMS**: Legt den Inhalt fest, der in einem SMS-Entwurf vorausgefüllt wird, wenn Nutzer:innen den Button auswählen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Klickverhalten" }

### Trennlinie {#divider}

Fügt eine durchgezogene, gepunktete oder gestrichelte Linie ein, um beim Abstand zu helfen.

| Eigenschaft | Beschreibung |
|---|---|
| Transparent | Wenn aktiviert, werden die Linien- und Breitenoptionen entfernt. |
| Line | Die verschiedenen Linienformate: gepunktet, gestrichelt oder durchgezogen. Sie können auch die Dicke und Farbe der Trennlinie ändern. |
| Width | Passt die Ausdehnung der Trennlinie in 5er-Schritten an. |
| Align | Verschiebt die Linie nach links, zentriert oder rechts. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Trennlinie" }

### Abstandshalter {#spacer}

Fügt Abstand oder Padding zwischen anderen Blöcken hinzu.

| Eigenschaft | Beschreibung |
|---|---|
| Height | Passt die Höhe des Abstandshalter-Blocks an. Der Standardwert beträgt 60 px. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Abstandshalter" }

### Bild {#image}

Fügt ein Bild aus der [Medienbibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) ein. Für dynamische Bilder (Bilder mit Liquid oder Connected Content) müssen Sie ein Fallback-Bild festlegen, um die automatischen Breiteneinstellungen zu verwenden. Bildspezifikationen finden Sie unter [E-Mail-Bildspezifikationen]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications#email).

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

| Eigenschaft | Beschreibung |
|---|---|
| Auto width | Ändert die Breite des Bildes in Pixeln. |
| Align | Legt die Bildausrichtung innerhalb des Blocks auf links, zentriert oder rechts fest. |
| Image with Liquid | Verwenden Sie [Liquid]({{site.baseurl}}/liquid)-Logik, um dynamisch verschiedene Bilder innerhalb desselben Inhaltsblocks festzulegen. |
| URL | Legen Sie ein Bild über die Adresse fest, unter der es gehostet wird. |
| Alternate text | Eine kurze Beschreibung des Bildes, die Nutzer:innen dieselben Informationen vermittelt, die im Bild gezeigt werden. Unverzichtbar für die Barrierefreiheit mit Screenreadern oder wenn das Bild nicht geladen werden kann. |
| Image with rounded corners | Rendert das Bild mit abgerundeten Ecken. Standardmäßig werden Bilder mit eckigen Ecken gerendert. |
| Action | Löst eine Aktion aus, wenn Nutzer:innen auf das Bild klicken. |
| Block options | Legt das Padding um den Bildblock fest. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Bild" }

{% alert tip %}
Für **Auto width** wählt die automatische Bildgrößenanpassung die beste Größe für das Bild basierend auf einer Kombination aus Bildbreite und verfügbarem Platz im Layout:
- Bilder, die breiter als der verfügbare Platz sind, werden auf 100 % Breite gesetzt und behalten dieses Verhältnis auf Mobilgeräten bei, wobei die gesamte Displaybreite des Geräts genutzt wird.
- Bilder, die kleiner als der verfügbare Platz sind, verwenden die natürliche Größe des Bildes, um Verzerrungseffekte oder unscharfe Bilder zu vermeiden.
{% endalert %}

#### Gmail-Download-Button-Verhalten {#gmail-download-button-behavior}

Gmail fügt automatisch einen Download-Button an Bilder an, denen kein Hyperlink (`href`) zugeordnet ist. Wenn das Seitenverhältnis des Bildes jedoch 299 x 524 px oder kleiner ist, zeigt Gmail den Download-Button nicht an.

Um zu verhindern, dass der Download-Button bei größeren Bildern erscheint, können Sie den „#“-Link-Workaround anwenden:

1. Wählen Sie den **Image**-Block aus.
2. Gehen Sie im Panel **Block Options** zum Abschnitt **Link**.
3. Setzen Sie den **Link type** auf **Open web page**.
4. Geben Sie ein Rautezeichen (`#`) in das **URL**-Eingabefeld ein.

Das Hinzufügen dieses Links verhindert, dass Gmail den Download-Button anzeigt, ohne die Nutzererfahrung zu beeinträchtigen.

### Video {#video}

Erstellt einen Link zu Videoinhalten. Nur YouTube und Vimeo werden unterstützt.

| Eigenschaft | Beschreibung |
|---|---|
| URL | Die URL für das Video. |
| Title | Wird automatisch aus den Video-Metadaten generiert oder kann angepasst werden. |
| Play icon style | Umfasst verschiedene Optionen für den Play-Button oben auf einem Videobild. |
| Play icon color | Option zur Auswahl von **Light** oder **Dark** für den Play-Button. |
| Play icon size | Wählen Sie die Pixelgröße für den Play-Button. Vordefinierter Bereich von 50&nbsp;px bis 80&nbsp;px (in 5-px-Schritten). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Video" }

{% alert tip %}
Videos, die auf Vimeo gehostet werden, funktionieren nur, wenn sie auf öffentlich gesetzt sind. Alle anderen Sicherheitseinstellungen in Vimeo (z. B. „Von Vimeo.com ausblenden“) erzeugen ein anderes Linkformat, das von diesem Content Block nicht unterstützt wird. Diese Arten von Links werden vom Builder verändert, was Braze daran hindert, ein Vorschaubild zu generieren.
{% endalert %}

### Social {#social}

Fügt Social-Media-Plattform-Icons ein. Sie können benutzerdefinierte Bilder für markenspezifische Icons hochladen.

| Eigenschaft | Beschreibung |
|---|---|
| Select icon collection | Legt den Stil Ihrer Icon-Sammlung fest. |
| Configure icon collection | Legt die URL für jedes Social-Icon fest. Enthält den Umschalter **More options** zum Bearbeiten des Titels und Alternativtexts. |
| Align | Verschiebt das Social-Icon nach links, zentriert oder rechts. |
| Icon spacing | Bestimmt den Abstand zwischen den einzelnen Social-Icons. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Social" }

### Icons {#icons}

Fügt ein Icon ein. Sie können benutzerdefinierte Bilder hochladen. Braze verwendet ein übergroßes Platzhalter-Icon, bis Sie ein Bild hochladen.

| Eigenschaft | Beschreibung |
|---|---|
| Font family | Der Schriftstil für Ihren Absatztext. |
| Font weight | Die allgemeine Fettung der Schrift. |
| Font size | Bestimmt die Größe Ihres Textes. |
| Text color | Ändert die Farbe des Titels. |
| Link color | Ändert die Farbe des Links. |
| Align | Verschiebt das Icon nach links, zentriert oder rechts. |
| Letter spacing | Ändert den Abstand zwischen den einzelnen Zeichen. |
| Icon size | Bestimmt die Größe Ihres Icons. |
| Icon spacing | Ändert den Abstand des Icons. |
| Icon padding | Ändert das Padding des Icons. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Icons" }

### HTML

Fügt rohes HTML ein. Empfohlen für [Liquid]({{site.baseurl}}/liquid), wie Connected Content oder bedingte Anweisungen.

| Eigenschaft | Beschreibung |
|---|---|
| HTML | Fügen Sie rohes HTML hinzu oder bearbeiten Sie es, einschließlich [Liquid]({{site.baseurl}}/liquid) für Personalisierung oder bedingte Logik. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="HTML" }

### Menü {#menu}

Erstellt ein flexibles Menü für die Nachricht, die Sie gestalten.

| Eigenschaft | Beschreibung |
|---|---|
| Configure menu items | Fügt ein Menüelement hinzu. |
| Font family | Der Schriftstil für das Menü. |
| Font size | Die Größe Ihres Menüs. |
| Text color | Ändert die Farbe des Menüs. |
| Link color | Ändert die Farbe des Menütexts. |
| Align | Verschiebt das Menü nach links, zentriert oder rechts. |
| Letter spacing | Ändert den Abstand zwischen den einzelnen Zeichen. |
| Layout | Bestimmt das Layout als horizontal oder vertikal. |
| Separator | Fügt Zeichen zwischen den Menüoptionen hinzu. |
| Mobile menu | Enthält Optionen zum Ändern der Icon-Größe, Farbe und des Icon-Typs bei Anzeige auf einem Mobilgerät. |
| Item padding | Ändert das Padding über den **+**- oder **-**-Button oder durch Eingabe einer bestimmten Zahl. |
| All sides | Legt eine einheitliche Padding-Zahl fest, wenn das Elementpadding deaktiviert ist. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Menü" }

### Produkt {#product}

Rendert Produktzeilen aus einem [Produktkatalog]({{site.baseurl}}/user_guide/messaging/design_and_edit/product_blocks), entweder als statische Artikel aus einer Katalogauswahl (bis zu 12) oder als dynamische Produkte, die durch einen [Canvas-E-Commerce-Trigger]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases) gesteuert werden (bis zu 24).

| Eigenschaft | Beschreibung |
| --- | --- |
| Content type | Legt fest, ob Produkte aus einer festen Katalog-**Auswahl** (**Static**, bis zu 12 Produkte) oder aus einem Canvas-E-Commerce-Empfehlungstrigger (**Dynamic**, bis zu 24 Produkte) stammen. **Dynamic** ist nur in Canvas-Nachrichtenschritten verfügbar. |
| Catalog | Wählt aus, welcher Produktkatalog die Produktdaten und Feldzuordnungen liefert. |
| Selection | *(Nur Static)* Wählt aus, welcher gefilterte Satz im Katalog bestimmt, welche Produkte angezeigt werden. |
| Show source details | Schaltet Hilfetext um, der den zugrunde liegenden Katalog oder das Ereignisfeld zeigt, das jedem Produktfeld zugeordnet ist. |
| Variant image | Zeigt oder blendet das Variantenbild für jede Produktkachel ein oder aus. |
| Product title | Zeigt oder blendet den Produkttitel für jede Kachel ein oder aus. |
| Price | Zeigt oder blendet den Produktpreis ein oder aus. |
| Button for product URL | Zeigt oder blendet einen Call-to-Action-Button ein oder aus, der zur Produkt-URL verlinkt. |
| Quantity | *(Dynamic, nur Canvas, wenn der Einstiegstrigger kein Produktansichtsereignis ist)* Zeigt oder blendet die Produktmenge aus dem Trigger-Ereignis ein oder aus. |
| Product orientation | Legt die Bildposition innerhalb jeder Kachel fest: **Image left**, **Image center** oder **Image right**. |
| Alignment | Legt die horizontale Ausrichtung des Inhalts innerhalb jeder Kachel fest. |
| Max products per row | Legt fest, wie viele Produkte pro Zeile angezeigt werden: **1**, **2** oder **3** (**3** ist nur verfügbar, wenn die Ausrichtung **Image center** ist). |
| Product spacing | Legt den Abstand zwischen Produkten fest: **Auto** oder **Custom**. |
| Custom spacing | *(Wenn **Custom** ausgewählt ist)* Legt den Abstand in Pixeln zwischen Produkten fest. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Produkt" }

## Personalisierung {#personalization}

Sie können Ihre E-Mail mithilfe von Liquid oder Connected Content personalisieren.

- **Liquid:** Wählen Sie unter **Content** > **Personalization** ein Attribut aus, kopieren Sie das Snippet und fügen Sie es in einen HTML-Block ein. Einfache Liquid-Snippets funktionieren zwar möglicherweise in Title-, Paragraph- und List-Blöcken, aber die Platzierung von Liquid in diesen Blöcken kann zu unerwartetem Verhalten und Layoutproblemen führen. Um Probleme zu vermeiden, verwenden Sie HTML-Blöcke für jegliche Liquid-Logik. Beachten Sie, dass Liquid in Image-Blöcken oder in Button-URL-Feldern nicht unterstützt wird.
- **[Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content):** Fügen Sie einen **HTML**-Block hinzu und platzieren Sie Ihren {% raw %}`{% connected_content %}`{% endraw %}-Aufruf dort.

{% endsdktab %}

{% sdktab in-app messages %}
## In-App-Nachrichten-Editor-Blöcke {#in-app-message-editor-blocks}

Editor-Blöcke befinden sich im Bereich **Build** für In-App-Nachrichten. Ziehen Sie einen Block in eine Spalte; er passt sich automatisch an die Spaltenbreite an. Wählen Sie einen Block aus, um seine Einstellungen im rechten Seitenpanel zu bearbeiten.

Weitere Informationen zum Erstellen von In-App-Nachrichten im **Drag-and-Drop-Editor** finden Sie unter [In-App-Nachricht per Drag-and-Drop erstellen]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop).

### Titel und Absatz {#title-and-paragraph}

Fügt Titel- oder Absatztext zur Nachricht hinzu.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Button

Fügt einen Standard-Button mit konfigurierbarem Styling, Links und Analytics hinzu.

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### Klickverhalten

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

### Optionsfeld {#radio-button}

Fügt eine Liste von Optionen hinzu, aus denen Nutzer:innen eine auswählen können. Beim Absenden protokolliert das Kundenprofil das zugehörige [angepasste Attribut]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), das ein String sein muss, um gespeichert zu werden. Angepasste Attribute mit anderen Datentypen werden nicht im Kundenprofil gespeichert.

{% multi_lang_include drag_and_drop/editor_block_properties/radio_button_properties.md %}

### Bild

Fügt ein Bild aus der [Medienbibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) ein.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

Bildspezifikationen finden Sie in unseren [In-App-Nachrichten-Bildspezifikationen]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications#in-app-messages).

#### Klickverhalten

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### Link {#link}

Fügt einen Hyperlink ein, auf den Nutzer:innen klicken können, um zu einer bestimmten URL zu navigieren. Kann in Text eingebettet oder eigenständig sein.

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### Klickverhalten

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### Abstandshalter

Fügt Abstand oder Padding zwischen anderen Blöcken hinzu.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Benutzerdefinierter Code {#custom-code}

Fügt benutzerdefiniertes HTML, CSS oder JavaScript für erweiterte Anpassungen ein.

| Eigenschaft | Beschreibung |
| --- | --- |
| Custom code | Ermöglicht das Hinzufügen, Bearbeiten oder Löschen von HTML, CSS und JavaScript für eine In-App-Nachricht. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Benutzerdefinierter Code" }

### Telefonnummernerfassung {#phone-capture}

Fügt ein Formularfeld für Telefonnummern ein. Beim Absenden wird die Nutzer:in für die [SMS]({{site.baseurl}}/sms_rcs_subscription_groups)- oder [WhatsApp-Abo-Gruppe]({{site.baseurl}}/whatsapp_subscription_groups) angemeldet.

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### E-Mail-Erfassung {#email-capture}

Fügt ein Formularfeld für E-Mail-Adressen ein. Beim Absenden wird die E-Mail-Adresse dem Kundenprofil in Braze hinzugefügt.

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### Kurztext {#short-text}

Fügt ein Formularfeld ein, das Standardattribute (wie Vor- und Nachname) oder einen angepassten Attribut-String Ihrer Wahl unterstützt.

{% multi_lang_include drag_and_drop/editor_block_properties/short_text_properties.md %}

### Dropdown {#dropdown}

Fügt ein Dropdown mit einer vordefinierten Liste von Elementen ein, aus denen Nutzer:innen eines auswählen können. Sie können beliebige angepasste Attribut-Strings zur Liste hinzufügen.

{% multi_lang_include drag_and_drop/editor_block_properties/dropdown_properties.md %}

### Kontrollkästchen {#checkbox}

Fügt ein Kontrollkästchen ein. Wenn Nutzer:innen das Kästchen aktivieren, wird das [boolesche angepasste Attribut]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) des Blocks auf `true` gesetzt. Wenn es nicht aktiviert wird, wird das Attribut auf `false` gesetzt.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_properties.md %}

### Kontrollkästchengruppe {#checkbox-group}

Nutzer:innen können aus mehreren Optionen auswählen. Werte werden in einem definierten [Array-angepassten Attribut]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) gesetzt oder hinzugefügt.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_group_properties.md %}

### Langtext {#long-text}

Mehrzeiliges Textfeld für umfrageähnliche Abläufe. Wenn Sie diesen Block nicht sehen, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) oder Ihren Braze-CSM.

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Gespeicherte Zeile {#saved-row}

Fügt eine wiederverwendbare Zeile ein, die Sie zuvor als Drag-and-Drop-Content Block gespeichert haben. Gespeicherte Zeilen sind **nicht verknüpft** mit dem ursprünglichen Content Block — wenn das Original aktualisiert wird, müssen Sie es erneut in den Editor ziehen, um die neueste Version zu erhalten. Weitere Informationen finden Sie unter [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks). Wenn Sie **Saved row** unter **Rows** nicht sehen, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) oder Ihren Braze-CSM.
-->

## Wissenswertes {#things-to-know}

- **Video:** Der Standard-Composer enthält keinen dedizierten Videoblock. Verwenden Sie **Custom code**, um bei Bedarf einen Player einzubetten. Weitere Informationen finden Sie unter [In-App-Nachrichten: Häufig gestellte Fragen]({{site.baseurl}}/user_guide/channels/in_app_messages/faq).

{% endsdktab %}

{% sdktab landing pages %}
## Landing-Page-Editor-Blöcke {#landing-page-editor-blocks}

Editor-Blöcke für Landing-Pages befinden sich im Bereich **Build** des **Drag-and-Drop-Editors** unter **Rows** und Blockkategorien. Ziehen Sie einen Block in eine Zeilenspalte; er passt sich automatisch an die Spaltenbreite an. Wählen Sie einen Block aus, um seine Einstellungen im rechten Eigenschaftenpanel zu bearbeiten.

Weitere Informationen zum Erstellen und Veröffentlichen von Landing-Pages finden Sie unter [Landing-Pages erstellen]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages).

### Titel und Absatz

Fügt Überschriften- oder Fließtext hinzu. Nützlich zum Strukturieren von Abschnitten und zur Verbesserung der Lesbarkeit.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Button

Fügt ein klickbares Element für Aktionen wie das Öffnen eines Links oder das Absenden eines Formulars hinzu.

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### Klickverhalten

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

{% alert important %}
Wenn Sie einen Button mit **Submit form when button is clicked** konfigurieren und eine Web-URL in einem neuen Tab öffnen, blockiert iOS Safari möglicherweise die Navigation. Öffnen Sie die URL nach dem Absenden im selben Tab, wenn Sie Formulare absenden. Weitere Informationen finden Sie unter [Landing-Pages erstellen]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages).
{% endalert %}

### Optionsfeld

Fügt eine Liste von Optionen hinzu, aus denen Nutzer:innen eine auswählen können. Verwenden Sie das Eigenschaftenpanel, um die verfügbaren Optionen und das angepasste Attribut zu konfigurieren, das den ausgewählten Wert empfängt. Das Kundenprofil protokolliert den ausgewählten Wert als [angepasstes String-Attribut]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), wenn das Formular abgesendet wird. Angepasste Attribute mit anderen Datentypen werden nicht im Kundenprofil gespeichert.

{% multi_lang_include drag_and_drop/editor_block_properties/radio_button_properties.md %}

### Bild

Zeigt ein Bild aus einem Upload oder einer externen URL an.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

#### Klickverhalten

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### Link

Fügt einen Hyperlink hinzu, den Nutzer:innen auswählen können, um zu einer URL zu navigieren. Kann in Text eingebettet oder eigenständig sein.

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### Klickverhalten

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### Abstandshalter

Fügt vertikalen Abstand zwischen Elementen hinzu.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Benutzerdefinierter Code

Fügt benutzerdefiniertes HTML, CSS oder JavaScript für erweiterte Anpassungen ein, z. B. [Google Tag Manager:in]({{site.baseurl}}/user_guide/messaging/landing_pages#adding-google-tag-manager-to-a-landing-page).

| Eigenschaft | Beschreibung |
| --- | --- |
| Custom code | Ermöglicht das Hinzufügen, Bearbeiten oder Löschen von HTML, CSS und JavaScript. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Benutzerdefinierter Code" }

<!-- Countdown timer is not yet released. Uncomment when available.
### Countdown-Timer {#countdown-timer}

Zeigt einen Countdown bis zu einem von Ihnen festgelegten Datum und Uhrzeit an. Wenn Sie diesen Block nicht sehen, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) oder Ihren Braze-CSM.

Nachdem Sie einen **Countdown-Timer**-Block hinzugefügt haben, verwenden Sie das Eigenschaftenpanel, um das Zieldatum und die Uhrzeit, Beschriftungen und das Styling festzulegen.
-->

### E-Mail-Erfassung

Fügt ein Formularfeld für E-Mail-Adressen hinzu. Beim Absenden wird die Adresse im Braze-Profil der Nutzer:in gespeichert.

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### Telefonnummernerfassung

Fügt ein Formularfeld für Telefonnummern hinzu. Beim Absenden wird die Nutzer:in für Ihre ausgewählte [SMS]({{site.baseurl}}/sms_rcs_subscription_groups)- oder [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups)-Abo-Gruppe angemeldet.

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### Eingabefeld {#input-field}

Fügt ein Formularfeld für Standardattribute (z. B. Vor- oder Nachname) oder einen angepassten Attribut-String hinzu.

{% multi_lang_include drag_and_drop/editor_block_properties/short_text_properties.md %}

### Dropdown

Eine vordefinierte Liste von Elementen; Nutzer:innen wählen eines aus. Sie können Werte angepassten Attribut-Strings zuordnen.

{% multi_lang_include drag_and_drop/editor_block_properties/dropdown_properties.md %}

### Kontrollkästchen

Wenn aktiviert, wird das [boolesche angepasste Attribut]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) des Blocks auf `true` gesetzt; wenn nicht aktiviert, auf `false`.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_properties.md %}

### Kontrollkästchengruppe

Nutzer:innen wählen mehrere Optionen aus; Werte werden in einem definierten [Array-angepassten Attribut]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) gesetzt oder hinzugefügt.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_group_properties.md %}

### Abos verwalten {#manage-subscriptions}

Fügt eine Checkliste von [E-Mail]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#email-subscription-groups)-, [SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#sms-subscription-states)- oder [WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-subscription-states)-Abo-Gruppen hinzu, damit Besucher:innen sich anmelden oder ihre Abos verwalten können, wenn sie das Formular absenden. Jeder Block ist für einen Kanal. Konfigurieren Sie ihn, nachdem Sie Abo-Gruppen zum Block hinzugefügt haben. Dieser Block listet keine RCS-Abo-Gruppen auf.

Für identifizierte Nutzer:innen, die die Seite über den [Liquid-Tag]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) der Landing-Page öffnen, füllt der Block jedes Kontrollkästchen mit dem aktuellen Abo-Status der Nutzer:in vor, sodass er auch als Seite zur Präferenzverwaltung dienen kann.

Wählen Sie den Block im Editor aus, um:

- Abo-Gruppen neu anzuordnen
- Abo-Gruppen hinzuzufügen oder zu entfernen
- Beschreibungen hinzuzufügen oder zu entfernen
- Ein Kontrollkästchen „Alle abonnieren“ hinzuzufügen oder zu entfernen, das jede Abo-Gruppe im Block auswählt

| Eigenschaft | Beschreibung |
| --- | --- |
| Subscription groups | Fügen Sie Abo-Gruppen hinzu, entfernen oder ordnen Sie die im Block angezeigten Abo-Gruppen neu an. |
| Include descriptions | Zeigt die Beschreibung jeder Abo-Gruppe neben ihrem Namen an. |
| Kontrollkästchen **Subscribe to all** | Fügt ein Kontrollkästchen hinzu, das jede Abo-Gruppe im Block auswählt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Abos verwalten" }

Den vollständigen Einrichtungsablauf finden Sie unter [Block „Abos verwalten“]({{site.baseurl}}/user_guide/messaging/landing_pages/manage_subscriptions).

### Langtext

Mehrzeiliges Textfeld für umfrageähnliche Abläufe. Wenn Sie diesen Block nicht sehen, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) oder Ihren Braze-CSM. Dieser Block ist für Standard-Landing-Pages nicht verfügbar.

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Gespeicherte Zeile

Fügt eine wiederverwendbare Zeile ein, die Sie zuvor als Drag-and-Drop-Content Block gespeichert haben. Gespeicherte Zeilen sind **nicht verknüpft** mit dem ursprünglichen Content Block — wenn das Original aktualisiert wird, müssen Sie es erneut in den Editor ziehen, um die neueste Version zu erhalten. Weitere Informationen finden Sie unter [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks). Wenn Sie **Saved row** unter **Rows** nicht sehen, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) oder Ihren Braze-CSM.
-->

## Wissenswertes

- **Video:** Der Standard-Composer enthält keinen dedizierten Videoblock. Verwenden Sie **Custom code**, um bei Bedarf einen Player einzubetten. Weitere Informationen finden Sie unter [Landing-Pages]({{site.baseurl}}/user_guide/messaging/landing_pages).

{% endsdktab %}

{% sdktab banners %}
## Banner-Editor-Blöcke {#banner-editor-blocks}

Ziehen Sie im Banner-Composer Zeilen und Blöcke aus dem Bereich **Build** in die Arbeitsfläche, um Ihre Nachricht zu gestalten. Wählen Sie **Styles**, um seitenweites Styling anzupassen, oder wählen Sie einen Block oder eine Zeile aus, um deren Eigenschaften im Seitenpanel zu bearbeiten.

Den vollständigen Ablauf zur Banner-Erstellung finden Sie unter [Banner erstellen]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#compose-a-banner).

Der Banner-Composer bietet dieselben Arten von Layout-Blöcken wie andere Drag-and-Drop-Oberflächen, jedoch nicht den vollständigen Satz an Formularblöcken (z. B. keine Optionsfeld-, Kurztext-, Dropdown- oder Kontrollkästchenblöcke). Sie können **Telefonnummernerfassung**- und **E-Mail-Erfassung**-Blöcke hinzufügen; pro Nachricht ist nur **ein** Telefonnummernerfassungs- und **ein** E-Mail-Erfassungsblock zulässig.

### Titel und Absatz

Fügt Überschriften- oder Fließtext mit Rich-Text-Optionen hinzu.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Button

Fügt einen klickbaren Button hinzu. Sie können Links und Analytics-Optionen im Eigenschaftenpanel festlegen.

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### Klickverhalten

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

Weitere Informationen finden Sie unter [Klickverhalten definieren]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#step-32-define-on-click-behavior-optional) im Banner-Artikel.

### Bild

Zeigt ein Bild von einer gehosteten URL an. Konfigurieren Sie die Anzeigeoptionen im Eigenschaftenpanel.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

#### Klickverhalten

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### Link

Fügt einen Hyperlink ein, den Nutzer:innen auswählen können.

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### Klickverhalten

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### Abstandshalter

Fügt vertikalen Abstand zwischen Blöcken hinzu.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Benutzerdefinierter Code

Fügt benutzerdefiniertes HTML für erweiterte Layouts oder eingebettete Inhalte ein (z. B. Video). Klicks innerhalb von benutzerdefiniertem HTML werden nicht getrackt, es sei denn, Sie rufen `brazeBridge.logClick()` auf — siehe [Benutzerdefinierter Code und JavaScript-Bridge für Banner]({{site.baseurl}}/user_guide/channels/banners/custom_code).

| Eigenschaft | Beschreibung |
| --- | --- |
| Custom code | Fügen Sie HTML (und zugehörige Assets) für das Banner hinzu oder bearbeiten Sie es. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Benutzerdefinierter Code" }

### Telefonnummernerfassung

Erfasst eine Telefonnummer. Beim Absenden wird die Nutzer:in für Ihre ausgewählte [SMS]({{site.baseurl}}/sms_rcs_subscription_groups)- oder [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups)-Abo-Gruppe angemeldet. Nur einer pro Banner.

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### E-Mail-Erfassung

Erfasst eine E-Mail-Adresse und fügt sie beim Absenden dem Braze-Profil der Nutzer:in hinzu. Nur einer pro Banner.

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### Langtext

Mehrzeiliges Textfeld für umfrageähnliche Abläufe. Wenn Sie diesen Block nicht sehen, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) oder Ihren Braze-CSM.

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Gespeicherte Zeile

Fügt eine wiederverwendbare Zeile ein, die Sie zuvor als Drag-and-Drop-Content Block gespeichert haben. Gespeicherte Zeilen sind **nicht verknüpft** mit dem ursprünglichen Content Block — wenn das Original aktualisiert wird, müssen Sie es erneut in den Editor ziehen, um die neueste Version zu erhalten. Weitere Informationen finden Sie unter [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks). Wenn Sie **Saved row** unter **Rows** nicht sehen, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) oder Ihren Braze-CSM.
-->

## Wissenswertes

- **Video:** Der Standard-Composer enthält keinen dedizierten Videoblock. Verwenden Sie **Custom code**, um bei Bedarf einen Player einzubetten. Weitere Informationen finden Sie unter [Banner: Häufig gestellte Fragen]({{site.baseurl}}/user_guide/channels/banners/faq).
- **Liquid:** Die meisten Liquid-Funktionen werden unterstützt; es gibt Ausnahmen wie Katalog-Rerender-Tags. Weitere Informationen finden Sie unter [Banner: Häufig gestellte Fragen]({{site.baseurl}}/user_guide/channels/banners/faq).

{% endsdktab %}

{% sdktab preference center %}
## Präferenzzentrum-Editor-Blöcke {#preference-center-editor-blocks}

Ziehen Sie Blöcke aus dem Bereich **Build** in eine Zeile im Drag-and-Drop-Präferenzzentrum-Editor. Jeder Block hat eigene Einstellungen; das rechte Seitenpanel wechselt zu den Eigenschaften oder dem Styling des ausgewählten Elements.

Bevor Sie Blöcke bearbeiten, fügen Sie Abo-Gruppen hinzu und konfigurieren Sie den Abo-**Smart-Block** (siehe folgenden Abschnitt). Den vollständigen Einrichtungsablauf finden Sie unter [E-Mail-Präferenzzentrum per Drag-and-Drop erstellen]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center).

### Titel und Absatz

Fügt Überschriften- oder Fließtext mit Rich-Text-Optionen hinzu.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Button

Fügt einen klickbaren Button hinzu (z. B. **Save** oder Navigation).

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

### Bild

Zeigt ein Bild aus der [Medienbibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) oder von einer URL an.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

### Abstandshalter

Fügt vertikalen Abstand zwischen Blöcken hinzu.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Abo-Gruppen (Smart-Block) {#subscription-groups-smart-block}

Fügt einen Template-Block hinzu, der Abo-Gruppen, optionale Steuerelemente **Subscribe to all** / **Unsubscribe from all** und Beschreibungen auflistet. Konfigurieren Sie ihn, nachdem Sie Gruppen im Präferenzzentrum-Workflow hinzugefügt haben.

Nachdem Sie [Abo-Gruppen hinzugefügt]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center#step-3-add-subscription-groups-to-the-preference-center) haben, wählen Sie den Smart-Block in der Arbeitsfläche aus, um:

- Abo-Gruppen neu anzuordnen
- Gruppen hinzuzufügen oder zu entfernen
- Beschreibungen hinzuzufügen oder zu entfernen
- **Subscribe to all** und **Unsubscribe from all** für die Gruppen in diesem Block umzuschalten

Das Steuerelement **Unsubscribe from all** am unteren Rand des Standard-Templates ist erforderlich und führt eine [globale Abmeldung]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states) von E-Mails durch.

## Wissenswertes

- **Gemeinsame Stile:** Sie können seitenweite Standardwerte unter **Common Styles** festlegen, bevor Sie einzelne Blöcke anpassen. Weitere Informationen finden Sie unter [Präferenzzentrum mit dem Drag-and-Drop-Editor anpassen]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center#step-4-customize-the-preference-center-using-the-drag-and-drop-editor).
- **Bestätigungsseite:** Wechseln Sie oben im Editor zu **Confirmation Page**, um das Erlebnis nach dem Speichern mit denselben Blocktypen zu gestalten.

{% endsdktab %}

{% endsdktabs %}