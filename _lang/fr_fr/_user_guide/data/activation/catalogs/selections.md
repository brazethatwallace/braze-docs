---
nav_title: Sélections
article_title: Sélections
page_order: 5
alias: /catalog_selections/
description: "Cet article de référence explique comment créer et utiliser des sélections avec vos catalogues pour référencer des données dans vos Campaigns Braze."
---

# Sélections {#selections}

> Les sélections sont des groupes de données que vous pouvez utiliser pour personnaliser un message pour chaque utilisateur de votre Campaign. Lorsque vous utilisez une sélection, vous configurez essentiellement des filtres personnalisés basés sur des colonnes spécifiques de votre catalogue. Il peut s'agir de filtres pour la marque, la taille, l'emplacement, la date d'ajout, etc. Cela vous donne le contrôle sur ce que vous montrez aux utilisateurs en vous permettant de définir des critères auxquels les éléments doivent répondre au préalable.<br><br>Cette page explique comment créer et utiliser des sélections avec vos catalogues.

Après avoir créé un [catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs), vous pouvez référencer davantage les données de votre catalogue en incorporant des sélections dans vos Campaigns ou recommandations Braze.

![La section Sélections dans un exemple de catalogue.]({% image_buster /assets/img_archive/catalog_selections1.png %})

## Ce qu'il faut savoir {#things-to-know}

- Vous pouvez créer jusqu'à 30 sélections par catalogue.
- Vous pouvez ajouter jusqu'à 10 filtres par sélection.
- Les sélections sont idéales pour affiner les recommandations à partir des données de catalogue Braze. Si vous cherchez de l'inspiration, consultez [À propos des recommandations d'articles]({{site.baseurl}}/user_guide/brazeai/recommendations) pour des exemples de cas d'usage.

## Filtres de géolocalisation {#geolocation-filters}

Si votre catalogue inclut un [type de champ Géolocalisation]({{site.baseurl}}/user_guide/data/activation/catalogs/create#supported-data-types), vous pouvez utiliser des filtres basés sur la géolocalisation dans vos sélections pour afficher les éléments du catalogue en fonction de leur proximité par rapport à un point géographique.

Deux opérateurs de géolocalisation sont disponibles :

| Opérateur | Description |
| -------- | ----------- |
| `geo within` | Renvoie les éléments dont le champ de géolocalisation se trouve dans un rayon spécifié autour d'un point central. |
| `geo outside` | Renvoie les éléments dont le champ de géolocalisation se trouve en dehors d'un rayon spécifié autour d'un point central. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Lorsqu'un filtre de géolocalisation est appliqué, les résultats sont triés par distance, l'élément le plus proche apparaissant en premier.

### Définir le point central avec Liquid {#setting-the-center-point-with-liquid}

Vous pouvez définir le point central de manière dynamique à l'aide de Liquid. Par exemple, pour filtrer les éléments par rapport à la localisation la plus récente de chaque utilisateur, utilisez l'attribut {% raw %}`{{${most_recent_location}}}`{% endraw %} comme valeur de filtre :

{% raw %}
```
{{${most_recent_location}}}
```
{% endraw %}

### Cas d'usage : afficher les emplacements de magasins les plus proches {#use-case-show-the-nearest-store-locations}

Supposons que votre catalogue contienne un champ `store_location` de type Géolocalisation. Vous pouvez créer une sélection qui utilise l'opérateur `geo within` pour renvoyer les emplacements de magasins situés dans un rayon défini autour de la localisation la plus récente de chaque utilisateur. Définissez la valeur du filtre sur {% raw %}`{{${most_recent_location}}}`{% endraw %} afin que le point central soit mis à jour pour chaque utilisateur. Comme les résultats sont triés par distance, le premier élément renvoyé est toujours le magasin le plus proche.

## Créer une sélection {#creating-a-selection}

Pour créer une sélection, procédez comme suit.

1. Accédez à **Catalogs** et sélectionnez votre catalogue dans la liste.
2. Sélectionnez l'onglet **Selection** et cliquez sur **Create Selection**.
3. Donnez un nom à votre sélection et ajoutez une description facultative.
4. Pour **Filter Field**, sélectionnez la colonne du catalogue par laquelle vous souhaitez filtrer. Les champs de type chaîne de caractères comportant plus de 1 000 caractères ne peuvent pas être sélectionnés comme filtres.
5. Terminez la définition de vos critères de filtre en sélectionnant l'opérateur pertinent (par exemple, « est égal à » ou « n'est pas égal à ») et l'attribut.
6. Dans la section **Sort type**, déterminez comment les résultats sont triés. Par défaut, les résultats sont renvoyés sans ordre particulier. Pour spécifier un tri par un champ spécifique, désactivez **Randomize Sort Order** et précisez le **Sort Field** et le **Sort Order** (croissant ou décroissant).
7. Dans la section **Results limit**, saisissez la limite de résultats (jusqu'à 50).
8. Sélectionnez **Create Selection**.

### Tester et prévisualiser {#test-and-preview}

Après avoir créé une sélection, vous pouvez utiliser la section **Preview for user** pour visualiser ce qu'une sélection renverrait pour un utilisateur aléatoire ou un utilisateur spécifique. Pour les sélections qui utilisent la personnalisation, vous ne pouvez afficher l'aperçu qu'après avoir sélectionné un utilisateur.

### Liquid dans les résultats de sélection {#liquid-in-selection-results}

L'utilisation de Liquid dans les catalogues, comme les attributs personnalisés et les événements personnalisés, peut entraîner des résultats différents renvoyés pour chaque utilisateur dans votre sélection.

{% alert note %}
Le Liquid de contenu connecté n'est pas pris en charge dans ces paramètres de filtre.
{% endalert %}

![Paramètres de filtre pour la sélection de catalogue où l'attribut est défini sur un attribut personnalisé Liquid.]({% image_buster /assets/img_archive/catalog_selections7.png %})

## Utiliser les sélections dans la communication {#using-selections-in-messaging}

Après avoir créé votre sélection, personnalisez vos messages avec Liquid pour insérer les éléments filtrés de ce catalogue. Vous pouvez demander à Braze de générer le Liquid pour vous depuis la fenêtre de personnalisation disponible dans les éditeurs de messages :

1. Dans tout éditeur de messages prenant en charge la personnalisation, sélectionnez <i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="Ajouter une personnalisation"></i> **Ajouter une personnalisation** pour ouvrir la fenêtre de personnalisation.
2. Pour **Type de personnalisation**, sélectionnez **Catalog Items**.
3. Sélectionnez le nom de votre catalogue.
4. Pour **Méthode de sélection d'élément**, sélectionnez **Use a selection**.
4. Sélectionnez votre sélection dans la liste.
5. Pour **Informations à afficher**, sélectionnez les champs du catalogue à inclure pour chaque élément.
6. Sélectionnez l'icône **Copier** et collez le Liquid à l'endroit souhaité dans votre message.

![La fenêtre modale Ajouter une personnalisation avec les sélections suivantes : « Catalog Items » pour « Type de personnalisation », « Games » pour « Nom du catalogue », « Selections » pour « Type de sélection », « game_selection » pour « Sélection », et « title » et « description_en » pour « Informations à afficher ».]({% image_buster /assets/img_archive/catalog_selections6.png %}){: style="max-width:70%;"}

{% alert note %}
L'aperçu de personnalisation dans le panneau de composition Liquid affiche jusqu'à trois sélections de catalogue, quel que soit le nombre limite de résultats que vous avez défini. Il s'agit du comportement attendu : le message réellement envoyé aux utilisateurs respecte la limite de résultats que vous avez configurée.
{% endalert %}

## Cas d'usage {#use-case}

Imaginons que vous possédez un service de livraison de repas et que vous souhaitez envoyer un message personnalisé à vos utilisateurs ayant des préférences alimentaires spécifiques, basées sur la catégorie d'aliments qu'ils ont consultée le plus récemment.

En utilisant un catalogue contenant les informations de votre service de livraison de repas (nom du repas, prix, image et catégorie du repas), vous pouvez créer une sélection pour recommander trois repas en fonction de la catégorie la plus récemment consultée par l'utilisateur.

![Un exemple de sélection pour un service de livraison de repas avec deux filtres : l'un identifiant un type de produit comme un repas, et l'autre identifiant la catégorie comme la plus récemment consultée. La sélection est configurée pour randomiser l'ordre dans lequel les trois résultats sont renvoyés.]({% image_buster /assets/img_archive/catalog_selections2.png %}){: style="max-width:90%;"}

Pour utiliser ce catalogue et cette sélection dans une campagne, utilisez la fenêtre modale **Ajouter une personnalisation** dans la section de composition du message lors de la création d'une campagne. Dans cet exemple, nous avons sélectionné le catalogue contenant les informations de votre service de livraison de repas, ainsi que la sélection pour les recommandations de repas basées sur la catégorie la plus récemment consultée. Cela nous permet d'afficher le nom du repas et le prix. Pour enrichir davantage votre message, vous pouvez utiliser la sélection pour ajouter également une image du premier repas recommandé.

![Une Content Card avec l'en-tête « You will LOVE these highly rated meals! » avec la sélection « recommendations_be_recent_category » dans la section de composition du message.]({% image_buster /assets/img_archive/catalog_selections3.png %}){: style="max-width:90%;"}

Par exemple, imaginons que vous avez un utilisateur dont la catégorie la plus récemment consultée est « Poulet ». En utilisant la personnalisation configurée et une campagne de Content Card, vous pouvez envoyer trois recommandations de repas incluant du poulet pour cet utilisateur.

![Une Content Card avec une image de poulet grillé au citron, et une liste de trois recommandations de repas incluant du poulet basées sur la catégorie la plus récemment consultée par l'utilisateur.]({% image_buster /assets/img_archive/catalog_selections4.png %}){: style="max-width:90%;"}

En utilisant la même personnalisation, vous pouvez également envoyer trois recommandations de repas pour un utilisateur dont la catégorie la plus récemment consultée est « Bœuf ».

![Une Content Card avec une image de bœuf stroganoff, et une liste de deux recommandations de repas incluant du bœuf basées sur la catégorie la plus récemment consultée par l'utilisateur.]({% image_buster /assets/img_archive/catalog_selections5.png %}){: style="max-width:90%;"}