---
nav_title: Propriétés d'entrée du Canvas
article_title: Propriétés d'entrée du Canvas
page_order: 4
description: "Découvrez comment utiliser les propriétés d'entrée du Canvas comme source de personnalisation dans vos messages."
---

# Propriétés d'entrée du Canvas

> Lorsqu'un Canvas est déclenché par un événement personnalisé, un achat ou un appel API, vous pouvez utiliser les métadonnées de ce déclencheur pour personnaliser les messages tout au long du workflow du Canvas. Ces valeurs sont appelées propriétés d'entrée et elles persistent à travers toutes les étapes d'un Canvas.

## Fonctionnement

{% raw %}
Les propriétés d'entrée sont accessibles via l'étiquette Liquid `{{context.${property_name}}}`. Lorsqu'un utilisateur entre dans un Canvas, Braze capture les propriétés de l'événement déclencheur ou de l'appel API, que vous pouvez ensuite référencer dans n'importe quelle étape suivante du Canvas.

Par exemple, si un Canvas est déclenché par un événement `completed_order` avec une propriété `product_name` :

```liquid
Thanks for ordering {{context.${product_name}}}! We'll send you a tracking number soon.
```
{% endraw %}

Les propriétés d'entrée sont disponibles dans les Canvas déclenchés par une action et les Canvas déclenchés par l'API.

## Propriétés d'entrée persistantes

Les propriétés d'entrée persistantes vous permettent de référencer les données d'entrée d'origine dans chaque étape de votre Canvas, y compris les étapes qui surviennent après un délai. Sans la persistance, les propriétés d'entrée ne sont disponibles que dans la première étape.

{% alert important %}
Les propriétés d'entrée persistantes font partie du workflow original des propriétés d'entrée du Canvas. Pour l'éditeur Canvas mis à jour actuel, consultez [Contexte et propriétés d'événement]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/).
{% endalert %}

Pour la référence complète sur les propriétés d'entrée persistantes, consultez [Propriétés d'entrée persistantes]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties/).