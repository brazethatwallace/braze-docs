---
nav_title: "Katalogauswahlobjekt"
article_title: API-Katalog-Auswahlobjekt
page_order: 12
page_type: reference
description: "Dieser Referenzartikel erläutert die verschiedenen Komponenten des Katalogauswahlobjekts."
tool: Catalogs

---

# Katalogauswahlobjekt {#catalog-selection-object}

> Beim Erstellen einer Katalogauswahl können Sie ein Auswahlobjekt bereitstellen, um die Filter-, Sortier- und Einschränkungskriterien für die aus Ihrem Katalog zurückgegebenen Artikel zu definieren.

Mit dem `selection`-Objekt können Sie festlegen, welche Artikel aus Ihrem Katalog anhand von Filtern in die Auswahl aufgenommen werden sollen, wie sie sortiert werden sollen und wie viele Ergebnisse zurückgegeben werden sollen. Verwenden Sie dieses Objekt, wenn Sie Katalogauswahlen über die API erstellen.

## Objektkörper {#object-body}

```json
{
  "selection": {
    "name": "Sale",
    "description": "Sales Collection",
    "external_id": "12345678",
    "source": "Shopify",
    "filters": [
      {
        "field": "collection",
        "operator": "includes value",
        "value": "Best Seller"
      },
      {
        "field": "collection",
        "operator": "does not include value",
        "value": "Sale"
      }
    ],
    "results_limit": 5,
    "sort_field": "id",
    "sort_order": "asc"
  }
}
```

## Objektdetails {#object-details}

| Schlüssel | Erforderlich | Datentyp | Beschreibung |
| --- | -------- | --------- | ----------- |
| `name` | Erforderlich | String | Der Name der Katalogauswahl. |
| `description` | Optional | String | Eine Beschreibung der Katalogauswahl. |
| `external_id` | Optional | String | Ein eindeutiger Bezeichner für die Auswahl. |
| `source` | Optional | String | Die Quelle der Katalogdaten. Für Shopify-Kataloge setzen Sie diesen Wert auf `"Shopify"`. Akzeptierte Werte sind `"Shopify"` und `"Braze"`. |
| `filters` | Erforderlich | Array von Objekten | Ein Array von Filterobjekten, die auf die Katalogartikel angewendet werden. Sie können bis zu zehn Filter pro Anfrage angeben. Wenn ein leeres Filter-Array übergeben wird, werden alle Artikel aus dem Katalog einbezogen. |
| `results_limit` | Erforderlich | Integer | Die maximale Anzahl der zurückzugebenden Ergebnisse. Muss eine Zahl zwischen 1 und 50 sein. |
| `sort_field` | Optional | String | Das Feld, nach dem die Ergebnisse sortiert werden sollen. Dieses muss zusammen mit `sort_order` angegeben werden. Wenn weder `sort_field` noch `sort_order` vorhanden sind, werden die Ergebnisse in zufälliger Reihenfolge zurückgegeben. |
| `sort_order` | Optional | String | Die Sortierreihenfolge der Ergebnisse. Akzeptierte Werte sind `"asc"` (aufsteigend) oder `"desc"` (absteigend). Dieses muss zusammen mit `sort_field` angegeben werden. Wenn weder `sort_field` noch `sort_order` vorhanden sind, werden die Ergebnisse in zufälliger Reihenfolge zurückgegeben. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Objektdetails" }

### Filterobjekt {#filter-object}

Jedes Filterobjekt im `filters`-Array enthält die in der folgenden Tabelle beschriebenen Felder.

| Schlüssel | Erforderlich | Datentyp | Beschreibung |
| --- | -------- | ------------------------------------------- | ----------- |
| `field` | Erforderlich | String | Das Katalogfeld, nach dem gefiltert werden soll. |
| `operator` | Erforderlich | String | Der Vergleichsoperator, der zum Filtern verwendet wird. Beispiele sind `"includes value"` und `"does not include value"`. |
| `value` | Erforderlich | Variiert (String, Zahl, Boolean, Zeit) | Der Wert, mit dem verglichen wird. Dieser muss dem Datentyp des zugrunde liegenden Katalogfelds entsprechen (z. B. String, Zahl, Boolean, Zeit). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Filterobjekt" }

{% alert note %}
Die API unterstützt maximal zehn Filter pro Auswahlanfrage. Filter werden in der Reihenfolge angewendet, in der sie im Array erscheinen.
{% endalert %}