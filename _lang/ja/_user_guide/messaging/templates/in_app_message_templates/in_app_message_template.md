---
nav_title: アプリ内メッセージテンプレートの作成
article_title: アプリ内メッセージテンプレートの作成
page_order: 0
description: "このリファレンス記事では、Brazeダッシュボードのテンプレートセクションからアプリ内メッセージテンプレートを作成、保存、管理する方法について説明します。従来のエディター用のカラープロファイルやCSSテンプレートについても解説します。"
tool:
  - Templates
channel:
  - in-app messages
search_rank: 1
---

# アプリ内メッセージテンプレートの作成 {#create-an-in-app-message-template}

> **コンテンツ** > **アプリ内メッセージ**を使用して、アプリ内メッセージやブラウザ内メッセージのレイアウトの再利用可能なライブラリーを構築できます。ドラッグ＆ドロップエディターからデザインを保存したり、[従来のエディター]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional)用の**カラープロファイル**や**CSSテンプレート**アセットを作成したりできます。

## ステップ 1:アプリ内メッセージテンプレートを開く {#step-1-open-in-app-message-templates}

Brazeダッシュボードで、**コンテンツ** > **アプリ内メッセージ**に移動します。

## ステップ 2:テンプレートの作成方法を選択する {#step-2-choose-how-to-create-a-template}

テンプレートの追加方法は目的によって異なります。

| 目的 | 操作 |
|------|------|
| ドラッグ＆ドロップレイアウトを再利用のために保存する | [ドラッグ＆ドロップのアプリ内メッセージ作成画面]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)で、エディターを終了した後に**テンプレートとして保存**を選択します（先にキャンペーンを起動するか、下書きとして保存する必要があります）。テンプレートは**テンプレート** > **アプリ内メッセージテンプレート**に表示され、次のメッセージで使用できます。 |
| カラープロファイルまたはCSSテンプレートを作成する（従来のエディター） | **アプリ内メッセージテンプレート**ページで、**+ 作成**を選択し、**カラープロファイル**または**CSSテンプレート**を選択します。詳細については、[カラープロファイルとCSSテンプレート](#reusable-color-profiles)を参照してください。 |
| Brazeテンプレートをカスタマイズする | ドラッグ＆ドロップエディターで[アプリ内メッセージを作成]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)し、Brazeテンプレートを選択してカスタマイズを行い、**テンプレートとして保存**を選択します。各Brazeテンプレートの説明については、[アプリ内メッセージテンプレート]({{site.baseurl}}/user_guide/messaging/templates/in_app_message_templates)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ 2:テンプレートの作成方法を選択する" }

{% alert note %}
カラープロファイルとCSSテンプレートは従来のエディターに適用されます。ドラッグ＆ドロップエディターを使用している場合は、メッセージレベルのスタイリングに[スタイル設定]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings)を使用してください。
{% endalert %}

## ステップ 3:テンプレートを管理する {#step-3-manage-your-templates}

**コンテンツ** > **アプリ内メッセージ**で、テンプレートのフィルタリング、検索、または編集のために開くことができます。他のテンプレートタイプと同様に、テンプレートを[複製]({{site.baseurl}}/user_guide/messaging/templates/managing_templates#duplicate-templates)したり[アーカイブ]({{site.baseurl}}/user_guide/messaging/templates/managing_templates#archive-templates)したりできます。テンプレートとメディアのワークフローの概要については、[テンプレート]({{site.baseurl}}/user_guide/messaging/templates)を参照してください。

アプリ内メッセージテンプレートにアクセスするには、アプリ内メッセージテンプレートの表示または編集を行うための[ユーザー権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)が必要です。

### カラープロファイルとCSSテンプレートの作成 {#reusable-color-profiles}

{% alert note %}
以下のオプションは[従来のエディター]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional)に適用されます。ドラッグ＆ドロップエディターを使用している場合は、代わりに[スタイル設定]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings)を使用してください。
{% endalert %}

既存のテンプレートを編集するか、**+ 作成**を選択して**カラープロファイル**または**CSSテンプレート**を選択し、アプリ内メッセージ用の新しいテンプレートを作成できます。

#### カラープロファイル {#color-profile}

メッセージテンプレートの配色は、HEXカラーコードを入力するか、色付きのボックスを選択してカラーピッカーで色を選択することでカスタマイズできます。従来のエディターで新しいアプリ内メッセージを作成する際にこのプロファイルをデフォルトで適用したい場合は、**デフォルトプロファイルとして使用**を選択します。

完了したら**カラープロファイルを保存**を選択します。

![アプリ内メッセージのカラープロファイルテンプレートエディター。]({% image_buster /assets/img/drag_and_drop/templates/color_profile_template.png %})

#### CSSテンプレート {#in-app-message-templates}

[WebモーダルのCSS](#web-modal-css)用に完全なCSSテンプレートをカスタマイズできます。

CSSテンプレートに名前を付けてタグを設定し、デフォルトテンプレートにするかどうかを選択します。用意されたスペースに独自のCSSを記述できます。このスペースにはメッセージプレビューに表示されるCSSがあらかじめ入力されており、必要に応じて調整できます。

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

背景色からフォントサイズ、太さなど、すべてを編集できます。

#### CSSを使用したモーダル（Webのみ） {#web-modal-css}

Web専用のCSS付きWebモーダルメッセージを使用する場合、独自のテンプレートを適用するか、用意されたスペースに独自のCSSを記述できます。このスペースにはメッセージプレビューに表示されるCSSがあらかじめ入力されていますが、必要に応じて調整できます。

独自のテンプレートを適用する場合は、**テンプレートを適用**を選択し、アプリ内メッセージテンプレートギャラリーから選択します。オプションがない場合は、**テンプレート** > **アプリ内メッセージテンプレート**のCSSテンプレートビルダーを使用して[CSSテンプレート](#in-app-message-templates)を追加できます。