---
nav_title: Katalogartikel mit einem Attribut-Array abgleichen
article_title: Katalogartikel mit einem angepassten Attribut-Array abgleichen
page_order: 2
page_type: reference
description: "Verwenden Sie eine Katalogauswahl und Liquid, um Katalogzeilen anzuzeigen, deren Namen oder IDs in einem angepassten Attribut-Array vorkommen, z. B. einer Wunschliste."
---

# Katalogartikel mit einem angepassten Attribut-Array abgleichen {#match-catalog-items-to-a-custom-attribute-array}

> Wenn Nutzer:innen eine Liste gespeicherter Produktnamen in ihrem Profil führen, können Sie eine Katalogauswahl zusammen mit Liquid verwenden, um nur die Katalogzeilen anzuzeigen, die in dieser Liste vorkommen – zum Beispiel in einer Wunschlisten-E-Mail.

## Über dieses Beispiel {#about-this-example}

Flash und Thread speichert die gespeicherten Produktnamen jeder Kund:in in einem angepassten Attribut vom Typ String-Array (`saved_product_names`). Der Katalog enthält vollständige Produktdetails (Kategorie, Preis, Bild-URL, Bestand).

Katalogauswahlen können Katalogspalten anhand statischer oder Liquid-Werte filtern, einschließlich Array-Feldern in Katalogzeilen. Sie filtern jedoch keine Katalogzeile anhand von Werten, die in einem Kundenprofil or Nutzerprofil-Array gespeichert sind. Um Inhalte anhand der Liste der Nutzer:innen zu personalisieren, geben Sie mit einer Auswahl eine breite Menge von Katalogartikeln zurück und verwenden dann Liquid, um nur die Zeilen beizubehalten, die mit dem Profil-Array übereinstimmen.

Dieses Muster:

1. Weist das Array-basierte angepasste Attribut der Nutzer:innen einer Liquid-Variablen zu.
2. Ruft `catalog_selection_items` für eine vorgefilterte Katalogauswahl auf (bis zu 50 Artikel).
3. Iteriert über `items` und verwendet `contains`, um jedes Katalogfeld (z. B. `name` oder `id`) mit dem Array abzugleichen.

{% alert important %}
Dieses Muster funktioniert nur, wenn die Ergebnismenge der Auswahl (bis zu 50 Katalogzeilen) die gespeicherten Artikel der jeweiligen Nutzer:innen plausibel enthalten kann – zum Beispiel bei kleinen Katalogen oder wenn Filter die Auswahl so weit eingrenzen, dass eine typische Liste abgedeckt wird. Wenn die gespeicherten Artikel von Nutzer:innen außerhalb der 50 zurückgegebenen Zeilen liegen, findet die Schleife keine Übereinstimmungen und die Nachricht rendert für diese Artikel nichts – kein Filter löst dieses Problem im allgemeinen Fall, da die Auswahl nicht gegen das Profil-Array der Nutzer:innen abgleichen kann.
{% endalert %}

## Hinweise {#considerations}

- Testen Sie Liquid und Katalogdaten in einem Staging-Workspace, bevor Sie an Kund:innen senden.
- Da eine Auswahl maximal 50 Katalogzeilen zurückgibt, fügen Sie Filter hinzu (z. B. auf Lager, aktive Kategorie oder Preisbereich), die die wahrscheinlich gespeicherten Artikel der jeweiligen Nutzer:innen innerhalb dieser Ergebnismenge halten.
- Dieses Beispiel verwendet ein String-Array im Kundenprofil or Nutzerprofil.
- Für ein Array von Objekten gleichen Sie anhand einer Eigenschaft innerhalb jedes Objekts ab (z. B. `product_id`) und passen die `contains`-Prüfung an oder verwenden eine `for`-Schleife über Objekte. Siehe [Array von Objekten]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects).
- Das Verhalten von `contains` hängt vom Attributtyp ab; für Arrays verwenden Sie `contains` statt `==`. Siehe [Bedingte Logik]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic).
- Gleichen Sie anhand stabiler Bezeichner ab (z. B. Katalog-`id`), wenn sich Produktnamen ändern oder doppelt vorkommen können.
- Die Liquid-Snippets in diesem Artikel sind Beispiele. Validieren Sie das Rendering in Ihren Kanälen (E-Mail-HTML, Push usw.).

## Einrichtung {#setup}

Dieses Beispiel setzt Folgendes voraus:

| Asset | Details |
| --- | --- |
| Angepasstes Attribut | `saved_product_names` – String-Array (z. B. `["linen_shirt", "trail_jacket", "canvas_tote"]`) |
| Katalog | `apparel_products` mit den Spalten `id`, `category`, `name`, `price`, `inventory`, `image_url` |
| Auswahl | `in_stock_apparel` auf `apparel_products`, Ergebnislimit 50, mit Filtern, die irrelevante Zeilen ausschließen (z. B. `inventory` größer als `0`) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Einrichtung" }

### Schritt 1: Katalog und Auswahl erstellen {#step-1-create-the-catalog-and-selection}

1. Importieren oder synchronisieren Sie Produktzeilen in einen Katalog namens `apparel_products`.
2. Erstellen Sie eine Auswahl (z. B. `in_stock_apparel`), die so viele relevante Zeilen wie nötig zurückgibt, bis zum Limit von 50 Artikeln.
3. Fügen Sie Auswahlfilter hinzu, um Zeilen auszuschließen, die Sie nie in der Nachricht haben möchten (nicht auf Lager, falsche Kategorie usw.).

Informationen zur Einrichtung von Auswahlen finden Sie unter [Auswahlen]({{site.baseurl}}/user_guide/data/activation/catalogs/selections).

### Schritt 2: Liquid in Ihre Nachricht einfügen {#step-2-add-liquid-in-your-message}

Weisen Sie das Profil-Array zu, laden Sie die Auswahl und iterieren Sie mit `contains`:

{% raw %}
```liquid
{% assign saved_product_names = custom_attribute.${saved_product_names} %}
{% catalog_selection_items apparel_products in_stock_apparel %}
{% for item in items %}
{% if saved_product_names contains item.name %}
Product: {{ item.name }}
Category: {{ item.category }}
Price: ${{ item.price }}
Image: {{ item.image_url }}
{% endif %}
{% endfor %}
```
{% endraw %}

Ersetzen Sie `item.name` durch `item.id` (oder eine andere Spalte), wenn Ihr Array IDs statt Anzeigenamen speichert. Fügen Sie Abstände oder HTML zwischen den Feldern für Ihren Kanal hinzu. In {% raw %}`${{ item.price }}`{% endraw %} ist das `$` ein literales Währungssymbol, das vor der Liquid-Ausgabe gedruckt wird – es ist kein Teil der {% raw %}`${}`{% endraw %}-Personalisierungssyntax von Braze.

Um dieses Liquid automatisch zu generieren, öffnen Sie das Modal **Personalisierung hinzufügen** (**Katalogartikel** > **Eine Auswahl verwenden**). Siehe [Kataloge verwenden]({{site.baseurl}}/user_guide/data/activation/catalogs/use).

### Schritt 3: Vorschau und Test {#step-3-preview-and-test}

Senden Sie Testnachrichten an Profile mit unterschiedlichen `saved_product_names`-Werten. Bestätigen Sie, dass nur übereinstimmende Katalogzeilen angezeigt werden und dass ein leeres Array keine Produktzeilen erzeugt.

## Verwandte Artikel {#related-articles}

- [Kataloge]({{site.baseurl}}/user_guide/data/activation/catalogs)
- [Auswahlen]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)
- [Kataloge verwenden]({{site.baseurl}}/user_guide/data/activation/catalogs/use)
- [Angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)
- [Bedingte Logik]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic)
- [Liquid-Anwendungsfallbibliothek – einen String in einem Array finden]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases#misc-string-in-array)