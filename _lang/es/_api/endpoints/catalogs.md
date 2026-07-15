---
nav_title: Catálogos
article_title: Puntos de conexión de catálogos
page_order: 0
layout: dev_guide

search_tag: Endpoint
description: "En esta página de inicio se enumeran los puntos de conexión de los catálogos de Braze."
page_type: landing

guide_top_header: "Puntos de conexión de catálogos"
guide_top_text: "Utiliza los puntos de conexión de catálogos de Braze para añadir, editar y gestionar tus catálogos y los detalles de los elementos de los catálogos. Para realizar cambios masivos en tu catálogo, utiliza los puntos de conexión de catálogo asíncronos. <br><br> ¿Buscas orientación para crear un catálogo? Consulta nuestro artículo para <a href='/docs/user_guide/personalization_and_dynamic_content/catalog'>crear y utilizar catálogos</a>."

guide_featured_title: "Puntos de conexión de gestión del catálogo"
guide_featured_list:
  - name: "DELETE: Eliminar catálogo"
    link: /docs/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog
    image: /assets/img/braze_icons/edit-05.svg
  - name: "GET: Listar catálogos"
    link: /docs/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs
    image: /assets/img/braze_icons/list.svg
  - name: "POST: Crear catálogo"
    link: /docs/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog
    image: /assets/img/braze_icons/check-square-broken.svg

guide_menu_title2: "Puntos de conexión asíncronos de elementos de catálogo"
guide_menu_list2:
  - name: "DELETE: Eliminar varios elementos del catálogo"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk
    image: /assets/img/braze_icons/edit-05.svg
  - name: "PATCH: Editar varios elementos del catálogo"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk
    image: /assets/img/braze_icons/user-edit.svg
  - name: "POST: Crear varios elementos de catálogo"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "PUT: Actualizar varios elementos del catálogo"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items
    image: /assets/img/braze_icons/user-circle.svg

guide_menu_title3: "Puntos de conexión síncronos de elementos de catálogo"
guide_menu_list3:
  - name: "DELETE: Eliminar elemento del catálogo"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item
    image: /assets/img/braze_icons/edit-05.svg
  - name: "GET: Listar detalles del elemento del catálogo"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details
    image: /assets/img/braze_icons/list.svg
  - name: "GET: Listar detalles de varios elementos del catálogo"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk
    image: /assets/img/braze_icons/list.svg
  - name: "PATCH: Editar elemento del catálogo"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item
    image: /assets/img/braze_icons/user-edit.svg
  - name: "POST: Crear elemento de catálogo"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "PUT: Sustituir elemento del catálogo"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item
    image: /assets/img/braze_icons/user-circle.svg

guide_menu_title4: "Puntos de conexión asíncronos de campos de catálogo"
guide_menu_list4:
  - name: "POST: Crear campos de catálogo"
    link: /docs/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "DELETE: Eliminar campo de catálogo"
    link: /docs/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field
    image: /assets/img/braze_icons/edit-05.svg

guide_menu_title5: "Puntos de conexión asíncronos de selecciones de catálogo"
guide_menu_list5:
  - name: "POST: Crear selecciones de catálogo"
    link: /docs/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "DELETE: Eliminar selección de catálogo"
    link: /docs/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection
    image: /assets/img/braze_icons/edit-05.svg

---