---
nav_title: 翻訳
article_title: 翻訳エンドポイント
search_tag: Endpoint
page_order: 9
layout: dev_guide

description: "このランディングページには、Brazeの翻訳エンドポイントが一覧表示されます。"
page_type: landing

guide_top_header: "翻訳エンドポイント"
guide_top_text: "Brazeの翻訳エンドポイントを使って、Campaign、Canvas、Content Blocksの翻訳を管理・更新できます。"

guide_featured_title: "Campaignエンドポイント"
guide_featured_list:
  - name: "GET: Campaignの翻訳を表示する"
    link: /docs/api/endpoints/translations/campaigns/get_translation_campaign
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT: Campaign内の翻訳を更新する"
    link: /docs/api/endpoints/translations/campaigns/put_update_translation_campaign
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: Campaignのデフォルトソース翻訳を表示する"
    link: /docs/api/endpoints/translations/campaigns/get_source_campaign
    image: /assets/img/braze_icons/message-plus-square.svg

guide_menu_title: "Canvasエンドポイント"
guide_menu_list:
  - name: "GET: Canvasの翻訳を表示する"
    link: /docs/api/endpoints/translations/canvas/get_translation_canvas
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT: Canvas内の翻訳を更新する"
    link: /docs/api/endpoints/translations/canvas/put_update_translation_canvas
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: Canvasのデフォルトソース翻訳を表示する"
    link: /docs/api/endpoints/translations/canvas/get_source_canvas
    image: /assets/img/braze_icons/message-plus-square.svg

guide_menu_title2: "メールテンプレートエンドポイント"
guide_menu_list2:
  - name: "GET: メールテンプレートのデフォルトソース翻訳を表示する"
    link: /docs/api/endpoints/translations/email_templates/get_view_source_template
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "GET: 特定の翻訳とロケールを表示する"
    link: /docs/api/endpoints/translations/email_templates/get_view_translation_locale_template
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: すべての翻訳とロケールを表示する"
    link: /docs/api/endpoints/translations/email_templates/get_view_translation_template
    image: /assets/img/braze_icons/target-04.svg
  - name: "PUT: メールテンプレートの翻訳を更新する"
    link: /docs/api/endpoints/translations/email_templates/put_update_template
    image: /assets/img/braze_icons/target-04.svg

guide_menu_title3: "コンテンツブロックエンドポイント"
guide_menu_list3:
  - name: "GET: コンテンツブロックの全翻訳を表示する"
    link: /docs/api/endpoints/translations/content_blocks/get_translation_content_block
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT: コンテンツブロック内の翻訳を更新する"
    link: /docs/api/endpoints/translations/content_blocks/put_update_translation_content_block
    image: /assets/img/braze_icons/target-04.svg

---

{% multi_lang_include alerts/early_access_beta_alert.md feature='Access to the Braze translation endpoints' %}

## 翻訳エンドポイントの仕組み {#how-our-translation-endpoints-work}

翻訳エンドポイントは[多言語構成]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings)と連携して動作します。メッセージは、受信するユーザーに応じてレンダリングされる異なるバージョンを持つことができます。

### 前提条件 {#prerequisites}

これらのエンドポイントを使用する前に、[ロケールを追加]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings#add-a-locale)する必要があります。

### 翻訳のテスト方法 {#how-to-test-your-translations}

APIとBrazeダッシュボードを使用して、Campaign、Canvas（個々のステップを含む）、Content Blocks、メールテンプレート全体で翻訳サポートを検証する方法は2つあります。

- 構成中（起動前）
- 起動後（起動後の下書きを使用）

翻訳の更新をテストする前に、以下を実行する必要があります。

1. [ロケールを追加します]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings#add-a-locale)。
2. メッセージを作成し、必要に応じて翻訳タグを使用します。
3. メッセージを保存します。
4. 含めるロケールを選択します。