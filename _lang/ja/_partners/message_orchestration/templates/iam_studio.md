---
nav_title: IAM Studio
article_title: IAM Studio
description: "このリファレンス記事では、BrazeとIAM Studioのパートナーシップについて説明します。IAM Studioは、パーソナライズされたリッチなアプリ内エクスペリエンスを作成し、Brazeを通じて配信できるメッセージパーソナライゼーションプラットフォームです。"
alias: /partners/iam_studio/
page_type: partner
search_tag: Partner

---

# IAM Studio

> [IAM Studio](https://www.inappmessage.com)は、パーソナライズされたリッチなアプリ内エクスペリエンスを作成し、Brazeを通じて配信できる、ノーコードのメッセージパーソナライゼーションプラットフォームです。

*この統合はIAM Studioによって管理されています。*

## 統合について {#about-the-integration}

BrazeとIAM Studioの統合により、カスタマイズ可能なアプリ内メッセージテンプレートをBrazeのアプリ内メッセージに簡単に挿入できます。画像の置き換え、テキストの変更、ディープリンク設定、カスタム属性、イベント設定が利用可能です。IAM Studioを使用すると、メッセージの作成時間を短縮し、コンテンツ計画により多くの時間を費やすことができます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| IAM Studioアカウント | このパートナーシップを活用するには、[IAM Studioアカウント](https://www.inappmessage.com/register)が必要です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## ユースケース {#use-cases}

- 商品の購入促進
- ユーザー情報の収集
- 会員登録の増加
- クーポン発行情報

## 統合 {#integration}

### ステップ1:テンプレートの選択 {#step-1-choose-a-template}

アプリ内メッセージテンプレートギャラリーから使用するアプリ内メッセージテンプレートを選択します。

![IAM Studioテンプレートギャラリーに「carousel slide modal」、「simple icon modal」、「modal full image」など、さまざまなテンプレートが表示されている。]({% image_buster /assets/img/iam_studio/iam_template_gallery.png %})

### ステップ2:テンプレートのカスタマイズ {#step-2-customize-the-template}

まず、コンテンツの画像、テキスト、ボタンをカスタマイズします。画像とボタンには必ず**Deeplink**を接続してください。

{% tabs local %}
{% tab Image %}
![画像をカスタマイズするオプションが表示されているIAM StudioのUI。これらのオプションには、画像、画像の角丸、画像の暗転が含まれます。]({% image_buster /assets/img/iam_studio/iam_customize_image.png %})
{% endtab %}
{% tab Text %}
![メッセージのタイトルとサブタイトルをカスタマイズするオプションが表示されているIAM StudioのUI。これらのオプションには、テキスト、フォーマット、フォントが含まれます。]({% image_buster /assets/img/iam_studio/iam_customize_text.png %})
{% endtab %}
{% tab Button %}
![メイン、左、右のボタンをカスタマイズするオプションが表示されているIAM StudioのUI。これらのオプションには、カラー、ディープリンク、テキスト、フォーマットが含まれます。]({% image_buster /assets/img/iam_studio/iam_customize_button.png %})
{% endtab %}
{% endtabs %}

次に、カスタムフォントを追加し、Liquidタグを使用して、パーソナライズされたアプリ内メッセージを作成します。ログとトラッキングを有効にするには、**Log data and track user behavior**を選択します。

{% tabs local %}
{% tab Fonts %}
![Liquidを追加するオプションが表示されているIAM StudioのUI。これらのオプションには、パーソナライズされた文章の作成が含まれます。]({% image_buster /assets/img/iam_studio/iam_custom_font.png %})
{% endtab %}
{% tab Liquid %}
![イベント/属性のロギングをカスタマイズするオプションが表示されているIAM StudioのUI。これらのオプションには、ユーザー行動ログが含まれます。]({% image_buster /assets/img/iam_studio/iam_liquid.png %})
{% endtab %}
{% tab Logging and Tracking %}
![フォントをカスタマイズするオプションが表示されているIAM StudioのUI。これらのオプションには、ユーザーがフォントスタイルをカスタマイズできる機能が含まれます。]({% image_buster /assets/img/iam_studio/iam_tracking_logging.png  %})
{% endtab %}
{% endtabs %}

### ステップ3:テンプレートのエクスポート {#step-3-export-the-template}

すべての編集が完了したら、**Export**をクリックしてテンプレートをエクスポートします。エクスポート後、アプリ内メッセージのHTMLコードが生成されます。**Copy code**ボタンをクリックして、このコードをコピーします。

![]({% image_buster /assets/img/iam_studio/export_iam_code.png %}){: style="max-width:45%;"}

### ステップ4:Brazeでのコードの使用 {#step-4-use-code-in-braze}

Brazeに移動し、アプリ内メッセージの**HTML Input**ボックスにカスタムコードを貼り付けます。メッセージが正しく表示されることを確認するために、必ずテストを行ってください。

![]({% image_buster /assets/img/iam_studio/braze_campaign_editor.png %}){: style="max-width:85%;"}