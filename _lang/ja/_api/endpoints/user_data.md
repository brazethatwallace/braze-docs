---
nav_title: ユーザーデータ
article_title: ユーザーデータエンドポイント
search_tag: Endpoint
page_order: 9

local_redirect: #event-object-specification #purchase-object-specification
  event-object-specification: '/docs/api/objects_filters/event_object/'
  purchase-object-specification: '/docs/api/objects_filters/purchase_object/'

layout: dev_guide

#Required
description: "このランディングページには、Brazeのユーザーデータエンドポイントが一覧表示されています。"
page_type: landing

guide_top_header: "ユーザーデータエンドポイント"
guide_top_text: "Brazeユーザーデータエンドポイントを使用すると、モバイルアプリの外部から入力されるユーザーに関するデータを記録することによって、ユーザーに関する情報を追跡できます。このAPIを使って、テストやその他の目的でユーザーを削除することもできます。<br> <br> すべてのAPIエンドポイントには、4&nbsp;MBのデータペイロード制限があります。4&nbsp;MBを超えるデータを投稿しようとすると、HTTP 413 Request Entity Too Largeで失敗します。<br> <br> このセクションの例にはURL https://rest.iad-01.braze.com が含まれていますが、別のエンドポイントURLを使用する必要がある場合もあります（例えば、Braze EUデータセンターでホストされている場合や、専用のBrazeインストール環境がある場合など）。別のエンドポイントURLを使用する必要がある場合は、Brazeカスタマーサクセスマネージャーがお知らせします。"

guide_featured_title: "ユーザーデータエンドポイント"
guide_featured_list:
  - name: "POST: 新しいユーザーエイリアスを作成する"
    link: /docs/api/endpoints/user_data/post_user_alias/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: ユーザーエイリアスを更新する"
    link: /docs/api/endpoints/user_data/post_users_alias_update/
    image: /assets/img/braze_icons/user-edit.svg
  - name: "POST: ユーザーデータを削除する"
    link: /docs/api/endpoints/user_data/post_user_delete/
    image: /assets/img/braze_icons/user-minus-01.svg
  - name: "POST: ユーザーを特定する"
    link: /docs/api/endpoints/user_data/post_user_identify/
    image: /assets/img/braze_icons/user-circle.svg
  - name: "POST: ユーザーを追跡する"
    link: /docs/api/endpoints/user_data/post_user_track/
    image: /assets/img/braze_icons/database-01.svg
  - name: "POST: ユーザーを追跡する（同期）"
    link: /docs/api/endpoints/user_data/post_user_track_synchronous/
    image: /assets/img/braze_icons/database-01.svg
  - name: "POST: ユーザーをマージする"
    link: /docs/api/endpoints/user_data/post_users_merge/
    image: /assets/img/braze_icons/users-01.svg

guide_menu_title: "External IDマイグレーションエンドポイント"
guide_menu_list:
  - name: "POST: External IDの名前変更"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: 非推奨のExternal IDを削除する"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove/
    image: /assets/img/braze_icons/user-minus-01.svg
---