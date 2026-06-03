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

## Ein Karussell-Template erstellen {#create-a-carousel-template}

Sie können Karussell-Templates in Braze mit dem WhatsApp-Template-Builder erstellen. Wenn Sie Templates erstellen, validiert Braze Ihre Inhalte, um die Kriterien von Meta zu erfüllen.

Beim Erstellen eines Templates in Braze können Sie entweder Folgendes verwenden:
- Liquid, das Sie beim Senden der Nachricht voraussichtlich verwenden werden. Braze speichert dies zur späteren Referenz.
- Generische Variablen wie {% raw %}`{{1}}`{% endraw %}.

{% alert note %}
{% raw %}`{% %}`{% endraw %} Liquid-Tags werden im Template-Builder nicht unterstützt, da sie die Inhaltskriterien von Meta nicht erfüllen.
{% endalert %}

Nach dem Einreichen erscheint das Template in der Template-Liste des WABA und wird innerhalb von 24 Stunden überprüft. Eine Überprüfung erfolgt jedoch häufig innerhalb weniger Minuten.

### 1. Schritt: Auf den Template-Builder zugreifen {#step-1-access-the-template-builder}

1. Gehen Sie in Braze zu **Templates**.
2. Wählen Sie **WhatsApp Templates** aus den verfügbaren Optionen.

![WhatsApp-Templates im Navigationsmenü „Templates“.]({% image_buster /assets/img/whatsapp/templates/whatsapp_templates.png %}){: style="max-width:70%;"}

{: start="3"}
3. Wählen Sie **Create Carousel Template**.

![Button zum Erstellen eines Karussell-Templates.]({% image_buster /assets/img/whatsapp/templates/create_carousel_template.png %})

### 2. Schritt: Template-Einstellungen konfigurieren {#step-2-configure-template-settings}

Füllen Sie die erforderlichen Felder aus.

| Feld | Beschreibung |
| --- | --- |
| WhatsApp Business Account | Wählen Sie das WABA aus, in dem dieses Template gespeichert wird. Beachten Sie, dass alle Abo-Gruppen und Telefonnummern innerhalb dieses WABA Zugriff auf das Template haben. |
| Template-Sprache | Wählen Sie die Sprache für Ihr Template. Meta beschränkt Templates auf eine einzelne Sprache, wählen Sie also die Sprache, die Ihre Zielgruppe sehen wird. |
| Template-Name | Geben Sie einen aussagekräftigen Namen ein, der Ihnen hilft, dieses Template später zu identifizieren. Template-Namen dürfen keine Leerzeichen enthalten – verwenden Sie Unterstriche oder entfernen Sie Leerzeichen vollständig (z. B. `carousel_example` oder `carouselexample`). |
| Kategorie | Wird automatisch auf **Marketing** gesetzt. Alle Karussell-Nachrichten werden als Marketing-Nachrichten kategorisiert. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 2: Configure template settings" }

![Panel mit WhatsApp-Template-Details, in dem ein WhatsApp Business Account ausgewählt ist, Englisch als Template-Sprache und „welcome_message“ als Template-Name.]({% image_buster /assets/img/whatsapp/templates/whatsapp_template_details.png %}){: style="max-width:70%"}

### 3. Schritt: Textinhalt hinzufügen {#step-3-add-body-content}

Jede Karussell-Nachricht muss mit einem Textinhalt beginnen, der über den Karussell-Karten angezeigt wird.

Sie können Liquid-Variablen zur Personalisierung einfügen, z. B. {% raw %}`{{first_name}}`{% endraw %}, wodurch ein leerer Variablen-Slot erstellt wird, der mit dynamischem Inhalt gefüllt oder später bei der Verwendung des Templates in Campaigns geändert werden kann. Variablen dürfen nicht ganz am Anfang oder Ende des Textinhalts platziert werden.

### 4. Schritt: Karussell-Einstellungen konfigurieren {#step-4-configure-carousel-settings}

Bevor Sie einzelne Karten erstellen, definieren Sie die Gesamtstruktur des Karussells mit den Karussell-Einstellungen. Diese Einstellungen gelten für alle Karten und können nach dem Einreichen des Templates nicht mehr geändert werden.

#### Medientyp {#media-type}

Wählen Sie den Medientyp: **Bild** oder **Video**. Dieser wird für alle Karten verwendet.

![Editor mit Optionen zur Auswahl eines Bild- oder Video-Medientyps.]({% image_buster /assets/img/whatsapp/templates/media_types.png %})

#### Button-Konfiguration {#button-configuration}

Wählen Sie den Button-Typ: **Quick Reply**, **Phone Number** oder **Visit Website**. Diese Konfiguration wird für alle Karten verwendet. Wählen Sie dann bis zu zwei Buttons pro Karte aus.

### 5. Schritt: Karussell-Karten erstellen {#step-5-create-carousel-cards}

Jetzt können Sie einzelne Karussell-Karten erstellen. Alle Karten behalten die gleiche Form und Struktur. Sie können bis zu 10 Karten hinzufügen, müssen aber mindestens zwei Karten hinzufügen.

{% alert important %}
Sie können die Anzahl der Karten nach dem Einreichen des Templates bei Meta zur Überprüfung nicht mehr ändern.
{% endalert %}

1. Laden Sie ein Bild oder Video hoch, je nach ausgewähltem Medientyp.
2. Fügen Sie Kartentext oder eine Beschreibung hinzu.
3. Konfigurieren Sie Button-Text und -Aktionen.
4. Fügen Sie bei Bedarf Liquid-Variablen hinzu. Sie können diese überall dort hinzufügen, wo ein **+**-Plus-Button vorhanden ist.

{% alert tip %}
Verwenden Sie Liquid-Variablen strategisch, um Inhalte wie Rabattprozentsätze, Produktnamen oder nutzerspezifische Angebote zu personalisieren. Variablen können zu Kartentext, Button-Text und URLs hinzugefügt werden.
{% endalert %}

![Editor mit Beispiel-Karussell-Karten, die nährende Lebensmittel bewerben.]({% image_buster /assets/img/whatsapp/templates/example_carousel_cards.png %})

### 6. Schritt: Vorschau anzeigen und einreichen {#step-6-preview-and-submit}

1. Verwenden Sie den Bereich **Preview**, um zu sehen, wie Ihr Karussell für Nutzer:innen angezeigt wird.
2. Wählen Sie **Submit to Meta for review**, damit Braze das Template zur Genehmigung an Meta sendet.
3. Die Genehmigung dauert in der Regel nur wenige Minuten, kann aber bis zu 24 Stunden in Anspruch nehmen.
4. Überprüfen Sie den Template-Status in Ihrer **Templates**-Liste auf der WhatsApp-Template-Seite oder im Canvas- und Campaign-Selektor.

{% alert note %}
Testsendungen sind erst nach der Genehmigung des Templates durch Meta verfügbar. Der Template-Status wird während der Erstellung als **Draft** angezeigt und ändert sich nach Abschluss der Überprüfung durch Meta zu **Approved**.
{% endalert %}

## Karussell-Templates verwenden {#use-carousel-templates}

Nachdem Ihr Karussell-Template von Meta genehmigt wurde, können Sie es in Campaigns und Canvases verwenden. Der Prozess ist für beide Nachrichtentypen ähnlich.

### 1. Schritt: Eine WhatsApp-Nachricht erstellen {#step-1-create-a-whatsapp-message}

1. Gehen Sie in Braze zu **Campaigns** oder **Canvases** und erstellen Sie eine WhatsApp-Nachricht.
2. Wählen Sie die Abo-Gruppe aus, die dem WhatsApp Business Account (WABA) Ihres Templates entspricht.

{% alert important %}
Wenn Sie mehrere WhatsApp Business Accounts haben, wählen Sie eine Abo-Gruppe aus demselben WABA, in dem das Template erstellt wurde. Templates werden nicht über WABAs hinweg geteilt, sondern über alle Abo-Gruppen und Telefonnummern innerhalb desselben WABA.
{% endalert %}

### 2. Schritt: Ihr Karussell-Template auswählen {#step-2-select-your-carousel-template}

1. Suchen Sie nach Ihrem Template anhand des Namens (z. B. „carousel_example“).
2. Überprüfen Sie, ob der Template-Status **Approved** ist.
3. Wählen Sie das Template aus, um es in den Nachrichten-Editor zu laden.

### 3. Schritt: Dynamische Inhalte anpassen {#step-3-customize-dynamic-content}

Wenn Ihr Template geladen wird, enthält es gesperrte und bearbeitbare Inhalte.

{% tabs local %}
{% tab Gesperrte Inhalte %}


- Statischer Text (alle Inhalte, die ohne Variablen eingereicht wurden) ist gesperrt und kann nicht bearbeitet werden.
- Die Anzahl der Karussell-Karten ist festgelegt.
- Medientyp und Button-Konfiguration können nicht geändert werden.

{% endtab %}
{% tab Bearbeitbare Inhalte %}


{% raw %}
- Jedes Feld mit einer Variable kann mit anderem Liquid geändert werden.
- Wenn Sie das Template mit Liquid eingereicht haben (z. B. `{{first_name}}`), bewahrt und zeigt Braze dieses Liquid automatisch an.
- Sie können das Liquid in andere Variablen ändern (z. B. von `{{first_name}}` zu `{{last_name}}` wechseln).
- Bilder mit Variablen können durch die Verwendung von URLs mit Liquid dynamisch gestaltet werden.
- Sie können neue Bilder aus der Braze-Medienbibliothek hochladen, anstatt die eingereichten Medien zu verwenden.
{% endraw %}

#### Beispiel {#example}

{% raw %}Angenommen, Ihr Template enthält eine Variable für den Rabattprozentsatz: `{{discount_percentage}}`. In der Campaign können Sie diese beibehalten oder zu `{{custom_attributes.vip_discount}}` ändern.{% endraw %} Meta verlangt nur, dass der Variablen-Slot gefüllt ist – das spezifische verwendete Liquid ist flexibel.

{% endtab %}
{% endtabs %}

### 4. Schritt: Ihre Campaign oder Ihr Canvas starten {#step-4-launch-your-campaign-or-canvas}

Fahren Sie nach der Erstellung mit Ihrem Campaign- oder Canvas-Start-Workflow fort, einschließlich Tests. Das Karussell-Template funktioniert wie jedes andere WhatsApp-Nachrichten-Template.

## Best Practices {#best-practices}

### Inhaltsrichtlinien {#content-guidelines}

- **Platzierung des Textinhalts:** Variablen dürfen nicht am Ende des Textinhalts platziert werden. Fügen Sie nach jeder Variable mindestens ein Wort oder Satzzeichen hinzu.
- **Einheitliche Kartenstruktur:** Alle Karten müssen die gleiche Form, den gleichen Medientyp und die gleiche Button-Konfiguration haben. Planen Sie Ihre Inhalte entsprechend.
- **Optimale Kartenanzahl:** Sie können zwar bis zu 10 Karten erstellen, aber bedenken Sie die Nutzererfahrung. Zu viele Karten können überwältigend sein; 3–5 Karten eignen sich für die meisten Anwendungsfälle gut.
- **Standardwerte:** Wenn Sie Liquid-Variablen verwenden, geben Sie immer Standardwerte für eine korrekte Vorschau an. Dies hilft sicherzustellen, dass die Nachricht korrekt angezeigt wird, falls bestimmte Nutzerprofildaten fehlen.

### WhatsApp Business Accounts und Abo-Gruppen {#whatsapp-business-accounts-and-subscription-groups}

- **Template-Freigabe verstehen:** Templates werden über alle Abo-Gruppen innerhalb desselben WhatsApp Business Account (WABA) geteilt, aber nicht über verschiedene WABAs hinweg. Planen Sie entsprechend, wenn Sie mehrere WABAs verwalten.
- **Nach WABA organisieren:** Wenn Sie mehrere WABAs haben, erwägen Sie, Ihre Templates nach Business Account zu organisieren, um Verwechslungen bei der Auswahl von Templates in Campaigns zu vermeiden.

### Tests und Genehmigung {#testing-and-approval}

- **Vorschau vor dem Einreichen:** Zeigen Sie immer eine Vorschau Ihrer Templates an, um Fehler zu erkennen, bevor Sie sie zur Genehmigung bei Meta einreichen.
- **Genehmigungszeit einplanen:** Obwohl die Genehmigung in der Regel nur wenige Minuten dauert, berücksichtigen Sie mögliche Verzögerungen bei der Planung von Campaign-Starts.
- **Gründlich testen:** Testen Sie Ihr Karussell nach der Genehmigung mit echten Nutzerdaten, um sicherzustellen, dass alle Variablen korrekt befüllt werden und die Nutzererfahrung nahtlos ist.

## Fehlerbehebung {#troubleshooting}

| Problem | Lösung |
| --- | --- |
| Template erscheint nicht in der Campaign | Überprüfen Sie, ob die ausgewählte Abo-Gruppe zum selben WABA wie das Template gehört. Prüfen Sie außerdem, ob der Template-Status **Approved** ist und sich nicht noch im Status **Draft** oder **Pending** befindet. |
| Variable kann nicht am Ende des Textkörpers platziert werden | Verschieben Sie die Variable weiter nach vorne im Text und fügen Sie mindestens ein Zeichen oder Satzzeichen danach hinzu. Dies ist eine Meta-Anforderung für WhatsApp-Templates. |
| Variablen werden im Test nicht befüllt | Stellen Sie sicher, dass Ihre Liquid-Syntax korrekt ist und die Attribute in Ihren Nutzerprofilen vorhanden sind. Prüfen Sie auf Tippfehler in Variablennamen und überprüfen Sie, ob Standardwerte dort gesetzt sind, wo es angemessen ist. |
| Template-Name enthält Leerzeichen | Template-Namen dürfen keine Leerzeichen enthalten. Verwenden Sie stattdessen Unterstriche (`template_name`) oder entfernen Sie Leerzeichen vollständig (`templatename`). |
| Anzahl der Karten kann nicht geändert werden | Die Anzahl der Karten wird bei der Erstellung des Templates festgelegt und kann nach dem Einreichen nicht mehr geändert werden. Wenn Sie eine andere Anzahl von Karten benötigen, müssen Sie ein neues Template erstellen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting" }