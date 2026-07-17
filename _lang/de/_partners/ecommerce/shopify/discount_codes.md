---
nav_title: Eindeutige Rabattcodes
article_title: Eindeutige Rabattcodes versenden
alias: /shopify_discount_codes/
page_order: 7
description: "Dieser Referenzartikel behandelt einen von der Community eingereichten Anwendungsfall zur Verwendung von Braze-Aktionscodes mit dem Shopify Bulk Discount Code Bot, um eindeutige Rabattcodes über Ihre Campaigns und Canvases zu versenden."
---

# Eindeutige Rabattcodes über Shopify versenden {#send-unique-discount-codes-through-shopify}

> Dieser von der Community eingereichte Anwendungsfall zeigt, wie Sie Braze-[Aktionscodes]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes) mit dem Shopify Bulk Discount Code Bot verwenden können, um eindeutige Rabattcodes für Ihre Campaigns und Canvases zu generieren. Eindeutige Rabattcodes helfen dabei, die Ausnutzung von generischen Aktionscodes zu vermeiden.

{% alert important %}
Dies ist eine von der Community eingereichte Integration, die nicht direkt von Braze unterstützt wird. Der Bulk Discount Code Bot wird direkt von Shopify unterstützt. Nur Braze-Aktionscodes werden von Braze unterstützt.
{% endalert %}

## Anforderungen {#requirements}

| Anforderung | Beschreibung |
| --- | --- |
| Einen Shopify-Shop einrichten | Bestätigen Sie, dass Sie bereits [einen Shopify-Shop mit Braze eingerichtet]({{site.baseurl}}/shopify_overview) haben. |
| Die App Bulk Discount Code Bot installieren | Laden Sie die App [Bulk Discount Code Bot](https://apps.shopify.com/bulk-discount-generator) im Shopify App Store herunter. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anforderungen" }

## Eindeutige Rabattcodes generieren {#generating-unique-discount-codes}

### Schritt 1: Konfigurieren Sie Ihre Rabattcodes {#step-1-configure-your-discount-codes}

Verwenden Sie den Bulk Discount Code Bot, um Ihre Rabattcodes nach der Anzahl der zu generierenden Codes, der Codelänge, dem Rabattwert und vielem mehr zu konfigurieren.

![Die Konfigurationsoptionen für ein Rabattset.][1]

### Schritt 2: Exportieren Sie Ihre Codes {#step-2-export-your-codes}

Suchen Sie Ihr Rabattset in der Suchleiste des Bulk Discount Code Bot und wählen Sie dann **Export Codes** > **Download Codes**, um eine CSV-Datei in Ihren Download-Ordner herunterzuladen.

![Suchleiste mit einem Dropdown, das das Rabattset anzeigt, und einer Reihe von Buttons zur Auswahl.][2]{: style="max-width:70%;"}

Löschen Sie in der CSV-Datei Zeile 1, um die Spaltenüberschrift „Promo“ zu entfernen. Dadurch wird verhindert, dass „Promo“ in Braze zu einem Rabattcode wird.

![Ein Flussdiagramm, das die Entfernung der Zeilenüberschrift „Promo“ in einer CSV-Datei zeigt.][3]{: style="max-width:60%;"}

### Schritt 3: Fügen Sie Ihre Rabattcodes zu Braze hinzu {#step-3-add-your-discount-codes-to-braze}

Gehen Sie in Braze zu **Dateneinstellungen** > **Aktionscodes** > **Aktionscodeliste erstellen** und [konfigurieren Sie Ihre Rabattcodeliste]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create#create). Stellen Sie sicher, dass das Ablaufdatum mit dem übereinstimmt, das im Bulk Discount Code Bot konfiguriert wurde.

Laden Sie dann Ihre CSV-Datei hoch und wählen Sie **Save List**.

### Schritt 4: Fügen Sie Ihre Rabattcodes zu einer Braze-Campaign oder einem Canvas-Schritt hinzu {#step-4-add-your-discount-codes-to-a-braze-campaign-or-canvas-step}

Wenn Sie Ihre eindeutigen Rabattcodes in einer einzelnen Campaign verwenden möchten oder es Ihnen nichts ausmacht, dass Nutzer:innen mehrere eindeutige Codes über verschiedene Campaigns oder Canvas-Schritte erhalten, kopieren Sie das Liquid-Snippet des Codes aus der Aktionscodeliste, die Sie gespeichert haben.

![Ein Liquid-Code-Snippet mit einem Button zum Kopieren.][4]{: style="max-width:60%;"}

Fügen Sie das Liquid-Snippet in eine Campaign oder einen Canvas-Schritt ein.

![Ein GIF, das zeigt, wie das Liquid-Snippet zu einem Canvas-Schritt hinzugefügt wird.][5]

Wenn Sie möchten, dass Nutzer:innen einen einzigen eindeutigen Rabattcode erhalten, unabhängig davon, wie oft der Rabattcode in Campaigns oder Canvases referenziert wird, erstellen Sie einen [Nutzeraktualisierung]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)-Schritt direkt vor dem ersten Nachrichtenschritt, der den Rabattcode einem angepassten Attribut wie „Promo Code“ zuweist.

{% alert tip %}
Sie können auch [ein angepasstes Attribut erstellen]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), indem Sie zu **Dateneinstellungen** > **Angepasste Attribute** gehen.
{% endalert %}

Führen Sie im Nutzeraktualisierung-Schritt für jedes Feld Folgendes aus:
- **Attribute Name:** Wählen Sie **Promo Code** aus.
- **Action:** Wählen Sie **Update** aus.
- **Key Value:** Fügen Sie das Liquid-Code-Snippet ein.

![Ein Nutzeraktualisierung-Schritt, der ein „Promo Code“-Attribut mit dem Liquid-Snippet aktualisiert.][6]

Jetzt können Sie das angepasste Attribut {% raw %}`{{custom_attribute.${Promo Code}}}`{% endraw %} zu jeder Nachricht hinzufügen, und der Rabattcode wird als Template eingefügt.

## Verhalten von Rabattcodes {#discount-code-behavior}

{% details Multichannel-Campaign oder Canvas-Schritt %}

Wenn ein Rabattcode-Snippet in einer Multichannel-Campaign oder einem Canvas-Schritt verwendet wird, erhalten Nutzer:innen immer einen eindeutigen Code. Wenn Nutzer:innen über mehr als einen Kanal einen Code erhalten können, erhalten sie über jeden Kanal denselben Code. Mit anderen Worten: Berechtigte Nutzer:innen erhalten nur einen Code für alle Nachrichten, die von dieser Campaign oder diesem Canvas-Schritt gesendet werden.

{% enddetails %}

{% details Verschiedene Canvas-Schritte oder separate Campaigns %}

Wenn ein Rabattcode in mehreren Schritten desselben Canvas oder in separaten Campaigns referenziert wird, erhalten berechtigte Nutzer:innen mehrere eindeutige Aktionscodes (einen Code pro Canvas-Schritt oder Campaign).

{% enddetails %}

[1]: {% image_buster /assets/img/shopify/configure_discount_codes.png %}
[2]: {% image_buster /assets/img/shopify/export_discount_codes.png %}
[3]: {% image_buster /assets/img/shopify/edited_codes_csv.png %}
[4]: {% image_buster /assets/img/shopify/liquid_code_snippet.png %}
[5]: {% image_buster /assets/img/shopify/liquid_promo_code.gif %}
[6]: {% image_buster /assets/img/shopify/user_update_step.png %}