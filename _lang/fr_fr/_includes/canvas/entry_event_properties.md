Vous pouvez utiliser les propriétés d'entrée et les propriétés d'événement Canvas dans vos parcours utilisateur Canvas.

{% tabs local %}
{% tab Canvas Entry Properties %}

Les [propriétés d'entrée de Canvas]({{site.baseurl}}/api/objects_filters/context_object) correspondent aux propriétés que vous mappez pour les Canvas basés sur des actions ou déclenchés par API. Notez que l'objet `canvas_entry_properties` a une taille maximale de 50 Ko.

{% alert note %}
Pour les canaux de messages in-app en particulier, `context` ne peut être référencé que dans Canvas.
{% endalert %}

Vous pouvez faire référence à `context` dans n'importe quelle étape Message avec ce format Liquid : ``{% raw %} context.${property_name} {% endraw %}``. Notez que les événements doivent être des événements personnalisés ou des événements d'achat pour être utilisés de cette manière.

#### Cas d'utilisation {#use-case}

{% raw %}
Supposons qu'un magasin de détail, RetailApp, ait la requête suivante : `"context" : {"product_name" : "shoes", "product_price" : 79.99}`.

RetailApp peut extraire le nom du produit (chaussures) dans un message à l'aide de ce Liquid : `{{context.${product_name}}}`.
{% endraw %}

RetailApp peut également déclencher l'envoi de messages spécifiques pour différentes propriétés `product_name` dans un Canvas qui cible les utilisateurs après qu'ils ont déclenché un événement d'achat. Par exemple, il est possible d'envoyer des messages différents aux utilisateurs qui ont acheté des chaussures et à ceux qui ont acheté autre chose en ajoutant le Liquid suivant dans une étape Message.

{% raw %}
```markdown
{% if  {{context.${product_name}}} == "shoes" %}
  Your order is set to ship soon. While you're waiting, why not step up your shoe care routine with a little upgrade? Check out our selection of shoelaces and premium shoe polish.
{% else %}
  Your order will be on its way shortly. If you missed something, you have until the end of the week to add more items to your cart for the same discounts.
{% endif %}

```
{% endraw %}

{% details Développer pour l'éditeur Canvas d'origine %}

Vous ne pouvez plus créer ni dupliquer de Canvas à l'aide de l'éditeur d'origine. Cette section n'est disponible qu'à titre de référence. Pour les Canvas créés avec l'éditeur d'origine, les propriétés d'entrée de Canvas ne peuvent être référencées que dans la première étape complète d'un Canvas.

{% enddetails %}
{% endtab %}

{% tab Event Properties %}

Les propriétés d'événement font référence aux propriétés que vous définissez pour les événements personnalisés et les achats. Ces `event_properties` peuvent être utilisées dans des Campaigns avec livraison par événement et dans des Canvas.

{% alert important %}
Il n'est pas possible d'utiliser `event_properties` dans la première étape Message de votre Canvas. Vous devez utiliser `context` ou ajouter une étape Parcours d'actions avec l'événement correspondant **avant** l'étape Message qui inclut `event_properties`.
{% endalert %}

Dans Canvas, les propriétés d'événement personnalisé et d'événement d'achat peuvent être utilisées dans Liquid dans n'importe quelle étape Message qui suit une étape Parcours d'actions. Veillez à utiliser {% raw %} ``{{event_properties.${property_name}}}``{% endraw %} si vous faites référence à ces propriétés d'événement. Ces événements doivent être des événements personnalisés ou des événements d'achat pour être utilisés de cette manière dans le composant Message.

Dans la première étape Message suivant un Parcours d'actions, vous pouvez utiliser les propriétés d'événement associées à l'événement référencé dans ce Parcours d'actions. Cependant, ces propriétés d'événement ne peuvent être utilisées que si l'utilisateur a réellement effectué l'action (et n'a pas été classé dans le groupe Tous les autres). Vous pouvez avoir d'autres étapes (qui ne sont pas un autre Parcours d'actions ou une étape Message) entre ce Parcours d'actions et l'étape Message.

{% details Développer pour l'éditeur Canvas d'origine %}

Vous ne pouvez plus créer ni dupliquer de Canvas à l'aide de l'éditeur d'origine. Cette section n'est disponible qu'à titre de référence. Dans l'éditeur Canvas d'origine, les propriétés d'événement ne peuvent pas être utilisées dans les étapes complètes planifiées. Cependant, vous pouvez utiliser les propriétés d'événement dans la première étape complète d'un Canvas basé sur une action, même si l'étape complète est planifiée.

{% enddetails %}

{% endtab %}
{% endtabs %}

Consultez [Propriétés d'entrée de Canvas et propriétés d'événement]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) pour plus d'informations et d'exemples.