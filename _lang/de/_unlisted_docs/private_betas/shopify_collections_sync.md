---
nav_title: Shopify-Kollektionen-Sync
article_title: Shopify-Kollektionen-Sync
permalink: "/shopify_collections_sync/"
description: "Dieser Referenzartikel beschreibt, wie Sie den Shopify-Kollektionen-Sync einrichten, mit dem Sie Ihre Produkte in Kollektionen gruppieren können, damit Kund:innen Ihre Produkte nach Kategorie finden können."
hidden: true
---

# Shopify-Kollektionen-Sync Beta {#shopify-collections-sync-beta}

> Der Shopify-Kollektionen-Sync ermöglicht es Ihnen, Ihre Produkte in Kollektionen zu gruppieren, damit Kund:innen Ihre Produkte nach Kategorie finden können. Für ein nahtloseres Einkaufserlebnis können Sie Artikel aus den Kollektionen Ihres Shops in Ihre Braze-Nachrichten einbinden.

{% alert important %}
Der Shopify-Kollektionen-Sync befindet sich derzeit in der Beta-Phase. Kontaktieren Sie Ihren Braze Account Manager, wenn Sie an der Beta teilnehmen möchten.
{% endalert %}

## Shopify-Kollektionen-Sync einrichten {#setting-up-shopify-collections-sync}

Um Ihre Produkte aus Ihrem Shopify-Shop mit Braze zu synchronisieren, aktivieren Sie das Kontrollkästchen **Sync Shopify collections** im Schritt **Sync products** der [Shopify-Integration](https://braze.com/docs/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify#setting-up-shopify-in-braze).<br><br>![Schritt 4 des Shopify-Produkt-Syncs mit aktiviertem Kontrollkästchen „Sync Shopify collections“.][1]

Sobald Ihre Produkte synchronisiert wurden, können Sie sehen, welche Produkte mit Ihren Kollektionen verknüpft sind, indem Sie Ihren Shopify-Katalog aufrufen. <br><br>![Katalog-Tabellenzeile mit einem Produkt in den Kollektionen „best-sellers“ und „front page“.][2]

In Ihrem Shopify-Katalog können Sie Ihre Shopify-Kollektion im Tab **Selections** anzeigen. <br><br>![Der Tab „Selections“ mit einer Liste von zwei Kollektionen: „best-sellers“ und „front page“.][3]

### Beta-Funktionalität {#beta-functionality}

- Braze unterstützt bis zu 30 Kollektionen.
- Die Sortierreihenfolge Ihrer Kollektion wird derzeit nicht beibehalten oder unterstützt. Die Sortierreihenfolge basiert aktuell auf Folgendem:
    - Den zuletzt zu Ihrer Kollektion hinzugefügten Artikeln.
    - Der Reihenfolge, in der Artikel während kontinuierlicher Syncs aktualisiert werden.
    - Der Reihenfolge, die Sie im Auswahl-Tab für Ihre Shopify-Kollektion festlegen.

## Shopify-Kollektionen verwenden {#using-shopify-collections}

Verwenden Sie Ihre Shopify-Kollektionen, um eine Nachricht für jede Nutzer:in in Ihrer Campaign zu personalisieren, ähnlich wie Sie eine [Braze-Auswahl](https://braze.com/docs/user_guide/personalization_and_dynamic_content/catalogs/selections/) verwenden würden.

{% alert warning %}
Beachten Sie das folgende Verhalten in der Beta: <br><br>Wenn Sie die Beschreibung der Shopify-Kollektion oder die Filtereinstellungen aktualisieren, wird Ihr Shopify-Kollektionen-Sync unterbrochen. Infolgedessen funktioniert Ihre Shopify-Kollektion nicht wie erwartet.
{% endalert %}

### 1. Schritt: Sortierreihenfolge Ihrer Shopify-Kollektion konfigurieren {#step-1-configure-the-sort-order-of-your-shopify-collection}

1. Legen Sie die Reihenfolge fest, in der Ihre Shopify-Kollektionsergebnisse zurückgegeben werden, indem Sie die **Sort Order** im Auswahl-Tab für Ihre Shopify-Kollektion auswählen. Dies umfasst auch eine Option zur Randomisierung der Sortierreihenfolge.
2. Geben Sie die maximale Anzahl der Ergebnisse (bis zu 50) unter **Limit number** ein.
3. Wählen Sie **Update Selection**.

![Die Seite „Edit Selection“, auf der Sie die Filtereinstellungen, den Sortiertyp und das Ergebnislimit auswählen können.][4]

### 2. Schritt: Die Kollektion in einer Campaign verwenden {#step-2-use-the-collection-in-a-campaign}

1. Erstellen Sie eine Campaign und wählen Sie dann **+ Personalization** im Nachrichten-Editor.
2. Wählen Sie Folgendes aus:<br>- **Catalog Items** als **Personalization type**<br>- Den Katalognamen<br>- Die Methode zur Artikelauswahl<br>- Den Auswahl-Namen (Ihr Shopify-Kollektionsname)<br>- Die Informationen, die in Ihrer Nachricht angezeigt werden sollen

{: start="3"}
3. Kopieren Sie das Liquid-Snippet und fügen Sie es dort ein, wo die Informationen in Ihrer Nachricht erscheinen sollen.

![Der Abschnitt „Add Personalization“ mit Feldern zur Auswahl Ihres Katalogs, der Artikelauswahlmethode und der anzuzeigenden Informationen.][5]{: style="max-width:30%;"}

#### Liquid in Auswahl-Ergebnissen {#liquid-in-selection-results}

Die Verwendung von Ergebnissen in Katalogen, wie z. B. angepasste Attribute und angepasste Events, kann dazu führen, dass für jede Nutzer:in in Ihrer Auswahl unterschiedliche Ergebnisse zurückgegeben werden.

[1]: {% image_buster /assets/unlisted_docs/img/shopify/sync_products.png %}
[2]: {% image_buster /assets/unlisted_docs/img/shopify/view_catalog.png %}
[3]: {% image_buster /assets/unlisted_docs/img/shopify/selections_tab.png %}
[4]: {% image_buster /assets/unlisted_docs/img/shopify/edit_selection.png %}
[5]: {% image_buster /assets/unlisted_docs/img/shopify/add_personalization.png %}