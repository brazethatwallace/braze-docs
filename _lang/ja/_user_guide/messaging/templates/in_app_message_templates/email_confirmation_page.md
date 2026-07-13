---
nav_title: 確認付きメールサインアップ
article_title: 確認ページ付きメールサインアップ
alias: "/email_confirmation_page/"
page_order: 7
description: "このページでは、アプリ内メッセージのドラッグ＆ドロップエディターを使用して、確認ページ付きのメールサインアップフォームを作成する方法について説明します。"
---

# 確認ページ付きメールサインアップ {#email-sign-up-with-confirmation-page}

> アプリ内メッセージのドラッグ＆ドロップエディターを使用して、確認ページ付きのメールサインアップフォームを作成します。

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## 確認ページ付きメールサインアップフォームの作成 {#creating-an-email-sign-up-form-with-a-confirmation-page}

### ステップ 1:テンプレートを選択する {#step-1-choose-your-template}

ドラッグ＆ドロップのアプリ内メッセージを作成する際、テンプレートとして**Email sign-up with confirmation page**を選択し、**Build message**を選択します。このテンプレートは、モバイルアプリとWebブラウザの両方でサポートされています。

![確認ページ付きメールサインアップフォームのテンプレートが表示されたアプリ内メッセージエディター。]({% image_buster /assets/img/drag_and_drop/templates/email_capture_confirmation.png %})

### ステップ 2:メッセージスタイルを設定する {#step-2-set-up-your-message-styles}

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### ステップ 3:メールサインアップコンポーネントをカスタマイズする {#step-3-customize-your-email-sign-up-component}

メールサインアップフォームの作成を開始するには、エディターでメールキャプチャ要素を選択します。デフォルトでは、収集されたメールアドレスにはグローバルサブスクリプショングループ**Subscribed**が設定されます。特定のサブスクリプショングループにユーザーをオプトインさせるには、[メールサブスクリプション状態の更新]({{site.baseurl}}/user_guide/channels/email/subscriptions#updating-email-subscription-states)を参照してください。

メールキャプチャ要素のプレースホルダーテキストとラベルテキストをカスタマイズできます。

![メールキャプチャ要素をカスタマイズするためのサイドメニューが表示されたアプリ内メッセージエディター。]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field_confirmation.png %})

#### メールバリデーション {#email-validation}

{% multi_lang_include drag_and_drop/templates.md section='email validation' %}

### ステップ 4:免責事項の文言を追加する（オプション） {#step-4-add-disclaimer-language-optional}

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### ステップ 5:メッセージのスタイルを設定する {#step-5-style-your-message}

ドラッグ＆ドロップの[アプリ内メッセージコンポーネント]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings#message-components)を使用して、メールサインアップフォームと確認ページの外観をカスタマイズします。

## 結果の分析 {#analyzing-the-results}

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## ベストプラクティス {#best-practices}

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}