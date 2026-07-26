---
nav_title: Produktnachrichten
article_title: Produktnachrichten
page_order: 4
description: "Diese Seite beschreibt, wie Sie WhatsApp-Produktnachrichten verwenden, um interaktive WhatsApp-Nachrichten zu senden, die Produkte aus Ihrem Meta-Katalog präsentieren."
page_type: reference
alias: "/whatsapp_product_messages/"
tool:
 - Campaigns
channel:
 - WhatsApp
---

# Produktnachrichten {#product-messages}

> Produktnachrichten ermöglichen es Ihnen, interaktive WhatsApp-Nachrichten zu senden, die Produkte direkt aus Ihrem Meta-Katalog präsentieren.

Wenn Sie eine WhatsApp-Produktnachricht an Nutzer:innen senden, durchlaufen diese die folgende geschäftskunden Journey:

1. Die Nutzer:innen erhalten Ihre Produkt- oder Katalognachricht in WhatsApp.
2. Die Nutzer:innen fügen Produkte direkt aus WhatsApp ihrem Warenkorb hinzu.
3. Die Nutzer:innen tippen in WhatsApp auf **Place order**.
4. Ihre Website oder App empfängt die Warenkorbdaten von Braze und generiert einen Checkout-Link.
5. Die Nutzer:innen werden zu Ihrer Website oder App weitergeleitet, um den Checkout abzuschließen.

Wenn Nutzer:innen über Katalognachrichten Artikel zu ihrem Warenkorb hinzufügen, empfängt Braze Webhook-Daten für Folgemaßnahmen.

## Voraussetzungen {#requirements}

| Voraussetzung | Beschreibung |
| --- | --- |
| WhatsApp Business-Konto | Um WhatsApp-Produktnachrichten zu verwenden, müssen Sie ein WhatsApp Business-Konto haben, das mit Braze verbunden ist. |
| Meta-Katalog | Sie müssen einen Meta-Katalog in Ihrem Commerce Manager einrichten. |
| Einhaltung der Nutzungsbedingungen | Halten Sie die [Meta Commerce-Nutzungsbedingungen und -Richtlinien](https://www.facebook.com/policies_center/commerce) ein. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Produktnachrichtentypen {#product-message-types}

{% alert note %}
Verbessern Sie Ihr Produktnachrichtenerlebnis mit dem integrierten Produktselektor, auf den Sie während Schritt 4 von [Produktnachrichten einrichten](#setting-up-product-messages) zugreifen können.
{% endalert %}

{% tabs local %}
{% tab Katalognachrichten %}

Katalognachrichten zeigen Ihren gesamten Produktkatalog in einem interaktiven Format an. Sie sind als [Template- und Antwortnachrichten](#building-a-product-message) verfügbar.

Wenn Sie Braze während der [Einrichtung](#setting-up-product-messages) Katalogberechtigungen erteilt haben, können Sie auswählen, welches Vorschaubild den Nutzer:innen angezeigt wird.

{% alert note %}
Sie müssen in Braze keine zusätzlichen Produktauswahlen treffen, da die Katalogverbindung von Meta verwaltet wird und somit in Ihren Produktkatalog übernommen wird.
{% endalert %}


{% endtab %}
{% tab Multi-Produkt-Nachrichten %}

Multi-Produkt-Nachrichten heben bestimmte Produkte aus Ihrem Katalog hervor, mit bis zu 30 hervorgehobenen Artikeln pro Nachricht. Sie sind als [Template- und Antwortnachrichten](#building-a-product-message) verfügbar.

Sie können die Produkte entweder manuell mit IDs auswählen oder, wenn Sie während der [Einrichtung](#setting-up-product-messages) Katalogberechtigungen aktiviert haben, den Dropdown-Produktselektor verwenden.

{% alert important %}
Es gibt ein bekanntes Problem mit der Header-Anzeige bei Multi-Produkt-Nachrichten-Templates auf Meta. Meta ist sich des Problems bewusst und arbeitet an einer Lösung.
{% endalert %}

{% endtab %}
{% tab Einzelprodukt %}

Einzelprodukt-Nachrichten heben ein bestimmtes Produkt aus Ihrem Produktkatalog hervor. Sie sind als [Antwortnachrichten](#building-a-product-message) verfügbar.

Sie können die Produkte entweder manuell mit IDs auswählen oder, wenn Sie während der [Einrichtung](#setting-up-product-messages) Katalogberechtigungen aktiviert haben, den Dropdown-Produktselektor verwenden.

{% endtab %}
{% endtabs %}

## Produktnachrichten einrichten {#setting-up-product-messages}

1. Folgen Sie im [Meta Commerce Manager](https://business.facebook.com/business/loginpage/?next=https%3A%2F%2Fbusiness.facebook.com%2Fcommerce_manager%2F#) den [Anweisungen von Meta](https://www.facebook.com/business/help/1275400645914358?id=725943027795860&ref=search_new_1), um Ihren Meta-Katalog zu erstellen. Stellen Sie sicher, dass Sie sich im selben Meta Business Portfolio befinden, in dem auch Ihr mit Braze verbundenes WhatsApp Business-Konto liegt.
2. Folgen Sie den Anweisungen von Meta, um [Ihren Meta-Katalog](https://www.facebook.com/business/help/1953352334878186?id=2042840805783715) mit Ihrem mit Braze verbundenen WhatsApp Business-Konto zu verbinden, indem Sie die Berechtigung „Manage Catalog“ im Meta Business Manager zuweisen.

![Meta-Seite „Catalogs“ mit einem Pfeil, der auf den Button „Assign partner“ für den Katalog „sweeney_catalog“ zeigt.]({% image_buster /assets/img/whatsapp/meta_catalog.png %}){: style="max-width:90%;"}

Stellen Sie sicher, dass Sie die Braze Business Manager ID `332231937299182` als Partner-Business-ID verwenden.

![Fenster zum Teilen eines Katalogs mit einem Partner, das Felder zur Eingabe einer Partner-Business-ID und zur Zuweisung der Berechtigung „Manage catalog“ enthält.]({% image_buster /assets/img/whatsapp/share_meta_catalog.png %}){: style="max-width:70%;"}

{: start="3"}
3. Wählen Sie Ihre Meta-Katalogeinstellungen aus. Sie müssen **Show catalog icon in chat header** auswählen, um Katalognachrichten zu senden.

![WhatsApp Manager-Einstellungsseite für den Katalog „Catalog_products“.]({% image_buster /assets/img/whatsapp/meta_catalog_settings.png %}){: style="max-width:90%;"}

{: start="4"}
4. Durchlaufen Sie in Braze den [Embedded-Signup]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup)-Prozess, um Berechtigungen zu erteilen. Stellen Sie sicher, dass Sie **alle** Kataloge auswählen, für die Sie Berechtigungen erteilen möchten. Dadurch wird der in Braze integrierte Produktselektor freigeschaltet.

![Fenster mit fünf ausgewählten Katalogen zur Erteilung von Berechtigungen.]({% image_buster /assets/img/whatsapp/select_catalogs.png %}){: style="max-width:50%;"}

{% alert tip %}
Best Practices für die Erstellung von Meta-Katalogen finden Sie unter [Tipps zum Erstellen eines hochwertigen Katalogs im Commerce Manager](https://www.facebook.com/business/help/2086567618225367?id=725943027795860).
{% endalert %}

## Eine Produktnachricht erstellen {#building-a-product-message}

Sie können eine Produktnachricht entweder mit einem WhatsApp-Template oder einer Antwortnachricht erstellen.

{% tabs local %}
{% tab WhatsApp-Nachrichtentemplate %}

1. Gehen Sie in Ihrem Meta Business Manager zu **Message Templates**.
2. Wählen Sie **Catalog** als Format und entscheiden Sie sich dann zwischen **Catalog message** (zeigt den vollständigen Katalog an) und **Multi-product catalog message** (hebt bestimmte Artikel hervor).
3. Erstellen Sie in Braze eine WhatsApp-Campaign oder einen Canvas-Nachrichtenschritt.
4. Wählen Sie die Abo-Gruppe aus, die zu dem Ort passt, an dem Sie das Template eingereicht haben.
5. Wählen Sie **WhatsApp Template Message**.
6. Wählen Sie das Template aus, das Sie verwenden möchten.
    - Wenn Sie ein Multi-Produkt-Template auswählen, geben Sie den Abschnittstitel und die Content-IDs für die hervorzuhebenden Produkte an. Sie können die Content-ID entweder direkt aus Ihrem Meta Commerce Manager kopieren oder, wenn Sie die Berechtigungen für den integrierten Produktselektor aktiviert haben, die Artikel auswählen.

![Artikelliste mit Feldern zur Eingabe Ihrer Abschnittstitel und Content-ID.]({% image_buster /assets/img/whatsapp/multi_product_template.png %}){: style="max-width:60%;"}

![Artikelliste mit Dropdown zur Auswahl von Artikeln.]({% image_buster /assets/img/whatsapp/content_id_items.png %}){: style="max-width:60%;"}

{: start="7"}
7. Fahren Sie mit der Erstellung Ihrer Nachricht fort.

{% endtab %}
{% tab Antwortnachricht %}

1. Erstellen Sie in Braze eine WhatsApp-Campaign oder einen Canvas-Nachrichtenschritt.
2. Wählen Sie eine Abo-Gruppe aus.
3. Wählen Sie **Response Message**.
4. Wählen Sie **Meta Product Messages**.

![Optionen zur Auswahl eines Nachrichtentyps und Antwortnachricht-Layouts, wobei „Response Message“ und „Meta Product Messages“ hervorgehoben sind.]({% image_buster /assets/img/whatsapp/response_message_layouts.png %}){: style="max-width:90%;"}

{: start="5"}
5. Wählen Sie den [Nachrichtentyp](#product-message-types) aus, den Sie verwenden möchten.

![Auswahl des Nachrichtenlayouts „Multi-product“.]({% image_buster /assets/img/whatsapp/multi-product_message_layout.png %}){: style="max-width:90%;"}

{: start="6"}
6. Fahren Sie mit der Erstellung Ihrer Nachricht fort.

![Beispiel einer Meta-Produktnachricht mit ausgefüllten Produktinformationen.]({% image_buster /assets/img/whatsapp/example_response_message.png %}){: style="max-width:90%;"}

{% endtab %}
{% endtabs %}

## Produkte verwalten {#managing-products}

### Zugriff auf den Commerce Manager {#accessing-commerce-manager}

Gehen Sie in Ihrem Meta Business Manager zu **Commerce Manager** und wählen Sie Ihre Organisation aus. Hier können Sie Ihre Katalog-Assets verwalten, wie zum Beispiel:
- Neue Kataloge erstellen
- Produkte zu bestehenden Katalogen hinzufügen
- Produktinformationen aktualisieren
- Eingestellte Artikel entfernen

{% alert important %}
Wenn Sie referenzierte Produkte aus Ihrem Katalog entfernen, können die zugehörigen Nachrichten nicht gesendet werden.
{% endalert %}

## Eingehende Produktanfragen empfangen {#receiving-inbound-product-questions}

Nutzer:innen können auf Ihre Produkt- oder Katalognachricht mit Produktanfragen antworten. Diese kommen als eingehende Nachrichten an, die dann mit einem [Aktionspfad]({{site.baseurl}}/action_paths) sortiert werden können.

Darüber hinaus extrahiert Braze die Produkt-ID und Katalog-ID aus diesen Anfragen. Wenn Sie also Antworten automatisieren oder Anfragen an ein anderes Team (z. B. den Support) weiterleiten möchten, können Sie diese Details einbeziehen. Sie könnten beispielsweise Antworten mit den WhatsApp-Eigenschaften `inbound_product_id` oder `inbound_catalog_id` personalisieren.

![Fenster „Personalisierung hinzufügen“ mit dem Personalisierungstyp „WhatsApp Properties“ und dem hervorgehobenen Attribut „inbound_product_id“.]({% image_buster /assets/img/whatsapp/inbound_product_questions.png %}){: style="max-width:60%;"}

## Checkout: Warenkorbverarbeitung und Webhooks {#checkout-cart-processing-and-webhooks}

Wenn Nutzer:innen mit Ihren WhatsApp-Produktnachrichten interagieren, können sie Produkte durchsuchen und Artikel zu ihrem Warenkorb hinzufügen. Derzeit gibt es jedoch keine integrierte Checkout-Funktionalität für Versandinformationen oder Zahlungsabwicklung. Stattdessen empfehlen wir Ihnen, einen Warenkorb in Ihrer eigenen App oder Website zu erstellen und die Nutzer:innen über einen benutzerdefinierten Link zu diesem Warenkorb weiterzuleiten.

### Hinweise {#considerations}

- **Kein In-App-Checkout:** Nutzer:innen können Käufe nicht direkt in WhatsApp abschließen. Alle Transaktionen müssen auf Ihre Website oder App umgeleitet werden.
- **Benutzerdefinierter Link erforderlich:** Sie müssen einen benutzerdefinierten Link erstellen, der die Nutzer:innen zu ihrem Warenkorb auf Ihrer Plattform weiterleitet.
- **Manuelle Einrichtung:** Der Einrichtungsprozess erfordert eine manuelle Konfiguration Ihres Warenkorbs und Ihrer Messaging-Workflows.

{% alert note %}
Wir unterstützen derzeit keine Zahlungen, die direkt in WhatsApp stattfinden. Zukünftige Unterstützung wird länderspezifisch sein (derzeit bietet Meta dies nur für Unternehmen an, die in Indien, Brasilien und Singapur ansässig sind und direkt mit Nutzer:innen in diesen Ländern arbeiten).
{% endalert %}

### Warenkorb-Event-Trigger einrichten {#setting-up-cart-event-triggers}

Wenn Kund:innen eine Bestellung in WhatsApp aufgeben, führt Braze automatisch folgende Schritte aus:
1. Empfängt den Warenkorbinhalt von WhatsApp (Produkt-IDs, Mengen und andere Bestelldaten).
2. Erstellt ein `ecommerce.cart_update` E-Commerce-Event mit allen relevanten Daten, einschließlich `source = whats_app`.
3. Löst eine Antwort aus, mit der Sie automatisierte Campaigns einrichten können, um auf die Bestellung zu reagieren.

Das `ecommerce.cart_update` E-Commerce-Event erscheint erst in Braze, nachdem ein Event gesendet wurde. Dies kann durch das Generieren einer Test-Produktnachricht aus Braze und das Absenden eines Warenkorb-Events erfolgen.
Das Warenkorb-Event enthält:

- **Warenkorb-ID:** Eindeutiger Bezeichner für den Warenkorb
- **Produkte:** Liste der Artikel mit Produkt-IDs, Mengen und Preisen
- **Gesamtwert:** Summe aller Artikel
- **Währung:** Die Währung des Warenkorbs
- **Quelle:** Gekennzeichnet als „whats_app“
- **Metadaten:** Zusätzliche Daten wie Katalog-ID und Nachrichtentext

Weitere Informationen zu Braze-Warenkorb-Events finden Sie unter [Typen empfohlener E-Commerce-Events]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events).

### Eine getriggerte Antwort einrichten {#setting-up-a-triggered-response}

1. Erstellen Sie einen angepassten Event-Trigger für `ecommerce.cart_updated`.
2. Fügen Sie einen Eigenschaftsfilter für `source = "whats_app"` hinzu.

![Canvas-Schritt für einen angepassten Event-Trigger „ecommerce.cart_updated“ mit der grundlegenden Eigenschaft „source“ gleich „whats_app“.]({% image_buster /assets/img/whatsapp/product_message_canvas_step.png %})

{: start="3"}
3. Konfigurieren Sie Folgeaktionen basierend auf den Warenkorbdaten.

### Empfohlene Checkout-Implementierungen {#recommended-checkout-implementations}

{% tabs local %}
{% tab Einfache Liquid-basierte Warenkorb-Links %}

Verwenden Sie Liquid, um Warenkorb-URLs direkt in Ihrer Antwortnachricht zu erstellen. Dies ist am besten geeignet, wenn Sie konsistente Produkt-IDs zwischen WhatsApp und Ihrer E-Commerce-Plattform haben.

#### Liquid-Beispiel {#example-liquid}

{% raw %}
```liquid
{% assign cart_link = "http://alejandro-test-new.myshopify.com/cart/" %}
{% for product in event_properties.products %}
 {% assign variant_id = product.product_id %}
 {% assign quantity = product.quantity %}
 {% if forloop.first %}
   {% assign cart_link = cart_link | append: variant_id | append: ":" | append: quantity %}
 {% else %}
   {% assign cart_link = cart_link | append: "," | append: variant_id | append: ":" | append: quantity %}
 {% endif %}
{% endfor %}
{{ cart_link }}
```
{% endraw %}

#### Einrichtung {#setup}

1. Erstellen Sie eine WhatsApp-Antwortnachricht-Campaign mit dem Trigger eines `ecommerce.cart_update` E-Commerce-Events.
2. Erstellen Sie eine Folgenachricht mit der Warenkorb-URL.
3. Erstellen Sie Ihre Warenkorb-URL mit Liquid. Wenn Sie Shopify verwenden, können Sie mit dem obigen Liquid-Beispiel einen [Warenkorb-Permalink erstellen](https://shopify.dev/docs/apps/build/checkout/create-cart-permalinks).

![Diagramm, das den Checkout-Workflow für einen Liquid-generierten Warenkorb zeigt: Meta sendet eine Bestellungsempfangsnachricht an Braze, das einen aktionsbasierten Trigger auslöst und dann eine Nachricht mit einem Warenkorb-Link erstellt, die dann als WhatsApp-Nachricht gesendet wird.]({% image_buster /assets/img/whatsapp/liquid_generated_cart_link_checkout.png %})

{% endtab %}
{% tab Connected Content %}

Führen Sie einen API-Aufruf an Ihr E-Commerce-System durch, um eine personalisierte Checkout-URL zu generieren. Dies ist am besten geeignet, wenn Sie eine dynamische Warenkorb-URL-Generierung oder komplexe Produktzuordnungen benötigen.

#### Einrichtung

1. Erstellen Sie eine Webhook-Campaign oder einen Canvas-Schritt, der durch das [`ecommerce.cart_update`]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events?tab=ecommerce.cart_updated) E-Commerce-Event getriggert wird und die Warenkorbdaten an Ihr E-Commerce-System sendet.
2. Erstellen Sie eine WhatsApp-Campaign oder einen Canvas-Nachrichtenschritt, der durch dasselbe E-Commerce-Event getriggert wird, um eine WhatsApp-Antwortnachricht mit der Warenkorb-URL an die Nutzer:innen zu senden. Folgen Sie den Anweisungen in der nachfolgenden Antwortnachricht zur Verwendung von [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content).

![Diagramm, das den Checkout-Workflow für einen Connected-Content-Aufruf zeigt: Meta sendet eine Bestellungsempfangsnachricht an Braze, das Hin-und-Her-Aufrufe mit einer E-Commerce-Plattform durchführt und dann eine WhatsApp-Nachricht sendet.]({% image_buster /assets/img/whatsapp/connected_content_checkout.png %})

{% endtab %}
{% tab Webhooks und angepasste Events %}

Verwenden Sie Webhooks, um Warenkorbdaten an Ihr System zu senden, und lösen Sie dann Folgenachrichten über angepasste Events aus. Dies ist am besten geeignet für komplexe Integrationen, die eine umfangreiche Warenkorbverarbeitung oder mehrstufige Workflows erfordern.

#### Einrichtung

Erstellen Sie eine Webhook-Campaign oder einen Canvas-Schritt, der durch das `ecommerce.cart_update` E-Commerce-Event getriggert wird und die Warenkorbdaten an Ihr E-Commerce-System sendet. Ihre API wird dann:
1. Warenkorbdaten empfangen
2. Einen Warenkorb in Ihrem System erstellen
3. Die Checkout-URL generieren
4. Ein `checkout_started`-Event an Braze senden, das Ihre WhatsApp-Nachricht mit dem Checkout-Link auslöst

![Diagramm, das den Checkout-Workflow für Webhooks und angepasste Events zeigt: Meta sendet eine Bestellungsempfangsnachricht an Braze, das Hin-und-Her-Aufrufe mit einer E-Commerce-Plattform durchführt und dann eine WhatsApp-Nachricht mit der Warenkorb-URL sendet.]({% image_buster /assets/img/whatsapp/webhooks_custom_events_checkout.png %})

{% endtab %}
{% endtabs %}

## Testen und Validierung {#testing-and-validation}

### Anforderungen für Testnachrichten {#test-message-requirements}

Die Warenkorbfunktionalität wird zwischen Testnachrichten übernommen, die Verarbeitung des eingehenden Ergebnisses jedoch nicht.

### Nachrichtenvorschau {#message-preview}

- Produktbilder und -details werden aus Ihrem Meta-Katalog abgerufen.
- Die interaktive Vorschau zeigt Platzhalter an, bis die Integration abgeschlossen ist.

### Fehlercodes {#error-codes}

- Wenn eine Produkt-ID nicht im Katalog existiert, erhalten Sie den Fehler `product not found for product_retailer_id, fake-product-id, in catalog_id, 1903196950214359`.
- Wenn ein Katalog vom WABA getrennt ist, erhalten Sie den Fehler `Check if catalog is linked to the WhatsApp Business Account and the catalog is enabled in the WhatsApp Commerce Settings`.