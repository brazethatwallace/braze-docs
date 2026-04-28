---
nav_title: カラープロファイルとCSSテンプレート
article_title: カラープロファイルとCSSテンプレート
page_order: 3
page_type: reference
description: "この記事では、アプリ内メッセージのカラープロファイルとCSSテンプレートの概要を説明します。"
channel:
  - in-app messages
---

# カラープロファイルとCSSテンプレート {#reusable-color-profiles}

> ダッシュボードでアプリ内メッセージやブラウザ内メッセージのテンプレートを保存して、自分のスタイルを使用した新しいCampaignsやメッセージを素早く作成できます。この記事は[従来のエディター]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/)に適用されます。ドラッグ＆ドロップエディターを使用している場合は、代わりに[スタイル設定]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings/)を参照してください。

**テンプレート** > **アプリ内メッセージテンプレート**に移動します。

このページから、既存のテンプレートを編集するか、**+ 作成**をクリックして**カラープロファイル**または**CSSテンプレート**を選択し、アプリ内メッセージで使用する新しいテンプレートを作成できます。

## カラープロファイル {#color-profile}

HEXカラーコードを入力するか、色付きのボックスをクリックしてカラーピッカーで色を選択することで、メッセージテンプレートの配色をカスタマイズできます。

完了したら**カラープロファイルを保存**をクリックします。

### カラープロファイルの管理 {#managing-color-profiles}

テンプレートを[複製]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/)したり[アーカイブ]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/)したりすることもできます。テンプレートやクリエイティブコンテンツの作成と管理の詳細については、[テンプレートとメディア]({{site.baseurl}}/user_guide/messaging/templates/)を参照してください。

## CSSテンプレート {#in-app-message-templates}

[WebモーダルIn-App Messages](#web-modal-css)用の完全なCSSテンプレートをカスタマイズできます。

CSSテンプレートに名前とタグを付け、デフォルトテンプレートにするかどうかを選択します。用意されたスペースに独自のCSSを記述できます。このスペースにはメッセージプレビューに表示されるCSSがあらかじめ入力されており、ニーズに合わせて自由に調整できます。

```css
.ab-message-header, .ab-message-text {
  color: #333333;
  text-align: center;
}

.ab-message-header {
  font-size: 20px;
  font-weight: bold;
}

.ab-message-text {
  font-size: 14px;
  font-weight: normal;
}

.ab-close-button svg {
  fill: #9b9b9b;
}

.ab-message-button {
  border: 1px solid #1b78cf;
  font-size: 14px;
  font-weight: bold;
}
.ab-message-button:first-of-type {
  background-color: white;
  color: #1b78cf;
}
.ab-message-button:last-of-type, .ab-message-button:first-of-type:last-of-type {
  background-color: #1b78cf;
  color: white;
}

.ab-background {
  background-color: white;
}

.ab-icon {
  background-color: #0073d5;
  color: white;
}

.ab-page-blocker {
  background-color: rgba(51, 51, 51, .75);
}
```

ご覧のとおり、背景色からフォントサイズ、ウェイトなど、あらゆる要素を編集できます。

### CSSテンプレートの管理 {#managing-css-templates}

テンプレートを[複製]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/)したり[アーカイブ]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/)したりすることもできます。テンプレートやクリエイティブコンテンツの作成と管理の詳細については、[テンプレートとメディア]({{site.baseurl}}/user_guide/messaging/templates/)を参照してください。

## CSS付きモーダル（Webのみ） {#web-modal-css}

Web専用のCSS付きWebモーダルメッセージを使用する場合、独自のテンプレートを適用するか、用意されたスペースに独自のCSSを記述できます。このスペースにはメッセージプレビューに表示されるCSSがあらかじめ入力されていますが、ニーズに合わせて自由に調整できます。

独自のテンプレートを適用する場合は、**テンプレートを適用**をクリックし、アプリ内メッセージテンプレートギャラリーから選択します。オプションがない場合は、CSSテンプレートビルダーを使用して[CSSテンプレート]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/color_profiles_and_css_templates/#in-app-message-templates)をアップロードできます。