---
nav_title: Einkäufe protokollieren
article_title: Käufe protokollieren für Windows Universal
platform: Windows Universal
page_order: 4
description: "Dieser Referenzartikel beschreibt, wie Sie Einkäufe auf der Windows Universal Plattform protokollieren können."
hidden: true
---

# Einkäufe protokollieren {#log-purchases}
{% multi_lang_include archive/windows_deprecation.md %}

Erfassen Sie In-App-Käufe, damit Sie Ihren Umsatz im Zeitverlauf und über verschiedene Umsatzquellen hinweg verfolgen und Ihre Nutzer:innen nach ihrem Lifetime-Value segmentieren können.

Braze unterstützt Einkäufe in mehreren Währungen. Einkäufe, die Sie in einer anderen Währung als dem USD melden, werden im Dashboard in USD auf der Grundlage des Wechselkurses an dem Tag, an dem sie gemeldet wurden, angezeigt.

Lesen Sie vor der Implementierung unbedingt die Beispiele für die Segmentierungsoptionen, die angepasste Events, angepasste Attribute und Kauf-Events bieten, in unserem Artikel über [Best Practices]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview#user-data-collection). Wir empfehlen Ihnen auch, sich mit unseren [Namenskonventionen für Events]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions) vertraut zu machen.

Um dieses Feature zu nutzen, fügen Sie diesen Methodenaufruf nach einem erfolgreichen Kauf in Ihrer App hinzu:

Käufe werden mit Hilfe des `EventLogger` protokolliert, einer Eigenschaft, die in IAppboy bereitgestellt wird. Um eine Referenz auf den `EventLogger` zu erhalten, rufen Sie `Appboy.SharedInstance.EventLogger` auf.

```csharp
bool LogPurchase(string productId, string currencyCode, decimal price)
```

## Käufe auf Bestellebene protokollieren {#log-purchases-at-the-order-level}
Wenn Sie Einkäufe auf der Bestellebene statt auf der Produktebene protokollieren möchten, können Sie den Bestellnamen oder die Bestellkategorie als `product_id` verwenden. Weitere Informationen finden Sie in unserer [Spezifikation für Kauf-Objekte]({{site.baseurl}}/api/objects_filters/purchase_object#naming-conventions).

## REST API

Sie können auch unsere REST API verwenden, um Einkäufe zu erfassen. Einzelheiten finden Sie in der Dokumentation zur [Nutzer:innen-API]({{site.baseurl}}/developer_guide/rest_api/user_data#user-data).