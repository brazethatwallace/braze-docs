---
nav_title: Kataloge
article_title: Kataloge
page_order: 3
layout: dev_guide

guide_top_header: "Kataloge"
guide_top_text: "Kataloge greifen auf Daten aus importierten CSV-Dateien und API-Endpunkten zu, um Ihre Nachrichten anzureichern – ähnlich wie Sie über Liquid auf angepasste Attribute oder Event-Eigenschaften zugreifen würden."

description: "Auf dieser Landing-Page finden Sie alles rund um Kataloge. Nutzen Sie Kataloge und gefilterte Sets, um Nicht-Nutzerdaten in Ihren Braze-Kampagnen einzusetzen und personalisierte Nachrichten zu versenden."

guide_featured_title: "Abschnitt-Artikel"
guide_featured_list:
- name: Katalog erstellen
  link: /docs/user_guide/data/activation/catalogs/create
  image: /assets/img/braze_icons/users-01.svg
- name: Verwendung von Katalogen
  link: /docs/user_guide/data/activation/catalogs/use
  image: /assets/img/braze_icons/users-01.svg
- name: „Wieder verfügbar“-Benachrichtigungen
  link: /docs/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: Preissenkungsbenachrichtigungen
  link: /docs/price_drop_notifications
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: Auswahlen
  link: /docs/user_guide/data/activation/catalogs/selections
  image: /assets/img/braze_icons/list.svg

guide_menu_title: "Weitere Artikel"
guide_menu_list:
- name: Katalog-API-Endpunkte
  link: /docs/api/endpoints/catalogs
  image: /assets/img/braze_icons/server-01.svg
- name: Drag-and-Drop-Produktblöcke
  link: /docs/dnd_product_blocks
  image: /assets/img/braze_icons/columns-01.svg
---
<br><br>

## Anwendungsfälle für Kataloge {#catalog-use-cases}

Sie können jede Art von Daten in einen Katalog einbringen. In der Regel handelt es sich dabei um Metadaten zu Angeboten wie Produkten, Rabatten, Aktionen, Events und Ähnlichem. In den folgenden Anwendungsfällen finden Sie einige Beispiele dafür, wie Sie diese Daten nutzen können, um Nutzer:innen mit hochrelevanten Nachrichten anzusprechen.

### Einzelhandel und E-Commerce {#retail-and-ecommerce}

- **Saisonale Aktionen:** Importieren Sie saisonale Produktkollektionen und personalisieren Sie Nachrichten, um aktuelle Trends widerzuspiegeln.
- **Lokalisierte Nachrichten:** Importieren Sie die Adressen, Öffnungszeiten und Dienste Ihrer Standorte und personalisieren Sie Benachrichtigungen basierend auf den Standorten der Nutzer:innen.
- **„Wieder verfügbar“-Benachrichtigungen:** Importieren Sie Produktinformationen einschließlich der Bestandsmenge und nutzen Sie dann [„Wieder verfügbar“-Benachrichtigungen]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications) sowie angepasste Braze-Events, um eine Campaign oder ein Canvas auszulösen, das Nutzer:innen darüber informiert, dass ein Produkt wieder auf Lager ist.
- **Preissenkungsbenachrichtigungen:** Importieren Sie Produktinformationen mit Produktpreisen und nutzen Sie dann [Preissenkungsbenachrichtigungen]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications) sowie angepasste Braze-Events, um ein Canvas auszulösen, das Nutzer:innen über die Preissenkung eines Produkts informiert.

### Unterhaltung {#entertainment}

- **Abo-Pläne:** Importieren Sie Abo-Pläne und bewerben Sie Add-Ons bei Ihren Nutzer:innen basierend auf deren Nutzungsverhalten und den Inhaltstypen, die sie am häufigsten konsumieren.
- **Bevorstehende Events:** Importieren Sie Listen bevorstehender Events mit Veranstaltungsorten und Altersgruppen und senden Sie personalisierte Benachrichtigungen an Nutzer:innen, die sich in der Nähe befinden und zur Zielgruppe gehören.
- **Medienpräferenzen:** Importieren Sie Informationen über Filme und Serien und empfehlen Sie Ihren Nutzer:innen Inhalte basierend auf ihren Lieblingstiteln und meistgesehenen Genres.

### Reisen und Gastgewerbe {#travel-and-hospitality}

- **Ziele:** Importieren Sie Reiseziele mit den beliebtesten Attraktionen, Restaurants und Aktivitäten und personalisieren Sie Empfehlungen für Ihre Nutzer:innen basierend auf deren früheren Reisen.
- **Unterkünfte:** Importieren Sie Hotels mit Ausstattung, Zimmertypen und Preisen und senden Sie Aktionsangebote an Ihre Nutzer:innen basierend auf deren ausgewählten Präferenzen.
- **Reisearten:** Importieren Sie Angebote und Aktionen für verschiedene Reisearten (z. B. Flüge, Züge, Mietwagen und andere) und senden Sie diese an Ihre Nutzer:innen basierend auf deren aktuellem Suchverlauf.
- **Essenspräferenzen:** Importieren Sie Informationen über das Essensangebot und nutzen Sie [Auswahlen]({{site.baseurl}}/user_guide/data/activation/catalogs/selections), um personalisierte Nachrichten an Nutzer:innen zu senden, die bestimmte Essenspräferenzen haben – basierend auf der zuletzt angesehenen Essenskategorie.

## Wie Kataloge und Liquid zusammenarbeiten {#how-catalogs-and-liquid-work-together}

Kataloge sind ein Feature zur Datenspeicherung. Sie enthalten große Datenmengen, auf die Sie in Ihren Nachrichten zur Personalisierung verweisen können. Um die Daten tatsächlich zu referenzieren, verwenden Sie [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) als Templating-Sprache. Anders gesagt: Kataloge sind der Speicher, in dem die Daten vorgehalten werden, und Liquid ist die Sprache, die die relevanten Daten aus dem Speicher abruft.

Beispiele dafür, wie Sie Liquid zum Abrufen von Kataloginformationen verwenden können, finden Sie in den zusätzlichen Anwendungsfällen unter [Katalog erstellen]({{site.baseurl}}/user_guide/data/activation/catalogs/create#additional-use-cases).

## Einschränkungen beim Datenspeicher {#data-storage-limitations}

Der Datenspeicher für Kataloge ist durch die Größe der Katalogartikel begrenzt, die sich von der Größe der hochgeladenen CSV-Dateien unterscheiden kann.

Bei der kostenlosen Version der Kataloge sind bis zu 100&nbsp;MB Speicherplatz zulässig. Sie können unbegrenzt viele Artikel anlegen, solange der Speicherplatz 100&nbsp;MB nicht überschreitet.

Für Catalogs Pro stehen folgende Speichergrößen zur Verfügung: 5&nbsp;GB, 10&nbsp;GB, 15&nbsp;GB oder 50&nbsp;GB. Beachten Sie, dass der Speicherplatz der kostenlosen Version (100&nbsp;MB) in jedem dieser Tarife enthalten ist.

Wenn Sie Ihren Katalogspeicher upgraden möchten, kontaktieren Sie Ihren Braze Account Manager. Einzelheiten zu den Tarifen und Berechtigungshinweise finden Sie unter [Katalogspeicher]({{site.baseurl}}/user_guide/data/activation/catalogs/create#tiers).