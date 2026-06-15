## バナーエディターブロック {#banner-editor-blocks}

バナーコンポーザーでは、**ビルド**セクションから行やブロックをキャンバスにドラッグしてメッセージをレイアウトします。**スタイル**を選択してページレベルのスタイリングを調整するか、ブロックまたは行を選択してサイドパネルでプロパティを編集します。

バナー作成の完全なフローについては、[バナーを作成する]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#compose-a-banner)を参照してください。

バナーコンポーザーは、他のドラッグ＆ドロップサーフェスと同じ種類のレイアウトブロックを提供しますが、完全なフォームブロックセットには対応していません（例えば、ラジオボタン、ショートテキスト、ドロップダウン、チェックボックスブロックはありません）。**電話番号キャプチャ**と**メールキャプチャ**ブロックを追加できます。メッセージごとに電話番号キャプチャとメールキャプチャブロックはそれぞれ**1つ**のみ許可されています。

### タイトルと段落 {#title-and-paragraph}

リッチテキストオプション付きの見出しまたは本文テキストを追加します。

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### ボタン {#button}

クリック可能なボタンを追加します。プロパティパネルでリンクと分析オプションを設定できます。

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### クリック時の動作 {#on-click-behavior}

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

詳細については、バナーの記事の[クリック時の動作を定義する]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#step-32-define-on-click-behavior-optional)を参照してください。

### 画像 {#image}

ホストされたURLから画像を表示します。プロパティパネルで表示オプションを設定します。

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

#### クリック時の動作

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### リンク {#link}

ユーザーが選択できるハイパーリンクを挿入します。

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### クリック時の動作

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### スペーサー {#spacer}

ブロック間に垂直方向のスペースを追加します。

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### カスタムコード {#custom-code}

高度なレイアウトや埋め込みコンテンツ（例えば動画）用のカスタムHTMLを挿入します。カスタムHTML内のクリックは、`brazeBridge.logClick()` を呼び出さない限りトラッキングされません。詳細については、[バナーのカスタムコードとJavaScriptブリッジ]({{site.baseurl}}/user_guide/channels/banners/custom_code/)を参照してください。

| プロパティ | 説明 |
| --- | --- |
| カスタムコード | バナー用のHTML（および関連アセット）を追加または編集します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom code" }

### 電話番号キャプチャ {#phone-capture}

電話番号を収集します。送信時に、選択した[SMS]({{site.baseurl}}/sms_rcs_subscription_groups/)または[WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups/)サブスクリプショングループにユーザーを登録します。バナーごとに1つのみ使用できます。

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### メールキャプチャ {#email-capture}

メールアドレスを収集し、送信時にユーザーのBrazeプロファイルに追加します。バナーごとに1つのみ使用できます。

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### ロングテキスト {#long-text}

調査スタイルのフロー用の複数行テキストフィールドです。このブロックが表示されない場合は、[Brazeサポート]({{site.baseurl}}/user_guide/administer/personal/braze_support/)またはBrazeカスタマーサクセスマネージャーにお問い合わせください。

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### 保存済み行 {#saved-row}

以前ドラッグ＆ドロップのContent Blockとして保存した再利用可能な行を挿入します。保存済み行は元のContent Blockに**リンクされていません**。元のContent Blockが更新された場合、最新バージョンを取得するにはエディターに再度ドラッグする必要があります。詳細については、[Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/)を参照してください。**行**の下に**保存済み行**が表示されない場合は、[Brazeサポート]({{site.baseurl}}/user_guide/administer/personal/braze_support/)またはBrazeカスタマーサクセスマネージャーにお問い合わせください。
-->

## 知っておくべきこと {#things-to-know}

- **動画:** 標準コンポーザーには専用の動画ブロックは含まれていません。必要に応じて**カスタムコード**を使用してプレーヤーを埋め込んでください。詳細については、[バナー：よくある質問]({{site.baseurl}}/user_guide/channels/banners/faq/)を参照してください。
- **Liquid:** ほとんどのLiquidがサポートされていますが、カタログの再レンダリングタグなど一部例外があります。詳細については、[バナー：よくある質問]({{site.baseurl}}/user_guide/channels/banners/faq/)を参照してください。