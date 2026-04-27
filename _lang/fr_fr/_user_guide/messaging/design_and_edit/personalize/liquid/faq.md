---
nav_title: FAQ
article_title: Questions fréquentes
page_order: 12
description: "Cet article fournit des réponses aux questions fréquemment posées sur Liquid."

---

# Questions fréquentes

> Sur cette page, vous trouverez des réponses aux questions fréquemment posées sur Liquid.<br><br>Braze ne prend pas actuellement en charge 100 % du Liquid de Shopify, mais seulement certaines parties que nous avons tenté de décrire dans notre documentation. Nous vous recommandons vivement de tester tous les messages utilisant Liquid avant de les envoyer afin de réduire le risque d'erreurs ou d'utilisation de Liquid non pris en charge.

### Comment utiliser les extraits de code Liquid dans Braze ?

Dans de nombreux cas, vous pouvez intégrer des extraits de code Liquid en accédant à vos campagnes ou Canvas, puis en insérant du Liquid dans la fenêtre modale de personnalisation, par exemple dans le corps d'un e-mail ou dans vos segments.

#### Où puis-je en savoir plus ?

Pour en savoir plus sur Liquid, consultez notre parcours guidé Braze Learning [Personnalisation dynamique avec Liquid](https://learning.braze.com/path/dynamic-personalization-with-liquid) ! Vous pouvez également consulter la [bibliothèque de cas d'utilisation Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases/) pour trouver de l'inspiration et une variété d'exemples de personnalisation utilisant Liquid.

### Quelle est la différence entre l'utilisation de Liquid et du Contenu connecté pour la personnalisation ?

Le Contenu connecté de Braze est un exemple d'étiquette Liquid. Il est également utilisé pour la personnalisation, mais les données proviennent d'un endpoint externe plutôt que de données stockées dans Braze. Consultez notre section dédiée au [Contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) pour en savoir plus sur les possibilités de personnalisation de vos messages.

### Qu'est-ce que le templating Liquid ?

C'est la manière la plus courante d'utiliser Liquid dans Braze. Le templating Liquid consiste à extraire des données du profil d'un utilisateur pour les insérer dans un message. Ces données peuvent aller du prénom de l'utilisateur aux événements personnalisés issus d'un message déclenché par un événement.

Consultez les [Étiquettes de personnalisation prises en charge]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/) pour obtenir la liste complète des étiquettes Liquid prises en charge.

### Comment affecter des variables avec Liquid ?

Vous pouvez créer et affecter des variables en utilisant l'étiquette `assign`. Cela crée une variable dans le composeur de messages qui peut également être référencée dans l'ensemble de votre message.

### L'utilisation de Liquid consomme-t-elle des points de donnée ?

Non.

### Comment utiliser Liquid pour envoyer un message d'accueil personnalisé ?

Pour un message d'accueil personnalisé utilisant le prénom de l'utilisateur, vous pouvez extraire les attributs standard du profil utilisateur tels que {% raw %} `{{${first_name}}}`, `{{${last_name}}}`.

Vous pouvez également utiliser une instruction Liquid `{% if X %}` {% endraw %} pour effectuer un rendu conditionnel basé sur n'importe quel critère, comme le jour de la semaine ou des attributs personnalisés. Pour plus d'informations sur les opérateurs Liquid pris en charge dans les instructions conditionnelles, consultez [Opérateurs]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/operators/).

### Comment personnaliser un message en fonction de la localisation d'un client ?

{% raw %}
Il existe un attribut par défaut pour la localisation de l'utilisateur : `{{${most_recent_location}}}`.

### Quelle est la différence entre {{campaign.${name}}} et {{campaign.${message_name}}} ?

`{{campaign.${name}}}` et `{{campaign.${message_name}}}` sont toutes deux des étiquettes de personnalisation Liquid prises en charge. Ces deux étiquettes font référence aux attributs de la campagne. `{{campaign.${name}}}` désigne le nom de votre campagne, et `{{campaign.${message_name}}}` est le nom de votre variante de message.
{% endraw %}

### Comment utiliser Liquid avec des objets imbriqués ?

Braze dispose d'une fonctionnalité intégrée qui génère du code Liquid pour les segments pouvant être utilisés dans un message. Plus précisément, vous pouvez créer un segment correspondant à plusieurs critères au sein d'un objet.

Pour plus d'informations, consultez [Segmentation multicritères]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support/#multi-criteria-segmentation).

### Comment utiliser les propriétés d'événement pour personnaliser un message déclenché par un événement ?

{% raw %}
Vous pouvez accéder aux propriétés des événements déclenchés par API avec l'étiquette `api_triggered_property` : `{{api_trigger_properties.${attribute_key}}}`.
{% endraw %}

### Qu'est-ce que la logique d'abandon et comment l'utiliser ?

La logique d'abandon vous permet d'empêcher l'envoi d'un message si les conditions sont remplies. Cela est particulièrement utile pour éviter d'envoyer des messages incomplets à vos utilisateurs. Pour des exemples de logique d'abandon dans vos campagnes marketing, consultez [Abandon de messages]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/).

### Qu'est-ce que la logique de boucle for et comment l'utiliser ?

Les boucles for sont également connues sous le nom d'[étiquettes d'itération](https://shopify.github.io/liquid/tags/iteration/). L'utilisation de la logique de boucle for dans vos extraits de code Liquid vous permet de parcourir des blocs Liquid jusqu'à ce qu'une condition soit remplie.

Dans Braze, cela peut être utilisé pour vérifier des éléments dans un attribut personnalisé de type tableau, ou une liste de valeurs et d'objets renvoyés par un appel de [catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/), de [sélection]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) ou de [Contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/). Plus précisément, vous pouvez utiliser la logique de boucle for dans vos messages pour vérifier si un produit est en stock ou s'il a une note minimale.

Par exemple, supposons que vous ayez un catalogue appelé « Games » avec une sélection appelée « cheap_games ». Pour extraire les titres des jeux dans « cheap_games », vous pouvez utiliser cet extrait de code Liquid :

{% raw %}
```liquid
{% catalog_selection_items Games cheap_games %}
{% for item in items %}
 Get this game: {{ item.title }}
{% endfor %}
```
{% endraw %}

Une fois les conditions définies remplies, votre message peut être envoyé. Cette logique est un moyen pratique de gagner du temps, plutôt que de répéter des blocs Liquid pour différentes conditions.

### Pourquoi y a-t-il des espaces supplémentaires dans les messages utilisant des Blocs de contenu ?

Si vous remarquez des espaces supplémentaires dans les messages envoyés qui utilisent des Blocs de contenu avec Liquid, il se peut que vous ayez des sauts de paragraphe ou de ligne inutiles dans vos instructions conditionnelles. Écrivez vos instructions conditionnelles sur une seule ligne plutôt que sur plusieurs lignes.

#### Exemple

{% raw %}
```liquid
{% if {{custom_attribute.${has_discount}}} == true %}Discounted Item{% elsif {{custom_attribute.${is_new_arrival}}} == true %}New Arrival{% else %}Regular Item{% endif %}
{% endraw %}

### When should I use `assign` versus `capture`?

Both `assign` and `capture` create Liquid variables, but they serve different purposes:

- `assign` is for simple variables that store a single value, such as a boolean, number, or simple string. You can also apply a single filter in the same line.
- `capture` is for storing a block of text that may include multiple variables, strings, or complex expressions. Use `capture` when the value is too complex for a single `assign` statement, such as URLs that utilize other Liquid variables or custom attributes as parameters. `capture` is also preferred when implementing Liquid variables in the body of Connected Content calls.

#### Examples

{% raw %}
```liquid
{% comment %} Valid assign usage {% endcomment %}
{% assign name = {{custom_attribute.${first_name}}} %}
{% assign price = {{custom_attribute.${price}}} | plus: 0 %}

{% comment %} Use capture for complex strings {% endcomment %}
{% capture greeting %}Hello, {{custom_attribute.${first_name}}}! Your order #{{custom_attribute.${order_id}}} is ready.{% endcapture %}
{{ greeting }}
```
{% endraw %}