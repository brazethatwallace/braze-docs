---
nav_title: Landing-Pages erstellen
article_title: Landing-Pages erstellen
description: "Dieser Artikel beschreibt, wie Sie Landing-Pages in Braze mit dem Drag-and-Drop-Editor erstellen und anpassen."
page_order: 0
---

# Landing-Pages erstellen {#create-landing-pages}

> Erfahren Sie, wie Sie mit dem Drag-and-Drop-Editor eine Landing-Page erstellen und anpassen, um Ihre Zielgruppe zu vergrößern und Präferenzen direkt in Braze zu erfassen.

## Voraussetzungen {#prerequisites}

Um auf den Landing-Page-Builder zugreifen zu können, benötigen Sie [bestimmte Berechtigungen]({{site.baseurl}}/user_guide/messaging/landing_pages#prerequisites). Falls Sie keinen Zugriff haben, wenden Sie sich an Ihre Braze-Admins.

## Eine Landing-Page erstellen {#creating-a-landing-page}

### Schritt 1: Einen neuen Entwurf erstellen {#step-1-create-a-new-draft}

Gehen Sie zu **Messaging** > **Landing Pages** und wählen Sie **Create landing page**. Sie können auch den Namen einer bestehenden Landing-Page auswählen, um diese zu duplizieren oder Änderungen vorzunehmen.

### Schritt 2: Seitendetails eingeben {#step-2-enter-the-page-details}

Fügen Sie interne und öffentlich sichtbare Details hinzu, die Ihnen helfen, Ihre Landing-Page zu organisieren, zu branden und zu teilen.

#### Allgemeine Details {#general-details}

Geben Sie einen Namen und eine Beschreibung für die Landing-Page ein. Diese Details werden verwendet, um die Seite in Ihrem internen Workspace zu suchen. Sie sind für Ihre Kund:innen nicht sichtbar.

#### Website-Details {#site-details}

Richten Sie Metatags ein, um das Erscheinungsbild Ihrer Seite im Browser-Tab anzupassen und für Suchmaschinenergebnisse zu optimieren. Diese sind für Ihre Kund:innen sichtbar.

Wir empfehlen die folgenden Best Practices:

| Feld | Beschreibung | Empfehlungen |
| --- | --- | --- |
| Website-Titel | Der Titel, der im Browser-Tab angezeigt wird. | Verwenden Sie bis zu 60 Zeichen. |
| Meta-Beschreibung | Ein Textausschnitt, der in Suchergebnissen angezeigt wird. | Verwenden Sie zwischen 140 und 160 Zeichen. |
| Favicon | Das Symbol, das neben dem Website-Titel im Browser-Tab erscheint. | Verwenden Sie ein Seitenverhältnis von 1:1 und einen unterstützten Dateityp wie PNG, JPEG oder ICO. |
| Seiten-URL | Dies ist der URL-Pfad zu Ihrer Landing-Page. Dieser Wert wird auch referenziert, wenn Sie [Landing-Page-Liquid-Tags]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) verwenden, die Sie in eine Nachricht einbetten können, um automatisch zu erkennen, wenn Nutzer:innen Ihr Formular absenden. | Dieser Wert muss innerhalb Ihres Workspace eindeutig sein. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Website-Details" }

### Schritt 3: Die Seite anpassen {#step-3-customize-the-page}

Falls noch nicht geschehen, wählen Sie **Als Entwurf speichern**. Um mit der Anpassung Ihrer Seite zu beginnen, wählen Sie **Edit landing page**. Der Drag-and-Drop-Editor wird mit einem Standard-Template vorgeladen, das Sie an Ihren Anwendungsfall anpassen können.

![Eine Beispiel-Landing-Page, die im Drag-and-Drop-Editor erstellt wird.]({% image_buster /assets/img/landing_pages/template.png %})

Der Editor verwendet zwei Arten von Komponenten für die Gestaltung von Landing-Pages: Basisblöcke und Formularblöcke. Alle Blöcke müssen in einer Zeile platziert werden. Eine vollständige Referenz aller Blöcke und Eigenschaften finden Sie unter [Editor-Blöcke (Landing-Pages)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages).

![Der Abschnitt „Build“ mit „Rows“ und „Form Blocks“.]({% image_buster /assets/img/landing_pages/dnd.png %}){: style="max-width:35%;"}

{% tabs %}
{% tab Basisblöcke %}

Mit diesen Blöcken können Sie Inhalte hinzufügen und das Layout Ihrer Landing-Page anpassen.

| Blocktyp | Beschreibung |
|-------------|-------------|
| Titel | Ein Textblock zum Hinzufügen einer Überschrift oder eines Titels zu Ihrem Inhalt. Nützlich für die Strukturierung von Abschnitten und die Verbesserung der Lesbarkeit. |
| Absatz | Ein Textblock für längere Beschreibungen oder zusätzlichen Kontext. Unterstützt Rich-Text-Formatierung. |
| Button | Ein klickbares Element, das Nutzer:innen zu einer bestimmten Aktion weiterleitet, z. B. zum Öffnen eines Links oder zum Absenden eines Formulars. |
| Optionsfeld | Fügt eine Liste von Optionen hinzu, aus denen Nutzer:innen eine auswählen können. Bei der Übermittlung wird das zugehörige angepasste Attribut im Nutzerprofil protokolliert. |
| Bild | Ein Block zur Anzeige von Bildern. Sie können ein Bild hochladen oder eine URL angeben, um eine externe Quelle zu referenzieren. |
| Link | Ein Hyperlink, auf den Nutzer:innen klicken können, um zu einer bestimmten URL zu navigieren. Kann in Text eingebettet oder eigenständig verwendet werden. |
| Abstandshalter | Ein unsichtbarer Block, der vertikalen Abstand zwischen Elementen hinzufügt, um Layout und Lesbarkeit zu verbessern. |
| Angepasster Code | Ein Block, mit dem Sie angepasstes HTML, CSS oder JavaScript für erweiterte Anpassungen einfügen und ausführen können. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Die Seite anpassen" }

#### Span-Text {#span-text}

Um bestimmte Stile auf Textblöcke ohne angepassten Code anzuwenden, markieren Sie den Text, den Sie gestalten möchten, und wählen Sie dann **Wrap with span for style**.

![Textfeld mit verschiedenen stilisierten Textabschnitten, z. B. unterschiedlichen Schriftgrößen und Farben, und einem hervorgehobenen Abschnitt, der eine Symbolleiste mit der Option „Wrap with span for style“ anzeigt.]({% image_buster /assets/img/landing_pages/wrap_with_span.png %}){: style="max-width:50%;"}

Passen Sie die Span-Eigenschaften an, um Ihre Textgestaltung zu aktualisieren. Dazu gehören:

- Schriftfamilie, -stärke, -größe
- Zeilenhöhe
- Zeichenabstand
- Textausrichtung und -farbe
- Block-Padding

![Panel mit Span-Eigenschaften und verschiedenen Optionen zur Aktualisierung.]({% image_buster /assets/img/landing_pages/span_properties.png %}){: style="max-width:35%;"}


{% endtab %}
{% tab Formularblöcke %}

Mit diesen Blöcken können Sie ein Formular erstellen, das von Nutzer:innen übermittelte Daten mit deren Profil in Braze verknüpft. Beachten Sie: Wenn Sie Formularblöcke verwenden, müssen Sie auch eine zusätzliche Landing-Page für den Bestätigungsstatus erstellen.

![Ein Formularblock, der neue Kund:innen registriert und einen Rabattcode an deren E-Mail-Adresse sendet.]({% image_buster /assets/img/landing_pages/form.png %}){: style="max-width:70%;"}

| Blocktyp | Beschreibung |
|---------------|-------------|
| E-Mail-Erfassung | Ein Formularfeld für E-Mail-Adressen. Bei der Übermittlung wird die E-Mail-Adresse dem Nutzerprofil in Braze hinzugefügt. |
| Telefon-Erfassung | Ein Formularfeld für Telefonnummern. Bei der Übermittlung werden die Nutzer:innen für Ihre SMS- oder WhatsApp-Abo-Gruppe angemeldet. |
| Eingabefeld | Ein Formularfeld, das Standardattribute (wie Vor- und Nachname) oder einen angepassten Attribut-String Ihrer Wahl unterstützt. |
| Dropdown | Nutzer:innen können einen Eintrag aus einer vordefinierten Liste auswählen. Sie können beliebige angepasste Attribut-Strings zur Liste hinzufügen. |
| Kontrollkästchen | Wenn Nutzer:innen das Kästchen aktivieren, wird das Attribut des Blocks auf `true` gesetzt. Wenn es nicht aktiviert wird, wird das Attribut auf `false` gesetzt. |
| Kontrollkästchen-Gruppe | Nutzer:innen können aus mehreren Optionen auswählen. Werte werden entweder gesetzt oder einem definierten Array-Attribut hinzugefügt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Formularblöcke" }

{% alert important %}
Nachdem Sie eine Landing-Page mit einem Formular erstellt haben, betten Sie unbedingt den zugehörigen [Landing-Page-Liquid-Tag]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) in Ihre Nachricht ein. Mit diesem Tag kann Braze bestehende Nutzerprofile automatisch identifizieren und aktualisieren, wenn diese das Formular absenden.
{% endalert %}

{% endtab %}
{% endtabs %}

#### Seitencontainer-Stile {#page-container-styles}

Sie können Stile festlegen, die auf alle relevanten Komponentenblöcke Ihrer Landing-Page angewendet werden, und zwar über den Tab **Page container**. Diese Stile werden überall auf Ihrer Seite verwendet, es sei denn, Sie überschreiben sie mit einem bestimmten Block.

Wir empfehlen, zunächst Stile auf Seitencontainer-Ebene einzurichten, bevor Sie Stile auf Blockebene anpassen. Sie können auch ein Hintergrundbild für die gesamte Seite hinzufügen.

![Der Abschnitt „Page container“ mit Optionen zur Anpassung von Hintergrundbildern, Farben, Rahmendetails und Inhaltsstilen.]({% image_buster /assets/img/landing_pages/page_container.png %}){: style="max-width:40%;"}

#### Responsiv für Nutzergeräte {#responsive-to-user-devices}

Sie können Ihre Landing-Page responsiv für die Bildschirmgröße der Nutzergeräte gestalten, indem Sie Spalten auf kleineren Bildschirmen vertikal stapeln. Um dies zu aktivieren, fügen Sie eine Spalte in die Zeile ein, die Sie responsiv gestalten möchten, und aktivieren Sie dann **Vertically stack on smaller screens** im Abschnitt **Customize columns**.

Wenn diese Option aktiviert ist, können Sie auch die Stapelreihenfolge der Spalten umkehren, um die vertikale Anordnung von mehrspaltigem Inhalt auf kleineren Bildschirmen zu steuern. So sehen und fühlen sich Seiten auf Mobilgeräten besser an – ohne angepassten Code.

![Der Schalter „Vertically stack on smaller screens“ im Abschnitt „Customize columns“.]({% image_buster /assets/img/landing_pages/device_responsive_toggle.png %}){: style="max-width:50%;"}

#### Optionale und erforderliche Felder {#optional-and-required-fields}

Sie können festlegen, ob ein Formularfeld erforderlich oder optional ist. Erforderliche Felder müssen ausgefüllt werden, bevor das Formular abgesendet werden kann. Optionale Felder können von Nutzer:innen leer gelassen oder nicht ausgewählt werden.

Um beispielsweise die Einwilligungserfassung vor dem Absenden des Formulars zu erzwingen, können Sie **Required field input** aktivieren, um ein Kontrollkästchen mit dem entsprechenden Hinweistext als erforderlich festzulegen.

![Ein Kontrollkästchen-Formularfeld mit aktiviertem Schalter „Required input field“.]({% image_buster /assets/img/landing_pages/lp-optional-required.png %}){: style="max-width:50%;"}

### Schritt 4: Eine Bestätigungsseite erstellen (optional) {#step-4-create-a-confirmation-page-optional}

Wenn Ihre Landing-Page kein Formular enthält, fahren Sie mit dem nächsten Schritt fort.

Wenn Ihre Landing-Page ein [Formular](#form-blocks) enthält, erstellen Sie eine zweite Landing-Page als Bestätigungserlebnis. Diese Seite sollte den Nutzer:innen danken oder einen nächsten Schritt nach dem Absenden des Formulars anbieten.

So verknüpfen Sie die Bestätigungsseite:
- Wählen Sie den **Submit**-Button in Ihrem Formular aus
- Verwenden Sie die Aktion **Open web URL**, um auf Ihre Bestätigungsseite zu verlinken

Wenn Sie keine Bestätigungsseite einbinden, wissen Nutzer:innen möglicherweise nicht, dass ihr Formular erfolgreich abgesendet wurde. Fügen Sie immer ein Bestätigungserlebnis hinzu, um die Journey abzuschließen.

{% alert note %}
Wenn Ihre Bestätigungsseite in einem neuen Tab geöffnet wird, kann es vorkommen, dass Nutzer:innen, die zur ursprünglichen Landing-Page zurückkehren und das Formular mit aktualisierten Informationen erneut absenden, die vorherige Übermittlung überschreiben, was zu inkonsistenten Daten führen kann.
{% endalert %}

### Schritt 5: Vorschau der Seite {#step-5-preview-the-page}

Sie können eine Vorschau Ihrer Landing-Page im Tab **Preview** des Editors anzeigen. Nachdem Sie Ihre Landing-Page als Entwurf gespeichert haben, können Sie die URL aufrufen, indem Sie zu **Landing Pages** gehen und neben Ihrer Landing-Page **Copy URL** auswählen. Sie können die URL auch mit Kolleg:innen teilen.

![Eine Landing-Page mit geöffnetem Menü, das die Option „Copy URL“ zeigt.]({% image_buster /assets/img/landing_pages/copy-url.png %})

Stellen Sie vor der Veröffentlichung sicher, dass:

- Sie das Limit für veröffentlichte Landing-Pages Ihres Plans nicht überschritten haben
- Jede formularbasierte Seite über die Aktion **Open web URL** mit einer [Bestätigungsseite](#step-4-create-a-confirmation-page) verknüpft ist
- Alle erforderlichen Seitenfelder (wie URL-Pfad und Titel) vollständig sind

Wenn Sie bereit sind, wählen Sie **Publish Landing Page**.

{% alert note %}
Aggressive Pop-up-Blocker und Werbeblocker auf iOS und in Safari (einschließlich der integrierten Steuerelemente von Safari und Erweiterungen von Drittanbietern) können das Verhalten von Landing-Pages negativ beeinflussen, wenn ein **Submit**-Button eines Formulars gleichzeitig eine andere URL öffnet – unabhängig davon, ob diese URL im selben Tab oder in einem neuen Tab geöffnet wird.
{% endalert %}

## Templates verwenden {#using-templates}

Verwenden Sie Landing-Page-Templates, um Templates für Ihre nächsten Campaigns zu erstellen. Diese Templates können sowohl im Landing-Page-Editor als auch auf der Seite **Landing Page Templates** (**Content** > **Landing Page**) aufgerufen und verwaltet werden. Landing-Page-Templates erfordern einen Namen und optional eine Beschreibung.

## Templates verwalten {#managing-templates}

Sie können Landing-Page-Templates in der Vorschau anzeigen, archivieren oder bearbeiten. Sie können Ihre eigenen Landing-Page-Templates (unter **Your Templates**) duplizieren, jedoch keine Braze-Templates. Beim Bearbeiten einer Landing-Page können Sie Ihre Landing-Page als Template speichern, Änderungen am Template vornehmen oder den Inhalt der Landing-Page löschen.

![Ein Dropdown-Menü mit Optionen zum Speichern, Ändern und Löschen einer Landing-Page.]({% image_buster /assets/img/landing_pages/manage-lp-template.png %}){: style="max-width:60%;"}

## Analytics anzeigen {#viewing-analytics}

Um die Effektivität Ihrer Landing-Page zu analysieren, gehen Sie zu **Messaging** > **Landing Pages** und wählen Sie eine veröffentlichte Landing-Page aus. Hier können Sie die Anzahl der Seitenaufrufe, Seitenklicks, Formularübermittlungen und die Übermittlungsraten für Ihre Landing-Page verfolgen.

![Der Analytics-Bereich für eine Landing-Page.]({% image_buster /assets/img/landing_pages/analytics.png %})

## Fehler bei der Formularübermittlung behandeln {#handling-form-submission-errors}

Wenn Nutzer:innen versuchen, ein Formular mit fehlenden oder nicht unterstützten Eingaben abzusenden, wird eine allgemeine Fehlermeldung angezeigt und das Absenden ist nicht möglich.

Häufige Ursachen:

- Erforderliche Felder sind leer
- Sonderzeichen werden in Texteingaben verwendet
- Ein erforderliches Kontrollkästchen ist nicht aktiviert

Fehlermeldungen, die Nutzer:innen angezeigt werden, können nicht angepasst werden. Zeigen Sie eine Vorschau Ihrer Landing-Page an, um das Feldverhalten vor der Veröffentlichung zu überprüfen.