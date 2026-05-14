---
nav_title: Smartling
article_title: Smartling
description: "このリファレンス記事では、BrazeとSmartlingのパートナーシップについて説明します。Smartlingはクラウドベースのローカライゼーションソフトウェアです。Braze Connectorは、HTMLメールテンプレート、Content Blocks、Canvases、Campaignメールメッセージの翻訳をサポートします。"
alias: /partners/smartling/
page_type: partner
search_tag: Partner
---

# Smartling

> [Smartling](https://www.smartling.com/)は、Webサイト、アプリ、およびカスタマーエクスペリエンスの翻訳を自動化することを目的とした顧客向けのエンドツーエンドのクラウド翻訳マネジメントソフトウェアです。

_この統合はSmartlingによって管理されています。_

## 統合について {#about-the-integration}

Braze Connectorは、CampaignsおよびCanvases（メール、プッシュ、アプリ内メッセージ、バナー）、メールテンプレート、およびContent Blocksのメッセージの翻訳をサポートします。各チャネルまたは機能でサポートされているエディタータイプについては、以下の表を参照してください。

| チャネル/機能 | 従来のエディター（例：HTML） | ドラッグ＆ドロップエディター |
| --------------- | ----------------------------- | -------------------- |
| [メール]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=email) | ✅ | ✅ |
| [IAM]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=in-app%20message) | ✅ | ✅ |
| [プッシュ]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=push) | ✅ | 該当なし |
| メールテンプレート | ✅ | ✅ |
| バナー | 該当なし | ✅ |
| Content Blocks |  ✅* |  ✅* |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="About the integration" }

*詳細については、[Content Blocksの翻訳の管理](#managing-translations-for-content-blocks)を参照してください。

### レガシーワークフロー {#legacy-workflow}

ユースケースに応じて、レガシー翻訳ワークフローまたは更新されたワークフローを使用してContent Blocksの翻訳を管理します。

更新されたワークフローでは、Brazeの多言語サポートとメッセージのロケールを使用して、翻訳タグがContent Blockに追加されます。ただし、Smartlingはメッセージレベルで翻訳を実行します。コンテンツは、CampaignまたはCanvasに含まれ、ターゲットロケールが設定されている場合にのみ翻訳されます。詳細については、[Content Blocksの翻訳の管理](#managing-translations-for-content-blocks)を参照してください。

レガシーワークフローの詳細については、[レガシーワークフローを使用した翻訳の管理](#managing-translations-using-the-legacy-workflow)を参照してください。

## 前提条件 {#prerequisites}

| 必要条件                   | 説明                                                                                                                                                         |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Smartlingアカウント             | このパートナーシップを活用するには、[Smartlingアカウント](https://dashboard.smartling.com/)が必要です。                                                          |
| Smartling翻訳プロジェクト | BrazeアカウントをSmartlingに接続するには、まずサインインし、[翻訳プロジェクトを作成する](https://help.smartling.com/hc/en-us/articles/115003074093)必要があります。 |
| Braze REST APIキー            | 以下の権限を持つBraze REST APIキー：<br>- campaigns.translations.get<br>- campaigns.translations.update<br>- campaigns.list<br>- campaigns.details<br>- canvas.translations.get<br>- canvas.translations.update<br>- campaigns.details<br>- templates.email.create<br>- templates.email.update<br>- templates.email.list<br>- templates.email.info<br>- templates.translations.get<br>- templates.translations.update<br>- content_blocks.info<br>- content_blocks.list<br>- content_blocks.create<br>- content_blocks.update<br><br> これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント           | [RESTエンドポイントURL]({{site.baseurl}}/api/basics/#endpoints)。エンドポイントはインスタンスのBraze URLに応じて異なります。             |
| Brazeの多言語設定 | [Brazeでの多言語設定の完了]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#prerequisites) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

### ステップ1：Brazeでの多言語設定の設定 {#step-1-set-up-multi-language-settings-in-braze}

Brazeでのロケールの設定については、[Brazeの多言語セットアップ手順]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#prerequisites)を参照してください。

### ステップ2：Smartling TMSでBrazeプロジェクトを設定する {#step-2-set-up-the-braze-project-in-smartling-tms}

コネクタの設定の詳細については、[Smartlingドキュメント](https://help.smartling.com/hc/en-us/articles/13248549217435)を参照してください。

### BrazeをSmartlingに接続する {#connecting-braze-to-smartling}

1. [Smartlingアカウント](https://dashboard.smartling.com/)で、[Braze Connector](https://help.smartling.com/hc/en-us/articles/115003074093)プロジェクトタイプを作成します。

![SmartlingでのBraze接続。]({% image_buster /assets/img/smartling/image1_Connecting_Braze_to_Smartling.png %})

{: start="2"}
2. このプロジェクトで、**Settings** > **Braze Settings** > **Connect to Braze**の順に選択します。
3. API URLやAPIキーなど、必須フィールドを入力します。テスト接続が成功した場合は、接続を保存します。テストが成功しなかった場合は、正しいAPI URLとAPIキーを入力したことを確認してください。

![Smartling API設定でのBraze接続。]({% image_buster /assets/img/smartling/image2_API.png %})

{: start="4"}
4. プロジェクト言語を追加します。

![Smartlingプロジェクト言語でのBraze接続。]({% image_buster /assets/img/smartling/image3_project_languages.png %})

{: start="5"}
5. Braze設定で、**Target Language (Braze)**列の値が、Brazeの多言語設定で設定されたロケールと一致することを確認します。ロケールの命名規則は完全に一致する必要があります。

![Smartling言語確認でのBraze接続。]({% image_buster /assets/img/smartling/image4_language_confirmation.png %})

### ステップ3：Brazeメッセージに翻訳タグを追加する {#step-3-add-translation-tags-to-your-braze-message}

メッセージに翻訳タグを追加する方法については、[Brazeの手順]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales/?tab%3Dhtml%2520editor#prerequisites)を参照してください。

- [メール]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=email)
- [プッシュ]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=push)
- [アプリ内メッセージ]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=in-app%20message)

以下は、翻訳タグを使用したHTMLメールキャンペーンの例です。

![翻訳タグ付きのBrazeメール。]({% image_buster /assets/img/smartling/image5_translation_tags.png %})

ロケールを選択するには、メッセージを下書きとして保存する必要があります。

### ステップ4：Smartlingでの翻訳の管理 {#step-4-manage-translations-in-smartling}

Braze Connectorを接続して設定したら、SmartlingプロジェクトのBrazeタブでBrazeコンテンツを確認できます。詳細については、[Smartlingドキュメント](https://help.smartling.com/hc/en-us/articles/13248577069979)を参照してください。

Smartlingは、以下の方法でコンテンツを検索および選択する高度な機能を提供します。
- キーワード検索
- Brazeコンテンツタイプ
- Brazeタグ付け

1. この例では、[ステップ3](#step-3-add-translation-tags-to-your-braze-message)で新年プロモーションメールキャンペーンを作成しました。

![翻訳タグ付きのBrazeメール。]({% image_buster /assets/img/smartling/image6_ny_promotion.png %})

{: start="2"}
2. 翻訳するCampaignを見つけたら、フォルダーを選択し、バリアントを選択して、**Request Translation**を選択します。

![翻訳のリクエスト。]({% image_buster /assets/img/smartling/image7_request_translation.png %})

{: start="3"}
3. 翻訳の新しいジョブを作成します。

![翻訳の新しいジョブを作成します。]({% image_buster /assets/img/smartling/image8_request_translation.png %})

{: start="4"}
4. ジョブが承認されたら、CATツールで各翻訳を編集します。

![翻訳CATツール。]({% image_buster /assets/img/smartling/image9_translation_job.png %})

{: start="5"}
5. 翻訳が完了したら、翻訳を保存してBrazeに送信します。

![Brazeに翻訳を送信します。]({% image_buster /assets/img/smartling/image10_translations.png %})

### ステップ5：Brazeで多言語ユーザーとしてメッセージをプレビューする {#step-5-preview-the-message-as-a-multi-language-user-in-braze}

Brazeで、多言語ユーザーとしてCampaignをプレビューし、翻訳が正しく適用されていることを確認します。

![多言語ユーザープレビュー。]({% image_buster /assets/img/smartling/image11_preview.png %})

## Content Blocksの翻訳の管理 {#managing-translations-for-content-blocks}

Content Blocksは、Brazeの**テンプレートとメディア**セクションで管理されます。

### メッセージコンポーネントの一部として保存された翻訳 {#translation-stored-as-part-of-the-message-component}

翻訳タグはContent Blockに属します。ただし、Smartlingはメッセージレベルで翻訳を実行します。コンテンツは、CampaignまたはCanvasに含まれ、ターゲットロケールが設定されている場合にのみ翻訳されます。

### 考慮事項 {#considerations}

- HTMLおよびドラッグ＆ドロップの両方のContent Blockエディターで、翻訳タグを手動でContent Blockに追加する必要があります。
- ロケールはメッセージレベルで選択されます。Content Block自体では選択されません。
- Canvasでは、Liquidタグを使用して手動で追加する代わりに、行を使用してContent Blocksをメッセージに挿入することをお勧めします。Content Blockをプレビューからメールにドラッグすると、ローカルコピーが作成されます。「親」Content Blockへの変更は、そのブロックを使用している他のCampaignsには反映されません。
- Content BlockのLiquidタグを使用する場合は、少なくとも1つの翻訳タグをメール本文に直接含めるようにしてください。翻訳タグを手動で追加すると、多言語ドロップダウンからロケールを選択できます。SmartlingはContent Blockの翻訳タグを取得します。`comment`タグを追加して、ユーザーにテキストが表示されないようにすることができます。

## レガシーワークフローを使用した翻訳の管理 {#managing-translations-using-the-legacy-workflow}

Content Block内で翻訳を直接管理する場合は、[Smartlingのドキュメント](https://help.smartling.com/hc/en-us/articles/13248577069979-Translating-with-the-Braze-Connector)のレガシー手順を参照してください。この方法は、言語属性とLiquidのif/elseロジックを使用して、さまざまな言語でテキストを表示します。

## よくある質問 {#frequently-asked-questions}

### ドラッグ＆ドロップエディターで翻訳タグはサポートされていますか？ {#are-translation-tags-supported-for-the-drag-and-drop-editor}

ドラッグ＆ドロップエディター（メール、Content Block、アプリ内メッセージ）では、Liquidタグとして翻訳タグを手動で追加する必要があります。

### Liquidタグ内のテキストを翻訳するにはどうすればよいですか？ {#how-do-you-translate-text-within-a-liquid-tag}

SmartlingはLiquidタグを認識し、コンポーザーで編集不可の変数にします。Liquidタグ内のその他のテキスト（デフォルトテキストやjoinのようなフィルターなど）も、Smartlingでは編集不可になります。ただし、SmartlingでLiquidタグを削除し、翻訳されたデフォルトテキストでLiquidタグを再作成してください。翻訳を保存する際に警告が表示されます。