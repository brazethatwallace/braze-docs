---
nav_title: 2月
page_order: 11
noindex: true
page_type: update
description: "この記事には2018年2月のリリースノートが含まれています。"
---
# 2018年2月 {#february-2018}

## iOSプッシュバッジカウント

Brazeのプッシュコンポーザーから[バッジカウントを更新]({{site.baseurl}}/help/best_practices/utilizing_badge_count#utilizing-badge-count)できるようになりました。
各プッシュメッセージについて、その通知がトリガーするバッジカウントを指定できます。

## メールアドレスを使用したAPI経由でのユーザーエクスポート

メールアドレスを指定することで、[API経由でユーザープロファイルデータをエクスポート]({{site.baseurl}}/developer_guide/rest_api/export#user-export)できるようになりました。
このエクスポートには、そのメールアドレスに関連するすべてのプロファイルが含まれます。

## メールテンプレートAPI

APIを使用して[メールテンプレートの作成と更新]({{site.baseurl}}/developer_guide/rest_api/email_templates#email-templates)ができるようになりました。各テンプレートには**email_template_id**が付与され、他のAPI呼び出しで参照できます。

REST APIキーの権限を設定できるようになりました。[複数のREST APIキーを作成]({{site.baseurl}}/api/basics#creating-rest-api-keys)し、それぞれにアクセス権限を構成できます。各キーは、特定のエンドポイントへのアクセスを許可するように設定できます。

また、特定のREST APIキーに対してREST APIリクエストを許可する[IPアドレスとサブネットのホワイトリスト]({{site.baseurl}}/developer_guide/rest_api/basics#api-ip-whitelisting)を指定することもできます。