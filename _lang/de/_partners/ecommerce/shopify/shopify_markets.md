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

## So funktioniert die Integration {#how-the-integration-works}

Shopify Markets erweitert Ihre bestehende Shopify-Integration. Verbinden Sie Ihren Standard-Storefront über den [Standard]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration)- oder [angepassten (SDK)]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration)-Integrationspfad und wählen Sie dann die Märkte aus, die Braze aus den konfigurierten Märkten Ihres Shops synchronisieren soll. Bestehende Integrationen können Märkte hinzufügen, ohne Kataloge, Abo-Gruppen oder Events zu beeinträchtigen. Eine schrittweise Anleitung finden Sie unter [Shopify Markets einrichten](#shopify-markets-setup).

Shopify Markets bietet die folgenden Funktionen:

- **Marktbezogene Profile:** Die Integration erfasst die Shopify-Locale jedes Nutzers bzw. jeder Nutzerin zusammen mit den Standard-Länder- und Sprachattributen von Braze, sodass Sie ohne angepasste Konfiguration nach Markt segmentieren und triggern können.
- **Lokalisierte Kataloge:** Marktspezifische Produktdaten werden täglich synchronisiert, einschließlich Preise und Währung sowie übersetzte Titel, Beschreibungen und Produkt-URLs.
- **Marktbezogene Personalisierung:** Verwenden Sie den {% raw %}`{% shopify_market %}`{% endraw %} Liquid-Tag, um Inhalte mit Katalogprodukten aus dem jeweiligen Markt der Nutzer:innen zu personalisieren, einschließlich der von Shopify übersetzten Inhalte. Sie können auch Marktdetails wie die Anzeigewährung aus unterstützten Shopify-Events wie `ecommerce.order_placed` referenzieren.
- **Fallback auf den Standard-Shop:** Wenn Nutzer:innen keinem Ihrer verbundenen Märkte angehören, verwendet Braze Ihre Standard-Shop-Einstellungen und -Produkte, sodass alle Nutzer:innen eine vollständige und korrekte Nachricht erhalten.

Beispiele finden Sie unter [Markets-Nutzerdaten verwenden](#use-markets-user-data) und [Tutorial: Produkte und Preise pro Markt anzeigen](#tutorial-show-products-and-prices-per-market).

## Unterstützte Shopify-Markttypen {#supported-shopify-market-types}

Sie können bis zu 25 aktive [Einzelland- oder Mehrländermärkte](https://help.shopify.com/en/manual/markets/getting-started/market-types#country-or-region-markets) auswählen. Jedes Land kann nur einem ausgewählten Markt angehören.

Subregionenmärkte, Einzelhandelsmärkte, B2B-Märkte und Kanalmärkte werden nicht unterstützt.

### Was jeder Markt benötigt {#what-each-market-needs}

Jeder ausgewählte Markt benötigt einen Marktkatalog mit aktiven Produkten. Braze liest die folgenden Daten aus diesem Katalog:

| Daten | Beschreibung |
| --- | --- |
| Preise | Im Marktkatalog festgelegt, in der für diesen Markt angegebenen Währung. Die Shopify-Einstellung „Use local currencies“ wird nicht unterstützt. |
| Übersetzungen | Angepasste Übersetzungen, die über die Shopify-App „Translate & Adapt“ erstellt wurden, z. B. Produkttitel und Variantentitel. Braze unterstützt derzeit keine spezifischen Marktspracheinstellungen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Was jeder Markt benötigt" }

![Shopify-Marktprofil für einen Australien-Markt.]({% image_buster /assets/img/shopify/shopify_markets_example.png %})

### Hinweise {#considerations}

#### Allgemein {#general}

- **Ein verbundener Shop:** Sie können jeweils nur einen Markets-fähigen Shopify-Shop mit einem Braze-Workspace verbinden.
- **Locale-Umfang:** Locales rufen übersetzte Produkttitel und Beschreibungen ab, basierend auf Ihren Konfigurationen in der Shopify-App „Translate & Adapt“, sowie Locale-spezifische URLs. Preis, Währung und andere gemeinsame Katalogfelder bleiben innerhalb eines Marktes über alle Locales hinweg gleich. Standardmäßig verwendet Braze die [Standardsprache](https://help.shopify.com/en/manual/markets/languages) jedes Marktes – die primäre Locale, die Shopify diesem Markt zuweist. Wenn Sie die erweiterte Locale-Unterstützung aktivieren, synchronisiert Braze zusätzliche Locales, die für diesen Markt konfiguriert sind.

#### Marktkatalog {#market-catalog}

- **Neue Marktansichten in Ihrem ursprünglichen Shopify-Katalog:** Markets erstellt keine separaten Kataloge. Stattdessen zeigt Braze sie als Teil Ihres ursprünglichen Shopify-Katalogs an. Marktdaten werden als neue Katalogzeilen zu Ihrem Shopify-Katalog hinzugefügt.
- **Katalogauswahlen:** Bis zu 30 Katalogauswahlen.
- **Aktualisierungsintervall:** Produktdaten des Marktkatalogs werden einmal täglich aktualisiert.
- **Marktpreise und lokalisierte Inhalte:** Marktzeilen enthalten den Marktpreis und `compare_at_price`, einschließlich lokalisierter Produkt- und Variantentitel sowie Produkt-URLs, wenn Übersetzungen über die Shopify-App „Translate & Adapt“ eingerichtet sind.
- **Lagerbestand:** Marktzeilen enthalten aggregierte Bestandswerte. Braze bietet derzeit keine Möglichkeit, den Bestand zwischen Standorten zu unterscheiden.
- **Preissenkung:** Wird für Marktkataloge unterstützt. Eine Preisänderung in einem Marktkatalog löst basierend auf dem Preis dieses Marktes aus, nicht auf Ihrem Standard-Shoppreis. Da Produktdaten des Marktkatalogs einmal täglich aktualisiert werden, werden Preissenkungen täglich erkannt und nicht zum Zeitpunkt der Preisänderung in Shopify.
- **Wieder auf Lager:** [Wieder auf Lager]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications) wird für Produkte in Ihrem Standard-Shopkatalog unterstützt. Marktzeilen lösen keine Wieder-auf-Lager-Benachrichtigungen aus. „Wieder auf Lager“ betrachtet den gesamten verfügbaren Bestand für eine Produktvariante über alle Shopify-Standorte hinweg, sodass Bestand, der an einem Einzelhandelsstandort hinzugefügt wird, eine Benachrichtigung auslösen kann.

## Einrichtung von Shopify Markets {#shopify-markets-setup}

### Wenn Sie bereits eine aktive Shopify-Integration haben {#if-you-already-have-an-active-shopify-integration}

Markets erweitert Ihre bestehende Integration. Sie müssen sie weder trennen noch Ihre Einrichtung neu aufbauen.

- Ihre Abo-Gruppen werden zu Ihren Shop-weiten Gruppen und erhalten weiterhin jedes Opt-in, einschließlich aller zusätzlich zugewiesenen Gruppen.
- Ihre bestehenden Abonnent:innen bleiben in den Gruppen, in denen sie bereits sind. Wenn Sie später Ländergruppen hinzufügen, fügt Braze bestehende Abonnent:innen diesen nicht hinzu.
- Ihr Katalog wird weiterhin synchronisiert. Markt-Zeilen werden zu diesem Katalog hinzugefügt, nicht zu einem neuen, und Ihre bestehenden Auswahlen funktionieren weiterhin mit Ihren Standardzeilen.
- Ihr Standard-Shop wird neben Ihren ausgewählten Märkten angezeigt, sodass Sie Abo-Gruppen zuweisen und Katalogauswahlen dafür auf die gleiche Weise erstellen können.

Wenn Ihr Shop bereits verbunden ist, beginnen Sie mit [Schritt 2](#step-2-select-your-market-user-data), um mehr über jede Konfiguration und ihre Funktionsweise zu erfahren.

### Schritt 1: Ihren Shopify Markets-fähigen Shop verbinden {#step-1-connect-your-shopify-markets-enabled-store}

1. Verbinden Sie Ihren Shop über den Pfad der [Shopify-Standardintegration]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration) oder der [benutzerdefinierten Shopify-Integration]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration). Nachdem Ihr Shop verbunden ist, konfigurieren Sie Shopify Markets im Einrichtungs-Composer.
2. Schließen Sie den OAuth-Flow ab und bestätigen Sie, dass Braze die Markets-Scopes im OAuth anfordert:
   - `read_markets`
   - `read_publications`
   - `read_locales`
3. Nachdem die Autorisierung erfolgreich war und der Einrichtungs-Composer geöffnet wurde, wählen Sie **Einrichtung beginnen**.
4. Aktivieren Sie die Braze SDKs.

### Schritt 2: Ihre Markt-Nutzerdaten auswählen {#step-2-select-your-market-user-data}

1. Wählen Sie unter **Shopify-Daten verfolgen** die Option **Shopify-Markets-Daten synchronisieren**.
2. Wählen Sie **Märkte auswählen**, um Ihren Markt auszuwählen, und stellen Sie sicher, dass Sie das Tracking von Verhaltens-Events und Nutzerattributen aktiviert haben.
   - (Optional) Aktivieren Sie die historische Rückfüllung

#### Markt-Nutzerdaten {#markets-user-data}

Um Shopify Markets zu unterstützen, synchronisiert Braze zusätzliche Daten über die [Standard-Events und -Attribute]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#tracked-shopify-events) der Integration hinaus.

##### Nutzerprofilattribute {#user-profile-attributes}

| Attribut | Datentyp | Beschreibung | Datenquelle |
| --- | --- | --- | --- |
| `shopify_locale` | Angepasstes Attribut | Die Sprache, in der Kund:innen Ihren Shop durchsuchen, z. B. `en` oder `fr-CA`. Sie ändert sich, wenn die Sprache der Storefront gewechselt wird. | Shopify-Kundenlocale |
| `browser_language` | Standardattribut | Die im Browser der Kund:innen eingestellte Sprache. | Braze SDKs |
| `country` | Standardattribut | Das Land der Kund:innen. | Braze SDKs |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Nutzerprofilattribute"}

##### Bestell-Event-Eigenschaften {#order-event-properties}

| Eigenschaft | Beschreibung | Datenquelle |
| --- | --- | --- |
| `country` | Zweistelliger Ländercode für die Kund:innen. | Die `default_address` der Kund:innen in Shopify oder die `shipping_address` der Bestellung, falls keine Standardadresse festgelegt ist |
| `presentment_currency` | Die Währung, in der die Kund:innen bezahlt haben, die sich von Ihrer Shop-Währung unterscheiden kann. | Shopify-Bestellung, Anzeigewährung |
| `market_handle` | Handle des Marktes, der dem Land der Kund:innen entspricht. Leer, wenn kein konfigurierter Markt übereinstimmt. | Braze, aus Ihrer Marktkonfiguration |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Bestell-Event-Eigenschaften"}

Diese Eigenschaften werden hinzugefügt zu:

- Empfohlenen E-Commerce-Events: `ecommerce.order_placed`, `ecommerce.order_cancelled`, `ecommerce.order_refunded`
- Angepassten Events: `shopify_paid_order`, `shopify_fulfilled_order`, `shopify_partially_fulfilled_order`

##### Wie diese Markt-Event-Eigenschaften funktionieren {#how-these-market-event-properties-work}

| Eigenschaft | Funktionsweise |
| --- | --- |
| `market_handle` | `market_handle` ist der Handle, den Sie dem Markt in Shopify gegeben haben, z. B. `france`. Derselbe Handle wird als Präfix für Marktzeilen-IDs in Ihrem Katalog verwendet, z. B. `france_46714756268231`. Er ist leer, wenn Sie keine Märkte konfiguriert haben oder wenn das Land der Bestellung nicht mit einem von Ihnen konfigurierten Markt übereinstimmt. Prüfen Sie daher auf einen leeren Wert, bevor Sie ihn in Liquid oder einem Segment-Filter verwenden. |
| `country` | `country` stammt aus der Standardadresse der Kund:innen und verwendet die `shipping_address`, falls die Standardadresse nicht existiert. Beispielsweise behält ein:e Kund:in in Frankreich, der/die eine Bestellung nach Japan sendet, weiterhin den Markt Frankreich. |
| Event-Eigenschaften | Event-Eigenschaften sind eine Momentaufnahme des Zeitpunkts, an dem das Event stattfand, und ändern sich danach nicht. Wenn Kund:innen ihre Standardadresse später aktualisieren, verwenden neue Events das neue Land, während vergangene Events das Land behalten, mit dem sie aufgezeichnet wurden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Wie Markt-Event-Eigenschaften funktionieren"}

##### Währung {#currency}

Unterstützte Shopify-Warenkorb-, Checkout- und Bestell-Events enthalten zwei Wertesätze:
- Ihre Shop-Währung in den vorhandenen Preis- und Gesamtfeldern, unverändert
- Das `presentment_currency`-Objekt mit den Beträgen, die die Kund:innen gesehen und bezahlt haben

Verwenden Sie `presentment_currency`, wenn Sie Kund:innen anzeigen, was sie bezahlt haben, z. B. in einer Bestellbestätigung oder einer Warenkorb-Abbruch-Nachricht. Verwenden Sie die Shop-Währungswerte, wenn Sie Umsätze über Märkte hinweg vergleichen, da diese bereits in einer einheitlichen Währung vorliegen.

##### Lokalisierte Produktinformationen {#localized-product-information}

Unterstützte Shopify-Events enthalten Produkt- und Variantentitel in Ihrer Standard-Shop-Sprache. Braze übersetzt keine Event-Payloads.

Übersetzte Titel, Beschreibungen und Produkt-URLs befinden sich auf Ihren Markt-Katalogzeilen. Um lokalisierte Produktinformationen in einer Nachricht anzuzeigen, suchen Sie das Produkt in Ihrem Katalog anhand der Produkt- oder Varianten-ID aus dem Event.

### Schritt 3: Nutzer:innen verwalten {#step-3-manage-users}

1. Wählen Sie Ihren `external_id`-Typ aus dem Dropdown.
2. Aktivieren Sie E-Mail- und SMS-Opt-ins von Shopify, wodurch Braze E-Mail- und SMS-Abo-Status von Shopify synchronisieren kann. Sie haben zwei Optionen:
   - **Integration verwenden:** Braze synchronisiert E-Mail- und SMS-Status. Wählen Sie die Abo-Gruppen, in die synchronisiert wird.
   - **Eigene Lösung erstellen:** Für mehr Kontrolle über die Statusverwaltung erstellen Sie eine benutzerdefinierte Integration über die Braze-Abo-Gruppen-Endpunkte.
3. Wählen Sie die Abo-Gruppen, in die Shopify-Einwilligungen synchronisiert werden:
   - **Shop-weite Gruppen (erforderlich):** Wählen Sie mindestens eine E-Mail-Gruppe und eine SMS-Gruppe. Jedes Opt-in, das Braze von Shopify erhält, wird hier aufgezeichnet.
   - **Ländergruppen (optional):** Weisen Sie einem oder mehreren Ländern in Ihren synchronisierten Märkten eine oder mehrere Gruppen zu. Opt-ins werden auch hier aufgezeichnet, wenn Braze das Land der Kund:innen bestimmen kann.

#### Wie Opt-ins und Opt-outs funktionieren {#how-opt-ins-and-opt-outs-work}

In Shopify hat jede:r Kund:in einen E-Mail-Einwilligungsstatus und einen SMS-Einwilligungsstatus. Wenn Kund:innen ein Opt-in durchführen, abonnieren sie Ihre Marke, nicht ein Land oder eine Liste.

Braze zeichnet jedes Opt-in in Ihren Shop-weiten Gruppen auf. Wenn Sie Ländergruppen einrichten und Braze feststellen kann, in welchem Land sich die Kund:innen befinden, wird das Opt-in auch in den Gruppen dieses Landes aufgezeichnet.

Wenn Sie keine Ländergruppen einrichten, gehen Opt-ins nur in Ihre Shop-weiten Gruppen, was der aktuellen Handhabung von Einwilligungen durch Shopify entspricht.

#### Wie Braze das Land bestimmt {#how-braze-determines-country}

| Kanal | Länderbestimmung |
| ------- | ---------------------------- |
| E-Mail | Verwendet zuerst das Shopify-Locale der Kund:innen; falls nicht verfügbar, wird das Länderattribut auf dem Braze-Profil verwendet. |
| SMS | Verwendet das Land der Telefonnummer, das durch E.164-Länder-Routing-Muster bestimmt wird. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze-Länderbestimmung nach Kanal"}

Ein Locale identifiziert ein Land nur dann, wenn es eine Region enthält, z. B. `fr-FR`. Ein Locale wie `fr` allein tut das nicht.

Für SMS stammt das Land aus der Telefonnummer. Der/die Käufer:in muss einer Abo-Gruppe hinzugefügt werden, die Nachrichten an diese Nummer senden kann.

#### Was passiert, wenn jemand ein Opt-in durchführt {#what-happens-when-someone-opts-in}

| Länderstatus | Shop-weite Gruppen | Ländergruppen |
|------------------------------------------|-------------------|---------------------------------------|
| Bestimmt und in Ihren Märkten konfiguriert | Abonniert | In den Gruppen dieses Landes abonniert |
| Kann nicht bestimmt werden | Abonniert | Nicht abonniert |
| Bestimmt, aber nicht in Ihren Märkten konfiguriert | Abonniert | Nicht abonniert |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Opt-in-Ergebnisse nach Länderstatus"}

Die Zugehörigkeit zu Abo-Gruppen basiert auf Einwilligungs-Events von Shopify. Wenn sich das Land oder Locale eines/einer Käufer:in ändert, ändert sich die Gruppenmitgliedschaft nicht. Braze aktualisiert sie nur, wenn Shopify ein neues Einwilligungs-Event sendet, z. B. wenn die Einwilligung nach der Änderung des Landes oder Locales erneut beim/bei der Käufer:in auf Shopify erhoben wird.

{% alert note %}
Ländergruppen steuern die Einwilligung, nicht die Sprache. Ein Land kann mehr als eine Sprache haben. Englisch- und französischsprachige Kund:innen in Kanada, `en-CA` und `fr-CA`, gehören derselben Ländergruppe an. Verwenden Sie `shopify_locale` in Ihren Nachrichten, um die Sprache festzulegen.
{% endalert %}

#### Was passiert, wenn jemand ein Opt-out durchführt {#what-happens-when-someone-opts-out}

Ein Opt-out in Shopify entfernt die Nutzer:innen aus jeder Abo-Gruppe, die Ihrer Shopify-Integration zugewiesen ist. Das gilt unabhängig davon, ob sie das Opt-out über eine Markt-Website oder über ihre Shopify-Kontoseite durchgeführt haben.

Abo-Gruppen in Ihrem Workspace, die der Integration nicht zugewiesen sind, sind nicht betroffen.

#### Opt-ins aus Ländern, die Sie nicht konfiguriert haben {#opt-ins-from-countries-you-havent-configured}

Wenn Kund:innen aus einem Land ein Opt-in durchführen, das nicht Teil Ihrer konfigurierten Märkte ist – sei es, weil Sie es nie hinzugefügt oder den Markt entfernt haben – abonnieren sie Ihre Shop-weiten Gruppen. Sie werden keiner Ländergruppe hinzugefügt.

Die Konfiguration von Märkten schränkt nicht ein, an wen Nachrichten gesendet werden können. Wenn Sie aus rechtlichen oder regulatorischen Gründen keine Nachrichten an ein Land senden können, schließen Sie diese Nutzer:innen mit einem Segment-Filter aus oder leiten Sie sie in eine separate Abo-Gruppe um.

{% alert tip %}
Erstellen Sie dieses Segment als Erlaubnisliste der Länder, die Sie bedienen, nicht als Sperrliste der Länder, die Sie nicht bedienen. Nutzer:innen, deren Land nicht bestimmt werden konnte, haben keinen Länderwert, sodass eine Sperrliste sie nicht erfasst.
{% endalert %}

Für SMS kontrollieren die Länderberechtigungen jeder Abo-Gruppe weiterhin die Zustellung. Nutzer:innen, deren Land für die Gruppe nicht zugelassen ist, erhalten keine Nachrichten von ihr.

#### Nutzer:innen werden nicht nachträglich zu Ländergruppen hinzugefügt {#users-arent-added-to-country-groups-later}

Wenn Braze das Land von Kund:innen zum Zeitpunkt des Opt-ins nicht bestimmen kann, werden sie nur Ihren Shop-weiten Gruppen hinzugefügt. Wenn ihr Land später bekannt wird, werden sie nicht automatisch zu den Gruppen dieses Landes hinzugefügt.

Wenn Sie Markets in einem bereits integrierten Shop aktivieren, werden Ihre bestehenden Abo-Gruppen zu Ihren Shop-weiten Gruppen. Bestehende Abonnent:innen bleiben in diesen Gruppen abonniert und werden nicht automatisch zu neuen Ländergruppen hinzugefügt.

Um sie selbst hinzuzufügen, erstellen Sie ein Segment für diese Nutzer:innen und abonnieren Sie sie mithilfe eines Canvas-[Nutzer-Update]({{site.baseurl}}/user_update)-Schritts.

#### Abonnent:innen über Gruppen hinweg zählen {#counting-subscribers-across-groups}

Ein Opt-in kann Nutzer:innen zu mehr als einer Abo-Gruppe hinzufügen, sodass das Addieren von Gruppensummen dieselbe Person mehrfach zählt. Verwenden Sie ein Segment, wenn Sie eine Anzahl eindeutiger Abonnent:innen benötigen.

#### Funktionsweise {#how-it-works}

1. Ein:e Kund:in abonniert SMS beim Checkout oder über ein Formular.
2. Shopify sendet die Anmeldung an Braze.
3. Braze setzt die Nutzer:innen auf „ausstehend“ und sendet Ihren Bestätigungstext.
4. Die Kund:innen antworten mit Ihrem Bestätigungs-Keyword und werden abonniert.
5. Wenn sie nicht vor Ablauf des Bestätigungsfensters antworten, bleiben sie ausstehend.

Weitere Informationen finden Sie unter [Double-Opt-in]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in).

### Schritt 4: Produkte synchronisieren {#step-4-sync-products}

1. Um Produkte innerhalb Ihres Marktes zu synchronisieren, wählen Sie **Shopify-Produkte und -Varianten mit Braze synchronisieren**.
2. Weisen Sie die Braze-Katalog-ID zu und konfigurieren Sie zusätzliche Einstellungen.

Ihr Katalog enthält eine marktbezogene Ansicht für die Standardprodukte Ihres Shops. Für jedes Produkt, das in Ihrem Markt veröffentlicht wird, fügt Braze eine Marktzeile zu Ihrem bestehenden Katalog hinzu, zusätzlich zu den bereits unterstützten [Standard-Shopify-Katalogfeldern]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs#supported-shopify-catalog-data). Es kann einige Minuten dauern, bis diese synchronisiert sind, wenn Sie Shopify Markets bei einer bestehenden Integration aktivieren.

Auf Marktzeilen haben diese Felder marktspezifische Werte:

| Feld | Beschreibung |
| --- | --- |
| `id` | Eine zusammengesetzte ID mit dem Markt-Handle als Präfix, z. B. `france_46714756268231`. Standardzeilen behalten ihre ursprünglichen Artikel-IDs. |
| `market_handle` | Der Handle, den Sie dem Markt in Shopify gegeben haben, z. B. `france`. |
| `locale` | Das Locale des Marktes, das die Sprache der übersetzten Inhalte bestimmt. |
| `price` | Marktspezifischer Preis aus der kontextuellen Preisgestaltung des Marktes, nach Anwendung etwaiger Preislistenanpassungen. |
| `compare_at_price` | Marktspezifischer Vergleichspreis nach Anpassungen. Braze gibt `0` zurück, wenn kein Vergleichspreis für diesen Markt aufgelöst werden kann, einschließlich wenn die Preisliste des Marktes so eingestellt ist, dass Vergleichspreise aufgehoben werden. |
| `product_title` und `variant_title` | Übersetzte Titel, wenn Übersetzungen über die Shopify-App „Translate & Adapt“ eingerichtet wurden. |
| `product_url` | Die Produkt-URL für diesen Markt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Katalogfelder für Marktzeilen"}

{% alert important %}
`inventory_quantity` ist auf Marktzeilen nicht enthalten. Es erscheint nur auf Standardzeilen, wo es den insgesamt verfügbaren Bestand für eine Produktvariante über alle Shopify-Standorte hinweg widerspiegelt.<br><br>Wenn Sie `compare_at_price` in Liquid verwenden, prüfen Sie auf „0“, bevor Sie ihn anzeigen oder einen Rabatt berechnen. Ein Markt ohne Vergleichspreis zeigt einen Preis von null oder einen falschen Rabatt an.
{% endalert %}

### Schritt 5: Kanäle aktivieren {#step-5-activate-channels}

1. (Optional) Wählen Sie, ob In-Browser-Messaging aktiviert werden soll.
2. Wählen Sie **Einrichtung abschließen**.

## Markets-Nutzerdaten verwenden {#use-markets-user-data}

Nachdem diese Attribute und Eigenschaften in den Nutzerprofilen vorhanden sind, können Sie sie nutzen, um Nutzer:innen nach Markt anzusprechen und Nachrichten zu personalisieren.

### Nach Markt in der Segmentierung filtern {#target-by-market-in-segmentation}

Filtern Sie nach Land, Browsersprache oder `shopify_locale` in Segments sowie in den Eintrittskriterien von Campaigns oder Canvas. Erstellen Sie beispielsweise eine Zielgruppe von Nutzer:innen in einem bestimmten Markt oder teilen Sie einen Canvas nach Gebietsschema auf.

### Mit Liquid triggern und personalisieren {#trigger-and-personalize-with-liquid}

Referenzieren Sie Marktdaten in Ihren Nachrichten mit diesen Liquid-Variablen.

#### Vom Nutzerprofil {#from-the-user-profile}

| Attribut | Liquid |
| --- | --- |
| Die Sprache der Kund:innen | {% raw %}`{{custom_attribute.${shopify_locale}}}`{% endraw %} |
| Das Land der Kund:innen | {% raw %}`{{${country}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liquid-Variablen für Markets-Nutzerprofil"}

#### Von Bestellungs-Events {#from-order-events}

| Event-Eigenschaft | Liquid |
| --- | --- |
| Das Land der Bestellung | {% raw %}`{{event_properties.${country}}}`{% endraw %} |
| Der Markt der Bestellung | {% raw %}`{{event_properties.${market_handle}}}`{% endraw %} |
| Die Währung, in der die Kund:innen bezahlt haben | {% raw %}`{{event_properties.${metadata}.presentment_currency.code}}`{% endraw %} |
| Die Bestellsumme in dieser Währung | {% raw %}`{{event_properties.${metadata}.presentment_currency.<total_value>}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liquid-Variablen für Markets-Bestellungs-Events"}

#### Preise in der Währung der Kund:innen anzeigen {#show-prices-in-the-customers-currency}

Verbinden Sie einen Betrag immer mit dem zugehörigen Währungscode. Ein Betrag ohne Währungsangabe ist der häufigste Fehler im Multi-Market-Messaging, da „129,95“ in jedem Markt etwas anderes bedeutet.

Verwenden Sie die Bestellsumme für Nachrichten auf Bestellebene, wie z. B. eine Bestätigung, und den Produktpreis für Inhalte auf Produktebene, wie z. B. einen Warenkorb oder eine Empfehlung.

{% raw %}
```liquid
Thanks for your order! Your total: {{event_properties.${metadata}.presentment_currency.code}}
{{event_properties.${metadata}.presentment_currency.<total field>}}
```
{% endraw %}

Da diese Eigenschaften mit dem Event mitgeliefert werden, bleibt die Nachricht für den Markt jeder Kund:in ohne zusätzliche Einrichtung korrekt.

#### Auf leere Werte prüfen {#check-for-empty-values}

Zwei Werte sind nicht immer vorhanden, und beide werden falsch dargestellt, wenn sie fehlen.

`market_handle` ist leer, wenn das Land der Kund:innen keinem konfigurierten Markt entspricht. Prüfen Sie dies, bevor Sie darauf basierend verzweigen:

{% raw %}
```liquid
{% if event_properties.${market_handle} != blank %}
  ...
{% endif %}
```
{% endraw %}

`compare_at_price` gibt `0` zurück, wenn für diesen Markt kein Vergleichspreis aufgelöst wird. Prüfen Sie auf `0`, bevor Sie ihn anzeigen oder einen Rabatt berechnen – andernfalls sehen Kund:innen einen durchgestrichenen Preis von null.

#### Lokalisierte Produktinformationen anzeigen {#show-localized-product-information}

Produktnamen in Events sind in Ihrer Standard-Shop-Sprache. Um übersetzte Titel, Beschreibungen oder Produkt-URLs anzuzeigen, schlagen Sie das Produkt in Ihrem Katalog anhand der Produkt- oder Varianten-ID aus dem Event nach. Ein Beispiel finden Sie unter [Tutorial: Produkte und Preise pro Markt anzeigen](#tutorial-show-products-and-prices-per-market).

### Nachrichten über Bestellaktivitäten triggern {#trigger-messages-from-order-activity}

Markteigenschaften sind in unterstützten Shopify-Events enthalten, sodass eine Campaign oder ein Canvas, die bzw. der durch eine Bestellung getriggert wird, diese ohne zusätzliche Einrichtung nutzen kann. Diese Events enthalten `country`, `presentment_currency` und `market_handle`.

| Event-Typ | Events |
| --- | --- |
| Empfohlene E-Commerce-Events | `ecommerce.order_placed`, `ecommerce.order_cancelled`, `ecommerce.order_refunded` |
| Angepasste Events | `shopify_paid_order`, `shopify_fulfilled_order`, `shopify_partially_fulfilled_order` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Shopify Markets-Bestellungs-Events mit Markteigenschaften"}

`presentment_currency` hat im Vergleich zu den anderen die breiteste Abdeckung. Es ist in unterstützten Warenkorb-, Checkout- und Bestellungs-Events enthalten, sodass eine Warenkorb-Abbruch-Nachricht den Betrag anzeigen kann, den Kund:innen gesehen haben, obwohl Warenkorb-Events weder `country` noch `market_handle` enthalten. Weitere Details finden Sie unter [Währung](#currency).

## Markets-Berichte {#markets-reporting}

Wenn Markets aktiviert ist, schlüsselt Braze Umsatz und Nachrichten-Performance nach Land auf.

### Umsatz nach Land {#revenue-by-country}

Ihr Umsatzbericht enthält eine Aufschlüsselung nach Land neben der App-Aufschlüsselung – sowohl für den Lifetime-Zeitraum als auch für einen ausgewählten Zeitraum.

Jede Bestellung wird einem Land zugeordnet, und der gesamte Umsatz fließt in dieses Land ein. Das Land wird zuerst aus der Bestellung und dann aus dem Profil der kaufenden Person ermittelt. Bestellungen, bei denen keines von beidem verfügbar ist, erscheinen unter **Unbekannt**.

Der Umsatz wird in USD angezeigt, genau wie im restlichen Umsatzbericht. Um zu sehen, was eine kaufende Person tatsächlich bezahlt hat, verwenden Sie `presentment_currency` im Bestell-Event.

### Performance nach Land {#performance-by-country}

Die Analytics für Campaigns und Canvas enthalten eine Tabelle **Performance by country**, die zeigt, wie eine Nachricht in jedem Land abgeschnitten hat, sowie eine Gesamtzeile für jedes Land. Währung und Gesamtumsatz werden aus der `presentment_currency` der Bestellung aggregiert.

| Spalte | Beschreibung |
| --- | --- |
| Land | Jedes Land, das Ihre Nachricht erreicht hat. |
| Währung | Die Währung für den Umsatz dieses Landes, aggregiert nach `presentment_currency`. |
| Gesamtumsatz | Umsatz, der diesem Land zugeordnet wurde. |
| Käufe | Käufe, die diesem Land zugeordnet wurden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Beschreibung der einzelnen Spalten in der Tabelle „Performance by country“"}

## Einen Markt entfernen {#remove-a-market}

Wenn Sie einen Markt entfernen, stoppt Braze die Synchronisierung neuer Daten für dessen Länder. Bereits vorhandene Daten werden dadurch nicht gelöscht.

### Abo-Gruppen {#subscription-groups}

Das Entfernen eines Marktes aktualisiert Ihre Marktkonfiguration. Es löscht weder Abo-Gruppen aus Ihrem Workspace noch entfernt es Nutzer:innen, die bereits Ländergruppen abonniert haben.

#### Was sich in Ihrer Konfiguration ändert {#what-changes-in-your-setup}

- Länder des entfernten Marktes erscheinen nicht mehr in der Markt-UI.
- Braze entfernt die Abo-Gruppen-Zuordnungen dieser Länder aus Ihrer Integrationskonfiguration.

#### Was unverändert bleibt {#what-stays-the-same}

- Länder-Abo-Gruppen bleiben in Ihrem Workspace und stehen weiterhin für das Targeting zur Verfügung, aber Shopify synchronisiert keine Opt-outs mehr dorthin. Nutzer:innen, die sich in Shopify abmelden, können in diesen Ländergruppen weiterhin als abonniert erscheinen, es sei denn, Sie aktualisieren deren Abo-Status auf anderem Wege – zum Beispiel über die [Abo-Gruppen-Endpunkte]({{site.baseurl}}/api/endpoints/subscription_groups) oder einen Opt-out-Workflow in Braze.
- Nutzer:innen, die bereits Ländergruppen eines entfernten Marktes abonniert haben, bleiben abonniert.

#### Zukünftige Einwilligungssynchronisierung {#future-consent-sync}

- Neue Opt-ins von Käufer:innen in entfernten Ländern werden nur mit Ihren shopweiten Gruppen synchronisiert, genau wie [Opt-ins aus Ländern, die Sie nicht konfiguriert haben](#opt-ins-from-countries-you-havent-configured).
- Braze synchronisiert keine neuen Opt-ins oder Opt-outs mehr mit den Ländergruppen der entfernten Länder.
- Shopweite Abo-Gruppen erhalten weiterhin Einwilligungsaktualisierungen.

### Nutzerdaten {#user-data}

- Attribute, die bereits im Profil von Nutzer:innen vorhanden sind, einschließlich `shopify_locale` und `country`, ändern sich nicht.
- Das Feld `market_handle` innerhalb neuer Bestellereignisse ist nicht mehr verfügbar.
- Shopify-Markt-Segment-Filter für entfernte Märkte sind nicht mehr verfügbar.
- Liquid-Referenzen auf einen entfernten Markt sind nicht mehr verfügbar.

### Kataloge {#catalogs}

- Marktzeilen für diesen Markt werden nicht mehr aktualisiert und aus Ihrem Katalog entfernt.
- Katalogauswahlen, die auf diesen Marktzeilen basieren, geben keine Produkte mehr zurück. Aktualisieren oder entfernen Sie diese vor Ihrem nächsten Versand.
- Ihre Standardzeilen und alle darauf basierenden Auswahlen sind davon nicht betroffen.

## Tutorial: Produkte und Preise nach Markt anzeigen {#tutorial-show-products-and-prices-per-market}

Verwenden Sie einen marktfähigen Katalog, um eine einzige Nachricht zu erstellen, die allen Nutzer:innen die Produkte und Preise für ihren eigenen Markt anzeigt.

1. Erstellen Sie eine Auswahl, die Marktdaten verwendet.
2. Referenzieren Sie die Auswahl in einer Nachricht mit Liquid.

Sie können einen festen Markt verwenden, wenn eine Nachricht auf einen bestimmten Markt abzielt.

### Schritt 1: Eine Auswahl mit Marktdaten erstellen {#step-1-create-a-selection-using-markets-data}

[Auswahlen]({{site.baseurl}}/catalog_selections) sind kuratierte Produktsets, die Sie in Nachrichten referenzieren. Für Shopify-Kataloge mit synchronisierten Märkten enthält der Bereich **Filter settings** einen Bereich **Market scope**, der Produktdaten auf einen Markt eingrenzt oder sie pro Nutzer:in personalisiert.

1. Gehen Sie zu Ihrem Shopify-Katalog und öffnen Sie den Tab **Selections**.
2. Wählen Sie **Create Selection** aus, benennen Sie die Auswahl, fügen Sie eine optionale Beschreibung hinzu und legen Sie ein Ergebnislimit fest.
3. Wählen Sie unter **Filter settings** im Bereich **Market scope** aus, wie die Auswahl marktspezifische Produkte im Dropdown **Market** auflöst:
   - **Personalized:** Alle Empfänger:innen sehen Produkte und Preise aus dem Markt, der dem `country`-Attribut ihres Profils entspricht.
   - **A synced market:** Wählen Sie einen Markt nach Name aus, um die Auswahl auf die Produkte und Preise dieses Marktes festzulegen. Verwenden Sie diese Option, wenn eine Nachricht nur auf einen einzelnen Markt abzielt.
4. Schließen Sie alle weiteren Filterkriterien ab und speichern Sie die Auswahl.
5. Wählen Sie unter **Preview for user** eine:n Nutzer:in aus, um zu sehen, was die Auswahl für dieses Profil zurückgibt. Auswahlen, die **Personalized** verwenden, können erst nach Auswahl einer/eines Nutzer:in in der Vorschau angezeigt werden.

| Ziel | Filter |
| --- | --- |
| Ein bestimmter Markt | `market_handle` = `au` |
| Nur Standardprodukte | `market_handle` = `default` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ziele und zugehörige Filter"}

{% alert note %}
Wenn Sie keinen Markt angeben, verwendet Braze Ihre Standardprodukte.
{% endalert %}

### Schritt 2: Marktfähige Katalogauswahlen zu Nachrichten hinzufügen {#step-2-add-market-aware-catalog-selections-to-messages}

Um allen Nutzer:innen die Produkte aus ihrem eigenen Markt in einer einzigen Nachricht bereitzustellen, erstellen Sie eine Auswahl mit diesem Filter:

| Name der Auswahl | Feld | Operator | Wert |
| --- | --- | --- | --- |
| `market_products` | `market_handle` | equals | {% raw %}`{{shopify_market.handle}}`{% endraw %} |
| `default_products` | `market_handle` | equals | `default` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Name der Auswahl und zugehörige Filter"}

Zum Sendezeitpunkt ersetzt Braze {% raw %}`{{shopify_market.handle}}`{% endraw %} durch den Markt der jeweiligen Nutzer:innen, sodass `market_products` allen die richtigen Produkte liefert. `default_products` ist der Fallback für Nutzer:innen ohne passenden Markt.

Referenzieren Sie Ihre Auswahl in Ihrer Nachricht mit dem Tag {% raw %}`{% shopify_market %}`{% endraw %}:

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

- Platzieren Sie {% raw %}`{% shopify_market %}`{% endraw %} vor {% raw %}`{% catalog_selection_items %}`{% endraw %}, damit der Markt der Nutzer:innen festgelegt wird, bevor die Auswahl ausgeführt wird.
- Ersetzen Sie `<your_catalog_name>` durch Ihren Katalog und verwenden Sie Ihre eigenen Auswahlnamen, falls diese abweichen.
- Die Prüfung von {% raw %}`{{shopify_market.handle}}`{% endraw %} leitet Nutzer:innen ohne passenden Markt zu `default_products` weiter, sodass sie weiterhin Produkte erhalten, anstatt eine leere Nachricht zu sehen.
- Wenn Sie `compare_at_price` in Liquid verwenden, prüfen Sie vor der Anzeige oder Rabattberechnung auf „0“. Ein Markt ohne Vergleichspreis gibt einen Preis von null aus oder erzeugt einen fehlerhaften Rabatt.

Zeigen Sie eine Vorschau als Nutzer:in in Ihrem Markt an, um zu bestätigen, dass die Nachricht die Produkte, Preise und übersetzten Titel dieses Marktes anzeigt.