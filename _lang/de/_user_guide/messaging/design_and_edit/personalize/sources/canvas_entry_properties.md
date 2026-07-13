---
nav_title: Canvas-Eingangs-Eigenschaften
article_title: Canvas-Eingangs-Eigenschaften
page_order: 4
description: "Erfahren Sie, wie Sie Canvas-Eingangs-Eigenschaften als Personalisierungsquelle in Ihren Nachrichten verwenden können."
---

# Canvas-Eingangs-Eigenschaften {#canvas-entry-properties}

> Wenn ein Canvas durch ein angepasstes Event, einen Kauf oder einen API-Aufruf getriggert wird, können Sie Metadaten aus diesem Trigger verwenden, um Nachrichten im gesamten Canvas-Workflow zu personalisieren. Diese Werte werden als Eingangs-Eigenschaften bezeichnet und sind über alle Schritte eines Canvas hinweg persistent.

## So funktioniert es {#how-it-works}

{% raw %}
Eingangs-Eigenschaften sind über den Liquid-Tag `{{context.${property_name}}}` verfügbar. Wenn ein:e Nutzer:in einen Canvas betritt, erfasst Braze die Eigenschaften aus dem auslösenden Event oder API-Aufruf, und Sie können diese in jedem nachfolgenden Canvas-Schritt referenzieren.

Wenn ein Canvas beispielsweise durch ein `completed_order`-Event mit einer `product_name`-Eigenschaft getriggert wird:

```liquid
Thanks for ordering {{context.${product_name}}}! We'll send you a tracking number soon.
```
{% endraw %}

Eingangs-Eigenschaften sind in aktionsbasierten und API-getriggerten Canvases verfügbar.

## Persistente Eingangs-Eigenschaften {#persistent-entry-properties}

Persistente Eingangs-Eigenschaften ermöglichen es Ihnen, die ursprünglichen Eingangsdaten in jedem Schritt Ihres Canvas zu referenzieren, einschließlich Schritten, die nach einer Verzögerung stattfinden. Ohne Persistenz sind Eingangs-Eigenschaften nur im ersten Schritt verfügbar.

{% alert important %}
Persistente Eingangs-Eigenschaften sind Teil des ursprünglichen Workflows für Canvas-Eingangs-Eigenschaften. Für den aktuellen, aktualisierten Canvas-Editor lesen Sie [Kontext- und Event-Eigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties).
{% endalert %}

Die vollständige Referenz zu persistenten Eingangs-Eigenschaften finden Sie unter [Persistente Eingangs-Eigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties).