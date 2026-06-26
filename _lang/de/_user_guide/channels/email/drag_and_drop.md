---
nav_title: Drag-and-Drop-Editor
article_title: Eine E-Mail mit Drag-and-Drop erstellen
alias: /dnd/
page_order: 1
description: "Dieser Artikel beschreibt, wie Sie den Drag-and-Drop-Editor für E-Mail-Nachrichten einrichten und richtig verwenden."
channel: email
tool:
- Campaigns
- Canvas
---

# Eine E-Mail mit Drag-and-Drop erstellen {#create-an-email-with-drag-and-drop}

> Mit dem Drag-and-Drop-Editor können Sie vollständig angepasste und personalisierte E-Mail-Nachrichten für Campaigns oder Canvases erstellen – ganz ohne HTML für den E-Mail-Body verwenden zu müssen.

## Über den Editor {#about-the-editor}

Der Drag-and-Drop-Editor verwendet [Inhalt](#content) und [Zeilen](#rows) als die beiden Schlüsselkomponenten, um Ihren Workflow zu vereinfachen – ohne zusätzliche Verwendung von HTML.

<table aria-label="Über den Editor" style="width: 100%; table-layout: fixed;">
    <caption>Inhalt und Zeilen als Editor-Komponenten</caption>
    <thead>
    <tr>
        <th style="width: 50%;">Inhalt</th>
        <th style="width: 50%;">Zeilen</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td style="text-align: center;">
            <img src="{% image_buster /assets/img/dnd/dnd_content.png %}" alt="Der Tab 'Zeilen' mit verschiedenen strukturellen Kombinationen für Ihr E-Mail-Layout." style="max-width: 100%; height: auto;">
        </td>
        <td style="text-align: center;">
            <img src="{% image_buster /assets/img/dnd/dnd_rows.png %}" alt="Der Tab 'Inhalt' mit grundlegenden Blöcken, Medien und erweiterten Optionen." style="max-width: 100%; height: auto;">
        </td>
    </tr>
    </tbody>
</table>
{: .reset-td-br-1 aria-label="Über den Editor" }

### Inhalt {#content}

**Inhalt** umfasst eine Reihe von Kacheln, die verschiedene Inhaltstypen darstellen, die Sie in Ihrer Nachricht verwenden können. Diese sind in drei Kategorien unterteilt: grundlegend, Medien und erweitert.

{% tabs %}
{% tab Grundlegend %}

Grundlegende Blöcke bilden das Fundament Ihrer E-Mail. Mit diesen Blöcken können Sie jedes der folgenden Elemente in Ihren E-Mail-Body einfügen:

- Titel
- Absatz
- Liste
- Button
- Trennlinie
- Abstandshalter

{% endtab %}
{% tab Medien %}

Mit Medienblöcken können Sie verschiedene visuelle Inhalte hinzufügen, wie Bilder, Videos, Social-Media-Icons und -Links sowie anpassbare Icons.

{% endtab %}
{% tab Erweitert %}

Obwohl der Drag-and-Drop-Editor Ihren Workflow mit diesen Blöcken vereinfacht, können Sie auch erweiterte Blöcke verwenden, um HTML einzufügen oder ein Menü zu Ihrem E-Mail-Body hinzuzufügen. Beachten Sie, dass die Verwendung von eigenem HTML die Darstellung der Nachricht beeinflussen kann.

{% endtab %}
{% endtabs %}

### Zeilen {#rows}

**Zeilen** sind strukturelle Einheiten, die die horizontale Zusammensetzung eines Abschnitts der Nachricht mithilfe von Spalten definieren. Sie können entweder leere Zeilen oder [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/) verwenden. Durch die Verwendung von mehr als einer Spalte können Sie verschiedene Inhaltselemente nebeneinander platzieren. So können Sie alle strukturellen Elemente, die Sie benötigen, zu Ihrer Nachricht hinzufügen – unabhängig davon, welches Template Sie zu Beginn ausgewählt haben.

#### Bilder in Textblöcken verschachteln {#nesting-images-inside-text-blocks}

Sie können im Drag-and-Drop-Editor kein Bild innerhalb eines Absatzes oder eines anderen Textblocks verschachteln. Um ein Bild neben oder innerhalb eines Textlayouts zu platzieren, verwenden Sie Spalten in einer **Zeile**: zum Beispiel eine mehrspaltige Zeile auf dem Desktop mit **Hide on mobile** für diese Zeile und eine separate, nur für Mobilgeräte bestimmte Zeile (mit **Hide on desktop** und **Do not stack on mobile** nach Bedarf), damit Bild und Text auf kleinen Bildschirmen sauber ausgerichtet sind.

#### Cards-Stil {#cards-style}

**Cards-Stil** ist eine Zeileneigenschaft, mit der Sie Abstände zwischen Spalten hinzufügen und deren Ecken abrunden können. Mit der Cards-Stil-Formatierung können Sie visuell ansprechendere Layouts erstellen, die Ihre wichtigsten Inhalte hervorheben – wie neue Produkt-Features, Testimonials, Sonderangebote, Neuigkeiten und mehr.

## Den Drag-and-Drop-Editor verwenden {#using-the-drag-and-drop-editor}

Sind Sie unsicher, ob Ihre E-Mail-Nachricht über eine Campaign oder ein Canvas gesendet werden sollte? Campaigns eignen sich besser für einzelne, gezielte Messaging-Kampagnen, während Canvases besser für mehrstufige User-Journeys geeignet sind.

{% alert note %}
Sie können eine Drag-and-Drop-E-Mail aus einer Campaign oder einem Canvas nicht direkt unter **Templates** > **E-Mail-Templates** als E-Mail-Template speichern. Erstellen Sie das Template zuerst unter **Templates**, oder lesen Sie [Kann ich meine Drag-and-Drop-E-Mail als Template speichern, nachdem ich sie in meiner Campaign oder meinem Canvas erstellt habe?]({{site.baseurl}}/user_guide/channels/email/drag_and_drop/faq/#can-i-save-my-drag-and-drop-email-as-a-template-after-i-build-it-within-my-campaign-or-canvas), um ein Drag-and-Drop-Template neu zu erstellen oder HTML mit **Download file** zu exportieren.
{% endalert %}

Nachdem Sie ausgewählt haben, wo Sie Ihre Nachricht erstellen möchten, gehen wir die Schritte zum Erstellen einer Drag-and-Drop-E-Mail durch.

### 1. Schritt: Template auswählen {#step-1-select-your-template}

Nachdem Sie den Drag-and-Drop-Editor als Bearbeitungserfahrung ausgewählt haben, können Sie:

- Mit einem leeren Template beginnen.
- Ein vorgefertigtes Braze-Drag-and-Drop-E-Mail-Template verwenden.
- Ein gespeichertes Drag-and-Drop-E-Mail-Template verwenden.

{% alert note %}
Um ein vorhandenes benutzerdefiniertes HTML-Template oder von Drittanbietern erstellte Templates zu verwenden, müssen Sie das Template neu erstellen, indem Sie zu **Content** > **Email** gehen und **Drag-And-Drop Editor** als Bearbeitungserfahrung auswählen.
{% endalert %}

Sie können auch über den Bereich **Templates** auf alle Templates zugreifen.

Nachdem Sie Ihr Template ausgewählt haben, sehen Sie unter **Email Variants** eine Übersicht Ihrer E-Mail, die die Sendeinformationen und den E-Mail-Body enthält.

Wählen Sie dann **Edit Email Body**, um mit dem Entwerfen der E-Mail-Struktur im Drag-and-Drop-Editor zu beginnen.

![Der Abschnitt „Email Variants“ mit einem Beispiel-E-Mail-Body.]({% image_buster /assets/img/dnd/dnd_emailvariant.png %})

### 2. Schritt: E-Mail erstellen {#step-2-build-your-email}

Die Drag-and-Drop-Bearbeitungserfahrung ist in drei Abschnitte unterteilt: **Sending Settings**, **Content** und **Preview & Test**. Die eigentliche Gestaltung Ihres E-Mail-Bodys findet im Abschnitt **Content** statt. Bevor Sie Ihre E-Mail erstellen, ist es wichtig, die Schlüsselkomponenten zu verstehen, die Ihre E-Mail-Erstellung leiten. Falls Sie eine Auffrischung benötigen, lesen Sie [Über den Editor](#about-the-editor).

Wenn Sie bereit sind, verwenden Sie die Drag-and-Drop-Inhaltsblöcke, um Ihre E-Mail zu erstellen.

1. Wählen Sie das Panel **Rows**. Ziehen Sie die Zeilenkonfigurationen per Drag-and-Drop in den Haupteditor. Dies legt das Layout Ihres E-Mail-Inhalts fest.
- Beachten Sie, dass neue Konfigurationen an den Anfang oder das Ende eines bestehenden Abschnitts gezogen werden müssen.
- Wenn Sie eine Zeilenkonfiguration auswählen, erscheinen die **Row Properties**-Einstellungen zur weiteren Anpassung von Zeilen-Hintergrundfarben, Bildern und benutzerdefinierten Spaltengrößen.
2. Wählen Sie das Panel **Content**. Ziehen Sie die gewünschten Inhaltskacheln per Drag-and-Drop in die Zeilenkomponenten.
- Sie können auch beliebige **Content**-Kacheln in den Haupteditor ziehen. Dadurch wird automatisch eine Zeile für die Kachel erstellt.
- Sie können die Kachel weiter verfeinern, indem Sie sie auswählen und die Felder unter **Content Properties** und **Block Options** anpassen. Dazu gehören die Bearbeitung von Zeichenabstand, Padding, Zeilenhöhe und mehr.

Weitere Möglichkeiten zur Anpassung Ihrer Drag-and-Drop-E-Mail finden Sie unter [Weitere Anpassungen](#other-customizations).

Während Sie Ihre E-Mail erstellen, können Sie zwischen einer Desktop- und einer Mobilansicht wechseln, um eine Vorschau zu sehen, wie Ihre E-Mail-Nachricht für Ihre Nutzergruppen aussehen wird. So können Sie überprüfen, ob Ihr Inhalt responsiv ist, und unterwegs alle notwendigen Anpassungen vornehmen.

{% alert tip %}
Brauchen Sie Hilfe beim Verfassen überzeugender Texte? Probieren Sie den [KI-Textassistenten]({{site.baseurl}}/user_guide/brazeai/operator/capabilities/#generate-copy) aus. Geben Sie einen Produktnamen oder eine Beschreibung ein, und die KI generiert menschenähnliche Marketingtexte zur Verwendung in Ihren Nachrichten.

![Button „Textassistent“ im Content-Panel neben den Stileinstellungen im Drag-and-Drop-Editor.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_dnd.png %})
{% endalert %}

### 3. Schritt: Sendeinformationen hinzufügen {#step-3-add-your-sending-information}

Sobald Sie das Design und den Aufbau Ihrer E-Mail-Nachricht abgeschlossen haben, ist es an der Zeit, Ihre Sendeinformationen im Abschnitt **Sending Settings** hinzuzufügen.

1. Wählen Sie unter **Sending Info** eine E-Mail als **From Display Name + Address** aus. Sie können dies auch anpassen, indem Sie **Customize From Display Name + Address** auswählen.
2. Wählen Sie eine E-Mail als **Reply-To Address** aus. Sie können dies auch anpassen, indem Sie **Customize Reply-To Address** auswählen.
3. Wählen Sie als Nächstes eine E-Mail als **BCC Address** aus, um Ihre E-Mail für diese Adresse sichtbar zu machen.
4. Fügen Sie Ihrer E-Mail eine Betreffzeile hinzu. Optional können Sie auch einen Preheader und ein Leerzeichen nach dem Preheader hinzufügen.

{% multi_lang_include alerts/tip_alerts.md alert='Liquid email display name and reply-to address' %}

Im rechten Panel wird eine Vorschau mit den von Ihnen hinzugefügten Sendeinformationen angezeigt. Diese Informationen können auch aktualisiert werden, indem Sie zu **Settings** > **Email Preferences** > **Sending Configuration** navigieren.

#### E-Mail-Anhänge hinzufügen {#add-email-attachments}

Unter **Sending Settings** > **Advanced** können Sie E-Mail-Anhänge mit den folgenden Methoden hinzufügen:

- **Datei hochladen:** Ziehen Sie eine Datei per Drag-and-Drop oder durchsuchen Sie Ihren Computer, um eine Datei direkt hochzuladen. Braze validiert den Dateityp und die Größe (standardmäßig bis zu 2&nbsp;MB) vor dem Hochladen, und die Dateien werden dann in die Medienbibliothek hochgeladen. Dateien, die das Limit von 2&nbsp;MB überschreiten, können nicht hochgeladen werden.
- **Medienbibliothek verwenden:** Durchsuchen und wählen Sie aus bereits in der [Medienbibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/) gespeicherten Assets. PDFs, Word-Dokumente, Excel-Dateien und PowerPoint-Präsentationen werden unterstützt.
- **Von URL hinzufügen:** Geben Sie eine URL ein, die auf die Datei verweist, und geben Sie einen Anzeige-Dateinamen an. Da Braze beliebige URLs während der E-Mail-Erstellung nicht auf ihre Größe prüfen kann, wird die Dateigröße zum Sendezeitpunkt überprüft. Beachten Sie, dass Liquid in diesem Feld nicht unterstützt wird.

Spezifische Best Practices finden Sie unter [E-Mail-Richtlinien]({{site.baseurl}}/user_guide/channels/email/best_practices/email_guidelines/).

#### E-Mail-Header personalisieren (erweitert) {#personalize-your-email-header-advanced}

Unter **Sending Settings** können Sie Personalisierung für E-Mail-Header und E-Mail-Extras hinzufügen, mit denen Sie zusätzliche Daten an andere E-Mail-Anbieter zurücksenden können. Die Personalisierung eines E-Mail-Headers, z. B. durch Einbeziehung des Namens der Empfänger:in, kann auch dazu beitragen, die Wahrscheinlichkeit zu erhöhen, dass Ihre E-Mail geöffnet wird.

{% alert note %}
Erweiterte Funktionen werden im Campaign- oder Canvas-Composer angezeigt. In den erweiterten Funktionen können Sie Ihre Inline-CSS-Einstellung ändern und Header- oder zusätzliche Schlüssel-Wert-Paare eingeben (falls konfiguriert).
{% endalert %}

### 4. Schritt: E-Mail testen {#step-4-test-your-email}

Nachdem Sie Ihre Sendeinformationen hinzugefügt haben, ist es an der Zeit, Ihre E-Mail zu testen.

{% alert tip %}
Wenn die E-Mail im Editor anders aussieht als in der Vorschau oder beim Testversand, überprüfen Sie, ob alle Tags geschlossen sind, Bildattribute Werte haben und Hintergrundbilder an den Rändern nicht unscharf sind.
{% endalert %}

Gehen Sie zum Abschnitt **Preview and Test**. Hier haben Sie die Möglichkeit, eine Vorschau Ihrer E-Mail als Nutzer:in anzuzeigen oder eine Testnachricht zu senden. Dieser Abschnitt enthält auch [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision/), mit dem Sie überprüfen können, ob Ihre E-Mail in verschiedenen mobilen und Web-Clients korrekt dargestellt wird.

{% alert tip %}
Sie können auch den Schalter **Dark Mode Preview** im Vorschau-Panel verwenden, um Ihren E-Mail-Body im Dark Mode anzuzeigen und Ihre E-Mail bei Bedarf anzupassen.
{% endalert %}

Da Sie drei verschiedene Versionen derselben E-Mail anzeigen können – im eigentlichen Editor, in Inbox Vision und als tatsächliche Test-E-Mail – ist es wichtig, die Details über alle Ihre Plattformen hinweg abzugleichen.

#### Vorschau und Testversand {#preview-and-test-send}

Unter dem Tab **Preview as a User** können Sie die folgenden Nutzertypen auswählen, um eine Vorschau Ihrer Nachricht anzuzeigen.

- **Random User:** Braze wählt zufällig eine:n Nutzer:in aus der Datenbank aus und zeigt die E-Mail basierend auf deren Attributen oder Ereignisinformationen in der Vorschau an.
- **Select User:** Sie können eine:n bestimmte:n Nutzer:in anhand der E-Mail-Adresse oder externen ID auswählen. Die E-Mail wird basierend auf den Attributen und Ereignisinformationen dieser Person in der Vorschau angezeigt.
- **Custom User:** Sie können eine:n Nutzer:in anpassen. Braze bietet Eingabefelder für alle verfügbaren Attribute und Ereignisse. Sie können beliebige Informationen eingeben, die Sie in der Vorschau-E-Mail sehen möchten.

{% alert note %}
Die zufällige Person kann, muss aber nicht Teil Ihrer Segmentierungskriterien sein. Die Segmentierung wird erst danach ausgewählt, sodass Braze zu diesem Zeitpunkt Ihre Zielgruppe nicht kennt.
{% endalert %}

Sie können auch **Copy preview link** auswählen, um einen teilbaren Vorschau-Link zu generieren und zu kopieren, der zeigt, wie die E-Mail für eine:n zufällige:n Nutzer:in aussehen wird. Der Link ist sieben Tage gültig, bevor er neu generiert werden muss.

Beachten Sie, dass Änderungen an einem E-Mail-Template sich nicht in einem zuvor generierten Link widerspiegeln. Sie müssen eine neue Link-Vorschau generieren, um Änderungen zu sehen.

![E-Mail-Vorschau mit einem Button zum Kopieren des Vorschau-Links und zum Kopieren des generierten Links.]({% image_buster /assets/img/dnd_email_link_preview.png %})

#### Inbox Vision verwenden {#use-inbox-vision}

Inbox Vision ermöglicht es Ihnen, Ihre E-Mail-Campaigns aus der Perspektive von E-Mail-Clients und Mobilgeräten zu betrachten. Um Ihre E-Mail-Nachricht mit Inbox Vision zu testen, wählen Sie **Inbox Vision** im Abschnitt **Preview & Test** und dann **Run Inbox Vision**.

Es ist wichtig, die feinen Details Ihrer E-Mail-Nachricht zu testen und zu überprüfen. Beispielsweise können Hintergrundbilder in E-Mail-Nachrichten manchmal weiße Linien oder Unterbrechungen zwischen Bildern verursachen, oder Clients wie Windows Outlook zeigen Hintergrundbilder möglicherweise nicht an. Die Verwendung von Inbox Vision kann helfen, diese Diskrepanzen zwischen Clients zu identifizieren. In diesem Szenario legen Sie eine Fallback-Hintergrundfarbe fest, damit diese Bilder wie erwartet dargestellt werden können.

Weitere Informationen finden Sie unter [Testnachrichten senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=email).

Nachdem Sie den Drag-and-Drop-Editor zum Entwerfen und Erstellen Ihrer E-Mail-Nachricht verwendet haben, fahren Sie mit dem [Aufbau]({{site.baseurl}}/user_guide/channels/email/html_editor/#step-4-build-the-remainder-of-your-campaign-or-canvas) des restlichen Teils Ihrer Campaign oder Ihres Canvas fort.

{% details Über die aktualisierte HTML-Engine %}
Die zugrunde liegende Engine, die HTML aus dem Drag-and-Drop-Editor erzeugt, wurde optimiert und aktualisiert, was zu Vorteilen bei der HTML-Dateikomprimierung und dem Rendering führt.

Unser durchschnittlicher exportierter HTML-Daten-Footprint wurde reduziert, was zu schnellerem Laden und Rendering, weniger mobilem Clipping und geringerem Bandbreitenverbrauch führt.

Das HTML-Rendering wurde durch die folgenden Updates verbessert, die die Anzahl der bedingten Kommentare und CSS-Media-Queries minimieren. Dadurch sind HTML-Dateien kleiner und effizienter codiert.
- Migration von einem `<div>`-Element-basierten Design zu einer standardmäßigen `<table aria-label="Inbox Vision verwenden">`-formatierten Codebasis
  <caption>Inbox Vision verwenden</caption>
- [Editor-Blöcke (E-Mail)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=email) wurden für Kompaktheit neu codiert
- Der finale HTML-Code wird komprimiert, um Leerzeichen zwischen Tags zu entfernen
- Transparente Trennlinien werden automatisch in Inhalts-Padding umgewandelt
{% enddetails %}

## Weitere Anpassungen {#other-customizations}

Während Sie Ihre Drag-and-Drop-E-Mails weiter erstellen, können Sie jeden E-Mail-Body mithilfe einer Kombination dieser kreativen Details weiter anpassen, um die Aufmerksamkeit und das Interesse Ihrer Zielgruppe an Ihrer Nachricht zu wecken.

{% alert tip %}
Sie können ein benutzerdefiniertes Theme für Ihren Drag-and-Drop-Editor mithilfe der [globalen Stileinstellungen]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings/) erstellen.
{% endalert %}

### Automatische Breite für Bilder {#auto-width-images}

Bilder, die zu Ihrer E-Mail hinzugefügt werden, werden automatisch auf **Auto width** eingestellt. Um diese Einstellung anzupassen, deaktivieren Sie **Auto width** und passen Sie den Breitenprozentsatz nach Bedarf an.

![Option „Auto width“ im Content-Tab des Drag-and-Drop-Editors.]({% image_buster /assets/img/dnd/dnd1.png %})

### Farbschichtung {#color-layering}

Mit der Farbschichtung können Sie die Farbe des E-Mail-Hintergrunds, des Inhaltsbereichs und verschiedener Inhaltskomponenten ändern. Die Farbreihenfolge von vorne nach hinten ist: Inhaltskomponentenfarbe, Inhaltsbereich-Hintergrundfarbe und Hintergrundfarbe.

![Beispiel der Farbschichtung im Drag-and-Drop-Editor.]({% image_buster /assets/img/dnd/dnd2.png %})

### Inhalts-Padding {#content-padding}

![Block-Optionen für den Drag-and-Drop-Editor.]({% image_buster /assets/img/dnd/dnd3.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

Um das Padding anzupassen, scrollen Sie nach unten zu **Block Options** und wählen Sie **More Options**. Sie können Ihr Padding fein abstimmen, damit Ihre E-Mail genau richtig aussieht.

### Inhaltshintergrund {#content-background}

Sie können ein Hintergrundbild zu Ihrer Zeilenkonfiguration hinzufügen, um mehr Design und visuelle Inhalte in Ihre E-Mail-Campaign einzubinden.

### Sprachattribut {#language-attribute}

Sie können das Sprachattribut festlegen, indem Sie zum Tab **Settings** gehen und die gewünschte Sprache auswählen. Sie können auch das Nutzerattribut {%raw%} `{{${language}}}` {%endraw%} verwenden, wenn die Nachricht für Nutzer:innen mit dynamischen Sprachwerten bestimmt ist.

![Festlegen des Werts „Language“ für eine E-Mail.]({% image_buster /assets/img/dnd/language_setting_dnd.png %}){: style="max-width:70%;"}

### Personalisierung {#personalization}

![Optionen zum Hinzufügen von Personalisierung für den Drag-and-Drop-Editor.]({% image_buster /assets/img/dnd/dnd4.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

Grundlegendes Liquid wird im Drag-and-Drop-E-Mail-Editor unterstützt. Um Personalisierung zu Ihrer E-Mail hinzuzufügen:

1. Wählen Sie **Personalization** im Abschnitt **Content**.
2. Wählen Sie den Personalisierungstyp aus. Dazu gehören Standard-Attribute, Geräteattribute, angepasste Attribute und mehr.
3. Suchen Sie nach dem hinzuzufügenden Attribut.
4. Kopieren Sie Ihr generiertes Liquid-Snippet und fügen Sie es in Ihren E-Mail-Body ein.

Liquid-Personalisierung wird für Bildblöcke und Button-Link-Typ-Felder nicht unterstützt.

#### Dynamische Bilder {#dynamic-images}

Sie können dynamische Bilder in Ihre E-Mail-Nachrichten einbinden, indem Sie [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/#about-connected-content) oder [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/) in Ihrem Bildquellattribut verwenden. Anstelle eines statischen Bildes können Sie beispielsweise {% raw %} `https://example.com/images/?imageBanner={{first_name}}` {% endraw %} als Bild-URL einfügen, um den Vornamen einer Person im Bild einzubinden. Dies hilft, Ihre E-Mails für jede:n Nutzer:in zu personalisieren.

{% alert important %}
Ihre Bild-URL muss mit `https://` beginnen. Die Verwendung von `http://` führt zum Absturz Ihrer App.
{% endalert %}

### Textrichtung {#text-direction}

Beim Verfassen Ihrer Nachricht können Sie die Textrichtung zwischen links-nach-rechts und rechts-nach-links umschalten, indem Sie den entsprechenden Button **Text direction** auswählen. Sie können diese Option verwenden, wenn Sie Nachrichten in Sprachen wie Arabisch und Hebräisch erstellen.

![Menü des E-Mail-Drag-and-Drop-Editors mit Button zum Umschalten der Textausrichtung zwischen rechts-nach-links und links-nach-rechts.]({% image_buster /assets/img/dnd/dnd_template1.png %}){: style="max-width:50%;"}

Das endgültige Erscheinungsbild von Rechts-nach-links-Nachrichten hängt weitgehend davon ab, wie die Dienstanbieter sie darstellen. Best Practices für die Erstellung von Rechts-nach-links-Nachrichten, die so genau wie möglich angezeigt werden, finden Sie unter [Rechts-nach-links-Nachrichten erstellen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages/).

### HTML

#### HTML-Attribute für Links {#html-attributes-to-links}

![Der Abschnitt „Attributes“ mit dem Attribut „clicktracking“, das für einen Link deaktiviert ist.]({% image_buster /assets/img/dnd_custom_attributes.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Bei der Verwendung von Links, Buttons, Bildern und Videos im Drag-and-Drop-Editor wählen Sie **Add new attribute** unter **Attributes** im Abschnitt **Content**, um zusätzliche Informationen an HTML-Tags in E-Mails anzuhängen. Dies kann besonders nützlich für die Personalisierung, Segmentierung und Gestaltung von Nachrichten sein.

Ein häufiger Anwendungsfall ist das Einfügen eines Attributs in Ihren Anchor-Tag, um das Klick-Tracking beim Versand über Braze zu deaktivieren.

* **SendGrid:** `clicktracking = "off"`
* **SparkPost:** `data-msys-clicktrack = "0"`

Ein weiterer häufiger Anwendungsfall ist die Kennzeichnung bestimmter Links als Universal Links. Universal Links sind Links, die zu Ihrer App weiterleiten und Ihren Nutzer:innen ein integriertes Erlebnis bieten.

* **SendGrid:** `universal = "true"`
* **SparkPost:** `data-msys-sublink = "open-in-app"` (ein [benutzerdefinierter Sub-Pfad](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#custom-link-sub-paths) muss konfiguriert werden)

Informationen zur Einrichtung von Universal Links finden Sie unter [Universal Links und App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links/).

Alternativ können Sie eine Integration mit einem unserer Attribution-Partner wie [Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/) oder [AppsFlyer]({{site.baseurl}}/partners/message_orchestration/attribution/appsflyer/appsflyer/#email-deep-linking-and-click-tracking) nutzen, um Universal Links zu verwalten.

Schließlich stehen vordefinierte Attribute zur Verfügung, die Ihre Nachricht barrierefreier machen. Mehr erfahren Sie in unserem Artikel [Barrierefreie Nachrichten in Braze erstellen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility/).

#### Benutzerdefinierte Head-Tags {#custom-head-tags}

Verwenden Sie `<head>`-Tags, um CSS und Metadaten in Ihrer E-Mail-Nachricht hinzuzufügen. Beispielsweise können Sie diese Tags verwenden, um ein Stylesheet oder ein Favicon hinzuzufügen. Liquid wird in `<head>`-Tags unterstützt.

Alles, was außerhalb von `<head>`-Tags hinzugefügt wird, wird nach dem `<body>`-Tag in Ihrer E-Mail eingefügt. Das bedeutet, dass der hinzugefügte Inhalt in der E-Mail angezeigt wird.

##### Zulässige Tags und Attribute nach Tag {#allowed-tags-and-attributes-by-tag}

| Tag-Name | Beschreibung | Beispiel |
| --- | --- | --- |
| `base` | Gibt die Basis-URL für alle relativen URLs in der Nachricht an. | `<base href="https://example.com" target="_blank">` |
| `link`| Definiert Beziehungen zwischen der Nachricht und externen Ressourcen. | `<link href="styles.css" rel="stylesheet" type="text/css">` |
| `meta` | Stellt Metadaten wie Seitenbeschreibung oder Schlüsselwörter bereit. | `<meta name="description" content="Free Web tutorials">` |
| `style` | Bettet interne CSS-Stile ein. | `<style type="text/css" media="screen">body { font-size: 16px; }</style>` |
| `title` | Legt den Titel des Dokuments fest, der in Browser-Tabs angezeigt wird. | `<title>StyleRyde</title>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Zulässige Tags und Attribute nach Tag" }

| Tag | Attribut | Beschreibung | Beispiel |
| --- | --- | --- | --- |
| `base` | `href` | Basis-URL für relative URLs. | ```<base href="https://braze.com">``` |
| `base` | `target`| Standard-Ziel für alle Hyperlinks und Formulare. | ```<base target="_blank">``` |
| `link` | `href` | URL zur externen Ressource. | ```<link href="style.css">``` |
| `link` | `rel` | Definiert Beziehungen zwischen der aktuellen und der verlinkten Nachricht. | ```<link rel="stylesheet">``` |
| `link` | `type` | Typ der verlinkten Ressource. | ```<link type="text/css">``` |
| `link` | `sizes` | Gibt die Größen von Icons an. | ```<link rel="icon" sizes="32x32" href="favicon-32.png">``` |
| `link` | `media` | Gibt das Medium oder Gerät an, für das Stile gelten. | ```<link rel="stylesheet" media="screen" href="style.css">``` |
| `meta` | `name` | Legt den Titel des Dokuments fest, der in Browser-Tabs angezeigt wird. | ```<meta name="viewport" content="width=device-width, initial-scale=1">``` |
| `meta` | `content` | Legt den Titel des Dokuments fest, der in Browser-Tabs angezeigt wird. | ```<meta name="description" content="Page about our newest products">``` |
| `meta` | `charset` | Deklariert die Zeichenkodierung. | ```<meta charset="UTF-8">``` |
| `meta` | `property` | Legt den Titel des Dokuments fest, der in Browser-Tabs angezeigt wird. | ```<meta property="og:title" content="Website title">``` |
| `style` | `type` | MIME-Typ des Stilinhalts. | {% raw %}```<style type="text/css">p { color: red; }</style>```{% endraw %} |
| `style` | `media` | Gibt das Medium oder Gerät an, für das Stile gelten. | ```<style media="print">body { font-size: 12pt; }</style>``` |
| `title` | Keine Attribute | Das `title`-Tag akzeptiert keine Attribute. | ```<title>Kitchenerie</title>``` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Zulässige Tags und Attribute nach Tag" }

{% alert note %}
Link-Namen können bis zu 63 Bytes lang sein und werden automatisch abgeschnitten, wenn sie das Limit überschreiten.
{% endalert %}