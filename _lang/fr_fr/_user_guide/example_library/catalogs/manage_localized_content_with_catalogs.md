---
nav_title: Contenu de catalogue localisé
article_title: Gérer le contenu localisé avec les catalogues Braze
page_order: 3
page_type: reference
description: "Stockez les textes, prix et URL d'images localisés dans les catalogues Braze et résolvez la bonne langue au moment de l'envoi."
---

# Gérer le contenu localisé avec les catalogues Braze {#manage-localized-content-with-braze-catalogs}

> Stockez les chaînes de caractères et les URL localisées dans des catalogues pour que chaque utilisateur reçoive le contenu dans sa langue à partir d'une seule Campaign ou d'un seul Canvas, sans créer de variantes séparées par langue.

## À propos de cet exemple {#about-this-example}

PantsLabyrinth, un détaillant de vêtements fictif, vend ses produits en Amérique du Nord et en Europe. Les noms de produits, les prix et les images principales varient selon la langue, mais l'équipe marketing souhaite un seul modèle d'e-mail ou de notification push qui se personnalise au moment de l'envoi.

Cet exemple couvre trois modèles de catalogue qui lisent l'[attribut standard]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) {% raw %}`${language}`{% endraw %} de l'utilisateur (collecté par le SDK à partir de la langue de l'appareil) :

- Champs d'objet JSON : toutes les langues dans une seule ligne par élément
- Colonnes plates par langue : `header_en`, `header_fr`, etc.
- Catalogue séparé par langue : nom de catalogue dynamique tel que `pantslabyrinth-promo-en`

Utilisez les catalogues lorsque le contenu localisé est constitué de données structurées (produits, promotions, URL d'images). Pour le contenu libre dans les e-mails ou les notifications push, préférez les [messages multilingues]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) lorsque vos canaux les prennent en charge. Pour comparer les modèles de localisation de manière plus générale, consultez [Gestion des traductions]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#translation-management).

## Points à considérer {#considerations}

- Les exemples sont illustratifs. Vérifiez la casse et le format de {% raw %}`${language}`{% endraw %} dans votre base d'utilisateurs avant de nommer les clés ou suffixes de catalogue.
- Pour les méthodes 1 et 2, si {% raw %}`${language}`{% endraw %} est vide ou ne correspond à aucune clé ou champ du catalogue, le contenu localisé peut être vide — vérifiez chaque champ indépendamment et utilisez une valeur par défaut (par exemple l'anglais).
- Pour la méthode 3, autorisez uniquement les codes de langue pris en charge avant de construire le nom du catalogue ; un catalogue manquant annule le message.
- Les [objets JSON]({{site.baseurl}}/user_guide/data/activation/catalogs/create#supported-data-types) dans les catalogues peuvent être créés ou mis à jour via l'API ou l'[ingestion de données cloud (CDI) pour les catalogues]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data), et non via un import CSV.
- La méthode 2 prend en charge la maintenance par CSV mais multiplie les colonnes à mesure que les langues s'ajoutent. Les fichiers CSV prennent en charge jusqu'à [1 000 colonnes]({{site.baseurl}}/user_guide/data/activation/catalogs/create#step-1-review-your-csv-file).
- La méthode 3 nécessite un catalogue pour chaque code de langue qui atteint la balise `catalog_items`. Si le catalogue n'existe pas, Braze annule le message. Un ID d'élément manquant dans un catalogue existant renvoie un tableau d'éléments vide.
- Les balises Liquid de catalogue ne peuvent pas être utilisées de manière [récursive]({{site.baseurl}}/user_guide/data/activation/catalogs/use#using-liquid).
- Les [sélections de catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) prennent en charge jusqu'à 10 filtres et renvoient jusqu'à 50 éléments — validez les filtres par rapport au schéma de votre catalogue.
- Consultez les [niveaux de stockage des catalogues]({{site.baseurl}}/user_guide/data/activation/catalogs/create#tiers) si vous gérez de grands flux de produits multilingues.

## Configuration {#setup}

### Étape 1 : Choisir une structure de catalogue {#step-1-choose-a-catalog-structure}

Choisissez une structure de catalogue en vous appuyant sur les indications de ce tableau.

| Méthode | Idéale quand | Compromis |
| --- | --- | --- |
| Champs d'objet JSON | Catalogue de taille moyenne ; une ligne par élément ; mises à jour via API ou CDI | Ajouter une langue met à jour chaque élément via l'API ; pas de CSV pour les champs JSON |
| Champs plats par langue | Peu de langues et de champs ; les équipes non techniques utilisent le CSV | Chaque nouvelle langue ajoute des colonnes ; la nomenclature des champs doit rester cohérente |
| Catalogue par langue | Grands flux par langue ou propriétaires de langues séparés ; CSV par langue | Chaque code de langue autorisé nécessite un catalogue ; les catalogues manquants annulent l'envoi |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Choisir une structure de catalogue" }

### Étape 2 : Créer le catalogue et les éléments {#step-2-create-the-catalog-and-items}

1. Accédez à **Data Settings** > **Catalogs** et créez un catalogue (ou plusieurs catalogues pour la méthode 3).
2. Ajoutez des champs et des éléments en fonction de la structure choisie. Consultez [Créer un catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/create).
3. (Facultatif) Créez une [sélection de catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) pour filtrer les éléments — par exemple par `category` correspondant à un attribut personnalisé de l'utilisateur.

{% tabs local %}
{% tab Méthode 1 : Champs JSON %}
Exemple d'élément dans le catalogue `PantsLabyrinth_Product_Copy` :

| Élément | Valeur |
| --- | --- |
| `id` | `trail-runner-001` |
| `name` | `{"EN":"Trail Runner","FR":"Chaussure de trail","DE":"Trailrunner"}` |
| `category` | `footwear` |
| `url` | `https://pantslabyrinth.shop/products/trail-runner-001` |
| `price` | `{"EN":"$120 USD","FR":"112 EUR","DE":"112 EUR"}` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Exemple d'élément de catalogue avec des champs JSON par langue" }

{% endtab %}
{% tab Méthode 2 : Champs plats %}
Exemple d'élément dans le catalogue `PantsLabyrinth_Promo_Copy` :

| Élément | Valeur |
| --- | --- |
| `id` | `spring-sale` |
| `header_en` | `Spring trail sale` |
| `header_fr` | `Soldes de printemps` |
| `body_en` | `Save on trail runners this week.` |
| `body_fr` | `Économisez sur les chaussures de trail cette semaine.` |
| `cta_text_en` | `Shop now` |
| `cta_text_fr` | `Acheter` |
| `img_src_en` | `https://cdn.pantslabyrinth.shop/en/spring.jpg` |
| `img_src_fr` | `https://cdn.pantslabyrinth.shop/fr/spring.jpg` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Exemple d'élément de catalogue avec des champs plats par langue" }

{% endtab %}
{% tab Méthode 3 : Catalogue par langue %}
Créez un catalogue par langue avec les mêmes champs. Par exemple, répétez le même `id` et les mêmes champs dans `pantslabyrinth-promo-fr` et `pantslabyrinth-promo-de` avec des valeurs localisées.

Exemple d'élément dans `pantslabyrinth-promo-en` :

| Élément | Valeur |
| --- | --- |
| `id` | `spring-sale` |
| `header` | `Spring trail sale` |
| `body` | `Save on trail runners this week.` |
| `cta_text` | `Shop now` |
| `img_src` | `https://cdn.pantslabyrinth.shop/en/spring.jpg` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Exemple d'élément dans un catalogue anglais par langue" }

{% endtab %}
{% endtabs %}

### Étape 3 : Ajouter le Liquid à votre message {#step-3-add-liquid-to-your-message}

Sélectionnez le modèle Liquid correspondant à la structure de catalogue que vous avez choisie à l'étape 1.

{% tabs local %}
{% tab Méthode 1 : Champs JSON %}
Stockez toutes les langues dans des champs d'objet JSON sur une seule ligne de catalogue, puis utilisez le filtre `property_accessor` pour lire les clés `name` et `price` correspondant à {% raw %}`${language}`{% endraw %} (normalisé en majuscules). Vérifiez chaque champ indépendamment et utilisez `EN` par défaut lorsque ce champ est vide, de sorte qu'une langue avec un nom mais sans prix affiche quand même un prix en anglais.

{% raw %}
```liquid
{% catalog_items PantsLabyrinth_Product_Copy trail-runner-001 %}
{% assign lang = ${language} | upcase %}
{% assign localized_name = items[0].name | property_accessor: lang %}
{% assign localized_price = items[0].price | property_accessor: lang %}
{% if localized_name == blank %}
  {% assign localized_name = items[0].name | property_accessor: 'EN' %}
{% endif %}
{% if localized_price == blank %}
  {% assign localized_price = items[0].price | property_accessor: 'EN' %}
{% endif %}
Product: {{ localized_name }}
Price: {{ localized_price }}
```
{% endraw %}

Consultez [Filtre property accessor]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters#property-accessor-filter).
{% endtab %}
{% tab Méthode 2 : Champs plats %}
Construisez des noms de champs dynamiques à partir de {% raw %}`${language}`{% endraw %} (normalisé en minuscules), puis lisez ces champs dans l'élément avec une recherche par crochets. Par exemple, {% raw %}`items[0][header_field]`{% endraw %} lit l'en-tête pour la langue résolue. Vérifiez chaque champ indépendamment et utilisez la colonne anglaise par défaut lorsque ce champ est vide, de sorte qu'une langue avec un en-tête mais sans corps reçoit quand même le texte du corps en anglais.

{% raw %}
```liquid
{% catalog_items PantsLabyrinth_Promo_Copy spring-sale %}
{% assign lang = ${language} | downcase %}
{% assign header_field = 'header_' | append: lang %}
{% assign body_field = 'body_' | append: lang %}
{% assign cta_field = 'cta_text_' | append: lang %}
{% assign img_field = 'img_src_' | append: lang %}
{% assign header_val = items[0][header_field] %}
{% assign body_val = items[0][body_field] %}
{% assign cta_val = items[0][cta_field] %}
{% assign img_val = items[0][img_field] %}
{% if header_val == blank %}
  {% assign header_val = items[0].header_en %}
{% endif %}
{% if body_val == blank %}
  {% assign body_val = items[0].body_en %}
{% endif %}
{% if cta_val == blank %}
  {% assign cta_val = items[0].cta_text_en %}
{% endif %}
{% if img_val == blank %}
  {% assign img_val = items[0].img_src_en %}
{% endif %}
<img src="{{ img_val }}" alt="" />
<h2>{{ header_val }}</h2>
<p>{{ body_val }}</p>
<a href="#">{{ cta_val }}</a>
```
{% endraw %}
{% endtab %}
{% tab Méthode 3 : Catalogue par langue %}
{% alert warning %}
Si le nom de catalogue que vous transmettez à `catalog_items` n'existe pas, Braze annule le message. Autorisez uniquement les codes de langue pris en charge avant de construire le nom du catalogue. Un ID d'élément manquant dans un catalogue existant renvoie un tableau d'éléments vide — vous pouvez utiliser le catalogue anglais comme solution de repli dans ce cas uniquement.
{% endalert %}

Autorisez les codes de langue qui possèdent des catalogues correspondants (ici `en`, `fr` et `de`), attribuez les valeurs non prises en charge ou vides à `en` par défaut, puis recherchez l'élément. Si l'ID de l'élément est manquant dans ce catalogue, utilisez le catalogue anglais comme solution de repli.

{% raw %}
```liquid
{% assign lang = ${language} | downcase %}
{% assign supported = 'en,fr,de' | split: ',' %}
{% if supported contains lang %}{% else %}{% assign lang = 'en' %}{% endif %}
{% assign theCatalog = 'pantslabyrinth-promo-' | append: lang %}
{% catalog_items {{ theCatalog }} spring-sale %}
{% if items[0] == blank %}
  {% catalog_items pantslabyrinth-promo-en spring-sale %}
{% endif %}
<img src="{{ items[0].img_src }}" alt="" />
<h2>{{ items[0].header }}</h2>
<p>{{ items[0].body }}</p>
<a href="#">{{ items[0].cta_text }}</a>
```
{% endraw %}

Consultez [Utiliser des modèles dans les noms de catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/create#template-catalog-names) et [Annuler des messages]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages).
{% endtab %}
{% endtabs %}

#### Sélection de catalogue facultative par catégorie {#optional-catalog-selection-by-category}

Filtrez les éléments avant la personnalisation — par exemple les promotions de chaussures pour les utilisateurs ayant `preferred_category = footwear` :

{% raw %}
```liquid
{% catalog_selection_items PantsLabyrinth_Product_Copy footwear_promos %}
{% for item in items %}
  {{ item.name }}
{% endfor %}
```
{% endraw %}

Définissez la sélection dans le tableau de bord avec des filtres sur votre colonne `category` et des attributs utilisateur selon vos besoins.

### Étape 4 : Prévisualiser et tester {#step-4-preview-and-test}

1. Utilisez **Preview as User** avec des profils utilisateur ayant différentes valeurs de {% raw %}`${language}`{% endraw %}.
2. Vérifiez le contenu de repli lorsque la langue est manquante ou non prise en charge, y compris les localisations partielles (par exemple un nom sans prix).
3. Pour la méthode 3, confirmez que chaque langue autorisée dispose d'un catalogue correspondant, et que les codes de langue non pris en charge sont redirigés vers votre catalogue par défaut sans annuler l'envoi.

## Articles connexes {#related-articles}

- [Catalogues]({{site.baseurl}}/user_guide/data/activation/catalogs)
- [Utiliser les catalogues]({{site.baseurl}}/user_guide/data/activation/catalogs/use)
- [Sélections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)
- [Créer un catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/create)
- [Filtres Liquid avancés]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters#property-accessor-filter)
- [Localisation]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization)
- [Messages multilingues]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)
- [Synchroniser et supprimer les données de catalogue]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)
- [Annuler des messages Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages)