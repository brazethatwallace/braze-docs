---
nav_title: メールサインアップフォーム
article_title: メールサインアップフォーム
alias: "/email_capture/"
page_order: 3
description: "このページでは、アプリ内メッセージのドラッグ＆ドロップエディターを使用してメールサインアップフォームを作成する方法について説明します。"
---

# メールサインアップフォーム {#email-sign-up-form}

> ドラッグ＆ドロップのメールサインアップアプリ内メッセージテンプレートを使用して、ユーザーのメールアドレスを収集し、サブスクリプショングループを拡大できます。

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## メールサインアップフォームの作成 {#creating-an-email-sign-up-form}

### ステップ 1:テンプレートを選択する {#step-1-choose-your-template}

ドラッグ＆ドロップのアプリ内メッセージを作成する際に、テンプレートとして**Email sign-up**を選択し、**Build message**を選択します。このテンプレートは、モバイルアプリとWebブラウザの両方でサポートされています。

![メールキャプチャフォームのテンプレートが表示されたアプリ内メッセージエディター。]({% image_buster /assets/img/drag_and_drop/templates/email_capture_template1.png %})

### ステップ 2:メッセージスタイルを設定する {#step-2-set-up-your-message-styles}

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### ステップ 3:メールサインアップコンポーネントをカスタマイズする {#step-3-customize-your-email-sign-up-component}

メールサインアップフォームの作成を開始するには、エディターでメールキャプチャ要素を選択します。デフォルトでは、収集されたメールアドレスにはグローバルサブスクリプショングループの**Subscribed**が設定されます。特定のサブスクリプショングループにユーザーをオプトインさせるには、[メールサブスクリプション状態の更新]({{site.baseurl}}/user_guide/channels/email/subscriptions/#updating-email-subscription-states)を参照してください。

メールキャプチャ要素のプレースホルダーテキストとラベルテキストをカスタマイズできます。

![メールキャプチャ要素をカスタマイズするためのサイドメニューが表示されたアプリ内メッセージエディター。]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field1.png %})

#### メールバリデーション {#email-validation}

ユーザーが許可されていない特殊文字を含むメールアドレスを入力した場合、一般的なエラーインジケーターが表示され、フォームを送信できません。このエラーメッセージはカスタマイズできません。エラーの動作は**Preview & Test**タブおよびテストデバイスで確認できます。Brazeがメールアドレスをどのようにフォーマットするかについて詳しくは、[メールバリデーション]({{site.baseurl}}/user_guide/channels/email/email_setup/email_validation/)を参照してください。

### ステップ 4:免責事項の文言を追加する（オプション） {#step-4-add-disclaimer-language-optional}

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### ステップ 5:メッセージをスタイリングする {#step-5-style-your-message}

ドラッグ＆ドロップの[アプリ内メッセージコンポーネント]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings/#message-components)を使用して、サインアップフォームの外観をカスタマイズします。

## 結果の分析 {#analyzing-the-results}

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## ベストプラクティス {#best-practices}

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}