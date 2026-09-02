---
nav_title: Propriedades de entrada do Canvas
article_title: Propriedades de entrada do Canvas
page_order: 4
description: "Saiba como usar as propriedades de entrada do Canvas como fonte de personalização nas suas mensagens."
---

# Propriedades de entrada do Canvas {#canvas-entry-properties}

> Quando um Canvas é disparado por um evento personalizado, uma compra ou uma chamada de API or interface de programação do aplicativo (API), você pode usar metadados desse gatilho para personalizar mensagens em todo o fluxo de trabalho do Canvas. Esses valores são conhecidos como propriedades de entrada e persistem em todas as etapas de um Canvas.

## Como funciona {#how-it-works}

{% raw %}
As propriedades de entrada estão disponíveis por meio da Liquid tag `{{context.${property_name}}}`. Quando um usuário entra em um Canvas, a Braze captura as propriedades do evento ou da chamada de API or interface de programação do aplicativo (API) que disparou a entrada, e você pode referenciá-las em qualquer etapa subsequente do Canvas.

Por exemplo, se um Canvas é disparado por um evento `completed_order` com uma propriedade `product_name`:

```liquid
Thanks for ordering {{context.${product_name}}}! We'll send you a tracking number soon.
```
{% endraw %}

As propriedades de entrada estão disponíveis em Canvas baseados em ação e disparados por API or interface de programação do aplicativo (API).

## Propriedades de entrada persistentes {#persistent-entry-properties}

As propriedades de entrada persistentes permitem que você referencie os dados originais de entrada em todas as etapas do seu Canvas, incluindo etapas que ocorrem após uma postergação. Sem a persistência, as propriedades de entrada ficam disponíveis apenas na primeira etapa.

{% alert important %}
As propriedades de entrada persistentes fazem parte do fluxo de trabalho original de propriedades de entrada do Canvas. Para o editor atualizado do Canvas, consulte [Propriedades de contexto e evento]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties).
{% endalert %}

Para a referência completa sobre propriedades de entrada persistentes, consulte [Propriedades de entrada persistentes]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties).