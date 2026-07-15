---
nav_title: Catálogos
article_title: Endpoints de catálogos
page_order: 0
layout: dev_guide

search_tag: Endpoint
description: "Esta landing page lista os endpoints de catálogos da Braze."
page_type: landing

guide_top_header: "Endpoints de catálogos"
guide_top_text: "Use os endpoints de catálogos da Braze para adicionar, editar e gerenciar seus catálogos e detalhes de itens do catálogo. Para alterações em massa no seu catálogo, use os endpoints assíncronos do catálogo. <br><br> Procurando orientação sobre como criar um catálogo? Confira nosso artigo sobre <a href='/docs/user_guide/personalization_and_dynamic_content/catalog'>como criar e usar catálogos</a>."

guide_featured_title: "Endpoints de gerenciamento de catálogo"
guide_featured_list:
  - name: "DELETE: Excluir catálogo"
    link: /docs/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog
    image: /assets/img/braze_icons/edit-05.svg
  - name: "GET: Listar catálogos"
    link: /docs/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs
    image: /assets/img/braze_icons/list.svg
  - name: "POST: Criar catálogo"
    link: /docs/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog
    image: /assets/img/braze_icons/check-square-broken.svg

guide_menu_title2: "Endpoints assíncronos de itens do catálogo"
guide_menu_list2:
  - name: "DELETE: Excluir vários itens do catálogo"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk
    image: /assets/img/braze_icons/edit-05.svg
  - name: "PATCH: Editar vários itens do catálogo"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk
    image: /assets/img/braze_icons/user-edit.svg
  - name: "POST: Criar vários itens do catálogo"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "PUT: Atualizar vários itens do catálogo"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items
    image: /assets/img/braze_icons/user-circle.svg

guide_menu_title3: "Endpoints síncronos de itens do catálogo"
guide_menu_list3:
  - name: "DELETE: Excluir item do catálogo"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item
    image: /assets/img/braze_icons/edit-05.svg
  - name: "GET: Listar detalhes do item do catálogo"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details
    image: /assets/img/braze_icons/list.svg
  - name: "GET: Listar detalhes de vários itens do catálogo"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk
    image: /assets/img/braze_icons/list.svg
  - name: "PATCH: Editar item do catálogo"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item
    image: /assets/img/braze_icons/user-edit.svg
  - name: "POST: Criar item do catálogo"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "PUT: Substituir item do catálogo"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item
    image: /assets/img/braze_icons/user-circle.svg

guide_menu_title4: "Endpoints assíncronos de campos do catálogo"
guide_menu_list4:
  - name: "POST: Criar campos do catálogo"
    link: /docs/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "DELETE: Excluir campo do catálogo"
    link: /docs/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field
    image: /assets/img/braze_icons/edit-05.svg

guide_menu_title5: "Endpoints assíncronos de seleções do catálogo"
guide_menu_list5:
  - name: "POST: Criar seleções do catálogo"
    link: /docs/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "DELETE: Excluir seleção do catálogo"
    link: /docs/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection
    image: /assets/img/braze_icons/edit-05.svg

---