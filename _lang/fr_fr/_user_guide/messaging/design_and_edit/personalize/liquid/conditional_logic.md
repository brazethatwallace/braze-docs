---
nav_title: Logique conditionnelle dans les messages
article_title: Logique conditionnelle Liquid dans les messages
page_order: 6
description: "Cet article de référence explique comment les balises peuvent et doivent être utilisées dans vos campagnes."

---

# Logique conditionnelle dans les messages {#conditional-messaging-logic}

> Les [balises](https://docs.shopify.com/themes/liquid-documentation/tags) vous permettent d'inclure une logique de programmation dans vos campagnes de communication. Les balises peuvent être utilisées pour exécuter des instructions conditionnelles ainsi que pour des cas d'usage avancés, comme l'affectation de variables ou l'itération à travers un bloc de code. <br><br>Cette page explique comment les balises peuvent et doivent être utilisées, notamment comment gérer les valeurs d'attributs null, nil et vides, et comment référencer des attributs personnalisés.

## Mise en forme des balises {#formatting-tags}

{% raw %}
Une balise doit être encadrée par `{% %}`.
{% endraw %}

Pour vous faciliter la vie, Braze inclut une mise en forme colorée qui s'active en vert et en violet si vous avez correctement formaté votre syntaxe Liquid. La mise en forme verte permet d'identifier les balises, tandis que la mise en forme violette met en évidence les zones contenant de la personnalisation.

Si vous avez du mal à utiliser les messages conditionnels, essayez d'écrire la syntaxe conditionnelle avant d'insérer vos attributs personnalisés et autres éléments Liquid.

Par exemple, ajoutez d'abord ce qui suit dans le champ de message :
{% raw %}
```liquid
{% if X >0 %}
{% else %}
{% endif %}
```

Assurez-vous que le texte s'affiche en vert, puis remplacez le `X` par le Liquid ou le contenu connecté de votre choix en utilisant le `+` bleu dans le coin du champ de message, et le `0` par la valeur souhaitée.
<br><br>
Ensuite, ajoutez vos variantes de message selon vos besoins entre les conditionnels `else` :
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Thanks for purchasing! Here's another 10% off!
{% else %}
Buy now! Would 5% off convince you?
{% endif %}
```
{% endraw %}

## Logique conditionnelle {#conditional-logic}

Vous pouvez inclure de nombreux types de [logique intelligente dans les messages](http://docs.shopify.com/themes/liquid-documentation/basics), comme une instruction conditionnelle. L'exemple suivant utilise des [conditionnels](http://docs.shopify.com/themes/liquid-documentation/tags/control-flow-tags) pour internationaliser une campagne :
{% raw %}

```liquid
{% if ${language} == 'en' %}
This is a message in English from Braze!
{% elsif ${language} == 'es' %}
Este es un mensaje en español de Braze !
{% elsif ${language} == 'zh' %}
这是一条来自Braze的中文消息。
{% else %}
This is a message from Braze! This is going to go to anyone who did not match the other specified languages!
{% endif %}
```

### Balises conditionnelles {#conditional-tags}

#### `if` et `elsif` {#if-and-elsif}

La logique conditionnelle commence par la balise `if`, qui définit la première condition à vérifier. Les conditions suivantes utilisent la balise `elsif` et sont vérifiées si les conditions précédentes ne sont pas remplies. Dans cet exemple, si l'appareil d'un utilisateur n'est pas configuré en anglais, ce code vérifiera si l'appareil est configuré en espagnol, et en cas d'échec, il vérifiera si l'appareil est configuré en chinois. Si l'appareil de l'utilisateur remplit l'une de ces conditions, l'utilisateur recevra un message dans la langue correspondante.

#### `else`

Vous avez la possibilité d'inclure une instruction `{% else %}` dans votre logique conditionnelle. Si aucune des conditions que vous avez définies n'est remplie, l'instruction `{% else %}` spécifie le message qui doit être envoyé. Dans cet exemple, nous utilisons l'anglais par défaut si la langue de l'utilisateur n'est ni l'anglais, ni l'espagnol, ni le chinois.

#### `case` et `when` {#case-and-when}

`{% case %}`, `{% when %}` et `{% endcase %}` fonctionnent comme une instruction switch : vous définissez une expression après `case`, et chaque branche `when` s'exécute lorsque cette expression est égale à la valeur indiquée (Liquid utilise l'égalité en arrière-plan, de manière similaire à l'enchaînement de `if` et `elsif` avec `==`). Vous pouvez lister plusieurs valeurs dans une même balise `when` en les séparant par une virgule ou `or`. Utilisez `{% else %}` comme solution de repli lorsqu'aucune valeur ne correspond, puis fermez avec `{% endcase %}`.

Assurez-vous de faire correspondre le format de vos valeurs `when` au type de données. Pour du texte (comme un code de langue), utilisez des guillemets : `{% when 'es' %}`. Pour les nombres, omettez les guillemets : `{% when 2 %}`.

```liquid
{% assign handle = 'cake' %}
{% case handle %}
{% when 'cake' %}
This is a cake
{% when 'cookie' %}
This is a cookie
{% else %}
This is not a cake nor a cookie
{% endcase %}
```

Vous pouvez utiliser le même schéma avec des balises de personnalisation Braze ou d'autres expressions Liquid à la place de `handle`. Pour plus d'options de syntaxe, consultez la [documentation de la balise `case`](https://shopify.dev/docs/api/liquid/tags/case) de Shopify.

#### `endif`

La balise `{% endif %}` signale que vous avez terminé un bloc `if`. Vous devez inclure la balise `{% endif %}` dans tout message utilisant `if`, `elsif`, `unless` ou `else` dans cette chaîne. Si vous n'incluez pas de balise `{% endif %}`, vous obtiendrez une erreur car Braze ne pourra pas analyser votre message. Si vous utilisez `{% case %}` à la place, fermez le bloc avec `{% endcase %}`, et non `{% endif %}`.

{% alert note %}
Dans les balises `if`, `elsif` et `unless`, vous pouvez utiliser des opérateurs mais pas des filtres. Dans les balises `case` et `when`, chaque branche correspond lorsque l'expression `case` est égale à une valeur `when` ; les filtres ne sont pas non plus pris en charge dans ces expressions. Pour évaluer une valeur filtrée, affectez d'abord le résultat du filtre à une variable, puis référencez cette variable dans votre clause `case` ou `when`. Pour plus de détails, consultez [Où utiliser les opérateurs et les filtres]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#where-to-use-operators-and-filters).
{% endalert %}

### Tutoriel : diffuser du contenu basé sur la localisation {#tutorial-deliver-location-based-content}

À la fin de ce tutoriel, vous serez en mesure d'utiliser les balises avec les instructions « if », « elsif » et « else » pour diffuser du contenu en fonction de la localisation d'un utilisateur.

1. Commencez par une balise `if` pour définir quel message doit être envoyé lorsque la ville de l'utilisateur est New York. Si la ville de l'utilisateur est New York, cette première condition est remplie et l'utilisateur recevra un message identifiant son statut de New-Yorkais.

```liquid
{% if ${city} == "New York" %}
  🎉 Hey there, New Yorker! We're excited to offer you a special deal!
  Get 20% off your next sandwich at your local Sandwich Emperor.
  Just show this message at the counter to redeem your offer!
```

{: start="2"}
2. Ensuite, utilisez la balise `elseif` pour définir quel message doit être envoyé si la ville de l'utilisateur est Los Angeles.

```liquid
{% elsif ${city} == "Los Angeles" %}
  🌞 Hello, Los Angeles! Enjoy a sunny day with a delicious sandwich!
  Present this message at our LA restaurant for a 20% discount on your next order!
```

{: start="3"}
3. Utilisons une autre balise `elseif` pour définir quel message doit être envoyé si la ville de l'utilisateur est Chicago.

```liquid
{% elsif ${city} == "Chicago" %}
  🍕 Chicago, we have a treat for you!
  Swing by our restaurant and get 20% off your favorite sandwich.
  Just show this message to our staff!
```

{: start="4"}
4. Maintenant, utilisons la balise `{% else %}` pour spécifier quel message doit être envoyé si la ville de l'utilisateur n'est ni San Francisco, ni New York, ni Chicago.

```liquid
{% else %}
 🥪 Craving a sandwich? Visit us at any of our locations for a delicious meal!
  Check our website for the nearest restaurant to you!
```

{: start="5"}
5. Enfin, nous utiliserons la balise `{% endif %}` pour indiquer que notre logique conditionnelle est terminée.

```liquid
{% endif %}
```

{% endraw %}

{% details Code Liquid complet %}

{% raw %}
```liquid
{% if ${city} == "New York City" %}
  🎉 Hey there, New Yorker! We're excited to offer you a special deal!
  Get 20% off your next sandwich at our New York location.
  Just show this message at the counter to redeem your offer!
{% elsif ${city} == "Los Angeles" %}
  🌞 Hello, Los Angeles! Enjoy a sunny day with a delicious sandwich!
  Present this message at our LA restaurant for a 20% discount on your next order!
{% elsif ${city} == "Chicago" %}
  🍕 Chicago, we have a treat for you!
  Swing by our restaurant and get 20% off your favorite sandwich.
  Just show this message to our staff!
{% else %}
  🥪 Craving a sandwich? Visit us at any of our locations for a delicious meal!
  Check our website for the nearest restaurant to you!
{% endif %}
```
{% endraw %}

{% enddetails %}

## Gestion des valeurs d'attributs null, nil et vides {#accounting-for-null-nil-and-blank-attribute-values}

La logique conditionnelle est un moyen utile de gérer les valeurs d'attributs qui ne sont pas définies dans les profils utilisateur.

### Valeurs d'attributs null et nil {#null-and-nil-attribute-values}

Une valeur null ou nil se produit lorsque la valeur d'un attribut personnalisé n'a pas été définie. Par exemple, un utilisateur qui n'a pas encore défini son prénom n'aura pas de prénom enregistré dans Braze.

Dans certaines circonstances, vous pouvez souhaiter envoyer un message complètement différent aux utilisateurs qui ont un prénom défini et à ceux qui n'en ont pas.

La balise suivante vous permet de spécifier un message pour les utilisateurs dont l'attribut « prénom » est null :

{% raw %}
```liquid
{% if ${first_name} == null %}
  ....
{% endif %}
```
{% endraw %}

![Exemple de message dans le tableau de bord de Braze, utilisant un attribut « prénom » null.]({% image_buster /assets/img/value_null.png %}){: style="max-width:60%;"}

{% raw %}
```liquid
{% if ${first_name} == null %}
We're having a sale! Hurry up and get 10% off all items today only!
{% else %}
Hey {{${first_name} | default: 'there'}}, we're having a sale! Hurry up and get 10% off all items today only!
{% endif %}
```

Notez qu'une valeur d'attribut null n'est pas strictement associée à un type de valeur (par exemple, une chaîne de caractères « null » est identique à un tableau « null »). Ainsi, dans l'exemple ci-dessus, la valeur d'attribut null fait référence à un prénom non défini, qui serait une chaîne de caractères.

{% endraw %}

### Valeurs d'attributs vides {#blank-attribute-values}

Une valeur vide se produit lorsque l'attribut d'un profil utilisateur n'est pas défini, est défini avec une chaîne d'espaces (` `), ou est défini comme `false`. Les valeurs vides doivent être vérifiées avant les autres variables pour éviter une erreur de traitement Liquid.

La balise suivante vous permet de spécifier un message pour les utilisateurs dont l'attribut « prénom » est vide.

{% raw %}
```liquid
{% if ${first_name} == blank %}
  ....
{% endif %}
```
{% endraw %}

## Référencer des attributs personnalisés {#referencing-custom-attributes}

Après avoir [créé des attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#managing-custom-attributes), vous pouvez référencer ces attributs personnalisés dans vos messages Liquid.

Lorsque vous utilisez la logique conditionnelle, vous devez connaître le type de données de l'attribut personnalisé pour vous assurer d'utiliser la syntaxe correcte. Depuis la page **Attributs personnalisés** du tableau de bord, recherchez le type de données associé à votre attribut personnalisé, puis consultez les exemples suivants répertoriés pour chaque type de données.

![Sélection d'un type de données pour un attribut personnalisé. L'exemple fourni montre un attribut Favorite_Category avec un type de données chaîne de caractères.]({% image_buster /assets/img_archive/custom_attribute_data_type.png %}){: style="max-width:80%;"}

{% alert tip %}
Les chaînes de caractères et les tableaux nécessitent des apostrophes droites autour d'eux, tandis que les valeurs booléennes et les entiers n'en ont jamais.
{% endalert %}

### Valeur booléenne {#boolean}

Les [valeurs booléennes]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#booleans) sont des valeurs binaires et peuvent être définies sur `true` ou `false`, comme `registration_complete: true`. Les valeurs booléennes n'ont pas d'apostrophes autour d'elles.

{% raw %}

```liquid
{% if {{custom_attribute.${registration_complete}}} == true %}
```

{% endraw %}

### Nombre {#number}

Les [nombres]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#numbers) sont des valeurs numériques, qui peuvent être des entiers ou des floats. Par exemple, un utilisateur peut avoir `shoe_size: 10` ou `levels_completed: 287`. Les valeurs numériques n'ont pas d'apostrophes autour d'elles.

{% raw %}

```liquid
{% if {{custom_attribute.${shoe_size}}} == 10 %}
```

{% endraw %}

Vous pouvez également utiliser d'autres [opérateurs de base](https://shopify.dev/docs/themes/liquid/reference/basics/operators) tels que inférieur à (<) ou supérieur à (>) pour les entiers :

{% raw %}

```liquid
{% if {{custom_attribute.${flyer_miles}}} >= 500 %}
```

{% endraw %}

### Chaîne de caractères {#string}

Une [chaîne de caractères]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#strings) est composée de caractères alphanumériques et stocke une donnée concernant votre utilisateur. Par exemple, vous pouvez avoir `favorite_color: red` ou `phone_number: 3025981329`. Les valeurs de chaîne de caractères doivent avoir des apostrophes autour d'elles.

{% raw %}

```liquid
{% if {{custom_attribute.${favorite_color}}} == 'blue' %}
```

{% endraw %}

Pour les chaînes de caractères, vous pouvez utiliser à la fois « == » ou « contains » dans votre Liquid.

### Tableau {#array}

Un [tableau]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#arrays) est une liste d'informations concernant votre utilisateur. Par exemple, un utilisateur peut avoir `last_viewed_shows: stranger things, planet earth, westworld`. Les valeurs de tableau doivent avoir des apostrophes autour d'elles.

{% raw %}

```liquid
{% if {{custom_attribute.${last_viewed_shows}}} contains 'homeland' %}
```

{% endraw %}

Pour les tableaux, vous devez utiliser `contains` et ne pouvez pas utiliser `==`.

#### Fonctionnement de `contains` avec les chaînes de caractères et les tableaux {#how-contains-works-with-strings-versus-arrays}

L'opérateur `contains` se comporte différemment selon qu'il évalue une chaîne de caractères ou un tableau :

- **Chaînes de caractères :** `contains` vérifie la présence d'une sous-chaîne n'importe où dans le texte.
- **Tableaux :** `contains` vérifie une correspondance exacte avec un élément complet du tableau.

{% alert important %}
Si un attribut est stocké sous forme de tableau (par exemple, `["med1", "med2", "abc"]`), la recherche de `contains "ab"` sera évaluée à `false` car aucun élément individuel de cette liste n'est exactement `"ab"`.
{% endalert %}

##### Recherche de sous-chaîne dans les tableaux {#substring-matching-on-arrays}

Si vous devez rechercher une correspondance partielle (sous-chaîne) au sein d'un attribut de type tableau, vous devez d'abord convertir le tableau en une seule chaîne de caractères à l'aide du filtre `join`.

Comme Braze ne prend pas en charge les filtres en ligne directement dans les blocs conditionnels {% raw %}`{% if %}`{% endraw %}, vous devez suivre un processus en deux étapes : d'abord, affecter la valeur jointe à une variable, puis exécuter votre vérification conditionnelle.

{% raw %}
```liquid
{% comment %} 1. Convert the array to a string using a comma separator {% endcomment %}
{% assign products_string = {{custom_attribute.${product_array}}} | join: "," %}

{% comment %} 2. Perform the substring check on the new variable {% endcomment %}
{% if products_string contains "ab" %}
  Match found!
{% else %}
  No match.
{% endif %}
```
{% endraw %}


{% alert tip %}
Comme `join` combine les éléments du tableau en une seule chaîne de caractères (séparateur par défaut : un espace unique), les vérifications de sous-chaîne peuvent correspondre au-delà des limites d'éléments (par exemple, `["Napa", "boulevard"]` devient `Napa boulevard`, où `contains "a b"` est `true`). Utilisez un séparateur explicite tel que « , » pour rendre les limites plus claires et réduire les correspondances accidentelles entre éléments.
{% endalert %}

### Horodatage {#time}

Un horodatage indiquant quand un événement a eu lieu. Les valeurs de type [horodatage]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#time) doivent avoir un [filtre mathématique]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters#math-filters) appliqué pour être utilisées dans la logique conditionnelle.

{% raw %}

```liquid
{% assign expire = {{custom_attribute.${subscription_end_date}}} | plus: 0 %}
```

{% endraw %}