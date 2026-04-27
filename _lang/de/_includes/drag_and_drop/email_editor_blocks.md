## Verwendung von E-Mail-Editor-Blöcken {#using-email-editor-blocks}

Die Editor-Blöcke befinden sich im Abschnitt **Inhalt** für E-Mail-Nachrichten. Um einen Editor-Block zu verwenden, ziehen Sie im Drag-and-Drop-Editor einen Editor-Block in eine Spalte. Er passt sich automatisch an die Spaltenbreite an. Jeder Editor-Block hat seine eigenen Einstellungen, wie z. B. die granulare Steuerung des Paddings.

Weitere Informationen zur Verwendung und Anpassung dieser Editor-Blöcke in Ihrer E-Mail finden Sie unter [Weitere Anpassungen]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/#other-customizations).

{% alert tip %}
Sie können auch [angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/) zu jeder URL innerhalb der Editor-Blöcke `Image`, `Button` oder `Text` hinzufügen.
{% endalert %}

## Typen {#types}

In der folgenden Tabelle wird beschrieben, wie Nutzer:innen die einzelnen Editor-Block-Typen verwenden können.

| Name | Beschreibung |
|---|---|
|Titel| Fügt Text für Überschriften innerhalb der E-Mail hinzu. |
|Absatz| Gibt Text in die Nachricht ein. Eine Symbolleiste hilft bei der Schrift- und Textbearbeitung. |
|Liste| Fügt eine Aufzählungsliste hinzu. |
|Button| Fügt einen Standard-Button hinzu. Die Eigenschaften dieses Blocks ermöglichen das einfache Bearbeiten und Setzen von Links. |
|Trennlinie| Fügt eine durchgezogene, gepunktete oder gestrichelte Linie ein, um die Abstände zu vergrößern.|
|Spacer| Fügt Leerraum oder „Padding“ zwischen anderen Blöcken hinzu. |
|Bild| Fügt ein Bild aus der [Medienbibliothek]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) ein. |
|Video| Erstellt einen Link zum Video-Inhalt. |
|Social| Fügt ein Social-Media-Plattform-Symbol ein. Sie können angepasste Bilder für markenspezifische Symbole hochladen. |
|Icons| Fügt ein Symbol ein. Sie können angepasste Bilder hochladen. Braze verwendet ein übergroßes Platzhalter-Symbol, bis Sie ein Bild hochladen. |
|HTML| Fügt rohes HTML ein. Empfohlen für [Liquid]({{site.baseurl}}/liquid/), wie beispielsweise Connected-Content oder bedingte Anweisungen. |
|Menü| Erstellt ein flexibles Menü für die Nachricht, die Sie entwerfen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Personalisierung in E-Mails {#personalization-in-email}

- **Liquid:** Wählen Sie unter **Inhalt** > **Personalisierung** ein Attribut aus, kopieren Sie das Snippet und fügen Sie es in einen Textblock (einfaches Liquid) oder HTML-Block (erweitertes Liquid) ein. Generell können Sie zwar einfaches Liquid in Textblöcken verwenden, wir empfehlen jedoch HTML-Blöcke für komplexere Logik, um Layout-Probleme zu vermeiden. Beachten Sie, dass Liquid in Bildblöcken oder in Button-URL-Feldern nicht unterstützt wird.
- **Connected-Content:** Fügen Sie einen **HTML**-Block hinzu und platzieren Sie Ihren {% raw %}`{% connected_content %}`{% endraw %}-Aufruf dort.

## Eigenschaften {#properties}

Einzelheiten zu den Eigenschaften der einzelnen Editor-Blöcke finden Sie in den folgenden Tabellen.

### Titel {#title}
In der folgenden Tabelle finden Sie Einzelheiten zu den Eigenschaften des Editor-Blocks `Title`.

| Eigenschaften | Beschreibung |
|---|---|
|Titel| Wählt den Überschriftenstil aus. |
|Schriftfamilie| Dies ist der Schriftstil für Ihren Titel. |
|Schriftschnitt| Dies ist die allgemeine Stärke der Schriftart. |
|Schriftgröße| Bestimmt die Größe Ihres Textes. |
|Textfarbe| Ändert die Farbe des Titels. |
|Linkfarbe| Ändert die Farbe des Links. |
|Ausrichtung| Verschiebt den Titel nach links, in die Mitte oder nach rechts. |
|Zeilenhöhe| Ändert den Abstand zwischen den Textzeilen. |
|Zeichenabstand| Ändert den Abstand zwischen den einzelnen Zeichen. |
|Textrichtung| Standardmäßig von links nach rechts, kann jedoch auf [rechts nach links]({{site.baseurl}}/right_to_left_messages/) geändert werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Absatz {#paragraph}

In der folgenden Tabelle finden Sie Einzelheiten zu den Eigenschaften des Editor-Blocks `Paragraph`.

| Eigenschaften | Beschreibung |
|---|---|
|Schriftfamilie| Dies ist der Schriftstil für Ihren Absatztext. |
|Schriftschnitt| Dies ist die allgemeine Stärke der Schriftart. |
|Schriftgröße| Bestimmt die Größe Ihres Textes. |
|Textfarbe| Ändert die Farbe des Textes. |
|Linkfarbe| Ändert die Farbe des Links. |
|Ausrichtung| Verschiebt den Text nach links, in die Mitte oder nach rechts. |
|Absatzabstand| Ändert den Abstand zwischen den Absätzen. |
|Zeilenhöhe| Ändert den Abstand zwischen den Textzeilen. |
|Buchstabenabstand| Ändert den Abstand zwischen den einzelnen Zeichen. |
|Textrichtung| Standardmäßig von links nach rechts, kann jedoch auf [rechts nach links]({{site.baseurl}}/right_to_left_messages/) geändert werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Liste {#list}

In der folgenden Tabelle finden Sie Einzelheiten zu den Eigenschaften des Editor-Blocks `List`.

| Eigenschaften | Beschreibung |
|---|---|
|Listentyp| Dies ist die Art der Liste. Kann entweder als Aufzählung oder nummeriert sein. |
|Listenstil-Typ| Bestimmt den Stil Ihrer Liste. |
|Liste beginnen ab| Bestimmt die Startnummer für Ihre Liste. |
|Schriftfamilie| Dies ist der Schriftstil für Ihren Absatztext. |
|Schriftschnitt| Dies ist die allgemeine Stärke der Schriftart. |
|Schriftgröße| Bestimmt die Größe Ihres Textes. |
|Textfarbe| Ändert die Farbe des Textes. |
|Linkfarbe| Ändert die Farbe des Links. |
|Ausrichtung| Verschiebt den Text nach links, in die Mitte oder nach rechts. |
|Abstand zwischen Listenelementen| Ändert den Abstand zwischen den Listenelementen. |
|Einrückung der Listenelemente| Ändert die Einrückung von Listenelementen. |
|Zeilenhöhe| Ändert den Abstand zwischen den Textzeilen. |
|Buchstabenabstand| Ändert den Abstand zwischen den einzelnen Zeichen. |
|Textrichtung| Standardmäßig von links nach rechts, kann jedoch auf [rechts nach links]({{site.baseurl}}/right_to_left_messages/) geändert werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Trennlinie {#divider}

In der folgenden Tabelle finden Sie Einzelheiten zum Editor-Block `Divider`.

| Eigenschaften | Beschreibung |
|---|---|
|Transparent| Wenn aktiviert, werden die Optionen „Linie“ und „Breite“ entfernt. |
|Linie| Die verschiedenen Linienformate, ob gestrichelt, gepunktet oder durchgezogen. Darüber hinaus können Sie die Dicke und Farbe der Trennlinie ändern. |
|Breite| Passt die Ausdehnung der Trennlinie in 5er-Schritten an. |
|Ausrichtung| Verschiebt die Linie nach links, in die Mitte oder nach rechts. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Spacer

In der folgenden Tabelle finden Sie Einzelheiten zum Editor-Block `Spacer`.

| Eigenschaften | Beschreibung |
|---|---|
|Höhe| Passt die Höhe des Spacer-Blocks an. Der Standardwert ist 60px.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Bild {#image}

In der folgenden Tabelle finden Sie Einzelheiten zum Editor-Block `Image`. Für dynamische Bilder (Bilder mit Liquid oder Connected-Content) müssen Sie ein Fallback-Bild festlegen, um die Einstellungen für die automatische Breitenanpassung zu verwenden. Informationen zu Bildspezifikationen finden Sie in unseren [E-Mail-Bildspezifikationen]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/image_specs/#email).

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

| Eigenschaften | Beschreibung |
|---|---|
|Automatische Breite| Ändert die Breite des Bildes in Pixel. |
|Ausrichtung| Richtet das Bild entweder links, in der Mitte oder rechts des Blocks aus. |
|Bild mit Liquid| Verwenden Sie [Liquid]({{site.baseurl}}/liquid/)-Logik, um dynamisch verschiedene Bilder innerhalb desselben Inhaltsblocks festzulegen. |
|URL| Legen Sie ein Bild über die Adresse fest, unter der es gehostet wird. |
|Alternativer Text| Eine kurze Beschreibung des Bildes, die den Nutzer:innen die gleichen Informationen liefert, die auch auf dem Bild zu sehen sind. Dies ist für die Barrierefreiheit von Screenreadern oder für den Fall, dass das Bild nicht geladen werden kann, unerlässlich. |
|Bild mit abgerundeten Ecken| Rendert das Bild mit abgerundeten Ecken. Standardmäßig werden Bilder mit eckigen Ecken gerendert. |
|Aktion| Löst eine Aktion aus, wenn die Nutzer:in auf das Bild klickt.|
|Blockoptionen| Legt das Padding um den Bildblock fest. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Für `Auto Width` wählt die automatische Bildgrößenanpassung die beste Größe für das Bild auf der Grundlage einer Kombination aus Bildbreite und verfügbarem Platz im Layout:
- Bilder, die breiter sind als der verfügbare Platz, werden auf eine Breite von 100 % gesetzt und behalten dieses Verhältnis auf Mobilgeräten bei, wobei die gesamte Anzeigebreite des Geräts genutzt wird.
- Bei Bildern, die kleiner sind als der verfügbare Platz, wird die natürliche Größe des Bildes verwendet, um Verzerrungseffekte oder unscharfe Bilder zu vermeiden.
{% endalert %}

### Video

In der folgenden Tabelle finden Sie Einzelheiten zum Editor-Block `Video`.

| Eigenschaften | Beschreibung |
|---|---|
|URL| Die URL für das Video. Beachten Sie, dass nur YouTube und Vimeo unterstützt werden. |
|Titel| Wird automatisch aus den Metadaten des Videos generiert oder kann angepasst werden. |
|Wiedergabesymbol-Stil| Enthält verschiedene Optionen für den Wiedergabe-Button, der sich oben auf einem Videobild befindet. |
|Wiedergabesymbol-Farbe| Option zur Auswahl von **Hell** oder **Dunkel** für den Wiedergabe-Button. |
|Wiedergabesymbol-Größe| Wählen Sie die Pixelgröße für den Wiedergabe-Button. Vordefinierter Bereich von 50&nbsp;px bis 80&nbsp;px (in 5&nbsp;px-Schritten). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Videos, die von Vimeo gehostet werden, funktionieren nur, wenn sie auf öffentlich eingestellt sind. Alle anderen Sicherheitseinstellungen, die in Vimeo verfügbar sind (z. B. „Vor Vimeo.com verbergen“), generieren ein anderes Linkformat, das von diesem Content-Block nicht unterstützt wird. Diese Arten von Links werden vom Builder geändert, wodurch Braze keine Miniaturansicht erstellen kann.
{% endalert %}

### Social

In der folgenden Tabelle finden Sie Einzelheiten zum Editor-Block `Social`.

| Eigenschaften | Beschreibung |
|---|---|
|Symbolsammlung auswählen| Legt den Stil Ihrer Symbolsammlung fest. |
|Symbolsammlung konfigurieren| Legt die URL für jedes Social-Media-Symbol fest. Enthält den Umschalter **Weitere Optionen** zum Bearbeiten des Titels und des Alternativtextes. |
|Ausrichtung| Verschiebt das Social-Media-Symbol nach links, in die Mitte oder nach rechts. |
|Symbolabstand| Bestimmt den Abstand zwischen den einzelnen Social-Media-Symbolen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Icons

In der folgenden Tabelle finden Sie Einzelheiten zum Editor-Block `Icons`.

| Eigenschaften | Beschreibung |
|---|---|
|Schriftfamilie| Dies ist der Schriftstil für Ihren Absatztext. |
|Schriftschnitt| Dies ist die allgemeine Stärke der Schriftart. |
|Schriftgröße| Bestimmt die Größe Ihres Textes. |
|Textfarbe| Ändert die Farbe des Textes. |
|Linkfarbe| Ändert die Farbe des Links. |
|Ausrichtung| Verschiebt das Symbol nach links, in die Mitte oder nach rechts. |
|Buchstabenabstand| Ändert den Abstand zwischen den einzelnen Zeichen. |
|Symbolgröße| Bestimmt die Größe Ihres Symbols. |
|Symbolabstand| Ändert den Abstand des Symbols. |
|Symbol-Padding| Ändert das Padding des Symbols. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### HTML

In der folgenden Tabelle finden Sie Einzelheiten zum Editor-Block `HTML`.

| Eigenschaften | Beschreibung |
|---|---|
|HTML-Editor| Geben Sie das rohe HTML ein. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Menü {#menu}

In der folgenden Tabelle finden Sie Einzelheiten zum Editor-Block `Menu`.

| Eigenschaften | Beschreibung |
|---|---|
|Menüelemente konfigurieren| Fügt ein Menüelement hinzu. |
|Schriftfamilie| Der Stil, der für Ihr Menü verwendet werden soll. |
|Schriftgröße| Die Größe Ihres Menüs. |
|Textfarbe| Ändert die Farbe des Menüs. |
|Linkfarbe| Ändert die Farbe des Menütextes. |
|Ausrichtung| Verschiebt das Menü nach links, in die Mitte oder nach rechts. |
|Buchstabenabstand| Ändert den Abstand zwischen den einzelnen Zeichen. |
|Layout| Legt fest, ob das Layout horizontal oder vertikal sein soll. |
|Trennzeichen| Fügt Zeichen zwischen den Menüoptionen ein. |
|Mobiles Menü| Enthält Optionen zum Ändern der Symbolgröße, Farbe und des Symboltyps bei der Anzeige auf einem Mobilgerät. |
|Element-Padding| Ändert das Padding entweder mit der Taste **+** oder **-** oder durch Eingabe einer bestimmten Zahl. |
|Alle Seiten| Legt ein einheitliches Padding fest, wenn das Element-Padding deaktiviert ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Aktionen {#actions}

Sie können eine Aktion zuweisen, die ausgeführt wird, wenn eine Nutzer:in auf einen Button, einen Link oder ein Bild in der Nachricht tippt. Sie können auch [Liquid]({{site.baseurl}}/liquid/) verwenden, um die Aktionen zu personalisieren. Einzelheiten zu den Aktionen der einzelnen Editor-Blöcke finden Sie in den folgenden Tabellen.

### Button

In der folgenden Tabelle finden Sie Einzelheiten zum Editor-Block `Button`.

| Eigenschaften | Beschreibung |
|---|---|
|Link-Typ| Legt die Aktion beim Klicken auf den Button fest und stellt das entsprechende Protokoll ein. |
|URL| Dynamisch basierend auf dem Link-Typ **Webseite öffnen**.|
|Empfänger:in, Betreff und Text| Für den Link-Typ **E-Mail senden** werden hier die E-Mail-Adresse der Empfänger:in, der Betreff und der Inhalt festgelegt, die in einem E-Mail-Entwurf angezeigt werden, wenn die Nutzer:in den Button auswählt.|
|Tel.| Für die Link-Typen **Anruf tätigen** und **SMS senden** wird hier die Telefonnummer festgelegt, die die Nutzer:in anruft oder per SMS kontaktiert, wenn sie den Button auswählt.|
|Nachricht| Für den Link-Typ **SMS senden** legt dies den Inhalt fest, der in einem SMS-Entwurf angezeigt wird, wenn die Nutzer:in den Button auswählt.|
|Button-Optionen| Legt verschiedene Button-Optionen fest, wie beispielsweise Schriftart, Breite, Farbe und andere.|
|Button-Hover| Der Stil des Buttons, wenn eine Nutzer:in mit der Maus oder dem Trackpad darüber fährt. Dazu gehören die Hintergrundfarbe des Buttons, die Schriftfarbe und der Rahmenstil.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }