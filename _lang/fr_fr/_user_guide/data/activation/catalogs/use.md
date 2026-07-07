---
nav_title: Utilisation des catalogues
article_title: Utiliser les catalogues
page_order: 1.5
description: "Cet article de référence explique comment utiliser les catalogues pour référencer des données non-utilisateurs dans vos campagnes Braze via Liquid."
---

# Utilisation des catalogues {#using-catalogs}

> Après avoir créé un catalogue, vous pouvez référencer des données non-utilisateurs dans vos campagnes Braze via [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid). Les catalogues sont utilisables dans tous vos canaux de communication, y compris partout dans l'éditeur par glisser-déposer où Liquid est pris en charge.

## Utiliser des catalogues dans un message {#using-catalogs-in-a-message}

La vidéo suivante explique comment utiliser les catalogues dans un message.

{% multi_lang_include video.html id="4yc2jkyn6w" source="wistia" %}

### Étape 1 : Ajouter un type de personnalisation {#step-one-personalization}

Dans l'éditeur de message de votre choix, sélectionnez <i class="fas fa-plus-circle"></i> **Add Personalization** et sélectionnez **Catalog Items** pour le **Personalization type**. Sélectionnez ensuite le nom de votre catalogue. En reprenant l'exemple précédent, nous allons sélectionner le catalogue « Games ».

![Fenêtre modale Add Personalization avec Catalog Items sélectionné, le catalogue Games choisi et un aperçu Liquid affichant la balise catalog_items.]({% image_buster /assets/img_archive/use_catalog_personalization.png %})

Nous pouvons immédiatement voir l'aperçu Liquid suivant :

{% raw %}
```liquid
{% catalog_items Games %}
```
{% endraw %}

### Étape 2 : Sélectionner les éléments du catalogue {#step-2-select-catalog-items}

Il est maintenant temps d'ajouter vos éléments de catalogue ! À l'aide de la liste déroulante, sélectionnez les éléments du catalogue et les informations à afficher. Ces informations correspondent aux colonnes du fichier CSV importé utilisé pour générer votre catalogue.

Par exemple, pour référencer le titre et le prix de notre jeu Tales, nous pouvons sélectionner l'`id` de Tales (1234) comme élément du catalogue et demander `title` et `price` pour les informations affichées.

{% raw %}
```liquid
{% catalog_items Games 1234 %}

Get {{ items[0].title }} for just {{ items[0].price }}!
```
{% endraw %}

Ceci donne le résultat suivant :

> Get Tales for just 7.49!

## Exporter des catalogues {#exporting-catalogs}

Vous pouvez exporter des catalogues depuis le tableau de bord de deux manières :

- Survolez la ligne du catalogue dans la section **Catalogs**. Sélectionnez ensuite le bouton **Export catalog**.
- Sélectionnez votre catalogue. Ensuite, sélectionnez le bouton **Export catalog** dans l'onglet **Preview** du catalogue.

Vous recevrez un e-mail pour télécharger le fichier CSV après avoir lancé l'exportation. Vous disposerez de quatre heures pour récupérer ce fichier.

## Cas d'utilisation supplémentaires {#additional-use-cases}

### Plusieurs éléments {#multiple-items}

Vous n'êtes pas limité à un seul élément par message. Utilisez la fenêtre modale **Add Personalization** pour ajouter jusqu'à trois éléments du catalogue à la fois. Pour en ajouter davantage, sélectionnez à nouveau **Add Personalization** dans l'éditeur, puis choisissez les éléments supplémentaires du catalogue et les informations à afficher.

Dans cet exemple, nous ajoutons l'`id` de trois jeux — Tales, Teslagrad et Acaratus — pour **Catalog Items** et nous sélectionnons `title` pour **Information to Display**.

![Fenêtre modale Add Personalization affichant trois ID d'éléments de catalogue sélectionnés et title choisi pour Information to Display, avec un aperçu Liquid listant le titre de chaque élément.]({% image_buster /assets/img_archive/catalog_multiple_items.png %}){: style="max-width:70%" }

Nous pouvons personnaliser davantage notre message en ajoutant du texte autour de notre Liquid :

{% raw %}
```liquid
Get the ultimate trio {% catalog_items Games 1234 1235 1236 %}
{{ items[0].title }}, {{ items[1].title }}, and {{ items[2].title }} today!
```
{% endraw %}

Ceci donne le résultat suivant :

```Get the ultimate trio Tales, Teslagrad, and Acaratus today!```

{% alert tip %}
Check out [selections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) to create groups of data for more personalized messaging!
{% endalert %}

### Using Liquid `if` statements

You can use catalog items to create conditional statements. For example, you can trigger a certain message to display when a specific item is selected in your campaign. You must declare the catalog (and, if applicable, the selection) before referencing `items` in an `if` statement.

#### With catalog items

{% raw %}
```liquid
{% catalog_items Games 1234 %}
{% if items[0].on_sale == true %}
  {{ items[0].title }} is on sale! Get it for {{ items[0].price }}.
{% else %}
  Check out {{ items[0].title }} at full price.
{% endif %}
```
{% endraw %}

Dans cet exemple, la balise `catalog_items` récupère l'élément `1234` du catalogue `Games`, puis l'instruction `if` vérifie le champ `on_sale` pour afficher différents messages.

#### Avec des sélections de catalogue

{% raw %}
```liquid
{% catalog_selection_items item-list selections %}
{% if items[0].venue_name.size > 10 %}
Message if the venue name's size is more than 10 characters.
{% elsif items[0].venue_name.size <= 10 %}
Message if the venue name's size is 10 characters or fewer.
{% else %}
{% abort_message('no venue_name') %}
{% endif %}
```
{% endraw %}

Dans cet exemple, différents messages s'affichent selon que le champ `venue_name` contient plus ou moins de 10 caractères. Si `venue_name` est vide, le message est interrompu.

Pour afficher le nombre d'éléments renvoyés par une sélection, utilisez le filtre Liquid `size` sur le tableau `items` après la balise, et non sur un champ individuel :

{% raw %}
```liquid
{% catalog_selection_items item-list selections %}{{ items | size }}
```
{% endraw %}

{% alert tip %}
Pour éviter les erreurs de syntaxe Liquid, sélectionnez le bouton **+** dans l'éditeur de message pour insérer automatiquement les balises Liquid de catalogue.
{% endalert %}

### Utiliser des images {#using-images}

Vous pouvez également référencer des images du catalogue pour les utiliser dans vos messages. Pour ce faire, utilisez la balise `catalogs` et l'objet `item` dans le champ Liquid pour les images.

Par exemple, pour ajouter le `image_link` de notre catalogue Games à notre message promotionnel pour Tales, sélectionnez l'`id` pour le champ **Catalog Items** et `image_link` pour le champ **Information to Display**. Ceci ajoute les balises Liquid suivantes à notre champ d'image :

{% raw %}
```liquid
{% catalog_items Games 1234 %}

{{ items[0].image_link }}
```
{% endraw %}

![Éditeur de carte de contenu avec une balise Liquid de catalogue utilisée dans le champ d'image.]({% image_buster /assets/img_archive/catalog_image_link1.png %})

Voici à quoi cela ressemble une fois le Liquid rendu :

![Exemple de carte de contenu avec rendu des balises Liquid du catalogue.]({% image_buster /assets/img_archive/catalog_image_link2.png %}){: style="max-width:50%" }

{% alert important %}
Dans les canaux **HTML** tels que l'e-mail, évitez les espaces ou sauts de ligne supplémentaires entre la balise de fermeture `{% raw %}{% catalog_items ... %}{% endraw %}` et le Liquid qui affiche l'URL de l'image (par exemple, `{% raw %}{{ items[0].image_link }}{% endraw %}`). Les espaces supplémentaires dans le modèle peuvent empêcher la résolution correcte de l'URL de l'image dans le message rendu. Gardez l'expression d'URL immédiatement adjacente à la balise du catalogue, comme ceci : `{% raw %}<img src="{% catalog_items Games 1234 %}{{ items[0].image_link }}">{% endraw %}`.
{% endalert %}

### Modèles d'éléments de catalogue

Vous pouvez également utiliser les modèles pour extraire dynamiquement des éléments du catalogue en fonction d'attributs personnalisés. Par exemple, imaginons qu'un utilisateur possède l'attribut personnalisé `wishlist`, qui contient un tableau d'ID de jeux de votre catalogue.

```json
{
    "attributes": [
        {
            "external_id": "user_id",
            "wishlist": ["1234", "1235"]
        }
    ]
}
```

{% alert note %}
Les objets JSON dans les catalogues ne sont ingérés que via l'API. Vous ne pouvez pas importer un objet JSON à l'aide d'un fichier CSV.
{% endalert %}

Grâce au modèle Liquid, vous pouvez extraire dynamiquement les ID de la liste de souhaits, puis les utiliser dans votre message. Pour ce faire, [affectez une variable]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#assigning-variables) à votre attribut personnalisé, puis utilisez la fenêtre modale **Add Personalization** pour extraire un élément spécifique du tableau. Les variables référencées comme ID d'élément du catalogue doivent être placées entre accolades pour être correctement référencées, comme `{{result}}`.

{% alert tip %}
N'oubliez pas que les tableaux commencent à `0` et non à `1`.
{% endalert %}

Par exemple, pour informer un utilisateur que Tales (un élément de notre catalogue qu'il a ajouté à ses souhaits) est en promotion, nous pouvons ajouter ce qui suit à notre éditeur de message :

{% raw %}
```liquid
{% assign wishlist = {{custom_attribute.${wishlist}}}%}
{% catalog_items Games {{ wishlist[0] }} %}

Get {{ items[0].title }} now for {{ items[0].price }}!
```
{% endraw %}

Ce qui s'affichera comme suit :
> Get Tales now for just 7.49!

Avec les modèles, vous pouvez afficher un élément du catalogue différent pour chaque utilisateur en fonction de ses attributs personnalisés, de ses propriétés d'événement ou de tout autre champ modélisable.

### Importer un CSV

Vous pouvez importer un fichier CSV contenant de nouveaux éléments de catalogue à ajouter ou des éléments existants à mettre à jour. Pour supprimer une liste d'éléments, vous pouvez importer un CSV d'ID d'éléments à supprimer.

### Utiliser Liquid

Vous pouvez également composer manuellement des catalogues avec la logique Liquid. Notez cependant que si vous saisissez un ID qui n'existe pas, Braze renverra tout de même un tableau d'éléments sans objet. Nous vous recommandons d'inclure une gestion des erreurs, comme la vérification de la taille du tableau et l'utilisation d'une instruction `if` pour gérer le cas d'un tableau vide.

#### Modélisation d'éléments de catalogue incluant du Liquid

Tout comme pour le [Contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), vous devez utiliser le drapeau `:rerender` dans une balise Liquid pour afficher le contenu Liquid d'un élément du catalogue. Notez que le drapeau `:rerender` ne s'applique qu'à un seul niveau de profondeur : il ne s'appliquera pas aux appels de balises Liquid imbriquées.

Si un élément du catalogue contient des champs de profil utilisateur (dans une balise de personnalisation Liquid), ces valeurs doivent être définies en Liquid plus tôt dans le message, avant la modélisation, afin de garantir le bon rendu du Liquid. Si le drapeau `:rerender` n'est pas fourni, le contenu Liquid brut sera restitué.

Par exemple, si un catalogue nommé « Messages » possède un élément avec ce Liquid :

![Ligne de tableau du catalogue avec l'id greet_msg et une colonne Welcome_Message contenant un message de bienvenue avec une variable Liquid pour le prénom.]({% image_buster /assets/img_archive/catalog_liquid_templating.png %}){: style="max-width:80%;"}

Pour rendre le contenu Liquid suivant :

{% raw %}
```liquid
Hi ${first_name},

{% catalog_items Messages greet_msg :rerender %}
{{ items[0].Welcome_Message }}
```
{% endraw %}

L'affichage sera le suivant :

{% raw %}
```
Hi Peter,

Welcome to our store, Peter!
```
{% endraw %}

{% alert note %}
Les balises Liquid des catalogues ne peuvent pas être utilisées de manière récursive à l'intérieur des catalogues.
{% endalert %}

## Résolution des problèmes de personnalisation des catalogues

Si le Liquid d'un catalogue ou d'une sélection ne s'affiche pas comme prévu dans un message ou une étape Canvas, vérifiez les points suivants :

| Symptôme | Ce qu'il faut vérifier |
| --- | --- |
| L'aperçu affiche les éléments mais les envois en production sont vides | Confirmez que les **ID d'éléments** du catalogue existent au moment de l'envoi. Si l'ID dans votre Liquid ne correspond à aucune ligne, Braze renvoie un tableau d'éléments vide — voir [Utiliser Liquid](#using-liquid). Vérifiez les fautes de frappe et les sources d'ID (telles que les propriétés d'événement) qui pourraient être absentes du déclencheur ou du profil utilisateur. |
| L'aperçu de l'éditeur fonctionne dans une Campaign mais pas dans Canvas | Confirmez que vous utilisez le bon contexte Liquid — **propriétés de contexte Canvas** versus **propriétés d'événement** — et que ces champs existent sur le déclencheur. Voir [Propriétés de contexte et d'événement]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties). |
| Une sélection ne renvoie aucun élément | Vérifiez les [filtres de sélection]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) et les limites ; confirmez que les données du catalogue sont synchronisées et que les noms de colonnes correspondent à vos filtres. |
| `:rerender` ou la distribution modélisée semble incorrecte | Pour le Liquid imbriqué dans les champs du catalogue, vous avez besoin de `:rerender` et d'un ordonnancement correct des variables — voir [Modélisation d'éléments de catalogue incluant du Liquid](#templating-catalog-items-including-liquid). Les messages in-app modélisés sont résolus au moment du déclenchement ; voir [Que sont les messages in-app modélisés ?]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#what-are-templated-in-app-messages). Certains canaux restreignent les balises de catalogue (par exemple, certaines utilisations de **:rerender** avec les bannières) — voir [Toutes les balises Liquid sont-elles prises en charge ?]({{site.baseurl}}/user_guide/channels/banners/faq#are-all-liquid-tags-supported) dans la FAQ des bannières. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Résolution des problèmes de personnalisation des catalogues" }

Pour le comportement général de Liquid, voir [Cas d'utilisation Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases) et [Utiliser Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid).

## Structurer les données de votre catalogue

Lorsque vous planifiez la structure des données de votre catalogue, partez de votre cas d'utilisation et concevez le catalogue en conséquence. Chaque ligne du catalogue représente un élément (avec un `id` unique). Les colonnes doivent contenir les attributs de cet élément, tels que les URL, le texte descriptif, les URL d'images, le prix, la note, la taille ou la couleur.

### Quand utiliser les appels de catalogue standard

Avec les appels de catalogue standard, vous faites correspondre une valeur à la colonne `id`. En insérant un attribut personnalisé ou une propriété d'événement (sous forme de chaîne de caractères d'ID) dans la balise Liquid du catalogue, vous pouvez récupérer plusieurs attributs d'un même élément dans votre message. Les cas d'utilisation courants incluent :

- Produit ou service récemment consulté
- Éléments de la liste de souhaits
- Offres par emplacement
- Produit acheté
- Contenu lié à l'étape du cycle de vie
- Produit ou service recherché le plus récemment

### Quand utiliser les sélections de catalogue

Les [sélections de catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) vous permettent de filtrer sur n'importe quelle colonne de votre catalogue et de renvoyer jusqu'à 50 éléments correspondants. En insérant des attributs personnalisés ou des propriétés d'événement dans les filtres de sélection, les résultats sont personnalisés pour chaque utilisateur. Les cas d'utilisation courants incluent :

- Éléments dont la catégorie correspond aux préférences de l'utilisateur
- Éléments correspondant à la marque, la cuisine ou la taille préférée de l'utilisateur
- Contenu lié au type d'abonnement ou au niveau de fidélité
- Produits dans la fourchette de valeur moyenne de commande de l'utilisateur

La différence principale est que les appels de catalogue standard recherchent un seul élément connu par `id`, tandis que les sélections de catalogue interrogent l'ensemble du catalogue et renvoient plusieurs éléments correspondant à vos critères de filtre.

[1]: {% image_buster /assets/img_archive/use_catalog_personalization.png %}
[2]: {% image_buster /assets/img_archive/catalog_multiple_items.png %}