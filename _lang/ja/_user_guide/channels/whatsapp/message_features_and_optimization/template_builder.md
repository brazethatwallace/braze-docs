---
nav_title: WhatsApp テンプレートビルダー
article_title: WhatsApp テンプレートビルダー
description: "WhatsApp テンプレートビルダーを使用して、Braze内で直接WhatsAppメッセージテンプレートを作成、設定、送信する方法を説明します。"
alias: /whatsapp_template_builder/
page_type: reference
channel:
  - WhatsApp
---

# WhatsApp テンプレートビルダー {#whatsapp-template-builder}

> WhatsApp テンプレートビルダーを使用すると、BrazeとMeta Business Managerを切り替えることなく、Braze内で直接WhatsAppメッセージテンプレートを作成して送信できます。Metaがテンプレートを承認した後は、必要な数のCampaignsやCanvasesで使用できます。

## 前提条件 {#prerequisites}

{% multi_lang_include whatsapp/template_prerequisites.md %}

## テンプレートを作成する {#create-a-template}

### ステップ 1:WhatsApp テンプレートに移動する {#step-1-go-to-whatsapp-templates}

**コンテンツ** > **WhatsApp**に移動し、**新規テンプレートを作成**を選択します。

![新しいテンプレートを作成するボタンがあるWhatsAppテンプレートページ。]({% image_buster /assets/img/whatsapp/templates/create_whatsapp_template.png %})

### ステップ 2:テンプレート設定を構成する {#step-2-configure-template-settings}

以下のフィールドに入力します。

| フィールド | 説明 |
| ----- | ----- |
| **アカウント** | テンプレートを送信するWhatsApp Business Account（WABA）。WABA内のすべてのサブスクリプショングループと電話番号がテンプレートアクセスを共有します。 |
| **言語** | このテンプレートの言語。WhatsAppでは言語ごとに個別のテンプレートが必要です。 |
| **テンプレート名** | テンプレートのユニークな名前。テンプレート名には小文字、数字、アンダースコアのみ使用できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ 2:テンプレート設定を構成する" }

### ステップ 3:レイアウトを選択する {#step-3-choose-a-layout}

**レイアウト**で、テンプレートタイプを選択します。

- **デフォルト:** 標準のWhatsAppメッセージ。この記事で説明するレイアウトです。
- **カルーセル:** 水平にスクロール可能なカードを含むメッセージ。詳細については、[カルーセルテンプレート]({{site.baseurl}}/whatsapp_carousel_templates)を参照してください。

### ステップ 4:テンプレートを構築する {#step-4-build-your-template}

#### ヘッダー（オプション） {#header-optional}

メッセージ本文の上に表示されるヘッダーを追加します。以下から選択できます。

- **テキスト:** 短いテキストヘッダー。
- **メディア:** 画像、動画、またはドキュメント（URLのみ）。Brazeはメディア参照を保存し、承認のためにサンプルをMetaに送信します。
- **なし:** ヘッダーなし

#### 本文 {#body}

メッセージのメインコンテンツを入力し、Liquidまたは汎用変数を使用して本文を必要に応じてパーソナライズします。

{% raw %}
- Liquidタグ（例: `{{${first_name}}}`）を使用します。BrazeはLiquidを保存し、CampaignまたはCanvasの作成画面でテンプレートを使用する際に表示します。
- 後でメッセージ作成時にパーソナライゼーションを追加したい場合は、番号付きプレースホルダー（例: `{{1}}`）などの汎用変数を使用します。
{% endraw %}

**+** プラスボタンが表示される場所にパーソナライゼーションを追加できます。すべてのフィールドがパーソナライゼーションに対応しているわけではありません。

#### フッター（オプション） {#footer-optional}

メッセージ本文の下に表示される短いフッターを追加します。

#### ボタン（オプション） {#buttons-optional}

テンプレートに最大10個のボタンを追加できます。ボタンタイプにはそれぞれ異なるカテゴリと仕様があります。

| ボタンタイプ | カテゴリ | 仕様 |
| --- | --- | --- |
| クイック返信 | クイック返信ボタン |{::nomarkdown}<ul><li><b>最大数:</b> 10</li><li><b>ボタンテキスト:</b> 最大25文字</li></ul> {:/}|
| 電話番号 | コールトゥアクションボタン | {::nomarkdown}<ul><li><b>最大数:</b> 1</li><li><b>ボタンテキスト:</b> 最大25文字</li><li><b>電話番号:</b> +を含まない国コード付きの有効な電話番号（例:「14155552671」）</li></ul> {:/}|
| Webサイトにアクセス | コールトゥアクションボタン | {::nomarkdown}<ul><li><b>最大数:</b> 2</li><li><b>ボタンテキスト:</b> 最大25文字</li><li><b>WebサイトURL:</b> 最大2,000文字</li></ul> {:/}|
| オファーコードをコピー | コールトゥアクションボタン | {::nomarkdown}<ul><li><b>最大数:</b> 1</li><li><b>ボタンテキスト:</b>「Copy offer code」（編集不可）</li><li><b>オファーコード:</b> 最大15文字</li></ul> {:/}|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ボタン（オプション）" }

![クイック返信ボタンとコールトゥアクションボタンを含むWhatsAppテンプレート作成画面。]({% image_buster /assets/img/whatsapp/templates/buttons.png %})

### ステップ 5:テンプレートをプレビューする {#step-5-preview-your-template}

送信前に、受信者にメッセージがどのように表示されるかプレビューします。

- **ユーザーとしてプレビュー:** メッセージの汎用プレビューを表示します。
- **特定のユーザーとしてプレビュー:** ユーザープロファイルを選択して、そのユーザーのデータでテンプレートがどのようにレンダリングされるか確認します。

### ステップ 6:レビューのために送信する {#step-6-submit-for-review}

**送信**を選択して、テンプレートをMetaのレビューに送信します。レビューは通常数分で完了しますが、最大24時間かかる場合があります。テンプレートは送信後に**WhatsApp テンプレート**ページに表示され、**WhatsApp テンプレート**ページを更新するとステータスが更新されます。

## サポートされているテンプレートカテゴリ {#supported-template-categories}

WhatsApp テンプレートビルダーでは、現在マーケティングテンプレートのみがサポートされています。

## 承認済みテンプレートをCampaignで使用する {#use-an-approved-template-in-a-campaign}

Metaがテンプレートを承認した後、WhatsApp CampaignまたはCanvasで使用できます。

1. **Campaigns**に移動し、**キャンペーンを作成** > **WhatsApp**を選択します。
2. メッセージ作成画面で、承認済みテンプレートを選択します。
3. Brazeはテンプレートのコンテンツ（テンプレート作成時に入力したメディアやLiquidを含む）を自動的に入力するため、再入力する必要はありません。
4. 必要に応じて変数コンテンツやパーソナライゼーションを更新します。Metaによってロックされたフィールド（グレーで表示）は編集できません。ロックされたコンテンツを変更するには、テンプレートを編集して承認のために再送信する必要があります。
5. **テスト**タブを使用してメッセージをプレビューし、本文変数を更新し、起動前にメッセージが期待どおりに表示されることを確認します。

WhatsApp Campaignの構築の詳細については、[WhatsAppメッセージを作成する]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message)を参照してください。

## よくある質問 {#frequently-asked-questions}

### Metaのテンプレートレビューにはどのくらい時間がかかりますか {#how-long-does-meta-template-review-take}

レビューは通常5分以内に完了しますが、最大24時間かかる場合があります。

### 承認後にテンプレートを編集できますか {#can-i-edit-a-template-after-its-been-approved}

ロックされたコンテンツ（本文コピーやその他のMeta管理フィールド）を変更するには、テンプレートを承認のために再送信する必要があり、WhatsApp Business Managerから行う必要があります。CampaignまたはCanvasを構築する際に、コンテンツとパーソナライゼーションを更新できます。

### テンプレートビルダーが利用可能になる前に送信したテンプレートはどうなりますか {#what-happens-to-templates-i-submitted-before-the-template-builder-was-available}

Meta Business Managerで作成されたテンプレートは、引き続きBrazeで使用できます。テンプレートビルダーは、Brazeダッシュボードを離れることなくテンプレートを作成・管理するための追加の方法です。

### すべてのフィールドにパーソナライゼーションを追加できないのはなぜですか {#why-cant-i-add-personalization-to-every-field}

Metaはテンプレートのどの部分をパーソナライズできるかを制限しています。**+** プラスボタンは、変数コンテンツをサポートするフィールドにのみ表示されます。