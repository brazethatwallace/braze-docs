---
nav_title: Sélections
article_title: Sélections
page_order: 5
alias: /catalog_selections/
description: "Cet article de référence explique comment créer et utiliser des sélections avec vos catalogues pour référencer des données dans vos campagnes Braze."
---

# Sélections {#selections}

> Cette page explique comment créer et utiliser des sélections avec vos [catalogues]({{site.baseurl}}/user_guide/data/activation/catalogs/).

## Fonctionnement {#how-it-works}

Les sélections sont des groupes de données qui permettent de personnaliser un message pour chaque utilisateur de votre campagne. Lorsque vous utilisez une sélection, vous configurez essentiellement des filtres personnalisés basés sur des colonnes spécifiques de votre catalogue. Il peut s'agir de filtres pour la marque, la taille, l'emplacement, la date d'ajout, etc. Cela vous donne le contrôle sur ce que vous montrez aux utilisateurs en vous permettant de définir des critères auxquels les éléments doivent répondre au préalable.

Après avoir créé un catalogue, vous pouvez référencer davantage les données de votre catalogue en incorporant des sélections dans vos Campaigns ou recommandations Braze.

![La section Sélections dans un exemple de catalogue.]({% image_buster /assets/img_archive/catalog_selections1.png %})

## Bon à savoir {#things-to-know}

- Vous pouvez créer jusqu'à 30 sélections par catalogue.
- Vous pouvez ajouter jusqu'à 10 filtres par sélection.
- Les sélections sont idéales pour affiner les recommandations à partir des données de catalogue Braze. Si vous cherchez de l'inspiration, consultez [À propos des recommandations d'articles]({{site.baseurl}}/user_guide/brazeai/item_recommendations/) pour des exemples de cas d'utilisation.

## Opérateurs pris en charge {#supported-operators}

Lors de la création d'un filtre de sélection, les opérateurs disponibles dépendent du type de champ que vous sélectionnez.

| Type de champ | Opérateurs disponibles |
| --- | --- |
| Chaîne de caractères | `equals`, `does not equal`, `is any of`, `is none of` |
| Nombre | `equals`, `does not equal`, `greater than`, `less than` |
| Valeur booléenne | `is` |
| Heure | `before`, `after` |
| Tableau | `includes value`, `does not include value` |
| Géo | `geo within`, `geo outside` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Supported operators" }

Les opérateurs `is any of` et `is none of` sont disponibles pour les champs de type chaîne de caractères et prennent chacun en charge jusqu'à 10 valeurs.

## Créer une sélection {#creating-a-selection}

Pour créer une sélection, procédez comme suit.

1. Allez dans **Catalogs** et sélectionnez votre catalogue dans la liste.
2. Sélectionnez l'onglet **Selection** et cliquez sur **Create Selection**.
3. Donnez un nom à votre sélection et, éventuellement, une description.
4. Dans le champ **Filter Field**, sélectionnez la colonne du catalogue sur laquelle vous souhaitez filtrer. Les champs de type chaîne de caractères de plus de 1 000 caractères ne peuvent pas être sélectionnés pour les filtres.
5. Terminez la définition de vos critères de filtrage en sélectionnant l'opérateur et l'attribut appropriés. Pour une liste complète des opérateurs par type de champ, consultez [Opérateurs pris en charge](#supported-operators).
6. Dans la section **Sort type**, déterminez comment les résultats sont triés. Par défaut, les résultats sont renvoyés sans ordre particulier. Pour spécifier un tri sur un champ spécifique, désactivez l'option **Randomize Sort Order** et précisez le **Sort Field** et l'ordre de tri (**Sort Order** : croissant ou décroissant).
7. Dans la section **Results limit**, saisissez le nombre de résultats (jusqu'à 50).
8. Sélectionnez **Create Selection**.

### Test et prévisualisation {#test-and-preview}

Après avoir créé une sélection, vous pouvez utiliser la section **Preview for user** pour voir ce qu'une sélection renverrait pour un utilisateur aléatoire ou un utilisateur spécifique. Pour les sélections qui utilisent la personnalisation, vous ne pouvez voir la prévisualisation qu'après avoir sélectionné un utilisateur.

### Liquid dans les résultats de la sélection {#liquid-in-selection-results}

L'utilisation de Liquid dans les catalogues, comme les attributs personnalisés et les événements personnalisés, peut donner lieu à des résultats différents pour chaque utilisateur de votre sélection.

{% alert note %}
Le Liquid de Contenu connecté n'est pas pris en charge dans ces paramètres de filtrage.
{% endalert %}

![Paramètres de filtrage pour la sélection du catalogue lorsque l'attribut est défini sur un attribut personnalisé Liquid.]({% image_buster /assets/img_archive/catalog_selections7.png %})

## Utiliser des sélections dans l'envoi de messages {#using-selections-in-messaging}

Après avoir créé votre sélection, personnalisez vos messages avec Liquid pour insérer les éléments filtrés de ce catalogue. Vous pouvez demander à Braze de générer le Liquid pour vous à partir de la fenêtre de personnalisation disponible dans les éditeurs de messages :

1. Dans tout éditeur de messages prenant en charge la personnalisation, sélectionnez <i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="Ajouter une personnalisation"></i> pour ouvrir la fenêtre de personnalisation.
2. Pour **Personalization Type**, sélectionnez **Catalog Items**.
3. Sélectionnez le nom de votre catalogue.
4. Pour **Item selection method**, sélectionnez **Use a selection**.
4. Sélectionnez votre sélection dans la liste.
5. Pour **Information to Display**, sélectionnez les champs du catalogue à inclure pour chaque article.
6. Sélectionnez l'icône **Copy** et collez le Liquid à l'endroit voulu dans votre message.

![La fenêtre modale Add Personalization avec les sélections suivantes : « Catalog Items » pour « Personalization Type », « Games » pour « Catalog Name », « Selections » pour « Selection Type », « game_selection » pour « Selection », et « title » et « description_en » pour « Information to Display ».]({% image_buster /assets/img_archive/catalog_selections6.png %}){: style="max-width:70%;"}

## Cas d'utilisation {#use-case}

Imaginons que vous possédiez un service de livraison de repas et que vous souhaitiez envoyer un message personnalisé à vos utilisateurs ayant des préférences alimentaires spécifiques, basées sur la catégorie de nourriture qu'ils ont consultée le plus récemment.

En utilisant un catalogue contenant les informations de votre service de livraison (nom du repas, prix, image et catégorie), vous pouvez créer une sélection pour recommander trois repas en fonction de la catégorie la plus récemment consultée par un utilisateur.

![Un exemple de sélection pour un service de livraison de repas avec deux filtres : un qui identifie un type de produit comme étant un repas, et un autre qui identifie la catégorie la plus récemment consultée. La sélection est configurée pour rendre aléatoire l'ordre dans lequel les trois résultats sont renvoyés.]({% image_buster /assets/img_archive/catalog_selections2.png %}){: style="max-width:90%;"}

Pour utiliser ce catalogue et cette sélection dans une campagne, utilisez la fenêtre modale **Add Personalization** dans la section de composition des messages lors de la création d'une campagne. Dans cet exemple, nous avons sélectionné le catalogue contenant les informations de votre service de livraison de repas, ainsi que la sélection pour les recommandations de repas basées sur la catégorie consultée le plus récemment. Cela nous permet d'afficher le nom du repas et son prix. Pour enrichir davantage votre message, vous pouvez utiliser la sélection pour ajouter également une image du premier repas recommandé.

![Une carte de contenu avec l'en-tête « You will LOVE these highly rated meals! » avec la sélection « recommendations_be_recent_category » dans la section de composition du message.]({% image_buster /assets/img_archive/catalog_selections3.png %}){: style="max-width:90%;"}

Par exemple, imaginons un utilisateur dont la catégorie consultée le plus récemment est « Chicken ». En utilisant la personnalisation définie et une campagne de cartes de contenu, vous pouvez envoyer trois recommandations de repas incluant du poulet à cet utilisateur.

![Une carte de contenu avec une image de poulet au citron grillé et une liste de trois recommandations de repas incluant du poulet, basées sur la dernière catégorie consultée par l'utilisateur.]({% image_buster /assets/img_archive/catalog_selections4.png %}){: style="max-width:90%;"}

En utilisant la même personnalisation, vous pouvez également envoyer trois recommandations de repas à un utilisateur dont la catégorie la plus récemment consultée est « Beef ».

![Une carte de contenu avec une image de bœuf stroganoff et une liste de deux recommandations de repas incluant du bœuf, basées sur la catégorie la plus récemment consultée par l'utilisateur.]({% image_buster /assets/img_archive/catalog_selections5.png %}){: style="max-width:90%;"}