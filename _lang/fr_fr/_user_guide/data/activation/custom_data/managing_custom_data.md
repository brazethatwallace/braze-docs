---
nav_title: Gérer les données personnalisées
article_title: Gérer les données personnalisées
page_order: 2
page_type: reference
description: "Cet article de référence explique comment gérer les événements et attributs personnalisés : pré-remplissage, ajout de descriptions et d'étiquettes, gestion des propriétés d'événement, forçage des types de données et marquage des attributs comme données personnelles."
---

# Gérer les données personnalisées {#manage-custom-data}

> Cette page explique comment pré-remplir les données personnalisées dans vos campagnes et segments, gérer les événements et attributs personnalisés ainsi que leurs propriétés, et configurer les types de données. Pour le blocage et la suppression de données personnalisées, consultez [Bloquer les données personnalisées]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data/).

Pour savoir comment gérer les attributs personnalisés en particulier (ajout de descriptions, ajout d'étiquettes et marquage des attributs comme données personnelles), reportez-vous à la section [Gestion des attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#managing-custom-attributes).

## Pré-remplissage des données personnalisées {#pre-populate-custom-data}

Il peut arriver que vous souhaitiez implémenter des campagnes et des segments à l'aide de données personnalisées avant que votre équipe de développement n'ait intégré ces données. Braze vous permet de pré-renseigner des événements et des attributs personnalisés sur le tableau de bord avant que ne commence le suivi de ces données, pour que ces événements et attributs soient disponibles dans les menus déroulants et durant le processus de création de campagnes.

Pour pré-remplir les événements et attributs personnalisés, procédez comme suit :

1. Allez dans **Paramètres des données** > **Événements personnalisés** ou **Attributs personnalisés** ou **Produits**.

![Naviguez jusqu'à Attributs personnalisés, Événements personnalisés ou Produits.]({% image_buster /assets/img_archive/prepopulate_page.png %}){: style="max-width:90%;" }

{: start="2"}
2. Pour ajouter un attribut personnalisé, un événement personnalisé ou un produit, rendez-vous sur la page correspondante et sélectionnez **Add Custom Attributes**, **Add Custom Events** ou **Add Products**.<br><br>Pour les attributs personnalisés, sélectionnez un [type de données]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/#custom-attribute-data-types) pour cet attribut (par exemple, valeur booléenne ou chaîne de caractères). Le type de données d'un attribut détermine les filtres de segmentation disponibles pour cet attribut. <br><br>![Ajouter un nouvel attribut ou événement]({% image_buster /assets/img_archive/prepopulate_add.png %}){: style="max-width:80%;" }
3. Sélectionnez **Save**.

### Attribution de noms aux événements et attributs personnalisés {#naming-custom-events-and-custom-attributes}

Les événements personnalisés et les attributs personnalisés sont sensibles à la casse. Gardez cela à l'esprit lorsque votre équipe de développement intégrera ultérieurement ces événements et attributs personnalisés. Les noms doivent correspondre exactement à ceux que vous avez définis ici, sinon Braze générera un événement ou un attribut personnalisé différent.

## Gestion des propriétés {#managing-properties}

Après avoir créé un événement personnalisé ou un produit, sélectionnez **Manage Properties** pour cet événement ou ce produit afin d'ajouter de nouvelles propriétés, bloquer des propriétés existantes et afficher les Campaigns ou les Canvas qui utilisent cette propriété dans un [événement déclencheur]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/).

![Propriétés personnalisées d'un événement personnalisé.]({% image_buster /assets/img_archive/manageproperties1.png %}){: style="max-width:80%"}

Pour bloquer des propriétés d'événement ou de produit, utilisez le menu d'actions sur la page des propriétés. Pour bloquer entièrement des attributs personnalisés, des événements ou des produits, consultez [Bloquer les données personnalisées]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data/).

Pour assurer la traçabilité des attributs personnalisés, événements, produits ou propriétés d'événement ajoutés, vous devez demander à votre équipe de développement de les créer dans le SDK en utilisant le nom exact que vous avez utilisé pour les ajouter précédemment. Vous pouvez également utiliser l'[API]({{site.baseurl}}/api/basics/) de Braze pour importer des données sur cet attribut. Ensuite, l'attribut personnalisé, l'événement ou autre sera exploitable et s'appliquera à vos utilisateurs.

{% include alerts/note_alerts.md alert='Manage custom data storage' %}

## Détection du type de données selon les environnements {#data-type-detection-across-environments}

Braze détecte automatiquement le type de données d'un attribut personnalisé en fonction de la première valeur reçue. Si votre environnement de développement envoie d'abord une valeur numérique comme `100`, l'attribut est stocké en tant que nombre. Si la première valeur provenant de votre environnement de production arrive sous forme de chaîne de caractères (par exemple `"100"` entre guillemets), l'attribut est stocké en tant que chaîne de caractères.

Pour éviter cela, assurez-vous que votre intégration envoie des types de données cohérents dans tous les environnements. Si un type incorrect est déjà défini, vous pouvez forcer le type de données correct dans **Data Settings** > **Custom Attributes** en utilisant la [liste déroulante du type de données](#forcing-data-type-comparisons).

## Forcer les comparaisons de type de données {#forcing-data-type-comparisons}

Braze reconnaît automatiquement les types de données pour les données d'attribut qui lui sont envoyées. Cependant, dans l'éventualité où plusieurs types de données sont appliqués à un seul attribut, vous pouvez forcer le type de données de n'importe quel attribut pour indiquer à Braze de quoi il s'agit. Sélectionnez le type souhaité dans la liste déroulante de la colonne **Data Type**.

{% alert note %}
À compter du 30 mars 2026, la détection automatique ne définit un type de données que lors de la première ingestion. Pour modifier le type de données après la première ingestion, mettez-le à jour manuellement en suivant les étapes ci-dessous.
{% endalert %}

{% alert note %}
Le forçage des types de données ne s'applique pas aux propriétés d'événement ni aux propriétés d'achat.
{% endalert %}

![Liste déroulante du type de données des attributs personnalisés]({% image_buster /assets/img_archive/custom_events_view_data_type_dropdown.png %})

{% alert warning %}
Si vous choisissez de forcer le type de données d'un attribut, toute donnée entrante qui n'est pas du type spécifié sera contrainte dans ce type. Si une telle coercition est impossible (par exemple, une chaîne de caractères contenant des lettres convertie en nombre), les données seront ignorées. Toutes les données ingérées avant le changement de type continueront d'être stockées sous l'ancien type (et ne pourront donc pas être segmentées), et un avertissement apparaîtra à côté de l'attribut sur les profils des utilisateurs concernés.
{% endalert %}

### Données existantes après un changement de type {#existing-data-after-a-type-change}

Forcer un changement de type de données n'affecte que les nouvelles données entrantes dans Braze. Toutes les données ingérées avant le changement de type continuent d'être stockées sous l'ancien type et peuvent ne pas être segmentables avec les filtres du nouveau type. Un avertissement apparaît sur les profils des utilisateurs concernés. Pour les nouvelles données entrantes, si une valeur ne correspond pas au type forcé, Braze peut la contraindre dans le type forcé (par exemple, la chaîne de caractères `"100"` vers le nombre `100`) ; les valeurs qui ne peuvent pas être contraintes sont ignorées et ne mettent pas à jour l'attribut.

Si vous avez besoin que toutes les données utilisateur existantes correspondent au nouveau type, vous devez renvoyer les valeurs de l'attribut pour ces utilisateurs via le SDK, l'API ou un import CSV. Il n'existe pas de conversion automatique en masse pour les données existantes.

### Coercition de type de données {#data-type-coercion}

| Type de données forcé | Description |
|------------------|-------------|
| Valeur booléenne | Les entrées `1`, `true`, `t` (non sensibles à la casse) sont stockées comme `true` |
| Valeur booléenne | Les entrées `0`, `false`, `f` (non sensibles à la casse) sont stockées comme `false` |
| Nombre | Les nombres entiers ou flottants (tels que `1`, `1.5`) sont stockés en tant que nombres |
| Nombre | Les chaînes de caractères numériques (telles que `"100"` ou `"3.14"`) peuvent être contraintes en nombres lorsque l'attribut est forcé au type **Nombre** |
| Chaîne de caractères | Les valeurs numériques peuvent être contraintes sous forme de chaîne de caractères lorsque l'attribut est forcé au type **Chaîne de caractères** |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Coercition de type de données" }

Pour plus d'informations sur les options de filtrage spécifiques exposées par les différentes comparaisons de types de données, consultez la section [Configuration des rapports]({{site.baseurl}}/user_guide/analytics/reports/configure_reporting/). Pour plus d'informations sur les différents types de données disponibles, reportez-vous à la section [Types de données]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/#custom-attribute-data-types).

{% alert note %}
Les données envoyées à Braze sont immuables et ne peuvent être ni supprimées ni modifiées après leur réception par Braze. Cependant, vous pouvez recourir à l'une des méthodes décrites dans les sections précédentes pour contrôler ce que vous suivez dans votre tableau de bord. Pour bloquer ou supprimer des données personnalisées, consultez [Bloquer les données personnalisées]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data/).
{% endalert %}