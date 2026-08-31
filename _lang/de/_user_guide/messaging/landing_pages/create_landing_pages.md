---
nav_title: Landing-Pages erstellen
article_title: Landing-Pages erstellen
description: "Dieser Artikel beschreibt, wie Sie Landing-Pages in Braze mit dem Drag-and-Drop-Editor erstellen und anpassen."
page_order: 0
---

# Landing-Pages erstellen {#create-landing-pages}

> Erfahren Sie, wie Sie mit dem Drag-and-Drop-Editor eine Landing-Page erstellen und anpassen, um Ihre Zielgruppe zu vergrößern und Präferenzen direkt in Braze zu erfassen.

## Voraussetzungen {#prerequisites}

Um auf den Landing-Page-Builder zugreifen zu können, benötigen Sie [bestimmte Berechtigungen]({{site.baseurl}}/user_guide/messaging/landing_pages#prerequisites). Wenn Sie keinen Zugriff haben, wenden Sie sich an Ihren Braze-Administrator.

## Landing-Page erstellen {#create-a-landing-page}

Eine Landing-Page ist eine veröffentlichte, live geschaltete Webseite mit einer teilbaren URL, die Ihre Kund:innen besuchen können.

{% alert note %}
Landing-Page-Templates sind unveröffentlichte Design-Ausgangspunkte ohne öffentliche URL, die nicht mit Ihren Kund:innen geteilt werden können. Um eine Seite aus einem Template zu erstellen, siehe [Templates verwenden](#using-templates).
{% endalert %}

### Schritt 1: Neuen Entwurf erstellen {#step-1-create-a-new-draft}

Gehen Sie zu **Messaging** > **Landing-Pages** und wählen Sie dann **Landing-Page erstellen**. Sie können auch den Namen einer bestehenden Landing-Page auswählen, um sie zu duplizieren oder Änderungen vorzunehmen.

### Schritt 2: Seitendetails eingeben {#step-2-enter-the-page-details}

Fügen Sie interne und öffentliche Details hinzu, die Ihnen helfen, Ihre Landing-Page zu organisieren, zu gestalten und zu teilen.

#### Allgemeine Details {#general-details}

Geben Sie einen Namen und eine Beschreibung für die Landing-Page ein. Diese Details werden verwendet, um die Seite in Ihrem internen Workspace zu suchen. Sie sind für Ihre Kund:innen nicht sichtbar.

#### Website-Details {#site-details}

Richten Sie Metatags ein, um die Darstellung Ihrer Seite im Browser-Tab anzupassen und für Suchmaschinenergebnisse zu optimieren. Diese sind für Ihre Kund:innen sichtbar.

Wir empfehlen die folgenden Best Practices:

| Feld | Beschreibung | Empfehlungen |
| --- | --- | --- |
| Website-Titel | Der Titel, der im Browser-Tab angezeigt wird. | Verwenden Sie bis zu 60 Zeichen. |
| Meta-Beschreibung | Ein Textausschnitt, der in Suchergebnissen angezeigt wird. | Verwenden Sie zwischen 140–160 Zeichen. |
| Favicon | Das Symbol, das neben dem Website-Titel im Browser-Tab erscheint. | Verwenden Sie ein Seitenverhältnis von 1:1 und einen unterstützten Dateityp wie PNG, JPEG oder ICO. |
| Seiten-URL | Dies ist der URL-Pfad zu Ihrer Landing-Page. Dieser Wert wird auch referenziert, wenn Sie [Landing-Page-Liquid-Tags]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) verwenden, die Sie in eine Nachricht einbetten können, um automatisch zu erkennen, wann Nutzer:innen Ihr Formular absenden. | Dieser Wert muss innerhalb Ihres Workspaces eindeutig sein. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Website-Details" }

### Schritt 3: Seite anpassen {#step-3-customize-the-page}

Falls noch nicht geschehen, wählen Sie **Als Entwurf speichern**. Um mit der Anpassung Ihrer Seite zu beginnen, wählen Sie **Landing-Page bearbeiten**. Der Drag-and-Drop-Editor wird mit einem Standard-Template vorgeladen, das Sie an Ihren Anwendungsfall anpassen können.

![Eine beispielhafte Landing-Page, die im Drag-and-Drop-Editor erstellt wird.]({% image_buster /assets/img/landing_pages/template.png %})

Der Editor verwendet zwei Arten von Komponenten für die Landing-Page-Erstellung: Basisblöcke und Formularblöcke. Alle Blöcke müssen in einer Zeile platziert werden. Eine vollständige Referenz aller Blöcke und Eigenschaften finden Sie unter [Editor-Blöcke (Landing-Pages)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages).

![Der Bereich „Build“ mit „Rows“ und „Form Blocks“.]({% image_buster /assets/img/landing_pages/dnd.png %}){: style="max-width:35%;"}

{% tabs %}
{% tab Basisblöcke %}

Sie können diese Blöcke verwenden, um Inhalte hinzuzufügen und das Layout Ihrer Landing-Page anzupassen.

| Blocktyp | Beschreibung |
|-------------|-------------|
| Titel | Ein Textblock zum Hinzufügen einer Überschrift oder eines Titels. Nützlich für die Strukturierung von Abschnitten und die Verbesserung der Lesbarkeit. |
| Absatz | Ein Textblock für längere Beschreibungen oder zusätzlichen Kontext. Unterstützt Rich-Text-Formatierung. |
| Button | Ein klickbares Element, das Nutzer:innen zu einer bestimmten Aktion weiterleitet, z. B. das Öffnen eines Links oder das Absenden eines Formulars. |
| Optionsfeld | Fügt eine Liste von Optionen hinzu, aus der Nutzer:innen eine auswählen müssen. Beim Absenden wird das zugehörige angepasste Attribut im Nutzerprofil gespeichert. |
| Bild | Ein Block zum Anzeigen von Bildern. Sie können ein Bild hochladen oder eine URL angeben, um eine externe Quelle zu referenzieren. |
| Link | Ein Hyperlink, auf den Nutzer:innen klicken können, um zu einer bestimmten URL zu navigieren. Kann in Text eingebettet oder eigenständig verwendet werden. |
| Abstandshalter | Ein unsichtbarer Block, der vertikalen Abstand zwischen Elementen für ein verbessertes Layout und bessere Lesbarkeit hinzufügt. |
| Angepasster Code | Ein Block, mit dem Sie angepasstes HTML, CSS oder JavaScript für erweiterte Anpassungen einfügen und ausführen können. Um über diesen Block mit dem Braze SDK zu interagieren, siehe [Pont JavaScript für Landing-Pages]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge) und [Angepasste Formularblöcke erstellen]({{site.baseurl}}/user_guide/messaging/landing_pages/custom_form_blocks). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 3: Seite anpassen" }

#### Span-Text {#span-text}

Um bestimmte Formatierungen auf Textblöcke ohne angepassten Code anzuwenden, markieren Sie den Text, den Sie formatieren möchten, und wählen Sie dann **Wrap with span for style**.

![Textfeld mit verschiedenen gestalteten Textabschnitten, z. B. unterschiedliche Schriftgrößen und Farben, und einem markierten Abschnitt, der eine Symbolleiste mit der Option „Wrap with span for style“ anzeigt.]({% image_buster /assets/img/landing_pages/wrap_with_span.png %}){: style="max-width:50%;"}

Passen Sie die Span-Eigenschaften an, um Ihre Textformatierung zu aktualisieren. Dazu gehören:

- Schriftfamilie, -stärke, -größe
- Zeilenhöhe
- Zeichenabstand
- Textausrichtung und -farbe
- Block-Padding

![Panel für Span-Eigenschaften mit verschiedenen Optionen zur Aktualisierung.]({% image_buster /assets/img/landing_pages/span_properties.png %}){: style="max-width:35%;"}


{% endtab %}
{% tab Formularblöcke %}

Sie können diese Blöcke verwenden, um ein Formular zu erstellen, das von Nutzer:innen übermittelte Daten mit deren Profil in Braze verknüpft. Beachten Sie, dass Sie bei Verwendung von Formularblöcken auch eine zusätzliche Landing-Page für den Bestätigungsstatus erstellen müssen.

![Ein Formularblock, der eine:n neue:n Kund:in registriert und einen Rabattcode an die E-Mail-Adresse sendet.]({% image_buster /assets/img/landing_pages/form.png %}){: style="max-width:70%;"}

{% alert tip %}
Sie können ein langes Formular in mehrere Schritte aufteilen, jeder mit eigenen Feldern und einem integrierten Bestätigungsschritt, indem Sie ein [mehrstufiges Formular]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/multi_step_forms) verwenden, anstatt Formularblöcke direkt in eine Zeile zu platzieren.
{% endalert %}

| Blocktyp | Beschreibung |
|---------------|-------------|
| E-Mail-Erfassung | Ein Formularfeld für E-Mail-Adressen. Beim Absenden wird die E-Mail-Adresse dem Nutzerprofil in Braze hinzugefügt. |
| Telefon-Erfassung | Ein Formularfeld für Telefonnummern. Beim Absenden wird die Person für Ihre SMS- oder WhatsApp-Abo-Gruppe angemeldet. |
| Eingabefeld | Ein Formularfeld, das Standardattribute (wie Vor- und Nachname) oder einen angepassten Attribut-String Ihrer Wahl unterstützt. |
| Dropdown | Nutzer:innen können einen Artikel aus einer vordefinierten Liste auswählen. Sie können beliebige angepasste Attribut-Strings zur Liste hinzufügen. |
| Checkbox | Wenn Nutzer:innen die Checkbox aktivieren, wird das Attribut des Blocks auf `true` gesetzt. Falls nicht aktiviert, wird sein Attribut auf `false` gesetzt. |
| Checkbox-Gruppe | Nutzer:innen können aus mehreren angebotenen Optionen auswählen. Werte werden entweder gesetzt oder zu einem definierten Array-Attribut hinzugefügt. |
| Abos verwalten | Eine Checkliste von E-Mail-Abo-Gruppen. Nutzer:innen wählen aus, welchen Gruppen sie beim Absenden des Formulars beitreten möchten. Weitere Informationen finden Sie unter [Block „Abos verwalten“]({{site.baseurl}}/user_guide/messaging/landing_pages/manage_subscriptions). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Span-Text" }

{% alert important %}
Nachdem Sie eine Landing-Page mit einem Formular erstellt haben, betten Sie unbedingt den [Landing-Page-Liquid-Tag]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) in Ihre Nachricht ein. Mit diesem Tag kann Braze bestehende Nutzerprofile automatisch identifizieren und aktualisieren, wenn sie das Formular absenden.
{% endalert %}

{% endtab %}
{% endtabs %}

#### Seitencontainer-Styles {#page-container-styles}

Sie können Styles festlegen, die auf alle relevanten Komponentenblöcke Ihrer Landing-Page im Tab **Page container** angewendet werden. Diese Styles gelten überall auf Ihrer Seite, es sei denn, Sie überschreiben sie mit einem bestimmten Block.

Wir empfehlen, zunächst Styles auf Seitencontainer-Ebene einzurichten, bevor Sie Styles auf Blockebene anpassen. Sie können auch ein Hintergrundbild für die gesamte Seite hinzufügen.

![Der Abschnitt „Page container“ mit Optionen zum Anpassen von Hintergrundbildern, Farben, Rahmendetails und Inhaltsformatierung.]({% image_buster /assets/img/landing_pages/page_container.png %}){: style="max-width:40%;"}

#### Responsiv für Endgeräte {#responsive-to-user-devices}

Sie können Ihre Landing-Page responsiv für die Größe des Endgeräts der Nutzer:innen machen, indem Sie Spalten auf kleineren Bildschirmen vertikal stapeln. Um dies zu aktivieren, fügen Sie eine Spalte in die Zeile ein, die Sie responsiv gestalten möchten, und aktivieren Sie dann **Vertically stack on smaller screens** im Abschnitt **Customize columns**.

Wenn aktiviert, können Sie auch die Stapelreihenfolge der Spalten umkehren, um die vertikale Reihenfolge von mehrspaltigem Inhalt auf kleineren Bildschirmen zu steuern. Damit sehen und fühlen sich Seiten auf Mobilgeräten besser an, ohne angepassten Code.

![Der Schalter „Vertically stack on smaller screens“ im Abschnitt „Customize columns“.]({% image_buster /assets/img/landing_pages/device_responsive_toggle.png %}){: style="max-width:50%;"}

{% multi_lang_include drag_and_drop/hide_rows_and_blocks_by_device.md channel='landing_page' %}

#### Optionale und erforderliche Felder {#optional-and-required-fields}

Sie können festlegen, ob bestimmte Formularfelder erforderlich oder optional sind. Erforderliche Felder müssen ausgefüllt werden, bevor das Formular abgesendet werden kann. Optionale Felder können von Nutzer:innen leer gelassen oder nicht ausgewählt werden.

{% alert note %}
Optionsfelder sind immer erforderlich und können nicht als optional festgelegt werden. Wenn Sie ein optionales Einzelwahlfeld benötigen, verwenden Sie stattdessen ein Dropdown.
{% endalert %}

Um beispielsweise die Einwilligungserfassung vor dem Absenden des Formulars zu erzwingen, können Sie **Required field input** aktivieren, um eine Checkbox mit dem entsprechenden Hinweistext als erforderlich festzulegen.

![Ein Checkbox-Formularfeld mit aktiviertem Schalter „Required input field“.]({% image_buster /assets/img/landing_pages/lp-optional-required.png %}){: style="max-width:50%;"}

### Schritt 4: Bestätigungsseite erstellen (optional) {#step-4-create-a-confirmation-page-optional}

Wenn Ihre Landing-Page kein Formular enthält, fahren Sie mit dem nächsten Schritt fort.

{% alert note %}
Wenn Ihr Formular ein [mehrstufiges Formular]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/multi_step_forms) verwendet, überspringen Sie diesen Schritt. Mehrstufige Formulare enthalten einen integrierten, gesperrten Bestätigungsschritt, sodass Sie keine separate Bestätigungsseite benötigen.
{% endalert %}

Wenn Ihre Landing-Page ein [Formular](#form-blocks) enthält, können Sie optional eine zweite Landing-Page als Bestätigungserlebnis erstellen. Diese Seite sollte Nutzer:innen danken oder einen nächsten Schritt nach dem Absenden des Formulars anbieten.

1. Wählen Sie den **Submit**-Button in Ihrem Formular aus
2. Wählen Sie, ob eine Bestätigungsseite angezeigt werden soll, wenn Nutzer:innen Ihr Formular absenden
    - Verwenden Sie das Klickverhalten **Open web URL**, um Nutzer:innen zu einer Bestätigungsseite zu senden
    - Verwenden Sie das Klickverhalten **None**, damit Nutzer:innen auf der Landing-Page verbleiben

Wenn Sie keine Bestätigungsseite einbinden, wissen Nutzer:innen möglicherweise nicht, dass ihr Formular erfolgreich abgesendet wurde. Binden Sie immer ein Bestätigungserlebnis ein, um die Journey abzuschließen.

{% alert note %}
Wenn Ihre Bestätigungsseite in einem neuen Tab geöffnet wird, kann es passieren, dass Nutzer:innen, die zur ursprünglichen Landing-Page zurückkehren und mit aktualisierten Informationen erneut absenden, die vorherige Übermittlung überschreiben, was zu inkonsistenten Daten führen kann.
{% endalert %}

### Schritt 5: Vorschau der Seite {#step-5-preview-the-page}

Sie können Ihre Landing-Page im Tab **Preview** des Editors in der Vorschau anzeigen. Nachdem Sie Ihre Landing-Page als Entwurf gespeichert haben, können Sie die URL besuchen, indem Sie zu **Landing-Pages** gehen und neben Ihrer Landing-Page **Copy URL** auswählen.

![Eine Landing-Page mit geöffnetem Menü, das die Option „Copy URL“ anzeigt.]({% image_buster /assets/img/landing_pages/copy-url.png %})

#### Vorschaulink teilen {#sharing-a-preview-link}

Im Editor können Sie auch **Copy preview link** auswählen, um die Seite mit Prüfer:innen zu teilen, die keinen Dashboard-Zugriff haben.

- Wenn Ihre Landing-Page kein Liquid verwendet, ist dieser Link identisch mit der direkten URL aus **Copy URL**, geöffnet im Vorschaumodus.
- Wenn Ihre Landing-Page Liquid verwendet und Sie über die Landing Pages Pro-Berechtigung verfügen, rendert der Link stattdessen die Live-Seite auf Abruf und spiegelt Ihre aktuellen Änderungen wider, anstatt einen Snapshot vom Zeitpunkt der Linkerstellung zu zeigen. Inhalte werden pro Nutzer:in personalisiert. Die Vorschau zeigt das Braze-Favicon und kann nicht geändert werden.

Für Vorschaulinks auf anderen Kanälen siehe [Teilbare Vorschau]({{site.baseurl}}/user_guide/messaging/governance/shareable_preview).

### Schritt 6: Veröffentlichen {#step-6-publish}

Stellen Sie vor der Veröffentlichung sicher, dass:

- Sie das Limit für veröffentlichte Landing-Pages Ihres Plans nicht überschritten haben
- Jede formularbasierte Seite mit einer [Bestätigungsseite](#step-4-create-a-confirmation-page-optional) über die Aktion **Open web URL** verlinkt ist oder ein [mehrstufiges Formular]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/multi_step_forms) mit integriertem Bestätigungsschritt verwendet
- Alle erforderlichen Seitenfelder (wie URL-Pfad und Titel) vollständig sind

Wenn Sie bereit sind, wählen Sie **Publish Landing Page**.

{% alert note %}
Aggressive Pop-up-Blocker und Werbeblocker auf iOS und in Safari (einschließlich Safaris integrierter Steuerelemente und Drittanbieter-Erweiterungen) können sich negativ darauf auswirken, wie Landing-Pages funktionieren, wenn ein **Submit**-Button des Formulars gleichzeitig eine andere URL öffnet, unabhängig davon, ob diese URL im selben Tab oder in einem neuen Tab geöffnet wird.
{% endalert %}

## Templates verwenden {#use-templates}

Landing-Page-Templates sind wiederverwendbare Design-Ausgangspunkte, mit denen Sie Landing-Pages schneller erstellen können. Ein Template hat keine öffentliche URL und kann von Kund:innen nicht besucht werden. Um aus einem Template eine Live-Landing-Page zu erstellen, wählen Sie das Template beim Erstellen einer neuen Landing-Page aus, passen Sie es nach Bedarf an und veröffentlichen Sie es.

Templates können sowohl im Landing-Page-Editor als auch über die Seite **Landing Page Templates** (**Content** > **Landing Page**) aufgerufen und verwaltet werden. Landing-Page-Templates erfordern einen Namen und eine optionale Beschreibung.

## Templates verwalten {#manage-templates}

Sie können Landing-Page-Templates in der Vorschau anzeigen, archivieren oder bearbeiten. Sie können Ihre eigenen Landing-Page-Templates duplizieren (unter **Your Templates**), nicht jedoch Braze-Templates. Beim Bearbeiten einer Landing-Page können Sie Ihre Landing-Page als Template speichern, Änderungen am Template vornehmen oder den Inhalt der Landing-Page löschen.

![Ein Dropdown mit Optionen zum Speichern, Ändern und Löschen einer Landing-Page.]({% image_buster /assets/img/landing_pages/manage-lp-template.png %}){: style="max-width:60%;"}

## Analytics anzeigen {#view-analytics}

Um die Effektivität Ihrer Landing-Page zu analysieren, gehen Sie zu **Messaging** > **Landing-Pages** und wählen Sie eine veröffentlichte Landing-Page aus. Hier können Sie die Anzahl der Seitenaufrufe, Seitenklicks, Formularübermittlungen und die Übermittlungsraten Ihrer Landing-Page verfolgen.

![Der Analytics-Bereich einer Landing-Page.]({% image_buster /assets/img/landing_pages/analytics.png %})

## Fehler bei der Formularübermittlung behandeln {#handling-form-submission-errors}

Wenn Nutzer:innen versuchen, ein Formular mit fehlenden oder nicht unterstützten Eingaben abzusenden, wird eine allgemeine Fehlermeldung angezeigt und das Absenden ist nicht möglich.

Häufige Ursachen:

- Erforderliche Felder sind leer
- Sonderzeichen werden in Texteingaben verwendet
- Ein erforderliches Kontrollkästchen ist nicht aktiviert

Fehlermeldungen, die Nutzer:innen angezeigt werden, können nicht angepasst werden. Zeigen Sie eine Vorschau Ihrer Landing-Page an, um das Feldverhalten vor der Veröffentlichung zu überprüfen.