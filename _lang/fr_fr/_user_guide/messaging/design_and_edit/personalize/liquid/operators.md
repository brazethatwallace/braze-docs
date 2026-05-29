---
nav_title: Opérateurs
article_title: Opérateurs Liquid
page_order: 2
description: "Cette page de référence présente les opérateurs pris en charge par Liquid, ainsi que des exemples pertinents."

---

# Opérateurs {#operators}

> Liquid prend en charge de nombreux [opérateurs](https://docs.shopify.com/themes/liquid/basics/operators) que vous pouvez utiliser dans vos instructions conditionnelles. Cette page présente les opérateurs pris en charge par Liquid et fournit des cas d'utilisation pour les intégrer dans vos messages.

Ce tableau répertorie les opérateurs pris en charge. Notez que les parenthèses sont des caractères non valides dans Liquid et empêchent vos balises de fonctionner.

| Syntaxe | Description de l'opérateur |
|---------|-----------|
| == | est égal à |
| != | n'est pas égal à |
| > | supérieur à |
| < | inférieur à |
| >= | supérieur ou égal à |
| <= | inférieur ou égal à |
| or | condition A ou condition B |
| and | condition A et condition B |
| contains | vérifie si une chaîne de caractères ou un tableau de chaînes contient une chaîne de caractères |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Operators" }

{% alert note %}
Les opérateurs peuvent être utilisés dans les instructions conditionnelles (`if`, `elsif`, `unless`) mais pas dans les instructions `assign`, les boucles `for` ou les crochets d'accès aux tableaux. Dans les balises `case` et `when`, chaque branche compare l'expression `case` à une valeur `when` en utilisant l'égalité plutôt que des expressions d'opérateurs arbitraires. Pour des exemples, consultez [Logique conditionnelle de messagerie]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic/#case-and-when-tags). Pour une explication complète, consultez [Où utiliser les opérateurs et les filtres]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid/#where-to-use-operators-and-filters).
{% endalert %}

### Regrouper des conditions sans parenthèses {#grouping-conditions-without-parentheses}

Liquid ne prend pas en charge les parenthèses pour regrouper les expressions. Pour évaluer une logique booléenne complexe telle que `(a and b) or c`, utilisez des instructions `if` imbriquées ou des variables intermédiaires.

Par exemple, pour vérifier si une valeur satisfait une condition composée, assignez une variable intermédiaire :

{% raw %}
```liquid
{% assign qualifies = false %}
{% if points > 100 %}
{% assign qualifies = true %}
{% elsif points == 100 and member_level == 'gold' %}
{% assign qualifies = true %}
{% endif %}

{% if qualifies %}
You qualify for a reward!
{% endif %}
```
{% endraw %}

## Tutoriels {#tutorials}

Passons en revue quelques tutoriels pour apprendre à utiliser ces opérateurs dans vos campagnes marketing :

### Choisir un message avec un attribut personnalisé de type entier {#choose-a-message-with-an-integer-custom-attribute}

Envoyons des notifications push avec des réductions promotionnelles personnalisées aux utilisateurs qui ont ou n'ont pas effectué d'achats. La notification push utilisera un attribut personnalisé de type entier appelé `total_spend` pour vérifier les dépenses totales d'un utilisateur.

1. Écrivez une instruction conditionnelle en utilisant l'opérateur supérieur à (`>`) pour vérifier si les dépenses totales d'un utilisateur sont supérieures à `0`, indiquant qu'il a effectué un achat. Ensuite, créez un message à envoyer à ces utilisateurs.

{% raw %}
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
```
{% endraw %}

{: start="2"}
2. Ajoutez la balise {% raw %}`{% else %}`{% endraw %} pour cibler les utilisateurs dont les dépenses totales sont égales à `0` ou n'existent pas. Ensuite, créez un message à envoyer à ces utilisateurs.

{% raw %}
```liquid
{% else %}
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
```
{% endraw %}

{: start="3"}
3. Fermez la logique conditionnelle avec la balise {% raw %}`{% endif %}`{% endraw %}.

{% raw %}
```liquid
{% endif %}
```
{% endraw %}

![Un compositeur de notification push avec le code Liquid complet du tutoriel.]({% image_buster /assets/img/liquid-if-totalspend.png %}){: width="100%"}

{% details Code Liquid complet %}
{% raw %}
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
{% else %}
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
{% endif %}
```
{% endraw %}
{% enddetails %}

Maintenant, si l'attribut personnalisé « Total Spend » d'un utilisateur est supérieur à `0`, il recevra le message :

```
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
```
Si l'attribut personnalisé « Total Spend » d'un utilisateur n'existe pas ou est égal à `0`, il recevra le message suivant :

```
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
```

### Choisir un message avec un attribut personnalisé de type chaîne de caractères {#choose-a-message-with-a-string-custom-attribute}

Envoyons des notifications push aux utilisateurs et personnalisons le message en fonction du dernier jeu auquel chaque utilisateur a joué. Cela utilisera un attribut personnalisé de type chaîne de caractères appelé `recent_game` pour vérifier à quel jeu un utilisateur a joué en dernier.

1. Écrivez une instruction conditionnelle en utilisant l'opérateur d'égalité (`==`) pour vérifier si le jeu le plus récent d'un utilisateur est *Awkward Dinner Party*. Ensuite, créez un message à envoyer à ces utilisateurs.

{% raw %}
```liquid
{% if {{custom_attribute.${recent_game}}} == 'Awkward Dinner Party' %}
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
```
{% endraw %}

{: start="2"}
2. Utilisez la balise `elsif` avec l'opérateur d'égalité (`==`) pour vérifier si le jeu le plus récent de l'utilisateur est *Proxy War 3: War of Thirst*. Ensuite, créez un message à envoyer à ces utilisateurs.

{% raw %}
```liquid
{% elsif {{custom_attribute.${recent_game}}} == 'Proxy War 3: War of Thirst' %}
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
```
{% endraw %}

{: start="3"}
3. Utilisez la balise `elsif` avec les opérateurs « n'est pas égal à » (`!=`) et « et » (`and`) pour vérifier si l'utilisateur a un jeu récent (c'est-à-dire que la valeur n'est pas vide), et que le jeu n'est ni *Awkward Dinner Party* ni *Proxy War 3: War of Thirst*. Ensuite, créez un message à envoyer à ces utilisateurs.

{% raw %}
```liquid
{% elsif {{custom_attribute.${recent_game}}} != blank and {{custom_attribute.${recent_game}}} != 'Awkward Dinner Party' and {{custom_attribute.${recent_game}}} != 'Proxy War 3: War of Thirst' %}
Limited Time Deal! Get 15% off our best-selling classics!
```
{% endraw %}

{: start="4"}
4. Ajoutez la balise {% raw %}`{% else %}`{% endraw %} pour cibler les utilisateurs qui n'ont pas de jeu récent. Ensuite, créez un message à envoyer à ces utilisateurs.

{% raw %}
```liquid
{% else %}
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
```
{% endraw %}

{: start="5"}
5. Fermez la logique conditionnelle avec la balise {% raw %}`{% endif %}`{% endraw %}.

{% raw %}
```liquid
{% endif %}
```
{% endraw %}

{% details Code Liquid complet %}
{% raw %}
```liquid
{% if {{custom_attribute.${recent_game}}} == 'Awkward Dinner Party' %}
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
{% elsif {{custom_attribute.${recent_game}}} == 'Proxy War 3: War of Thirst' %}
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
{% elsif {{custom_attribute.${recent_game}}} != blank and {{custom_attribute.${recent_game}}} != 'Awkward Dinner Party' and {{custom_attribute.${recent_game}}} != 'Proxy War 3: War of Thirst' %}
Limited Time Deal! Get 15% off our best-selling classics!
{% else %}
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
{% endif %}
```
{% endraw %}
{% enddetails %}

![Un compositeur de notification push avec le code Liquid complet du tutoriel.]({% image_buster /assets/img/liquid-if-elsif-games.png %})

Maintenant, si un utilisateur a joué en dernier à *Awkward Dinner Party*, il recevra ce message :

```
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
```

Si le jeu le plus récent d'un utilisateur est *Proxy War 3: War of Thirst*, il recevra ce message :

```
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
```

Si un utilisateur a récemment joué à un jeu qui n'était ni *Awkward Dinner Party* ni *Proxy War 3: War of Thirst*, il recevra ce message :

```
Limited Time Deal! Get 15% off our best-selling classics!
```

Si un utilisateur n'a joué à aucun jeu ou si cet attribut personnalisé n'existe pas dans son profil, il recevra ce message :

```
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
```

### Annuler un message en fonction de la localisation {#abort-message-based-on-location}

Vous pouvez annuler un message en fonction de pratiquement n'importe quel critère. Annulons un message si un utilisateur ne se trouve pas dans une zone spécifique, car il pourrait ne pas être éligible à la promotion, au spectacle ou à la livraison.

1. Écrivez une instruction conditionnelle en utilisant l'opérateur d'égalité (`==`) pour vérifier si le fuseau horaire de l'utilisateur est `America/Los_Angeles`, puis créez un message à envoyer à ces utilisateurs.

{% raw %}
```liquid
{% if {{${time_zone}}} == 'America/Los_Angeles' %}
Stream now!
```
{% endraw %}

{: start="2"}
2. Pour éviter d'envoyer des messages aux utilisateurs en dehors du fuseau horaire `America/Los_Angeles`, encadrez les balises {% raw %}`{% else %}`{% endraw %} et {% raw %}`{% endif %}`{% endraw %} autour d'une balise {% raw %}`{% abort_message () %}`{% endraw %}.

{% raw %}
```liquid
{% else %}
{% abort_message () %}
{% endif %}
```
{% endraw %}

{% details Code Liquid complet %}
{% raw %}
```liquid
{% if {{${time_zone}}} =='America/Los_Angeles' %}
Stream now!
{% else %}
{% abort_message () %}
{% endif %}
```
{% endraw %}
{% enddetails %}

![Un compositeur de notification push avec le code Liquid complet du tutoriel.]({% image_buster /assets/img/abort-if.png %})

Vous pouvez également [annuler des messages]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content/) en fonction du Contenu connecté.

## Résolution des problèmes {#troubleshooting}

### L'envoi test n'arrive pas lors de l'utilisation d'`abort_message` {#test-send-doesnt-arrive-when-using-abort_message}

Si vous utilisez [`abort_message`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/) et qu'un envoi test n'arrive jamais, il se peut que l'utilisateur de prévisualisation ne possède pas les attributs attendus par votre code Liquid. La logique d'annulation s'exécute lors du rendu ; lorsqu'elle se déclenche, Braze n'envoie pas le message. Prévisualisez avec un utilisateur qui dispose des données de profil requises, ou utilisez **Preview as user** pour tester les champs du destinataire qui fournissent les mêmes valeurs que celles de votre audience de production.

### La prévisualisation peut convertir incorrectement les types de propriétés {#preview-may-incorrectly-coerce-property-types}

Lors de la prévisualisation d'un message dans le tableau de bord, la plupart des variables (comme les attributs personnalisés) sont converties dans le type correct. Cependant, certaines variables n'ont pas de type défini que la prévisualisation peut rechercher :

- `api_trigger_properties`
- `canvas_entry_properties`
- `context`

Pour ces propriétés, la prévisualisation tente de déduire le type à partir de la valeur. Cela signifie qu'une valeur que vous souhaitez traiter comme une **chaîne de caractères** pourrait être interprétée à tort comme un **nombre**. Par exemple, si la valeur d'une propriété est la chaîne `"3"`, la prévisualisation peut la convertir en entier `3`, ce qui peut provoquer un comportement inattendu dans les opérations sur les chaînes comme `contains` ou `split`.

Si vous observez des résultats de prévisualisation inattendus avec ces types de propriétés, gardez à l'esprit que l'inférence de type de la prévisualisation peut ne pas correspondre à ce qui se passe au moment de l'envoi. Au moment de l'envoi, les types de données réels provenant de l'événement déclencheur ou de l'appel API sont préservés.

Pour forcer un type spécifique dans la prévisualisation, vous pouvez convertir explicitement la valeur :

{% raw %}
```liquid
{% comment %} Force a value to be treated as a number {% endcomment %}
{% assign orders = {{canvas_entry_properties.${number_of_orders}}} | plus: 0 %}

{% comment %} Force a value to be treated as a string {% endcomment %}
{% assign code = {{api_trigger_properties.${promo_code}}} | append: "" %}
```
{% endraw %}