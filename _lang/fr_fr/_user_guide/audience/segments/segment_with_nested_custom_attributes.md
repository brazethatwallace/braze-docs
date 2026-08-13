---
nav_title: "Cas d'utilisation : Attributs personnalisés imbriqués"
article_title: "Cas d'utilisation : Segmenter avec des attributs personnalisés imbriqués"
page_order: 10
page_type: tutorial
tool: Segments
description: "Créez des segments à l'aide d'attributs personnalisés imbriqués : le filtre Attributs personnalisés imbriqués, les chemins et comparateurs, les filtres temporels, la segmentation multicritère, la génération de schéma et l'explorateur d'objets imbriqués."
---

# Cas d'utilisation : Segmenter avec des attributs personnalisés imbriqués {#use-case-segment-with-nested-custom-attributes}

> Ces cas d'utilisation montrent comment segmenter les utilisateurs avec des attributs personnalisés imbriqués dans Braze, et contiennent des exemples de JSON et de workflows dans le tableau de bord que vous pouvez adapter à vos propres données.

Imaginons que vous faites partie de l'équipe marketing d'une application de streaming musical et que vous souhaitez envoyer des messages en fonction des attributs personnalisés imbriqués d'un utilisateur, tels que des objets de compte avec des soldes et des types. Ces cas d'utilisation présentent différentes façons dont votre équipe peut utiliser les attributs personnalisés imbriqués dans les segments, et vous apprennent à :

- Configurer un filtre de segment d'attribut personnalisé imbriqué, valider les chemins et choisir des comparateurs correspondant au type de données de chaque propriété.
- Savoir quand utiliser les opérateurs **Day of Year** par rapport aux opérateurs **Time** pour les valeurs de date imbriquées, et comment la **segmentation multicritère** fait correspondre les utilisateurs lorsqu'au moins un objet dans un tableau répond à tous les critères listés.
- Générer un schéma pour un objet ou un tableau d'objets, l'explorer dans le tableau de bord et finaliser un segment (par exemple, les utilisateurs avec un solde inférieur à 100) en utilisant le sélecteur de chemin au lieu de saisir les chemins de mémoire.

## Filtrer par attributs personnalisés imbriqués {#filter-by-nested-custom-attributes}

Créons un segment basé sur un attribut personnalisé imbriqué pour cibler les utilisateurs qui ont écouté leur chanson la plus jouée plus de 300 fois.

### Étape 1 : Ajouter le filtre {#step-1-add-the-filter}

Sélectionnez le filtre **Nested Custom Attributes** pour afficher un menu déroulant dans lequel vous pouvez sélectionner un attribut personnalisé imbriqué spécifique. Nous sélectionnerons `most_played_song`, qui contient les données sur la chanson la plus jouée d'un utilisateur.

### Étape 2 : Sélectionner la propriété {#step-2-select-the-property}

Sélectionnez la **propriété** au sein de l'attribut personnalisé imbriqué par laquelle vous souhaitez filtrer. Nous sélectionnerons `play_analytics.count`, qui suit le nombre de fois qu'un utilisateur a écouté sa chanson la plus jouée.

### Étape 3 : Sélectionner une comparaison et une valeur d'attribut personnalisé imbriqué {#step-3-select-a-comparison-and-nested-custom-attribute-value}

Lorsque vous filtrez par attributs personnalisés imbriqués, le type de données de votre propriété détermine les comparateurs disponibles pour le filtrage. Par exemple, comme `play_analytics.count` est un nombre, vous pouvez sélectionner un comparateur dans la catégorie **Number**.

Pour filtrer les utilisateurs qui ont écouté leur chanson la plus jouée au moins 300 fois, sélectionnez la comparaison **More than**, puis saisissez « 300 » comme valeur.

![Un utilisateur choisissant un opérateur en fonction du type de données de l'attribut personnalisé imbriqué]({% image_buster /assets/img_archive/nca_comparator.png %})

## Filtrer les types de données temporelles {#filter-for-time-data-types}

Lorsque vous filtrez un attribut personnalisé imbriqué de type temporel, vous pouvez choisir de filtrer avec des opérateurs sous les catégories **Jour de l'année** ou **Heure** lors de la comparaison de la valeur de date.

Si vous sélectionnez un opérateur sous la catégorie **Jour de l'année**, seuls le mois et le jour sont vérifiés pour la comparaison, au lieu de l'horodatage complet de la valeur de l'attribut personnalisé imbriqué. La sélection d'un opérateur sous la catégorie **Heure** compare l'horodatage complet, y compris l'année.

{% alert note %}
Lorsque vous utilisez des opérateurs **Heure** qui prennent en charge les unités de jours et de semaines (tels que **est supérieur à**, **est inférieur à**, **exactement** et **après**), Braze convertit automatiquement la valeur en semaines lorsque vous enregistrez le Segment. Par exemple, 91 jours sont convertis en 13 semaines. Les unités de jours et de semaines sont toutes deux prises en charge pour ces filtres.
{% endalert %}

## Utiliser la segmentation multicritère {#use-multi-criteria-segmentation}

Utilisez la **segmentation multicritère** pour créer un segment qui correspond à plusieurs critères au sein d'un même objet. Cela qualifie l'utilisateur dans le segment s'il possède au moins un objet dans le tableau qui correspond à tous les critères spécifiés. Par exemple, les utilisateurs ne correspondent à ce segment que si leur clé n'est pas vide et si leur nombre est supérieur à 0.

### Copier le Liquid pour le segment {#copy-liquid-for-segment}

Vous pouvez également utiliser la fonctionnalité **Copy Liquid for segment** pour générer du code Liquid pour ce segment et l'utiliser dans un message. Par exemple, supposons que vous ayez un tableau d'objets de comptes et un segment qui cible les clients possédant des comptes imposables actifs. Pour inciter les clients à contribuer à l'objectif de compte associé à l'un de leurs comptes actifs et imposables, vous souhaiterez créer un message pour les encourager.

![Un exemple de segment avec la case cochée pour la segmentation multicritère.]({% image_buster /assets/img_archive/nca_multi_criteria.png %})

Lorsque vous sélectionnez **Copy Liquid for segment**, Braze génère automatiquement du code Liquid qui renvoie un tableau d'objets contenant uniquement les comptes actifs et imposables.

{% raw %}

```
{% assign segmented_nested_objects = '' | split: '' %}
{% assign obj_array = {{custom_attribute.${accounts}}} %}
{% for obj in obj_array %}
  {% if obj["account_type"] == 'taxable' and obj["active"] == true %}
    {% assign segmented_nested_objects = obj_array | slice: forloop.index0 | concat: segmented_nested_objects | reverse %}
  {% endif %}
{% endfor %}
```

À partir de là, vous pouvez utiliser `segmented_nested_objects` et personnaliser votre message. Dans cet exemple, nous souhaitons récupérer un objectif du premier compte imposable actif et le personnaliser :

```
Get to your {{segmented_nested_objects[0].goal}} goal faster, make a deposit using our new fast deposit feature!
```

{% endraw %}

Cela renvoie le message suivant à votre client : « Get to your retirement goal faster, make a deposit using our new fast deposit feature! »

## Générer un schéma à l'aide de l'explorateur d'objets imbriqués {#generate-schema}

Vous pouvez générer un schéma pour vos objets afin de créer des filtres de segment sans avoir besoin de mémoriser les chemins d'objets imbriqués.

### Étape 1 : Générer un schéma {#step-1-generate-a-schema}

Par exemple, supposons que nous avons un tableau d'objets `accounts` que nous venons d'envoyer à Braze :

```json
{"accounts": [
  {"type": "taxable",
  "balance": 22500,
  "active": true},
  {"type": "non-taxable",
  "balance": 0,
  "active": true}
]}
```

Dans le tableau de bord de Braze, accédez à **Data Settings** > **Custom Attributes**.

Recherchez votre objet ou tableau d'objets. Dans la colonne **Attribute Name**, sélectionnez **Generate Schema**.

![Une liste d'attributs personnalisés avec une option pour générer le schéma de l'attribut accounts.]({% image_buster /assets/img_archive/nca_generate_schema.png %})

{% alert tip %}
La génération de votre schéma peut prendre quelques minutes en fonction de la quantité de données que vous nous avez envoyées.
{% endalert %}

Une fois le schéma généré, un nouveau bouton <i class="fas fa-plus"></i> plus apparaît à la place du bouton **Generate Schema**. Vous pouvez cliquer dessus pour voir ce que Braze sait de cet attribut personnalisé imbriqué.

Lors de la génération du schéma, Braze examine les données précédemment envoyées et construit une représentation idéale de vos données pour cet attribut. Braze analyse également et ajoute un type de données pour vos valeurs imbriquées. Cela est réalisé en échantillonnant les données précédemment envoyées à Braze pour l'attribut imbriqué donné.

Pour notre tableau d'objets `accounts`, vous pouvez voir qu'au sein du tableau d'objets, il y a un objet contenant les éléments suivants :

- Un type booléen avec une clé `active` (que le compte soit actif ou non)
- Un type nombre avec une clé `balance` (montant du solde du compte)
- Un type chaîne de caractères avec une clé `type` (compte non imposable ou imposable)

![Schéma du tableau d'objets accounts avec trois valeurs imbriquées : active, balance et type.]({% image_buster /assets/img_archive/nca_schema.png %}){: style="max-width:70%" }

Maintenant que nous avons analysé et construit une représentation des données, créons un segment.

### Étape 2 : Créer un segment {#step-2-build-a-segment}

Ciblons les clients qui ont un solde inférieur à 100 afin de leur envoyer un message les encourageant à effectuer un dépôt.

Créez un segment et ajoutez le filtre `Nested Custom Attribute`, puis recherchez et sélectionnez votre objet ou tableau d'objets. Ici, nous avons ajouté le tableau d'objets `accounts`.

![Filtrage d'attribut personnalisé imbriqué pour le tableau d'objets accounts.]({% image_buster /assets/img_archive/nca_segment_schema.png %})

Sélectionnez le bouton <i class="fas fa-plus"></i> plus dans le champ de chemin. Cela ouvre une représentation de votre objet ou tableau d'objets. Vous pouvez sélectionner n'importe quel élément listé et Braze l'insère dans le champ de chemin pour vous. Dans cet exemple, nous devons obtenir le solde. Sélectionnez le solde comme chemin (dans ce cas, `[].balance`) qui est automatiquement renseigné dans le champ de chemin.

![Schéma accounts avec une liste de chemins consultable.]({% image_buster /assets/img_archive/nca_segment_schema2.png %}){: style="max-width:70%" }

Sélectionnez **less than** comme comparateur, puis saisissez « 100 » comme valeur de solde.

![Un filtre pour les utilisateurs avec un solde de compte inférieur à 100.]({% image_buster /assets/img_archive/nca_segment_schema_3.png %})

Et voilà ! Vous venez de créer un segment à l'aide d'un attribut personnalisé imbriqué, le tout sans avoir besoin de connaître la structure des données. L'explorateur d'objets imbriqués de Braze a généré une représentation visuelle de vos données et vous a permis d'explorer et de sélectionner exactement ce dont vous aviez besoin pour créer un segment.