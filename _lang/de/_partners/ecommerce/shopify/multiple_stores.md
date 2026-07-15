---
nav_title: Verbinden mehrerer Shops
article_title: Shopify Unterstützung mehrerer Shops
alias: /shopify_connecting_multiple_stores/
page_order: 6
description: "Dieser Referenzartikel beschreibt, wie Sie mehrere Shopify Shops mit einem einzigen Workspace verbinden und konfigurieren können."
---

# Mehrere Shopify Shops verbinden {#connect-multiple-shopify-stores}

> Verbinden Sie mehrere Shopify Shop-Domains mit einem einzigen Workspace, um einen ganzheitlichen Überblick über Ihre Kund:innen in allen Märkten zu erhalten. Erstellen und starten Sie Automatisierungsprogramme und Journeys in einem einzigen Workspace, ohne doppelte Arbeit in den regionalen Shops.

{% alert important %}
Dieses Feature unterstützt nicht Shopify Markets oder Markets Pro. {% multi_lang_include product_feedback_cta.md context="gap" feature="Shopify Markets or Markets Pro support" %}
{% endalert %}

## Anforderungen {#requirements}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Einen Shopify Shop einrichten | Stellen Sie sicher, dass Sie bereits [mindestens einen Shopify Shop mit Braze eingerichtet]({{site.baseurl}}/shopify_overview) haben. |
| Eindeutige Shopify Storefront-Domains für jede Region | Die Unterstützung mehrerer Shops ist für die Verwendung eindeutiger Shopify Shop-Domains für verschiedene regionale Storefronts gedacht. <br><br>Wenn Sie mehrere Untermarken mit Braze verbinden möchten, empfehlen wir, für jede Untermarke einen eigenen Workspace zu erstellen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anforderungen" }

## Einen zusätzlichen Shop verbinden {#connecting-an-additional-store}
Nachdem Sie die Braze App in Ihrem Shopify Shop installiert und Ihren ersten Shop eingerichtet haben, wählen Sie **+ Connect New Store**.

![Der Button „+ Connect New Store“ auf der Shopify Integrationsseite.]({% image_buster /assets/img/shopify/begin_setup_button.png %}){: style="max-width:80%;"}

Für Ihren zusätzlichen regionalen Shopify Shop wählen Sie **Begin setup**.

![Der Bereich „Integration settings“ mit einem Button „Begin setup“.]({% image_buster /assets/img/shopify/multiple_stores.png %}){: style="max-width:80%;"}

Wie bei Ihrer ersten Shopify Shop-Integration können Sie zwischen einer Standard- oder angepassten Einrichtung wählen.

![Bereich „Enable the Braze SDKs“ mit Optionen zur Implementierung des Braze Web SDK mit der Standard- oder angepassten Einrichtung.]({% image_buster /assets/img/shopify/standard_or_custom.png %}){: style="max-width:80%;"}

Wählen Sie die Option, die Ihren Bedürfnissen am besten entspricht:

{% multi_lang_include partners/shopify.md section='Integration Tabs' %}

Um die einzelnen Shop-Integrationen anzuzeigen und erweiterte Einstellungen zu konfigurieren, wählen Sie einen Shop im Dropdown-Menü aus.

![„Integration settings“ mit einem Dropdown-Menü zum Auswählen eines Shopify Shops.]({% image_buster /assets/img/shopify/store_dropdown_menu.png %})

## Synchronisierung von Nutzer:innen über verschiedene Shops {#syncing-users-across-stores}

### Shopify-Alias

Wenn Sie mehrere Shops verbinden, erhalten synchronisierte Shopify-Nutzer:innen, die sich angemeldet oder eine Bestellung aufgegeben haben, einen neuen Alias im Format: {% raw %}`shopify_customer_id_{{storename}}`{% endraw %}.

### Externe Braze-ID {#braze-external-id}

Für Ihre externe Braze-ID können Sie aus den folgenden Optionen wählen:

| Option | Beschreibung |
|------|-----------|
| Shopify-Kunden-ID | Wenn Sie die Shopify-Kunden-ID als externe Braze-ID verwenden, generiert jeder Shop eine eindeutige Kunden-ID für jede:n Nutzer:in. Das bedeutet, dass Nutzer:innen, die mit mehreren Shops interagieren, separate Profile in Braze haben. |
| E-Mail, gehashte E-Mail oder angepasste externe ID | Wenn Sie die Typen E-Mail, gehashte E-Mail oder angepasste externe ID verwenden, werden die Profile von Nutzer:innen, die sich in mehreren Shops engagieren, in einem einzigen konsolidierten Profil zusammengeführt, wenn sie sich anmelden oder eine Bestellung aufgeben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Externe Braze-ID" }

### Zusammengeführte Felder {#merged-fields}

Wenn ein Nutzerprofil synchronisiert wird, werden die folgenden Felder zusammengeführt. Ausführliche Informationen zum Zusammenführungsverhalten finden Sie unter [Zusammenführungsverhalten]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior).

- Geräteinformationen
- Gesamtzahl der Sitzungen (kombiniert aus beiden Profilen)
- Angepasste Event- und Kaufdaten
- Angepasste Event-Eigenschaften für die Segmentierung (z. B. „X Mal in Y Tagen“, wobei X ≤ 50 und Y ≤ 30)
- Event-Anzahl (kombiniert aus beiden Profilen)
- Datum des ersten und letzten Events (Braze wählt das früheste und jüngste Datum aus)
- Daten zur Campaign-Interaktion (jüngste Datumsfelder)
- Workflow-Zusammenfassungen (jüngste Datumsfelder)
- Nachrichten- und Engagement-Verlauf
- Abo-Gruppen

### Sammeln von Abonnent:innen (optional) {#collecting-subscribers-optional}

Sie können wählen, ob Sie Abonnent:innen direkt über Braze (in Ihren Shopify-Konnektor-Einstellungen) oder über API- und SDK-Alternativen, die Daten von Shopify synchronisieren, sammeln möchten.

{% tabs local %}
{% tab Shopify-Konnektor %}
Im Schritt **Manage users** Ihrer Shopify-Konnektor-Einstellungen können Sie Braze verwenden, um Opt-ins von E-Mail- und SMS-Abonnent:innen zu sammeln und sie in einer speziellen Abo-Gruppe zu organisieren:

1. Erstellen Sie für jeden Shop, den Sie verbinden, eine eindeutige Abo-Gruppe. So erhalten Sie genaue Daten darüber, woher die Abonnent:innen kommen.
2. Aktivieren Sie die Erfassung von E-Mail- und SMS-Abonnent:innen.
{% endtab %}

{% tab Braze API oder SDKs %}
Alternativ können Sie die Opt-in-Informationen für E-Mail- und SMS-Marketing direkt von Shopify über die Braze API oder SDKs synchronisieren.

| Option | Ressourcen |
|------|---------|
| API | - [Abo-Gruppen-Endpunkte]({{site.baseurl}}/api/endpoints/subscription_groups), um direkt zu ersetzen, was von der Integration unterstützt wird<br>- [`Users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track#set-subscription-groups) zum Festlegen der Abo-Gruppen-Daten oder des [globalen E-Mail-Abo-Status]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#subscription-states)<br>- [Braze Präferenzzentrum]({{site.baseurl}}/user_guide/channels/email/subscriptions) für angepasstere Marketing-Opt-in-Optionen |
| SDKs | - [`NotificationSubscriptionTypes`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#notificationsubscriptiontypes)<br>- [`addToSubscriptionGroup`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)<br>- [`removeFromSubscriptionGroup`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#removefromsubscriptiongroup)<br>- [`setEmailNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sammeln von Abonnent:innen (optional)" }
{% endtab %}
{% endtabs %}

## Shopify-Daten {#shopify-data}

### Synchronisierte Attribute {#synced-attributes}

Wenn Sie mehr als einen Shop verbinden, werden die folgenden Attribute mit dem neuesten Stand des Shopify-Profils synchronisiert:
- Vorname
- Nachname
- E-Mail
- Geschlecht
- Geburtsdatum
- Land
- Ort
- Letzte App-Nutzung
- Sprache
- Zeitzone
- Shopify-Tags
- Anzahl der Shopify-Bestellungen
- Shopify-Gesamtausgaben

### Unterstützte Events {#supported-events}

#### Empfohlene E-Commerce-Events {#ecommerce-recommended-events}

Wenn Sie mehrere Shops verbinden, enthalten eingehende empfohlene E-Commerce-Events eine Quell-Event-Eigenschaft. Diese Eigenschaft gibt an, von welcher Storefront-URL das Event stammt, sodass Sie diese Information zur Segmentierung oder zum Triggern bestimmter Anwendungsfälle verwenden können.

![Ein aktionsbasiertes Canvas mit einem Trigger zur Erfassung von Nutzer:innen, die das angepasste Event „ecommerce.order_placed“ ausführen.]({% image_buster /assets/img/shopify/ecommerce_order_placed.png %}){: style="max-width:80%;"}

Die unterstützten empfohlenen E-Commerce-Events innerhalb der Shopify-Integration sind:

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_cancelled`
- `ecommerce.order_refunded`

#### Angepasste Shopify-Events {#shopify-custom-events}

Eingehende angepasste Shopify-Events enthalten eine Event-Eigenschaft namens `shopify_storefront`. Diese Eigenschaft zeigt an, von welcher Storefront-URL das Event stammt, sodass Sie sie für die Segmentierung oder das Triggern von Anwendungsfällen nutzen können.

![Ein aktionsbasiertes Canvas mit einem Trigger zur Erfassung von Nutzer:innen, die das angepasste Event „shopify_paid_order“ ausführen.]({% image_buster /assets/img/shopify/shopify_paid_order.png %}){: style="max-width:80%;"}

Zu den unterstützten angepassten Shopify-Events gehören:

- `shopify_fulfilled_order`
- `shopify_partially_fulfilled_order`
- `shopify_paid_order`
- `shopify_account_login`

Eine vollständige Übersicht über alle Event-Payloads finden Sie unter [Shopify-Daten-Features]({{site.baseurl}}/shopify_data_features).

### Shopify-Produktsynchronisierung {#shopify-product-sync}

Wenn Sie jeden Shopify Shop in Braze verbinden und konfigurieren, können Sie optional die Shopify-Produktsynchronisierung als Teil der Integration aktivieren.

Wenn Sie die Produktsynchronisierung für jeden Shop aktivieren, nimmt Braze den Namen Ihres Shopify Shops in den Katalognamen auf. So können Sie Produkte aus verschiedenen Shops unterscheiden.

![Shopify-Kataloge mit ihrem Shopify-Shop-Namen.]({% image_buster /assets/img/shopify/catalog_store_name.png %})