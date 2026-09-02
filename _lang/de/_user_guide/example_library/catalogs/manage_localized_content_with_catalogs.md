---
nav_title: Lokalisierte Kataloginhalte
article_title: Lokalisierte Inhalte mit Braze-Katalogen verwalten
page_order: 3
page_type: reference
description: "Speichern Sie lokalisierte Produkttexte, Preise und Bild-URLs in Braze-Katalogen und lösen Sie die richtige Sprache zum Sendezeitpunkt auf."
---

# Lokalisierte Inhalte mit Braze-Katalogen verwalten {#manage-localized-content-with-braze-catalogs}

> Speichern Sie lokalisierte Strings und URLs in Katalogen, damit jede:r Nutzer:in Texte in der eigenen Sprache aus einer einzelnen Campaign oder einem Canvas erhält – ohne separate Varianten pro Sprache.

## Über dieses Beispiel {#about-this-example}

PantsLabyrinth, ein fiktiver Bekleidungshändler, verkauft seine Produkte in Nordamerika und Europa. Produktnamen, Preise und Hero-Bilder unterscheiden sich je nach Sprache, doch das Marketing-Team möchte ein einziges E-Mail- oder Push-Template, das zum Sendezeitpunkt personalisiert wird.

Dieses Beispiel behandelt drei Katalog-Patterns, die das {% raw %}`${language}`{% endraw %} [Standardattribut]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) der Nutzer:innen auslesen (vom SDK or Software-Development-Kit über das Geräte-Locale erfasst):

- JSON-Objektfelder: alle Sprachen in einer Zeile pro Artikel
- Flache sprachspezifische Spalten: `header_en`, `header_fr` usw.
- Separater Katalog pro Sprache: dynamischer Katalogname wie `pantslabyrinth-promo-en`

Verwenden Sie Kataloge, wenn lokalisierte Inhalte strukturierte Daten sind (Produkte, Aktionen, Bild-URLs). Für freien Nachrichtentext in E-Mail oder Push verwenden Sie bevorzugt [mehrsprachige Nachrichten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages), wenn Ihre Kanäle diese unterstützen. Einen breiteren Vergleich der Lokalisierungs-Patterns finden Sie unter [Übersetzungsmanagement]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#translation-management).

## Hinweise {#considerations}

- Die Beispiele dienen der Veranschaulichung. Überprüfen Sie die Groß-/Kleinschreibung und das Format von {% raw %}`${language}`{% endraw %} in Ihrer Nutzerbasis, bevor Sie Katalogschlüssel oder -suffixe benennen.
- Bei Methode 1 und 2 kann die lokalisierte Ausgabe leer sein, wenn {% raw %}`${language}`{% endraw %} leer ist oder keinem Katalogschlüssel oder -feld entspricht – prüfen Sie jedes Feld einzeln und verwenden Sie einen Fallback zu einem Standard (z. B. Englisch).
- Bei Methode 3 müssen Sie unterstützte Sprachcodes auf eine Allowlist setzen, bevor Sie den Katalognamen erstellen; ein fehlender Katalog bricht die Nachricht ab.
- [JSON-Objekte]({{site.baseurl}}/user_guide/data/activation/catalogs/create#supported-data-types) in Katalogen können über die API oder [Cloud Data Ingestion (CDI) für Kataloge]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data) erstellt oder aktualisiert werden, nicht per CSV-Upload.
- Methode 2 unterstützt CSV-Pflege, vervielfacht aber die Spalten mit jeder neuen Sprache. CSV-Dateien unterstützen bis zu [1.000 Spalten]({{site.baseurl}}/user_guide/data/activation/catalogs/create#step-1-review-your-csv-file).
- Methode 3 erfordert einen Katalog für jeden Sprachcode, der das `catalog_items`-Tag erreicht. Existiert der Katalog nicht, bricht Braze die Nachricht ab. Eine fehlende Artikel-ID in einem vorhandenen Katalog gibt ein leeres Items-Array zurück.
- Katalog-Liquid-Tags können nicht [rekursiv]({{site.baseurl}}/user_guide/data/activation/catalogs/use#using-liquid) verwendet werden.
- [Katalogselektionen]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) unterstützen bis zu 10 Filter und geben bis zu 50 Artikel zurück – validieren Sie Filter gegen Ihr Katalogschema.
- Prüfen Sie die [Katalog-Speicherstufen]({{site.baseurl}}/user_guide/data/activation/catalogs/create#tiers), wenn Sie große mehrsprachige Produkt-Feeds pflegen.

## Einrichtung {#setup}

### Schritt 1: Katalogstruktur wählen {#step-1-choose-a-catalog-structure}

Wählen Sie eine Katalogstruktur anhand der Hinweise in dieser Tabelle.

| Methode | Am besten geeignet, wenn | Kompromiss |
| --- | --- | --- |
| JSON-Objektfelder | Mittlere Kataloggröße; eine Zeile pro Artikel; Aktualisierungen über API oder CDI | Das Hinzufügen einer Sprache aktualisiert jeden Artikel über die API; kein CSV für JSON-Felder |
| Flache sprachspezifische Felder | Wenige Sprachen und Felder; nicht-technische Teams nutzen CSV | Jede neue Sprache fügt Spalten hinzu; Feldnamen müssen konsistent bleiben |
| Katalog pro Sprache | Große länderspezifische Feeds oder separate Verantwortliche pro Sprache; CSV pro Sprache | Jeder auf der Allowlist stehende Sprachcode benötigt einen Katalog; fehlende Kataloge brechen den Versand ab |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Katalogstruktur wählen" }

### Schritt 2: Katalog und Artikel erstellen {#step-2-create-the-catalog-and-items}

1. Gehen Sie zu **Dateneinstellungen** > **Kataloge** und erstellen Sie einen Katalog (oder mehrere Kataloge für Methode 3).
2. Fügen Sie Felder und Artikel basierend auf Ihrer gewählten Struktur hinzu. Siehe [Katalog erstellen]({{site.baseurl}}/user_guide/data/activation/catalogs/create).
3. (Optional) Erstellen Sie eine [Katalogselektion]({{site.baseurl}}/user_guide/data/activation/catalogs/selections), um Artikel zu filtern – z. B. nach `category`, die einem angepassten Attribut der Nutzer:innen entspricht.

{% tabs local %}
{% tab Methode 1: JSON-Felder %}
Beispielartikel im Katalog `PantsLabyrinth_Product_Copy`:

| Artikel | Wert |
| --- | --- |
| `id` | `trail-runner-001` |
| `name` | `{"EN":"Trail Runner","FR":"Chaussure de trail","DE":"Trailrunner"}` |
| `category` | `footwear` |
| `url` | `https://pantslabyrinth.shop/products/trail-runner-001` |
| `price` | `{"EN":"$120 USD","FR":"112 EUR","DE":"112 EUR"}` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Beispiel-Katalogartikel mit JSON-Sprachfeldern" }

{% endtab %}
{% tab Methode 2: Flache Felder %}
Beispielartikel im Katalog `PantsLabyrinth_Promo_Copy`:

| Artikel | Wert |
| --- | --- |
| `id` | `spring-sale` |
| `header_en` | `Spring trail sale` |
| `header_fr` | `Soldes de printemps` |
| `body_en` | `Save on trail runners this week.` |
| `body_fr` | `Économisez sur les chaussures de trail cette semaine.` |
| `cta_text_en` | `Shop now` |
| `cta_text_fr` | `Acheter` |
| `img_src_en` | `https://cdn.pantslabyrinth.shop/en/spring.jpg` |
| `img_src_fr` | `https://cdn.pantslabyrinth.shop/fr/spring.jpg` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Beispiel-Katalogartikel mit flachen sprachspezifischen Feldern" }

{% endtab %}
{% tab Methode 3: Katalog pro Sprache %}
Erstellen Sie einen Katalog pro Sprache mit denselben Feldern. Wiederholen Sie z. B. dieselbe `id` und dieselben Felder in `pantslabyrinth-promo-fr` und `pantslabyrinth-promo-de` mit lokalisierten Werten.

Beispielartikel in `pantslabyrinth-promo-en`:

| Artikel | Wert |
| --- | --- |
| `id` | `spring-sale` |
| `header` | `Spring trail sale` |
| `body` | `Save on trail runners this week.` |
| `cta_text` | `Shop now` |
| `img_src` | `https://cdn.pantslabyrinth.shop/en/spring.jpg` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Beispielartikel in einem englischsprachigen Katalog pro Sprache" }

{% endtab %}
{% endtabs %}

### Schritt 3: Liquid zu Ihrer Nachricht hinzufügen {#step-3-add-liquid-to-your-message}

Wählen Sie das Liquid-Pattern, das zur Katalogstruktur passt, die Sie in Schritt 1 gewählt haben.

{% tabs local %}
{% tab Methode 1: JSON-Felder %}
Speichern Sie alle Sprachen in JSON-Objektfeldern in einer einzelnen Katalogzeile und verwenden Sie den `property_accessor`-Filter, um die `name`- und `price`-Schlüssel auszulesen, die zu {% raw %}`${language}`{% endraw %} passen (auf Großbuchstaben normalisiert). Prüfen Sie jedes Feld einzeln und verwenden Sie `EN` als Fallback, wenn das Feld leer ist, sodass eine Sprache mit einem Namen, aber ohne Preis dennoch einen englischen Preis erhält.

{% raw %}
```liquid
{% catalog_items PantsLabyrinth_Product_Copy trail-runner-001 %}
{% assign lang = ${language} | upcase %}
{% assign localized_name = items[0].name | property_accessor: lang %}
{% assign localized_price = items[0].price | property_accessor: lang %}
{% if localized_name == blank %}
  {% assign localized_name = items[0].name | property_accessor: 'EN' %}
{% endif %}
{% if localized_price == blank %}
  {% assign localized_price = items[0].price | property_accessor: 'EN' %}
{% endif %}
Product: {{ localized_name }}
Price: {{ localized_price }}
```
{% endraw %}

Siehe [Property-Accessor-Filter]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters#property-accessor-filter).
{% endtab %}
{% tab Methode 2: Flache Felder %}
Erstellen Sie dynamische Feldnamen aus {% raw %}`${language}`{% endraw %} (auf Kleinbuchstaben normalisiert) und lesen Sie diese Felder mit Bracket-Lookup aus dem Artikel aus. Zum Beispiel liest {% raw %}`items[0][header_field]`{% endraw %} die Überschrift für die aufgelöste Sprache. Prüfen Sie jedes Feld einzeln und verwenden Sie die englische Spalte als Fallback, wenn das Feld leer ist, sodass eine Sprache mit einer Überschrift, aber ohne Text dennoch englischen Text erhält.

{% raw %}
```liquid
{% catalog_items PantsLabyrinth_Promo_Copy spring-sale %}
{% assign lang = ${language} | downcase %}
{% assign header_field = 'header_' | append: lang %}
{% assign body_field = 'body_' | append: lang %}
{% assign cta_field = 'cta_text_' | append: lang %}
{% assign img_field = 'img_src_' | append: lang %}
{% assign header_val = items[0][header_field] %}
{% assign body_val = items[0][body_field] %}
{% assign cta_val = items[0][cta_field] %}
{% assign img_val = items[0][img_field] %}
{% if header_val == blank %}
  {% assign header_val = items[0].header_en %}
{% endif %}
{% if body_val == blank %}
  {% assign body_val = items[0].body_en %}
{% endif %}
{% if cta_val == blank %}
  {% assign cta_val = items[0].cta_text_en %}
{% endif %}
{% if img_val == blank %}
  {% assign img_val = items[0].img_src_en %}
{% endif %}
<img src="{{ img_val }}" alt="" />
<h2>{{ header_val }}</h2>
<p>{{ body_val }}</p>
<a href="#">{{ cta_val }}</a>
```
{% endraw %}
{% endtab %}
{% tab Methode 3: Katalog pro Sprache %}
{% alert warning %}
Wenn der Katalogname, den Sie an `catalog_items` übergeben, nicht existiert, bricht Braze die Nachricht ab. Setzen Sie unterstützte Sprachcodes auf eine Allowlist, bevor Sie den Katalognamen erstellen. Eine fehlende Artikel-ID in einem vorhandenen Katalog gibt ein leeres Items-Array zurück – Sie können in diesem Fall auf den englischen Katalog zurückfallen.
{% endalert %}

Setzen Sie die Sprachcodes, die passende Kataloge haben, auf eine Allowlist (hier `en`, `fr` und `de`), verwenden Sie für nicht unterstützte oder leere Werte `en` als Standard und suchen Sie dann den Artikel. Fehlt die Artikel-ID in diesem Katalog, fällt das System auf den englischen Katalog zurück.

{% raw %}
```liquid
{% assign lang = ${language} | downcase %}
{% assign supported = 'en,fr,de' | split: ',' %}
{% if supported contains lang %}{% else %}{% assign lang = 'en' %}{% endif %}
{% assign theCatalog = 'pantslabyrinth-promo-' | append: lang %}
{% catalog_items {{ theCatalog }} spring-sale %}
{% if items[0] == blank %}
  {% catalog_items pantslabyrinth-promo-en spring-sale %}
{% endif %}
<img src="{{ items[0].img_src }}" alt="" />
<h2>{{ items[0].header }}</h2>
<p>{{ items[0].body }}</p>
<a href="#">{{ items[0].cta_text }}</a>
```
{% endraw %}

Siehe [Templates in Katalognamen verwenden]({{site.baseurl}}/user_guide/data/activation/catalogs/create#template-catalog-names) und [Nachrichten abbrechen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages).
{% endtab %}
{% endtabs %}

#### Optionale Katalogselektion nach Kategorie {#optional-catalog-selection-by-category}

Filtern Sie Artikel vor der Personalisierung – z. B. Schuh-Aktionen für Nutzer:innen mit `preferred_category = footwear`:

{% raw %}
```liquid
{% catalog_selection_items PantsLabyrinth_Product_Copy footwear_promos %}
{% for item in items %}
  {{ item.name }}
{% endfor %}
```
{% endraw %}

Definieren Sie die Selektion im Dashboard mit Filtern auf Ihrer `category`-Spalte und Nutzerattributen nach Bedarf.

### Schritt 4: Vorschau und Test {#step-4-preview-and-test}

1. Verwenden Sie **Als Nutzer:in Vorschau anzeigen** mit Nutzerprofilen, die verschiedene {% raw %}`${language}`{% endraw %}-Werte haben.
2. Bestätigen Sie den Fallback-Text, wenn die Sprache fehlt oder nicht unterstützt wird, einschließlich teilweiser Lokalisierungen (z. B. ein Name ohne Preis).
3. Bestätigen Sie bei Methode 3, dass jede auf der Allowlist stehende Sprache einen passenden Katalog hat und dass nicht unterstützte Sprachcodes auf Ihren Standardkatalog abgebildet werden, ohne den Versand abzubrechen.

## Verwandte Artikel {#related-articles}

- [Kataloge]({{site.baseurl}}/user_guide/data/activation/catalogs)
- [Kataloge verwenden]({{site.baseurl}}/user_guide/data/activation/catalogs/use)
- [Selektionen]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)
- [Katalog erstellen]({{site.baseurl}}/user_guide/data/activation/catalogs/create)
- [Erweiterte Liquid-Filter]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters#property-accessor-filter)
- [Lokalisierung]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization)
- [Mehrsprachige Nachrichten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)
- [Katalogdaten synchronisieren und löschen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)
- [Liquid-Nachrichten abbrechen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages)