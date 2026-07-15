---
nav_title: 外部IDの移行
article_title: 外部IDの移行
search_tag: Endpoint
page_order: 7
layout: dev_guide

description: "このランディングページでは、Brazeの外部ID移行機能について説明し、一覧を示します。"
page_type: landing

guide_top_header: "外部IDの移行"
guide_top_text: "外部ID移行APIを使用すると、既存の外部IDの名前を変更したり（新しいプライマリIDを作成し、既存のIDを非推奨にする）、移行後に非推奨のIDを削除したりできます。<br><br> このソリューションは、以前の外部ID命名スキーマを使用するアプリの古いバージョンが壊れないように、移行期間をサポートするために複数の外部IDを許可するように設計されています。古い命名スキーマが使用されなくなった場合は、非推奨の外部IDを削除することを強く推奨します。"

guide_featured_title: "外部ID移行エンドポイント"
guide_featured_list:
  - name: "POST:外部IDの名前を変更する"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST:非推奨の外部IDを削除する"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove
    image: /assets/img/braze_icons/user-minus-01.svg
---