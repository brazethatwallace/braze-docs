---
nav_title: Catalogue
article_title: Catalogue
page_order: 2
description: "Découvrez comment utiliser les catalogues comme source de données pour personnaliser vos messages Braze avec des données non liées aux utilisateurs, telles que les détails produits, les flux de contenu et les tarifs."
---

# Catalogue {#catalog}

> Référencez des données non liées aux utilisateurs dans vos messages en vous connectant aux catalogues. Les catalogues stockent des jeux de données structurés — tels que des informations produits, des listes de restaurants ou des flux de contenu — auxquels vous pouvez accéder via Liquid pour personnaliser n'importe quel message.

## Fonctionnement {#how-it-works}

{% raw %}
Après avoir importé des données dans un catalogue (via CSV ou API), référencez les éléments du catalogue dans vos messages à l'aide de l'étiquette Liquid `items`. Par exemple, pour extraire le nom d'un produit d'un catalogue appelé `products` :

```liquid
{% catalog_items products {{${product_id}}} %}
{{items[0].name}} is back in stock!
```
{% endraw %}

Les catalogues prennent en charge jusqu'à 1 000 champs par élément et peuvent stocker des millions de lignes, ce qui les rend adaptés aux grands inventaires de produits et aux bibliothèques de contenu.

## Cas d'utilisation courants {#common-use-cases}

| Cas d'utilisation | Description |
| --- | --- |
| Détails produits | Insérez des noms, descriptions, prix et images à partir d'un catalogue de produits |
| Listes de restaurants ou de magasins | Personnalisez les messages avec des détails propres à un emplacement |
| Recommandations de contenu | Référencez des articles, vidéos ou autres éléments multimédias |
| Informations sur les événements | Intégrez des dates d'événements, des lieux et des descriptions dans les messages |
| Offres par niveau | Associez des promotions au niveau d'adhésion ou au segment d'un utilisateur |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cas d'utilisation courants" }

## Déclencheurs de catalogue {#catalog-triggers}

Les catalogues permettent également l'envoi de messages automatisés grâce aux déclencheurs de catalogue. Configurez des notifications de retour en stock et des notifications de baisse de prix pour envoyer automatiquement des messages aux utilisateurs lorsque les éléments du catalogue changent.

Pour en savoir plus, consultez [Déclencheurs de catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers).

## Sélections {#selections}

Utilisez les sélections pour regrouper les éléments d'un catalogue selon des filtres que vous définissez. Par exemple, créez une sélection d'articles à moins de 20 $ ou d'articles dans une catégorie spécifique, puis référencez l'ensemble filtré dans vos messages.

Pour en savoir plus, consultez [Sélections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections).

## Pour commencer {#getting-started}

Pour créer et gérer des catalogues, consultez [Catalogues]({{site.baseurl}}/user_guide/data/activation/catalogs). Pour apprendre à référencer les données d'un catalogue dans vos messages, consultez [Utiliser les catalogues dans un message]({{site.baseurl}}/user_guide/data/activation/catalogs/use).