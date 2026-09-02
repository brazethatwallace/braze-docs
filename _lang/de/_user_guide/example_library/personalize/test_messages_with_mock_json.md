---
nav_title: Nachrichten mit Mock-JSON testen
article_title: Nachrichten mit Mock-JSON in der Vorschau testen
page_order: 1
page_type: reference
description: "Verwenden Sie Liquid capture und json_parse, um Connected-Content- oder Entry-Style-JSON im Nachrichten-Editor in der Vorschau zu simulieren, ohne eine Campaign zu starten oder Testnachrichten zu senden."
---

# Nachrichten mit Mock-JSON in der Vorschau testen {#test-messages-with-mock-json-in-preview}

> Simulieren Sie API- oder Entry-Style-JSON in Ihrer Nachricht mit `capture` und `json_parse`, um Liquid und Layout in der Vorschau des Nachrichten-Editors zu validieren, bevor Sie eine Campaign starten, ein Canvas Trigger or triggern or triggern oder Connected Content live aufrufen.

## Über dieses Beispiel {#about-this-example}

Flash & Thread, eine fiktive Bekleidungsmarke im Einzelhandel, erstellt Nachrichten, die auf Connected-Content-Antworten, Canvas-Kontextvariablen oder Array-of-Objects-Profildaten basieren. Echte API-Aufrufe auszulösen oder Campaigns für jede Iteration zu starten, verlangsamt die Entwicklung.

Dieses Muster bettet ein simuliertes JSON-Payload in den Nachrichtentext ein, speichert es mit `capture` und parst es anschließend mit `json_parse`, sodass Liquid im **Vorschau**-Bereich auf strukturierte Felder zugreifen kann – ohne einen Live-Connected-Content-Aufruf, einen API-getriggerten Canvas-Entry oder einen Testversand.

Verwenden Sie dieses Muster während der Nachrichtenentwicklung. Es ersetzt keine End-to-End-Tests mit echten Trigger or triggern or triggern, Testversendungen oder [Vorschau von Nutzerpfaden]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths) in Canvas.

## Hinweise {#considerations}

- Dieser Ansatz unterstützt die Vorschau im Nachrichten-Editor während der Entwicklung. Führen Sie Testsendungen und Live-Pfad-Prüfungen durch, bevor Sie den Versand an Kund:innen starten.
- Ein `capture`-Block allein speichert JSON als String. Referenzieren Sie Felder erst, nachdem Sie **`json_parse`** angewendet haben – andernfalls kann die Vorschauausgabe leer sein.
- Mock-JSON muss gültig sein. Ungültiges JSON führt dazu, dass `json_parse` fehlschlägt oder unerwartete Strukturen zurückgibt.
- Entfernen oder ersetzen Sie Mock-Blöcke vor dem Launch, oder schützen Sie Ihr Produktions-Liquid so, dass Mock-Daten nur in der Vorschau verwendet werden (zum Beispiel mit einem Kommentar-Flag, das Sie vor dem Go-live löschen).
- Die Liquid-Snippets in diesem Artikel sind Beispiele. Testen Sie sie in Ihren Kanälen und mit Ihren tatsächlichen Payload-Strukturen.
- Entfernen Sie für Connected-Content in der Produktion den Mock-Block und verwenden Sie Ihren Live-URL-Tag. Siehe [Einen API-Aufruf durchführen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call).

## Einrichtung {#setup}

Dieses Beispiel simuliert eine Connected-Content-ähnliche Produktlisten-Antwort für eine E-Mail, die über `listings` iteriert.

### Schritt 1: Mock-JSON in der Nachricht erfassen {#step-1-capture-mock-json-in-the-message}

Verwenden Sie `capture`, um den JSON-String zu speichern. Verwenden Sie innerhalb des Blocks gültige JSON-Syntax (doppelte Anführungszeichen für Schlüssel und String-Werte).

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

Weisen Sie die geparste Struktur einer Variablen zu, auf die Sie im Representational State Transfer der Nachricht verweisen.

{% raw %}
```liquid
{% assign response_json = mock_response | json_parse %}
```
{% endraw %}

Ohne `json_parse` gibt die Punkt-Notation auf dem erfassten String (zum Beispiel {% raw %}`{{ mock_response.listings }}`{% endraw %}) in der Vorschau in der Regel nichts aus.

### Schritt 3: Geparste Felder in Liquid referenzieren {#step-3-reference-parsed-fields-in-liquid}

Iterieren Sie über das geparste Array und rendern Sie Felder so, wie Sie es bei einer Live-API-Antwort tun würden.

{% raw %}
```liquid
{% for listing in response_json.listings %}
{{ listing.name }} — {{ listing.price.actual }} {{ listing.price.currency }}
{% endfor %}
```
{% endraw %}

Gehen Sie zum Abschnitt **Vorschau** im Nachrichten-Editor und überprüfen Sie, ob die Felder korrekt gerendert werden.

### Schritt 4: Dasselbe Muster auf andere JSON-Strukturen anwenden {#step-4-apply-the-same-pattern-to-other-json-shapes}

Verwenden Sie denselben `capture`- + `json_parse`-Ablauf, um Folgendes zu simulieren:

| Daten, die Sie testen möchten | Mock-JSON-Struktur |
| --- | --- |
| Canvas-Kontextvariablen | Objekt mit den Eigenschaftsschlüsseln, die Ihre Nachricht erwartet |
| Array von Objekten in einem Profil | JSON-Array von Objekten mit denselben Schlüsseln wie Ihr angepasstes Attribut |
| Connected-Content-Antwort | Beispiel-API-JSON, das aus einem früheren erfolgreichen Aufruf gespeichert wurde |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Daten, die Sie testen möchten, und JSON-Struktur" }

Ersetzen Sie Mock-Variablen durch produktive Liquid-Ausdrücke (Canvas-Kontextvariablen, angepasste Attribute oder Connected-Content-Tags), bevor Sie die Nachricht starten.

## Verwandte Artikel {#related-articles}

- [Testnachrichten senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages)
- [Vorschau von Nutzerpfaden in Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths)
- [Erweiterte Liquid-Filter (`json_parse`)]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters)
- [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)
- [Array von Objekten]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects)
- [Kontextvariablen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables)