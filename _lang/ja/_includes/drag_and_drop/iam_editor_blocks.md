## アプリ内メッセージエディターブロック {#in-app-message-editor-blocks}

エディターブロックは、アプリ内メッセージの**Build**セクションにあります。ブロックを列にドラッグすると、列の幅に自動調整されます。ブロックを選択すると、右側のパネルで設定を編集できます。

**ドラッグ＆ドロップエディター**でアプリ内メッセージを作成する方法の詳細については、[ドラッグ＆ドロップでアプリ内メッセージを作成する]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/)を参照してください。

### タイトルとパラグラフ {#title-and-paragraph}

メッセージにタイトルまたはパラグラフテキストを追加します。

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### ボタン {#button}

スタイル、リンク、分析を設定可能な標準ボタンを追加します。

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### クリック時の動作 {#on-click-behavior}

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

### ラジオボタン {#radio-button}

ユーザーが1つ選択できるオプションのリストを追加します。送信されると、ユーザープロファイルに関連する[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/)が記録されます。保存するには文字列である必要があります。他のデータタイプのカスタム属性はユーザープロファイルに保存されません。

{% multi_lang_include drag_and_drop/editor_block_properties/radio_button_properties.md %}

### 画像 {#image}

[メディアライブラリ]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/)から画像を挿入します。

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

画像の仕様については、[アプリ内メッセージの画像仕様]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications/#in-app-messages)を参照してください。

#### クリック時の動作

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### リンク {#link}

ユーザーがクリックして指定したURLに移動できるハイパーリンクを挿入します。テキスト内に埋め込むことも、スタンドアロンで使用することもできます。

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### クリック時の動作

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### スペーサー {#spacer}

他のブロックの間にスペースまたはパディングを追加します。

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### カスタムコード {#custom-code}

高度なカスタマイズのために、カスタムHTML、CSS、またはJavaScriptを挿入します。

| プロパティ | 説明 |
| --- | --- |
| カスタムコード | アプリ内メッセージのHTML、CSS、JavaScriptを追加、編集、削除できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom code" }

### 電話キャプチャ {#phone-capture}

電話番号のフォームフィールドを挿入します。送信されると、ユーザーは[SMS]({{site.baseurl}}/sms_rcs_subscription_groups/)または[WhatsAppサブスクリプショングループ]({{site.baseurl}}/whatsapp_subscription_groups/)に登録されます。

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### メールキャプチャ {#email-capture}

メールアドレスのフォームフィールドを挿入します。送信されると、メールアドレスがBrazeのそのユーザーのプロファイルに追加されます。

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### ショートテキスト {#short-text}

標準属性項目（名や姓など）または任意のカスタム属性文字列をサポートするフォームフィールドを挿入します。

{% multi_lang_include drag_and_drop/editor_block_properties/short_text_properties.md %}

### ドロップダウン {#dropdown}

ユーザーが1つ選択できる事前定義された項目リストを含むドロップダウンを挿入します。任意のカスタム属性文字列をリストに追加できます。

{% multi_lang_include drag_and_drop/editor_block_properties/dropdown_properties.md %}

### チェックボックス {#checkbox}

チェックボックスを挿入します。ユーザーがボックスをチェックすると、ブロックの[ブール値カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#custom-attribute-data-types)が`true`に設定されます。チェックを外したままにすると、その属性は`false`に設定されます。

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_properties.md %}

### チェックボックスグループ {#checkbox-group}

ユーザーは複数の選択肢から選択できます。値は、定義済みの[配列カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#custom-attribute-data-types)に設定されるか、追加されます。

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_group_properties.md %}

### ロングテキスト {#long-text}

調査スタイルのフロー向けの複数行テキストフィールドです。このブロックが表示されない場合は、[Brazeサポート]({{site.baseurl}}/user_guide/administer/personal/braze_support/)またはBrazeカスタマーサクセスマネージャーにお問い合わせください。

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Saved row

Inserts a reusable row you saved earlier as a drag-and-drop Content Block. Saved rows are **not linked** to the original Content Block — if the original is updated, you'll need to drag it into the editor again to get the latest version. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/). If you don't see **Saved row** under **Rows**, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support/) or your Braze customer success manager.
-->

## 知っておくべきこと {#things-to-know}

- **動画:** 標準コンポーザーには専用の動画ブロックは含まれていません。必要に応じて**カスタムコード**を使用してプレーヤーを埋め込んでください。詳細については、[アプリ内メッセージ：よくある質問]({{site.baseurl}}/user_guide/channels/in_app_messages/faq/)を参照してください。