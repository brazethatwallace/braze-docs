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

> WhatsApp テンプレートビルダーを使用すると、BrazeとMeta Business Managerを切り替えることなく、Braze内で直接WhatsAppメッセージテンプレートを作成して送信できます。Metaがテンプレートを承認した後は、必要な数のキャンペーンやキャンバスで使用できます。

## 前提条件 {#prerequisites}

{% multi_lang_include whatsapp/template_prerequisites.md %}

## テンプレートを作成する {#create-a-template}

### ステップ1:WhatsAppテンプレートに移動する {#step-1-go-to-whatsapp-templates}

**コンテンツ** > **テンプレート** > **WhatsApp** に移動し、**新しいテンプレートを作成** を選択します。

![新しいテンプレートを作成するボタンがあるWhatsAppテンプレートページ。]({% image_buster /assets/img/whatsapp/templates/create_whatsapp_template.png %})

### ステップ2:テンプレート設定を構成する {#step-2-configure-template-settings}

以下のフィールドを入力します。

| フィールド | 説明 |
| ----- | ----- |
| **アカウント** | テンプレートを送信するWhatsApp Businessアカウント（WABA）。WABA内のすべての購読グループと電話番号がテンプレートへのアクセスを共有します。 |
| **言語** | このテンプレートの言語。WhatsAppでは言語ごとに個別のテンプレートが必要です。 |
| **テンプレート名** | テンプレートの一意の名前。テンプレート名には小文字、数字、アンダースコアのみ使用できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ2:テンプレート設定を構成する" }

### ステップ3:レイアウトを選択する {#step-3-choose-a-layout}

**レイアウト** で、テンプレートタイプを選択します。

- **デフォルト:** 標準的なWhatsAppメッセージ。この記事で説明するレイアウトです。
- **カルーセル:** 水平方向にスクロール可能なカードを含むメッセージ。詳細については、[カルーセルテンプレート]({{site.baseurl}}/whatsapp_carousel_templates)を参照してください。

### ステップ4:テンプレートを作成する {#step-4-build-your-template}

#### ヘッダー（オプション） {#header-optional}

メッセージ本文の前に表示されるヘッダーを追加します。以下から選択できます。

- **テキスト:** 短いテキストヘッダー。
- **メディア:** 画像、動画、またはドキュメント（URLのみ）。Brazeはメディア参照を保存し、承認のためにサンプルをMetaに送信します。
- **なし:** ヘッダーなし

#### 本文 {#body}

メッセージのメインコンテンツを入力し、Liquidまたは汎用変数を使用して本文を必要に応じてパーソナライズします。

{% raw %}
- Liquidタグを使用します（例：`{{${first_name}}}`）。Brazeはお客様のLiquidを保存し、キャンペーンやキャンバスの作成画面でテンプレートを使用する際に表示します。
- 後でメッセージ作成時にパーソナライゼーションを追加したい場合は、番号付きプレースホルダー（例：`{{1}}`）などの汎用変数を使用します。
{% endraw %}

**+** プラスボタンが表示される場所にパーソナライゼーションを追加できます。すべてのフィールドがパーソナライゼーションに対応しているわけではありません。

#### Liquidの文字数制限 {#liquid-character-limits}

Metaは、承認のために送信するテンプレート構造に文字数制限を適用します（例：本文は1,024文字、テキストヘッダーは60文字）。テンプレートビルダーでは、これらの制限はMetaに送信されるテンプレートに適用され、送信時の最終レンダリングメッセージには適用されません。

- **{% raw %}`{{ }}`{% endraw %} 変数:** Brazeは長さをチェックする前にLiquid変数を番号付きプレースホルダー（{% raw %}`{{1}}`、`{{2}}`{% endraw %}）に変換します。{% raw %}`{{${first_name}}}`{% endraw %}のような長い式は、完全なLiquid構文ではなく短いプレースホルダーとしてカウントされます。
- **{% raw %}`{% %}`{% endraw %} タグ:** Liquidロジックタグは完全な長さでリテラルテキストとしてカウントされ、テンプレートメッセージでは編集不可のコピーとして表示されます。

複雑なパーソナライゼーションの場合は、[コンテキストステップ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties)を使用して値を計算し、テンプレートで短い変数を参照します。メッセージエクストラと条件付きロジックの制約については、[WhatsAppテンプレートビルダーでのLiquid]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder/template_builder_liquid)を参照してください。

#### フッター（オプション） {#footer-optional}

メッセージ本文の後に表示される短いフッターを追加します。

#### ボタン（オプション） {#buttons-optional}

テンプレートに最大10個のボタンを追加できます。ボタンタイプにはそれぞれ異なるカテゴリと仕様があります。

| ボタンタイプ | カテゴリ | 仕様 |
| --- | --- | --- |
| クイック返信 | クイック返信ボタン |{::nomarkdown}<ul><li><b>最大数:</b> 10</li><li><b>ボタンテキスト:</b> 最大25文字</li></ul> {:/}|
| 電話番号 | コールトゥアクションボタン | {::nomarkdown}<ul><li><b>最大数:</b> 1</li><li><b>ボタンテキスト:</b> 最大25文字</li><li><b>電話番号:</b> 国コード付きの有効な電話番号（+なし、例：「14155552671」）</li></ul> {:/}|
| Webサイトにアクセス | コールトゥアクションボタン | {::nomarkdown}<ul><li><b>最大数:</b> 2</li><li><b>ボタンテキスト:</b> 最大25文字</li><li><b>WebサイトURL:</b> 最大2,000文字</li></ul> {:/}|
| オファーコードをコピー | コールトゥアクションボタン | {::nomarkdown}<ul><li><b>最大数:</b> 1</li><li><b>ボタンテキスト:</b>「Copy offer code」（編集不可）</li><li><b>オファーコード:</b> 最大15文字</li></ul> {:/}|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ボタン（オプション）" }

![クイック返信ボタンとコールトゥアクションボタンを含むWhatsAppテンプレート作成画面。]({% image_buster /assets/img/whatsapp/templates/buttons.png %})

### ステップ5:テンプレートをプレビューする {#step-5-preview-your-template}

送信前に、受信者にメッセージがどのように表示されるかをプレビューします。

- **ユーザーとしてプレビュー:** メッセージの汎用プレビューを表示します。
- **特定のユーザーとしてプレビュー:** ユーザープロファイルを選択して、そのユーザーのデータでテンプレートがどのようにレンダリングされるかをプレビューします。

### ステップ6:審査に送信する {#step-6-submit-for-review}

**送信** を選択して、テンプレートをMetaの審査に送信します。審査は通常数分で完了しますが、最大24時間かかる場合があります。テンプレートは送信されると **WhatsAppテンプレート** ページに表示され、**WhatsAppテンプレート** ページを更新するとステータスが更新されます。

## サポートされているテンプレートカテゴリー {#supported-template-categories}

現在、WhatsApp テンプレートビルダーではマーケティングテンプレートのみがサポートされています。

## 承認済みテンプレートをキャンペーンで使用する {#use-an-approved-template-in-a-campaign}

Meta がテンプレートを承認した後、WhatsApp キャンペーンまたはキャンバスで使用できます。

1. **キャンペーン**に移動し、**キャンペーンを作成** > **WhatsApp** を選択します。
2. メッセージ作成画面で、承認済みテンプレートを選択します。
3. Braze はテンプレートのコンテンツ（テンプレート作成時に入力したメディアや Liquid を含む）を自動的に入力するため、再入力する必要はありません。
4. 必要に応じて、変数コンテンツやパーソナライゼーションを更新します。Meta によってロックされたフィールド（グレーで表示）は編集できません。ロックされたコンテンツを変更するには、テンプレートを編集して承認のために再送信する必要があります。
5. **テスト**タブを使用してメッセージをプレビューし、本文の変数を更新し、送信前にメッセージが期待どおりに表示されることを確認します。

WhatsApp キャンペーンの作成について詳しくは、[WhatsApp メッセージを作成する]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message)を参照してください。

## よくある質問 {#frequently-asked-questions}

### Meta のテンプレート審査にはどのくらい時間がかかりますか？ {#how-long-does-meta-template-review-take}

審査は通常5分以内に完了しますが、最大24時間かかる場合があります。

### 承認後にテンプレートを編集できますか？ {#can-i-edit-a-template-after-its-been-approved}

キャンペーンやキャンバスを作成する際に、変数コンテンツやパーソナライゼーションを更新できます。ロックされたコンテンツ（本文コピー、ボタンレイアウト、その他の Meta が管理するフィールド）を変更するには、テンプレートビルダーで新しいテンプレートを作成するか、Meta の WhatsApp Manager でテンプレートを編集し、Meta の再承認を待つ必要があります。[クリックトラッキング]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/click_tracking)を使用している場合は、Braze で作成したテンプレートを Meta の WhatsApp Manager で編集する前に、その記事を参照してください。

### テンプレートビルダーが利用可能になる前に送信したテンプレートはどうなりますか？ {#what-happens-to-templates-i-submitted-before-the-template-builder-was-available}

Meta Business Manager で作成されたテンプレートは、引き続き Braze で使用できます。テンプレートビルダーは、Braze ダッシュボードを離れることなくテンプレートを作成・管理するための追加の方法です。

### すべてのフィールドにパーソナライゼーションを追加できないのはなぜですか？ {#why-cant-i-add-personalization-to-every-field}

Meta はテンプレートのどの部分をパーソナライズできるかを制限しています。**+** プラスボタンは、変数コンテンツをサポートするフィールドにのみ表示されます。