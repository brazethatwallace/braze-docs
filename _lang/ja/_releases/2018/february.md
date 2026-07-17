---
nav_title: 2月
page_order: 11
noindex: true
page_type: update
description: "この記事には2018年2月のリリースノートが含まれています。"
---
# 2018年2月 {#february-2018}

## iOSプッシュバッジカウント {#ios-push-badge-count}

Brazeのプッシュコンポーザーから[バッジカウントを更新]({{site.baseurl}}/help/best_practices/utilizing_badge_count#utilizing-badge-count)できるようになりました。
プッシュメッセージごとに、その通知がトリガーするバッジカウントを指定できます。

## メールアドレスを使用してAPI経由でユーザーをエクスポートする {#exporting-users-via-api-using-email-addresses}

メールアドレスを指定して、[API経由でユーザープロファイルデータをエクスポート]({{site.baseurl}}/developer_guide/rest_api/export#user-export)できるようになりました。
このエクスポートには、そのメールアドレスに関連するすべてのプロファイルが含まれます。

## メールテンプレートAPI {#email-template-apis}

[メールテンプレートをAPI経由で]({{site.baseurl}}/developer_guide/rest_api/email_templates#email-templates)作成および更新できるようになりました。各テンプレートには、他のAPIコールで参照できる**email_template_id**が付与されます。

## REST APIキーの権限 {#rest-api-keys-permissions}

[複数のREST APIキーを作成]({{site.baseurl}}/developer_guide/rest_api/basics#creating-rest-api-keys)し、それぞれにアクセス権限を設定できるようになりました。各キーは、特定のエンドポイントへのアクセスを許可するように設定できます。

また、特定のREST APIキーに対してREST APIリクエストを許可する[IPアドレスとサブネットのホワイトリスト]({{site.baseurl}}/developer_guide/rest_api/basics#api-ip-whitelisting)を指定することもできます。