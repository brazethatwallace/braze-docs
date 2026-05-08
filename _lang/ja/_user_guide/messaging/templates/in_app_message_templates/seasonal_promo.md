---
nav_title: 背景画像付き季節プロモーション
article_title: 背景画像付き季節プロモーション
alias: "/seasonal_promotion/"
page_order: 9
description: "このページでは、アプリ内メッセージのドラッグ＆ドロップエディターを使用して、季節限定のオファーやセールをプロモーションし、ユーザーエンゲージメントを促進する方法について説明します。"
---

# 背景画像付き季節プロモーション {#seasonal-promotion-with-background-image}

> アプリ内メッセージのドラッグ＆ドロップエディターを使用して、季節限定のオファーやセールをプロモーションし、ユーザーエンゲージメントを促進します。

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## 背景画像付き季節プロモーションの作成 {#creating-a-seasonal-promotion-with-a-background-image}

### ステップ 1: テンプレートを選択する {#step-1-choose-your-template}

ドラッグ＆ドロップのアプリ内メッセージを作成する際に、テンプレートとして**Seasonal promotion with background image**を選択し、**Build message**を選択します。このテンプレートはモバイルアプリとWebブラウザの両方に対応しています。

![季節プロモーション用テンプレートが表示されたアプリ内メッセージエディター。]({% image_buster /assets/img/drag_and_drop/templates/seasonal_promo.png %})

### ステップ 2: メッセージスタイルを設定する {#step-2-set-up-your-message-styles}

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### ステップ 3: ボタンコンポーネントをカスタマイズする {#step-3-customize-your-button-component}

季節プロモーションの作成を開始するには、エディターでボタンコンポーネントを選択します。次に、サイドメニューを使用して、ユーザーがボタンを選択したときの遷移先を設定します。テンプレートのデフォルトではメッセージを閉じる設定になっていますが、アプリ内の特定のページ（プロモーション対象の製品ページなど）に遷移するよう変更できます。

![ボタン要素をカスタマイズするためのサイドメニューが表示されたアプリ内メッセージエディター。]({% image_buster /assets/img/drag_and_drop/templates/seasonal_promo_button.png %})

また、**Pages**セクションで季節プロモーションにメッセージを追加し、それらをリンクして順次フローを作成することもできます。たとえば、製品の機能を簡単に説明する一連のメッセージを作成し、最後にユーザーを製品ページに誘導するボタンを配置できます。その方法については、[ページを接続する]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/?tab=adding%20pages#step-3a-connect-pages-together)をご覧ください。

### ステップ 4: メッセージのスタイルを設定する {#step-4-style-your-message}

ドラッグ＆ドロップの[アプリ内メッセージコンポーネント]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings/#message-components)を使用して、季節プロモーションの外観をカスタマイズします。**Message container**メニューでデフォルトの背景画像URLを置き換えて独自の背景画像を追加するか、URLを削除して[メディアライブラリ]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/)から画像を選択します。

![背景画像を選択するためのサイドメニューが表示されたアプリ内メッセージエディター。]({% image_buster /assets/img/drag_and_drop/templates/seasonal_promo_image.png %})

## 結果の分析 {#analyzing-the-results}

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}