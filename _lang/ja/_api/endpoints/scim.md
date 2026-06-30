---
nav_title: SCIM
article_title: SCIMエンドポイント
search_tag: Endpoint
page_order: 5
layout: dev_guide
alias: /scim/

description: "このランディングページには、Braze SCIMエンドポイントが一覧表示されています。"
page_type: landing

guide_top_header: "SCIMエンドポイント"
guide_top_text: "[System for Cross-domain Identity Management (SCIM)](http://www.simplecloud.info/) 仕様は、ユーザーとグループを表すための定義されたスキーマを提供することにより、クラウドベースのアプリケーションおよびサービスでのユーザーIDの管理を容易にするように設計されています。Braze SCIMエンドポイントを使用して、自動ユーザープロビジョニングを管理します。"

guide_featured_title: ""
guide_featured_list:
  - name: "POST: 新しいダッシュボードユーザーアカウントを作成する"
    link: /docs/post_create_user_account
    image: /assets/img/braze_icons/plus-circle.svg
  - name: "GET: 既存のダッシュボードユーザーアカウントの検索"
    link: /docs/get_see_user_account_information
    image: /assets/img/braze_icons/eye.svg
  - name: "GET: 既存のダッシュボードユーザーアカウントをメールで検索"
    link: /docs/api/endpoints/scim/get_search_existing_dashboard_user
    image: /assets/img/braze_icons/eye.svg
  - name: "PUT: ダッシュボードユーザーアカウントの更新"
    link: /docs/post_update_existing_user_account
    image: /assets/img/braze_icons/pencil-01.svg
  - name: "DELETE: ダッシュボードのユーザーアカウントを削除する"
    link: /docs/delete_existing_dashboard_user
    image: /assets/img/braze_icons/trash-01.svg
---


## ダッシュボードにアクセスできるユーザーの一覧をエクスポートする方法 {#how-to-export-a-list-of-users-with-dashboard-access}

このワークフローを使用して、Brazeダッシュボードにアクセスできるユーザーを監査します。

1. **設定** > **管理者設定** > **セキュリティ設定** > **セキュリティイベントのダウンロード**からセキュリティイベントレポートをダウンロードします。
2. レポートからユーザーのメールアドレスを抽出します。
3. 各メールアドレスについて、[GET: 既存のダッシュボードユーザーアカウントをメールで検索]({{site.baseurl}}/api/endpoints/scim/get_search_existing_dashboard_user)を使用してユーザーの詳細を取得します。
4. 必要に応じて、返されたリソース`id`を[GET: 既存のダッシュボードユーザーアカウントの検索]({{site.baseurl}}/api/endpoints/scim/get_see_user_account_information)で使用して、追加のユーザー詳細を取得します。

SCIMエンドポイントの完全な一覧については、[SCIMエンドポイント]({{site.baseurl}}/api/endpoints/scim)を参照してください。レポートソースの詳細については、[セキュリティイベントレポートのダウンロード]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#security-event-report)を参照してください。