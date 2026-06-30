---
nav_title: Catalogues
article_title: Endpoints des catalogues
page_order: 0
layout: dev_guide

search_tag: Endpoint
description: "Cette page d'accueil répertorie les endpoints des catalogues Braze."
page_type: landing

guide_top_header: "Endpoints des catalogues"
guide_top_text: "Utilisez les endpoints des catalogues Braze pour ajouter, modifier et gérer vos catalogues et les détails de vos éléments de catalogue. Pour les modifications en masse de votre catalogue, utilisez les endpoints de catalogue asynchrones. <br><br> Vous cherchez des conseils pour créer un catalogue ? Consultez notre article consacré à <a href='/docs/user_guide/personalization_and_dynamic_content/catalog'>la création et l'utilisation des catalogues</a>."

guide_featured_title: "Endpoints de gestion des catalogues"
guide_featured_list:
  - name: "DELETE : Supprimer un catalogue"
    link: /docs/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog
    image: /assets/img/braze_icons/edit-05.svg
  - name: "GET : Lister les catalogues"
    link: /docs/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs
    image: /assets/img/braze_icons/list.svg
  - name: "POST : Créer un catalogue"
    link: /docs/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog
    image: /assets/img/braze_icons/check-square-broken.svg

guide_menu_title2: "Endpoints asynchrones des éléments de catalogue"
guide_menu_list2:
  - name: "DELETE : Supprimer plusieurs éléments de catalogue"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk
    image: /assets/img/braze_icons/edit-05.svg
  - name: "PATCH : Modifier plusieurs éléments de catalogue"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk
    image: /assets/img/braze_icons/user-edit.svg
  - name: "POST : Créer plusieurs éléments de catalogue"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "PUT : Mettre à jour plusieurs éléments de catalogue"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items
    image: /assets/img/braze_icons/user-circle.svg

guide_menu_title3: "Endpoints synchrones des éléments de catalogue"
guide_menu_list3:
  - name: "DELETE : Supprimer un élément de catalogue"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item
    image: /assets/img/braze_icons/edit-05.svg
  - name: "GET : Lister les détails d'un élément de catalogue"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details
    image: /assets/img/braze_icons/list.svg
  - name: "GET : Lister les détails de plusieurs éléments de catalogue"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk
    image: /assets/img/braze_icons/list.svg
  - name: "PATCH : Modifier un élément de catalogue"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item
    image: /assets/img/braze_icons/user-edit.svg
  - name: "POST : Créer un élément de catalogue"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "PUT : Remplacer un élément de catalogue"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item
    image: /assets/img/braze_icons/user-circle.svg

guide_menu_title4: "Endpoints asynchrones des champs de catalogue"
guide_menu_list4:
  - name: "POST : Créer des champs de catalogue"
    link: /docs/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "DELETE : Supprimer un champ de catalogue"
    link: /docs/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field
    image: /assets/img/braze_icons/edit-05.svg

guide_menu_title5: "Endpoints asynchrones des sélections de catalogue"
guide_menu_list5:
  - name: "POST : Créer des sélections de catalogue"
    link: /docs/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "DELETE : Supprimer une sélection de catalogue"
    link: /docs/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection
    image: /assets/img/braze_icons/edit-05.svg

---