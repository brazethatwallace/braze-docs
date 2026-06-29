---
nav_title: テストバナー
article_title: テストバナー
page_order: 2
description: "すべてのメディア、コピー、パーソナライゼーション、カスタム属性が正しくレンダリングされるようにするために、Campaignを起動する前にバナーメッセージをテストする方法について説明します。"
channel:
  - banners
noindex: true
---

# テストバナー {#test-banners}

> すべてのメディア、コピー、パーソナライゼーション、カスタム属性が正しくレンダリングされるようにするために、Campaignを起動する前にバナーメッセージをテストする方法について説明します。一般的な情報については、[バナーについて]({{site.baseurl}}/developer_guide/banners)を参照してください。

## 前提条件 {#prerequisites}

Brazeでバナーメッセージをテストする前に、[Brazeでバナーキャンペーンを作成する]({{site.baseurl}}/user_guide/channels/banners/create_a_banner)必要があります。さらに、テストしたいプレースメントがすでに[アプリやWebサイトに配置されている]({{site.baseurl}}/developer_guide/banners/placements)ことを確認してください。

テストを[コンテンツテストグループ]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab#content-test-groups)または個々のユーザーに送信するには、送信前にテストデバイスでプッシュが有効になっており、テストユーザーの有効なプッシュトークンが登録されている必要があります。

## バナーをテストする {#test-a-banner}

{% multi_lang_include banners/testing.md page="testing" %}