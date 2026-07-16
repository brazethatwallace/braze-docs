---
nav_title: Catalogues
article_title: Catalogues
page_order: 3
layout: dev_guide

guide_top_header: "Catalogues"
guide_top_text: "Les catalogues accèdent aux données des fichiers CSV importés et des endpoints API pour enrichir vos messages, de la même manière que vous accéderiez à des attributs personnalisés ou à des propriétés d'événement via Liquid."

description: "Cette page d'accueil est dédiée aux catalogues. Utilisez les catalogues et les ensembles filtrés pour exploiter des données non liées aux utilisateurs dans vos Campaigns Braze afin d'envoyer des messages personnalisés."

guide_featured_title: "Articles de la section"
guide_featured_list:
- name: Créer un catalogue
  link: /docs/user_guide/data/activation/catalogs/create
  image: /assets/img/braze_icons/users-01.svg
- name: Utilisation des catalogues
  link: /docs/user_guide/data/activation/catalogs/use
  image: /assets/img/braze_icons/users-01.svg
- name: Notifications de retour en stock
  link: /docs/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: Notifications de baisse de prix
  link: /docs/price_drop_notifications
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: Sélections
  link: /docs/user_guide/data/activation/catalogs/selections
  image: /assets/img/braze_icons/list.svg

guide_menu_title: "Autres articles"
guide_menu_list:
- name: Endpoints API des catalogues
  link: /docs/api/endpoints/catalogs
  image: /assets/img/braze_icons/server-01.svg
- name: Blocs de produits par glisser-déposer
  link: /docs/dnd_product_blocks
  image: /assets/img/braze_icons/columns-01.svg
---
<br><br>

## Cas d'usage des catalogues {#catalog-use-cases}

N'importe quel type de données peut être intégré à un catalogue. Il s'agit généralement de métadonnées relatives à des offres : produits, remises, promotions, événements, etc. Consultez les cas d'usage ci-dessous pour découvrir comment exploiter ces données afin de cibler vos utilisateurs avec des messages hautement pertinents.

### Retail et e-commerce {#retail-and-ecommerce}

- **Offres promotionnelles saisonnières :** Importez des collections de produits saisonniers et personnalisez vos messages pour refléter les tendances du moment.
- **Messages localisés :** Importez les adresses, horaires et services de vos points de vente, puis personnalisez les notifications en fonction de la localisation des utilisateurs.
- **Notifications de retour en stock :** Importez des informations produit incluant les quantités en stock, puis utilisez les [notifications de retour en stock]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications) et les événements personnalisés Braze pour déclencher une Campaign ou un Canvas qui informe les utilisateurs qu'un produit est de nouveau disponible.
- **Notifications de baisse de prix :** Importez des informations produit incluant les prix, puis utilisez les [notifications de baisse de prix]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications) et les événements personnalisés Braze pour déclencher un Canvas qui informe les utilisateurs qu'un produit a baissé de prix.

### Divertissement {#entertainment}

- **Plans d'abonnement :** Importez des plans d'abonnement et faites la promotion de modules complémentaires auprès de vos utilisateurs en fonction de leurs habitudes d'utilisation et des types de contenu qu'ils consomment le plus souvent.
- **Événements à venir :** Importez les listes d'événements à venir avec leurs emplacements et les tranches d'âge du public, puis envoyez des notifications personnalisées aux utilisateurs situés dans la zone concernée et appartenant aux tranches d'âge ciblées.
- **Préférences médias :** Importez des informations sur les films et les séries, puis recommandez du contenu à vos utilisateurs en fonction de leurs titres favoris et de leurs genres les plus regardés.

### Voyages et hôtellerie {#travel-and-hospitality}

- **Destinations :** Importez des destinations de voyage avec leurs attractions, restaurants et activités les plus populaires, puis personnalisez les recommandations en fonction des voyages précédents de vos utilisateurs.
- **Hébergements :** Importez des établissements hôteliers avec leurs équipements, types de chambres et tarifs, puis envoyez des promotions à vos utilisateurs en fonction de leurs préférences sélectionnées.
- **Modes de transport :** Importez des offres et promotions pour différents modes de transport (vols, trains, voitures de location, etc.), puis envoyez-les à vos utilisateurs en fonction de leur historique de recherche récent.
- **Préférences alimentaires :** Importez des informations sur les offres de repas et utilisez les [sélections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) pour envoyer des messages personnalisés aux utilisateurs ayant des préférences alimentaires spécifiques, en fonction de la catégorie d'aliments qu'ils ont consultée le plus récemment.

## Comment les catalogues et Liquid fonctionnent ensemble {#how-catalogs-and-liquid-work-together}

Les catalogues sont une fonctionnalité de stockage de données. Ils contiennent de vastes ensembles de données pouvant être référencés dans vos messages à des fins de personnalisation. Pour accéder à ces données, vous utiliserez [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) comme langage de modélisation. Autrement dit, les catalogues constituent l'espace de stockage des données, et Liquid est le langage qui extrait les données pertinentes de cet espace.

Pour des exemples d'utilisation de Liquid pour extraire des informations de catalogue, consultez les cas d'usage supplémentaires dans [Créer un catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/create#additional-use-cases).

## Limites de stockage des données {#data-storage-limitations}

Le stockage des données pour les catalogues est limité en fonction de la taille des éléments du catalogue, qui peut différer de la taille des fichiers CSV importés.

Pour la version gratuite des catalogues, l'espace de stockage autorisé est de 500&nbsp;Mo. Vous pouvez avoir un nombre illimité d'éléments tant que l'espace de stockage ne dépasse pas 500&nbsp;Mo.

Pour Catalogues Pro, les options de taille de stockage sont : 5&nbsp;Go, 10&nbsp;Go, 15&nbsp;Go ou 50&nbsp;Go. Notez que l'espace de stockage de la version gratuite (500&nbsp;Mo) est inclus dans chacune de ces formules.

Si vous devez augmenter votre espace de stockage de catalogue, contactez votre gestionnaire de compte Braze. Pour plus de détails sur les formules et les droits associés, consultez [Stockage des catalogues]({{site.baseurl}}/user_guide/data/activation/catalogs/create#tiers).