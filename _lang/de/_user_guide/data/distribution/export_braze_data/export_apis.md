---
nav_title: Export-APIs
article_title: Export-APIs
page_order: 5
page_type: reference
description: "Dieser Referenzartikel hilft Ihnen bei der Entscheidung, wann Sie Export-APIs anstelle von CSV-Downloads aus dem Dashboard verwenden sollten."
platform: API

---

# Export-APIs {#export-apis}

> Diese Seite hilft Ihnen bei der Entscheidung, wann Sie Export-APIs anstelle von CSV-Downloads aus dem Dashboard verwenden sollten.

Die Braze-Export-APIs ermöglichen es Ihnen, Braze-Daten programmatisch als JSON zu exportieren. Details dazu, was Sie exportieren können, welche Voraussetzungen gelten und wie die Zustellung funktioniert, finden Sie unter [Export-Endpunkte]({{site.baseurl}}/api/endpoints/export).

## Wann Sie Export-APIs anstelle von CSV-Downloads verwenden sollten {#when-to-use-export-apis-instead-of-csv-downloads}

Die folgende Tabelle beschreibt gängige Szenarien, in denen die Verwendung der Export-API eine bessere Wahl als ein CSV-Download aus dem Dashboard ist.

| Szenario | Details |
| --- | --- |
| Ihr Export ist zu groß für das Dashboard | CSV-Exporte aus dem Dashboard sind auf 500.000 Zeilen begrenzt. Wenn Sie Daten zu einem Segment mit mehr als 500.000 Nutzer:innen exportieren, verwenden Sie die Export-API, die keine Begrenzung für die Exportmenge hat. |
| Sie möchten wiederkehrende Berichte automatisieren | Planen Sie API-Exporte über eine Integration, um Daten in regelmäßigen Abständen ohne manuelle Dashboard-Interaktion abzurufen. |
| Sie müssen Daten in externe Tools einspeisen | Rufen Sie Exportdaten direkt in BI-Tools, Data Warehouses oder andere Analytics-Plattformen ab. |
| Sie benötigen Daten, die nicht als CSV-Export im Dashboard verfügbar sind | Einige Datenkategorien, darunter KPIs, Umsatzreihen, Analytics für angepasste Events und Sitzungsdaten, sind nur über die API verfügbar. |
| Sie möchten programmatisch mit den Daten interagieren | Nutzen Sie die JSON-Ausgabe für angepasste Verarbeitung, Transformationen oder Integrationen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Wann Sie Export-APIs anstelle von CSV-Downloads verwenden sollten" }

{% alert tip %}
Hilfe zu CSV- und API-Exporten finden Sie unter [Fehlerbehebung bei Exporten]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}