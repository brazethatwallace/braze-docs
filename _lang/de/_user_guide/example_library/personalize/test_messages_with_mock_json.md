---
nav_title: Nachrichten mit Mock-JSON testen
article_title: Nachrichten mit Mock-JSON in der Vorschau testen
page_order: 1
page_type: reference
description: "Verwenden Sie Liquid capture und json_parse, um Connected-Content- oder Entry-Style-JSON im Nachrichten-Editor in der Vorschau zu simulieren, ohne eine Campaign zu starten oder Testnachrichten zu senden."
---

# Nachrichten mit Mock-JSON in der Vorschau testen {#test-messages-with-mock-json-in-preview}

> Simulieren Sie API- oder Entry-Style-JSON in Ihrer Nachricht mit `capture` und `json_parse`, um Liquid und Layout in der Vorschau des Nachrichten-Editors zu validieren, bevor Sie eine Campaign starten, ein Canvas triggern oder Connected Content live aufrufen.

## Über dieses Beispiel {#about-this-example}

Flash & Thread, eine Einzelhandelsmarke für Bekleidung, erstellt Nachrichten, die von Connected-Content-Antworten, Canvas-Kontextvariablen oder Array-of-Objects-Profildaten abhängen. Echte API-Aufrufe auszulösen oder Campaigns für jede Iteration zu starten, verlangsamt die Entwicklung.

Dieses Muster bettet ein Mock-JSON-Payload in den Nachrichtentext ein, speichert es mit `capture` und parst es dann mit `json_parse`, sodass Liquid strukturierte Felder im Bereich **Vorschau** referenzieren kann – ohne einen Live-Connected-Content-Aufruf, einen API-getriggerten Canvas-Entry oder einen Testversand.

Verwenden Sie dies während der Nachrichtenentwicklung. Es ersetzt keine End-to-End-Tests mit echten Triggern, Testversendungen oder [Vorschau von Nutzerpfaden]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths) in Canvas.

## Hinweise {#considerations}

- Dieser Ansatz unterstützt die Vorschau im Nachrichten-Editor während der Entwicklung. Führen Sie Testversendungen und Live-Pfad-Prüfungen durch, bevor Sie an Kund:innen senden.
- Ein `capture`-Block allein speichert JSON als String. Referenzieren Sie Felder erst, nachdem Sie **`json_parse`** angewendet haben – andernfalls kann die Vorschauausgabe leer sein.
- Mock-JSON muss gültig sein. Ungültiges JSON führt dazu, dass `json_parse` fehlschlägt oder unerwartete Strukturen zurückgibt.
- Entfernen oder ersetzen Sie Mock-Blöcke vor dem Launch, oder schützen Sie Ihr Produktions-Liquid so, dass Mock-Daten nur in der Vorschau verwendet werden (zum Beispiel mit einem Kommentar-Flag, das Sie vor dem Go-live löschen).
- Die Liquid-Snippets in diesem Artikel sind Beispiele. Testen Sie sie in Ihren Kanälen und mit Ihren tatsächlichen Payload-Strukturen.
- Für Connected Content in der Produktion entfernen Sie den Mock-Block und verwenden Sie Ihren Live-URL-Tag. Siehe [Einen API-Aufruf durchführen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call).

## Einrichtung {#setup}

Dieses Beispiel simuliert eine Connected-Content-ähnliche Produktlisten-Antwort für eine E-Mail, die über `listings` iteriert.

### Schritt 1: Mock-JSON in der Nachricht erfassen {#step-1-capture-mock-json-in-the-message}

Verwenden Sie `capture`, um den JSON-String zu speichern. Verwenden Sie gültige JSON-Syntax innerhalb des Blocks (doppelte Anführungszeichen für Schlüssel und String-Werte).

{% raw %}
```liquid
{% capture mock_response %}
{
  "success": true,
  "listings": [
    {
      "id": 45731,
      "name": "Summit Trail Jacket",
      "image_url": "https://example.com/images/trail-jacket.png",
      "price": {
        "actual": "89.00",
        "currency": "USD"
      },
      "link": "https://example.com/products/trail-jacket",
      "product_category": "Outerwear",
      "properties": {
        "size": "L",
        "colour": "Navy",
        "limited_edition": false
      },
      "out_of_stock": false
    }
  ]
}
{% endcapture %}
```
{% endraw %}

### Schritt 2: JSON mit json_parse parsen {#step-2-parse-json-with-json_parse}

Weisen Sie die geparste Struktur einer Variablen zu, die Sie im Rest der Nachricht referenzieren.

{% raw %}
```liquid
{% assign response_json = mock_response | json_parse %}
```
{% endraw %}

Ohne `json_parse` gibt die Punkt-Notation auf dem erfassten String (zum Beispiel {% raw %}`{{ mock_response.listings }}`{% endraw %}) in der Vorschau typischerweise nichts aus.

### Schritt 3: Geparste Felder in Liquid referenzieren {#step-3-reference-parsed-fields-in-liquid}

Iterieren Sie über das geparste Array und rendern Sie Felder so, wie Sie es bei einer Live-API-Antwort tun würden.

{% raw %}
```liquid
{% for listing in response_json.listings %}
{{ listing.name }} — {{ listing.price.actual }} {{ listing.price.currency }}
{% endfor %}
```
{% endraw %}

Gehen Sie zum Bereich **Vorschau** im Nachrichten-Editor und überprüfen Sie, ob die Felder korrekt gerendert werden.

### Schritt 4: Dasselbe Muster auf andere JSON-Strukturen anwenden {#step-4-apply-the-same-pattern-to-other-json-shapes}

Verwenden Sie denselben `capture`- und `json_parse`-Ablauf, um Folgendes zu simulieren:

| Daten, die Sie testen möchten | Mock-JSON-Struktur |
| --- | --- |
| Canvas-Kontextvariablen | Objekt mit den Eigenschaftsschlüsseln, die Ihre Nachricht erwartet |
| Array of Objects in einem Profil | JSON-Array von Objekten mit denselben Schlüsseln wie Ihr angepasstes Attribut |
| Connected-Content-Antwort | Beispiel-API-JSON, gespeichert aus einem früheren erfolgreichen Aufruf |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Zu testende Daten und JSON-Struktur" }

Ersetzen Sie Mock-Variablen durch Produktions-Liquid (Canvas-Kontextvariablen, angepasste Attribute oder Connected-Content-Tags), bevor Sie launchen.

## Verwandte Artikel {#related-articles}

- [Testnachrichten senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages)
- [Nutzerpfade in Canvas in der Vorschau anzeigen]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths)
- [Erweiterte Liquid-Filter (`json_parse`)]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters)
- [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)
- [Array of Objects]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects)
- [Kontextvariablen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables)