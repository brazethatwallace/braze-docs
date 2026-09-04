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
| Shopify-Shop einrichten | Bestätigen Sie, dass Sie bereits einen [Shopify-Shop mit Braze eingerichtet]({{site.baseurl}}/shopify_overview) haben. |
| Die App „Bulk Discount Code Bot“ installieren | Laden Sie die App [Bulk Discount Code Bot](https://apps.shopify.com/bulk-discount-generator) im Shopify App Store herunter. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anforderungen" }

## Eindeutige Rabattcodes generieren {#generating-unique-discount-codes}

### Schritt 1: Rabattcodes konfigurieren {#step-1-configure-your-discount-codes}

Verwenden Sie den Bulk Discount Code Bot, um Ihre Rabattcodes basierend auf der Anzahl der zu generierenden Codes, der Code-Länge, dem Rabattwert und mehr zu konfigurieren.

![Die Konfigurationsoptionen für ein Rabattcode-Set.][1]{: width="1203" height="677" style="max-width:100%;"}

### Schritt 2: Codes exportieren {#step-2-export-your-codes}

Suchen Sie Ihr Rabattcode-Set in der Suchleiste des Bulk Discount Code Bots und wählen Sie dann **Export Codes** > **Download Codes** aus, um eine CSV-Datei in Ihren Downloads-Ordner herunterzuladen.

![Suchleiste mit einem Dropdown, das das Rabattcode-Set und eine Reihe von Buttons zur Auswahl anzeigt.][2]{: width="1163" height="858" style="max-width:70%;"}

Löschen Sie in der CSV-Datei Zeile 1, um die Spaltenüberschrift „Promo“ zu entfernen. Dies verhindert, dass „Promo“ in Braze als Aktionscode übernommen wird.

![Ein Flussdiagramm, das die Entfernung der Zeilenüberschrift „Promo“ in einer CSV-Datei zeigt.][3]{: width="448" height="222" style="max-width:60%;"}

### Schritt 3: Rabattcodes zu Braze hinzufügen {#step-3-add-your-discount-codes-to-braze}

Gehen Sie in Braze zu **Data Settings** > **Promotion Codes** > **Create Promotion Code List** und [konfigurieren Sie Ihre Aktionscode-Liste]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create#create). Stellen Sie sicher, dass das Ablaufdatum mit dem übereinstimmt, das im Bulk Discount Code Bot konfiguriert wurde.

Laden Sie dann Ihre CSV-Datei hoch und wählen Sie **Save List** aus.

### Schritt 4: Rabattcodes zu einer Braze-Campaign oder einem Canvas-Schritt hinzufügen {#step-4-add-your-discount-codes-to-a-braze-campaign-or-canvas-step}

Wenn Sie Ihre eindeutigen Rabattcodes in einer Einzelversand-Campaign verwenden möchten oder es Ihnen nichts ausmacht, dass Nutzer:innen mehrere eindeutige Codes über verschiedene Campaigns oder Canvas-Schritte erhalten, kopieren Sie das Liquid-Snippet des Codes aus der gespeicherten Aktionscode-Liste.

![Ein Liquid-Code-Snippet mit einem Button zum Kopieren.][4]{: width="958" height="295" style="max-width:60%;"}

Fügen Sie das Liquid-Snippet in eine Campaign oder einen Canvas-Schritt ein.

<video autoplay muted loop playsinline loading="lazy" width="800" height="540" style="max-width:100%;height:auto;aspect-ratio:800/540;" aria-label="Ein Video, das zeigt, wie das Liquid-Snippet zu einem Canvas-Schritt hinzugefügt wird.">
  <source src="{% image_buster /assets/img/shopify/liquid_promo_code.mp4 %}" type="video/mp4">
</video>

Wenn Nutzer:innen einen einzigen eindeutigen Rabattcode erhalten sollen, unabhängig davon, wie oft der Rabattcode in Campaigns oder Canvases referenziert wird, erstellen Sie einen [User Update]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)-Schritt direkt vor dem ersten Nachrichtenschritt, der den Rabattcode einem angepassten Attribut zuweist, z. B. „Promo Code“.

{% alert tip %}
Sie können auch [ein angepasstes Attribut erstellen]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), indem Sie zu **Data Settings** > **angepasste Attribute** gehen.
{% endalert %}

Führen Sie im User-Update-Schritt für jedes Feld Folgendes aus:
- **Attribute Name:** Wählen Sie **Promo Code** aus.
- **Action:** Wählen Sie **Update** aus.
- **Key Value:** Fügen Sie das Liquid-Code-Snippet ein.

![Ein User-Update-Schritt, der ein „Promo Code“-Attribut mit dem Liquid-Snippet aktualisiert.][6]{: width="2464" height="1322" style="max-width:100%;"}

Jetzt können Sie das angepasste Attribut {% raw %}`{{custom_attribute.${Promo Code}}}`{% endraw %} zu jeder Nachricht hinzufügen, und der Rabattcode wird automatisch eingefügt.

## Verhalten von Rabattcodes {#discount-code-behavior}

{% details Mehrkanalige Campaign oder Canvas-Schritt %}

Wenn ein Rabattcode-Snippet in einer mehrkanaligen Campaign oder einem Canvas-Schritt verwendet wird, erhalten Nutzer:innen immer einen eindeutigen Code. Wenn Nutzer:innen berechtigt sind, einen Code über mehr als einen Kanal zu erhalten, erhalten sie über jeden Kanal denselben Code. Mit anderen Worten: Berechtigte Nutzer:innen erhalten nur einen Code über alle Nachrichten hinweg, die von dieser Campaign oder diesem Canvas-Schritt gesendet werden.

{% enddetails %}

{% details Verschiedene Canvas-Schritte oder separate Campaigns %}

Wenn ein Rabattcode von mehreren Schritten im selben Canvas oder von separaten Campaigns referenziert wird, erhalten berechtigte Nutzer:innen mehrere eindeutige Aktionscodes (einen Code für jeden Canvas-Schritt oder jede Campaign).

{% enddetails %}

[1]: {% image_buster /assets/img/shopify/configure_discount_codes.png %}
[2]: {% image_buster /assets/img/shopify/export_discount_codes.png %}
[3]: {% image_buster /assets/img/shopify/edited_codes_csv.png %}
[4]: {% image_buster /assets/img/shopify/liquid_code_snippet.png %}
[6]: {% image_buster /assets/img/shopify/user_update_step.png %}