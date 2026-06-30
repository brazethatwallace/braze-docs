---
nav_title: Kataloge
article_title: Katalog-Endpunkte
page_order: 0
layout: dev_guide

search_tag: Endpoint
description: "Diese Landing-Page listet die Braze-Katalog-Endpunkte auf."
page_type: landing

guide_top_header: "Katalog-Endpunkte"
guide_top_text: "Verwenden Sie die Braze-Katalog-Endpunkte, um Ihre Kataloge und die Details Ihrer Katalogartikel hinzuzufügen, zu bearbeiten und zu verwalten. Für Massenänderungen an Ihrem Katalog verwenden Sie die asynchronen Katalog-Endpunkte. <br><br> Sie suchen eine Anleitung zur Erstellung eines Katalogs? Lesen Sie unseren Artikel zur <a href='/docs/user_guide/personalization_and_dynamic_content/catalog'>Erstellung und Verwendung von Katalogen</a>."

guide_featured_title: "Endpunkte für die Katalogverwaltung"
guide_featured_list:
  - name: "DELETE: Katalog löschen"
    link: /docs/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog
    image: /assets/img/braze_icons/edit-05.svg
  - name: "GET: Kataloge auflisten"
    link: /docs/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs
    image: /assets/img/braze_icons/list.svg
  - name: "POST: Katalog erstellen"
    link: /docs/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog
    image: /assets/img/braze_icons/check-square-broken.svg

guide_menu_title2: "Asynchrone Katalogartikel-Endpunkte"
guide_menu_list2:
  - name: "DELETE: Mehrere Katalogartikel löschen"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk
    image: /assets/img/braze_icons/edit-05.svg
  - name: "PATCH: Mehrere Katalogartikel bearbeiten"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk
    image: /assets/img/braze_icons/user-edit.svg
  - name: "POST: Mehrere Katalogartikel erstellen"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "PUT: Mehrere Katalogartikel aktualisieren"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items
    image: /assets/img/braze_icons/user-circle.svg

guide_menu_title3: "Synchrone Katalogartikel-Endpunkte"
guide_menu_list3:
  - name: "DELETE: Katalogartikel löschen"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item
    image: /assets/img/braze_icons/edit-05.svg
  - name: "GET: Katalogartikeldetails auflisten"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details
    image: /assets/img/braze_icons/list.svg
  - name: "GET: Details mehrerer Katalogartikel auflisten"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk
    image: /assets/img/braze_icons/list.svg
  - name: "PATCH: Katalogartikel bearbeiten"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item
    image: /assets/img/braze_icons/user-edit.svg
  - name: "POST: Katalogartikel erstellen"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "PUT: Katalogartikel ersetzen"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item
    image: /assets/img/braze_icons/user-circle.svg

guide_menu_title4: "Asynchrone Katalogfeld-Endpunkte"
guide_menu_list4:
  - name: "POST: Katalogfelder erstellen"
    link: /docs/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "DELETE: Katalogfeld löschen"
    link: /docs/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field
    image: /assets/img/braze_icons/edit-05.svg

guide_menu_title5: "Asynchrone Katalogauswahl-Endpunkte"
guide_menu_list5:
  - name: "POST: Katalogauswahlen erstellen"
    link: /docs/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "DELETE: Katalogauswahl löschen"
    link: /docs/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection
    image: /assets/img/braze_icons/edit-05.svg

---