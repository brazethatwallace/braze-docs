---
nav_title: Synchronisation des collections Shopify
article_title: Synchronisation des collections Shopify
permalink: "/shopify_collections_sync/"
description: "Cet article de référence explique comment configurer la synchronisation des collections Shopify, qui vous permet de regrouper vos produits en collections afin que les clients puissent trouver vos produits par catégorie."
hidden: true
---

# Bêta de la synchronisation des collections Shopify {#shopify-collections-sync-beta}

> La synchronisation des collections Shopify vous permet de regrouper vos produits en collections afin que les clients puissent trouver vos produits par catégorie. Pour une expérience d'achat plus fluide, vous pouvez intégrer les articles des collections de votre boutique dans vos messages Braze.

{% alert important %}
La synchronisation des collections Shopify est actuellement en version bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à la bêta.
{% endalert %}

## Configurer la synchronisation des collections Shopify {#setting-up-shopify-collections-sync}

Pour synchroniser vos produits depuis votre boutique Shopify vers Braze, cochez la case **Sync Shopify collections** à l'étape **Sync products** de l'[intégration Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/#setting-up-shopify-in-braze).<br><br>![Étape 4 de la synchronisation des produits Shopify avec la case « Sync Shopify collections » cochée.][1]

Une fois vos produits synchronisés, vous pouvez voir quels produits sont associés à vos collections en consultant votre catalogue Shopify. <br><br>![Ligne du tableau de catalogue montrant un produit dans les collections « best-sellers » et « front page ».][2]

Depuis votre catalogue Shopify, vous pouvez consulter votre collection Shopify dans l'onglet **Selections**. <br><br>![L'onglet Selections affichant une liste de deux collections : « best-sellers » et « front page ».][3]

### Fonctionnalités de la bêta {#beta-functionality}

- Braze prend en charge jusqu'à 30 collections.
- L'ordre de tri de votre collection n'est pas maintenu ni pris en charge pour le moment. Pour l'instant, l'ordre de tri est basé sur les éléments suivants :
    - Les articles les plus récemment ajoutés à votre collection.
    - L'ordre dans lequel les articles sont mis à jour lors des synchronisations continues.
    - L'ordre que vous sélectionnez dans l'onglet de sélection de votre collection Shopify.

## Utiliser les collections Shopify {#using-shopify-collections}

Utilisez vos collections Shopify pour personnaliser un message pour chaque utilisateur dans votre Campaign, de la même manière que vous utiliseriez une [sélection Braze]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/).

{% alert warning %}
Prenez note du comportement suivant dans la bêta : <br><br>Si vous modifiez la description de la collection Shopify ou les paramètres de filtre, vous interromprez la synchronisation de votre collection Shopify. Par conséquent, votre collection Shopify ne fonctionnera pas comme prévu.
{% endalert %}

### Étape 1 : Configurer l'ordre de tri de votre collection Shopify {#step-1-configure-the-sort-order-of-your-shopify-collection}

1. Spécifiez l'ordre dans lequel les résultats de votre collection Shopify sont renvoyés en sélectionnant **Sort Order** dans l'onglet de sélection de votre collection Shopify. Cela inclut une option pour randomiser l'ordre de tri.
2. Saisissez le nombre maximum de résultats (jusqu'à 50) pour le champ **Limit number**.
3. Sélectionnez **Update Selection**.

![La page de modification de la sélection où vous pouvez sélectionner les paramètres de filtre, le type de tri et la limite de résultats.][4]

### Étape 2 : Utiliser la collection dans une Campaign {#step-2-use-the-collection-in-a-campaign}

1. Créez une Campaign, puis sélectionnez **+ Personalization** dans le compositeur de messages.
2. Sélectionnez les éléments suivants :<br>- **Catalog Items** comme **Personalization type**<br>- Le nom du catalogue<br>- La méthode de sélection des articles<br>- Le nom de la sélection (le nom de votre collection Shopify) <br>- Les informations à afficher dans votre message

{: start="3"}
3. Copiez et collez l'extrait de code Liquid à l'endroit où vous souhaitez que les informations apparaissent dans votre message.

![La section « Add Personalization » avec des champs pour sélectionner votre catalogue, la méthode de sélection des articles et les informations à afficher.][5]{: style="max-width:30%;"}

#### Liquid dans les résultats de sélection {#liquid-in-selection-results}

L'utilisation de résultats dans les catalogues, tels que les attributs personnalisés et les événements personnalisés, peut entraîner des résultats différents pour chaque utilisateur dans votre sélection.

[1]: {% image_buster /assets/unlisted_docs/img/shopify/sync_products.png %}
[2]: {% image_buster /assets/unlisted_docs/img/shopify/view_catalog.png %}
[3]: {% image_buster /assets/unlisted_docs/img/shopify/selections_tab.png %}
[4]: {% image_buster /assets/unlisted_docs/img/shopify/edit_selection.png %}
[5]: {% image_buster /assets/unlisted_docs/img/shopify/add_personalization.png %}