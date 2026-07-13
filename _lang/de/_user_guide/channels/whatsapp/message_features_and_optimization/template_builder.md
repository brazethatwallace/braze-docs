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

## Template erstellen {#create-a-template}

### 1. Schritt: WhatsApp-Templates aufrufen {#step-1-go-to-whatsapp-templates}

Gehen Sie zu **Inhalt** > **WhatsApp** und wählen Sie **Neues Template erstellen**.

![WhatsApp-Templates-Seite mit Button zum Erstellen eines neuen Templates.]({% image_buster /assets/img/whatsapp/templates/create_whatsapp_template.png %})

### 2. Schritt: Template-Einstellungen konfigurieren {#step-2-configure-template-settings}

Füllen Sie die folgenden Felder aus:

| Feld | Beschreibung |
| ----- | ----- |
| **Konto** | Das WhatsApp Business Account (WABA), bei dem Sie das Template einreichen möchten. Alle Abo-Gruppen und Telefonnummern innerhalb eines WABA teilen sich den Template-Zugriff. |
| **Sprache** | Die Sprache für dieses Template. WhatsApp erfordert ein separates Template für jede Sprache. |
| **Template-Name** | Ein eindeutiger Name für Ihr Template. Template-Namen dürfen nur Kleinbuchstaben, Zahlen und Unterstriche enthalten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="2. Schritt: Template-Einstellungen konfigurieren" }

### 3. Schritt: Layout auswählen {#step-3-choose-a-layout}

Wählen Sie unter **Layout** den Template-Typ:

- **Standard:** Eine Standard-WhatsApp-Nachricht. Dies ist das in diesem Artikel behandelte Layout.
- **Karussell:** Eine Nachricht mit horizontal scrollbaren Karten. Weitere Informationen finden Sie unter [Karussell-Templates]({{site.baseurl}}/whatsapp_carousel_templates).

### 4. Schritt: Template erstellen {#step-4-build-your-template}

#### Header (optional) {#header-optional}

Fügen Sie einen Header hinzu, der über dem Nachrichtentext erscheint. Sie können wählen:

- **Text:** Ein kurzer Text-Header.
- **Medien:** Ein Bild, Video oder Dokument (nur URL). Braze speichert die Medienreferenz und reicht ein Beispiel bei Meta zur Genehmigung ein.
- **Keiner:** Kein Header

#### Body {#body}

Geben Sie den Hauptinhalt Ihrer Nachricht ein und personalisieren Sie den Text nach Bedarf mit Liquid oder generischen Variablen:

{% raw %}
- Verwenden Sie Liquid-Tags (zum Beispiel `{{${first_name}}}`). Braze speichert Ihr Liquid und stellt es bereit, wenn Sie das Template in einem Campaign- oder Canvas-Editor verwenden.
- Verwenden Sie generische Variablen, wie nummerierte Platzhalter (zum Beispiel `{{1}}`), wenn Sie die Personalisierung erst später beim Erstellen Ihrer Nachricht hinzufügen möchten.
{% endraw %}

Sie können überall dort Personalisierung hinzufügen, wo der **+**-Plus-Button erscheint. Nicht alle Felder unterstützen Personalisierung.

#### Fußzeile (optional) {#footer-optional}

Fügen Sie eine kurze Fußzeile hinzu, die unter dem Nachrichtentext erscheint.

#### Buttons (optional) {#buttons-optional}

Fügen Sie Ihrem Template bis zu 10 Buttons hinzu. Button-Typen haben unterschiedliche Kategorien und Spezifikationen.

| Button-Typ | Kategorie | Spezifikationen |
| --- | --- | --- |
| Schnellantwort | Schnellantwort-Buttons |{::nomarkdown}<ul><li><b>Maximale Anzahl:</b> 10</li><li><b>Button-Text:</b> Bis zu 25 Zeichen</li></ul> {:/}|
| Telefonnummer | Call-to-Action-Buttons | {::nomarkdown}<ul><li><b>Maximale Anzahl:</b> 1</li><li><b>Button-Text:</b> Bis zu 25 Zeichen</li><li><b>Telefonnummer:</b> Gültige Telefonnummer mit Ländervorwahl, ohne + (z. B. „14155552671“)</li></ul> {:/}|
| Website besuchen | Call-to-Action-Buttons | {::nomarkdown}<ul><li><b>Maximale Anzahl:</b> 2</li><li><b>Button-Text:</b> Bis zu 25 Zeichen</li><li><b>Website-URL:</b> Bis zu 2.000 Zeichen</li></ul> {:/}|
| Angebotscode kopieren | Call-to-Action-Buttons | {::nomarkdown}<ul><li><b>Maximale Anzahl:</b> 1</li><li><b>Button-Text:</b> „Copy offer code“ (kann nicht bearbeitet werden)</li><li><b>Angebotscode:</b> Bis zu 15 Zeichen</li></ul> {:/}|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Buttons (optional)" }

![WhatsApp-Template-Editor mit Schnellantwort- und Call-to-Action-Buttons.]({% image_buster /assets/img/whatsapp/templates/buttons.png %})

### 5. Schritt: Template-Vorschau anzeigen {#step-5-preview-your-template}

Sehen Sie sich vor dem Einreichen eine Vorschau an, wie Ihre Nachricht für Empfänger:innen aussehen wird:

- **Vorschau als Nutzer:in:** Sehen Sie eine generische Vorschau der Nachricht.
- **Vorschau als bestimmte:r Nutzer:in:** Wählen Sie ein Nutzerprofil aus, um zu sehen, wie das Template mit den Daten dieser Person dargestellt wird.

### 6. Schritt: Zur Überprüfung einreichen {#step-6-submit-for-review}

Wählen Sie **Senden**, um Ihr Template zur Überprüfung an Meta zu senden. Die Überprüfung dauert in der Regel wenige Minuten, kann aber bis zu 24 Stunden in Anspruch nehmen. Das Template erscheint auf Ihrer **WhatsApp-Templates**-Seite, sobald es eingereicht wurde, und der Status wird aktualisiert, wenn Sie die **WhatsApp-Templates**-Seite aktualisieren.

## Unterstützte Template-Kategorien {#supported-template-categories}

Im WhatsApp-Template-Builder werden derzeit nur Marketing-Templates unterstützt.

## Ein genehmigtes Template in einer Campaign verwenden {#use-an-approved-template-in-a-campaign}

Nachdem Meta Ihr Template genehmigt hat, können Sie es in einer WhatsApp-Campaign oder einem Canvas verwenden.

1. Gehen Sie zu **Campaigns** und wählen Sie **Kampagne erstellen** > **WhatsApp**.
2. Wählen Sie im Nachrichten-Editor Ihr genehmigtes Template aus.
3. Braze füllt den Inhalt des Templates automatisch aus – einschließlich aller Medien und Liquid-Elemente, die Sie bei der Template-Erstellung eingegeben haben – sodass Sie diese nicht erneut eingeben müssen.
4. Aktualisieren Sie bei Bedarf variable Inhalte oder Personalisierungen. Von Meta gesperrte Felder (grau dargestellt) können nicht bearbeitet werden. Um gesperrte Inhalte zu ändern, müssen Sie das Template bearbeiten und erneut zur Genehmigung einreichen.
5. Verwenden Sie den Tab **Test**, um eine Vorschau der Nachricht anzuzeigen, Text-Variablen zu aktualisieren und zu bestätigen, dass die Nachricht vor dem Start wie erwartet aussieht.

Weitere Informationen zum Erstellen von WhatsApp-Campaigns finden Sie unter [WhatsApp-Nachricht erstellen]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message).

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wie lange dauert die Meta-Template-Überprüfung? {#how-long-does-meta-template-review-take}

Überprüfungen werden in der Regel innerhalb von fünf Minuten abgeschlossen, können aber bis zu 24 Stunden dauern.

### Kann ich ein Template nach der Genehmigung bearbeiten? {#can-i-edit-a-template-after-its-been-approved}

Alle Änderungen an gesperrten Inhalten (Textkörper oder andere von Meta kontrollierte Felder) erfordern eine erneute Einreichung des Templates zur Genehmigung, die über den WhatsApp Business Manager erfolgen muss. Sie können Inhalte und Personalisierungen beim Erstellen Ihrer Campaign oder Ihres Canvas aktualisieren.

### Was passiert mit Templates, die ich vor der Verfügbarkeit des Template Builders eingereicht habe? {#what-happens-to-templates-i-submitted-before-the-template-builder-was-available}

Templates, die im Meta Business Manager erstellt wurden, sind weiterhin in Braze verfügbar. Der Template Builder ist eine zusätzliche Möglichkeit, Templates zu erstellen und zu verwalten, ohne das Braze-Dashboard verlassen zu müssen.

### Warum kann ich nicht in jedem Feld Personalisierung hinzufügen? {#why-cant-i-add-personalization-to-every-field}

Meta schränkt ein, welche Teile eines Templates personalisiert werden können. Der **+**-Plus-Button erscheint nur in Feldern, die variable Inhalte unterstützen.