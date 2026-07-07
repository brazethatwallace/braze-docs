---
nav_title: カタログ
article_title: カタログエンドポイント
page_order: 0
layout: dev_guide

search_tag: Endpoint
description: "このランディングページには、Brazeカタログエンドポイントの一覧が掲載されています。"
page_type: landing

guide_top_header: "カタログエンドポイント"
guide_top_text: "Brazeカタログエンドポイントを使用して、カタログとカタログアイテムの詳細を追加、編集、管理できます。カタログを一括変更するには、非同期カタログエンドポイントを使用します。<br><br>カタログの作成に関するガイダンスをお探しですか？<a href='/docs/user_guide/personalization_and_dynamic_content/catalog'>カタログの作成と使用</a> に関する記事をご覧ください。"

guide_featured_title: "カタログ管理エンドポイント"
guide_featured_list:
  - name: "DELETE: カタログを削除する"
    link: /docs/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog
    image: /assets/img/braze_icons/edit-05.svg
  - name: "GET: カタログ一覧を取得する"
    link: /docs/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs
    image: /assets/img/braze_icons/list.svg
  - name: "POST: カタログを作成する"
    link: /docs/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog
    image: /assets/img/braze_icons/check-square-broken.svg

guide_menu_title2: "非同期カタログアイテムエンドポイント"
guide_menu_list2:
  - name: "DELETE: 複数のカタログアイテムを削除する"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk
    image: /assets/img/braze_icons/edit-05.svg
  - name: "PATCH: 複数のカタログアイテムを編集する"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk
    image: /assets/img/braze_icons/user-edit.svg
  - name: "POST: 複数のカタログアイテムを作成する"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "PUT: 複数のカタログアイテムを更新する"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items
    image: /assets/img/braze_icons/user-circle.svg

guide_menu_title3: "同期カタログアイテムエンドポイント"
guide_menu_list3:
  - name: "DELETE: カタログアイテムを削除する"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item
    image: /assets/img/braze_icons/edit-05.svg
  - name: "GET: カタログアイテムの詳細を取得する"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details
    image: /assets/img/braze_icons/list.svg
  - name: "GET: 複数のカタログアイテムの詳細を取得する"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk
    image: /assets/img/braze_icons/list.svg
  - name: "PATCH: カタログアイテムを編集する"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item
    image: /assets/img/braze_icons/user-edit.svg
  - name: "POST: カタログアイテムを作成する"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "PUT: カタログアイテムを置換する"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item
    image: /assets/img/braze_icons/user-circle.svg

guide_menu_title4: "非同期カタログフィールドエンドポイント"
guide_menu_list4:
  - name: "POST: カタログフィールドを作成する"
    link: /docs/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "DELETE: カタログフィールドを削除する"
    link: /docs/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field
    image: /assets/img/braze_icons/edit-05.svg

guide_menu_title5: "非同期カタログセレクションエンドポイント"
guide_menu_list5:
  - name: "POST: カタログセレクションを作成する"
    link: /docs/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "DELETE: カタログセレクションを削除する"
    link: /docs/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection
    image: /assets/img/braze_icons/edit-05.svg

---