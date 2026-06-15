---
nav_title: Persistente Eingangs-Eigenschaften
article_title: Persistente Eingangs-Eigenschaften
alias: "/persistent_entry/"
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie persistente Eingangs-Eigenschaften in Ihrem Canvas verwenden können, um besser kuratierte Nachrichten zu senden und ein hochgradig verfeinertes Endnutzer:innen-Erlebnis zu schaffen."
tool: Canvas
page_order: 5
---

# Persistente Eingangs-Eigenschaften {#persistent-entry-properties}

> Wenn ein Canvas durch ein angepasstes Event, einen Kauf oder einen API-Aufruf getriggert wird, können Sie Metadaten aus dem API-Aufruf, dem angepassten Event oder dem Kauf-Event zur Personalisierung in jedem Schritt Ihres Canvas-Workflows verwenden. Sie können diese Eigenschaften nutzen, um besser kuratierte Nachrichten zu senden.

{% alert important %}
Persistente Eingangs-Eigenschaften sind ein Artefakt des ursprünglichen Canvas-Editors, daher gibt es veraltete Verweise auf Begriffe wie Canvas-Eingangs-Eigenschaften, die aus historischen Gründen bestehen bleiben. Für den aktuellen Canvas-Editor lesen Sie [Kontext- und Event-Eigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/).<br><br>Um persistente Eingangs-Eigenschaften im aktuellen Canvas-Editor zu verwenden, müssen Sie entweder einen neuen Canvas erstellen oder einen bestehenden in den aktuellen Editor [klonen]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases/).
{% endalert %}

## Eingangs-Eigenschaften verwenden {#using-entry-properties}

Eingangs-Eigenschaften können in aktionsbasierten und API-getriggerten Canvases verwendet werden. Diese Eingangs-Eigenschaften werden definiert, wenn ein Canvas durch ein angepasstes Event, einen Kauf oder einen API-Aufruf getriggert wird. Weitere Informationen finden Sie in den folgenden Artikeln:

- [Canvas-Eingangs-Eigenschaften-Objekt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/)
- [Event-Eigenschaften-Objekt]({{site.baseurl}}/api/objects_filters/event_object/)
- [Kauf-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-product_id)

Eigenschaften, die von diesen Objekten übergeben werden, können mit dem Liquid-Tag `canvas_entry_properties` referenziert werden. Zum Beispiel könnte eine Anfrage mit `"canvas_entry_properties": {"product_name": "shoes", "product_price": 79.99}` das Wort „shoes“ zu einer Nachricht hinzufügen, indem der Liquid-Code {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %} verwendet wird.

Wenn ein Canvas eine Nachricht mit dem Liquid-Tag `canvas_entry_properties` enthält, werden die mit diesen Eigenschaften verknüpften Werte für die Dauer der Journey einer Nutzer:in im Canvas gespeichert und gelöscht, wenn die Nutzer:in den Canvas verlässt. Beachten Sie, dass Canvas-Eingangs-Eigenschaften nur zur Referenzierung in Liquid verfügbar sind. Um innerhalb des Canvas nach den Eigenschaften zu filtern, verwenden Sie stattdessen die [Event-Eigenschafts-Segmentierung]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects/).

{% alert note %}
Das Canvas-Eingangs-Eigenschaften-Objekt hat eine maximale Größenbeschränkung von 50 KB.
{% endalert %}

## Canvas aktualisieren, um Eingangs-Eigenschaften zu verwenden {#updating-canvas-to-use-entry-properties}

Wenn ein aktiver Canvas, der zuvor keine Nachrichten mit `canvas_entry_properties` enthielt, bearbeitet wird, um `canvas_entry_properties` einzuschließen, ist der entsprechende Wert für diese Eigenschaft nicht für Nutzer:innen verfügbar, die den Canvas betreten haben, bevor `canvas_entry_properties` zum Canvas hinzugefügt wurde. Die Werte werden nur für Nutzer:innen gespeichert, die den Canvas nach der Änderung betreten.

Wenn Sie beispielsweise am 3. November einen Canvas gestartet haben, der keine Eingangs-Eigenschaften verwendete, und dann am 11. November eine neue Eigenschaft `product_name` zum Canvas hinzugefügt haben, würden Werte für `product_name` nur für Nutzer:innen gespeichert, die den Canvas ab dem 11. November betreten haben.

Falls eine Canvas-Eingangs-Eigenschaft null oder leer ist, können Sie Nachrichten mithilfe von Bedingungen abbrechen. Das folgende Code-Snippet ist ein Beispiel dafür, wie Sie Liquid verwenden können, um eine Nachricht abzubrechen.
{%raw%}
```
{% if canvas_entry_properties.${product_name} == blank %}
{% abort_message() %}
{% endif %}
```
{%endraw%}

Weitere Informationen zum Abbrechen von Nachrichten mit Liquid finden Sie in unserer [Liquid-Dokumentation]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/#abort-messages).

## Globale Canvas-Eingangs-Eigenschaften {#global-canvas-entry-properties}

Mit `canvas_entry_properties` können Sie globale Eigenschaften festlegen, die für alle Nutzer:innen gelten, oder nutzerspezifische Eigenschaften, die nur für die angegebene Nutzer:in gelten. Die nutzerspezifische Eigenschaft hat Vorrang vor der globalen Eigenschaft für diese Nutzer:in.

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

In dieser Anfrage ist der globale Wert für „food allergies“ „none“. Für Customer_123 ist der Wert „dairy“. Nachrichten in diesem Canvas, die das Liquid-Snippet {%raw%}`{{canvas_entry_properties.${food_allergies}}}`{%endraw%} enthalten, werden für Customer_123 mit „dairy“ und für alle anderen mit „none“ gerendert.

## Anwendungsfall {#use-case}

Wenn Sie einen Canvas haben, der getriggert wird, wenn eine Nutzer:in einen Artikel auf Ihrer E-Commerce-Website ansieht, ihn aber nicht in den Warenkorb legt, könnte der erste Schritt des Canvas eine Push-Benachrichtigung sein, die fragt, ob Interesse am Kauf des Artikels besteht. Sie könnten den Produktnamen referenzieren, indem Sie {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %} verwenden.

![]({% image_buster /assets/img/persistent_entry_properties/PEP1.png %}){: style="border:0;margin-left:15px;"}

Der zweite Schritt könnte eine weitere Push-Benachrichtigung senden, die die Nutzer:in zum Checkout auffordert, wenn der Artikel in den Warenkorb gelegt, aber noch nicht gekauft wurde. Sie können weiterhin die Eingangs-Eigenschaft `product_name` referenzieren, indem Sie {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %} verwenden.

![]({% image_buster /assets/img/persistent_entry_properties/PEP12.png %}){: style="border:0;margin-left:15px;"}