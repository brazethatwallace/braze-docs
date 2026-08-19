---
nav_title: Faire correspondre des éléments de catalogue à un tableau d'attributs
article_title: Faire correspondre des éléments de catalogue à un tableau d'attributs personnalisés
page_order: 2
page_type: reference
description: "Utilisez une sélection de catalogue et Liquid pour afficher les lignes de catalogue dont les noms ou les ID apparaissent dans un tableau d'attributs personnalisés, comme une liste de souhaits."
---

# Faire correspondre des éléments de catalogue à un tableau d'attributs personnalisés {#match-catalog-items-to-a-custom-attribute-array}

> Lorsque chaque utilisateur conserve une liste de noms de produits enregistrés sur son profil, utilisez une sélection de catalogue combinée à Liquid pour n'afficher que les lignes de catalogue présentes dans cette liste, par exemple dans un e-mail de liste de souhaits.

## À propos de cet exemple {#about-this-example}

Flash & Thread stocke les noms de produits enregistrés de chaque client dans un attribut personnalisé de type tableau de chaînes de caractères (`saved_product_names`). Leur catalogue contient les détails complets des produits (catégorie, prix, URL de l'image, inventaire).

Les sélections de catalogue peuvent filtrer les colonnes d'un catalogue par rapport à des valeurs statiques ou Liquid, y compris les champs de type tableau sur les lignes du catalogue. Elles ne filtrent pas une ligne de catalogue par rapport aux valeurs stockées dans un tableau du profil utilisateur. Pour personnaliser à partir de la liste de l'utilisateur, renvoyez un ensemble large d'éléments de catalogue avec une sélection, puis utilisez Liquid pour ne conserver que les lignes correspondant au tableau du profil.

Ce modèle :

1. Assigne le tableau d'attributs personnalisés de l'utilisateur à une variable Liquid.
2. Appelle `catalog_selection_items` pour une sélection de catalogue pré-filtrée (jusqu'à 50 éléments).
3. Boucle sur `items` et utilise `contains` pour faire correspondre chaque champ du catalogue (par exemple, `name` ou `id`) avec le tableau.

{% alert important %}
Ce modèle ne fonctionne que lorsque l'ensemble de résultats de la sélection (jusqu'à 50 lignes de catalogue) peut raisonnablement contenir les éléments enregistrés de chaque utilisateur, par exemple pour de petits catalogues ou des catalogues dont les filtres restreignent suffisamment la sélection pour couvrir une liste typique. Si les éléments enregistrés d'un utilisateur se trouvent en dehors des 50 lignes renvoyées, la boucle ne trouve aucune correspondance et le message n'affiche rien pour ces éléments — aucun filtre ne résout ce problème dans le cas général, car la sélection ne peut pas effectuer de correspondance avec le tableau du profil de l'utilisateur.
{% endalert %}

## Considérations {#considerations}

- Testez le Liquid et les données de catalogue dans un espace de travail de staging avant d'envoyer aux clients.
- Comme une sélection renvoie au maximum 50 lignes de catalogue, ajoutez des filtres (par exemple, en stock, catégorie active ou tranche de prix) qui maintiennent les éléments enregistrés probables de chaque utilisateur dans cet ensemble de résultats.
- Cet exemple utilise un tableau de chaînes de caractères sur le profil utilisateur.
- Pour un tableau d'objets, effectuez la correspondance sur une propriété à l'intérieur de chaque objet (par exemple, `product_id`) et ajustez la vérification `contains` ou utilisez une boucle `for` sur les objets. Voir [Tableau d'objets]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects).
- Le comportement de `contains` dépend du type d'attribut ; pour les tableaux, utilisez `contains` plutôt que `==`. Voir [Logique conditionnelle]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic).
- Effectuez la correspondance sur des identifiants stables (par exemple, l'`id` du catalogue) lorsque les noms de produits peuvent changer ou être dupliqués.
- Les extraits de code Liquid de cet article sont des exemples. Validez le rendu dans vos canaux (HTML d'e-mail, notification push, etc.).

## Configuration {#setup}

Cet exemple suppose :

| Ressource | Détails |
| --- | --- |
| Attribut personnalisé | `saved_product_names` — tableau de chaînes de caractères (par exemple, `["linen_shirt", "trail_jacket", "canvas_tote"]`) |
| Catalogue | `apparel_products` avec les colonnes `id`, `category`, `name`, `price`, `inventory`, `image_url` |
| Sélection | `in_stock_apparel` sur `apparel_products`, limite de résultats 50, avec des filtres excluant les lignes non pertinentes (par exemple, `inventory` supérieur à `0`) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configuration" }

### Étape 1 : Créer le catalogue et la sélection {#step-1-create-the-catalog-and-selection}

1. Importez ou synchronisez les lignes de produits dans un catalogue nommé `apparel_products`.
2. Créez une sélection (par exemple, `in_stock_apparel`) qui renvoie autant de lignes pertinentes que nécessaire, jusqu'à la limite de 50 éléments.
3. Ajoutez des filtres de sélection pour exclure les lignes que vous ne souhaitez jamais voir dans le message (rupture de stock, mauvaise catégorie, etc.).

Pour la configuration des sélections, voir [Sélections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections).

### Étape 2 : Ajouter du Liquid dans votre message {#step-2-add-liquid-in-your-message}

Assignez le tableau du profil, chargez la sélection et bouclez avec `contains` :

{% raw %}
```liquid
{% assign saved_product_names = custom_attribute.${saved_product_names} %}
{% catalog_selection_items apparel_products in_stock_apparel %}
{% for item in items %}
{% if saved_product_names contains item.name %}
Product: {{ item.name }}
Category: {{ item.category }}
Price: ${{ item.price }}
Image: {{ item.image_url }}
{% endif %}
{% endfor %}
```
{% endraw %}

Remplacez `item.name` par `item.id` (ou une autre colonne) si votre tableau stocke des ID au lieu de noms d'affichage. Ajoutez des espaces ou du HTML entre les champs selon votre canal. Dans {% raw %}`${{ item.price }}`{% endraw %}, le `$` est un symbole monétaire littéral qui s'affiche avant la sortie Liquid — il ne fait pas partie de la syntaxe de personnalisation {% raw %}`${}`{% endraw %} de Braze.

Pour générer ce Liquid automatiquement, ouvrez la fenêtre modale **Ajouter une personnalisation** (**Éléments de catalogue** > **Utiliser une sélection**). Voir [Utiliser les catalogues]({{site.baseurl}}/user_guide/data/activation/catalogs/use).

### Étape 3 : Prévisualiser et tester {#step-3-preview-and-test}

Envoyez des messages de test à des profils avec différentes valeurs de `saved_product_names`. Confirmez que seules les lignes de catalogue correspondantes apparaissent et qu'un tableau vide ne produit aucune ligne de produit.

## Articles connexes {#related-articles}

- [Catalogues]({{site.baseurl}}/user_guide/data/activation/catalogs)
- [Sélections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)
- [Utiliser les catalogues]({{site.baseurl}}/user_guide/data/activation/catalogs/use)
- [Attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)
- [Logique conditionnelle]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic)
- [Bibliothèque de cas d'usage Liquid — trouver une chaîne de caractères dans un tableau]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases#misc-string-in-array)