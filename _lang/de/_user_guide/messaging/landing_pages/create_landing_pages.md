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

Eine Landing-Page ist eine live veröffentlichte Webseite mit einer teilbaren URL, die Ihre Kund:innen besuchen können.

{% alert note %}
Landing-Page-Templates sind unveröffentlichte Designvorlagen ohne öffentliche URL, die nicht mit Ihren Kund:innen geteilt werden können. Um eine Seite aus einem Template zu erstellen, siehe [Templates verwenden](#using-templates).
{% endalert %}

### Schritt 1: Neuen Entwurf erstellen {#step-1-create-a-new-draft}

Gehen Sie zu **Messaging** > **Landing-Pages** und wählen Sie **Create landing page**. Sie können auch den Namen einer bestehenden Landing-Page auswählen, um diese zu duplizieren oder Änderungen vorzunehmen.

### Schritt 2: Seitendetails eingeben {#step-2-enter-the-page-details}

Fügen Sie interne und öffentlich sichtbare Details hinzu, die Ihnen helfen, Ihre Landing-Page zu organisieren, zu kennzeichnen und zu teilen.

#### Allgemeine Details {#general-details}

Geben Sie einen Namen und eine Beschreibung für die Landing-Page ein. Diese Details werden verwendet, um die Seite in Ihrem internen Workspace zu suchen. Sie sind für Ihre Kund:innen nicht sichtbar.

#### Website-Details {#site-details}

Richten Sie Metatags ein, um das Erscheinungsbild Ihrer Seite im Browser-Tab anzupassen und für Suchmaschinenergebnisse zu optimieren. Diese sind für Ihre Kund:innen sichtbar.

Wir empfehlen, die folgenden Best Practices zu befolgen:

| Feld | Beschreibung | Empfehlungen |
| --- | --- | --- |
| Website-Titel | Der Titel, der im Browser-Tab angezeigt wird. | Verwenden Sie bis zu 60 Zeichen. |
| Meta-Beschreibung | Ein Textausschnitt, der in Suchergebnissen angezeigt wird. | Verwenden Sie zwischen 140–160 Zeichen. |
| Favicon | Das Symbol, das neben dem Website-Titel im Browser-Tab erscheint. | Verwenden Sie ein Seitenverhältnis von 1:1 und einen unterstützten Dateityp wie PNG, JPEG oder ICO. |
| Seiten-URL | Dies ist der URL-Pfad zu Ihrer Landing-Page. Dieser Wert wird auch referenziert, wenn Sie [Landing-Page-Liquid-Tags]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) verwenden, die Sie in eine Nachricht einbetten können, um automatisch zu erkennen, wenn Nutzer:innen Ihr Formular absenden. | Dieser Wert muss innerhalb Ihres Workspace eindeutig sein. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Website-Details" }

### Schritt 3: Seite anpassen {#step-3-customize-the-page}

Falls noch nicht geschehen, wählen Sie **Save as draft**. Um mit der Anpassung Ihrer Seite zu beginnen, wählen Sie **Edit landing page**. Der Drag-and-Drop-Editor lädt ein Standard-Template vor, das Sie an Ihren Anwendungsfall anpassen können.

![Eine Beispiel-Landing-Page, die im Drag-and-Drop-Editor erstellt wird.]({% image_buster /assets/img/landing_pages/template.png %})

Der Editor verwendet zwei Arten von Komponenten für die Landing-Page-Erstellung: Basis-Blöcke und Formular-Blöcke. Alle Blöcke müssen in einer Zeile platziert werden. Eine detaillierte Referenz zu jedem Block und seinen Eigenschaften finden Sie unter [Editor-Blöcke (Landing-Pages)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages).

![Der Abschnitt „Build“ mit „Rows“ und „Form Blocks“.]({% image_buster /assets/img/landing_pages/dnd.png %}){: style="max-width:35%;"}

{% tabs %}
{% tab Basis-Blöcke %}

Sie können diese Blöcke verwenden, um Inhalte hinzuzufügen und das Layout Ihrer Landing-Page anzupassen.

| Blocktyp | Beschreibung |
|-------------|-------------|
| Titel | Ein Textblock zum Hinzufügen einer Überschrift oder eines Titels zu Ihrem Inhalt. Nützlich zum Strukturieren von Abschnitten und zur Verbesserung der Lesbarkeit. |
| Absatz | Ein Textblock für längere Beschreibungen oder zusätzlichen Kontext. Unterstützt Rich-Text-Formatierung. |
| Button | Ein klickbares Element, das Nutzer:innen zu einer bestimmten Aktion weiterleitet, z. B. einen Link öffnen oder ein Formular absenden. |
| Radio-Button | Fügt eine Liste von Optionen hinzu, aus der Nutzer:innen eine auswählen müssen. Beim Absenden wird das zugehörige angepasste Attribut im Kundenprofil or Nutzerprofil protokolliert. |
| Bild | Ein Block zur Anzeige von Bildern. Sie können ein Bild hochladen oder eine URL angeben, um auf eine externe Quelle zu verweisen. |
| Link | Ein Hyperlink, auf den Nutzer:innen klicken können, um zu einer bestimmten URL zu navigieren. Kann in Text eingebettet oder eigenständig verwendet werden. |
| Abstandshalter | Ein unsichtbarer Block, der vertikalen Abstand zwischen Elementen hinzufügt, um Layout und Lesbarkeit zu verbessern. |
| Angepasster Code | Ein Block, mit dem Sie angepasstes HTML, CSS oder JavaScript einfügen und ausführen können, um erweiterte Anpassungen vorzunehmen. Informationen zur Anbindung an das Braze SDK or Software-Development-Kit aus diesem Block finden Sie unter [JavaScript-Bridge für Landing-Pages]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge) und [Angepasste Formularblöcke erstellen]({{site.baseurl}}/user_guide/messaging/landing_pages/custom_form_blocks). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 3: Seite anpassen" }

#### Span-Text {#span-text}

Um bestimmte Stile auf Textblöcke ohne angepassten Code anzuwenden, markieren Sie den Text, den Sie gestalten möchten, und wählen Sie dann **Wrap with span for style**.

![Textfeld mit verschiedenen gestalteten Textabschnitten, z. B. unterschiedlichen Schriftgrößen und Farben, und einem markierten Abschnitt, der eine Symbolleiste mit der Option „Wrap with span for style“ anzeigt.]({% image_buster /assets/img/landing_pages/wrap_with_span.png %}){: style="max-width:50%;"}

Passen Sie die Span-Eigenschaften an, um Ihre Textgestaltung zu Update or aktualisieren or aktualisieren. Dazu gehören:

- Schriftfamilie, -stärke, -größe
- Zeilenhöhe
- Buchstabenabstand
- Textausrichtung und -farbe
- Block-Padding

![Panel mit Span-Eigenschaften und verschiedenen Optionen zur Aktualisierung.]({% image_buster /assets/img/landing_pages/span_properties.png %}){: style="max-width:35%;"}


{% endtab %}
{% tab Formular-Blöcke %}

Sie können diese Blöcke verwenden, um ein Formular zu erstellen, das von Nutzer:innen übermittelte Daten mit deren Profil in Braze verknüpft. Beachten Sie, dass Sie bei Verwendung von Formular-Blöcken auch eine zusätzliche Landing-Page für den Bestätigungsstatus erstellen müssen.

![Ein Formular-Block, der neue Kund:innen registriert und einen Rabattcode an deren E-Mail-Adresse sendet.]({% image_buster /assets/img/landing_pages/form.png %}){: style="max-width:70%;"}

{% alert tip %}
Sie können ein langes Formular in mehrere Schritte mit jeweils eigenen Feldern und einem integrierten Bestätigungsschritt aufteilen, indem Sie ein [mehrstufiges Formular]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/multi_step_forms) verwenden, anstatt Formular-Blöcke direkt in einer Zeile zu platzieren.
{% endalert %}

| Blocktyp | Beschreibung |
|---------------|-------------|
| E-Mail-Erfassung | Ein Formularfeld für E-Mail-Adressen. Beim Absenden wird die E-Mail-Adresse dem Kundenprofil or Nutzerprofil in Braze hinzugefügt. |
| Telefon-Erfassung | Ein Formularfeld für Telefonnummern. Beim Absenden wird die Nutzer:in für Ihre Kurzmitteilungsdienst or SMS- oder WhatsApp-Abo-Gruppe angemeldet. |
| Eingabefeld | Ein Formularfeld, das Standardattribute (wie Vor- und Nachname) oder einen angepassten Attribut-String Ihrer Wahl unterstützt. |
| Dropdown | Nutzer:innen können einen Artikel aus einer vordefinierten Liste auswählen. Sie können beliebige angepasste Attribut-Strings zur Liste hinzufügen. |
| Checkbox | Wenn eine Nutzer:in die Box ankreuzt, wird das Attribut des Blocks auf `true` gesetzt. Wenn sie nicht angekreuzt wird, wird das Attribut auf `false` gesetzt. |
| Checkbox-Gruppe | Nutzer:innen können aus mehreren angebotenen Optionen auswählen. Die Werte werden in einem definierten Array-angepassten-Attribut gesetzt oder hinzugefügt. |
| Abos verwalten | Eine Checkliste von E-Mail-, Kurzmitteilungsdienst or SMS- oder WhatsApp-Abo-Gruppen. Nutzer:innen wählen beim Absenden des Formulars aus, welchen Gruppen sie beitreten möchten. Jeder Block ist für einen Kanal. Weitere Informationen finden Sie unter [Block „Abos verwalten“]({{site.baseurl}}/user_guide/messaging/landing_pages/manage_subscriptions). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Span-Text" }

{% alert important %}
Nachdem Sie eine Landing-Page mit einem Formular erstellt haben, stellen Sie sicher, dass Sie den [Landing-Page-Liquid-Tag]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) in Ihre Nachricht einbetten. Mit diesem Tag kann Braze bestehende Nutzerprofile automatisch identifizieren und Update or aktualisieren or aktualisieren, wenn sie das Formular absenden.
{% endalert %}

{% endtab %}
{% endtabs %}

#### Seitencontainer-Stile {#page-container-styles}

Sie können Stile festlegen, die auf alle relevanten Komponentenblöcke Ihrer Landing-Page angewendet werden, und zwar über den Tab **Page container**. Diese Stile gelten überall auf Ihrer Seite, es sei denn, Sie überschreiben sie mit einem bestimmten Block.

Wir empfehlen, zunächst Stile auf Seitencontainer-Ebene einzurichten, bevor Sie Stile auf Blockebene anpassen. Sie können auch ein Hintergrundbild für die gesamte Seite hinzufügen.

![Der Abschnitt „Page container“ mit Optionen zum Anpassen von Hintergrundbildern, Farben, Rahmendetails und Inhaltsgestaltung.]({% image_buster /assets/img/landing_pages/page_container.png %}){: style="max-width:40%;"}

#### Responsiv für Nutzergeräte {#responsive-to-user-devices}

Sie können Ihre Landing-Page responsiv für die Bildschirmgröße der Nutzergeräte machen, indem Sie Spalten auf kleineren Bildschirmen vertikal stapeln. Um dies zu aktivieren, fügen Sie eine Spalte in die Zeile ein, die Sie responsiv gestalten möchten, und schalten Sie dann **Vertically Stack on smaller screens** im Abschnitt **Customize columns** ein.

Wenn aktiviert, können Sie auch Spalten in umgekehrter Reihenfolge stapeln, um die vertikale Reihenfolge von mehrspaltigem Inhalt auf kleineren Bildschirmen zu steuern. So sehen Seiten auf Mobilgeräten besser aus und fühlen sich besser an – ohne angepassten Code.

![Der Schalter „Vertically stack on smaller screens“ im Abschnitt „Customize columns“.]({% image_buster /assets/img/landing_pages/device_responsive_toggle.png %}){: style="max-width:50%;"}

{% multi_lang_include drag_and_drop/hide_rows_and_blocks_by_device.md channel='landing_page' %}

#### Optionale und Pflichtfelder {#optional-and-required-fields}

Sie können festlegen, ob bestimmte Formularfelder erforderlich oder optional sind. Pflichtfelder müssen ausgefüllt werden, bevor das Formular abgesendet werden kann. Optionale Felder können von Nutzer:innen leer gelassen oder nicht ausgewählt werden.

{% alert note %}
Radio-Buttons sind immer Pflichtfelder und können nicht auf optional gesetzt werden. Wenn Sie ein optionales Einzelauswahl-Feld benötigen, verwenden Sie stattdessen ein Dropdown.
{% endalert %}

Um beispielsweise die Einwilligungserfassung vor dem Absenden des Formulars zu erzwingen, können Sie **Required field input** aktivieren, um eine Checkbox mit dem entsprechenden Hinweistext als Pflichtfeld festzulegen.

![Ein Checkbox-Formularfeld mit aktiviertem Schalter „Required input field“.]({% image_buster /assets/img/landing_pages/lp-optional-required.png %}){: style="max-width:50%;"}

### Schritt 4: Bestätigungsseite erstellen (optional) {#step-4-create-a-confirmation-page-optional}

Wenn Ihre Landing-Page kein Formular enthält, fahren Sie mit dem nächsten Schritt fort.

{% alert note %}
Wenn Ihr Formular ein [mehrstufiges Formular]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/multi_step_forms) verwendet, überspringen Sie diesen Schritt. Mehrstufige Formulare enthalten einen integrierten, gesperrten Bestätigungsschritt, sodass Sie keine separate Bestätigungsseite benötigen.
{% endalert %}

Wenn Ihre Landing-Page ein [Formular](#form-blocks) enthält, können Sie optional eine zweite Landing-Page als Bestätigungserlebnis erstellen. Diese Seite sollte den Nutzer:innen danken oder einen nächsten Schritt nach dem Absenden des Formulars bieten.

1. Wählen Sie den **Submit**-Button in Ihrem Formular
2. Legen Sie fest, ob eine Bestätigungsseite angezeigt werden soll, wenn Nutzer:innen Ihr Formular absenden
    - Verwenden Sie das Klickverhalten **Open web URL**, um Nutzer:innen zu einer Bestätigungsseite zu senden
    - Verwenden Sie das Klickverhalten **None**, damit Nutzer:innen auf der Landing-Page bleiben

Wenn Sie keine Bestätigungsseite einbinden, wissen Nutzer:innen möglicherweise nicht, dass ihr Formular erfolgreich abgesendet wurde. Binden Sie immer ein Bestätigungserlebnis ein, um den Ablauf abzuschließen.

{% alert note %}
Wenn Ihre Bestätigungsseite in einem neuen Tab geöffnet wird, kann eine Nutzer:in, die zur ursprünglichen Landing-Page zurückkehrt und das Formular mit aktualisierten Informationen erneut absendet, die vorherige Übermittlung überschreiben, was zu inkonsistenten Daten führen kann.
{% endalert %}

### Schritt 5: Vorschau der Seite {#step-5-preview-the-page}

Sie können eine Vorschau Ihrer Landing-Page im Tab **Preview** des Editors anzeigen. Nachdem Sie Ihre Landing-Page als Entwurf gespeichert haben, können Sie die URL besuchen, indem Sie zu **Landing-Pages** gehen und neben Ihrer Landing-Page **Copy URL** auswählen.

![Eine Landing-Page mit geöffnetem Menü, das die Option „Copy URL“ anzeigt.]({% image_buster /assets/img/landing_pages/copy-url.png %})

#### Vorschau-Link teilen {#sharing-a-preview-link}

Im Editor können Sie auch **Copy preview link** auswählen, um die Seite mit Prüfer:innen zu teilen, die keinen Dashboard-Zugang haben.

- Wenn Ihre Landing-Page kein Liquid verwendet, ist dieser Link derselbe wie die direkte URL von **Copy URL**, im Vorschaumodus geöffnet.
- Wenn Ihre Landing-Page Liquid verwendet und Sie über die Landing Pages Pro-Berechtigung verfügen, rendert der Link stattdessen die Live-Seite bei Bedarf und spiegelt Ihre aktuellen Änderungen wider, anstatt einen Snapshot vom Zeitpunkt der Link-Erstellung zu zeigen. Der Inhalt wird pro Nutzer:in personalisiert. Die Vorschau zeigt das Braze-Favicon an und kann nicht geändert werden.

Informationen zu Vorschau-Links für andere Kanäle finden Sie unter [Teilbare Vorschau]({{site.baseurl}}/user_guide/messaging/governance/shareable_preview).

### Schritt 6: Veröffentlichen {#step-6-publish}

Stellen Sie vor der Veröffentlichung sicher, dass:

- Sie das Limit für veröffentlichte Landing-Pages Ihres Plans nicht überschritten haben
- Jede formularbasierte Seite über die Aktion **Open web URL** mit einer [Bestätigungsseite](#step-4-create-a-confirmation-page-optional) verknüpft ist oder ein [mehrstufiges Formular]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/multi_step_forms) mit integriertem Bestätigungsschritt verwendet
- Alle erforderlichen Seitenfelder (wie URL-Pfad und Titel) vollständig sind

Wenn Sie bereit sind, wählen Sie **Publish Landing Page**.

{% alert note %}
Aggressive Pop-up-Blocker und Werbeblocker auf iOS und in Safari (einschließlich der integrierten Steuerungen von Safari und Erweiterungen von Drittanbietern) können sich negativ auf das Verhalten von Landing-Pages auswirken, wenn ein Formular-**Submit**-Button gleichzeitig eine andere URL öffnet, unabhängig davon, ob diese URL im selben Tab oder in einem neuen Tab geöffnet wird.
{% endalert %}

## Templates verwenden {#use-templates}

Landing-Page-Templates sind wiederverwendbare Design-Ausgangspunkte, die Ihnen helfen, Landing-Pages schneller zu erstellen. Ein Template hat keine öffentliche URL und kann nicht von Kund:innen besucht werden. Um aus einem Template eine aktive Landing-Page zu erstellen, wählen Sie das Template beim Erstellen einer neuen Landing-Page aus, passen Sie es nach Bedarf an und veröffentlichen Sie es.

Templates können sowohl im Landing-Page-Editor als auch auf der Seite **Landing Page Templates** (**Content** > **Landing Page**) aufgerufen und verwaltet werden. Landing-Page-Templates erfordern einen Namen und eine optionale Beschreibung.

## Templates verwalten {#manage-templates}

Sie können Landing-Page-Templates in der Vorschau anzeigen, archivieren oder bearbeiten. Sie können Ihre eigenen Landing-Page-Templates (unter **Ihre Templates**) duplizieren, jedoch keine Braze-Templates. Beim Bearbeiten einer Landing-Page können Sie Ihre Landing-Page als Template speichern, Änderungen am Template vornehmen oder den Inhalt der Landing-Page löschen.

![Ein Dropdown-Menü mit Optionen zum Speichern, Ändern und Löschen einer Landing-Page.]({% image_buster /assets/img/landing_pages/manage-lp-template.png %}){: style="max-width:60%;"}

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