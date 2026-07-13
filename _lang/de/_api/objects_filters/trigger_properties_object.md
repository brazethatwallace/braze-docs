---
nav_title: "Trigger-Eigenschaften-Objekt"
article_title: API-Trigger-Eigenschaften-Objekt
page_order: 11
page_type: reference
description: "Dieser Referenzartikel erläutert die verschiedenen Komponenten des Trigger-Eigenschaften-Objekts."
tool: Campaigns

---

# Trigger-Eigenschaften-Objekt {#trigger-properties-object}

> Wenn Sie einen der Endpunkte für den Versand einer Campaign mit API-getriggerter Zustellung verwenden, können Sie eine Zuordnung von Schlüsseln und Werten bereitstellen, um Ihre Nachricht anzupassen.

Wenn Sie eine API-Anfrage stellen, die ein Objekt in `trigger_properties` enthält, können die Werte in diesem Objekt dann in Ihrem Nachrichten-Template unter dem Namensraum `api_trigger_properties` referenziert werden. Eine Anfrage mit folgendem Inhalt könnte zum Beispiel das Wort `"shoes"` zu einer Nachricht hinzufügen, indem Sie {% raw %}`{{api_trigger_properties.${product_name}}}`{% endraw %} einfügen.

Beachten Sie, dass Trigger-Eigenschaften zwar als Template in Nachrichten eingefügt werden können, aber standardmäßig nicht automatisch im Nutzerprofil gespeichert werden.

{% alert note %}
Das Objekt `trigger_properties` und die Syntax {% raw %}`api_trigger_properties.${product_name}`{% endraw %} werden nur in Campaigns unterstützt. Um Nachrichten mit Schlüsseln und Werten aus einer API-Trigger-Anfrage für Canvas anzupassen, verwenden Sie das [Canvas-Eingangs-Eigenschaften-Objekt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context). Das Objekt `trigger_properties` hat eine maximale Größe von 50 KB.
{% endalert %}

## Objektinhalt {#object-body}

```json
{
  "trigger_properties" : {
    "product_name" : "shoes",
    "product_price" : 79.99,
    "details" : {
      "color" : "red",
      "size" : {
        "numerical" : 10,
        "country" : "US"
      }
    },
    "related_skus": ["123", "456", "789"]
  }
}
```


