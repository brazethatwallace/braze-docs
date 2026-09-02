---
nav_title: E-Commerce-Umsatz-Dashboard
article_title: E-Commerce-Umsatz-Dashboard
alias: "/ecommerce_revenue_dashboard/"
page_order: 1
description: "Dieser Artikel bietet eine Übersicht über das Dashboard „E-Commerce-Umsatz – Last-Touch-Attribution“."
---

# E-Commerce-Umsatz-Dashboard {#ecommerce-revenue-dashboard}

> Das Dashboard **E-Commerce-Umsatz – Last-Touch-Attribution** erfasst den per Last-Touch-Attribution zugeordneten Umsatz für Campaigns und Canvase mithilfe von [empfohlenen E-Commerce-Events]({{site.baseurl}}/ecommerce_events). Nutzen Sie dieses Dashboard, um zu verstehen, welche Nachrichten Umsatz generieren, und um die gesamte E-Commerce-Performance im Zeitverlauf zu überwachen.

{% alert note %}
Wenn Sie den neuen [Shopify-Konnektor]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores?tab=shopify%20connector) verwenden, stehen empfohlene E-Commerce-Events automatisch über die Integration zur Verfügung. Andernfalls müssen diese Events implementiert werden, bevor Daten in diesem Dashboard angezeigt werden.
{% endalert %}

Um Ihr E-Commerce-Umsatz-Dashboard aufzurufen, gehen Sie zu **Analytics** > **Dashboard Builder** und wählen Sie **eCommerce Revenue - Last Touch Attribution** aus. Dieses Dashboard zeigt den Umsatz, der der letzten Campaign oder dem letzten Canvas zugeordnet wird, mit der bzw. dem ein:e Nutzer:in vor einer Bestellung interagiert hat – innerhalb des ausgewählten Conversion-Fensters.

![Dashboard „E-Commerce-Umsatz – Last-Touch-Attribution“ mit Statistiken für E-Commerce-Umsatz, tägliche Bestellungen und durchschnittlichen täglichen E-Commerce-Umsatz sowie einem Chart „E-Commerce-Umsatz im Zeitverlauf“.]({% image_buster /assets/img/ecommerce/ecommerce_revenue_dashboard.png %})

## Verfügbare Metriken {#available-metrics}

| Metrik | Definition |
| --- | --- |
| E-Commerce-Umsatz | Gesamter per Last-Touch-Attribution zugeordneter Umsatz basierend auf dem ausgewählten Datumsbereich und Conversion-Fenster. |
| Tägliche Bestellungen | Die durchschnittliche Anzahl einzelner Bestellungen pro Tag. |
| Durchschnittlicher täglicher E-Commerce-Umsatz | Durchschnittlicher zugeordneter Umsatz pro Tag für den ausgewählten Zeitraum. |
| E-Commerce-Umsatz im Zeitverlauf | Eine Zeitreihe des zugeordneten Umsatzes im ausgewählten Datumsbereich. |
| E-Commerce-Umsatz nach Campaign | Zugeordneter Umsatz aufgeschlüsselt nach Campaign. |
| E-Commerce-Umsatz nach Canvas | Zugeordneter Umsatz aufgeschlüsselt nach Canvas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Verfügbare Metriken" }

![Charts „E-Commerce-Umsatz nach Campaign“ und „E-Commerce-Umsatz nach Canvas“.]({% image_buster /assets/img/ecommerce/ecommerce_revenue_charts.png %})

## Attributionsmodell {#attribution-model}

Das Dashboard **E-Commerce-Umsatz – Last-Touch-Attribution** verwendet Last-Touch-Attribution. Das bedeutet, dass der Umsatz der letzten Braze-Campaign oder dem letzten Canvas zugeordnet wird, mit der bzw. dem ein:e Nutzer:in vor einer Bestellung interagiert hat.

Die folgenden Nachrichteninteraktionen gelten als Touch-Events für die Attribution:

- E-Mail-Klick
- Push-Öffnung
- Content-Card-Klick
- In-App-Nachricht-Klick
- Kurzmitteilungsdienst or SMS-Kurzlink-Klick
- WhatsApp-Kurzlink-Klick

{% alert important %}
Nachrichteninteraktionen müssen innerhalb des ausgewählten Conversion-Fensters stattgefunden haben. Bestellungen ohne eine qualifizierende Nachrichteninteraktion innerhalb des Conversion-Fensters werden nicht zugeordnet.
{% endalert %}

## Enthaltene Daten {#included-data}

Das Dashboard **E-Commerce-Umsatz – Last-Touch-Attribution** bezieht Daten aus empfohlenen E-Commerce-Events:

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_refunded`
- `ecommerce.order_cancelled`

{% alert note %}
Damit Daten im Dashboard **E-Commerce-Umsatz – Last-Touch-Attribution** angezeigt werden, müssen `total_value`, `product.price` und `product.quantity` für das Event `ecommerce.order_placed` den Wert `0` oder höher haben.
{% endalert %}

Umsatz und Bestellanzahlen verwenden standardisierte Braze-Berechnungen.

| Metrik | Berechnung |
| --- | --- |
| Gesamtumsatz | Summe der Bestellwerte − Summe der Erstattungswerte |
| Gesamtbestellungen | Einzelne aufgegebene Bestellungen − Einzelne stornierte Bestellungen |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Enthaltene Daten" }

### Ausgeschlossene Daten {#excluded-data}

Käufe, die über das veraltete Kauf-Event erfasst wurden, sind nicht enthalten. Das Dashboard **E-Commerce-Umsatz – Last-Touch-Attribution** unterstützt derzeit keine Features, die an veraltete Kauf-Events gebunden sind, wie z. B. LTV or Lifetime-Value oder Umsatzberichte innerhalb von Campaigns oder Canvase.

## Währungsbehandlung {#currency-handling}

Alle Umsätze werden in USD angezeigt. Nicht-USD-Währungen werden anhand des Wechselkurses am Tag der Event-Erfassung in USD umgerechnet. Um eine Umrechnung zu vermeiden, setzen Sie die Währung beim Senden von Events fest auf `USD`.