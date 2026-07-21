## ランディングページエディターブロック {#landing-page-editor-blocks}

ランディングページのエディターブロックは、**ドラッグ＆ドロップエディター**の**ビルド**セクションにあり、**行**とブロックカテゴリの下に配置されています。ブロックを行の列にドラッグすると、列幅に自動調整されます。ブロックを選択すると、右側のプロパティパネルで設定を編集できます。

ランディングページの作成と公開の詳細については、[ランディングページの作成]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)を参照してください。

### タイトルと段落 {#title-and-paragraph}

見出しまたは本文テキストを追加します。セクションの構造化や可読性の向上に役立ちます。

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### ボタン {#button}

リンクを開いたりフォームを送信したりするなどのアクション用のクリック可能な要素を追加します。

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### クリック時の動作 {#on-click-behavior}

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

{% alert important %}
**ボタンクリック時にフォームを送信**を設定し、新しいタブでWeb URLを開く場合、iOS Safariではナビゲーションがブロックされることがあります。フォーム送信時には、送信後のURLを同じタブで開いてください。詳細については、[ランディングページの作成]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)を参照してください。
{% endalert %}

### ラジオボタン {#radio-button}

ユーザーが1つを選択できるオプションのリストを追加します。プロパティパネルを使用して、利用可能なオプションと選択された値を受け取るカスタム属性を設定します。フォームが送信されると、ユーザープロファイルに選択された値が[文字列カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)として記録されます。他のデータタイプのカスタム属性はユーザープロファイルに保存されません。

{% multi_lang_include drag_and_drop/editor_block_properties/radio_button_properties.md %}

### 画像 {#image}

アップロードまたは外部URLから画像を表示します。

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

#### クリック時の動作

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### リンク {#link}

ユーザーが選択してURLに移動できるハイパーリンクを追加します。テキスト内に配置することも、単独で配置することもできます。

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### クリック時の動作

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### スペーサー {#spacer}

要素間に垂直方向のスペースを追加します。

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### カスタムコード {#custom-code}

[Google Tag Manager]({{site.baseurl}}/user_guide/messaging/landing_pages#adding-google-tag-manager-to-a-landing-page)などの高度なカスタマイズのために、カスタムHTML、CSS、またはJavaScriptを挿入します。

| プロパティ | 説明 |
| --- | --- |
| カスタムコード | HTML、CSS、JavaScriptの追加、編集、削除ができます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="カスタムコード" }

<!-- Countdown timer is not yet released. Uncomment when available.
### Countdown timer

Displays a countdown to a date and time you set. If you don't see this block, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) or your Braze customer success manager.

After you add a **Countdown timer** block, use the properties panel to set the target date and time, labels, and styling.
-->

### メールキャプチャ {#email-capture}

メールアドレス用のフォームフィールドを追加します。送信時に、アドレスはユーザーのBrazeプロファイルに保存されます。

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### 電話番号キャプチャ {#phone-capture}

電話番号用のフォームフィールドを追加します。送信時に、選択した[SMS]({{site.baseurl}}/sms_rcs_subscription_groups)または[WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups)購読グループにユーザーを登録します。

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### 入力フィールド {#input-field}

標準属性項目（名や姓など）またはカスタム属性の文字列用のフォームフィールドを追加します。

{% multi_lang_include drag_and_drop/editor_block_properties/short_text_properties.md %}

### ドロップダウン {#dropdown}

事前定義された項目のリストで、ユーザーが1つを選択します。値をカスタム属性の文字列にマッピングできます。

{% multi_lang_include drag_and_drop/editor_block_properties/dropdown_properties.md %}

### チェックボックス {#checkbox}

チェックされると、ブロックの[ブール値カスタム属性]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types)が`true`に設定され、チェックが外されると`false`に設定されます。

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_properties.md %}

### チェックボックスグループ {#checkbox-group}

ユーザーが複数のオプションを選択でき、値は定義された[配列カスタム属性]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types)に設定または追加されます。

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_group_properties.md %}

### 長文テキスト {#long-text}

調査スタイルのフロー用の複数行テキストフィールドです。このブロックが表示されない場合は、[Brazeサポート]({{site.baseurl}}/user_guide/administer/personal/braze_support)またはBrazeカスタマーサクセスマネージャーにお問い合わせください。このブロックは標準のランディングページでは使用できません。

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Saved row

Inserts a reusable row you saved earlier as a drag-and-drop Content Block. Saved rows are **not linked** to the original Content Block — if the original is updated, you'll need to drag it into the editor again to get the latest version. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks). If you don't see **Saved row** under **Rows**, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) or your Braze customer success manager.
-->

## 注意事項 {#things-to-know}

- **動画:** 標準のコンポーザーには専用の動画ブロックは含まれていません。必要に応じて**カスタムコード**を使用してプレーヤーを埋め込んでください。詳細については、[ランディングページ]({{site.baseurl}}/user_guide/messaging/landing_pages)を参照してください。