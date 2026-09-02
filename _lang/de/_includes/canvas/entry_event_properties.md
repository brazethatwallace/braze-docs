Sie können Canvas-Entry-Eigenschaften und Event-Eigenschaften in Ihren Canvas-Journeys für Nutzer:innen verwenden.

{% tabs local %}
{% tab Canvas Entry Properties %}

[Canvas-Entry-Eigenschaften]({{site.baseurl}}/api/objects_filters/context_object) sind die Eigenschaften, die Sie für Canvase zuordnen, die aktionsbasiert oder API-getriggert sind. Beachten Sie, dass das Objekt `canvas_entry_properties` eine maximale Größe von 50 KB hat.

{% alert note %}
Speziell für In-App-Nachricht-Kanäle gilt: `context` kann nur in Canvas referenziert werden.
{% endalert %}

Sie können `context` in jedem Nachrichten-Schritt mit diesem Liquid-Format referenzieren: ``{% raw %} context.${property_name} {% endraw %}``. Beachten Sie, dass es sich bei den Events um angepasste Events oder Kauf-Events handeln muss, um auf diese Weise verwendet werden zu können.

#### Anwendungsfall {#use-case}

{% raw %}
Angenommen, der Shop RetailApp erhält folgende Anfrage: `"context" : {"product_name" : "shoes", "product_price" : 79.99}`.

RetailApp kann den Produktnamen (Schuhe) mit diesem Liquid in eine Nachricht einfügen: `{{context.${product_name}}}`.
{% endraw %}

RetailApp kann auch spezielle Nachrichten für verschiedene `product_name`-Eigenschaften in einem Canvas Trigger or triggern or triggern, das Nutzer:innen anspricht, nachdem sie ein Kauf-Event ausgelöst haben. Sie können zum Beispiel unterschiedliche Nachrichten an Nutzer:innen, die Schuhe gekauft haben, und Nutzer:innen, die etwas anderes gekauft haben, senden, indem Sie das folgende Liquid in einen Nachrichten-Schritt einfügen.

{% raw %}
```markdown
{% if  {{context.${product_name}}} == "shoes" %}
  Your order is set to ship soon. While you're waiting, why not step up your shoe care routine with a little upgrade? Check out our selection of shoelaces and premium shoe polish.
{% else %}
  Your order will be on its way shortly. If you missed something, you have until the end of the week to add more items to your cart for the same discounts.
{% endif %}

```
{% endraw %}

{% details Für den Original-Canvas-Editor erweitern %}

Sie können Canvase nicht mehr mit dem Original-Editor erstellen oder duplizieren. Dieser Abschnitt dient nur als Referenz. Bei Canvase, die mit dem Original-Editor erstellt wurden, können Canvas-Entry-Eigenschaften nur im ersten vollständigen Schritt eines Canvas referenziert werden.

{% enddetails %}
{% endtab %}

{% tab Event Properties %}

Event-Eigenschaften beziehen sich auf die Eigenschaften, die Sie für angepasste Events und Käufe festlegen. Diese `event_properties` können in Campaigns mit aktionsbasierter Zustellung und Canvase verwendet werden.

{% alert important %}
Sie können `event_properties` nicht im ersten Nachrichten-Schritt Ihres Canvas verwenden. Stattdessen müssen Sie `context` verwenden oder einen Aktionspfade-Schritt mit dem entsprechenden Event **vor** dem Nachrichten-Schritt hinzufügen, der `event_properties` enthält.
{% endalert %}

In Canvas können angepasste Event- und Kauf-Event-Eigenschaften in Liquid in jedem Nachrichten-Schritt verwendet werden, der auf einen Aktionspfade-Schritt folgt. Stellen Sie sicher, dass Sie {% raw %} ``{{event_properties.${property_name}}}``{% endraw %} verwenden, wenn Sie auf diese Event-Eigenschaften verweisen. Diese Events müssen angepasste Events oder Kauf-Events sein, um auf diese Weise in der Nachrichten-Komponente verwendet werden zu können.

Im ersten Nachrichten-Schritt, der auf einen Aktionspfade-Schritt folgt, können Sie Event-Eigenschaften verwenden, die sich auf das in diesem Aktionspfad referenzierte Event beziehen. Diese Event-Eigenschaften können jedoch nur verwendet werden, wenn die Nutzer:innen die Aktion tatsächlich durchgeführt haben (und nicht in die Gruppe „Alle anderen“ einsortiert wurden). Zwischen diesem Aktionspfade-Schritt und dem Nachrichten-Schritt können Sie weitere Schritte einfügen (die selbst keine Aktionspfade- oder Nachrichten-Schritte sind).

{% details Für den Original-Canvas-Editor erweitern %}

Sie können Canvase nicht mehr mit dem Original-Editor erstellen oder duplizieren. Dieser Abschnitt dient nur als Referenz. Im Original-Canvas-Editor können Event-Eigenschaften nicht in geplanten vollständigen Schritten verwendet werden. Sie können jedoch Event-Eigenschaften im ersten vollständigen Schritt eines aktionsbasierten Canvas verwenden, auch wenn der vollständige Schritt geplant ist.

{% enddetails %}

{% endtab %}
{% endtabs %}

Weitere Informationen und Beispiele finden Sie unter [Canvas-Entry-Eigenschaften und Event-Eigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties).