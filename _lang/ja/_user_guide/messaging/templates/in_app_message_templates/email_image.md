---
nav_title: 画像付きメールサインアップ
article_title: バックグラウンド画像付きメールサインアップ
alias: "/email_image/"
page_order: 5
description: "このページでは、アプリ内メッセージのドラッグ＆ドロップエディターを使用して、シンプルなメッセージでブランドスタイルをアピールし、メールリストを構築する方法について説明します。"
---

# バックグラウンド画像付きメールサインアップ {#email-sign-up-with-background-image}

> アプリ内メッセージのドラッグ＆ドロップエディターを使用して、シンプルなメッセージでブランドスタイルをアピールし、メールリストを構築できます。

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## バックグラウンド画像付きメールサインアップフォームの作成 {#creating-an-email-sign-up-form-with-a-background-image}

### ステップ 1:テンプレートを選択する {#step-1-choose-your-template}

ドラッグ＆ドロップのアプリ内メッセージを作成する際に、テンプレートとして**Email sign-up with background image**を選択し、**Build message**を選択します。このテンプレートは、モバイルアプリとWebブラウザの両方でサポートされています。

![バックグラウンド画像付きメールサインアップフォームのテンプレートが表示されたアプリ内メッセージエディター。]({% image_buster /assets/img/drag_and_drop/templates/email_capture_image.png %})

### ステップ 2:メッセージスタイルを設定する {#step-2-set-up-your-message-styles}

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### ステップ 3:メールサインアップコンポーネントをカスタマイズする {#step-3-customize-your-email-sign-up-component}

メールサインアップフォームの作成を開始するには、エディターでメールキャプチャ要素を選択します。デフォルトでは、収集されたメールアドレスにはグローバルサブスクリプショングループ**Subscribed**が設定されます。ユーザーを特定のサブスクリプショングループにオプトインさせるには、[メールサブスクリプション状態の更新]({{site.baseurl}}/user_guide/channels/email/subscriptions#updating-email-subscription-states)を参照してください。

メールキャプチャ要素のプレースホルダーテキストとラベルテキストをカスタマイズできます。

![メールキャプチャ要素をカスタマイズするためのサイドメニューが表示されたアプリ内メッセージエディター。]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field_image.png %})

#### メールバリデーション {#email-validation}

{% multi_lang_include drag_and_drop/templates.md section='email validation' %}

### ステップ 4:免責事項の文言を追加する（オプション） {#step-4-add-disclaimer-language-optional}

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### ステップ 5:メッセージのスタイルを設定する {#step-5-style-your-message}

ドラッグ＆ドロップの[アプリ内メッセージコンポーネント]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings#message-components)を使用して、サインアップフォームの外観をカスタマイズします。**Message container**メニューでデフォルトのバックグラウンド画像URLを置き換えて独自のバックグラウンド画像を追加するか、URLを削除して[メディアライブラリ]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library)から画像を選択します。

## 結果の分析 {#analyzing-the-results}

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## ベストプラクティス {#best-practices}

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}