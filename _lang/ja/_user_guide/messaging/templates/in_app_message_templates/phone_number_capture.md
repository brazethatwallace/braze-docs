---
nav_title: SMS、RCS、WhatsApp登録フォーム
article_title: SMS、RCS、WhatsApp登録フォーム
alias: "/phone_number_capture/"
page_order: 2
description: "このページでは、アプリ内メッセージのドラッグ＆ドロップエディターを使用してSMS、RCS、WhatsApp登録フォームを作成する方法について説明します。"
---

# SMS、RCS、WhatsApp登録フォーム {#sms-rcs-and-whatsapp-sign-up-form}

> SMS、RCS、WhatsApp登録フォームは、アプリ内メッセージ用のドラッグ＆ドロップエディターで利用できるテンプレートです。これらのテンプレートを使用して、ユーザーの電話番号を収集し、SMS、MMS、RCS、WhatsAppサブスクリプショングループを拡大できます。

![電話番号登録フォームテンプレートを使用して作成されたアプリ内メッセージの3つの例。]({% image_buster /assets/img_archive/dnd_iam_phone_capture_example2.png %})

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## 電話番号登録フォームの作成 {#creating-a-phone-number-sign-up-form}

### ステップ 1:テンプレートを選択する {#step-1-choose-your-template}

ドラッグ＆ドロップのアプリ内メッセージを作成する際、テンプレートとして**SMS sign-up**（RCS登録にも対応）または**WhatsApp sign-up**を選択し、**Build message**を選択します。これらのテンプレートは、モバイルアプリとWebブラウザの両方でサポートされています。

![アプリ内メッセージ作成時にSMS sign-upまたはWhatsApp sign-upをテンプレートとして選択するモーダル。]({% image_buster /assets/img_archive/dnd_iam_phone_capture_template.png %}){: style="max-width:80%"}

### ステップ 2:メッセージスタイルを設定する {#step-2-set-up-your-message-styles}

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

![カスタムフォントのアップロードと選択のワークフロー。]({% image_buster /assets/img_archive/dnd_iam_phone_capture_custom_font.gif %})

### ステップ 3:電話番号入力コンポーネントをカスタマイズする {#step-3-customize-your-phone-number-input-component}

登録フォームの作成を開始するには、エディターで電話番号入力コンポーネントを選択します。

![電話番号入力コンポーネントが選択された状態の登録フォーム作成時のプレビューエリア。]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%"}

サイドメニューから、このテンプレートで電話番号を収集するサブスクリプショングループを指定します。コンプライアンスのベストプラクティスに従い、1つの電話番号登録フォームにつき1つのサブスクリプショングループへの同意のみ収集できます。ただし、必要に応じて複数のフォームを使用して、他のサブスクリプショングループへの同意を収集できます。

![サブスクリプショングループが選択されたサブスクリプショングループのドロップダウン。]({% image_buster /assets/img_archive/dnd_iam_phone_capture_subscription.png %}){: style="max-width:40%"}

デフォルトではグローバルに番号を収集しますが、番号を収集する国を制限することもできます。これは、特定の国の電話番号を持つユーザーにのみメッセージを送信する場合に便利で、リストのクリーンさを維持するのに役立ちます。これを行うには、**Collect numbers from all countries**をオフにし、ドロップダウンを使用して特定の国を選択します。ユーザーは、明示的に追加した国のみ選択できます。

![番号を収集する国を選択するための国のドロップダウン。]({% image_buster /assets/img_archive/dnd_iam_phone_capture_countries.png %}){: style="max-width:40%"}

#### 無効な電話番号 {#invalid-phone-numbers}

ユーザーが許可されていない特殊文字を含む電話番号を入力した場合、カスタマイズ不可の汎用エラーインジケーターが表示され、フォームを送信できません。**Preview & Test**タブおよびテストデバイスでエラーの動作を確認できます。Brazeが電話番号をどのようにフォーマットするかについては、[こちらの記事]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers/#importing-phone-numbers)を参照してください。

### ステップ 4:免責事項の文言を追加する（SMSおよびRCS登録フォームの場合） {#step-4-add-disclaimer-language-for-sms-and-rcs-sign-up-forms}

SMSおよびRCS登録フォームでは、送信するSMSまたはRCSの種類を明確に伝えることが重要です。フォームに以下の情報を含めることで、リスト拡大がコンプライアンスに準拠していることを確認してください。

- 顧客が受け取ることが予想されるSMSおよびRCSメッセージの種類の説明（カートリマインダー、プロモーションや特典、予約リマインダーなど）。すべてのユースケースを列挙する必要はありませんが、ブランドが送信するメッセージの種類の説明を提供する必要があります。
- 同意が購入の条件ではないことの注記（該当する場合）。
- メッセージの頻度、およびメッセージ料金とデータ料金が適用されることのリマインダー。正確なメッセージ頻度がわからない場合は、頻度が変動する可能性があると記載できます。
- 利用規約およびSMS・RCSプライバシーポリシーへのリンク。
- ヘルプおよびオプトアウトキーワードのリマインダー（ヘルプはHELP、キャンセルはSTOP）。

テンプレートには例としてのみプレースホルダーの免責事項を提供しています。これは法的助言を構成するものではなく、コンプライアンス目的で依拠すべきものではありません。お客様のブランドに合わせた文言を作成するために、法務チームと協力することが重要です。

{% alert note %}
このドキュメントは法的助言を提供することを意図しておらず、法的助言として完全に依拠することはできません。
{% endalert %}

SMSおよびRCSのコンプライアンスの詳細については、[SMS、MMS、RCSに関する法律と規制]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations/)を参照してください。

### ステップ 5:メッセージのスタイルを設定する {#step-5-style-your-message}

ドラッグ＆ドロップの[アプリ内メッセージコンポーネント]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings/#message-components)を使用して、メッセージの外観をカスタマイズします。

## 結果の分析 {#analyzing-the-results}

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

![アプリ内メッセージの各リンクのクリック数を表示するアプリ内メッセージパフォーマンスパネル。]({% image_buster /assets/img_archive/dnd_iam_phone_capture_analytics.png %})