---
nav_title: WhatsApp-Template-Builder
article_title: WhatsApp-Template-Builder
description: "Erfahren Sie, wie Sie WhatsApp-Nachrichten-Templates direkt in Braze mit dem WhatsApp-Template-Builder erstellen, konfigurieren und einreichen."
alias: /whatsapp_template_builder/
page_type: reference
channel:
  - WhatsApp
---

# WhatsApp-Template-Builder {#whatsapp-template-builder}

> Mit dem WhatsApp-Template-Builder können Sie WhatsApp-Nachrichten-Templates direkt in Braze erstellen und einreichen – ohne zwischen Braze und dem Meta Business Manager wechseln zu müssen. Nachdem Meta Ihr Template genehmigt hat, können Sie es in beliebig vielen Campaigns und Canvases verwenden.

## Voraussetzungen {#prerequisites}

{% multi_lang_include whatsapp/template_prerequisites.md %}

## Ein Template erstellen {#create-a-template}

### Schritt 1: WhatsApp-Templates aufrufen {#step-1-go-to-whatsapp-templates}

Gehen Sie zu **Content** > **Templates** > **WhatsApp** und wählen Sie **Create new template** aus.

![WhatsApp-Templates-Seite mit Button zum Erstellen eines neuen Templates.]({% image_buster /assets/img/whatsapp/templates/create_whatsapp_template.png %})

### Schritt 2: Template-Einstellungen konfigurieren {#step-2-configure-template-settings}

Füllen Sie die folgenden Felder aus:

| Feld | Beschreibung |
| ----- | ----- |
| **Account** | Der WhatsApp Business Account (WABA), an den Sie das Template übermitteln möchten. Alle Abo-Gruppen und Telefonnummern innerhalb eines WABA teilen sich den Template-Zugriff. |
| **Language** | Die Sprache für dieses Template. WhatsApp erfordert ein separates Template für jede Sprache. |
| **Template name** | Ein eindeutiger Name für Ihr Template. Template-Namen dürfen nur Kleinbuchstaben, Zahlen und Unterstriche enthalten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 2: Template-Einstellungen konfigurieren" }

### Schritt 3: Layout auswählen {#step-3-choose-a-layout}

Wählen Sie unter **Layout** den Template-Typ aus:

- **Default:** Eine Standard-WhatsApp-Nachricht. Dies ist das in diesem Artikel behandelte Layout.
- **Carousel:** Eine Nachricht mit horizontal scrollbaren Karten. Weitere Informationen finden Sie unter [Karussell-Templates]({{site.baseurl}}/whatsapp_carousel_templates).

### Schritt 4: Ihr Template erstellen {#step-4-build-your-template}

#### Header (optional) {#header-optional}

Fügen Sie einen Header hinzu, der vor dem Nachrichtentext erscheint. Sie können wählen:

- **Text:** Ein kurzer Text-Header.
- **Media:** Ein Bild, Video oder Dokument (nur URL). Braze speichert die Medienreferenz und übermittelt ein Beispiel an Meta zur Genehmigung.
- **None:** Kein Header

#### Body {#body}

Geben Sie den Hauptinhalt Ihrer Nachricht ein und personalisieren Sie den Body nach Bedarf mit Liquid oder generischen Variablen:

{% raw %}
- Verwenden Sie Liquid-Tags (zum Beispiel `{{${first_name}}}`). Braze speichert Ihr Liquid und stellt es bereit, wenn Sie das Template in einer Campaign oder einem Canvas-Composer verwenden.
- Verwenden Sie generische Variablen, wie nummerierte Platzhalter (zum Beispiel `{{1}}`), wenn Sie die Personalisierung lieber später beim Erstellen Ihrer Nachricht hinzufügen möchten.
{% endraw %}

Sie können Personalisierung überall dort hinzufügen, wo der **+**-Plus-Button erscheint. Nicht alle Felder unterstützen Personalisierung.

#### Liquid-Zeichenlimits {#liquid-character-limits}

Meta erzwingt Zeichenlimits für die Template-Struktur, die Sie zur Genehmigung einreichen (zum Beispiel 1.024 Zeichen für den Body und 60 Zeichen für einen Text-Header). Im Template-Builder gelten diese Limits für das an Meta gesendete Template, nicht für die endgültige gerenderte Nachricht zum Sendezeitpunkt.

- **{% raw %}`{{ }}`{% endraw %}-Variablen:** Braze konvertiert Liquid-Variablen in nummerierte Platzhalter ({% raw %}`{{1}}`, `{{2}}`{% endraw %}), bevor die Länge geprüft wird. Ein langer Ausdruck wie {% raw %}`{{${first_name}}}`{% endraw %} zählt als kurzer Platzhalter, nicht als vollständige Liquid-Syntax.
- **{% raw %}`{% %}`{% endraw %}-Tags:** Liquid-Logik-Tags zählen als Literaltext in ihrer vollen Länge und erscheinen als nicht bearbeitbare Kopie in Template-Nachrichten.

Für komplexe Personalisierung verwenden Sie einen [Kontextschritt]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties), um Werte zu berechnen, und referenzieren Sie dann kürzere Variablen im Template. Informationen zu Message Extras und Einschränkungen bei bedingter Logik finden Sie unter [Liquid im WhatsApp-Template-Builder]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder/template_builder_liquid).

#### Fußzeile (optional) {#footer-optional}

Fügen Sie eine kurze Fußzeile hinzu, die nach dem Nachrichtentext erscheint.

#### Buttons (optional) {#buttons-optional}

Fügen Sie bis zu 10 Buttons zu Ihrem Template hinzu. Button-Typen haben unterschiedliche Kategorien und Spezifikationen.

| Button-Typ | Kategorie | Spezifikationen |
| --- | --- | --- |
| Schnellantwort | Schnellantwort-Buttons |{::nomarkdown}<ul><li><b>Maximale Anzahl:</b> 10</li><li><b>Button-Text:</b> Bis zu 25 Zeichen</li></ul> {:/}|
| Telefonnummer | Call-to-Action-Buttons | {::nomarkdown}<ul><li><b>Maximale Anzahl:</b> 1</li><li><b>Button-Text:</b> Bis zu 25 Zeichen</li><li><b>Telefonnummer:</b> Gültige Telefonnummer mit Ländervorwahl, ohne + (z. B. „14155552671“)</li></ul> {:/}|
| Website besuchen | Call-to-Action-Buttons | {::nomarkdown}<ul><li><b>Maximale Anzahl:</b> 2</li><li><b>Button-Text:</b> Bis zu 25 Zeichen</li><li><b>Website-URL:</b> Bis zu 2.000 Zeichen</li></ul> {:/}|
| Angebotscode kopieren | Call-to-Action-Buttons | {::nomarkdown}<ul><li><b>Maximale Anzahl:</b> 1</li><li><b>Button-Text:</b> „Copy offer code“ (kann nicht bearbeitet werden)</li><li><b>Angebotscode:</b> Bis zu 15 Zeichen</li></ul> {:/}|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Buttons (optional)" }

![WhatsApp-Template-Composer mit Schnellantwort- und Call-to-Action-Buttons.]({% image_buster /assets/img/whatsapp/templates/buttons.png %})

### Schritt 5: Ihr Template in der Vorschau anzeigen {#step-5-preview-your-template}

Bevor Sie das Template einreichen, sehen Sie sich in der Vorschau an, wie Ihre Nachricht für Empfänger:innen erscheint:

- **Preview as a user:** Sehen Sie eine generische Vorschau der Nachricht.
- **Preview as a specific user:** Wählen Sie ein Nutzerprofil aus, um eine Vorschau zu sehen, wie das Template mit den Daten dieser/dieses Nutzer:in gerendert wird.

### Schritt 6: Zur Überprüfung einreichen {#step-6-submit-for-review}

Wählen Sie **Submit** aus, um Ihr Template zur Überprüfung an Meta zu senden. Die Überprüfung dauert in der Regel wenige Minuten, kann aber bis zu 24 Stunden in Anspruch nehmen. Das Template erscheint auf Ihrer **WhatsApp templates**-Seite, sobald es eingereicht wurde, und der Status wird aktualisiert, wenn Sie die **WhatsApp templates**-Seite neu laden.

## Unterstützte Template-Kategorien {#supported-template-categories}

Derzeit werden im WhatsApp-Template-Builder nur Marketing-Templates unterstützt.

## Ein genehmigtes Template in einer Campaign verwenden {#use-an-approved-template-in-a-campaign}

Nachdem Meta Ihr Template genehmigt hat, können Sie es in einer WhatsApp-Campaign oder einem Canvas verwenden.

1. Gehen Sie zu **Campaigns** und wählen Sie **Campaign erstellen** > **WhatsApp**.
2. Wählen Sie im Nachrichten-Editor Ihr genehmigtes Template aus.
3. Braze befüllt automatisch den Inhalt des Templates – einschließlich aller Medien und Liquid-Elemente, die Sie bei der Template-Erstellung eingegeben haben – sodass Sie diese nicht erneut eingeben müssen.
4. Aktualisieren Sie bei Bedarf variable Inhalte oder Personalisierungen. Von Meta gesperrte Felder (grau dargestellt) können nicht bearbeitet werden. Um gesperrte Inhalte zu ändern, müssen Sie das Template bearbeiten und erneut zur Genehmigung einreichen.
5. Verwenden Sie den Tab **Test**, um eine Vorschau der Nachricht anzuzeigen, Body-Variablen zu aktualisieren und vor dem Versand zu bestätigen, dass die Nachricht wie erwartet aussieht.

Weitere Informationen zum Erstellen von WhatsApp-Campaigns finden Sie unter [Eine WhatsApp-Nachricht erstellen]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message).

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wie lange dauert die Template-Überprüfung durch Meta? {#how-long-does-meta-template-review-take}

Überprüfungen werden in der Regel innerhalb von fünf Minuten abgeschlossen, können aber bis zu 24 Stunden dauern.

### Kann ich ein Template bearbeiten, nachdem es genehmigt wurde? {#can-i-edit-a-template-after-its-been-approved}

Sie können variable Inhalte und Personalisierung beim Erstellen einer Campaign oder eines Canvas aktualisieren. Änderungen an gesperrten Inhalten (Fließtext, Button-Layout oder andere von Meta kontrollierte Felder) erfordern das Erstellen eines neuen Templates im Template-Builder oder das Bearbeiten des Templates in Metas WhatsApp Manager und das Warten auf eine erneute Genehmigung durch Meta. Wenn Sie [Klick-Tracking]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/click_tracking) verwenden, lesen Sie diesen Artikel, bevor Sie in Braze erstellte Templates in Metas WhatsApp Manager bearbeiten.

### Was passiert mit Templates, die ich eingereicht habe, bevor der Template-Builder verfügbar war? {#what-happens-to-templates-i-submitted-before-the-template-builder-was-available}

Templates, die im Meta Business Manager erstellt wurden, sind weiterhin in Braze verfügbar. Der Template-Builder ist eine zusätzliche Möglichkeit, Templates zu erstellen und zu verwalten, ohne das Braze-Dashboard zu verlassen.

### Warum kann ich nicht in jedem Feld Personalisierung hinzufügen? {#why-cant-i-add-personalization-to-every-field}

Meta schränkt ein, welche Teile eines Templates personalisiert werden können. Der **+**-Plus-Button erscheint nur in Feldern, die variable Inhalte unterstützen.