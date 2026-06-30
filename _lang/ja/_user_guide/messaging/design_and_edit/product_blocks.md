---
nav_title: 製品ブロック
article_title: ドラッグ＆ドロップ製品ブロック
page_order: 5
description: "このリファレンス記事では、ドラッグ＆ドロップ製品ブロックについて説明します。この機能により、カタログアイテムのダイナミックまたは静的なショーケースをすばやく追加・設定できます。"
tool:
    - Campaigns
    - Canvas
alias: /dnd_product_blocks/
---

# ドラッグ＆ドロップ製品ブロック {#drag-and-drop-product-blocks}

> ドラッグ＆ドロップエディターを使用すると、カスタムLiquidコードを作成することなく、メッセージに製品ブロックをすばやく追加・設定して、シームレスな製品ショーケースを実現できます。

{% alert important %}
ドラッグ＆ドロップ製品ブロック機能は早期アクセス段階にあり、現在はメールでのみ利用可能です。早期アクセスへの参加をご希望の場合は、Brazeアカウントマネージャーにお問い合わせください。
{% endalert %}

## 要件 {#requirements}

| 要件 | 説明 |
| --- | --- |
| eコマース推奨イベント | [eコマース推奨イベント]({{site.baseurl}}/ecommerce_events)は、注文の前後に発生する主要な行動イベントに対して標準化されたデータスキーマを提供します。これらのイベントは、最終的にレガシーのBraze購入イベントに代わり、コマース関連の行動をトラッキングするための標準となります。<br><br> eコマース推奨イベントは、ダイナミック製品ブロックに必須です。 |
| eコマースCanvasテンプレート | eコマース推奨イベントは、閲覧放棄、カート放棄、注文確認などの重要なユースケース向けに設計されたeコマースCanvasテンプレートを含む、事前構築済みテンプレートをサポートしています。<br><br>[eコマースCanvasテンプレート]({{site.baseurl}}/ecommerce_use_cases)を使用してこれらの重要なeコマースユースケースを実装する場合は、提供されたCanvasテンプレートを使用するか、それに従う必要があります。 |
| Brazeカタログ | 製品ブロックの設定で使用する以下のフィールドを含むBrazeカタログを作成する必要があります。{::nomarkdown}<code><ul><li>product_title</li><li>product_url</li><li>variant_image_url</li></ul></code>{:/} |
| カタログセレクション | 静的製品ブロックの場合、製品ブロックに含める製品を指定するために[カタログセレクション]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)を作成する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="要件" }

## ドラッグ＆ドロップ製品ブロックの種類 {#types-of-drag-and-drop-product-blocks}

| 製品ブロック | 目的 | ユースケース | 利用可能状況 |
| --- | --- | --- | --- |
| ダイナミック | [eコマース推奨イベント]({{site.baseurl}}/ecommerce_events)とカタログを[eコマースCanvasテンプレート]({{site.baseurl}}/ecommerce_use_cases)内で使用して、顧客のインタラクションに基づいた製品ショーケースでメッセージングをパーソナライズします。 | {::nomarkdown}<ul><li>閲覧放棄</li><li>カート放棄</li><li>チェックアウト放棄</li><li>注文確認</li></ul>{:/} | Canvasでのみ利用可能です。 |
| 静的 | Brazeカタログに保存されたデータを使用して製品をパーソナライズします。含める製品を指定するには、[カタログセレクション]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)を使用する必要があります。 | 新製品の発売やカテゴリ別のオファーを紹介するのに最適です。| |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="ドラッグ＆ドロップ製品ブロックの種類" }

## 製品ブロックのコンテンツ設定 {#product-block-content-configuration}

各ブロックタイプには異なるコンテンツ設定があります。

### 製品フィールド {#product-fields}

**Product Fields**セクションで、製品ブロックタイプを選択し、各製品に含めたいフィールドをオンに切り替えます。各フィールドは、選択した製品ブロックのタイプに基づいて異なるソースから取得されます。

#### ダイナミック製品ブロック {#dynamic-product-block}

| 製品フィールド | ソース |
| --- | --- |
| バリアント画像 | カタログ |
| 製品タイトル | カタログ |
| 製品URLボタン | カタログ |
| 価格 | eコマース推奨イベントプロパティ|
| 数量 | eコマース推奨イベントプロパティ|
{: .reset-td-br-1 .reset-td-br-2 aria-label="ダイナミック製品ブロック" }

![ダイナミック製品ブロックの製品フィールド。カタログデータとイベントデータに分かれています]({% image_buster /assets/img/product_blocks/dynamic_fields.png %}){: style="max-width:50%;"}

#### 静的製品ブロック {#static-product-block}

| 製品フィールド | ソース |
| --- | --- |
| バリアント画像 | カタログ |
| 製品タイトル | カタログ |
| 製品URLボタン | カタログ |
| 価格 | カタログ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="静的製品ブロック" }

![静的製品ブロックの製品フィールド。すべてカタログデータとして分類されています。]({% image_buster /assets/img/product_blocks/static_fields.png %}){: style="max-width:50%;"}

### レイアウトオプション {#layout-options}

レイアウトオプションを使用して、製品ブロック内での製品の表示方法をカスタマイズします。

| オプション | 説明 |
| --- | --- |
| 製品の向き | ブロック内の画像と製品フィールドの向きを選択します。 |
| 配置 | ブロック内のテキストフィールドとボタンの配置を調整します。 |
| 1行あたりの最大製品数 | 1行あたり最大3つの製品を表示できます。静的製品ブロックでは合計最大12製品、ダイナミック製品ブロックでは合計最大24製品まで表示できます。 |
| 製品間のスペース | 製品間のスペースを設定します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="レイアウトオプション" }

![製品の向き、配置、1行あたりの最大製品数、製品間のスペースのレイアウトオプション。]({% image_buster /assets/img/product_blocks/layout_options.png %}){: style="max-width:50%;"}

### グローバルメールスタイル設定 {#global-email-style-settings}

[グローバルメールスタイル設定]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings)を使用すると、Braze内のメールに一貫したスタイルを適用できます。これにより、フォント、色、ボタンデザインなどの特定のスタイルを定義し、すべてのメールに自動的に適用できます。

#### グローバルメールスタイル設定と製品ブロックの連携 {#how-global-email-style-settings-work-with-product-blocks}

段落とボタンの既存のスタイルは、製品ブロック内のテキストおよびボタン要素に自動的に適用されます。これにより、段落やボタンに設定した書式が製品ブロックでも一貫して使用され、メール全体で統一感のある外観が維持されます。

## 製品ブロックの設定 {#setting-up-product-blocks}

### カタログの設定 {#catalog-setup}

{% alert important %}
BrazeとShopifyの統合を[製品同期]({{site.baseurl}}/shopify_catalogs)に使用している場合、ドラッグ＆ドロップ製品ブロックを使用するための追加手順は必要ありません。<br><br>製品バリアント情報がない場合は、イベントペイロードとカタログの両方で、製品フィールドと製品バリアントフィールドの両方にトップレベルの製品情報を複製する必要があります。つまり、製品ブロックが正しく機能するように、両方の識別子に同じ製品詳細を提供して一貫性を維持する必要があります。
{% endalert %}

ドラッグ＆ドロップ製品ブロックを使用するには、特定のフィールド値を含むBrazeカタログを設定する必要があります。これらのフィールドは製品ブロックの設定で使用します。カタログに以下のフィールドが含まれていることを確認してください。

| フィールド | 説明 |
| --- | --- |
| `product_title` | 製品のタイトルです。|
| `product_url` | 顧客が製品を閲覧または購入できるURLです。 |
| `variant_image_url` | バリアント画像のURLです。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="カタログの設定" }

必須フィールドを含むこの[サンプル製品カタログ](/docs/assets/download_file/ecommerce_product_catalog_sample.csv)を活用して、すばやく開始できます。

![必須フィールドとその他のフィールドを含むサンプルCSVファイル。]({% image_buster /assets/img/ecommerce/sample_product_catalog.png %})

#### カタログフィールドへのマッピング {#mapping-to-catalog-fields}

カタログの**設定**タブで、**Product blocks**トグルを選択して、カタログ内の特定のフィールドと情報にマッピングできます。これにより、製品タイトル、製品URL、画像URLとして使用するフィールドを選択できます。Shopifyカタログのフィールドはデフォルトでマッピングされており、変更できません。

{% alert note %}
Shopifyを使用していない場合は、アカウントマネージャーに連絡してフィールドマッピングを有効にしてもらうことができます。これにより、任意のカタログを製品ブロックに接続し、そのフィールドを`product_title`、`product_url`、`variant_image_url`にマッピングできます。
{% endalert %}

## 製品ブロックの作成 {#creating-product-blocks}

このガイドでは、メールのドラッグ＆ドロップエディターを使用して、ダイナミックまたは静的な製品ブロックを作成、テスト、および機能を確認する手順を説明します。

### ステップ1: メールCampaignまたはメールCanvasステップを作成する {#step-1-create-an-email-campaign-or-email-canvas-step}

#### ダイナミック製品ブロック

{% alert note %}
ダイナミック製品ブロックには[eコマース推奨イベント]({{site.baseurl}}/ecommerce_events)が必要であり、[Canvases]({{site.baseurl}}/ecommerce_use_cases)内でのみ使用できます。Braze Shopifyユーザーの場合、これらのイベントは統合の一部として自動的に含まれます。Shopify以外のユーザーの場合は、開発者と協力してこれらのイベントをBrazeに渡し、イベント内のプライマリ製品識別子がカタログアイテムIDとして追加されていることを確認する必要があります。
{% endalert %}

特定のユースケースに対応する利用可能なBrazeテンプレートのいずれかを使用して、新しいCanvasを作成します。
- 閲覧放棄
- カート放棄
- チェックアウト放棄
- 注文確認

eコマースCanvasの作成に関する詳細な手順については、[eコマースユースケース]({{site.baseurl}}/ecommerce_use_cases)を参照してください。

#### 静的製品ブロック

ドラッグ＆ドロップのメールCampaign、アクションベースのCanvas、またはドラッグ＆ドロップのメールメッセージステップを持つテンプレートを作成します。

### ステップ2: 製品ブロックを追加する {#step-2-add-a-product-block}

{% tabs %}
{% tab ダイナミック製品ブロック %}

メッセージステップ内で、ドラッグ＆ドロップメールコンポーザーを使用してメールを作成するか、既存のテンプレートを変更します。
製品ブロックをメールメッセージにドラッグします。
ダイナミックブロックタイプが選択されていることを確認します。
パーソナライゼーションに使用する製品カタログを選択します。ターゲットとしているインバウンドイベントの製品と一致していることを確認してください。

{% endtab %}
{% tab 静的製品ブロック %}

製品ブロックをメールメッセージにドラッグし、静的ブロックタイプを選択します。
製品ブロックに使用するカタログを選択します。製品ブロックに表示する製品を指定するために、カタログセレクションを選択する必要があります。

{% endtab %}
{% endtabs %}

![製品ブロックなどのエディターブロックを含む「コンテンツ」タブ。]({% image_buster /assets/img/product_blocks/product_block.png %}){: style="max-width:40%;"}

### ステップ3: 製品フィールドを設定する {#step-3-configure-product-fields}

製品ブロックに表示する[製品フィールド](#product-fields)を選択します。変更のたびに**Apply Settings**を選択して、エディターで更新を確認してください。

Liquidタグの前のテキストをカスタマイズすることもできます。たとえば、アイテムの価格の前にドル記号（$）を追加したり、数量の用語を「amount」やその他の好みのラベルに変更したりできます。

![アイテムの価格の前にドル記号が追加された製品ブロック。]({% image_buster /assets/img/product_blocks/liquid.png %}){: style="max-width:45%;"}

### ステップ4: レイアウト設定を構成する {#step-4-configure-layout-settings}

[レイアウトオプション](#layout-options)を変更して、製品ブロック内での製品の表示方法を更新します。変更のたびに**Apply settings**を選択してください。

### ステップ5: メッセージをプレビューしてテストする {#step-5-preview-and-test-your-message}

{% tabs %}
{% tab ダイナミック製品ブロック %}

1. **Preview & Test**セクションで、カスタムユーザーとしてメッセージをプレビューします。
2. プレビューでレンダリングするアイテム数を指定します。
3. 正しい数のアイテムが表示され、レイアウトオプションが正しく適用されていることを確認します。表示されるアイテムはランダムに選択されることに注意してください。

![「ユーザーとしてプレビュー」タブ。「ダイナミック製品ブロック」ドロップダウンセクションで4アイテムの表示が指定されています。]({% image_buster /assets/img/product_blocks/preview_as_a_user.png %}){: style="max-width:40%;"}

{% endtab %}
{% tab 静的製品ブロック %}

製品ブロックに変更を適用すると、ドラッグ＆ドロップコンポーザー内でプレビューが生成されます。

![異なるアイテムタイルを含む生成された製品ブロックを表示するメールのドラッグ＆ドロップコンポーザー。]({% image_buster /assets/img/product_blocks/static_block_preview.png %})

{% endtab %}
{% endtabs %}

メッセージの作成が完了し、期待どおりの表示であることを確認したら、送信の準備は完了です！