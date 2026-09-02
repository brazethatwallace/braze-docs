---
nav_title: Karussell-Templates
article_title: WhatsApp-Karussell-Templates
description: "Dieser Referenzartikel behandelt WhatsApp-Karussell-Templates."
tool:
  - WhatsApp
alias: /whatsapp_carousel_templates/
toc_headers: h2
---

# WhatsApp-Karussell-Templates {#whatsapp-carousel-templates}

> Mit WhatsApp-Karussell-Templates können Sie interaktive Nachrichten mit mehreren Karten erstellen, durch die Nutzer:innen wischen können. Jedes Karussell kann bis zu 10 Karten mit Bildern oder Videos sowie anpassbare Buttons für das Engagement enthalten. Dieses Feature eignet sich ideal, um Ihre Produkte und Serviceleistungen oder mehrstufige Inhalte in einem visuell ansprechenden Format zu präsentieren.

## Voraussetzungen {#prerequisites}

{% multi_lang_include whatsapp/template_prerequisites.md %}

## Karussell-Template erstellen {#create-a-carousel-template}

Sie können Karussell-Templates innerhalb von Braze mit dem WhatsApp-Template-Builder erstellen. Wenn Sie Templates erstellen, validiert Braze Ihre Inhalte, um die Kriterien von Meta zu erfüllen.

Beim Erstellen eines Templates in Braze können Sie Folgendes verwenden:
- Liquid, das Sie beim Senden der Nachricht voraussichtlich verwenden werden. Braze speichert dies für zukünftige Referenz.
- Generische Variablen wie {% raw %}`{{1}}`{% endraw %}.

{% alert note %}
{% raw %}`{% %}`{% endraw %} Liquid-Tags werden im Template-Builder nicht unterstützt, da sie die Inhaltskriterien von Meta nicht erfüllen.
{% endalert %}

Nachdem das Template eingereicht wurde, erscheint es in der Template-Liste des WABA und wird innerhalb von 24 Stunden überprüft. Eine Überprüfung erfolgt jedoch oft innerhalb weniger Minuten.

### Schritt 1: Auf den Template-Builder zugreifen {#step-1-access-the-template-builder}

1. Gehen Sie in Braze zu **Templates**.
2. Wählen Sie **WhatsApp Templates** aus den verfügbaren Optionen aus.

![WhatsApp-Templates im Template-Navigationsmenü.]({% image_buster /assets/img/whatsapp/templates/whatsapp_templates.png %}){: style="max-width:70%;"}

{: start="3"}
3. Wählen Sie **Create Carousel Template** aus.

![Button zum Erstellen eines Karussell-Templates.]({% image_buster /assets/img/whatsapp/templates/create_carousel_template.png %})

### Schritt 2: Template-Einstellungen konfigurieren {#step-2-configure-template-settings}

Füllen Sie die Pflichtfelder aus.

| Feld | Beschreibung |
| --- | --- |
| WhatsApp Business Account | Wählen Sie das WABA aus, in dem dieses Template gespeichert wird. Beachten Sie, dass alle Abo-Gruppen und Telefonnummern innerhalb dieses WABA Zugriff auf das Template haben. |
| Template-Sprache | Wählen Sie die Sprache für Ihr Template aus. Meta beschränkt Templates auf eine einzelne Sprache, wählen Sie also die Sprache, die Ihre Zielgruppe sehen wird. |
| Template-Name | Geben Sie einen aussagekräftigen Namen ein, der Ihnen hilft, dieses Template später zu identifizieren. Template-Namen dürfen keine Leerzeichen enthalten – verwenden Sie Unterstriche oder entfernen Sie Leerzeichen vollständig (z. B. `carousel_example` oder `carouselexample`). |
| Kategorie | Wird automatisch auf **Marketing** gesetzt. Alle Karussell-Nachrichten werden als Marketing-Nachrichten kategorisiert. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 2: Template-Einstellungen konfigurieren" }

![Panel mit WhatsApp-Template-Details, in dem ein WhatsApp Business Account ausgewählt ist, Englisch als Template-Sprache eingestellt und als Template-Name „welcome_message“ eingetragen ist.]({% image_buster /assets/img/whatsapp/templates/whatsapp_template_details.png %}){: style="max-width:70%"}

### Schritt 3: Textinhalt hinzufügen {#step-3-add-body-content}

Jede Karussell-Nachricht muss mit einem Textinhalt beginnen, also Text, der vor den Karussell-Karten angezeigt wird.

Sie können Liquid-Variablen zur Personalisierung einbinden, z. B. {% raw %}`{{first_name}}`{% endraw %}, wodurch ein leerer Variablen-Platzhalter erstellt wird, der mit dynamischem Content gefüllt oder später bei der Verwendung des Templates in Campaigns angepasst werden kann. Variablen können nicht ganz am Anfang oder Ende des Textinhalts platziert werden.

### Schritt 4: Karussell-Einstellungen konfigurieren {#step-4-configure-carousel-settings}

Bevor Sie einzelne Karten erstellen, definieren Sie die Gesamtstruktur des Karussells mit den Karussell-Einstellungen. Diese Einstellungen gelten für alle Karten und können nach der Template-Einreichung nicht mehr geändert werden.

#### Medientyp {#media-type}

Wählen Sie den Medientyp: **Image** oder **Video**. Dieser wird für alle Karten verwendet.

![Editor mit Optionen zur Auswahl des Medientyps „Image“ oder „Video“.]({% image_buster /assets/img/whatsapp/templates/media_types.png %})

#### Button-Konfiguration {#button-configuration}

Wählen Sie den Button-Typ: **Quick Reply**, **Phone Number** oder **Visit Website**. Diese Konfiguration wird für alle Karten verwendet. Wählen Sie dann bis zu zwei Buttons pro Karte aus.

### Schritt 5: Karussell-Karten erstellen {#step-5-create-carousel-cards}

Jetzt können Sie einzelne Karussell-Karten erstellen. Alle Karten behalten die gleiche Form und Struktur bei. Sie können bis zu 10 Karten hinzufügen, müssen aber mindestens zwei Karten hinzufügen.

{% alert important %}
Sie können die Anzahl der Karten nicht mehr ändern, nachdem Sie das Template zur Überprüfung an Meta eingereicht haben.
{% endalert %}

1. Laden Sie ein Bild oder Video hoch, je nach dem ausgewählten Medientyp.
2. Fügen Sie Kartentext oder eine Beschreibung hinzu.
3. Konfigurieren Sie Button-Text und -Aktionen.
4. Fügen Sie bei Bedarf Liquid-Variablen hinzu. Sie können sie überall dort einfügen, wo ein **+**-Plus-Button vorhanden ist.

#### Karte duplizieren {#duplicate-a-card}

Um eine vorhandene Karte zu kopieren, wählen Sie das Dreipunktmenü auf der Karte, die Sie duplizieren möchten, und wählen Sie **Duplicate card**. Braze kopiert die Medien, den Text und die Button-Konfiguration der Karte auf eine neue Karte, die am Ende des Karussells angehängt wird.

Sie können zwischen 2 und 10 Karten haben. **Duplicate card** ist nicht verfügbar, wenn das Karussell bereits 10 Karten enthält oder nachdem Sie das Template an Meta eingereicht haben (wenn die Kartenanzahl festgelegt ist).

{% alert tip %}
Verwenden Sie Liquid-Variablen strategisch, um Inhalte wie Rabattprozentsätze, Produktnamen oder nutzerspezifische Angebote zu personalisieren. Variablen können zu Kartentext, Button-Text und URLs hinzugefügt werden.
{% endalert %}

![Editor mit Beispiel-Karussell-Karten, die nahrhafte Lebensmittel bewerben.]({% image_buster /assets/img/whatsapp/templates/example_carousel_cards.png %})

### Schritt 6: Vorschau anzeigen und einreichen {#step-6-preview-and-submit}

1. Verwenden Sie den Bereich **Vorschau**, um zu sehen, wie Ihr Karussell für Nutzer:innen angezeigt wird.
2. Wählen Sie **Submit to Meta for review**, damit Braze das Template zur Genehmigung an Meta sendet.
3. Die Genehmigung dauert in der Regel wenige Minuten, kann aber bis zu 24 Stunden in Anspruch nehmen.
4. Überprüfen Sie den Template-Status in Ihrer **Templates**-Liste auf der WhatsApp-Template-Seite oder im Canvas- und Campaign-Selektor.

{% alert note %}
Testversand ist erst möglich, nachdem Meta das Template genehmigt hat. Der Template-Status wird während der Erstellung als **Draft** angezeigt und ändert sich nach Abschluss der Überprüfung durch Meta zu **Genehmigt**.
{% endalert %}

## Karussell-Templates verwenden {#use-carousel-templates}

Nachdem Ihr Karussell-Template von Meta genehmigt wurde, können Sie es in Campaigns und Canvase verwenden. Der Ablauf ist für beide Nachrichtentypen ähnlich.

### Schritt 1: WhatsApp-Nachricht erstellen {#step-1-create-a-whatsapp-message}

1. Gehen Sie in Braze zu **Campaigns** oder **Canvase** und erstellen Sie eine WhatsApp-Nachricht.
2. Wählen Sie die Abo-Gruppe aus, die dem WhatsApp Business Account (WABA) Ihres Templates entspricht.

{% alert important %}
Wenn Sie mehrere WhatsApp Business Accounts haben, wählen Sie eine Abo-Gruppe aus demselben WABA aus, in dem das Template erstellt wurde. Templates werden nicht zwischen WABAs geteilt, aber innerhalb desselben WABA über alle Abo-Gruppen und Telefonnummern hinweg gemeinsam genutzt.
{% endalert %}

### Schritt 2: Karussell-Template auswählen {#step-2-select-your-carousel-template}

1. Suchen Sie nach Ihrem Template anhand des Namens (z. B. „carousel_example“).
2. Überprüfen Sie, ob der Template-Status **Genehmigt** ist.
3. Wählen Sie das Template aus, um es in den Nachrichten-Editor zu laden.

### Schritt 3: Dynamischen Content anpassen {#step-3-customize-dynamic-content}

Wenn Ihr Template geladen wird, enthält es gesperrte und bearbeitbare Inhalte.

{% tabs local %}
{% tab Gesperrte Inhalte %}


- Statischer Text (alle Inhalte, die ohne Variablen eingereicht wurden) ist gesperrt und kann nicht bearbeitet werden.
- Die Anzahl der Karussellkarten ist festgelegt.
- Medientyp und Button-Konfiguration können nicht geändert werden.

{% endtab %}
{% tab Bearbeitbare Inhalte %}


{% raw %}
- Jedes Feld mit einer Variable kann mit anderem Liquid angepasst werden.
- Wenn Sie das Template mit Liquid eingereicht haben (z. B. `{{first_name}}`), bewahrt Braze dieses Liquid automatisch und zeigt es an.
- Sie können das Liquid auf andere Variablen ändern (z. B. von `{{first_name}}` zu `{{last_name}}` wechseln).
- Bilder mit Variablen können durch Verwendung von URLs mit Liquid dynamisch gestaltet werden.
- Sie können neue Bilder aus der Braze-Medienbibliothek hochladen, anstatt die eingereichten Medien zu verwenden.
{% endraw %}

#### Beispiel {#example}

{% raw %}Angenommen, Ihr Template enthält eine Variable für den Rabattprozentsatz: `{{discount_percentage}}`. In der Campaign können Sie diese beibehalten oder zu `{{custom_attributes.vip_discount}}` ändern.{% endraw %} Meta verlangt lediglich, dass der Variablen-Slot ausgefüllt ist – das konkret verwendete Liquid ist flexibel.

{% endtab %}
{% endtabs %}

### Schritt 4: Campaign oder Canvas starten {#step-4-launch-your-campaign-or-canvas}

Fahren Sie nach der Gestaltung mit dem Start-Workflow Ihrer Campaign oder Ihres Canvas fort, einschließlich Tests. Das Karussell-Template funktioniert wie jedes andere WhatsApp-Nachrichten-Template.

## Best Practices {#best-practices}

### Richtlinien für Inhalte {#content-guidelines}

- **Platzierung von Textinhalten:** Variablen dürfen nicht am Ende des Textinhalts stehen. Fügen Sie nach jeder Variable mindestens ein Wort oder ein Satzzeichen hinzu.
- **Einheitliche Kartenstruktur:** Alle Karten müssen dieselbe Form, denselben Medientyp und dieselbe Button-Konfiguration aufweisen. Planen Sie Ihre Inhalte entsprechend.
- **Optimale Kartenanzahl:** Sie können zwar bis zu 10 Karten erstellen, sollten aber die Nutzer:innenerfahrung berücksichtigen. Zu viele Karten können überwältigend sein; 3–5 Karten eignen sich für die meisten Anwendungsfälle.
- **Standardwerte:** Wenn Sie Liquid-Variablen verwenden, geben Sie immer Standardwerte an, um eine korrekte Vorschau zu erhalten. So können Sie sicherstellen, dass die Nachricht korrekt angezeigt wird, auch wenn bestimmte Nutzerprofildaten fehlen.

### WhatsApp Business-Konten und Abo-Gruppen {#whatsapp-business-accounts-and-subscription-groups}

- **Template-Freigabe verstehen:** Templates werden über alle Abo-Gruppen innerhalb desselben WhatsApp Business-Kontos (WABA) hinweg geteilt, jedoch nicht zwischen verschiedenen WABAs. Planen Sie entsprechend, wenn Sie mehrere WABAs verwalten.
- **Nach WABA organisieren:** Wenn Sie mehrere WABAs haben, sollten Sie Ihre Templates nach Business-Konto organisieren, um Verwechslungen bei der Auswahl von Templates in Campaigns zu vermeiden.

### Testen und Genehmigung {#testing-and-approval}

- **Vorschau vor dem Einreichen:** Sehen Sie sich Ihre Templates immer in der Vorschau an, um Fehler zu erkennen, bevor Sie sie zur Genehmigung bei Meta einreichen.
- **Genehmigungszeit einplanen:** Die Genehmigung dauert zwar in der Regel nur wenige Minuten, aber berücksichtigen Sie mögliche Verzögerungen bei der Planung von Campaign-Starts.
- **Gründlich testen:** Testen Sie Ihr Karussell nach der Genehmigung mit echten Nutzerdaten, um sicherzustellen, dass alle Variablen korrekt befüllt werden und die Nutzer:innenerfahrung reibungslos ist.

## Fehlerbehebung {#troubleshooting}

| Problem | Lösung |
| --- | --- |
| Template erscheint nicht in der Campaign | Überprüfen Sie, ob die ausgewählte Abo-Gruppe zur selben WABA gehört wie das Template. Prüfen Sie außerdem, ob der Template-Status **Genehmigt** ist und nicht noch auf **Draft** oder **Pending** steht. |
| Variable kann nicht am Ende des Textkörpers platziert werden | Verschieben Sie die Variable weiter nach vorne im Text und fügen Sie mindestens ein Zeichen oder Satzzeichen danach ein. Dies ist eine Meta-Anforderung für WhatsApp-Templates. |
| Variablen werden im Test nicht befüllt | Stellen Sie sicher, dass Ihre Liquid-Syntax korrekt ist und die Attribute in Ihren Nutzerprofilen vorhanden sind. Prüfen Sie Variablennamen auf Tippfehler und überprüfen Sie, ob Standardwerte dort gesetzt sind, wo es sinnvoll ist. |
| Template-Name enthält Leerzeichen | Template-Namen dürfen keine Leerzeichen enthalten. Verwenden Sie stattdessen Unterstriche (`template_name`) oder entfernen Sie Leerzeichen vollständig (`templatename`). |
| Anzahl der Karten kann nicht geändert werden | Die Anzahl der Karten wird beim Erstellen des Templates festgelegt und kann nach dem Einreichen nicht mehr geändert werden. Wenn Sie eine andere Anzahl von Karten benötigen, müssen Sie ein neues Template erstellen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fehlerbehebung" }