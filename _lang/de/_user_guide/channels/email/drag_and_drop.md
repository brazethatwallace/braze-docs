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

Der Drag-and-Drop-Editor verwendet [Inhalt](#content) und [Zeilen](#rows) als die beiden wichtigsten Komponenten, um Ihren Workflow zu vereinfachen – ohne zusätzliche Verwendung von HTML.

<table aria-label="Über den Editor" style="width: 100%; table-layout: fixed;">
    <caption>Inhalt- und Zeilen-Editor-Komponenten</caption>
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

**Inhalt** umfasst eine Reihe von Kacheln, die verschiedene Arten von Inhalten darstellen, die Sie in Ihrer Nachricht verwenden können. Diese sind in drei Kategorien unterteilt: Grundlegend, Medien und Erweitert.

{% tabs %}
{% tab Grundlegend %}

Grundlegende Blöcke bilden die Basis Ihrer E-Mail. Mit diesen Blöcken können Sie eines der folgenden Elemente in Ihren E-Mail-Text einfügen:

- Titel
- Absatz
- Liste
- Button
- Trennlinie
- Abstandshalter

{% endtab %}
{% tab Medien %}

Mit Medienblöcken können Sie verschiedene visuelle Inhalte hinzufügen, z. B. Bilder, Videos, Social-Media-Icons und -Links sowie anpassbare Icons.

{% endtab %}
{% tab Erweitert %}

Obwohl der Drag-and-Drop-Editor Ihren Workflow mit diesen Blöcken vereinfacht, können Sie auch erweiterte Blöcke verwenden, um HTML einzufügen oder ein Menü in Ihren E-Mail-Text einzubauen. Beachten Sie, dass die Verwendung von eigenem HTML die Darstellung der Nachricht beeinflussen kann.

{% endtab %}
{% endtabs %}

### Zeilen {#rows}

**Zeilen** sind strukturelle Einheiten, die die horizontale Zusammensetzung eines Abschnitts der Nachricht mithilfe von Spalten definieren. Sie können entweder leere Zeilen oder [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) verwenden. Durch die Verwendung von mehr als einer Spalte können Sie verschiedene Inhaltselemente nebeneinander platzieren. So können Sie alle benötigten strukturellen Elemente zu Ihrer Nachricht hinzufügen, unabhängig davon, welches Template Sie zu Beginn ausgewählt haben.

#### Bilder in Textblöcken verschachteln {#nesting-images-inside-text-blocks}

Sie können im Drag-and-Drop-Editor kein Bild innerhalb eines Absatzes oder eines anderen Textblocks verschachteln. Um ein Bild neben oder innerhalb eines Text-Layouts zu platzieren, verwenden Sie Spalten in einer **Zeile**: zum Beispiel eine mehrspaltige Zeile auf dem Desktop mit **Auf Mobilgeräten ausblenden** für diese Zeile und eine separate Zeile nur für Mobilgeräte (mit **Auf Desktop ausblenden** und **Auf Mobilgeräten nicht stapeln** nach Bedarf), damit Bild und Text auf kleinen Bildschirmen sauber ausgerichtet sind.

#### Cards Style {#cards-style}

**Cards Style** ist eine Zeileneigenschaft, mit der Sie Abstände zwischen Spalten hinzufügen und deren Ecken abrunden können. Mit der Card-Style-Formatierung können Sie visuell ansprechendere Layouts erstellen, um Ihre wichtigsten Inhalte hervorzuheben – etwa neue Produkt-Features, Testimonials, Sonderangebote, Neuigkeiten und mehr.

## Den Drag-and-Drop-Editor verwenden {#using-the-drag-and-drop-editor}

Sie sind sich nicht sicher, ob Ihre E-Mail-Nachricht über eine Campaign oder einen Canvas gesendet werden soll? Campaigns eignen sich besser für einzelne, gezielte Messaging-Kampagnen, während Canvases besser für mehrstufige User-Journeys geeignet sind.

{% alert note %}
Sie können eine Drag-and-Drop-E-Mail aus einer Campaign oder einem Canvas nicht direkt unter **Templates** > **E-Mail-Templates** als E-Mail-Template speichern. Erstellen Sie Ihre E-Mail zuerst unter **Templates**, oder lesen Sie [Kann ich meine Drag-and-Drop-E-Mail nach dem Erstellen in meiner Campaign oder meinem Canvas als Template speichern?]({{site.baseurl}}/user_guide/channels/email/drag_and_drop/faq#can-i-save-my-drag-and-drop-email-as-a-template-after-i-build-it-within-my-campaign-or-canvas), um ein Drag-and-Drop-Template neu zu erstellen oder HTML mit **Datei herunterladen** zu exportieren.
{% endalert %}

Nachdem Sie ausgewählt haben, wo Sie Ihre Nachricht erstellen möchten, gehen wir die Schritte zum Erstellen einer Drag-and-Drop-E-Mail durch.

### Schritt 1: Template auswählen {#step-1-select-your-template}

Nachdem Sie den Drag-and-Drop-Editor als Bearbeitungserfahrung ausgewählt haben, können Sie:

- Mit einem leeren Template beginnen.
- Ein vorgefertigtes Braze Drag-and-Drop-E-Mail-Template verwenden.
- Ein gespeichertes Drag-and-Drop-E-Mail-Template verwenden.

{% alert note %}
Um ein vorhandenes benutzerdefiniertes HTML-Template oder von Drittanbietern erstellte Templates zu verwenden, müssen Sie das Template neu erstellen, indem Sie zu **Content** > **E-Mail** navigieren und **Drag-And-Drop Editor** als Bearbeitungserfahrung auswählen.
{% endalert %}

Sie können auch über den Abschnitt **Templates** auf alle Templates zugreifen.

Nachdem Sie Ihr Template ausgewählt haben, sehen Sie unter **E-Mail-Varianten** eine Übersicht Ihrer E-Mail, die die Versandinformationen und den E-Mail-Text enthält.

Wählen Sie dann **E-Mail-Text bearbeiten**, um mit der Gestaltung der E-Mail-Struktur im Drag-and-Drop-Editor zu beginnen.

![Der Abschnitt „E-Mail-Varianten“ mit einem Beispiel-E-Mail-Text.]({% image_buster /assets/img/dnd/dnd_emailvariant.png %})

### Schritt 2: E-Mail erstellen {#step-2-build-your-email}

Die Drag-and-Drop-Bearbeitungserfahrung ist in drei Abschnitte unterteilt: **Sendeeinstellungen**, **Content** und **Vorschau und Test**. Der eigentliche Aufbau Ihres E-Mail-Textes findet im Abschnitt **Content** statt. Bevor Sie mit dem Erstellen beginnen, ist es wichtig, die Schlüsselkomponenten zu verstehen, die Ihre E-Mail-Erstellung leiten. Falls Sie diese wiederholen möchten, lesen Sie [Über den Editor](#about-the-editor).

Wenn Sie bereit sind, verwenden Sie die Drag-and-Drop-Content-Blöcke, um Ihre E-Mail zu erstellen.

1. Wählen Sie das Panel **Zeilen**. Ziehen Sie die Zeilenkonfigurationen per Drag-and-Drop in den Haupteditor. Dies legt das Layout Ihres E-Mail-Contents fest.
- Beachten Sie, dass neue Konfigurationen an den Anfang oder das Ende eines vorhandenen Abschnitts gezogen werden müssen.
- Wenn Sie eine Zeilenkonfiguration auswählen, werden die **Zeileneigenschaften** zur weiteren Anpassung von Hintergrundfarben, Bildern und angepassten Spaltengrößen angezeigt.
2. Wählen Sie das Panel **Content**. Ziehen Sie die gewünschten Content-Kacheln per Drag-and-Drop in die Zeilenkomponenten.
- Sie können auch jede der **Content**-Kacheln in den Haupteditor ziehen. Dadurch wird automatisch eine Zeile für die Kachel erstellt.
- Sie können die Kachel weiter verfeinern, indem Sie sie auswählen und die Felder unter **Content-Eigenschaften** und **Blockoptionen** anpassen. Dazu gehören die Bearbeitung von Zeichenabstand, Padding, Zeilenhöhe und mehr.

Unter [Weitere Anpassungen](#other-customizations) finden Sie zusätzliche Möglichkeiten, Ihre Drag-and-Drop-E-Mail weiter anzupassen.

Während Sie Ihre E-Mail erstellen, können Sie zwischen einer Desktop- und einer mobilen Ansicht wechseln, um eine Vorschau zu sehen, wie Ihre E-Mail-Nachricht für Ihre Nutzergruppen aussehen wird. So stellen Sie sicher, dass Ihr Content responsiv ist, und können unterwegs alle notwendigen Anpassungen vornehmen.

{% alert tip %}
Benötigen Sie Hilfe beim Erstellen großartiger Texte? Probieren Sie den [KI-Textassistenten]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy) aus. Geben Sie einen Produktnamen oder eine Beschreibung ein, und die KI generiert menschenähnliche Marketingtexte für Ihr Messaging.

![Button für den Textassistenten, im Content-Panel neben den Stileinstellungen im Drag-and-Drop-Editor.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_dnd.png %})
{% endalert %}

### Schritt 3: Versandinformationen hinzufügen {#step-3-add-your-sending-information}

Sobald Sie Ihre E-Mail-Nachricht fertig gestaltet und erstellt haben, ist es an der Zeit, Ihre Versandinformationen im Abschnitt **Sendeeinstellungen** hinzuzufügen.

{% multi_lang_include email/sending_info_steps.md %}

{% multi_lang_include alerts/tip_alerts.md alert='Liquid email display name and reply-to address' %}

Eine Vorschau im rechten Panel wird mit den von Ihnen hinzugefügten Versandinformationen befüllt. Diese Informationen können auch aktualisiert werden, indem Sie zu **Einstellungen** > **E-Mail-Einstellungen** > **Sendekonfiguration** navigieren.

#### E-Mail-Anhänge hinzufügen {#add-email-attachments}

Unter **Sendeeinstellungen** > **Erweitert** können Sie E-Mail-Anhänge mit den folgenden Methoden hinzufügen:

{% multi_lang_include email/attachment_upload_options.md %}

Spezifische Best Practices finden Sie unter [E-Mail-Richtlinien]({{site.baseurl}}/user_guide/channels/email/best_practices/email_guidelines).

#### E-Mail-Header personalisieren (erweitert) {#personalize-your-email-header-advanced}

Unter **Sendeeinstellungen** können Sie Personalisierungen für E-Mail-Header und E-Mail-Extras hinzufügen, mit denen Sie zusätzliche Daten an andere E-Mail-Anbieter zurücksenden können. Die Personalisierung eines E-Mail-Headers, z. B. durch Einfügen des Namens der Empfängerin oder des Empfängers, kann ebenfalls dazu beitragen, die Wahrscheinlichkeit zu erhöhen, dass Ihre E-Mail geöffnet wird.

{% alert note %}
Erweiterte Funktionen werden im Campaign- oder Canvas-Composer angezeigt. In den erweiterten Funktionen können Sie Ihre Inline-CSS-Einstellung ändern und Header- oder zusätzliche Schlüssel-Wert-Paare eingeben (sofern konfiguriert).
{% endalert %}

### Schritt 4: E-Mail testen {#step-4-test-your-email}

Nachdem Sie Ihre Versandinformationen hinzugefügt haben, ist es an der Zeit, Ihre E-Mail zu testen.

{% alert tip %}
Wenn die E-Mail im Editor anders aussieht als in der Vorschau oder beim Testversand, überprüfen Sie, ob alle Tags geschlossen sind, Bildattribute Werte haben und Hintergrundbilder an den Rändern nicht unscharf sind.
{% endalert %}

Gehen Sie zum Abschnitt **Vorschau und Test**. Hier haben Sie die Möglichkeit, eine Vorschau Ihrer E-Mail als Nutzer:in anzuzeigen oder eine Testnachricht zu senden. Dieser Abschnitt enthält auch [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision), mit dem Sie überprüfen können, ob Ihre E-Mail in verschiedenen mobilen und Web-Clients korrekt dargestellt wird.

{% alert tip %}
Sie können auch den Schalter **Dark-Mode-Vorschau** im Vorschau-Panel verwenden, um Ihren E-Mail-Text im Dark Mode anzuzeigen und Ihre E-Mail bei Bedarf anzupassen.
{% endalert %}

Da Sie drei verschiedene Versionen derselben E-Mail im eigentlichen Editor, in Inbox Vision und als tatsächliche Test-E-Mail anzeigen können, ist es wichtig, die Details über alle Ihre Plattformen hinweg abzugleichen.

#### Vorschau und Testversand {#preview-and-test-send}

Unter dem Tab **Vorschau als Nutzer:in** können Sie die folgenden Nutzertypen auswählen, um eine Vorschau Ihrer Nachricht anzuzeigen.

- **Zufällige:r Nutzer:in:** Braze wählt zufällig eine Person aus der Datenbank aus und zeigt die E-Mail-Vorschau basierend auf deren Attributen oder Ereignisinformationen an.
- **Nutzer:in auswählen:** Sie können eine bestimmte Person anhand ihrer E-Mail-Adresse oder externen ID auswählen. Die E-Mail wird basierend auf den Attributen und Ereignisinformationen dieser Person in der Vorschau angezeigt.
- **Angepasste:r Nutzer:in:** Sie können eine Person anpassen. Braze stellt Eingabefelder für alle verfügbaren Attribute und Ereignisse bereit. Sie können beliebige Informationen eingeben, die Sie in der Vorschau-E-Mail sehen möchten.

{% alert note %}
Die zufällige Person kann, muss aber nicht Teil Ihrer Segmentierungskriterien sein. Die Segmentierung wird erst danach ausgewählt, daher kennt Braze Ihre Zielgruppe zu diesem Zeitpunkt noch nicht.
{% endalert %}

Sie können auch **Vorschaulink kopieren** auswählen, um einen teilbaren Vorschaulink zu generieren und zu kopieren, der zeigt, wie die E-Mail für eine zufällige Person aussehen wird. Weitere Informationen finden Sie unter [Teilbare Vorschau]({{site.baseurl}}/user_guide/messaging/governance/shareable_preview).

![E-Mail-Vorschau mit einem Button zum Kopieren des Vorschaulinks und zum Kopieren des generierten Links.]({% image_buster /assets/img/dnd_email_link_preview.png %})

#### Inbox Vision verwenden {#use-inbox-vision}

Inbox Vision ermöglicht es Ihnen, Ihre E-Mail-Campaigns aus der Perspektive von E-Mail-Clients und mobilen Geräten zu betrachten. Um Ihre E-Mail-Nachricht mit Inbox Vision zu testen, wählen Sie **Inbox Vision** im Abschnitt **Vorschau und Test** und klicken Sie auf **Inbox Vision ausführen**.

Es ist wichtig, die feineren Details Ihrer E-Mail-Nachricht zu testen und zu überprüfen. Zum Beispiel können Hintergrundbilder in E-Mail-Nachrichten manchmal weiße Linien oder Trennungen zwischen Bildern verursachen, oder Clients wie Windows Outlook zeigen Hintergrundbilder möglicherweise nicht an. Inbox Vision kann helfen, diese Abweichungen zwischen Clients zu identifizieren. In diesem Szenario sollten Sie eine Fallback-Hintergrundfarbe setzen, damit diese Bilder wie erwartet dargestellt werden.

Weitere Informationen finden Sie unter [Testnachrichten senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=email).

Nachdem Sie den Drag-and-Drop-Editor zum Gestalten und Erstellen Ihrer E-Mail-Nachricht verwendet haben, fahren Sie mit dem [Erstellen]({{site.baseurl}}/user_guide/channels/email/html_editor#step-4-build-the-remainder-of-your-campaign-or-canvas) des restlichen Teils Ihrer Campaign oder Ihres Canvas fort.

{% details Über die aktualisierte HTML-Engine %}
Die zugrunde liegende Engine, die HTML aus dem Drag-and-Drop-Editor erzeugt, wurde optimiert und aktualisiert, was zu Vorteilen bei der HTML-Dateikomprimierung und beim Rendering führt.

Die durchschnittliche Größe der exportierten HTML-Daten wurde reduziert, was zu schnellerem Laden und Rendering, weniger mobilem Clipping und geringerem Ressourcenverbrauch führt.

Das HTML-Rendering wurde durch die folgenden Updates verbessert, die die Anzahl der bedingten Kommentare und CSS-Media-Queries minimieren. Dadurch sind HTML-Dateien kleiner und effizienter codiert.
- Migration von einem `<div>`-elementbasierten Design zu einer standardmäßigen `<table aria-label="Inbox Vision verwenden">`-formatierten Codebasis
  <caption>Inbox Vision verwenden</caption>
- [Editor-Blöcke (E-Mail)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=email) wurden für Kürze neu programmiert
- Der finale HTML-Code wird komprimiert, um Leerzeichen zwischen Tags zu entfernen
- Transparente Trennlinien werden automatisch in Content-Padding umgewandelt
{% enddetails %}

## Weitere Anpassungen {#other-customizations}

Während Sie Ihre Drag-and-Drop-E-Mails weiter erstellen, können Sie jeden E-Mail-Text mithilfe einer Kombination dieser kreativen Details weiter anpassen, um die Aufmerksamkeit und das Interesse Ihrer Zielgruppe an Ihrer Nachricht zu wecken.

{% alert tip %}
Sie können ein benutzerdefiniertes Theme für Ihren Drag-and-Drop-Editor erstellen, indem Sie [globale Stileinstellungen]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings) verwenden.
{% endalert %}

### Automatische Breite für Bilder {#auto-width-images}

Bilder, die Sie Ihrer E-Mail hinzufügen, werden automatisch auf **Automatische Breite** eingestellt. Um diese Einstellung anzupassen, deaktivieren Sie **Automatische Breite** und passen Sie den Breitenprozentsatz nach Bedarf an.

![Option für automatische Breite im Tab „Inhalt“ des Drag-and-Drop-Editors.]({% image_buster /assets/img/dnd/dnd1.png %})

### Farbschichtung {#color-layering}

Mit der Farbschichtung können Sie die Farbe des E-Mail-Hintergrunds, des Inhaltsbereichs und verschiedener Inhaltskomponenten ändern. Die Farbreihenfolge von vorne nach hinten ist: Farbe der Inhaltskomponente, Hintergrundfarbe des Inhaltsbereichs und Hintergrundfarbe.

![Beispiel für die Farbschichtung im Drag-and-Drop-Editor.]({% image_buster /assets/img/dnd/dnd2.png %})

### Inhalts-Padding {#content-padding}

![Blockoptionen für den Drag-and-Drop-Editor.]({% image_buster /assets/img/dnd/dnd3.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

Um das Padding anzupassen, scrollen Sie nach unten zu **Blockoptionen** und wählen Sie **Mehr Optionen**. Sie können Ihr Padding fein abstimmen, damit Ihre E-Mail genau richtig aussieht.

### Inhaltshintergrund {#content-background}

Sie können Ihrer Zeilenkonfiguration ein Hintergrundbild hinzufügen, sodass Sie mehr Design- und visuelle Inhalte in Ihre E-Mail-Kampagne einbinden können.

### Sprachattribut {#language-attribute}

Sie können das Sprachattribut festlegen, indem Sie zum Tab **Einstellungen** gehen und die gewünschte Sprache auswählen. Sie können auch das Nutzerattribut {%raw%} `{{${language}}}` {%endraw%} verwenden, wenn die Nachricht für Nutzer:innen mit dynamischen Sprachwerten bestimmt ist.

![Festlegen des „Sprache“-Werts für eine E-Mail.]({% image_buster /assets/img/dnd/language_setting_dnd.png %}){: style="max-width:70%;"}

### Personalisierung {#personalization}

![Optionen zum Hinzufügen von Personalisierung im Drag-and-Drop-Editor.]({% image_buster /assets/img/dnd/dnd4.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

Einfaches Liquid wird im Drag-and-Drop-E-Mail-Editor unterstützt. Um Personalisierung zu Ihrer E-Mail hinzuzufügen:

1. Wählen Sie **Personalisierung** im Abschnitt **Inhalt** aus.
2. Wählen Sie den Personalisierungstyp. Dazu gehören Standard-Attribute, Geräteattribute, angepasste Attribute und mehr.
3. Suchen Sie nach dem hinzuzufügenden Attribut.
4. Kopieren Sie Ihr generiertes Liquid-Snippet und fügen Sie es in Ihren E-Mail-Text ein.

Liquid-Personalisierung wird für Bildblöcke und Button-Link-Typ-Felder nicht unterstützt.

#### Dynamische Bilder {#dynamic-images}

Sie können dynamische Bilder in Ihre E-Mail-Nachrichten einbinden, indem Sie [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) oder [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) in Ihrem Bildquell-Attribut verwenden. Anstelle eines statischen Bildes können Sie beispielsweise {% raw %} `https://example.com/images/?imageBanner={{first_name}}` {% endraw %} als Bild-URL einfügen, um den Vornamen eines Nutzers/einer Nutzerin in das Bild einzubinden. Dies hilft Ihnen, Ihre E-Mails für jede:n Nutzer:in zu personalisieren.

{% alert important %}
Ihre Bild-URL muss mit `https://` beginnen. Die Verwendung von `http://` führt zum Absturz Ihrer App.
{% endalert %}

### Textrichtung {#text-direction}

Beim Verfassen Ihrer Nachricht können Sie die Textrichtung zwischen links-nach-rechts und rechts-nach-links umschalten, indem Sie den entsprechenden **Textrichtung**-Button auswählen. Diese Option kann beim Erstellen von Nachrichten in Sprachen wie Arabisch und Hebräisch nützlich sein.

![Menü des Drag-and-Drop-E-Mail-Editors mit Button zum Umschalten der Textausrichtung zwischen rechts-nach-links und links-nach-rechts.]({% image_buster /assets/img/dnd/dnd_template1.png %}){: style="max-width:50%;"}

Das endgültige Erscheinungsbild von Rechts-nach-links-Nachrichten hängt weitgehend davon ab, wie E-Mail-Anbieter sie darstellen. Best Practices zum Erstellen von Rechts-nach-links-Nachrichten, die so genau wie möglich angezeigt werden, finden Sie unter [Rechts-nach-links-Nachrichten erstellen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

### HTML

#### HTML-Attribute für Links {#html-attributes-to-links}

![Der Abschnitt „Attribute“ mit dem deaktivierten Attribut „clicktracking“ für einen Link.]({% image_buster /assets/img/dnd_custom_attributes.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Wenn Sie Links, Buttons, Bilder und Videos im Drag-and-Drop-Editor verwenden, wählen Sie **Neues Attribut hinzufügen** unter **Attribute** im Abschnitt **Inhalt** aus, um zusätzliche Informationen an HTML-Tags in E-Mails anzuhängen. Dies kann besonders nützlich für Nachrichtenpersonalisierung, Segmentierung und Styling sein.

Ein häufiger Anwendungsfall ist das Deaktivieren des Klick-Trackings für bestimmte Links beim Versand über Braze. Dies können Sie auf zwei Arten tun:

- **Link-Modul-Attribute verwenden:** Wählen Sie ein Link-Element aus (z. B. einen Button oder ein Link-Modul) und verwenden Sie dann **Neues Attribut hinzufügen** unter **Attribute**, um hinzuzufügen:
  - Für SendGrid verwenden Sie `clicktracking` als Name und `off` als Wert.
  - Für SparkPost verwenden Sie `data-msys-clicktrack` als Name und `0` als Wert.
- **HTML-Block verwenden:** Fügen Sie einen HTML-Block ein und integrieren Sie das Klick-Tracking-Attribut direkt in Ihren Anchor-Tag-Code:
  - Für SendGrid verwenden Sie `<a href="your-url" clicktracking="off">Linktext</a>`.
  - Für SparkPost verwenden Sie `<a href="your-url" data-msys-clicktrack="0">Linktext</a>`.

Ein weiterer häufiger Anwendungsfall ist das Kennzeichnen bestimmter Links als Universal Links. Universal Links sind Links, die zu Ihrer App weiterleiten und Ihren Nutzer:innen ein integriertes Erlebnis bieten.

* **SendGrid:** `universal = "true"`
* **SparkPost:** `data-msys-sublink = "open-in-app"` (ein [benutzerdefinierter Sub-Pfad](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#custom-link-sub-paths) muss konfiguriert werden)

Informationen zum Einrichten von Universal Links finden Sie unter [Universal Links und App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links).

Alternativ können Sie einen unserer Attributionspartner integrieren, wie z. B. [Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking) oder [AppsFlyer]({{site.baseurl}}/partners/message_orchestration/deeplinking/appsflyer/appsflyer#integrate-appsflyer-with-braze-for-deep-linking), um Universal Links zu verwalten.

Schließlich stehen vordefinierte Attribute zur Verfügung, die Ihre Nachricht barrierefrei gestalten. Erfahren Sie mehr in unserem Artikel [Barrierefreie Nachrichten in Braze erstellen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility), einschließlich [wie E-Mail-Clients Alt-Text anzeigen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#how-email-clients-display-alt-text).

#### Benutzerdefinierte Head-Tags {#custom-head-tags}

Verwenden Sie `<head>`-Tags, um CSS und Metadaten in Ihre E-Mail-Nachricht einzufügen. Sie können diese Tags beispielsweise verwenden, um ein Stylesheet oder Favicon hinzuzufügen. Liquid wird in `<head>`-Tags unterstützt.

Alles, was außerhalb von `<head>`-Tags hinzugefügt wird, wird nach dem `<body>`-Tag in Ihrer E-Mail eingefügt. Das bedeutet, dass der hinzugefügte Inhalt in der E-Mail angezeigt wird.

##### Zulässige Tags und Attribute nach Tag {#allowed-tags-and-attributes-by-tag}

| Tag-Name | Beschreibung | Beispiel |
| --- | --- | --- |
| `base` | Gibt die Basis-URL für alle relativen URLs in der Nachricht an. | `<base href="https://example.com" target="_blank">` |
| `link`| Definiert Beziehungen zwischen der Nachricht und externen Ressourcen. | `<link href="styles.css" rel="stylesheet" type="text/css">` |
| `meta` | Stellt Metadaten wie Seitenbeschreibung oder Schlüsselwörter bereit. | `<meta name="description" content="Free Web tutorials">` |
| `style` | Bettet interne CSS-Styles ein. | `<style type="text/css" media="screen">body { font-size: 16px; }</style>` |
| `title` | Legt den Titel des Dokuments fest, der in Browser-Tabs angezeigt wird. | `<title>StyleRyde</title>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Zulässige Tags und Attribute nach Tag" }

| Tag | Attribut | Beschreibung | Beispiel |
| --- | --- | --- | --- |
| `base` | `href` | Basis-URL für relative URLs. | ```<base href="https://braze.com">``` |
| `base` | `target`| Standardziel für alle Hyperlinks und Formulare. | ```<base target="_blank">``` |
| `link` | `href` | URL zur externen Ressource. | ```<link href="style.css">``` |
| `link` | `rel` | Definiert Beziehungen zwischen der aktuellen und der verlinkten Nachricht. | ```<link rel="stylesheet">``` |
| `link` | `type` | Typ der verlinkten Ressource. | ```<link type="text/css">``` |
| `link` | `sizes` | Gibt die Größen von Icons an. | ```<link rel="icon" sizes="32x32" href="favicon-32.png">``` |
| `link` | `media` | Gibt das Medium oder Gerät an, für das Styles gelten. | ```<link rel="stylesheet" media="screen" href="style.css">``` |
| `meta` | `name` | Legt den Titel des Dokuments fest, der in Browser-Tabs angezeigt wird. | ```<meta name="viewport" content="width=device-width, initial-scale=1">``` |
| `meta` | `content` | Legt den Titel des Dokuments fest, der in Browser-Tabs angezeigt wird. | ```<meta name="description" content="Page about our newest products">``` |
| `meta` | `charset` | Deklariert die Zeichenkodierung. | ```<meta charset="UTF-8">``` |
| `meta` | `property` | Legt den Titel des Dokuments fest, der in Browser-Tabs angezeigt wird. | ```<meta property="og:title" content="Website title">``` |
| `style` | `type` | MIME-Typ des Style-Inhalts. | {% raw %}```<style type="text/css">p { color: red; }</style>```{% endraw %} |
| `style` | `media` | Gibt das Medium oder Gerät an, für das Styles gelten. | ```<style media="print">body { font-size: 12pt; }</style>``` |
| `title` | Keine Attribute | Das `title`-Tag akzeptiert keine Attribute. | ```<title>Kitchenerie</title>``` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Zulässige Tags und Attribute nach Tag" }

{% alert note %}
Link-Namen können bis zu 63 Bytes lang sein und werden automatisch gekürzt, wenn sie das Limit überschreiten.
{% endalert %}