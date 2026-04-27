---
nav_title: Définir des valeurs par défaut
article_title: Définir des valeurs Liquid par défaut
page_order: 5
description: "Cet article de référence explique comment définir des valeurs de repli par défaut pour tout attribut de personnalisation que vous utilisez dans vos messages."

---

# Définir des valeurs par défaut

{% raw %}

> Des valeurs de repli par défaut peuvent être définies pour tout attribut de personnalisation que vous utilisez dans vos messages. Cet article explique comment fonctionnent les valeurs par défaut, comment les configurer et comment les utiliser dans vos messages.

## Fonctionnement

Les valeurs par défaut peuvent être ajoutées en spécifiant un [filtre Liquid](http://docs.shopify.com/themes/liquid-documentation/filters) (utilisez `|` pour distinguer le filtre en ligne, comme illustré) avec le nom « default ».

```
| default: 'Insert Your Desired Default Here'
```

Si aucune valeur par défaut n'est fournie et que le champ est manquant ou non défini pour l'utilisateur, le champ sera vide dans le message.

L'exemple suivant montre la syntaxe correcte pour ajouter une valeur par défaut. Dans ce cas, les mots « Valued User » remplaceront l'attribut `{{ ${first_name} }}` si le champ `first_name` de l'utilisateur est vide ou indisponible.

```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```

Pour une utilisatrice nommée Janet Doe, le message s'afficherait de l'une des manières suivantes :

```
Hi Janet, thanks for using the App!
```

Ou...

```
Hi Valued User, thanks for using the App!
```
{% endraw %}

{% alert important %}
La valeur par défaut s'affichera pour les valeurs vides (empty), mais pas pour les valeurs blanches (blank). Une valeur vide ne contient rien, tandis qu'une valeur blanche contient des caractères d'espacement (tels que des espaces) et aucun autre caractère. Par exemple, une chaîne de caractères vide pourrait ressembler à `""` et une chaîne de caractères blanche pourrait ressembler à `" "`.
{% endalert %}

## Définir des valeurs par défaut pour différents types de données

L'exemple ci-dessus montre comment définir une valeur par défaut pour une chaîne de caractères. Vous pouvez définir des valeurs par défaut pour tout type de données Liquid dont la valeur est `empty`, `nil` (non défini) ou `false`, ce qui inclut les chaînes de caractères, les valeurs booléennes, les tableaux, les objets et les nombres.

### Cas d'utilisation : valeurs booléennes

Supposons que vous ayez un attribut personnalisé de type booléen appelé `premium_user` et que vous souhaitiez envoyer un message personnalisé en fonction du statut premium de l'utilisateur. Certains utilisateurs n'ont pas de statut premium défini, vous devrez donc configurer une valeur par défaut pour prendre en compte ces utilisateurs.

1. Vous allez affecter une variable appelée `is_premium_user` à l'attribut `premium_user` avec une valeur par défaut de `false`. Cela signifie que si `premium_user` est `nil`, la valeur de `is_premium_user` sera par défaut `false`.

{% raw %}
```liquid
{% assign is_premium_user = {{custom_attribute.${premium_user}}} | default: false %}
```

{: start="2"}
2. Ensuite, utilisez une logique conditionnelle pour spécifier le message à envoyer si `is_premium_user` est `true`. Autrement dit, quel message envoyer si `premium_user` est `true`. Vous affecterez également une valeur par défaut au prénom de l'utilisateur, au cas où vous ne disposeriez pas de son nom.

```liquid
{% if is_premium_user %}
Hi {{${first_name} | default: 'premium user'}}, thank you for being a premium user!
```

{: start="3"}
3. Enfin, spécifiez le message à envoyer si `is_premium_user` est `false` (ce qui signifie que `premium_user` est `false` ou `nil`). Puis fermez la logique conditionnelle.

```liquid
{% else %}
Hi {{${first_name} | default: 'valued user'}}, consider upgrading to premium for more benefits!
{% endif %}
```
{% endraw %}

{% details Code Liquid complet %}
{% raw %}
```liquid
{% assign is_premium_user = {{custom_attribute.${premium_user}}} | default: false %}
{% if is_premium_user %}
Hi {{${first_name} | default: 'premium user'}}, thank you for being a premium user!
{% else %}
Hi {{${first_name} | default: 'valued user'}}, consider upgrading to premium for more benefits!
{% endif %}
```
{% endraw %}
{% enddetails %}

### Cas d'utilisation : nombres

Supposons que vous ayez un attribut personnalisé numérique appelé `reward_points` et que vous souhaitiez envoyer un message contenant les points de récompense de l'utilisateur. Certains utilisateurs n'ont pas de points de récompense définis, vous devrez donc configurer une valeur par défaut pour prendre en compte ces utilisateurs.

1. Commencez le message en vous adressant à l'utilisateur par son prénom ou une valeur par défaut de `Valued User`, au cas où vous ne disposeriez pas de son nom.

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}},
```
{% endraw %}

{: start="2"}
2. Terminez le message en indiquant le nombre de points de récompense de l'utilisateur à l'aide de l'attribut personnalisé appelé `reward_points` et en utilisant la valeur par défaut de `0`. Tous les utilisateurs dont les `reward_points` ont une valeur `nil` auront `0` points de récompense dans le message.

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}}, you have {{custom_attribute.${reward_points} | default: 0}} reward points.
```
{% endraw %}

### Cas d'utilisation : objets

Supposons que vous ayez un objet d'attribut personnalisé imbriqué appelé `location` contenant les propriétés `city` et `state`. Si l'une de ces propriétés n'est pas définie, vous souhaitez encourager l'utilisateur à les fournir.

1. Adressez-vous à l'utilisateur par son prénom et incluez une valeur par défaut, au cas où vous ne disposeriez pas de son nom.

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}},
```
{% endraw %}

{: start="2"}
2. Rédigez un message indiquant que vous souhaitez confirmer la localisation de l'utilisateur.

{% raw %}
```liquid
We'd like to confirm the location associated with your account. We use this location to send you promotions and offers for stores nearest you. You can update your location in your profile settings.
```
{% endraw %}

{: start="3"}
3. Insérez la localisation de l'utilisateur dans le message et affectez des valeurs par défaut pour les cas où la propriété d'adresse n'est pas définie.

{% raw %}
```liquid
Your location:
City: {{custom_attribute.${address.city} | default: 'Unknown'}}
State: {{custom_attribute.${address.state} | default: 'Unknown'}}
```
{% endraw %}

{% details Code Liquid complet %}
{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}}

We'd like to confirm the location associated with your account. We use this location to send you promotions and offers for stores nearest you. You can update your location in your profile settings.

Your location:
City: {{custom_attribute.${address.city} | default: 'Unknown'}}
State: {{custom_attribute.${address.state} | default: 'Unknown'}}
```
{% endraw %}
{% enddetails %}

### Cas d'utilisation : tableaux

Supposons que vous ayez un attribut personnalisé de type tableau appelé `upcoming_trips` contenant des voyages avec les propriétés `destination` et `departure_date`. Vous souhaitez envoyer aux utilisateurs des messages personnalisés selon qu'ils ont ou non des voyages planifiés.

1. Rédigez une logique conditionnelle pour spécifier qu'un message ne doit pas être envoyé si `upcoming_trips` est `empty`.

{% raw %}
```liquid
{% if {{custom_attribute.${upcoming_trips}}} == empty %}
{% abort_message('No upcoming trips scheduled') %}
```
{% endraw %}

{: start="2"}
2. Spécifiez le message à envoyer si `upcoming_trips` a du contenu :<br><br>**2a.** Adressez-vous à l'utilisateur et incluez une valeur par défaut, au cas où vous ne disposeriez pas de son nom. <br>**2b.** Utilisez une balise `for` pour spécifier que vous allez extraire les propriétés (ou informations) de chaque voyage contenu dans `upcoming_trips`. <br>**2c.** Listez les propriétés dans le message et incluez une valeur par défaut pour le cas où `departure_date` n'est pas défini. (Supposons qu'une `destination` est requise pour créer un voyage, vous n'avez donc pas besoin de définir une valeur par défaut pour celle-ci.)<br>**2d.** Fermez la balise `for`, puis fermez la logique conditionnelle.

{% raw %}
```liquid
{% else %}
Hello {{${first_name} | default: 'fellow traveler'}},
  Here are your upcoming trips:
  <ul>
  {% for trip in {{custom_attribute.${upcoming_trips}}} %}
    <li>
      Destination: {{trip.destination}}
      Departure Date: {{trip.departure_date | default: 'Date not set'}}
    </li>
  {% endfor %}
  </ul>
{% endif %}
```
{% endraw %}

{% details Code Liquid complet %}
{% raw %}
```liquid
{% if {{custom_attribute.${upcoming_trips}}} == blank %}
{% abort_message('No upcoming trips scheduled') %}
{% else %}
Hello {{${first_name} | default: 'fellow traveler'}},
  Here are your upcoming trips:
  <ul>
  {% for trip in {{custom_attribute.${upcoming_trips}}} %}
    <li>
      Destination: {{trip.destination}}
      Departure Date: {{trip.departure_date | default: 'Date not set'}}
    </li>
  {% endfor %}
  </ul>
{% endif %}
```
{% endraw %}
{% enddetails %}

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[37]:#accounting-for-null-attribute-values