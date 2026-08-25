---
nav_title: Créer un catalogue
article_title: Créer un catalogue
alias: "/catalogs/"
page_order: 1
description: "Cet article de référence explique comment créer des catalogues qui référencent des données non-utilisateurs dans vos campagnes Braze via Liquid."
---

# Créer un catalogue {#create-a-catalog}

> La création d'un catalogue consiste à importer un fichier CSV de données non-utilisateurs dans Braze. Vous pouvez ensuite accéder à ces informations pour enrichir vos messages. N'importe quel type de données peut être intégré à un catalogue. Il s'agit généralement de métadonnées provenant de votre entreprise, comme des informations produits pour un site e-commerce ou des informations sur les cours pour un fournisseur de formation.

## Cas d'usage {#use-cases}

Les cas d'usage courants des catalogues comprennent :

- Produits
- Services
- Alimentation
- Événements à venir
- Musique
- Forfaits

Une fois ces informations importées, vous pouvez commencer à y accéder dans vos messages de manière similaire à l'accès aux attributs personnalisés ou aux propriétés d'événement personnalisé via Liquid.

## Types de données pris en charge {#supported-data-types}

Le tableau suivant répertorie les types de données de catalogue pris en charge et la manière dont ils peuvent être créés ou mis à jour.

| Type de données | Description | Disponible via import CSV | Disponible via API et CDI |
|--------------|-----------------------------------------------|:------------------------:|:-------------------------:|
| Chaîne de caractères | Une séquence de caractères. | ✅ Oui | ✅ Oui |
| Nombre | Une valeur numérique, entière ou décimale. | ✅ Oui | ✅ Oui |
| Valeur booléenne | Une valeur `true` ou `false`. | ✅ Oui | ✅ Oui |
| Date | Une chaîne de caractères au format [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). | ✅ Oui | ✅ Oui |
| Géolocalisation | Un tableau de coordonnées `[longitude, latitude]`. La latitude doit être comprise entre -90 et 90 ; la longitude doit être comprise entre -180 et 180. Par exemple, `[-73.988103, 40.779109]`. | ✅ Oui | ✅ Oui |
| Objet JSON | Un objet imbriqué avec des paires clé-valeur. Peut être affiché dans la plateforme, mais ne peut être créé ou mis à jour que via l'API ou le CDI. | ⛔ Non | ✅ Oui |
| Tableau de chaînes de caractères | Une liste de chaînes de caractères. Peut être affiché dans la plateforme, mais ne peut être créé ou mis à jour que via l'API ou le CDI. Maximum de 100 éléments. | ⛔ Non | ✅ Oui |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Créer un catalogue {#creating-a-catalog}

Pour créer un catalogue, accédez à **Paramètres des données** > **Catalogues**, puis sélectionnez **Créer un nouveau catalogue** et choisissez l'une des options suivantes :

{% tabs local %}
{% tab Upload CSV %}
### Étape 1 : Vérifier votre fichier CSV {#step-1-review-your-csv-file}

Avant d'importer votre fichier CSV, assurez-vous qu'il respecte les exigences suivantes :

| Exigence CSV | Détails |
|--------------|---------|
| En-têtes | La première colonne du fichier CSV doit s'appeler `id`, et chaque ligne doit avoir une valeur `id` unique. |
| Colonnes | Un fichier CSV peut contenir un maximum de 1 000 champs (colonnes), et chaque nom de colonne peut comporter jusqu'à 250 caractères. |
| Taille du fichier | Pour les forfaits Free, la taille totale de tous les fichiers CSV d'une entreprise est limitée à 500 Mo. Pour les forfaits Pro, la taille maximale d'un fichier CSV unique est de 2 Go. |
| Valeurs des champs | Chaque cellule (valeur de champ) peut contenir jusqu'à 5 000 caractères. |
| Caractères valides | La colonne `id` et toutes les valeurs d'en-tête ne peuvent contenir que des lettres, des chiffres, des tirets et des traits de soulignement. |
| Types de données | Les types de données pris en charge pour les importations CSV incluent string, number, boolean, time et geolocation. Pour la liste complète des types de données, y compris ceux disponibles uniquement via l'API et le CDI, consultez [Types de données pris en charge](#supported-data-types). |
| Formatage | Formatez tout le texte en minuscules pour maintenir la cohérence. |
| Encodage | Enregistrez et importez le fichier CSV en utilisant l'encodage UTF-8. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert note %}
Besoin de plus d'espace pour vos fichiers CSV ? Contactez votre gestionnaire de compte Braze pour en savoir plus sur la mise à niveau de vos catalogues.
{% endalert %}

### Étape 2 : Importer le CSV {#step-2-upload-csv}

Glissez-déposez votre fichier dans la zone d'importation, ou sélectionnez **Upload CSV** et choisissez votre fichier.

![Glissez-déposez votre fichier dans la zone d'importation, ou sélectionnez Upload CSV et choisissez votre fichier.]({% image_buster /assets/img_archive/catalog_CSV_upload.png %}){: style="max-width:80%;"}

Sélectionnez un type de données pour chaque colonne.

{% alert note %}
Ce type de données ne peut pas être modifié après la configuration de votre catalogue. De plus, une valeur `NULL` n'est pas prise en charge lors de l'importation CSV et sera traitée comme une chaîne de caractères.
{% endalert %}

![Ce type de données ne peut pas être modifié après la configuration de votre catalogue. De plus, une valeur NULL n'est pas prise en charge lors de l'importation CSV et sera traitée comme une chaîne de caractères.]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:80%;"}

Saisissez un nom et une description facultative pour votre catalogue. Gardez les exigences suivantes à l'esprit lorsque vous nommez votre catalogue :

  - Doit être unique
  - Maximum de 250 caractères
  - Ne peut contenir que des chiffres, des lettres, des tirets et des traits de soulignement

{% alert tip %}
Vous pouvez également [utiliser des modèles dans un nom de catalogue](#template-catalog-names), ce qui vous permet de générer dynamiquement des noms de catalogue basés sur des variables comme la langue ou la campagne.
{% endalert %}

![Un catalogue nommé « my_catalog ».]({% image_buster /assets/img_archive/in_browser_catalog.png %}){: style="max-width:80%;"}

Sélectionnez **Process Catalog** pour créer le catalogue.

{% alert important %}
Votre fichier CSV peut être rejeté si vous dépassez votre [niveau](#tiers).
{% endalert %}

### Tutoriel : Créer un catalogue à partir d'un fichier CSV {#tutorial-creating-a-catalog-from-a-csv-file}

Pour ce tutoriel, nous utilisons un catalogue qui répertorie deux jeux, leur prix et un lien vers une image.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg" aria-label="Tutoriel : Créer un catalogue à partir d'un fichier CSV">
<thead>
  <tr>
    <th class="tg-0pky">id</th>
    <th class="tg-0pky">title</th>
    <th class="tg-0pky">price</th>
    <th class="tg-0pky">image_link</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">1234</td>
    <td class="tg-0pky">Tales</td>
    <td class="tg-0pky">7.49</td>
    <td class="tg-0pky">https://picsum.photos/200</td>
  </tr>
  <tr>
    <td class="tg-0pky">1235</td>
    <td class="tg-0pky">Regeneration</td>
    <td class="tg-0pky">22.49</td>
    <td class="tg-0pky">https://picsum.photos/200</td>
  </tr>
</tbody>
</table>

Nous allons créer le catalogue en important un fichier CSV. Les types de données pour `id`, `title`, `price` et `image_link` sont respectivement string, string, number et string.

{% alert note %}
Ce type de données ne peut pas être modifié après la configuration de votre catalogue.
{% endalert %}

![Quatre noms de colonnes du catalogue : « id », « title », « price », « image_link ».]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:85%;"}

Ensuite, nous nommerons ce catalogue « games_catalog » et sélectionnerons le bouton **Process Catalog**. Braze vérifiera alors le catalogue pour détecter d'éventuelles erreurs avant la création du catalogue.

![Un catalogue nommé « games_catalog ».]({% image_buster /assets/img_archive/catalog_new_name.png %}){: style="max-width:85%;"}

Notez que vous ne pourrez pas modifier ce nom après la création du catalogue. Vous pouvez supprimer un catalogue et réimporter une version mise à jour en utilisant le même nom de catalogue.

Après avoir créé le catalogue, vous pouvez commencer à référencer le [catalogue dans une campagne]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs).

{% alert important %}
Les fichiers CSV précédemment importés sont disponibles au téléchargement depuis la page **Catalogues** pendant 30 jours après la date d'importation. Après 30 jours, le fichier est définitivement supprimé et ne peut plus être consulté.
{% endalert %}
{% endtab %}

{% tab Create in browser %}
### Prérequis {#prerequisites}

Avant de pouvoir modifier ou créer des catalogues dans le navigateur, vous avez besoin des [autorisations utilisateur]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) suivantes pour votre espace de travail :

- View Catalogs
- Edit Catalogs
- Export Catalogs
- Delete Catalogs

### Étape 1 : Saisir les détails du catalogue {#step-1-enter-catalog-details}

Saisissez un nom et une description facultative pour votre catalogue. Gardez les exigences suivantes à l'esprit lorsque vous nommez votre catalogue :

- Doit être unique
- Maximum de 250 caractères
- Ne peut contenir que des chiffres, des lettres, des tirets et des traits de soulignement

{% alert tip %}
Vous pouvez également [utiliser des modèles dans un nom de catalogue](#template-catalog-names), ce qui vous permet de générer dynamiquement des noms de catalogue basés sur des variables comme la langue ou la campagne.
{% endalert %}

![Un catalogue nommé « my_catalog ».]({% image_buster /assets/img_archive/in_browser_catalog.png %}){: style="max-width:80%;"}

### Étape 2 : Créer votre catalogue {#step-2-create-your-catalog}

Sélectionnez votre catalogue dans la liste, puis sélectionnez **Update Catalog** > **Add fields**. Saisissez le **nom du champ** et utilisez le menu déroulant pour sélectionner le type de données. Répétez l'opération autant de fois que nécessaire.

![Deux exemples de champs « rating » et « name ».]({% image_buster /assets/img_archive/add_catalog_fields.png %}){: style="max-width:50%;"}

Sélectionnez **Update Catalog** > **Add items** pour ajouter un élément à votre catalogue en saisissant les informations basées sur les champs que vous avez précédemment ajoutés. Ensuite, sélectionnez **Save Item** ou **Save and Add Another** pour continuer à ajouter vos éléments.

![Ajouter un élément au catalogue.]({% image_buster /assets/img_archive/add_catalog_items.png %}){: style="max-width:50%;"}

{% alert note %}
Braze traite les valeurs temporelles en fonction de l'horodatage du tableau de bord. Par exemple, si une colonne a la valeur « 03/13/2024 » et que votre fuseau horaire est le fuseau horaire du Pacifique, cette heure sera importée dans Braze comme « Mar 12, 2024, 5:00 PM ».
{% endalert %}
{% endtab %}
{% endtabs %}

## Types de données de catalogue {#catalog-data-types}

Les catalogues prennent en charge différents types de données pour vous aider à organiser et structurer efficacement vos données. Le tableau suivant décrit chaque type de données pris en charge et la correspondance avec les noms de types CSV et API :

| Type de données | Format | Exemple | Description |
|-----------|--------|---------|-------------|
| String | Texte | `"Hello World"` | Toute séquence de caractères utilisée pour des données textuelles comme les noms, descriptions et ID. Équivalent au type `string` dans les imports CSV et API. |
| Time | ISO 8601 ou horodatage Unix (secondes) | `"2024-03-15T14:30:00Z"` | Valeurs de date et d'heure formatées en ISO 8601 ou en horodatage Unix en secondes. Équivalent au type `time` dans l'API et au type `datetime` dans les imports CSV. |
| Boolean | `true` ou `false` | `true` | Valeurs logiques représentant les états vrai ou faux. Équivalent au type `boolean` dans les imports CSV et API. |
| Number | Entier ou décimal | `42` ou `19.99` | Valeurs numériques comprenant les entiers et les nombres à virgule flottante pour les prix, quantités, notes et plus encore. Équivalent aux types `integer` et `float` dans les imports CSV et au type `number` dans l'API. |
| Geolocation | Tableau `[longitude, latitude]` | `[-73.988103, 40.779109]` | Une paire de coordonnées représentant un emplacement géographique. La longitude doit être comprise entre -180 et 180 ; la latitude doit être comprise entre -90 et 90. La valeur `type` de l'API est `geo`. Peut être ajouté via le tiroir **Add Fields** dans l'interface des catalogues, par import CSV ou via la REST API. |
| Object | Objet JSON | `{"key": "value", "price": 10}` | Structures de données imbriquées complexes. La valeur `type` de l'API est `object`. Affiché comme JSON Object dans le tableau de bord. Disponible uniquement via l'API ou l'ingestion de données cloud (CDI). |
| Array | Tableau de chaînes de caractères | `["red", "blue", "green"]` | Listes de valeurs de chaînes de caractères. La valeur `type` de l'API est `array`. Affiché comme String array dans le tableau de bord. Disponible uniquement via l'API ou CDI. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

## Utilisation de modèles dans les noms de catalogues {#template-catalog-names}

Lorsque vous nommez votre catalogue, vous pouvez également utiliser des modèles dans le nom du catalogue. Cela vous permet de générer dynamiquement des noms de catalogues en fonction de variables telles que la langue ou la campagne. Par exemple :

{% raw %}
```liquid
{% assign language = "content_spanish" %}

{% catalog_items {{language}} fall_campaign %}
{{ items[0].body }}
```
{% endraw %}

## Gestion des catalogues {#managing-catalogs}

### Dans le tableau de bord {#in-the-dashboard}

Pour mettre à jour votre catalogue après avoir importé un fichier CSV ou créé un catalogue dans le navigateur, sélectionnez **Update Catalog > Upload CSV**, puis choisissez si vous souhaitez mettre à jour, ajouter ou supprimer des éléments dans votre catalogue.

### Utilisation de la REST API {#using-the-rest-api}

Au fur et à mesure que vous créez des catalogues, vous pouvez également utiliser l'[endpoint Lister les catalogues]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) pour obtenir la liste des catalogues d'un espace de travail.

La REST API prend en charge tous les [types de données de catalogue](#supported-data-types), y compris les objets JSON et les tableaux de chaînes de caractères. Les objets JSON et les tableaux de chaînes de caractères ne peuvent être créés ou mis à jour que via la REST API.

### Utilisation de l'ingestion de données cloud {#using-cloud-data-ingestion}

Vous pouvez gérer vos catalogues grâce à l'[ingestion de données cloud]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data) en synchronisant les données de catalogue directement depuis votre entrepôt de données (tel que Snowflake, Redshift, BigQuery, Databricks, Microsoft Fabric ou S3) de manière planifiée.

## Gestion des articles de catalogue {#managing-catalog-items}

En plus de gérer vos catalogues, vous pouvez également utiliser des endpoints asynchrones et synchrones pour gérer les articles de catalogue. Cela inclut la possibilité de modifier et de supprimer des articles de catalogue, ainsi que de lister les détails des articles de catalogue.

Par exemple, si vous souhaitez modifier un article de catalogue individuel, vous pouvez utiliser l'[endpoint `/catalogs/catalog_name/items/item_id`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item).

## Stockage des catalogues {#tiers}

La version gratuite des catalogues prend en charge des fichiers CSV d'une taille totale combinée de 500 Mo pour l'ensemble de votre entreprise, tandis que la version Catalogues Pro prend en charge des fichiers CSV d'une taille maximale de 2 Go par fichier.

{% alert important %}
Les droits d'utilisation des packages affichés dans le tableau de bord de Braze sont arrondis à l'unité la plus proche à des fins d'affichage. Vous conservez toutefois l'intégralité des droits d'utilisation achetés. Pour demander une mise à niveau du stockage des catalogues, contactez votre gestionnaire de compte Braze.
{% endalert %}

### Version gratuite {#free-version}

La taille de stockage pour la version gratuite des catalogues est de 500&nbsp;Mo maximum. Vous pouvez avoir un nombre illimité d'éléments tant qu'ils ne dépassent pas 500&nbsp;Mo au total.

#### Catalogues Pro {#catalogs-pro}

Au niveau de l'entreprise, le stockage maximum pour Catalogues Pro dépend de la taille des données du catalogue. Les options de taille de stockage sont les suivantes : 5&nbsp;Go, 10&nbsp;Go ou 15&nbsp;Go. L'espace de stockage de la version gratuite (500&nbsp;Mo) est inclus dans chacun de ces plans.

## Spécifications {#specifications}

Le tableau suivant résume les spécifications relatives à ce que vous pouvez inclure dans les catalogues.

| Domaine | Spécifications |
|------|-----------|
| Caractères par valeur d'élément | Jusqu'à 5 000 caractères dans une seule valeur. Par exemple, si vous avez un champ intitulé `description`, le nombre maximum de caractères dans ce champ est de 5 000. |
| Caractères par nom de colonne d'élément | Jusqu'à 250 caractères |
| Sélections par catalogue | Jusqu'à 30 sélections par catalogue |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Les étiquettes Liquid de catalogue ne peuvent pas être utilisées de manière récursive, ce qui signifie que vous ne pouvez pas référencer un élément de catalogue qui appelle ensuite un second élément de catalogue au sein de la même évaluation Liquid.
{% endalert %}