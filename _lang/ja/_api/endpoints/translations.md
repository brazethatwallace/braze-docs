---
nav_title: 翻訳
article_title: 翻訳エンドポイント
search_tag: Endpoint
page_order: 9
layout: dev_guide

description: "このランディングページには、Brazeの翻訳エンドポイントが一覧表示されます。"
page_type: landing

guide_top_header: "翻訳エンドポイント"
guide_top_text: "Brazeの翻訳エンドポイントを使って、キャンペーン、キャンバス、Content Blocks、メールテンプレート、Webhookテンプレートの翻訳を管理・更新できます。"

guide_featured_title: "キャンペーンエンドポイント"
guide_featured_list:
  - name: "GET: キャンペーンの翻訳を表示する"
    link: /docs/api/endpoints/translations/campaigns/get_translation_campaign
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT: キャンペーン内の翻訳を更新する"
    link: /docs/api/endpoints/translations/campaigns/put_update_translation_campaign
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: キャンペーンのデフォルトソース翻訳を表示する"
    link: /docs/api/endpoints/translations/campaigns/get_source_campaign
    image: /assets/img/braze_icons/message-plus-square.svg

guide_menu_title: "キャンバスエンドポイント"
guide_menu_list:
  - name: "GET: キャンバスの翻訳を表示する"
    link: /docs/api/endpoints/translations/canvas/get_translation_canvas
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT: キャンバス内の翻訳を更新する"
    link: /docs/api/endpoints/translations/canvas/put_update_translation_canvas
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: キャンバスのデフォルトソース翻訳を表示する"
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

guide_menu_title4: "Webhookテンプレートエンドポイント"
guide_menu_list4:
  - name: "GET: Webhookテンプレートのデフォルトソース翻訳を表示する"
    link: /docs/api/endpoints/translations/webhook_templates/get_view_source_webhook_template
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "GET: Webhookテンプレートの翻訳を表示する"
    link: /docs/api/endpoints/translations/webhook_templates/get_view_translations_webhook_template
    image: /assets/img/braze_icons/target-04.svg
  - name: "PUT: Webhookテンプレートの翻訳を更新する"
    link: /docs/api/endpoints/translations/webhook_templates/put_update_webhook_template
    image: /assets/img/braze_icons/target-04.svg

---

{% multi_lang_include alerts/early_access_beta_alert.md feature='Access to the Braze translation endpoints' %}

## 翻訳エンドポイントの仕組み {#how-our-translation-endpoints-work}

翻訳エンドポイントは[多言語コンポジション]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings)と連携しており、メッセージを受信するユーザーに応じて異なるバージョンのメッセージをレンダリングできます。

### 前提条件 {#prerequisites}

これらのエンドポイントを使用する前に、[ロケールを追加]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings#add-a-locale)する必要があります。

### 翻訳のテスト方法 {#how-to-test-your-translations}

APIとBrazeダッシュボードを使用して、キャンペーン、キャンバス（個々のステップを含む）、Content Blocks、メールテンプレート、Webhookテンプレートにわたる翻訳サポートを検証する方法は2つあります。

- コンポジション中（ローンチ前）
- ローンチ後（ローンチ後の下書きを使用）

翻訳の更新をテストする前に、以下を行う必要があります。

1. [ロケールを追加]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings#add-a-locale)します。
2. メッセージを作成し、適切な場所に翻訳タグを使用します。
3. メッセージを保存します。
4. 含めるロケールを選択します。