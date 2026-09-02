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

> Mit dem WhatsApp-Template-Builder können Sie WhatsApp-Nachrichten-Templates direkt in Braze erstellen und einreichen – ohne zwischen Braze und dem Meta Business Manager:in wechseln zu müssen. Nachdem Meta Ihr Template genehmigt hat, können Sie es in beliebig vielen Campaigns und Canvase verwenden.

## Voraussetzungen {#prerequisites}

{% multi_lang_include whatsapp/template_prerequisites.md %}

## Ein Template erstellen {#create-a-template}

### Schritt 1: WhatsApp-Templates aufrufen {#step-1-go-to-whatsapp-templates}

Gehen Sie zu **Inhalte** > **Templates** > **WhatsApp** und wählen Sie **Neues Template erstellen**.

![WhatsApp-Templates-Seite mit Button zum Erstellen eines neuen Templates.]({% image_buster /assets/img/whatsapp/templates/create_whatsapp_template.png %})

Sie können ein Template auch beim Erstellen einer WhatsApp-Campaign oder eines Canvas erstellen. Weitere Informationen finden Sie unter [Ein Template aus einer Campaign oder einem Canvas erstellen](#create-a-template-from-a-campaign-or-canvas).

### Schritt 2: Kategorie und Typ auswählen {#step-2-choose-a-category-and-type}

Wählen Sie eine Template-Kategorie und einen Template-Typ aus und klicken Sie dann auf **Weiter zum Template**, wenn Sie bereit sind.

{% alert note %}
Meta überprüft Templates anhand von [Kategorierichtlinien](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-categorization) und Inhalten.
{% endalert %}

#### Marketing {#marketing}

Marketing-Templates sind für Werbe- und Engagement-Nachrichten gedacht (zum Beispiel Willkommensnachrichten, Aktionen, Angebote, Gutscheine, Newsletter und Ankündigungen).

| Typ | Beschreibung |
| --- | --- |
| **Angepasst** | Eine Standard-WhatsApp-Nachricht, die Sie von Grund auf erstellen. Dies ist das Layout, das unter [Ihr Template erstellen](#step-4-build-your-template) beschrieben wird. |
| **Karussell** | Eine Nachricht mit horizontal scrollbaren Karten. Weitere Informationen finden Sie unter [Karussell-Templates]({{site.baseurl}}/whatsapp_carousel_templates). |
| **Zeitlich begrenztes Angebot** | Ein zeitlich begrenztes Werbeangebot. Weitere Informationen finden Sie unter [Templates für zeitlich begrenzte Angebote]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/message_and_image_formats#limited-time-offer-templates). |
| **Flow** | Ein Template, das einen WhatsApp-Flow öffnet (zum Beispiel Umfragen oder Terminbuchungen). Erstellen und verwalten Sie den Flow in Metas WhatsApp Manager:in und wählen Sie ihn dann beim Erstellen des Templates aus. Weitere Informationen finden Sie unter [WhatsApp Flows]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/whatsapp_flows). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Marketing-Template-Typen" }

#### Utility {#utility}

Utility-Templates sind für nicht-werbliche Nachrichten gedacht (zum Beispiel Bestellbestätigungen, Kontoaktualisierungen, Quittungen, Terminerinnerungen und Abrechnungen). Meta klassifiziert Werbeinhalte als Marketing um.

| Typ | Beschreibung |
| --- | --- |
| **Angepasst** | Eine Standard-Utility-Nachricht, die Sie von Grund auf erstellen. Folgen Sie denselben Schritten wie unter [Ihr Template erstellen](#step-4-build-your-template). |
| **Flow** | Ein Utility-Flow-Template (zum Beispiel Erinnerungen, Feedback oder Bestellverwaltung). Erstellen und verwalten Sie den Flow in Metas WhatsApp Manager:in und wählen Sie ihn dann beim Erstellen des Templates aus. Weitere Informationen finden Sie unter [WhatsApp Flows]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/whatsapp_flows). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Utility-Template-Typen" }

{% alert note %}
Karussell- und zeitlich begrenzte Angebotslayouts sind nur für Marketing-Templates verfügbar.
{% endalert %}

### Schritt 3: Template-Einstellungen konfigurieren {#step-3-configure-template-settings}

Füllen Sie die folgenden Felder aus:

| Feld | Beschreibung |
| ----- | ----- |
| **Konto** | Das WhatsApp Business-Konto (WABA), bei dem Sie das Template einreichen möchten. Alle Abo-Gruppen und Telefonnummern innerhalb eines WABA teilen den Template-Zugriff. |
| **Sprache** | Die Sprache für dieses Template. WhatsApp erfordert ein separates Template für jede Sprache. |
| **Template-Name** | Ein eindeutiger Name für Ihr Template. Template-Namen dürfen nur Kleinbuchstaben, Zahlen und Unterstriche enthalten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 3: Template-Einstellungen konfigurieren" }

### Schritt 4: Ihr Template erstellen {#step-4-build-your-template}

#### Header (optional) {#header-optional}

Fügen Sie einen Header hinzu, der vor dem Nachrichtentext angezeigt wird. Sie können wählen:

- **Text:** Ein kurzer Text-Header.
- **Medien:** Ein Bild, Video oder Dokument (nur URL). Braze speichert die Medienreferenz und reicht ein Beispiel bei Meta zur Genehmigung ein.
- **Keiner:** Kein Header

#### Body {#body}

Geben Sie den Hauptinhalt Ihrer Nachricht ein und personalisieren Sie den Body nach Bedarf mit Liquid oder generischen Variablen:

{% raw %}
- Verwenden Sie Liquid-Tags (zum Beispiel `{{${first_name}}}`). Braze speichert Ihr Liquid und zeigt es an, wenn Sie das Template in einer Campaign oder einem Canvas-Composer verwenden.
- Verwenden Sie generische Variablen wie nummerierte Platzhalter (zum Beispiel `{{1}}`), wenn Sie die Personalisierung lieber später beim Erstellen Ihrer Nachricht hinzufügen möchten.
{% endraw %}

Sie können überall dort Personalisierung hinzufügen, wo der **+**-Plus-Button angezeigt wird. Nicht alle Felder unterstützen Personalisierung.

#### Liquid-Zeichenlimits {#liquid-character-limits}

Meta legt Zeichenlimits für die Template-Struktur fest, die Sie zur Genehmigung einreichen (zum Beispiel 1.024 Zeichen für den Body und 60 Zeichen für einen Text-Header). Im Template-Builder gelten diese Limits für das Template, das an Meta gesendet wird, nicht für die endgültige gerenderte Nachricht zum Sendezeitpunkt.

- **{% raw %}`{{ }}`{% endraw %}-Variablen:** Braze wandelt Liquid-Variablen in nummerierte Platzhalter ({% raw %}`{{1}}`, `{{2}}`{% endraw %}) um, bevor die Länge geprüft wird. Ein langer Ausdruck wie {% raw %}`{{${first_name}}}`{% endraw %} zählt als kurzer Platzhalter, nicht als vollständige Liquid-Syntax.
- **{% raw %}`{% %}`{% endraw %}-Tags:** Liquid-Logik-Tags zählen als Literaltext in voller Länge und erscheinen als nicht editierbarer Text in Template-Nachrichten.

Für komplexe Personalisierung verwenden Sie einen [Kontextschritt]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties), um Werte zu berechnen, und referenzieren dann kürzere Variablen im Template. Informationen zu Message Extras und Einschränkungen bei bedingter Logik finden Sie unter [Liquid im WhatsApp-Template-Builder]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder/template_builder_liquid).

#### Fußzeile (optional) {#footer-optional}

Fügen Sie eine kurze Fußzeile hinzu, die nach dem Nachrichtentext angezeigt wird.

#### Buttons (optional) {#buttons-optional}

Fügen Sie Ihrem Template bis zu 10 Buttons hinzu. Button-Typen haben verschiedene Kategorien und Spezifikationen und werden nach Kategorie nach dem Nachrichtentext gruppiert. Standardmäßig erscheinen Schnellantwort-Buttons zuerst. Um die Reihenfolge zu ändern – zum Beispiel um Schnellantwort-Buttons nach Call-to-Action-Buttons zu verschieben – wählen Sie **Gruppenreihenfolge tauschen**.

| Button-Typ | Kategorie | Spezifikationen |
| --- | --- | --- |
| Schnellantwort | Schnellantwort-Buttons |{::nomarkdown}<ul><li><b>Maximale Anzahl:</b> 10</li><li><b>Button-Text:</b> Bis zu 25 Zeichen</li></ul> {:/}|
| Telefonnummer | Call-to-Action-Buttons | {::nomarkdown}<ul><li><b>Maximale Anzahl:</b> 1</li><li><b>Button-Text:</b> Bis zu 25 Zeichen</li><li><b>Telefonnummer:</b> Gültige Telefonnummer mit Landesvorwahl, ohne + (zum Beispiel „14155552671“)</li></ul> {:/}|
| Website besuchen | Call-to-Action-Buttons | {::nomarkdown}<ul><li><b>Maximale Anzahl:</b> 2</li><li><b>Button-Text:</b> Bis zu 25 Zeichen</li><li><b>Website-URL:</b> Bis zu 2.000 Zeichen</li></ul> {:/}|
| Angebotscode kopieren | Call-to-Action-Buttons | {::nomarkdown}<ul><li><b>Maximale Anzahl:</b> 1</li><li><b>Button-Text:</b> „Copy offer code“ (kann nicht bearbeitet werden)</li><li><b>Angebotscode:</b> Bis zu 15 Zeichen</li></ul> {:/}|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Buttons (optional)" }

Für Flow-Templates konfigurieren Sie den Flow-Button und wählen einen bestehenden Flow aus Meta aus, anstatt Standard-Call-to-Action-Buttons hinzuzufügen.

### Schritt 5: Vorschau Ihres Templates {#step-5-preview-your-template}

Bevor Sie es einreichen, sehen Sie in der Vorschau, wie Ihre Nachricht bei Empfänger:innen angezeigt wird:

- **Vorschau als Nutzer:in:** Sehen Sie eine generische Vorschau der Nachricht.
- **Vorschau als bestimmte:r Nutzer:in:** Wählen Sie ein Kundenprofil or Nutzerprofil aus, um zu sehen, wie das Template mit den Daten dieser/dieses Nutzers/Nutzerin gerendert wird.

### Schritt 6: Zur Überprüfung einreichen {#step-6-submit-for-review}

Wählen Sie **Einreichen**, um Ihr Template zur Überprüfung an Meta zu senden. Die Überprüfung dauert in der Regel einige Minuten, kann jedoch bis zu 24 Stunden in Anspruch nehmen. Das Template erscheint auf Ihrer Seite **WhatsApp-Templates**, sobald es eingereicht wurde, und der Status wird aktualisiert, wenn Sie die Seite **WhatsApp-Templates** Update or aktualisieren or aktualisieren.

## Ein Template aus einer Campaign oder einem Canvas erstellen {#create-a-template-from-a-campaign-or-canvas}

Sie können ein WhatsApp-Template erstellen und einreichen, ohne eine Campaign oder einen Canvas-Nachrichtenschritt verlassen zu müssen.

1. Wählen Sie in einer WhatsApp-[Campaign]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message) oder einem Canvas-Nachrichtenschritt den Nachrichtentyp **WhatsApp-Template-Nachricht** aus.
2. Wählen Sie **Neues Template erstellen** aus.
3. Wählen Sie eine Kategorie und einen Typ aus und erstellen und reichen Sie das Template auf dieselbe Weise ein wie auf der WhatsApp-Templates-Seite.
4. Nach dem Einreichen bindet Braze das ausstehende Template an die Nachricht. Fahren Sie mit der Personalisierung fort, während das Template ausstehend ist, und starten Sie es, nachdem Meta es genehmigt hat.

Wählen Sie **Template aus Bibliothek auswählen**, um den Builder zu verlassen und stattdessen ein vorhandenes Template auszuwählen.

{% alert note %}
Wenn Sie ein Template aus einer Campaign oder einem Canvas erstellen, kann Braze Ihre Arbeit als Entwurf speichern, damit sie erhalten bleibt, wenn Sie den Nachrichtenschritt verlassen.
{% endalert %}

## Ein genehmigtes Template in einer Campaign verwenden {#use-an-approved-template-in-a-campaign}

Nachdem Meta Ihr Template genehmigt hat, können Sie es in einer WhatsApp-Campaign oder einem Canvas verwenden.

1. Gehen Sie zu **Campaigns** und wählen Sie **Campaign erstellen** > **WhatsApp**.
2. Wählen Sie im Nachrichten-Editor Ihr genehmigtes Template aus.
3. Braze befüllt automatisch den Inhalt des Templates – einschließlich aller Medien und Liquid, die Sie bei der Template-Erstellung eingegeben haben – sodass Sie ihn nicht erneut eingeben müssen.
4. Update or aktualisieren or aktualisieren Sie Variableninhalte oder Personalisierung nach Bedarf. Von Meta gesperrte Felder (grau dargestellt) können nicht bearbeitet werden. Um gesperrte Inhalte zu ändern, müssen Sie das Template bearbeiten und erneut zur Genehmigung einreichen.
5. Verwenden Sie den Tab **Test**, um eine Vorschau der Nachricht anzuzeigen, Body-Variablen zu Update or aktualisieren or aktualisieren und zu bestätigen, dass die Nachricht vor dem Senden wie erwartet aussieht.

Weitere Informationen zum Erstellen von WhatsApp-Campaigns finden Sie unter [Eine WhatsApp-Nachricht erstellen]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message).

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wie lange dauert die Template-Überprüfung durch Meta? {#how-long-does-meta-template-review-take}

Überprüfungen werden in der Regel innerhalb von fünf Minuten abgeschlossen, können aber bis zu 24 Stunden dauern.

### Kann ich ein Template bearbeiten, nachdem es genehmigt wurde? {#can-i-edit-a-template-after-its-been-approved}

Sie können variable Inhalte und Personalisierung beim Erstellen einer Campaign oder eines Canvas Update or aktualisieren or aktualisieren. Änderungen an gesperrten Inhalten (Fließtext, Button-Layout oder andere von Meta kontrollierte Felder) erfordern das Erstellen eines neuen Templates im Template-Builder oder das Bearbeiten des Templates im WhatsApp Manager:in von Meta und das Warten auf eine erneute Genehmigung durch Meta. Wenn Sie [Klick-Tracking]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/click_tracking) verwenden, lesen Sie diesen Artikel, bevor Sie in Braze erstellte Templates im WhatsApp Manager:in von Meta bearbeiten.

### Was passiert mit Templates, die ich vor der Verfügbarkeit des Template-Builders eingereicht habe? {#what-happens-to-templates-i-submitted-before-the-template-builder-was-available}

Templates, die im Meta Business Manager:in erstellt wurden, können weiterhin in Braze verwendet werden. Der Template-Builder ist eine zusätzliche Möglichkeit, Templates zu erstellen und zu verwalten, ohne das Braze-Dashboard zu verlassen.

### Warum kann ich nicht in jedem Feld Personalisierung hinzufügen? {#why-cant-i-add-personalization-to-every-field}

Meta schränkt ein, welche Teile eines Templates personalisiert werden können. Der **+**-Plus-Button erscheint nur in Feldern, die variable Inhalte unterstützen.