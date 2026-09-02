---
nav_title: Produkt-Blöcke
article_title: Drag-and-Drop-Produkt-Blöcke
page_order: 5
description: "Dieser Referenzartikel behandelt Drag-and-Drop-Produkt-Blöcke, mit denen Nutzer:innen schnell dynamische oder statische Präsentationen von Katalogartikeln hinzufügen und konfigurieren können."
tool:
    - Campaigns
    - Canvas
alias: /dnd_product_blocks/
---

# Drag-and-Drop-Produkt-Blöcke {#drag-and-drop-product-blocks}

> Der Drag-and-Drop-Editor ermöglicht es Ihnen, Produkt-Blöcke schnell hinzuzufügen und zu konfigurieren, um Produkte nahtlos in Ihren Nachrichten zu präsentieren – ganz ohne angepassten Liquid-Code.

{% alert important %}
Das Feature für Drag-and-Drop-Produkt-Blöcke befindet sich im Early Access und ist derzeit nur für E-Mail verfügbar. Wenden Sie sich an Ihren Braze Account Manager:in, wenn Sie am Early Access teilnehmen möchten.
{% endalert %}

## Voraussetzungen {#requirements}

| Voraussetzung | Beschreibung |
| --- | --- |
| Empfohlene E-Commerce-Ereignisse | [Empfohlene E-Commerce-Ereignisse]({{site.baseurl}}/ecommerce_events) bieten standardisierte Datenschemata für wichtige Verhaltens-Ereignisse, die vor und nach einer Bestellung auftreten. Diese Ereignisse werden langfristig das bisherige Braze-Kauf-Event ersetzen und zum Standard für das Tracking von Commerce-bezogenem Verhalten werden. <br><br> Empfohlene E-Commerce-Ereignisse sind für dynamische Produkt-Blöcke erforderlich. |
| E-Commerce-Canvas-Templates | Die empfohlenen E-Commerce-Ereignisse unterstützen vorgefertigte Templates, einschließlich E-Commerce-Canvas-Templates für wesentliche Anwendungsfälle wie abgebrochenes Browsing, Warenkorb-Abbruch und Bestellbestätigungen. <br><br>Wenn Sie einen dieser wesentlichen E-Commerce-Anwendungsfälle mit den [E-Commerce-Canvas-Templates]({{site.baseurl}}/ecommerce_use_cases) umsetzen möchten, müssen Sie das bereitgestellte Canvas-Template verwenden oder sich daran orientieren. |
| Braze-Katalog | Sie müssen einen Braze-Katalog erstellen, der die folgenden Felder enthält, die Sie in Ihrer Produkt-Block-Konfiguration verwenden:{::nomarkdown}<code><ul><li>product_title</li><li>product_url</li><li>variant_image_url</li></ul></code>{:/} |
| Katalogauswahl | Für statische Produkt-Blöcke müssen Sie eine [Katalogauswahl]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) erstellen, um festzulegen, welche Produkte in Ihrem Produkt-Block enthalten sein sollen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Typen von Drag-and-Drop-Produkt-Blöcken {#types-of-drag-and-drop-product-blocks}

| Produkt-Block | Zweck | Anwendungsfälle | Verfügbarkeit |
| --- | --- | --- | --- |
| Dynamisch | Personalisieren Sie Ihre Nachrichten mit einer Produktpräsentation basierend auf Kundeninteraktionen, indem Sie [empfohlene E-Commerce-Ereignisse]({{site.baseurl}}/ecommerce_events) und Kataloge innerhalb unserer [E-Commerce-Canvas-Templates]({{site.baseurl}}/ecommerce_use_cases) verwenden. | {::nomarkdown}<ul><li>Abgebrochenes Browsing</li><li>Warenkorb-Abbruch</li><li>Abgebrochener Checkout</li><li>Bestellbestätigungen</li></ul>{:/} | Nur in Canvas verfügbar. |
| Statisch | Personalisieren Sie Produkte mithilfe von Daten, die in einem Braze-Katalog gespeichert sind. Sie müssen eine [Katalogauswahl]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) verwenden, um festzulegen, welche Produkte enthalten sein sollen. | Ideal für die Präsentation neuer Produkteinführungen oder kategoriespezifischer Angebote. | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Typen von Drag-and-Drop-Produkt-Blöcken" }

## Inhaltskonfiguration von Produkt-Blöcken {#product-block-content-configuration}

Jeder Block-Typ hat unterschiedliche Inhaltskonfigurationen.

### Produktfelder {#product-fields}

Wählen Sie im Abschnitt **Product Fields** Ihren Produkt-Block-Typ aus und aktivieren Sie dann die Felder, die Sie für jedes Produkt einbeziehen möchten. Jedes Feld wird je nach ausgewähltem Produkt-Block-Typ aus unterschiedlichen Quellen bezogen.

#### Dynamischer Produkt-Block {#dynamic-product-block}

| Produktfeld | Quelle |
| --- | --- |
| Variantenbild | Kataloge |
| Produkttitel | Kataloge |
| Button für Produkt-URL | Kataloge |
| Preis | Eigenschaft des empfohlenen E-Commerce-Ereignisses |
| Menge | Eigenschaft des empfohlenen E-Commerce-Ereignisses |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Dynamischer Produkt-Block" }

![Produktfelder für einen dynamischen Produkt-Block, unterteilt in Katalogdaten und Ereignisdaten]({% image_buster /assets/img/product_blocks/dynamic_fields.png %}){: style="max-width:50%;"}

#### Statischer Produkt-Block {#static-product-block}

| Produktfeld | Quelle |
| --- | --- |
| Variantenbild | Kataloge |
| Produkttitel | Kataloge |
| Button für Produkt-URL | Kataloge |
| Preis | Kataloge |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Statischer Produkt-Block" }

![Produktfelder für einen statischen Produkt-Block, die alle als Katalogdaten kategorisiert sind.]({% image_buster /assets/img/product_blocks/static_fields.png %}){: style="max-width:50%;"}

### Layout-Optionen {#layout-options}

Verwenden Sie Layout-Optionen, um anzupassen, wie Ihre Produkte innerhalb Ihres Produkt-Blocks angezeigt werden.

| Option | Beschreibung |
| --- | --- |
| Produktausrichtung | Wählen Sie, wie das Bild und die Produktfelder innerhalb des Blocks ausgerichtet werden. |
| Ausrichtung | Passen Sie die Ausrichtung der Textfelder und des Buttons innerhalb des Blocks an. |
| Maximale Produkte pro Zeile | Zeigen Sie bis zu drei Produkte pro Zeile an, insgesamt bis zu 12 Produkte für statische Produkt-Blöcke und bis zu 24 Produkte für dynamische Produkt-Blöcke. |
| Produktabstand | Legen Sie den Abstand zwischen den Produkten fest. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Layout-Optionen" }

![Layout-Optionen für Produktausrichtung, Ausrichtung, maximale Produkte pro Zeile und Produktabstand.]({% image_buster /assets/img/product_blocks/layout_options.png %}){: style="max-width:50%;"}

### Globale E-Mail-Stileinstellungen {#global-email-style-settings}

[Globale E-Mail-Stileinstellungen]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings) ermöglichen es Ihnen, einheitliche Stile auf Ihre E-Mails in Braze anzuwenden. Das bedeutet, dass Sie bestimmte Stile – wie Schriftarten, Farben und Button-Designs – definieren können, die automatisch auf alle Ihre E-Mails angewendet werden.

#### Wie globale E-Mail-Stileinstellungen mit Produkt-Blöcken funktionieren {#how-global-email-style-settings-work-with-product-blocks}

Bestehende Stile für Absätze und Buttons werden automatisch auf die Text- und Button-Elemente innerhalb des Produkt-Blocks angewendet. Das bedeutet, dass Ihr Produkt-Block konsistent alle Formatierungen verwendet, die Sie für Absätze und Buttons festgelegt haben, und so ein einheitliches Erscheinungsbild in Ihrer gesamten E-Mail gewährleistet wird.

## Produkt-Blöcke einrichten {#setting-up-product-blocks}

### Katalog-Einrichtung {#catalog-setup}

{% alert important %}
Wenn Sie die Braze- und Shopify-Integration für die [Produktsynchronisierung]({{site.baseurl}}/shopify_catalogs) verwenden, sind keine zusätzlichen Schritte erforderlich, um Drag-and-Drop-Produkt-Blöcke zu nutzen.<br><br> Wenn Sie keine Produktvarianteninformationen haben, müssen Sie die übergeordneten Produktinformationen sowohl in den Produkt- als auch in den Produktvariantenfeldern innerhalb der Ereignis-Payloads und Kataloge duplizieren. Das bedeutet, dass Sie dieselben Produktdetails für beide Bezeichner angeben müssen, um die Konsistenz für die korrekte Funktion des Produkt-Blocks sicherzustellen.
{% endalert %}

Um Drag-and-Drop-Produkt-Blöcke zu verwenden, müssen Sie einen Braze-Katalog mit bestimmten Feldwerten einrichten. Diese Felder verwenden Sie in Ihrer Produkt-Block-Konfiguration. Stellen Sie sicher, dass Ihr Katalog die folgenden Felder enthält:

| Feld | Beschreibung |
| --- | --- |
| `product_title` | Der Titel des Produkts. |
| `product_url` | Die URL, unter der Kund:innen das Produkt ansehen oder kaufen können. |
| `variant_image_url` | Die URL für das Variantenbild. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Katalog-Einrichtung" }

Starten Sie direkt mit diesem [Beispiel-Produktkatalog](/docs/assets/download_file/ecommerce_product_catalog_sample.csv), der die erforderlichen Felder enthält.

![Eine Beispiel-CSV-Datei mit den erforderlichen Feldern sowie weiteren Feldern.]({% image_buster /assets/img/ecommerce/sample_product_catalog.png %})

#### Zuordnung zu Katalogfeldern {#mapping-to-catalog-fields}

Im Tab **Einstellungen** Ihres Katalogs können Sie den Schalter **Product blocks** aktivieren, um bestimmte Felder und Informationen in Ihrem Katalog zuzuordnen. So können Sie auswählen, welche Felder als Produkttitel, Produkt-URL und Bild-URL verwendet werden sollen. Beachten Sie, dass Shopify-Katalogfelder standardmäßig zugeordnet sind und nicht geändert werden können.

{% alert note %}
Wenn Sie Shopify nicht verwenden, können Sie sich an Ihren Account Manager:in wenden, um die Feldzuordnung zu aktivieren. Damit können Sie jeden Katalog mit Produkt-Blöcken verbinden und seine Felder den Feldern `product_title`, `product_url` und `variant_image_url` zuordnen.
{% endalert %}

## Produkt-Blöcke erstellen {#creating-product-blocks}

Diese Anleitung führt Sie durch die Schritte zum Erstellen, Testen und Sicherstellen der Funktionalität eines dynamischen oder statischen Produkt-Blocks mit unserem E-Mail-Drag-and-Drop-Editor.

### 1. Schritt: E-Mail-Campaign oder E-Mail-Canvas-Schritt erstellen {#step-1-create-an-email-campaign-or-email-canvas-step}

#### Dynamischer Produkt-Block

{% alert note %}
Dynamische Produkt-Blöcke erfordern [empfohlene E-Commerce-Ereignisse]({{site.baseurl}}/ecommerce_events) und können nur innerhalb von [Canvase]({{site.baseurl}}/ecommerce_use_cases) verwendet werden. Für Braze-Shopify-Nutzer:innen sind diese Ereignisse automatisch als Teil der Integration enthalten. Für Nicht-Shopify-Nutzer:innen müssen Sie mit Ihren Entwickler:innen zusammenarbeiten, um diese Ereignisse an Braze zu übergeben und sicherzustellen, dass der primäre Produktbezeichner innerhalb der Ereignisse als Katalog-Artikel-ID hinzugefügt wird.
{% endalert %}

Erstellen Sie ein neues Canvas, das eines der verfügbaren Braze-Templates für Ihren spezifischen Anwendungsfall verwendet:
- Abgebrochenes Browsing
- Warenkorb-Abbruch
- Abgebrochener Checkout
- Bestellbestätigungen

Detaillierte Anweisungen zum Erstellen Ihrer E-Commerce-Canvase finden Sie unter [E-Commerce-Anwendungsfälle]({{site.baseurl}}/ecommerce_use_cases).

#### Statischer Produkt-Block

Erstellen Sie eine Drag-and-Drop-E-Mail-Campaign, ein aktionsbasiertes Canvas oder ein Template mit einem Drag-and-Drop-E-Mail-Nachrichten-Schritt.

### 2. Schritt: Produkt-Block hinzufügen {#step-2-add-a-product-block}

{% tabs %}
{% tab Dynamischer Produkt-Block %}

Erstellen Sie innerhalb des Nachrichten-Schritts eine E-Mail oder bearbeiten Sie das vorhandene Template mit dem Drag-and-Drop-E-Mail-Composer.
Ziehen Sie einen Produkt-Block in Ihre E-Mail-Nachricht.
Bestätigen Sie, dass der dynamische Block-Typ ausgewählt ist.
Wählen Sie den Produktkatalog aus, den Sie für die Personalisierung verwenden möchten. Stellen Sie sicher, dass er mit den Produkten aus den eingehenden Ereignissen übereinstimmt, die Sie ansprechen.

{% endtab %}
{% tab Statischer Produkt-Block %}

Ziehen Sie einen Produkt-Block in Ihre E-Mail-Nachricht und wählen Sie den statischen Block-Typ aus.
Wählen Sie den Katalog aus, den Sie für Ihren Produkt-Block verwenden möchten. Sie müssen eine Katalogauswahl treffen, um festzulegen, welche Produkte in Ihrem Produkt-Block angezeigt werden.

{% endtab %}
{% endtabs %}

![Der Tab „Content“ mit Editor-Blöcken, wie z. B. Produkt-Blöcken.]({% image_buster /assets/img/product_blocks/product_block.png %}){: style="max-width:40%;"}

### 3. Schritt: Produktfelder konfigurieren {#step-3-configure-product-fields}

Wählen Sie aus, welche [Produktfelder](#product-fields) im Produkt-Block angezeigt werden sollen. Wählen Sie nach jeder Änderung **Apply Settings**, um die Aktualisierungen im Editor zu sehen.

Sie können auch den Text vor Ihren Liquid-Tags anpassen. Beispielsweise können Sie ein Dollarzeichen ($) vor dem Preis eines Artikels einfügen oder den Begriff für Menge in „Anzahl“ oder ein anderes bevorzugtes Label ändern.

![Produkt-Block mit einem vorangestellten Dollarzeichen vor dem Artikelpreis.]({% image_buster /assets/img/product_blocks/liquid.png %}){: style="max-width:45%;"}

### 4. Schritt: Layout-Einstellungen konfigurieren {#step-4-configure-layout-settings}

Ändern Sie die [Layout-Optionen](#layout-options), um die Darstellung der Produkte innerhalb Ihres Produkt-Blocks anzupassen, und wählen Sie nach jeder Änderung **Apply settings**.

### 5. Schritt: Nachricht in der Vorschau anzeigen und testen {#step-5-preview-and-test-your-message}

{% tabs %}
{% tab Dynamischer Produkt-Block %}

1. Zeigen Sie im Abschnitt **Preview & Test** die Nachricht als benutzerdefinierte:r Nutzer:in in der Vorschau an.
2. Geben Sie an, wie viele Artikel in der Vorschau gerendert werden sollen.
3. Bestätigen Sie, dass die richtige Anzahl von Artikeln angezeigt wird und Ihre Layout-Optionen korrekt angewendet werden. Beachten Sie, dass die angezeigten Artikel zufällig ausgewählt werden.

![Tab „Preview as a User“ mit einem Dropdown-Bereich „Dynamic product block“, der die Anzeige von 4 Artikeln festlegt.]({% image_buster /assets/img/product_blocks/preview_as_a_user.png %}){: style="max-width:40%;"}

{% endtab %}
{% tab Statischer Produkt-Block %}

Eine Vorschau wird im Drag-and-Drop-Composer generiert, wenn Sie Änderungen an Ihrem Produkt-Block anwenden.

![E-Mail-Drag-and-Drop-Composer mit einem generierten Produkt-Block mit verschiedenen Artikelkacheln.]({% image_buster /assets/img/product_blocks/static_block_preview.png %})

{% endtab %}
{% endtabs %}

Nachdem Sie Ihre Nachricht erstellt und bestätigt haben, dass sie wie erwartet aussieht, können Sie sie versenden!