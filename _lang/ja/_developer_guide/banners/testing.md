---
nav_title: テストバナー
article_title: テストバナー
page_order: 2
description: "すべてのメディア、コピー、パーソナライゼーション、カスタム属性が正しくレンダリングされるようにするために、キャンペーンを起動する前にバナーメッセージをテストする方法について説明します。"
channel:
  - banners
noindex: true
---

# テストバナー {#test-banners}

> すべてのメディア、コピー、パーソナライゼーション、カスタム属性が正しくレンダリングされるようにするために、キャンペーンを起動する前にバナーメッセージをテストする方法について説明します。一般的な情報については、[バナーについて]({{site.baseurl}}/developer_guide/banners)を参照してください。

## 前提条件 {#prerequisites}

Brazeでバナーメッセージをテストするには、まず[Brazeでバナーキャンペーンを作成]({{site.baseurl}}/user_guide/channels/banners/create_a_banner)する必要があります。さらに、テストしたいプレースメントがすでに[アプリまたはWebサイトに配置されている]({{site.baseurl}}/developer_guide/banners/placements)ことを確認してください。

[コンテンツテストグループ]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups)または個別のユーザーにテストを送信するには、送信前にテストデバイスでプッシュが有効になっており、テストユーザーに有効なプッシュトークンが登録されている必要があります。

## バナーのテスト {#test-a-banner}

{% multi_lang_include banners/testing.md page="testing" %}