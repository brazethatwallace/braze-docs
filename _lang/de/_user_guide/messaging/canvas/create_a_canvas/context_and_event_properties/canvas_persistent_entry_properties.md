---
nav_title: Persistente Entry-Eigenschaften
article_title: Persistente Entry-Eigenschaften
alias: "/persistent_entry/"
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie persistente Entry-Eigenschaften in Ihrem Canvas verwenden können, um besser kuratierte Nachrichten zu senden und ein hochgradig verfeinertes Endnutzer:innen-Erlebnis zu schaffen."
tool: Canvas
page_order: 5
---

# Persistente Entry-Eigenschaften {#persistent-entry-properties}

> Wenn ein Canvas durch ein angepasstes Event, einen Kauf oder einen API-Aufruf getriggert wird, können Sie Metadaten aus dem API-Aufruf, dem angepassten Event oder dem Kauf-Event zur Personalisierung in jedem Schritt Ihres Canvas-Workflows verwenden. Sie können diese Eigenschaften nutzen, um besser kuratierte Nachrichten zu senden.

{% alert important %}
Persistente Entry-Eigenschaften sind ein Artefakt des ursprünglichen Canvas-Editors, daher gibt es veraltete Verweise auf Begriffe wie Canvas-Entry-Eigenschaften, die aus historischen Gründen bestehen bleiben. Für den aktuellen Canvas-Editor lesen Sie [Kontext- und Event-Eigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties).<br><br>Um persistente Entry-Eigenschaften im aktuellen Canvas-Editor zu verwenden, müssen Sie entweder einen neuen Canvas erstellen oder einen bestehenden in den aktuellen Editor [Klon or klonen]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases).
{% endalert %}

## Entry-Eigenschaften verwenden {#using-entry-properties}

Entry-Eigenschaften können in aktionsbasierten und API-getriggerten Canvase verwendet werden. Diese Entry-Eigenschaften werden definiert, wenn ein Canvas durch ein angepasstes Event, einen Kauf oder einen API-Aufruf getriggert wird. Weitere Informationen finden Sie in den folgenden Artikeln:

- [Canvas-Entry-Eigenschaften-Objekt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context)
- [Event-Eigenschaften-Objekt]({{site.baseurl}}/api/objects_filters/event_object)
- [Kauf-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object#purchase-product-id)

Eigenschaften, die von diesen Objekten übergeben werden, können über den Liquid-Tag `canvas_entry_properties` referenziert werden. Beispielsweise könnte eine Anfrage mit `"canvas_entry_properties": {"product_name": "shoes", "product_price": 79.99}` das Wort „shoes“ zu einer Nachricht hinzufügen, indem der Liquid-Code {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %} verwendet wird.

Wenn ein Canvas eine Nachricht mit dem Liquid-Tag `canvas_entry_properties` enthält, werden die mit diesen Eigenschaften verknüpften Werte für die Dauer der Journey der Nutzer:innen im Canvas gespeichert und gelöscht, wenn die Nutzer:innen das Canvas verlassen. Beachten Sie, dass Canvas-Entry-Eigenschaften nur zur Referenzierung in Liquid verfügbar sind. Um innerhalb des Canvas nach den Eigenschaften zu filtern, verwenden Sie stattdessen die [Event-Eigenschafts-Segmentierung]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects).

{% alert note %}
Das Canvas-Entry-Eigenschaften-Objekt hat eine maximale Größenbeschränkung von 50 KB.
{% endalert %}

## Canvas Update or aktualisieren or aktualisieren, um Entry-Eigenschaften zu verwenden {#updating-canvas-to-use-entry-properties}

Wenn ein aktives Canvas, das zuvor keine Nachrichten mit `canvas_entry_properties` enthielt, so bearbeitet wird, dass es `canvas_entry_properties` enthält, ist der Wert, der dieser Eigenschaft entspricht, für Nutzer:innen, die das Canvas betreten haben, bevor `canvas_entry_properties` zum Canvas hinzugefügt wurde, nicht verfügbar. Die Werte werden nur für Nutzer:innen gespeichert, die das Canvas nach der Änderung betreten.

Wenn Sie beispielsweise ein Canvas, das keine Entry-Eigenschaften verwendete, ursprünglich am 3. November gestartet und dann am 11. November eine neue Eigenschaft `product_name` zum Canvas hinzugefügt haben, werden Werte für `product_name` nur für Nutzer:innen gespeichert, die das Canvas ab dem 11. November betreten haben.

Falls eine Canvas-Entry-Eigenschaft null oder leer ist, können Sie Nachrichten mithilfe von Bedingungen abbrechen. Das folgende Code-Snippet ist ein Beispiel dafür, wie Sie Liquid verwenden können, um eine Nachricht abzubrechen.
{%raw%}
```
{% if canvas_entry_properties.${product_name} == blank %}
{% abort_message() %}
{% endif %}
```
{%endraw%}

Weitere Informationen zum Abbrechen von Nachrichten mit Liquid finden Sie in unserer [Liquid-Dokumentation]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages).

## Globale Canvas-Entry-Eigenschaften {#global-canvas-entry-properties}

Mit `canvas_entry_properties` können Sie globale Eigenschaften festlegen, die für alle Nutzer:innen gelten, oder nutzerspezifische Eigenschaften, die nur für die angegebenen Nutzer:innen gelten. Die nutzerspezifische Eigenschaft hat für diese:n Nutzer:in Vorrang vor der globalen Eigenschaft.

### Beispielanfrage {#example-request}

```bash
curl -X POST \
-H 'Content-Type: application/json' \
-d '{
      "api_key": "a valid rest api key",
      "canvas_id": "the ID of your Canvas",
      "canvas_entry_properties": {
        "food_allergies": "none"
      },
      "recipients": [
        {
          "external_user_id": "Customer_123",
          "canvas_entry_properties": {
            "food_allergies": ["dairy", "soy"],
            "nutrition": {
              "calories_per_serving": 200,
              "serving_size_in_ounces": 4
            }
          }
        }
      ]
    }'
```

In dieser Anfrage ist der globale Wert für „food allergies“ gleich „none“. Für Customer_123 ist der Wert „dairy“. Nachrichten in diesem Canvas, die das Liquid-Snippet {%raw%}`{{canvas_entry_properties.${food_allergies}}}`{%endraw%} enthalten, werden für Customer_123 mit „dairy“ und für alle anderen mit „none“ gerendert.

## Anwendungsfall {#use-case}

Wenn Sie ein Canvas haben, das ausgelöst wird, wenn Nutzer:innen einen Artikel auf Ihrer E-Commerce-Website ansehen, ihn aber nicht in den Warenkorb legen, könnte der erste Schritt des Canvas eine Push-Benachrichtigung sein, in der gefragt wird, ob Interesse am Kauf des Artikels besteht. Sie könnten den Produktnamen referenzieren, indem Sie {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %} verwenden.

![Wenn Sie ein Canvas haben, das ausgelöst wird, wenn Nutzer:innen einen Artikel auf Ihrer E-Commerce-Website ansehen, ihn aber nicht in den Warenkorb legen, könnte der erste Schritt des Canvas eine Push-Benachrichtigung sein, in der gefragt wird, ob Interesse am Kauf des Artikels besteht. Sie könnten den Produktnamen referenzieren, indem Sie {% raw %}{{canvas_entry_properties.${product_name}}}{% endraw %} verwenden.]({% image_buster /assets/img/persistent_entry_properties/PEP1.png %}){: style="border:0;margin-left:15px;"}

Der zweite Schritt könnte eine weitere Push-Benachrichtigung senden, die Nutzer:innen zum Bezahlen auffordert, wenn sie den Artikel in den Warenkorb gelegt, aber noch nicht gekauft haben. Sie können weiterhin auf die Entry-Eigenschaft `product_name` verweisen, indem Sie {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %} verwenden.

![Screenshot zum Anwendungsfall.]({% image_buster /assets/img/persistent_entry_properties/PEP12.png %}){: style="border:0;margin-left:15px;"}

## Fehlerbehebung {#troubleshooting}

### Entry-Eigenschaften sind leer bei mehreren Entry-Trigger or triggern or triggern {#entry-properties-are-blank-with-multiple-entry-triggers}

Braze speichert `canvas_entry_properties` von dem Trigger or triggern, der diese:n Nutzer:in in den Canvas geführt hat, nicht von jedem auf dem Canvas konfigurierten Trigger or triggern. Wenn dieser Trigger or triggern kein Event oder API-Payload hat – zum Beispiel **Sitzung starten** oder **Angepassten Attributwert ändern** – ist Liquid `canvas_entry_properties` für diese Journey leer. Nutzer:innen, die denselben Canvas über ein angepasstes Event, einen Kauf oder einen API-Aufruf betreten, verfügen weiterhin über die Eigenschaften aus diesem Payload.

Um Entry-Eigenschaften für alle Nutzer:innen befüllt zu halten, verwenden Sie nur Entry-Typen, die diese Eigenschaften übergeben (angepasstes Event, Kauf oder API-getriggert). Für die Personalisierung im aktuellen Canvas-Editor verwenden Sie [Kontext- und Event-Eigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties). Um nach Eigenschaften zu filtern, nutzen Sie die [Event-Eigenschaften-Segmentierung]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects) anstelle von Liquid `canvas_entry_properties`.