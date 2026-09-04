---
nav_title: Shopify Markets
article_title: Shopify Markets
description: "Dieser Referenzartikel beschreibt, wie Sie die Shopify Markets-Integration mit Braze einrichten und verwenden."
page_type: partner
search_tag: Partner
permalink: "/shopify_markets/"
hidden: true
---

# Shopify Markets

> Dieser Artikel behandelt die Shopify Markets-Integration (derzeit in der Beta-Phase), einschließlich des Umfangs, der Funktionsweise und der Nutzung Ihrer Markets-Daten in Ihrem Messaging. Braze veröffentlicht im Laufe der Beta-Phase schrittweise zusätzliche Markets-Funktionalitäten und skaliert die Unterstützung für komplexere Marktstrukturen im Laufe der Zeit.

{% alert important %}
Shopify Markets befindet sich derzeit in der Beta-Phase. Für weitere Informationen wenden Sie sich an Ihren Braze CSM.
{% endalert %}

## Funktionsweise der Integration {#how-the-integration-works}

Shopify Markets erweitert Ihre bestehende Shopify-Integration. Verbinden Sie Ihren Standard-Storefront über den [Standard-]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration) oder [angepassten (SDK)]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration) Integrationspfad und wählen Sie dann die Märkte aus, die Braze aus den konfigurierten Märkten Ihres Shops synchronisieren soll. Bestehende Integrationen können Märkte hinzufügen, ohne Kataloge, Abo-Gruppen oder Events zu beeinträchtigen. Eine Schritt-für-Schritt-Anleitung finden Sie unter [Shopify Markets einrichten](#shopify-markets-setup).

Shopify Markets bietet folgende Funktionen:

- **Marktbezogene Profile.** Die Integration erfasst die Shopify-Locale jedes Nutzers bzw. jeder Nutzerin zusammen mit den Standard-Attributen für Land und Sprache von Braze, sodass Sie ohne angepasste Einrichtung nach Markt segmentieren und triggern können.
- **Lokalisierte Kataloge.** Marktspezifische Produktdaten werden täglich synchronisiert: Preise, Währung und Verfügbarkeit pro Markt sowie übersetzte Titel, Beschreibungen und Produkt-URLs.
- **Marktbezogene Personalisierung.** Verwenden Sie den {% raw %}`{% shopify_market %}`{% endraw %} Liquid-Tag, um mit Katalogprodukten aus dem jeweiligen Markt der Nutzer:innen zu personalisieren, einschließlich der übersetzten Inhalte von Shopify. Sie können auch Marktdetails wie die Anzeigewährung aus unterstützten Shopify-Events wie `ecommerce.order_placed` referenzieren.
- **Fallback auf den Standard-Shop.** Wenn Nutzer:innen keinem Ihrer verbundenen Märkte angehören, verwendet Braze die Einstellungen und Produkte Ihres Standard-Shops, sodass alle Nutzer:innen eine vollständige, korrekte Nachricht erhalten.

Beispiele finden Sie unter [Markets-Nutzerdaten verwenden](#use-markets-user-data) und [Marktbezogener Katalog-Anwendungsfall](#tutorial-show-products-and-prices-per-market).

## Unterstützte Shopify-Markttypen {#supported-shopify-market-types}

In dieser Phase der Beta können Sie bis zu 25 Einzelland-Märkte in Braze auswählen, vorbehaltlich der folgenden Regeln:

- Jeder ausgewählte Markt muss ein aktiver [Einzelland-Markt](https://help.shopify.com/en/manual/markets/getting-started/market-types#country-or-region-markets) sein. B2B- und Einzelhandelsmärkte werden nicht unterstützt.
  - Die Shopify-Einstellung „Lokale Währungen verwenden“ wird nicht unterstützt.
- Ein Land kann nur einem ausgewählten Markt angehören.
- Mehrländer-Märkte werden in dieser Phase der Beta nicht unterstützt.

Jeder ausgewählte Markt erfordert einen Marktkatalog mit aktiven Produkten, damit Braze Folgendes unterstützen kann:

- Marktspezifische Preise für Produkte unter Verwendung der im Marktkatalog festgelegten Währung
- Produktverfügbarkeit pro Markt
- Produktübersetzungen, die über die Shopify Translate & Adapt-App erstellt wurden (z. B. Produkttitel oder Variantentitel)

![Shopify-Marktprofil für einen Australien-Markt.]({% image_buster /assets/img/shopify/shopify_markets_example.png %})

### Hinweise {#considerations}

#### Allgemein {#general}

- **Ein verbundener Shop:** Sie können jeweils nur einen Markets-fähigen Shopify-Shop mit einem Braze-Workspace verbinden.
- **Locale-Umfang:** Locales übernehmen übersetzte Produkttitel und -beschreibungen basierend auf dem, was Sie mit der Shopify Translate & Adapt-App konfiguriert haben, sowie locale-spezifische URLs. Preis, Währung und andere gemeinsame Katalogfelder bleiben innerhalb eines Marktes über alle Locales hinweg gleich. Standardmäßig verwendet Braze die [Standardsprache](https://help.shopify.com/en/manual/markets/languages) jedes Marktes, die primäre Locale, die Shopify diesem Markt zuweist. Wenn die erweiterte Locale-Unterstützung für Ihr Konto aktiviert ist, synchronisiert Braze zusätzliche Locales, die für diesen Markt konfiguriert sind.

#### Marktkatalog {#market-catalog}

- **Neue Marktansichten in Ihrem ursprünglichen Shopify-Katalog:** Markets erstellt keine separaten Kataloge. Stattdessen werden sie als Teil Ihres ursprünglichen Shopify-Katalogs angezeigt. Markets-Daten werden als neue Katalogzeilen zu Ihrem Shopify-Katalog hinzugefügt.
- **Katalogselektionen:** Bis zu 30 Katalogselektionen.
- **Aktualisierungszeitpunkt:** Marktkatalog-Produktdaten werden einmal täglich aktualisiert.
- **Reine Preiskataloge:** Ein reiner Preismarktkatalog legt marktspezifische Preise fest, ohne Produkte in einem Vertriebskanal zu veröffentlichen. Bestand und Produktverfügbarkeit werden aus Ihrem Standard-Shop-Katalog synchronisiert, während der Preis die Preisliste oder kontextuelle Preisgestaltung des Marktkatalogs widerspiegelt.

### Nicht unterstützte Features {#unsupported-features}

Folgendes wird in dieser Beta nicht unterstützt:

- Preissenkung- und Wieder-verfügbar-Trigger für Marktkataloge
- E-Mail- und SMS-Double-Opt-in für marktbezogen konfigurierte Abo-Gruppen
- Verschachtelte Marktgruppen oder Ländergruppen-Workflows über das aktuelle Einzelland- und Mehrländer-Auswahlmodell hinaus
- Auswahl von mehr als 25 Märkten
- Katalogexport für Markets-fähige Kataloge
- Vollständige Parität mit Shopifys lokaler Währungsumrechnung, Rundungsregeln und Mehrfachkatalog-Niedrigstpreis-Verhalten beim Browsen und Checkout

## Shopify Markets einrichten {#shopify-markets-setup}

### Schritt 1: Ihren Markets-fähigen Shopify-Shop verbinden {#step-1-connect-your-shopify-markets-enabled-store}

1. Verbinden Sie Ihren Shop entweder über die [Shopify-Standardintegration]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration) oder die [angepasste Shopify-Integration]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration). Nachdem Ihr Shop verbunden ist, konfigurieren Sie Shopify Markets im Setup-Composer.
2. Schließen Sie den OAuth-Flow ab und bestätigen Sie, dass Braze die Markets-Scopes im OAuth anfordert:
   - `read_markets`
   - `read_publications`
   - `read_locales`
3. Nachdem die Autorisierung erfolgreich war und der Setup-Composer geöffnet wird, wählen Sie **Begin Setup**.
4. Aktivieren Sie die Braze SDKs.

### Schritt 2: Markt- und Dateneinstellungen auswählen {#step-2-select-your-market-and-data-settings}

1. Wählen Sie unter **Track Shopify Data** die Option **Sync Shopify Markets data**.
2. Wählen Sie **Select Markets**, um Ihren Markt auszuwählen, und stellen Sie sicher, dass Sie das Tracking von Verhaltens-Events und Nutzerattributen aktiviert haben.
   - (Optional) Aktivieren Sie den historischen Backfill.

#### Markets-Nutzerdaten {#markets-user-data}

Zur Unterstützung von Shopify Markets synchronisiert Braze mehr Daten als die [Standard-Events und -Attribute]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#tracked-shopify-events) der Integration.

Braze schreibt diesen zusätzlichen Marktkontext in jedes Kundenprofil:

| Datentyp | Wert | Datenquelle |
| --- | --- | --- |
| Angepasstes Attribut | `shopify_locale` | Shopify |
| Standardattribut | Browsersprache | Braze SDKs |
| Standardattribut | Land | Braze SDKs |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Datentyp des Nutzerprofils"}

Braze erfasst außerdem die folgenden zusätzlichen Bestell-Event-Eigenschaften zur Unterstützung des Marktkontexts:

| Datentyp | Betroffene Events | Neu hinzugefügte Eigenschaften |
| --- | --- | --- |
| Empfohlene E-Commerce-Events | `ecommerce.order_placed`<br>`ecommerce.order_cancelled`<br>`ecommerce.order_refunded` | `country`, `presentment_currency`, `market_handle` |
| Angepasste Events | `shopify_paid_order`<br>`shopify_fulfilled_order`<br>`shopify_partially_fulfilled_order` | `country`, `presentment_currency`, `market_handle` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Datentyp der Bestell-Events"}

Jede Eigenschaft wird aus den folgenden Quellen abgeleitet:

| Eigenschaft | Datenquelle |
| --- | --- |
| `country` | Shopify-Kund:innen `default_address`; falls nicht verfügbar, verwendet Braze `shipping_address` |
| `presentment_currency` | Shopify-Anzeigewährungswert |
| `market_handle` | Konfigurierter Shopify-Markt für das Bestellland; wird nur gesetzt, wenn Märkte konfiguriert sind und das Land übereinstimmt |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Datenquellen der Bestell-Event-Eigenschaften"}

### Schritt 3: Nutzer:innen verwalten {#step-3-manage-users}

1. Wählen Sie Ihren `external_id`-Typ aus dem Dropdown.
2. Aktivieren Sie E-Mail- und SMS-Opt-ins von Shopify, damit Braze E-Mail- und SMS-Abo-Status von Shopify synchronisieren kann. Sie haben zwei Optionen:
  - **Integration verwenden:** Braze synchronisiert E-Mail- und SMS-Status. Sie müssen nur die Abo-Gruppen auswählen, in die synchronisiert wird.
  - **Eigene Lösung erstellen:** Für mehr Kontrolle über die Statusverwaltung können Sie eine angepasste Integration mit den Braze-Abo-Gruppen-Endpunkten erstellen.
3. Erstellen Sie Standard-Abo-Gruppen für jedes Land, das mit Ihren synchronisierten Märkten während der Einrichtung verknüpft ist.
  - **Neue Shopify-Integration:** Weisen Sie eine Standard-E-Mail- und SMS-Abo-Gruppe pro Land zu.
  - **Bestehende Shopify-Integration:** Die aktuelle Standardgruppe Ihres Shops wird nicht mehr synchronisiert. Weisen Sie neue Standard-E-Mail- und SMS-Gruppen pro Land zu. Ihre alte Einrichtung wird nicht automatisch übernommen.

#### Funktionsweise von Opt-ins und Abmeldungen {#how-opt-ins-and-unsubscribes-work}

Während der Einrichtung konfigurieren Sie Standard-E-Mail- und SMS-Abo-Gruppen für jedes Land, das mit Ihren synchronisierten Märkten verknüpft ist (bis zu 25 Länder). Dies ist erforderlich, bevor Sie Ihre Länderkonfiguration speichern können. Sie können auch zusätzliche Abo-Gruppen pro Land zuweisen, wenn Sie die Einwilligung an mehr als eine Liste weiterleiten möchten.

##### Einwilligung gilt für alle konfigurierten Länder {#consent-applies-to-all-configured-countries}

Wenn sich der Einwilligungsstatus von Nutzer:innen in Shopify ändert, wendet Braze diese Änderung auf die Standard-Abo-Gruppen aller Länder an, die mit Ihrem verbundenen Shop verknüpft sind – nicht nur auf das spezifische Land der Nutzer:innen:
  - Wenn Nutzer:innen in Shopify abonniert werden, werden sie in die Standard-E-Mail- oder SMS-Abo-Gruppe für jedes von Ihnen konfigurierte Land eingetragen.
  - Wenn sich Nutzer:innen in Shopify abmelden, werden sie aus der Standard-E-Mail- oder SMS-Abo-Gruppe für jedes von Ihnen konfigurierte Land ausgetragen.

{% alert important %}
Die Shopify-Einwilligung gilt pro Shop, nicht pro Land. In Shopify wird die Einwilligung einmal für E-Mail und einmal für SMS pro Kundendatensatz erfasst und erfolgt nicht nach Land oder Listentyp. Daher kann Braze Einwilligungsänderungen nicht auf ein einzelnes Land oder eine einzelne Abo-Gruppe anwenden. Ein Abonnement- oder Abmeldeereignis in Shopify gilt immer gleichzeitig für die Standard-Abo-Gruppen aller Ihrer konfigurierten Länder. <br><br> Innerhalb von Braze haben Sie jedoch eine granularere Kontrolle über Opt-ins und Opt-outs auf Abo-Gruppen-Ebene, wenn Nutzer:innen mit Messaging-Kanälen interagieren.
{% endalert %}

### Schritt 4: Produkte synchronisieren {#step-4-sync-products}

1. Um Produkte innerhalb Ihres Marktes zu synchronisieren, wählen Sie **Sync Shopify products and variants to Braze**.
2. Weisen Sie die Braze-**Katalog-ID** zu und konfigurieren Sie alle zusätzlichen Einstellungen.

Ihr Katalog enthält eine marktbezogene Ansicht für die Standardprodukte Ihres Shops. Für jedes Produkt, das in Ihrem Markt veröffentlicht ist, fügt Braze eine Marktzeile zu Ihrem bestehenden Katalog hinzu, zusätzlich zu den bereits unterstützten [Standard-Shopify-Katalogfeldern]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs#supported-shopify-catalog-data). Es kann einige Minuten dauern, bis diese synchronisiert sind, wenn Sie Shopify Markets bei einer bestehenden Integration aktivieren.

In Marktzeilen haben diese Felder marktspezifische Werte:

| Feld | Beschreibung |
| --- | --- |
| {% raw %}`market_handle`{% endraw %} | Identifiziert den Markt für die Zeile. Standardmarkt-Zeilen verwenden `default`; zusätzliche Märkte verwenden ihren Handle (z. B. `au`). |
| {% raw %}`locale`{% endraw %} | Wenn die erweiterte Locale-Unterstützung aktiviert ist, identifiziert dies die Locale für die Zeile (z. B. `fr`). |
| {% raw %}`price`{% endraw %} | Marktspezifischer Preis aus der kontextuellen Preisgestaltung des Marktes. |
| {% raw %}`compare_at_price`{% endraw %} | Marktspezifischer Vergleichspreis oder `0`, wenn Shopify keinen Vergleichspreis für diesen Markt hat. |
| {% raw %}`product_title`{% endraw %} | Übersetzter Produkttitel, wenn eine Shopify-Übersetzung für die Locale der Zeile existiert. |
| {% raw %}`variant_title`{% endraw %} | Übersetzter Variantentitel, wenn eine Shopify-Übersetzung für die Locale der Zeile existiert. |
| {% raw %}`product_url`{% endraw %} | Storefront-URL für den Markt und die Locale, wenn lokalisierte URLs aktiviert sind; andernfalls ist dies die Standard-`myshopify.com`-Produkt-URL. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Katalogfelder der Marktzeilen"}

Marktzeilen verwenden eine zusammengesetzte `id` mit dem Markt-Handle als Präfix, z. B. `<market>_<variant_id>`. Wenn die erweiterte Locale-Unterstützung aktiviert ist, enthält die ID auch die Locale (z. B. `<market>_<locale>_<variant_id>`). Ihre Standardprodukte behalten ihre ursprünglichen IDs.

### Schritt 5: Kanäle aktivieren {#step-5-activate-channels}

1. (Optional) Wählen Sie, ob Sie **In-Browser-Messaging** aktivieren möchten.
2. Wählen Sie **Finish Setup**.

## Markets-Nutzerdaten verwenden {#use-markets-user-data}

Nachdem diese Attribute und Eigenschaften in den Nutzerprofilen vorhanden sind, können Sie sie verwenden, um Nutzer:innen nach Markt anzusprechen und Nachrichten zu personalisieren.

### Nach Markt in der Segmentierung filtern {#target-by-market-in-segmentation}

Filtern Sie nach Land, Browsersprache oder `shopify_locale` in Segmenten und in den Eintrittskriterien von Campaigns oder Canvas. Erstellen Sie beispielsweise eine Zielgruppe von Nutzer:innen in einem bestimmten Markt oder teilen Sie einen Canvas nach Locale auf.

### Mit Liquid personalisieren und triggern {#personalize-and-trigger-with-liquid}

Referenzieren Sie die Daten direkt in Ihren Nachrichten.

| Zu referenzierende Nutzerdaten | Zu verwendendes Liquid |
| --- | --- |
| Die Locale der Nutzer:innen | {% raw %}`{{custom_attribute.${shopify_locale}}}`{% endraw %} |
| Das Land der Nutzer:innen | {% raw %}`{{${country}}}`{% endraw %} |
| Das Land einer Bestellung (in einer getriggerten Nachricht) | {% raw %}`{{event_properties.${country}}}`{% endraw %} |
| Der Markt einer Bestellung (in einer getriggerten Nachricht) | {% raw %}`{{event_properties.${market_handle}}}`{% endraw %} |
| Die Währung einer Bestellung (in einer getriggerten Nachricht) | {% raw %}`{{event_properties.${presentment_currency}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Nutzerdaten mit Liquid referenzieren"}

### Nachrichten aus Bestellaktivitäten triggern {#trigger-messages-from-order-activity}

Die neuen Bestelleigenschaften werden mit jedem Bestell-Event übermittelt, sodass Sie eine Nachricht basierend auf einer Bestellung triggern und den Inhalt mit marktbezogenen Details personalisieren können.

Eine einfache Version im Nachrichtentext könnte so aussehen:

{% raw %}
```liquid
Thanks for your order! Your total: {{event_properties.${presentment_currency}}} {{event_properties.${total_value}}}
```
{% endraw %}

Da die Eigenschaften am Event selbst hängen, bleibt die Nachricht ohne zusätzliche Einrichtung für den Markt jedes Nutzers bzw. jeder Nutzerin korrekt.

## Tutorial: Produkte und Preise pro Markt anzeigen {#tutorial-show-products-and-prices-per-market}

Verwenden Sie einen marktbezogenen Katalog, um eine einzelne Nachricht zu erstellen, die allen Nutzer:innen die Produkte und Preise ihres eigenen Marktes anzeigt.

1. Erstellen Sie eine Selektion, die Markets-Daten verwendet.
2. Referenzieren Sie die Selektion in einer Nachricht mit Liquid.

Sie können einen festen Markt verwenden, wenn eine Nachricht auf einen bestimmten Markt abzielt.

### Schritt 1: Eine Selektion mit Markets-Daten erstellen {#step-1-create-a-selection-using-markets-data}

[Selektionen]({{site.baseurl}}/catalog_selections) sind kuratierte Produktsets, die Sie in Nachrichten referenzieren. Für Shopify-Kataloge mit synchronisierten Märkten enthält der Bereich **Filter settings** einen Bereich **Market scope**, der Produktdaten auf einen Markt eingrenzt oder pro Nutzer:in personalisiert.

1. Gehen Sie zu Ihrem Shopify-Katalog und öffnen Sie den Tab **Selections**.
2. Wählen Sie **Create Selection**, benennen Sie die Selektion, fügen Sie eine optionale Beschreibung hinzu und legen Sie ein Ergebnislimit fest.
3. Verwenden Sie unter **Filter settings** im Bereich **Market scope** das Dropdown **Market**, um festzulegen, wie die Selektion marktspezifische Produkte auflöst:
   - **Personalized:** Alle Empfänger:innen sehen Produkte und Preise aus dem Markt, der zum `country`-Attribut ihres Profils passt.
   - **A synced market:** Wählen Sie einen Markt nach Name aus, um die Selektion auf die Produkte und Preise dieses Marktes festzulegen. Verwenden Sie dies, wenn eine Nachricht nur auf einen einzelnen Markt abzielt.
4. Vervollständigen Sie alle weiteren Filterkriterien und speichern Sie die Selektion.
5. Wählen Sie unter **Preview for user** Nutzer:innen aus, um zu sehen, was die Selektion für dieses Profil zurückgibt. Selektionen mit **Personalized** können erst nach Auswahl von Nutzer:innen in der Vorschau angezeigt werden.

| Ziel | Filter |
| --- | --- |
| Ein bestimmter Markt | `market_handle` = `au` |
| Nur Standardprodukte | `market_handle` = `default` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ziele und zugehörige Filter"}

{% alert note %}
Wenn Sie keinen Markt angeben, verwendet Braze Ihre Standardprodukte.
{% endalert %}

### Schritt 2: Marktbezogene Katalogselektionen zu Nachrichten hinzufügen {#step-2-add-market-aware-catalog-selections-to-messages}

Um allen Nutzer:innen die Produkte aus ihrem eigenen Markt in einer einzelnen Nachricht bereitzustellen, erstellen Sie eine Selektion mit diesem Filter:

| Selektionsname | Feld | Operator | Wert |
| --- | --- | --- | --- |
| `market_products` | `market_handle` | equals | {% raw %}`{{shopify_market.handle}}`{% endraw %} |
| `default_products` | `market_handle` | equals | `default` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Selektionsname und zugehörige Filter"}

Zum Sendezeitpunkt ersetzt Braze {% raw %}`{{shopify_market.handle}}`{% endraw %} durch den Markt der jeweiligen Nutzer:innen, sodass `market_products` allen die richtigen Produkte liefert. `default_products` ist der Fallback für Nutzer:innen ohne passenden Markt.

Referenzieren Sie Ihre Selektion in Ihrer Nachricht mit dem {% raw %}`{% shopify_market %}`{% endraw %}-Tag:

{% raw %}
```liquid
{% shopify_market %}
{% if shopify_market.handle %}
  {% catalog_selection_items <your_catalog_name> <your_market-catalog_selection_name> %}
  {% for item in items %}
    {{ item.product_title }} — {{ item.price }}
  {% endfor %}
{% else %}
  {% catalog_selection_items <your_catalog_name> <your_default-catalog_selection_name> %}
  {% for item in items %}
    {{ item.product_title }} — {{ item.price }}
  {% endfor %}
{% endif %}
```
{% endraw %}

- Platzieren Sie {% raw %}`{% shopify_market %}`{% endraw %} vor {% raw %}`{% catalog_selection_items %}`{% endraw %}, damit der Markt der Nutzer:innen gesetzt wird, bevor die Selektion ausgeführt wird.
- Ersetzen Sie `<your_catalog_name>` durch Ihren Katalog und verwenden Sie Ihre eigenen Selektionsnamen, falls diese abweichen.
- Die {% raw %}`{{shopify_market.handle}}`{% endraw %}-Prüfung leitet Nutzer:innen ohne passenden Markt zu `default_products` weiter, sodass sie trotzdem Produkte statt einer leeren Nachricht erhalten.

Zeigen Sie die Vorschau als Nutzer:in in Ihrem Markt an, um zu bestätigen, dass die Nachricht die Produkte, Preise und übersetzten Titel dieses Marktes anzeigt.